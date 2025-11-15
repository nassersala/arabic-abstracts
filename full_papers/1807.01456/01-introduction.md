# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** computational algebra, algorithm, composable, functional programming, domain-specific language, type system, lazy evaluation, declarative, purity, property-based testing, embedded systems

---

### English Version

In the last few decades, the area of computational algebra has grown larger. Many algorithms have been proposed, and there have emerged plenty of computer algebra systems. Such systems must achieve correctness, composability and safety so that one can implement and examine new algorithms within them. More specifically, we want to achieve the following goals:

**Composability** means that users can easily implement algorithms or mathematical objects so that they work seamlessly with existing features.

**Safety** prevents users and implementors from writing "wrong" code. For example, elements in different rings, e.g. Q[x, y, z] and Q[w, x, y], should be treated differently and must not directly be added. Also, it is convenient to have handy ways to convert, inject, or coerce such values.

**Correctness** of algorithms, with respect to prescribed formal specifications, should be guaranteed with a high assurance.

We apply methods in the area of functional programming to achieve these goals. As a proof-of-concept, we present the computational-algebra package [12]. It is implemented as an embedded domain-specific language in the Haskell Language [10]. More precisely, we adopt the Glasgow Haskell Compiler (GHC) [7] as our hosting language. We use GHC because: its type-system allows us to build a safe and composable interface for computer algebra; lazy evaluation enables us to treat infinite objects intuitively; declarative style sometimes reduces a burden of writing mathematical programs; purity permits a wide range of equational optimisation; and there is a plenty of libraries for functional methods, especially property-based testing. These methods are not widely adopted in this area; an exception is DoCon [23], a pioneering work combining Haskell and computer algebra. Our system is designed with more emphasis on safety and correctness than DoCon, adding more ingredients. Although we use a functional language, some methods in this paper are applicable in imperative languages.

This paper is organised as follows. In Section 2, we discuss how the progressive type-system of GHC enables us to build a safe and expressive type-system for a computer algebra. Then, in Section 3, we see how the method of property-based testing can be applied to verify the correctness of algebraic programs in a lightweight and top-down manner. To demonstrate the practical advantages of Haskell, Section 4 gives a brief description of the current implementations of the Hilbert-driven, F₄ and F₅ algorithms. We also take a simple benchmark there. We summarise the paper and discuss related and future works in Section 5.

In what follows, we use symbols in Table 1 in code fragments for readability.

---

### النسخة العربية

في العقود القليلة الماضية، نما مجال الجبر الحاسوبي بشكل كبير. تم اقتراح العديد من الخوارزميات، وظهرت الكثير من أنظمة الجبر الحاسوبي. يجب أن تحقق هذه الأنظمة الصحة وقابلية التركيب والأمان حتى يتمكن المرء من تطبيق وفحص خوارزميات جديدة داخلها. بشكل أكثر تحديداً، نريد تحقيق الأهداف التالية:

**قابلية التركيب** تعني أن المستخدمين يمكنهم بسهولة تطبيق الخوارزميات أو الكائنات الرياضية بحيث تعمل بسلاسة مع الميزات الموجودة.

**الأمان** يمنع المستخدمين والمطورين من كتابة شفرة "خاطئة". على سبيل المثال، يجب معاملة العناصر في الحلقات المختلفة، مثل Q[x, y, z] و Q[w, x, y]، بشكل مختلف ويجب عدم جمعها مباشرة. أيضاً، من المريح وجود طرق سهلة لتحويل أو حقن أو إكراه مثل هذه القيم.

**الصحة** للخوارزميات، بالنسبة للمواصفات الرسمية المحددة، يجب ضمانها بضمان عالٍ.

نطبق أساليب في مجال البرمجة الوظيفية لتحقيق هذه الأهداف. كإثبات للمفهوم، نقدم حزمة computational-algebra [12]. تم تنفيذها كلغة خاصة بالمجال مدمجة في لغة Haskell [10]. بشكل أكثر دقة، نعتمد مترجم Glasgow Haskell Compiler (GHC) [7] كلغتنا المضيفة. نستخدم GHC لأن: نظام الأنواع الخاص به يسمح لنا ببناء واجهة آمنة وقابلة للتركيب للجبر الحاسوبي؛ التقييم الكسول يمكننا من معاملة الكائنات اللانهائية بشكل بديهي؛ النمط التصريحي يقلل أحياناً من عبء كتابة البرامج الرياضية؛ النقاء يسمح بمجموعة واسعة من التحسين المعادلاتي؛ ويوجد الكثير من المكتبات للأساليب الوظيفية، وخاصة الاختبار القائم على الخصائص. هذه الأساليب ليست مستخدمة على نطاق واسع في هذا المجال؛ استثناء واحد هو DoCon [23]، وهو عمل رائد يجمع بين Haskell والجبر الحاسوبي. تم تصميم نظامنا مع المزيد من التركيز على الأمان والصحة مقارنة بـ DoCon، مع إضافة المزيد من المكونات. على الرغم من أننا نستخدم لغة وظيفية، إلا أن بعض الأساليب في هذه الورقة قابلة للتطبيق في اللغات الإلزامية.

يتم تنظيم هذه الورقة على النحو التالي. في القسم 2، نناقش كيف يمكننا نظام الأنواع التقدمي لـ GHC من بناء نظام أنواع آمن ومعبر للجبر الحاسوبي. ثم، في القسم 3، نرى كيف يمكن تطبيق طريقة الاختبار القائم على الخصائص للتحقق من صحة البرامج الجبرية بطريقة خفيفة الوزن ومن أعلى إلى أسفل. لإظهار المزايا العملية لـ Haskell، يقدم القسم 4 وصفاً موجزاً للتطبيقات الحالية لخوارزميات Hilbert-driven و F₄ و F₅. نأخذ أيضاً معياراً بسيطاً هناك. نلخص الورقة ونناقش الأعمال ذات الصلة والمستقبلية في القسم 5.

فيما يلي، نستخدم الرموز في الجدول 1 في أجزاء الشفرة لسهولة القراءة.

---

### Translation Notes

- **Figures referenced:** Table 1 (Symbols in Code Fragments)
- **Key terms introduced:** composability (قابلية التركيب), safety (الأمان), correctness (الصحة), lazy evaluation (التقييم الكسول), equational optimisation (التحسين المعادلاتي)
- **Equations:** 0
- **Citations:** [7] GHC, [10] Haskell Language, [12] computational-algebra package, [23] DoCon
- **Special handling:**
  - Preserved mathematical notation: Q[x, y, z] and Q[w, x, y]
  - Preserved programming language and system names in English
  - Table 1 reference maintained

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
