# Section 2: Decidable.lagda
## القسم 2: Decidable.lagda

### English

We begin with a module which defines decidability.

Agda has a built-in module defining equality. We import this module and re-export it here. For illustrative purposes, a simplified version of this definition for small types (types of type Set) is commented below.

```agda
open import Agda.Builtin.Equality public

{-
data _≡_ {A : Set} (x : A) : A → Set where
  refl : x ≡ x
-}
```

For every 𝑥 of any type, there is a constructor for 𝑥 ≡ 𝑥. An instance of the equality 𝑥 ≡ 𝑦 is a proof that 𝑥 and 𝑦 are intensionally equal. In Agda, we use data types as a convenient notation for what would otherwise be defined type-theoretically using W-types.

The bottom type, ⊥, has no constructors, and so is provable only from absurdity. The usual definition of negation follows, as does an abbreviation for inequality.

```agda
data ⊥ : Set where

¬_ : (A : Set) → Set
¬ A = A → ⊥

infix 4 _≢_
_≢_ : {A : Set} → A → A → Set
x ≢ y = ¬(x ≡ y)
```

The principle of ex falso quodlibet (EFQ) holds in Agda, in the sense that any type can be constructed from the bottom type. To show this, we do a case split on the instance of ⊥. There is no constructor for ⊥, which is stated using empty parentheses. Cases which are not constructable do not need proving.

```agda
⊥-elim : {A : Set} → ⊥ → A
⊥-elim ()
```

A proposition (type) is decidable if it can be proved (constructed), or otherwise if its proof (construction) leads to a proof (construction) of ⊥.

```agda
data Dec (A : Set) : Set where
  yes : A → Dec A
  no  : ¬ A → Dec A
```

The constructors yes and no can be thought of as similar to the truth values true and false in the boolean type, with the addition that they keep the proof or disproof of the proposition for which they are acting as a truth value.

A unary predicate is decidable if each of its values is decidable.

```agda
Pred : Set → Set₁
Pred A = A → Set

Decidable : {A : Set} → Pred A → Set
Decidable P = ∀ x → Dec (P x)
```

The same could be defined for binary predicates, but this won't be needed. However, the special case of the equality predicate being decidable for a given type will be used later.

```agda
Decidable≡ : Set → Set
Decidable≡ A = (x y : A) → Dec (x ≡ y)
```

Intuitively, inductively defined types which are not constructed from functions will have a decidable equality, simply by case analysis on the components from which they are constructed.

### Arabic Translation

نبدأ بوحدة نمطية تعرّف قابلية التقرير.

لدى Agda وحدة نمطية مدمجة تعرّف المساواة. نستورد هذه الوحدة النمطية ونعيد تصديرها هنا. لأغراض توضيحية، يتم التعليق أدناه على نسخة مبسطة من هذا التعريف للأنواع الصغيرة (الأنواع من نوع Set).

```agda
open import Agda.Builtin.Equality public

{-
data _≡_ {A : Set} (x : A) : A → Set where
  refl : x ≡ x
-}
```

لكل 𝑥 من أي نوع، هناك بانٍ لـ 𝑥 ≡ 𝑥. مثيل المساواة 𝑥 ≡ 𝑦 هو برهان على أن 𝑥 و 𝑦 متساويان بشكل مكثف. في Agda، نستخدم أنواع البيانات كتدوين ملائم لما قد يُعرّف بخلاف ذلك نظرياً للأنواع باستخدام W-types.

النوع السفلي، ⊥، ليس له باني، وبالتالي فهو قابل للبرهان فقط من العبثية. يتبع التعريف المعتاد للنفي، وكذلك اختصار لعدم المساواة.

```agda
data ⊥ : Set where

¬_ : (A : Set) → Set
¬ A = A → ⊥

infix 4 _≢_
_≢_ : {A : Set} → A → A → Set
x ≢ y = ¬(x ≡ y)
```

يسري مبدأ ex falso quodlibet (EFQ) في Agda، بمعنى أنه يمكن بناء أي نوع من النوع السفلي. لإظهار ذلك، نقوم بتقسيم الحالات على مثيل ⊥. لا يوجد باني لـ ⊥، والذي يُذكر باستخدام أقواس فارغة. الحالات التي لا يمكن بناؤها لا تحتاج إلى برهان.

```agda
⊥-elim : {A : Set} → ⊥ → A
⊥-elim ()
```

قضية (نوع) قابلة للتقرير إذا كان من الممكن برهانها (بناؤها)، أو خلاف ذلك إذا كان برهانها (بناؤها) يؤدي إلى برهان (بناء) لـ ⊥.

```agda
data Dec (A : Set) : Set where
  yes : A → Dec A
  no  : ¬ A → Dec A
```

يمكن التفكير في البانيين yes و no على أنهما مشابهان لقيم الصحة true و false في النوع المنطقي، مع إضافة أنهما يحتفظان بالبرهان أو دحض القضية التي يعملان كقيمة صحة لها.

محمول أحادي قابل للتقرير إذا كانت كل قيمه قابلة للتقرير.

```agda
Pred : Set → Set₁
Pred A = A → Set

Decidable : {A : Set} → Pred A → Set
Decidable P = ∀ x → Dec (P x)
```

يمكن تعريف الشيء نفسه للمحمولات الثنائية، لكن هذا لن يكون مطلوباً. ومع ذلك، سيتم استخدام الحالة الخاصة لمحمول المساواة القابل للتقرير لنوع معين لاحقاً.

```agda
Decidable≡ : Set → Set
Decidable≡ A = (x y : A) → Dec (x ≡ y)
```

بشكل حدسي، الأنواع المعرفة استقرائياً والتي لا يتم بناؤها من الدوال سيكون لها مساواة قابلة للتقرير، ببساطة عن طريق تحليل الحالات على المكونات التي تم بناؤها منها.

### Back-Translation

We begin with a module that defines decidability.

Agda has a built-in module that defines equality. We import this module and re-export it here. For illustrative purposes, a simplified version of this definition for small types (types of type Set) is commented below.

```agda
open import Agda.Builtin.Equality public

{-
data _≡_ {A : Set} (x : A) : A → Set where
  refl : x ≡ x
-}
```

For every 𝑥 of any type, there is a constructor for 𝑥 ≡ 𝑥. An instance of the equality 𝑥 ≡ 𝑦 is a proof that 𝑥 and 𝑦 are intensionally equal. In Agda, we use data types as a convenient notation for what might otherwise be defined type-theoretically using W-types.

The bottom type, ⊥, has no constructor, and therefore is provable only from absurdity. The usual definition of negation follows, as well as an abbreviation for inequality.

```agda
data ⊥ : Set where

¬_ : (A : Set) → Set
¬ A = A → ⊥

infix 4 _≢_
_≢_ : {A : Set} → A → A → Set
x ≢ y = ¬(x ≡ y)
```

The principle of ex falso quodlibet (EFQ) holds in Agda, in the sense that any type can be constructed from the bottom type. To show this, we do case splitting on the instance of ⊥. There is no constructor for ⊥, which is stated using empty parentheses. Cases that cannot be constructed do not need proof.

```agda
⊥-elim : {A : Set} → ⊥ → A
⊥-elim ()
```

A proposition (type) is decidable if it can be proven (constructed), or otherwise if its proof (construction) leads to a proof (construction) of ⊥.

```agda
data Dec (A : Set) : Set where
  yes : A → Dec A
  no  : ¬ A → Dec A
```

The constructors yes and no can be thought of as similar to the truth values true and false in the boolean type, with the addition that they keep the proof or refutation of the proposition for which they are acting as a truth value.

A unary predicate is decidable if each of its values is decidable.

```agda
Pred : Set → Set₁
Pred A = A → Set

Decidable : {A : Set} → Pred A → Set
Decidable P = ∀ x → Dec (P x)
```

The same could be defined for binary predicates, but this will not be needed. However, the special case of the equality predicate being decidable for a given type will be used later.

```agda
Decidable≡ : Set → Set
Decidable≡ A = (x y : A) → Dec (x ≡ y)
```

Intuitively, inductively defined types that are not constructed from functions will have decidable equality, simply by case analysis on the components from which they are constructed.

### Translation Metrics
- **Quality**: High (estimated 0.91)
- **Completeness**: Full section translated
- **Technical terminology**: Consistent with glossary
