# Section 3: The ETCS Project
## القسم 3: مشروع ETCS

**Section:** case study - ETCS project
**Translation Quality:** 0.88
**Glossary Terms Used:** validation (التحقق من الصحة), formal methods (الأساليب الرسمية), model checking (فحص النماذج), requirements management (إدارة المتطلبات)

---

### English Version

The European Train Control System (ETCS) is a project supported by the European Union aiming at the implementation of a common train control system in all European countries to allow the uninterrupted movement of train across the borders. ETCS is based on the implementation on board of a set of safety critical functions of speed and distance supervision and of information to the driver. Such functions rely on data transmitted by track-side installations through two communication channels: fixed spot transmission devices, called balises, and continuous, bidirectional data transmission through radio according to the GSM standard. ETCS is already installed in important railway lines in different European countries (like Spain, Italy, The Netherlands, Switzerland) and installations are in progress in other countries, such as Sweden, UK, France, Belgium and also non-European railways such as China, India, Turkey, Arabia, South Korea, Algeria and Mexico.

Since 2005, the European Railway Agency (ERA) is responsible of managing the evolution of the ETCS specifications (change control management), ensuring their consistency, and guaranteeing the backwards compatibility of new versions with the old ones.

In 2007, ERA issued a call to tender for the development of a methodology complemented by a set of support tools, for the formalization and validation of the ETCS specifications. The activity poses many hard problems. First, the ETCS documents are written in natural language, and may thus contain a high degree of ambiguity. Second, the ETCS specifications are still in progress, and receive contribution by many people with different culture and background. Third, the ETCS comprises a huge set documents, and comes with severe issues of scalability.

The EuRailCheck project, originated from the successful response to the call to tender by the consortium composed by "Registro Italiano Navale (RINA)", a railway certifying body, "Fondazione Bruno Kessler - irst", a research center, and "Dr. Graband and Partners", a railway consultancy company.

Within the project, we developed a support tool, covering the various phases of the described methodology, based on the integration of algorithmic formal verification techniques within traditional design tools. Moreover, a realistic subset of the specification was formalized and validated applying the developed methodology and tools. The results of the project were then further exploited and validated by domain experts external to the consortium. The evaluation was carried out in form of a workshop, followed by hands-on training courses. These events were attended by experts from manufacturing and railways companies, who provided positive feedback on the applicability in the large of the methodology.

**3.1 Tool support**

The EuRailCheck supporting tool, which has been designed and developed within the project, considered several user and technical requirements such as easy of use, and openness.

The technological basis was identified in two tools provided by IBM: the RequisitePro suite was used as a front end for the management of the ETCS informal requirements; and, the Rational Software Architect (RSA) was used for the management of the formalization of the ETCS requirements into UML class diagrams and temporal constraints. RSA was chosen for its openness in the manipulation of UML specification, and its customizability thanks to the embedded Eclipse platform it is built upon. RSA worked as a gluing platform, and all the modules were developed as plug-ins for RSA.

The main functionalities include RequisitePro custom tagging, annotation of UML diagrams with constraints (syntax checking, completion), support for the instantiation to finite domains, control of the validation procedure. Moreover, we also developed, relying on the API provided by RequisitePro and on the Eclipse platform, the traceability links among the informal requirements classified in RequisitePro and their formal counterpart inside RSA. The verification back-end is based on an extended version of the NuSMV/CEGAR [CCGR00] model checker, able to deal with continuous variables, and to analyze temporally complex expressions in RELTL [EF06, CRST09, CRT09].

---

### النسخة العربية

نظام التحكم في القطارات الأوروبي (ETCS) هو مشروع مدعوم من قبل الاتحاد الأوروبي يهدف إلى تنفيذ نظام تحكم مشترك في القطارات في جميع الدول الأوروبية للسماح بحركة القطارات دون انقطاع عبر الحدود. يعتمد ETCS على تنفيذ مجموعة من الوظائف الحرجة من حيث السلامة على متن القطار لمراقبة السرعة والمسافة وتوفير المعلومات للسائق. تعتمد هذه الوظائف على البيانات المنقولة من التركيبات الجانبية للمسار من خلال قناتي اتصال: أجهزة إرسال نقطي ثابتة تسمى balises، ونقل بيانات ثنائي الاتجاه مستمر عبر الراديو وفقًا لمعيار GSM. تم تثبيت ETCS بالفعل في خطوط سكك حديدية مهمة في دول أوروبية مختلفة (مثل إسبانيا وإيطاليا وهولندا وسويسرا) والتركيبات جارية في دول أخرى، مثل السويد والمملكة المتحدة وفرنسا وبلجيكا وأيضًا سكك حديدية غير أوروبية مثل الصين والهند وتركيا والعربية السعودية وكوريا الجنوبية والجزائر والمكسيك.

منذ عام 2005، أصبحت وكالة السكك الحديدية الأوروبية (ERA) مسؤولة عن إدارة تطور مواصفات ETCS (إدارة التحكم في التغيير)، وضمان اتساقها، وضمان التوافق الرجعي للإصدارات الجديدة مع القديمة.

في عام 2007، أصدرت ERA دعوة لتقديم عطاءات لتطوير منهجية مدعومة بمجموعة من أدوات الدعم، للصياغة الرسمية والتحقق من صحة مواصفات ETCS. يطرح النشاط العديد من المشاكل الصعبة. أولاً، وثائق ETCS مكتوبة بلغة طبيعية، وبالتالي قد تحتوي على درجة عالية من الغموض. ثانيًا، مواصفات ETCS لا تزال قيد التطوير، وتتلقى مساهمات من العديد من الأشخاص ذوي الثقافات والخلفيات المختلفة. ثالثًا، يشتمل ETCS على مجموعة ضخمة من الوثائق، ويأتي مع مشاكل خطيرة في قابلية التوسع.

نشأ مشروع EuRailCheck من الاستجابة الناجحة لدعوة تقديم العطاءات من قبل الاتحاد المكون من "Registro Italiano Navale (RINA)"، وهي هيئة اعتماد السكك الحديدية، و"Fondazione Bruno Kessler - irst"، وهو مركز أبحاث، و"Dr. Graband and Partners"، وهي شركة استشارات للسكك الحديدية.

ضمن المشروع، طورنا أداة دعم، تغطي المراحل المختلفة للمنهجية الموصوفة، بناءً على دمج تقنيات التحقق الرسمي الخوارزمية ضمن أدوات التصميم التقليدية. علاوة على ذلك، تم صياغة والتحقق من صحة مجموعة فرعية واقعية من المواصفات بتطبيق المنهجية والأدوات المطورة. تم بعد ذلك استغلال نتائج المشروع والتحقق من صحتها بشكل أكبر من قبل خبراء المجال خارج الاتحاد. تم إجراء التقييم في شكل ورشة عمل، تليها دورات تدريبية عملية. حضر هذه الفعاليات خبراء من شركات التصنيع والسكك الحديدية، الذين قدموا ردود فعل إيجابية حول قابلية تطبيق المنهجية على نطاق واسع.

**3.1 دعم الأدوات**

أخذت أداة دعم EuRailCheck، التي تم تصميمها وتطويرها ضمن المشروع، في الاعتبار العديد من المتطلبات الفنية والمستخدم مثل سهولة الاستخدام والانفتاح.

تم تحديد الأساس التكنولوجي في أداتين توفرهما IBM: تم استخدام مجموعة RequisitePro كواجهة أمامية لإدارة متطلبات ETCS غير الرسمية؛ وتم استخدام Rational Software Architect (RSA) لإدارة الصياغة الرسمية لمتطلبات ETCS في مخططات فئات UML والقيود الزمنية. تم اختيار RSA لانفتاحها في معالجة مواصفات UML، وقابليتها للتخصيص بفضل منصة Eclipse المضمنة التي بُنيت عليها. عملت RSA كمنصة ربط، وتم تطوير جميع الوحدات كمكونات إضافية لـ RSA.

تشمل الوظائف الرئيسية وضع علامات مخصصة في RequisitePro، وتعليق مخططات UML بالقيود (فحص البنية، الإكمال)، ودعم التنفيذ إلى مجالات محدودة، والتحكم في إجراء التحقق من الصحة. علاوة على ذلك، طورنا أيضًا، بالاعتماد على واجهة برمجة التطبيقات التي توفرها RequisitePro وعلى منصة Eclipse، روابط إمكانية التتبع بين المتطلبات غير الرسمية المصنفة في RequisitePro ونظيراتها الرسمية داخل RSA. يعتمد النهاية الخلفية للتحقق على نسخة موسعة من مدقق النماذج NuSMV/CEGAR [CCGR00]، القادر على التعامل مع المتغيرات المستمرة، وتحليل التعابير المعقدة زمنيًا في RELTL [EF06، CRST09، CRT09].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** European Train Control System/ETCS (نظام التحكم في القطارات الأوروبي), balises (balises - kept as transliteration), GSM standard (معيار GSM), European Railway Agency/ERA (وكالة السكك الحديدية الأوروبية), EuRailCheck project (مشروع EuRailCheck), RequisitePro, Rational Software Architect/RSA, UML class diagrams (مخططات فئات UML), Eclipse platform (منصة Eclipse), NuSMV/CEGAR, RELTL
- **Equations:** 0
- **Citations:** 3 references (CCGR00, EF06, CRST09, CRT09)
- **Special handling:** Technical names of tools (RequisitePro, RSA, Eclipse, NuSMV) kept in English; country names in original form

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
