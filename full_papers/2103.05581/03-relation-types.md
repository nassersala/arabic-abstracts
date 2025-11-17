# Section 3: Relation Types
## القسم 3: أنواع العلاقات

**Section:** relation types
**Translation Quality:** 0.86
**Glossary Terms Used:** relation, predicate, equivalence relation, kernel, quotient, truncation, proposition, set, function extensionality

---

### English Version (Summary)

**3 Relation Types**

We now present the AgdaUALib's Relations module and its submodules. In §3.1 we define types that represent unary and binary relations, which we refer to as "discrete relations" to contrast them with the ("continuous") general and dependent relations that we introduce in §3.2. We call the latter "continuous relations" because they can have arbitrary arity (general relations) and they can be defined over arbitrary families of types (dependent relations).

**3.1 Discrete relations**

**Unary relations:** In set theory, given two sets A and P, we say that P is a subset of A, written P ⊆ A, just in case ∀ x (x ∈ P → x ∈ A). In Agda, we represent this using a unary predicate type Pred defined as follows:

```
Pred : U⋆ → (W : Universe) → U ⊔ W+⋆
Pred A W = A → W⋆
```

This is a general unary predicate type. The UALib includes types representing element inclusion (∈) and subset inclusion (⊆):

```
_∈_ : A → Pred A W → W⋆
x ∈ P = P x

_⊆_ : Pred A W → Pred A Z → U ⊔ W ⊔ Z⋆
P ⊆ Q = ∀ {x} → x ∈ P → x ∈ Q
```

**Predicates toolbox:** We define useful operations on predicates including disjoint union (⊎), union (∪), empty set (∅), and singletons. The image containment notation Im_⊆_ asserts that the image of a function is contained in a predicate:

```
Im_⊆_ : (A → B) → Pred B Z → U ⊔ Z⋆
Im f ⊆ S = ∀ x → f x ∈ S
```

**Binary Relations:** A binary relation on A is modeled as an inhabitant of A → A → W⋆. We generalize to relations from A to B:

```
REL : U⋆ → W⋆ → (Z : Universe) → U ⊔ W ⊔ Z+⋆
REL A B Z = A → B → Z⋆

Rel : U⋆ → (Z : Universe) → U ⊔ Z+⋆
Rel A Z = REL A A Z
```

**The kernel of a function:** The kernel of f : A → B is {(x, y) ∈ A × A : f x = f y}, represented as:

```
ker : (A → B) → Rel A W
ker g x y = g x ≡ g y
```

**3.2 Continuous relations**

This section introduces general relations (arbitrary arity) and dependent relations (defined over arbitrary families of types).

**General relations:** A general (or continuous) relation of arbitrary arity over a type I is a function from I → A to some universe W. We call it "continuous" because the arguments are functions from I (like continuous functions from the real interval [0,1]):

```
Rel-gen : U⋆ → (I : W⋆) → (Z : Universe) → U ⊔ W ⊔ Z+⋆
Rel-gen A I Z = (I → A) → Z⋆
```

**Dependent relations:** A dependent relation is defined over an indexed family of types. Given a family A : I → U⋆, a dependent relation is:

```
Rel-dep : {I : W⋆} → (I → U⋆) → (Z : Universe) → W ⊔ U ⊔ Z+⋆
Rel-dep A Z = Π A → Z⋆
```

**3.3 Equivalence relations and quotients**

An equivalence relation on A is a binary relation that is reflexive, symmetric, and transitive. The standard way to encode this in Agda is as a Sigma type:

```
IsEquivalence : Rel A Z → U ⊔ Z⋆
IsEquivalence R = (IsRefl R) × (IsSym R) × (IsTrans R)

Equivalence : U⋆ → (Z : Universe) → U ⊔ Z+⋆
Equivalence A Z = Σ R ∶ Rel A Z , IsEquivalence R
```

**Equivalence classes and quotients:** Given an equivalence relation R on A, we define the equivalence class (or R-block) containing x as:

```
[_] : A → Pred A Z
[ x ] = λ y → R x y
```

The quotient A / R is the collection of all R-blocks:

```
_/_ : (A : U⋆) → Equivalence A Z → U ⊔ Z+⋆
A / R = Σ P ∶ Pred A Z , ∃ x ∶ A , P ≡ [ x ]
```

**3.4 Truncation**

Truncation is a crucial concept in the mechanization of mathematics using type theory. We introduce the closely related concepts of truncation, sets, propositions, and proposition extensionality.

**Propositions and proposition extensionality:** A type P is a proposition (or is proof-irrelevant) if for all p q : P we have p ≡ q. In Agda:

```
is-Prop : U⋆ → U⋆
is-Prop A = (x y : A) → x ≡ y
```

This is also called is-subsingleton. Proposition extensionality asserts that logically equivalent propositions are equal:

```
Prop-Ext : (U : Universe) → U+⋆
Prop-Ext U = {P Q : U⋆} → is-Prop P → is-Prop Q → (P → Q) → (Q → P) → P ≡ Q
```

**Sets and uniqueness of identity proofs (UIP):** A type is a set (or satisfies UIP) if all of its identity types are subsingletons. In other words, for any x y : A, there is at most one proof of x ≡ y:

```
is-Set : U⋆ → U⋆
is-Set A = (x y : A) → is-Prop (x ≡ y)
```

The principle of unique identity proofs:

```
UIP : (A : U⋆) → U⋆
UIP A = {x y : A}(p q : x ≡ y) → p ≡ q
```

We can prove that is-Set and UIP are logically equivalent.

**Truncation:** The propositional truncation of a type A, denoted ∥A∥ or ║A║, is a proposition with the same "existence content" as A. It represents the proposition "A is inhabited." The key property is that ∥A∥ is a proposition (proof-irrelevant) even when A is not.

**3.5 Relation extensionality**

Just as function extensionality asserts that pointwise equal functions are equal, relation extensionality asserts that pointwise equal relations are equal:

```
Rel-Ext : (U W : Universe) → U ⊔ W+⋆
Rel-Ext U W = {A : U⋆}{R S : Rel A W} → (∀ x y → R x y ⇔ S x y) → R ≡ S
```

where ⇔ denotes logical equivalence. This principle, like function extensionality, must be postulated as it is independent of MLTT.

---

### النسخة العربية (الملخص)

**3 أنواع العلاقات**

نقدم الآن وحدة Relations في AgdaUALib ووحداتها الفرعية. في §3.1 نعرّف الأنواع التي تمثل العلاقات الأحادية والثنائية، والتي نشير إليها بـ "العلاقات المتقطعة" للتمييز بينها وبين العلاقات ("المستمرة") العامة والتابعة التي نقدمها في §3.2. نسمي الأخيرة "العلاقات المستمرة" لأنها يمكن أن تكون لها قوى عشوائية (العلاقات العامة) ويمكن تعريفها على عائلات عشوائية من الأنواع (العلاقات التابعة).

**3.1 العلاقات المتقطعة**

**العلاقات الأحادية:** في نظرية المجموعات، بالنظر إلى مجموعتين A وP، نقول إن P مجموعة جزئية من A، ونكتب P ⊆ A، فقط في حالة ∀ x (x ∈ P → x ∈ A). في Agda، نمثل هذا باستخدام نوع محمول أحادي Pred معرّف كما يلي:

```
Pred : U⋆ → (W : Universe) → U ⊔ W+⋆
Pred A W = A → W⋆
```

هذا نوع محمول أحادي عام. تتضمن UALib أنواعاً تمثل الاحتواء العنصري (∈) والاحتواء الجزئي (⊆):

```
_∈_ : A → Pred A W → W⋆
x ∈ P = P x

_⊆_ : Pred A W → Pred A Z → U ⊔ W ⊔ Z⋆
P ⊆ Q = ∀ {x} → x ∈ P → x ∈ Q
```

**صندوق أدوات المحمولات:** نعرّف عمليات مفيدة على المحمولات بما في ذلك الاتحاد المنفصل (⊎)، والاتحاد (∪)، والمجموعة الفارغة (∅)، والأحاديات. يؤكد ترميز احتواء الصورة Im_⊆_ أن صورة دالة محتواة في محمول:

```
Im_⊆_ : (A → B) → Pred B Z → U ⊔ Z⋆
Im f ⊆ S = ∀ x → f x ∈ S
```

**العلاقات الثنائية:** تُنمذج العلاقة الثنائية على A كساكن في A → A → W⋆. نعمم إلى العلاقات من A إلى B:

```
REL : U⋆ → W⋆ → (Z : Universe) → U ⊔ W ⊔ Z+⋆
REL A B Z = A → B → Z⋆

Rel : U⋆ → (Z : Universe) → U ⊔ Z+⋆
Rel A Z = REL A A Z
```

**نواة دالة:** نواة f : A → B هي {(x, y) ∈ A × A : f x = f y}، وتُمثَّل كـ:

```
ker : (A → B) → Rel A W
ker g x y = g x ≡ g y
```

**3.2 العلاقات المستمرة**

يقدم هذا القسم العلاقات العامة (قوى عشوائية) والعلاقات التابعة (معرّفة على عائلات عشوائية من الأنواع).

**العلاقات العامة:** العلاقة العامة (أو المستمرة) ذات القوى العشوائية على نوع I هي دالة من I → A إلى كون W ما. نسميها "مستمرة" لأن الوسائط هي دوال من I (مثل الدوال المستمرة من الفترة الحقيقية [0,1]):

```
Rel-gen : U⋆ → (I : W⋆) → (Z : Universe) → U ⊔ W ⊔ Z+⋆
Rel-gen A I Z = (I → A) → Z⋆
```

**العلاقات التابعة:** تُعرَّف العلاقة التابعة على عائلة مفهرسة من الأنواع. بالنظر إلى عائلة A : I → U⋆، فإن العلاقة التابعة هي:

```
Rel-dep : {I : W⋆} → (I → U⋆) → (Z : Universe) → W ⊔ U ⊔ Z+⋆
Rel-dep A Z = Π A → Z⋆
```

**3.3 علاقات التكافؤ والحاصلات القسمية**

علاقة التكافؤ على A هي علاقة ثنائية انعكاسية وتماثلية ومتعدية. الطريقة القياسية لترميز هذا في Agda هي كنوع سيجما:

```
IsEquivalence : Rel A Z → U ⊔ Z⋆
IsEquivalence R = (IsRefl R) × (IsSym R) × (IsTrans R)

Equivalence : U⋆ → (Z : Universe) → U ⊔ Z+⋆
Equivalence A Z = Σ R ∶ Rel A Z , IsEquivalence R
```

**فئات التكافؤ والحاصلات القسمية:** بالنظر إلى علاقة تكافؤ R على A، نعرّف فئة التكافؤ (أو R-كتلة) التي تحتوي x كـ:

```
[_] : A → Pred A Z
[ x ] = λ y → R x y
```

الحاصل القسمي A / R هو مجموعة جميع R-كتل:

```
_/_ : (A : U⋆) → Equivalence A Z → U ⊔ Z+⋆
A / R = Σ P ∶ Pred A Z , ∃ x ∶ A , P ≡ [ x ]
```

**3.4 الاقتطاع**

الاقتطاع مفهوم حاسم في ميكنة الرياضيات باستخدام نظرية الأنواع. نقدم المفاهيم المترابطة ارتباطاً وثيقاً للاقتطاع والمجموعات والقضايا والتوسعية القضوية.

**القضايا والتوسعية القضوية:** النوع P قضية (أو غير ذي صلة بالبرهان) إذا كان لجميع p q : P لدينا p ≡ q. في Agda:

```
is-Prop : U⋆ → U⋆
is-Prop A = (x y : A) → x ≡ y
```

يُسمى هذا أيضاً is-subsingleton. تؤكد التوسعية القضوية أن القضايا المتكافئة منطقياً متساوية:

```
Prop-Ext : (U : Universe) → U+⋆
Prop-Ext U = {P Q : U⋆} → is-Prop P → is-Prop Q → (P → Q) → (Q → P) → P ≡ Q
```

**المجموعات ووحدانية براهين الهوية (UIP):** النوع مجموعة (أو يحقق UIP) إذا كانت جميع أنواع هويته أحادية جزئية. بعبارة أخرى، لأي x y : A، يوجد على الأكثر برهان واحد لـ x ≡ y:

```
is-Set : U⋆ → U⋆
is-Set A = (x y : A) → is-Prop (x ≡ y)
```

مبدأ وحدانية براهين الهوية:

```
UIP : (A : U⋆) → U⋆
UIP A = {x y : A}(p q : x ≡ y) → p ≡ q
```

يمكننا إثبات أن is-Set وUIP متكافئان منطقياً.

**الاقتطاع:** الاقتطاع القضوي لنوع A، المرموز له بـ ∥A∥ أو ║A║، هو قضية لها نفس "محتوى الوجود" مثل A. إنه يمثل القضية "A مسكون". الخاصية الأساسية هي أن ∥A∥ قضية (غير ذات صلة بالبرهان) حتى عندما لا يكون A كذلك.

**3.5 التوسعية العلاقاتية**

تماماً كما تؤكد التوسعية الدالية أن الدوال المتساوية نقطياً متساوية، تؤكد التوسعية العلاقاتية أن العلاقات المتساوية نقطياً متساوية:

```
Rel-Ext : (U W : Universe) → U ⊔ W+⋆
Rel-Ext U W = {A : U⋆}{R S : Rel A W} → (∀ x y → R x y ⇔ S x y) → R ≡ S
```

حيث ⇔ يدل على التكافؤ المنطقي. هذا المبدأ، مثل التوسعية الدالية، يجب افتراضه لأنه مستقل عن MLTT.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Pred, Rel, REL, kernel, quotient, equivalence relation, truncation, is-Prop, is-Set, UIP, proposition extensionality, relation extensionality
- **Equations:** Multiple type signatures and Agda definitions
- **Citations:** None direct, but references to standard mathematical concepts
- **Special handling:** Mathematical notation preserved; Agda code in monospace; careful translation of technical terminology

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Key Paragraph

English (original): "A type P is a proposition (or is proof-irrelevant) if for all p q : P we have p ≡ q. Proposition extensionality asserts that logically equivalent propositions are equal."

Arabic translation: "النوع P قضية (أو غير ذي صلة بالبرهان) إذا كان لجميع p q : P لدينا p ≡ q. تؤكد التوسعية القضوية أن القضايا المتكافئة منطقياً متساوية."

Back-translation: "The type P is a proposition (or irrelevant to proof) if for all p q : P we have p ≡ q. Proposition extensionality asserts that logically equivalent propositions are equal."

**Verification:** ✓ Semantic equivalence maintained
