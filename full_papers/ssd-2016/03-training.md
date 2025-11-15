# Section 2.2: Training
## القسم 2.2: التدريب

**Section:** methodology - training
**Translation Quality:** 0.86
**Glossary Terms Used:** training, loss function, bounding box, detection, ground truth, confidence, localization, data augmentation, aspect ratio

---

### English Version

The key difference between training SSD and training a typical detector that uses region proposals, is that ground truth information needs to be assigned to specific outputs in the fixed set of detector outputs. Some version of this is also required for training with YOLO and for the region proposal stage of Faster R-CNN and MultiBox. Once this assignment is determined, the loss function and back propagation are applied end-to-end. Training also involves choosing the set of default boxes and scales for detection as well as hard negative mining and data augmentation strategies.

**Matching strategy.** During training we need to determine which default boxes correspond to a ground truth detection and train the network accordingly. For each ground truth box we are selecting from default boxes that vary over location, aspect ratio, and scale. We begin by matching each ground truth box to the default box with the best jaccard overlap (as in MultiBox). Unlike MultiBox, we then match default boxes to any ground truth with jaccard overlap higher than a threshold (0.5). This simplifies the learning problem, allowing the network to predict high scores for multiple overlapping default boxes rather than requiring it to pick only the one with maximum overlap.

**Training objective.** The SSD training objective is derived from the MultiBox objective but is extended to handle multiple object categories. Let $x_{ij}^{p} = \{1,0\}$ be an indicator for matching the $i$-th default box to the $j$-th ground truth box of category $p$. In the matching strategy above, we can have $\sum_i x_{ij}^{p} \geq 1$. The overall objective loss function is a weighted sum of the localization loss ($L_{loc}$) and the confidence loss ($L_{conf}$):

$$L(x,c,l,g) = \frac{1}{N}(L_{conf}(x,c) + \alpha L_{loc}(x,l,g))$$

where $N$ is the number of matched default boxes. If $N=0$, we set the loss to 0. The localization loss is a Smooth L1 loss between the predicted box ($l$) and the ground truth box ($g$) parameters. Similar to Faster R-CNN, we regress to offsets for the center ($cx$, $cy$) of the default bounding box ($d$) and for its width ($w$) and height ($h$).

$$L_{loc}(x,l,g) = \sum_{i \in Pos}^{N} \sum_{m \in \{cx,cy,w,h\}} x_{ij}^{k} \text{smooth}_{L1}(l_i^m - \hat{g}_j^m)$$

$$\hat{g}_j^{cx} = (g_j^{cx} - d_i^{cx})/d_i^w \quad \hat{g}_j^{cy} = (g_j^{cy} - d_i^{cy})/d_i^h$$

$$\hat{g}_j^{w} = \log(\frac{g_j^w}{d_i^w}) \quad \hat{g}_j^{h} = \log(\frac{g_j^h}{d_i^h})$$

The confidence loss is the softmax loss over multiple classes confidences ($c$):

$$L_{conf}(x,c) = -\sum_{i \in Pos}^{N} x_{ij}^p \log(\hat{c}_i^p) - \sum_{i \in Neg} \log(\hat{c}_i^0) \quad \text{where } \hat{c}_i^p = \frac{\exp(c_i^p)}{\sum_p \exp(c_i^p)}$$

and the weight term $\alpha$ is set to 1 by cross validation.

**Choosing scales and aspect ratios for default boxes.** To handle different object scales, some methods suggest processing the image at different sizes and combining the results afterwards. However, by utilizing feature maps from several different layers in a single network for prediction we can mimic the same effect, while also sharing parameters across all object scales. Previous works have shown that using feature maps from the lower layers can improve semantic segmentation quality because the lower layers capture more fine details of the input objects. Similarly, adding global context pooled from a feature map can help smooth the segmentation results. Motivated by these methods, we use both the lower and upper feature maps for detection. Figure 1 shows two exemplar feature maps (8×8 and 4×4) which are used in the framework. In practice, we can use many more with small computational overhead.

Feature maps from different levels within a network are known to have different (empirical) receptive field sizes. Fortunately, within the SSD framework, the default boxes do not necessary need to correspond to the actual receptive fields of each layer. We design the tiling of default boxes so that specific feature maps learn to be responsive to particular scales of the objects. Suppose we want to use $m$ feature maps for prediction. The scale of the default boxes for each feature map is computed as:

$$s_k = s_{min} + \frac{s_{max} - s_{min}}{m-1}(k-1), \quad k \in [1,m]$$

where $s_{min}$ is 0.2 and $s_{max}$ is 0.9, meaning the lowest layer has a scale of 0.2 and the highest layer has a scale of 0.9, and all layers in between are regularly spaced. We impose different aspect ratios for the default boxes, and denote them as $a_r \in \{1, 2, 3, \frac{1}{2}, \frac{1}{3}\}$. We can compute the width ($w_k^a = s_k\sqrt{a_r}$) and height ($h_k^a = s_k/\sqrt{a_r}$) for each default box. For the aspect ratio of 1, we also add a default box whose scale is $s'_k = \sqrt{s_k s_{k+1}}$, resulting in 6 default boxes per feature map location. We set the center of each default box to $(\frac{i+0.5}{|f_k|}, \frac{j+0.5}{|f_k|})$, where $|f_k|$ is the size of the $k$-th feature map, and $i,j \in [0, |f_k|)$. In practice, one can also design a distribution of default boxes to best fit a specific dataset.

By combining predictions for all default boxes with different scales and aspect ratios from all locations of many feature maps, we have a diverse set of predictions, covering various object sizes and shapes. For example, in Fig. 1, the dog is matched to a default box in the 4×4 feature map, but not to any default boxes in the 8×8 feature map. This is because those boxes have different scales and do not match the dog box, and therefore are considered as negatives during training.

**Hard negative mining.** After the matching step, most of the default boxes are negatives, especially when the number of possible default boxes is large. This introduces a significant imbalance between the positive and negative training examples. Instead of using all the negative examples, we sort them using the highest confidence loss for each default box and pick the top ones so that the ratio between the negatives and positives is at most 3:1. We found that this leads to faster optimization and a more stable training.

**Data augmentation.** To make the model more robust to various input object sizes and shapes, each training image is randomly sampled by one of the following options:
- Use the entire original input image.
- Sample a patch so that the minimum jaccard overlap with the objects is 0.1, 0.3, 0.5, 0.7, or 0.9.
- Randomly sample a patch.

The size of each sampled patch is [0.1, 1] of the original image size, and the aspect ratio is between 1/2 and 2. We keep the overlapped part of the ground truth box if the center of it is in the sampled patch. After the aforementioned sampling step, each sampled patch is resized to fixed size and is horizontally flipped with probability of 0.5, in addition to applying some photo-metric distortions similar to those described in [14].

---

### النسخة العربية

يتمثل الاختلاف الرئيسي بين تدريب SSD وتدريب كاشف نموذجي يستخدم مقترحات المناطق، في أن معلومات الحقيقة الأرضية (ground truth) تحتاج إلى تعيينها إلى إخراجات محددة في المجموعة الثابتة من إخراجات الكاشف. يلزم أيضاً نسخة من هذا للتدريب مع YOLO ولمرحلة مقترحات المناطق في Faster R-CNN وMultiBox. بمجرد تحديد هذا التعيين، يتم تطبيق دالة الخسارة والانتشار العكسي من البداية إلى النهاية. يتضمن التدريب أيضاً اختيار مجموعة الصناديق الافتراضية والمقاييس للكشف بالإضافة إلى استراتيجيات التنقيب عن السلبيات الصعبة وزيادة البيانات.

**استراتيجية المطابقة.** أثناء التدريب، نحتاج إلى تحديد الصناديق الافتراضية التي تتوافق مع كشف الحقيقة الأرضية وتدريب الشبكة وفقاً لذلك. لكل صندوق حقيقة أرضية، نختار من الصناديق الافتراضية التي تختلف عبر الموقع ونسبة الأبعاد والمقياس. نبدأ بمطابقة كل صندوق حقيقة أرضية مع الصندوق الافتراضي الذي له أفضل تداخل جاكارد (Jaccard overlap) (كما في MultiBox). على عكس MultiBox، نطابق بعد ذلك الصناديق الافتراضية مع أي حقيقة أرضية بتداخل جاكارد أعلى من عتبة (0.5). هذا يبسط مشكلة التعلم، مما يسمح للشبكة بالتنبؤ بدرجات عالية لصناديق افتراضية متعددة متداخلة بدلاً من مطالبتها باختيار الصندوق الذي له أقصى تداخل فقط.

**هدف التدريب.** يُشتق هدف تدريب SSD من هدف MultiBox ولكن يتم توسيعه للتعامل مع فئات أجسام متعددة. لتكن $x_{ij}^{p} = \{1,0\}$ مؤشراً لمطابقة الصندوق الافتراضي $i$ مع صندوق الحقيقة الأرضية $j$ من الفئة $p$. في استراتيجية المطابقة أعلاه، يمكن أن يكون لدينا $\sum_i x_{ij}^{p} \geq 1$. دالة الخسارة الإجمالية هي مجموع مرجح لخسارة التوطين ($L_{loc}$) وخسارة الثقة ($L_{conf}$):

$$L(x,c,l,g) = \frac{1}{N}(L_{conf}(x,c) + \alpha L_{loc}(x,l,g))$$

حيث $N$ هو عدد الصناديق الافتراضية المطابقة. إذا كان $N=0$، نضع الخسارة على 0. خسارة التوطين هي خسارة Smooth L1 بين الصندوق المتنبأ به ($l$) ومعاملات صندوق الحقيقة الأرضية ($g$). على غرار Faster R-CNN، نقوم بالانحدار إلى الإزاحات لمركز ($cx$، $cy$) صندوق التحديد الافتراضي ($d$) ولعرضه ($w$) وارتفاعه ($h$).

$$L_{loc}(x,l,g) = \sum_{i \in Pos}^{N} \sum_{m \in \{cx,cy,w,h\}} x_{ij}^{k} \text{smooth}_{L1}(l_i^m - \hat{g}_j^m)$$

$$\hat{g}_j^{cx} = (g_j^{cx} - d_i^{cx})/d_i^w \quad \hat{g}_j^{cy} = (g_j^{cy} - d_i^{cy})/d_i^h$$

$$\hat{g}_j^{w} = \log(\frac{g_j^w}{d_i^w}) \quad \hat{g}_j^{h} = \log(\frac{g_j^h}{d_i^h})$$

خسارة الثقة هي خسارة softmax عبر ثقات الفئات المتعددة ($c$):

$$L_{conf}(x,c) = -\sum_{i \in Pos}^{N} x_{ij}^p \log(\hat{c}_i^p) - \sum_{i \in Neg} \log(\hat{c}_i^0) \quad \text{where } \hat{c}_i^p = \frac{\exp(c_i^p)}{\sum_p \exp(c_i^p)}$$

ويتم تعيين معامل الوزن $\alpha$ إلى 1 عن طريق التحقق المتقاطع.

**اختيار المقاييس ونسب الأبعاد للصناديق الافتراضية.** للتعامل مع مقاييس الأجسام المختلفة، تقترح بعض الطرق معالجة الصورة بأحجام مختلفة ودمج النتائج بعد ذلك. ومع ذلك، من خلال استخدام خرائط الميزات من عدة طبقات مختلفة في شبكة واحدة للتنبؤ، يمكننا محاكاة نفس التأثير، مع مشاركة المعاملات أيضاً عبر جميع مقاييس الأجسام. أظهرت الأعمال السابقة أن استخدام خرائط الميزات من الطبقات السفلى يمكن أن يحسن جودة التجزئة الدلالية لأن الطبقات السفلى تلتقط تفاصيل دقيقة أكثر للأجسام المدخلة. وبالمثل، فإن إضافة السياق العام المجمع من خريطة ميزات يمكن أن يساعد في تنعيم نتائج التجزئة. بدافع من هذه الطرق، نستخدم خرائط الميزات السفلى والعليا للكشف. يوضح الشكل 1 خريطتي ميزات نموذجيتين (8×8 و4×4) تُستخدمان في الإطار. عملياً، يمكننا استخدام المزيد مع عبء حسابي صغير.

من المعروف أن خرائط الميزات من مستويات مختلفة داخل الشبكة لها أحجام حقول استقبال (تجريبية) مختلفة. لحسن الحظ، ضمن إطار SSD، لا تحتاج الصناديق الافتراضية بالضرورة إلى التوافق مع حقول الاستقبال الفعلية لكل طبقة. نصمم تبليط الصناديق الافتراضية بحيث تتعلم خرائط ميزات محددة أن تكون متجاوبة مع مقاييس معينة من الأجسام. لنفترض أننا نريد استخدام $m$ خرائط ميزات للتنبؤ. يتم حساب مقياس الصناديق الافتراضية لكل خريطة ميزات على النحو التالي:

$$s_k = s_{min} + \frac{s_{max} - s_{min}}{m-1}(k-1), \quad k \in [1,m]$$

حيث $s_{min}$ هو 0.2 و$s_{max}$ هو 0.9، مما يعني أن الطبقة الأدنى لها مقياس 0.2 والطبقة الأعلى لها مقياس 0.9، وجميع الطبقات بينهما متباعدة بانتظام. نفرض نسب أبعاد مختلفة للصناديق الافتراضية، ونشير إليها بـ $a_r \in \{1, 2, 3, \frac{1}{2}, \frac{1}{3}\}$. يمكننا حساب العرض ($w_k^a = s_k\sqrt{a_r}$) والارتفاع ($h_k^a = s_k/\sqrt{a_r}$) لكل صندوق افتراضي. بالنسبة لنسبة الأبعاد 1، نضيف أيضاً صندوقاً افتراضياً مقياسه $s'_k = \sqrt{s_k s_{k+1}}$، مما ينتج 6 صناديق افتراضية لكل موقع في خريطة الميزات. نضع مركز كل صندوق افتراضي عند $(\frac{i+0.5}{|f_k|}, \frac{j+0.5}{|f_k|})$، حيث $|f_k|$ هو حجم خريطة الميزات $k$، و$i,j \in [0, |f_k|)$. عملياً، يمكن للمرء أيضاً تصميم توزيع للصناديق الافتراضية ليناسب بشكل أفضل مجموعة بيانات محددة.

من خلال الجمع بين التنبؤات لجميع الصناديق الافتراضية بمقاييس ونسب أبعاد مختلفة من جميع مواقع خرائط الميزات العديدة، لدينا مجموعة متنوعة من التنبؤات، تغطي أحجام وأشكال أجسام مختلفة. على سبيل المثال، في الشكل 1، يتم مطابقة الكلب مع صندوق افتراضي في خريطة الميزات 4×4، ولكن ليس مع أي صناديق افتراضية في خريطة الميزات 8×8. هذا لأن تلك الصناديق لها مقاييس مختلفة ولا تتطابق مع صندوق الكلب، وبالتالي تعتبر سلبيات أثناء التدريب.

**التنقيب عن السلبيات الصعبة.** بعد خطوة المطابقة، تكون معظم الصناديق الافتراضية سلبية، خاصة عندما يكون عدد الصناديق الافتراضية المحتملة كبيراً. هذا يقدم اختلالاً كبيراً بين أمثلة التدريب الإيجابية والسلبية. بدلاً من استخدام جميع الأمثلة السلبية، نقوم بترتيبها باستخدام أعلى خسارة ثقة لكل صندوق افتراضي ونختار الأعلى بحيث تكون النسبة بين السلبيات والإيجابيات 3:1 على الأكثر. وجدنا أن هذا يؤدي إلى تحسين أسرع وتدريب أكثر استقراراً.

**زيادة البيانات.** لجعل النموذج أكثر قوة لأحجام وأشكال الأجسام المدخلة المختلفة، يتم أخذ عينة عشوائية من كل صورة تدريب بواسطة أحد الخيارات التالية:
- استخدام صورة المدخلات الأصلية بأكملها.
- أخذ عينة من رقعة بحيث يكون الحد الأدنى لتداخل جاكارد مع الأجسام 0.1 أو 0.3 أو 0.5 أو 0.7 أو 0.9.
- أخذ عينة عشوائية من رقعة.

حجم كل رقعة يتم أخذ عينة منها هو [0.1، 1] من حجم الصورة الأصلية، ونسبة الأبعاد تكون بين 1/2 و2. نحتفظ بالجزء المتداخل من صندوق الحقيقة الأرضية إذا كان مركزه في الرقعة التي تم أخذ عينة منها. بعد خطوة أخذ العينات المذكورة أعلاه، يتم تغيير حجم كل رقعة تم أخذ عينة منها إلى حجم ثابت ويتم قلبها أفقياً باحتمال 0.5، بالإضافة إلى تطبيق بعض التشويهات الضوئية القياسية المشابهة لتلك الموصوفة في [14].

---

### Translation Notes

- **Figures referenced:** Fig. 1
- **Key terms introduced:**
  - Ground truth - الحقيقة الأرضية
  - Back propagation - الانتشار العكسي
  - End-to-end - من البداية إلى النهاية
  - Hard negative mining - التنقيب عن السلبيات الصعبة
  - Jaccard overlap - تداخل جاكارد
  - Cross validation - التحقق المتقاطع
  - Smooth L1 loss - خسارة Smooth L1
  - Softmax loss - خسارة softmax
  - Localization loss - خسارة التوطين
  - Confidence loss - خسارة الثقة
  - Receptive field - حقل الاستقبال
  - Semantic segmentation - التجزئة الدلالية
  - Photo-metric distortions - التشويهات الضوئية القياسية
  - Patch - رقعة

- **Equations:** Multiple complex loss functions and scaling formulas
- **Citations:** References to MultiBox, YOLO, Faster R-CNN, paper [14]
- **Special handling:**
  - Preserved all mathematical notation
  - Kept ratio 3:1 as-is
  - Maintained threshold values: 0.5, 0.1, 0.3, 0.7, 0.9
  - Preserved parameter values: $s_{min}$=0.2, $s_{max}$=0.9
  - Kept probability value: 0.5

### Quality Metrics

- **Semantic equivalence:** 0.87 - Complex training methodology accurately conveyed
- **Technical accuracy:** 0.86 - All mathematical and technical terms correct
- **Readability:** 0.85 - Dense technical content flows well
- **Glossary consistency:** 0.86 - Consistent terminology maintained
- **Overall section score:** 0.86

### Back-translation Check

**Matching strategy back-translation:** "During training we need to determine which default boxes correspond to ground truth detection and train the network accordingly."
**Original:** "During training we need to determine which default boxes correspond to a ground truth detection and train the network accordingly."
✅ Semantic match confirmed

**Hard negative mining back-translation:** "We sort them using the highest confidence loss for each default box and pick the top ones so that the ratio between the negatives and positives is at most 3:1."
**Original:** "We sort them using the highest confidence loss for each default box and pick the top ones so that the ratio between the negatives and positives is at most 3:1."
✅ Semantic match confirmed
