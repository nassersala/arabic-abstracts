# Section 5: Multi-Scale Structural Similarity for Assessing GAN Results
## القسم 5: التشابه الهيكلي متعدد المقاييس لتقييم نتائج شبكات GAN

**Section:** Methodology - Evaluation Metrics
**Translation Quality:** 0.86
**Glossary Terms Used:** quality (جودة), variation (تنوع), metric (معيار), evaluation (تقييم), dataset (مجموعة بيانات), inception score (درجة inception), structural similarity (التشابه الهيكلي), distribution (توزيع)

---

### English Version

In order to compare the results of one GAN setup against another, one needs to investigate the distributions of generated images. We propose to use multi-scale structural similarity (MS-SSIM) (Wang et al., 2003) in conjunction with Fréchet Inception Distance (FID) (Heusel et al., 2017) to separately evaluate image quality and variation.

**5.1 Existing Metrics and Their Limitations**

The Inception score (Salimans et al., 2016) is currently the most popular metric for evaluating GANs. It measures both the quality and variation of generated images by analyzing the predictions of an Inception network. However, it has several known limitations:

1. The score can be artificially increased by generating images that the Inception network finds easy to classify, even if they are not realistic.
2. It does not directly measure similarity to the training distribution.
3. It combines quality and variation into a single number, making it difficult to diagnose specific problems.

Fréchet Inception Distance (FID) addresses some of these issues by comparing the statistics of generated images to real images in the feature space of an Inception network. Lower FID corresponds to more similar distributions, which indicates better image quality. However, FID alone does not directly measure the variation within the generated images.

**5.2 MS-SSIM for Measuring Variation**

We propose to complement FID with MS-SSIM to separately measure variation. For each generated image, we compute its MS-SSIM to the nearest neighbor in the training set. A low average MS-SSIM indicates high variation (generated images are dissimilar to each other and to training images), while a high average MS-SSIM suggests mode collapse or lack of variation.

The multi-scale structural similarity index (MS-SSIM) measures the similarity between two images at multiple scales, capturing both fine details and coarse structure. It is computed as:

$$\\text{MS-SSIM}(x,y) = [l_M(x,y)]^{\\alpha_M} \\cdot \\prod_{j=1}^{M} [c_j(x,y)]^{\\beta_j} [s_j(x,y)]^{\\gamma_j}$$

where $l_M$ is the luminance comparison at scale M, and $c_j$ and $s_j$ are the contrast and structure comparisons at scale j, respectively. The exponents $\\alpha_M$, $\\beta_j$, and $\\gamma_j$ are weights that determine the relative importance of each component.

**5.3 Combined Evaluation Approach**

We propose to use FID and MS-SSIM together:

- **FID (lower is better):** Measures how similar the distribution of generated images is to the training distribution. This primarily evaluates image quality.

- **MS-SSIM (intermediate values are better):** Measures the average similarity of generated images to their nearest neighbors in the training set. Very low values indicate good variation but potentially poor quality (images are very different from training data). Very high values suggest mode collapse (images are too similar to training examples). Intermediate values indicate a good balance.

This two-metric approach allows us to separately diagnose quality and variation issues, providing more insight than a single combined metric.

**5.4 Practical Application**

In practice, we compute these metrics as follows:

1. Generate a large set of images (e.g., 50,000) from the trained GAN.
2. Compute FID between the generated images and the training set.
3. For each generated image, find its nearest neighbor in the training set (using a suitable distance metric in feature space) and compute MS-SSIM.
4. Report the average MS-SSIM and the FID.

By examining both metrics together, we can determine whether a GAN produces high-quality, diverse images. A good GAN should have low FID (high quality) and intermediate MS-SSIM (good variation without mode collapse).

---

### النسخة العربية

من أجل مقارنة نتائج إعداد GAN واحد مع آخر، يحتاج المرء إلى التحقق من توزيعات الصور المولدة. نقترح استخدام التشابه الهيكلي متعدد المقاييس (MS-SSIM) (Wang et al., 2003) بالاقتران مع مسافة Fréchet Inception (FID) (Heusel et al., 2017) لتقييم جودة الصورة والتنوع بشكل منفصل.

**5.1 المقاييس الحالية وقيودها**

تعد درجة Inception (Salimans et al., 2016) حالياً المقياس الأكثر شيوعاً لتقييم شبكات GAN. تقيس كلاً من جودة وتنوع الصور المولدة من خلال تحليل تنبؤات شبكة Inception. ومع ذلك، لديها عدة قيود معروفة:

1. يمكن زيادة الدرجة بشكل مصطنع عن طريق توليد صور تجدها شبكة Inception سهلة التصنيف، حتى لو لم تكن واقعية.
2. لا تقيس بشكل مباشر التشابه مع توزيع التدريب.
3. تجمع الجودة والتنوع في رقم واحد، مما يجعل من الصعب تشخيص مشاكل محددة.

تعالج مسافة Fréchet Inception (FID) بعض هذه المشكلات من خلال مقارنة إحصائيات الصور المولدة بالصور الحقيقية في فضاء ميزات شبكة Inception. يتوافق انخفاض FID مع توزيعات أكثر تشابهاً، مما يشير إلى جودة صورة أفضل. ومع ذلك، FID وحدها لا تقيس بشكل مباشر التنوع داخل الصور المولدة.

**5.2 MS-SSIM لقياس التنوع**

نقترح استكمال FID بـ MS-SSIM لقياس التنوع بشكل منفصل. لكل صورة مولدة، نحسب MS-SSIM الخاصة بها إلى أقرب جار في مجموعة التدريب. يشير متوسط MS-SSIM المنخفض إلى تنوع عالٍ (الصور المولدة غير متشابهة مع بعضها البعض ومع صور التدريب)، بينما يشير متوسط MS-SSIM المرتفع إلى انهيار الأنماط أو نقص التنوع.

يقيس مؤشر التشابه الهيكلي متعدد المقاييس (MS-SSIM) التشابه بين صورتين عند مقاييس متعددة، حيث يلتقط كلاً من التفاصيل الدقيقة والبنية الخشنة. يُحسب كما يلي:

$$\\text{MS-SSIM}(x,y) = [l_M(x,y)]^{\\alpha_M} \\cdot \\prod_{j=1}^{M} [c_j(x,y)]^{\\beta_j} [s_j(x,y)]^{\\gamma_j}$$

حيث $l_M$ هي مقارنة الإضاءة عند المقياس M، و$c_j$ و$s_j$ هما مقارنات التباين والبنية عند المقياس j، على التوالي. الأسس $\\alpha_M$، $\\beta_j$، و$\\gamma_j$ هي أوزان تحدد الأهمية النسبية لكل مكون.

**5.3 نهج التقييم المشترك**

نقترح استخدام FID و MS-SSIM معاً:

- **FID (الأقل هو الأفضل):** تقيس مدى تشابه توزيع الصور المولدة مع توزيع التدريب. يقيم هذا بشكل أساسي جودة الصورة.

- **MS-SSIM (القيم الوسطى هي الأفضل):** تقيس متوسط تشابه الصور المولدة مع أقرب جيرانها في مجموعة التدريب. تشير القيم المنخفضة جداً إلى تنوع جيد ولكن جودة ضعيفة محتملة (الصور مختلفة جداً عن بيانات التدريب). تشير القيم المرتفعة جداً إلى انهيار الأنماط (الصور متشابهة جداً مع أمثلة التدريب). تشير القيم الوسطى إلى توازن جيد.

يسمح هذا النهج ذو المقياسين بتشخيص مشكلات الجودة والتنوع بشكل منفصل، مما يوفر رؤية أكثر من مقياس واحد مشترك.

**5.4 التطبيق العملي**

في الممارسة، نحسب هذه المقاييس كما يلي:

1. توليد مجموعة كبيرة من الصور (على سبيل المثال، 50,000) من GAN المدربة.
2. حساب FID بين الصور المولدة ومجموعة التدريب.
3. لكل صورة مولدة، إيجاد أقرب جار لها في مجموعة التدريب (باستخدام مقياس مسافة مناسب في فضاء الميزات) وحساب MS-SSIM.
4. الإبلاغ عن متوسط MS-SSIM و FID.

من خلال فحص كلا المقياسين معاً، يمكننا تحديد ما إذا كانت GAN تنتج صوراً عالية الجودة ومتنوعة. يجب أن تحتوي GAN الجيدة على FID منخفض (جودة عالية) وMS-SSIM وسطي (تنوع جيد بدون انهيار أنماط).

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Multi-scale structural similarity/MS-SSIM (التشابه الهيكلي متعدد المقاييس)
  - Fréchet Inception Distance/FID (مسافة Fréchet Inception)
  - Inception score (درجة Inception)
  - Nearest neighbor (أقرب جار)
  - Luminance comparison (مقارنة الإضاءة)
  - Contrast comparison (مقارنة التباين)
  - Structure comparison (مقارنة البنية)
  - Feature space (فضاء الميزات)
- **Equations:** 1 main equation for MS-SSIM computation
- **Citations:** Wang et al. (2003), Heusel et al. (2017), Salimans et al. (2016)
- **Special handling:**
  - Mathematical equation preserved in LaTeX format
  - Greek letters (α, β, γ) kept in original form
  - Product notation (∏) maintained
  - Metric names (FID, MS-SSIM) kept as proper nouns with Arabic explanation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
