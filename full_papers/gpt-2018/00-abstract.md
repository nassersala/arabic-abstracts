# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** natural language, unsupervised, supervised, fine-tuning, discriminative, pre-training, language model, benchmarks, task-agnostic

---

### English Version

Natural language understanding comprises a wide range of diverse tasks such as textual entailment, question answering, semantic similarity assessment, and document classification. Although large unlabeled text corpora are abundant, labeled data for learning these specific tasks is scarce, making it challenging for discriminatively trained models to perform adequately. We demonstrate that large gains on these tasks can be realized by generative pre-training of a language model on a diverse corpus of unlabeled text, followed by discriminative fine-tuning on each specific task. In contrast to previous approaches, we make use of task-aware input transformations during fine-tuning to achieve effective transfer while requiring minimal changes to the model architecture. We demonstrate the effectiveness of our approach on a wide range of benchmarks for natural language understanding. Our general task-agnostic model outperforms discriminatively trained models that use architectures specifically crafted for each task, significantly improving upon the state of the art in 9 out of the 12 tasks studied. For instance, we achieve absolute improvements of 8.9% on commonsense reasoning (Stories Cloze Test), 5.7% on question answering (RACE), and 1.5% on textual entailment (MultiNLI).

---

### النسخة العربية

يشمل فهم اللغة الطبيعية مجموعة واسعة من المهام المتنوعة مثل الاستلزام النصي، والإجابة على الأسئلة، وتقييم التشابه الدلالي، وتصنيف المستندات. على الرغم من وفرة المدونات النصية الكبيرة غير المُعنونة، إلا أن البيانات المُعنونة اللازمة لتعلم هذه المهام المحددة نادرة، مما يجعل من الصعب على النماذج المُدربة بشكل تمييزي أن تؤدي أداءً ملائماً. نُظهر أن مكاسب كبيرة في هذه المهام يمكن تحقيقها من خلال التدريب المسبق التوليدي لنموذج لغة على مدونة متنوعة من النصوص غير المُعنونة، يليه ضبط دقيق تمييزي لكل مهمة محددة. على النقيض من الأساليب السابقة، نستخدم تحويلات إدخال واعية بالمهمة أثناء الضبط الدقيق لتحقيق نقل فعّال مع الحاجة إلى تغييرات طفيفة في معمارية النموذج. نُظهر فعالية نهجنا على مجموعة واسعة من معايير فهم اللغة الطبيعية. يتفوق نموذجنا العام المستقل عن المهام على النماذج المُدربة تمييزياً التي تستخدم معماريات مصممة خصيصاً لكل مهمة، محققاً تحسينات كبيرة على أحدث ما توصلت إليه التقنية في 9 من أصل 12 مهمة تمت دراستها. على سبيل المثال، نحقق تحسينات مطلقة بنسبة 8.9% في الاستدلال المنطقي (اختبار Stories Cloze)، و5.7% في الإجابة على الأسئلة (RACE)، و1.5% في الاستلزام النصي (MultiNLI).

---

### Translation Notes

- **Key terms introduced:**
  - Natural language understanding = فهم اللغة الطبيعية
  - Textual entailment = الاستلزام النصي
  - Semantic similarity = التشابه الدلالي
  - Generative pre-training = التدريب المسبق التوليدي
  - Discriminative fine-tuning = ضبط دقيق تمييزي
  - Task-agnostic = مستقل عن المهام
  - Commonsense reasoning = الاستدلال المنطقي

- **Benchmark names:** Kept in English (Stories Cloze Test, RACE, MultiNLI) as they are proper names
- **Percentages and numbers:** Preserved exactly as in original

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90
