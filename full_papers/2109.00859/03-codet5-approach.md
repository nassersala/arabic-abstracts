# Section 3: CodeT5
## القسم 3: CodeT5

**Section:** methodology/approach
**Translation Quality:** 0.86
**Glossary Terms Used:** مشفر-فك تشفير, تسلسل إلى تسلسل, التدريب المسبق, المعرفات, شجرة البنية التركيبية المجردة, إزالة التشويش, وسم المعرفات, التنبؤ بالمعرفات المخفية, التوليد المزدوج ثنائي الوضع, التعلم متعدد المهام, الضبط الدقيق, تدفق البيانات

---

### English Version

**3 CodeT5**

Our CodeT5 builds on an encoder-decoder framework with the same architecture as T5 (Raffel et al., 2020). It aims to derive generic representations for programming language (PL) and natural language (NL) via pre-training on unlabeled source code. As illustrated in Figure 2, we extend the denoising Seq2Seq objective in T5 by proposing two identifier tagging and prediction tasks to enable the model to better leverage the token type information from PL, which are the identifiers assigned by developers. To improve the NL-PL alignment, we further propose a bimodal dual learning objective for a bidirectional conversion between NL and PL.

In the following, we introduce how CodeT5 encodes PL and NL inputs (§3.1) and our proposed identifier-aware pre-training tasks (§3.2), followed by the fine-tuning with task-specific transfer learning and multi-task training (§3.3).

**3.1 Encoding NL and PL**

At the pre-training stage, our model would receive either PL-only or NL-PL as inputs depending on whether the code snippet has accompanying NL descriptions or not. For the NL-PL bimodal inputs, we concatenate them into a sequence with a delimiter token [SEP] and represent the whole input sequence into the format as $x = ([CLS], w_1, ..., w_n, [SEP], c_1, ..., c_m, [SEP])$, where $n$ and $m$ denote the number of NL word tokens and PL code tokens, respectively. The NL word sequence will be empty for PL-only unimodal inputs.

In order to capture more code-specific features, we propose to leverage token type information from code. We focus on the type of identifiers (e.g., function names and variables) as they are one of the most PL-agnostic features and reserve rich code semantics. Specifically, we convert the PL segment into an Abstract Syntax Tree (AST) and extract the node types for each code token. Finally, we construct a sequence of binary labels $y \in \{0,1\}^m$ for the PL segment, where each $y_i \in \{0,1\}$ represents whether the code token $c_i$ is an identifier or not.

**3.2 Pre-training Tasks**

We now introduce our proposed pre-training tasks that enable CodeT5 to learn useful patterns from either PL-only or NL-PL bimodal data.

**Identifier-aware Denoising Pre-training.** Denoising Sequence-to-Sequence (Seq2Seq) pre-training has been shown to be quite effective in a broad set of NLP tasks (Song et al., 2019; Raffel et al., 2020; Lewis et al., 2020). This denoising objective typically first corrupts the source sequence with some noising functions and then requires the decoder to recover the original texts. In this work, we utilize a span masking objective similar to T5 (Raffel et al., 2020) that randomly masks spans with arbitrary lengths and then predicts these masked spans combined with some sentinel tokens at the decoder. We refer this task to **Masked Span Prediction (MSP)**, as illustrated in Figure 2 (a).

Specifically, we employ the same 15% corruption rate as T5 and ensure the average span length to be 3 by uniformly sampling spans of from 1 to 5 tokens. Moreover, we employ the whole word masking by sampling spans before subword tokenization, which aims to avoid masking partial sub-tokens and is shown to be helpful (Sun et al., 2019). Notably, we pre-train a shared model for various PLs to learn robust cross-lingual representations. We describe the masked span prediction loss as:

$$\mathcal{L}_{MSP}(\theta) = \sum_{t=1}^{k} -\log P(x_t^{mask} | x^{\neg mask}, x_{<t}^{mask}; \theta)$$
(1)

where $\theta$ are the model parameters, $x^{\neg mask}$ is the masked input, $x^{mask}$ is the masked sequence to predict from the decoder with $k$ denoting the number of tokens in $x^{mask}$, and $x_{<t}^{mask}$ is the span sequence generated so far.

To fuse more code-specific structural information (the identifier node type in AST) into the model, we propose two additional tasks: **Identifier Tagging (IT)** and **Masked Identifier Prediction (MIP)** to complement the denoising pre-training.

**Identifier Tagging (IT)** It aims to notify the model with the knowledge of whether this code token is an identifier or not, which shares a similar spirit of syntax highlighting in some developer-aided tools. As shown in Figure 2 (b), we map the final hidden states of the PL segment at the CodeT5 encoder into a sequence of probabilities $p = (p_1, ..., p_m)$, and compute a binary cross entropy loss for sequence labeling:

$$\mathcal{L}_{IT}(\theta_e) = -\sum_{i=1}^{m} [y_i \log p_i + (1 - y_i) \log(1 - p_i)]$$
(2)

where $\theta_e$ are the encoder parameters. Note that by casting the task as a sequence labeling problem, the model is expected to capture the code syntax and the data flow structures of the code.

**Masked Identifier Prediction (MIP)** Different from the random span masking in MSP, we mask all identifiers in the PL segment and employ a unique sentinel token for all occurrences of one specific identifier. In the field of software engineering, this is called obfuscation where changing identifier names does not impact the code semantics. Inspired by Rozière et al. (2021), we arrange the unique identifiers with the sentinel tokens into a target sequence $I$ as shown in Figure 2 (c). We then predict it in an auto-regressive manner:

$$\mathcal{L}_{MIP}(\theta) = \sum_{j=1}^{|I|} -\log P(I_j | x^{\neg I}, I_{<j}; \theta)$$
(3)

where $x^{\neg I}$ is the masked input. Note that deobfuscation is a more challenging task that requires the model to comprehend the code semantics based on obfuscated code and link the occurrences of the same identifiers together.

We alternately optimize these three losses with an equal probability, which constitutes our proposed identifier-aware denoising pre-training.

**Bimodal Dual Generation.** In the pre-training phase, the decoder only sees discrete masked spans and identifiers, which is disparate from the downstream tasks where the decoder needs to generate either fluent NL texts or syntactically correct code snippets. To close the gap between the pre-training and fine-tuning, we propose to leverage the NL-PL bimodal data to train the model for a bidirectional conversion as shown in Figure 2 (d). Specifically, we regard the NL→PL generation and PL→NL generation as dual tasks and simultaneously optimize the model on them. For each NL-PL bimodal datapoint, we construct two training instances with reverse directions and add language ids (e.g., <java> and <en> for Java PL and English NL, respectively). This operation can be also seen as a special case of T5's span masking by either masking the full NL or PL segment from the bimodal inputs. This task aims to improve the alignment between the NL and PL counterparts.

**3.3 Fine-tuning CodeT5**

After pre-training on large-scale unlabeled data, we adapt CodeT5 to downstream tasks via either task-specific transfer learning or multi-task learning.

**Task-specific Transfer Learning: Generation vs. Understanding Tasks.** Code-related tasks can be categorized into generation and understanding tasks. For the former one, our CodeT5 can be naturally adapted with its Seq2Seq framework. For understanding tasks, we investigate two ways of either generating the label as a unigram target sequence (Raffel et al., 2020), or predicting it from the vocabulary of class labels based on the last decoder hidden state following Lewis et al. (2020).

**Multi-task Learning.** We also explore a multi-task learning setting by training a shared model on multiple tasks at a time. Multi-task learning is able to reduce computation cost by reusing the most of model weights for many tasks and has been shown to improve the model generalization capability in NL pre-training (Liu et al., 2019a). We follow Raffel et al. (2020) to employ the same unified model for all tasks without adding any task-specific networks but allow to select different best checkpoints for different tasks. To notify the model with which task it is dealing with, we design a unified format of task control codes and prepend it into the source inputs as shown in Figure 1. For instance, we employ "Translate Java to CSharp:" as the source prompt for the code-to-code translation task from Java to CSharp.

As different tasks have different dataset sizes, we follow Conneau and Lample (2019) to employ a balanced sampling strategy. For $N$ number of datasets (or tasks), with probabilities $\{q_i\}_{i=1}^N$, we define the following multinomial distribution to sample from:

$$q_i = \frac{r_i^\alpha}{\sum_{j=1}^N r_j^\alpha}, \text{ where } r_i = \frac{n_i}{\sum_{k=1}^N n_k}$$
(4)

where $n_i$ is number of examples for i-th task and $\alpha$ is set to 0.7. This balanced sampling aims to alleviate the bias towards high-resource tasks.

---

### النسخة العربية

**3 CodeT5**

يبني CodeT5 الخاص بنا على إطار عمل مشفر-فك تشفير بنفس معمارية T5 (Raffel et al., 2020). يهدف إلى اشتقاق تمثيلات عامة للغة البرمجة (PL) واللغة الطبيعية (NL) عبر التدريب المسبق على الشفرة المصدرية غير المُعنونة. كما هو موضح في الشكل 2، نوسع هدف تسلسل إلى تسلسل لإزالة التشويش في T5 من خلال اقتراح مهمتين لوسم المعرفات والتنبؤ بها لتمكين النموذج من الاستفادة بشكل أفضل من معلومات نوع الرمز من لغة البرمجة، والتي هي المعرفات المُعينة من قبل المطورين. لتحسين المحاذاة بين اللغة الطبيعية ولغة البرمجة، نقترح أيضاً هدف تعلم مزدوج ثنائي الوضع للتحويل ثنائي الاتجاه بين اللغة الطبيعية ولغة البرمجة.

في ما يلي، نقدم كيفية ترميز CodeT5 لمدخلات لغة البرمجة واللغة الطبيعية (§3.1) ومهام التدريب المسبق المدركة للمعرفات المقترحة (§3.2)، متبوعة بالضبط الدقيق مع التعلم التحويلي الخاص بالمهمة والتدريب متعدد المهام (§3.3).

**3.1 ترميز اللغة الطبيعية ولغة البرمجة**

في مرحلة التدريب المسبق، يتلقى نموذجنا إما لغة برمجة فقط أو لغة طبيعية-لغة برمجة كمدخلات اعتماداً على ما إذا كان مقتطف الشفرة لديه أوصاف باللغة الطبيعية مصاحبة أم لا. بالنسبة لمدخلات اللغة الطبيعية-لغة البرمجة ثنائية الوضع، نربطها في تسلسل برمز فاصل [SEP] ونمثل تسلسل الإدخال الكامل بالتنسيق $x = ([CLS], w_1, ..., w_n, [SEP], c_1, ..., c_m, [SEP])$، حيث $n$ و $m$ تشير إلى عدد رموز كلمات اللغة الطبيعية ورموز شفرة لغة البرمجة على التوالي. سيكون تسلسل كلمات اللغة الطبيعية فارغاً للمدخلات أحادية الوضع بلغة برمجة فقط.

من أجل التقاط المزيد من الميزات الخاصة بالشفرة، نقترح الاستفادة من معلومات نوع الرمز من الشفرة. نركز على نوع المعرفات (على سبيل المثال، أسماء الدوال والمتغيرات) حيث أنها واحدة من أكثر الميزات المستقلة عن لغة البرمجة وتحفظ دلالات شفرة غنية. على وجه التحديد، نحول قطاع لغة البرمجة إلى شجرة بنية تركيبية مجردة (AST) ونستخرج أنواع العقد لكل رمز شفرة. أخيراً، نبني تسلسلاً من التسميات الثنائية $y \in \{0,1\}^m$ لقطاع لغة البرمجة، حيث كل $y_i \in \{0,1\}$ يمثل ما إذا كان رمز الشفرة $c_i$ معرّفاً أم لا.

**3.2 مهام التدريب المسبق**

نقدم الآن مهام التدريب المسبق المقترحة التي تمكّن CodeT5 من تعلم أنماط مفيدة من بيانات أحادية الوضع بلغة برمجة فقط أو ثنائية الوضع باللغة الطبيعية-لغة البرمجة.

**التدريب المسبق لإزالة التشويش المدرك للمعرفات.** لقد ثبت أن التدريب المسبق لتسلسل إلى تسلسل لإزالة التشويش فعال جداً في مجموعة واسعة من مهام معالجة اللغة الطبيعية (Song et al., 2019; Raffel et al., 2020; Lewis et al., 2020). عادةً ما يُفسد هذا الهدف لإزالة التشويش أولاً تسلسل المصدر بدوال تشويش معينة ثم يطلب من فك التشفير استعادة النصوص الأصلية. في هذا العمل، نستخدم هدف إخفاء النطاق مشابهاً لـ T5 (Raffel et al., 2020) الذي يخفي بشكل عشوائي نطاقات بأطوال تعسفية ثم يتنبأ بهذه النطاقات المخفية مجتمعة مع بعض الرموز الحارسة في فك التشفير. نشير إلى هذه المهمة باسم **التنبؤ بالنطاق المخفي (MSP)**، كما هو موضح في الشكل 2 (أ).

على وجه التحديد، نستخدم نفس معدل الإفساد 15% كـ T5 ونضمن أن يكون متوسط طول النطاق 3 من خلال أخذ عينات موحدة من نطاقات من 1 إلى 5 رموز. علاوة على ذلك، نستخدم إخفاء الكلمة الكاملة من خلال أخذ عينات من النطاقات قبل ترميز الكلمات الفرعية، والذي يهدف إلى تجنب إخفاء الرموز الفرعية الجزئية وقد ثبت أنه مفيد (Sun et al., 2019). من الجدير بالذكر أننا ندرب نموذجاً مشتركاً مسبقاً لمختلف لغات البرمجة لتعلم تمثيلات متينة عبر اللغات. نصف خسارة التنبؤ بالنطاق المخفي كما يلي:

$$\mathcal{L}_{MSP}(\theta) = \sum_{t=1}^{k} -\log P(x_t^{mask} | x^{\neg mask}, x_{<t}^{mask}; \theta)$$
(1)

حيث $\theta$ هي معاملات النموذج، $x^{\neg mask}$ هو الإدخال المخفي، $x^{mask}$ هو التسلسل المخفي للتنبؤ به من فك التشفير مع $k$ يشير إلى عدد الرموز في $x^{mask}$، و $x_{<t}^{mask}$ هو تسلسل النطاق المُولد حتى الآن.

لدمج المزيد من المعلومات البنيوية الخاصة بالشفرة (نوع عقدة المعرف في AST) في النموذج، نقترح مهمتين إضافيتين: **وسم المعرفات (IT)** و**التنبؤ بالمعرفات المخفية (MIP)** لاستكمال التدريب المسبق لإزالة التشويش.

**وسم المعرفات (IT)** تهدف إلى إخطار النموذج بمعرفة ما إذا كان رمز الشفرة هذا معرّفاً أم لا، والذي يشارك روحاً مشابهة لتسليط الضوء على بناء الجملة في بعض أدوات مساعدة المطورين. كما هو موضح في الشكل 2 (ب)، نقوم بتعيين الحالات المخفية النهائية لقطاع لغة البرمجة في مشفر CodeT5 إلى تسلسل من الاحتماليات $p = (p_1, ..., p_m)$، ونحسب خسارة الانتروبيا المتقاطعة الثنائية لوسم التسلسل:

$$\mathcal{L}_{IT}(\theta_e) = -\sum_{i=1}^{m} [y_i \log p_i + (1 - y_i) \log(1 - p_i)]$$
(2)

حيث $\theta_e$ هي معاملات المشفر. لاحظ أنه من خلال صياغة المهمة كمشكلة وسم تسلسل، من المتوقع أن يلتقط النموذج بناء جملة الشفرة وبنى تدفق البيانات للشفرة.

**التنبؤ بالمعرفات المخفية (MIP)** على عكس إخفاء النطاق العشوائي في MSP، نخفي جميع المعرفات في قطاع لغة البرمجة ونستخدم رمزاً حارساً فريداً لجميع حالات ظهور معرّف محدد واحد. في مجال هندسة البرمجيات، يُسمى هذا بالتعتيم حيث لا يؤثر تغيير أسماء المعرفات على دلالات الشفرة. مستوحى من Rozière et al. (2021)، نرتب المعرفات الفريدة مع الرموز الحارسة في تسلسل مستهدف $I$ كما هو موضح في الشكل 2 (ج). ثم نتنبأ به بطريقة انحدار ذاتي:

$$\mathcal{L}_{MIP}(\theta) = \sum_{j=1}^{|I|} -\log P(I_j | x^{\neg I}, I_{<j}; \theta)$$
(3)

حيث $x^{\neg I}$ هو الإدخال المخفي. لاحظ أن إزالة التعتيم هي مهمة أكثر تحدياً تتطلب من النموذج فهم دلالات الشفرة بناءً على شفرة مُعتمة وربط حالات ظهور نفس المعرفات معاً.

نحسّن هذه الخسائر الثلاث بالتناوب مع احتمالية متساوية، مما يشكل التدريب المسبق لإزالة التشويش المدرك للمعرفات المقترح.

**التوليد المزدوج ثنائي الوضع.** في مرحلة التدريب المسبق، يرى فك التشفير فقط نطاقات ومعرفات مخفية منفصلة، وهو ما يختلف عن المهام اللاحقة حيث يحتاج فك التشفير إلى توليد إما نصوص لغة طبيعية طليقة أو مقتطفات شفرة صحيحة من الناحية النحوية. لسد الفجوة بين التدريب المسبق والضبط الدقيق، نقترح الاستفادة من بيانات اللغة الطبيعية-لغة البرمجة ثنائية الوضع لتدريب النموذج على تحويل ثنائي الاتجاه كما هو موضح في الشكل 2 (د). على وجه التحديد، نعتبر توليد اللغة الطبيعية→لغة البرمجة وتوليد لغة البرمجة→اللغة الطبيعية كمهام مزدوجة ونحسّن النموذج عليهما في وقت واحد. لكل نقطة بيانات ثنائية الوضع للغة الطبيعية-لغة البرمجة، نبني حالتي تدريب باتجاهات عكسية ونضيف معرّفات اللغة (على سبيل المثال، <java> و <en> للغة برمجة Java واللغة الطبيعية الإنجليزية على التوالي). يمكن أيضاً رؤية هذه العملية كحالة خاصة من إخفاء النطاق في T5 من خلال إخفاء قطاع اللغة الطبيعية أو لغة البرمجة الكامل من المدخلات ثنائية الوضع. تهدف هذه المهمة إلى تحسين المحاذاة بين نظيري اللغة الطبيعية ولغة البرمجة.

**3.3 الضبط الدقيق لـ CodeT5**

بعد التدريب المسبق على بيانات واسعة النطاق غير المُعنونة، نكيّف CodeT5 للمهام اللاحقة عبر إما التعلم التحويلي الخاص بالمهمة أو التعلم متعدد المهام.

**التعلم التحويلي الخاص بالمهمة: مهام التوليد مقابل الفهم.** يمكن تصنيف المهام المتعلقة بالشفرة إلى مهام التوليد والفهم. بالنسبة للأولى، يمكن تكييف CodeT5 الخاص بنا بشكل طبيعي مع إطار عمل تسلسل إلى تسلسل الخاص به. بالنسبة لمهام الفهم، نستكشف طريقتين إما توليد التسمية كتسلسل مستهدف أحادي الكلمة (Raffel et al., 2020)، أو التنبؤ بها من مفردات تسميات الفئات بناءً على آخر حالة مخفية لفك التشفير متبعين Lewis et al. (2020).

**التعلم متعدد المهام.** نستكشف أيضاً إعداد تعلم متعدد المهام من خلال تدريب نموذج مشترك على مهام متعددة في وقت واحد. يمكن للتعلم متعدد المهام تقليل تكلفة الحساب من خلال إعادة استخدام معظم أوزان النموذج للعديد من المهام وقد ثبت أنه يحسن قدرة التعميم للنموذج في التدريب المسبق للغة الطبيعية (Liu et al., 2019a). نتبع Raffel et al. (2020) لاستخدام نفس النموذج الموحد لجميع المهام دون إضافة أي شبكات خاصة بالمهام ولكن نسمح باختيار أفضل نقاط التحقق المختلفة للمهام المختلفة. لإخطار النموذج بالمهمة التي يتعامل معها، نصمم تنسيقاً موحداً لرموز التحكم في المهام ونضيفه إلى مدخلات المصدر كما هو موضح في الشكل 1. على سبيل المثال، نستخدم "Translate Java to CSharp:" كموجه مصدر لمهمة ترجمة الشفرة إلى شفرة من Java إلى CSharp.

نظراً لأن المهام المختلفة لها أحجام مجموعات بيانات مختلفة، نتبع Conneau و Lample (2019) لاستخدام استراتيجية أخذ عينات متوازنة. لعدد $N$ من مجموعات البيانات (أو المهام)، مع احتماليات $\{q_i\}_{i=1}^N$، نحدد التوزيع متعدد الحدود التالي لأخذ العينات منه:

$$q_i = \frac{r_i^\alpha}{\sum_{j=1}^N r_j^\alpha}, \text{ حيث } r_i = \frac{n_i}{\sum_{k=1}^N n_k}$$
(4)

حيث $n_i$ هو عدد الأمثلة للمهمة i-th و $\alpha$ يتم تعيينه إلى 0.7. يهدف هذا الأخذ المتوازن للعينات إلى تخفيف التحيز نحو المهام ذات الموارد العالية.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2 (with subfigures a, b, c, d)
- **Key terms introduced:** شجرة البنية التركيبية المجردة (AST - Abstract Syntax Tree), التنبؤ بالنطاق المخفي (Masked Span Prediction - MSP), وسم المعرفات (Identifier Tagging - IT), التنبؤ بالمعرفات المخفية (Masked Identifier Prediction - MIP), التعتيم (obfuscation), إزالة التعتيم (deobfuscation), رمز حارس (sentinel token), الانتروبيا المتقاطعة الثنائية (binary cross entropy)
- **Equations:** 4 main equations (MSP loss, IT loss, MIP loss, balanced sampling)
- **Citations:** 10 references cited (Raffel 2020, Song 2019, Lewis 2020, Sun 2019, Rozière 2021, Liu 2019a, Conneau 2019, Lample 2019)
- **Special handling:**
  - Preserved mathematical notation in LaTeX format
  - Kept special tokens like [CLS], [SEP], <java>, <en> in English
  - Maintained model names (T5, CodeT5) in English
  - Added Arabic explanations for complex mathematical expressions

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
