# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network, convolutional, capsule, parse tree, vector, entity, feature detector, instantiation parameters, pooling

---

### English Version

Human vision ignores irrelevant details by using a carefully determined sequence of fixation points to ensure that only a tiny fraction of the optic array is ever processed at the highest resolution. Introspection is a poor guide to understanding how these fixation points are selected, but it seems plausible that the sequence is determined by a sequential attention mechanism that uses a high-level interpretation of the scene to decide where to look next. This paper makes the much weaker assumption that a single fixation gives us much more than just a single identified object and its properties. We assume that our multi-layer visual system creates a parse tree-like structure on each fixation, and we ignore the issue of how successive fixations are co-ordinated. This tree structure may not be consciously accessible, but we believe it is there.

A parse tree is generally constructed on the fly by dynamically allocating memory. Computer vision, by contrast, has a much more straightforward way to carve a parse tree out of a fixed multilayer neural network. At every position in the image there is at most one node of each type in the parse tree. So if we replicate a capsule at every position in the image, it is possible to allocate a small group of neurons for every possible node in the parse tree and to use the intensity of the activity vector to determine whether that node is present or not. This is much more efficient than dynamically allocating neurons.

A capsule is a group of neurons whose activity vector represents the instantiation parameters of a specific type of entity such as an object or an object part. We use the length of the activity vector to represent the probability that the entity exists and its orientation to represent the instantiation parameters. Active capsules at one level make predictions, via transformation matrices, for the instantiation parameters of higher-level capsules. When multiple predictions agree, a higher level capsule becomes active. We show that a discriminatively trained, multi-layer capsule system achieves state-of-the-art performance on MNIST and is considerably better than a convolutional net at recognizing highly overlapping digits. To achieve these results, we use an iterative routing-by-agreement mechanism: A lower-level capsule prefers to send its output to higher level capsules whose activity vectors have a big scalar product with the prediction coming from the lower-level capsule.

The fact that the output of a capsule is a vector makes it possible to use a powerful dynamic routing mechanism to ensure that the output of the capsule gets sent to an appropriate parent in the layer above. Initially, the output is routed to all possible parents but is scaled down by coupling coefficients that sum to 1. For each possible parent, the capsule computes a "prediction vector" by multiplying its own output by a weight matrix. If this prediction vector has a large scalar product with the output of a possible parent, there is top-down feedback which has the effect of increasing the coupling coefficient for that parent and decreasing it for other parents. This increases the contribution that the capsule makes to that parent thus further increasing the scalar product of the capsule's prediction with the parent's output. This type of "routing-by-agreement" should be far more effective than the very primitive form of routing implemented by max-pooling, which allows neurons in one layer to ignore all but the most active feature detector in a local pool in the layer below.

---

### النسخة العربية

تتجاهل الرؤية البشرية التفاصيل غير ذات الصلة باستخدام تسلسل محدد بعناية من نقاط التثبيت (fixation points) لضمان معالجة جزء صغير فقط من المصفوفة البصرية بأعلى دقة. لا يُعد التأمل الذاتي دليلاً جيداً لفهم كيفية اختيار نقاط التثبيت هذه، لكن يبدو من المعقول أن التسلسل يتم تحديده بواسطة آلية انتباه تسلسلية تستخدم تفسيراً عالي المستوى للمشهد لتحديد المكان الذي يجب النظر إليه تالياً. يفترض هذا البحث افتراضاً أضعف بكثير وهو أن التثبيت الواحد يعطينا أكثر بكثير من مجرد جسم واحد محدد وخصائصه. نفترض أن نظامنا البصري متعدد الطبقات ينشئ بنية شبيهة بشجرة التحليل اللغوي (parse tree) في كل تثبيت، ونتجاهل مسألة كيفية تنسيق التثبيتات المتتالية. قد لا تكون بنية الشجرة هذه متاحة بشكل واعٍ، لكننا نعتقد أنها موجودة.

عادةً ما يتم بناء شجرة التحليل اللغوي بشكل فوري عن طريق تخصيص الذاكرة ديناميكياً. على النقيض من ذلك، تمتلك رؤية الحاسوب طريقة أكثر بساطة لنحت شجرة تحليل لغوي من شبكة عصبية ثابتة متعددة الطبقات. في كل موضع في الصورة، يوجد على الأكثر عقدة واحدة من كل نوع في شجرة التحليل اللغوي. لذا إذا قمنا بتكرار كبسولة في كل موضع في الصورة، يصبح من الممكن تخصيص مجموعة صغيرة من العصبونات لكل عقدة محتملة في شجرة التحليل اللغوي واستخدام شدة متجه النشاط لتحديد ما إذا كانت تلك العقدة موجودة أم لا. هذا أكثر كفاءة بكثير من تخصيص العصبونات ديناميكياً.

الكبسولة هي مجموعة من العصبونات يمثل متجه نشاطها معاملات التجسيد لنوع محدد من الكيان مثل جسم أو جزء من جسم. نستخدم طول متجه النشاط لتمثيل احتمالية وجود الكيان، ونستخدم اتجاهه لتمثيل معاملات التجسيد. تقوم الكبسولات النشطة في مستوى معين بعمل تنبؤات، عبر مصفوفات التحويل، لمعاملات التجسيد الخاصة بالكبسولات ذات المستوى الأعلى. عندما تتفق تنبؤات متعددة، تصبح كبسولة المستوى الأعلى نشطة. نُظهر أن نظام الكبسولات متعدد الطبقات المدرب بشكل تمييزي يحقق أداءً متقدماً على مجموعة بيانات MNIST ويتفوق بشكل ملحوظ على الشبكة الالتفافية في التعرف على الأرقام المتداخلة بشكل كبير. لتحقيق هذه النتائج، نستخدم آلية توجيه متكررة بالاتفاق (routing-by-agreement): تفضل الكبسولة ذات المستوى الأدنى إرسال مخرجاتها إلى الكبسولات ذات المستوى الأعلى التي تحتوي متجهات نشاطها على حاصل ضرب قياسي كبير مع التنبؤ القادم من الكبسولة ذات المستوى الأدنى.

حقيقة أن مخرجات الكبسولة عبارة عن متجه تجعل من الممكن استخدام آلية توجيه ديناميكية قوية لضمان إرسال مخرجات الكبسولة إلى عقدة أب مناسبة في الطبقة الأعلى. في البداية، يتم توجيه المخرجات إلى جميع الآباء المحتملين ولكن يتم تصغير حجمها بواسطة معاملات الاقتران (coupling coefficients) التي مجموعها 1. لكل أب محتمل، تحسب الكبسولة "متجه تنبؤ" (prediction vector) عن طريق ضرب مخرجاتها الخاصة في مصفوفة أوزان. إذا كان متجه التنبؤ هذا يحتوي على حاصل ضرب قياسي كبير مع مخرجات الأب المحتمل، فهناك تغذية راجعة من أعلى إلى أسفل لها تأثير زيادة معامل الاقتران لذلك الأب وتقليله للآباء الآخرين. هذا يزيد من المساهمة التي تقدمها الكبسولة لذلك الأب، وبالتالي يزيد من حاصل الضرب القياسي لتنبؤ الكبسولة مع مخرجات الأب. يجب أن يكون هذا النوع من "التوجيه بالاتفاق" أكثر فعالية بكثير من الشكل البدائي جداً للتوجيه الذي يتم تنفيذه بواسطة التجميع الأقصى (max-pooling)، والذي يسمح للعصبونات في طبقة واحدة بتجاهل كل شيء باستثناء كاشف الميزات الأكثر نشاطاً في مجموعة محلية في الطبقة الأدنى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - fixation points (نقاط التثبيت) - biological vision concept
  - parse tree (شجرة التحليل اللغوي) - hierarchical structure representation
  - attention mechanism (آلية انتباه) - sequential attention
  - capsule (كبسولة) - core concept, group of neurons
  - instantiation parameters (معاملات التجسيد) - entity properties
  - activity vector (متجه النشاط) - capsule output
  - routing-by-agreement (التوجيه بالاتفاق) - dynamic routing mechanism
  - coupling coefficients (معاملات الاقتران) - routing weights
  - prediction vector (متجه التنبؤ) - capsule predictions
  - scalar product (حاصل الضرب القياسي) - dot product
  - max-pooling (التجميع الأقصى) - CNN operation

- **Equations:** None in introduction
- **Citations:** References MNIST dataset
- **Special handling:**
  - Maintained biological vision analogy with human visual system
  - Preserved technical precision for routing mechanism description
  - Kept mathematical terminology consistent (scalar product, vector, matrix)
  - Explained the dynamic routing concept clearly

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Semantic Analysis

The translation accurately captures:
1. The biological motivation from human vision and fixation points
2. The parse tree analogy and how it maps to neural networks
3. The complete definition and function of capsules
4. The routing-by-agreement mechanism in detail
5. The contrast with traditional CNNs and max-pooling
6. The performance claims on MNIST

The Arabic maintains formal academic style while preserving all technical details and the logical flow of the introduction.
