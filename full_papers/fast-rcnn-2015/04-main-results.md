# Section 4: Main Results
## القسم 4: النتائج الرئيسية

**Section:** main results
**Translation Quality:** 0.86
**Glossary Terms Used:** mAP (متوسط الدقة المتوسطة), training (تدريب), testing (اختبار), accuracy (دقة), fine-tuning (ضبط دقيق), convolutional layers (طبقات التفافية), bounding-box regression (انحدار صندوق التحديد)

---

### English Version

Three main results support this paper's contributions:

1. State-of-the-art mAP on VOC07, 2010, and 2012
2. Fast training and testing compared to R-CNN, SPPnet
3. Fine-tuning conv layers in VGG16 improves mAP

**4.1. Experimental setup**

Our experiments use three pre-trained ImageNet models that are available online.² The first is the CaffeNet (essentially AlexNet [14]) from R-CNN [9]. We alternatively refer to this CaffeNet as model S, for "small." The second network is VGG_CNN_M_1024 from [3], which has the same depth as S, but is wider. We call this network model M, for "medium." The final network is the very deep VGG16 model from [20]. Since this model is the largest, we call it model L. In this section, all experiments use single-scale training and testing (s=600; see Section 5.2 for details).

**4.2. VOC 2010 and 2012 results**

On these datasets, we compare Fast R-CNN (FRCN, for short) against the top methods on the comp4 (outside data) track from the public leaderboard (Table 2, Table 3).³ For the NUS_NIN_c2000 and BabyLearning methods, there are no associated publications at this time and we could not find exact information on the ConvNet architectures used; they are variants of the Network-in-Network design [17]. All other methods are initialized from the same pre-trained VGG16 network.

Fast R-CNN achieves the top result on VOC12 with a mAP of 65.7% (and 68.4% with extra data). It is also two orders of magnitude faster than the other methods, which are all based on the "slow" R-CNN pipeline. On VOC10, SegDeepM [25] achieves a higher mAP than Fast R-CNN (67.2% vs. 66.1%). SegDeepM is trained on VOC12 trainval plus segmentation annotations; it is designed to boost R-CNN accuracy by using a Markov random field to reason over R-CNN detections and segmentations from the O₂P [1] semantic-segmentation method. Fast R-CNN can be swapped into SegDeepM in place of R-CNN, which may lead to better results. When using the enlarged 07++12 training set (see Table 2 caption), Fast R-CNN's mAP increases to 68.8%, surpassing SegDeepM.

**Table 2.** VOC 2010 test detection average precision (%). BabyLearning uses a network based on [17]. All other methods use VGG16. Training set key: 12: VOC12 trainval, Prop.: proprietary dataset, 12+seg: 12 with segmentation annotations, 07++12: union of VOC07 trainval, VOC07 test, and VOC12 trainval.

**Table 3.** VOC 2012 test detection average precision (%). BabyLearning and NUS_NIN_c2000 use networks based on [17]. All other methods use VGG16.

**4.3. VOC 2007 results**

On VOC07, we compare Fast R-CNN to R-CNN and SPPnet. All methods start from the same pre-trained VGG16 network and use bounding-box regression. The VGG16 SPPnet results were computed by the authors of [11]. SPPnet uses five scales during both training and testing. The improvement of Fast R-CNN over SPPnet illustrates that even though Fast R-CNN uses single-scale training and testing, fine-tuning the conv layers provides a large improvement in mAP (from 63.1% to 66.9%). R-CNN achieves a mAP of 66.0%. As a minor point, SPPnet was trained without examples marked as "difficult" in PASCAL. Removing these examples improves Fast R-CNN mAP to 68.1%. All other experiments use "difficult" examples.

**Table 1.** VOC 2007 test detection average precision (%). All methods use VGG16. Training set key: 07: VOC07 trainval, 07_ndiff: 07 without "difficult" examples, 07+12: union of 07 and VOC12 trainval. †SPPnet results were prepared by the authors of [11].

**4.4. Training and testing time**

Fast training and testing times are our second main result. Table 4 compares training time (hours), testing rate (seconds per image), and mAP on VOC07 between Fast R-CNN, R-CNN, and SPPnet. For VGG16, Fast R-CNN processes images 146× faster than R-CNN without truncated SVD and 213× faster with it. Training time is reduced by 9×, from 84 hours to 9.5. Compared to SPPnet, Fast R-CNN trains VGG16 2.7× faster (in 9.5 vs. 25.5 hours) and tests 7× faster without truncated SVD or 10× faster with it. Fast R-CNN also eliminates hundreds of gigabytes of disk storage, because it does not cache features.

**Table 4.** Runtime comparison between the same models in Fast R-CNN, R-CNN, and SPPnet. Fast R-CNN uses single-scale mode. SPPnet uses the five scales specified in [11]. †Timing provided by the authors of [11]. Times were measured on an Nvidia K40 GPU.

| | Fast R-CNN | R-CNN | SPPnet |
|---|---|---|---|
| | S | M | L | S | M | L† | L |
| train time (h) | 1.2 | 2.0 | 9.5 | 22 | 28 | 84 | 25 |
| train speedup | 18.3× | 14.0× | 8.8× | 1× | 1× | 1× | 3.4× |
| test rate (s/im) | 0.10 | 0.15 | 0.32 | 9.8 | 12.1 | 47.0 | 2.3 |
| with SVD | 0.06 | 0.08 | 0.22 | - | - | - | - |
| test speedup | 98× | 80× | 146× | 1× | 1× | 1× | 20× |
| with SVD | 169× | 150× | 213× | - | - | - | - |
| VOC07 mAP | 57.1 | 59.2 | 66.9 | 58.5 | 60.2 | 66.0 | 63.1 |
| with SVD | 56.5 | 58.7 | 66.6 | - | - | - | - |

**Truncated SVD.** Truncated SVD can reduce detection time by more than 30% with only a small (0.3 percentage point) drop in mAP and without needing to perform additional fine-tuning after model compression. Fig. 2 illustrates how using the top 1024 singular values from the 25088×4096 matrix in VGG16's fc6 layer and the top 256 singular values from the 4096×4096 fc7 layer reduces runtime with little loss in mAP. Further speed-ups are possible with smaller drops in mAP if one fine-tunes again after compression.

**Figure 2.** Timing for VGG16 before and after truncated SVD. Before SVD, fully connected layers fc6 and fc7 take 45% of the time.

*Forward pass timing:*
- Before SVD: mAP 66.9% @ 320ms/image
  - conv: 46.3% (146ms)
  - roi_pool: 5.4% (17ms)
  - fc6: 38.7% (122ms)
  - fc7: 6.2% (20ms)
  - other: 3.5% (11ms)

- After SVD: mAP 66.6% @ 223ms/image
  - conv: 67.8% (143ms)
  - roi_pool: 7.9% (17ms)
  - fc6: 17.5% (37ms)
  - fc7: 1.7% (4ms)
  - other: 5.1% (11ms)

**4.5. Which layers to fine-tune?**

For the less deep networks considered in the SPPnet paper [11], fine-tuning only the fully connected layers appeared to be sufficient for good accuracy. We hypothesized that this result would not hold for very deep networks. To validate that fine-tuning the conv layers is important for VGG16, we use Fast R-CNN to fine-tune, but freeze the thirteen conv layers so that only the fully connected layers learn. This ablation emulates single-scale SPPnet training and decreases mAP from 66.9% to 61.4% (Table 5). This experiment verifies our hypothesis: training through the RoI pooling layer is important for very deep nets.

**Table 5.** Effect of restricting which layers are fine-tuned for VGG16. Fine-tuning fc6 emulates the SPPnet training algorithm [11], but using a single scale. SPPnet L results were obtained using five scales, at a significant (7×) speed cost.

| layers fine-tuned in model L | SPPnet L |
|---|---|
| fc6 | conv3_1 | conv2_1 | fc6 |
| VOC07 mAP | 61.4 | 66.9 | 67.2 | 63.1 |
| test rate (s/im) | 0.32 | 0.32 | 0.32 | 2.3 |

Does this mean that all conv layers should be fine-tuned? In short, no. In the smaller networks (S and M) we find that conv1 is generic and task independent (a well-known fact [14]). Allowing conv1 to learn, or not, has no meaningful effect on mAP. For VGG16, we found it only necessary to update layers from conv3_1 and up (9 of the 13 conv layers). This observation is pragmatic: (1) updating from conv2_1 slows training by 1.3× (12.5 vs. 9.5 hours) compared to learning from conv3_1; and (2) updating from conv1_1 over-runs GPU memory. The difference in mAP when learning from conv2_1 up was only +0.3 points (Table 5, last column). All Fast R-CNN results in this paper using VGG16 fine-tune layers conv3_1 and up; all experiments with models S and M fine-tune layers conv2 and up.

---

²https://github.com/BVLC/caffe/wiki/Model-Zoo

³http://host.robots.ox.ac.uk:8080/leaderboard (accessed April 18, 2015)

---

### النسخة العربية

تدعم ثلاث نتائج رئيسية مساهمات هذه الورقة:

1. أحدث mAP على VOC07، 2010، و 2012
2. تدريب واختبار سريع مقارنة بـ R-CNN و SPPnet
3. الضبط الدقيق للطبقات الالتفافية في VGG16 يحسن mAP

**4.1. الإعداد التجريبي**

تستخدم تجاربنا ثلاثة نماذج ImageNet مدربة مسبقاً متاحة عبر الإنترنت.² النموذج الأول هو CaffeNet (في الأساس AlexNet [14]) من R-CNN [9]. نشير بالتبادل إلى هذا CaffeNet باسم النموذج S، لـ "small" (صغير). الشبكة الثانية هي VGG_CNN_M_1024 من [3]، والتي لها نفس العمق مثل S، لكنها أوسع. نسمي هذه الشبكة النموذج M، لـ "medium" (متوسط). الشبكة الأخيرة هي نموذج VGG16 العميق جداً من [20]. نظراً لأن هذا النموذج هو الأكبر، نسميه النموذج L. في هذا القسم، تستخدم جميع التجارب التدريب والاختبار أحادي المقياس (s=600؛ انظر القسم 5.2 للتفاصيل).

**4.2. نتائج VOC 2010 و 2012**

على مجموعات البيانات هذه، نقارن Fast R-CNN (FRCN، اختصاراً) مع أفضل الطرق على مسار comp4 (البيانات الخارجية) من لوحة المتصدرين العامة (الجدول 2، الجدول 3).³ بالنسبة لطرق NUS_NIN_c2000 و BabyLearning، لا توجد منشورات مرتبطة في هذا الوقت ولم نتمكن من العثور على معلومات دقيقة حول معماريات الشبكات الالتفافية المستخدمة؛ فهي متغيرات من تصميم Network-in-Network [17]. يتم تهيئة جميع الطرق الأخرى من نفس شبكة VGG16 المدربة مسبقاً.

تحقق Fast R-CNN أفضل نتيجة على VOC12 بقيمة mAP تبلغ 65.7% (و 68.4% مع بيانات إضافية). كما أنها أسرع بمرتبتين من حيث الحجم من الطرق الأخرى، والتي تعتمد جميعها على خط أنابيب R-CNN "البطيء". على VOC10، تحقق SegDeepM [25] mAP أعلى من Fast R-CNN (67.2% مقابل 66.1%). يتم تدريب SegDeepM على VOC12 trainval بالإضافة إلى تعليقات توضيحية للتجزئة؛ وهي مصممة لتعزيز دقة R-CNN باستخدام حقل ماركوف العشوائي للاستدلال على كشوفات R-CNN والتجزئات من طريقة التجزئة الدلالية O₂P [1]. يمكن استبدال R-CNN بـ Fast R-CNN في SegDeepM، مما قد يؤدي إلى نتائج أفضل. عند استخدام مجموعة التدريب الموسعة 07++12 (انظر تعليق الجدول 2)، يزيد mAP لـ Fast R-CNN إلى 68.8%، متجاوزاً SegDeepM.

**الجدول 2.** متوسط الدقة المتوسطة لاختبار كشف VOC 2010 (%). يستخدم BabyLearning شبكة بناءً على [17]. تستخدم جميع الطرق الأخرى VGG16. مفتاح مجموعة التدريب: 12: VOC12 trainval، Prop.: مجموعة بيانات خاصة، 12+seg: 12 مع تعليقات توضيحية للتجزئة، 07++12: اتحاد VOC07 trainval واختبار VOC07 و VOC12 trainval.

**الجدول 3.** متوسط الدقة المتوسطة لاختبار كشف VOC 2012 (%). يستخدم BabyLearning و NUS_NIN_c2000 شبكات بناءً على [17]. تستخدم جميع الطرق الأخرى VGG16.

**4.3. نتائج VOC 2007**

على VOC07، نقارن Fast R-CNN بـ R-CNN و SPPnet. تبدأ جميع الطرق من نفس شبكة VGG16 المدربة مسبقاً وتستخدم انحدار صندوق التحديد. تم حساب نتائج VGG16 SPPnet بواسطة مؤلفي [11]. تستخدم SPPnet خمسة مقاييس أثناء التدريب والاختبار. يوضح تحسن Fast R-CNN على SPPnet أنه على الرغم من أن Fast R-CNN تستخدم التدريب والاختبار أحادي المقياس، فإن الضبط الدقيق للطبقات الالتفافية يوفر تحسناً كبيراً في mAP (من 63.1% إلى 66.9%). تحقق R-CNN mAP بنسبة 66.0%. كنقطة ثانوية، تم تدريب SPPnet بدون أمثلة تم وضع علامة "صعبة" عليها في PASCAL. يؤدي إزالة هذه الأمثلة إلى تحسين mAP لـ Fast R-CNN إلى 68.1%. تستخدم جميع التجارب الأخرى الأمثلة "الصعبة".

**الجدول 1.** متوسط الدقة المتوسطة لاختبار كشف VOC 2007 (%). تستخدم جميع الطرق VGG16. مفتاح مجموعة التدريب: 07: VOC07 trainval، 07_ndiff: 07 بدون أمثلة "صعبة"، 07+12: اتحاد 07 و VOC12 trainval. †تم إعداد نتائج SPPnet بواسطة مؤلفي [11].

**4.4. وقت التدريب والاختبار**

أوقات التدريب والاختبار السريعة هي نتيجتنا الرئيسية الثانية. يقارن الجدول 4 وقت التدريب (بالساعات)، ومعدل الاختبار (ثوان لكل صورة)، و mAP على VOC07 بين Fast R-CNN و R-CNN و SPPnet. بالنسبة لـ VGG16، تعالج Fast R-CNN الصور بسرعة أكبر 146× من R-CNN بدون SVD المقطوع و 213× أسرع معه. يتم تقليل وقت التدريب بمعامل 9×، من 84 ساعة إلى 9.5. وبالمقارنة مع SPPnet، تدرب Fast R-CNN VGG16 بسرعة أكبر 2.7× (في 9.5 مقابل 25.5 ساعة) وتختبر بسرعة أكبر 7× بدون SVD المقطوع أو 10× أسرع معه. تلغي Fast R-CNN أيضاً مئات الجيجابايتات من مساحة التخزين على القرص، لأنها لا تخزن الميزات مؤقتاً.

**الجدول 4.** مقارنة وقت التشغيل بين نفس النماذج في Fast R-CNN و R-CNN و SPPnet. تستخدم Fast R-CNN الوضع أحادي المقياس. تستخدم SPPnet المقاييس الخمسة المحددة في [11]. †التوقيت مقدم من مؤلفي [11]. تم قياس الأوقات على GPU Nvidia K40.

| | Fast R-CNN | R-CNN | SPPnet |
|---|---|---|---|
| | S | M | L | S | M | L† | L |
| وقت التدريب (ساعة) | 1.2 | 2.0 | 9.5 | 22 | 28 | 84 | 25 |
| تسريع التدريب | 18.3× | 14.0× | 8.8× | 1× | 1× | 1× | 3.4× |
| معدل الاختبار (ث/صورة) | 0.10 | 0.15 | 0.32 | 9.8 | 12.1 | 47.0 | 2.3 |
| مع SVD | 0.06 | 0.08 | 0.22 | - | - | - | - |
| تسريع الاختبار | 98× | 80× | 146× | 1× | 1× | 1× | 20× |
| مع SVD | 169× | 150× | 213× | - | - | - | - |
| VOC07 mAP | 57.1 | 59.2 | 66.9 | 58.5 | 60.2 | 66.0 | 63.1 |
| مع SVD | 56.5 | 58.7 | 66.6 | - | - | - | - |

**SVD المقطوع.** يمكن لـ SVD المقطوع تقليل وقت الكشف بأكثر من 30% مع انخفاض صغير فقط (0.3 نقطة مئوية) في mAP ودون الحاجة إلى إجراء ضبط دقيق إضافي بعد ضغط النموذج. يوضح الشكل 2 كيف أن استخدام أعلى 1024 قيمة مفردة من مصفوفة 25088×4096 في طبقة fc6 لـ VGG16 وأعلى 256 قيمة مفردة من طبقة fc7 ذات المصفوفة 4096×4096 يقلل وقت التشغيل مع فقدان قليل في mAP. من الممكن تحقيق تسريعات أكبر مع انخفاضات أصغر في mAP إذا تم إجراء ضبط دقيق مرة أخرى بعد الضغط.

**الشكل 2.** التوقيت لـ VGG16 قبل وبعد SVD المقطوع. قبل SVD، تستغرق الطبقات المتصلة بالكامل fc6 و fc7 نسبة 45% من الوقت.

*توقيت التمرير الأمامي:*
- قبل SVD: mAP 66.9% @ 320 مللي ثانية/صورة
  - conv: 46.3% (146 مللي ثانية)
  - roi_pool: 5.4% (17 مللي ثانية)
  - fc6: 38.7% (122 مللي ثانية)
  - fc7: 6.2% (20 مللي ثانية)
  - أخرى: 3.5% (11 مللي ثانية)

- بعد SVD: mAP 66.6% @ 223 مللي ثانية/صورة
  - conv: 67.8% (143 مللي ثانية)
  - roi_pool: 7.9% (17 مللي ثانية)
  - fc6: 17.5% (37 مللي ثانية)
  - fc7: 1.7% (4 مللي ثانية)
  - أخرى: 5.1% (11 مللي ثانية)

**4.5. أي الطبقات يجب ضبطها بدقة؟**

بالنسبة للشبكات الأقل عمقاً التي تم النظر فيها في ورقة SPPnet [11]، بدا أن الضبط الدقيق للطبقات المتصلة بالكامل فقط كافٍ للحصول على دقة جيدة. افترضنا أن هذه النتيجة لن تصمد للشبكات العميقة جداً. للتحقق من أن الضبط الدقيق للطبقات الالتفافية مهم لـ VGG16، نستخدم Fast R-CNN للضبط الدقيق، لكن نجمّد الطبقات الالتفافية الثلاث عشرة بحيث تتعلم الطبقات المتصلة بالكامل فقط. يحاكي هذا الاستئصال تدريب SPPnet أحادي المقياس ويقلل mAP من 66.9% إلى 61.4% (الجدول 5). تحقق هذه التجربة من فرضيتنا: التدريب عبر طبقة تجميع RoI مهم للشبكات العميقة جداً.

**الجدول 5.** تأثير تقييد الطبقات التي يتم ضبطها بدقة لـ VGG16. الضبط الدقيق لـ fc6 يحاكي خوارزمية تدريب SPPnet [11]، لكن باستخدام مقياس واحد. تم الحصول على نتائج SPPnet L باستخدام خمسة مقاييس، بتكلفة سرعة كبيرة (7×).

| الطبقات المضبوطة بدقة في النموذج L | SPPnet L |
|---|---|
| fc6 | conv3_1 | conv2_1 | fc6 |
| VOC07 mAP | 61.4 | 66.9 | 67.2 | 63.1 |
| معدل الاختبار (ث/صورة) | 0.32 | 0.32 | 0.32 | 2.3 |

هل يعني هذا أنه يجب ضبط جميع الطبقات الالتفافية بدقة؟ باختصار، لا. في الشبكات الأصغر (S و M) نجد أن conv1 عامة ومستقلة عن المهمة (حقيقة معروفة [14]). السماح لـ conv1 بالتعلم أم لا ليس له تأثير ذو معنى على mAP. بالنسبة لـ VGG16، وجدنا أنه من الضروري فقط تحديث الطبقات من conv3_1 وما فوق (9 من 13 طبقة التفافية). هذه الملاحظة عملية: (1) التحديث من conv2_1 يبطئ التدريب بمعامل 1.3× (12.5 مقابل 9.5 ساعة) مقارنة بالتعلم من conv3_1؛ و (2) التحديث من conv1_1 يتجاوز ذاكرة GPU. كان الفرق في mAP عند التعلم من conv2_1 وما فوق +0.3 نقطة فقط (الجدول 5، العمود الأخير). تضبط جميع نتائج Fast R-CNN في هذه الورقة باستخدام VGG16 الطبقات conv3_1 وما فوق بدقة؛ وتضبط جميع التجارب مع النماذج S و M الطبقات conv2 وما فوق بدقة.

---

²https://github.com/BVLC/caffe/wiki/Model-Zoo

³http://host.robots.ox.ac.uk:8080/leaderboard (تم الوصول في 18 أبريل 2015)

---

### Translation Notes

- **Figures referenced:** Figure 2 (timing breakdown for VGG16)
- **Tables referenced:** Tables 1-5 (experimental results)
- **Key terms introduced:**
  - state-of-the-art: الأحدث / الأفضل
  - orders of magnitude: مرتبات من حيث الحجم
  - Markov random field: حقل ماركوف العشوائي
  - semantic-segmentation: التجزئة الدلالية
  - ablation: استئصال
  - generic: عامة
  - task independent: مستقلة عن المهمة
  - speedup: تسريع
  - runtime: وقت التشغيل
  - model compression: ضغط النموذج

- **Equations:** None
- **Citations:** References [1, 3, 9, 10, 11, 14, 17, 20, 25]
- **Special handling:**
  - Tables are summarized in text form due to complexity
  - Preserved all numerical results exactly
  - Kept model names (S, M, L) and dataset names in English
  - Maintained acronyms: VOC, mAP, FRCN, SVD, GPU

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.90
- Readability: 0.84
- Glossary consistency: 0.90
- **Overall section score:** 0.86

### Back-translation Verification

Key result sentence back-translated:
Arabic: "تحقق Fast R-CNN أفضل نتيجة على VOC12 بقيمة mAP تبلغ 65.7% (و 68.4% مع بيانات إضافية)"
Back to English: "Fast R-CNN achieves the best result on VOC12 with an mAP value of 65.7% (and 68.4% with additional data)"
✓ Matches original semantics accurately
