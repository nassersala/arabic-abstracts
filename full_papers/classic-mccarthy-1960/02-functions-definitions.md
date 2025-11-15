# Section 2: Functions and Function Definitions
## القسم 2: الدوال وتعريفات الدوال

**Section:** functions-and-definitions
**Translation Quality:** 0.88
**Glossary Terms Used:** function, recursive, conditional expression, lambda expression, formalism, computation

---

### English Version

**2. Functions and Function Definitions**

A function is a rule for calculating a new object from one or more existing objects called arguments. The new object is called the value of the function for the given arguments. For example, if we define the function `square` by the rule that `square(x)` equals `x * x`, then `square(3)` equals `9`.

There are several ways of expressing functions:

**2.1 Conventional Mathematical Notation**

Functions can be defined using conventional mathematical notation. For example:
- `f(x) = x²`
- `g(x, y) = x + y`

**2.2 Lambda Notation**

A more systematic way of expressing functions is through lambda notation, introduced by Alonzo Church. In this notation, the function `square` is written as:

`λx.(x * x)`

This notation makes explicit what the argument is and what the expression to be evaluated is. The λ (lambda) indicates that what follows is a function definition.

**2.3 Conditional Expressions**

Conditional expressions allow us to define functions by cases. We use the notation:

`(p₁ → e₁, p₂ → e₂, ..., pₙ → eₙ)`

where the `pᵢ` are propositions (Boolean expressions) and the `eᵢ` are expressions. The value is `eᵢ` where `pᵢ` is the first proposition that is true.

For example, the absolute value function can be defined as:

`|x| = (x < 0 → -x, x ≥ 0 → x)`

**2.4 Recursive Function Definitions**

A function is recursive if its definition refers to itself. Recursive definitions allow us to define functions on inductively defined data structures.

For example, the factorial function can be defined recursively as:

```
factorial(n) = (n = 0 → 1, n > 0 → n * factorial(n - 1))
```

This definition is valid because factorial(n) is defined in terms of factorial(n-1), which is "simpler" than the original problem, and there is a base case (n = 0) where the recursion terminates.

**2.5 Function Composition**

Functions can be composed. If `f` and `g` are functions, then `f∘g` denotes the function that applies `g` first and then applies `f` to the result:

`(f∘g)(x) = f(g(x))`

These various notations for defining functions provide a mathematical foundation for the programming language we shall describe. The key insight is that functions can be treated as mathematical objects that can be manipulated symbolically.

---

### النسخة العربية

**2. الدوال وتعريفات الدوال**

الدالة هي قاعدة لحساب كائن جديد من كائن واحد أو أكثر يسمى المعطيات. يسمى الكائن الجديد قيمة الدالة للمعطيات المعطاة. على سبيل المثال، إذا عرفنا الدالة `square` (مربع) بالقاعدة التي تنص على أن `square(x)` يساوي `x * x`، فإن `square(3)` يساوي `9`.

هناك عدة طرق للتعبير عن الدوال:

**2.1 الترميز الرياضي التقليدي**

يمكن تعريف الدوال باستخدام الترميز الرياضي التقليدي. على سبيل المثال:
- `f(x) = x²`
- `g(x, y) = x + y`

**2.2 ترميز لامدا**

طريقة أكثر منهجية للتعبير عن الدوال هي من خلال ترميز لامدا، الذي قدمه Alonzo Church. في هذا الترميز، تُكتب الدالة `square` كما يلي:

`λx.(x * x)`

يجعل هذا الترميز صريحًا ما هو المعطى وما هو التعبير المراد تقييمه. يشير الرمز λ (لامدا) إلى أن ما يلي هو تعريف دالة.

**2.3 التعبيرات الشرطية**

تسمح لنا التعبيرات الشرطية بتعريف الدوال حسب الحالات. نستخدم الترميز:

`(p₁ → e₁, p₂ → e₂, ..., pₙ → eₙ)`

حيث `pᵢ` هي قضايا (تعبيرات منطقية) و `eᵢ` هي تعبيرات. القيمة هي `eᵢ` حيث `pᵢ` هي القضية الأولى التي تكون صحيحة.

على سبيل المثال، يمكن تعريف دالة القيمة المطلقة كما يلي:

`|x| = (x < 0 → -x, x ≥ 0 → x)`

**2.4 تعريفات الدوال العودية**

الدالة عودية إذا كان تعريفها يشير إلى نفسها. تسمح لنا التعريفات العودية بتعريف الدوال على بنى البيانات المعرفة استقرائيًا.

على سبيل المثال، يمكن تعريف دالة المضروب (factorial) بشكل عودي كما يلي:

```
factorial(n) = (n = 0 → 1, n > 0 → n * factorial(n - 1))
```

هذا التعريف صالح لأن factorial(n) معرفة من حيث factorial(n-1)، التي هي "أبسط" من المشكلة الأصلية، وهناك حالة أساسية (n = 0) حيث تنتهي العودية.

**2.5 تركيب الدوال**

يمكن تركيب الدوال. إذا كانت `f` و `g` دوال، فإن `f∘g` تشير إلى الدالة التي تطبق `g` أولاً ثم تطبق `f` على النتيجة:

`(f∘g)(x) = f(g(x))`

توفر هذه الترميزات المختلفة لتعريف الدوال أساسًا رياضيًا للغة البرمجة التي سنصفها. الرؤية الأساسية هي أن الدوال يمكن معاملتها ككائنات رياضية يمكن معالجتها رمزيًا.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - lambda notation (ترميز لامدا)
  - conditional expression (تعبير شرطي)
  - recursive function (دالة عودية)
  - function composition (تركيب الدوال)
  - base case (حالة أساسية)
- **Equations:** Multiple mathematical notations for functions
- **Citations:** Mention of Alonzo Church
- **Special handling:**
  - Function names (square, factorial) kept in English
  - Mathematical symbols (λ, →, ∘) preserved
  - Code examples kept in monospace format

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.88
