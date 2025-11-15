# Section 2: Background and Related Work
## القسم 2: الخلفية والأعمال ذات الصلة

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** distributed optimization, federated learning, heterogeneous, data center, privacy, device, SGD, convergence, non-convex, IID, multi-task learning

---

### English Version

Large-scale machine learning in data centers has driven development of numerous distributed optimization methods over the past decade. However, as computing devices like phones and sensors become more powerful, learning locally in distributed networks rather than centralizing data has become increasingly attractive. This challenge, termed federated learning, introduces novel complications around privacy, heterogeneous data and devices, and massively distributed networks.

Recent optimization approaches tailored to federated settings have demonstrated improvements over traditional distributed techniques such as ADMM or mini-batch methods by enabling inexact local updating and allowing small device subsets to participate in each communication round. For instance, Smith et al. (2017) proposed a communication-efficient primal-dual method enabling each device to learn distinct but related models through multi-task learning. However, such approaches don't generalize to non-convex problems like deep learning where strong duality fails. In non-convex settings, Federated Averaging (FedAvg), a heuristic averaging local SGD updates, has demonstrated strong empirical performance.

FedAvg presents significant analytical challenges due to its local updating scheme, limited device participation, and frequently non-identically distributed data. As devices generate their own local data, statistical heterogeneity is inherent, with non-identical distributions across devices. Several works have studied parallel SGD variants in simplified settings, but these analyses rely on the IID assumption that each local solver mirrors the same stochastic process—an assumption that doesn't hold in heterogeneous settings.

Recent work has explored convergence guarantees under statistical heterogeneity, yet these typically require all devices participate in every communication round, which proves infeasible in realistic federated networks. Additionally, these analyses mandate specific solvers (SGD or GD) or impose restrictive assumptions like convexity or uniformly bounded gradients. Heuristic approaches addressing statistical heterogeneity through data sharing either burden network bandwidth, compromise privacy by transmitting local data, or require carefully generating auxiliary proxy data.

Beyond statistical heterogeneity, systems heterogeneity presents critical concerns. Device storage, computational capability, and communication capacity vary due to hardware differences (CPU, memory), network connectivity (3G, 4G, 5G, wifi), and power availability. Practical approaches often discard constrained devices failing to complete certain training amounts, though this limits effective participating devices and potentially introduces bias if dropped devices have specific data characteristics.

This work proposes FedProx, exploring a broader framework handling heterogeneous federated environments while maintaining privacy and computational benefits. The analysis characterizes statistical dissimilarity between local functions while accounting for practical systems constraints. The dissimilarity characterization draws inspiration from the randomized Kaczmarz method for linear system solving, with similar assumptions employed in other SGD variant analyses. The framework provides improved robustness and stability for heterogeneous federated network optimization.

Two aspects—the proximal term in FedProx and the bounded dissimilarity assumption—have prior treatment in optimization literature, though typically with different motivations and outside federated contexts. Additional background discussion appears in Appendix B.

---

### النسخة العربية

دفع التعلم الآلي واسع النطاق في مراكز البيانات إلى تطوير العديد من طرق التحسين الموزع خلال العقد الماضي. ومع ذلك، مع ازدياد قوة الأجهزة الحاسوبية مثل الهواتف وأجهزة الاستشعار، أصبح التعلم المحلي في الشبكات الموزعة بدلاً من مركزة البيانات أكثر جاذبية بشكل متزايد. يقدم هذا التحدي، الذي يُطلق عليه التعلم الاتحادي، تعقيدات جديدة حول الخصوصية والبيانات والأجهزة غير المتجانسة والشبكات الموزعة على نطاق واسع.

أظهرت أساليب التحسين الحديثة المصممة خصيصًا للإعدادات الاتحادية تحسينات على التقنيات الموزعة التقليدية مثل ADMM أو طرق الدفعات الصغيرة (mini-batch) من خلال تمكين التحديث المحلي غير الدقيق والسماح لمجموعات فرعية صغيرة من الأجهزة بالمشاركة في كل جولة اتصال. على سبيل المثال، اقترح Smith et al. (2017) طريقة أولية-ثنائية فعالة في الاتصال تمكّن كل جهاز من تعلم نماذج متميزة ولكن ذات صلة من خلال التعلم متعدد المهام. ومع ذلك، فإن هذه الأساليب لا تعمم على المسائل غير المحدبة مثل التعلم العميق حيث تفشل الثنائية القوية. في الإعدادات غير المحدبة، أظهر FedAvg، وهو استدلالي لحساب متوسط تحديثات SGD المحلية، أداءً تجريبيًا قويًا.

يقدم FedAvg تحديات تحليلية كبيرة بسبب مخطط التحديث المحلي، والمشاركة المحدودة للأجهزة، والبيانات الموزعة بشكل غير متطابق في كثير من الأحيان. نظرًا لأن الأجهزة تولد بياناتها المحلية الخاصة، فإن عدم التجانس الإحصائي متأصل، مع توزيعات غير متطابقة عبر الأجهزة. درست العديد من الأعمال متغيرات SGD المتوازية في إعدادات مبسطة، لكن هذه التحليلات تعتمد على افتراض IID بأن كل حلال محلي يعكس نفس العملية العشوائية - وهو افتراض لا يصمد في الإعدادات غير المتجانسة.

استكشفت الأعمال الحديثة ضمانات التقارب في ظل عدم التجانس الإحصائي، ومع ذلك فإن هذه تتطلب عادةً مشاركة جميع الأجهزة في كل جولة اتصال، وهو ما يثبت أنه غير عملي في الشبكات الاتحادية الواقعية. بالإضافة إلى ذلك، تفرض هذه التحليلات حلالات محددة (SGD أو GD) أو تفرض افتراضات مقيدة مثل التحدب أو التدرجات المحدودة بشكل موحد. تؤدي الأساليب الاستدلالية التي تعالج عدم التجانس الإحصائي من خلال مشاركة البيانات إما إلى تحميل عرض النطاق الترددي للشبكة، أو المساس بالخصوصية من خلال نقل البيانات المحلية، أو تتطلب توليد بيانات وكيلة مساعدة بعناية.

بالإضافة إلى عدم التجانس الإحصائي، يقدم عدم التجانس في الأنظمة مخاوف حاسمة. يختلف تخزين الجهاز والقدرة الحسابية وسعة الاتصال بسبب الاختلافات في الأجهزة (CPU، الذاكرة)، واتصال الشبكة (3G، 4G، 5G، wifi)، وتوافر الطاقة. غالبًا ما تتجاهل الأساليب العملية الأجهزة المقيدة التي تفشل في إكمال كميات معينة من التدريب، على الرغم من أن هذا يحد من الأجهزة المشاركة الفعالة ويمكن أن يقدم تحيزًا إذا كانت الأجهزة المسقطة تحتوي على خصائص بيانات محددة.

يقترح هذا العمل FedProx، الذي يستكشف إطار عمل أوسع للتعامل مع البيئات الاتحادية غير المتجانسة مع الحفاظ على فوائد الخصوصية والحسابية. يميز التحليل التباين الإحصائي بين الدوال المحلية مع مراعاة قيود الأنظمة العملية. يستلهم توصيف التباين من طريقة Kaczmarz العشوائية لحل الأنظمة الخطية، مع افتراضات مماثلة مستخدمة في تحليلات متغيرات SGD الأخرى. يوفر إطار العمل قوة واستقرارًا محسّنين لتحسين الشبكات الاتحادية غير المتجانسة.

جانبان - الحد القريبي في FedProx وافتراض التباين المحدود - لهما معالجة سابقة في أدبيات التحسين، على الرغم من أنه عادةً بدوافع مختلفة وخارج السياقات الاتحادية. تظهر مناقشة الخلفية الإضافية في الملحق B.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - ADMM (Alternating Direction Method of Multipliers)
  - mini-batch (دفعات صغيرة)
  - primal-dual method (طريقة أولية-ثنائية)
  - multi-task learning (التعلم متعدد المهام)
  - strong duality (الثنائية القوية)
  - IID (Independent and Identically Distributed)
  - convexity (التحدب)
  - bounded gradients (التدرجات المحدودة)
  - Kaczmarz method (طريقة Kaczmarz)
  - dissimilarity (التباين)
- **Equations:** None
- **Citations:** Smith et al. (2017)
- **Special handling:**
  - Technical acronyms like ADMM, IID, SGD, GD kept in English as standard in the field
  - Network standards (3G, 4G, 5G) kept as-is

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
