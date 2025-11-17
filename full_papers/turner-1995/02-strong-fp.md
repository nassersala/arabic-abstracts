# Section 2: Strong Functional Programming
## القسم 2: البرمجة الوظيفية القوية

**Section:** strong-functional-programming
**Translation Quality:** 0.86
**Glossary Terms Used:** functional programming, termination, Church-Rosser, normalization, strict, lazy, type system

---

### English Version

Conventional functional programming may be called weak. What is the difference between weak and strong?

In a weak functional language if we have an expression, say

```
e :: int
```

we know that if evaluation of e terminates successfully, the result will be an integer - but evaluation of e might fail to terminate, or might result in an error condition.

In a strong functional language, if we have an expression

```
e :: int
```

we know that evaluation of e will terminate successfully with an integer result.

In strong functional programming there are no non-terminating computations, and no run-time errors.

In the semantics of weak functional programming each type T contains an extra element ⊥_T to denote errors and non-terminations.

In strong functional programming ⊥ does not exist. The data types are those of standard mathematics.

What are the advantages of strong functional programming? There are three principle ones:

1) The proof theory is much more straightforward.
2) The implementor has greater freedom of action.
3) Language design issues are greatly simplified (no strict versus non-strict).

### 2.1 Simpler Proof Theory

One of the things we say about functional programming is that it's easy to prove things, because there are no side effects. But in Miranda or Haskell - or indeed SML - the rules are not those of standard mathematics. For example if e is of type nat, we cannot assume

```
e - e = 0
```

because e might have for its value ⊥_nat.

Similarly we cannot rely on usual principle of induction for nats

```
P(0)
∀n.P(n)⇒P(n+1)
∀n.P(n)
```

without taking precautions to deal with the case n=⊥.

These problems arise, in different ways, in both strict and lazy languages.

In strong functional programming these problems go away because there is no ⊥ to worry about. We are back in the familiar world of sets.

### 2.2 Flexibility of Implementation

In strong functional programming reduction is strongly Church-Rosser. Note the distinction between

**(A) Church-Rosser Property:**
If E can be reduced in two different ways, then if they both produce normal forms, these will be the same

**(B) Strong Church-Rosser Property:**
Every reduction sequence leads to a normal form and normal forms are unique.

The ordinary Church-Rosser property gives a form of confluence, with strong Church-Rosser we have this plus strong normalisability - so we can evaluate in any order. This gives much greater freedom for implementor to choose an efficient strategy, perhaps to improve space behaviour, or to get more parallelism.

The choice of eager or lazy evaluation becomes a matter for the implementor, and cannot affect the semantics.

### 2.3 Simpler Language Design

In weak functional programming languages we have many extra design decisions to make, because of strict versus non-strict. Consider for example the & operation on bool, defined by

```
True & True = True
True & False = False
False & True = False
False & False = False
```

but there are more cases to consider:

```
⊥ & y = ?
x & ⊥ = ?
```

Considering the possible values for these (which are constrained by monotonicity) gives us a total of four different possible kinds of & namely

(i) doubly strict &
(ii) left-strict &
(iii) right-strict &
(iv) doubly non-strict (parallel) &

Should we provide them all? Only one? How shall we decide?

In strong functional programming these semantic choices go away. Only one & operation exists, and it is defined by its actions on True, False alone.

### 2.4 Disadvantages

What are the disadvantages of strong functional programming? There are two obvious ones

1) Programming language is no longer Turing complete!
2) If all programs terminate, how do we write an operating system?

Can we live with 1? We will return to this in the closing section, so let us postpone discussion for now.

The answer to 2 is that we need codata as well as data. (But unlike in weak functional programming, the two will be kept separate. We will have finite data and infinite codata, but no partial data.)

There already exists a theory of strong functional programming which has been extensively studied. This is the constructive type theory of Per Martin-Löf (of which there are several different versions). This is a very complex theory which includes:

• Dependent types (types indexed over values)
• Second order types
• An isomorphism between types and propositions, that enables programs to encode proof information.

This is a powerful and interesting theory, but it not suitable as a vehicle for first year teaching - it seems unlikely to replace PASCAL as the introductory programming language.

We need something simpler.

---

### النسخة العربية

يمكن تسمية البرمجة الوظيفية التقليدية بالضعيفة. ما الفرق بين الضعيفة والقوية؟

في لغة وظيفية ضعيفة، إذا كان لدينا تعبير، لنقل

```
e :: int
```

نعلم أنه إذا انتهى تقييم e بنجاح، ستكون النتيجة عدداً صحيحاً - لكن تقييم e قد يفشل في الإنهاء، أو قد ينتج عنه حالة خطأ.

في لغة وظيفية قوية، إذا كان لدينا تعبير

```
e :: int
```

نعلم أن تقييم e سينتهي بنجاح بنتيجة عدد صحيح.

في البرمجة الوظيفية القوية، لا توجد عمليات حسابية غير منتهية، ولا أخطاء وقت تشغيل.

في دلالات البرمجة الوظيفية الضعيفة، يحتوي كل نوع T على عنصر إضافي ⊥_T للإشارة إلى الأخطاء وعدم الإنهاء.

في البرمجة الوظيفية القوية، ⊥ غير موجود. أنواع البيانات هي تلك الخاصة بالرياضيات القياسية.

ما هي مزايا البرمجة الوظيفية القوية؟ هناك ثلاث مزايا رئيسية:

1) نظرية الإثبات أكثر وضوحاً بكثير.
2) لدى المُنفِّذ حرية أكبر في التصرف.
3) قضايا تصميم اللغة مبسطة بشكل كبير (لا يوجد صارم مقابل غير صارم).

### 2.1 نظرية إثبات أبسط

أحد الأشياء التي نقولها عن البرمجة الوظيفية هو أنه من السهل إثبات الأشياء، لأنه لا توجد آثار جانبية. لكن في Miranda أو Haskell - أو في الواقع SML - القواعد ليست تلك الخاصة بالرياضيات القياسية. على سبيل المثال، إذا كان e من النوع nat، لا يمكننا افتراض

```
e - e = 0
```

لأن e قد تكون قيمته ⊥_nat.

وبالمثل، لا يمكننا الاعتماد على المبدأ المعتاد للاستقراء للأعداد الطبيعية

```
P(0)
∀n.P(n)⇒P(n+1)
∀n.P(n)
```

دون اتخاذ احتياطات للتعامل مع الحالة n=⊥.

تنشأ هذه المشاكل، بطرق مختلفة، في كل من اللغات الصارمة والكسولة.

في البرمجة الوظيفية القوية، تختفي هذه المشاكل لأنه لا يوجد ⊥ للقلق بشأنه. نحن عدنا إلى عالم المجموعات المألوف.

### 2.2 مرونة التنفيذ

في البرمجة الوظيفية القوية، الاختزال يتمتع بخاصية Church-Rosser القوية. لاحظ الفرق بين

**(A) خاصية Church-Rosser:**
إذا كان يمكن اختزال E بطريقتين مختلفتين، فإذا أنتجتا كلتاهما أشكالاً عادية، فستكون هذه متطابقة

**(B) خاصية Church-Rosser القوية:**
كل تسلسل اختزال يؤدي إلى شكل عادي والأشكال العادية فريدة.

تعطي خاصية Church-Rosser العادية شكلاً من أشكال التقارب، مع خاصية Church-Rosser القوية لدينا هذا بالإضافة إلى قابلية التطبيع القوية - لذا يمكننا التقييم بأي ترتيب. هذا يعطي حرية أكبر بكثير للمُنفِّذ لاختيار استراتيجية فعالة، ربما لتحسين سلوك المساحة، أو للحصول على المزيد من التوازي.

يصبح اختيار التقييم المتلهف أو الكسول مسألة للمُنفِّذ، ولا يمكن أن يؤثر على الدلالات.

### 2.3 تصميم لغة أبسط

في لغات البرمجة الوظيفية الضعيفة، لدينا العديد من القرارات التصميمية الإضافية التي يجب اتخاذها، بسبب الصارم مقابل غير الصارم. خذ على سبيل المثال عملية & على bool، المعرّفة بـ

```
True & True = True
True & False = False
False & True = False
False & False = False
```

لكن هناك المزيد من الحالات التي يجب مراعاتها:

```
⊥ & y = ?
x & ⊥ = ?
```

النظر في القيم المحتملة لهذه (التي تكون مقيدة بالأحادية) يعطينا إجمالي أربعة أنواع مختلفة محتملة من & وهي

(i) & صارمة مزدوجاً
(ii) & صارمة يساراً
(iii) & صارمة يميناً
(iv) & غير صارمة مزدوجاً (متوازية)

هل يجب أن نوفرها جميعاً؟ واحدة فقط؟ كيف نقرر؟

في البرمجة الوظيفية القوية، تختفي هذه الاختيارات الدلالية. توجد عملية & واحدة فقط، وهي معرّفة بأفعالها على True و False وحدهما.

### 2.4 العيوب

ما هي عيوب البرمجة الوظيفية القوية؟ هناك عيبان واضحان

1) لغة البرمجة لم تعد مكتملة من حيث تورينج!
2) إذا كانت جميع البرامج تنتهي، كيف نكتب نظام تشغيل؟

هل يمكننا التعايش مع 1؟ سنعود إلى هذا في القسم الختامي، لذا دعونا نؤجل المناقشة الآن.

الإجابة على 2 هي أننا بحاجة إلى البيانات المشتركة بالإضافة إلى البيانات. (لكن على عكس البرمجة الوظيفية الضعيفة، سيتم فصل الاثنين. سيكون لدينا بيانات محدودة وبيانات مشتركة لانهائية، ولكن لا توجد بيانات جزئية.)

توجد بالفعل نظرية للبرمجة الوظيفية القوية تمت دراستها على نطاق واسع. هذه هي نظرية الأنواع البنائية لـ Per Martin-Löf (التي توجد منها عدة نسخ مختلفة). هذه نظرية معقدة جداً تتضمن:

• الأنواع المعتمدة (الأنواع المُفهرسة على القيم)
• الأنواع من الدرجة الثانية
• تشاكل بين الأنواع والقضايا، يمكّن البرامج من ترميز معلومات الإثبات.

هذه نظرية قوية ومثيرة للاهتمام، لكنها غير مناسبة كوسيلة للتدريس في السنة الأولى - يبدو من غير المحتمل أن تحل محل PASCAL كلغة برمجة تمهيدية.

نحتاج إلى شيء أبسط.

---

### Translation Notes

- **Key terms introduced:**
  - weak functional programming (البرمجة الوظيفية الضعيفة)
  - strong functional programming (البرمجة الوظيفية القوية)
  - bottom ⊥ (القاع - left untranslated as standard mathematical notation)
  - Church-Rosser property (خاصية Church-Rosser)
  - confluence (التقارب)
  - strong normalisability (قابلية التطبيع القوية)
  - strict vs non-strict (صارم مقابل غير صارم)
  - eager vs lazy evaluation (تقييم متلهف أو كسول)
  - dependent types (الأنواع المعتمدة)
  - constructive type theory (نظرية الأنواع البنائية)
- **Mathematical notation:** ⊥ (bottom), ∀ (for all), ⇒ (implies)
- **Citations:** [None in this section]
- **Special handling:** Code examples preserved in English, mathematical notation preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
