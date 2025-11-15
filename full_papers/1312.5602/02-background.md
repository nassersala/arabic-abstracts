# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.89
**Glossary Terms Used:** reinforcement learning, Markov decision process, policy, value function, Q-learning, Bellman equation, function approximation, neural network, temporal difference

---

### English Version

We consider tasks in which an agent interacts with an environment $\mathcal{E}$, in this case the Atari emulator, in a sequence of actions, observations and rewards. At each time-step the agent selects an action $a_t$ from the set of legal game actions, $\mathcal{A} = \{1, \ldots, K\}$. The action is passed to the emulator and modifies its internal state and the game score. In general $\mathcal{E}$ may be stochastic. The emulator's internal state is not observed by the agent; instead it observes an image $x_t \in \mathbb{R}^d$ from the emulator, which is a vector of raw pixel values representing the current screen. In addition it receives a reward $r_t$ representing the change in game score. Note that in general the game score may depend on the whole prior sequence of actions and observations; feedback about an action may only be received after many thousands of time-steps have elapsed.

Since the agent only observes images of the current screen, the task is partially observable and many emulator states are perceptually aliased, i.e. it is impossible to fully understand the current situation from only the current screen $x_t$. We therefore consider sequences of actions and observations, $s_t = x_1, a_1, x_2, \ldots, a_{t-1}, x_t$, and learn game strategies that depend upon these sequences. All sequences in the emulator are assumed to terminate in a finite number of time-steps. This gives rise to a large but finite Markov decision process (MDP) in which each sequence is a distinct state. As a result, we can apply standard reinforcement learning methods for MDPs, simply by using the complete sequence $s_t$ as the state representation at time $t$.

The goal of the agent is to interact with the emulator by selecting actions in a way that maximises future rewards. We make the standard assumption that future rewards are discounted by a factor of $\gamma$ per time-step, and define the future discounted return at time $t$ as $R_t = \sum_{t'=t}^{T} \gamma^{t'-t} r_{t'}$, where $T$ is the time-step at which the game terminates. We define the optimal action-value function $Q^*(s,a)$ as the maximum expected return achievable by following any strategy, after seeing some sequence $s$ and then taking some action $a$, $Q^*(s,a) = \max_\pi \mathbb{E}[R_t \mid s_t = s, a_t = a, \pi]$, where $\pi$ is a policy mapping sequences to actions (or distributions over actions).

The optimal action-value function obeys an important identity known as the Bellman equation. This is based on the following intuition: if the optimal value $Q^*(s',a')$ of the sequence $s'$ at the next time-step was known for all possible actions $a'$, then the optimal strategy is to select the action $a'$ maximising the expected value of $r + \gamma Q^*(s',a')$,

$$Q^*(s,a) = \mathbb{E}_{s' \sim \mathcal{E}} [r + \gamma \max_{a'} Q^*(s',a') \mid s,a]$$

The basic idea behind many reinforcement learning algorithms is to estimate the action-value function, by using the Bellman equation as an iterative update, $Q_{i+1}(s,a) = \mathbb{E}[r + \gamma \max_{a'} Q_i(s',a') \mid s,a]$. Such value iteration algorithms converge to the optimal action-value function, $Q_i \to Q^*$ as $i \to \infty$. In practice, this basic approach is totally impractical, because the action-value function is estimated separately for each sequence, without any generalisation. Instead, it is common to use a function approximator to estimate the action-value function, $Q(s,a; \theta) \approx Q^*(s,a)$. In the reinforcement learning community this is typically a linear function approximator, but sometimes a non-linear function approximator is used instead, such as a neural network. We refer to a neural network function approximator with weights $\theta$ as a Q-network. A Q-network can be trained by minimising a sequence of loss functions $L_i(\theta_i)$ that changes at each iteration $i$,

$$L_i(\theta_i) = \mathbb{E}_{s,a \sim \rho(\cdot)} [(y_i - Q(s,a; \theta_i))^2]$$

where $y_i = \mathbb{E}_{s' \sim \mathcal{E}}[r + \gamma \max_{a'} Q(s',a'; \theta_{i-1}) \mid s,a]$ is the target for iteration $i$ and $\rho(s,a)$ is a probability distribution over sequences $s$ and actions $a$ that we refer to as the behaviour distribution. The parameters from the previous iteration $\theta_{i-1}$ are held fixed when optimising the loss function $L_i(\theta_i)$. Note that the targets depend on the network weights; this is in contrast with the targets used for supervised learning, which are fixed before learning begins. Differentiating the loss function with respect to the weights we arrive at the following gradient,

$$\nabla_{\theta_i} L_i(\theta_i) = \mathbb{E}_{s,a \sim \rho(\cdot); s' \sim \mathcal{E}} [(r + \gamma \max_{a'} Q(s',a'; \theta_{i-1}) - Q(s,a; \theta_i)) \nabla_{\theta_i} Q(s,a; \theta_i)]$$

Rather than computing the full expectations in the above gradient, it is often computationally expedient to optimise the loss function by stochastic gradient descent. If the weights are updated after every time-step, and the expectations are replaced by single samples from the behaviour distribution $\rho$ and the emulator $\mathcal{E}$ respectively, then we arrive at the familiar Q-learning algorithm.

Note that this algorithm is model-free: it solves the reinforcement learning task directly using samples from the emulator $\mathcal{E}$, without explicitly constructing an estimate of $\mathcal{E}$. It is also off-policy: it learns about the greedy strategy $a = \max_a Q(s,a; \theta)$, while following a behaviour distribution that ensures adequate exploration of the state space. In practice, the behaviour distribution is often selected by an $\epsilon$-greedy strategy that follows the greedy strategy with probability $1 - \epsilon$ and selects a random action with probability $\epsilon$.

---

### النسخة العربية

نعتبر المهام التي يتفاعل فيها وكيل مع بيئة $\mathcal{E}$، في هذه الحالة محاكي Atari، في تسلسل من الإجراءات والملاحظات والمكافآت. في كل خطوة زمنية يختار الوكيل إجراءً $a_t$ من مجموعة إجراءات اللعبة القانونية، $\mathcal{A} = \{1, \ldots, K\}$. يتم تمرير الإجراء إلى المحاكي ويعدل حالته الداخلية ونقاط اللعبة. بشكل عام، قد تكون $\mathcal{E}$ عشوائية. لا يلاحظ الوكيل الحالة الداخلية للمحاكي؛ بدلاً من ذلك يلاحظ صورة $x_t \in \mathbb{R}^d$ من المحاكي، وهي متجه من قيم البكسلات الخام يمثل الشاشة الحالية. بالإضافة إلى ذلك يتلقى مكافأة $r_t$ تمثل التغيير في نقاط اللعبة. لاحظ أنه بشكل عام قد تعتمد نقاط اللعبة على التسلسل الكامل السابق من الإجراءات والملاحظات؛ قد يتم تلقي التعليقات حول إجراء ما فقط بعد مرور آلاف الخطوات الزمنية.

نظرًا لأن الوكيل يلاحظ فقط صور الشاشة الحالية، فإن المهمة قابلة للملاحظة جزئيًا والعديد من حالات المحاكي مستعارة إدراكيًا، أي أنه من المستحيل فهم الوضع الحالي بشكل كامل من الشاشة الحالية $x_t$ فقط. لذلك نعتبر تسلسلات من الإجراءات والملاحظات، $s_t = x_1, a_1, x_2, \ldots, a_{t-1}, x_t$، ونتعلم استراتيجيات اللعب التي تعتمد على هذه التسلسلات. يُفترض أن جميع التسلسلات في المحاكي تنتهي في عدد محدود من الخطوات الزمنية. يؤدي هذا إلى عملية قرار ماركوف (MDP) كبيرة ولكن محدودة حيث يكون كل تسلسل حالة متميزة. ونتيجة لذلك، يمكننا تطبيق أساليب التعلم المعزز القياسية لعمليات قرار ماركوف، ببساطة باستخدام التسلسل الكامل $s_t$ كتمثيل للحالة في الوقت $t$.

هدف الوكيل هو التفاعل مع المحاكي عن طريق اختيار الإجراءات بطريقة تزيد من المكافآت المستقبلية. نقوم بالافتراض القياسي بأن المكافآت المستقبلية مخصومة بعامل $\gamma$ لكل خطوة زمنية، ونعرّف العائد المخصوم المستقبلي في الوقت $t$ على أنه $R_t = \sum_{t'=t}^{T} \gamma^{t'-t} r_{t'}$، حيث $T$ هي الخطوة الزمنية التي تنتهي عندها اللعبة. نعرّف دالة قيمة الإجراء المثلى $Q^*(s,a)$ على أنها أقصى عائد متوقع يمكن تحقيقه باتباع أي استراتيجية، بعد رؤية تسلسل معين $s$ ثم اتخاذ إجراء معين $a$، $Q^*(s,a) = \max_\pi \mathbb{E}[R_t \mid s_t = s, a_t = a, \pi]$، حيث $\pi$ هي سياسة تربط التسلسلات بالإجراءات (أو التوزيعات على الإجراءات).

تطيع دالة قيمة الإجراء المثلى مطابقة مهمة تُعرف بمعادلة بيلمان. يستند هذا إلى الحدس التالي: إذا كانت القيمة المثلى $Q^*(s',a')$ للتسلسل $s'$ في الخطوة الزمنية التالية معروفة لجميع الإجراءات الممكنة $a'$، فإن الاستراتيجية المثلى هي اختيار الإجراء $a'$ الذي يزيد من القيمة المتوقعة لـ $r + \gamma Q^*(s',a')$،

$$Q^*(s,a) = \mathbb{E}_{s' \sim \mathcal{E}} [r + \gamma \max_{a'} Q^*(s',a') \mid s,a]$$

الفكرة الأساسية وراء العديد من خوارزميات التعلم المعزز هي تقدير دالة قيمة الإجراء، باستخدام معادلة بيلمان كتحديث تكراري، $Q_{i+1}(s,a) = \mathbb{E}[r + \gamma \max_{a'} Q_i(s',a') \mid s,a]$. تتقارب خوارزميات تكرار القيمة هذه إلى دالة قيمة الإجراء المثلى، $Q_i \to Q^*$ عندما $i \to \infty$. في الممارسة العملية، هذا النهج الأساسي غير عملي تمامًا، لأن دالة قيمة الإجراء يتم تقديرها بشكل منفصل لكل تسلسل، دون أي تعميم. بدلاً من ذلك، من الشائع استخدام مقرب دالي لتقدير دالة قيمة الإجراء، $Q(s,a; \theta) \approx Q^*(s,a)$. في مجتمع التعلم المعزز، هذا عادةً ما يكون مقرب دالي خطي، ولكن في بعض الأحيان يُستخدم مقرب دالي غير خطي بدلاً من ذلك، مثل الشبكة العصبية. نشير إلى مقرب دالي للشبكة العصبية بأوزان $\theta$ باسم شبكة-Q. يمكن تدريب شبكة-Q عن طريق تقليل تسلسل من دوال الخسارة $L_i(\theta_i)$ التي تتغير في كل تكرار $i$،

$$L_i(\theta_i) = \mathbb{E}_{s,a \sim \rho(\cdot)} [(y_i - Q(s,a; \theta_i))^2]$$

حيث $y_i = \mathbb{E}_{s' \sim \mathcal{E}}[r + \gamma \max_{a'} Q(s',a'; \theta_{i-1}) \mid s,a]$ هو الهدف للتكرار $i$ و $\rho(s,a)$ هو توزيع احتمالي على التسلسلات $s$ والإجراءات $a$ نشير إليه باسم توزيع السلوك. يتم تثبيت المعاملات من التكرار السابق $\theta_{i-1}$ عند تحسين دالة الخسارة $L_i(\theta_i)$. لاحظ أن الأهداف تعتمد على أوزان الشبكة؛ هذا على النقيض من الأهداف المستخدمة للتعلم الموجه، والتي يتم تثبيتها قبل بدء التعلم. بالتفاضل في دالة الخسارة بالنسبة للأوزان نصل إلى التدرج التالي،

$$\nabla_{\theta_i} L_i(\theta_i) = \mathbb{E}_{s,a \sim \rho(\cdot); s' \sim \mathcal{E}} [(r + \gamma \max_{a'} Q(s',a'; \theta_{i-1}) - Q(s,a; \theta_i)) \nabla_{\theta_i} Q(s,a; \theta_i)]$$

بدلاً من حساب التوقعات الكاملة في التدرج أعلاه، غالبًا ما يكون من المناسب حسابيًا تحسين دالة الخسارة عن طريق الانحدار التدرجي العشوائي. إذا تم تحديث الأوزان بعد كل خطوة زمنية، واستُبدلت التوقعات بعينات منفردة من توزيع السلوك $\rho$ والمحاكي $\mathcal{E}$ على التوالي، فإننا نصل إلى خوارزمية Q-learning المألوفة.

لاحظ أن هذه الخوارزمية خالية من النموذج: فهي تحل مهمة التعلم المعزز مباشرة باستخدام عينات من المحاكي $\mathcal{E}$، دون بناء تقدير صريح لـ $\mathcal{E}$. وهي أيضًا خارج السياسة: فهي تتعلم عن الاستراتيجية الجشعة $a = \max_a Q(s,a; \theta)$، بينما تتبع توزيع سلوك يضمن استكشافًا كافيًا لفضاء الحالة. في الممارسة العملية، غالبًا ما يتم اختيار توزيع السلوك بواسطة استراتيجية إبسيلون-جشعة التي تتبع الاستراتيجية الجشعة باحتمال $1 - \epsilon$ وتختار إجراءً عشوائيًا باحتمال $\epsilon$.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Markov decision process (عملية قرار ماركوف)
  - action-value function (دالة قيمة الإجراء)
  - Bellman equation (معادلة بيلمان)
  - Q-network (شبكة-Q)
  - value iteration (تكرار القيمة)
  - function approximator (مقرب دالي)
  - behaviour distribution (توزيع السلوك)
  - model-free (خالية من النموذج)
  - off-policy (خارج السياسة)
  - epsilon-greedy (إبسيلون-جشعة)
  - greedy strategy (استراتيجية جشعة)
  - discounted return (العائد المخصوم)
  - perceptually aliased (مستعارة إدراكيًا)

- **Equations:** 7 major equations covering Bellman equation, loss function, gradients
- **Citations:** 0
- **Special handling:**
  - All mathematical notation preserved in LaTeX
  - Greek symbols (γ, θ, π, ρ, ε) kept as-is in equations
  - Mathematical expressions maintained in original form
  - Technical terms like "MDP" translated but acronym kept

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89
