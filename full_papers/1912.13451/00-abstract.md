# Abstract: Introduction to Rank-polymorphic Programming in Remora
## الملخص: مقدمة إلى البرمجة متعددة الأشكال حسب الرتبة في Remora

**Section:** abstract
**Translation Quality:** 0.89
**Glossary Terms Used:** لغة البرمجة, مصفوفات, التوازي, نموذج حسابي, نظام الأنواع, مترجم, استنتاج

---

### English Version

Remora is a higher-order, rank-polymorphic array-processing programming language, in the same general class of languages as APL and J. It is intended for writing programs to be executed on parallel hardware.

We provide an example-driven introduction to the language and its general computational model, originally developed by Iverson for APL. We begin with Dynamic Remora, a variant of the language with a dynamic type system (as in Scheme or Lisp), to introduce the fundamental computational mechanisms of the language, then shift to Explicitly Typed Remora, a variant of the language with a static, dependent type system that permits the shape of the arrays being computed to be captured at compile time.

This article can be considered an introduction to the general topic of the rank-polymorphic array-processing computational model, above and beyond the specific details of the Remora language. A reader generally interested in the topic of the computational model that serves as the foundation for this entire class of languages should find the tutorial informative.

We do not address the details of type inference in Remora, that is, the assignment of explicit types to programs written without such annotations; this is ongoing research.

---

### النسخة العربية

Remora هي لغة برمجة عالية المستوى متعددة الأشكال حسب الرتبة لمعالجة المصفوفات في نفس الفئة العامة مثل APL وJ، مصممة لتنفيذ الأجهزة المتوازية.

توفر الورقة مقدمة موجهة بالأمثلة للغة ونموذجها الحسابي، الذي أنشأه Iverson أصلاً لـ APL. تغطي نسختين من اللغة: Remora الديناميكية مع الكتابة الديناميكية (مشابهة لـ Scheme أو Lisp) وRemora المكتوبة بشكل صريح مع نظام أنواع ثابت يعتمد على الاعتماديات يمكّن من التقاط شكل المصفوفة في وقت الترجمة.

يعمل المقال كمقدمة لمعالجة المصفوفات متعددة الأشكال حسب الرتبة كنموذج حسابي بشكل عام، بعيداً عن تفاصيل Remora المحددة. القارئ المهتم بشكل عام بالنموذج الحسابي الذي يعمل كأساس لهذه الفئة بأكملها من اللغات سيجد هذا الدليل التعليمي مفيداً.

تفاصيل استنتاج الأنواع تبقى غير معالجة كبحث جارٍ، أي تعيين الأنواع الصريحة للبرامج المكتوبة بدون مثل هذه التعليقات التوضيحية.

---

### Translation Notes

- **Key terms introduced:** rank-polymorphic (متعددة الأشكال حسب الرتبة), array-processing (معالجة المصفوفات), parallel hardware (أجهزة متوازية), computational model (نموذج حسابي), dynamic type system (نظام أنواع ديناميكي), dependent type system (نظام أنواع يعتمد على الاعتماديات), type inference (استنتاج الأنواع)
- **Programming languages mentioned:** APL, J, Scheme, Lisp, Remora
- **Special handling:** Technical terminology preserved where appropriate (e.g., Iverson's name)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89

### Back-Translation

Remora is a high-level rank-polymorphic array-processing programming language in the same general category as APL and J, designed for parallel hardware execution. The paper provides an example-driven introduction to the language and its computational model, originally created by Iverson for APL. It covers two language variants: Dynamic Remora with dynamic typing (similar to Scheme or Lisp) and Explicitly Typed Remora with a static dependent type system that enables array shape capture at compile time. The article works as an introduction to rank-polymorphic array processing as a computational model in general, beyond Remora-specific details. Readers generally interested in the computational model that serves as the foundation for this entire class of languages will find this tutorial helpful. Type inference details remain unaddressed as ongoing research, namely the assignment of explicit types to programs written without such annotations.
