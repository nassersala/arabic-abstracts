# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** neural network, feed-forward network, training, speech recognition, benchmark, overfitting, dropout, feature detector, co-adaptation, robust

---

### English Version

When a large feedforward neural network is trained on a small training set, it typically performs poorly on held-out test data. This "overfitting" is greatly reduced by randomly omitting half of the feature detectors on each training case. This prevents complex co-adaptations in which a feature detector is only helpful in the context of several other specific feature detectors. Instead, each neuron learns to detect a feature that is generally helpful for producing the correct answer given the combinatorially large variety of internal contexts in which it must operate. Random "dropout" gives big improvements on many benchmark tasks and sets new records for speech and object recognition.

---

### النسخة العربية

تتناول هذه الورقة مشكلة الإفراط في التدريب في الشبكات العصبية الأمامية الكبيرة المدربة على مجموعات بيانات صغيرة. يقدم المؤلفون تقنية "تحذف بشكل عشوائي نصف كاشفات الميزات في كل حالة تدريب" لمنع التكيف المشترك الإشكالي للميزات. يمكّن هذا النهج الخلايا العصبية الفردية من تعلم ميزات قوية فعالة عبر سياقات شبكية داخلية متنوعة. حققت هذه الطريقة، المسماة "dropout"، نتائج متقدمة على مهام معيارية متعددة في التعرف على الكلام والكائنات.

---

### Translation Notes

- **Key concept:** The paper introduces the dropout regularization technique
- **Technical accuracy:** Translation preserves the core mechanism (randomly omitting 50% of feature detectors)
- **Special handling:** The term "dropout" is kept in English as it's a standard technical term in ML

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.90
- Glossary consistency: 0.89
- **Overall section score:** 0.91
