# Section 5: Hierarchical Sampling
## القسم 5: العينات الهرمية

**Section:** hierarchical-sampling
**Translation Quality:** 0.87
**Glossary Terms Used:** hierarchical sampling, variance reduction, adaptive sampling, stratification, refinement, spatial hierarchy

---

### English Version

We now introduce hierarchical sampling, a new variance reduction technique that is particularly effective for Monte Carlo rendering. The key insight is to adaptively subdivide the integration domain based on the local variance of the integrand, concentrating samples in regions that contribute most to the variance.

**Motivation**

In standard Monte Carlo integration, samples are distributed uniformly (or according to a fixed importance distribution) across the entire domain. However, in many rendering scenarios, the integrand varies greatly across the domain:

- Direct lighting from small area light sources creates high-variance regions
- Specular reflections concentrate energy in narrow solid angle ranges
- Caustics create localized bright regions
- Complex geometry creates discontinuities in the integrand

A uniform sampling strategy wastes samples in low-variance regions while under-sampling high-variance regions. Hierarchical sampling addresses this by adaptively allocating samples based on estimated variance.

**The Hierarchical Sampling Algorithm**

The algorithm proceeds in multiple passes:

**Pass 1: Initial Sampling**
1. Divide the integration domain into a coarse grid of cells
2. Take a small number of samples $n_0$ in each cell
3. Compute the sample mean $\mu_i$ and variance $\sigma_i^2$ for each cell $i$

**Pass 2: Adaptive Refinement**
1. Estimate the contribution of each cell to the total variance:
   $$V_i = \sigma_i^2 \cdot A_i^2$$
   where $A_i$ is the area (or measure) of cell $i$
2. Sort cells by their variance contribution
3. Subdivide cells with highest variance into smaller cells
4. Take additional samples in the refined cells
5. Update mean and variance estimates

**Pass 3: Iteration**
Repeat the refinement process until:
- A sample budget is exhausted, or
- The variance falls below a threshold, or
- A maximum refinement level is reached

**Mathematical Foundation**

The variance of a Monte Carlo estimator over a partitioned domain can be decomposed as:

$$\text{Var}[\langle I \rangle] = \sum_{i=1}^{M} \frac{A_i^2}{n_i} \sigma_i^2$$

where:
- $M$ is the number of cells in the partition
- $A_i$ is the measure of cell $i$
- $n_i$ is the number of samples in cell $i$
- $\sigma_i^2$ is the variance within cell $i$

To minimize total variance for a fixed total number of samples $N = \sum_i n_i$, we want to allocate samples proportionally to $A_i \sigma_i$ (this follows from Lagrange multipliers):

$$n_i \propto A_i \sigma_i$$

Hierarchical sampling approximates this optimal allocation by:
1. Estimating $\sigma_i$ from preliminary samples
2. Subdividing high-variance cells (reducing $A_i$ and $\sigma_i$)
3. Allocating more samples to refined regions

**Hierarchical Data Structures**

Hierarchical sampling can be implemented using various spatial data structures:

- **Quadtrees/Octrees**: for 2D/3D domains, recursively subdivide into 4/8 children
- **KD-trees**: axis-aligned binary space partitioning
- **BSP trees**: general binary space partitioning with arbitrary planes
- **Grids**: uniform subdivision with adaptive refinement

For rendering applications, we typically use quadtrees for image-space subdivision (pixels) and octrees for directional domains (hemisphere of directions).

**Application to Rendering**

In the context of the rendering equation, hierarchical sampling can be applied to:

**1. Pixel Sampling**
Subdivide the image plane adaptively, taking more samples in high-contrast regions (edges, shadows, highlights).

**2. Directional Sampling**
Subdivide the hemisphere of incident directions at each surface point, concentrating samples near:
- Specular reflection directions
- Light source directions
- High-frequency BRDF features

**3. Area Light Sampling**
Subdivide extended light sources, taking more samples from regions that contribute significantly to the illumination.

**4. Path Space Sampling**
Treat the space of all possible light paths as the integration domain and adaptively sample important paths.

**Bias and Convergence**

A key property of hierarchical sampling is that it remains unbiased if the variance estimates are computed correctly. The subdivision and sample allocation decisions are based on the samples themselves, which introduces correlation, but as long as we:

1. Use unbiased variance estimators
2. Weight samples correctly by their probability
3. Don't discard samples based on their values

the overall estimator remains unbiased with guaranteed convergence to the true integral.

**Variance Reduction Analysis**

For integrands with localized high-variance regions, hierarchical sampling can reduce variance significantly compared to uniform sampling. Consider a 1D integral with a narrow spike:

- **Uniform sampling**: variance is $O(1)$ because most samples miss the spike
- **Hierarchical sampling**: after $\log(1/\epsilon)$ refinement levels, cells containing the spike have width $\epsilon$, reducing variance by a factor proportional to $1/\epsilon$

In practice, we observe variance reductions of 2-10× for typical rendering scenarios, which translates to needing 4-100× fewer samples for the same image quality.

**Comparison with Other Techniques**

Hierarchical sampling is related to but distinct from:

- **Stratified sampling**: pre-divides the domain uniformly; hierarchical sampling adapts the partition
- **Adaptive sampling**: general term; hierarchical sampling is a specific adaptive strategy
- **Importance sampling**: changes the probability distribution; hierarchical sampling changes the partition while potentially using importance sampling within cells
- **Quasi-Monte Carlo**: uses deterministic low-discrepancy sequences; hierarchical sampling can be combined with QMC

**Implementation Considerations**

Practical implementation requires careful attention to:

1. **Storage**: hierarchical structures require memory for the tree
2. **Sample budget**: balance initial sampling vs. refinement samples
3. **Variance estimation**: need enough samples per cell for reliable estimates (typically $n_0 \geq 4$)
4. **Termination criteria**: when to stop refining
5. **Amortization**: can reuse hierarchies across frames for temporal coherence

**Extensions and Variations**

The basic hierarchical sampling framework admits many variations:

- **Multi-resolution hierarchies**: maintain samples at all levels, not just leaves
- **Error-driven refinement**: use error estimates instead of variance
- **Perceptual metrics**: refine based on perceptual importance rather than raw variance
- **Gradient-based refinement**: use local gradients to predict variance
- **Anisotropic refinement**: subdivide non-uniformly in different dimensions

These extensions make hierarchical sampling a versatile and powerful tool for Monte Carlo rendering.

---

### النسخة العربية

نقدم الآن العينات الهرمية، وهي تقنية جديدة لتقليل التباين فعالة بشكل خاص للتقديم بطريقة مونت كارلو. الملاحظة الأساسية هي تقسيم مجال التكامل بشكل تكيفي بناءً على التباين المحلي للدالة المُكاملة، مع تركيز العينات في المناطق التي تساهم أكثر في التباين.

**الدافع**

في تكامل مونت كارلو القياسي، تُوزع العينات بشكل موحد (أو وفقاً لتوزيع أهمية ثابت) عبر المجال بأكمله. ومع ذلك، في العديد من سيناريوهات التقديم، تتباين الدالة المُكاملة بشكل كبير عبر المجال:

- الإضاءة المباشرة من مصادر ضوء صغيرة المساحة تخلق مناطق عالية التباين
- الانعكاسات المرآوية تركز الطاقة في نطاقات زاوية صلبة ضيقة
- الظواهر الكاوية تخلق مناطق ساطعة موضعية
- الهندسة المعقدة تخلق عدم استمرارية في الدالة المُكاملة

تهدر استراتيجية أخذ العينات الموحدة العينات في المناطق منخفضة التباين بينما تأخذ عينات غير كافية من المناطق عالية التباين. تعالج العينات الهرمية هذا من خلال تخصيص العينات بشكل تكيفي بناءً على التباين المقدر.

**خوارزمية العينات الهرمية**

تستمر الخوارزمية في عدة ممرات:

**الممر 1: أخذ العينات الأولي**
1. تقسيم مجال التكامل إلى شبكة خشنة من الخلايا
2. أخذ عدد صغير من العينات $n_0$ في كل خلية
3. حساب متوسط العينة $\mu_i$ والتباين $\sigma_i^2$ لكل خلية $i$

**الممر 2: التحسين التكيفي**
1. تقدير مساهمة كل خلية في التباين الكلي:
   $$V_i = \sigma_i^2 \cdot A_i^2$$
   حيث $A_i$ هي المساحة (أو القياس) للخلية $i$
2. ترتيب الخلايا حسب مساهمتها في التباين
3. تقسيم الخلايا ذات التباين الأعلى إلى خلايا أصغر
4. أخذ عينات إضافية في الخلايا المحسنة
5. تحديث تقديرات المتوسط والتباين

**الممر 3: التكرار**
تكرار عملية التحسين حتى:
- استنفاد ميزانية العينات، أو
- انخفاض التباين إلى ما دون عتبة معينة، أو
- الوصول إلى مستوى تحسين أقصى

**الأساس الرياضي**

يمكن تفكيك تباين مقدر مونت كارلو على مجال مُقسم على النحو التالي:

$$\text{Var}[\langle I \rangle] = \sum_{i=1}^{M} \frac{A_i^2}{n_i} \sigma_i^2$$

حيث:
- $M$ هو عدد الخلايا في التقسيم
- $A_i$ هو قياس الخلية $i$
- $n_i$ هو عدد العينات في الخلية $i$
- $\sigma_i^2$ هو التباين داخل الخلية $i$

لتقليل التباين الكلي لعدد إجمالي ثابت من العينات $N = \sum_i n_i$، نريد تخصيص العينات بشكل متناسب مع $A_i \sigma_i$ (وهذا يتبع من مضاعفات لاغرانج):

$$n_i \propto A_i \sigma_i$$

تقارب العينات الهرمية هذا التخصيص الأمثل من خلال:
1. تقدير $\sigma_i$ من العينات الأولية
2. تقسيم الخلايا عالية التباين (تقليل $A_i$ و $\sigma_i$)
3. تخصيص المزيد من العينات للمناطق المحسنة

**بنى البيانات الهرمية**

يمكن تنفيذ العينات الهرمية باستخدام بنى بيانات مكانية مختلفة:

- **الأشجار الرباعية/الثمانية**: للمجالات ثنائية/ثلاثية الأبعاد، تقسيم تكراري إلى 4/8 أطفال
- **أشجار KD**: تقسيم فضاء ثنائي محاذي للمحور
- **أشجار BSP**: تقسيم فضاء ثنائي عام بمستويات تعسفية
- **الشبكات**: تقسيم موحد مع تحسين تكيفي

لتطبيقات التقديم، نستخدم عادةً الأشجار الرباعية لتقسيم فضاء الصورة (البكسلات) والأشجار الثمانية للمجالات الاتجاهية (نصف كرة الاتجاهات).

**التطبيق على التقديم**

في سياق معادلة التقديم، يمكن تطبيق العينات الهرمية على:

**1. أخذ عينات البكسل**
تقسيم مستوى الصورة بشكل تكيفي، مع أخذ المزيد من العينات في المناطق عالية التباين (الحواف، الظلال، الإضاءات البارزة).

**2. أخذ العينات الاتجاهي**
تقسيم نصف كرة الاتجاهات الساقطة عند كل نقطة سطح، مع تركيز العينات بالقرب من:
- اتجاهات الانعكاس المرآوي
- اتجاهات مصدر الضوء
- ميزات BRDF عالية التردد

**3. أخذ عينات الضوء المساحي**
تقسيم مصادر الضوء الممتدة، مع أخذ المزيد من العينات من المناطق التي تساهم بشكل كبير في الإضاءة.

**4. أخذ عينات فضاء المسار**
التعامل مع فضاء جميع مسارات الضوء المحتملة كمجال التكامل وأخذ عينات تكيفية من المسارات المهمة.

**التحيز والتقارب**

خاصية أساسية للعينات الهرمية هي أنها تبقى غير متحيزة إذا تم حساب تقديرات التباين بشكل صحيح. تستند قرارات التقسيم وتخصيص العينات إلى العينات نفسها، مما يُدخل ترابطاً، ولكن طالما:

1. نستخدم مقدرات تباين غير متحيزة
2. نوزن العينات بشكل صحيح حسب احتماليتها
3. لا نتخلص من العينات بناءً على قيمها

يبقى المقدر الإجمالي غير متحيز مع تقارب مضمون إلى التكامل الحقيقي.

**تحليل تقليل التباين**

للدوال المُكاملة ذات المناطق عالية التباين الموضعية، يمكن للعينات الهرمية أن تقلل التباين بشكل كبير مقارنة بأخذ العينات الموحد. لنعتبر تكامل أحادي البعد به قمة ضيقة:

- **أخذ العينات الموحد**: التباين هو $O(1)$ لأن معظم العينات تفوت القمة
- **العينات الهرمية**: بعد $\log(1/\epsilon)$ مستويات تحسين، تكون الخلايا المحتوية على القمة بعرض $\epsilon$، مما يقلل التباين بمعامل متناسب مع $1/\epsilon$

عملياً، نلاحظ تخفيضات في التباين بمقدار 2-10× لسيناريوهات التقديم النموذجية، مما يعني الحاجة إلى عينات أقل بمقدار 4-100× لنفس جودة الصورة.

**المقارنة مع التقنيات الأخرى**

ترتبط العينات الهرمية بما يلي ولكنها مختلفة عنها:

- **أخذ العينات الطبقي**: يقسم المجال مسبقاً بشكل موحد؛ العينات الهرمية تُكيف التقسيم
- **أخذ العينات التكيفي**: مصطلح عام؛ العينات الهرمية هي استراتيجية تكيفية محددة
- **أخذ العينات حسب الأهمية**: تغير توزيع الاحتمال؛ العينات الهرمية تغير التقسيم بينما قد تستخدم أخذ العينات حسب الأهمية داخل الخلايا
- **شبه مونت كارلو**: تستخدم متتاليات حتمية منخفضة التباين؛ يمكن دمج العينات الهرمية مع QMC

**اعتبارات التنفيذ**

يتطلب التنفيذ العملي اهتماماً دقيقاً بـ:

1. **التخزين**: تتطلب البنى الهرمية ذاكرة للشجرة
2. **ميزانية العينات**: توازن أخذ العينات الأولي مقابل عينات التحسين
3. **تقدير التباين**: نحتاج إلى عينات كافية لكل خلية لتقديرات موثوقة (عادةً $n_0 \geq 4$)
4. **معايير الإنهاء**: متى نتوقف عن التحسين
5. **الاستهلاك**: يمكن إعادة استخدام التسلسلات الهرمية عبر الإطارات للتماسك الزمني

**التوسعات والتنويعات**

يقبل إطار العينات الهرمية الأساسي العديد من التنويعات:

- **التسلسلات الهرمية متعددة الدقة**: الحفاظ على العينات في جميع المستويات، وليس فقط الأوراق
- **التحسين المدفوع بالخطأ**: استخدام تقديرات الخطأ بدلاً من التباين
- **المقاييس الإدراكية**: التحسين بناءً على الأهمية الإدراكية بدلاً من التباين الخام
- **التحسين القائم على التدرج**: استخدام التدرجات المحلية للتنبؤ بالتباين
- **التحسين غير المتماثل**: التقسيم بشكل غير موحد في أبعاد مختلفة

تجعل هذه التوسعات العينات الهرمية أداة متعددة الاستخدامات وقوية للتقديم بطريقة مونت كارلو.

---

### Translation Notes

- **Figures referenced:** None explicitly, though the paper likely has diagrams of hierarchical subdivision
- **Key terms introduced:**
  - hierarchical sampling (العينات الهرمية)
  - adaptive sampling (أخذ العينات التكيفي)
  - adaptive subdivision (تقسيم تكيفي)
  - variance contribution (مساهمة التباين)
  - sample budget (ميزانية العينات)
  - refinement level (مستوى التحسين)
  - partition (تقسيم)
  - cell (خلية)
  - coarse grid (شبكة خشنة)
  - sample mean (متوسط العينة)
  - Lagrange multipliers (مضاعفات لاغرانج)
  - optimal allocation (التخصيص الأمثل)
  - quadtree (الشجرة الرباعية)
  - octree (الشجرة الثمانية)
  - KD-tree (شجرة KD)
  - BSP tree (شجرة BSP)
  - space partitioning (تقسيم الفضاء)
  - image-space (فضاء الصورة)
  - directional domain (المجال الاتجاهي)
  - area light (ضوء مساحي)
  - path space (فضاء المسار)
  - unbiased estimator (مقدر غير متحيز)
  - correlation (ترابط)
  - localized regions (مناطق موضعية)
  - temporal coherence (التماسك الزمني)
  - multi-resolution (متعدد الدقة)
  - error-driven (مدفوع بالخطأ)
  - perceptual importance (الأهمية الإدراكية)
  - gradient-based (قائم على التدرج)
  - anisotropic (غير متماثل)
- **Equations:** 3+ equations including variance decomposition, optimal allocation
- **Citations:** None explicitly
- **Special handling:**
  - Preserved all mathematical notation
  - Explained the algorithm in clear steps
  - Connected theory to practical implementation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
