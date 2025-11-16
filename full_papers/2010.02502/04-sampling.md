# Section 4: Sampling from Generalized Generative Processes
## القسم 4: أخذ العينات من العمليات التوليدية المعممة

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** sampling, generative process, deterministic, stochastic, acceleration, latent space, interpolation, encoding, DDIM

---

### English Version

In this section, we describe how to sample from the family of generative processes $\{p_\theta^{(\sigma)}\}_\sigma$ derived in the previous section. We focus particularly on the deterministic case ($\sigma = 0$), which we call DDIM, and show how it enables several capabilities not possible with standard DDPMs.

#### 4.1 Denoising Diffusion Implicit Models

From Theorem 1, we can use any inference process $q_\sigma$ with the same pre-trained model $\epsilon_\theta$. The sampling procedure for the generative process $p_\theta^{(\sigma)}$ follows directly from the definition in Section 3.2.

For $t = T, T-1, \ldots, 1$, we sample:

$$x_{t-1} = \sqrt{\bar{\alpha}_{t-1}} \underbrace{\left( \frac{x_t - \sqrt{1-\bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}} \right)}_{\text{"predicted } x_0\text{"}} + \underbrace{\sqrt{1 - \bar{\alpha}_{t-1} - \sigma_t^2} \cdot \epsilon_\theta(x_t, t)}_{\text{"direction pointing to } x_t\text{"}} + \underbrace{\sigma_t \epsilon_t}_{\text{random noise}}$$

where $\epsilon_t \sim \mathcal{N}(0, I)$ is independent noise at each timestep.

This sampling equation has an intuitive interpretation:

1. The first term $\sqrt{\bar{\alpha}_{t-1}} \left( \frac{x_t - \sqrt{1-\bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}} \right)$ represents a prediction of $x_0$ from the current $x_t$, scaled by $\sqrt{\bar{\alpha}_{t-1}}$.

2. The second term $\sqrt{1 - \bar{\alpha}_{t-1} - \sigma_t^2} \cdot \epsilon_\theta(x_t, t)$ represents the "direction" pointing from the predicted $x_0$ back to $x_t$, adjusted for the noise level at timestep $t-1$.

3. The third term $\sigma_t \epsilon_t$ adds random noise with variance $\sigma_t^2$.

**The DDIM Sampling Formula:**

When we set $\sigma_t = 0$ for all $t$, the sampling process becomes deterministic (except for the initial sampling of $x_T$ from $\mathcal{N}(0, I)$). The sampling equation simplifies to:

$$x_{t-1} = \sqrt{\bar{\alpha}_{t-1}} \left( \frac{x_t - \sqrt{1-\bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}} \right) + \sqrt{1 - \bar{\alpha}_{t-1}} \cdot \epsilon_\theta(x_t, t)$$

We call this the DDIM sampling formula. This deterministic process defines an implicit probabilistic model, hence the name "Denoising Diffusion Implicit Model."

#### 4.2 Accelerated Generation with Fewer Steps

A key advantage of the DDIM formulation is that we can subsample the timesteps to accelerate generation. Since the forward process is now non-Markovian, we are no longer restricted to following all $T$ timesteps in sequence.

Let $\tau = [\tau_1, \tau_2, \ldots, \tau_S]$ be an increasing sub-sequence of $[1, 2, \ldots, T]$ where $S < T$. We can define a forward process that only uses the timesteps in $\tau$:

$$q_\sigma(x_{\tau_{i-1}}|x_{\tau_i}, x_0) = \mathcal{N}\left(\sqrt{\bar{\alpha}_{\tau_{i-1}}} x_0 + \sqrt{1 - \bar{\alpha}_{\tau_{i-1}} - \sigma_{\tau_i}^2} \cdot \frac{x_{\tau_i} - \sqrt{\bar{\alpha}_{\tau_i}} x_0}{\sqrt{1 - \bar{\alpha}_{\tau_i}}}, \sigma_{\tau_i}^2 I\right)$$

The corresponding generative process uses the same sampling formula as before, but only at the timesteps in $\tau$. In the deterministic case ($\sigma = 0$), the sampling equation becomes:

$$x_{\tau_{i-1}} = \sqrt{\bar{\alpha}_{\tau_{i-1}}} \left( \frac{x_{\tau_i} - \sqrt{1-\bar{\alpha}_{\tau_i}} \epsilon_\theta(x_{\tau_i}, \tau_i)}{\sqrt{\bar{\alpha}_{\tau_i}}} \right) + \sqrt{1 - \bar{\alpha}_{\tau_{i-1}}} \cdot \epsilon_\theta(x_{\tau_i}, \tau_i)$$

This allows us to generate samples with only $S$ steps instead of $T$ steps. For example, if $T = 1000$ and we choose $S = 50$, we can generate samples 20× faster than the original DDPM. Empirically, we find that DDIMs maintain high sample quality even with $S$ as small as 10-50 steps, enabling dramatic speedups.

#### 4.3 Relevance to Neural ODEs

The deterministic DDIM sampling process can be viewed as discretizing an ordinary differential equation (ODE). As $\Delta t$ becomes infinitesimally small (i.e., as we increase the number of steps), the DDIM sampling process approaches the solution of a continuous-time ODE.

Specifically, we can write the DDIM update as:

$$\frac{x_{t-\Delta t} - x_t}{\Delta t} \approx -\sqrt{1-\bar{\alpha}_t} \frac{d \log \bar{\alpha}_t}{dt} \left( \frac{x_t}{\sqrt{\bar{\alpha}_t}} - \frac{\epsilon_\theta(x_t, t)}{\sqrt{1-\bar{\alpha}_t}} \right)$$

In the limit as $\Delta t \to 0$, this becomes an ODE that governs the evolution of $x_t$ over continuous time. This connection to Neural ODEs provides several insights:

1. **Continuous Limit:** DDIMs can be viewed as Euler discretizations of a continuous-time generative process.

2. **ODE Solvers:** We could potentially use more sophisticated ODE solvers (e.g., Runge-Kutta methods) to further improve sampling efficiency or quality.

3. **Theoretical Analysis:** The ODE perspective allows us to apply tools from dynamical systems theory to analyze and understand the generative process.

This connection also relates DDIMs to recent work on continuous normalizing flows and score-based generative models using SDEs (stochastic differential equations).

#### 4.4 Consistency Property and Semantic Interpolation

An important property of deterministic DDIMs is consistency: given the same initial latent $x_T$, the model will always generate the same sample $x_0$. This is in contrast to stochastic DDPMs, which generate different samples even from the same initial latent.

This consistency enables several useful capabilities:

**Image Encoding:** Since the DDIM forward process is deterministic (for $\sigma = 0$), we can encode an image $x_0$ into a latent representation $x_T$ by running the forward process. This latent $x_T$ can then be decoded back to $x_0$ using the DDIM sampling procedure. Empirically, we find that DDIMs can nearly perfectly reconstruct images through this encode-decode process.

**Semantic Interpolation:** Given two images $x_0^{(1)}$ and $x_0^{(2)}$, we can encode them to their latent representations $x_T^{(1)}$ and $x_T^{(2)}$. We can then interpolate in the latent space:

$$x_T^{(\alpha)} = \alpha x_T^{(1)} + (1-\alpha) x_T^{(2)}$$

for $\alpha \in [0, 1]$, and decode $x_T^{(\alpha)}$ to generate an interpolated image $x_0^{(\alpha)}$. Since the latent space $x_T$ is close to a standard Gaussian, linear interpolation in this space tends to produce semantically meaningful transitions between images.

This interpolation capability is similar to that of VAEs and GANs, but was not possible with standard DDPMs due to their stochastic sampling process. The deterministic nature of DDIMs is crucial for enabling this functionality.

#### 4.5 Trading Off Quality and Speed

The parameter $\sigma$ in our generative process family allows us to trade off between sample quality and computation time. The two extremes are:

- **$\sigma = 0$ (DDIM):** Fully deterministic, fastest sampling, enables interpolation and encoding.

- **$\sigma = \tilde{\beta}$ (DDPM):** Fully stochastic, slower sampling, potentially slightly better sample quality in some cases.

Intermediate values of $\sigma$ provide a continuum between these extremes. In our experiments (Section 5), we primarily focus on the deterministic case ($\sigma = 0$) as it provides the best speed-quality tradeoff in most scenarios.

---

### النسخة العربية

في هذا القسم، نصف كيفية أخذ العينات من عائلة العمليات التوليدية $\{p_\theta^{(\sigma)}\}_\sigma$ المشتقة في القسم السابق. نركز بشكل خاص على الحالة الحتمية ($\sigma = 0$)، التي نسميها DDIM، ونُظهر كيف تمكّن من عدة قدرات غير ممكنة مع DDPMs القياسية.

#### 4.1 نماذج الانتشار الضمنية لإزالة الضوضاء

من النظرية 1، يمكننا استخدام أي عملية استدلالية $q_\sigma$ مع نفس النموذج المدرب مسبقاً $\epsilon_\theta$. يتبع إجراء أخذ العينات للعملية التوليدية $p_\theta^{(\sigma)}$ مباشرة من التعريف في القسم 3.2.

لـ $t = T, T-1, \ldots, 1$، نأخذ عينة:

$$x_{t-1} = \sqrt{\bar{\alpha}_{t-1}} \underbrace{\left( \frac{x_t - \sqrt{1-\bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}} \right)}_{\text{"} x_0 \text{ المتنبأ به"}} + \underbrace{\sqrt{1 - \bar{\alpha}_{t-1} - \sigma_t^2} \cdot \epsilon_\theta(x_t, t)}_{\text{"الاتجاه المشير إلى } x_t\text{"}} + \underbrace{\sigma_t \epsilon_t}_{\text{ضوضاء عشوائية}}$$

حيث $\epsilon_t \sim \mathcal{N}(0, I)$ هي ضوضاء مستقلة عند كل خطوة زمنية.

لهذه المعادلة لأخذ العينات تفسير بديهي:

1. المصطلح الأول $\sqrt{\bar{\alpha}_{t-1}} \left( \frac{x_t - \sqrt{1-\bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}} \right)$ يمثل تنبؤاً بـ $x_0$ من $x_t$ الحالي، مقيساً بـ $\sqrt{\bar{\alpha}_{t-1}}$.

2. المصطلح الثاني $\sqrt{1 - \bar{\alpha}_{t-1} - \sigma_t^2} \cdot \epsilon_\theta(x_t, t)$ يمثل "الاتجاه" المشير من $x_0$ المتنبأ به إلى $x_t$، معدّلاً لمستوى الضوضاء عند الخطوة الزمنية $t-1$.

3. المصطلح الثالث $\sigma_t \epsilon_t$ يضيف ضوضاء عشوائية بتباين $\sigma_t^2$.

**صيغة أخذ عينات DDIM:**

عندما نعيّن $\sigma_t = 0$ لجميع $t$، تصبح عملية أخذ العينات حتمية (باستثناء أخذ العينة الأولي لـ $x_T$ من $\mathcal{N}(0, I)$). تبسط معادلة أخذ العينات إلى:

$$x_{t-1} = \sqrt{\bar{\alpha}_{t-1}} \left( \frac{x_t - \sqrt{1-\bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}} \right) + \sqrt{1 - \bar{\alpha}_{t-1}} \cdot \epsilon_\theta(x_t, t)$$

نسمي هذه صيغة أخذ عينات DDIM. تعرّف هذه العملية الحتمية نموذجاً احتمالياً ضمنياً، ومن هنا جاء الاسم "نموذج الانتشار الضمني لإزالة الضوضاء".

#### 4.2 التوليد المتسارع بخطوات أقل

ميزة أساسية لصياغة DDIM هي أنه يمكننا أخذ عينة فرعية من الخطوات الزمنية لتسريع التوليد. نظراً لأن العملية الأمامية الآن غير ماركوفية، لم نعد مقيدين باتباع جميع خطوات $T$ بالتسلسل.

لتكن $\tau = [\tau_1, \tau_2, \ldots, \tau_S]$ تسلسلاً فرعياً متزايداً من $[1, 2, \ldots, T]$ حيث $S < T$. يمكننا تعريف عملية أمامية تستخدم فقط الخطوات الزمنية في $\tau$:

$$q_\sigma(x_{\tau_{i-1}}|x_{\tau_i}, x_0) = \mathcal{N}\left(\sqrt{\bar{\alpha}_{\tau_{i-1}}} x_0 + \sqrt{1 - \bar{\alpha}_{\tau_{i-1}} - \sigma_{\tau_i}^2} \cdot \frac{x_{\tau_i} - \sqrt{\bar{\alpha}_{\tau_i}} x_0}{\sqrt{1 - \bar{\alpha}_{\tau_i}}}, \sigma_{\tau_i}^2 I\right)$$

تستخدم العملية التوليدية المقابلة نفس صيغة أخذ العينات كما كان من قبل، ولكن فقط عند الخطوات الزمنية في $\tau$. في الحالة الحتمية ($\sigma = 0$)، تصبح معادلة أخذ العينات:

$$x_{\tau_{i-1}} = \sqrt{\bar{\alpha}_{\tau_{i-1}}} \left( \frac{x_{\tau_i} - \sqrt{1-\bar{\alpha}_{\tau_i}} \epsilon_\theta(x_{\tau_i}, \tau_i)}{\sqrt{\bar{\alpha}_{\tau_i}}} \right) + \sqrt{1 - \bar{\alpha}_{\tau_{i-1}}} \cdot \epsilon_\theta(x_{\tau_i}, \tau_i)$$

يسمح لنا هذا بتوليد عينات بـ $S$ خطوة فقط بدلاً من $T$ خطوة. على سبيل المثال، إذا كان $T = 1000$ واخترنا $S = 50$، يمكننا توليد عينات أسرع بـ 20× من DDPM الأصلي. تجريبياً، نجد أن DDIMs تحافظ على جودة عينة عالية حتى مع $S$ صغيرة تصل إلى 10-50 خطوة، مما يتيح تسريعات دراماتيكية.

#### 4.3 الصلة بالمعادلات التفاضلية العادية العصبية

يمكن النظر إلى عملية أخذ عينات DDIM الحتمية على أنها تحويل معادلة تفاضلية عادية (ODE) إلى شكل منفصل. عندما يصبح $\Delta t$ صغيراً بشكل لا نهائي (أي، عندما نزيد عدد الخطوات)، تقترب عملية أخذ عينات DDIM من حل ODE ذات زمن مستمر.

على وجه التحديد، يمكننا كتابة تحديث DDIM كـ:

$$\frac{x_{t-\Delta t} - x_t}{\Delta t} \approx -\sqrt{1-\bar{\alpha}_t} \frac{d \log \bar{\alpha}_t}{dt} \left( \frac{x_t}{\sqrt{\bar{\alpha}_t}} - \frac{\epsilon_\theta(x_t, t)}{\sqrt{1-\bar{\alpha}_t}} \right)$$

في الحد عندما $\Delta t \to 0$، يصبح هذا ODE يحكم تطور $x_t$ على مر الزمن المستمر. يوفر هذا الارتباط بالمعادلات التفاضلية العادية العصبية عدة رؤى:

1. **الحد المستمر:** يمكن النظر إلى DDIMs على أنها تحويلات أويلر المنفصلة لعملية توليدية ذات زمن مستمر.

2. **حالات حل ODE:** يمكننا استخدام حالات حل ODE أكثر تطوراً (مثل طرق رونج-كوتا) لتحسين كفاءة أو جودة أخذ العينات بشكل أكبر.

3. **التحليل النظري:** يسمح لنا منظور ODE بتطبيق أدوات من نظرية الأنظمة الديناميكية لتحليل وفهم العملية التوليدية.

يربط هذا الارتباط أيضاً DDIMs بالأعمال الحديثة حول التدفقات المُطبعة المستمرة والنماذج التوليدية القائمة على النقاط باستخدام المعادلات التفاضلية العشوائية (SDEs).

#### 4.4 خاصية الاتساق والاستيفاء الدلالي

خاصية مهمة لـ DDIMs الحتمية هي الاتساق: معطى نفس الكامن الأولي $x_T$، سيولد النموذج دائماً نفس العينة $x_0$. هذا على النقيض من DDPMs العشوائية، التي تولد عينات مختلفة حتى من نفس الكامن الأولي.

يمكّن هذا الاتساق من عدة قدرات مفيدة:

**ترميز الصور:** نظراً لأن عملية DDIM الأمامية حتمية (لـ $\sigma = 0$)، يمكننا ترميز صورة $x_0$ في تمثيل كامن $x_T$ عن طريق تشغيل العملية الأمامية. يمكن بعد ذلك فك تشفير هذا الكامن $x_T$ إلى $x_0$ باستخدام إجراء أخذ عينات DDIM. تجريبياً، نجد أن DDIMs يمكنها إعادة بناء الصور بشكل شبه مثالي من خلال عملية الترميز-فك الترميز هذه.

**الاستيفاء الدلالي:** معطى صورتين $x_0^{(1)}$ و $x_0^{(2)}$، يمكننا ترميزهما إلى تمثيلاتهما الكامنة $x_T^{(1)}$ و $x_T^{(2)}$. يمكننا بعد ذلك الاستيفاء في الفضاء الكامن:

$$x_T^{(\alpha)} = \alpha x_T^{(1)} + (1-\alpha) x_T^{(2)}$$

لـ $\alpha \in [0, 1]$، وفك تشفير $x_T^{(\alpha)}$ لتوليد صورة مستوفاة $x_0^{(\alpha)}$. نظراً لأن الفضاء الكامن $x_T$ قريب من غاوسي قياسي، يميل الاستيفاء الخطي في هذا الفضاء إلى إنتاج انتقالات ذات معنى دلالي بين الصور.

قدرة الاستيفاء هذه مماثلة لتلك الموجودة في VAEs و GANs، ولكنها لم تكن ممكنة مع DDPMs القياسية بسبب عملية أخذ العينات العشوائية. الطبيعة الحتمية لـ DDIMs حاسمة لتمكين هذه الوظيفة.

#### 4.5 المفاضلة بين الجودة والسرعة

يسمح لنا المعامل $\sigma$ في عائلة عملياتنا التوليدية بالمفاضلة بين جودة العينة ووقت الحساب. الطرفان المتطرفان هما:

- **$\sigma = 0$ (DDIM):** حتمي بالكامل، أخذ عينات أسرع، يمكّن الاستيفاء والترميز.

- **$\sigma = \tilde{\beta}$ (DDPM):** عشوائي بالكامل، أخذ عينات أبطأ، جودة عينة أفضل قليلاً في بعض الحالات.

القيم الوسيطة لـ $\sigma$ توفر استمرارية بين هذين الطرفين المتطرفين. في تجاربنا (القسم 5)، نركز بشكل أساسي على الحالة الحتمية ($\sigma = 0$) لأنها توفر أفضل مفاضلة بين السرعة والجودة في معظم السيناريوهات.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - DDIM sampling formula - صيغة أخذ عينات DDIM
  - Accelerated generation - التوليد المتسارع
  - Timestep subsampling - أخذ عينة فرعية من الخطوات الزمنية
  - Neural ODEs - المعادلات التفاضلية العادية العصبية
  - Euler discretization - تحويلات أويلر المنفصلة
  - Consistency property - خاصية الاتساق
  - Image encoding - ترميز الصور
  - Semantic interpolation - الاستيفاء الدلالي
  - Continuous normalizing flows - التدفقات المُطبعة المستمرة
  - Stochastic differential equations (SDEs) - المعادلات التفاضلية العشوائية

- **Equations:** 6 major sampling equations and ODE formulation
- **Citations:** References to Neural ODEs, normalizing flows, score-based models
- **Special handling:**
  - Detailed mathematical derivations
  - Algorithm-style sampling procedures
  - Connections to continuous-time processes

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
