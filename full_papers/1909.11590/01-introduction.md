# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** blockchain, transaction, throughput, Merkle tree, consensus, distributed system, I/O bottleneck, proof-of-work, smart contract, Ethereum

---

### English Version

Public blockchains like Ethereum have transformed how we think about distributed trust and computation. These systems allow mutually distrusting parties to execute transactions and smart contracts without a trusted third party. However, despite their revolutionary potential, public blockchains suffer from severely limited transaction throughput. While systems like Visa can process thousands of transactions per second, Ethereum processes only tens of transactions per second. This fundamental limitation has prevented blockchain systems from scaling to support the transaction volumes required for many real-world applications.

The low throughput of public blockchains has often been attributed to their consensus protocols, particularly proof-of-work (PoW). However, our empirical analysis reveals a different bottleneck: **I/O operations**. Specifically, we show that the use of Merkle trees for maintaining and verifying blockchain state creates a significant I/O bottleneck that limits transaction processing throughput.

Merkle trees are cryptographically authenticated data structures that allow clients to verify data received from untrusted servers. In blockchain systems, they enable light clients to verify transactions without downloading the entire blockchain state. However, this security property comes at a significant performance cost. Processing a single block of 100 transactions in Ethereum requires performing more than 10,000 random I/O operations. Even on datacenter-grade NVMe SSDs, these operations take hundreds of milliseconds, severely limiting throughput.

The I/O bottleneck manifests in two critical ways:

**First, I/O amplification**: Merkle trees stored in key-value stores like RocksDB suffer from expensive random reads. Each node lookup requires computing cryptographic hashes to locate nodes, and the log-structured merge tree organization of RocksDB further amplifies I/O operations. A single transaction read can trigger dozens of disk accesses.

**Second, I/O in the critical path**: Current blockchain architectures place I/O operations directly in the transaction processing path. Miners must sequentially process each transaction, performing disk I/O for every state read and write. This serialization prevents parallelization and keeps CPUs idle while waiting for disk operations to complete.

We present **RAINBLOCK**, a new architecture for public blockchains that increases throughput by an order of magnitude without compromising security or altering consensus mechanisms. RAINBLOCK addresses both dimensions of the I/O bottleneck:

1. **Removing I/O from the critical path**: RAINBLOCK introduces prefetching clients that perform I/O operations out-of-band, before transactions reach miners. Clients pre-execute transactions to determine required data, fetch it from storage nodes, and package it with transactions as cryptographically authenticated witnesses. Miners receive all necessary data in memory and process transactions purely as CPU operations without any disk access.

2. **Reducing I/O amplification**: RAINBLOCK introduces the Distributed Sharded Merkle tree (DSM-TREE), a novel authenticated data structure that stores blockchain state efficiently. DSM-TREE uses in-memory pointer-based traversal instead of hash-based lookups, implements lazy hash computation, and supports multi-versioning for concurrent updates. These optimizations reduce I/O operations by over 100× compared to traditional Merkle trees.

The RAINBLOCK architecture consists of three components:

- **Prefetching clients** that read data from storage nodes, pre-execute transactions, and generate witnesses
- **Miners** that verify and execute transactions using prefetched data, create blocks, and send updates to storage
- **Storage nodes** that maintain the distributed DSM-TREE and serve data requests from clients

A key challenge in this design is handling smart contracts. Since Ethereum smart contracts are Turing-complete, determining which data a contract will access requires executing it. RAINBLOCK uses speculative pre-execution: clients execute contracts using estimated values for block-dependent parameters (timestamps, block numbers). Our analysis of Ethereum contracts shows this successfully prefetches correct witnesses in the vast majority of cases.

We implement a prototype of RAINBLOCK consisting of approximately 15,000 lines of TypeScript, with performance-critical operations in C++. We evaluate RAINBLOCK using workloads derived from public Ethereum transaction traces, including smart contracts.

Our evaluation demonstrates significant performance improvements:

- A single RAINBLOCK miner processes **27,400 transactions per second**, compared to 1,000 transactions per second for a single Ethereum miner—a **27× improvement**.
- In a geo-distributed setting with four regions spread across three continents, RAINBLOCK processes **20,000 transactions per second**, maintaining high throughput despite network latency.
- For smart contracts, RAINBLOCK achieves **17,900 ERC-20 token transfer operations per second**, demonstrating that the architecture effectively handles complex contract execution.

RAINBLOCK achieves these improvements while maintaining the same security properties as Ethereum. The system does not modify consensus protocols, block creation rates, or trust assumptions. All participants verify data cryptographically, and no component needs to trust any other.

In summary, this paper makes the following contributions:

- **Empirical analysis** identifying I/O operations as the primary bottleneck in public blockchain transaction processing
- **RAINBLOCK architecture** that decouples I/O from transaction execution by introducing prefetching clients and restructuring the miner workflow
- **DSM-TREE**, a novel distributed, sharded, multi-versioned Merkle tree that reduces I/O amplification by over 100×
- **Implementation and evaluation** demonstrating that RAINBLOCK increases throughput by 27× for a single miner and achieves 20,000 transactions per second in geo-distributed deployments
- **Analysis** showing that speculative pre-execution successfully handles the vast majority of Ethereum smart contracts

The rest of this paper is organized as follows: Section 2 provides background on blockchain systems and Merkle trees. Section 3 presents the RAINBLOCK architecture. Section 4 describes the DSM-TREE design in detail. Section 5 discusses implementation details. Section 6 presents our evaluation results. Section 7 discusses related work, and Section 8 concludes.

---

### النسخة العربية

لقد غيرت سلاسل الكتل العامة مثل إيثيريوم طريقة تفكيرنا في الثقة الموزعة والحوسبة. تتيح هذه الأنظمة للأطراف التي لا تثق ببعضها البعض تنفيذ المعاملات والعقود الذكية دون الحاجة إلى طرف ثالث موثوق به. ومع ذلك، وعلى الرغم من إمكاناتها الثورية، تعاني سلاسل الكتل العامة من محدودية شديدة في إنتاجية المعاملات. بينما يمكن لأنظمة مثل فيزا معالجة آلاف المعاملات في الثانية، لا تعالج إيثيريوم سوى عشرات المعاملات في الثانية. لقد منع هذا القيد الأساسي أنظمة البلوك تشين من التوسع لدعم أحجام المعاملات المطلوبة للعديد من التطبيقات الواقعية.

غالباً ما يُعزى انخفاض إنتاجية سلاسل الكتل العامة إلى بروتوكولات الإجماع الخاصة بها، وخاصة إثبات العمل (PoW). ومع ذلك، يكشف تحليلنا التجريبي عن عنق زجاجة مختلف: **عمليات الإدخال/الإخراج**. على وجه التحديد، نُظهر أن استخدام أشجار ميركل للحفاظ على حالة البلوك تشين والتحقق منها يخلق عنق زجاجة كبير في الإدخال/الإخراج يحد من إنتاجية معالجة المعاملات.

أشجار ميركل هي هياكل بيانات مصادق عليها تشفيرياً تسمح للعملاء بالتحقق من البيانات المستلمة من خوادم غير موثوقة. في أنظمة البلوك تشين، تمكّن العملاء الخفيفة من التحقق من المعاملات دون تنزيل حالة البلوك تشين بأكملها. ومع ذلك، تأتي خاصية الأمان هذه بتكلفة أداء كبيرة. تتطلب معالجة كتلة واحدة من 100 معاملة في إيثيريوم تنفيذ أكثر من 10,000 عملية إدخال/إخراج عشوائية. حتى على أقراص NVMe SSD من فئة مراكز البيانات، تستغرق هذه العمليات مئات الميلي ثانية، مما يحد بشدة من الإنتاجية.

يتجلى عنق الزجاجة في الإدخال/الإخراج بطريقتين حاسمتين:

**أولاً، تضخيم الإدخال/الإخراج**: تعاني أشجار ميركل المخزنة في مخازن القيم-المفاتيح مثل RocksDB من قراءات عشوائية مكلفة. يتطلب كل بحث عن عقدة حساب تجزئات تشفيرية لتحديد موقع العقد، كما أن تنظيم شجرة الدمج المنظمة بالسجل (log-structured merge tree) في RocksDB يزيد من تضخيم عمليات الإدخال/الإخراج. يمكن لقراءة معاملة واحدة أن تؤدي إلى عشرات الوصولات إلى القرص.

**ثانياً، الإدخال/الإخراج في المسار الحرج**: تضع معماريات البلوك تشين الحالية عمليات الإدخال/الإخراج مباشرة في مسار معالجة المعاملات. يجب على المُعدِّنين معالجة كل معاملة بشكل تسلسلي، وإجراء عمليات إدخال/إخراج للقرص لكل قراءة وكتابة للحالة. يمنع هذا التسلسل التوازي ويبقي وحدات المعالجة المركزية في وضع الخمول أثناء انتظار اكتمال عمليات القرص.

نقدم **RAINBLOCK**، وهي معمارية جديدة لسلاسل الكتل العامة تزيد الإنتاجية بمقدار من الحجم دون المساس بالأمان أو تغيير آليات الإجماع. يعالج RAINBLOCK كلا البعدين من عنق زجاجة الإدخال/الإخراج:

1. **إزالة الإدخال/الإخراج من المسار الحرج**: يقدم RAINBLOCK عملاء جلب مسبق ينفذون عمليات الإدخال/الإخراج خارج النطاق، قبل وصول المعاملات إلى المُعدِّنين. يقوم العملاء بتنفيذ المعاملات مسبقاً لتحديد البيانات المطلوبة، وجلبها من عقد التخزين، وتعبئتها مع المعاملات كشهود مصادق عليها تشفيرياً. يتلقى المُعدِّنون جميع البيانات الضرورية في الذاكرة ويعالجون المعاملات بشكل صرف كعمليات معالج مركزي دون أي وصول إلى القرص.

2. **تقليل تضخيم الإدخال/الإخراج**: يقدم RAINBLOCK شجرة ميركل المجزأة الموزعة (DSM-TREE)، وهي هيكل بيانات مصادق عليه جديد يخزن حالة البلوك تشين بكفاءة. تستخدم DSM-TREE المرور القائم على المؤشرات في الذاكرة بدلاً من البحث القائم على التجزئة، وتنفذ الحساب الكسول للتجزئة، وتدعم النسخ المتعددة للتحديثات المتزامنة. تقلل هذه التحسينات عمليات الإدخال/الإخراج بأكثر من 100× مقارنة بأشجار ميركل التقليدية.

تتكون معمارية RAINBLOCK من ثلاثة مكونات:

- **عملاء الجلب المسبق** الذين يقرؤون البيانات من عقد التخزين، وينفذون المعاملات مسبقاً، ويولدون الشهود
- **المُعدِّنون** الذين يتحققون من المعاملات وينفذونها باستخدام البيانات المجلوبة مسبقاً، وينشئون الكتل، ويرسلون التحديثات إلى التخزين
- **عقد التخزين** التي تحافظ على DSM-TREE الموزعة وتخدم طلبات البيانات من العملاء

يتمثل التحدي الرئيسي في هذا التصميم في التعامل مع العقود الذكية. نظراً لأن العقود الذكية لإيثيريوم كاملة حسب تورينج، فإن تحديد البيانات التي سيصل إليها العقد يتطلب تنفيذه. يستخدم RAINBLOCK التنفيذ المسبق التخميني: ينفذ العملاء العقود باستخدام قيم مقدرة للمعاملات المعتمدة على الكتلة (الطوابع الزمنية، أرقام الكتل). يُظهر تحليلنا لعقود إيثيريوم أن هذا يجلب الشهود الصحيحين مسبقاً بنجاح في الغالبية العظمى من الحالات.

نقوم بتطبيق نموذج أولي لـ RAINBLOCK يتكون من حوالي 15,000 سطر من TypeScript، مع عمليات حرجة للأداء في C++. نقيّم RAINBLOCK باستخدام أحمال عمل مشتقة من آثار معاملات إيثيريوم العامة، بما في ذلك العقود الذكية.

يُظهر تقييمنا تحسينات أداء كبيرة:

- يعالج مُعدِّن RAINBLOCK واحد **27,400 معاملة في الثانية**، مقارنة بـ 1,000 معاملة في الثانية لمُعدِّن إيثيريوم واحد—**تحسن بمقدار 27×**.
- في بيئة موزعة جغرافياً مع أربع مناطق موزعة عبر ثلاث قارات، يعالج RAINBLOCK **20,000 معاملة في الثانية**، مع الحفاظ على إنتاجية عالية على الرغم من زمن استجابة الشبكة.
- بالنسبة للعقود الذكية، يحقق RAINBLOCK **17,900 عملية نقل رمز ERC-20 في الثانية**، مما يدل على أن المعمارية تتعامل بفعالية مع تنفيذ العقود المعقدة.

يحقق RAINBLOCK هذه التحسينات مع الحفاظ على نفس خصائص الأمان الخاصة بإيثيريوم. لا يُعدِّل النظام بروتوكولات الإجماع أو معدلات إنشاء الكتل أو افتراضات الثقة. يتحقق جميع المشاركين من البيانات تشفيرياً، ولا يحتاج أي مكون إلى الثقة في أي مكون آخر.

باختصار، تقدم هذه الورقة المساهمات التالية:

- **تحليل تجريبي** يحدد عمليات الإدخال/الإخراج كعنق الزجاجة الأساسي في معالجة معاملات البلوك تشين العامة
- **معمارية RAINBLOCK** التي تفصل الإدخال/الإخراج عن تنفيذ المعاملات من خلال تقديم عملاء الجلب المسبق وإعادة هيكلة سير عمل المُعدِّن
- **DSM-TREE**، شجرة ميركل موزعة، مجزأة، متعددة النسخ جديدة تقلل من تضخيم الإدخال/الإخراج بأكثر من 100×
- **تطبيق وتقييم** يُظهر أن RAINBLOCK يزيد الإنتاجية بمقدار 27× لمُعدِّن واحد ويحقق 20,000 معاملة في الثانية في عمليات النشر الموزعة جغرافياً
- **تحليل** يُظهر أن التنفيذ المسبق التخميني يتعامل بنجاح مع الغالبية العظمى من العقود الذكية لإيثيريوم

يتم تنظيم بقية هذه الورقة على النحو التالي: يوفر القسم 2 خلفية عن أنظمة البلوك تشين وأشجار ميركل. يقدم القسم 3 معمارية RAINBLOCK. يصف القسم 4 تصميم DSM-TREE بالتفصيل. يناقش القسم 5 تفاصيل التطبيق. يعرض القسم 6 نتائج تقييمنا. يناقش القسم 7 الأعمال ذات الصلة، ويختتم القسم 8.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** RAINBLOCK architecture, DSM-TREE, prefetching clients, I/O amplification, speculative pre-execution, critical path, witnesses
- **Equations:** None
- **Citations:** General references to Ethereum, Visa, RocksDB
- **Special handling:**
  - Kept system names like RAINBLOCK, DSM-TREE, RocksDB, NVMe in English
  - ERC-20 kept as English technical standard name
  - Performance numbers preserved exactly (27,400 TPS, 20,000 TPS, etc.)
  - "Turing-complete" translated as "كاملة حسب تورينج"

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
