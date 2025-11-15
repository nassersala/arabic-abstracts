# Section 2.2: Objective - Permutation Language Modeling
## القسم 2.2: الهدف - النمذجة اللغوية بالتبديل

**Section:** permutation-language-modeling
**Translation Quality:** 0.86
**Glossary Terms Used:** autoregressive, BERT, factorization, permutation, bidirectional context, independence assumption, pretrain-finetune discrepancy, likelihood, expectation

---

### English Version

According to the comparison above, AR language modeling and BERT possess their unique advantages over the other. A natural question to ask is whether there exists a pretraining objective that brings the advantages of both while avoiding their weaknesses.

Borrowing ideas from orderless NADE [32], we propose the permutation language modeling objective that not only retains the benefits of AR models but also allows models to capture bidirectional contexts. Specifically, for a sequence $x$ of length $T$, there are $T!$ different orders to perform a valid autoregressive factorization. Intuitively, if model parameters are shared across all factorization orders, in expectation, the model will learn to gather information from all positions on both sides.

To formalize the idea, let $\mathcal{Z}_T$ be the set of all possible permutations of the length-$T$ index sequence $[1, 2, \ldots, T]$. We use $z_t$ and $z_{<t}$ to denote the $t$-th element and the first $t-1$ elements of a permutation $z \in \mathcal{Z}_T$. Then, our proposed permutation language modeling objective can be expressed as follows:

$$\max_{\theta} \mathbb{E}_{z \sim \mathcal{Z}_T} \left[ \sum_{t=1}^{T} \log p_{\theta}(x_{z_t} | x_{z_{<t}}) \right]$$  (3)

Essentially, for a text sequence $x$, we sample a factorization order $z$ at a time and decompose the likelihood $p_{\theta}(x)$ according to factorization order. Since the same model parameter $\theta$ is shared across all factorization orders during training, in expectation, $x_t$ has seen every possible element $x_i \neq x_t$ in the sequence, hence being able to capture the bidirectional context. Moreover, as this objective fits into the AR framework, it naturally avoids the independence assumption and the pretrain-finetune discrepancy discussed in Section 2.1.

**Remark on Permutation:** The proposed objective only permutes the factorization order, not the sequence order. In other words, we keep the original sequence order, use the positional encodings corresponding to the original sequence, and rely on a proper attention mask in Transformers to achieve permutation of the factorization order. Note that this choice is necessary, since the model will only encounter text sequences with the natural order during finetuning.

To provide an overall picture, we show an example of predicting the token $x_3$ given the same input sequence $x$ but under different factorization orders in the Appendix A.7 with Figure 4.

---

### النسخة العربية

وفقاً للمقارنة أعلاه، تمتلك النمذجة اللغوية الانحدارية الذاتية و BERT مزاياهما الفريدة على الآخر. السؤال الطبيعي الذي يجب طرحه هو ما إذا كان هناك هدف تدريب مسبق يجمع مزايا كليهما مع تجنب نقاط ضعفهما.

باستعارة أفكار من NADE عديم الترتيب [32]، نقترح هدف النمذجة اللغوية بالتبديل الذي لا يحتفظ فقط بفوائد نماذج الانحدار الذاتي ولكن يسمح أيضاً للنماذج بالتقاط السياقات ثنائية الاتجاه. على وجه التحديد، بالنسبة لتسلسل $x$ بطول $T$، هناك $T!$ ترتيباً مختلفاً لإجراء تحليل عاملي انحداري ذاتي صالح. بشكل بديهي، إذا تم مشاركة معاملات النموذج عبر جميع ترتيبات التحليل العاملي، فإنه في التوقع، سيتعلم النموذج جمع المعلومات من جميع المواضع على كلا الجانبين.

لإضفاء الطابع الرسمي على الفكرة، دع $\mathcal{Z}_T$ تكون مجموعة جميع التبديلات الممكنة لتسلسل الفهرس بطول $T$ وهو $[1, 2, \ldots, T]$. نستخدم $z_t$ و $z_{<t}$ للإشارة إلى العنصر $t$ والعناصر $t-1$ الأولى من تبديل $z \in \mathcal{Z}_T$. يمكن التعبير عن هدف النمذجة اللغوية بالتبديل المقترح على النحو التالي:

$$\max_{\theta} \mathbb{E}_{z \sim \mathcal{Z}_T} \left[ \sum_{t=1}^{T} \log p_{\theta}(x_{z_t} | x_{z_{<t}}) \right]$$  (3)

في الأساس، بالنسبة لتسلسل نصي $x$، نقوم بأخذ عينة من ترتيب التحليل العاملي $z$ في كل مرة ونحلل الاحتمالية $p_{\theta}(x)$ وفقاً لترتيب التحليل العاملي. نظراً لأن معامل النموذج نفسه $\theta$ يتم مشاركته عبر جميع ترتيبات التحليل العاملي أثناء التدريب، فإنه في التوقع، يكون $x_t$ قد رأى كل عنصر ممكن $x_i \neq x_t$ في التسلسل، وبالتالي يكون قادراً على التقاط السياق ثنائي الاتجاه. علاوة على ذلك، نظراً لأن هذا الهدف يتناسب مع إطار الانحدار الذاتي، فإنه يتجنب بشكل طبيعي افتراض الاستقلال والتباين بين التدريب المسبق والضبط الدقيق الذي تمت مناقشته في القسم 2.1.

**ملاحظة حول التبديل:** الهدف المقترح يبدل فقط ترتيب التحليل العاملي، وليس ترتيب التسلسل. بعبارة أخرى، نحافظ على ترتيب التسلسل الأصلي، ونستخدم الترميزات الموضعية المقابلة للتسلسل الأصلي، ونعتمد على قناع انتباه مناسب في المحولات لتحقيق تبديل ترتيب التحليل العاملي. لاحظ أن هذا الاختيار ضروري، حيث سيواجه النموذج فقط تسلسلات نصية بالترتيب الطبيعي أثناء الضبط الدقيق.

لتوفير صورة شاملة، نعرض مثالاً على التنبؤ بالرمز $x_3$ بالنظر إلى نفس تسلسل المدخلات $x$ ولكن في ظل ترتيبات تحليل عاملي مختلفة في الملحق A.7 مع الشكل 4.

---

### Translation Notes

- **Figures referenced:** Figure 4 (in Appendix A.7)
- **Key terms introduced:** Permutation language modeling, factorization order, orderless NADE, expectation over permutations
- **Equations:** Equation 3 (main permutation LM objective)
- **Citations:** [32] for orderless NADE
- **Special handling:** Mathematical notation for permutations and expectations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
