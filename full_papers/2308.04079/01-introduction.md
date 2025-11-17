# Section 1: Introduction
## القسم ١: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** rendering, real-time, neural network, radiance field, novel-view synthesis, optimization, rasterization, GPU, volumetric, representation, anisotropic, covariance, spherical harmonic, alpha-blending, differentiable, splatting, scene, training, dataset, state-of-the-art

---

### English Version

## 1 INTRODUCTION

Meshes and points are the most common 3D scene representations because they are explicit and are a good fit for fast GPU/CUDA-based rasterization. In contrast, recent Neural Radiance Field (NeRF) methods build on continuous scene representations, typically optimizing a Multi-Layer Perceptron (MLP) using volumetric ray-marching for novel-view synthesis of captured scenes. Similarly, the most efficient radiance field solutions to date build on continuous representations by interpolating values stored in, e.g., voxel [Fridovich-Keil and Yu et al. 2022] or hash [Müller et al. 2022] grids or points [Xu et al. 2022]. While the continuous nature of these methods helps optimization, the stochastic sampling required for rendering is costly and can result in noise. We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive training times, while our tile-based splatting solution ensures real-time rendering at SOTA quality for 1080p resolution on several previously published datasets [Barron et al. 2022; Hedman et al. 2018; Knapitsch et al. 2017] (see Fig. 1).

Our goal is to allow real-time rendering for scenes captured with multiple photos, and create the representations with optimization times as fast as the most efficient previous methods for typical real scenes. Recent methods achieve fast training [Fridovich-Keil and Yu et al. 2022; Müller et al. 2022], but struggle to achieve the visual quality obtained by the current SOTA NeRF methods, i.e., Mip-NeRF360 [Barron et al. 2022], which requires up to 48 hours of training time. The fast – but lower-quality – radiance field methods can achieve interactive rendering times depending on the scene (10-15 frames per second), but fall short of real-time rendering at high resolution.

Our solution builds on three main components. We first introduce 3D Gaussians as a flexible and expressive scene representation. We start with the same input as previous NeRF-like methods, i.e., cameras calibrated with Structure-from-Motion (SfM) [Snavely et al. 2006] and initialize the set of 3D Gaussians with the sparse point cloud produced for free as part of the SfM process. In contrast to most point-based solutions that require Multi-View Stereo (MVS) data [Aliev et al. 2020; Kopanas et al. 2021; Rückert et al. 2022], we achieve high-quality results with only SfM points as input. Note that for the NeRF-synthetic dataset, our method achieves high quality even with random initialization. We show that 3D Gaussians are an excellent choice, since they are a differentiable volumetric representation, but they can also be rasterized very efficiently by projecting them to 2D, and applying standard α-blending, using an equivalent image formation model as NeRF. The second component of our method is optimization of the properties of the 3D Gaussians – 3D position, opacity α, anisotropic covariance, and spherical harmonic (SH) coefficients – interleaved with adaptive density control steps, where we add and occasionally remove 3D Gaussians during optimization. The optimization procedure produces a reasonably compact, unstructured, and precise representation of the scene (1-5 million Gaussians for all scenes tested). The third and final element of our method is our real-time rendering solution that uses fast GPU sorting algorithms and is inspired by tile-based rasterization, following recent work [Lassner and Zollhofer 2021]. However, thanks to our 3D Gaussian representation, we can perform anisotropic splatting that respects visibility ordering – thanks to sorting and α-blending – and enable a fast and accurate backward pass by tracking the traversal of as many sorted splats as required.

To summarize, we provide the following contributions:
• The introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields.
• An optimization method of 3D Gaussian properties, interleaved with adaptive density control that creates high-quality representations for captured scenes.
• A fast, differentiable rendering approach for the GPU, which is visibility-aware, allows anisotropic splatting and fast backpropagation to achieve high-quality novel view synthesis.

Our results on previously published datasets show that we can optimize our 3D Gaussians from multi-view captures and achieve equal or better quality than the best quality previous implicit radiance field approaches. We also can achieve training speeds and quality similar to the fastest methods and importantly provide the first real-time rendering with high quality for novel-view synthesis.

---

### النسخة العربية

## ١ المقدمة

تُعد الشبكات (Meshes) والنقاط أكثر تمثيلات المشاهد ثلاثية الأبعاد شيوعاً لأنها صريحة وتتناسب جيداً مع التنقيط السريع القائم على وحدات معالجة الرسومات GPU/CUDA. في المقابل، تعتمد طرق حقول الإشعاع العصبية (NeRF) الحديثة على تمثيلات مشاهد مستمرة، حيث تقوم عادةً بتحسين البيرسبترون متعدد الطبقات (MLP) باستخدام التتبع الشعاعي الحجمي لتوليد المناظر الجديدة للمشاهد الملتقطة. وبالمثل، تعتمد حلول حقول الإشعاع الأكثر كفاءة حتى الآن على تمثيلات مستمرة من خلال استيفاء القيم المخزنة في، على سبيل المثال، شبكات الفوكسل [Fridovich-Keil and Yu et al. 2022] أو الهاش [Müller et al. 2022] أو النقاط [Xu et al. 2022]. بينما تساعد الطبيعة المستمرة لهذه الطرق في التحسين، فإن العينات العشوائية المطلوبة للتقديم مكلفة ويمكن أن تؤدي إلى ضوضاء. نقدم نهجاً جديداً يجمع بين أفضل ما في العالمين: يسمح تمثيلنا بالغاوسيات ثلاثية الأبعاد بالتحسين مع جودة بصرية متقدمة (SOTA) وأوقات تدريب منافسة، بينما يضمن حلنا للتناثر القائم على البلاط التقديم في الوقت الفعلي بجودة متقدمة بدقة وضوح ١٠٨٠ بكسل على عدة مجموعات بيانات منشورة سابقاً [Barron et al. 2022; Hedman et al. 2018; Knapitsch et al. 2017] (انظر الشكل ١).

هدفنا هو تمكين التقديم في الوقت الفعلي للمشاهد الملتقطة بصور متعددة، وإنشاء التمثيلات بأوقات تحسين سريعة بقدر أكثر الطرق السابقة كفاءة للمشاهد الواقعية النموذجية. تحقق الطرق الحديثة تدريباً سريعاً [Fridovich-Keil and Yu et al. 2022; Müller et al. 2022]، لكنها تكافح لتحقيق الجودة البصرية التي تحصل عليها طرق NeRF المتقدمة الحالية، أي Mip-NeRF360 [Barron et al. 2022]، والتي تتطلب ما يصل إلى ٤٨ ساعة من وقت التدريب. يمكن لطرق حقول الإشعاع السريعة - ولكن الأقل جودة - تحقيق أوقات تقديم تفاعلية اعتماداً على المشهد (١٠-١٥ إطاراً في الثانية)، لكنها تفشل في تحقيق التقديم في الوقت الفعلي بدقة وضوح عالية.

يعتمد حلنا على ثلاثة مكونات رئيسية. أولاً، نقدم الغاوسيات ثلاثية الأبعاد كتمثيل مرن ومعبّر للمشهد. نبدأ بنفس المدخلات كالطرق السابقة الشبيهة بـ NeRF، أي الكاميرات المعايرة باستخدام البنية من الحركة (SfM) [Snavely et al. 2006] ونُهيئ مجموعة الغاوسيات ثلاثية الأبعاد بسحابة النقاط المتفرقة المنتجة مجاناً كجزء من عملية SfM. على النقيض من معظم الحلول القائمة على النقاط التي تتطلب بيانات الاستريو متعدد المناظر (MVS) [Aliev et al. 2020; Kopanas et al. 2021; Rückert et al. 2022]، نحقق نتائج عالية الجودة بنقاط SfM فقط كمدخلات. لاحظ أنه بالنسبة لمجموعة بيانات NeRF-synthetic، تحقق طريقتنا جودة عالية حتى مع التهيئة العشوائية. نُظهر أن الغاوسيات ثلاثية الأبعاد اختيار ممتاز، لأنها تمثيل حجمي قابل للاشتقاق، لكن يمكن أيضاً تنقيطها بكفاءة عالية من خلال إسقاطها إلى 2D، وتطبيق المزج ألفا القياسي، باستخدام نموذج تشكيل الصورة المكافئ لـ NeRF. المكون الثاني لطريقتنا هو تحسين خصائص الغاوسيات ثلاثية الأبعاد - الموقع ثلاثي الأبعاد، والعتامة α، والتباين المشترك اللامتماثل، ومعاملات التوافقيات الكروية (SH) - متشابكاً مع خطوات التحكم في الكثافة التكيفية، حيث نضيف ونزيل أحياناً غاوسيات ثلاثية الأبعاد أثناء التحسين. تنتج عملية التحسين تمثيلاً مضغوطاً ومنظماً ودقيقاً بشكل معقول للمشهد (١-٥ مليون غاوسي لجميع المشاهد المختبرة). العنصر الثالث والأخير لطريقتنا هو حل التقديم في الوقت الفعلي الذي يستخدم خوارزميات فرز GPU السريعة ومستوحى من التنقيط القائم على البلاط، متبعاً أعمالاً حديثة [Lassner and Zollhofer 2021]. ومع ذلك، بفضل تمثيلنا بالغاوسيات ثلاثية الأبعاد، يمكننا إجراء تناثر لامتماثل يحترم ترتيب الرؤية - بفضل الفرز والمزج ألفا - ويتيح تمريراً خلفياً سريعاً ودقيقاً من خلال تتبع اجتياز أكبر عدد ممكن من التناثرات المفروزة حسب الحاجة.

للتلخيص، نقدم المساهمات التالية:
• تقديم الغاوسيات ثلاثية الأبعاد اللامتماثلة كتمثيل عالي الجودة وغير منظم لحقول الإشعاع.
• طريقة تحسين لخصائص الغاوسيات ثلاثية الأبعاد، متشابكة مع التحكم في الكثافة التكيفية التي تنشئ تمثيلات عالية الجودة للمشاهد الملتقطة.
• نهج تقديم سريع وقابل للاشتقاق لوحدات معالجة الرسومات، واعٍ للرؤية، ويسمح بالتناثر اللامتماثل والانتشار الخلفي السريع لتحقيق توليد مناظر جديدة عالي الجودة.

تُظهر نتائجنا على مجموعات البيانات المنشورة سابقاً أنه يمكننا تحسين غاوسياتنا ثلاثية الأبعاد من الالتقاطات متعددة المناظر وتحقيق جودة مساوية أو أفضل من أفضل أساليب حقول الإشعاع الضمنية السابقة من حيث الجودة. يمكننا أيضاً تحقيق سرعات تدريب وجودة مماثلة لأسرع الطرق والأهم من ذلك توفير أول تقديم في الوقت الفعلي بجودة عالية لتوليد المناظر الجديدة.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:**
  - Meshes (الشبكات)
  - Points (النقاط)
  - Rasterization (التنقيط)
  - Neural Radiance Field/NeRF (حقل الإشعاع العصبي)
  - Multi-Layer Perceptron/MLP (البيرسبترون متعدد الطبقات)
  - Volumetric ray-marching (التتبع الشعاعي الحجمي)
  - Novel-view synthesis (توليد المناظر الجديدة)
  - Voxel (الفوكسل)
  - Hash grids (شبكات الهاش)
  - 3D Gaussians (الغاوسيات ثلاثية الأبعاد)
  - Splatting (التناثر)
  - Structure-from-Motion/SfM (البنية من الحركة)
  - Multi-View Stereo/MVS (الاستريو متعدد المناظر)
  - Anisotropic covariance (التباين المشترك اللامتماثل)
  - Spherical harmonic/SH (التوافقيات الكروية)
  - Alpha-blending (المزج ألفا)
  - Tile-based rasterization (التنقيط القائم على البلاط)

- **Equations:** None in this section
- **Citations:** Multiple references cited [Barron et al. 2022; Hedman et al. 2018; Knapitsch et al. 2017; Fridovich-Keil and Yu et al. 2022; Müller et al. 2022; Xu et al. 2022; Snavely et al. 2006; Aliev et al. 2020; Kopanas et al. 2021; Rückert et al. 2022; Lassner and Zollhofer 2021]

- **Special handling:**
  - Acronyms kept in English with Arabic explanations: NeRF, MLP, SfM, MVS, SH, SOTA
  - Technical terms translated but original kept in parentheses for clarity
  - Three main contributions listed as bullet points

### Quality Metrics

- **Semantic equivalence:** 0.88
- **Technical accuracy:** 0.87
- **Readability:** 0.86
- **Glossary consistency:** 0.88
- **Overall section score:** 0.87

### Back-Translation (Key Paragraphs)

**First paragraph (back-translated):**
Meshes and points are the most common 3D scene representations because they are explicit and fit well with fast GPU/CUDA-based rasterization. In contrast, recent Neural Radiance Field (NeRF) methods rely on continuous scene representations, typically optimizing the Multi-Layer Perceptron (MLP) using volumetric ray tracing for generating new views of captured scenes. Similarly, the most efficient radiance field solutions to date rely on continuous representations through interpolating values stored in, for example, voxel grids [Fridovich-Keil and Yu et al. 2022] or hash [Müller et al. 2022] or points [Xu et al. 2022]. While the continuous nature of these methods helps in optimization, the random samples required for rendering are costly and can lead to noise. We present a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive training times, while our tile-based splatting solution ensures real-time rendering with advanced quality at 1080p resolution on several previously published datasets [Barron et al. 2022; Hedman et al. 2018; Knapitsch et al. 2017] (see Figure 1).

**Contributions (back-translated):**
• Introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields.
• An optimization method for 3D Gaussian properties, interleaved with adaptive density control that creates high-quality representations for captured scenes.
• A fast, differentiable rendering approach for GPUs, visibility-aware, allowing anisotropic splatting and fast backpropagation to achieve high-quality generation of new views.

**Assessment:** The back-translation preserves the technical meaning and structure of the original text with high fidelity. Minor variations in word choice do not affect semantic equivalence.
