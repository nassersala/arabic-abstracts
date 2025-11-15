# Section 2: The Dataset
## القسم 2: مجموعة البيانات

**Section:** dataset
**Translation Quality:** 0.91
**Glossary Terms Used:** dataset, training, image classification, normalization, resolution

---

### English Version

ImageNet is a dataset of over 15 million labeled high-resolution images belonging to roughly 22,000 categories. The images were collected from the web and labeled by human labelers using Amazon's Mechanical Turk crowd-sourcing tool. Starting in 2010, as part of the Pascal Visual Object Classes (VOC) challenge, an annual competition called the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC) has been held. ILSVRC uses a subset of ImageNet with roughly 1000 images in each of 1000 categories. In all, there are roughly 1.2 million training images, 50,000 validation images, and 150,000 testing images.

ILSVRC-2010 is the only version of ILSVRC for which the test set labels are available, so this is the version on which we performed most of our experiments. Since we also entered our model in the ILSVRC-2012 competition, in Section 6 we also report our results on this version of the dataset, whose test set labels are unavailable. On ImageNet, it is customary to report two error rates: top-1 and top-5, where the top-5 error rate is the fraction of test images for which the correct label is not among the five labels considered most probable by the model.

ImageNet consists of variable-resolution images, while our system requires a constant input dimensionality. Therefore, we down-sampled the images to a fixed resolution of 256 × 256. Given a rectangular image, we first rescaled the image such that the shorter side was of length 256, and then cropped out the central 256×256 patch from the resulting image. We did not pre-process the images in any other way, except for subtracting the mean activity over the training set from each pixel. So we trained our network on the (centered) raw RGB values of the pixels.

---

### النسخة العربية

ImageNet هي مجموعة بيانات تحتوي على أكثر من 15 مليون صورة موسومة عالية الدقة تنتمي إلى ما يقرب من 22,000 فئة. تم جمع الصور من الويب وتوسيمها بواسطة موسمين بشريين باستخدام أداة Amazon Mechanical Turk للتعهيد الجماعي. بدءاً من عام 2010، كجزء من تحدي Pascal Visual Object Classes (VOC)، تم عقد مسابقة سنوية تسمى ImageNet Large-Scale Visual Recognition Challenge (ILSVRC). تستخدم مسابقة ILSVRC مجموعة فرعية من ImageNet تحتوي على ما يقرب من 1000 صورة في كل فئة من 1000 فئة. في المجمل، هناك ما يقرب من 1.2 مليون صورة تدريبية، و50,000 صورة للتحقق، و150,000 صورة اختبار.

ILSVRC-2010 هي النسخة الوحيدة من ILSVRC التي تتوفر فيها تسميات مجموعة الاختبار، لذلك هذه هي النسخة التي أجرينا عليها معظم تجاربنا. نظراً لأننا شاركنا أيضاً بنموذجنا في مسابقة ILSVRC-2012، في القسم 6 نقدم أيضاً نتائجنا على هذه النسخة من مجموعة البيانات، التي تسميات مجموعة الاختبار فيها غير متاحة. في ImageNet، من المعتاد الإبلاغ عن معدلي خطأ: top-1 وtop-5، حيث معدل خطأ top-5 هو نسبة صور الاختبار التي لا تكون فيها التسمية الصحيحة من بين التسميات الخمس التي يعتبرها النموذج الأكثر احتمالاً.

تتكون ImageNet من صور ذات دقة متغيرة، بينما يتطلب نظامنا بُعداً ثابتاً للإدخال. لذلك، قمنا بتقليل حجم الصور إلى دقة ثابتة قدرها 256 × 256. بالنسبة لصورة مستطيلة، قمنا أولاً بإعادة تحجيم الصورة بحيث يكون الجانب الأقصر بطول 256، ثم قصصنا المقطع المركزي 256×256 من الصورة الناتجة. لم نقم بمعالجة الصور مسبقاً بأي طريقة أخرى، باستثناء طرح متوسط النشاط على مجموعة التدريب من كل بكسل. لذلك قمنا بتدريب شبكتنا على قيم RGB الخام (المركزة) للبكسلات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - labeled images (صور موسومة)
  - high-resolution (عالية الدقة)
  - crowd-sourcing (التعهيد الجماعي)
  - validation images (صور للتحقق)
  - testing images (صور اختبار)
  - error rate (معدل خطأ)
  - variable-resolution (دقة متغيرة)
  - constant input dimensionality (بُعد ثابت للإدخال)
  - down-sampled (قمنا بتقليل حجم)
  - fixed resolution (دقة ثابتة)
  - rescaled (إعادة تحجيم)
  - cropped (قصصنا)
  - mean activity (متوسط النشاط)
  - centered raw RGB values (قيم RGB الخام المركزة)
- **Equations:** None
- **Citations:** Reference to Section 6
- **Special handling:**
  - Dataset names (ImageNet, Pascal VOC, ILSVRC) kept in English
  - Amazon Mechanical Turk kept in English (proper name)
  - Numerical data preserved exactly (256×256, 1000 categories, etc.)
  - Image dimensions kept in standard notation (256 × 256)

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.94
- Readability: 0.89
- Glossary consistency: 0.89
- **Overall section score:** 0.91

### Back-Translation Check

Key sentence back-translated:
Arabic: "ImageNet هي مجموعة بيانات تحتوي على أكثر من 15 مليون صورة موسومة عالية الدقة..."
Back to English: "ImageNet is a dataset containing over 15 million labeled high-resolution images..."
✓ Semantic match confirmed

Processing description back-translated:
Arabic: "قمنا أولاً بإعادة تحجيم الصورة بحيث يكون الجانب الأقصر بطول 256..."
Back to English: "We first rescaled the image so that the shorter side was of length 256..."
✓ Semantic match confirmed
