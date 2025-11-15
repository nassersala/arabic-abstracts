# Section 4: Implementing Linear Haskell
## القسم 4: تنفيذ Haskell الخطي

**Section:** Implementation
**Translation Quality:** 0.86
**Glossary Terms Used:** compiler, type system, type inference, implementation, GHC

---

### English Version

We implement Linear Haskell on top of the leading Haskell compiler, GHC, version 8.2. The implementation modifies type inference and type-checking in the compiler. Neither the intermediate language nor the run-time system are affected. Our implementation of multiplicity polymorphism is incomplete, but the current prototype is sufficient for the examples and case studies presented in this paper (see Sec. 5).

In order to implement the linear arrow, we added a multiplicity annotation to function arrows as in λq→. The constructor for arrow types is constructed and destructed frequently in GHC's type checker, and this accounts for most of the modifications to existing code.

As suggested in Sec. 3.2, the multiplicities are an output of the type inference algorithm. In order to infer the multiplicities coming out of a case expression we need a way to aggregate the multiplicities coming out of the individual branches. To this effect, we compute, for every variable, the join of its multiplicity in each branch.

Implementing Linear Haskell affects 1,152 lines of GHC (in subsystems of the compiler that together amount to more than 100k lines of code), including 444 net extra lines. These figures support our claim that Linear Haskell is easy to integrate into an existing implementation: despite GHC being 25 years old, we implement a first version of Linear Haskell with reasonable effort.

---

### النسخة العربية

ننفذ Haskell الخطي على قمة مترجم Haskell الرائد، GHC، الإصدار 8.2. يعدل التنفيذ استدلال الأنواع وفحص الأنواع في المترجم. لا تتأثر اللغة الوسيطة ولا نظام وقت التشغيل. تنفيذنا لتعددية الأشكال التعددية غير مكتمل، لكن النموذج الأولي الحالي كافٍ للأمثلة ودراسات الحالة المقدمة في هذا البحث (انظر القسم 5).

من أجل تنفيذ السهم الخطي، أضفنا تعليقاً توضيحياً للتعددية إلى أسهم الدوال كما في λq→. يتم إنشاء وتفكيك المُنشئ لأنواع الأسهم بشكل متكرر في مدقق الأنواع في GHC، وهذا يمثل معظم التعديلات على الشفرة الموجودة.

كما اقترح في القسم 3.2، التعدديات هي ناتج خوارزمية استدلال الأنواع. من أجل استنتاج التعدديات الناتجة من تعبير حالة، نحتاج إلى طريقة لتجميع التعدديات الناتجة من الفروع الفردية. لهذا الغرض، نحسب، لكل متغير، الاتحاد (join) لتعدديته في كل فرع.

يؤثر تنفيذ Haskell الخطي على 1,152 سطراً من GHC (في أنظمة فرعية من المترجم تصل معاً إلى أكثر من 100 ألف سطر من الشفرة)، بما في ذلك 444 سطراً إضافياً صافياً. تدعم هذه الأرقام ادعاءنا بأن Haskell الخطي سهل الدمج في تنفيذ موجود: على الرغم من أن GHC يبلغ من العمر 25 عاماً، فإننا ننفذ نسخة أولى من Haskell الخطي بجهد معقول.

---

### Translation Notes

- **Key terms introduced:**
  - Type inference (استدلال الأنواع)
  - Type-checking (فحص الأنواع)
  - Intermediate language (اللغة الوسيطة)
  - Run-time system (نظام وقت التشغيل)
- **Statistics:** Code modification statistics preserved
- **Implementation details:** Technical aspects maintained in translation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
