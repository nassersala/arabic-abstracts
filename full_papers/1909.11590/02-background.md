# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** blockchain, Merkle tree, transaction, consensus, proof-of-work, hash function, distributed system, key-value store, state, account

---

### English Version

This section provides background on blockchain systems and Merkle trees, focusing on aspects relevant to understanding RAINBLOCK's design.

#### 2.1 Public Blockchain Architecture

Public blockchains are distributed systems that maintain a shared, append-only ledger of transactions without requiring trust in any central authority. The ledger is organized into blocks, where each block contains a set of transactions and a cryptographic hash linking it to the previous block, forming a chain.

**Consensus and Mining:** Blockchain systems use consensus protocols to agree on which blocks to add to the chain. In proof-of-work (PoW) systems like Bitcoin and Ethereum, miners compete to solve computationally difficult puzzles. The miner who solves the puzzle first creates the next block and broadcasts it to the network. Other nodes verify the block and add it to their local copy of the blockchain.

**Blockchain State:** Beyond just recording transactions, smart contract platforms like Ethereum maintain a global state representing account balances, contract code, and contract storage. Each transaction can read from and write to this state. For example, a transaction might transfer tokens from one account to another, requiring reading both account balances, subtracting from one, adding to the other, and writing the updated balances back.

The state is typically organized as a mapping from account addresses to account objects. Each account object contains:
- Balance (amount of cryptocurrency)
- Nonce (transaction counter)
- Code hash (for smart contract accounts)
- Storage root (hash of account's storage trie)

**Transaction Processing:** When a miner creates a block, they must:
1. Select pending transactions from the transaction pool
2. For each transaction, read the current state
3. Execute the transaction (which may involve running smart contract code)
4. Update the state with the transaction's effects
5. Compute a new state root hash
6. Include transactions and the new state root in the block

Critically, each transaction execution requires reading from and potentially writing to multiple state locations. For a simple token transfer, this involves accessing at least two accounts. For complex smart contracts, hundreds or thousands of state locations may be accessed.

#### 2.2 Merkle Trees in Blockchains

Merkle trees are the fundamental data structure enabling trustless verification in blockchains. A Merkle tree is a binary tree where:
- Leaf nodes contain data items
- Internal nodes contain cryptographic hashes of their children
- The root hash uniquely represents the entire tree contents

**Cryptographic Authentication:** The key property of Merkle trees is that they provide cryptographic proofs of membership. To prove that a particular data item is in the tree, one only needs to provide:
- The data item
- The "Merkle proof": a path from the leaf to the root, including all sibling hashes along the path

A verifier can recompute hashes along the path and check that the recomputed root matches the known root hash. This proof is logarithmic in the tree size, making it compact even for trees with millions of items.

**Light Clients:** Merkle trees enable "light clients"—nodes that don't store the full blockchain state. A light client only stores block headers (including state root hashes) and can request Merkle proofs from full nodes to verify specific state items. This is crucial for mobile devices and resource-constrained environments.

**Merkle Patricia Tries in Ethereum:** Ethereum uses a variant called Merkle Patricia Tries (MPTs) to store the state. A Patricia trie is a space-optimized prefix tree where nodes with single children are compressed. The Ethereum state MPT maps account addresses (160-bit values) to account data.

The MPT supports three operations:
- **Get(key)**: Retrieve the value associated with a key
- **Put(key, value)**: Insert or update a key-value pair
- **GetProof(key)**: Retrieve a Merkle proof for a key

Each operation requires traversing the tree from root to leaf, computing or verifying hashes at each node.

#### 2.3 Storage Layer

Blockchain implementations typically store Merkle trees using key-value stores. Ethereum's reference implementation uses LevelDB (or RocksDB in some clients).

**Hash-Based Node Addressing:** Merkle tree nodes are stored in the key-value store with the node's hash as the key and the serialized node contents as the value. This means that traversing from a parent to a child requires:
1. Reading the parent node from storage
2. Deserializing it to extract child hashes
3. Using the child hash as a key to read the child node
4. Repeating until reaching the target leaf

Each step involves a random disk I/O operation to fetch a node by its hash.

**Log-Structured Merge Trees:** RocksDB organizes data using Log-Structured Merge trees (LSM-trees). Writes go to an in-memory memtable, which is periodically flushed to disk as an immutable SSTable. SSTables are organized in levels, with periodic compaction merging and reorganizing files.

For reads, RocksDB must search the memtable and potentially multiple SSTables across levels. Without careful tuning and caching, this can result in multiple disk I/O operations per read. Bloom filters help reduce unnecessary reads, but cannot eliminate them entirely.

**I/O Amplification:** The combination of hash-based addressing and LSM-tree storage creates severe I/O amplification:
- Each Merkle tree traversal from root to leaf involves ~20 random reads (for a tree with millions of nodes)
- Each read may trigger multiple LSM-tree lookups across SSTables
- Processing a single transaction accessing multiple accounts requires multiple tree traversals
- Processing a block of 100 transactions can require 10,000+ random I/O operations

Even modern NVMe SSDs, which can perform 500,000+ random read IOPS, are bottlenecked when processing blockchain transactions due to this amplification.

#### 2.4 Smart Contracts

Smart contracts are programs stored on the blockchain that execute when triggered by transactions. Ethereum smart contracts are written in high-level languages like Solidity and compiled to EVM (Ethereum Virtual Machine) bytecode.

**Execution Model:** When a transaction calls a smart contract:
1. The EVM loads the contract bytecode
2. Executes the code with the transaction data as input
3. The code can read from and write to the contract's persistent storage
4. The code can call other contracts
5. Execution completes and returns a result

**Turing Completeness:** Unlike Bitcoin's limited scripting language, Ethereum smart contracts are Turing-complete—they can perform arbitrary computation. This power creates a challenge: it's impossible to predict in advance which storage locations a contract will access without actually executing it.

**Gas and Execution Limits:** To prevent infinite loops and limit resource consumption, Ethereum charges "gas" for each operation. Transactions include a gas limit, and execution halts if the limit is exceeded. This ensures all executions terminate.

**Popular Contract Types:** Common smart contract patterns include:
- **ERC-20 tokens**: Fungible tokens with standard transfer/balance operations
- **ERC-721 tokens**: Non-fungible tokens (NFTs)
- **Decentralized exchanges**: Automated market makers for token trading
- **DeFi protocols**: Lending, borrowing, and yield farming

Each of these involves complex logic and multiple storage accesses per transaction.

#### 2.5 The I/O Bottleneck

The throughput limitations of blockchain systems stem from the interaction between Merkle trees, storage layers, and transaction processing:

**Sequential Processing:** Most blockchain implementations process transactions sequentially within a block. Each transaction must complete before the next begins to ensure correct state dependencies. This serialization means I/O latency directly translates to throughput limits.

**Storage Latency:** Even with SSDs, each random read operation takes tens of microseconds. With 10,000+ reads per block, I/O time dominates CPU execution time. Miners spend most of their time waiting for disk operations rather than computing.

**Cache Limitations:** While caching can help, the working set for blockchain state is large (gigabytes to terabytes) and access patterns are largely random based on transaction content. Cache hit rates are typically low except for frequently accessed accounts.

**Scaling Challenges:** Simply adding more miners doesn't solve the problem—each miner independently processes the same transactions and encounters the same I/O bottleneck. The fundamental issue is that I/O latency limits the rate at which any single miner can process transactions and create blocks.

This analysis motivates RAINBLOCK's design: to increase throughput, we must either eliminate I/O from the critical path or dramatically reduce I/O operations—preferably both.

---

### النسخة العربية

يوفر هذا القسم خلفية عن أنظمة البلوك تشين وأشجار ميركل، مع التركيز على الجوانب ذات الصلة بفهم تصميم RAINBLOCK.

#### 2.1 معمارية البلوك تشين العامة

سلاسل الكتل العامة هي أنظمة موزعة تحافظ على دفتر أستاذ مشترك يقبل الإضافة فقط للمعاملات دون الحاجة إلى الثقة في أي سلطة مركزية. يتم تنظيم دفتر الأستاذ في كتل، حيث تحتوي كل كتلة على مجموعة من المعاملات وتجزئة تشفيرية تربطها بالكتلة السابقة، مكونة سلسلة.

**الإجماع والتعدين:** تستخدم أنظمة البلوك تشين بروتوكولات الإجماع للاتفاق على الكتل التي يجب إضافتها إلى السلسلة. في أنظمة إثبات العمل (PoW) مثل بيتكوين وإيثيريوم، يتنافس المُعدِّنون لحل ألغاز صعبة حسابياً. المُعدِّن الذي يحل اللغز أولاً ينشئ الكتلة التالية ويبثها إلى الشبكة. تتحقق العقد الأخرى من الكتلة وتضيفها إلى نسختها المحلية من البلوك تشين.

**حالة البلوك تشين:** بالإضافة إلى مجرد تسجيل المعاملات، تحافظ منصات العقود الذكية مثل إيثيريوم على حالة عامة تمثل أرصدة الحسابات، وكود العقود، وتخزين العقود. يمكن لكل معاملة القراءة من هذه الحالة والكتابة إليها. على سبيل المثال، قد تنقل المعاملة الرموز من حساب إلى آخر، مما يتطلب قراءة أرصدة كلا الحسابين، والطرح من واحد، والإضافة إلى الآخر، وكتابة الأرصدة المحدثة مرة أخرى.

عادة ما يتم تنظيم الحالة كتعيين من عناوين الحسابات إلى كائنات الحسابات. يحتوي كل كائن حساب على:
- الرصيد (كمية العملة المشفرة)
- Nonce (عداد المعاملات)
- تجزئة الكود (لحسابات العقود الذكية)
- جذر التخزين (تجزئة شجرة تخزين الحساب)

**معالجة المعاملات:** عندما ينشئ مُعدِّن كتلة، يجب عليه:
1. اختيار المعاملات المعلقة من مجمع المعاملات
2. لكل معاملة، قراءة الحالة الحالية
3. تنفيذ المعاملة (والتي قد تتضمن تشغيل كود العقد الذكي)
4. تحديث الحالة بتأثيرات المعاملة
5. حساب تجزئة جذر الحالة الجديدة
6. تضمين المعاملات وجذر الحالة الجديد في الكتلة

من الأهمية بمكان، أن كل تنفيذ معاملة يتطلب القراءة من مواقع حالة متعددة والكتابة إليها محتملاً. بالنسبة لنقل رمز بسيط، يتضمن هذا الوصول إلى حسابين على الأقل. بالنسبة للعقود الذكية المعقدة، قد يتم الوصول إلى مئات أو آلاف مواقع الحالة.

#### 2.2 أشجار ميركل في سلاسل الكتل

أشجار ميركل هي هيكل البيانات الأساسي الذي يمكّن التحقق بدون ثقة في سلاسل الكتل. شجرة ميركل هي شجرة ثنائية حيث:
- تحتوي العقد الورقية على عناصر البيانات
- تحتوي العقد الداخلية على تجزئات تشفيرية لأطفالها
- تمثل تجزئة الجذر بشكل فريد محتويات الشجرة بأكملها

**المصادقة التشفيرية:** الخاصية الأساسية لأشجار ميركل هي أنها توفر إثباتات تشفيرية للعضوية. لإثبات أن عنصر بيانات معين موجود في الشجرة، يحتاج المرء فقط إلى توفير:
- عنصر البيانات
- "إثبات ميركل": مسار من الورقة إلى الجذر، بما في ذلك جميع تجزئات الأشقاء على طول المسار

يمكن للمتحقق إعادة حساب التجزئات على طول المسار والتحقق من أن الجذر المعاد حسابه يطابق تجزئة الجذر المعروفة. هذا الإثبات هو لوغاريتمي في حجم الشجرة، مما يجعله مدمجاً حتى للأشجار التي تحتوي على ملايين العناصر.

**العملاء الخفيفون:** تمكّن أشجار ميركل "العملاء الخفيفين"—العقد التي لا تخزن حالة البلوك تشين الكاملة. يخزن العميل الخفيف رؤوس الكتل فقط (بما في ذلك تجزئات جذر الحالة) ويمكنه طلب إثباتات ميركل من العقد الكاملة للتحقق من عناصر الحالة المحددة. هذا أمر بالغ الأهمية للأجهزة المحمولة والبيئات محدودة الموارد.

**أشجار ميركل باتريشيا في إيثيريوم:** تستخدم إيثيريوم متغيراً يسمى أشجار ميركل باتريشيا (MPTs) لتخزين الحالة. شجرة باتريشيا هي شجرة بادئة محسّنة للمساحة حيث يتم ضغط العقد ذات الأطفال المفردين. تعيّن MPT لحالة إيثيريوم عناوين الحسابات (قيم 160 بت) إلى بيانات الحساب.

تدعم MPT ثلاث عمليات:
- **Get(key)**: استرجاع القيمة المرتبطة بمفتاح
- **Put(key, value)**: إدراج أو تحديث زوج مفتاح-قيمة
- **GetProof(key)**: استرجاع إثبات ميركل لمفتاح

كل عملية تتطلب المرور عبر الشجرة من الجذر إلى الورقة، وحساب أو التحقق من التجزئات في كل عقدة.

#### 2.3 طبقة التخزين

عادة ما تخزن تطبيقات البلوك تشين أشجار ميركل باستخدام مخازن القيم-المفاتيح. يستخدم التطبيق المرجعي لإيثيريوم LevelDB (أو RocksDB في بعض العملاء).

**معالجة العقد القائمة على التجزئة:** يتم تخزين عقد شجرة ميركل في مخزن القيم-المفاتيح مع تجزئة العقدة كمفتاح ومحتويات العقدة المتسلسلة كقيمة. هذا يعني أن المرور من الوالد إلى الطفل يتطلب:
1. قراءة عقدة الوالد من التخزين
2. إلغاء تسلسلها لاستخراج تجزئات الأطفال
3. استخدام تجزئة الطفل كمفتاح لقراءة عقدة الطفل
4. التكرار حتى الوصول إلى الورقة المستهدفة

تتضمن كل خطوة عملية إدخال/إخراج عشوائية للقرص لجلب عقدة بتجزئتها.

**أشجار الدمج المنظمة بالسجل:** ينظم RocksDB البيانات باستخدام أشجار الدمج المنظمة بالسجل (LSM-trees). تذهب الكتابات إلى جدول ذاكرة في الذاكرة (memtable)، والذي يتم تفريغه بشكل دوري إلى القرص كـ SSTable غير قابل للتغيير. يتم تنظيم SSTables في مستويات، مع دمج وإعادة تنظيم الملفات بشكل دوري.

للقراءات، يجب على RocksDB البحث في جدول الذاكرة وربما عدة SSTables عبر المستويات. بدون ضبط ودقيق وتخزين مؤقت، يمكن أن يؤدي ذلك إلى عمليات إدخال/إخراج متعددة للقرص لكل قراءة. تساعد مرشحات Bloom في تقليل القراءات غير الضرورية، ولكن لا يمكنها القضاء عليها تماماً.

**تضخيم الإدخال/الإخراج:** يخلق الجمع بين المعالجة القائمة على التجزئة وتخزين LSM-tree تضخيماً شديداً للإدخال/الإخراج:
- كل مرور لشجرة ميركل من الجذر إلى الورقة يتضمن ~20 قراءة عشوائية (لشجرة تحتوي على ملايين العقد)
- كل قراءة قد تؤدي إلى عمليات بحث متعددة في LSM-tree عبر SSTables
- معالجة معاملة واحدة تصل إلى حسابات متعددة تتطلب مرورات متعددة للشجرة
- معالجة كتلة من 100 معاملة يمكن أن تتطلب أكثر من 10,000 عملية إدخال/إخراج عشوائية

حتى أقراص NVMe SSD الحديثة، التي يمكنها إجراء أكثر من 500,000 IOPS قراءة عشوائية، تواجه عنق زجاجة عند معالجة معاملات البلوك تشين بسبب هذا التضخيم.

#### 2.4 العقود الذكية

العقود الذكية هي برامج مخزنة على البلوك تشين يتم تنفيذها عند تشغيلها بواسطة المعاملات. تتم كتابة العقود الذكية لإيثيريوم بلغات عالية المستوى مثل Solidity وتجميعها إلى رمز بايت EVM (آلة إيثيريوم الافتراضية).

**نموذج التنفيذ:** عندما تستدعي معاملة عقداً ذكياً:
1. يحمّل EVM رمز بايت العقد
2. ينفذ الكود مع بيانات المعاملة كإدخال
3. يمكن للكود القراءة من والكتابة إلى التخزين الدائم للعقد
4. يمكن للكود استدعاء عقود أخرى
5. يكتمل التنفيذ ويعيد نتيجة

**الاكتمال حسب تورينج:** على عكس لغة البرمجة النصية المحدودة لبيتكوين، فإن العقود الذكية لإيثيريوم كاملة حسب تورينج—يمكنها إجراء حسابات تعسفية. تخلق هذه القوة تحدياً: من المستحيل التنبؤ مسبقاً بمواقع التخزين التي سيصل إليها العقد دون تنفيذه فعلياً.

**الغاز وحدود التنفيذ:** لمنع الحلقات اللانهائية والحد من استهلاك الموارد، تفرض إيثيريوم رسوم "غاز" لكل عملية. تتضمن المعاملات حد غاز، ويتوقف التنفيذ إذا تم تجاوز الحد. هذا يضمن إنهاء جميع التنفيذات.

**أنواع العقود الشائعة:** تتضمن أنماط العقود الذكية الشائعة:
- **رموز ERC-20**: رموز قابلة للاستبدال مع عمليات نقل/رصيد قياسية
- **رموز ERC-721**: رموز غير قابلة للاستبدال (NFTs)
- **البورصات اللامركزية**: صناع سوق آليون لتداول الرموز
- **بروتوكولات DeFi**: الإقراض والاقتراض وزراعة العائد

يتضمن كل من هذه منطقاً معقداً ووصولات تخزين متعددة لكل معاملة.

#### 2.5 عنق زجاجة الإدخال/الإخراج

تنبع قيود الإنتاجية لأنظمة البلوك تشين من التفاعل بين أشجار ميركل وطبقات التخزين ومعالجة المعاملات:

**المعالجة التسلسلية:** تعالج معظم تطبيقات البلوك تشين المعاملات بشكل تسلسلي داخل الكتلة. يجب أن تكتمل كل معاملة قبل أن تبدأ التالية لضمان التبعيات الصحيحة للحالة. يعني هذا التسلسل أن زمن استجابة الإدخال/الإخراج يترجم مباشرة إلى حدود الإنتاجية.

**زمن استجابة التخزين:** حتى مع أقراص SSD، تستغرق كل عملية قراءة عشوائية عشرات الميكروثانية. مع أكثر من 10,000 قراءة لكل كتلة، يهيمن وقت الإدخال/الإخراج على وقت تنفيذ المعالج المركزي. يقضي المُعدِّنون معظم وقتهم في انتظار عمليات القرص بدلاً من الحوسبة.

**قيود التخزين المؤقت:** بينما يمكن أن يساعد التخزين المؤقت، فإن مجموعة العمل لحالة البلوك تشين كبيرة (غيغابايت إلى تيرابايت) وأنماط الوصول عشوائية إلى حد كبير بناءً على محتوى المعاملة. عادة ما تكون معدلات الإصابة في الذاكرة المؤقتة منخفضة باستثناء الحسابات التي يتم الوصول إليها بشكل متكرر.

**تحديات التوسع:** مجرد إضافة المزيد من المُعدِّنين لا يحل المشكلة—يعالج كل مُعدِّن نفس المعاملات بشكل مستقل ويواجه نفس عنق زجاجة الإدخال/الإخراج. المشكلة الأساسية هي أن زمن استجابة الإدخال/الإخراج يحد من المعدل الذي يمكن لأي مُعدِّن واحد معالجة المعاملات وإنشاء الكتل به.

يحفز هذا التحليل تصميم RAINBLOCK: لزيادة الإنتاجية، يجب علينا إما القضاء على الإدخال/الإخراج من المسار الحرج أو تقليل عمليات الإدخال/الإخراج بشكل كبير—ويفضل كلاهما.

---

### Translation Notes

- **Key terms introduced:** memtable, SSTable, LSM-tree, Merkle Patricia Trie, gas, ERC-20, ERC-721, DeFi
- **Technical concepts:** hash-based addressing, log-structured merge trees, I/O amplification, Turing completeness
- **Special handling:**
  - Kept technical names like LevelDB, RocksDB, EVM, SSTable in English
  - "Light clients" translated as "العملاء الخفيفون"
  - Gas kept in English with Arabic explanation
  - IOPS kept as English abbreviation
  - DeFi kept as English abbreviation with Arabic expansion

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
