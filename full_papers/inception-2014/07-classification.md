# Section 7: ILSVRC 2014 Classification Challenge Setup and Results
## القسم 7: إعداد ونتائج تحدي التصنيف ILSVRC 2014

**Section:** ILSVRC 2014 Classification Challenge
**Translation Quality:** 0.89
**Glossary Terms Used:** classification, validation, test, top-1 accuracy, top-5 error, ensemble, multi-scale cropping, benchmark, dataset

---

### English Version

The ILSVRC 2014 classification challenge involves the task of classifying the image into one of 1000 leaf-node categories in the Imagenet hierarchy. There are about 1.2 million images for training, 50,000 for validation and 100,000 images for testing. Each image is associated with one ground truth category, and performance is measured based on the highest scoring classifier predictions. Two numbers are usually reported: the top-1 accuracy rate, which compares the ground truth against the first predicted class, and the top-5 error rate, which compares the ground truth against the first 5 predicted classes: an image is deemed correctly classified if the ground truth is among the top-5, regardless of its rank in them. The challenge uses the top-5 error rate for ranking purposes.

We participated in the challenge with no external data used for training. In addition to the training techniques aforementioned in this paper, we adopted a set of techniques during testing to obtain a higher performance, which we elaborate below.

1. We independently trained 7 versions of the same GoogLeNet model (including one wider version), and performed ensemble prediction with them. These models were trained with the same initialization (even with the same initial weights, mainly because of an oversight) and learning rate policies, and they only differ in sampling methodologies and the random order in which they see input images.

2. During testing, we adopted a more aggressive cropping approach than that of Krizhevsky et al. [9]. Specifically, we resize the image to 4 scales where the shorter dimension (height or width) is 256, 288, 320 and 352 respectively, take the left, center and right square of these resized images (in the case of portrait images, we take the top, center and bottom squares). For each square, we then take the 4 corners and the center 224×224 crop as well as the square resized to 224×224, and their mirrored versions. This results in 4×3×6×2 = 144 crops per image. A similar approach was used by Andrew Howard [8] in the previous year's entry, which we empirically verified to perform slightly worse than the proposed scheme. We note that such aggressive cropping may not be necessary in real applications, as the benefit of more crops becomes marginal after a reasonable number of crops are present (as we will show later on).

3. The softmax probabilities are averaged over multiple crops and over all the individual classifiers to obtain the final prediction. In our experiments we analyzed alternative approaches on the validation data, such as max pooling over crops and averaging over classifiers, but they lead to inferior performance than the simple averaging.

In the remainder of this paper, we analyze the multiple factors that contribute to the overall performance of the final submission.

Our final submission in the challenge obtains a top-5 error of 6.67% on both the validation and testing data, ranking the first among other participants. This is a 56.5% relative reduction compared to the SuperVision approach in 2012, and about 40% relative reduction compared to the previous year's best approach (Clarifai), both of which used external data for training the classifiers. The following table shows the statistics of some of the top-performing approaches.

We also analyze and report the performance of multiple testing choices, by varying the number of models and the number of crops used when predicting an image in the following table. When we use one model, we chose the one with the lowest top-1 error rate on the validation data. All numbers are reported on the validation dataset in order to not overfit to the test set statistics.

---

### النسخة العربية

يتضمن تحدي التصنيف ILSVRC 2014 مهمة تصنيف الصورة إلى واحدة من 1000 فئة من فئات العقد الطرفية في التسلسل الهرمي لـ ImageNet. هناك حوالي 1.2 مليون صورة للتدريب، و50,000 للتحقق، و100,000 صورة للاختبار. كل صورة مرتبطة بفئة حقيقة أرضية واحدة، ويتم قياس الأداء بناءً على تنبؤات المصنف الأعلى تسجيلاً. عادةً ما يتم الإبلاغ عن رقمين: معدل دقة top-1، الذي يقارن الحقيقة الأرضية مع الفئة المتنبأ بها الأولى، ومعدل خطأ top-5، الذي يقارن الحقيقة الأرضية مع الفئات الخمس المتنبأ بها الأولى: تُعتبر الصورة مصنفة بشكل صحيح إذا كانت الحقيقة الأرضية من بين الـ top-5، بغض النظر عن ترتيبها فيها. يستخدم التحدي معدل خطأ top-5 لأغراض الترتيب.

شاركنا في التحدي دون استخدام بيانات خارجية للتدريب. بالإضافة إلى تقنيات التدريب المذكورة سابقاً في هذا البحث، اعتمدنا مجموعة من التقنيات أثناء الاختبار للحصول على أداء أعلى، والتي نوضحها أدناه.

1. قمنا بتدريب 7 إصدارات بشكل مستقل من نفس نموذج GoogLeNet (بما في ذلك إصدار واحد أوسع)، وأجرينا تنبؤات مجموعات (ensemble) معهم. تم تدريب هذه النماذج بنفس التهيئة (حتى بنفس الأوزان الأولية، بشكل رئيسي بسبب إغفال) وسياسات معدل التعلم، وهي تختلف فقط في منهجيات أخذ العينات والترتيب العشوائي الذي ترى به صور الإدخال.

2. أثناء الاختبار، اعتمدنا نهج قص أكثر قوة من نهج Krizhevsky وآخرين [9]. على وجه التحديد، نقوم بتغيير حجم الصورة إلى 4 مقاييس حيث يكون البُعد الأقصر (الارتفاع أو العرض) 256 و288 و320 و352 على التوالي، ونأخذ المربع الأيسر والأوسط والأيمن لهذه الصور المُعاد حجمها (في حالة الصور الطولية، نأخذ المربعات العلوية والوسطى والسفلية). لكل مربع، نأخذ بعد ذلك الزوايا الأربع والقص المركزي 224×224 بالإضافة إلى المربع المُعاد حجمه إلى 224×224، ونسخها المعكوسة. ينتج عن هذا 4×3×6×2 = 144 قصاً لكل صورة. تم استخدام نهج مماثل من قبل Andrew Howard [8] في مشاركة العام السابق، والذي تحققنا تجريبياً من أنه يؤدي بشكل أسوأ قليلاً من المخطط المقترح. نلاحظ أن مثل هذا القص القوي قد لا يكون ضرورياً في التطبيقات الحقيقية، حيث تصبح فائدة المزيد من القصات هامشية بعد وجود عدد معقول من القصات (كما سنوضح لاحقاً).

3. يتم حساب متوسط احتماليات softmax على قصات متعددة وعلى جميع المصنفات الفردية للحصول على التنبؤ النهائي. في تجاربنا، قمنا بتحليل نُهج بديلة على بيانات التحقق، مثل التجميع الأقصى على القصات والمتوسط على المصنفات، لكنها تؤدي إلى أداء أدنى من المتوسط البسيط.

في ما تبقى من هذا البحث، نحلل العوامل المتعددة التي تساهم في الأداء العام للتقديم النهائي.

يحصل تقديمنا النهائي في التحدي على خطأ top-5 بنسبة 6.67٪ على كل من بيانات التحقق والاختبار، ليحتل المرتبة الأولى بين المشاركين الآخرين. هذا تخفيض نسبي بنسبة 56.5٪ مقارنة بنهج SuperVision في عام 2012، وحوالي 40٪ تخفيض نسبي مقارنة بأفضل نهج في العام السابق (Clarifai)، وكلاهما استخدم بيانات خارجية لتدريب المصنفات. يوضح الجدول التالي إحصاءات بعض النُهج ذات الأداء الأفضل.

نحلل أيضاً ونبلّغ عن أداء خيارات اختبار متعددة، من خلال تنويع عدد النماذج وعدد القصات المستخدمة عند التنبؤ بصورة في الجدول التالي. عندما نستخدم نموذجاً واحداً، نختار النموذج ذو أقل معدل خطأ top-1 على بيانات التحقق. يتم الإبلاغ عن جميع الأرقام على مجموعة بيانات التحقق حتى لا نفرط في التكيف مع إحصاءات مجموعة الاختبار.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Multiple tables mentioned but not shown
- **Key terms introduced:** ImageNet hierarchy, leaf-node categories, ground truth, top-1 accuracy, top-5 error, ensemble prediction, aggressive cropping, multi-scale testing, mirrored versions, softmax probabilities
- **Equations:** Mathematical expression for crops: 4×3×6×2 = 144
- **Citations:** [8], [9]
- **Special handling:**
  - Kept "ILSVRC 2014" and "ImageNet" as proper nouns
  - Translated "ground truth" as "الحقيقة الأرضية"
  - Kept "top-1" and "top-5" with English terms
  - Kept "softmax" as English term
  - Kept "ensemble" with Arabic translation "مجموعات" in parentheses
  - Translated "cropping" as "قص"
  - Kept competitor names in English: SuperVision, Clarifai, GoogLeNet
  - Translated "validation" as "التحقق" and "testing" as "الاختبار"
  - Kept mathematical dimensions like "224×224", "256, 288, 320, 352" unchanged
  - Translated "mirrored versions" as "نسخها المعكوسة"

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
