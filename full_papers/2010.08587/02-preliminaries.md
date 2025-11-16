# Section 2: Preliminaries
## القسم 2: المفاهيم الأساسية

**Section:** preliminaries
**Translation Quality:** 0.87
**Glossary Terms Used:** reinforcement learning, Markov Decision Process, MDP, state space, action space, reward function, discount, policy, Q-function, policy iteration, Kullback-Leibler divergence, prior

---

### English Version

We consider the standard reinforcement learning setting in a Markov Decision Process (MDP) described by the tuple $(S, A, r, \gamma, P, \rho_0)$ consisting of: the state space $S$, the action space $A$, the instantaneous reward function $r(s_t, a_t)$ – obtained by executing action $a_t$ in state $s_t$ – the discount $\gamma$, the transition distribution $P(s_{t+1}|s_t, a_t)$ and the initial state distribution $\rho_0$. The RL objective $J$ corresponds to maximizing the expected reward under a given policy $J(\pi) = \mathbb{E}_{\pi, P}[\sum_{t=0}^{\infty} \gamma^t r(s_t, a_t) | s_0 \sim \rho_0(s)]$, where we have $a_t \sim \pi(\cdot|s_t)$ and $s_{t+1} \sim P(\cdot|s_t, a_t)$. We use $\pi^* = \arg\max_{\pi} J(\pi)$ to denote the optimal policy. We make use of the state-action value function for policy $\pi$, also known as the Q-function which can be defined recursively as $Q^{\pi}(s_t, a_t) = r(s_t, a_t) + \gamma \mathbb{E}_{\pi, P}[Q^{\pi}(s_{t+1}, a_{t+1})]$, with which we can express $J$ in the alternate form $J(\pi) = \mathbb{E}_{\pi, P}[Q^{\pi}(s_t, a_t) | s_0 \sim \rho_0(s)]$. Furthermore, we consider a policy iteration scheme [5] with additional KL constraints [6, 7, 8]. In this setting the goal is to maximize the Q-values while staying close to a reference (or prior) policy $\pi_{prior}$. In particular, given a current policy $\pi_{i-1}$ that we want to improve upon, we can write the objective for iteration $i$ as a constrained optimization problem, assuming access to a dataset $\mathcal{D}$:

$$\pi_i = \arg\max_{\pi} J_c(\pi, \pi_{prior}, \epsilon) = \arg\max_{\pi} \mathbb{E}_{s \sim \mathcal{D}} \mathbb{E}_{a \sim \pi(\cdot|s)}[Q^{\pi_{i-1}}(a, s)]$$

$$\text{s.t. } \forall s \in \mathcal{D}: \text{KL}(\pi(\cdot|s) \| \pi_{prior}(\cdot|s)) \leq \epsilon, \qquad (1)$$

where the policy to be optimized is denoted as $\pi(a|s)$, $\pi_{prior}$ is the prior policy, and $\text{KL}$ denotes the Kullback-Leibler divergence. Note that from the perspective presented here, $\pi_{prior}$ is not necessarily a guess for an optimal policy but serves as the prior towards which we regularize.¹ Successively solving the optimization from Equation 1 for $i \in [1, N]$ – with interleaved policy evaluation to obtain $Q^{\pi}$ – then constitutes the policy iteration loop.

¹ Note that the per-state KL constraint is often relaxed to an average constraint over states from the buffer; e.g. in Nair et al. [4], Abdolmaleki et al. [7], Siegel et al. [9].

---

### النسخة العربية

نعتبر إعداد التعلم المعزز القياسي في عملية قرار ماركوف (MDP) الموصوفة بالمجموعة المرتبة $(S, A, r, \gamma, P, \rho_0)$ التي تتكون من: فضاء الحالات $S$، وفضاء الأفعال $A$، ودالة المكافأة اللحظية $r(s_t, a_t)$ – التي يتم الحصول عليها بتنفيذ الفعل $a_t$ في الحالة $s_t$ – وعامل الخصم $\gamma$، وتوزيع الانتقال $P(s_{t+1}|s_t, a_t)$ وتوزيع الحالة الأولية $\rho_0$. يقابل هدف التعلم المعزز $J$ تعظيم المكافأة المتوقعة تحت سياسة معينة $J(\pi) = \mathbb{E}_{\pi, P}[\sum_{t=0}^{\infty} \gamma^t r(s_t, a_t) | s_0 \sim \rho_0(s)]$، حيث لدينا $a_t \sim \pi(\cdot|s_t)$ و $s_{t+1} \sim P(\cdot|s_t, a_t)$. نستخدم $\pi^* = \arg\max_{\pi} J(\pi)$ للإشارة إلى السياسة المثلى. نستخدم دالة قيمة الحالة-الفعل للسياسة $\pi$، والمعروفة أيضاً بدالة Q والتي يمكن تعريفها بشكل تكراري كـ $Q^{\pi}(s_t, a_t) = r(s_t, a_t) + \gamma \mathbb{E}_{\pi, P}[Q^{\pi}(s_{t+1}, a_{t+1})]$، والتي يمكننا من خلالها التعبير عن $J$ بالصيغة البديلة $J(\pi) = \mathbb{E}_{\pi, P}[Q^{\pi}(s_t, a_t) | s_0 \sim \rho_0(s)]$. علاوة على ذلك، نعتبر مخطط تكرار السياسة [5] مع قيود KL إضافية [6، 7، 8]. في هذا الإعداد، الهدف هو تعظيم قيم Q مع البقاء قريباً من سياسة مرجعية (أو مُسبَق) $\pi_{prior}$. على وجه الخصوص، بالنظر إلى سياسة حالية $\pi_{i-1}$ نريد تحسينها، يمكننا كتابة الهدف للتكرار $i$ كمسألة تحسين مقيدة، بافتراض الوصول إلى مجموعة بيانات $\mathcal{D}$:

$$\pi_i = \arg\max_{\pi} J_c(\pi, \pi_{prior}, \epsilon) = \arg\max_{\pi} \mathbb{E}_{s \sim \mathcal{D}} \mathbb{E}_{a \sim \pi(\cdot|s)}[Q^{\pi_{i-1}}(a, s)]$$

$$\text{بشرط } \forall s \in \mathcal{D}: \text{KL}(\pi(\cdot|s) \| \pi_{prior}(\cdot|s)) \leq \epsilon, \qquad (1)$$

حيث يُشار إلى السياسة المراد تحسينها بـ $\pi(a|s)$، و $\pi_{prior}$ هي السياسة المُسبَقة، و $\text{KL}$ يشير إلى تباعد كولباك-لايبلر. لاحظ أنه من المنظور المقدم هنا، $\pi_{prior}$ ليست بالضرورة تخميناً للسياسة المثلى ولكنها تعمل كمُسبَق نقوم بالتنظيم تجاهه.¹ الحل المتعاقب للتحسين من المعادلة 1 لـ $i \in [1, N]$ – مع تقييم السياسة المتداخل للحصول على $Q^{\pi}$ – يشكل إذن حلقة تكرار السياسة.

¹ لاحظ أن قيد KL لكل حالة غالباً ما يُخفف إلى قيد متوسط على الحالات من المخزن المؤقت؛ على سبيل المثال في Nair وآخرون [4]، Abdolmaleki وآخرون [7]، Siegel وآخرون [9].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Markov Decision Process (MDP), state-action value function, Q-function, KL constraint, prior policy, policy iteration
- **Equations:** 1 main equation with mathematical notation
- **Citations:** [4, 5, 6, 7, 8, 9]
- **Special handling:** LaTeX mathematical notation preserved; equations kept in original format with Arabic explanation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
