# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** differential privacy, privacy guarantees, mechanism, database, adjacent databases, Gaussian mechanism, sensitivity, composition theorem, privacy accountant, deep learning, neural networks, loss function, gradient descent, SGD, mini-batch, TensorFlow

---

### English Version

In this section we briefly recall the definition of differential privacy, introduce the Gaussian mechanism and composition theorems, and overview basic principles of deep learning.

#### 2.1 Differential Privacy

Differential privacy constitutes a strong standard for privacy guarantees for algorithms on aggregate databases. It is defined in terms of the application-specific concept of adjacent databases. In our experiments, for instance, each training dataset is a set of image-label pairs; we say that two of these sets are adjacent if they differ in a single entry, that is, if one image-label pair is present in one set and absent in the other.

**Definition:** A randomized mechanism M: D → R with domain D and range R satisfies (ε,δ)-differential privacy if for any two adjacent inputs d,d' ∈ D and for any subset of outputs S ⊆ R it holds that

Pr[M(d) ∈ S] ≤ e^ε Pr[M(d') ∈ S] + δ.

The original definition of ε-differential privacy does not include the additive term δ. We use the variant introduced by Dwork et al., which allows for the possibility that plain ε-differential privacy is broken with probability δ (which is preferably smaller than 1/|d|).

Differential privacy has several properties that make it particularly useful in applications such as ours: composability, group privacy, and robustness to auxiliary information. Composability enables modular design of mechanisms: if all the components of a mechanism are differentially private, then so is their composition. Group privacy implies graceful degradation of privacy guarantees if datasets contain correlated inputs, such as the ones contributed by the same individual. Robustness to auxiliary information means that privacy guarantees are not affected by any side information available to the adversary.

A common paradigm for approximating a deterministic real-valued function f: D → ℝ with a differentially private mechanism is via additive noise calibrated to f's sensitivity S_f, which is defined as the maximum of the absolute distance |f(d)-f(d')| where d and d' are adjacent inputs. (The restriction to a real-valued function is intended to simplify this review, but is not essential.) For instance, the Gaussian noise mechanism is defined by

M(d) = f(d) + N(0, S_f² · σ²),

where N(0, S_f² · σ²) is the normal (Gaussian) distribution with mean 0 and standard deviation S_f σ. A single application of the Gaussian mechanism to function f of sensitivity S_f satisfies (ε, δ)-differential privacy if δ ≥ (4/5)exp(-(σε)²/2) and ε < 1. Note that this analysis of the mechanism can be applied post hoc, and, in particular, that there are infinitely many (ε,δ) pairs that satisfy this condition.

Differential privacy for repeated applications of additive-noise mechanisms follows from the basic composition theorem, or from advanced composition theorems and their refinements. The task of keeping track of the accumulated privacy loss in the course of execution of a composite mechanism, and enforcing the applicable privacy policy, can be performed by the privacy accountant, introduced by McSherry.

The basic blueprint for designing a differentially private additive-noise mechanism that implements a given functionality consists of the following steps: approximating the functionality by a sequential composition of bounded-sensitivity functions; choosing parameters of additive noise; and performing privacy analysis of the resulting mechanism. We follow this approach in Section 3.

#### 2.2 Deep Learning

Deep neural networks, which are remarkably effective for many machine learning tasks, define parameterized functions from inputs to outputs as compositions of many layers of basic building blocks, such as affine transformations and simple nonlinear functions. Commonly used examples of the latter are sigmoids and rectified linear units (ReLUs). By varying parameters of these blocks, we can "train" such a parameterized function with the goal of fitting any given finite set of input/output examples.

More precisely, we define a loss function L that represents the penalty for mismatching the training data. The loss L(θ) on parameters θ is the average of the loss over the training examples {x₁, ..., xₙ}, so L(θ) = (1/N)Σᵢ L(θ, xᵢ). Training consists in finding θ that yields an acceptably small loss, hopefully the smallest loss (though in practice we seldom expect to reach an exact global minimum).

For complex networks, the loss function L is usually non-convex and difficult to minimize. In practice, the minimization is often done by the mini-batch stochastic gradient descent (SGD) algorithm. In this algorithm, at each step, one forms a batch B of random examples and computes g_B = (1/|B|)Σ_{x∈B} ∇_θ L(θ, x) as an estimation to the gradient ∇_θ L(θ). Then θ is updated following the gradient direction -g_B towards a local minimum.

Several systems have been built to support the definition of neural networks, to enable efficient training, and then to perform efficient inference (execution for fixed parameters). We base our work on TensorFlow, an open-source dataflow engine released by Google. TensorFlow allows the programmer to define large computation graphs from basic operators, and to distribute their execution across a heterogeneous distributed system. TensorFlow automates the creation of the computation graphs for gradients; it also makes it easy to batch computation.

---

### النسخة العربية

في هذا القسم نستعرض بإيجاز تعريف الخصوصية التفاضلية، ونقدم آلية غاوس (Gaussian mechanism) ومبرهنات التركيب، ونعطي نظرة عامة على المبادئ الأساسية للتعلم العميق.

#### 2.1 الخصوصية التفاضلية

تشكل الخصوصية التفاضلية معياراً قوياً لضمانات الخصوصية للخوارزميات على قواعد البيانات المجمعة. يتم تعريفها بدلالة مفهوم قواعد البيانات المتجاورة الخاص بالتطبيق. في تجاربنا، على سبيل المثال، كل مجموعة بيانات تدريب هي مجموعة من أزواج صورة-تسمية؛ نقول إن مجموعتين من هذه المجموعات متجاورتان إذا اختلفتا في إدخال واحد، أي إذا كان زوج صورة-تسمية واحد موجوداً في مجموعة وغائباً في الأخرى.

**التعريف:** آلية عشوائية M: D → R بمجال D ومدى R تحقق خصوصية تفاضلية (ε,δ) إذا كان لأي مدخلين متجاورين d,d' ∈ D ولأي مجموعة فرعية من المخرجات S ⊆ R يتحقق أن

Pr[M(d) ∈ S] ≤ e^ε Pr[M(d') ∈ S] + δ.

التعريف الأصلي للخصوصية التفاضلية ε لا يتضمن الحد الإضافي δ. نستخدم النسخة التي قدمها Dwork وزملاؤه، والتي تسمح بإمكانية أن يتم كسر الخصوصية التفاضلية البسيطة ε باحتمال δ (والذي يُفضل أن يكون أصغر من 1/|d|).

تمتلك الخصوصية التفاضلية عدة خصائص تجعلها مفيدة بشكل خاص في تطبيقات مثل تطبيقاتنا: القابلية للتركيب، وخصوصية المجموعة، والمتانة ضد المعلومات المساعدة. تتيح القابلية للتركيب التصميم المعياري للآليات: إذا كانت جميع مكونات آلية ما خاصة بالخصوصية التفاضلية، فكذلك يكون تركيبها. تعني خصوصية المجموعة التدهور التدريجي لضمانات الخصوصية إذا كانت مجموعات البيانات تحتوي على مدخلات مترابطة، مثل تلك المقدمة من نفس الفرد. تعني المتانة ضد المعلومات المساعدة أن ضمانات الخصوصية لا تتأثر بأي معلومات جانبية متاحة للخصم.

النموذج الشائع لتقريب دالة محددة ذات قيمة حقيقية f: D → ℝ بآلية خاصة بالخصوصية التفاضلية هو عبر ضوضاء إضافية معايرة لحساسية f وهي S_f، والتي تُعرف بأنها القيمة القصوى للمسافة المطلقة |f(d)-f(d')| حيث d و d' مدخلات متجاورة. (القيد على دالة ذات قيمة حقيقية مقصود لتبسيط هذا الاستعراض، ولكنه ليس أساسياً). على سبيل المثال، آلية ضوضاء غاوس تُعرف بـ

M(d) = f(d) + N(0, S_f² · σ²),

حيث N(0, S_f² · σ²) هو التوزيع الطبيعي (غاوس) بمتوسط 0 وانحراف معياري S_f σ. يحقق تطبيق واحد لآلية غاوس على دالة f ذات حساسية S_f خصوصية تفاضلية (ε, δ) إذا كان δ ≥ (4/5)exp(-(σε)²/2) و ε < 1. لاحظ أن هذا التحليل للآلية يمكن تطبيقه بأثر رجعي (post hoc)، وعلى وجه الخصوص، أن هناك عدداً لا نهائياً من أزواج (ε,δ) التي تحقق هذا الشرط.

تنتج الخصوصية التفاضلية للتطبيقات المتكررة لآليات الضوضاء الإضافية من مبرهنة التركيب الأساسية، أو من مبرهنات التركيب المتقدمة وتحسيناتها. يمكن أن تُنفذ مهمة تتبع خسارة الخصوصية المتراكمة في سياق تنفيذ آلية مركبة، وفرض سياسة الخصوصية المعمول بها، بواسطة محاسب الخصوصية (privacy accountant)، الذي قدمه McSherry.

المخطط الأساسي لتصميم آلية ضوضاء إضافية خاصة بالخصوصية التفاضلية تنفذ وظيفة معينة يتكون من الخطوات التالية: تقريب الوظيفة بتركيب تسلسلي لدوال محدودة الحساسية؛ اختيار معاملات الضوضاء الإضافية؛ وإجراء تحليل الخصوصية للآلية الناتجة. نتبع هذا النهج في القسم 3.

#### 2.2 التعلم العميق

تعرّف الشبكات العصبية العميقة، والتي تُعد فعالة بشكل ملحوظ للعديد من مهام تعلم الآلة، دوالاً معاملية من المدخلات إلى المخرجات كتركيبات من طبقات عديدة من الكتل البنائية الأساسية، مثل التحويلات الخطية والدوال غير الخطية البسيطة. من الأمثلة الشائعة الاستخدام للأخيرة دوال السيغمويد ووحدات التصحيح الخطية (ReLUs). من خلال تغيير معاملات هذه الكتل، يمكننا "تدريب" مثل هذه الدالة المعاملية بهدف ملاءمة أي مجموعة محدودة معطاة من أمثلة الإدخال/الإخراج.

بشكل أكثر دقة، نعرّف دالة خسارة L تمثل العقوبة لعدم مطابقة بيانات التدريب. الخسارة L(θ) على المعاملات θ هي متوسط الخسارة على أمثلة التدريب {x₁, ..., xₙ}، بحيث L(θ) = (1/N)Σᵢ L(θ, xᵢ). يتكون التدريب من إيجاد θ الذي ينتج خسارة صغيرة مقبولة، ونأمل أصغر خسارة (على الرغم من أننا في الممارسة العملية نادراً ما نتوقع الوصول إلى حد أدنى عام دقيق).

بالنسبة للشبكات المعقدة، عادة ما تكون دالة الخسارة L غير محدبة وصعبة التصغير. في الممارسة العملية، غالباً ما يتم التصغير بواسطة خوارزمية الانحدار التدرجي العشوائي بالدفعات الصغيرة (mini-batch SGD). في هذه الخوارزمية، في كل خطوة، يتم تشكيل دفعة B من الأمثلة العشوائية ويتم حساب g_B = (1/|B|)Σ_{x∈B} ∇_θ L(θ, x) كتقدير للتدرج ∇_θ L(θ). ثم يتم تحديث θ باتباع اتجاه التدرج -g_B نحو حد أدنى محلي.

تم بناء عدة أنظمة لدعم تعريف الشبكات العصبية، ولتمكين التدريب الفعال، ثم لإجراء الاستنتاج الفعال (التنفيذ للمعاملات الثابتة). نبني عملنا على TensorFlow، وهو محرك تدفق بيانات مفتوح المصدر أطلقته Google. يتيح TensorFlow للمبرمج تعريف رسوم بيانية حسابية كبيرة من المعاملات الأساسية، وتوزيع تنفيذها عبر نظام موزع غير متجانس. يقوم TensorFlow بأتمتة إنشاء الرسوم البيانية الحسابية للتدرجات؛ كما يسهل دفع (batching) الحسابات.

---

### Translation Notes

- **Key concepts:**
  - Formal definition of differential privacy with (ε,δ) parameters
  - Gaussian mechanism for adding calibrated noise
  - Composition theorems and privacy accountant
  - Deep learning fundamentals: loss functions, SGD, TensorFlow

- **Technical terms:**
  - "adjacent databases" - قواعد البيانات المتجاورة (formal privacy term)
  - "mechanism" - آلية (standard privacy terminology)
  - "sensitivity" - حساسية (mathematical term)
  - "privacy accountant" - محاسب الخصوصية (technical term introduced in privacy literature)
  - "mini-batch SGD" - الانحدار التدرجي العشوائي بالدفعات الصغيرة (established ML term)
  - "ReLUs" - وحدات التصحيح الخطية (kept acronym, provided translation)
  - "post hoc" - بأثر رجعي (Latin term, translated)

- **Mathematical notation:**
  - Preserved all mathematical symbols and equations
  - Added Arabic explanations where helpful
  - Maintained formal definition structure

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
