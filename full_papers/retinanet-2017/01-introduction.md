# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.90
**Glossary Terms Used:** object detection, convolutional neural network, accuracy, inference, training, class imbalance, cross entropy, loss function, feature pyramid, ResNet

---

### English Version

Current state-of-the-art object detectors are based on a two-stage, proposal-driven mechanism. As popularized in the R-CNN framework [11], the first stage generates a sparse set of candidate object locations and the second stage classifies each candidate location as one of the foreground classes or as background using a convolutional neural network. Through a sequence of advances [10, 28, 20, 14], this two-stage framework consistently achieves top accuracy on the challenging COCO benchmark [21].

Despite the success of two-stage detectors, a natural question is: could a simple one-stage detector achieve similar accuracy? One stage detectors are applied over a regular, dense sampling of object locations, scales, and aspect ratios. Recent work on one-stage detectors, such as YOLO [26, 27] and SSD [22], demonstrates promising results, yielding faster detectors with accuracy within 10-40% of state-of-the-art two-stage methods.

This paper pushes the envelope further: we present a one-stage object detector that, for the first time, matches the state-of-the-art COCO AP of more complex two-stage detectors, such as the Feature Pyramid Network (FPN) [20] or Mask R-CNN [14] variants of Faster R-CNN [28]. To achieve this result, we identify class imbalance during training as the main obstacle impeding one-stage detector from achieving state-of-the-art accuracy and propose a new loss function that eliminates this barrier.

Class imbalance is addressed in R-CNN-like detectors by a two-stage cascade and sampling heuristics. The proposal stage (e.g., Selective Search [35], EdgeBoxes [39], DeepMask [24, 25], RPN [28]) rapidly narrows down the number of candidate object locations to a small number (e.g., 1-2k), filtering out most background samples. In the second classification stage, sampling heuristics, such as a fixed foreground-to-background ratio (1:3), or online hard example mining (OHEM) [31], are performed to maintain a manageable balance between foreground and background.

In contrast, a one-stage detector must process a much larger set of candidate object locations regularly sampled across an image. In practice this often amounts to enumerating ~100k locations that densely cover spatial positions, scales, and aspect ratios. While similar sampling heuristics may also be applied, they are inefficient as the training procedure is still dominated by easily classified background examples. This inefficiency is a classic problem in object detection that is typically addressed via techniques such as bootstrapping [33, 29] or hard example mining [37, 8, 31].

In this paper, we propose a new loss function that acts as a more effective alternative to previous approaches for dealing with class imbalance. The loss function is a dynamically scaled cross entropy loss, where the scaling factor decays to zero as confidence in the correct class increases, see Figure 1. Intuitively, this scaling factor can automatically down-weight the contribution of easy examples during training and rapidly focus the model on hard examples. Experiments show that our proposed Focal Loss enables us to train a high-accuracy, one-stage detector that significantly outperforms the alternatives of training with the sampling heuristics or hard example mining, the previous state-of-the-art techniques for training one-stage detectors. Finally, we note that the exact form of the focal loss is not critical, and we show other instantiations can achieve similar results.

To demonstrate the effectiveness of the proposed focal loss, we design a simple one-stage object detector called RetinaNet, named for its dense sampling of object locations in an input image. Its design features an efficient in-network feature pyramid and use of anchor boxes. It draws on a variety of recent ideas from [20, 22, 28, 17]. RetinaNet is efficient and accurate; our best model, based on a ResNet-101-FPN backbone, achieves a COCO test-dev AP of 39.1 while running at 5 fps, surpassing the previously best published single-model results from both one and two-stage detectors, see Figure 2.

---

### النسخة العربية

تعتمد كواشف الأجسام الحديثة المتقدمة على آلية من مرحلتين مدفوعة بالمقترحات. كما شاع استخدامه في إطار عمل R-CNN [11]، تولد المرحلة الأولى مجموعة متناثرة من مواقع الأجسام المرشحة وتُصنف المرحلة الثانية كل موقع مرشح كإحدى فئات المقدمة أو كخلفية باستخدام شبكة عصبية التفافية. من خلال سلسلة من التطورات [10، 28، 20، 14]، يحقق إطار العمل ثنائي المرحلة هذا باستمرار أعلى دقة على معيار COCO الصعب [21].

على الرغم من نجاح الكواشف ثنائية المرحلة، يطرح سؤال طبيعي: هل يمكن لكاشف بسيط أحادي المرحلة تحقيق دقة مماثلة؟ تُطبق الكواشف أحادية المرحلة على عينات منتظمة وكثيفة من مواقع الأجسام ومقاييسها ونسب أبعادها. يُظهر العمل الحديث على الكواشف أحادية المرحلة، مثل YOLO [26، 27] وSSD [22]، نتائج واعدة، منتجاً كواشف أسرع بدقة تقع ضمن 10-40% من طرق ثنائية المرحلة الحديثة المتقدمة.

يدفع هذا البحث الحدود أبعد من ذلك: نقدم كاشف أجسام أحادي المرحلة، للمرة الأولى، يطابق أداء COCO AP الحديث المتقدم للكواشف ثنائية المرحلة الأكثر تعقيداً، مثل شبكة الهرم الميزاتي (FPN) [20] أو متغيرات Mask R-CNN [14] من Faster R-CNN [28]. لتحقيق هذه النتيجة، نحدد عدم التوازن بين الفئات أثناء التدريب كالعائق الرئيسي الذي يمنع الكاشف أحادي المرحلة من تحقيق الدقة الحديثة المتقدمة ونقترح دالة خسارة جديدة تزيل هذا الحاجز.

يُعالج عدم التوازن بين الفئات في الكواشف الشبيهة بـ R-CNN من خلال تسلسل من مرحلتين واستدلالات أخذ العينات. تُقلص مرحلة المقترحات (مثل، Selective Search [35]، EdgeBoxes [39]، DeepMask [24، 25]، RPN [28]) بسرعة عدد مواقع الأجسام المرشحة إلى عدد صغير (مثل، 1-2 ألف)، مما يُرشح معظم عينات الخلفية. في مرحلة التصنيف الثانية، تُنفذ استدلالات أخذ العينات، مثل نسبة ثابتة بين المقدمة والخلفية (1:3)، أو التنقيب عن الأمثلة الصعبة عبر الإنترنت (OHEM) [31]، للحفاظ على توازن قابل للإدارة بين المقدمة والخلفية.

في المقابل، يجب على الكاشف أحادي المرحلة معالجة مجموعة أكبر بكثير من مواقع الأجسام المرشحة التي تُؤخذ عيناتها بانتظام عبر الصورة. في الممارسة العملية، يصل هذا غالباً إلى تعداد حوالي 100 ألف موقع تغطي بكثافة المواقع المكانية والمقاييس ونسب الأبعاد. بينما يمكن أيضاً تطبيق استدلالات أخذ العينات المماثلة، فإنها غير فعالة لأن إجراء التدريب لا يزال مُهيمناً عليه بواسطة أمثلة الخلفية المصنفة بسهولة. هذه عدم الكفاءة مشكلة كلاسيكية في كشف الأجسام تُعالج عادة عبر تقنيات مثل التمهيد الذاتي [33، 29] أو التنقيب عن الأمثلة الصعبة [37، 8، 31].

في هذا البحث، نقترح دالة خسارة جديدة تعمل كبديل أكثر فعالية للنهج السابقة للتعامل مع عدم التوازن بين الفئات. دالة الخسارة هي دالة إنتروبيا متقاطعة مُعدلة ديناميكياً، حيث يتلاشى عامل التحجيم إلى الصفر مع زيادة الثقة في الفئة الصحيحة، انظر الشكل 1. بشكل حدسي، يمكن لعامل التحجيم هذا أن يُقلل تلقائياً من مساهمة الأمثلة السهلة أثناء التدريب ويُركز بسرعة النموذج على الأمثلة الصعبة. تُظهر التجارب أن الخسارة المُركزة المقترحة تُمكننا من تدريب كاشف أحادي المرحلة عالي الدقة يتفوق بشكل كبير على بدائل التدريب باستخدام استدلالات أخذ العينات أو التنقيب عن الأمثلة الصعبة، وهي التقنيات الحديثة المتقدمة السابقة لتدريب الكواشف أحادية المرحلة. أخيراً، نلاحظ أن الشكل الدقيق للخسارة المُركزة ليس حاسماً، ونُظهر أن تجسيدات أخرى يمكنها تحقيق نتائج مماثلة.

لإثبات فعالية الخسارة المُركزة المقترحة، نصمم كاشف أجسام بسيط أحادي المرحلة يُسمى RetinaNet، سُمي هكذا لأخذ العينات الكثيف لمواقع الأجسام في صورة الإدخال. يتميز تصميمه بهرم ميزات فعال داخل الشبكة واستخدام صناديق المرساة. يستند إلى مجموعة متنوعة من الأفكار الحديثة من [20، 22، 28، 17]. RetinaNet فعال ودقيق؛ نموذجنا الأفضل، المبني على عمود فقري ResNet-101-FPN، يحقق أداء COCO test-dev AP بمقدار 39.1 بينما يعمل بسرعة 5 إطارات في الثانية، متجاوزاً أفضل النتائج المنشورة سابقاً لنموذج واحد من كل من الكواشف أحادية وثنائية المرحلة، انظر الشكل 2.

---

### Translation Notes

- **Figures referenced:** Figure 1 (focal loss visualization), Figure 2 (speed/accuracy comparison)
- **Key terms introduced:**
  - Proposal-driven (مدفوعة بالمقترحات)
  - Foreground/background (المقدمة/الخلفية)
  - Sampling heuristics (استدلالات أخذ العينات)
  - Hard example mining (التنقيب عن الأمثلة الصعبة)
  - Feature Pyramid Network (شبكة الهرم الميزاتي)
  - Anchor boxes (صناديق المرساة)
  - Backbone (عمود فقري)

- **Equations:** None in this section
- **Citations:** Multiple papers referenced [11], [10, 28, 20, 14], [21], [26, 27], [22], [35, 39, 24, 25, 28], [31], [33, 29, 37, 8], [20, 22, 28, 17]
- **Special handling:**
  - Model names preserved in English: R-CNN, YOLO, SSD, FPN, Mask R-CNN, Faster R-CNN, ResNet
  - COCO benchmark name preserved
  - "AP" (Average Precision) kept as-is
  - Technical abbreviations: OHEM, RPN preserved

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.89
- Glossary consistency: 0.88
- **Overall section score: 0.90**

### Back-translation Check

Key technical phrases verified:
- "مدفوعة بالمقترحات" → "proposal-driven" ✓
- "استدلالات أخذ العينات" → "sampling heuristics" ✓
- "التنقيب عن الأمثلة الصعبة" → "hard example mining" ✓
- "هرم ميزات" → "feature pyramid" ✓
- "صناديق المرساة" → "anchor boxes" ✓
