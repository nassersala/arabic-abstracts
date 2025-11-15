# Section 5: Design Evaluation
## القسم 5: تقييم التصميم

**Section:** design evaluation
**Translation Quality:** 0.87
**Glossary Terms Used:** multi-task learning (التعلم متعدد المهام), training (تدريب), accuracy (دقة), scale-invariant (ثابت المقياس), softmax, SVM (آلات المتجهات الداعمة), object proposals (مقترحات الأجسام)

---

### English Version

We conducted experiments to understand how Fast R-CNN compares to R-CNN and SPPnet, as well as to evaluate design decisions. Following best practices, we performed these experiments on the PASCAL VOC07 dataset.

**5.1. Does multi-task training help?**

Multi-task training is convenient because it avoids managing a pipeline of sequentially-trained tasks. But it also has the potential to improve results because the tasks influence each other through a shared representation (the ConvNet) [2]. Does multi-task training improve object detection accuracy in Fast R-CNN?

To test this question, we train baseline networks that use only the classification loss, L_cls, in Eq. 1 (i.e., setting λ=0). These baselines are printed for models S, M, and L in the first column of each group in Table 6. Note that these models do not have bounding-box regressors. Next (second column per group), we take networks that were trained with the multi-task loss (Eq. 1, λ=1), but we disable bounding-box regression at test time. This isolates the networks' classification accuracy and allows an apples-to-apples comparison with the baseline networks.

Across all three networks we observe that multi-task training improves pure classification accuracy relative to training for classification alone. The improvement ranges from +0.8 to +1.1 mAP points, showing a consistent positive effect from multi-task learning.

Finally, we take the baseline models (trained with only the classification loss), tack on the bounding-box regression layer, and train them with L_loc while keeping all other network parameters frozen. The third column in each group shows the results of this stage-wise training scheme: mAP improves over column one, but stage-wise training underperforms multi-task training (fourth column per group).

**Table 6.** Multi-task training (fourth column per group) improves mAP over piecewise training (third column per group).

**5.2. Scale invariance: to brute force or finesse?**

We compare two strategies for achieving scale-invariant object detection: brute-force learning (single scale) and image pyramids (multi-scale). In either case, we define the scale s of an image to be the length of its shortest side.

All single-scale experiments use s=600 pixels; s may be less than 600 for some images as we cap the longest image side at 1000 pixels and maintain the image's aspect ratio. These values were selected so that VGG16 fits in GPU memory during fine-tuning. The smaller models are not memory bound and can benefit from larger values of s; however, optimizing s for each model is not our main concern. We note that PASCAL images are 384×473 pixels on average and thus the single-scale setting typically upsamples images by a factor of 1.6. The average effective stride at the RoI pooling layer is thus ~10 pixels.

In the multi-scale setting, we use the same five scales specified in [11] (s ∈ {480, 576, 688, 864, 1200}) to facilitate comparison with SPPnet. However, we cap the longest side at 2000 pixels to avoid exceeding GPU memory.

Table 7 shows models S and M when trained and tested with either one or five scales. Perhaps the most surprising result in [11] was that single-scale detection performs almost as well as multi-scale detection. Our findings confirm their result: deep ConvNets are adept at directly learning scale invariance. The multi-scale approach offers only a small increase in mAP at a large cost in compute time (Table 7). In the case of VGG16 (model L), we are limited to using a single scale by implementation details. Yet it achieves a mAP of 66.9%, which is slightly higher than the 66.0% reported for R-CNN [10], even though R-CNN uses "infinite" scales in the sense that each proposal is warped to a canonical size.

Since single-scale processing offers the best tradeoff between speed and accuracy, especially for very deep models, all experiments outside of this sub-section use single-scale training and testing with s=600 pixels.

**Table 7.** Multi-scale vs. single scale. SPPnet ZF (similar to model S) results are from [11]. Larger networks with a single-scale offer the best speed/accuracy tradeoff. (L cannot use multi-scale in our implementation due to GPU memory constraints.)

**5.3. Do we need more training data?**

A good object detector should improve when supplied with more training data. Zhu et al. [24] found that DPM [8] mAP saturates after only a few hundred to thousand training examples. Here we augment the VOC07 trainval set with the VOC12 trainval set, roughly tripling the number of images to 16.5k, to evaluate Fast R-CNN. Enlarging the training set improves mAP on VOC07 test from 66.9% to 70.0% (Table 1). When training on this dataset we use 60k mini-batch iterations instead of 40k.

We perform similar experiments for VOC10 and 2012, for which we construct a dataset of 21.5k images from the union of VOC07 trainval, test, and VOC12 trainval. When training on this dataset, we use 100k SGD iterations and lower the learning rate by 0.1× each 40k iterations (instead of each 30k). For VOC10 and 2012, mAP improves from 66.1% to 68.8% and from 65.7% to 68.4%, respectively.

**5.4. Do SVMs outperform softmax?**

Fast R-CNN uses the softmax classifier learnt during fine-tuning instead of training one-vs-rest linear SVMs post-hoc, as was done in R-CNN and SPPnet. To understand the impact of this choice, we implemented post-hoc SVM training with hard negative mining in Fast R-CNN. We use the same training algorithm and hyper-parameters as in R-CNN.

**Table 8.** Fast R-CNN with softmax vs. SVM (VOC07 mAP).

| method | classifier | S | M | L |
|---|---|---|---|---|
| R-CNN [9, 10] | SVM | 58.5 | 60.2 | 66.0 |
| FRCN [ours] | SVM | 56.3 | 58.7 | 66.8 |
| FRCN [ours] | softmax | 57.1 | 59.2 | 66.9 |

Table 8 shows softmax slightly outperforming SVM for all three networks, by +0.1 to +0.8 mAP points. This effect is small, but it demonstrates that "one-shot" fine-tuning is sufficient compared to previous multi-stage training approaches. We note that softmax, unlike one-vs-rest SVMs, introduces competition between classes when scoring a RoI.

**5.5. Are more proposals always better?**

There are (broadly) two types of object detectors: those that use a sparse set of object proposals (e.g., selective search [21]) and those that use a dense set (e.g., DPM [8]). Classifying sparse proposals is a type of cascade [22] in which the proposal mechanism first rejects a vast number of candidates leaving the classifier with a small set to evaluate. This cascade improves detection accuracy when applied to DPM detections [21]. We find evidence that the proposal-classifier cascade also improves Fast R-CNN accuracy.

Using selective search's quality mode, we sweep from 1k to 10k proposals per image, each time re-training and re-testing model M. If proposals serve a purely computational role, increasing the number of proposals per image should not harm mAP.

We find that mAP rises and then falls slightly as the proposal count increases (Fig. 3, solid blue line). This experiment shows that swamping the deep classifier with more proposals does not help, and even slightly hurts, accuracy. This result is difficult to predict without actually running the experiment. The state-of-the-art for measuring object proposal quality is Average Recall (AR) [12]. AR correlates well with mAP for several proposal methods using R-CNN, when using a fixed number of proposals per image. Fig. 3 shows that AR (solid red line) does not correlate well with mAP as the number of proposals per image is varied. AR must be used with care; higher AR due to more proposals does not imply that mAP will increase. Fortunately, training and testing with model M takes less than 2.5 hours. Fast R-CNN thus enables efficient, direct evaluation of object proposal mAP, which is preferable to proxy metrics.

We also investigate Fast R-CNN when using densely generated boxes (over scale, position, and aspect ratio), at a rate of about 45k boxes/image. This dense set is rich enough that when each selective search box is replaced by its closest (in IoU) dense box, mAP drops only 1 point (to 57.7%, Fig. 3, blue triangle).

The statistics of the dense boxes differ from those of selective search boxes. Starting with 2k selective search boxes, we test mAP when adding a random sample of 1000×{2,4,6,8,10,32,45} dense boxes. For each experiment we re-train and re-test model M. When these dense boxes are added, mAP falls more strongly than when adding more selective search boxes, eventually reaching 53.0%.

We also train and test Fast R-CNN using only dense boxes (45k/image). This setting yields a mAP of 52.9% (blue diamond). Finally, we check if SVMs with hard negative mining are needed to cope with the dense box distribution. SVMs do even worse: 49.3% (blue circle).

**Figure 3.** VOC07 test mAP and AR for various proposal schemes.

**5.6. Preliminary MS COCO results**

We applied Fast R-CNN (with VGG16) to the MS COCO dataset [18] to establish a preliminary baseline. We trained on the 80k image training set for 240k iterations and evaluated on the "test-dev" set using the evaluation server. The PASCAL-style mAP is 35.9%; the new COCO-style AP, which also averages over IoU thresholds, is 19.7%.

---

### النسخة العربية

أجرينا تجارب لفهم كيفية مقارنة Fast R-CNN بـ R-CNN و SPPnet، وكذلك لتقييم قرارات التصميم. متبعين أفضل الممارسات، أجرينا هذه التجارب على مجموعة بيانات PASCAL VOC07.

**5.1. هل يساعد التدريب متعدد المهام؟**

التدريب متعدد المهام مريح لأنه يتجنب إدارة خط أنابيب من المهام المدربة بشكل تسلسلي. ولكنه أيضاً لديه إمكانية تحسين النتائج لأن المهام تؤثر على بعضها البعض من خلال تمثيل مشترك (الشبكة الالتفافية) [2]. هل يحسن التدريب متعدد المهام دقة كشف الأجسام في Fast R-CNN؟

لاختبار هذا السؤال، ندرب شبكات أساسية تستخدم فقط خسارة التصنيف، L_cls، في المعادلة 1 (أي تعيين λ=0). تُطبع هذه الخطوط الأساسية للنماذج S و M و L في العمود الأول من كل مجموعة في الجدول 6. لاحظ أن هذه النماذج لا تحتوي على منحدرات صناديق التحديد. تالياً (العمود الثاني لكل مجموعة)، نأخذ شبكات تم تدريبها بخسارة متعددة المهام (المعادلة 1، λ=1)، لكننا نعطل انحدار صندوق التحديد في وقت الاختبار. هذا يعزل دقة تصنيف الشبكات ويسمح بمقارنة متساوية مع الشبكات الأساسية.

عبر جميع الشبكات الثلاث نلاحظ أن التدريب متعدد المهام يحسن دقة التصنيف الصرفة نسبة إلى التدريب للتصنيف وحده. يتراوح التحسن من +0.8 إلى +1.1 نقطة mAP، مما يظهر تأثيراً إيجابياً متسقاً من التعلم متعدد المهام.

أخيراً، نأخذ النماذج الأساسية (المدربة بخسارة التصنيف فقط)، ونضيف طبقة انحدار صندوق التحديد، وندربها بـ L_loc مع الحفاظ على جميع معاملات الشبكة الأخرى مجمدة. يظهر العمود الثالث في كل مجموعة نتائج مخطط التدريب على مراحل هذا: يتحسن mAP على العمود الأول، لكن التدريب على مراحل يكون أقل أداءً من التدريب متعدد المهام (العمود الرابع لكل مجموعة).

**الجدول 6.** التدريب متعدد المهام (العمود الرابع لكل مجموعة) يحسن mAP على التدريب المجزأ (العمود الثالث لكل مجموعة).

**5.2. ثبات المقياس: بالقوة الغاشمة أم بالمهارة؟**

نقارن استراتيجيتين لتحقيق كشف الأجسام الثابت للمقياس: التعلم بالقوة الغاشمة (مقياس واحد) وأهرامات الصور (متعدد المقاييس). في كلتا الحالتين، نعرّف المقياس s للصورة بأنه طول أقصر جانب لها.

تستخدم جميع التجارب أحادية المقياس s=600 بكسل؛ قد يكون s أقل من 600 لبعض الصور حيث نحد أطول جانب للصورة عند 1000 بكسل ونحافظ على نسبة أبعاد الصورة. تم اختيار هذه القيم بحيث تتناسب VGG16 مع ذاكرة GPU أثناء الضبط الدقيق. النماذج الأصغر ليست محدودة بالذاكرة ويمكن أن تستفيد من قيم أكبر لـ s؛ ومع ذلك، فإن تحسين s لكل نموذج ليس مصدر قلقنا الرئيسي. نلاحظ أن صور PASCAL بمتوسط 384×473 بكسل وبالتالي فإن إعداد المقياس الواحد عادة ما يزيد عينات الصور بمعامل 1.6. متوسط الخطوة الفعالة عند طبقة تجميع RoI هو بالتالي ~10 بكسل.

في إعداد متعدد المقاييس، نستخدم نفس المقاييس الخمسة المحددة في [11] (s ∈ {480، 576، 688، 864، 1200}) لتسهيل المقارنة مع SPPnet. ومع ذلك، نحد الجانب الأطول عند 2000 بكسل لتجنب تجاوز ذاكرة GPU.

يُظهر الجدول 7 النماذج S و M عند التدريب والاختبار بمقياس واحد أو خمسة مقاييس. ربما كانت النتيجة الأكثر إثارة للدهشة في [11] هي أن الكشف أحادي المقياس يؤدي تقريباً بنفس جودة الكشف متعدد المقاييس. تؤكد نتائجنا نتيجتهم: الشبكات الالتفافية العميقة بارعة في التعلم المباشر لثبات المقياس. يقدم النهج متعدد المقاييس زيادة صغيرة فقط في mAP بتكلفة كبيرة في وقت الحساب (الجدول 7). في حالة VGG16 (النموذج L)، نحن محدودون باستخدام مقياس واحد بسبب تفاصيل التنفيذ. ومع ذلك فهو يحقق mAP بنسبة 66.9%، وهو أعلى قليلاً من 66.0% المبلغ عنه لـ R-CNN [10]، على الرغم من أن R-CNN يستخدم مقاييس "لا نهائية" بمعنى أن كل مقترح يُشوه إلى حجم معياري.

نظراً لأن المعالجة أحادية المقياس توفر أفضل مقايضة بين السرعة والدقة، خاصة للنماذج العميقة جداً، فإن جميع التجارب خارج هذا القسم الفرعي تستخدم التدريب والاختبار أحادي المقياس مع s=600 بكسل.

**الجدول 7.** متعدد المقاييس مقابل المقياس الواحد. نتائج SPPnet ZF (مماثلة للنموذج S) من [11]. الشبكات الأكبر مع المقياس الواحد توفر أفضل مقايضة سرعة/دقة. (لا يمكن لـ L استخدام متعدد المقاييس في تنفيذنا بسبب قيود ذاكرة GPU.)

**5.3. هل نحتاج إلى مزيد من بيانات التدريب؟**

يجب أن يتحسن كاشف الأجسام الجيد عند تزويده بمزيد من بيانات التدريب. وجد Zhu وآخرون [24] أن mAP لـ DPM [8] يتشبع بعد بضع مئات إلى آلاف من أمثلة التدريب فقط. هنا نعزز مجموعة VOC07 trainval بمجموعة VOC12 trainval، مما يضاعف عدد الصور تقريباً ثلاث مرات إلى 16.5 ألف، لتقييم Fast R-CNN. يؤدي توسيع مجموعة التدريب إلى تحسين mAP على اختبار VOC07 من 66.9% إلى 70.0% (الجدول 1). عند التدريب على مجموعة البيانات هذه نستخدم 60 ألف تكرار دفعة صغيرة بدلاً من 40 ألف.

نجري تجارب مماثلة لـ VOC10 و 2012، التي نبني لها مجموعة بيانات من 21.5 ألف صورة من اتحاد VOC07 trainval واختبار و VOC12 trainval. عند التدريب على مجموعة البيانات هذه، نستخدم 100 ألف تكرار SGD ونخفض معدل التعلم بمعامل 0.1× كل 40 ألف تكرار (بدلاً من كل 30 ألف). بالنسبة لـ VOC10 و 2012، يتحسن mAP من 66.1% إلى 68.8% ومن 65.7% إلى 68.4%، على التوالي.

**5.4. هل تتفوق آلات المتجهات الداعمة على softmax؟**

تستخدم Fast R-CNN مصنف softmax الذي تم تعلمه أثناء الضبط الدقيق بدلاً من تدريب آلات المتجهات الداعمة الخطية واحد-مقابل-البقية بعد الحقيقة، كما تم في R-CNN و SPPnet. لفهم تأثير هذا الاختيار، قمنا بتنفيذ تدريب آلات المتجهات الداعمة بعد الحقيقة مع تعدين سلبي صعب في Fast R-CNN. نستخدم نفس خوارزمية التدريب والمعاملات الفائقة كما في R-CNN.

**الجدول 8.** Fast R-CNN مع softmax مقابل SVM (VOC07 mAP).

| الطريقة | المصنف | S | M | L |
|---|---|---|---|---|
| R-CNN [9, 10] | SVM | 58.5 | 60.2 | 66.0 |
| FRCN [لنا] | SVM | 56.3 | 58.7 | 66.8 |
| FRCN [لنا] | softmax | 57.1 | 59.2 | 66.9 |

يُظهر الجدول 8 أن softmax يتفوق قليلاً على SVM لجميع الشبكات الثلاث، بمقدار +0.1 إلى +0.8 نقطة mAP. هذا التأثير صغير، لكنه يوضح أن الضبط الدقيق "بطلقة واحدة" كافٍ مقارنة بالأساليب التدريبية متعددة المراحل السابقة. نلاحظ أن softmax، على عكس آلات المتجهات الداعمة واحد-مقابل-البقية، يقدم منافسة بين الفئات عند تقييم RoI.

**5.5. هل المزيد من المقترحات دائماً أفضل؟**

يوجد (بشكل عام) نوعان من كاشفات الأجسام: تلك التي تستخدم مجموعة متفرقة من مقترحات الأجسام (مثل البحث الانتقائي [21]) وتلك التي تستخدم مجموعة كثيفة (مثل DPM [8]). تصنيف المقترحات المتفرقة هو نوع من التسلسل [22] حيث تقوم آلية الاقتراح أولاً برفض عدد كبير من المرشحين تاركة المصنف بمجموعة صغيرة للتقييم. يحسن هذا التسلسل دقة الكشف عند تطبيقه على كشوفات DPM [21]. نجد دليلاً على أن تسلسل المقترح-المصنف يحسن أيضاً دقة Fast R-CNN.

باستخدام وضع الجودة للبحث الانتقائي، نمسح من 1 ألف إلى 10 آلاف مقترح لكل صورة، في كل مرة نعيد تدريب وإعادة اختبار النموذج M. إذا كانت المقترحات تخدم دوراً حسابياً بحتاً، فإن زيادة عدد المقترحات لكل صورة لا يجب أن يضر بـ mAP.

نجد أن mAP يرتفع ثم ينخفض قليلاً مع زيادة عدد المقترحات (الشكل 3، الخط الأزرق الصلب). توضح هذه التجربة أن إغراق المصنف العميق بمزيد من المقترحات لا يساعد، بل يضر قليلاً بالدقة. يصعب التنبؤ بهذه النتيجة دون تشغيل التجربة فعلياً. الأحدث في قياس جودة مقترحات الأجسام هو متوسط الاستدعاء (AR) [12]. يرتبط AR جيداً بـ mAP لعدة طرق اقتراح باستخدام R-CNN، عند استخدام عدد ثابت من المقترحات لكل صورة. يُظهر الشكل 3 أن AR (الخط الأحمر الصلب) لا يرتبط جيداً بـ mAP عند تغيير عدد المقترحات لكل صورة. يجب استخدام AR بحذر؛ ارتفاع AR بسبب المزيد من المقترحات لا يعني أن mAP سيزداد. لحسن الحظ، يستغرق التدريب والاختبار مع النموذج M أقل من 2.5 ساعة. وبالتالي تمكن Fast R-CNN من التقييم المباشر والفعال لـ mAP مقترحات الأجسام، وهو أفضل من المقاييس البديلة.

نحقق أيضاً في Fast R-CNN عند استخدام صناديق كثيفة التوليد (عبر المقياس والموقع ونسبة الأبعاد)، بمعدل حوالي 45 ألف صندوق/صورة. هذه المجموعة الكثيفة غنية بما يكفي بحيث عندما يتم استبدال كل صندوق بحث انتقائي بأقرب صندوق كثيف له (في IoU)، ينخفض mAP نقطة واحدة فقط (إلى 57.7%، الشكل 3، المثلث الأزرق).

تختلف إحصائيات الصناديق الكثيفة عن تلك الخاصة بصناديق البحث الانتقائي. بدءاً من 2 ألف صندوق بحث انتقائي، نختبر mAP عند إضافة عينة عشوائية من 1000×{2،4،6،8،10،32،45} صندوق كثيف. لكل تجربة نعيد تدريب وإعادة اختبار النموذج M. عند إضافة هذه الصناديق الكثيفة، ينخفض mAP بقوة أكبر من عند إضافة المزيد من صناديق البحث الانتقائي، ليصل في النهاية إلى 53.0%.

ندرب ونختبر أيضاً Fast R-CNN باستخدام الصناديق الكثيفة فقط (45 ألف/صورة). ينتج هذا الإعداد mAP بنسبة 52.9% (الماسة الزرقاء). أخيراً، نتحقق مما إذا كانت آلات المتجهات الداعمة مع تعدين سلبي صعب مطلوبة للتعامل مع توزيع الصناديق الكثيفة. تقوم آلات المتجهات الداعمة بأداء أسوأ: 49.3% (الدائرة الزرقاء).

**الشكل 3.** VOC07 اختبار mAP و AR لمخططات اقتراح مختلفة.

**5.6. النتائج الأولية لـ MS COCO**

طبقنا Fast R-CNN (مع VGG16) على مجموعة بيانات MS COCO [18] لإنشاء خط أساس أولي. دربنا على مجموعة التدريب المكونة من 80 ألف صورة لـ 240 ألف تكرار وقيمنا على مجموعة "test-dev" باستخدام خادم التقييم. mAP بأسلوب PASCAL هو 35.9%؛ AP بأسلوب COCO الجديد، الذي يتوسط أيضاً عبر عتبات IoU، هو 19.7%.

---

### Translation Notes

- **Figures referenced:** Figure 3 (mAP and AR for proposal schemes)
- **Tables referenced:** Tables 6, 7, 8
- **Key terms introduced:**
  - multi-task learning: التعلم متعدد المهام
  - stage-wise training: التدريب على مراحل
  - piecewise training: التدريب المجزأ
  - apples-to-apples comparison: مقارنة متساوية
  - brute-force: القوة الغاشمة
  - finesse: المهارة
  - aspect ratio: نسبة الأبعاد
  - upsamples: يزيد عينات
  - one-shot fine-tuning: الضبط الدقيق بطلقة واحدة
  - one-vs-rest: واحد-مقابل-البقية
  - post-hoc: بعد الحقيقة
  - hard negative mining: تعدين سلبي صعب
  - cascade: تسلسل
  - selective search: البحث الانتقائي
  - sparse: متفرقة
  - dense: كثيفة
  - Average Recall (AR): متوسط الاستدعاء
  - proxy metrics: المقاييس البديلة

- **Equations:** None
- **Citations:** References [2, 8, 10, 11, 12, 18, 21, 22, 24]
- **Special handling:**
  - Maintained all numerical results precisely
  - Kept dataset names and model designations in English
  - Preserved technical acronyms

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.92
- **Overall section score:** 0.87

### Back-translation Verification

Key finding back-translated:
Arabic: "نجد أن mAP يرتفع ثم ينخفض قليلاً مع زيادة عدد المقترحات"
Back to English: "We find that mAP rises and then falls slightly as the number of proposals increases"
✓ Matches original semantics accurately
