# Section 2: Concurrency in Haskell
## القسم 2: التزامن في Haskell

**Section:** background
**Translation Quality:** 0.86
**Glossary Terms Used:** monad, concurrent, thread, transactional memory, atomicity, isolation, mutable, side effects

---

### English Version

Haskell was born as pure lazy functional language; side effects are handled by means of monads. For instance, I/O actions have type `IO a` and can be combined together by the monadic bind combinator `>>=`. Therefore, the function `putChar :: Char -> IO ()` takes a character and delivers an I/O action that, when performed (even multiple times), prints the given character. Besides external inputs/outputs, values of `IO` include operations with side effects on mutable (typed) cells. A cell holding values of type `a` has type `IORef a` and may be dealt with only via the following operations:

```haskell
newIORef   :: a -> IO (IORef a)
readIORef  :: IORef a -> IO a
writeIORef :: IORef a -> a -> IO ()
```

Concurrent Haskell adds support to threads which independently perform a given I/O action as explained by the type of the thread creation function:

```haskell
forkIO :: IO () -> IO ThreadId
```

The main mechanism for safe thread communication and synchronisation are MVars. A value of type `MVar a` is mutable location (as for `IORef a`) that is either empty or full with a value of type `a`. There are two fundamental primitives to interact with MVars:

```haskell
takeMVar :: Mvar a -> IO a
putMvar  :: Mvar a -> a -> IO ()
```

The first empties a full location and blocks otherwise whereas the second fills an empty location and blocks otherwise. Therefore, MVars can be seen as one-place channels and the particular case of `MVar ()` corresponds to binary semaphores.

We refer the reader to [jones:2010awkward-squad] for an introduction to concurrency, I/O, exceptions, and cross language interfacing (the "awkward squad" of pure, lazy, functional programming).

STM Haskell builds on Concurrent Haskell adding transactional actions and a transactional memory for safe thread communication, called transactional variables or TVars for short.

Transactional actions have type `STM a` and are concatenated using `STM` monadic "bind" combinator, akin I/O actions. A transactional action remains tentative during its execution and (its effect) is exposed to the rest of the system by

```haskell
atomically :: STM a -> IO a
```

which takes an STM action and delivers an I/O action that, when performed, runs the transaction guaranteeing atomicity and isolation with respect to the rest of the system.

Transactional variables have type `TVar a` where `a` is the type of the value held and, like IOrefs, are manipulated via the interface:

```haskell
newTVar   :: a -> STM (TVar a)
readTVar  :: TVar a -> STM a
writeTVar :: TVar a -> a -> STM ()
```

For instance, the following code uses monadic bind to combine a read and write operation on a transactional variable and define a "transactional update":

```haskell
modifyTVar :: TVar a -> (a -> a) -> STM ()
modifyTVar var f = do
    x <- readTVar var
    writeOTVar var (f x)
```

Then, `atomically (modifyTVar x f)` delivers an I/O action that applies `f` to the value held by `x` and updates `x` accordingly—the two steps being executed as a single atomic isolated operation.

The primitives recalled so far cover memory interaction, but STM allows also for composable blocking. In STM Haskell, blocking translates in "this thread has been scheduled too early, i.e., the right conditions are not fulfilled (yet)". The programmer can tell the scheduler about this fact by means of the primitive:

```haskell
retry :: STM a
```

The semantics of `retry` is to abort the transaction and re-run it after at least one of the transactional variables it has read from has been updated—there is no point in blindly restarting a transaction.

Finally, transactions can be composed as alternatives by means of

```haskell
orElse :: STM a -> STM a -> STM a
```

which evaluates its first argument, and if this results is a `retry` the second argument is evaluated discarding any effect of the first.

---

### النسخة العربية

وُلدت Haskell كلغة وظيفية كسولة نقية؛ يتم التعامل مع التأثيرات الجانبية باستخدام الموناد. على سبيل المثال، إجراءات الإدخال/الإخراج لها النوع `IO a` ويمكن دمجها معاً بواسطة رابط الموناد `>>=`. لذلك، تأخذ الدالة `putChar :: Char -> IO ()` حرفاً وتقدم إجراء إدخال/إخراج، عند تنفيذه (حتى عدة مرات)، يطبع الحرف المعطى. إلى جانب المدخلات/المخرجات الخارجية، تشمل قيم `IO` العمليات ذات التأثيرات الجانبية على الخلايا القابلة للتغيير (المكتوبة). الخلية التي تحمل قيماً من النوع `a` لها النوع `IORef a` ولا يمكن التعامل معها إلا عبر العمليات التالية:

```haskell
newIORef   :: a -> IO (IORef a)
readIORef  :: IORef a -> IO a
writeIORef :: IORef a -> a -> IO ()
```

تضيف Haskell المتزامنة دعماً للخيوط التي تنفذ بشكل مستقل إجراء إدخال/إخراج معيناً كما هو موضح بنوع دالة إنشاء الخيط:

```haskell
forkIO :: IO () -> IO ThreadId
```

الآلية الرئيسية لاتصال الخيوط الآمن والمزامنة هي MVars. القيمة من النوع `MVar a` هي موقع قابل للتغيير (كما في `IORef a`) يكون إما فارغاً أو ممتلئاً بقيمة من النوع `a`. هناك عمليتان أساسيتان للتفاعل مع MVars:

```haskell
takeMVar :: Mvar a -> IO a
putMvar  :: Mvar a -> a -> IO ()
```

الأولى تفرغ موقعاً ممتلئاً وتحجب بخلاف ذلك، بينما الثانية تملأ موقعاً فارغاً وتحجب بخلاف ذلك. لذلك، يمكن رؤية MVars كقنوات ذات مكان واحد، والحالة الخاصة `MVar ()` تتوافق مع العدادات السيمافورية الثنائية.

نشير القارئ إلى [jones:2010awkward-squad] للحصول على مقدمة للتزامن، والإدخال/الإخراج، والاستثناءات، والتواصل بين اللغات ("الفرقة المحرجة" في البرمجة الوظيفية النقية والكسولة).

تبني STM Haskell على Haskell المتزامنة بإضافة الإجراءات المعاملاتية وذاكرة معاملات لاتصال الخيوط الآمن، تسمى المتغيرات المعاملاتية أو TVars اختصاراً.

الإجراءات المعاملاتية لها النوع `STM a` ويتم ربطها باستخدام رابط الموناد "bind" لـ `STM`، مشابهة لإجراءات الإدخال/الإخراج. يبقى الإجراء المعاملاتي مؤقتاً أثناء تنفيذه ويتم كشف (تأثيره) لبقية النظام بواسطة

```haskell
atomically :: STM a -> IO a
```

الذي يأخذ إجراء STM ويقدم إجراء إدخال/إخراج، عند تنفيذه، يشغل المعاملة مع ضمان الذرية والعزل بالنسبة لبقية النظام.

المتغيرات المعاملاتية لها النوع `TVar a` حيث `a` هو نوع القيمة المحتفظ بها، ومثل IOrefs، يتم التعامل معها عبر الواجهة:

```haskell
newTVar   :: a -> STM (TVar a)
readTVar  :: TVar a -> STM a
writeTVar :: TVar a -> a -> STM ()
```

على سبيل المثال، يستخدم الكود التالي رابط الموناد لدمج عملية قراءة وكتابة على متغير معاملاتي وتعريف "تحديث معاملاتي":

```haskell
modifyTVar :: TVar a -> (a -> a) -> STM ()
modifyTVar var f = do
    x <- readTVar var
    writeOTVar var (f x)
```

بعد ذلك، `atomically (modifyTVar x f)` يقدم إجراء إدخال/إخراج يطبق `f` على القيمة المحتفظ بها في `x` ويحدّث `x` وفقاً لذلك - حيث يتم تنفيذ الخطوتين كعملية معزولة ذرية واحدة.

تغطي العمليات الأساسية المذكورة حتى الآن التفاعل مع الذاكرة، ولكن STM تسمح أيضاً بالحجب القابل للتركيب. في STM Haskell، يترجم الحجب إلى "تم جدولة هذا الخيط مبكراً جداً، أي أن الشروط الصحيحة لم تُستوف (بعد)". يمكن للمبرمج إخبار المجدول بهذه الحقيقة باستخدام العملية الأساسية:

```haskell
retry :: STM a
```

دلالات `retry` هي إحباط المعاملة وإعادة تشغيلها بعد تحديث واحد على الأقل من المتغيرات المعاملاتية التي قرأ منها - لا فائدة من إعادة تشغيل معاملة بشكل أعمى.

أخيراً، يمكن تركيب المعاملات كبدائل باستخدام

```haskell
orElse :: STM a -> STM a -> STM a
```

الذي يقيّم حجته الأولى، وإذا كانت النتيجة `retry` يتم تقييم الحجة الثانية مع تجاهل أي تأثير للأولى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Lazy functional language → لغة وظيفية كسولة
  - Side effects → التأثيرات الجانبية
  - Monadic bind combinator → رابط الموناد
  - Mutable cells → الخلايا القابلة للتغيير
  - Thread creation → إنشاء الخيط
  - One-place channels → قنوات ذات مكان واحد
  - Binary semaphores → العدادات السيمافورية الثنائية
  - Transactional actions → الإجراءات المعاملاتية
  - Transactional variables (TVars) → المتغيرات المعاملاتية
  - Composable blocking → الحجب القابل للتركيب
  - Scheduler → المجدول

- **Equations:** None

- **Citations:**
  - [pw:popl1993]
  - [pgf:popl1996]
  - [jones:2010awkward-squad]
  - [hmpm:ppopp2005]

- **Special handling:**
  - All Haskell code examples preserved in English
  - Type signatures kept as-is
  - Function names preserved (`forkIO`, `putChar`, `newIORef`, etc.)
  - Type constructors preserved (`IO`, `STM`, `TVar`, `MVar`, `IORef`)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
