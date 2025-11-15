# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** algorithm, optimization, gradient, stochastic, memory, performance, adaptive, convergence, sparse, objective function

---

### English Version

We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective functions, based on adaptive estimates of lower-order moments. The method is straightforward to implement, is computationally efficient, has little memory requirements, is invariant to diagonal rescaling of the gradients, and is well suited for problems that are large in terms of data and/or parameters. The method is also appropriate for non-stationary objectives and problems with very noisy and/or sparse gradients. The hyper-parameters have intuitive interpretations and typically require little tuning. We provide a regret bound on the convergence rate that is comparable to the best known results under the online convex optimization framework. Empirical results demonstrate that Adam works well in practice and compares favorably to other stochastic optimization methods. Finally, we discuss AdaMax, a variant of Adam based on the infinity norm.

---

### النسخة العربية

تقدم هذه الورقة Adam، "خوارزمية لتحسين الدوال الهدفية العشوائية القائمة على تدرجات الدرجة الأولى، استناداً إلى تقديرات تكيفية للعزوم ذات الدرجة الأدنى." الطريقة فعالة حسابياً مع الحد الأدنى من متطلبات الذاكرة وتتعامل بشكل فعال مع الأهداف غير الثابتة والتدرجات المتفرقة. يقدم المؤلفون تحليل تقارب نظري ويُظهرون مزايا الأداء التجريبي بالمقارنة مع طرق التحسين الأخرى، كما يناقشون AdaMax كمتغير.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** Adam, adaptive moment estimation, stochastic optimization, AdaMax
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Algorithm name "Adam" kept in English; AdaMax kept in English

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.92
- Readability: 0.91
- Glossary consistency: 0.92
- **Overall section score:** 0.92
