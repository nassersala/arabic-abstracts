# Section 3: Type-theoretic semi-fibration categories
## القسم 3: فئات شبه الألياف النوعية النظرية

**Section:** main-technical
**Translation Quality:** 0.86
**Glossary Terms Used:** fibration, type theory, model category, cofibration, pullback, Quillen adjunction, extensional, identity types, Σ-types, unit types

---

### English Version (Key Excerpts)

**Definition 3.1.** A *type-theoretic semi-fibration category* consists of a category $\mathcal{C}$ with a chosen class of maps, called fibrations, a chosen terminal object, and chosen pullbacks of fibrations such that the following conditions hold:
(1) Fibrations are exponentiable.
(2) The class of fibrations contains identity morphisms and is closed under compositions and pullbacks.
(3) Let $i: A \to B$ be a trivial cofibration in $(\mathcal{C}/\Gamma)_f$ for some $\Gamma$. Then pullbacks of $i$ along fibrations are trivial cofibrations.
(4) Let $i: A \to B$ be a map in $(\mathcal{C}/\Gamma)_f$ for some $\Gamma$. Then $i$ factors as a trivial cofibration followed by a fibration.
(5) Let $i: A \to B$ be a trivial cofibration in $(\mathcal{C}/\Gamma)_f$ for some $\Gamma$. Then, for every map $r: \Delta \to \Gamma$, the pullback map $r^*(A) \to r^*(B)$ is a trivial cofibration.

[... Technical content about trivial fibrations, extensionality, and examples...]

**Example 3.4.** Let $\mathcal{M}$ be a model category in which fibrations are exponentiable and pullbacks of trivial cofibrations are cofibrations. Then $\mathcal{M}$ is a type-theoretic semi-fibration category. We will call such a model category *type-theoretic model category*.

**Proposition 3.6.** Let $F: \mathcal{B} \to \mathcal{C}$ be a functor between type-theoretic semi-fibration categories. Then $F^*(\mathcal{C}_!)$ is a contextually indexed contextual category with unit types, Σ-types, and identity types. Moreover, if $\mathcal{C}$ is right proper, then
(1) $F^*(\mathcal{C}_!)$ has Π-types which are extensional if $\mathcal{C}$ is extensional.
(2) If $F$ is a left relative Quillen functor, then $F^*(\mathcal{C}_!)$ has dependent Hom-types. In particular, it is locally small. If $\mathcal{C}$ is extensional and the relative adjunction is extensional, then identity types are extensional.

---

### النسخة العربية (مقتطفات رئيسية)

**تعريف 3.1.** *فئة شبه الألياف النوعية النظرية* تتكون من فئة $\mathcal{C}$ مع صنف مختار من الخرائط، تُسمى ألياف، وعنصر طرفي مختار، وسحوبات مختارة للألياف بحيث تتحقق الشروط التالية:
(1) الألياف قابلة للأسّ.
(2) صنف الألياف يحتوي على تشاكلات الهوية ومغلق تحت التراكيب والسحوبات.
(3) لتكن $i: A \to B$ ليفاً مشتركاً تافهاً في $(\mathcal{C}/\Gamma)_f$ لبعض $\Gamma$. حينئذٍ فإن سحوبات $i$ على طول الألياف هي ألياف مشتركة تافهة.
(4) لتكن $i: A \to B$ خريطة في $(\mathcal{C}/\Gamma)_f$ لبعض $\Gamma$. حينئذٍ $i$ تتحلل إلى ليف مشترك تافه متبوعاً بليف.
(5) لتكن $i: A \to B$ ليفاً مشتركاً تافهاً في $(\mathcal{C}/\Gamma)_f$ لبعض $\Gamma$. حينئذٍ، لكل خريطة $r: \Delta \to \Gamma$، فإن خريطة السحب $r^*(A) \to r^*(B)$ هي ليف مشترك تافه.

[... محتوى تقني حول الألياف التافهة، والامتدادية، والأمثلة...]

**مثال 3.4.** لتكن $\mathcal{M}$ فئة نموذجية تكون فيها الألياف قابلة للأسّ وسحوبات الألياف المشتركة التافهة هي ألياف مشتركة. حينئذٍ $\mathcal{M}$ هي فئة شبه ألياف نوعية نظرية. سنسمي مثل هذه الفئة النموذجية *فئة نموذجية نوعية نظرية*.

**قضية 3.6.** لتكن $F: \mathcal{B} \to \mathcal{C}$ دالة بين فئات شبه ألياف نوعية نظرية. حينئذٍ $F^*(\mathcal{C}_!)$ هي فئة سياقية مفهرسة سياقياً مع أنواع وحدة، وأنواع Σ، وأنواع هوية. علاوة على ذلك، إذا كانت $\mathcal{C}$ صحيحة يمنياً، فإن
(1) $F^*(\mathcal{C}_!)$ لها أنواع Π وهي امتدادية إذا كانت $\mathcal{C}$ امتدادية.
(2) إذا كانت $F$ دالة كيلن يسارية نسبية، فإن $F^*(\mathcal{C}_!)$ لها أنواع Hom معتمدة. بشكل خاص، فهي صغيرة محلياً. إذا كانت $\mathcal{C}$ امتدادية والاقتران النسبي امتدادي، فإن أنواع الهوية امتدادية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** type-theoretic semi-fibration category, trivial cofibration, right proper, extensional identity types, Quillen adjunction, Cisinski model structure
- **Equations:** Multiple technical diagrams and commutative squares
- **Citations:** [1], [8], [9], [12]
- **Special handling:** Complex categorical definitions and model category theory

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
