# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** mobile architecture (معمارية المحمول), inverted residual (البقايا المعكوسة), bottleneck layers (طبقات العنق), depthwise convolution (الالتفاف حسب العمق), representational power (القدرة التمثيلية), ImageNet, COCO, VOC, multiply-adds (عمليات الضرب والجمع), parameters (معاملات)

---

### English Version

In this paper we describe a new mobile architecture, MobileNetV2, that improves the state of the art performance of mobile models on multiple tasks and benchmarks as well as across a spectrum of different model sizes. We also describe efficient ways of applying these mobile models to object detection in a novel framework we call SSDLite. Additionally, we demonstrate how to build mobile semantic segmentation models through a reduced form of DeepLabv3 which we call Mobile DeepLabv3.

The architecture is based on an inverted residual structure where the shortcut connections are between the thin bottleneck layers. The intermediate expansion layer uses lightweight depthwise convolutions to filter features as a source of non-linearity. Additionally, we find that it is important to remove non-linearities in the narrow layers in order to maintain representational power. We demonstrate that this improves performance and provide an intuition that led to this design.

Finally, our approach allows decoupling of the input/output domains from the expressiveness of the transformation, which provides a convenient framework for further analysis. We measure our performance on ImageNet classification, COCO object detection, VOC image segmentation. We evaluate the trade-offs between accuracy, and number of operations measured by multiply-adds (MAdd), as well as actual latency, and the number of parameters.

---

### النسخة العربية

في هذا البحث نصف معمارية محمول جديدة، MobileNetV2، تُحسّن أداء أحدث النماذج المحمولة في مهام ومعايير متعددة بالإضافة إلى طيف من أحجام النماذج المختلفة. كما نصف طرقاً فعالة لتطبيق هذه النماذج المحمولة على كشف الأجسام في إطار عمل جديد نسميه SSDLite. بالإضافة إلى ذلك، نوضح كيفية بناء نماذج تجزئة دلالية محمولة من خلال نسخة مُختزلة من DeepLabv3 نسميها Mobile DeepLabv3.

تعتمد المعمارية على بنية بقايا معكوسة حيث تكون اتصالات الاختصار بين طبقات العنق الرقيقة. تستخدم طبقة التوسيع الوسيطة التفافات خفيفة الوزن حسب العمق لتصفية الميزات كمصدر لللاخطية. بالإضافة إلى ذلك، نجد أنه من المهم إزالة اللاخطيات في الطبقات الضيقة للحفاظ على القدرة التمثيلية. نُثبت أن هذا يُحسّن الأداء ونقدم الحدس الذي أدى إلى هذا التصميم.

أخيراً، يسمح نهجنا بفصل مجالات الإدخال/الإخراج عن التعبيرية للتحويل، مما يوفر إطار عمل ملائم لمزيد من التحليل. نقيس أداءنا على تصنيف ImageNet، وكشف الأجسام في COCO، وتجزئة الصور في VOC. نُقيّم المقايضات بين الدقة وعدد العمليات المقاسة بعمليات الضرب والجمع (MAdd)، بالإضافة إلى زمن الاستجابة الفعلي وعدد المعاملات.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - MobileNetV2 (kept as is - proper noun)
  - Inverted residual structure (بنية بقايا معكوسة)
  - Bottleneck layers (طبقات العنق)
  - Depthwise convolutions (التفافات حسب العمق)
  - SSDLite (kept as is - proper noun)
  - Mobile DeepLabv3 (kept as is - proper noun)
  - Shortcut connections (اتصالات الاختصار)
  - Expansion layer (طبقة التوسيع)
  - Representational power (القدرة التمثيلية)
  - Multiply-adds/MAdd (عمليات الضرب والجمع)

- **Equations:** None
- **Citations:** ImageNet, COCO, VOC datasets (kept as proper nouns)
- **Special handling:**
  - Model/architecture names preserved in English
  - Dataset names preserved as proper nouns
  - Technical metrics (MAdd, latency, parameters) translated with parenthetical English

### Quality Metrics

- **Semantic equivalence:** 0.92 - Accurately captures all key concepts and innovations
- **Technical accuracy:** 0.93 - Correct translation of all technical terms using established glossary
- **Readability:** 0.89 - Natural flow in Arabic while maintaining technical precision
- **Glossary consistency:** 0.90 - Uses consistent terminology from glossary, establishes new terms appropriately
- **Overall section score:** 0.91

### Back-translation Check (Key Sentences)

**Original:** "The architecture is based on an inverted residual structure where the shortcut connections are between the thin bottleneck layers."

**Arabic:** "تعتمد المعمارية على بنية بقايا معكوسة حيث تكون اتصالات الاختصار بين طبقات العنق الرقيقة."

**Back-translation:** "The architecture relies on an inverted residual structure where the shortcut connections are between the thin bottleneck layers."

✓ **Semantic match verified**
