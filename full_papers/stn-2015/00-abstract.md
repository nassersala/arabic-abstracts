# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional neural network, spatial, feature maps, differentiable, invariance, translation, scale, rotation, state-of-the-art, benchmarks

---

### English Version

Convolutional Neural Networks define an exceptionally powerful class of models, but are still limited by the lack of ability to be spatially invariant to the input data in a computationally and parameter efficient manner. In this work we introduce a new learnable module, the Spatial Transformer, which explicitly allows the spatial manipulation of data within the network. This differentiable module can be inserted into existing convolutional architectures, giving neural networks the ability to actively spatially transform feature maps, conditional on the feature map itself, without any extra training supervision or modification to the optimisation process. We show that the use of spatial transformers results in models which learn invariance to translation, scale, rotation and more generic warping, resulting in state-of-the-art performance on several benchmarks, and for a number of classes of transformations.

---

### النسخة العربية

تُعرّف الشبكات العصبية الالتفافية فئة استثنائية القوة من النماذج، لكنها لا تزال محدودة بسبب عدم القدرة على أن تكون ثابتة مكانياً تجاه بيانات الإدخال بطريقة فعالة حسابياً ومن حيث المعاملات. في هذا العمل، نقدم وحدة قابلة للتعلم جديدة، وهي المحوّل المكاني، والتي تسمح صراحةً بالمعالجة المكانية للبيانات داخل الشبكة. يمكن إدراج هذه الوحدة القابلة للاشتقاق في المعماريات الالتفافية الموجودة، مما يمنح الشبكات العصبية القدرة على تحويل خرائط الميزات مكانياً بشكل نشط، بشرط خريطة الميزات نفسها، دون أي إشراف تدريبي إضافي أو تعديل على عملية التحسين. نُظهر أن استخدام المحوّلات المكانية ينتج عنه نماذج تتعلم الثبات تجاه الإزاحة والتحجيم والدوران والالتواء الأكثر عمومية، مما يؤدي إلى أداء متقدم على عدة معايير، ولعدد من فئات التحويلات.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Spatial Transformer (المحوّل المكاني)
  - Spatial invariance (الثبات المكاني)
  - Feature maps (خرائط الميزات)
  - Differentiable module (وحدة قابلة للاشتقاق)
  - Spatial manipulation (المعالجة المكانية)

- **Equations:** 0
- **Citations:** 0
- **Special handling:**
  - "Spatially invariant" translated as "ثابتة مكانياً" (spatially stable/constant)
  - "Learnable module" translated as "وحدة قابلة للتعلم"
  - "Warping" translated as "الالتواء" (warping/distortion)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation

Convolutional Neural Networks define an exceptionally powerful class of models, but they are still limited due to the inability to be spatially stable toward input data in a computationally and parameter-efficient manner. In this work, we introduce a new learnable module, the Spatial Transformer, which explicitly allows spatial manipulation of data within the network. This differentiable module can be inserted into existing convolutional architectures, giving neural networks the ability to actively transform feature maps spatially, conditional on the feature map itself, without any additional training supervision or modification to the optimization process. We show that the use of spatial transformers results in models that learn stability toward translation, scaling, rotation, and more general warping, leading to state-of-the-art performance on several benchmarks, and for a number of transformation classes.
