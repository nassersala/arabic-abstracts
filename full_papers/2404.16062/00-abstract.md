# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** property-based testing, parallelism, testing, benchmark, shrinking, counterexample

---

### English Version

This work presents a parallel runtime system for QuickCheck, a Haskell testing framework. The system enables multiple tests for a single property in parallel, using the available cores, and supports parallel test case shrinking. The authors report achieving 3–9× speed-up for testing QuickCheck properties across various benchmarks. They evaluate two shrinking approaches: deterministic shrinking, which ensures identical minimal counterexamples to sequential execution, and greedy shrinking, which offers faster results without this guarantee.

---

### النسخة العربية

يقدم هذا العمل نظام وقت تشغيل متوازي لـ QuickCheck، وهو إطار اختبار Haskell. يمكّن النظام اختبارات متعددة لخاصية واحدة بالتوازي، باستخدام النوى المتاحة، ويدعم تقليص حالة الاختبار بالتوازي. يبلغ المؤلفون عن تحقيق تسريع من 3 إلى 9 مرات لاختبار خصائص QuickCheck عبر معايير مختلفة. يقيّمون نهجين للتقليص: التقليص الحتمي، الذي يضمن أمثلة مضادة دنيا متطابقة للتنفيذ التسلسلي، والتقليص الجشع، الذي يوفر نتائج أسرع دون هذا الضمان.

---

### Translation Notes

- **Key terms introduced:** QuickCheck (kept in Latin), property-based testing, parallel runtime, shrinking, counterexample, deterministic shrinking, greedy shrinking
- **Citations:** None in abstract
- **Special handling:** Technical terminology for testing and parallelism

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.89
- Glossary consistency: 0.90
- **Overall section score:** 0.90
