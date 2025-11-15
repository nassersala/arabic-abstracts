# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** generative methods (طرق توليدية), deep learning (تعلم عميق), resolution (دقة), training (تدريب), generator (المولد), discriminator (المميز), convergence (تقارب), mode collapse (انهيار الأنماط), stability (استقرار)

---

### English Version

Generative methods that produce novel samples from high-dimensional data distributions, such as images, are finding widespread use, for example in speech synthesis (van den Oord et al., 2016), image-to-image translation (Zhu et al., 2017; Liu et al., 2017; Wang et al., 2017), and image inpainting (Iizuka et al., 2017). Currently the most prominent approaches are autoregressive models (van den Oord et al., 2016b; 2016a), variational autoencoders (VAE) (Kingma & Welling, 2014), and generative adversarial networks (GAN) (Goodfellow et al., 2014). Currently, GANs are capable of generating the highest quality samples.

The general training stability of GANs has improved significantly in recent years (Radford et al., 2016; Gulrajani et al., 2017; Berthelot et al., 2017; Kodali et al., 2017), but they continue to be difficult to train at high resolutions and for large datasets. The current solutions trade off the overall quality with faster training (Zhang et al., 2017; Nguyen et al., 2017) or focus on narrow distributions where less diversity is needed (Marchesi, 2017).

Our primary contribution is a training methodology for GANs where we start with low-resolution images, and then progressively increase the resolution by adding layers to the networks. This incremental nature allows the training to first discover large-scale structure of the image distribution and then shift attention to increasingly finer scale detail, instead of having to learn all scales simultaneously. We describe the approach in detail in Section 2.

Our second contribution is a simple way to increase the variation in generated images. We observe that the generator sometimes ignores some of the latent input variables. This creates entanglements where some combination of latent variables can lead to a single mode in the generated output. We propose adding a new term to the generator that actively encourages it to vary the generated images. The details are in Section 3.

We observe that mode collapse — a scenario where the generator produces a very limited variety of samples — is much less likely to occur when the training progresses stably. We also propose some implementation details that further improve the training stability. We parameterize the per-pixel feature vector norms in both generator and discriminator. We also introduce a simple way to scale the gradient magnitudes to achieve more balanced learning across the scales. We discuss these details in Section 4.

We also introduce a novel way to evaluate the results. Existing metrics like Inception score (Salimans et al., 2016) and Fréchet Inception Distance (FID) (Heusel et al., 2017) focus on quality but ignore variation, or vice versa. We propose to use multi-scale structural similarity (MS-SSIM) in conjunction with FID to separately evaluate both image quality and variation. Section 5 describes our approach.

Our contributions allow us to generate CelebA-HQ images at 1024² resolution with considerably better visual quality than previous methods. We also improve the best published Inception score on CIFAR10 from 7.90 to 8.80. The code, trained networks, and the CelebA-HQ dataset are available at https://github.com/tkarras/progressive_growing_of_gans.

---

### النسخة العربية

تجد الطرق التوليدية التي تنتج عينات جديدة من توزيعات البيانات عالية الأبعاد، مثل الصور، استخداماً واسع النطاق، على سبيل المثال في تركيب الكلام (van den Oord et al., 2016)، والترجمة من صورة إلى صورة (Zhu et al., 2017; Liu et al., 2017; Wang et al., 2017)، وإصلاح الصور (Iizuka et al., 2017). حالياً، النُهج الأكثر بروزاً هي النماذج الانحدارية الذاتية (van den Oord et al., 2016b; 2016a)، والمشفرات التلقائية التغايرية (VAE) (Kingma & Welling, 2014)، والشبكات الخصامية التوليدية (GAN) (Goodfellow et al., 2014). حالياً، تُعد شبكات GAN قادرة على توليد عينات بأعلى جودة.

لقد تحسن استقرار التدريب العام لشبكات GAN بشكل كبير في السنوات الأخيرة (Radford et al., 2016; Gulrajani et al., 2017; Berthelot et al., 2017; Kodali et al., 2017)، لكنها لا تزال صعبة التدريب عند الدقة العالية وعلى مجموعات البيانات الكبيرة. الحلول الحالية تتنازل عن الجودة الإجمالية مقابل تدريب أسرع (Zhang et al., 2017; Nguyen et al., 2017) أو تركز على توزيعات ضيقة حيث يلزم تنوع أقل (Marchesi, 2017).

مساهمتنا الأساسية هي منهجية تدريب لشبكات GAN حيث نبدأ بصور منخفضة الدقة، ثم نزيد الدقة تدريجياً بإضافة طبقات إلى الشبكات. تسمح هذه الطبيعة التدريجية للتدريب باكتشاف البنية واسعة النطاق لتوزيع الصورة أولاً، ثم تحويل الانتباه إلى تفاصيل أدق بشكل متزايد، بدلاً من الاضطرار إلى تعلم جميع المقاييس في وقت واحد. نصف النهج بالتفصيل في القسم 2.

مساهمتنا الثانية هي طريقة بسيطة لزيادة التنوع في الصور المولدة. نلاحظ أن المولد يتجاهل أحياناً بعض متغيرات الإدخال الكامنة. يؤدي هذا إلى تشابكات حيث يمكن لبعض مجموعات المتغيرات الكامنة أن تؤدي إلى نمط واحد في المخرجات المولدة. نقترح إضافة مصطلح جديد إلى المولد يشجعه بنشاط على تنويع الصور المولدة. التفاصيل موجودة في القسم 3.

نلاحظ أن انهيار الأنماط - وهو سيناريو حيث ينتج المولد مجموعة محدودة جداً من العينات - يكون أقل احتمالاً للحدوث عندما يتقدم التدريب بشكل مستقر. كما نقترح أيضاً بعض تفاصيل التنفيذ التي تحسن استقرار التدريب بشكل أكبر. نقوم بمعايرة معايير متجه الميزات لكل بكسل في كل من المولد والمميز. كما نقدم أيضاً طريقة بسيطة لقياس مقادير التدرج لتحقيق تعلم أكثر توازناً عبر المقاييس. نناقش هذه التفاصيل في القسم 4.

نقدم أيضاً طريقة جديدة لتقييم النتائج. تركز المقاييس الحالية مثل درجة Inception (Salimans et al., 2016) ومسافة Fréchet Inception (FID) (Heusel et al., 2017) على الجودة لكنها تتجاهل التنوع، أو العكس. نقترح استخدام التشابه الهيكلي متعدد المقاييس (MS-SSIM) بالاقتران مع FID لتقييم جودة الصورة والتنوع بشكل منفصل. يصف القسم 5 نهجنا.

تسمح لنا مساهماتنا بتوليد صور CelebA-HQ بدقة 1024² بجودة بصرية أفضل بكثير من الطرق السابقة. كما نحسن أيضاً أفضل درجة Inception منشورة على CIFAR10 من 7.90 إلى 8.80. الكود والشبكات المدربة ومجموعة بيانات CelebA-HQ متاحة على https://github.com/tkarras/progressive_growing_of_gans.

---

### Translation Notes

- **Figures referenced:** None directly in introduction
- **Key terms introduced:**
  - Autoregressive models (النماذج الانحدارية الذاتية)
  - Variational autoencoders/VAE (المشفرات التلقائية التغايرية)
  - Mode collapse (انهيار الأنماط)
  - Latent variables (متغيرات كامنة)
  - Multi-scale structural similarity/MS-SSIM (التشابه الهيكلي متعدد المقاييس)
  - Fréchet Inception Distance/FID (مسافة Fréchet Inception)
- **Equations:** None in introduction
- **Citations:** 17 references cited
- **Special handling:**
  - Kept dataset names (CelebA-HQ, CIFAR10) and metric names (Inception score, FID, MS-SSIM) as proper nouns
  - Preserved GitHub URL
  - Maintained citation format

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
