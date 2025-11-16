# Section 3: Composable open transactions
## القسم 3: المعاملات المفتوحة القابلة للتركيب

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** transactional memory, atomic, isolated, monad, composable, thread, semaphore, blocking, retry

---

### English Version

In this section we present the key ideas of the paper by gradually introducing the primitives from the OTM library, summarised in Figure 1.

Although the OTM model can be implemented in any language, we consider Haskell because its expressive type system offers a perfect environment for studying the ideas of transactional memory. In [hmpm:ppopp2005] this has been used to single out computations which can be executed in transactions, i.e. terms which can perform memory effects, from those which can perform irreversible input/output effects. In this paper we refine further this approach by using the type system to separate isolated transactions from those which can interact, and hence merged.

**Figure 1: The base interface of OTM**
```haskell
data ITM a
data OTM a
-- henceforth, t is a placeholder for ITM or OTM --

-- Sequencing, do notation ------------------------
(>>=)  :: t a -> (a -> t b) -> t b
return :: a -> t a

-- Running isolated and atomic computations -------
atomic   :: OTM a -> IO a
isolated :: ITM a -> OTM a
retry    :: ITM a
orElse   :: ITM a -> ITM a -> ITM a

-- Exceptions -------------------------------------
throw :: Exception e => e -> t a
catch :: Exception e => t a -> (e -> t a) -> t a

-- Threading --------------------------------------
fork :: OTM () -> OTM ThreadId

-- Transactional memory ---------------------------
data OTVar a
newOTVar     :: a -> ITM (OTVar a)
readOTVar    :: OTVar a -> ITM a
writeOTVar   :: OTVar a -> a -> ITM ()
```

The key point is to separate isolation from atomicity. In fact, isolation is a computational aspect which can be added to atomic transactions. From this perspective, we distinguish between isolated atomic actions and (non isolated) atomic actions. The former are values of type `ITM a` and the latter of `OTM a`. Each type of actions can be sequentially composed (by the corresponding monadic binders) preserving atomicity and, for the former, isolation.

The function `isolated` takes an isolated atomic action and delivers an atomic action whose effects are guaranteed to be executed in isolation with respect to other actions. Then, `atomic` takes an atomic action and delivers an I/O action that when performed runs a transaction whose effects are kept tentative until it commits. Tentative effects are shared among all non-isolated transactions. Therefore, any value of type `STM a` can be seen as a value of `ITM a` for the I/O they deliver is the same:

```haskell
atomically  = atomic . isolated
```

**Isolation**

OTM supports composable blocking via the primitive `retry`, under STM slogan "a thread that has to be blocked because it has been scheduled too soon". As for STM, retrying a transactional action actually corresponds to block the threads on some condition. Note that `retry :: OTM a` is not a primitive since it can be defined from that of `ITM` as `isolated retry`.

Checks may be declared as follows:
```haskell
check :: Bool -> ITM ()
check b = if b then return () else retry
```
although similar primitives may be implemented at the runtime level in order to use this information in thread scheduling.

OTM provides a mechanism for safe thread communication by means of transactional variables called OTVars, similar to STM's TVars but supporting open transactions. These variables are values of type `OTVar a` where `a` is the type of value held. Creating, reading and writing OTVars is done via the interface shown in Figure 1. All these actions are both atomic and isolated as ensured by their type. Therefore, when it comes to actions of type `ITM a`, OTVars are basically TVars; e.g. `modifyTVar` from STM corresponds to:

```haskell
modifyOTVar :: OTVar a -> (a -> a) -> ITM ()
modifyOTVar var f = do
    x <- readOTVar var
    writeOTVar var (f x)
```

From its type it is immediate to see that the update is both atomic and isolated. In fact, read and write operations are glued together by the `>>=` combinator, preserving both properties.

Likewise, invariants on transactional variables can be easily checked by composing reads and checks as follows:
```haskell
assertOTVar :: OTVar a -> (a -> Bool) -> ITM ()
assertOTVar var p = do
    x <- readOTVar var
    check (p x)
```

**Blocking**

A semaphore is a counter with two fundamental operation: `up` which increments the counter and `down` which decrements the counter if it is not zero and blocks otherwise. Semaphores are implemented using OTM as OTVars holding a counter:

```haskell
type Semaphore = OTVar Int
```

Then, `up` and `down` are two trivial atomic and isolated updates, with the latter being guarded by a pre-condition:

```haskell
up :: Semaphore -> ITM ()
up s = modifyOTvar s (1+)

down :: Semaphore -> ITM ()
down s = do
    assertOTVar s (> 0)
    modifyOTVar s (-1+)
```

Actions can also be composed as alternatives by means of the primitive `orElse`. For instance, the following takes a family of semaphores and delivers an action that decrements one of them, blocking only if none can be decremented:

```haskell
downAny :: [Sempahore] -> ITM ()
downAny (x:xs) = down x `orElse` downAny xs
downAny [] = retry
```

**Interaction**

The interchangeability of OTM and STM ends when isolation is dropped. In fact, OTM offers shared OTVars as a mechanism for safe transaction interaction. This means that non-isolated transactional actions see the effects on shared variables of any other non-isolated transactional action, as they are performed concurrently on the same object. This flow of information introduces dependencies between concurrent tentative actions tying together their fate: an action cannot make its effects permanent, if it depends on informations produced by another action which fails to complete. OTM guarantees coherence of transactional actions in presence of interaction through shared transactional variables. Thus, OTVars enables loosely-coupled interaction right inside atomic actions taking the programming style of STM a step further. For instance, communication, rendezvous, brokering, and in general, multi-party interactions can all be atomic (non-isolated) actions.

In order to substantiate these claims, let us see open transactions in action by implementing a synchronisation scenario as described in Section 1. In this example a master process outsources part of an atomic computation to some thread chosen from a worker pool; data is exchanged via some shared variable, whose access is coordinated by a pair of semaphores. Notably, both the master and the worker can abort the computation at any time, leading the other party to abort as well. This can be achieved straightforwardly using OTM:

```haskell
master c1 c2 = do               worker c1 c2 = do
    -- put request                 -- do something
    isolated (up c1)                isolated (down c1)
    -- do something else            -- get request
    isolated (down c2)              -- put answer
    -- get answer                   isolated (up c2)
```

Both functions deliver atomic actions in `OTM`, and hence are not isolated. We used semaphores for the sake of exposition but we could synchronize by means of more abstract mechanisms, like barriers, channels or futures, which can be implemented using OTM.

**Concurrency**

Differently from STM, OTM supports parallelism inside non-isolated transactions. We can easily fork new threads without leaving `OTM` but, like any effect of a transactional action, thread creation and execution remain tentative until the whole transaction commits. Forked threads participate to their transaction and impact its life-cycle (e.g. issuing aborts) as any other participant. This means that before committing, all forked threads have to complete their transactional action, i.e. terminate. Therefore, although the whole effect delivered by the transaction has happened concurrently, forked threads never leave a transaction alive.

Because of their transactional nature, threads forked inside a transaction do not have compensations nor continuations (i.e. I/O actions to be executed after an abort or after a commit). Compensations are pointless since aborts revert all effects including thread creation. It is indeed possible to replace the primitive `fork` with one supporting I/O actions as continuations like

```haskell
forkCont :: OTM a -> (a -> IO ()) -> OTM ThreadID
```

In fact, this mechanism can be implemented by means of the primitives already offered OTM: since commits are synchronisation points, the above corresponds to the parent thread forking a thread for each continuation, after the atomic action is successfully completed.

On the other hand, by definition isolated atomic actions have to appear as being executed in a single-threaded setting; hence `ITM`, like `STM`, does not support thread creation.

---

### النسخة العربية

في هذا القسم نقدم الأفكار الرئيسية للبحث من خلال تقديم تدريجي للعمليات الأساسية من مكتبة OTM، الملخصة في الشكل 1.

على الرغم من أن نموذج OTM يمكن تنفيذه في أي لغة، فإننا نعتبر Haskell لأن نظام الأنواع التعبيري الخاص بها يوفر بيئة مثالية لدراسة أفكار ذاكرة المعاملات. في [hmpm:ppopp2005] تم استخدام هذا لتمييز الحوسبات التي يمكن تنفيذها في المعاملات، أي المصطلحات التي يمكن أن تؤدي تأثيرات الذاكرة، عن تلك التي يمكن أن تؤدي تأثيرات إدخال/إخراج غير قابلة للعكس. في هذا البحث نحسّن هذا النهج بشكل أكبر باستخدام نظام الأنواع لفصل المعاملات المعزولة عن تلك التي يمكن أن تتفاعل، وبالتالي يتم دمجها.

**الشكل 1: الواجهة الأساسية لـ OTM**
```haskell
data ITM a
data OTM a
-- من الآن فصاعداً، t هو عنصر نائب لـ ITM أو OTM --

-- التسلسل، تدوين do ------------------------
(>>=)  :: t a -> (a -> t b) -> t b
return :: a -> t a

-- تشغيل الحوسبات المعزولة والذرية -------
atomic   :: OTM a -> IO a
isolated :: ITM a -> OTM a
retry    :: ITM a
orElse   :: ITM a -> ITM a -> ITM a

-- الاستثناءات -------------------------------------
throw :: Exception e => e -> t a
catch :: Exception e => t a -> (e -> t a) -> t a

-- الخيوط --------------------------------------
fork :: OTM () -> OTM ThreadId

-- ذاكرة المعاملات ---------------------------
data OTVar a
newOTVar     :: a -> ITM (OTVar a)
readOTVar    :: OTVar a -> ITM a
writeOTVar   :: OTVar a -> a -> ITM ()
```

النقطة الأساسية هي فصل العزل عن الذرية. في الواقع، العزل هو جانب حسابي يمكن إضافته إلى المعاملات الذرية. من هذا المنظور، نميز بين الإجراءات الذرية المعزولة والإجراءات الذرية (غير المعزولة). الأولى هي قيم من النوع `ITM a` والأخيرة من النوع `OTM a`. يمكن تركيب كل نوع من الإجراءات بشكل تسلسلي (بواسطة روابط الموناد المقابلة) مع الحفاظ على الذرية، وبالنسبة للأولى، العزل.

تأخذ الدالة `isolated` إجراء ذري معزول وتقدم إجراء ذري مضمون تنفيذ تأثيراته بشكل معزول بالنسبة للإجراءات الأخرى. بعد ذلك، تأخذ `atomic` إجراء ذري وتقدم إجراء إدخال/إخراج عند تنفيذه يشغل معاملة يتم الاحتفاظ بتأثيراتها مؤقتة حتى تلتزم. يتم مشاركة التأثيرات المؤقتة بين جميع المعاملات غير المعزولة. لذلك، يمكن النظر إلى أي قيمة من النوع `STM a` كقيمة من النوع `ITM a` لأن الإدخال/الإخراج الذي تقدمه هو نفسه:

```haskell
atomically  = atomic . isolated
```

**العزل**

تدعم OTM الحجب القابل للتركيب عبر العملية الأساسية `retry`، تحت شعار STM "خيط يجب حجبه لأنه تم جدولته مبكراً جداً". كما هو الحال بالنسبة لـ STM، فإن إعادة محاولة إجراء معاملاتي يتوافق فعلياً مع حجب الخيوط على بعض الشروط. لاحظ أن `retry :: OTM a` ليست عملية أساسية لأنه يمكن تعريفها من `ITM` كـ `isolated retry`.

يمكن الإعلان عن الفحوصات على النحو التالي:
```haskell
check :: Bool -> ITM ()
check b = if b then return () else retry
```
على الرغم من أنه يمكن تنفيذ عمليات أساسية مماثلة على مستوى وقت التشغيل من أجل استخدام هذه المعلومات في جدولة الخيوط.

توفر OTM آلية لاتصال الخيوط الآمن باستخدام المتغيرات المعاملاتية المسماة OTVars، مشابهة لـ TVars في STM ولكنها تدعم المعاملات المفتوحة. هذه المتغيرات هي قيم من النوع `OTVar a` حيث `a` هو نوع القيمة المحتفظ بها. يتم إنشاء وقراءة وكتابة OTVars عبر الواجهة الموضحة في الشكل 1. جميع هذه الإجراءات ذرية ومعزولة كما هو مضمون بنوعها. لذلك، عندما يتعلق الأمر بالإجراءات من النوع `ITM a`، فإن OTVars هي في الأساس TVars؛ على سبيل المثال `modifyTVar` من STM يتوافق مع:

```haskell
modifyOTVar :: OTVar a -> (a -> a) -> ITM ()
modifyOTVar var f = do
    x <- readOTVar var
    writeOTVar var (f x)
```

من نوعها يمكن رؤية على الفور أن التحديث ذري ومعزول. في الواقع، يتم ربط عمليات القراءة والكتابة معاً بواسطة الرابط `>>=`، مع الحفاظ على كلتا الخاصيتين.

وبالمثل، يمكن التحقق بسهولة من الثوابت على المتغيرات المعاملاتية من خلال تركيب القراءات والفحوصات على النحو التالي:
```haskell
assertOTVar :: OTVar a -> (a -> Bool) -> ITM ()
assertOTVar var p = do
    x <- readOTVar var
    check (p x)
```

**الحجب**

العداد السيمافوري هو عداد مع عمليتين أساسيتين: `up` التي تزيد العداد و `down` التي تنقص العداد إذا لم يكن صفراً وتحجب بخلاف ذلك. يتم تنفيذ العدادات السيمافورية باستخدام OTM كـ OTVars تحمل عداداً:

```haskell
type Semaphore = OTVar Int
```

بعد ذلك، `up` و `down` هما تحديثان ذريان ومعزولان بسيطان، مع كون الأخير محمياً بشرط مسبق:

```haskell
up :: Semaphore -> ITM ()
up s = modifyOTvar s (1+)

down :: Semaphore -> ITM ()
down s = do
    assertOTVar s (> 0)
    modifyOTVar s (-1+)
```

يمكن أيضاً تركيب الإجراءات كبدائل باستخدام العملية الأساسية `orElse`. على سبيل المثال، يأخذ ما يلي عائلة من العدادات السيمافورية ويقدم إجراءً ينقص واحداً منها، محجوباً فقط إذا لم يكن من الممكن إنقاص أي منها:

```haskell
downAny :: [Sempahore] -> ITM ()
downAny (x:xs) = down x `orElse` downAny xs
downAny [] = retry
```

**التفاعل**

ينتهي التبادل بين OTM و STM عندما يتم إسقاط العزل. في الواقع، توفر OTM OTVars المشتركة كآلية للتفاعل الآمن للمعاملات. هذا يعني أن الإجراءات المعاملاتية غير المعزولة ترى التأثيرات على المتغيرات المشتركة لأي إجراء معاملاتي آخر غير معزول، حيث يتم تنفيذها بشكل متزامن على نفس الكائن. يقدم تدفق المعلومات هذا تبعيات بين الإجراءات المؤقتة المتزامنة تربط مصيرها معاً: لا يمكن لإجراء جعل تأثيراته دائمة، إذا كان يعتمد على معلومات تنتجها إجراء آخر يفشل في الاكتمال. تضمن OTM تماسك الإجراءات المعاملاتية في وجود التفاعل من خلال المتغيرات المعاملاتية المشتركة. وبالتالي، تمكّن OTVars التفاعل ضعيف الاقتران داخل الإجراءات الذرية مباشرة، مما يأخذ نمط البرمجة لـ STM خطوة إلى الأمام. على سبيل المثال، يمكن أن يكون الاتصال، والموعد، والوساطة، وبشكل عام، التفاعلات متعددة الأطراف جميعها إجراءات ذرية (غير معزولة).

من أجل إثبات هذه الادعاءات، دعونا نرى المعاملات المفتوحة في العمل من خلال تنفيذ سيناريو مزامنة كما هو موضح في القسم 1. في هذا المثال، تقوم عملية رئيسية بالاستعانة بمصادر خارجية لجزء من حوسبة ذرية إلى بعض الخيوط المختارة من مجموعة عمال؛ يتم تبادل البيانات عبر بعض المتغيرات المشتركة، والتي يتم تنسيق الوصول إليها بواسطة زوج من العدادات السيمافورية. بشكل ملحوظ، يمكن لكل من الرئيس والعامل إحباط الحوسبة في أي وقت، مما يؤدي إلى إحباط الطرف الآخر أيضاً. يمكن تحقيق ذلك بشكل مباشر باستخدام OTM:

```haskell
master c1 c2 = do               worker c1 c2 = do
    -- وضع الطلب                     -- القيام بشيء ما
    isolated (up c1)                isolated (down c1)
    -- القيام بشيء آخر                -- الحصول على الطلب
    isolated (down c2)              -- وضع الإجابة
    -- الحصول على الإجابة              isolated (up c2)
```

كلتا الدالتين تقدمان إجراءات ذرية في `OTM`، وبالتالي فهي غير معزولة. استخدمنا العدادات السيمافورية لغرض التوضيح ولكن يمكننا المزامنة باستخدام آليات أكثر تجريداً، مثل الحواجز، أو القنوات، أو المستقبليات، والتي يمكن تنفيذها باستخدام OTM.

**التزامن**

بشكل مختلف عن STM، تدعم OTM التوازي داخل المعاملات غير المعزولة. يمكننا بسهولة تفريع خيوط جديدة دون مغادرة `OTM` ولكن، مثل أي تأثير لإجراء معاملاتي، يبقى إنشاء الخيط وتنفيذه مؤقتاً حتى تلتزم المعاملة بأكملها. تشارك الخيوط المفرّعة في معاملتها وتؤثر على دورة حياتها (على سبيل المثال إصدار الإحباطات) مثل أي مشارك آخر. هذا يعني أنه قبل الالتزام، يجب على جميع الخيوط المفرّعة إكمال إجراءها المعاملاتي، أي الإنهاء. لذلك، على الرغم من أن التأثير الكامل الذي قدمته المعاملة قد حدث بشكل متزامن، فإن الخيوط المفرّعة لا تغادر المعاملة حية أبداً.

بسبب طبيعتها المعاملاتية، الخيوط المفرّعة داخل معاملة ليس لديها تعويضات ولا استمرارات (أي إجراءات إدخال/إخراج يتم تنفيذها بعد الإحباط أو بعد الالتزام). التعويضات لا جدوى منها لأن الإحباطات تعكس جميع التأثيرات بما في ذلك إنشاء الخيط. من الممكن بالفعل استبدال العملية الأساسية `fork` بواحدة تدعم إجراءات الإدخال/الإخراج كاستمرارات مثل

```haskell
forkCont :: OTM a -> (a -> IO ()) -> OTM ThreadID
```

في الواقع، يمكن تنفيذ هذه الآلية باستخدام العمليات الأساسية التي توفرها OTM بالفعل: نظراً لأن الالتزامات هي نقاط مزامنة، فإن ما سبق يتوافق مع قيام الخيط الأصل بتفريع خيط لكل استمرار، بعد الانتهاء بنجاح من الإجراء الذري.

من ناحية أخرى، بحكم التعريف، يجب أن تظهر الإجراءات الذرية المعزولة كما لو تم تنفيذها في إعداد أحادي الخيط؛ وبالتالي فإن `ITM`، مثل `STM`، لا يدعم إنشاء الخيوط.

---

### Translation Notes

- **Figures referenced:** Figure 1 (base interface of OTM)
- **Key terms introduced:**
  - Irreversible effects → تأثيرات غير قابلة للعكس
  - Monadic binders → روابط الموناد
  - Tentative effects → التأثيرات المؤقتة
  - Pre-condition → شرط مسبق
  - Rendezvous → الموعد
  - Brokering → الوساطة
  - Multi-party interactions → التفاعلات متعددة الأطراف
  - Worker pool → مجموعة عمال
  - Barriers → الحواجز
  - Futures → المستقبليات
  - Compensations → تعويضات
  - Continuations → استمرارات
  - Synchronisation points → نقاط مزامنة

- **Equations:** None

- **Citations:**
  - [hmpm:ppopp2005]

- **Special handling:**
  - All Haskell code preserved in English
  - Type signatures and function names kept as-is
  - Code comments translated in Arabic version

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
