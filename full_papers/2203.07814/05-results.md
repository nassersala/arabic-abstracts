# Section 5: Results
## القسم 5: النتائج

**Section:** results
**Translation Quality:** 0.88
**Glossary Terms Used:** تقييم, معيار, تجميع, تصفية, معدل الحل, عينات, البرمجة التنافسية, قياس, نموذج

---

### English Version

## 5.1 Codeforces Competitions Evaluation

AlphaCode was tested on 10 Codeforces competitions from December 2021, each with over 5,000 participants. The system achieved "an average ranking of top 54.3% in competitions with more than 5,000 participants" and an estimated rating of 1238, placing it in the top 28% of active users.

Key metrics from actual competition submissions:
- Average of 2.4 submissions needed per solved problem (with 10-submission limit)
- When allowed more submissions (second/third runs), ranking improved to top 48.8% with average 28.8 submissions per problem

## 5.2 CodeContests Evaluation

Performance on the researchers' curated dataset showed:
- 34.2% solve rate (10@1M metric) on validation set with 1 million samples
- 31.8% on validation set with 100k samples
- 29.6% on test set with 100k samples

The 41B model with clustering consistently outperformed the 9B model across all sample budgets.

## 5.3 CodeContests Ablations & Results

### 5.3.1 Scaling Analysis

The study demonstrated "solve rates scale approximately log-linearly with the number of samples," with better models showing steeper improvement curves. Performance also "scales approximately log-linearly with more training compute."

### 5.3.2 Architecture Optimizations

Multi-query attention and asymmetric encoder-decoder designs improved sampling speed significantly (4.74 samples/TPU second) while maintaining solve rate at 17.3% (10@10k).

### 5.3.3 Pre-training Dataset Impact

Full GitHub pre-training (12.4% solve rate at 10@1k) substantially outperformed Python-only (5.8%) and MassiveText (9.7%) alternatives.

### 5.3.4 Model Enhancements

Cumulative improvements from modifications increased 10@100k solve rate from 15.2% to 24.1%:
- Masked language modeling
- Tempering regularization
- Tags and ratings conditioning
- Value prediction
- GOLD training algorithm

### 5.3.5 Filtering and Clustering

"Filtering removes approximately 99% of model samples," while clustering of remaining samples prevents redundant submissions. Without clustering, the system showed flat performance; with it, solve rates scaled substantially with sample counts.

## 5.4 Results on APPS

On the APPS benchmark, AlphaCode 1B achieved 20.36% solve rate (introductory), 9.66% (interview), and 7.75% (competition difficulty) with 50,000 samples and 5 submissions—outperforming previously published baselines despite not using all full methodology components.

---

### النسخة العربية

## 5.1 تقييم مسابقات Codeforces

تم اختبار AlphaCode في 10 مسابقات Codeforces من ديسمبر 2021، كل منها مع أكثر من 5,000 مشارك. حقق النظام "متوسط تصنيف ضمن أفضل 54.3% في مسابقات مع أكثر من 5,000 مشارك" وتقييماً مقدراً بـ 1238، مما وضعه ضمن أفضل 28% من المستخدمين النشطين.

المقاييس الرئيسية من حلول المسابقة الفعلية:
- متوسط 2.4 حل مقدم مطلوب لكل مشكلة محلولة (مع حد 10 حلول مقدمة)
- عند السماح بمزيد من الحلول المقدمة (جولات ثانية/ثالثة)، تحسن التصنيف إلى أفضل 48.8% بمتوسط 28.8 حل مقدم لكل مشكلة

## 5.2 تقييم CodeContests

أظهر الأداء على مجموعة البيانات المنسقة من الباحثين:
- معدل حل 34.2% (مقياس 10@1M) على مجموعة التحقق مع مليون عينة
- 31.8% على مجموعة التحقق مع 100 ألف عينة
- 29.6% على مجموعة الاختبار مع 100 ألف عينة

تفوق نموذج 41B مع التجميع باستمرار على نموذج 9B عبر جميع ميزانيات العينات.

## 5.3 دراسات الاستئصال والنتائج على CodeContests

### 5.3.1 تحليل القياس

أظهرت الدراسة "أن معدلات الحل تتناسب تقريباً لوغاريتمياً خطياً مع عدد العينات"، حيث تُظهر النماذج الأفضل منحنيات تحسين أكثر حدة. يتناسب الأداء أيضاً "تقريباً لوغاريتمياً خطياً مع المزيد من الحساب التدريبي".

### 5.3.2 تحسينات المعمارية

حسّن الانتباه متعدد الاستعلامات وتصاميم المشفر-فك التشفير غير المتماثلة سرعة أخذ العينات بشكل كبير (4.74 عينة/ثانية TPU) مع الحفاظ على معدل الحل عند 17.3% (10@10k).

### 5.3.3 تأثير مجموعة بيانات التدريب المسبق

تفوق التدريب المسبق الكامل على GitHub (معدل حل 12.4% عند 10@1k) بشكل كبير على بدائل بايثون فقط (5.8%) و MassiveText (9.7%).

### 5.3.4 تحسينات النموذج

زادت التحسينات التراكمية من التعديلات معدل حل 10@100k من 15.2% إلى 24.1%:
- نمذجة اللغة المقنعة
- تنظيم التلطيف
- التكييف بالوسوم والتقييمات
- تنبؤ القيمة
- خوارزمية تدريب GOLD

### 5.3.5 التصفية والتجميع

"تزيل التصفية ما يقرب من 99% من عينات النموذج"، بينما يمنع تجميع العينات المتبقية الحلول المقدمة الزائدة. بدون التجميع، أظهر النظام أداءً ثابتاً؛ ومعه، تناسبت معدلات الحل بشكل كبير مع أعداد العينات.

## 5.4 النتائج على APPS

على معيار APPS، حقق AlphaCode 1B معدل حل 20.36% (مستوى تمهيدي)، و 9.66% (مقابلة)، و 7.75% (صعوبة المسابقة) مع 50,000 عينة و 5 حلول مقدمة - متفوقاً على خطوط الأساس المنشورة سابقاً على الرغم من عدم استخدام جميع مكونات المنهجية الكاملة.

---

### Translation Notes

- **Subsections:** 5.1 Codeforces competitions evaluation, 5.2 CodeContests evaluation, 5.3 CodeContests ablations & results (with 5 sub-subsections), 5.4 Results on APPS

- **Key terms introduced:**
  - solve rate (معدل الحل)
  - validation set (مجموعة التحقق)
  - test set (مجموعة الاختبار)
  - sample budget (ميزانية العينات)
  - ablation studies (دراسات الاستئصال)
  - log-linearly (لوغاريتمياً خطياً)
  - training compute (الحساب التدريبي)
  - sampling speed (سرعة أخذ العينات)
  - cumulative improvements (التحسينات التراكمية)
  - redundant submissions (الحلول المقدمة الزائدة)
  - baseline (خط الأساس)

- **Performance metrics preserved:**
  - Top 54.3% ranking (Codeforces)
  - Rating of 1238
  - Top 28% of active users
  - 2.4 average submissions per solved problem
  - Top 48.8% with 28.8 submissions
  - 34.2% solve rate (10@1M on validation)
  - 31.8% (10@100k on validation)
  - 29.6% (10@100k on test)
  - 41B vs 9B model comparison
  - 4.74 samples/TPU second
  - 17.3% solve rate (10@10k)
  - 12.4% (full GitHub) vs 5.8% (Python-only) vs 9.7% (MassiveText)
  - 15.2% → 24.1% cumulative improvement
  - 99% filtering removal rate
  - 20.36%/9.66%/7.75% on APPS (introductory/interview/competition)
  - 50,000 samples with 5 submissions on APPS

- **Model sizes:** 1B, 9B, 41B - preserved

- **Metric notation:** 10@1M, 10@100k, 10@10k, 10@1k - preserved

- **Platform/Dataset names:** Codeforces, CodeContests, APPS, MassiveText, GitHub - kept in English as proper nouns

- **Technical terms:** TPU (Tensor Processing Unit) - kept as abbreviation

- **Direct quotes:** Preserved in quotation marks in both versions

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Validation

The Arabic translation accurately conveys: Codeforces evaluation results (10 competitions December 2021, top 54.3% average ranking, rating 1238 = top 28%, 2.4 submissions/problem, improved to top 48.8% with 28.8 submissions), CodeContests evaluation performance (34.2% at 10@1M validation, 31.8% at 10@100k validation, 29.6% at 10@100k test, 41B outperforming 9B), ablation study findings (log-linear scaling with samples and compute, architecture optimizations achieving 4.74 samples/TPU-second and 17.3% solve rate, full GitHub pre-training 12.4% vs Python-only 5.8% vs MassiveText 9.7%, cumulative improvements 15.2%→24.1%, filtering removing 99%, clustering enabling scaling), and APPS benchmark results (20.36%/9.66%/7.75% across difficulty levels with 50k samples and 5 submissions, outperforming baselines).
