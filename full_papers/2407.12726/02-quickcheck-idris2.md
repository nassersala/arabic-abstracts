# Section 2: QuickCheck in Idris2
## القسم 2: QuickCheck في Idris2

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** property-based testing, monad, generator, dependent types, type checker, interface, pseudorandom number generator

---

### English Version

QuickCheck is a Property Based Testing tool introduced by Claessen and Hughes in 2000 [19]. Although initially written for Haskell, it has been successfully ported to many programming languages including Isabelle [6], Erlang [20], Coq [27], and Java [36].

We can use our QuickCheck implementation at the type level, since types in Idris2 are first class. Thus the test suite can be run at compile-time, acting on the implementation itself — rather than a test environment — and then being erased for the compiled program.

## 2.1 Regular QuickCheck in Idris2

Most of QuickCheck ports directly to Idris2 from the original Haskell implementation, with some minor modifications. We start with the type for specifying generators of types:

```idris
data Gen : Type -> Type where
  MkGen : (Int -> PRNGState -> a) -> Gen a
```

Idris2 has no newtype so we have to wrap it in a regular datatype; the implementation is otherwise identical. The PRNGState type represents the state type of a Pseudorandom Number Generator (PRNG), which is essential for allowing QuickCheck to generate example instances. As in Haskell, Gen is an instance of the Monad interface. It requires passing two independent PRNGs [19], which is easily achieved if the provided PRNG is splittable — that two seemingly independent PRNGs may be derived from an initial one [15].

```idris
(>>=) (MkGen g1) c = MkGen (\ n, r0 =>
  let (r1, r2) = split r0
      (MkGen g2) = c (g1 n r1)
  in g2 n r2)
```

Statistically sound splits are challenging to achieve and have been the source of bugs in the Haskell implementation [21]. Schaatun [38] concluded that amongst many existing allegedly splittable PRNGs, only the one presented by Claessen and Pałka [21] was sound. As such, we do not make any cryptographic promises about the PRNG used in our implementation: we use a Linear Congruence Generator for its ease of implementation, using known good multipliers [39]. This is sufficient for demonstrating our approach.

Another difference between Idris2 and Haskell is that (->) is a binder, and defining interface instances over binders is not allowed in Idris2. Therefore, we manually wrap functions in a data type alongside an eliminator:

```idris
data Fn : Type -> Type -> Type where
  MkFn : (f : a -> b) -> Fn a b

apply : Fn a b -> a -> b
apply (MkFn f) = f
```

We can now implement promoting functions of type `a -> Gen b` to a generator of functions from a to b, as well as implement the Arbitrary interface — which indicates that we can generate arbitrary instances of a given type — for functions, provided we know how to (1) modify a generator given some specific instance of the domain's type, and (2) generate arbitrary instances of the codomain's type:

```idris
promote : (a -> Gen b) -> Gen (Fn a b)
promote f = MkGen (\ n, r => MkFn
  (\x => let (MkGen gb) = f x in gb n r))

Arbitrary a => Arbitrary b =>
  Arbitrary (Fn a b) where
    arbitrary = promote (`coarbitrary` arbitrary)
    coarbitrary fn gen = arbitrary >>=
      ((`coarbitrary` gen) . (apply fn))
```

## 2.2 QuickCheck with Dependent Types

Using QuickCheck with dependent types presents new challenges. Consider, for example, the Vect datatype: lists which carry their length in the type. QuickCheck's bread and butter is generators and the Arbitrary interface. Provided we know how to generate the type of the elements, we should be able to generate a vector of them. However, the following definition fails:

```idris
Arbitrary t => Arbitrary (Vect n t) where
  arbitrary = do
    arbN <- arbitrary
    v <- genN arbN arbitrary
    pure v
  where
    genN : (n : Nat) -> Gen t -> Gen (Vect n t)
    genN Z _ = []
    genN (S k) g = do
      x <- g
      xs <- genN k g
      pure (x :: xs)
```

The type checker has no way of unifying n with arbN since n is implicitly generalised and bound outwith the context of the interface. We are telling the type checker that arbN should exactly match some external n which nobody has thought of yet; understandably, this fails to type check. One solution is to write Arbitrary instances only for the sizes of vectors we are interested in:

```idris
Arbitrary t => Arbitrary (Vect 3 t) where
  arbitrary = do
    v0 <- arbitrary
    v1 <- arbitrary
    v2 <- arbitrary
    pure [v0, v1, v2]
```

However, this is not very useful: we need an implementation for every length, and should we want to generate an arbitrary length we would have to reduce our arbitrary length to only the lengths which we have defined generators for, defeating the point of Arbitrary interface. Instead, we can use dependent pairs, where the second element's type depends on the value of the first, written using (**). This allows us to indicate to the type checker that although we may not know the exact length of the vector at type checking time, when we know the length, we also know it is related to a concrete instance of Vect:

```idris
someVect : (n : Nat ** Vect n Nat)
someVect = (3 ** [1, 2, 3])
```

Idris2 has failing blocks which compile if and only if they contain a term raising an error. Passing in a string requires it to be part of the error message, with the compiler rejecting the block if it fails with a different message. We can thus confirm it is an error to provide a mismatching length and Vect:

```idris
failing "Mismatch between: 1 and 0."
  sizeMismatch : (n : Nat ** Vect n Nat)
  sizeMismatch = (0 ** [3])
```

And we can ask Idris2 to infer the first element's value:

```idris
inferLength : (n : Nat ** Vect n Nat)
inferLength = (_ ** [1, 2, 3])
```

Dependent pairs allow us to define a general Arbitrary instance for Vect:

```idris
Arbitrary t => Arbitrary (n : Nat ** Vect n t) where
  arbitrary = do
    nElems <- arbitrary
    vect <- genN nElems
    pure (_ ** vect)
  where
    genN : Arbitrary a => (m : Nat) -> Gen (Vect m a)
    genN Z = pure []
    genN (S k) = do
      x <- arbitrary
      xs <- genN k
      pure (x :: xs)
```

---

### النسخة العربية

QuickCheck هي أداة اختبار قائمة على الخصائص قدمها Claessen و Hughes في عام 2000 [19]. على الرغم من أنها كتبت في البداية لـ Haskell، فقد تم نقلها بنجاح إلى العديد من لغات البرمجة بما في ذلك Isabelle [6]، و Erlang [20]، و Coq [27]، و Java [36].

يمكننا استخدام تطبيق QuickCheck الخاص بنا على مستوى الأنواع، حيث أن الأنواع في Idris2 هي من الدرجة الأولى. وبالتالي يمكن تشغيل مجموعة الاختبار في وقت الترجمة، بالعمل على التطبيق نفسه — بدلاً من بيئة الاختبار — ومن ثم محوها للبرنامج المُترجم.

## 2.1 QuickCheck العادي في Idris2

معظم QuickCheck ينقل مباشرة إلى Idris2 من تطبيق Haskell الأصلي، مع بعض التعديلات الطفيفة. نبدأ بالنوع لتحديد مولدات الأنواع:

```idris
data Gen : Type -> Type where
  MkGen : (Int -> PRNGState -> a) -> Gen a
```

ليس لدى Idris2 newtype لذا يتعين علينا لفه في نوع بيانات عادي؛ التطبيق متطابق خلاف ذلك. يمثل النوع PRNGState نوع حالة مولد الأرقام الشبه عشوائية (PRNG)، وهو ضروري للسماح لـ QuickCheck بتوليد حالات مثالية. كما في Haskell، Gen هو مثيل لواجهة Monad. يتطلب تمرير اثنين من PRNGs مستقلة [19]، وهو ما يتم تحقيقه بسهولة إذا كان PRNG المقدم قابلاً للتقسيم — أي أنه يمكن اشتقاق اثنين من PRNGs مستقلة ظاهرياً من PRNG أولي واحد [15].

```idris
(>>=) (MkGen g1) c = MkGen (\ n, r0 =>
  let (r1, r2) = split r0
      (MkGen g2) = c (g1 n r1)
  in g2 n r2)
```

التقسيمات السليمة إحصائياً تشكل تحدياً وكانت مصدر أخطاء في تطبيق Haskell [21]. خلص Schaatun [38] إلى أنه من بين العديد من PRNGs القابلة للتقسيم المزعومة، فقط تلك التي قدمها Claessen و Pałka [21] كانت سليمة. على هذا النحو، لا نقدم أي وعود تشفيرية حول PRNG المستخدم في تطبيقنا: نستخدم مولد تطابق خطي لسهولة تطبيقه، باستخدام مضاعفات جيدة معروفة [39]. هذا كافٍ لإظهار نهجنا.

الفرق الآخر بين Idris2 و Haskell هو أن (->) هو رابط، ولا يُسمح بتعريف مثيلات الواجهة على الروابط في Idris2. لذلك، نقوم يدوياً بلف الدوال في نوع بيانات جنباً إلى جنب مع مُلغٍ:

```idris
data Fn : Type -> Type -> Type where
  MkFn : (f : a -> b) -> Fn a b

apply : Fn a b -> a -> b
apply (MkFn f) = f
```

يمكننا الآن تطبيق ترقية الدوال من النوع `a -> Gen b` إلى مولد دوال من a إلى b، بالإضافة إلى تطبيق واجهة Arbitrary — التي تشير إلى أننا يمكننا توليد حالات تعسفية لنوع معين — للدوال، بشرط أن نعرف كيفية (1) تعديل مولد معطى حالة معينة من نوع المجال، و (2) توليد حالات تعسفية من نوع المجال المقابل:

```idris
promote : (a -> Gen b) -> Gen (Fn a b)
promote f = MkGen (\ n, r => MkFn
  (\x => let (MkGen gb) = f x in gb n r))

Arbitrary a => Arbitrary b =>
  Arbitrary (Fn a b) where
    arbitrary = promote (`coarbitrary` arbitrary)
    coarbitrary fn gen = arbitrary >>=
      ((`coarbitrary` gen) . (apply fn))
```

## 2.2 QuickCheck مع الأنواع التابعة

استخدام QuickCheck مع الأنواع التابعة يطرح تحديات جديدة. لنأخذ على سبيل المثال نوع البيانات Vect: قوائم تحمل طولها في النوع. خبز QuickCheck وزبدته هي المولدات وواجهة Arbitrary. بشرط أن نعرف كيفية توليد نوع العناصر، يجب أن نكون قادرين على توليد متجه منها. ومع ذلك، يفشل التعريف التالي:

```idris
Arbitrary t => Arbitrary (Vect n t) where
  arbitrary = do
    arbN <- arbitrary
    v <- genN arbN arbitrary
    pure v
  where
    genN : (n : Nat) -> Gen t -> Gen (Vect n t)
    genN Z _ = []
    genN (S k) g = do
      x <- g
      xs <- genN k g
      pure (x :: xs)
```

ليس لدى مدقق الأنواع طريقة لتوحيد n مع arbN حيث أن n معمم ضمنياً ومرتبط خارج سياق الواجهة. نحن نخبر مدقق الأنواع أن arbN يجب أن تتطابق تماماً مع n خارجي لم يفكر فيه أحد بعد؛ من المفهوم أن هذا يفشل في فحص الأنواع. أحد الحلول هو كتابة مثيلات Arbitrary فقط لأحجام المتجهات التي نهتم بها:

```idris
Arbitrary t => Arbitrary (Vect 3 t) where
  arbitrary = do
    v0 <- arbitrary
    v1 <- arbitrary
    v2 <- arbitrary
    pure [v0, v1, v2]
```

ومع ذلك، هذا ليس مفيداً جداً: نحتاج إلى تطبيق لكل طول، وإذا أردنا توليد طول تعسفي، سيتعين علينا تقليل طولنا التعسفي إلى الأطوال التي حددنا لها مولدات فقط، مما يهزم الغرض من واجهة Arbitrary. بدلاً من ذلك، يمكننا استخدام الأزواج التابعة، حيث يعتمد نوع العنصر الثاني على قيمة الأول، مكتوب باستخدام (**). هذا يسمح لنا بالإشارة إلى مدقق الأنواع أنه على الرغم من أننا قد لا نعرف الطول الدقيق للمتجه في وقت فحص الأنواع، عندما نعرف الطول، نعلم أيضاً أنه مرتبط بمثيل ملموس من Vect:

```idris
someVect : (n : Nat ** Vect n Nat)
someVect = (3 ** [1, 2, 3])
```

يحتوي Idris2 على كتل فشل تترجم إذا وفقط إذا كانت تحتوي على حد يثير خطأ. تمرير سلسلة نصية يتطلب أن تكون جزءاً من رسالة الخطأ، مع رفض المترجم للكتلة إذا فشلت برسالة مختلفة. يمكننا بالتالي تأكيد أنه خطأ تقديم طول وVect غير متطابقين:

```idris
failing "Mismatch between: 1 and 0."
  sizeMismatch : (n : Nat ** Vect n Nat)
  sizeMismatch = (0 ** [3])
```

ويمكننا أن نطلب من Idris2 استنتاج قيمة العنصر الأول:

```idris
inferLength : (n : Nat ** Vect n Nat)
inferLength = (_ ** [1, 2, 3])
```

تسمح لنا الأزواج التابعة بتعريف مثيل Arbitrary عام لـ Vect:

```idris
Arbitrary t => Arbitrary (n : Nat ** Vect n t) where
  arbitrary = do
    nElems <- arbitrary
    vect <- genN nElems
    pure (_ ** vect)
  where
    genN : Arbitrary a => (m : Nat) -> Gen (Vect m a)
    genN Z = pure []
    genN (S k) = do
      x <- arbitrary
      xs <- genN k
      pure (x :: xs)
```

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - First class types - أنواع من الدرجة الأولى
  - Compile-time - وقت الترجمة
  - Generator - مولد
  - Pseudorandom Number Generator (PRNG) - مولد الأرقام الشبه عشوائية
  - Monad interface - واجهة Monad
  - Splittable - قابل للتقسيم
  - Linear Congruence Generator - مولد تطابق خطي
  - Arbitrary interface - واجهة Arbitrary
  - Dependent pairs - أزواج تابعة
  - Type unification - توحيد الأنواع
  - Failing blocks - كتل فشل

- **Equations:** None
- **Code blocks:** 11 Idris2 code examples (kept in original form)
- **Citations:** [6,15,19,20,21,27,36,38,39]
- **Special handling:** All code kept in English; technical terms explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
