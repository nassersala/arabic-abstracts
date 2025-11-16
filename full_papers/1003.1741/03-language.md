# Section 2.1: A Property Specification Language for Safety-Critical Applications
## القسم 2.1: لغة مواصفات الخصائص للتطبيقات الحرجة من حيث السلامة

**Section:** language specification
**Translation Quality:** 0.87
**Glossary Terms Used:** first-order logic (منطق الدرجة الأولى), temporal logic (المنطق الزمني), hybrid logic (المنطق الهجين), model checking (فحص النماذج), class diagram (مخطط الفئات)

---

### English Version

The success of the methodology relies on the availability of a specification language which is enough expressive to represent the requirements of safety-critical applications, and enough simple to be used by domain experts and analyzed with automatic techniques.

In order to specify requirements in the context of safety-critical applications we adopt a fragment of first-order temporal logic. The first-order component allows to specify constraints on objects, their relationships, and their attributes, which typically have rich data types. The temporal component allows to specify constraints on the temporal evolution of the possible configurations. We enriched the logic with constructs able to specify hybrid aspects of the objects' attributes such as derivatives of the continuous variables and instantaneous changes of the discrete variables. The logical formulas are consequently interpreted over hybrid traces where continuous evolutions alternate with discrete changes. Finally, the logic has been designed in order to be suitable for an automatic analysis with model checking techniques.

As described in [CRST09], we use a class diagram to define the classes of objects specified by the requirements, their relationships and their attributes. The class diagram basically defines the signature of the first-order temporal logic. The functional symbols that represent the attributes and the relationships of the objects are flexible in the sense that their interpretation change at different time points. Quantifiers are allowed to range over the objects of a class, and can be intermixed with the temporal operators.

The basic atoms of the logic are arithmetic predicates of the attributes and relationships of objects. As described in [CRT09], the "next" operator can be used to refer to the value of a variable after a discrete change, while the "der" operator can be used to refer to the first derivative of continuous variables during a continuous evolution.

The temporal structure of the logic encompasses the classical linear-time temporal operators combined with regular expressions. This combination is well established in the context of digital circuits and forms the core of standard languages such as the Property Specification Language (PSL) [EF06].

On the lines of PSL, we also provide a number of syntactic sugar which increases the usability of the language by the domain experts. This includes natural language expressions that substitute the temporal operators, the quantifiers, and most of the mathematical symbols.

---

### النسخة العربية

يعتمد نجاح المنهجية على توافر لغة مواصفات تعبيرية بما يكفي لتمثيل متطلبات التطبيقات الحرجة من حيث السلامة، وبسيطة بما يكفي لاستخدامها من قبل خبراء المجال وتحليلها باستخدام التقنيات التلقائية.

من أجل تحديد المتطلبات في سياق التطبيقات الحرجة من حيث السلامة، نعتمد جزءًا من منطق الدرجة الأولى الزمني. يسمح مكون الدرجة الأولى بتحديد القيود على الكائنات وعلاقاتها وسماتها، التي عادة ما تحتوي على أنواع بيانات غنية. يسمح المكون الزمني بتحديد القيود على التطور الزمني للتكوينات الممكنة. أثرينا المنطق ببنى قادرة على تحديد الجوانب الهجينة لسمات الكائنات مثل مشتقات المتغيرات المستمرة والتغييرات اللحظية للمتغيرات المنفصلة. وبالتالي، يتم تفسير الصيغ المنطقية على تتبعات هجينة حيث تتناوب التطورات المستمرة مع التغييرات المنفصلة. أخيرًا، تم تصميم المنطق ليكون مناسبًا للتحليل التلقائي باستخدام تقنيات فحص النماذج.

كما هو موضح في [CRST09]، نستخدم مخطط فئات لتحديد فئات الكائنات المحددة بالمتطلبات وعلاقاتها وسماتها. يحدد مخطط الفئات بشكل أساسي توقيع منطق الدرجة الأولى الزمني. الرموز الوظيفية التي تمثل سمات وعلاقات الكائنات مرنة بمعنى أن تفسيرها يتغير في نقاط زمنية مختلفة. يُسمح للمحددات الكمية بالتراوح على كائنات فئة، ويمكن مزجها مع العوامل الزمنية.

الذرات الأساسية للمنطق هي محمولات حسابية لسمات وعلاقات الكائنات. كما هو موضح في [CRT09]، يمكن استخدام عامل "next" (التالي) للإشارة إلى قيمة متغير بعد تغيير منفصل، بينما يمكن استخدام عامل "der" (المشتق) للإشارة إلى المشتق الأول للمتغيرات المستمرة أثناء التطور المستمر.

تشمل البنية الزمنية للمنطق عوامل المنطق الزمني الخطي الكلاسيكية المدمجة مع التعابير النظامية. هذا المزيج راسخ في سياق الدوائر الرقمية ويشكل جوهر اللغات القياسية مثل لغة مواصفات الخصائص (PSL) [EF06].

على غرار PSL، نوفر أيضًا عددًا من التحسينات النحوية التي تزيد من سهولة استخدام اللغة من قبل خبراء المجال. يتضمن ذلك تعبيرات اللغة الطبيعية التي تحل محل العوامل الزمنية والمحددات الكمية ومعظم الرموز الرياضية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** first-order temporal logic (منطق الدرجة الأولى الزمني), class diagram (مخطط الفئات), hybrid traces (تتبعات هجينة), quantifiers (المحددات الكمية), temporal operators (العوامل الزمنية), regular expressions (التعابير النظامية), Property Specification Language/PSL (لغة مواصفات الخصائص), syntactic sugar (التحسينات النحوية), next operator (عامل التالي), der operator (عامل المشتق)
- **Equations:** 0
- **Citations:** 3 references (CRST09, CRT09, EF06)
- **Special handling:** Technical operators "next" and "der" kept in English with Arabic explanation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
