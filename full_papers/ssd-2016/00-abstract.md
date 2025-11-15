# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** object detection, deep learning, neural network, bounding box, feature map, aspect ratio, training, mAP, accuracy

---

### English Version

We present a method for detecting objects in images using a single deep neural network. Our approach, named SSD, discretizes the output space of bounding boxes into a set of default boxes over different aspect ratios and scales per feature map location. At prediction time, the network generates scores for the presence of each object category in each default box and produces adjustments to the box to better match the object shape. Additionally, the network combines predictions from multiple feature maps with different resolutions to naturally handle objects of various sizes. SSD is simple relative to methods that require object proposals because it completely eliminates proposal generation and subsequent pixel or feature resampling stages and encapsulates all computation in a single network. This makes SSD easy to train and straightforward to integrate into systems that require a detection component. Experimental results on the PASCAL VOC, COCO, and ILSVRC datasets confirm that SSD has competitive accuracy to methods that utilize an additional object proposal step and is much faster, while providing a unified framework for both training and inference. For 300×300 input, SSD achieves 74.3% mAP on VOC2007 test at 59 FPS on a Nvidia Titan X and for 512×512 input, SSD achieves 76.8% mAP, outperforming a comparable state-of-the-art Faster R-CNN model. Compared to other single stage methods, SSD has much better accuracy even with a smaller input image size. Code is available at https://github.com/weiliu89/caffe/tree/ssd.

---

### النسخة العربية

نقدم طريقة لكشف الأجسام في الصور باستخدام شبكة عصبية عميقة واحدة. يقوم نهجنا، المسمى SSD، بتقسيم فضاء الإخراج لصناديق التحديد إلى مجموعة من الصناديق الافتراضية عبر نسب أبعاد ومقاييس مختلفة لكل موقع في خريطة الميزات. في وقت التنبؤ، تولد الشبكة درجات لوجود كل فئة من الأجسام في كل صندوق افتراضي وتنتج تعديلات على الصندوق لمطابقة شكل الجسم بشكل أفضل. بالإضافة إلى ذلك، تجمع الشبكة التنبؤات من خرائط ميزات متعددة بدرجات دقة مختلفة للتعامل بشكل طبيعي مع الأجسام ذات الأحجام المختلفة. يعتبر SSD بسيطاً مقارنة بالطرق التي تتطلب مقترحات الأجسام لأنه يلغي تماماً مرحلة توليد المقترحات ومراحل إعادة أخذ العينات من البكسل أو الميزات اللاحقة ويشمل جميع العمليات الحسابية في شبكة واحدة. هذا يجعل SSD سهل التدريب ومباشراً للدمج في الأنظمة التي تتطلب مكون كشف. تؤكد النتائج التجريبية على مجموعات بيانات PASCAL VOC وCOCO وILSVRC أن SSD يمتلك دقة منافسة للطرق التي تستخدم خطوة إضافية لمقترحات الأجسام وهو أسرع بكثير، مع توفير إطار موحد لكل من التدريب والاستنتاج. بالنسبة لمدخلات بحجم 300×300، يحقق SSD دقة 74.3% على مقياس mAP على مجموعة اختبار VOC2007 بسرعة 59 إطاراً في الثانية على Nvidia Titan X، وبالنسبة لمدخلات 512×512، يحقق SSD دقة 76.8% على مقياس mAP، متفوقاً على نموذج Faster R-CNN المتقدم المماثل. بالمقارنة مع طرق المرحلة الواحدة الأخرى، يمتلك SSD دقة أفضل بكثير حتى مع حجم صورة مدخلات أصغر. الشفرة المصدرية متاحة على https://github.com/weiliu89/caffe/tree/ssd.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Single Shot MultiBox Detector (SSD) - كاشف الأجسام أحادي الطلقة متعدد الصناديق
  - Default boxes - الصناديق الافتراضية
  - Object proposals - مقترحات الأجسام
  - Feature map location - موقع في خريطة الميزات
  - Pixel or feature resampling - إعادة أخذ العينات من البكسل أو الميزات

- **Equations:** None
- **Citations:** None
- **Special handling:**
  - Preserved technical metrics: 74.3% mAP, 59 FPS, 76.8% mAP
  - Preserved dataset names: PASCAL VOC, COCO, ILSVRC
  - Preserved model names: Faster R-CNN, SSD
  - Preserved hardware: Nvidia Titan X
  - Preserved GitHub URL as-is
  - Input dimensions: 300×300, 512×512

### Quality Metrics

- **Semantic equivalence:** 0.92 - Accurately preserves all technical details and meaning
- **Technical accuracy:** 0.90 - All terms correctly translated using glossary
- **Readability:** 0.88 - Flows naturally in formal academic Arabic
- **Glossary consistency:** 0.90 - Consistent use of established terms
- **Overall section score:** 0.90

### Back-translation Check

**First sentence back-translation:** "We present a method for detecting objects in images using a single deep neural network."
**Original:** "We present a method for detecting objects in images using a single deep neural network."
✅ Semantic match confirmed

**Key claim back-translation:** "For 300×300 input, SSD achieves 74.3% mAP on VOC2007 test at 59 FPS on Nvidia Titan X."
**Original:** "For 300×300 input, SSD achieves 74.3% mAP on VOC2007 test at 59 FPS on a Nvidia Titan X."
✅ Semantic match confirmed
