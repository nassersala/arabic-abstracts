# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** lazy evaluation, call-by-need, call-by-value, call-by-name, monad, functional programming, evaluation strategy

---

### English Version

Purely functional languages use lazy evaluation (also called *call-by-need*) to allow elegant programming with infinite data structures and to guarantee that a program will not evaluate a diverging term unless it is needed to obtain the final result. However, reasoning about lazy evaluation is difficult thus it is not suitable for programming with effects.

An elegant way to embed effectful computations in lazy functional languages, introduced by Moggi and Wadler, is to use monads. Monads embed effects in a purely functional setting and explicitly specify the evaluation order of monadic (effectful) operations.

Wadler gives two ways of translating pure programs to a corresponding monadic version. One approach leads to a *call-by-value* semantics, where effects of function arguments are performed before calling a function. However, if an argument has an effect and terminates the program, this may not be appropriate if the function can successfully complete without using the argument. The second approach gives a *call-by-name* semantics, where effects are performed only if the argument is actually used. However, this approach is also not always suitable, because an effect may be performed repeatedly. Wadler leaves an open question whether there is a translation that would correspond to *call-by-need* semantics, where effects are performed only when the result is needed, but at most once.

The main contribution of this paper is an alternative translation of functional code to a monadic form, parameterized by an operation *malias*. The translation has the following properties:

- A single translation gives monadic code with either call-by-name or call-by-value semantics, depending on the definition of *malias* (Section 2). When used in languages such as Haskell, it is possible to write code that is parameterized by the evaluation strategy.

- The translation can be used to construct monads that provide the *call-by-need* semantics, which partly answers the open question posed by Wadler. Furthermore, for some monads, it is possible to use *parallel call-by-need* semantics, where arguments are evaluated in parallel with the body of a function.

- The *malias* operation has solid foundations in category theory. It arises from augmenting a *monad* structure with a *computational semi-comonad* based on the same functor (Section 3). We use this theory to define laws that should be obeyed by *malias* implementations.

This paper was inspired by work on *joinads*, which introduced the *malias* operation for a similar purpose. However, operations with the same type and similar laws appear several times in the literature. We return to joinads in Section 4 and review other related work in Section 5.

#### Translating to monadic code

We first demonstrate the two standard options for translating purely functional code to monadic form. Consider the following two functions that use `pureLookupInput` to read some configuration property. Assuming the configuration is already loaded in memory, we can write the following pure computation:

```haskell
chooseSize :: Int -> Int -> Int
chooseSize new legacy =
  if new > 0 then new else legacy

resultSize :: Int
resultSize =
  chooseSize (pureLookupInput "new_size")
             (pureLookupInput "legacy_size")
```

The `resultSize` function reads two different configuration keys and chooses one of them using `chooseSize`. When using a language with lazy evaluation, the call `pureLookupInput "legacy_size"` is performed only when the value of `"new_size"` is less than or equal to zero.

To modify the function to actually read configuration from a file as opposed to performing in-memory lookup, we now use `lookupInput` which returns `IO Int` instead of the `pureLookupInput` function. Then we need to modify the two above functions. There are two mechanical ways that give different semantics.

**Call-by-value.** In the first style, we call `lookupInput` and then apply monadic bind on the resulting computation. This reads both of the configuration values before calling the `chooseSize` function, and so arguments are fully evaluated before the body of a function as in the *call-by-value* evaluation strategy:

```haskell
chooseSize_cbv :: Int -> Int -> IO Int
chooseSize_cbv new legacy =
  return (if new > 0 then new else legacy)

resultSize_cbv :: IO Int
resultSize_cbv = do
  new <- lookupInput_cbv "new_size"
  legacy <- lookupInput_cbv "legacy_size"
  chooseSize_cbv new legacy
```

In this version of the translation, a function of type `A -> B` is turned into a function `A -> M B`. For example, the `chooseSize_cbv` function takes integers as parameters and returns a computation that returns an integer and may perform some effects. When calling a function in this setting, the arguments may not be fully evaluated (the functional part is still lazy), but the effects associated with obtaining the value of the argument happen before the function call.

For example, if the call `lookupInput_cbv "new_size"` read a file and then returned 1024, but the operation `lookupInput_cbv "legacy_size"` caused the program to crash because a specified key was not present in a configuration file, then the entire program would crash.

**Call-by-name.** In the second style, we pass unevaluated computations as arguments to functions. This means we call `lookupInput` to create an effectful computation that will read the input, but the computation is then passed to `chooseSize`, which may not need to evaluate it:

```haskell
chooseSize_cbn :: IO Int -> IO Int -> IO Int
chooseSize_cbn new legacy = do
  newVal <- new
  if newVal > 0 then new else legacy

resultSize_cbn :: IO Int
resultSize_cbn =
  chooseSize_cbn (lookupInput_cbn "new_size")
                 (lookupInput_cbn "legacy_size")
```

The translation turns a function of type `A -> B` into a function `M A -> M B`. This means that the `chooseSize_cbn` function takes a computation that performs the I/O effect and reads information from the configuration file, as opposed to taking a value whose effects were already performed.

Following the mechanical translation, `chooseSize_cbn` returns a monadic computation that evaluates the first argument and then behaves either as `new` or as `legacy`, depending on the obtained value. When the resulting computation is executed, the computation which reads the value of the `"new_size"` key may be executed repeatedly. First, inside the `chooseSize_cbn` function and then repeatedly when the result of this function is evaluated. In this particular example, we can easily change the code to perform the effect just once, but this is not generally possible for computations obtained by the *call-by-name* translation.

---

### النسخة العربية

تستخدم اللغات الوظيفية النقية التقييم الكسول (lazy evaluation) (المسمى أيضاً *استدعاء بالحاجة*) للسماح بالبرمجة الأنيقة مع هياكل البيانات اللانهائية ولضمان أن البرنامج لن يُقيّم حداً متباعداً (diverging term) إلا إذا كان ضرورياً للحصول على النتيجة النهائية. ومع ذلك، فإن الاستدلال حول التقييم الكسول أمر صعب وبالتالي فهو غير مناسب للبرمجة مع الآثار الجانبية.

الطريقة الأنيقة لتضمين الحسابات ذات الآثار الجانبية في اللغات الوظيفية الكسولة، والتي قدمها Moggi و Wadler، هي استخدام الموناد. تُضمّن الموناد الآثار الجانبية في بيئة وظيفية نقية وتحدد بشكل صريح ترتيب التقييم للعمليات الموناد (ذات الآثار الجانبية).

يقدم Wadler طريقتين لترجمة البرامج النقية إلى نسخة موناد مقابلة. يؤدي أحد النهجين إلى دلاليات *استدعاء بالقيمة*، حيث تُنفذ آثار وسائط الدالة قبل استدعاء الدالة. ومع ذلك، إذا كان لوسيط ما تأثير وأنهى البرنامج، فقد لا يكون هذا مناسباً إذا كانت الدالة يمكن أن تكتمل بنجاح دون استخدام الوسيط. يعطي النهج الثاني دلاليات *استدعاء بالاسم*، حيث تُنفذ الآثار فقط إذا تم استخدام الوسيط فعلياً. ومع ذلك، هذا النهج أيضاً ليس مناسباً دائماً، لأن التأثير قد يُنفذ بشكل متكرر. يترك Wadler سؤالاً مفتوحاً حول ما إذا كانت هناك ترجمة تتوافق مع دلاليات *استدعاء بالحاجة*، حيث تُنفذ الآثار فقط عندما تكون النتيجة مطلوبة، ولكن مرة واحدة على الأكثر.

المساهمة الرئيسية لهذا البحث هي ترجمة بديلة للشفرة الوظيفية إلى صيغة موناد، مُعَلّمة بعملية *malias*. تمتلك الترجمة الخصائص التالية:

- تعطي ترجمة واحدة شفرة موناد بدلاليات استدعاء بالاسم أو استدعاء بالقيمة، اعتماداً على تعريف *malias* (القسم 2). عند الاستخدام في لغات مثل Haskell، من الممكن كتابة شفرة مُعَلّمة باستراتيجية التقييم.

- يمكن استخدام الترجمة لبناء موناد توفر دلاليات *استدعاء بالحاجة*، مما يجيب جزئياً على السؤال المفتوح الذي طرحه Wadler. علاوة على ذلك، بالنسبة لبعض الموناد، من الممكن استخدام دلاليات *استدعاء بالحاجة الموازية* (parallel call-by-need)، حيث يتم تقييم الوسائط بالتوازي مع جسم الدالة.

- عملية *malias* لها أسس راسخة في نظرية التصنيف (category theory). تنشأ من إضافة بنية *كوموناد شبه حوسبية* (computational semi-comonad) إلى بنية *موناد* بناءً على نفس الدالة التصنيفية (القسم 3). نستخدم هذه النظرية لتحديد القوانين التي يجب أن تطيعها تطبيقات *malias*.

استُلهم هذا البحث من العمل على *joinads*، الذي قدم عملية *malias* لغرض مماثل. ومع ذلك، تظهر عمليات بنفس النوع وقوانين مماثلة عدة مرات في الأدبيات. نعود إلى joinads في القسم 4 ونراجع الأعمال ذات الصلة الأخرى في القسم 5.

#### الترجمة إلى شفرة موناد

نُظهر أولاً الخيارين القياسيين لترجمة الشفرة الوظيفية النقية إلى صيغة موناد. لنأخذ الدالتين التاليتين اللتين تستخدمان `pureLookupInput` لقراءة خاصية إعداد معينة. بافتراض أن الإعداد محمّل بالفعل في الذاكرة، يمكننا كتابة الحساب النقي التالي:

```haskell
chooseSize :: Int -> Int -> Int
chooseSize new legacy =
  if new > 0 then new else legacy

resultSize :: Int
resultSize =
  chooseSize (pureLookupInput "new_size")
             (pureLookupInput "legacy_size")
```

تقرأ الدالة `resultSize` مفتاحي إعداد مختلفين وتختار أحدهما باستخدام `chooseSize`. عند استخدام لغة مع تقييم كسول، يتم تنفيذ الاستدعاء `pureLookupInput "legacy_size"` فقط عندما تكون قيمة `"new_size"` أقل من أو تساوي الصفر.

لتعديل الدالة لقراءة الإعداد فعلياً من ملف بدلاً من إجراء بحث في الذاكرة، نستخدم الآن `lookupInput` التي تُرجع `IO Int` بدلاً من دالة `pureLookupInput`. بعد ذلك نحتاج إلى تعديل الدالتين أعلاه. هناك طريقتان آليتان تعطيان دلاليات مختلفة.

**استدعاء بالقيمة.** في النمط الأول، نستدعي `lookupInput` ثم نطبق الربط الموناد على الحساب الناتج. هذا يقرأ كلا قيم الإعداد قبل استدعاء الدالة `chooseSize`، وبالتالي يتم تقييم الوسائط بالكامل قبل جسم الدالة كما في استراتيجية التقييم *استدعاء بالقيمة*:

```haskell
chooseSize_cbv :: Int -> Int -> IO Int
chooseSize_cbv new legacy =
  return (if new > 0 then new else legacy)

resultSize_cbv :: IO Int
resultSize_cbv = do
  new <- lookupInput_cbv "new_size"
  legacy <- lookupInput_cbv "legacy_size"
  chooseSize_cbv new legacy
```

في هذا الإصدار من الترجمة، يتم تحويل دالة من نوع `A -> B` إلى دالة `A -> M B`. على سبيل المثال، تأخذ الدالة `chooseSize_cbv` أعداداً صحيحة كمعاملات وتُرجع حساباً يُرجع عدداً صحيحاً وقد ينفذ بعض الآثار. عند استدعاء دالة في هذا السياق، قد لا يتم تقييم الوسائط بالكامل (الجزء الوظيفي لا يزال كسولاً)، لكن الآثار المرتبطة بالحصول على قيمة الوسيط تحدث قبل استدعاء الدالة.

على سبيل المثال، إذا قرأ الاستدعاء `lookupInput_cbv "new_size"` ملفاً ثم أرجع 1024، لكن العملية `lookupInput_cbv "legacy_size"` تسببت في تعطل البرنامج لأن مفتاحاً محدداً لم يكن موجوداً في ملف الإعداد، فسيتعطل البرنامج بأكمله.

**استدعاء بالاسم.** في النمط الثاني، نمرر حسابات غير مُقيّمة كوسائط للدوال. هذا يعني أننا نستدعي `lookupInput` لإنشاء حساب ذو آثار جانبية سيقرأ المدخلات، ولكن يتم بعد ذلك تمرير الحساب إلى `chooseSize`، التي قد لا تحتاج إلى تقييمه:

```haskell
chooseSize_cbn :: IO Int -> IO Int -> IO Int
chooseSize_cbn new legacy = do
  newVal <- new
  if newVal > 0 then new else legacy

resultSize_cbn :: IO Int
resultSize_cbn =
  chooseSize_cbn (lookupInput_cbn "new_size")
                 (lookupInput_cbn "legacy_size")
```

تحول الترجمة دالة من نوع `A -> B` إلى دالة `M A -> M B`. هذا يعني أن الدالة `chooseSize_cbn` تأخذ حساباً ينفذ تأثير الإدخال/الإخراج ويقرأ المعلومات من ملف الإعداد، بدلاً من أخذ قيمة تم تنفيذ آثارها بالفعل.

بعد الترجمة الآلية، تُرجع `chooseSize_cbn` حساباً موناد يُقيّم الوسيط الأول ثم يتصرف إما كـ `new` أو كـ `legacy`، اعتماداً على القيمة المحصلة. عند تنفيذ الحساب الناتج، قد يتم تنفيذ الحساب الذي يقرأ قيمة المفتاح `"new_size"` بشكل متكرر. أولاً، داخل الدالة `chooseSize_cbn` ثم بشكل متكرر عند تقييم نتيجة هذه الدالة. في هذا المثال بالذات، يمكننا بسهولة تغيير الشفرة لتنفيذ التأثير مرة واحدة فقط، ولكن هذا غير ممكن بشكل عام للحسابات التي يتم الحصول عليها من خلال ترجمة *استدعاء بالاسم*.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** malias, computational semi-comonad, joinads, diverging term
- **Code examples:** 6 Haskell code blocks (kept in English)
- **Citations:** Moggi, Wadler (multiple references)
- **Special handling:**
  - Code blocks preserved in original English
  - Technical term "malias" kept in English as it's a specific operation introduced in the paper
  - "diverging term" translated as حد متباعد

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-Translation Check

First paragraph back-translates to: "Purely functional languages use lazy evaluation (also called *call-by-need*) to allow elegant programming with infinite data structures and to ensure that the program will not evaluate a diverging term unless it is necessary to obtain the final result. However, reasoning about lazy evaluation is difficult and therefore it is not suitable for programming with side effects."
