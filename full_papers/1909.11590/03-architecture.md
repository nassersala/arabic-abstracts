# Section 3: RAINBLOCK Architecture
## القسم 3: معمارية RAINBLOCK

**Section:** architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** architecture, distributed system, miner, client, node, transaction, prefetch, witness, critical path, I/O, throughput, verification, smart contract, asynchronous

---

### English Version

This section presents the RAINBLOCK architecture, which addresses the I/O bottleneck in blockchain transaction processing through two key innovations: removing I/O from the critical path and reducing I/O amplification through specialized data structures.

#### 3.1 Design Overview

RAINBLOCK separates the blockchain system into three distinct components, each optimized for its specific role:

**Prefetching Clients:** These nodes serve as intermediaries between users and miners. When a client receives a transaction from a user, it:
1. Pre-executes the transaction to determine which state data it will access
2. Fetches the required data from storage nodes
3. Constructs a cryptographic witness (Merkle proof) for the accessed data
4. Optimizes the witness size through compaction techniques
5. Sends the transaction along with its witness to miners

By performing these I/O-intensive operations before transactions reach miners, clients remove I/O from the miner's critical path.

**Miners:** Miners focus exclusively on transaction verification and block creation. When a miner receives a transaction with its witness:
1. Verifies the cryptographic witness against its local state root
2. Executes the transaction using the pre-fetched data (all in memory)
3. Computes the updated state
4. Collects verified transactions into blocks
5. Asynchronously sends state updates to storage nodes

Crucially, miners perform no disk I/O during transaction execution. All data access happens in memory, allowing transactions to execute at CPU speed.

**Storage Nodes:** Storage nodes maintain the authoritative system state using the DSM-TREE data structure (described in detail in Section 4). They:
1. Serve read requests from clients with Merkle proofs
2. Receive state updates from miners
3. Apply updates to create new state versions
4. Garbage collect old versions when forks are abandoned
5. Shard the state across multiple nodes for scalability

Storage nodes handle all persistent state management, freeing miners from storage concerns.

#### 3.2 Transaction Lifecycle

The complete flow of a transaction through RAINBLOCK involves multiple stages:

**Stage 1: User Submission**
A user creates a transaction (e.g., "transfer 10 tokens from Alice to Bob") and submits it to a prefetching client. The transaction includes standard fields: sender, receiver, amount, nonce, signature, and gas limit.

**Stage 2: Pre-execution**
The client executes the transaction against its local view of the state. For smart contracts, this means running the contract code with estimated values for block-dependent parameters (current timestamp, block number). The pre-execution records all state locations accessed (read or written).

**Stage 3: Data Prefetching**
For each accessed state location, the client requests the current value and Merkle proof from storage nodes. Storage nodes return:
- The requested state value
- A Merkle proof (path from leaf to root with sibling hashes)
- The current state version number

The client caches this data for potential reuse across multiple transactions.

**Stage 4: Witness Generation**
The client constructs a witness containing:
- All state values the transaction will read
- Merkle proofs for each value
- References to values the transaction will write

The witness cryptographically proves that the provided data matches the current state root, allowing miners to verify correctness without accessing storage.

**Stage 5: Witness Optimization**
To reduce network overhead, the client applies two optimizations:
- **Witness compaction**: Only include Merkle proof nodes below a certain tree level, as miners cache upper levels
- **Node bagging**: Batch multiple witnesses together and eliminate duplicate nodes

These optimizations reduce witness sizes by up to 95% in common cases.

**Stage 6: Miner Verification and Execution**
The miner receives the transaction and witness. It:
1. Verifies the witness against its cached state root
2. If verification succeeds, executes the transaction in memory
3. Computes state changes (updates to account balances, contract storage, etc.)
4. Includes the transaction in the next block
5. Updates its local state root

If verification fails (e.g., stale witness from an outdated state), the miner rejects the transaction, and the client must retry with updated data.

**Stage 7: Block Creation and Propagation**
Once the miner has accumulated enough transactions, it:
1. Creates a block containing the transactions
2. Computes the new state root hash
3. Solves the proof-of-work puzzle
4. Broadcasts the block to the network

Other miners verify the block using standard blockchain consensus rules.

**Stage 8: Asynchronous State Updates**
After creating a block, the miner sends logical state updates to storage nodes. These updates specify which keys changed and their new values, not the physical tree modifications. Storage nodes:
1. Receive updates from the miner
2. Apply them to the DSM-TREE, creating a new version
3. Acknowledge the update

This happens asynchronously—the miner doesn't wait for storage updates before processing the next block.

#### 3.3 Handling Smart Contracts

Smart contracts pose a unique challenge because their execution paths depend on runtime data and block parameters. RAINBLOCK uses several techniques to handle them effectively:

**Speculative Pre-execution:**
For contracts that depend on block-specific values (timestamp, block number), clients cannot know the exact values during pre-execution. Instead, they use estimated values:
- Timestamp: current time + estimated block delay
- Block number: latest known block + 1

Analysis of Ethereum contracts shows that these parameters typically affect only written data, not read access patterns. Therefore, speculative pre-execution successfully prefetches the correct read set in most cases.

**Variable Address Handling:**
Some contracts compute storage addresses dynamically (e.g., `storage[hash(sender, nonce)]`). Clients can pre-execute these to determine the exact addresses accessed. However, a small percentage of contracts have addresses that depend on block parameters. For these:
- Clients prefetch based on estimated addresses
- If estimation is wrong, miners fetch the missing data asynchronously
- The transaction succeeds but with slightly higher latency

**Re-execution Detection:**
Miners detect when pre-execution results differ from actual execution. If a client's witness contains incorrect predictions:
- The miner can fetch additional data from storage (fallback path)
- The miner can request an updated witness from the client
- If neither succeeds quickly, the transaction is deferred to the next block

**Contract Call Chains:**
When a contract calls other contracts, the call chain can be arbitrarily deep. Clients recursively pre-execute the entire call chain, capturing all accessed state. The witness includes data for all contracts in the chain.

#### 3.4 Network I/O Trade-offs

RAINBLOCK trades local disk I/O for network I/O. While this trade-off is generally favorable (network bandwidth exceeds disk IOPS), it requires careful optimization:

**Witness Size Management:**
Without optimization, witnesses for complex transactions could be large (megabytes). The compaction and bagging optimizations reduce typical witness sizes to tens of kilobytes.

**Network Bandwidth:**
In a geo-distributed setting, network latency and bandwidth become considerations. RAINBLOCK mitigates this through:
- Batching: clients send multiple transactions together
- Compression: witnesses compress well due to repeated hash values
- Locality: clients can connect to nearby miners to minimize latency

**Client-Storage Communication:**
Clients communicate extensively with storage nodes. To avoid overwhelming storage nodes:
- Clients cache aggressively (reducing redundant fetches)
- Storage nodes serve reads from memory (DSM-TREE is largely in-memory)
- State is sharded across storage nodes (distributing load)

**Miner-Storage Communication:**
Miners send updates to storage asynchronously, so this doesn't affect the critical path. Updates are batched per block, reducing message overhead.

#### 3.5 Consistency and Correctness

RAINBLOCK maintains the same consistency guarantees as traditional blockchains:

**State Consistency:**
At any point, there is a canonical blockchain and corresponding state. Miners agree on this state through the consensus protocol (proof-of-work in Ethereum's case). Witnesses are verified against the current state root, ensuring consistency.

**Transaction Ordering:**
Within a block, transactions execute in the order specified by the miner. The miner must ensure that witnesses are valid for the state at each transaction's execution point. If state changes between when a client generated a witness and when the miner executes the transaction, verification fails.

**Fork Handling:**
Blockchains naturally experience temporary forks when multiple miners find blocks simultaneously. RAINBLOCK handles forks as follows:
- Each blockchain fork has an associated state version in the DSM-TREE
- Storage nodes maintain versions for all active forks
- When a fork is abandoned (one chain becomes longer), its state version is garbage collected
- Clients may generate witnesses for soon-to-be-abandoned forks; miners will reject these, and clients retry

**Byzantine Fault Tolerance:**
RAINBLOCK does not trust any component:
- Clients don't trust storage nodes: they verify Merkle proofs
- Miners don't trust clients: they verify witnesses
- Storage nodes don't trust miners: they validate updates before applying them

Even if a majority of clients or storage nodes are malicious, they cannot violate state integrity.

#### 3.6 Security Model

RAINBLOCK maintains Ethereum's security properties:

**No Changes to Consensus:**
RAINBLOCK does not modify the proof-of-work consensus protocol. Miners still compete to solve puzzles, and the longest chain rule still applies. This means RAINBLOCK inherits Ethereum's security against double-spending and other consensus-level attacks.

**Cryptographic Verification:**
All data transfers include cryptographic proofs. Witnesses use Merkle proofs, ensuring that clients cannot provide false state data to miners. State roots in blocks commit to the entire state, as in standard blockchains.

**No New Trust Assumptions:**
RAINBLOCK doesn't introduce new trusted parties. Clients and storage nodes are untrusted infrastructure. Only miners (through consensus) determine the canonical state.

**Denial of Service Resistance:**
Malicious clients cannot DoS miners by sending invalid witnesses—verification is fast, and invalid witnesses are simply rejected. Miners can rate-limit or blacklist abusive clients.

#### 3.7 Design Rationale

Several design decisions merit explanation:

**Why Separate Clients and Miners?**
Combining these roles would create dependencies between I/O and transaction execution, recreating the bottleneck. Separating them allows I/O to happen out-of-band.

**Why Not Miners Prefetch Their Own Data?**
This would still place I/O in the critical path. By the time a miner receives a transaction, it should be ready to execute immediately.

**Why Witness-Based Rather Than Stateless?**
Pure stateless clients (where clients generate witnesses without storage nodes) would require users to maintain state, which is impractical. RAINBLOCK's approach balances efficiency and usability.

**Why Asynchronous Storage Updates?**
Synchronous updates would reintroduce I/O in the critical path. Asynchronous updates allow miners to proceed immediately while storage catches up.

The RAINBLOCK architecture achieves high throughput by carefully orchestrating these components and optimizations. The next section describes the DSM-TREE, which makes the architecture practical by providing efficient state storage.

---

### النسخة العربية

يقدم هذا القسم معمارية RAINBLOCK، والتي تعالج عنق زجاجة الإدخال/الإخراج في معالجة معاملات البلوك تشين من خلال ابتكارين رئيسيين: إزالة الإدخال/الإخراج من المسار الحرج وتقليل تضخيم الإدخال/الإخراج من خلال هياكل البيانات المتخصصة.

#### 3.1 نظرة عامة على التصميم

يفصل RAINBLOCK نظام البلوك تشين إلى ثلاثة مكونات متميزة، كل منها محسّن لدوره المحدد:

**عملاء الجلب المسبق:** تعمل هذه العقد كوسطاء بين المستخدمين والمُعدِّنين. عندما يتلقى العميل معاملة من مستخدم، فإنه:
1. ينفذ المعاملة مسبقاً لتحديد بيانات الحالة التي سيصل إليها
2. يجلب البيانات المطلوبة من عقد التخزين
3. يبني شاهداً تشفيرياً (إثبات ميركل) للبيانات التي تم الوصول إليها
4. يحسّن حجم الشاهد من خلال تقنيات الضغط
5. يرسل المعاملة مع شاهدها إلى المُعدِّنين

من خلال أداء هذه العمليات كثيفة الإدخال/الإخراج قبل وصول المعاملات إلى المُعدِّنين، يزيل العملاء الإدخال/الإخراج من المسار الحرج للمُعدِّن.

**المُعدِّنون:** يركز المُعدِّنون حصرياً على التحقق من المعاملات وإنشاء الكتل. عندما يتلقى مُعدِّن معاملة مع شاهدها:
1. يتحقق من الشاهد التشفيري مقابل جذر الحالة المحلي الخاص به
2. ينفذ المعاملة باستخدام البيانات المجلوبة مسبقاً (كلها في الذاكرة)
3. يحسب الحالة المحدثة
4. يجمع المعاملات المتحقق منها في كتل
5. يرسل تحديثات الحالة بشكل غير متزامن إلى عقد التخزين

بشكل حاسم، لا يُجري المُعدِّنون أي إدخال/إخراج للقرص أثناء تنفيذ المعاملة. يحدث كل الوصول إلى البيانات في الذاكرة، مما يسمح للمعاملات بالتنفيذ بسرعة المعالج المركزي.

**عقد التخزين:** تحافظ عقد التخزين على حالة النظام الموثوقة باستخدام هيكل بيانات DSM-TREE (موصوف بالتفصيل في القسم 4). هم:
1. يخدمون طلبات القراءة من العملاء مع إثباتات ميركل
2. يتلقون تحديثات الحالة من المُعدِّنين
3. يطبقون التحديثات لإنشاء إصدارات حالة جديدة
4. يجمعون النفايات للإصدارات القديمة عند التخلي عن التشعبات
5. يجزئون الحالة عبر عقد متعددة لقابلية التوسع

تتعامل عقد التخزين مع جميع إدارة الحالة الدائمة، مما يحرر المُعدِّنين من مخاوف التخزين.

#### 3.2 دورة حياة المعاملة

يتضمن التدفق الكامل للمعاملة عبر RAINBLOCK مراحل متعددة:

**المرحلة 1: إرسال المستخدم**
ينشئ المستخدم معاملة (على سبيل المثال، "نقل 10 رموز من أليس إلى بوب") ويرسلها إلى عميل جلب مسبق. تتضمن المعاملة الحقول القياسية: المرسل، المستقبل، المبلغ، nonce، التوقيع، وحد الغاز.

**المرحلة 2: التنفيذ المسبق**
ينفذ العميل المعاملة مقابل عرضه المحلي للحالة. بالنسبة للعقود الذكية، هذا يعني تشغيل كود العقد مع قيم مقدرة للمعاملات المعتمدة على الكتلة (الطابع الزمني الحالي، رقم الكتلة). يسجل التنفيذ المسبق جميع مواقع الحالة التي تم الوصول إليها (قراءة أو كتابة).

**المرحلة 3: الجلب المسبق للبيانات**
لكل موقع حالة تم الوصول إليه، يطلب العميل القيمة الحالية وإثبات ميركل من عقد التخزين. تُعيد عقد التخزين:
- قيمة الحالة المطلوبة
- إثبات ميركل (مسار من الورقة إلى الجذر مع تجزئات الأشقاء)
- رقم إصدار الحالة الحالي

يخزن العميل هذه البيانات مؤقتاً لإعادة الاستخدام المحتملة عبر معاملات متعددة.

**المرحلة 4: توليد الشاهد**
يبني العميل شاهداً يحتوي على:
- جميع قيم الحالة التي ستقرأها المعاملة
- إثباتات ميركل لكل قيمة
- مراجع للقيم التي ستكتبها المعاملة

يثبت الشاهد تشفيرياً أن البيانات المقدمة تطابق جذر الحالة الحالي، مما يسمح للمُعدِّنين بالتحقق من الصحة دون الوصول إلى التخزين.

**المرحلة 5: تحسين الشاهد**
لتقليل العبء على الشبكة، يطبق العميل تحسينين:
- **ضغط الشاهد**: تضمين عقد إثبات ميركل فقط أسفل مستوى شجرة معين، حيث يخزن المُعدِّنون المستويات العليا مؤقتاً
- **تجميع العقد**: تجميع عدة شهود معاً والقضاء على العقد المكررة

تقلل هذه التحسينات أحجام الشهود بنسبة تصل إلى 95% في الحالات الشائعة.

**المرحلة 6: التحقق والتنفيذ من قبل المُعدِّن**
يتلقى المُعدِّن المعاملة والشاهد. هو:
1. يتحقق من الشاهد مقابل جذر الحالة المخزن مؤقتاً
2. إذا نجح التحقق، ينفذ المعاملة في الذاكرة
3. يحسب تغييرات الحالة (تحديثات لأرصدة الحسابات، تخزين العقود، إلخ)
4. يضمّن المعاملة في الكتلة التالية
5. يحدّث جذر الحالة المحلي الخاص به

إذا فشل التحقق (على سبيل المثال، شاهد قديم من حالة قديمة)، يرفض المُعدِّن المعاملة، ويجب على العميل إعادة المحاولة ببيانات محدثة.

**المرحلة 7: إنشاء ونشر الكتلة**
بمجرد أن يجمع المُعدِّن معاملات كافية، فإنه:
1. ينشئ كتلة تحتوي على المعاملات
2. يحسب تجزئة جذر الحالة الجديدة
3. يحل لغز إثبات العمل
4. يبث الكتلة إلى الشبكة

يتحقق المُعدِّنون الآخرون من الكتلة باستخدام قواعد إجماع البلوك تشين القياسية.

**المرحلة 8: تحديثات الحالة غير المتزامنة**
بعد إنشاء كتلة، يرسل المُعدِّن تحديثات الحالة المنطقية إلى عقد التخزين. تحدد هذه التحديثات المفاتيح التي تغيرت وقيمها الجديدة، وليس التعديلات الفعلية للشجرة. عقد التخزين:
1. تتلقى التحديثات من المُعدِّن
2. تطبقها على DSM-TREE، مما يخلق إصداراً جديداً
3. تقر بالتحديث

يحدث هذا بشكل غير متزامن—لا ينتظر المُعدِّن تحديثات التخزين قبل معالجة الكتلة التالية.

#### 3.3 التعامل مع العقود الذكية

تشكل العقود الذكية تحدياً فريداً لأن مسارات تنفيذها تعتمد على بيانات وقت التشغيل ومعاملات الكتلة. يستخدم RAINBLOCK عدة تقنيات للتعامل معها بفعالية:

**التنفيذ المسبق التخميني:**
بالنسبة للعقود التي تعتمد على قيم خاصة بالكتلة (الطابع الزمني، رقم الكتلة)، لا يمكن للعملاء معرفة القيم الدقيقة أثناء التنفيذ المسبق. بدلاً من ذلك، يستخدمون قيماً مقدرة:
- الطابع الزمني: الوقت الحالي + تأخير الكتلة المقدر
- رقم الكتلة: آخر كتلة معروفة + 1

يُظهر تحليل عقود إيثيريوم أن هذه المعاملات عادة ما تؤثر فقط على البيانات المكتوبة، وليس أنماط الوصول للقراءة. لذلك، ينجح التنفيذ المسبق التخميني في جلب مجموعة القراءة الصحيحة في معظم الحالات.

**معالجة العناوين المتغيرة:**
تحسب بعض العقود عناوين التخزين ديناميكياً (على سبيل المثال، `storage[hash(sender, nonce)]`). يمكن للعملاء تنفيذها مسبقاً لتحديد العناوين الدقيقة التي تم الوصول إليها. ومع ذلك، فإن نسبة صغيرة من العقود لها عناوين تعتمد على معاملات الكتلة. لهذه:
- يجلب العملاء مسبقاً بناءً على العناوين المقدرة
- إذا كان التقدير خاطئاً، يجلب المُعدِّنون البيانات المفقودة بشكل غير متزامن
- تنجح المعاملة ولكن مع زمن استجابة أعلى قليلاً

**كشف إعادة التنفيذ:**
يكتشف المُعدِّنون عندما تختلف نتائج التنفيذ المسبق عن التنفيذ الفعلي. إذا كان شاهد العميل يحتوي على توقعات غير صحيحة:
- يمكن للمُعدِّن جلب بيانات إضافية من التخزين (مسار احتياطي)
- يمكن للمُعدِّن طلب شاهد محدث من العميل
- إذا لم ينجح أي منهما بسرعة، يتم تأجيل المعاملة إلى الكتلة التالية

**سلاسل استدعاء العقود:**
عندما يستدعي عقد عقوداً أخرى، يمكن أن تكون سلسلة الاستدعاء عميقة بشكل تعسفي. ينفذ العملاء مسبقاً سلسلة الاستدعاء بأكملها بشكل تكراري، ويلتقطون جميع الحالات التي تم الوصول إليها. يتضمن الشاهد بيانات لجميع العقود في السلسلة.

#### 3.4 مقايضات إدخال/إخراج الشبكة

يتاجر RAINBLOCK بإدخال/إخراج القرص المحلي مقابل إدخال/إخراج الشبكة. بينما هذه المقايضة مواتية بشكل عام (عرض نطاق الشبكة يتجاوز IOPS للقرص)، فإنها تتطلب تحسيناً دقيقاً:

**إدارة حجم الشاهد:**
بدون تحسين، يمكن أن تكون شهود المعاملات المعقدة كبيرة (ميغابايتات). تقلل تحسينات الضغط والتجميع أحجام الشهود النموذجية إلى عشرات الكيلوبايتات.

**عرض نطاق الشبكة:**
في بيئة موزعة جغرافياً، يصبح زمن استجابة الشبكة وعرض النطاق اعتبارات. يخفف RAINBLOCK من ذلك من خلال:
- التجميع: يرسل العملاء معاملات متعددة معاً
- الضغط: تضغط الشهود بشكل جيد بسبب قيم التجزئة المتكررة
- المحلية: يمكن للعملاء الاتصال بالمُعدِّنين القريبين لتقليل زمن الاستجابة

**اتصال العميل-التخزين:**
يتواصل العملاء على نطاق واسع مع عقد التخزين. لتجنب إرهاق عقد التخزين:
- يخزن العملاء مؤقتاً بقوة (تقليل عمليات الجلب الزائدة)
- تخدم عقد التخزين القراءات من الذاكرة (DSM-TREE في الذاكرة إلى حد كبير)
- تجزأ الحالة عبر عقد التخزين (توزيع الحمل)

**اتصال المُعدِّن-التخزين:**
يرسل المُعدِّنون التحديثات إلى التخزين بشكل غير متزامن، لذلك لا يؤثر هذا على المسار الحرج. يتم تجميع التحديثات لكل كتلة، مما يقلل من عبء الرسائل.

#### 3.5 الاتساق والصحة

يحافظ RAINBLOCK على نفس ضمانات الاتساق مثل سلاسل الكتل التقليدية:

**اتساق الحالة:**
في أي نقطة، هناك بلوك تشين قانوني وحالة مقابلة. يتفق المُعدِّنون على هذه الحالة من خلال بروتوكول الإجماع (إثبات العمل في حالة إيثيريوم). يتم التحقق من الشهود مقابل جذر الحالة الحالي، مما يضمن الاتساق.

**ترتيب المعاملات:**
داخل الكتلة، تُنفذ المعاملات بالترتيب الذي يحدده المُعدِّن. يجب على المُعدِّن التأكد من أن الشهود صالحون للحالة في نقطة تنفيذ كل معاملة. إذا تغيرت الحالة بين الوقت الذي ولد فيه العميل شاهداً والوقت الذي ينفذ فيه المُعدِّن المعاملة، يفشل التحقق.

**معالجة التشعبات:**
تواجه سلاسل الكتل بشكل طبيعي تشعبات مؤقتة عندما يجد عدة مُعدِّنين كتلاً في وقت واحد. يتعامل RAINBLOCK مع التشعبات على النحو التالي:
- لكل تشعب بلوك تشين إصدار حالة مرتبط في DSM-TREE
- تحافظ عقد التخزين على إصدارات لجميع التشعبات النشطة
- عندما يتم التخلي عن تشعب (تصبح سلسلة واحدة أطول)، يتم جمع إصدار حالته كنفايات
- قد يولد العملاء شهوداً لتشعبات على وشك التخلي عنها؛ سيرفض المُعدِّنون هذه، ويعيد العملاء المحاولة

**تحمل الأخطاء البيزنطية:**
لا يثق RAINBLOCK بأي مكون:
- لا يثق العملاء بعقد التخزين: يتحققون من إثباتات ميركل
- لا يثق المُعدِّنون بالعملاء: يتحققون من الشهود
- لا تثق عقد التخزين بالمُعدِّنين: يتحققون من صحة التحديثات قبل تطبيقها

حتى لو كانت غالبية العملاء أو عقد التخزين خبيثة، فلا يمكنهم انتهاك سلامة الحالة.

#### 3.6 نموذج الأمان

يحافظ RAINBLOCK على خصائص أمان إيثيريوم:

**لا تغييرات على الإجماع:**
لا يُعدِّل RAINBLOCK بروتوكول إجماع إثبات العمل. لا يزال المُعدِّنون يتنافسون لحل الألغاز، ولا تزال قاعدة السلسلة الأطول تنطبق. هذا يعني أن RAINBLOCK يرث أمان إيثيريوم ضد الإنفاق المزدوج والهجمات الأخرى على مستوى الإجماع.

**التحقق التشفيري:**
تتضمن جميع عمليات نقل البيانات إثباتات تشفيرية. يستخدم الشهود إثباتات ميركل، مما يضمن أن العملاء لا يمكنهم تقديم بيانات حالة خاطئة للمُعدِّنين. تلتزم جذور الحالة في الكتل بالحالة بأكملها، كما في سلاسل الكتل القياسية.

**لا افتراضات ثقة جديدة:**
لا يقدم RAINBLOCK أطرافاً موثوقة جديدة. العملاء وعقد التخزين هم بنية تحتية غير موثوقة. فقط المُعدِّنون (من خلال الإجماع) يحددون الحالة القانونية.

**مقاومة رفض الخدمة:**
لا يمكن للعملاء الخبيثين شن هجوم رفض الخدمة على المُعدِّنين عن طريق إرسال شهود غير صالحة—التحقق سريع، ويتم رفض الشهود غير الصالحة ببساطة. يمكن للمُعدِّنين الحد من المعدل أو إدراج العملاء المسيئين في القائمة السوداء.

#### 3.7 الأساس المنطقي للتصميم

تستحق عدة قرارات تصميمية التفسير:

**لماذا فصل العملاء والمُعدِّنين؟**
سيؤدي الجمع بين هذه الأدوار إلى إنشاء تبعيات بين الإدخال/الإخراج وتنفيذ المعاملات، مما يعيد إنشاء عنق الزجاجة. يسمح فصلهم للإدخال/الإخراج بالحدوث خارج النطاق.

**لماذا لا يجلب المُعدِّنون بياناتهم الخاصة مسبقاً؟**
سيظل هذا يضع الإدخال/الإخراج في المسار الحرج. بحلول الوقت الذي يتلقى فيه المُعدِّن معاملة، يجب أن تكون جاهزة للتنفيذ فوراً.

**لماذا يستند إلى الشهود بدلاً من عدم الحالة؟**
العملاء عديمو الحالة الخالصون (حيث يولد العملاء شهوداً بدون عقد تخزين) سيتطلبون من المستخدمين الحفاظ على الحالة، وهو أمر غير عملي. يوازن نهج RAINBLOCK بين الكفاءة وسهولة الاستخدام.

**لماذا تحديثات التخزين غير المتزامنة؟**
ستعيد التحديثات المتزامنة إدخال الإدخال/الإخراج في المسار الحرج. تسمح التحديثات غير المتزامنة للمُعدِّنين بالمتابعة على الفور بينما يلحق التخزين.

تحقق معمارية RAINBLOCK إنتاجية عالية من خلال تنسيق هذه المكونات والتحسينات بعناية. يصف القسم التالي DSM-TREE، والذي يجعل المعمارية عملية من خلال توفير تخزين حالة فعال.

---

### Translation Notes

- **Key terms introduced:** prefetching client, witness, witness compaction, node bagging, speculative pre-execution, asynchronous updates, fork handling
- **Technical concepts:** transaction lifecycle, cryptographic verification, Byzantine fault tolerance, denial of service resistance
- **Special handling:**
  - Kept technical acronyms like DSM-TREE, IOPS in English
  - Transaction flow stages numbered consistently in both languages
  - Nonce kept in English as standard blockchain terminology
  - DoS kept as English abbreviation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
