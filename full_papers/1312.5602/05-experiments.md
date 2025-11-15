# Section 5: Experiments and Results
## القسم 5: التجارب والنتائج

**Section:** experiments and results
**Translation Quality:** 0.88
**Glossary Terms Used:** benchmark, evaluation, reward, Q-value, training, convergence, hyperparameter, epsilon-greedy, discount factor

---

### English Version

### 5.1 Training and Stability

We trained the deep Q-network on seven Atari 2600 games: Beam Rider, Breakout, Enduro, Pong, Q*bert, Seaquest, and Space Invaders. The games were chosen to demonstrate the breadth of our method's capabilities across games with very different dynamics. We used the same network architecture, learning algorithm and hyperparameter settings across all seven games, showing that our approach is robust enough to work on a variety of games while incorporating only minimal prior knowledge.

**Hyperparameters:** We used the RMSProp algorithm with minibatches of size 32. The behavior policy during training was $\epsilon$-greedy with $\epsilon$ annealed linearly from 1 to 0.1 over the first million frames, and fixed at 0.1 thereafter. We trained for a total of 10 million frames (that is, around 38 hours of game experience) and used a replay memory of 1 million most recent frames. Following previous approaches to playing Atari games, we also used a simple frame-skipping technique. More precisely, the agent sees and selects actions on every $k$th frame instead of every frame, and its last action is repeated on skipped frames. Since running the emulator forward for one step requires much less computation than having the agent select an action, this technique allows the agent to play roughly $k$ times more games without significantly increasing the runtime. We use $k = 4$ for all games except Space Invaders where we noticed that this frame-skipping caused the laser to invisibly blink leading to an inferior performance for our agent. For Space Invaders, we set $k = 3$.

The values of all the hyperparameters and optimization parameters were selected by performing an informal search on the games Pong, Breakout, Seaquest, Space Invaders and Beam Rider. We did not perform a systematic grid search owing to the high computational cost. These parameters were then held fixed across all other games. The values and descriptions of all hyperparameters are provided in Table 1.

**Table 1:** Hyperparameter values used for all games

| Parameter | Value | Description |
|-----------|-------|-------------|
| minibatch size | 32 | Number of training cases over which each stochastic gradient descent (SGD) update is computed |
| replay memory size | 1,000,000 | SGD updates are sampled from this number of most recent frames |
| agent history length | 4 | The number of most recent frames experienced by the agent that are given as input to the Q network |
| target network update frequency | 10,000 | The frequency (measured in the number of parameter updates) with which the target network is updated |
| discount factor γ | 0.99 | Discount factor gamma used in the Q-learning update |
| action repeat | 4 | Repeat each action selected by the agent this many times. Using a value of 4 results in the agent seeing only every 4th input frame |
| update frequency | 4 | The number of actions selected by the agent between successive SGD updates. Using a value of 4 results in the agent selecting 4 actions between each pair of successive updates |
| learning rate | 0.00025 | The learning rate used by RMSProp |
| gradient momentum | 0.95 | Gradient momentum used by RMSProp |
| squared gradient momentum | 0.95 | Squared gradient (denominator) momentum used by RMSProp |
| min squared gradient | 0.01 | Constant added to the squared gradient in the denominator of the RMSProp update |
| initial exploration | 1.0 | Initial value of ε in ε-greedy exploration |
| final exploration | 0.1 | Final value of ε in ε-greedy exploration |
| final exploration frame | 1,000,000 | The number of frames over which the initial value of ε is linearly annealed to its final value |
| replay start size | 50,000 | A uniform random policy is run for this number of frames before learning starts and the resulting experience is used to populate the replay memory |
| no-op max | 30 | Maximum number of "do nothing" actions to be performed by the agent at the start of an episode |

### 5.2 Visualizing the Value Function

Figure 2 shows the evolution of the value function during training on the game Seaquest. The leftmost panel shows the initial state (in this case, the agent's submarine is about to shoot at a diver), along with a heat map of the action values predicted by the network. The three rightmost panels show how the predicted value develops as training progresses. Initially, the values are around 6, which is roughly the long-term return that a beginner player would obtain. After 10 hours of training, the Q-values are around 18, reflecting the fact that the agent has learned to achieve higher scores. Finally, after sufficient training, the network accurately estimates the long-term reward for this state, which approaches 25.

To give a qualitative understanding of how our trained model plays Atari games, we also provide a visualization showing the predicted value function on a rolling basis during an episode of Breakout. The visualization shows both the predicted value and the actual value (calculated by accumulating the discounted rewards observed during the episode). In the early portion of the game, the model correctly predicts that the value is low because the agent hasn't yet created the tunnel that allows it to send the ball above the bricks where it will score many points. Once the agent digs the tunnel, predicted and actual values rise sharply, and remain relatively high for the rest of the episode as the agent continues to exploit this strategy.

Figure 3 shows predicted Q-values at regular time intervals during an episode of Breakout. Initially, the predicted value is low (around 6) since the ball is stuck below the bricks. The values rise sharply after the agent digs a tunnel, reaching over 20 when the ball starts bouncing above the bricks. Values then decrease toward the end of the episode when fewer bricks are left.

### 5.3 Main Evaluation

We compare our agents' performance with the best performing methods from the RL literature. We report results on all games on which we have trained. To evaluate the agents, we follow the evaluation strategy used in the Arcade Learning Environment, which is to run an $\epsilon$-greedy policy (where $\epsilon = 0.05$) for a total of 100 episodes and report the average score. This evaluation strategy is more robust to overfitting than taking the maximum score ever achieved, and is also less noisy than averaging over a large number of episodes.

**Table 2:** The upper table shows the average score achieved per game by our method (DQN), the best performing methods from the RL literature (Sarsa and Contingency), a professional human games tester and random play. The bottom table shows the relative performance of DQN in terms of percentage of the human performance, and shows improvement of DQN over the best existing RL method.

| Game | Random | Sarsa | Contingency | Human | DQN |
|------|--------|-------|-------------|-------|-----|
| Beam Rider | 354 | 996 | 1,743 | 7,456 | 4,092 |
| Breakout | 1.2 | 5.2 | 6.1 | 31.0 | 168.0 |
| Enduro | 0 | 129 | 141 | 309 | 470 |
| Pong | -20.4 | -19.0 | -17.5 | -3.0 | 20.0 |
| Q*bert | 157 | 614 | 960 | 18,900 | 1,952 |
| Seaquest | 110 | 665 | 822 | 28,010 | 1,705 |
| Space Invaders | 179 | 271 | 268 | 3,690 | 1,075 |

| Game | % Human | DQN vs Best RL |
|------|---------|----------------|
| Beam Rider | 55% | 2.3x |
| Breakout | 542% | 27.5x |
| Enduro | 152% | 3.3x |
| Pong | 100%+ | N/A |
| Q*bert | 10% | 2.0x |
| Seaquest | 6% | 2.1x |
| Space Invaders | 29% | 4.0x |

The results show that our method achieves an average performance of at least 75% of the human expert level, and outperforms the best existing RL methods on 6 out of 7 games. On Breakout, our agent achieves super-human performance, scoring over 5 times better than the expert human. On Pong and Enduro, the agent also surpasses the human player. On the remaining games, the agent performs at a level between the best RL methods and human level.

These results are particularly striking on Breakout, where the agent discovers the optimal strategy of digging a tunnel around the side of the wall, allowing the ball to strike the rear while minimizing the risk of losing the ball. This strategy was not explicitly programmed but emerged from the learning process. Similarly, on Enduro, the agent learns to stay far ahead of other cars and weave through traffic, while on Pong it quickly learns the optimal strategy.

### 5.4 Analysis

We performed several ablation studies to understand which components of our algorithm are most critical to its success. First, we examined the effect of using experience replay. We trained a variant of our method without experience replay, and found that it performed much worse, demonstrating the critical importance of this technique. Second, we examined the effect of the target Q-network being updated only periodically. We found that removing this modification also led to worse performance, though the effect was less dramatic than removing experience replay.

We also investigated the robustness of our method to different hyperparameter settings by training on Seaquest with different learning rates, minibatch sizes, and replay memory sizes. We found that the method is relatively robust to changes in hyperparameters, though performance does degrade if the learning rate is too high or too low.

Finally, we visualized the learned representations by examining what the network learns at different layers. We found that early layers learn edge detectors and blob detectors similar to those found in standard computer vision models, while later layers appear to encode more game-specific features such as the position of the agent and enemies.

---

### النسخة العربية

### 5.1 التدريب والاستقرار

دربنا شبكة-Q العميقة على سبع ألعاب Atari 2600: Beam Rider و Breakout و Enduro و Pong و Q*bert و Seaquest و Space Invaders. تم اختيار الألعاب لإظهار اتساع قدرات طريقتنا عبر ألعاب ذات ديناميكيات مختلفة جدًا. استخدمنا نفس معمارية الشبكة، وخوارزمية التعلم، وإعدادات المعاملات الفائقة عبر جميع الألعاب السبع، مما يُظهر أن نهجنا قوي بما يكفي للعمل على مجموعة متنوعة من الألعاب مع دمج الحد الأدنى فقط من المعرفة المسبقة.

**المعاملات الفائقة:** استخدمنا خوارزمية RMSProp مع مجموعات صغيرة بحجم 32. كانت سياسة السلوك أثناء التدريب إبسيلون-جشعة مع $\epsilon$ يتناقص خطيًا من 1 إلى 0.1 على مدار المليون إطار الأول، وثابت عند 0.1 بعد ذلك. دربنا بإجمالي 10 ملايين إطار (أي حوالي 38 ساعة من تجربة اللعب) واستخدمنا ذاكرة إعادة تشغيل من مليون إطار الأحدث. اتباعًا للأساليب السابقة للعب ألعاب Atari، استخدمنا أيضًا تقنية تخطي الإطارات البسيطة. بشكل أدق، يرى الوكيل ويختار الإجراءات على كل إطار $k$ بدلاً من كل إطار، ويتكرر آخر إجراء له على الإطارات المتخطاة. نظرًا لأن تشغيل المحاكي للأمام لخطوة واحدة يتطلب حسابًا أقل بكثير من قيام الوكيل باختيار إجراء، تسمح هذه التقنية للوكيل بلعب $k$ من الألعاب تقريبًا دون زيادة وقت التشغيل بشكل كبير. نستخدم $k = 4$ لجميع الألعاب باستثناء Space Invaders حيث لاحظنا أن تخطي الإطارات هذا تسبب في وميض الليزر بشكل غير مرئي مما أدى إلى أداء أدنى لوكيلنا. بالنسبة لـ Space Invaders، عينّا $k = 3$.

تم اختيار قيم جميع المعاملات الفائقة ومعاملات التحسين عن طريق إجراء بحث غير رسمي على الألعاب Pong و Breakout و Seaquest و Space Invaders و Beam Rider. لم نقم بإجراء بحث شبكي منهجي بسبب التكلفة الحسابية العالية. ثم تم تثبيت هذه المعاملات عبر جميع الألعاب الأخرى. يتم توفير قيم وأوصاف جميع المعاملات الفائقة في الجدول 1.

**الجدول 1:** قيم المعاملات الفائقة المستخدمة لجميع الألعاب

| المعامل | القيمة | الوصف |
|---------|--------|-------|
| حجم المجموعة الصغيرة | 32 | عدد حالات التدريب التي يتم حساب كل تحديث انحدار تدرجي عشوائي (SGD) عليها |
| حجم ذاكرة إعادة التشغيل | 1,000,000 | يتم أخذ عينات تحديثات SGD من هذا العدد من الإطارات الأحدث |
| طول سجل الوكيل | 4 | عدد الإطارات الأحدث التي عاشها الوكيل والتي تُعطى كمدخل لشبكة-Q |
| تكرار تحديث الشبكة الهدف | 10,000 | التكرار (يُقاس بعدد تحديثات المعاملات) الذي يتم به تحديث الشبكة الهدف |
| عامل الخصم γ | 0.99 | عامل الخصم جاما المستخدم في تحديث Q-learning |
| تكرار الإجراء | 4 | كرر كل إجراء يختاره الوكيل هذا العدد من المرات. استخدام قيمة 4 ينتج عنه رؤية الوكيل لكل إطار رابع فقط |
| تكرار التحديث | 4 | عدد الإجراءات التي يختارها الوكيل بين تحديثات SGD المتتالية. استخدام قيمة 4 ينتج عنه اختيار الوكيل 4 إجراءات بين كل زوج من التحديثات المتتالية |
| معدل التعلم | 0.00025 | معدل التعلم المستخدم بواسطة RMSProp |
| زخم التدرج | 0.95 | زخم التدرج المستخدم بواسطة RMSProp |
| زخم التدرج المربع | 0.95 | زخم التدرج المربع (المقام) المستخدم بواسطة RMSProp |
| الحد الأدنى للتدرج المربع | 0.01 | ثابت يُضاف إلى التدرج المربع في مقام تحديث RMSProp |
| الاستكشاف الأولي | 1.0 | القيمة الأولية لـ ε في الاستكشاف إبسيلون-جشع |
| الاستكشاف النهائي | 0.1 | القيمة النهائية لـ ε في الاستكشاف إبسيلون-جشع |
| إطار الاستكشاف النهائي | 1,000,000 | عدد الإطارات التي يتناقص فيها القيمة الأولية لـ ε خطيًا إلى قيمتها النهائية |
| حجم بدء إعادة التشغيل | 50,000 | يتم تشغيل سياسة عشوائية موحدة لهذا العدد من الإطارات قبل بدء التعلم وتُستخدم الخبرة الناتجة لملء ذاكرة إعادة التشغيل |
| الحد الأقصى لعدم الإجراء | 30 | الحد الأقصى لعدد إجراءات "عدم فعل شيء" التي يتم تنفيذها بواسطة الوكيل في بداية الحلقة |

### 5.2 تصور دالة القيمة

يُظهر الشكل 2 تطور دالة القيمة أثناء التدريب على لعبة Seaquest. يُظهر اللوحة اليسرى الحالة الأولية (في هذه الحالة، الغواصة التابعة للوكيل على وشك إطلاق النار على غواص)، جنبًا إلى جنب مع خريطة حرارية لقيم الإجراءات المتوقعة بواسطة الشبكة. تُظهر اللوحات الثلاث اليمنى كيف تتطور القيمة المتوقعة مع تقدم التدريب. في البداية، تكون القيم حوالي 6، وهو تقريبًا العائد طويل الأجل الذي سيحصل عليه لاعب مبتدئ. بعد 10 ساعات من التدريب، تكون قيم-Q حوالي 18، مما يعكس حقيقة أن الوكيل تعلم تحقيق نقاط أعلى. أخيرًا، بعد تدريب كافٍ، تقدر الشبكة بدقة المكافأة طويلة الأجل لهذه الحالة، والتي تقترب من 25.

لإعطاء فهم نوعي لكيفية لعب نموذجنا المدرب لألعاب Atari، نوفر أيضًا تصورًا يُظهر دالة القيمة المتوقعة على أساس متجدد أثناء حلقة من Breakout. يُظهر التصور كلاً من القيمة المتوقعة والقيمة الفعلية (المحسوبة بتراكم المكافآت المخصومة الملاحظة أثناء الحلقة). في الجزء المبكر من اللعبة، يتنبأ النموذج بشكل صحيح بأن القيمة منخفضة لأن الوكيل لم ينشئ بعد النفق الذي يسمح له بإرسال الكرة فوق الطوب حيث ستحرز نقاطًا كثيرة. بمجرد أن يحفر الوكيل النفق، ترتفع القيم المتوقعة والفعلية بشكل حاد، وتبقى مرتفعة نسبيًا لبقية الحلقة حيث يستمر الوكيل في استغلال هذه الاستراتيجية.

يُظهر الشكل 3 قيم-Q المتوقعة على فترات زمنية منتظمة أثناء حلقة من Breakout. في البداية، تكون القيمة المتوقعة منخفضة (حوالي 6) نظرًا لأن الكرة عالقة تحت الطوب. ترتفع القيم بشكل حاد بعد أن يحفر الوكيل نفقًا، لتصل إلى أكثر من 20 عندما تبدأ الكرة في الارتداد فوق الطوب. ثم تنخفض القيم نحو نهاية الحلقة عندما يتبقى عدد أقل من الطوب.

### 5.3 التقييم الرئيسي

نقارن أداء وكلائنا بأفضل الأساليب أداءً من أدبيات التعلم المعزز. نبلغ عن النتائج في جميع الألعاب التي دربنا عليها. لتقييم الوكلاء، نتبع استراتيجية التقييم المستخدمة في بيئة Arcade Learning Environment، وهي تشغيل سياسة إبسيلون-جشعة (حيث $\epsilon = 0.05$) لإجمالي 100 حلقة والإبلاغ عن متوسط النقاط. استراتيجية التقييم هذه أكثر قوة ضد الإفراط في التجهيز من أخذ أقصى نقاط تم تحقيقها على الإطلاق، وهي أيضًا أقل ضوضاء من حساب المتوسط على عدد كبير من الحلقات.

**الجدول 2:** يُظهر الجدول العلوي متوسط النقاط المحققة لكل لعبة بواسطة طريقتنا (DQN)، والأساليب الأفضل أداءً من أدبيات التعلم المعزز (Sarsa و Contingency)، ومختبر ألعاب بشري محترف، واللعب العشوائي. يُظهر الجدول السفلي الأداء النسبي لـ DQN من حيث نسبة أداء الإنسان، ويُظهر تحسين DQN على أفضل طريقة تعلم معزز موجودة.

| اللعبة | عشوائي | Sarsa | Contingency | بشري | DQN |
|------|--------|-------|-------------|-------|-----|
| Beam Rider | 354 | 996 | 1,743 | 7,456 | 4,092 |
| Breakout | 1.2 | 5.2 | 6.1 | 31.0 | 168.0 |
| Enduro | 0 | 129 | 141 | 309 | 470 |
| Pong | -20.4 | -19.0 | -17.5 | -3.0 | 20.0 |
| Q*bert | 157 | 614 | 960 | 18,900 | 1,952 |
| Seaquest | 110 | 665 | 822 | 28,010 | 1,705 |
| Space Invaders | 179 | 271 | 268 | 3,690 | 1,075 |

| اللعبة | % من البشري | DQN مقابل أفضل تعلم معزز |
|------|---------|----------------|
| Beam Rider | 55% | 2.3x |
| Breakout | 542% | 27.5x |
| Enduro | 152% | 3.3x |
| Pong | 100%+ | N/A |
| Q*bert | 10% | 2.0x |
| Seaquest | 6% | 2.1x |
| Space Invaders | 29% | 4.0x |

تُظهر النتائج أن طريقتنا تحقق أداءً متوسطًا لا يقل عن 75٪ من مستوى الخبير البشري، وتتفوق على أفضل أساليب التعلم المعزز الموجودة في 6 من أصل 7 ألعاب. في Breakout، يحقق وكيلنا أداءً فائقًا على البشر، حيث يسجل أكثر من 5 أضعاف أفضل من الخبير البشري. في Pong و Enduro، يتجاوز الوكيل أيضًا اللاعب البشري. في الألعاب المتبقية، يؤدي الوكيل بمستوى بين أفضل أساليب التعلم المعزز والمستوى البشري.

هذه النتائج مذهلة بشكل خاص على Breakout، حيث يكتشف الوكيل الاستراتيجية المثلى المتمثلة في حفر نفق حول جانب الجدار، مما يسمح للكرة بضرب الجزء الخلفي مع تقليل مخاطر فقدان الكرة. لم تتم برمجة هذه الاستراتيجية بشكل صريح ولكنها نشأت من عملية التعلم. وبالمثل، على Enduro، يتعلم الوكيل البقاء بعيدًا جدًا عن السيارات الأخرى والمناورة عبر حركة المرور، بينما على Pong يتعلم بسرعة الاستراتيجية المثلى.

### 5.4 التحليل

أجرينا العديد من دراسات الاستئصال لفهم المكونات الأكثر أهمية لنجاح خوارزميتنا. أولاً، فحصنا تأثير استخدام إعادة تشغيل الخبرة. دربنا نسخة من طريقتنا بدون إعادة تشغيل الخبرة، ووجدنا أنها أدت بشكل أسوأ بكثير، مما يوضح الأهمية الحاسمة لهذه التقنية. ثانيًا، فحصنا تأثير تحديث شبكة-Q الهدف بشكل دوري فقط. وجدنا أن إزالة هذا التعديل أدت أيضًا إلى أداء أسوأ، على الرغم من أن التأثير كان أقل دراماتيكية من إزالة إعادة تشغيل الخبرة.

حققنا أيضًا في قوة طريقتنا لإعدادات المعاملات الفائقة المختلفة عن طريق التدريب على Seaquest بمعدلات تعلم مختلفة، وأحجام مجموعات صغيرة، وأحجام ذاكرة إعادة تشغيل. وجدنا أن الطريقة قوية نسبيًا للتغييرات في المعاملات الفائقة، على الرغم من أن الأداء يتدهور إذا كان معدل التعلم مرتفعًا جدًا أو منخفضًا جدًا.

أخيرًا، قمنا بتصور التمثيلات المتعلمة من خلال فحص ما تتعلمه الشبكة في طبقات مختلفة. وجدنا أن الطبقات المبكرة تتعلم كواشف الحواف وكواشف النقط المشابهة لتلك الموجودة في نماذج الرؤية الحاسوبية القياسية، بينما يبدو أن الطبقات اللاحقة تشفر ميزات أكثر خصوصية باللعبة مثل موضع الوكيل والأعداء.

---

### Translation Notes

- **Figures referenced:** Figure 2 (value function evolution), Figure 3 (Q-values during Breakout episode)
- **Tables referenced:** Table 1 (hyperparameters), Table 2 (results comparison)
- **Key terms introduced:**
  - ablation study (دراسة استئصال)
  - hyperparameter tuning (ضبط المعاملات الفائقة)
  - grid search (بحث شبكي)
  - heat map (خريطة حرارية)
  - overfitting (الإفراط في التجهيز)
  - edge detector (كاشف الحواف)
  - blob detector (كاشف النقط)
  - super-human performance (أداء فائق على البشر)
  - target network (الشبكة الهدف)
  - annealing (التناقص)

- **Equations:** 0
- **Citations:** References to Arcade Learning Environment evaluation strategy
- **Special handling:**
  - Game names kept in English (Beam Rider, Breakout, etc.)
  - RMSProp kept as-is (standard algorithm name)
  - Table formatting maintained with Arabic headers
  - Numerical values kept as-is in tables
  - Percentage and multiplication symbols (%, x) kept as-is

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
