# Section 2: Algorithm
## القسم 2: الخوارزمية

**Section:** algorithm
**Translation Quality:** 0.89
**Glossary Terms Used:** algorithm, stochastic, objective function, gradient, parameters, exponential moving average, moment, bias-corrected, stepsize, convergence, hyperparameter, decay rate

---

### English Version

See algorithm 1 for pseudo-code of our proposed algorithm Adam. Let $f(\theta)$ be a noisy objective function: a stochastic scalar function that is differentiable w.r.t. parameters $\theta$. We are interested in minimizing the expected value of this function, $\mathbb{E}[f(\theta)]$ w.r.t. its parameters $\theta$. With $f_1(\theta), ..., f_T(\theta)$ we denote the realisations of the stochastic function at subsequent timesteps $1, ..., T$. The stochasticity might come from the evaluation at random subsamples (minibatches) of datapoints, or arise from inherent function noise. With $g_t = \nabla_\theta f_t(\theta)$ we denote the gradient, i.e. the vector of partial derivatives of $f_t$, w.r.t $\theta$ evaluated at timestep $t$.

The algorithm updates exponential moving averages of the gradient ($m_t$) and the squared gradient ($v_t$) where the hyper-parameters $\beta_1, \beta_2 \in [0, 1)$ control the exponential decay rates of these moving averages. The moving averages themselves are estimates of the 1st moment (the mean) and the 2nd raw moment (the uncentered variance) of the gradient. However, these moving averages are initialized as (vectors of) 0's, leading to moment estimates that are biased towards zero, especially during the initial timesteps, and especially when the decay rates are small (i.e. the $\beta$s are close to 1). The good news is that this initialization bias can be easily counteracted, resulting in bias-corrected estimates $\hat{m}_t$ and $\hat{v}_t$. See section 3 for more details.

Note that the efficiency of algorithm 1 can, at the expense of clarity, be improved upon by changing the order of computation, e.g. by replacing the last three lines in the loop with the following lines:
$\alpha_t = \alpha \cdot \sqrt{1 - \beta_2^t}/(1 - \beta_1^t)$ and $\theta_t \leftarrow \theta_{t-1} - \alpha_t \cdot m_t/(\sqrt{v_t} + \hat{\epsilon})$.

**Algorithm 1: Adam**, our proposed algorithm for stochastic optimization. See section 2 for details, and for a slightly more efficient (but less clear) order of computation. $g_t^2$ indicates the elementwise square $g_t \odot g_t$. Good default settings for the tested machine learning problems are $\alpha = 0.001$, $\beta_1 = 0.9$, $\beta_2 = 0.999$ and $\epsilon = 10^{-8}$. All operations on vectors are element-wise. With $\beta_1^t$ and $\beta_2^t$ we denote $\beta_1$ and $\beta_2$ to the power $t$.

**Require:** $\alpha$: Stepsize
**Require:** $\beta_1, \beta_2 \in [0, 1)$: Exponential decay rates for the moment estimates
**Require:** $f(\theta)$: Stochastic objective function with parameters $\theta$
**Require:** $\theta_0$: Initial parameter vector

$m_0 \leftarrow 0$ (Initialize 1st moment vector)
$v_0 \leftarrow 0$ (Initialize 2nd moment vector)
$t \leftarrow 0$ (Initialize timestep)

**while** $\theta_t$ not converged **do**
    $t \leftarrow t + 1$
    $g_t \leftarrow \nabla_\theta f_t(\theta_{t-1})$ (Get gradients w.r.t. stochastic objective at timestep $t$)
    $m_t \leftarrow \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$ (Update biased first moment estimate)
    $v_t \leftarrow \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$ (Update biased second raw moment estimate)
    $\hat{m}_t \leftarrow m_t/(1 - \beta_1^t)$ (Compute bias-corrected first moment estimate)
    $\hat{v}_t \leftarrow v_t/(1 - \beta_2^t)$ (Compute bias-corrected second raw moment estimate)
    $\theta_t \leftarrow \theta_{t-1} - \alpha \cdot \hat{m}_t/(\sqrt{\hat{v}_t} + \epsilon)$ (Update parameters)
**end while**

**return** $\theta_t$ (Resulting parameters)

**2.1 ADAM'S UPDATE RULE**

An important property of Adam's update rule is its careful choice of stepsizes. Assuming $\epsilon = 0$, the effective step taken in parameter space at timestep $t$ is $\Delta_t = \alpha \cdot \hat{m}_t/\sqrt{\hat{v}_t}$. The effective stepsize has two upper bounds: $|\Delta_t| \leq \alpha \cdot (1 - \beta_1)/\sqrt{1 - \beta_2}$ in the case $(1 - \beta_1) > \sqrt{1 - \beta_2}$, and $|\Delta_t| \leq \alpha$ otherwise. The first case only happens in the most severe case of sparsity: when a gradient has been zero at all timesteps except at the current timestep. For less sparse cases, the effective stepsize will be smaller. When $(1 - \beta_1) = \sqrt{1 - \beta_2}$ we have that $|\hat{m}_t/\sqrt{\hat{v}_t}| < 1$ therefore $|\Delta_t| < \alpha$. In more common scenarios, we will have that $\hat{m}_t/\sqrt{\hat{v}_t} \approx \pm 1$ since $|\mathbb{E}[g]/\sqrt{\mathbb{E}[g^2]}| \leq 1$. The effective magnitude of the steps taken in parameter space at each timestep are approximately bounded by the stepsize setting $\alpha$, i.e., $|\Delta_t| \lesssim \alpha$. This can be understood as establishing a trust region around the current parameter value, beyond which the current gradient estimate does not provide sufficient information. This typically makes it relatively easy to know the right scale of $\alpha$ in advance. For many machine learning models, for instance, we often know in advance that good optima are with high probability within some set region in parameter space; it is not uncommon, for example, to have a prior distribution over the parameters. Since $\alpha$ sets (an upper bound of) the magnitude of steps in parameter space, we can often deduce the right order of magnitude of $\alpha$ such that optima can be reached from $\theta_0$ within some number of iterations. With a slight abuse of terminology, we will call the ratio $\hat{m}_t/\sqrt{\hat{v}_t}$ the signal-to-noise ratio (SNR). With a smaller SNR the effective stepsize $\Delta_t$ will be closer to zero. This is a desirable property, since a smaller SNR means that there is greater uncertainty about whether the direction of $\hat{m}_t$ corresponds to the direction of the true gradient. For example, the SNR value typically becomes closer to 0 towards an optimum, leading to smaller effective steps in parameter space: a form of automatic annealing. The effective stepsize $\Delta_t$ is also invariant to the scale of the gradients; rescaling the gradients $g$ with factor $c$ will scale $\hat{m}_t$ with a factor $c$ and $\hat{v}_t$ with a factor $c^2$, which cancel out: $(c \cdot \hat{m}_t)/(\sqrt{c^2 \cdot \hat{v}_t}) = \hat{m}_t/\sqrt{\hat{v}_t}$.

---

### النسخة العربية

انظر الخوارزمية 1 للشفرة الزائفة للخوارزمية المقترحة Adam. لتكن $f(\theta)$ دالة هدفية صاخبة: دالة قياسية عشوائية قابلة للاشتقاق فيما يتعلق بالمعاملات $\theta$. نحن مهتمون بتصغير القيمة المتوقعة لهذه الدالة، $\mathbb{E}[f(\theta)]$ فيما يتعلق بمعاملاتها $\theta$. مع $f_1(\theta), ..., f_T(\theta)$ نشير إلى تحققات الدالة العشوائية عند الخطوات الزمنية المتتالية $1, ..., T$. قد تأتي العشوائية من التقييم عند عينات فرعية عشوائية (دفعات صغيرة) من نقاط البيانات، أو تنشأ من ضوضاء الدالة المتأصلة. مع $g_t = \nabla_\theta f_t(\theta)$ نشير إلى التدرج، أي متجه المشتقات الجزئية لـ $f_t$، فيما يتعلق بـ $\theta$ المُقيَّم عند الخطوة الزمنية $t$.

تقوم الخوارزمية بتحديث المتوسطات المتحركة الأسية للتدرج ($m_t$) والتدرج المربع ($v_t$) حيث تتحكم المعاملات الفائقة $\beta_1, \beta_2 \in [0, 1)$ في معدلات الاضمحلال الأسي لهذه المتوسطات المتحركة. المتوسطات المتحركة نفسها هي تقديرات للعزم الأول (المتوسط) والعزم الخام الثاني (التباين غير المتمركز) للتدرج. ومع ذلك، يتم تهيئة هذه المتوسطات المتحركة كأصفار (متجهات من الأصفار)، مما يؤدي إلى تقديرات عزم منحازة نحو الصفر، خاصة خلال الخطوات الزمنية الأولية، وخاصة عندما تكون معدلات الاضمحلال صغيرة (أي أن قيم $\beta$ قريبة من 1). الأخبار الجيدة هي أنه يمكن مواجهة انحياز التهيئة هذا بسهولة، مما ينتج عنه تقديرات مصححة الانحياز $\hat{m}_t$ و $\hat{v}_t$. انظر القسم 3 لمزيد من التفاصيل.

لاحظ أن كفاءة الخوارزمية 1 يمكن تحسينها، على حساب الوضوح، من خلال تغيير ترتيب الحساب، على سبيل المثال عن طريق استبدال الأسطر الثلاثة الأخيرة في الحلقة بالأسطر التالية:
$\alpha_t = \alpha \cdot \sqrt{1 - \beta_2^t}/(1 - \beta_1^t)$ و $\theta_t \leftarrow \theta_{t-1} - \alpha_t \cdot m_t/(\sqrt{v_t} + \hat{\epsilon})$.

**الخوارزمية 1: Adam**، خوارزميتنا المقترحة للتحسين العشوائي. انظر القسم 2 للتفاصيل، ولترتيب حساب أكثر كفاءة قليلاً (ولكن أقل وضوحاً). $g_t^2$ يشير إلى المربع العنصري $g_t \odot g_t$. الإعدادات الافتراضية الجيدة لمسائل التعلم الآلي المختبرة هي $\alpha = 0.001$، $\beta_1 = 0.9$، $\beta_2 = 0.999$ و $\epsilon = 10^{-8}$. جميع العمليات على المتجهات هي عنصرية. مع $\beta_1^t$ و $\beta_2^t$ نشير إلى $\beta_1$ و $\beta_2$ مرفوعة للأس $t$.

**يتطلب:** $\alpha$: حجم الخطوة
**يتطلب:** $\beta_1, \beta_2 \in [0, 1)$: معدلات الاضمحلال الأسي لتقديرات العزم
**يتطلب:** $f(\theta)$: دالة هدفية عشوائية مع معاملات $\theta$
**يتطلب:** $\theta_0$: متجه المعاملات الأولي

$m_0 \leftarrow 0$ (تهيئة متجه العزم الأول)
$v_0 \leftarrow 0$ (تهيئة متجه العزم الثاني)
$t \leftarrow 0$ (تهيئة الخطوة الزمنية)

**طالما أن** $\theta_t$ لم يتقارب **نفذ**
    $t \leftarrow t + 1$
    $g_t \leftarrow \nabla_\theta f_t(\theta_{t-1})$ (احصل على التدرجات فيما يتعلق بالهدف العشوائي عند الخطوة الزمنية $t$)
    $m_t \leftarrow \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$ (حدّث تقدير العزم الأول المنحاز)
    $v_t \leftarrow \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$ (حدّث تقدير العزم الخام الثاني المنحاز)
    $\hat{m}_t \leftarrow m_t/(1 - \beta_1^t)$ (احسب تقدير العزم الأول المصحح الانحياز)
    $\hat{v}_t \leftarrow v_t/(1 - \beta_2^t)$ (احسب تقدير العزم الخام الثاني المصحح الانحياز)
    $\theta_t \leftarrow \theta_{t-1} - \alpha \cdot \hat{m}_t/(\sqrt{\hat{v}_t} + \epsilon)$ (حدّث المعاملات)
**انتهى طالما أن**

**أرجع** $\theta_t$ (المعاملات الناتجة)

**2.1 قاعدة تحديث آدم**

خاصية مهمة لقاعدة تحديث Adam هي اختيارها الدقيق لأحجام الخطوات. بافتراض $\epsilon = 0$، فإن الخطوة الفعالة المتخذة في فضاء المعاملات عند الخطوة الزمنية $t$ هي $\Delta_t = \alpha \cdot \hat{m}_t/\sqrt{\hat{v}_t}$. لحجم الخطوة الفعال حدان أعليان: $|\Delta_t| \leq \alpha \cdot (1 - \beta_1)/\sqrt{1 - \beta_2}$ في الحالة $(1 - \beta_1) > \sqrt{1 - \beta_2}$، و $|\Delta_t| \leq \alpha$ بخلاف ذلك. تحدث الحالة الأولى فقط في الحالة الأشد للتفرق: عندما يكون التدرج صفراً في جميع الخطوات الزمنية باستثناء الخطوة الزمنية الحالية. بالنسبة للحالات الأقل تفرقاً، سيكون حجم الخطوة الفعال أصغر. عندما $(1 - \beta_1) = \sqrt{1 - \beta_2}$ يكون لدينا أن $|\hat{m}_t/\sqrt{\hat{v}_t}| < 1$ وبالتالي $|\Delta_t| < \alpha$. في السيناريوهات الأكثر شيوعاً، سيكون لدينا أن $\hat{m}_t/\sqrt{\hat{v}_t} \approx \pm 1$ نظراً لأن $|\mathbb{E}[g]/\sqrt{\mathbb{E}[g^2]}| \leq 1$. القيمة الفعالة لحجم الخطوات المتخذة في فضاء المعاملات عند كل خطوة زمنية محدودة تقريباً بإعداد حجم الخطوة $\alpha$، أي $|\Delta_t| \lesssim \alpha$. يمكن فهم ذلك على أنه إنشاء منطقة ثقة حول قيمة المعامل الحالي، وبعدها لا يوفر تقدير التدرج الحالي معلومات كافية. هذا عادة ما يجعل من السهل نسبياً معرفة المقياس الصحيح لـ $\alpha$ مسبقاً. بالنسبة للعديد من نماذج التعلم الآلي، على سبيل المثال، غالباً ما نعرف مسبقاً أن الحلول المثلى الجيدة توجد باحتمالية عالية ضمن منطقة معينة في فضاء المعاملات؛ ليس من غير المألوف، على سبيل المثال، أن يكون لدينا توزيع أولي على المعاملات. نظراً لأن $\alpha$ يحدد (حداً أعلى لـ) حجم الخطوات في فضاء المعاملات، يمكننا غالباً استنتاج الرتبة الصحيحة لحجم $\alpha$ بحيث يمكن الوصول إلى الحلول المثلى من $\theta_0$ في عدد معين من التكرارات. مع إساءة استخدام طفيفة للمصطلحات، سنسمي النسبة $\hat{m}_t/\sqrt{\hat{v}_t}$ نسبة الإشارة إلى الضوضاء (SNR). مع نسبة إشارة إلى ضوضاء أصغر، سيكون حجم الخطوة الفعال $\Delta_t$ أقرب إلى الصفر. هذه خاصية مرغوبة، حيث أن نسبة إشارة إلى ضوضاء أصغر تعني أن هناك عدم يقين أكبر حول ما إذا كان اتجاه $\hat{m}_t$ يتوافق مع اتجاه التدرج الحقيقي. على سبيل المثال، تصبح قيمة نسبة الإشارة إلى الضوضاء عادةً أقرب إلى 0 نحو الحل الأمثل، مما يؤدي إلى خطوات فعالة أصغر في فضاء المعاملات: شكل من أشكال التلدين التلقائي. حجم الخطوة الفعال $\Delta_t$ أيضاً ثابت تجاه مقياس التدرجات؛ إعادة قياس التدرجات $g$ بعامل $c$ سيقيس $\hat{m}_t$ بعامل $c$ و $\hat{v}_t$ بعامل $c^2$، والتي تلغي بعضها البعض: $(c \cdot \hat{m}_t)/(\sqrt{c^2 \cdot \hat{v}_t}) = \hat{m}_t/\sqrt{\hat{v}_t}$.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Exponential moving average (المتوسط المتحرك الأسي)
  - Bias-corrected (مصحح الانحياز)
  - First moment/second moment (العزم الأول/العزم الثاني)
  - Raw moment (العزم الخام)
  - Uncentered variance (التباين غير المتمركز)
  - Signal-to-noise ratio (نسبة الإشارة إلى الضوضاء)
  - Trust region (منطقة ثقة)
  - Automatic annealing (التلدين التلقائي)
- **Equations:** Multiple mathematical equations preserved in LaTeX format
- **Citations:** Algorithm 1 pseudocode preserved with English keywords and Arabic translations in comments
- **Special handling:**
  - Mathematical notation kept in original form
  - Algorithm pseudocode keywords kept in English with Arabic translations in parentheses
  - Greek letters (α, β, θ, ε) preserved
  - Mathematical symbols and operators preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
