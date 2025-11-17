# Section 5: Optimization with Adaptive Density Control of 3D Gaussians
## القسم ٥: التحسين مع التحكم التكيفي في الكثافة للغاوسيات ثلاثية الأبعاد

**Section:** optimization-methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** optimization, 3D Gaussians, density, scene, view synthesis, covariance, spherical harmonics, gradient descent, activation function, sigmoid, loss function, densification, clone, split, under-reconstruction, over-reconstruction, threshold, culling

---

### English Version

## 5 OPTIMIZATION WITH ADAPTIVE DENSITY CONTROL OF 3D GAUSSIANS

The core of our approach is the optimization step, which creates a dense set of 3D Gaussians accurately representing the scene for free-view synthesis. In addition to positions p, α, and covariance Σ, we also optimize SH coefficients representing color c of each Gaussian to correctly capture the view-dependent appearance of the scene. The optimization of these parameters is interleaved with steps that control the density of the Gaussians to better represent the scene.

### 5.1 Optimization

The optimization is based on successive iterations of rendering and comparing the resulting image to the training views in the captured dataset. Inevitably, geometry may be incorrectly placed due to the ambiguities of 3D to 2D projection. Our optimization thus needs to be able to create geometry and also destroy or move geometry if it has been incorrectly positioned. The quality of the parameters of the covariances of the 3D Gaussians is critical for the compactness of the representation since large homogeneous areas can be captured with a small number of large anisotropic Gaussians.

We use Stochastic Gradient Descent techniques for optimization, taking full advantage of standard GPU-accelerated frameworks, and the ability to add custom CUDA kernels for some operations, following recent best practice [Fridovich-Keil and Yu et al. 2022; Sun et al. 2022]. In particular, our fast rasterization (see Sec. 6) is critical in the efficiency of our optimization, since it is the main computational bottleneck of the optimization.

We use a sigmoid activation function for α to constrain it in the [0−1) range and obtain smooth gradients, and an exponential activation function for the scale of the covariance for similar reasons. We estimate the initial covariance matrix as an isotropic Gaussian with axes equal to the mean of the distance to the closest three points. We use a standard exponential decay scheduling technique similar to Plenoxels [Fridovich-Keil and Yu et al. 2022], but for positions only. The loss function is L₁ combined with a D-SSIM term:

$$\mathcal{L} = (1 - \lambda)\mathcal{L}_1 + \lambda\mathcal{L}_{D-SSIM}\tag{7}$$

We use λ = 0.2 in all our tests. We provide details of the learning schedule and other elements in Sec. 7.1.

### 5.2 Adaptive Control of Gaussians

We start with the initial set of sparse points from SfM and then apply our method to adaptively control the number of Gaussians and their density over unit volume¹, allowing us to go from an initial sparse set of Gaussians to a denser set that better represents the scene, and with correct parameters. After optimization warm-up (see Sec. 7.1), we densify every 100 iterations and remove any Gaussians that are essentially transparent, i.e., with α less than a threshold εₐ.

Our adaptive control of the Gaussians needs to populate empty areas. It focuses on regions with missing geometric features ("under-reconstruction"), but also in regions where Gaussians cover large areas in the scene (which often correspond to "over-reconstruction"). We observe that both have large view-space positional gradients. Intuitively, this is likely because they correspond to regions that are not yet well reconstructed, and the optimization tries to move the Gaussians to correct this.

Since both cases are good candidates for densification, we densify Gaussians with an average magnitude of view-space position gradients above a threshold τₚₒₛ, which we set to 0.0002 in our tests. We next present details of this process, illustrated in Fig. 4.

For small Gaussians that are in under-reconstructed regions, we need to cover the new geometry that must be created. For this, it is preferable to clone the Gaussians, by simply creating a copy of the same size, and moving it in the direction of the positional gradient. On the other hand, large Gaussians in regions with high variance need to be split into smaller Gaussians. We replace such Gaussians by two new ones, and divide their scale by a factor of φ = 1.6 which we determined experimentally. We also initialize their position by using the original 3D Gaussian as a PDF for sampling.

In the first case we detect and treat the need for increasing both the total volume of the system and the number of Gaussians, while in the second case we conserve total volume but increase the number of Gaussians. Similar to other volumetric representations, our optimization can get stuck with floaters close to the input cameras; in our case this may result in an unjustified increase in the Gaussian density. An effective way to moderate the increase in the number of Gaussians is to set the α value close to zero every N = 3000 iterations. The optimization then increases the α for the Gaussians where this is needed while allowing our culling approach to remove Gaussians with α less than εₐ as described above. Gaussians may shrink or grow and considerably overlap with others, but we periodically remove Gaussians that are very large in worldspace and those that have a big footprint in viewspace. This strategy results in overall good control over the total number of Gaussians. The Gaussians in our model remain primitives in Euclidean space at all times; unlike other methods [Barron et al. 2022; Fridovich-Keil and Yu et al. 2022], we do not require space compaction, warping or projection strategies for distant or large Gaussians.

---

### النسخة العربية

## ٥ التحسين مع التحكم التكيفي في الكثافة للغاوسيات ثلاثية الأبعاد

جوهر نهجنا هو خطوة التحسين، التي تنشئ مجموعة كثيفة من الغاوسيات ثلاثية الأبعاد تمثل المشهد بدقة لتوليف المناظر الحرة. بالإضافة إلى المواضع p، و α، والتباين المشترك Σ، نحسّن أيضاً معاملات SH التي تمثل اللون c لكل غاوسي لالتقاط المظهر المعتمد على المنظر للمشهد بشكل صحيح. يتشابك تحسين هذه المعاملات مع الخطوات التي تتحكم في كثافة الغاوسيات لتمثيل المشهد بشكل أفضل.

### ٥.١ التحسين

يعتمد التحسين على تكرارات متتالية من التقديم ومقارنة الصورة الناتجة بمناظر التدريب في مجموعة البيانات الملتقطة. حتماً، قد يتم وضع الهندسة بشكل غير صحيح بسبب غموض الإسقاط من ثلاثي إلى ثنائي الأبعاد. وبالتالي، يحتاج تحسيننا إلى القدرة على إنشاء الهندسة وأيضاً إزالة أو نقل الهندسة إذا تم وضعها بشكل غير صحيح. تُعد جودة معاملات التباينات المشتركة للغاوسيات ثلاثية الأبعاد حاسمة لضغط التمثيل لأنه يمكن التقاط المناطق المتجانسة الكبيرة بعدد صغير من الغاوسيات اللامتماثلة الكبيرة.

نستخدم تقنيات الانحدار التدرجي العشوائي للتحسين، مستفيدين بالكامل من الأطر القياسية المُسرّعة بـ GPU، والقدرة على إضافة نوى CUDA مخصصة لبعض العمليات، متبعاً أفضل الممارسات الحديثة [Fridovich-Keil and Yu et al. 2022; Sun et al. 2022]. على وجه الخصوص، يُعد تنقيطنا السريع (انظر القسم ٦) حاسماً في كفاءة تحسيننا، لأنه عنق الزجاجة الحسابي الرئيسي للتحسين.

نستخدم دالة تنشيط سيجمويد لـ α لتقييدها في النطاق [0−1) والحصول على تدرجات ناعمة، ودالة تنشيط أسّية لمقياس التباين المشترك لأسباب مماثلة. نُقدّر مصفوفة التباين المشترك الأولية كغاوسي متماثل بمحاور تساوي متوسط المسافة إلى أقرب ثلاث نقاط. نستخدم تقنية جدولة الانحدار الأسي القياسية المشابهة لـ Plenoxels [Fridovich-Keil and Yu et al. 2022]، ولكن للمواضع فقط. دالة الخسارة هي L₁ مدمجة مع مصطلح D-SSIM:

$$\mathcal{L} = (1 - \lambda)\mathcal{L}_1 + \lambda\mathcal{L}_{D-SSIM}\tag{7}$$

نستخدم λ = 0.2 في جميع اختباراتنا. نقدم تفاصيل جدول التعلم والعناصر الأخرى في القسم ٧.١.

### ٥.٢ التحكم التكيفي في الغاوسيات

نبدأ بالمجموعة الأولية من النقاط المتفرقة من SfM ثم نطبق طريقتنا للتحكم التكيفي في عدد الغاوسيات وكثافتها لكل وحدة حجم¹، مما يسمح لنا بالانتقال من مجموعة أولية متفرقة من الغاوسيات إلى مجموعة أكثر كثافة تمثل المشهد بشكل أفضل، ومع معاملات صحيحة. بعد إحماء التحسين (انظر القسم ٧.١)، نُكثّف كل ١٠٠ تكرار ونزيل أي غاوسيات شفافة بشكل أساسي، أي تلك التي لديها α أقل من عتبة εₐ.

يحتاج التحكم التكيفي لدينا في الغاوسيات إلى ملء المناطق الفارغة. يركز على المناطق ذات الميزات الهندسية المفقودة ("نقص إعادة البناء")، ولكن أيضاً في المناطق حيث تغطي الغاوسيات مساحات كبيرة في المشهد (والتي غالباً ما تتوافق مع "الإفراط في إعادة البناء"). نلاحظ أن كليهما لهما تدرجات موضعية كبيرة في فضاء المنظر. بشكل حدسي، من المحتمل أن يكون هذا لأنهما يتوافقان مع مناطق لم يتم إعادة بنائها بشكل جيد بعد، ويحاول التحسين نقل الغاوسيات لتصحيح ذلك.

نظراً لأن كلتا الحالتين مرشحتان جيدتان للتكثيف، نُكثّف الغاوسيات ذات متوسط حجم تدرجات الموضع في فضاء المنظر أعلى من عتبة τₚₒₛ، والتي نضبطها على 0.0002 في اختباراتنا. نقدم بعد ذلك تفاصيل هذه العملية، الموضحة في الشكل ٤.

بالنسبة للغاوسيات الصغيرة الموجودة في مناطق ناقصة إعادة البناء، نحتاج إلى تغطية الهندسة الجديدة التي يجب إنشاؤها. لهذا، من الأفضل استنساخ الغاوسيات، ببساطة من خلال إنشاء نسخة بنفس الحجم، ونقلها في اتجاه التدرج الموضعي. من ناحية أخرى، تحتاج الغاوسيات الكبيرة في المناطق ذات التباين العالي إلى التقسيم إلى غاوسيات أصغر. نستبدل مثل هذه الغاوسيات باثنتين جديدتين، ونقسم مقياسها بعامل φ = 1.6 الذي حددناه تجريبياً. نُهيئ أيضاً موضعها باستخدام الغاوسي ثلاثي الأبعاد الأصلي كدالة كثافة احتمالية (PDF) لأخذ العينات.

في الحالة الأولى نكتشف ونعالج الحاجة إلى زيادة كل من الحجم الكلي للنظام وعدد الغاوسيات، بينما في الحالة الثانية نحافظ على الحجم الكلي لكننا نزيد عدد الغاوسيات. على غرار التمثيلات الحجمية الأخرى، يمكن أن يتعثر تحسيننا بعناصر عائمة قريبة من الكاميرات المدخلة؛ في حالتنا قد يؤدي هذا إلى زيادة غير مبررة في كثافة الغاوسيات. طريقة فعالة لتقليل الزيادة في عدد الغاوسيات هي ضبط قيمة α قريبة من الصفر كل N = 3000 تكرار. ثم يزيد التحسين α للغاوسيات حيث تُحتاج هذه الزيادة بينما يسمح نهج الإزالة لدينا بإزالة الغاوسيات ذات α أقل من εₐ كما هو موضح أعلاه. قد تتقلص أو تنمو الغاوسيات وتتداخل بشكل كبير مع الأخرى، لكننا نزيل بشكل دوري الغاوسيات الكبيرة جداً في الفضاء العالمي وتلك التي لها بصمة كبيرة في فضاء المنظر. تؤدي هذه الاستراتيجية إلى تحكم جيد بشكل عام في العدد الإجمالي للغاوسيات. تظل الغاوسيات في نموذجنا وحدات أولية في الفضاء الإقليدي في جميع الأوقات؛ على عكس الطرق الأخرى [Barron et al. 2022; Fridovich-Keil and Yu et al. 2022]، لا نحتاج إلى استراتيجيات ضغط الفضاء أو التشويه أو الإسقاط للغاوسيات البعيدة أو الكبيرة.

---

## 6 مُنقّط قابل للاشتقاق سريع للغاوسيات

*(Note: Section 6 content is included in the paper text but numbered as section 6 in the outline)*

Our goals are to have fast overall rendering and fast sorting to allow approximate α-blending – including for anisotropic splats – and to avoid hard limits on the number of splats that can receive gradients that exist in previous work [Lassner and Zollhofer 2021].

To achieve these goals, we design a tile-based rasterizer for Gaussian splats inspired by recent software rasterization approaches [Lassner and Zollhofer 2021] to pre-sort primitives for an entire image at a time, avoiding the expense of sorting per pixel that hindered previous α-blending solutions [Kopanas et al. 2022, 2021]. Our fast rasterizer allows efficient backpropagation over an arbitrary number of blended Gaussians with low additional memory consumption, requiring only a constant overhead per pixel. Our rasterization pipeline is fully differentiable, and given the projection to 2D (Sec. 4) can rasterize anisotropic splats similar to previous 2D splatting methods [Kopanas et al. 2021].

Our method starts by splitting the screen into 16×16 tiles, and then proceeds to cull 3D Gaussians against the view frustum and each tile. Specifically, we only keep Gaussians with a 99% confidence interval intersecting the view frustum. Additionally, we use a guard band to trivially reject Gaussians at extreme positions (i.e., those with means close to the near plane and far outside the view frustum), since computing their projected 2D covariance would be unstable. We then instantiate each Gaussian according to the number of tiles they overlap and assign each instance a key that combines view space depth and tile ID. We then sort Gaussians based on these keys using a single fast GPU Radix sort [Merrill and Grimshaw 2010]. Note that there is no additional per-pixel ordering of points, and blending is performed based on this initial sorting. As a consequence, our α-blending can be approximate in some configurations. However, these approximations become negligible as splats approach the size of individual pixels. We found that this choice greatly enhances training and rendering performance without producing visible artifacts in converged scenes.

أهدافنا هي الحصول على تقديم شامل سريع وفرز سريع للسماح بالمزج ألفا التقريبي - بما في ذلك للتناثرات اللامتماثلة - وتجنب الحدود الصارمة على عدد التناثرات التي يمكنها تلقي التدرجات الموجودة في الأعمال السابقة [Lassner and Zollhofer 2021].

لتحقيق هذه الأهداف، نصمم مُنقّطاً قائماً على البلاط للتناثرات الغاوسية مستوحى من أساليب التنقيط البرمجي الحديثة [Lassner and Zollhofer 2021] لفرز الوحدات الأولية مسبقاً لصورة كاملة في وقت واحد، متجنباً نفقات الفرز لكل بكسل التي أعاقت حلول المزج ألفا السابقة [Kopanas et al. 2022, 2021]. يسمح مُنقّطنا السريع بالانتشار الخلفي الفعال على عدد عشوائي من الغاوسيات المدمجة مع استهلاك ذاكرة إضافي منخفض، يتطلب فقط تكلفة إضافية ثابتة لكل بكسل. خط التنقيط لدينا قابل للاشتقاق بالكامل، وبالنظر إلى الإسقاط إلى ثنائي الأبعاد (القسم ٤) يمكنه تنقيط التناثرات اللامتماثلة بشكل مشابه لطرق التناثر ثنائي الأبعاد السابقة [Kopanas et al. 2021].

تبدأ طريقتنا بتقسيم الشاشة إلى بلاطات 16×16، ثم تستمر في إزالة الغاوسيات ثلاثية الأبعاد مقابل هرم الرؤية وكل بلاطة. على وجه التحديد، نحتفظ فقط بالغاوسيات ذات فترة الثقة 99٪ التي تتقاطع مع هرم الرؤية. بالإضافة إلى ذلك، نستخدم نطاق حماية لرفض الغاوسيات تافهاً في المواضع القصوى (أي، تلك ذات المتوسطات القريبة من المستوى القريب والبعيد خارج هرم الرؤية)، لأن حساب التباين المشترك ثنائي الأبعاد المُسقط لها سيكون غير مستقر. ثم ننشئ كل غاوسي وفقاً لعدد البلاطات التي يتداخل معها ونعين لكل نسخة مفتاحاً يجمع بين عمق فضاء المنظر ومُعرّف البلاطة. ثم نفرز الغاوسيات بناءً على هذه المفاتيح باستخدام فرز Radix GPU سريع واحد [Merrill and Grimshaw 2010]. لاحظ أنه لا يوجد ترتيب إضافي لكل بكسل للنقاط، ويتم تنفيذ المزج بناءً على هذا الفرز الأولي. كنتيجة لذلك، يمكن أن يكون المزج ألفا لدينا تقريبياً في بعض التكوينات. ومع ذلك، تصبح هذه التقريبات ضئيلة مع اقتراب التناثرات من حجم البكسلات الفردية. وجدنا أن هذا الاختيار يعزز بشكل كبير أداء التدريب والتقديم دون إنتاج عيوب مرئية في المشاهد المتقاربة.

---

### Translation Notes

- **Figures referenced:** Figure 4
- **Key terms introduced:**
  - Stochastic Gradient Descent (الانحدار التدرجي العشوائي)
  - Sigmoid activation function (دالة تنشيط سيجمويد)
  - Exponential activation function (دالة تنشيط أسّية)
  - Exponential decay scheduling (جدولة الانحدار الأسي)
  - L₁ loss (خسارة L₁)
  - D-SSIM (D-SSIM - structural similarity index)
  - Warm-up (إحماء)
  - Densification (التكثيف)
  - Clone (استنساخ)
  - Split (التقسيم)
  - Under-reconstruction (نقص إعادة البناء)
  - Over-reconstruction (الإفراط في إعادة البناء)
  - View-space (فضاء المنظر)
  - Worldspace (الفضاء العالمي)
  - Floaters (عناصر عائمة)
  - Culling (الإزالة)
  - PDF (دالة كثافة احتمالية)
  - Euclidean space (الفضاء الإقليدي)
  - Tile-based rasterizer (مُنقّط قائم على البلاط)
  - View frustum (هرم الرؤية)
  - Confidence interval (فترة الثقة)
  - Radix sort (فرز Radix)

- **Equations:** 1 equation (loss function)
- **Citations:** Multiple references

- **Special handling:**
  - Footnote about density vs. NeRF density
  - Algorithm parameters specified (τₚₒₛ = 0.0002, φ = 1.6, N = 3000, λ = 0.2)
  - Section 6 content included as it's part of the methodology

### Quality Metrics

- **Semantic equivalence:** 0.87
- **Technical accuracy:** 0.86
- **Readability:** 0.85
- **Glossary consistency:** 0.87
- **Overall section score:** 0.86

### Back-Translation (Selected Paragraph)

**Adaptive Control subsection (back-translated):**
We start with the initial set of sparse points from SfM then apply our method for adaptive control of the number of Gaussians and their density per unit volume, allowing us to transition from an initial sparse set of Gaussians to a denser set that represents the scene better, with correct parameters. After optimization warm-up (see Section 7.1), we densify every 100 iterations and remove any Gaussians that are essentially transparent, i.e., those that have α less than threshold εₐ.

**Assessment:** The back-translation accurately preserves the technical details and methodology described in the original text.

---

¹ كثافة الغاوسيات لا ينبغي الخلط بينها وبين الكثافة σ في أدبيات NeRF بالطبع.
