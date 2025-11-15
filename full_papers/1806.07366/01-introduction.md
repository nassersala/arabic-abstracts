# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** neural network, deep learning, residual, derivative, memory, continuous, hidden state, differential equation, backpropagation, ODE solver

---

### English Version

Models like Residual Networks (ResNets), Recurrent Neural Networks (RNNs), and Normalizing Flows build complicated transformations by composing a sequence of transformations to a hidden state:

$$h_{t+1} = h_t + f(h_t, \theta_t)$$

where $t \in \{0, \ldots, T\}$ and $h_t \in \mathbb{R}^D$ is the hidden state at layer $t$. These iterative updates can be seen as an Euler discretization of a continuous transformation.

What happens as we add more layers and take smaller steps? In the limit, we parameterize the continuous dynamics of hidden units using an ordinary differential equation (ODE) specified by a neural network:

$$\frac{dh(t)}{dt} = f(h(t), t, \theta)$$

Starting from the input layer $h(0)$, we can define the output layer $h(T)$ to be the solution to this ODE initial value problem at some time $T$. This value can be computed by a black-box differential equation solver, which evaluates the hidden unit dynamics $f$ wherever necessary to determine the solution with the desired accuracy.

**Figure 1 comparison:** A Residual network defines a discrete sequence of finite transformations, whereas ODE networks define a vector field, which continuously transforms the state. Both: Circles represent evaluation locations.

Defining and evaluating models using ODE solvers has several benefits:

**Memory efficiency.** In Section 2, we show how to compute gradients of a scalar-valued loss with respect to all inputs of any ODE solver, without backpropagating through the operations of the solver. Not storing any intermediate quantities of the forward pass allows us to train our models with constant memory cost as a function of depth, a major bottleneck of training deep models.

**Adaptive computation.** Modern ODE solvers provide guarantees about the growth of approximation error, monitor the level of error, and adapt their evaluation strategy on the fly to achieve the requested level of accuracy. This allows the cost of evaluating a model to scale with problem complexity. After training, accuracy can be reduced for real-time or low-power applications.

**Scalable and invertible normalizing flows.** An unexpected side-benefit of continuous transformations is that the change of variables formula becomes easier to compute. In Section 4, we derive this result and use it to construct a new class of invertible density models that avoids the single-unit bottleneck of normalizing flows, and can be trained directly by maximum likelihood.

**Continuous time-series models.** Unlike RNNs which require discretizing observation and emission intervals, continuously-defined dynamics can naturally incorporate data which arrives at arbitrary times. In Section 5, we construct and demonstrate such a model.

**Contribution.** We show how to train continuous-depth networks by introducing a method to compute gradients through an ODE solver. We perform experiments demonstrating the memory efficiency, parameter efficiency, and scalability of these models. We also construct continuous normalizing flows and time-series latent variable models having these properties, and introduce and generative model for irregularly-sampled time series.

---

### النسخة العربية

تبني النماذج مثل الشبكات المتبقية (ResNets) والشبكات العصبية التكرارية (RNNs) وتدفقات التطبيع (Normalizing Flows) تحويلات معقدة من خلال تركيب تسلسل من التحويلات على حالة مخفية:

$$h_{t+1} = h_t + f(h_t, \theta_t)$$

حيث $t \in \{0, \ldots, T\}$ و $h_t \in \mathbb{R}^D$ هي الحالة المخفية عند الطبقة $t$. يمكن النظر إلى هذه التحديثات التكرارية على أنها تقطيع أويلر (Euler discretization) لتحويل مستمر.

ماذا يحدث عندما نضيف المزيد من الطبقات ونأخذ خطوات أصغر؟ في الحد الأقصى، نحدد معاملات الديناميكيات المستمرة للوحدات المخفية باستخدام معادلة تفاضلية عادية (ODE) محددة بواسطة شبكة عصبية:

$$\frac{dh(t)}{dt} = f(h(t), t, \theta)$$

ابتداءً من طبقة الإدخال $h(0)$، يمكننا تعريف طبقة الإخراج $h(T)$ على أنها الحل لمسألة القيمة الابتدائية لهذه المعادلة التفاضلية العادية عند وقت $T$ معين. يمكن حساب هذه القيمة بواسطة حلال معادلات تفاضلية صندوق أسود، والذي يقيم ديناميكيات الوحدة المخفية $f$ حيثما كان ذلك ضرورياً لتحديد الحل بالدقة المطلوبة.

**مقارنة الشكل 1:** تحدد الشبكة المتبقية تسلسلاً منفصلاً من التحويلات المحدودة، بينما تحدد شبكات المعادلات التفاضلية العادية حقل متجه، والذي يحول الحالة بشكل مستمر. كلاهما: تمثل الدوائر مواقع التقييم.

إن تعريف وتقييم النماذج باستخدام حلالات المعادلات التفاضلية العادية له عدة فوائد:

**كفاءة الذاكرة.** في القسم 2، نوضح كيفية حساب التدرجات لدالة خسارة قيمة قياسية بالنسبة لجميع مدخلات أي حلال للمعادلات التفاضلية العادية، دون الانتشار العكسي عبر عمليات الحلال. عدم تخزين أي كميات وسيطة من المرور الأمامي يسمح لنا بتدريب نماذجنا بتكلفة ذاكرة ثابتة كدالة للعمق، وهو عنق الزجاجة الرئيسي لتدريب النماذج العميقة.

**الحوسبة التكيفية.** توفر حلالات المعادلات التفاضلية العادية الحديثة ضمانات حول نمو خطأ التقريب، وتراقب مستوى الخطأ، وتكيف استراتيجية التقييم الخاصة بها أثناء التنفيذ لتحقيق مستوى الدقة المطلوب. هذا يسمح لتكلفة تقييم النموذج بالتوسع مع تعقيد المشكلة. بعد التدريب، يمكن تقليل الدقة للتطبيقات في الوقت الفعلي أو ذات الطاقة المنخفضة.

**تدفقات التطبيع القابلة للتوسع والعكس.** فائدة جانبية غير متوقعة من التحويلات المستمرة هي أن صيغة تغيير المتغيرات تصبح أسهل في الحساب. في القسم 4، نشتق هذه النتيجة ونستخدمها لبناء فئة جديدة من نماذج الكثافة القابلة للعكس التي تتجنب عنق الزجاجة أحادي الوحدة لتدفقات التطبيع، ويمكن تدريبها مباشرة بأقصى احتمالية.

**نماذج السلاسل الزمنية المستمرة.** على عكس الشبكات العصبية التكرارية التي تتطلب تقطيع فترات الملاحظة والانبعاث، يمكن للديناميكيات المحددة بشكل مستمر أن تدمج بشكل طبيعي البيانات التي تصل في أوقات تعسفية. في القسم 5، نبني ونوضح مثل هذا النموذج.

**المساهمة.** نوضح كيفية تدريب الشبكات ذات العمق المستمر من خلال تقديم طريقة لحساب التدرجات عبر حلال المعادلات التفاضلية العادية. نجري تجارب توضح كفاءة الذاكرة وكفاءة المعاملات وقابلية التوسع لهذه النماذج. نبني أيضاً تدفقات التطبيع المستمرة ونماذج المتغيرات الكامنة للسلاسل الزمنية التي تتمتع بهذه الخصائص، ونقدم نموذجاً توليدياً للسلاسل الزمنية ذات العينات غير المنتظمة.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** neural ODEs, continuous depth, ODE solver, adjoint method (referenced), continuous normalizing flows, hidden state dynamics
- **Equations:** 2 main ODEs
- **Citations:** References to ResNets, RNNs, Normalizing Flows
- **Special handling:** Mathematical equations kept in LaTeX, residual network structure explained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
