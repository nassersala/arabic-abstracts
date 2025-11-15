# Section 4: Case Study: Implementing the Hilbert-driven, F₄ and F₅ algorithms for calculating Gröbner bases
## القسم 4: دراسة حالة: تطبيق خوارزميات Hilbert-driven و F₄ و F₅ لحساب قواعد Gröbner

**Section:** case-study
**Translation Quality:** 0.86
**Glossary Terms Used:** algorithm, Gröbner basis, lazy evaluation, parallelism, composable, homogeneous, polynomial, Gaussian elimination, matrix, benchmark

---

### English Version

In this section, we will focus on three algorithms as case-studies: the Hilbert-driven, F₄ and F₅ algorithms. Firstly, we demonstrate the power of laziness and parallelism by the Hilbert-driven algorithm. Then by the F₄ interface, we illustrate the practical example of composability. Finally, we skim through the simplified version of the main routine of F₅ and see how imperative programming with mutable states can be written purely in Haskell. For our purpose, we will discuss only a fragment of implementations that elucidates the advantages of Haskell, rather than the entire implementation and theoretical details.

#### 4.1 Homogenisation and Hilbert-driven basis conversion

Homogenisation is a powerful tool in Gröbner basis computation. If I ⊆ k[X] is a non-homogeneous ideal and Ī ⊆ k[x, X] its homogenisation, then one can get a Gröbner basis for I by unhomogenising the Gröbner basis Ḡ for Ī w.r.t. a suitably induced monomial ordering. In this way, any Gröbner basis algorithm for homogeneous ideals can be converted into one for non-homogeneous ones.

**Code 6** is an API for these operations. The type `Homogenised poly` represents polynomials obtained by homogenising polynomials of type `poly`. Then `calcGBViaHomog calc i` first checks if the input `i` is homogeneous. If it is so, then it applies the argument `calc` to its input directly (Line 15); otherwise, it first homogenises the input, applies `calc`, and then unhomogenises it to get the final result (Line 16). Note that, though it uses the same term `calc` in both cases, they have different types. In the first case, since it just feeds an input directly, `calc` has type `Ideal poly → [poly]`. On the other hand, in the non-homogeneous case, it is applied after homogenisation, hence it is of type `Ideal (Homogenised poly) → [Homogenised poly]`. Thus, `calcGBViaHomog` takes a polymorphic function as its first argument and this is why we have `∀` inside the type of the first argument. Such a nested polymorphic type is called a rank n polymorphic type, and it is supported by GHC's RankNTypes language extension.

For example, one can use the so-called Hilbert-driven algorithm as the first argument to `calcGBViaHomog`. It first computes a Gröbner basis w.r.t. a lighter monomial ordering, compute the Hilbert–Poincaré series (HPS) with it and use it to compute Gröbner basis w.r.t. the heavier ordering. In this procedure, we need the following operations on HPS: Equality test on HPS's, n-th Taylor coefficient of the given HPS, and the Z[X]-module operation on HPS. **Code 7** illustrates such an interface for HPS. For equality test, we use the numerator `hpsNumerator` of the closed form, and an infinite list `taylor` maintains Taylor coefficients. By the lazy nature of Haskell, we can intuitively treat infinite lists and write a convolution on them. In Line 12, `par` and `seq` specify the evaluation strategy. In brief, expressions x and y in "x 'par' y" (resp. seq) are evaluated parallelly (resp. sequentially). Since every expression is pure in Haskell, we can safely take advantage of parallelism, without a possibility of changing results.

#### 4.2 A composable implementation of F₄

F₄ is one of the most efficient algorithms for Gröbner basis computation and introduced by Faugère [5]. Briefly, F₄ reduces more than two polynomials at once, replacing S-polynomial remaindering in the Buchberger Algorithm with the Gaussian elimination of the matrices. This means that the efficiency of F₄ reduces to that of Gaussian elimination and the internal representation of matrices. Thus, it is useful if we can easily switch internal representations and elimination algorithms. For this purpose, we provide type-classes for mutable and immutable matrices which admit row operations and a dedicated Gaussian elimination. **Code 8** demonstrates the interface for immutable and mutable matrices (`Matrix` and `MMatrix`) and the type signature of our F₄ implementation (`f4`). In Lines 1 and 6, the last type argument `a` of `Matrix` and `MMatrix` corresponds to the type of coefficients. Note that, one can give different instance definitions for the same `mat` but different coefficient types `a`. For example, one can implement efficient Gaussian elimination on F_p for `Matrix Mat F_p`, and then use it in the definition of `Matrix Mat Q`, with the Hensel lifting or Chinese remaindering.

In Line 15, the first argument of `f4` of type `proxy mat` specifies the internal representation `mat` of matrices. In addition, `f4` takes a selection strategy as the second argument. Here, the selection strategy is abstracted as a weighting function to some ordered types, and we store intermediate polynomials in a heap and select all the polynomials with the minimum weight at each iteration.

#### 4.3 The F₅ algorithm

Finally, we present the simplified version of the main routine of Faugère's F₅ [6] (**Code 9**). Readers may be surprised that the code looks much imperative. This is made possible by the ST monad [19], which encapsulates side-effects introduced by mutable states and prevents them from leaking outside. We use a functional heap to choose the polynomial vectors with the least signature, demonstrating the fusion of functional and imperative styles.

#### 4.4 Benchmarks

We also take a simple benchmark and the result is shown in **Table 2** (examples are taken from Giovini et al. [8]). This compares the algorithms implemented in our computational-algebra package and Singular. The first four rows correspond to the algorithms implemented in our library; i.e. the Buchberger algorithm optimised with syzygy and sugar strategy (B), the degree-by-degree algorithm for homogeneous ideals (DbyD), the Hilbert-driven algorithm (Hilb), and F₅. S(gr) and S(sba) stand for the `groebner` and `sba` functions in the Singular computer algebra system 4.0.3. The complete source-code is available on GitHub [12]. The benchmark program is compiled with GHC 8.2.2 with flags `-O2 -threaded -rtsopts -with-rtsopts=-N`, and ran on an Intel Xeon E5-2690 at 2.90 GHz, RAM 128GB, Linux 3.16.0-4 (SMP), using 10 cores in parallel. We used the Gauge framework to report the run-time of our library, and the `rtimer` primitive for Singular. Unfortunately, in our system, F₄ takes much more computing time, hence we did not include the result. The results show that, among the algorithms implemented in our system, F₅ works fine in general, though it takes much time in some specific cases. Nevertheless, there remains much room for improvement to compete with the state-of-the-art implementations such as Singular, although there is one case where our implementation is slightly faster than Singular's `groebner` function.

---

### النسخة العربية

في هذا القسم، سنركز على ثلاث خوارزميات كدراسات حالة: خوارزميات Hilbert-driven و F₄ و F₅. أولاً، نوضح قوة الكسل والتوازي بواسطة خوارزمية Hilbert-driven. ثم من خلال واجهة F₄، نوضح مثالاً عملياً على قابلية التركيب. أخيراً، نستعرض بشكل سريع النسخة المبسطة من الروتين الرئيسي لـ F₅ ونرى كيف يمكن كتابة البرمجة الإلزامية مع الحالات القابلة للتغيير بشكل نقي في Haskell. لغرضنا، سنناقش فقط جزءاً من التطبيقات التي توضح مزايا Haskell، بدلاً من التطبيق الكامل والتفاصيل النظرية.

#### 4.1 التجنيس وتحويل القاعدة المدفوع بـ Hilbert

التجنيس (Homogenisation) هو أداة قوية في حساب قاعدة Gröbner. إذا كان I ⊆ k[X] مثالياً غير متجانس و Ī ⊆ k[x, X] تجنيسه، فيمكن للمرء الحصول على قاعدة Gröbner لـ I عن طريق إزالة التجنيس من قاعدة Gröbner Ḡ لـ Ī بالنسبة لترتيب أحادي الحد المُحفز بشكل مناسب. بهذه الطريقة، يمكن تحويل أي خوارزمية قاعدة Gröbner للمثاليات المتجانسة إلى واحدة للمثاليات غير المتجانسة.

**الكود 6** هو واجهة برمجة تطبيقات لهذه العمليات. يمثل النوع `Homogenised poly` كثيرات الحدود التي تم الحصول عليها من خلال تجنيس كثيرات الحدود من النوع `poly`. ثم تتحقق `calcGBViaHomog calc i` أولاً مما إذا كان المدخل `i` متجانساً. إذا كان الأمر كذلك، فإنها تطبق الوسيط `calc` على مدخلها مباشرة (السطر 15)؛ وإلا، فإنها تجنس المدخل أولاً، وتطبق `calc`، ثم تزيل التجنيس للحصول على النتيجة النهائية (السطر 16). لاحظ أنه، على الرغم من أنها تستخدم نفس المصطلح `calc` في كلتا الحالتين، إلا أن لديهما أنواعاً مختلفة. في الحالة الأولى، نظراً لأنها تغذي المدخل مباشرة فقط، فإن `calc` من النوع `Ideal poly → [poly]`. من ناحية أخرى، في الحالة غير المتجانسة، يتم تطبيقها بعد التجنيس، وبالتالي فهي من النوع `Ideal (Homogenised poly) → [Homogenised poly]`. وبالتالي، تأخذ `calcGBViaHomog` دالة متعددة الأشكال كوسيطها الأول وهذا هو السبب في أن لدينا `∀` داخل نوع الوسيط الأول. يُسمى مثل هذا النوع متعدد الأشكال المتداخل نوع متعدد الأشكال من الرتبة n، وهو مدعوم بامتداد لغة RankNTypes في GHC.

على سبيل المثال، يمكن للمرء استخدام ما يسمى خوارزمية Hilbert-driven كالوسيط الأول لـ `calcGBViaHomog`. تحسب أولاً قاعدة Gröbner بالنسبة لترتيب أحادي حد أخف، وتحسب سلسلة Hilbert–Poincaré (HPS) معها وتستخدمها لحساب قاعدة Gröbner بالنسبة للترتيب الأثقل. في هذا الإجراء، نحتاج إلى العمليات التالية على HPS: اختبار المساواة على HPS، معامل تايلور النوني لـ HPS المعطى، وعملية الوحدة Z[X] على HPS. يوضح **الكود 7** مثل هذه الواجهة لـ HPS. لاختبار المساواة، نستخدم البسط `hpsNumerator` للشكل المغلق، وتحافظ قائمة لانهائية `taylor` على معاملات تايلور. بفضل الطبيعة الكسولة لـ Haskell، يمكننا معاملة القوائم اللانهائية بشكل بديهي وكتابة التفاف (convolution) عليها. في السطر 12، يحدد `par` و `seq` استراتيجية التقييم. باختصار، يتم تقييم التعبيرات x و y في "x 'par' y" (أو seq) بشكل متوازٍ (أو متسلسل). نظراً لأن كل تعبير نقي في Haskell، يمكننا الاستفادة بأمان من التوازي، دون احتمال تغيير النتائج.

#### 4.2 تطبيق قابل للتركيب لـ F₄

F₄ هي واحدة من أكثر الخوارزميات كفاءة لحساب قاعدة Gröbner وقدمها Faugère [5]. باختصار، تقلل F₄ أكثر من كثيري حدود اثنين في وقت واحد، وتستبدل حساب باقي كثير الحدود S في خوارزمية Buchberger بالحذف الغاوسي للمصفوفات. هذا يعني أن كفاءة F₄ تتقلص إلى كفاءة الحذف الغاوسي والتمثيل الداخلي للمصفوفات. وبالتالي، من المفيد إذا كان بإمكاننا تبديل التمثيلات الداخلية وخوارزميات الحذف بسهولة. لهذا الغرض، نوفر أصناف أنواع للمصفوفات القابلة للتغيير وغير القابلة للتغيير التي تسمح بعمليات الصف وحذف غاوسي مخصص. يوضح **الكود 8** الواجهة للمصفوفات غير القابلة للتغيير والقابلة للتغيير (`Matrix` و `MMatrix`) وتوقيع النوع لتطبيق F₄ الخاص بنا (`f4`). في الأسطر 1 و 6، يتوافق وسيط النوع الأخير `a` لـ `Matrix` و `MMatrix` مع نوع المعاملات. لاحظ أنه، يمكن للمرء إعطاء تعريفات نماذج مختلفة لنفس `mat` ولكن أنواع معاملات `a` مختلفة. على سبيل المثال، يمكن للمرء تطبيق حذف غاوسي فعال على F_p لـ `Matrix Mat F_p`، ثم استخدامه في تعريف `Matrix Mat Q`، مع رفع Hensel أو الباقي الصيني.

في السطر 15، يحدد الوسيط الأول لـ `f4` من النوع `proxy mat` التمثيل الداخلي `mat` للمصفوفات. بالإضافة إلى ذلك، تأخذ `f4` استراتيجية اختيار كوسيط ثانٍ. هنا، يتم تجريد استراتيجية الاختيار كدالة ترجيح لبعض الأنواع المرتبة، ونخزن كثيرات الحدود الوسيطة في كومة ونختار جميع كثيرات الحدود ذات الوزن الأدنى في كل تكرار.

#### 4.3 خوارزمية F₅

أخيراً، نقدم النسخة المبسطة من الروتين الرئيسي لـ F₅ لـ Faugère [6] (**الكود 9**). قد يفاجأ القراء من أن الشفرة تبدو إلزامية إلى حد كبير. أصبح هذا ممكناً بفضل ST monad [19]، الذي يغلف التأثيرات الجانبية التي تقدمها الحالات القابلة للتغيير ويمنعها من التسرب إلى الخارج. نستخدم كومة وظيفية لاختيار متجهات كثيرات الحدود ذات أقل توقيع، مما يوضح دمج الأنماط الوظيفية والإلزامية.

#### 4.4 المعايير القياسية

نأخذ أيضاً معياراً بسيطاً والنتيجة موضحة في **الجدول 2** (الأمثلة مأخوذة من Giovini وآخرون [8]). يقارن هذا الخوارزميات المُطبقة في حزمة computational-algebra الخاصة بنا و Singular. تتوافق الصفوف الأربعة الأولى مع الخوارزميات المُطبقة في مكتبتنا؛ أي خوارزمية Buchberger المُحسنة باستراتيجية syzygy و sugar (B)، خوارزمية درجة بدرجة للمثاليات المتجانسة (DbyD)، خوارزمية Hilbert-driven (Hilb)، و F₅. يرمز S(gr) و S(sba) إلى دالتي `groebner` و `sba` في نظام الجبر الحاسوبي Singular 4.0.3. الشفرة المصدرية الكاملة متاحة على GitHub [12]. تم تجميع برنامج المعيار القياسي باستخدام GHC 8.2.2 مع العلامات `-O2 -threaded -rtsopts -with-rtsopts=-N`، وتم تشغيله على Intel Xeon E5-2690 بسرعة 2.90 جيجاهرتز، ذاكرة وصول عشوائي 128 جيجابايت، Linux 3.16.0-4 (SMP)، باستخدام 10 أنوية بالتوازي. استخدمنا إطار عمل Gauge للإبلاغ عن وقت التشغيل لمكتبتنا، والبدائي `rtimer` لـ Singular. للأسف، في نظامنا، تستغرق F₄ وقت حوسبة أكثر بكثير، وبالتالي لم ندرج النتيجة. تظهر النتائج أنه، من بين الخوارزميات المُطبقة في نظامنا، تعمل F₅ بشكل جيد بشكل عام، على الرغم من أنها تستغرق وقتاً طويلاً في بعض الحالات المحددة. ومع ذلك، لا تزال هناك مساحة كبيرة للتحسين للمنافسة مع التطبيقات الحديثة مثل Singular، على الرغم من وجود حالة واحدة يكون فيها تطبيقنا أسرع قليلاً من دالة `groebner` في Singular.

---

### Translation Notes

- **Figures referenced:** Code 6, Code 7, Code 8, Code 9, Table 2
- **Key terms introduced:** homogenisation (التجنيس), unhomogenising (إزالة التجنيس), Hilbert–Poincaré series (سلسلة Hilbert–Poincaré), Taylor coefficient (معامل تايلور), convolution (التفاف), Gaussian elimination (الحذف الغاوسي), mutable/immutable (قابل للتغيير/غير قابل للتغيير), ST monad (ST monad), Hensel lifting (رفع Hensel), Chinese remaindering (الباقي الصيني)
- **Equations:** Mathematical notation preserved
- **Citations:** [5, 6, 8, 12, 19]
- **Special handling:**
  - All code examples preserved in English
  - Algorithm names (F₄, F₅, Buchberger) kept in English
  - Benchmark table data preserved as is
  - Technical system names maintained
  - Mathematical symbols and formulas unchanged

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
