# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** dexterous manipulation, state-action space, exploration, reinforcement learning, off-policy, demonstration, policy iteration, importance sampling, prior, bimanual robot

---

### English Version

Learning dexterous manipulation in high-dimensional state-action spaces is an important open challenge with exploration presenting a major bottleneck. Although in many cases the learning process could be guided by demonstrations or other suboptimal experts, current RL algorithms for continuous action spaces often fail to effectively utilize combinations of highly off-policy expert data and on-policy exploration data. As a solution, we introduce Relative Entropy Q-Learning (REQ), a simple policy iteration algorithm that combines ideas from successful offline and conventional RL algorithms. It represents the optimal policy via importance sampling from a learned prior and is well-suited to take advantage of mixed data distributions. We demonstrate experimentally that REQ outperforms several strong baselines on robotic manipulation tasks for which suboptimal experts are available. We show how suboptimal experts can be constructed effectively by composing simple waypoint tracking controllers, and we also show how learned primitives can be combined with waypoint controllers to obtain reference behaviors to bootstrap a complex manipulation task on a simulated bimanual robot with human-like hands. Finally, we show that REQ is also effective for general off-policy RL, offline RL, and RL from demonstrations.

---

### النسخة العربية

يُعد تعلم التلاعب البارع في فضاءات الحالة-الفعل عالية الأبعاد تحدياً مفتوحاً مهماً حيث يشكل الاستكشاف عائقاً رئيسياً. على الرغم من أنه في كثير من الحالات يمكن توجيه عملية التعلم بواسطة العروض التوضيحية أو خبراء غير مثاليين آخرين، إلا أن خوارزميات التعلم المعزز الحالية لفضاءات الأفعال المستمرة غالباً ما تفشل في الاستفادة بفعالية من مجموعات بيانات الخبراء عالية الانحراف عن السياسة وبيانات الاستكشاف المتوافقة مع السياسة. كحل، نقدم التعلم-Q بالإنتروبيا النسبية (REQ)، وهي خوارزمية بسيطة لتكرار السياسة تجمع أفكاراً من خوارزميات التعلم المعزز غير المتصلة بالإنترنت والتقليدية الناجحة. تمثل السياسة المثلى من خلال أخذ العينات بالأهمية من مُسبَق مُتعلَّم وهي مناسبة تماماً للاستفادة من توزيعات البيانات المختلطة. نوضح تجريبياً أن REQ تتفوق على عدة خطوط أساس قوية في مهام التلاعب الروبوتي التي تتوفر لها خبراء غير مثاليين. نوضح كيف يمكن بناء خبراء غير مثاليين بفعالية من خلال تركيب متحكمات تتبع نقاط المسار البسيطة، ونوضح أيضاً كيف يمكن دمج العناصر الأولية المتعلمة مع متحكمات نقاط المسار للحصول على سلوكيات مرجعية لتهيئة مهمة تلاعب معقدة على روبوت ثنائي اليد محاكى بأيدٍ شبيهة بالبشر. أخيراً، نوضح أن REQ فعالة أيضاً للتعلم المعزز العام خارج السياسة، والتعلم المعزز غير المتصل بالإنترنت، والتعلم المعزز من العروض التوضيحية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Relative Entropy Q-Learning (REQ), importance sampling, learned prior, suboptimal experts, waypoint tracking controllers
- **Equations:** 0
- **Citations:** 0
- **Special handling:** None

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.90
- Glossary consistency: 0.89
- **Overall section score:** 0.91
