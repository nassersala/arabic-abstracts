# Section 4: Approach
## القسم 4: المنهجية

**Section:** approach
**Translation Quality:** 0.87
**Glossary Terms Used:** محول, معمارية, تدريب مسبق, ضبط دقيق, مشفر, فك التشفير, آلية الانتباه, تصفية, تجميع, عينات, خوارزمية, نموذج لغة

---

### English Version

## Overview

The AlphaCode system addresses code generation by implementing a four-stage pipeline: pre-training on GitHub, fine-tuning on competitive programming data, large-scale sampling, and intelligent filtering/clustering of candidates.

## 4.1 Model Architecture

AlphaCode uses an encoder-decoder transformer treating code generation as a sequence-to-sequence task. The encoder processes natural language problem descriptions while the decoder generates solutions autoregressively.

Key architectural choices:
- **Asymmetric design**: 1536-token encoder but 768-token decoder (descriptions are ~2x longer than solutions)
- **Shallow encoder, deep decoder**: improves training efficiency without sacrificing performance
- **Multi-query attention**: shares key/value heads per attention block to reduce memory usage and sampling costs, enabling larger batch sizes

The system uses SentencePiece tokenization with 8,000 tokens trained on mixed GitHub and CodeContests data.

## 4.2 Pre-training

Models are pre-trained on 715.1 GB of filtered GitHub code (multiple languages: C++, Python, Java, etc.). Training uses:
- Cross-entropy next-token prediction for decoder
- Masked language modeling loss for encoder
- Files split at random pivots—content before becomes encoder input, content after becomes decoder target

Training follows compute-optimal scaling principles, with larger models trained longer. The 1B base model trained for 10⁶ steps with batch size 256.

## 4.3 Fine-tuning

Fine-tuning occurs on the CodeContests dataset using problem descriptions as encoder input and solutions as decoder targets. Four key enhancements are introduced:

**Tempering**: Divides output logits by temperature T before softmax. During fine-tuning, T=0.2 sharpens the distribution to prevent overfitting; at inference, T'=0.12 smooths distribution.

**Value conditioning & prediction**: Model conditions on whether a submission is correct (inserted into problem description). An auxiliary classifier predicts correctness from token representations. This allows leveraging both correct and incorrect training examples.

**GOLD (offline RL algorithm)**: Addresses the "one-of-many" nature of problem-solving. Rather than distributing probability across all valid solutions (like standard maximum likelihood), GOLD concentrates on finding any single correct solution within the submission budget.

**Metadata conditioning**: Tags (algorithm types), problem ratings, and language are included in prompts. At inference, random tags and ratings increase diversity.

Learning rate: 10⁻⁵ decayed to 10⁻⁶ with 1,000-step linear warm-up.

## 4.4 Large-Scale Sampling

A critical component: generating massive numbers of samples (millions per problem) then filtering intelligently. Diversity is ensured by:
- Generating half samples in Python, half in C++
- Randomizing problem tags from top 50 most popular
- Sampling ratings uniformly from 800-3500 range
- Using fixed sampling temperature (T'=0.25 with tempering+GOLD)

This exploration strategy compensates for the limited submission budget (10 attempts per problem in competition format).

## 4.5 Filtering

Samples are filtered to pass example tests provided in problem statements. This removes approximately 99% of candidates, though thousands typically remain per problem. The filtering step itself is non-trivial—approximately 10% of problems yield no samples passing example tests.

## 4.6 Clustering

A separate learned test input generation model creates novel test cases from problem descriptions. Remaining samples are executed on these generated tests and grouped by behavioral equivalence (identical outputs). One sample is selected from each cluster in descending size order, exploiting the heuristic that correct solutions cluster together more than incorrect ones.

If fewer than 10 clusters exist, the process cycles through clusters, skipping already-submitted samples.

---

This integrated approach—combining architectural efficiency, targeted fine-tuning techniques, and large-scale exploration with intelligent filtering—enables competitive-level problem-solving without relying on memorization from training data.

---

### النسخة العربية

## نظرة عامة

يعالج نظام AlphaCode توليد الشفرة البرمجية من خلال تنفيذ خط أنابيب من أربع مراحل: التدريب المسبق على GitHub، والضبط الدقيق على بيانات البرمجة التنافسية، وأخذ العينات على نطاق واسع، والتصفية/التجميع الذكي للمرشحين.

## 4.1 معمارية النموذج

يستخدم AlphaCode محول مشفر-فك تشفير يعامل توليد الشفرة البرمجية كمهمة تسلسل إلى تسلسل. يعالج المشفر أوصاف المشاكل باللغة الطبيعية بينما يولد فك التشفير الحلول بشكل انحداري ذاتي.

الخيارات المعمارية الرئيسية:
- **تصميم غير متماثل**: مشفر بـ 1536 رمز لكن فك تشفير بـ 768 رمز (الأوصاف أطول بحوالي مرتين من الحلول)
- **مشفر ضحل، فك تشفير عميق**: يحسن كفاءة التدريب دون التضحية بالأداء
- **انتباه متعدد الاستعلامات**: يشارك رؤوس المفتاح/القيمة لكل كتلة انتباه لتقليل استخدام الذاكرة وتكاليف أخذ العينات، مما يمكّن أحجام دفعات أكبر

يستخدم النظام ترميز SentencePiece مع 8,000 رمز مدرب على بيانات GitHub و CodeContests المختلطة.

## 4.2 التدريب المسبق

تُدرب النماذج مسبقاً على 715.1 جيجابايت من شفرة GitHub المصفاة (لغات متعددة: ++C، بايثون، جافا، إلخ). يستخدم التدريب:
- تنبؤ الرمز التالي بالانتروبيا المتقاطعة لفك التشفير
- خسارة نمذجة اللغة المقنعة للمشفر
- الملفات مقسمة عند نقاط محورية عشوائية - المحتوى قبلها يصبح مدخل المشفر، والمحتوى بعدها يصبح هدف فك التشفير

يتبع التدريب مبادئ القياس الأمثل للحساب، حيث تُدرب النماذج الأكبر لفترة أطول. تدرب النموذج الأساسي بحجم 1B لـ 10⁶ خطوة بحجم دفعة 256.

## 4.3 الضبط الدقيق

يحدث الضبط الدقيق على مجموعة بيانات CodeContests باستخدام أوصاف المشاكل كمدخل للمشفر والحلول كأهداف لفك التشفير. يتم تقديم أربعة تحسينات رئيسية:

**التلطيف (Tempering)**: يقسم logits الإخراج على درجة الحرارة T قبل softmax. أثناء الضبط الدقيق، T=0.2 يشحذ التوزيع لمنع الإفراط في التلاؤم؛ عند الاستدلال، T'=0.12 ينعّم التوزيع.

**التكييف والتنبؤ بالقيمة**: يُكيف النموذج بناءً على ما إذا كان الحل المقدم صحيحاً (يُدرج في وصف المشكلة). يتنبأ مصنف مساعد بالصحة من تمثيلات الرموز. يتيح هذا الاستفادة من أمثلة التدريب الصحيحة وغير الصحيحة على حد سواء.

**GOLD (خوارزمية RL غير متصلة)**: يعالج طبيعة "واحد من العديد" لحل المشكلات. بدلاً من توزيع الاحتمال عبر جميع الحلول الصالحة (مثل الاحتمالية القصوى القياسية)، يركز GOLD على إيجاد أي حل صحيح واحد ضمن ميزانية الحلول المقدمة.

**التكييف بالبيانات الوصفية**: يتم تضمين الوسوم (أنواع الخوارزميات)، وتقييمات المشاكل، واللغة في المطالبات. عند الاستدلال، تزيد الوسوم والتقييمات العشوائية من التنوع.

معدل التعلم: 10⁻⁵ يتناقص إلى 10⁻⁶ مع إحماء خطي لـ 1,000 خطوة.

## 4.4 أخذ العينات على نطاق واسع

مكون حاسم: توليد أعداد هائلة من العينات (ملايين لكل مشكلة) ثم التصفية بذكاء. يتم ضمان التنوع من خلال:
- توليد نصف العينات في بايثون، ونصفها في ++C
- عشوائية وسوم المشاكل من أفضل 50 الأكثر شيوعاً
- أخذ عينات من التقييمات بشكل موحد من نطاق 800-3500
- استخدام درجة حرارة أخذ عينات ثابتة (T'=0.25 مع التلطيف+GOLD)

تعوض استراتيجية الاستكشاف هذه عن ميزانية الحلول المقدمة المحدودة (10 محاولات لكل مشكلة في شكل المسابقة).

## 4.5 التصفية

تُصفى العينات لتمرير اختبارات الأمثلة المقدمة في بيانات المشاكل. يزيل هذا ما يقرب من 99% من المرشحين، على الرغم من أن الآلاف عادةً تبقى لكل مشكلة. خطوة التصفية نفسها ليست تافهة - حوالي 10% من المشاكل لا تنتج عينات تمرر اختبارات الأمثلة.

## 4.6 التجميع

ينشئ نموذج توليد مدخلات الاختبار المتعلم منفصل حالات اختبار جديدة من أوصاف المشاكل. تُنفذ العينات المتبقية على هذه الاختبارات المولدة وتُجمع حسب التكافؤ السلوكي (مخرجات متطابقة). يتم اختيار عينة واحدة من كل مجموعة بترتيب الحجم التنازلي، مستغلاً الاستدلال بأن الحلول الصحيحة تتجمع معاً أكثر من الحلول غير الصحيحة.

إذا كان هناك أقل من 10 مجموعات، تتكرر العملية عبر المجموعات، متخطيةً العينات المقدمة بالفعل.

---

يمكّن هذا النهج المتكامل - الجامع بين الكفاءة المعمارية، وتقنيات الضبط الدقيق المستهدفة، والاستكشاف على نطاق واسع مع التصفية الذكية - من حل المشكلات على مستوى تنافسي دون الاعتماد على الحفظ من بيانات التدريب.

---

### Translation Notes

- **Subsections:** 4.1 Model architecture, 4.2 Pre-training, 4.3 Fine-tuning, 4.4 Large scale sampling, 4.5 Filtering, 4.6 Clustering

- **Key terms introduced:**
  - encoder-decoder transformer (محول مشفر-فك تشفير)
  - sequence-to-sequence (تسلسل إلى تسلسل)
  - autoregressively (بشكل انحداري ذاتي)
  - asymmetric design (تصميم غير متماثل)
  - multi-query attention (انتباه متعدد الاستعلامات)
  - SentencePiece tokenization (ترميز SentencePiece)
  - cross-entropy (الانتروبيا المتقاطعة)
  - next-token prediction (تنبؤ الرمز التالي)
  - masked language modeling (نمذجة اللغة المقنعة)
  - compute-optimal scaling (القياس الأمثل للحساب)
  - tempering (التلطيف)
  - logits (logits)
  - softmax (softmax)
  - overfitting (الإفراط في التلاؤم)
  - value conditioning (التكييف بالقيمة)
  - auxiliary classifier (مصنف مساعد)
  - GOLD algorithm (خوارزمية GOLD)
  - offline RL (التعلم المعزز غير المتصل)
  - maximum likelihood (الاحتمالية القصوى)
  - metadata conditioning (التكييف بالبيانات الوصفية)
  - learning rate (معدل التعلم)
  - warm-up (إحماء)
  - behavioral equivalence (التكافؤ السلوكي)

- **Technical parameters:**
  - 1536-token encoder, 768-token decoder preserved
  - 8,000 tokens for SentencePiece preserved
  - 715.1 GB GitHub code preserved
  - 10⁶ steps, batch size 256 preserved
  - T=0.2 (fine-tuning), T'=0.12 (inference) preserved
  - Learning rate 10⁻⁵ → 10⁻⁶ preserved
  - 1,000-step warm-up preserved
  - 50% Python, 50% C++ preserved
  - Top 50 most popular tags preserved
  - 800-3500 rating range preserved
  - T'=0.25 sampling temperature preserved
  - 99% filtering rate preserved
  - 10% problems with no passing samples preserved
  - 10 clusters threshold preserved

- **Algorithm/Method names:** SentencePiece, GOLD, softmax - kept in English as technical terms

- **Programming languages:** C++, Python, Java - kept in English as standard practice

- **Platform names:** GitHub, CodeContests - kept in English as proper nouns

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Validation

The Arabic translation accurately conveys: the four-stage pipeline approach (pre-training on GitHub, fine-tuning on competitive programming, large-scale sampling, filtering/clustering), the asymmetric encoder-decoder transformer architecture (1536/768 tokens, shallow encoder/deep decoder, multi-query attention, SentencePiece with 8000 tokens), pre-training details (715.1GB GitHub code, cross-entropy and masked LM losses, random file splitting, 1B model with 10⁶ steps), fine-tuning enhancements (tempering with T=0.2/0.12, value conditioning and prediction, GOLD algorithm for one-of-many solutions, metadata conditioning, learning rate 10⁻⁵→10⁻⁶), large-scale sampling strategy (millions of samples, 50% Python/50% C++, randomized tags from top 50, ratings 800-3500, T'=0.25), filtering (99% removal, 10% problems yield no passing samples), and clustering (test input generation, behavioral equivalence grouping, descending cluster size selection, heuristic that correct solutions cluster together).
