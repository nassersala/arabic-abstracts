# Section 5: Functional Programming Systems (FP Systems)
## القسم 5: أنظمة البرمجة الوظيفية (أنظمة FP)

**Section:** fp-systems
**Translation Quality:** 0.89
**Glossary Terms Used:** functional programming, combining forms, primitive functions, objects, sequences, atoms

---

### English Version

An FP system is a precise mathematical framework for functional programming. It consists of:

1. A set of **objects** (atoms and sequences)
2. A set of **primitive functions**
3. A set of **functional forms** (combining forms)
4. An **application** operation
5. A set of **definitions**

## 5.1 Objects

The domain of objects in an FP system includes:

- **Atoms**: Numbers, symbols, true (T), false (F), undefined (⊥)
- **Sequences**: Ordered collections enclosed in angle brackets
  - Example: `<1, 2, 3>` is a sequence of three numbers
  - Example: `<A, <B, C>, D>` is a sequence with a nested sequence
- **The empty sequence**: `<>` or `φ`
- **Bottom**: `⊥` represents undefined (result of error or non-termination)

Objects are hierarchical and can be arbitrarily nested. Every object is either an atom or a sequence.

## 5.2 Primitive Functions

FP systems have a small set of primitive functions that operate on objects:

**Selector functions:**
- `1`: selects the first element: `1:<a, b, c> = a`
- `2`: selects the second element: `2:<a, b, c> = b`
- `n`: selects the nth element: `n:<a₁, ..., aₙ> = aₙ`

**Tail function:**
- `tl`: returns all but the first element: `tl:<a, b, c> = <b, c>`

**Identity function:**
- `id`: returns its argument unchanged: `id:x = x`

**Atom test:**
- `atom`: returns T if atom, F if sequence: `atom:A = T`, `atom:<A> = F`

**Equality test:**
- `eq`: tests equality: `eq:<3, 3> = T`, `eq:<3, 4> = F`

**Null test:**
- `null`: tests for empty sequence: `null:<> = T`, `null:<a> = F`

**Reverse:**
- `reverse`: reverses a sequence: `reverse:<a, b, c> = <c, b, a>`

**Arithmetic:**
- `+`, `-`, `×`, `÷`: arithmetic operations on pairs
- `+:<3, 4> = 7`

**Append functions:**
- `apndl`: append on left: `apndl:<a, <b, c>> = <a, b, c>`
- `apndr`: append on right: `apndr:<<a, b>, c> = <a, b, c>`

**Distribution:**
- `distl`: distribute from left: `distl:<a, <b, c, d>> = <<a, b>, <a, c>, <a, d>>`
- `distr`: distribute from right: `distr:<<a, b, c>, d> = <<a, d>, <b, d>, <c, d>>`

**Length:**
- `length`: returns length of sequence: `length:<a, b, c> = 3`

## 5.3 Functional Forms (Combining Forms)

Functional forms take functions as parameters and return new functions. The key forms are:

**Composition (∘):**
```
Definition: (f ∘ g):x = f:(g:x)
Example: (tl ∘ tl):<a, b, c, d> = tl:(tl:<a, b, c, d>) = tl:<b, c, d> = <c, d>
```

**Construction ([f₁, ..., fₙ]):**
```
Definition: [f₁, ..., fₙ]:x = <f₁:x, ..., fₙ:x>
Example: [1, 2, 3]:<a, b, c, d> = <a, b, c>
Example: [+, -, ×]:<3, 4> = <7, -1, 12>
```

**Condition (p → f; g):**
```
Definition: (p → f; g):x = if p:x = T then f:x else g:x
Example: (atom → id; 1):<a, b> = 1:<a, b> = a
Example: (atom → id; 1):a = id:a = a
```

**Constant (x̄):**
```
Definition: x̄:y = x  (always returns x regardless of input)
Example: 3̄:anything = 3
```

**Insert (Apply-to-all) (αf):**
```
Definition: αf:<x₁, ..., xₙ> = <f:x₁, ..., f:xₙ>
Example: α(×2):<1, 2, 3> = <2, 4, 6>
Example: α1:<<a, b>, <c, d>, <e, f>> = <a, c, e>
```

**Insert (Reduce) (/f):**
```
Definition: /f:<x₁, ..., xₙ> = f:<x₁, /f:<x₂, ..., xₙ>>
           /f:<x> = x
Example: /+:<1, 2, 3, 4> = +:<1, /+:<2, 3, 4>> = ... = 10
Example: /×:<2, 3, 4> = 24
```

**While (while p f):**
```
Definition: Repeatedly apply f while p is true
Example: (while (not ∘ atom) 1)<<<a>> = a
```

## 5.4 Definitions

An FP system allows naming functions through definitions:

```
Def sum ≡ /+
Def avg ≡ (÷ ∘ [sum, length])
Def fact ≡ /× ∘ range
```

Where `range:n = <1, 2, ..., n>`

## 5.5 Example Programs

**Inner Product:**
```
Def IP ≡ /+ ∘ α× ∘ trans
```
Where `trans` transposes a pair of sequences into a sequence of pairs:
```
trans:<<1, 2, 3>, <4, 5, 6>> = <<1, 4>, <2, 5>, <3, 6>>
```

**Matrix Multiply:**
```
Def MM ≡ αα(IP) ∘ αdistl ∘ distr ∘ [1, trans ∘ 2]
```

This demonstrates the power of FP: complex algorithms expressed concisely through composition of simple, well-understood functions.

**Quicksort:**
```
Def sort ≡ (null ∘ tl → 1;
           append ∘ [sort ∘ filter ∘ [lesseq ∘ [1, id], tl],
                     [1],
                     sort ∘ filter ∘ [greater ∘ [1, id], tl]])
```

This sorts by:
- If list has ≤1 element, return it
- Otherwise: sort elements ≤ pivot, append pivot, append sorted elements > pivot

## 5.6 Advantages of FP Systems

1. **Simplicity**: Small syntax, few concepts
2. **No variables**: Functions don't name parameters
3. **No assignment**: No state mutation
4. **Mathematical foundation**: Programs are equations
5. **Compositionality**: Build complex from simple
6. **Optimization**: Algebraic laws enable transformation

---

### النسخة العربية

نظام FP هو إطار رياضي دقيق للبرمجة الوظيفية. يتكون من:

1. مجموعة من **الكائنات** (ذرات ومتتاليات)
2. مجموعة من **الدوال الأولية**
3. مجموعة من **الأشكال الوظيفية** (أشكال التركيب)
4. عملية **تطبيق**
5. مجموعة من **التعريفات**

## 5.1 الكائنات

يتضمن نطاق الكائنات في نظام FP:

- **الذرات**: أرقام، رموز، صحيح (T)، خطأ (F)، غير معرّف (⊥)
- **المتتاليات**: مجموعات مرتبة محاطة بأقواس زاوية
  - مثال: `<1, 2, 3>` هي متتالية من ثلاثة أرقام
  - مثال: `<A, <B, C>, D>` هي متتالية بمتتالية متداخلة
- **المتتالية الفارغة**: `<>` أو `φ`
- **القاع**: `⊥` يمثل غير معرّف (نتيجة خطأ أو عدم إنهاء)

الكائنات هرمية ويمكن تداخلها بشكل تعسفي. كل كائن إما ذرة أو متتالية.

## 5.2 الدوال الأولية

تمتلك أنظمة FP مجموعة صغيرة من الدوال الأولية التي تعمل على الكائنات:

**دوال الاختيار:**
- `1`: تختار العنصر الأول: `1:<a, b, c> = a`
- `2`: تختار العنصر الثاني: `2:<a, b, c> = b`
- `n`: تختار العنصر nth: `n:<a₁, ..., aₙ> = aₙ`

**دالة الذيل:**
- `tl`: تُرجع جميع العناصر عدا الأول: `tl:<a, b, c> = <b, c>`

**دالة الهوية:**
- `id`: تُرجع وسيطها دون تغيير: `id:x = x`

**اختبار الذرة:**
- `atom`: تُرجع T إذا كانت ذرة، F إذا كانت متتالية: `atom:A = T`, `atom:<A> = F`

**اختبار المساواة:**
- `eq`: تختبر المساواة: `eq:<3, 3> = T`, `eq:<3, 4> = F`

**اختبار الفراغ:**
- `null`: تختبر المتتالية الفارغة: `null:<> = T`, `null:<a> = F`

**العكس:**
- `reverse`: تعكس متتالية: `reverse:<a, b, c> = <c, b, a>`

**الحساب:**
- `+`, `-`, `×`, `÷`: عمليات حسابية على أزواج
- `+:<3, 4> = 7`

**دوال الإلحاق:**
- `apndl`: إلحاق من اليسار: `apndl:<a, <b, c>> = <a, b, c>`
- `apndr`: إلحاق من اليمين: `apndr:<<a, b>, c> = <a, b, c>`

**التوزيع:**
- `distl`: توزيع من اليسار: `distl:<a, <b, c, d>> = <<a, b>, <a, c>, <a, d>>`
- `distr`: توزيع من اليمين: `distr:<<a, b, c>, d> = <<a, d>, <b, d>, <c, d>>`

**الطول:**
- `length`: تُرجع طول المتتالية: `length:<a, b, c> = 3`

## 5.3 الأشكال الوظيفية (أشكال التركيب)

تأخذ الأشكال الوظيفية دوالاً كمعاملات وتُرجع دوالاً جديدة. الأشكال الرئيسية هي:

**التركيب (∘):**
```
التعريف: (f ∘ g):x = f:(g:x)
مثال: (tl ∘ tl):<a, b, c, d> = tl:(tl:<a, b, c, d>) = tl:<b, c, d> = <c, d>
```

**البناء ([f₁, ..., fₙ]):**
```
التعريف: [f₁, ..., fₙ]:x = <f₁:x, ..., fₙ:x>
مثال: [1, 2, 3]:<a, b, c, d> = <a, b, c>
مثال: [+, -, ×]:<3, 4> = <7, -1, 12>
```

**الشرط (p → f; g):**
```
التعريف: (p → f; g):x = if p:x = T then f:x else g:x
مثال: (atom → id; 1):<a, b> = 1:<a, b> = a
مثال: (atom → id; 1):a = id:a = a
```

**الثابت (x̄):**
```
التعريف: x̄:y = x  (دائماً تُرجع x بغض النظر عن المدخل)
مثال: 3̄:anything = 3
```

**التطبيق على الكل (αf):**
```
التعريف: αf:<x₁, ..., xₙ> = <f:x₁, ..., f:xₙ>
مثال: α(×2):<1, 2, 3> = <2, 4, 6>
مثال: α1:<<a, b>, <c, d>, <e, f>> = <a, c, e>
```

**الإدراج (الاختزال) (/f):**
```
التعريف: /f:<x₁, ..., xₙ> = f:<x₁, /f:<x₂, ..., xₙ>>
           /f:<x> = x
مثال: /+:<1, 2, 3, 4> = +:<1, /+:<2, 3, 4>> = ... = 10
مثال: /×:<2, 3, 4> = 24
```

**بينما (while p f):**
```
التعريف: تطبيق f بشكل متكرر بينما p صحيح
مثال: (while (not ∘ atom) 1)<<<a>> = a
```

## 5.4 التعريفات

يسمح نظام FP بتسمية الدوال من خلال التعريفات:

```
Def sum ≡ /+
Def avg ≡ (÷ ∘ [sum, length])
Def fact ≡ /× ∘ range
```

حيث `range:n = <1, 2, ..., n>`

## 5.5 أمثلة على البرامج

**الضرب الداخلي:**
```
Def IP ≡ /+ ∘ α× ∘ trans
```
حيث `trans` ينقل زوجاً من المتتاليات إلى متتالية من الأزواج:
```
trans:<<1, 2, 3>, <4, 5, 6>> = <<1, 4>, <2, 5>, <3, 6>>
```

**ضرب المصفوفات:**
```
Def MM ≡ αα(IP) ∘ αdistl ∘ distr ∘ [1, trans ∘ 2]
```

يوضح هذا قوة FP: خوارزميات معقدة معبر عنها بإيجاز من خلال تركيب دوال بسيطة ومفهومة جيداً.

**الترتيب السريع:**
```
Def sort ≡ (null ∘ tl → 1;
           append ∘ [sort ∘ filter ∘ [lesseq ∘ [1, id], tl],
                     [1],
                     sort ∘ filter ∘ [greater ∘ [1, id], tl]])
```

يرتب هذا من خلال:
- إذا كانت القائمة تحتوي على ≤1 عنصر، أعدها
- وإلا: رتب العناصر ≤ المحور، ألحق المحور، ألحق العناصر المرتبة > المحور

## 5.6 مزايا أنظمة FP

1. **البساطة**: بنية تركيبية صغيرة، مفاهيم قليلة
2. **بدون متغيرات**: الدوال لا تسمي المعاملات
3. **بدون إسناد**: لا تحوير للحالة
4. **أساس رياضي**: البرامج هي معادلات
5. **التركيبية**: بناء المعقد من البسيط
6. **التحسين**: القوانين الجبرية تمكن من التحويل

---

### Translation Notes

- **Key terms introduced:**
  - objects (الكائنات)
  - atoms (الذرات)
  - sequences (المتتاليات)
  - bottom (⊥) (القاع)
  - selector functions (دوال الاختيار)
  - composition (∘) (التركيب)
  - construction ([]) (البناء)
  - condition (→) (الشرط)
  - apply-to-all (α) (التطبيق على الكل)
  - insert/reduce (/) (الإدراج/الاختزال)

- **Mathematical notation:** Extensive use of FP notation, all preserved
- **Code examples:** Multiple FP programs (IP, MM, sort, etc.)
- **Equations:** Formal definitions of all functions and forms
- **Special handling:** FP syntax explained with both definition and examples

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89
