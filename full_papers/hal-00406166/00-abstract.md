# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** algorithm, probabilistic, memory, accuracy, analysis, data, cardinality, estimation, distinct elements, near-optimal, standard error, single pass, auxiliary, sliding window, parallelize

---

### English Version

This extended abstract describes and analyses a near-optimal probabilistic algorithm, HYPERLOGLOG, dedicated to estimating the number of distinct elements (the cardinality) of very large data ensembles. Using an auxiliary memory of m units (typically, "short bytes"), HYPERLOGLOG performs a single pass over the data and produces an estimate of the cardinality such that the relative accuracy (the standard error) is typically about 1.04/√m. This improves on the best previously known cardinality estimator, LOGLOG, whose accuracy can be matched by consuming only 64% of the original memory. For instance, the new algorithm makes it possible to estimate cardinalities well beyond 10^9 with a typical accuracy of 2% while using a memory of only 1.5 kilobytes. The algorithm parallelizes optimally and adapts to the sliding window model.

---

### النسخة العربية

تصف هذه الخلاصة الموسعة وتحلل خوارزمية احتمالية شبه مثالية، HYPERLOGLOG، مخصصة لتقدير عدد العناصر المتمايزة (العددية) في مجموعات بيانات كبيرة جداً. باستخدام ذاكرة مساعدة من m وحدة (عادةً "بايتات قصيرة")، تنفذ HYPERLOGLOG ممراً واحداً عبر البيانات وتنتج تقديراً للعددية بحيث تكون الدقة النسبية (الخطأ المعياري) عادةً حوالي 1.04/√m. يحسن هذا على أفضل مقدِّر عددية معروف سابقاً، LOGLOG، حيث يمكن مطابقة دقته باستهلاك 64% فقط من الذاكرة الأصلية. على سبيل المثال، تجعل الخوارزمية الجديدة من الممكن تقدير عدديات تتجاوز 10^9 بكثير بدقة نموذجية تبلغ 2% بينما تستخدم ذاكرة قدرها 1.5 كيلوبايت فقط. تتوازى الخوارزمية بشكل مثالي وتتكيف مع نموذج النافذة المنزلقة.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** cardinality (العددية), estimation (تقدير), distinct elements (عناصر متمايزة), standard error (الخطأ المعياري), auxiliary memory (ذاكرة مساعدة)
- **Equations:** Mathematical notation 1.04/√m, 10^9, 64%, 2%, 1.5 kilobytes
- **Citations:** None in abstract
- **Special handling:** Algorithm name HYPERLOGLOG and LOGLOG kept in English

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.92
