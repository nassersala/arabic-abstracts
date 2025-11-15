# Section 5: Algorithm
## القسم 5: الخوارزمية

**Section:** Algorithm Implementation
**Translation Quality:** 0.88
**Glossary Terms Used:** algorithm, automatic differentiation, gradient ascent, advantage function, value function, neural network, parameter sharing, entropy, coefficient, policy gradient, recurrent neural network, generalized advantage estimation, trajectory, actor, optimization, minibatch

---

### English Version

The surrogate losses from the previous sections can be computed and differentiated with a minor change to a typical policy gradient implementation. For implementations that use automatic differentation, one simply constructs the loss $L^{CLIP}$ or $L^{KLPEN}$ instead of $L^{PG}$, and one performs multiple steps of stochastic gradient ascent on this objective.

Most techniques for computing variance-reduced advantage-function estimators make use a learned state-value function $V(s)$; for example, generalized advantage estimation [Sch+15a], or the finite-horizon estimators in [Mni+16]. If using a neural network architecture that shares parameters between the policy and value function, we must use a loss function that combines the policy surrogate and a value function error term. This objective can further be augmented by adding an entropy bonus to ensure sufficient exploration, as suggested in past work [Wil92; Mni+16]. Combining these terms, we obtain the following objective, which is (approximately) maximized each iteration:

$$L^{CLIP+VF+S}_t(\theta) = \hat{\mathbb{E}}_t \left[ L^{CLIP}_t(\theta) - c_1 L^{VF}_t(\theta) + c_2 S[\pi_\theta](s_t) \right], \tag{9}$$

where $c_1$, $c_2$ are coefficients, and $S$ denotes an entropy bonus, and $L^{VF}_t$ is a squared-error loss $(V_\theta(s_t) - V^{\text{targ}}_t)^2$.

One style of policy gradient implementation, popularized in [Mni+16] and well-suited for use with recurrent neural networks, runs the policy for $T$ timesteps (where $T$ is much less than the episode length), and uses the collected samples for an update. This style requires an advantage estimator that does not look beyond timestep $T$. The estimator used by [Mni+16] is

$$\hat{A}_t = -V(s_t) + r_t + \gamma r_{t+1} + \cdots + \gamma^{T-t+1} r_{T-1} + \gamma^{T-t} V(s_T) \tag{10}$$

where $t$ specifies the time index in $[0, T]$, within a given length-$T$ trajectory segment. Generalizing this choice, we can use a truncated version of generalized advantage estimation, which reduces to Equation (10) when $\lambda = 1$:

$$\hat{A}_t = \delta_t + (\gamma\lambda)\delta_{t+1} + \cdots + \cdots + (\gamma\lambda)^{T-t+1}\delta_{T-1}, \tag{11}$$

where $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$ \tag{12}$$

A proximal policy optimization (PPO) algorithm that uses fixed-length trajectory segments is shown below. Each iteration, each of $N$ (parallel) actors collect $T$ timesteps of data. Then we construct the surrogate loss on these $NT$ timesteps of data, and optimize it with minibatch SGD (or usually for better performance, Adam [KB14]), for $K$ epochs.

---

**Algorithm 1** PPO, Actor-Critic Style

**for** iteration=1, 2, ... **do**
    **for** actor=1, 2, ..., $N$ **do**
        Run policy $\pi_{\theta_\text{old}}$ in environment for $T$ timesteps
        Compute advantage estimates $\hat{A}_1, \ldots, \hat{A}_T$
    **end for**
    Optimize surrogate $L$ wrt $\theta$, with $K$ epochs and minibatch size $M \leq NT$
    $\theta_\text{old} \leftarrow \theta$
**end for**

---

### النسخة العربية

يمكن حساب وتفاضل خسائر الدوال البديلة من الأقسام السابقة بتغيير بسيط في تطبيق تدرج السياسة النموذجي. بالنسبة للتطبيقات التي تستخدم التفاضل الآلي، يقوم المرء ببساطة ببناء الخسارة $L^{CLIP}$ أو $L^{KLPEN}$ بدلاً من $L^{PG}$، ويقوم بعدة خطوات من الصعود التدرجي العشوائي على هذه الدالة الهدفية.

تستخدم معظم تقنيات حساب مقدرات دالة الأفضلية المخفضة للتباين دالة قيمة الحالة المتعلمة $V(s)$؛ على سبيل المثال، تقدير الأفضلية المعمم [Sch+15a]، أو مقدرات الأفق المحدود في [Mni+16]. إذا كنا نستخدم معمارية شبكة عصبية تشارك المعاملات بين دالة السياسة ودالة القيمة، يجب أن نستخدم دالة خسارة تجمع بين الدالة البديلة للسياسة وحد خطأ دالة القيمة. يمكن تعزيز هذه الدالة الهدفية بشكل أكبر من خلال إضافة مكافأة الإنتروبيا لضمان الاستكشاف الكافي، كما هو مقترح في الأعمال السابقة [Wil92; Mni+16]. من خلال دمج هذه الحدود، نحصل على الدالة الهدفية التالية، والتي يتم تعظيمها (تقريباً) في كل تكرار:

$$L^{CLIP+VF+S}_t(\theta) = \hat{\mathbb{E}}_t \left[ L^{CLIP}_t(\theta) - c_1 L^{VF}_t(\theta) + c_2 S[\pi_\theta](s_t) \right], \tag{9}$$

حيث $c_1$، $c_2$ هما معاملان، و$S$ تشير إلى مكافأة الإنتروبيا، و$L^{VF}_t$ هي خسارة الخطأ التربيعي $(V_\theta(s_t) - V^{\text{targ}}_t)^2$.

أحد أنماط تطبيق تدرج السياسة، المشهور في [Mni+16] والمناسب جيداً للاستخدام مع الشبكات العصبية المتكررة، يشغل السياسة لـ$T$ خطوات زمنية (حيث $T$ أقل بكثير من طول الحلقة)، ويستخدم العينات المجمعة للتحديث. يتطلب هذا النمط مقدر أفضلية لا ينظر إلى ما بعد الخطوة الزمنية $T$. المقدر المستخدم من قبل [Mni+16] هو

$$\hat{A}_t = -V(s_t) + r_t + \gamma r_{t+1} + \cdots + \gamma^{T-t+1} r_{T-1} + \gamma^{T-t} V(s_T) \tag{10}$$

حيث $t$ يحدد مؤشر الوقت في $[0, T]$، ضمن مقطع مسار معطى بطول-$T$. من خلال تعميم هذا الاختيار، يمكننا استخدام نسخة مقطوعة من تقدير الأفضلية المعمم، والتي تختزل إلى المعادلة (10) عندما $\lambda = 1$:

$$\hat{A}_t = \delta_t + (\gamma\lambda)\delta_{t+1} + \cdots + \cdots + (\gamma\lambda)^{T-t+1}\delta_{T-1}, \tag{11}$$

$$\text{حيث} \quad \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t) \tag{12}$$

يظهر أدناه خوارزمية تحسين السياسة التقريبية (PPO) التي تستخدم مقاطع مسار ذات طول ثابت. في كل تكرار، يجمع كل من $N$ فاعل (متوازي) $T$ خطوة زمنية من البيانات. ثم نبني خسارة الدالة البديلة على هذه الخطوات $NT$ من البيانات، ونحسنها باستخدام SGD للدفعات الصغيرة (أو عادة للأداء الأفضل، Adam [KB14])، لـ$K$ حقب.

---

**الخوارزمية 1** PPO، نمط الفاعل-الناقد

**لـ** iteration=1, 2, ... **قم بـ**
    **لـ** actor=1, 2, ..., $N$ **قم بـ**
        شغّل السياسة $\pi_{\theta_\text{old}}$ في البيئة لـ$T$ خطوات زمنية
        احسب تقديرات الأفضلية $\hat{A}_1, \ldots, \hat{A}_T$
    **نهاية لـ**
    حسّن الدالة البديلة $L$ بالنسبة لـ$\theta$، مع $K$ حقب وحجم دفعة صغيرة $M \leq NT$
    $\theta_\text{old} \leftarrow \theta$
**نهاية لـ**

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - surrogate loss - خسارة الدالة البديلة
  - automatic differentiation - التفاضل الآلي
  - stochastic gradient ascent - الصعود التدرجي العشوائي
  - variance-reduced - مخفضة للتباين
  - state-value function - دالة قيمة الحالة
  - generalized advantage estimation (GAE) - تقدير الأفضلية المعمم
  - finite-horizon - الأفق المحدود
  - parameter sharing - مشاركة المعاملات
  - error term - حد الخطأ
  - entropy bonus - مكافأة الإنتروبيا
  - sufficient exploration - الاستكشاف الكافي
  - squared-error loss - خسارة الخطأ التربيعي
  - recurrent neural networks - الشبكات العصبية المتكررة
  - timestep - خطوة زمنية
  - episode length - طول الحلقة
  - trajectory segment - مقطع مسار
  - truncated version - نسخة مقطوعة
  - fixed-length - طول ثابت
  - parallel actors - فاعلون متوازيون
  - minibatch SGD - SGD للدفعات الصغيرة
  - epochs - حقب
  - Actor-Critic - الفاعل-الناقد
- **Equations:** 4 equations (9-12)
- **Citations:** [Sch+15a], [Mni+16], [Wil92], [KB14]
- **Special handling:**
  - Algorithm pseudocode kept in structured format with Arabic keywords
  - Mathematical notation preserved
  - Added Arabic description of algorithm steps
  - Maintained clarity in variable definitions

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
