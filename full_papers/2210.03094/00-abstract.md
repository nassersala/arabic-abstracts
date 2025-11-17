# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** prompt-based learning, natural language processing, language model, robot manipulation, demonstration, multimodal, transformer, imitation learning, generalization, zero-shot, scalability, data efficiency, motor actions, tabletop tasks, autoregressive

---

### English Version

Prompt-based learning has emerged as a successful paradigm in natural language processing, where a single general-purpose language model can be instructed to perform any task specified by input prompts. Yet task specification in robotics comes in various forms, such as imitating one-shot demonstrations, following language instructions, and reaching visual goals. They are often considered different tasks and tackled by specialized models. We show that a wide spectrum of robot manipulation tasks can be expressed with multimodal prompts, interleaving textual and visual tokens. Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and a four-level evaluation protocol for systematic generalization. We design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor actions autoregressively. VIMA features a recipe that achieves strong model scalability and data efficiency. It outperforms alternative designs in the hardest zero-shot generalization setting by up to $2.9\times$ task success rate given the same training data. With $10\times$ less training data, VIMA still performs $2.7\times$ better than the best competing variant.

---

### النسخة العربية

ظهر التعلم القائم على الموجهات كنموذج ناجح في معالجة اللغة الطبيعية، حيث يمكن توجيه نموذج لغة واحد عام الغرض لأداء أي مهمة محددة بواسطة موجهات الإدخال. ومع ذلك، فإن تحديد المهام في الروبوتات يأتي بأشكال مختلفة، مثل تقليد العروض التوضيحية لمرة واحدة، واتباع تعليمات اللغة، والوصول إلى أهداف بصرية. غالباً ما تُعتبر مهام مختلفة ويتم معالجتها بواسطة نماذج متخصصة. نوضح أن طيفاً واسعاً من مهام التلاعب الروبوتي يمكن التعبير عنها بموجهات متعددة الوسائط، تتداخل فيها الرموز النصية والبصرية. وفقاً لذلك، نطور معياراً محاكاةً جديداً يتكون من آلاف المهام المكتبية المُولَّدة إجرائياً بموجهات متعددة الوسائط، وأكثر من 600 ألف مسار خبير للتعلم بالتقليد، وبروتوكول تقييم من أربعة مستويات للتعميم المنهجي. نصمم وكيلاً روبوتياً قائماً على المحول، VIMA، الذي يعالج هذه الموجهات ويُخرج إجراءات حركية بشكل انحداري ذاتي. يتميز VIMA بوصفة تحقق قابلية توسع قوية للنموذج وكفاءة البيانات. يتفوق على التصميمات البديلة في أصعب إعداد للتعميم بدون أمثلة بمعدل نجاح مهام يصل إلى 2.9 مرة عند إعطائه نفس بيانات التدريب. مع بيانات تدريب أقل بـ 10 مرات، لا يزال VIMA يؤدي أفضل بـ 2.7 مرة من أفضل متغير منافس.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** multimodal prompts, prompt-based learning, robot manipulation, zero-shot generalization, transformer-based agent, behavioral cloning, imitation learning
- **Equations:** None
- **Citations:** None in abstract
- **Special handling:** None

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.93
- Readability: 0.92
- Glossary consistency: 0.93
- **Overall section score:** 0.93

### Back-Translation Validation

Prompt-based learning has emerged as a successful paradigm in natural language processing, where a single general-purpose language model can be directed to perform any task specified by input prompts. However, task specification in robotics comes in various forms, such as imitating one-shot demonstrations, following language instructions, and reaching visual goals. They are often considered different tasks and are handled by specialized models. We show that a wide spectrum of robot manipulation tasks can be expressed with multimodal prompts, with interleaving textual and visual tokens. Accordingly, we develop a new simulation benchmark consisting of thousands of procedurally-generated desktop tasks with multimodal prompts, over 600 thousand expert trajectories for imitation learning, and a four-level evaluation protocol for systematic generalization. We design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor actions autoregressively. VIMA features a recipe that achieves strong model scalability and data efficiency. It outperforms alternative designs in the hardest zero-shot generalization setting by up to 2.9× task success rate when given the same training data. With 10× less training data, VIMA still performs 2.7× better than the best competing variant.
