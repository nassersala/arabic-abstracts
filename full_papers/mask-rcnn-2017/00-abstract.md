# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.88
**Glossary Terms Used:** instance segmentation, object detection, bounding box, Region of Interest (RoI), framework, architecture, mask

---

### English Version

We present a conceptually simple, flexible, and general framework for object instance segmentation. Our approach efficiently detects objects in an image while simultaneously generating a high-quality segmentation mask for each instance. The method, called Mask R-CNN, extends Faster R-CNN by adding a branch for predicting an object mask in parallel with the existing branch for bounding box recognition. Mask R-CNN is simple to train and adds only a small overhead to Faster R-CNN, running at 5 fps. In addition, Mask R-CNN is easy to generalize to other tasks, e.g., allowing us to estimate human poses in the same framework. We show top results in all three tracks of the COCO suite of challenges, including instance segmentation, bounding-box object detection, and person keypoint detection. Without bells and whistles, Mask R-CNN outperforms all existing, single-model entries on every task, including the COCO 2016 challenge winners.

---

### النسخة العربية

نقدم إطار عمل بسيط مفاهيمياً ومرناً وعاماً لتجزئة نسخ الكائنات (object instance segmentation). يكتشف نهجنا الكائنات في الصورة بكفاءة بينما يولد في الوقت نفسه قناع تجزئة عالي الجودة لكل نسخة. الطريقة، التي تسمى ماسك آر-سي إن إن (Mask R-CNN)، توسع فاستر آر-سي إن إن (Faster R-CNN) بإضافة فرع للتنبؤ بقناع الكائن بالتوازي مع الفرع الموجود للتعرف على صندوق التحديد (bounding box). ماسك آر-سي إن إن بسيطة في التدريب وتضيف فقط عبء حسابي صغير إلى فاستر آر-سي إن إن، وتعمل بسرعة 5 إطارات في الثانية. بالإضافة إلى ذلك، من السهل تعميم ماسك آر-سي إن إن على مهام أخرى، على سبيل المثال، مما يسمح لنا بتقدير أوضاع الإنسان في نفس إطار العمل. نُظهر نتائج متفوقة في جميع المسارات الثلاثة لمجموعة تحديات COCO، بما في ذلك تجزئة نسخ الكائنات، والكشف عن الكائنات بصناديق التحديد، والكشف عن النقاط المفصلية للأشخاص. بدون حيل إضافية، تتفوق ماسك آر-سي إن إن على جميع الإدخالات الموجودة للنموذج الواحد في كل مهمة، بما في ذلك الفائزين بتحدي COCO 2016.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Instance segmentation (تجزئة نسخ الكائنات)
  - Mask R-CNN (ماسك آر-سي إن إن)
  - Faster R-CNN (فاستر آر-سي إن إن)
  - Bounding box (صندوق التحديد)
  - Framework (إطار عمل)
  - Keypoint detection (الكشف عن النقاط المفصلية)
- **Equations:** None
- **Citations:** None
- **Special handling:**
  - COCO kept as English acronym (standard benchmark name)
  - "5 fps" kept as number (frames per second)
  - Model names (Mask R-CNN, Faster R-CNN) kept in English with Arabic transliteration

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
