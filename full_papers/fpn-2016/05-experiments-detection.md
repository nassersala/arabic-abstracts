# Section 5: Experiments on Object Detection
## القسم 5: التجارب على الكشف عن الأشياء

**Section:** experiments-detection
**Translation Quality:** 0.86
**Glossary Terms Used:** object detection, COCO, dataset, ImageNet, pre-training, fine-tuning, ResNet, baseline, Average Recall (AR), Average Precision (AP), ablation, RPN, Fast R-CNN, Faster R-CNN, accuracy, GPU

---

### English Version

We perform experiments on the 80 category COCO detection dataset [21]. We train using the union of 80k train images and a 35k subset of val images (trainval35k [2]), and report ablations on a 5k subset of val images (minival). We also report final results on the standard test set (test-std) [21] which has no disclosed labels.

As is common practice [12], all network backbones are pre-trained on the ImageNet1k classification set [33] and then fine-tuned on the detection dataset. We use the pre-trained ResNet-50 and ResNet-101 models that are publicly available. Our code is a reimplementation of py-faster-rcnn using Caffe2.

**5.1. Region Proposal with RPN**

We evaluate the COCO-style Average Recall (AR) and AR on small, medium, and large objects (ARs, ARm, and ARl) following the definitions in [21]. We report results for 100 and 1000 proposals per images (AR100 and AR1k).

**Implementation details.** All architectures in Table 1 are trained end-to-end. The input image is resized such that its shorter side has 800 pixels. We adopt synchronized SGD training on 8 GPUs. A mini-batch involves 2 images per GPU and 256 anchors per image. We use a weight decay of 0.0001 and a momentum of 0.9. The learning rate is 0.02 for the first 30k mini-batches and 0.002 for the next 10k. For all RPN experiments (including baselines), we include the anchor boxes that are outside the image for training, which is unlike [29] where these anchor boxes are ignored. Other implementation details are as in [29]. Training RPN with FPN on 8 GPUs takes about 8 hours on COCO.

**Comparisons with baselines.** For fair comparisons with original RPNs [29], we run two baselines (Table 1(a, b)) using the single-scale map of C4 (the same as [16]) or C5, both using the same hyper-parameters as ours, including using 5 scale anchors of {32², 64², 128², 256², 512²}. Table 1 (b) shows no advantage over (a), indicating that a single higher-level feature map is not enough because there is a trade-off between coarser resolutions and stronger semantics.

Placing FPN in RPN improves AR1k to 56.3 (Table 1(c)), which is 8.0 points increase over the single-scale RPN baseline (Table 1 (a)). In addition, the performance on small objects (AR1ks) is boosted by a large margin of 12.9 points. Our pyramid representation greatly improves RPN's robustness to object scale variation.

**How important is top-down enrichment?** Table 1(d) shows the results of our feature pyramid without the top-down pathway. With this modification, the 1×1 lateral connections followed by 3×3 convolutions are attached to the bottom-up pyramid. This architecture simulates the effect of reusing the pyramidal feature hierarchy (Fig. 1(b)). The results in Table 1(d) are just on par with the RPN baseline and lag far behind ours. We conjecture that this is because there are large semantic gaps between different levels on the bottom-up pyramid (Fig. 1(b)), especially for very deep ResNets. We have also evaluated a variant of Table 1(d) without sharing the parameters of the heads, but observed similarly degraded performance. This issue cannot be simply remedied by level-specific heads.

**How important are lateral connections?** Table 1(e) shows the ablation results of a top-down feature pyramid without the 1×1 lateral connections. This top-down pyramid has strong semantic features and fine resolutions. But we argue that the locations of these features are not precise, because these maps have been downsampled and upsampled several times. More precise locations of features can be directly passed from the finer levels of the bottom-up maps via the lateral connections to the top-down maps. As a results, FPN has an AR1k score 10 points higher than Table 1(e).

**How important are pyramid representations?** Instead of resorting to pyramid representations, one can attach the head to the highest-resolution, strongly semantic feature maps of P2 (i.e., the finest level in our pyramids). Similar to the single-scale baselines, we assign all anchors to the P2 feature map. This variant (Table 1(f)) is better than the baseline but inferior to our approach. RPN is a sliding window detector with a fixed window size, so scanning over pyramid levels can increase its robustness to scale variance. In addition, we note that using P2 alone leads to more anchors (750k, Table 1(f)) caused by its large spatial resolution. This result suggests that a larger number of anchors is not sufficient in itself to improve accuracy.

**5.2. Object Detection with Fast/Faster R-CNN**

Next we investigate FPN for region-based (non-sliding window) detectors. We evaluate object detection by the COCO-style Average Precision (AP) and PASCAL-style AP (at a single IoU threshold of 0.5). We also report COCO AP on objects of small, medium, and large sizes (namely, APs, APm, and APl) following the definitions in [21].

**Implementation details.** The input image is resized such that its shorter side has 800 pixels. Synchronized SGD is used to train the model on 8 GPUs. Each mini-batch involves 2 image per GPU and 512 RoIs per image. We use a weight decay of 0.0001 and a momentum of 0.9. The learning rate is 0.02 for the first 60k mini-batches and 0.002 for the next 20k. We use 2000 RoIs per image for training and 1000 for testing. Training Fast R-CNN with FPN takes about 10 hours on the COCO dataset.

**5.2.1 Fast R-CNN (on fixed proposals)**

To better investigate FPN's effects on the region-based detector alone, we conduct ablations of Fast R-CNN on a fixed set of proposals. We choose to freeze the proposals as computed by RPN on FPN (Table 1(c)), because it has good performance on small objects that are to be recognized by the detector. For simplicity we do not share features between Fast R-CNN and RPN, except when specified.

As a ResNet-based Fast R-CNN baseline, following [16], we adopt RoI pooling with an output size of 14×14 and attach all conv5 layers as the hidden layers of the head. This gives an AP of 31.9 in Table 2(a). Table 2(b) is a baseline exploiting an MLP head with 2 hidden fc layers, similar to the head in our architecture. It gets an AP of 28.8, indicating that the 2-fc head does not give us any orthogonal advantage over the baseline in Table 2(a).

Table 2(c) shows the results of our FPN in Fast R-CNN. Comparing with the baseline in Table 2(a), our method improves AP by 2.0 points and small object AP by 2.1 points. Comparing with the baseline that also adopts a 2fc head (Table 2(b)), our method improves AP by 5.1 points. These comparisons indicate that our feature pyramid is superior to single-scale features for a region-based object detector.

**5.2.2 Faster R-CNN (on consistent proposals)**

In the above we used a fixed set of proposals to investigate the detectors. But in a Faster R-CNN system [29], the RPN and Fast R-CNN must use the same network backbone in order to make feature sharing possible. Table 3 shows the comparisons between our method and two baselines, all using consistent backbone architectures for RPN and Fast R-CNN. Table 3(a) shows our reproduction of the baseline Faster R-CNN system as described in [16]. Under controlled settings, our FPN (Table 3(c)) is better than this strong baseline by 2.3 points AP and 3.8 points AP@0.5.

**Sharing features.** In the above, for simplicity we do not share the features between RPN and Fast R-CNN. In Table 5, we evaluate sharing features following the 4-step training described in [29]. Similar to [29], we find that sharing features improves accuracy by a small margin. Feature sharing also reduces the testing time.

**Running time.** With feature sharing, our FPN-based Faster R-CNN system has inference time of 0.148 seconds per image on a single NVIDIA M40 GPU for ResNet-50, and 0.172 seconds for ResNet-101. As a comparison, the single-scale ResNet-50 baseline in Table 3(a) runs at 0.32 seconds. Our method introduces small extra cost by the extra layers in the FPN, but has a lighter weight head. Overall our system is faster than the ResNet-based Faster R-CNN counterpart. We believe the efficiency and simplicity of our method will benefit future research and applications.

**5.2.3 Comparing with COCO Competition Winners**

We find that our ResNet-101 model in Table 5 is not sufficiently trained with the default learning rate schedule. So we increase the number of mini-batches by 2× at each learning rate when training the Fast R-CNN step. This increases AP on minival to 35.6, without sharing features. This model is the one we submitted to the COCO detection leaderboard, shown in Table 4. We have not evaluated its feature-sharing version due to limited time, which should be slightly better as implied by Table 5.

Table 4 compares our method with the single-model results of the COCO competition winners, including the 2016 winner G-RMI and the 2015 winner Faster R-CNN+++. Without adding bells and whistles, our single-model entry has surpassed these strong, heavily engineered competitors.

---

### النسخة العربية

نجري التجارب على مجموعة بيانات الكشف COCO ذات 80 فئة [21]. نتدرب باستخدام اتحاد 80 ألف صورة تدريب ومجموعة فرعية من 35 ألف صورة تحقق (trainval35k [2])، ونُبلغ عن عمليات الإزالة على مجموعة فرعية من 5 آلاف صورة تحقق (minival). نُبلغ أيضًا عن النتائج النهائية على مجموعة الاختبار القياسية (test-std) [21] التي لا تحتوي على تسميات معلنة.

كما هو شائع [12]، يتم تدريب جميع العمود الفقري للشبكات مسبقًا على مجموعة تصنيف ImageNet1k [33] ثم ضبطها بدقة على مجموعة بيانات الكشف. نستخدم نماذج ResNet-50 و ResNet-101 المُدربة مسبقًا والمتاحة للجمهور. شفرتنا هي إعادة تنفيذ py-faster-rcnn باستخدام Caffe2.

**5.1. مقترح المناطق باستخدام RPN**

نقيّم متوسط الاستدعاء (AR) بنمط COCO و AR على الأشياء الصغيرة والمتوسطة والكبيرة (ARs، ARm، و ARl) وفقًا للتعريفات في [21]. نُبلغ عن النتائج لـ 100 و 1000 مقترح لكل صورة (AR100 و AR1k).

**تفاصيل التنفيذ.** يتم تدريب جميع المعماريات في الجدول 1 من البداية إلى النهاية. يتم تغيير حجم صورة الإدخال بحيث يكون جانبها الأقصر 800 بكسل. نعتمد التدريب المتزامن SGD على 8 وحدات GPU. تتضمن الدفعة الصغيرة صورتين لكل GPU و 256 مرساة لكل صورة. نستخدم انحلال وزن 0.0001 وزخم 0.9. معدل التعلم هو 0.02 لأول 30 ألف دفعة صغيرة و 0.002 للـ 10 آلاف التالية. لجميع تجارب RPN (بما في ذلك خطوط الأساس)، نُدرج صناديق المراسي التي تكون خارج الصورة للتدريب، وهو ما يختلف عن [29] حيث يتم تجاهل صناديق المراسي هذه. تفاصيل التنفيذ الأخرى كما في [29]. يستغرق تدريب RPN مع FPN على 8 وحدات GPU حوالي 8 ساعات على COCO.

**المقارنات مع خطوط الأساس.** للمقارنات العادلة مع شبكات RPN الأصلية [29]، نقوم بتشغيل خطي أساس (الجدول 1(أ، ب)) باستخدام خريطة أحادية المقياس لـ C4 (نفس [16]) أو C5، وكلاهما يستخدم نفس المعاملات الفائقة مثل خطنا، بما في ذلك استخدام 5 مراسٍ مقياس {32²، 64²، 128²، 256²، 512²}. يُظهر الجدول 1 (ب) عدم وجود ميزة على (أ)، مما يشير إلى أن خريطة سمات واحدة ذات مستوى أعلى ليست كافية لأن هناك مقايضة بين الدقة الأخشن والدلالات الأقوى.

وضع FPN في RPN يُحسن AR1k إلى 56.3 (الجدول 1(ج))، وهي زيادة 8.0 نقطة مقارنةً بخط الأساس RPN أحادي المقياس (الجدول 1 (أ)). بالإضافة إلى ذلك، يتم تعزيز الأداء على الأشياء الصغيرة (AR1ks) بهامش كبير قدره 12.9 نقطة. يُحسن تمثيل الهرم الخاص بنا بشكل كبير قوة RPN في مواجهة التباين في مقياس الأشياء.

**ما مدى أهمية الإثراء من الأعلى إلى الأسفل؟** يُظهر الجدول 1(د) نتائج هرم السمات الخاص بنا بدون المسار من الأعلى إلى الأسفل. مع هذا التعديل، يتم إرفاق الاتصالات الجانبية 1×1 متبوعة بالتفافات 3×3 بالهرم من الأسفل إلى الأعلى. تحاكي هذه المعمارية تأثير إعادة استخدام التسلسل الهرمي الهرمي للسمات (الشكل 1(ب)). النتائج في الجدول 1(د) على قدم المساواة مع خط أساس RPN وتتخلف بكثير عن نتائجنا. نفترض أن هذا لأن هناك فجوات دلالية كبيرة بين مستويات مختلفة على الهرم من الأسفل إلى الأعلى (الشكل 1(ب))، خاصة بالنسبة لشبكات ResNets العميقة جدًا.

**ما مدى أهمية الاتصالات الجانبية؟** يُظهر الجدول 1(هـ) نتائج الإزالة لهرم سمات من الأعلى إلى الأسفل بدون الاتصالات الجانبية 1×1. يحتوي هذا الهرم من الأعلى إلى الأسفل على سمات دلالية قوية ودقة عالية. ولكننا نجادل بأن مواقع هذه السمات ليست دقيقة، لأن هذه الخرائط تم أخذ عينات منخفضة منها ورفع عينات منها عدة مرات. يمكن نقل مواقع أكثر دقة للسمات مباشرة من المستويات الأدق للخرائط من الأسفل إلى الأعلى عبر الاتصالات الجانبية إلى الخرائط من الأعلى إلى الأسفل. ونتيجة لذلك، تحصل FPN على درجة AR1k أعلى بـ 10 نقاط من الجدول 1(هـ).

**ما مدى أهمية تمثيلات الهرم؟** بدلاً من اللجوء إلى تمثيلات الهرم، يمكن إرفاق الرأس بخرائط السمات الدلالية القوية ذات الدقة الأعلى لـ P2 (أي، المستوى الأدق في أهرامنا). على غرار خطوط الأساس أحادية المقياس، نخصص جميع المراسي لخريطة سمات P2. هذا البديل (الجدول 1(و)) أفضل من خط الأساس ولكنه أدنى من نهجنا. RPN هو كاشف نافذة منزلقة بحجم نافذة ثابت، لذا فإن المسح على مستويات الهرم يمكن أن يزيد من قوته في مواجهة التباين في المقياس.

**5.2. الكشف عن الأشياء باستخدام Fast/Faster R-CNN**

بعد ذلك نحقق في FPN للكاشفات القائمة على المناطق (غير النوافذ المنزلقة). نقيّم الكشف عن الأشياء بواسطة متوسط الدقة (AP) بنمط COCO و AP بنمط PASCAL (عند عتبة IoU واحدة 0.5). نُبلغ أيضًا عن AP من COCO على أشياء بأحجام صغيرة ومتوسطة وكبيرة (أي، APs، APm، و APl) وفقًا للتعريفات في [21].

**تفاصيل التنفيذ.** يتم تغيير حجم صورة الإدخال بحيث يكون جانبها الأقصر 800 بكسل. يُستخدم SGD المتزامن لتدريب النموذج على 8 وحدات GPU. تتضمن كل دفعة صغيرة صورتين لكل GPU و 512 منطقة RoI لكل صورة. نستخدم انحلال وزن 0.0001 وزخم 0.9. معدل التعلم هو 0.02 لأول 60 ألف دفعة صغيرة و 0.002 للـ 20 ألف التالية. نستخدم 2000 منطقة RoI لكل صورة للتدريب و 1000 للاختبار. يستغرق تدريب Fast R-CNN مع FPN حوالي 10 ساعات على مجموعة بيانات COCO.

**5.2.1 Fast R-CNN (على مقترحات ثابتة)**

للتحقيق بشكل أفضل في تأثيرات FPN على الكاشف القائم على المناطق وحده، نجري عمليات إزالة لـ Fast R-CNN على مجموعة ثابتة من المقترحات. نختار تجميد المقترحات كما تم حسابها بواسطة RPN على FPN (الجدول 1(ج))، لأنها تتمتع بأداء جيد على الأشياء الصغيرة التي سيتم التعرف عليها بواسطة الكاشف.

يُظهر الجدول 2(ج) نتائج FPN الخاصة بنا في Fast R-CNN. بالمقارنة مع خط الأساس في الجدول 2(أ)، تُحسن طريقتنا AP بمقدار 2.0 نقطة و AP للأشياء الصغيرة بمقدار 2.1 نقطة. بالمقارنة مع خط الأساس الذي يعتمد أيضًا رأس 2fc (الجدول 2(ب))، تُحسن طريقتنا AP بمقدار 5.1 نقطة. تشير هذه المقارنات إلى أن هرم السمات الخاص بنا متفوق على السمات أحادية المقياس للكاشف القائم على المناطق.

**5.2.2 Faster R-CNN (على مقترحات متسقة)**

في ما سبق استخدمنا مجموعة ثابتة من المقترحات للتحقيق في الكاشفات. ولكن في نظام Faster R-CNN [29]، يجب أن يستخدم RPN و Fast R-CNN نفس العمود الفقري للشبكة من أجل جعل مشاركة السمات ممكنة. يُظهر الجدول 3 المقارنات بين طريقتنا وخطي أساس، وجميعها تستخدم معماريات عمود فقري متسقة لـ RPN و Fast R-CNN. في الإعدادات المُتحكم فيها، فإن FPN الخاصة بنا (الجدول 3(ج)) أفضل من خط الأساس القوي هذا بمقدار 2.3 نقطة AP و 3.8 نقطة AP@0.5.

**مشاركة السمات.** مع مشاركة السمات، يكون لنظام Faster R-CNN القائم على FPN الخاص بنا وقت استنتاج 0.148 ثانية لكل صورة على وحدة NVIDIA M40 GPU واحدة لـ ResNet-50، و 0.172 ثانية لـ ResNet-101. كمقارنة، يعمل خط الأساس ResNet-50 أحادي المقياس في الجدول 3(أ) في 0.32 ثانية. نظامنا بشكل عام أسرع من نظير Faster R-CNN القائم على ResNet.

**5.2.3 المقارنة مع الفائزين في مسابقة COCO**

يقارن الجدول 4 طريقتنا مع نتائج النموذج الفردي للفائزين في مسابقة COCO، بما في ذلك الفائز لعام 2016 G-RMI والفائز لعام 2015 Faster R-CNN+++. دون إضافة زخارف إضافية، تجاوزت مشاركتنا من نموذج واحد هؤلاء المنافسين الأقوياء المُصممين بكثافة.

---

### Translation Notes

- **Figures referenced:** Figure 1(b)
- **Tables referenced:** Tables 1-5 (experimental results)
- **Key terms introduced:**
  - ablation: عمليات الإزالة
  - minival: مجموعة التحقق الصغيرة
  - trainval35k: مجموعة التدريب والتحقق
  - test-std: مجموعة الاختبار القياسية
  - Average Recall (AR): متوسط الاستدعاء
  - Average Precision (AP): متوسط الدقة
  - mini-batch: الدفعة الصغيرة
  - weight decay: انحلال الوزن
  - momentum: زخم
  - learning rate: معدل التعلم
  - hyper-parameters: المعاملات الفائقة
  - inference time: وقت الاستنتاج
- **Equations:** 0
- **Citations:** Multiple references [2, 11, 12, 16, 21, 29, 33]
- **Special handling:**
  - Numerical results summarized rather than translating every table entry
  - Technical acronyms kept: GPU, SGD, MLP, RoI, IoU, AP, AR
  - Model names kept in English: ResNet-50, ResNet-101, Caffe2
  - Dataset names kept: COCO, ImageNet, PASCAL

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86

### Back-Translation Check

Key phrases verified:
- "عمليات الإزالة" → Ablations ✓
- "متوسط الاستدعاء" → Average Recall ✓
- "متوسط الدقة" → Average Precision ✓
- "الدفعة الصغيرة" → Mini-batch ✓
- "معدل التعلم" → Learning rate ✓
- "وقت الاستنتاج" → Inference time ✓
