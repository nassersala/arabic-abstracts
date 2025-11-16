# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** diffusion model, denoising, probabilistic, variational inference, Markov chain, forward process, reverse process, training, latent variable, Gaussian noise

---

### English Version

In this section, we review the mathematical formulation of denoising diffusion probabilistic models (DDPMs) and the variational inference framework used for training them.

#### 2.1 Denoising Diffusion Probabilistic Models

DDPMs are latent variable models of the form $p_\theta(x_0) = \int p_\theta(x_{0:T}) dx_{1:T}$, where $x_0 \sim q(x_0)$ is the data, and $x_1, \ldots, x_T$ are latent variables of the same dimensionality as $x_0$. The joint distribution $p_\theta(x_{0:T})$ is called the reverse process, and is defined as a Markov chain with learned Gaussian transitions starting from a standard Gaussian prior $p(x_T) = \mathcal{N}(x_T; 0, I)$:

$$p_\theta(x_{0:T}) = p(x_T) \prod_{t=1}^{T} p_\theta(x_{t-1}|x_t)$$

$$p_\theta(x_{t-1}|x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$$

where $\mu_\theta$ and $\Sigma_\theta$ are parametrized by neural networks.

The reverse process is trained to invert a fixed forward process (or diffusion process) that gradually adds Gaussian noise to the data according to a variance schedule $\beta_1, \ldots, \beta_T \in (0, 1)$:

$$q(x_{1:T}|x_0) = \prod_{t=1}^{T} q(x_t|x_{t-1})$$

$$q(x_t|x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t} x_{t-1}, \beta_t I)$$

An important property of the forward process is that we can sample $x_t$ at any timestep $t$ in closed form. If we let $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod_{s=1}^{t} \alpha_s$, then:

$$q(x_t|x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1-\bar{\alpha}_t) I)$$

This allows us to efficiently sample $x_t$ from $x_0$ and a noise sample $\epsilon \sim \mathcal{N}(0, I)$ via the reparametrization trick: $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \epsilon$.

#### 2.2 Variational Inference Objective

Training DDPMs involves maximizing a variational lower bound on the log-likelihood:

$$\mathbb{E}_{q(x_0)}[\log p_\theta(x_0)] \geq \mathbb{E}_{q(x_{0:T})}[\log p_\theta(x_{0:T}) - \log q(x_{1:T}|x_0)]$$

This can be rewritten as:

$$L_0 + L_1 + \cdots + L_{T-1} + L_T$$

where:

$$L_0 = \mathbb{E}_{q(x_1|x_0)}[\log p_\theta(x_0|x_1)]$$

$$L_{t-1} = \mathbb{E}_{q(x_t|x_0)}[D_{KL}(q(x_{t-1}|x_t, x_0) \| p_\theta(x_{t-1}|x_t))]$$

$$L_T = D_{KL}(q(x_T|x_0) \| p(x_T))$$

for $t \in \{2, \ldots, T\}$, and $D_{KL}$ denotes the Kullback-Leibler divergence.

The term $L_T$ is constant and can be ignored during training since the forward process has no learnable parameters. The reconstruction term $L_0$ can be modeled using a discrete decoder. The key terms are $L_1, \ldots, L_{T-1}$, which measure the KL divergence between the forward process posterior $q(x_{t-1}|x_t, x_0)$ and the reverse process transition $p_\theta(x_{t-1}|x_t)$.

#### 2.3 Surrogate Objective

A remarkable property of the forward process is that the posterior $q(x_{t-1}|x_t, x_0)$ is tractable and is given by:

$$q(x_{t-1}|x_t, x_0) = \mathcal{N}(x_{t-1}; \tilde{\mu}_t(x_t, x_0), \tilde{\beta}_t I)$$

where:

$$\tilde{\mu}_t(x_t, x_0) = \frac{\sqrt{\bar{\alpha}_{t-1}} \beta_t}{1 - \bar{\alpha}_t} x_0 + \frac{\sqrt{\alpha_t}(1 - \bar{\alpha}_{t-1})}{1 - \bar{\alpha}_t} x_t$$

$$\tilde{\beta}_t = \frac{1 - \bar{\alpha}_{t-1}}{1 - \bar{\alpha}_t} \beta_t$$

Ho et al. (2020) showed that instead of directly predicting $\mu_\theta(x_t, t)$, one can parametrize the model to predict the noise $\epsilon$ used to generate $x_t$ from $x_0$. Specifically, they set:

$$\mu_\theta(x_t, t) = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}} \epsilon_\theta(x_t, t) \right)$$

where $\epsilon_\theta$ is a neural network that predicts the noise. This leads to the following simplified training objective:

$$L_\gamma = \sum_{t=1}^{T} \gamma_t \mathbb{E}_{x_0 \sim q(x_0), \epsilon \sim \mathcal{N}(0,I)} \left[ \| \epsilon - \epsilon_\theta(x_t, t) \|^2 \right]$$

where $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \epsilon$ and $\gamma_t$ are positive coefficients. When $\gamma_t = 1$ for all $t$, this objective corresponds to a reweighted version of the variational bound. Empirically, Ho et al. found that setting all $\gamma_t = 1$ (uniform weighting) works better than the theoretically-motivated weighting derived from the variational bound.

This surrogate objective $L_\gamma$ is the key to our approach: we observe that it only depends on the marginals $q(x_t|x_0)$ of the forward process, and not on the joint distribution $q(x_{1:T}|x_0)$. This insight allows us to consider alternative forward processes that preserve these marginals while having different joint distributions, leading to more efficient sampling procedures.

---

### النسخة العربية

في هذا القسم، نستعرض الصياغة الرياضية لنماذج الانتشار الاحتمالية لإزالة الضوضاء (DDPMs) وإطار الاستدلال التباين المستخدم لتدريبها.

#### 2.1 نماذج الانتشار الاحتمالية لإزالة الضوضاء

DDPMs هي نماذج متغيرات كامنة من الشكل $p_\theta(x_0) = \int p_\theta(x_{0:T}) dx_{1:T}$، حيث $x_0 \sim q(x_0)$ هي البيانات، و $x_1, \ldots, x_T$ هي متغيرات كامنة لها نفس الأبعاد مثل $x_0$. يُطلق على التوزيع المشترك $p_\theta(x_{0:T})$ اسم العملية العكسية، ويتم تعريفه على أنه سلسلة ماركوف مع تحولات غاوسية متعلمة تبدأ من توزيع غاوسي قياسي مسبق $p(x_T) = \mathcal{N}(x_T; 0, I)$:

$$p_\theta(x_{0:T}) = p(x_T) \prod_{t=1}^{T} p_\theta(x_{t-1}|x_t)$$

$$p_\theta(x_{t-1}|x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$$

حيث $\mu_\theta$ و $\Sigma_\theta$ يتم تحديد معالمهما بواسطة الشبكات العصبية.

يتم تدريب العملية العكسية لعكس عملية أمامية ثابتة (أو عملية انتشار) تضيف تدريجياً ضوضاء غاوسية إلى البيانات وفقاً لجدول زمني للتباين $\beta_1, \ldots, \beta_T \in (0, 1)$:

$$q(x_{1:T}|x_0) = \prod_{t=1}^{T} q(x_t|x_{t-1})$$

$$q(x_t|x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t} x_{t-1}, \beta_t I)$$

خاصية مهمة للعملية الأمامية هي أنه يمكننا أخذ عينة $x_t$ في أي خطوة زمنية $t$ بشكل مغلق. إذا جعلنا $\alpha_t = 1 - \beta_t$ و $\bar{\alpha}_t = \prod_{s=1}^{t} \alpha_s$، فإن:

$$q(x_t|x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1-\bar{\alpha}_t) I)$$

يسمح لنا هذا بأخذ عينة $x_t$ بكفاءة من $x_0$ وعينة ضوضاء $\epsilon \sim \mathcal{N}(0, I)$ عبر حيلة إعادة المعايرة: $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \epsilon$.

#### 2.2 هدف الاستدلال التباين

يتضمن تدريب DDPMs تعظيم حد تبايني أدنى على لوغاريتم الاحتمالية:

$$\mathbb{E}_{q(x_0)}[\log p_\theta(x_0)] \geq \mathbb{E}_{q(x_{0:T})}[\log p_\theta(x_{0:T}) - \log q(x_{1:T}|x_0)]$$

يمكن إعادة كتابة هذا على النحو التالي:

$$L_0 + L_1 + \cdots + L_{T-1} + L_T$$

حيث:

$$L_0 = \mathbb{E}_{q(x_1|x_0)}[\log p_\theta(x_0|x_1)]$$

$$L_{t-1} = \mathbb{E}_{q(x_t|x_0)}[D_{KL}(q(x_{t-1}|x_t, x_0) \| p_\theta(x_{t-1}|x_t))]$$

$$L_T = D_{KL}(q(x_T|x_0) \| p(x_T))$$

لـ $t \in \{2, \ldots, T\}$، و $D_{KL}$ يشير إلى تباعد كولباك-ليبلر.

المصطلح $L_T$ ثابت ويمكن تجاهله أثناء التدريب نظراً لأن العملية الأمامية ليس لها معاملات قابلة للتعلم. يمكن نمذجة مصطلح إعادة البناء $L_0$ باستخدام مفكك شفرة منفصل. المصطلحات الأساسية هي $L_1, \ldots, L_{T-1}$، التي تقيس تباعد KL بين التوزيع اللاحق للعملية الأمامية $q(x_{t-1}|x_t, x_0)$ والانتقال للعملية العكسية $p_\theta(x_{t-1}|x_t)$.

#### 2.3 الهدف البديل

خاصية ملحوظة للعملية الأمامية هي أن التوزيع اللاحق $q(x_{t-1}|x_t, x_0)$ قابل للمعالجة ويُعطى بـ:

$$q(x_{t-1}|x_t, x_0) = \mathcal{N}(x_{t-1}; \tilde{\mu}_t(x_t, x_0), \tilde{\beta}_t I)$$

حيث:

$$\tilde{\mu}_t(x_t, x_0) = \frac{\sqrt{\bar{\alpha}_{t-1}} \beta_t}{1 - \bar{\alpha}_t} x_0 + \frac{\sqrt{\alpha_t}(1 - \bar{\alpha}_{t-1})}{1 - \bar{\alpha}_t} x_t$$

$$\tilde{\beta}_t = \frac{1 - \bar{\alpha}_{t-1}}{1 - \bar{\alpha}_t} \beta_t$$

أظهر Ho وآخرون (2020) أنه بدلاً من التنبؤ المباشر بـ $\mu_\theta(x_t, t)$، يمكن للمرء معايرة النموذج للتنبؤ بالضوضاء $\epsilon$ المستخدمة لتوليد $x_t$ من $x_0$. على وجه التحديد، قاموا بتعيين:

$$\mu_\theta(x_t, t) = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}} \epsilon_\theta(x_t, t) \right)$$

حيث $\epsilon_\theta$ هي شبكة عصبية تتنبأ بالضوضاء. يؤدي هذا إلى هدف التدريب المبسط التالي:

$$L_\gamma = \sum_{t=1}^{T} \gamma_t \mathbb{E}_{x_0 \sim q(x_0), \epsilon \sim \mathcal{N}(0,I)} \left[ \| \epsilon - \epsilon_\theta(x_t, t) \|^2 \right]$$

حيث $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \epsilon$ و $\gamma_t$ هي معاملات موجبة. عندما يكون $\gamma_t = 1$ لجميع $t$، يتوافق هذا الهدف مع نسخة معاد وزنها من الحد التبايني. تجريبياً، وجد Ho وآخرون أن تعيين كل $\gamma_t = 1$ (وزن موحد) يعمل بشكل أفضل من الترجيح المشتق نظرياً من الحد التبايني.

هذا الهدف البديل $L_\gamma$ هو مفتاح نهجنا: نلاحظ أنه يعتمد فقط على الهوامش $q(x_t|x_0)$ للعملية الأمامية، وليس على التوزيع المشترك $q(x_{1:T}|x_0)$. تسمح لنا هذه الرؤية بالنظر في عمليات أمامية بديلة تحافظ على هذه الهوامش بينما لها توزيعات مشتركة مختلفة، مما يؤدي إلى إجراءات أخذ عينات أكثر كفاءة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Latent variable models - نماذج متغيرات كامنة
  - Reverse process - العملية العكسية
  - Forward process / diffusion process - العملية الأمامية / عملية الانتشار
  - Variance schedule - جدول زمني للتباين
  - Reparametrization trick - حيلة إعادة المعايرة
  - Variational lower bound - حد تبايني أدنى
  - Kullback-Leibler divergence - تباعد كولباك-ليبلر
  - Forward process posterior - التوزيع اللاحق للعملية الأمامية
  - Surrogate objective - الهدف البديل
  - Marginals - الهوامش

- **Equations:** 15 major mathematical equations with LaTeX notation
- **Citations:** Ho et al. (2020) for DDPM formulation
- **Special handling:** Heavy mathematical content with probability distributions, integrals, and summations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
