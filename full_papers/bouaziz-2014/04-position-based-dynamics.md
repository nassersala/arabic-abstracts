# Section 4: Position Based Dynamics View
## القسم 4: منظور الديناميكيات القائمة على الموضع

**Section:** Position Based Dynamics View
**Translation Quality:** 0.87
**Glossary Terms Used:** position based dynamics, solver, optimization, constraint, convergence, momentum

---

### English Version

While [Liu et al. 2013] hint at the similarity between general variational implicit Euler and PBD, in this section, we derive the exact relationship not just between implicit Euler and PBD, but also between the local/global formulation and PBD, for general constraints. This analysis highlights the close connections of PBD to our solver, but also identifies fundamental differences that explain the higher accuracy of results obtained with our approach.

**4.1 Gauss-Seidel Solver**

A classical PBD solver [Müller et al. 2007] performs three steps. In the first step, the positions are initialized by an explicit Euler step, ignoring internal forces. In the second step, the positions are updated by projecting the current configuration consecutively on each constraint set respecting the mass weighting. In the last step, the velocities are updated as $v_{n+1} = (q_{n+1} - q_n)/h$.

We can show that the constraint resolution strategy of PBD actually implements a Gauss-Seidel type minimization on the energy

$$\frac{1}{2} \sum_i \|M_i^{-1/2}(S_i q - p_i)\|_F^2 + \mathbb{I}_{C_i}(p_i); \tag{11}$$

using a lumped mass matrix $M_i$ only involving the constraint's points. A Gauss-Seidel approach minimizes this energy by optimizing each summand sequentially, i.e., minimizing potentials of the form $\frac{1}{2}\|M^{-1/2}\Delta q\|_F^2 + C(q + \Delta q)$ where we introduce corrections $\Delta q = p - q$ to simplify the derivation. Using Lagrange multipliers for the linearized constraint $C(q) + \text{tr}(\nabla C(q)^T \Delta q) = 0$, we can define the Lagrangian

$$\frac{1}{2}\|M^{-1/2}\Delta q\|_F^2 + \lambda\left[C(q) + \text{tr}(\nabla C(q)^T \Delta q)\right]. \tag{12}$$

Using the critical point condition w.r.t. $\Delta q$, we find the optimal direction $\Delta q = -\lambda M^{-1} \nabla C(q)$. The Lagrange multiplier $\lambda$ can then be found by requiring that the linearized constraint vanishes in this direction, i.e., $C(q) - \lambda \|M^{-1/2} \nabla C(q)\|_F^2 = 0$, leading to the final update

$$\Delta q = -M^{-1} \nabla C(q) \frac{C(q)}{\|M^{-1/2} \nabla C(q)\|_F^2}; \tag{13}$$

corresponding exactly to the mass-weighted update rule of PBD [Bender et al. 2013].

**Discussion.** Theoretically, Gauss-Seidel has good convergence, however only for feasible constraint sets. For non-feasible sets, lacking a global view on the optimization problem, Gauss-Seidel will oscillate between the incompatible sets (see Figure 3). As an example, when simulating the compression of an elastic material with stretch constraints and boundary conditions or collisions, the constraints can become unfeasible and thus the solution will oscillate and not converge.

More severely, the same is true for the momentum estimation performed in the first step, which consists of first solving the constraint given in Equation 5. If added as a true constraint to the optimization, it could lead to completely incompatible constraint sets and make convergence even worse. By solving the momentum constraint first with the initial explicit Euler step, it is possible to maintain the linear momentum of the entire object, however the individual momenta of the points are washed away the longer the optimization iterates – contrary to finding a compromise between momentum and internal elasticity as suggested by the Implicit Euler solver that we propose (see Figure 4).

**4.2 Jacobi Solver**

In the view of Equation 11, we can solve these issues in a straightforward manner by performing two steps. First, we replace the Gauss-Seidel by a Jacobi solver (see Figure 3) that is able to deal with incompatible constraints. Jacobi solvers have in general slower convergence than Gauss-Seidel solvers [Thomaszewski et al. 2009]. However, they allow the use of differential coordinate representations for faster convergence and efficient parallelization of the constraint projections that resolve this shortcoming. Second, we introduce the momentum constraint into the optimization to take into account the inertia of each point. As seen in the continuum mechanics view, to achieve a correct behavior we need to add back the inertia of each point by integrating the momentum constraint term defined in Equation 5

$$\frac{1}{2h^2}\|M^{1/2}(q - s_n)\|_F^2 + \sum_i \frac{w_i}{2}\|M_i^{-1/2}(S_i q - p_i)\|_F^2 + \mathbb{I}_{C_i}(p_i). \tag{14}$$

The Jacobi solver then becomes a two-step optimization: In the local step, the current solution $q$ is first projected onto the constraints independently by solving Equation 11 for all $p_i$. Then, a consensus can be reached between the different solutions by solving the global step over $q$.

**Connection to Projective Implicit Euler.** At this stage, we can see how close this Jacobi solver is to our projective implicit solver procedure presented in the last section – we recover this solver by choosing $A_i = B_i = M_i^{-1/2}$. By deriving constraints from a continuum principle in the next section we furthermore achieve better independence on mesh tessellation and convergence than with the simpler mass-based weighting used in PBD (see Figure 5).

---

### النسخة العربية

بينما يلمح [Liu et al. 2013] إلى التشابه بين أويلر الضمني التغايري العام وPBD، في هذا القسم، نشتق العلاقة الدقيقة ليس فقط بين أويلر الضمني وPBD، ولكن أيضاً بين الصياغة المحلية/العامة وPBD، للقيود العامة. يسلط هذا التحليل الضوء على الروابط الوثيقة بين PBD وحلالنا، ولكنه يحدد أيضاً الاختلافات الأساسية التي تفسر الدقة الأعلى للنتائج التي تم الحصول عليها بنهجنا.

**4.1 حلال Gauss-Seidel**

يؤدي حلال PBD الكلاسيكي [Müller et al. 2007] ثلاث خطوات. في الخطوة الأولى، يتم تهيئة المواضع بخطوة أويلر صريحة، متجاهلاً القوى الداخلية. في الخطوة الثانية، يتم تحديث المواضع من خلال إسقاط التكوين الحالي بشكل متتابع على كل مجموعة قيود مع احترام ترجيح الكتلة. في الخطوة الأخيرة، يتم تحديث السرعات على أنها $v_{n+1} = (q_{n+1} - q_n)/h$.

يمكننا أن نُظهر أن استراتيجية حل القيود الخاصة بـ PBD تنفذ فعلياً تصغيراً من نوع Gauss-Seidel على الطاقة

$$\frac{1}{2} \sum_i \|M_i^{-1/2}(S_i q - p_i)\|_F^2 + \mathbb{I}_{C_i}(p_i); \tag{11}$$

باستخدام مصفوفة كتلة مُجمّعة $M_i$ تشمل فقط نقاط القيد. يصغّر نهج Gauss-Seidel هذه الطاقة من خلال تحسين كل مجموع بشكل تسلسلي، أي تصغير الطاقات الكامنة من النموذج $\frac{1}{2}\|M^{-1/2}\Delta q\|_F^2 + C(q + \Delta q)$ حيث نقدم تصحيحات $\Delta q = p - q$ لتبسيط الاشتقاق. باستخدام مضاعفات لاغرانج للقيد المخطط $C(q) + \text{tr}(\nabla C(q)^T \Delta q) = 0$، يمكننا تعريف لاغرانجي

$$\frac{1}{2}\|M^{-1/2}\Delta q\|_F^2 + \lambda\left[C(q) + \text{tr}(\nabla C(q)^T \Delta q)\right]. \tag{12}$$

باستخدام شرط النقطة الحرجة بالنسبة لـ $\Delta q$، نجد الاتجاه الأمثل $\Delta q = -\lambda M^{-1} \nabla C(q)$. يمكن بعد ذلك إيجاد مضاعف لاغرانج $\lambda$ من خلال طلب أن يختفي القيد المخطط في هذا الاتجاه، أي $C(q) - \lambda \|M^{-1/2} \nabla C(q)\|_F^2 = 0$، مما يؤدي إلى التحديث النهائي

$$\Delta q = -M^{-1} \nabla C(q) \frac{C(q)}{\|M^{-1/2} \nabla C(q)\|_F^2}; \tag{13}$$

المطابق تماماً لقاعدة التحديث المرجحة بالكتلة لـ PBD [Bender et al. 2013].

**المناقشة.** نظرياً، Gauss-Seidel له تقارب جيد، ولكن فقط لمجموعات القيود الممكنة. بالنسبة للمجموعات غير الممكنة، وبسبب افتقاره إلى رؤية عامة لمشكلة التحسين، سيتذبذب Gauss-Seidel بين المجموعات غير المتوافقة (انظر الشكل 3). كمثال، عند محاكاة ضغط مادة مرنة مع قيود التمدد والشروط الحدية أو الاصطدامات، يمكن أن تصبح القيود غير ممكنة وبالتالي سيتذبذب الحل ولن يتقارب.

بشكل أكثر خطورة، الأمر نفسه صحيح لتقدير الزخم الذي يتم إجراؤه في الخطوة الأولى، والذي يتكون من حل القيد المعطى في المعادلة 5 أولاً. إذا تمت إضافته كقيد حقيقي للتحسين، فقد يؤدي إلى مجموعات قيود غير متوافقة تماماً ويجعل التقارب أسوأ. من خلال حل قيد الزخم أولاً بخطوة أويلر الصريحة الأولية، من الممكن الحفاظ على الزخم الخطي للجسم بأكمله، ومع ذلك فإن الزخوم الفردية للنقاط تُغسل كلما طالت تكرارات التحسين - على عكس إيجاد حل وسط بين الزخم والمرونة الداخلية كما يقترح حلال أويلر الضمني الذي نقترحه (انظر الشكل 4).

**4.2 حلال Jacobi**

من وجهة نظر المعادلة 11، يمكننا حل هذه المشكلات بطريقة مباشرة من خلال تنفيذ خطوتين. أولاً، نستبدل Gauss-Seidel بحلال Jacobi (انظر الشكل 3) القادر على التعامل مع القيود غير المتوافقة. عموماً، حلالات Jacobi لها تقارب أبطأ من حلالات Gauss-Seidel [Thomaszewski et al. 2009]. ومع ذلك، فإنها تسمح باستخدام تمثيلات الإحداثيات التفاضلية لتقارب أسرع والتوازي الفعال لإسقاطات القيود التي تحل هذا القصور. ثانياً، نقدم قيد الزخم في التحسين لأخذ القصور الذاتي لكل نقطة في الاعتبار. كما رأينا في منظور ميكانيكا الاستمرارية، لتحقيق سلوك صحيح نحتاج إلى إضافة القصور الذاتي لكل نقطة من خلال دمج حد قيد الزخم المحدد في المعادلة 5

$$\frac{1}{2h^2}\|M^{1/2}(q - s_n)\|_F^2 + \sum_i \frac{w_i}{2}\|M_i^{-1/2}(S_i q - p_i)\|_F^2 + \mathbb{I}_{C_i}(p_i). \tag{14}$$

يصبح حلال Jacobi بعد ذلك تحسيناً من خطوتين: في الخطوة المحلية، يتم أولاً إسقاط الحل الحالي $q$ على القيود بشكل مستقل من خلال حل المعادلة 11 لجميع $p_i$. بعد ذلك، يمكن التوصل إلى إجماع بين الحلول المختلفة من خلال حل الخطوة العامة على $q$.

**الارتباط بأويلر الضمني الإسقاطي.** في هذه المرحلة، يمكننا أن نرى مدى قرب حلال Jacobi هذا من إجراء حلالنا الضمني الإسقاطي المقدم في القسم الأخير - نستعيد هذا الحلال من خلال اختيار $A_i = B_i = M_i^{-1/2}$. من خلال اشتقاق القيود من مبدأ الاستمرارية في القسم التالي، نحقق علاوة على ذلك استقلالية أفضل عن تفسيفة الشبكة والتقارب مما هو عليه مع الترجيح البسيط القائم على الكتلة المستخدم في PBD (انظر الشكل 5).

---

### Translation Notes

- **Equations:** Equations 11-14 preserved in LaTeX format
- **Figures referenced:** Figure 3, Figure 4, Figure 5
- **Key terms introduced:**
  - Gauss-Seidel: Gauss-Seidel (kept as is - proper name)
  - Jacobi solver: حلال Jacobi (kept Jacobi as proper name)
  - Lumped mass matrix: مصفوفة كتلة مُجمّعة
  - Lagrange multipliers: مضاعفات لاغرانج
  - Lagrangian: لاغرانجي
  - Feasible constraint sets: مجموعات القيود الممكنة
  - Linear momentum: الزخم الخطي
  - Inertia: القصور الذاتي
  - Consensus: إجماع

- **Special handling:**
  - Mathematical notation preserved exactly
  - Proper names (Gauss-Seidel, Jacobi) kept in Latin script
  - PBD acronym maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
