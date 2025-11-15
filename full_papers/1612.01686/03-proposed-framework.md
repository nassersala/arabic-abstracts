# Section 3: Proposed Framework
## القسم 3: إطار العمل المقترح

**Section:** proposed-framework
**Translation Quality:** 0.86
**Glossary Terms Used:** API, framework, specification, state transitions, discrete time, category theory, formal methods, ScalaCheck, Scala

---

### English Version

Figure 1 depicts the proposed model that will allow for combining formal methods with property-based-testing. The first row (API calls) represents the actual system under test. The second row represents the world in which the specification formulas lives. The time between subsequent API calls is modelled through a function of discreet time. Time functions are mapped to the corresponding state transitions between states. The general idea is to start with specifying the system using human-oriented modelling techniques founded on formal methods. Then, to develop system software according to the specifications. Finally, to run the test suite to verify that the system runs according to the specification. If a test fails, it will be the judgment of the engineer to decide whether the errors were in the system software or in the specification formulas for which the system was not correctly specified.

**Figure 1. Proposed Framework**

[Figure shows three rows:
- Row 1: API calls → API Calls → API Calls → API Calls (with "discreet time" label)
- Row 2: State Model → State Model → State Model → State Model (with "Formal methods" label)
- Row 3: Result → Result → Result → Result (with "state transitions" label)]

The implementation language of choice is Scala programming language. It was selected for many reasons. First of all, it is one of the most popular languages on the Java virtual machine. The ecosystem will make it possible to find quick answers for questions that are related to technical aspects. Secondly, BeSpaceD is implemented in Scala. This will lower the impedance mismatch between research model and BeSpaceD. Finally, Scala, is a functional language. This will make working with the concepts of property based testing more natural and simple.

For the property-based testing, we are going to apply the ScalaCheck library. However, since the research will investigate the substitution of the simplistic state machine in ScalaCheck with formal methods, the use of this library might be limited.

To relate the different modeling and abstraction layers to each other in the proposed framework, we are using category theory. Category theory helps in illuminating the relations of many aspects of the proposed ingredients that would be unseen otherwise. Figure 1 relates the human actions (API call), system states (state model) and results to each other. Our formal methods-based techniques will only be applied to the State-model level. This will help to stair the direction of future investigation of the proposed model.

---

### النسخة العربية

يوضح الشكل 1 النموذج المقترح الذي سيسمح بالجمع بين الأساليب الرسمية والاختبار القائم على الخصائص. يمثل الصف الأول (استدعاءات واجهة برمجة التطبيقات) النظام الفعلي قيد الاختبار. يمثل الصف الثاني العالم الذي تعيش فيه صيغ المواصفات. يتم نمذجة الوقت بين استدعاءات واجهة برمجة التطبيقات المتتالية من خلال دالة الزمن المنفصل. يتم ربط دوال الزمن بانتقالات الحالة المقابلة بين الحالات. الفكرة العامة هي البدء بتحديد مواصفات النظام باستخدام تقنيات النمذجة الموجهة نحو الإنسان والمبنية على الأساليب الرسمية. ثم تطوير برمجيات النظام وفقاً للمواصفات. أخيراً، تشغيل مجموعة الاختبارات للتحقق من أن النظام يعمل وفقاً للمواصفات. إذا فشل اختبار ما، فسيكون من حكم المهندس أن يقرر ما إذا كانت الأخطاء في برمجيات النظام أو في صيغ المواصفات التي لم يتم تحديد النظام لها بشكل صحيح.

**الشكل 1. إطار العمل المقترح**

[يوضح الشكل ثلاثة صفوف:
- الصف 1: استدعاءات واجهة برمجة التطبيقات → استدعاءات واجهة برمجة التطبيقات → استدعاءات واجهة برمجة التطبيقات → استدعاءات واجهة برمجة التطبيقات (مع تسمية "الزمن المنفصل")
- الصف 2: نموذج الحالة → نموذج الحالة → نموذج الحالة → نموذج الحالة (مع تسمية "الأساليب الرسمية")
- الصف 3: النتيجة → النتيجة → النتيجة → النتيجة (مع تسمية "انتقالات الحالة")]

لغة التنفيذ المختارة هي لغة برمجة Scala. تم اختيارها لأسباب عديدة. أولاً، إنها واحدة من أكثر اللغات شعبية على آلة Java الافتراضية. سيجعل النظام البيئي من الممكن العثور على إجابات سريعة للأسئلة المتعلقة بالجوانب التقنية. ثانياً، تم تنفيذ BeSpaceD في Scala. سيؤدي هذا إلى تقليل عدم التوافق بين نموذج البحث و BeSpaceD. أخيراً، Scala هي لغة وظيفية. سيجعل هذا العمل مع مفاهيم الاختبار القائم على الخصائص أكثر طبيعية وبساطة.

بالنسبة للاختبار القائم على الخصائص، سنطبق مكتبة ScalaCheck. ومع ذلك، نظراً لأن البحث سيبحث في استبدال آلة الحالة البسيطة في ScalaCheck بالأساليب الرسمية، فقد يكون استخدام هذه المكتبة محدوداً.

لربط طبقات النمذجة والتجريد المختلفة ببعضها البعض في إطار العمل المقترح، نستخدم نظرية الفئات. تساعد نظرية الفئات في إضاءة العلاقات بين العديد من جوانب المكونات المقترحة التي قد تكون غير مرئية بخلاف ذلك. يربط الشكل 1 الإجراءات البشرية (استدعاء واجهة برمجة التطبيقات) وحالات النظام (نموذج الحالة) والنتائج ببعضها البعض. ستُطبق تقنياتنا القائمة على الأساليب الرسمية فقط على مستوى نموذج الحالة. سيساعد هذا في توجيه اتجاه البحث المستقبلي للنموذج المقترح.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Proposed Framework diagram)
- **Key terms introduced:** discrete time, state transitions, category theory, ScalaCheck, impedance mismatch
- **Equations:** None
- **Citations:** None in this section
- **Special handling:** Figure description and architectural framework explanation

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
