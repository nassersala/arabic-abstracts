# Section 2: Shadowing is Purely Functional
## القسم 2: التظليل وظيفي صرف

**Section:** shadowing
**Translation Quality:** 0.87
**Glossary Terms Used:** pure function, shadowing, binding, variable, single-assignment, De Bruijn notation

---

### English Version

Here is how you could code in SML the function x ↦ x⁴:

```sml
fn x => let val x = x * x in x * x end
```

There is no doubt that the above denotes a pure function. The fact that the introduction of the variable x via `val x = x * x` shadows the previous binding of x in `fn x` might make it look a little bit more unusual than the more common

```sml
fn x => let val y = x * x in y * y end,
```

but of course both denotations are equivalent. Rewriting both functions in De Bruijn notation [3] would actually yield the exact same closed term.

Yet it seems that the conception that shadowing is somehow wrong lies at the heart of why PFP and SP do not overlap in the mind of many programmers. An instance where shadowing is forbidden in order to obtain a notion of pure variables is the programming language Erlang which features single-assignment of variables. Quoting the inventor of Erlang [1, p. 29]:

> When Erlang sees a statement such as X = 1234, it binds the variable X to the value 1234. Before being bound, X could take any value: it's just an empty hole waiting to be filled. However, once it gets a value, it holds on to it forever.

Clearly in Erlang shadowing is a victim of the idea that variables are not just names bound to values, but that the variables themselves are the state.

Something similar can be observed in the programming language Scala [6]. Scala combines functional and structured programming in an elegant fashion. But when it comes to integrate purely functional programming and SP, Scala does not go all the way: it also forbids shadowing. For example, the following Scala function implements x ↦ x⁸,

```scala
(x : Int) => { val y = x*x; val z = y*y; z*z },
```

but both of the following expressions are illegal in Scala:

```scala
(x : Int) => { val y = x*x; val y = y*y; y*y },
(x : Int) => { val y = x*x; y = y*y; y*y }.
```

The last expression can be turned into a legal Scala expression by replacing the keyword `val`, which introduces immutable variables, with the keyword `var`, which introduces mutable variables:

```scala
(x : Int) => { var y = x*x; y = y*y; y*y }.
```

It might seem that after all, shadowing in Scala is possible! But this is not the case. That `var` behaves differently than shadowing can easily be checked:

```scala
(x : Int) => { var y = x*x
               val h = () => y
               y = y*y
               h() * y }
```

also implements x ↦ x⁸. With shadowing, we would expect above function to implement x ↦ x⁶.

---

### النسخة العربية

إليك كيف يمكنك كتابة الدالة x ↦ x⁴ في SML:

```sml
fn x => let val x = x * x in x * x end
```

لا شك في أن ما سبق يشير إلى دالة صرفة. حقيقة أن تعريف المتغير x عبر `val x = x * x` يظلل الارتباط السابق لـ x في `fn x` قد يجعله يبدو أكثر غرابة قليلاً من الصيغة الأكثر شيوعاً

```sml
fn x => let val y = x * x in y * y end,
```

لكن بالطبع كلا التعبيرين متكافئان. إعادة كتابة كلتا الدالتين بتدوين دي بروين [3] ستؤدي في الواقع إلى نفس الحد المغلق تماماً.

ومع ذلك، يبدو أن التصور بأن التظليل خاطئ بطريقة ما يكمن في قلب سبب عدم تداخل البرمجة الوظيفية الصرفة والبرمجة المهيكلة في ذهن العديد من المبرمجين. مثال على ذلك حيث يُحظر التظليل من أجل الحصول على مفهوم المتغيرات الصرفة هو لغة البرمجة Erlang التي تتميز بالإسناد الأحادي للمتغيرات. اقتباس من مخترع Erlang [1، ص. 29]:

> عندما ترى Erlang عبارة مثل X = 1234، فإنها تربط المتغير X بالقيمة 1234. قبل الارتباط، يمكن لـ X أن يأخذ أي قيمة: إنه مجرد ثقب فارغ ينتظر أن يُملأ. ومع ذلك، بمجرد حصوله على قيمة، يتمسك بها إلى الأبد.

من الواضح أن التظليل في Erlang هو ضحية لفكرة أن المتغيرات ليست مجرد أسماء مرتبطة بقيم، بل أن المتغيرات نفسها هي الحالة.

يمكن ملاحظة شيء مماثل في لغة البرمجة Scala [6]. تجمع Scala بين البرمجة الوظيفية والبرمجة المهيكلة بطريقة أنيقة. لكن عندما يتعلق الأمر بدمج البرمجة الوظيفية الصرفة والبرمجة المهيكلة، لا تذهب Scala إلى نهاية الطريق: فهي أيضاً تحظر التظليل. على سبيل المثال، دالة Scala التالية تنفذ x ↦ x⁸،

```scala
(x : Int) => { val y = x*x; val z = y*y; z*z },
```

لكن كلاً من التعبيرين التاليين غير قانوني في Scala:

```scala
(x : Int) => { val y = x*x; val y = y*y; y*y },
(x : Int) => { val y = x*x; y = y*y; y*y }.
```

يمكن تحويل التعبير الأخير إلى تعبير Scala قانوني باستبدال الكلمة المفتاحية `val`، التي تقدم متغيرات غير قابلة للتغيير، بالكلمة المفتاحية `var`، التي تقدم متغيرات قابلة للتغيير:

```scala
(x : Int) => { var y = x*x; y = y*y; y*y }.
```

قد يبدو أنه في النهاية، التظليل في Scala ممكن! لكن هذا ليس هو الحال. أن `var` يتصرف بشكل مختلف عن التظليل يمكن التحقق منه بسهولة:

```scala
(x : Int) => { var y = x*x
               val h = () => y
               y = y*y
               h() * y }
```

أيضاً ينفذ x ↦ x⁸. مع التظليل، نتوقع أن الدالة أعلاه تنفذ x ↦ x⁶.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Shadowing (التظليل)
  - Pure function (دالة صرفة)
  - Binding (ارتباط)
  - Single-assignment (إسناد أحادي)
  - De Bruijn notation (تدوين دي بروين)
  - Closed term (حد مغلق)
  - Immutable variables (متغيرات غير قابلة للتغيير)
  - Mutable variables (متغيرات قابلة للتغيير)
- **Equations:** Mathematical function notation x ↦ x⁴, x ↦ x⁶, x ↦ x⁸
- **Citations:** [1] Armstrong (Erlang inventor), [3] De Bruijn, [6] Scala
- **Special handling:**
  - Code blocks kept in original syntax
  - Keywords (val, var, fn, let, in) kept in English
  - Mathematical notation preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
