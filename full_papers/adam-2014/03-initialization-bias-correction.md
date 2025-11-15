# Section 3: Initialization Bias Correction
## القسم 3: تصحيح انحياز التهيئة

**Section:** initialization-bias-correction
**Translation Quality:** 0.87
**Glossary Terms Used:** bias correction, initialization, moment estimate, exponential moving average, decay rate, gradient, second moment, first moment, stationary

---

### English Version

As explained in section 2, Adam utilizes initialization bias correction terms. We will here derive the term for the second moment estimate; the derivation for the first moment estimate is completely analogous. Let $g$ be the gradient of the stochastic objective $f$, and we wish to estimate its second raw moment (uncentered variance) using an exponential moving average of the squared gradient, with decay rate $\beta_2$. Let $g_1, ..., g_T$ be the gradients at subsequent timesteps, each a draw from an underlying gradient distribution $g_t \sim p(g_t)$. Let us initialize the exponential moving average as $v_0 = 0$ (a vector of zeros). First note that the update at timestep $t$ of the exponential moving average $v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$ (where $g_t^2$ indicates the elementwise square $g_t \odot g_t$) can be written as a function of the gradients at all previous timesteps:

$$v_t = (1 - \beta_2) \sum_{i=1}^{t} \beta_2^{t-i} \cdot g_i^2 \tag{1}$$

We wish to know how $\mathbb{E}[v_t]$, the expected value of the exponential moving average at timestep $t$, relates to the true second moment $\mathbb{E}[g_t^2]$, so we can correct for the discrepancy between the two. Taking expectations of the left-hand and right-hand sides of eq. (1):

$$\mathbb{E}[v_t] = \mathbb{E}\left[(1 - \beta_2) \sum_{i=1}^{t} \beta_2^{t-i} \cdot g_i^2\right] \tag{2}$$

$$= \mathbb{E}[g_t^2] \cdot (1 - \beta_2) \sum_{i=1}^{t} \beta_2^{t-i} + \zeta \tag{3}$$

$$= \mathbb{E}[g_t^2] \cdot (1 - \beta_2^t) + \zeta \tag{4}$$

where $\zeta = 0$ if the true second moment $\mathbb{E}[g_i^2]$ is stationary; otherwise $\zeta$ can be kept small since the exponential decay rate $\beta_1$ can (and should) be chosen such that the exponential moving average assigns small weights to gradients too far in the past. What is left is the term $(1 - \beta_2^t)$ which is caused by initializing the running average with zeros. In algorithm 1 we therefore divide by this term to correct the initialization bias.

In case of sparse gradients, for a reliable estimate of the second moment one needs to average over many gradients by chosing a small value of $\beta_2$; however it is exactly this case of small $\beta_2$ where a lack of initialisation bias correction would lead to initial steps that are much larger.

---

### النسخة العربية

كما هو موضح في القسم 2، تستخدم Adam مصطلحات تصحيح انحياز التهيئة. سنشتق هنا المصطلح لتقدير العزم الثاني؛ الاشتقاق لتقدير العزم الأول مماثل تماماً. لتكن $g$ تدرج الهدف العشوائي $f$، ونريد تقدير عزمه الخام الثاني (التباين غير المتمركز) باستخدام متوسط متحرك أسي للتدرج المربع، بمعدل اضمحلال $\beta_2$. لتكن $g_1, ..., g_T$ التدرجات عند الخطوات الزمنية المتتالية، كل منها سحب من توزيع تدرج أساسي $g_t \sim p(g_t)$. لنهيئ المتوسط المتحرك الأسي كـ $v_0 = 0$ (متجه من الأصفار). لاحظ أولاً أن التحديث عند الخطوة الزمنية $t$ للمتوسط المتحرك الأسي $v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$ (حيث $g_t^2$ يشير إلى المربع العنصري $g_t \odot g_t$) يمكن كتابته كدالة للتدرجات في جميع الخطوات الزمنية السابقة:

$$v_t = (1 - \beta_2) \sum_{i=1}^{t} \beta_2^{t-i} \cdot g_i^2 \tag{1}$$

نريد معرفة كيف ترتبط $\mathbb{E}[v_t]$، القيمة المتوقعة للمتوسط المتحرك الأسي عند الخطوة الزمنية $t$، بالعزم الثاني الحقيقي $\mathbb{E}[g_t^2]$، حتى نتمكن من تصحيح التناقض بينهما. بأخذ التوقعات للطرف الأيسر والأيمن من المعادلة (1):

$$\mathbb{E}[v_t] = \mathbb{E}\left[(1 - \beta_2) \sum_{i=1}^{t} \beta_2^{t-i} \cdot g_i^2\right] \tag{2}$$

$$= \mathbb{E}[g_t^2] \cdot (1 - \beta_2) \sum_{i=1}^{t} \beta_2^{t-i} + \zeta \tag{3}$$

$$= \mathbb{E}[g_t^2] \cdot (1 - \beta_2^t) + \zeta \tag{4}$$

حيث $\zeta = 0$ إذا كان العزم الثاني الحقيقي $\mathbb{E}[g_i^2]$ ثابتاً؛ وإلا فيمكن إبقاء $\zeta$ صغيراً نظراً لأن معدل الاضمحلال الأسي $\beta_1$ يمكن (ويجب) اختياره بحيث يخصص المتوسط المتحرك الأسي أوزاناً صغيرة للتدرجات البعيدة جداً في الماضي. ما تبقى هو المصطلح $(1 - \beta_2^t)$ الذي ينتج عن تهيئة المتوسط الجاري بالأصفار. في الخوارزمية 1 لذلك نقسم على هذا المصطلح لتصحيح انحياز التهيئة.

في حالة التدرجات المتفرقة، للحصول على تقدير موثوق للعزم الثاني يحتاج المرء إلى حساب المتوسط على العديد من التدرجات عن طريق اختيار قيمة صغيرة لـ $\beta_2$؛ ومع ذلك فإن هذه الحالة بالضبط من $\beta_2$ الصغيرة حيث إن عدم تصحيح انحياز التهيئة سيؤدي إلى خطوات أولية أكبر بكثير.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Initialization bias (انحياز التهيئة)
  - Bias correction (تصحيح الانحياز)
  - Expected value (القيمة المتوقعة)
  - Stationary (ثابت)
  - Running average (المتوسط الجاري)
  - Elementwise square (المربع العنصري)
- **Equations:** 4 numbered equations (1-4) preserved in LaTeX format
- **Citations:** None
- **Special handling:**
  - Mathematical derivation preserved with all equations
  - Greek letters and mathematical symbols maintained
  - Summation notation preserved
  - Probability notation $\sim$ and $\mathbb{E}$ preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87
