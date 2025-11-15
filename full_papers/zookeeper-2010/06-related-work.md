# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** distributed system, coordination, consensus, lock service, configuration management

---

### English Version

ZooKeeper relates to several areas of distributed systems, and in this section we briefly mention some of the important work.

The Chubby lock service [6] is the project most similar to ZooKeeper. Chubby also has a file-system-like interface, and it implements a relaxed form of locks called advisory locks. Unlike ZooKeeper, Chubby emphasizes more locking than the implementation of general coordination primitives. Also, the Chubby API does not expose the ordering guarantees that ZooKeeper provides. ZooKeeper watches are similar to Chubby's events. However, Chubby events are not first-class citizens of the API and can only be used to signal changes of file content. ZooKeeper watches are ordered with respect to updates and other events, and they do not need to be re-registered unless the session terminates, simplifying their use.

Boxwood [20] is a collection of components for building higher-level services. It is designed with a similar layered approach as we have used in designing ZooKeeper. As Chubby, Boxwood has a lock service but it is built upon a more powerful consensus service. In a different vein, unlike ZooKeeper, Boxwood maintains strong consistency in read operations. ZooKeeper can have stale reads in some configurations, making it more scalable at the expense of guaranteed fresh reads.

ISIS [5] is a system developed in the late 80s that enables process groups to communicate with each other and manage group membership. ZooKeeper provides a similar membership management service with ephemeral nodes. However, ZooKeeper is not primarily a messaging system, so it offers more flexibility for applications implementing their messaging infrastructure.

Sinfonia [1] is a general-purpose shared-memory service, and ZooKeeper is not. We have chosen not to implement the most general of primitives at the server for several reasons. First, the specialized primitives we do provide expose a simple interface that makes ZooKeeper very easy to program with. Second, the specialized primitives allow us to achieve our demanding performance goals, which has been a major design consideration of ZooKeeper.

Distributed lock services are provided by several systems. VAXcluster [17] provides a distributed lock manager, and IBM 360/370 [16] has a lock manager in the kernel to synchronize access to the shared file system. For VAXcluster and most other distributed lock manager systems, locks are of mandatory use and clients must acquire locks to be able to access an object. ZooKeeper uses advisory locks, and locks are built using ZooKeeper primitives at the client.

Antiquity [13] and Oceanstore [19] replicate data in a peer-to-peer fashion. These systems target read-only or write-once data. ZooKeeper, on the other hand, is designed to offer both high read throughput and high availability, which enables applications to use ZooKeeper as their primary coordination service.

Dynamo [8] from Amazon is a distributed key-value store designed for high availability and reliability. Dynamo assumes that even in the presence of conflicting updates, data must still be available, which led to its optimistic replication approach. In contrast, ZooKeeper uses a primary copy replication strategy to guarantee ordering and allow strong consistency. As such, Dynamo focuses more on dealing with partitions and ZooKeeper assumes that full network partitions are rare.

Paxos [18] is a consensus protocol and it has been used in several systems as a component for implementing reliable distributed systems, Boxwood and Chubby being two examples. ZooKeeper does not expose its consensus protocol to applications, instead the API exposes primitives based on wait-free data objects. The Zab protocol that ZooKeeper uses bears some resemblance to Paxos, but it does not share the same properties. We are currently working to precisely characterize the properties of Zab [24]. We can say with confidence, however, that Zab provides the ordering properties necessary for ZooKeeper.

Several systems in the literature provide configuration services. Comet [27] is a configuration management service. It uses a centralized model where one node, called the server, stores the configuration, and many clients connect to this server to read the configuration. It has no replication and if the server fails, the configuration service is unavailable. ZooKeeper replicates its state and is thus able to provide an available configuration service.

RACS [29] (Reconfigurable Distributed Storage) is a system for dynamic reconfiguration of distributed storage systems. RACS uses a configuration service similar to ZooKeeper. It uses a state machine approach to execute configuration commands, and a primary based coordination system with failover to ensure availability. Unlike ZooKeeper, RACS does not implement a lock-free coordination service. The state machine in RACS is also used to compute policies, but policies are not used in ZooKeeper, although one might be able to use our watches to implement such a mechanism.

---

### النسخة العربية

يرتبط زوكيبر بعدة مجالات من الأنظمة الموزعة، وفي هذا القسم نذكر بإيجاز بعض الأعمال المهمة.

خدمة قفل Chubby [6] هي المشروع الأكثر تشابهاً مع زوكيبر. يحتوي Chubby أيضاً على واجهة تشبه نظام الملفات، وينفذ شكلاً مخففاً من الأقفال يسمى الأقفال الاستشارية. على عكس زوكيبر، يركز Chubby أكثر على القفل من تنفيذ بدائيات التنسيق العامة. أيضاً، لا تكشف واجهة برمجة تطبيقات Chubby عن ضمانات الترتيب التي يوفرها زوكيبر. مراقبات زوكيبر تشبه أحداث Chubby. ومع ذلك، فإن أحداث Chubby ليست مواطنين من الدرجة الأولى في واجهة برمجة التطبيقات ويمكن استخدامها فقط للإشارة إلى تغييرات محتوى الملف. يتم ترتيب مراقبات زوكيبر فيما يتعلق بالتحديثات والأحداث الأخرى، ولا تحتاج إلى إعادة التسجيل ما لم تنتهي الجلسة، مما يبسط استخدامها.

Boxwood [20] هي مجموعة من المكونات لبناء خدمات من مستوى أعلى. تم تصميمها بنهج طبقي مماثل كما استخدمنا في تصميم زوكيبر. مثل Chubby، يحتوي Boxwood على خدمة قفل لكنها مبنية على خدمة إجماع أكثر قوة. في نهج مختلف، على عكس زوكيبر، يحافظ Boxwood على اتساق قوي في عمليات القراءة. يمكن أن يكون لدى زوكيبر قراءات قديمة في بعض التكوينات، مما يجعلها أكثر قابلية للتوسع على حساب القراءات الطازجة المضمونة.

ISIS [5] هو نظام تم تطويره في أواخر الثمانينيات يتيح لمجموعات العمليات التواصل مع بعضها البعض وإدارة عضوية المجموعة. يوفر زوكيبر خدمة إدارة عضوية مماثلة مع العقد المؤقتة. ومع ذلك، فإن زوكيبر ليس في المقام الأول نظام مراسلة، لذا فهو يوفر مرونة أكبر للتطبيقات التي تنفذ البنية التحتية للمراسلة الخاصة بها.

Sinfonia [1] هي خدمة ذاكرة مشتركة للأغراض العامة، وزوكيبر ليس كذلك. اخترنا عدم تنفيذ البدائيات الأكثر عمومية على الخادم لعدة أسباب. أولاً، البدائيات المتخصصة التي نوفرها تكشف عن واجهة بسيطة تجعل البرمجة مع زوكيبر سهلة جداً. ثانياً، تسمح لنا البدائيات المتخصصة بتحقيق أهداف الأداء المتطلبة لدينا، والتي كانت اعتباراً رئيسياً في تصميم زوكيبر.

توفر عدة أنظمة خدمات القفل الموزع. يوفر VAXcluster [17] مدير قفل موزع، ويحتوي IBM 360/370 [16] على مدير قفل في النواة لمزامنة الوصول إلى نظام الملفات المشترك. بالنسبة لـ VAXcluster ومعظم أنظمة إدارة القفل الموزع الأخرى، تكون الأقفال للاستخدام الإلزامي ويجب على العملاء الحصول على أقفال لتتمكن من الوصول إلى كائن. يستخدم زوكيبر أقفالاً استشارية، ويتم بناء الأقفال باستخدام بدائيات زوكيبر على العميل.

Antiquity [13] و Oceanstore [19] تنسخ البيانات بطريقة نظير إلى نظير. تستهدف هذه الأنظمة البيانات للقراءة فقط أو الكتابة مرة واحدة. من ناحية أخرى، تم تصميم زوكيبر لتوفير كل من إنتاجية قراءة عالية وتوفر عالٍ، مما يمكّن التطبيقات من استخدام زوكيبر كخدمة تنسيق أساسية لها.

Dynamo [8] من Amazon هو مخزن مفتاح-قيمة موزع مصمم للتوفر العالي والموثوقية. يفترض Dynamo أنه حتى في وجود تحديثات متعارضة، يجب أن تظل البيانات متاحة، مما أدى إلى نهج النسخ المتماثل المتفائل. في المقابل، يستخدم زوكيبر استراتيجية نسخ النسخة الأساسية لضمان الترتيب والسماح بالاتساق القوي. على هذا النحو، يركز Dynamo أكثر على التعامل مع الأقسام بينما يفترض زوكيبر أن أقسام الشبكة الكاملة نادرة.

Paxos [18] هو بروتوكول إجماع وقد تم استخدامه في عدة أنظمة كمكون لتنفيذ أنظمة موزعة موثوقة، حيث يكون Boxwood و Chubby مثالين. لا يكشف زوكيبر عن بروتوكول الإجماع الخاص به للتطبيقات، بدلاً من ذلك تكشف واجهة برمجة التطبيقات عن بدائيات تستند إلى كائنات بيانات خالية من الانتظار. يحمل بروتوكول Zab الذي يستخدمه زوكيبر بعض التشابه مع Paxos، لكنه لا يشارك نفس الخصائص. نعمل حالياً على تحديد خصائص Zab بدقة [24]. ومع ذلك، يمكننا القول بثقة أن Zab يوفر خصائص الترتيب اللازمة لزوكيبر.

توفر عدة أنظمة في الأدبيات خدمات التكوين. Comet [27] هي خدمة إدارة التكوين. تستخدم نموذجاً مركزياً حيث تخزن عقدة واحدة، تسمى الخادم، التكوين، ويتصل العديد من العملاء بهذا الخادم لقراءة التكوين. لا يوجد لديها نسخ متماثل وإذا فشل الخادم، فإن خدمة التكوين غير متاحة. ينسخ زوكيبر حالته وبالتالي قادر على توفير خدمة تكوين متاحة.

RACS [29] (التخزين الموزع القابل لإعادة التكوين) هو نظام لإعادة التكوين الديناميكي لأنظمة التخزين الموزعة. يستخدم RACS خدمة تكوين مشابهة لزوكيبر. يستخدم نهج آلة الحالة لتنفيذ أوامر التكوين، ونظام تنسيق قائم على الأساسي مع تبديل لضمان التوفر. على عكس زوكيبر، لا ينفذ RACS خدمة تنسيق خالية من القفل. يتم استخدام آلة الحالة في RACS أيضاً لحساب السياسات، لكن السياسات لا تُستخدم في زوكيبر، على الرغم من أنه قد يكون من الممكن استخدام مراقباتنا لتنفيذ مثل هذه الآلية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Advisory locks (أقفال استشارية) - non-mandatory locks
  - Mandatory locks (أقفال إلزامية) - required locks
  - Optimistic replication (نسخ متماثل متفائل) - Dynamo approach
  - Primary copy replication (نسخ النسخة الأساسية) - ZooKeeper approach
  - State machine (آلة الحالة) - implementation approach

- **Equations:** None
- **Citations:** [1], [5], [6], [8], [13], [16], [17], [18], [19], [20], [24], [27], [29] - all preserved
- **Special handling:**
  - System names (Chubby, Boxwood, ISIS, Sinfonia, VAXcluster, Antiquity, Oceanstore, Dynamo, Paxos, Comet, RACS) kept in English
  - Company names (Amazon, IBM) kept in English
  - Protocol names (Paxos, Zab) kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-translation Check

First paragraph back-translation: "ZooKeeper relates to several areas of distributed systems, and in this section we briefly mention some important work."

✅ Semantically equivalent to original
