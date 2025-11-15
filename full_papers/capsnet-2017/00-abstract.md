# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** capsule, neural network, vector, entity, layer, transformation matrix, convolutional network, discriminative, MNIST

---

### English Version

A capsule is a group of neurons whose activity vector represents the instantiation parameters of a specific type of entity such as an object or an object part. We use the length of the activity vector to represent the probability that the entity exists and its orientation to represent the instantiation parameters. Active capsules at one level make predictions, via transformation matrices, for the instantiation parameters of higher-level capsules. When multiple predictions agree, a higher level capsule becomes active. We show that a discriminatively trained, multi-layer capsule system achieves state-of-the-art performance on MNIST and is considerably better than a convolutional net at recognizing highly overlapping digits.

---

### النسخة العربية

الكبسولة (Capsule) هي مجموعة من العصبونات يمثل متجه نشاطها معاملات التجسيد (instantiation parameters) لنوع محدد من الكيان مثل جسم أو جزء من جسم. نستخدم طول متجه النشاط لتمثيل احتمالية وجود الكيان، ونستخدم اتجاهه لتمثيل معاملات التجسيد. تقوم الكبسولات النشطة في مستوى معين بعمل تنبؤات، عبر مصفوفات التحويل، لمعاملات التجسيد الخاصة بالكبسولات ذات المستوى الأعلى. عندما تتفق تنبؤات متعددة، تصبح كبسولة المستوى الأعلى نشطة. نُظهر أن نظام الكبسولات متعدد الطبقات المدرب بشكل تمييزي يحقق أداءً متقدماً على مجموعة بيانات MNIST ويتفوق بشكل ملحوظ على الشبكة الالتفافية في التعرف على الأرقام المتداخلة بشكل كبير.

---

### Back-Translation (Validation)

A capsule is a group of neurons whose activity vector represents the instantiation parameters of a specific type of entity such as an object or part of an object. We use the length of the activity vector to represent the probability of the entity's existence, and we use its direction to represent the instantiation parameters. Active capsules at a certain level make predictions, via transformation matrices, for the instantiation parameters of higher-level capsules. When multiple predictions agree, the higher-level capsule becomes active. We show that a multi-layer capsule system trained discriminatively achieves state-of-the-art performance on the MNIST dataset and significantly outperforms the convolutional network in recognizing highly overlapping digits.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - capsule (كبسولة) - NEW term, core concept of the paper
  - instantiation parameters (معاملات التجسيد) - NEW term, represents entity properties
  - activity vector (متجه النشاط) - represents capsule output
  - routing-by-agreement (implied in "multiple predictions agree")

- **Equations:** None in abstract
- **Citations:** References MNIST dataset
- **Special handling:**
  - Kept "Capsule" in both English and Arabic initially to introduce the term
  - "instantiation parameters" translated as معاملات التجسيد (parameters of embodiment/materialization)
  - Maintained technical precision while ensuring natural flow in Arabic

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.89
- Glossary consistency: 0.90
- **Overall section score:** 0.91

### Semantic Analysis

The translation accurately captures:
1. The definition of a capsule as a group of neurons
2. The dual representation: vector length = probability, orientation = parameters
3. The hierarchical prediction mechanism through transformation matrices
4. The routing-by-agreement concept (when predictions agree)
5. The performance claims on MNIST and superiority over CNNs for overlapping digits

The back-translation confirms semantic preservation with only minor stylistic variations.
