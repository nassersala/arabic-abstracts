# Section 3: Related Work
## القسم 3: العمل ذو الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** peer-to-peer (من نظير إلى نظير), distributed hash table (جدول تجزئة موزع), DHT (جدول تجزئة موزع), routing (توجيه), replication (نسخ تماثلي), conflict resolution (حل التعارضات), eventual consistency (اتساق نهائي), distributed file system (نظام ملفات موزع), Byzantine fault tolerance (تحمل الأخطاء البيزنطية)

---

### English Version

## 3.1 Peer to Peer Systems

There are several peer-to-peer (P2P) systems that have looked at the problem of data storage and distribution. The first generation of P2P systems, such as Freenet and Gnutella, were predominantly used as file sharing systems. These were examples of unstructured P2P networks where the overlay links between peers were established arbitrarily. In these networks, a search query is usually flooded through the network to find as many peers as possible that share the data. P2P systems evolved to the next generation into what is widely known as structured P2P networks. These networks employ a globally consistent protocol to ensure that any node can efficiently route a search query to some peer that has the desired data. Systems like Pastry [16] and Chord [20] use routing mechanisms to ensure that queries can be answered within a bounded number of hops. To reduce the additional latency introduced by multi-hop routing, some P2P systems (e.g., [14]) employ O(1) routing where each peer maintains enough routing information locally so that it can route requests (to access a data item) to the appropriate peer within a constant number of hops.

Various storage systems, such as Oceanstore [9] and PAST [17] were built on top of these routing overlays. Oceanstore provides a global, transactional, persistent storage service that supports serialized updates on widely replicated data. To allow for concurrent updates while avoiding many of the problems inherent with wide-area locking, it uses an update model based on conflict resolution. Conflict resolution was introduced in [21] to reduce the number of transaction aborts. Oceanstore resolves conflicts by processing a series of updates, choosing a total order among them, and then applying them atomically in that order. It is built for an environment where the data is replicated on an untrusted infrastructure. By comparison, PAST provides a simple abstraction layer on top of Pastry for persistent and immutable objects. It assumes that the application can build the necessary storage semantics (such as mutable files) on top of it.

## 3.2 Distributed File Systems and Databases

Distributing data for performance, availability and durability has been widely studied in the file system and database systems community. Compared to P2P storage systems that only support flat namespaces, distributed file systems typically support hierarchical namespaces. Systems like Ficus [15] and Coda [19] replicate files for high availability at the expense of consistency. Update conflicts are typically managed using specialized conflict resolution procedures. The Farsite system [1] is a distributed file system that does not use any centralized server like NFS. Farsite achieves high availability and scalability using replication. The Google File System [6] is another distributed file system built for hosting the state of Google's internal applications. GFS uses a simple design with a single master server for hosting the entire metadata and where the data is split into chunks and stored in chunkservers. Bayou is a distributed relational database system that allows disconnected operations and provides eventual data consistency [21].

Among these systems, Bayou, Coda and Ficus allow disconnected operations and are resilient to issues such as network partitions and outages. These systems differ on their conflict resolution procedures. For instance, Coda and Ficus perform system level conflict resolution and Bayou allows application level resolution. All of them, however, guarantee eventual consistency. Similar to these systems, Dynamo allows read and write operations to continue even during network partitions and resolves updated conflicts using different conflict resolution mechanisms.

Distributed block storage systems like FAB [18] split large size objects into smaller blocks and stores each block in a highly available manner. In comparison to these systems, a key-value store is more suitable in this case because: (a) it is intended to store relatively small objects (size < 1M) and (b) key-value stores are easier to configure on a per-application basis. Antiquity is a wide-area distributed storage system designed to handle multiple server failures [23]. It uses a secure log to preserve data integrity, replicates each log on multiple servers for durability, and uses Byzantine fault tolerance protocols to ensure data consistency. In contrast to Antiquity, Dynamo does not focus on the problem of data integrity and security and is built for a trusted environment.

Bigtable is a distributed storage system for managing structured data. It maintains a sparse, multi-dimensional sorted map and allows applications to access their data using multiple attributes [2]. Compared to Bigtable, Dynamo targets applications that require only key/value access with primary focus on high availability where updates are not rejected even in the wake of network partitions or server failures.

Traditional replicated relational database systems focus on the problem of guaranteeing strong consistency to replicated data. Although strong consistency provides the application writer a convenient programming model, these systems are limited in scalability and availability [7]. These systems are not capable of handling network partitions because they typically provide strong consistency guarantees.

## 3.3 Discussion

Dynamo differs from the aforementioned decentralized storage systems in terms of its target requirements. First, Dynamo is targeted mainly at applications that need an "always writeable" data store where no updates are rejected due to failures or concurrent writes. This is a crucial requirement for many Amazon applications. Second, as noted earlier, Dynamo is built for an infrastructure within a single administrative domain where all nodes are assumed to be trusted. Third, applications that use Dynamo do not require support for hierarchical namespaces (a norm in many file systems) or complex relational schema (supported by traditional databases). Fourth, Dynamo is built for latency sensitive applications that require at least 99.9% of read and write operations to be performed within a few hundred milliseconds. To meet these stringent latency requirements, it was imperative for us to avoid routing requests through multiple nodes (which is the typical design adopted by several distributed hash table systems such as Chord and Pastry). This is because multi-hop routing increases variability in response times, thereby increasing the latency at higher percentiles. Dynamo can be characterized as a zero-hop DHT, where each node maintains enough routing information locally to route a request to the appropriate node directly.

---

### النسخة العربية

## 3.1 أنظمة من نظير إلى نظير

هناك العديد من أنظمة من نظير إلى نظير (P2P) التي نظرت في مشكلة تخزين البيانات وتوزيعها. كان الجيل الأول من أنظمة P2P، مثل Freenet و Gnutella، يُستخدم في الغالب كأنظمة مشاركة الملفات. كانت هذه أمثلة على شبكات P2P غير المنظمة حيث تم إنشاء روابط التراكب بين النظراء بشكل تعسفي. في هذه الشبكات، عادةً ما يتم إغراق استعلام البحث عبر الشبكة للعثور على أكبر عدد ممكن من النظراء الذين يشاركون البيانات. تطورت أنظمة P2P إلى الجيل التالي إلى ما يُعرف على نطاق واسع بالشبكات P2P المنظمة. تستخدم هذه الشبكات بروتوكولاً متسقاً عالمياً لضمان أن أي عقدة يمكنها توجيه استعلام بحث بكفاءة إلى نظير لديه البيانات المطلوبة. تستخدم أنظمة مثل Pastry [16] و Chord [20] آليات توجيه لضمان الإجابة على الاستعلامات ضمن عدد محدود من القفزات. لتقليل زمن الوصول الإضافي الذي يقدمه التوجيه متعدد القفزات، تستخدم بعض أنظمة P2P (مثل [14]) توجيه O(1) حيث تحتفظ كل نظير بمعلومات توجيه كافية محلياً بحيث يمكنها توجيه الطلبات (للوصول إلى عنصر بيانات) إلى النظير المناسب ضمن عدد ثابت من القفزات.

تم بناء أنظمة تخزين مختلفة، مثل Oceanstore [9] و PAST [17] فوق تراكبات التوجيه هذه. يوفر Oceanstore خدمة تخزين دائمة ومعاملاتية عالمية تدعم التحديثات المتسلسلة على البيانات المنسوخة تماثلياً على نطاق واسع. للسماح بالتحديثات المتزامنة مع تجنب العديد من المشاكل الكامنة في القفل واسع النطاق، يستخدم نموذج تحديث يعتمد على حل التعارضات. تم تقديم حل التعارضات في [21] لتقليل عدد عمليات إحباط المعاملات. يحل Oceanstore التعارضات عن طريق معالجة سلسلة من التحديثات، واختيار ترتيب كلي من بينها، ثم تطبيقها ذرياً بهذا الترتيب. تم بناؤه لبيئة حيث يتم نسخ البيانات على بنية تحتية غير موثوقة. بالمقارنة، يوفر PAST طبقة تجريد بسيطة فوق Pastry للكائنات الدائمة والثابتة. يفترض أن التطبيق يمكنه بناء دلالات التخزين الضرورية (مثل الملفات القابلة للتغيير) فوقها.

## 3.2 أنظمة الملفات الموزعة وقواعد البيانات

تم دراسة توزيع البيانات للأداء والتوافر والمتانة على نطاق واسع في مجتمع نظام الملفات وأنظمة قواعد البيانات. بالمقارنة مع أنظمة التخزين P2P التي تدعم فقط مساحات الأسماء المسطحة، تدعم أنظمة الملفات الموزعة عادةً مساحات الأسماء الهرمية. تنسخ أنظمة مثل Ficus [15] و Coda [19] الملفات تماثلياً لتحقيق توافر عالٍ على حساب الاتساق. تُدار تعارضات التحديث عادةً باستخدام إجراءات حل التعارضات المتخصصة. نظام Farsite [1] هو نظام ملفات موزع لا يستخدم أي خادم مركزي مثل NFS. يحقق Farsite توافراً عالياً وقابلية توسع باستخدام النسخ التماثلي. نظام ملفات جوجل [6] هو نظام ملفات موزع آخر تم بناؤه لاستضافة حالة تطبيقات جوجل الداخلية. يستخدم GFS تصميماً بسيطاً مع خادم رئيسي واحد لاستضافة البيانات الوصفية بالكامل وحيث يتم تقسيم البيانات إلى أجزاء وتخزينها في خوادم الأجزاء. Bayou هو نظام قاعدة بيانات علائقية موزع يسمح بالعمليات المنفصلة ويوفر اتساق البيانات النهائي [21].

من بين هذه الأنظمة، تسمح Bayou و Coda و Ficus بالعمليات المنفصلة ومرنة للقضايا مثل تقسيم الشبكة والانقطاعات. تختلف هذه الأنظمة في إجراءات حل التعارضات الخاصة بها. على سبيل المثال، يؤدي Coda و Ficus حل التعارضات على مستوى النظام ويسمح Bayou بالحل على مستوى التطبيق. ومع ذلك، جميعها تضمن الاتساق النهائي. على غرار هذه الأنظمة، يسمح ديناموا بمواصلة عمليات القراءة والكتابة حتى أثناء تقسيم الشبكة ويحل تعارضات التحديث باستخدام آليات حل التعارضات المختلفة.

أنظمة تخزين الكتل الموزعة مثل FAB [18] تقسم الكائنات ذات الحجم الكبير إلى كتل أصغر وتخزن كل كتلة بطريقة عالية التوافر. بالمقارنة مع هذه الأنظمة، يكون مخزن المفتاح-القيمة أكثر ملاءمة في هذه الحالة لأن: (أ) الهدف منه هو تخزين كائنات صغيرة نسبياً (الحجم < 1M) و (ب) من الأسهل تكوين مخازن المفتاح-القيمة على أساس كل تطبيق على حدة. Antiquity هو نظام تخزين موزع واسع النطاق مصمم للتعامل مع فشل خوادم متعددة [23]. يستخدم سجلاً آمناً للحفاظ على سلامة البيانات، وينسخ كل سجل على خوادم متعددة من أجل المتانة، ويستخدم بروتوكولات تحمل الأخطاء البيزنطية لضمان اتساق البيانات. على النقيض من Antiquity، لا يركز ديناموا على مشكلة سلامة البيانات والأمن وتم بناؤه لبيئة موثوقة.

Bigtable هو نظام تخزين موزع لإدارة البيانات المهيكلة. يحتفظ بخريطة متفرقة ومرتبة ومتعددة الأبعاد ويسمح للتطبيقات بالوصول إلى بياناتها باستخدام سمات متعددة [2]. بالمقارنة مع Bigtable، يستهدف ديناموا التطبيقات التي تتطلب فقط وصول المفتاح/القيمة مع التركيز الأساسي على التوافر العالي حيث لا يتم رفض التحديثات حتى في أعقاب تقسيم الشبكة أو فشل الخادم.

تركز أنظمة قواعد البيانات العلائقية المنسوخة تماثلياً التقليدية على مشكلة ضمان الاتساق القوي للبيانات المنسوخة. على الرغم من أن الاتساق القوي يوفر لكاتب التطبيق نموذج برمجة مريح، فإن هذه الأنظمة محدودة في قابلية التوسع والتوافر [7]. هذه الأنظمة غير قادرة على التعامل مع تقسيم الشبكة لأنها عادةً ما توفر ضمانات اتساق قوية.

## 3.3 مناقشة

يختلف ديناموا عن أنظمة التخزين اللامركزية المذكورة أعلاه من حيث متطلباته المستهدفة. أولاً، يستهدف ديناموا بشكل رئيسي التطبيقات التي تحتاج إلى مخزن بيانات "قابل للكتابة دائماً" حيث لا يتم رفض أي تحديثات بسبب الإخفاقات أو الكتابات المتزامنة. هذا مطلب حاسم للعديد من تطبيقات أمازون. ثانياً، كما لوحظ سابقاً، تم بناء ديناموا لبنية تحتية ضمن مجال إداري واحد حيث يُفترض أن جميع العقد موثوقة. ثالثاً، التطبيقات التي تستخدم ديناموا لا تتطلب دعماً لمساحات الأسماء الهرمية (معيار في العديد من أنظمة الملفات) أو المخططات العلائقية المعقدة (التي تدعمها قواعد البيانات التقليدية). رابعاً، تم بناء ديناموا للتطبيقات الحساسة لزمن الوصول والتي تتطلب إجراء 99.9% على الأقل من عمليات القراءة والكتابة خلال بضع مئات من المللي ثانية. لتلبية متطلبات زمن الوصول الصارمة هذه، كان من الضروري بالنسبة لنا تجنب توجيه الطلبات عبر عقد متعددة (وهو التصميم النموذجي الذي تتبناه العديد من أنظمة جدول التجزئة الموزع مثل Chord و Pastry). هذا لأن التوجيه متعدد القفزات يزيد من التباين في أوقات الاستجابة، وبالتالي زيادة زمن الوصول عند النسب المئوية الأعلى. يمكن وصف ديناموا بأنه جدول تجزئة موزع بدون قفزات (zero-hop DHT)، حيث تحتفظ كل عقدة بمعلومات توجيه كافية محلياً لتوجيه طلب إلى العقدة المناسبة مباشرة.

---

### Translation Notes

- **Key systems/projects mentioned (kept in English):**
  - Freenet, Gnutella, Pastry, Chord, Oceanstore, PAST, Ficus, Coda, Farsite, GFS (Google File System), Bayou, FAB, Antiquity, Bigtable, NFS

- **Key technical terms:**
  - "Unstructured P2P networks" → "شبكات P2P غير المنظمة"
  - "Structured P2P networks" → "الشبكات P2P المنظمة"
  - "Overlay links" → "روابط التراكب"
  - "Multi-hop routing" → "التوجيه متعدد القفزات"
  - "O(1) routing" → "توجيه O(1)"
  - "Transactional storage" → "تخزين معاملاتي"
  - "Serialized updates" → "التحديثات المتسلسلة"
  - "Wide-area locking" → "القفل واسع النطاق"
  - "Total order" → "ترتيب كلي"
  - "Hierarchical namespaces" → "مساحات الأسماء الهرمية"
  - "Flat namespaces" → "مساحات الأسماء المسطحة"
  - "Block storage" → "تخزين الكتل"
  - "Byzantine fault tolerance" → "تحمل الأخطاء البيزنطية"
  - "Zero-hop DHT" → "جدول تجزئة موزع بدون قفزات"
  - "Single administrative domain" → "مجال إداري واحد"

- **Figures referenced:** None
- **Citations:** [1], [2], [6], [7], [9], [14], [15], [16], [17], [18], [19], [20], [21], [23]

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check (Key Paragraph)

"Dynamo differs from the aforementioned decentralized storage systems in terms of its target requirements. First, Dynamo is targeted mainly at applications that need an 'always writeable' data store where no updates are rejected due to failures or concurrent writes. This is a crucial requirement for many Amazon applications. Second, as noted earlier, Dynamo is built for an infrastructure within a single administrative domain where all nodes are assumed to be trusted. Third, applications that use Dynamo do not require support for hierarchical namespaces (a norm in many file systems) or complex relational schemas (supported by traditional databases). Fourth, Dynamo is built for latency-sensitive applications that require at least 99.9% of read and write operations to be performed within a few hundred milliseconds."

✓ Semantic match confirmed
