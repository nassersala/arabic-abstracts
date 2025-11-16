# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods (الأساليب الرسمية), model checking (فحص النماذج), theorem proving (إثبات النظريات), property-based approach (النهج القائم على الخصائص), satisfiability (الإرضاء)

---

### English Version

*Formal methods* are widely used in the development process of safety-critical systems. The application of formal verification techniques relies on the formalization of the system's design into a mathematical language. Several formal languages are available according to the different aspects that are relevant to the verification, and many design tools can automatically formalize the design into one of these languages. The verification techniques typically trade-off the automation of the analysis with the expressiveness of the specification language. State-of-the-art approaches mix *model checking* and *theorem proving* in order to tackle the verification of infinite-state systems with a sufficient level of automation.

Another important aspect of the development process is the correctness of the *requirements*. Very often bugs in the late phases are caused by some flaws in requirements specification. These are difficult to detect and have a huge impact on the cost of fixing the bug. Nevertheless, formal methods on requirements validation are not yet mature. In particular there is no precise definition of correct requirements.

The most relevant solution has been proposed in the context of the *property-based approach* to design, where the development process starts from listing a set of formal properties, rather than defining an abstract-level model. The requirements validation is performed with a series of checks that improve the confidence in the correctness of the requirements. These checks consist of verifying that the requirements do not contain contradictions and that they are neither too strict to forbid desired behaviors, nor too weak to allow undesired behaviors. This process relies on the availability of a sufficiently expressive logic so that properties as well as desired and undesired behaviors can be formalized into formulas. The approach considers a one-to-one mapping between the properties and the logical formulas. This allows for traceability of the formalization and the validation results, and for incremental and modular approaches to the validation.

In the context of safety-critical applications, the choice of the language used to formalize the requirements is still an open issue, requiring a delicate balance between expressiveness, decidability, and complexity of inference. The difficulty in finding a suitable trade-off lies in the fact that the requirements for many real-world applications involve several dimensions. On the one side, the objects having an active role in the target application may have complex structure and mutual relationships, whose modeling may require the use of rich data types. On the other side, static constraints over their attributes must be complemented with constraints on their temporal evolution.

One of the main obstacle in applying this approach to the industrial level is that requirements are often written in a natural language so that a domain knowledge is necessary both to formalize them and to define which behaviors are desirable and which not during the validation process. Since domain experts are typically not advanced users of formal methods, they must be provided with a rich but friendly language for the formal specification and an automatic but scalable engine for the formal verification.

In this paper, we report on a methodology and a series of techniques that we developed for the formalization and validation of high-level requirements for safety-critical applications. The methodology is based on a three-phases approach that goes from the informal analysis of the requirements, to their formalization and validation [CRST08a]. The methodology relies on two main ingredients: a very expressive formal language and automatic satisfiability procedures. The language combines first-order, temporal, and hybrid logic [CRST08b, CRST09, CRT09]. The satisfiability procedures are based on model checking and satisfiability modulo theory. We applied this technology within an industrial project to the validation of railways requirements. The tool [CCM+09] integrates, within a commercial environment, techniques for requirements management and model-based design, and advanced techniques for formal validation with the model checker NuSMV [CCGR00].

The rest of the paper is organized as follow: in Section 2, we outline the proposed methodology, giving details on the chosen language in Section 2.1 and on the validation procedure in Section 2.2; in Section 3, we describe the project where the methodology was applied; in Section 4, we review the related work, and in Section 5, we conclude.

---

### النسخة العربية

تُستخدم *الأساليب الرسمية* على نطاق واسع في عملية تطوير الأنظمة الحرجة من حيث السلامة. يعتمد تطبيق تقنيات التحقق الرسمي على صياغة تصميم النظام في لغة رياضية. تتوفر العديد من اللغات الرسمية وفقًا للجوانب المختلفة ذات الصلة بالتحقق، ويمكن للعديد من أدوات التصميم صياغة التصميم تلقائيًا في إحدى هذه اللغات. تقوم تقنيات التحقق عادةً بالموازنة بين أتمتة التحليل وقوة التعبير في لغة المواصفات. تجمع الأساليب الحديثة بين *فحص النماذج* و*إثبات النظريات* من أجل معالجة التحقق من الأنظمة ذات الحالات اللانهائية بمستوى كافٍ من الأتمتة.

جانب آخر مهم من عملية التطوير هو صحة *المتطلبات*. في كثير من الأحيان، تحدث الأخطاء في المراحل المتأخرة بسبب بعض العيوب في مواصفات المتطلبات. يصعب اكتشافها ولها تأثير كبير على تكلفة إصلاح الخطأ. ومع ذلك، فإن الأساليب الرسمية للتحقق من صحة المتطلبات ليست ناضجة بعد. على وجه الخصوص، لا يوجد تعريف دقيق للمتطلبات الصحيحة.

تم اقتراح الحل الأكثر أهمية في سياق *النهج القائم على الخصائص* للتصميم، حيث تبدأ عملية التطوير من إدراج مجموعة من الخصائص الرسمية، بدلاً من تحديد نموذج على مستوى تجريدي. يتم إجراء التحقق من صحة المتطلبات من خلال سلسلة من الفحوصات التي تحسن الثقة في صحة المتطلبات. تتكون هذه الفحوصات من التحقق من أن المتطلبات لا تحتوي على تناقضات وأنها ليست صارمة للغاية بحيث تمنع السلوكيات المرغوبة، ولا ضعيفة جدًا بحيث تسمح بالسلوكيات غير المرغوبة. تعتمد هذه العملية على توافر منطق تعبيري كافٍ بحيث يمكن صياغة الخصائص بالإضافة إلى السلوكيات المرغوبة وغير المرغوبة في صيغ. يعتبر النهج تطابقًا واحدًا لواحد بين الخصائص والصيغ المنطقية. يتيح ذلك إمكانية تتبع الصياغة الرسمية ونتائج التحقق من الصحة، والأساليب التدريجية والنمطية للتحقق من الصحة.

في سياق التطبيقات الحرجة من حيث السلامة، لا يزال اختيار اللغة المستخدمة لصياغة المتطلبات رسميًا مسألة مفتوحة، تتطلب توازنًا دقيقًا بين قوة التعبير وقابلية القرار وتعقيد الاستدلال. تكمن الصعوبة في إيجاد مقايضة مناسبة في حقيقة أن متطلبات العديد من التطبيقات الواقعية تتضمن عدة أبعاد. من جانب، قد يكون للكائنات التي لها دور نشط في التطبيق المستهدف بنية معقدة وعلاقات متبادلة، قد يتطلب نمذجتها استخدام أنواع بيانات غنية. من الجانب الآخر، يجب استكمال القيود الثابتة على سماتها بقيود على تطورها الزمني.

أحد العوائق الرئيسية في تطبيق هذا النهج على المستوى الصناعي هو أن المتطلبات غالبًا ما تُكتب بلغة طبيعية بحيث تكون المعرفة بالمجال ضرورية لصياغتها رسميًا ولتحديد السلوكيات المرغوبة وأيها ليست كذلك أثناء عملية التحقق من الصحة. نظرًا لأن خبراء المجال عادةً ليسوا مستخدمين متقدمين للأساليب الرسمية، يجب تزويدهم بلغة غنية ولكن سهلة الاستخدام للمواصفات الرسمية ومحرك تلقائي ولكن قابل للتوسع للتحقق الرسمي.

في هذا البحث، نقدم تقريرًا عن منهجية وسلسلة من التقنيات التي طورناها للصياغة الرسمية والتحقق من صحة المتطلبات عالية المستوى للتطبيقات الحرجة من حيث السلامة. تعتمد المنهجية على نهج ثلاثي المراحل ينتقل من التحليل غير الرسمي للمتطلبات، إلى صياغتها الرسمية والتحقق من صحتها [CRST08a]. تعتمد المنهجية على مكونين رئيسيين: لغة رسمية شديدة التعبير وإجراءات إرضاء تلقائية. تجمع اللغة بين منطق الدرجة الأولى والمنطق الزمني والمنطق الهجين [CRST08b، CRST09، CRT09]. تستند إجراءات الإرضاء إلى فحص النماذج ونظرية الإرضاء بالقياس. طبقنا هذه التكنولوجيا ضمن مشروع صناعي للتحقق من صحة متطلبات السكك الحديدية. تدمج الأداة [CCM+09]، ضمن بيئة تجارية، تقنيات لإدارة المتطلبات والتصميم القائم على النماذج، وتقنيات متقدمة للتحقق الرسمي باستخدام مدقق النماذج NuSMV [CCGR00].

يتم تنظيم باقي البحث على النحو التالي: في القسم 2، نوجز المنهجية المقترحة، مع تقديم تفاصيل عن اللغة المختارة في القسم 2.1 وعن إجراء التحقق من الصحة في القسم 2.2؛ في القسم 3، نصف المشروع الذي تم تطبيق المنهجية فيه؛ في القسم 4، نراجع الأعمال ذات الصلة، وفي القسم 5، نختتم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** formal methods (الأساليب الرسمية), model checking (فحص النماذج), theorem proving (إثبات النظريات), property-based approach (النهج القائم على الخصائص), traceability (إمكانية التتبع), decidability (قابلية القرار), satisfiability modulo theory (نظرية الإرضاء بالقياس), NuSMV
- **Equations:** 0
- **Citations:** 7 references cited (CRST08a, CRST08b, CRST09, CRT09, CCM+09, CCGR00)
- **Special handling:** Italics used for emphasis on key terms

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
