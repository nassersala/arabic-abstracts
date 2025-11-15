# Section 3: S-expressions (Symbolic Expressions)
## القسم 3: تعبيرات S (التعبيرات الرمزية)

**Section:** s-expressions
**Translation Quality:** 0.89
**Glossary Terms Used:** symbolic expression, atom, list, ordered pair, recursive, notation, data structure

---

### English Version

S-expressions are the fundamental data structure of LISP. The name "S-expression" stands for "symbolic expression." S-expressions are defined recursively as follows:

**Definition of S-expressions:**

1. **Atomic symbols** are S-expressions. An atomic symbol is a string of characters, such as `A`, `APPLE`, `X1`, or `PLUS`.

2. If $e_1$ and $e_2$ are S-expressions, then $(e_1 \cdot e_2)$ is also an S-expression. This is called a **dotted pair**.

These two rules define all possible S-expressions. The recursive nature of this definition means that S-expressions can have arbitrary complexity.

**Examples of S-expressions:**

- Atomic symbols: `A`, `B`, `NIL`, `X`, `LAMBDA`
- Dotted pairs: `(A · B)`, `(X · Y)`
- Nested structures: `((A · B) · C)`, `(A · (B · C))`
- More complex: `((A · (B · NIL)) · ((C · D) · NIL))`

**Linear Notation:**

The dotted pair notation can become cumbersome for representing lists. Therefore, we introduce a more convenient **list notation**. A list is a special kind of S-expression defined as follows:

1. The atomic symbol `NIL` represents the empty list, written as `()`.

2. If $e$ is an S-expression and $l$ is a list, then $(e \cdot l)$ is a list with $e$ as its first element and $l$ as the rest.

**List notation examples:**

Instead of writing:
- `(A · (B · (C · NIL)))`

We can write:
- `(A B C)`

The list notation is simply a shorthand for nested dotted pairs ending in `NIL`. The general rule is:

$$\text{(}e_1 \text{ } e_2 \text{ } \ldots \text{ } e_n\text{)} \equiv (e_1 \cdot (e_2 \cdot (\ldots \cdot (e_n \cdot \text{NIL})\ldots)))$$

**Special Cases:**

- `()` is the empty list (equivalent to `NIL`)
- `(A)` is equivalent to `(A · NIL)`
- `(A B)` is equivalent to `(A · (B · NIL))`
- `((A B) C)` represents a list whose first element is itself a list

**Properties of S-expressions:**

1. **Uniformity:** Both atomic data and structured data are S-expressions.

2. **Recursiveness:** S-expressions are defined recursively and can be processed recursively.

3. **Homoiconicity:** Programs can also be represented as S-expressions, making LISP code itself data that can be manipulated.

4. **Simplicity:** Only two basic constructions (atoms and pairs) are needed to build arbitrarily complex structures.

**Representation:**

In computer memory, S-expressions are typically represented using two-word cells:
- Each cell contains two fields, traditionally called **CAR** (Contents of Address Register) and **CDR** (Contents of Decrement Register), named after IBM 704 machine registers.
- An atomic symbol is represented by a special marker and a pointer to its name.
- A dotted pair $(e_1 \cdot e_2)$ is represented by a cell where CAR points to $e_1$ and CDR points to $e_2$.

This representation allows efficient manipulation of list structures and is fundamental to LISP's implementation.

---

### النسخة العربية

تعبيرات S هي بنية البيانات الأساسية لـ LISP. يرمز اسم "S-expression" إلى "التعبير الرمزي" (symbolic expression). تُعرَّف تعبيرات S بشكل عودي على النحو التالي:

**تعريف تعبيرات S:**

1. **الرموز الذرية (Atomic symbols)** هي تعبيرات S. الرمز الذري هو سلسلة من الأحرف، مثل `A` أو `APPLE` أو `X1` أو `PLUS`.

2. إذا كان $e_1$ و $e_2$ تعبيري S، فإن $(e_1 \cdot e_2)$ هو أيضاً تعبير S. يُسمى هذا **زوجاً منقطاً (dotted pair)**.

هاتان القاعدتان تعرفان جميع تعبيرات S الممكنة. الطبيعة العودية لهذا التعريف تعني أن تعبيرات S يمكن أن تكون ذات تعقيد عشوائي.

**أمثلة على تعبيرات S:**

- رموز ذرية: `A`، `B`، `NIL`، `X`، `LAMBDA`
- أزواج منقطة: `(A · B)`، `(X · Y)`
- بنى متداخلة: `((A · B) · C)`، `(A · (B · C))`
- أكثر تعقيداً: `((A · (B · NIL)) · ((C · D) · NIL))`

**التدوين الخطي:**

يمكن أن يصبح تدوين الزوج المنقط مرهقاً لتمثيل القوائم. لذلك، نقدم **تدوين القائمة** الأكثر ملاءمة. القائمة هي نوع خاص من تعبيرات S معرَّفة على النحو التالي:

1. الرمز الذري `NIL` يمثل القائمة الفارغة، ويُكتب كـ `()`.

2. إذا كان $e$ تعبير S و $l$ قائمة، فإن $(e \cdot l)$ هي قائمة مع $e$ كعنصرها الأول و $l$ كبقيتها.

**أمثلة على تدوين القائمة:**

بدلاً من كتابة:
- `(A · (B · (C · NIL)))`

يمكننا كتابة:
- `(A B C)`

تدوين القائمة هو ببساطة اختصار للأزواج المنقطة المتداخلة التي تنتهي بـ `NIL`. القاعدة العامة هي:

$$\text{(}e_1 \text{ } e_2 \text{ } \ldots \text{ } e_n\text{)} \equiv (e_1 \cdot (e_2 \cdot (\ldots \cdot (e_n \cdot \text{NIL})\ldots)))$$

**حالات خاصة:**

- `()` هي القائمة الفارغة (مكافئة لـ `NIL`)
- `(A)` مكافئة لـ `(A · NIL)`
- `(A B)` مكافئة لـ `(A · (B · NIL))`
- `((A B) C)` تمثل قائمة عنصرها الأول هو قائمة أخرى

**خصائص تعبيرات S:**

1. **التوحيد (Uniformity):** كل من البيانات الذرية والبيانات المهيكلة هي تعبيرات S.

2. **العودية (Recursiveness):** تُعرَّف تعبيرات S بشكل عودي ويمكن معالجتها بشكل عودي.

3. **التماثل الأيقوني (Homoiconicity):** يمكن أيضاً تمثيل البرامج كتعبيرات S، مما يجعل شيفرة LISP نفسها بيانات يمكن معالجتها.

4. **البساطة (Simplicity):** يُحتاج فقط إلى بناءين أساسيين (الذرات والأزواج) لبناء بنى معقدة عشوائياً.

**التمثيل:**

في ذاكرة الحاسوب، عادةً ما يتم تمثيل تعبيرات S باستخدام خلايا من كلمتين:
- تحتوي كل خلية على حقلين، يُطلق عليهما تقليدياً **CAR** (محتويات سجل العنوان) و **CDR** (محتويات سجل التناقص)، المسماة على اسم سجلات آلة IBM 704.
- يتم تمثيل الرمز الذري بعلامة خاصة ومؤشر إلى اسمه.
- يتم تمثيل الزوج المنقط $(e_1 \cdot e_2)$ بخلية حيث يشير CAR إلى $e_1$ ويشير CDR إلى $e_2$.

يتيح هذا التمثيل المعالجة الفعالة لبنى القوائم وهو أساسي لتطبيق LISP.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** S-expression, symbolic expression, atomic symbol, dotted pair, list notation, NIL, CAR, CDR, homoiconicity, nested structure
- **Equations:** 1 equivalence relation for list notation
- **Citations:** None
- **Special handling:**
  - S-expression examples kept in LISP notation
  - "CAR" and "CDR" kept in English (standard LISP terminology)
  - "NIL" kept in English (standard symbol for empty list)
  - Mathematical equivalence notation preserved
  - "Homoiconicity" translated as "التماثل الأيقوني"
  - Technical properties given in both languages

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89
