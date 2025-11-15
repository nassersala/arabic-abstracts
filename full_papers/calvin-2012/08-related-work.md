# Section 8: Related Work
## القسم 8: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** distributed database, transaction processing, replication, consistency, NoSQL, NewSQL, concurrency control, deterministic execution

---

### English Version

#### 8.1 Traditional Distributed Databases

Classical distributed database systems, such as those based on two-phase commit (2PC) and two-phase locking (2PL), have been extensively studied for decades. Systems like IBM DB2, Oracle RAC, and Microsoft SQL Server use variants of these protocols to provide ACID transactions across distributed data.

The fundamental limitation of these approaches is their reliance on distributed coordination during transaction execution. Each transaction must acquire locks across multiple nodes and execute 2PC to ensure atomicity. This coordination overhead severely limits scalability, particularly for geographically distributed deployments.

Calvin differs fundamentally by eliminating the need for distributed commit protocols through deterministic execution. While traditional systems must coordinate to resolve conflicts during execution, Calvin resolves all conflicts beforehand through global transaction ordering.

#### 8.2 NoSQL and Eventually Consistent Systems

The scalability limitations of traditional ACID databases led to the rise of NoSQL systems like Amazon Dynamo, Apache Cassandra, and MongoDB. These systems sacrifice strong consistency guarantees in favor of availability and partition tolerance, as described by the CAP theorem.

NoSQL systems typically provide eventual consistency: replicas may temporarily diverge but eventually converge to the same state. While this approach achieves excellent scalability, it places a significant burden on application developers to handle consistency anomalies such as lost updates, dirty reads, and write-write conflicts.

Calvin demonstrates that the traditional ACID vs. NoSQL trade-off is not fundamental. By using deterministic execution, Calvin provides full ACID guarantees while achieving scalability comparable to NoSQL systems. This positions Calvin in the emerging "NewSQL" category—systems that combine the consistency guarantees of traditional SQL databases with the scalability of NoSQL.

#### 8.3 Deterministic Database Systems

Calvin builds on prior research into deterministic database execution, particularly H-Store and VoltDB. H-Store demonstrated that single-partition transactions could be executed deterministically at very high throughput by eliminating concurrency control overhead within a partition.

However, H-Store's approach to multi-partition transactions was limited. It required executing multi-partition transactions sequentially across all involved partitions, creating a significant bottleneck. VoltDB, the commercial successor to H-Store, improved this somewhat but still struggled with cross-partition transactions.

Calvin's key contribution is extending deterministic execution to handle multi-partition transactions efficiently. By using a global sequencing layer and deterministic locking across partitions, Calvin supports arbitrary multi-partition transactions without sacrificing the benefits of deterministic execution.

Other related work includes:

**Granola**: Proposed a hybrid approach combining timestamp ordering with fine-grained locking. However, it still requires distributed coordination for conflict resolution.

**ROCOCO**: Uses a similar deterministic ordering approach but focuses on optimizing for specific access patterns rather than providing a general-purpose system.

#### 8.4 Replication Protocols

Calvin's replication strategy draws on established consensus protocols, particularly Paxos and its variants. Google's Chubby and Apache ZooKeeper provide practical implementations of Paxos-based consensus that Calvin leverages for its synchronous replication mode.

**Primary-backup replication**: Calvin's asynchronous mode is similar to traditional primary-backup schemes, where a master processes requests and forwards them to replicas. However, Calvin's deterministic execution ensures replicas remain consistent without requiring complex reconciliation protocols.

**State machine replication**: Calvin implements state-machine replication by replicating transaction inputs rather than outputs. This is more efficient than traditional approaches that replicate database writes, as transaction inputs are typically much smaller.

**Chain replication**: Systems like FAWN and CRAQ use chain replication for consistency. Calvin's approach differs by using Paxos for stronger consistency guarantees and supporting more flexible replication topologies.

#### 8.5 Optimistic Concurrency Control

Optimistic concurrency control (OCC) systems, such as those used in Google's Percolator and various main-memory databases, avoid locks by allowing transactions to execute speculatively and validating them at commit time.

While OCC can achieve good performance for low-contention workloads, it suffers from high abort rates under contention. Aborted transactions must be restarted, wasting significant resources. Calvin's deterministic locking approach never aborts transactions due to conflicts, providing more predictable performance.

#### 8.6 Google Spanner

Google Spanner, published concurrently with Calvin, uses an alternative approach to distributed transactions. Spanner relies on TrueTime, a globally synchronized clock with bounded uncertainty, to assign timestamps to transactions and ensure consistency across replicas.

While Spanner achieves impressive results, it requires specialized hardware (GPS and atomic clocks) for TrueTime, making it challenging to replicate outside of Google's infrastructure. Calvin achieves similar consistency guarantees using only standard consensus protocols, making it more practical for general deployment.

Both systems demonstrate that strong consistency and high performance are achievable in distributed databases, but they take fundamentally different approaches: Spanner relies on synchronized clocks, while Calvin relies on deterministic execution.

#### 8.7 Transaction Scheduling

Research on transaction scheduling has explored various approaches to improving concurrency:

**Dependency graphs**: Systems like DORA use fine-grained dependency tracking to maximize parallelism. Calvin's deterministic approach provides similar benefits with simpler implementation.

**Batch scheduling**: Early work on batch transaction processing influenced Calvin's epoch-based batching approach. By processing transactions in groups, systems can amortize coordination costs.

**Timestamp ordering**: Multiversion concurrency control (MVCC) systems use timestamp ordering to avoid locks. Calvin uses logical timestamps (the global sequence order) but combines this with deterministic locking for stronger guarantees.

#### 8.8 Positioning Calvin

Calvin occupies a unique position in the database system landscape:

- **Stronger consistency than NoSQL**: Provides full ACID guarantees rather than eventual consistency
- **Better scalability than traditional RDBMS**: Eliminates 2PC overhead through deterministic execution
- **More general than H-Store**: Supports efficient multi-partition transactions
- **More accessible than Spanner**: Requires no specialized hardware

This combination makes Calvin particularly suitable for applications that need both strong consistency guarantees and the ability to scale horizontally across commodity hardware.

---

### النسخة العربية

#### 8.1 قواعد البيانات الموزعة التقليدية

تمت دراسة أنظمة قواعد البيانات الموزعة الكلاسيكية، مثل تلك المستندة إلى الالتزام ثنائي الطور (2PC) والقفل ثنائي الطور (2PL)، على نطاق واسع لعقود. تستخدم أنظمة مثل IBM DB2 وOracle RAC وMicrosoft SQL Server متغيرات من هذه البروتوكولات لتوفير معاملات ACID عبر البيانات الموزعة.

القيد الأساسي لهذه الأساليب هو اعتمادها على التنسيق الموزع أثناء تنفيذ المعاملات. يجب على كل معاملة الحصول على أقفال عبر عقد متعددة وتنفيذ 2PC لضمان الذرية. تحد هذه التكلفة العامة للتنسيق بشدة من قابلية التوسع، خاصة بالنسبة للنشرات الموزعة جغرافياً.

يختلف كالفن بشكل أساسي من خلال إلغاء الحاجة إلى بروتوكولات الالتزام الموزع من خلال التنفيذ الحتمي. بينما يجب على الأنظمة التقليدية التنسيق لحل التعارضات أثناء التنفيذ، يحل كالفن جميع التعارضات مسبقاً من خلال الترتيب العالمي للمعاملات.

#### 8.2 أنظمة NoSQL والاتساق النهائي

أدت قيود قابلية التوسع في قواعد بيانات ACID التقليدية إلى ظهور أنظمة NoSQL مثل Amazon Dynamo وApache Cassandra وMongoDB. تضحي هذه الأنظمة بضمانات الاتساق القوية لصالح التوافر وتحمل التقسيم، كما هو موضح في نظرية CAP.

توفر أنظمة NoSQL عادةً الاتساق النهائي: قد تتباين النُسخ المتماثلة مؤقتاً ولكنها تتقارب في النهاية إلى نفس الحالة. بينما يحقق هذا النهج قابلية توسع ممتازة، فإنه يضع عبئاً كبيراً على مطوري التطبيقات للتعامل مع شذوذات الاتساق مثل التحديثات المفقودة والقراءات القذرة وتعارضات الكتابة-الكتابة.

يوضح كالفن أن المفاضلة التقليدية بين ACID وNoSQL ليست أساسية. من خلال استخدام التنفيذ الحتمي، يوفر كالفن ضمانات ACID كاملة مع تحقيق قابلية توسع قابلة للمقارنة بأنظمة NoSQL. هذا يضع كالفن في فئة "NewSQL" الناشئة—الأنظمة التي تجمع بين ضمانات الاتساق لقواعد بيانات SQL التقليدية وقابلية توسع NoSQL.

#### 8.3 أنظمة قواعد البيانات الحتمية

يبني كالفن على البحث السابق في التنفيذ الحتمي لقاعدة البيانات، خاصة H-Store وVoltDB. أظهرت H-Store أن المعاملات أحادية القسم يمكن تنفيذها بشكل حتمي بإنتاجية عالية جداً من خلال إلغاء التكلفة العامة للتحكم في التزامن داخل القسم.

ومع ذلك، كان نهج H-Store للمعاملات متعددة الأقسام محدوداً. تطلب تنفيذ المعاملات متعددة الأقسام بشكل تسلسلي عبر جميع الأقسام المعنية، مما خلق عنق زجاجة كبيراً. حسّنت VoltDB، الخليفة التجاري لـ H-Store، هذا إلى حد ما ولكنها لا تزال تكافح مع المعاملات عبر الأقسام.

مساهمة كالفن الرئيسية هي توسيع التنفيذ الحتمي للتعامل مع المعاملات متعددة الأقسام بكفاءة. من خلال استخدام طبقة تسلسل عالمية والقفل الحتمي عبر الأقسام، يدعم كالفن المعاملات متعددة الأقسام التعسفية دون التضحية بفوائد التنفيذ الحتمي.

تشمل الأعمال الأخرى ذات الصلة:

**Granola**: اقترحت نهجاً هجيناً يجمع بين ترتيب الطابع الزمني والقفل دقيق التفصيل. ومع ذلك، لا يزال يتطلب تنسيقاً موزعاً لحل التعارضات.

**ROCOCO**: تستخدم نهج ترتيب حتمي مماثل ولكنها تركز على التحسين لأنماط وصول محددة بدلاً من توفير نظام للأغراض العامة.

#### 8.4 بروتوكولات النسخ

تستند استراتيجية النسخ في كالفن إلى بروتوكولات الإجماع المعمول بها، خاصة باكسوس ومتغيراتها. توفر Chubby من Google وApache ZooKeeper تطبيقات عملية للإجماع المستند إلى باكسوس التي يستفيد منها كالفن لوضع النسخ المتزامن الخاص به.

**نسخ رئيسي-احتياطي**: وضع كالفن اللامتزامن مشابه لمخططات رئيسية-احتياطية التقليدية، حيث تعالج رئيسية الطلبات وتعيد توجيهها إلى النُسخ المتماثلة. ومع ذلك، يضمن التنفيذ الحتمي لكالفن بقاء النُسخ المتماثلة متسقة دون الحاجة إلى بروتوكولات مصالحة معقدة.

**نسخ آلة الحالة**: ينفذ كالفن نسخ آلة الحالة من خلال نسخ مدخلات المعاملات بدلاً من المخرجات. هذا أكثر كفاءة من الأساليب التقليدية التي تنسخ كتابات قاعدة البيانات، حيث أن مدخلات المعاملات عادةً أصغر بكثير.

**نسخ السلسلة**: تستخدم أنظمة مثل FAWN وCRAQ نسخ السلسلة للاتساق. يختلف نهج كالفن باستخدام باكسوس لضمانات اتساق أقوى ودعم طوبولوجيات نسخ أكثر مرونة.

#### 8.5 التحكم التفاؤلي في التزامن

تتجنب أنظمة التحكم التفاؤلي في التزامن (OCC)، مثل تلك المستخدمة في Percolator من Google وقواعد البيانات المختلفة في الذاكرة الرئيسية، الأقفال من خلال السماح للمعاملات بالتنفيذ بشكل تخميني والتحقق منها في وقت الالتزام.

بينما يمكن لـ OCC تحقيق أداء جيد لأحمال العمل منخفضة التنافس، فإنها تعاني من معدلات إلغاء عالية تحت التنافس. يجب إعادة تشغيل المعاملات الملغاة، مما يهدر موارد كبيرة. لا يلغي نهج القفل الحتمي لكالفن أبداً المعاملات بسبب التعارضات، مما يوفر أداءً أكثر قابلية للتنبؤ.

#### 8.6 Google Spanner

يستخدم Google Spanner، الذي نُشر بالتزامن مع كالفن، نهجاً بديلاً للمعاملات الموزعة. يعتمد Spanner على TrueTime، وهي ساعة متزامنة عالمياً مع عدم يقين محدود، لتعيين طوابع زمنية للمعاملات وضمان الاتساق عبر النُسخ المتماثلة.

بينما يحقق Spanner نتائج مبهرة، فإنه يتطلب أجهزة متخصصة (GPS والساعات الذرية) لـ TrueTime، مما يجعل من الصعب النسخ خارج البنية التحتية لـ Google. يحقق كالفن ضمانات اتساق مماثلة باستخدام بروتوكولات الإجماع القياسية فقط، مما يجعله أكثر عملية للنشر العام.

يوضح كلا النظامين أن الاتساق القوي والأداء العالي قابلان للتحقيق في قواعد البيانات الموزعة، لكنهما يتخذان نهجين مختلفين أساسياً: يعتمد Spanner على الساعات المتزامنة، بينما يعتمد كالفن على التنفيذ الحتمي.

#### 8.7 جدولة المعاملات

استكشف البحث حول جدولة المعاملات أساليب مختلفة لتحسين التزامن:

**رسوم بيانية التبعية**: تستخدم أنظمة مثل DORA تتبع التبعية دقيق التفصيل لتعظيم التوازي. يوفر نهج كالفن الحتمي فوائد مماثلة مع تطبيق أبسط.

**جدولة الدفعات**: أثّر العمل المبكر حول معالجة المعاملات بالدفعات على نهج التجميع القائم على الحقبة في كالفن. من خلال معالجة المعاملات في مجموعات، يمكن للأنظمة إطفاء تكاليف التنسيق.

**ترتيب الطابع الزمني**: تستخدم أنظمة التحكم في التزامن متعددة الإصدارات (MVCC) ترتيب الطابع الزمني لتجنب الأقفال. يستخدم كالفن طوابع زمنية منطقية (ترتيب التسلسل العالمي) ولكنه يجمع هذا مع القفل الحتمي لضمانات أقوى.

#### 8.8 وضع كالفن

يحتل كالفن موقعاً فريداً في مشهد نظام قاعدة البيانات:

- **اتساق أقوى من NoSQL**: يوفر ضمانات ACID كاملة بدلاً من الاتساق النهائي
- **قابلية توسع أفضل من RDBMS التقليدي**: يلغي التكلفة العامة لـ 2PC من خلال التنفيذ الحتمي
- **أكثر عمومية من H-Store**: يدعم المعاملات متعددة الأقسام الفعالة
- **أكثر سهولة من Spanner**: لا يتطلب أجهزة متخصصة

يجعل هذا المزيج كالفن مناسباً بشكل خاص للتطبيقات التي تحتاج إلى ضمانات اتساق قوية والقدرة على التوسع أفقياً عبر الأجهزة السلعية.

---

### Translation Notes

- **Key terms introduced:**
  - CAP theorem: نظرية CAP
  - NewSQL: NewSQL (kept in English as a proper category name)
  - Eventual consistency: الاتساق النهائي
  - Primary-backup replication: نسخ رئيسي-احتياطي
  - State machine replication: نسخ آلة الحالة
  - Chain replication: نسخ السلسلة
  - TrueTime: TrueTime (kept as proper name)
  - Dependency graphs: رسوم بيانية التبعية
  - Multiversion concurrency control (MVCC): التحكم في التزامن متعدد الإصدارات
  - Logical timestamps: طوابع زمنية منطقية

- **Equations:** None
- **Citations:** Multiple systems referenced: DB2, Oracle RAC, SQL Server, Dynamo, Cassandra, MongoDB, H-Store, VoltDB, Granola, ROCOCO, Chubby, ZooKeeper, Percolator, Spanner, DORA
- **Special handling:** Maintained accuracy for system comparisons and positioning

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation Validation

The Arabic translation accurately preserves:
- Comparison with traditional distributed databases
- Distinction from NoSQL and eventual consistency systems
- Relationship to prior deterministic database work (H-Store, VoltDB)
- Comparison with Google Spanner
- Calvin's unique positioning in the database landscape

✅ Translation maintains technical accuracy for related work comparisons.
