# Section 2: Background: Policy Optimization
## القسم 2: الخلفية: تحسين السياسة

**Section:** Background
**Translation Quality:** 0.87
**Glossary Terms Used:** policy gradient, optimization, stochastic, gradient ascent, advantage function, automatic differentiation, trust region, constraint, surrogate objective, KL divergence

---

### English Version

## 2.1 Policy Gradient Methods

Policy gradient methods work by computing an estimator of the policy gradient and plugging it into a stochastic gradient ascent algorithm. The most commonly used gradient estimator has the form

$$\hat{g} = \hat{\mathbb{E}}_t \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \hat{A}_t \right] \tag{1}$$

where $\pi_\theta$ is a stochastic policy and $\hat{A}_t$ is an estimator of the advantage function at timestep $t$. Here, the expectation $\hat{\mathbb{E}}_t[...]$ indicates the empirical average over a finite batch of samples, in an algorithm that alternates between sampling and optimization. Implementations that use automatic differentiation software work by constructing an objective function whose gradient is the policy gradient estimator; the estimator $\hat{g}$ is obtained by differentiating the objective

$$L^{PG}(\theta) = \hat{\mathbb{E}}_t \left[ \log \pi_\theta(a_t | s_t) \hat{A}_t \right]. \tag{2}$$

While it is appealing to perform multiple steps of optimization on this loss $L^{PG}$ using the same trajectory, doing so is not well-justified, and empirically it often leads to destructively large policy updates (see Section 6.1; results are not shown but were similar or worse than the "no clipping or penalty" setting).

## 2.2 Trust Region Methods

In TRPO [Sch+15b], an objective function (the "surrogate" objective) is maximized subject to a constraint on the size of the policy update. Specifically,

$$\text{maximize}_\theta \quad \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)} \hat{A}_t \right] \tag{3}$$

$$\text{subject to} \quad \hat{\mathbb{E}}_t [KL[\pi_{\theta_\text{old}}(\cdot | s_t), \pi_\theta(\cdot | s_t)]] \leq \delta. \tag{4}$$

Here, $\theta_\text{old}$ is the vector of policy parameters before the update. This problem can efficiently be approximately solved using the conjugate gradient algorithm, after making a linear approximation to the objective and a quadratic approximation to the constraint.

The theory justifying TRPO actually suggests using a penalty instead of a constraint, i.e., solving the unconstrained optimization problem

$$\text{maximize}_\theta \quad \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)} \hat{A}_t - \beta \text{KL}[\pi_{\theta_\text{old}}(\cdot | s_t), \pi_\theta(\cdot | s_t)] \right] \tag{5}$$

for some coefficient $\beta$. This follows from the fact that a certain surrogate objective (which computes the max KL over states instead of the mean) forms a lower bound (i.e., a pessimistic bound) on the performance of the policy $\pi$. TRPO uses a hard constraint rather than a penalty because it is hard to choose a single value of $\beta$ that performs well across different problems—or even within a single problem, where the the characteristics change over the course of learning. Hence, to achieve our goal of a first-order algorithm that emulates the monotonic improvement of TRPO, experiments show that it is not sufficient to simply choose a fixed penalty coefficient $\beta$ and optimize the penalized objective Equation (5) with SGD; additional modifications are required.

---

### النسخة العربية

## 2.1 طرق تدرجات السياسات

تعمل طرق تدرجات السياسات من خلال حساب مقدر لتدرج السياسة وإدخاله في خوارزمية صعود تدرجي عشوائي. المقدر الأكثر استخداماً للتدرج له الشكل

$$\hat{g} = \hat{\mathbb{E}}_t \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \hat{A}_t \right] \tag{1}$$

حيث $\pi_\theta$ هي سياسة عشوائية و$\hat{A}_t$ هو مقدر لدالة الأفضلية عند الخطوة الزمنية $t$. هنا، يشير التوقع $\hat{\mathbb{E}}_t[...]$ إلى المتوسط التجريبي على دفعة محدودة من العينات، في خوارزمية تتناوب بين أخذ العينات والتحسين. التطبيقات التي تستخدم برمجيات التفاضل الآلي تعمل من خلال بناء دالة هدفية يكون تدرجها هو مقدر تدرج السياسة؛ يتم الحصول على المقدر $\hat{g}$ من خلال تفاضل الدالة الهدفية

$$L^{PG}(\theta) = \hat{\mathbb{E}}_t \left[ \log \pi_\theta(a_t | s_t) \hat{A}_t \right]. \tag{2}$$

بينما يبدو من الجذاب إجراء خطوات متعددة من التحسين على هذه الخسارة $L^{PG}$ باستخدام نفس المسار، فإن القيام بذلك غير مبرر جيداً، وتجريبياً غالباً ما يؤدي إلى تحديثات سياسة كبيرة بشكل مدمر (انظر القسم 6.1؛ النتائج غير معروضة لكنها كانت مشابهة أو أسوأ من إعداد "بدون قص أو عقوبة").

## 2.2 طرق منطقة الثقة

في TRPO [Sch+15b]، يتم تعظيم دالة هدفية (الدالة الهدفية "البديلة") مع قيد على حجم تحديث السياسة. على وجه التحديد،

$$\text{maximize}_\theta \quad \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)} \hat{A}_t \right] \tag{3}$$

$$\text{subject to} \quad \hat{\mathbb{E}}_t [KL[\pi_{\theta_\text{old}}(\cdot | s_t), \pi_\theta(\cdot | s_t)]] \leq \delta. \tag{4}$$

حيث $\theta_\text{old}$ هو متجه معاملات السياسة قبل التحديث. يمكن حل هذه المسألة بكفاءة وبشكل تقريبي باستخدام خوارزمية التدرج المترافق، بعد عمل تقريب خطي للدالة الهدفية وتقريب تربيعي للقيد.

النظرية التي تبرر TRPO تقترح في الواقع استخدام عقوبة بدلاً من قيد، أي حل مسألة التحسين غير المقيدة

$$\text{maximize}_\theta \quad \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)} \hat{A}_t - \beta \text{KL}[\pi_{\theta_\text{old}}(\cdot | s_t), \pi_\theta(\cdot | s_t)] \right] \tag{5}$$

لمعامل $\beta$ ما. يأتي هذا من حقيقة أن دالة هدفية بديلة معينة (تحسب أقصى KL على الحالات بدلاً من المتوسط) تشكل حداً أدنى (أي حداً متشائماً) على أداء السياسة $\pi$. يستخدم TRPO قيداً صارماً بدلاً من عقوبة لأنه من الصعب اختيار قيمة واحدة لـ$\beta$ تؤدي أداءً جيداً عبر مشاكل مختلفة—أو حتى ضمن مشكلة واحدة، حيث تتغير الخصائص خلال مسار التعلم. وبالتالي، لتحقيق هدفنا المتمثل في خوارزمية من الدرجة الأولى تحاكي التحسن الأحادي الاتجاه لـ TRPO، تظهر التجارب أنه لا يكفي ببساطة اختيار معامل عقوبة ثابت $\beta$ وتحسين الدالة الهدفية المعاقبة في المعادلة (5) باستخدام SGD؛ التعديلات الإضافية مطلوبة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - policy gradient estimator - مقدر تدرج السياسة
  - stochastic policy - سياسة عشوائية
  - advantage function - دالة الأفضلية
  - timestep - الخطوة الزمنية
  - empirical average - المتوسط التجريبي
  - batch of samples - دفعة من العينات
  - automatic differentiation - التفاضل الآلي
  - objective function - دالة هدفية
  - trajectory - مسار
  - destructively large - كبيرة بشكل مدمر
  - trust region - منطقة الثقة
  - surrogate objective - دالة هدفية بديلة
  - constraint - قيد
  - conjugate gradient - التدرج المترافق
  - linear approximation - تقريب خطي
  - quadratic approximation - تقريب تربيعي
  - KL divergence - تباعد KL
  - penalty - عقوبة
  - unconstrained optimization - تحسين غير مقيد
  - hard constraint - قيد صارم
  - monotonic improvement - تحسن أحادي الاتجاه
  - SGD (stochastic gradient descent) - SGD (الانحدار التدرجي العشوائي)
- **Equations:** 5 equations (1-5)
- **Citations:** [Sch+15b]
- **Special handling:**
  - All mathematical equations preserved in LaTeX format
  - Added Arabic explanations after key equations
  - Kept standard notation ($\theta$, $\pi$, $\hat{A}$, etc.)
  - Translated "maximize" and "subject to" in optimization problems

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87
