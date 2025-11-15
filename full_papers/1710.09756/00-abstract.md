# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.89
**Glossary Terms Used:** type system, functional programming, compiler, higher-order, polymorphism, linear types

---

### English Version

The paper presents a linear type system designed for integration with existing functional programming languages. Rather than creating separate linear and non-linear type variants, the approach "attach[es] linearity to function arrows." Linear functions can accept inputs from linearly-bound values while also operating on unrestricted values. The authors implemented their system in GHC (Haskell compiler) and demonstrated two applications: "mutable data with pure interfaces; and enforcing protocols in I/O-performing functions."

---

### النسخة العربية

يقدم البحث نظام أنواع خطي مصمماً للتكامل مع لغات البرمجة الوظيفية الموجودة. بدلاً من إنشاء متغيرات نوع خطية وغير خطية منفصلة، يقوم النهج "بإرفاق الخطية بأسهم الدوال". يمكن للدوال الخطية قبول المدخلات من القيم المرتبطة خطياً مع العمل أيضاً على القيم غير المقيدة. نفذ المؤلفون نظامهم في GHC (مترجم Haskell) وأظهروا تطبيقين: "بيانات قابلة للتغيير بواجهات نقية؛ وفرض البروتوكولات في الدوال التي تؤدي عمليات الإدخال/الإخراج".

---

### Translation Notes

- **Key terms introduced:** linear type system (نظام الأنواع الخطي), function arrows (أسهم الدوال), linearly-bound values (القيم المرتبطة خطياً), unrestricted values (القيم غير المقيدة)
- **Applications mentioned:** mutable data (بيانات قابلة للتغيير), pure interfaces (واجهات نقية), I/O protocols (بروتوكولات الإدخال/الإخراج)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89
