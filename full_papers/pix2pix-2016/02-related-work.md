# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.86
**Glossary Terms Used:** structured loss, per-pixel, classification, regression, L1 loss, L2 loss, conditional GAN, encoder-decoder, architecture, image-to-image translation

---

### English Version

**Structured losses for image modeling.** Image-to-image translation problems are often formulated as per-pixel classification or regression (e.g., [32, 48, 64]). These formulations treat the output space as "unstructured" in the sense that each output pixel is considered conditionally independent from all others given the input image. Conditional GANs instead learn a structured loss. Structured losses penalize the joint configuration of the output. A large body of literature has considered losses of this kind, with popular methods including conditional random fields [3], the SSIM metric [63], feature matching [16], nonparametric losses [30], the convolutional pseudo-prior [66], and losses based on matching covariance statistics [31]. The conditional GAN is different in that the loss is learned, and can, in theory, penalize any possible structure that differs between output and target.

**Conditional GANs.** We are not the first to apply GANs in the conditional setting. Prior and concurrent works have conditioned GANs on discrete labels [44, 53], text [51], and images [27, 43, 55, 61]. The image-conditional models closest to our work are those of [61] and [27]. However, our approach differs in several architectural choices for the generator and discriminator. Unlike prior work, for our generator we use a "U-Net"-based architecture [52], and for our discriminator we use a convolutional "PatchGAN" classifier, which only penalizes structure at the scale of image patches. A similar PatchGAN architecture was previously proposed by [38] for the purpose of capturing local style statistics. Here we show that this approach is effective on a wider range of problems, and we investigate the effect of changing the patch size.

Other recent work has also used GANs for image-to-image mappings. For example, [65] used a GAN to map between satellite and map views, and [27] used GANs for super-resolution. [35] uses a conditional GAN for video prediction, and [62] applies GANs to 3D modeling. However, each of these papers focus on a specific application, while our framework is general purpose.

**Image-to-image translation using CNNs.** Many vision and graphics tasks have been tackled with CNNs in a supervised setting [14, 15, 25, 28, 57]. Since our method is also supervised, we include discussion of unsupervised methods in the supplemental material. Image-to-image networks generally take the form of an encoder-decoder [25, 57], or its variant the skip connection encoder-decoder [52] ("U-Net"). CNNs have also been applied in settings where the goal is to predict a normal map, depth, or semantic labels from a single color image (e.g., [14, 15, 32, 36, 39, 64]). These works typically define a loss between the output and ground truth and directly backpropagate through the network. Such approaches benefit from defining specialized loss functions, with some losses being specific to a particular application. Our goal, in contrast, is to sidestep the need to specify such losses.

---

### النسخة العربية

**الخسائر المُهيكَلة لنمذجة الصور.** غالباً ما تُصاغ مسائل الترجمة من صورة إلى صورة كتصنيف أو انحدار على مستوى البكسل (Per-pixel Classification or Regression) (مثل [32، 48، 64]). تعامل هذه الصياغات فضاء المخرجات على أنه "غير مُهيكل" بمعنى أن كل بكسل مخرج يُعتبر مستقلاً شرطياً عن جميع البكسلات الأخرى بالنظر إلى الصورة المدخلة. في المقابل، تتعلم الشبكات التنافسية التوليدية المشروطة خسارة مُهيكَلة. تعاقب الخسائر المُهيكَلة التكوين المشترك للمخرجات. نظر عدد كبير من الأدبيات في خسائر من هذا النوع، مع طرق شائعة تشمل الحقول العشوائية المشروطة (Conditional Random Fields) [3]، ومقياس SSIM [63]، ومطابقة الخصائص (Feature Matching) [16]، والخسائر اللامعلمية (Nonparametric Losses) [30]، والتوزيع السابق الشبه تلافيفي (Convolutional Pseudo-prior) [66]، والخسائر المبنية على مطابقة إحصائيات التباين المشترك [31]. تختلف الشبكة التنافسية التوليدية المشروطة في أن الخسارة مُتعلَّمة، ويمكنها، نظرياً، معاقبة أي بنية محتملة تختلف بين المخرجات والهدف.

**الشبكات التنافسية التوليدية المشروطة.** لسنا الأوائل في تطبيق الشبكات التنافسية التوليدية في السياق المشروط. شرطت أعمال سابقة ومتزامنة الشبكات التنافسية التوليدية على تسميات منفصلة [44، 53]، ونصوص [51]، وصور [27، 43، 55، 61]. النماذج المشروطة بالصور الأقرب لعملنا هي تلك الموجودة في [61] و[27]. ومع ذلك، يختلف نهجنا في عدة خيارات معمارية للمولّد والمميّز. على عكس الأعمال السابقة، نستخدم للمولّد معمارية قائمة على "U-Net" [52]، وللمميّز نستخدم مصنف "PatchGAN" التلافيفي، الذي يعاقب فقط البنية على مستوى رقع الصورة (Image Patches). تم اقتراح معمارية PatchGAN مماثلة سابقاً بواسطة [38] لغرض التقاط إحصائيات الأسلوب المحلي. هنا نُظهر أن هذا النهج فعال على نطاق أوسع من المسائل، ونستكشف تأثير تغيير حجم الرقعة.

استخدمت أعمال حديثة أخرى أيضاً الشبكات التنافسية التوليدية لتعيينات من صورة إلى صورة. على سبيل المثال، استخدم [65] شبكة تنافسية توليدية للتعيين بين منظر الأقمار الصناعية ومنظر الخرائط، واستخدم [27] الشبكات التنافسية التوليدية للتحسين الفائق (Super-resolution). يستخدم [35] شبكة تنافسية توليدية مشروطة للتنبؤ بالفيديو، ويطبق [62] الشبكات التنافسية التوليدية على النمذجة ثلاثية الأبعاد. ومع ذلك، تركز كل من هذه الأوراق على تطبيق محدد، بينما إطار عملنا عام الغرض.

**الترجمة من صورة إلى صورة باستخدام الشبكات العصبية التلافيفية.** تمت معالجة العديد من مهام الرؤية والرسومات بالشبكات العصبية التلافيفية في سياق موجَّه (Supervised Setting) [14، 15، 25، 28، 57]. نظراً لأن طريقتنا أيضاً موجَّهة، نُدرج مناقشة الطرق غير الموجَّهة في المادة التكميلية. تتخذ شبكات الترجمة من صورة إلى صورة عموماً شكل مشفر-فك تشفير (Encoder-Decoder) [25، 57]، أو متغيره مشفر-فك تشفير بوصلات التخطي (Skip Connection Encoder-Decoder) [52] ("U-Net"). كما طُبقت الشبكات العصبية التلافيفية في سياقات يكون فيها الهدف هو التنبؤ بخريطة الأسطح العمودية (Normal Map)، أو العمق، أو التسميات الدلالية من صورة ملونة واحدة (مثل [14، 15، 32، 36، 39، 64]). تحدد هذه الأعمال عادةً خسارة بين المخرجات والحقيقة الأرضية (Ground Truth) وتنشر الخطأ عكسياً مباشرة عبر الشبكة. تستفيد هذه الأساليب من تعريف دوال خسارة متخصصة، مع بعض الخسائر الخاصة بتطبيق معين. هدفنا، في المقابل، هو تجاوز الحاجة إلى تحديد مثل هذه الخسائر.

---

### Translation Notes

- **Key terms introduced:**
  - Structured loss (خسارة مُهيكَلة)
  - Per-pixel classification (تصنيف على مستوى البكسل)
  - Conditional Random Fields (الحقول العشوائية المشروطة)
  - Feature matching (مطابقة الخصائص)
  - PatchGAN (مصنف رقع الصورة)
  - U-Net (معمارية U-Net)
  - Image patches (رقع الصورة)
  - Super-resolution (التحسين الفائق)
  - Encoder-decoder (مشفر-فك تشفير)
  - Skip connections (وصلات التخطي)
  - Normal map (خريطة الأسطح العمودية)
  - Ground truth (الحقيقة الأرضية)
  - Supervised setting (سياق موجَّه)

- **Equations:** 0
- **Citations:** Multiple references [3, 14, 15, 16, 25, 27, 28, 30, 31, 32, 36, 38, 39, 43, 44, 48, 51, 52, 53, 55, 57, 61, 62, 63, 64, 65, 66]
- **Special handling:**
  - Maintained technical terminology consistency with previous sections
  - Preserved citation format
  - Kept acronyms like SSIM, U-Net, PatchGAN in English with Arabic explanations

- **Translation choices:**
  - "structured loss" → "خسارة مُهيكَلة" (emphasizing the structured nature)
  - "unstructured" → "غير مُهيكل"
  - "per-pixel" → "على مستوى البكسل"
  - "joint configuration" → "التكوين المشترك"
  - "image patches" → "رقع الصورة"
  - "general purpose" → "عام الغرض"
  - "supervised setting" → "سياق موجَّه"
  - "ground truth" → "الحقيقة الأرضية"

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

---

### Quality Assessment

The translation effectively presents the related work context, distinguishing the pix2pix approach from prior methods. It covers three main areas: structured losses, conditional GANs, and CNN-based image-to-image translation. The translation maintains technical precision while explaining complex concepts in formal Arabic. The score reflects the high quality of the translation with room for minor improvements in flow.
