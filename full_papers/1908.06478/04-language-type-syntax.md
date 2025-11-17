# Section 4: Language & Type Syntax
## القسم 4: صياغة اللغة والأنواع

**Section:** language-type-syntax
**Translation Quality:** 0.86
**Glossary Terms Used:** type system, syntax, polymorphism, algebraic types, type variables, function types

---

### English Version

In the next section, we will discuss how we had to adapt the existing JVFH type rules for GHC Core. For this purpose, we will be using a streamlined representation of the Core syntax as depicted in Figure 2. This representation is slightly different from the one actually used within the compiler [1]. For example, we distinguish more clearly between variables and constructors, both of which are represented as Var within the GHC compiler. On the other hand, we also omit several expressions which are currently unsupported in our analysis, namely Cast, Coercion and Tick.

**Figure 2:** Simplified representation of the GHC Core syntax

```
e ::= x | c | l | τ | λx. e | Λτ. e | e₁ e₂
    | let x = e₁ in e₂ | letrec x₁ = e₁ ; ...; xₙ = eₙ in e
    | case x = e₀ of {default → eₐ | c₁(x₁) → e₁ | ··· | cₙ(xₙ) → eₙ}
    | case x = e₀ of {default → eₐ | l₁ → e₁ | ··· | lₙ → eₙ}
```

For our types, we are reusing the type syntax from the original JVFH system without modifications. This syntax, as depicted in Figure 3, covers type variables, functions, thunks and algebraic types. Most of these contain annotations that signify the resource usage of the respective expression. Depending on the cost model used, this can refer to memory usage or runtime duration, for example.

**Figure 3:** Type syntax, as originally defined in [9]

```
A ::= X | A →^p B | T^q(A) | µX. {c₁ : (q₁, A₁) | ··· | cₙ : (qₙ, Aₙ)}
```

The type A →^p B represents a function, that takes an argument of type A, and returns a result of type B. The type annotation p signifies the cost of executing this function, i.e., evaluating the function result to weak head normal form.

The algebraic type µX. {c₁ : (q₁, A₁) | ··· | cₙ : (qₙ, Aₙ)} is a possibly recursive type consisting of several constructors cᵢ. For each constructor, we specify a potential qᵢ, which are resources "reserved" during structure allocation for future use. During a pattern match, this potential can be redeemed to pay for any upcoming calculations. Additionally, each constructor is also associated with a list of constructor fields Aᵢ. The type variable X can be used within these constructor fields as a recursive reference to the algebraic type. As an example, consider the following representation of a list type:

```
µX. {Nil : (1, []) | Cons : (2, [T³(Int), T⁴(X)])}
```

This example type consists of two constructors: The first, Nil, has potential 1 and no fields; and the second, Cons, has potential 2 and two fields, namely a list element of type Int, and a reference to the next list node, represented recursively with a type variable X. Note that type variables in our system may only be used as recursive references, and therefore must always be contained within algebraic types that bind them.

Finally, the thunk type T^q(A) is a wrapper that represents lazy evaluation; It signifies that an expression of this type possibly has not been evaluated to weak head normal form yet, and doing so will use up q resources. Thunk types can only (and will always) appear in specific places: Namely, as the argument of any function type, as the constructor fields of any algebraic type, and as the type of every variable in the context of any typing judgment.

We apply some workarounds for Haskell/Core types that do not have any direct equivalent in this syntax: Primitive types such as "Int#" or "Float#" are represented as an empty algebraic type "µX.{}" in our system; and type abstractions "forall x. T" are replaced with an "artificial" function "µX.{} →^0 T". However, note that polymorphism is currently unsupported in our implementation; Therefore, this artificial function does not actually have any meaningful effect within the type system, and only serves as an informatory annotation for the user. Also note that this representation breaks the requirement that all function arguments are wrapped in thunk types; This can be used to easily distinguish "real" functions from an artificial function representing type abstraction.

Applying these workarounds instead of extending the type syntax may seem restricting, but it offers one major advantage: The JVFH type system defines several relations between different types, which we can reuse without any modifications. This would not be possible if we modified the type syntax or its semantics.

---

### النسخة العربية

في القسم التالي، سنناقش كيف اضطررنا إلى تكييف قواعد أنواع JVFH الموجودة لـ GHC Core. لهذا الغرض، سنستخدم تمثيلاً مُبسّطاً لصياغة Core كما هو موضح في الشكل 2. هذا التمثيل يختلف قليلاً عن التمثيل المستخدم فعلياً داخل المترجم [1]. على سبيل المثال، نميز بشكل أوضح بين المتغيرات والمنشئات، وكلاهما يُمثّل كـ Var داخل مترجم GHC. من ناحية أخرى، نحذف أيضاً عدة تعبيرات غير مدعومة حالياً في تحليلنا، وهي Cast و Coercion و Tick.

**الشكل 2:** تمثيل مُبسّط لصياغة GHC Core

```
e ::= x | c | l | τ | λx. e | Λτ. e | e₁ e₂
    | let x = e₁ in e₂ | letrec x₁ = e₁ ; ...; xₙ = eₙ in e
    | case x = e₀ of {default → eₐ | c₁(x₁) → e₁ | ··· | cₙ(xₙ) → eₙ}
    | case x = e₀ of {default → eₐ | l₁ → e₁ | ··· | lₙ → eₙ}
```

بالنسبة لأنواعنا، نعيد استخدام صياغة الأنواع من نظام JVFH الأصلي دون تعديلات. تغطي هذه الصياغة، كما هو موضح في الشكل 3، متغيرات الأنواع والدوال والثانكات والأنواع الجبرية. يحتوي معظمها على تعليمات تشير إلى استخدام الموارد للتعبير المعني. اعتماداً على نموذج التكلفة المستخدم، يمكن أن يشير ذلك إلى استخدام الذاكرة أو مدة وقت التشغيل، على سبيل المثال.

**الشكل 3:** صياغة الأنواع، كما تم تعريفها أصلاً في [9]

```
A ::= X | A →^p B | T^q(A) | µX. {c₁ : (q₁, A₁) | ··· | cₙ : (qₙ, Aₙ)}
```

يمثل النوع A →^p B دالة تأخذ معاملاً من النوع A، وتُرجع نتيجة من النوع B. يشير تعليم النوع p إلى تكلفة تنفيذ هذه الدالة، أي تقييم نتيجة الدالة إلى الشكل الطبيعي الضعيف للرأس.

النوع الجبري µX. {c₁ : (q₁, A₁) | ··· | cₙ : (qₙ, Aₙ)} هو نوع تكراري محتمل يتكون من عدة منشئات cᵢ. لكل منشئ، نحدد إمكانية qᵢ، وهي موارد "محجوزة" أثناء تخصيص البنية للاستخدام المستقبلي. أثناء مطابقة النمط، يمكن استرداد هذه الإمكانية لدفع ثمن أي حسابات قادمة. بالإضافة إلى ذلك، يرتبط كل منشئ أيضاً بقائمة من حقول المنشئ Aᵢ. يمكن استخدام متغير النوع X داخل حقول المنشئ هذه كمرجع تكراري للنوع الجبري. كمثال، لننظر إلى التمثيل التالي لنوع قائمة:

```
µX. {Nil : (1, []) | Cons : (2, [T³(Int), T⁴(X)])}
```

يتكون هذا النوع المثالي من منشئين: الأول، Nil، له إمكانية 1 وليس له حقول؛ والثاني، Cons، له إمكانية 2 وحقلان، وهما عنصر قائمة من النوع Int، ومرجع إلى عقدة القائمة التالية، ممثلة تكرارياً بمتغير النوع X. لاحظ أن متغيرات الأنواع في نظامنا قد تُستخدم فقط كمراجع تكرارية، وبالتالي يجب أن تكون دائماً موجودة داخل الأنواع الجبرية التي تربطها.

أخيراً، نوع الثانك T^q(A) هو غلاف يمثل التقييم الكسول؛ يشير إلى أن تعبيراً من هذا النوع ربما لم يتم تقييمه بعد إلى الشكل الطبيعي الضعيف للرأس، وأن القيام بذلك سيستهلك q من الموارد. يمكن لأنواع الثانك أن تظهر فقط (وستظهر دائماً) في أماكن محددة: وهي، كمعامل لأي نوع دالة، كحقول منشئ لأي نوع جبري، وكنوع لكل متغير في سياق أي حكم تنميط.

نطبق بعض الحلول البديلة لأنواع Haskell/Core التي ليس لها ما يعادلها المباشر في هذه الصياغة: يتم تمثيل الأنواع البدائية مثل "Int#" أو "Float#" كنوع جبري فارغ "µX.{}" في نظامنا؛ ويتم استبدال تجريدات الأنواع "forall x. T" بدالة "صناعية" "µX.{} →^0 T". ومع ذلك، لاحظ أن تعدد الأشكال غير مدعوم حالياً في تطبيقنا؛ لذلك، لا يكون لهذه الدالة الصناعية أي تأثير فعلي ذي معنى داخل نظام الأنواع، وتعمل فقط كتعليم إعلامي للمستخدم. لاحظ أيضاً أن هذا التمثيل يكسر المتطلب بأن جميع معاملات الدوال مغلفة في أنواع الثانك؛ يمكن استخدام ذلك للتمييز بسهولة بين الدوال "الحقيقية" والدالة الصناعية التي تمثل تجريد الأنواع.

قد يبدو تطبيق هذه الحلول البديلة بدلاً من توسيع صياغة الأنواع مقيداً، لكنه يقدم ميزة رئيسية واحدة: يحدد نظام أنواع JVFH عدة علاقات بين الأنواع المختلفة، والتي يمكننا إعادة استخدامها دون أي تعديلات. لن يكون ذلك ممكناً إذا قمنا بتعديل صياغة الأنواع أو دلالاتها.

---

### Translation Notes

- **Figures referenced:** Figure 2 (GHC Core syntax), Figure 3 (Type syntax)
- **Key terms introduced:**
  - streamlined representation (تمثيل مُبسّط)
  - weak head normal form (الشكل الطبيعي الضعيف للرأس)
  - recursive type (نوع تكراري)
  - potential (إمكانية)
  - pattern match (مطابقة النمط)
  - constructor fields (حقول المنشئ)
  - recursive reference (مرجع تكراري)
  - typing judgment (حكم تنميط)
  - primitive types (أنواع بدائية)
  - type abstraction (تجريد الأنواع)
  - artificial function (دالة صناعية)
  - semantics (دلالات)
- **Equations:** Multiple formal syntax definitions
- **Citations:** [1, 9]
- **Special handling:**
  - Formal mathematical syntax preserved in original form
  - Greek letters (λ, Λ, τ, µ) kept as is
  - Subscripts and superscripts preserved
  - "thunk" kept in transliteration (ثانك)
  - "weak head normal form" is a standard technical term translated literally

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation (First & Last Paragraphs)

**First paragraph:** In the next section, we will discuss how we had to adapt the existing JVFH type rules for GHC Core. For this purpose, we will use a simplified representation of the Core syntax as shown in Figure 2. This representation differs slightly from the representation actually used within the compiler [1]. For example, we distinguish more clearly between variables and constructors, both of which are represented as Var within the GHC compiler. On the other hand, we also omit several expressions that are currently unsupported in our analysis, namely Cast, Coercion, and Tick.

**Last paragraph:** Applying these workarounds instead of extending the type syntax may seem restrictive, but it offers one major advantage: The JVFH type system defines several relations between different types, which we can reuse without any modifications. This would not be possible if we modified the type syntax or its semantics.
