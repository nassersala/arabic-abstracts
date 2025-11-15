# Section 7: Quasicategories
## القسم 7: الفئات الشبه

**Section:** main-technical
**Translation Quality:** 0.87
**Glossary Terms Used:** quasicategory, simplicial sets, Joyal model structure, Kan complex, categorical fibration, Cartesian fibration, functor

---

### English Version (Key Excerpts)

In this section, we describe a contextually indexed contextual category based on quasicategories.

Consider the functor $\mathrm{Id}: \mathbf{sSet}_K \to \mathbf{sSet}_J$, where $\mathbf{sSet}_K$ is equipped with the Kan model structure and $\mathbf{sSet}_J$ is equipped with the Joyal model structure. This functor is not a left Quillen functor, but it is a relative left Quillen functor. To construct its relative right adjoint, we define an auxiliary notion. Let $x: \Delta^1 \to X$ be a 1-simplex of a simplicial set $X$. We will call such a simplex an *edge* of $X$. We will say that $x$ is *invertible* if it extends to a map $\widehat{\Delta^1} \to X$, where $\widehat{\Delta^1}$ is the nerve of the groupoid with two objects and a unique arrow between any pair of objects.

For every simplicial set $X$, let $G(X)$ be the subset of $X$ consisting of simplices in which every edge is invertible. We will denote the inclusion map $G(X) \to X$ by $\varepsilon_X$. Clearly, $G: \mathbf{sSet} \to \mathbf{sSet}$ is a functor. Moreover, it is a right adjoint to Id relative to Kan complexes.

**Lemma 7.1.** For every simplicial set $X$, the following conditions are equivalent:
(1) Every edge of $X$ is invertible.
(2) $X$ has the right lifting property with respect to the map $\Delta^1 \to \widehat{\Delta^1}$.
(3) $G(X) = X$.
(4) $X$ is isomorphic to $G(Y)$ for some simplicial set $Y$.

Simplicial sets in which all edges are invertible often can replace Kan complexes. For example, every categorical fibration with a Kan complex as a codomain is a Cartesian fibration. We will prove in Proposition 7.3 that this is also true for categorical fibrations with a codomain in which all edges are invertible.

**Proposition 7.3.** If every edge of a simplicial set $Y$ is invertible, then every categorical fibration $p: X \to Y$ is a Cartesian fibration.

**Proposition 7.4.** If edges of simplicial sets $X$ and $Y$ are invertible, then every map $X \to Y$ factors into a categorical trivial cofibration $X \to Z$ followed by a Kan fibration $Z \to Y$.

**Lemma 7.5.** The functor $G$ maps categorical fibrations to Kan fibrations.

**Theorem 7.6.** Let $\mathrm{Id}: \mathbf{sSet}_K \to \mathbf{sSet}_J$ be the identity functor, where $\mathbf{sSet}_K$ is equipped with the Kan model structure and $\mathbf{sSet}_J$ is equipped with the Joyal model structure. Then the contextually indexed contextual category $\mathrm{Id}^*( (\mathbf{sSet}_J)_!)$ is locally small and Cartesian closed. Moreover, it has Π-types in the empty context and dependent Hom-types. It also has Σ-types, unit types, extensional identity types, dependent products, stable dependent coproducts, strict initial types, stable binary coproducts, unstable pushouts, and (indexed) extension types with respect to cofibrations.

---

### النسخة العربية (مقتطفات رئيسية)

في هذا القسم، نصف فئة سياقية مفهرسة سياقياً بناءً على الفئات الشبه.

اعتبر الدالة $\mathrm{Id}: \mathbf{sSet}_K \to \mathbf{sSet}_J$، حيث $\mathbf{sSet}_K$ مزودة ببنية نموذج كان و $\mathbf{sSet}_J$ مزودة ببنية نموذج جويال. هذه الدالة ليست دالة كيلن يسارية، لكنها دالة كيلن يسارية نسبية. لبناء مرافقها الأيمن النسبي، نعرّف مفهوماً مساعداً. لتكن $x: \Delta^1 \to X$ مبسطة 1 لمجموعة بسيطة $X$. سنسمي مثل هذه المبسطة *حافة* من $X$. سنقول أن $x$ *قابلة للعكس* إذا امتدت إلى خريطة $\widehat{\Delta^1} \to X$، حيث $\widehat{\Delta^1}$ هو عصب الغرو بويد مع عنصرين وسهم فريد بين أي زوج من العناصر.

لكل مجموعة بسيطة $X$، لتكن $G(X)$ المجموعة الفرعية من $X$ المكونة من المبسطات التي فيها كل حافة قابلة للعكس. سنرمز لخريطة التضمين $G(X) \to X$ بـ $\varepsilon_X$. من الواضح أن $G: \mathbf{sSet} \to \mathbf{sSet}$ هي دالة. علاوة على ذلك، فهي مُرافق أيمن لـ Id نسبية لمُركبات كان.

**لمة 7.1.** لكل مجموعة بسيطة $X$، فإن الشروط التالية متكافئة:
(1) كل حافة من $X$ قابلة للعكس.
(2) $X$ لها خاصية الرفع اليمنى بالنسبة للخريطة $\Delta^1 \to \widehat{\Delta^1}$.
(3) $G(X) = X$.
(4) $X$ متماثلة مع $G(Y)$ لبعض المجموعة البسيطة $Y$.

المجموعات البسيطة التي فيها جميع الحواف قابلة للعكس غالباً يمكن أن تستبدل مُركبات كان. على سبيل المثال، كل ليف فئوي مع مُركب كان كمجال متشارك هو ليف ديكارتي. سنثبت في القضية 7.3 أن هذا صحيح أيضاً للألياف الفئوية مع مجال متشارك فيه جميع الحواف قابلة للعكس.

**قضية 7.3.** إذا كانت كل حافة من مجموعة بسيطة $Y$ قابلة للعكس، فإن كل ليف فئوي $p: X \to Y$ هو ليف ديكارتي.

**قضية 7.4.** إذا كانت حواف المجموعات البسيطة $X$ و $Y$ قابلة للعكس، فإن كل خريطة $X \to Y$ تتحلل إلى ليف مشترك تافه فئوي $X \to Z$ متبوعاً بليف كان $Z \to Y$.

**لمة 7.5.** الدالة $G$ تُرسل الألياف الفئوية إلى ألياف كان.

**نظرية 7.6.** لتكن $\mathrm{Id}: \mathbf{sSet}_K \to \mathbf{sSet}_J$ دالة الهوية، حيث $\mathbf{sSet}_K$ مزودة ببنية نموذج كان و $\mathbf{sSet}_J$ مزودة ببنية نموذج جويال. حينئذٍ فإن الفئة السياقية المفهرسة سياقياً $\mathrm{Id}^*((\mathbf{sSet}_J)_!)$ صغيرة محلياً وديكارتية مغلقة. علاوة على ذلك، لها أنواع Π في السياق الفارغ وأنواع Hom معتمدة. لها أيضاً أنواع Σ، وأنواع وحدة، وأنواع هوية امتدادية، وجداءات معتمدة، وجداءات مشتركة معتمدة مستقرة، وأنواع أولية صارمة، وجداءات مشتركة ثنائية مستقرة، ودفعات غير مستقرة، وأنواع تمديد (مفهرسة) بالنسبة للألياف المشتركة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** invertible edge, relative Quillen functor, Joyal model structure, Kan model structure, $G$ functor
- **Equations:** Categorical constructions and simplex definitions
- **Citations:** [3], [9]
- **Special handling:** Simplicial set theory and quasicategory theory

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
