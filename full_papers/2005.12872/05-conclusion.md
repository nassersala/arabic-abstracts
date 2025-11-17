# Section 5: Conclusion
## القسم 5: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** كشف الأجسام (object detection), محول (transformer), المطابقة الثنائية (bipartite matching), التنبؤ بالمجموعات (set prediction), التجزئة الشاملة (panoptic segmentation), الانتباه الذاتي (self-attention)

---

### English Version

We presented DETR, a new design for object detection systems based on transformers and bipartite matching loss for direct set prediction. The approach achieves comparable results to an optimized Faster R-CNN baseline on the challenging COCO dataset. DETR is straightforward to implement and has a flexible architecture that is easily extensible to panoptic segmentation, with competitive results. In addition, it achieves significantly better performance on large objects than Faster R-CNN, likely thanks to the processing of global information performed by the self-attention.

This new design for detectors also comes with new challenges, in particular regarding training, optimization and performances on small objects. Current detectors required several years of improvements to cope with similar issues, and we expect future work to successfully address them for DETR.

---

### النسخة العربية

قدمنا DETR، تصميماً جديداً لأنظمة كشف الأجسام يعتمد على المحولات وخسارة المطابقة الثنائية للتنبؤ المباشر بالمجموعات. يحقق النهج نتائج مماثلة لخط أساس Faster R-CNN المحسّن على مجموعة بيانات COCO الصعبة. DETR مباشر في التنفيذ وله معمارية مرنة قابلة للتوسع بسهولة إلى التجزئة الشاملة، مع نتائج تنافسية. بالإضافة إلى ذلك، يحقق أداءً أفضل بكثير على الأجسام الكبيرة من Faster R-CNN، على الأرجح بفضل معالجة المعلومات العامة التي يقوم بها الانتباه الذاتي.

يأتي هذا التصميم الجديد للكاشفات أيضاً بتحديات جديدة، خاصة فيما يتعلق بالتدريب والتحسين والأداء على الأجسام الصغيرة. تطلبت الكاشفات الحالية عدة سنوات من التحسينات للتعامل مع مسائل مماثلة، ونتوقع أن يعالج العمل المستقبلي هذه المسائل بنجاح لـ DETR.

---

### Translation Notes

- **Key contributions summarized:**
  - New transformer-based architecture for object detection
  - Direct set prediction with bipartite matching
  - Competitive results with Faster R-CNN on COCO
  - Easy extensibility to panoptic segmentation
  - Superior performance on large objects

- **Challenges identified:**
  - Training and optimization
  - Performance on small objects
  - Need for future improvements

- **Citations:** Reference to COCO dataset
- **Special handling:**
  - Model names (DETR, Faster R-CNN) kept in English
  - Dataset name (COCO) kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.85
- **Overall section score:** 0.88
