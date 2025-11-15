# Section 2: Progressive Growing of GANs
## القسم 2: النمو التدريجي لشبكات GAN

**Section:** Methodology - Progressive Growing
**Translation Quality:** 0.87
**Glossary Terms Used:** generator (المولد), discriminator (المميز), training (تدريب), resolution (دقة), layers (طبقات), convolutional (التفافي), upsampling (رفع العينات), downsampling (تقليل العينات), fade in (الظهور التدريجي), transition (انتقال), stability (استقرار)

---

### English Version

Our primary contribution is a training methodology for GANs where we start with low-resolution images, and then progressively increase the resolution by adding layers to the networks as the training progresses. This allows the model to first learn the large-scale structure of the image distribution and then shift to finer-scale details, instead of having to simultaneously learn all the scales.

We start by training the networks at a very low spatial resolution (4×4 pixels), and then progressively add layers that introduce higher-resolution details as the training progresses. Both the generator and the discriminator are grown in synchrony. All existing layers remain trainable throughout the process. Figure 1 illustrates the progressive growing process in detail.

**Starting point (4×4).** We start with both the generator and the discriminator having only the layers that operate at 4×4 spatial resolution. The generator has a latent code input and produces 4×4 RGB images. The discriminator has 4×4 RGB images as input and produces a single scalar output representing the realness score.

**Adding higher resolution layers.** When the training has stabilized, we add a new layer to both the generator and the discriminator. In the generator, a new upsampling layer followed by a convolutional layer is added. The upsampling is done using nearest neighbor filtering followed by a 3×3 convolutional layer. In the discriminator, we add a new convolutional layer followed by a downsampling layer (implemented as 2×2 average pooling).

**Smooth transition.** When new layers are added to the networks, we fade them in smoothly, as illustrated in Figure 1. This avoids sudden shocks to the already well-trained, smaller-resolution layers. We implement this by using a linear interpolation parameter α that controls the influence of the new layer. When α = 0, the new layer has no effect and we have the original network. When α = 1, the new layer is fully integrated. During the transition phase, α grows linearly from 0 to 1.

More specifically, let's consider adding a new higher-resolution block to the generator. We denote the existing low-resolution block by G_low and the new high-resolution block by G_high. During the transition, the output is computed as:

$$y = (1-\\alpha) \\cdot \\text{upsample}(G_{low}(z)) + \\alpha \\cdot G_{high}(G_{low}(z))$$

where z is the latent code input, and the upsampling operation simply doubles the resolution using nearest neighbor filtering. The parameter α is increased linearly from 0 to 1 during the transition. An analogous procedure is used for the discriminator.

**Benefits of progressive growing.** The key insight is that the progressive setup has several benefits:

1. **Improved stability:** By starting with a low resolution, the model learns the overall structure first, which provides a stable foundation for higher-resolution details. This greatly reduces the likelihood of mode collapse and training instability.

2. **Faster training:** Early training at low resolution takes much less time than training directly at high resolution. Even though we need to go through several resolution stages, the cumulative training time is significantly reduced because most of the iterations happen at lower resolutions.

3. **Better image quality:** By learning the image distribution in a coarse-to-fine manner, the networks can discover the large-scale structure of the distribution more easily. This leads to higher quality results compared to training at the target resolution from the beginning.

The networks are trained with a standard GAN loss function. We use the Wasserstein GAN loss with gradient penalty (WGAN-GP) (Gulrajani et al., 2017) in our experiments, as it has been shown to provide improved training stability. However, our progressive training approach is compatible with any GAN loss function.

---

### النسخة العربية

مساهمتنا الأساسية هي منهجية تدريب لشبكات GAN حيث نبدأ بصور منخفضة الدقة، ثم نزيد الدقة تدريجياً بإضافة طبقات إلى الشبكات مع تقدم التدريب. يسمح هذا للنموذج بتعلم البنية واسعة النطاق لتوزيع الصورة أولاً، ثم الانتقال إلى التفاصيل الأدق، بدلاً من الاضطرار إلى تعلم جميع المقاييس في وقت واحد.

نبدأ بتدريب الشبكات عند دقة مكانية منخفضة جداً (4×4 بكسل)، ثم نضيف تدريجياً طبقات تقدم تفاصيل عالية الدقة مع تقدم التدريب. ينمو كل من المولد والمميز بشكل متزامن. تظل جميع الطبقات الموجودة قابلة للتدريب طوال العملية. يوضح الشكل 1 عملية النمو التدريجي بالتفصيل.

**نقطة البداية (4×4).** نبدأ بكل من المولد والمميز ولديهما فقط الطبقات التي تعمل عند دقة مكانية 4×4. المولد لديه إدخال رمز كامن وينتج صور RGB بدقة 4×4. المميز لديه صور RGB بدقة 4×4 كإدخال وينتج مخرجاً عددياً واحداً يمثل درجة الواقعية.

**إضافة طبقات ذات دقة أعلى.** عندما يستقر التدريب، نضيف طبقة جديدة لكل من المولد والمميز. في المولد، يتم إضافة طبقة رفع عينات جديدة متبوعة بطبقة التفافية. يتم رفع العينات باستخدام ترشيح الجار الأقرب متبوعاً بطبقة التفافية 3×3. في المميز، نضيف طبقة التفافية جديدة متبوعة بطبقة تقليل عينات (مُنفذة كتجميع متوسط 2×2).

**انتقال سلس.** عندما تُضاف طبقات جديدة إلى الشبكات، نجعلها تظهر تدريجياً بشكل سلس، كما هو موضح في الشكل 1. يتجنب هذا الصدمات المفاجئة للطبقات الأصغر دقة والمدربة جيداً بالفعل. ننفذ هذا باستخدام معامل استيفاء خطي α يتحكم في تأثير الطبقة الجديدة. عندما α = 0، الطبقة الجديدة ليس لها تأثير ولدينا الشبكة الأصلية. عندما α = 1، الطبقة الجديدة متكاملة بالكامل. خلال مرحلة الانتقال، ينمو α خطياً من 0 إلى 1.

بشكل أكثر تحديداً، دعنا نفكر في إضافة كتلة جديدة عالية الدقة إلى المولد. نشير إلى الكتلة منخفضة الدقة الحالية بـ G_low والكتلة الجديدة عالية الدقة بـ G_high. خلال الانتقال، يُحسب المخرج كما يلي:

$$y = (1-\\alpha) \\cdot \\text{upsample}(G_{low}(z)) + \\alpha \\cdot G_{high}(G_{low}(z))$$

حيث z هو إدخال الرمز الكامن، وعملية رفع العينات ببساطة تضاعف الدقة باستخدام ترشيح الجار الأقرب. يزداد المعامل α خطياً من 0 إلى 1 خلال الانتقال. يتم استخدام إجراء مماثل للمميز.

**فوائد النمو التدريجي.** الرؤية الأساسية هي أن الإعداد التدريجي له عدة فوائد:

1. **تحسين الاستقرار:** بالبدء بدقة منخفضة، يتعلم النموذج البنية الإجمالية أولاً، مما يوفر أساساً مستقراً للتفاصيل عالية الدقة. هذا يقلل بشكل كبير من احتمالية انهيار الأنماط وعدم استقرار التدريب.

2. **تدريب أسرع:** التدريب المبكر عند دقة منخفضة يستغرق وقتاً أقل بكثير من التدريب مباشرة عند دقة عالية. على الرغم من أننا بحاجة إلى المرور عبر عدة مراحل دقة، فإن وقت التدريب التراكمي يقل بشكل كبير لأن معظم التكرارات تحدث عند دقة أقل.

3. **جودة صورة أفضل:** من خلال تعلم توزيع الصورة بطريقة من الخشن إلى الناعم، يمكن للشبكات اكتشاف البنية واسعة النطاق للتوزيع بسهولة أكبر. يؤدي هذا إلى نتائج ذات جودة أعلى مقارنة بالتدريب عند الدقة المستهدفة من البداية.

يتم تدريب الشبكات باستخدام دالة خسارة GAN قياسية. نستخدم خسارة Wasserstein GAN مع عقوبة التدرج (WGAN-GP) (Gulrajani et al., 2017) في تجاربنا، حيث ثبت أنها توفر استقراراً محسناً للتدريب. ومع ذلك، فإن نهج التدريب التدريجي الخاص بنا متوافق مع أي دالة خسارة GAN.

---

### Translation Notes

- **Figures referenced:** Figure 1 (illustrating progressive growing process)
- **Key terms introduced:**
  - Progressive growing (النمو التدريجي)
  - Upsampling (رفع العينات)
  - Downsampling (تقليل العينات)
  - Fade in (الظهور التدريجي)
  - Nearest neighbor filtering (ترشيح الجار الأقرب)
  - Average pooling (تجميع متوسط)
  - Latent code (رمز كامن)
  - Realness score (درجة الواقعية)
  - WGAN-GP (Wasserstein GAN with gradient penalty)
  - Coarse-to-fine (من الخشن إلى الناعم)
- **Equations:** 1 main equation for smooth transition (fade-in formula)
- **Citations:** Reference to WGAN-GP (Gulrajani et al., 2017)
- **Special handling:**
  - Mathematical equation preserved in LaTeX format
  - Technical operations (upsampling, downsampling, pooling) translated consistently
  - Greek letter α kept in original form with Arabic explanation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
