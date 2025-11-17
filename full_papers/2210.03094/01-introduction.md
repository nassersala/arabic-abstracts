# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** transformer, multimodal, prompts, generalization, zero-shot, robot manipulation, imitation learning, sequence modeling, multi-task learning, visual goal, language instructions

---

### English Version

Transformer models have enabled remarkable multi-task consolidation across AI domains. For instance, users can describe tasks to GPT-3 using natural language prompts, allowing a single model to perform question answering, machine translation, text summarization, and similar functions.

The authors envision that generalist robots should have "an intuitive and expressive interface for task specification." They illustrate this with a household robot example: it could receive simple language instructions like "bring me a cup of water," more specific multimodal instructions like "bring me <image of the cup>," or learn from video demonstrations for novel skills. Tasks involving unfamiliar objects can be explained through image examples, and visual constraints ensure safe deployment.

The work makes three key contributions: (1) a novel multimodal prompting formulation that converts diverse robot manipulation tasks into one sequence modeling problem; (2) a large-scale benchmark with systematic evaluation protocols; and (3) VIMA, a multimodal-prompted robot agent capable of multi-task and zero-shot generalization.

The central observation is that "many robot manipulation tasks can be formulated by multimodal prompts that interleave language and images or video frames." Examples include visual goal tasks like "Please rearrange objects to match this {scene_image}" and few-shot imitation prompts embedding video sequences.

Previously, different manipulation tasks required distinct architectures and training procedures, creating siloed systems. The multimodal prompt interface enables leveraging advances in large transformer models for developing scalable multi-task robot learners, offering an accessible alternative to specialized, incompatible approaches.

---

### النسخة العربية

مكّنت نماذج المحول من دمج متعدد المهام بشكل ملحوظ عبر مجالات الذكاء الاصطناعي. على سبيل المثال، يمكن للمستخدمين وصف المهام لـ GPT-3 باستخدام موجهات اللغة الطبيعية، مما يسمح لنموذج واحد بأداء الإجابة على الأسئلة، والترجمة الآلية، وتلخيص النصوص، ووظائف مماثلة.

يتصور المؤلفون أن الروبوتات متعددة الأغراض يجب أن يكون لديها "واجهة بديهية ومعبرة لتحديد المهام". يوضحون ذلك بمثال روبوت منزلي: يمكنه تلقي تعليمات لغوية بسيطة مثل "أحضر لي كوباً من الماء"، أو تعليمات متعددة الوسائط أكثر تحديداً مثل "أحضر لي <صورة الكوب>"، أو التعلم من عروض فيديو توضيحية لمهارات جديدة. يمكن شرح المهام التي تتضمن أشياء غير مألوفة من خلال أمثلة صور، والقيود البصرية تضمن النشر الآمن.

يقدم العمل ثلاث مساهمات رئيسية: (1) صياغة موجهات متعددة الوسائط جديدة تحول مهام التلاعب الروبوتي المتنوعة إلى مشكلة نمذجة تسلسل واحدة؛ (2) معيار واسع النطاق مع بروتوكولات تقييم منهجية؛ و(3) VIMA، وكيل روبوتي مدفوع بموجهات متعددة الوسائط قادر على التعلم متعدد المهام والتعميم بدون أمثلة.

الملاحظة المركزية هي أن "العديد من مهام التلاعب الروبوتي يمكن صياغتها بموجهات متعددة الوسائط تتداخل فيها اللغة والصور أو إطارات الفيديو". تشمل الأمثلة مهام الأهداف البصرية مثل "يرجى إعادة ترتيب الأشياء لتتطابق مع هذا {scene_image}" وموجهات التقليد قليلة الأمثلة التي تضمن تسلسلات فيديو.

في السابق، كانت مهام التلاعب المختلفة تتطلب معماريات وإجراءات تدريب متميزة، مما يخلق أنظمة معزولة. تمكّن واجهة الموجهات متعددة الوسائط من الاستفادة من التقدم في نماذج المحول الكبيرة لتطوير متعلمي روبوتات متعددي المهام وقابلين للتوسع، مما يوفر بديلاً ميسراً للنهج المتخصصة وغير المتوافقة.

---

### Translation Notes

- **Figures referenced:** None directly in this section
- **Key terms introduced:** multimodal prompting, generalist robots, task specification interface, sequence modeling, few-shot imitation
- **Equations:** None
- **Citations:** Reference to GPT-3
- **Special handling:**
  - Preserved example prompts in quotes with Arabic translation
  - Maintained technical term consistency with glossary
  - Used formal academic Arabic style

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation

Transformer models enabled remarkable multi-task consolidation across AI fields. For example, users can describe tasks to GPT-3 using natural language prompts, allowing a single model to perform question answering, machine translation, text summarization, and similar functions.

The authors envision that general-purpose robots should have "an intuitive and expressive interface for task specification." They illustrate this with a household robot example: it can receive simple language instructions like "bring me a cup of water," or more specific multimodal instructions like "bring me <image of the cup>," or learn from video demonstrations for new skills. Tasks involving unfamiliar objects can be explained through image examples, and visual constraints ensure safe deployment.

The work presents three key contributions: (1) a new multimodal prompting formulation that converts diverse robot manipulation tasks into a single sequence modeling problem; (2) a large-scale benchmark with systematic evaluation protocols; and (3) VIMA, a robot agent driven by multimodal prompts capable of multi-task learning and zero-shot generalization.

The central observation is that "many robot manipulation tasks can be formulated with multimodal prompts that interleave language and images or video frames." Examples include visual goal tasks like "please rearrange objects to match this {scene_image}" and few-shot imitation prompts that embed video sequences.

Previously, different manipulation tasks required distinct architectures and training procedures, creating isolated systems. The multimodal prompts interface enables leveraging advances in large transformer models to develop scalable multi-task robot learners, providing an accessible alternative to specialized, incompatible approaches.
