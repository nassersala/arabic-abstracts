# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** analysis, compiler, functional programming, type system, resource usage, lazy evaluation, amortized analysis

---

### English Version

We propose an amortized analysis that approximates the resource usage of a Haskell expression. Using the plugin API of GHC, we convert the Haskell code into a simplified representation called GHC Core. We then apply a type-based system which derives linear upper bounds on the resource usage. This setup allows us to analyze actual Haskell code, whereas previous implementations of similar analyses do not support any commonly used lazy functional programming languages.

---

### النسخة العربية

نقترح تحليلاً مطفأً يقرّب استخدام الموارد لتعبير Haskell. باستخدام واجهة برمجة التطبيقات للإضافات في GHC، نحول شفرة Haskell إلى تمثيل مبسط يسمى GHC Core. ثم نطبق نظاماً قائماً على الأنواع يستنتج حدوداً عليا خطية على استخدام الموارد. يسمح لنا هذا الإعداد بتحليل شفرة Haskell الفعلية، بينما لا تدعم التطبيقات السابقة للتحليلات المماثلة أي لغات برمجة وظيفية كسولة شائعة الاستخدام.

---

### Translation Notes

- **Key terms introduced:** amortized analysis (التحليل المطفأ), GHC Core, type-based system (نظام قائم على الأنواع), linear upper bounds (حدود عليا خطية), lazy functional programming (البرمجة الوظيفية الكسولة)
- **Special handling:** GHC (Glasgow Haskell Compiler) kept in English as it's a proper name

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.89
- Glossary consistency: 0.90
- **Overall section score:** 0.90

### Back-Translation (Validation)

We propose an amortized analysis that approximates resource usage for a Haskell expression. Using the plugin API in GHC, we convert Haskell code into a simplified representation called GHC Core. We then apply a type-based system that derives linear upper bounds on resource usage. This setup allows us to analyze actual Haskell code, while previous implementations of similar analyses do not support any commonly used lazy functional programming languages.
