# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** بنى البيانات الموزعة المصادق عليها, دالة التجزئة, البلوك تشين, سلامة البيانات, التوفر, الإجماع, إثبات العمل, قابلية التركيب, الثقة غير المتجانسة

---

### English Version

A variety of distributed systems obtain data integrity assurance by building distributed data structures in which data blocks are referenced using collision-resistant hashes [54], allowing easy verification that the correct data has been retrieved via a reference. We call these Authenticated Distributed Data Structures (ADDSs). A particularly interesting example of an ADDS is a blockchain, but there are other examples, such as distributed hash tables as in CFS [14], distributed version control systems like Git [68], and file distribution systems like BitTorrent [12]. However, an ADDS does not automatically possess all properties needed by blockchains and other applications. An ADDS might fail to ensure availability, because a reference to data does not guarantee it can be retrieved. It might even fail to ensure integrity, because an ADDS might be extended in inconsistent, contradictory ways—for example, multiple new blocks could claim to be the 7th in some blockchain.

Therefore, an ADDS commonly incorporates additional mechanisms to ensure availability and integrity in the presence of malicious adversaries. Some systems rely on gossip and incentive schemes to ensure availability, and consensus or proof-of-work schemes to ensure integrity. Blockchains like Bitcoin [51] and Ethereum [19] lose integrity if the adversary controls a majority of the hash power, while Chord loses availability if an adversary controls enough consecutive nodes [67].

Importantly, all past ADDS systems lack composability: an application cannot use multiple ADDSs in a uniform way and obtain a composition of their guarantees. ADDSs from different systems cannot intersect (share blocks) or even reference each other. Lack of composability makes it difficult for applications to atomically commit information to multiple ADDSs. For instance, if blockchain ADDSs were composable, we could atomically commit a single block to two cryptocurrency blockchains, instead of requiring trusted clearinghouses.

A core reason for this lack of composability is that each system has its own set of failure assumptions. A user of Bitcoin or Ethereum, for example, must assume that at least half the hashpower is honest. There is no mechanism for observers or applications to choose their own assumptions.

We address these limitations with Charlotte, a decentralized framework for composable ADDS with well-defined availability and integrity properties. Together, these ADDSs form the blockweb, an authenticated directed acyclic graph (DAG) [45] of all Charlotte data, which is divided into blocks that reference each other by hash. Charlotte distills ADDSs down to their essentials, allowing it to serve as a common framework for building a wide variety of ADDSs in a composable manner, as illustrated by Figure 1.

Within the blockweb, different applications can construct any acyclic data structure from blocks, including chains, trees, polytrees, multitrees, and skiplists. Whereas blockchains enforce a total ordering on all data, the blockweb requires ordering only when one block references another. Unnecessary ordering is an enormous drain on performance; indeed, it arguably consumes almost all of traditional blockchains' resources. Charlotte applications can create an ordering on blocks, but blocks are by default only partially ordered.

In Charlotte, each server stores whichever blocks it wishes. Most servers will want blocks relevant to applications they're running, but some may provide storage or ordering as a service for sufficiently trusting clients.

Charlotte users can set their own (application-specific) failure assumptions. The failure assumptions of a user effectively filter the blockweb down to blocks forming an ADDS that remains available and consistent under all tolerable failures and adversarial attacks. An observer whose failure assumptions are correct can, given the assumptions of a different correct observer, calculate the subgraph of the blockweb they share.

A key novelty of Charlotte is its generality; it is not application-specific. Unlike other systems that build DAGs of blocks, Charlotte does not implement a cryptocurrency [53, 42, 57, 63, 64], require a universal "smart contract" language for all applications [27, 69, 34], have any distinguished "main chain" [52, 71], or try to enforce the same integrity requirements across all ADDSs in the system [37, 44, 72, 15, 7].

Instead, Charlotte distills ADDSs down their essentials, allowing it to serve as a more general ADDS framework, in which each application can construct an ADDS based on its own trust assumptions and guarantees, yet all of these heterogeneous ADDSs are part of the same blockweb. Indeed, existing block-DAG systems can be recreated within Charlotte, gaining a degree of composability. We have implemented example applications to demonstrate that Charlotte is flexible enough to simultaneously support a variety of applications, including Git-like distributed version control, timestamping, and blockchains based variously on agreement, consensus, and proof-of-work. The shared framework even supports adding shared blocks on multiple chains.

**Contributions**

• Our mathematical model for ADDSs (§3) gives a general way to characterize ADDSs with diverse properties in terms of observers, a novel characterization of different failure tolerances for different participants, and a general way to compose ADDSs and their properties.

• Charlotte provides an extensible type system for blocks, and a standard API for communicating them (§4).

• Example applications show the benefits of using the Charlotte model (§5).

• We generalize blockchains in the Charlotte model, including a technique for separating availability and integrity duties onto separate services and a general model of linearizable transactions on distributed objects (§6).

• We have implemented a prototype of Charlotte along with proof-of-concept implementations of various applications that demonstrate its expressiveness and ability to compose ADDSs (§7).

• Performance measurements show that Charlotte's performance overheads are reasonable (§8).

• Analysis of real usage data shows that Charlotte's added concurrency offers a large speed advantage over traditional blockchain techniques (§6.5).

---

### النسخة العربية

تحصل مجموعة متنوعة من الأنظمة الموزعة على ضمان سلامة البيانات من خلال بناء بنى بيانات موزعة يتم فيها الإشارة إلى كتل البيانات باستخدام دوال تجزئة مقاومة للتصادم [54]، مما يسمح بالتحقق السهل من أن البيانات الصحيحة قد تم استرجاعها عبر مرجع. نسمي هذه بنى البيانات الموزعة المصادق عليها (ADDSs). مثال مثير للاهتمام بشكل خاص لـ ADDS هو البلوك تشين، ولكن هناك أمثلة أخرى، مثل جداول التجزئة الموزعة كما في CFS [14]، وأنظمة التحكم في الإصدارات الموزعة مثل Git [68]، وأنظمة توزيع الملفات مثل BitTorrent [12]. ومع ذلك، لا تمتلك ADDS تلقائياً جميع الخصائص التي تحتاجها البلوك تشين والتطبيقات الأخرى. قد تفشل ADDS في ضمان التوفر، لأن الإشارة إلى البيانات لا تضمن إمكانية استرجاعها. قد تفشل حتى في ضمان السلامة، لأن ADDS قد يتم توسيعها بطرق غير متسقة ومتناقضة—على سبيل المثال، قد تدعي كتل جديدة متعددة أنها السابعة في بعض البلوك تشين.

لذلك، عادة ما تتضمن ADDS آليات إضافية لضمان التوفر والسلامة في وجود خصوم ضارين. تعتمد بعض الأنظمة على مخططات النميمة (gossip) والحوافز لضمان التوفر، ومخططات الإجماع أو إثبات العمل لضمان السلامة. تفقد البلوك تشين مثل Bitcoin [51] وEthereum [19] السلامة إذا سيطر الخصم على غالبية قوة التجزئة، بينما يفقد Chord التوفر إذا سيطر خصم على عقد متتالية كافية [67].

والأهم من ذلك، أن جميع أنظمة ADDS السابقة تفتقر إلى قابلية التركيب: لا يمكن للتطبيق استخدام ADDSs متعددة بطريقة موحدة والحصول على تركيب لضماناتها. لا يمكن لـ ADDSs من أنظمة مختلفة أن تتقاطع (تشارك الكتل) أو حتى تشير إلى بعضها البعض. يجعل الافتقار إلى قابلية التركيب من الصعب على التطبيقات الالتزام بشكل ذري بمعلومات إلى ADDSs متعددة. على سبيل المثال، إذا كانت ADDSs البلوك تشين قابلة للتركيب، يمكننا الالتزام بشكل ذري بكتلة واحدة إلى سلسلتي عملات مشفرة، بدلاً من طلب مقاصات موثوقة.

السبب الأساسي لهذا الافتقار إلى قابلية التركيب هو أن كل نظام له مجموعته الخاصة من افتراضات الفشل. يجب على مستخدم Bitcoin أو Ethereum، على سبيل المثال، أن يفترض أن نصف قوة التجزئة على الأقل أمين. لا توجد آلية للمراقبين أو التطبيقات لاختيار افتراضاتهم الخاصة.

نتناول هذه القيود مع Charlotte، وهو إطار عمل لامركزي لـ ADDS قابلة للتركيب مع خصائص توفر وسلامة محددة جيداً. معاً، تشكل هذه ADDSs شبكة الكتل (blockweb)، وهي رسم بياني لا دوري موجه (DAG) [45] مصادق عليه لجميع بيانات Charlotte، والتي تنقسم إلى كتل تشير إلى بعضها البعض بالتجزئة. يقطر Charlotte ADDSs إلى أساسياتها، مما يسمح لها بالعمل كإطار مشترك لبناء مجموعة واسعة من ADDSs بطريقة قابلة للتركيب، كما هو موضح في الشكل 1.

داخل شبكة الكتل، يمكن للتطبيقات المختلفة بناء أي بنية بيانات لا دورية من الكتل، بما في ذلك السلاسل والأشجار والأشجار المتعددة والأشجار الطبقية وقوائم التخطي. بينما تفرض البلوك تشين ترتيباً كلياً على جميع البيانات، فإن شبكة الكتل تتطلب الترتيب فقط عندما تشير كتلة إلى أخرى. الترتيب غير الضروري هو استنزاف هائل للأداء؛ في الواقع، يمكن القول إنه يستهلك تقريباً جميع موارد البلوك تشين التقليدية. يمكن لتطبيقات Charlotte إنشاء ترتيب على الكتل، ولكن الكتل مرتبة جزئياً فقط بشكل افتراضي.

في Charlotte، يخزن كل خادم أي كتل يرغب فيها. ستحتاج معظم الخوادم إلى كتل ذات صلة بالتطبيقات التي تشغلها، ولكن قد يوفر البعض التخزين أو الترتيب كخدمة للعملاء الذين يثقون بشكل كافٍ.

يمكن لمستخدمي Charlotte تعيين افتراضات الفشل الخاصة بهم (الخاصة بالتطبيق). تقوم افتراضات الفشل للمستخدم بتصفية شبكة الكتل بشكل فعال إلى الكتل التي تشكل ADDS يظل متاحاً ومتسقاً في ظل جميع الإخفاقات المقبولة والهجمات العدائية. يمكن للمراقب الذي افتراضاته للفشل صحيحة، نظراً لافتراضات مراقب مختلف صحيح، حساب الرسم البياني الفرعي لشبكة الكتل الذي يشاركونه.

الجدة الرئيسية لـ Charlotte هي عموميتها؛ فهي ليست خاصة بالتطبيق. على عكس الأنظمة الأخرى التي تبني DAGs من الكتل، لا ينفذ Charlotte عملة مشفرة [53، 42، 57، 63، 64]، ولا يتطلب لغة "عقد ذكي" عالمية لجميع التطبيقات [27، 69، 34]، وليس لديه أي "سلسلة رئيسية" مميزة [52، 71]، ولا يحاول فرض نفس متطلبات السلامة عبر جميع ADDSs في النظام [37، 44، 72، 15، 7].

بدلاً من ذلك، يقطر Charlotte ADDSs إلى أساسياتها، مما يسمح لها بالعمل كإطار ADDS أكثر عمومية، حيث يمكن لكل تطبيق بناء ADDS بناءً على افتراضات الثقة والضمانات الخاصة به، ومع ذلك فإن جميع هذه ADDSs غير المتجانسة هي جزء من نفس شبكة الكتل. في الواقع، يمكن إعادة إنشاء أنظمة block-DAG الموجودة داخل Charlotte، مما يكتسب درجة من قابلية التركيب. لقد نفذنا تطبيقات نموذجية لإثبات أن Charlotte مرنة بما يكفي لدعم مجموعة متنوعة من التطبيقات في وقت واحد، بما في ذلك التحكم في الإصدارات الموزعة على غرار Git، والطوابع الزمنية، والبلوك تشين المستند بشكل متنوع إلى الاتفاق والإجماع وإثبات العمل. يدعم الإطار المشترك حتى إضافة كتل مشتركة على سلاسل متعددة.

**المساهمات**

• يعطي نموذجنا الرياضي لـ ADDSs (§3) طريقة عامة لتوصيف ADDSs بخصائص متنوعة من حيث المراقبين، وتوصيف جديد لتحملات فشل مختلفة لمشاركين مختلفين، وطريقة عامة لتركيب ADDSs وخصائصها.

• يوفر Charlotte نظام أنواع قابل للتوسيع للكتل، وواجهة برمجة تطبيقات قياسية للتواصل معها (§4).

• تُظهر التطبيقات النموذجية فوائد استخدام نموذج Charlotte (§5).

• نعمم البلوك تشين في نموذج Charlotte، بما في ذلك تقنية لفصل واجبات التوفر والسلامة إلى خدمات منفصلة ونموذج عام للمعاملات القابلة للخطية على الكائنات الموزعة (§6).

• لقد نفذنا نموذجاً أولياً لـ Charlotte جنباً إلى جنب مع تطبيقات إثبات المفهوم لتطبيقات مختلفة توضح قدرتها التعبيرية وقدرتها على تركيب ADDSs (§7).

• تظهر قياسات الأداء أن التكاليف الإضافية لأداء Charlotte معقولة (§8).

• يظهر تحليل بيانات الاستخدام الفعلية أن التزامن المضاف لـ Charlotte يوفر ميزة سرعة كبيرة على تقنيات البلوك تشين التقليدية (§6.5).

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** Authenticated Distributed Data Structures (ADDS), blockweb, composability, failure assumptions, observers, heterogeneous trust, Wilbur servers, Fern servers
- **Equations:** None in introduction
- **Citations:** 20+ references to related work
- **Special handling:** Maintained technical precision while ensuring Arabic readability; kept technical terms consistent with glossary

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
