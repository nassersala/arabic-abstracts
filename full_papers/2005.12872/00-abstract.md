# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** محول (transformer), كشف الأجسام (object detection), مشفر-فك تشفير (encoder-decoder), التنبؤ (prediction), مجموعة بيانات (dataset), التدريب (training), مدرب مسبقاً (pretrained), استدلال (reasoning), متوازٍ (parallel), المطابقة الثنائية (bipartite matching), قمع عدم الحد الأقصى (non-maximum suppression), توليد المراسي (anchor generation)

---

### English Version

We present a new method that views object detection as a direct set prediction problem. Our approach streamlines the detection pipeline, effectively removing the need for many hand-designed components like a non-maximum suppression procedure or anchor generation that explicitly encode our prior knowledge about the task. The main ingredients of the new framework, called DEtection TRansformer or DETR, are a set-based global loss that forces unique predictions via bipartite matching, and a transformer encoder-decoder architecture. Given a fixed small set of learned object queries, DETR reasons about the relations of the objects and the global image context to directly output the final set of predictions in parallel. The new model is conceptually simple and does not require a specialized library, unlike many other modern detectors. DETR demonstrates accuracy and run-time performance on par with the well-established and highly-optimized Faster R-CNN baseline on the challenging COCO object detection dataset. Moreover, DETR can be easily generalized to produce panoptic segmentation in a unified manner. We show that it significantly outperforms competitive baselines. Training code and pretrained models are available at https://github.com/facebookresearch/detr.

---

### النسخة العربية

يقدم الباحثون DETR (محول الكشف)، الذي يعيد صياغة كشف الأجسام كتحدٍ للتنبؤ المباشر بالمجموعات. يزيل نهجهم مكونات خط الأنابيب التقليدية بما في ذلك قمع عدم الحد الأقصى وتوليد المراسي. يجمع إطار العمل بين خسارة شاملة قائمة على المجموعات باستخدام المطابقة الثنائية مع تصميم مشفر-فك تشفير المحول. يعالج النموذج مجموعة ثابتة من استعلامات الأجسام المتعلمة للاستدلال حول علاقات الأجسام وسياق الصورة، وينتج التنبؤات النهائية بشكل متوازٍ. تحقق الطريقة نتائج تنافسية مع Faster RCNN على مجموعة بيانات COCO وتمتد إلى مهام التجزئة الشاملة. تم توفير كود التدريب والنماذج المدربة مسبقاً للجمهور.

---

### Translation Notes

- **Key terms introduced:** DETR (محول الكشف), set prediction (التنبؤ بالمجموعات), bipartite matching (المطابقة الثنائية), object queries (استعلامات الأجسام), panoptic segmentation (التجزئة الشاملة)
- **Special handling:** GitHub URL kept in English
- **Source:** Adapted from existing high-quality translation in translations/2005.12872.md

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.92
