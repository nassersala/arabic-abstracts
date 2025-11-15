# Section 5: Related Work
## القسم 5: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.88
**Glossary Terms Used:** optimization, algorithm, stochastic, gradient, momentum, sparse gradients, curvature, preconditioner, natural gradient descent, Fisher information matrix, bias correction, convergence

---

### English Version

Optimization methods bearing a direct relation to Adam are RMSProp (Tieleman & Hinton, 2012; Graves, 2013) and AdaGrad (Duchi et al., 2011); these relationships are discussed below. Other stochastic optimization methods include vSGD (Schaul et al., 2012), AdaDelta (Zeiler, 2012) and the natural Newton method from Roux & Fitzgibbon (2010), all setting stepsizes by estimating curvature from first-order information. The Sum-of-Functions Optimizer (SFO) (Sohl-Dickstein et al., 2014) is a quasi-Newton method based on minibatches, but (unlike Adam) has memory requirements linear in the number of minibatch partitions of a dataset, which is often infeasible on memory-constrained systems such as a GPU. Like natural gradient descent (NGD) (Amari, 1998), Adam employs a preconditioner that adapts to the geometry of the data, since $\hat{v}_t$ is an approximation to the diagonal of the Fisher information matrix (Pascanu & Bengio, 2013); however, Adam's preconditioner (like AdaGrad's) is more conservative in its adaption than vanilla NGD by preconditioning with the square root of the inverse of the diagonal Fisher information matrix approximation.

**RMSProp:** An optimization method closely related to Adam is RMSProp (Tieleman & Hinton, 2012). A version with momentum has sometimes been used (Graves, 2013). There are a few important differences between RMSProp with momentum and Adam: RMSProp with momentum generates its parameter updates using a momentum on the rescaled gradient, whereas Adam updates are directly estimated using a running average of first and second moment of the gradient. RMSProp also lacks a bias-correction term; this matters most in case of a value of $\beta_2$ close to 1 (required in case of sparse gradients), since in that case not correcting the bias leads to very large stepsizes and often divergence, as we also empirically demonstrate in section 6.4.

**AdaGrad:** An algorithm that works well for sparse gradients is AdaGrad (Duchi et al., 2011). Its basic version updates parameters as $\theta_{t+1} = \theta_t - \alpha \cdot g_t/\sqrt{\sum_{i=1}^{t} g_t^2}$. Note that if we choose $\beta_2$ to be infinitesimally close to 1 from below, then $\lim_{\beta_2 \to 1} \hat{v}_t = t^{-1} \cdot \sum_{i=1}^{t} g_t^2$. AdaGrad corresponds to a version of Adam with $\beta_1 = 0$, infinitesimal $(1 - \beta_2)$ and a replacement of $\alpha$ by an annealed version $\alpha_t = \alpha \cdot t^{-1/2}$, namely $\theta_t - \alpha \cdot t^{-1/2} \cdot \hat{m}_t/\sqrt{\lim_{\beta_2 \to 1} \hat{v}_t} = \theta_t - \alpha \cdot t^{-1/2} \cdot g_t/\sqrt{t^{-1} \cdot \sum_{i=1}^{t} g_t^2} = \theta_t - \alpha \cdot g_t/\sqrt{\sum_{i=1}^{t} g_t^2}$. Note that this direct correspondence between Adam and Adagrad does not hold when removing the bias-correction terms; without bias correction, like in RMSProp, a $\beta_2$ infinitesimally close to 1 would lead to infinitely large bias, and infinitely large parameter updates.

---

### النسخة العربية

طرق التحسين التي تحمل علاقة مباشرة بـ Adam هي RMSProp (Tieleman & Hinton, 2012; Graves, 2013) و AdaGrad (Duchi et al., 2011)؛ تُناقش هذه العلاقات أدناه. تشمل طرق التحسين العشوائية الأخرى vSGD (Schaul et al., 2012)، وAdaDelta (Zeiler, 2012) وطريقة نيوتن الطبيعية من Roux & Fitzgibbon (2010)، وجميعها تحدد أحجام الخطوات عن طريق تقدير الانحناء من معلومات الدرجة الأولى. محسِّن مجموع الدوال (SFO) (Sohl-Dickstein et al., 2014) هو طريقة شبه نيوتن تعتمد على الدفعات الصغيرة، ولكن (على عكس Adam) لديها متطلبات ذاكرة خطية في عدد تقسيمات الدفعات الصغيرة لمجموعة البيانات، وهو ما يكون غالباً غير ممكن على الأنظمة المقيدة بالذاكرة مثل GPU. مثل الانحدار التدرجي الطبيعي (NGD) (Amari, 1998)، تستخدم Adam مُكيِّفاً مسبقاً يتكيف مع هندسة البيانات، نظراً لأن $\hat{v}_t$ هو تقريب لقطر مصفوفة معلومات فيشر (Pascanu & Bengio, 2013)؛ ومع ذلك، فإن المُكيِّف المسبق لـ Adam (مثل AdaGrad) أكثر تحفظاً في تكيفه من NGD البسيط من خلال التكييف المسبق بالجذر التربيعي لمعكوس تقريب مصفوفة معلومات فيشر القطرية.

**RMSProp:** طريقة تحسين ذات صلة وثيقة بـ Adam هي RMSProp (Tieleman & Hinton, 2012). تم استخدام نسخة مع الزخم في بعض الأحيان (Graves, 2013). هناك بعض الاختلافات المهمة بين RMSProp مع الزخم و Adam: RMSProp مع الزخم ينتج تحديثات معاملاته باستخدام زخم على التدرج المُعاد قياسه، بينما تُقدَّر تحديثات Adam مباشرة باستخدام متوسط جاري للعزم الأول والثاني للتدرج. كما أن RMSProp يفتقر إلى حد تصحيح الانحياز؛ وهذا مهم بشكل خاص في حالة قيمة $\beta_2$ قريبة من 1 (المطلوبة في حالة التدرجات المتفرقة)، حيث أنه في تلك الحالة عدم تصحيح الانحياز يؤدي إلى أحجام خطوات كبيرة جداً وغالباً ما يحدث تباعد، كما نُظهر تجريبياً أيضاً في القسم 6.4.

**AdaGrad:** خوارزمية تعمل بشكل جيد مع التدرجات المتفرقة هي AdaGrad (Duchi et al., 2011). نسختها الأساسية تحدِّث المعاملات كـ $\theta_{t+1} = \theta_t - \alpha \cdot g_t/\sqrt{\sum_{i=1}^{t} g_t^2}$. لاحظ أنه إذا اخترنا $\beta_2$ ليكون قريباً جداً من 1 من الأسفل، فإن $\lim_{\beta_2 \to 1} \hat{v}_t = t^{-1} \cdot \sum_{i=1}^{t} g_t^2$. تتوافق AdaGrad مع نسخة من Adam مع $\beta_1 = 0$، و$(1 - \beta_2)$ متناهي في الصغر واستبدال $\alpha$ بنسخة مُلدَّنة $\alpha_t = \alpha \cdot t^{-1/2}$، أي $\theta_t - \alpha \cdot t^{-1/2} \cdot \hat{m}_t/\sqrt{\lim_{\beta_2 \to 1} \hat{v}_t} = \theta_t - \alpha \cdot t^{-1/2} \cdot g_t/\sqrt{t^{-1} \cdot \sum_{i=1}^{t} g_t^2} = \theta_t - \alpha \cdot g_t/\sqrt{\sum_{i=1}^{t} g_t^2}$. لاحظ أن هذا التطابق المباشر بين Adam و Adagrad لا ينطبق عند إزالة حدود تصحيح الانحياز؛ بدون تصحيح الانحياز، مثل RMSProp، فإن $\beta_2$ قريباً جداً من 1 سيؤدي إلى انحياز كبير بشكل لا نهائي، وتحديثات معاملات كبيرة بشكل لا نهائي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Preconditioner (مُكيِّف مسبق)
  - Fisher information matrix (مصفوفة معلومات فيشر)
  - Natural gradient descent (الانحدار التدرجي الطبيعي)
  - Quasi-Newton method (طريقة شبه نيوتن)
  - Curvature (الانحناء)
  - Annealed (مُلدَّن)
  - Vanilla (البسيط)
  - Divergence (تباعد)
  - Infinitesimally (متناهي في الصغر)
- **Equations:** Several mathematical equations showing relationships between algorithms
- **Citations:** Multiple citations (Tieleman & Hinton 2012, Graves 2013, Duchi et al. 2011, etc.)
- **Special handling:**
  - Algorithm names (RMSProp, AdaGrad, vSGD, AdaDelta, SFO, NGD) kept in English
  - Mathematical derivations preserved with LaTeX
  - Limit notation preserved
  - Technical comparisons between algorithms carefully translated

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
