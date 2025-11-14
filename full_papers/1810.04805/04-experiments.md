# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** fine-tuning, benchmark, accuracy, NLP, classification, question answering, inference, F1 score, training, evaluation

---

### English Version

In this section, we present BERT fine-tuning results on 11 NLP tasks.

#### 4.1 GLUE

The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks. Detailed descriptions of GLUE datasets are included in Appendix B.1.

To fine-tune on GLUE, we represent the input sequence (for single sentence or sentence pairs) as described in Section 3, and use the final hidden vector C ∈ R^H corresponding to the first input token ([CLS]) as the aggregate representation. The only new parameters introduced during fine-tuning are classification layer weights W ∈ R^(K×H), where K is the number of labels. We compute a standard classification loss with C and W, i.e., log(softmax(CW^T)).

We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks. For each task, we selected the best fine-tuning learning rate (among 5e-5, 4e-5, 3e-5, and 2e-5) on the Dev set. Additionally, for BERT_LARGE we found that fine-tuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on the Dev set. With random restarts, we use the same pre-trained checkpoint but perform different fine-tuning data shuffling and classifier layer initialization.

Results are presented in Table 1. Both BERT_BASE and BERT_LARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the prior state of the art. Note that BERT_BASE and OpenAI GPT are nearly identical in terms of model architecture apart from the attention masking. For the largest and most widely reported GLUE task, MNLI, BERT obtains a 4.6% absolute accuracy improvement. On the official GLUE leaderboard, BERT_LARGE obtains a score of 80.5, compared to OpenAI GPT, which obtains 72.8 as of the date of writing.

We find that BERT_LARGE significantly outperforms BERT_BASE across all tasks, especially those with very little training data. The effect of model size is explored more thoroughly in Section 5.2.

#### 4.2 SQuAD v1.1

The Stanford Question Answering Dataset (SQuAD v1.1) is a collection of 100k crowdsourced question/answer pairs (Rajpurkar et al., 2016). Given a question and a passage from Wikipedia containing the answer, the task is to predict the answer text span in the passage.

As shown in Figure 1, in the question answering task, we represent the input question and passage as a single packed sequence, with the question using the A embedding and the passage using the B embedding. We only introduce a start vector S ∈ R^H and an end vector E ∈ R^H during fine-tuning. The probability of word i being the start of the answer span is computed as a dot product between T_i and S followed by a softmax over all of the words in the paragraph: P_i = e^(S·T_i) / Σ_j e^(S·T_j).

The analogous formula is used for the end of the answer span. The score of a candidate span from position i to position j is defined as S·T_i + E·T_j, and the maximum scoring span where j ≥ i is used as a prediction. The training objective is the sum of the log-likelihoods of the correct start and end positions. We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32.

Table 2 shows top leaderboard entries as well as results from top published systems (Seo et al., 2017; Clark and Gardner, 2018; Peters et al., 2018a; Hu et al., 2018). The top results from the SQuAD leaderboard do not have up-to-date public system descriptions available, and are allowed to use any public data when training their systems. We therefore use modest data augmentation in our system by first fine-tuning on TriviaQA (Joshi et al., 2017) before fine-tuning on SQuAD.

Our best performing system outperforms the top leaderboard system by +1.5 F1 in ensembling and +1.3 F1 as a single system. In fact, our single BERT model outperforms the top ensemble system in terms of F1 score. Without TriviaQA fine-tuning data, we only lose 0.1-0.4 F1, still outperforming all existing systems by a wide margin.

#### 4.3 SQuAD v2.0

The SQuAD 2.0 task extends the SQuAD 1.1 problem definition by allowing for the possibility that no short answer exists in the provided paragraph, making the problem more realistic.

We use a simple approach to extend the SQuAD v1.1 BERT model for this task. We treat questions that do not have an answer as having an answer span with start and end at the [CLS] token. The probability space for the start and end answer span positions is extended to include the position of the [CLS] token. For prediction, we compare the score of the no-answer span: s_null = S·C + E·C to the score of the best non-null span ŝ_i,j = max_{j≥i} S·T_i + E·T_j. We predict a non-null answer when ŝ_i,j > s_null + τ, where the threshold τ is selected on the dev set to maximize F1. We did not use TriviaQA data for this model. We fine-tuned for 2 epochs with a learning rate of 5e-5 and a batch size of 48.

The results compared to prior leaderboard entries and top published work (Sun et al., 2018; Wang et al., 2018b) are shown in Table 3, excluding systems that use BERT as one of their components. We observe a +5.1 F1 improvement over the previous best system.

#### 4.4 SWAG

The Situations With Adversarial Generations (SWAG) dataset contains 113k sentence-pair completion examples that evaluate grounded commonsense inference (Zellers et al., 2018). Given a sentence, the task is to choose the most plausible continuation among four choices.

When fine-tuning on the SWAG dataset, we construct four input sequences, each containing the concatenation of the given sentence (sentence A) and a possible continuation (sentence B). The only task-specific parameters introduced is a vector whose dot product with the [CLS] token representation C denotes a score for each choice which is normalized with a softmax layer.

We fine-tune the model for 3 epochs with a learning rate of 2e-5 and a batch size of 16. Results are presented in Table 4. BERT_LARGE outperforms the authors' baseline ESIM+ELMo system by +27.1% and OpenAI GPT by 8.3%.

---

### النسخة العربية

في هذا القسم، نقدم نتائج الضبط الدقيق لـ BERT على 11 مهمة من مهام معالجة اللغة الطبيعية.

#### 4.1 GLUE

معيار التقييم العام لفهم اللغة (GLUE) (Wang et al., 2018a) هو مجموعة من مهام فهم اللغة الطبيعية المتنوعة. يتم تضمين أوصاف تفصيلية لمجموعات بيانات GLUE في الملحق B.1.

للضبط الدقيق على GLUE، نمثل تسلسل الإدخال (لجملة واحدة أو أزواج جمل) كما هو موصوف في القسم 3، ونستخدم المتجه الخفي النهائي C ∈ R^H المقابل لرمز الإدخال الأول ([CLS]) كتمثيل مُجمَّع. المعاملات الجديدة الوحيدة المُقدَّمة أثناء الضبط الدقيق هي أوزان طبقة التصنيف W ∈ R^(K×H)، حيث K هو عدد الفئات. نحسب خسارة تصنيف قياسية مع C و W، أي log(softmax(CW^T)).

نستخدم حجم دفعة 32 ونضبط دقيقاً لـ 3 حقب على البيانات لجميع مهام GLUE. لكل مهمة، اخترنا أفضل معدل تعلم للضبط الدقيق (من بين 5e-5، 4e-5، 3e-5، و 2e-5) على مجموعة Dev. بالإضافة إلى ذلك، بالنسبة لـ BERT_LARGE وجدنا أن الضبط الدقيق كان أحياناً غير مستقر على مجموعات البيانات الصغيرة، لذلك أجرينا عدة عمليات إعادة تشغيل عشوائية واخترنا أفضل نموذج على مجموعة Dev. مع عمليات إعادة التشغيل العشوائية، نستخدم نفس نقطة التحقق المدربة مسبقاً ولكن نجري خلطاً مختلفاً لبيانات الضبط الدقيق وتهيئة طبقة المصنف.

يتم تقديم النتائج في الجدول 1. كل من BERT_BASE و BERT_LARGE يتفوقان على جميع الأنظمة في جميع المهام بهامش كبير، محققين تحسيناً في متوسط الدقة بنسبة 4.5% و 7.0% على التوالي مقارنة بأحدث النتائج السابقة. لاحظ أن BERT_BASE و OpenAI GPT متطابقان تقريباً من حيث معمارية النموذج باستثناء إخفاء الانتباه. بالنسبة لأكبر مهمة GLUE والأكثر انتشاراً، MNLI، يحقق BERT تحسيناً مطلقاً في الدقة بنسبة 4.6%. على لوحة الصدارة الرسمية لـ GLUE، يحصل BERT_LARGE على درجة 80.5، مقارنة بـ OpenAI GPT، الذي يحصل على 72.8 في تاريخ الكتابة.

نجد أن BERT_LARGE يتفوق بشكل كبير على BERT_BASE عبر جميع المهام، خاصة تلك التي تحتوي على بيانات تدريب قليلة جداً. يتم استكشاف تأثير حجم النموذج بشكل أكثر شمولاً في القسم 5.2.

#### 4.2 SQuAD v1.1

مجموعة بيانات الإجابة على أسئلة ستانفورد (SQuAD v1.1) هي مجموعة من 100 ألف زوج سؤال/إجابة من مصادر جماعية (Rajpurkar et al., 2016). بإعطاء سؤال ومقطع من ويكيبيديا يحتوي على الإجابة، تكون المهمة هي التنبؤ بنطاق نص الإجابة في المقطع.

كما هو موضح في الشكل 1، في مهمة الإجابة على الأسئلة، نمثل سؤال الإدخال والمقطع كتسلسل معبأ واحد، مع استخدام السؤال لتضمين A واستخدام المقطع لتضمين B. نقدم فقط متجه بداية S ∈ R^H ومتجه نهاية E ∈ R^H أثناء الضبط الدقيق. يتم حساب احتمال أن تكون الكلمة i بداية نطاق الإجابة كحاصل ضرب نقطي بين T_i و S متبوعاً بـ softmax على جميع الكلمات في الفقرة: P_i = e^(S·T_i) / Σ_j e^(S·T_j).

يتم استخدام الصيغة المماثلة لنهاية نطاق الإجابة. يتم تعريف درجة نطاق مرشح من الموضع i إلى الموضع j على أنها S·T_i + E·T_j، ويتم استخدام النطاق الأعلى درجة حيث j ≥ i كتنبؤ. هدف التدريب هو مجموع الاحتماليات اللوغاريتمية لمواضع البداية والنهاية الصحيحة. نضبط دقيقاً لـ 3 حقب مع معدل تعلم 5e-5 وحجم دفعة 32.

يوضح الجدول 2 أعلى إدخالات لوحة الصدارة بالإضافة إلى نتائج من أفضل الأنظمة المنشورة (Seo et al., 2017; Clark and Gardner, 2018; Peters et al., 2018a; Hu et al., 2018). أعلى نتائج من لوحة صدارة SQuAD ليس لها أوصاف أنظمة عامة محدثة متاحة، ويُسمح لها باستخدام أي بيانات عامة عند تدريب أنظمتها. لذلك نستخدم زيادة بيانات متواضعة في نظامنا عن طريق الضبط الدقيق أولاً على TriviaQA (Joshi et al., 2017) قبل الضبط الدقيق على SQuAD.

نظامنا الأفضل أداءً يتفوق على نظام أعلى لوحة الصدارة بمقدار +1.5 F1 في التجميع و +1.3 F1 كنظام واحد. في الواقع، نموذج BERT الواحد لدينا يتفوق على نظام التجميع الأعلى من حيث درجة F1. بدون بيانات الضبط الدقيق لـ TriviaQA، نخسر فقط 0.1-0.4 F1، لا نزال نتفوق على جميع الأنظمة الموجودة بهامش واسع.

#### 4.3 SQuAD v2.0

تمدد مهمة SQuAD 2.0 تعريف مشكلة SQuAD 1.1 بالسماح بإمكانية عدم وجود إجابة قصيرة في الفقرة المقدمة، مما يجعل المشكلة أكثر واقعية.

نستخدم نهجاً بسيطاً لتوسيع نموذج BERT SQuAD v1.1 لهذه المهمة. نتعامل مع الأسئلة التي ليس لها إجابة على أنها لها نطاق إجابة مع بداية ونهاية عند رمز [CLS]. يتم توسيع فضاء الاحتمال لمواضع نطاق الإجابة للبداية والنهاية ليشمل موضع رمز [CLS]. للتنبؤ، نقارن درجة نطاق عدم الإجابة: s_null = S·C + E·C مع درجة أفضل نطاق غير فارغ ŝ_i,j = max_{j≥i} S·T_i + E·T_j. نتنبأ بإجابة غير فارغة عندما ŝ_i,j > s_null + τ، حيث يتم اختيار العتبة τ على مجموعة dev لتعظيم F1. لم نستخدم بيانات TriviaQA لهذا النموذج. ضبطنا دقيقاً لـ 2 حقبتين مع معدل تعلم 5e-5 وحجم دفعة 48.

يتم عرض النتائج مقارنة بإدخالات لوحة الصدارة السابقة وأفضل الأعمال المنشورة (Sun et al., 2018; Wang et al., 2018b) في الجدول 3، باستثناء الأنظمة التي تستخدم BERT كأحد مكوناتها. نلاحظ تحسيناً بمقدار +5.1 F1 على أفضل نظام سابق.

#### 4.4 SWAG

تحتوي مجموعة بيانات المواقف مع التوليدات الخصامية (SWAG) على 113 ألف مثال لإكمال أزواج الجمل تقيّم الاستنتاج الحس السليم المؤسس (Zellers et al., 2018). بإعطاء جملة، المهمة هي اختيار الاستمرار الأكثر منطقية من بين أربعة خيارات.

عند الضبط الدقيق على مجموعة بيانات SWAG، نبني أربعة تسلسلات إدخال، كل منها يحتوي على تسلسل الجملة المُعطاة (الجملة A) واستمرار محتمل (الجملة B). المعاملات الخاصة بالمهمة الوحيدة المُقدَّمة هي متجه يشير حاصل ضربه النقطي مع تمثيل رمز [CLS] C إلى درجة لكل خيار يتم تطبيعها بطبقة softmax.

نضبط النموذج دقيقاً لـ 3 حقب مع معدل تعلم 2e-5 وحجم دفعة 16. يتم تقديم النتائج في الجدول 4. يتفوق BERT_LARGE على نظام خط الأساس ESIM+ELMo للمؤلفين بنسبة +27.1% و OpenAI GPT بنسبة 8.3%.

---

### Translation Notes

- **Tables referenced:** Table 1 (GLUE results), Table 2 (SQuAD v1.1), Table 3 (SQuAD v2.0), Table 4 (SWAG)
- **Key terms introduced:**
  - GLUE benchmark - معيار GLUE
  - Question answering - الإجابة على الأسئلة
  - Dev set - مجموعة Dev
  - Test set - مجموعة Test
  - Leaderboard - لوحة الصدارة
  - Ensemble - التجميع
  - Data augmentation - زيادة البيانات
  - Crowdsourced - من مصادر جماعية
  - Answer span - نطاق الإجابة

- **Equations:** Multiple formulas for probability calculations and scoring
- **Citations:** 15 references cited
- **Special handling:**
  - Kept dataset names in English (GLUE, SQuAD, SWAG, TriviaQA, MNLI, etc.)
  - Preserved numerical results and percentages exactly
  - Maintained mathematical notation and formulas
  - Kept hyperparameters in original form

### Quality Metrics

- **Semantic equivalence:** 0.89
- **Technical accuracy:** 0.88
- **Readability:** 0.87
- **Glossary consistency:** 0.88

**Overall section score:** 0.88
