# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** algorithm, reinforcement learning, gradient, optimization, stochastic, benchmark, complexity, empirical

---

### English Version

We propose a new family of policy gradient methods for reinforcement learning, which alternate between sampling data through interaction with the environment, and optimizing a "surrogate" objective function using stochastic gradient ascent. Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates. The new methods, which we call proximal policy optimization (PPO), have some of the benefits of trust region policy optimization (TRPO), but they are much simpler to implement, more general, and have better sample complexity (empirically). Our experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, and we show that PPO outperforms other online policy gradient methods, and overall strikes a favorable balance between sample complexity, simplicity, and wall-time.

---

### النسخة العربية

نقترح عائلة جديدة من طرق تدرجات السياسات للتعلم المعزز، والتي تتناوب بين أخذ عينات البيانات من خلال التفاعل مع البيئة، وتحسين دالة هدفية "بديلة" باستخدام الصعود التدرجي العشوائي. بينما تقوم طرق تدرجات السياسات القياسية بتحديث تدرجي واحد لكل عينة بيانات، نقترح دالة هدفية جديدة تمكن من عدة حقب من تحديثات الدفعات الصغيرة. الطرق الجديدة، التي نسميها تحسين السياسة التقريبية (PPO)، لها بعض فوائد تحسين السياسة بمنطقة الثقة (TRPO)، لكنها أبسط بكثير في التطبيق، وأكثر عمومية، ولها تعقيد عينات أفضل (تجريبياً). تختبر تجاربنا PPO على مجموعة من مهام المعايير القياسية، بما في ذلك الحركة الروبوتية المحاكاة ولعب ألعاب Atari، ونظهر أن PPO تتفوق على طرق تدرجات السياسات الأخرى عبر الإنترنت، وبشكل عام تحقق توازناً مواتياً بين تعقيد العينات والبساطة ووقت التنفيذ الفعلي.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - proximal policy optimization (PPO) - تحسين السياسة التقريبية
  - trust region policy optimization (TRPO) - تحسين السياسة بمنطقة الثقة
  - policy gradient - تدرجات السياسات
  - surrogate objective - دالة هدفية بديلة
  - sample complexity - تعقيد العينات
  - wall-time - وقت التنفيذ الفعلي
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Acronyms PPO and TRPO kept in English alongside Arabic translations

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90
