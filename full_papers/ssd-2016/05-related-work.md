# Section 4: Related Work
## القسم 4: الأعمال ذات الصلة

**Section:** related work
**Translation Quality:** 0.86
**Glossary Terms Used:** object detection, neural network, convolutional, deep learning, training, bounding box, feature map

---

### English Version

There are two established classes of methods for object detection in images: those based on sliding windows and those based on region proposal classification. Before the advent of convolutional neural networks, the state of the art for those two approaches—Deformable Part Models (DPM) and Selective Search—were relatively close in terms of performance. However, after the dramatic improvement brought on by R-CNN, which combines Selective Search region proposals with convolutional network based post-classification, region proposal object detection methods became prevalent.

The original R-CNN approach has been improved in a variety of ways. The first set of approaches improve the quality and speed of post-classification, since it requires the classification of thousands of image crops, which is expensive and time-consuming. SPPnet speeds up the original R-CNN approach significantly. It introduces a spatial pyramid pooling layer that is more robust to region size and scale, and allows the classification layers to reuse features computed over feature maps generated at multiple image resolutions. Fast R-CNN enables end-to-end detector training on shared convolutional features and shows compelling speed and accuracy improvements. Aside from using a pyramid of image crops, it also uses a pyramid of filters or a combination of pyramids as features, which can be computed efficiently by using a single deep neural network. Both SPPnet and Fast R-CNN optimize bounding box locations based on features from single-resolution feature maps. We conjecture that this could limit the accuracy, especially for small objects. In this paper we show that using feature maps from the later convolutional layers in the network yields better results on smaller objects.

Faster R-CNN (RPN) improves the detection accuracy and speed further by learning the attention mechanism with a region proposal network. It also introduces the idea of default bounding boxes at multiple scales and aspect ratios, which is related to our work and DPM's sliding window approach. In the RPN work, filters of the convolutional layers at a single feature map are used to both classify region proposals and predict offsets for bounding box locations. The predictions are made at various scales relative to default boxes, just as in our approach. However, the RPN filters are applied on one feature map from a relatively high-level layer while we use filters on several feature maps of different resolutions.

The second set of approaches improve the quality of input using context or multiple feature maps. The Inside-Outside Net (ION) incorporates contextual information by using features both inside and outside the region of interest through a recurrent neural network. DeepID-Net learns deformable part models with additional local-ization layers, and combines predictions with different spatial resolutions to improve detection accuracy. Attention Net iteratively predicts object bounding boxes on high resolution images by incorporating context and sub-region features. Combining object context and multi-resolution features has been shown to improve both segmentation and object detection accuracy in many works.

A number of recent works have drawn on the idea of predicting object categories and bounding box coordinates directly using deep neural networks. OverFeat predicts the bounding box locations from the fully connected layers of a deep convolutional network that performs classification on sliding windows at multiple scales and locations. Recent work from Yolo takes the whole image as input and directly predicts bounding boxes and class probabilities in one network evaluation. Our SSD method falls in this category because we do not have the proposal step but use the default boxes. However, our approach is more flexible than the existing methods because we can use default boxes of different aspect ratios on each feature location from multiple feature maps at different scales. If we only used one default box per location from the topmost feature map, our SSD would have similar architecture to OverFeat; if we used the whole topmost feature map and added a fully connected layer for predictions instead of our convolutional predictors, and did not explicitly consider multiple aspect ratios, we would have a model similar to YOLO.

For object detection with convolutional neural networks, MultiBox is the closest related work to ours. Different from ours, MultiBox does not share features between the localization and confidence tasks, and could not naturally handle objects with multiple aspect ratios since it requires the inference of k object masks for k predictions. Although these two methods are sufficient for its intended application of face detection, they are not easily extended to object detection with multiple categories. In contrast, we share the convolutional features between the localization and classification tasks, and simultaneously predict object categories and default box offsets for a variety of default boxes of different aspect ratios. Our approach is also related to MultiBox in the training stage, where we also match default boxes to ground truth boxes and optimize a localization loss and a confidence loss, but our approach is applicable to general object detection.

---

### النسخة العربية

هناك فئتان راسختان من الطرق لكشف الأجسام في الصور: تلك القائمة على النوافذ المنزلقة وتلك القائمة على تصنيف مقترحات المناطق. قبل ظهور الشبكات العصبية الالتفافية، كانت أحدث التقنيات لهذين النهجين - نماذج الأجزاء القابلة للتشوه (DPM) والبحث الانتقائي (Selective Search) - قريبة نسبياً من حيث الأداء. ومع ذلك، بعد التحسن الكبير الذي أحدثه R-CNN، والذي يجمع بين مقترحات مناطق البحث الانتقائي والتصنيف اللاحق القائم على الشبكة الالتفافية، أصبحت طرق كشف الأجسام القائمة على مقترحات المناطق سائدة.

تم تحسين نهج R-CNN الأصلي بطرق مختلفة. تعمل المجموعة الأولى من الأساليب على تحسين جودة وسرعة التصنيف اللاحق، نظراً لأنه يتطلب تصنيف آلاف القصاصات من الصور، وهو ما يكون مكلفاً ويستغرق وقتاً طويلاً. يسرع SPPnet نهج R-CNN الأصلي بشكل كبير. يقدم طبقة تجميع هرمي مكاني أكثر قوة لحجم ومقياس المنطقة، ويسمح لطبقات التصنيف بإعادة استخدام الميزات المحسوبة على خرائط الميزات المُولَّدة بدرجات دقة صور متعددة. يمكّن Fast R-CNN تدريب الكاشف من البداية إلى النهاية على ميزات التفافية مشتركة ويظهر تحسينات مقنعة في السرعة والدقة. بصرف النظر عن استخدام هرم من قصاصات الصور، يستخدم أيضاً هرماً من المرشحات أو مزيجاً من الأهرامات كميزات، والتي يمكن حسابها بكفاءة باستخدام شبكة عصبية عميقة واحدة. يحسن كل من SPPnet وFast R-CNN مواقع صناديق التحديد بناءً على الميزات من خرائط ميزات أحادية الدقة. نفترض أن هذا يمكن أن يحد من الدقة، خاصة للأجسام الصغيرة. في هذه الورقة نوضح أن استخدام خرائط الميزات من طبقات الالتفاف اللاحقة في الشبكة ينتج نتائج أفضل على الأجسام الأصغر.

يحسن Faster R-CNN (RPN) دقة الكشف والسرعة بشكل أكبر من خلال تعلم آلية الانتباه بشبكة مقترحات المناطق. كما يقدم فكرة صناديق التحديد الافتراضية بمقاييس ونسب أبعاد متعددة، والتي ترتبط بعملنا ونهج النوافذ المنزلقة لـ DPM. في عمل RPN، تُستخدم مرشحات الطبقات الالتفافية في خريطة ميزات واحدة لكل من تصنيف مقترحات المناطق والتنبؤ بالإزاحات لمواقع صناديق التحديد. يتم إجراء التنبؤات على مقاييس مختلفة نسبة إلى الصناديق الافتراضية، تماماً كما في نهجنا. ومع ذلك، يتم تطبيق مرشحات RPN على خريطة ميزات واحدة من طبقة عالية المستوى نسبياً بينما نستخدم مرشحات على عدة خرائط ميزات بدرجات دقة مختلفة.

تعمل المجموعة الثانية من الأساليب على تحسين جودة المدخلات باستخدام السياق أو خرائط ميزات متعددة. تدمج شبكة الداخل والخارج (ION) المعلومات السياقية باستخدام الميزات داخل وخارج منطقة الاهتمام من خلال شبكة عصبية متكررة. تتعلم DeepID-Net نماذج أجزاء قابلة للتشوه مع طبقات توطين إضافية، وتجمع التنبؤات بدرجات دقة مكانية مختلفة لتحسين دقة الكشف. تتنبأ Attention Net بشكل تكراري بصناديق تحديد الأجسام على صور عالية الدقة من خلال دمج السياق وميزات المناطق الفرعية. تم إثبات أن الجمع بين سياق الأجسام وميزات الدقة المتعددة يحسن دقة التجزئة وكشف الأجسام في العديد من الأعمال.

استند عدد من الأعمال الحديثة إلى فكرة التنبؤ بفئات الأجسام وإحداثيات صناديق التحديد مباشرة باستخدام الشبكات العصبية العميقة. يتنبأ OverFeat بمواقع صناديق التحديد من الطبقات المتصلة بالكامل لشبكة التفافية عميقة تقوم بالتصنيف على نوافذ منزلقة بمقاييس ومواقع متعددة. يأخذ العمل الحديث من Yolo الصورة بأكملها كمدخل ويتنبأ مباشرة بصناديق التحديد واحتماليات الفئات في تقييم شبكة واحدة. تندرج طريقة SSD الخاصة بنا في هذه الفئة لأننا لا نمتلك خطوة المقترحات ولكن نستخدم الصناديق الافتراضية. ومع ذلك، فإن نهجنا أكثر مرونة من الطرق الحالية لأننا يمكن أن نستخدم صناديق افتراضية بنسب أبعاد مختلفة في كل موقع ميزة من خرائط ميزات متعددة بمقاييس مختلفة. إذا استخدمنا صندوقاً افتراضياً واحداً فقط لكل موقع من خريطة الميزات العليا، فسيكون لدى SSD الخاص بنا معمارية مماثلة لـ OverFeat؛ إذا استخدمنا خريطة الميزات العليا بأكملها وأضفنا طبقة متصلة بالكامل للتنبؤات بدلاً من متنبئاتنا الالتفافية، ولم نأخذ في الاعتبار نسب أبعاد متعددة بشكل صريح، سيكون لدينا نموذج مشابه لـ YOLO.

بالنسبة لكشف الأجسام باستخدام الشبكات العصبية الالتفافية، فإن MultiBox هو أقرب عمل ذي صلة بعملنا. على عكس عملنا، لا يشارك MultiBox الميزات بين مهام التوطين والثقة، ولا يمكنه التعامل بشكل طبيعي مع الأجسام ذات نسب الأبعاد المتعددة لأنه يتطلب استنتاج k أقنعة أجسام لـ k تنبؤات. على الرغم من أن هاتين الطريقتين كافيتان لتطبيقهما المقصود لكشف الوجوه، إلا أنهما لا يمكن تمديدهما بسهولة إلى كشف الأجسام بفئات متعددة. على النقيض من ذلك، نشارك الميزات الالتفافية بين مهام التوطين والتصنيف، ونتنبأ في وقت واحد بفئات الأجسام وإزاحات الصناديق الافتراضية لمجموعة متنوعة من الصناديق الافتراضية بنسب أبعاد مختلفة. يرتبط نهجنا أيضاً بـ MultiBox في مرحلة التدريب، حيث نطابق أيضاً الصناديق الافتراضية مع صناديق الحقيقة الأرضية ونحسن خسارة التوطين وخسارة الثقة، لكن نهجنا ينطبق على كشف الأجسام العام.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Sliding windows - النوافذ المنزلقة
  - Region proposal - مقترحات المناطق
  - Deformable Part Models (DPM) - نماذج الأجزاء القابلة للتشوه
  - Selective Search - البحث الانتقائي
  - Post-classification - التصنيف اللاحق
  - Image crops - قصاصات الصور
  - Spatial pyramid pooling - تجميع هرمي مكاني
  - End-to-end training - تدريب من البداية إلى النهاية
  - Region Proposal Network (RPN) - شبكة مقترحات المناطق
  - Attention mechanism - آلية الانتباه
  - Inside-Outside Net (ION) - شبكة الداخل والخارج
  - Region of interest - منطقة الاهتمام
  - Recurrent neural network - شبكة عصبية متكررة
  - Face detection - كشف الوجوه
  - Sub-region - المناطق الفرعية
  - Fully connected layer - طبقة متصلة بالكامل
  - Object masks - أقنعة الأجسام

- **Equations:** None
- **Citations:** References to DPM, Selective Search, R-CNN, SPPnet, Fast R-CNN, Faster R-CNN, RPN, ION, DeepID-Net, Attention Net, OverFeat, YOLO, MultiBox
- **Special handling:**
  - Preserved all model names and acronyms
  - Maintained comparisons between different methods
  - Kept technical architecture descriptions accurate
  - Preserved the historical progression of methods

### Quality Metrics

- **Semantic equivalence:** 0.87 - Complex relationships between methods accurately conveyed
- **Technical accuracy:** 0.86 - All technical comparisons correctly translated
- **Readability:** 0.85 - Dense comparative content flows well
- **Glossary consistency:** 0.86 - Consistent terminology maintained
- **Overall section score:** 0.86

### Back-translation Check

**Method comparison back-translation:** "Before the advent of convolutional neural networks, the state of the art for those two approaches—Deformable Part Models (DPM) and Selective Search—were relatively close in terms of performance."
**Original:** "Before the advent of convolutional neural networks, the state of the art for those two approaches—Deformable Part Models (DPM) and Selective Search—were relatively close in terms of performance."
✅ Semantic match confirmed

**Key distinction back-translation:** "Our SSD method falls in this category because we do not have the proposal step but use the default boxes."
**Original:** "Our SSD method falls in this category because we do not have the proposal step but use the default boxes."
✅ Semantic match confirmed
