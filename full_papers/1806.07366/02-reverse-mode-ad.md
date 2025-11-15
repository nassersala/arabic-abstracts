# Section 2: Reverse-mode Automatic Differentiation of ODE Solutions
## القسم 2: التفاضل الآلي بالوضع العكسي لحلول المعادلات التفاضلية العادية

**Section:** methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** backpropagation, gradient, derivative, automatic differentiation, adjoint, loss function, optimization, ODE solver, memory, training

---

### English Version

The main technical difficulty in training continuous-depth networks is performing reverse-mode differentiation (also known as backpropagation) through the ODE solver. Differentiating through the operations of the solver incurs a high memory cost and introduces additional numerical error.

We treat the ODE solver as a black box, and compute gradients using the adjoint sensitivity method (Pontryagin et al., 1962). This approach computes gradients by solving a second, augmented ODE backwards in time, and is applicable to all ODE solvers. This approach scales linearly with problem size, has low memory cost, and explicitly controls numerical error.

**Consider optimizing a scalar-valued loss function $L()$, whose input is the result of an ODE solver:**

$$L(z(t_1)) = L\left(z(t_0) + \int_{t_0}^{t_1} f(z(t), t, \theta) dt\right) = L(\text{ODESolve}(z(t_0), f, t_0, t_1, \theta))$$

To optimize $L$, we require gradients with respect to $\theta$. The first step is to determining how the gradient of the loss depends on the hidden state $z(t)$ at each instant. This quantity is called the adjoint $a(t) = \partial L / \partial z(t)$. Its dynamics are given by another ODE, which can be thought of as the instantaneous analog of the chain rule:

$$\frac{da(t)}{dt} = -a(t)^T \frac{\partial f(z(t), t, \theta)}{\partial z}$$

We can compute $\partial L / \partial z(t_0)$ by another call to an ODE solver. This solver must run backwards, starting from the initial value of $\partial L / \partial z(t_1)$. One complication is that solving this ODE requires the knowing value of $z(t)$ along its entire trajectory. However, we can simply recompute $z(t)$ backwards in time together with the adjoint, starting from its final value $z(t_1)$.

**Computing gradients with respect to the parameters $\theta$** requires evaluating a third integral, which depends on both $z(t)$ and $a(t)$:

$$\frac{dL}{d\theta} = -\int_{t_1}^{t_0} a(t)^T \frac{\partial f(z(t), t, \theta)}{\partial \theta} dt$$

The vector-Jacobian products $a(t)^T \frac{\partial f}{\partial z}$ and $a(t)^T \frac{\partial f}{\partial \theta}$ in the previous two equations can be efficiently evaluated by automatic differentiation, at a time cost similar to that of evaluating $f$. All integrals can be computed in a single call to an ODE solver, by concatenating the original state, the adjoint, and the other partial derivatives into a single vector. Algorithm 1 shows how to construct the augmented dynamics, and call an ODE solver to compute all gradients at once.

**Algorithm 1 Reverse-mode derivative of an ODE initial value problem**

Input: dynamics parameters $\theta$, start time $t_0$, stop time $t_1$, final state $z(t_1)$, loss gradient $\partial L / \partial z(t_1)$

Define the augmented state:
$$s(t) = [z(t), a(t), \partial L/\partial \theta(t), \partial L/\partial t_0(t)]$$

Define the augmented dynamics:
$$\frac{ds(t)}{dt} = f_{\text{aug}}(s(t), t, \theta) = [f(z(t), t, \theta), -a(t)^T \frac{\partial f}{\partial z}, -a(t)^T \frac{\partial f}{\partial \theta}, -a(t)^T \frac{\partial f}{\partial t}]$$

Initialize: $s(t_1) = [z(t_1), \partial L/\partial z(t_1), \mathbf{0}_{\theta}, 0]$

Compute: $s(t_0) = \text{ODESolve}(s(t_1), f_{\text{aug}}, t_1, t_0, \theta)$

Return: $[\partial L/\partial z(t_0), \partial L/\partial \theta, \partial L/\partial t_0] = s(t_0)[2:4]$

Most ODE solvers don't allow a user to pass in the backward ODE which will be used to compute gradients. Differentiable ODE solvers exist, but suffer from high memory use, or require manually deriving Jacobians. In contrast, we wrap an existing ODE solver with a single function that automatically constructs the necessary dynamics.

This approach allows use of any ODE solver, not backpropagating through the solver itself. This drastically reduces memory requirements. All intermediate quantities of the forward pass can be computed from $z(t_1)$, we do not need to store them. Computational cost is also reduced: the forward and backward ODE can be solved in a single call.

---

### النسخة العربية

الصعوبة التقنية الرئيسية في تدريب الشبكات ذات العمق المستمر هي إجراء التفاضل بالوضع العكسي (المعروف أيضاً باسم الانتشار العكسي) عبر حلال المعادلات التفاضلية العادية. يؤدي التفاضل عبر عمليات الحلال إلى تكلفة ذاكرة عالية ويقدم خطأ عددي إضافي.

نتعامل مع حلال المعادلات التفاضلية العادية كصندوق أسود، ونحسب التدرجات باستخدام طريقة حساسية المرافق (Pontryagin et al., 1962). تحسب هذه الطريقة التدرجات بحل معادلة تفاضلية عادية ثانية معززة بشكل عكسي في الزمن، وهي قابلة للتطبيق على جميع حلالات المعادلات التفاضلية العادية. تتوسع هذه الطريقة خطياً مع حجم المشكلة، ولها تكلفة ذاكرة منخفضة، وتتحكم بشكل صريح في الخطأ العددي.

**لنفكر في تحسين دالة خسارة قيمة قياسية $L()$، والتي يكون مدخلها نتيجة حلال معادلة تفاضلية عادية:**

$$L(z(t_1)) = L\left(z(t_0) + \int_{t_0}^{t_1} f(z(t), t, \theta) dt\right) = L(\text{ODESolve}(z(t_0), f, t_0, t_1, \theta))$$

لتحسين $L$، نحتاج إلى التدرجات بالنسبة لـ $\theta$. الخطوة الأولى هي تحديد كيفية اعتماد تدرج الخسارة على الحالة المخفية $z(t)$ في كل لحظة. تسمى هذه الكمية بالمرافق $a(t) = \partial L / \partial z(t)$. يتم إعطاء ديناميكياتها بواسطة معادلة تفاضلية عادية أخرى، والتي يمكن اعتبارها النظير اللحظي لقاعدة السلسلة:

$$\frac{da(t)}{dt} = -a(t)^T \frac{\partial f(z(t), t, \theta)}{\partial z}$$

يمكننا حساب $\partial L / \partial z(t_0)$ من خلال استدعاء آخر لحلال المعادلات التفاضلية العادية. يجب أن يعمل هذا الحلال بشكل عكسي، بدءاً من القيمة الابتدائية لـ $\partial L / \partial z(t_1)$. أحد التعقيدات هو أن حل هذه المعادلة التفاضلية العادية يتطلب معرفة قيمة $z(t)$ على طول مسارها بالكامل. ومع ذلك، يمكننا ببساطة إعادة حساب $z(t)$ بشكل عكسي في الزمن مع المرافق، بدءاً من قيمته النهائية $z(t_1)$.

**يتطلب حساب التدرجات بالنسبة للمعاملات $\theta$** تقييم تكامل ثالث، والذي يعتمد على كل من $z(t)$ و $a(t)$:

$$\frac{dL}{d\theta} = -\int_{t_1}^{t_0} a(t)^T \frac{\partial f(z(t), t, \theta)}{\partial \theta} dt$$

يمكن تقييم جداءات المتجه-جاكوبيان $a(t)^T \frac{\partial f}{\partial z}$ و $a(t)^T \frac{\partial f}{\partial \theta}$ في المعادلتين السابقتين بكفاءة بواسطة التفاضل الآلي، بتكلفة زمنية مشابهة لتكلفة تقييم $f$. يمكن حساب جميع التكاملات في استدعاء واحد لحلال المعادلات التفاضلية العادية، من خلال دمج الحالة الأصلية والمرافق والمشتقات الجزئية الأخرى في متجه واحد. تُظهر الخوارزمية 1 كيفية بناء الديناميكيات المعززة، واستدعاء حلال المعادلات التفاضلية العادية لحساب جميع التدرجات دفعة واحدة.

**الخوارزمية 1: المشتقة بالوضع العكسي لمسألة القيمة الابتدائية للمعادلة التفاضلية العادية**

المدخلات: معاملات الديناميكيات $\theta$، وقت البداية $t_0$، وقت التوقف $t_1$، الحالة النهائية $z(t_1)$، تدرج الخسارة $\partial L / \partial z(t_1)$

تعريف الحالة المعززة:
$$s(t) = [z(t), a(t), \partial L/\partial \theta(t), \partial L/\partial t_0(t)]$$

تعريف الديناميكيات المعززة:
$$\frac{ds(t)}{dt} = f_{\text{aug}}(s(t), t, \theta) = [f(z(t), t, \theta), -a(t)^T \frac{\partial f}{\partial z}, -a(t)^T \frac{\partial f}{\partial \theta}, -a(t)^T \frac{\partial f}{\partial t}]$$

التهيئة: $s(t_1) = [z(t_1), \partial L/\partial z(t_1), \mathbf{0}_{\theta}, 0]$

الحساب: $s(t_0) = \text{ODESolve}(s(t_1), f_{\text{aug}}, t_1, t_0, \theta)$

الإرجاع: $[\partial L/\partial z(t_0), \partial L/\partial \theta, \partial L/\partial t_0] = s(t_0)[2:4]$

معظم حلالات المعادلات التفاضلية العادية لا تسمح للمستخدم بتمرير المعادلة التفاضلية العادية العكسية التي سيتم استخدامها لحساب التدرجات. توجد حلالات معادلات تفاضلية عادية قابلة للتفاضل، لكنها تعاني من استخدام ذاكرة عالي، أو تتطلب اشتقاق الجاكوبيان يدوياً. في المقابل، نحن نلف حلال معادلات تفاضلية عادية موجود بدالة واحدة تبني الديناميكيات اللازمة تلقائياً.

تتيح هذه الطريقة استخدام أي حلال للمعادلات التفاضلية العادية، دون الانتشار العكسي عبر الحلال نفسه. هذا يقلل بشكل كبير من متطلبات الذاكرة. يمكن حساب جميع الكميات الوسيطة للمرور الأمامي من $z(t_1)$، ولا نحتاج إلى تخزينها. يتم أيضاً تقليل التكلفة الحسابية: يمكن حل المعادلة التفاضلية العادية الأمامية والعكسية في استدعاء واحد.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** adjoint sensitivity method, augmented dynamics, vector-Jacobian product, reverse-mode differentiation, chain rule
- **Equations:** 5 main equations including adjoint dynamics
- **Citations:** Pontryagin et al. (1962)
- **Special handling:** Algorithm 1 translated with code structure preserved, mathematical derivations carefully translated

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.88
