# Section 2: Type System for Safety and Composability
## القسم 2: نظام الأنواع للأمان وقابلية التركيب

**Section:** type-system
**Translation Quality:** 0.87
**Glossary Terms Used:** type system, dependent types, type-level functions, ad-hoc polymorphism, algebraic, polynomial, monomial, composable, safety, rewriting rules, purity

---

### English Version

In this section, we will see how the progressive type-level functionalities of GHC can be exploited to construct a safe, composable and flexible type-system for a computer algebra system. There are several existing works on type-systems for computer algebra, such as in Java and Scala [18, 15], and DoCon. However, none of them achieves the same level of safety and composability as our approach, which utilises the power of dependent types and type-level functions.

#### 2.1 Type Classes to Encode Algebraic Hierarchy

We use type-classes, an ad-hoc polymorphism mechanism in Haskell, to encode an algebraic hierarchy. This idea is not particularly new (for example, see Mechveliani [23] or Jolly [15]), and we build our system on top of the existing algebra package [17], which provides a fine-grained abstract algebraic hierarchy.

**Code 1** illustrates a simplified version of the algebraic hierarchy up to Group provided by the algebra package. Each statement between `class` or `⇒` and `where`, such as `Additive a` or `Monoidal a`, expresses the constraint for types. For example, Lines 1 and 2 express "a type `a` is Additive if it is endowed with a binary operation `+`", and Lines 3 and 4 that "a type `a` is Monoidal if it is Additive and has a distinguished element called `zero`".

Note that, none of these requires the "proof" of algebraic axioms. Hence, one can accidentally write a non-associative Additive-instance, or non-distributive Ring-instance. This sounds rather "unsafe", and we will see how this could be addressed reasonably in Section 3.

#### 2.2 Classes for Polynomials and Dependent Types

Expressing algebraic hierarchy using type-class hierarchy, or class inheritance, is not so new and they are already implemented in DoCon or JAS. However, these systems lack a functionality to distinguish the arity of polynomials or the denominator of a quotient ring. In particular, DoCon uses sample arguments to indicate such parameters, and they cannot be checked at compile-time. To overcome these restrictions, we use Dependent Types.

For example, **Code 2** presents the simplified definition of the class `IsOrdPoly` for polynomials. We provide an abstract class for polynomials, not just an implementation, to enable users to choose appropriate internal representations fitting their use-cases.

The class definition includes not only functions, but also associated types, or type-level functions: `Arity`, `MOrder` and `Coeff`. Respectively, they correspond to the number of variables, the monomial ordering and the coefficient ring.

Note that `liftMap` corresponds to the universality of the polynomial ring R[X₁, . . . , Xₙ]; i.e. the free associative commutative R-algebra over {1, . . . , n}. In theory, this function suffices to characterise the polynomial ring. However, for the sake of efficiency, we also include some other operations in the definition.

**Code 3** shows example instance definitions for the standard multivariate and univariate polynomial ring types. Note that, in Lines 8 and 12, number literal expressions 1 and 3 occur in type contexts. Types depending on expressions are called Dependent Types in type theory. GHC supports them via the Promoted Data-types language extension [27] since version 7.4. Our library heavily uses this functionality, and achieves the type-safety preventing users from unintendedly confusing elements from different rings.

#### 2.3 Proofs in Dependent Types and Type-driven Casting Function

In theory, we can use `liftMap` to cast between any elements of "compatible" polynomial rings. To reduce the burden to write boilerplate casting functions, our library comes with smart functions, as shown in **Code 4**. The `convPoly` function maps a polynomial into one with the same setting but different representation; e.g. `OrdPoly Q Lex 1` into `Unipol Q`. The next `injVars` function maps an element of R[X₁, . . . , Xₙ] into another polynomial ring with the same coefficient ring, but with more number of variables, e.g. R[X₁, . . . , Xₙ₊ₘ], regardless of ordering. For example, it maps `Unipol Q` into `OrdPoly Q Grevelx 3`. Then, `injVarsOffset` is a variant of `injVars` which maps variables with offset.

To work with type-level naturals, we sometimes have to prove some constraints. For example, suppose we want to write a variant of `injVars` mapping variables to the end of those of the target polynomial ring, instead of the beginning. Although the constraint `Arity r' - Arity r + Arity r ≤ Arity r'` is rather clear to us, we have to give the compiler its proof. We have developed the type-natural package [14] which includes typical "lemmas". For example, we can use the `minusPlus` lemma to fix this.

Since giving such a proof each time is rather tedious, we can use type-checker plugins to let the compiler try to prove constraints automatically. In particular, the author developed the ghc-typelits-presburger plugin [13] to resolve propositions in Presburger arithmetic at compile time.

Our library also provides the `LabPoly` type, which converts existing polynomial types into "labelled" ones. Using the type-level information, one can invoke the canonical inclusion maps naturally.

#### 2.4 Optimising Casting Functions with Rewriting Rules

Since the casting functions are implemented generically, they sometimes introduce unnecessary overhead. For example, if one uses `injVars` with the same source and target types, it should just be the identity function. Fortunately, we can use the type-safe Rewriting Rule functionality of GHC to achieve this.

Each rewriting rule fires at compile-time, if there is a term matching the left-hand side of the rule and having the same type as the right-hand side.

In Haskell, it suffices just to consider algebraic laws to write down custom rewriting rules. This is due to the purity of Haskell. That is, every expression in Haskell is pure, in a sense that they evaluate to the same result when given the same arguments. Note that this does not mean that Haskell cannot treat values with side-effects; indeed, the type-system of Haskell distinguishes pure and impure values at type-level, and one can treat impure operations without violating purity as a whole. The trick behind this situation is to describe side-effects as some kind of abstract instructions, instead of treating impure values directly. Hence, for example, duplicating the same term does not make any difference in its meaning, provided that it is algebraically correct. Such a rewriting rule is used extensively in Haskell. For example, Stream Fusion [3] uses them to eliminate unnecessary intermediate expressions and fuse complicated functions into efficient one-path constructions. Yet, DoCon did not do any optimisation using rewriting rules.

In our library, we also use rewriting rules to remove idempotent applications such as "grading" a monomial ordering twice.

#### 2.5 Notes on applicability in imperative languages

The safety we achieved in this section cannot be achieved at compile-time without dependent types and type-level functions. Existing works using type-classes or class inheritance to encode algebraic hierarchy, such as JAS or DoCon, lack this level of safety. In theory, one can achieve the same level of safety even in a statically-typed imperative language, if it supports a kind of dependent types. For example, in C++, templates with non-type arguments can be used to simulate dependent types. On the other hand, in Java, Generics do not allow non-type arguments and we need to mimic Peano numerals with classes. In either case, it requires much effort to prove the properties of naturals within them, because they lack dedicated support for type-level naturals or type-checker plugins.

On the other hand, to make use of rewriting rules, we need purity as discussed above.

---

### النسخة العربية

في هذا القسم، سنرى كيف يمكن استغلال وظائف مستوى الأنواع التقدمية في GHC لبناء نظام أنواع آمن وقابل للتركيب ومرن لنظام جبر حاسوبي. هناك عدة أعمال موجودة حول أنظمة الأنواع للجبر الحاسوبي، مثل تلك الموجودة في Java و Scala [18، 15]، و DoCon. ومع ذلك، لا يحقق أي منها نفس مستوى الأمان وقابلية التركيب كنهجنا، الذي يستخدم قوة الأنواع التابعة والدوال على مستوى الأنواع.

#### 2.1 أصناف الأنواع لترميز التسلسل الهرمي الجبري

نستخدم أصناف الأنواع (type-classes)، وهي آلية تعدد الأشكال المخصصة في Haskell، لترميز التسلسل الهرمي الجبري. هذه الفكرة ليست جديدة بشكل خاص (على سبيل المثال، انظر Mechveliani [23] أو Jolly [15])، ونبني نظامنا على حزمة algebra الموجودة [17]، والتي توفر تسلسلاً هرمياً جبرياً مجرداً دقيق الحبيبات.

يوضح **الكود 1** نسخة مبسطة من التسلسل الهرمي الجبري حتى Group المقدمة من حزمة algebra. كل تعبير بين `class` أو `⇒` و `where`، مثل `Additive a` أو `Monoidal a`، يعبر عن القيد على الأنواع. على سبيل المثال، تعبر الأسطر 1 و 2 عن "نوع `a` هو Additive إذا كان مزوداً بعملية ثنائية `+`"، والأسطر 3 و 4 تعبر عن "نوع `a` هو Monoidal إذا كان Additive ولديه عنصر متميز يسمى `zero`".

لاحظ أن، لا يتطلب أي من هذه "إثبات" البديهيات الجبرية. وبالتالي، يمكن للمرء عن طريق الخطأ كتابة نموذج Additive غير ترابطي، أو نموذج Ring غير توزيعي. هذا يبدو غير "آمن" إلى حد ما، وسنرى كيف يمكن معالجة هذا بشكل معقول في القسم 3.

#### 2.2 أصناف كثيرات الحدود والأنواع التابعة

التعبير عن التسلسل الهرمي الجبري باستخدام التسلسل الهرمي لأصناف الأنواع، أو وراثة الأصناف، ليس جديداً جداً وقد تم تنفيذها بالفعل في DoCon أو JAS. ومع ذلك، تفتقر هذه الأنظمة إلى وظيفة للتمييز بين عدد متغيرات كثيرات الحدود أو مقام حلقة القسمة. على وجه الخصوص، يستخدم DoCon وسائط عينة للإشارة إلى مثل هذه المعاملات، ولا يمكن فحصها في وقت الترجمة. للتغلب على هذه القيود، نستخدم الأنواع التابعة.

على سبيل المثال، يقدم **الكود 2** التعريف المبسط لصنف `IsOrdPoly` لكثيرات الحدود. نوفر صنفاً مجرداً لكثيرات الحدود، وليس مجرد تطبيق، لتمكين المستخدمين من اختيار التمثيلات الداخلية المناسبة التي تناسب حالات الاستخدام الخاصة بهم.

يتضمن تعريف الصنف ليس فقط الدوال، ولكن أيضاً الأنواع المرتبطة، أو الدوال على مستوى الأنواع: `Arity` و `MOrder` و `Coeff`. على التوالي، تتوافق مع عدد المتغيرات، وترتيب الأحادي الحد، وحلقة المعاملات.

لاحظ أن `liftMap` تتوافق مع عالمية حلقة كثيرات الحدود R[X₁, . . . , Xₙ]؛ أي الجبر R الترابطي التبديلي الحر على {1, . . . , n}. من الناحية النظرية، هذه الدالة كافية لوصف حلقة كثيرات الحدود. ومع ذلك، من أجل الكفاءة، نقوم أيضاً بتضمين بعض العمليات الأخرى في التعريف.

يعرض **الكود 3** أمثلة تعريفات النماذج لأنواع حلقات كثيرات الحدود القياسية متعددة المتغيرات وأحادية المتغير. لاحظ أنه، في الأسطر 8 و 12، تحدث تعبيرات الأرقام الحرفية 1 و 3 في سياقات الأنواع. تسمى الأنواع التي تعتمد على التعبيرات الأنواع التابعة في نظرية الأنواع. يدعمها GHC عبر امتداد لغة Promoted Data-types [27] منذ الإصدار 7.4. تستخدم مكتبتنا هذه الوظيفة بشكل كبير، وتحقق أمان الأنواع الذي يمنع المستخدمين من الخلط غير المقصود بين عناصر من حلقات مختلفة.

#### 2.3 البراهين في الأنواع التابعة ودالة التحويل المدفوعة بالأنواع

من الناحية النظرية، يمكننا استخدام `liftMap` للتحويل بين أي عناصر من حلقات كثيرات الحدود "المتوافقة". لتقليل عبء كتابة دوال التحويل النمطية، تأتي مكتبتنا مع دوال ذكية، كما هو موضح في **الكود 4**. تقوم دالة `convPoly` بتحويل كثير حدود إلى واحد بنفس الإعداد ولكن بتمثيل مختلف؛ على سبيل المثال `OrdPoly Q Lex 1` إلى `Unipol Q`. تقوم دالة `injVars` التالية بتحويل عنصر من R[X₁, . . . , Xₙ] إلى حلقة كثيرات حدود أخرى بنفس حلقة المعاملات، ولكن بعدد أكبر من المتغيرات، على سبيل المثال R[X₁, . . . , Xₙ₊ₘ]، بغض النظر عن الترتيب. على سبيل المثال، تحول `Unipol Q` إلى `OrdPoly Q Grevelx 3`. ثم، `injVarsOffset` هي نسخة من `injVars` تحول المتغيرات مع إزاحة.

للعمل مع الأرقام الطبيعية على مستوى الأنواع، يتعين علينا أحياناً إثبات بعض القيود. على سبيل المثال، لنفترض أننا نريد كتابة نسخة من `injVars` تحول المتغيرات إلى نهاية متغيرات حلقة كثيرات الحدود المستهدفة، بدلاً من البداية. على الرغم من أن القيد `Arity r' - Arity r + Arity r ≤ Arity r'` واضح تماماً بالنسبة لنا، يجب أن نعطي المترجم إثباته. لقد طورنا حزمة type-natural [14] التي تتضمن "المبرهنات" النموذجية. على سبيل المثال، يمكننا استخدام المبرهنة `minusPlus` لإصلاح هذا.

نظراً لأن إعطاء مثل هذا الإثبات في كل مرة أمر مملٌ إلى حد ما، يمكننا استخدام ملحقات فاحص الأنواع (type-checker plugins) للسماح للمترجم بمحاولة إثبات القيود تلقائياً. على وجه الخصوص، طور المؤلف ملحق ghc-typelits-presburger [13] لحل القضايا في حساب بريسبرجر في وقت الترجمة.

توفر مكتبتنا أيضاً نوع `LabPoly`، الذي يحول أنواع كثيرات الحدود الموجودة إلى أنواع "مُعنونة". باستخدام معلومات مستوى الأنواع، يمكن للمرء استدعاء خرائط الإدراج الكانونية بشكل طبيعي.

#### 2.4 تحسين دوال التحويل باستخدام قواعد إعادة الكتابة

نظراً لأن دوال التحويل يتم تنفيذها بشكل عام، فإنها تقدم أحياناً نفقات عامة غير ضرورية. على سبيل المثال، إذا استخدم أحد `injVars` مع نفس أنواع المصدر والهدف، فيجب أن تكون مجرد دالة الهوية. لحسن الحظ، يمكننا استخدام وظيفة قواعد إعادة الكتابة الآمنة للأنواع في GHC لتحقيق ذلك.

تعمل كل قاعدة إعادة كتابة في وقت الترجمة، إذا كان هناك مصطلح يطابق الجانب الأيسر من القاعدة وله نفس النوع مثل الجانب الأيمن.

في Haskell، يكفي فقط النظر في القوانين الجبرية لكتابة قواعد إعادة الكتابة المخصصة. هذا بسبب نقاء Haskell. أي أن كل تعبير في Haskell نقي، بمعنى أنها تُقيّم إلى نفس النتيجة عندما تُعطى نفس الوسائط. لاحظ أن هذا لا يعني أن Haskell لا يمكنها معاملة القيم ذات التأثيرات الجانبية؛ في الواقع، يميز نظام الأنواع في Haskell القيم النقية وغير النقية على مستوى الأنواع، ويمكن للمرء معاملة العمليات غير النقية دون انتهاك النقاء ككل. الحيلة وراء هذا الوضع هي وصف التأثيرات الجانبية كنوع من التعليمات المجردة، بدلاً من معاملة القيم غير النقية مباشرة. وبالتالي، على سبيل المثال، فإن تكرار نفس المصطلح لا يُحدث أي فرق في معناه، بشرط أن يكون صحيحاً جبرياً. تُستخدم قاعدة إعادة الكتابة هذه على نطاق واسع في Haskell. على سبيل المثال، يستخدمها Stream Fusion [3] للقضاء على التعبيرات الوسيطة غير الضرورية ودمج الدوال المعقدة في بنيات فعالة ذات مسار واحد. ومع ذلك، لم يقم DoCon بأي تحسين باستخدام قواعد إعادة الكتابة.

في مكتبتنا، نستخدم أيضاً قواعد إعادة الكتابة لإزالة التطبيقات المُتماثلة مثل "تصنيف" ترتيب أحادي الحد مرتين.

#### 2.5 ملاحظات حول قابلية التطبيق في اللغات الإلزامية

لا يمكن تحقيق الأمان الذي حققناه في هذا القسم في وقت الترجمة بدون الأنواع التابعة والدوال على مستوى الأنواع. تفتقر الأعمال الموجودة التي تستخدم أصناف الأنواع أو وراثة الأصناف لترميز التسلسل الهرمي الجبري، مثل JAS أو DoCon، إلى هذا المستوى من الأمان. من الناحية النظرية، يمكن للمرء تحقيق نفس مستوى الأمان حتى في لغة إلزامية ذات أنواع ثابتة، إذا كانت تدعم نوعاً من الأنواع التابعة. على سبيل المثال، في C++، يمكن استخدام القوالب (templates) مع الوسائط غير الأنواع لمحاكاة الأنواع التابعة. من ناحية أخرى، في Java، لا تسمح الأنواع العامة (Generics) بوسائط غير الأنواع ونحتاج إلى محاكاة أرقام بيانو بالأصناف. في كلتا الحالتين، يتطلب الأمر جهداً كبيراً لإثبات خصائص الأعداد الطبيعية داخلها، لأنها تفتقر إلى الدعم المخصص للأعداد الطبيعية على مستوى الأنواع أو ملحقات فاحص الأنواع.

من ناحية أخرى، للاستفادة من قواعد إعادة الكتابة، نحتاج إلى النقاء كما نوقش أعلاه.

---

### Translation Notes

- **Figures referenced:** Code 1, Code 2, Code 3, Code 4
- **Key terms introduced:** type-class (صنف الأنواع), ad-hoc polymorphism (تعدد الأشكال المخصص), dependent types (الأنواع التابعة), type-level functions (الدوال على مستوى الأنواع), associated types (الأنواع المرتبطة), rewriting rules (قواعد إعادة الكتابة), purity (النقاء), singleton (المفرد)
- **Equations:** Several type signatures preserved in code
- **Citations:** [3, 13, 14, 15, 17, 18, 23, 27]
- **Special handling:**
  - All code examples preserved in English (industry standard)
  - Mathematical notation preserved: R[X₁, . . . , Xₙ]
  - Type system terminology translated consistently
  - Complex technical concepts explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
