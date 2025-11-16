# Section 2: Preliminaries
## القسم 2: المقدمات التمهيدية

**Section:** preliminaries
**Translation Quality:** 0.88
**Glossary Terms Used:** meta-model (نموذج فوقي), ontology (أنطولوجيا), theorem prover (مُثبِّت النظريات), higher order logic (منطق من الرتبة الأعلى), document model (نموذج المستند)

---

### English Version

**SACM.** Assurance cases are often presented using a notation like GSN [23] (Figure 1), that shows the claims that are made, the argumentation strategies, the contextual elements, assumptions, justifications, and eventually evidence. SACM is an OMG standard meta-model for assurance cases [20,28]. It aims at unifying and refining a variety of predecessor notations, including GSN [23] and CAE (Claims, Arguments, and Evidence), and is intended to be a definitive reference model.

SACM has three crucial concepts: arguments, artifacts, and terminology. An argument consists of a collection of claims, evidence citations, and inferential links between them. Artifacts manifest evidence, such as models, techniques, results, verification activities, and participants. Terminology is used to fix formal terms for the use in claims. Normally, claims are textual, but in SACM they can also contain structured expressions, which allows integration of formal languages.

The argumentation meta-model is shown in Figure 2. The base class is ArgumentAsset, which groups the argument assets, such as Claims, ArtifactReferences, and AssertedRelationships (which are inferential links). Every asset may contain a MultiLangString that provides a description, potentially in multiple natural and formal languages, and corresponds to contents of the shapes in Figure 1.

AssertedRelationships represent a relationship that exists between several assets. They can be of type AssertedContext, which uses an artifact to define context; AssertedEvidence, which evidences a claim; AssertedInference which describes explicit reasoning from premises to conclusion(s); or AssertedArtifactSupport which documents an inferential dependency between the claims of two artifacts.

Both Claims and AssertedRelationships inherit from Assertion, because in SACM both claims and inferential links are subject to argumentation and refutation. SACM allows six different classes of assertion, via the attribute assertionDeclaration, including axiomatic (needing no further support), assumed, and defeated, where a claim is refuted. An AssertedRelationship can also be flagged as isCounter, where counterevidence for a claim is presented.

**Isabelle.** Isabelle/HOL is an interactive theorem prover for higher order logic (HOL) [24], based on the generic framework Isabelle/Isar [30]. The former provides a functional specification language, and a large array of facilities for proof and automated verification. The latter has an interactive, extensible, and executable document model, which describes Isabelle theories. An Isabelle theory contains a sequence of executable markup commands with a semantics given in the meta-language SML.

Figure 3 gives an overview of the document model. The first section for context definition describes imports of existing theories, and keywords which give extensions to the concrete syntax. The second section is the body enclosed between begin-end which is a sequence of commands. Isabelle commands have a concrete syntax consisting of pre-declared top-level keywords (in blue), such as the command ML, followed by a "semantics area" enclosed between <...>. The keywords can be associated with optional attribute keywords (in green). The processing of the concrete syntax and any extensions is performed by SML code.

An Isabelle session is as an acyclic graph grouping several theories and their dependencies. When an edit is made to a document in a session, it is immediately processed and executed, with feedback provided to the user. For example, whenever the dependency structure of a document changes due to the removal, addition, or alteration of artifacts, Isabelle reruns the associated code and any dependencies. This feature makes Isabelle ideal for assurance cases, which have to be updated with every increment in system development.

In addition to formal content, Isabelle theories can also contain informal commentary. The text <...> command is a processor for textual markup content containing a mixture of informal content, and links to formal document entities through antiquotations of the form @{aqname ...}. Antiquotations trigger a series of checks, for example the antiquotation @{thm <HOL.refl>} checks if the theorem HOL.refl exists within the underlying theory context, and if so inserts a hyperlink.

Plugins, such as Isabelle/HOL, HOL-TestGen [3], and Isabelle/DOF [2] contain document models and conservative extensions, following the LCF approach. Isabelle/DOF [2] is a plugin that the Isabelle/Isar document model implemented with support for ontologies. The result is a machine-checked document model with formal hyperlinks between document instances of the modelled ontology.

The central component of Isabelle/DOF is the Isabelle Ontology Specification Language (IOSL), which describes the content of documents in terms of several document classes. Document classes can be linked to form a class model. We refer to [2] for examples to model document content within Isabelle/DOF. A document class is the main entity in IOSL and it is represented using the command doc_class, which creates a new class with a number of typed attributes. The attributes of doc_class can refer both to the standard HOL types such as string, bool, and also internal Isabelle meta-types such as thm, term, or typ, which represent theorems, logical terms, and types, respectively. This is because DOF ontologies sit a the meta-logical level, and so they can freely mix formal and informal content. This is our motivation for its use in mechanising SACM.

---

### النسخة العربية

**SACM.** غالباً ما يتم تقديم حالات الضمان باستخدام تدوين مثل GSN [23] (الشكل 1)، الذي يُظهر الادعاءات المقدمة، واستراتيجيات الحجاج، والعناصر السياقية، والافتراضات، والتبريرات، وفي النهاية الأدلة. SACM هو نموذج فوقي معياري من OMG لحالات الضمان [20،28]. يهدف إلى توحيد وتنقيح مجموعة متنوعة من التدوينات السابقة، بما في ذلك GSN [23] و CAE (الادعاءات، الحجج، والأدلة)، ويُقصد به أن يكون نموذجاً مرجعياً نهائياً.

يحتوي SACM على ثلاثة مفاهيم حاسمة: الحجج، والمصنوعات، والمصطلحات. تتكون الحجة من مجموعة من الادعاءات، واستشهادات الأدلة، والروابط الاستنتاجية بينها. تُظهر المصنوعات الأدلة، مثل النماذج، والتقنيات، والنتائج، وأنشطة التحقق، والمشاركين. تُستخدم المصطلحات لتثبيت المصطلحات الرسمية للاستخدام في الادعاءات. عادةً ما تكون الادعاءات نصية، ولكن في SACM يمكن أن تحتوي أيضاً على تعبيرات منظمة، مما يسمح بتكامل اللغات الرسمية.

يظهر النموذج الفوقي للحجاج في الشكل 2. الصنف الأساسي هو ArgumentAsset، الذي يجمع أصول الحجة، مثل Claims (الادعاءات)، و ArtifactReferences (مراجع المصنوعات)، و AssertedRelationships (العلاقات المؤكدة) (وهي روابط استنتاجية). قد يحتوي كل أصل على MultiLangString الذي يوفر وصفاً، يحتمل أن يكون بلغات طبيعية ورسمية متعددة، ويقابل محتويات الأشكال في الشكل 1.

تمثل AssertedRelationships علاقة موجودة بين عدة أصول. يمكن أن تكون من نوع AssertedContext، الذي يستخدم مصنوعاً لتحديد السياق؛ AssertedEvidence، الذي يدلل على ادعاء؛ AssertedInference الذي يصف الاستدلال الصريح من المقدمات إلى الاستنتاج (الاستنتاجات)؛ أو AssertedArtifactSupport الذي يوثق اعتماداً استنتاجياً بين ادعاءات مصنوعين.

ترث كل من Claims و AssertedRelationships من Assertion، لأنه في SACM كلاً من الادعاءات والروابط الاستنتاجية تخضع للمناقشة والدحض. يسمح SACM بستة فئات مختلفة من التأكيد، عبر سمة assertionDeclaration، بما في ذلك axiomatic (البديهي) (لا يحتاج إلى دعم إضافي)، و assumed (المفترض)، و defeated (المهزوم)، حيث يتم دحض ادعاء. يمكن أيضاً وضع علامة على AssertedRelationship على أنها isCounter، حيث يتم تقديم دليل مضاد لادعاء.

**Isabelle.** Isabelle/HOL هو مُثبِّت نظريات تفاعلي للمنطق من الرتبة الأعلى (HOL) [24]، يعتمد على الإطار العام Isabelle/Isar [30]. يوفر الأول لغة مواصفات وظيفية، ومجموعة كبيرة من المرافق للإثبات والتحقق الآلي. يحتوي الأخير على نموذج مستند تفاعلي وقابل للتوسيع وقابل للتنفيذ، والذي يصف نظريات Isabelle. تحتوي نظرية Isabelle على تسلسل من أوامر الترميز القابلة للتنفيذ مع دلالات معطاة في اللغة الفوقية SML.

يعطي الشكل 3 نظرة عامة على نموذج المستند. يصف القسم الأول لتعريف السياق استيرادات النظريات الموجودة، والكلمات المفتاحية التي تعطي امتدادات للبنية التركيبية الملموسة. القسم الثاني هو الجسم المحصور بين begin-end وهو تسلسل من الأوامر. تحتوي أوامر Isabelle على بنية تركيبية ملموسة تتكون من كلمات مفتاحية من المستوى الأعلى معلنة مسبقاً (باللون الأزرق)، مثل الأمر ML، متبوعة بـ "منطقة الدلالات" المحصورة بين <...>. يمكن ربط الكلمات المفتاحية بكلمات مفتاحية للسمات الاختيارية (باللون الأخضر). يتم تنفيذ معالجة البنية التركيبية الملموسة وأي امتدادات بواسطة شفرة SML.

جلسة Isabelle هي رسم بياني لا دوري يجمع عدة نظريات وتبعياتها. عند إجراء تعديل على مستند في جلسة، يتم معالجته وتنفيذه على الفور، مع تقديم ملاحظات للمستخدم. على سبيل المثال، كلما تغيرت بنية تبعية المستند بسبب إزالة أو إضافة أو تعديل المصنوعات، يعيد Isabelle تشغيل الشفرة المرتبطة وأي تبعيات. تجعل هذه الميزة Isabelle مثالياً لحالات الضمان، التي يجب تحديثها مع كل زيادة في تطوير النظام.

بالإضافة إلى المحتوى الرسمي، يمكن أن تحتوي نظريات Isabelle أيضاً على تعليقات غير رسمية. الأمر text <...> هو معالج لمحتوى الترميز النصي الذي يحتوي على مزيج من المحتوى غير الرسمي، وروابط إلى كيانات المستندات الرسمية من خلال الاقتباسات القديمة (antiquotations) بالصيغة @{aqname ...}. تؤدي الاقتباسات القديمة إلى سلسلة من الفحوصات، على سبيل المثال الاقتباس القديم @{thm <HOL.refl>} يتحقق مما إذا كانت النظرية HOL.refl موجودة ضمن سياق النظرية الأساسي، وإذا كان الأمر كذلك يُدرج رابطاً فائقاً.

تحتوي المكونات الإضافية، مثل Isabelle/HOL و HOL-TestGen [3] و Isabelle/DOF [2] على نماذج مستندات وامتدادات محافظة، باتباع نهج LCF. Isabelle/DOF [2] هو مكون إضافي لنموذج مستند Isabelle/Isar المنفذ بدعم للأنطولوجيات. النتيجة هي نموذج مستند متحقق منه آلياً مع روابط فائقة رسمية بين مثيلات المستندات للأنطولوجيا المنمذجة.

المكون المركزي لـ Isabelle/DOF هو لغة مواصفات الأنطولوجيا Isabelle (IOSL)، التي تصف محتوى المستندات من حيث عدة فئات من المستندات. يمكن ربط فئات المستندات لتشكيل نموذج فئة. نشير إلى [2] للحصول على أمثلة لنمذجة محتوى المستند ضمن Isabelle/DOF. فئة المستند هي الكيان الرئيسي في IOSL ويتم تمثيلها باستخدام الأمر doc_class، الذي ينشئ فئة جديدة مع عدد من السمات المكتوبة. يمكن أن تشير سمات doc_class إلى أنواع HOL القياسية مثل string و bool، وأيضاً أنواع Isabelle الفوقية الداخلية مثل thm و term أو typ، والتي تمثل النظريات، والحدود المنطقية، والأنواع، على التوالي. هذا لأن أنطولوجيات DOF تقع على المستوى الفوقي المنطقي، وبالتالي يمكنها مزج المحتوى الرسمي وغير الرسمي بحرية. هذا هو دافعنا لاستخدامه في أتمتة SACM.

---

### Translation Notes

- **Figures referenced:** Figure 1 (GSN notation), Figure 2 (SACM Argumentation Meta-Model), Figure 3 (Document Model)
- **Key terms introduced:**
  - SACM (النموذج الفوقي لحالة الضمان المهيكلة)
  - GSN - Goal Structuring Notation (تدوين هيكلة الأهداف)
  - CAE - Claims, Arguments, and Evidence (الادعاءات، الحجج، والأدلة)
  - ArgumentAsset (أصل الحجة)
  - MultiLangString (سلسلة متعددة اللغات)
  - AssertedRelationship (العلاقة المؤكدة)
  - Isabelle/HOL
  - Higher order logic - HOL (المنطق من الرتبة الأعلى)
  - Isabelle/Isar
  - SML - meta-language
  - Antiquotation (الاقتباس القديم)
  - LCF approach (نهج LCF)
  - Isabelle/DOF
  - IOSL - Isabelle Ontology Specification Language (لغة مواصفات الأنطولوجيا Isabelle)
- **Equations:** 0
- **Citations:** [2,3,20,23,24,28,30]
- **Special handling:**
  - Technical names (SACM, GSN, CAE, Isabelle, HOL, SML, LCF, DOF, IOSL) kept in English
  - Class names (ArgumentAsset, AssertedRelationship, etc.) kept in English with Arabic explanation
  - Code syntax (@{thm}, doc_class, etc.) kept as is

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
