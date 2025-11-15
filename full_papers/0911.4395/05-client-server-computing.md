# Section 5: Client/Server Computing
## القسم 5: حوسبة العميل/الخادم

**Section:** Client/Server Computing
**Translation Quality:** 0.86
**Glossary Terms Used:** client, server, distributed system, network, middleware, database, security, authentication, proxy

---

### English Version

As networks of computing resources have become widespread, the notion of distributing interrelated processing amongst several resources has become popular. Over the years, numerous methods have evolved to facilitate this distribution. One of the popular distributed models is client/server computing [SILV98]. The client/server model is an extension of the modular programming model. Modular programming breaks down the design of a program into individual modules that can be programmed and tested independently. A modular program consists of a main module and one or more auxiliary modules. Like modular programming model, a client/server model consists of clients and servers. The clients and servers normally run on different computers interconnected by a computer network. The calling component becomes the client and the called component the server.

**[Figure 4 showing Client/Server communication with Server at top connected to multiple Clients at bottom via Request/Response arrows]**

A client application sends messages to a server via the network to request the server for performing a specific task. The client handles local resources such as input-output devices, local disks, and other peripherals. The server program listens for client requests that are transmitted via the network. Servers receive those requests and perform actions. Most of the data is processed on the server and only the results are returned to the client. This reduces the amount of network traffic between the server and the client machine. Thus network performance is improved further. The server controls the allocation of the information and also optimizes the resource consumption.

An important design consideration for large client/server systems is whether a client talks directly to the server, or whether an intermediary process is introduced between the client and the server. The former is a two-tier architecture (figure 4); the latter is a three-tier architecture. N-tier architecture is usually used for web applications to forward the requests further to other enterprise services. The two-tier architecture is easier to implement and is typically used in small environments. However, two-tier architecture is less scalable than a three-tier architecture.

In the three-tier architecture (figure 5), an intermediate process connects the clients and servers [CHAN05, JI96]. The intermediary can accumulate frequently used server data to guarantee enhanced performance and scalability. In database based 3-tier client/server architecture, normally there are three essential components: a client computer, an application server and a database server. The application server is the middle tier server which runs the business application. The data is retrieved from database server and it is forwarded to the client by the middle tier server. Middleware is a key to developing three-tier client/server application. Database-oriented middleware offers an Application Program Interface (API) access to a database. Java Database Connectivity (JDBC) is a well-known API, these classes can be inured to aid an applet or a servlet access any number of databases without considerate the inhabitant features of the database.

**[Figure 5: 3-tier Client/server structure showing Client - Query/response - Server - Search - Data]**

For security purposes servers must also address the problem of authentication. In a networked environment, an unauthorized client may attempt to access sensitive data stored on a server. Authentication of clients is provided by cryptographic techniques such as public key encryption or special authentication servers. Sometimes critical servers are replicated in order to achieve high availability and fault tolerance. If one replica fails then the other replicas hosted in different servers still remain available for the clients.

In the 3-tier architecture, it is easier to modify or replace any tier without affecting the other tiers. The separation of application and database functionality achieves better load balancing. Moreover, necessary security guidelines can be put into effect within the server tiers without hampering the clients.

**[Figure 6: Proxy Server Model showing Client - Request/Response - Proxy Server connected to multiple Web Servers]**

A 3-tier client/server model known as 'proxy server model' (figure 6) is commonly used to improve retrieval performance of Internet. The intermediate process – proxy server, distributes client requests to several servers so that requests execute in parallel. A client connects to the proxy server, requesting some service, such as web page available in a web server. The proxy server assesses the request based on its filtering policy. For example, it may filter traffic by IP address or protocol. If the request is authenticated by the filter, the proxy presents the resource by connecting to the appropriate server and demanding the required service for the client. A proxy server may sometimes serve the request without contacting the specified web server. This is made possible by keeping the pages commonly visited by users in the cache of the proxy. By keeping local copies of frequently accessed file, the proxy can serve those files back to a requesting browser without going to the external site each time; this dramatically improves the performance seen by the end user. A proxy server with the ability to cache information is generally called a "proxy-cache server". A proxy is sometimes used to authenticate users by asking them to identify themselves, such as with a username and password. It is also easy to grant access to external resources only to authorised users, and to record each use of external resources in log files. A proxy can also be used in a reverse direction to balance the load amongst a set of identical servers.

**Advantages of client/server model:**
i. All resources are centralised, hence, server can manage resources that are common to all users. For example a central database would be used to evade problems caused by redundant and conflicting data.
ii. Improved security is offered as the number of entry points giving access to data is not so important.
iii. Server level administration is adequate as clients do not play a major role in the client/server model, they require less administration.
iv. A scalable network as it is possible to remove or add clients without affecting the operation of the network and without the need for major modification.

**Disadvantages of the client/server model:**
i. Increased cost due to the technical complexity of the server.
ii. If a server fails, none of its clients will get service, unless the system is designed to be fault-tolerant.
iii. If the network fails, all servers become unreachable.
iv. If one client produces high network traffic, then all clients may suffer from long response times.

---

### النسخة العربية

مع انتشار شبكات موارد الحوسبة، أصبح مفهوم توزيع المعالجة المترابطة بين عدة موارد شائعًا. على مر السنين، تطورت طرق عديدة لتسهيل هذا التوزيع. أحد النماذج الموزعة الشائعة هو حوسبة العميل/الخادم [SILV98]. نموذج العميل/الخادم هو امتداد لنموذج البرمجة النمطية. تقسم البرمجة النمطية تصميم برنامج إلى وحدات فردية يمكن برمجتها واختبارها بشكل مستقل. يتكون البرنامج النمطي من وحدة رئيسية ووحدة أو أكثر مساعدة. مثل نموذج البرمجة النمطية، يتكون نموذج العميل/الخادم من عملاء وخوادم. عادة ما يعمل العملاء والخوادم على حواسيب مختلفة متصلة ببعضها البعض بواسطة شبكة حاسوبية. يصبح المكون المُستدعي هو العميل والمكون المُستدعى هو الخادم.

**[الشكل 4 يوضح اتصال العميل/الخادم مع الخادم في الأعلى متصل بعملاء متعددين في الأسفل عبر أسهم الطلب/الاستجابة]**

يرسل تطبيق العميل رسائل إلى خادم عبر الشبكة لطلب الخادم لأداء مهمة محددة. يتعامل العميل مع الموارد المحلية مثل أجهزة الإدخال والإخراج، والأقراص المحلية، والأجهزة الطرفية الأخرى. يستمع برنامج الخادم لطلبات العميل التي يتم إرسالها عبر الشبكة. تتلقى الخوادم تلك الطلبات وتنفذ الإجراءات. تتم معالجة معظم البيانات على الخادم ويتم إرجاع النتائج فقط إلى العميل. هذا يقلل من كمية حركة مرور الشبكة بين الخادم وجهاز العميل. وبالتالي يتم تحسين أداء الشبكة أكثر. يتحكم الخادم في تخصيص المعلومات ويُحسّن أيضًا استهلاك الموارد.

اعتبار تصميم مهم لأنظمة العميل/الخادم الكبيرة هو ما إذا كان العميل يتحدث مباشرة إلى الخادم، أو ما إذا كان يتم إدخال عملية وسيطة بين العميل والخادم. الأول هو معمارية ثنائية الطبقات (الشكل 4)؛ والأخير هو معمارية ثلاثية الطبقات. عادة ما تُستخدم معمارية N-tier لتطبيقات الويب لإعادة توجيه الطلبات إلى خدمات المؤسسة الأخرى. معمارية الطبقتين أسهل في التنفيذ وتُستخدم عادة في البيئات الصغيرة. ومع ذلك، معمارية الطبقتين أقل قابلية للتوسع من معمارية الطبقات الثلاث.

في معمارية الطبقات الثلاث (الشكل 5)، تربط عملية وسيطة العملاء والخوادم [CHAN05, JI96]. يمكن للوسيط تجميع بيانات الخادم المستخدمة بشكل متكرر لضمان أداء وقابلية توسع محسّنة. في معمارية العميل/الخادم ثلاثية الطبقات القائمة على قاعدة البيانات، عادة ما تكون هناك ثلاثة مكونات أساسية: حاسوب عميل، وخادم تطبيق وخادم قاعدة بيانات. خادم التطبيق هو خادم الطبقة الوسطى الذي يشغل تطبيق الأعمال. يتم استرجاع البيانات من خادم قاعدة البيانات ويتم إعادة توجيهها إلى العميل بواسطة خادم الطبقة الوسطى. البرمجيات الوسيطة هي مفتاح تطوير تطبيق عميل/خادم ثلاثي الطبقات. توفر البرمجيات الوسيطة الموجهة لقاعدة البيانات واجهة برمجة تطبيقات (API) للوصول إلى قاعدة بيانات. اتصال قاعدة بيانات Java (JDBC) هو واجهة برمجة تطبيقات معروفة، يمكن استخدام هذه الفئات لمساعدة تطبيق صغير أو servlet على الوصول إلى أي عدد من قواعد البيانات دون مراعاة الميزات المقيمة لقاعدة البيانات.

**[الشكل 5: بنية العميل/الخادم ثلاثية الطبقات تُظهر العميل - الاستعلام/الاستجابة - الخادم - البحث - البيانات]**

لأغراض أمنية، يجب على الخوادم أيضًا معالجة مشكلة المصادقة. في بيئة متصلة بالشبكة، قد يحاول عميل غير مصرح له الوصول إلى بيانات حساسة مخزنة على خادم. يتم توفير مصادقة العملاء بواسطة تقنيات التشفير مثل تشفير المفتاح العام أو خوادم المصادقة الخاصة. في بعض الأحيان يتم نسخ الخوادم الحرجة لتحقيق توفر عالٍ وتحمل للأخطاء. إذا فشلت نسخة متماثلة واحدة، فإن النسخ المتماثلة الأخرى المستضافة في خوادم مختلفة لا تزال متاحة للعملاء.

في معمارية الطبقات الثلاث، من الأسهل تعديل أو استبدال أي طبقة دون التأثير على الطبقات الأخرى. يحقق الفصل بين وظائف التطبيق وقاعدة البيانات توازنًا أفضل للحمل. علاوة على ذلك، يمكن وضع الإرشادات الأمنية الضرورية قيد التنفيذ ضمن طبقات الخادم دون عرقلة العملاء.

**[الشكل 6: نموذج الخادم الوكيل يُظهر العميل - الطلب/الاستجابة - الخادم الوكيل المتصل بخوادم ويب متعددة]**

نموذج العميل/الخادم ثلاثي الطبقات المعروف باسم "نموذج الخادم الوكيل" (الشكل 6) يُستخدم عادة لتحسين أداء استرجاع الإنترنت. العملية الوسيطة - الخادم الوكيل، توزع طلبات العميل إلى عدة خوادم بحيث تنفذ الطلبات بشكل متوازٍ. يتصل العميل بالخادم الوكيل، طالبًا بعض الخدمة، مثل صفحة ويب متاحة في خادم ويب. يقيّم الخادم الوكيل الطلب بناءً على سياسة التصفية الخاصة به. على سبيل المثال، قد يقوم بتصفية حركة المرور حسب عنوان IP أو البروتوكول. إذا تم مصادقة الطلب بواسطة الفلتر، يعرض الوكيل المورد من خلال الاتصال بالخادم المناسب وطلب الخدمة المطلوبة للعميل. قد يخدم الخادم الوكيل أحيانًا الطلب دون الاتصال بخادم الويب المحدد. يتم ذلك من خلال الاحتفاظ بالصفحات التي يزورها المستخدمون عادة في ذاكرة التخزين المؤقت للوكيل. من خلال الاحتفاظ بنسخ محلية من الملفات التي يتم الوصول إليها بشكل متكرر، يمكن للوكيل تقديم تلك الملفات مرة أخرى إلى متصفح طالب دون الذهاب إلى الموقع الخارجي في كل مرة؛ وهذا يحسّن بشكل كبير الأداء الذي يراه المستخدم النهائي. يُسمى الخادم الوكيل الذي لديه القدرة على تخزين المعلومات مؤقتًا عمومًا "خادم وكيل-ذاكرة تخزين مؤقت". يُستخدم الوكيل أحيانًا لمصادقة المستخدمين من خلال مطالبتهم بتعريف أنفسهم، مثل اسم المستخدم وكلمة المرور. من السهل أيضًا منح الوصول إلى الموارد الخارجية فقط للمستخدمين المصرح لهم، وتسجيل كل استخدام للموارد الخارجية في ملفات السجل. يمكن أيضًا استخدام الوكيل في الاتجاه العكسي لتوازن الحمل بين مجموعة من الخوادم المتطابقة.

**مزايا نموذج العميل/الخادم:**
1. جميع الموارد مركزية، ومن ثم، يمكن للخادم إدارة الموارد المشتركة لجميع المستخدمين. على سبيل المثال، سيتم استخدام قاعدة بيانات مركزية لتجنب المشاكل الناجمة عن البيانات المكررة والمتضاربة.
2. يتم تقديم أمان محسّن حيث أن عدد نقاط الدخول التي توفر الوصول إلى البيانات ليس مهمًا جدًا.
3. الإدارة على مستوى الخادم كافية حيث لا يلعب العملاء دورًا رئيسيًا في نموذج العميل/الخادم، يتطلبون إدارة أقل.
4. شبكة قابلة للتوسع حيث يمكن إزالة أو إضافة العملاء دون التأثير على تشغيل الشبكة ودون الحاجة إلى تعديل كبير.

**عيوب نموذج العميل/الخادم:**
1. زيادة التكلفة بسبب التعقيد التقني للخادم.
2. إذا فشل خادم، لن يحصل أي من عملائه على الخدمة، ما لم يتم تصميم النظام ليكون متحملاً للأخطاء.
3. إذا فشلت الشبكة، تصبح جميع الخوادم غير قابلة للوصول.
4. إذا أنتج عميل واحد حركة مرور عالية على الشبكة، فقد يعاني جميع العملاء من أوقات استجابة طويلة.

---

### Translation Notes

- **Figures referenced:** Figure 4 (Client/Server communication), Figure 5 (3-tier), Figure 6 (Proxy Server)
- **Key terms introduced:** client/server model, two-tier/three-tier architecture, proxy server, middleware, JDBC
- **Equations:** None
- **Citations:** [SILV98], [CHAN05, JI96]
- **Special handling:** Architecture diagrams and advantages/disadvantages lists

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
