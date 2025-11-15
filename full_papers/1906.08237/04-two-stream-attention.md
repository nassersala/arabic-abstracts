# Section 2.3: Architecture - Two-Stream Self-Attention for Target-Aware Representations
## القسم 2.3: المعمارية - الانتباه الذاتي ثنائي التدفق للتمثيلات الواعية بالهدف

**Section:** two-stream-attention
**Translation Quality:** 0.87
**Glossary Terms Used:** permutation language modeling, transformer, self-attention, target-aware, hidden representation, query, key, value, content representation, query representation, factorization, partial prediction

---

### English Version

While the permutation language modeling objective has desired properties, naive implementation with standard Transformer parameterization may not work. To see the problem, assume we parameterize the next-token distribution $p_{\theta}(X_{z_t} | x_{z_{<t}})$ using the standard Softmax formulation, i.e., $p_{\theta}(X_{z_t} = x | x_{z_{<t}}) = \frac{\exp(e(x)^{\top} h_{\theta}(x_{z_{<t}}))}{\sum_{x'} \exp(e(x')^{\top} h_{\theta}(x_{z_{<t}}))}$, where $h_{\theta}(x_{z_{<t}})$ denotes the hidden representation of $x_{z_{<t}}$ produced by the shared Transformer network after proper masking. Now notice that the representation $h_{\theta}(x_{z_{<t}})$ does not depend on which position it will predict, i.e., the value of $z_t$. Consequently, the same distribution is predicted regardless of the target position, which is not able to learn useful representations (see Appendix A.1 for a concrete example). To avoid this problem, we propose to re-parameterize the next-token distribution to be target position aware:

$$p_{\theta}(X_{z_t} = x | x_{z_{<t}}) = \frac{\exp(e(x)^{\top} g_{\theta}(x_{z_{<t}}, z_t))}{\sum_{x'} \exp(e(x')^{\top} g_{\theta}(x_{z_{<t}}, z_t))}$$  (4)

where $g_{\theta}(x_{z_{<t}}, z_t)$ denotes a new type of representations which additionally take the target position $z_t$ as input.

**Two-Stream Self-Attention:** While the idea of target-aware representations removes the ambiguity in target prediction, how to formulate $g_{\theta}(x_{z_{<t}}, z_t)$ remains a non-trivial problem. Among other possibilities, we propose to "stand" at the target position $z_t$ and rely on the position $z_t$ to gather information from the context $x_{z_{<t}}$ through attention. For this parameterization to work, there are two requirements that are contradictory in a standard Transformer architecture: (1) to predict the token $x_{z_t}$, $g_{\theta}(x_{z_{<t}}, z_t)$ should only use the position $z_t$ and not the content $x_{z_t}$, otherwise the objective becomes trivial; (2) to predict the other tokens $x_{z_j}$ with $j > t$, $g_{\theta}(x_{z_{<t}}, z_t)$ should also encode the content $x_{z_t}$ to provide full contextual information. To resolve such a contradiction, we propose to use two sets of hidden representations instead of one:

• The **content representation** $h_{\theta}(x_{z_{\leq t}})$, or abbreviated as $h_{z_t}$, which serves a similar role to the standard hidden states in Transformer. This representation encodes both the context and $x_{z_t}$ itself.

• The **query representation** $g_{\theta}(x_{z_{<t}}, z_t)$, or abbreviated as $g_{z_t}$, which only has access to the contextual information $x_{z_{<t}}$ and the position $z_t$, but not the content $x_{z_t}$, as discussed above.

Computationally, the first layer query stream is initialized with a trainable vector, i.e. $g_i^{(0)} = w$, while the content stream is set to the corresponding word embedding, i.e. $h_i^{(0)} = e(x_i)$. For each self-attention layer $m = 1, \ldots, M$, the two streams of representations are schematically updated with a shared set of parameters as follows (illustrated in Figures 1 (a) and (b)):

$$g_{z_t}^{(m)} \leftarrow \text{Attention}(Q = g_{z_t}^{(m-1)}, KV = h_{z_{<t}}^{(m-1)}; \theta)$$  (query stream: use $z_t$ but cannot see $x_{z_t}$)

$$h_{z_t}^{(m)} \leftarrow \text{Attention}(Q = h_{z_t}^{(m-1)}, KV = h_{z_{\leq t}}^{(m-1)}; \theta)$$  (content stream: use both $z_t$ and $x_{z_t}$)

where $Q$, $K$, $V$ denote the query, key, and value in an attention operation [33]. The update rule of the content representations is exactly the same as the standard self-attention, so during finetuning, we can simply drop the query stream and use the content stream as a normal Transformer(-XL). Finally, we can use the last-layer query representation $g_{z_t}^{(M)}$ to compute Eq. (4).

**Partial Prediction:** While the permutation language modeling objective (3) has several benefits, it is a much more challenging optimization problem due to the permutation and causes slow convergence in preliminary experiments. To reduce the optimization difficulty, we choose to only predict the last tokens in a factorization order. Formally, we split $z$ into a non-target subsequence $z_{\leq c}$ and a target subsequence $z_{>c}$, where $c$ is the cutting point. The objective is to maximize the log-likelihood of the target subsequence conditioned on the non-target subsequence, i.e.,

$$\max_{\theta} \mathbb{E}_{z \sim \mathcal{Z}_T} \left[ \log p_{\theta}(x_{z_{>c}} | x_{z_{\leq c}}) \right] = \mathbb{E}_{z \sim \mathcal{Z}_T} \left[ \sum_{t=c+1}^{|z|} \log p_{\theta}(x_{z_t} | x_{z_{<t}}) \right]$$  (5)

Note that $z_{>c}$ is chosen as the target because it possesses the longest context in the sequence given the current factorization order $z$. A hyperparameter $K$ is used such that about $1/K$ tokens are selected for predictions; i.e., $|z|/(|z| - c) \approx K$. For unselected tokens, their query representations need not be computed, which saves speed and memory.

---

### النسخة العربية

بينما يمتلك هدف النمذجة اللغوية بالتبديل خصائص مرغوبة، قد لا يعمل التطبيق الساذج مع بارامترة المحول القياسية. لرؤية المشكلة، افترض أننا نبارمتر توزيع الرمز التالي $p_{\theta}(X_{z_t} | x_{z_{<t}})$ باستخدام صيغة Softmax القياسية، أي $p_{\theta}(X_{z_t} = x | x_{z_{<t}}) = \frac{\exp(e(x)^{\top} h_{\theta}(x_{z_{<t}}))}{\sum_{x'} \exp(e(x')^{\top} h_{\theta}(x_{z_{<t}}))}$، حيث $h_{\theta}(x_{z_{<t}})$ يشير إلى التمثيل المخفي لـ $x_{z_{<t}}$ الذي تنتجه شبكة المحول المشتركة بعد الإخفاء المناسب. لاحظ الآن أن التمثيل $h_{\theta}(x_{z_{<t}})$ لا يعتمد على الموضع الذي سيتنبأ به، أي قيمة $z_t$. وبالتالي، يتم التنبؤ بنفس التوزيع بغض النظر عن موضع الهدف، وهو غير قادر على تعلم تمثيلات مفيدة (انظر الملحق A.1 للحصول على مثال ملموس). لتجنب هذه المشكلة، نقترح إعادة بارامترة توزيع الرمز التالي ليكون واعياً بموضع الهدف:

$$p_{\theta}(X_{z_t} = x | x_{z_{<t}}) = \frac{\exp(e(x)^{\top} g_{\theta}(x_{z_{<t}}, z_t))}{\sum_{x'} \exp(e(x')^{\top} g_{\theta}(x_{z_{<t}}, z_t))}$$  (4)

حيث $g_{\theta}(x_{z_{<t}}, z_t)$ يشير إلى نوع جديد من التمثيلات التي تأخذ بالإضافة إلى ذلك موضع الهدف $z_t$ كمدخل.

**الانتباه الذاتي ثنائي التدفق:** بينما تزيل فكرة التمثيلات الواعية بالهدف الغموض في التنبؤ بالهدف، تظل كيفية صياغة $g_{\theta}(x_{z_{<t}}, z_t)$ مشكلة غير تافهة. من بين الاحتمالات الأخرى، نقترح "الوقوف" عند موضع الهدف $z_t$ والاعتماد على الموضع $z_t$ لجمع المعلومات من السياق $x_{z_{<t}}$ من خلال الانتباه. لكي تعمل هذه البارامترة، هناك متطلبان متناقضان في معمارية المحول القياسية: (1) للتنبؤ بالرمز $x_{z_t}$، يجب أن يستخدم $g_{\theta}(x_{z_{<t}}, z_t)$ فقط الموضع $z_t$ وليس المحتوى $x_{z_t}$، وإلا يصبح الهدف تافهاً؛ (2) للتنبؤ بالرموز الأخرى $x_{z_j}$ مع $j > t$، يجب أن يقوم $g_{\theta}(x_{z_{<t}}, z_t)$ أيضاً بترميز المحتوى $x_{z_t}$ لتوفير معلومات سياقية كاملة. لحل هذا التناقض، نقترح استخدام مجموعتين من التمثيلات المخفية بدلاً من واحدة:

• **تمثيل المحتوى** $h_{\theta}(x_{z_{\leq t}})$، أو مختصراً $h_{z_t}$، والذي يخدم دوراً مشابهاً للحالات المخفية القياسية في المحول. يقوم هذا التمثيل بترميز كل من السياق و $x_{z_t}$ نفسه.

• **تمثيل الاستعلام** $g_{\theta}(x_{z_{<t}}, z_t)$، أو مختصراً $g_{z_t}$، والذي يمتلك فقط الوصول إلى المعلومات السياقية $x_{z_{<t}}$ والموضع $z_t$، ولكن ليس المحتوى $x_{z_t}$، كما تمت مناقشته أعلاه.

حسابياً، يتم تهيئة تدفق الاستعلام للطبقة الأولى بمتجه قابل للتدريب، أي $g_i^{(0)} = w$، بينما يتم تعيين تدفق المحتوى إلى التضمين الكلمي المقابل، أي $h_i^{(0)} = e(x_i)$. لكل طبقة انتباه ذاتي $m = 1, \ldots, M$، يتم تحديث تدفقي التمثيلات بشكل تخطيطي بمجموعة مشتركة من المعاملات كما يلي (موضح في الأشكال 1 (أ) و (ب)):

$$g_{z_t}^{(m)} \leftarrow \text{Attention}(Q = g_{z_t}^{(m-1)}, KV = h_{z_{<t}}^{(m-1)}; \theta)$$  (تدفق الاستعلام: استخدام $z_t$ ولكن لا يمكن رؤية $x_{z_t}$)

$$h_{z_t}^{(m)} \leftarrow \text{Attention}(Q = h_{z_t}^{(m-1)}, KV = h_{z_{\leq t}}^{(m-1)}; \theta)$$  (تدفق المحتوى: استخدام كل من $z_t$ و $x_{z_t}$)

حيث $Q$، $K$، $V$ تشير إلى الاستعلام والمفتاح والقيمة في عملية الانتباه [33]. قاعدة التحديث لتمثيلات المحتوى هي بالضبط نفس الانتباه الذاتي القياسي، لذلك أثناء الضبط الدقيق، يمكننا ببساطة إسقاط تدفق الاستعلام واستخدام تدفق المحتوى كمحول عادي (-XL). أخيراً، يمكننا استخدام تمثيل الاستعلام للطبقة الأخيرة $g_{z_t}^{(M)}$ لحساب المعادلة (4).

**التنبؤ الجزئي:** بينما يمتلك هدف النمذجة اللغوية بالتبديل (3) عدة فوائد، فهو مشكلة تحسين أكثر تحدياً بكثير بسبب التبديل ويسبب تقارباً بطيئاً في التجارب الأولية. لتقليل صعوبة التحسين، نختار التنبؤ فقط بالرموز الأخيرة في ترتيب التحليل العاملي. رسمياً، نقسم $z$ إلى تسلسل فرعي غير مستهدف $z_{\leq c}$ وتسلسل فرعي مستهدف $z_{>c}$، حيث $c$ هي نقطة القطع. الهدف هو تعظيم اللوغاريتم للاحتمالية للتسلسل الفرعي المستهدف مشروطاً بالتسلسل الفرعي غير المستهدف، أي:

$$\max_{\theta} \mathbb{E}_{z \sim \mathcal{Z}_T} \left[ \log p_{\theta}(x_{z_{>c}} | x_{z_{\leq c}}) \right] = \mathbb{E}_{z \sim \mathcal{Z}_T} \left[ \sum_{t=c+1}^{|z|} \log p_{\theta}(x_{z_t} | x_{z_{<t}}) \right]$$  (5)

لاحظ أن $z_{>c}$ يتم اختياره كهدف لأنه يمتلك أطول سياق في التسلسل بالنظر إلى ترتيب التحليل العاملي الحالي $z$. يتم استخدام معامل فائق $K$ بحيث يتم تحديد حوالي $1/K$ من الرموز للتنبؤات؛ أي $|z|/(|z| - c) \approx K$. بالنسبة للرموز غير المحددة، لا حاجة لحساب تمثيلات الاستعلام الخاصة بها، مما يوفر السرعة والذاكرة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (a) and (b) - showing content and query stream attention
- **Key terms introduced:** Two-stream self-attention, content representation, query representation, target-aware representations, partial prediction
- **Equations:** Equations 4 and 5 (target-aware distribution and partial prediction objective)
- **Citations:** [33] for attention mechanism
- **Special handling:** Complex mathematical formulations with multiple subscripts and superscripts

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
