# Section 2: Distributed System Architecture
## القسم 2: معمارية النظام الموزع

**Section:** Architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** distributed system, architecture, middleware, network, autonomous, communication, protocol, node, scalability, synchronous, asynchronous, topology

---

### English Version

Distributed systems are built up on top of existing networking and operating systems software. A distributed system comprises a collection of autonomous computers, linked through a computer network and distribution middleware. To become autonomous there exist a clear master/slave association between two computers in the network. The middleware enables computers to coordinate their activities and to share the resources of the system, so that users perceive the system as a single, integrated computing facility. Thus, middleware is the bridge that connects distributed applications across dissimilar physical locations, with dissimilar hardware platforms, network technologies, operating systems, and programming languages. The middleware software is being developed following agreed standards and protocols. It provides standard services such as naming, persistence, concurrency control to ensures that accurate results for concurrent processes are produced and obtains the results as fast as possible, event distribution, authorization to specify access rights to resources, security etc. The middleware service extends over multiple machines. Figure 1 shows a simple architecture of a distributed system [GEOR01, ANDR02].

**Figure 1. A Distributed System**
[Diagram showing three machines (A, B, C) with layers: Distributed applications at top, Middleware service in middle, Local OS on each machine, connected via Network at bottom]

The distributed system can be viewed as defined by the physical components or as defined from user or computation point of view. The first is known as the physical view and the second as the logical view. Physically a distributed system consists of a set of nodes (computers) linked together by a communication network. The nodes in the network are loosely coupled and do not share their memory. The nodes in the system communicate by passing messages over the communication network. Communication protocols are used for sending messages from one node to another. The logical model is the view that an application has of the system. It contains a set of concurrent processes and communication channels between them. The core network is treated as fully connected. Processes communicate by sending messages to each other. A system is synchronous if during a proper execution, it all the time performs the intended operation in a known fixed time, otherwise it is asynchronous. In synchronous system the failure can be noticed by a lack of response from the system. Therefore, timeout based techniques are used for failure discovery.

A distributed system can be constructed by means of fully connected networks or partially connected networks [HUAN05, MIN04, NELS01]. A fully connected network (figure 2) is a network in which each of the nodes is connected to each other. The problem with such a system is that adding new nodes to the system results in the increase of number of nodes connected to the node. Due to this the number of file descriptors and complexity for each node to implement the connections are increased heavily. Thus, the scalability (capability of a system to continue to function well when the system is changed in size or volume) of such systems is limited by each node's capacity to open file descriptors and the ability to handle the new connections. The communication cost - the message delay of sending a message from the source to the destination- is low because a message sent from one computer to another one only goes through one link. Fully connected systems are reliable because when a few computers or links fail, the rest of the computers can still communicate with others.

In a partially connected network, direct links exist between some, but not all, pairs of computers. A few of the partially connected network models are star structured networks, multi-access bus networks; ring structured networks, and tree-structured networks (figure 2). Some of the traditional distributed systems such as client/server paradigm use a star as the network topology. The problem with such a system is that when the central node fails, the entire system will be collapsed. In a multi-access bus network, a set of clients are connected via a shared communications line, called a bus. The bus link becomes the bottleneck and if it fails, all the nodes in the system cannot connect to each other. Another disadvantage is that performance degrades as additional computers are added or on heavy traffic. In a ring network each node connects to exactly two other nodes, forming a single continuous pathway for signals through each node. As new nodes are added, the diameter of the system grows as the number of nodes in the system, resulting in a longer message transmission delay. A node failure or cable break might isolate every node attached to the ring. In a tree-structured network (hierarchical network), the nodes are connected as a tree. Each node in the network having a specific fixed number, of nodes associated to it at the next lower level in the hierarchy. The scalability of the tree-structured network is better than that of the fully connected network, since new node can be added as the child node of the leaf nodes or the interior nodes. On the other hand, in such systems, only messages transmitted between a parent node and its child node go though one link, other messages transmitted between two nodes have to go through one or more intermediate nodes.

**Figure 2. Network Models**
[Diagrams showing: Fully Connected Network, Tree Structured Network, Ring Structured Network, Multi-access Bus Network, Star Structured Network]

---

### النسخة العربية

تُبنى الأنظمة الموزعة فوق برمجيات الشبكات وأنظمة التشغيل الموجودة. يتألف النظام الموزع من مجموعة من الحواسيب المستقلة، المرتبطة من خلال شبكة حاسوبية والبرمجيات الوسيطة الموزعة. لكي تصبح مستقلة يوجد ارتباط واضح بين سيد/عبد بين حاسوبين في الشبكة. تمكّن البرمجيات الوسيطة الحواسيب من تنسيق أنشطتها ومشاركة موارد النظام، بحيث يدرك المستخدمون النظام كمرفق حوسبة واحد متكامل. وبالتالي، البرمجيات الوسيطة هي الجسر الذي يربط التطبيقات الموزعة عبر مواقع مادية مختلفة، مع منصات أجهزة مختلفة، وتقنيات شبكات، وأنظمة تشغيل، ولغات برمجة. يتم تطوير برمجيات الوسيطة وفقًا لمعايير وبروتوكولات متفق عليها. توفر خدمات قياسية مثل التسمية، والاستمرارية، والتحكم في التزامن لضمان إنتاج نتائج دقيقة للعمليات المتزامنة والحصول على النتائج بأسرع ما يمكن، وتوزيع الأحداث، والتفويض لتحديد حقوق الوصول إلى الموارد، والأمان وما إلى ذلك. تمتد خدمة البرمجيات الوسيطة عبر أجهزة متعددة. يوضح الشكل 1 معمارية بسيطة لنظام موزع [GEOR01, ANDR02].

**الشكل 1. نظام موزع**
[رسم تخطيطي يوضح ثلاثة أجهزة (A، B، C) مع طبقات: التطبيقات الموزعة في الأعلى، خدمة البرمجيات الوسيطة في الوسط، نظام التشغيل المحلي على كل جهاز، متصلة عبر الشبكة في الأسفل]

يمكن النظر إلى النظام الموزع على أنه محدد بواسطة المكونات المادية أو محدد من وجهة نظر المستخدم أو الحساب. الأول يُعرف بالعرض المادي والثاني بالعرض المنطقي. ماديًا، يتكون النظام الموزع من مجموعة من العقد (الحواسيب) المرتبطة معًا بواسطة شبكة اتصالات. العقد في الشبكة مرتبطة بشكل فضفاض ولا تشارك ذاكرتها. تتواصل العقد في النظام عن طريق تمرير الرسائل عبر شبكة الاتصالات. تُستخدم بروتوكولات الاتصال لإرسال الرسائل من عقدة إلى أخرى. النموذج المنطقي هو العرض الذي يمتلكه التطبيق للنظام. يحتوي على مجموعة من العمليات المتزامنة وقنوات الاتصال بينها. تُعامل الشبكة الأساسية على أنها متصلة بالكامل. تتواصل العمليات عن طريق إرسال رسائل لبعضها البعض. النظام متزامن إذا كان أثناء تنفيذ صحيح، ينفذ طوال الوقت العملية المقصودة في وقت ثابت معروف، وإلا فهو لامتزامن. في النظام المتزامن يمكن ملاحظة الفشل من خلال عدم وجود استجابة من النظام. لذلك، تُستخدم تقنيات قائمة على المهلة الزمنية لاكتشاف الفشل.

يمكن بناء نظام موزع بوسائل شبكات متصلة بالكامل أو شبكات متصلة جزئيًا [HUAN05, MIN04, NELS01]. الشبكة المتصلة بالكامل (الشكل 2) هي شبكة يتصل فيها كل من العقد بكل منها الآخر. المشكلة مع مثل هذا النظام هي أن إضافة عقد جديدة إلى النظام تؤدي إلى زيادة عدد العقد المتصلة بالعقدة. بسبب هذا يزداد عدد واصفات الملفات والتعقيد لكل عقدة لتنفيذ الاتصالات بشكل كبير. وبالتالي، قابلية التوسع (قدرة النظام على الاستمرار في العمل بشكل جيد عندما يتم تغيير حجم أو كمية النظام) لمثل هذه الأنظمة محدودة بقدرة كل عقدة على فتح واصفات الملفات والقدرة على التعامل مع الاتصالات الجديدة. تكلفة الاتصال - تأخير الرسالة لإرسال رسالة من المصدر إلى الوجهة - منخفضة لأن الرسالة المرسلة من حاسوب إلى آخر تمر فقط عبر رابط واحد. الأنظمة المتصلة بالكامل موثوقة لأنه عندما تفشل بعض الحواسيب أو الروابط، لا يزال بإمكان بقية الحواسيب التواصل مع الآخرين.

في الشبكة المتصلة جزئيًا، توجد روابط مباشرة بين بعض أزواج الحواسيب، ولكن ليس كلها. بعض نماذج الشبكات المتصلة جزئيًا هي الشبكات ذات البنية النجمية، وشبكات الناقل متعدد الوصول؛ والشبكات ذات البنية الحلقية، والشبكات ذات البنية الشجرية (الشكل 2). بعض الأنظمة الموزعة التقليدية مثل نموذج العميل/الخادم تستخدم النجمة كطوبولوجيا الشبكة. المشكلة مع مثل هذا النظام هي أنه عندما تفشل العقدة المركزية، سينهار النظام بأكمله. في شبكة الناقل متعدد الوصول، مجموعة من العملاء متصلة عبر خط اتصالات مشترك، يسمى الناقل. يصبح رابط الناقل عنق الزجاجة وإذا فشل، لا يمكن لجميع العقد في النظام الاتصال ببعضها البعض. عيب آخر هو أن الأداء يتدهور مع إضافة حواسيب إضافية أو على حركة المرور الكثيفة. في الشبكة الحلقية، تتصل كل عقدة بالضبط بعقدتين أخريين، مشكلة مسارًا مستمرًا واحدًا للإشارات عبر كل عقدة. مع إضافة عقد جديدة، ينمو قطر النظام مع عدد العقد في النظام، مما يؤدي إلى تأخير أطول في نقل الرسالة. قد يعزل فشل عقدة أو كسر كابل كل عقدة متصلة بالحلقة. في الشبكة ذات البنية الشجرية (الشبكة الهرمية)، تتصل العقد كشجرة. كل عقدة في الشبكة لها عدد ثابت محدد من العقد المرتبطة بها في المستوى الأدنى التالي في التسلسل الهرمي. قابلية التوسع للشبكة ذات البنية الشجرية أفضل من تلك للشبكة المتصلة بالكامل، حيث يمكن إضافة عقدة جديدة كعقدة فرعية للعقد الورقية أو العقد الداخلية. من ناحية أخرى، في مثل هذه الأنظمة، فقط الرسائل المرسلة بين عقدة أصل وعقدة فرع لها تمر عبر رابط واحد، الرسائل الأخرى المرسلة بين عقدتين يجب أن تمر عبر عقدة أو أكثر وسيطة.

**الشكل 2. نماذج الشبكات**
[رسوم تخطيطية توضح: الشبكة المتصلة بالكامل، الشبكة ذات البنية الشجرية، الشبكة ذات البنية الحلقية، شبكة الناقل متعدد الوصول، الشبكة ذات البنية النجمية]

---

### Translation Notes

- **Figures referenced:** Figure 1 (Distributed System Architecture), Figure 2 (Network Models)
- **Key terms introduced:** middleware, physical view, logical view, synchronous/asynchronous systems, network topologies, scalability
- **Equations:** None
- **Citations:** [GEOR01, ANDR02], [HUAN05, MIN04, NELS01]
- **Special handling:** Multiple network topology diagrams referenced

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
