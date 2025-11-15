# Section 4: Related Work
## القسم 4: الأعمال ذات الصلة

**Section:** related work
**Translation Quality:** 0.86
**Glossary Terms Used:** temporal difference learning, function approximation, neural network, reinforcement learning, Q-learning, value iteration, supervised learning

---

### English Version

Perhaps the best known success story of reinforcement learning is TD-Gammon, a backgammon playing program which learned entirely by self-play and achieved a level of play comparable to the best human players. TD-Gammon used a model-free reinforcement learning algorithm similar to Q-learning, and approximated the value function using a multi-layer perceptron with one hidden layer.

However, early attempts to follow up on TD-Gammon, including applications of the same method to chess, backgammon using a raw board representation and Go, were less successful. This led to a widespread belief that the convergence problems of TD-learning combined with neural networks would doom the approach to failure on all but the simplest problems. Indeed, the literature is replete with theoretical results showing that even Q-learning can diverge when combined with a nonlinear function approximator or even with a linear function approximator in the off-policy setting.

Nevertheless, another line of research has recently demonstrated that deep reinforcement learning is quite feasible by combining an experience replay memory with restricted Boltzmann machines to represent value functions. This architecture was successful at learning simple game-playing strategies, but it relied on heavily pre-training the layers of the network using unsupervised learning techniques. Our work shows that successful reinforcement learning is possible with deep neural networks and raw visual input without any unsupervised pre-training.

There has been substantial prior work on applying deep learning approaches to the problem of learning from pixels for robotic control. Most of this work, however, has employed supervised learning techniques on data collected from a teacher or learning algorithm, and has not directly addressed the reinforcement learning problem of learning from rewards. Closest to our work is a line of research that has recently used neural networks to represent visual features in the context of reinforcement learning. The main difference from our approach is that these methods learn only a representation for vision and not an end-to-end policy from pixels to actions.

Several researchers have investigated methods for incorporating visual or sensory context into traditional hand-coded features for Atari games. The HyperNEAT-GGP system evolved a convolutional neural network for 61 Atari games, but performed no better than random on most of them. Similar to previous work on general game playing, these approaches rely on the learned or hand-designed features to generalize to new games. Our approach learns a representation that is entirely game-specific, but is able to do so remarkably quickly. Our method builds a representation on the fly, in a sample efficient way that allows for rapid generalization.

There have been several previous attempts to apply reinforcement learning to Atari games. The most successful previous approach is the contingency (CONT) agent, which scored better than human experts on 15 of the 51 games tested. This approach used a simple linear method, Sarsa learning with hand-coded visual features. When applied to a small set of games, learning linear control policies from the raw pixel input was found to perform much worse than using hand-crafted features. In our work, we demonstrate that deep learning methods can successfully learn from pixels without hand-coded features, and in fact, achieve state-of-the-art performance on a significant proportion of the games.

An earlier version of our work has appeared in a workshop paper. The present version adds an analysis of the method, a more detailed description of the algorithm, results for more games, and an improved network architecture.

---

### النسخة العربية

ربما تكون قصة النجاح الأكثر شهرة للتعلم المعزز هي TD-Gammon، وهو برنامج لعب طاولة الزهر تعلم بالكامل عن طريق اللعب الذاتي وحقق مستوى لعب مماثل لأفضل اللاعبين البشر. استخدم TD-Gammon خوارزمية تعلم معزز خالية من النموذج مماثلة لـ Q-learning، وقرب دالة القيمة باستخدام إدراك متعدد الطبقات مع طبقة مخفية واحدة.

ومع ذلك، كانت المحاولات المبكرة لمتابعة TD-Gammon، بما في ذلك تطبيقات نفس الأسلوب على الشطرنج، وطاولة الزهر باستخدام تمثيل لوحة خام، والـ Go، أقل نجاحًا. أدى هذا إلى اعتقاد واسع النطاق بأن مشاكل التقارب لـ TD-learning مع الشبكات العصبية ستحكم على النهج بالفشل في جميع المشاكل باستثناء أبسطها. في الواقع، الأدبيات مليئة بالنتائج النظرية التي تُظهر أن حتى Q-learning يمكن أن يتباعد عند دمجه مع مقرب دالي غير خطي أو حتى مع مقرب دالي خطي في إعداد خارج السياسة.

ومع ذلك، أظهر خط بحث آخر مؤخرًا أن التعلم المعزز العميق ممكن تمامًا من خلال الجمع بين ذاكرة إعادة تشغيل الخبرة وآلات بولتزمان المقيدة لتمثيل دوال القيمة. نجحت هذه المعمارية في تعلم استراتيجيات لعب بسيطة، لكنها اعتمدت بشكل كبير على التدريب المسبق لطبقات الشبكة باستخدام تقنيات التعلم غير الموجه. يُظهر عملنا أن التعلم المعزز الناجح ممكن مع الشبكات العصبية العميقة والمدخلات المرئية الخام دون أي تدريب مسبق غير موجه.

كان هناك عمل سابق كبير على تطبيق أساليب التعلم العميق على مشكلة التعلم من البكسلات للتحكم الروبوتي. ومع ذلك، فقد استخدم معظم هذا العمل تقنيات التعلم الموجه على البيانات التي تم جمعها من معلم أو خوارزمية تعلم، ولم يعالج مباشرة مشكلة التعلم المعزز المتمثلة في التعلم من المكافآت. الأقرب إلى عملنا هو خط بحث استخدم مؤخرًا الشبكات العصبية لتمثيل الميزات البصرية في سياق التعلم المعزز. الفرق الرئيسي عن نهجنا هو أن هذه الأساليب تتعلم فقط تمثيلًا للرؤية وليس سياسة شاملة من البكسلات إلى الإجراءات.

حقق العديد من الباحثين في أساليب لدمج السياق البصري أو الحسي في الميزات المشفرة يدويًا التقليدية لألعاب Atari. طور نظام HyperNEAT-GGP شبكة عصبية التفافية لـ 61 لعبة Atari، لكنه لم يؤدِ أفضل من العشوائي في معظمها. على غرار العمل السابق على اللعب العام للألعاب، تعتمد هذه الأساليب على الميزات المتعلمة أو المصممة يدويًا للتعميم على ألعاب جديدة. يتعلم نهجنا تمثيلًا خاصًا تمامًا باللعبة، لكنه قادر على القيام بذلك بسرعة ملحوظة. تبني طريقتنا تمثيلًا بشكل فوري، بطريقة فعالة من حيث العينات تسمح بتعميم سريع.

كانت هناك عدة محاولات سابقة لتطبيق التعلم المعزز على ألعاب Atari. النهج السابق الأكثر نجاحًا هو وكيل الطوارئ (CONT)، الذي سجل أفضل من الخبراء البشر في 15 من 51 لعبة تم اختبارها. استخدم هذا النهج أسلوبًا خطيًا بسيطًا، تعلم Sarsa مع ميزات بصرية مشفرة يدويًا. عند تطبيقه على مجموعة صغيرة من الألعاب، وُجد أن تعلم سياسات التحكم الخطية من مدخل البكسل الخام يؤدي أداءً أسوأ بكثير من استخدام الميزات المصممة يدويًا. في عملنا، نثبت أن أساليب التعلم العميق يمكن أن تتعلم بنجاح من البكسلات دون ميزات مشفرة يدويًا، وفي الواقع، تحقق أداءً متقدمًا في نسبة كبيرة من الألعاب.

ظهرت نسخة سابقة من عملنا في ورقة ورشة عمل. تضيف النسخة الحالية تحليلاً للطريقة، ووصفًا أكثر تفصيلاً للخوارزمية، ونتائج لمزيد من الألعاب، ومعمارية شبكة محسّنة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - TD-Gammon (تم الإبقاء على الاسم كما هو)
  - TD-learning (تعلم TD)
  - Sarsa learning (تعلم Sarsa)
  - HyperNEAT-GGP (تم الإبقاء على الاسم كما هو)
  - contingency agent (وكيل الطوارئ)
  - unsupervised pre-training (تدريب مسبق غير موجه)
  - end-to-end policy (سياسة شاملة)
  - sample efficient (فعال من حيث العينات)
  - general game playing (اللعب العام للألعاب)
  - convergence problems (مشاكل التقارب)

- **Equations:** 0
- **Citations:** Multiple implicit references to prior work (TD-Gammon, HyperNEAT-GGP, CONT agent, Sarsa)
- **Special handling:**
  - Game names (backgammon, chess, Go) - chess translated as الشطرنج, backgammon as طاولة الزهر, Go kept as Go
  - Algorithm/system names kept in English (TD-Gammon, HyperNEAT-GGP, CONT, Sarsa)
  - "state-of-the-art" translated as أداء متقدم

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.86
