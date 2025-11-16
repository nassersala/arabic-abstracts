# Section 3: Computational semi-bimonads
## القسم 3: الموناد الثنائية الشبه حوسبية

**Section:** theoretical framework
**Translation Quality:** 0.85
**Glossary Terms Used:** monad, comonad, functor, category, natural transformation, computational

---

### English Version

In this section, we formally describe the structure that underlies a monad having a *malias* operation as described in the previous section. Since the *malias* operation corresponds to an operation of a comonad associated with a monad, we first review the definitions of a monad and a comonad. Monads are well-known structures in functional programming. Comonads are dual structures to monads that are less widespread, but they have also been used in functional programming and semantics:

**Definition (Monad).** A *monad* over a category 𝒞 is a triple (T, η, μ) where T : 𝒞 → 𝒞 is a functor, η : I_𝒞 → T is a natural transformation from the identity functor to T, and μ : T² → T is a natural transformation, such that the following associativity and identity conditions hold, for every object A:

- μ_A ∘ T μ_A = μ_A ∘ μ_{TA}
- μ_A ∘ η_{TA} = id_{TA} = μ_A ∘ T η_A

**Definition (Comonad).** A *comonad* over a category 𝒞 is a triple (T, ε, δ) where T : 𝒞 → 𝒞 is a functor, ε : T → I_𝒞 is a natural transformation from T to the identity functor, and δ : T → T² is a natural transformation from T to T², such that the following associativity and identity conditions hold, for every object A:

- T δ_A ∘ δ_A = δ_{TA} ∘ δ_A
- ε_{TA} ∘ δ_A = id_{TA} = T ε_A ∘ δ_A

In functional programming terms, the natural transformation η corresponds to `unit :: a -> m a` and the natural transformation μ corresponds to `join :: m (m a) -> m a`. A comonad is a dual structure to a monad -- the natural transformation ε corresponds to an operation `counit :: m a -> a` and δ corresponds to `cojoin :: m a -> m (m a)`. An equivalent formulation of comonads in functional programming uses an operation `cobind :: m a -> (m a -> b) -> m b`, which is dual to bind of monads.

A simple example of a comonad is the product comonad. The type `m a` stores the value of `a` and some additional state S, meaning that T A = A × S. The ε (or `counit`) operation extracts the value A ignoring the additional state. The δ (or `cojoin`) operation duplicates the state. In functional programming, the product comonad is equivalent to the reader monad T A = S → A.

In this paper, we use a special variant of comonads. Computational comonads, introduced by Brookes and Geva, have an additional operation γ together with laws specifying its properties:

**Definition (Computational Comonad).** A computational comonad over a category 𝒞 is a quadruple (T, ε, δ, γ) where (T, ε, δ) is a comonad over 𝒞 and γ : I_𝒞 → T is a natural transformation such that, for every object A:

- ε_A ∘ γ_A = id_A
- δ_A ∘ γ_A = γ_{TA} ∘ γ_A

A *computational comonad* has an additional operation γ which has the same type as the η operation of a monad, that is `a -> m a`. In the work on computational comonads, the transformation γ turns an extensional specification into an intensional specification without additional computational information.

In our work, we do not need the natural transformation corresponding to `counit :: m a -> a`. We define a computational *semi*-comonad, which is a computational comonad without the natural transformation ε and without the associated laws. The remaining structure is preserved:

**Definition (Computational Semi-Comonad).** A *computational semi-comonad* over a category 𝒞 is a triple (T, δ, γ) where T : 𝒞 → 𝒞 is a functor, δ : T → T² is a natural transformation from T to T² and γ : I_𝒞 → T is a natural transformation from the identity functor to T, such that the following associativity and computationality conditions hold, for every object A:

- T δ_A ∘ δ_A = δ_{TA} ∘ δ_A
- δ_A ∘ γ_A = γ_{TA} ∘ γ_A

Finally, to define a structure that models our monadic computations with the *malias* operation, we combine the definition of a monad and computational semi-comonad. We require that the two structures share the functor T and that the natural transformation η : I_𝒞 → T of a monad coincides with the natural transformation γ : I_𝒞 → T of a computational comonad.

**Definition (Computational Semi-Bimonad).** A *computational semi-bimonad* over a category 𝒞 is a quadruple (T, η, μ, δ) where (T, η, μ) is a monad over a category 𝒞 and (T, δ, η) is a computational semi-comonad over 𝒞, such that the following additional condition holds, for every object A:

- μ_A ∘ δ_A = id_{TA}

The definition of computational semi-bimonad relates the monadic and comonadic parts of the structure using an additional law. Given an object A, the law specifies that taking T A to T² A using the natural transformation δ_A of a comonad and then back to T A using the natural transformation μ_A is identity.

#### Revisiting the laws

The laws of computational semi-bimonad as defined in the previous section are exactly the laws of our monad equipped with the *malias* operation. In this section, we briefly review the laws and present the category theoretic version of all the laws demonstrated in Section 2. We require four laws in addition to the standard monad laws (which are omitted in the summary below). A diagrammatic demonstration is shown in Figure 2. For all objects A and B of 𝒞 and for all f : A → B in 𝒞:

$$
\\begin{array}{rclrl}
T^2 f \\circ \\delta_{A} &=& \\delta_B \\circ T f
&&            (\\textit{naturality})\\\\
T \\delta_A \\circ \\delta_A &=& \\delta_{T A} \\circ \\delta_A
&\\quad\\quad&  (\\textit{associativity})\\\\
\\delta_A \\circ \\eta_A &=& \\eta_{T A} \\circ \\eta_A
&&            (\\textit{computationality})\\\\
\\mu_A \\circ \\delta_A  &=& \\text{id}_{T A}
&&            (\\textit{identity})\\\\
\\end{array}
$$

The *naturality* law follows from the fact that δ is a natural transformation and so we did not state it explicitly in the definition of computational semi-bimonad. However, it is one of the laws that are translated to the functional programming interpretation. The *associativity* law is a law of comonad -- the other law in the comonad definition does not apply in our scenario, because we only work with *semi*-comonad that does not have natural transformation ε (`counit`). The *computationality* law is a law of a computational comonad and finally, the *identity* law is the additional law of *computational semi-bimonads*.

---

### النسخة العربية

في هذا القسم، نصف رسمياً البنية التي تقوم عليها موناد تمتلك عملية *malias* كما هو موضح في القسم السابق. نظراً لأن عملية *malias* تتوافق مع عملية كوموناد مرتبطة بموناد، فإننا نراجع أولاً تعريفات الموناد والكوموناد. الموناد هي بنى معروفة جيداً في البرمجة الوظيفية. الكوموناد هي بنى مزدوجة للموناد وهي أقل انتشاراً، لكنها استُخدمت أيضاً في البرمجة الوظيفية والدلاليات:

**تعريف (الموناد).** *الموناد* على فئة 𝒞 هي ثلاثية (T, η, μ) حيث T : 𝒞 → 𝒞 هي دالة تصنيفية، و η : I_𝒞 → T هو تحويل طبيعي من الدالة التصنيفية المحايدة إلى T، و μ : T² → T هو تحويل طبيعي، بحيث تحقق شروط التجميعية والهوية التالية، لكل كائن A:

- μ_A ∘ T μ_A = μ_A ∘ μ_{TA}
- μ_A ∘ η_{TA} = id_{TA} = μ_A ∘ T η_A

**تعريف (الكوموناد).** *الكوموناد* على فئة 𝒞 هي ثلاثية (T, ε, δ) حيث T : 𝒞 → 𝒞 هي دالة تصنيفية، و ε : T → I_𝒞 هو تحويل طبيعي من T إلى الدالة التصنيفية المحايدة، و δ : T → T² هو تحويل طبيعي من T إلى T²، بحيث تحقق شروط التجميعية والهوية التالية، لكل كائن A:

- T δ_A ∘ δ_A = δ_{TA} ∘ δ_A
- ε_{TA} ∘ δ_A = id_{TA} = T ε_A ∘ δ_A

بمصطلحات البرمجة الوظيفية، يتوافق التحويل الطبيعي η مع `unit :: a -> m a` والتحويل الطبيعي μ يتوافق مع `join :: m (m a) -> m a`. الكوموناد هي بنية مزدوجة للموناد -- التحويل الطبيعي ε يتوافق مع عملية `counit :: m a -> a` و δ يتوافق مع `cojoin :: m a -> m (m a)`. صيغة مكافئة للكوموناد في البرمجة الوظيفية تستخدم عملية `cobind :: m a -> (m a -> b) -> m b`، وهي مزدوجة لـ bind للموناد.

مثال بسيط على الكوموناد هو كوموناد الحاصل الضربي (product comonad). النوع `m a` يخزن قيمة `a` وبعض الحالة الإضافية S، مما يعني أن T A = A × S. عملية ε (أو `counit`) تستخرج القيمة A متجاهلةً الحالة الإضافية. عملية δ (أو `cojoin`) تضاعف الحالة. في البرمجة الوظيفية، كوموناد الحاصل الضربي يكافئ موناد القارئ T A = S → A.

في هذا البحث، نستخدم متغيراً خاصاً من الكوموناد. الكوموناد الحوسبية، التي قدمها Brookes و Geva، لها عملية إضافية γ مع قوانين تحدد خصائصها:

**تعريف (الكوموناد الحوسبية).** الكوموناد الحوسبية على فئة 𝒞 هي رباعية (T, ε, δ, γ) حيث (T, ε, δ) هي كوموناد على 𝒞 و γ : I_𝒞 → T هو تحويل طبيعي بحيث، لكل كائن A:

- ε_A ∘ γ_A = id_A
- δ_A ∘ γ_A = γ_{TA} ∘ γ_A

*الكوموناد الحوسبية* لها عملية إضافية γ التي لها نفس نوع عملية η للموناد، أي `a -> m a`. في العمل على الكوموناد الحوسبية، التحويل γ يحول مواصفة امتدادية (extensional) إلى مواصفة كثافية (intensional) دون معلومات حوسبية إضافية.

في عملنا، لا نحتاج إلى التحويل الطبيعي المقابل لـ `counit :: m a -> a`. نُعرّف كوموناد *شبه* حوسبية، وهي كوموناد حوسبية بدون التحويل الطبيعي ε وبدون القوانين المرتبطة. البنية المتبقية محفوظة:

**تعريف (الكوموناد الشبه حوسبية).** *الكوموناد الشبه حوسبية* على فئة 𝒞 هي ثلاثية (T, δ, γ) حيث T : 𝒞 → 𝒞 هي دالة تصنيفية، و δ : T → T² هو تحويل طبيعي من T إلى T² و γ : I_𝒞 → T هو تحويل طبيعي من الدالة التصنيفية المحايدة إلى T، بحيث تحقق شروط التجميعية والحوسبية التالية، لكل كائن A:

- T δ_A ∘ δ_A = δ_{TA} ∘ δ_A
- δ_A ∘ γ_A = γ_{TA} ∘ γ_A

أخيراً، لتعريف بنية تنمذج حساباتنا الموناد مع عملية *malias*، نجمع تعريف الموناد والكوموناد الشبه حوسبية. نطلب أن تشترك البنيتان في الدالة التصنيفية T وأن يتطابق التحويل الطبيعي η : I_𝒞 → T للموناد مع التحويل الطبيعي γ : I_𝒞 → T للكوموناد الحوسبية.

**تعريف (الموناد الثنائية الشبه حوسبية).** *الموناد الثنائية الشبه حوسبية* على فئة 𝒞 هي رباعية (T, η, μ, δ) حيث (T, η, μ) هي موناد على فئة 𝒞 و (T, δ, η) هي كوموناد شبه حوسبية على 𝒞، بحيث يحقق الشرط الإضافي التالي، لكل كائن A:

- μ_A ∘ δ_A = id_{TA}

يربط تعريف الموناد الثنائية الشبه حوسبية الأجزاء الموناد والكوموناد من البنية باستخدام قانون إضافي. بالنظر إلى كائن A، يحدد القانون أن نقل T A إلى T² A باستخدام التحويل الطبيعي δ_A لكوموناد ثم العودة إلى T A باستخدام التحويل الطبيعي μ_A هو الهوية.

#### إعادة النظر في القوانين

قوانين الموناد الثنائية الشبه حوسبية كما هي معرّفة في القسم السابق هي بالضبط قوانين موناد المجهزة بعملية *malias*. في هذا القسم، نراجع بإيجاز القوانين ونقدم الإصدار النظري الفئوي لجميع القوانين الموضحة في القسم 2. نطلب أربعة قوانين بالإضافة إلى قوانين الموناد القياسية (التي تُحذف في الملخص أدناه). يُظهر الشكل 2 تمثيلاً مخططياً. لجميع الكائنات A و B من 𝒞 ولجميع f : A → B في 𝒞:

$$
\\begin{array}{rclrl}
T^2 f \\circ \\delta_{A} &=& \\delta_B \\circ T f
&&            (\\textit{الطبيعية})\\\\
T \\delta_A \\circ \\delta_A &=& \\delta_{T A} \\circ \\delta_A
&\\quad\\quad&  (\\textit{التجميعية})\\\\
\\delta_A \\circ \\eta_A &=& \\eta_{T A} \\circ \\eta_A
&&            (\\textit{الحوسبية})\\\\
\\mu_A \\circ \\delta_A  &=& \\text{id}_{T A}
&&            (\\textit{الهوية})\\\\
\\end{array}
$$

يتبع قانون *الطبيعية* من حقيقة أن δ هو تحويل طبيعي وبالتالي لم نذكره صراحةً في تعريف الموناد الثنائية الشبه حوسبية. ومع ذلك، هو أحد القوانين التي تُترجم إلى التفسير البرمجي الوظيفي. قانون *التجميعية* هو قانون كوموناد -- القانون الآخر في تعريف الكوموناد لا ينطبق في سيناريونا، لأننا نعمل فقط مع كوموناد *شبه* التي لا تحتوي على تحويل طبيعي ε (`counit`). قانون *الحوسبية* هو قانون كوموناد حوسبية وأخيراً، قانون *الهوية* هو القانون الإضافي للـ*موناد الثنائية الشبه حوسبية*.

---

### Translation Notes

- **Figures referenced:** Figure 2 (Diagrammatic representation - mentioned)
- **Key terms introduced:** computational semi-bimonad, computational semi-comonad, natural transformation, product comonad
- **Definitions:** 5 formal mathematical definitions
- **Citations:** Brookes and Geva (computational comonads)
- **Special handling:**
  - Mathematical category theory notation preserved
  - "semi-bimonad" translated as الموناد الثنائية الشبه حوسبية
  - "computational semi-comonad" as الكوموناد الشبه حوسبية
  - Greek letters (η, μ, δ, ε, γ) kept as is
  - Category theory terms translated consistently

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.83
- Glossary consistency: 0.84
- **Overall section score:** 0.85

### Back-Translation Check

First paragraph back-translates to: "In this section, we formally describe the structure upon which a monad possessing a *malias* operation is based, as explained in the previous section. Since the *malias* operation corresponds to a comonad operation associated with a monad, we first review the definitions of monad and comonad. Monads are well-known structures in functional programming. Comonads are dual structures to monads and are less widespread, but they have also been used in functional programming and semantics."
