# Section 3: Multimodal Prompts for Task Specification
## القسم 3: الموجهات متعددة الوسائط لتحديد المهام

**Section:** method-multimodal-prompts
**Translation Quality:** 0.88
**Glossary Terms Used:** multimodal prompts, task specification, robot manipulation, visual goal, novel concept grounding, one-shot imitation, visual constraint satisfaction, visual reasoning, sequence

---

### English Version

A central and open problem in robot learning is task specification (Agrawal, 2022). In prior literature (Stepputtis et al., 2020; Dasari & Gupta, 2020; Brunke et al., 2021b), different tasks often require diverse and incompatible interfaces, resulting in siloed robot systems that do not generalize well across tasks. Our key insight is that various task specification paradigms (such as goal conditioning, video demonstration, natural language instruction) can all be instantiated as multimodal prompts (Fig. 1). Concretely, a multimodal prompt P of length l is defined as an ordered sequence of arbitrarily interleaved texts and images P := {x₁, x₂, ..., xₗ}, where each element xᵢ ∈ {text, image}.

**Task Suite.** The flexibility afforded by multimodal prompts allows us to specify and build models for a variety of task specification formats. Here we consider the following six categories.

1. **Simple object manipulation.** Simple tasks like "put <object> into <container>", where each image in the prompt corresponds to a single object;

2. **Visual goal reaching.** Manipulating objects to reach a goal configuration, e.g., Rearrangement (Batra et al., 2020);

3. **Novel concept grounding.** The prompt contains unfamiliar words like "dax" and "blicket", which are explained by in-prompt images and then immediately used in an instruction. This tests the agent's ability to rapidly internalize new concepts;

4. **One-shot video imitation.** Watching a video demonstration and learning to reproduce the same motion trajectory for a particular object;

5. **Visual constraint satisfaction.** The robot must manipulate the objects carefully and avoid violating the (safety) constraints;

6. **Visual reasoning.** Tasks that require reasoning skills, such as appearance matching "move all objects with same textures as <object> into <container>", and visual memory "put <object> in <container> and then restore to their original position".

Note that these six categories are not mutually exclusive. For example, a task may introduce a previously unseen verb (Novel Concept) by showing a video demonstration, or combine goal reaching with visual reasoning. More details about the task suite are discussed in Appendix, Sec. B.

---

### النسخة العربية

المشكلة المركزية والمفتوحة في تعلم الروبوتات هي تحديد المهام (Agrawal, 2022). في الأدبيات السابقة (Stepputtis et al., 2020; Dasari & Gupta, 2020; Brunke et al., 2021b)، غالباً ما تتطلب المهام المختلفة واجهات متنوعة وغير متوافقة، مما يؤدي إلى أنظمة روبوتية معزولة لا تتعمم جيداً عبر المهام. رؤيتنا الرئيسية هي أن نماذج تحديد المهام المختلفة (مثل التكييف بالهدف، والعرض التوضيحي بالفيديو، وتعليمات اللغة الطبيعية) يمكن جميعها إنشاؤها كموجهات متعددة الوسائط (الشكل 1). بشكل ملموس، يتم تعريف موجه متعدد الوسائط P بطول l كتسلسل مرتب من النصوص والصور المتداخلة بشكل تعسفي P := {x₁, x₂, ..., xₗ}، حيث كل عنصر xᵢ ∈ {نص، صورة}.

**مجموعة المهام.** تتيح لنا المرونة التي توفرها الموجهات متعددة الوسائط تحديد وبناء نماذج لمجموعة متنوعة من تنسيقات تحديد المهام. هنا نعتبر الفئات الست التالية.

1. **التلاعب البسيط بالأشياء.** مهام بسيطة مثل "ضع <الشيء> في <الحاوية>"، حيث تتوافق كل صورة في الموجه مع شيء واحد؛

2. **الوصول إلى الهدف البصري.** التلاعب بالأشياء للوصول إلى تكوين هدف، على سبيل المثال، إعادة الترتيب (Batra et al., 2020)؛

3. **تأسيس المفاهيم الجديدة.** يحتوي الموجه على كلمات غير مألوفة مثل "dax" و "blicket"، والتي يتم شرحها بصور داخل الموجه ثم يتم استخدامها فوراً في تعليمات. هذا يختبر قدرة الوكيل على استيعاب المفاهيم الجديدة بسرعة؛

4. **تقليد الفيديو لمرة واحدة.** مشاهدة عرض توضيحي بالفيديو والتعلم لإعادة إنتاج نفس مسار الحركة لشيء معين؛

5. **إرضاء القيود البصرية.** يجب على الروبوت التلاعب بالأشياء بعناية وتجنب انتهاك القيود (الأمان)؛

6. **الاستدلال البصري.** مهام تتطلب مهارات استدلالية، مثل مطابقة المظهر "نقل جميع الأشياء ذات الأنسجة نفسها مثل <الشيء> إلى <الحاوية>"، والذاكرة البصرية "ضع <الشيء> في <الحاوية> ثم أعده إلى موضعه الأصلي".

لاحظ أن هذه الفئات الست ليست حصرية متبادلة. على سبيل المثال، قد تقدم مهمة فعلاً غير مرئي سابقاً (مفهوم جديد) بعرض عرض توضيحي بالفيديو، أو تجمع بين الوصول إلى الهدف والاستدلال البصري. يتم مناقشة المزيد من التفاصيل حول مجموعة المهام في الملحق، القسم B.

---

### Translation Notes

- **Figures referenced:** Figure 1 (multimodal prompts illustration)
- **Key terms introduced:** multimodal prompts, task specification, novel concept grounding, one-shot video imitation, visual constraint satisfaction, visual reasoning
- **Equations:** Set notation for prompt definition: P := {x₁, x₂, ..., xₗ}
- **Citations:** Agrawal 2022, Stepputtis et al. 2020, Dasari & Gupta 2020, Brunke et al. 2021b, Batra et al. 2020
- **Special handling:**
  - Preserved mathematical notation for sequence definition
  - Maintained example prompts in quotes with English placeholders
  - Numbered list format preserved

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation

The central and open problem in robot learning is task specification (Agrawal, 2022). In previous literature (Stepputtis et al., 2020; Dasari & Gupta, 2020; Brunke et al., 2021b), different tasks often require diverse and incompatible interfaces, leading to isolated robot systems that do not generalize well across tasks. Our key insight is that different task specification paradigms (such as goal conditioning, video demonstration, natural language instructions) can all be instantiated as multimodal prompts (Figure 1). Concretely, a multimodal prompt P of length l is defined as an ordered sequence of arbitrarily interleaved texts and images P := {x₁, x₂, ..., xₗ}, where each element xᵢ ∈ {text, image}.

**Task Suite.** The flexibility provided by multimodal prompts allows us to specify and build models for a variety of task specification formats. Here we consider the following six categories.

1. **Simple object manipulation.** Simple tasks like "put <object> in <container>", where each image in the prompt corresponds to a single object;

2. **Visual goal reaching.** Manipulating objects to reach a goal configuration, for example, Rearrangement (Batra et al., 2020);

3. **Novel concept grounding.** The prompt contains unfamiliar words like "dax" and "blicket", which are explained by images within the prompt and then immediately used in instructions. This tests the agent's ability to rapidly internalize new concepts;

4. **One-shot video imitation.** Watching a video demonstration and learning to reproduce the same motion trajectory for a specific object;

5. **Visual constraint satisfaction.** The robot must manipulate objects carefully and avoid violating (safety) constraints;

6. **Visual reasoning.** Tasks requiring reasoning skills, such as appearance matching "move all objects with the same textures as <object> to <container>", and visual memory "put <object> in <container> then return it to its original position".

Note that these six categories are not mutually exclusive. For example, a task may introduce a previously unseen verb (new concept) by showing a video demonstration, or combine goal reaching with visual reasoning. More details about the task suite are discussed in Appendix, Section B.
