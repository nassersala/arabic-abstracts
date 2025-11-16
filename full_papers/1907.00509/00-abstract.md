# Section 0: Abstract
## القسم 0: الملخص

**Section:** Abstract
**Translation Quality:** 0.88
**Glossary Terms Used:** لغات البرمجة, دوال, مصفوفات, البُعد, البرمجة الوظيفية, دلاليات, نظام الأنواع, مترجم, وقت التشغيل, نموذج حسابي

---

### English Version

Iverson's APL and its descendants (such as J, K and FISh) exemplify "rank-polymorphic" programming languages, which use "the general lifting of functions that operate on arrays of rank (or dimension) r to operate on arrays of any higher rank r' > r" as their primary control mechanism. This work introduces Remora, a functional language embodying this mechanism, along with both formal dynamic semantics and an accompanying static, rank-polymorphic type system. The static semantics captures shape-based lifting mechanisms. The authors establish progress and preservation properties, demonstrating soundness such that "array shape" errors cannot occur at runtime in well-typed programs. The type system employs dependent types with existential type abstractions, enabling operations on dynamically computed array shapes while remaining statically checkable. Additionally, the paper presents a dynamic semantics for a partially erased variant and demonstrates computational equivalence between fully-typed and partially-erased variants, precisely characterizing necessary type information for compiler construction.

---

### النسخة العربية

APL لـ Iverson وسلالاته (مثل J وK وFISh) تُجسد لغات البرمجة "متعددة الأشكال حسب الرتبة"، والتي تستخدم "الرفع العام للدوال التي تعمل على مصفوفات من الرتبة (أو البُعد) r لتعمل على مصفوفات من أي رتبة أعلى r' > r" كآلية التحكم الأساسية لها. يقدم هذا العمل Remora، لغة وظيفية تجسد هذه الآلية، مع دلاليات ديناميكية رسمية ونظام أنواع ثابت متعدد الأشكال حسب الرتبة مصاحب. تلتقط الدلاليات الثابتة آليات الرفع القائمة على الشكل. يثبت المؤلفون خصائص التقدم والحفظ، مُظهرين صحة بحيث لا يمكن أن تحدث أخطاء "شكل المصفوفة" في وقت التشغيل في البرامج المكتوبة جيداً. يستخدم نظام الأنواع أنواعاً معتمدة مع تجريدات أنواع وجودية، مما يمكّن من العمليات على أشكال المصفوفات المحسوبة ديناميكياً مع البقاء قابلة للفحص بشكل ثابت. بالإضافة إلى ذلك، تقدم الورقة دلاليات ديناميكية لنسخة ممحوة جزئياً وتُظهر التكافؤ الحسابي بين النسختين المكتوبة بالكامل والممحوة جزئياً، مُحددة بدقة معلومات الأنواع الضرورية لبناء المترجم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Rank polymorphism (تعدد الأشكال حسب الرتبة)
  - Lifting (الرفع)
  - Array shape (شكل المصفوفة)
  - Dependent types (الأنواع المعتمدة)
  - Existential type abstractions (تجريدات الأنواع الوجودية)
  - Type erasure (محو الأنواع)
- **Equations:** None
- **Citations:** None in abstract
- **Special handling:**
  - Language names (APL, J, K, FISh, Remora) kept in English
  - Technical terms translated consistently with glossary

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.90
- **Overall section score:** 0.88

### Back-Translation (Validation)

Iverson's APL and its descendants (such as J, K, and FISh) embody "rank-polymorphic" programming languages, which use "the general lifting of functions that operate on arrays of rank (or dimension) r to operate on arrays of any higher rank r' > r" as their primary control mechanism. This work introduces Remora, a functional language embodying this mechanism, with formal dynamic semantics and an accompanying static rank-polymorphic type system. The static semantics captures shape-based lifting mechanisms. The authors prove progress and preservation properties, demonstrating soundness such that "array shape" errors cannot occur at runtime in well-typed programs. The type system uses dependent types with existential type abstractions, enabling operations on dynamically computed array shapes while remaining statically checkable. Additionally, the paper presents dynamic semantics for a partially erased variant and demonstrates computational equivalence between fully-typed and partially-erased variants, precisely determining the type information necessary for compiler construction.

**Validation:** ✅ Semantic match confirmed. The back-translation preserves the original meaning accurately.
