# Section 2: Motivation
## القسم 2: الدافع

**Section:** motivation
**Translation Quality:** 0.87
**Glossary Terms Used:** software integration (تكامل البرمجيات), Model Based Systems Engineering (MBSE) (الهندسة النظامية القائمة على النماذج), formal methods (الأساليب الرسمية), formal modeling (النمذجة الرسمية), avionics (إلكترونيات الطيران)

---

### English Version

**Software Integration Cost**

Software integration is a major cost driver in avionics development. Integration problems often go undetected until late in the development process, when the impact to cost and schedule to fix such issues is much higher (as shown in Figure 1).

**Limitations of Current Approaches**

A variety of efforts in recent years have leveraged Model Based Systems Engineering (MBSE) to reduce the risk of software integration, such as Future Airborne Capability Environment (FACE) [16]. These efforts have garnered industry momentum toward modeling as a key element of systems engineering. However, system faults associated with the underspecified behavior of integrated components remain problematic. For example, in 1999 the Mars Polar Lander is believed to have crashed because of unspecified behavior of Hall Effect sensors on its landing legs [18]. The behavior was known to the landing leg engineers, but was not communicated to the software engineers. Integrated system behavior can also manifest in more subtle errors, such as timing errors in software integration due to inconsistent communication paradigm assumptions in software components found in a recent U.S. Army Study [8].

Formal modeling of component behavior has potential to address these issues. Formal modeling of the Mars Polar Lander landing legs could have communicated the legs behavior and enabled automated detection of integration errors in the interaction between the landing legs and software. Formal analysis can uncover unlikely system configurations that may be difficult to evaluate using conventional testing methods. However, there are two significant factors that complicate application of formal methods that must be addressed before formal methods can be viable in avionics systems engineering workflows. First, formal methods are outside of the expertise of many systems engineers. Although training can bridge this gap, tools and methodologies that reduce the effort required to employ formal methods could provide a low-cost-high-return alternative to extensive training. Second, current applications of formal methods analysis are not geared toward integration of components from different organizations or teams.

**Contributions of this Paper**

The objective of this SLICED project is to make formal methods capabilities accessible to systems engineers by leveraging existing formal methods tools, MBSE environments, and models. This paper describes how SLICED addresses two core limitations of the state of art using a compositional approach to formulating formal methods specifications in terms of standardized component architypes and a methodology for generating formal specifications and assertions from conventional engineering models. This paper also explores methods for creating formal assertions to check both for potential error conditions and to generate plans for error recovery. This paper describes a case study demonstrating a novel approach translating a Simulink model to modularized NuSMV state machine specifications. This paper uses the NASA Virtual ADAPT model for evaluation. The overall architecture for ADAPT and the elements implemented in Virtual ADAPT are shown in Figure 2 from [21].

Our approach in SLICED is based on the Architecture-Centric Virtual Integration Process (ACVIP). ACVIP provides early detection of integration errors through model integration [9]. Our first automated implementation of the SLICED methodology was based on AADL, which provides a lexicon for clearly and consistently describing embedded software components [1]. The most common language for ACVIP modeling is AADL, which is an embedded computing systems modeling language. Although the approach described in this paper does not use AADL directly (ADAPT is provided by NASA in Simulink, not AADL), the component prototypes used to establish interface boundaries in ADAPT (e.g., battery and relay) are defined with intent and granularity informed by types in AADL (e.g., thread and bus). Simulink models provide a test platform for simulation-based evaluation. SLICED takes a Simulink model, abstracts the inner complexity of its components, creates an FSM, and evaluates that FSM to generate scenarios for evaluation via simulation.

---

### النسخة العربية

**تكلفة تكامل البرمجيات**

يعد تكامل البرمجيات محركاً رئيسياً للتكلفة في تطوير إلكترونيات الطيران. غالباً ما تمر مشاكل التكامل دون اكتشاف حتى وقت متأخر من عملية التطوير، عندما يكون التأثير على التكلفة والجدول الزمني لإصلاح هذه المشاكل أعلى بكثير (كما هو موضح في الشكل 1).

**قيود الأساليب الحالية**

استفادت مجموعة متنوعة من الجهود في السنوات الأخيرة من الهندسة النظامية القائمة على النماذج (MBSE) لتقليل مخاطر تكامل البرمجيات، مثل بيئة القدرة الجوية المستقبلية (FACE) [16]. حققت هذه الجهود زخماً صناعياً نحو النمذجة كعنصر رئيسي في هندسة الأنظمة. ومع ذلك، تظل أعطال الأنظمة المرتبطة بالسلوك غير المحدد بشكل كافٍ للمكونات المتكاملة إشكالية. على سبيل المثال، يُعتقد أن مسبار المريخ القطبي (Mars Polar Lander) قد تحطم في عام 1999 بسبب سلوك غير محدد لمستشعرات Hall Effect على أرجل الهبوط الخاصة به [18]. كان السلوك معروفاً لمهندسي أرجل الهبوط، ولكن لم يتم إبلاغه لمهندسي البرمجيات. يمكن أن يظهر سلوك الأنظمة المتكاملة أيضاً في أخطاء أكثر دقة، مثل أخطاء التوقيت في تكامل البرمجيات بسبب افتراضات نموذج الاتصال غير المتسقة في مكونات البرمجيات الموجودة في دراسة حديثة للجيش الأمريكي [8].

لدى النمذجة الرسمية لسلوك المكونات القدرة على معالجة هذه المشكلات. كان من الممكن أن تقوم النمذجة الرسمية لأرجل الهبوط في مسبار المريخ القطبي بإبلاغ سلوك الأرجل وتمكين الكشف الآلي عن أخطاء التكامل في التفاعل بين أرجل الهبوط والبرمجيات. يمكن للتحليل الرسمي الكشف عن تكوينات نظام غير محتملة قد يكون من الصعب تقييمها باستخدام طرق الاختبار التقليدية. ومع ذلك، هناك عاملان مهمان يعقدان تطبيق الأساليب الرسمية ويجب معالجتهما قبل أن تكون الأساليب الرسمية قابلة للتطبيق في سير عمل هندسة أنظمة إلكترونيات الطيران. أولاً، الأساليب الرسمية خارج خبرة العديد من مهندسي الأنظمة. على الرغم من أن التدريب يمكن أن يسد هذه الفجوة، فإن الأدوات والمنهجيات التي تقلل من الجهد المطلوب لتوظيف الأساليب الرسمية يمكن أن توفر بديلاً منخفض التكلفة وعالي العائد للتدريب الشامل. ثانياً، التطبيقات الحالية لتحليل الأساليب الرسمية ليست موجهة نحو تكامل المكونات من منظمات أو فرق مختلفة.

**مساهمات هذه الورقة**

هدف مشروع SLICED هو جعل قدرات الأساليب الرسمية متاحة لمهندسي الأنظمة من خلال الاستفادة من أدوات الأساليب الرسمية الموجودة، وبيئات MBSE، والنماذج. تصف هذه الورقة كيف تعالج SLICED قيدين أساسيين لحالة الفن باستخدام نهج تركيبي لصياغة مواصفات الأساليب الرسمية من حيث الأنماط الأساسية للمكونات الموحدة ومنهجية لتوليد المواصفات الرسمية والتأكيدات من نماذج الهندسة التقليدية. تستكشف هذه الورقة أيضاً طرق إنشاء التأكيدات الرسمية للتحقق من كل من حالات الخطأ المحتملة ولتوليد خطط للتعافي من الأخطاء. تصف هذه الورقة دراسة حالة توضح نهجاً جديداً لترجمة نموذج Simulink إلى مواصفات آلة حالة NuSMV معيارية. تستخدم هذه الورقة نموذج Virtual ADAPT من ناسا للتقييم. المعمارية العامة لـ ADAPT والعناصر المنفذة في Virtual ADAPT موضحة في الشكل 2 من [21].

يعتمد نهجنا في SLICED على عملية التكامل الافتراضي المتمحورة حول المعمارية (ACVIP). توفر ACVIP الكشف المبكر عن أخطاء التكامل من خلال تكامل النموذج [9]. كان أول تنفيذ تلقائي لمنهجية SLICED مبنياً على AADL، التي توفر معجماً لوصف مكونات البرمجيات المدمجة بوضوح واتساق [1]. اللغة الأكثر شيوعاً لنمذجة ACVIP هي AADL، وهي لغة نمذجة أنظمة الحوسبة المدمجة. على الرغم من أن النهج الموصوف في هذه الورقة لا يستخدم AADL مباشرة (يتم توفير ADAPT من قبل ناسا في Simulink، وليس AADL)، فإن نماذج المكونات الأولية المستخدمة لتحديد حدود الواجهة في ADAPT (على سبيل المثال، البطارية والمرحل) محددة بنية وتفصيل مستنير من الأنواع في AADL (على سبيل المثال، الخيط والناقل). توفر نماذج Simulink منصة اختبار للتقييم القائم على المحاكاة. تأخذ SLICED نموذج Simulink، وتجرد التعقيد الداخلي لمكوناته، وتنشئ آلة حالة محدودة، وتقيم تلك الآلة لتوليد سيناريوهات للتقييم عبر المحاكاة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (cost diagram), Figure 2 (ADAPT components)
- **Key terms introduced:**
  - Software integration - تكامل البرمجيات
  - Avionics development - تطوير إلكترونيات الطيران
  - Model Based Systems Engineering (MBSE) - الهندسة النظامية القائمة على النماذج
  - FACE (Future Airborne Capability Environment) - بيئة القدرة الجوية المستقبلية
  - Hall Effect sensors - مستشعرات Hall Effect
  - Mars Polar Lander - مسبار المريخ القطبي
  - Compositional approach - نهج تركيبي
  - Component archetypes - الأنماط الأساسية للمكونات
  - Error recovery - التعافي من الأخطاء
  - ACVIP (Architecture-Centric Virtual Integration Process) - عملية التكامل الافتراضي المتمحورة حول المعمارية
- **Equations:** 0
- **Citations:** [1], [8], [9], [16], [18], [21]
- **Special handling:**
  - Figure 1 is a cost diagram showing defect introduction and detection phases
  - Figure 2 shows ADAPT architecture with components

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
