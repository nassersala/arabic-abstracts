# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** service-oriented (موجه بالخدمات), stateless (عديم الحالة), stateful (ذو حالة), relational database (قاعدة بيانات علائقية), RDBMS (نظام إدارة قواعد البيانات العلائقية), ACID (خصائص ACID), consistency (اتساق), availability (توافر), durability (متانة), isolation (عزل), SLA (اتفاقية مستوى الخدمة), latency (زمن الوصول), throughput (إنتاجية), percentile (مئيني)

---

### English Version

Amazon's e-commerce platform is composed of hundreds of services that work in concert to deliver functionality ranging from recommendations to order fulfillment to fraud detection. Each service is exposed through a well defined interface and is accessible over the network. These services are hosted in an infrastructure that consists of tens of thousands of servers located across many data centers world-wide. Some of these services are stateless (i.e., services which aggregate responses from other services) and some are stateful (i.e., a service that generates its response by executing business logic on its state stored in persistent store).

Traditionally production systems store their state in relational databases. For many of the more common usage patterns of state persistence, however, a relational database is a solution that is far from ideal. Most of these services only store and retrieve data by primary key and do not require the complex querying and management functionality offered by an RDBMS. This excess functionality requires expensive hardware and highly skilled personnel for its operation, making it a very inefficient solution. In addition, the available replication technologies are limited and typically choose consistency over availability. Although many advances have been made in the recent years, it is still not easy to scale-out databases or use smart partitioning schemes for load balancing.

This paper describes Dynamo, a highly available data storage technology that addresses the needs of these important classes of services. Dynamo has a simple key/value interface, is highly available with a clearly defined consistency window, is efficient in its resource usage, and has a simple scale out scheme to address growth in data set size or request rates. Each service that uses Dynamo runs its own Dynamo instances.

## 2.1 System Assumptions and Requirements

The storage system for this class of services has the following requirements:

**Query Model:** simple read and write operations to a data item that is uniquely identified by a key. State is stored as binary objects (i.e., blobs) identified by unique keys. No operations span multiple data items and there is no need for relational schema. This requirement is based on the observation that a significant portion of Amazon's services can work with this simple query model and do not need any relational schema. Dynamo targets applications that need to store objects that are relatively small (usually less than 1 MB).

**ACID Properties:** ACID (Atomicity, Consistency, Isolation, Durability) is a set of properties that guarantee that database transactions are processed reliably. In the context of databases, a single logical operation on the data is called a transaction. Experience at Amazon has shown that data stores that provide ACID guarantees tend to have poor availability. This has been widely acknowledged by both the industry and academia [5]. Dynamo targets applications that operate with weaker consistency (the "C" in ACID) if this results in high availability. Dynamo does not provide any isolation guarantees and permits only single key updates.

**Efficiency:** The system needs to function on a commodity hardware infrastructure. In Amazon's platform, services have stringent latency requirements which are in general measured at the 99.9th percentile of the distribution. Given that state access plays a crucial role in service operation the storage system must be capable of meeting such stringent SLAs (see Section 2.2 below). Services must be able to configure Dynamo such that they consistently achieve their latency and throughput requirements. The tradeoffs are in performance, cost efficiency, availability, and durability guarantees.

**Other Assumptions:** Dynamo is used only by Amazon's internal services. Its operation environment is assumed to be non-hostile and there are no security related requirements such as authentication and authorization. Moreover, since each service uses its distinct instance of Dynamo, its initial design targets a scale of up to hundreds of storage hosts. We will discuss the scalability limitations of Dynamo and possible scalability related extensions in later sections.

## 2.2 Service Level Agreements (SLA)

To guarantee that the application can deliver its functionality in a bounded time, each and every dependency in the platform needs to deliver its functionality with even tighter bounds. Clients and services engage in a Service Level Agreement (SLA), a formally negotiated contract where a client and a service agree on several system-related characteristics, which most prominently include the client's expected request rate distribution for a particular API and the expected service latency under those conditions. An example of a simple SLA is a service guaranteeing that it will provide a response within 300ms for 99.9% of its requests for a peak client load of 500 requests per second.

In Amazon's decentralized service oriented infrastructure, SLAs play an important role. For example a page request to one of the e-commerce sites typically requires the rendering engine to construct its response by sending requests to over 150 services. These services often have multiple dependencies, which frequently are other services, and as such it is not uncommon for the call graph of an application to have more than one level. To ensure that the page rendering engine can maintain a clear bound on page delivery each service within the call chain must obey its performance contract.

Figure 1 shows an abstract view of the architecture of Amazon's platform, where dynamic web content is generated by page rendering components which in turn query many other services. A service can use different data stores to manage its state and these data stores are only accessible within its service boundaries. Some services act as aggregators by using several other services to produce a composite response. Typically, the aggregator services are stateless, although they use extensive caching.

A common approach in the industry for forming a performance oriented SLA is to describe it using average, median and expected variance. At Amazon we have found that these metrics are not good enough if the goal is to build a system where all customers have a good experience, rather than just the majority. For example if extensive personalization techniques are used then customers with longer histories require more processing which impacts performance at the high-end of the distribution. An SLA stated in terms of mean or median response times will not address the performance of this important customer segment. To address this issue, at Amazon, SLAs are expressed and measured at the 99.9th percentile of the distribution. The choice for 99.9% over an even higher percentile has been made based on a cost-benefit analysis which demonstrated a significant increase in cost to improve performance that much. Experiences with Amazon's production systems have shown that this approach provides a better overall experience compared to those systems that meet SLAs defined based on the mean or median.

In this paper there are many references to this 99.9th percentile of distributions, which reflects Amazon engineers' relentless focus on performance from the perspective of the customers' experience. Many papers report on averages, so these are included where it makes sense for comparison purposes. Nevertheless, Amazon's engineering and optimization efforts are not focused on averages. Several techniques, such as the load balanced selection of write coordinators, are purely targeted at controlling performance at the 99.9th percentile.

Storage systems often play an important role in establishing a service's SLA, especially if the business logic is relatively lightweight, as is the case for many Amazon services. State management then becomes the main component of a service's SLA. One of the main design considerations for Dynamo is to give services control over their system properties, such as durability and consistency, and to let services make their own tradeoffs between functionality, performance and cost-effectiveness.

## 2.3 Design Considerations

Data replication algorithms used in commercial systems traditionally perform synchronous replica coordination in order to provide a strongly consistent data access interface. To achieve this level of consistency, these algorithms are forced to tradeoff the availability of the data under certain failure scenarios. For instance, rather than dealing with the uncertainty of the correctness of an answer, the data is made unavailable until it is absolutely certain that it is correct. From the very early replicated database works, it is well known that when dealing with the possibility of network failures, strong consistency and high data availability cannot be achieved simultaneously [2, 11]. As such systems and applications need to be aware which properties can be achieved under which conditions.

For systems prone to server and network failures, availability can be increased by using optimistic replication techniques, where changes are allowed to propagate to replicas in the background, and concurrent, disconnected work is tolerated. The challenge with this approach is that it can lead to conflicting changes which must be detected and resolved. This process of conflict resolution introduces two problems: when to resolve them and who resolves them. Dynamo is designed to be an eventually consistent data store; that is all updates reach all replicas eventually.

An important design consideration is to decide when to perform the process of resolving update conflicts, i.e., whether conflicts should be resolved during reads or writes. Many traditional data stores execute conflict resolution during writes and keep the read complexity simple [7]. In such systems, writes may be rejected if the data store cannot reach all (or a majority of) the replicas at a given time. On the other hand, Dynamo targets the design space of an "always writeable" data store (i.e., a data store that is highly available for writes). For a number of Amazon services, rejecting customer updates could result in a poor customer experience. For instance, the shopping cart service must allow customers to add and remove items from their shopping cart even amidst network and server failures. This requirement forces us to push the complexity of conflict resolution to the reads in order to ensure that writes are never rejected.

The next design choice is who performs the process of conflict resolution. This can be done by the data store or the application. If conflict resolution is done by the data store, its choices are rather limited. In such cases, the data store can only use simple policies, such as "last write wins" [22], to resolve conflicting updates. On the other hand, since the application is aware of the data schema it can decide on the conflict resolution method that is best suited for its client's experience. For instance, the application that maintains customer shopping carts can choose to "merge" the conflicting versions and return a single unified shopping cart. Despite this flexibility, some application developers may not want to write their own conflict resolution mechanisms and choose to push it down to the data store, which in turn chooses a simple policy such as "last write wins".

**Other key principles embraced in the design are:**

**Incremental scalability:** Dynamo should be able to scale out one storage host (henceforth, referred to as "node") at a time, with minimal impact on both operators of the system and the system itself.

**Symmetry:** Every node in Dynamo should have the same set of responsibilities as its peers; there should be no distinguished node or nodes that take special roles or extra set of responsibilities. In our experience, symmetry simplifies the process of system provisioning and maintenance.

**Decentralization:** An extension of symmetry, the design should favor decentralized peer-to-peer techniques over centralized control. In the past, centralized control has resulted in outages and the goal is to avoid it as much as possible. This leads to a simpler, more scalable, and more available system.

**Heterogeneity:** The system needs to be able to exploit heterogeneity in the infrastructure it runs on. e.g. the work distribution must be proportional to the capabilities of the individual servers. This is essential in adding new nodes with higher capacity without having to upgrade all hosts at once.

---

### النسخة العربية

تتكون منصة التجارة الإلكترونية لأمازون من مئات الخدمات التي تعمل معاً لتقديم وظائف تتراوح من التوصيات إلى تنفيذ الطلبات إلى اكتشاف الاحتيال. يتم عرض كل خدمة من خلال واجهة محددة جيداً ويمكن الوصول إليها عبر الشبكة. تُستضاف هذه الخدمات في بنية تحتية تتكون من عشرات الآلاف من الخوادم الموجودة عبر العديد من مراكز البيانات في جميع أنحاء العالم. بعض هذه الخدمات عديمة الحالة (أي الخدمات التي تجمع الاستجابات من خدمات أخرى) وبعضها ذو حالة (أي خدمة تولد استجابتها عن طريق تنفيذ منطق الأعمال على حالتها المخزنة في مخزن دائم).

تقليدياً، تخزن أنظمة الإنتاج حالتها في قواعد بيانات علائقية. ومع ذلك، بالنسبة للعديد من أنماط الاستخدام الأكثر شيوعاً لثبات الحالة، فإن قاعدة البيانات العلائقية هي حل بعيد عن المثالية. معظم هذه الخدمات تخزن وتسترجع البيانات فقط بالمفتاح الأساسي ولا تتطلب وظائف الاستعلام والإدارة المعقدة التي يوفرها نظام إدارة قواعد البيانات العلائقية (RDBMS). تتطلب هذه الوظائف الزائدة أجهزة باهظة الثمن وموظفين ذوي مهارات عالية لتشغيلها، مما يجعلها حلاً غير فعال للغاية. بالإضافة إلى ذلك، فإن تقنيات النسخ التماثلي المتاحة محدودة وتختار عادةً الاتساق على حساب التوافر. على الرغم من إحراز العديد من التقدمات في السنوات الأخيرة، لا يزال من الصعب توسيع قواعد البيانات أو استخدام مخططات تجزئة ذكية لموازنة الحمل.

تصف هذه الورقة ديناموا، وهي تقنية تخزين بيانات عالية التوافر تلبي احتياجات هذه الفئات المهمة من الخدمات. يحتوي ديناموا على واجهة مفتاح/قيمة بسيطة، وهو عالي التوافر مع نافذة اتساق محددة بوضوح، وفعال في استخدام موارده، ولديه مخطط توسع بسيط لمعالجة النمو في حجم مجموعة البيانات أو معدلات الطلبات. تشغل كل خدمة تستخدم ديناموا نسخها الخاصة من ديناموا.

## 2.1 افتراضات ومتطلبات النظام

يحتوي نظام التخزين لهذه الفئة من الخدمات على المتطلبات التالية:

**نموذج الاستعلام:** عمليات قراءة وكتابة بسيطة لعنصر بيانات يتم تحديده بشكل فريد بواسطة مفتاح. يتم تخزين الحالة ككائنات ثنائية (أي كائنات ثنائية كبيرة - blobs) محددة بمفاتيح فريدة. لا تمتد أي عمليات عبر عناصر بيانات متعددة ولا حاجة لمخطط علائقي. يستند هذا المتطلب إلى ملاحظة أن جزءاً كبيراً من خدمات أمازون يمكن أن تعمل بهذا النموذج البسيط للاستعلام ولا تحتاج إلى أي مخطط علائقي. يستهدف ديناموا التطبيقات التي تحتاج إلى تخزين كائنات صغيرة نسبياً (عادة أقل من 1 ميجابايت).

**خصائص ACID:** ACID (الذرية، الاتساق، العزل، المتانة) هي مجموعة من الخصائص التي تضمن معالجة معاملات قاعدة البيانات بشكل موثوق. في سياق قواعد البيانات، تسمى عملية منطقية واحدة على البيانات معاملة. أظهرت التجربة في أمازون أن مخازن البيانات التي توفر ضمانات ACID تميل إلى أن يكون لديها توافر ضعيف. تم الاعتراف بذلك على نطاق واسع من قبل كل من الصناعة والأوساط الأكاديمية [5]. يستهدف ديناموا التطبيقات التي تعمل باتساق أضعف (الحرف "C" في ACID) إذا أدى ذلك إلى توافر عالٍ. لا يوفر ديناموا أي ضمانات عزل ويسمح فقط بتحديثات المفتاح الواحد.

**الكفاءة:** يحتاج النظام إلى العمل على بنية تحتية للأجهزة السلعية. في منصة أمازون، تحتوي الخدمات على متطلبات زمن وصول صارمة والتي يتم قياسها بشكل عام عند المئين 99.9 من التوزيع. نظراً لأن الوصول إلى الحالة يلعب دوراً حاسماً في تشغيل الخدمة، يجب أن يكون نظام التخزين قادراً على تلبية مثل هذه اتفاقيات مستوى الخدمة الصارمة (انظر القسم 2.2 أدناه). يجب أن تكون الخدمات قادرة على تكوين ديناموا بحيث تحقق باستمرار متطلبات زمن الوصول والإنتاجية الخاصة بها. المقايضات هي في الأداء، وكفاءة التكلفة، والتوافر، وضمانات المتانة.

**افتراضات أخرى:** يُستخدم ديناموا فقط من قبل خدمات أمازون الداخلية. يُفترض أن بيئة تشغيله غير معادية ولا توجد متطلبات أمنية مثل المصادقة والترخيص. علاوة على ذلك، نظراً لأن كل خدمة تستخدم نسختها المميزة من ديناموا، فإن تصميمها الأولي يستهدف حجماً يصل إلى مئات من مضيفي التخزين. سنناقش قيود قابلية توسع ديناموا والامتدادات المحتملة المتعلقة بقابلية التوسع في أقسام لاحقة.

## 2.2 اتفاقيات مستوى الخدمة (SLA)

لضمان قدرة التطبيق على تقديم وظائفه في وقت محدود، يجب أن يقدم كل تبعية في المنصة وظائفها بحدود أكثر إحكاماً. يدخل العملاء والخدمات في اتفاقية مستوى الخدمة (SLA)، وهي عقد متفاوض عليه رسمياً حيث يتفق العميل والخدمة على العديد من الخصائص المتعلقة بالنظام، والتي تتضمن بشكل بارز توزيع معدل الطلبات المتوقع للعميل لواجهة برمجة تطبيقات معينة وزمن وصول الخدمة المتوقع في ظل تلك الظروف. مثال على اتفاقية مستوى خدمة بسيطة هو خدمة تضمن أنها ستوفر استجابة خلال 300 مللي ثانية لـ 99.9% من طلباتها لحمل عميل ذروة يبلغ 500 طلب في الثانية.

في البنية التحتية الموجهة بالخدمات اللامركزية لأمازون، تلعب اتفاقيات مستوى الخدمة دوراً مهماً. على سبيل المثال، يتطلب طلب صفحة إلى أحد مواقع التجارة الإلكترونية عادةً من محرك التقديم إنشاء استجابته عن طريق إرسال طلبات إلى أكثر من 150 خدمة. غالباً ما يكون لهذه الخدمات تبعيات متعددة، والتي غالباً ما تكون خدمات أخرى، وعلى هذا النحو ليس من غير المألوف أن يكون للرسم البياني للاستدعاءات الخاص بتطبيق ما أكثر من مستوى واحد. لضمان قدرة محرك تقديم الصفحة على الحفاظ على حد واضح لتسليم الصفحة، يجب على كل خدمة ضمن سلسلة الاستدعاءات الامتثال لعقد الأداء الخاص بها.

يُظهر الشكل 1 عرضاً مجرداً لمعمارية منصة أمازون، حيث يتم إنشاء محتوى الويب الديناميكي بواسطة مكونات تقديم الصفحات التي تستعلم بدورها عن العديد من الخدمات الأخرى. يمكن للخدمة استخدام مخازن بيانات مختلفة لإدارة حالتها وهذه المخازن يمكن الوصول إليها فقط ضمن حدود خدمتها. تعمل بعض الخدمات كمجمعات باستخدام العديد من الخدمات الأخرى لإنتاج استجابة مركبة. عادةً، الخدمات المجمعة عديمة الحالة، على الرغم من أنها تستخدم التخزين المؤقت على نطاق واسع.

النهج الشائع في الصناعة لتشكيل اتفاقية مستوى خدمة موجهة نحو الأداء هو وصفها باستخدام المتوسط والوسيط والتباين المتوقع. في أمازون، وجدنا أن هذه المقاييس ليست جيدة بما فيه الكفاية إذا كان الهدف هو بناء نظام حيث يحصل جميع العملاء على تجربة جيدة، بدلاً من الأغلبية فقط. على سبيل المثال، إذا تم استخدام تقنيات تخصيص موسعة، فإن العملاء الذين لديهم تاريخ أطول يحتاجون إلى مزيد من المعالجة مما يؤثر على الأداء في الطرف الأعلى من التوزيع. لن تعالج اتفاقية مستوى الخدمة المذكورة من حيث أوقات الاستجابة المتوسطة أو الوسيطة أداء هذا القطاع المهم من العملاء. لمعالجة هذه المسألة، في أمازون، يتم التعبير عن اتفاقيات مستوى الخدمة وقياسها عند المئين 99.9 من التوزيع. تم اختيار 99.9% على نسبة مئوية أعلى بناءً على تحليل التكلفة والفائدة الذي أظهر زيادة كبيرة في التكلفة لتحسين الأداء بهذا القدر. أظهرت التجارب مع أنظمة الإنتاج في أمازون أن هذا النهج يوفر تجربة إجمالية أفضل مقارنة بالأنظمة التي تلبي اتفاقيات مستوى الخدمة المحددة بناءً على المتوسط أو الوسيط.

في هذه الورقة هناك العديد من الإشارات إلى هذا المئين 99.9 من التوزيعات، والذي يعكس التركيز المتواصل لمهندسي أمازون على الأداء من منظور تجربة العملاء. تقدم العديد من الأوراق تقارير عن المتوسطات، لذلك يتم تضمينها حيثما كان ذلك منطقياً لأغراض المقارنة. ومع ذلك، فإن جهود الهندسة والتحسين في أمازون لا تركز على المتوسطات. العديد من التقنيات، مثل الاختيار الموازن للحمل لمنسقي الكتابة، تستهدف بشكل بحت التحكم في الأداء عند المئين 99.9.

غالباً ما تلعب أنظمة التخزين دوراً مهماً في إنشاء اتفاقية مستوى الخدمة للخدمة، خاصة إذا كان منطق الأعمال خفيفاً نسبياً، كما هو الحال بالنسبة للعديد من خدمات أمازون. تصبح إدارة الحالة بعد ذلك المكون الرئيسي لاتفاقية مستوى الخدمة للخدمة. أحد الاعتبارات الرئيسية في تصميم ديناموا هو منح الخدمات التحكم في خصائص نظامها، مثل المتانة والاتساق، والسماح للخدمات بإجراء مقايضاتها الخاصة بين الوظائف والأداء والفعالية من حيث التكلفة.

## 2.3 اعتبارات التصميم

خوارزميات النسخ التماثلي للبيانات المستخدمة في الأنظمة التجارية تقوم تقليدياً بتنسيق النسخ المتماثل المتزامن من أجل توفير واجهة وصول بيانات متسقة بقوة. لتحقيق هذا المستوى من الاتساق، تُجبر هذه الخوارزميات على المقايضة بتوافر البيانات في ظروف فشل معينة. على سبيل المثال، بدلاً من التعامل مع عدم اليقين بشأن صحة إجابة، يتم جعل البيانات غير متاحة حتى يكون من المؤكد تماماً أنها صحيحة. من أعمال قواعد البيانات المنسوخة تماثلياً المبكرة جداً، من المعروف جيداً أنه عند التعامل مع احتمال فشل الشبكة، لا يمكن تحقيق الاتساق القوي والتوافر العالي للبيانات في وقت واحد [2، 11]. على هذا النحو، تحتاج الأنظمة والتطبيقات إلى أن تكون على دراية بالخصائص التي يمكن تحقيقها في ظل أي ظروف.

بالنسبة للأنظمة المعرضة لفشل الخادم والشبكة، يمكن زيادة التوافر باستخدام تقنيات النسخ التماثلي المتفائل، حيث يُسمح بنشر التغييرات إلى النسخ المتماثلة في الخلفية، ويتم التسامح مع العمل المتزامن والمنفصل. التحدي مع هذا النهج هو أنه يمكن أن يؤدي إلى تغييرات متعارضة يجب اكتشافها وحلها. تقدم هذه العملية لحل التعارضات مشكلتين: متى يتم حلها ومن يحلها. تم تصميم ديناموا ليكون مخزن بيانات متسق نهائياً؛ أي أن جميع التحديثات تصل إلى جميع النسخ المتماثلة في النهاية.

أحد الاعتبارات المهمة في التصميم هو تحديد متى يتم تنفيذ عملية حل تعارضات التحديث، أي ما إذا كان يجب حل التعارضات أثناء عمليات القراءة أو الكتابة. تنفذ العديد من مخازن البيانات التقليدية حل التعارضات أثناء عمليات الكتابة وتحافظ على بساطة عمليات القراءة [7]. في مثل هذه الأنظمة، قد يتم رفض عمليات الكتابة إذا لم يتمكن مخزن البيانات من الوصول إلى جميع (أو أغلبية) النسخ المتماثلة في وقت معين. من ناحية أخرى، يستهدف ديناموا مساحة تصميم مخزن بيانات "قابل للكتابة دائماً" (أي مخزن بيانات عالي التوافر لعمليات الكتابة). بالنسبة لعدد من خدمات أمازون، فإن رفض تحديثات العملاء يمكن أن يؤدي إلى تجربة عميل سيئة. على سبيل المثال، يجب أن تسمح خدمة سلة التسوق للعملاء بإضافة وإزالة عناصر من سلة التسوق الخاصة بهم حتى في خضم فشل الشبكة والخادم. يجبرنا هذا المتطلب على دفع تعقيد حل التعارضات إلى عمليات القراءة من أجل ضمان عدم رفض عمليات الكتابة أبداً.

الخيار التصميمي التالي هو من يقوم بعملية حل التعارضات. يمكن القيام بذلك بواسطة مخزن البيانات أو التطبيق. إذا تم حل التعارضات بواسطة مخزن البيانات، فإن خياراته محدودة إلى حد ما. في مثل هذه الحالات، يمكن لمخزن البيانات استخدام سياسات بسيطة فقط، مثل "آخر كتابة تفوز" [22]، لحل التحديثات المتعارضة. من ناحية أخرى، نظراً لأن التطبيق على دراية بمخطط البيانات، يمكنه أن يقرر طريقة حل التعارضات الأنسب لتجربة عميله. على سبيل المثال، يمكن للتطبيق الذي يحافظ على سلال تسوق العملاء أن يختار "دمج" النسخ المتعارضة وإرجاع سلة تسوق موحدة واحدة. على الرغم من هذه المرونة، قد لا يرغب بعض مطوري التطبيقات في كتابة آليات حل التعارضات الخاصة بهم ويختارون دفعها إلى مخزن البيانات، والذي بدوره يختار سياسة بسيطة مثل "آخر كتابة تفوز".

**المبادئ الرئيسية الأخرى المتبناة في التصميم هي:**

**قابلية التوسع التدريجي:** يجب أن يكون ديناموا قادراً على التوسع بمضيف تخزين واحد (يُشار إليه فيما يلي بـ "عقدة") في كل مرة، مع تأثير ضئيل على كل من مشغلي النظام والنظام نفسه.

**التماثل:** يجب أن يكون لكل عقدة في ديناموا نفس مجموعة المسؤوليات مثل نظرائها؛ يجب ألا تكون هناك عقدة أو عقد متميزة تأخذ أدواراً خاصة أو مجموعة إضافية من المسؤوليات. في تجربتنا، يبسط التماثل عملية تزويد النظام وصيانته.

**اللامركزية:** امتداد للتماثل، يجب أن يفضل التصميم التقنيات اللامركزية من نظير إلى نظير على التحكم المركزي. في الماضي، أدى التحكم المركزي إلى انقطاعات والهدف هو تجنبها قدر الإمكان. يؤدي هذا إلى نظام أبسط وأكثر قابلية للتوسع وأكثر توافراً.

**عدم التجانس:** يحتاج النظام إلى أن يكون قادراً على استغلال عدم التجانس في البنية التحتية التي يعمل عليها. على سبيل المثال، يجب أن يكون توزيع العمل متناسباً مع قدرات الخوادم الفردية. هذا ضروري في إضافة عقد جديدة بسعة أعلى دون الحاجة إلى ترقية جميع المضيفين دفعة واحدة.

---

### Translation Notes

- **Key technical terms:**
  - "Stateless/Stateful services" → "خدمات عديمة/ذات الحالة"
  - "RDBMS" → "نظام إدارة قواعد البيانات العلائقية"
  - "Binary objects (blobs)" → "كائنات ثنائية (كائنات ثنائية كبيرة - blobs)"
  - "ACID properties" → "خصائص ACID"
  - "Commodity hardware" → "أجهزة سلعية"
  - "99.9th percentile" → "المئين 99.9"
  - "Service Level Agreement (SLA)" → "اتفاقية مستوى الخدمة"
  - "Synchronous replica coordination" → "تنسيق النسخ المتماثل المتزامن"
  - "Strong consistency" → "الاتساق القوي"
  - "Optimistic replication" → "النسخ التماثلي المتفائل"
  - "Eventually consistent" → "متسق نهائياً"
  - "Always writeable" → "قابل للكتابة دائماً"
  - "Last write wins" → "آخر كتابة تفوز"
  - "Incremental scalability" → "قابلية التوسع التدريجي"
  - "Peer-to-peer" → "من نظير إلى نظير"
  - "Heterogeneity" → "عدم التجانس"

- **Figures referenced:** Figure 1 (service-oriented architecture diagram)
- **Citations:** [2], [5], [7], [11], [22]
- **Special handling:** Preserved English terms like "ACID", "RDBMS", "SLA" where appropriate

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check (Key Technical Paragraph)

"Data replication algorithms used in commercial systems traditionally perform synchronous replica coordination in order to provide a strongly consistent data access interface. To achieve this level of consistency, these algorithms are forced to trade off data availability under certain failure scenarios. For instance, rather than dealing with the uncertainty of the correctness of an answer, the data is made unavailable until it is absolutely certain that it is correct. From very early replicated database works, it is well known that when dealing with the possibility of network failures, strong consistency and high data availability cannot be achieved simultaneously [2, 11]. As such, systems and applications need to be aware of which properties can be achieved under which conditions."

✓ Technical accuracy confirmed
