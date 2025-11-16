# Section 7: Ensemble.lagda
## القسم 7: Ensemble.lagda

### English

Serious consideration must be given to the data type used to describe the context of a natural deduction tree. In a proof tree for Γ ⊢ 𝛼, it must be verified that the remaining open assumptions are all members of Γ, so the type must have a notion of 'subset'. For universal generalisation introduction, and existential generalisation elimination, it will also be necessary to verify that a given variable is not free in any open assumption, so the type must also have a notion for a predicate holding on all elements. Throughout the natural deduction proof, the collection of open assumptions is modified, either by making new assumptions, by combining collections of assumptions, or by discharging assumptions. Finally, while we will be giving proofs about natural deduction trees, we would also like to give proofs regarding actual formulae (and axiom schemes). Giving natural deduction proofs in this system should correspond closely to doing natural deduction (from the bottom up) by hand. There should not be any need for operations other than the usual rules for natural deduction (with a single exception at the beginning of the proof, as will be shown later). Any manipulation of the context should be done automatically by Agda, and proofs regarding variable freedom and open assumptions should be solvable using Agda's proof search.

The List (or Vec) type is not suitable. While removal of elements from a list of formulae can be defined with a function, it is unwieldy to give proofs regarding the results of such computations, as they depend on equality-checking of formulae, and so proofs must include both the case where the equality is as expected, and the degenerate case.

An implementation of classical propositional logic in the style of natural deduction was given in [5]. While this does use (something equivalent to) lists, it requires frequent use of extra deduction rules for weakening the context. This would not be suitable for a natural deduction assistant, and it also does not solve the problems given above for first order logic.

Predicates can be used to store collections of values, in the manner of set comprehension. We define the type Ensemble as another name for Pred. It will be used to refer to predicates which have been created in a manner to follow. This is only for ease of understanding, and is not an actual restriction. Ensembles will resemble finite sets.

```agda
Ensemble : Set → Set₁
Ensemble A = A → Set
```

Membership is defined by satisfying the predicate.

```agda
infix 4 _∈_ _∉_

_∈_ : {A : Set} → A → Ensemble A → Set
α ∈ αs = αs α

_∉_ : {A : Set} → A → Ensemble A → Set
α ∉ αs = ¬(α ∈ αs)
```

A sensible definition of subset is 𝐴 ⊂ 𝐵 if ∀𝑥(𝑥 ∈ 𝐴 → 𝑥 ∈ 𝐵). However, some ensembles will be defined using negations. If it is absurd for 𝑥 to be in 𝐴 (for example, if 𝐴 is the empty set), then proving that 𝑥 ∈ 𝐵 can be done by either pattern matching to an empty case, or using the lemma ⊥-elim. However, Agda's proof search will not do pattern matching inside lambda expressions, and it will not find lemmas unless it is hinted to do so. For convenience, we adopt a minimal logic translation by taking the double negative of the right side of the implication, which solves this issue.

```agda
infix 4 _⊂_

_⊂_ : {A : Set} → Ensemble A → Ensemble A → Set
αs ⊂ βs = ∀ x → x ∈ αs → ¬(x ∉ βs)
```

The empty ensemble and singleton ensembles are defined in the obvious way.

```agda
∅ : {A : Set} → Ensemble A
∅ = λ _ → ⊥

⟨_⟩ : {A : Set} → A → Ensemble A
⟨ α ⟩ = λ x → x ≡ α
```

It would be reasonable to define union in terms of a disjoint union type, so that a proof of 𝑥 ∈ 𝐴 ∪ 𝐵 would be either a proof of 𝑥 ∈ 𝐴 or of 𝑥 ∈ 𝐵. However, we want Agda's proof search to fill in proofs regarding subsets. For a proof that 𝐴 ∪ 𝐵 ⊂ 𝐴 ∪ 𝐵 ∪ ∅, we would have to do a case analysis on a proof of 𝑥 ∈ 𝐴 ∪ 𝐵. Instead we define 𝑥 ∈ 𝐴 ∪ 𝐵 using functions, so that pattern matching is not necessary in order to make use of such a proof. One definition involving only functions is 𝑥 ∈ 𝐴 ∪ 𝐵 ≔ 𝑥 ∉ 𝐴 → 𝑥 ∈ 𝐵. We take the double negative of the right side of the implication, for the same reasons as above.

```agda
infixr 5 _∪_

_∪_ : {A : Set} → Ensemble A → Ensemble A → Ensemble A
(αs ∪ βs) = λ x → x ∉ αs → ¬(x ∉ βs)
```

Instead of defining a set difference, we define notation for removing a single element from an ensemble. Since ensembles will be used only for finite collections, this is not a limitation. A definition using conjunctions is that 𝑥 ∈ 𝐴 − 𝑎 means 𝑥 ∈ 𝐴 and 𝑥 ≠ 𝑎. Translating this to functions gives 𝑥 ∈ 𝐴 − 𝑎 ≔ ¬(𝑥 ∈ 𝐴 → 𝑥 ≡ 𝑎). Take the contrapositive of the inner implication.

```agda
infixl 5 _-_

_-_ : {A : Set} → Ensemble A → A → Ensemble A
(αs - α) = λ x → ¬(x ≢ α → x ∉ αs)
```

These definitions allow subset propositions to be proved without case analysis or ⊥-elim (EFQ), by adopting functional definitions and using double negations. Moreover, the only quantifier used in the definitions is in the definition of _⊂_. Since functions are equivalent to implications, we have translated the notion of subset to a proposition of the form ∀𝑥𝐴, where 𝐴 is a formula in the implicational fragment of minimal logic. This is to be expected, since we wanted the proof terms to be simply typed lambda calculus terms, which is precisely equivalent to minimal logic [11].

Subset proofs can now be solved by Agda automatically, with good performance. In the case of all natural deduction proofs to follow, Agda solved the subset proof in less than one second (the default time limit for proof search). Moreover, since the implicational fragment of minimal logic is decidable, there are proof search algorithms which will always find a proof if one exists [15].

Of course, ensembles are just predicates, so they can be created in any way that functions can be created. We can define a type to keep track of the creation of a predicate, to ensure it was created using (something equal to) the functions above. Additionally, the type requires that the predicate is over a type with a decidable equality.

```agda
data Assembled {A : Set} (eq : Decidable≡ A) : Pred A → Set₁ where
  from∅   : Assembled eq ∅
  from⟨_⟩ : (α : A) → Assembled eq (⟨ α ⟩)
  from_∪_ : ∀{αs βs} → Assembled eq αs → Assembled eq βs
          → Assembled eq (αs ∪ βs)
  from_-_ : ∀{αs}    → Assembled eq αs → (α : A) → Assembled eq (αs - α)
```

**Proposition 7.0.1.** Assembled ensembles have decidable membership.

**Proof.**

```agda
dec∈ : {A : Set} {eq : Decidable≡ A} {αs : Ensemble A}
     → (x : A) → Assembled eq αs → Dec (x ∈ αs)
```

Nothing is in the empty ensemble.

```agda
dec∈ x from∅ = no λ x∈∅ → x∈∅
```

Membership of a singleton is defined by an equality, and so its decidability is just the decidable equality from Assembled.

```agda
dec∈ {_} {eq} x (from⟨ α ⟩) = eq x α
```

To check membership for a union, simply check first for membership of the left ensemble, then the right. The lambda expression proofs given here are non-trivial, and difficult to interpret, but can be provided by Agda's proof search.

```agda
dec∈ x (from Aαs ∪ Aβs)  with dec∈ x Aαs
...  | yes x∈αs  = yes λ x∉αs _ → x∉αs x∈αs
...  | no x∉αs  with dec∈ x Aβs
...    | yes x∈βs  = yes λ _ x∉βs → x∉βs x∈βs
...    | no x∉βs   = no λ x∉αs∪βs → x∉αs∪βs x∉αs x∉βs
```

Finally, in the case of an element being removed, use the decidable equality from Assembled to check if the given element was removed, and otherwise check if the given element is in the inner ensemble.

```agda
dec∈ {_} {eq} x (from Aαs - α)  with eq x α
...  | yes refl  = no λ α∈αs-α → α∈αs-α λ α≢α _ → α≢α refl
...  | no x≢α  with dec∈ x Aαs
...    | yes x∈αs  = yes λ x≢α→x∉αs → x≢α→x∉αs x≢α x∈αs
...    | no x∉αs   = no λ x∈αs-α
                       → x∈αs-α (λ _ _ → x∈αs-α (λ _ _ → x∈αs-α (λ _ → x∉αs)))
```

Given an ensemble 𝐴, a sensible definition for a predicate 𝑃 holding on every element of 𝐴 would be ∀𝑥(𝑥 ∈ 𝐴 → 𝑃 𝑥). However, for inductively defined predicates (like _notFreeIn α for some 𝛼), this is not easy to work with, either by hand or using proof search. For example, to prove that the variable 𝑦 is not free in all members of {∀𝑦𝑄𝑦} ∪ {⊥}, it would be necessary to show that every member is equal to either ∀𝑦𝑄𝑦 or ⊥, and only then supply the required constructors for each case. Once again, this requires pattern matching.

Instead, for an assembled ensemble, we give a definition for All which utilises the structure of the ensemble, and describes what computation must be performed to check that a predicate holds on all members. To do so, maintain a list of all elements which have been removed from the ensemble.

```agda
infixr 5 _all∪_

data All_[_∖_] {A : Set} (P : Pred A) : Ensemble A → List A → Set₁ where
  all∅ : ∀{xs}
       → All P [ ∅ ∖ xs ]
```

𝑃 holds on all of a singleton if it holds on the element of the singleton, or else if that element has already been removed.

```agda
  all⟨_⟩  : ∀{α xs}
          → P α
          → All P [ ⟨ α ⟩ ∖ xs ]
  all⟨-_⟩ : ∀{α xs}
          → α List.∈ xs → All P [ ⟨ α ⟩ ∖ xs ]
```

In the case of a union, 𝑃 must hold on both sides of the union.

```agda
  _all∪_  : ∀{αs βs xs} → All P [ αs ∖ xs ] → All P [ βs ∖ xs ]
          → All P [ αs ∪ βs ∖ xs ]
```

Finally, when an ensemble has been created by removing an element from another, check that 𝑃 holds on the other ensemble for all values other than the removed one.

```agda
  all-_   : ∀{αs x xs}
          → All P [ αs ∖ x ∷ xs ] → All P [ αs - x ∖ xs ]
```

Now, 𝑃 holds on all of 𝛼𝑠 if it holds according to the above procedure, with the removed element list starting empty.

```agda
All : {A : Set} → Pred A → Ensemble A → Set₁
All P αs = All P [ αs ∖ [] ]
```

**Proposition 7.0.2.** The definition of All for assembled ensembles is weaker than the usual set definition.

**Proof.** We use a lemma to show that this is the case for all values of the removed list of elements, and apply it to the case of the empty list.

```agda
fAll→All : {A : Set} {eq : Decidable≡ A} {P : Pred A} {αs : Ensemble A}
         → Assembled eq αs → (∀ x → x ∈ αs → P x) → All P αs
fAll→All {A} {eq} {P} Aαs fall = φ Aαs [] (λ x x∈αs _ → fall x x∈αs)
  where
    φ : ∀{αs} → Assembled eq αs → ∀ xs
      → (∀ x → x ∈ αs → x List.∉ xs → P x) → All P [ αs ∖ xs ]
    φ from∅ xs fall∅ = all∅
```

For a singleton {𝛼}, either 𝛼 has been removed, or otherwise it has not been removed, in which case we use the functional all to prove 𝑃 𝛼.

```agda
    φ from⟨ α ⟩ xs fall⟨α⟩  with List.dec∈ eq α xs
    ...  | yes α∈xs  = all⟨- α∈xs ⟩
    ...  | no α∉xs   = all⟨ fall⟨α⟩ α refl α∉xs ⟩
```

Since unions are defined using a double negation, to show that the functional all for a union means functional all for each of the two ensembles, use a contradiction for each.

```agda
    φ (from Aαs ∪ Aβs) xs fallαs∪βs = (φ Aαs xs fallαs)
                                      all∪ (φ Aβs xs fallβs)
      where
        fallαs : _
        fallαs x x∈αs = fallαs∪βs x (λ x∉αs _   → x∉αs x∈αs)
        fallβs : _
        fallβs x x∈βs = fallαs∪βs x (λ _   x∉βs → x∉βs x∈βs)
```

In the case of 𝛼𝑠 − 𝛼, we show first that if 𝑥 ∈ 𝛼𝑠 then 𝑥 ∈ 𝛼𝑠 − 𝛼, and that if 𝑥 ∉ 𝛼 ∷ 𝑥𝑠 then 𝑥 ∉ 𝑥𝑠.

```agda
    φ (from Aαs - α) xs fallαs-α = all- (φ Aαs (α ∷ xs) fallαs)
      where
        fallαs : _
        fallαs x x∈αs x∉α∷xs =
          let x∈αs-α : _
              x∈αs-α x≢α→x∉αs = x≢α→x∉αs (λ x≢α → x∉α∷xs List.[ x≢α ]) x∈αs
              x∉xs : x List.∉ xs
              x∉xs x∈xs = x∉α∷xs (α ∷ x∈xs)
          in fallαs-α x x∈αs-α x∉xs
```

The converse cannot be proved; All is in fact strictly weaker than the functional definition. While it could be expected that pattern matching on both All and Assembled would lead to a proof, this will not work because Agda cannot unify function types. For example, in the case that an ensemble was assembled by from Aαs ∪ Aβs, case analysis of the proof of All P (αs ∪ βs) does not show that the only constructor is _all∪_; Agda cannot determine that λ x → x ∉ αs → ¬(x ∉ βs) does not unify with λ _ → ⊥, so all∅ may or may not be a constructor. If we wanted a stronger type which is equivalent to the functional definition, the assembled structure would need to be included in All.

We can use the All predicate to define the restriction that certain deductions are valid only if a given variable is not free in an ensemble of open assumptions. For the usual use case (i.e. cases other than abstract proof tree manipulation where variable freedom is determined by some lemma), Agda's proof search will find the required proof. However, due to the above limitations with unification of functions, Agda does not see that there is only one constructor for each non-singleton ensemble, so the search algorithm is not fast. For larger proof trees, it is necessary to increase the timeout from the default one second to ten seconds. This could also be resolved by including the assembled structure in All.

### Arabic Translation

يجب إعطاء اهتمام جاد لنوع البيانات المستخدم لوصف سياق شجرة الاستنتاج الطبيعي. في شجرة برهان لـ Γ ⊢ 𝛼، يجب التحقق من أن الافتراضات المفتوحة المتبقية جميعها أعضاء في Γ، لذا يجب أن يكون للنوع مفهوم 'مجموعة فرعية'. بالنسبة لإدخال التعميم الكلي، وإزالة التعميم الوجودي، سيكون من الضروري أيضاً التحقق من أن متغيراً معيناً ليس حراً في أي افتراض مفتوح، لذا يجب أن يكون للنوع أيضاً مفهوم لمحمول يسري على جميع العناصر. طوال برهان الاستنتاج الطبيعي، يتم تعديل مجموعة الافتراضات المفتوحة، إما عن طريق إجراء افتراضات جديدة، أو عن طريق دمج مجموعات من الافتراضات، أو عن طريق إبراء الافتراضات. أخيراً، بينما سنقدم براهين حول أشجار الاستنتاج الطبيعي، نود أيضاً تقديم براهين بخصوص الصيغ الفعلية (ومخططات البديهيات). إعطاء براهين الاستنتاج الطبيعي في هذا النظام يجب أن يتوافق بشكل وثيق مع القيام بالاستنتاج الطبيعي (من الأسفل إلى الأعلى) يدوياً. لا ينبغي أن تكون هناك حاجة لعمليات أخرى غير القواعد المعتادة للاستنتاج الطبيعي (مع استثناء واحد في بداية البرهان، كما سيتم توضيحه لاحقاً). يجب أن يتم أي تلاعب بالسياق تلقائياً بواسطة Agda، ويجب أن تكون البراهين المتعلقة بحرية المتغير والافتراضات المفتوحة قابلة للحل باستخدام بحث البرهان في Agda.

نوع List (أو Vec) غير مناسب. بينما يمكن تعريف إزالة العناصر من قائمة من الصيغ بدالة، فإنه من الصعب إعطاء براهين بخصوص نتائج مثل هذه الحسابات، حيث أنها تعتمد على فحص مساواة الصيغ، وبالتالي يجب أن تتضمن البراهين كلاً من الحالة حيث تكون المساواة كما هو متوقع، والحالة المنحطة.

تم إعطاء تنفيذ للمنطق القضوي الكلاسيكي بأسلوب الاستنتاج الطبيعي في [5]. بينما يستخدم هذا (شيء مكافئ لـ) القوائم، فإنه يتطلب استخداماً متكرراً لقواعد استنتاج إضافية لإضعاف السياق. هذا لن يكون مناسباً لمساعد الاستنتاج الطبيعي، كما أنه لا يحل المشاكل المذكورة أعلاه للمنطق من الدرجة الأولى.

يمكن استخدام المحمولات لتخزين مجموعات من القيم، بطريقة فهم المجموعات. نعرّف النوع Ensemble كاسم آخر لـ Pred. سيتم استخدامه للإشارة إلى المحمولات التي تم إنشاؤها بطريقة ستتبع. هذا فقط لسهولة الفهم، وليس قيداً فعلياً. ستشبه Ensembles المجموعات المحدودة.

```agda
Ensemble : Set → Set₁
Ensemble A = A → Set
```

يتم تعريف العضوية من خلال تلبية المحمول.

```agda
infix 4 _∈_ _∉_

_∈_ : {A : Set} → A → Ensemble A → Set
α ∈ αs = αs α

_∉_ : {A : Set} → A → Ensemble A → Set
α ∉ αs = ¬(α ∈ αs)
```

تعريف معقول للمجموعة الفرعية هو 𝐴 ⊂ 𝐵 إذا ∀𝑥(𝑥 ∈ 𝐴 → 𝑥 ∈ 𝐵). ومع ذلك، سيتم تعريف بعض المجموعات باستخدام النفي. إذا كان من العبث أن يكون 𝑥 في 𝐴 (على سبيل المثال، إذا كانت 𝐴 هي المجموعة الفارغة)، فإن برهان أن 𝑥 ∈ 𝐵 يمكن القيام به إما عن طريق مطابقة الأنماط لحالة فارغة، أو باستخدام اللمة ⊥-elim. ومع ذلك، بحث البرهان في Agda لن يقوم بمطابقة الأنماط داخل تعابير لامبدا، ولن يجد اللمات ما لم يتم تلميحه للقيام بذلك. للراحة، نتبنى ترجمة المنطق الأدنى عن طريق أخذ النفي المزدوج للجانب الأيمن من التضمين، مما يحل هذه المشكلة.

```agda
infix 4 _⊂_

_⊂_ : {A : Set} → Ensemble A → Ensemble A → Set
αs ⊂ βs = ∀ x → x ∈ αs → ¬(x ∉ βs)
```

يتم تعريف المجموعة الفارغة والمجموعات المفردة بالطريقة الواضحة.

```agda
∅ : {A : Set} → Ensemble A
∅ = λ _ → ⊥

⟨_⟩ : {A : Set} → A → Ensemble A
⟨ α ⟩ = λ x → x ≡ α
```

سيكون من المعقول تعريف الاتحاد من حيث نوع اتحاد منفصل، بحيث يكون برهان 𝑥 ∈ 𝐴 ∪ 𝐵 إما برهان 𝑥 ∈ 𝐴 أو 𝑥 ∈ 𝐵. ومع ذلك، نريد أن يملأ بحث البرهان في Agda البراهين المتعلقة بالمجموعات الفرعية. بالنسبة لبرهان أن 𝐴 ∪ 𝐵 ⊂ 𝐴 ∪ 𝐵 ∪ ∅، سنضطر إلى القيام بتحليل حالات على برهان 𝑥 ∈ 𝐴 ∪ 𝐵. بدلاً من ذلك نعرّف 𝑥 ∈ 𝐴 ∪ 𝐵 باستخدام الدوال، بحيث لا تكون مطابقة الأنماط ضرورية من أجل الاستفادة من مثل هذا البرهان. تعريف واحد يتضمن فقط الدوال هو 𝑥 ∈ 𝐴 ∪ 𝐵 ≔ 𝑥 ∉ 𝐴 → 𝑥 ∈ 𝐵. نأخذ النفي المزدوج للجانب الأيمن من التضمين، لنفس الأسباب أعلاه.

```agda
infixr 5 _∪_

_∪_ : {A : Set} → Ensemble A → Ensemble A → Ensemble A
(αs ∪ βs) = λ x → x ∉ αs → ¬(x ∉ βs)
```

بدلاً من تعريف فرق المجموعات، نعرّف تدويناً لإزالة عنصر واحد من مجموعة. نظراً لأن المجموعات ستستخدم فقط للمجموعات المحدودة، فهذا ليس قيداً. تعريف باستخدام العطف هو أن 𝑥 ∈ 𝐴 − 𝑎 يعني 𝑥 ∈ 𝐴 و 𝑥 ≠ 𝑎. ترجمة هذا إلى الدوال يعطي 𝑥 ∈ 𝐴 − 𝑎 ≔ ¬(𝑥 ∈ 𝐴 → 𝑥 ≡ 𝑎). خذ التناقض العكسي للتضمين الداخلي.

```agda
infixl 5 _-_

_-_ : {A : Set} → Ensemble A → A → Ensemble A
(αs - α) = λ x → ¬(x ≢ α → x ∉ αs)
```

هذه التعريفات تسمح لقضايا المجموعات الفرعية بأن يتم برهانها دون تحليل الحالات أو ⊥-elim (EFQ)، من خلال اعتماد تعريفات دالية واستخدام النفي المزدوج. علاوة على ذلك، المكمم الوحيد المستخدم في التعريفات هو في تعريف _⊂_. نظراً لأن الدوال مكافئة للتضمينات، فقد ترجمنا مفهوم المجموعة الفرعية إلى قضية من الشكل ∀𝑥𝐴، حيث 𝐴 هي صيغة في الشظية التضمينية للمنطق الأدنى. هذا متوقع، حيث أننا أردنا أن تكون حدود البرهان حدود حساب لامبدا المطبوعة ببساطة، والتي تكافئ بدقة المنطق الأدنى [11].

يمكن الآن حل براهين المجموعات الفرعية بواسطة Agda تلقائياً، بأداء جيد. في حالة جميع براهين الاستنتاج الطبيعي التالية، حلت Agda برهان المجموعة الفرعية في أقل من ثانية واحدة (الحد الزمني الافتراضي لبحث البرهان). علاوة على ذلك، نظراً لأن الشظية التضمينية للمنطق الأدنى قابلة للتقرير، هناك خوارزميات بحث البرهان التي ستجد دائماً برهاناً إذا كان موجوداً [15].

بالطبع، المجموعات هي فقط محمولات، لذا يمكن إنشاؤها بأي طريقة يمكن بها إنشاء الدوال. يمكننا تعريف نوع لتتبع إنشاء محمول، للتأكد من أنه تم إنشاؤه باستخدام (شيء مساوٍ لـ) الدوال أعلاه. بالإضافة إلى ذلك، يتطلب النوع أن يكون المحمول على نوع بمساواة قابلة للتقرير.

```agda
data Assembled {A : Set} (eq : Decidable≡ A) : Pred A → Set₁ where
  from∅   : Assembled eq ∅
  from⟨_⟩ : (α : A) → Assembled eq (⟨ α ⟩)
  from_∪_ : ∀{αs βs} → Assembled eq αs → Assembled eq βs
          → Assembled eq (αs ∪ βs)
  from_-_ : ∀{αs}    → Assembled eq αs → (α : A) → Assembled eq (αs - α)
```

**قضية 7.0.1.** المجموعات المجمعة لها عضوية قابلة للتقرير.

**البرهان.**

```agda
dec∈ : {A : Set} {eq : Decidable≡ A} {αs : Ensemble A}
     → (x : A) → Assembled eq αs → Dec (x ∈ αs)
```

لا شيء في المجموعة الفارغة.

```agda
dec∈ x from∅ = no λ x∈∅ → x∈∅
```

عضوية المفرد معرفة بمساواة، وبالتالي فإن قابليتها للتقرير هي فقط المساواة القابلة للتقرير من Assembled.

```agda
dec∈ {_} {eq} x (from⟨ α ⟩) = eq x α
```

للتحقق من العضوية لاتحاد، ببساطة تحقق أولاً من العضوية في المجموعة اليسرى، ثم اليمنى. براهين تعابير لامبدا المعطاة هنا غير تافهة، وصعبة التفسير، لكن يمكن توفيرها بواسطة بحث البرهان في Agda.

```agda
dec∈ x (from Aαs ∪ Aβs)  with dec∈ x Aαs
...  | yes x∈αs  = yes λ x∉αs _ → x∉αs x∈αs
...  | no x∉αs  with dec∈ x Aβs
...    | yes x∈βs  = yes λ _ x∉βs → x∉βs x∈βs
...    | no x∉βs   = no λ x∉αs∪βs → x∉αs∪βs x∉αs x∉βs
```

أخيراً، في حالة إزالة عنصر، استخدم المساواة القابلة للتقرير من Assembled للتحقق إذا تمت إزالة العنصر المعطى، وإلا تحقق إذا كان العنصر المعطى في المجموعة الداخلية.

```agda
dec∈ {_} {eq} x (from Aαs - α)  with eq x α
...  | yes refl  = no λ α∈αs-α → α∈αs-α λ α≢α _ → α≢α refl
...  | no x≢α  with dec∈ x Aαs
...    | yes x∈αs  = yes λ x≢α→x∉αs → x≢α→x∉αs x≢α x∈αs
...    | no x∉αs   = no λ x∈αs-α
                       → x∈αs-α (λ _ _ → x∈αs-α (λ _ _ → x∈αs-α (λ _ → x∉αs)))
```

بإعطاء مجموعة 𝐴، تعريف معقول لمحمول 𝑃 يسري على كل عنصر من 𝐴 سيكون ∀𝑥(𝑥 ∈ 𝐴 → 𝑃 𝑥). ومع ذلك، بالنسبة للمحمولات المعرفة استقرائياً (مثل _notFreeIn α لبعض 𝛼)، هذا ليس سهل العمل معه، سواء يدوياً أو باستخدام بحث البرهان. على سبيل المثال، لبرهان أن المتغير 𝑦 ليس حراً في جميع أعضاء {∀𝑦𝑄𝑦} ∪ {⊥}، سيكون من الضروري إظهار أن كل عضو يساوي إما ∀𝑦𝑄𝑦 أو ⊥، وفقط بعد ذلك توفير البناة المطلوبة لكل حالة. مرة أخرى، هذا يتطلب مطابقة الأنماط.

بدلاً من ذلك، بالنسبة لمجموعة مجمعة، نعطي تعريفاً لـ All يستخدم بنية المجموعة، ويصف أي حساب يجب إجراؤه للتحقق من أن محمولاً يسري على جميع الأعضاء. للقيام بذلك، حافظ على قائمة بجميع العناصر التي تمت إزالتها من المجموعة.

```agda
infixr 5 _all∪_

data All_[_∖_] {A : Set} (P : Pred A) : Ensemble A → List A → Set₁ where
  all∅ : ∀{xs}
       → All P [ ∅ ∖ xs ]
```

𝑃 يسري على الكل من مفرد إذا كان يسري على عنصر المفرد، أو خلاف ذلك إذا تمت إزالة ذلك العنصر بالفعل.

```agda
  all⟨_⟩  : ∀{α xs}
          → P α
          → All P [ ⟨ α ⟩ ∖ xs ]
  all⟨-_⟩ : ∀{α xs}
          → α List.∈ xs → All P [ ⟨ α ⟩ ∖ xs ]
```

في حالة اتحاد، 𝑃 يجب أن يسري على كلا جانبي الاتحاد.

```agda
  _all∪_  : ∀{αs βs xs} → All P [ αs ∖ xs ] → All P [ βs ∖ xs ]
          → All P [ αs ∪ βs ∖ xs ]
```

أخيراً، عندما يتم إنشاء مجموعة عن طريق إزالة عنصر من أخرى، تحقق من أن 𝑃 يسري على المجموعة الأخرى لجميع القيم غير المحذوفة.

```agda
  all-_   : ∀{αs x xs}
          → All P [ αs ∖ x ∷ xs ] → All P [ αs - x ∖ xs ]
```

الآن، 𝑃 يسري على الكل من 𝛼𝑠 إذا كان يسري وفقاً للإجراء أعلاه، مع قائمة العناصر المحذوفة تبدأ فارغة.

```agda
All : {A : Set} → Pred A → Ensemble A → Set₁
All P αs = All P [ αs ∖ [] ]
```

**قضية 7.0.2.** تعريف All للمجموعات المجمعة أضعف من تعريف المجموعة المعتاد.

**البرهان.** نستخدم لمة لإظهار أن هذا هو الحال لجميع قيم قائمة العناصر المحذوفة، ونطبقها على حالة القائمة الفارغة.

```agda
fAll→All : {A : Set} {eq : Decidable≡ A} {P : Pred A} {αs : Ensemble A}
         → Assembled eq αs → (∀ x → x ∈ αs → P x) → All P αs
fAll→All {A} {eq} {P} Aαs fall = φ Aαs [] (λ x x∈αs _ → fall x x∈αs)
  where
    φ : ∀{αs} → Assembled eq αs → ∀ xs
      → (∀ x → x ∈ αs → x List.∉ xs → P x) → All P [ αs ∖ xs ]
    φ from∅ xs fall∅ = all∅
```

بالنسبة لمفرد {𝛼}، إما تمت إزالة 𝛼، أو خلاف ذلك لم تتم إزالته، في هذه الحالة نستخدم الكل الدالي لبرهان 𝑃 𝛼.

```agda
    φ from⟨ α ⟩ xs fall⟨α⟩  with List.dec∈ eq α xs
    ...  | yes α∈xs  = all⟨- α∈xs ⟩
    ...  | no α∉xs   = all⟨ fall⟨α⟩ α refl α∉xs ⟩
```

نظراً لأن الاتحادات معرفة باستخدام نفي مزدوج، لإظهار أن الكل الدالي لاتحاد يعني الكل الدالي لكل من المجموعتين، استخدم تناقضاً لكل منهما.

```agda
    φ (from Aαs ∪ Aβs) xs fallαs∪βs = (φ Aαs xs fallαs)
                                      all∪ (φ Aβs xs fallβs)
      where
        fallαs : _
        fallαs x x∈αs = fallαs∪βs x (λ x∉αs _   → x∉αs x∈αs)
        fallβs : _
        fallβs x x∈βs = fallαs∪βs x (λ _   x∉βs → x∉βs x∈βs)
```

في حالة 𝛼𝑠 − 𝛼، نظهر أولاً أنه إذا كان 𝑥 ∈ 𝛼𝑠 فإن 𝑥 ∈ 𝛼𝑠 − 𝛼، وأنه إذا كان 𝑥 ∉ 𝛼 ∷ 𝑥𝑠 فإن 𝑥 ∉ 𝑥𝑠.

```agda
    φ (from Aαs - α) xs fallαs-α = all- (φ Aαs (α ∷ xs) fallαs)
      where
        fallαs : _
        fallαs x x∈αs x∉α∷xs =
          let x∈αs-α : _
              x∈αs-α x≢α→x∉αs = x≢α→x∉αs (λ x≢α → x∉α∷xs List.[ x≢α ]) x∈αs
              x∉xs : x List.∉ xs
              x∉xs x∈xs = x∉α∷xs (α ∷ x∈xs)
          in fallαs-α x x∈αs-α x∉xs
```

لا يمكن برهان العكس؛ All في الواقع أضعف بشكل صارم من التعريف الدالي. بينما يمكن أن يُتوقع أن مطابقة الأنماط على كل من All و Assembled ستؤدي إلى برهان، فإن هذا لن ينجح لأن Agda لا يمكنها توحيد أنواع الدوال. على سبيل المثال، في حالة أن مجموعة تم تجميعها بواسطة from Aαs ∪ Aβs، تحليل حالات برهان All P (αs ∪ βs) لا يظهر أن الباني الوحيد هو _all∪_؛ Agda لا يمكنها تحديد أن λ x → x ∉ αs → ¬(x ∉ βs) لا يتوحد مع λ _ → ⊥، لذا فإن all∅ قد يكون أو لا يكون بانياً. إذا أردنا نوعاً أقوى يكافئ التعريف الدالي، فإن البنية المجمعة ستحتاج إلى أن تُدرج في All.

يمكننا استخدام المحمول All لتعريف القيد بأن بعض الاستنتاجات صالحة فقط إذا لم يكن متغير معين حراً في مجموعة من الافتراضات المفتوحة. بالنسبة لحالة الاستخدام المعتادة (أي الحالات بخلاف التلاعب المجرد بشجرة البرهان حيث يتم تحديد حرية المتغير بواسطة بعض اللمات)، سيجد بحث البرهان في Agda البرهان المطلوب. ومع ذلك، بسبب القيود أعلاه مع توحيد الدوال، لا ترى Agda أن هناك بانياً واحداً فقط لكل مجموعة غير مفردة، لذا فإن خوارزمية البحث ليست سريعة. بالنسبة لأشجار البرهان الأكبر، من الضروري زيادة المهلة الزمنية من الثانية الواحدة الافتراضية إلى عشر ثوانٍ. يمكن حل هذا أيضاً من خلال تضمين البنية المجمعة في All.

### Translation Metrics
- **Quality**: High (estimated 0.89)
- **Completeness**: Full section translated
- **Technical terminology**: Consistent with glossary
- **Note**: Complex functional definitions for subset and union using minimal logic
