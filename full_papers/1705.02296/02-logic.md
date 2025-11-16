# Section 2: The Logic
## القسم 2: المنطق

**Section:** methodology (logic framework)
**Translation Quality:** 0.86
**Glossary Terms Used:** first-order logic (منطق من الدرجة الأولى), axiom (بديهية), term (حد), formula (صيغة), function symbol (رمز دالة), variable (متغير), computational model (نموذج حسابي), Turing machine (آلة تورينج), polynomial time (زمن متعدد الحدود)

---

### English Version (Summary)

**Section II: THE LOGIC**

Our goal is to formally study the protocols in the computational model. In order to do this we follow the directions described in [4]: we specify in a first-order logic what the attacker cannot do, which yields a set of axioms A. We also compute from the protocol and the security property a formula ¬ψ expressing that there is an attack on the protocol. We know that if A∪{¬ψ} is unsatisfiable, then the protocol is secure in any model of A. If, in addition, every axiom is computationally sound, then the protocol is computationally secure.

In this section we recall the first-order (indistinguishability) logic and provide a set of axioms A, some of which are valid in any computational model while others require some security assumptions on the cryptographic primitives.

**A. Syntax of the logic**

Terms are built on a set of function symbols F, a set of function symbols G (used to represent the attacker's computations), a set of names N and a set of variables X.

In the examples that are considered in this paper, F contains at least the following function symbols:
H, ⊕, ⟨_,_⟩, EQ(_; _), if _ then _ else _, true, false, π₁, π₂, 0

Each variable and term has a sort, which is either bool, short, or message. The typing rules ensure proper usage:
- Pairing: ⟨_,_⟩ : message × message → message
- Booleans: true, false : → bool
- Projections: π₁, π₂ : message → message
- Equality: EQ(_; _) : message × message → bool
- Names have type short
- XOR: ⊕ : short × short → short (restricted to fixed length)
- Hash function: H : message × short → short (keyed hash)
- Conditional: if _ then _ else _ (polymorphic types)

**Formulas:** Atomic formulas represent the indistinguishability of two experiments:
u₁, ..., uₙ ∼ v₁, ..., vₙ

where uᵢ and vᵢ have the same sort for every i. Formulas are obtained by combining atomic formulas with Boolean connectives ∧, →, ∨, ¬ and quantifiers.

**B. Semantics of the logic**

We rely on classical first-order interpretations with the generic axioms in Figure 1 (provided in the paper), which are computationally valid.

One particular class of interpretations are the computational semantics:
- The domain is the set of deterministic polynomial time Turing machines with input tape and two random tapes (ρ₁ for honest random values, ρ₂ for attacker random values)
- Names are interpreted as machines extracting words from ρ₁
- Function symbols in F are interpreted as deterministic polynomial time Turing machines
- Function symbols in G represent attacker computations (using ρ₂ but not ρ₁)
- The predicate ∼ is interpreted as computational indistinguishability ≈

**C. Computationally valid axioms**

Proposition 1: The axioms displayed in Figure 1 are computationally valid.

These include:
- Reflexivity, symmetry, transitivity of ∼
- Congruence rules
- Structural rules for conditionals and XOR
- Independence axiom (Indep): If n does not occur in x, y, ~u, ~v then ~u ∼ ~v ⇒ ~u, x ⊕ n ∼ ~v, y ⊕ n
- Fresh nonce axiom
- Various other structural properties

**D. Assumptions on primitives**

Implementation assumptions (identities that must be satisfied):
- π₁(⟨x, y⟩) = x and π₂(⟨x, y⟩) = y

**Collision Resistance (CR) axiom:**
If the only occurrences of k in t, t', ~u are as a second argument of H:
~u, if EQ(t;t') then false else EQ(H(t, k); H(t', k)) ∼ ~u, false

Proposition 2: The CR axiom is sound in any computational model where H is collision resistant under hidden-key attacks.

**Pseudo-Random Function (PRF) axiom schema:**
~u, if c then 0 else H(t, k) ∼ ~u, if c then 0 else n (PRFₙ)

where:
- The occurrences of H (and k) in ~u, t are H(t₁, k), ..., H(tₙ, k)
- n is a fresh name
- c ≡ ⋁ⁿᵢ₌₁ EQ(tᵢ; t)

Proposition 3: For any n, (PRFₙ) is computationally sound if H(·, k) is a PRF family.

---

### النسخة العربية (ملخص)

**القسم II: المنطق**

هدفنا هو دراسة البروتوكولات رسمياً في النموذج الحسابي. للقيام بذلك، نتبع التوجيهات الموصوفة في [4]: نحدد في منطق من الدرجة الأولى ما لا يمكن للمهاجم فعله، مما ينتج عنه مجموعة من البديهيات A. نحسب أيضاً من البروتوكول وخاصية الأمان صيغة ψ¬ تعبر عن وجود هجوم على البروتوكول. نعلم أنه إذا كانت {ψ¬} ∪ A غير قابلة للإرضاء، فإن البروتوكول آمن في أي نموذج لـ A. إذا كانت، بالإضافة إلى ذلك، كل بديهية صحيحة حسابياً، فإن البروتوكول آمن حسابياً.

في هذا القسم نذكر منطق (عدم القابلية للتمييز) من الدرجة الأولى ونقدم مجموعة من البديهيات A، بعضها صالح في أي نموذج حسابي بينما يتطلب البعض الآخر افتراضات أمان على البدائل التشفيرية.

**أ. بناء جملة المنطق**

تُبنى الحدود على مجموعة من رموز الدوال F، ومجموعة من رموز الدوال G (تُستخدم لتمثيل حسابات المهاجم)، ومجموعة من الأسماء N ومجموعة من المتغيرات X.

في الأمثلة المُنظر فيها في هذه الورقة، تحتوي F على الأقل على رموز الدوال التالية:
H, ⊕, ⟨_,_⟩, EQ(_; _), if _ then _ else _, true, false, π₁, π₂, 0

كل متغير وحد له نوع (sort)، وهو إما bool أو short أو message. تضمن قواعد الكتابة الاستخدام الصحيح:
- الإقران: ⟨_,_⟩ : message × message → message
- القيم المنطقية: true, false : → bool
- الإسقاطات: π₁, π₂ : message → message
- المساواة: EQ(_; _) : message × message → bool
- الأسماء من نوع short
- XOR: ⊕ : short × short → short (مقيد بطول ثابت)
- دالة التجزئة: H : message × short → short (تجزئة بمفتاح)
- الشرطي: if _ then _ else _ (أنواع متعددة الأشكال)

**الصيغ:** الصيغ الذرية تمثل عدم القابلية للتمييز بين تجربتين:
u₁, ..., uₙ ∼ v₁, ..., vₙ

حيث uᵢ و vᵢ لهما نفس النوع لكل i. يتم الحصول على الصيغ من خلال الجمع بين الصيغ الذرية بروابط منطقية ∧، →، ∨، ¬ ومُحددات كمية.

**ب. دلالات المنطق**

نعتمد على التفسيرات الكلاسيكية من الدرجة الأولى مع البديهيات العامة في الشكل 1 (المقدمة في الورقة)، والتي تكون صحيحة حسابياً.

فئة معينة من التفسيرات هي الدلالات الحسابية:
- المجال هو مجموعة آلات تورينج الحتمية متعددة الحدود في الزمن مع شريط إدخال وشريطين عشوائيين (ρ₁ للقيم العشوائية الصادقة، ρ₂ للقيم العشوائية للمهاجم)
- الأسماء تُفسر كآلات تستخرج كلمات من ρ₁
- رموز الدوال في F تُفسر كآلات تورينج حتمية متعددة الحدود في الزمن
- رموز الدوال في G تمثل حسابات المهاجم (باستخدام ρ₂ وليس ρ₁)
- المحمول ∼ يُفسر كعدم قابلية للتمييز حسابي ≈

**ج. البديهيات الصحيحة حسابياً**

القضية 1: البديهيات المعروضة في الشكل 1 صحيحة حسابياً.

تشمل هذه:
- الانعكاسية، التماثل، التعدية لـ ∼
- قواعد التطابق
- القواعد الهيكلية للشرطيات و XOR
- بديهية الاستقلالية (Indep): إذا لم يظهر n في x, y, ~u, ~v فإن ~u ∼ ~v ⇒ ~u, x ⊕ n ∼ ~v, y ⊕ n
- بديهية الأرقام العشوائية الجديدة
- خصائص هيكلية أخرى متنوعة

**د. افتراضات على البدائل**

افتراضات التنفيذ (هويات يجب أن تُلبى):
- π₁(⟨x, y⟩) = x و π₂(⟨x, y⟩) = y

**بديهية مقاومة التصادم (CR):**
إذا كانت التواجدات الوحيدة لـ k في t, t', ~u هي كوسيط ثانٍ لـ H:
~u, if EQ(t;t') then false else EQ(H(t, k); H(t', k)) ∼ ~u, false

القضية 2: بديهية CR صحيحة في أي نموذج حسابي حيث H مقاومة للتصادم تحت هجمات المفتاح المخفي.

**مخطط بديهية الدالة شبه العشوائية (PRF):**
~u, if c then 0 else H(t, k) ∼ ~u, if c then 0 else n (PRFₙ)

حيث:
- تواجدات H (و k) في ~u, t هي H(t₁, k), ..., H(tₙ, k)
- n اسم جديد
- c ≡ ⋁ⁿᵢ₌₁ EQ(tᵢ; t)

القضية 3: لأي n، (PRFₙ) صحيحة حسابياً إذا كانت H(·, k) عائلة PRF.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Generic axioms)
- **Key terms introduced:**
  - Sort (نوع)
  - Indistinguishability (عدم القابلية للتمييز)
  - Computational semantics (دلالات حسابية)
  - Random tape (شريط عشوائي)
  - Collision resistance (مقاومة التصادم)
  - Hidden-key attack (هجوم المفتاح المخفي)
  - PRF family (عائلة PRF)
- **Equations:** Multiple formal logic expressions preserved in original notation
- **Citations:** [4]
- **Special handling:**
  - Mathematical symbols preserved (∼, ⊕, ⟨⟩, π, ∧, ∨, ¬, ⇒, ≡, ⋁)
  - Type signatures maintained
  - Logical notation kept in original form

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
