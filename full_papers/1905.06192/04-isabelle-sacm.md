# Section 4: Isabelle/SACM
## القسم 4: Isabelle/SACM

**Section:** isabelle-sacm
**Translation Quality:** 0.86
**Glossary Terms Used:** ontology (أنطولوجيا), meta-model (نموذج فوقي), embedding (تضمين), domain-specific language (لغة خاصة بالمجال), datatype (نوع بيانات)

---

### English Version

In the following we encode SACM in Isabelle/DOF as an ontology, and then use it to provide a concrete syntax for our assurance case language. Our embedding implements assurance cases as meta-logical entities. We are not embedding assurance arguments in the HOL logic, as this would prevent the expression of informal reasoning and explanation. Rather, SACM is implemented as a datatype in SML, meaning that we can refer to entities like types, terms, and theorems as objects. Thus, certain claims can contain formal expressions, but others may have unstructured natural language. Thus, we faithfully represent the inherently semi-formal nature of assurance cases.

We focus on the ArgumentationPackage from Figure 2, as this is most relevant for the TIS argument we develop in §6. Different types of evidences and context, modelled by the ArtifactPackage, can support a claim. The class ArgumentAsset is represented in Isabelle/DOF as follows:

```
doc_class ArgumentAsset = ArgumentationElement +
  content_assoc:: MultiLangString
```

Here, ArgumentationElement is a base class which ArgumentAsset inherits from, but is not discussed further. The content_assoc:: MultiLangString is an attribute modelling an association between ArgumentAsset and MultiLangString from the BasePackage. It allows classes inherited from ArgumentAsset to include content expressed in multiple languages, and also structured expressions, using the TerminologyPackage. Our implementation of MultiLangString allows us to embed a variety of informal and formal content utilising the Isabelle term language.

The class ArgumentAsset is inherited by three classes: (1) Assertion, which is a unified type for claims and their relationships; (2) ArgumentReasoning, which is used to explicate the argumentation strategy being employed; and (3) ArtifactReference, that evidences a claim with an artifact.

In Isabelle/DOF, ArgumentAsset is inherited as follows:

```
datatype assertionDeclarations_t =
  Asserted|Axiomatic|Defeated|Assumed|NeedsSupport
doc_class Assertion = ArgumentAsset +
  assertionDeclaration::assertionDeclarations_t
doc_class ArgumentReasoning = ArgumentAsset +
  structure_assoc::"ArgumentPackage option"
doc_class ArtifactReference = ArgumentAsset +
  referencedArtifactElement_assoc::"ArtifactElement set"
```

Here, assertionDeclarations_t is an Isabelle/HOL enumeration type, set is the set type, and option is the optional type. The attribute assertionDeclaration is of type assertionDeclarations_t, which specifies the status of assertions. The attribute structure_assoc is an association to the class ArgumentPackage, which is not discussed here. Finally, the attribute referencedArtifactElement_assoc is an association to the ArtifactPackage allowing claims to reference artifacts.

The class Claim is a leaf child class and inherits from the class Assertion. This means that an instance of Claim has a gid, a MultiLangString description, and can be Axiomatic, Asserted, etc. The other child class for Assertion is:

```
doc_class AssertedRelationship = Assertion +
  isCounter::bool
  reasoning_assoc:: "ArgumentReasoning option"
```

Here, isCounter specifies whether the target of the relation is refuted by the source, and reasoning_assoc is an association to ArgumentReasoning, to elaborate the strategy. AssertedRelationship models the relationships between elements of type ArgumentAsset. In addition to the inherited attributes from parent classes, the relationship classes have the attributes source and target. The source attribute carries the supporting elements and the target carries the supported elements.

From the SACM ontology, we create a number of Isabelle commands that create elements of the meta-model. Our approach gives a concrete syntax for SACM in terms of Isabelle commands as follows. Instances of concrete leaf child classes in the metamodel have concrete syntax consisting of an Isabelle top-level command. Instances of attributes of a leaf child class, including the inherited ones, have a concrete syntax represented by an Isabelle (green) subcommand. Instances of associations between leaf child classes have a concrete syntax represented by an Isabelle subcommand. The command has the name of the represented association and has an input with the type of the association of the underlying instance. A selection of the commands for SACM is shown below.

```
CLAIM <gid> CONTENT <MultiLangString>
ASSERTED_INFERENCE <gid> SOURCE <gid>* TARGET <gid>*
ASSERTED_CONTEXT <gid> SOURCE <gid>* TARGET <gid>*
ASSERTED_EVIDENCE <gid> SOURCE <gid>* TARGET <gid>*
ARTIFACT <gid> VERSION <text> DATE <text> CONTENT <MultiLangString>
```

CLAIM creates a new claim with an identifier (gid), and content described by a MultiLangString. ASSERTED_INFERENCE creates an inference between several claims. Is has subcommands SOURCE and TARGET that are both lists of elements. The command ensures that the cited claims exist, otherwise an error message is issued. ASSERTED_CONTEXT similarly asserts that an entity should be treated as context for another, and ASSERTED_EVIDENCE associates evidence with a claim. The ARTIFACT command creates an evidential artifact, with description, date, and content.

Each command also has an associated antiquotation, which can be used to reference the entity type in a claim string. This is illustrated in Figure 5, which shows the interactive nature of the assurance case language. It represents an inferential link between a strategy and a justification (cf. Figure 1). An asserted inference called Rel_A has been created that attempts to link existing claims Claim_A and Claim_B. However, Claim_B does not exist, and so the error message at the top of the screenshot is issued. A textual element is then created which references Rel_A using the antiquotation class @{AssertedInference ...}. This also leads to an error, shown at the bottom, since Rel_A does not exist.

We have now developed our interactive assurance case tool. In the next section we begin to consider assurance of the Tokeener system, first considering formal verification of the security properties.

---

### النسخة العربية

في ما يلي نقوم بتشفير SACM في Isabelle/DOF كأنطولوجيا، ثم نستخدمه لتوفير بنية تركيبية ملموسة للغة حالة الضمان الخاصة بنا. يطبق تضميننا حالات الضمان ككيانات منطقية فوقية. نحن لا نضمن حجج الضمان في منطق HOL، لأن ذلك سيمنع التعبير عن الاستدلال والتفسير غير الرسمي. بدلاً من ذلك، يتم تطبيق SACM كنوع بيانات في SML، مما يعني أنه يمكننا الإشارة إلى كيانات مثل الأنواع، والحدود، والنظريات ككائنات. وبالتالي، يمكن أن تحتوي بعض الادعاءات على تعبيرات رسمية، ولكن قد يكون لدى البعض الآخر لغة طبيعية غير منظمة. وبالتالي، نمثل بأمانة الطبيعة شبه الرسمية المتأصلة لحالات الضمان.

نركز على ArgumentationPackage من الشكل 2، حيث أن هذا هو الأكثر صلة بحجة TIS التي نطورها في §6. يمكن لأنواع مختلفة من الأدلة والسياق، المنمذجة بواسطة ArtifactPackage، دعم ادعاء. يتم تمثيل الصنف ArgumentAsset في Isabelle/DOF على النحو التالي:

```
doc_class ArgumentAsset = ArgumentationElement +
  content_assoc:: MultiLangString
```

هنا، ArgumentationElement هو صنف أساسي يرث منه ArgumentAsset، ولكن لا تتم مناقشته بشكل أكبر. content_assoc:: MultiLangString هي سمة تنمذج ارتباطاً بين ArgumentAsset و MultiLangString من BasePackage. تسمح للأصناف الموروثة من ArgumentAsset بتضمين محتوى معبر عنه بلغات متعددة، وأيضاً تعبيرات منظمة، باستخدام TerminologyPackage. يتيح لنا تطبيقنا لـ MultiLangString تضمين مجموعة متنوعة من المحتوى غير الرسمي والرسمي باستخدام لغة حدود Isabelle.

يتم وراثة الصنف ArgumentAsset بواسطة ثلاثة أصناف: (1) Assertion، وهو نوع موحد للادعاءات وعلاقاتها؛ (2) ArgumentReasoning، الذي يُستخدم لتوضيح استراتيجية الحجاج المستخدمة؛ و(3) ArtifactReference، الذي يدلل على ادعاء بمصنوع.

في Isabelle/DOF، يتم وراثة ArgumentAsset على النحو التالي:

```
datatype assertionDeclarations_t =
  Asserted|Axiomatic|Defeated|Assumed|NeedsSupport
doc_class Assertion = ArgumentAsset +
  assertionDeclaration::assertionDeclarations_t
doc_class ArgumentReasoning = ArgumentAsset +
  structure_assoc::"ArgumentPackage option"
doc_class ArtifactReference = ArgumentAsset +
  referencedArtifactElement_assoc::"ArtifactElement set"
```

هنا، assertionDeclarations_t هو نوع تعداد Isabelle/HOL، و set هو نوع المجموعة، و option هو النوع الاختياري. السمة assertionDeclaration من نوع assertionDeclarations_t، التي تحدد حالة التأكيدات. السمة structure_assoc هي ارتباط بالصنف ArgumentPackage، الذي لا تتم مناقشته هنا. أخيراً، السمة referencedArtifactElement_assoc هي ارتباط بـ ArtifactPackage تسمح للادعاءات بالإشارة إلى المصنوعات.

الصنف Claim هو صنف فرعي ورقي ويرث من الصنف Assertion. هذا يعني أن مثيل Claim له gid، ووصف MultiLangString، ويمكن أن يكون Axiomatic، أو Asserted، إلخ. الصنف الفرعي الآخر لـ Assertion هو:

```
doc_class AssertedRelationship = Assertion +
  isCounter::bool
  reasoning_assoc:: "ArgumentReasoning option"
```

هنا، يحدد isCounter ما إذا كان هدف العلاقة مدحوضاً بواسطة المصدر، و reasoning_assoc هو ارتباط بـ ArgumentReasoning، لتوضيح الاستراتيجية. ينمذج AssertedRelationship العلاقات بين عناصر من نوع ArgumentAsset. بالإضافة إلى السمات الموروثة من الأصناف الأصلية، تحتوي أصناف العلاقة على السمات source و target. تحمل سمة source العناصر الداعمة وتحمل target العناصر المدعومة.

من أنطولوجيا SACM، نقوم بإنشاء عدد من أوامر Isabelle التي تنشئ عناصر النموذج الفوقي. يعطي نهجنا بنية تركيبية ملموسة لـ SACM من حيث أوامر Isabelle على النحو التالي. تحتوي مثيلات الأصناف الفرعية الورقية الملموسة في النموذج الفوقي على بنية تركيبية ملموسة تتكون من أمر Isabelle من المستوى الأعلى. تحتوي مثيلات سمات صنف فرعي ورقي، بما في ذلك الموروثة، على بنية تركيبية ملموسة ممثلة بأمر فرعي Isabelle (أخضر). تحتوي مثيلات الارتباطات بين أصناف فرعية ورقية على بنية تركيبية ملموسة ممثلة بأمر فرعي Isabelle. يحتوي الأمر على اسم الارتباط الممثل وله مدخل بنوع الارتباط للمثيل الأساسي. يظهر اختيار من الأوامر لـ SACM أدناه.

```
CLAIM <gid> CONTENT <MultiLangString>
ASSERTED_INFERENCE <gid> SOURCE <gid>* TARGET <gid>*
ASSERTED_CONTEXT <gid> SOURCE <gid>* TARGET <gid>*
ASSERTED_EVIDENCE <gid> SOURCE <gid>* TARGET <gid>*
ARTIFACT <gid> VERSION <text> DATE <text> CONTENT <MultiLangString>
```

ينشئ CLAIM ادعاءً جديداً بمعرف (gid)، ومحتوى موصوف بـ MultiLangString. ينشئ ASSERTED_INFERENCE استنتاجاً بين عدة ادعاءات. لديه أوامر فرعية SOURCE و TARGET وكلاهما قوائم من العناصر. يضمن الأمر وجود الادعاءات المستشهد بها، وإلا يتم إصدار رسالة خطأ. يؤكد ASSERTED_CONTEXT بالمثل أنه يجب التعامل مع كيان كسياق لآخر، ويربط ASSERTED_EVIDENCE دليلاً بادعاء. ينشئ أمر ARTIFACT مصنوعاً إثباتياً، مع الوصف والتاريخ والمحتوى.

لكل أمر أيضاً اقتباس قديم مرتبط، يمكن استخدامه للإشارة إلى نوع الكيان في سلسلة ادعاء. يوضح هذا في الشكل 5، الذي يُظهر الطبيعة التفاعلية للغة حالة الضمان. يمثل رابطاً استنتاجياً بين استراتيجية وتبرير (قارن الشكل 1). تم إنشاء استنتاج مؤكد يسمى Rel_A يحاول ربط الادعاءات الموجودة Claim_A و Claim_B. ومع ذلك، لا يوجد Claim_B، وبالتالي يتم إصدار رسالة الخطأ في أعلى لقطة الشاشة. ثم يتم إنشاء عنصر نصي يشير إلى Rel_A باستخدام فئة الاقتباس القديم @{AssertedInference ...}. هذا يؤدي أيضاً إلى خطأ، موضح في الأسفل، حيث أن Rel_A غير موجود.

لقد طورنا الآن أداة حالة الضمان التفاعلية الخاصة بنا. في القسم التالي نبدأ في النظر في ضمان نظام Tokeneer، مع النظر أولاً في التحقق الرسمي من خصائص الأمان.

---

### Translation Notes

- **Figures referenced:** Figure 2 (SACM Argumentation Meta-Model), Figure 5 (Relations in Isabelle/SACM)
- **Key terms introduced:**
  - Meta-logical entities (كيانات منطقية فوقية)
  - Embedding (تضمين)
  - Datatype (نوع بيانات)
  - ArgumentationPackage (حزمة الحجاج)
  - ArtifactPackage (حزمة المصنوعات)
  - BasePackage (الحزمة الأساسية)
  - TerminologyPackage (حزمة المصطلحات)
  - Enumeration type (نوع تعداد)
  - Set type (نوع المجموعة)
  - Optional type (النوع الاختياري)
  - Antiquotation (الاقتباس القديم)
  - Global identifier - gid (معرف عام)
- **Equations:** 0
- **Citations:** None in this section
- **Special handling:**
  - Code blocks kept in English with syntax preserved
  - Class names (ArgumentAsset, Assertion, Claim, etc.) kept in English
  - Command syntax (CLAIM, ASSERTED_INFERENCE, etc.) kept in English
  - Type names (bool, option, set, etc.) kept in English
  - Isabelle-specific terms (doc_class, datatype) kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
