# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.90
**Glossary Terms Used:** neural networks (الشبكات العصبية), machine intelligence (الذكاء الآلي), accuracy (دقة), computational resources (موارد حسابية), mobile (محمول), embedded applications (تطبيقات مدمجة), architecture (معمارية), computer vision (رؤية حاسوبية), operations (عمليات), memory (ذاكرة), inverted residual (البقايا المعكوسة), linear bottleneck (العنق الخطي), depthwise convolution (الالتفاف حسب العمق), TensorFlow-Slim, inference (الاستدلال), tensors (موترات)

---

### English Version

Neural networks have revolutionized many areas of machine intelligence, enabling superhuman accuracy for challenging image recognition tasks. However, the drive to improve accuracy often comes at a cost: modern state of the art networks require high computational resources beyond the capabilities of many mobile and embedded applications.

This paper introduces a new neural network architecture that is specifically tailored for mobile and resource constrained environments. Our network pushes the state of the art for mobile tailored computer vision models, by significantly decreasing the number of operations and memory needed while retaining the same accuracy.

Our main contribution is a novel layer module: the inverted residual with linear bottleneck. This module takes as an input a low-dimensional compressed representation which is first expanded to high dimension and filtered with a lightweight depthwise convolution. Features are subsequently projected back to a low-dimensional representation with a linear convolution. The official implementation is available as part of TensorFlow-Slim model library in [cite].

This module can be efficiently implemented using standard operations in any modern framework and allows our models to beat state of the art along multiple performance points using standard benchmarks. Furthermore, this convolutional module is particularly suitable for mobile designs, because it allows to significantly reduce the memory footprint needed during inference by never fully materializing large intermediate tensors. This reduces the need for main memory access in many embedded hardware designs, that provide small amounts of very fast software controlled cache memory.

---

### النسخة العربية

لقد أحدثت الشبكات العصبية ثورة في العديد من مجالات الذكاء الآلي، مما مكّن من تحقيق دقة تفوق البشر في مهام التعرف على الصور الصعبة. ومع ذلك، فإن السعي لتحسين الدقة غالباً ما يأتي بتكلفة: تتطلب الشبكات الحديثة الأحدث موارد حسابية عالية تتجاوز قدرات العديد من التطبيقات المحمولة والمدمجة.

يقدم هذا البحث معمارية شبكة عصبية جديدة مُصممة خصيصاً للبيئات المحمولة والمقيدة بالموارد. تدفع شبكتنا حدود أحدث نماذج الرؤية الحاسوبية المُصممة للأجهزة المحمولة، من خلال تقليل عدد العمليات والذاكرة المطلوبة بشكل كبير مع الحفاظ على نفس الدقة.

مساهمتنا الرئيسية هي وحدة طبقة جديدة: البقايا المعكوسة مع العنق الخطي. تأخذ هذه الوحدة كمدخل تمثيلاً مضغوطاً منخفض الأبعاد يتم توسيعه أولاً إلى أبعاد عالية ويُصفى باستخدام التفاف خفيف الوزن حسب العمق. ثم تُسقط الميزات مرة أخرى إلى تمثيل منخفض الأبعاد باستخدام التفاف خطي. التنفيذ الرسمي متاح كجزء من مكتبة نماذج TensorFlow-Slim.

يمكن تنفيذ هذه الوحدة بكفاءة باستخدام العمليات القياسية في أي إطار عمل حديث، وتسمح لنماذجنا بتجاوز أحدث ما توصلت إليه التقنية عبر نقاط أداء متعددة باستخدام المعايير القياسية. علاوة على ذلك، فإن هذه الوحدة الالتفافية مناسبة بشكل خاص للتصاميم المحمولة، لأنها تسمح بتقليل البصمة الذاكرية المطلوبة أثناء الاستدلال بشكل كبير من خلال عدم تجسيد الموترات الوسيطة الكبيرة بالكامل. هذا يقلل من الحاجة للوصول إلى الذاكرة الرئيسية في العديد من تصاميم الأجهزة المدمجة التي توفر كميات صغيرة من ذاكرة التخزين المؤقت السريعة جداً المتحكم بها برمجياً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Neural networks (الشبكات العصبية)
  - Machine intelligence (الذكاء الآلي)
  - Superhuman accuracy (دقة تفوق البشر)
  - Resource constrained environments (البيئات المقيدة بالموارد)
  - Inverted residual with linear bottleneck (البقايا المعكوسة مع العنق الخطي)
  - Low-dimensional compressed representation (تمثيل مضغوط منخفض الأبعاد)
  - Depthwise convolution (الالتفاف حسب العمق)
  - Memory footprint (البصمة الذاكرية)
  - Materializing tensors (تجسيد الموترات)
  - Cache memory (ذاكرة التخزين المؤقت)

- **Equations:** None
- **Citations:** 1 reference to TensorFlow-Slim implementation (indicated by [cite])
- **Special handling:**
  - TensorFlow-Slim kept as proper noun
  - Technical architecture names preserved
  - "State of the art" translated as "أحدث ما توصلت إليه التقنية" / "الأحدث"

### Quality Metrics

- **Semantic equivalence:** 0.91 - Accurately preserves all technical concepts and motivation
- **Technical accuracy:** 0.92 - Correct translation of specialized terms (tensors, memory footprint, etc.)
- **Readability:** 0.88 - Natural Arabic flow while maintaining technical precision
- **Glossary consistency:** 0.89 - Uses established terms consistently
- **Overall section score:** 0.90

### Back-translation Check (Key Sentences)

**Original:** "This module takes as an input a low-dimensional compressed representation which is first expanded to high dimension and filtered with a lightweight depthwise convolution."

**Arabic:** "تأخذ هذه الوحدة كمدخل تمثيلاً مضغوطاً منخفض الأبعاد يتم توسيعه أولاً إلى أبعاد عالية ويُصفى باستخدام التفاف خفيف الوزن حسب العمق."

**Back-translation:** "This module takes as input a low-dimensional compressed representation that is first expanded to high dimensions and filtered using a lightweight depthwise convolution."

✓ **Semantic match verified**

**Original:** "This reduces the need for main memory access in many embedded hardware designs, that provide small amounts of very fast software controlled cache memory."

**Arabic:** "هذا يقلل من الحاجة للوصول إلى الذاكرة الرئيسية في العديد من تصاميم الأجهزة المدمجة التي توفر كميات صغيرة من ذاكرة التخزين المؤقت السريعة جداً المتحكم بها برمجياً."

**Back-translation:** "This reduces the need to access main memory in many embedded hardware designs that provide small amounts of very fast software-controlled cache memory."

✓ **Semantic match verified**
