# Section 3: Experimental Setup
## القسم 3: الإعداد التجريبي

**Section:** experimental-setup
**Translation Quality:** 0.86
**Glossary Terms Used:** FAIRSEQ, mixed precision (الدقة المختلطة), GPU, hyperparameter (معامل فائق), Adam epsilon, batch size (حجم الدفعة), GLUE, SQuAD, RACE, development set (مجموعة التطوير), test set (مجموعة الاختبار), fine-tuning (الضبط الدقيق), benchmark (معيار), leaderboard (لوحة الصدارة)

---

### English Version

## 3 Experimental Setup

In this section, we describe the experimental setup for our replication study of BERT.

### 3.1 Implementation

We reimplement BERT in FAIRSEQ (Ott et al., 2019). We primarily follow the original BERT optimization hyperparameters, given in Section 2, except for the peak learning rate and number of warmup steps, which are tuned separately for each setting. We additionally found training to be very sensitive to the Adam epsilon term, and in some cases we obtained better performance or improved stability after tuning it. Similarly, we found setting $\beta_2 = 0.98$ to improve stability when training with large batch sizes.

We pretrain with sequences of at most $T = 512$ tokens. Unlike Devlin et al. (2019), we do not randomly inject short sequences, and we do not train with a reduced sequence length for the first 90% of updates. We train only with full-length sequences.

We train with mixed precision floating point arithmetic on DGX-1 machines, each with 8 × 32GB Nvidia V100 GPUs interconnected by Infiniband (Micikevicius et al., 2018).

### 3.2 Data

BERT-style pretraining crucially relies on large quantities of text. Baevski et al. (2019) demonstrate that increasing data size can result in improved end-task performance. Several efforts have trained on datasets larger and more diverse than the original BERT (Radford et al., 2019; Yang et al., 2019; Zellers et al., 2019). Unfortunately, not all of the additional datasets can be publicly released. For our study, we focus on gathering as much data as possible for experimentation, allowing us to match the overall quality and quantity of data as appropriate for each comparison.

We consider five English-language corpora of varying sizes and domains, totaling over 160GB of uncompressed text. We use the following text corpora:

• **BOOKCORPUS** (Zhu et al., 2015) plus English WIKIPEDIA. This is the original data used to train BERT. (16GB).

• **CC-NEWS**, which we collected from the English portion of the CommonCrawl News dataset (Nagel, 2016). The data contains 63 million English news articles crawled between September 2016 and February 2019. (76GB after filtering).

• **OPENWEBTEXT** (Gokaslan and Cohen, 2019), an open-source recreation of the WebText corpus described in Radford et al. (2019). The text is web content extracted from URLs shared on Reddit with at least three upvotes. (38GB).

• **STORIES**, a dataset introduced in Trinh and Le (2018) containing a subset of CommonCrawl data filtered to match the story-like style of Winograd schemas. (31GB).

### 3.3 Evaluation

Following previous work, we evaluate our pretrained models on downstream tasks using the following three benchmarks.

**GLUE** The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2019b) is a collection of 9 datasets for evaluating natural language understanding systems. Tasks are framed as either single-sentence classification or sentence-pair classification tasks. The GLUE organizers provide training and development data splits as well as a submission server and leaderboard that allows participants to evaluate and compare their systems on private held-out test data.

For the replication study in Section 4, we report results on the development sets after finetuning the pretrained models on the corresponding single-task training data (i.e., without multi-task training or ensembling). Our finetuning procedure follows the original BERT paper (Devlin et al., 2019).

In Section 5 we additionally report test set results obtained from the public leaderboard. These results depend on a several task-specific modifications, which we describe in Section 5.1.

**SQuAD** The Stanford Question Answering Dataset (SQuAD) provides a paragraph of context and a question. The task is to answer the question by extracting the relevant span from the context. We evaluate on two versions of SQuAD: V1.1 and V2.0 (Rajpurkar et al., 2016, 2018). In V1.1 the context always contains an answer, whereas in V2.0 some questions are not answered in the provided context, making the task more challenging.

For SQuAD V1.1 we adopt the same span prediction method as BERT (Devlin et al., 2019). For SQuAD V2.0, we add an additional binary classifier to predict whether the question is answerable, which we train jointly by summing the classification and span loss terms. During evaluation, we only predict span indices on pairs that are classified as answerable.

**RACE** The ReAding Comprehension from Examinations (RACE) (Lai et al., 2017) task is a large-scale reading comprehension dataset with more than 28,000 passages and nearly 100,000 questions. The dataset is collected from English examinations in China, which are designed for middle and high school students. In RACE, each passage is associated with multiple questions. For every question, the task is to select one correct answer from four options. RACE has significantly longer context than other popular reading comprehension datasets and the proportion of questions that requires reasoning is very large.

---

### النسخة العربية

## 3 الإعداد التجريبي

في هذا القسم، نصف الإعداد التجريبي لدراسة التكرار الخاصة بنا لـ BERT.

### 3.1 التنفيذ

نعيد تنفيذ BERT في FAIRSEQ (Ott وآخرون، 2019). نتبع بشكل أساسي معاملات التحسين الفائقة الأصلية لـ BERT، المذكورة في القسم 2، باستثناء معدل التعلم الأقصى وعدد خطوات الإحماء، والتي يتم ضبطها بشكل منفصل لكل إعداد. وجدنا أيضاً أن التدريب حساس جداً لمعامل إبسيلون في آدم، وفي بعض الحالات حصلنا على أداء أفضل أو استقرار محسّن بعد ضبطه. وبالمثل، وجدنا أن تعيين $\beta_2 = 0.98$ يحسّن الاستقرار عند التدريب بأحجام دفعات كبيرة.

نتدرب مسبقاً بتسلسلات من $T = 512$ رمزاً كحد أقصى. على عكس Devlin وآخرون (2019)، لا نحقن تسلسلات قصيرة بشكل عشوائي، ولا نتدرب بطول تسلسل مخفض لأول 90% من التحديثات. نتدرب فقط بتسلسلات كاملة الطول.

نتدرب بحساب النقطة العائمة بالدقة المختلطة على أجهزة DGX-1، كل منها مع 8 × 32 جيجابايت من وحدات معالجة الرسومات Nvidia V100 المترابطة بواسطة Infiniband (Micikevicius وآخرون، 2018).

### 3.2 البيانات

يعتمد التدريب المسبق بأسلوب BERT بشكل حاسم على كميات كبيرة من النصوص. يُظهر Baevski وآخرون (2019) أن زيادة حجم البيانات يمكن أن تؤدي إلى تحسين الأداء في المهام النهائية. قامت عدة جهود بالتدريب على مجموعات بيانات أكبر وأكثر تنوعاً من BERT الأصلي (Radford وآخرون، 2019؛ Yang وآخرون، 2019؛ Zellers وآخرون، 2019). لسوء الحظ، لا يمكن إصدار جميع مجموعات البيانات الإضافية بشكل عام. بالنسبة لدراستنا، نركز على جمع أكبر قدر ممكن من البيانات للتجريب، مما يسمح لنا بمطابقة الجودة والكمية الإجمالية للبيانات بما يناسب كل مقارنة.

نأخذ في الاعتبار خمس مجموعات نصوص باللغة الإنجليزية بأحجام ومجالات متفاوتة، يبلغ مجموعها أكثر من 160 جيجابايت من النص غير المضغوط. نستخدم مجموعات النصوص التالية:

• **BOOKCORPUS** (Zhu وآخرون، 2015) بالإضافة إلى ويكيبيديا الإنجليزية. هذه هي البيانات الأصلية المستخدمة لتدريب BERT. (16 جيجابايت).

• **CC-NEWS**، التي جمعناها من الجزء الإنجليزي من مجموعة بيانات CommonCrawl News (Nagel، 2016). تحتوي البيانات على 63 مليون مقالة إخبارية إنجليزية تم الزحف إليها بين سبتمبر 2016 وفبراير 2019. (76 جيجابايت بعد الترشيح).

• **OPENWEBTEXT** (Gokaslan وCohen، 2019)، إعادة إنشاء مفتوحة المصدر لمجموعة WebText الموصوفة في Radford وآخرون (2019). النص هو محتوى ويب مستخرج من عناوين URL المشتركة على Reddit مع ثلاثة أصوات مؤيدة على الأقل. (38 جيجابايت).

• **STORIES**، مجموعة بيانات تم تقديمها في Trinh وLe (2018) تحتوي على مجموعة فرعية من بيانات CommonCrawl تم ترشيحها لمطابقة النمط الشبيه بالقصة لمخططات Winograd. (31 جيجابايت).

### 3.3 التقييم

باتباع العمل السابق، نقيّم نماذجنا المدربة مسبقاً على المهام النهائية باستخدام المعايير الثلاثة التالية.

**GLUE** معيار تقييم الفهم اللغوي العام (GLUE) (Wang وآخرون، 2019b) هو مجموعة من 9 مجموعات بيانات لتقييم أنظمة فهم اللغة الطبيعية. يتم صياغة المهام كمهام تصنيف جملة واحدة أو مهام تصنيف أزواج الجمل. يوفر منظمو GLUE تقسيمات بيانات التدريب والتطوير بالإضافة إلى خادم إرسال ولوحة صدارة تسمح للمشاركين بتقييم ومقارنة أنظمتهم على بيانات اختبار خاصة محتجزة.

بالنسبة لدراسة التكرار في القسم 4، نبلغ عن النتائج على مجموعات التطوير بعد الضبط الدقيق للنماذج المدربة مسبقاً على بيانات التدريب المقابلة لمهمة واحدة (أي، بدون تدريب متعدد المهام أو تجميع). يتبع إجراء الضبط الدقيق لدينا ورقة BERT الأصلية (Devlin وآخرون، 2019).

في القسم 5 نبلغ أيضاً عن نتائج مجموعة الاختبار المحصل عليها من لوحة الصدارة العامة. تعتمد هذه النتائج على عدة تعديلات خاصة بالمهام، والتي نصفها في القسم 5.1.

**SQuAD** توفر مجموعة بيانات ستانفورد للإجابة على الأسئلة (SQuAD) فقرة من السياق وسؤال. المهمة هي الإجابة على السؤال عن طريق استخراج النطاق ذي الصلة من السياق. نقيّم على نسختين من SQuAD: V1.1 وV2.0 (Rajpurkar وآخرون، 2016، 2018). في V1.1 يحتوي السياق دائماً على إجابة، بينما في V2.0 لا يتم الإجابة على بعض الأسئلة في السياق المقدم، مما يجعل المهمة أكثر تحدياً.

بالنسبة لـ SQuAD V1.1 نعتمد نفس طريقة التنبؤ بالنطاق كما في BERT (Devlin وآخرون، 2019). بالنسبة لـ SQuAD V2.0، نضيف مصنفاً ثنائياً إضافياً للتنبؤ بما إذا كان السؤال قابلاً للإجابة، والذي نقوم بتدريبه بشكل مشترك عن طريق جمع حدود التصنيف والنطاق. أثناء التقييم، نتنبأ فقط بمؤشرات النطاق على الأزواج المصنفة على أنها قابلة للإجابة.

**RACE** مهمة الفهم القرائي من الامتحانات (RACE) (Lai وآخرون، 2017) هي مجموعة بيانات فهم قرائي واسعة النطاق تحتوي على أكثر من 28,000 فقرة وما يقرب من 100,000 سؤال. تم جمع مجموعة البيانات من امتحانات اللغة الإنجليزية في الصين، والتي تم تصميمها لطلاب المدارس المتوسطة والثانوية. في RACE، كل فقرة مرتبطة بأسئلة متعددة. لكل سؤال، المهمة هي اختيار إجابة صحيحة واحدة من أربعة خيارات. يحتوي RACE على سياق أطول بكثير من مجموعات بيانات الفهم القرائي الشائعة الأخرى ونسبة الأسئلة التي تتطلب استدلالاً كبيرة جداً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** FAIRSEQ, DGX-1, Nvidia V100 GPU, Infiniband, CC-NEWS, OPENWEBTEXT, STORIES, CommonCrawl, WebText, Winograd schemas
- **Equations:** Mathematical notation for sequence length constraint
- **Citations:** 13 citations (multiple references to datasets, benchmarks, and prior work)
- **Special handling:**
  - Framework name FAIRSEQ kept in English
  - Hardware names (DGX-1, Nvidia V100, Infiniband) kept in English as product names
  - Dataset names (BOOKCORPUS, CC-NEWS, OPENWEBTEXT, STORIES) kept in English
  - Benchmark names (GLUE, SQuAD, RACE) kept in English
  - Platform name (Reddit) kept in English
  - GLUE task count preserved (9 datasets)
  - SQuAD versions (V1.1, V2.0) kept in English notation
  - Numerical data preserved: 160GB, 16GB, 76GB, 38GB, 31GB, 63 million articles, 28,000 passages, 100,000 questions

### Quality Metrics

- Semantic equivalence: 0.87 - All experimental details accurately conveyed
- Technical accuracy: 0.86 - Correct handling of datasets, benchmarks, and technical specifications
- Readability: 0.85 - Clear Arabic explanation of complex experimental setup
- Glossary consistency: 0.86 - Consistent technical terminology
- **Overall section score:** 0.86
