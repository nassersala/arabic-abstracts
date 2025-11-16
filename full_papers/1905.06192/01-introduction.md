# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** cyber-physical systems (الأنظمة السيبرانية الفيزيائية), assurance case (حالة ضمان), formal methods (الأساليب الرسمية), verification (التحقق), model-based design (التصميم المبني على النماذج), theorem prover (مُثبِّت النظريات)

---

### English Version

Cyber-physical systems (CPS) control critical socio-technical processes prone to faults and other critical events with potentially undesired consequences. Such systems include autonomous vehicles, traffic flow control, patient monitoring, surgical robot assistants, and building security automation. Real-time concurrency of physical events and computation poses tough challenges in achieving high levels of assurance in verification and validation. Consequently, the benefits of CPS can only be harnessed if they acquire consumer trust and regulatory acceptance.

Safety cases [20, 23], and more generally assurance cases, are structured arguments, supported by evidence, intended to convince a regulator that a system is acceptably safe for application in a specific operating environment [18]. They are recommended by several international standards, such as ISO26262 for automotive applications. An assurance case consists of a hierarchical decomposition of requirements, through appropriate argumentation strategies, into further claims, and eventually supporting evidence. Several languages exist for expressing assurance cases, including the Goal Structuring Notation [23] (GSN), and the closely related Structured Assurance Case Metamodel (SACM).

Assurance case creation can be supported by model-based design, which utilises architectural and behavioural models over which requirements can be formulated [18]. However, safety cases can suffer from undermining logical fallacies and lack of evidence [17]. A proposed solution is formalisation in a machine-checked logic to enable verification of consistency and well-foundedness [26]. As confirmed by avionics standard DO-178C supplement DO-333, the evidence gathering process can also benefit from the rigour of formal methods. At the same time, we acknowledge that, (1) assurance cases are intended primarily for human consumption, and (2) that formal models must be validated informally [19]. Consequently, assurance cases will usually combine informal and formal content, and any tool must support this.

Our vision is a unified framework for machine-checked assurance cases, and with evidence provided by a number of integrated formal methods [16]. Such a framework can have a transformative effect in the field of assurance by harnessing results from automated formal verification to produce assurance cases undergirded by specific mathematical guarantees of their consistency and adequacy of the evidence. Moreover, it can provide a potential route to regulatory acceptance, through the production of mathematically verified safety certificates.

The contributions of this paper make a first step in this direction: (1) an implementation of SACM in the Isabelle interactive theorem prover [24], (2) a machine-checked domain-specific assurance language, and (3) integration of formal evidence from our verification framework, Isabelle/UTP [14]. Isabelle provides a sophisticated executable document model for presenting a graph of hyperlinked artifacts, like definitions, theorems, and proofs. The document model provides automatic and incremental consistency checking, and change analysis, where updates to model artifacts trigger rechecking. Such capabilities can support efficient maintenance and evolution of model-based assurance cases [20].

Moreover, the document model allows management of both informal and formal content, and access to a vast array of automated verification tools [29]. In particular, our own verification framework, Isabelle/UTP [14,15], harnesses Hoare and He's Unifying Theories of Programming [21] (UTP) to provide verification facilities for a variety of programming and modelling languages with paradigms as diverse as concurrency, real-time, and hybrid computation. We validate our approach by mechanising an assurance case for the Tokeneer system [1], including the underlying formal model and verification of security functional requirements.

In §2 we outline preliminary materials: SACM, Isabelle, and the Isabelle/DOF ontology framework. In §3 we describe the Tokeneer system, and how it is assured and verified. In §4 we begin our contributions by describing the implementation of Isabelle/SACM and our assurance DSL in Isabelle. In §5 we describe how we model and verify Tokeneer using our verification framework, Isabelle/UTP. In §6 we describe the mechanisation of the assurance case for Tokeneer in Isabelle/SACM. In §7 we highlight related work, and in §8 we conclude.

---

### النسخة العربية

تتحكم الأنظمة السيبرانية الفيزيائية (CPS) في العمليات الاجتماعية-التقنية الحرجة المعرضة للأخطاء والأحداث الحرجة الأخرى ذات العواقب غير المرغوب فيها المحتملة. تشمل هذه الأنظمة المركبات ذاتية القيادة، والتحكم في تدفق حركة المرور، ومراقبة المرضى، ومساعدي الروبوتات الجراحية، وأتمتة أمن المباني. يطرح التزامن في الوقت الفعلي للأحداث الفيزيائية والحساب تحديات صعبة في تحقيق مستويات عالية من الضمان في التحقق والمصادقة. وبالتالي، لا يمكن تسخير فوائد الأنظمة السيبرانية الفيزيائية إلا إذا اكتسبت ثقة المستهلك والقبول التنظيمي.

حالات السلامة [20، 23]، وبشكل أعم حالات الضمان، هي حجج منظمة مدعومة بأدلة، تهدف إلى إقناع جهة تنظيمية بأن النظام آمن بشكل مقبول للتطبيق في بيئة تشغيل محددة [18]. يوصى بها من قبل العديد من المعايير الدولية، مثل ISO26262 لتطبيقات السيارات. تتكون حالة الضمان من تحليل هرمي للمتطلبات، من خلال استراتيجيات حجاجية مناسبة، إلى مزيد من الادعاءات، وفي النهاية أدلة داعمة. توجد عدة لغات للتعبير عن حالات الضمان، بما في ذلك تدوين هيكلة الأهداف [23] (GSN)، والنموذج الفوقي لحالة الضمان المهيكلة (SACM) ذي الصلة الوثيقة.

يمكن دعم إنشاء حالات الضمان بواسطة التصميم المبني على النماذج، الذي يستخدم النماذج المعمارية والسلوكية التي يمكن صياغة المتطلبات عليها [18]. ومع ذلك، يمكن أن تعاني حالات السلامة من المغالطات المنطقية المقوضة ونقص الأدلة [17]. الحل المقترح هو الإضفاء الرسمي في منطق يتم التحقق منه آلياً لتمكين التحقق من الاتساق والأساس الجيد [26]. كما أكده معيار الطيران DO-178C الملحق DO-333، يمكن لعملية جمع الأدلة أيضاً الاستفادة من صرامة الأساليب الرسمية. في الوقت نفسه، نقر بأن، (1) حالات الضمان مخصصة في المقام الأول للاستهلاك البشري، و(2) أن النماذج الرسمية يجب التحقق من صحتها بشكل غير رسمي [19]. وبالتالي، ستجمع حالات الضمان عادةً بين المحتوى غير الرسمي والرسمي، ويجب أن تدعم أي أداة ذلك.

رؤيتنا هي إطار موحد لحالات الضمان المتحقق منها آلياً، ومع أدلة مقدمة من عدد من الأساليب الرسمية المتكاملة [16]. يمكن أن يكون لمثل هذا الإطار تأثير تحويلي في مجال الضمان من خلال تسخير نتائج التحقق الرسمي الآلي لإنتاج حالات ضمان مدعومة بضمانات رياضية محددة لاتساقها وكفاية الأدلة. علاوة على ذلك، يمكن أن يوفر مساراً محتملاً للقبول التنظيمي، من خلال إنتاج شهادات سلامة متحقق منها رياضياً.

تقدم مساهمات هذه الورقة خطوة أولى في هذا الاتجاه: (1) تنفيذ SACM في مُثبِّت النظريات التفاعلي Isabelle [24]، (2) لغة ضمان خاصة بالمجال متحقق منها آلياً، و(3) تكامل الأدلة الرسمية من إطار التحقق الخاص بنا، Isabelle/UTP [14]. يوفر Isabelle نموذج مستند قابل للتنفيذ متطور لتقديم رسم بياني من المصنوعات المترابطة بالروابط الفائقة، مثل التعريفات والنظريات والبراهين. يوفر نموذج المستند فحص الاتساق الآلي والتدريجي، وتحليل التغيير، حيث تؤدي التحديثات على مصنوعات النموذج إلى إعادة الفحص. يمكن لمثل هذه القدرات دعم الصيانة الفعالة والتطور لحالات الضمان المبنية على النماذج [20].

علاوة على ذلك، يسمح نموذج المستند بإدارة كل من المحتوى غير الرسمي والرسمي، والوصول إلى مجموعة واسعة من أدوات التحقق الآلية [29]. على وجه الخصوص، يستفيد إطار التحقق الخاص بنا، Isabelle/UTP [14،15]، من النظريات الموحدة للبرمجة لهور وهي (UTP) [21] لتوفير مرافق تحقق لمجموعة متنوعة من لغات البرمجة والنمذجة ذات النماذج المتنوعة مثل التزامن والوقت الفعلي والحساب الهجين. نتحقق من صحة نهجنا من خلال أتمتة حالة ضمان لنظام Tokeneer [1]، بما في ذلك النموذج الرسمي الأساسي والتحقق من المتطلبات الوظيفية للأمان.

في §2 نحدد المواد التمهيدية: SACM و Isabelle وإطار الأنطولوجيا Isabelle/DOF. في §3 نصف نظام Tokeneer، وكيف يتم ضمانه والتحقق منه. في §4 نبدأ مساهماتنا من خلال وصف تنفيذ Isabelle/SACM ولغة الضمان الخاصة بالمجال الخاصة بنا في Isabelle. في §5 نصف كيف نمذجنا والتحقق من Tokeneer باستخدام إطار التحقق الخاص بنا، Isabelle/UTP. في §6 نصف أتمتة حالة الضمان لـ Tokeneer في Isabelle/SACM. في §7 نسلط الضوء على الأعمال ذات الصلة، وفي §8 نختتم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Cyber-physical systems (الأنظمة السيبرانية الفيزيائية)
  - Safety cases (حالات السلامة)
  - Assurance cases (حالات الضمان)
  - Goal Structuring Notation - GSN (تدوين هيكلة الأهداف)
  - SACM (النموذج الفوقي لحالة الضمان المهيكلة)
  - Model-based design (التصميم المبني على النماذج)
  - Isabelle/DOF
  - Isabelle/UTP
  - Tokeneer
  - UTP - Unifying Theories of Programming (النظريات الموحدة للبرمجة)
- **Equations:** 0
- **Citations:** 29 references cited [1,14,15,16,17,18,19,20,21,23,24,26,29]
- **Special handling:**
  - System names (Isabelle, SACM, GSN, UTP, Tokeneer) kept in English
  - Standard names (ISO26262, DO-178C, DO-333) kept in English
  - Section references (§2-§8) kept as is

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
