# Section 7: Related Work
## القسم 7: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** تخليق البرامج, محول, نموذج لغة, معيار, تقييم, البرمجة التنافسية, عينات, تصفية

---

### English Version

## 7.1 Program Synthesis

Traditional program synthesis research has explored multiple specification approaches. Early work employed deductive synthesis, which "transforms the task specification into constraints, uses a theorem prover to find a proof that satisfies all the constraints, and extracts the program from the proof." Input/output examples later became standard specifications, exemplified by tools like FlashFill. Sketch-based approaches reduced search spaces by providing program skeletons.

The paper notes that "most prior work has been limited to either restricted domain-specific programming languages or short code snippets," representing significant constraints on applicability.

## 7.2 Transformers for Program Synthesis

Recent advances leveraged large-scale transformer models. The authors acknowledge that "recent large-scale transformer-based language models...have successfully generated code that solves simple programming problems in Python." They specifically reference Codex's performance on simple tasks, noting that their baseline "performs similarly to Codex (Table LABEL:tab:human-eval)" without specialized modifications.

However, these models struggled with complex reasoning. The paper emphasizes that Codex and similar systems achieved only "low single-digit solve rates" on competitive programming benchmarks.

## 7.3 Scaling Sampling

A distinctive contribution involves large-scale sampling strategies. The authors demonstrate that "large-scale model sampling to explore the search space, followed by filtering based on program behavior" proves critical for performance. Their analysis reveals that "solve rates scale approximately log-linearly with k" (sample count), justifying the sampling-heavy approach.

## 7.4 Evaluation Metrics

The research highlights evaluation challenges in prior work, noting that existing datasets exhibit "30% or more programs which pass all tests but are not actually correct." Their CodeContests dataset "reduces the false positive rate from 30-60% in existing datasets to just 4%," addressing fundamental measurement issues.

## 7.5 Competitive Programming

Competitive programming provides a rigorous benchmark. The paper notes that "problems are often given ratings to indicate difficulty, and more difficult problems are worth more points," with evaluation against "an exhaustive set of hidden tests." This contrasts sharply with simpler benchmarks using only provided examples.

Human performance provides meaningful context: international competitions like ICPC attract "almost 60,000 students from over 3,000 universities," establishing AlphaCode's achievement of "top 54.3%" average ranking as genuinely competitive.

---

### النسخة العربية

## 7.1 تخليق البرامج

استكشف البحث التقليدي في تخليق البرامج أساليب مواصفات متعددة. استخدم العمل المبكر التخليق الاستنتاجي، الذي "يحول مواصفات المهمة إلى قيود، ويستخدم مُثبِت النظريات للعثور على برهان يرضي جميع القيود، ويستخرج البرنامج من البرهان". أصبحت أمثلة الإدخال/الإخراج فيما بعد مواصفات قياسية، كما يتضح من أدوات مثل FlashFill. قللت الأساليب القائمة على الرسومات التخطيطية فضاءات البحث من خلال توفير هياكل البرامج.

يلاحظ الورقة أن "معظم الأعمال السابقة كانت محدودة إما بلغات برمجة خاصة بالمجال محدودة أو مقتطفات شفرة قصيرة"، مما يمثل قيوداً كبيرة على قابلية التطبيق.

## 7.2 المحولات لتخليق البرامج

استفادت التطورات الحديثة من نماذج المحولات الكبيرة. يقر المؤلفون بأن "نماذج اللغة الكبيرة القائمة على المحولات الحديثة... نجحت في توليد شفرة تحل مشاكل برمجية بسيطة في بايثون". يشيرون على وجه التحديد إلى أداء Codex في المهام البسيطة، مشيرين إلى أن خط أساسهم "يؤدي بشكل مماثل لـ Codex (الجدول LABEL:tab:human-eval)" دون تعديلات متخصصة.

ومع ذلك، واجهت هذه النماذج صعوبة في الاستدلال المعقد. تؤكد الورقة أن Codex والأنظمة المماثلة حققت فقط "معدلات حل من رقم واحد منخفضة" على معايير البرمجة التنافسية.

## 7.3 قياس أخذ العينات

تتضمن مساهمة مميزة استراتيجيات أخذ عينات واسعة النطاق. يوضح المؤلفون أن "أخذ عينات النموذج على نطاق واسع لاستكشاف فضاء البحث، متبوعاً بالتصفية بناءً على سلوك البرنامج" يثبت أنه حاسم للأداء. يكشف تحليلهم أن "معدلات الحل تتناسب تقريباً لوغاريتمياً خطياً مع k" (عدد العينات)، مما يبرر النهج الثقيل بأخذ العينات.

## 7.4 مقاييس التقييم

يسلط البحث الضوء على تحديات التقييم في الأعمال السابقة، مشيراً إلى أن مجموعات البيانات الحالية تُظهر "30% أو أكثر من البرامج التي تجتاز جميع الاختبارات ولكنها ليست صحيحة فعلياً". تقلل مجموعة بيانات CodeContests الخاصة بهم "معدل الإيجابية الخاطئة من 30-60% في مجموعات البيانات الحالية إلى 4% فقط"، معالجةً مشاكل القياس الأساسية.

## 7.5 البرمجة التنافسية

توفر البرمجة التنافسية معياراً صارماً. تلاحظ الورقة أن "المشاكل غالباً ما تُعطى تقييمات للإشارة إلى الصعوبة، والمشاكل الأكثر صعوبة تستحق نقاطاً أكثر"، مع التقييم مقابل "مجموعة شاملة من الاختبارات المخفية". يتناقض هذا بشكل حاد مع المعايير الأبسط التي تستخدم فقط الأمثلة المقدمة.

يوفر الأداء البشري سياقاً ذا معنى: المسابقات الدولية مثل ICPC تجذب "ما يقرب من 60,000 طالب من أكثر من 3,000 جامعة"، مما يؤسس إنجاز AlphaCode في تحقيق متوسط تصنيف "ضمن أفضل 54.3%" كإنجاز تنافسي حقيقي.

---

### Translation Notes

- **Subsections:** 7.1 Program synthesis, 7.2 Transformers for program synthesis, 7.3 Scaling sampling, 7.4 Evaluation metrics, 7.5 Competitive programming

- **Key terms introduced:**
  - program synthesis (تخليق البرامج)
  - deductive synthesis (التخليق الاستنتاجي)
  - theorem prover (مُثبِت النظريات)
  - input/output examples (أمثلة الإدخال/الإخراج)
  - sketch-based approaches (الأساليب القائمة على الرسومات التخطيطية)
  - program skeletons (هياكل البرامج)
  - domain-specific programming languages (لغات برمجة خاصة بالمجال)
  - code snippets (مقتطفات شفرة)
  - baseline (خط الأساس)
  - single-digit solve rates (معدلات حل من رقم واحد)
  - search space (فضاء البحث)
  - program behavior (سلوك البرنامج)
  - sample count (عدد العينات)
  - false positive rate (معدل الإيجابية الخاطئة)
  - exhaustive set (مجموعة شاملة)
  - hidden tests (الاختبارات المخفية)

- **Tools/Systems mentioned:** FlashFill, Codex - kept in English as proper nouns

- **Competitions:** ICPC - kept as abbreviation

- **Performance metrics:**
  - 30% or more false positives in existing datasets
  - 30-60% → 4% improvement in false positive rate
  - "Low single-digit solve rates" for Codex on competitive programming
  - "Top 54.3%" average ranking for AlphaCode
  - 60,000 students from 3,000 universities in ICPC

- **Mathematical notation:** k (sample count) - preserved

- **Direct quotes:** Preserved in quotation marks in both versions

- **Table references:** LABEL:tab:human-eval - kept as in original (internal reference)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Validation

The Arabic translation accurately conveys: program synthesis history (deductive synthesis with theorem provers, input/output examples like FlashFill, sketch-based approaches with program skeletons, limitations to domain-specific languages or short snippets), transformer-based approaches (recent large-scale models successfully generating simple Python code, Codex performance on simple tasks matching baseline, but low single-digit solve rates on competitive programming), scaling sampling contributions (large-scale sampling for search space exploration followed by behavior-based filtering, log-linear scaling of solve rates with sample count k), evaluation metric challenges (30%+ false positives in existing datasets, CodeContests reducing 30-60% to 4%), and competitive programming context (difficulty ratings with point values, exhaustive hidden test sets vs simple benchmarks, ICPC with 60,000 students from 3,000 universities, AlphaCode's top 54.3% as genuinely competitive).
