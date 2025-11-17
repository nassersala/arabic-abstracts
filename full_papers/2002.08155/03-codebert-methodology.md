# Section 3: CodeBERT
## القسم 3: CodeBERT

**Section:** Methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** معمارية, محولات, ثنائي الاتجاه, التمثيلات, التدريب المسبق, نمذجة اللغة المقنعة, الكشف عن الرموز المستبدلة, ثنائي الوضع, أحادي الوضع, الضبط الدقيق, مولد, مميز, دالة الخسارة

---

### English Version

# 3 CodeBERT

We describe the details about CodeBERT in this section, including the model architecture, the input and output representations, the objectives and data used for training CodeBERT, and how to fine-tune CodeBERT when it is applied to downstream tasks.

## 3.1 Model Architecture

We follow BERT (Devlin et al., 2018) and RoBERTa (Liu et al., 2019), and use multi-layer bidirectional Transformer (Vaswani et al., 2017) as the model architecture of CodeBERT. We will not review the ubiquitous Transformer architecture in detail. We develop CodeBERT by using exactly the same model architecture as RoBERTa-base. The total number of model parameters is 125M.

## 3.2 Input/Output Representations

In the pre-training phase, we set the input as the concatenation of two segments with a special separator token, namely [CLS], w1, w2, ..wn, [SEP], c1, c2, ..., cm, [EOS]. One segment is natural language text, and another is code from a certain programming language. [CLS] is a special token in front of the two segments, whose final hidden representation is considered as the aggregated sequence representation for classification or ranking. Following the standard way of processing text in Transformer, we regard a natural language text as a sequence of words, and split it as WordPiece (Wu et al., 2016). We regard a piece of code as a sequence of tokens.

The output of CodeBERT includes (1) contextual vector representation of each token, for both natural language and code, and (2) the representation of [CLS], which works as the aggregated sequence representation.

## 3.3 Pre-Training Data

We train CodeBERT with both bimodal data, which refers to parallel data of natural language-code pairs, and unimodal data, which stands for codes without paired natural language texts and natural language without paired codes.

We use datapoints from Github repositories, where each bimodal datapoint is an individual function with paired documentation, and each unimodal code is a function without paired documentation. Specifically, we use a recent large dataset provided by Husain et al. (2019), which includes 2.1M bimodal datapoints and 6.4M unimodal codes across six programming languages (Python, Java, JavaScript, PHP, Ruby, and Go). Data statistics is shown in Table 1.

**Table 1: Statistics of the dataset used for training CodeBERT.**

| TRAINING DATA | bimodal DATA | unimodal CODES |
|---------------|--------------|----------------|
| GO            | 319,256      | 726,768        |
| JAVA          | 500,754      | 1,569,889      |
| JAVASCRIPT    | 143,252      | 1,857,835      |
| PHP           | 662,907      | 977,821        |
| PYTHON        | 458,219      | 1,156,085      |
| RUBY          | 52,905       | 164,048        |
| ALL           | 2,137,293    | 6,452,446      |

The data comes from publicly available open-source non-fork GitHub repositories and are filtered with a set of constraints and rules. For example, (1) each project should be used by at least one other project, (2) each documentation is truncated to the first paragraph, (3) documentations shorter than three tokens are removed, (4) functions shorter than three lines are removed, and (5) function names with substring "test" are removed.

## 3.4 Pre-Training CodeBERT

We describe the two objectives used for training CodeBERT here. The first objective is masked language modeling (MLM), which has proven effective in literature (Devlin et al., 2018; Liu et al., 2019; Sun et al., 2019). We apply masked language modeling on bimodal data of NL-PL pairs. The second objective is replaced token detection (RTD), which further uses a large amount of unimodal data, such as codes without paired natural language texts.

**Objective #1: Masked Language Modeling (MLM)** Given a datapoint of NL-PL pair (x = {w, c}) as input, where w is a sequence of NL words and c is a sequence of PL tokens, we first select a random set of positions for both NL and PL to mask out (i.e. $m^w$ and $m^c$, respectively), and then replace the selected positions with a special [MASK] token. Following Devlin et al. (2018), 15% of the tokens from x are masked out.

$$m^w_i \sim \text{unif}\{1, |w|\} \text{ for } i = 1 \text{ to } |w|$$ (1)

$$m^c_i \sim \text{unif}\{1, |c|\} \text{ for } i = 1 \text{ to } |c|$$ (2)

$$w^{\text{masked}} = \text{REPLACE}(w, m^w, [\text{MASK}])$$ (3)

$$c^{\text{masked}} = \text{REPLACE}(c, m^c, [\text{MASK}])$$ (4)

$$x = w + c$$ (5)

The MLM objective is to predict the original tokens which are masked out, formulated as follows, where $p_{D1}$ is the discriminator which predicts a token from a large vocabulary.

$$\mathcal{L}_{\text{MLM}}(\theta) = \sum_{i \in m^w \cup m^c} -\log p_{D1}(x_i | w^{\text{masked}}, c^{\text{masked}})$$ (6)

**Objective #2: Replaced Token Detection (RTD)** In the MLM objective, only bimodal data (i.e. datapoints of NL-PL pairs) is used for training. Here we present the objective of replaced token detection. The RTD objective (Clark et al., 2020) is originally developed for efficiently learning pre-trained model for natural language. We adapt it in our scenario, with the advantage of using both bimodal and unimodal data for training. Specifically, there are two data generators here, an NL generator $p_{Gw}$ and a PL generator $p_{Gc}$, both for generating plausible alternatives for the set of randomly masked positions.

$$\hat{w}_i \sim p_{Gw}(w_i | w^{\text{masked}}) \text{ for } i \in m^w$$ (7)

$$\hat{c}_i \sim p_{Gc}(c_i | c^{\text{masked}}) \text{ for } i \in m^c$$ (8)

$$w^{\text{corrupt}} = \text{REPLACE}(w, m^w, \hat{w})$$ (9)

$$c^{\text{corrupt}} = \text{REPLACE}(c, m^c, \hat{c})$$ (10)

$$x^{\text{corrupt}} = w^{\text{corrupt}} + c^{\text{corrupt}}$$ (11)

The discriminator is trained to determine whether a word is the original one or not, which is a binary classification problem. It is worth noting that the RTD objective is applied to every position in the input, and it differs from GAN (generative adversarial network) in that if a generator happens to produce the correct token, the label of that token is "real" instead of "fake" (Clark et al., 2020). The loss function of RTD with regard to the discriminator parameterized by θ is given below, where $\delta(i)$ is an indicator function and $p_{D2}$ is the discriminator that predicts the probability of the i-th word being original.

$$\mathcal{L}_{\text{RTD}}(\theta) = \sum_{i=1}^{|w|+|c|} \left[ \delta(i) \log p_{D2}(x^{\text{corrupt}}, i) + (1 - \delta(i))(1 - \log p_{D2}(x^{\text{corrupt}}, i)) \right]$$ (12)

$$\delta(i) = \begin{cases} 1, & \text{if } x^{\text{corrupt}}_i = x_i \\ 0, & \text{otherwise} \end{cases}$$ (13)

There are many different ways to implement the generators. In this work, we implement two efficient n-gram language models (Jurafsky, 2000) with bidirectional contexts, one for NL and one for PL, and learn them from corresponding unimodal datapoints, respectively. The approach is easily generalized to learn bimodal generators or use more complicated generators like Transformer-based neural architecture learned in a joint manner. We leave these to future work. The PL training data is the unimodal codes as shown in Table 1, and the NL training data comes from the documentations from bimodal data. One could easily extend these two training datasets to larger amount. The final loss function are given below.

$$\min_\theta \mathcal{L}_{\text{MLM}}(\theta) + \mathcal{L}_{\text{RTD}}(\theta)$$ (14)

## 3.5 Fine-Tuning CodeBERT

We have different settings to use CodeBERT in downstream NL-PL tasks. For example, in natural language code search, we feed the input as the same way as the pre-training phase and use the representation of [CLS] to measure the semantic relevance between code and natural language query, while in code-to-text generation, we use an encoder-decoder framework and initialize the encoder of a generative model with CodeBERT. Details are given in the experiment section.

---

### النسخة العربية

# 3 CodeBERT

نصف تفاصيل CodeBERT في هذا القسم، بما في ذلك معمارية النموذج، وتمثيلات المدخلات والمخرجات، والأهداف والبيانات المستخدمة لتدريب CodeBERT، وكيفية الضبط الدقيق لـ CodeBERT عند تطبيقه على المهام المتتابعة.

## 3.1 معمارية النموذج

نتبع BERT (Devlin et al., 2018) و RoBERTa (Liu et al., 2019)، ونستخدم المحولات ثنائية الاتجاه متعددة الطبقات (Vaswani et al., 2017) كمعمارية النموذج لـ CodeBERT. لن نراجع معمارية المحولات المنتشرة في كل مكان بالتفصيل. نطور CodeBERT باستخدام نفس معمارية النموذج بالضبط مثل RoBERTa-base. العدد الإجمالي لمعاملات النموذج هو 125 مليون.

## 3.2 تمثيلات المدخلات/المخرجات

في مرحلة التدريب المسبق، نضع المدخلات على أنها تسلسل مُركّب من قطعتين برمز فاصل خاص، وهو [CLS], w1, w2, ..wn, [SEP], c1, c2, ..., cm, [EOS]. قطعة واحدة هي نص باللغة الطبيعية، والأخرى هي شفرة من لغة برمجة معينة. [CLS] هو رمز خاص في مقدمة القطعتين، يُعتبر تمثيله المخفي النهائي التمثيل المجمّع للتسلسل للتصنيف أو الترتيب. باتباع الطريقة القياسية لمعالجة النص في المحولات، نعتبر نص اللغة الطبيعية تسلسلاً من الكلمات، ونقسمه إلى WordPiece (Wu et al., 2016). نعتبر جزء الشفرة تسلسلاً من الرموز.

يتضمن مخرج CodeBERT (1) التمثيل المتجه السياقي لكل رمز، لكل من اللغة الطبيعية والشفرة، و(2) تمثيل [CLS]، الذي يعمل كالتمثيل المجمّع للتسلسل.

## 3.3 بيانات التدريب المسبق

ندرب CodeBERT بكل من البيانات ثنائية الوضع، التي تشير إلى البيانات المتوازية لأزواج اللغة الطبيعية والشفرة، والبيانات أحادية الوضع، التي تمثل شفرات بدون نصوص باللغة الطبيعية مقترنة ولغة طبيعية بدون شفرات مقترنة.

نستخدم نقاط بيانات من مستودعات Github، حيث كل نقطة بيانات ثنائية الوضع هي دالة فردية مع توثيق مقترن، وكل شفرة أحادية الوضع هي دالة بدون توثيق مقترن. على وجه التحديد، نستخدم مجموعة بيانات كبيرة حديثة قدمها Husain et al. (2019)، والتي تتضمن 2.1 مليون نقطة بيانات ثنائية الوضع و6.4 مليون شفرة أحادية الوضع عبر ست لغات برمجة (Python و Java و JavaScript و PHP و Ruby و Go). إحصائيات البيانات موضحة في الجدول 1.

**الجدول 1: إحصائيات مجموعة البيانات المستخدمة لتدريب CodeBERT.**

| بيانات التدريب | بيانات ثنائية الوضع | شفرات أحادية الوضع |
|----------------|---------------------|---------------------|
| GO             | 319,256             | 726,768             |
| JAVA           | 500,754             | 1,569,889           |
| JAVASCRIPT     | 143,252             | 1,857,835           |
| PHP            | 662,907             | 977,821             |
| PYTHON         | 458,219             | 1,156,085           |
| RUBY           | 52,905              | 164,048             |
| الكل           | 2,137,293           | 6,452,446           |

تأتي البيانات من مستودعات GitHub مفتوحة المصدر غير المتفرعة المتاحة للعامة ويتم تصفيتها بمجموعة من القيود والقواعد. على سبيل المثال، (1) يجب أن يُستخدم كل مشروع من قبل مشروع آخر واحد على الأقل، و(2) يتم اقتطاع كل توثيق إلى الفقرة الأولى، و(3) تُزال التوثيقات الأقصر من ثلاثة رموز، و(4) تُزال الدوال الأقصر من ثلاثة أسطر، و(5) تُزال أسماء الدوال التي تحتوي على السلسلة الفرعية "test".

## 3.4 التدريب المسبق لـ CodeBERT

نصف هنا الهدفين المستخدمين لتدريب CodeBERT. الهدف الأول هو نمذجة اللغة المقنعة (MLM)، والتي ثبتت فعاليتها في الأدبيات (Devlin et al., 2018; Liu et al., 2019; Sun et al., 2019). نطبق نمذجة اللغة المقنعة على البيانات ثنائية الوضع لأزواج اللغة الطبيعية ولغة البرمجة. الهدف الثاني هو الكشف عن الرموز المستبدلة (RTD)، والذي يستخدم بشكل أكبر كمية كبيرة من البيانات أحادية الوضع، مثل الشفرات بدون نصوص باللغة الطبيعية مقترنة.

**الهدف رقم 1: نمذجة اللغة المقنعة (MLM)** بالنظر إلى نقطة بيانات لزوج اللغة الطبيعية ولغة البرمجة (x = {w, c}) كمدخل، حيث w هو تسلسل كلمات اللغة الطبيعية و c هو تسلسل رموز لغة البرمجة، نختار أولاً مجموعة عشوائية من المواضع لكل من اللغة الطبيعية ولغة البرمجة للتقنيع (أي $m^w$ و $m^c$، على التوالي)، ثم نستبدل المواضع المختارة برمز [MASK] خاص. باتباع Devlin et al. (2018)، يتم تقنيع 15% من الرموز من x.

$$m^w_i \sim \text{unif}\{1, |w|\} \text{ لـ } i = 1 \text{ إلى } |w|$$ (1)

$$m^c_i \sim \text{unif}\{1, |c|\} \text{ لـ } i = 1 \text{ إلى } |c|$$ (2)

$$w^{\text{masked}} = \text{REPLACE}(w, m^w, [\text{MASK}])$$ (3)

$$c^{\text{masked}} = \text{REPLACE}(c, m^c, [\text{MASK}])$$ (4)

$$x = w + c$$ (5)

هدف MLM هو التنبؤ بالرموز الأصلية التي تم تقنيعها، والمصاغة على النحو التالي، حيث $p_{D1}$ هو المميز الذي يتنبأ برمز من مفردات كبيرة.

$$\mathcal{L}_{\text{MLM}}(\theta) = \sum_{i \in m^w \cup m^c} -\log p_{D1}(x_i | w^{\text{masked}}, c^{\text{masked}})$$ (6)

**الهدف رقم 2: الكشف عن الرموز المستبدلة (RTD)** في هدف MLM، تُستخدم البيانات ثنائية الوضع فقط (أي نقاط بيانات أزواج اللغة الطبيعية ولغة البرمجة) للتدريب. هنا نقدم هدف الكشف عن الرموز المستبدلة. تم تطوير هدف RTD (Clark et al., 2020) أصلاً لتعلم النموذج المُدرب مسبقاً للغة الطبيعية بكفاءة. نقوم بتكييفه في سيناريونا، مع ميزة استخدام كل من البيانات ثنائية الوضع وأحادية الوضع للتدريب. على وجه التحديد، يوجد هنا مولدان للبيانات، مولد للغة الطبيعية $p_{Gw}$ ومولد للغة البرمجة $p_{Gc}$، كلاهما لتوليد بدائل محتملة لمجموعة المواضع المقنعة عشوائياً.

$$\hat{w}_i \sim p_{Gw}(w_i | w^{\text{masked}}) \text{ لـ } i \in m^w$$ (7)

$$\hat{c}_i \sim p_{Gc}(c_i | c^{\text{masked}}) \text{ لـ } i \in m^c$$ (8)

$$w^{\text{corrupt}} = \text{REPLACE}(w, m^w, \hat{w})$$ (9)

$$c^{\text{corrupt}} = \text{REPLACE}(c, m^c, \hat{c})$$ (10)

$$x^{\text{corrupt}} = w^{\text{corrupt}} + c^{\text{corrupt}}$$ (11)

يتم تدريب المميز لتحديد ما إذا كانت الكلمة أصلية أم لا، وهي مشكلة تصنيف ثنائي. تجدر الإشارة إلى أن هدف RTD يُطبق على كل موضع في المدخلات، ويختلف عن GAN (الشبكة التوليدية الخصامية) في أنه إذا حدث أن أنتج المولد الرمز الصحيح، فإن تسمية ذلك الرمز هي "حقيقي" بدلاً من "مزيف" (Clark et al., 2020). دالة الخسارة لـ RTD فيما يتعلق بالمميز المُعاملي بـ θ معطاة أدناه، حيث $\delta(i)$ هي دالة مؤشر و $p_{D2}$ هو المميز الذي يتنبأ باحتمالية كون الكلمة الـ i أصلية.

$$\mathcal{L}_{\text{RTD}}(\theta) = \sum_{i=1}^{|w|+|c|} \left[ \delta(i) \log p_{D2}(x^{\text{corrupt}}, i) + (1 - \delta(i))(1 - \log p_{D2}(x^{\text{corrupt}}, i)) \right]$$ (12)

$$\delta(i) = \begin{cases} 1, & \text{إذا } x^{\text{corrupt}}_i = x_i \\ 0, & \text{خلاف ذلك} \end{cases}$$ (13)

هناك العديد من الطرق المختلفة لتنفيذ المولدات. في هذا العمل، ننفذ نموذجين فعالين للغة n-gram (Jurafsky, 2000) بسياقات ثنائية الاتجاه، واحد للغة الطبيعية وواحد للغة البرمجة، ونتعلمها من نقاط البيانات أحادية الوضع المقابلة، على التوالي. النهج يمكن تعميمه بسهولة لتعلم مولدات ثنائية الوضع أو استخدام مولدات أكثر تعقيداً مثل المعمارية العصبية القائمة على المحولات المتعلمة بطريقة مشتركة. نترك ذلك للعمل المستقبلي. بيانات تدريب لغة البرمجة هي الشفرات أحادية الوضع كما هو موضح في الجدول 1، وبيانات تدريب اللغة الطبيعية تأتي من التوثيقات من البيانات ثنائية الوضع. يمكن للمرء بسهولة توسيع مجموعتي البيانات التدريبية هاتين إلى كمية أكبر. دالة الخسارة النهائية معطاة أدناه.

$$\min_\theta \mathcal{L}_{\text{MLM}}(\theta) + \mathcal{L}_{\text{RTD}}(\theta)$$ (14)

## 3.5 الضبط الدقيق لـ CodeBERT

لدينا إعدادات مختلفة لاستخدام CodeBERT في مهام اللغة الطبيعية ولغة البرمجة المتتابعة. على سبيل المثال، في البحث عن الشفرة باللغة الطبيعية، نقدم المدخلات بنفس الطريقة كمرحلة التدريب المسبق ونستخدم تمثيل [CLS] لقياس الصلة الدلالية بين الشفرة واستعلام اللغة الطبيعية، بينما في توليد النص من الشفرة، نستخدم إطار مشفر-فك تشفير ونهيئ المشفر للنموذج التوليدي بـ CodeBERT. التفاصيل معطاة في قسم التجارب.

---

### Translation Notes

- **Figures referenced:** Figure 2 (illustration of RTD objective - not translated, referenced)
- **Tables referenced:** Table 1 (data statistics - translated)
- **Key terms introduced:** Masked language modeling (MLM), Replaced token detection (RTD), discriminator, generator, WordPiece, n-gram language model
- **Equations:** 14 equations (1-14) - LaTeX format preserved
- **Citations:** 8 references cited
- **Special handling:**
  - Mathematical equations kept in LaTeX with Arabic explanatory text
  - Special tokens [CLS], [SEP], [EOS], [MASK] kept in English as standard notation
  - Model names (BERT, RoBERTa) kept in English
  - Programming languages kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Sample

Key paragraph (from 3.4, RTD description) back-translated:

**Arabic:** "يتم تدريب المميز لتحديد ما إذا كانت الكلمة أصلية أم لا، وهي مشكلة تصنيف ثنائي. تجدر الإشارة إلى أن هدف RTD يُطبق على كل موضع في المدخلات، ويختلف عن GAN (الشبكة التوليدية الخصامية) في أنه إذا حدث أن أنتج المولد الرمز الصحيح، فإن تسمية ذلك الرمز هي "حقيقي" بدلاً من "مزيف"."

**Back-translation:** "The discriminator is trained to determine whether a word is original or not, which is a binary classification problem. It is worth noting that the RTD objective is applied to every position in the inputs, and differs from GAN (Generative Adversarial Network) in that if the generator happens to produce the correct token, the label of that token is 'real' instead of 'fake'."

**Semantic match:** ✓ High fidelity to original
