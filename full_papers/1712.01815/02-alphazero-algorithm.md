# Section 2: AlphaZero Algorithm
## القسم 2: خوارزمية AlphaZero

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** reinforcement learning, neural network, Monte Carlo Tree Search, policy, value function, self-play, training, convolutional neural network, residual network

---

### English Version

## AlphaZero Algorithm

The AlphaZero algorithm is based on the AlphaGo Zero algorithm, but generalized to work for any two-player, zero-sum game with perfect information. The algorithm consists of three main components: (1) a neural network that takes the board position as input and outputs both a policy (move probabilities) and a value (expected outcome); (2) a Monte Carlo tree search (MCTS) algorithm that uses the neural network to guide its search; and (3) a self-play reinforcement learning algorithm that continually trains the neural network.

### Neural Network Architecture

The neural network uses a residual tower architecture similar to AlphaGo Zero. The input to the neural network is a representation of the board position. For chess and shogi, we use a simple representation based on the piece positions. The board is represented by a stack of planes, where each plane encodes the positions of a particular piece type for a particular player, along with additional planes encoding repetitions, castling rights, and other game-specific information.

The neural network consists of multiple residual blocks. Each residual block applies a rectified linear unit (ReLU) nonlinearity to the input, followed by a 3×3 convolution with batch normalization, another ReLU, and another 3×3 convolution with batch normalization. A skip connection adds the input to the output of the second convolution, followed by a final ReLU.

The network has two output heads: a policy head that outputs move probabilities for all legal moves, and a value head that outputs a scalar value estimating the expected outcome from the current position (from the perspective of the current player).

### Monte Carlo Tree Search

During self-play, moves are selected by running MCTS. Each simulation starts from the root (the current board position) and iteratively selects moves until reaching a leaf node. At each node in the tree, we select the action with the highest upper confidence bound:

$$a_t = \arg\max_a \left( Q(s_t, a) + U(s_t, a) \right)$$

where $Q(s_t, a)$ is the mean action-value, and $U(s_t, a)$ is an upper confidence bound:

$$U(s_t, a) = c_{puct} \cdot P(s_t, a) \cdot \frac{\sqrt{\sum_b N(s_t, b)}}{1 + N(s_t, a)}$$

Here, $P(s_t, a)$ is the prior probability of selecting action $a$ in state $s_t$ (from the neural network policy), $N(s_t, a)$ is the visit count for that state-action pair, and $c_{puct}$ is a constant that controls the level of exploration.

When a leaf node is reached, it is expanded and evaluated using the neural network. The value output is then backed up through the tree, updating the statistics at each node along the path.

After running MCTS for a fixed number of simulations, a move is selected. During training, the move is sampled from the search probabilities. During evaluation, the move with the highest visit count is selected deterministically.

### Self-Play Training

Training proceeds by continual self-play. At each iteration, the current neural network plays games against itself. For each position in the game, MCTS is executed and the search probabilities are stored. At the end of the game, the outcome is known, and each position is labeled with this outcome.

The neural network is trained on data from the most recent games. The training objective minimizes the error between:
- The predicted value and the actual game outcome (value loss)
- The predicted policy and the search probabilities from MCTS (policy loss)
- Plus an L2 regularization term to prevent overfitting

The loss function is:

$$\ell = (z - v)^2 - \pi^T \log p + c \|\theta\|^2$$

where $z$ is the game outcome, $v$ is the value prediction, $\pi$ is the search probability vector from MCTS, $p$ is the policy output, $\theta$ represents the network parameters, and $c$ is a regularization constant.

Training uses stochastic gradient descent with momentum. The network is trained continuously as new self-play games are generated, with the training data consisting of the most recent window of games.

### Game-Specific Adaptations

While AlphaZero uses the same algorithm for all three games, there are some minimal game-specific adaptations in the input representation and rules encoding:
- Board size and piece types differ between games
- Legal move generation follows each game's specific rules
- Game termination conditions (checkmate, stalemate, repetition) are game-specific

Importantly, no game-specific knowledge is used beyond the rules themselves. There are no handcrafted features, opening books, endgame tables, or other domain knowledge incorporated into the system.

---

### النسخة العربية

## خوارزمية AlphaZero

تستند خوارزمية AlphaZero إلى خوارزمية AlphaGo Zero، ولكن تم تعميمها للعمل مع أي لعبة لاعبين ذات مجموع صفري ومعلومات كاملة. تتكون الخوارزمية من ثلاثة مكونات رئيسية: (1) شبكة عصبية تأخذ موضع اللوحة كمدخل وتخرج كلاً من السياسة (احتماليات الحركة) والقيمة (النتيجة المتوقعة)؛ (2) خوارزمية بحث شجرة مونت كارلو (MCTS) تستخدم الشبكة العصبية لتوجيه بحثها؛ و(3) خوارزمية تعلم معزز باللعب الذاتي تدرب الشبكة العصبية بشكل مستمر.

### معمارية الشبكة العصبية

تستخدم الشبكة العصبية معمارية برج متبقي (residual tower) مشابهة لـ AlphaGo Zero. المدخل إلى الشبكة العصبية هو تمثيل لموضع اللوحة. بالنسبة للشطرنج وشوغي، نستخدم تمثيلاً بسيطاً يعتمد على مواضع القطع. يتم تمثيل اللوحة بمجموعة من المستويات، حيث يشفر كل مستوى مواضع نوع معين من القطع للاعب معين، إلى جانب مستويات إضافية تشفر التكرارات، وحقوق التبييت (castling)، ومعلومات أخرى خاصة باللعبة.

تتكون الشبكة العصبية من كتل متبقية متعددة. تطبق كل كتلة متبقية لاخطية وحدة خطية مصححة (ReLU) على المدخل، تليها التفاف 3×3 مع تطبيع الدفعات، ثم ReLU أخرى، والتفاف آخر 3×3 مع تطبيع الدفعات. يضيف اتصال التخطي (skip connection) المدخل إلى مخرج الالتفاف الثاني، يليه ReLU نهائي.

تحتوي الشبكة على رأسين للمخرجات: رأس السياسة الذي يخرج احتماليات الحركة لجميع الحركات القانونية، ورأس القيمة الذي يخرج قيمة قياسية تقدر النتيجة المتوقعة من الموضع الحالي (من منظور اللاعب الحالي).

### بحث شجرة مونت كارلو

أثناء اللعب الذاتي، يتم اختيار الحركات عن طريق تشغيل MCTS. تبدأ كل محاكاة من الجذر (موضع اللوحة الحالي) وتختار الحركات بشكل متكرر حتى الوصول إلى عقدة ورقية. في كل عقدة في الشجرة، نختار الإجراء الذي يحتوي على أعلى حد ثقة علوي:

$$a_t = \arg\max_a \left( Q(s_t, a) + U(s_t, a) \right)$$

حيث $Q(s_t, a)$ هي متوسط قيمة الإجراء، و $U(s_t, a)$ هو حد الثقة العلوي:

$$U(s_t, a) = c_{puct} \cdot P(s_t, a) \cdot \frac{\sqrt{\sum_b N(s_t, b)}}{1 + N(s_t, a)}$$

هنا، $P(s_t, a)$ هي الاحتمالية المسبقة لاختيار الإجراء $a$ في الحالة $s_t$ (من سياسة الشبكة العصبية)، $N(s_t, a)$ هو عدد الزيارات لزوج الحالة-الإجراء، و $c_{puct}$ هو ثابت يتحكم في مستوى الاستكشاف.

عندما يتم الوصول إلى عقدة ورقية، يتم توسيعها وتقييمها باستخدام الشبكة العصبية. ثم يتم نشر مخرج القيمة عبر الشجرة، وتحديث الإحصاءات في كل عقدة على طول المسار.

بعد تشغيل MCTS لعدد ثابت من المحاكاة، يتم اختيار حركة. أثناء التدريب، يتم أخذ عينة من الحركة من احتماليات البحث. أثناء التقييم، يتم اختيار الحركة ذات أعلى عدد زيارات بشكل حتمي.

### التدريب باللعب الذاتي

يستمر التدريب من خلال اللعب الذاتي المستمر. في كل تكرار، تلعب الشبكة العصبية الحالية ألعاباً ضد نفسها. لكل موضع في اللعبة، يتم تنفيذ MCTS وتخزين احتماليات البحث. في نهاية اللعبة، تكون النتيجة معروفة، ويتم تسمية كل موضع بهذه النتيجة.

يتم تدريب الشبكة العصبية على البيانات من الألعاب الأحدث. يقلل هدف التدريب من الخطأ بين:
- القيمة المتنبأ بها ونتيجة اللعبة الفعلية (خسارة القيمة)
- السياسة المتنبأ بها واحتماليات البحث من MCTS (خسارة السياسة)
- بالإضافة إلى مصطلح تنظيم L2 لمنع الإفراط في التوافق

دالة الخسارة هي:

$$\ell = (z - v)^2 - \pi^T \log p + c \|\theta\|^2$$

حيث $z$ هي نتيجة اللعبة، $v$ هي تنبؤ القيمة، $\pi$ هو متجه احتمالية البحث من MCTS، $p$ هو مخرج السياسة، $\theta$ تمثل معاملات الشبكة، و $c$ هو ثابت التنظيم.

يستخدم التدريب الانحدار التدرجي العشوائي مع الزخم. يتم تدريب الشبكة بشكل مستمر مع توليد ألعاب اللعب الذاتي الجديدة، حيث تتكون بيانات التدريب من النافذة الأحدث من الألعاب.

### التكيفات الخاصة باللعبة

بينما يستخدم AlphaZero نفس الخوارزمية للألعاب الثلاثة جميعاً، هناك بعض التكيفات البسيطة الخاصة باللعبة في تمثيل المدخل وتشفير القواعد:
- يختلف حجم اللوحة وأنواع القطع بين الألعاب
- يتبع توليد الحركات القانونية قواعد كل لعبة المحددة
- شروط انتهاء اللعبة (كش مات، طريق مسدود، تكرار) خاصة باللعبة

والأهم من ذلك، لا يتم استخدام أي معرفة خاصة باللعبة بخلاف القواعد نفسها. لا توجد ميزات مصنوعة يدوياً، أو كتب افتتاحية، أو جداول نهاية اللعبة، أو أي معرفة أخرى بالمجال مدمجة في النظام.

---

### Translation Notes

- **Key terms introduced:**
  - residual tower (برج متبقي)
  - residual block (كتلة متبقية)
  - skip connection (اتصال التخطي)
  - ReLU (وحدة خطية مصححة)
  - batch normalization (تطبيع الدفعات)
  - upper confidence bound (حد الثقة العلوي)
  - visit count (عدد الزيارات)
  - policy head (رأس السياسة)
  - value head (رأس القيمة)
  - stochastic gradient descent (الانحدار التدرجي العشوائي)
  - L2 regularization (تنظيم L2)
  - castling rights (حقوق التبييت)
  - opening books (كتب افتتاحية)
  - endgame tables (جداول نهاية اللعبة)

- **Equations:** 3 mathematical equations with explanations
- **Special handling:**
  - Mathematical notation preserved in LaTeX
  - Technical terms like "ReLU" explained in parentheses
  - Algorithm name "MCTS" kept as acronym with full form in Arabic

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
