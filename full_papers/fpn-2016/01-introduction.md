# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.90
**Glossary Terms Used:** computer vision, feature pyramid, multi-scale, deep learning, convolutional neural network, object detection, architecture, semantic, ResNets, segmentation, accuracy, baseline

---

### English Version

Recognizing objects at vastly different scales is a fundamental challenge in computer vision. Feature pyramids built upon image pyramids (for short we call these featurized image pyramids) form the basis of a standard solution [1] (Fig. 1(a)). These pyramids are scale-invariant in the sense that an object's scale change is offset by shifting its level in the pyramid. Intuitively, this property enables a model to detect objects across a large range of scales by scanning the model over both positions and pyramid levels.

Featurized image pyramids were heavily used in the era of hand-engineered features [5, 25]. They were so critical that object detectors like DPM [7] required dense scale sampling to achieve good results (e.g., 10 scales per octave). For recognition tasks, engineered features have largely been replaced with features computed by deep convolutional networks (ConvNets) [19, 20]. Aside from being capable of representing higher-level semantics, ConvNets are also more robust to variance in scale and thus facilitate recognition from features computed on a single input scale [15, 11, 29] (Fig. 1(b)). But even with this robustness, pyramids are still needed to get the most accurate results. All recent top entries in the ImageNet [33] and COCO [21] detection challenges use multi-scale testing on featurized image pyramids (e.g., [16, 35]). The principle advantage of featurizing each level of an image pyramid is that it produces a multi-scale feature representation in which all levels are semantically strong, including the high-resolution levels.

Nevertheless, featurizing each level of an image pyramid has obvious limitations. Inference time increases considerably (e.g., by four times [11]), making this approach impractical for real applications. Moreover, training deep networks end-to-end on an image pyramid is infeasible in terms of memory, and so, if exploited, image pyramids are used only at test time [15, 11, 16, 35], which creates an inconsistency between train/test-time inference. For these reasons, Fast and Faster R-CNN [11, 29] opt to not use featurized image pyramids under default settings.

However, image pyramids are not the only way to compute a multi-scale feature representation. A deep ConvNet computes a feature hierarchy layer by layer, and with subsampling layers the feature hierarchy has an inherent multi-scale, pyramidal shape. This in-network feature hierarchy produces feature maps of different spatial resolutions, but introduces large semantic gaps caused by different depths. The high-resolution maps have low-level features that harm their representational capacity for object recognition.

The Single Shot Detector (SSD) [22] is one of the first attempts at using a ConvNet's pyramidal feature hierarchy as if it were a featurized image pyramid (Fig. 1(c)). Ideally, the SSD-style pyramid would reuse the multi-scale feature maps from different layers computed in the forward pass and thus come free of cost. But to avoid using low-level features SSD foregoes reusing already computed layers and instead builds the pyramid starting from high up in the network (e.g., conv4_3 of VGG nets [36]) and then by adding several new layers. Thus it misses the opportunity to reuse the higher-resolution maps of the feature hierarchy. We show that these are important for detecting small objects.

The goal of this paper is to naturally leverage the pyramidal shape of a ConvNet's feature hierarchy while creating a feature pyramid that has strong semantics at all scales. To achieve this goal, we rely on an architecture that combines low-resolution, semantically strong features with high-resolution, semantically weak features via a top-down pathway and lateral connections (Fig. 1(d)). The result is a feature pyramid that has rich semantics at all levels and is built quickly from a single input image scale. In other words, we show how to create in-network feature pyramids that can be used to replace featurized image pyramids without sacrificing representational power, speed, or memory.

Similar architectures adopting top-down and skip connections are popular in recent research [28, 17, 8, 26]. Their goals are to produce a single high-level feature map of a fine resolution on which the predictions are to be made (Fig. 2 top). On the contrary, our method leverages the architecture as a feature pyramid where predictions (e.g., object detections) are independently made on each level (Fig. 2 bottom). Our model echoes a featurized image pyramid, which has not been explored in these works.

We evaluate our method, called a Feature Pyramid Network (FPN), in various systems for detection and segmentation [11, 29, 27]. Without bells and whistles, we report a state-of-the-art single-model result on the challenging COCO detection benchmark [21] simply based on FPN and a basic Faster R-CNN detector [29], surpassing all existing heavily-engineered single-model entries of competition winners. In ablation experiments, we find that for bounding box proposals, FPN significantly increases the Average Recall (AR) by 8.0 points; for object detection, it improves the COCO-style Average Precision (AP) by 2.3 points and PASCAL-style AP by 3.8 points, over a strong single-scale baseline of Faster R-CNN on ResNets [16]. Our method is also easily extended to mask proposals and improves both instance segmentation AR and speed over state-of-the-art methods that heavily depend on image pyramids.

In addition, our pyramid structure can be trained end-to-end with all scales and is used consistently at train/test time, which would be memory-infeasible using image pyramids. As a result, FPNs are able to achieve higher accuracy than all existing state-of-the-art methods. Moreover, this improvement is achieved without increasing testing time over the single-scale baseline. We believe these advances will facilitate future research and applications. Our code will be made publicly available.

---

### النسخة العربية

يُعد التعرف على الأشياء بمقاييس مختلفة إلى حد كبير تحديًا أساسيًا في الرؤية الحاسوبية. تُشكل أهرام السمات المبنية على أهرام الصور (نسميها اختصارًا أهرام الصور المُسمّتة) أساس حل قياسي [1] (الشكل 1(أ)). هذه الأهرام ثابتة المقياس بمعنى أن تغيير مقياس الشيء يتم تعويضه بتحريك مستواه في الهرم. بشكل بديهي، تُمكّن هذه الخاصية النموذج من الكشف عن الأشياء عبر نطاق كبير من المقاييس عن طريق مسح النموذج على كل من المواضع ومستويات الهرم.

تم استخدام أهرام الصور المُسمّتة بكثافة في عصر السمات المُصممة يدويًا [5، 25]. كانت حاسمة لدرجة أن كاشفات الأشياء مثل DPM [7] تطلبت أخذ عينات كثيفة من المقاييس لتحقيق نتائج جيدة (على سبيل المثال، 10 مقاييس لكل أوكتاف). بالنسبة لمهام التعرف، تم استبدال السمات المُصممة إلى حد كبير بالسمات المحسوبة بواسطة الشبكات الالتفافية العميقة (ConvNets) [19، 20]. بصرف النظر عن قدرتها على تمثيل دلالات من المستوى الأعلى، فإن الشبكات الالتفافية أيضًا أكثر قوة في مواجهة التباين في المقياس وبالتالي تسهل التعرف من السمات المحسوبة على مقياس إدخال واحد [15، 11، 29] (الشكل 1(ب)). ولكن حتى مع هذه القوة، لا تزال الأهرام مطلوبة للحصول على النتائج الأكثر دقة. جميع المشاركات الأعلى الأخيرة في تحديات الكشف في ImageNet [33] و COCO [21] تستخدم الاختبار متعدد النطاقات على أهرام الصور المُسمّتة (على سبيل المثال، [16، 35]). الميزة الرئيسية لتسميت كل مستوى من هرم الصورة هي أنه ينتج تمثيل سمات متعدد النطاقات حيث جميع المستويات قوية دلاليًا، بما في ذلك المستويات عالية الدقة.

ومع ذلك، فإن تسميت كل مستوى من هرم الصورة له قيود واضحة. يزداد وقت الاستنتاج بشكل كبير (على سبيل المثال، بأربعة أضعاف [11])، مما يجعل هذا النهج غير عملي للتطبيقات الحقيقية. علاوة على ذلك، فإن تدريب الشبكات العميقة من البداية إلى النهاية على هرم صورة غير ممكن من حيث الذاكرة، وبالتالي، إذا تم استغلالها، يتم استخدام أهرام الصور فقط في وقت الاختبار [15، 11، 16، 35]، مما يخلق عدم اتساق بين الاستنتاج في وقت التدريب/الاختبار. لهذه الأسباب، تختار Fast R-CNN و Faster R-CNN [11، 29] عدم استخدام أهرام الصور المُسمّتة في الإعدادات الافتراضية.

ومع ذلك، فإن أهرام الصور ليست الطريقة الوحيدة لحساب تمثيل سمات متعدد النطاقات. تحسب الشبكة الالتفافية العميقة تسلسلاً هرميًا من السمات طبقة تلو الأخرى، ومع طبقات أخذ العينات الفرعية يكون للتسلسل الهرمي للسمات شكل هرمي متعدد النطاقات بطبيعته. ينتج هذا التسلسل الهرمي للسمات داخل الشبكة خرائط سمات ذات دقة مكانية مختلفة، ولكنه يقدم فجوات دلالية كبيرة ناتجة عن أعماق مختلفة. تحتوي الخرائط عالية الدقة على سمات منخفضة المستوى تضر بقدرتها التمثيلية للتعرف على الأشياء.

يُعد الكاشف أحادي الطلقة (SSD) [22] أحد المحاولات الأولى لاستخدام التسلسل الهرمي الهرمي للسمات في الشبكة الالتفافية كما لو كان هرم صورة مُسمّت (الشكل 1(ج)). من الناحية المثالية، فإن الهرم بنمط SSD سيعيد استخدام خرائط السمات متعددة النطاقات من طبقات مختلفة محسوبة في المرور الأمامي وبالتالي يأتي بدون تكلفة. ولكن لتجنب استخدام السمات منخفضة المستوى، يتخلى SSD عن إعادة استخدام الطبقات المحسوبة بالفعل وبدلاً من ذلك يبني الهرم بدءًا من أعلى في الشبكة (على سبيل المثال، conv4_3 من شبكات VGG [36]) ثم بإضافة عدة طبقات جديدة. وبالتالي فإنه يفوت فرصة إعادة استخدام الخرائط عالية الدقة من التسلسل الهرمي للسمات. نُظهر أن هذه مهمة للكشف عن الأشياء الصغيرة.

الهدف من هذا البحث هو الاستفادة بشكل طبيعي من الشكل الهرمي للتسلسل الهرمي للسمات في الشبكة الالتفافية مع إنشاء هرم سمات له دلالات قوية على جميع النطاقات. لتحقيق هذا الهدف، نعتمد على معمارية تجمع بين السمات منخفضة الدقة القوية دلاليًا مع السمات عالية الدقة الضعيفة دلاليًا عبر مسار من الأعلى إلى الأسفل واتصالات جانبية (الشكل 1(د)). النتيجة هي هرم سمات له دلالات غنية على جميع المستويات ويُبنى بسرعة من مقياس صورة إدخال واحد. بعبارة أخرى، نُظهر كيفية إنشاء أهرام سمات داخل الشبكة يمكن استخدامها لاستبدال أهرام الصور المُسمّتة دون التضحية بالقدرة التمثيلية أو السرعة أو الذاكرة.

المعماريات المماثلة التي تعتمد الاتصالات من الأعلى إلى الأسفل والاتصالات القافزة شائعة في الأبحاث الحديثة [28، 17، 8، 26]. أهدافها هي إنتاج خريطة سمات واحدة عالية المستوى بدقة عالية يتم عليها إجراء التنبؤات (الشكل 2 أعلى). على العكس من ذلك، تستفيد طريقتنا من المعمارية كهرم سمات حيث يتم إجراء التنبؤات (على سبيل المثال، اكتشافات الأشياء) بشكل مستقل على كل مستوى (الشكل 2 أسفل). يحاكي نموذجنا هرم صورة مُسمّت، والذي لم يتم استكشافه في هذه الأعمال.

نقوم بتقييم طريقتنا، التي تسمى شبكة هرم السمات (FPN)، في أنظمة مختلفة للكشف والتجزئة [11، 29، 27]. دون زخارف إضافية، نُبلغ عن نتيجة حديثة من نموذج واحد على معيار الكشف COCO الصعب [21] بناءً ببساطة على FPN وكاشف Faster R-CNN الأساسي [29]، متفوقين على جميع المشاركات الموجودة من نموذج واحد المُصممة بكثافة من الفائزين في المسابقة. في تجارب الإزالة، نجد أنه بالنسبة لمقترحات صناديق التحديد، تزيد FPN بشكل كبير متوسط الاستدعاء (AR) بمقدار 8.0 نقاط؛ للكشف عن الأشياء، يُحسن متوسط الدقة بنمط COCO (AP) بمقدار 2.3 نقطة و AP بنمط PASCAL بمقدار 3.8 نقاط، مقارنةً بخط أساس قوي أحادي المقياس من Faster R-CNN على ResNets [16]. يمكن أيضًا تمديد طريقتنا بسهولة إلى مقترحات القناع وتُحسن كلاً من AR للتجزئة حسب المثيل والسرعة مقارنةً بطرق الحالة الحديثة التي تعتمد بشكل كبير على أهرام الصور.

بالإضافة إلى ذلك، يمكن تدريب بنية الهرم الخاصة بنا من البداية إلى النهاية مع جميع النطاقات ويتم استخدامها بشكل متسق في وقت التدريب/الاختبار، وهو ما سيكون غير ممكن من حيث الذاكرة باستخدام أهرام الصور. ونتيجة لذلك، تستطيع شبكات FPN تحقيق دقة أعلى من جميع طرق الحالة الحديثة الموجودة. علاوة على ذلك، يتم تحقيق هذا التحسين دون زيادة وقت الاختبار مقارنةً بخط الأساس أحادي المقياس. نعتقد أن هذه التطورات ستُسهل الأبحاث والتطبيقات المستقبلية. سيتم إتاحة الشفرة البرمجية للجمهور.

---

### Translation Notes

- **Figures referenced:** Figure 1(a), 1(b), 1(c), 1(d), Figure 2
- **Key terms introduced:**
  - featurized image pyramids: أهرام الصور المُسمّتة
  - scale-invariant: ثابتة المقياس
  - hand-engineered features: السمات المُصممة يدويًا
  - ConvNets: الشبكات الالتفافية
  - semantic gaps: فجوات دلالية
  - top-down pathway: مسار من الأعلى إلى الأسفل
  - skip connections: الاتصالات القافزة
  - ablation experiments: تجارب الإزالة
  - Average Recall (AR): متوسط الاستدعاء
  - Average Precision (AP): متوسط الدقة
  - instance segmentation: التجزئة حسب المثيل
- **Equations:** 0
- **Citations:** Multiple references [1-36], including DPM, ImageNet, COCO, SSD, VGG, ResNets, Faster R-CNN
- **Special handling:**
  - Kept technical names like "DPM", "SSD", "VGG", "ResNets", "Faster R-CNN", "Fast R-CNN" in English
  - "conv4_3" kept as technical layer notation
  - "octave" translated as "أوكتاف" (standard musical/scale term)

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.89
- Glossary consistency: 0.87
- **Overall section score:** 0.90

### Back-Translation Check

Key phrases verified:
- "أهرام الصور المُسمّتة" → Featurized image pyramids ✓
- "ثابتة المقياس" → Scale-invariant ✓
- "الشبكات الالتفافية العميقة" → Deep convolutional networks ✓
- "فجوات دلالية كبيرة" → Large semantic gaps ✓
- "مسار من الأعلى إلى الأسفل واتصالات جانبية" → Top-down pathway and lateral connections ✓
