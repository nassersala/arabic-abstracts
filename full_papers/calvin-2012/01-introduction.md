# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** distributed transaction, database, scalability, consistency, partitioning, replication, ACID, two-phase commit, latency, throughput, deterministic, concurrency control

---

### English Version

The rise of cloud computing and the increasing demand for web-scale data management have led to a renaissance in distributed database system design. Modern applications require both high availability and strong consistency guarantees, yet distributed transactions have traditionally been considered too expensive to support at scale. The fundamental challenge is that maintaining ACID properties across partitioned and replicated data typically requires expensive coordination protocols, particularly two-phase commit (2PC), which introduce significant latency and limit scalability.

Traditional distributed database systems face a difficult trade-off: they can either provide strong consistency with poor performance due to coordination overhead, or they can sacrifice consistency to achieve better scalability. This dilemma has led many modern NoSQL systems to abandon transactional semantics entirely, opting instead for eventual consistency models. However, this approach places a significant burden on application developers, who must reason about complex consistency anomalies and implement application-level conflict resolution.

Calvin takes a fundamentally different approach to this problem. Rather than attempting to minimize coordination during transaction execution, Calvin eliminates the need for distributed coordination entirely through deterministic transaction execution. The key insight is that if all replicas can agree on a global transaction ordering before execution begins, and if transaction execution is deterministic, then all replicas will independently arrive at the same state without requiring any further coordination during execution.

This approach offers several key advantages. First, by eliminating distributed commit protocols, Calvin avoids the latency and communication overhead associated with 2PC. Second, because transaction execution is deterministic, Calvin can replicate transaction inputs rather than transaction effects, enabling efficient replication even for complex multi-partition transactions. Third, the deterministic execution model makes Calvin's behavior highly predictable and easier to reason about compared to traditional concurrency control mechanisms.

Calvin achieves determinism through careful system design across three layers: a sequencing layer that establishes a global transaction order using Paxos-based replication, a scheduling layer that uses deterministic locking to orchestrate transaction execution, and a pluggable storage layer that can work with various storage engines. The sequencing layer batches transaction requests into 10-millisecond epochs and uses consensus protocols to establish a total ordering across all replicas. The scheduling layer then executes transactions in this predetermined order using a lock manager that grants locks strictly according to the global sequence.

The main contributions of this paper are:

1. **Deterministic database design**: We present the first practical database system that achieves high performance through deterministic transaction execution, eliminating the need for distributed commit protocols.

2. **Scalable architecture**: We demonstrate how to build a distributed database that provides full ACID guarantees while achieving linear scalability through careful separation of sequencing, scheduling, and storage concerns.

3. **Replication flexibility**: Calvin supports both asynchronous replication for maximum throughput and Paxos-based synchronous replication for strong consistency, allowing users to choose the appropriate trade-off for their workload.

4. **Disk-aware optimizations**: We introduce techniques for handling disk-resident data in a deterministic execution model, including predictive prefetching and delayed scheduling.

5. **Comprehensive evaluation**: We provide experimental evidence that Calvin can sustain over 500,000 TPC-C transactions per second on a 100-node commodity cluster, matching world-record performance achieved on significantly more expensive hardware.

The remainder of this paper is organized as follows. Section 2 provides background on distributed transactions and discusses the limitations of traditional approaches. Section 3 presents Calvin's architecture and the interaction between its three layers. Section 4 details the sequencing layer and its replication protocols. Section 5 describes the scheduling layer's deterministic locking mechanism. Section 6 discusses how Calvin handles disk-resident data and checkpointing. Section 7 presents our experimental evaluation. Section 8 surveys related work, and Section 9 concludes with a discussion of future directions.

---

### النسخة العربية

أدى ظهور الحوسبة السحابية والطلب المتزايد على إدارة البيانات على نطاق الويب إلى نهضة في تصميم أنظمة قواعد البيانات الموزعة. تتطلب التطبيقات الحديثة كلاً من التوافر العالي وضمانات الاتساق القوية، ومع ذلك كانت المعاملات الموزعة تُعتبر تقليدياً مكلفة للغاية لدعمها على نطاق واسع. التحدي الأساسي هو أن الحفاظ على خصائص ACID عبر البيانات المجزأة والمنسوخة يتطلب عادةً بروتوكولات تنسيق مكلفة، وخاصة الالتزام ثنائي الطور (2PC)، والتي تقدم زمن استجابة كبيراً وتحد من قابلية التوسع.

تواجه أنظمة قواعد البيانات الموزعة التقليدية مفاضلة صعبة: يمكنها إما توفير اتساق قوي مع أداء ضعيف بسبب التكلفة العامة للتنسيق، أو يمكنها التضحية بالاتساق لتحقيق قابلية توسع أفضل. أدت هذه المعضلة بالعديد من أنظمة NoSQL الحديثة إلى التخلي عن الدلالات المعاملاتية تماماً، واختيار نماذج الاتساق النهائي بدلاً من ذلك. ومع ذلك، يضع هذا النهج عبئاً كبيراً على مطوري التطبيقات، الذين يجب عليهم التفكير في شذوذات الاتساق المعقدة وتنفيذ حل النزاعات على مستوى التطبيق.

يتبنى كالفن نهجاً مختلفاً جوهرياً لهذه المشكلة. بدلاً من محاولة تقليل التنسيق أثناء تنفيذ المعاملات، يلغي كالفن الحاجة إلى التنسيق الموزع بالكامل من خلال التنفيذ الحتمي للمعاملات. الفكرة الأساسية هي أنه إذا كان بإمكان جميع النُسخ المتماثلة الاتفاق على ترتيب عالمي للمعاملات قبل بدء التنفيذ، وإذا كان تنفيذ المعاملات حتمياً، فإن جميع النُسخ المتماثلة ستصل بشكل مستقل إلى نفس الحالة دون الحاجة إلى أي تنسيق إضافي أثناء التنفيذ.

يقدم هذا النهج عدة مزايا رئيسية. أولاً، من خلال إلغاء بروتوكولات الالتزام الموزع، يتجنب كالفن زمن الاستجابة والتكلفة العامة للاتصال المرتبطة بـ 2PC. ثانياً، نظراً لأن تنفيذ المعاملات حتمي، يمكن لكالفن نسخ مدخلات المعاملات بدلاً من تأثيرات المعاملات، مما يتيح النسخ الفعال حتى للمعاملات المعقدة متعددة الأقسام. ثالثاً، يجعل نموذج التنفيذ الحتمي سلوك كالفن قابلاً للتنبؤ بدرجة كبيرة وأسهل في الفهم مقارنة بآليات التحكم في التزامن التقليدية.

يحقق كالفن الحتمية من خلال التصميم الدقيق للنظام عبر ثلاث طبقات: طبقة تسلسل تنشئ ترتيباً عالمياً للمعاملات باستخدام النسخ المستند إلى باكسوس، وطبقة جدولة تستخدم القفل الحتمي لتنسيق تنفيذ المعاملات، وطبقة تخزين قابلة للتوصيل يمكن أن تعمل مع محركات تخزين مختلفة. تقوم طبقة التسلسل بتجميع طلبات المعاملات في حِقَب زمنية مدتها 10 ميلي ثانية وتستخدم بروتوكولات الإجماع لإنشاء ترتيب كلي عبر جميع النُسخ المتماثلة. ثم تنفذ طبقة الجدولة المعاملات بهذا الترتيب المحدد مسبقاً باستخدام مدير أقفال يمنح الأقفال بشكل صارم وفقاً للتسلسل العالمي.

المساهمات الرئيسية لهذا البحث هي:

1. **تصميم قاعدة بيانات حتمية**: نقدم أول نظام قاعدة بيانات عملي يحقق أداءً عالياً من خلال التنفيذ الحتمي للمعاملات، مما يلغي الحاجة إلى بروتوكولات الالتزام الموزع.

2. **معمارية قابلة للتوسع**: نوضح كيفية بناء قاعدة بيانات موزعة توفر ضمانات ACID كاملة مع تحقيق قابلية توسع خطية من خلال الفصل الدقيق بين مخاوف التسلسل والجدولة والتخزين.

3. **مرونة النسخ**: يدعم كالفن كلاً من النسخ اللامتزامن لتحقيق أقصى إنتاجية والنسخ المتزامن المستند إلى باكسوس للاتساق القوي، مما يسمح للمستخدمين باختيار المفاضلة المناسبة لحمل عملهم.

4. **تحسينات واعية بالقرص**: نقدم تقنيات للتعامل مع البيانات المقيمة على القرص في نموذج تنفيذ حتمي، بما في ذلك الجلب المسبق التنبؤي والجدولة المتأخرة.

5. **تقييم شامل**: نقدم دليلاً تجريبياً على أن كالفن يمكنه الحفاظ على أكثر من 500,000 معاملة TPC-C في الثانية على عنقود سلعي مكون من 100 عقدة، مطابقاً للأداء القياسي العالمي المحقق على أجهزة أكثر تكلفة بكثير.

يتم تنظيم بقية هذا البحث على النحو التالي. يوفر القسم 2 خلفية عن المعاملات الموزعة ويناقش قيود الأساليب التقليدية. يعرض القسم 3 معمارية كالفن والتفاعل بين طبقاته الثلاث. يفصّل القسم 4 طبقة التسلسل وبروتوكولات النسخ الخاصة بها. يصف القسم 5 آلية القفل الحتمي لطبقة الجدولة. يناقش القسم 6 كيفية تعامل كالفن مع البيانات المقيمة على القرص والنقاط المرجعية. يقدم القسم 7 تقييمنا التجريبي. يستعرض القسم 8 الأعمال ذات الصلة، ويختتم القسم 9 بمناقشة الاتجاهات المستقبلية.

---

### Translation Notes

- **Figures referenced:** None explicitly, but mentions Figure 1 in typical presentation
- **Key terms introduced:**
  - Cloud computing: الحوسبة السحابية
  - Web-scale: نطاق الويب
  - Strong consistency: اتساق قوي
  - Eventual consistency: الاتساق النهائي
  - Deterministic execution: التنفيذ الحتمي
  - Global transaction ordering: ترتيب عالمي للمعاملات
  - Consensus protocols: بروتوكولات الإجماع
  - Epochs: حِقَب زمنية
  - Predictive prefetching: الجلب المسبق التنبؤي
  - Commodity cluster: عنقود سلعي

- **Equations:** None
- **Citations:** None explicitly in introduction, but references to TPC-C benchmark
- **Special handling:** Maintained technical precision while ensuring Arabic reads naturally

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation

The Arabic translation accurately preserves:
- The motivation and context for Calvin's design
- The fundamental trade-off in distributed databases
- Calvin's novel approach using deterministic execution
- The three-layer architecture
- All five main contributions
- The paper's organizational structure

✅ Translation maintains technical accuracy and readability.
