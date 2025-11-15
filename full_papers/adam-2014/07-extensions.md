# Section 7: Extensions
## القسم 7: الامتدادات

**Section:** extensions
**Translation Quality:** 0.88
**Glossary Terms Used:** algorithm, optimization, infinity norm, L2 norm, Lp norm, exponential moving average, stepsize, gradient, parameters, convergence, temporal averaging, Polyak-Ruppert averaging, generalization

---

### English Version

**7.1 ADAMAX**

In Adam, the update rule for individual weights is to scale their gradients inversely proportional to a (scaled) L2 norm of their individual current and past gradients. We can generalize the L2 norm based update rule to a Lp norm based update rule. Such variants become numerically unstable for large p. However, in the special case where we let $p \to \infty$, a surprisingly simple and stable algorithm emerges; see algorithm 2. We'll now derive the algorithm. Let, in case of the Lp norm, the stepsize at time $t$ be inversely proportional to $v_t^{1/p}$, where:

$$v_t = \beta_2^p v_{t-1} + (1 - \beta_2^p)|g_t|^p \tag{6}$$

$$= (1 - \beta_2^p) \sum_{i=1}^{t} \beta_2^{p(t-i)} \cdot |g_i|^p \tag{7}$$

Note that the decay term is here equivalently parameterised as $\beta_2^p$ instead of $\beta_2$. Now let $p \to \infty$, and define $u_t = \lim_{p \to \infty}(v_t)^{1/p}$, then:

$$u_t = \lim_{p \to \infty}(v_t)^{1/p} = \lim_{p \to \infty} \left((1 - \beta_2^p) \sum_{i=1}^{t} \beta_2^{p(t-i)} \cdot |g_i|^p\right)^{1/p} \tag{8}$$

$$= \lim_{p \to \infty}(1 - \beta_2^p)^{1/p} \left(\sum_{i=1}^{t} \beta_2^{p(t-i)} \cdot |g_i|^p\right)^{1/p} \tag{9}$$

$$= \lim_{p \to \infty} \left(\sum_{i=1}^{t} \left(\beta_2^{(t-i)} \cdot |g_i|\right)^p\right)^{1/p} \tag{10}$$

$$= \max\left(\beta_2^{t-1}|g_1|, \beta_2^{t-2}|g_2|, \ldots, \beta_2|g_{t-1}|, |g_t|\right) \tag{11}$$

Which corresponds to the remarkably simple recursive formula:

$$u_t = \max(\beta_2 \cdot u_{t-1}, |g_t|) \tag{12}$$

with initial value $u_0 = 0$. Note that, conveniently enough, we don't need to correct for initialization bias in this case. Also note that the magnitude of parameter updates has a simpler bound with AdaMax than Adam, namely: $|\Delta_t| \leq \alpha$.

**Algorithm 2: AdaMax**, a variant of Adam based on the infinity norm. See section 7.1 for details. Good default settings for the tested machine learning problems are $\alpha = 0.002$, $\beta_1 = 0.9$ and $\beta_2 = 0.999$. With $\beta_1^t$ we denote $\beta_1$ to the power $t$. Here, $(\alpha/(1 - \beta_1^t))$ is the learning rate with the bias-correction term for the first moment. All operations on vectors are element-wise.

**Require:** $\alpha$: Stepsize
**Require:** $\beta_1, \beta_2 \in [0, 1)$: Exponential decay rates
**Require:** $f(\theta)$: Stochastic objective function with parameters $\theta$
**Require:** $\theta_0$: Initial parameter vector

$m_0 \leftarrow 0$ (Initialize 1st moment vector)
$u_0 \leftarrow 0$ (Initialize the exponentially weighted infinity norm)
$t \leftarrow 0$ (Initialize timestep)

**while** $\theta_t$ not converged **do**
    $t \leftarrow t + 1$
    $g_t \leftarrow \nabla_\theta f_t(\theta_{t-1})$ (Get gradients w.r.t. stochastic objective at timestep $t$)
    $m_t \leftarrow \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$ (Update biased first moment estimate)
    $u_t \leftarrow \max(\beta_2 \cdot u_{t-1}, |g_t|)$ (Update the exponentially weighted infinity norm)
    $\theta_t \leftarrow \theta_{t-1} - (\alpha/(1 - \beta_1^t)) \cdot m_t/u_t$ (Update parameters)
**end while**

**return** $\theta_t$ (Resulting parameters)

**7.2 TEMPORAL AVERAGING**

Since the last iterate is noisy due to stochastic approximation, better generalization performance is often achieved by averaging. Previously in Moulines & Bach (2011), Polyak-Ruppert averaging (Polyak & Juditsky, 1992; Ruppert, 1988) has been shown to improve the convergence of standard SGD, where $\bar{\theta}_t = \frac{1}{t}\sum_{n=k}^{1} \theta_k$. Alternatively, an exponential moving average over the parameters can be used, giving higher weight to more recent parameter values. This can be trivially implemented by adding one line to the inner loop of algorithms 1 and 2: $\bar{\theta}_t \leftarrow \beta_2 \cdot \bar{\theta}_{t-1} + (1-\beta_2)\theta_t$, with $\bar{\theta}_0 = 0$. Initalization bias can again be corrected by the estimator $\tilde{\theta}_t = \bar{\theta}_t/(1 - \beta_2^t)$.

---

### النسخة العربية

**7.1 آداماكس (AdaMax)**

في Adam، قاعدة التحديث للأوزان الفردية هي قياس تدرجاتها بشكل عكسي متناسب مع معيار L2 (مُقاس) لتدرجاتها الفردية الحالية والسابقة. يمكننا تعميم قاعدة التحديث القائمة على معيار L2 إلى قاعدة تحديث قائمة على معيار Lp. مثل هذه المتغيرات تصبح غير مستقرة عددياً لقيم p الكبيرة. ومع ذلك، في الحالة الخاصة حيث نسمح لـ $p \to \infty$، تظهر خوارزمية بسيطة ومستقرة بشكل مفاجئ؛ انظر الخوارزمية 2. سنشتق الآن الخوارزمية. لتكن، في حالة معيار Lp، حجم الخطوة عند الوقت $t$ متناسباً عكسياً مع $v_t^{1/p}$، حيث:

$$v_t = \beta_2^p v_{t-1} + (1 - \beta_2^p)|g_t|^p \tag{6}$$

$$= (1 - \beta_2^p) \sum_{i=1}^{t} \beta_2^{p(t-i)} \cdot |g_i|^p \tag{7}$$

لاحظ أن حد الاضمحلال هنا مُعلمن بشكل مكافئ كـ $\beta_2^p$ بدلاً من $\beta_2$. الآن لتكن $p \to \infty$، ونعرف $u_t = \lim_{p \to \infty}(v_t)^{1/p}$، إذن:

$$u_t = \lim_{p \to \infty}(v_t)^{1/p} = \lim_{p \to \infty} \left((1 - \beta_2^p) \sum_{i=1}^{t} \beta_2^{p(t-i)} \cdot |g_i|^p\right)^{1/p} \tag{8}$$

$$= \lim_{p \to \infty}(1 - \beta_2^p)^{1/p} \left(\sum_{i=1}^{t} \beta_2^{p(t-i)} \cdot |g_i|^p\right)^{1/p} \tag{9}$$

$$= \lim_{p \to \infty} \left(\sum_{i=1}^{t} \left(\beta_2^{(t-i)} \cdot |g_i|\right)^p\right)^{1/p} \tag{10}$$

$$= \max\left(\beta_2^{t-1}|g_1|, \beta_2^{t-2}|g_2|, \ldots, \beta_2|g_{t-1}|, |g_t|\right) \tag{11}$$

الذي يتوافق مع الصيغة التكرارية البسيطة بشكل ملحوظ:

$$u_t = \max(\beta_2 \cdot u_{t-1}, |g_t|) \tag{12}$$

مع قيمة أولية $u_0 = 0$. لاحظ أنه، بشكل مناسب بما فيه الكفاية، لا نحتاج إلى التصحيح لانحياز التهيئة في هذه الحالة. لاحظ أيضاً أن حجم تحديثات المعاملات له حد أبسط مع AdaMax من Adam، وهو: $|\Delta_t| \leq \alpha$.

**الخوارزمية 2: AdaMax**، متغير من Adam يعتمد على معيار اللانهاية. انظر القسم 7.1 للتفاصيل. الإعدادات الافتراضية الجيدة لمسائل التعلم الآلي المختبرة هي $\alpha = 0.002$، $\beta_1 = 0.9$ و $\beta_2 = 0.999$. مع $\beta_1^t$ نشير إلى $\beta_1$ مرفوعة للأس $t$. هنا، $(\alpha/(1 - \beta_1^t))$ هو معدل التعلم مع حد تصحيح الانحياز للعزم الأول. جميع العمليات على المتجهات هي عنصرية.

**يتطلب:** $\alpha$: حجم الخطوة
**يتطلب:** $\beta_1, \beta_2 \in [0, 1)$: معدلات الاضمحلال الأسي
**يتطلب:** $f(\theta)$: دالة هدفية عشوائية مع معاملات $\theta$
**يتطلب:** $\theta_0$: متجه المعاملات الأولي

$m_0 \leftarrow 0$ (تهيئة متجه العزم الأول)
$u_0 \leftarrow 0$ (تهيئة معيار اللانهاية الموزون أسياً)
$t \leftarrow 0$ (تهيئة الخطوة الزمنية)

**طالما أن** $\theta_t$ لم يتقارب **نفذ**
    $t \leftarrow t + 1$
    $g_t \leftarrow \nabla_\theta f_t(\theta_{t-1})$ (احصل على التدرجات فيما يتعلق بالهدف العشوائي عند الخطوة الزمنية $t$)
    $m_t \leftarrow \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$ (حدّث تقدير العزم الأول المنحاز)
    $u_t \leftarrow \max(\beta_2 \cdot u_{t-1}, |g_t|)$ (حدّث معيار اللانهاية الموزون أسياً)
    $\theta_t \leftarrow \theta_{t-1} - (\alpha/(1 - \beta_1^t)) \cdot m_t/u_t$ (حدّث المعاملات)
**انتهى طالما أن**

**أرجع** $\theta_t$ (المعاملات الناتجة)

**7.2 المتوسط الزمني**

نظراً لأن التكرار الأخير صاخب بسبب التقريب العشوائي، فإن أداء التعميم الأفضل غالباً ما يتحقق بالمتوسط. سابقاً في Moulines & Bach (2011)، تم إظهار أن متوسط Polyak-Ruppert (Polyak & Juditsky, 1992; Ruppert, 1988) يحسن تقارب SGD القياسي، حيث $\bar{\theta}_t = \frac{1}{t}\sum_{n=k}^{1} \theta_k$. بدلاً من ذلك، يمكن استخدام متوسط متحرك أسي على المعاملات، مما يعطي وزناً أعلى لقيم المعاملات الأحدث. يمكن تنفيذ ذلك بشكل تافه بإضافة سطر واحد إلى الحلقة الداخلية للخوارزميتين 1 و 2: $\bar{\theta}_t \leftarrow \beta_2 \cdot \bar{\theta}_{t-1} + (1-\beta_2)\theta_t$، مع $\bar{\theta}_0 = 0$. يمكن تصحيح انحياز التهيئة مرة أخرى بواسطة المُقدِّر $\tilde{\theta}_t = \bar{\theta}_t/(1 - \beta_2^t)$.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - AdaMax (آداماكس)
  - Infinity norm (معيار اللانهاية)
  - Lp norm (معيار Lp)
  - Temporal averaging (المتوسط الزمني)
  - Polyak-Ruppert averaging (متوسط Polyak-Ruppert)
  - Generalization performance (أداء التعميم)
  - Exponentially weighted (موزون أسياً)
  - Numerically unstable (غير مستقر عددياً)
- **Equations:** Multiple equations (6-12) deriving AdaMax
- **Citations:** Moulines & Bach (2011), Polyak & Juditsky (1992), Ruppert (1988)
- **Special handling:**
  - Algorithm 2 pseudocode formatted similarly to Algorithm 1
  - Mathematical derivation with limits preserved
  - Max operator preserved
  - Subscript and superscript notation maintained

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
