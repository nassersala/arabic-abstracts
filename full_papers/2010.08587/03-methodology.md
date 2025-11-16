# Section 3-4: Methodology (Relative Entropy Q-Learning & RL from Suboptimal Experts)
## القسم 3-4: المنهجية (التعلم-Q بالإنتروبيا النسبية والتعلم المعزز من الخبراء غير المثاليين)

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** policy iteration, KL constraint, importance sampling, Q-function, prior policy, temporal difference, target network, softmax Bellman operator, trust region, waypoint tracking, suboptimal expert, exploration strategy

---

### English Version

## 3 Relative Entropy Q-Learning

We introduce Relative Entropy Q-Learning (REQ). REQ is a policy iteration algorithm targeting the KL-constrained RL objective $J_c$ from Equation 1 in each iteration. We start by realizing that the solution to the KL-constrained objective at iteration $i$, $\pi_i = \arg\max_{\pi} J_c(\pi, \pi_{prior}^i, \epsilon)$, can be obtained in closed form by formulating the Lagrangian of the constrained optimization problem and solving for $\pi$. The solution consists of a softmax over Q-values (a well known result, see e.g. [6, 7, 8, 9, 10]) $\pi_i(a|s) \propto \pi_{prior}^i(a|s) \exp(Q^{\pi_{i-1}}(s, a)/\tau_s)$ where the temperature $\tau_s$ can be obtained by solving the dual function of $J_c$; a convex optimization problem. We refer to the Appendix A.3 for a derivation of the Lagrangian as well as how we optimize the dual function for $\tau_s$. Exactly calculating the normalization constant is intractable in continuous action spaces but we can, however, sample from $\pi_i(a|s)$ via importance weighting of samples from $\pi_{prior}^i$ – an observation that we will now use to define the REQ policy evaluation step.

**Policy Evaluation** The first key observation is that we can learn the state-action value function of $\pi_i$ without the need to explicitly represent $\pi_i$ via a parametric policy. Instead, we can realize that the squared temporal difference error $(Q^{\pi_i}(s_t, a_t) - (r(s_t, a_t) + \gamma \mathbb{E}_{\pi_i}[Q^{\pi_i}(s_{t+1}, a_{t+1})]))^2$ can be evaluated using importance sampling, leading to the following objective:

$$Q^{\pi_i} = \arg\min_Q \mathbb{E}_{s,a,r,s' \sim \mathcal{D}} \left[ \left( Q(s, a) - \left[ r + \gamma \sum_{j=1}^N \frac{\exp(Q_{\theta'}(s', a_j)/\tau_{s'})}{\sum_k \exp(Q_{\theta'}(s', a_k)/\tau_{s'})} Q_{\theta'}(s', a_j) \right] \right)^2 \right], \qquad (2)$$

with $\forall j: a_j \sim \pi_{prior}^i(\cdot|s')$, where $\theta'$ denotes the parameters of a target network [11] and we estimate the expectation $\mathbb{E}_{\pi_i}[Q(s', a)] \propto \mathbb{E}_{a' \sim \pi_{prior}(\cdot|s')}[\exp(Q(s', a')/\tau_{s'})Q(s', a')]$ with self-normalized importance sampling based on $N$ samples.

A few observations can be made about this objective. The learned Q-function corresponds to the one considered in ABM+MPO [9], but with the difference that $\pi_i$ is never projected onto a parametric policy. Instead it is only implicitly represented via importance sampling from the prior – we thus only need to learn $\pi_{prior}$ and a Q-function. This can be beneficial when the prior is learned from data but is not well aligned with high-value regions in $Q^{\pi_i}$. In such a case $\pi_i$ may become multimodal and hard to project to a parametric policy without accumulation of errors. Note that REQ can still represent the optimal policy, as for $\epsilon \to \infty$ the policy $\pi_i$ will approach $\pi^*$. Hence, the constraint $\epsilon$ allows us to trade-off the exploitation of the Q-function and regularizing towards prior. An alternative view of the REQ policy evaluation is to consider it as a policy iteration algorithm that uses the softmax Bellman operator [12, 13] for policy evaluation (with an adaptive method to satisfy a hard KL constraint with respect to a given prior). Further analysis of the REQ policy evaluation is provided in the Appendix A.2.

**Prior Policy Improvement** The Q-learning like algorithm from above can work with any prior as long as $\pi_{prior}$ has probability mass everywhere; $\pi_{prior}(a|s) > 0 \; \forall a$. However, the sample based importance weighting scheme from Equation 2 becomes ineffective – potentially leading to learning Q-values of a suboptimal policy – if the number of samples $N$ is low and the prior has small probability mass at actions with high Q-values. The policy improvement step of REQ thus is to learn an effective prior, $\pi_{prior}^i$, and improve it in each iteration. We achieve this by fitting the prior to all actions from the dataset, $\mathcal{D}$, whose value is estimated to be higher than the average value of the policy. Formally, we find

$$\pi_{prior}^{i+1} = \arg\max_{\pi_{prior}} \mathbb{E}_{a,s \sim \mathcal{D}} \left[ \mathbb{1} \left[ Q_{\theta'}^{\pi_i}(s, a) \geq \mathbb{E}_{a \sim \pi_i(\cdot|s)}[Q_{\theta'}^{\pi_i}(s, a)] \right] \log \pi_{prior}(a|s) \right], \qquad (3)$$

where $\mathbb{1}$ is the indicator function. That is, we consider learning a prior similar to recent offline RL algorithms such as ABM [9] and CRR-bin [3]. To avoid overfitting during training (e.g. due to suboptimal Q-values shrinking the prior distribution) we additionally regularize the prior update step. In particular, we employ constraints on the movement of the prior-policy mean ($\text{KL}(\pi_{prior}^{i+1}(a|s) \| \pi_{prior}^i(a|s; \mu = \mu_i)) < \epsilon_\mu$) and the covariance ($\text{KL}(\pi_{prior}^{i+1}(a|s) \| \pi_{prior}^i(a|s; \Sigma = \Sigma_i)) < \epsilon_\Sigma$) for a Gaussian prior – analogous to the trust-regions used for policy optimization in MPO [7], which we can enforce via a simple Lagrangian relaxation approach similar to MPO [8].

**Practical algorithm** A full listing of our procedure is presented in Algorithm 1. In contrast to previous works [7], we formulate a per-state KL constraint $\tau_s$ that we optimize for each state in the batch; i.e. we perform multiple gradient steps on the dual for a given $s$ to ensure the constraint is tight. In addition, instead of fully optimizing the policy and Q-function in each iteration, we switch to a new iteration after a fixed amount of gradient descent steps (via the use of target networks).

**Algorithm 1** Relative Entropy Q-learning (REQ)

**Input:** number of learning steps $N$, steps between target updates $U$, number of action samples $M$, KL regularization parameter $\epsilon$, initial parameters for $\theta, \phi$ and $\tau_s$

```
def REQ_update(θ, φ, τ, B):
    // For this step let π(a|s) ∝ π_φ'(a|s) exp(Q_θ'(a,s)/τ_s) and A(a,s) = Q_θ'(a,s) - V(a,s)

    Find τ_s for s ∈ B via gradient: ∇_τ 1/|B| Σ_s (ε + τ_s log(1/M Σ_j=1^M exp(Q_θ'(s,a_j)/τ_s))) | a_j ~ π_φ'(·,s)

    Compute V(s) = (Σ_j=1^M exp(Q_θ'(a_j,s)/τ_s))/(Σ_j=1^M exp(Q_θ'(a_j,s)/τ_s)) Q_θ'(a_j,s), where a_j ~ π_φ_prior'(·|s)

    Update Q-function with gradient: ∇_θ 1/|B| Σ_(s,a,r,s'∈B) (r + γV(s') - Q(a,s))^2

    Update prior with gradient: ∇_φ 1/|B| Σ_(s,a,r∈B) 𝟙[A(a,s)≥0] log π(a|s)

Initialize: i = 0, θ' = θ, φ' = φ
while i ≤ N do
    Optionally: collect new data D_i by following π_i or some mixture of π_i and an expert policy ρ
    Let D ← D ∪ D_i
    sample a batch B from replay buffer D
    execute REQ_update(θ, φ, τ, B)
    Update policy and Q-function every U steps by copying: θ' ← θ, φ' ← φ
end while
```

## 4 Reinforcement Learning from Suboptimal Experts

In this section we explain how our method can be used for reinforcement learning from suboptimal experts and describe a class of suboptimal experts for robotic manipulation consisting of simple waypoint tracking controllers.

**Problem Formulation** We consider an RL setting with additional access to a suboptimal expert $\rho(a|s)$. We assume that $\rho$ exhibits behaviors that are relevant to the task but is not necessarily the optimal policy $\pi^*$. We refer to this setting as Reinforcement Learning from Suboptimal Experts (RLfSE). In RLfSE, our policy iteration scheme can be understood as a form of sample-based approximate policy iteration from mixed behavior data – somewhat similar to the AggreVaTe family of algorithms [14, 15]. This setting is motivated by real world problems for which domain-specific solutions are already deployed. RLfSE can give us access to broader data distributions than reinforcement learning from demonstrations (RLfD [1, 2]), as we can choose to collect data from $\rho$ or a mixture of $\pi$ and $\rho$. Additionally, direct access to $\rho$ also allows us to label off-policy data with the expert's actions, similar to commonly used no-regret imitation learning algorithms [14, 16, 17].

**Waypoint Tracking Controllers** As a concrete example, for each manipulation task, we construct a suboptimal expert $\rho(a|s)$ by composing waypoint (pose) tracking controllers. (Note $\rho$ is deterministic in our case, thus we can write $a = \rho(s)$.) Such pose tracking controllers can be formulated by leveraging differential kinematics as well as velocity control modes of robotic arms. Using relative reference frames, these controllers can generalize under homogeneous transformations and provide an intuitive interface for humans to specify waypoints to follow. The pose controllers that we use are linear feedback controllers on the end-effector(s) of the robot arm(s) using velocity control. Formally we use $\rho(s) = [\nu_p(s), \nu_o(s)]$ for each controllable six degree of freedom with $\nu_p(s) = K_p e_p(s)$ and $\nu_o(s) = K_o e_o(s)$ where $K_p$ and $K_o$ are positive definite gain matrices. The position error is $e_p(s) = p_d(s) - p_t(s)$, where $p_t$ and $p_d$ are the measured and desired positions of the end-effector, respectively. We define the orientation error using unit quaternions where $Q_d = \{\eta_d, \vec{\epsilon}_d\}$ and $Q_t = \{\eta_t, \vec{\epsilon}_t\}$ represent the desired and measured orientations respectively, with $\eta$ representing the real valued quaternion components and $\vec{\epsilon}$ the imaginary values. We define the orientation error as $e_o(s) = \eta_t(s)\vec{\epsilon}_d(s) - \eta_d(s)\vec{\epsilon}_t(s) - S(\vec{\epsilon}_d(s))\vec{\epsilon}_t(s)$ where $S(\cdot)$ is the skew-symmetric operator [18]. Additional details of the composition of the waypoint tracking controller are presented in Appendix A.4.

**Relative Entropy Q-learning from Suboptimal Experts** To make use of the suboptimal expert $\rho$, we propose a simple exploration strategy: intertwining the execution of the current policy with the execution of $\rho$. For each episode we first randomly choose with probability $p_{intertwine}$ whether to execute a mix of the policy and the expert or either of the policy or the expert only. In episodes in which we choose actions according to a mixture of policy and expert we execute expert's action with probability $p_\rho$ at every time step. Otherwise, we execute the entire episode with probability $p_\pi$. This is illustrated in Figure 1 and the full procedure is presented in Appendix A.5 Algorithm 3. Note that setting $p_{intertwine} = 0$ recovers the RLfD setting, where a certain portion of the data in the replay buffer are demonstrations from the suboptimal expert $\rho$. In addition to using $\rho$ for data generation, we can also take advantage of access to the expert in the prior policy improvement step of REQ by using the following equation,

$$\pi_{prior}^{i+1} = \arg\max_\pi \mathbb{E}_{a,s \sim \mathcal{D}} \left[ \mathbb{1}[A_q(a,s) \geq 0] \right] + \mathbb{E}_{a \sim \rho} \left[ \mathbb{1}[A_q(a,s) \geq 0] \log \pi(a|s) \right], \qquad (4)$$

where we now consider actions sampled from $\mathcal{D}$ and actions from the expert $\rho$ for inclusion into the prior, by evaluating the suboptimal expert on states from $\mathcal{D}$. Note that since $\rho$ is deterministic in our case, i.e. the expectation is over a delta distribution and can be evaluated using the single $a = \rho(s)$.

---

### النسخة العربية

## 3 التعلم-Q بالإنتروبيا النسبية

نقدم التعلم-Q بالإنتروبيا النسبية (REQ). REQ هي خوارزمية تكرار سياسة تستهدف هدف التعلم المعزز المقيد بـ KL وهو $J_c$ من المعادلة 1 في كل تكرار. نبدأ بإدراك أن الحل للهدف المقيد بـ KL في التكرار $i$، $\pi_i = \arg\max_{\pi} J_c(\pi, \pi_{prior}^i, \epsilon)$، يمكن الحصول عليه في صورة مغلقة من خلال صياغة لاغرانجيان لمسألة التحسين المقيدة وحل $\pi$. يتكون الحل من softmax على قيم Q (نتيجة معروفة، انظر على سبيل المثال [6، 7، 8، 9، 10]) $\pi_i(a|s) \propto \pi_{prior}^i(a|s) \exp(Q^{\pi_{i-1}}(s, a)/\tau_s)$ حيث يمكن الحصول على درجة الحرارة $\tau_s$ من خلال حل الدالة الثنائية لـ $J_c$؛ وهي مسألة تحسين محدبة. نشير إلى الملحق A.3 لاشتقاق اللاغرانجيان وكذلك كيفية تحسين الدالة الثنائية لـ $\tau_s$. حساب ثابت التطبيع بدقة غير قابل للتتبع في فضاءات الأفعال المستمرة ولكن يمكننا، مع ذلك، أخذ عينات من $\pi_i(a|s)$ عبر ترجيح الأهمية للعينات من $\pi_{prior}^i$ – وهي ملاحظة سنستخدمها الآن لتعريف خطوة تقييم السياسة لـ REQ.

**تقييم السياسة** الملاحظة الرئيسية الأولى هي أنه يمكننا تعلم دالة قيمة الحالة-الفعل لـ $\pi_i$ دون الحاجة إلى تمثيل $\pi_i$ صراحةً عبر سياسة بارامترية. بدلاً من ذلك، يمكننا إدراك أن خطأ الفرق الزمني المربع $(Q^{\pi_i}(s_t, a_t) - (r(s_t, a_t) + \gamma \mathbb{E}_{\pi_i}[Q^{\pi_i}(s_{t+1}, a_{t+1})]))^2$ يمكن تقييمه باستخدام أخذ العينات بالأهمية، مما يؤدي إلى الهدف التالي:

$$Q^{\pi_i} = \arg\min_Q \mathbb{E}_{s,a,r,s' \sim \mathcal{D}} \left[ \left( Q(s, a) - \left[ r + \gamma \sum_{j=1}^N \frac{\exp(Q_{\theta'}(s', a_j)/\tau_{s'})}{\sum_k \exp(Q_{\theta'}(s', a_k)/\tau_{s'})} Q_{\theta'}(s', a_j) \right] \right)^2 \right], \qquad (2)$$

مع $\forall j: a_j \sim \pi_{prior}^i(\cdot|s')$، حيث $\theta'$ يشير إلى بارامترات شبكة الهدف [11] ونقدر التوقع $\mathbb{E}_{\pi_i}[Q(s', a)] \propto \mathbb{E}_{a' \sim \pi_{prior}(\cdot|s')}[\exp(Q(s', a')/\tau_{s'})Q(s', a')]$ مع أخذ العينات بالأهمية المطبّع ذاتياً بناءً على $N$ عينة.

يمكن إجراء بضع ملاحظات حول هذا الهدف. تقابل دالة Q المتعلمة تلك المعتبرة في ABM+MPO [9]، ولكن مع الاختلاف أن $\pi_i$ لا يتم إسقاطها أبداً على سياسة بارامترية. بدلاً من ذلك يتم تمثيلها فقط ضمنياً عبر أخذ العينات بالأهمية من المُسبَق – وبالتالي نحتاج فقط إلى تعلم $\pi_{prior}$ ودالة Q. يمكن أن يكون هذا مفيداً عندما يتم تعلم المُسبَق من البيانات ولكنه لا يتماشى بشكل جيد مع مناطق القيمة العالية في $Q^{\pi_i}$. في مثل هذه الحالة قد تصبح $\pi_i$ متعددة الأنماط ويصعب إسقاطها على سياسة بارامترية دون تراكم الأخطاء. لاحظ أن REQ لا يزال بإمكانها تمثيل السياسة المثلى، حيث أنه لـ $\epsilon \to \infty$ فإن السياسة $\pi_i$ ستقترب من $\pi^*$. وبالتالي، فإن القيد $\epsilon$ يسمح لنا بالمفاضلة بين استغلال دالة Q والتنظيم نحو المُسبَق. النظرة البديلة لتقييم سياسة REQ هي اعتباره خوارزمية تكرار سياسة تستخدم معامل بيلمان softmax [12، 13] لتقييم السياسة (مع طريقة تكيفية لتلبية قيد KL صارم فيما يتعلق بمُسبَق معين). يتم توفير مزيد من التحليل لتقييم سياسة REQ في الملحق A.2.

**تحسين السياسة المُسبَقة** يمكن لخوارزمية التعلم-Q المذكورة أعلاه أن تعمل مع أي مُسبَق طالما أن $\pi_{prior}$ له كتلة احتمالية في كل مكان؛ $\pi_{prior}(a|s) > 0 \; \forall a$. ومع ذلك، يصبح مخطط ترجيح الأهمية القائم على العينات من المعادلة 2 غير فعال – مما قد يؤدي إلى تعلم قيم Q لسياسة غير مثلى – إذا كان عدد العينات $N$ منخفضاً وكان للمُسبَق كتلة احتمالية صغيرة عند الأفعال ذات قيم Q العالية. وبالتالي فإن خطوة تحسين السياسة لـ REQ هي تعلم مُسبَق فعال، $\pi_{prior}^i$، وتحسينه في كل تكرار. نحقق ذلك من خلال ملاءمة المُسبَق لجميع الأفعال من مجموعة البيانات، $\mathcal{D}$، التي تقدر قيمتها بأنها أعلى من متوسط قيمة السياسة. رسمياً، نجد

$$\pi_{prior}^{i+1} = \arg\max_{\pi_{prior}} \mathbb{E}_{a,s \sim \mathcal{D}} \left[ \mathbb{1} \left[ Q_{\theta'}^{\pi_i}(s, a) \geq \mathbb{E}_{a \sim \pi_i(\cdot|s)}[Q_{\theta'}^{\pi_i}(s, a)] \right] \log \pi_{prior}(a|s) \right], \qquad (3)$$

حيث $\mathbb{1}$ هي دالة المؤشر. أي أننا نعتبر تعلم مُسبَق مشابه لخوارزميات التعلم المعزز غير المتصل بالإنترنت الحديثة مثل ABM [9] و CRR-bin [3]. لتجنب الإفراط في التكييف أثناء التدريب (على سبيل المثال بسبب قيم Q غير المثلى التي تقلص توزيع المُسبَق) نقوم بتنظيم خطوة تحديث المُسبَق بشكل إضافي. على وجه الخصوص، نوظف قيوداً على حركة متوسط السياسة المُسبَقة ($\text{KL}(\pi_{prior}^{i+1}(a|s) \| \pi_{prior}^i(a|s; \mu = \mu_i)) < \epsilon_\mu$) والتباين المشترك ($\text{KL}(\pi_{prior}^{i+1}(a|s) \| \pi_{prior}^i(a|s; \Sigma = \Sigma_i)) < \epsilon_\Sigma$) لمُسبَق غاوسي – بما يماثل مناطق الثقة المستخدمة لتحسين السياسة في MPO [7]، والتي يمكننا فرضها عبر نهج استرخاء لاغرانجي بسيط مشابه لـ MPO [8].

**خوارزمية عملية** يتم تقديم قائمة كاملة بإجراءنا في الخوارزمية 1. على النقيض من الأعمال السابقة [7]، نصيغ قيد KL لكل حالة $\tau_s$ الذي نحسنه لكل حالة في الدفعة؛ أي نقوم بتنفيذ خطوات متعددة من الانحدار التدرجي على الثنائي لـ $s$ معين لضمان إحكام القيد. بالإضافة إلى ذلك، بدلاً من تحسين السياسة ودالة Q بالكامل في كل تكرار، ننتقل إلى تكرار جديد بعد عدد ثابت من خطوات الانحدار التدرجي (عبر استخدام شبكات الهدف).

**الخوارزمية 1** التعلم-Q بالإنتروبيا النسبية (REQ)

**مدخلات:** عدد خطوات التعلم $N$، الخطوات بين تحديثات الهدف $U$، عدد عينات الأفعال $M$، بارامتر تنظيم KL وهو $\epsilon$، البارامترات الأولية لـ $\theta, \phi$ و $\tau_s$

```
def REQ_update(θ, φ, τ, B):
    // لهذه الخطوة دع π(a|s) ∝ π_φ'(a|s) exp(Q_θ'(a,s)/τ_s) و A(a,s) = Q_θ'(a,s) - V(a,s)

    أوجد τ_s لـ s ∈ B عبر التدرج: ∇_τ 1/|B| Σ_s (ε + τ_s log(1/M Σ_j=1^M exp(Q_θ'(s,a_j)/τ_s))) | a_j ~ π_φ'(·,s)

    احسب V(s) = (Σ_j=1^M exp(Q_θ'(a_j,s)/τ_s))/(Σ_j=1^M exp(Q_θ'(a_j,s)/τ_s)) Q_θ'(a_j,s)، حيث a_j ~ π_φ_prior'(·|s)

    حدث دالة Q بالتدرج: ∇_θ 1/|B| Σ_(s,a,r,s'∈B) (r + γV(s') - Q(a,s))^2

    حدث المُسبَق بالتدرج: ∇_φ 1/|B| Σ_(s,a,r∈B) 𝟙[A(a,s)≥0] log π(a|s)

تهيئة: i = 0, θ' = θ, φ' = φ
بينما i ≤ N قم بـ
    اختيارياً: جمع بيانات جديدة D_i باتباع π_i أو مزيج من π_i وسياسة خبير ρ
    دع D ← D ∪ D_i
    عينة دفعة B من المخزن المؤقت لإعادة التشغيل D
    نفذ REQ_update(θ, φ, τ, B)
    حدث السياسة ودالة Q كل U خطوة بالنسخ: θ' ← θ, φ' ← φ
نهاية بينما
```

## 4 التعلم المعزز من الخبراء غير المثاليين

في هذا القسم نوضح كيف يمكن استخدام طريقتنا للتعلم المعزز من الخبراء غير المثاليين ونصف فئة من الخبراء غير المثاليين للتلاعب الروبوتي تتكون من متحكمات تتبع نقاط المسار البسيطة.

**صياغة المسألة** نعتبر إعداد تعلم معزز مع وصول إضافي إلى خبير غير مثالي $\rho(a|s)$. نفترض أن $\rho$ يُظهر سلوكيات ذات صلة بالمهمة ولكنه ليس بالضرورة السياسة المثلى $\pi^*$. نشير إلى هذا الإعداد باسم التعلم المعزز من الخبراء غير المثاليين (RLfSE). في RLfSE، يمكن فهم مخطط تكرار السياسة لدينا كشكل من أشكال تكرار السياسة التقريبي القائم على العينات من بيانات سلوك مختلطة – مشابه إلى حد ما لعائلة خوارزميات AggreVaTe [14، 15]. هذا الإعداد مدفوع بمشاكل العالم الحقيقي التي يتم فيها نشر حلول خاصة بالمجال بالفعل. يمكن لـ RLfSE أن يمنحنا الوصول إلى توزيعات بيانات أوسع من التعلم المعزز من العروض التوضيحية (RLfD [1، 2])، حيث يمكننا اختيار جمع البيانات من $\rho$ أو مزيج من $\pi$ و $\rho$. بالإضافة إلى ذلك، فإن الوصول المباشر إلى $\rho$ يسمح لنا أيضاً بتسمية البيانات خارج السياسة بأفعال الخبير، بشكل مشابه لخوارزميات التعلم بالتقليد بدون ندم المستخدمة عادة [14، 16، 17].

**متحكمات تتبع نقاط المسار** كمثال ملموس، لكل مهمة تلاعب، نبني خبيراً غير مثالي $\rho(a|s)$ من خلال تركيب متحكمات تتبع نقاط المسار (الوضعية). (لاحظ أن $\rho$ حتمي في حالتنا، وبالتالي يمكننا كتابة $a = \rho(s)$.) يمكن صياغة متحكمات تتبع الوضعية هذه من خلال الاستفادة من الحركيات التفاضلية وكذلك أوضاع التحكم في السرعة للأذرع الروبوتية. باستخدام الإطارات المرجعية النسبية، يمكن لهذه المتحكمات التعميم تحت التحويلات المتجانسة وتوفير واجهة بديهية للبشر لتحديد نقاط المسار التي يجب اتباعها. متحكمات الوضعية التي نستخدمها هي متحكمات تغذية راجعة خطية على المُنفذ(ات) الطرفي(ة) لذراع(أذرع) الروبوت باستخدام التحكم في السرعة. رسمياً نستخدم $\rho(s) = [\nu_p(s), \nu_o(s)]$ لكل ست درجات حرية قابلة للتحكم مع $\nu_p(s) = K_p e_p(s)$ و $\nu_o(s) = K_o e_o(s)$ حيث $K_p$ و $K_o$ هي مصفوفات كسب محددة موجبة. خطأ الموضع هو $e_p(s) = p_d(s) - p_t(s)$، حيث $p_t$ و $p_d$ هما الموضعان المُقاس والمرغوب للمُنفذ الطرفي، على التوالي. نعرف خطأ الاتجاه باستخدام الرباعيات الوحدوية حيث $Q_d = \{\eta_d, \vec{\epsilon}_d\}$ و $Q_t = \{\eta_t, \vec{\epsilon}_t\}$ تمثل الاتجاهات المرغوبة والمُقاسة على التوالي، مع $\eta$ تمثل مكونات الرباعية ذات القيمة الحقيقية و $\vec{\epsilon}$ القيم الخيالية. نعرف خطأ الاتجاه كـ $e_o(s) = \eta_t(s)\vec{\epsilon}_d(s) - \eta_d(s)\vec{\epsilon}_t(s) - S(\vec{\epsilon}_d(s))\vec{\epsilon}_t(s)$ حيث $S(\cdot)$ هو المعامل المنحرف المتماثل [18]. تُعرض تفاصيل إضافية لتركيب متحكم تتبع نقاط المسار في الملحق A.4.

**التعلم-Q بالإنتروبيا النسبية من الخبراء غير المثاليين** للاستفادة من الخبير غير المثالي $\rho$، نقترح استراتيجية استكشاف بسيطة: تشابك تنفيذ السياسة الحالية مع تنفيذ $\rho$. لكل حلقة نختار أولاً بشكل عشوائي باحتمالية $p_{intertwine}$ ما إذا كنا سننفذ مزيجاً من السياسة والخبير أو إما السياسة أو الخبير فقط. في الحلقات التي نختار فيها الأفعال وفقاً لمزيج من السياسة والخبير ننفذ فعل الخبير باحتمالية $p_\rho$ في كل خطوة زمنية. وإلا، ننفذ الحلقة بأكملها باحتمالية $p_\pi$. يتم توضيح ذلك في الشكل 1 ويتم تقديم الإجراء الكامل في الملحق A.5 الخوارزمية 3. لاحظ أن تعيين $p_{intertwine} = 0$ يسترجع إعداد RLfD، حيث يكون جزء معين من البيانات في المخزن المؤقت لإعادة التشغيل عروضاً توضيحية من الخبير غير المثالي $\rho$. بالإضافة إلى استخدام $\rho$ لتوليد البيانات، يمكننا أيضاً الاستفادة من الوصول إلى الخبير في خطوة تحسين السياسة المُسبَقة لـ REQ باستخدام المعادلة التالية:

$$\pi_{prior}^{i+1} = \arg\max_\pi \mathbb{E}_{a,s \sim \mathcal{D}} \left[ \mathbb{1}[A_q(a,s) \geq 0] \right] + \mathbb{E}_{a \sim \rho} \left[ \mathbb{1}[A_q(a,s) \geq 0] \log \pi(a|s) \right], \qquad (4)$$

حيث نعتبر الآن الأفعال المأخوذة من $\mathcal{D}$ والأفعال من الخبير $\rho$ لإدراجها في المُسبَق، من خلال تقييم الخبير غير المثالي على الحالات من $\mathcal{D}$. لاحظ أنه نظراً لأن $\rho$ حتمي في حالتنا، أي أن التوقع على توزيع دلتا ويمكن تقييمه باستخدام $a = \rho(s)$ الواحد.

---

### Translation Notes

- **Figures referenced:** Figure 1 (referenced in Section 4)
- **Key terms introduced:** Relative Entropy Q-Learning (REQ), importance weighting, softmax Bellman operator, prior policy improvement, waypoint tracking controllers, RLfSE
- **Equations:** 3 main equations (Equations 2, 3, 4)
- **Citations:** [1-20]
- **Special handling:** Algorithm pseudocode translated with English code preserved; mathematical notation maintained; quaternion mathematics explained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
