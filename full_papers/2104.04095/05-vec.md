# Section 5: Vec.lagda
## القسم 5: Vec.lagda

### English

Vectors are similar to lists, but the type is indexed by length. For example, vectors in ℕ² are of different type to vectors in ℕ³.

```agda
data Vec (A : Set) : ℕ → Set where
  [] : Vec A zero
  _∷_ : ∀{n} → A → Vec A n → Vec A (suc n)
```

We define All, Any, and membership the same way as for lists. The decidability proofs below are omitted, as they are identical to the corresponding proofs for lists.

```agda
data All {A : Set} (P : Pred A) : ∀{n} → Vec A n → Set where
  [] : All P []
  _∷_ : ∀{x n} {xs : Vec A n} → P x → All P xs → All P (x ∷ xs)

decAll : ∀{A n P} → (p : Decidable P) → (xs : Vec A n) → Dec (All P xs)
-- Proof omitted.

data Any {A : Set} (P : Pred A) : ∀{n} → Vec A n → Set where
  [_] : ∀{n x} {xs : Vec A n} → P x → Any P (x ∷ xs)
  _∷_ : ∀{n} {xs : Vec A n} → (x : A) → Any P xs → Any P (x ∷ xs)

decAny : ∀{A n P} → (p : Decidable P) → (xs : Vec A n) → Dec (Any P xs)
-- Proof omitted.
```

```agda
infix 4 _∈_ _∉_

_∈_ : {A : Set} {n : ℕ} → (x : A) → Vec A n → Set
x ∈ xs = Any (x ≡_) xs

_∉_ : {A : Set} {n : ℕ} → (x : A) → Vec A n → Set
x ∉ xs = ¬(x ∈ xs)

dec∈ : ∀{A n} → Decidable≡ A → (x : A) → (xs : Vec A n) → Dec (x ∈ xs)
dec∈ _≟_ x xs = decAny (x ≟_) xs
```

### Arabic Translation

المتجهات تشبه القوائم، لكن النوع مفهرس بالطول. على سبيل المثال، المتجهات في ℕ² هي من نوع مختلف عن المتجهات في ℕ³.

```agda
data Vec (A : Set) : ℕ → Set where
  [] : Vec A zero
  _∷_ : ∀{n} → A → Vec A n → Vec A (suc n)
```

نعرّف All و Any والعضوية بنفس الطريقة كما في القوائم. براهين قابلية التقرير أدناه محذوفة، لأنها مماثلة للبراهين المقابلة للقوائم.

```agda
data All {A : Set} (P : Pred A) : ∀{n} → Vec A n → Set where
  [] : All P []
  _∷_ : ∀{x n} {xs : Vec A n} → P x → All P xs → All P (x ∷ xs)

decAll : ∀{A n P} → (p : Decidable P) → (xs : Vec A n) → Dec (All P xs)
-- البرهان محذوف.

data Any {A : Set} (P : Pred A) : ∀{n} → Vec A n → Set where
  [_] : ∀{n x} {xs : Vec A n} → P x → Any P (x ∷ xs)
  _∷_ : ∀{n} {xs : Vec A n} → (x : A) → Any P xs → Any P (x ∷ xs)

decAny : ∀{A n P} → (p : Decidable P) → (xs : Vec A n) → Dec (Any P xs)
-- البرهان محذوف.
```

```agda
infix 4 _∈_ _∉_

_∈_ : {A : Set} {n : ℕ} → (x : A) → Vec A n → Set
x ∈ xs = Any (x ≡_) xs

_∉_ : {A : Set} {n : ℕ} → (x : A) → Vec A n → Set
x ∉ xs = ¬(x ∈ xs)

dec∈ : ∀{A n} → Decidable≡ A → (x : A) → (xs : Vec A n) → Dec (x ∈ xs)
dec∈ _≟_ x xs = decAny (x ≟_) xs
```

### Back-Translation

Vectors are similar to lists, but the type is indexed by length. For example, vectors in ℕ² are of a different type than vectors in ℕ³.

```agda
data Vec (A : Set) : ℕ → Set where
  [] : Vec A zero
  _∷_ : ∀{n} → A → Vec A n → Vec A (suc n)
```

We define All, Any, and membership in the same way as for lists. The decidability proofs below are omitted, as they are identical to the corresponding proofs for lists.

```agda
data All {A : Set} (P : Pred A) : ∀{n} → Vec A n → Set where
  [] : All P []
  _∷_ : ∀{x n} {xs : Vec A n} → P x → All P xs → All P (x ∷ xs)

decAll : ∀{A n P} → (p : Decidable P) → (xs : Vec A n) → Dec (All P xs)
-- Proof omitted.

data Any {A : Set} (P : Pred A) : ∀{n} → Vec A n → Set where
  [_] : ∀{n x} {xs : Vec A n} → P x → Any P (x ∷ xs)
  _∷_ : ∀{n} {xs : Vec A n} → (x : A) → Any P xs → Any P (x ∷ xs)

decAny : ∀{A n P} → (p : Decidable P) → (xs : Vec A n) → Dec (Any P xs)
-- Proof omitted.
```

```agda
infix 4 _∈_ _∉_

_∈_ : {A : Set} {n : ℕ} → (x : A) → Vec A n → Set
x ∈ xs = Any (x ≡_) xs

_∉_ : {A : Set} {n : ℕ} → (x : A) → Vec A n → Set
x ∉ xs = ¬(x ∈ xs)

dec∈ : ∀{A n} → Decidable≡ A → (x : A) → (xs : Vec A n) → Dec (x ∈ xs)
dec∈ _≟_ x xs = decAny (x ≟_) xs
```

### Translation Metrics
- **Quality**: High (estimated 0.90)
- **Completeness**: Full section translated
- **Technical terminology**: Consistent with glossary
