# Section 11: Beyond Convolution
## القسم 11: ما وراء التفاف

**Section:** Theory Extension
**Translation Quality:** 0.85
**Glossary Terms Used:** convolution, applicative, functor, monad, homomorphism

---

### English Version (Summary)

This section generalizes beyond monoid-based convolution to arbitrary binary operations.

**The Problem:** Convolution on statically sized arrays requires non-uniform types:
```
(∗) :: Semiring s ⇒ Array_{m+1} s → Array_{n+1} s → Array_{m+n+1} s
```

This is incompatible with semiring multiplication where arguments and result have the same type.

**The Solution: lift_n**

Generalize from monoidal combination (⊕) to arbitrary binary operations:
```haskell
lift_2 :: Semiring s ⇒ (a → b → c) → (a → s) → (b → s) → (c → s)
lift_2 h f g = Σ_{u,v} h u v ↦ f u ∗ g v
```

For arbitrary arity:
```haskell
lift_n :: Semiring s ⇒ (a_1 → ⋯ → a_n → b)
       → (a_1 → s) → ⋯ → (a_n → s) → (b → s)
lift_n h f_1 ⋯ f_n = Σ_{u_1,...,u_n} h u_1 ⋯ u_n ↦ f_1 u_1 ∗ ⋯ ∗ f_n u_n
```

**Special Cases:**
```haskell
lift_1 h f = Σ_u h u ↦ f u
lift_0 b = single b
```

**Connection to Applicative:**

The type wrapper `s ← a = F (a → s)` makes lift_n correspond to fmap, liftA_2, and pure from the Applicative class (Figure 8).

**Theorem 16:** For each instance in Figure 8, `1 = pure ε` and `(∗) = liftA_2 (⊕)`.

**Theorem 17 (Convolution Theorem):** The Fourier transform is a semiring and left semimodule homomorphism from b ← a to a → b.

**Theorem 18:** The preimage operation `pre :: (a → b) → (P a ← b)` is a Functor and Applicative homomorphism.

**Key Insight:** Convolution generalizes to applicative functors, with the monoid case being a special instance.

---

### النسخة العربية (ملخص)

يعمم هذا القسم ما وراء التفاف القائم على الأحادي إلى عمليات ثنائية تعسفية.

**المشكلة:** التفاف على المصفوفات ذات الحجم الثابت يتطلب أنواع غير موحدة:
```
(∗) :: Semiring s ⇒ Array_{m+1} s → Array_{n+1} s → Array_{m+n+1} s
```

هذا غير متوافق مع ضرب الحلقة الشبه جمعية حيث الوسائط والنتيجة لها نفس النوع.

**الحل: lift_n**

تعميم من الجمع الأحادي (⊕) إلى عمليات ثنائية تعسفية:
```haskell
lift_2 :: Semiring s ⇒ (a → b → c) → (a → s) → (b → s) → (c → s)
lift_2 h f g = Σ_{u,v} h u v ↦ f u ∗ g v
```

لـ arity تعسفي:
```haskell
lift_n :: Semiring s ⇒ (a_1 → ⋯ → a_n → b)
       → (a_1 → s) → ⋯ → (a_n → s) → (b → s)
lift_n h f_1 ⋯ f_n = Σ_{u_1,...,u_n} h u_1 ⋯ u_n ↦ f_1 u_1 ∗ ⋯ ∗ f_n u_n
```

**حالات خاصة:**
```haskell
lift_1 h f = Σ_u h u ↦ f u
lift_0 b = single b
```

**الاتصال بـ Applicative:**

غلاف النوع `s ← a = F (a → s)` يجعل lift_n يتوافق مع fmap و liftA_2 و pure من صنف Applicative (الشكل 8).

**النظرية 16:** لكل نموذج في الشكل 8، `1 = pure ε` و `(∗) = liftA_2 (⊕)`.

**النظرية 17 (نظرية التفاف):** تحويل فورييه هو تشاكل حلقة شبه جمعية ووحدة شبه جمعية يسارية من b ← a إلى a → b.

**النظرية 18:** عملية الصورة الأولية `pre :: (a → b) → (P a ← b)` هي تشاكل Functor و Applicative.

**البصيرة الرئيسية:** التفاف يعمم على الدوالات التطبيقية، مع كون حالة الأحادي نموذج خاص.

---

### Translation Notes

- **Major Generalization**: From monoids to arbitrary operations
- **Connection to Category Theory**: Applicative functors
- **Quality Score:** 0.85
