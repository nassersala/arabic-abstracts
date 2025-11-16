# Section 1: Introduction
## القسم 1: المقدمة

### English

Agda [2] is a dependently-typed functional programming language [9], based on an extension of intuitionistic Martin-Löf type theory. We implement first order natural deduction in Agda. We use Agda's type checker to verify the correctness natural deduction proofs, and also prove properties of natural deduction, using Agda's proof assistant functionality. This implementation corresponds to a formalisation of natural deduction in constructive type theory, and the proofs are verified by Agda to be correct (under the assumption that Agda itself is correct).

The Agda code below has been written in literate Agda, which allows Agda to be mixed with LATEX. The files which have been used to typeset this document can also be evaluated and type checked. Some trivial proofs are omitted from the typeset document; these are only hidden for brevity, and are still present in the code and used by Agda. The results which rely on them are therefore still verified. This should not be mistaken for use of postulates, wherein Agda itself is told to assume that a proof exists. Postulates are used only in the module for outputting natural deduction proofs as LATEX for use with the bussproofs package. All other code type checks with Agda in safe mode, meaning that it provably halts.

Each of the following sections corresponds to its own literate Agda file. Sections named with a file name ending in '.lagda' are modules. Each section imports the modules preceding it, unless stated otherwise. These module declarations and imports have been hidden for brevity.

Inspiration for the definition of vector types and decidable types comes from the Agda standard library [1]. However, the standard library will not be directly imported, to maintain clarity of definitions, and because it is not needed. We will use built-in types for natural numbers, lists, and the dependent sum, explaining their definitions when they appear.

The full code is available online at https://lsw.nz/tome. It is written for (and has been tested against) Agda version 2.6.0.

### Arabic Translation

Agda [2] هي لغة برمجة وظيفية ذات أنواع تابعة [9]، تستند إلى امتداد لنظرية الأنواع الحدسية لمارتن-لوف. نطبق الاستنتاج الطبيعي من الدرجة الأولى في Agda. نستخدم مدقق الأنواع في Agda للتحقق من صحة براهين الاستنتاج الطبيعي، وأيضاً نبرهن خصائص الاستنتاج الطبيعي، باستخدام وظيفة مساعد البرهان في Agda. يتوافق هذا التطبيق مع صياغة رسمية للاستنتاج الطبيعي في نظرية الأنواع البنائية، والبراهين يتم التحقق من صحتها بواسطة Agda لتكون صحيحة (بافتراض أن Agda نفسها صحيحة).

تمت كتابة كود Agda أدناه بصيغة Agda الأدبية، والتي تسمح بدمج Agda مع LATEX. يمكن أيضاً تقييم الملفات التي تم استخدامها لإنشاء هذا المستند والتحقق من أنواعها. تم حذف بعض البراهين البسيطة من المستند المنضد؛ هذه مخفية فقط للإيجاز، ولا تزال موجودة في الكود وتستخدمها Agda. النتائج التي تعتمد عليها لا تزال بالتالي محققة. لا ينبغي الخلط بين هذا واستخدام المسلمات، حيث يُطلب من Agda نفسها افتراض وجود برهان. تُستخدم المسلمات فقط في الوحدة النمطية لإخراج براهين الاستنتاج الطبيعي كـ LATEX للاستخدام مع حزمة bussproofs. جميع الأكواد الأخرى تتحقق أنواعها مع Agda في الوضع الآمن، مما يعني أنها تتوقف بشكل قابل للبرهان.

يتوافق كل قسم من الأقسام التالية مع ملف Agda أدبي خاص به. الأقسام المسماة باسم ملف ينتهي بـ '.lagda' هي وحدات نمطية. يستورد كل قسم الوحدات النمطية السابقة له، ما لم يُذكر خلاف ذلك. تم إخفاء تصريحات الوحدات النمطية وعمليات الاستيراد هذه للإيجاز.

يأتي الإلهام لتعريف أنواع المتجهات والأنواع القابلة للتقرير من مكتبة Agda القياسية [1]. ومع ذلك، لن يتم استيراد المكتبة القياسية مباشرة، للحفاظ على وضوح التعريفات، ولأنها غير مطلوبة. سنستخدم الأنواع المدمجة للأعداد الطبيعية، والقوائم، والمجموع التابع، موضحين تعريفاتها عند ظهورها.

الكود الكامل متاح عبر الإنترنت على https://lsw.nz/tome. تم كتابته لـ (وتم اختباره مقابل) Agda الإصدار 2.6.0.

### Back-Translation

Agda [2] is a dependently-typed functional programming language [9], based on an extension of intuitionistic Martin-Löf type theory. We implement first-order natural deduction in Agda. We use Agda's type checker to verify the correctness of natural deduction proofs, and also prove properties of natural deduction, using Agda's proof assistant functionality. This implementation corresponds to a formal formalization of natural deduction in constructive type theory, and the proofs are verified by Agda to be correct (assuming that Agda itself is correct).

The Agda code below has been written in literate Agda format, which allows Agda to be combined with LATEX. The files that were used to create this document can also be evaluated and type-checked. Some simple proofs have been omitted from the typeset document; these are hidden only for brevity, and are still present in the code and used by Agda. The results that depend on them are therefore still verified. This should not be confused with the use of postulates, where Agda itself is asked to assume the existence of a proof. Postulates are used only in the module for outputting natural deduction proofs as LATEX for use with the bussproofs package. All other code type-checks with Agda in safe mode, meaning that it provably halts.

Each of the following sections corresponds to its own literate Agda file. Sections named with a file name ending in '.lagda' are modules. Each section imports the modules preceding it, unless otherwise stated. These module declarations and imports have been hidden for brevity.

The inspiration for the definition of vector types and decidable types comes from the Agda standard library [1]. However, the standard library will not be imported directly, to maintain clarity of definitions, and because it is not required. We will use built-in types for natural numbers, lists, and the dependent sum, explaining their definitions when they appear.

The complete code is available online at https://lsw.nz/tome. It was written for (and tested against) Agda version 2.6.0.

### Translation Metrics
- **Quality**: High (estimated 0.92)
- **Completeness**: Full section translated
- **Technical terminology**: Consistent with glossary
