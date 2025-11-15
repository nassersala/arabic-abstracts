# Section 5: Representation and Storage of S-expressions
## القسم 5: تمثيل وتخزين تعبيرات S

**Section:** representation
**Translation Quality:** 0.86
**Glossary Terms Used:** representation, memory, storage, pointer, data structure, binary, register, address

---

### English Version

The representation of S-expressions in computer memory is a critical aspect of LISP's implementation. The elegance of S-expressions as an abstract data structure must be mapped onto the concrete architecture of the IBM 704 computer.

**Memory Representation:**

Each S-expression is stored using a **cons cell** (short for "construct cell"), which consists of two machine words:

1. **CAR field** (Contents of Address Register): Stores the first element of a dotted pair or a pointer to it
2. **CDR field** (Contents of Decrement Register): Stores the second element of a dotted pair or a pointer to it

These names derive from the IBM 704 machine architecture, where the address and decrement parts of a word could be extracted and modified separately.

**Atomic Symbols:**

Atomic symbols are represented differently from cons cells:
- A special tag bit indicates whether a word represents an atom or a pointer to a cons cell
- For atoms, the word contains a pointer to a **property list** that stores the symbol's name and associated properties
- Common atoms like `T`, `F`, and `NIL` have fixed locations in memory

**List Structure:**

A list like `(A B C)` is represented as a chain of cons cells:

```
[A|•]→[B|•]→[C|NIL]
```

Where:
- The CAR of each cell points to an element (A, B, or C)
- The CDR of each cell points to the next cons cell (or NIL for the last cell)
- `•` represents a pointer to the next cell

**Sharing and Circular Structures:**

Because S-expressions are represented using pointers, multiple structures can share common substructures:

```lisp
X = (A B C)
Y = (X D E)  ; Y = ((A B C) D E)
```

The list `X` is not copied into `Y`; instead, `Y`'s first element points to the same structure as `X`. This sharing is:
- **Memory efficient:** Avoids duplication
- **Semantically important:** Changes to shared structure affect all references

Circular structures are also possible (though potentially dangerous):

```lisp
; A list that points to itself
X = (A . X)
```

**Garbage Collection:**

As computation proceeds, cons cells are allocated from a pool of **free storage**. When storage is exhausted, a **garbage collector** reclaims cells that are no longer accessible from any active computation. The original LISP system used a **mark-and-sweep** algorithm:

1. **Mark phase:** Starting from root references (variables, stack), mark all reachable cells
2. **Sweep phase:** Collect all unmarked cells back into the free list

This automatic memory management was revolutionary in 1960 and remains a defining feature of LISP-family languages.

**Address Calculations:**

The IBM 704 had special instructions for manipulating the address and decrement fields of a word, making CAR and CDR operations efficient:
- **CAR operation:** Extract the address field
- **CDR operation:** Extract the decrement field
- **CONS operation:** Combine two values into a single word with proper tagging

**Storage Efficiency Considerations:**

McCarthy noted several efficiency concerns:
1. **Fragmentation:** Free storage becomes fragmented over time
2. **Garbage collection overhead:** Collection pauses can be significant
3. **Pointer overhead:** Each element requires full word storage even for small values

Despite these concerns, the uniform representation of S-expressions as cons cells provides:
- **Simplicity:** Only one data structure type to implement
- **Flexibility:** Can represent any tree structure
- **Homoiconicity:** Programs and data have identical representation

---

### النسخة العربية

يعد تمثيل تعبيرات S في ذاكرة الحاسوب جانباً حاسماً في تطبيق LISP. يجب تعيين أناقة تعبيرات S كبنية بيانات مجردة على المعمارية الملموسة لحاسوب IBM 704.

**تمثيل الذاكرة:**

يتم تخزين كل تعبير S باستخدام **خلية cons** (اختصار لـ "خلية البناء" - construct cell)، والتي تتكون من كلمتي آلة:

1. **حقل CAR** (محتويات سجل العنوان - Contents of Address Register): يخزن العنصر الأول من زوج منقط أو مؤشراً إليه
2. **حقل CDR** (محتويات سجل التناقص - Contents of Decrement Register): يخزن العنصر الثاني من زوج منقط أو مؤشراً إليه

تأتي هذه الأسماء من معمارية آلة IBM 704، حيث يمكن استخراج وتعديل أجزاء العنوان والتناقص من الكلمة بشكل منفصل.

**الرموز الذرية:**

يتم تمثيل الرموز الذرية بشكل مختلف عن خلايا cons:
- تشير بِتة وسم خاصة إلى ما إذا كانت الكلمة تمثل ذرة أو مؤشراً إلى خلية cons
- بالنسبة للذرات، تحتوي الكلمة على مؤشر إلى **قائمة خصائص** (property list) تخزن اسم الرمز والخصائص المرتبطة به
- الذرات الشائعة مثل `T` و `F` و `NIL` لها مواقع ثابتة في الذاكرة

**بنية القائمة:**

يتم تمثيل قائمة مثل `(A B C)` كسلسلة من خلايا cons:

```
[A|•]→[B|•]→[C|NIL]
```

حيث:
- يشير CAR لكل خلية إلى عنصر (A أو B أو C)
- يشير CDR لكل خلية إلى خلية cons التالية (أو NIL للخلية الأخيرة)
- `•` يمثل مؤشراً إلى الخلية التالية

**المشاركة والبنى الدائرية:**

نظراً لأن تعبيرات S يتم تمثيلها باستخدام المؤشرات، يمكن لبنى متعددة مشاركة بنى فرعية مشتركة:

```lisp
X = (A B C)
Y = (X D E)  ; Y = ((A B C) D E)
```

القائمة `X` لا يتم نسخها إلى `Y`؛ بدلاً من ذلك، يشير العنصر الأول لـ `Y` إلى نفس البنية مثل `X`. هذه المشاركة:
- **فعالة من حيث الذاكرة:** تتجنب التكرار
- **مهمة دلالياً:** التغييرات على البنية المشتركة تؤثر على جميع المراجع

البنى الدائرية ممكنة أيضاً (على الرغم من كونها خطرة محتملاً):

```lisp
; قائمة تشير إلى نفسها
X = (A . X)
```

**جمع القمامة:**

مع تقدم الحساب، يتم تخصيص خلايا cons من مجموعة **التخزين الحر** (free storage). عندما ينفد التخزين، يستعيد **جامع القمامة** (garbage collector) الخلايا التي لم تعد قابلة للوصول من أي حساب نشط. استخدم نظام LISP الأصلي خوارزمية **المَرْك والمسح** (mark-and-sweep):

1. **مرحلة المَرْك:** بدءاً من المراجع الجذرية (المتغيرات، المكدس)، قم بوسم جميع الخلايا القابلة للوصول
2. **مرحلة المسح:** اجمع جميع الخلايا غير الموسومة مرة أخرى في قائمة الحرة

كانت هذه الإدارة الآلية للذاكرة ثورية في عام 1960 ولا تزال سمة مميزة للغات عائلة LISP.

**حسابات العناوين:**

كانت لدى IBM 704 تعليمات خاصة لمعالجة حقول العنوان والتناقص من الكلمة، مما يجعل عمليات CAR و CDR فعالة:
- **عملية CAR:** استخراج حقل العنوان
- **عملية CDR:** استخراج حقل التناقص
- **عملية CONS:** دمج قيمتين في كلمة واحدة مع الوسم المناسب

**اعتبارات كفاءة التخزين:**

أشار مكارثي إلى عدة مخاوف تتعلق بالكفاءة:
1. **التجزئة (Fragmentation):** يصبح التخزين الحر مجزأً مع مرور الوقت
2. **عبء جمع القمامة:** يمكن أن تكون فترات التوقف للجمع كبيرة
3. **عبء المؤشرات:** يتطلب كل عنصر تخزين كلمة كاملة حتى للقيم الصغيرة

على الرغم من هذه المخاوف، يوفر التمثيل الموحد لتعبيرات S كخلايا cons:
- **البساطة:** نوع واحد فقط من بنية البيانات للتطبيق
- **المرونة:** يمكن تمثيل أي بنية شجرية
- **التماثل الأيقوني:** البرامج والبيانات لها تمثيل متطابق

---

### Translation Notes

- **Figures referenced:** ASCII diagram of list structure
- **Key terms introduced:** cons cell, property list, garbage collection, mark-and-sweep, free storage, sharing, circular structure, fragmentation
- **Equations:** None
- **Citations:** None
- **Special handling:**
  - "cons cell" translated as "خلية cons"
  - "CAR" and "CDR" kept in English with Arabic explanation
  - "garbage collection" translated as "جمع القمامة" (standard term)
  - "mark-and-sweep" translated as "المَرْك والمسح"
  - Code examples and diagrams kept in English notation
  - IBM 704 architecture details explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
