# Section 4: Applications
## القسم 4: التطبيقات

**Section:** applications
**Translation Quality:** 0.87
**Glossary Terms Used:** feature pyramid, RPN, bounding box, object detection, architecture, ResNets, RoI pooling, classification, regression, anchors

---

### English Version

Our method is a generic solution for building feature pyramids inside deep ConvNets. In the following we adopt our method in RPN [29] for bounding box proposal generation and in Fast R-CNN [11] for object detection. To demonstrate the simplicity and effectiveness of our method, we make minimal modifications to the original systems of [29, 11] when adapting them to our feature pyramid.

**4.1. Feature Pyramid Networks for RPN**

RPN [29] is a sliding-window class-agnostic object detector. In the original RPN design, a small subnetwork is evaluated on dense 3×3 sliding windows, on top of a single-scale convolutional feature map, performing object/non-object binary classification and bounding box regression. This is realized by a 3×3 convolutional layer followed by two sibling 1×1 convolutions for classification and regression, which we refer to as a network head. The object/non-object criterion and bounding box regression target are defined with respect to a set of reference boxes called anchors [29]. The anchors are of multiple pre-defined scales and aspect ratios in order to cover objects of different shapes.

We adapt RPN by replacing the single-scale feature map with our FPN. We attach a head of the same design (3×3 conv and two sibling 1×1 convs) to each level on our feature pyramid. Because the head slides densely over all locations in all pyramid levels, it is not necessary to have multi-scale anchors on a specific level. Instead, we assign anchors of a single scale to each level. Formally, we define the anchors to have areas of {32², 64², 128², 256², 512²} pixels on {P2, P3, P4, P5, P6} respectively. As in [29] we also use anchors of multiple aspect ratios {1:2, 1:1, 2:1} at each level. So in total there are 15 anchors over the pyramid.

We assign training labels to the anchors based on their Intersection-over-Union (IoU) ratios with ground-truth bounding boxes as in [29]. Formally, an anchor is assigned a positive label if it has the highest IoU for a given ground-truth box or an IoU over 0.7 with any ground-truth box, and a negative label if it has IoU lower than 0.3 for all ground-truth boxes. Note that scales of ground-truth boxes are not explicitly used to assign them to the levels of the pyramid; instead, ground-truth boxes are associated with anchors, which have been assigned to pyramid levels. As such, we introduce no extra rules in addition to those in [29].

We note that the parameters of the heads are shared across all feature pyramid levels; we have also evaluated the alternative without sharing parameters and observed similar accuracy. The good performance of sharing parameters indicates that all levels of our pyramid share similar semantic levels. This advantage is analogous to that of using a featurized image pyramid, where a common head classifier can be applied to features computed at any image scale.

With the above adaptations, RPN can be naturally trained and tested with our FPN, in the same fashion as in [29]. We elaborate on the implementation details in the experiments.

**4.2. Feature Pyramid Networks for Fast R-CNN**

Fast R-CNN [11] is a region-based object detector in which Region-of-Interest (RoI) pooling is used to extract features. Fast R-CNN is most commonly performed on a single-scale feature map. To use it with our FPN, we need to assign RoIs of different scales to the pyramid levels.

We view our feature pyramid as if it were produced from an image pyramid. Thus we can adapt the assignment strategy of region-based detectors [15, 11] in the case when they are run on image pyramids. Formally, we assign an RoI of width w and height h (on the input image to the network) to the level Pk of our feature pyramid by:

$$k = \lfloor k_0 + \log_2(\sqrt{wh}/224) \rfloor. \tag{1}$$

Here 224 is the canonical ImageNet pre-training size, and k₀ is the target level on which an RoI with w × h = 224² should be mapped into. Analogous to the ResNet-based Faster R-CNN system [16] that uses C4 as the single-scale feature map, we set k₀ to 4. Intuitively, Eqn. (1) means that if the RoI's scale becomes smaller (say, 1/2 of 224), it should be mapped into a finer-resolution level (say, k = 3).

We attach predictor heads (in Fast R-CNN the heads are class-specific classifiers and bounding box regressors) to all RoIs of all levels. Again, the heads all share parameters, regardless of their levels. In [16], a ResNet's conv5 layers (a 9-layer deep subnetwork) are adopted as the head on top of the conv4 features, but our method has already harnessed conv5 to construct the feature pyramid. So unlike [16], we simply adopt RoI pooling to extract 7×7 features, and attach two hidden 1,024-d fully-connected (fc) layers (each followed by ReLU) before the final classification and bounding box regression layers. These layers are randomly initialized, as there are no pre-trained fc layers available in ResNets. Note that compared to the standard conv5 head, our 2-fc MLP head is lighter weight and faster.

Based on these adaptations, we can train and test Fast R-CNN on top of the feature pyramid. Implementation details are given in the experimental section.

---

### النسخة العربية

طريقتنا هي حل عام لبناء أهرام السمات داخل الشبكات الالتفافية العميقة. فيما يلي نعتمد طريقتنا في RPN [29] لتوليد مقترحات صناديق التحديد وفي Fast R-CNN [11] للكشف عن الأشياء. لإظهار بساطة وفعالية طريقتنا، نقوم بإجراء تعديلات قليلة على الأنظمة الأصلية لـ [29، 11] عند تكييفها مع هرم السمات الخاص بنا.

**4.1. شبكات هرم السمات لـ RPN**

RPN [29] هو كاشف أشياء مستقل عن الفئة بنافذة منزلقة. في التصميم الأصلي لـ RPN، يتم تقييم شبكة فرعية صغيرة على نوافذ منزلقة كثيفة 3×3، فوق خريطة سمات التفافية أحادية المقياس، لإجراء تصنيف ثنائي شيء/غير شيء وانحدار صندوق التحديد. يتحقق هذا من خلال طبقة التفاف 3×3 متبوعة بطبقتي التفاف شقيقتين 1×1 للتصنيف والانحدار، والتي نشير إليها برأس الشبكة. يتم تعريف معيار شيء/غير شيء وهدف انحدار صندوق التحديد بالنسبة إلى مجموعة من الصناديق المرجعية تسمى المراسي [29]. المراسي ذات مقاييس ونسب أبعاد متعددة محددة مسبقًا لتغطية أشياء ذات أشكال مختلفة.

نقوم بتكييف RPN عن طريق استبدال خريطة السمات أحادية المقياس بشبكة FPN الخاصة بنا. نرفق رأسًا بنفس التصميم (التفاف 3×3 وطبقتي التفاف شقيقتين 1×1) لكل مستوى على هرم السمات الخاص بنا. نظرًا لأن الرأس ينزلق بكثافة على جميع المواقع في جميع مستويات الهرم، فليس من الضروري وجود مراسٍ متعددة النطاقات على مستوى محدد. بدلاً من ذلك، نخصص مراسٍ بمقياس واحد لكل مستوى. بشكل رسمي، نحدد أن المراسي لها مساحات {32²، 64²، 128²، 256²، 512²} بكسل على {P2، P3، P4، P5، P6} على التوالي. كما في [29] نستخدم أيضًا مراسٍ ذات نسب أبعاد متعددة {1:2، 1:1، 2:1} على كل مستوى. لذا في المجموع هناك 15 مرساة على الهرم.

نخصص تسميات التدريب للمراسي بناءً على نسب التقاطع على الاتحاد (IoU) الخاصة بها مع صناديق التحديد الحقيقية كما في [29]. بشكل رسمي، يُخصص للمرساة تسمية إيجابية إذا كان لديها أعلى IoU لصندوق حقيقي معين أو IoU أكثر من 0.7 مع أي صندوق حقيقي، وتسمية سلبية إذا كان لديها IoU أقل من 0.3 لجميع الصناديق الحقيقية. لاحظ أن مقاييس الصناديق الحقيقية لا تُستخدم صراحةً لتخصيصها لمستويات الهرم؛ بدلاً من ذلك، ترتبط الصناديق الحقيقية بالمراسي، والتي تم تخصيصها لمستويات الهرم. على هذا النحو، لا نقدم أي قواعد إضافية بالإضافة إلى تلك الموجودة في [29].

نلاحظ أن معاملات الرؤوس مشتركة عبر جميع مستويات هرم السمات؛ لقد قيّمنا أيضًا البديل دون مشاركة المعاملات ولاحظنا دقة مماثلة. يشير الأداء الجيد لمشاركة المعاملات إلى أن جميع مستويات هرمنا تشترك في مستويات دلالية متشابهة. هذه الميزة مماثلة لتلك الخاصة باستخدام هرم صورة مُسمّت، حيث يمكن تطبيق مصنف رأس مشترك على السمات المحسوبة على أي مقياس صورة.

مع التكييفات المذكورة أعلاه، يمكن تدريب واختبار RPN بشكل طبيعي مع شبكة FPN الخاصة بنا، بنفس الطريقة كما في [29]. نوضح تفاصيل التنفيذ في التجارب.

**4.2. شبكات هرم السمات لـ Fast R-CNN**

Fast R-CNN [11] هو كاشف أشياء قائم على المناطق حيث يتم استخدام تجميع منطقة الاهتمام (RoI) لاستخراج السمات. يتم إجراء Fast R-CNN بشكل أكثر شيوعًا على خريطة سمات أحادية المقياس. لاستخدامه مع شبكة FPN الخاصة بنا، نحتاج إلى تخصيص مناطق RoI ذات مقاييس مختلفة لمستويات الهرم.

نعتبر هرم السمات الخاص بنا كما لو كان منتجًا من هرم صورة. وبالتالي يمكننا تكييف استراتيجية التخصيص للكاشفات القائمة على المناطق [15، 11] في الحالة التي يتم فيها تشغيلها على أهرام الصور. بشكل رسمي، نخصص RoI بعرض w وارتفاع h (على صورة الإدخال للشبكة) للمستوى Pk من هرم السمات الخاص بنا بواسطة:

$$k = \lfloor k_0 + \log_2(\sqrt{wh}/224) \rfloor. \tag{1}$$

هنا 224 هو حجم التدريب المسبق القياسي لـ ImageNet، و k₀ هو المستوى المستهدف الذي يجب تعيين RoI بـ w × h = 224² إليه. بالمماثلة لنظام Faster R-CNN القائم على ResNet [16] الذي يستخدم C4 كخريطة سمات أحادية المقياس، نضع k₀ على 4. بشكل بديهي، تعني المعادلة (1) أنه إذا أصبح مقياس RoI أصغر (لنقل، 1/2 من 224)، فيجب تعيينه إلى مستوى بدقة أدق (لنقل، k = 3).

نرفق رؤوس تنبؤ (في Fast R-CNN الرؤوس هي مصنفات خاصة بالفئة ومنحدرات صناديق التحديد) لجميع مناطق RoI على جميع المستويات. مرة أخرى، تشترك جميع الرؤوس في المعاملات، بغض النظر عن مستوياتها. في [16]، يتم اعتماد طبقات conv5 لشبكة ResNet (شبكة فرعية عميقة بـ 9 طبقات) كرأس فوق سمات conv4، لكن طريقتنا قد استغلت بالفعل conv5 لبناء هرم السمات. لذا على عكس [16]، نعتمد ببساطة تجميع RoI لاستخراج سمات 7×7، ونرفق طبقتين مخفيتين متصلتين بالكامل (fc) بحجم 1,024 بُعد (كل منهما متبوعة بـ ReLU) قبل طبقات التصنيف وانحدار صندوق التحديد النهائية. يتم تهيئة هذه الطبقات عشوائيًا، حيث لا توجد طبقات fc مُدربة مسبقًا متاحة في ResNets. لاحظ أنه بالمقارنة مع رأس conv5 القياسي، فإن رأس MLP ثنائي الطبقة المتصلة بالكامل أخف وزنًا وأسرع.

بناءً على هذه التكييفات، يمكننا تدريب واختبار Fast R-CNN فوق هرم السمات. تُعطى تفاصيل التنفيذ في القسم التجريبي.

---

### Translation Notes

- **Figures referenced:** None explicitly in this section
- **Key terms introduced:**
  - sliding-window: نافذة منزلقة
  - class-agnostic: مستقل عن الفئة
  - network head: رأس الشبكة
  - anchors: المراسي
  - aspect ratios: نسب الأبعاد
  - Intersection-over-Union (IoU): التقاطع على الاتحاد
  - ground-truth: الحقيقية
  - Region-of-Interest (RoI): منطقة الاهتمام
  - RoI pooling: تجميع منطقة الاهتمام
  - fully-connected layers: طبقات متصلة بالكامل
  - MLP (Multi-Layer Perceptron): شبكة إدراك متعددة الطبقات
- **Equations:** 1 equation for RoI assignment
- **Citations:** References to [11, 15, 16, 29]
- **Special handling:**
  - Mathematical notation kept as is: k₀, w × h, 224²
  - Technical terms like "RPN", "Fast R-CNN", "ResNet", "ReLU" kept in English
  - Anchor sizes {32², 64², 128², 256², 512²} kept in original notation
  - Aspect ratios {1:2, 1:1, 2:1} kept as is

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.84
- **Overall section score:** 0.87

### Back-Translation Check

Key phrases verified:
- "كاشف أشياء مستقل عن الفئة" → Class-agnostic object detector ✓
- "رأس الشبكة" → Network head ✓
- "المراسي" → Anchors ✓
- "التقاطع على الاتحاد" → Intersection-over-Union ✓
- "منطقة الاهتمام" → Region-of-Interest ✓
- "طبقات متصلة بالكامل" → Fully-connected layers ✓
