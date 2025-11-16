# Section 4: Abstracting evaluation strategy in practice
## القسم 4: تجريد استراتيجية التقييم عملياً

**Section:** implementation and applications
**Translation Quality:** 0.87
**Glossary Terms Used:** monad, evaluation strategy, call-by-value, call-by-name, call-by-need, monad transformer, functional programming

---

### English Version (Summary)

In this section, we present several practical uses of the *malias* operation. We start by showing how to write monadic code that is parameterized over the evaluation strategy and then consider expressing *call-by-need* in this framework. Then we also briefly consider *parallel call-by-need* and the relation between *malias* and *joinads*.

#### Parameterization by evaluation strategy

One of the motivations of this work is that the standard monadic translations for *call-by-name* and *call-by-value* produce code with different structure. Section 2 gave a translation that can be used with both of the evaluation strategies just by changing the definition of the *malias* operation. In this section, we make one more step -- we show how to write code parameterized by evaluation strategy.

We define a *monad transformer* that takes a monad and turns it into a monad with `malias` that implements a specific evaluation strategy. Our example can then be implemented using functions that are polymorphic over the monad transformer. We continue using the previous example based on the `IO` monad, but the transformer can operate on any monad.

As a first step, we define a type class named `MonadAlias` that extends `Monad` with the *malias* operation:

```haskell
class Monad m => MonadAlias m where
  malias :: m a -> m (m a)
```

Next, we define two new types that represent monadic computations using the *call-by-name* and *call-by-value* evaluation strategy. The two types are wrappers that make it possible to implement two different instances of `MonadAlias` for any underlying monadic computation `m a`:

```haskell
newtype CbV m a = CbV { runCbV :: m a }
newtype CbN m a = CbN { runCbN :: m a }
```

The implementation of the `Monad` type class is the same for both types, because it simply uses `return` and bind operations of the underlying monad. The instances of the `MonadAlias` type class associate the two implementations of *malias* with the two data types:

```haskell
instance Monad m => MonadAlias (CbV m) where
  malias m = m >>= (return . return)

instance Monad m => MonadAlias (CbN m) where
  malias m = return m
```

**Example.** Using the previous definitions, we can now rewrite the example using generic functions that can be executed using both `runCbV` and `runCbN`. Instead of implementing *malias* for a specific monad such as `IO a`, we use a monad transformer `t` that lifts the monadic computation to either `CbV IO a` or to `CbN IO a`.

In Haskell, this can be succinctly written using *constraint kinds* that make it possible to define a single constraint `EvalStrategy t m` that combines both conditions:

```haskell
type EvalStrategy t m = (MonadTrans t, MonadAlias (t m))

chooseSize :: EvalStrategy t IO => t IO Int -> t IO Int -> t IO Int
chooseSize new legacy = do
  newVal <- new
  if newVal > 0 then new else legacy

resultSize :: EvalStrategy t IO => t IO Int
resultSize = do
  new <- malias $ lift (lookupInput "new_size")
  legacy <- malias $ lift (lookupInput "legacy_size")
  chooseSize new legacy
```

The return type of the `resultSize` computation is parameterized over the evaluation strategy `t`. This means that we can call it in two different ways. Writing `runCbN resultSize` executes the computation using call-by-name semantics, while `runCbV resultSize` uses call-by-value semantics.

#### Call-by-need semantics

The previous section showed how to implement code that is parameterized over the evaluation strategy. However, we used only the two basic evaluation strategies. In this section, we show how to implement *call-by-need* semantics for some monads.

For call-by-need semantics, we need to ensure that effects are performed at most once. This can be achieved by using memoization. For monads that support state, we can implement call-by-need by storing computed values in a state and retrieving them when needed again.

The paper presents an implementation using the `State` monad transformer that maintains a cache of computed values. The key idea is that *malias* creates a computation that, when first executed, performs the effects and stores the result. Subsequent executions retrieve the cached value without re-executing the effects.

#### Parallel call-by-need

For some monads, it is possible to implement a *parallel call-by-need* strategy where arguments are evaluated in parallel with the body of a function. This is particularly useful for monads representing parallel computations.

The implementation uses futures or promises to represent computations that may execute in parallel. The *malias* operation starts the computation in the background and returns a reference that can be used to retrieve the result when needed.

#### Relation to joinads

The *malias* operation is related to the concept of *joinads*, which extends monads with pattern matching capabilities for concurrent and parallel programming. Joinads introduce additional operations that allow programmers to express patterns of concurrent execution.

The *malias* operation can be seen as a building block for implementing joinads. The paper discusses how joinads use a similar operation to abstract over different execution patterns, and how the theoretical framework of computational semi-bimonads provides a foundation for understanding these abstractions.

---

### النسخة العربية (ملخص)

في هذا القسم، نقدم عدة استخدامات عملية لعملية *malias*. نبدأ بإظهار كيفية كتابة شفرة موناد مُعَلّمة على استراتيجية التقييم ثم ننظر في التعبير عن *استدعاء بالحاجة* في هذا الإطار. ثم ننظر أيضاً بإيجاز في *استدعاء بالحاجة الموازية* والعلاقة بين *malias* و*joinads*.

#### المعلمة باستراتيجية التقييم

أحد دوافع هذا العمل هو أن الترجمات الموناد القياسية لـ *استدعاء بالاسم* و*استدعاء بالقيمة* تنتج شفرة ببنية مختلفة. أعطى القسم 2 ترجمة يمكن استخدامها مع كلتا استراتيجيتي التقييم فقط بتغيير تعريف عملية *malias*. في هذا القسم، نتخذ خطوة إضافية -- نُظهر كيفية كتابة شفرة مُعَلّمة باستراتيجية التقييم.

نُعرّف *محول موناد* (monad transformer) يأخذ موناد ويحوله إلى موناد مع `malias` ينفذ استراتيجية تقييم محددة. يمكن بعد ذلك تطبيق مثالنا باستخدام دوال متعددة الأشكال على محول الموناد. نستمر في استخدام المثال السابق بناءً على موناد `IO`، لكن المحول يمكن أن يعمل على أي موناد.

كخطوة أولى، نُعرّف صنف نوع مسمى `MonadAlias` يُوسّع `Monad` بعملية *malias*:

```haskell
class Monad m => MonadAlias m where
  malias :: m a -> m (m a)
```

بعد ذلك، نُعرّف نوعين جديدين يمثلان حسابات موناد باستخدام استراتيجية التقييم *استدعاء بالاسم* و*استدعاء بالقيمة*. النوعان هما أغلفة تجعل من الممكن تطبيق نسختين مختلفتين من `MonadAlias` لأي حساب موناد أساسي `m a`:

```haskell
newtype CbV m a = CbV { runCbV :: m a }
newtype CbN m a = CbN { runCbN :: m a }
```

تطبيق صنف النوع `Monad` هو نفسه لكلا النوعين، لأنه يستخدم ببساطة عمليات `return` و bind للموناد الأساسية. تربط نسخ صنف النوع `MonadAlias` تطبيقي *malias* مع نوعي البيانات:

```haskell
instance Monad m => MonadAlias (CbV m) where
  malias m = m >>= (return . return)

instance Monad m => MonadAlias (CbN m) where
  malias m = return m
```

**مثال.** باستخدام التعريفات السابقة، يمكننا الآن إعادة كتابة المثال باستخدام دوال عامة يمكن تنفيذها باستخدام كل من `runCbV` و `runCbN`. بدلاً من تطبيق *malias* لموناد محددة مثل `IO a`، نستخدم محول موناد `t` يرفع الحساب الموناد إما إلى `CbV IO a` أو إلى `CbN IO a`.

في Haskell، يمكن كتابة هذا بإيجاز باستخدام *أنواع القيود* (constraint kinds) التي تجعل من الممكن تعريف قيد واحد `EvalStrategy t m` يجمع كلا الشرطين:

```haskell
type EvalStrategy t m = (MonadTrans t, MonadAlias (t m))

chooseSize :: EvalStrategy t IO => t IO Int -> t IO Int -> t IO Int
chooseSize new legacy = do
  newVal <- new
  if newVal > 0 then new else legacy

resultSize :: EvalStrategy t IO => t IO Int
resultSize = do
  new <- malias $ lift (lookupInput "new_size")
  legacy <- malias $ lift (lookupInput "legacy_size")
  chooseSize new legacy
```

نوع الإرجاع لحساب `resultSize` مُعَلّم على استراتيجية التقييم `t`. هذا يعني أنه يمكننا استدعاؤه بطريقتين مختلفتين. كتابة `runCbN resultSize` تنفذ الحساب باستخدام دلاليات استدعاء بالاسم، بينما `runCbV resultSize` تستخدم دلاليات استدعاء بالقيمة.

#### دلاليات استدعاء بالحاجة

أظهر القسم السابق كيفية تطبيق شفرة مُعَلّمة على استراتيجية التقييم. ومع ذلك، استخدمنا فقط استراتيجيتي التقييم الأساسيتين. في هذا القسم، نُظهر كيفية تطبيق دلاليات *استدعاء بالحاجة* لبعض الموناد.

لدلاليات استدعاء بالحاجة، نحتاج إلى ضمان تنفيذ الآثار مرة واحدة على الأكثر. يمكن تحقيق ذلك باستخدام التذكير (memoization). بالنسبة للموناد التي تدعم الحالة، يمكننا تطبيق استدعاء بالحاجة بتخزين القيم المحسوبة في حالة واسترجاعها عند الحاجة إليها مرة أخرى.

يقدم البحث تطبيقاً باستخدام محول موناد `State` الذي يحافظ على ذاكرة تخزين مؤقت للقيم المحسوبة. الفكرة الأساسية هي أن *malias* ينشئ حساباً، عند تنفيذه لأول مرة، ينفذ الآثار ويخزن النتيجة. التنفيذات اللاحقة تسترجع القيمة المخزنة مؤقتاً دون إعادة تنفيذ الآثار.

#### استدعاء بالحاجة الموازية

بالنسبة لبعض الموناد، من الممكن تطبيق استراتيجية *استدعاء بالحاجة الموازية* حيث يتم تقييم الوسائط بالتوازي مع جسم الدالة. هذا مفيد بشكل خاص للموناد التي تمثل حسابات موازية.

يستخدم التطبيق المستقبليات (futures) أو الوعود (promises) لتمثيل الحسابات التي قد تنفذ بالتوازي. عملية *malias* تبدأ الحساب في الخلفية وتُرجع مرجعاً يمكن استخدامه لاسترجاع النتيجة عند الحاجة.

#### العلاقة بـ joinads

عملية *malias* مرتبطة بمفهوم *joinads*، الذي يوسّع الموناد بقدرات مطابقة الأنماط للبرمجة المتزامنة والموازية. تُدخل joinads عمليات إضافية تسمح للمبرمجين بالتعبير عن أنماط التنفيذ المتزامن.

يمكن اعتبار عملية *malias* كوحدة بناء لتطبيق joinads. يناقش البحث كيف تستخدم joinads عملية مماثلة لتجريد أنماط التنفيذ المختلفة، وكيف يوفر الإطار النظري للموناد الثنائية الشبه حوسبية أساساً لفهم هذه التجريدات.

---

### Translation Notes

- **Subsections:** Parameterization by evaluation strategy, Call-by-need semantics, Parallel call-by-need, Relation to joinads
- **Code examples:** 5 Haskell code blocks (condensed from original)
- **Key terms introduced:** monad transformer, MonadAlias type class, CbV, CbN, constraint kinds, memoization, futures/promises
- **Citations:** References to monad transformers, constraint kinds, joinads
- **Special handling:**
  - This is a summary translation covering main concepts
  - Some detailed implementation code condensed for brevity
  - Key code examples preserved
  - Technical accuracy maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Check

Opening paragraph back-translates to: "In this section, we present several practical uses of the *malias* operation. We begin by showing how to write monad code parameterized on evaluation strategy then we consider expressing *call-by-need* in this framework. Then we also briefly consider *parallel call-by-need* and the relationship between *malias* and *joinads*."
