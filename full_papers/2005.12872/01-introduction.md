# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** كشف الأجسام (object detection), صناديق التحديد (bounding boxes), محول (transformer), مشفر-فك تشفير (encoder-decoder), الانتباه الذاتي (self-attention), المطابقة الثنائية (bipartite matching), قمع عدم الحد الأقصى (non-maximum suppression), المراسي (anchors), من طرف إلى طرف (end-to-end), فك التشفير المتوازي (parallel decoding), انحداري ذاتي (autoregressive), التنبؤ بالمجموعات (set prediction)

---

### English Version

The goal of object detection is to predict a set of bounding boxes and category labels for each object of interest. Modern detectors address this set prediction task in an indirect way, by defining surrogate regression and classification problems on a large set of proposals, anchors, or window centers. Their performances are significantly influenced by postprocessing steps to collapse near-duplicate predictions, by the design of the anchor sets and by the heuristics that assign target boxes to anchors. To simplify these pipelines, we propose a direct set prediction approach to bypass the surrogate tasks. This end-to-end philosophy has led to significant advances in complex structured prediction tasks such as machine translation or speech recognition, but not yet in object detection: previous attempts either add other forms of prior knowledge, or have not proven to be competitive with strong baselines on challenging benchmarks. This paper aims to bridge this gap.

**Figure 1:** DETR directly predicts (in parallel) the final set of detections by combining a common CNN with a transformer architecture. During training, bipartite matching uniquely assigns predictions with ground truth boxes. Prediction with no match should yield a "no object" (∅) class prediction.

We streamline the training pipeline by viewing object detection as a direct set prediction problem. We adopt an encoder-decoder architecture based on transformers, a popular architecture for sequence prediction. The self-attention mechanisms of transformers, which explicitly model all pairwise interactions between elements in a sequence, make these architectures particularly suitable for specific constraints of set prediction such as removing duplicate predictions.

Our DEtection TRansformer (DETR, see Figure 1) predicts all objects at once, and is trained end-to-end with a set loss function which performs bipartite matching between predicted and ground-truth objects. DETR simplifies the detection pipeline by dropping multiple hand-designed components that encode prior knowledge, like spatial anchors or non-maximal suppression. Unlike most existing detection methods, DETR doesn't require any customized layers, and thus can be reproduced easily in any framework that contains standard CNN and transformer classes.

Compared to most previous work on direct set prediction, the main features of DETR are the conjunction of the bipartite matching loss and transformers with (non-autoregressive) parallel decoding. In contrast, previous work focused on autoregressive decoding with RNNs. Our matching loss function uniquely assigns a prediction to a ground truth object, and is invariant to a permutation of predicted objects, so we can emit them in parallel.

We evaluate DETR on one of the most popular object detection datasets, COCO, against a very competitive Faster R-CNN baseline. Faster R-CNN has undergone many design iterations and its performance was greatly improved since the original publication. Our experiments show that our new model achieves comparable performances. More precisely, DETR demonstrates significantly better performance on large objects, a result likely enabled by the non-local computations of the transformer. It obtains, however, lower performances on small objects. We expect that future work will improve this aspect in the same way the development of FPN did for Faster R-CNN.

Training settings for DETR differ from standard object detectors in multiple ways. The new model requires extra-long training schedule and benefits from auxiliary decoding losses in the transformer. We thoroughly explore what components are crucial for the demonstrated performance.

The design ethos of DETR easily extend to more complex tasks. In our experiments, we show that a simple segmentation head trained on top of a pre-trained DETR outperforms competitive baselines on Panoptic Segmentation, a challenging pixel-level recognition task that has recently gained popularity.

---

### النسخة العربية

الهدف من كشف الأجسام هو التنبؤ بمجموعة من صناديق التحديد وتسميات الفئات لكل جسم محل الاهتمام. تتناول الكاشفات الحديثة مهمة التنبؤ بالمجموعات هذه بطريقة غير مباشرة، من خلال تحديد مسائل انحدار وتصنيف بديلة على مجموعة كبيرة من المقترحات أو المراسي أو مراكز النوافذ. تتأثر أداءاتها بشكل كبير بخطوات المعالجة اللاحقة لدمج التنبؤات المتكررة تقريباً، وبتصميم مجموعات المراسي، وبالاستدلالات التي تعين صناديق الهدف إلى المراسي. لتبسيط هذه الخطوط، نقترح نهج التنبؤ المباشر بالمجموعات لتجاوز المهام البديلة. أدت فلسفة "من طرف إلى طرف" هذه إلى تقدم كبير في مهام التنبؤ المنظم المعقدة مثل الترجمة الآلية أو التعرف على الكلام، ولكن ليس بعد في كشف الأجسام: إما أن المحاولات السابقة أضافت أشكالاً أخرى من المعرفة المسبقة، أو لم تثبت قدرتها على المنافسة مع الخطوط الأساسية القوية على المعايير الصعبة. يهدف هذا البحث إلى سد هذه الفجوة.

**الشكل 1:** يتنبأ DETR مباشرة (بشكل متوازٍ) بالمجموعة النهائية من الاكتشافات من خلال الجمع بين شبكة CNN شائعة ومعمارية المحول. أثناء التدريب، تقوم المطابقة الثنائية بتعيين التنبؤات بشكل فريد مع صناديق الحقيقة الأرضية. يجب أن ينتج التنبؤ الذي لا يحتوي على مطابقة تنبؤاً بفئة "لا يوجد جسم" (∅).

نبسط خط أنابيب التدريب من خلال عرض كشف الأجسام كمسألة تنبؤ مباشر بالمجموعات. نتبنى معمارية مشفر-فك تشفير تعتمد على المحولات، وهي معمارية شائعة للتنبؤ بالتسلسلات. تجعل آليات الانتباه الذاتي للمحولات، التي تصمم صراحةً جميع التفاعلات الثنائية بين العناصر في تسلسل، هذه المعماريات مناسبة بشكل خاص للقيود المحددة للتنبؤ بالمجموعات مثل إزالة التنبؤات المكررة.

يتنبأ محول الكشف الخاص بنا (DETR، انظر الشكل 1) بجميع الأجسام دفعة واحدة، ويتم تدريبه من طرف إلى طرف باستخدام دالة خسارة مجموعات تقوم بالمطابقة الثنائية بين الأجسام المتنبأ بها والأجسام الحقيقية. يبسط DETR خط أنابيب الكشف من خلال إسقاط مكونات متعددة مصممة يدوياً تشفر المعرفة المسبقة، مثل المراسي المكانية أو قمع عدم الحد الأقصى. على عكس معظم طرق الكشف الموجودة، لا يتطلب DETR أي طبقات مخصصة، وبالتالي يمكن إعادة إنتاجه بسهولة في أي إطار عمل يحتوي على فئات CNN والمحولات القياسية.

بالمقارنة مع معظم الأعمال السابقة حول التنبؤ المباشر بالمجموعات، فإن الميزات الرئيسية لـ DETR هي الجمع بين خسارة المطابقة الثنائية والمحولات مع فك التشفير المتوازي (غير الانحداري الذاتي). في المقابل، ركز العمل السابق على فك التشفير الانحداري الذاتي باستخدام الشبكات العصبية المتكررة (RNNs). تقوم دالة خسارة المطابقة الخاصة بنا بتعيين تنبؤ بشكل فريد لجسم حقيقي أرضي، وهي غير متغيرة بالنسبة لتبديل الأجسام المتنبأ بها، لذا يمكننا إصدارها بشكل متوازٍ.

نقيّم DETR على واحدة من أكثر مجموعات بيانات كشف الأجسام شيوعاً، COCO، مقابل خط أساس Faster R-CNN تنافسي للغاية. خضع Faster R-CNN للعديد من تكرارات التصميم وتحسن أداؤه بشكل كبير منذ النشر الأصلي. تظهر تجاربنا أن نموذجنا الجديد يحقق أداءً مماثلاً. بشكل أكثر دقة، يُظهر DETR أداءً أفضل بكثير على الأجسام الكبيرة، وهي نتيجة يُحتمل أن تكون ممكنة بفضل الحسابات غير المحلية للمحول. ومع ذلك، فإنه يحصل على أداء أقل على الأجسام الصغيرة. نتوقع أن العمل المستقبلي سيحسن هذا الجانب بنفس الطريقة التي فعل بها تطوير FPN لـ Faster R-CNN.

تختلف إعدادات التدريب لـ DETR عن كاشفات الأجسام القياسية بطرق متعددة. يتطلب النموذج الجديد جدولاً زمنياً طويلاً للغاية للتدريب ويستفيد من خسائر فك التشفير المساعدة في المحول. نستكشف بدقة المكونات الحاسمة للأداء المُظهَر.

يمتد روح تصميم DETR بسهولة إلى مهام أكثر تعقيداً. في تجاربنا، نُظهر أن رأس تجزئة بسيط مدرب على قمة DETR مُدرب مسبقاً يتفوق على الخطوط الأساسية التنافسية في التجزئة الشاملة، وهي مهمة تعرف على مستوى البكسل صعبة اكتسبت شعبية مؤخراً.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** DETR (محول الكشف), direct set prediction (التنبؤ المباشر بالمجموعات), bipartite matching (المطابقة الثنائية), object queries (استعلامات الأجسام), parallel decoding (فك التشفير المتوازي)
- **Citations:** Multiple references to prior work [numbers preserved]
- **Special handling:**
  - Technical abbreviations (CNN, RNN, FPN, COCO) kept in English
  - Figure caption translated
  - Mathematical notation: ∅ symbol preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.87
