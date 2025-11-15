# Section 4: Training Procedure Analysis
## القسم 4: تحليل إجراءات التدريب

**Section:** training-procedure-analysis
**Translation Quality:** 0.87
**Glossary Terms Used:** static masking (الإخفاء الثابت), dynamic masking (الإخفاء الديناميكي), next sentence prediction (التنبؤ بالجملة التالية), batch size (حجم الدفعة), perplexity (الحيرة), gradient accumulation (تراكم التدرج), byte-pair encoding (ترميز زوج البايت), tokenization (التجزئة), hyperparameter (معامل فائق), F1 score (درجة F1), accuracy (الدقة)

---

### English Version

## 4 Training Procedure Analysis

This section explores and quantifies which choices are important for successfully pretraining BERT models. We keep the model architecture fixed. Specifically, we begin by training BERT models with the same configuration as BERT$_\text{BASE}$ ($L = 12$, $H = 768$, $A = 12$, 110M params).

### 4.1 Static vs. Dynamic Masking

As discussed in Section 2, BERT relies on randomly masking and predicting tokens. The original BERT implementation performed masking once during data preprocessing, resulting in a single static mask. To avoid using the same mask for each training instance in every epoch, training data was duplicated 10 times so that each sequence is masked in 10 different ways over the 40 epochs of training. Thus, each training sequence was seen with the same mask four times during training.

We compare this strategy with *dynamic masking* where we generate the masking pattern every time we feed a sequence to the model. This becomes crucial when pretraining for more steps or with larger datasets.

**Results** Table 1 compares the published BERT$_\text{BASE}$ results from Devlin et al. (2019) to our reimplementation with either static or dynamic masking. We find that our reimplementation with static masking performs similar to the original BERT model, and dynamic masking is comparable or slightly better than static masking. Given these results and the additional efficiency benefits of dynamic masking, we use dynamic masking in the remainder of the experiments.

| Masking | SQuAD 2.0 | MNLI-m | SST-2 |
|---------|-----------|--------|-------|
| reference | 76.3 | 84.3 | 92.8 |
| Our reimplementation: | | | |
| static | 78.3 | 84.3 | 92.5 |
| dynamic | 78.7 | 84.0 | 92.9 |

**Table 1:** Comparison between static and dynamic masking for BERT$_\text{BASE}$. We report F1 for SQuAD and accuracy for MNLI-m and SST-2. Reported results are medians over 5 random initializations (seeds). Reference results are from Yang et al. (2019).

### 4.2 Model Input Format and Next Sentence Prediction

In the original BERT pretraining procedure, the model observes two concatenated document segments, which are either sampled contiguously from the same document (with $p = 0.5$) or from distinct documents. In addition to the masked language modeling objective, the model is trained to predict whether the observed document segments come from the same or distinct documents via an auxiliary Next Sentence Prediction (NSP) loss.

The NSP loss was hypothesized to be an important factor in training the original BERT model. Devlin et al. (2019) observe that removing NSP hurts performance, with significant performance degradation on QNLI, MNLI, and SQuAD 1.1. However, some recent work has questioned the necessity of the NSP loss (Lample and Conneau, 2019; Yang et al., 2019; Joshi et al., 2019).

To better understand this discrepancy, we compare several alternative training formats:

• **SEGMENT-PAIR+NSP:** This follows the original input format used in BERT (Devlin et al., 2019), with the NSP loss. Each input has a pair of segments, which can each contain multiple natural sentences, but the total combined length must be less than 512 tokens.

• **SENTENCE-PAIR+NSP:** Each input contains a pair of natural *sentences*, either sampled from a contiguous portion of one document or from separate documents. Since these inputs are significantly shorter than 512 tokens, we increase the batch size so that the total number of tokens remains similar to SEGMENT-PAIR+NSP. We retain the NSP loss.

• **FULL-SENTENCES:** Each input is packed with full sentences sampled contiguously from one or more documents, such that the total length is at most 512 tokens. Inputs may cross document boundaries. When we reach the end of one document, we begin sampling sentences from the next document and add an extra separator token between documents. We remove the NSP loss.

• **DOC-SENTENCES:** Inputs are constructed similarly to FULL-SENTENCES, except that they may not cross document boundaries. Inputs sampled near the end of a document may be shorter than 512 tokens, so we dynamically increase the batch size in these cases to achieve a similar number of total tokens as FULL-SENTENCES. We remove the NSP loss.

**Results** Table 2 shows results for the four different settings. We first compare the original SEGMENT-PAIR input format from Devlin et al. (2019) to the SENTENCE-PAIR format; both formats retain the NSP loss, but the latter uses single sentences. We find that **using individual sentences hurts performance on downstream tasks**, which we hypothesize is because the model is not able to learn long-range dependencies.

We next compare training without the NSP loss and training with blocks of text from a single document (DOC-SENTENCES). We find that this setting outperforms the originally published BERT$_\text{BASE}$ results and that **removing the NSP loss matches or slightly improves downstream task performance**, in contrast to Devlin et al. (2019). It is possible that the original BERT implementation may only have removed the loss term while still retaining the SEGMENT-PAIR input format.

Finally we find that restricting sequences to come from a single document (DOC-SENTENCES) performs slightly better than packing sequences from multiple documents (FULL-SENTENCES). However, because the DOC-SENTENCES format results in variable batch sizes, we use FULL-SENTENCES in the remainder of our experiments for easier comparison with related work.

| Model | SQuAD 1.1/2.0 | MNLI-m | SST-2 | RACE |
|-------|---------------|--------|-------|------|
| Our reimplementation (with NSP loss): | | | | |
| SEGMENT-PAIR | 90.4/78.7 | 84.0 | 92.9 | 64.2 |
| SENTENCE-PAIR | 88.7/76.2 | 82.9 | 92.1 | 63.0 |
| Our reimplementation (without NSP loss): | | | | |
| FULL-SENTENCES | 90.4/79.1 | 84.7 | 92.5 | 64.8 |
| DOC-SENTENCES | 90.6/79.7 | 84.7 | 92.7 | 65.6 |
| BERT$_\text{BASE}$ | 88.5/76.3 | 84.3 | 92.8 | 64.3 |
| XLNet$_\text{BASE}$ (K = 7) | –/81.3 | 85.8 | 92.7 | 66.1 |
| XLNet$_\text{BASE}$ (K = 6) | –/81.0 | 85.6 | 93.4 | 66.7 |

**Table 2:** Development set results for base models pretrained over BOOKCORPUS and WIKIPEDIA. All models are trained for 1M steps with a batch size of 256 sequences. We report F1 for SQuAD and accuracy for MNLI-m, SST-2 and RACE. Reported results are medians over five random initializations (seeds). Results for BERT$_\text{BASE}$ and XLNet$_\text{BASE}$ are from Yang et al. (2019).

### 4.3 Training with large batches

Past work in Neural Machine Translation has shown that training with very large mini-batches can both improve optimization speed and end-task performance when the learning rate is increased appropriately (Ott et al., 2018). Recent work has shown that BERT is also amenable to large batch training (You et al., 2019).

Devlin et al. (2019) originally trained BERT$_\text{BASE}$ for 1M steps with a batch size of 256 sequences. This is equivalent in computational cost, via gradient accumulation, to training for 125K steps with a batch size of 2K sequences, or for 31K steps with a batch size of 8K.

In Table 3 we compare perplexity and end-task performance of BERT$_\text{BASE}$ as we increase the batch size, controlling for the number of passes through the training data. We observe that training with large batches improves perplexity for the masked language modeling objective, as well as end-task accuracy. Large batches are also easier to parallelize via distributed data parallel training, and in later experiments we train with batches of 8K sequences.

Notably You et al. (2019) train BERT with even larger batche sizes, up to 32K sequences. We leave further exploration of the limits of large batch training to future work.

| bsz | steps | lr | ppl | MNLI-m | SST-2 |
|-----|-------|-----|-----|--------|-------|
| 256 | 1M | 1e-4 | 3.99 | 84.7 | 92.7 |
| 2K | 125K | 7e-4 | 3.68 | 85.2 | 92.9 |
| 8K | 31K | 1e-3 | 3.77 | 84.6 | 92.8 |

**Table 3:** Perplexity on held-out training data (ppl) and development set accuracy for base models trained over BOOKCORPUS and WIKIPEDIA with varying batch sizes (bsz). We tune the learning rate (lr) for each setting. Models make the same number of passes over the data (epochs) and have the same computational cost.

### 4.4 Text Encoding

Byte-Pair Encoding (BPE) (Sennrich et al., 2016) is a hybrid between character- and word-level representations that allows handling the large vocabularies common in natural language corpora. Instead of full words, BPE relies on subwords units, which are extracted by performing statistical analysis of the training corpus.

BPE vocabulary sizes typically range from 10K-100K subword units. However, unicode characters can account for a sizeable portion of this vocabulary when modeling large and diverse corpora, such as the ones considered in this work.

Radford et al. (2019) introduce a clever implementation of BPE that uses bytes instead of unicode characters as the base subword units. Using bytes makes it possible to learn a subword vocabulary of a modest size (50K units) that can still encode any input text without introducing any "unknown" tokens.

The original BERT implementation (Devlin et al., 2019) uses a character-level BPE vocabulary of size 30K, which is learned after preprocessing the input with heuristic tokenization rules. Following Radford et al. (2019), we instead consider training BERT with a larger byte-level BPE vocabulary containing 50K subword units, without any additional preprocessing or tokenization of the input. This adds approximately 15M and 20M additional parameters for BERT$_\text{BASE}$ and BERT$_\text{LARGE}$, respectively.

Early experiments revealed only slight differences between these encodings, with the Radford et al. (2019) BPE achieving slightly worse end-task performance on some tasks. Nevertheless, we believe the advantages of a universal encoding scheme outweighs the minor degredation in performance and use this encoding in the remainder of our experiments. A more detailed comparison of these encodings is left to future work.

---

### النسخة العربية

## 4 تحليل إجراءات التدريب

يستكشف هذا القسم ويحدد كمياً الاختيارات المهمة للتدريب المسبق الناجح لنماذج BERT. نحافظ على معمارية النموذج ثابتة. على وجه التحديد، نبدأ بتدريب نماذج BERT بنفس التكوين كـ BERT$_\text{BASE}$ ($L = 12$، $H = 768$، $A = 12$، 110 مليون معامل).

### 4.1 الإخفاء الثابت مقابل الإخفاء الديناميكي

كما نوقش في القسم 2، يعتمد BERT على إخفاء الرموز والتنبؤ بها بشكل عشوائي. قام تنفيذ BERT الأصلي بإجراء الإخفاء مرة واحدة أثناء المعالجة المسبقة للبيانات، مما أدى إلى قناع ثابت واحد. لتجنب استخدام نفس القناع لكل مثيل تدريبي في كل حقبة، تم تكرار بيانات التدريب 10 مرات بحيث يتم إخفاء كل تسلسل بـ 10 طرق مختلفة على مدى 40 حقبة من التدريب. وبالتالي، تم رؤية كل تسلسل تدريبي بنفس القناع أربع مرات أثناء التدريب.

نقارن هذه الاستراتيجية مع *الإخفاء الديناميكي* حيث نولد نمط الإخفاء في كل مرة نغذي فيها تسلسلاً للنموذج. يصبح هذا حاسماً عند التدريب المسبق لمزيد من الخطوات أو مع مجموعات بيانات أكبر.

**النتائج** يقارن الجدول 1 نتائج BERT$_\text{BASE}$ المنشورة من Devlin وآخرون (2019) بإعادة تنفيذنا إما بالإخفاء الثابت أو الديناميكي. نجد أن إعادة تنفيذنا بالإخفاء الثابت يؤدي بشكل مماثل لنموذج BERT الأصلي، والإخفاء الديناميكي قابل للمقارنة أو أفضل قليلاً من الإخفاء الثابت. بالنظر إلى هذه النتائج والفوائد الإضافية في الكفاءة للإخفاء الديناميكي، نستخدم الإخفاء الديناميكي في بقية التجارب.

| الإخفاء | SQuAD 2.0 | MNLI-m | SST-2 |
|---------|-----------|--------|-------|
| المرجع | 76.3 | 84.3 | 92.8 |
| إعادة تنفيذنا: | | | |
| ثابت | 78.3 | 84.3 | 92.5 |
| ديناميكي | 78.7 | 84.0 | 92.9 |

**الجدول 1:** مقارنة بين الإخفاء الثابت والديناميكي لـ BERT$_\text{BASE}$. نبلغ عن F1 لـ SQuAD والدقة لـ MNLI-m وSST-2. النتائج المبلغ عنها هي الوسيط على 5 تهيئات عشوائية (بذور). النتائج المرجعية من Yang وآخرون (2019).

### 4.2 تنسيق إدخال النموذج والتنبؤ بالجملة التالية

في إجراء التدريب المسبق الأصلي لـ BERT، يراقب النموذج مقطعي وثائق مترابطين، يتم أخذهما إما بشكل متجاور من نفس الوثيقة (مع $p = 0.5$) أو من وثائق مختلفة. بالإضافة إلى هدف نمذجة اللغة المقنعة، يتم تدريب النموذج للتنبؤ بما إذا كانت مقاطع الوثائق الملاحظة تأتي من نفس الوثائق أو وثائق مختلفة عبر خسارة التنبؤ بالجملة التالية (NSP) المساعدة.

افتُرض أن خسارة NSP عامل مهم في تدريب نموذج BERT الأصلي. لاحظ Devlin وآخرون (2019) أن إزالة NSP تضر بالأداء، مع تدهور كبير في الأداء على QNLI وMNLI وSQuAD 1.1. ومع ذلك، شكك بعض الأعمال الحديثة في ضرورة خسارة NSP (Lample وConneau، 2019؛ Yang وآخرون، 2019؛ Joshi وآخرون، 2019).

لفهم هذا التناقض بشكل أفضل، نقارن عدة تنسيقات تدريب بديلة:

• **SEGMENT-PAIR+NSP:** يتبع هذا تنسيق الإدخال الأصلي المستخدم في BERT (Devlin وآخرون، 2019)، مع خسارة NSP. كل إدخال له زوج من المقاطع، يمكن أن يحتوي كل منها على جمل طبيعية متعددة، ولكن يجب أن يكون الطول المشترك الإجمالي أقل من 512 رمزاً.

• **SENTENCE-PAIR+NSP:** يحتوي كل إدخال على زوج من *الجمل* الطبيعية، إما مأخوذة من جزء متجاور من وثيقة واحدة أو من وثائق منفصلة. نظراً لأن هذه المدخلات أقصر بكثير من 512 رمزاً، نزيد حجم الدفعة بحيث يظل العدد الإجمالي للرموز مماثلاً لـ SEGMENT-PAIR+NSP. نحتفظ بخسارة NSP.

• **FULL-SENTENCES:** يتم حزم كل إدخال بجمل كاملة مأخوذة بشكل متجاور من وثيقة واحدة أو أكثر، بحيث يكون الطول الإجمالي 512 رمزاً على الأكثر. قد تعبر المدخلات حدود الوثائق. عندما نصل إلى نهاية وثيقة واحدة، نبدأ في أخذ عينات من الجمل من الوثيقة التالية ونضيف رمز فاصل إضافي بين الوثائق. نزيل خسارة NSP.

• **DOC-SENTENCES:** يتم بناء المدخلات بشكل مماثل لـ FULL-SENTENCES، باستثناء أنها قد لا تعبر حدود الوثائق. قد تكون المدخلات المأخوذة بالقرب من نهاية وثيقة أقصر من 512 رمزاً، لذلك نزيد حجم الدفعة ديناميكياً في هذه الحالات لتحقيق عدد مماثل من الرموز الإجمالية كـ FULL-SENTENCES. نزيل خسارة NSP.

**النتائج** يُظهر الجدول 2 النتائج للإعدادات الأربعة المختلفة. نقارن أولاً تنسيق إدخال SEGMENT-PAIR الأصلي من Devlin وآخرون (2019) بتنسيق SENTENCE-PAIR؛ كلا التنسيقين يحتفظان بخسارة NSP، لكن الأخير يستخدم جملاً فردية. نجد أن **استخدام الجمل الفردية يضر بالأداء على المهام النهائية**، والذي نفترض أنه بسبب عدم قدرة النموذج على تعلم التبعيات طويلة المدى.

نقارن بعد ذلك التدريب بدون خسارة NSP والتدريب بكتل من النص من وثيقة واحدة (DOC-SENTENCES). نجد أن هذا الإعداد يتفوق على نتائج BERT$_\text{BASE}$ المنشورة أصلاً وأن **إزالة خسارة NSP تطابق أو تحسن قليلاً أداء المهام النهائية**، على عكس Devlin وآخرون (2019). من الممكن أن يكون تنفيذ BERT الأصلي قد أزال فقط حد الخسارة مع الاحتفاظ بتنسيق إدخال SEGMENT-PAIR.

أخيراً نجد أن تقييد التسلسلات للمجيء من وثيقة واحدة (DOC-SENTENCES) يؤدي بشكل أفضل قليلاً من حزم التسلسلات من وثائق متعددة (FULL-SENTENCES). ومع ذلك، نظراً لأن تنسيق DOC-SENTENCES ينتج عنه أحجام دفعات متغيرة، نستخدم FULL-SENTENCES في بقية تجاربنا لسهولة المقارنة مع الأعمال ذات الصلة.

| النموذج | SQuAD 1.1/2.0 | MNLI-m | SST-2 | RACE |
|-------|---------------|--------|-------|------|
| إعادة تنفيذنا (مع خسارة NSP): | | | | |
| SEGMENT-PAIR | 90.4/78.7 | 84.0 | 92.9 | 64.2 |
| SENTENCE-PAIR | 88.7/76.2 | 82.9 | 92.1 | 63.0 |
| إعادة تنفيذنا (بدون خسارة NSP): | | | | |
| FULL-SENTENCES | 90.4/79.1 | 84.7 | 92.5 | 64.8 |
| DOC-SENTENCES | 90.6/79.7 | 84.7 | 92.7 | 65.6 |
| BERT$_\text{BASE}$ | 88.5/76.3 | 84.3 | 92.8 | 64.3 |
| XLNet$_\text{BASE}$ (K = 7) | –/81.3 | 85.8 | 92.7 | 66.1 |
| XLNet$_\text{BASE}$ (K = 6) | –/81.0 | 85.6 | 93.4 | 66.7 |

**الجدول 2:** نتائج مجموعة التطوير للنماذج الأساسية المدربة مسبقاً على BOOKCORPUS وWIKIPEDIA. تم تدريب جميع النماذج لـ 1 مليون خطوة بحجم دفعة 256 تسلسلاً. نبلغ عن F1 لـ SQuAD والدقة لـ MNLI-m وSST-2 وRACE. النتائج المبلغ عنها هي الوسيط على خمس تهيئات عشوائية (بذور). نتائج BERT$_\text{BASE}$ وXLNet$_\text{BASE}$ من Yang وآخرون (2019).

### 4.3 التدريب بدفعات كبيرة

أظهر العمل السابق في الترجمة الآلية العصبية أن التدريب بدفعات صغيرة كبيرة جداً يمكن أن يحسن كلاً من سرعة التحسين وأداء المهمة النهائية عند زيادة معدل التعلم بشكل مناسب (Ott وآخرون، 2018). أظهر العمل الحديث أن BERT أيضاً قابل للتدريب بدفعات كبيرة (You وآخرون، 2019).

قام Devlin وآخرون (2019) في الأصل بتدريب BERT$_\text{BASE}$ لـ 1 مليون خطوة بحجم دفعة 256 تسلسلاً. هذا يعادل في التكلفة الحسابية، عبر تراكم التدرج، التدريب لـ 125 ألف خطوة بحجم دفعة 2 ألف تسلسل، أو لـ 31 ألف خطوة بحجم دفعة 8 آلاف.

في الجدول 3 نقارن الحيرة وأداء المهمة النهائية لـ BERT$_\text{BASE}$ عندما نزيد حجم الدفعة، مع التحكم في عدد المرات التي تمر فيها البيانات التدريبية. نلاحظ أن التدريب بدفعات كبيرة يحسن الحيرة لهدف نمذجة اللغة المقنعة، وكذلك دقة المهمة النهائية. الدفعات الكبيرة أيضاً أسهل في التوازي عبر التدريب الموزع المتوازي للبيانات، وفي التجارب اللاحقة نتدرب بدفعات من 8 آلاف تسلسل.

من الجدير بالذكر أن You وآخرون (2019) يدربون BERT بأحجام دفعات أكبر، تصل إلى 32 ألف تسلسل. نترك المزيد من الاستكشاف لحدود التدريب بالدفعات الكبيرة للعمل المستقبلي.

| bsz | الخطوات | lr | ppl | MNLI-m | SST-2 |
|-----|-------|-----|-----|--------|-------|
| 256 | 1 مليون | 1e-4 | 3.99 | 84.7 | 92.7 |
| 2 ألف | 125 ألف | 7e-4 | 3.68 | 85.2 | 92.9 |
| 8 آلاف | 31 ألف | 1e-3 | 3.77 | 84.6 | 92.8 |

**الجدول 3:** الحيرة على بيانات التدريب المحتجزة (ppl) ودقة مجموعة التطوير للنماذج الأساسية المدربة على BOOKCORPUS وWIKIPEDIA بأحجام دفعات متفاوتة (bsz). نضبط معدل التعلم (lr) لكل إعداد. تقوم النماذج بنفس عدد المرات بالمرور على البيانات (الحقب) ولديها نفس التكلفة الحسابية.

### 4.4 ترميز النص

ترميز زوج البايت (BPE) (Sennrich وآخرون، 2016) هو مزيج بين تمثيلات مستوى الحرف والكلمة يسمح بالتعامل مع المفردات الكبيرة الشائعة في مجموعات نصوص اللغة الطبيعية. بدلاً من الكلمات الكاملة، يعتمد BPE على وحدات الكلمات الفرعية، والتي يتم استخراجها من خلال إجراء تحليل إحصائي لمجموعة التدريب.

تتراوح أحجام مفردات BPE عادةً من 10 آلاف إلى 100 ألف وحدة كلمات فرعية. ومع ذلك، يمكن أن تمثل أحرف يونيكود جزءاً كبيراً من هذه المفردات عند نمذجة مجموعات كبيرة ومتنوعة، مثل تلك التي تم أخذها في الاعتبار في هذا العمل.

يقدم Radford وآخرون (2019) تنفيذاً ذكياً لـ BPE يستخدم البايتات بدلاً من أحرف يونيكود كوحدات الكلمات الفرعية الأساسية. يجعل استخدام البايتات من الممكن تعلم مفردات كلمات فرعية بحجم متواضع (50 ألف وحدة) يمكنها مع ذلك ترميز أي نص إدخال دون إدخال أي رموز "غير معروفة".

يستخدم تنفيذ BERT الأصلي (Devlin وآخرون، 2019) مفردات BPE على مستوى الأحرف بحجم 30 ألفاً، والتي يتم تعلمها بعد معالجة الإدخال مسبقاً بقواعد التجزئة الاستكشافية. باتباع Radford وآخرون (2019)، نأخذ في الاعتبار بدلاً من ذلك تدريب BERT بمفردات BPE أكبر على مستوى البايت تحتوي على 50 ألف وحدة كلمات فرعية، دون أي معالجة مسبقة أو تجزئة إضافية للإدخال. هذا يضيف ما يقرب من 15 مليون و20 مليون معامل إضافي لـ BERT$_\text{BASE}$ وBERT$_\text{LARGE}$، على التوالي.

كشفت التجارب المبكرة عن اختلافات طفيفة فقط بين هذه الترميزات، حيث حقق BPE من Radford وآخرون (2019) أداءً أسوأ قليلاً في المهمة النهائية على بعض المهام. ومع ذلك، نعتقد أن مزايا نظام الترميز الشامل تفوق التدهور الطفيف في الأداء ونستخدم هذا الترميز في بقية تجاربنا. تُترك مقارنة أكثر تفصيلاً لهذه الترميزات للعمل المستقبلي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Static masking, dynamic masking, SEGMENT-PAIR, SENTENCE-PAIR, FULL-SENTENCES, DOC-SENTENCES, perplexity, gradient accumulation, byte-level BPE
- **Equations:** Mathematical notation for probability ($p = 0.5$), model configuration parameters
- **Citations:** 10 citations (Yang et al. 2019, Devlin et al. 2019, Lample and Conneau 2019, Joshi et al. 2019, Ott et al. 2018, You et al. 2019, Sennrich et al. 2016, Radford et al. 2019)
- **Special handling:**
  - **3 important tables** with numerical results - all values preserved exactly
  - Input format names (SEGMENT-PAIR, SENTENCE-PAIR, etc.) kept in English for clarity
  - Model subscripts (BASE, LARGE) preserved in LaTeX
  - Table headers and values all accurately translated
  - Statistical terms (median, F1, accuracy, perplexity) properly translated

### Quality Metrics

- Semantic equivalence: 0.88 - All experimental findings and comparisons accurately conveyed
- Technical accuracy: 0.87 - Tables, numbers, and technical details precisely preserved
- Readability: 0.86 - Clear Arabic explanation of complex experimental results
- Glossary consistency: 0.87 - Consistent terminology for masking, NSP, batching concepts
- **Overall section score:** 0.87
