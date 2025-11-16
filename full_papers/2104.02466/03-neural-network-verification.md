# Section 3: Neural Network Verification
## القسم 3: التحقق من الشبكة العصبية

**Section:** Neural Network Verification Methods
**Translation Quality:** 0.86
**Glossary Terms Used:** neural networks, verification, SMT, optimization, abstract interpretation, ReLU, activation function, adversarial examples, robustness, soundness, completeness

---

### English Version

## 3. Verification of Neural Networks

The majority of formal verification research for machine learning focuses on feedforward neural networks, particularly deep neural networks with piecewise linear activation functions such as ReLU (Rectified Linear Unit). This section surveys the three main families of verification techniques: SMT-based, optimization-based, and abstract interpretation approaches.

### 3.1 Problem Formulation

Neural network verification typically addresses questions of the form: *Given a trained neural network N and a property φ, does N satisfy φ for all inputs in some region?*

Common verification properties include:

**Local Robustness**: For a given input x and small perturbation bound ε, verify that all inputs within distance ε of x produce the same classification. Formally: ∀x' : ||x' - x|| ≤ ε ⟹ argmax(N(x')) = argmax(N(x))

This property is crucial for defending against adversarial examples—small perturbations crafted to cause misclassification.

**Safety Properties**: Verify that outputs satisfy domain-specific constraints. For example, in collision avoidance systems, verify that the network never produces commands that would result in unsafe aircraft separation.

**Input-Output Specifications**: Given preconditions on inputs and postconditions on outputs, verify the implication holds: Input ∈ P_in ⟹ Output ∈ P_out

The verification problem is computationally challenging. Even for networks with piecewise linear activations, exact verification is NP-complete. This motivates approximate techniques that trade completeness or precision for scalability.

### 3.2 SMT-Based Verification

Satisfiability Modulo Theories (SMT) solvers decide satisfiability of logical formulas in various theories (e.g., linear arithmetic, bit-vectors). SMT-based neural network verification encodes the network and property as logical constraints, then queries the SMT solver.

**Approach**: For a network with ReLU activations, each layer can be encoded as linear constraints with conditionals for the ReLU max(0,x) operation. The verification query becomes: "Is there an input satisfying the precondition that violates the postcondition?"

If the SMT solver returns UNSAT (unsatisfiable), the property is verified. If SAT (satisfiable), the solver provides a counterexample.

**Tools and Techniques**:

- **Reluplex** (Katz et al., 2017): The first SMT-based verifier for ReLU networks, extending the Simplex algorithm to handle ReLU constraints. Applied to collision avoidance systems (ACAS Xu), proving safety properties on small networks.

- **Planet** (Ehlers, 2017): Uses incremental SMT solving with conflict-driven learning to improve scalability.

- **Marabou** (Katz et al., 2019): Successor to Reluplex, supporting larger networks and additional activation functions. Uses divide-and-conquer strategies and symbolic bound propagation.

**Strengths**:
- Complete for piecewise linear networks (finds counterexamples if they exist)
- Exact—no approximation when verification succeeds
- Provides concrete counterexamples when properties fail

**Limitations**:
- Scalability: Struggles with networks beyond a few thousand neurons
- Restricted to specific activation functions (primarily ReLU and variants)
- Exponential worst-case complexity
- No guarantee of termination within reasonable time for large problems

### 3.3 Optimization-Based Verification

Optimization-based approaches formulate verification as solving an optimization problem, typically finding the maximum or minimum of an objective function over the input space subject to neural network constraints.

**Approach**: To verify local robustness, solve:
$$\max_{x'} \; f_t(N(x')) - f_y(N(x')) \quad \text{subject to} \quad ||x' - x|| \leq \epsilon$$

where $f_t$ is the logit for true class and $f_y$ for another class. If the maximum is negative for all classes $y \neq t$, robustness is verified.

**Techniques**:

- **Linear Programming Relaxations**: Overapproximate nonlinear activation functions with linear constraints, creating a linear program that can be solved efficiently. If the LP proves the property, it holds for the original network (soundness). However, the relaxation may be too loose to prove properties (incomplete).

- **Convex Relaxations**: Formulate tighter convex approximations of network behavior. Methods like those in Wong & Kolter (2018) use dual approaches to certify robustness bounds.

- **Mixed-Integer Programming**: Encode ReLU networks exactly as mixed-integer linear programs (MILPs). Exact but computationally expensive for large networks.

**Tools**:

- **DeepPoly** (Singh et al., 2019): Combines abstract interpretation with optimization, using polyhedra to approximate network layers efficiently.

- **CROWN** (Zhang et al., 2018): Certified Robustness with Output Network, uses linear bounds propagation.

- **Certify** (Raghunathan et al., 2018): Semidefinite programming relaxation for robustness certification.

**Strengths**:
- Better scalability than SMT for certain problem classes
- Can leverage mature optimization solvers
- Provides certified bounds on network outputs
- Parallelizable for different classes or input regions

**Limitations**:
- Relaxations may be too loose, failing to verify true properties (incompleteness)
- Exact methods (MILPs) face scalability issues
- Primarily applicable to ReLU and piecewise linear activations
- Difficulty handling very deep networks (bound looseness compounds across layers)

### 3.4 Abstract Interpretation for Neural Networks

Abstract interpretation approaches apply the theoretical framework described in Section 2.2 to neural networks, overapproximating the set of possible outputs for a given input region using abstract domains.

**Approach**: Start with an abstract representation of the input region (e.g., an interval or zonotope). Propagate this abstract element through network layers using abstract transformers that overapproximate each operation. If the resulting output abstraction satisfies the property for all concretizations, the property is verified.

**Abstract Domains**:

- **Intervals**: Track lower and upper bounds for each neuron. Efficient but imprecise due to losing correlations.

- **Zonotopes**: Represent sets as affine transformations of unit boxes, preserving linear relationships. More precise than intervals for linear layers but require approximation for nonlinear activations.

- **Polyhedra**: Arbitrary linear constraints, offering high precision but higher computational cost.

- **Hybrid Domains**: Combine multiple domains, using simpler domains where sufficient and precise domains where needed.

**Tools**:

- **AI² (Gehr et al., 2018)**: First abstract interpretation verifier for neural networks, using zonotopes and polyhedra.

- **DeepZ** (Singh et al., 2018): Zonotope-based verifier with optimized abstract transformers.

- **RefineZono** (Singh et al., 2019): Refines abstractions using MILP when initial approximation is too coarse.

- **ERAN** (Singh et al., 2019): ETH Robustness Analyzer for Neural Networks, combining multiple abstract domains.

**Strengths**:
- Sound guarantees—verified properties hold for all inputs
- Scales to larger networks than SMT/exact optimization
- Automatic—no manual proof guidance needed
- Handles various activation functions through abstract transformers
- Can verify properties over infinite input regions

**Limitations**:
- Incomplete—may fail to verify true properties due to overapproximation
- False alarms from conservative approximations
- Precision degrades with network depth (approximation error accumulates)
- Requires careful domain selection for balance between precision and performance

### 3.5 Comparative Analysis

The three families of techniques present different tradeoffs:

| Aspect | SMT-Based | Optimization-Based | Abstract Interpretation |
|--------|-----------|-------------------|------------------------|
| **Soundness** | ✓ Sound | ✓ Sound (with proper relaxations) | ✓ Sound |
| **Completeness** | ✓ Complete | ✗ Incomplete (relaxations) | ✗ Incomplete |
| **Scalability** | Limited (thousands of neurons) | Moderate | Best (millions of parameters) |
| **Counterexamples** | ✓ Provides counterexamples | Sometimes | ✗ No counterexamples |
| **Activation Functions** | Limited (ReLU, variants) | Primarily piecewise linear | More flexible |
| **Precision** | Exact (when completes) | Depends on relaxation | Depends on domain |

**Emerging Trends**:
- **Hybrid Methods**: Combining approaches (e.g., abstract interpretation with SMT refinement)
- **Certified Training**: Modifying training to produce more verifiable networks
- **Abstraction Refinement**: Automatically refining abstractions when verification fails
- **GPU Acceleration**: Parallelizing verification computations

Despite significant progress, verifying large modern networks (e.g., ImageNet-scale ResNets with millions of parameters) remains challenging. Current tools typically handle networks with thousands to tens of thousands of neurons for complete properties, or provide incomplete guarantees for larger networks.

---

### النسخة العربية

## 3. التحقق من الشبكات العصبية

تركز غالبية أبحاث التحقق الرسمي لتعلم الآلة على الشبكات العصبية ذات التغذية الأمامية، وخاصة الشبكات العصبية العميقة ذات دوال التنشيط الخطية المجزأة مثل ReLU (وحدة التصحيح الخطية). يستعرض هذا القسم العائلات الثلاث الرئيسية لتقنيات التحقق: المناهج القائمة على SMT، والمناهج القائمة على التحسين، ومناهج التفسير المجرد.

### 3.1 صياغة المشكلة

يعالج التحقق من الشبكة العصبية عادةً أسئلة من الشكل: *بالنظر إلى شبكة عصبية مدربة N وخاصية φ، هل تفي N بـ φ لجميع المدخلات في منطقة معينة؟*

تشمل خصائص التحقق الشائعة:

**المتانة المحلية**: لمدخل معين x وحد اضطراب صغير ε، تحقق من أن جميع المدخلات ضمن مسافة ε من x تنتج نفس التصنيف. رسمياً: ∀x' : ||x' - x|| ≤ ε ⟹ argmax(N(x')) = argmax(N(x))

هذه الخاصية حاسمة للدفاع ضد الأمثلة الخصامية—الاضطرابات الصغيرة المصممة لإحداث تصنيف خاطئ.

**خصائص السلامة**: تحقق من أن المخرجات تفي بقيود خاصة بالمجال. على سبيل المثال، في أنظمة تجنب التصادم، تحقق من أن الشبكة لا تنتج أبداً أوامر قد تؤدي إلى فصل غير آمن للطائرات.

**مواصفات المدخلات-المخرجات**: بالنظر إلى الشروط المسبقة على المدخلات والشروط اللاحقة على المخرجات، تحقق من أن التضمين صحيح: Input ∈ P_in ⟹ Output ∈ P_out

مشكلة التحقق صعبة حسابياً. حتى بالنسبة للشبكات ذات التنشيطات الخطية المجزأة، فإن التحقق الدقيق هو NP-كامل. وهذا يحفز التقنيات التقريبية التي تتبادل الاكتمال أو الدقة من أجل قابلية التوسع.

### 3.2 التحقق القائم على SMT

تقرر حلالات نظرية الإرضاء بالقياس (SMT) إرضاء الصيغ المنطقية في نظريات مختلفة (على سبيل المثال، الحساب الخطي، متجهات البت). يشفر التحقق من الشبكة العصبية القائم على SMT الشبكة والخاصية كقيود منطقية، ثم يستعلم حلال SMT.

**المنهج**: بالنسبة لشبكة بتنشيطات ReLU، يمكن تشفير كل طبقة كقيود خطية مع شروط لعملية ReLU max(0,x). يصبح استعلام التحقق: "هل هناك مدخل يفي بالشرط المسبق الذي ينتهك الشرط اللاحق؟"

إذا أرجع حلال SMT UNSAT (غير قابل للإرضاء)، يتم التحقق من الخاصية. إذا SAT (قابل للإرضاء)، يوفر الحلال مثالاً مضاداً.

**الأدوات والتقنيات**:

- **Reluplex** (Katz et al., 2017): أول مُحقق قائم على SMT لشبكات ReLU، يمدد خوارزمية Simplex للتعامل مع قيود ReLU. تم تطبيقه على أنظمة تجنب التصادم (ACAS Xu)، مما يثبت خصائص السلامة على الشبكات الصغيرة.

- **Planet** (Ehlers, 2017): يستخدم حل SMT التدريجي مع التعلم المدفوع بالتعارض لتحسين قابلية التوسع.

- **Marabou** (Katz et al., 2019): خلف Reluplex، يدعم شبكات أكبر ودوال تنشيط إضافية. يستخدم استراتيجيات فرِّق تَسُد وانتشار الحدود الرمزية.

**نقاط القوة**:
- كامل للشبكات الخطية المجزأة (يجد أمثلة مضادة إذا كانت موجودة)
- دقيق—لا تقريب عندما ينجح التحقق
- يوفر أمثلة مضادة محددة عندما تفشل الخصائص

**القيود**:
- قابلية التوسع: يكافح مع الشبكات التي تتجاوز بضعة آلاف من العصبونات
- مقيد بدوال تنشيط محددة (بشكل أساسي ReLU والمتغيرات)
- تعقيد أسوأ حالة أسي
- لا ضمان للإنهاء في وقت معقول للمشاكل الكبيرة

### 3.3 التحقق القائم على التحسين

تصيغ المناهج القائمة على التحسين التحقق كحل لمشكلة تحسين، عادةً إيجاد الحد الأقصى أو الأدنى لدالة هدف على فضاء المدخلات مع قيود الشبكة العصبية.

**المنهج**: للتحقق من المتانة المحلية، حل:
$$\max_{x'} \; f_t(N(x')) - f_y(N(x')) \quad \text{مع قيد} \quad ||x' - x|| \leq \epsilon$$

حيث $f_t$ هي logit للفئة الحقيقية و $f_y$ لفئة أخرى. إذا كان الحد الأقصى سالباً لجميع الفئات $y \neq t$، يتم التحقق من المتانة.

**التقنيات**:

- **إرخاءات البرمجة الخطية**: تقريب زائد لدوال التنشيط غير الخطية بقيود خطية، مما يخلق برنامجاً خطياً يمكن حله بكفاءة. إذا أثبت LP الخاصية، فإنها تنطبق على الشبكة الأصلية (السلامة المنطقية). ومع ذلك، قد يكون الإرخاء فضفاضاً جداً لإثبات الخصائص (غير كامل).

- **الإرخاءات المحدبة**: صياغة تقريبات محدبة أكثر إحكاماً لسلوك الشبكة. تستخدم أساليب مثل تلك الموجودة في Wong & Kolter (2018) مناهج مزدوجة لإصدار شهادات حدود المتانة.

- **البرمجة الصحيحة المختلطة**: تشفير شبكات ReLU بدقة كبرامج خطية صحيحة مختلطة (MILPs). دقيق ولكنه مكلف حسابياً للشبكات الكبيرة.

**الأدوات**:

- **DeepPoly** (Singh et al., 2019): يجمع بين التفسير المجرد والتحسين، باستخدام المضلعات لتقريب طبقات الشبكة بكفاءة.

- **CROWN** (Zhang et al., 2018): المتانة المعتمدة مع شبكة الإخراج، يستخدم انتشار الحدود الخطية.

- **Certify** (Raghunathan et al., 2018): إرخاء البرمجة شبه المحددة لإصدار شهادات المتانة.

**نقاط القوة**:
- قابلية توسع أفضل من SMT لفئات مشاكل معينة
- يمكن الاستفادة من حلالات التحسين الناضجة
- يوفر حدوداً معتمدة على مخرجات الشبكة
- قابل للتوازي لفئات أو مناطق مدخلات مختلفة

**القيود**:
- قد تكون الإرخاءات فضفاضة جداً، فاشلة في التحقق من الخصائص الحقيقية (عدم الاكتمال)
- تواجه الأساليب الدقيقة (MILPs) مشاكل قابلية التوسع
- قابلة للتطبيق بشكل أساسي على ReLU والتنشيطات الخطية المجزأة
- صعوبة في التعامل مع الشبكات العميقة جداً (يتراكم فضفضة الحدود عبر الطبقات)

### 3.4 التفسير المجرد للشبكات العصبية

تطبق مناهج التفسير المجرد الإطار النظري الموصوف في القسم 2.2 على الشبكات العصبية، مع التقريب الزائد لمجموعة المخرجات الممكنة لمنطقة مدخلات معينة باستخدام النطاقات المجردة.

**المنهج**: ابدأ بتمثيل مجرد لمنطقة المدخلات (على سبيل المثال، فترة أو zonotope). انشر هذا العنصر المجرد عبر طبقات الشبكة باستخدام محولات مجردة تقرب بشكل زائد كل عملية. إذا كان التجريد الناتج للمخرجات يفي بالخاصية لجميع التجسيدات، يتم التحقق من الخاصية.

**النطاقات المجردة**:

- **الفترات**: تتبع الحدود السفلية والعليا لكل عصبون. فعال ولكنه غير دقيق بسبب فقدان الارتباطات.

- **Zonotopes**: تمثل المجموعات كتحويلات أفينية لصناديق الوحدة، مع الحفاظ على العلاقات الخطية. أكثر دقة من الفترات للطبقات الخطية ولكنها تتطلب تقريباً للتنشيطات غير الخطية.

- **المضلعات**: قيود خطية عشوائية، تقدم دقة عالية ولكن بتكلفة حسابية أعلى.

- **النطاقات الهجينة**: تجمع بين نطاقات متعددة، باستخدام نطاقات أبسط حيثما كانت كافية ونطاقات دقيقة حيثما كانت هناك حاجة.

**الأدوات**:

- **AI²** (Gehr et al., 2018): أول مُحقق تفسير مجرد للشبكات العصبية، باستخدام zonotopes والمضلعات.

- **DeepZ** (Singh et al., 2018): مُحقق قائم على Zonotope مع محولات مجردة محسّنة.

- **RefineZono** (Singh et al., 2019): يحسّن التجريدات باستخدام MILP عندما يكون التقريب الأولي خشناً جداً.

- **ERAN** (Singh et al., 2019): محلل المتانة ETH للشبكات العصبية، يجمع بين نطاقات مجردة متعددة.

**نقاط القوة**:
- ضمانات سليمة—الخصائص المحققة تنطبق على جميع المدخلات
- يتوسع إلى شبكات أكبر من SMT/التحسين الدقيق
- تلقائي—لا حاجة لتوجيه الإثبات اليدوي
- يتعامل مع دوال تنشيط مختلفة من خلال المحولات المجردة
- يمكن التحقق من الخصائص على مناطق مدخلات لا نهائية

**القيود**:
- غير كامل—قد يفشل في التحقق من الخصائص الحقيقية بسبب التقريب الزائد
- إنذارات كاذبة من التقريبات المحافظة
- تتدهور الدقة مع عمق الشبكة (يتراكم خطأ التقريب)
- يتطلب اختياراً دقيقاً للنطاق للتوازن بين الدقة والأداء

### 3.5 تحليل مقارن

تقدم العائلات الثلاث من التقنيات مقايضات مختلفة:

| الجانب | القائم على SMT | القائم على التحسين | التفسير المجرد |
|--------|-----------|-------------------|------------------------|
| **السلامة المنطقية** | ✓ سليم | ✓ سليم (مع الإرخاءات المناسبة) | ✓ سليم |
| **الاكتمال** | ✓ كامل | ✗ غير كامل (إرخاءات) | ✗ غير كامل |
| **قابلية التوسع** | محدودة (آلاف العصبونات) | معتدلة | الأفضل (ملايين المعاملات) |
| **أمثلة مضادة** | ✓ يوفر أمثلة مضادة | أحياناً | ✗ لا أمثلة مضادة |
| **دوال التنشيط** | محدودة (ReLU، المتغيرات) | بشكل أساسي خطية مجزأة | أكثر مرونة |
| **الدقة** | دقيق (عندما يكتمل) | يعتمد على الإرخاء | يعتمد على النطاق |

**الاتجاهات الناشئة**:
- **الأساليب الهجينة**: الجمع بين المناهج (على سبيل المثال، التفسير المجرد مع تحسين SMT)
- **التدريب المعتمد**: تعديل التدريب لإنتاج شبكات أكثر قابلية للتحقق
- **تحسين التجريد**: تحسين التجريدات تلقائياً عندما يفشل التحقق
- **تسريع GPU**: توازي حسابات التحقق

على الرغم من التقدم الكبير، يظل التحقق من الشبكات الحديثة الكبيرة (على سبيل المثال، ResNets على نطاق ImageNet بملايين المعاملات) أمراً صعباً. تتعامل الأدوات الحالية عادةً مع الشبكات التي تحتوي على آلاف إلى عشرات الآلاف من العصبونات للخصائص الكاملة، أو توفر ضمانات غير كاملة للشبكات الأكبر.

---

### Translation Notes

- **Figures referenced:** None (table included in text)
- **Key terms introduced:**
  - ReLU - Rectified Linear Unit (وحدة التصحيح الخطية)
  - Local robustness (المتانة المحلية)
  - Adversarial examples (الأمثلة الخصامية)
  - SMT - Satisfiability Modulo Theories (نظرية الإرضاء بالقياس)
  - Zonotope (zonotope - kept technical term)
  - Polyhedra (المضلعات)
  - MILP - Mixed-Integer Linear Programming (البرمجة الخطية الصحيحة المختلطة)
  - Overapproximation (التقريب الزائد)
  - NP-complete (NP-كامل)
- **Equations:** Mathematical formulas for robustness and optimization
- **Citations:** Multiple tool names and papers (Katz, Singh, etc.)
- **Special handling:** Kept tool names (Reluplex, Marabou, DeepPoly, etc.) in English as standard practice

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check (Key Paragraph)

Arabic → English: "Abstract interpretation approaches apply the theoretical framework described in Section 2.2 to neural networks, overapproximating the set of possible outputs for a given input region using abstract domains."

✓ Semantically equivalent to original
