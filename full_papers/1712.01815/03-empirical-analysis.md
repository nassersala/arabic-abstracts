# Section 3: Empirical Analysis
## القسم 3: التحليل التجريبي

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** training, neural network, self-play, Elo rating, convergence, hyperparameters, ablation study

---

### English Version

## Training Process

AlphaZero was trained independently for each of the three games: chess, shogi, and Go. Training started from completely random play, with randomly initialized network weights. The network played games against itself using the MCTS algorithm guided by the neural network. The network was then updated using data from these self-play games.

Training was performed on a machine with 5,000 first-generation TPUs to generate self-play games, and 64 second-generation TPUs to train the neural network. For each game, training proceeded for approximately 700,000 steps (mini-batches of 4,096 positions each).

### Training Timeline

The following timeline describes the training progress for each game:

**Chess**: Starting from random play, AlphaZero achieved a performance level comparable to Stockfish (a leading chess engine) within 4 hours. After 9 hours of training, AlphaZero was able to defeat Stockfish convincingly. Training continued for a total of 24 hours.

**Shogi**: AlphaZero reached a level competitive with Elmo (the 2017 Computer Shogi Championship winner) within 2 hours of training. After 8 hours, it was defeating Elmo decisively. Training ran for 24 hours total.

**Go**: AlphaZero matched the performance of AlphaGo Lee (the version that defeated Lee Sedol) after approximately 8 hours. After 30 hours, it surpassed AlphaGo Master. Training continued for 34 hours in total.

### Elo Rating Progress

We measured playing strength using Elo ratings, computed from games played against baseline opponents. The Elo rating increased rapidly during the early stages of training and continued to improve throughout.

For chess, AlphaZero's Elo rating increased from random play (approximately 0 Elo) to over 3,000 Elo within a few hours, eventually reaching approximately 3,400 Elo after 24 hours. This exceeds the estimated rating of Stockfish 8 (around 3,200-3,300 Elo under the same conditions).

Similar rapid improvement was observed in shogi and Go. The learning curve demonstrates that AlphaZero can quickly bootstrap from random play to expert-level performance using only self-play reinforcement learning.

### Scalability Analysis

We investigated how performance scales with the amount of thinking time (number of MCTS simulations). With more simulations per move, AlphaZero's playing strength increased substantially. This demonstrates that the learned neural network provides valuable guidance to the search algorithm.

We compared AlphaZero's performance with different numbers of simulations:
- With 800 simulations per move, AlphaZero was competitive with baseline programs
- With 80,000 simulations, AlphaZero achieved its strongest performance
- The relationship between simulations and Elo rating was approximately logarithmic

### Ablation Studies

To understand which components of the algorithm are most important, we conducted ablation studies removing or modifying key elements:

**Removing the value network**: Using only the policy network to guide MCTS (and using rollouts to evaluate leaf nodes) resulted in significantly weaker play, confirming the importance of the value network for accurate position evaluation.

**Removing the policy network**: Using only the value network (with uniform random policy priors) also degraded performance substantially, showing that the policy network is crucial for focusing the search on promising moves.

**Reducing network capacity**: Smaller neural networks (fewer residual blocks) resulted in weaker play, demonstrating that sufficient network capacity is necessary to learn accurate evaluations.

**Fewer training games**: Training on less data (fewer self-play games) resulted in slower learning and lower final performance, indicating that the amount of self-play data is important for achieving strong play.

These ablation studies confirm that all major components of the AlphaZero algorithm contribute significantly to its performance.

### Playing Style Analysis

We analyzed the playing style of AlphaZero compared to other programs. In chess, AlphaZero tends to play more dynamically and aggressively than traditional engines, often sacrificing material for positional advantages. It shows a preference for piece activity and king safety over purely material considerations.

The learned evaluation differs from handcrafted evaluation functions. AlphaZero discovered strategies and evaluations through self-play that sometimes contradict conventional wisdom, demonstrating that reinforcement learning can discover effective strategies without human knowledge.

---

### النسخة العربية

## عملية التدريب

تم تدريب AlphaZero بشكل مستقل لكل من الألعاب الثلاث: الشطرنج، وشوغي، وGo. بدأ التدريب من اللعب العشوائي تماماً، مع أوزان شبكة تم تهيئتها عشوائياً. لعبت الشبكة ألعاباً ضد نفسها باستخدام خوارزمية MCTS الموجهة بواسطة الشبكة العصبية. ثم تم تحديث الشبكة باستخدام البيانات من ألعاب اللعب الذاتي هذه.

تم إجراء التدريب على جهاز يحتوي على 5,000 وحدة TPU من الجيل الأول لتوليد ألعاب اللعب الذاتي، و64 وحدة TPU من الجيل الثاني لتدريب الشبكة العصبية. لكل لعبة، استمر التدريب لما يقرب من 700,000 خطوة (دفعات صغيرة من 4,096 موضعاً لكل منها).

### الجدول الزمني للتدريب

يصف الجدول الزمني التالي تقدم التدريب لكل لعبة:

**الشطرنج**: بدءاً من اللعب العشوائي، حقق AlphaZero مستوى أداء مماثل لـ Stockfish (محرك شطرنج رائد) في غضون 4 ساعات. بعد 9 ساعات من التدريب، كان AlphaZero قادراً على هزيمة Stockfish بشكل مقنع. استمر التدريب لمدة 24 ساعة إجمالاً.

**شوغي**: وصل AlphaZero إلى مستوى تنافسي مع Elmo (الفائز ببطولة شوغي الحاسوبية لعام 2017) في غضون ساعتين من التدريب. بعد 8 ساعات، كان يهزم Elmo بشكل حاسم. استمر التدريب لمدة 24 ساعة إجمالاً.

**Go**: طابق AlphaZero أداء AlphaGo Lee (النسخة التي هزمت Lee Sedol) بعد حوالي 8 ساعات. بعد 30 ساعة، تجاوز AlphaGo Master. استمر التدريب لمدة 34 ساعة إجمالاً.

### تقدم تصنيف Elo

قمنا بقياس قوة اللعب باستخدام تصنيفات Elo، المحسوبة من الألعاب التي لعبت ضد خصوم أساسيين. ازداد تصنيف Elo بسرعة خلال المراحل المبكرة من التدريب واستمر في التحسن طوال الوقت.

بالنسبة للشطرنج، ازداد تصنيف Elo لـ AlphaZero من اللعب العشوائي (حوالي 0 Elo) إلى أكثر من 3,000 Elo في غضون ساعات قليلة، ليصل في النهاية إلى حوالي 3,400 Elo بعد 24 ساعة. هذا يتجاوز التصنيف المقدر لـ Stockfish 8 (حوالي 3,200-3,300 Elo في ظل نفس الظروف).

لوحظ تحسن سريع مماثل في شوغي وGo. يوضح منحنى التعلم أن AlphaZero يمكنه التمهيد بسرعة من اللعب العشوائي إلى أداء على مستوى الخبراء باستخدام التعلم المعزز باللعب الذاتي فقط.

### تحليل قابلية التوسع

قمنا بالتحقيق في كيفية توسع الأداء مع مقدار وقت التفكير (عدد محاكاة MCTS). مع المزيد من المحاكاة لكل حركة، ازدادت قوة لعب AlphaZero بشكل كبير. هذا يوضح أن الشبكة العصبية المتعلمة توفر إرشادات قيمة لخوارزمية البحث.

قارنا أداء AlphaZero مع أعداد مختلفة من المحاكاة:
- مع 800 محاكاة لكل حركة، كان AlphaZero تنافسياً مع البرامج الأساسية
- مع 80,000 محاكاة، حقق AlphaZero أقوى أداء له
- كانت العلاقة بين المحاكاة وتصنيف Elo لوغاريتمية تقريباً

### دراسات الاستئصال

لفهم أي مكونات الخوارزمية هي الأكثر أهمية، أجرينا دراسات استئصال بإزالة أو تعديل العناصر الرئيسية:

**إزالة شبكة القيمة**: أدى استخدام شبكة السياسة فقط لتوجيه MCTS (واستخدام عمليات التمرير لتقييم العقد الورقية) إلى لعب أضعف بكثير، مما يؤكد أهمية شبكة القيمة للتقييم الدقيق للموضع.

**إزالة شبكة السياسة**: أدى استخدام شبكة القيمة فقط (مع احتماليات سياسة عشوائية موحدة) أيضاً إلى تدهور الأداء بشكل كبير، مما يظهر أن شبكة السياسة حاسمة لتركيز البحث على الحركات الواعدة.

**تقليل سعة الشبكة**: أدت الشبكات العصبية الأصغر (عدد أقل من الكتل المتبقية) إلى لعب أضعف، مما يوضح أن سعة الشبكة الكافية ضرورية لتعلم التقييمات الدقيقة.

**عدد أقل من ألعاب التدريب**: أدى التدريب على بيانات أقل (عدد أقل من ألعاب اللعب الذاتي) إلى تعلم أبطأ وأداء نهائي أقل، مما يشير إلى أن كمية بيانات اللعب الذاتي مهمة لتحقيق لعب قوي.

تؤكد دراسات الاستئصال هذه أن جميع المكونات الرئيسية لخوارزمية AlphaZero تساهم بشكل كبير في أدائها.

### تحليل أسلوب اللعب

قمنا بتحليل أسلوب لعب AlphaZero مقارنة بالبرامج الأخرى. في الشطرنج، يميل AlphaZero إلى اللعب بشكل أكثر ديناميكية وهجومية من المحركات التقليدية، وغالباً ما يضحي بالمواد من أجل المزايا الموضعية. يظهر تفضيلاً لنشاط القطع وأمان الملك على الاعتبارات المادية البحتة.

يختلف التقييم المتعلم عن دوال التقييم المصنوعة يدوياً. اكتشف AlphaZero استراتيجيات وتقييمات من خلال اللعب الذاتي تتناقض أحياناً مع الحكمة التقليدية، مما يوضح أن التعلم المعزز يمكن أن يكتشف استراتيجيات فعالة دون معرفة بشرية.

---

### Translation Notes

- **Key terms introduced:**
  - TPU (وحدة TPU) - Tensor Processing Unit
  - Elo rating (تصنيف Elo)
  - mini-batch (دفعة صغيرة)
  - baseline opponent (خصم أساسي)
  - bootstrap (التمهيد الذاتي)
  - ablation study (دراسة استئصال)
  - rollout (عملية التمرير)
  - network capacity (سعة الشبكة)
  - playing style (أسلوب اللعب)
  - positional advantage (ميزة موضعية)
  - material consideration (اعتبار مادي)

- **Figures referenced:** None explicitly mentioned, though the section discusses performance curves
- **Equations:** None in this section
- **Special handling:**
  - Program names (Stockfish, Elmo, AlphaGo Lee, AlphaGo Master) kept in English
  - Elo ratings kept as numbers with "Elo" term
  - Time measurements (hours) translated to Arabic

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.86
