# Section 4: Algebra Types
## القسم 4: أنواع الجبور

**Section:** algebra types
**Translation Quality:** 0.87
**Glossary Terms Used:** algebra, signature, operation, arity, product, congruence, quotient, homomorphism, compatibility

---

### English Version (Summary)

**4 Algebra Types**

We now present the Algebras module of the AgdaUALib. Here we use type theory and Agda to codify the most basic objects of universal algebra, such as operations and signatures (§4.1), algebras (§4.2), product algebras (§4.3), congruence relations and quotient algebras (§4.4).

A popular way to represent algebraic structures in type theory is with record types. The Sigma type provides an equivalent alternative that we prefer throughout the library, both for consistency and because of its direct connection to the existential quantifier of logic. When a Sigma type Σ x : X , P is inhabited by (x, p), we conclude "there exists x in X such that P x holds;" in symbols, ∃ x ∈ X , P x. The pair (x, p) is not merely a proof but also a witness with "computational content."

**4.1 Signatures**

We define the signature of an algebraic structure in Agda as:

```
Signature : (O V : Universe) → (O ⊔ V)+⋆
Signature O V = Σ F : O⋆ , (F → V⋆)
```

The symbol O denotes the universe of operation symbol types, while V is the universe of arity types. If S : Signature O V is a signature, then | S | denotes the set of operation symbols, and ∥ S ∥ denotes the arity function. If f : | S | is an operation symbol, then ∥ S ∥ f is the arity of f.

**Example of a signature:** Here is the signature for monoids:

```
data monoid-op : O⋆ where
  e : monoid-op
  · : monoid-op

monoid-sig : Signature O U₀
monoid-sig = monoid-op , λ { e → 0; · → 2 }
```

Thus, the monoid signature consists of two operation symbols e and · where e is nullary (arity 0) and · is binary (arity 2).

**4.2 Algebras**

For a fixed signature S : Signature O V and universe U, we define the type of algebras in signature S (S-algebras) with domain of type U⋆ as:

```
Algebra : (U : Universe)(S : Signature O V) → O ⊔ V ⊔ U+⋆
Algebra U S = Σ A : U⋆ ,           -- the domain
              Π f : | S | , Op (∥ S ∥ f) A  -- the basic operations
```

Technically these are "∞-algebras" because the domain can be an arbitrary type and need not be a set. We work with general algebras throughout and assume uniqueness of identity proofs (UIP) explicitly only where needed, making dependence on UIP more transparent.

**Operation interpretation syntax:** We define convenient shorthand for operation interpretation:

```
_ˆ_ : (f : | S |)(A : Algebra U S) → (∥ S ∥ f → | A |) → | A |
f ˆ A = λ a → (∥ A ∥ f) a
```

If f : | S | is an operation symbol and a : ∥ S ∥ f → | A | is a tuple of the same arity, then (f ˆ A) a denotes operation f interpreted in A and evaluated at a.

**Lifts of algebras:** To resolve universe level issues, we provide lifting tools:

```
Lift-op : ((I → A) → A) → (W : Universe) → ((I → Lift{W} A) → Lift{W} A)
Lift-alg : Algebra U S → (W : Universe) → Algebra (U ⊔ W) S
```

The Lift-alg type preserves term identities, is a homomorphism, an algebraic invariant, and a subalgebraic invariant.

**Compatibility of binary relations:** We define compatibility of a binary relation R with all operations of algebra A:

```
compatible : (A : Algebra U S) → Rel | A | W → O ⊔ U ⊔ V ⊔ W⋆
compatible A R = ∀ f → (f ˆ A) |: R
```

**Compatibility of continuous relations:** We extend compatibility to continuous and dependent relations:

```
cont-compatible : {I : V⋆}(A : Algebra U S) → ContRel I | A | W → O ⊔ U ⊔ V ⊔ W⋆
cont-compatible A R = Π f : | S | , cont-compatible-op (f ˆ A) R

dep-compatible : {I : V⋆}(A : I → Algebra U S) → DepRel I (λ i → | A i |) W → O ⊔ U ⊔ V ⊔ W⋆
dep-compatible A R = Π f : | S | , dep-compatible-op (λ i → f ˆ (A i)) R
```

**4.3 Products**

Given a type I : I⋆ and a family A : I → Algebra U S, the product ⨅ A is the algebra whose domain is the Cartesian product Π i : I , | A i | of the domains, with operations interpreted pointwise. If f is a J-ary operation symbol and a : Π i : I , J → A i, then (f ˆ ⨅A) a := (i : I) → (f ˆ A i)(a i).

We define the product algebra type:

```
⨅ : (A : I → Algebra U S) → Algebra (O ⊔ V ⊔ U ⊔ I) S
⨅ A = (Π i : I , | A i |) , λ f a i → (f ˆ A i)(λ x → a x i)
```

This product construction is fundamental in universal algebra and is used extensively in the proof of Birkhoff's variety theorem.

**4.4 Congruences**

A congruence relation on an algebra A is an equivalence relation on | A | that is compatible with the operations of A. We represent this as:

```
Con : {U : Universe}(A : Algebra U S) → (O ⊔ V ⊔ U)+⋆
Con A = Σ θ ∶ Equivalence | A | _ , compatible A | θ |
```

**Special congruences:** The zero congruence (identity relation) is:

```
0ᶜ : (A : Algebra U S){fe : funext V U} → Con{U} A
0ᶜ A {fe} = IsCongruence→Con 0 (Δ A {fe})
```

**Quotient algebras:** Given algebra A and congruence θ, the quotient A / θ is defined with standard notation:

```
_/_ : (A : Algebra U S) → Con{W} A → Algebra (U ⊔ W+) S
A / θ = (| A | / | θ |) ,           -- domain of quotient
        λ f a → ⟦ (f ˆ A)(λ i → fst ∥ a i ∥) ⟧  -- operations of quotient
```

The quotient construction is essential for fundamental theorems in universal algebra, including the homomorphism theorems and Birkhoff's variety theorem.

---

### النسخة العربية (الملخص)

**4 أنواع الجبور**

نقدم الآن وحدة Algebras من AgdaUALib. نستخدم هنا نظرية الأنواع وAgda لترميز أبسط كائنات الجبر العام، مثل العمليات والتواقيع (§4.1)، والجبور (§4.2)، وجبور الجداء (§4.3)، وعلاقات التطابق والجبور الحاصل القسمي (§4.4).

طريقة شائعة لتمثيل البنى الجبرية في نظرية الأنواع هي باستخدام أنواع السجلات. يوفر نوع سيجما بديلاً مكافئاً نفضله في جميع أنحاء المكتبة، لكل من الاتساق ولارتباطه المباشر بالمكمم الوجودي في المنطق. عندما يكون نوع سيجما Σ x : X , P مسكوناً بـ (x, p)، نستنتج "يوجد x في X بحيث يحمل P x؛" بالرموز، ∃ x ∈ X , P x. الزوج (x, p) ليس مجرد برهان بل أيضاً شاهد ذو "محتوى حسابي."

**4.1 التواقيع**

نعرّف التوقيع للبنية الجبرية في Agda كـ:

```
Signature : (O V : Universe) → (O ⊔ V)+⋆
Signature O V = Σ F : O⋆ , (F → V⋆)
```

يدل الرمز O على كون أنواع رموز العمليات، بينما V هو كون أنواع القوى. إذا كان S : Signature O V توقيعاً، فإن | S | يدل على مجموعة رموز العمليات، و∥ S ∥ تدل على دالة القوى. إذا كان f : | S | رمز عملية، فإن ∥ S ∥ f هي قوة f.

**مثال على التوقيع:** فيما يلي التوقيع للأحاديات:

```
data monoid-op : O⋆ where
  e : monoid-op
  · : monoid-op

monoid-sig : Signature O U₀
monoid-sig = monoid-op , λ { e → 0; · → 2 }
```

وبالتالي، يتكون توقيع الأحادي من رمزي عمليات e و· حيث e صفرية القوى (القوة 0) و· ثنائية (القوة 2).

**4.2 الجبور**

لتوقيع ثابت S : Signature O V وكون U، نعرّف نوع الجبور في التوقيع S (S-جبور) بمجال من النوع U⋆ كـ:

```
Algebra : (U : Universe)(S : Signature O V) → O ⊔ V ⊔ U+⋆
Algebra U S = Σ A : U⋆ ,           -- المجال
              Π f : | S | , Op (∥ S ∥ f) A  -- العمليات الأساسية
```

هذه تقنياً "∞-جبور" لأن المجال يمكن أن يكون نوعاً عشوائياً ولا يلزم أن يكون مجموعة. نعمل مع الجبور العامة في كل مكان ونفترض وحدانية براهين الهوية (UIP) صراحة فقط حيث تكون مطلوبة، مما يجعل الاعتماد على UIP أكثر شفافية.

**صيغة تفسير العمليات:** نعرّف اختصاراً مناسباً لتفسير العمليات:

```
_ˆ_ : (f : | S |)(A : Algebra U S) → (∥ S ∥ f → | A |) → | A |
f ˆ A = λ a → (∥ A ∥ f) a
```

إذا كان f : | S | رمز عملية وa : ∥ S ∥ f → | A | هو صف بنفس القوة، فإن (f ˆ A) a يدل على العملية f المفسَّرة في A والمقيَّمة عند a.

**رفع الجبور:** لحل مشاكل مستوى الكون، نوفر أدوات رفع:

```
Lift-op : ((I → A) → A) → (W : Universe) → ((I → Lift{W} A) → Lift{W} A)
Lift-alg : Algebra U S → (W : Universe) → Algebra (U ⊔ W) S
```

يحفظ نوع Lift-alg هويات الحدود، وهو تشاكل ومتغير جبري ومتغير جبري جزئي.

**توافق العلاقات الثنائية:** نعرّف توافق علاقة ثنائية R مع جميع عمليات الجبر A:

```
compatible : (A : Algebra U S) → Rel | A | W → O ⊔ U ⊔ V ⊔ W⋆
compatible A R = ∀ f → (f ˆ A) |: R
```

**توافق العلاقات المستمرة:** نمدد التوافق إلى العلاقات المستمرة والتابعة:

```
cont-compatible : {I : V⋆}(A : Algebra U S) → ContRel I | A | W → O ⊔ U ⊔ V ⊔ W⋆
cont-compatible A R = Π f : | S | , cont-compatible-op (f ˆ A) R

dep-compatible : {I : V⋆}(A : I → Algebra U S) → DepRel I (λ i → | A i |) W → O ⊔ U ⊔ V ⊔ W⋆
dep-compatible A R = Π f : | S | , dep-compatible-op (λ i → f ˆ (A i)) R
```

**4.3 الجداءات**

بالنظر إلى نوع I : I⋆ وعائلة A : I → Algebra U S، فإن الجداء ⨅ A هو الجبر الذي مجاله الجداء الديكارتي Π i : I , | A i | للمجالات، مع تفسير العمليات نقطياً. إذا كان f رمز عملية J-القوى وa : Π i : I , J → A i، فإن (f ˆ ⨅A) a := (i : I) → (f ˆ A i)(a i).

نعرّف نوع جبر الجداء:

```
⨅ : (A : I → Algebra U S) → Algebra (O ⊔ V ⊔ U ⊔ I) S
⨅ A = (Π i : I , | A i |) , λ f a i → (f ˆ A i)(λ x → a x i)
```

هذا البناء للجداء أساسي في الجبر العام ويُستخدم على نطاق واسع في برهان مبرهنة التنوع لبيركوف.

**4.4 التطابقات**

علاقة التطابق على جبر A هي علاقة تكافؤ على | A | متوافقة مع عمليات A. نمثل هذا كـ:

```
Con : {U : Universe}(A : Algebra U S) → (O ⊔ V ⊔ U)+⋆
Con A = Σ θ ∶ Equivalence | A | _ , compatible A | θ |
```

**التطابقات الخاصة:** تطابق الصفر (علاقة الهوية) هو:

```
0ᶜ : (A : Algebra U S){fe : funext V U} → Con{U} A
0ᶜ A {fe} = IsCongruence→Con 0 (Δ A {fe})
```

**الجبور الحاصل القسمي:** بالنظر إلى الجبر A والتطابق θ، يُعرَّف الحاصل القسمي A / θ بالترميز القياسي:

```
_/_ : (A : Algebra U S) → Con{W} A → Algebra (U ⊔ W+) S
A / θ = (| A | / | θ |) ,           -- مجال الحاصل القسمي
        λ f a → ⟦ (f ˆ A)(λ i → fst ∥ a i ∥) ⟧  -- عمليات الحاصل القسمي
```

بناء الحاصل القسمي ضروري للمبرهنات الأساسية في الجبر العام، بما في ذلك مبرهنات التشاكل ومبرهنة التنوع لبيركوف.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Signature, Algebra, operation interpretation, Lift-alg, compatible, congruence, Con, quotient algebra
- **Equations:** Multiple type signatures and Agda code
- **Citations:** None direct
- **Special handling:** Agda code preserved; mathematical notation carefully translated; technical terms maintain precision

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Key Paragraph

English (original): "For a fixed signature S and universe U, we define the type of algebras in signature S (S-algebras) with domain of type U⋆ as a Sigma type consisting of a domain (the carrier) and a family of basic operations indexed by the operation symbols."

Arabic translation: "لتوقيع ثابت S وكون U، نعرّف نوع الجبور في التوقيع S (S-جبور) بمجال من النوع U⋆ كنوع سيجما يتكون من مجال (الحامل) وعائلة من العمليات الأساسية مفهرسة برموز العمليات."

Back-translation: "For a fixed signature S and universe U, we define the type of algebras in signature S (S-algebras) with domain of type U⋆ as a Sigma type consisting of a domain (the carrier) and a family of basic operations indexed by operation symbols."

**Verification:** ✓ Semantic equivalence maintained
