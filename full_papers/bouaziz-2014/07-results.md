# Section 7: Results
## القسم 7: النتائج

**Section:** Results
**Translation Quality:** 0.87
**Glossary Terms Used:** simulation, solver, constraint, performance, convergence

---

### English Version (Summary)

This section demonstrates the capabilities of the projective implicit Euler solver through various experiments and comparisons.

**7.1 Generality** - The solver handles diverse constraint types within a single framework, demonstrated by complex scenes mixing volumetric strain constraints, edge strain, bending constraints, and collisions. Examples include cloths, shells, solids, and example-based simulations.

**7.2 Robustness and Simplicity** - The solver remains numerically stable even under extreme forces and degenerate mesh elements. The weakly decreasing energy property eliminates the need for safeguards. The algorithm structure is simple and closely related to PBD, making it easy to extend with new constraints.

**7.3 Accuracy and Performance** - Comparisons show:
- vs. Newton's method: Slower convergence per iteration but 30x faster per iteration computationally, making it superior for interactive applications
- vs. PBD: More accurate and consistent material stiffness independent of iteration count
- Mesh independence: Continuum-based constraints maintain behavior across different resolutions

Timing: Medium-sized models (<30K constraints, <30K DoFs) achieve real-time performance at 1-6ms per iteration with 5-10 iterations sufficient for visual quality.

---

### النسخة العربية

يوضح هذا القسم قدرات حلال أويلر الضمني الإسقاطي من خلال تجارب ومقارنات متنوعة.

**7.1 العمومية**

لا يعتمد حلالنا على أي نوع معين من القيود وقادر على التعامل مع أي مجموعة متنوعة من القيود الهندسية ضمن نفس الإعداد، مما يجعل من الممكن محاكاة مشاهد معقدة باستخدام حلال واحد ومعالجة تفاعلات الأجسام بقوة بطريقة ضمنية. في الشكل 1 نُظهر مثل هذا المشهد المعقد بأنواع قيود مختلفة، حيث يتم أيضاً ربط الأجسام معاً. على سبيل المثال، تُنمذج الشجرة والمنزل بقيود إجهاد حجمية بينما يستخدم خط الغسيل والقماش والعشب والأوراق قيود إجهاد الحافة والانحناء.

**الأقمشة والقشور.** في الشكل 10 نستخدم ببساطة قيود إجهاد الحافة لنمذجة سلوك علم قرصان. تُضاف قوى الرياح كدالة لاتجاه الرياح والعمودي على المثلث. عندما تكون قوى الرياح قوية جداً، يتمزق علم القرصان. يتحقق هذا من خلال إزالة قيود الحافة عندما يتجاوز الإجهاد عتبة معينة. يمكن أيضاً نمذجة أقمشة أكثر تعقيداً يمكن أن تخضع لكميات صغيرة إلى متوسطة من التمدد باستخدام حد على إجهاد المثلث بالاشتراك مع قيود الانحناء.

**الأجسام الصلبة والمحاكاة القائمة على الأمثلة.** نحاكي الأجسام الصلبة باستخدام مزيج من قيود الإجهاد والحجم المطبقة على شبكات رباعية السطوح. كما هو موضح في الشكل 7، يمكن نمذجة أنواع مختلفة من المواد من خلال تغيير الأوزان التي تجمع بين هذه القيود. المحاكاة القائمة على الأمثلة للشبكات الحجمية ممكنة أيضاً في صياغتنا. هذا يسمح بالتحكم الفني في المحاكاة الفيزيائية.

**7.2 القوة والبساطة**

ميزة مهمة واحدة لنهجنا هي الاستقرار الرقمي. في الشكل 10 نُظهر أنه حتى تحت القوى القصوى يبقى حلالنا قوياً. وبالمثل، تبقى طريقتنا موثوقة في الحالات التي تتدهور فيها عناصر الشبكة. المتطلب الوحيد لنهجنا هو أن عناصر الشبكة للنموذج المُدخل تكون جيدة السلوك من أجل حساب تفصيل معاملات التدرج ولابلاس-بيلترامي لمتعدد الشعب الأصلي.

نوضح بساطة نهجنا من خلال عرض إجراء التحسين الخاص بنا في الخوارزمية 1. بإزالة السطر 7 وتغيير $p_i$ إلى $q_{n+1}$ في السطر 5، نكون قادرين على استرداد بنية خوارزمية PBD الأصلية تماماً. علاوة على ذلك، لاحظ أن إدخال قيد جديد يتطلب فقط تعريف إسقاط القيد المستخدم في الحل المحلي وتعريف مقاييس المسافة التربيعية المناسبة (المصفوفات $A_i$ و $B_i$).

**7.3 الدقة والأداء**

**المقارنة مع نيوتن.** في الشكل 12 نقارن أداء حلالنا المحلي/العام مع طريقة نيوتن. كما هو موضح، يتقارب النهج المحلي/العام بشكل أبطأ في عدد التكرارات. هذا منطقي تماماً حيث تُظهر طريقة نيوتن تقارباً تربيعياً بينما الحلالات المحلية/العامة (طرق الهبوط المنسق على الكتل) لها تقارب خطي. ومع ذلك، عند النظر إلى التقارب من حيث الوقت الحسابي، نلاحظ أن نهجنا أسرع من طريقة نيوتن للتطبيقات التفاعلية. لتكرار نيوتن واحد يمكن إجراء حوالي 30 تكراراً محلياً/عاماً. هذا يرجع إلى حقيقة أنه في كل تكرار نيوتن يجب إعادة حساب مصفوفة هيسيان وبالتالي يجب حل نظام خطي جديد.

**المقارنة مع الديناميكيات القائمة على الموضع.** قارنا أيضاً نهجنا مع PBD باستخدام قيود إجهاد الحافة. كما هو موضح في القسم 4، لا يتضمن PBD قيود الزخم مما يجعل صلابة المادة معتمدة على عدد التكرارات. يمكن رؤية هذا في الفيديو المرفق وفي الشكل 4، حيث لعدد مختلف من التكرارات تتغير صلابة المادة المحاكاة بواسطة PBD بشكل كبير. هذا ليس هو الحال في نهجنا حيث صلابة المادة أقل اعتماداً بكثير على عدد التكرارات.

**استقلالية الشبكة.** في القسم 5 قدمنا مجموعة جديدة من القيود المشتقة من الطاقات المستمرة. كما هو موضح في الشكل 5، تسمح هذه القيود الجديدة لحلالنا بالحفاظ على سلوك التشوه تحت تقريبات بسيطة متعددة متقطعة مختلفة لنفس السطح الأساسي. هذه خاصية مهمة لتطبيقات رسومات الحاسوب والبيئات التفاعلية حيث يمكن أن تتغير دقة الشبكة بشكل متكرر أثناء التطوير وحيث يتم استخدام مستويات تفصيل هندسية على نطاق واسع لزيادة الأداء.

---

### Translation Notes

- **Figures referenced:** Figure 1, 4, 5, 7, 10, 11, 12
- **Key comparisons:** Newton's method, PBD, mesh independence
- **Performance metrics:** 1-6ms/iteration, 5-10 iterations for visual quality

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
