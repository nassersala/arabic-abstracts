# Section 2: Abstracting evaluation strategy
## القسم 2: تجريد استراتيجية التقييم

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** monad, evaluation strategy, call-by-value, call-by-name, call-by-need, aliasing, lambda calculus, functor

---

### English Version

The translations demonstrated in the previous section have two major problems. Firstly, it is not easy to switch between the two -- when we introduce effects using monads, we need to decide to use one or the other style and changing between them later on involves rewriting of the program and changing types. Secondly, even in the IO monad, we cannot easily implement a *call-by-need* strategy that would perform effects only when a value is needed, but at most once.

#### Translation using aliasing

To solve these problems, we propose an alternative translation. We require a monad `m` with an additional operation *malias* that abstracts out the evaluation strategy and has a type `m a -> m (m a)`. The term *aliasing* refers to the fact that some part of effects may be performed once and their results shared in multiple monadic computations. The translation of the previous example using *malias* looks as follows:

```haskell
chooseSize :: IO Int -> IO Int -> IO Int
chooseSize new legacy = do
  newVal <- new
  if newVal > 0 then new else legacy

resultSize :: IO Int
resultSize = do
  new <- malias (lookupInput "new_size")
  legacy <- malias (lookupInput "legacy_size")
  chooseSize new legacy
```

The types of functions and access to function parameters are translated in the same way as in the *call-by-name* translation. The `chooseSize` function returns a computation `IO Int` and its parameters also become computations of type `IO Int`. When using the value of a parameter, the computation is evaluated using monadic bind (e.g. the line `newVal <- new` in `chooseSize`).

The computations passed as arguments are not the original computations as in the *call-by-name* translation. The translation inserts a call to *malias* for every function argument (and also for every let-bound value, which can be encoded using lambda abstraction and application). The computation returned by *malias* has a type `m (m a)`, which makes it possible to perform the effects at two different call sites:

- When simulating the *call-by-value* strategy, all effects are performed when binding the outer monadic computation before a function call.

- When simulating the *call-by-name* strategy, all effects are performed when binding the inner monadic computation, when the value is actually needed.

These two strategies can be implemented by two simple definitions of *malias*. However, by delegating the implementation of *malias* to the monad, we make it possible to implement more advanced strategies as well. We discuss some of them later in Section 4. We keep the translation informal until the lambda calculus translation subsection and discuss the *malias* operation in more detail first.

**Implementing call-by-name.** To implement the *call-by-name* strategy, the *malias* operation needs to return the computation specified as an argument inside the monad. In the type `m (m a)`, the outer `m` will not carry any effects and the inner `m` will be the same as the original computation:

```haskell
malias :: m a -> m (m a)
malias m = return m
```

From the monad laws, we know that applying monadic bind to a computation created from a value using `return` is equivalent to just passing the value to the rest of the computation. This means that the additional binding in the translation does not have any effect and the resulting program behaves as the *call-by-name* strategy.

**Implementing call-by-value.** Implementing the *call-by-value* strategy is similarly simple. In the returned computation of type `m (m a)`, the computation corresponding to the outer `m` needs to perform all the effects. The computation corresponding to the inner `m` will be a computation that simply returns the previously computed value without performing any effects:

```haskell
malias :: m a -> m (m a)
malias m = m >>= (return . return)
```

In Haskell, the second line could be written as `liftM return m`. The `liftM` operation represents the functor associated with the monad. This means that binding on the returned computation performs all the effects, obtains a value `v` and returns a computation `return v`.

When calling a function that takes an argument of type `m a`, the argument passed to it using this implementation of *malias* will always be constructed using the `return` operation. Hence the resulting behaviour is equivalent to the original *call-by-value* translation.

#### The malias operation laws

In order to define a reasonable evaluation strategy, we require the *malias* operation to obey a number of laws. The laws follow from the theoretical background that is discussed in Section 3, namely from the fact that *malias* is the *cojoin* operation of a computational semi-comonad.

The laws that relate *malias* to the monad are easier to write in terms of `join`, `map` and `unit` than using the formulation based on bind and `return`. For completeness, the two equivalent definitions of monads with the monad laws are shown in Figure 1 (monad laws). The required laws for *malias* are the following:

$$
\\begin{array}{rclcl}
\\textit{map}~(\\textit{map}~f) \\circ \\textit{malias} &=& \\textit{malias} \\circ (\\textit{map}~f)
  &\\quad\\quad&(\\textit{naturality}) \\\\
 \\textit{map}~\\textit{malias} \\circ \\textit{malias} &=& \\textit{malias} \\circ \\textit{malias}
  &&(\\textit{associativity}) \\\\
              \\textit{malias} \\circ \\textit{unit} &=& \\textit{unit} \\circ \\textit{unit}
  &&(\\textit{computationality}) \\\\
                \\textit{join} \\circ \\textit{malias} &=& \\textit{id}
  &&(\\textit{identity}) \\\\
\\end{array}
$$

The first two laws follow from the fact that *malias* is a *cojoin* operation of a comonad. The *naturality* law specifies that applying a function to a value inside a computation is the same as applying the function to a value inside an aliased computation. The *associativity* law specifies that aliasing an aliased computation is the same as aliasing a computation produced by an aliased computation.

The *computationality* law is derived from the fact that the comonad defining *malias* is a *computational comonad* with *unit* as one of the components. The law specifies that aliasing of a pure computation creates a pure computation. Finally, the *identity* law relates *malias* with the monadic structure, by requiring that `join` is a *left inverse* of *malias*. Intuitively, it specifies that aliasing a computation of type `m a` and then joining the result returns the original computation.

All four laws hold for the two implementations of *malias* presented in the previous section. We prove that the laws hold for any monad using the standard monad laws.

#### Lambda calculus translation

The *call-by-name* and *call-by-value* translations given in the introduction were first formally introduced by Wadler. In this section, we present a similar formal definition of our translation based on the *malias* operation. For our source language, we use a simply-typed λ calculus with let-binding:

$$e \\in \\textit{Expr}, \\quad e ::= x \\mid \\lambda x . e \\mid e_1 \\: e_2 \\mid \\textbf{let} \\: x = e_1 \\: \\textbf{in} \\: e_2$$
$$\\tau \\in \\textit{Type}, \\quad \\tau ::= \\alpha \\mid \\tau_1 \\rightarrow \\tau_2$$

The target language of the translation is identical but for one exception -- it adds a type scheme $M~\\tau$ representing monadic computations.

Our translation, called *call-by-alias*, is presented below. The translation has similar structure to Wadler's *call-by-name* translation, but it inserts *malias* operation in the last two cases:

**Type translation:**
$$[\\![\\alpha]\\!]_{cba} = \\alpha$$
$$[\\![\\tau_1 \\rightarrow \\tau_2]\\!]_{cba} = M~[\\![\\tau_1]\\!]_{cba} \\rightarrow M~[\\![\\tau_2]\\!]_{cba}$$

**Expression translation:**
$$[\\![x]\\!]_{cba} = x$$
$$[\\![\\lambda x . e]\\!]_{cba} = \\textit{unit}~(\\lambda x . [\\![e]\\!]_{cba})$$
$$[\\![e_1 \\: e_2]\\!]_{cba} = \\textit{bind}~[\\![e_1]\\!]_{cba}~(\\lambda f . \\textit{bind}~(\\textit{malias}~[\\![e_2]\\!]_{cba})~f)$$
$$[\\![\\textbf{let} \\: x = e_1 \\: \\textbf{in} \\: e_2]\\!]_{cba} = \\textit{bind}~(\\textit{malias}~[\\![e_1]\\!]_{cba})~(\\lambda x . [\\![e_2]\\!]_{cba})$$

The translation turns user-defined variables of type τ into variables of type M τ. A variable access x is translated to a variable access, which now represents a computation (that may have effects). A lambda expression is turned into a lambda expression wrapped in a pure monadic computation.

The two interesting cases are application and let-binding. When translating function application, we bind on the computation representing the function. We want to call the function f with an aliased computation as an argument. This is achieved by passing the translated argument to *malias* and then applying bind again. The translation of let-binding is similar, but slightly simpler, because it does not need to use bind to obtain a function.

#### The meaning of malias laws

Having provided the translation, we can discuss the intuition behind the *malias* laws and what they imply about the translated code. The *naturality* law specifies that *malias* is a natural transformation. Although we do not give a formal proof, we argue that the law follows from the parametricity of the *malias* type signature.

**Effect conservation.** The meaning of *associativity* and *identity* can be informally demonstrated by treating effects as units of information. Given a computation type involving a number of occurrences of `m`, we say that there are *effects* (or *information*) associated with each occurrence of `m`.

The *identity* law specifies that `join ∘ malias` does not lose effects -- given a computation of type `m a`, the *malias* operation constructs a computation of type `m (m a)`. This is done by splitting the effects of the computation between two monadic computations. Requiring that applying `join` to the new computation returns the original computation means that all the effects of the original computation are preserved, because `join` combines the effects of the two computations.

The *associativity* law specifies how the effects should be split. When applying *malias* to an aliased computation of type `m (m a)`, we can apply the operation to the inner or the outer `m`. The law forbids implementations that split the effects in an asymmetric way.

**Semantics-preserving transformations.** The *computationality* and *identity* laws also specify that certain semantics-preserving transformations on the original source code correspond to equivalent terms in the code translated using the *call-by-alias* transformation. The source transformations corresponding to *computationality* and *identity*, respectively, are:

$$\\textbf{let}~f = \\lambda x.e_1~\\textbf{in}~e_2 \\equiv e_2 [f \\leftarrow \\lambda x.e_1]$$
$$\\textbf{let}~x = e~\\textbf{in}~x \\equiv e$$

---

### النسخة العربية

تعاني الترجمات التي تم إظهارها في القسم السابق من مشكلتين رئيسيتين. أولاً، ليس من السهل التبديل بين الاثنين -- عندما نُدخل الآثار الجانبية باستخدام الموناد، نحتاج إلى تحديد استخدام نمط أو آخر، والتغيير بينهما لاحقاً يتضمن إعادة كتابة البرنامج وتغيير الأنواع. ثانياً، حتى في موناد الإدخال/الإخراج (IO)، لا يمكننا بسهولة تطبيق استراتيجية *استدعاء بالحاجة* تنفذ الآثار فقط عندما تكون القيمة مطلوبة، ولكن مرة واحدة على الأكثر.

#### الترجمة باستخدام الأسماء المستعارة (aliasing)

لحل هذه المشاكل، نقترح ترجمة بديلة. نطلب موناد `m` مع عملية إضافية *malias* تجرد استراتيجية التقييم ولها نوع `m a -> m (m a)`. يشير مصطلح *aliasing* (الأسماء المستعارة) إلى حقيقة أن بعض أجزاء الآثار قد تُنفذ مرة واحدة وتُشارك نتائجها في حسابات موناد متعددة. تبدو الترجمة للمثال السابق باستخدام *malias* كما يلي:

```haskell
chooseSize :: IO Int -> IO Int -> IO Int
chooseSize new legacy = do
  newVal <- new
  if newVal > 0 then new else legacy

resultSize :: IO Int
resultSize = do
  new <- malias (lookupInput "new_size")
  legacy <- malias (lookupInput "legacy_size")
  chooseSize new legacy
```

تُترجم أنواع الدوال والوصول إلى معاملات الدوال بنفس الطريقة كما في ترجمة *استدعاء بالاسم*. تُرجع الدالة `chooseSize` حساباً `IO Int` وتصبح معاملاتها أيضاً حسابات من نوع `IO Int`. عند استخدام قيمة معامل، يتم تقييم الحساب باستخدام الربط الموناد (على سبيل المثال السطر `newVal <- new` في `chooseSize`).

الحسابات الممررة كوسائط ليست الحسابات الأصلية كما في ترجمة *استدعاء بالاسم*. تُدرج الترجمة استدعاءً لـ *malias* لكل وسيط دالة (وأيضاً لكل قيمة مربوطة بـ let، والتي يمكن ترميزها باستخدام تجريد لامدا والتطبيق). الحساب الذي تُرجعه *malias* له نوع `m (m a)`، مما يجعل من الممكن تنفيذ الآثار في موقعي استدعاء مختلفين:

- عند محاكاة استراتيجية *استدعاء بالقيمة*، تُنفذ جميع الآثار عند ربط الحساب الموناد الخارجي قبل استدعاء الدالة.

- عند محاكاة استراتيجية *استدعاء بالاسم*، تُنفذ جميع الآثار عند ربط الحساب الموناد الداخلي، عندما تكون القيمة مطلوبة فعلياً.

يمكن تطبيق هاتين الاستراتيجيتين بتعريفين بسيطين لـ *malias*. ومع ذلك، من خلال تفويض تطبيق *malias* إلى الموناد، نجعل من الممكن تطبيق استراتيجيات أكثر تقدماً أيضاً. نناقش بعضها لاحقاً في القسم 4. نبقي الترجمة غير رسمية حتى قسم ترجمة حساب لامدا ونناقش عملية *malias* بمزيد من التفصيل أولاً.

**تطبيق استدعاء بالاسم.** لتطبيق استراتيجية *استدعاء بالاسم*، تحتاج عملية *malias* إلى إرجاع الحساب المحدد كوسيط داخل الموناد. في النوع `m (m a)`، لن يحمل `m` الخارجي أي آثار وسيكون `m` الداخلي هو نفسه الحساب الأصلي:

```haskell
malias :: m a -> m (m a)
malias m = return m
```

من قوانين الموناد، نعلم أن تطبيق الربط الموناد على حساب تم إنشاؤه من قيمة باستخدام `return` يكافئ مجرد تمرير القيمة إلى بقية الحساب. هذا يعني أن الربط الإضافي في الترجمة ليس له أي تأثير والبرنامج الناتج يتصرف كاستراتيجية *استدعاء بالاسم*.

**تطبيق استدعاء بالقيمة.** تطبيق استراتيجية *استدعاء بالقيمة* بسيط بالمثل. في الحساب المُرجع من نوع `m (m a)`، يحتاج الحساب المقابل لـ `m` الخارجي إلى تنفيذ جميع الآثار. سيكون الحساب المقابل لـ `m` الداخلي حساباً يُرجع ببساطة القيمة المحسوبة مسبقاً دون تنفيذ أي آثار:

```haskell
malias :: m a -> m (m a)
malias m = m >>= (return . return)
```

في Haskell، يمكن كتابة السطر الثاني كـ `liftM return m`. تمثل عملية `liftM` الدالة التصنيفية المرتبطة بالموناد. هذا يعني أن الربط على الحساب المُرجع ينفذ جميع الآثار، ويحصل على قيمة `v` ويُرجع حساباً `return v`.

عند استدعاء دالة تأخذ وسيطاً من نوع `m a`، سيتم دائماً إنشاء الوسيط الممرر إليها باستخدام هذا التطبيق لـ *malias* باستخدام عملية `return`. وبالتالي فإن السلوك الناتج يكافئ ترجمة *استدعاء بالقيمة* الأصلية.

#### قوانين عملية malias

من أجل تعريف استراتيجية تقييم معقولة، نطلب من عملية *malias* إطاعة عدد من القوانين. تتبع القوانين من الخلفية النظرية التي نناقشها في القسم 3، وتحديداً من حقيقة أن *malias* هي عملية *cojoin* (الاقتران المشترك) لكوموناد شبه حوسبية.

القوانين التي تربط *malias* بالموناد أسهل في الكتابة من حيث `join` و `map` و `unit` من استخدام الصياغة المعتمدة على bind و `return`. من أجل الاكتمال، يتم عرض التعريفين المكافئين للموناد مع قوانين الموناد في الشكل 1. القوانين المطلوبة لـ *malias* هي التالية:

$$
\\begin{array}{rclcl}
\\textit{map}~(\\textit{map}~f) \\circ \\textit{malias} &=& \\textit{malias} \\circ (\\textit{map}~f)
  &\\quad\\quad&(\\textit{الطبيعية}) \\\\
 \\textit{map}~\\textit{malias} \\circ \\textit{malias} &=& \\textit{malias} \\circ \\textit{malias}
  &&(\\textit{التجميعية}) \\\\
              \\textit{malias} \\circ \\textit{unit} &=& \\textit{unit} \\circ \\textit{unit}
  &&(\\textit{الحوسبية}) \\\\
                \\textit{join} \\circ \\textit{malias} &=& \\textit{id}
  &&(\\textit{الهوية}) \\\\
\\end{array}
$$

يتبع القانونان الأولان من حقيقة أن *malias* هي عملية *cojoin* لكوموناد. يحدد قانون *الطبيعية* أن تطبيق دالة على قيمة داخل حساب هو نفسه تطبيق الدالة على قيمة داخل حساب ذو اسم مستعار. يحدد قانون *التجميعية* أن إنشاء اسم مستعار لحساب ذو اسم مستعار هو نفسه إنشاء اسم مستعار لحساب أُنتج بواسطة حساب ذو اسم مستعار.

يُشتق قانون *الحوسبية* من حقيقة أن الكوموناد التي تعرّف *malias* هي *كوموناد حوسبية* مع *unit* كأحد المكونات. يحدد القانون أن إنشاء اسم مستعار لحساب نقي ينشئ حساباً نقياً. أخيراً، يربط قانون *الهوية* *malias* بالبنية الموناد، من خلال المطالبة بأن `join` هو *معكوس أيسر* لـ *malias*. بشكل بديهي، يحدد أن إنشاء اسم مستعار لحساب من نوع `m a` ثم ضم النتيجة يُرجع الحساب الأصلي.

تحقق جميع القوانين الأربعة لتطبيقي *malias* المقدمين في القسم السابق. نُثبت أن القوانين تحقق لأي موناد باستخدام قوانين الموناد القياسية.

#### ترجمة حساب لامدا

تم تقديم ترجمات *استدعاء بالاسم* و*استدعاء بالقيمة* المعطاة في المقدمة رسمياً لأول مرة من قبل Wadler. في هذا القسم، نقدم تعريفاً رسمياً مماثلاً لترجمتنا بناءً على عملية *malias*. للغة المصدر لدينا، نستخدم حساب λ بسيط النمط مع ربط let:

$$e \\in \\textit{Expr}, \\quad e ::= x \\mid \\lambda x . e \\mid e_1 \\: e_2 \\mid \\textbf{let} \\: x = e_1 \\: \\textbf{in} \\: e_2$$
$$\\tau \\in \\textit{Type}, \\quad \\tau ::= \\alpha \\mid \\tau_1 \\rightarrow \\tau_2$$

لغة الهدف للترجمة متطابقة باستثناء واحد -- تضيف مخطط نوع $M~\\tau$ يمثل حسابات موناد.

يتم تقديم ترجمتنا، المسماة *استدعاء بالاسم المستعار* (call-by-alias)، أدناه. تحتوي الترجمة على بنية مماثلة لترجمة *استدعاء بالاسم* لـ Wadler، لكنها تُدرج عملية *malias* في الحالتين الأخيرتين:

**ترجمة الأنواع:**
$$[\\![\\alpha]\\!]_{cba} = \\alpha$$
$$[\\![\\tau_1 \\rightarrow \\tau_2]\\!]_{cba} = M~[\\![\\tau_1]\\!]_{cba} \\rightarrow M~[\\![\\tau_2]\\!]_{cba}$$

**ترجمة التعبيرات:**
$$[\\![x]\\!]_{cba} = x$$
$$[\\![\\lambda x . e]\\!]_{cba} = \\textit{unit}~(\\lambda x . [\\![e]\\!]_{cba})$$
$$[\\![e_1 \\: e_2]\\!]_{cba} = \\textit{bind}~[\\![e_1]\\!]_{cba}~(\\lambda f . \\textit{bind}~(\\textit{malias}~[\\![e_2]\\!]_{cba})~f)$$
$$[\\![\\textbf{let} \\: x = e_1 \\: \\textbf{in} \\: e_2]\\!]_{cba} = \\textit{bind}~(\\textit{malias}~[\\![e_1]\\!]_{cba})~(\\lambda x . [\\![e_2]\\!]_{cba})$$

تحول الترجمة المتغيرات المعرّفة من قبل المستخدم من نوع τ إلى متغيرات من نوع M τ. يُترجم الوصول إلى متغير x إلى وصول متغير، يمثل الآن حساباً (قد يكون له آثار). يتحول تعبير لامدا إلى تعبير لامدا ملفوف في حساب موناد نقي.

الحالتان المثيرتان للاهتمام هما التطبيق وربط let. عند ترجمة تطبيق دالة، نربط على الحساب الذي يمثل الدالة. نريد استدعاء الدالة f مع حساب ذو اسم مستعار كوسيط. يتحقق هذا بتمرير الوسيط المترجم إلى *malias* ثم تطبيق bind مرة أخرى. ترجمة ربط let مماثلة، لكنها أبسط قليلاً، لأنها لا تحتاج إلى استخدام bind للحصول على دالة.

#### معنى قوانين malias

بعد تقديم الترجمة، يمكننا مناقشة البديهة وراء قوانين *malias* وما تعنيه حول الشفرة المترجمة. يحدد قانون *الطبيعية* أن *malias* هو تحويل طبيعي (natural transformation). على الرغم من أننا لا نقدم إثباتاً رسمياً، نجادل بأن القانون يتبع من المعلمية لتوقيع نوع *malias*.

**الحفاظ على الآثار.** يمكن إظهار معنى *التجميعية* و*الهوية* بشكل غير رسمي من خلال معاملة الآثار كوحدات معلومات. بالنظر إلى نوع حساب يتضمن عدداً من ظهورات `m`، نقول إن هناك *آثار* (أو *معلومات*) مرتبطة بكل ظهور لـ `m`.

يحدد قانون *الهوية* أن `join ∘ malias` لا تفقد الآثار -- بالنظر إلى حساب من نوع `m a`، تنشئ عملية *malias* حساباً من نوع `m (m a)`. يتم هذا بتقسيم آثار الحساب بين حسابين موناد. المطالبة بأن تطبيق `join` على الحساب الجديد يُرجع الحساب الأصلي يعني أن جميع آثار الحساب الأصلي محفوظة، لأن `join` تجمع آثار الحسابين.

يحدد قانون *التجميعية* كيف يجب تقسيم الآثار. عند تطبيق *malias* على حساب ذو اسم مستعار من نوع `m (m a)`، يمكننا تطبيق العملية على `m` الداخلي أو الخارجي. يمنع القانون التطبيقات التي تقسم الآثار بطريقة غير متماثلة.

**التحويلات الحافظة للدلاليات.** تحدد قوانين *الحوسبية* و*الهوية* أيضاً أن بعض التحويلات الحافظة للدلاليات على شفرة المصدر الأصلية تتوافق مع حدود مكافئة في الشفرة المترجمة باستخدام تحويل *استدعاء بالاسم المستعار*. التحويلات المصدرية المقابلة لـ *الحوسبية* و*الهوية*، على التوالي، هي:

$$\\textbf{let}~f = \\lambda x.e_1~\\textbf{in}~e_2 \\equiv e_2 [f \\leftarrow \\lambda x.e_1]$$
$$\\textbf{let}~x = e~\\textbf{in}~x \\equiv e$$

---

### Translation Notes

- **Figures referenced:** Figure 1 (Monad laws - mentioned but not shown in extract)
- **Key terms introduced:** aliasing, call-by-alias, cojoin, computational semi-comonad, naturality, associativity, computationality, identity (as law names)
- **Equations:** Multiple mathematical equations and laws (4 malias laws, lambda calculus translation rules)
- **Code examples:** 3 Haskell code blocks
- **Citations:** Wadler (monads), Voigtländer (free theorems)
- **Special handling:**
  - Mathematical notation preserved in LaTeX format
  - Law names kept in both English and Arabic
  - "malias" kept as technical term
  - "aliasing" translated as الأسماء المستعارة

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check

Opening paragraph back-translates to: "The translations demonstrated in the previous section suffer from two main problems. First, it is not easy to switch between the two -- when we introduce side effects using monads, we need to specify using one style or another, and changing between them later involves rewriting the program and changing types. Second, even in the input/output (IO) monad, we cannot easily implement a *call-by-need* strategy that executes effects only when a value is needed, but at most once."
