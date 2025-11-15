# Section 3: Deep Reinforcement Learning
## القسم 3: التعلم المعزز العميق

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** experience replay, convolutional neural network, stochastic gradient descent, minibatch, preprocessing, ReLU activation, replay memory, training algorithm

---

### English Version

Recent breakthroughs in computer vision and speech recognition have relied on efficiently training deep neural networks with tens of millions of parameters. This training process requires back-propagating gradients through many layers. Training a large neural network in the Q-learning setting presents a number of challenges that were not present in these supervised learning applications.

First, most successful deep learning applications to date have required large amounts of hand-labelled training data. By contrast, RL algorithms must be able to learn from a scalar reward signal that is frequently sparse, noisy and delayed. The delay between actions and resulting rewards can be thousands of timesteps long. This contrasts with the direct association between inputs and targets found in supervised learning applications.

Second, most deep learning algorithms assume that the data samples are independent, while in reinforcement learning one typically encounters sequences of highly correlated states. Third, in RL the data distribution changes as the algorithm learns new behaviours, which can be problematic for deep learning methods that assume a fixed underlying distribution.

We address these instabilities with a novel variant of Q-learning, which uses two key ideas. First, we use a biologically inspired mechanism termed experience replay that randomizes over the data, thereby removing correlations in the observation sequence and smoothing over changes in the data distribution. Second, we use an iterative update that adjusts the action-values ($Q$) towards target values that are only periodically updated, thereby reducing correlations with the target.

### 3.1 Preprocessing and Model Architecture

**Preprocessing:** Working directly with raw Atari frames, which are 210 × 160 pixel images with a 128 color palette, can be computationally demanding, so we apply a basic preprocessing step aimed at reducing the input dimensionality. The raw frames are preprocessed by first converting their RGB representation to gray-scale and down-sampling it to a 110 × 84 image. The final input representation is obtained by cropping an 84 × 84 region of the image that roughly captures the playing area. For the experiments in this paper, the function $\phi$ from algorithm 1 applies this preprocessing to the last 4 frames of a history and stacks them to produce the input to the Q-function.

**Network Architecture:** There are several possible ways of parameterizing Q using a neural network. Since Q maps history-action pairs to scalar estimates of their Q-value, the history and the action have been used as inputs to the neural network by some previous approaches. The main drawback of this type of architecture is that a separate forward pass is required to compute the Q-value of each action, resulting in a cost that scales linearly with the number of actions. We instead use an architecture in which there is a separate output unit for each possible action, and only the state representation is an input to the neural network. The outputs correspond to the predicted Q-values of the individual actions for the input state. The main advantage of this type of architecture is the ability to compute Q-values for all possible actions in a given state with only a single forward pass through the network.

The exact architecture, shown schematically in Figure 1, is as follows. The input to the neural network consists of an 84 × 84 × 4 image produced by $\phi$. The first hidden layer convolves 16 filters of 8 × 8 with stride 4 with the input image and applies a rectifier nonlinearity. The second hidden layer convolves 32 filters of 4 × 4 with stride 2, again followed by a rectifier nonlinearity. The final hidden layer is fully-connected and consists of 256 rectifier units. The output layer is a fully-connected linear layer with a single output for each valid action. The number of valid actions varied between 4 and 18 on the games we considered.

### 3.2 Experience Replay

While RL agents have a long history of using experience replay, there have been comparatively few applications involving large neural networks, perhaps because of the common view that online algorithms are required to learn complex functions. In our setting, experience replay provides several advantages over standard online Q-learning.

First, each step of experience is potentially used in many weight updates, which allows for greater data efficiency. Second, learning directly from consecutive samples is inefficient, due to the strong correlations between the samples; randomizing the samples breaks these correlations and therefore reduces the variance of the updates. Third, when learning on-policy the current parameters determine the next data sample that the parameters are trained on. For example, if the maximizing action is to move left then the training samples will be dominated by samples from the left-hand side; if the maximizing action then switches to the right then the training distribution will also switch. It is easy to see how unwanted feedback loops may arise and the parameters could get stuck in a poor local minimum, or even diverge catastrophically. By using experience replay the behavior distribution is averaged over many of its previous states, smoothing out learning and avoiding oscillations or divergence in the parameters. Note that when learning by experience replay, it is necessary to learn off-policy (because our current parameters are different to those used to generate the sample), which motivates the choice of Q-learning.

In practice, our algorithm only stores the last $N$ experience tuples in the replay memory, and samples uniformly at random from $D$ when performing updates. This approach is in some respects limited since the memory buffer does not differentiate important transitions and always overwrites with recent transitions due to the finite memory size $N$. Similarly, the uniform sampling gives equal importance to all transitions in the replay memory. A more sophisticated sampling strategy might emphasize transitions from which we can learn the most, similar to prioritized sweeping.

### 3.3 Algorithm

The complete algorithm for training deep Q-networks is presented in Algorithm 1. The agent selects and executes actions according to an $\epsilon$-greedy policy based on $Q$. Since using histories of arbitrary length as inputs to a neural network can be difficult, our Q-function instead works on fixed length representation of histories produced by the function $\phi$. The algorithm modifies standard online Q-learning in two ways to make it suitable for training large neural networks without diverging.

**Algorithm 1** Deep Q-learning with Experience Replay

```
Initialize replay memory D to capacity N
Initialize action-value function Q with random weights θ
for episode = 1, M do
    Initialize sequence s₁ = {x₁} and preprocessed sequence φ₁ = φ(s₁)
    for t = 1, T do
        With probability ε select a random action aₜ
        otherwise select aₜ = argmax_a Q(φ(sₜ), a; θ)
        Execute action aₜ in emulator and observe reward rₜ and image xₜ₊₁
        Set sₜ₊₁ = sₜ, aₜ, xₜ₊₁ and preprocess φₜ₊₁ = φ(sₜ₊₁)
        Store transition (φₜ, aₜ, rₜ, φₜ₊₁) in D
        Sample random minibatch of transitions (φⱼ, aⱼ, rⱼ, φⱼ₊₁) from D
        Set yⱼ = {
            rⱼ                                     if episode terminates at step j+1
            rⱼ + γ max_a' Q(φⱼ₊₁, a'; θ)          otherwise
        }
        Perform a gradient descent step on (yⱼ - Q(φⱼ, aⱼ; θ))² with respect to θ
    end for
end for
```

First, we use the technique of experience replay. During the inner loop of the algorithm, we store the agent's experiences at each time-step, $e_t = (s_t, a_t, r_t, s_{t+1})$, in a data-set $D = e_1, \ldots, e_N$ pooled over many episodes. During the inner loop we apply Q-learning updates, or minibatch updates, to samples of experience $(s, a, r, s') \sim U(D)$, drawn at random from the pool of stored samples. After performing experience replay, the agent selects and executes an action according to an $\epsilon$-greedy policy. Since it is impractical to run Atari games at full speed in order to minimize the computational complexity, we use a simple frame-skipping technique where the agent sees and selects actions on every $k$-th frame instead of every frame, and its last action is repeated on skipped frames. Since running the emulator forward for one step requires much less computation than having the agent select an action, this technique allows the agent to play roughly $k$ times more games without significantly increasing the runtime.

---

### النسخة العربية

اعتمدت الاختراقات الأخيرة في الرؤية الحاسوبية والتعرف على الكلام على التدريب الفعال للشبكات العصبية العميقة بعشرات الملايين من المعاملات. تتطلب عملية التدريب هذه نشر التدرجات بشكل عكسي عبر طبقات عديدة. يطرح تدريب شبكة عصبية كبيرة في إعداد Q-learning عددًا من التحديات التي لم تكن موجودة في تطبيقات التعلم الموجه هذه.

أولاً، تطلبت معظم تطبيقات التعلم العميق الناجحة حتى الآن كميات كبيرة من بيانات التدريب المُصنّفة يدويًا. على النقيض من ذلك، يجب أن تكون خوارزميات التعلم المعزز قادرة على التعلم من إشارة مكافأة قياسية غالبًا ما تكون متفرقة وصاخبة ومتأخرة. يمكن أن يمتد التأخير بين الإجراءات والمكافآت الناتجة لآلاف الخطوات الزمنية. يتناقض هذا مع الربط المباشر بين المدخلات والأهداف الموجود في تطبيقات التعلم الموجه.

ثانيًا، تفترض معظم خوارزميات التعلم العميق أن عينات البيانات مستقلة، بينما في التعلم المعزز نواجه عادةً تسلسلات من الحالات المترابطة بشكل كبير. ثالثًا، في التعلم المعزز يتغير توزيع البيانات مع تعلم الخوارزمية سلوكيات جديدة، وهو ما قد يكون إشكاليًا لأساليب التعلم العميق التي تفترض توزيعًا أساسيًا ثابتًا.

نعالج هذه الاضطرابات بنسخة جديدة من Q-learning، والتي تستخدم فكرتين رئيسيتين. أولاً، نستخدم آلية مستوحاة بيولوجيًا تسمى إعادة تشغيل الخبرة التي تجعل البيانات عشوائية، وبالتالي إزالة الارتباطات في تسلسل الملاحظات وتنعيم التغييرات في توزيع البيانات. ثانيًا، نستخدم تحديثًا تكراريًا يعدل قيم الإجراءات ($Q$) نحو قيم الهدف التي يتم تحديثها بشكل دوري فقط، وبالتالي تقليل الارتباطات مع الهدف.

### 3.1 المعالجة المسبقة ومعمارية النموذج

**المعالجة المسبقة:** يمكن أن يكون العمل مباشرة مع إطارات Atari الخام، وهي صور بكسل 210 × 160 مع لوحة ألوان 128، متطلبًا حسابيًا، لذلك نطبق خطوة معالجة مسبقة أساسية تهدف إلى تقليل أبعاد المدخل. تتم معالجة الإطارات الخام مسبقًا عن طريق تحويل تمثيل RGB الخاص بها إلى تدرج الرمادي وتقليل العينات إلى صورة 110 × 84. يتم الحصول على تمثيل المدخل النهائي عن طريق اقتصاص منطقة 84 × 84 من الصورة التي تلتقط تقريبًا منطقة اللعب. بالنسبة للتجارب في هذه الورقة، تطبق الدالة $\phi$ من الخوارزمية 1 هذه المعالجة المسبقة على آخر 4 إطارات من السجل وتكدسها لإنتاج مدخل دالة-Q.

**معمارية الشبكة:** هناك عدة طرق ممكنة لتحديد معاملات Q باستخدام شبكة عصبية. نظرًا لأن Q تربط أزواج السجل-الإجراء بتقديرات قياسية لقيمة-Q الخاصة بها، فقد تم استخدام السجل والإجراء كمدخلات للشبكة العصبية من قبل بعض الأساليب السابقة. العيب الرئيسي لهذا النوع من المعمارية هو أنه يلزم مرور أمامي منفصل لحساب قيمة-Q لكل إجراء، مما يؤدي إلى تكلفة تتناسب خطيًا مع عدد الإجراءات. نستخدم بدلاً من ذلك معمارية يوجد فيها وحدة مخرجات منفصلة لكل إجراء ممكن، وفقط تمثيل الحالة هو مدخل للشبكة العصبية. تتوافق المخرجات مع قيم-Q المتوقعة للإجراءات الفردية لحالة المدخل. الميزة الرئيسية لهذا النوع من المعمارية هي القدرة على حساب قيم-Q لجميع الإجراءات الممكنة في حالة معينة بمرور أمامي واحد فقط عبر الشبكة.

المعمارية الدقيقة، الموضحة تخطيطيًا في الشكل 1، هي كما يلي. يتكون مدخل الشبكة العصبية من صورة 84 × 84 × 4 تنتجها $\phi$. تقوم الطبقة المخفية الأولى بإجراء التفاف لـ 16 مرشحًا بحجم 8 × 8 بخطوة 4 مع صورة المدخل وتطبق لا خطية مُقوِّمة. تقوم الطبقة المخفية الثانية بإجراء التفاف لـ 32 مرشحًا بحجم 4 × 4 بخطوة 2، متبوعة مرة أخرى بلا خطية مُقوِّمة. الطبقة المخفية النهائية متصلة بالكامل وتتكون من 256 وحدة مُقوِّمة. طبقة المخرجات هي طبقة خطية متصلة بالكامل مع مخرج واحد لكل إجراء صالح. تراوح عدد الإجراءات الصالحة بين 4 و 18 في الألعاب التي نظرنا فيها.

### 3.2 إعادة تشغيل الخبرة

بينما لدى وكلاء التعلم المعزز تاريخ طويل في استخدام إعادة تشغيل الخبرة، كان هناك عدد قليل نسبيًا من التطبيقات التي تتضمن شبكات عصبية كبيرة، ربما بسبب الرأي السائد بأن الخوارزميات عبر الإنترنت مطلوبة لتعلم دوال معقدة. في إعدادنا، توفر إعادة تشغيل الخبرة عدة مزايا على Q-learning القياسي عبر الإنترنت.

أولاً، يمكن استخدام كل خطوة من الخبرة في العديد من تحديثات الأوزان، مما يسمح بكفاءة أكبر في البيانات. ثانيًا، التعلم مباشرة من عينات متتالية غير فعال، بسبب الارتباطات القوية بين العينات؛ جعل العينات عشوائية يكسر هذه الارتباطات وبالتالي يقلل من تباين التحديثات. ثالثًا، عند التعلم على السياسة، تحدد المعاملات الحالية عينة البيانات التالية التي يتم تدريب المعاملات عليها. على سبيل المثال، إذا كان الإجراء الأقصى هو التحرك لليسار فستهيمن عينات التدريب على العينات من الجانب الأيسر؛ إذا تحول الإجراء الأقصى بعد ذلك إلى اليمين فسيتحول توزيع التدريب أيضًا. من السهل رؤية كيف قد تنشأ حلقات ردود فعل غير مرغوب فيها وقد تتعثر المعاملات في حد أدنى محلي ضعيف، أو حتى تتباعد بشكل كارثي. باستخدام إعادة تشغيل الخبرة، يتم حساب متوسط توزيع السلوك على العديد من حالاته السابقة، مما ينعم التعلم ويتجنب التذبذبات أو التباعد في المعاملات. لاحظ أنه عند التعلم عن طريق إعادة تشغيل الخبرة، من الضروري التعلم خارج السياسة (لأن معاملاتنا الحالية مختلفة عن تلك المستخدمة لتوليد العينة)، مما يبرر اختيار Q-learning.

في الممارسة العملية، تخزن خوارزميتنا فقط آخر $N$ من مجموعات الخبرة في ذاكرة إعادة التشغيل، وتأخذ عينات بشكل عشوائي موحد من $D$ عند إجراء التحديثات. هذا النهج محدود من بعض النواحي لأن المخزن المؤقت للذاكرة لا يميز الانتقالات المهمة ويستبدل دائمًا بالانتقالات الحديثة بسبب حجم الذاكرة المحدود $N$. وبالمثل، فإن أخذ العينات الموحد يعطي أهمية متساوية لجميع الانتقالات في ذاكرة إعادة التشغيل. قد تؤكد استراتيجية أخذ عينات أكثر تطورًا على الانتقالات التي يمكننا التعلم منها أكثر، على غرار المسح ذي الأولوية.

### 3.3 الخوارزمية

يتم تقديم الخوارزمية الكاملة لتدريب شبكات-Q العميقة في الخوارزمية 1. يختار الوكيل الإجراءات وينفذها وفقًا لسياسة إبسيلون-جشعة بناءً على $Q$. نظرًا لأن استخدام سجلات ذات طول تعسفي كمدخلات لشبكة عصبية يمكن أن يكون صعبًا، فإن دالة-Q الخاصة بنا تعمل بدلاً من ذلك على تمثيل ذي طول ثابت للسجلات التي تنتجها الدالة $\phi$. تعدل الخوارزمية Q-learning القياسي عبر الإنترنت بطريقتين لجعلها مناسبة لتدريب الشبكات العصبية الكبيرة دون تباعد.

**الخوارزمية 1** Q-learning العميق مع إعادة تشغيل الخبرة

```
تهيئة ذاكرة إعادة التشغيل D بسعة N
تهيئة دالة قيمة الإجراء Q بأوزان عشوائية θ
for episode = 1, M do
    تهيئة التسلسل s₁ = {x₁} والتسلسل المُعالج مسبقًا φ₁ = φ(s₁)
    for t = 1, T do
        باحتمال ε اختر إجراءً عشوائيًا aₜ
        وإلا اختر aₜ = argmax_a Q(φ(sₜ), a; θ)
        نفذ الإجراء aₜ في المحاكي ولاحظ المكافأة rₜ والصورة xₜ₊₁
        عيّن sₜ₊₁ = sₜ, aₜ, xₜ₊₁ وعالج مسبقًا φₜ₊₁ = φ(sₜ₊₁)
        خزّن الانتقال (φₜ, aₜ, rₜ, φₜ₊₁) في D
        خذ عينة عشوائية من مجموعة صغيرة من الانتقالات (φⱼ, aⱼ, rⱼ, φⱼ₊₁) من D
        عيّن yⱼ = {
            rⱼ                                     إذا انتهت الحلقة عند الخطوة j+1
            rⱼ + γ max_a' Q(φⱼ₊₁, a'; θ)          خلاف ذلك
        }
        قم بخطوة انحدار تدرجي على (yⱼ - Q(φⱼ, aⱼ; θ))² بالنسبة لـ θ
    end for
end for
```

أولاً، نستخدم تقنية إعادة تشغيل الخبرة. أثناء الحلقة الداخلية للخوارزمية، نخزن تجارب الوكيل في كل خطوة زمنية، $e_t = (s_t, a_t, r_t, s_{t+1})$، في مجموعة بيانات $D = e_1, \ldots, e_N$ مجمعة على حلقات عديدة. أثناء الحلقة الداخلية نطبق تحديثات Q-learning، أو تحديثات المجموعات الصغيرة، على عينات من الخبرة $(s, a, r, s') \sim U(D)$، مرسومة بشكل عشوائي من مجموعة العينات المخزنة. بعد إجراء إعادة تشغيل الخبرة، يختار الوكيل وينفذ إجراءً وفقًا لسياسة إبسيلون-جشعة. نظرًا لأنه من غير العملي تشغيل ألعاب Atari بالسرعة الكاملة من أجل تقليل التعقيد الحسابي، نستخدم تقنية تخطي الإطارات البسيطة حيث يرى الوكيل ويختار الإجراءات على كل إطار $k$ بدلاً من كل إطار، ويتكرر آخر إجراء له على الإطارات المتخطاة. نظرًا لأن تشغيل المحاكي للأمام لخطوة واحدة يتطلب حسابًا أقل بكثير من قيام الوكيل باختيار إجراء، تسمح هذه التقنية للوكيل بلعب $k$ من الألعاب تقريبًا دون زيادة وقت التشغيل بشكل كبير.

---

### Translation Notes

- **Figures referenced:** Figure 1 (network architecture schematic)
- **Key terms introduced:**
  - experience replay (إعادة تشغيل الخبرة)
  - replay memory (ذاكرة إعادة التشغيل)
  - rectifier nonlinearity (لا خطية مُقوِّمة) - refers to ReLU
  - frame-skipping (تخطي الإطارات)
  - minibatch (مجموعة صغيرة)
  - on-policy (على السياسة)
  - off-policy (خارج السياسة)
  - feedback loop (حلقة ردود فعل)
  - prioritized sweeping (المسح ذي الأولوية)
  - data efficiency (كفاءة البيانات)

- **Equations:** 0 (referenced from previous section)
- **Citations:** 0
- **Special handling:**
  - Algorithm 1 presented in bilingual format (English pseudocode with Arabic translation)
  - Network architecture specifications (16 filters 8×8, stride 4, etc.) kept as technical details
  - Mathematical notation ($\phi$, $\theta$, $\gamma$, $\epsilon$) preserved
  - ReLU kept as "مُقوِّمة" (rectifier)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.87
