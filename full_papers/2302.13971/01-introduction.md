# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** large language model, training, parameter, token, inference, compute budget, few-shot, transformer, benchmark, publicly available, dataset, GPU

---

### English Version

Large Languages Models (LLMs) trained on massive corpora of texts have shown their ability to perform new tasks from textual instructions or from a few examples (Brown et al., 2020). These few-shot properties first appeared when scaling models to a sufficient size (Kaplan et al., 2020), resulting in a line of work that focuses on further scaling these models (Chowdhery et al., 2022; Rae et al., 2021).

These efforts are based on the assumption that more parameters will lead to better performance. However, recent work from Hoffmann et al. (2022) shows that, for a given compute budget, the best performances are not achieved by the largest models, but by smaller models trained on more data.

The objective of the scaling laws from Hoffmann et al. (2022) is to determine how to best scale the dataset and model sizes for a particular training compute budget. However, this objective disregards the inference budget, which becomes critical when serving a language model at scale. In this context, given a target level of performance, the preferred model is not the fastest to train but the fastest at inference, and although it may be cheaper to train a large model to reach a certain level of performance, a smaller one trained longer will ultimately be cheaper at inference. For instance, although Hoffmann et al. (2022) recommends training a 10B model on 200B tokens, we find that the performance of a 7B model continues to improve even after 1T tokens.

The focus of this work is to train a series of language models that achieve the best possible performance at various inference budgets, by training on more tokens than what is typically used. The resulting models, called LLaMA, ranges from 7B to 65B parameters with competitive performance compared to the best existing LLMs. For instance, LLaMA-13B outperforms GPT-3 on most benchmarks, despite being 10× smaller. We believe that this model will help democratize the access and study of LLMs, since it can be run on a single GPU. At the higher-end of the scale, our 65B-parameter model is also competitive with the best large language models such as Chinchilla or PaLM-540B.

Unlike Chinchilla, PaLM, or GPT-3, we only use publicly available data, making our work compatible with open-sourcing, while most existing models rely on data which is either not publicly available or undocumented (e.g. "Books – 2TB" or "Social media conversations"). There exist some exceptions, notably OPT (Zhang et al., 2022), GPT-NeoX (Black et al., 2022), BLOOM (Scao et al., 2022) and GLM (Zeng et al., 2022), but none that are competitive with PaLM-62B or Chinchilla.

In the rest of this paper, we present an overview of the modifications we made to the transformer architecture (Vaswani et al., 2017), as well as our training method. We then report the performance of our models and compare with others LLMs on a set of standard benchmarks. Finally, we expose some of the biases and toxicity encoded in our models, using some of the most recent benchmarks from the responsible AI community.

---

### النسخة العربية

أظهرت نماذج اللغة الكبيرة (LLMs) المُدربة على مجموعات نصية ضخمة قدرتها على أداء مهام جديدة من تعليمات نصية أو من أمثلة قليلة (Brown et al., 2020). ظهرت هذه الخصائص القائمة على الأمثلة القليلة لأول مرة عند توسيع حجم النماذج إلى حجم كافٍ (Kaplan et al., 2020)، مما أدى إلى سلسلة من الأعمال التي تركز على زيادة توسيع هذه النماذج (Chowdhery et al., 2022; Rae et al., 2021).

تستند هذه الجهود إلى الافتراض بأن المزيد من المعاملات سيؤدي إلى أداء أفضل. ومع ذلك، يُظهر العمل الحديث من Hoffmann et al. (2022) أنه بالنسبة لميزانية حسابية معينة، لا يتم تحقيق أفضل أداء من خلال أكبر النماذج، بل من خلال نماذج أصغر مُدربة على بيانات أكثر.

الهدف من قوانين التوسيع من Hoffmann et al. (2022) هو تحديد أفضل طريقة لتوسيع أحجام مجموعات البيانات والنماذج لميزانية حسابية محددة للتدريب. ومع ذلك، يتجاهل هذا الهدف ميزانية الاستنتاج، التي تصبح حاسمة عند تقديم نموذج لغة على نطاق واسع. في هذا السياق، بالنظر إلى مستوى أداء مستهدف، فإن النموذج المفضل ليس الأسرع في التدريب بل الأسرع في الاستنتاج، وعلى الرغم من أنه قد يكون أرخص تدريب نموذج كبير للوصول إلى مستوى معين من الأداء، إلا أن نموذجاً أصغر مُدرباً لفترة أطول سيكون في النهاية أرخص في الاستنتاج. على سبيل المثال، على الرغم من أن Hoffmann et al. (2022) يوصي بتدريب نموذج 10B على 200B رمز، نجد أن أداء نموذج 7B يستمر في التحسن حتى بعد 1T رمز.

ينصب تركيز هذا العمل على تدريب سلسلة من نماذج اللغة التي تحقق أفضل أداء ممكن عند ميزانيات استنتاج مختلفة، من خلال التدريب على رموز أكثر مما يُستخدم عادةً. النماذج الناتجة، المسماة LLaMA، تتراوح من 7B إلى 65B معامل مع أداء تنافسي مقارنةً بأفضل نماذج اللغة الكبيرة الموجودة. على سبيل المثال، يتفوق LLaMA-13B على GPT-3 في معظم المعايير، على الرغم من أنه أصغر بعشر مرات. نعتقد أن هذا النموذج سيساعد في إضفاء الطابع الديمقراطي على الوصول إلى نماذج اللغة الكبيرة ودراستها، حيث يمكن تشغيله على وحدة معالجة رسومية واحدة. على الطرف الأعلى من النطاق، نموذجنا ذو الـ 65B معامل منافس أيضاً لأفضل نماذج اللغة الكبيرة مثل Chinchilla أو PaLM-540B.

على عكس Chinchilla أو PaLM أو GPT-3، نستخدم فقط بيانات متاحة للعموم، مما يجعل عملنا متوافقاً مع المصادر المفتوحة، بينما تعتمد معظم النماذج الموجودة على بيانات إما غير متاحة للعموم أو غير موثقة (مثل "Books – 2TB" أو "محادثات وسائل التواصل الاجتماعي"). توجد بعض الاستثناءات، لا سيما OPT (Zhang et al., 2022)، وGPT-NeoX (Black et al., 2022)، وBLOOM (Scao et al., 2022)، وGLM (Zeng et al., 2022)، ولكن لا يوجد نموذج منها منافس لـ PaLM-62B أو Chinchilla.

في بقية هذه الورقة، نقدم نظرة عامة على التعديلات التي أجريناها على معمارية المحول (Vaswani et al., 2017)، بالإضافة إلى طريقة التدريب الخاصة بنا. ثم نُبلغ عن أداء نماذجنا ونقارنها مع نماذج اللغة الكبيرة الأخرى على مجموعة من المعايير القياسية. أخيراً، نكشف عن بعض التحيزات والسمية المشفرة في نماذجنا، باستخدام بعض أحدث المعايير من مجتمع الذكاء الاصطناعي المسؤول.

---

### Translation Notes

- **Figures referenced:** Figure 1 (training loss curves)
- **Key terms introduced:** few-shot learning, scaling laws, inference budget, compute budget
- **Citations:** 12+ references to prior work (Brown et al. 2020, Kaplan et al. 2020, Hoffmann et al. 2022, etc.)
- **Special handling:**
  - Model sizes kept in English notation (7B, 10B, 65B, 175B)
  - Token counts kept in scientific notation (200B, 1T)
  - Proper nouns (Chinchilla, PaLM, GPT-3, OPT, BLOOM, GLM) kept in original form

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
