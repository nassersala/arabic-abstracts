# Section 2: Contextually indexed contextual categories
## القسم 2: الفئات السياقية المفهرسة سياقياً

**Section:** main-technical
**Translation Quality:** 0.87
**Glossary Terms Used:** category, functor, fibration, contextual category, type theory, indexed, pullback, terminal object, local universes, Hom-types, dependent Hom-types, Π-types, change of base

---

### English Version (Key Excerpts)

**2.1. Definition.** Indexed type theories are defined in [5] as certain essentially algebraic theory. Thus, we have a notion of a model of such a theory. We will call models of indexed unary (resp., dependent) type theories *contextually indexed categories* (resp., *contextually indexed contextual categories*). We can also define them explicitly. A contextually indexed category is a contextual category $\mathcal{B}$ together with a category indexed over $\mathcal{B}$, that is a functor $\mathcal{B}^{op} \to \mathbf{Cat}$. A contextually indexed contextual category is a contextual category $\mathcal{B}$ together with a contextual category indexed over $\mathcal{B}$, that is a functor $\mathcal{B}^{op} \to \mathbf{ConCat}$.

One class of contextually indexed contextual categories was already defined in [5]. An indexed type theory can be interpreted in an appropriate homotopy type theory. This implies that there is a forgetful functor $U$ from the category of contextual categories to the category of contextually indexed contextual categories. If $M$ is a contextual category, then $U(M)$ will be called the *canonical indexing* of $M$ over itself. The underlying contextual category of $U(M)$ is indeed $M$ itself.

A contextually indexed category $\mathcal{C}: \mathcal{B}^{op} \to \mathbf{Cat}$ is *locally small* if, for every context $\Gamma$ of $\mathcal{B}$ and every pair of objects $A, B \in \mathcal{C}(\Gamma)$, there is a type $\mathrm{Hom}(A,B)$ over $\Gamma$ of maps between $A$ and $B$. To be more precise, $\mathrm{Hom}(A,B)$ is a type equipped with a bijection between the set of terms of this type and the set of maps between $A$ and $B$ stable under reindexing.

If $\mathcal{C}$ is a contextually indexed contextual category, then there is a stronger version of Hom-types which we call *dependent Hom-types*. If $B$ is an indexed type in an indexed context $\Delta$ over a base context $\Gamma$, then a dependent Hom-type $\mathrm{Hom}(\Delta.B)$ is a type over $\Gamma$ such that there is a bijection between the set of its terms and the set of terms of $B$ stable under reindexing.

[... Technical content about change of base, local universes construction, and various lemmas...]

**Lemma 2.1.** Let $F: \mathcal{B} \to \mathcal{C}$ be a functor between categories with fibrations. Suppose that, for every fibration $f: A \twoheadrightarrow B$ in $\mathcal{C}$, the pullback functor $f^*: \mathcal{C}/B \to \mathcal{C}/A$ has a right adjoint $\Pi_f: \mathcal{C}/A \to \mathcal{C}/B$. Then
(1) If $\Pi_f$ maps fibrations over $A$ to fibrations over $B$, then $F^*(\mathcal{C}_!)$ has Π-types.
(2) [Additional technical conditions for Cartesian closure...]

**Lemma 2.2.** Let $F: \mathcal{B} \to \mathcal{C}$ be a functor between categories with fibrations which has a right adjoint $G$ relative to fibrant objects of $\mathcal{B}$ which preserves fibrations. If $F^*(\mathcal{C}_!)$ has the Π-type $\Pi(\Delta.B)$ for some type $\Gamma | \Delta \vdash B$, then it has the dependent Hom-type $\mathrm{Hom}(\Delta.B)$. In particular, if it is Cartesian closed, then it is locally small.

---

### النسخة العربية (مقتطفات رئيسية)

**2.1. التعريف.** تُعرَّف نظريات الأنواع المفهرسة في [5] كنظرية جبرية أساسية معينة. وبالتالي، لدينا مفهوم نموذج لمثل هذه النظرية. سنسمي نماذج نظريات الأنواع الأحادية المفهرسة (resp.، المعتمدة) *الفئات المفهرسة سياقياً* (resp.، *الفئات السياقية المفهرسة سياقياً*). يمكننا أيضاً تعريفها بشكل صريح. الفئة المفهرسة سياقياً هي فئة سياقية $\mathcal{B}$ مع فئة مفهرسة فوق $\mathcal{B}$، أي دالة $\mathcal{B}^{op} \to \mathbf{Cat}$. الفئة السياقية المفهرسة سياقياً هي فئة سياقية $\mathcal{B}$ مع فئة سياقية مفهرسة فوق $\mathcal{B}$، أي دالة $\mathcal{B}^{op} \to \mathbf{ConCat}$.

صنف واحد من الفئات السياقية المفهرسة سياقياً تم تعريفه بالفعل في [5]. يمكن تفسير نظرية الأنواع المفهرسة في نظرية أنواع هوموتوبية مناسبة. هذا يعني أن هناك دالة نسيان $U$ من فئة الفئات السياقية إلى فئة الفئات السياقية المفهرسة سياقياً. إذا كانت $M$ فئة سياقية، فإن $U(M)$ تُسمى *الفهرسة الكانونية* لـ $M$ فوق نفسها. الفئة السياقية الأساسية لـ $U(M)$ هي بالفعل $M$ نفسها.

الفئة المفهرسة سياقياً $\mathcal{C}: \mathcal{B}^{op} \to \mathbf{Cat}$ هي *صغيرة محلياً* إذا كان، لكل سياق $\Gamma$ من $\mathcal{B}$ ولكل زوج من العناصر $A, B \in \mathcal{C}(\Gamma)$، يوجد نوع $\mathrm{Hom}(A,B)$ فوق $\Gamma$ من الخرائط بين $A$ و $B$. بشكل أكثر دقة، $\mathrm{Hom}(A,B)$ هو نوع مزود بتقابل ثنائي بين مجموعة حدود هذا النوع ومجموعة الخرائط بين $A$ و $B$ مستقر تحت إعادة الفهرسة.

إذا كانت $\mathcal{C}$ فئة سياقية مفهرسة سياقياً، فهناك نسخة أقوى من أنواع Hom نسميها *أنواع Hom المعتمدة*. إذا كان $B$ نوعاً مفهرساً في سياق مفهرس $\Delta$ فوق سياق أساسي $\Gamma$، فإن نوع Hom المعتمد $\mathrm{Hom}(\Delta.B)$ هو نوع فوق $\Gamma$ بحيث يوجد تقابل ثنائي بين مجموعة حدوده ومجموعة حدود $B$ مستقر تحت إعادة الفهرسة.

[... محتوى تقني حول تغيير القاعدة، بناء الأكوان المحلية، ومختلف اللمات...]

**لمة 2.1.** لتكن $F: \mathcal{B} \to \mathcal{C}$ دالة بين فئات مع ألياف. افترض أنه لكل ليف $f: A \twoheadrightarrow B$ في $\mathcal{C}$، فإن دالة السحب $f^*: \mathcal{C}/B \to \mathcal{C}/A$ لها مُرافق أيمن $\Pi_f: \mathcal{C}/A \to \mathcal{C}/B$. حينئذٍ
(1) إذا كانت $\Pi_f$ تُرسل الألياف فوق $A$ إلى ألياف فوق $B$، فإن $F^*(\mathcal{C}_!)$ لها أنواع Π.
(2) [شروط تقنية إضافية للإغلاق الديكارتي...]

**لمة 2.2.** لتكن $F: \mathcal{B} \to \mathcal{C}$ دالة بين فئات مع ألياف لها مُرافق أيمن $G$ نسبي للعناصر الليفية من $\mathcal{B}$ والذي يحفظ الألياف. إذا كان لـ $F^*(\mathcal{C}_!)$ نوع Π وهو $\Pi(\Delta.B)$ لنوع ما $\Gamma | \Delta \vdash B$، فإن لها نوع Hom المعتمد $\mathrm{Hom}(\Delta.B)$. بشكل خاص، إذا كانت ديكارتية مغلقة، فهي صغيرة محلياً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** locally small, dependent Hom-types, change of base, local universes, Cartesian closed, relative right adjoint
- **Equations:** Multiple mathematical formulas and diagrams
- **Citations:** [5], [8], [13], [14]
- **Special handling:** Heavy use of category theory notation, commutative diagrams, and type theory rules

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
