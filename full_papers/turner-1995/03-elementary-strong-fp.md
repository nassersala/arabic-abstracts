# Section 3: Elementary Strong Functional Programming
## القسم 3: البرمجة الوظيفية القوية الأولية

**Section:** elementary-strong-functional-programming
**Translation Quality:** 0.87
**Glossary Terms Used:** type system, data type, recursion, structural recursion, primitive recursion, well-founded, pattern matching, polymorphic types, higher-order functions

---

### English Version

What I propose is something much more modest than constructive type theory, namely an elementary discipline of strong functional programming.

Elementary here means

1) Type structure no more complicated than Hindley/Milner, or one of its simple variants. So we will have types like int→int, and polymorphic types like α→α, but nothing worse.

2) Programs and proofs will be kept separate, as in conventional programming. What we are looking for is essentially a strongly terminating subset of Miranda or Haskell (or for that matter SML, since the difference between strict and lazy goes away in a strong functional language)

First, we must be able to define data types.

```
> data day = Mon | Tue | Wed | Thur | Fri | Sat | Sun
> data nat = Zero | Suc nat
> data list a = Nil | Cons a (list a)
> data tree = Nilt | Node nat tree tree
> data array a = Array (nat->a)
```

As is usual some types - nat, list for example - will be built in, with special syntax, for convenience. So we can write e.g. 3 instead of Suc(Suc(Suc Zero)).

There are three essential restrictions.

**RULE 1) All primitive operations must be total.** This will involve some non-standard decisions - for example we will have

```
0 / 0 = 0
```

Runciman [6] gives a useful and interesting discussion of how to make natural arithmetic closed. He argues that the basic arithmetic type in a functional language should be nat and not int and I am persuaded by his arguments.

Making all basic operations total of course requires some attention at types other than nat - for example we have to decide what to do about hd[]. There are various possible solutions - making hd return an element of a disjoint union, or giving it an extra argument, which is the value to be returned on [], are the two obvious possibilities. It will require a period of experiment to find the best style.

Notice that because hd is polymorphic we cannot simply assign a conventional value to hd[], for with the abolition of ⊥ we no longer have any values of type α.

**RULE 2) Type recursion must be covariant.** That is type recursion through the left hand side of → is not permitted. For example

```
> data silly = Silly (silly->nat) ||not allowed!
```

Contravariant types like silly allow ⊥ to sneak back in, and are therefore banned.

Finally, it should be clear that we also need some restriction on recursive function definitions. Allowing unrestricted general recursion would bring back ⊥.

First note that to define functions we introduce the usual style of equational definition, using pattern matching over data types. Eg

```
> size :: tree a -> nat
> size Nilt = 0
> size (Node n x y) = n + size x + size y
```

To avoid non-termination, we must restrict ourselves to well-founded recursion. How should we do this? If we were to allow arbitrary well-founded recursion, we would have to submit a proof that each recursive call descends on some well-founded ordering, which the compiler would have to check. We might also have to supply a proof that the ordering in question really is well-founded, if it is not a standard one.

This contradicts our requirement for an elementary language, in which programs and proofs can be kept separate. We need a purely syntactic criterion, by which the compiler can enforce well-foundedness. I propose the following rule

**RULE 3) Each recursive function call must be on a syntactic subcomponent of its formal parameter** (the exact rule is slightly more elaborate, to take account of pattern matching over several arguments simultaneously - this is so as to allow "nested" structural recursion, as in Ackermann's function - the extension adds no power, because what it does can be desugared using higher order functions, but is syntactically convenient).

The classic example of what this allows is recursion of the form

```
> f :: nat->thing
> f 0 = something
> f (n+1) = ...f n...
```

except that we generalise the paradigm to multiple arguments and to syntactic descent on the constructors of any data type, not just nat.

The rule effectively restricts us to primitive recursion, which is guaranteed to terminate. But isn't primitive recursion quite weak? For example is it not the case that Ackermann's function fails to be primitive recursive? NO, that's a first order result - it does not apply to a language with higher order functions.

**IMPORTANT FACT:** we are here working in a higher order language, so what we actually have are the primitive recursive functionals of finite type, as studied by Gödel [2] in his System T.

These are known to include every recursive function whose totality can be proved in first order logic (starting from the usual axioms for the elementary data types, eg the Peano axioms for nat). So Ackermann is there, and much, much else. Indeed, we have more than system T, because we can define data structures with functional components, giving us infinitarily branching trees. Depending on the exact rules for typechecking polymorphic functions, it is possible to enlarge the set of definable functions to all those which can be proved total in second order arithmetic.

So it seems the restriction to primitive recursion does not deprive us of any functions that we need, BUT we may have to code things in an unfamiliar way - and it is an open question whether it gives us all the algorithms we need (this is a different issue, as it relates to complexity and not just computability). I have been studying various examples, and find the discipline surprisingly convenient.

**An example.**

Quicksort is not primitive recursive. However Treesort is primitive recursive (we descend on the subtrees) and for each version of Quicksort there is a Treesort which performs exactly the same comparisons and has the same complexity, so we haven't lost anything.

**Another example - fast exponentiation.**

```
> pow :: nat->nat->nat
> pow x n = 1, if n == 0
> = x * pow (x * x) (n/2), if odd n
> = pow (x * x) (n/2), otherwise
```

(An aside - note that the last guard of a guard set must be otherwise.) This definition is not primitive recursive - it descends from n to n/2. Primitive recursion on nats descends from (n+1) to n.

However, we can recode by introducing an intermediate data type [bit], (i.e. list-of-bit), and assuming a built in function that gives us access to the binary representation of a number.

```
> data bit = On | Off
> bits :: nat->[bit] ||built in
> pow x n = pow1 x (bits n)
> pow1 x Nil = 1
> pow1 x (On : y) = x * pow1 (x * x) y
> pow1 x (Off : y) = pow1 (x * x) y
```

**Summary of programming situation:**

**Expressive power** - we can write any function which can be proved total in the first order theory of the (relevant) data types. (FACT, DUE TO GÖDEL)

**Efficiency** - I find that around 80% of the algorithms we ordinarily write are already primitive recursive. Many of the others can be reexpressed as primitive recursive, with same computational complexity, by introducing an intermediate data structure. (MY CONJECTURE: with more practice we will find this is always true.)

I believe it would not be at all difficult to learn to program in this discipline, but you do have to make some changes to your programming style. More research is needed (for example Euclid's algorithm for gcd is difficult to express in a natural way).

It is worth remarking that there is a sledge-hammer approach that can be used to rewrite as primitive recursive any algorithm for which we can compute an upper bound on its complexity. We add an additional parameter, which is a natural number initialised to the complexity bound, and count down on that argument while recursing. This wins no prizes for elegance, but it is an existence proof that makes more plausible my conjecture above.

### 3.1 PROOFS

Proving things about programs written in this discipline is very straightforward.

Equational reasoning, starting from the program equations as axioms about the functions they define.

For each data type we have a principle of structural induction, which can be read off from the type definition, eg

```
> data nat = Zero | Suc nat
```

this gives us, for any property P over nat

```
P(Zero)
∀n.P(n)⇒P(Suc n)
∀n.P(n)
```

We have no ⊥ and no domain theory to worry about. We are in standard (set theoretic) mathematics.

---

### النسخة العربية

ما أقترحه هو شيء أكثر تواضعاً بكثير من نظرية الأنواع البنائية، وهو انضباط أولي للبرمجة الوظيفية القوية.

أولي هنا تعني

1) بنية الأنواع ليست أكثر تعقيداً من Hindley/Milner، أو أحد متغيراته البسيطة. لذلك سيكون لدينا أنواع مثل int→int، وأنواع متعددة الأشكال مثل α→α، ولكن لا شيء أسوأ.

2) سيتم فصل البرامج والإثباتات، كما في البرمجة التقليدية. ما نبحث عنه هو بشكل أساسي مجموعة فرعية منتهية بقوة من Miranda أو Haskell (أو SML في هذا الصدد، حيث يختفي الفرق بين الصارم والكسول في لغة وظيفية قوية)

أولاً، يجب أن نكون قادرين على تعريف أنواع البيانات.

```
> data day = Mon | Tue | Wed | Thur | Fri | Sat | Sun
> data nat = Zero | Suc nat
> data list a = Nil | Cons a (list a)
> data tree = Nilt | Node nat tree tree
> data array a = Array (nat->a)
```

كما هو معتاد، ستكون بعض الأنواع - nat و list على سبيل المثال - مدمجة، مع تركيب خاص، للراحة. لذا يمكننا كتابة 3 مثلاً بدلاً من Suc(Suc(Suc Zero)).

هناك ثلاثة قيود أساسية.

**القاعدة 1) يجب أن تكون جميع العمليات الأولية كلية.** سيتضمن هذا بعض القرارات غير القياسية - على سبيل المثال سيكون لدينا

```
0 / 0 = 0
```

يقدم Runciman [6] مناقشة مفيدة ومثيرة للاهتمام حول كيفية جعل الحساب الطبيعي مغلقاً. يجادل بأن نوع الحساب الأساسي في لغة وظيفية يجب أن يكون nat وليس int وأنا مقتنع بحججه.

جعل جميع العمليات الأساسية كلية بالطبع يتطلب بعض الاهتمام بالأنواع الأخرى غير nat - على سبيل المثال علينا أن نقرر ما يجب فعله بشأن hd[]. هناك حلول محتملة مختلفة - جعل hd ترجع عنصراً من اتحاد منفصل، أو إعطاؤها وسيطة إضافية، وهي القيمة التي سيتم إرجاعها على []، هما الإمكانيتان الواضحتان. سيتطلب الأمر فترة من التجربة للعثور على أفضل أسلوب.

لاحظ أنه بما أن hd متعددة الأشكال، لا يمكننا ببساطة تعيين قيمة تقليدية لـ hd[]، لأنه مع إلغاء ⊥ لم يعد لدينا أي قيم من النوع α.

**القاعدة 2) يجب أن يكون تكرار النوع متغايراً.** أي أن تكرار النوع من خلال الجانب الأيسر من → غير مسموح به. على سبيل المثال

```
> data silly = Silly (silly->nat) ||not allowed!
```

الأنواع المتغايرة العكسية مثل silly تسمح لـ ⊥ بالتسلل مرة أخرى، وبالتالي يتم حظرها.

أخيراً، يجب أن يكون واضحاً أننا نحتاج أيضاً إلى بعض القيود على تعريفات الدوال الترددية. السماح بتكرار عام غير مقيد سيعيد ⊥.

لاحظ أولاً أنه لتعريف الدوال نُدخل الأسلوب المعتاد للتعريف المعادلي، باستخدام مطابقة الأنماط على أنواع البيانات. على سبيل المثال

```
> size :: tree a -> nat
> size Nilt = 0
> size (Node n x y) = n + size x + size y
```

لتجنب عدم الإنهاء، يجب أن نقيد أنفسنا بالتكرار المؤسس جيداً. كيف يجب أن نفعل ذلك؟ إذا كنا سنسمح بتكرار مؤسس جيداً تعسفياً، فسيتعين علينا تقديم إثبات بأن كل استدعاء تردُّدي ينزل على بعض الترتيب المؤسس جيداً، والذي سيتعين على المترجم فحصه. قد نحتاج أيضاً إلى تقديم إثبات بأن الترتيب المعني مؤسس جيداً حقاً، إذا لم يكن قياسياً.

هذا يتناقض مع متطلباتنا للغة أولية، حيث يمكن فصل البرامج والإثباتات. نحتاج إلى معيار تركيبي بحت، يمكن للمترجم من خلاله فرض التأسيس الجيد. أقترح القاعدة التالية

**القاعدة 3) يجب أن يكون كل استدعاء دالة تردُّدية على مكون فرعي تركيبي لمعاملها الصوري** (القاعدة الدقيقة أكثر تفصيلاً قليلاً، لمراعاة مطابقة الأنماط على عدة وسيطات في وقت واحد - هذا للسماح بالتكرار البنيوي "المتداخل"، كما في دالة Ackermann - الامتداد لا يضيف قوة، لأن ما يفعله يمكن إزالة السكر منه باستخدام دوال من رتبة أعلى، ولكنه مريح تركيبياً).

المثال الكلاسيكي لما يسمح به هذا هو التكرار بالشكل

```
> f :: nat->thing
> f 0 = something
> f (n+1) = ...f n...
```

باستثناء أننا نعمم النموذج لوسيطات متعددة وللنزول التركيبي على بناة أي نوع بيانات، وليس فقط nat.

تقيدنا القاعدة فعلياً بالتكرار البدائي، والذي يضمن الإنهاء. لكن أليس التكرار البدائي ضعيفاً جداً؟ على سبيل المثال، أليس صحيحاً أن دالة Ackermann ليست بدائية تردُّدية؟ لا، هذه نتيجة من الدرجة الأولى - لا تنطبق على لغة ذات دوال من رتبة أعلى.

**حقيقة مهمة:** نحن هنا نعمل في لغة من رتبة أعلى، لذا ما لدينا فعلياً هو الدوال التردُّدية البدائية من النوع المحدود، كما درسها Gödel [2] في نظامه T.

من المعروف أن هذه تتضمن كل دالة تردُّدية يمكن إثبات كليتها في المنطق من الدرجة الأولى (بدءاً من البديهيات المعتادة لأنواع البيانات الأولية، على سبيل المثال بديهيات Peano لـ nat). لذا فإن Ackermann موجود، وأكثر من ذلك بكثير. في الواقع، لدينا أكثر من النظام T، لأنه يمكننا تعريف بنى بيانات ذات مكونات دالّية، مما يعطينا أشجاراً متفرعة لانهائياً. اعتماداً على القواعد الدقيقة لفحص الأنواع للدوال متعددة الأشكال، من الممكن توسيع مجموعة الدوال القابلة للتعريف إلى كل تلك التي يمكن إثبات كليتها في الحساب من الدرجة الثانية.

لذا يبدو أن القيد على التكرار البدائي لا يحرمنا من أي دوال نحتاجها، لكن قد يتعين علينا ترميز الأشياء بطريقة غير مألوفة - وهو سؤال مفتوح ما إذا كان يعطينا جميع الخوارزميات التي نحتاجها (هذه مسألة مختلفة، لأنها تتعلق بالتعقيد وليس فقط بالقابلية للحساب). لقد كنت أدرس أمثلة مختلفة، وأجد الانضباط مريحاً بشكل مفاجئ.

**مثال.**

الترتيب السريع ليس تردُّدياً بدائياً. ومع ذلك فإن ترتيب الشجرة تردُّدي بدائي (ننزل على الأشجار الفرعية) ولكل نسخة من الترتيب السريع توجد نسخة ترتيب شجرة تجري نفس المقارنات تماماً ولها نفس التعقيد، لذا لم نخسر شيئاً.

**مثال آخر - الرفع السريع.**

```
> pow :: nat->nat->nat
> pow x n = 1, if n == 0
> = x * pow (x * x) (n/2), if odd n
> = pow (x * x) (n/2), otherwise
```

(ملاحظة جانبية - لاحظ أن آخر حارس في مجموعة الحراس يجب أن يكون otherwise.) هذا التعريف ليس تردُّدياً بدائياً - ينزل من n إلى n/2. التكرار البدائي على nats ينزل من (n+1) إلى n.

ومع ذلك، يمكننا إعادة الترميز عن طريق إدخال نوع بيانات وسيط [bit]، (أي قائمة من البت)، وافتراض دالة مدمجة تعطينا الوصول إلى التمثيل الثنائي للعدد.

```
> data bit = On | Off
> bits :: nat->[bit] ||built in
> pow x n = pow1 x (bits n)
> pow1 x Nil = 1
> pow1 x (On : y) = x * pow1 (x * x) y
> pow1 x (Off : y) = pow1 (x * x) y
```

**ملخص وضع البرمجة:**

**القوة التعبيرية** - يمكننا كتابة أي دالة يمكن إثبات كليتها في النظرية من الدرجة الأولى لأنواع البيانات (ذات الصلة). (حقيقة، بسبب GÖDEL)

**الكفاءة** - أجد أن حوالي 80% من الخوارزميات التي نكتبها عادةً هي بالفعل تردُّدية بدائية. يمكن إعادة التعبير عن العديد من الأخرى كتردُّدية بدائية، بنفس التعقيد الحسابي، عن طريق إدخال بنية بيانات وسيطة. (تخميني: مع المزيد من الممارسة سنجد أن هذا صحيح دائماً.)

أعتقد أنه لن يكون صعباً على الإطلاق تعلم البرمجة في هذا الانضباط، لكن عليك إجراء بعض التغييرات على أسلوب البرمجة الخاص بك. هناك حاجة إلى المزيد من البحث (على سبيل المثال خوارزمية إقليدس لـ gcd يصعب التعبير عنها بطريقة طبيعية).

يجدر بالذكر أن هناك نهج مطرقة ثقيلة يمكن استخدامه لإعادة كتابة أي خوارزمية كتردُّدية بدائية يمكننا حساب حد أعلى لتعقيدها. نضيف معاملاً إضافياً، وهو عدد طبيعي يتم تهيئته لحد التعقيد، ونعد تنازلياً على تلك الوسيطة أثناء التكرار. هذا لا يفوز بأي جوائز للأناقة، لكنه إثبات وجود يجعل تخميني أعلاه أكثر معقولية.

### 3.1 الإثباتات

إثبات الأشياء حول البرامج المكتوبة في هذا الانضباط أمر بسيط جداً.

الاستدلال المعادلي، بدءاً من معادلات البرنامج كبديهيات حول الدوال التي تعرّفها.

لكل نوع بيانات لدينا مبدأ الاستقراء البنيوي، الذي يمكن قراءته من تعريف النوع، على سبيل المثال

```
> data nat = Zero | Suc nat
```

هذا يعطينا، لأي خاصية P على nat

```
P(Zero)
∀n.P(n)⇒P(Suc n)
∀n.P(n)
```

ليس لدينا ⊥ ولا نظرية النطاق للقلق بشأنها. نحن في الرياضيات القياسية (نظرية المجموعات).

---

### Translation Notes

- **Key terms introduced:**
  - elementary (أولي)
  - Hindley/Milner type system (نظام أنواع Hindley/Milner)
  - polymorphic types (أنواع متعددة الأشكال)
  - total operations (عمليات كلية)
  - covariant type recursion (تكرار النوع المتغاير)
  - contravariant (متغاير عكسي)
  - well-founded recursion (تكرار مؤسس جيداً)
  - structural recursion (تكرار بنيوي)
  - primitive recursion (تكرار بدائي)
  - primitive recursive functionals (دوال تردُّدية بدائية)
  - Gödel's System T (نظام Gödel T)
  - structural induction (استقراء بنيوي)
  - domain theory (نظرية النطاق)
- **Mathematical content:** Peano axioms, System T, first-order/second-order logic
- **Code examples:** 11 code blocks with Miranda/Haskell syntax
- **Citations:** [2] (Gödel), [6] (Runciman)
- **Special handling:** Three core rules highlighted with bold formatting

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
