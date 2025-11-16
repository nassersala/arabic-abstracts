# Section 5: Applications
## القسم 5: التطبيقات

**Section:** Applications
**Translation Quality:** 0.88
**Glossary Terms Used:** search problems, choice rules, constraints, CDCL, graph coloring, mixed integer problems, functional modelling

---

### English Version

#### 5.1 Multiple interpretations for one variable

Directly translating PCF gives us little more than a traditional interpreter of PCF would do, but based on this translation we can provide extra functionality, leveraging the existing ASP solvers. Traditional PCF does not support the possibility that the interpretation of a term is not uniquely defined, but we can extend PCF so we can declare the variable $a$ as a number between 1 and 10 without defining its specific value. In that case we can get (at most) 10 different evaluations of our program, one for each interpretation of $a$. It is easy to extend the translation to encode this in ASP.

Traditional interpreters solve the question: "What is the evaluation of this program?". But using these variables another question can be interesting: what value(s) for $a$ should I choose so that the program evaluates to 0. We can leverage the strengths of ASP solvers to find the solutions. Expressing that the evaluation should be zero can be done through a simple ASP constraint:
```
:- not result(0).
```

When this constraint is added, the resulting answer sets will now all have the same interpretation (0) for the result predicate, but we are interested in the interpretation for $a$.

**Example 11.** In Listing 4 you can see a PCF expression representing that $a + b = c$. If we now use choice rules in ASP to translate these variables to the domain of natural numbers between 0 and 10, we can use ASP to find multiple solutions of this equation. An example of how this would look in ASP can be seen in Listing 5.

**Listing 4:** $a + b = c$ in PCF

```
(λeq. λplus.
  eq (plus a b) c)
(fix (λeq. λx. λy. ifz x then (ifz y then 0 else 1)
                    else (ifz y then 1 else eq (pred x) (pred y))))
(fix (λplus. λx. λy. ifz y then x else plus (succ x) (pred y)))
```

**Listing 5:** $a + b = c$ in ASP

```
1  1{ a(X) }1 :- X = 1..10.
2  1{ b(X) }1 :- X = 1..10.
3  1{ c(X) }1 :- X = 1..10.
4  :- not result(0).
5  ...
6  domain(X1, A) :- domain((l0, ()), X0), domain((l1, (X0)), X1), a(A).
7  ...
```

The problem in Example 11 can easily be generalised to arbitrarily complex polynomials to model mixed integer problems. A graph coloring problem can be represented by using a new constant for each node that needs to be colored and writing down an expression that evaluated to 0 if the graph is colored correctly.

An important thing to note here is that ASP does not naively calculate the result for all possible values of the choice rules. It uses a CDCL-based solving algorithm to explore the search space in an intelligent way.

#### 5.2 Towards a more expressive language

PCF is not intended to be an end-user language, but it serves as a basis for many real world programming languages. Analogously, we are developing a more expressive language based on the principles of PCF. This language includes more complex data types for representations which are more elegant than possible in PCF. Together with the multiple-model semantics of ASP this leads to an interesting modelling language. Using these ideas the new Functional Modelling System (FMS) is being developed. On the website https://dtai.cs.kuleuven.be/krr/fms a demonstration of this new system can be found. This system is an extension of PCF with some more practical language constructs and uses the translation principles described in this paper to use ASP as a solver engine for this new language. However as indicated in Section 4.5, a lot of optimisations are needed to be competitive with native ASP encodings. The efficiency of these translators have not been formally investigated yet.

---

### النسخة العربية

#### 5.1 تفسيرات متعددة لمتغير واحد

ترجمة PCF مباشرة تعطينا أكثر قليلاً مما سيفعله مفسر تقليدي لـ PCF، لكن بناءً على هذه الترجمة يمكننا توفير وظائف إضافية، بالاستفادة من محللات ASP الموجودة. PCF التقليدي لا يدعم إمكانية أن تفسير حد غير معرّف بشكل فريد، لكن يمكننا توسيع PCF بحيث يمكننا تعريف المتغير $a$ كرقم بين 1 و 10 دون تحديد قيمته المحددة. في هذه الحالة يمكننا الحصول على (على الأكثر) 10 تقييمات مختلفة لبرنامجنا، واحد لكل تفسير لـ $a$. من السهل توسيع الترجمة لترميز هذا في ASP.

المفسرون التقليديون يحلون السؤال: "ما هو تقييم هذا البرنامج؟". لكن باستخدام هذه المتغيرات يمكن أن يكون سؤال آخر مثيراً للاهتمام: ما القيمة (القيم) لـ $a$ التي يجب أن أختارها بحيث يُقيّم البرنامج إلى 0. يمكننا الاستفادة من نقاط قوة محللات ASP لإيجاد الحلول. التعبير عن أن التقييم يجب أن يكون صفراً يمكن أن يتم من خلال قيد ASP بسيط:
```
:- not result(0).
```

عندما يُضاف هذا القيد، ستكون لمجموعات الإجابات الناتجة الآن جميعها نفس التفسير (0) لمحمول النتيجة، لكننا مهتمون بالتفسير لـ $a$.

**مثال 11.** في القائمة 4 يمكنك رؤية تعبير PCF يمثل أن $a + b = c$. إذا استخدمنا الآن قواعد الاختيار في ASP لترجمة هذه المتغيرات إلى نطاق الأعداد الطبيعية بين 0 و 10، يمكننا استخدام ASP لإيجاد حلول متعددة لهذه المعادلة. مثال على كيف سيبدو هذا في ASP يمكن رؤيته في القائمة 5.

**القائمة 4:** $a + b = c$ في PCF

```
(λeq. λplus.
  eq (plus a b) c)
(fix (λeq. λx. λy. ifz x then (ifz y then 0 else 1)
                    else (ifz y then 1 else eq (pred x) (pred y))))
(fix (λplus. λx. λy. ifz y then x else plus (succ x) (pred y)))
```

**القائمة 5:** $a + b = c$ في ASP

```
1  1{ a(X) }1 :- X = 1..10.
2  1{ b(X) }1 :- X = 1..10.
3  1{ c(X) }1 :- X = 1..10.
4  :- not result(0).
5  ...
6  domain(X1, A) :- domain((l0, ()), X0), domain((l1, (X0)), X1), a(A).
7  ...
```

المشكلة في المثال 11 يمكن تعميمها بسهولة إلى متعددات حدود معقدة بشكل تعسفي لنمذجة مشاكل الأعداد الصحيحة المختلطة. يمكن تمثيل مشكلة تلوين الرسوم البيانية باستخدام ثابت جديد لكل عقدة تحتاج إلى التلوين وكتابة تعبير يُقيّم إلى 0 إذا تم تلوين الرسم البياني بشكل صحيح.

شيء مهم يجب ملاحظته هنا هو أن ASP لا يحسب بشكل ساذج النتيجة لجميع القيم الممكنة لقواعد الاختيار. يستخدم خوارزمية حل قائمة على CDCL لاستكشاف فضاء البحث بطريقة ذكية.

#### 5.2 نحو لغة أكثر تعبيراً

PCF ليس مقصوداً أن يكون لغة للمستخدم النهائي، لكنه يخدم كأساس للعديد من لغات البرمجة في العالم الحقيقي. بالمثل، نحن نطور لغة أكثر تعبيراً بناءً على مبادئ PCF. تتضمن هذه اللغة أنواع بيانات أكثر تعقيداً لتمثيلات أكثر أناقة مما هو ممكن في PCF. مع دلالات النماذج المتعددة لـ ASP، يؤدي هذا إلى لغة نمذجة مثيرة للاهتمام. باستخدام هذه الأفكار يتم تطوير نظام النمذجة الوظيفي الجديد (FMS). على الموقع https://dtai.cs.kuleuven.be/krr/fms يمكن العثور على عرض توضيحي لهذا النظام الجديد. هذا النظام هو امتداد لـ PCF مع بعض البنيات اللغوية الأكثر عملية ويستخدم مبادئ الترجمة الموصوفة في هذا البحث لاستخدام ASP كمحرك محلل لهذه اللغة الجديدة. ومع ذلك كما هو مشار إليه في القسم 4.5، هناك حاجة إلى الكثير من التحسينات لتكون منافسة مع ترميزات ASP الأصلية. كفاءة هذه المترجمات لم يتم التحقيق فيها بشكل رسمي بعد.

---

### Translation Notes

- **Figures referenced:** Listing 4, Listing 5 (code examples)
- **Key terms introduced:**
  - multiple interpretations - تفسيرات متعددة
  - choice rules - قواعد الاختيار
  - mixed integer problems - مشاكل الأعداد الصحيحة المختلطة
  - graph coloring - تلوين الرسوم البيانية
  - CDCL (Conflict-Driven Clause Learning) - CDCL (kept as is)
  - search space - فضاء البحث
  - Functional Modelling System (FMS) - نظام النمذجة الوظيفي
  - multiple-model semantics - دلالات النماذج المتعددة
  - solver engine - محرك محلل
- **Equations:** Examples showing $a + b = c$
- **Citations:** None in this section
- **Special handling:**
  - Code listings with both PCF and ASP versions preserved
  - URL preserved in original form
  - Cross-references to Section 4.5 maintained

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Validation

Key paragraph: "Directly translating PCF gives us little more than what a traditional PCF interpreter would do, but based on this translation we can provide additional functionality, by leveraging existing ASP solvers. Traditional PCF does not support the possibility that the interpretation of a term is not uniquely defined, but we can extend PCF so we can define variable $a$ as a number between 1 and 10 without specifying its specific value. In this case we can get (at most) 10 different evaluations of our program, one for each interpretation of $a$. It is easy to extend the translation to encode this in ASP."

The back-translation accurately preserves the technical meaning and practical applications described.
