# Section 3: What is Software-Defined Networking?
## القسم 3: ما هي الشبكات المُعرَّفة بالبرمجيات؟

**Section:** what-is-sdn
**Translation Quality:** 0.86
**Glossary Terms Used:** Software-Defined Networking (SDN), OpenFlow, forwarding state, data plane, control plane, decoupled, flow-based, flow table, controller, Network Operating System (NOS), programmable, abstraction, southbound interface, northbound interface, management plane, API, network virtualization, NFV

---

### English Version

The term SDN (Software-Defined Networking) was originally coined to represent the ideas and work around OpenFlow at Stanford University. As originally defined, SDN refers to a network architecture where the forwarding state in the data plane is managed by a remote control plane decoupled from the former. The networking industry has on many occasions shifted from this original view of SDN, by referring to anything that involves software as being SDN. We therefore attempt, in this section, to provide a much less ambiguous definition of software-defined networking.

We define an SDN as a network architecture with four pillars:

1. The control and data planes are *decoupled*. Control functionality is removed from network devices that will become simple (packet) forwarding elements.

2. Forwarding decisions are flow-based, instead of destination-based. A flow is broadly defined by a set of packet field values acting as a match (filter) criterion and a set of actions (instructions). In the SDN/OpenFlow context, a flow is a sequence of packets between a source and a destination. All packets of a flow receive identical service policies at the forwarding devices. The flow abstraction allows unifying the behavior of different types of network devices, including routers, switches, firewalls, and middleboxes. Flow programming enables unprecedented flexibility, limited only to the capabilities of the implemented flow tables.

3. Control logic is moved to an external entity, the so-called SDN controller or Network Operating System (NOS). The NOS is a software platform that runs on commodity server technology and provides the essential resources and abstractions to facilitate the programming of forwarding devices based on a logically centralized, abstract network view. Its purpose is therefore similar to that of a traditional operating system.

4. The network is *programmable* through software applications running on top of the NOS that interacts with the underlying data plane devices. This is a fundamental characteristic of SDN, considered as its main value proposition.

Note that the logical centralization of the control logic, in particular, offers several additional benefits. First, it is simpler and less error-prone to modify network policies through high-level languages and software components, compared with low-level device specific configurations. Second, a control program can automatically react to spurious changes of the network state and thus maintain the high-level policies intact. Third, the centralization of the control logic in a controller with global knowledge of the network state simplifies the development of more sophisticated networking functions, services and applications.

Following the SDN concept introduced earlier, an SDN can be defined by three fundamental abstractions: (i) forwarding, (ii) distribution, and (iii) specification. In fact, abstractions are essential tools of research in computer science and information technology, being already an ubiquitous feature of many computer architectures and systems.

Ideally, the *forwarding abstraction* should allow any forwarding behavior desired by the network application (the control program) while hiding details of the underlying hardware. OpenFlow is one realization of such abstraction, which can be seen as the equivalent to a "device driver" in an operating system.

The *distribution abstraction* should shield SDN applications from the vagaries of distributed state, making the distributed control problem a logically centralized one. Its realization requires a common distribution layer, which in SDN resides in the NOS. This layer has two essential functions. First, it is responsible for installing the control commands on the forwarding devices. Second, it collects status information about the forwarding layer (network devices and links), to offer a global network view to network applications.

The last abstraction is *specification*, which should allow a network application to express the desired network behavior without being responsible for implementing that behavior itself. This can be achieved through virtualization solutions, as well as network programming languages. These approaches map the abstract configurations that the applications express based on a simplified, abstract model of the network, into a physical configuration for the global network view exposed by the SDN controller. Figure 3 depicts the SDN architecture, concepts and building blocks.

As previously mentioned, the strong coupling between control and data planes has made it difficult to add new functionality to traditional networks, a fact illustrated in Figure 4. The coupling of the control and data planes (and its physical embedding in the network elements) makes the development and deployment of new networking features (e.g., routing algorithms) very hard since it would imply a modification of the control plane of all network devices -- through the installation of new firmware and, in some cases, hardware upgrades. Hence, the new networking features are commonly introduced via expensive, specialized and hard-to-configure equipment (aka middleboxes) such as load balancers, intrusion detection systems (IDS), and firewalls, among others. These middleboxes need to be placed strategically in the network, making it even harder to later change the network topology, configuration, and functionality.

In contrast, SDN decouples the control plane from the network devices and becomes an external entity: the network operating system or SDN controller. This approach has several advantages:

- It becomes easier to program these applications since the abstractions provided by the control platform and/or the network programming languages can be shared.
- All applications can take advantage of the same network information (the global network view), leading (arguably) to more consistent and effective policy decisions while re-using control plane software modules.
- These applications can take actions (i.e., reconfigure forwarding devices) from any part of the network. There is therefore no need to devise a precise strategy about the location of the new functionality.
- The integration of different applications becomes more straightforward. For instance, load balancing and routing applications can be combined sequentially, with load balancing decisions having precedence over routing policies.

**Terminology**

To identify the different elements of an SDN as unequivocally as possible, we now present the essential terminology used throughout this work.

*Forwarding Devices (FD)*: Hardware- or software-based data plane devices that perform a set of elementary operations. The forwarding devices have well-defined instruction sets (e.g., flow rules) used to take actions on the incoming packets (e.g., forward to specific ports, drop, forward to the controller, rewrite some header). These instructions are defined by southbound interfaces (e.g., OpenFlow, ForCES, Protocol-Oblivious Forwarding (POF)) and are installed in the forwarding devices by the SDN controllers implementing the southbound protocols.

*Data Plane (DP)*: Forwarding devices are interconnected through wireless radio channels or wired cables. The network infrastructure comprises the interconnected forwarding devices, which represent the data plane.

*Southbound Interface (SI)*: The instruction set of the forwarding devices is defined by the southbound API, which is part of the southbound interface. Furthermore, the SI also defines the communication protocol between forwarding devices and control plane elements. This protocol formalizes the way the control and data plane elements interact.

*Control Plane (CP)*: Forwarding devices are programmed by control plane elements through well-defined SI embodiments. The control plane can therefore be seen as the "network brain". All control logic rests in the applications and controllers, which form the control plane.

*Northbound Interface (NI)*: The network operating system can offer an API to application developers. This API represents a northbound interface, i.e., a common interface for developing applications. Typically, a northbound interface abstracts the low level instruction sets used by southbound interfaces to program forwarding devices.

*Management Plane (MP)*: The management plane is the set of applications that leverage the functions offered by the NI to implement network control and operation logic. This includes applications such as routing, firewalls, load balancers, monitoring, and so forth. Essentially, a management application defines the policies, which are ultimately translated to southbound-specific instructions that program the behavior of the forwarding devices.

**Alternative and Broadening Definitions**

Since its inception in 2010, the original OpenFlow-centered SDN term has seen its scope broadened beyond architectures with a cleanly decoupled control plane interface. The definition of SDN will likely continue to broaden, driven by the industry business-oriented views on SDN -- irrespective of the decoupling of the control plane. In this survey, we focus on the original, "canonical" SDN definition based on the aforementioned key pillars and the concept of layered abstractions. However, for the sake of completeness and clarity, we acknowledge alternative SDN definitions, including:

*Control Plane / Broker SDN*: A networking approach that retains existing distributed control planes but offers new APIs that allow applications to interact (bidirectionally) with the network. An SDN controller --often called orchestration platform-- acts as a broker between the applications and the network elements. This approach effectively presents control plane data to the application and allows a certain degree of network programmability by means of "plug-ins" between the orchestrator function and network protocols. This API-driven approach corresponds to a hybrid model of SDN, since it enables the broker to manipulate and directly interact with the control planes of devices such as routers and switches. Examples of this view on SDN include recent standardization efforts at IETF and the design philosophy behind the OpenDaylight project that goes beyond the OpenFlow split control mode.

*Overlay SDN*: A networking approach where the (software- or hardware-based) network edge is dynamically programmed to manage tunnels between hypervisors and/or network switches, introducing an overlay network. In this hybrid networking approach, the distributed control plane providing the underlay remains untouched. The centralized control plane provides a logical overlay that utilizes the underlay as a transport network. This flavor of SDN follows a proactive model to install the overlay tunnels. The overlay tunnels usually terminate inside virtual switches within hypervisors or in physical devices acting as gateways to the existing network. This approach is very popular in recent data center network virtualization, and are based on a variety of tunneling technologies (e.g., STT, VXLAN, NVGRE, LISP, GENEVE).

Recently, other attempts to define SDN in a layered approach have appeared. From a practical perspective and trying to keep backward compatibility with existing network management approaches, one initiative at IRTF SDNRG proposes a management plane at the same level of the control plane, i.e., it classifies solutions in two categories: control logic (with control plane southbound interfaces) and management logic (with management plane southbound interfaces). In other words, the management plane can be seen as a control platform that accommodates traditional network management services and protocols, such as SNMP, BGP, PCEP, and NETCONF.

In addition the broadening definitions above, the term SDN is often used to define extensible network management planes (e.g., OpenStack), whitebox / bare-metal switches with open operating systems (e.g., Cumulus Linux), open-source dataplanes (e.g., Pica8 Xorplus, Quagga), specialized programmable hardware devices (e.g., NetFPGA), virtualized software-based appliances (e.g., Open Platform for Network Functions Virtualization - OPNFV), in spite of lacking a decoupled control and data plane or common interface along its API.

**Standardization Activities**

The standardization landscape in SDN (and SDN-related issues) is already wide and is expected to keep evolving over time. While some of the activities are being carried out in Standard Development Organizations (SDOs), other related efforts are ongoing at industrial or community consortia (e.g., OpenDaylight, OpenStack, OPNFV), delivering results often considered candidates for *de facto* standards. These results often come in the form of open source implementations that have become the common strategy towards accelerating SDN and related cloud and networking technologies. The reason for this fragmentation is due to SDN concepts spanning different areas of IT and networking, both from a network segmentation point of view (from access to core) and from a technology perspective (from optical to wireless).

Table 1 presents a summary of the main SDOs and organizations contributing to the standardization of SDN, as well as the main outcomes produced to date.

The Open Networking Foundation (ONF) was conceived as a member-driven organization to promote the adoption of SDN through the development of the OpenFlow protocol as an open standard to communicate control decisions to data plane devices. The ONF is structured in several working groups (WGs). Some WGs are focused on either defining extensions to the OpenFlow protocol in general, such as the Extensibility WG, or tailored to specific technological areas. Examples of the latter include the Optical Transport (OT) WG, the Wireless and Mobile (W&M) WG, and the Northbound Interfaces (NBI) WG. Other WGs center their activity in providing new protocol capabilities to enhance the protocol itself, such as the Architecture WG or the Forwarding Abstractions (FA) WG.

Similar to how network programmability ideas have been considered by several Working Groups (WGs) of the Internet Engineering Task Force (IETF) in the past, the present SDN trend is also influencing a number of activities. A related body that focuses on research aspects for the evolution of the Internet, the Internet Research Task Force (IRTF), has created the Software Defined Networking Research Group (SDNRG). This group investigates SDN from various perspectives with the goal of identifying the approaches that can be defined, deployed and used in the near term, as well as identifying future research challenges.

In the International Telecommunications Union's Telecommunication sector (ITU-T), some Study Groups (SGs) have already started to develop recommendations for SDN, and a Joint Coordination Activity on SDN (JCA-SDN) has been established to coordinate the SDN standardization work.

The Broadband Forum (BBF) is working on SDN topics through the Service Innovation & Market Requirements (SIMR) WG. The objective of the BBF is to release recommendations for supporting SDN in multi-service broadband networks, including hybrid environments where only some of the network equipment is SDN-enabled.

The Metro Ethernet Forum (MEF) is approaching SDN with the aim of defining service orchestration with APIs for existing networks.

At the Institute of Electrical and Electronics Engineers (IEEE), the 802 LAN/MAN Standards Committee has recently started some activities to standardize SDN capabilities on access networks based on IEEE 802 infrastructure through the P802.1CF project, for both wired and wireless technologies to embrace new control interfaces.

The Optical Internetworking Forum (OIF) Carrier WG released a set of requirements for Transport Software-Defined Networking. The initial activities have as main goal to describe the features and functionalities needed to support the deployment of SDN capabilities in carrier transport networks.

The Open Data Center Alliance (ODCA) is an organization working on unifying data center in the migration to cloud computing environments through interoperable solutions. Through the documentation of usage models, specifically one for SDN, the ODCA is defining new requirements for cloud deployment.

The Alliance for Telecommunication Industry Solutions (ATIS) created a Focus Group for analyzing operational issues and opportunities associated with the programmable capabilities of network infrastructure.

At the European Telecommunication Standards Institute (ETSI), efforts are being devoted to Network Function Virtualization (NFV) through a newly defined Industry Specification Group (ISG). NFV and SDN concepts are considered complementary, sharing the goal of accelerating innovation inside the network by allowing programmability, and altogether changing the network operational model through automation and a real shift to software-based platforms.

Finally, the mobile networking industry 3GPP consortium is studying the management of virtualized networks, an effort aligned with the ETSI NFV architecture and, as such, likely to leverage from SDN.

[Table 1: OpenFlow standardization activities - includes detailed breakdown of SDO activities, working groups, focus areas, and outcomes for ONF, IETF, IRTF, ITU-T, BBF, MEF, IEEE, OIF, ODCA, ETSI, and ATIS]

---

### النسخة العربية

صِيغَ مصطلح SDN (الشبكات المُعرَّفة بالبرمجيات) في الأصل لتمثيل الأفكار والعمل حول OpenFlow في جامعة ستانفورد. كما هو محدد في الأصل، تشير SDN إلى معمارية شبكة حيث تتم إدارة حالة إعادة التوجيه في مستوى البيانات بواسطة مستوى تحكم بعيد منفصل عن الأول. لقد انحرفت صناعة الشبكات في مناسبات عديدة عن هذه الرؤية الأصلية لـ SDN، من خلال الإشارة إلى أي شيء يتضمن البرمجيات على أنه SDN. لذلك نحاول، في هذا القسم، تقديم تعريف أقل غموضاً بكثير للشبكات المُعرَّفة بالبرمجيات.

نُعرِّف SDN كمعمارية شبكة بأربعة أركان:

1. مستويا التحكم والبيانات *منفصلان*. تتم إزالة وظائف التحكم من أجهزة الشبكة التي ستصبح عناصر إعادة توجيه (حزم) بسيطة.

2. قرارات إعادة التوجيه تعتمد على التدفق، بدلاً من أن تكون على أساس الوجهة. يتم تعريف التدفق بشكل واسع من خلال مجموعة من قيم حقول الحزمة التي تعمل كمعيار مطابقة (تصفية) ومجموعة من الإجراءات (التعليمات). في سياق SDN/OpenFlow، التدفق هو تسلسل من الحزم بين مصدر ووجهة. تتلقى جميع حزم التدفق سياسات خدمة متطابقة في أجهزة إعادة التوجيه. يسمح تجريد التدفق بتوحيد سلوك أنواع مختلفة من أجهزة الشبكة، بما في ذلك الموجهات والمحولات وجدران الحماية والصناديق الوسيطة. تتيح برمجة التدفق مرونة غير مسبوقة، محدودة فقط بقدرات جداول التدفق المنفذة.

3. يتم نقل منطق التحكم إلى كيان خارجي، يُسمى متحكم SDN أو نظام تشغيل الشبكة (NOS). NOS هو منصة برمجيات تعمل على تقنية خادم تجارية وتوفر الموارد والتجريدات الأساسية لتسهيل برمجة أجهزة إعادة التوجيه بناءً على عرض شبكة مجرد ومركزي منطقياً. غرضه بالتالي مشابه لغرض نظام تشغيل تقليدي.

4. الشبكة *قابلة للبرمجة* من خلال تطبيقات البرمجيات التي تعمل على قمة NOS والتي تتفاعل مع أجهزة مستوى البيانات الأساسية. هذه خاصية أساسية لـ SDN، تُعتبر عرض قيمتها الرئيسي.

لاحظ أن المركزية المنطقية لمنطق التحكم، على وجه الخصوص، توفر عدة فوائد إضافية. أولاً، من الأبسط والأقل عرضة للخطأ تعديل سياسات الشبكة من خلال لغات عالية المستوى ومكونات برمجية، مقارنة بالتكوينات الخاصة بالأجهزة منخفضة المستوى. ثانياً، يمكن لبرنامج التحكم أن يتفاعل تلقائياً مع التغييرات الزائفة في حالة الشبكة وبالتالي الحفاظ على السياسات عالية المستوى سليمة. ثالثاً، تبسط مركزية منطق التحكم في متحكم بمعرفة عالمية لحالة الشبكة تطوير وظائف وخدمات وتطبيقات شبكات أكثر تطوراً.

بعد مفهوم SDN المُقدَّم سابقاً، يمكن تعريف SDN بثلاثة تجريدات أساسية: (i) إعادة التوجيه، (ii) التوزيع، و (iii) المواصفات. في الواقع، التجريدات هي أدوات أساسية للبحث في علوم الحاسوب وتكنولوجيا المعلومات، كونها بالفعل ميزة موجودة في كل مكان للعديد من معماريات وأنظمة الحاسوب.

بشكل مثالي، يجب أن يسمح *تجريد إعادة التوجيه* بأي سلوك إعادة توجيه يرغب فيه تطبيق الشبكة (برنامج التحكم) بينما يخفي تفاصيل الأجهزة الأساسية. OpenFlow هو أحد تحقيقات هذا التجريد، والذي يمكن اعتباره معادلاً لـ "برنامج تشغيل الجهاز" في نظام التشغيل.

يجب أن يحمي *تجريد التوزيع* تطبيقات SDN من تقلبات الحالة الموزعة، مما يجعل مشكلة التحكم الموزعة مشكلة مركزية منطقياً. يتطلب تحقيقها طبقة توزيع مشتركة، والتي تقع في SDN في NOS. لهذه الطبقة وظيفتان أساسيتان. أولاً، هي مسؤولة عن تثبيت أوامر التحكم على أجهزة إعادة التوجيه. ثانياً، تجمع معلومات الحالة حول طبقة إعادة التوجيه (أجهزة الشبكة والروابط)، لتقديم عرض شبكة عالمي لتطبيقات الشبكة.

التجريد الأخير هو *المواصفات*، والذي يجب أن يسمح لتطبيق الشبكة بالتعبير عن سلوك الشبكة المرغوب دون أن يكون مسؤولاً عن تنفيذ هذا السلوك نفسه. يمكن تحقيق ذلك من خلال حلول الافتراض، وكذلك لغات برمجة الشبكة. تقوم هذه النهج بتعيين التكوينات المجردة التي تعبر عنها التطبيقات بناءً على نموذج مبسط ومجرد للشبكة، إلى تكوين فيزيائي لعرض الشبكة العالمي المكشوف بواسطة متحكم SDN. يصور الشكل 3 معمارية SDN والمفاهيم والكتل البنائية.

كما ذُكر سابقاً، جعل الاقتران القوي بين مستويي التحكم والبيانات من الصعب إضافة وظائف جديدة إلى الشبكات التقليدية، وهي حقيقة موضحة في الشكل 4. يجعل اقتران مستويي التحكم والبيانات (وتضمينه الفيزيائي في عناصر الشبكة) تطوير ونشر ميزات الشبكات الجديدة (على سبيل المثال، خوارزميات التوجيه) صعباً للغاية حيث سيعني ذلك تعديل مستوى التحكم لجميع أجهزة الشبكة -- من خلال تثبيت برامج ثابتة جديدة وفي بعض الحالات، ترقيات الأجهزة. ولذلك، يتم تقديم ميزات الشبكات الجديدة عادة عبر معدات باهظة الثمن ومتخصصة وصعبة التكوين (تُعرف بالصناديق الوسيطة) مثل موازنات الحمل وأنظمة كشف التطفل (IDS) وجدران الحماية، من بين أمور أخرى. يجب وضع هذه الصناديق الوسيطة استراتيجياً في الشبكة، مما يجعل من الصعب أيضاً تغيير طوبولوجيا الشبكة وتكوينها ووظيفتها لاحقاً.

في المقابل، تفصل SDN مستوى التحكم عن أجهزة الشبكة ويصبح كياناً خارجياً: نظام تشغيل الشبكة أو متحكم SDN. لهذا النهج عدة مزايا:

- يصبح من الأسهل برمجة هذه التطبيقات نظراً لأن التجريدات التي توفرها منصة التحكم و/أو لغات برمجة الشبكة يمكن مشاركتها.
- يمكن لجميع التطبيقات الاستفادة من نفس معلومات الشبكة (عرض الشبكة العالمي)، مما يؤدي (على ما يُزعم) إلى قرارات سياسات أكثر اتساقاً وفعالية أثناء إعادة استخدام وحدات برمجيات مستوى التحكم.
- يمكن لهذه التطبيقات اتخاذ إجراءات (أي إعادة تكوين أجهزة إعادة التوجيه) من أي جزء من الشبكة. لذلك لا حاجة لوضع استراتيجية دقيقة حول موقع الوظيفة الجديدة.
- يصبح دمج التطبيقات المختلفة أكثر مباشرة. على سبيل المثال، يمكن دمج تطبيقات موازنة الحمل والتوجيه بشكل تسلسلي، مع أن تكون لقرارات موازنة الحمل الأسبقية على سياسات التوجيه.

**المصطلحات**

لتحديد العناصر المختلفة لـ SDN بشكل لا لبس فيه قدر الإمكان، نقدم الآن المصطلحات الأساسية المستخدمة في جميع أنحاء هذا العمل.

*أجهزة إعادة التوجيه (FD)*: أجهزة مستوى بيانات قائمة على الأجهزة أو البرمجيات تؤدي مجموعة من العمليات الأولية. تحتوي أجهزة إعادة التوجيه على مجموعات تعليمات محددة جيداً (على سبيل المثال، قواعد التدفق) تُستخدم لاتخاذ إجراءات على الحزم الواردة (على سبيل المثال، إعادة التوجيه إلى منافذ محددة، الإسقاط، إعادة التوجيه إلى المتحكم، إعادة كتابة بعض الرؤوس). يتم تعريف هذه التعليمات بواسطة الواجهات الجنوبية (على سبيل المثال، OpenFlow و ForCES و Protocol-Oblivious Forwarding (POF)) ويتم تثبيتها في أجهزة إعادة التوجيه بواسطة متحكمات SDN التي تنفذ البروتوكولات الجنوبية.

*مستوى البيانات (DP)*: يتم ربط أجهزة إعادة التوجيه من خلال قنوات راديو لاسلكية أو كابلات سلكية. تتكون البنية التحتية للشبكة من أجهزة إعادة التوجيه المترابطة، والتي تمثل مستوى البيانات.

*الواجهة الجنوبية (SI)*: يتم تعريف مجموعة تعليمات أجهزة إعادة التوجيه بواسطة واجهة برمجة التطبيقات الجنوبية، والتي هي جزء من الواجهة الجنوبية. علاوة على ذلك، تحدد SI أيضاً بروتوكول الاتصال بين أجهزة إعادة التوجيه وعناصر مستوى التحكم. يضفي هذا البروتوكول الطابع الرسمي على طريقة تفاعل عناصر التحكم ومستوى البيانات.

*مستوى التحكم (CP)*: تتم برمجة أجهزة إعادة التوجيه بواسطة عناصر مستوى التحكم من خلال تجسيدات SI محددة جيداً. يمكن بالتالي اعتبار مستوى التحكم "دماغ الشبكة". يكمن كل منطق التحكم في التطبيقات والمتحكمات، التي تشكل مستوى التحكم.

*الواجهة الشمالية (NI)*: يمكن لنظام تشغيل الشبكة أن يقدم واجهة برمجة تطبيقات لمطوري التطبيقات. تمثل واجهة برمجة التطبيقات هذه واجهة شمالية، أي واجهة مشتركة لتطوير التطبيقات. عادةً، تجرد الواجهة الشمالية مجموعات التعليمات منخفضة المستوى المستخدمة من قبل الواجهات الجنوبية لبرمجة أجهزة إعادة التوجيه.

*مستوى الإدارة (MP)*: مستوى الإدارة هو مجموعة التطبيقات التي تستفيد من الوظائف التي تقدمها NI لتنفيذ منطق التحكم وتشغيل الشبكة. يتضمن ذلك تطبيقات مثل التوجيه وجدران الحماية وموازنات الحمل والمراقبة، وما إلى ذلك. في الأساس، يحدد تطبيق الإدارة السياسات، والتي تُترجم في النهاية إلى تعليمات خاصة بالجانب الجنوبي تبرمج سلوك أجهزة إعادة التوجيه.

**تعريفات بديلة وموسعة**

منذ نشأته في عام 2010، شهد مصطلح SDN الأصلي المتمحور حول OpenFlow توسيع نطاقه إلى ما هو أبعد من المعماريات ذات واجهة مستوى تحكم منفصلة بشكل نظيف. من المحتمل أن يستمر تعريف SDN في التوسع، مدفوعاً بوجهات نظر الصناعة الموجهة نحو الأعمال على SDN -- بغض النظر عن فصل مستوى التحكم. في هذه الدراسة، نركز على التعريف الأصلي "الكنسي" لـ SDN بناءً على الأركان الرئيسية المذكورة أعلاه ومفهوم التجريدات الطبقية. ومع ذلك، من أجل الاكتمال والوضوح، نعترف بتعريفات SDN البديلة، بما في ذلك:

*مستوى التحكم / وسيط SDN*: نهج شبكات يحتفظ بمستويات تحكم موزعة موجودة لكنه يقدم واجهات برمجة تطبيقات جديدة تسمح للتطبيقات بالتفاعل (ثنائي الاتجاه) مع الشبكة. يعمل متحكم SDN -- غالباً ما يُسمى منصة التنسيق -- كوسيط بين التطبيقات وعناصر الشبكة. يقدم هذا النهج بشكل فعال بيانات مستوى التحكم إلى التطبيق ويسمح بدرجة معينة من قابلية برمجة الشبكة عن طريق "المكونات الإضافية" بين وظيفة المنسق وبروتوكولات الشبكة. يتوافق هذا النهج المدفوع بواجهة برمجة التطبيقات مع نموذج هجين من SDN، حيث يمكّن الوسيط من التعامل والتفاعل المباشر مع مستويات تحكم الأجهزة مثل الموجهات والمحولات. تتضمن أمثلة هذه الرؤية على SDN جهود التوحيد القياسي الأخيرة في IETF وفلسفة التصميم وراء مشروع OpenDaylight الذي يتجاوز وضع التحكم المنقسم OpenFlow.

*تراكب SDN*: نهج شبكات حيث تتم برمجة حافة الشبكة (القائمة على البرمجيات أو الأجهزة) ديناميكياً لإدارة الأنفاق بين المحاكيات الافتراضية و/أو محولات الشبكة، مما يقدم شبكة تراكب. في نهج الشبكات الهجين هذا، يظل مستوى التحكم الموزع الذي يوفر الطبقة الأساسية دون تغيير. يوفر مستوى التحكم المركزي تراكباً منطقياً يستخدم الطبقة الأساسية كشبكة نقل. يتبع هذا النوع من SDN نموذجاً استباقياً لتثبيت أنفاق التراكب. تنتهي أنفاق التراكب عادة داخل المحولات الافتراضية داخل المحاكيات الافتراضية أو في الأجهزة الفيزيائية التي تعمل كبوابات للشبكة الحالية. هذا النهج شائع جداً في افتراض شبكة مركز البيانات الحديثة، ويستند إلى مجموعة متنوعة من تقنيات الأنفاق (على سبيل المثال، STT و VXLAN و NVGRE و LISP و GENEVE).

مؤخراً، ظهرت محاولات أخرى لتعريف SDN في نهج طبقي. من منظور عملي ومحاولة الحفاظ على التوافق العكسي مع مناهج إدارة الشبكة الحالية، تقترح إحدى المبادرات في IRTF SDNRG مستوى إدارة على نفس مستوى مستوى التحكم، أي أنها تصنف الحلول في فئتين: منطق التحكم (مع واجهات جنوبية لمستوى التحكم) ومنطق الإدارة (مع واجهات جنوبية لمستوى الإدارة). بعبارة أخرى، يمكن اعتبار مستوى الإدارة منصة تحكم تستوعب خدمات وبروتوكولات إدارة الشبكة التقليدية، مثل SNMP و BGP و PCEP و NETCONF.

بالإضافة إلى التعريفات الموسعة أعلاه، غالباً ما يُستخدم مصطلح SDN لتعريف مستويات إدارة الشبكة القابلة للتوسع (على سبيل المثال، OpenStack)، محولات الصندوق الأبيض / المعدن العاري مع أنظمة تشغيل مفتوحة (على سبيل المثال، Cumulus Linux)، مستويات بيانات مفتوحة المصدر (على سبيل المثال، Pica8 Xorplus و Quagga)، أجهزة قابلة للبرمجة متخصصة (على سبيل المثال، NetFPGA)، أجهزة افتراضية قائمة على البرمجيات (على سبيل المثال، منصة مفتوحة لافتراض وظائف الشبكة - OPNFV)، على الرغم من الافتقار إلى مستوى تحكم وبيانات منفصل أو واجهة مشتركة على طول واجهة برمجة التطبيقات الخاصة بها.

**أنشطة التوحيد القياسي**

المشهد القياسي في SDN (والقضايا المتعلقة بـ SDN) واسع بالفعل ومن المتوقع أن يستمر في التطور مع مرور الوقت. بينما يتم تنفيذ بعض الأنشطة في منظمات تطوير المعايير (SDOs)، فإن الجهود الأخرى ذات الصلة جارية في الاتحادات الصناعية أو المجتمعية (على سبيل المثال، OpenDaylight و OpenStack و OPNFV)، وتقديم نتائج غالباً ما تُعتبر مرشحة لمعايير *فعلية*. غالباً ما تأتي هذه النتائج في شكل تطبيقات مفتوحة المصدر أصبحت الاستراتيجية المشتركة نحو تسريع SDN والتقنيات السحابية والشبكات ذات الصلة. السبب في هذا التجزؤ يرجع إلى مفاهيم SDN التي تمتد إلى مجالات مختلفة من تكنولوجيا المعلومات والشبكات، سواء من وجهة نظر تقسيم الشبكة (من الوصول إلى النواة) ومن منظور تكنولوجي (من الضوئي إلى اللاسلكي).

يعرض الجدول 1 ملخصاً لمنظمات SDOs والمنظمات الرئيسية التي تساهم في توحيد SDN، بالإضافة إلى النتائج الرئيسية المنتجة حتى الآن.

تم تصميم مؤسسة الشبكات المفتوحة (ONF) كمنظمة يقودها الأعضاء لتعزيز اعتماد SDN من خلال تطوير بروتوكول OpenFlow كمعيار مفتوح لإيصال قرارات التحكم إلى أجهزة مستوى البيانات. يتم تنظيم ONF في عدة مجموعات عمل (WGs). بعض WGs مركزة على إما تحديد امتدادات لبروتوكول OpenFlow بشكل عام، مثل WG للتوسيع، أو مصممة خصيصاً لمجالات تكنولوجية محددة. تتضمن أمثلة الأخيرة WG للنقل الضوئي (OT)، و WG اللاسلكية والمحمولة (W&M)، و WG للواجهات الشمالية (NBI). مجموعات عمل أخرى تركز نشاطها على توفير قدرات بروتوكول جديدة لتعزيز البروتوكول نفسه، مثل WG للمعمارية أو WG لتجريدات إعادة التوجيه (FA).

على غرار كيفية اعتبار أفكار قابلية برمجة الشبكة من قبل عدة مجموعات عمل (WGs) في فرقة عمل هندسة الإنترنت (IETF) في الماضي، فإن اتجاه SDN الحالي يؤثر أيضاً على عدد من الأنشطة. أنشأ جسم ذو صلة يركز على جوانب البحث لتطور الإنترنت، فرقة عمل بحوث الإنترنت (IRTF)، مجموعة بحوث الشبكات المُعرَّفة بالبرمجيات (SDNRG). تحقق هذه المجموعة في SDN من وجهات نظر مختلفة بهدف تحديد النهج التي يمكن تعريفها ونشرها واستخدامها على المدى القريب، بالإضافة إلى تحديد تحديات البحث المستقبلية.

في قطاع الاتصالات في اتحاد الاتصالات الدولي (ITU-T)، بدأت بعض مجموعات الدراسة (SGs) بالفعل في تطوير توصيات لـ SDN، وتم إنشاء نشاط تنسيق مشترك على SDN (JCA-SDN) لتنسيق أعمال توحيد SDN القياسية.

يعمل منتدى النطاق العريض (BBF) على موضوعات SDN من خلال مجموعة عمل ابتكار الخدمة ومتطلبات السوق (SIMR). هدف BBF هو إصدار توصيات لدعم SDN في شبكات النطاق العريض متعددة الخدمات، بما في ذلك البيئات الهجينة حيث يتم تمكين SDN فقط على بعض معدات الشبكة.

يقترب منتدى مترو إيثرنت (MEF) من SDN بهدف تحديد تنسيق الخدمة مع واجهات برمجة التطبيقات للشبكات الحالية.

في معهد المهندسين الكهربائيين والإلكترونيين (IEEE)، بدأت لجنة معايير 802 LAN/MAN مؤخراً بعض الأنشطة لتوحيد قدرات SDN على شبكات الوصول بناءً على البنية التحتية IEEE 802 من خلال مشروع P802.1CF، لكل من التقنيات السلكية واللاسلكية لاحتضان واجهات تحكم جديدة.

أصدرت مجموعة عمل Carrier في منتدى الربط الضوئي (OIF) مجموعة من المتطلبات للشبكات المُعرَّفة بالبرمجيات للنقل. الأنشطة الأولية لها الهدف الرئيسي المتمثل في وصف الميزات والوظائف اللازمة لدعم نشر قدرات SDN في شبكات النقل الناقل.

يعمل تحالف مركز البيانات المفتوح (ODCA) على توحيد مركز البيانات في الانتقال إلى بيئات الحوسبة السحابية من خلال حلول قابلة للتشغيل البيني. من خلال توثيق نماذج الاستخدام، وتحديداً واحد لـ SDN، يحدد ODCA متطلبات جديدة لنشر السحابة.

أنشأ تحالف حلول صناعة الاتصالات (ATIS) مجموعة تركيز لتحليل القضايا والفرص التشغيلية المرتبطة بقدرات البرمجة للبنية التحتية للشبكة.

في المعهد الأوروبي لمعايير الاتصالات (ETSI)، يتم تكريس الجهود لافتراض وظائف الشبكة (NFV) من خلال مجموعة مواصفات صناعية محددة حديثاً (ISG). تُعتبر مفاهيم NFV و SDN مكملة، وتشترك في هدف تسريع الابتكار داخل الشبكة من خلال السماح بقابلية البرمجة، ومعاً تغيير نموذج تشغيل الشبكة من خلال الأتمتة والتحول الحقيقي إلى المنصات القائمة على البرمجيات.

أخيراً، يدرس اتحاد صناعة الشبكات المحمولة 3GPP إدارة الشبكات الافتراضية، وهو جهد يتوافق مع معمارية ETSI NFV وعلى هذا النحو، من المحتمل أن يستفيد من SDN.

[الجدول 1: أنشطة توحيد OpenFlow القياسية - يتضمن تفصيلاً تفصيلياً لأنشطة SDO ومجموعات العمل ومجالات التركيز والنتائج لـ ONF و IETF و IRTF و ITU-T و BBF و MEF و IEEE و OIF و ODCA و ETSI و ATIS]

---

### Translation Notes

- **Figures referenced:** Figure 3 (SDN architecture and abstractions), Figure 4 (Traditional vs SDN)
- **Key terms introduced:** four pillars of SDN, flow-based forwarding, NOS, three abstractions (forwarding, distribution, specification), southbound/northbound interfaces, terminology (FD, DP, SI, CP, NI, MP), alternative definitions (Control Plane/Broker SDN, Overlay SDN)
- **Organizations:** ONF, IETF, IRTF, ITU-T, BBF, MEF, IEEE, OIF, ODCA, ETSI, ATIS, 3GPP
- **Technologies mentioned:** OpenFlow, ForCES, POF, STT, VXLAN, NVGRE, LISP, GENEVE, SNMP, BGP, PCEP, NETCONF, OpenStack, OpenDaylight, OPNFV, NetFPGA
- **Special handling:** Detailed terminology section, large standardization table (Table 1 referenced but not fully translated in detail due to length)

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
