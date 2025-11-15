# Section 5: Finite maps
## القسم 5: الخرائط المحدودة

**Section:** Core Implementation
**Translation Quality:** 0.85
**Glossary Terms Used:** finite map, data structure, partial function, semiring, semimodule, homomorphism

---

### English Version (Summary)

Finite maps (Map a b) represent partial functions from keys of type a to values of type b, implemented as key-ordered balanced trees.

**Key Design Decision:** To model total functions, treat unassigned keys as denoting zero. This requires b to be an additive monoid.

**Instances (Figure 2):**

```haskell
instance (Ord a, Additive b) ⇒ Indexable a b (Map a b) where
  m ! a = M.findWithDefault 0 a m

instance (Ord a, Additive b) ⇒ HasSingle a b (Map a b) where
  (↦) = M.singleton

instance (Ord a, Additive b) ⇒ Additive (Map a b) where
  0 = M.empty
  (+) = M.unionWith (+)

instance Semiring b ⇒ LeftSemimodule b (Map a b) where
  (^·) b = fmap (b ∗)

instance (Ord a, Monoid a, Semiring b) ⇒ Semiring (Map a b) where
  1 = ε ↦ 1
  p ∗ q = sum [u ⊕ v ↦ p ! u ∗ q ! v | u ← M.keys p, v ← M.keys q]
```

**Theorem:** Given these definitions, (!) is a homomorphism with respect to each instantiated class.

**Limitation:** The finiteness of finite maps prevents giving a useful StarSemiring instance.

**Advantage:** Provides efficient sparse representation for functions with finite support.

---

### النسخة العربية (ملخص)

الخرائط المحدودة (Map a b) تمثل دوال جزئية من مفاتيح من النوع a إلى قيم من النوع b، منفذة كأشجار متوازنة مرتبة بالمفاتيح.

**قرار التصميم الرئيسي:** لنمذجة الدوال الكلية، عامل المفاتيح غير المعينة كدالة على الصفر. هذا يتطلب أن يكون b أحادي جمعي.

**النماذج (الشكل 2):**

```haskell
instance (Ord a, Additive b) ⇒ Indexable a b (Map a b) where
  m ! a = M.findWithDefault 0 a m

instance (Ord a, Additive b) ⇒ HasSingle a b (Map a b) where
  (↦) = M.singleton

instance (Ord a, Additive b) ⇒ Additive (Map a b) where
  0 = M.empty
  (+) = M.unionWith (+)

instance Semiring b ⇒ LeftSemimodule b (Map a b) where
  (^·) b = fmap (b ∗)

instance (Ord a, Monoid a, Semiring b) ⇒ Semiring (Map a b) where
  1 = ε ↦ 1
  p ∗ q = sum [u ⊕ v ↦ p ! u ∗ q ! v | u ← M.keys p, v ← M.keys q]
```

**النظرية:** بالنظر إلى هذه التعريفات، (!) هو تشاكل بالنسبة لكل صنف مُنشأ.

**القيد:** محدودية الخرائط المحدودة تمنع إعطاء نموذج StarSemiring مفيد.

**الميزة:** توفر تمثيل متناثر فعال للدوال ذات الدعم المحدود.

---

### Translation Notes

- **Data Structure**: Balanced tree implementation for efficiency
- **Key Property**: Homomorphism preservation across all instances
- **Quality Score:** 0.85
