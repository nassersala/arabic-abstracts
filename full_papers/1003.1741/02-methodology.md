# Section 2: A Methodology for the Formalization and Validation of Requirements
## القسم 2: منهجية للصياغة الرسمية والتحقق من صحة المتطلبات

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** validation (التحقق من الصحة), formalization (الصياغة الرسمية), consistency (الاتساق), traceability (إمكانية التتبع), model checking (فحص النماذج)

---

### English Version

Our methodology has been presented in [CRST08a]. It consists of three main steps:

• **Informal analysis.** The first activity in the methodology is the informal analysis of the set of requirements. In this phase, first the requirement fragments are identified and categorized on the basis of their characteristics. Then, they are structured according to their dependencies.

• **Formalization.** The second phase consists of the formalization of each categorized requirement fragment identified in the informal analysis by specifying the corresponding formal counterpart. The link between informal and formal is used for requirements traceability of the formalization against the informal textual requirements, and to select directly from the textual requirements document a categorized requirement fragment to validate.

• **Formal validation.** The third phase aims at improving the quality of the requirements and increasing the confidence that the categorized requirement fragment and its corresponding formalized counterpart meet the design intent. It consists of the definition of a series of validation problems and the analysis of the results given by an automatic validation check. The problems include three main types of checks; namely, checking logical consistency, scenario compatibility, and property entailment:

  – **Logical consistency** to formally verify the absence of logical contradictions in the considered formalized requirement fragments. It is indeed possible that two formalized requirement fragments mandate mutually incompatible behaviors. Note that this check does not require any domain knowledge.

  – **Scenario compatibility** to verify whether a scenario is admitted given the constraints imposed by the considered formalized requirement fragments. Intuitively, the check for scenario compatibility can be seen as a form of simulation guided by a set of constraints. The check for scenario compatibility can be reduced to the problem of checking the consistency of the set of considered formalized requirement fragments with the constraint describing the scenario.

  – **Property entailment** to verify whether an expected property is implied by the considered formalized requirement fragments. This check is similar in spirit to model checking, where a property is checked against a model. Here the considered set of formalized requirement fragment plays the role of the model against which the property must be verified. Property checking can be reduced to the problem of checking the consistency of the considered formalized requirement fragments with the negation of the property.

If one of the check reveals a problem, two causes are possible: the first one is that the formalization is not correct due to an improper use of the formal language or to an ambiguity of the informal specification; the second possibility is that there is a flaw in the informal specification that needs to be corrected. An inspection of the diagnostic information can be carried out in order to discriminate among the two possibilities in order to take the most appropriate corrective action.

In fact, the above checks not only produce a yes/no answer, but they can also provide the domain expert with diagnostic information, mainly in the form of:

  – **Traces.** When consistency and scenario checking succeeds, it is possible to produce a trace witnessing the consistency, i.e. satisfying all the constraints in the considered formalized requirement fragments. Similarly, when a property check fails the tool provides a trace witnessing the violation of the property by the formalized requirement fragments.

  – **Unsatisfiable core.** If the specification is inconsistent or the scenario is incompatible, no behavior can be associated to the considered formalized requirement fragments; in these cases, the tool can also generate diagnostic information in the form of a minimal inconsistent subset. This information can be given to the domain expert, to support the identification and the fix of the flaw.

---

### النسخة العربية

تم عرض منهجيتنا في [CRST08a]. تتكون من ثلاث خطوات رئيسية:

• **التحليل غير الرسمي.** النشاط الأول في المنهجية هو التحليل غير الرسمي لمجموعة المتطلبات. في هذه المرحلة، يتم أولاً تحديد أجزاء المتطلبات وتصنيفها على أساس خصائصها. ثم يتم هيكلتها وفقًا لتبعياتها.

• **الصياغة الرسمية.** تتكون المرحلة الثانية من الصياغة الرسمية لكل جزء متطلبات مصنف تم تحديده في التحليل غير الرسمي من خلال تحديد النظير الرسمي المقابل. يُستخدم الرابط بين غير الرسمي والرسمي لإمكانية تتبع المتطلبات للصياغة الرسمية مقابل المتطلبات النصية غير الرسمية، ولاختيار جزء متطلبات مصنف مباشرة من وثيقة المتطلبات النصية للتحقق من صحته.

• **التحقق الرسمي من الصحة.** تهدف المرحلة الثالثة إلى تحسين جودة المتطلبات وزيادة الثقة في أن جزء المتطلبات المصنف ونظيره الرسمي المقابل يفيان بقصد التصميم. وتتكون من تعريف سلسلة من مشاكل التحقق من الصحة وتحليل النتائج المقدمة من فحص التحقق من الصحة التلقائي. تتضمن المشاكل ثلاثة أنواع رئيسية من الفحوصات؛ وهي فحص الاتساق المنطقي، وتوافق السيناريو، واستلزام الخاصية:

  – **الاتساق المنطقي** للتحقق رسميًا من عدم وجود تناقضات منطقية في أجزاء المتطلبات الرسمية المعتبرة. من الممكن بالفعل أن يفرض جزءان من أجزاء المتطلبات الرسمية سلوكيات غير متوافقة بشكل متبادل. لاحظ أن هذا الفحص لا يتطلب أي معرفة بالمجال.

  – **توافق السيناريو** للتحقق مما إذا كان السيناريو مقبولاً في ظل القيود المفروضة من أجزاء المتطلبات الرسمية المعتبرة. بشكل حدسي، يمكن النظر إلى فحص توافق السيناريو على أنه شكل من أشكال المحاكاة الموجهة بمجموعة من القيود. يمكن تقليص فحص توافق السيناريو إلى مشكلة فحص اتساق مجموعة أجزاء المتطلبات الرسمية المعتبرة مع القيد الذي يصف السيناريو.

  – **استلزام الخاصية** للتحقق مما إذا كانت خاصية متوقعة مستلزمة من أجزاء المتطلبات الرسمية المعتبرة. هذا الفحص مشابه في الروح لفحص النماذج، حيث يتم فحص خاصية مقابل نموذج. هنا تلعب مجموعة أجزاء المتطلبات الرسمية المعتبرة دور النموذج الذي يجب التحقق من الخاصية مقابله. يمكن تقليص فحص الخاصية إلى مشكلة فحص اتساق أجزاء المتطلبات الرسمية المعتبرة مع نفي الخاصية.

إذا كشف أحد الفحوصات عن مشكلة، فهناك سببان محتملان: الأول هو أن الصياغة الرسمية غير صحيحة بسبب استخدام غير صحيح للغة الرسمية أو بسبب غموض في المواصفات غير الرسمية؛ والاحتمال الثاني هو أن هناك عيبًا في المواصفات غير الرسمية يحتاج إلى التصحيح. يمكن إجراء فحص للمعلومات التشخيصية من أجل التمييز بين الاحتمالين من أجل اتخاذ الإجراء التصحيحي الأنسب.

في الواقع، لا تنتج الفحوصات أعلاه إجابة نعم/لا فقط، ولكن يمكنها أيضًا تزويد خبير المجال بمعلومات تشخيصية، بشكل رئيسي في شكل:

  – **التتبعات.** عندما ينجح فحص الاتساق والسيناريو، من الممكن إنتاج تتبع يشهد على الاتساق، أي يرضي جميع القيود في أجزاء المتطلبات الرسمية المعتبرة. وبالمثل، عندما يفشل فحص الخاصية، توفر الأداة تتبعًا يشهد على انتهاك الخاصية من قبل أجزاء المتطلبات الرسمية.

  – **النواة غير القابلة للإرضاء.** إذا كانت المواصفات غير متسقة أو كان السيناريو غير متوافق، فلا يمكن ربط أي سلوك بأجزاء المتطلبات الرسمية المعتبرة؛ في هذه الحالات، يمكن للأداة أيضًا توليد معلومات تشخيصية في شكل مجموعة فرعية غير متسقة دنيا. يمكن إعطاء هذه المعلومات لخبير المجال، لدعم تحديد وإصلاح العيب.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** informal analysis (التحليل غير الرسمي), formalization (الصياغة الرسمية), formal validation (التحقق الرسمي من الصحة), logical consistency (الاتساق المنطقي), scenario compatibility (توافق السيناريو), property entailment (استلزام الخاصية), traces (التتبعات), unsatisfiable core (النواة غير القابلة للإرضاء)
- **Equations:** 0
- **Citations:** 1 reference (CRST08a)
- **Special handling:** Bulleted list structure preserved, sub-items with dashes maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
