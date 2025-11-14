# Section 4: Measuring and Preventing Memorization of Benchmarks
## القسم 4: قياس ومنع حفظ المعايير

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** dataset, training, benchmark, contamination, overlap, memorization, evaluation, test set, validation, accuracy, performance

---

### English Version

Since our training dataset is sourced from the internet, it is possible that our model has seen some of the benchmark test sets during training. This could lead to inflated performance on those benchmarks, not because the model has truly learned to perform the task, but because it has memorized specific examples from the test set. To address this concern, we develop a set of tools to measure and prevent contamination of benchmarks in our training data.

#### 4.1 Overlap Analysis

We search for 13-gram overlaps between our training data and the development and test sets of our benchmarks. We consider a benchmark potentially contaminated if more than 10% of its examples have overlaps with the training data. We classify overlaps into several categories:

- **Clean:** Less than 10% overlap
- **Potentially contaminated:** 10-50% overlap
- **Contaminated:** More than 50% overlap

For each benchmark, we calculate the percentage of N-gram overlap between the test/development set and our training data.

#### 4.2 Results of Contamination Analysis

We find varying levels of contamination across benchmarks:

**High contamination (>50% overlap):**
- Some datasets show significant overlap with web data, particularly those derived from Wikipedia or other widely-distributed sources

**Medium contamination (10-50% overlap):**
- Several benchmarks show moderate overlap, which we mark for further analysis

**Low/no contamination (<10% overlap):**
- Many academic benchmarks and recently created datasets show minimal overlap

#### 4.3 Adjusting Results for Contamination

For benchmarks with high levels of contamination, we take several approaches:

1. **Conservative analysis:** We report results on clean versions of benchmarks where possible
2. **Overlap-adjusted metrics:** For some tasks, we compute performance separately on clean vs. contaminated examples
3. **Manual inspection:** We manually inspect high-overlap examples to determine if they represent true memorization or coincidental similarity

In cases where we identify clear contamination, we report both the standard results and contamination-adjusted results. For most benchmarks, we find that even when controlling for contamination, GPT-3 still shows strong performance improvements over baseline models.

#### 4.4 Preventing Future Contamination

To prevent contamination in future work, we propose several best practices:

- **Temporal partitioning:** Only use training data from before the creation date of benchmarks
- **Test set sequestration:** Never expose models to test sets during training or development
- **Deduplication:** Perform aggressive deduplication to remove exact and near-exact matches
- **Benchmark diversity:** Evaluate on a wide range of benchmarks, including new ones created after model training

#### 4.5 Impact on Reported Results

For the vast majority of benchmarks in this paper, we find low levels of contamination (less than 10% overlap). In cases where contamination is higher, we note it in our results tables and provide adjusted metrics where possible. Overall, we find that contamination does not substantially affect our main conclusions about GPT-3's capabilities.

However, we acknowledge that memorization remains a concern for very large language models trained on internet-scale data, and we encourage the community to develop better tools and practices for detecting and preventing data contamination.

---

### النسخة العربية

نظرًا لأن مجموعة بيانات التدريب الخاصة بنا مصدرها الإنترنت، فمن الممكن أن يكون نموذجنا قد رأى بعض مجموعات اختبار المعايير أثناء التدريب. قد يؤدي هذا إلى تضخيم الأداء على تلك المعايير، ليس لأن النموذج قد تعلم حقًا كيفية أداء المهمة، ولكن لأنه حفظ أمثلة معينة من مجموعة الاختبار. لمعالجة هذا القلق، نطور مجموعة من الأدوات لقياس ومنع تلوث المعايير في بيانات التدريب الخاصة بنا.

#### 4.1 تحليل التداخل

نبحث عن تداخلات من 13 كلمة (13-gram) بين بيانات التدريب الخاصة بنا ومجموعات التطوير والاختبار الخاصة بمعاييرنا. نعتبر معيارًا ملوثًا محتملاً إذا كان أكثر من 10% من أمثلته تتداخل مع بيانات التدريب. نصنف التداخلات إلى عدة فئات:

- **نظيف:** أقل من 10% تداخل
- **ملوث محتمل:** تداخل 10-50%
- **ملوث:** أكثر من 50% تداخل

لكل معيار، نحسب النسبة المئوية لتداخل N-gram بين مجموعة الاختبار/التطوير وبيانات التدريب الخاصة بنا.

#### 4.2 نتائج تحليل التلوث

نجد مستويات متفاوتة من التلوث عبر المعايير:

**تلوث عالٍ (>50% تداخل):**
- تُظهر بعض مجموعات البيانات تداخلًا كبيرًا مع بيانات الويب، خاصة تلك المشتقة من ويكيبيديا أو مصادر أخرى واسعة الانتشار

**تلوث متوسط (تداخل 10-50%):**
- تُظهر عدة معايير تداخلًا معتدلًا، والذي نضع علامة عليه لمزيد من التحليل

**تلوث منخفض/بدون تلوث (<10% تداخل):**
- تُظهر العديد من المعايير الأكاديمية ومجموعات البيانات المنشأة حديثًا الحد الأدنى من التداخل

#### 4.3 تعديل النتائج للتلوث

للمعايير ذات المستويات العالية من التلوث، نتخذ عدة مناهج:

1. **تحليل متحفظ:** نُبلغ عن النتائج على النسخ النظيفة من المعايير حيثما أمكن
2. **مقاييس معدلة للتداخل:** لبعض المهام، نحسب الأداء بشكل منفصل على الأمثلة النظيفة مقابل الملوثة
3. **فحص يدوي:** نفحص يدويًا الأمثلة ذات التداخل العالي لتحديد ما إذا كانت تمثل حفظًا حقيقيًا أو تشابهًا صدفيًا

في الحالات التي نحدد فيها تلوثًا واضحًا، نُبلغ عن كل من النتائج القياسية والنتائج المعدلة للتلوث. بالنسبة لمعظم المعايير، نجد أنه حتى عند التحكم في التلوث، لا يزال GPT-3 يُظهر تحسينات قوية في الأداء مقارنة بالنماذج الأساسية.

#### 4.4 منع التلوث المستقبلي

لمنع التلوث في الأعمال المستقبلية، نقترح العديد من أفضل الممارسات:

- **التقسيم الزمني:** استخدام بيانات التدريب فقط من قبل تاريخ إنشاء المعايير
- **عزل مجموعة الاختبار:** عدم تعريض النماذج لمجموعات الاختبار أثناء التدريب أو التطوير
- **إلغاء التكرار:** إجراء إلغاء تكرار صارم لإزالة التطابقات الدقيقة والقريبة من الدقيقة
- **تنوع المعايير:** التقييم على مجموعة واسعة من المعايير، بما في ذلك المعايير الجديدة المنشأة بعد تدريب النموذج

#### 4.5 التأثير على النتائج المُبلغ عنها

بالنسبة للغالبية العظمى من المعايير في هذا البحث، نجد مستويات منخفضة من التلوث (أقل من 10% تداخل). في الحالات التي يكون فيها التلوث أعلى، نشير إليه في جداول النتائج الخاصة بنا ونقدم مقاييس معدلة حيثما أمكن. بشكل عام، نجد أن التلوث لا يؤثر بشكل كبير على استنتاجاتنا الرئيسية حول قدرات GPT-3.

ومع ذلك، نقر بأن الحفظ يبقى مصدر قلق بالنسبة لنماذج اللغة الكبيرة جدًا المدربة على بيانات بحجم الإنترنت، ونشجع المجتمع على تطوير أدوات وممارسات أفضل لاكتشاف ومنع تلوث البيانات.

---

### Translation Notes

- **Figures referenced:** Tables showing contamination analysis results
- **Key terms introduced:** contamination (التلوث), N-gram overlap (تداخل N-gram), memorization (الحفظ), deduplication (إلغاء التكرار), test set sequestration (عزل مجموعة الاختبار)
- **Equations:** Percentage calculations, overlap thresholds
- **Citations:** References to benchmark datasets
- **Special handling:** Preserved technical terms like "13-gram" and specific threshold values

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check

Opening paragraph back-translates to: "Since our training dataset is sourced from the internet, it's possible that our model has seen some of the benchmark test sets during training. This could lead to inflating performance on those benchmarks, not because the model has truly learned how to perform the task, but because it memorized specific examples from the test set. To address this concern, we develop a set of tools to measure and prevent contamination of benchmarks in our training data."

This confirms strong semantic equivalence with the original English text.
