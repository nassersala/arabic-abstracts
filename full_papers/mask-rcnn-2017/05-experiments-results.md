# Section 5: Experiments and Results
## القسم 5: التجارب والنتائج

**Section:** experiments-results
**Translation Quality:** 0.89
**Glossary Terms Used:** COCO dataset, Average Precision (AP), instance segmentation, object detection, keypoint detection, ablation study, backbone, FPN, ResNet, ResNeXt, baseline, benchmark

---

### English Version

We present a comprehensive experimental analysis of Mask R-CNN. We report thorough ablation studies on the COCO dataset. We also report results on the COCO instance segmentation and keypoint detection tasks.

**Instance Segmentation Results on COCO**

We compare Mask R-CNN to the state-of-the-art methods in instance segmentation on the COCO dataset. All entries use ResNet or ResNeXt models. Table 1 shows the results on the COCO test-dev set.

Our Mask R-CNN method outperforms all existing state-of-the-art single-model entries on every metric on the COCO instance segmentation task, including the COCO 2016 challenge winner. Without bells and whistles such as multi-scale train/test, horizontal flip test, or OHEM, we achieve a mask AP of 35.7 with ResNet-101-FPN and 37.1 with ResNeXt-101-FPN. This is a significant improvement over the previous best single-model results: MNC at 24.6 mask AP and FCIS+++ at 33.6 mask AP.

Mask R-CNN with ResNet-101-FPN also achieves the top results among single-model entries on the bounding box detection task, with 39.8 box AP. This demonstrates that high-quality instance segmentation enables high-quality object detection.

**Ablation Experiments**

We conduct extensive ablation experiments to analyze Mask R-CNN. All ablation experiments are performed on the COCO trainval35k split. We report mask AP unless otherwise noted.

**Multinomial vs. Independent Masks:** Mask R-CNN decouples mask and class prediction: it predicts a binary mask for each class independently, using a per-pixel sigmoid and a binary loss. As an alternative, we can predict a single multi-class mask using a per-pixel softmax and a multinomial loss (as commonly done in semantic segmentation). Table 2b shows that this alternative decreases mask AP by 5.5 points. This suggests that once an instance is classified, it is sufficient to predict a binary mask without concern for categories, and decoupling of mask and classification is essential for good instance segmentation results.

**Class-Specific vs. Class-Agnostic Masks:** Our default design predicts class-specific masks. Alternatively, we can predict a single mask for all classes (class-agnostic). Table 2b shows that the class-specific design improves mask AP by 2.7 points.

**RoIAlign:** Table 2c shows quantitative results of RoIAlign. For the ResNet-50-C4 backbone, RoIAlign improves mask AP by 3 points over RoIPool. More importantly, we see that RoIAlign has a larger benefit when using more powerful backbones: with ResNet-50-FPN, RoIAlign improves mask AP by 1.5 points; with ResNet-101-FPN, the improvement is 2.1 points. With even larger strides (stride-32 C5 features), the improvement reaches 7.3 points.

We also compare to RoIWarp which was proposed in MNC. Despite also using bilinear resampling, RoIWarp performs on par with RoIPool, showing that alignment is the crucial factor.

**Mask Branch:** In Table 2e we compare multi-layer perceptrons (MLP) and fully convolutional networks (FCN) for mask prediction. Using an MLP with two hidden 1024-d fc layers decreases mask AP by 2.1 points. This verifies our claim that the spatial structure of an FCN is important for pixel-to-pixel mask prediction.

**Network Backbone:** Table 2d shows the impact of deeper networks. Upgrading from ResNet-50 to ResNet-101 improves mask AP by 2.4 points. Upgrading to Feature Pyramid Networks (FPN) further improves mask AP by 2.3 points with ResNet-50 and 2.1 points with ResNet-101. These gains come with only a small computational overhead.

**Object Detection Results**

We also report object detection results on COCO in Table 3. Unsurprisingly, Mask R-CNN outperforms the base variants of Faster R-CNN, demonstrating that the mask branch has a regularization effect. The mask branch improves box AP by 0.9 to 1.4 points.

Furthermore, we achieve state-of-the-art results in bounding box detection. With ResNet-101-FPN, our Mask R-CNN achieves 38.2 box AP on test-dev, which exceeds all existing single-model entries, including the COCO 2016 detection winner (37.7 AP).

**Timing:** With ResNet-101-FPN, our method runs at ~195ms per image on an NVIDIA Tesla M40 GPU, and training on COCO trainval35k takes 32 hours on a single machine with 8 GPUs (32GB memory in total). For ResNet-101-C4, the timing is ~400ms, as res5 layers are expensive. Although Mask R-CNN is slightly slower than Faster R-CNN, we believe this is a reasonable trade-off for the large gains in instance segmentation accuracy.

**Human Pose Estimation on COCO**

Mask R-CNN can also be applied to human pose estimation (keypoint detection) with only minor modifications. We model a keypoint's location as a one-hot binary mask, and adopt Mask R-CNN to predict K masks, one for each of K keypoint types (e.g., left shoulder, right elbow). This task helps demonstrate the generality of our approach.

We report results on the COCO keypoint detection task. For this task, we train on COCO trainval35k. We apply standard keypoint detection metrics. With ResNet-50-FPN, our method achieves 62.7 keypoint AP on test-dev. The winning entry of the COCO 2016 keypoint detection task achieved 59.8 keypoint AP.

Remarkably, we found minimal interaction between the keypoint and mask branches. Predicting masks simultaneously with keypoints only marginally decreases the keypoint AP (by 0.3 points). We believe this is due to the decoupled nature of our approach, where each branch produces independent predictions. Nonetheless, our unified model achieves top results on both instance segmentation and keypoint detection tasks, running at 5 fps.

---

### النسخة العربية

نقدم تحليلاً تجريبياً شاملاً لماسك آر-سي إن إن. نُبلّغ عن دراسات استئصال شاملة على مجموعة بيانات COCO. نُبلّغ أيضاً عن النتائج على مهام تجزئة نسخ الكائنات والكشف عن النقاط المفصلية في COCO.

**نتائج تجزئة نسخ الكائنات على COCO**

نقارن ماسك آر-سي إن إن بالطرق المتقدمة في تجزئة نسخ الكائنات على مجموعة بيانات COCO. تستخدم جميع الإدخالات نماذج ResNet أو ResNeXt. يُظهر الجدول 1 النتائج على مجموعة COCO test-dev.

تتفوق طريقة ماسك آر-سي إن إن على جميع إدخالات النموذج الواحد المتقدمة الموجودة على كل مقياس في مهمة تجزئة نسخ الكائنات COCO، بما في ذلك الفائز بتحدي COCO 2016. بدون حيل إضافية مثل التدريب/الاختبار متعدد المقاييس، أو اختبار القلب الأفقي، أو OHEM، نحقق دقة متوسطة للقناع (mask AP) تبلغ 35.7 مع ResNet-101-FPN و37.1 مع ResNeXt-101-FPN. هذا تحسين كبير عن أفضل نتائج النموذج الواحد السابقة: MNC عند 24.6 mask AP و FCIS+++ عند 33.6 mask AP.

تحقق ماسك آر-سي إن إن مع ResNet-101-FPN أيضاً النتائج الأفضل بين إدخالات النموذج الواحد في مهمة الكشف عن صندوق التحديد، مع دقة متوسطة للصندوق (box AP) تبلغ 39.8. هذا يُظهر أن تجزئة نسخ الكائنات عالية الجودة تمكّن الكشف عن الكائنات عالي الجودة.

**تجارب الاستئصال**

نُجري تجارب استئصال واسعة لتحليل ماسك آر-سي إن إن. تُنفّذ جميع تجارب الاستئصال على تقسيم COCO trainval35k. نُبلّغ عن mask AP ما لم يُذكر خلاف ذلك.

**الأقنعة متعددة الحدود مقابل المستقلة:** تفصل ماسك آر-سي إن إن التنبؤ بالقناع والصنف: تتنبأ بقناع ثنائي لكل صنف بشكل مستقل، باستخدام سيغمويد لكل بكسل وخسارة ثنائية. كبديل، يمكننا التنبؤ بقناع واحد متعدد الفئات باستخدام سوفت ماكس لكل بكسل وخسارة متعددة الحدود (كما هو شائع في التجزئة الدلالية). يُظهر الجدول 2b أن هذا البديل يقلل mask AP بمقدار 5.5 نقطة. هذا يشير إلى أنه بمجرد تصنيف نسخة، يكفي التنبؤ بقناع ثنائي دون القلق بشأن الفئات، وأن فصل القناع والتصنيف ضروري للحصول على نتائج جيدة لتجزئة نسخ الكائنات.

**الأقنعة الخاصة بالصنف مقابل المحايدة للصنف:** يتنبأ تصميمنا الافتراضي بأقنعة خاصة بالصنف. بدلاً من ذلك، يمكننا التنبؤ بقناع واحد لجميع الأصناف (محايد للصنف). يُظهر الجدول 2b أن التصميم الخاص بالصنف يحسن mask AP بمقدار 2.7 نقطة.

**آر أو آي ألاين:** يُظهر الجدول 2c نتائج كمية لآر أو آي ألاين. بالنسبة للعمود الفقري ResNet-50-C4، يحسن آر أو آي ألاين mask AP بمقدار 3 نقاط مقارنة بآر أو آي بول. والأهم من ذلك، نرى أن آر أو آي ألاين له فائدة أكبر عند استخدام أعمدة فقرية أقوى: مع ResNet-50-FPN، يحسن آر أو آي ألاين mask AP بمقدار 1.5 نقطة؛ مع ResNet-101-FPN، التحسين هو 2.1 نقطة. مع خطوات أكبر (ميزات C5 بخطوة 32)، يصل التحسين إلى 7.3 نقطة.

نقارن أيضاً بآر أو آي وارب (RoIWarp) الذي اُقترح في MNC. على الرغم من استخدامه أيضاً لإعادة العينة ثنائية الخطية، يؤدي آر أو آي وارب على قدم المساواة مع آر أو آي بول، مما يُظهر أن المحاذاة هي العامل الحاسم.

**فرع القناع:** في الجدول 2e نقارن الشبكات العصبية متعددة الطبقات الإدراكية (MLP) والشبكات الالتفافية الكاملة (FCN) للتنبؤ بالقناع. استخدام MLP مع طبقتين مخفيتين fc بحجم 1024-d يقلل mask AP بمقدار 2.1 نقطة. هذا يؤكد ادعاءنا بأن البنية المكانية لـ FCN مهمة للتنبؤ بالقناع بكسل تلو بكسل.

**العمود الفقري للشبكة:** يُظهر الجدول 2d تأثير الشبكات الأعمق. يؤدي الترقية من ResNet-50 إلى ResNet-101 إلى تحسين mask AP بمقدار 2.4 نقطة. الترقية إلى شبكات هرم الميزات (FPN) تحسن mask AP بشكل إضافي بمقدار 2.3 نقطة مع ResNet-50 و2.1 نقطة مع ResNet-101. تأتي هذه المكاسب مع عبء حسابي صغير فقط.

**نتائج الكشف عن الكائنات**

نُبلّغ أيضاً عن نتائج الكشف عن الكائنات على COCO في الجدول 3. ليس من المستغرب أن تتفوق ماسك آر-سي إن إن على المتغيرات الأساسية لفاستر آر-سي إن إن، مما يُظهر أن فرع القناع له تأثير تنظيمي. يحسن فرع القناع box AP بمقدار 0.9 إلى 1.4 نقطة.

علاوة على ذلك، نحقق نتائج متقدمة في الكشف عن صندوق التحديد. مع ResNet-101-FPN، تحقق ماسك آر-سي إن إن 38.2 box AP على test-dev، والتي تتجاوز جميع إدخالات النموذج الواحد الموجودة، بما في ذلك الفائز بالكشف في COCO 2016 (37.7 AP).

**التوقيت:** مع ResNet-101-FPN، تعمل طريقتنا عند ~195 ميلي ثانية لكل صورة على GPU من نوع NVIDIA Tesla M40، ويستغرق التدريب على COCO trainval35k 32 ساعة على آلة واحدة مع 8 GPUs (ذاكرة 32GB إجمالاً). بالنسبة لـ ResNet-101-C4، يكون التوقيت ~400 ميلي ثانية، حيث أن طبقات res5 مكلفة. على الرغم من أن ماسك آر-سي إن إن أبطأ قليلاً من فاستر آر-سي إن إن، نعتقد أن هذا مقايضة معقولة للمكاسب الكبيرة في دقة تجزئة نسخ الكائنات.

**تقدير وضعية الإنسان على COCO**

يمكن أيضاً تطبيق ماسك آر-سي إن إن على تقدير وضعية الإنسان (الكشف عن النقاط المفصلية) مع تعديلات بسيطة فقط. نمذج موقع النقطة المفصلية كقناع ثنائي بنقطة ساخنة واحدة، ونعتمد ماسك آر-سي إن إن للتنبؤ بـ K أقنعة، واحد لكل نوع من أنواع النقاط المفصلية K (مثل الكتف الأيسر، الكوع الأيمن). تساعد هذه المهمة في إثبات عمومية نهجنا.

نُبلّغ عن النتائج على مهمة الكشف عن النقاط المفصلية COCO. لهذه المهمة، نُدرّب على COCO trainval35k. نطبق مقاييس الكشف عن النقاط المفصلية القياسية. مع ResNet-50-FPN، تحقق طريقتنا 62.7 keypoint AP على test-dev. حقق الإدخال الفائز لمهمة الكشف عن النقاط المفصلية COCO 2016 نتيجة 59.8 keypoint AP.

بشكل ملحوظ، وجدنا تفاعلاً ضئيلاً بين فرعي النقاط المفصلية والأقنعة. التنبؤ بالأقنعة في وقت واحد مع النقاط المفصلية يقلل فقط بشكل طفيف keypoint AP (بمقدار 0.3 نقطة). نعتقد أن هذا يرجع إلى الطبيعة المفصولة لنهجنا، حيث ينتج كل فرع تنبؤات مستقلة. ومع ذلك، يحقق نموذجنا الموحد نتائج متفوقة على كل من مهام تجزئة نسخ الكائنات والكشف عن النقاط المفصلية، ويعمل بسرعة 5 إطارات في الثانية.

---

### Translation Notes

- **Figures referenced:** Tables 1, 2 (a-e), 3, 4 (not embedded in text)
- **Key terms introduced:**
  - Average Precision (AP) (الدقة المتوسطة)
  - Mask AP (دقة متوسطة للقناع)
  - Box AP (دقة متوسطة للصندوق)
  - Keypoint AP (دقة متوسطة للنقطة المفصلية)
  - Ablation study (دراسة استئصال)
  - Test-dev (اختبار-تطوير)
  - Trainval (تدريب-تحقق)
  - Multi-scale training (تدريب متعدد المقاييس)
  - Horizontal flip (قلب أفقي)
  - OHEM - Online Hard Example Mining (تعدين الأمثلة الصعبة عبر الإنترنت)
  - Regularization effect (تأثير تنظيمي)
  - One-hot mask (قناع بنقطة ساخنة واحدة)
- **Equations:** None (numerical results preserved)
- **Citations:** References to MNC, FCIS, COCO 2016 challenge
- **Special handling:**
  - All AP scores kept as decimal numbers
  - Model names kept in English
  - Dataset names (COCO, test-dev, trainval35k) kept in English
  - Timing measurements preserved in milliseconds and hours
  - GPU specifications kept in English

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89
