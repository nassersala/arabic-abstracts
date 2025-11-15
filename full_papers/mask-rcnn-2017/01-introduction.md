# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** instance segmentation, object detection, semantic segmentation, bounding box, Region of Interest, RoI, classification, localization, Fast R-CNN, Faster R-CNN, FCN, RoIPool, RoIAlign

---

### English Version

The vision community has rapidly improved object detection and semantic segmentation results over a short period of time. In large part, these advances have been driven by powerful baseline systems, such as the Fast/Faster R-CNN and Fully Convolutional Network (FCN) frameworks for object detection and semantic segmentation, respectively. These methods are conceptually intuitive and offer flexibility and robustness, together with fast training and inference time. Our work was inspired by this simple and flexible framework.

In this paper, we present a conceptually simple, flexible, and general framework for object instance segmentation. Instance segmentation is challenging because it requires the correct detection of all objects in an image while also precisely segmenting each instance. It therefore combines elements from the classical computer vision tasks of object detection, where the goal is to classify individual objects and localize each using a bounding box, and semantic segmentation, where the goal is to classify each pixel into a fixed set of categories without differentiating object instances.

Our approach, called Mask R-CNN, extends Faster R-CNN by adding a branch for predicting segmentation masks on each Region of Interest (RoI), in parallel with the existing branch for classification and bounding box regression. The mask branch is a small FCN applied to each RoI, predicting a segmentation mask in a pixel-to-pixel manner.

Mask R-CNN is simple to train and adds only a small overhead to Faster R-CNN, running at 5 fps. Moreover, Mask R-CNN is easy to generalize to other tasks, e.g., allowing us to estimate human poses in the same framework.

We show top results in all three tracks of the COCO suite of challenges, including instance segmentation, bounding-box object detection, and person keypoint detection. Without bells and whistles, Mask R-CNN outperforms all existing, single-model entries on every task, including the COCO 2016 challenge winners.

However, achieving state-of-the-art results requires addressing several important details. Faster R-CNN was not designed for pixel-to-pixel alignment between network inputs and outputs. This is most evident in how RoIPool, the de facto core operation for attending to instances, performs coarse spatial quantization for feature extraction. To fix the misalignment, we propose a simple, quantization-free layer, called RoIAlign, that faithfully preserves exact spatial locations. Despite being a seemingly minor change, RoIAlign has a large impact: it improves mask accuracy by relative 10% to 50%, showing bigger gains under stricter localization metrics. Second, we found it essential to decouple mask and class prediction: we predict a binary mask for each class independently, without competition among classes, and rely on the network's RoI classification branch to predict the category. In contrast, FCNs usually perform per-pixel multi-class categorization, which couples segmentation and classification, and based on our experiments works poorly for instance segmentation.

Without bells and whistles, Mask R-CNN surpasses all previous state-of-the-art single-model results on the COCO instance segmentation task, including the heavily-engineered entries from the 2016 competition winner.

---

### النسخة العربية

حقق مجتمع الرؤية الحاسوبية تحسينات سريعة في نتائج الكشف عن الكائنات والتجزئة الدلالية خلال فترة زمنية قصيرة. في جزء كبير منه، كانت هذه التطورات مدفوعة بأنظمة أساسية قوية، مثل أطر عمل فاست/فاستر آر-سي إن إن (Fast/Faster R-CNN) والشبكة الالتفافية الكاملة (FCN) للكشف عن الكائنات والتجزئة الدلالية، على التوالي. هذه الطرق بديهية مفاهيمياً وتوفر المرونة والمتانة، إلى جانب وقت تدريب واستدلال سريع. ألهم عملنا هذا الإطار البسيط والمرن.

في هذا البحث، نقدم إطار عمل بسيط مفاهيمياً ومرناً وعاماً لتجزئة نسخ الكائنات. تجزئة نسخ الكائنات (Instance segmentation) مليئة بالتحديات لأنها تتطلب الكشف الصحيح عن جميع الكائنات في صورة بينما تقوم أيضاً بتجزئة كل نسخة بدقة. وبالتالي فهي تجمع عناصر من مهام الرؤية الحاسوبية الكلاسيكية المتمثلة في الكشف عن الكائنات، حيث الهدف هو تصنيف الكائنات الفردية وتحديد موقع كل منها باستخدام صندوق تحديد، والتجزئة الدلالية، حيث الهدف هو تصنيف كل بكسل إلى مجموعة ثابتة من الفئات دون التمييز بين نسخ الكائنات.

نهجنا، المسمى ماسك آر-سي إن إن، يوسع فاستر آر-سي إن إن بإضافة فرع للتنبؤ بأقنعة التجزئة على كل منطقة اهتمام (Region of Interest - RoI)، بالتوازي مع الفرع الموجود للتصنيف وانحدار صندوق التحديد. فرع القناع عبارة عن شبكة التفافية كاملة (FCN) صغيرة مطبقة على كل منطقة اهتمام، تتنبأ بقناع تجزئة بطريقة بكسل تلو بكسل.

ماسك آر-سي إن إن بسيطة في التدريب وتضيف فقط عبء حسابي صغير إلى فاستر آر-سي إن إن، وتعمل بسرعة 5 إطارات في الثانية. علاوة على ذلك، من السهل تعميم ماسك آر-سي إن إن على مهام أخرى، على سبيل المثال، مما يسمح لنا بتقدير أوضاع الإنسان في نفس إطار العمل.

نُظهر نتائج متفوقة في جميع المسارات الثلاثة لمجموعة تحديات COCO، بما في ذلك تجزئة نسخ الكائنات، والكشف عن الكائنات بصناديق التحديد، والكشف عن النقاط المفصلية للأشخاص. بدون حيل إضافية، تتفوق ماسك آر-سي إن إن على جميع الإدخالات الموجودة للنموذج الواحد في كل مهمة، بما في ذلك الفائزين بتحدي COCO 2016.

ومع ذلك، فإن تحقيق نتائج متقدمة يتطلب معالجة العديد من التفاصيل المهمة. لم يتم تصميم فاستر آر-سي إن إن لمحاذاة بكسل تلو بكسل بين مدخلات ومخرجات الشبكة. هذا واضح بشكل خاص في كيفية قيام آر أو آي بول (RoIPool)، وهي العملية الأساسية الفعلية للانتباه إلى النسخ، بإجراء تكميم مكاني خشن لاستخراج الميزات. لإصلاح عدم المحاذاة، نقترح طبقة بسيطة خالية من التكميم، تسمى آر أو آي ألاين (RoIAlign)، التي تحافظ بأمانة على المواقع المكانية الدقيقة. على الرغم من كونه تغييراً يبدو بسيطاً، فإن آر أو آي ألاين له تأثير كبير: فهو يحسن دقة القناع بنسبة 10٪ إلى 50٪ نسبياً، ويظهر مكاسب أكبر في ظل مقاييس توطين أكثر صرامة. ثانياً، وجدنا أنه من الضروري فصل التنبؤ بالقناع والصنف: نتنبأ بقناع ثنائي لكل صنف بشكل مستقل، دون منافسة بين الأصناف، ونعتمد على فرع تصنيف منطقة الاهتمام في الشبكة للتنبؤ بالفئة. في المقابل، تقوم الشبكات الالتفافية الكاملة (FCNs) عادةً بالتصنيف متعدد الفئات لكل بكسل، والذي يربط التجزئة والتصنيف، وبناءً على تجاربنا يعمل بشكل سيئ لتجزئة نسخ الكائنات.

بدون حيل إضافية، تتفوق ماسك آر-سي إن إن على جميع النتائج السابقة المتقدمة للنموذج الواحد في مهمة تجزئة نسخ الكائنات COCO، بما في ذلك الإدخالات المصممة بشكل مكثف من الفائز بمسابقة 2016.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:**
  - Instance segmentation (تجزئة نسخ الكائنات)
  - Object detection (الكشف عن الكائنات)
  - Semantic segmentation (التجزئة الدلالية)
  - Bounding box (صندوق التحديد)
  - Region of Interest / RoI (منطقة الاهتمام / RoI)
  - RoIPool (آر أو آي بول)
  - RoIAlign (آر أو آي ألاين)
  - Classification (التصنيف)
  - Localization (التوطين)
  - Fully Convolutional Network / FCN (الشبكة الالتفافية الكاملة)
- **Equations:** None
- **Citations:** References to Fast R-CNN, Faster R-CNN, FCN, COCO challenge
- **Special handling:**
  - Model names kept in English with Arabic transliteration
  - COCO kept as acronym
  - Technical terms like RoIPool, RoIAlign kept in English with transliteration
  - "5 fps" kept as number

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
