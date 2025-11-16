# Section 3: Variational Inference for non-Markovian Forward Processes
## القسم 3: الاستدلال التباين لعمليات الانتشار الأمامية غير الماركوفية

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** non-Markovian, variational inference, forward process, marginal distribution, joint distribution, surrogate objective, diffusion model, training

---

### English Version

In this section, we present our main theoretical contribution: a generalization of DDPMs to a family of non-Markovian forward processes that lead to the same training objective. This allows us to derive alternative sampling procedures that can be much more efficient than the original DDPM.

#### 3.1 Non-Markovian Forward Processes

The key observation from Section 2 is that the DDPM training objective $L_\gamma$ depends only on the marginals $q(x_t|x_0)$ and not on the joint $q(x_{1:T}|x_0)$. This suggests that we can consider inference distributions (forward processes) other than the one used by DDPM, as long as they have the same marginals.

We consider a family of inference distributions indexed by a real vector $\sigma \in \mathbb{R}_{\geq 0}^T$:

$$q_\sigma(x_{1:T}|x_0) = q_\sigma(x_T|x_0) \prod_{t=2}^{T} q_\sigma(x_{t-1}|x_t, x_0)$$

where for all $t > 1$:

$$q_\sigma(x_t|x_0) = \mathcal{N}(\sqrt{\bar{\alpha}_t} x_0, (1-\bar{\alpha}_t) I)$$

and

$$q_\sigma(x_{t-1}|x_t, x_0) = \mathcal{N}\left(\sqrt{\bar{\alpha}_{t-1}} x_0 + \sqrt{1 - \bar{\alpha}_{t-1} - \sigma_t^2} \cdot \frac{x_t - \sqrt{\bar{\alpha}_t} x_0}{\sqrt{1 - \bar{\alpha}_t}}, \sigma_t^2 I\right)$$

Note that this forward process is defined "backwards" in time: we specify $q_\sigma(x_T|x_0)$ first, then define $q_\sigma(x_{t-1}|x_t, x_0)$ for decreasing $t$. This is in contrast to the Markovian forward process in DDPM, which is defined "forwards" as $q(x_t|x_{t-1})$.

The crucial property of this family is that all $q_\sigma$ have the same marginals $q_\sigma(x_t|x_0)$ for all $t$, regardless of the choice of $\sigma$. However, different choices of $\sigma$ lead to different joint distributions $q_\sigma(x_{1:T}|x_0)$, giving us a rich family of forward processes.

**Special Cases:**

- When $\sigma_t = \sqrt{\frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}} \sqrt{1-\frac{\bar{\alpha}_t}{\bar{\alpha}_{t-1}}}$ for all $t$, the forward process becomes Markovian and matches the DDPM forward process exactly.

- When $\sigma_t = 0$ for all $t$, the forward process becomes deterministic given $x_t$ and $x_0$, except for $t=1$. We call this the DDIM forward process.

#### 3.2 Generative Process and Unified Variational Inference Objective

For each forward process $q_\sigma$, we can define a corresponding reverse generative process. Following the variational inference framework, we parametrize the reverse process as:

$$p_\theta^{(\sigma)}(x_{0:T}) = p_\theta^{(\sigma)}(x_T) \prod_{t=1}^{T} p_\theta^{(\sigma)}(x_{t-1}|x_t)$$

where $p_\theta^{(\sigma)}(x_T) = \mathcal{N}(x_T; 0, I)$ and

$$p_\theta^{(\sigma)}(x_{t-1}|x_t) = \begin{cases}
\mathcal{N}(f_\theta^{(1)}(x_1), \sigma_1^2 I) & \text{if } t = 1 \\
q_\sigma(x_{t-1}|x_t, f_\theta^{(t)}(x_t)) & \text{otherwise}
\end{cases}$$

where $f_\theta^{(t)}(x_t)$ is a function that predicts $x_0$ from $x_t$.

The following theorem is the key result of this section:

**Theorem 1 (Variational Bound for Non-Markovian Forward Processes).** For all $\sigma > 0$, there exists $\gamma \in \mathbb{R}_{>0}^T$ and $C \in \mathbb{R}$ such that

$$\mathbb{E}_{q_\sigma(x_{0:T})}[\log p_\theta^{(\sigma)}(x_{0:T}) - \log q_\sigma(x_{1:T}|x_0)] = -L_\gamma(\epsilon_\theta) + C$$

where $L_\gamma(\epsilon_\theta)$ is defined as in Section 2.3, and $C$ is a constant that does not depend on $\theta$.

This remarkable result shows that all forward processes in our family $\{q_\sigma\}_\sigma$ lead to variational bounds that share the same surrogate objective $L_\gamma$, up to a constant. This means we can train a single neural network $\epsilon_\theta$ using the DDPM objective, and then use it with any of the generative processes $\{p_\theta^{(\sigma)}\}_\sigma$ at sampling time, without any additional training.

#### 3.3 Derivation of the Variational Bound

We now provide a sketch of the proof of Theorem 1. The full derivation follows standard variational inference techniques.

The variational lower bound can be written as:

$$J_\sigma(\epsilon_\theta) = \mathbb{E}_{q_\sigma(x_{0:T})}[\log p_\theta^{(\sigma)}(x_{0:T}) - \log q_\sigma(x_{1:T}|x_0)]$$

Expanding this, we get:

$$J_\sigma(\epsilon_\theta) = \mathbb{E}_{q_\sigma(x_0, x_T)}[\log p_\theta^{(\sigma)}(x_T)] - \mathbb{E}_{q_\sigma(x_0)}[\log q_\sigma(x_T|x_0)] + \sum_{t=2}^{T} \mathbb{E}_{q_\sigma(x_0, x_t)} \left[ \log \frac{p_\theta^{(\sigma)}(x_{t-1}|x_t)}{q_\sigma(x_{t-1}|x_t, x_0)} \bigg|_{x_{t-1} \sim q_\sigma(x_{t-1}|x_t, x_0)} \right] + \mathbb{E}_{q_\sigma(x_0, x_1)}[\log p_\theta^{(\sigma)}(x_0|x_1)]$$

The first two terms do not depend on $\theta$ and can be absorbed into the constant $C$. For $t \geq 2$, both $p_\theta^{(\sigma)}(x_{t-1}|x_t)$ and $q_\sigma(x_{t-1}|x_t, x_0)$ are Gaussians with the same variance $\sigma_t^2 I$, so their KL divergence reduces to a squared error between their means.

Specifically, if we define $f_\theta^{(t)}(x_t)$ such that it predicts $x_0$ from $x_t$ using the noise prediction network $\epsilon_\theta$:

$$f_\theta^{(t)}(x_t) = \frac{x_t - \sqrt{1-\bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}}$$

then the KL divergence terms can be shown to be proportional to $\|\epsilon - \epsilon_\theta(x_t, t)\|^2$, where $\epsilon$ is the noise used to generate $x_t$ from $x_0$.

This completes the sketch of the proof. The key insight is that regardless of the choice of $\sigma$, the dependence on $\epsilon_\theta$ in the variational bound always reduces to the same surrogate objective $L_\gamma$.

#### 3.4 Implications

Theorem 1 has profound implications for diffusion-based generative modeling:

1. **No Retraining Required:** We can use a single pre-trained DDPM model (trained with the standard $L_\gamma$ objective) with any forward process $q_\sigma$, giving us access to a large family of generative processes.

2. **Flexibility in Sampling:** Different choices of $\sigma$ lead to different sampling procedures with different speed-quality tradeoffs, which we explore in the next section.

3. **Unification:** The DDPM formulation is a special case ($\sigma_t = \tilde{\beta}_t$) of our more general framework, showing that DDPMs are part of a larger family of models.

4. **Theoretical Foundation:** This result provides a principled theoretical foundation for exploring alternative sampling procedures for diffusion models.

---

### النسخة العربية

في هذا القسم، نقدم مساهمتنا النظرية الرئيسية: تعميم DDPMs إلى عائلة من عمليات الانتشار الأمامية غير الماركوفية التي تؤدي إلى نفس هدف التدريب. يسمح لنا هذا باشتقاق إجراءات أخذ عينات بديلة يمكن أن تكون أكثر كفاءة بكثير من DDPM الأصلي.

#### 3.1 عمليات الانتشار الأمامية غير الماركوفية

الملاحظة الأساسية من القسم 2 هي أن هدف تدريب DDPM $L_\gamma$ يعتمد فقط على الهوامش $q(x_t|x_0)$ وليس على المشترك $q(x_{1:T}|x_0)$. يشير هذا إلى أنه يمكننا النظر في توزيعات استدلالية (عمليات أمامية) غير تلك المستخدمة بواسطة DDPM، طالما أن لديها نفس الهوامش.

نعتبر عائلة من توزيعات الاستدلال مفهرسة بمتجه حقيقي $\sigma \in \mathbb{R}_{\geq 0}^T$:

$$q_\sigma(x_{1:T}|x_0) = q_\sigma(x_T|x_0) \prod_{t=2}^{T} q_\sigma(x_{t-1}|x_t, x_0)$$

حيث لجميع $t > 1$:

$$q_\sigma(x_t|x_0) = \mathcal{N}(\sqrt{\bar{\alpha}_t} x_0, (1-\bar{\alpha}_t) I)$$

و

$$q_\sigma(x_{t-1}|x_t, x_0) = \mathcal{N}\left(\sqrt{\bar{\alpha}_{t-1}} x_0 + \sqrt{1 - \bar{\alpha}_{t-1} - \sigma_t^2} \cdot \frac{x_t - \sqrt{\bar{\alpha}_t} x_0}{\sqrt{1 - \bar{\alpha}_t}}, \sigma_t^2 I\right)$$

لاحظ أن هذه العملية الأمامية معرفة "للخلف" في الزمن: نحدد $q_\sigma(x_T|x_0)$ أولاً، ثم نعرّف $q_\sigma(x_{t-1}|x_t, x_0)$ لـ $t$ المتناقص. هذا على النقيض من العملية الأمامية الماركوفية في DDPM، والتي يتم تعريفها "للأمام" كـ $q(x_t|x_{t-1})$.

الخاصية الحاسمة لهذه العائلة هي أن جميع $q_\sigma$ لها نفس الهوامش $q_\sigma(x_t|x_0)$ لجميع $t$، بغض النظر عن اختيار $\sigma$. ومع ذلك، تؤدي الاختيارات المختلفة لـ $\sigma$ إلى توزيعات مشتركة مختلفة $q_\sigma(x_{1:T}|x_0)$، مما يمنحنا عائلة غنية من العمليات الأمامية.

**حالات خاصة:**

- عندما يكون $\sigma_t = \sqrt{\frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}} \sqrt{1-\frac{\bar{\alpha}_t}{\bar{\alpha}_{t-1}}}$ لجميع $t$، تصبح العملية الأمامية ماركوفية وتطابق عملية DDPM الأمامية تماماً.

- عندما يكون $\sigma_t = 0$ لجميع $t$، تصبح العملية الأمامية حتمية معطى $x_t$ و $x_0$، باستثناء $t=1$. نسمي هذه عملية DDIM الأمامية.

#### 3.2 العملية التوليدية وهدف الاستدلال التباين الموحد

لكل عملية أمامية $q_\sigma$، يمكننا تعريف عملية توليدية عكسية مقابلة. باتباع إطار الاستدلال التباين، نقوم بمعايرة العملية العكسية على النحو التالي:

$$p_\theta^{(\sigma)}(x_{0:T}) = p_\theta^{(\sigma)}(x_T) \prod_{t=1}^{T} p_\theta^{(\sigma)}(x_{t-1}|x_t)$$

حيث $p_\theta^{(\sigma)}(x_T) = \mathcal{N}(x_T; 0, I)$ و

$$p_\theta^{(\sigma)}(x_{t-1}|x_t) = \begin{cases}
\mathcal{N}(f_\theta^{(1)}(x_1), \sigma_1^2 I) & \text{إذا كان } t = 1 \\
q_\sigma(x_{t-1}|x_t, f_\theta^{(t)}(x_t)) & \text{خلاف ذلك}
\end{cases}$$

حيث $f_\theta^{(t)}(x_t)$ هي دالة تتنبأ بـ $x_0$ من $x_t$.

النظرية التالية هي النتيجة الأساسية لهذا القسم:

**نظرية 1 (الحد التبايني لعمليات الانتشار الأمامية غير الماركوفية).** لجميع $\sigma > 0$، يوجد $\gamma \in \mathbb{R}_{>0}^T$ و $C \in \mathbb{R}$ بحيث

$$\mathbb{E}_{q_\sigma(x_{0:T})}[\log p_\theta^{(\sigma)}(x_{0:T}) - \log q_\sigma(x_{1:T}|x_0)] = -L_\gamma(\epsilon_\theta) + C$$

حيث يتم تعريف $L_\gamma(\epsilon_\theta)$ كما في القسم 2.3، و $C$ ثابت لا يعتمد على $\theta$.

تُظهر هذه النتيجة الملحوظة أن جميع العمليات الأمامية في عائلتنا $\{q_\sigma\}_\sigma$ تؤدي إلى حدود تباينية تشترك في نفس الهدف البديل $L_\gamma$، حتى ثابت. هذا يعني أنه يمكننا تدريب شبكة عصبية واحدة $\epsilon_\theta$ باستخدام هدف DDPM، ثم استخدامها مع أي من العمليات التوليدية $\{p_\theta^{(\sigma)}\}_\sigma$ في وقت أخذ العينات، دون أي تدريب إضافي.

#### 3.3 اشتقاق الحد التبايني

نقدم الآن رسماً تخطيطياً لبرهان النظرية 1. يتبع الاشتقاق الكامل تقنيات الاستدلال التباين القياسية.

يمكن كتابة الحد التبايني الأدنى على النحو التالي:

$$J_\sigma(\epsilon_\theta) = \mathbb{E}_{q_\sigma(x_{0:T})}[\log p_\theta^{(\sigma)}(x_{0:T}) - \log q_\sigma(x_{1:T}|x_0)]$$

بتوسيع هذا، نحصل على:

$$J_\sigma(\epsilon_\theta) = \mathbb{E}_{q_\sigma(x_0, x_T)}[\log p_\theta^{(\sigma)}(x_T)] - \mathbb{E}_{q_\sigma(x_0)}[\log q_\sigma(x_T|x_0)] + \sum_{t=2}^{T} \mathbb{E}_{q_\sigma(x_0, x_t)} \left[ \log \frac{p_\theta^{(\sigma)}(x_{t-1}|x_t)}{q_\sigma(x_{t-1}|x_t, x_0)} \bigg|_{x_{t-1} \sim q_\sigma(x_{t-1}|x_t, x_0)} \right] + \mathbb{E}_{q_\sigma(x_0, x_1)}[\log p_\theta^{(\sigma)}(x_0|x_1)]$$

المصطلحان الأولان لا يعتمدان على $\theta$ ويمكن استيعابهما في الثابت $C$. لـ $t \geq 2$، كل من $p_\theta^{(\sigma)}(x_{t-1}|x_t)$ و $q_\sigma(x_{t-1}|x_t, x_0)$ هما توزيعان غاوسيان لهما نفس التباين $\sigma_t^2 I$، لذا يختزل تباعد KL الخاص بهما إلى خطأ تربيعي بين متوسطاتهما.

على وجه التحديد، إذا عرّفنا $f_\theta^{(t)}(x_t)$ بحيث تتنبأ بـ $x_0$ من $x_t$ باستخدام شبكة التنبؤ بالضوضاء $\epsilon_\theta$:

$$f_\theta^{(t)}(x_t) = \frac{x_t - \sqrt{1-\bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}}$$

فيمكن إظهار أن مصطلحات تباعد KL تتناسب مع $\|\epsilon - \epsilon_\theta(x_t, t)\|^2$، حيث $\epsilon$ هي الضوضاء المستخدمة لتوليد $x_t$ من $x_0$.

هذا يكمل رسم البرهان. الرؤية الأساسية هي أنه بغض النظر عن اختيار $\sigma$، فإن الاعتماد على $\epsilon_\theta$ في الحد التبايني يختزل دائماً إلى نفس الهدف البديل $L_\gamma$.

#### 3.4 التداعيات

للنظرية 1 تداعيات عميقة على النمذجة التوليدية القائمة على الانتشار:

1. **لا حاجة لإعادة التدريب:** يمكننا استخدام نموذج DDPM واحد مدرب مسبقاً (مدرب بهدف $L_\gamma$ القياسي) مع أي عملية أمامية $q_\sigma$، مما يمنحنا الوصول إلى عائلة كبيرة من العمليات التوليدية.

2. **مرونة في أخذ العينات:** تؤدي الاختيارات المختلفة لـ $\sigma$ إلى إجراءات أخذ عينات مختلفة مع مفاضلات مختلفة بين السرعة والجودة، وهو ما نستكشفه في القسم التالي.

3. **التوحيد:** صياغة DDPM هي حالة خاصة ($\sigma_t = \tilde{\beta}_t$) من إطارنا الأكثر عمومية، مما يُظهر أن DDPMs هي جزء من عائلة أكبر من النماذج.

4. **الأساس النظري:** توفر هذه النتيجة أساساً نظرياً مبدئياً لاستكشاف إجراءات أخذ عينات بديلة لنماذج الانتشار.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Non-Markovian forward processes - عمليات الانتشار الأمامية غير الماركوفية
  - Inference distributions - توزيعات استدلالية
  - Generative process - العملية التوليدية
  - Unified variational inference objective - هدف الاستدلال التباين الموحد
  - Deterministic process - عملية حتمية
  - DDIM forward process - عملية DDIM الأمامية

- **Equations:** 12 major mathematical equations with complex probability distributions
- **Citations:** References to standard variational inference techniques
- **Special handling:**
  - Theorem statement in formal mathematical notation
  - Proof sketch with detailed mathematical derivations
  - Heavy use of conditional probability notation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
