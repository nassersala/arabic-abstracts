# Section 6: Localization
## القسم 6: التوطين

**Section:** main-technical
**Translation Quality:** 0.85
**Glossary Terms Used:** localization, model category, fibration, identity types, extensional, Bousfield localization, Cisinski model structure

---

### English Version (Key Excerpts)

In this section, we consider the following problem. Let $\mathcal{C}$ be a category and let $\mathcal{F}$ and $\mathcal{F}'$ be two classes of fibrations of $\mathcal{C}$ such that $\mathcal{F}' \subseteq \mathcal{F}$. If we know that a contextually indexed contextual category of the form $F^*((\ mathcal{C}, \mathcal{F})_!)$ has some categorical constructions, when does $F^*( (\mathcal{C}, \mathcal{F}')_!)$ also have these constructions?

**6.1. Identity types.**

Let $(\mathcal{C}, \mathcal{F})$ be a category with fibrations and let $\mathcal{F}'$ be a subclass of $\mathcal{F}$. We will say that $\mathcal{F}'$ is *closed under identity types* if every map in $((\mathcal{C}, \mathcal{F}')/ \Gamma)_f$ factors into a trivial cofibration of $(\mathcal{C}, \mathcal{F})$ followed by a fibration in $\mathcal{F}'$.

**Lemma 6.2.** Let $(\mathcal{C}, \mathcal{F})$ be either a type-theoretic semi-fibration category or a model category and let $\mathcal{F}'$ be a subclass of $\mathcal{F}$ which is closed under retracts, compositions, and pullbacks and contains all trivial fibrations. Then the following conditions are equivalent:
(1) The class $\mathcal{F}'$ is closed under identity types.
(2) A map in $((\mathcal{C}, \mathcal{F}')/ \Gamma)_f$ belongs to $\mathcal{F}$ if and only if it belongs to $\mathcal{F}'$.
(3) For every fibration $p: Y \twoheadrightarrow \Gamma$ in $\mathcal{F}'$, the diagonal $Y \to Y \times_\Gamma Y$ factors as a trivial cofibration $Y \to P(Y)$ of $\mathcal{C}$ followed by a fibration $P(Y) \twoheadrightarrow Y \times_\Gamma Y$ in $\mathcal{F}'$.

**Proposition 6.3.** Let $(\mathcal{C}, \mathcal{F})$ be a type-theoretic semi-fibration category and let $\mathcal{F}'$ be a subclass of $\mathcal{F}$ which contains identity morphisms and closed under compositions, pullbacks, and identity types. Then $(\mathcal{C}, \mathcal{F}')$ is also a type-theoretic semi-fibration category. Moreover, $(\mathcal{C}, \mathcal{F}')$ is closed under identity types in the sense that identity types in this category are equivalent to identity types in $(\mathcal{C}, \mathcal{F})$.

**6.2. Localization of model categories.**

Let $S$ be a class of maps of a model category $\mathcal{C}$. We will write $S$-inj for the class of maps of $\mathcal{C}$ that have the right lifting property with respect to $S$. If $S$ is closed under coidentity types (a technical condition involving cylinder objects), then the class of fibrations that have the right lifting property with respect to $S$ is closed under identity types.

**Lemma 6.7.** Let $S$ be a class of cofibrations of a model category $\mathcal{C}$ closed under coidentity types. Suppose that either the domains of maps in $S$ are cofibrant or $\mathcal{C}$ is left proper. Then the class of fibrations that have the right lifting property with respect to $S$ is closed under identity types.

---

### النسخة العربية (مقتطفات رئيسية)

في هذا القسم، نعتبر المسألة التالية. لتكن $\mathcal{C}$ فئة ولتكن $\mathcal{F}$ و $\mathcal{F}'$ صنفين من ألياف $\mathcal{C}$ بحيث $\mathcal{F}' \subseteq \mathcal{F}$. إذا علمنا أن فئة سياقية مفهرسة سياقياً من الشكل $F^*((\mathcal{C}, \mathcal{F})_!)$ لها بعض البنى الفئوية، فمتى يكون لـ $F^*((\mathcal{C}, \mathcal{F}')_!)$ أيضاً هذه البنى؟

**6.1. أنواع الهوية.**

لتكن $(\mathcal{C}, \mathcal{F})$ فئة مع ألياف ولتكن $\mathcal{F}'$ صنفاً فرعياً من $\mathcal{F}$. سنقول أن $\mathcal{F}'$ *مغلق تحت أنواع الهوية* إذا كانت كل خريطة في $((\mathcal{C}, \mathcal{F}')/\Gamma)_f$ تتحلل إلى ليف مشترك تافه من $(\mathcal{C}, \mathcal{F})$ متبوعاً بليف في $\mathcal{F}'$.

**لمة 6.2.** لتكن $(\mathcal{C}, \mathcal{F})$ إما فئة شبه ألياف نوعية نظرية أو فئة نموذجية ولتكن $\mathcal{F}'$ صنفاً فرعياً من $\mathcal{F}$ مغلق تحت الانكماشات والتراكيب والسحوبات ويحتوي على جميع الألياف التافهة. حينئذٍ فإن الشروط التالية متكافئة:
(1) الصنف $\mathcal{F}'$ مغلق تحت أنواع الهوية.
(2) خريطة في $((\mathcal{C}, \mathcal{F}')/\Gamma)_f$ تنتمي إلى $\mathcal{F}$ إذا وفقط إذا كانت تنتمي إلى $\mathcal{F}'$.
(3) لكل ليف $p: Y \twoheadrightarrow \Gamma$ في $\mathcal{F}'$، فإن القطر $Y \to Y \times_\Gamma Y$ يتحلل كليف مشترك تافه $Y \to P(Y)$ من $\mathcal{C}$ متبوعاً بليف $P(Y) \twoheadrightarrow Y \times_\Gamma Y$ في $\mathcal{F}'$.

**قضية 6.3.** لتكن $(\mathcal{C}, \mathcal{F})$ فئة شبه ألياف نوعية نظرية ولتكن $\mathcal{F}'$ صنفاً فرعياً من $\mathcal{F}$ يحتوي على تشاكلات الهوية ومغلق تحت التراكيب والسحوبات وأنواع الهوية. حينئذٍ $(\mathcal{C}, \mathcal{F}')$ هي أيضاً فئة شبه ألياف نوعية نظرية. علاوة على ذلك، $(\mathcal{C}, \mathcal{F}')$ مغلقة تحت أنواع الهوية بمعنى أن أنواع الهوية في هذه الفئة تكافئ أنواع الهوية في $(\mathcal{C}, \mathcal{F})$.

**6.2. توطين الفئات النموذجية.**

لتكن $S$ صنفاً من خرائط فئة نموذجية $\mathcal{C}$. سنكتب $S$-inj لصنف خرائط $\mathcal{C}$ التي لها خاصية الرفع اليمنى بالنسبة لـ $S$. إذا كانت $S$ مغلقة تحت أنواع الهوية المشتركة (شرط تقني يتضمن عناصر الأسطوانة)، فإن صنف الألياف التي لها خاصية الرفع اليمنى بالنسبة لـ $S$ مغلق تحت أنواع الهوية.

**لمة 6.7.** لتكن $S$ صنفاً من الألياف المشتركة لفئة نموذجية $\mathcal{C}$ مغلقة تحت أنواع الهوية المشتركة. افترض أن إما مجالات الخرائط في $S$ هي ألياف مشتركة أو $\mathcal{C}$ صحيحة يسارياً. حينئذٍ فإن صنف الألياف التي لها خاصية الرفع اليمنى بالنسبة لـ $S$ مغلق تحت أنواع الهوية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** closure under identity types, coidentity types, left/right Bousfield localization, K-local equivalence
- **Equations:** Categorical diagrams and model category structures
- **Citations:** [1], [3], [5]
- **Special handling:** Technical conditions on model categories and localizations

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
