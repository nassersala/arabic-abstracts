# Section 4: Experimental Setup
## القسم 4: الإعداد التجريبي

**Section:** experimental-setup
**Translation Quality:** 0.86
**Glossary Terms Used:** dataset, pre-processing, code completion, code summarization, code search, transformer, abstract syntax tree, hyperparameters, evaluation metrics, BLEU, METEOR, ROUGE-L, MRR

---

### English Version

## 4 EXPERIMENTAL SETUP

### 4.1 Datasets and pre-processing

Following the prior work [41], we choose the Java and Python datasets from CodeSearchNet [37] for evaluation. CodeSearchNet is a collection of large datasets with code-document pairs from open source projects on GitHub, which is widely-used in code intelligence tasks [42], [43]. Detailed data statistics are illustrated in Table 2. The subject data consist of 165K / 5K / 11K training / validation / test code snippets for Java and 252K / 14K / 15K for Python, respectively. For facilitating analysis, we parse the code snippets into ASTs, and traverse the ASTs into sequences of tokens as input in depth-first-search order following [5].

### 4.2 Implementation

In this work, we consider three code intelligence tasks: code completion, code summarization, and code search. We elaborate on the detailed implementation of the three tasks in the following.

**Code completion.** We use the setup, metrics and implementation of Transformer according to [8]. Besides, we split code sequence whose length is over 500 following [5].

**Code summarization.** In our experiments, we select [10] as Transformer implementation except that we do not split sub-token following Chirkova et al. [5].

**Code search.** In our experiments, we implement a Transformer architecture for code search task based on [44]. We process the dataset following the strategy of Evangelos et. al [44]. For example, we filter the non-ASCII tokens and replace symbols by their English names (e.g., the symbol + in code token is replace by addoperator).

**Hyper-parameters.** The hyper-parameters setting in our experiments follows Transformer implementations [8], [10], [44] and we list the major hyper-parameters for code completion, code summarization, and code search tasks. Our Transformer models include 6 layers, 6 heads with the layers of our models to be 512. We set the maximum distance of relative attention to 32 for all tasks. We train Transformers using Adam with a starting learning rate of 0.0001 and a batch size of 32 / 32 / 128 with the epoch number being 15 / 20 / 100 for code completion, summarization, and search respectively. We train all models on 4 GPUs of Nvidia Tesla V100 with 32G of memory.

**Evaluation set.** As illustrated in Table 1, not all the transformation strategies are applicable for both programming languages. For example, the bool to int strategy is only allowed in Python. During analyzing the impact of each code transformation strategy on models' performance, we only evaluate on the transformable code instead of all the code in the test set. Besides, to minimize the performance bias, we run each experiment for three times and report the average results.

### 4.3 Evaluation metrics

#### 4.3.1 Code summarization

We evaluate the source code summarization performance using three metrics: BLEU, METEOR and ROUGE-L.

**BLEU** is a widely-used metric in natural language processing and software engineering fields to evaluate the quality of generated texts, e.g., machine translation, code comment generation, and code commit message generation [45]. It computes the frequencies of the co-occurrence of n-grams between the ground truth ŷ and the generated sequence y to judge the similarity:

$$BLEU-N = b(y, \hat{y}) \cdot \exp \left( \sum_{n=1}^{N} \beta_n \log p_n(y, \hat{y}) \right),$$

where b(y, ŷ) is the brevity penalty, pₙ(y, ŷ) represents the precision of n-grams, and βₙ is the weight of n-grams.

**ROUGE-L** is a widely-used metric in text summarization fields [46]. The metric is based on the longest common sub-sequence (LCS) and can be calculated as:

$$F_{lcs} = \frac{(1 + \beta^2) R_{lcs} P_{lcs}}{R_{lcs} + \beta^2 P_{lcs}},$$

where $R_{lcs} = \frac{LCS(X,Y)}{len(Y)}$ and $P_{lcs} = \frac{LCS(X,Y)}{len(X)}$. X and Y denote candidate sequence and reference sequence, respectively. LCS(X, Y) represents the length of the longest common sub-sequence between X and Y.

**METEOR** is an evaluation metric proposed based on BLEU [47]. It introduces synonym, stem, and other information to replace the precise matching in BLEU, and strengthens the role of recall in automatic evaluation.

#### 4.3.2 Code search and code completion

For code search and code completion tasks, we use MRR [48] as the evaluation metric. MRR is the average of the reciprocal rank of results of a set of queries. The reciprocal rank of a query is the inverse of the rank of the first hit result.

$$MRR = \frac{1}{N} \sum_{n=1}^{N} \frac{1}{rank_i},$$

where N is the total number of targets (tokens for code completion and code snippet for code search) in data pool and rankᵢ represents the position of the i-th true target in the ranking results.

---

### النسخة العربية

## 4 الإعداد التجريبي

### 4.1 مجموعات البيانات والمعالجة المسبقة

متابعةً للعمل السابق [41]، نختار مجموعات بيانات جافا وبايثون من CodeSearchNet [37] للتقييم. CodeSearchNet هي مجموعة من مجموعات البيانات الكبيرة مع أزواج شفرة-وثيقة من مشاريع مفتوحة المصدر على GitHub، والتي تُستخدم على نطاق واسع في مهام ذكاء الشفرة [42]، [43]. تُوضح إحصائيات البيانات التفصيلية في الجدول 2. تتكون بيانات الموضوع من 165K / 5K / 11K مقتطفات شفرة للتدريب / التحقق / الاختبار لجافا و 252K / 14K / 15K لبايثون، على التوالي. لتسهيل التحليل، نحلل مقتطفات الشفرة إلى أشجار AST، ونجتاز أشجار AST إلى تسلسلات من الرموز كمدخلات بترتيب البحث بالعمق أولاً متابعةً لـ [5].

### 4.2 التنفيذ

في هذا العمل، نأخذ في الاعتبار ثلاث مهام ذكاء شفرة: إكمال الشفرة، وتلخيص الشفرة، والبحث في الشفرة. نشرح بالتفصيل التنفيذ التفصيلي للمهام الثلاث في ما يلي.

**إكمال الشفرة.** نستخدم الإعداد والمقاييس والتنفيذ للمحول وفقاً لـ [8]. بالإضافة إلى ذلك، نقسم تسلسل الشفرة الذي يزيد طوله عن 500 متابعةً لـ [5].

**تلخيص الشفرة.** في تجاربنا، نختار [10] كتنفيذ للمحول باستثناء أننا لا نقسم الرمز الفرعي متابعةً لـ Chirkova وآخرين [5].

**البحث في الشفرة.** في تجاربنا، ننفذ معمارية محول لمهمة البحث في الشفرة بناءً على [44]. نعالج مجموعة البيانات متابعةً لاستراتيجية Evangelos وآخرين [44]. على سبيل المثال، نُرشح الرموز غير ASCII ونستبدل الرموز بأسمائها الإنجليزية (على سبيل المثال، يتم استبدال الرمز + في رمز الشفرة بـ addoperator).

**المعاملات الفائقة.** يتبع إعداد المعاملات الفائقة في تجاربنا تنفيذات المحول [8]، [10]، [44] ونسرد المعاملات الفائقة الرئيسية لمهام إكمال الشفرة وتلخيص الشفرة والبحث في الشفرة. تتضمن نماذج المحول الخاصة بنا 6 طبقات، و6 رؤوس مع كون طبقات نماذجنا 512. نحدد المسافة القصوى للانتباه النسبي عند 32 لجميع المهام. نُدرب المحولات باستخدام Adam بمعدل تعلم ابتدائي قدره 0.0001 وحجم دفعة 32 / 32 / 128 مع كون عدد الحقب 15 / 20 / 100 لإكمال الشفرة والتلخيص والبحث على التوالي. نُدرب جميع النماذج على 4 وحدات معالجة رسومية من Nvidia Tesla V100 بسعة ذاكرة 32 جيجابايت.

**مجموعة التقييم.** كما هو موضح في الجدول 1، ليست كل استراتيجيات التحويل قابلة للتطبيق على كلتا لغتي البرمجة. على سبيل المثال، استراتيجية bool to int مسموح بها فقط في بايثون. أثناء تحليل تأثير كل استراتيجية تحويل شفرة على أداء النماذج، نقيم فقط الشفرة القابلة للتحويل بدلاً من كل الشفرة في مجموعة الاختبار. بالإضافة إلى ذلك، لتقليل تحيز الأداء، نشغل كل تجربة ثلاث مرات ونبلغ عن النتائج المتوسطة.

### 4.3 مقاييس التقييم

#### 4.3.1 تلخيص الشفرة

نقيم أداء تلخيص الشفرة المصدرية باستخدام ثلاثة مقاييس: BLEU وMETEOR وROUGE-L.

**BLEU** هو مقياس مستخدم على نطاق واسع في مجالات معالجة اللغة الطبيعية وهندسة البرمجيات لتقييم جودة النصوص المُولدة، على سبيل المثال، الترجمة الآلية، وتوليد تعليقات الشفرة، وتوليد رسائل التزام الشفرة [45]. يحسب ترددات التواجد المشترك لـ n-grams بين القيمة الحقيقية ŷ والتسلسل المُولد y للحكم على التشابه:

$$BLEU-N = b(y, \hat{y}) \cdot \exp \left( \sum_{n=1}^{N} \beta_n \log p_n(y, \hat{y}) \right),$$

حيث $b(y, \hat{y})$ هي عقوبة الإيجاز، $p_n(y, \hat{y})$ تمثل دقة n-grams، و $\beta_n$ هو وزن n-grams.

**ROUGE-L** هو مقياس مستخدم على نطاق واسع في مجالات تلخيص النص [46]. يعتمد المقياس على أطول تسلسل فرعي مشترك (LCS) ويمكن حسابه كما يلي:

$$F_{lcs} = \frac{(1 + \beta^2) R_{lcs} P_{lcs}}{R_{lcs} + \beta^2 P_{lcs}},$$

حيث $R_{lcs} = \frac{LCS(X,Y)}{len(Y)}$ و $P_{lcs} = \frac{LCS(X,Y)}{len(X)}$. يشير X و Y إلى التسلسل المرشح والتسلسل المرجعي، على التوالي. يمثل LCS(X, Y) طول أطول تسلسل فرعي مشترك بين X و Y.

**METEOR** هو مقياس تقييم مقترح بناءً على BLEU [47]. يقدم المرادف والجذر ومعلومات أخرى لاستبدال المطابقة الدقيقة في BLEU، ويعزز دور الاستدعاء في التقييم التلقائي.

#### 4.3.2 البحث في الشفرة وإكمال الشفرة

لمهام البحث في الشفرة وإكمال الشفرة، نستخدم MRR [48] كمقياس تقييم. MRR هو متوسط الترتيب المعكوس المتبادل لنتائج مجموعة من الاستعلامات. الترتيب المعكوس المتبادل لاستعلام هو معكوس ترتيب نتيجة الضربة الأولى.

$$MRR = \frac{1}{N} \sum_{n=1}^{N} \frac{1}{rank_i},$$

حيث N هو العدد الإجمالي للأهداف (الرموز لإكمال الشفرة ومقتطف الشفرة للبحث في الشفرة) في تجمع البيانات و $rank_i$ يمثل موضع الهدف الحقيقي i-th في نتائج الترتيب.

---

### Translation Notes

- **Tables referenced:** Table 1 (transformation strategies), Table 2 (dataset statistics)
- **Equations:** 3 mathematical equations for BLEU, ROUGE-L, and MRR
- **Key terms introduced:**
  - CodeSearchNet (مجموعة بيانات CodeSearchNet)
  - depth-first-search (البحث بالعمق أولاً)
  - sub-token (رمز فرعي)
  - non-ASCII tokens (رموز غير ASCII)
  - hyperparameters (معاملات فائقة)
  - batch size (حجم الدفعة)
  - epoch (حقبة)
  - learning rate (معدل التعلم)
  - GPU (وحدة معالجة رسومية)
  - BLEU (مقياس BLEU)
  - METEOR (مقياس METEOR)
  - ROUGE-L (مقياس ROUGE-L)
  - MRR (Mean Reciprocal Rank - الترتيب المعكوس المتبادل المتوسط)
  - n-grams (n-grams)
  - longest common subsequence (أطول تسلسل فرعي مشترك)
  - brevity penalty (عقوبة الإيجاز)
  - recall (استدعاء)
  - precision (دقة)
  - reciprocal rank (ترتيب معكوس متبادل)

- **Citations:** References [5], [8], [10], [37], [41]-[48]
- **Special handling:**
  - Dataset statistics preserved (165K/5K/11K for Java, 252K/14K/15K for Python)
  - Model architecture details (6 layers, 6 heads, 512 dimensions)
  - Training details (Adam optimizer, learning rate 0.0001, batch sizes, epochs)
  - Hardware specifications (4x Nvidia Tesla V100 with 32GB)
  - Mathematical formulas preserved in LaTeX with Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
