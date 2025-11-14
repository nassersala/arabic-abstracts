# Section 5: Training
## القسم 5: التدريب

**Section:** training
**Translation Quality:** 0.87
**Glossary Terms Used:** training data, batching, optimizer, learning rate, regularization, dropout, label smoothing

---

### English Version

This section describes the training regime for our models.

## 5.1 Training Data and Batching

We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding [3], which has a shared source-target vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary [38]. Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000 target tokens.

## 5.2 Hardware and Schedule

We trained our models on one machine with 8 NVIDIA P100 GPUs. For our base models using the hyperparameters described throughout the paper, each training step took about 0.4 seconds. We trained the base models for a total of 100,000 steps or 12 hours. For our big models, (described on the bottom line of table 3), step time was 1.0 seconds. The big models were trained for 300,000 steps (3.5 days).

## 5.3 Optimizer

We used the Adam optimizer [20] with β₁ = 0.9, β₂ = 0.98 and ε = 10⁻⁹. We varied the learning rate over the course of training, according to the formula:

$$lrate = d_{\text{model}}^{-0.5} \cdot \min(\text{step\\_num}^{-0.5}, \text{step\\_num} \cdot \text{warmup\\_steps}^{-1.5}) \quad (3)$$

This corresponds to increasing the learning rate linearly for the first warmup_steps training steps, and decreasing it thereafter proportionally to the inverse square root of the step number. We used warmup_steps = 4000.

## 5.4 Regularization

We employ three types of regularization during training:

**Residual Dropout:** We apply dropout [33] to the output of each sub-layer, before it is added to the sub-layer input and normalized. In addition, we apply dropout to the sums of the embeddings and the positional encodings in both the encoder and decoder stacks. For the base model, we use a rate of P_drop = 0.1.

**Label Smoothing:** During training, we employed label smoothing of value ε_ls = 0.1 [36]. This hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score.

---

### النسخة العربية

يصف هذا القسم نظام التدريب لنماذجنا.

## 5.1 بيانات التدريب والتجميع

درّبنا على مجموعة بيانات WMT 2014 القياسية للإنجليزية-الألمانية التي تتكون من حوالي 4.5 مليون زوج جملة. تم ترميز الجمل باستخدام ترميز أزواج البايتات (byte-pair encoding) [3]، الذي يحتوي على مفردات مصدر-هدف مشتركة من حوالي 37000 رمز. للإنجليزية-الفرنسية، استخدمنا مجموعة بيانات WMT 2014 الإنجليزية-الفرنسية الأكبر بكثير التي تتكون من 36 مليون جملة وقسّمنا الرموز إلى مفردات قطع كلمات بحجم 32000 [38]. تم تجميع أزواج الجمل معاً حسب طول التسلسل التقريبي. احتوت كل دفعة تدريب على مجموعة من أزواج الجمل تحتوي على حوالي 25000 رمز مصدر و25000 رمز هدف.

## 5.2 العتاد والجدول الزمني

درّبنا نماذجنا على جهاز واحد مع 8 وحدات معالجة رسومية NVIDIA P100. لنماذجنا الأساسية باستخدام المعاملات الفائقة (hyperparameters) الموصوفة في جميع أنحاء الورقة، استغرقت كل خطوة تدريب حوالي 0.4 ثانية. درّبنا النماذج الأساسية لإجمالي 100,000 خطوة أو 12 ساعة. بالنسبة لنماذجنا الكبيرة، (الموصوفة في السطر السفلي من الجدول 3)، كان وقت الخطوة 1.0 ثانية. تم تدريب النماذج الكبيرة لـ 300,000 خطوة (3.5 يوم).

## 5.3 المُحسِّن

استخدمنا مُحسِّن Adam [20] مع β₁ = 0.9، β₂ = 0.98 و ε = 10⁻⁹. غيّرنا معدل التعلّم على مدار التدريب، وفقاً للصيغة:

$$lrate = d_{\text{model}}^{-0.5} \cdot \min(\text{step\\_num}^{-0.5}, \text{step\\_num} \cdot \text{warmup\\_steps}^{-1.5}) \quad (3)$$

يتوافق هذا مع زيادة معدل التعلّم خطياً لأول warmup_steps خطوات تدريب، وتقليله بعد ذلك بالتناسب مع الجذر التربيعي العكسي لرقم الخطوة. استخدمنا warmup_steps = 4000.

## 5.4 التنظيم

نستخدم ثلاثة أنواع من التنظيم أثناء التدريب:

**إسقاط متبقي (Residual Dropout):** نطبق الإسقاط (dropout) [33] على إخراج كل طبقة فرعية، قبل إضافته إلى إدخال الطبقة الفرعية وتطبيعه. بالإضافة إلى ذلك، نطبق الإسقاط على مجاميع التضمينات والترميزات الموضعية في كل من مكدّسات المشفّر وفك التشفير. بالنسبة للنموذج الأساسي، نستخدم معدل P_drop = 0.1.

**تنعيم التصنيفات (Label Smoothing):** أثناء التدريب، استخدمنا تنعيم التصنيفات بقيمة ε_ls = 0.1 [36]. يضر هذا بالحيرة (perplexity)، حيث يتعلم النموذج أن يكون أكثر عدم يقين، لكنه يحسّن الدقة ونتيجة BLEU.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 3 (الجدول 3)
- **Key terms introduced:**
  - Training regime (نظام التدريب)
  - Byte-pair encoding (ترميز أزواج البايتات)
  - Shared source-target vocabulary (مفردات مصدر-هدف مشتركة)
  - Word-piece vocabulary (مفردات قطع كلمات)
  - Batching (التجميع)
  - Training batch (دفعة تدريب)
  - Hyperparameters (المعاملات الفائقة)
  - Training step (خطوة تدريب)
  - Adam optimizer (مُحسِّن Adam)
  - Learning rate (معدل التعلّم)
  - Warmup steps (خطوات الإحماء)
  - Inverse square root (الجذر التربيعي العكسي)
  - Regularization (التنظيم)
  - Residual Dropout (إسقاط متبقي)
  - Dropout (الإسقاط)
  - Label smoothing (تنعيم التصنيفات)
  - Perplexity (الحيرة)

- **Equations:**
  - Equation (3): Learning rate schedule
  - Preserved in LaTeX format

- **Citations:** [3], [38], [20], [33], [36] all preserved

- **Special handling:**
  - Dataset names kept in English (WMT 2014)
  - GPU model (NVIDIA P100) kept in English
  - Optimizer name (Adam) kept in English
  - Variable names preserved: β₁, β₂, ε, P_drop, ε_ls
  - Numbers and statistics preserved exactly
  - BLEU score kept as English term

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
