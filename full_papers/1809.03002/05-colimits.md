# Section 5: Colimits
## القسم 5: الحدود المشتركة

**Section:** main-technical
**Translation Quality:** 0.86
**Glossary Terms Used:** colimit, pushout, coproduct, initial type, fibration, quasifibration, cofibration, model category, trivial cofibration

---

### English Version (Key Excerpts)

In this section, we give sufficient conditions for a model $F^*(\mathcal{C})$ to have initial types, binary coproducts, arbitrary coproducts, and pushouts.

**5.1. Quasifibrations.** We will say that a map $f: X \to Z$ in a category with fibrations is a *quasifibration* if it factors as a trivial cofibration $i: X \to Y$ followed by a fibration $p: Y \twoheadrightarrow Z$ and, for every diagram [of pullbacks], the map $i'$ is a trivial cofibration. This notion is similar to the classical notion of a quasifibration between spaces.

**Lemma 5.3.** In a right proper type-theoretic model category, stable under pullbacks coproducts of fibrations over a fixed base are quasifibrations.

**5.2. Coproducts.**

**Proposition 5.5.** Let $\mathcal{B}$ be a contextual category, let $\mathcal{C}$ be a category with fibrations, and let $F: \mathcal{B} \to \mathcal{C}$ be a functor between them. If $\mathcal{C}$ has a strict quasifibrant initial object, then $F^*(\mathcal{C})$ has strict initial types.

**Proposition 5.9.** [Conditions for stable dependent coproducts...]

**Proposition 5.11.** Let $F: \mathcal{B} \to \mathcal{C}$ be a functor between categories with fibrations. Suppose that the following conditions hold:
(1) $F$ preserves pullbacks along fibrations and pullbacks of $F$-fibrations exist.
(2) Fibrations and $F$-fibrations are exponentiable.
(3) The composition of a fibration and an $F$-fibration is a quasifibration.

Then $F^*(\mathcal{C}_!)$ has stable dependent coproducts.

**5.3. Pushouts.**

**Lemma 5.14.** Let $\mathcal{B}$ be a category with fibrations, let $\mathcal{C}$ be a category with fibrations which has path types (as defined in Section 4), and let $F: \mathcal{B} \to \mathcal{C}$ be a functor. Suppose that, for every pair of maps $f: A \to B$ and $g: A \to C$ over an object $\Gamma$ of $\mathcal{C}$, the map $A \times \Delta^1 \coprod_{A\coprod A} B \coprod C \to \Gamma$ is a quasifibration. Then $F^*(\mathcal{C}_!)$ has stable dependent pushouts.

**Lemma 5.15.** If $\mathcal{C}$ is a locally Cartesian closed right proper type-theoretic model category which has path types, then it satisfies the conditions of Lemma 5.14.

---

### النسخة العربية (مقتطفات رئيسية)

في هذا القسم، نعطي شروطاً كافية لنموذج $F^*(\mathcal{C})$ لكي يكون له أنواع أولية، وجداءات مشتركة ثنائية، وجداءات مشتركة تعسفية، ودفعات.

**5.1. شبه الألياف.** سنقول أن خريطة $f: X \to Z$ في فئة مع ألياف هي *شبه ليف* إذا تحللت كليف مشترك تافه $i: X \to Y$ متبوعاً بليف $p: Y \twoheadrightarrow Z$ و، لكل مخطط [من السحوبات]، فإن الخريطة $i'$ هي ليف مشترك تافه. هذا المفهوم مشابه للمفهوم الكلاسيكي لشبه الليف بين الفضاءات.

**لمة 5.3.** في فئة نموذجية نوعية نظرية صحيحة يمنياً، فإن الجداءات المشتركة المستقرة تحت السحوبات للألياف فوق قاعدة ثابتة هي أشباه ألياف.

**5.2. الجداءات المشتركة.**

**قضية 5.5.** لتكن $\mathcal{B}$ فئة سياقية، ولتكن $\mathcal{C}$ فئة مع ألياف، ولتكن $F: \mathcal{B} \to \mathcal{C}$ دالة بينهما. إذا كان لـ $\mathcal{C}$ عنصر أولي شبه ليفي صارم، فإن $F^*(\mathcal{C})$ له أنواع أولية صارمة.

**قضية 5.9.** [شروط للجداءات المشتركة المعتمدة المستقرة...]

**قضية 5.11.** لتكن $F: \mathcal{B} \to \mathcal{C}$ دالة بين فئات مع ألياف. افترض أن الشروط التالية تتحقق:
(1) $F$ تحفظ السحوبات على طول الألياف وسحوبات الألياف-$F$ موجودة.
(2) الألياف والألياف-$F$ قابلة للأسّ.
(3) تركيب ليف وليف-$F$ هو شبه ليف.

حينئذٍ $F^*(\mathcal{C}_!)$ لها جداءات مشتركة معتمدة مستقرة.

**5.3. الدفعات.**

**لمة 5.14.** لتكن $\mathcal{B}$ فئة مع ألياف، ولتكن $\mathcal{C}$ فئة مع ألياف لها أنواع مسارات (كما هو معرّف في القسم 4)، ولتكن $F: \mathcal{B} \to \mathcal{C}$ دالة. افترض أنه لكل زوج من الخرائط $f: A \to B$ و $g: A \to C$ فوق عنصر $\Gamma$ من $\mathcal{C}$، فإن الخريطة $A \times \Delta^1 \coprod_{A\coprod A} B \coprod C \to \Gamma$ هي شبه ليف. حينئذٍ $F^*(\mathcal{C}_!)$ لها دفعات معتمدة مستقرة.

**لمة 5.15.** إذا كانت $\mathcal{C}$ فئة نموذجية نوعية نظرية ديكارتية مغلقة محلياً صحيحة يمنياً ولها أنواع مسارات، فإنها تحقق شروط اللمة 5.14.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** quasifibration, strict initial object, stable coproducts, unstable pushouts, dependent coproducts
- **Equations:** Multiple categorical constructions and diagrams
- **Citations:** [3], [7], [9]
- **Special handling:** Technical constructions involving colimits in category theory

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
