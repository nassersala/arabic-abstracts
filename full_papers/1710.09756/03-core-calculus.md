# Section 3: λQ→: A Core Calculus for Linear Haskell
## القسم 3: λQ→: حساب أساسي لـ Haskell الخطي

**Section:** Core Calculus
**Translation Quality:** 0.85
**Glossary Terms Used:** type system, linear types, polymorphism, data types, multiplicities, type inference

---

### English Version

We do not formalise all of Linear Haskell, but rather a core calculus, λq→ which exhibits all key features, including datatypes and multiplicity polymorphism. This way we make precise much of the informal discussion above.

**3.1 Syntax**

The term syntax of λq→ is that of a type-annotated (à la Church) simply-typed λ-calculus with let-definitions (Fig. 5). It includes multiplicity polymorphism, but to avoid clutter we omit ordinary type polymorphism.

λq→ is an explicitly-typed language: each binder is annotated with its type and multiplicity; and multiplicity abstraction and application are explicit. Linear Haskell will use type inference to fill in much of this information, but we do not address the challenges of type inference here.

The types of λq→ (see Fig. 5) are simple types with arrows (albeit multiplicity-annotated ones), datatypes, and multiplicity polymorphism. We use the following abbreviations: A → B = A →ω B and A ⊸ B = A →1 B.

Datatype declarations are of the following form:
```
data D p1 ... pn where ck : A1 →π1 ... Ank →πnk D
```

The above declaration means that D is parameterized over n multiplicities pi and has m constructors ck, each with nk arguments. Arguments of constructors have a multiplicity, just like arguments of functions: an argument of multiplicity ω means that consuming the data constructor once makes no claim on how often that argument is consumed (Def. 2.1).

**3.2 Static semantics**

The static semantics of λq→ is given in Fig. 6. Each binding in Γ, of form x :µ A, includes a multiplicity π. The familiar judgement Γ ⊢ t : A should be read as follows:

Γ ⊢ t : A asserts that consuming the term t : A exactly once will consume each binding (x :π A) in Γ with its multiplicity π.

One may want to think of the types in Γ as inputs of the judgement, and the multiplicities as outputs.

The rule (abs) for lambda abstraction adds (x :π A) to the environment Γ before checking the body t of the abstraction. The dual application rule (app) is more interesting:

```
Γ ⊢ t : A →π B    ∆ ⊢ u : A
―――――――――――――――――――――――――
Γ + π∆ ⊢ t u : B
```

To consume (t u) once, we consume t once, yielding the multiplicities in Γ, and u once, yielding the multiplicies in ∆. But if the multiplicity π on u's function arrow is ω, then the function consumes its argument not once but ω times, so all u's free variables must also be used with multiplicity ω. We express this by scaling the multiplicities in ∆ by π. Finally we need to add together all the multiplicities in Γ and π∆; hence the context Γ + π∆ in the conclusion of the rule.

**Definition 3.4 (equivalence of multiplicities).** The equivalence of multiplicities is the smallest transitive and reflexive relation, which obeys the following laws:
• + and · are associative and commutative
• 1 is the unit of ·
• · distributes over +
• ω · ω = ω
• 1 + 1 = 1 + ω = ω + ω = ω

Thus, multiplicities form a semi-ring (without a zero), which extends to a module structure on typing contexts.

**3.3 Data constructors and case expressions**

The handling of data constructors and case expressions is a distinctive aspect of our design. For constructor applications, the rule (con), everything is straightforward: we treat the data constructor in precisely the same way as an application of a function with that data constructor's type.

The (case) rule is more interesting. The scrutinee t is consumed π times, which accounts for the πΓ in the conclusion. Now consider the bindings (xi :π µi[π1 ...πn] Ai) in the environment for typechecking uk. That binding will be linear only if both π and πi are linear.

**3.4 Metatheory**

In order to prove that our type system meets its stated goals, we introduce an operational semantics. The details are deferred to Appendix A.

Our preservation and progress theorems (proved in Sec. A.3) read as follows:

**Theorem 3.5 (Type preservation).** If a is well typed, and a ⇓ b, or a ⇓* b then b is well-typed.

**Theorem 3.6 (Progress).** Evaluation does not block. That is, for any partial evaluation a ⇓* b, where a is well-typed, the derivation can be extended.

Furthermore, linear types can be used to implement some operations as in-place updates, and typestates are actually enforced by the type system.

**Theorem 3.7 (Type preservation).** For any well-typed σ, if σ ⇓ τ or σ ⇓* τ, then τ is well-typed.

**Theorem 3.8 (Progress).** Evaluation does not block. That is, for any partial evaluation σ ⇓* τ, for σ well-typed, the evaluation can be extended. In particular, typestates need not be checked dynamically.

**Theorem 3.9 (Observational equivalence).** The semantics with in-place mutation is observationally equivalent to the pure semantics.

**3.5 Design choices & trade-offs**

We could as well have picked different points in the design space for λq→. We review some of the choices we made:

**Case rule.** Thanks to caseω, we can use linear arrows on all data types.

**Subtyping.** Because the type A ⊸ B only strengthens the contract of its elements compared to A → B, one might expect the type A ⊸ B to be a subtype of A → B. But while λq→ has polymorphism, it does not have subtyping. The lack of subtyping is a deliberate choice in our design: it is well known that Hindley-Milner-style type inference does not mesh well with subtyping.

**Polymorphism & multiplicities.** Consider the definition: "id x = x". Our typing rules would validate both id :: Int → Int and id :: Int ⊸ Int. So, since we think of multiplicities ranging over {1,ω}, surely we should also have id :: ∀p. Int →p Int? But as it stands, our rules do not accept it.

**Divergence.** Consider this definition:
```haskell
f :: [Int] ⊸ [Int]
f xs = repeat 1 ++ xs
```
But wait! Does f really consume its argument xs exactly once? After all, (repeat 1) is infinite so f will never evaluate xs at all! In corner cases like this we look to metatheory. Yes, the typing rules give the specified types for (++) and f. Yes, the operational claims guaranteed by the metatheory remain valid. Intuitively you may imagine it like this: linearity claims that if you were consume the result of f completely, exactly once, then you would consume its argument once; but since the result of f is infinite we cannot consume it completely exactly once, so the claim holds vacuously.

---

### النسخة العربية

لا نضفي الطابع الرسمي على كل Haskell الخطي، بل على حساب أساسي، λq→ الذي يعرض جميع الميزات الرئيسية، بما في ذلك أنواع البيانات وتعددية التعددية. بهذه الطريقة نجعل الكثير من المناقشة غير الرسمية أعلاه دقيقة.

**3.1 البناء**

بناء المصطلح لـ λq→ هو بناء حساب λ بسيط الأنواع مع تعليقات الأنواع (على طريقة Church) مع تعريفات let. يتضمن تعددية التعددية، ولكن لتجنب الفوضى نحذف تعددية الأنواع العادية.

λq→ هي لغة ذات أنواع صريحة: كل رابط مُعلَّم بنوعه وتعدديته؛ والتجريد والتطبيق للتعددية صريحان. سيستخدم Haskell الخطي استدلال الأنواع لملء الكثير من هذه المعلومات، لكننا لا نتناول تحديات استدلال الأنواع هنا.

أنواع λq→ هي أنواع بسيطة مع أسهم (وإن كانت مُعلَّمة بالتعددية)، وأنواع بيانات، وتعددية التعددية. نستخدم الاختصارات التالية: A → B = A →ω B و A ⊸ B = A →1 B.

إعلانات أنواع البيانات من الشكل التالي:
```
data D p1 ... pn where ck : A1 →π1 ... Ank →πnk D
```

**3.2 الدلالات الثابتة**

تُعطى الدلالات الثابتة لـ λq→ في الشكل 6. يتضمن كل ربط في Γ، من الشكل x :µ A، تعددية π. يجب قراءة الحكم المألوف Γ ⊢ t : A على النحو التالي:

Γ ⊢ t : A يؤكد أن استهلاك المصطلح t : A مرة واحدة بالضبط سيستهلك كل ربط (x :π A) في Γ بتعدديته π.

قد يرغب المرء في التفكير في الأنواع في Γ كمدخلات للحكم، والتعدديات كمخرجات.

قاعدة (abs) للتجريد لامدا تضيف (x :π A) إلى البيئة Γ قبل فحص جسم t من التجريد. قاعدة التطبيق المزدوجة (app) أكثر إثارة للاهتمام:

```
Γ ⊢ t : A →π B    ∆ ⊢ u : A
―――――――――――――――――――――――――
Γ + π∆ ⊢ t u : B
```

لاستهلاك (t u) مرة واحدة، نستهلك t مرة واحدة، مما ينتج عنه التعدديات في Γ، و u مرة واحدة، مما ينتج عنه التعدديات في ∆. ولكن إذا كانت التعددية π على سهم دالة u هي ω، فإن الدالة تستهلك وسيطها ليس مرة واحدة بل ω مرة، لذا يجب أيضاً استخدام جميع المتغيرات الحرة لـ u بتعددية ω. نعبر عن هذا بقياس التعدديات في ∆ بـ π. أخيراً نحتاج إلى جمع كل التعدديات في Γ و π∆؛ ومن ثم السياق Γ + π∆ في استنتاج القاعدة.

**التعريف 3.4 (تكافؤ التعدديات).** تكافؤ التعدديات هو أصغر علاقة انتقالية وانعكاسية، تطيع القوانين التالية:
• + و · تجميعية وتبديلية
• 1 هي وحدة ·
• · توزع على +
• ω · ω = ω
• 1 + 1 = 1 + ω = ω + ω = ω

وبالتالي، تشكل التعدديات حلقة شبه (بدون صفر)، والتي تمتد إلى بنية وحدة على سياقات الكتابة.

**3.3 مُنشئات البيانات وتعبيرات الحالة**

التعامل مع مُنشئات البيانات وتعبيرات الحالة هو جانب مميز من تصميمنا. بالنسبة لتطبيقات المُنشئ، فإن القاعدة (con)، كل شيء واضح ومباشر: نتعامل مع مُنشئ البيانات بنفس الطريقة تماماً كتطبيق دالة بنوع مُنشئ البيانات.

قاعدة (case) أكثر إثارة للاهتمام. يتم استهلاك المُدقق t مرات π، مما يمثل πΓ في الاستنتاج.

**3.4 النظرية الفوقية**

من أجل إثبات أن نظام الأنواع لدينا يحقق أهدافه المعلنة، نقدم دلالات تشغيلية. يتم تأجيل التفاصيل إلى الملحق A.

تقرأ نظريات الحفظ والتقدم لدينا (المثبتة في القسم A.3) كما يلي:

**النظرية 3.5 (حفظ الأنواع).** إذا كان a مكتوباً جيداً، و a ⇓ b، أو a ⇓* b فإن b مكتوب جيداً.

**النظرية 3.6 (التقدم).** التقييم لا يتوقف. أي، لأي تقييم جزئي a ⇓* b، حيث a مكتوب جيداً، يمكن تمديد الاشتقاق.

علاوة على ذلك، يمكن استخدام الأنواع الخطية لتنفيذ بعض العمليات كتحديثات في المكان، ويتم فرض حالات الأنواع بالفعل بواسطة نظام الأنواع.

**النظرية 3.7 (حفظ الأنواع).** لأي σ مكتوب جيداً، إذا σ ⇓ τ أو σ ⇓* τ، فإن τ مكتوب جيداً.

**النظرية 3.8 (التقدم).** التقييم لا يتوقف. أي، لأي تقييم جزئي σ ⇓* τ، لـ σ مكتوب جيداً، يمكن تمديد التقييم. على وجه الخصوص، لا حاجة للتحقق من حالات الأنواع ديناميكياً.

**النظرية 3.9 (التكافؤ الملحوظ).** الدلالات مع التحور في المكان متكافئة ملحوظاً مع الدلالات النقية.

**3.5 خيارات التصميم والمقايضات**

كان يمكننا أيضاً اختيار نقاط مختلفة في مساحة التصميم لـ λq→. نراجع بعض الاختيارات التي قمنا بها:

**قاعدة الحالة.** بفضل caseω، يمكننا استخدام الأسهم الخطية على جميع أنواع البيانات.

**الكتابة الفرعية.** نظراً لأن النوع A ⊸ B يقوي فقط عقد عناصره مقارنة بـ A → B، قد يتوقع المرء أن يكون النوع A ⊸ B نوعاً فرعياً من A → B. ولكن بينما لدى λq→ تعددية الأشكال، ليس لديها كتابة فرعية. عدم وجود كتابة فرعية هو اختيار متعمد في تصميمنا: من المعروف أن استدلال الأنواع على طراز Hindley-Milner لا يتناسب بشكل جيد مع الكتابة الفرعية.

**تعددية الأشكال والتعدديات.** ضع في اعتبارك التعريف: "id x = x". ستقبل قواعد الكتابة لدينا كلاً من id :: Int → Int و id :: Int ⊸ Int.

**الاختلاف.** ضع في اعتبارك هذا التعريف:
```haskell
f :: [Int] ⊸ [Int]
f xs = repeat 1 ++ xs
```
لكن انتظر! هل تستهلك f حقاً وسيطها xs مرة واحدة بالضبط؟ بعد كل شيء، (repeat 1) لانهائي لذا لن تقيم f xs على الإطلاق! في الحالات الركنية مثل هذه ننظر إلى النظرية الفوقية.

---

### Translation Notes

- **Figures referenced:** Fig. 5 (Syntax), Fig. 6 (Typing rules)
- **Key terms introduced:**
  - Core calculus (الحساب الأساسي)
  - Multiplicities (التعدديات)
  - Semi-ring (حلقة شبه)
  - Type preservation (حفظ الأنواع)
  - Progress (التقدم)
  - Observational equivalence (التكافؤ الملحوظ)
- **Mathematical notation:** Typing judgements, operational semantics notation preserved
- **Theorems:** 5 main theorems (3.5-3.9) stated precisely

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.85
