# Section 5: Implementation Notes
## القسم 5: ملاحظات التنفيذ

**Section:** implementation-notes
**Translation Quality:** 0.86
**Glossary Terms Used:** memory efficient (كفء في استخدام الذاكرة), inference (الاستدلال), TensorFlow, Caffe, directed acyclic compute hypergraph (رسم بياني فائق حسابي لا دوري موجه), operations (عمليات), nodes (عقد), tensors (موترات), intermediate computation (الحساب الوسيط), bottleneck residual block (كتلة عنق البقايا), linear transformation (تحويل خطي), non-linear per-channel transformation (تحويل لاخطي لكل قناة), depthwise (حسب العمق), internal storage (التخزين الداخلي), matrix multiplication (ضرب المصفوفات), cache misses (إخفاقات الذاكرة المؤقتة)

---

### English Version

## 5.1 Memory Efficient Inference

The inverted residual bottleneck layers allow a particularly memory efficient implementation which is very important for mobile applications. A standard efficient implementation of inference that uses for instance TensorFlow or Caffe, builds a directed acyclic compute hypergraph $G$, consisting of edges representing the operations and nodes representing tensors of intermediate computation. The computation is scheduled in order to minimize the total number of tensors that needs to be stored in memory. In the most general case, it searches over all plausible computation orders $\Sigma(G)$ and picks the one that minimizes:

$$M(G) = \min_{\pi\in \Sigma(G)} \max_{i \in 1..n} \left[\sum_{A \in R(i, \pi, G)} |A|\right] + \text{size}(\pi_i)$$

where $R(i, \pi, G)$ is the list of intermediate tensors that are connected to any of $\pi_{i}\dots \pi_{n}$ nodes, $|A|$ represents the size of the tensor $A$ and $\text{size}(i)$ is the total amount of memory needed for internal storage during operation $i$.

For graphs that have only trivial parallel structure (such as residual connection), there is only one non-trivial feasible computation order, and thus the total amount and a bound on the memory needed for inference on compute graph $G$ can be simplified:

$$M(G) = \max_{op \in G} \left[\sum_{A \in \text{op}_{inp}} |A| + \sum_{B \in \text{op}_{out}} |B| + |op|\right]$$

Or to restate, the amount of memory is simply the maximum total size of combined inputs and outputs across all operations. In what follows we show that if we treat a bottleneck residual block as a single operation (and treat inner convolution as a disposable tensor), the total amount of memory would be dominated by the size of bottleneck tensors, rather than the size of tensors that are internal to bottleneck (and much larger).

**Bottleneck Residual Block**: A bottleneck block operator $\mathcal{F}(x)$ shown in Figure 3 can be expressed as a composition of three operators $\mathcal{F}(x) = [A \circ \mathcal{N} \circ B] x$, where $A$ is a linear transformation $A:\mathbb{R}^{s \times s \times k} \rightarrow \mathbb{R}^{s \times s \times n}$, $\mathcal{N}$ is a non-linear per-channel transformation: $\mathcal{N}: \mathbb{R}^{s \times s \times n} \rightarrow \mathbb{R}^{s' \times s' \times n}$, and $B$ is again a linear transformation to the output domain: $B: \mathbb{R}^{s' \times s' \times n} \rightarrow \mathbb{R}^{s' \times s' \times k'}$.

For our networks $\mathcal{N} = \text{ReLU6} \circ \text{dwise} \circ \text{ReLU6}$, but the results apply to any per-channel transformation. Suppose the size of the input domain is $|x|$ and the size of the output domain is $|y|$, then the memory required to compute $\mathcal{F}(X)$ can be as low as $|s^2 k| + |s'^2 k'| + O(\max(s^2, s'^2))$.

The algorithm is based on the fact that the inner tensor $\mathcal{I}$ can be represented as concatenation of $t$ tensors, of size $n/t$ each and our function can then be represented as:

$$\mathcal{F}(x) = \sum_{i=1}^t (A_i \circ \mathcal{N} \circ B_i)(x)$$

by accumulating the sum, we only require one intermediate block of size $n/t$ to be kept in memory at all times. Using $n=t$ we end up having to keep only a single channel of the intermediate representation at all times. The two constraints that enabled us to use this trick is (a) the fact that the inner transformation (which includes non-linearity and depthwise) is per-channel, and (b) the consecutive non-per-channel operators have significant ratio of the input size to the output. For most of the traditional neural networks, such trick would not produce a significant improvement.

We note that, the number of multiply-adds operators needed to compute $\mathcal{F}(X)$ using $t$-way split is independent of $t$, however in existing implementations we find that replacing one matrix multiplication with several smaller ones hurts runtime performance due to increased cache misses. We find that this approach is the most helpful to be used with $t$ being a small constant between 2 and 5. It significantly reduces the memory requirement, but still allows one to utilize most of the efficiencies gained by using highly optimized matrix multiplication and convolution operators provided by deep learning frameworks. It remains to be seen if special framework level optimization may lead to further runtime improvements.

---

### النسخة العربية

## 5.1 الاستدلال الكفء في استخدام الذاكرة

تسمح طبقات عنق البقايا المعكوسة بتنفيذ كفء بشكل خاص في استخدام الذاكرة وهو أمر مهم جداً للتطبيقات المحمولة. يبني التنفيذ القياسي الكفء للاستدلال الذي يستخدم على سبيل المثال TensorFlow أو Caffe، رسماً بيانياً فائقاً حسابياً لا دورياً موجهاً $G$، يتكون من حواف تمثل العمليات وعقد تمثل موترات الحساب الوسيط. يتم جدولة الحساب لتقليل العدد الإجمالي للموترات التي يجب تخزينها في الذاكرة. في الحالة الأكثر عمومية، يبحث عن جميع ترتيبات الحساب المعقولة $\Sigma(G)$ ويختار الترتيب الذي يقلل:

$$M(G) = \min_{\pi\in \Sigma(G)} \max_{i \in 1..n} \left[\sum_{A \in R(i, \pi, G)} |A|\right] + \text{size}(\pi_i)$$

حيث $R(i, \pi, G)$ هي قائمة الموترات الوسيطة المتصلة بأي من العقد $\pi_{i}\dots \pi_{n}$، و$|A|$ يمثل حجم الموتر $A$ و$\text{size}(i)$ هو إجمالي كمية الذاكرة المطلوبة للتخزين الداخلي أثناء العملية $i$.

بالنسبة للرسوم البيانية التي لها فقط بنية متوازية تافهة (مثل اتصال البقايا)، هناك ترتيب حساب قابل للتنفيذ واحد فقط غير تافه، وبالتالي يمكن تبسيط الكمية الإجمالية والحد الأقصى للذاكرة المطلوبة للاستدلال على الرسم البياني الحسابي $G$:

$$M(G) = \max_{op \in G} \left[\sum_{A \in \text{op}_{inp}} |A| + \sum_{B \in \text{op}_{out}} |B| + |op|\right]$$

أو بإعادة الصياغة، فإن كمية الذاكرة هي ببساطة الحد الأقصى للحجم الإجمالي للمدخلات والمخرجات المجمعة عبر جميع العمليات. في ما يلي نُظهر أنه إذا عاملنا كتلة عنق البقايا كعملية واحدة (وعاملنا الالتفاف الداخلي كموتر يمكن التخلص منه)، فإن الكمية الإجمالية للذاكرة ستكون مهيمنة من قبل حجم موترات العنق، بدلاً من حجم الموترات الداخلية للعنق (والأكبر بكثير).

**كتلة عنق البقايا**: يمكن التعبير عن مشغل كتلة عنق $\mathcal{F}(x)$ الموضح في الشكل 3 كتركيب لثلاثة مشغلات $\mathcal{F}(x) = [A \circ \mathcal{N} \circ B] x$، حيث $A$ هو تحويل خطي $A:\mathbb{R}^{s \times s \times k} \rightarrow \mathbb{R}^{s \times s \times n}$، و$\mathcal{N}$ هو تحويل لاخطي لكل قناة: $\mathcal{N}: \mathbb{R}^{s \times s \times n} \rightarrow \mathbb{R}^{s' \times s' \times n}$، و$B$ هو مرة أخرى تحويل خطي إلى مجال الإخراج: $B: \mathbb{R}^{s' \times s' \times n} \rightarrow \mathbb{R}^{s' \times s' \times k'}$.

بالنسبة لشبكاتنا $\mathcal{N} = \text{ReLU6} \circ \text{dwise} \circ \text{ReLU6}$، لكن النتائج تنطبق على أي تحويل لكل قناة. لنفترض أن حجم مجال الإدخال هو $|x|$ وحجم مجال الإخراج هو $|y|$، فإن الذاكرة المطلوبة لحساب $\mathcal{F}(X)$ يمكن أن تكون منخفضة تصل إلى $|s^2 k| + |s'^2 k'| + O(\max(s^2, s'^2))$.

تعتمد الخوارزمية على حقيقة أن الموتر الداخلي $\mathcal{I}$ يمكن تمثيله كتسلسل لـ $t$ موترات، كل منها بحجم $n/t$ ويمكن تمثيل دالتنا بعد ذلك على النحو التالي:

$$\mathcal{F}(x) = \sum_{i=1}^t (A_i \circ \mathcal{N} \circ B_i)(x)$$

من خلال تجميع المجموع، نحتاج فقط إلى كتلة وسيطة واحدة بحجم $n/t$ للاحتفاظ بها في الذاكرة في جميع الأوقات. باستخدام $n=t$ ينتهي بنا الأمر بالاحتفاظ فقط بقناة واحدة من التمثيل الوسيط في جميع الأوقات. القيدان اللذان مكّناننا من استخدام هذه الحيلة هما (أ) حقيقة أن التحويل الداخلي (الذي يتضمن اللاخطية والعمق) هو لكل قناة، و(ب) المشغلات المتتالية غير الخاصة بكل قناة لها نسبة كبيرة من حجم الإدخال إلى الإخراج. بالنسبة لمعظم الشبكات العصبية التقليدية، فإن مثل هذه الحيلة لن تنتج تحسيناً كبيراً.

نلاحظ أن عدد مشغلات عمليات الضرب والجمع المطلوبة لحساب $\mathcal{F}(X)$ باستخدام التقسيم إلى $t$ أجزاء مستقل عن $t$، ومع ذلك في التطبيقات الحالية نجد أن استبدال ضرب مصفوفة واحد بعدة عمليات أصغر يضر بأداء وقت التشغيل بسبب زيادة إخفاقات الذاكرة المؤقتة. نجد أن هذا النهج هو الأكثر فائدة عند استخدامه مع $t$ كثابت صغير بين 2 و5. فهو يقلل بشكل كبير من متطلبات الذاكرة، ولكنه لا يزال يسمح باستخدام معظم الكفاءات المكتسبة من استخدام مشغلات ضرب المصفوفات والالتفاف المُحسّنة للغاية التي توفرها أطر عمل التعلم العميق. لا يزال يتعين رؤية ما إذا كان التحسين الخاص على مستوى إطار العمل قد يؤدي إلى مزيد من تحسينات وقت التشغيل.

---

### Translation Notes

- **Figures referenced:** Figure 3 (bottleneck residual block)
- **Key terms introduced:**
  - Memory efficient implementation (تنفيذ كفء في استخدام الذاكرة)
  - Directed acyclic compute hypergraph (رسم بياني فائق حسابي لا دوري موجه)
  - Intermediate computation (الحساب الوسيط)
  - Computation order (ترتيب الحساب)
  - Internal storage (التخزين الداخلي)
  - Disposable tensor (موتر يمكن التخلص منه)
  - Per-channel transformation (تحويل لكل قناة)
  - Matrix multiplication (ضرب المصفوفات)
  - Cache misses (إخفاقات الذاكرة المؤقتة)
  - Framework level optimization (التحسين على مستوى إطار العمل)

- **Equations:** 3 main equations for memory computation
- **Citations:** References to TensorFlow, Caffe frameworks
- **Special handling:**
  - Complex mathematical notation preserved in LaTeX
  - Framework names (TensorFlow, Caffe) kept as proper nouns
  - ReLU6, dwise kept as standard operation names
  - Mathematical symbols ($\mathcal{F}$, $\mathcal{N}$, etc.) preserved
  - Big-O notation maintained

### Quality Metrics

- **Semantic equivalence:** 0.87 - Accurately conveys complex memory optimization concepts
- **Technical accuracy:** 0.88 - Correct translation of advanced computer science and optimization terms
- **Readability:** 0.84 - Complex material but clearly presented in Arabic
- **Glossary consistency:** 0.86 - Uses established terms, introduces new optimization terms appropriately
- **Overall section score:** 0.86

### Back-translation Check (Key Sentences)

**Original:** "In what follows we show that if we treat a bottleneck residual block as a single operation (and treat inner convolution as a disposable tensor), the total amount of memory would be dominated by the size of bottleneck tensors, rather than the size of tensors that are internal to bottleneck (and much larger)."

**Arabic:** "في ما يلي نُظهر أنه إذا عاملنا كتلة عنق البقايا كعملية واحدة (وعاملنا الالتفاف الداخلي كموتر يمكن التخلص منه)، فإن الكمية الإجمالية للذاكرة ستكون مهيمنة من قبل حجم موترات العنق، بدلاً من حجم الموترات الداخلية للعنق (والأكبر بكثير)."

**Back-translation:** "In what follows we show that if we treat the bottleneck residual block as a single operation (and treat the inner convolution as a disposable tensor), the total amount of memory will be dominated by the size of the bottleneck tensors, rather than the size of the internal tensors to the bottleneck (which are much larger)."

✓ **Semantic match verified**

**Original:** "We find that this approach is the most helpful to be used with $t$ being a small constant between 2 and 5. It significantly reduces the memory requirement, but still allows one to utilize most of the efficiencies gained by using highly optimized matrix multiplication and convolution operators provided by deep learning frameworks."

**Arabic:** "نجد أن هذا النهج هو الأكثر فائدة عند استخدامه مع $t$ كثابت صغير بين 2 و5. فهو يقلل بشكل كبير من متطلبات الذاكرة، ولكنه لا يزال يسمح باستخدام معظم الكفاءات المكتسبة من استخدام مشغلات ضرب المصفوفات والالتفاف المُحسّنة للغاية التي توفرها أطر عمل التعلم العميق."

**Back-translation:** "We find that this approach is most beneficial when used with $t$ as a small constant between 2 and 5. It significantly reduces memory requirements, but still allows utilizing most of the efficiencies gained from using highly optimized matrix multiplication and convolution operators provided by deep learning frameworks."

✓ **Semantic match verified**
