# Section 4: Extension types
## القسم 4: أنواع التمديد

**Section:** main-technical
**Translation Quality:** 0.85
**Glossary Terms Used:** type theory, extension types, Π-types, identity types, fibration, pushout, path types, higher inductive types, pushout-product axiom

---

### English Version (Key Excerpts)

Extension types were defined in [11]. In this section, we describe an analogous construction in ordinary homotopy type theory and in indexed type theory.

Extension types generalize Π-types (and products in the indexed case). Semantically, if $j: U \to V$ is a map, $p: A \twoheadrightarrow V$ is a fibration, and $a: U \to A$ is a section of $p$ over $j$, then the extension object $\langle \Pi_V(p)|_j^a \rangle$ is the object of sections of $p$ which restrict to $a$.

The syntax in ordinary type theory:
$$\frac{\Gamma, y: V \vdash A \quad \Gamma, x: U \vdash a: A[jx/y]}{\Gamma \vdash \langle \Pi_{y:V} A |_{x.a}\rangle}$$

One example of an extension type is the type of extensions along a map of the form $1 \coprod 1 \to \Delta^1$, where $1$ is the terminal object and $\Delta^1$ is some object. The type of extensions in $A$ along such a map is the type of morphisms in the simplicial space (or $\infty$-category) $A$ in a version of the type theory described in [11] if $\Delta^1$ is interpreted appropriately. We can interpret $\Delta^1$ as a contractible type and add a rule to the syntax which implies that it is contractible. Then extension types along $1 \coprod 1 \to \Delta^1$ are equivalent to (heterogeneous) identity types. Such extension types were defined and studied in [4, Subsection 3.2]. We will call them *path types* since they are literally types of paths (that is, maps from the interval) between two specified points.

Path types can be used to give a convenient description of higher inductive types. For example, let $f: A \to B$ and $g: A \to C$ be a pair of maps. Then their pushout $B \coprod_A C$ has three constructors: $\mathrm{inl}: B \to B \coprod_A C$, $\mathrm{inr}: C \to B \coprod_A C$, and $\mathrm{glue}: A \to \Delta^1 \to B \coprod_A C$. The last constructor satisfies equations $\mathrm{glue}\, a\, j_0 = f\, a$ and $\mathrm{glue}\, a\, j_1 = g\, a$, where $[j_0, j_1] = j: 1 \coprod 1 \to \Delta^1$.

We will say that a category with fibrations satisfies the *pushout-product axiom* with respect to a map $j: U \to V$ if $U$ and $V$ are exponentiable and, for every fibration $X \twoheadrightarrow Y$, the map $X^V \to Y^V \times_{Y^U} X^U$ is a fibration.

**Proposition 4.2.** If a category with fibrations $\mathcal{C}$ satisfies the pushout-product axiom with respect to a map $j: U \to V$, then it has extension types along $j$.

---

### النسخة العربية (مقتطفات رئيسية)

تم تعريف أنواع التمديد في [11]. في هذا القسم، نصف بناءً مماثلاً في نظرية أنواع الهوموتوبي العادية وفي نظرية الأنواع المفهرسة.

أنواع التمديد تُعمم أنواع Π (والجداءات في الحالة المفهرسة). دلالياً، إذا كانت $j: U \to V$ خريطة، و $p: A \twoheadrightarrow V$ ليفاً، و $a: U \to A$ مقطعاً من $p$ فوق $j$، فإن عنصر التمديد $\langle \Pi_V(p)|_j^a \rangle$ هو عنصر المقاطع من $p$ التي تقتصر على $a$.

التركيب في نظرية الأنواع العادية:
$$\frac{\Gamma, y: V \vdash A \quad \Gamma, x: U \vdash a: A[jx/y]}{\Gamma \vdash \langle \Pi_{y:V} A |_{x.a}\rangle}$$

أحد أمثلة نوع التمديد هو نوع التمديدات على طول خريطة من الشكل $1 \coprod 1 \to \Delta^1$، حيث $1$ هو العنصر الطرفي و $\Delta^1$ هو عنصر ما. نوع التمديدات في $A$ على طول مثل هذه الخريطة هو نوع التشاكلات في الفضاء البسيط (أو $\infty$-فئة) $A$ في نسخة من نظرية الأنواع الموصوفة في [11] إذا تم تفسير $\Delta^1$ بشكل مناسب. يمكننا تفسير $\Delta^1$ كنوع قابل للانقباض وإضافة قاعدة للتركيب تعني أنه قابل للانقباض. حينئذٍ فإن أنواع التمديد على طول $1 \coprod 1 \to \Delta^1$ تكافئ أنواع الهوية (غير المتجانسة). تم تعريف ودراسة مثل هذه الأنواع من التمديد في [4، القسم الفرعي 3.2]. سنسميها *أنواع المسارات* لأنها حرفياً أنواع المسارات (أي، الخرائط من الفترة) بين نقطتين محددتين.

يمكن استخدام أنواع المسارات لإعطاء وصف ملائم للأنواع الحثية العليا. على سبيل المثال، لتكن $f: A \to B$ و $g: A \to C$ زوجاً من الخرائط. حينئذٍ فإن دفعتهما $B \coprod_A C$ لها ثلاثة منشئات: $\mathrm{inl}: B \to B \coprod_A C$، و $\mathrm{inr}: C \to B \coprod_A C$، و $\mathrm{glue}: A \to \Delta^1 \to B \coprod_A C$. المنشئ الأخير يحقق المعادلات $\mathrm{glue}\, a\, j_0 = f\, a$ و $\mathrm{glue}\, a\, j_1 = g\, a$، حيث $[j_0, j_1] = j: 1 \coprod 1 \to \Delta^1$.

سنقول أن فئة مع ألياف تحقق *بديهية جداء الدفع* بالنسبة لخريطة $j: U \to V$ إذا كانت $U$ و $V$ قابلتين للأسّ، ولكل ليف $X \twoheadrightarrow Y$، فإن الخريطة $X^V \to Y^V \times_{Y^U} X^U$ هي ليف.

**قضية 4.2.** إذا كانت فئة مع ألياف $\mathcal{C}$ تحقق بديهية جداء الدفع بالنسبة لخريطة $j: U \to V$، فإن لها أنواع تمديد على طول $j$.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** extension types, path types, pushout-product axiom, higher inductive types, interval type
- **Equations:** Type theory rules and categorical definitions
- **Citations:** [4], [7], [11], [13]
- **Special handling:** Type-theoretic syntax and categorical semantics

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
