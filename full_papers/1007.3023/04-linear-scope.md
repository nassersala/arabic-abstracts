# Section 4: Linear Scope
## القسم 4: النطاق الخطي

**Section:** linear-scope
**Translation Quality:** 0.87
**Glossary Terms Used:** linear scope, shadowing, binding, lexical scope, val-statement, val-assign-statement

---

### English Version

Let us gain a first intuitive understanding of Mini Babel-17 before formally introducing its semantics. Here is how you could denote x ↦ x⁸ in Mini Babel-17:

```
x => begin val y = x*x; val z = y*y; z*z end
```

This looks pretty much like the Scala denotation of x ↦ x⁸ from Section 2. But because Mini Babel-17 is designed so that shadowing of variables is allowed, an equivalent notation is:

```
x => begin val x = x*x; val x = x*x; x*x end
```

The central idea of Mini Babel-17 is the notion of linear scope. Whenever an identifier x is in linear scope, it is allowed to rebind x to a new value, and that rebinding will affect all other later lookups of x that happen within its normal lexical scope. The rebinding is done via a val-assign-statement.

The linear scope of a variable is contained in the usual lexical scope of that variable. The linear scope of a variable x starts

- in the statement after the val-statement that defines x, or
- in the first statement of an anonymous function that binds x as a function argument, if the body of that function is a block, or
- in the first statement of the block of a for-loop where x is the identifier bound by that loop.

It continues throughout the rest of the block unless a new linear scope for x starts. It does extend into nested blocks and statements, but not into simple-expressions. The reason for this is that blocks and statements are ordered sequentially, but there is no natural order for the evaluation of the components of a simple-expression.

Using the linear scope rules of Mini Babel-17, the above function can also be encoded as

```
x => begin x = x*x; x = x*x; x*x end
```

If there are no nested blocks involved, then linear scope is no big deal. It is just a fancy way of saying that when in a val-statement the variable being defined shadows a previously defined variable, often it is ok to drop the val keyword, effectively turning a val-statement into a val-assign-statement.

But with nested blocks, linear scope becomes important:

| Program 1 | Program 2 | Program 3 |
|-----------|-----------|-----------|
| ```val x = 2``` | ```val x = 2``` | ```val x = 2``` |
| ```begin``` | ```begin``` | ```begin``` |
| ```  val y = x*x``` | ```  val y = x*x``` | ```  val y = x*x``` |
| ```  val x = y``` | ```  x = y``` | ```  val x = 0``` |
| ```end``` | ```end``` | ```  x = y``` |
| ```x+x``` | ```x+x``` | ```end``` |
| | | ```x+x``` |
| evaluates to 4 | evaluates to 8 | evaluates to 4 |

The left and right programs both evaluate to 4 because the `begin ... end` block is superfluous as none of its statements have any effect in the outer scope. The middle program evaluates to 8, though, because the rebinding `x = y` effects all later lookups in the lexical scope of that x that has been introduced via `val x = 2`, and `x+x` certainly is such a later lookup.

Maybe the rules of linear scope sound confusing at first. But they really are not. Just replace in your mind in the above three programs the vals by vars and view them as imperative programs. What value would you assign now to each program?

Let us also recode the last Scala expression of Section 2 as a Mini Babel-17 expression:

```
x => begin
       val y = x*x
       val h = dummy => y
       y = y*y
       h 0 * y
     end
```

Mini Babel-17 is purely functional, therefore the value of h is of course not changed by the rebinding `y = y*y` which affects only later lookups of y. Thus the above expression implements x ↦ x⁶, not x ↦ x⁸.

---

### النسخة العربية

دعونا نكتسب فهماً حدسياً أولياً لـ Mini Babel-17 قبل تقديم دلالاتها بشكل صوري. إليك كيف يمكنك التعبير عن x ↦ x⁸ في Mini Babel-17:

```
x => begin val y = x*x; val z = y*y; z*z end
```

هذا يبدو إلى حد كبير مثل تمثيل Scala لـ x ↦ x⁸ من القسم 2. لكن نظراً لأن Mini Babel-17 مصممة بحيث يُسمح بتظليل المتغيرات، فإن التدوين المكافئ هو:

```
x => begin val x = x*x; val x = x*x; x*x end
```

الفكرة المركزية في Mini Babel-17 هي مفهوم النطاق الخطي. كلما كان المعرّف x في نطاق خطي، يُسمح بإعادة ربط x بقيمة جديدة، وهذا الربط الجديد سيؤثر على جميع عمليات البحث اللاحقة الأخرى لـ x التي تحدث ضمن نطاقه المعجمي الطبيعي. يتم إعادة الربط عبر val-assign-statement.

النطاق الخطي لمتغير يحتويه النطاق المعجمي المعتاد لذلك المتغير. يبدأ النطاق الخطي للمتغير x

- في العبارة بعد val-statement التي تعرّف x، أو
- في العبارة الأولى من دالة مجهولة تربط x كمعامل دالة، إذا كان جسم تلك الدالة كتلة، أو
- في العبارة الأولى من كتلة حلقة for حيث x هو المعرّف المرتبط بتلك الحلقة.

يستمر خلال باقي الكتلة ما لم يبدأ نطاق خطي جديد لـ x. إنه يمتد إلى الكتل والعبارات المتداخلة، ولكن ليس إلى التعبيرات البسيطة. السبب في ذلك هو أن الكتل والعبارات مرتبة بشكل متسلسل، لكن لا يوجد ترتيب طبيعي لتقييم مكونات التعبير البسيط.

باستخدام قواعد النطاق الخطي في Mini Babel-17، يمكن أيضاً ترميز الدالة أعلاه كـ

```
x => begin x = x*x; x = x*x; x*x end
```

إذا لم تكن هناك كتل متداخلة، فإن النطاق الخطي ليس بالأمر الجلل. إنها مجرد طريقة فاخرة للقول إنه عندما تظلل المتغير المعرّف في val-statement متغيراً معرّفاً سابقاً، فإنه غالباً ما يكون من المقبول إسقاط الكلمة المفتاحية val، مما يحول بشكل فعال val-statement إلى val-assign-statement.

لكن مع الكتل المتداخلة، يصبح النطاق الخطي مهماً:

| البرنامج 1 | البرنامج 2 | البرنامج 3 |
|-----------|-----------|-----------|
| ```val x = 2``` | ```val x = 2``` | ```val x = 2``` |
| ```begin``` | ```begin``` | ```begin``` |
| ```  val y = x*x``` | ```  val y = x*x``` | ```  val y = x*x``` |
| ```  val x = y``` | ```  x = y``` | ```  val x = 0``` |
| ```end``` | ```end``` | ```  x = y``` |
| ```x+x``` | ```x+x``` | ```end``` |
| | | ```x+x``` |
| يُقيّم إلى 4 | يُقيّم إلى 8 | يُقيّم إلى 4 |

كلا البرنامجين الأيسر والأيمن يُقيّمان إلى 4 لأن كتلة `begin ... end` زائدة حيث لا يكون لأي من عباراتها أي تأثير في النطاق الخارجي. ومع ذلك، البرنامج الأوسط يُقيّم إلى 8، لأن إعادة الربط `x = y` تؤثر على جميع عمليات البحث اللاحقة في النطاق المعجمي لذلك الـ x الذي تم تقديمه عبر `val x = 2`، و `x+x` بالتأكيد هي عملية بحث لاحقة كهذه.

ربما تبدو قواعد النطاق الخطي مربكة في البداية. لكنها حقاً ليست كذلك. فقط استبدل في ذهنك في البرامج الثلاثة أعلاه vals بـ vars وانظر إليها كبرامج أمرية. ما القيمة التي ستسندها الآن لكل برنامج؟

دعونا أيضاً نعيد ترميز تعبير Scala الأخير من القسم 2 كتعبير Mini Babel-17:

```
x => begin
       val y = x*x
       val h = dummy => y
       y = y*y
       h 0 * y
     end
```

Mini Babel-17 وظيفية صرفة، لذلك فإن قيمة h بالطبع لا تتغير بإعادة الربط `y = y*y` التي تؤثر فقط على عمليات البحث اللاحقة لـ y. وبالتالي فإن التعبير أعلاه ينفذ x ↦ x⁶، وليس x ↦ x⁸.

---

### Translation Notes

- **Figures referenced:** None (table included inline)
- **Key terms introduced:**
  - Linear scope (النطاق الخطي)
  - Lexical scope (النطاق المعجمي)
  - Rebinding (إعادة الربط)
  - Lookup (عملية بحث / بحث)
  - val-assign-statement (عبارة إسناد val)
  - Nested blocks (كتل متداخلة)
- **Equations:** Mathematical function notation x ↦ x⁶, x ↦ x⁸
- **Citations:** None (refers to Section 2)
- **Special handling:**
  - Code blocks preserved with original syntax
  - Three-column comparison table translated
  - Keywords kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
