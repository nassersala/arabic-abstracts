# Section 1: What is Functional Programming?
## القسم 1: ما هي البرمجة الوظيفية؟

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** functional programming, type system, strong typing, pattern matching, equational reasoning, induction, data types

---

### English Version

It is widely agreed that functional programming languages make excellent introductory teaching vehicles for the basic concepts of computing. The wide range of topics covered in this symposium is evidence for that. But what is functional programming?

Well, it is programming with functions, that much seems clear. But this really is not specific enough. The methods of denotational semantics show us how almost any programming language construction, no matter how opaque and side-effect ridden, can be construed functionally if we are willing to introduce complicated enough spaces for the functions to work on.

It is somewhat difficult to pin down with complete precision, but what we conventionally mean by functional programming involves the idea that the functions are transparent in the notation we actually write, rather than having to be teased out by some complex process of interpretation. For example if I write, in Miranda or Haskell (actually neither language has nat as a distinct type, but that's an oversight)

```
> fac :: nat->nat
> fac 0 = 1
> fac (n+1) = (n+1) * fac n
```

then the semantics I intend has that fac really is a function from natural numbers to natural numbers, not something else, such as a function from nat×store to nat×store, as I would have to say in a language with side effects, or a transformation over nat-demanding continuations, which is what I would have to say in a language with jumps as well as side effects.

Further, the equations which I have written as the definition of fac are actually true, and are everything I need to know about it. From them I can infer not only, e.g.

```
fac 3 = 6
```

but also more general properties of fac, by using induction principles and algebraic reasoning.

In a functional language things are what we say they are, not something much more complicated in disguise. This is particularly apparent in the notational style represented by such languages as Miranda [9], Haskell [4], and the functional subset of Standard ML [3]. We have

(i) **strong typing:** the domain and codomain of each function is either stated in or inferable from the program text, and there is a syntactic discipline which prevents a function from being applied to an inappropriate argument.

(ii) **functions are defined by equations** - typically involving case analysis by pattern matching - and we can do equational reasoning in a familiar algebraic way.

(iii) **expressions can be evaluated by treating the program equations as rewrite rules,** so computation is a special case of equational reasoning - and the final result will be independent of the order in which the rewrite rules are applied.

(iv) **there are simple induction rules** associated with the various (non-function) data types - and new types are introduced in a way that enables a corresponding induction principle to be readily inferred.

We can sum this up by saying that functional programming is programming with functions in a style that supports equational reasoning and proof by induction.

Those of us who have become converted are convinced that this is an excellent way to teach programming.

**THE BAD NEWS.** Unfortunately, none of the properties I have ascribed to functional languages above is actually quite true of any of our present languages. There is a pathology, connected with the possibility of run-time errors and non-terminating computations, which runs right through everything, and messes up all the details.

For a discussion of the complexities that can arise in reasoning about Miranda programs see Thompson [7]. Similar complications arise for any of the functional languages in current use, the details depending on such matters as whether the language is strict or lazy.

The thesis of this paper is as follows. Functional programming is a very good idea, but we haven't got it quite right yet. What we have been doing up to now is weak functional programming. What we should be doing is strong functional programming.

---

### النسخة العربية

من المتفق عليه على نطاق واسع أن لغات البرمجة الوظيفية تشكل وسائل تدريس تمهيدية ممتازة للمفاهيم الأساسية للحوسبة. إن النطاق الواسع من المواضيع التي يغطيها هذا الندوة دليل على ذلك. لكن ما هي البرمجة الوظيفية؟

حسناً، إنها البرمجة بالدوال، هذا يبدو واضحاً. لكن هذا في الواقع ليس محدداً بما فيه الكفاية. تُظهر لنا طرق الدلالات التعيينية كيف يمكن تفسير أي بناء في لغة برمجة تقريباً، مهما كان غامضاً ومليئاً بالآثار الجانبية، بشكل وظيفي إذا كنا مستعدين لإدخال فضاءات معقدة بما فيه الكفاية للدوال للعمل عليها.

من الصعب نوعاً ما تحديد ذلك بدقة كاملة، لكن ما نعنيه تقليدياً بالبرمجة الوظيفية يتضمن فكرة أن الدوال شفافة في الترميز الذي نكتبه فعلياً، بدلاً من الاضطرار إلى استخراجها من خلال بعض العمليات المعقدة للتفسير. على سبيل المثال، إذا كتبت في Miranda أو Haskell (في الواقع لا تحتوي أي من اللغتين على nat كنوع متميز، لكن هذا إغفال):

```
> fac :: nat->nat
> fac 0 = 1
> fac (n+1) = (n+1) * fac n
```

فإن الدلالات التي أقصدها هي أن fac حقاً دالة من الأعداد الطبيعية إلى الأعداد الطبيعية، وليست شيئاً آخر، مثل دالة من nat×store إلى nat×store، كما سأضطر إلى القول في لغة ذات آثار جانبية، أو تحويل على استمراريات تتطلب nat، وهو ما سأضطر إلى قوله في لغة ذات قفزات بالإضافة إلى آثار جانبية.

علاوة على ذلك، فإن المعادلات التي كتبتها كتعريف لـ fac صحيحة فعلاً، وهي كل ما أحتاج إلى معرفته عنها. منها يمكنني استنتاج ليس فقط، على سبيل المثال:

```
fac 3 = 6
```

بل أيضاً خصائص أكثر عمومية لـ fac، باستخدام مبادئ الاستقراء والاستدلال الجبري.

في لغة وظيفية، الأشياء هي ما نقول إنها عليه، وليست شيئاً أكثر تعقيداً بكثير متنكراً. هذا واضح بشكل خاص في أسلوب الترميز الذي تمثله لغات مثل Miranda [9] و Haskell [4] والجزء الوظيفي من Standard ML [3]. لدينا:

(i) **كتابة قوية:** نطاق ونطاق مشترك لكل دالة إما مذكور في نص البرنامج أو يمكن استنتاجه منه، وهناك انضباط تركيبي يمنع تطبيق دالة على وسيطة غير مناسبة.

(ii) **الدوال معرّفة بمعادلات** - تتضمن عادةً تحليل الحالات عن طريق مطابقة الأنماط - ويمكننا إجراء استدلال معادلي بطريقة جبرية مألوفة.

(iii) **يمكن تقييم التعبيرات عن طريق معاملة معادلات البرنامج كقواعد إعادة كتابة،** لذا فإن الحوسبة حالة خاصة من الاستدلال المعادلي - والنتيجة النهائية ستكون مستقلة عن الترتيب الذي تُطبق به قواعد إعادة الكتابة.

(iv) **هناك قواعد استقراء بسيطة** مرتبطة بأنواع البيانات المختلفة (غير الدالّية) - ويتم إدخال الأنواع الجديدة بطريقة تمكن من استنتاج مبدأ استقراء مطابق بسهولة.

يمكننا تلخيص ذلك بالقول إن البرمجة الوظيفية هي البرمجة بالدوال بأسلوب يدعم الاستدلال المعادلي والإثبات بالاستقراء.

أولئك منا الذين تحولوا إلى هذا النهج مقتنعون بأن هذه طريقة ممتازة لتدريس البرمجة.

**الأخبار السيئة.** لسوء الحظ، لا يوجد أي من الخصائص التي نسبتها للغات الوظيفية أعلاه صحيح تماماً في أي من لغاتنا الحالية. هناك خلل مرضي، مرتبط بإمكانية حدوث أخطاء وقت التشغيل والعمليات الحسابية غير المنتهية، يتخلل كل شيء، ويخلط جميع التفاصيل.

للاطلاع على مناقشة التعقيدات التي يمكن أن تنشأ في الاستدلال حول برامج Miranda، انظر Thompson [7]. تنشأ تعقيدات مماثلة لأي من لغات البرمجة الوظيفية المستخدمة حالياً، حيث تعتمد التفاصيل على أمور مثل ما إذا كانت اللغة صارمة أو كسولة.

أطروحة هذه الورقة هي كما يلي. البرمجة الوظيفية فكرة جيدة جداً، لكننا لم نطبقها بشكل صحيح تماماً بعد. ما كنا نفعله حتى الآن هو البرمجة الوظيفية الضعيفة. ما يجب أن نفعله هو البرمجة الوظيفية القوية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - strong typing (كتابة قوية)
  - pattern matching (مطابقة الأنماط)
  - equational reasoning (استدلال معادلي)
  - rewrite rules (قواعد إعادة كتابة)
  - denotational semantics (الدلالات التعيينية)
  - side effects (آثار جانبية)
  - continuations (استمراريات)
  - strict vs lazy (صارمة أو كسولة)
- **Equations:** 2 code examples
- **Citations:** [3], [4], [7], [9]
- **Special handling:** Code blocks preserved in English with Miranda/Haskell syntax

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
