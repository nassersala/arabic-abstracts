# Section 7: Conditional Expressions and Functions
## القسم 7: التعبيرات الشرطية والدوال

**Section:** conditional-expressions
**Translation Quality:** 0.87
**Glossary Terms Used:** conditional, expression, predicate, boolean, control flow, evaluation

---

### English Version

Conditional expressions are a fundamental innovation of LISP that McCarthy adapted from mathematical logic. Unlike traditional programming languages that use conditional statements (if-then-else), LISP treats conditionals as **expressions** that return values.

**Syntax of Conditional Expressions:**

A conditional expression has the form:

$$[p_1 \to e_1; p_2 \to e_2; \ldots; p_n \to e_n]$$

where:
- $p_1, p_2, \ldots, p_n$ are **predicates** (boolean expressions)
- $e_1, e_2, \ldots, e_n$ are **consequent expressions**
- The arrow `→` separates conditions from their consequents
- Semicolons `;` separate the different cases

**Evaluation Semantics:**

The conditional expression is evaluated by:
1. Evaluating $p_1$
2. If $p_1$ is true, evaluate and return $e_1$
3. Otherwise, try $p_2$, and if true, evaluate and return $e_2$
4. Continue until a true predicate is found
5. If no predicate is true, the result is undefined

**Example - Factorial Function:**

```lisp
factorial[n] = [eq[n; 0] → 1;
                T → n × factorial[n - 1]]
```

This reads as:
- If $n = 0$, return 1
- Otherwise (T is always true), return $n \times \text{factorial}(n-1)$

**Example - Absolute Value:**

```lisp
abs[x] = [x < 0 → -x;
          T → x]
```

**Advantages Over Conditional Statements:**

1. **Expression vs. Statement:** Conditionals return values and can be nested anywhere expressions are allowed

2. **Functional purity:** No need for assignment statements or mutable variables

3. **Mathematical clarity:** Resembles mathematical case analysis:
   $$f(x) = \begin{cases} e_1 & \text{if } p_1 \\ e_2 & \text{if } p_2 \\ \ldots \end{cases}$$

4. **Composability:** Conditional expressions can be freely composed with other expressions

**Multi-way Conditionals:**

Unlike binary if-then-else, LISP conditionals can have arbitrarily many branches:

```lisp
sign[x] = [x < 0 → NEGATIVE;
           eq[x; 0] → ZERO;
           x > 0 → POSITIVE]
```

**The Special Predicate T:**

The atomic symbol `T` (for "true") is a special predicate that always evaluates to true. It is conventionally used as the final condition to provide a default case:

```lisp
classify[x] = [eq[x; A] → CASE-A;
               eq[x; B] → CASE-B;
               eq[x; C] → CASE-C;
               T → OTHER]
```

**Nested Conditionals:**

Conditional expressions can be nested to express complex logic:

```lisp
max[x; y; z] = [x > y → [x > z → x; T → z];
                T → [y > z → y; T → z]]
```

**Short-Circuit Evaluation:**

LISP conditionals use **short-circuit evaluation**: once a true predicate is found, subsequent predicates are not evaluated. This allows for:

1. **Efficiency:** Avoid unnecessary computation
2. **Safety:** Later predicates can assume earlier ones were false

Example:

```lisp
safe-divide[x; y] = [eq[y; 0] → ERROR;
                     T → x / y]
```

The division `x / y` is only evaluated if `y ≠ 0`.

**Conditional Expressions in Function Definitions:**

Most LISP functions are defined using conditional expressions. The pattern is:

```lisp
function[args] = [base-case → base-value;
                  T → recursive-case]
```

This pattern appears throughout functional programming and is central to recursive function definition.

**Relationship to Lambda Calculus:**

McCarthy noted that conditional expressions provide a clean way to define functions by cases, which complements the lambda calculus. While lambda provides function abstraction, conditionals provide case analysis - together they form a complete basis for computation.

**Implementation:**

In the LISP evaluator, conditionals are handled by the `evcon` function:

```lisp
evcon[c; a] = [eval[caar[c]; a] → eval[cadar[c]; a];
               T → evcon[cdr[c]; a]]
```

This recursively checks each condition until one evaluates to true, then evaluates its consequent.

---

### النسخة العربية

التعبيرات الشرطية هي ابتكار أساسي في LISP قام مكارثي بتكييفه من المنطق الرياضي. على عكس لغات البرمجة التقليدية التي تستخدم جمل شرطية (if-then-else)، تتعامل LISP مع الشروط كـ **تعبيرات** (expressions) تُرجع قيماً.

**صيغة التعبيرات الشرطية:**

التعبير الشرطي له الشكل:

$$[p_1 \to e_1; p_2 \to e_2; \ldots; p_n \to e_n]$$

حيث:
- $p_1, p_2, \ldots, p_n$ هي **عبارات شرطية** (predicates) (تعبيرات منطقية)
- $e_1, e_2, \ldots, e_n$ هي **تعبيرات النتيجة** (consequent expressions)
- السهم `→` يفصل الشروط عن نتائجها
- الفواصل المنقوطة `;` تفصل الحالات المختلفة

**دلاليات التقييم:**

يتم تقييم التعبير الشرطي عن طريق:
1. تقييم $p_1$
2. إذا كان $p_1$ صحيحاً، قيّم وأرجع $e_1$
3. خلاف ذلك، جرّب $p_2$، وإذا كان صحيحاً، قيّم وأرجع $e_2$
4. استمر حتى يُعثر على عبارة شرطية صحيحة
5. إذا لم تكن أي عبارة شرطية صحيحة، تكون النتيجة غير معرّفة

**مثال - دالة المضروب:**

```lisp
factorial[n] = [eq[n; 0] → 1;
                T → n × factorial[n - 1]]
```

يُقرأ هذا كما يلي:
- إذا كان $n = 0$، أرجع 1
- خلاف ذلك (T صحيح دائماً)، أرجع $n \times \text{factorial}(n-1)$

**مثال - القيمة المطلقة:**

```lisp
abs[x] = [x < 0 → -x;
          T → x]
```

**مزايا على الجمل الشرطية:**

1. **تعبير مقابل جملة:** الشروط تُرجع قيماً ويمكن تداخلها في أي مكان يُسمح فيه بالتعبيرات

2. **النقاء الوظيفي:** لا حاجة لجمل الإسناد أو المتغيرات القابلة للتغيير

3. **الوضوح الرياضي:** يشبه تحليل الحالات الرياضية:
   $$f(x) = \begin{cases} e_1 & \text{إذا } p_1 \\ e_2 & \text{إذا } p_2 \\ \ldots \end{cases}$$

4. **قابلية التركيب:** يمكن تركيب التعبيرات الشرطية بحرية مع تعبيرات أخرى

**الشروط متعددة الاتجاهات:**

على عكس if-then-else الثنائي، يمكن أن تحتوي شروط LISP على عدد عشوائي من الفروع:

```lisp
sign[x] = [x < 0 → NEGATIVE;
           eq[x; 0] → ZERO;
           x > 0 → POSITIVE]
```

**العبارة الشرطية الخاصة T:**

الرمز الذري `T` (للدلالة على "صحيح") هو عبارة شرطية خاصة تُقيّم دائماً إلى صحيح. يُستخدم تقليدياً كشرط نهائي لتوفير حالة افتراضية:

```lisp
classify[x] = [eq[x; A] → CASE-A;
               eq[x; B] → CASE-B;
               eq[x; C] → CASE-C;
               T → OTHER]
```

**الشروط المتداخلة:**

يمكن تداخل التعبيرات الشرطية للتعبير عن منطق معقد:

```lisp
max[x; y; z] = [x > y → [x > z → x; T → z];
                T → [y > z → y; T → z]]
```

**التقييم القصير الدائرة:**

تستخدم شروط LISP **التقييم القصير الدائرة** (short-circuit evaluation): بمجرد العثور على عبارة شرطية صحيحة، لا يتم تقييم العبارات الشرطية اللاحقة. يتيح هذا:

1. **الكفاءة:** تجنب الحساب غير الضروري
2. **الأمان:** يمكن للعبارات الشرطية اللاحقة افتراض أن السابقة كانت خاطئة

مثال:

```lisp
safe-divide[x; y] = [eq[y; 0] → ERROR;
                     T → x / y]
```

القسمة `x / y` يتم تقييمها فقط إذا كان `y ≠ 0`.

**التعبيرات الشرطية في تعريفات الدوال:**

معظم دوال LISP معرّفة باستخدام التعبيرات الشرطية. النمط هو:

```lisp
function[args] = [base-case → base-value;
                  T → recursive-case]
```

يظهر هذا النمط في جميع أنحاء البرمجة الوظيفية وهو محوري لتعريف الدوال العودية.

**العلاقة بحساب لامبدا:**

أشار مكارثي إلى أن التعبيرات الشرطية توفر طريقة نظيفة لتعريف الدوال بحسب الحالات، مما يكمل حساب لامبدا. بينما توفر لامبدا تجريد الدوال، توفر الشروط تحليل الحالات - معاً يشكلان أساساً كاملاً للحساب.

**التطبيق:**

في مُقيِّم LISP، يتم التعامل مع الشروط بواسطة دالة `evcon`:

```lisp
evcon[c; a] = [eval[caar[c]; a] → eval[cadar[c]; a];
               T → evcon[cdr[c]; a]]
```

تتحقق هذه بشكل عودي من كل شرط حتى يُقيّم أحدها إلى صحيح، ثم تقيّم نتيجته.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** conditional expression, predicate, consequent, short-circuit evaluation, multi-way conditional, case analysis
- **Equations:** Mathematical case notation for functions
- **Citations:** None
- **Special handling:**
  - Mathematical notation for conditionals preserved: $[p \to e]$
  - "T" kept in English (standard LISP symbol for true)
  - Code examples in LISP notation
  - "short-circuit evaluation" translated as "التقييم القصير الدائرة"
  - Function definition patterns shown in both languages
  - Comparison with traditional if-then-else explained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
