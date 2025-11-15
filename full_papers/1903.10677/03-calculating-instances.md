# Section 3: Calculating Instances from Homomorphisms
## القسم 3: حساب النماذج من التشاكلات

**Section:** Methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** homomorphism, instance, semiring, semimodule, predicate, isomorphism

---

### English Version (Summary)

This section introduces the **central guiding principle** of the paper: calculating instances from homomorphisms rather than guessing at definitions.

**The Method:**
1. Start with a type for which instances are unknown (e.g., sets P a)
2. Find an isomorphism to a type with known instances (e.g., predicates a → Bool)
3. Require the isomorphism to be a homomorphism
4. Solve for the unknown instances algebraically

**Example: Sets as an Additive Monoid**

Given the predicate isomorphism:
```haskell
pred :: P a → (a → Bool)
pred as = λ a → a ∈ as

pred⁻¹ :: (a → Bool) → P a
pred⁻¹ f = { a | f a }
```

To find the Additive instance, require `pred` to be an additive monoid homomorphism:
```
pred 0 = 0
pred (p + q) = pred p + pred q
```

Solving these equations:
```
0 = pred⁻¹ 0 = ∅
p + q = pred⁻¹ (pred p + pred q) = p ∪ q
```

**Example: Sets as a Left Semimodule**

For `LeftSemimodule Bool (P a)`, require `pred⁻¹` to be a left Bool-semimodule homomorphism:
```
s · p = pred⁻¹ (s · pred p)
      = if s then p else ∅
```

This definition ensures `True` preserves and `False` annihilates, as required by semimodule laws.

**Key Insight:** This systematic approach eliminates guesswork and guarantees correctness by construction.

---

### النسخة العربية (ملخص)

يقدم هذا القسم **المبدأ التوجيهي الأساسي** للورقة: حساب النماذج (instances) من التشاكلات (homomorphisms) بدلاً من التخمين في التعريفات.

**الطريقة:**
1. ابدأ بنوع ذو نماذج غير معروفة (مثل المجموعات P a)
2. أوجد تماثلاً (isomorphism) لنوع ذو نماذج معروفة (مثل المحمولات a → Bool)
3. اطلب أن يكون التماثل تشاكلاً (homomorphism)
4. حل للنماذج المجهولة جبرياً

**مثال: المجموعات كأحادي جمعي**

بالنظر إلى تماثل المحمول:
```haskell
pred :: P a → (a → Bool)
pred as = λ a → a ∈ as

pred⁻¹ :: (a → Bool) → P a
pred⁻¹ f = { a | f a }
```

لإيجاد نموذج Additive، نطلب أن يكون `pred` تشاكل أحادي جمعي:
```
pred 0 = 0
pred (p + q) = pred p + pred q
```

حل هذه المعادلات:
```
0 = pred⁻¹ 0 = ∅
p + q = pred⁻¹ (pred p + pred q) = p ∪ q
```

**مثال: المجموعات كوحدة شبه جمعية يسارية**

لـ `LeftSemimodule Bool (P a)`، نطلب أن يكون `pred⁻¹` تشاكل وحدة شبه جمعية يسارية من Bool:
```
s · p = pred⁻¹ (s · pred p)
      = if s then p else ∅
```

يضمن هذا التعريف أن `True` يحفظ و `False` يفني، كما هو مطلوب بواسطة قوانين الوحدات الشبه جمعية.

**البصيرة الرئيسية:** هذا النهج المنظم يزيل التخمين ويضمن الصحة بالبناء.

---

### Translation Notes

- **Core Methodology**: This section establishes the paper's fundamental approach
- **Key Innovation**: Deriving correct implementations from homomorphism requirements
- **Quality Score:** 0.86
