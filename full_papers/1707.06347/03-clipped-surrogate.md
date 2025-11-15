# Section 3: Clipped Surrogate Objective
## القسم 3: الدالة الهدفية البديلة المقصوصة

**Section:** Core Methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** surrogate objective, probability ratio, clipping, hyperparameter, optimization, conservative policy iteration, pessimistic bound, lower bound

---

### English Version

Let $r_t(\theta)$ denote the probability ratio $r_t(\theta) = \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)}$, so $r(\theta_\text{old}) = 1$. TRPO maximizes a "surrogate" objective

$$L^{CPI}(\theta) = \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)} \hat{A}_t \right] = \hat{\mathbb{E}}_t \left[ r_t(\theta) \hat{A}_t \right]. \tag{6}$$

The superscript CPI refers to conservative policy iteration [KL02], where this objective was proposed. Without a constraint, maximization of $L^{CPI}$ would lead to an excessively large policy update; hence, we now consider how to modify the objective, to penalize changes to the policy that move $r_t(\theta)$ away from 1.

The main objective we propose is the following:

$$L^{CLIP}(\theta) = \hat{\mathbb{E}}_t \left[ \min(r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t) \right] \tag{7}$$

where epsilon is a hyperparameter, say, $\epsilon = 0.2$. The motivation for this objective is as follows. The first term inside the min is $L^{CPI}$. The second term, $\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t$, modifies the surrogate objective by clipping the probability ratio, which removes the incentive for moving $r_t$ outside of the interval $[1-\epsilon, 1+\epsilon]$. Finally, we take the minimum of the clipped and unclipped objective, so the final objective is a lower bound (i.e., a pessimistic bound) on the unclipped objective. With this scheme, we only ignore the change in probability ratio when it would make the objective improve, and we include it when it makes the objective worse. Note that $L^{CLIP}(\theta) = L^{CPI}(\theta)$ to first order around $\theta_\text{old}$ (i.e., where $r = 1$), however, they become different as $\theta$ moves away from $\theta_\text{old}$. Figure 1 plots a single term (i.e., a single $t$) in $L^{CLIP}$; note that the probability ratio $r$ is clipped at $1-\epsilon$ or $1+\epsilon$ depending on whether the advantage is positive or negative.

**Figure 1:** Plots showing one term (i.e., a single timestep) of the surrogate function $L^{CLIP}$ as a function of the probability ratio $r$, for positive advantages (left) and negative advantages (right). The red circle on each plot shows the starting point for the optimization, i.e., $r = 1$. Note that $L^{CLIP}$ sums many of these terms.

[Left plot: Shows $L^{CLIP}$ vs $r$ for $A > 0$, with clipping at $1+\epsilon$]
[Right plot: Shows $L^{CLIP}$ vs $r$ for $A < 0$, with clipping at $1-\epsilon$]

Figure 2 provides another source of intuition about the surrogate objective $L^{CLIP}$. It shows how several objectives vary as we interpolate along the policy update direction, obtained by proximal policy optimization (the algorithm we will introduce shortly) on a continuous control problem. We can see that $L^{CLIP}$ is a lower bound on $L^{CPI}$, with a penalty for having too large of a policy update.

**Figure 2:** Surrogate objectives, as we interpolate between the initial policy parameter $\theta_\text{old}$, and the updated policy parameter, which we compute after one iteration of PPO. The updated policy has a KL divergence of about 0.02 from the initial policy, and this is the point at which $L^{CLIP}$ is maximal. This plot corresponds to the first policy update on the Hopper-v1 problem, using hyperparameters provided in Section 6.1.

[Plot shows curves for: $\hat{\mathbb{E}}_t[KL_t]$, $L^{CPI} = \hat{\mathbb{E}}_t[r_t A_t]$, $\hat{\mathbb{E}}_t[\text{clip}(r_t, 1-\epsilon, 1+\epsilon)A_t]$, and $L^{CLIP} = \hat{\mathbb{E}}_t[\min(r_t A_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon)A_t)]$]

---

### النسخة العربية

لنفرض أن $r_t(\theta)$ يشير إلى نسبة الاحتمالية $r_t(\theta) = \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)}$، بحيث $r(\theta_\text{old}) = 1$. يعظم TRPO دالة هدفية "بديلة"

$$L^{CPI}(\theta) = \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)} \hat{A}_t \right] = \hat{\mathbb{E}}_t \left[ r_t(\theta) \hat{A}_t \right]. \tag{6}$$

يشير الحرف العلوي CPI إلى التكرار المحافظ للسياسة [KL02]، حيث تم اقتراح هذه الدالة الهدفية. بدون قيد، سيؤدي تعظيم $L^{CPI}$ إلى تحديث سياسة كبير بشكل مفرط؛ وبالتالي، ننظر الآن في كيفية تعديل الدالة الهدفية، لمعاقبة التغييرات في السياسة التي تبعد $r_t(\theta)$ عن 1.

الدالة الهدفية الرئيسية التي نقترحها هي التالية:

$$L^{CLIP}(\theta) = \hat{\mathbb{E}}_t \left[ \min(r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t) \right] \tag{7}$$

حيث إبسيلون هو معامل فائق، على سبيل المثال، $\epsilon = 0.2$. الدافع لهذه الدالة الهدفية هو كما يلي. الحد الأول داخل min هو $L^{CPI}$. الحد الثاني، $\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t$، يعدل الدالة الهدفية البديلة من خلال قص نسبة الاحتمالية، مما يزيل الحافز لتحريك $r_t$ خارج الفترة $[1-\epsilon, 1+\epsilon]$. أخيراً، نأخذ الحد الأدنى من الدالة الهدفية المقصوصة وغير المقصوصة، بحيث تكون الدالة الهدفية النهائية حداً أدنى (أي حداً متشائماً) على الدالة الهدفية غير المقصوصة. مع هذا المخطط، نتجاهل فقط التغيير في نسبة الاحتمالية عندما يحسن الدالة الهدفية، ونضمنه عندما يجعل الدالة الهدفية أسوأ. لاحظ أن $L^{CLIP}(\theta) = L^{CPI}(\theta)$ من الدرجة الأولى حول $\theta_\text{old}$ (أي عندما $r = 1$)، ومع ذلك، يصبحان مختلفين عندما يبتعد $\theta$ عن $\theta_\text{old}$. يرسم الشكل 1 حداً واحداً (أي $t$ واحد) في $L^{CLIP}$؛ لاحظ أن نسبة الاحتمالية $r$ يتم قصها عند $1-\epsilon$ أو $1+\epsilon$ اعتماداً على ما إذا كانت الأفضلية موجبة أم سالبة.

**الشكل 1:** رسومات توضح حداً واحداً (أي خطوة زمنية واحدة) من الدالة البديلة $L^{CLIP}$ كدالة لنسبة الاحتمالية $r$، للأفضليات الموجبة (اليسار) والأفضليات السالبة (اليمين). تُظهر الدائرة الحمراء في كل رسم نقطة البداية للتحسين، أي $r = 1$. لاحظ أن $L^{CLIP}$ تجمع العديد من هذه الحدود.

[الرسم الأيسر: يوضح $L^{CLIP}$ مقابل $r$ عندما $A > 0$، مع القص عند $1+\epsilon$]
[الرسم الأيمن: يوضح $L^{CLIP}$ مقابل $r$ عندما $A < 0$، مع القص عند $1-\epsilon$]

يوفر الشكل 2 مصدراً آخر للحدس حول الدالة الهدفية البديلة $L^{CLIP}$. يوضح كيف تتغير عدة دوال هدفية عندما نستكمل على طول اتجاه تحديث السياسة، الذي تم الحصول عليه من خلال تحسين السياسة التقريبية (الخوارزمية التي سنقدمها قريباً) على مشكلة تحكم مستمر. يمكننا أن نرى أن $L^{CLIP}$ هو حد أدنى على $L^{CPI}$، مع عقوبة على وجود تحديث سياسة كبير جداً.

**الشكل 2:** الدوال الهدفية البديلة، عندما نستكمل بين معامل السياسة الأولي $\theta_\text{old}$، ومعامل السياسة المحدث، الذي نحسبه بعد تكرار واحد من PPO. للسياسة المحدثة تباعد KL حوالي 0.02 من السياسة الأولية، وهذه هي النقطة التي يكون عندها $L^{CLIP}$ أقصى. يتوافق هذا الرسم مع تحديث السياسة الأول على مشكلة Hopper-v1، باستخدام المعاملات الفائقة المقدمة في القسم 6.1.

[الرسم يوضح منحنيات لـ: $\hat{\mathbb{E}}_t[KL_t]$، $L^{CPI} = \hat{\mathbb{E}}_t[r_t A_t]$، $\hat{\mathbb{E}}_t[\text{clip}(r_t, 1-\epsilon, 1+\epsilon)A_t]$، و $L^{CLIP} = \hat{\mathbb{E}}_t[\min(r_t A_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon)A_t)]$]

---

### Translation Notes

- **Figures referenced:** Figure 1 (two plots for positive/negative advantages), Figure 2 (surrogate objectives comparison)
- **Key terms introduced:**
  - probability ratio - نسبة الاحتمالية
  - conservative policy iteration - التكرار المحافظ للسياسة
  - clip/clipping - قص
  - hyperparameter - معامل فائق
  - incentive - حافز
  - interval - فترة
  - minimum - الحد الأدنى
  - pessimistic bound - حد متشائم
  - lower bound - حد أدنى
  - unclipped - غير مقصوصة
  - first order - الدرجة الأولى
  - interpolate - نستكمل
  - policy update direction - اتجاه تحديث السياسة
- **Equations:** 2 equations (6-7)
- **Citations:** [KL02]
- **Special handling:**
  - Preserved all mathematical notation and LaTeX equations
  - Translated figure captions in detail
  - Kept function names (clip, min, max) in English within equations
  - Explained the clipping mechanism in clear Arabic
  - Described visual content of figures for reference

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
