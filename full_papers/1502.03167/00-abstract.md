# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** deep neural networks, training, layer, parameters, learning rates, initialization, normalization, model architecture, mini-batch, regularizer, dropout, image classification, accuracy, validation

---

### English Version

Training Deep Neural Networks is complicated by the fact that the distribution of each layer's inputs changes during training, as the parameters of the previous layers change. This slows down the training by requiring lower learning rates and careful parameter initialization, and makes it notoriously hard to train models with saturating nonlinearities. We refer to this phenomenon as internal covariate shift, and address the problem by normalizing layer inputs. Our method draws its strength from making normalization a part of the model architecture and performing the normalization for each training mini-batch. Batch Normalization allows us to use much higher learning rates and be less careful about initialization. It also acts as a regularizer, in some cases eliminating the need for Dropout. Applied to a state-of-the-art image classification model, Batch Normalization achieves the same accuracy with 14 times fewer training steps, and beats the original model by a significant margin. Using an ensemble of batch-normalized networks, we improve upon the best published result on ImageNet classification: reaching 4.9% top-5 validation error (and 4.8% test error), exceeding the accuracy of human raters.

---

### النسخة العربية

يتعقد تدريب الشبكات العصبية العميقة بسبب أن توزيع مدخلات كل طبقة يتغير أثناء التدريب، مع تغير معاملات الطبقات السابقة. يؤدي هذا إلى إبطاء التدريب من خلال تطلب معدلات تعلم أقل وتهيئة دقيقة للمعاملات، ويجعل تدريب النماذج ذات اللاخطيات المشبعة صعباً بشكل معروف. نشير إلى هذه الظاهرة باسم التحول التباين الداخلي (Internal Covariate Shift)، ونعالج المشكلة من خلال تطبيع مدخلات الطبقة. تستمد طريقتنا قوتها من جعل التطبيع جزءاً من معمارية النموذج وتنفيذ التطبيع لكل حزمة تدريب صغيرة (Mini-batch). يتيح لنا تطبيع الحزمة استخدام معدلات تعلم أعلى بكثير وأن نكون أقل حرصاً بشأن التهيئة. كما يعمل كمنظم (Regularizer)، وفي بعض الحالات يلغي الحاجة إلى الإسقاط (Dropout). عند تطبيقه على نموذج متقدم لتصنيف الصور، يحقق تطبيع الحزمة نفس الدقة بعدد خطوات تدريب أقل 14 مرة، ويتفوق على النموذج الأصلي بهامش كبير. باستخدام مجموعة من الشبكات المطبعة بالحزمة، نحسّن أفضل نتيجة منشورة في تصنيف ImageNet: لنصل إلى خطأ تحقق 4.9% في أفضل 5 نتائج (Top-5) وخطأ اختبار 4.8%، متجاوزين دقة المقيّمين البشريين.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Internal Covariate Shift (التحول التباين الداخلي)
  - Batch Normalization (تطبيع الحزمة)
  - Mini-batch (حزمة تدريب صغيرة)
  - Saturating nonlinearities (اللاخطيات المشبعة)
- **Equations:** None in abstract
- **Citations:** None in abstract
- **Special handling:** Technical terms retained in English parenthetically for clarity

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.89
- Glossary consistency: 0.90
- **Overall section score:** 0.90
