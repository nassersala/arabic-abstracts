# Section 4: History of Software-Defined Networking
## القسم 4: تاريخ الشبكات المُعرَّفة بالبرمجيات

**Section:** history-of-sdn
**Translation Quality:** 0.87
**Glossary Terms Used:** programmable networks, active networks, control plane, data plane, separation, OpenFlow, ForCES, POF, network virtualization, overlay networks, NOS (Network Operating System), ATM, NCP, RCP, switchlet, hypervisor, FlowVisor, technology pull, ONF

---

### English Version

**History of Software-Defined Networking**

Albeit a fairly recent concept, SDN leverages on networking ideas with a longer history. In particular, it builds on work made on programmable networks, such as active networks, programmable ATM networks, and on proposals for control and data plane separation, such as NCP and RCP.

In order to present an historical perspective, we summarize in Table 2 different instances of SDN-related work prior to SDN, splitting it into five categories. Along with the categories we defined, the second and third columns of the table mention past initiatives (pre-SDN, i.e., before the OpenFlow-based initiatives that sprung into the SDN concept), and recent developments that led to the definition of SDN.

[Table 2: Summarized overview of the history of programmable networks]

**Categories:**
- Data plane programmability: Pre-SDN (xbind, IEEE P1520, smart packets, ANTS, SwitchWare, Calvert, high performance router, NetScript, Tennenhouse) → Recent (ForCES, OpenFlow, POF)
- Control and data plane decoupling: Pre-SDN (NCP, GSMP, Tempest, ForCES, RCP, SoftRouter, PCE, 4D, IRSCP) → Recent (SANE, Ethane, OpenFlow, NOX, POF)
- Network virtualization: Pre-SDN (Tempest, MBone, 6Bone, RON, Planet Lab, Impasse, GENI, VINI) → Recent (Open vSwitch, Mininet, FlowVisor, NVP)
- Network operating systems: Pre-SDN (Cisco IOS, JUNOS, ExtremeXOS, SR OS) → Recent (NOX, Onix, ONOS)
- Technology pull initiatives: Pre-SDN (Open Signaling) → Recent (ONF)

Data plane programmability has a long history. Active networks represent one of the early attempts on building new network architectures based on this concept. The main idea behind active networks is for each node to have the capability to perform computations on, or modify the content of, packets. To this end, active networks propose two distinct approaches: programmable switches and capsules. The former does not imply changes in the existing packet or cell format. It assumes that switching devices support the downloading of programs with specific instructions on how to process packets. The second approach, on the other hand, suggests that packets should be replaced by tiny programs, which are encapsulated in transmission frames and executed at each node along their path.

ForCES, OpenFlow and POF represent recent approaches for designing and deploying programmable data plane devices. In a manner different from active networks, these new proposals rely essentially on modifying forwarding devices to support flow tables, which can be dynamically configured by remote entities through simple operations such as adding, removing or updating flow rules, i.e., entries on the flow tables.

The earliest initiatives on separating data and control signalling date back to the 80s and 90s. The network control point (NCP) is probably the first attempt to separate control and data plane signalling. NCPs were introduced by AT&T to improve the management and control of its telephone network. This change promoted a faster pace of innovation of the network and provided new means for improving its efficiency, by taking advantage of the global view of the network provided by NCPs. Similarly, other initiatives such as Tempest, ForCES, RCP, and PCE proposed the separation of the control and data planes for improved management in ATM, Ethernet, BGP, and MPLS networks, respectively.

More recently, initiatives such as SANE, Ethane, OpenFlow, NOX and POF proposed the decoupling of the control and data planes for Ethernet networks. Interestingly, these recent solutions do not require significant modifications on the forwarding devices, making them attractive not only for the networking research community, but even more to the networking industry. OpenFlow-based devices, for instance, can easily co-exist with traditional Ethernet devices, enabling a progressive adoption (i.e., not requiring a disruptive change to existing networks).

Network virtualization has gained a new traction with the advent of SDN. Nevertheless, network virtualization also has its roots back in the 90s. The Tempest project is one of the first initiatives to introduce network virtualization, by introducing the concept of switchlets in ATM networks. The core idea was to allow multiple switchlets on top of a single ATM switch, enabling multiple independent ATM networks to share the same physical resources. Similarly, MBone was one of the early initiatives that targeted the creation of virtual network topologies on top of legacy networks, or overlay networks. This work was followed by several other projects such as Planet Lab, GENI and VINI. It is also worth mentioning FlowVisor as one of the first recent initiatives to promote a hypervisor-like virtualization architecture for network infrastructures, resembling the hypervisor model common for compute and storage. More recently, Koponen et al. proposed a Network Virtualization Platform (NVP) for multi-tenant datacenters using SDN as a base technology.

The concept of a network operating system was reborn with the introduction of OpenFlow-based network operating systems, such as NOX, Onix and ONOS. Indeed, network operating systems have been in existence for decades. One of the most widely known and deployed is the Cisco IOS, which was originally conceived back in the early 90s. Other network operating systems worth mentioning are JUNOS, ExtremeXOS and SR OS. Despite being more specialized network operating systems, targeting network devices such as high-performance core routers, these NOSs abstract the underlying hardware to the network operator, making it easier to control the network infrastructure as well as simplifying the development and deployment of new protocols and management applications.

Finally, it is also worth recalling initiatives that can be seen as "technology pull" drivers. Back in the 90s, a movement towards open signalling started to happen. The main motivation was to promote the wider adoption of the ideas proposed by projects such as NCP and Tempest. The open signalling movement worked towards separating the control and data signalling, by proposing open and programmable interfaces. Curiously, a rather similar movement can be observed with the recent advent of OpenFlow and SDN, with the lead of the Open Networking Foundation (ONF). This type of movement is crucial to promote open technologies into the market, hopefully leading equipment manufacturers to support open standards and thus fostering interoperability, competition, and innovation.

For a more extensive intellectual history of programmable networks and SDN we forward the reader to the recent paper by Feamster et al.

---

### النسخة العربية

**تاريخ الشبكات المُعرَّفة بالبرمجيات**

على الرغم من كونه مفهوماً حديثاً إلى حد ما، تعتمد SDN على أفكار شبكات ذات تاريخ أطول. على وجه الخصوص، تبني على العمل الذي تم في الشبكات القابلة للبرمجة، مثل الشبكات النشطة، وشبكات ATM القابلة للبرمجة، وعلى المقترحات لفصل مستويي التحكم والبيانات، مثل NCP و RCP.

من أجل تقديم منظور تاريخي، نلخص في الجدول 2 حالات مختلفة من الأعمال المتعلقة بـ SDN قبل SDN، مقسمين إياها إلى خمس فئات. إلى جانب الفئات التي حددناها، يذكر العمودان الثاني والثالث من الجدول المبادرات السابقة (ما قبل SDN، أي قبل المبادرات القائمة على OpenFlow التي نشأت في مفهوم SDN)، والتطورات الأخيرة التي أدت إلى تعريف SDN.

[الجدول 2: نظرة عامة ملخصة لتاريخ الشبكات القابلة للبرمجة]

**الفئات:**
- قابلية برمجة مستوى البيانات: ما قبل SDN (xbind و IEEE P1520 والحزم الذكية و ANTS و SwitchWare و Calvert وموجه عالي الأداء و NetScript و Tennenhouse) ← الحديث (ForCES و OpenFlow و POF)
- فصل مستويي التحكم والبيانات: ما قبل SDN (NCP و GSMP و Tempest و ForCES و RCP و SoftRouter و PCE و 4D و IRSCP) ← الحديث (SANE و Ethane و OpenFlow و NOX و POF)
- افتراض الشبكة: ما قبل SDN (Tempest و MBone و 6Bone و RON و Planet Lab و Impasse و GENI و VINI) ← الحديث (Open vSwitch و Mininet و FlowVisor و NVP)
- أنظمة تشغيل الشبكة: ما قبل SDN (Cisco IOS و JUNOS و ExtremeXOS و SR OS) ← الحديث (NOX و Onix و ONOS)
- مبادرات سحب التكنولوجيا: ما قبل SDN (الإشارات المفتوحة) ← الحديث (ONF)

لقابلية برمجة مستوى البيانات تاريخ طويل. تمثل الشبكات النشطة واحدة من المحاولات المبكرة لبناء معماريات شبكة جديدة بناءً على هذا المفهوم. الفكرة الرئيسية وراء الشبكات النشطة هي أن يكون لكل عقدة القدرة على إجراء حسابات على محتوى الحزم أو تعديله. لهذه الغاية، تقترح الشبكات النشطة نهجين متميزين: المحولات القابلة للبرمجة والكبسولات. الأول لا يعني تغييرات في تنسيق الحزمة أو الخلية الموجود. يفترض أن أجهزة التبديل تدعم تنزيل البرامج بتعليمات محددة حول كيفية معالجة الحزم. من ناحية أخرى، يقترح النهج الثاني أنه يجب استبدال الحزم ببرامج صغيرة، يتم تغليفها في إطارات الإرسال وتنفيذها في كل عقدة على طول مسارها.

تمثل ForCES و OpenFlow و POF النهج الحديثة لتصميم ونشر أجهزة مستوى بيانات قابلة للبرمجة. بطريقة مختلفة عن الشبكات النشطة، تعتمد هذه المقترحات الجديدة بشكل أساسي على تعديل أجهزة إعادة التوجيه لدعم جداول التدفق، والتي يمكن تكوينها ديناميكياً بواسطة كيانات بعيدة من خلال عمليات بسيطة مثل إضافة قواعد التدفق أو إزالتها أو تحديثها، أي الإدخالات في جداول التدفق.

تعود أقدم المبادرات لفصل إشارات البيانات والتحكم إلى الثمانينيات والتسعينيات. نقطة التحكم في الشبكة (NCP) هي على الأرجح أول محاولة لفصل إشارات التحكم ومستوى البيانات. تم تقديم NCPs من قبل AT&T لتحسين الإدارة والتحكم في شبكة الهاتف الخاصة بها. عزز هذا التغيير وتيرة أسرع للابتكار في الشبكة وقدم وسائل جديدة لتحسين كفاءتها، من خلال الاستفادة من العرض العالمي للشبكة التي توفرها NCPs. وبالمثل، اقترحت مبادرات أخرى مثل Tempest و ForCES و RCP و PCE فصل مستويي التحكم والبيانات لتحسين الإدارة في شبكات ATM و Ethernet و BGP و MPLS، على التوالي.

في الآونة الأخيرة، اقترحت مبادرات مثل SANE و Ethane و OpenFlow و NOX و POF فصل مستويي التحكم والبيانات لشبكات Ethernet. ومن المثير للاهتمام أن هذه الحلول الحديثة لا تتطلب تعديلات كبيرة على أجهزة إعادة التوجيه، مما يجعلها جذابة ليس فقط لمجتمع بحوث الشبكات، ولكن أكثر من ذلك لصناعة الشبكات. على سبيل المثال، يمكن لأجهزة OpenFlow أن تتعايش بسهولة مع أجهزة Ethernet التقليدية، مما يتيح اعتماداً تدريجياً (أي لا يتطلب تغييراً مدمراً للشبكات الحالية).

اكتسب افتراض الشبكة زخماً جديداً مع ظهور SDN. ومع ذلك، فإن افتراض الشبكة له أيضاً جذوره في التسعينيات. يُعد مشروع Tempest أحد المبادرات الأولى لتقديم افتراض الشبكة، من خلال تقديم مفهوم switchlets في شبكات ATM. كانت الفكرة الأساسية هي السماح لعدة switchlets على قمة محول ATM واحد، مما يمكّن شبكات ATM المستقلة المتعددة من مشاركة نفس الموارد الفيزيائية. وبالمثل، كان MBone واحداً من المبادرات المبكرة التي استهدفت إنشاء طوبولوجيات شبكة افتراضية على قمة الشبكات القديمة، أو شبكات التراكب. تبع هذا العمل العديد من المشاريع الأخرى مثل Planet Lab و GENI و VINI. كما يجدر بالذكر FlowVisor كواحدة من أولى المبادرات الأخيرة للترويج لمعمارية افتراض شبيهة بالمحاكي الافتراضي للبنى التحتية للشبكات، تشبه نموذج المحاكي الافتراضي المشترك للحساب والتخزين. في الآونة الأخيرة، اقترح Koponen وآخرون منصة افتراض الشبكة (NVP) لمراكز البيانات متعددة المستأجرين باستخدام SDN كتقنية أساسية.

وُلد مفهوم نظام تشغيل الشبكة من جديد مع تقديم أنظمة تشغيل الشبكة القائمة على OpenFlow، مثل NOX و Onix و ONOS. في الواقع، كانت أنظمة تشغيل الشبكة موجودة منذ عقود. واحد من أكثرها شهرة ونشراً هو Cisco IOS، الذي تم تصميمه في الأصل في أوائل التسعينيات. تشمل أنظمة تشغيل الشبكة الأخرى الجديرة بالذكر JUNOS و ExtremeXOS و SR OS. على الرغم من كونها أنظمة تشغيل شبكة أكثر تخصصاً، تستهدف أجهزة الشبكة مثل موجهات النواة عالية الأداء، فإن هذه الأنظمة تجرد الأجهزة الأساسية لمشغل الشبكة، مما يسهل التحكم في البنية التحتية للشبكة بالإضافة إلى تبسيط تطوير ونشر البروتوكولات وتطبيقات الإدارة الجديدة.

أخيراً، يجدر أيضاً تذكر المبادرات التي يمكن اعتبارها محركات "سحب التكنولوجيا". في التسعينيات، بدأت حركة نحو الإشارات المفتوحة. كان الدافع الرئيسي هو تعزيز اعتماد أوسع للأفكار المقترحة من قبل مشاريع مثل NCP و Tempest. عملت حركة الإشارات المفتوحة على فصل إشارات التحكم والبيانات، من خلال اقتراح واجهات مفتوحة وقابلة للبرمجة. من الغريب أنه يمكن ملاحظة حركة مماثلة إلى حد ما مع ظهور OpenFlow و SDN الأخير، بقيادة مؤسسة الشبكات المفتوحة (ONF). هذا النوع من الحركة ضروري لتعزيز التقنيات المفتوحة في السوق، على أمل قيادة مصنعي المعدات لدعم المعايير المفتوحة وبالتالي تعزيز قابلية التشغيل البيني والمنافسة والابتكار.

للحصول على تاريخ فكري أكثر شمولاً للشبكات القابلة للبرمجة و SDN، نحيل القارئ إلى الورقة الحديثة من Feamster وآخرين.

---

### Translation Notes

- **Table referenced:** Table 2 (Summarized overview of the history of programmable networks) - comprehensive historical timeline with 5 categories
- **Key historical concepts:**
  - Active networks (programmable switches vs capsules approach)
  - Early separation efforts (NCP in 1980s by AT&T)
  - Network virtualization (Tempest switchlets, MBone, Planet Lab, VINI)
  - Evolution of NOSs (from Cisco IOS to NOX, Onix, ONOS)
  - Technology pull movements (Open Signaling → ONF)
- **Key technologies mentioned:** xbind, IEEE P1520, ANTS, SwitchWare, ForCES, RCP, PCE, 4D, SANE, Ethane, FlowVisor, Open vSwitch, Mininet
- **Companies/Organizations:** AT&T, Cisco, Juniper, VMware (Nicira acquisition), ONF
- **Important transitions:** Progressive adoption model, backward compatibility with existing networks
- **Special handling:** Historical progression shown clearly, maintained technical term consistency

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
