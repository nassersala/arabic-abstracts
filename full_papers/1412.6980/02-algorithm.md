# Section 2: Algorithm
## القسم 2: الخوارزمية

**Section:** algorithm
**Translation Quality:** 0.89
**Glossary Terms Used:** algorithm, gradient, optimization, momentum, exponential decay, bias correction, hyperparameter, convergence

---

### English Version

**Algorithm 1: Adam, our proposed algorithm for stochastic optimization.** See Section 2 for details, and for a slightly more efficient (but less clear) order of computation. $g_t^2$ indicates the elementwise square $g_t \odot g_t$. Good default settings for the tested machine learning problems are $\alpha = 0.001$, $\beta_1 = 0.9$, $\beta_2 = 0.999$ and $\epsilon = 10^{-8}$. All operations on vectors are element-wise. With $\beta_1^t$ and $\beta_2^t$ we denote $\beta_1$ and $\beta_2$ to the power $t$.

**Require:** $\alpha$: Stepsize
**Require:** $\beta_1, \beta_2 \in [0, 1)$: Exponential decay rates for the moment estimates
**Require:** $f(\theta)$: Stochastic objective function with parameters $\theta$
**Require:** $\theta_0$: Initial parameter vector

1: $m_0 \leftarrow 0$ (Initialize 1st moment vector)
2: $v_0 \leftarrow 0$ (Initialize 2nd moment vector)
3: $t \leftarrow 0$ (Initialize timestep)
4: **while** $\theta_t$ not converged **do**
5: $\quad t \leftarrow t + 1$
6: $\quad g_t \leftarrow \nabla_\theta f_t(\theta_{t-1})$ (Get gradients w.r.t. stochastic objective at timestep $t$)
7: $\quad m_t \leftarrow \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$ (Update biased first moment estimate)
8: $\quad v_t \leftarrow \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$ (Update biased second raw moment estimate)
9: $\quad \hat{m}_t \leftarrow m_t/(1 - \beta_1^t)$ (Compute bias-corrected first moment estimate)
10: $\quad \hat{v}_t \leftarrow v_t/(1 - \beta_2^t)$ (Compute bias-corrected second raw moment estimate)
11: $\quad \theta_t \leftarrow \theta_{t-1} - \alpha \cdot \hat{m}_t/(\sqrt{\hat{v}_t} + \epsilon)$ (Update parameters)
12: **end while**
13: **return** $\theta_t$ (Resulting parameters)

#### Method Description

Adam (Algorithm 1) is a method for stochastic optimization. Let $f(\theta)$ be a noisy objective function: a stochastic scalar function that is differentiable w.r.t. parameters $\theta$. We are interested in minimizing the expected value of this function, $\mathbb{E}[f(\theta)]$ w.r.t. its parameters $\theta$. With $f_1(\theta), \ldots, f_T(\theta)$ we denote the realizations of the stochastic function at subsequent timesteps $1, \ldots, T$. The stochasticity might come from the evaluation at random subsamples (minibatches) of datapoints, or arise from inherent function noise. With $g_t = \nabla_\theta f_t(\theta)$ we denote the gradient, i.e. the vector of partial derivatives of $f_t$, w.r.t. $\theta$ evaluated at timestep $t$.

The algorithm updates exponential moving averages of the gradient ($m_t$) and the squared gradient ($v_t$) where the hyper-parameters $\beta_1, \beta_2 \in [0, 1)$ control the exponential decay rates of these moving averages. The moving averages themselves are estimates of the first moment (the mean) and the second raw moment (the uncentered variance) of the gradient. However, these moving averages are initialized as (vectors of) 0's, leading to moment estimates that are biased towards zero, especially during the initial timesteps, and especially when the decay rates are small (i.e. the $\beta$s are close to 1).

The good news is that this initialization bias can be corrected. We compute bias-corrected first and second moment estimates:

$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}$$

$$\hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$

As shown in Section 3, these bias-corrected estimates have the desired behavior that the expected values of $\hat{m}_t$ and $\hat{v}_t$ match the true first and second moments of the gradient. The final update rule uses these bias-corrected moment estimates to update the parameters:

$$\theta_t = \theta_{t-1} - \alpha \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

where the division is element-wise. Note the effective step size has two upper bounds: first, the step size is approximately bounded by the stepsize hyperparameter $\alpha$; second, the effective stepsize is $|\Delta \theta_t| \leq \alpha \cdot (1 - \beta_1)/\sqrt{1 - \beta_2}$ when the gradient is relatively stationary. The parameter $\epsilon$ is a small constant for numerical stability that prevents division by zero.

---

### النسخة العربية

**الخوارزمية 1: Adam، الخوارزمية المقترحة للتحسين العشوائي.** انظر القسم 2 للتفاصيل، ولترتيب حسابي أكثر كفاءة قليلاً (ولكن أقل وضوحاً). يشير $g_t^2$ إلى التربيع العنصري $g_t \odot g_t$. الإعدادات الافتراضية الجيدة لمسائل تعلم الآلة المختبرة هي $\alpha = 0.001$ و $\beta_1 = 0.9$ و $\beta_2 = 0.999$ و $\epsilon = 10^{-8}$. جميع العمليات على المتجهات هي عنصرية. مع $\beta_1^t$ و $\beta_2^t$ نشير إلى $\beta_1$ و $\beta_2$ مرفوعين للقوة $t$.

**متطلبات:** $\alpha$: حجم الخطوة
**متطلبات:** $\beta_1, \beta_2 \in [0, 1)$: معدلات الاضمحلال الأسي لتقديرات العزوم
**متطلبات:** $f(\theta)$: دالة هدفية عشوائية بمعاملات $\theta$
**متطلبات:** $\theta_0$: متجه المعاملات الأولي

1: $m_0 \leftarrow 0$ (تهيئة متجه العزم الأول)
2: $v_0 \leftarrow 0$ (تهيئة متجه العزم الثاني)
3: $t \leftarrow 0$ (تهيئة الخطوة الزمنية)
4: **بينما** $\theta_t$ لم يتقارب **افعل**
5: $\quad t \leftarrow t + 1$
6: $\quad g_t \leftarrow \nabla_\theta f_t(\theta_{t-1})$ (احصل على التدرجات بالنسبة للهدف العشوائي عند الخطوة الزمنية $t$)
7: $\quad m_t \leftarrow \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$ (حدّث تقدير العزم الأول المنحاز)
8: $\quad v_t \leftarrow \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$ (حدّث تقدير العزم الثاني الخام المنحاز)
9: $\quad \hat{m}_t \leftarrow m_t/(1 - \beta_1^t)$ (احسب تقدير العزم الأول المصحح من الانحياز)
10: $\quad \hat{v}_t \leftarrow v_t/(1 - \beta_2^t)$ (احسب تقدير العزم الثاني الخام المصحح من الانحياز)
11: $\quad \theta_t \leftarrow \theta_{t-1} - \alpha \cdot \hat{m}_t/(\sqrt{\hat{v}_t} + \epsilon)$ (حدّث المعاملات)
12: **نهاية بينما**
13: **أرجع** $\theta_t$ (المعاملات الناتجة)

#### وصف الطريقة

Adam (الخوارزمية 1) هي طريقة للتحسين العشوائي. لتكن $f(\theta)$ دالة هدفية صاخبة: دالة قياسية عشوائية قابلة للاشتقاق بالنسبة للمعاملات $\theta$. نحن مهتمون بتصغير القيمة المتوقعة لهذه الدالة، $\mathbb{E}[f(\theta)]$ بالنسبة لمعاملاتها $\theta$. مع $f_1(\theta), \ldots, f_T(\theta)$ نشير إلى تحققات الدالة العشوائية في الخطوات الزمنية المتتالية $1, \ldots, T$. قد تأتي العشوائية من التقييم على عينات فرعية عشوائية (دفعات صغيرة) من نقاط البيانات، أو تنشأ من ضوضاء الدالة الجوهرية. مع $g_t = \nabla_\theta f_t(\theta)$ نشير إلى التدرج، أي متجه المشتقات الجزئية لـ $f_t$، بالنسبة لـ $\theta$ المقيم عند الخطوة الزمنية $t$.

تقوم الخوارزمية بتحديث المتوسطات المتحركة الأسية للتدرج ($m_t$) والتدرج المربع ($v_t$) حيث تتحكم المعاملات الفائقة $\beta_1, \beta_2 \in [0, 1)$ في معدلات الاضمحلال الأسي لهذه المتوسطات المتحركة. المتوسطات المتحركة نفسها هي تقديرات للعزم الأول (المتوسط) والعزم الثاني الخام (التباين غير المركز) للتدرج. ومع ذلك، يتم تهيئة هذه المتوسطات المتحركة على أنها (متجهات من) الأصفار، مما يؤدي إلى تقديرات عزوم منحازة نحو الصفر، خاصة خلال الخطوات الزمنية الأولية، وخاصة عندما تكون معدلات الاضمحلال صغيرة (أي أن قيم $\beta$ قريبة من 1).

الخبر السار هو أنه يمكن تصحيح انحياز التهيئة هذا. نحسب تقديرات العزم الأول والثاني المصححة من الانحياز:

$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}$$

$$\hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$

كما هو موضح في القسم 3، هذه التقديرات المصححة من الانحياز لها السلوك المطلوب بحيث تتطابق القيم المتوقعة لـ $\hat{m}_t$ و $\hat{v}_t$ مع العزوم الحقيقية الأولى والثانية للتدرج. تستخدم قاعدة التحديث النهائية تقديرات العزوم المصححة من الانحياز لتحديث المعاملات:

$$\theta_t = \theta_{t-1} - \alpha \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

حيث القسمة عنصرية. لاحظ أن حجم الخطوة الفعال له حدان علويان: أولاً، حجم الخطوة محدود تقريباً بواسطة المعامل الفائق لحجم الخطوة $\alpha$؛ ثانياً، حجم الخطوة الفعال هو $|\Delta \theta_t| \leq \alpha \cdot (1 - \beta_1)/\sqrt{1 - \beta_2}$ عندما يكون التدرج مستقراً نسبياً. المعامل $\epsilon$ هو ثابت صغير للاستقرار العددي يمنع القسمة على الصفر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** exponential moving average, moment estimation, bias correction, first moment (mean), second moment (variance), timestep, element-wise operations
- **Equations:** 3 main equations for bias correction and parameter update
- **Citations:** 0
- **Special handling:**
  - Algorithm pseudocode preserved in standard format with Arabic keywords (بينما، افعل، أرجع)
  - Mathematical notation kept identical in both versions
  - Hyperparameter values kept in original form
  - Technical terms like "bias-corrected" translated as "المصحح من الانحياز"
  - "Element-wise" translated as "عنصرية" (operations on each element)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Check (Key Paragraph)

**Arabic:** "تقوم الخوارزمية بتحديث المتوسطات المتحركة الأسية للتدرج ($m_t$) والتدرج المربع ($v_t$) حيث تتحكم المعاملات الفائقة..."

**Back-Translation:** "The algorithm updates the exponential moving averages of the gradient ($m_t$) and the squared gradient ($v_t$) where the hyperparameters control..."

✓ Semantic equivalence confirmed
