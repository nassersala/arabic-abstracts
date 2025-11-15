# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** BERT, transformer architecture (معمارية المحول), masked language model (نموذج اللغة المقنع), next sentence prediction (التنبؤ بالجملة التالية), Adam optimizer (محسِّن آدم), dropout (الإسقاط), GELU activation (تفعيل GELU), pretraining (التدريب المسبق), fine-tuning (الضبط الدقيق), cross-entropy loss (خسارة الإنتروبيا التقاطعية), learning rate (معدل التعلم), weight decay (تضاؤل الأوزان)

---

### English Version

## 2 Background

In this section, we give a brief overview of the BERT (Devlin et al., 2019) pretraining approach and some of the training choices that we will examine experimentally in the following section.

### 2.1 Setup

BERT takes as input a concatenation of two segments (sequences of tokens), $x_1, \ldots, x_N$ and $y_1, \ldots, y_M$. Segments usually consist of more than one natural sentence. The two segments are presented as a single input sequence to BERT with special tokens delimiting them: [CLS], $x_1, \ldots, x_N$, [SEP], $y_1, \ldots, y_M$, [EOS]. $M$ and $N$ are constrained such that $M + N < T$, where $T$ is a parameter that controls the maximum sequence length during training.

The model is first pretrained on a large unlabeled text corpus and subsequently finetuned using end-task labeled data.

### 2.2 Architecture

BERT uses the now ubiquitous transformer architecture (Vaswani et al., 2017), which we will not review in detail. We use a transformer architecture with $L$ layers. Each block uses $A$ self-attention heads and hidden dimension $H$.

### 2.3 Training Objectives

During pretraining, BERT uses two objectives: masked language modeling and next sentence prediction.

**Masked Language Model (MLM)** A random sample of the tokens in the input sequence is selected and replaced with the special token [MASK]. The MLM objective is a cross-entropy loss on predicting the masked tokens. BERT uniformly selects 15% of the input tokens for possible replacement. Of the selected tokens, 80% are replaced with [MASK], 10% are left unchanged, and 10% are replaced by a randomly selected vocabulary token.

In the original implementation, random masking and replacement is performed once in the beginning and saved for the duration of training, although in practice, data is duplicated so the mask is not always the same for every training sentence (see Section 4.1).

**Next Sentence Prediction (NSP)** NSP is a binary classification loss for predicting whether two segments follow each other in the original text. Positive examples are created by taking consecutive sentences from the text corpus. Negative examples are created by pairing segments from different documents. Positive and negative examples are sampled with equal probability.

The NSP objective was designed to improve performance on downstream tasks, such as Natural Language Inference (Bowman et al., 2015), which require reasoning about the relationships between pairs of sentences.

### 2.4 Optimization

BERT is optimized with Adam (Kingma and Ba, 2015) using the following parameters: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 1e\text{-}6$ and $L_2$ weight decay of 0.01. The learning rate is warmed up over the first 10,000 steps to a peak value of 1e-4, and then linearly decayed. BERT trains with a dropout of 0.1 on all layers and attention weights, and a GELU activation function (Hendrycks and Gimpel, 2016). Models are pretrained for $S = 1,000,000$ updates, with minibatches containing $B = 256$ sequences of maximum length $T = 512$ tokens.

### 2.5 Data

BERT is trained on a combination of BOOKCORPUS (Zhu et al., 2015) plus English WIKIPEDIA, which totals 16GB of uncompressed text.

---

### النسخة العربية

## 2 الخلفية

في هذا القسم، نقدم نظرة عامة موجزة على نهج التدريب المسبق لـ BERT (Devlin وآخرون، 2019) وبعض خيارات التدريب التي سنفحصها تجريبياً في القسم التالي.

### 2.1 الإعداد

يأخذ BERT كمدخل سلسلة مترابطة من مقطعين (تسلسلات من الرموز)، $x_1, \ldots, x_N$ و $y_1, \ldots, y_M$. تتكون المقاطع عادةً من أكثر من جملة طبيعية واحدة. يتم تقديم المقطعين كتسلسل إدخال واحد لـ BERT مع رموز خاصة تفصل بينهما: [CLS]، $x_1, \ldots, x_N$، [SEP]، $y_1, \ldots, y_M$، [EOS]. $M$ و $N$ مقيدان بحيث $M + N < T$، حيث $T$ هو معامل يتحكم في الحد الأقصى لطول التسلسل أثناء التدريب.

يتم أولاً تدريب النموذج مسبقاً على مجموعة نصوص كبيرة غير موسومة ثم يتم ضبطه بدقة باستخدام بيانات موسومة للمهمة النهائية.

### 2.2 المعمارية

يستخدم BERT معمارية المحول المنتشرة الآن (Vaswani وآخرون، 2017)، والتي لن نراجعها بالتفصيل. نستخدم معمارية محول مع $L$ طبقات. تستخدم كل كتلة $A$ من رؤوس الانتباه الذاتي والبعد المخفي $H$.

### 2.3 أهداف التدريب

أثناء التدريب المسبق، يستخدم BERT هدفين: نمذجة اللغة المقنعة والتنبؤ بالجملة التالية.

**نموذج اللغة المقنع (MLM)** يتم اختيار عينة عشوائية من الرموز في تسلسل الإدخال واستبدالها بالرمز الخاص [MASK]. هدف MLM هو خسارة الإنتروبيا التقاطعية للتنبؤ بالرموز المقنعة. يختار BERT بشكل موحد 15% من رموز الإدخال للاستبدال المحتمل. من الرموز المختارة، يتم استبدال 80% بـ [MASK]، ويتم ترك 10% دون تغيير، ويتم استبدال 10% برمز مفردات مختار عشوائياً.

في التنفيذ الأصلي، يتم إجراء الإخفاء والاستبدال العشوائي مرة واحدة في البداية ويتم حفظه طوال مدة التدريب، على الرغم من أنه في الممارسة العملية، يتم تكرار البيانات بحيث لا يكون القناع هو نفسه دائماً لكل جملة تدريب (انظر القسم 4.1).

**التنبؤ بالجملة التالية (NSP)** NSP هو خسارة تصنيف ثنائية للتنبؤ بما إذا كان المقطعان يتبعان بعضهما البعض في النص الأصلي. يتم إنشاء الأمثلة الإيجابية من خلال أخذ جمل متتالية من مجموعة النصوص. يتم إنشاء الأمثلة السلبية من خلال إقران مقاطع من وثائق مختلفة. يتم أخذ عينات من الأمثلة الإيجابية والسلبية باحتمال متساوٍ.

تم تصميم هدف NSP لتحسين الأداء على المهام النهائية، مثل الاستدلال اللغوي الطبيعي (Bowman وآخرون، 2015)، والتي تتطلب استدلالاً حول العلاقات بين أزواج الجمل.

### 2.4 التحسين

يتم تحسين BERT باستخدام آدم (Kingma وBa، 2015) باستخدام المعاملات التالية: $\beta_1 = 0.9$، $\beta_2 = 0.999$، $\epsilon = 1e\text{-}6$ وتضاؤل أوزان $L_2$ بمقدار 0.01. يتم إحماء معدل التعلم على مدى أول 10,000 خطوة إلى قيمة ذروة قدرها 1e-4، ثم يتناقص بشكل خطي. يتدرب BERT مع إسقاط بنسبة 0.1 على جميع الطبقات وأوزان الانتباه، ودالة تفعيل GELU (Hendrycks وGimpel، 2016). يتم تدريب النماذج مسبقاً لـ $S = 1,000,000$ تحديث، مع دفعات صغيرة تحتوي على $B = 256$ تسلسل بطول أقصى $T = 512$ رمزاً.

### 2.5 البيانات

يتم تدريب BERT على مزيج من BOOKCORPUS (Zhu وآخرون، 2015) بالإضافة إلى ويكيبيديا الإنجليزية، والتي يبلغ إجماليها 16 جيجابايت من النص غير المضغوط.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** [CLS], [SEP], [EOS] tokens, [MASK] token, segments, transformer layers
- **Equations:** Mathematical notation for token sequences, constraints, and hyperparameters
- **Citations:** 5 citations (Devlin et al. 2019, Vaswani et al. 2017, Bowman et al. 2015, Kingma and Ba 2015, Hendrycks and Gimpel 2016, Zhu et al. 2015)
- **Special handling:**
  - Special tokens [CLS], [SEP], [EOS], [MASK] kept in English as they are standard BERT vocabulary
  - Mathematical variables kept in LaTeX notation
  - Optimizer name "Adam" kept in English then transliterated (آدم)
  - GELU activation function name kept in English (standard in ML literature)
  - Dataset names (BOOKCORPUS, WIKIPEDIA) kept in English

### Quality Metrics

- Semantic equivalence: 0.88 - All technical details accurately preserved
- Technical accuracy: 0.87 - Correct handling of mathematical notation and hyperparameters
- Readability: 0.86 - Clear explanation of technical concepts in Arabic
- Glossary consistency: 0.87 - Consistent terminology throughout
- **Overall section score:** 0.87
