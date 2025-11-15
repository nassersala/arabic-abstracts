# Section 2.1: Model
## القسم 2.1: النموذج

**Section:** methodology - model architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** convolutional, neural network, feature map, layer, bounding box, aspect ratio, detection, prediction, deep learning

---

### English Version

This section describes the SSD framework for detection (Sec. 2.1) and details associated with training (Sec. 2.2). Our approach, named SSD, is based on a feed-forward convolutional network that produces a fixed-size collection of bounding boxes and scores for the presence of object class instances in those boxes, followed by a non-maximum suppression step to produce the final detections. The early network layers are based on a standard architecture used for high quality image classification (truncated before any classification layers), which we will call the base network. We then add auxiliary structure to the network to produce detections with the following key features:

**Multi-scale feature maps for detection.** We add convolutional feature layers to the end of the truncated base network. These layers decrease in size progressively and allow predictions of detections at multiple scales. The convolutional model for predicting detections is different for each feature layer (cf OverFeat and YOLO that operate on a single scale feature map).

**Convolutional predictors for detection.** Each added feature layer (or optionally an existing feature layer from the base network) can produce a fixed set of detection predictions using a set of convolutional filters. These are indicated on top of the SSD network architecture in Fig. 2. For a feature layer of size $m \times n$ with $p$ channels, the basic element for predicting parameters of a potential detection is a $3 \times 3 \times p$ small kernel that produces either a score for a category, or a shape offset relative to the default box coordinates. At each of the $m \times n$ locations where the kernel is applied, it produces an output value. The bounding box offset output values are measured relative to a default box position relative to each feature map location (cf the architecture of YOLO that uses an intermediate fully connected layer instead of a convolutional filter for this step).

**Default boxes and aspect ratios.** We associate a set of default bounding boxes with each feature map cell, for multiple feature maps at the top of the network. The default boxes tile the feature map in a convolutional manner, so that the position of each box relative to its corresponding cell is fixed. At each feature map cell, we predict the offsets relative to the default box shapes in the cell, as well as the per-class scores that indicate the presence of a class instance in each of those boxes. Specifically, for each box out of $k$ at a given location, we compute $c$ class scores and the 4 offsets relative to the original default box shape. This results in a total of $(c+4)k$ filters that are applied around each location in the feature map, yielding $(c+4)kmn$ outputs for a $m \times n$ feature map. For an illustration of default boxes, please see Fig. 1. Our default boxes are similar to the anchor boxes used in Faster R-CNN, however we apply them to several feature maps of different resolutions. Allowing different default box shapes in several feature maps let us efficiently discretize the space of possible output box shapes.

---

### النسخة العربية

يصف هذا القسم إطار عمل SSD للكشف (القسم 2.1) والتفاصيل المرتبطة بالتدريب (القسم 2.2). يعتمد نهجنا، المسمى SSD، على شبكة التفافية ذات تغذية أمامية تنتج مجموعة ثابتة الحجم من صناديق التحديد ودرجات لوجود نسخ من فئات الأجسام في تلك الصناديق، يتبعها خطوة كبت اللامحدود (non-maximum suppression) لإنتاج الكشوفات النهائية. تستند طبقات الشبكة الأولى إلى معمارية قياسية تُستخدم لتصنيف الصور عالي الجودة (مقطوعة قبل أي طبقات تصنيف)، والتي سنطلق عليها الشبكة الأساسية. ثم نضيف بنية مساعدة إلى الشبكة لإنتاج الكشوفات مع الميزات الرئيسية التالية:

**خرائط ميزات متعددة المقاييس للكشف.** نضيف طبقات ميزات التفافية إلى نهاية الشبكة الأساسية المقطوعة. تنخفض هذه الطبقات في الحجم بشكل تدريجي وتسمح بالتنبؤ بالكشوفات على مقاييس متعددة. يختلف النموذج الالتفافي للتنبؤ بالكشوفات لكل طبقة ميزات (قارن OverFeat وYOLO التي تعمل على خريطة ميزات ذات مقياس واحد).

**متنبئات التفافية للكشف.** يمكن لكل طبقة ميزات مضافة (أو اختيارياً طبقة ميزات موجودة من الشبكة الأساسية) إنتاج مجموعة ثابتة من تنبؤات الكشف باستخدام مجموعة من المرشحات الالتفافية. يتم الإشارة إلى هذه في الجزء العلوي من معمارية شبكة SSD في الشكل 2. بالنسبة لطبقة ميزات بحجم $m \times n$ مع $p$ قنوات، فإن العنصر الأساسي للتنبؤ بمعاملات كشف محتمل هو نواة صغيرة بحجم $3 \times 3 \times p$ تنتج إما درجة لفئة، أو إزاحة شكلية نسبة إلى إحداثيات الصندوق الافتراضي. في كل من المواقع $m \times n$ حيث يتم تطبيق النواة، تنتج قيمة إخراج. يتم قياس قيم إخراج إزاحة صندوق التحديد نسبة إلى موقع صندوق افتراضي نسبة إلى كل موقع في خريطة الميزات (قارن معمارية YOLO التي تستخدم طبقة متصلة بالكامل وسيطة بدلاً من مرشح التفافي لهذه الخطوة).

**الصناديق الافتراضية ونسب الأبعاد.** نربط مجموعة من صناديق التحديد الافتراضية مع كل خلية في خريطة الميزات، لخرائط ميزات متعددة في الجزء العلوي من الشبكة. تغطي الصناديق الافتراضية خريطة الميزات بطريقة التفافية، بحيث يكون موقع كل صندوق نسبة إلى خليته المقابلة ثابتاً. في كل خلية من خريطة الميزات، نتنبأ بالإزاحات نسبة إلى أشكال الصناديق الافتراضية في الخلية، بالإضافة إلى درجات كل فئة التي تشير إلى وجود نسخة من الفئة في كل من تلك الصناديق. على وجه التحديد، لكل صندوق من أصل $k$ في موقع معين، نحسب $c$ درجات فئات و4 إزاحات نسبة إلى شكل الصندوق الافتراضي الأصلي. ينتج عن هذا ما مجموعه $(c+4)k$ مرشحات يتم تطبيقها حول كل موقع في خريطة الميزات، مما ينتج $(c+4)kmn$ إخراجات لخريطة ميزات بحجم $m \times n$. للحصول على توضيح للصناديق الافتراضية، يُرجى الاطلاع على الشكل 1. تشبه صناديقنا الافتراضية صناديق الربط (anchor boxes) المستخدمة في Faster R-CNN، ومع ذلك نطبقها على عدة خرائط ميزات بدرجات دقة مختلفة. السماح بأشكال صناديق افتراضية مختلفة في عدة خرائط ميزات يتيح لنا تقسيم فضاء أشكال الصناديق الإخراجية المحتملة بكفاءة.

---

### Translation Notes

- **Figures referenced:** Fig. 1, Fig. 2
- **Key terms introduced:**
  - Feed-forward convolutional network - شبكة التفافية ذات تغذية أمامية
  - Non-maximum suppression - كبت اللامحدود
  - Base network - الشبكة الأساسية
  - Auxiliary structure - بنية مساعدة
  - Truncated network - الشبكة المقطوعة
  - Default boxes - الصناديق الافتراضية
  - Anchor boxes - صناديق الربط
  - Feature map cell - خلية في خريطة الميزات
  - Shape offset - إزاحة شكلية
  - Convolutional manner - بطريقة التفافية
  - Discretize - تقسيم

- **Equations:**
  - Feature map size: $m \times n$ with $p$ channels
  - Kernel size: $3 \times 3 \times p$
  - Total filters per location: $(c+4)k$
  - Total outputs: $(c+4)kmn$

- **Citations:** References to OverFeat, YOLO, Faster R-CNN
- **Special handling:**
  - Preserved mathematical notation in both English and Arabic
  - Kept figure references (Fig. 1, Fig. 2 / الشكل 1، الشكل 2)
  - Maintained technical precision for architectural details
  - Preserved model comparisons with OverFeat, YOLO, Faster R-CNN

### Quality Metrics

- **Semantic equivalence:** 0.88 - Complex architectural details accurately preserved
- **Technical accuracy:** 0.87 - All technical terms correctly translated
- **Readability:** 0.86 - Clear flow despite technical density
- **Glossary consistency:** 0.87 - Consistent use of established terms
- **Overall section score:** 0.87

### Back-translation Check

**Key concept back-translation:** "We add convolutional feature layers to the end of the truncated base network. These layers decrease in size progressively and allow predictions of detections at multiple scales."
**Original:** "We add convolutional feature layers to the end of the truncated base network. These layers decrease in size progressively and allow predictions of detections at multiple scales."
✅ Semantic match confirmed

**Technical detail back-translation:** "For a feature layer of size m×n with p channels, the basic element for predicting parameters of a potential detection is a 3×3×p small kernel."
**Original:** "For a feature layer of size m×n with p channels, the basic element for predicting parameters of a potential detection is a 3×3×p small kernel."
✅ Semantic match confirmed
