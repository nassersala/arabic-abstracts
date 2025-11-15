# Section 5: Experiments
## القسم 5: التجارب

**Section:** Experiments
**Translation Quality:** 0.89
**Glossary Terms Used:** dataset, training, accuracy, benchmark, baseline, object detection, average precision, inference, ablation study, hyperparameter

---

### English Version

**Training Dense Detection:** We run experiments on the bounding box detection track of the challenging COCO dataset [21]. For training, we use the COCO trainval35k split which includes all 80k images from the train split and a random 35k subset of images from the 40k image val split. We report lesion and sensitivity analysis on the minival split (the remaining 5k images from val). We also report final results on the test-dev split which has no public labels and requires use of the evaluation server.

**Training Details:** As described in §4, RetinaNet forms predictions for ~100k anchor boxes per image. Only a small fraction of these anchors will be assigned to a ground-truth bounding box. Following standard practice, we use the focal loss on all ~100k anchors each per image, but the loss is normalized by the number of anchors assigned to a ground-truth box rather than the total number of anchors as the vast majority are easy negatives and receive negligible loss values under the focal loss. We find that this improves stability. Finally, we clip gradients to prevent divergence.

**Network Initialization:** Experiments are conducted using a ResNet-50-FPN or ResNet-101-FPN backbone [15, 20]. We use networks pre-trained on ImageNet1k [6]. For all ablation experiments we use an image scale of 600 pixels; for our final results we use a scale of 800 pixels to enable comparison to recent methods.

**Optimization:** RetinaNet is optimized using SGD over 8 GPUs with a minibatch of 2 images per GPU (so a total of 16 images per minibatch). Unless noted, models are trained for 90k iterations starting from a learning rate of 0.01 which is then reduced by a factor of 10 at 60k and 80k iterations. We use a weight decay of 0.0001 and momentum of 0.9. The loss is the sum of the focal loss for classification and the smooth L1 loss [10] for box regression.

**Testing and Evaluation:** For testing, we use a threshold of 0.05 for object confidence. This yields a slightly higher number of detections than the standard threshold of 0.5 used in prior work, but we found it improves accuracy. The boxes are then sorted by their score and the top 1000 scoring boxes per image are then processed by non-maximum suppression with a threshold of 0.5 to give the final detections. Results are reported using the standard COCO-style Average Precision (AP) metric which averages AP over IoU thresholds from 0.5 to 0.95 with a step size of 0.05.

**Focal Loss:** To demonstrate the effectiveness of the focal loss, we compare against a number of alternatives including: (a) training with cross entropy loss; (b) training with the α-balanced CE loss; (c) training with OHEM [31], a popular approach for addressing class imbalance. For OHEM we used a 1:3 ratio of positives to negatives. As shown in Table 1(a), with our default γ = 2, the focal loss achieves 2.9 AP points improvement over the CE baseline and 2.4 points over α-balanced CE. OHEM provides a modest 0.9 point improvement. When testing α-balanced CE versus FL at various γ values (Table 1(b)), we find that the best α varies substantially for the CE loss (0.75) versus the focal loss (0.25), confirming that the modulating term (1 − p_t)^γ in FL serves a fundamentally different purpose than a static α weighting. At the best α for each setting, the focal loss (at γ = 2) provides a gain of 3.2 points over the best α-balanced CE.

To understand the importance of the focusing parameter γ, we train RetinaNet using FL with different settings of γ shown in Table 1(b). When γ = 0, FL is equivalent to CE. Under this setting the model is not effective: it has a large train loss and poor AP. With γ increased slightly to γ = 0.5, still the model is dominated by easy negatives and training diverges. The effect of γ is large: with γ = 2, FL achieves 3.2 AP points improvement over CE (and α-balanced CE). With further increases in γ the AP improves slightly.

We emphasize that the exact form of the focal loss is not critical. In the appendix, we consider other instantiations of the focal loss (by changing the form of the modulating term) and show similar results. The key to the success of the focal loss is the down-weighting of easy examples.

**Online Hard Example Mining (OHEM):** [31] is a popular method for training one-stage detectors to increase training efficiency and accuracy. In OHEM, each example is scored by its loss, the top examples are selected, and a minibatch is created from these hard examples. As with our approach, OHEM emphasizes examples with high loss but, critically, OHEM completely discards easy examples. We implement OHEM using the loss computed after the final layer (before focal loss is applied). We use a batch size of 128 with a 1:3 ratio of foreground to background. As shown in Table 1(a), our FL gives better results. We note that we were unable to get OHEM working when training on the full set of ~100k anchors per image as the memory and computation are prohibitive. Instead the results presented use a sample of 512-1024 per image.

**Hinge Loss:** Finally, in early experiments, we attempted to train with the hinge loss on p_t, which sets loss to 0 above a certain value of p_t. However, this was unstable and we do not report numbers.

**Model Architecture Design:** Table 1(c-e) shows the results of various architecture design choices for RetinaNet. The design of the anchor boxes has a modest effect on AP. Using just three scales and three aspect ratios per location we obtain a good result (Table 1(c)). Halving or doubling the number of scales gives a small drop in AP. Using one scale and three aspect ratios or three scales and one aspect ratio drops AP slightly (by 1.3-1.4 points). These results indicate that using a few anchor parameters is sufficient.

Next we analyze the subnet design. Higher capacity subnets improve AP (Table 1(d)). Using four conv layers in the subnets gives a 1.1 AP improvement over using two conv layers. Adding more layers yields diminishing returns. We also tried using batch normalization in the subnets; however, it did not improve accuracy so we opted not to use it for the results reported. Finally, we observe that using separable layers [3] between classification and box regression (not sharing weights) is critical for good accuracy: it improves AP by 1.0 point (Table 1(e)).

**Comparison to State of the Art:** We evaluate RetinaNet on the challenging COCO test-dev dataset that consists of ~20k images. We use an image scale of 800 pixels in the larger dimension for all results unless noted and train using the COCO train set. Systems are compared in Table 2. Our best result achieves 39.1 AP which outperforms the best previously published single-model result from Deformable ConvNets [5] at 34.5 AP. The next best result is from Mask R-CNN [14] at 37.8 AP. Note that we trained the Mask R-CNN model without using mask targets. All the prior art uses ResNet-101 as the base network, while our method also tested ResNet-50 variants, which achieved a strong 37.4 AP. Remarkably, our one-stage detector outperforms all two-stage detectors from the literature.

Compared to the fastest high-accuracy detector from Faster R-CNN [28] (which runs at 5 fps), RetinaNet achieves a 2.3 point AP improvement while running at a similar speed (5 fps), see Figure 2. When using larger image scales, RetinaNet achieves still higher accuracy (40.8 AP at 800 pixel scale and 43.0 AP at 1000 pixels), albeit at reduced speeds.

**Speed versus Accuracy:** Figure 2 shows the trade-off between accuracy and speed for our detector as well as recent methods. On the plot, our method achieves a better speed/accuracy trade-off than all the two-stage methods. The DSSD [12] detector achieves superior speed but at lower accuracy. The one-stage YOLOv2 [27] is faster than our detector but is more than 10 AP points lower in accuracy. Note that for the ResNet-101-800 model, we report a runtime of 122 ms which includes all pre- and post-processing (e.g., image resizing and NMS). This is competitive with comparable Faster R-CNN methods.

---

### النسخة العربية

**تدريب الكشف الكثيف:** نُجري التجارب على مسار كشف صندوق التحديد لمجموعة بيانات COCO الصعبة [21]. للتدريب، نستخدم تقسيم COCO trainval35k الذي يتضمن جميع صور 80 ألف من تقسيم القطار ومجموعة فرعية عشوائية من 35 ألف صورة من تقسيم val البالغ 40 ألف صورة. نُبلغ عن تحليل الآفات والحساسية على تقسيم minival (الصور الـ 5 آلاف المتبقية من val). نُبلغ أيضاً عن النتائج النهائية على تقسيم test-dev الذي ليس له تسميات عامة ويتطلب استخدام خادم التقييم.

**تفاصيل التدريب:** كما هو موضح في §4، يُشكل RetinaNet تنبؤات لحوالي 100 ألف صندوق مرساة لكل صورة. فقط جزء صغير من هذه المراسي سيُخصص لصندوق تحديد حقيقة أرضية. باتباع الممارسة القياسية، نستخدم الخسارة المُركزة على جميع المراسي الـ 100 ألف تقريباً لكل صورة، لكن الخسارة مُطبعة بعدد المراسي المخصصة لصندوق حقيقة أرضية بدلاً من العدد الإجمالي للمراسي حيث أن الغالبية العظمى هي أمثلة سلبية سهلة وتحصل على قيم خسارة ضئيلة تحت الخسارة المُركزة. نجد أن هذا يحسن الاستقرار. أخيراً، نقص التدرجات لمنع التباعد.

**تهيئة الشبكة:** تُجرى التجارب باستخدام عمود فقري ResNet-50-FPN أو ResNet-101-FPN [15، 20]. نستخدم شبكات مُدربة مسبقاً على ImageNet1k [6]. لجميع تجارب الإزالة نستخدم مقياس صورة 600 بكسل؛ لنتائجنا النهائية نستخدم مقياس 800 بكسل لتمكين المقارنة بالطرق الحديثة.

**التحسين:** يُحسن RetinaNet باستخدام SGD على 8 وحدات معالجة رسومات بدفعة صغيرة من صورتين لكل GPU (إذاً إجمالي 16 صورة لكل دفعة صغيرة). ما لم يُذكر، تُدرب النماذج لـ 90 ألف تكرار بدءاً من معدل تعلم 0.01 والذي يُخفض بعد ذلك بعامل 10 عند 60 ألف و80 ألف تكرار. نستخدم انحلال وزن 0.0001 وزخم 0.9. الخسارة هي مجموع الخسارة المُركزة للتصنيف وخسارة L1 الناعمة [10] لانحدار الصندوق.

**الاختبار والتقييم:** للاختبار، نستخدم عتبة 0.05 لثقة الجسم. هذا ينتج عدداً أعلى قليلاً من الكشوفات من العتبة القياسية 0.5 المستخدمة في الأعمال السابقة، لكننا وجدنا أنها تحسن الدقة. تُرتب الصناديق بعد ذلك حسب درجتها ويُعالج أفضل 1000 صندوق تسجيل لكل صورة بواسطة قمع غير الحد الأقصى بعتبة 0.5 لإعطاء الكشوفات النهائية. تُبلغ النتائج باستخدام معيار متوسط الدقة (AP) القياسي بنمط COCO والذي يحسب متوسط AP على عتبات IoU من 0.5 إلى 0.95 بحجم خطوة 0.05.

**الخسارة المُركزة:** لإثبات فعالية الخسارة المُركزة، نقارن مع عدد من البدائل بما في ذلك: (أ) التدريب بخسارة الإنتروبيا المتقاطعة؛ (ب) التدريب بخسارة CE الموزونة بـ α؛ (ج) التدريب بـ OHEM [31]، نهج شائع لمعالجة عدم التوازن بين الفئات. لـ OHEM استخدمنا نسبة 1:3 من الإيجابيات إلى السلبيات. كما هو موضح في الجدول 1(أ)، مع γ = 2 الافتراضي لدينا، تحقق الخسارة المُركزة تحسناً بمقدار 2.9 نقطة AP على خط أساس CE و 2.4 نقطة على CE الموزون بـ α. يوفر OHEM تحسناً متواضعاً بمقدار 0.9 نقطة. عند اختبار CE الموزون بـ α مقابل FL عند قيم γ مختلفة (الجدول 1(ب))، نجد أن أفضل α يختلف بشكل كبير لخسارة CE (0.75) مقابل الخسارة المُركزة (0.25)، مما يؤكد أن حد التعديل (1 − p_t)^γ في FL يخدم غرضاً مختلفاً جوهرياً عن الوزن الثابت α. عند أفضل α لكل إعداد، توفر الخسارة المُركزة (عند γ = 2) مكسباً قدره 3.2 نقطة على أفضل CE موزون بـ α.

لفهم أهمية معامل التركيز γ، ندرب RetinaNet باستخدام FL بإعدادات مختلفة لـ γ موضحة في الجدول 1(ب). عندما γ = 0، FL مكافئ لـ CE. في ظل هذا الإعداد، النموذج غير فعال: لديه خسارة تدريب كبيرة و AP ضعيف. مع زيادة γ قليلاً إلى γ = 0.5، لا يزال النموذج مهيمناً عليه بالأمثلة السلبية السهلة ويتباعد التدريب. تأثير γ كبير: مع γ = 2، يحقق FL تحسناً بمقدار 3.2 نقطة AP على CE (و CE الموزون بـ α). مع زيادات أخرى في γ يتحسن AP قليلاً.

نؤكد أن الشكل الدقيق للخسارة المُركزة ليس حاسماً. في الملحق، نعتبر تجسيدات أخرى للخسارة المُركزة (من خلال تغيير شكل حد التعديل) ونُظهر نتائج مماثلة. مفتاح نجاح الخسارة المُركزة هو تقليل وزن الأمثلة السهلة.

**التنقيب عن الأمثلة الصعبة عبر الإنترنت (OHEM):** [31] طريقة شائعة لتدريب الكواشف أحادية المرحلة لزيادة كفاءة التدريب والدقة. في OHEM، يُسجل كل مثال بخسارته، تُختار الأمثلة العليا، وتُنشأ دفعة صغيرة من هذه الأمثلة الصعبة. كما في نهجنا، يؤكد OHEM على الأمثلة ذات الخسارة العالية لكن، بشكل حاسم، يتجاهل OHEM الأمثلة السهلة تماماً. نُنفذ OHEM باستخدام الخسارة المحسوبة بعد الطبقة النهائية (قبل تطبيق الخسارة المُركزة). نستخدم حجم دفعة 128 بنسبة 1:3 من المقدمة إلى الخلفية. كما هو موضح في الجدول 1(أ)، يعطي FL لدينا نتائج أفضل. نلاحظ أننا لم نتمكن من جعل OHEM يعمل عند التدريب على المجموعة الكاملة من حوالي 100 ألف مرساة لكل صورة حيث أن الذاكرة والحساب باهظان. بدلاً من ذلك، النتائج المقدمة تستخدم عينة من 512-1024 لكل صورة.

**خسارة Hinge:** أخيراً، في التجارب المبكرة، حاولنا التدريب بخسارة hinge على p_t، التي تضبط الخسارة على 0 فوق قيمة معينة من p_t. ومع ذلك، كان هذا غير مستقر ولا نُبلغ عن أرقام.

**تصميم معمارية النموذج:** يُظهر الجدول 1(ج-هـ) نتائج خيارات تصميم معمارية متنوعة لـ RetinaNet. تصميم صناديق المراسي له تأثير متواضع على AP. باستخدام ثلاثة مقاييس فقط وثلاث نسب أبعاد لكل موقع نحصل على نتيجة جيدة (الجدول 1(ج)). تقليل أو مضاعفة عدد المقاييس إلى النصف يعطي انخفاضاً صغيراً في AP. استخدام مقياس واحد وثلاث نسب أبعاد أو ثلاثة مقاييس ونسبة أبعاد واحدة يُخفض AP قليلاً (بمقدار 1.3-1.4 نقطة). تشير هذه النتائج إلى أن استخدام بعض معاملات المرساة كافٍ.

بعد ذلك نحلل تصميم الشبكة الفرعية. الشبكات الفرعية ذات السعة الأعلى تحسن AP (الجدول 1(د)). استخدام أربع طبقات التفاف في الشبكات الفرعية يعطي تحسناً بمقدار 1.1 AP على استخدام طبقتي التفاف. إضافة المزيد من الطبقات ينتج عوائد متناقصة. جربنا أيضاً استخدام تطبيع الدفعة في الشبكات الفرعية؛ ومع ذلك، لم يحسن الدقة لذا اخترنا عدم استخدامه للنتائج المُبلغ عنها. أخيراً، نلاحظ أن استخدام طبقات منفصلة [3] بين التصنيف وانحدار الصندوق (عدم مشاركة الأوزان) حاسم للدقة الجيدة: يحسن AP بمقدار 1.0 نقطة (الجدول 1(هـ)).

**المقارنة بأحدث التقنيات:** نُقيم RetinaNet على مجموعة بيانات COCO test-dev الصعبة التي تتكون من حوالي 20 ألف صورة. نستخدم مقياس صورة 800 بكسل في البُعد الأكبر لجميع النتائج ما لم يُذكر وندرب باستخدام مجموعة تدريب COCO. تُقارن الأنظمة في الجدول 2. أفضل نتيجة لدينا تحقق 39.1 AP والتي تتفوق على أفضل نتيجة منشورة سابقاً لنموذج واحد من Deformable ConvNets [5] عند 34.5 AP. أفضل نتيجة تالية من Mask R-CNN [14] عند 37.8 AP. لاحظ أننا دربنا نموذج Mask R-CNN دون استخدام أهداف القناع. جميع الأعمال السابقة تستخدم ResNet-101 كشبكة أساسية، بينما اختبرت طريقتنا أيضاً متغيرات ResNet-50، التي حققت 37.4 AP قوياً. بشكل ملحوظ، كاشفنا أحادي المرحلة يتفوق على جميع الكواشف ثنائية المرحلة من الأدبيات.

مقارنة بأسرع كاشف عالي الدقة من Faster R-CNN [28] (الذي يعمل بسرعة 5 إطارات في الثانية)، يحقق RetinaNet تحسناً بمقدار 2.3 نقطة AP بينما يعمل بسرعة مماثلة (5 fps)، انظر الشكل 2. عند استخدام مقاييس صور أكبر، يحقق RetinaNet دقة أعلى (40.8 AP عند مقياس 800 بكسل و 43.0 AP عند 1000 بكسل)، وإن كان بسرعات مُخفضة.

**السرعة مقابل الدقة:** يُظهر الشكل 2 المفاضلة بين الدقة والسرعة لكاشفنا بالإضافة إلى الطرق الحديثة. على الرسم، تحقق طريقتنا مفاضلة أفضل بين السرعة/الدقة من جميع الطرق ثنائية المرحلة. يحقق كاشف DSSD [12] سرعة فائقة لكن بدقة أقل. YOLOv2 [27] أحادي المرحلة أسرع من كاشفنا لكنه أقل بأكثر من 10 نقاط AP في الدقة. لاحظ أنه لنموذج ResNet-101-800، نُبلغ عن وقت تشغيل 122 مللي ثانية والذي يتضمن جميع المعالجة المسبقة واللاحقة (مثل، تغيير حجم الصورة و NMS). هذا تنافسي مع طرق Faster R-CNN المماثلة.

---

### Translation Notes

- **Figures referenced:** Figure 2 (speed vs accuracy comparison)
- **Tables referenced:** Table 1(a-e) (ablation studies), Table 2 (comparison to state-of-the-art)
- **Key terms introduced:**
  - Ablation study (تجارب الإزالة)
  - Trainval split (تقسيم trainval)
  - Test-dev split (تقسيم test-dev)
  - Evaluation server (خادم التقييم)
  - Gradient clipping (قص التدرجات)
  - Divergence (التباعد)
  - Trade-off (المفاضلة)
  - Runtime (وقت تشغيل)
  - Pre-processing / Post-processing (المعالجة المسبقة/اللاحقة)

- **Equations:** None
- **Citations:** [21], [15, 20], [6], [10], [31], [5], [14], [28], [12], [27], [3]
- **Special handling:**
  - Dataset names preserved: COCO, ImageNet1k
  - Split names: trainval35k, minival, test-dev
  - Model names: Deformable ConvNets, Mask R-CNN, Faster R-CNN, DSSD, YOLOv2
  - Metrics: AP (Average Precision), IoU (Intersection over Union)
  - Speed measure: fps (frames per second) preserved as إطارات في الثانية
  - OHEM kept as abbreviation
  - NMS (Non-Maximum Suppression) kept as abbreviation

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score: 0.89**

### Back-translation Check

Key technical phrases:
- "تجارب الإزالة" → "Ablation experiments/studies" ✓
- "خادم التقييم" → "Evaluation server" ✓
- "قص التدرجات" → "Gradient clipping" ✓
- "المفاضلة" → "Trade-off" ✓
- "المعالجة المسبقة/اللاحقة" → "Pre-processing/Post-processing" ✓
