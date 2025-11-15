# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** object detection, convolutional neural network, class imbalance, loss function, one-stage detector, two-stage detector, accuracy, training

---

### English Version

The highest accuracy object detectors to date are based on a two-stage approach popularized by R-CNN, where a classifier is applied to a sparse set of candidate object locations. In contrast, one-stage detectors that are applied over a regular, dense sampling of possible object locations have the potential to be faster and simpler, but have trailed the accuracy of two-stage detectors thus far. In this paper, we investigate why this is the case. We discover that the extreme foreground-background class imbalance encountered during training of dense detectors is the central cause. We propose to address this class imbalance by reshaping the standard cross entropy loss such that it down-weights the loss assigned to well-classified examples. Our novel Focal Loss focuses training on a sparse set of hard examples and prevents the vast number of easy negatives from overwhelming the detector during training. To evaluate the effectiveness of our loss, we design and train a simple dense detector we call RetinaNet. Our results show that when trained with the focal loss, RetinaNet is able to match the speed of previous one-stage detectors while surpassing the accuracy of all existing state-of-the-art two-stage detectors. Code is at: https://github.com/facebookresearch/Detectron.

---

### النسخة العربية

تعتمد أدق كواشف الأجسام حتى الآن على نهج من مرحلتين شاع استخدامه بواسطة R-CNN، حيث يُطبق مصنف على مجموعة متناثرة من مواقع الأجسام المرشحة. في المقابل، الكواشف أحادية المرحلة التي تُطبق على عينات منتظمة وكثيفة من مواقع الأجسام المحتملة لديها القدرة على أن تكون أسرع وأبسط، لكنها تخلفت عن دقة الكواشف ثنائية المرحلة حتى الآن. في هذا البحث، نستقصي سبب ذلك. نكتشف أن عدم التوازن الشديد بين فئة المقدمة والخلفية الذي يُواجه أثناء تدريب الكواشف الكثيفة هو السبب الرئيسي. نقترح معالجة عدم التوازن هذا بين الفئات من خلال إعادة تشكيل دالة الخسارة القياسية للإنتروبيا المتقاطعة بحيث تُقلل من وزن الخسارة المخصصة للأمثلة المصنفة بشكل جيد. تُركز الخسارة المُركزة (Focal Loss) الجديدة التي نقدمها عملية التدريب على مجموعة متناثرة من الأمثلة الصعبة وتمنع العدد الهائل من الأمثلة السلبية السهلة من إغراق الكاشف أثناء التدريب. لتقييم فعالية دالة الخسارة الخاصة بنا، نصمم ونُدرب كاشفاً كثيفاً بسيطاً نسميه RetinaNet. تُظهر نتائجنا أنه عند تدريبه باستخدام الخسارة المُركزة، يستطيع RetinaNet مطابقة سرعة الكواشف أحادية المرحلة السابقة مع تجاوز دقة جميع الكواشف ثنائية المرحلة الحديثة المتقدمة الموجودة. الشفرة البرمجية متاحة على: https://github.com/facebookresearch/Detectron.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Focal Loss (الخسارة المُركزة)
  - Dense detector (كاشف كثيف)
  - One-stage detector (كاشف أحادي المرحلة)
  - Two-stage detector (كاشف ثنائي المرحلة)
  - Class imbalance (عدم التوازن بين الفئات)
  - Hard examples (أمثلة صعبة)
  - Easy negatives (أمثلة سلبية سهلة)

- **Equations:** None
- **Citations:** R-CNN mentioned, code repository link
- **Special handling:**
  - "RetinaNet" kept in English as it's a proper name
  - GitHub URL preserved as-is
  - "Focal Loss" translated as الخسارة المُركزة (literally: focused/concentrated loss)

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score: 0.91**

### Back-translation Check

Key phrases back-translated from Arabic:
- "الخسارة المُركزة" → "Focused/Concentrated Loss" ✓ (captures the essence of Focal Loss)
- "عدم التوازن بين الفئات" → "Class imbalance" ✓
- "كاشف كثيف" → "Dense detector" ✓
- "أمثلة صعبة" → "Hard examples" ✓
