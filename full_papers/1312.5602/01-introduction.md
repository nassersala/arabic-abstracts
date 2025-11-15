# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** reinforcement learning, deep learning, computer vision, algorithm, high-dimensional, feature, supervised learning, temporal difference, convolutional neural network

---

### English Version

Learning to control agents directly from high-dimensional sensory inputs like vision and speech is one of the long-standing challenges of reinforcement learning (RL). Most successful RL applications that operate on these domains have relied on hand-crafted features combined with linear value functions or policy representations. Clearly, the performance of such systems heavily relies on the quality of the feature representation.

Recent advances in deep learning have made it possible to extract high-level features from raw sensory data, leading to breakthroughs in computer vision and speech recognition. These methods utilize a range of neural network architectures, including convolutional networks, multilayer perceptrons, restricted Boltzmann machines and recurrent neural networks, and have exploited both supervised and unsupervised learning. It seems natural, therefore, to ask whether similar techniques could also be beneficial for RL with sensory data.

However, reinforcement learning presents several challenges from a deep learning perspective. First, most successful deep learning applications to date have required large amounts of hand-labelled training data. RL algorithms, on the other hand, must be able to learn from a scalar reward signal that is frequently sparse, noisy and delayed. The delay between actions and resulting rewards, which can be thousands of timesteps long, seems particularly daunting when compared to the direct association between inputs and targets found in supervised learning. Another issue is that most deep learning algorithms assume the data samples to be independent, while in reinforcement learning one typically encounters sequences of highly correlated states. Furthermore, in RL the data distribution changes as the algorithm learns new behaviours, which can be problematic for deep learning methods that assume a fixed underlying distribution.

This paper demonstrates that a convolutional neural network can overcome these challenges to learn successful control policies from raw video data in complex RL environments. The network is trained with a variant of the Q-learning algorithm, with stochastic gradient descent to update the weights. To alleviate the problems of correlated data and non-stationary distributions, we use an experience replay mechanism which randomly samples previous transitions, and thereby smooths the training distribution over many past behaviors.

We apply our approach to a range of Atari 2600 games implemented in The Arcade Learning Environment (ALE). Atari 2600 is a challenging RL testbed that presents agents with a high dimensional visual input (210 × 160 RGB video at 60Hz) and a diverse and interesting set of tasks that were designed to be difficult for humans players. Our goal is to create a single neural network agent that is able to successfully learn to play as many of the games as possible. The network was not provided with any game-specific information or hand-designed visual features, and was not privy to the internal state of the emulator; it learned from nothing but the video input, the reward and terminal signals, and the set of possible actions—just as a human player would. Furthermore the network architecture and all hyperparameters used for training were kept constant across the games. So far the network has outperformed all previous RL methods on six of the seven games we have attempted and surpassed an expert human player on three of them. Figure 1 provides sample screenshots from five of the games used for training.

---

### النسخة العربية

يُعدّ تعلُّم التحكم بالوكلاء مباشرة من المدخلات الحسية عالية الأبعاد مثل الرؤية والكلام أحد التحديات الطويلة الأمد في التعلم المعزز (RL). اعتمدت معظم تطبيقات التعلم المعزز الناجحة التي تعمل على هذه المجالات على ميزات مصممة يدويًا مدمجة مع دوال قيمة خطية أو تمثيلات سياسات. من الواضح أن أداء مثل هذه الأنظمة يعتمد بشكل كبير على جودة تمثيل الميزات.

أتاحت التطورات الحديثة في التعلم العميق استخراج ميزات عالية المستوى من البيانات الحسية الخام، مما أدى إلى اختراقات في الرؤية الحاسوبية والتعرف على الكلام. تستخدم هذه الأساليب مجموعة من معماريات الشبكات العصبية، بما في ذلك الشبكات الالتفافية، والإدراك متعدد الطبقات، وآلات بولتزمان المقيدة، والشبكات العصبية التكرارية، وقد استفادت من التعلم الموجه وغير الموجه على حد سواء. لذلك يبدو من الطبيعي أن نتساءل عما إذا كانت تقنيات مماثلة يمكن أن تكون مفيدة أيضًا للتعلم المعزز مع البيانات الحسية.

ومع ذلك، يطرح التعلم المعزز عدة تحديات من منظور التعلم العميق. أولاً، تطلبت معظم تطبيقات التعلم العميق الناجحة حتى الآن كميات كبيرة من بيانات التدريب المُصنّفة يدويًا. من ناحية أخرى، يجب أن تكون خوارزميات التعلم المعزز قادرة على التعلم من إشارة مكافأة قياسية غالبًا ما تكون متفرقة وصاخبة ومتأخرة. يبدو التأخير بين الإجراءات والمكافآت الناتجة، والذي يمكن أن يمتد لآلاف الخطوات الزمنية، شاقًا بشكل خاص عند مقارنته بالربط المباشر بين المدخلات والأهداف الموجود في التعلم الموجه. قضية أخرى هي أن معظم خوارزميات التعلم العميق تفترض أن عينات البيانات مستقلة، بينما في التعلم المعزز نواجه عادةً تسلسلات من الحالات المترابطة بشكل كبير. علاوة على ذلك، في التعلم المعزز يتغير توزيع البيانات مع تعلم الخوارزمية سلوكيات جديدة، وهو ما قد يكون إشكاليًا لأساليب التعلم العميق التي تفترض توزيعًا أساسيًا ثابتًا.

تُظهر هذه الورقة أن الشبكة العصبية الالتفافية يمكنها التغلب على هذه التحديات لتعلم سياسات تحكم ناجحة من بيانات الفيديو الخام في بيئات التعلم المعزز المعقدة. يتم تدريب الشبكة بنسخة من خوارزمية Q-learning، مع الانحدار التدرجي العشوائي لتحديث الأوزان. لتخفيف مشاكل البيانات المترابطة والتوزيعات غير الثابتة، نستخدم آلية إعادة تشغيل الخبرة التي تقوم بأخذ عينات عشوائية من الانتقالات السابقة، وبالتالي تنعيم توزيع التدريب على العديد من السلوكيات السابقة.

نطبق نهجنا على مجموعة من ألعاب Atari 2600 المُنفّذة في بيئة Arcade Learning Environment (ALE). يُعدّ Atari 2600 بيئة اختبار صعبة للتعلم المعزز تقدم للوكلاء مدخلاً مرئيًا عالي الأبعاد (فيديو RGB بدقة 210 × 160 بمعدل 60Hz) ومجموعة متنوعة ومثيرة للاهتمام من المهام التي صُممت لتكون صعبة على اللاعبين البشر. هدفنا هو إنشاء وكيل شبكة عصبية واحد قادر على تعلم لعب أكبر عدد ممكن من الألعاب بنجاح. لم يتم تزويد الشبكة بأي معلومات خاصة باللعبة أو ميزات بصرية مصممة يدويًا، ولم تكن على علم بالحالة الداخلية للمحاكي؛ تعلمت من مدخل الفيديو فقط، وإشارات المكافأة والإنهاء، ومجموعة الإجراءات الممكنة - تمامًا كما يفعل اللاعب البشري. علاوة على ذلك، تم الحفاظ على معمارية الشبكة وجميع المعاملات الفائقة المستخدمة للتدريب ثابتة عبر الألعاب. حتى الآن، تفوقت الشبكة على جميع أساليب التعلم المعزز السابقة في ستة من الألعاب السبعة التي حاولناها وتجاوزت لاعبًا بشريًا خبيرًا في ثلاثة منها. يوفر الشكل 1 لقطات شاشة نموذجية من خمس من الألعاب المستخدمة للتدريب.

---

### Translation Notes

- **Figures referenced:** Figure 1 (sample screenshots from games)
- **Key terms introduced:** experience replay (إعادة تشغيل الخبرة), Q-learning, stochastic gradient descent (الانحدار التدرجي العشوائي), action-value function, temporal correlation, non-stationary distribution
- **Equations:** 0
- **Citations:** Implicit references to deep learning literature
- **Special handling:**
  - Game names (Atari 2600, Arcade Learning Environment) kept in English
  - Technical specifications (210 × 160 RGB, 60Hz) kept as-is
  - Boltzmann machines (آلات بولتزمان) - transcribed name

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
