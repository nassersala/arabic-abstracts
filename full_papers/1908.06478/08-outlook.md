# Section 8: Outlook
## القسم 8: التوقعات المستقبلية

**Section:** outlook
**Translation Quality:** 0.86
**Glossary Terms Used:** type system, polymorphism, compiler, analysis, optimization

---

### English Version

The tool described in this paper was implemented as part of a master's thesis. [12] The goal of this thesis was to provide an initial implementation, which can then be used as a basis for future improvements. While our analysis already works on a substantial subset of Haskell, there still are several flaws that severely inhibit its usefulness. In this section, we will discuss some of the shortcomings that may be used as a starting point for any future work.

The biggest issue of our current work is the lack of support for polymorphism. As we previously discussed in section 3, we specifically chose GHC Core over STG for our analysis with future support for polymorphism in mind; But as our type system is based on JVFH, which does not feature polymorphism at all, this feature is also missing in our current implementation. While the type syntax does include type variables, these may only be used as recursive references in an algebraic type; And several inference rules in the JVFH type system (which we currently reuse without alterations) were written with this assumption in mind. Therefore, providing full support for polymorphism may require large modifications to our type system.

We currently also do not support the "Cast" and "Coercion" expressions of GHC Core. These are used by the compiler to support types defined via newtype, as well as several Haskell language extensions such as GADT, associated types, and functional dependencies. [13] Therefore, none of these features are currently supported in our analysis. As of yet, we have not investigated which modifications to our type system would be necessary to support these two expressions.

Multi-module programs also are not supported yet; Therefore, we cannot analyze any expressions that contain variables imported from different modules, including the Prelude. In some cases, however, the compiler may automatically inline function calls, circumventing this limitation. This is the reason why we can use the operators + and $ in the example codes in the previous section.

We also have not formally proven the soundness of our adapted type system. For this purpose, it would be necessary to define the cost-annotated operational semantics for GHC Core; and to show that type annotations calculated by our analysis are always greater or equal to the costs determined by the operational semantics. As we have previously discussed in sections 5 and 7, it may also be necessary to revisit the soundness proof for the original LETAND† rule [10].

---

### النسخة العربية

تم تطبيق الأداة الموصوفة في هذه الورقة كجزء من رسالة ماجستير. [12] كان هدف هذه الرسالة هو توفير تطبيق أولي، والذي يمكن بعد ذلك استخدامه كأساس للتحسينات المستقبلية. بينما يعمل تحليلنا بالفعل على مجموعة فرعية كبيرة من Haskell، لا تزال هناك عدة عيوب تعيق بشدة فائدته. في هذا القسم، سنناقش بعض أوجه القصور التي قد تُستخدم كنقطة بداية لأي عمل مستقبلي.

المشكلة الأكبر في عملنا الحالي هي عدم دعم تعدد الأشكال. كما ناقشنا سابقاً في القسم 3، اخترنا على وجه التحديد GHC Core على STG لتحليلنا مع وضع الدعم المستقبلي لتعدد الأشكال في الاعتبار؛ لكن نظراً لأن نظام الأنواع لدينا يعتمد على JVFH، الذي لا يتضمن تعدد الأشكال على الإطلاق، فإن هذه الميزة مفقودة أيضاً في تطبيقنا الحالي. بينما تتضمن صياغة الأنواع متغيرات الأنواع، فإنه لا يمكن استخدامها إلا كمراجع تكرارية في نوع جبري؛ وقد تمت كتابة عدة قواعد استنتاج في نظام أنواع JVFH (والتي نعيد استخدامها حالياً دون تعديلات) مع وضع هذا الافتراض في الاعتبار. لذلك، قد يتطلب توفير دعم كامل لتعدد الأشكال تعديلات كبيرة على نظام الأنواع لدينا.

حالياً أيضاً لا ندعم تعبيرات "Cast" و "Coercion" في GHC Core. يتم استخدامها من قبل المترجم لدعم الأنواع المحددة عبر newtype، بالإضافة إلى عدة امتدادات للغة Haskell مثل GADT والأنواع المرتبطة والتبعيات الوظيفية. [13] لذلك، لا تُدعم أي من هذه الميزات حالياً في تحليلنا. حتى الآن، لم نحقق في التعديلات التي ستكون ضرورية لنظام الأنواع لدينا لدعم هذين التعبيرين.

البرامج متعددة الوحدات أيضاً غير مدعومة بعد؛ لذلك، لا يمكننا تحليل أي تعبيرات تحتوي على متغيرات مستوردة من وحدات مختلفة، بما في ذلك Prelude. في بعض الحالات، مع ذلك، قد يُدرج المترجم تلقائياً استدعاءات الدوال بشكل مضمّن، متجاوزاً هذا القيد. هذا هو السبب في أننا يمكننا استخدام المعاملات + و $ في أمثلة الشفرة في القسم السابق.

لم نثبت أيضاً رسمياً صحة نظام الأنواع المكيّف لدينا. لهذا الغرض، سيكون من الضروري تعريف دلالات التشغيل المُعلّمة بالتكلفة لـ GHC Core؛ وإظهار أن تعليمات الأنواع المحسوبة بواسطة تحليلنا دائماً أكبر من أو تساوي التكاليف المحددة بواسطة دلالات التشغيل. كما ناقشنا سابقاً في القسمين 5 و 7، قد يكون من الضروري أيضاً إعادة النظر في إثبات صحة قاعدة LETAND† الأصلية [10].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - future improvements (تحسينات مستقبلية)
  - shortcomings (أوجه قصور)
  - newtype (newtype - kept in English as technical term)
  - GADT (GADT - kept in English as acronym)
  - associated types (أنواع مرتبطة)
  - functional dependencies (تبعيات وظيفية)
  - inline (مضمّن)
  - operational semantics (دلالات التشغيل)
  - cost-annotated (مُعلّمة بالتكلفة)
- **Equations:** None
- **Citations:** [10, 12, 13]
- **Special handling:**
  - Technical Haskell terms (newtype, GADT) kept in English
  - Operator symbols (+, $) preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation (First & Last Paragraphs)

**First paragraph:** The tool described in this paper was implemented as part of a master's thesis. [12] The goal of this thesis was to provide an initial implementation, which can then be used as a basis for future improvements. While our analysis already works on a substantial subset of Haskell, there are still several flaws that severely inhibit its usefulness. In this section, we will discuss some of the shortcomings that may be used as a starting point for any future work.

**Last paragraph:** We also have not formally proven the soundness of our adapted type system. For this purpose, it would be necessary to define the cost-annotated operational semantics for GHC Core; and to show that type annotations calculated by our analysis are always greater than or equal to the costs determined by the operational semantics. As we previously discussed in sections 5 and 7, it may also be necessary to revisit the soundness proof for the original LETAND† rule [10].
