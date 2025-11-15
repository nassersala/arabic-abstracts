# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.90
**Glossary Terms Used:** distributed system, coordination, consensus, fault-tolerant, asynchronous, scalability, API, client

---

### English Version

Large-scale distributed applications require different forms of coordination. Configuration is one of the most basic forms of coordination. In its simplest form, configuration is just a list of operational parameters for the system processes, whereas more sophisticated systems have dynamic configuration parameters. Group membership and leader election are also common in distributed systems: often processes need to know which other processes are alive and what those processes are in charge of. Locks constitute a powerful coordination primitive that implement mutually exclusive access to critical resources.

One approach to coordination is to develop services for each of the different coordination needs. For example, Amazon Simple Queue Service focuses specifically on queuing. Other services have been developed specifically for leader election [25] and configuration [27]. Services that implement more powerful primitives can be used to implement less powerful ones. For example, Chubby is a locking service with strong synchronization guarantees. Locks can then be used to implement leader election, group membership, etc.

When designing our coordination service, we moved away from implementing specific primitives on the server side, and instead we opted for exposing an API that enables application developers to implement their own primitives. Such a choice led to the implementation of a coordination kernel that enables new primitives without requiring changes to the service core. This approach enables multiple forms of coordination adapted to the requirements of applications, instead of constraining developers to a fixed set of primitives.

When designing the API for ZooKeeper, we moved away from blocking primitives, such as locks. Blocking primitives for a coordination service can cause, among other problems, slow or faulty clients to impact negatively the performance of faster clients. The implementation of the service itself becomes more complicated if processing requests depends on responses and failure detection of other clients. Our system, Zookeeper, hence implements an API that manipulates simple wait-free data objects organized hierarchically as in file systems. In fact, the ZooKeeper API resembles the one for file systems, and looking at just the API signatures, ZooKeeper seems to be a Chubby without the lock methods, open, and close. Implementing wait-free data objects, however, differentiates ZooKeeper significantly from systems based on blocking primitives such as locks.

Although the wait-free property is important for performance and fault tolerance, it is not sufficient for coordination. We have also to provide order guarantees for operations. In particular, we have found that guaranteeing both FIFO client ordering of all operations and linearizable writes enables an efficient implementation of the service and it is sufficient to implement coordination primitives of interest to our applications. In fact, we can implement consensus for any number of processes with our API, and according to the hierarchy of Herlihy, ZooKeeper implements a universal object [14].

The ZooKeeper service comprises an ensemble of servers that use replication to achieve high availability and performance. Its high performance enables applications comprising a large number of processes to use such a coordination service. The ability to cache the ZooKeeper state in the form of watches enables clients to receive timely notifications of changes, making it feasible to use ZooKeeper for coordinating processes both at a node and across nodes. The ordering guarantees of ZooKeeper enable efficient reasoning about system state, and watches allow efficient waiting for events. Although the consistency guarantees for reads are weaker than linearizability (reads can be stale), reads from the same client are FIFO ordered and updates are totally ordered, providing enough consistency for a wide range of uses.

Our contributions in this paper can be summarized as follows:

**Coordination kernel:** We propose a wait-free coordination service with relaxed consistency guarantees for use in distributed systems. In particular, we describe our design and implementation of a coordination kernel. This kernel has been used in many critical applications to implement various coordination techniques.

**Coordination recipes:** We show how ZooKeeper can be used to build higher level coordination primitives, even blocking and strongly consistent primitives, that are often useful in distributed applications.

**Experience with Coordination:** We share some of the ways that we use ZooKeeper and evaluate its performance.

---

### النسخة العربية

تتطلب التطبيقات الموزعة واسعة النطاق أشكالاً مختلفة من التنسيق. التكوين هو أحد أبسط أشكال التنسيق. في شكله الأبسط، التكوين هو مجرد قائمة من المعاملات التشغيلية لعمليات النظام، بينما تحتوي الأنظمة الأكثر تطوراً على معاملات تكوين ديناميكية. عضوية المجموعة وانتخاب القائد شائعان أيضاً في الأنظمة الموزعة: غالباً ما تحتاج العمليات إلى معرفة العمليات الأخرى النشطة وما هي المسؤوليات التي تقوم بها تلك العمليات. تشكل الأقفال بدائية تنسيق قوية تنفذ الوصول الحصري المتبادل إلى الموارد الحرجة.

أحد أساليب التنسيق هو تطوير خدمات لكل من احتياجات التنسيق المختلفة. على سبيل المثال، تركز خدمة Amazon Simple Queue Service بشكل خاص على قوائم الانتظار. تم تطوير خدمات أخرى خصيصاً لانتخاب القائد [25] والتكوين [27]. يمكن استخدام الخدمات التي تنفذ بدائيات أكثر قوة لتنفيذ بدائيات أقل قوة. على سبيل المثال، Chubby هي خدمة قفل مع ضمانات تزامن قوية. يمكن بعد ذلك استخدام الأقفال لتنفيذ انتخاب القائد وعضوية المجموعة وما إلى ذلك.

عند تصميم خدمة التنسيق الخاصة بنا، ابتعدنا عن تنفيذ بدائيات محددة على جانب الخادم، وبدلاً من ذلك اخترنا كشف واجهة برمجة تطبيقات تمكّن مطوري التطبيقات من تنفيذ بدائياتهم الخاصة. أدى هذا الاختيار إلى تنفيذ نواة تنسيق تمكّن من إنشاء بدائيات جديدة دون الحاجة إلى تغييرات في جوهر الخدمة. يتيح هذا النهج أشكالاً متعددة من التنسيق متكيفة مع متطلبات التطبيقات، بدلاً من تقييد المطورين بمجموعة ثابتة من البدائيات.

عند تصميم واجهة برمجة التطبيقات لزوكيبر، ابتعدنا عن البدائيات الحاجبة، مثل الأقفال. يمكن أن تتسبب البدائيات الحاجبة لخدمة التنسيق، من بين مشاكل أخرى، في أن يؤثر العملاء البطيئون أو المعيبون سلباً على أداء العملاء الأسرع. يصبح تنفيذ الخدمة نفسها أكثر تعقيداً إذا كانت معالجة الطلبات تعتمد على استجابات واكتشاف فشل العملاء الآخرين. لذلك ينفذ نظامنا، زوكيبر، واجهة برمجة تطبيقات تتلاعب بكائنات بيانات بسيطة خالية من الانتظار منظمة بشكل هرمي كما هو الحال في أنظمة الملفات. في الواقع، تشبه واجهة برمجة التطبيقات الخاصة بزوكيبر تلك الخاصة بأنظمة الملفات، وبالنظر إلى توقيعات واجهة برمجة التطبيقات فقط، يبدو زوكيبر وكأنه Chubby بدون طرق القفل والفتح والإغلاق. ومع ذلك، فإن تنفيذ كائنات البيانات الخالية من الانتظار يميز زوكيبر بشكل كبير عن الأنظمة القائمة على البدائيات الحاجبة مثل الأقفال.

على الرغم من أن خاصية الخلو من الانتظار مهمة للأداء وتحمل الأخطاء، إلا أنها ليست كافية للتنسيق. يجب علينا أيضاً توفير ضمانات ترتيب للعمليات. على وجه الخصوص، وجدنا أن ضمان كل من ترتيب FIFO للعميل لجميع العمليات وخطية الكتابات يتيح تنفيذاً فعالاً للخدمة ويكفي لتنفيذ بدائيات التنسيق ذات الأهمية لتطبيقاتنا. في الواقع، يمكننا تنفيذ الإجماع لأي عدد من العمليات باستخدام واجهة برمجة التطبيقات الخاصة بنا، ووفقاً لتسلسل Herlihy الهرمي، ينفذ زوكيبر كائناً عالمياً [14].

تتألف خدمة زوكيبر من مجموعة من الخوادم التي تستخدم النسخ المتماثل لتحقيق توفر عالٍ وأداء عالٍ. يتيح أداؤها العالي للتطبيقات التي تشمل عدداً كبيراً من العمليات استخدام خدمة التنسيق هذه. تتيح القدرة على التخزين المؤقت لحالة زوكيبر في شكل مراقبات (watches) للعملاء تلقي إشعارات فورية بالتغييرات، مما يجعل من الممكن استخدام زوكيبر لتنسيق العمليات على مستوى العقدة وعبر العقد. تتيح ضمانات الترتيب في زوكيبر الاستدلال الفعال حول حالة النظام، وتسمح المراقبات بالانتظار الفعال للأحداث. على الرغم من أن ضمانات الاتساق للقراءات أضعف من الخطية (يمكن أن تكون القراءات قديمة)، إلا أن القراءات من نفس العميل مرتبة بطريقة FIFO والتحديثات مرتبة كلياً، مما يوفر اتساقاً كافياً لمجموعة واسعة من الاستخدامات.

يمكن تلخيص مساهماتنا في هذا البحث على النحو التالي:

**نواة التنسيق:** نقترح خدمة تنسيق خالية من الانتظار مع ضمانات اتساق مخففة للاستخدام في الأنظمة الموزعة. على وجه الخصوص، نصف تصميمنا وتنفيذنا لنواة التنسيق. تم استخدام هذه النواة في العديد من التطبيقات الحيوية لتنفيذ تقنيات تنسيق مختلفة.

**وصفات التنسيق:** نوضح كيف يمكن استخدام زوكيبر لبناء بدائيات تنسيق من مستوى أعلى، حتى البدائيات الحاجبة والمتسقة بشدة، والتي غالباً ما تكون مفيدة في التطبيقات الموزعة.

**الخبرة في التنسيق:** نشارك بعض الطرق التي نستخدم بها زوكيبر ونقيّم أداءه.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:**
  - Coordination kernel (نواة التنسيق) - core service component
  - Wait-free (خالٍ من الانتظار) - non-blocking operations
  - FIFO client ordering (ترتيب FIFO للعميل) - ordering guarantee
  - Linearizable writes (كتابات خطية) - consistency guarantee
  - Watches (مراقبات) - event notification mechanism
  - Ensemble (مجموعة) - group of servers
  - Blocking primitives (بدائيات حاجبة) - operations that block
  - Coordination primitives (بدائيات التنسيق) - basic building blocks

- **Equations:** None
- **Citations:** [14], [25], [27] - preserved as in original
- **Special handling:**
  - Chubby and Amazon Simple Queue Service kept in English (proper names)
  - FIFO kept as acronym with context
  - "Universal object" from Herlihy's hierarchy translated as "كائن عالمي"

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.93
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.90

### Back-translation Check

First paragraph back-translation: "Large-scale distributed applications require different forms of coordination. Configuration is one of the simplest forms of coordination. In its simplest form, configuration is just a list of operational parameters for system processes, while more sophisticated systems contain dynamic configuration parameters..."

✅ Semantically equivalent to original
