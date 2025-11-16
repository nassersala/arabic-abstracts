# Section 4: Related Work
## القسم 4: الأعمال ذات الصلة

**Section:** related work
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods (الأساليب الرسمية), model checking (فحص النماذج), theorem proving (إثبات النظريات), temporal logic (المنطق الزمني), first-order logic (منطق الدرجة الأولى)

---

### English Version

Several works faced with the problem of the formal specification and validation of requirements. Some of them focused on the problem of formalizing natural language specifications, other focused on the formal specification languages to be used in such a task, other proposed a methodological approach to the requirements representation and validation.

On the first side, works such as [FGR+94] and [AG06] aim at extracting automatically from a natural language description a formal model to be analyzed. However, their target formal languages cannot express temporal constraints over object models. Moreover, they miss a methodology for an adequate formal analysis of the requirements. Other works such as [GMM90, BDZ97] provided expressive formal languages to represent the requirements. Although, the proposed languages have some similarities with ours such as the adoption of first-order temporal logic, they do not allow specification of hybrid aspects which are necessary for safety-critical applications. Also these works miss a methodology for the analysis of the formal requirements and the verification algorithms are perform either with interactive theorem proving or with model checking restricted to propositional sub-cases.

Several formal specification languages such as Z [Spi92], B [Abr96], and OCL [OMG06] have been proposed for formal model-based specification. They are very expressive but require a deep background in order to write a correct formalization. Alloy [Jac02] is a formal language for describing structural properties of a system relying on the subset of Z [Spi92] that allows for object modeling. An Alloy specification consists of basic structures representing classes together with constraints and operations describing how the structures change dynamically. Alloy only allows to specify attributes belonging to finite domains (no Reals or Integers). Thus, it would have been impossible to model the Train position as requested by the ETCS specifications. Although Alloy supports the "next" operator ("prime" operator) to specify the temporal evolution of a given object, it does not allow to express properties using LTL and regular expressions.

Among the methodological approaches, in [HJL96], a framework is proposed for the automated checking of requirement specifications expressed in Software Cost Reduction tabular notation, which aims at detecting specification problems such as type errors, missing cases, circular definitions and non-determinism. Although this work has many related points to our approach, the proposed language is not adapt to formalize requirements that contain functional descriptions of the system at high level of abstraction with temporal assumptions on the environment. Formal Tropos (FT) [SPGM05, FLM+04] and KAOS [DDMvL97, vL09] are goal-oriented software development methodologies that provide a visual modeling language that can be used to define an informal specification, allowing to model intentional and social concepts, such as those of actor, goal, and social relationships between actors, and annotate the diagrams with temporal constraints to characterize the valid behaviors of the model. Both FT and KAOS are limited to propositional LTL temporal constraints, and thus not suitable for formalizing safety-critical requirements.

---

### النسخة العربية

واجهت العديد من الأعمال مشكلة المواصفات الرسمية والتحقق من صحة المتطلبات. ركز بعضها على مشكلة صياغة مواصفات اللغة الطبيعية رسميًا، بينما ركز البعض الآخر على لغات المواصفات الرسمية التي سيتم استخدامها في مثل هذه المهمة، واقترح آخرون نهجًا منهجيًا لتمثيل المتطلبات والتحقق من صحتها.

من الجانب الأول، تهدف أعمال مثل [FGR+94] و[AG06] إلى استخراج نموذج رسمي تلقائيًا من وصف باللغة الطبيعية ليتم تحليله. ومع ذلك، لا يمكن للغات الرسمية المستهدفة التعبير عن القيود الزمنية على نماذج الكائنات. علاوة على ذلك، تفتقر إلى منهجية للتحليل الرسمي الكافي للمتطلبات. قدمت أعمال أخرى مثل [GMM90، BDZ97] لغات رسمية تعبيرية لتمثيل المتطلبات. على الرغم من أن اللغات المقترحة لها بعض أوجه التشابه مع لغتنا مثل اعتماد منطق الدرجة الأولى الزمني، إلا أنها لا تسمح بتحديد الجوانب الهجينة الضرورية للتطبيقات الحرجة من حيث السلامة. كما تفتقر هذه الأعمال إلى منهجية لتحليل المتطلبات الرسمية ويتم تنفيذ خوارزميات التحقق إما باستخدام إثبات النظريات التفاعلي أو باستخدام فحص النماذج المقيد بالحالات الفرعية القضوية.

تم اقتراح العديد من لغات المواصفات الرسمية مثل Z [Spi92] وB [Abr96] وOCL [OMG06] للمواصفات الرسمية القائمة على النماذج. إنها تعبيرية للغاية ولكنها تتطلب خلفية عميقة من أجل كتابة صياغة رسمية صحيحة. Alloy [Jac02] هي لغة رسمية لوصف الخصائص الهيكلية للنظام بالاعتماد على مجموعة فرعية من Z [Spi92] تسمح بنمذجة الكائنات. تتكون مواصفات Alloy من بنى أساسية تمثل الفئات مع القيود والعمليات التي تصف كيفية تغير البنى ديناميكيًا. يسمح Alloy فقط بتحديد السمات التي تنتمي إلى مجالات محدودة (لا أعداد حقيقية أو صحيحة). وبالتالي، كان من المستحيل نمذجة موقع القطار كما هو مطلوب في مواصفات ETCS. على الرغم من أن Alloy يدعم عامل "next" (عامل "prime") لتحديد التطور الزمني لكائن معين، إلا أنه لا يسمح بالتعبير عن الخصائص باستخدام LTL والتعابير النظامية.

من بين الأساليب المنهجية، في [HJL96]، تم اقتراح إطار عمل للفحص الآلي لمواصفات المتطلبات المعبر عنها في تدوين جدولي لتقليل تكلفة البرمجيات، والذي يهدف إلى اكتشاف مشاكل المواصفات مثل أخطاء النوع والحالات المفقودة والتعريفات الدائرية وعدم الحتمية. على الرغم من أن هذا العمل له العديد من النقاط المتعلقة بنهجنا، إلا أن اللغة المقترحة غير مناسبة لصياغة المتطلبات التي تحتوي على أوصاف وظيفية للنظام على مستوى عالٍ من التجريد مع افتراضات زمنية على البيئة. Formal Tropos (FT) [SPGM05، FLM+04] وKAOS [DDMvL97، vL09] هي منهجيات تطوير برمجيات موجهة نحو الأهداف توفر لغة نمذجة مرئية يمكن استخدامها لتحديد مواصفات غير رسمية، تسمح بنمذجة المفاهيم النوايا والاجتماعية، مثل مفاهيم الفاعل والهدف والعلاقات الاجتماعية بين الفاعلين، والتعليق على المخططات بالقيود الزمنية لتوصيف السلوكيات الصحيحة للنموذج. كل من FT وKAOS محدودان بقيود LTL الزمنية القضوية، وبالتالي ليسا مناسبين لصياغة المتطلبات الحرجة من حيث السلامة رسميًا.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** natural language processing (معالجة اللغة الطبيعية), Z language (لغة Z), B language (لغة B), OCL (OCL), Alloy (Alloy), Software Cost Reduction (تقليل تكلفة البرمجيات), Formal Tropos/FT (Formal Tropos), KAOS (KAOS), goal-oriented (موجه نحو الأهداف), propositional LTL (LTL القضوي)
- **Equations:** 0
- **Citations:** 13 references (FGR+94, AG06, GMM90, BDZ97, Spi92, Abr96, OMG06, Jac02, HJL96, SPGM05, FLM+04, DDMvL97, vL09)
- **Special handling:** Technical names of formal languages (Z, B, OCL, Alloy, Formal Tropos, KAOS) kept in original form

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
