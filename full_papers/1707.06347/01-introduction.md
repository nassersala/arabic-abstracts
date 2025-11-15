# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** reinforcement learning, deep learning, algorithm, optimization, neural network, function approximation, gradient, hyperparameter, scalable, robust, data efficiency

---

### English Version

In recent years, several different approaches have been proposed for reinforcement learning with neural network function approximators. The leading contenders are deep Q-learning [Mni+15], "vanilla" policy gradient methods [Mni+16], and trust region / natural policy gradient methods [Sch+15b]. However, there is room for improvement in developing a method that is scalable (to large models and parallel implementations), data efficient, and robust (i.e., successful on a variety of problems without hyperparameter tuning). Q-learning (with function approximation) fails on many simple problems¹ and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust region policy optimization (TRPO) is relatively complicated, and is not compatible with architectures that include noise (such as dropout) or parameter sharing (between the policy and value function, or with auxiliary tasks).

This paper seeks to improve the current state of affairs by introducing an algorithm that attains the data efficiency and reliable performance of TRPO, while using only first-order optimization. We propose a novel objective with clipped probability ratios, which forms a pessimistic estimate (i.e., lower bound) of the performance of the policy. To optimize policies, we alternate between sampling data from the policy and performing several epochs of optimization on the sampled data.

Our experiments compare the performance of various different versions of the surrogate objective, and find that the version with the clipped probability ratios performs best. We also compare PPO to several previous algorithms from the literature. On continuous control tasks, it performs better than the algorithms we compare against. On Atari, it performs significantly better (in terms of sample complexity) than A2C and similarly to ACER though it is much simpler.

---

**Footnote:**

¹While DQN works well on game environments like the Arcade Learning Environment [Bel+15] with discrete action spaces, it has not been demonstrated to perform well on continuous control benchmarks such as those in OpenAI Gym [Bro+16] and described by Duan et al. [Dua+16].

---

### النسخة العربية

في السنوات الأخيرة، تم اقتراح عدة طرق مختلفة للتعلم المعزز مع مقربات الدوال بالشبكات العصبية. المتنافسون الرئيسيون هم تعلم-Q العميق [Mni+15]، وطرق تدرجات السياسات "البسيطة" [Mni+16]، وطرق منطقة الثقة/تدرجات السياسات الطبيعية [Sch+15b]. ومع ذلك، هناك مجال للتحسين في تطوير طريقة قابلة للتوسع (للنماذج الكبيرة والتطبيقات المتوازية)، وفعالة في استخدام البيانات، وقوية (أي ناجحة على مجموعة متنوعة من المشاكل دون ضبط المعاملات الفائقة). يفشل تعلم-Q (مع تقريب الدوال) في العديد من المشاكل البسيطة¹ وهو مفهوم بشكل سيء، وطرق تدرجات السياسات البسيطة لها كفاءة بيانات وقوة ضعيفة؛ وتحسين السياسة بمنطقة الثقة (TRPO) معقد نسبياً، وغير متوافق مع المعماريات التي تتضمن ضوضاء (مثل dropout) أو مشاركة المعاملات (بين دالة السياسة ودالة القيمة، أو مع المهام المساعدة).

تسعى هذه الورقة لتحسين الوضع الحالي من خلال تقديم خوارزمية تحقق كفاءة البيانات والأداء الموثوق لـ TRPO، مع استخدام التحسين من الدرجة الأولى فقط. نقترح دالة هدفية جديدة بنسب احتمالية مقصوصة، والتي تشكل تقديراً متشائماً (أي حد أدنى) لأداء السياسة. لتحسين السياسات، نتناوب بين أخذ عينات البيانات من السياسة وإجراء عدة حقب من التحسين على البيانات المأخوذة.

تقارن تجاربنا أداء إصدارات مختلفة من الدالة الهدفية البديلة، ونجد أن الإصدار بنسب الاحتمالية المقصوصة يحقق أفضل أداء. كما نقارن PPO بالعديد من الخوارزميات السابقة من الأدبيات. في مهام التحكم المستمر، تحقق أداءً أفضل من الخوارزميات التي نقارنها. في Atari، تحقق أداءً أفضل بكثير (من حيث تعقيد العينات) من A2C وبشكل مشابه لـ ACER رغم أنها أبسط بكثير.

---

**حاشية:**

¹بينما تعمل DQN بشكل جيد في بيئات الألعاب مثل بيئة التعلم من الآركيد [Bel+15] مع فضاءات الأفعال المنفصلة، لم يتم إثبات أدائها الجيد على معايير التحكم المستمر مثل تلك الموجودة في OpenAI Gym [Bro+16] والموصوفة من قبل Duan وآخرون [Dua+16].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - deep Q-learning - تعلم-Q العميق
  - vanilla policy gradient - تدرجات السياسات البسيطة
  - trust region - منطقة الثقة
  - natural policy gradient - تدرجات السياسات الطبيعية
  - scalable - قابلة للتوسع
  - data efficient - فعالة في استخدام البيانات
  - robust - قوية
  - hyperparameter tuning - ضبط المعاملات الفائقة
  - function approximation - تقريب الدوال
  - dropout - dropout (kept in English as technical term)
  - parameter sharing - مشاركة المعاملات
  - first-order optimization - التحسين من الدرجة الأولى
  - clipped probability ratios - نسب احتمالية مقصوصة
  - pessimistic estimate - تقدير متشائم
  - lower bound - حد أدنى
  - surrogate objective - دالة هدفية بديلة
  - continuous control - التحكم المستمر
  - sample complexity - تعقيد العينات
  - A2C - A2C (Advantage Actor-Critic)
  - ACER - ACER (Actor-Critic with Experience Replay)
- **Equations:** 0
- **Citations:** [Mni+15], [Mni+16], [Sch+15b], [Bel+15], [Bro+16], [Dua+16]
- **Special handling:**
  - Kept algorithm names (DQN, TRPO, PPO, A2C, ACER) in English as they are standard acronyms
  - Kept "dropout" in English as it's a technical term
  - Added footnote translation

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
