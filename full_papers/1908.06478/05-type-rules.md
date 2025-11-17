# Section 5: Type Rules
## القسم 5: قواعد الأنواع

**Section:** type-rules
**Translation Quality:** 0.85
**Glossary Terms Used:** type system, inference rules, type judgment, linear constraints, type equality, polymorphism

---

### English Version

In this section, we will give an overview over the adapted type rules used in our implementation. However, note that we abstain from reciting a large portion of the rules and definitions which we reuse from the original JVFH system without modification. Instead, please refer to the original publication by Jost et al. [9]

The following types of judgments are used in both the JVFH and our type system:

• The **typing judgment** Γ ⊢^p_q e : T states that, given context Γ, expression e has type T. Additionally, p is an upper bound on the number of resources required to evaluate e to weak head normal form; and q is a lower bound on the number of resources that are available after this evaluation.

Among the type rules that can be applied to these judgments, we distinguish between **syntax driven rules** and **structural rules**. The latter serve various difference purposes; For example, the PREPAY rule can be used to pay the thunk cost of any variable only once, even if the variable is used multiple times in the expression; And the RELAX rule allows us to increase the over-approximation of the cost upper bounds in a typing judgment on purpose, thereby relaxing linear constraints which otherwise might render the linear program unsolvable. While the purpose of the various structural type rules vary widely, they have in common that they can be applied to any typing judgment, regardless of the expression. This means that we can reuse these rules in our system without any modifications.

The syntax driven rules can only be applied to typing judgments with specific expressions. Many of these rules contain cost constants, which can be set by the user; The basic goal of the type system is to count how often certain kinds of expressions are executed, and to add up the cost constants associated with these expressions. For example, if we set the cost constants associated with any expressions involving variable bindings to 1, and the remaining constants to 0, our analysis will derive an upper bound on the number of memory allocations required to evaluate an expression. However, as these type rules directly depend on the available expressions of the language and their syntax, the original JVFH rules cannot be applied to GHC Core without modifications. We will elaborate on how we adapted these rules for Core in the second half of this section.

• The **type equality judgment** T₁ = T₂ is used to unify two types T₁ and T₂.

• The **Sharing judgment** T ▷ {T₁, T₂} enforces that all types have the same structure, but may have different type annotations within certain limitations. Most importantly, we enforce that the potential in the left hand side is greater or equal the sum of the potentials in the right hand side; In other words, the potential of T is "shared" between T₁ and T₂.

This property is used to ensure that potential can be redeemed only once. For example, consider a typing judgment Γ, x:X ⊢^p_q e : T, where the variable x appears in expression e multiple times. In a non-affine system, this would mean that any potential in X could be redeemed once for each occurrence. But in our system, we instead use Sharing to split up the potential of X between several subtypes Xᵢ which are then assigned to the various instances of x in e.

Note that the Sharing relation is defined for any number of types on the right hand side; In fact, the subtype relation T₁ <: T₂ is defined as a shorthand for T₁ ▷ {T₂}, a Sharing relation with only one type on the right hand side.

As the Sharing judgment is a relation between different types and does not depend on the language syntax at all, we reuse the inference rules provided for JVFH [9] without any modifications.

• The judgment T₁ ⊳ T₂ is another relation between different types and therefore can also be reused in our implementation without modifications. Just like Sharing, this judgment forces both T₁ and T₂ to have the same structure while giving some leeway to the type annotations. In particular, if T₁ and T₂ are some algebraic type µX. {···}, then all recursive references T^q(X) within T₁ may have reduced thunk costs – even zero – compared to their counterparts in T₂. This is used as an optimization when analyzing recursive variable definitions, where we can assume that these thunks have already been evaluated. However, as we will discuss shortly, there were concerns about the correctness of this assumption and the operator is currently not used in our implementation.

• The final kind of judgment in our system is **linear constraints** such as v₁·c₁ +...+ vₙ·cₙ ≤ c₀, where vᵢ are numerical variables and cᵢ are constants. We collect every linear constraint that comes up during the analysis into a single linear program, which is then passed to the LP solver.

As illustrated in this list, only the syntax driven type rules actually require modifications for GHC Core. In the remainder of this section, we will list our adapted type rules and explain why and how they were modified. For the original type rules, please refer to the original paper on JVFH [9] and the bachelor's thesis that introduced the type rule for mutually recursive definitions [10].

Even among the syntax driven type rules, several rules could be reused with minor or no modifications, due to overlaps between the JVFH and GHC Core languages. As depicted in Figure 4, these encompass variables, abstraction, applying functions to variables, and recursive variable bindings. Functionally, these four rules are identical to their respective counterparts in the JVFH systems. However, the rules were renamed from VAR, ABS, APP and LETAND† to VAR_GC, ABS_GC, APPVAR_GC and LETREC_GC; And the latter has been adjusted for the minor syntactical differences between the JVFH letand and the Core letrec expressions.

**Figure 4:** Unmodified syntax driven type rules (VAR_GC, ABS_GC, APPVAR_GC, LETREC_GC)

[Mathematical inference rules preserved in original notation]

However, LETREC_GC is also noteworthy as it is the only inference rule in our adapted type system that makes use of the ⊳ operator. There exists a soundness proof of this rule [10], indicating that the usage of this operator should be correct; But during our tests, we encountered a counter-example where this rule does allow for under-approximation:

```haskell
letrec zipWith = ··· in let one = ··· in let zero = ··· in
letrec fibs = Cons zero fibs1 ;
       fibs1 = Cons one fibs2 ;
       fibs2 = zipWith (+)_Int fibs fibs1
in fibs
```

For this (abridged) expression, which evaluates to an infinite list of Fibonacci numbers, our analysis was able to derive a list type with constant costs. This is due to the ⊳ operator in the LETREC_GC type rule, which allows us to treat the reference to fibs2 in the definition of fibs1 as if it had constant cost. However, this is clearly incorrect – fibs2 is an infinite list which can never be fully evaluated, so the cost of the list has to be linear at least. To work around this issue, we have disabled the ⊳ operator for now and simply use type unification in its place. With this modification, our implementation will fail to analyze the code above, as the generated linear program is now unsolvable. However, conceding failure is preferable to returning incorrect results.

In Figure 5, we list several rules which required larger modifications from the JVFH type system:

**Figure 5:** Modified type rules (APP_GC, CONS_GC, LET_GC, LIT_GC)

[Mathematical inference rules preserved in original notation]

The application rule APP_GC is a generalization of the original APP rule. In JVFH, the arguments of function applications always have to be variables, but in GHC Core, this is not necessarily the case. Therefore, we adapted this rule to allow for any expression in the argument. However, if the argument actually is a variable, using this generalized rule can artificially increase the thunk cost of the variable. In those cases, we instead use the previously mentioned APPVAR_GC rule, which is an unmodified copy of the original APP rule, to prevent this undesired side-effect.

CONS_GC can be considered a replacement of the original LETCONS and CONS rules. JVFH handles structure allocation via a letcons expression, which fulfills multiple purposes at once: First, it fully applies the constructor to all of its arguments; This is simple, because all arguments have to be variables, so this can be done by looking up their types in the context. In GHC Core, the arguments can be more complex, so we defer handling the arguments to the APP_GC and APPVAR_GC rules instead. Second, the resulting structure is immediately bound to a variable in JVFH. However, in GHC Core, a structure can sometimes be used immediately without binding it to a variable first. This is generally the case when the constructor does not have any fields, such as the "empty list" constructor of a list type. Because of these differences, we chose to process constructors individually, instead of aggregating them with surrounding application and binding expressions.

The LET_GC rule is a simplified version of the original LET† rule. Unlike JVFH, the let expression in GHC Core does not support recursive definitions – the letrec expression has to be used instead. Our rule was adapted to reflect this difference.

LIT_GC is an entirely new rule introduced to type literals. As we do not distinguish between different primitive types such as Int#, Float# or Char#, we simply type these as the empty algebraic type µX.{}.

The rules in Figure 6 cover two different kinds of pattern matches, namely on algebraic types and on primitive types:

**Figure 6:** Adapted type rules for case expressions (CASEALG_GC, CASELIT_GC)

[Mathematical inference rules preserved in original notation]

CASEALG_GC was extended from the original MATCH rule to account for some additional features of Core's case expression which are not available to JVFH's match; Namely, binding the value of the scrutinee to a variable, and an additional default case which is used when none of the other cases match.

CASELIT_GC, then, was heavily simplified from our own CASEALG_GC rule, as primitive types cannot have fields and as we do not distinguish between different primitive values.

Finally, we introduced the rules listed in Figure 7, which offer very limited support for type abstraction and type application. Unfortunately, as mentioned earlier, our type system currently does not support polymorphism yet, as this feature is also missing in JVFH, and extending the type system with major new features was not within the scope of our work. Instead, we opted to simply "ignore" type abstraction and application for now.

**Figure 7:** New type rules for handling type expressions (TYABS_GC, TYAPP_GC, TYLET_GC)

[Mathematical inference rules preserved in original notation]

To see why this can be convenient, consider the repeat example discussed earlier:
```haskell
repeat x = let xs = x : xs in xs
it = repeat 1 :: [Int]
```

We do not explicitly specify a type for the function repeat; Therefore, GHC will automatically infer the polymorphic type "forall a. a -> [a]" and introduce the appropriate type abstractions and applications into the generated Core code. Without our type rules from Figure 7, our analysis would fail when it encounters any of these expressions. However, if we instead simply ignore them, we will then unify the type variable a with Int, which essentially turns the function into a monomorphic function of type "Int -> [Int]". An additional wrapper µX.{} →^0 C around the actual type C is introduced as an annotation to inform the user about any ignored type abstractions.

However, this should be considered a workaround, and will only work if every polymorphic function is used monomorphically. If it is used polymorphically, this will lead to the unification of two incompatible types; And if it is never used at all, the resulting type will contain free type variables, which is not valid in our system.

---

### النسخة العربية

في هذا القسم، سنقدم نظرة عامة على قواعد الأنواع المكيّفة المستخدمة في تطبيقنا. ومع ذلك، لاحظ أننا نمتنع عن تكرار جزء كبير من القواعد والتعريفات التي نعيد استخدامها من نظام JVFH الأصلي دون تعديل. بدلاً من ذلك، يرجى الرجوع إلى المنشور الأصلي بواسطة Jost وزملائه [9].

تُستخدم الأنواع التالية من الأحكام في كل من JVFH ونظام الأنواع لدينا:

• **حكم التنميط** Γ ⊢^p_q e : T ينص على أنه، بالنظر إلى السياق Γ، فإن التعبير e له النوع T. بالإضافة إلى ذلك، p هو حد أعلى على عدد الموارد المطلوبة لتقييم e إلى الشكل الطبيعي الضعيف للرأس؛ و q هو حد أدنى على عدد الموارد المتاحة بعد هذا التقييم.

من بين قواعد الأنواع التي يمكن تطبيقها على هذه الأحكام، نميز بين **القواعد المدفوعة بالصياغة** و **القواعد الهيكلية**. تخدم الأخيرة أغراضاً مختلفة متنوعة؛ على سبيل المثال، يمكن استخدام قاعدة PREPAY لدفع تكلفة الثانك لأي متغير مرة واحدة فقط، حتى لو تم استخدام المتغير عدة مرات في التعبير؛ وتسمح لنا قاعدة RELAX بزيادة المبالغة في التقريب للحدود العليا للتكلفة في حكم التنميط عن قصد، وبالتالي تخفيف القيود الخطية التي قد تجعل البرنامج الخطي غير قابل للحل. بينما يختلف الغرض من قواعد الأنواع الهيكلية المختلفة على نطاق واسع، فإن ما لديها مشترك هو أنه يمكن تطبيقها على أي حكم تنميط، بغض النظر عن التعبير. وهذا يعني أنه يمكننا إعادة استخدام هذه القواعد في نظامنا دون أي تعديلات.

يمكن تطبيق القواعد المدفوعة بالصياغة فقط على أحكام التنميط ذات التعبيرات المحددة. تحتوي العديد من هذه القواعد على ثوابت تكلفة، يمكن تعيينها من قبل المستخدم؛ الهدف الأساسي لنظام الأنواع هو حساب عدد المرات التي يتم فيها تنفيذ أنواع معينة من التعبيرات، وجمع ثوابت التكلفة المرتبطة بهذه التعبيرات. على سبيل المثال، إذا قمنا بتعيين ثوابت التكلفة المرتبطة بأي تعبيرات تتضمن روابط متغيرات إلى 1، والثوابت المتبقية إلى 0، فسيشتق تحليلنا حداً أعلى على عدد تخصيصات الذاكرة المطلوبة لتقييم تعبير. ومع ذلك، نظراً لأن قواعد الأنواع هذه تعتمد بشكل مباشر على التعبيرات المتاحة للغة وصياغتها، فلا يمكن تطبيق قواعد JVFH الأصلية على GHC Core دون تعديلات. سنوضح كيف قمنا بتكييف هذه القواعد لـ Core في النصف الثاني من هذا القسم.

• **حكم مساواة الأنواع** T₁ = T₂ يُستخدم لتوحيد نوعين T₁ و T₂.

• **حكم المشاركة** T ▷ {T₁, T₂} يفرض أن جميع الأنواع لها نفس البنية، ولكن قد يكون لها تعليمات أنواع مختلفة ضمن قيود معينة. والأهم من ذلك، نفرض أن الإمكانية في الجانب الأيسر أكبر من أو تساوي مجموع الإمكانيات في الجانب الأيمن؛ بعبارة أخرى، يتم "مشاركة" إمكانية T بين T₁ و T₂.

تُستخدم هذه الخاصية لضمان إمكانية استرداد الإمكانية مرة واحدة فقط. على سبيل المثال، لننظر إلى حكم تنميط Γ, x:X ⊢^p_q e : T، حيث يظهر المتغير x في التعبير e عدة مرات. في نظام غير أفيني، سيعني هذا أنه يمكن استرداد أي إمكانية في X مرة واحدة لكل ظهور. لكن في نظامنا، نستخدم بدلاً من ذلك المشاركة لتقسيم إمكانية X بين عدة أنواع فرعية Xᵢ والتي يتم تعيينها بعد ذلك إلى الحالات المختلفة من x في e.

لاحظ أن علاقة المشاركة معرّفة لأي عدد من الأنواع على الجانب الأيمن؛ في الواقع، يتم تعريف علاقة النوع الفرعي T₁ <: T₂ كاختصار لـ T₁ ▷ {T₂}، وهي علاقة مشاركة مع نوع واحد فقط على الجانب الأيمن.

نظراً لأن حكم المشاركة هو علاقة بين أنواع مختلفة ولا يعتمد على صياغة اللغة على الإطلاق، فإننا نعيد استخدام قواعد الاستنتاج المقدمة لـ JVFH [9] دون أي تعديلات.

• الحكم T₁ ⊳ T₂ هو علاقة أخرى بين أنواع مختلفة وبالتالي يمكن أيضاً إعادة استخدامه في تطبيقنا دون تعديلات. تماماً مثل المشاركة، يفرض هذا الحكم على كل من T₁ و T₂ أن يكون لهما نفس البنية مع إعطاء بعض المرونة لتعليمات الأنواع. على وجه الخصوص، إذا كان T₁ و T₂ نوعاً جبرياً µX. {···}، فقد يكون لجميع المراجع التكرارية T^q(X) داخل T₁ تكاليف ثانك منخفضة - حتى صفر - مقارنة بنظيراتها في T₂. يُستخدم هذا كتحسين عند تحليل تعريفات المتغيرات التكرارية، حيث يمكننا افتراض أن هذه الثانكات قد تم تقييمها بالفعل. ومع ذلك، كما سنناقش قريباً، كانت هناك مخاوف بشأن صحة هذا الافتراض والمُعامل غير مستخدم حالياً في تطبيقنا.

• النوع الأخير من الأحكام في نظامنا هو **القيود الخطية** مثل v₁·c₁ +...+ vₙ·cₙ ≤ c₀، حيث vᵢ هي متغيرات عددية و cᵢ هي ثوابت. نجمع كل قيد خطي يظهر أثناء التحليل في برنامج خطي واحد، والذي يتم بعد ذلك تمريره إلى حلّال البرمجة الخطية.

كما هو موضح في هذه القائمة، فقط القواعد المدفوعة بالصياغة تتطلب فعلياً تعديلات لـ GHC Core. في بقية هذا القسم، سنسرد قواعد الأنواع المكيّفة ونشرح لماذا وكيف تم تعديلها. بالنسبة لقواعد الأنواع الأصلية، يرجى الرجوع إلى الورقة الأصلية حول JVFH [9] ورسالة البكالوريوس التي قدمت قاعدة الأنواع للتعريفات المتبادلة التكرارية [10].

حتى بين القواعد المدفوعة بالصياغة، يمكن إعادة استخدام عدة قواعد مع تعديلات طفيفة أو بدونها، بسبب التداخلات بين لغات JVFH و GHC Core. كما هو موضح في الشكل 4، تشمل هذه المتغيرات والتجريد وتطبيق الدوال على المتغيرات وروابط المتغيرات التكرارية. وظيفياً، هذه القواعد الأربعة متطابقة مع نظيراتها في أنظمة JVFH. ومع ذلك، تمت إعادة تسمية القواعد من VAR و ABS و APP و LETAND† إلى VAR_GC و ABS_GC و APPVAR_GC و LETREC_GC؛ وتم تعديل الأخيرة للاختلافات الصياغية الطفيفة بين تعبير letand في JVFH وتعبير letrec في Core.

**الشكل 4:** قواعد مدفوعة بالصياغة غير معدلة (VAR_GC, ABS_GC, APPVAR_GC, LETREC_GC)

[تم الحفاظ على قواعد الاستنتاج الرياضية بالتدوين الأصلي]

ومع ذلك، فإن LETREC_GC جديرة بالملاحظة أيضاً لكونها قاعدة الاستنتاج الوحيدة في نظام الأنواع المكيّف لدينا التي تستخدم مُعامل ⊳. يوجد إثبات صحة لهذه القاعدة [10]، مما يشير إلى أن استخدام هذا المُعامل يجب أن يكون صحيحاً؛ لكن أثناء اختباراتنا، واجهنا مثالاً مضاداً حيث تسمح هذه القاعدة بالتقليل من التقدير:

```haskell
letrec zipWith = ··· in let one = ··· in let zero = ··· in
letrec fibs = Cons zero fibs1 ;
       fibs1 = Cons one fibs2 ;
       fibs2 = zipWith (+)_Int fibs fibs1
in fibs
```

بالنسبة لهذا التعبير (المختصر)، الذي يُقيّم إلى قائمة لا نهائية من أعداد فيبوناتشي، تمكن تحليلنا من اشتقاق نوع قائمة بتكاليف ثابتة. يرجع ذلك إلى مُعامل ⊳ في قاعدة نوع LETREC_GC، والذي يسمح لنا بمعاملة المرجع إلى fibs2 في تعريف fibs1 كما لو كانت له تكلفة ثابتة. ومع ذلك، هذا غير صحيح بوضوح - fibs2 هي قائمة لا نهائية لا يمكن أبداً تقييمها بالكامل، لذلك يجب أن تكون تكلفة القائمة خطية على الأقل. للتغلب على هذه المشكلة، قمنا بتعطيل مُعامل ⊳ في الوقت الحالي ونستخدم ببساطة توحيد الأنواع في مكانه. مع هذا التعديل، سيفشل تطبيقنا في تحليل الشفرة أعلاه، حيث أصبح البرنامج الخطي المُولّد الآن غير قابل للحل. ومع ذلك، فإن الاعتراف بالفشل أفضل من إرجاع نتائج غير صحيحة.

في الشكل 5، نسرد عدة قواعد تطلبت تعديلات أكبر من نظام أنواع JVFH:

**الشكل 5:** قواعد أنواع معدلة (APP_GC, CONS_GC, LET_GC, LIT_GC)

[تم الحفاظ على قواعد الاستنتاج الرياضية بالتدوين الأصلي]

قاعدة التطبيق APP_GC هي تعميم لقاعدة APP الأصلية. في JVFH، يجب أن تكون معاملات تطبيقات الدوال دائماً متغيرات، لكن في GHC Core، هذا ليس بالضرورة هو الحال. لذلك، قمنا بتكييف هذه القاعدة للسماح بأي تعبير في المعامل. ومع ذلك، إذا كان المعامل في الواقع متغيراً، فإن استخدام هذه القاعدة المعممة يمكن أن يزيد بشكل مصطنع من تكلفة الثانك للمتغير. في تلك الحالات، نستخدم بدلاً من ذلك قاعدة APPVAR_GC المذكورة سابقاً، وهي نسخة غير معدلة من قاعدة APP الأصلية، لمنع هذا التأثير الجانبي غير المرغوب فيه.

يمكن اعتبار CONS_GC بديلاً لقواعد LETCONS و CONS الأصلية. يتعامل JVFH مع تخصيص البنية عبر تعبير letcons، والذي يحقق أغراضاً متعددة في آن واحد: أولاً، يطبق بالكامل المنشئ على جميع معاملاته؛ هذا بسيط، لأن جميع المعاملات يجب أن تكون متغيرات، لذلك يمكن القيام بذلك عن طريق البحث عن أنواعها في السياق. في GHC Core، يمكن أن تكون المعاملات أكثر تعقيداً، لذلك نؤجل التعامل مع المعاملات إلى قواعد APP_GC و APPVAR_GC بدلاً من ذلك. ثانياً، يتم ربط البنية الناتجة على الفور بمتغير في JVFH. ومع ذلك، في GHC Core، يمكن أحياناً استخدام البنية مباشرة دون ربطها بمتغير أولاً. هذا هو الحال بشكل عام عندما لا يكون للمنشئ أي حقول، مثل منشئ "القائمة الفارغة" لنوع قائمة. بسبب هذه الاختلافات، اخترنا معالجة المنشئات بشكل فردي، بدلاً من تجميعها مع تعبيرات التطبيق والربط المحيطة.

قاعدة LET_GC هي نسخة مبسطة من قاعدة LET† الأصلية. على عكس JVFH، لا يدعم تعبير let في GHC Core التعريفات التكرارية - يجب استخدام تعبير letrec بدلاً من ذلك. تم تكييف قاعدتنا لتعكس هذا الاختلاف.

LIT_GC هي قاعدة جديدة تماماً تم إدخالها لأنواع الحرفيات. نظراً لأننا لا نميز بين الأنواع البدائية المختلفة مثل Int# أو Float# أو Char#، فإننا ببساطة ننمّط هذه كنوع جبري فارغ µX.{}.

تغطي القواعد في الشكل 6 نوعين مختلفين من مطابقات الأنماط، وهما على الأنواع الجبرية وعلى الأنواع البدائية:

**الشكل 6:** قواعد أنواع مكيّفة لتعبيرات case (CASEALG_GC, CASELIT_GC)

[تم الحفاظ على قواعد الاستنتاج الرياضية بالتدوين الأصلي]

تم توسيع CASEALG_GC من قاعدة MATCH الأصلية لحساب بعض الميزات الإضافية لتعبير case في Core والتي ليست متاحة لـ match في JVFH؛ وهي ربط قيمة المفحوص بمتغير، وحالة افتراضية إضافية تُستخدم عندما لا تتطابق أي من الحالات الأخرى.

تم بعد ذلك تبسيط CASELIT_GC بشكل كبير من قاعدة CASEALG_GC الخاصة بنا، حيث لا يمكن أن يكون للأنواع البدائية حقول ونظراً لأننا لا نميز بين القيم البدائية المختلفة.

أخيراً، قدمنا القواعد المدرجة في الشكل 7، والتي توفر دعماً محدوداً جداً لتجريد الأنواع وتطبيق الأنواع. لسوء الحظ، كما ذكرنا سابقاً، لا يدعم نظام الأنواع لدينا حالياً تعدد الأشكال بعد، حيث أن هذه الميزة مفقودة أيضاً في JVFH، ولم يكن توسيع نظام الأنواع بميزات جديدة رئيسية ضمن نطاق عملنا. بدلاً من ذلك، اخترنا ببساطة "تجاهل" تجريد الأنواع وتطبيقها في الوقت الحالي.

**الشكل 7:** قواعد أنواع جديدة للتعامل مع تعبيرات الأنواع (TYABS_GC, TYAPP_GC, TYLET_GC)

[تم الحفاظ على قواعد الاستنتاج الرياضية بالتدوين الأصلي]

لنرى لماذا قد يكون هذا ملائماً، لننظر إلى مثال repeat الذي تمت مناقشته سابقاً:
```haskell
repeat x = let xs = x : xs in xs
it = repeat 1 :: [Int]
```

لا نحدد صراحةً نوعاً لدالة repeat؛ لذلك، سيستنتج GHC تلقائياً النوع متعدد الأشكال "forall a. a -> [a]" ويُدخل تجريدات وتطبيقات الأنواع المناسبة في شفرة Core المُولّدة. بدون قواعد الأنواع الخاصة بنا من الشكل 7، سيفشل تحليلنا عندما يواجه أياً من هذه التعبيرات. ومع ذلك، إذا قمنا ببساطة بتجاهلها، فسنقوم بعد ذلك بتوحيد متغير النوع a مع Int، مما يحول الدالة بشكل أساسي إلى دالة أحادية الشكل من النوع "Int -> [Int]". يتم إدخال غلاف إضافي µX.{} →^0 C حول النوع الفعلي C كتعليم لإعلام المستخدم عن أي تجريدات أنواع تم تجاهلها.

ومع ذلك، يجب اعتبار هذا حلاً بديلاً، ولن يعمل إلا إذا تم استخدام كل دالة متعددة الأشكال بشكل أحادي الشكل. إذا تم استخدامها بشكل متعدد الأشكال، فسيؤدي ذلك إلى توحيد نوعين غير متوافقين؛ وإذا لم يتم استخدامها على الإطلاق، فسيحتوي النوع الناتج على متغيرات أنواع حرة، وهو أمر غير صالح في نظامنا.

---

### Translation Notes

- **Figures referenced:** Figure 4, 5, 6, 7 (Type rule inference rules)
- **Key terms introduced:**
  - typing judgment (حكم التنميط)
  - syntax driven rules (قواعد مدفوعة بالصياغة)
  - structural rules (قواعد هيكلية)
  - cost constants (ثوابت التكلفة)
  - type equality (مساواة الأنواع)
  - sharing judgment (حكم المشاركة)
  - linear constraints (قيود خطية)
  - soundness proof (إثبات صحة)
  - counter-example (مثال مضاد)
  - under-approximation (التقليل من التقدير)
  - scrutinee (المفحوص)
  - monomorphic function (دالة أحادية الشكل)
  - free type variables (متغيرات أنواع حرة)
- **Equations:** Multiple formal inference rules and type judgments
- **Citations:** [9, 10]
- **Special handling:**
  - Mathematical notation preserved (⊢, ▷, ⊳, ≤, etc.)
  - Rule names (VAR_GC, ABS_GC, etc.) kept in English
  - Formal inference rules kept in original mathematical notation
  - Code examples in Haskell kept as is

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85

### Back-Translation (Key Complex Paragraph)

**Sharing judgment paragraph:** The Sharing judgment T ▷ {T₁, T₂} enforces that all types have the same structure, but may have different type annotations within certain constraints. Most importantly, we enforce that the possibility on the left side is greater than or equal to the sum of possibilities on the right side; in other words, the possibility of T is "shared" between T₁ and T₂.

This property is used to ensure the possibility can be redeemed only once. For example, let's look at a typing judgment Γ, x:X ⊢^p_q e : T, where the variable x appears in expression e several times. In a non-affine system, this would mean any possibility in X could be redeemed once for each occurrence. But in our system, we instead use Sharing to split the possibility of X between several subtypes Xᵢ which are then assigned to the various instances of x in e.
