# Section 5: Conditionals and Loops
## القسم 5: الشرطيات والحلقات

**Section:** conditionals-loops
**Translation Quality:** 0.86
**Glossary Terms Used:** conditional, loop, structured programming, linear scope, pattern matching

---

### English Version

Conditionals and especially loops are the meat of structured programming. With linear scope, they are easily seen also as part of purely functional programming. All we need to do is to apply linear scoping rules to the nested blocks that the if-, while- and for-statements consist of. For example, this is how you can encode the subtraction based Euclidean algorithm for two non-negative integers in Mini Babel-17:

```
a => b =>
  if a == 0 then
    b
  else
    val a = a
    while b != 0 do
      if a > b then
        a = a - b
      else
        b = b - a
      end
    end
    a
  end
```

Note the line `val a = a` which on first sight seems to be superfluous. But while the linear scope of b encompasses the whole function body, the linear scope of a does not, because linear scope does not extend into simple-expressions. If Mini Babel-17 had pattern matching, the line `val a = a` could be avoided by starting the function definition with

```
[a, b] =>
  ...
```

instead.

---

### النسخة العربية

الشرطيات وخاصة الحلقات هي جوهر البرمجة المهيكلة. مع النطاق الخطي، يُنظر إليها بسهولة أيضاً كجزء من البرمجة الوظيفية الصرفة. كل ما نحتاج إلى فعله هو تطبيق قواعد النطاق الخطي على الكتل المتداخلة التي تتكون منها عبارات if و while و for. على سبيل المثال، هذه هي الطريقة التي يمكنك بها ترميز خوارزمية إقليدس القائمة على الطرح لعددين صحيحين غير سالبين في Mini Babel-17:

```
a => b =>
  if a == 0 then
    b
  else
    val a = a
    while b != 0 do
      if a > b then
        a = a - b
      else
        b = b - a
      end
    end
    a
  end
```

لاحظ السطر `val a = a` الذي يبدو للوهلة الأولى أنه زائد. لكن بينما يشمل النطاق الخطي لـ b جسم الدالة بالكامل، فإن النطاق الخطي لـ a لا يشمل ذلك، لأن النطاق الخطي لا يمتد إلى التعبيرات البسيطة. إذا كانت Mini Babel-17 تحتوي على مطابقة الأنماط، فيمكن تجنب السطر `val a = a` بالبدء بتعريف الدالة بـ

```
[a, b] =>
  ...
```

بدلاً من ذلك.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Conditionals (شرطيات)
  - Loops (حلقات)
  - Euclidean algorithm (خوارزمية إقليدس)
  - Pattern matching (مطابقة الأنماط)
  - Non-negative integers (أعداد صحيحة غير سالبة)
- **Equations:** None
- **Citations:** None
- **Special handling:**
  - Code blocks preserved with original syntax
  - Keywords (if, then, else, while, do, end, val) kept in English
  - Algorithm name (Euclidean) kept recognizable with Arabic transliteration

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
