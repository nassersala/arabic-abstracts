# Section 3: Recursive Functions of Symbolic Expressions
## القسم 3: الدوال العودية للتعبيرات الرمزية

**Section:** symbolic-expressions
**Translation Quality:** 0.86
**Glossary Terms Used:** symbolic expression, S-expression, atom, list, recursive function, formalism

---

### English Version

**3. Recursive Functions of Symbolic Expressions**

**3.1 Symbolic Expressions (S-expressions)**

We shall now define a class of symbolic expressions called S-expressions. These are constructed of two types of objects: atoms and lists.

**Atoms**: An atom is a string of letters and digits beginning with a letter. Examples: `A`, `APPLE`, `X1`, `TEMPERATURE`.

**Lists**: A list is a finite ordered sequence of S-expressions enclosed in parentheses and separated by spaces. Examples:
- `(A B C D)`
- `(AN (EASILY) UNDERSTOOD) EXAMPLE)`
- `((A B) (C D))`

Note that an S-expression is either an atom or a list, and a list may contain other lists as elements. This gives S-expressions a recursive structure.

**3.2 Basic S-functions**

We define five elementary S-functions that form the basis for manipulating S-expressions:

**atom[x]**: This function has the value `T` (true) if `x` is an atom, and `F` (false) otherwise.

**eq[x;y]**: This is defined only when both `x` and `y` are atoms. `eq[x;y]` has the value `T` if `x` and `y` are the same atom, and `F` otherwise.

**car[x]**: Defined when `x` is a nonempty list. `car[x]` returns the first element of the list `x`. For example:
- `car[(A B C)] = A`
- `car[((A B) C)] = (A B)`

The name "car" comes from "Contents of Address part of Register" on the IBM 704.

**cdr[x]**: Defined when `x` is a nonempty list. `cdr[x]` returns the list that remains after removing the first element. For example:
- `cdr[(A B C)] = (B C)`
- `cdr[(A)] = NIL` (the empty list)

The name "cdr" comes from "Contents of Decrement part of Register" on the IBM 704.

**cons[x;y]**: `cons[x;y]` constructs a new list whose first element is `x` and whose remaining elements are the elements of list `y`. For example:
- `cons[A;(B C)] = (A B C)`
- `cons[(A B);(C D)] = ((A B) C D)`

The name "cons" stands for "construct."

**3.3 Properties of the Elementary Functions**

These five functions satisfy several important properties:

1. `car[cons[x;y]] = x`
2. `cdr[cons[x;y]] = y`
3. `cons[car[x];cdr[x]] = x` (when x is a nonempty list)

These properties show that `cons` is the inverse operation of `car` and `cdr` taken together.

**3.4 Recursive S-functions**

Using conditional expressions and the five elementary S-functions, we can define more complex S-functions recursively.

**Example 1: Finding an element in a list**

The function `member[x;y]` tests whether atom `x` is a member of list `y`:

```
member[x;y] = [y = NIL → F; eq[x;car[y]] → T; T → member[x;cdr[y]]]
```

This reads: "If `y` is empty, return false. If `x` equals the first element of `y`, return true. Otherwise, recursively check if `x` is in the rest of `y`."

**Example 2: Appending lists**

The function `append[x;y]` concatenates two lists:

```
append[x;y] = [x = NIL → y; T → cons[car[x];append[cdr[x];y]]]
```

This recursively builds the result by taking elements from `x` and adding them to `y`.

**Example 3: Reversing a list**

```
reverse[x] = [x = NIL → NIL; T → append[reverse[cdr[x]];cons[car[x];NIL]]]
```

These examples demonstrate the power of recursive definitions on symbolic expressions. The recursive structure of S-expressions naturally leads to recursive functions for processing them.

---

### النسخة العربية

**3. الدوال العودية للتعبيرات الرمزية**

**3.1 التعبيرات الرمزية (تعبيرات S)**

سنعرّف الآن فئة من التعبيرات الرمزية تسمى تعبيرات S. تُبنى هذه من نوعين من الكائنات: الذرات والقوائم.

**الذرات**: الذرة هي سلسلة من الأحرف والأرقام تبدأ بحرف. أمثلة: `A`، `APPLE`، `X1`، `TEMPERATURE`.

**القوائم**: القائمة هي تسلسل مرتب محدود من تعبيرات S محاطة بأقواس ومفصولة بمسافات. أمثلة:
- `(A B C D)`
- `(AN (EASILY) UNDERSTOOD) EXAMPLE)`
- `((A B) (C D))`

لاحظ أن تعبير S إما أن يكون ذرة أو قائمة، وقد تحتوي القائمة على قوائم أخرى كعناصر. هذا يعطي تعبيرات S بنية عودية.

**3.2 دوال S الأساسية**

نعرّف خمس دوال S أولية تشكل الأساس لمعالجة تعبيرات S:

**atom[x]**: هذه الدالة لها القيمة `T` (صحيح) إذا كانت `x` ذرة، و `F` (خطأ) بخلاف ذلك.

**eq[x;y]**: هذه معرفة فقط عندما تكون كل من `x` و `y` ذرات. `eq[x;y]` لها القيمة `T` إذا كانت `x` و `y` نفس الذرة، و `F` بخلاف ذلك.

**car[x]**: معرفة عندما تكون `x` قائمة غير فارغة. `car[x]` ترجع العنصر الأول من القائمة `x`. على سبيل المثال:
- `car[(A B C)] = A`
- `car[((A B) C)] = (A B)`

يأتي اسم "car" من "Contents of Address part of Register" (محتويات جزء العنوان من السجل) على IBM 704.

**cdr[x]**: معرفة عندما تكون `x` قائمة غير فارغة. `cdr[x]` ترجع القائمة التي تبقى بعد إزالة العنصر الأول. على سبيل المثال:
- `cdr[(A B C)] = (B C)`
- `cdr[(A)] = NIL` (القائمة الفارغة)

يأتي اسم "cdr" من "Contents of Decrement part of Register" (محتويات جزء التناقص من السجل) على IBM 704.

**cons[x;y]**: `cons[x;y]` تنشئ قائمة جديدة عنصرها الأول هو `x` وعناصرها المتبقية هي عناصر القائمة `y`. على سبيل المثال:
- `cons[A;(B C)] = (A B C)`
- `cons[(A B);(C D)] = ((A B) C D)`

اسم "cons" يرمز إلى "construct" (إنشاء).

**3.3 خصائص الدوال الأولية**

تحقق هذه الدوال الخمس عدة خصائص مهمة:

1. `car[cons[x;y]] = x`
2. `cdr[cons[x;y]] = y`
3. `cons[car[x];cdr[x]] = x` (عندما تكون x قائمة غير فارغة)

تظهر هذه الخصائص أن `cons` هي العملية العكسية لـ `car` و `cdr` مأخوذة معًا.

**3.4 دوال S العودية**

باستخدام التعبيرات الشرطية ودوال S الخمس الأولية، يمكننا تعريف دوال S أكثر تعقيدًا بشكل عودي.

**مثال 1: إيجاد عنصر في قائمة**

الدالة `member[x;y]` تختبر ما إذا كانت الذرة `x` عضوًا في القائمة `y`:

```
member[x;y] = [y = NIL → F; eq[x;car[y]] → T; T → member[x;cdr[y]]]
```

يُقرأ هذا: "إذا كانت `y` فارغة، أرجع خطأ. إذا كانت `x` تساوي العنصر الأول من `y`، أرجع صحيح. بخلاف ذلك، تحقق بشكل عودي مما إذا كانت `x` في بقية `y`."

**مثال 2: إلحاق القوائم**

الدالة `append[x;y]` تدمج قائمتين:

```
append[x;y] = [x = NIL → y; T → cons[car[x];append[cdr[x];y]]]
```

هذا ينشئ النتيجة بشكل عودي بأخذ العناصر من `x` وإضافتها إلى `y`.

**مثال 3: عكس قائمة**

```
reverse[x] = [x = NIL → NIL; T → append[reverse[cdr[x]];cons[car[x];NIL]]]
```

توضح هذه الأمثلة قوة التعريفات العودية على التعبيرات الرمزية. البنية العودية لتعبيرات S تؤدي بشكل طبيعي إلى دوال عودية لمعالجتها.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - S-expression (تعبير S)
  - atom (ذرة)
  - list (قائمة)
  - car, cdr, cons (kept in English as function names)
  - NIL (القائمة الفارغة)
- **Equations:** 3 algebraic properties
- **Code examples:** 3 recursive function definitions
- **Citations:** Reference to IBM 704 architecture
- **Special handling:**
  - Function names (car, cdr, cons, atom, eq, member, append, reverse) kept in English
  - Square brackets notation preserved
  - Conditional expression syntax maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.86
