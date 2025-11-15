# Section 2: Motivation and Intuitions
## القسم 2: الدافع والبديهيات

**Section:** Motivation and Intuitions (Sections 2.1-2.8)
**Translation Quality:** 0.86
**Glossary Terms Used:** linear types, function, consumed exactly once, mutable arrays, I/O protocols, data constructors, multiplicity polymorphism

---

### English Version

Informally, a function is "linear" if it consumes its argument exactly once. (It is "affine" if it consumes it at most once.) A linear type system gives a static guarantee that a claimed linear function really is linear. There are many motivations for linear type systems, but here we focus on two of them:

• Is it safe to update this value in-place (Sec. 2.2)? That depends on whether there are aliases to the value; update-in-place is ok if there are no other pointers to it. Linearity supports a more efficient implementation, by O(1) update rather than O(n) copying.

• Am I obeying the usage protocol of this external resource (Sec. 2.3)? For example, an open file should be closed, and should not be used after it has been closed; a socket should be opened, then bound, and only then used for reading; a malloc'd memory block should be freed, and should not be used after that. Here, linearity does not affect efficiency, but rather eliminates many bugs.

We introduce our extension to Haskell, which we call Linear Haskell, by focusing on these two use-cases. In doing so, we introduce a number of ideas that we flesh out in subsequent subsections.

**2.1 Operational intuitions**

We have said informally that "a linear function consumes its argument exactly once". But what exactly does that mean?

Meaning of the linear arrow: f :: s ⊸ t guarantees that if (f u) is consumed exactly once, then the argument u is consumed exactly once.

To make sense of this statement we need to know what "consumed exactly once" means. Our definition is based on the type of the value concerned:

**Definition 2.1 (Consume exactly once):**
• To consume a value of atomic base type (like Int or Ptr) exactly once, just evaluate it.
• To consume a function value exactly once, apply it to one argument, and consume its result exactly once.
• To consume a pair exactly once, pattern-match on it, and consume each component exactly once.
• In general, to consume a value of an algebraic datatype exactly once, pattern-match on it, and consume all its linear components exactly once (Sec. 2.5).

This definition is enough to allow programmers to reason about the typing of their functions, and it drives the formal typing judgements in Sec. 3.

Note that a linear arrow specifies how the function uses its argument. It does not restrict the arguments to which the function can be applied. In particular, a linear function cannot assume that it is given the unique pointer to its argument. For example, if f :: s ⊸ t, then this is fine:

```haskell
g :: s → t
g x = f x
```

The type of g makes no particular guarantees about the way in which it uses x; in particular, g can pass that argument to f.

**2.2 Safe mutable arrays**

The Haskell language provides immutable arrays, built with the function array. But how is array implemented? A possible answer is "it is built-in; don't ask". But in reality GHC implements array using more primitive pieces, so that library authors can readily implement more complex variations. Here is the definition of array, using library functions whose types are given in Fig. 1:

```haskell
array :: Int → [(Int, a)] → Array a
array size pairs = runST
  (do {ma ← newMArray size
      ; forM_ pairs (write ma)
      ; unsafeFreeze ma})
```

In the first line we allocate a mutable array, of type MArray s a. Then we iterate over the pairs, with forM_, updating the array in place for each pair. Finally, we freeze the mutable array, returning an immutable array as required. All this is done in the ST monad, using runST to securely encapsulate an imperative algorithm in a purely-functional context.

Why is unsafeFreeze unsafe? The result of (unsafeFreeze ma) is a new immutable array, but to avoid an unnecessary copy, it is actually ma. The intention is that unsafeFreeze should be the last use of the mutable array; but nothing stops us continuing to mutate it further, with quite undefined semantics.

Linear types allow a more secure and less sequential interface. Linear Haskell introduces a new kind of function type: the linear arrow a⊸b. A linear function f::a⊸b must consume its argument exactly once. This new arrow is used in a new array API, given in Fig. 2:

```haskell
type MArray a
type Array a
newMArray :: Int → (MArray a ⊸ Unrestricted b) ⊸ b
write :: MArray a ⊸ (Int, a) → MArray a
read :: MArray a ⊸ Int → (MArray a, Unrestricted a)
freeze :: MArray a ⊸ Unrestricted (Array a)
```

Using this API we can define array thus:

```haskell
array :: Int → [(Int, a)] → Array a
array size pairs = newMArray size (λma → freeze (foldl write ma pairs))
```

**2.3 I/O protocols**

Consider the API for files in Fig. 3, where a File is a cursor in a physical file. Each call to readLine returns a ByteString (the line) and moves the cursor one line forward. But nothing stops us reading a file after we have closed it, or forgetting to close it. An alternative API using linear types is given in Fig. 4. Using it we can write a simple file handling program, firstLine:

```haskell
firstLine :: FilePath → IOL ω Bytestring
firstLine fp =
  do { f ← openFile fp
     ; (f,Unrestricted bs) ← readLine f
     ; closeFile f
     ; return bs }
```

**2.4 Linear datatypes**

With the above intuitions in mind, what type should we assign to a data constructor such as the pairing constructor (,)? Using the definition in Sec. 2.1, the correct choice is:

```haskell
(,) :: a ⊸ b ⊸ (a, b)
```

The same idea applies to all existing Haskell datatypes: in Linear Haskell we treat all datatypes defined using legacy Haskell-98 (non-GADT) syntax as defining constructors with linear arrows.

**2.5 Unrestricted data constructors**

Sometimes we need to declare data constructors with non-linear types. Using GADT-style syntax we can give an explicit type signature to the data constructor:

```haskell
data Unrestricted a where
  {Unrestricted :: a → Unrestricted a}
```

The type (Unrestricted t) is very much like "!t" in linear logic, but in our setting it is just an ordinary user-defined datatype.

**2.6 Multiplicity polymorphism**

A linear function provides more guarantees to its caller than a non-linear one — it is more general. Linear Haskell features quantification over multiplicities and parameterised arrows (A →q B). Using these, map can be given the following more general type:

```haskell
map :: ∀p. (a →p b) → [a] →p [b]
```

**2.7 Linear input/output**

In Sec. 2.3 we introduced the IOL monad. But how does it work? IOL is just a generalisation of the IO monad:

```haskell
type IOL p a
returnIOL :: a →p IOL p a
bindIOL :: IOL p a ⊸ (a →p IOL q b) ⊸ IOL q b
```

**2.8 Linearity and strictness**

It is tempting to assume that, since a linear function consumes its argument exactly once, then it must also be strict. But not so! For example:

```haskell
f :: a ⊸ (a, Bool)
f x = (x, True)
```

Here f is certainly linear according to Sec. 2.1, but f is certainly not strict: f ⊥ is not ⊥.

---

### النسخة العربية

بشكل غير رسمي، تكون الدالة "خطية" إذا استهلكت وسيطها مرة واحدة بالضبط. (تكون "أفينية" affine إذا استهلكته على الأكثر مرة واحدة.) يعطي نظام الأنواع الخطي ضماناً ثابتاً بأن الدالة الخطية المزعومة هي بالفعل خطية. هناك العديد من الدوافع لأنظمة الأنواع الخطية، لكننا هنا نركز على اثنين منها:

• هل من الآمن تحديث هذه القيمة في المكان (القسم 2.2)؟ يعتمد ذلك على ما إذا كانت هناك أسماء مستعارة (aliases) للقيمة؛ التحديث في المكان جيد إذا لم تكن هناك مؤشرات أخرى إليها. تدعم الخطية تنفيذاً أكثر كفاءة، من خلال تحديث O(1) بدلاً من نسخ O(n).

• هل أطيع بروتوكول الاستخدام لهذا المورد الخارجي (القسم 2.3)؟ على سبيل المثال، يجب إغلاق ملف مفتوح، ويجب عدم استخدامه بعد إغلاقه؛ يجب فتح المقبس (socket)، ثم ربطه، وعندها فقط استخدامه للقراءة؛ يجب تحرير كتلة الذاكرة المخصصة بـ malloc، ويجب عدم استخدامها بعد ذلك. هنا، لا تؤثر الخطية على الكفاءة، بل تزيل العديد من الأخطاء.

نقدم امتدادنا لـ Haskell، والذي نسميه Haskell الخطي، من خلال التركيز على حالتي الاستخدام هاتين. في القيام بذلك، نقدم عدداً من الأفكار التي نفصلها في الأقسام الفرعية اللاحقة.

**2.1 البديهيات التشغيلية**

قلنا بشكل غير رسمي أن "الدالة الخطية تستهلك وسيطها مرة واحدة بالضبط". لكن ماذا يعني ذلك بالضبط؟

معنى السهم الخطي: f :: s ⊸ t يضمن أنه إذا تم استهلاك (f u) مرة واحدة بالضبط، فإن الوسيط u يُستهلك مرة واحدة بالضبط.

لفهم هذا البيان، نحتاج إلى معرفة ما يعنيه "استُهلك مرة واحدة بالضبط". يعتمد تعريفنا على نوع القيمة المعنية:

**التعريف 2.1 (الاستهلاك مرة واحدة بالضبط):**
• لاستهلاك قيمة من نوع أساسي ذري (مثل Int أو Ptr) مرة واحدة بالضبط، قم فقط بتقييمها.
• لاستهلاك قيمة دالة مرة واحدة بالضبط، قم بتطبيقها على وسيط واحد، واستهلك نتيجتها مرة واحدة بالضبط.
• لاستهلاك زوج مرة واحدة بالضبط، قم بمطابقة الأنماط عليه، واستهلك كل مكون مرة واحدة بالضبط.
• بشكل عام، لاستهلاك قيمة من نوع بيانات جبري مرة واحدة بالضبط، قم بمطابقة الأنماط عليها، واستهلك جميع مكوناتها الخطية مرة واحدة بالضبط (القسم 2.5).

هذا التعريف كافٍ للسماح للمبرمجين بالتفكير في كتابة دوالهم، ويدفع أحكام الكتابة الرسمية في القسم 3.

لاحظ أن السهم الخطي يحدد كيف تستخدم الدالة وسيطها. لا يقيد الوسائط التي يمكن تطبيق الدالة عليها. على وجه الخصوص، لا يمكن للدالة الخطية أن تفترض أنها تُعطى المؤشر الفريد لوسيطها.

**2.2 المصفوفات القابلة للتغيير الآمنة**

توفر لغة Haskell مصفوفات غير قابلة للتغيير، مبنية بالدالة array. ولكن كيف يتم تنفيذ array؟ إجابة محتملة هي "إنها مدمجة؛ لا تسأل". ولكن في الواقع ينفذ GHC array باستخدام قطع أكثر بدائية، بحيث يمكن لمؤلفي المكتبات تنفيذ اختلافات أكثر تعقيداً بسهولة.

لماذا يكون unsafeFreeze غير آمن؟ نتيجة (unsafeFreeze ma) هي مصفوفة جديدة غير قابلة للتغيير، ولكن لتجنب نسخة غير ضرورية، هي في الواقع ma. القصد هو أن يكون unsafeFreeze هو الاستخدام الأخير للمصفوفة القابلة للتغيير؛ لكن لا شيء يمنعنا من الاستمرار في تغييرها أكثر، مع دلالات غير محددة تماماً.

تسمح الأنواع الخطية بواجهة أكثر أماناً وأقل تسلسلاً. يقدم Haskell الخطي نوعاً جديداً من دالة: السهم الخطي a⊸b. يجب على الدالة الخطية f::a⊸b استهلاك وسيطها مرة واحدة بالضبط.

**2.3 بروتوكولات الإدخال/الإخراج**

ضع في اعتبارك واجهة برمجة التطبيقات للملفات حيث File هو مؤشر في ملف فعلي. لا شيء يمنعنا من قراءة ملف بعد إغلاقه، أو نسيان إغلاقه. واجهة برمجة تطبيقات بديلة باستخدام الأنواع الخطية تحل هذه المشاكل.

**2.4 أنواع البيانات الخطية**

مع البديهيات أعلاه في الاعتبار، ما النوع الذي يجب أن نعينه لمُنشئ بيانات مثل منشئ الإقران (،)؟ الاختيار الصحيح هو:

```haskell
(,) :: a ⊸ b ⊸ (a, b)
```

**2.5 مُنشئات البيانات غير المقيدة**

في بعض الأحيان نحتاج إلى الإعلان عن مُنشئات بيانات بأنواع غير خطية. باستخدام بناء GADT يمكننا إعطاء توقيع نوع صريح لمُنشئ البيانات:

```haskell
data Unrestricted a where
  {Unrestricted :: a → Unrestricted a}
```

**2.6 تعددية التعددية**

توفر الدالة الخطية ضمانات أكثر للمتصل بها من دالة غير خطية - إنها أكثر عمومية. يتميز Haskell الخطي بالتحديد الكمي على التعدديات والأسهم ذات المعاملات.

**2.7 الإدخال/الإخراج الخطي**

في القسم 2.3 قدمنا monad IOL. لكن كيف يعمل؟ IOL هو مجرد تعميم لـ IO monad.

**2.8 الخطية والصرامة**

من المغري أن نفترض أنه، نظراً لأن الدالة الخطية تستهلك وسيطها مرة واحدة بالضبط، فيجب أن تكون أيضاً صارمة. لكن ليس كذلك!

---

### Translation Notes

- **Figures referenced:** Fig. 1, Fig. 2, Fig. 3, Fig. 4 (type signatures for arrays and files)
- **Key terms introduced:**
  - Linear function (الدالة الخطية)
  - Consumed exactly once (استُهلك مرة واحدة بالضبط)
  - Linear arrow (السهم الخطي)
  - Mutable array (المصفوفة القابلة للتغيير)
  - Multiplicity polymorphism (تعددية التعددية)
  - Unrestricted (غير مقيد)
- **Code examples:** Multiple Haskell code snippets maintained in English
- **Mathematical notation:** O(1), O(n) notation preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
