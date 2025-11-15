# Section 3: ELMo: Embeddings from Language Models
## القسم 3: ELMo: التضمينات من النماذج اللغوية

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** embedding, language model, bidirectional, LSTM, character convolution, semi-supervised learning, pre-training, token, CNN, forward pass, backward pass, softmax, layer normalization, dropout, residual connection, highway networks, perplexity, fine-tuning, domain transfer

---

### English Version

Unlike most widely used word embeddings (Pennington et al., 2014), ELMo word representations are functions of the entire input sentence, as described in this section. They are computed on top of two-layer biLMs with character convolutions (Sec. 3.1), as a linear function of the internal network states (Sec. 3.2). This setup allows us to do semi-supervised learning, where the biLM is pre-trained at a large scale (Sec. 3.4) and easily incorporated into a wide range of existing neural NLP architectures (Sec. 3.3).

**3.1 Bidirectional language models**

Given a sequence of N tokens, $(t_1, t_2, ..., t_N)$, a forward language model computes the probability of the sequence by modeling the probability of token $t_k$ given the history $(t_1, ..., t_{k-1})$:

$$p(t_1, t_2, ..., t_N) = \prod_{k=1}^{N} p(t_k | t_1, t_2, ..., t_{k-1})$$

Recent state-of-the-art neural language models (Józefowicz et al., 2016; Melis et al., 2017; Merity et al., 2017) compute a context-independent token representation $x_k^{LM}$ (via token embeddings or a CNN over characters) then pass it through L layers of forward LSTMs. At each position k, each LSTM layer outputs a context-dependent representation $\vec{h}_{k,j}^{LM}$ where $j = 1, ..., L$. The top layer LSTM output, $\vec{h}_{k,L}^{LM}$, is used to predict the next token $t_{k+1}$ with a Softmax layer.

A backward LM is similar to a forward LM, except it runs over the sequence in reverse, predicting the previous token given the future context:

$$p(t_1, t_2, ..., t_N) = \prod_{k=1}^{N} p(t_k | t_{k+1}, t_{k+2}, ..., t_N)$$

It can be implemented in an analogous way to a forward LM, with each backward LSTM layer j in a L layer deep model producing representations $\overleftarrow{h}_{k,j}^{LM}$ of $t_k$ given $(t_{k+1}, ..., t_N)$.

A biLM combines both a forward and backward LM. Our formulation jointly maximizes the log likelihood of the forward and backward directions:

$$\sum_{k=1}^{N} (\log p(t_k | t_1, ..., t_{k-1}; \Theta_x, \vec{\Theta}_{LSTM}, \Theta_s) + \log p(t_k | t_{k+1}, ..., t_N; \Theta_x, \overleftarrow{\Theta}_{LSTM}, \Theta_s))$$

We tie the parameters for both the token representation ($\Theta_x$) and Softmax layer ($\Theta_s$) in the forward and backward direction while maintaining separate parameters for the LSTMs in each direction. Overall, this formulation is similar to the approach of Peters et al. (2017), with the exception that we share some weights between directions instead of using completely independent parameters. In the next section, we depart from previous work by introducing a new approach for learning word representations that are a linear combination of the biLM layers.

**3.2 ELMo**

ELMo is a task specific combination of the intermediate layer representations in the biLM. For each token $t_k$, a L-layer biLM computes a set of $2L + 1$ representations:

$$R_k = \{x_k^{LM}, \vec{h}_{k,j}^{LM}, \overleftarrow{h}_{k,j}^{LM} | j = 1, ..., L\} = \{h_{k,j}^{LM} | j = 0, ..., L\}$$

where $h_{k,0}^{LM}$ is the token layer and $h_{k,j}^{LM} = [\vec{h}_{k,j}^{LM}; \overleftarrow{h}_{k,j}^{LM}]$, for each biLSTM layer.

For inclusion in a downstream model, ELMo collapses all layers in R into a single vector, $\text{ELMo}_k = E(R_k; \Theta_e)$. In the simplest case, ELMo just selects the top layer, $E(R_k) = h_{k,L}^{LM}$, as in TagLM (Peters et al., 2017) and CoVe (McCann et al., 2017). More generally, we compute a task specific weighting of all biLM layers:

$$\text{ELMo}_k^{task} = E(R_k; \Theta^{task}) = \gamma^{task} \sum_{j=0}^{L} s_j^{task} h_{k,j}^{LM}$$  (1)

In (1), $s^{task}$ are softmax-normalized weights and the scalar parameter $\gamma^{task}$ allows the task model to scale the entire ELMo vector. $\gamma$ is of practical importance to aid the optimization process (see supplemental material for details). Considering that the activations of each biLM layer have a different distribution, in some cases it also helped to apply layer normalization (Ba et al., 2016) to each biLM layer before weighting.

**3.3 Using biLMs for supervised NLP tasks**

Given a pre-trained biLM and a supervised architecture for a target NLP task, it is a simple process to use the biLM to improve the task model. We simply run the biLM and record all of the layer representations for each word. Then, we let the end task model learn a linear combination of these representations, as described below.

First consider the lowest layers of the supervised model without the biLM. Most supervised NLP models share a common architecture at the lowest layers, allowing us to add ELMo in a consistent, unified manner. Given a sequence of tokens $(t_1, ..., t_N)$, it is standard to form a context-independent token representation $x_k$ for each token position using pre-trained word embeddings and optionally character-based representations. Then, the model forms a context-sensitive representation $h_k$, typically using either bidirectional RNNs, CNNs, or feed forward networks.

To add ELMo to the supervised model, we first freeze the weights of the biLM and then concatenate the ELMo vector $\text{ELMo}_k^{task}$ with $x_k$ and pass the ELMo enhanced representation $[x_k; \text{ELMo}_k^{task}]$ into the task RNN. For some tasks (e.g., SNLI, SQuAD), we observe further improvements by also including ELMo at the output of the task RNN by introducing another set of output specific linear weights and replacing $h_k$ with $[h_k; \text{ELMo}_k^{task}]$. As the remainder of the supervised model remains unchanged, these additions can happen within the context of more complex neural models. For example, see the SNLI experiments in Sec. 4 where a bi-attention layer follows the biLSTMs, or the coreference resolution experiments where a clustering model is layered on top of the biLSTMs.

Finally, we found it beneficial to add a moderate amount of dropout to ELMo (Srivastava et al., 2014) and in some cases to regularize the ELMo weights by adding $\lambda||w||_2^2$ to the loss. This imposes an inductive bias on the ELMo weights to stay close to an average of all biLM layers.

**3.4 Pre-trained bidirectional language model architecture**

The pre-trained biLMs in this paper are similar to the architectures in Józefowicz et al. (2016) and Kim et al. (2015), but modified to support joint training of both directions and add a residual connection between LSTM layers. We focus on large scale biLMs in this work, as Peters et al. (2017) highlighted the importance of using biLMs over forward-only LMs and large scale training.

To balance overall language model perplexity with model size and computational requirements for downstream tasks while maintaining a purely character-based input representation, we halved all embedding and hidden dimensions from the single best model CNN-BIG-LSTM in Józefowicz et al. (2016). The final model uses L = 2 biLSTM layers with 4096 units and 512 dimension projections and a residual connection from the first to second layer. The context insensitive type representation uses 2048 character n-gram convolutional filters followed by two highway layers (Srivastava et al., 2015) and a linear projection down to a 512 representation. As a result, the biLM provides three layers of representations for each input token, including those outside the training set due to the purely character input. In contrast, traditional word embedding methods only provide one layer of representation for tokens in a fixed vocabulary.

After training for 10 epochs on the 1B Word Benchmark (Chelba et al., 2014), the average forward and backward perplexities is 39.7, compared to 30.0 for the forward CNN-BIG-LSTM. Generally, we found the forward and backward perplexities to be approximately equal, with the backward value slightly lower.

Once pretrained, the biLM can compute representations for any task. In some cases, fine tuning the biLM on domain specific data leads to significant drops in perplexity and an increase in downstream task performance. This can be seen as a type of domain transfer for the biLM. As a result, in most cases we used a fine-tuned biLM in the downstream task. See supplemental material for details.

---

### النسخة العربية

على عكس معظم تضمينات الكلمات المستخدمة على نطاق واسع (Pennington et al., 2014)، فإن تمثيلات كلمات ELMo هي دوال للجملة الكاملة المُدخلة، كما هو موضح في هذا القسم. يتم حسابها فوق نماذج لغة ثنائية الاتجاه (biLMs) من طبقتين مع التفافات الأحرف (القسم 3.1)، كدالة خطية للحالات الداخلية للشبكة (القسم 3.2). يسمح لنا هذا الإعداد بالقيام بالتعلم شبه المُشرف، حيث يتم تدريب نموذج اللغة ثنائي الاتجاه (biLM) مسبقاً على نطاق واسع (القسم 3.4) ودمجه بسهولة في مجموعة واسعة من معماريات معالجة اللغة الطبيعية العصبية الموجودة (القسم 3.3).

**3.1 نماذج اللغة ثنائية الاتجاه**

بالنظر إلى تسلسل من N رمزاً، $(t_1, t_2, ..., t_N)$، يحسب نموذج اللغة الأمامي احتمال التسلسل عن طريق نمذجة احتمال الرمز $t_k$ بالنظر إلى التاريخ $(t_1, ..., t_{k-1})$:

$$p(t_1, t_2, ..., t_N) = \prod_{k=1}^{N} p(t_k | t_1, t_2, ..., t_{k-1})$$

نماذج اللغة العصبية الحديثة (Józefowicz et al., 2016; Melis et al., 2017; Merity et al., 2017) تحسب تمثيل رمز مستقل عن السياق $x_k^{LM}$ (عبر تضمينات الرموز أو CNN فوق الأحرف) ثم تمرره عبر L طبقات من LSTMs الأمامية. في كل موضع k، تُخرج كل طبقة LSTM تمثيلاً معتمداً على السياق $\vec{h}_{k,j}^{LM}$ حيث $j = 1, ..., L$. يُستخدم إخراج طبقة LSTM العليا، $\vec{h}_{k,L}^{LM}$، للتنبؤ بالرمز التالي $t_{k+1}$ بطبقة Softmax.

نموذج اللغة الخلفي مشابه لنموذج اللغة الأمامي، باستثناء أنه يعمل على التسلسل بالعكس، متنبئاً بالرمز السابق بالنظر إلى السياق المستقبلي:

$$p(t_1, t_2, ..., t_N) = \prod_{k=1}^{N} p(t_k | t_{k+1}, t_{k+2}, ..., t_N)$$

يمكن تنفيذه بطريقة مماثلة لنموذج اللغة الأمامي، حيث تُنتج كل طبقة LSTM خلفية j في نموذج عميق من L طبقات تمثيلات $\overleftarrow{h}_{k,j}^{LM}$ لـ $t_k$ بالنظر إلى $(t_{k+1}, ..., t_N)$.

نموذج اللغة ثنائي الاتجاه (biLM) يجمع بين نموذج اللغة الأمامي والخلفي. صياغتنا تعظم بشكل مشترك لوغاريتم الاحتمالية للاتجاهين الأمامي والخلفي:

$$\sum_{k=1}^{N} (\log p(t_k | t_1, ..., t_{k-1}; \Theta_x, \vec{\Theta}_{LSTM}, \Theta_s) + \log p(t_k | t_{k+1}, ..., t_N; \Theta_x, \overleftarrow{\Theta}_{LSTM}, \Theta_s))$$

نربط المعاملات لكل من تمثيل الرمز ($\Theta_x$) وطبقة Softmax ($\Theta_s$) في الاتجاهين الأمامي والخلفي مع الحفاظ على معاملات منفصلة لـ LSTMs في كل اتجاه. بشكل عام، هذه الصياغة مشابهة لنهج Peters et al. (2017)، باستثناء أننا نشارك بعض الأوزان بين الاتجاهات بدلاً من استخدام معاملات مستقلة تماماً. في القسم التالي، نبتعد عن الأعمال السابقة من خلال تقديم نهج جديد لتعلم تمثيلات الكلمات التي هي مزيج خطي من طبقات نموذج اللغة ثنائي الاتجاه.

**3.2 ELMo**

ELMo هو مزيج خاص بالمهمة من تمثيلات الطبقات الوسيطة في نموذج اللغة ثنائي الاتجاه. لكل رمز $t_k$، يحسب نموذج لغة ثنائي الاتجاه من L طبقات مجموعة من $2L + 1$ تمثيلاً:

$$R_k = \{x_k^{LM}, \vec{h}_{k,j}^{LM}, \overleftarrow{h}_{k,j}^{LM} | j = 1, ..., L\} = \{h_{k,j}^{LM} | j = 0, ..., L\}$$

حيث $h_{k,0}^{LM}$ هي طبقة الرمز و $h_{k,j}^{LM} = [\vec{h}_{k,j}^{LM}; \overleftarrow{h}_{k,j}^{LM}]$، لكل طبقة biLSTM.

للإدراج في نموذج نهائي، يطوي ELMo جميع الطبقات في R إلى متجه واحد، $\text{ELMo}_k = E(R_k; \Theta_e)$. في أبسط الحالات، يختار ELMo الطبقة العليا فقط، $E(R_k) = h_{k,L}^{LM}$، كما في TagLM (Peters et al., 2017) وCoVe (McCann et al., 2017). بشكل أكثر عمومية، نحسب ترجيحاً خاصاً بالمهمة لجميع طبقات نموذج اللغة ثنائي الاتجاه:

$$\text{ELMo}_k^{task} = E(R_k; \Theta^{task}) = \gamma^{task} \sum_{j=0}^{L} s_j^{task} h_{k,j}^{LM}$$  (1)

في المعادلة (1)، $s^{task}$ هي أوزان منظمة بواسطة softmax والمعامل القياسي $\gamma^{task}$ يسمح لنموذج المهمة بتحجيم متجه ELMo بأكمله. $\gamma$ ذو أهمية عملية للمساعدة في عملية التحسين (انظر المواد التكميلية للتفاصيل). بالنظر إلى أن تنشيطات كل طبقة من طبقات نموذج اللغة ثنائي الاتجاه لها توزيع مختلف، في بعض الحالات ساعد أيضاً تطبيق تطبيع الطبقة (Ba et al., 2016) على كل طبقة من طبقات نموذج اللغة ثنائي الاتجاه قبل الترجيح.

**3.3 استخدام نماذج اللغة ثنائية الاتجاه لمهام معالجة اللغة الطبيعية المُشرفة**

بالنظر إلى نموذج لغة ثنائي الاتجاه مُدرب مسبقاً ومعمارية مُشرفة لمهمة معالجة لغة طبيعية مستهدفة، فإن استخدام نموذج اللغة ثنائي الاتجاه لتحسين نموذج المهمة هو عملية بسيطة. نقوم ببساطة بتشغيل نموذج اللغة ثنائي الاتجاه وتسجيل جميع تمثيلات الطبقات لكل كلمة. ثم، نسمح لنموذج المهمة النهائية بتعلم مزيج خطي من هذه التمثيلات، كما هو موضح أدناه.

أولاً، فكر في الطبقات الأدنى من النموذج المُشرف بدون نموذج اللغة ثنائي الاتجاه. معظم نماذج معالجة اللغة الطبيعية المُشرفة تشترك في معمارية مشتركة في الطبقات الأدنى، مما يسمح لنا بإضافة ELMo بطريقة متسقة وموحدة. بالنظر إلى تسلسل من الرموز $(t_1, ..., t_N)$، من القياسي تشكيل تمثيل رمز مستقل عن السياق $x_k$ لكل موضع رمز باستخدام تضمينات الكلمات المدربة مسبقاً واختيارياً التمثيلات القائمة على الأحرف. ثم، يشكل النموذج تمثيلاً حساساً للسياق $h_k$، عادة باستخدام إما RNNs ثنائية الاتجاه، أو CNNs، أو شبكات التغذية الأمامية.

لإضافة ELMo إلى النموذج المُشرف، نُجمد أولاً أوزان نموذج اللغة ثنائي الاتجاه ثم نربط متجه ELMo $\text{ELMo}_k^{task}$ مع $x_k$ ونمرر التمثيل المحسن بـ ELMo $[x_k; \text{ELMo}_k^{task}]$ إلى RNN المهمة. بالنسبة لبعض المهام (مثل SNLI، SQuAD)، نلاحظ تحسينات إضافية من خلال تضمين ELMo أيضاً في إخراج RNN المهمة عن طريق إدخال مجموعة أخرى من الأوزان الخطية الخاصة بالإخراج واستبدال $h_k$ بـ $[h_k; \text{ELMo}_k^{task}]$. نظراً لأن بقية النموذج المُشرف يظل دون تغيير، يمكن أن تحدث هذه الإضافات في سياق نماذج عصبية أكثر تعقيداً. على سبيل المثال، راجع تجارب SNLI في القسم 4 حيث تتبع طبقة انتباه ثنائي (bi-attention) biLSTMs، أو تجارب حل الإحالة المرجعية حيث يتم وضع نموذج تجميع فوق biLSTMs.

أخيراً، وجدنا أنه من المفيد إضافة كمية معتدلة من dropout إلى ELMo (Srivastava et al., 2014) وفي بعض الحالات تنظيم أوزان ELMo بإضافة $\lambda||w||_2^2$ إلى الخسارة. يفرض هذا تحيزاً استقرائياً على أوزان ELMo للبقاء قريبة من متوسط جميع طبقات نموذج اللغة ثنائي الاتجاه.

**3.4 معمارية نموذج اللغة ثنائي الاتجاه المدرب مسبقاً**

نماذج اللغة ثنائية الاتجاه المدربة مسبقاً في هذا البحث مشابهة للمعماريات في Józefowicz et al. (2016) وKim et al. (2015)، لكنها معدلة لدعم التدريب المشترك لكلا الاتجاهين وإضافة اتصال متبقي بين طبقات LSTM. نركز على نماذج اللغة ثنائية الاتجاه واسعة النطاق في هذا العمل، حيث أبرز Peters et al. (2017) أهمية استخدام نماذج اللغة ثنائية الاتجاه على نماذج اللغة الأمامية فقط والتدريب واسع النطاق.

لموازنة حيرة نموذج اللغة الإجمالية مع حجم النموذج والمتطلبات الحسابية للمهام النهائية مع الحفاظ على تمثيل إدخال قائم على الأحرف بحتة، قللنا إلى النصف جميع أبعاد التضمين والأبعاد المخفية من نموذج واحد أفضل CNN-BIG-LSTM في Józefowicz et al. (2016). يستخدم النموذج النهائي L = 2 طبقات biLSTM مع 4096 وحدة وإسقاطات بُعد 512 واتصال متبقي من الطبقة الأولى إلى الثانية. يستخدم تمثيل النوع غير الحساس للسياق 2048 مرشح التفاف n-gram للأحرف متبوعاً بطبقتين من شبكات الطرق السريعة (Srivastava et al., 2015) وإسقاط خطي إلى تمثيل 512. نتيجة لذلك، يوفر نموذج اللغة ثنائي الاتجاه ثلاث طبقات من التمثيلات لكل رمز إدخال، بما في ذلك تلك خارج مجموعة التدريب بسبب إدخال الأحرف البحت. في المقابل، توفر طرق تضمين الكلمات التقليدية طبقة واحدة فقط من التمثيل للرموز في مفردات ثابتة.

بعد التدريب لـ 10 حقب على معيار 1B Word (Chelba et al., 2014)، متوسط الحيرة الأمامية والخلفية هو 39.7، مقارنة بـ 30.0 لـ CNN-BIG-LSTM الأمامي. بشكل عام، وجدنا أن الحيرة الأمامية والخلفية متساوية تقريباً، مع انخفاض طفيف في القيمة الخلفية.

بمجرد التدريب المسبق، يمكن لنموذج اللغة ثنائي الاتجاه حساب التمثيلات لأي مهمة. في بعض الحالات، يؤدي الضبط الدقيق لنموذج اللغة ثنائي الاتجاه على بيانات خاصة بالمجال إلى انخفاضات كبيرة في الحيرة وزيادة في أداء المهمة النهائية. يمكن اعتبار هذا نوعاً من نقل المجال لنموذج اللغة ثنائي الاتجاه. نتيجة لذلك، في معظم الحالات استخدمنا نموذج لغة ثنائي الاتجاه مضبوط بدقة في المهمة النهائية. راجع المواد التكميلية للحصول على التفاصيل.

---

### Translation Notes

- **Figures referenced:** None (references to Sec. 3.1, 3.2, 3.3, 3.4, Sec. 4)
- **Key terms introduced:** biLM (bidirectional language model), TagLM, SNLI, SQuAD, bi-attention, coreference resolution, highway layers, n-gram convolutions, perplexity, domain transfer, 1B Word Benchmark
- **Equations:** 5 major equations describing forward LM, backward LM, biLM objective, ELMo representation, and weighted combination
- **Citations:** Pennington et al. 2014, Józefowicz et al. 2016, Melis et al. 2017, Merity et al. 2017, Peters et al. 2017, McCann et al. 2017, Ba et al. 2016, Srivastava et al. 2014, Srivastava et al. 2015, Kim et al. 2015, Chelba et al. 2014
- **Special handling:**
  - Preserved all LaTeX equations with proper formatting
  - Maintained technical abbreviations: biLM, LSTM, CNN, RNN
  - Added Arabic explanations for key concepts
  - Used consistent mathematical notation in both languages

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Validation (Opening Paragraph)

Unlike most widely used word embeddings, ELMo word representations are functions of the complete input sentence, as described in this section. They are computed on top of two-layer bidirectional language models (biLMs) with character convolutions (Section 3.1), as a linear function of the internal network states (Section 3.2). This setup allows us to do semi-supervised learning, where the biLM is pre-trained at large scale (Section 3.4) and easily integrated into a wide range of existing neural NLP architectures (Section 3.3).

**Validation:** ✓ Excellent semantic match with original, technical accuracy maintained
