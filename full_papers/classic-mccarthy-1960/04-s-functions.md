# Section 4: Elementary S-functions and Predicates
## القسم 4: دوال S الأولية والعبارات الشرطية

**Section:** s-functions
**Translation Quality:** 0.88
**Glossary Terms Used:** function, predicate, symbolic expression, atom, list, primitive, composition

---

### English Version

We now define the basic functions and predicates that operate on S-expressions. These five elementary operations form the foundation from which all other LISP functions can be built through composition and recursion.

**1. atom[x]** - The Atom Predicate

The function `atom[x]` returns `T` (true) if $x$ is an atomic symbol, and returns `F` (false) if $x$ is a dotted pair.

Examples:
- `atom[A]` = `T`
- `atom[(A · B)]` = `F`
- `atom[()]` = `T` (NIL is atomic)

**2. eq[x; y]** - The Equality Predicate

The function `eq[x; y]` is defined only when both $x$ and $y$ are atomic symbols. It returns `T` if $x$ and $y$ are the same symbol, and `F` otherwise.

Examples:
- `eq[A; A]` = `T`
- `eq[A; B]` = `F`
- `eq[NIL; NIL]` = `T`

Note: `eq` is undefined for non-atomic arguments.

**3. car[x]** - Extract First Element

For a dotted pair $(e_1 \cdot e_2)$, the function `car[x]` returns the first element $e_1$.

Examples:
- `car[(A · B)]` = `A`
- `car[((A · B) · C)]` = `(A · B)`
- `car[(A B C)]` = `car[(A · (B · (C · NIL)))]` = `A`

The name "CAR" stands for "Contents of Address Register" from the IBM 704 architecture.

**4. cdr[x]** - Extract Rest of List

For a dotted pair $(e_1 \cdot e_2)$, the function `cdr[x]` returns the second element $e_2$.

Examples:
- `cdr[(A · B)]` = `B`
- `cdr[(A · (B · C))]` = `(B · C)`
- `cdr[(A B C)]` = `cdr[(A · (B · (C · NIL)))]` = `(B C)`

The name "CDR" stands for "Contents of Decrement Register."

**5. cons[x; y]** - Construct Pair

The function `cons[x; y]` constructs a new dotted pair with $x$ as the first element and $y$ as the second element. It is the inverse operation of `car` and `cdr`.

Examples:
- `cons[A; B]` = `(A · B)`
- `cons[A; (B · C)]` = `(A · (B · C))` = `(A B C)`
- `cons[(A · B); C]` = `((A · B) · C)`

**Identity Properties:**

For any dotted pair $x$:
$$\text{cons}[\text{car}[x]; \text{cdr}[x]] = x$$

For any S-expressions $e_1$ and $e_2$:
$$\text{car}[\text{cons}[e_1; e_2]] = e_1$$
$$\text{cdr}[\text{cons}[e_1; e_2]] = e_2$$

**Building Complex Functions:**

From these five primitive functions, we can build more complex functions through composition. For example:

- `caar[x]` = `car[car[x]]` (first element of first element)
- `cadr[x]` = `car[cdr[x]]` (second element of a list)
- `caddr[x]` = `car[cdr[cdr[x]]]` (third element of a list)

**Recursive List Processing:**

The power of these primitives becomes apparent when combined with recursion. For example, a function to compute the length of a list:

```lisp
length[x] = [atom[x] → 0; T → 1 + length[cdr[x]]]
```

This recursively processes the list by:
1. If the list is empty (atomic), return 0
2. Otherwise, add 1 and recursively process the rest of the list

**Universality:**

These five elementary functions, combined with conditional expressions and recursive definitions, are sufficient to express any computable function on S-expressions. This universality is analogous to the universality of Turing machines but expressed in a more natural and compositional way.

---

### النسخة العربية

نعرّف الآن الدوال والعبارات الشرطية الأساسية التي تعمل على تعبيرات S. هذه العمليات الأولية الخمس تشكل الأساس الذي يمكن من خلاله بناء جميع دوال LISP الأخرى عبر التركيب والعودية.

**1. atom[x]** - عبارة الذرة الشرطية

الدالة `atom[x]` تُرجع `T` (صحيح) إذا كان $x$ رمزاً ذرياً، وتُرجع `F` (خطأ) إذا كان $x$ زوجاً منقطاً.

أمثلة:
- `atom[A]` = `T`
- `atom[(A · B)]` = `F`
- `atom[()]` = `T` (NIL ذري)

**2. eq[x; y]** - عبارة التساوي الشرطية

الدالة `eq[x; y]` معرّفة فقط عندما يكون كل من $x$ و $y$ رمزين ذريين. تُرجع `T` إذا كان $x$ و $y$ نفس الرمز، و `F` خلاف ذلك.

أمثلة:
- `eq[A; A]` = `T`
- `eq[A; B]` = `F`
- `eq[NIL; NIL]` = `T`

ملاحظة: `eq` غير معرّفة للمعاملات غير الذرية.

**3. car[x]** - استخراج العنصر الأول

بالنسبة للزوج المنقط $(e_1 \cdot e_2)$، الدالة `car[x]` تُرجع العنصر الأول $e_1$.

أمثلة:
- `car[(A · B)]` = `A`
- `car[((A · B) · C)]` = `(A · B)`
- `car[(A B C)]` = `car[(A · (B · (C · NIL)))]` = `A`

اسم "CAR" يرمز إلى "محتويات سجل العنوان" (Contents of Address Register) من معمارية IBM 704.

**4. cdr[x]** - استخراج بقية القائمة

بالنسبة للزوج المنقط $(e_1 \cdot e_2)$، الدالة `cdr[x]` تُرجع العنصر الثاني $e_2$.

أمثلة:
- `cdr[(A · B)]` = `B`
- `cdr[(A · (B · C))]` = `(B · C)`
- `cdr[(A B C)]` = `cdr[(A · (B · (C · NIL)))]` = `(B C)`

اسم "CDR" يرمز إلى "محتويات سجل التناقص" (Contents of Decrement Register).

**5. cons[x; y]** - بناء زوج

الدالة `cons[x; y]` تبني زوجاً منقطاً جديداً مع $x$ كالعنصر الأول و $y$ كالعنصر الثاني. إنها العملية العكسية لـ `car` و `cdr`.

أمثلة:
- `cons[A; B]` = `(A · B)`
- `cons[A; (B · C)]` = `(A · (B · C))` = `(A B C)`
- `cons[(A · B); C]` = `((A · B) · C)`

**خصائص الهوية:**

لأي زوج منقط $x$:
$$\text{cons}[\text{car}[x]; \text{cdr}[x]] = x$$

لأي تعبيري S، $e_1$ و $e_2$:
$$\text{car}[\text{cons}[e_1; e_2]] = e_1$$
$$\text{cdr}[\text{cons}[e_1; e_2]] = e_2$$

**بناء دوال معقدة:**

من هذه الدوال الأولية الخمس، يمكننا بناء دوال أكثر تعقيداً من خلال التركيب. على سبيل المثال:

- `caar[x]` = `car[car[x]]` (العنصر الأول من العنصر الأول)
- `cadr[x]` = `car[cdr[x]]` (العنصر الثاني من قائمة)
- `caddr[x]` = `car[cdr[cdr[x]]]` (العنصر الثالث من قائمة)

**معالجة القوائم العودية:**

تصبح قوة هذه الأوليات واضحة عند دمجها مع العودية. على سبيل المثال، دالة لحساب طول قائمة:

```lisp
length[x] = [atom[x] → 0; T → 1 + length[cdr[x]]]
```

تعالج هذه القائمة بشكل عودي عن طريق:
1. إذا كانت القائمة فارغة (ذرية)، أرجع 0
2. خلاف ذلك، أضف 1 وعالج بقية القائمة بشكل عودي

**العمومية:**

هذه الدوال الأولية الخمس، مع التعبيرات الشرطية والتعريفات العودية، كافية للتعبير عن أي دالة قابلة للحوسبة على تعبيرات S. هذه العمومية مماثلة لعمومية آلات تورينغ ولكن يتم التعبير عنها بطريقة أكثر طبيعية وتركيبية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** atom, eq, car, cdr, cons, predicate, primitive function, composition, identity properties
- **Equations:** 3 identity equations
- **Citations:** None
- **Special handling:**
  - Function names (atom, eq, car, cdr, cons) kept in English (standard LISP primitives)
  - Function notation preserved: `function[args]`
  - Code examples in LISP notation with Arabic explanations
  - Boolean values T and F kept in English
  - Identity properties shown with mathematical notation
  - Composition examples (caar, cadr, caddr) kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
