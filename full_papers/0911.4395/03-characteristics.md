# Section 3: Characteristics of a Distributed System
## القسم 3: خصائص النظام الموزع

**Section:** Characteristics
**Translation Quality:** 0.86
**Glossary Terms Used:** distributed system, fault-tolerant, scalable, transparency, security, performance, openness, replication, caching, distribution, availability, reliability

---

### English Version

A distributed system must possess the following characteristics to deliver utmost performance for the users:

**Fault-Tolerant:** Distributed systems consist of a large number of hardware and software modules that are bound to fail in the long run. Such component failures can escort to service unavailability. Hence, the systems should be able to recover from component failures without performing erroneous actions. The goal of fault tolerance is to avoid failures in the system even in the presence of faults to provide uninterrupted service. A system is said to be fault tolerant if it can mask the presence of faults. The aim of any fault tolerant system is to increase its reliability or availability. The reliability of a system is defined as the probability that the system survives till that time. A reliable system prevents loss of information even in the event of component failures. Availability is the fraction of time for which a system is available for use. Usually fault tolerance is achieved by providing redundancy. Redundancy is defined as those parts of the system that are not needed for its correct functioning. It is of three types – hardware, software and time. Hardware redundancy is achieved by adding extra hardware components to system which take over the role of failed components in case some faults occur in them. Software redundancy includes extra instructions and code included for managing the extra hardware components, and using them correctly for uninterrupted service, in case of some component failure. In time redundancy the same instruction is executed many times. This is used to handle temporary faults in the system [VIKA04].

**Scalable:** A distributed system can operate correctly even as some aspect of the system is scaled to a larger size. Scale has three components: the number of users and other entities that are part of the system, the distance between the farthest nodes in the system, and the number of organizations that exert administrative control over pieces of the system. The three elements of scale affect distributed systems in many ways. Among the affected components are naming, authentication for verifying someone's identity, authorization, communication, the use of remote resources, and the mechanisms by which users observe the system. Three techniques are employed to manage scale: replication, distribution, and caching [CLIF94].

Replication creates multiple copies of resources. Its use in naming, authentication, and file services reduces the load on individual servers and improves the reliability and availability of the services as a whole. The two important issues of replication are the placement of the replicas and the mechanisms by which they are kept consistent. The placement of replicas in a distributed system depends on the purpose for replicating the resource. If a service is being replicated to reduce the network delays when the service is accessed, the replicas are sprinkled across the system. If the majority of users are local, and if the service is being replicated to improve its availability or to spread the load across multiple servers, then replicas may be placed near one another. If a change is made to the object, the change should be noticeable to everyone in the system. For example, the system sends the updates to any replica, and that replica forwards the update to the others as they become available. If inconsistent updates are received by different replicas in different orders, timestamps (the date/time at which the update was generated) are used to differentiate the copies.

Distribution, another mechanism for managing scale in distributed systems, allows the information maintained by a distributed service to be extended across several servers. Distributing data across multiple servers reduces the size of the database that must be maintained by each server, dropping the time needed to search the database. Distribution also spreads the load across the servers reducing the number of requests that are handled by each. If requests can be distributed to servers in proportion to their power, the load on servers can be effectively managed. Network traffic can be reduced if data are assigned to servers close to the location from which they are most frequently used. In tree structured system, if cached copies are available from subordinate servers, the upper levels can be avoided.

Caching is another important technique for building scalable systems. Caching decreases the load on servers and the network. Cached data can be accessed faster than if a new request is made. The difference between replication and caching is that cached data is a short-term data. Instead of propagating updates on cached data, consistency is maintained by nullifying cached data when consistency can not be guaranteed. Caching is usually performed by the client, reducing frequent requests to network services. Caching can also occur on the servers executing those services. Reading a file from the memory cached copy on the file server is faster than reading it from the client's local disk.

**Predictable Performance:** Various performance metrics such as response time (elapsed time between the end of an inquiry or demand on a computer system and the beginning of a response), throughput (the rate at which a network sends or receives data), system utilization, network capacity etc. are employed to assess the performance. Predictable performance is the ability to provide desired responsiveness in a timely manner.

**Openness:** The attribute 'openness' ensures that a subsystem is continually open to interaction with other systems. Web services are software systems designed to support interoperable machine-to-machine interaction over a network. These protocols allow distributed systems to be extended and scaled. An open system that scales has benefit over a completely closed and self-reliant system. A distributed system independent from heterogeneity of the underlying environment such as hardware and software platforms achieves the property of openness. Therefore, every service is equally accessible to every client (local or remote) in the system. The implementation, installation and debugging of new services should not be very complex in a system possessing openness characteristic.

**Security:** Distributed systems should allow communication between programs/users/resources on different computers by enforcing necessary security arrangements. The security features are mainly intended to provide confidentiality, integrity and availability. Confidentiality (privacy) is protection against disclosure to unauthorised person. Violation of confidentiality range from the discomforting to the catastrophic. Integrity provides protection against alteration and corruption. Availability keeps the resource accessible. Many incidents of hacking compromise the integrity of databases and other resources. "Denial of service" attacks are attacks against availability. Other important security concerns are access control and nonrepudiation. Maintaining access control facilitates the users to access only those resources and services to which they are entitled. It also ensures that users are not denied resources that they legitimately can expect to access. Nonrepudiation provides protection against denial by one of the entities involved in a communication. The security mechanisms put into practice should guarantee appropriate use of resources by different users in the system.

**Transparency:** Distributed systems should be perceived by users and application developers as a whole rather than as a collection of cooperating components. The locations of the computer systems involved in the operations, concurrent operations, data replication, resource discovery from multiple sites, failures, system recovery etc. are hidden from users. Transparency hides the distributed nature of the system from its users and shows the user that the system is appearing and performing as a normal centralized system. The transparency can be employed in different ways in a distributed system (Figure 3) [KAZI00, PRAD02].

**Figure 3. Transparency in Distributed Systems**
[Diagram showing hierarchy of transparency types: Access Transparency, Location Transparency at bottom; Migration Transparency, Replication Transparency, Concurrency Transparency in middle; Scalability Transparency, Performance Transparency, Failure Transparency at top]

- **Access transparency** facilitates the users of a distributed system to access local and remote resources using identical operations. (e.g. navigation in the web).

- **Location transparency** describes names used to identify network resources (e.g. IP address) independent of both the user's location and the resource location. In other words, location transparency facilitates a user to access resources from anywhere on the network without knowing where the resource is located. A file could be on the user's own PC, or thousands of miles away on other servers.

- **Concurrency transparency** enables several processes to operate concurrently using shared information objects without interference between them (e.g.: Automatic Teller Machine network). The users will not notice the existence of other users in the system (even if they access the same resources).

- **Replication transparency** enables the system to make additional copies of files and other resources for the purpose of performance and/or reliability, without the users noticing. If a resource is replicated among several locations, it should appear to the user as a single resource (e.g. Mirroring - Mirror sites are usually used to offer multiple sources of the same information as a way of providing reliable access to large downloads).

- **Failure transparency** enables the applications to complete their task despite failures occurring in certain components of the system. For example, if a server fails, but users are automatically redirected to another server and the user never notices the failure, the system is said to show high failure transparency. Failure transparency is one of the most difficult types of transparency to accomplish since it is hard to determine whether a server has actually failed, or whether it is simply responding very slowly. Moreover, it is generally unfeasible to achieve full failure transparency in a distributed system since networks are unreliable.

- **Migration transparency** facilitates the resources to move from one location to another without having their names changed. (e.g.: Web Pages). Users should not be aware of whether a resource or computing entity possesses the ability to move to a different physical or logical location.

- **Performance transparency** ensures the load variation should not lead to performance degradation. This could be achieved by automatic reconfiguration as response to changes of the load. (e.g.: load distribution)

- **Scalability transparency** allows the system to remain efficient even with a significant increase in the number of users and resources connected (e.g. World-Wide-Web, distributed database).

---

### النسخة العربية

يجب أن يمتلك النظام الموزع الخصائص التالية لتقديم أقصى أداء للمستخدمين:

**متحمل للأخطاء:** تتكون الأنظمة الموزعة من عدد كبير من وحدات الأجهزة والبرمجيات التي من المحتم أن تفشل على المدى الطويل. يمكن أن تؤدي مثل هذه إخفاقات المكونات إلى عدم توفر الخدمة. ومن ثم، يجب أن تكون الأنظمة قادرة على التعافي من إخفاقات المكونات دون تنفيذ إجراءات خاطئة. الهدف من تحمل الأخطاء هو تجنب الفشل في النظام حتى في وجود أخطاء لتوفير خدمة غير منقطعة. يُقال أن النظام متحمل للأخطاء إذا كان يمكنه إخفاء وجود الأخطاء. الهدف من أي نظام متحمل للأخطاء هو زيادة موثوقيته أو توفره. تُعرّف موثوقية النظام بأنها احتمال بقاء النظام حتى ذلك الوقت. يمنع النظام الموثوق فقدان المعلومات حتى في حالة فشل المكونات. التوفر هو الجزء من الوقت الذي يكون فيه النظام متاحًا للاستخدام. عادة يتم تحقيق تحمل الأخطاء من خلال توفير التكرار. يُعرَّف التكرار بأنه تلك الأجزاء من النظام التي لا تُحتاج لعمله الصحيح. وهو من ثلاثة أنواع - الأجهزة والبرمجيات والوقت. يتم تحقيق تكرار الأجهزة من خلال إضافة مكونات أجهزة إضافية إلى النظام تتولى دور المكونات الفاشلة في حالة حدوث بعض الأخطاء فيها. يتضمن تكرار البرمجيات تعليمات وشفرة إضافية مضمنة لإدارة مكونات الأجهزة الإضافية، واستخدامها بشكل صحيح للخدمة المتواصلة، في حالة فشل بعض المكونات. في تكرار الوقت يتم تنفيذ نفس التعليمة عدة مرات. يُستخدم هذا للتعامل مع الأخطاء المؤقتة في النظام [VIKA04].

**قابل للتوسع:** يمكن للنظام الموزع أن يعمل بشكل صحيح حتى مع توسيع بعض جوانب النظام إلى حجم أكبر. للتوسع ثلاثة مكونات: عدد المستخدمين والكيانات الأخرى التي هي جزء من النظام، والمسافة بين العقد الأبعد في النظام، وعدد المنظمات التي تمارس التحكم الإداري على أجزاء من النظام. العناصر الثلاثة للتوسع تؤثر على الأنظمة الموزعة بطرق عديدة. من بين المكونات المتأثرة التسمية، والمصادقة للتحقق من هوية شخص ما، والتفويض، والاتصال، واستخدام الموارد البعيدة، والآليات التي يلاحظ بها المستخدمون النظام. يتم توظيف ثلاث تقنيات لإدارة التوسع: التكرار، والتوزيع، والتخزين المؤقت [CLIF94].

يُنشئ التكرار نسخًا متعددة من الموارد. يؤدي استخدامه في التسمية والمصادقة وخدمات الملفات إلى تقليل الحمل على الخوادم الفردية ويحسن موثوقية وتوفر الخدمات ككل. المشكلتان المهمتان للتكرار هما وضع النسخ المتماثلة والآليات التي يتم من خلالها الحفاظ على اتساقها. يعتمد وضع النسخ المتماثلة في نظام موزع على الغرض من نسخ المورد. إذا كان يتم نسخ خدمة لتقليل تأخيرات الشبكة عند الوصول إلى الخدمة، يتم رش النسخ المتماثلة عبر النظام. إذا كانت غالبية المستخدمين محليين، وإذا كان يتم نسخ الخدمة لتحسين توفرها أو لنشر الحمل عبر خوادم متعددة، فقد يتم وضع النسخ المتماثلة بالقرب من بعضها البعض. إذا تم إجراء تغيير على الكائن، يجب أن يكون التغيير ملحوظًا للجميع في النظام. على سبيل المثال، يرسل النظام التحديثات إلى أي نسخة متماثلة، وتلك النسخة المتماثلة تُعيد توجيه التحديث إلى الآخرين عندما تصبح متاحة. إذا تم استلام تحديثات غير متسقة من قبل نسخ متماثلة مختلفة بترتيبات مختلفة، تُستخدم الطوابع الزمنية (التاريخ/الوقت الذي تم فيه إنشاء التحديث) للتمييز بين النسخ.

التوزيع، آلية أخرى لإدارة التوسع في الأنظمة الموزعة، يسمح بتوسيع المعلومات التي تحتفظ بها خدمة موزعة عبر عدة خوادم. يؤدي توزيع البيانات عبر خوادم متعددة إلى تقليل حجم قاعدة البيانات التي يجب أن يحتفظ بها كل خادم، مما يقلل الوقت اللازم للبحث في قاعدة البيانات. كما ينشر التوزيع الحمل عبر الخوادم مما يقلل من عدد الطلبات التي يتم التعامل معها من قبل كل منها. إذا كان بالإمكان توزيع الطلبات على الخوادم بما يتناسب مع قوتها، يمكن إدارة الحمل على الخوادم بفعالية. يمكن تقليل حركة المرور على الشبكة إذا تم تخصيص البيانات للخوادم القريبة من الموقع الذي يتم استخدامها منه بشكل متكرر. في النظام ذي البنية الشجرية، إذا كانت النسخ المخزنة مؤقتًا متاحة من الخوادم التابعة، يمكن تجنب المستويات العليا.

التخزين المؤقت هو تقنية مهمة أخرى لبناء أنظمة قابلة للتوسع. يقلل التخزين المؤقت الحمل على الخوادم والشبكة. يمكن الوصول إلى البيانات المخزنة مؤقتًا بشكل أسرع مما لو تم تقديم طلب جديد. الفرق بين التكرار والتخزين المؤقت هو أن البيانات المخزنة مؤقتًا هي بيانات قصيرة الأجل. بدلاً من نشر التحديثات على البيانات المخزنة مؤقتًا، يتم الحفاظ على الاتساق من خلال إبطال البيانات المخزنة مؤقتًا عندما لا يمكن ضمان الاتساق. عادة ما يتم التخزين المؤقت من قبل العميل، مما يقلل الطلبات المتكررة لخدمات الشبكة. يمكن أن يحدث التخزين المؤقت أيضًا على الخوادم التي تنفذ تلك الخدمات. قراءة ملف من النسخة المخزنة مؤقتًا في الذاكرة على خادم الملفات أسرع من قراءته من القرص المحلي للعميل.

**أداء قابل للتنبؤ:** يتم استخدام مقاييس أداء مختلفة مثل وقت الاستجابة (الوقت المنقضي بين نهاية استعلام أو طلب على نظام حاسوبي وبداية الاستجابة)، والإنتاجية (المعدل الذي ترسل أو تستقبل به الشبكة البيانات)، واستخدام النظام، وسعة الشبكة وما إلى ذلك لتقييم الأداء. الأداء القابل للتنبؤ هو القدرة على توفير الاستجابة المطلوبة في الوقت المناسب.

**الانفتاح:** تضمن خاصية "الانفتاح" أن النظام الفرعي مفتوح باستمرار للتفاعل مع الأنظمة الأخرى. خدمات الويب هي أنظمة برمجية مصممة لدعم التفاعل بين الآلات القابل للتشغيل البيني عبر شبكة. تسمح هذه البروتوكولات بتوسيع الأنظمة الموزعة وتوسيع نطاقها. النظام المفتوح الذي يتوسع له فائدة على نظام مغلق تمامًا ويعتمد على نفسه. يحقق النظام الموزع المستقل عن تباين البيئة الأساسية مثل منصات الأجهزة والبرمجيات خاصية الانفتاح. لذلك، كل خدمة قابلة للوصول على قدم المساواة لكل عميل (محلي أو بعيد) في النظام. يجب ألا يكون تنفيذ وتثبيت وتصحيح أخطاء الخدمات الجديدة معقدًا جدًا في نظام يمتلك خاصية الانفتاح.

**الأمان:** يجب أن تسمح الأنظمة الموزعة بالتواصل بين البرامج/المستخدمين/الموارد على حواسيب مختلفة من خلال فرض ترتيبات أمنية ضرورية. تهدف ميزات الأمان بشكل أساسي إلى توفير السرية والسلامة والتوفر. السرية (الخصوصية) هي الحماية ضد الكشف لشخص غير مصرح له. يتراوح انتهاك السرية من المزعج إلى الكارثي. توفر السلامة الحماية ضد التغيير والفساد. يحافظ التوفر على إمكانية الوصول إلى المورد. العديد من حوادث القرصنة تعرض سلامة قواعد البيانات والموارد الأخرى للخطر. هجمات "رفض الخدمة" هي هجمات ضد التوفر. المخاوف الأمنية المهمة الأخرى هي التحكم في الوصول وعدم الإنكار. يسهل الحفاظ على التحكم في الوصول للمستخدمين الوصول فقط إلى تلك الموارد والخدمات التي يحق لهم الحصول عليها. كما يضمن أن المستخدمين لا يُحرمون من الموارد التي يمكنهم توقع الوصول إليها بشكل مشروع. يوفر عدم الإنكار الحماية ضد الإنكار من قبل أحد الكيانات المشاركة في الاتصال. يجب أن تضمن آليات الأمان الموضوعة في الممارسة الاستخدام المناسب للموارد من قبل مستخدمين مختلفين في النظام.

**الشفافية:** يجب أن يُنظر إلى الأنظمة الموزعة من قبل المستخدمين ومطوري التطبيقات ككل بدلاً من مجموعة من المكونات المتعاونة. مواقع أنظمة الحاسوب المشاركة في العمليات، والعمليات المتزامنة، ونسخ البيانات، واكتشاف الموارد من مواقع متعددة، والفشل، واستعادة النظام وما إلى ذلك مخفية عن المستخدمين. تخفي الشفافية الطبيعة الموزعة للنظام عن مستخدميه وتُظهر للمستخدم أن النظام يظهر ويعمل كنظام مركزي عادي. يمكن توظيف الشفافية بطرق مختلفة في نظام موزع (الشكل 3) [KAZI00, PRAD02].

**الشكل 3. الشفافية في الأنظمة الموزعة**
[رسم تخطيطي يوضح تسلسل هرمي لأنواع الشفافية: شفافية الوصول، شفافية الموقع في الأسفل؛ شفافية الترحيل، شفافية التكرار، شفافية التزامن في الوسط؛ شفافية قابلية التوسع، شفافية الأداء، شفافية الفشل في الأعلى]

- **شفافية الوصول** تسهل لمستخدمي نظام موزع الوصول إلى الموارد المحلية والبعيدة باستخدام عمليات متطابقة. (مثل التنقل في الويب).

- **شفافية الموقع** تصف الأسماء المستخدمة لتحديد موارد الشبكة (مثل عنوان IP) المستقلة عن موقع المستخدم وموقع المورد. بعبارة أخرى، تسهل شفافية الموقع للمستخدم الوصول إلى الموارد من أي مكان على الشبكة دون معرفة موقع المورد. يمكن أن يكون الملف على جهاز الكمبيوتر الخاص بالمستخدم نفسه، أو على بعد آلاف الأميال على خوادم أخرى.

- **شفافية التزامن** تُمكّن عدة عمليات من العمل بشكل متزامن باستخدام كائنات معلومات مشتركة دون تداخل بينها (مثل: شبكة أجهزة الصراف الآلي). لن يلاحظ المستخدمون وجود مستخدمين آخرين في النظام (حتى إذا وصلوا إلى نفس الموارد).

- **شفافية التكرار** تُمكّن النظام من إنشاء نسخ إضافية من الملفات والموارد الأخرى لغرض الأداء و/أو الموثوقية، دون أن يلاحظ المستخدمون. إذا تم نسخ مورد بين عدة مواقع، يجب أن يظهر للمستخدم كمورد واحد (مثل النسخ المتطابق - عادة ما تُستخدم مواقع النسخ المتطابق لتوفير مصادر متعددة لنفس المعلومات كوسيلة لتوفير وصول موثوق للتنزيلات الكبيرة).

- **شفافية الفشل** تُمكّن التطبيقات من إكمال مهمتها على الرغم من حدوث فشل في مكونات معينة من النظام. على سبيل المثال، إذا فشل خادم، لكن تم إعادة توجيه المستخدمين تلقائيًا إلى خادم آخر ولم يلاحظ المستخدم الفشل أبدًا، يُقال أن النظام يُظهر شفافية فشل عالية. شفافية الفشل هي واحدة من أصعب أنواع الشفافية لتحقيقها لأنه من الصعب تحديد ما إذا كان الخادم قد فشل فعلاً، أو ما إذا كان يستجيب ببطء شديد فقط. علاوة على ذلك، من غير الممكن عمومًا تحقيق شفافية فشل كاملة في نظام موزع لأن الشبكات غير موثوقة.

- **شفافية الترحيل** تسهل انتقال الموارد من موقع إلى آخر دون تغيير أسمائها. (مثل: صفحات الويب). يجب ألا يكون المستخدمون على علم بما إذا كان المورد أو كيان الحوسبة يمتلك القدرة على الانتقال إلى موقع مادي أو منطقي مختلف.

- **شفافية الأداء** تضمن أن تباين الحمل لا يجب أن يؤدي إلى تدهور الأداء. يمكن تحقيق ذلك من خلال إعادة التكوين التلقائي كاستجابة للتغيرات في الحمل. (مثل: توزيع الحمل)

- **شفافية قابلية التوسع** تسمح للنظام بالبقاء فعالاً حتى مع زيادة كبيرة في عدد المستخدمين والموارد المتصلة (مثل شبكة الويب العالمية، قاعدة البيانات الموزعة).

---

### Translation Notes

- **Figures referenced:** Figure 3 (Transparency in Distributed Systems)
- **Key terms introduced:** fault tolerance, scalability, transparency types, redundancy, replication, distribution, caching, security (confidentiality, integrity, availability)
- **Equations:** None
- **Citations:** [VIKA04], [CLIF94], [KAZI00, PRAD02]
- **Special handling:** Extensive definitions of system characteristics with examples

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
