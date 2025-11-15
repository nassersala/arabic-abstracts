# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** self-training (التدريب الذاتي), ELMo, GPT, BERT, XLM, XLNet, performance gains (مكاسب الأداء), hyperparameter tuning (ضبط المعاملات الفائقة), masked language model (نموذج اللغة المقنع), next sentence prediction (التنبؤ بالجملة التالية), dynamic masking (الإخفاء الديناميكي), state-of-the-art (الأحدث والأفضل)

---

### English Version

Self-training methods such as ELMo (Peters et al., 2018), GPT (Radford et al., 2018), BERT (Devlin et al., 2019), XLM (Lample and Conneau, 2019), and XLNet (Yang et al., 2019) have brought significant performance gains, but it can be challenging to determine which aspects of the methods contribute the most. Training is computationally expensive, limiting the amount of tuning that can be done, and is often done with private training data of varying sizes, limiting our ability to measure the effects of the modeling advances.

We present a replication study of BERT pretraining (Devlin et al., 2019), which includes a careful evaluation of the effects of hyperparmeter tuning and training set size. We find that BERT was significantly undertrained and propose an improved recipe for training BERT models, which we call RoBERTa, that can match or exceed the performance of all of the post-BERT methods. Our modifications are simple, they include: (1) training the model longer, with bigger batches, over more data; (2) removing the next sentence prediction objective; (3) training on longer sequences; and (4) dynamically changing the masking pattern applied to the training data. We also collect a large new dataset (CC-NEWS) of comparable size to other privately used datasets, to better control for training set size effects.

When controlling for training data, our improved training procedure improves upon the published BERT results on both GLUE and SQuAD. When trained for longer over additional data, our model achieves a score of 88.5 on the public GLUE leaderboard, matching the 88.4 reported by Yang et al. (2019). Our model establishes a new state-of-the-art on 4/9 of the GLUE tasks: MNLI, QNLI, RTE and STS-B. We also match state-of-the-art results on SQuAD and RACE. Overall, we re-establish that BERT's masked language model training objective is competitive with other recently proposed training objectives such as perturbed autoregressive language modeling (Yang et al., 2019).

In summary, the contributions of this paper are: (1) We present a set of important BERT design choices and training strategies and introduce alternatives that lead to better downstream task performance; (2) We use a novel dataset, CC-NEWS, and confirm that using more data for pretraining further improves performance on downstream tasks; (3) Our training improvements show that masked language model pretraining, under the right design choices, is competitive with all other recently published methods. We release our model, pretraining and fine-tuning code implemented in PyTorch (Paszke et al., 2017).

---

### النسخة العربية

حققت أساليب التدريب الذاتي مثل ELMo (Peters وآخرون، 2018)، وGPT (Radford وآخرون، 2018)، وBERT (Devlin وآخرون، 2019)، وXLM (Lample وConneau، 2019)، وXLNet (Yang وآخرون، 2019) مكاسب كبيرة في الأداء، لكن قد يكون من الصعب تحديد أي جوانب هذه الأساليب تساهم بشكل أكبر. التدريب مكلف من الناحية الحسابية، مما يحد من مقدار الضبط الذي يمكن إجراؤه، وغالباً ما يتم باستخدام بيانات تدريب خاصة بأحجام متفاوتة، مما يحد من قدرتنا على قياس تأثير التحسينات في النمذجة.

نقدم دراسة تكرار للتدريب المسبق لـ BERT (Devlin وآخرون، 2019)، والتي تتضمن تقييماً دقيقاً لتأثيرات ضبط المعاملات الفائقة وحجم مجموعة التدريب. نجد أن BERT كان يعاني من نقص كبير في التدريب ونقترح وصفة محسّنة لتدريب نماذج BERT، نسميها RoBERTa، يمكنها مطابقة أو تجاوز أداء جميع الأساليب التي جاءت بعد BERT. تعديلاتنا بسيطة، وتشمل: (1) تدريب النموذج لفترة أطول، بدفعات أكبر، على المزيد من البيانات؛ (2) إزالة هدف التنبؤ بالجملة التالية؛ (3) التدريب على تسلسلات أطول؛ و(4) تغيير نمط الإخفاء المطبق على بيانات التدريب بشكل ديناميكي. نجمع أيضاً مجموعة بيانات جديدة كبيرة (CC-NEWS) بحجم مماثل لمجموعات البيانات الخاصة الأخرى المستخدمة، لتحسين التحكم في تأثيرات حجم مجموعة التدريب.

عند التحكم في بيانات التدريب، تتحسن إجراءات التدريب المحسّنة لدينا على نتائج BERT المنشورة في كل من GLUE وSQuAD. عندما يتم التدريب لفترة أطول على بيانات إضافية، يحقق نموذجنا درجة 88.5 على لوحة صدارة GLUE العامة، مطابقاً الـ 88.4 المبلغ عنها من قبل Yang وآخرون (2019). يضع نموذجنا حالة جديدة من الأحدث والأفضل على 4/9 من مهام GLUE: MNLI وQNLI وRTE وSTS-B. نطابق أيضاً نتائج الأحدث والأفضل على SQuAD وRACE. بشكل عام، نعيد التأكيد على أن هدف التدريب بنموذج اللغة المقنع لـ BERT تنافسي مع أهداف التدريب الأخرى المقترحة مؤخراً مثل نمذجة اللغة الانحدارية التلقائية المضطربة (Yang وآخرون، 2019).

باختصار، مساهمات هذه الورقة هي: (1) نقدم مجموعة من خيارات التصميم واستراتيجيات التدريب المهمة لـ BERT ونقدم بدائل تؤدي إلى أداء أفضل في المهام النهائية؛ (2) نستخدم مجموعة بيانات جديدة، CC-NEWS، ونؤكد أن استخدام المزيد من البيانات للتدريب المسبق يحسّن الأداء بشكل أكبر على المهام النهائية؛ (3) تُظهر تحسينات التدريب لدينا أن التدريب المسبق بنموذج اللغة المقنع، في ظل خيارات التصميم الصحيحة، تنافسي مع جميع الأساليب الأخرى المنشورة مؤخراً. نصدر نموذجنا وكود التدريب المسبق والضبط الدقيق المنفذ في PyTorch (Paszke وآخرون، 2017).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** RoBERTa, CC-NEWS dataset, dynamic masking, perturbed autoregressive language modeling
- **Equations:** None
- **Citations:** 9 citations (ELMo, GPT, BERT, XLM, XLNet, Yang et al. 2019, Paszke et al. 2017)
- **Special handling:**
  - Model names (ELMo, GPT, BERT, XLM, XLNet) kept in English as they are proper names
  - Benchmark names (GLUE, SQuAD, RACE) kept in English
  - Dataset name (CC-NEWS) kept in English
  - GLUE task acronyms (MNLI, QNLI, RTE, STS-B) kept in English
  - PyTorch kept in English as a framework name

### Quality Metrics

- Semantic equivalence: 0.89 - All key claims and findings accurately translated
- Technical accuracy: 0.88 - All technical terms and model names properly handled
- Readability: 0.87 - Natural Arabic flow while maintaining technical precision
- Glossary consistency: 0.88 - Consistent use of established terms
- **Overall section score:** 0.88
