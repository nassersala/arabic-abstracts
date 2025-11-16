# Section 4: DSM-Tree Design
## القسم 4: تصميم DSM-TREE

**Section:** dsm-tree
**Translation Quality:** 0.86
**Glossary Terms Used:** Merkle tree, data structure, sharding, distributed, multi-versioning, hash function, pointer, node, tree traversal, serialization, garbage collection, copy-on-write

---

### English Version

The Distributed Sharded Merkle tree (DSM-TREE) is the storage layer that makes RAINBLOCK's architecture practical. This section describes the DSM-TREE design, which addresses I/O amplification through in-memory representation, lazy hashing, sharding, and multi-versioning.

#### 4.1 Design Goals

The DSM-TREE must satisfy several requirements:

**Performance:** Support high-throughput reads and writes without becoming a bottleneck. Specifically:
- Reads must serve client prefetch requests quickly (hundreds of thousands per second)
- Writes must apply miner updates efficiently without blocking reads
- Tree traversal must be fast (microseconds, not milliseconds)

**Correctness:** Provide cryptographic authentication of state through Merkle proofs. Any data returned to clients must be verifiably part of the current state.

**Scalability:** Support billions of accounts and terabytes of state by distributing across multiple storage nodes. No single node should store the entire state.

**Consistency:** Handle concurrent updates from multiple miners (due to forks) without conflicts or data corruption. Support efficient garbage collection when forks are abandoned.

**Compatibility:** Maintain compatibility with Ethereum's state representation (account model, Merkle Patricia Trie structure) so RAINBLOCK can process real Ethereum transactions.

The DSM-TREE achieves these goals through a novel combination of techniques.

#### 4.2 In-Memory Representation

Traditional blockchain storage uses hash-based node addressing: each tree node is stored with its hash as the key. Traversing from parent to child requires:
1. Computing the child's hash
2. Looking up that hash in the key-value store
3. Deserializing the retrieved node

This is expensive because:
- Hash computation requires serializing node contents
- Key-value lookups involve disk I/O or expensive memory lookups
- The process repeats for every level of the tree

**DSM-TREE Optimization:** In the DSM-TREE, tree nodes in memory are connected by pointers, not hashes. Traversing from parent to child is a simple pointer dereference—a single CPU instruction taking nanoseconds.

```
Traditional:
  parent.childHash → compute hash → KV lookup → deserialize child

DSM-TREE:
  parent.childPtr → dereference → child
```

This eliminates:
- Hash computation during traversal
- Serialization during traversal
- Key-value lookups during traversal

Reads that would take milliseconds in traditional systems take microseconds in DSM-TREE.

#### 4.3 Lazy Hash Computation

While pointer-based traversal is fast, we still need hashes for Merkle proofs and the state root. Computing all hashes eagerly (after every update) would be expensive.

**Lazy Hashing Strategy:** DSM-TREE defers hash computation until a hash is actually needed. Each node has a "dirty" flag indicating whether its hash needs recomputation. When a node is modified:
1. Mark the node and all ancestors as dirty
2. Don't compute hashes yet

When a hash is needed (for a Merkle proof or state root):
1. Check if the node is dirty
2. If dirty, recursively compute child hashes, then compute this node's hash
3. Cache the hash and mark the node clean

**Why This Works:** The key insight is that most state modifications don't require immediate hash computation. Miners update many locations, but only compute the final state root once per block. Clients request Merkle proofs for specific locations, not every location. By deferring hashing, we avoid computing hashes for intermediate states that are never queried.

**Savings:** Lazy hashing reduces hash computations by 50-80% in typical workloads. It also saves serialization operations, as computing a hash requires serializing the node contents.

#### 4.4 Sharding

A single server cannot store billions of accounts in memory. DSM-TREE distributes the tree across multiple storage nodes through sharding.

**Two-Layer Architecture:**

**Bottom Layer (Sharded):** The tree is partitioned by key prefix across storage nodes. For example, with 16 shards:
- Shard 0 stores keys starting with 0x0...
- Shard 1 stores keys starting with 0x1...
- ...
- Shard 15 stores keys starting with 0xF...

Each shard stores a subtree containing all keys with that prefix. Shards operate independently and don't communicate with each other.

**Top Layer (Replicated):** The upper levels of the tree (above the sharding point) are small and replicated on every node. This includes:
- The root node
- Nodes in the first few levels
- Any nodes above the shard split point

**Rationale:** Most tree traversals start at the root and descend to a specific leaf. By replicating the top layers, every node can route queries to the correct shard without coordination. The sharded bottom layers contain the bulk of the data but are distributed across nodes.

**Shard Configuration:** The sharding level is configurable. Deeper sharding (more levels replicated) reduces per-shard storage but increases replica overhead. Shallower sharding increases per-shard storage but reduces replication. In practice, sharding at level 4-6 works well, creating 16-64 shards.

#### 4.5 Multi-Versioning

Blockchains naturally experience forks when multiple miners create blocks simultaneously. Each fork represents an alternative version of the state. Traditional systems handle this by maintaining separate trees for each fork, which is space-inefficient.

**Copy-on-Write Versioning:** DSM-TREE uses copy-on-write (CoW) to share structure between versions. When a miner updates the state:
1. The update creates a new version
2. Modified nodes are copied; unmodified nodes are shared with the previous version
3. Each version has its own root node pointing into the tree

Multiple versions coexist efficiently because they share most of their structure. Only the nodes along the path from the modified leaves to the root are copied.

**Example:** Suppose we have version V1 with state root R1. A miner creates a block updating account A, producing version V2 with root R2. The tree for V2 shares all nodes with V1 except:
- The leaf for account A (modified)
- All ancestors of that leaf up to the root (their child pointers changed)

If the tree has depth 20, only ~20 nodes are copied. Millions of unchanged nodes are shared.

**Version Management:** Each version is identified by its block hash. Storage nodes maintain:
- A mapping from block hash to state root
- Reference counts for shared nodes
- A set of "active" versions (for current forks)

When a fork is abandoned (the blockchain converges on a single chain), versions for the abandoned fork are marked for garbage collection.

**Garbage Collection:** Periodically, storage nodes:
1. Identify versions with no references (abandoned forks)
2. Decrement reference counts for nodes in those versions
3. Delete nodes with zero references

This reclaims space while preserving nodes shared by active versions.

#### 4.6 Node Structure

A DSM-TREE node contains:

**For Internal Nodes:**
- Pointers to children (up to 16 for a hexary tree)
- Cached hash (if clean) or dirty flag
- Version information (which versions reference this node)
- Reference count (for garbage collection)

**For Leaf Nodes:**
- Key (account address or storage location)
- Value (account data or storage value)
- Cached hash or dirty flag
- Version information
- Reference count

**Compression:** To save memory, nodes use variable-length encoding:
- If a node has only one child, it's compressed into a "short node" that stores a key prefix
- Null pointers are not stored (sparse array representation)
- Values are stored inline if small, referenced if large

This compression is standard in Patricia tries and reduces memory overhead significantly.

#### 4.7 Read Operation

When a client requests data for account A:

1. **Shard Selection:** Determine which shard contains A (based on key prefix)
2. **Tree Traversal:** On the appropriate storage node, traverse from root to leaf using pointers
3. **Proof Generation:** Walk back up from leaf to root, collecting sibling hashes for the Merkle proof
4. **Lazy Hash Computation:** For any dirty nodes along the path, compute hashes on demand
5. **Response:** Return the value and Merkle proof to the client

Steps 1-2 are fast (pointer dereferences). Step 3 requires collecting hashes, which may involve lazy computation (step 4). The entire operation typically takes tens of microseconds.

**Caching:** Frequently accessed nodes and recently computed hashes are cached in memory, further accelerating reads.

#### 4.8 Write Operation

When a miner sends state updates after creating a block:

1. **Version Creation:** Create a new version V_new with the block hash
2. **Update Application:** For each modified key-value pair:
   a. Traverse to the leaf (copy-on-write: copy nodes along path)
   b. Update the leaf value
   c. Mark the leaf and all ancestors as dirty
3. **Root Update:** The copied root node becomes the root for V_new
4. **Acknowledgment:** Inform the miner that the update is complete

The miner provides logical updates (which keys changed and their new values), not physical tree operations. The storage node translates these into tree modifications.

**Batching:** Updates for an entire block are applied together as a single batch, amortizing overhead.

#### 4.9 Proof Compaction

Merkle proofs can be large for deep trees. With tree depth ~20, a proof includes ~20 sibling hashes of 32 bytes each = 640 bytes minimum. For transactions accessing many accounts, witnesses can grow to kilobytes or megabytes.

**Compaction Strategy:** RAINBLOCK assumes miners cache the top layers of the tree (above a configurable compaction level). Witnesses only include proof nodes below this level.

Example: With compaction level 10, witnesses omit the top 10 levels of the tree. Proofs start from level 10 and go to the leaf (level ~20), including ~10 sibling hashes instead of ~20. This halves proof sizes.

**Tradeoff:** Miners must cache the top layers. If the cache is evicted, proof verification requires fetching the missing nodes. In practice, the top layers are small (kilobytes to megabytes) and easily cached.

#### 4.10 Node Bagging

When a client submits multiple transactions, their witnesses may contain duplicate nodes. For example, two transactions accessing nearby accounts share most of their Merkle proof paths.

**Bagging Optimization:** The client:
1. Collects all witnesses for a batch of transactions
2. Identifies duplicate nodes (by hash)
3. Includes each unique node once, referenced by multiple witnesses

This dramatically reduces witness sizes for batched transactions. Empirically, bagging reduces total witness size by 70-95% for batches of 100+ transactions.

#### 4.11 Comparison with Traditional Merkle Trees

The DSM-TREE provides several advantages over traditional Merkle tree storage:

| Aspect | Traditional MPT | DSM-TREE |
|--------|----------------|----------|
| Traversal | Hash lookup per level (ms) | Pointer dereference (μs) |
| Hashing | Eager (on every write) | Lazy (on demand) |
| Storage | Single node (limited scale) | Sharded (distributed) |
| Versioning | Separate trees (space-intensive) | Copy-on-write (shared structure) |
| Memory usage | High (RocksDB overhead) | Low (optimized in-memory) |
| Read throughput | ~1K ops/sec | ~200K ops/sec |
| Write throughput | ~1K ops/sec | ~200K ops/sec |

The performance improvement comes from eliminating I/O operations and optimizing the in-memory data structure.

#### 4.12 Limitations and Trade-offs

DSM-TREE makes specific trade-offs:

**Memory Requirements:** The tree must fit in aggregate memory across storage nodes. For Ethereum's current state (~100M accounts, ~50GB), this requires multiple servers with hundreds of GB of RAM. As state grows, more storage nodes must be added.

**Sharding Overhead:** The replicated top layers consume memory on every storage node. Deeper sharding reduces per-shard size but increases replication overhead.

**Version Proliferation:** If forks persist for long periods, many versions accumulate. Garbage collection must run periodically to reclaim space.

**Consistency Model:** DSM-TREE provides eventual consistency for writes (asynchronous updates), but strong consistency for reads (Merkle proofs verify against committed state roots). This matches blockchain semantics, where state changes are committed in blocks.

Despite these trade-offs, the DSM-TREE's performance advantages make it essential to RAINBLOCK's high throughput.

---

### النسخة العربية

شجرة ميركل المجزأة الموزعة (DSM-TREE) هي طبقة التخزين التي تجعل معمارية RAINBLOCK عملية. يصف هذا القسم تصميم DSM-TREE، والذي يعالج تضخيم الإدخال/الإخراج من خلال التمثيل في الذاكرة، والتجزئة الكسولة، والتجزئة، والنسخ المتعددة.

#### 4.1 أهداف التصميم

يجب أن تفي DSM-TREE بعدة متطلبات:

**الأداء:** دعم القراءات والكتابات عالية الإنتاجية دون أن تصبح عنق زجاجة. على وجه التحديد:
- يجب أن تخدم القراءات طلبات الجلب المسبق للعملاء بسرعة (مئات الآلاف في الثانية)
- يجب أن تطبق الكتابات تحديثات المُعدِّنين بكفاءة دون حظر القراءات
- يجب أن يكون مرور الشجرة سريعاً (ميكروثانية، وليس ميلي ثانية)

**الصحة:** توفير المصادقة التشفيرية للحالة من خلال إثباتات ميركل. يجب أن تكون أي بيانات يتم إرجاعها إلى العملاء جزءاً قابلاً للتحقق من الحالة الحالية.

**قابلية التوسع:** دعم مليارات الحسابات وتيرابايتات من الحالة من خلال التوزيع عبر عقد تخزين متعددة. يجب ألا تخزن أي عقدة واحدة الحالة بأكملها.

**الاتساق:** معالجة التحديثات المتزامنة من عدة مُعدِّنين (بسبب التشعبات) دون تعارضات أو تلف البيانات. دعم جمع النفايات الفعال عند التخلي عن التشعبات.

**التوافق:** الحفاظ على التوافق مع تمثيل حالة إيثيريوم (نموذج الحساب، بنية شجرة ميركل باتريشيا) حتى يتمكن RAINBLOCK من معالجة معاملات إيثيريوم الحقيقية.

تحقق DSM-TREE هذه الأهداف من خلال مزيج جديد من التقنيات.

#### 4.2 التمثيل في الذاكرة

يستخدم التخزين التقليدي للبلوك تشين معالجة العقد القائمة على التجزئة: يتم تخزين كل عقدة شجرة مع تجزئتها كمفتاح. يتطلب المرور من الوالد إلى الطفل:
1. حساب تجزئة الطفل
2. البحث عن تلك التجزئة في مخزن القيم-المفاتيح
3. إلغاء تسلسل العقدة المسترجعة

هذا مكلف لأن:
- يتطلب حساب التجزئة تسلسل محتويات العقدة
- تتضمن عمليات البحث في القيم-المفاتيح إدخال/إخراج القرص أو عمليات بحث ذاكرة مكلفة
- تتكرر العملية لكل مستوى من الشجرة

**تحسين DSM-TREE:** في DSM-TREE، ترتبط عقد الشجرة في الذاكرة بالمؤشرات، وليس التجزئات. المرور من الوالد إلى الطفل هو إلغاء مرجع مؤشر بسيط—تعليمة معالج مركزي واحدة تستغرق نانوثانية.

```
التقليدي:
  parent.childHash → حساب التجزئة → بحث KV → إلغاء تسلسل الطفل

DSM-TREE:
  parent.childPtr → إلغاء المرجع → الطفل
```

هذا يزيل:
- حساب التجزئة أثناء المرور
- التسلسل أثناء المرور
- عمليات البحث في القيم-المفاتيح أثناء المرور

القراءات التي كانت ستستغرق ميلي ثانية في الأنظمة التقليدية تستغرق ميكروثانية في DSM-TREE.

#### 4.3 الحساب الكسول للتجزئة

بينما يكون المرور القائم على المؤشرات سريعاً، لا نزال بحاجة إلى تجزئات لإثباتات ميركل وجذر الحالة. سيكون حساب جميع التجزئات بشغف (بعد كل تحديث) مكلفاً.

**استراتيجية التجزئة الكسولة:** تؤجل DSM-TREE حساب التجزئة حتى تكون هناك حاجة فعلية للتجزئة. لكل عقدة علامة "متسخة" تشير إلى ما إذا كانت تجزئتها تحتاج إلى إعادة حساب. عندما يتم تعديل عقدة:
1. وضع علامة على العقدة وجميع الأسلاف كمتسخة
2. عدم حساب التجزئات بعد

عندما تكون هناك حاجة إلى تجزئة (لإثبات ميركل أو جذر الحالة):
1. التحقق مما إذا كانت العقدة متسخة
2. إذا كانت متسخة، حساب تجزئات الأطفال بشكل تكراري، ثم حساب تجزئة هذه العقدة
3. تخزين التجزئة مؤقتاً ووضع علامة على العقدة كنظيفة

**لماذا يعمل هذا:** الرؤية الأساسية هي أن معظم تعديلات الحالة لا تتطلب حساب تجزئة فوري. يحدّث المُعدِّنون العديد من المواقع، لكنهم يحسبون جذر الحالة النهائي مرة واحدة فقط لكل كتلة. يطلب العملاء إثباتات ميركل لمواقع محددة، وليس كل موقع. من خلال تأجيل التجزئة، نتجنب حساب التجزئات للحالات الوسيطة التي لا يتم الاستعلام عنها أبداً.

**التوفير:** تقلل التجزئة الكسولة حسابات التجزئة بنسبة 50-80% في أحمال العمل النموذجية. كما أنها توفر عمليات التسلسل، حيث يتطلب حساب التجزئة تسلسل محتويات العقدة.

#### 4.4 التجزئة

لا يمكن لخادم واحد تخزين مليارات الحسابات في الذاكرة. توزع DSM-TREE الشجرة عبر عقد تخزين متعددة من خلال التجزئة.

**معمارية ذات طبقتين:**

**الطبقة السفلى (مجزأة):** يتم تقسيم الشجرة حسب بادئة المفتاح عبر عقد التخزين. على سبيل المثال، مع 16 جزءاً:
- الجزء 0 يخزن المفاتيح التي تبدأ بـ 0x0...
- الجزء 1 يخزن المفاتيح التي تبدأ بـ 0x1...
- ...
- الجزء 15 يخزن المفاتيح التي تبدأ بـ 0xF...

يخزن كل جزء شجرة فرعية تحتوي على جميع المفاتيح بتلك البادئة. تعمل الأجزاء بشكل مستقل ولا تتواصل مع بعضها البعض.

**الطبقة العليا (منسوخة):** المستويات العليا من الشجرة (فوق نقطة التجزئة) صغيرة ومنسوخة على كل عقدة. يتضمن هذا:
- عقدة الجذر
- العقد في المستويات القليلة الأولى
- أي عقد فوق نقطة تقسيم الجزء

**الأساس المنطقي:** تبدأ معظم مرورات الشجرة من الجذر وتنحدر إلى ورقة محددة. من خلال نسخ الطبقات العليا، يمكن لكل عقدة توجيه الاستعلامات إلى الجزء الصحيح دون تنسيق. تحتوي الطبقات السفلى المجزأة على الجزء الأكبر من البيانات ولكنها موزعة عبر العقد.

**تكوين الجزء:** مستوى التجزئة قابل للتكوين. التجزئة الأعمق (المزيد من المستويات المنسوخة) تقلل من تخزين كل جزء ولكنها تزيد من عبء النسخ. التجزئة الأقل عمقاً تزيد من تخزين كل جزء ولكنها تقلل من النسخ. في الممارسة، التجزئة في المستوى 4-6 تعمل بشكل جيد، مما يخلق 16-64 جزءاً.

#### 4.5 النسخ المتعددة

تواجه سلاسل الكتل بشكل طبيعي تشعبات عندما ينشئ عدة مُعدِّنين كتلاً في وقت واحد. يمثل كل تشعب نسخة بديلة من الحالة. تتعامل الأنظمة التقليدية مع هذا من خلال الحفاظ على أشجار منفصلة لكل تشعب، وهو غير فعال من حيث المساحة.

**النسخ بنسخ عند الكتابة:** تستخدم DSM-TREE نسخ عند الكتابة (CoW) لمشاركة البنية بين الإصدارات. عندما يحدّث مُعدِّن الحالة:
1. ينشئ التحديث إصداراً جديداً
2. يتم نسخ العقد المعدلة؛ تتم مشاركة العقد غير المعدلة مع الإصدار السابق
3. لكل إصدار عقدة جذر خاصة به تشير إلى الشجرة

تتعايش إصدارات متعددة بكفاءة لأنها تشترك في معظم بنيتها. يتم نسخ العقد فقط على طول المسار من الأوراق المعدلة إلى الجذر.

**مثال:** لنفترض أن لدينا إصدار V1 بجذر حالة R1. ينشئ مُعدِّن كتلة تحدّث الحساب A، منتجاً إصدار V2 بجذر R2. تشترك الشجرة لـ V2 في جميع العقد مع V1 باستثناء:
- الورقة للحساب A (معدلة)
- جميع أسلاف تلك الورقة حتى الجذر (تغيرت مؤشرات أطفالهم)

إذا كان عمق الشجرة 20، يتم نسخ ~20 عقدة فقط. يتم مشاركة ملايين العقد غير المتغيرة.

**إدارة الإصدار:** يتم تحديد كل إصدار بتجزئة كتلته. تحافظ عقد التخزين على:
- تعيين من تجزئة الكتلة إلى جذر الحالة
- أعداد المراجع للعقد المشتركة
- مجموعة من الإصدارات "النشطة" (للتشعبات الحالية)

عندما يتم التخلي عن تشعب (يتقارب البلوك تشين على سلسلة واحدة)، يتم وضع علامة على إصدارات التشعب المتخلى عنه لجمع النفايات.

**جمع النفايات:** بشكل دوري، عقد التخزين:
1. تحدد الإصدارات بدون مراجع (تشعبات متخلى عنها)
2. تخفض أعداد المراجع للعقد في تلك الإصدارات
3. تحذف العقد بأعداد مراجع صفر

هذا يستعيد المساحة مع الحفاظ على العقد المشتركة بواسطة الإصدارات النشطة.

#### 4.6 بنية العقدة

تحتوي عقدة DSM-TREE على:

**للعقد الداخلية:**
- مؤشرات إلى الأطفال (حتى 16 لشجرة سداسية عشرية)
- تجزئة مخزنة مؤقتاً (إذا كانت نظيفة) أو علامة متسخة
- معلومات الإصدار (الإصدارات التي تشير إلى هذه العقدة)
- عدد المراجع (لجمع النفايات)

**للعقد الورقية:**
- المفتاح (عنوان الحساب أو موقع التخزين)
- القيمة (بيانات الحساب أو قيمة التخزين)
- تجزئة مخزنة مؤقتاً أو علامة متسخة
- معلومات الإصدار
- عدد المراجع

**الضغط:** لتوفير الذاكرة، تستخدم العقد ترميزاً متغير الطول:
- إذا كان للعقدة طفل واحد فقط، يتم ضغطها إلى "عقدة قصيرة" تخزن بادئة مفتاح
- لا يتم تخزين المؤشرات الفارغة (تمثيل مصفوفة متفرقة)
- يتم تخزين القيم مضمنة إذا كانت صغيرة، مشار إليها إذا كانت كبيرة

هذا الضغط قياسي في أشجار باتريشيا ويقلل من عبء الذاكرة بشكل كبير.

#### 4.7 عملية القراءة

عندما يطلب عميل بيانات للحساب A:

1. **اختيار الجزء:** تحديد الجزء الذي يحتوي على A (بناءً على بادئة المفتاح)
2. **مرور الشجرة:** على عقدة التخزين المناسبة، المرور من الجذر إلى الورقة باستخدام المؤشرات
3. **توليد الإثبات:** السير للخلف من الورقة إلى الجذر، جمع تجزئات الأشقاء لإثبات ميركل
4. **الحساب الكسول للتجزئة:** لأي عقد متسخة على طول المسار، حساب التجزئات عند الطلب
5. **الاستجابة:** إرجاع القيمة وإثبات ميركل إلى العميل

الخطوات 1-2 سريعة (إلغاءات مرجع المؤشرات). تتطلب الخطوة 3 جمع التجزئات، والتي قد تتضمن حساباً كسولاً (الخطوة 4). عادة ما تستغرق العملية بأكملها عشرات الميكروثانية.

**التخزين المؤقت:** يتم تخزين العقد التي يتم الوصول إليها بشكل متكرر والتجزئات المحسوبة مؤخراً مؤقتاً في الذاكرة، مما يسرع القراءات بشكل أكبر.

#### 4.8 عملية الكتابة

عندما يرسل مُعدِّن تحديثات الحالة بعد إنشاء كتلة:

1. **إنشاء الإصدار:** إنشاء إصدار جديد V_new مع تجزئة الكتلة
2. **تطبيق التحديث:** لكل زوج مفتاح-قيمة معدل:
   a. المرور إلى الورقة (نسخ عند الكتابة: نسخ العقد على طول المسار)
   b. تحديث قيمة الورقة
   c. وضع علامة على الورقة وجميع الأسلاف كمتسخة
3. **تحديث الجذر:** تصبح عقدة الجذر المنسوخة الجذر لـ V_new
4. **الإقرار:** إبلاغ المُعدِّن بأن التحديث مكتمل

يوفر المُعدِّن تحديثات منطقية (المفاتيح التي تغيرت وقيمها الجديدة)، وليس عمليات الشجرة الفعلية. تترجم عقدة التخزين هذه إلى تعديلات الشجرة.

**التجميع:** يتم تطبيق التحديثات لكتلة كاملة معاً كدفعة واحدة، مما يوزع العبء.

#### 4.9 ضغط الإثبات

يمكن أن تكون إثباتات ميركل كبيرة للأشجار العميقة. مع عمق الشجرة ~20، يتضمن الإثبات ~20 تجزئة شقيقة من 32 بايت لكل منها = 640 بايت كحد أدنى. للمعاملات التي تصل إلى حسابات عديدة، يمكن أن تنمو الشهود إلى كيلوبايتات أو ميغابايتات.

**استراتيجية الضغط:** يفترض RAINBLOCK أن المُعدِّنين يخزنون الطبقات العليا من الشجرة مؤقتاً (فوق مستوى ضغط قابل للتكوين). تتضمن الشهود فقط عقد الإثبات أسفل هذا المستوى.

مثال: مع مستوى ضغط 10، تحذف الشهود المستويات العليا العشرة من الشجرة. تبدأ الإثباتات من المستوى 10 وتذهب إلى الورقة (المستوى ~20)، بما في ذلك ~10 تجزئات شقيقة بدلاً من ~20. هذا يقلل أحجام الإثبات إلى النصف.

**المقايضة:** يجب على المُعدِّنين تخزين الطبقات العليا مؤقتاً. إذا تم إخلاء الذاكرة المؤقتة، يتطلب التحقق من الإثبات جلب العقد المفقودة. في الممارسة، الطبقات العليا صغيرة (كيلوبايتات إلى ميغابايتات) ويسهل تخزينها مؤقتاً.

#### 4.10 تجميع العقد

عندما يرسل عميل معاملات متعددة، قد تحتوي شهودهم على عقد مكررة. على سبيل المثال، تشترك معاملتان تصلان إلى حسابات قريبة في معظم مسارات إثبات ميركل الخاصة بهما.

**تحسين التجميع:** العميل:
1. يجمع جميع الشهود لدفعة من المعاملات
2. يحدد العقد المكررة (بالتجزئة)
3. يتضمن كل عقدة فريدة مرة واحدة، مشار إليها بواسطة عدة شهود

هذا يقلل بشكل كبير من أحجام الشهود للمعاملات المجمعة. تجريبياً، يقلل التجميع حجم الشاهد الكلي بنسبة 70-95% لدفعات من أكثر من 100 معاملة.

#### 4.11 المقارنة مع أشجار ميركل التقليدية

توفر DSM-TREE عدة مزايا على تخزين شجرة ميركل التقليدية:

| الجانب | MPT التقليدية | DSM-TREE |
|--------|----------------|----------|
| المرور | بحث تجزئة لكل مستوى (ms) | إلغاء مرجع المؤشر (μs) |
| التجزئة | شغوفة (في كل كتابة) | كسولة (عند الطلب) |
| التخزين | عقدة واحدة (مقياس محدود) | مجزأة (موزعة) |
| النسخ | أشجار منفصلة (كثيفة المساحة) | نسخ عند الكتابة (بنية مشتركة) |
| استخدام الذاكرة | عالي (عبء RocksDB) | منخفض (محسّن في الذاكرة) |
| إنتاجية القراءة | ~1K عملية/ثانية | ~200K عملية/ثانية |
| إنتاجية الكتابة | ~1K عملية/ثانية | ~200K عملية/ثانية |

يأتي تحسين الأداء من القضاء على عمليات الإدخال/الإخراج وتحسين هيكل البيانات في الذاكرة.

#### 4.12 القيود والمقايضات

تجري DSM-TREE مقايضات محددة:

**متطلبات الذاكرة:** يجب أن تتناسب الشجرة مع الذاكرة الإجمالية عبر عقد التخزين. بالنسبة لحالة إيثيريوم الحالية (~100 مليون حساب، ~50 جيجابايت)، يتطلب هذا خوادم متعددة بمئات جيجابايت من ذاكرة الوصول العشوائي. مع نمو الحالة، يجب إضافة المزيد من عقد التخزين.

**عبء التجزئة:** تستهلك الطبقات العليا المنسوخة الذاكرة على كل عقدة تخزين. التجزئة الأعمق تقلل من حجم كل جزء ولكنها تزيد من عبء النسخ.

**انتشار الإصدار:** إذا استمرت التشعبات لفترات طويلة، تتراكم إصدارات كثيرة. يجب تشغيل جمع النفايات بشكل دوري لاستعادة المساحة.

**نموذج الاتساق:** توفر DSM-TREE اتساقاً نهائياً للكتابات (تحديثات غير متزامنة)، ولكن اتساقاً قوياً للقراءات (إثباتات ميركل تتحقق مقابل جذور الحالة الملتزمة). هذا يطابق دلالات البلوك تشين، حيث يتم تثبيت تغييرات الحالة في الكتل.

على الرغم من هذه المقايضات، فإن مزايا أداء DSM-TREE تجعلها ضرورية لإنتاجية RAINBLOCK العالية.

---

### Translation Notes

- **Key terms introduced:** copy-on-write, lazy hashing, shard, replica, garbage collection, dirty flag, node bagging, compaction level
- **Technical concepts:** two-layer architecture, multi-versioning, reference counting, variable-length encoding, sparse array
- **Special handling:**
  - Kept DSM-TREE, CoW, MPT as English acronyms
  - Code examples preserved in English with ASCII art
  - Performance metrics in table format maintained
  - μs and ms kept as standard time unit abbreviations

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
