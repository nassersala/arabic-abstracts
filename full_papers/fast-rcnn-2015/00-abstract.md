# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** object detection (كشف الأجسام), convolutional network (شبكة التفافية), training (التدريب), accuracy (دقة), bounding box (صندوق التحديد)

---

### English Version

This paper proposes a Fast Region-based Convolutional Network method (Fast R-CNN) for object detection. Fast R-CNN builds on previous work to efficiently classify object proposals using deep convolutional networks. Compared to previous work, Fast R-CNN employs several innovations to improve training and testing speed while also increasing detection accuracy. Fast R-CNN trains the very deep VGG16 network 9× faster than R-CNN, is 213× faster at test-time, and achieves a higher mAP on PASCAL VOC 2012. Compared to SPPnet, Fast R-CNN trains VGG16 3× faster, tests 10× faster, and is more accurate. Fast R-CNN is implemented in Python and C++ (using Caffe) and is available under the open-source MIT License at https://github.com/rbgirshick/fast-rcnn.

---

### النسخة العربية

تقترح هذه الورقة طريقة Fast R-CNN (شبكة التفافية قائمة على المناطق السريعة) لكشف الأجسام. تبني Fast R-CNN على الأعمال السابقة لتصنيف مقترحات الأجسام بكفاءة باستخدام الشبكات العصبية الالتفافية العميقة. وبالمقارنة مع الأعمال السابقة، تستخدم Fast R-CNN عدة ابتكارات لتحسين سرعة التدريب والاختبار مع زيادة دقة الكشف أيضاً. تقوم Fast R-CNN بتدريب شبكة VGG16 العميقة جداً بسرعة أكبر 9 مرات من R-CNN، وهي أسرع بـ 213 مرة في وقت الاختبار، وتحقق mAP أعلى على مجموعة بيانات PASCAL VOC 2012. وبالمقارنة مع SPPnet، تقوم Fast R-CNN بتدريب VGG16 بسرعة أكبر 3 مرات، والاختبار بسرعة أكبر 10 مرات، وتكون أكثر دقة. تم تنفيذ Fast R-CNN بلغتي Python و C++ (باستخدام Caffe) وهي متاحة تحت ترخيص MIT مفتوح المصدر على https://github.com/rbgirshick/fast-rcnn.

---

### Translation Notes

- **Key terms introduced:**
  - Fast R-CNN: شبكة التفافية قائمة على المناطق السريعة
  - object proposals: مقترحات الأجسام
  - deep convolutional networks: الشبكات العصبية الالتفافية العميقة
  - mAP (mean Average Precision): متوسط الدقة المتوسطة (kept as mAP)
  - PASCAL VOC: مجموعة بيانات PASCAL VOC
  - VGG16: شبكة VGG16
  - test-time: وقت الاختبار

- **Special handling:**
  - Kept technical acronyms (R-CNN, Fast R-CNN, SPPnet, VGG16, mAP) in English as they are standard in the field
  - Preserved numerical comparisons (9×, 213×, 3×, 10×) exactly
  - Kept framework name "Caffe" and "MIT License" in English
  - Preserved GitHub URL as-is

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.95
- Readability: 0.88
- Glossary consistency: 0.95
- **Overall section score:** 0.90

### Back-translation Verification

Key sentence back-translated:
Arabic: "تقوم Fast R-CNN بتدريب شبكة VGG16 العميقة جداً بسرعة أكبر 9 مرات من R-CNN"
Back to English: "Fast R-CNN trains the very deep VGG16 network 9 times faster than R-CNN"
✓ Matches original semantics accurately
