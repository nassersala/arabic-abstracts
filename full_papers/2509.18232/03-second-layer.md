# Section 3: Second layer: equivalence classes and equations

## English Version

### 3 Second layer: equivalence classes and equations

Here, we go a step further toward our goal of building a "world" where regular languages have a best representation, both simple and unique. To reach this goal, regular languages are given an integer identifier corresponding to both a short normalized expression and the initial state of a DFA for the language. Original techniques used to make it possible are described here but, to ensure that different regular languages are given different identifiers, the implemented system also uses well-known algorithms for minimizing DFAs [1, 17, 25]. In this section, we focus solely on the new techniques. The new and old methods are used together in Section 4, devoted to experiments, showing that the overall goal is achievable.

A key idea of the approach described below is to maintain a large set of normalized expressions that are systematically simplified and linked to a DFA. This set constitutes a kind of database of regular languages from which useful information can be extracted to efficiently simplify other expressions and compute DFAs for them. In the following, we call this database the **background**.

In Section 3.1, the background is described at a high level, with the main operations required to extend it and maintain its consistency. Section 3.2 deals with its implementation, which is efficient and constitutes the most original and challenging contribution of this document.

### 3.1 High-level description of the background

#### 3.1.1 Content of the background: expressions, equivalence classes, and equations

We define the background as a "mutable" abstract object containing at each moment a finite set of normalized expressions grouped into equivalence classes. The background also contains equations relating expressions in it.

Expressions belonging to the same equivalence class must denote the same regular language. The converse does not hold, in general, although it can be achieved, as shown later in Section 4.2. Moreover, each equivalence class contains a unique best expression, called the **representative** of the class. If E is an expression in the background, we denote the representative of its equivalence class by rep(E). The representatives are chosen in such a way that size(rep(E)) ≤ size(E). The size of an expression can be defined recursively in an obvious way but several variations can be imagined. That is why no strict definition is given here; it will be for the experiments, in Section 4.

**Equations** are constructs of the form E = o + ... + x · Eₓ + ..., where o ∈ {0, 1}, the x are distinct letters, and E and the Eₓ are expressions in the background. We say that E is the **left part** of the equation, while o + ... + x · Eₓ + ... is its **right part**. Notice that, technically, a right part is not a normalized expression but another kind of formal object built with 0 or 1, letters, and normalized expressions. For every equation in the background, it is required that

1. E = rep(E) and Eₓ = rep(Eₓ), for all x.
2. L(E) = L(o) ∪ ... ∪ {x}.L(Eₓ) ∪ ... .

We call these conditions the **invariant of the background**. See Section 3.1.3 for examples. We can see that, intuitively, each equation relates an expression to its direct derivatives but the expressions Eₓ are not necessarily the exact syntactic derivatives of E, with respect to x, as defined in [9]. Let E be an expression belonging to the background. We say that **E has an equation** in the background if rep(E) is the left part of an equation in the background. However, it is not necessarily the case that an expression in the background has an equation. Thus, in general, the number of equations in the background is smaller than the number of expressions. However, this is not always true because some equations may overlap: We say that two different equations in the background **overlap** if either their left parts or their right parts are equal (i.e. syntactically identical). A background containing overlapping equations can be refined by merging some equivalence classes. Otherwise, we say that the background is **reduced**. This desirable property should be enforced as soon as possible but it can be locally violated in some operations, as explained in the next subsection.

Sets of equations in the background can be used to represent deterministic finite automata, as suggested in [7, 9, 13]. We say that a set of equations is **complete** if every expression Eₓ used in the right part of an equation is the left part of an equation in this set. A complete set of equations determines a DFA for all expressions that are the left part of an equation of this set: Left parts are the states and right parts define transition functions to next states and indicate if the corresponding left parts are accepting states or not. If E is the left part of an equation belonging to a complete set of equations, we say that the smallest complete set of equations containing this equation is the **DFA of E** in the background. If E' is another expression such that E = rep(E'), we say that the DFA of E is a **DFA for E'**.

---

## النسخة العربية

### 3 الطبقة الثانية: فئات التكافؤ والمعادلات

هنا، نذهب خطوة أبعد نحو هدفنا المتمثل في بناء "عالم" حيث يكون للغات النظامية تمثيل أفضل، بسيط وفريد في آن واحد. لتحقيق هذا الهدف، تُعطى اللغات النظامية مُعرِّف عدد صحيح يتوافق مع كل من تعبير مُطبَّع قصير والحالة الأولية لآلة ذات حالة محدودة حتمية (DFA) للغة. يتم وصف التقنيات الأصلية المستخدمة لجعل ذلك ممكناً هنا، ولكن لضمان إعطاء لغات نظامية مختلفة مُعرِّفات مختلفة، يستخدم النظام المُطبَّق أيضاً خوارزميات معروفة لتصغير الآلات ذات الحالة المحدودة الحتمية [1، 17، 25]. في هذا القسم، نركز فقط على التقنيات الجديدة. يتم استخدام الطرق الجديدة والقديمة معاً في القسم 4، المخصص للتجارب، مما يُظهر أن الهدف العام قابل للتحقيق.

الفكرة الرئيسية للنهج الموصوف أدناه هي الحفاظ على مجموعة كبيرة من التعبيرات المُطبَّعة التي يتم تبسيطها بشكل منهجي وربطها بآلة ذات حالة محدودة حتمية. تشكل هذه المجموعة نوعاً من قاعدة بيانات اللغات النظامية التي يمكن استخلاص معلومات مفيدة منها لتبسيط تعبيرات أخرى بكفاءة وحساب آلات ذات حالة محدودة لها. في ما يلي، نسمي قاعدة البيانات هذه **الخلفية**.

في القسم 3.1، يتم وصف الخلفية على مستوى عالٍ، مع العمليات الرئيسية المطلوبة لتوسيعها والحفاظ على اتساقها. يتناول القسم 3.2 تطبيقها، وهو فعال ويشكل المساهمة الأكثر أصالة وتحدياً في هذه الوثيقة.

### 3.1 الوصف عالي المستوى للخلفية

#### 3.1.1 محتوى الخلفية: التعبيرات وفئات التكافؤ والمعادلات

نُعرِّف الخلفية ككائن مجرد "قابل للتغيير" يحتوي في كل لحظة على مجموعة محدودة من التعبيرات المُطبَّعة مُجمَّعة في فئات تكافؤ. تحتوي الخلفية أيضاً على معادلات تربط التعبيرات الموجودة فيها.

يجب أن تشير التعبيرات التي تنتمي إلى نفس فئة التكافؤ إلى نفس اللغة النظامية. العكس لا ينطبق، بشكل عام، على الرغم من أنه يمكن تحقيقه، كما هو موضح لاحقاً في القسم 4.2. علاوة على ذلك، تحتوي كل فئة تكافؤ على تعبير أفضل فريد، يُسمى **الممثل** للفئة. إذا كان E تعبيراً في الخلفية، فإننا نشير إلى ممثل فئة التكافؤ الخاصة به بـ rep(E). يتم اختيار الممثلين بحيث يكون size(rep(E)) ≤ size(E). يمكن تعريف حجم التعبير بشكل تكراري بطريقة واضحة، لكن يمكن تصور عدة اختلافات. لهذا السبب لا يُعطى تعريف صارم هنا؛ سيكون ذلك للتجارب، في القسم 4.

**المعادلات** هي بنيات من الشكل E = o + ... + x · Eₓ + ...، حيث o ∈ {0، 1}، والحروف x متميزة، وE وEₓ هي تعبيرات في الخلفية. نقول إن E هو **الجزء الأيسر** من المعادلة، بينما o + ... + x · Eₓ + ... هو **الجزء الأيمن**. لاحظ أنه، من الناحية التقنية، الجزء الأيمن ليس تعبيراً مُطبَّعاً بل نوع آخر من الكائنات الشكلية المبنية بـ 0 أو 1، وحروف، وتعبيرات مُطبَّعة. لكل معادلة في الخلفية، يُطلب أن:

1. E = rep(E) وEₓ = rep(Eₓ)، لجميع x.
2. L(E) = L(o) ∪ ... ∪ {x}.L(Eₓ) ∪ ... .

نسمي هذه الشروط **ثابت الخلفية**. انظر القسم 3.1.3 للأمثلة. يمكننا أن نرى أنه، بشكل بديهي، كل معادلة تربط تعبيراً بمشتقاته المباشرة، لكن التعبيرات Eₓ ليست بالضرورة المشتقات النحوية الدقيقة لـ E، بالنسبة إلى x، كما هو محدد في [9]. لنفترض أن E تعبير ينتمي إلى الخلفية. نقول إن **E له معادلة** في الخلفية إذا كان rep(E) هو الجزء الأيسر من معادلة في الخلفية. ومع ذلك، ليس بالضرورة أن يكون للتعبير في الخلفية معادلة. وبالتالي، بشكل عام، فإن عدد المعادلات في الخلفية أصغر من عدد التعبيرات. ومع ذلك، هذا ليس صحيحاً دائماً لأن بعض المعادلات قد تتداخل: نقول إن معادلتين مختلفتين في الخلفية **تتداخلان** إذا كانت أجزاؤهما اليسرى أو أجزاؤهما اليمنى متساوية (أي متطابقة نحوياً). يمكن تحسين خلفية تحتوي على معادلات متداخلة من خلال دمج بعض فئات التكافؤ. وإلا، نقول إن الخلفية **مُختزلة**. يجب فرض هذه الخاصية المرغوبة في أقرب وقت ممكن، لكن يمكن انتهاكها محلياً في بعض العمليات، كما هو موضح في القسم الفرعي التالي.

يمكن استخدام مجموعات المعادلات في الخلفية لتمثيل الآلات ذات الحالة المحدودة الحتمية، كما هو مقترح في [7، 9، 13]. نقول إن مجموعة معادلات **كاملة** إذا كان كل تعبير Eₓ مستخدم في الجزء الأيمن من معادلة هو الجزء الأيسر من معادلة في هذه المجموعة. تحدد مجموعة كاملة من المعادلات آلة ذات حالة محدودة حتمية لجميع التعبيرات التي هي الجزء الأيسر من معادلة في هذه المجموعة: الأجزاء اليسرى هي الحالات، والأجزاء اليمنى تحدد دوال الانتقال إلى الحالات التالية وتشير إلى ما إذا كانت الأجزاء اليسرى المقابلة حالات قبول أم لا. إذا كان E هو الجزء الأيسر من معادلة تنتمي إلى مجموعة كاملة من المعادلات، فإننا نقول إن أصغر مجموعة كاملة من المعادلات تحتوي على هذه المعادلة هي **آلة ذات حالة محدودة حتمية لـ E** في الخلفية. إذا كان E' تعبيراً آخر بحيث E = rep(E')، فإننا نقول إن الآلة ذات الحالة المحدودة الحتمية لـ E هي **آلة ذات حالة محدودة حتمية لـ E'**.

#### 3.1.2 Operations on the background

The background can be extended with new expressions and new equations. On the other hand, it can be made more informative by merging equivalence classes and refining equations accordingly.

New expressions can be added to the background by applying the operations ⊕, ⊙, and ⋆ to expressions in the background. A newly added expression defines a new equivalence class containing this expression only. Similarly, new equations can be added to background by specifying a left part E and a right part o + ... + x · Eₓ + ... . They must respect the invariant specified in Section 3.1.1. The first condition of the invariant can be easily enforced, but the second condition is under the responsibility of the user of the system. It can be ensured by using the algorithm to compute derivatives described in [9]. A reduced background may lose this property after the addition of a new equation.

Two equivalence classes can be unified to a single one by using the operation unify. Let E₁ and E₂ be two expressions belonging to two different equivalence classes of the background. The operation unify(E₁, E₂) unites the two classes into one, as follows: Assuming that rep(E₁) is better than rep(E₂), rep(E₁) becomes the new representative of the new equivalence class. Moreover, rep(E₂) is replaced by rep(E₁) in every equation using it. The old equations are removed from the background. It is the user's responsibility to make sure that the precondition L(E₁) = L(E₂) holds, since the invariant of the background can be violated otherwise.

Unifying equivalence classes and adding equations may result in a non reduced background. Then, a reduced background can be obtained by applying the operation reduce to it: If the background is not reduced, the operation selects two overlapping equations Eᵢ = oᵢ + ... + x · Eᵢₓ + ... (i = 1, 2). If E₁ ≠ E₂, it unifies E₁ and E₂; otherwise, it selects two expressions E₁ₓ and E₂ₓ that are not equal, and it unifies them. Afterwards, it iterates the same process until a reduced background is obtained. The execution of the operation reduce terminates since the number of equivalence classes decreases by one at each iteration. Moreover, the invariant of the background is maintained, since it is maintained after each execution of unify. In addition, the final set of equations is made of all equations rep(E) = o + ... + x · rep(Eₓ) + ... such that an equation E = o + ... + x · Eₓ + ... was in the initial background. Consequently, each complete set of equations is replaced by a new complete set of equations, representing a possibly smaller DFA for the same expressions. It can also be proven that the final set of equivalence classes produced by the operation reduce does not depend on what particular pairs of overlapping equations are chosen at each iteration of the algorithm (see Section B.1). This confluence property is nice but not really essential for most applications of the work presented in this paper.

#### 3.1.3 Example

I give an example to show how the background evolves when it is extended with new expressions and equations, and subsequently refined by using the operations unify and reduce.

---

## النسخة العربية

#### 3.1.2 العمليات على الخلفية

يمكن توسيع الخلفية بتعبيرات جديدة ومعادلات جديدة. من ناحية أخرى، يمكن جعلها أكثر إفادة من خلال دمج فئات التكافؤ وتحسين المعادلات وفقاً لذلك.

يمكن إضافة تعبيرات جديدة إلى الخلفية من خلال تطبيق العمليات ⊕، ⊙، و⋆ على التعبيرات الموجودة في الخلفية. يحدد التعبير المُضاف حديثاً فئة تكافؤ جديدة تحتوي على هذا التعبير فقط. وبالمثل، يمكن إضافة معادلات جديدة إلى الخلفية من خلال تحديد جزء أيسر E وجزء أيمن o + ... + x · Eₓ + ... . يجب أن تحترم هذه المعادلات الثابت المحدد في القسم 3.1.1. يمكن فرض الشرط الأول من الثابت بسهولة، لكن الشرط الثاني يقع على عاتق مستخدم النظام. يمكن ضمان ذلك باستخدام الخوارزمية لحساب المشتقات الموصوفة في [9]. قد تفقد الخلفية المُختزلة هذه الخاصية بعد إضافة معادلة جديدة.

يمكن توحيد فئتي تكافؤ في فئة واحدة باستخدام العملية unify. لنفترض أن E₁ وE₂ تعبيران ينتميان إلى فئتي تكافؤ مختلفتين في الخلفية. تقوم العملية unify(E₁, E₂) بتوحيد الفئتين في فئة واحدة، على النحو التالي: بافتراض أن rep(E₁) أفضل من rep(E₂)، يصبح rep(E₁) الممثل الجديد لفئة التكافؤ الجديدة. علاوة على ذلك، يتم استبدال rep(E₂) بـ rep(E₁) في كل معادلة تستخدمه. تُزال المعادلات القديمة من الخلفية. تقع على عاتق المستخدم مسؤولية التأكد من أن الشرط المسبق L(E₁) = L(E₂) محقق، لأن ثابت الخلفية يمكن أن يُنتهك بطريقة أخرى.

قد يؤدي توحيد فئات التكافؤ وإضافة المعادلات إلى خلفية غير مُختزلة. عندئذٍ، يمكن الحصول على خلفية مُختزلة من خلال تطبيق العملية reduce عليها: إذا لم تكن الخلفية مُختزلة، تختار العملية معادلتين متداخلتين Eᵢ = oᵢ + ... + x · Eᵢₓ + ... (i = 1, 2). إذا كان E₁ ≠ E₂، فإنها توحد E₁ وE₂؛ وإلا، فإنها تختار تعبيرين E₁ₓ وE₂ₓ غير متساويين، وتوحدهما. بعد ذلك، تكرر نفس العملية حتى يتم الحصول على خلفية مُختزلة. ينتهي تنفيذ العملية reduce لأن عدد فئات التكافؤ ينخفض بمقدار واحد في كل تكرار. علاوة على ذلك، يتم الحفاظ على ثابت الخلفية، لأنه يتم الحفاظ عليه بعد كل تنفيذ لـ unify. بالإضافة إلى ذلك، تتكون المجموعة النهائية من المعادلات من جميع المعادلات rep(E) = o + ... + x · rep(Eₓ) + ... بحيث كانت المعادلة E = o + ... + x · Eₓ + ... في الخلفية الأولية. وبالتالي، يتم استبدال كل مجموعة كاملة من المعادلات بمجموعة كاملة جديدة من المعادلات، تمثل آلة ذات حالة محدودة حتمية أصغر احتمالاً لنفس التعبيرات. يمكن أيضاً إثبات أن المجموعة النهائية من فئات التكافؤ التي تنتجها العملية reduce لا تعتمد على أزواج المعادلات المتداخلة المحددة في كل تكرار من الخوارزمية (انظر القسم B.1). هذه الخاصية التقاربية جيدة لكنها ليست ضرورية حقاً لمعظم تطبيقات العمل المقدم في هذه الورقة.

#### 3.1.3 مثال

أقدم مثالاً لتوضيح كيفية تطور الخلفية عند توسيعها بتعبيرات ومعادلات جديدة، ثم تحسينها لاحقاً باستخدام العمليات unify وreduce.

Let us start with a minimal background, only containing the atomic expressions 0, 1, a, ..., z spread into 27 equivalence classes. Let us add to the background the expression E = (1 + a)(ab*)*.

Now let us compute the derivatives of E and of its subexpressions using the algorithm of [9]. The principle of this algorithm boils down to unfolding expressions to the left until they start with a letter. Expressions starting with the same letter are then grouped to form the derivatives. For the expression F = (ab*)*, we get:

F = 1 + ab*(ab*)*
  = 1 + ab*F
  = 1 + a·G                                    (1)

G = b*F
  = F + bb*F
  = 1 + a·G + b·G                              (2)

The equations (1) and (2) may thus be added to the background. They constitute a complete set of equations, i.e. a DFA, and even an MDFA, for F.

**Note** The above calculation of equations for F and G makes use of the equality symbol (=) in an intuitive and "loose" way. It certainly does not denote syntactic equality as in Definition 1 but we can see that the left and right parts of equations denote the same regular language, which intuitively justifies the conclusion. The algorithm in [9] obtains the same result, by working on normalized expressions using the operations ⊕, ⊙, ⋆, and a set of derivation rules for normalized expressions.

Let us continue by computing derivatives and equations for the expression E:

E = (1 + a)F
  = F + aF
  = 1 + ab*F + aF
  = 1 + a·(F + b*F)
  = 1 + a·H                                    (3)

H = F + b*F
  = 1 + ab*F + bb*F
  = 1 + a·G + b·G                              (4)

At this point, we have a DFA for E, made of the three equations (3), (4), and (2). However, the equations (2) and (4) overlap (as defined in Section 3.1.1). Since size(G) < size(H), we replace H by G in all equations. Therefore, equation (4) is removed from the background, and equation (3) is replaced by

E = 1 + a·G                                    (3')

Now the equations (1) and (3') overlap. Thus, the expressions E and F are unified, which means that E is simplified to F. Equation (3') is removed from the background and we are left with equations (1) and (2), constituting an MDFA for E and F. We also see that the expressions E, F, G, and H are distributed into two equivalence classes {E, F} and {G, H}, of which F and G are the representatives. Notice that exactly the same classes and equations would have been obtained if the derivatives of E were computed before those of F. But computing the derivatives of only E would have failed to simplify E into F because F is not a derivative of E.

Finally, let us add the expression U = (a + b)* to the background and compute its derivatives. We get a single new equation:

U = 1 + (a + b)U
  = 1 + a·U + b·U                              (5)

Although L(U) = L(G), the expressions U and G are kept in different equivalence classes because equations (2) and (5) do not overlap. However, we can apply a minimization algorithm [17, 25] to the set of all equations to conclude that L(U) = L(G), and thus to safely execute unify(U, E), resulting into the final set of equations:

F = 1 + a·U                                    (1')
U = 1 + a·U + b·U                              (5)

and the equivalence classes {E, F} and {G, H, U}, of which F and U are the representatives.

---

#### 3.1.3 مثال

لنبدأ بخلفية دنيا، تحتوي فقط على التعبيرات الذرية 0، 1، a، ...، z موزعة على 27 فئة تكافؤ. لنضف إلى الخلفية التعبير E = (1 + a)(ab*)*.

لنحسب الآن مشتقات E ومشتقات تعبيراته الفرعية باستخدام خوارزمية [9]. يتلخص مبدأ هذه الخوارزمية في فك طي التعبيرات إلى اليسار حتى تبدأ بحرف. ثم يتم تجميع التعبيرات التي تبدأ بنفس الحرف لتشكيل المشتقات. بالنسبة للتعبير F = (ab*)* نحصل على:

F = 1 + ab*(ab*)*
  = 1 + ab*F
  = 1 + a·G                                    (1)

G = b*F
  = F + bb*F
  = 1 + a·G + b·G                              (2)

يمكن إذن إضافة المعادلتين (1) و(2) إلى الخلفية. تشكلان مجموعة كاملة من المعادلات، أي آلة ذات حالة محدودة حتمية، بل آلة حتمية دنيا، للتعبير F.

**ملاحظة** يستخدم الحساب أعلاه للمعادلات لـ F وG رمز التساوي (=) بطريقة حدسية و"فضفاضة". لا يشير بالتأكيد إلى التساوي النحوي كما في التعريف 1 ولكن يمكننا أن نرى أن الأجزاء اليسرى واليمنى من المعادلات تشير إلى نفس اللغة النظامية، مما يبرر الاستنتاج بشكل حدسي. تحصل الخوارزمية في [9] على نفس النتيجة، من خلال العمل على التعبيرات المُطبَّعة باستخدام العمليات ⊕، ⊙، ⋆، ومجموعة من قواعد الاشتقاق للتعبيرات المُطبَّعة.

لنستمر بحساب المشتقات والمعادلات للتعبير E:

E = (1 + a)F
  = F + aF
  = 1 + ab*F + aF
  = 1 + a·(F + b*F)
  = 1 + a·H                                    (3)

H = F + b*F
  = 1 + ab*F + bb*F
  = 1 + a·G + b·G                              (4)

في هذه المرحلة، لدينا آلة ذات حالة محدودة حتمية لـ E، مكونة من المعادلات الثلاث (3)، (4)، و(2). ومع ذلك، تتداخل المعادلتان (2) و(4) (كما هو معرّف في القسم 3.1.1). نظراً لأن size(G) < size(H)، نستبدل H بـ G في جميع المعادلات. لذلك، تُزال المعادلة (4) من الخلفية، وتُستبدل المعادلة (3) بـ:

E = 1 + a·G                                    (3')

الآن تتداخل المعادلتان (1) و(3'). وبالتالي، يتم توحيد التعبيرين E وF، مما يعني أن E يُبسَّط إلى F. تُزال المعادلة (3') من الخلفية ونبقى مع المعادلتين (1) و(2)، اللتين تشكلان آلة حتمية دنيا لـ E وF. نرى أيضاً أن التعبيرات E، F، G، وH موزعة على فئتي تكافؤ {E, F} و{G, H}، اللتين F وG هما ممثلاهما. لاحظ أن نفس الفئات والمعادلات بالضبط كانت ستُحصَل عليها لو حُسبت مشتقات E قبل مشتقات F. لكن حساب مشتقات E فقط كان سيفشل في تبسيط E إلى F لأن F ليس مشتقاً لـ E.

أخيراً، لنضف التعبير U = (a + b)* إلى الخلفية ونحسب مشتقاته. نحصل على معادلة جديدة واحدة:

U = 1 + (a + b)U
  = 1 + a·U + b·U                              (5)

على الرغم من أن L(U) = L(G)، يتم الاحتفاظ بالتعبيرين U وG في فئتي تكافؤ مختلفتين لأن المعادلتين (2) و(5) لا تتداخلان. ومع ذلك، يمكننا تطبيق خوارزمية تصغير [17، 25] على مجموعة جميع المعادلات للاستنتاج أن L(U) = L(G)، وبالتالي تنفيذ unify(U, E) بأمان، مما ينتج عنه المجموعة النهائية من المعادلات:

F = 1 + a·U                                    (1')
U = 1 + a·U + b·U                              (5)

وفئات التكافؤ {E, F} و{G, H, U}، اللتان F وU هما ممثلاهما.
