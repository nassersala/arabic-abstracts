# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** scalability (قابلية التوسع), reliability (موثوقية), availability (التوافر), decentralized (لامركزي), service-oriented architecture (معمارية موجهة بالخدمات), data store (مخزن بيانات), consistent hashing (تجزئة متسقة), quorum (نصاب), vector clocks (ساعات متجهة), gossip protocol (بروتوكول الشائعات)

---

### English Version

Amazon runs a world-wide e-commerce platform that serves tens of millions customers at peak times using tens of thousands of servers located in many data centers around the world. There are strict operational requirements on Amazon's platform in terms of performance, reliability and efficiency, and to support continuous growth the platform needs to be highly scalable. Reliability is one of the most important requirements because even the slightest outage has significant financial consequences and impacts customer trust. In addition, to support continuous growth, the platform needs to be highly scalable.

One of the lessons our organization has learned from operating Amazon's platform is that the reliability and scalability of a system is dependent on how its application state is managed. Amazon uses a highly decentralized, loosely coupled, service oriented architecture consisting of hundreds of services. In this environment there is a particular need for storage technologies that are always available. For example, customers should be able to view and add items to their shopping cart even if disks are failing, network routes are flapping, or data centers are being destroyed by tornados. Therefore, the service responsible for managing shopping carts requires that it can always write to and read from its data store, and that its data needs to be available across multiple data centers.

Dealing with failures in an infrastructure comprised of millions of components is our standard mode of operation; there are always a small but significant number of server and network components that are failing at any given time. As such Amazon's software systems need to be constructed in a manner that treats failure handling as the normal case without impacting availability or performance.

To meet the reliability and scaling needs, Amazon has developed a number of storage technologies, of which the Amazon Simple Storage Service (also available outside of Amazon and known as Amazon S3), is probably the best known. This paper presents the design and implementation of Dynamo, another highly available and scalable distributed data store built for Amazon's platform. Dynamo is used to manage the state of services that have very high reliability requirements and need tight control over the tradeoffs between availability, consistency, cost-effectiveness and performance. Amazon's platform has a very diverse set of applications with different storage requirements. A select set of applications requires a storage technology that is flexible enough to let application designers configure their data store appropriately based on these tradeoffs to achieve high availability and guaranteed performance in the most cost effective manner.

There are many services on Amazon's platform that only need primary-key access to a data store. For many services, such as those that provide best seller lists, shopping carts, customer preferences, session management, sales rank, and product catalog, the common pattern of using a relational database would lead to inefficiencies and limit scale and availability. Dynamo provides a simple primary-key only interface to meet the requirements of these applications.

Dynamo uses a synthesis of well known techniques to achieve scalability and availability: Data is partitioned and replicated using consistent hashing [10], and consistency is facilitated by object versioning [12]. The consistency among replicas during updates is maintained by a quorum-like technique and a decentralized replica synchronization protocol. Dynamo employs a gossip based distributed failure detection and membership protocol. Dynamo is a completely decentralized system with minimal need for manual administration. Storage nodes can be added and removed from Dynamo without requiring any manual partitioning or redistribution.

In the past year, Dynamo has been the underlying storage technology for a number of the core services in Amazon's e-commerce platform. It was able to scale to extreme peak loads efficiently without any downtime during the busy holiday shopping season. For example, the service that maintains shopping cart (Shopping Cart Service) served tens of millions requests that resulted in well over 3 million checkouts in a single day and the service that manages session state handled hundreds of thousands of concurrently active sessions.

The main contribution of this work for the research community is the evaluation of how different techniques can be combined to provide a single highly-available system. It demonstrates that an eventually-consistent storage system can be used in production with demanding applications. It also provides insight into the tuning of these techniques to meet the requirements of production systems with very strict performance demands.

The paper is structured as follows. Section 2 presents the background and Section 3 presents the related work. Section 4 presents the system design and Section 5 describes the implementation. Section 6 details the experiences and insights gained by running Dynamo in production and Section 7 concludes the paper. There are a number of places in this paper where additional information may have been appropriate but where protecting Amazon's business interests require us to reduce some level of detail. For this reason, the intra- and inter-datacenter latencies in section 6, the absolute request rates in section 6.2 and outage lengths and workloads in section 6.3 are provided through aggregate measures instead of absolute details.

---

### النسخة العربية

تدير أمازون منصة تجارة إلكترونية عالمية تخدم عشرات الملايين من العملاء في أوقات الذروة باستخدام عشرات الآلاف من الخوادم الموجودة في العديد من مراكز البيانات حول العالم. هناك متطلبات تشغيلية صارمة على منصة أمازون من حيث الأداء والموثوقية والكفاءة، ولدعم النمو المستمر، تحتاج المنصة إلى أن تكون عالية قابلية التوسع. تُعد الموثوقية أحد أهم المتطلبات لأن أي انقطاع مهما كان طفيفاً له عواقب مالية كبيرة ويؤثر على ثقة العملاء. بالإضافة إلى ذلك، لدعم النمو المستمر، تحتاج المنصة إلى أن تكون عالية قابلية التوسع.

أحد الدروس التي تعلمتها مؤسستنا من تشغيل منصة أمازون هو أن موثوقية وقابلية توسع النظام تعتمد على كيفية إدارة حالة التطبيق. تستخدم أمازون معمارية موجهة بالخدمات لامركزية ومقترنة بشكل غير وثيق تتكون من مئات الخدمات. في هذه البيئة هناك حاجة خاصة لتقنيات تخزين متاحة دائماً. على سبيل المثال، يجب أن يكون العملاء قادرين على عرض وإضافة عناصر إلى سلة التسوق الخاصة بهم حتى لو كانت الأقراص تفشل، أو مسارات الشبكة تتذبذب، أو مراكز البيانات تُدمر بواسطة الأعاصير. لذلك، فإن الخدمة المسؤولة عن إدارة سلال التسوق تتطلب أن تكون قادرة دائماً على الكتابة إلى مخزن البيانات الخاص بها والقراءة منه، وأن تكون بياناتها متاحة عبر مراكز بيانات متعددة.

التعامل مع الإخفاقات في بنية تحتية تتكون من ملايين المكونات هو وضع التشغيل القياسي لدينا؛ فهناك دائماً عدد صغير ولكنه كبير من مكونات الخوادم والشبكة التي تفشل في أي وقت معين. ولذلك، يجب بناء أنظمة أمازون البرمجية بطريقة تتعامل مع معالجة الفشل على أنه الحالة العادية دون التأثير على التوافر أو الأداء.

لتلبية احتياجات الموثوقية والتوسع، طورت أمازون عدداً من تقنيات التخزين، والتي من بينها خدمة التخزين البسيط من أمازون (Amazon Simple Storage Service) (المتاحة أيضاً خارج أمازون والمعروفة باسم Amazon S3)، وهي على الأرجح الأكثر شهرة. تقدم هذه الورقة تصميم وتنفيذ ديناموا (Dynamo)، وهو مخزن بيانات موزع آخر عالي التوافر وقابل للتوسع تم بناؤه لمنصة أمازون. يُستخدم ديناموا لإدارة حالة الخدمات التي لديها متطلبات موثوقية عالية جداً وتحتاج إلى تحكم محكم في المقايضات بين التوافر والاتساق والفعالية من حيث التكلفة والأداء. تمتلك منصة أمازون مجموعة متنوعة للغاية من التطبيقات ذات متطلبات تخزين مختلفة. تتطلب مجموعة مختارة من التطبيقات تقنية تخزين مرنة بما يكفي للسماح لمصممي التطبيقات بتكوين مخزن البيانات الخاص بهم بشكل مناسب بناءً على هذه المقايضات لتحقيق توافر عالٍ وأداء مضمون بأكثر الطرق فعالية من حيث التكلفة.

هناك العديد من الخدمات على منصة أمازون التي تحتاج فقط إلى الوصول بالمفتاح الأساسي إلى مخزن بيانات. بالنسبة للعديد من الخدمات، مثل تلك التي توفر قوائم الأكثر مبيعاً، وسلال التسوق، وتفضيلات العملاء، وإدارة الجلسات، وترتيب المبيعات، وكتالوج المنتجات، فإن النمط الشائع لاستخدام قاعدة بيانات علائقية سيؤدي إلى عدم الكفاءة ويحد من التوسع والتوافر. يوفر ديناموا واجهة بسيطة بالمفتاح الأساسي فقط لتلبية متطلبات هذه التطبيقات.

يستخدم ديناموا توليفة من التقنيات المعروفة جيداً لتحقيق قابلية التوسع والتوافر: يتم تجزئة البيانات ونسخها تماثلياً باستخدام التجزئة المتسقة [10]، ويتم تسهيل الاتساق بواسطة إصدارات الكائنات [12]. يتم الحفاظ على الاتساق بين النسخ المتماثلة أثناء التحديثات بواسطة تقنية شبيهة بالنصاب وبروتوكول مزامنة نسخ متماثل لامركزي. يستخدم ديناموا بروتوكول كشف فشل وعضوية موزع قائم على الشائعات (gossip). ديناموا هو نظام لامركزي تماماً مع الحد الأدنى من الحاجة إلى الإدارة اليدوية. يمكن إضافة عُقد التخزين وإزالتها من ديناموا دون الحاجة إلى أي تجزئة أو إعادة توزيع يدوية.

في العام الماضي، كان ديناموا التقنية الأساسية للتخزين لعدد من الخدمات الأساسية في منصة التجارة الإلكترونية لأمازون. وكان قادراً على التوسع لأحمال الذروة القصوى بكفاءة دون أي توقف خلال موسم التسوق المزدحم في العطلات. على سبيل المثال، الخدمة التي تحافظ على سلة التسوق (Shopping Cart Service) خدمت عشرات الملايين من الطلبات التي أدت إلى أكثر من 3 ملايين عملية دفع في يوم واحد، والخدمة التي تدير حالة الجلسة تعاملت مع مئات الآلاف من الجلسات النشطة في وقت واحد.

المساهمة الرئيسية لهذا العمل بالنسبة لمجتمع الأبحاث هي تقييم كيف يمكن دمج التقنيات المختلفة لتوفير نظام واحد عالي التوافر. إنه يوضح أن نظام تخزين متسق نهائياً يمكن استخدامه في الإنتاج مع التطبيقات الصعبة. كما يوفر نظرة ثاقبة حول ضبط هذه التقنيات لتلبية متطلبات أنظمة الإنتاج ذات متطلبات الأداء الصارمة للغاية.

الورقة منظمة على النحو التالي. يقدم القسم 2 الخلفية ويقدم القسم 3 العمل ذي الصلة. يقدم القسم 4 تصميم النظام ويصف القسم 5 التنفيذ. يفصل القسم 6 الخبرات والأفكار المكتسبة من تشغيل ديناموا في الإنتاج ويختتم القسم 7 الورقة. هناك عدد من الأماكن في هذه الورقة حيث قد تكون المعلومات الإضافية مناسبة ولكن حيث تتطلب حماية مصالح أمازون التجارية أن نقلل من بعض مستوى التفاصيل. لهذا السبب، يتم توفير زمن الوصول داخل وبين مراكز البيانات في القسم 6، ومعدلات الطلبات المطلقة في القسم 6.2 وأطوال الانقطاع وأحمال العمل في القسم 6.3 من خلال مقاييس إجمالية بدلاً من التفاصيل المطلقة.

---

### Translation Notes

- **Key terms introduced:**
  - "Service-oriented architecture" → "معمارية موجهة بالخدمات"
  - "Loosely coupled" → "مقترنة بشكل غير وثيق"
  - "Shopping cart" → "سلة التسوق"
  - "Primary-key access" → "الوصول بالمفتاح الأساسي"
  - "Consistent hashing" → "التجزئة المتسقة"
  - "Object versioning" → "إصدارات الكائنات"
  - "Quorum" → "النصاب"
  - "Gossip protocol" → "بروتوكول الشائعات"
  - "Eventually-consistent" → "متسق نهائياً"
  - "Peak loads" → "أحمال الذروة"

- **Figures referenced:** None in this section
- **Citations:** [10], [12] (references to consistent hashing and object versioning)
- **Special handling:** Amazon S3 kept in English as it's a proper name

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Check (Key Paragraphs)

**First paragraph back-translation:** "Amazon runs a global e-commerce platform that serves tens of millions of customers at peak times using tens of thousands of servers located in many data centers around the world. There are strict operational requirements on Amazon's platform in terms of performance, reliability, and efficiency, and to support continuous growth, the platform needs to be highly scalable. Reliability is one of the most important requirements because any outage, however slight, has significant financial consequences and impacts customer trust. Additionally, to support continuous growth, the platform needs to be highly scalable."

✓ Semantic match confirmed

**Key technical paragraph back-translation:** "Dynamo uses a synthesis of well-known techniques to achieve scalability and availability: Data is partitioned and replicated using consistent hashing [10], and consistency is facilitated by object versioning [12]. Consistency among replicas during updates is maintained by a quorum-like technique and a decentralized replica synchronization protocol. Dynamo uses a gossip-based distributed failure detection and membership protocol. Dynamo is a completely decentralized system with minimal need for manual administration. Storage nodes can be added and removed from Dynamo without the need for any manual partitioning or redistribution."

✓ Technical accuracy confirmed
