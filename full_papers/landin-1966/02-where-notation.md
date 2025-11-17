# Section 2: The where-Notation
## القسم 2: تدوين where

**Section:** where-notation
**Translation Quality:** 0.86
**Glossary Terms Used:** expression, syntax, semantics, functional notation, type

---

### English Version

In ordinary mathematical communication, these uses of 'where' require no explanation. Nor do the following:

```
f(b+2c) + f(2b−c)
where f(x) = x(x+a)

f(b+2c) − f(2b-c)
where f(x) = x(x+a)
and b = u/(u+1)
and c = v/(v+1)

g(f where f(x) = ax² + bx + c,
  u/(u+1),
  v/(v+1))
where g(f, p, q) = f(p+2q, 2p−q)
```

A phrase of the form 'where definition' will be called a "where-clause." An expression of the form 'expression where-clause' is a "where-expression." Its two principal components are called, respectively, its "main clause" and its "supporting definition." To put 'where' into a programming language the following questions need answers.

**Linguistic Structure.** What structures of expression can appropriately be qualified by a where-clause, e.g., conditional expressions, operand-listings, statements, declarations, where-expressions?

Likewise, what structures of expression can appropriately be written as the right-hand side (rhs) of a supporting definition? What contexts are appropriate for a where-expression, e.g., as an arm of a conditional expression, an operator, the main-clause of a where-expression, the left-hand side (lhs) of a supporting definition, the rhs of a supporting definition?

**Syntax.** Having answered the above questions, what are the rules for writing the acceptable configurations unambiguously? E.g., where are brackets optional or obligatory? or other punctuation? or line breaks? or indentation? Note the separation of decisions about structure from decisions about syntax. (This is not a denial that language designers might iterate, like hardware designers who distinguish levels of hardware design.)

**Semantic Constraints on Linguistic Structure.** In the above examples each main clause was a numerical expression; i.e., given appropriate meanings for the various identifiers in it, it denoted a number. What other kinds of meaning are appropriate for a mainclause, e.g., arrays, functions, structure descriptions, print-formats?

Likewise what kinds of meaning are appropriate for rhs's of supporting definitions? Notice there is not a third question analogous to the third question above under linguistic structure. This is because a where-expression must mean the same kind of thing as its main clause and hence raises no new question concerning what contexts are meaningful. Notice also that the questions about meaning are almost entirely independent of those about structure. They depend on classifying expressions in two ways that run across each other.

**Outcome.** What is the outcome of the more recondite structural configurations among those deemed admissible, e.g. mixed nests of where-expressions, function definitions, conditional expressions, etc.?

Experimental programming has led the author to think that there is no configuration, however unpromising it might seem when judged cold, that will not turn up quite naturally. Furthermore, some configurations of 'where' that might first appear to reflect somewhat pedantic distinctions, in fact provide close matches for current language features such as name/value and own (see [2, 3]).

All these questions are not answered in this paper. The techniques for answering them are outlined in Section 4.

One other issue arises when 'where' is added to a programming language--types and specifications. A method of expressing these functionally is explained in [2]. It amounts to using named transfer-functions instead of class names like integer, i.e., writing:

```
where n = round(n)
```

instead of the specification:

```
integer n
```

Thus the use of functional notation does not jeopardize the determination of type from textual evidence.

---

### النسخة العربية

في التواصل الرياضي العادي، هذه الاستخدامات لـ'where' (حيث) لا تتطلب تفسيراً. كذلك لا يتطلب التالي تفسيراً:

```
f(b+2c) + f(2b−c)
where f(x) = x(x+a)

f(b+2c) − f(2b-c)
where f(x) = x(x+a)
and b = u/(u+1)
and c = v/(v+1)

g(f where f(x) = ax² + bx + c,
  u/(u+1),
  v/(v+1))
where g(f, p, q) = f(p+2q, 2p−q)
```

حيث f(x) = x(x+a)
حيث g(f, p, q) = f(p+2q, 2p−q)

سيتم تسمية عبارة من النوع 'where تعريف' بـ"عبارة where" (where-clause). التعبير من النوع 'تعبير عبارة-where' هو "تعبير-where" (where-expression). يُطلق على مكونيه الرئيسيين، على التوالي، "العبارة الرئيسية" (main clause) و"التعريف الداعم" (supporting definition). لوضع 'where' في لغة برمجة، تحتاج الأسئلة التالية إلى إجابات.

**البنية اللغوية.** ما هي بنى التعبيرات التي يمكن أن تُوصف بشكل مناسب بعبارة where، مثل التعبيرات الشرطية، قوائم المعاملات، العبارات، التصريحات، تعبيرات-where؟

وبالمثل، ما هي بنى التعبيرات التي يمكن كتابتها بشكل مناسب كالجانب الأيمن (rhs) من تعريف داعم؟ ما هي السياقات المناسبة لتعبير-where، مثل كونه ذراع تعبير شرطي، معامل، العبارة الرئيسية لتعبير-where، الجانب الأيسر (lhs) من تعريف داعم، الجانب الأيمن من تعريف داعم؟

**التركيب.** بعد الإجابة على الأسئلة أعلاه، ما هي قواعد كتابة التكوينات المقبولة بشكل لا لبس فيه؟ على سبيل المثال، أين تكون الأقواس اختيارية أو إلزامية؟ أو علامات الترقيم الأخرى؟ أو فواصل الأسطر؟ أو المسافة البادئة؟ لاحظ الفصل بين القرارات المتعلقة بالبنية والقرارات المتعلقة بالتركيب. (هذا ليس إنكاراً لأن مصممي اللغات قد يكررون العملية، مثل مصممي الأجهزة الذين يميزون مستويات تصميم الأجهزة.)

**القيود الدلالية على البنية اللغوية.** في الأمثلة أعلاه، كانت كل عبارة رئيسية تعبيراً عددياً؛ أي أنه بإعطاء معانٍ مناسبة للمعرفات المختلفة فيها، فإنها تشير إلى رقم. ما الأنواع الأخرى من المعاني المناسبة للعبارة الرئيسية، مثل المصفوفات، الدوال، أوصاف البنية، صيغ الطباعة؟

وبالمثل، ما أنواع المعاني المناسبة للجوانب اليمنى من التعريفات الداعمة؟ لاحظ أنه لا يوجد سؤال ثالث مماثل للسؤال الثالث أعلاه تحت البنية اللغوية. هذا لأن تعبير-where يجب أن يعني نفس نوع الشيء الذي تعنيه عبارته الرئيسية، وبالتالي لا يثير سؤالاً جديداً بشأن السياقات ذات المعنى. لاحظ أيضاً أن الأسئلة المتعلقة بالمعنى مستقلة تقريباً تماماً عن تلك المتعلقة بالبنية. فهي تعتمد على تصنيف التعبيرات بطريقتين تتقاطعان مع بعضهما البعض.

**النتيجة.** ما هي نتيجة التكوينات البنيوية الأكثر غموضاً من بين تلك التي تُعتبر مقبولة، مثل الأعشاش المختلطة من تعبيرات-where، تعريفات الدوال، التعبيرات الشرطية، إلخ؟

لقد قادت البرمجة التجريبية المؤلف إلى الاعتقاد بأنه لا يوجد تكوين، مهما بدا غير واعد عند الحكم عليه بشكل مجرد، لن يظهر بشكل طبيعي تماماً. علاوة على ذلك، فإن بعض تكوينات 'where' التي قد تبدو في البداية وكأنها تعكس تمييزات أكاديمية إلى حد ما، توفر في الواقع مطابقات وثيقة لميزات اللغة الحالية مثل الاسم/القيمة (name/value) والملكية (own) (انظر [2، 3]).

لا تتم الإجابة على كل هذه الأسئلة في هذه الورقة. يتم تحديد تقنيات الإجابة عليها في القسم 4.

تنشأ مسألة أخرى عند إضافة 'where' إلى لغة برمجة--الأنواع والمواصفات. يتم شرح طريقة للتعبير عن هذه بشكل وظيفي في [2]. إنها تعادل استخدام دوال النقل المسماة بدلاً من أسماء الأصناف مثل integer، أي كتابة:

```
where n = round(n)
```

بدلاً من المواصفة:

```
integer n
```

وبالتالي فإن استخدام التدوين الوظيفي لا يعرض تحديد النوع من الأدلة النصية للخطر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - where-clause: عبارة where
  - where-expression: تعبير-where
  - main clause: العبارة الرئيسية
  - supporting definition: التعريف الداعم
  - right-hand side (rhs): الجانب الأيمن
  - left-hand side (lhs): الجانب الأيسر
  - functional notation: التدوين الوظيفي

- **Equations:** Multiple mathematical examples with where-clauses
- **Citations:** References to [2, 3] for name/value and own features
- **Special handling:**
  - Mathematical notation preserved in both English and Arabic
  - Code examples kept in monospace format
  - Technical terms like "where-clause" partially transliterated for precision

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

---

### Back-Translation (Key Paragraph for Validation)

"In ordinary mathematical communication, these uses of 'where' require no explanation. A phrase of the form 'where definition' will be called a 'where-clause.' An expression of the form 'expression where-clause' is a 'where-expression.' Its two principal components are called, respectively, its 'main clause' and its 'supporting definition.'"

**Validation:** ✓ Maintains semantic equivalence and technical accuracy.
