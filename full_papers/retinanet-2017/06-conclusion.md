# Section 6: Conclusion
## القسم 6: الخلاصة

**Section:** Conclusion
**Translation Quality:** 0.92
**Glossary Terms Used:** object detection, loss function, class imbalance, one-stage detector, accuracy, training

---

### English Version

In this work we identify class imbalance as the primary obstacle preventing one-stage object detectors from surpassing top-performing, two-stage methods. To address this, we propose the focal loss which applies a modulating term to the cross entropy loss in order to focus learning on hard negative examples. Our approach is simple and highly effective. We demonstrate its efficacy by designing a fully convolutional one-stage detector and report extensive experimental analysis showing that our detector achieves state-of-the-art accuracy and speed. Source code is made available at https://github.com/facebookresearch/Detectron (in Caffe2) and https://github.com/facebookresearch/detectron2 (in PyTorch).

---

### النسخة العربية

في هذا العمل، نحدد عدم التوازن بين الفئات كالعائق الرئيسي الذي يمنع الكواشف أحادية المرحلة من تجاوز الطرق ثنائية المرحلة عالية الأداء. لمعالجة ذلك، نقترح الخسارة المُركزة التي تطبق حد تعديل على خسارة الإنتروبيا المتقاطعة من أجل تركيز التعلم على الأمثلة السلبية الصعبة. نهجنا بسيط وفعال للغاية. نُثبت فعاليته من خلال تصميم كاشف التفافي كامل أحادي المرحلة ونُبلغ عن تحليل تجريبي واسع النطاق يُظهر أن كاشفنا يحقق دقة وسرعة حديثة متقدمة. الشفرة المصدرية متاحة على https://github.com/facebookresearch/Detectron (في Caffe2) و https://github.com/facebookresearch/detectron2 (في PyTorch).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Fully convolutional (التفافي كامل)
  - Source code (الشفرة المصدرية)
  - Extensive experimental analysis (تحليل تجريبي واسع النطاق)

- **Equations:** None
- **Citations:** GitHub repositories for Detectron (Caffe2) and Detectron2 (PyTorch)
- **Special handling:**
  - GitHub URLs preserved as-is
  - Framework names preserved: Caffe2, PyTorch
  - Detectron/Detectron2 names preserved
  - Concise conclusion section maintaining the key contributions

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.93
- Readability: 0.92
- Glossary consistency: 0.90
- **Overall section score: 0.92**

### Back-translation Check

Key phrases:
- "العائق الرئيسي" → "Primary obstacle" ✓
- "حد تعديل" → "Modulating term" ✓
- "الأمثلة السلبية الصعبة" → "Hard negative examples" ✓
- "التفافي كامل" → "Fully convolutional" ✓
- "تحليل تجريبي واسع النطاق" → "Extensive experimental analysis" ✓
- "حديثة متقدمة" → "State-of-the-art" ✓
