# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** experiments, accuracy, model, ImageNet, object detection, classification, neural network, architecture, hyperparameter, latency, efficient

---

### English Version

In this section we first investigate the effects of depthwise convolutions as well as the choice of shrinking by reducing the width of the network rather than the number of layers. We then show the trade offs of reducing the network based on the two hyper-parameters: width multiplier and resolution multiplier and compare results to a number of popular models. We then investigate MobileNets applied to a number of different applications.

#### 4.1. Model Choices

First we show results for MobileNet with depthwise separable convolutions compared to a model built with full convolutions. In Table 4 we see that using depthwise separable convolutions compared to full convolutions only reduces accuracy by 1% on ImageNet was saving tremendously on mult-adds and parameters.

We next show results comparing thinner models with width multiplier to shallower models using less layers. To make MobileNet shallower, the 5 layers of separable filters with feature size 14×14×512 in Table 1 are removed. Table 5 shows that at similar computation and number of parameters, that making MobileNets thinner is 3% better than making them shallower.

#### 4.2. Model Shrinking Hyperparameters

Table 6 shows the accuracy, computation and size trade offs of shrinking the MobileNet architecture with the width multiplier α. Accuracy drops off smoothly until the architecture is made too small at α = 0.25.

Table 7 shows the accuracy, computation and size trade offs for different resolution multipliers by training MobileNets with reduced input resolutions. Accuracy drops off smoothly across resolution.

Figure 4 shows the trade off between ImageNet Accuracy and computation for the 16 models made from the cross product of width multiplier α ∈ {1, 0.75, 0.5, 0.25} and resolutions {224, 192, 160, 128}. Results are log linear with a jump when models get very small at α = 0.25.

Figure 5 shows the trade off between ImageNet Accuracy and number of parameters for the 16 models made from the cross product of width multiplier α ∈ {1, 0.75, 0.5, 0.25} and resolutions {224, 192, 160, 128}.

Table 8 compares full MobileNet to the original GoogleNet [30] and VGG16 [27]. MobileNet is nearly as accurate as VGG16 while being 32 times smaller and 27 times less compute intensive. It is more accurate than GoogleNet while being smaller and more than 2.5 times less computation.

Table 9 compares a reduced MobileNet with width multiplier α = 0.5 and reduced resolution 160×160. Reduced MobileNet is 4% better than AlexNet [19] while being 45× smaller and 9.4× less compute than AlexNet. It is also 4% better than Squeezenet [12] at about the same size and 22× less computation.

#### 4.3. Fine Grained Recognition

We train MobileNet for fine grained recognition on the Stanford Dogs dataset [17]. We extend the approach of [18] and collect an even larger but noisy training set than [18] from the web. We use the noisy web data to pretrain a fine grained dog recognition model and then fine tune the model on the Stanford Dogs training set. Results on Stanford Dogs test set are in Table 10. MobileNet can almost achieve the state of the art results from [18] at greatly reduced computation and size.

#### 4.4. Large Scale Geolocalizaton

PlaNet [35] casts the task of determining where on earth a photo was taken as a classification problem. The approach divides the earth into a grid of geographic cells that serve as the target classes and trains a convolutional neural network on millions of geo-tagged photos. PlaNet has been shown to successfully localize a large variety of photos and to outperform Im2GPS [6, 7] that addresses the same task.

We re-train PlaNet using the MobileNet architecture on the same data. While the full PlaNet model based on the Inception V3 architecture [31] has 52 million parameters and 5.74 billion mult-adds. The MobileNet model has only 13 million parameters with the usual 3 million for the body and 10 million for the final layer and 0.58 Million mult-adds. As shown in Table 11, the MobileNet version delivers only slightly decreased performance compared to PlaNet despite being much more compact. Moreover, it still outperforms Im2GPS by a large margin.

#### 4.5. Face Attributes

Another use-case for MobileNet is compressing large systems with unknown or esoteric training procedures. In a face attribute classification task, we demonstrate a synergistic relationship between MobileNet and distillation [9], a knowledge transfer technique for deep networks. We seek to reduce a large face attribute classifier with 75 million parameters and 1600 million Mult-Adds. The classifier is trained on a multi-attribute dataset similar to YFCC100M [32].

We distill a face attribute classifier using the MobileNet architecture. Distillation [9] works by training the classifier to emulate the outputs of a larger model instead of the ground-truth labels, hence enabling training from large (and potentially infinite) unlabeled datasets. Marrying the scalability of distillation training and the parsimonious parameterization of MobileNet, the end system not only requires no regularization (e.g. weight-decay and early-stopping), but also demonstrates enhanced performances. It is evident from Table 12 that the MobileNet-based classifier is resilient to aggressive model shrinking: it achieves a similar mean average precision across attributes (mean AP) as the in-house while consuming only 1% the Multi-Adds.

#### 4.6. Object Detection

MobileNet can also be deployed as an effective base network in modern object detection systems. We report results for MobileNet trained for object detection on COCO data based on the recent work that won the 2016 COCO challenge [10]. In table 13, MobileNet is compared to VGG and Inception V2 [13] under both Faster-RCNN [23] and SSD [21] framework. In our experiments, SSD is evaluated with 300 input resolution (SSD 300) and Faster-RCNN is compared with both 300 and 600 input resolution (Faster-RCNN 300, Faster-RCNN 600). The Faster-RCNN model evaluates 300 RPN proposal boxes per image. The models are trained on COCO train+val excluding 8k minival images and evaluated on minival. For both frameworks, MobileNet achieves comparable results to other networks with only a fraction of computational complexity and model size.

#### 4.7. Face Embeddings

The FaceNet model is a state of the art face recognition model [25]. It builds face embeddings based on the triplet loss. To build a mobile FaceNet model we use distillation to train by minimizing the squared differences of the output of FaceNet and MobileNet on the training data. Results for very small MobileNet models can be found in table 14.

---

### النسخة العربية

في هذا القسم، نبحث أولاً في تأثيرات التفافات حسب العمق بالإضافة إلى اختيار التقليص عن طريق تقليل عرض الشبكة بدلاً من عدد الطبقات. ثم نعرض المفاضلات الناتجة عن تقليل الشبكة بناءً على المعاملين الفائقين: مضاعف العرض ومضاعف دقة الوضوح ونقارن النتائج بعدد من النماذج الشائعة. ثم نبحث في تطبيق MobileNets على عدد من التطبيقات المختلفة.

#### 4.1. خيارات النموذج

أولاً نعرض نتائج MobileNet مع التفافات قابلة للفصل حسب العمق مقارنة بنموذج مبني بالتفافات كاملة. في الجدول 4 نرى أن استخدام التفافات قابلة للفصل حسب العمق مقارنة بالتفافات كاملة يقلل الدقة بنسبة 1% فقط على ImageNet مع توفير هائل في mult-adds والمعاملات.

نعرض بعد ذلك نتائج تقارن النماذج الأنحف مع مضاعف العرض بالنماذج الأقل عمقاً باستخدام طبقات أقل. لجعل MobileNet أقل عمقاً، تم إزالة 5 طبقات من المرشحات القابلة للفصل بحجم ميزة 14×14×512 في الجدول 1. يوضح الجدول 5 أنه عند عمليات حسابية وعدد معاملات متشابهة، فإن جعل MobileNets أنحف أفضل بنسبة 3% من جعلها أقل عمقاً.

#### 4.2. معاملات تقليص النموذج الفائقة

يوضح الجدول 6 المفاضلات بين الدقة والعمليات الحسابية والحجم الناتجة عن تقليص معمارية MobileNet بمضاعف العرض α. تنخفض الدقة بسلاسة حتى تصبح المعمارية صغيرة جداً عند α = 0.25.

يوضح الجدول 7 المفاضلات بين الدقة والعمليات الحسابية والحجم لمضاعفات دقة وضوح مختلفة عن طريق تدريب MobileNets بدقة وضوح إدخال مخفضة. تنخفض الدقة بسلاسة عبر دقة الوضوح.

يوضح الشكل 4 المفاضلة بين دقة ImageNet والعمليات الحسابية للـ 16 نموذجاً المصنوعة من حاصل الضرب التبادلي لمضاعف العرض α ∈ {1, 0.75, 0.5, 0.25} ودقة الوضوح {224, 192, 160, 128}. النتائج خطية لوغاريتمية مع قفزة عندما تصبح النماذج صغيرة جداً عند α = 0.25.

يوضح الشكل 5 المفاضلة بين دقة ImageNet وعدد المعاملات للـ 16 نموذجاً المصنوعة من حاصل الضرب التبادلي لمضاعف العرض α ∈ {1, 0.75, 0.5, 0.25} ودقة الوضوح {224, 192, 160, 128}.

يقارن الجدول 8 MobileNet الكامل بـ GoogleNet الأصلي [30] و VGG16 [27]. MobileNet دقيق تقريباً مثل VGG16 بينما هو أصغر 32 مرة وأقل كثافة حسابية 27 مرة. إنه أكثر دقة من GoogleNet بينما هو أصغر وأقل عمليات حسابية بأكثر من 2.5 مرة.

يقارن الجدول 9 MobileNet مخفض بمضاعف عرض α = 0.5 ودقة وضوح مخفضة 160×160. MobileNet المخفض أفضل بنسبة 4% من AlexNet [19] بينما هو أصغر 45 مرة وأقل عمليات حسابية 9.4 مرة من AlexNet. إنه أيضاً أفضل بنسبة 4% من Squeezenet [12] بنفس الحجم تقريباً وأقل عمليات حسابية 22 مرة.

#### 4.3. التعرف الدقيق

ندرب MobileNet للتعرف الدقيق على مجموعة بيانات Stanford Dogs [17]. نوسع نهج [18] ونجمع مجموعة تدريبية أكبر ولكن أكثر ضوضاء من [18] من الويب. نستخدم بيانات الويب الضوضائية للتدريب المسبق لنموذج تعرف دقيق على الكلاب ثم نضبط النموذج بدقة على مجموعة تدريب Stanford Dogs. النتائج على مجموعة اختبار Stanford Dogs موجودة في الجدول 10. يمكن لـ MobileNet تحقيق نتائج قريبة من أحدث التقنيات من [18] بعمليات حسابية وحجم مخفضين بشكل كبير.

#### 4.4. التوطين الجغرافي واسع النطاق

تصوغ PlaNet [35] مهمة تحديد مكان التقاط صورة على الأرض كمشكلة تصنيف. يقسم النهج الأرض إلى شبكة من الخلايا الجغرافية التي تعمل كفئات الهدف ويدرب شبكة عصبية التفافية على ملايين الصور الموسومة جغرافياً. تم إثبات نجاح PlaNet في توطين مجموعة كبيرة ومتنوعة من الصور والتفوق على Im2GPS [6, 7] التي تعالج نفس المهمة.

نعيد تدريب PlaNet باستخدام معمارية MobileNet على نفس البيانات. بينما نموذج PlaNet الكامل المبني على معمارية Inception V3 [31] لديه 52 مليون معامل و5.74 مليار mult-adds. نموذج MobileNet لديه فقط 13 مليون معامل مع 3 ملايين المعتادة للجسم و10 ملايين للطبقة النهائية و0.58 مليون mult-adds. كما هو موضح في الجدول 11، تقدم نسخة MobileNet أداءً منخفضاً قليلاً فقط مقارنة بـ PlaNet على الرغم من كونها أكثر إحكاماً بكثير. علاوة على ذلك، لا تزال تتفوق على Im2GPS بهامش كبير.

#### 4.5. سمات الوجه

حالة استخدام أخرى لـ MobileNet هي ضغط الأنظمة الكبيرة ذات إجراءات التدريب غير المعروفة أو الغامضة. في مهمة تصنيف سمات الوجه، نوضح علاقة تآزرية بين MobileNet والتقطير [9]، وهي تقنية نقل المعرفة للشبكات العميقة. نسعى لتقليل مصنف سمات الوجه الكبير مع 75 مليون معامل و1600 مليون Mult-Adds. يتم تدريب المصنف على مجموعة بيانات متعددة السمات مشابهة لـ YFCC100M [32].

نقطر مصنف سمات الوجه باستخدام معمارية MobileNet. يعمل التقطير [9] عن طريق تدريب المصنف لمحاكاة مخرجات نموذج أكبر بدلاً من التسميات الحقيقية، وبالتالي تمكين التدريب من مجموعات بيانات كبيرة (وربما لانهائية) غير موسومة. من خلال الجمع بين قابلية التوسع لتدريب التقطير والتحديد الاقتصادي لمعاملات MobileNet، لا يتطلب النظام النهائي أي تنظيم (مثل تضاؤل الأوزان والإيقاف المبكر) فحسب، بل يظهر أيضاً أداءً محسناً. من الواضح من الجدول 12 أن المصنف المبني على MobileNet مرن للتقليص القوي للنموذج: إنه يحقق متوسط دقة متوسط مشابهاً عبر السمات (mean AP) كما في النموذج الداخلي بينما يستهلك فقط 1% من Multi-Adds.

#### 4.6. كشف الأجسام

يمكن أيضاً نشر MobileNet كشبكة أساسية فعالة في أنظمة كشف الأجسام الحديثة. نقدم نتائج لـ MobileNet مدرب لكشف الأجسام على بيانات COCO بناءً على العمل الأخير الذي فاز بتحدي COCO 2016 [10]. في الجدول 13، تتم مقارنة MobileNet بـ VGG و Inception V2 [13] تحت كل من إطار Faster-RCNN [23] و SSD [21]. في تجاربنا، تم تقييم SSD بدقة وضوح إدخال 300 (SSD 300) وتمت مقارنة Faster-RCNN بكل من دقة وضوح إدخال 300 و600 (Faster-RCNN 300، Faster-RCNN 600). يقيم نموذج Faster-RCNN 300 صندوق مقترح RPN لكل صورة. يتم تدريب النماذج على COCO train+val باستثناء 8k صورة minival وتقييمها على minival. لكلا الإطارين، تحقق MobileNet نتائج قابلة للمقارنة بالشبكات الأخرى مع جزء فقط من التعقيد الحسابي وحجم النموذج.

#### 4.7. تضمينات الوجه

نموذج FaceNet هو نموذج تعرف على الوجه حديث [25]. إنه يبني تضمينات الوجه بناءً على خسارة الثلاثية. لبناء نموذج FaceNet محمول، نستخدم التقطير للتدريب عن طريق تقليل الاختلافات المربعة لمخرجات FaceNet و MobileNet على بيانات التدريب. يمكن العثور على نتائج نماذج MobileNet الصغيرة جداً في الجدول 14.

---

### Translation Notes

- **Figures referenced:** Figure 4 (accuracy vs computation tradeoff), Figure 5 (accuracy vs parameters tradeoff), Table 4-14 (various experimental results)
- **Key terms introduced:** fine grained recognition, Stanford Dogs dataset, geolocalization, PlaNet, Im2GPS, face attributes, distillation, knowledge transfer, COCO, Faster-RCNN, SSD, RPN, FaceNet, triplet loss, embeddings
- **Equations:** None (mainly experimental results and tables)
- **Citations:** [17], [18], [35], [6, 7], [31], [9], [32], [10], [23], [21], [13], [25]
- **Special handling:**
  - Dataset and model names kept in English (Stanford Dogs, PlaNet, Im2GPS, COCO, FaceNet, etc.)
  - "fine grained recognition" = "التعرف الدقيق"
  - "geolocalization" = "التوطين الجغرافي"
  - "face attributes" = "سمات الوجه"
  - "distillation" = "التقطير"
  - "knowledge transfer" = "نقل المعرفة"
  - "embeddings" = "تضمينات"
  - "triplet loss" = "خسارة الثلاثية"
  - Numerical results preserved exactly as in original

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
