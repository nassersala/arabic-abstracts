# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** diffusion probabilistic models, forward process, reverse process, Markov chain, Gaussian transition, variational bound, parameterization, neural network

---

### English Version

Diffusion probabilistic models are latent variable models of the form $p_\theta(\mathbf{x}_0) := \int p_\theta(\mathbf{x}_{0:T}) d\mathbf{x}_{1:T}$, where $\mathbf{x}_1, \ldots, \mathbf{x}_T$ are latents of the same dimensionality as the data $\mathbf{x}_0 \sim q(\mathbf{x}_0)$. The joint distribution $p_\theta(\mathbf{x}_{0:T})$ is called the reverse process, and it is defined as a Markov chain with learned Gaussian transitions starting at $p(\mathbf{x}_T) = \mathcal{N}(\mathbf{x}_T; \mathbf{0}, \mathbf{I})$:

$$p_\theta(\mathbf{x}_{0:T}) := p(\mathbf{x}_T) \prod_{t=1}^T p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t), \quad p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t) := \mathcal{N}(\mathbf{x}_{t-1}; \boldsymbol{\mu}_\theta(\mathbf{x}_t, t), \boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t))$$

What distinguishes diffusion models from other types of latent variable models is that the approximate posterior $q(\mathbf{x}_{1:T} | \mathbf{x}_0)$, called the forward process or diffusion process, is fixed to a Markov chain that gradually adds Gaussian noise to the data according to a variance schedule $\beta_1, \ldots, \beta_T$:

$$q(\mathbf{x}_{1:T} | \mathbf{x}_0) := \prod_{t=1}^T q(\mathbf{x}_t | \mathbf{x}_{t-1}), \quad q(\mathbf{x}_t | \mathbf{x}_{t-1}) := \mathcal{N}(\mathbf{x}_t; \sqrt{1 - \beta_t} \mathbf{x}_{t-1}, \beta_t \mathbf{I})$$

Training is performed by optimizing the usual variational bound on negative log likelihood:

$$\mathbb{E}[-\log p_\theta(\mathbf{x}_0)] \leq \mathbb{E}_q\left[-\log \frac{p_\theta(\mathbf{x}_{0:T})}{q(\mathbf{x}_{1:T} | \mathbf{x}_0)}\right] =: L$$

The forward process variances $\beta_t$ can be learned by reparameterization or held constant as hyperparameters, and expressivity of the reverse process is ensured in part by the choice of Gaussian conditionals in $p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t)$, because both processes have the same functional form when $\beta_t$ are small.

A notable property of the forward process is that it admits sampling $\mathbf{x}_t$ at an arbitrary timestep $t$ in closed form: using the notation $\alpha_t := 1 - \beta_t$ and $\bar{\alpha}_t := \prod_{s=1}^t \alpha_s$, we have

$$q(\mathbf{x}_t | \mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t; \sqrt{\bar{\alpha}_t} \mathbf{x}_0, (1 - \bar{\alpha}_t) \mathbf{I})$$

Efficient training is therefore possible by optimizing random terms of $L$ with stochastic gradient descent.

---

### النسخة العربية

نماذج الانتشار الاحتمالية هي نماذج متغيرات كامنة من الشكل $p_\theta(\mathbf{x}_0) := \int p_\theta(\mathbf{x}_{0:T}) d\mathbf{x}_{1:T}$، حيث $\mathbf{x}_1, \ldots, \mathbf{x}_T$ هي متغيرات كامنة لها نفس البُعد الذي تمتلكه البيانات $\mathbf{x}_0 \sim q(\mathbf{x}_0)$. يُسمى التوزيع المشترك $p_\theta(\mathbf{x}_{0:T})$ بالعملية العكسية، وهو مُعرّف كسلسلة ماركوف مع انتقالات غاوسية متعلمة تبدأ من $p(\mathbf{x}_T) = \mathcal{N}(\mathbf{x}_T; \mathbf{0}, \mathbf{I})$:

$$p_\theta(\mathbf{x}_{0:T}) := p(\mathbf{x}_T) \prod_{t=1}^T p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t), \quad p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t) := \mathcal{N}(\mathbf{x}_{t-1}; \boldsymbol{\mu}_\theta(\mathbf{x}_t, t), \boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t))$$

ما يميز نماذج الانتشار عن الأنواع الأخرى من نماذج المتغيرات الكامنة هو أن التوزيع الخلفي التقريبي $q(\mathbf{x}_{1:T} | \mathbf{x}_0)$، المسمى بالعملية الأمامية أو عملية الانتشار، ثابت كسلسلة ماركوف تضيف تدريجياً ضوضاء غاوسية إلى البيانات وفقاً لجدول تباين $\beta_1, \ldots, \beta_T$:

$$q(\mathbf{x}_{1:T} | \mathbf{x}_0) := \prod_{t=1}^T q(\mathbf{x}_t | \mathbf{x}_{t-1}), \quad q(\mathbf{x}_t | \mathbf{x}_{t-1}) := \mathcal{N}(\mathbf{x}_t; \sqrt{1 - \beta_t} \mathbf{x}_{t-1}, \beta_t \mathbf{I})$$

يتم التدريب عن طريق تحسين الحد التبايني المعتاد على اللوغاريتم السلبي للاحتمالية:

$$\mathbb{E}[-\log p_\theta(\mathbf{x}_0)] \leq \mathbb{E}_q\left[-\log \frac{p_\theta(\mathbf{x}_{0:T})}{q(\mathbf{x}_{1:T} | \mathbf{x}_0)}\right] =: L$$

يمكن تعلم تباينات العملية الأمامية $\beta_t$ عن طريق إعادة المعاملة أو الاحتفاظ بها ثابتة كمعاملات فائقة، ويتم ضمان تعبيرية العملية العكسية جزئياً من خلال اختيار الشروط الغاوسية في $p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t)$، لأن كلتا العمليتين لهما نفس الشكل الدالي عندما تكون $\beta_t$ صغيرة.

خاصية ملحوظة للعملية الأمامية هي أنها تسمح بأخذ عينات $\mathbf{x}_t$ عند خطوة زمنية تعسفية $t$ في شكل مغلق: باستخدام الترميز $\alpha_t := 1 - \beta_t$ و $\bar{\alpha}_t := \prod_{s=1}^t \alpha_s$، لدينا

$$q(\mathbf{x}_t | \mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t; \sqrt{\bar{\alpha}_t} \mathbf{x}_0, (1 - \bar{\alpha}_t) \mathbf{I})$$

وبالتالي فإن التدريب الفعال ممكن من خلال تحسين حدود عشوائية من $L$ باستخدام الانحدار التدرجي العشوائي.

---

### Translation Notes

- **Mathematical notation preserved:** All LaTeX equations kept intact
- **Key technical terms:**
  - Reverse process (العملية العكسية)
  - Forward process (العملية الأمامية)
  - Diffusion process (عملية الانتشار)
  - Markov chain (سلسلة ماركوف)
  - Gaussian transitions (انتقالات غاوسية)
  - Variance schedule (جدول التباين)
  - Variational bound (الحد التبايني)
  - Closed form (شكل مغلق)
  - Stochastic gradient descent (الانحدار التدرجي العشوائي)

- **Equations:** 5 major equations defining the diffusion process
- **Parameters:** $\beta_t$, $\alpha_t$, $\bar{\alpha}_t$, $\theta$

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.87
