# Section 4: The Eight Fallacies of Distributed Computing
## القسم 4: المفاهيم الخاطئة الثمانية للحوسبة الموزعة

**Section:** Eight Fallacies
**Translation Quality:** 0.87
**Glossary Terms Used:** distributed computing, network, latency, bandwidth, security, topology, reliability, administrator

---

### English Version

In 1994, Peter Deutsch of SUN drafted 7 assumptions [ARNO06, INGR04], architects and designers of distributed systems are expected to make, which prove wrong in the end. In 1997 James Gosling - father of the Java programming language, added another such fallacy – the eighth fallacy of distributed computing. The assumptions are now collectively known as the "The 8 fallacies of distributed computing". The fallacies of distributed Computing are a set of common but false assumptions made by programmers when first developing distributed applications. Many distributed systems which were developed based on these assumptions were needlessly complex caused by mistakes that required patching later on.

**The Fallacies of Distributed Computing:**
1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

**Reliability:** The software which has been developed with the assumption that network is reliable; the network will lead to trouble when it starts dropping packets. Reliability can often be improved by increasing the autonomy of the nodes in a system. Replication can also improve the reliability of a system.

**Latency:** Latency is the time between initiating a request for data and the beginning of the actual data transfer. Latency can be comparatively good on a LAN; however it deteriorates quickly the user move to WAN scenarios or internet scenarios. Assuming latency is zero will definitely lead to scalability problems as the application grows geographically, or is moved to a different kind of network.

**Bandwidth:** A measure of the capacity of a communications channel, i.e. how much data we can transfer during that time. The higher a channel's bandwidth, the more information it can carry. However, there are two forces at work to keep this assumption a fallacy. One is that while the bandwidth grows, so does the amount of information we try to squeeze through it. VoIP, videos, and IPTV are some of the newer applications that take up bandwidth. The other force at work to lower bandwidth is packet loss (along with frame size). Bandwidth limitations direct us to strive to limit the size of the information we send over the wire.

**Security:** The network is never secure since the systems are facing various types of threats. Hence, the developer should perform threat modelling to evaluate the security risks. Following this, analyze which risk should be mitigated by what measures (a tradeoff between costs, risks and their probability) and take appropriate measures. Security is typically a multi-layered solution that is handled on the network, infrastructure, and application levels. The software architect should be conscious that security is very essential and the consequences it may have.

**Topology:** Topology deals with the different configurations that can be adopted in building networks, such as a ring, bus, star or fully connected. For example any given node in the LAN will have one or more links to one or more other nodes in the network and the mapping of these links and nodes onto a graph results in a geometrical shape that determines the physical topology of the network. Likewise, the mapping of the flow of data between the nodes in the network determines the logical topology of the network. The physical and logical topologies might be identical in any particular network but they also may be different. When a new application is deployed in an organization, the network structure may also be altered. The operations team is likely to add and remove servers every once in a while and/or make other changes to the network. Finally, there are server and network faults which can cause routing changes. At the client's side the situation is even worse. There are laptops coming and going, wireless adhoc networks, new mobile devices etc. In a nutshell, topology in a distributed system is changing persistently [NELS01].

**Administrator:** The sixth distributed computing fallacy is "there is one administrator". A simple situation is that with different administrators assigned according to expertise - databases, web servers, networks, different operating systems and the like for a company. The problem occurs when the company collaborates with external entities such as a business partner, or if the application is deployed for Internet consumption and hosted by some hosting service and the application consumes external services. In these situations, the other administrators are not even under company administrators control and they may have their own rules for administration. Hence the assumption of 'one administrator' is proven to be a myth.

Most of the time, the administrators are not part of the software development team. Therefore, the developers should provide them with tools to diagnose and find problems. A practical approach is to include tools for monitoring ongoing operations as well; for instance, to allow administrators recognize problems when they are small before they become a system failure. As a distributed system grows, its various components such as users, resources, nodes, networks, etc. will start to cross administrative domains. This means that the number of organizations or individuals that exert administrative control over the system will grow. In a system that scales poorly with regards to administrative growth, this can lead to problems of resource usage, reimbursement, security, etc.

**Transport cost:** Transport cost never becomes zero. The costs for setting and running the network are not free. There are costs for buying the routers, costs for securing the network, costs for leasing the bandwidth for internet connections, and costs for operating and maintaining the network running.

**Homogeneous network:** The eighth distributed computing fallacy is "network is homogeneous." Homogeneous network is a network derived of computers using similar configuration and protocols. Except a few very trivial ones, no network is homogeneous. Proprietary protocols are very harder to integrate. Hence, make use of standard technologies that are widely accepted such as XML (extended markup language) or Web Services as these technologies help alleviate the affects of the heterogeneity of the enterprise environment.

---

### النسخة العربية

في عام 1994، صاغ بيتر دويتش من شركة SUN سبعة افتراضات [ARNO06, INGR04]، من المتوقع أن يقوم معماريو ومصممو الأنظمة الموزعة بها، والتي تثبت خطأها في النهاية. في عام 1997 أضاف جيمس جوسلينج - والد لغة برمجة Java، مفهومًا خاطئًا آخر - المفهوم الخاطئ الثامن للحوسبة الموزعة. الافتراضات معروفة الآن مجتمعة باسم "المفاهيم الخاطئة الثمانية للحوسبة الموزعة". المفاهيم الخاطئة للحوسبة الموزعة هي مجموعة من الافتراضات الشائعة ولكنها خاطئة التي يقوم بها المبرمجون عند تطوير التطبيقات الموزعة لأول مرة. العديد من الأنظمة الموزعة التي تم تطويرها بناءً على هذه الافتراضات كانت معقدة بلا داعٍ بسبب أخطاء تطلبت تصحيحًا لاحقًا.

**المفاهيم الخاطئة للحوسبة الموزعة:**
1. الشبكة موثوقة.
2. الكمون صفر.
3. النطاق الترددي لا نهائي.
4. الشبكة آمنة.
5. الطوبولوجيا لا تتغير.
6. يوجد مسؤول واحد.
7. تكلفة النقل صفر.
8. الشبكة متجانسة.

**الموثوقية:** البرنامج الذي تم تطويره بافتراض أن الشبكة موثوقة؛ ستؤدي الشبكة إلى مشاكل عندما تبدأ في إسقاط الحزم. يمكن في كثير من الأحيان تحسين الموثوقية من خلال زيادة استقلالية العقد في النظام. يمكن أن يحسن التكرار أيضًا موثوقية النظام.

**الكمون:** الكمون هو الوقت بين بدء طلب البيانات وبداية النقل الفعلي للبيانات. يمكن أن يكون الكمون جيدًا نسبيًا على الشبكة المحلية؛ ومع ذلك يتدهور بسرعة عندما ينتقل المستخدم إلى سيناريوهات الشبكة الواسعة أو سيناريوهات الإنترنت. افتراض أن الكمون صفر سيؤدي بالتأكيد إلى مشاكل قابلية التوسع مع نمو التطبيق جغرافيًا، أو نقله إلى نوع مختلف من الشبكة.

**النطاق الترددي:** مقياس لسعة قناة الاتصالات، أي مقدار البيانات التي يمكننا نقلها خلال ذلك الوقت. كلما ارتفع النطاق الترددي للقناة، زادت المعلومات التي يمكنها حملها. ومع ذلك، هناك قوتان تعملان للحفاظ على هذا الافتراض كمفهوم خاطئ. إحداهما أنه بينما ينمو النطاق الترددي، كذلك تنمو كمية المعلومات التي نحاول ضغطها من خلاله. VoIP والفيديو و IPTV هي بعض التطبيقات الأحدث التي تستهلك النطاق الترددي. القوة الأخرى التي تعمل على خفض النطاق الترددي هي فقدان الحزم (جنبًا إلى جنب مع حجم الإطار). تدفعنا قيود النطاق الترددي إلى السعي لتحديد حجم المعلومات التي نرسلها عبر السلك.

**الأمان:** الشبكة ليست آمنة أبدًا لأن الأنظمة تواجه أنواعًا مختلفة من التهديدات. ومن ثم، يجب على المطور إجراء نمذجة التهديدات لتقييم المخاطر الأمنية. بعد ذلك، تحليل المخاطر التي يجب تخفيفها بواسطة أي تدابير (مقايضة بين التكاليف والمخاطر واحتماليتها) واتخاذ التدابير المناسبة. الأمان عادة ما يكون حلاً متعدد الطبقات يتم التعامل معه على مستوى الشبكة والبنية التحتية والتطبيق. يجب أن يكون معماري البرمجيات واعيًا بأن الأمان مهم جدًا والعواقب التي قد تترتب عليه.

**الطوبولوجيا:** تتعامل الطوبولوجيا مع التكوينات المختلفة التي يمكن اعتمادها في بناء الشبكات، مثل الحلقة، أو الناقل، أو النجمة أو المتصلة بالكامل. على سبيل المثال، أي عقدة معينة في الشبكة المحلية سيكون لها رابط واحد أو أكثر إلى عقدة واحدة أو أكثر أخرى في الشبكة وينتج عن تخطيط هذه الروابط والعقد على رسم بياني شكل هندسي يحدد الطوبولوجيا المادية للشبكة. وبالمثل، يحدد تخطيط تدفق البيانات بين العقد في الشبكة الطوبولوجيا المنطقية للشبكة. قد تكون الطوبولوجيا المادية والمنطقية متطابقة في أي شبكة معينة ولكنها قد تكون أيضًا مختلفة. عندما يتم نشر تطبيق جديد في مؤسسة، قد يتم أيضًا تغيير بنية الشبكة. من المحتمل أن يضيف فريق العمليات ويزيل الخوادم كل فترة و/أو يجري تغييرات أخرى على الشبكة. أخيرًا، هناك أخطاء في الخادم والشبكة التي يمكن أن تسبب تغييرات في التوجيه. من جانب العميل الوضع أسوأ. هناك أجهزة الكمبيوتر المحمولة تأتي وتذهب، والشبكات اللاسلكية المخصصة، والأجهزة المحمولة الجديدة وما إلى ذلك. باختصار، تتغير الطوبولوجيا في نظام موزع باستمرار [NELS01].

**المسؤول:** المفهوم الخاطئ السادس للحوسبة الموزعة هو "يوجد مسؤول واحد". حالة بسيطة هي أن مع مسؤولين مختلفين معينين وفقًا للخبرة - قواعد البيانات، وخوادم الويب، والشبكات، وأنظمة التشغيل المختلفة وما شابه ذلك لشركة. تحدث المشكلة عندما تتعاون الشركة مع كيانات خارجية مثل شريك تجاري، أو إذا تم نشر التطبيق للاستهلاك عبر الإنترنت واستضافته بواسطة بعض خدمات الاستضافة ويستهلك التطبيق خدمات خارجية. في هذه الحالات، المسؤولون الآخرون ليسوا حتى تحت سيطرة مسؤولي الشركة وقد يكون لديهم قواعدهم الخاصة للإدارة. ومن ثم ثبت أن افتراض "مسؤول واحد" هو أسطورة.

في معظم الأحيان، لا يكون المسؤولون جزءًا من فريق تطوير البرمجيات. لذلك، يجب على المطورين تزويدهم بأدوات لتشخيص المشاكل وإيجادها. النهج العملي هو تضمين أدوات لمراقبة العمليات الجارية أيضًا؛ على سبيل المثال، للسماح للمسؤولين بالتعرف على المشاكل عندما تكون صغيرة قبل أن تصبح فشلاً في النظام. مع نمو نظام موزع، ستبدأ مكوناته المختلفة مثل المستخدمين والموارد والعقد والشبكات وما إلى ذلك في عبور المجالات الإدارية. وهذا يعني أن عدد المنظمات أو الأفراد الذين يمارسون التحكم الإداري على النظام سينمو. في نظام يتوسع بشكل سيئ فيما يتعلق بالنمو الإداري، يمكن أن يؤدي ذلك إلى مشاكل في استخدام الموارد، والتعويض، والأمان، وما إلى ذلك.

**تكلفة النقل:** لا تصبح تكلفة النقل صفرًا أبدًا. تكاليف إعداد وتشغيل الشبكة ليست مجانية. هناك تكاليف لشراء أجهزة التوجيه، وتكاليف لتأمين الشبكة، وتكاليف لتأجير النطاق الترددي لاتصالات الإنترنت، وتكاليف لتشغيل وصيانة تشغيل الشبكة.

**الشبكة المتجانسة:** المفهوم الخاطئ الثامن للحوسبة الموزعة هو "الشبكة متجانسة". الشبكة المتجانسة هي شبكة مشتقة من حواسيب تستخدم تكوينًا وبروتوكولات مماثلة. باستثناء القليل جدًا التافهة منها، لا توجد شبكة متجانسة. البروتوكولات الاحتكارية يصعب جدًا دمجها. ومن ثم، استخدم التقنيات القياسية المقبولة على نطاق واسع مثل XML (لغة الترميز الموسعة) أو خدمات الويب حيث تساعد هذه التقنيات في تخفيف آثار عدم التجانس في بيئة المؤسسة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** fallacies, latency, bandwidth, topology, homogeneous network
- **Equations:** None
- **Citations:** [ARNO06, INGR04], [NELS01]
- **Special handling:** Important historical concepts from Peter Deutsch and James Gosling

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
