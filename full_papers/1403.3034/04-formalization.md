# Section 4: Formalizing the Signalling Domain
## القسم 4: صياغة مجال الإشارات رسميًا

**Section:** formalization
**Translation Quality:** 0.86
**Glossary Terms Used:** algebraic specification (المواصفات الجبرية), CASL (CASL), Modal CASL (Modal CASL), formal methods (الأساليب الرسمية), UML (يو إم إل), comorphism (كوموفيزم), specification formalism (شكلية المواصفات)

---

### English Version

**Introduction**

We now present the formalisation of our DSL in CASL. We introduce CASL and Modal CASL, and discuss an automatic formalisation of UML class diagrams. Finally, we model the railway narrative for movement authorities.

**4.1 Background: The Underlying Specification Formalisms**

We introduce the relevant background on CASL, Modal CASL and give details on translating Modal CASL to CASL.

**CASL**

The Common Algebraic Specification Language, known as CASL, is a specification formalism developed by the CoFI initiative throughout the late 1990's and early 2000's in order to design a *Common Framework for Algebraic Specification and Development*. CASL has *basic*, *structured*, and *architectural* specifications, of which we consider the first two kinds only.

Roughly speaking, a CASL *basic specification* consists of a *signature* made up of sorts, operations, and predicates (declared by means of the keywords **sort**, **op**, and **pred**, respectively), and axioms referring to the signature items. Operations can be partial or total. Furthermore, one may declare a *subsort relation* on the sort symbols. Axioms are written in first-order logic. Going one step beyond first order logic, CASL also features sort generation constraints for datatypes (keywords **generated**, **free type**).

As an example consider the CASL specification in Figure 6 formalising the concept of time. The specification has the name Time. It specifies the sort symbol Time, the constant function symbol 0, the total function symbol suc from sort Time to sort Time, the partial function symbol pre from sort Time to sort Time and the predicate symbol \_\_ <= \_\_ over Time × Time. The axiom is a first order formula stating that 0 denotes the smallest element of sort Time.

A *model* of a CASL specification is an algebra which interprets sorts as (non empty) sets and operations and predicates as (partial) functions and subsets respectively, in such a way that the given axioms are satisfied. The subsorting relation is reflected by injective coercion functions between the sets interpreting the involved sorts (*not* by subset inclusion). The collection of all these models is called the *model class* of the specification. It is a speciality of CASL to support *loose specification*, i.e., to write a specification that has algebras of different "forms" in its model class.

The CASL specification Time of Figure 6 has the naturals with the standard interpretations as its model, i.e., discrete time is a possible model. It also has the non-negative reals as a model, i.e., dense continuous time is a possible model as well. The CASL specification Time is a typical example of a loose specification with algebras of different form: the naturals are countable, while the non-negative reals are not countable.

Besides basic specifications, CASL provides ways of building complex (*structured*) specifications out of simpler ones (the simplest being basic specifications) by means of various *specification-building operations*. These include translation, hiding, union, and both free and loose forms of extension.

*Translations* of declared symbols to new symbols are specified by giving lists of 'maplets' of the form old ↦ new (keyword **with**).

The signature of a *union* of two specifications is the union of their signatures. Given models over the component signatures, the unique model over the union signature that extends each of these models is called their *amalgamation*. The models of a union (keyword **and**) are all amalgamations of the models of the component specifications.

*Extensions* (keyword **then**) may specify new symbols or merely require further properties of old ones. Extensions can be classified by their effect on the specified model class. For instance, an extension is called *implicational* (annotation **%implies**) if the signature and model class remain unchanged.

**Modal CASL**

Modal CASL extends CASL with modal operators for describing state-based systems. It allows specification of dynamic behavior through modalities. The modal operators enable reasoning about temporal properties and state transitions, which is particularly useful for modeling railway systems with changing states.

**4.2 Contribution: Comorphism from UML to Modal CASL**

We present an automatic translation from UML class diagrams to Modal CASL specifications. This comorphism preserves the structure and semantics of the UML diagram while adding formal semantics. The translation handles:

- Classes → Sorts
- Properties → Operations
- Associations → Predicates
- Generalisations → Subsort relations
- Multiplicities → Axioms

This automatic translation ensures faithful modelling by maintaining a direct correspondence between the informal DSL and formal specification.

**4.3 Contribution: Narrative Modelling**

We formalize the dynamic behavior described in the railway narrative (N1 and N2) using Modal CASL. The movement authority extension and release operations are captured as modal transitions. This formalization allows us to specify and verify safety properties about movement authorities, such as ensuring that overlapping movement authorities are never assigned simultaneously.

The complete formal specification combines the automatically generated UML translation with the hand-crafted narrative formalization, resulting in a comprehensive model of the railway signalling domain that can be used for automated verification.

---

### النسخة العربية

**مقدمة**

نقدم الآن الصياغة الرسمية للغتنا الخاصة بالمجال في CASL. نقدم CASL و Modal CASL، ونناقش الصياغة الرسمية التلقائية لمخططات فئات UML. أخيرًا، نمذجة السرد الخاص بالسكك الحديدية لسلطات الحركة.

**4.1 خلفية: شكليات المواصفات الأساسية**

نقدم الخلفية ذات الصلة حول CASL و Modal CASL ونقدم تفاصيل حول ترجمة Modal CASL إلى CASL.

**CASL**

لغة المواصفات الجبرية الشائعة، المعروفة باسم CASL، هي شكلية مواصفات تم تطويرها من قبل مبادرة CoFI طوال أواخر التسعينيات وأوائل الألفية الثانية من أجل تصميم *إطار عمل مشترك للمواصفات الجبرية والتطوير*. تحتوي CASL على مواصفات *أساسية* و *منظمة* و *معمارية*، ونحن نعتبر النوعين الأولين فقط.

بشكل تقريبي، تتكون *المواصفات الأساسية* لـ CASL من *توقيع* مكون من أنواع، وعمليات، ومحمولات (معلن عنها بواسطة الكلمات الرئيسية **sort** و **op** و **pred**، على التوالي)، وبديهيات تشير إلى عناصر التوقيع. يمكن أن تكون العمليات جزئية أو كلية. علاوة على ذلك، يمكن للمرء أن يعلن عن *علاقة نوع فرعي* على رموز الأنواع. يتم كتابة البديهيات في منطق من الدرجة الأولى. تجاوزًا لمنطق من الدرجة الأولى، تتميز CASL أيضًا بقيود توليد الأنواع لأنواع البيانات (الكلمات الرئيسية **generated** و **free type**).

كمثال، انظر إلى مواصفات CASL في الشكل 6 التي تصوغ مفهوم الوقت رسميًا. المواصفات لها اسم Time. تحدد رمز النوع Time، ورمز الدالة الثابتة 0، ورمز الدالة الكلية suc من النوع Time إلى النوع Time، ورمز الدالة الجزئية pre من النوع Time إلى النوع Time، ورمز المحمول \_\_ <= \_\_ على Time × Time. البديهية هي صيغة من الدرجة الأولى تنص على أن 0 يشير إلى أصغر عنصر من النوع Time.

*نموذج* مواصفات CASL هو جبر يفسر الأنواع كمجموعات (غير فارغة) والعمليات والمحمولات كدوال (جزئية) ومجموعات فرعية على التوالي، بطريقة تُرضي البديهيات المعطاة. تنعكس علاقة النوع الفرعي بدوال إكراه حقنية بين المجموعات التي تفسر الأنواع المعنية (*وليس* بواسطة تضمين المجموعات الفرعية). تسمى مجموعة كل هذه النماذج *فئة النموذج* للمواصفات. من خصوصيات CASL دعم *المواصفات الفضفاضة*، أي كتابة مواصفات لها جبريات من "أشكال" مختلفة في فئة نموذجها.

مواصفات CASL Time من الشكل 6 لها الأعداد الطبيعية مع التفسيرات القياسية كنموذجها، أي أن الوقت المنفصل هو نموذج محتمل. كما أنه لديه الأعداد الحقيقية غير السالبة كنموذج، أي أن الوقت المستمر الكثيف هو نموذج محتمل أيضًا. مواصفات CASL Time هي مثال نموذجي على المواصفات الفضفاضة مع جبريات من شكل مختلف: الأعداد الطبيعية قابلة للعد، بينما الأعداد الحقيقية غير السالبة ليست قابلة للعد.

إلى جانب المواصفات الأساسية، توفر CASL طرقًا لبناء مواصفات معقدة (*منظمة*) من مواصفات أبسط (الأبسط هي المواصفات الأساسية) بواسطة *عمليات بناء المواصفات* المختلفة. تشمل هذه الترجمة، والإخفاء، والاتحاد، وكل من الأشكال الحرة والفضفاضة للتوسع.

يتم تحديد *الترجمات* للرموز المعلنة إلى رموز جديدة من خلال إعطاء قوائم من 'الخرائط' من الشكل old ↦ new (الكلمة الرئيسية **with**).

توقيع *اتحاد* مواصفتين هو اتحاد توقيعاتهما. بالنظر إلى النماذج على توقيعات المكونات، يُسمى النموذج الفريد على توقيع الاتحاد الذي يوسع كل هذه النماذج *دمجها*. نماذج الاتحاد (الكلمة الرئيسية **and**) هي جميع عمليات الدمج لنماذج مواصفات المكونات.

قد تحدد *التوسعات* (الكلمة الرئيسية **then**) رموزًا جديدة أو تتطلب ببساطة خصائص إضافية للرموز القديمة. يمكن تصنيف التوسعات من خلال تأثيرها على فئة النموذج المحددة. على سبيل المثال، تسمى التوسعة *ضمنية* (التعليق التوضيحي **%implies**) إذا ظل التوقيع وفئة النموذج دون تغيير.

**Modal CASL**

يمتد Modal CASL لـ CASL مع عوامل موديولية لوصف الأنظمة القائمة على الحالة. يسمح بتحديد السلوك الديناميكي من خلال الموديوليات. تمكن العوامل الموديولية من الاستدلال حول الخصائص الزمنية وانتقالات الحالة، وهو أمر مفيد بشكل خاص لنمذجة أنظمة السكك الحديدية ذات الحالات المتغيرة.

**4.2 المساهمة: الكوموفيزم من UML إلى Modal CASL**

نقدم ترجمة تلقائية من مخططات فئات UML إلى مواصفات Modal CASL. يحافظ هذا الكوموفيزم على بنية ودلالات مخطط UML مع إضافة دلالات رسمية. تتعامل الترجمة مع:

- الفئات ← الأنواع
- الخصائص ← العمليات
- الارتباطات ← المحمولات
- التعميمات ← علاقات الأنواع الفرعية
- التعددية ← البديهيات

تضمن هذه الترجمة التلقائية النمذجة الأمينة من خلال الحفاظ على مراسلة مباشرة بين اللغة الخاصة بالمجال غير الرسمية والمواصفات الرسمية.

**4.3 المساهمة: نمذجة السرد**

نصوغ رسميًا السلوك الديناميكي الموصوف في سرد السكك الحديدية (N1 و N2) باستخدام Modal CASL. يتم التقاط عمليات تمديد وإفراج سلطة الحركة كانتقالات موديولية. تسمح لنا هذه الصياغة الرسمية بتحديد والتحقق من خصائص السلامة حول سلطات الحركة، مثل ضمان عدم تعيين سلطات الحركة المتداخلة في وقت واحد أبدًا.

تجمع المواصفات الرسمية الكاملة بين ترجمة UML التي تم إنشاؤها تلقائيًا وصياغة السرد المصنوعة يدويًا، مما ينتج عنه نموذج شامل لمجال إشارات السكك الحديدية الذي يمكن استخدامه للتحقق التلقائي.

---

### Translation Notes

- **Key concepts:** CASL, Modal CASL, specification formalism, comorphism, UML translation
- **Technical terminology:** sorts, operations, predicates, subsort relation, axioms, loose specification, model class
- **Figures referenced:** Figure 6 (CASL Time specification)
- **Special handling:** Formal specification language syntax preserved, technical terms carefully translated

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
