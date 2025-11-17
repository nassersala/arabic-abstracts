# Section 4: CODATA
## القسم 4: البيانات المشتركة

**Section:** codata
**Translation Quality:** 0.86
**Glossary Terms Used:** codata, data type, recursion, corecursion, infinite, finite, induction, coinduction, bisimilarity

---

### English Version

What we have sketched so far would make a nice teaching language but is not enough for production programming. Let us return to the issue of writing an operating system.

An operating system can be considered as a function from a stream of requests to a stream of responses. To program things like this functionally we need infinite lists - or something equivalent to infinite lists.

In making everything well-founded and terminating we have seemingly removed the possibility of defining infinite data structures. To get them back we introduce codata type definitions:

```
> codata colist a = Conil | a <> colist a
```

Codata definitions are equations over types that produce final algebras, instead of the initial algebras we get for data definitions. So the type colist contains all the infinite lists as well as finite ones - to get the infinite ones alone we would omit the Conil alternative. Note that infix <> is the coconstructor for colists.

The rule for coprimitive corecursion on codata is the dual to that for primitive recursion on data. Instead of descending on the argument, we ascend on the result. Like this

```
> f :: something->colist nat ||example
> f args = RHS (f args')
```

where the leading operator of RHS must be a coconstructor. There is no constraint on the form of args'.

Notice that corecursion creates (potentially infinite) codata, whereas ordinary recursion analyses (necessarily finite) data. Ordinary recursion is not legal over codata, because it might not terminate. Conversely corecursion is not legal if the result type is data, because data must be finite.

Now we can define infinite structures, such as

```
> ones :: colist nat
> ones = 1 <> ones
> fibs :: colist nat
> fibs = f 0 1
> where
> f a b = a <> f b (a+b)
```

and many other examples which every Miranda or Haskell programmer knows and loves.

**NOTE THAT ALL OUR INFINITE STRUCTURES ARE TOTAL**

As in the case of primitive recursion over data, the rule for coprimitive corecursion over codata requires us to rewrite some of our algorithms, to adhere to the discipline of strong functional programming. This is sometimes quite hard - for example rewriting the well known sieve of Eratosthenes program in this discipline involves coding in some bound on the distance from one prime to the next.

There is a (very nice) principle of coinduction, which we use to prove infinite structures equal. It can be read off from the definition of the codata type. We discuss this in the next subsection.

A question. Does the introduction of codata destroy the strong Church-Rosser property? No! (But you have to have the right definition of normal form. Every expression whose principle operator is a coconstructor is in normal form.)

### 4.1 Coinduction

First we give the definition of bisimilarity (on colists). We can characterise ≈ the bisimilarity relation as follows

```
x≈y⇒hd x = hd y ∧ tl x≈tl y
```

Actually this is itself a corecursive definition! To avoid a meaningless regress what one actually says is that anything obeying the above is a bisimulation and by bisimilarity we mean the largest such relation. For a fuller discussion see Pitts [5]. Taking as read this background understanding of how to avoid logical regress, we say that in general two pieces of codata are bisimilar if:

• their finite parts are equal, and
• their infinite parts are bisimilar.

The principle of coinduction may now be stated as follows: **Bisimilar objects are equal.**

One way to understand this principle is to take it as the definition of equality on infinite objects

We can package the definition of bisimilarity and the principle that bisimilar objects are equal in the following method of proof: When proving the equality of two infinite structures we may assume the equality of recursive substructures of the same form.

For colists we get — to prove

```
g x1 ... xn = h x1 ... xn
```

It is sufficient to show

```
g x1 ... xn = e <> g a1 ... an
h x1 ... xn = e <> h a1 ... an
```

There is a similar rule for each codata type

**A trivial example**

```
> x = 1 <> x
> y = 1 <> y
```

How do we prove that x = y?

Theorem x = y

Proof by coinduction
```
x
= 1 <> x {x}
= 1 <> y {ex hypothesi}
= y {y}
```
QED

**Example: reflection on infinite trees**

```
> codata inftree = T nat inftree inftree
> refl :: inftree -> inftree
> refl (T a x y) = T a (refl y)(refl x)
```

Theorem refl (refl x) = x

Proof by coinduction
```
refl (refl (T a y z)
= refl (T a (refl z) (refl y)) {refl}
= T a (refl (refl y)) (refl (refl z)) {refl}
= T a y z {ex hypothesi}
```
QED

**Example: the (co)map-iterate theorem**

The following theorem is from Bird & Wadler (see [1], page 184). We have changed the name of map to comap because for us they are different functions.

```
> iterate f x = x <> iterate f (f x)
> comap f (a <> x) = f a <> comap f x
```

Theorem iterate f (f x) = comap f (iterate f x)

Proof by coinduction
```
iterate f (f x)
= f x <> iterate f (f (f x)) {iterate}
= f x <> comap f (iterate f (f x)) {ex hypothesi}
= comap f (x <> iterate f (f x)) {comap}
= comap f (iterate f x) {iterate}
```
QED

The proof given in [1] uses the take-lemma - it is longer than that given above and requires an auxiliary construction, involving the application of a take function to both sides of the equation, and an induction on the length of the take.

**Summary**

The "strong coinduction" principle illustrated here seems to give shorter proofs of equations over infinite lists than either of the proof methods for this which have been developed in the theory of weak functional programming - namely partial object induction (Turner [8]) and the take-lemma (Bird [1]).

The framework seems simpler than previous accounts of coinduction - see for example Pitts [5], because we are not working with domain theory and partial objects, but with the simpler world of total objects.

Moral: Getting rid of partial objects seems to be an unmitigated blessing - not only when reasoning about finite data, but also, perhaps even more so, in the case of infinite data.

---

### النسخة العربية

ما رسمناه حتى الآن سيجعل لغة تدريس جيدة لكنها ليست كافية للبرمجة الإنتاجية. دعونا نعود إلى مسألة كتابة نظام تشغيل.

يمكن اعتبار نظام التشغيل دالة من تدفق من الطلبات إلى تدفق من الاستجابات. لبرمجة أشياء كهذه وظيفياً، نحتاج إلى قوائم لانهائية - أو شيء معادل للقوائم اللانهائية.

في جعل كل شيء مؤسساً جيداً ومنتهياً، يبدو أننا أزلنا إمكانية تعريف بنى بيانات لانهائية. لاستعادتها نُدخل تعريفات أنواع البيانات المشتركة:

```
> codata colist a = Conil | a <> colist a
```

تعريفات البيانات المشتركة هي معادلات على الأنواع تنتج جبور نهائية، بدلاً من الجبور الأولية التي نحصل عليها لتعريفات البيانات. لذا فإن النوع colist يحتوي على جميع القوائم اللانهائية بالإضافة إلى المحدودة - للحصول على اللانهائية وحدها سنحذف بديل Conil. لاحظ أن <> اللاحقة هي البناء المشترك لـ colists.

القاعدة للتكرار المشترك البدائي على البيانات المشتركة هي الازدواج لتلك الخاصة بالتكرار البدائي على البيانات. بدلاً من النزول على الوسيطة، نصعد على النتيجة. هكذا

```
> f :: something->colist nat ||example
> f args = RHS (f args')
```

حيث يجب أن يكون المُشغّل الرئيسي لـ RHS بناءً مشتركاً. لا يوجد قيد على شكل args'.

لاحظ أن التكرار المشترك ينشئ بيانات مشتركة (لانهائية محتملاً)، بينما التكرار العادي يحلل بيانات (محدودة بالضرورة). التكرار العادي غير قانوني على البيانات المشتركة، لأنه قد لا ينتهي. وعلى العكس، فإن التكرار المشترك غير قانوني إذا كان نوع النتيجة بيانات، لأن البيانات يجب أن تكون محدودة.

الآن يمكننا تعريف بنى لانهائية، مثل

```
> ones :: colist nat
> ones = 1 <> ones
> fibs :: colist nat
> fibs = f 0 1
> where
> f a b = a <> f b (a+b)
```

والعديد من الأمثلة الأخرى التي يعرفها ويحبها كل مبرمج Miranda أو Haskell.

**لاحظ أن جميع بنانا اللانهائية كلية**

كما في حالة التكرار البدائي على البيانات، تتطلب منا القاعدة للتكرار المشترك البدائي على البيانات المشتركة إعادة كتابة بعض خوارزمياتنا، للالتزام بانضباط البرمجة الوظيفية القوية. هذا صعب أحياناً - على سبيل المثال، إعادة كتابة برنامج غربال إراتوستينس المعروف في هذا الانضباط يتضمن ترميز حد ما على المسافة من عدد أولي إلى التالي.

هناك مبدأ (جميل جداً) للاستقراء المشترك، الذي نستخدمه لإثبات تساوي البنى اللانهائية. يمكن قراءته من تعريف نوع البيانات المشتركة. نناقش هذا في القسم الفرعي التالي.

سؤال. هل إدخال البيانات المشتركة يدمر خاصية Church-Rosser القوية؟ لا! (لكن يجب أن يكون لديك التعريف الصحيح للشكل العادي. كل تعبير مُشغّله الرئيسي بناء مشترك في شكل عادي.)

### 4.1 الاستقراء المشترك

أولاً نعطي تعريف التشابه الثنائي (على colists). يمكننا توصيف ≈ علاقة التشابه الثنائي كما يلي

```
x≈y⇒hd x = hd y ∧ tl x≈tl y
```

في الواقع هذا نفسه تعريف تكرار مشترك! لتجنب التراجع غير المعنوي، ما يقال فعلاً هو أن أي شيء يطيع ما سبق هو تشابه ثنائي وبالتشابه الثنائي نعني أكبر علاقة من هذا القبيل. للحصول على مناقشة أكمل، انظر Pitts [5]. مع أخذ هذا الفهم الخلفي لكيفية تجنب التراجع المنطقي كمُسلَّم به، نقول أنه بشكل عام قطعتان من البيانات المشتركة متشابهتان ثنائياً إذا:

• أجزاؤهما المحدودة متساوية، و
• أجزاؤهما اللانهائية متشابهة ثنائياً.

يمكن الآن ذكر مبدأ الاستقراء المشترك كما يلي: **الأشياء المتشابهة ثنائياً متساوية.**

طريقة واحدة لفهم هذا المبدأ هي أخذه كتعريف للمساواة على الأشياء اللانهائية

يمكننا تجميع تعريف التشابه الثنائي ومبدأ أن الأشياء المتشابهة ثنائياً متساوية في طريقة الإثبات التالية: عند إثبات مساواة بنيتين لانهائيتين، يمكننا افتراض مساواة البنى الفرعية التردُّدية من نفس الشكل.

لـ colists نحصل على - لإثبات

```
g x1 ... xn = h x1 ... xn
```

يكفي إظهار

```
g x1 ... xn = e <> g a1 ... an
h x1 ... xn = e <> h a1 ... an
```

هناك قاعدة مماثلة لكل نوع بيانات مشتركة

**مثال تافه**

```
> x = 1 <> x
> y = 1 <> y
```

كيف نثبت أن x = y؟

نظرية x = y

إثبات بالاستقراء المشترك
```
x
= 1 <> x {x}
= 1 <> y {ex hypothesi}
= y {y}
```
انتهى الإثبات

**مثال: الانعكاس على الأشجار اللانهائية**

```
> codata inftree = T nat inftree inftree
> refl :: inftree -> inftree
> refl (T a x y) = T a (refl y)(refl x)
```

نظرية refl (refl x) = x

إثبات بالاستقراء المشترك
```
refl (refl (T a y z)
= refl (T a (refl z) (refl y)) {refl}
= T a (refl (refl y)) (refl (refl z)) {refl}
= T a y z {ex hypothesi}
```
انتهى الإثبات

**مثال: نظرية (co)map-iterate**

النظرية التالية من Bird & Wadler (انظر [1]، صفحة 184). قمنا بتغيير اسم map إلى comap لأنهما دالتان مختلفتان بالنسبة لنا.

```
> iterate f x = x <> iterate f (f x)
> comap f (a <> x) = f a <> comap f x
```

نظرية iterate f (f x) = comap f (iterate f x)

إثبات بالاستقراء المشترك
```
iterate f (f x)
= f x <> iterate f (f (f x)) {iterate}
= f x <> comap f (iterate f (f x)) {ex hypothesi}
= comap f (x <> iterate f (f x)) {comap}
= comap f (iterate f x) {iterate}
```
انتهى الإثبات

الإثبات المعطى في [1] يستخدم مبرهنة take - وهو أطول من المعطى أعلاه ويتطلب بناءً مساعداً، يتضمن تطبيق دالة take على كلا جانبي المعادلة، واستقراء على طول take.

**ملخص**

يبدو أن مبدأ "الاستقراء المشترك القوي" الموضح هنا يعطي إثباتات أقصر للمعادلات على القوائم اللانهائية من أي من طرق الإثبات لهذا التي تم تطويرها في نظرية البرمجة الوظيفية الضعيفة - وهي استقراء الأشياء الجزئية (Turner [8]) ومبرهنة take (Bird [1]).

يبدو الإطار أبسط من الحسابات السابقة للاستقراء المشترك - انظر على سبيل المثال Pitts [5]، لأننا لا نعمل مع نظرية النطاق والأشياء الجزئية، بل مع عالم الأشياء الكلية الأبسط.

الأخلاق: التخلص من الأشياء الجزئية يبدو نعمة خالصة - ليس فقط عند الاستدلال حول البيانات المحدودة، ولكن أيضاً، وربما أكثر من ذلك، في حالة البيانات اللانهائية.

---

### Translation Notes

- **Key terms introduced:**
  - codata (بيانات مشتركة)
  - colist (قائمة مشتركة)
  - coconstructor (بناء مشترك)
  - corecursion (تكرار مشترك)
  - coprimitive corecursion (تكرار مشترك بدائي)
  - final algebras (جبور نهائية)
  - initial algebras (جبور أولية)
  - coinduction (استقراء مشترك)
  - bisimilarity (تشابه ثنائي)
  - bisimulation (تشابه ثنائي)
  - infinite structures (بنى لانهائية)
  - partial objects (أشياء جزئية)
  - total objects (أشياء كلية)
  - take-lemma (مبرهنة take)
- **Mathematical content:** 3 proof examples using coinduction
- **Code examples:** 7 code blocks showing codata definitions and infinite structures
- **Citations:** [1] (Bird & Wadler), [5] (Pitts), [8] (Turner)
- **Special handling:** Proof format preserved with indentation and QED markers

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
