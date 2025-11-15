# Section 7: Conclusions and Future Work
## القسم 7: الاستنتاجات والعمل المستقبلي

**Section:** conclusions
**Translation Quality:** 0.90
**Glossary Terms Used:** network architecture (معمارية الشبكة), efficient (كفء/فعال), mobile models (نماذج محمولة), memory-efficient (كفء في استخدام الذاكرة), inference (الاستدلال), neural frameworks (أطر عمل عصبية), ImageNet dataset (مجموعة بيانات ImageNet), performance points (نقاط الأداء), object detection (كشف الأجسام), COCO dataset, accuracy (دقة), model complexity (تعقيد النموذج), SSDLite, YOLOv2, convolutional block (كتلة التفافية), expressiveness (التعبيرية), capacity (السعة), expansion layers (طبقات التوسيع), bottleneck inputs (مدخلات العنق)

---

### English Version

We described a very simple network architecture that allowed us to build a family of highly efficient mobile models. Our basic building unit, has several properties that make it particularly suitable for mobile applications. It allows very memory-efficient inference and relies utilize standard operations present in all neural frameworks.

For the ImageNet dataset, our architecture improves the state of the art for wide range of performance points.

For object detection task, our network outperforms state-of-art realtime detectors on COCO dataset both in terms of accuracy and model complexity. Notably, our architecture combined with the SSDLite detection module is 20× less computation and 10× less parameters than YOLOv2.

On the theoretical side: the proposed convolutional block has a unique property that allows to separate the network expressiveness (encoded by expansion layers) from its capacity (encoded by bottleneck inputs). Exploring this is an important direction for future research.

**Acknowledgments**: We would like to thank Matt Streeter and Sergey Ioffe for their helpful feedback and discussion.

---

### النسخة العربية

وصفنا معمارية شبكة بسيطة جداً سمحت لنا ببناء عائلة من النماذج المحمولة عالية الكفاءة. وحدة البناء الأساسية لدينا، لها عدة خصائص تجعلها مناسبة بشكل خاص للتطبيقات المحمولة. فهي تسمح باستدلال كفء جداً في استخدام الذاكرة وتعتمد على استخدام العمليات القياسية الموجودة في جميع الأطر العصبية.

بالنسبة لمجموعة بيانات ImageNet، تُحسّن معماريتنا أحدث ما توصلت إليه التقنية لمجموعة واسعة من نقاط الأداء.

بالنسبة لمهمة كشف الأجسام، تتفوق شبكتنا على كواشف الوقت الفعلي الأحدث على مجموعة بيانات COCO من حيث الدقة وتعقيد النموذج. والجدير بالذكر أن معماريتنا مقترنة بوحدة الكشف SSDLite أقل حساباً بـ 20 مرة وأقل معاملات بـ 10 مرات من YOLOv2.

من الناحية النظرية: الكتلة الالتفافية المقترحة لها خاصية فريدة تسمح بفصل تعبيرية الشبكة (المشفرة بواسطة طبقات التوسيع) عن سعتها (المشفرة بواسطة مدخلات العنق). استكشاف هذا هو اتجاه مهم للبحث المستقبلي.

**شكر وتقدير**: نود أن نشكر Matt Streeter وSergey Ioffe على ملاحظاتهم ونقاشاتهم المفيدة.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** None
- **Key terms introduced:**
  - Network architecture (معمارية الشبكة)
  - Family of models (عائلة من النماذج)
  - Highly efficient (عالية الكفاءة)
  - Basic building unit (وحدة البناء الأساسية)
  - Memory-efficient inference (استدلال كفء في استخدام الذاكرة)
  - Standard operations (العمليات القياسية)
  - Neural frameworks (الأطر العصبية)
  - State of the art (أحدث ما توصلت إليه التقنية)
  - Performance points (نقاط الأداء)
  - Realtime detectors (كواشف الوقت الفعلي)
  - Model complexity (تعقيد النموذج)
  - Detection module (وحدة الكشف)
  - Convolutional block (كتلة التفافية)
  - Network expressiveness (تعبيرية الشبكة)
  - Network capacity (سعة الشبكة)
  - Expansion layers (طبقات التوسيع)
  - Bottleneck inputs (مدخلات العنق)
  - Future research (البحث المستقبلي)

- **Equations:** None
- **Citations:** References to ImageNet, COCO datasets, SSDLite, YOLOv2
- **Special handling:**
  - Dataset names kept as proper nouns
  - Model names (SSDLite, YOLOv2) kept as proper nouns
  - Author names in acknowledgments kept in English
  - "State of the art" translated as "أحدث ما توصلت إليه التقنية"
  - Numerical comparisons (20×, 10×) preserved

### Quality Metrics

- **Semantic equivalence:** 0.91 - Accurately summarizes key contributions and results
- **Technical accuracy:** 0.92 - Correct translation of architectural concepts and achievements
- **Readability:** 0.89 - Clear and concise conclusion in formal Arabic
- **Glossary consistency:** 0.89 - Uses established terms consistently throughout
- **Overall section score:** 0.90

### Back-translation Check (Key Sentences)

**Original:** "We described a very simple network architecture that allowed us to build a family of highly efficient mobile models. Our basic building unit, has several properties that make it particularly suitable for mobile applications."

**Arabic:** "وصفنا معمارية شبكة بسيطة جداً سمحت لنا ببناء عائلة من النماذج المحمولة عالية الكفاءة. وحدة البناء الأساسية لدينا، لها عدة خصائص تجعلها مناسبة بشكل خاص للتطبيقات المحمولة."

**Back-translation:** "We described a very simple network architecture that allowed us to build a family of highly efficient mobile models. Our basic building unit has several properties that make it particularly suitable for mobile applications."

✓ **Semantic match verified**

**Original:** "On the theoretical side: the proposed convolutional block has a unique property that allows to separate the network expressiveness (encoded by expansion layers) from its capacity (encoded by bottleneck inputs). Exploring this is an important direction for future research."

**Arabic:** "من الناحية النظرية: الكتلة الالتفافية المقترحة لها خاصية فريدة تسمح بفصل تعبيرية الشبكة (المشفرة بواسطة طبقات التوسيع) عن سعتها (المشفرة بواسطة مدخلات العنق). استكشاف هذا هو اتجاه مهم للبحث المستقبلي."

**Back-translation:** "On the theoretical side: the proposed convolutional block has a unique property that allows separating the network's expressiveness (encoded by expansion layers) from its capacity (encoded by bottleneck inputs). Exploring this is an important direction for future research."

✓ **Semantic match verified**
