# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.89
**Glossary Terms Used:** object detection, deep learning, convolutional neural network, region proposal, class imbalance, loss function, training, robustness

---

### English Version

**Classic Object Detectors:** The sliding-window paradigm, in which a classifier is applied on a dense image grid, has a long and rich history. One of the earliest successes is the classic work of LeCun et al. who applied convolutional neural networks to handwritten digit recognition [19, 36]. Viola and Jones [34] used boosted object detectors for face detection, leading to widespread adoption of such models. The introduction of HOG [4] and integral channel features [5] gave rise to effective methods for pedestrian detection. DPMs [9] helped extend dense detectors to more general object categories and had top results on PASCAL [7] for many years. While the sliding-window approach was the leading detection paradigm in classic computer vision, with the resurgence of deep learning [18], two-stage detectors, described next, quickly came to dominate object detection.

**Two-stage Detectors:** The dominant paradigm in modern object detection is based on a two-stage approach. As pioneered in Selective Search [35] and in the Regions with CNN features (R-CNN) [11] method, the first stage generates a sparse set of candidate proposals that should contain all objects while filtering out the majority of negative locations, and the second stage classifies the proposals into foreground classes or background. R-CNN was improved over the years: Fast R-CNN [10] improved accuracy and speed by learning to classify proposal boxes using a single network and introduced the ROI pooling layer; Faster R-CNN [28] introduced a learned Region Proposal Network (RPN) to generate proposals directly in the network, avoiding the need for an external region proposal algorithm like Selective Search; the latest incarnations, such as Feature Pyramid Networks (FPN) [20] and Mask R-CNN [14], extend Faster R-CNN in various ways and achieve state-of-the-art results. Two-stage detectors have dominated all recent object detection benchmarks.

**One-stage Detectors:** OverFeat [30] was one of the first modern one-stage object detector based on deep networks. More recently SSD [22] and YOLO [26, 27] have renewed interest in one-stage methods which have become very popular due to their high speed, although their accuracy is typically 10-40% lower than two-stage methods on the challenging COCO benchmark. Recent work showed that two-stage detectors can be made as fast as one-stage detectors while maintaining higher accuracy [17], however in practice one-stage detectors are still attractive due to their simplicity.

**Class Imbalance:** Both classic one-stage object detection methods, like boosted detectors [34, 5] and DPMs [9], and more recent methods, like SSD [22], face a large class imbalance during training. These detectors evaluate 10^4-10^5 candidate locations per image but only a few locations contain objects. This imbalance causes two problems: (1) training is inefficient as most locations are easy negatives that contribute no useful learning signal; (2) en masse, the easy negatives can overwhelm training and lead to degenerate models. A common solution is to perform some form of hard negative mining [33, 37, 8, 22, 31] that samples hard examples during training or more complex sampling/reweighing schemes [2]. In contrast, we show that our proposed focal loss naturally handles the class imbalance faced by a one-stage detector and allows us to efficiently train on all examples without sampling and without easy negatives overwhelming the loss and computed gradients.

**Robust Estimation:** There has been much interest in designing robust loss functions (e.g., Huber loss [16]) that reduce the contribution of outliers by down-weighting the loss of examples with large errors (hard examples). In contrast, rather than addressing outliers, our focal loss is designed to address class imbalance by down-weighting inliers (easy examples) such that their contribution to the total loss is small even if their number is large. In other words, the focal loss performs the opposite role of a robust loss: it focuses training on a sparse set of hard examples.

---

### النسخة العربية

**كواشف الأجسام الكلاسيكية:** نموذج النافذة المنزلقة، حيث يُطبق مصنف على شبكة صورة كثيفة، له تاريخ طويل وغني. أحد أوائل النجاحات هو العمل الكلاسيكي لـ LeCun وآخرون الذين طبقوا الشبكات العصبية الالتفافية على التعرف على الأرقام المكتوبة بخط اليد [19، 36]. استخدم Viola و Jones [34] كواشف أجسام معززة لكشف الوجوه، مما أدى إلى اعتماد واسع النطاق لمثل هذه النماذج. أدى إدخال HOG [4] وميزات القنوات التكاملية [5] إلى ظهور طرق فعالة لكشف المشاة. ساعدت نماذج DPM [9] في توسيع الكواشف الكثيفة لفئات أجسام أكثر عمومية وحققت أفضل النتائج على معيار PASCAL [7] لسنوات عديدة. بينما كان نهج النافذة المنزلقة النموذج الرائد للكشف في الرؤية الحاسوبية الكلاسيكية، مع انبعاث التعلم العميق [18]، سرعان ما أصبحت الكواشف ثنائية المرحلة، الموصوفة تالياً، مهيمنة على كشف الأجسام.

**الكواشف ثنائية المرحلة:** النموذج المهيمن في كشف الأجسام الحديث يعتمد على نهج من مرحلتين. كما رائد في Selective Search [35] وفي طريقة المناطق مع ميزات CNN (R-CNN) [11]، تولد المرحلة الأولى مجموعة متناثرة من المقترحات المرشحة التي يجب أن تحتوي على جميع الأجسام بينما ترشح غالبية المواقع السلبية، والمرحلة الثانية تصنف المقترحات إلى فئات مقدمة أو خلفية. تحسن R-CNN على مر السنين: حسّن Fast R-CNN [10] الدقة والسرعة من خلال التعلم لتصنيف صناديق المقترحات باستخدام شبكة واحدة وقدم طبقة تجميع ROI؛ قدم Faster R-CNN [28] شبكة مقترحات مناطق مُتعلمة (RPN) لتوليد المقترحات مباشرة في الشبكة، متجنباً الحاجة لخوارزمية مقترحات مناطق خارجية مثل Selective Search؛ التجسيدات الأحدث، مثل شبكات الهرم الميزاتي (FPN) [20] و Mask R-CNN [14]، توسع Faster R-CNN بطرق متنوعة وتحقق نتائج حديثة متقدمة. هيمنت الكواشف ثنائية المرحلة على جميع معايير كشف الأجسام الحديثة.

**الكواشف أحادية المرحلة:** كان OverFeat [30] أحد أوائل كواشف الأجسام الحديثة أحادية المرحلة المبنية على الشبكات العميقة. في الآونة الأخيرة، جدد SSD [22] و YOLO [26، 27] الاهتمام بالطرق أحادية المرحلة التي أصبحت شائعة جداً بسبب سرعتها العالية، على الرغم من أن دقتها عادة أقل بنسبة 10-40% من الطرق ثنائية المرحلة على معيار COCO الصعب. أظهر العمل الحديث أنه يمكن جعل الكواشف ثنائية المرحلة سريعة مثل الكواشف أحادية المرحلة مع الحفاظ على دقة أعلى [17]، ومع ذلك في الممارسة العملية لا تزال الكواشف أحادية المرحلة جذابة بسبب بساطتها.

**عدم التوازن بين الفئات:** تواجه كل من طرق كشف الأجسام الكلاسيكية أحادية المرحلة، مثل الكواشف المعززة [34، 5] ونماذج DPM [9]، والطرق الأحدث، مثل SSD [22]، عدم توازن كبير بين الفئات أثناء التدريب. تُقيّم هذه الكواشف 10^4 إلى 10^5 موقع مرشح لكل صورة لكن عدداً قليلاً فقط من المواقع يحتوي على أجسام. يسبب هذا عدم التوازن مشكلتين: (1) التدريب غير فعال حيث معظم المواقع هي أمثلة سلبية سهلة لا تساهم بأي إشارة تعليمية مفيدة؛ (2) بشكل جماعي، يمكن للأمثلة السلبية السهلة إغراق التدريب والإدى إلى نماذج منحلة. الحل الشائع هو إجراء شكل من التنقيب عن الأمثلة السلبية الصعبة [33، 37، 8، 22، 31] الذي يأخذ عينات من الأمثلة الصعبة أثناء التدريب أو مخططات أخذ عينات/إعادة وزن أكثر تعقيداً [2]. في المقابل، نُظهر أن الخسارة المُركزة المقترحة تتعامل بشكل طبيعي مع عدم التوازن بين الفئات الذي يواجهه الكاشف أحادي المرحلة وتسمح لنا بالتدريب بكفاءة على جميع الأمثلة دون أخذ عينات ودون أن تغرق الأمثلة السلبية السهلة الخسارة والتدرجات المحسوبة.

**التقدير الصلب:** كان هناك اهتمام كبير في تصميم دوال خسارة صلبة (مثل، خسارة Huber [16]) التي تُقلل من مساهمة القيم الشاذة عن طريق تقليل وزن خسارة الأمثلة ذات الأخطاء الكبيرة (الأمثلة الصعبة). في المقابل، بدلاً من معالجة القيم الشاذة، صُممت الخسارة المُركزة لدينا لمعالجة عدم التوازن بين الفئات من خلال تقليل وزن القيم الداخلية (الأمثلة السهلة) بحيث تكون مساهمتها في إجمالي الخسارة صغيرة حتى لو كان عددها كبيراً. بمعنى آخر، تؤدي الخسارة المُركزة الدور المعاكس لخسارة صلبة: إنها تُركز التدريب على مجموعة متناثرة من الأمثلة الصعبة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Sliding-window paradigm (نموذج النافذة المنزلقة)
  - Region proposal (مقترحات مناطق)
  - ROI pooling (تجميع ROI)
  - Hard negative mining (التنقيب عن الأمثلة السلبية الصعبة)
  - Robust loss (خسارة صلبة)
  - Outliers (القيم الشاذة)
  - Inliers (القيم الداخلية)
  - Degenerate models (نماذج منحلة)

- **Equations:** Mathematical notation 10^4-10^5 preserved
- **Citations:** Multiple papers [19, 36], [34], [4], [5], [9], [7], [18], [35], [11], [10], [28], [20], [14], [30], [22], [26, 27], [17], [33, 37, 8, 22, 31], [2], [16]
- **Special handling:**
  - Model names preserved: LeCun, Viola-Jones, HOG, DPM, PASCAL, R-CNN variants, OverFeat, SSD, YOLO, FPN
  - ROI (Region of Interest) kept as acronym
  - Huber loss mentioned by name
  - COCO benchmark preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score: 0.89**

### Back-translation Check

Key technical phrases:
- "النافذة المنزلقة" → "Sliding window" ✓
- "التنقيب عن الأمثلة السلبية الصعبة" → "Hard negative mining" ✓
- "نماذج منحلة" → "Degenerate models" ✓
- "القيم الشاذة/الداخلية" → "Outliers/Inliers" ✓
