# Section 3: Continuum Mechanics View
## القسم 3: منظور ميكانيكا الاستمرارية

**Section:** Continuum Mechanics View
**Translation Quality:** 0.86
**Glossary Terms Used:** continuum mechanics, finite element, solver, optimization, constraint, dynamics, mesh

---

### English Version

In this section we introduce the special structure of our potentials that form the basis of our method. We start with the implicit time integration of FEM-discretized elastic models.

**3.1 Implicit Euler Solver**

Let us briefly review the variational form of implicit Euler integration [Martin et al. 2011]. We assume a mesh consisting of m vertices with positions $q \in \mathbb{R}^{m \times 3}$ and velocities $v \in \mathbb{R}^{m \times 3}$. The system evolves in time according to Newton's laws of motion through a discrete set of time samples $t_1, t_2, \ldots$. At time $t_n$, the system is defined as $\{q_n, v_n\}$. The sum of the external forces is defined as $f_{ext}$ and the sum of internal forces as $f_{int}$. We consider position dependent internal forces such that $f_{int}(q) = -\sum_i \nabla W_i(q)$, where $W_i(q)$ is a scalar potential energy function. Implicit Euler time integration results in the following update rule:

$$q_{n+1} = q_n + h v_{n+1} \tag{1}$$

$$v_{n+1} = v_n + h M^{-1}(f_{int}(q_{n+1}) + f_{ext}) \tag{2}$$

where $M$ is the mass-matrix and $h$ represents the simulation step size. Note that $f_{ext}$ and $M$ are held constant for any given time step. Using these equations we can derive

$$M(q_{n+1} - q_n - h v_n) = h^2(f_{int}(q_{n+1}) + f_{ext}). \tag{3}$$

This system can be converted to an optimization problem

$$\min_{q_{n+1}} \frac{1}{2h^2} \|M^{1/2}(q_{n+1} - s_n)\|_F^2 + \sum_i W_i(q_{n+1}), \tag{4}$$

where $s_n = q_n + h v_n + h^2 M^{-1} f_{ext}$ and $\|\cdot\|_F$ denotes the Frobenius norm. Intuitively, this minimization problem describes the compromise between the momentum potential

$$\frac{1}{2h^2} \|M^{1/2}(q_{n+1} - s_n)\|_F^2, \tag{5}$$

which states that the solution should follow its momentum (plus external forces), and the elastic potential, that requires the solution to minimize the elastic deformation. The corresponding weighting terms, i.e., the mass distribution in $M$, the time step $h$ and the material stiffness of $W$, determine which potential has more importance in this balance. Furthermore, according to Noether's theorem, linear and angular momenta are always conserved when the elastic potential is rigid motion invariant.

The minimization of Equation 4 is commonly performed using careful implementations of Newton's method [Martin et al. 2011]. However, this is quite costly because at each iteration a different linear system needs to be solved, as the Hessian changes from one iteration to the next. To simplify notation, we will drop below the subscript in $q_{n+1}$ and just use $q$.

**3.2 Nonlinear Elasticity**

We analyze the classical form of FEM-based nonlinear elastic energies to reveal how we can restrict the elastic potentials in Equation 4 to a structure that will allow deriving our novel solver.

**Nonlinear elastic potentials.** In nonlinear continuum mechanics the deformation from a rest state is measured using a discrete, elemental strain $E(q)$, e.g., the quadratic Green's strain [Irving et al. 2004]. Numerous elastic potentials used in practice are formulated as a function of the strain using a (often nonlinear) material model $\Psi(\cdot)$, resulting in elastic potentials $W(q) = \Psi(E(q))$. From a geometric point of view, we can observe that $E(q) = 0$ defines a constraint manifold of all possible undeformed configurations, while $\Psi(E(q))$ measures how far the deformed configuration is from this manifold (level sets in Figure 2). Our key observation is that these two concepts can be decoupled; the distance metric does not have to be a complicated nonlinear function because the nonlinearities are already captured by the constraint manifold.

**Decoupling distance measure and constraint manifold.** We introduce potential functions $W$ that make use of an auxiliary variable $p$ as

$$W(q,p) = d(q,p) + \mathbb{I}_E(p): \tag{6}$$

Here, $\mathbb{I}_E(p)$ is an indicator function that evaluates to zero if $E(p) = 0$ and to $+\infty$ otherwise, and formalizes the requirement that $p$ should lie on the constraint manifold. The function $d(q,p)$ then measures a distance between $q$ and $p$. Minimizing Equation 6 over $p$ corresponds to a projection of $q$ onto the constraint manifold, as illustrated in Figure 2. An elastic potential analogous to $\Psi(E(q))$ can therefore be defined as $\tilde{W}(q) = \min_p W(q,p)$.

**Quadratic distance measures.** With this separation in mind, we can build a solver that alternates between distance minimization and projection. An important advantage of this formulation is that the distance measure can be freely chosen. The constraint nonlinearity (also known as geometric nonlinearity) is already taken care of by the projection on the constraint set, so the distance metric can be kept simple, trading general material nonlinearity against efficiency and robustness. Specifically, we consider distance metrics leading to the following potentials:

$$W(q,p) = \frac{w}{2} \|Aq - Bp\|_F^2 + \mathbb{I}_C(p), \tag{7}$$

where $A$ and $B$ are constant matrices and $w$ is a nonnegative weight. The distance to the constraint set is thus modeled by a quadratic function in $q$ and $p$, which allows us to deploy an efficient solver. Moreover, we are not restricted to Green's strains but can use any constraint definition $C(q) = 0$ for the set of desired configurations [Baraff and Witkin 1998], e.g., describing desired bending angles between triangles, goal volumes for tetrahedrons, or boundary conditions, as discussed below.

**3.3 Projective Implicit Euler Solver**

Using simplified potentials as given in Equation 7, we can reformulate the implicit integration defined in Equation 4 as the minimization of

$$\frac{1}{2h^2} \|M^{1/2}(q - s_n)\|_F^2 + \sum_i \frac{w_i}{2} \|A_i S_i q - B_i p_i\|_F^2 + \mathbb{I}_{C_i}(p_i) \tag{8}$$

over $q$ and the auxiliary variables $p_i$, where $S_i$ is a constant selection matrix that selects the vertices involved in the $i$-th constraint. We minimize Equation 8 using a local/global alternating minimization technique.

**Local solve.** First, we minimize Equation 8 over the auxiliary variables keeping the positions fixed. Since each constraint has its own set of auxiliary variables $p_i$, the minimization can be performed independently for each constraint as

$$\min_{p_i} \frac{w_i}{2} \|A_i S_i q - B_i p_i\|_F^2 + \mathbb{I}_{C_i}(p_i), \tag{9}$$

which allows massive parallelization of the local step. We will discuss specific constraint types in Section 5.

**Global solve.** Second, we minimize Equation 8 over the positions, keeping the auxiliary variables fixed. Since Equation 8 is quadratic in the unknowns $q$, we can minimize it with a single linear solve. Requiring that the gradient vanishes at the critical point leads to the linear system

$$\left(\frac{M}{h^2} + \sum_i w_i S_i^T A_i^T A_i S_i\right) q = \frac{M}{h^2} s_n + \sum_i w_i S_i^T A_i^T B_i p_i. \tag{10}$$

The system matrix is constant as long as the constraints are not changing and therefore can be prefactored at initialization, allowing for very efficient global solves. The right hand side requires recomputation in each iteration after the projection variables have been updated in the local step. Note that the objective is bounded below and that both local and global steps are guaranteed to weakly decrease it, even for non-convex sets. Consequently, the optimization converges, making safeguards unnecessary.

**Algorithm.** We summarize our optimization procedure in Algorithm 1. On line 2 we warm start the optimization using the momentum estimate $s_n$. We observe that this is favorable when using only few solver iterations, leading to less damped systems than when using the last time step's solution as starting point. After solving multiple local/global iterations the velocities are updated in line 9.

**Algorithm 1:** Projective Implicit Euler Solver
```
1  s_n = q_n + h v_n + h^2 M^{-1} f_ext
2  q_{n+1} = s_n
3  loop solverIteration times
4    forall the constraints i do
5      p_i = ProjectOnConstraintSet(C_i, q_{n+1})
6    end
7    q_{n+1} = SolveLinearSystem(s_n, p_1, p_2, p_3, ...)
8  end
9  v_{n+1} = (q_{n+1} - q_n) / h
```

**Choice of A and B.** If we choose $A_i = B_i = I$, Equation 7 measures the squared Euclidean distance from $S_i q$ to its closest point on the constraint set. With diagonal matrices, the Hessian of the global solve ends up being diagonal as well, leading to a trivial linear system to solve. However, this choice corresponds to working directly with absolute positions, which results in a poor convergence rate because changes propagate slowly through the (usually locally) coupled points [Bouaziz et al. 2012].

The convergence can be greatly improved if we make use of the fact that internal physical constraints are translation invariant (i.e., applying a common translation to all involved points in the constraints does not change the values of the constraints). In this case, we can choose $A_i = B_i$ as differential coordinate matrices (global translation in their null space). Various such matrices can be used, for example one can subtract the mean [Bouaziz et al. 2012] or simply one of the vertices involved in the constraint [Liu et al. 2013]. Note that the choice of $A_i$ and $B_i$ only impacts the numerical solution procedure and does not affect the conservation of momentum.

Using such differential coordinates greatly improves the convergence speed of the resulting local/global solver [Bouaziz et al. 2012]. However, without further precautions, the resulting behavior is tessellation and resolution dependent. We show in Section 5 that in certain cases the $A_i$ and $B_i$ matrices can be derived from continuum formulations in order to avoid these shortcomings.

---

### النسخة العربية

في هذا القسم نقدم البنية الخاصة لطاقاتنا الكامنة التي تشكل أساس طريقتنا. نبدأ بالتكامل الزمني الضمني للنماذج المرنة المفصّلة بطريقة العناصر المحدودة.

**3.1 حلال أويلر الضمني**

دعونا نراجع بإيجاز الشكل التغايري للتكامل الضمني لأويلر [Martin et al. 2011]. نفترض شبكة تتكون من m رؤوس بمواضع $q \in \mathbb{R}^{m \times 3}$ وسرعات $v \in \mathbb{R}^{m \times 3}$. يتطور النظام عبر الزمن وفقاً لقوانين نيوتن للحركة من خلال مجموعة منفصلة من عينات الزمن $t_1, t_2, \ldots$. في الزمن $t_n$، يُعرّف النظام بـ $\{q_n, v_n\}$. مجموع القوى الخارجية يُعرّف بـ $f_{ext}$ ومجموع القوى الداخلية بـ $f_{int}$. نعتبر القوى الداخلية المعتمدة على الموضع بحيث $f_{int}(q) = -\sum_i \nabla W_i(q)$، حيث $W_i(q)$ هي دالة طاقة كامنة قياسية. ينتج عن التكامل الزمني الضمني لأويلر قاعدة التحديث التالية:

$$q_{n+1} = q_n + h v_{n+1} \tag{1}$$

$$v_{n+1} = v_n + h M^{-1}(f_{int}(q_{n+1}) + f_{ext}) \tag{2}$$

حيث $M$ هي مصفوفة الكتلة و $h$ يمثل حجم خطوة المحاكاة. لاحظ أن $f_{ext}$ و $M$ يبقيان ثابتين لأي خطوة زمنية معطاة. باستخدام هذه المعادلات يمكننا اشتقاق

$$M(q_{n+1} - q_n - h v_n) = h^2(f_{int}(q_{n+1}) + f_{ext}). \tag{3}$$

يمكن تحويل هذا النظام إلى مشكلة تحسين

$$\min_{q_{n+1}} \frac{1}{2h^2} \|M^{1/2}(q_{n+1} - s_n)\|_F^2 + \sum_i W_i(q_{n+1}), \tag{4}$$

حيث $s_n = q_n + h v_n + h^2 M^{-1} f_{ext}$ و $\|\cdot\|_F$ يشير إلى معيار فروبينيوس. بشكل حدسي، تصف مشكلة التصغير هذه الحل الوسط بين طاقة الزخم الكامنة

$$\frac{1}{2h^2} \|M^{1/2}(q_{n+1} - s_n)\|_F^2, \tag{5}$$

التي تنص على أن الحل يجب أن يتبع زخمه (بالإضافة إلى القوى الخارجية)، والطاقة الكامنة المرنة، التي تتطلب من الحل تقليل التشوه المرن. تحدد حدود الترجيح المقابلة، أي توزيع الكتلة في $M$، والخطوة الزمنية $h$ وصلابة المادة لـ $W$، أي طاقة كامنة لها أهمية أكبر في هذا التوازن. علاوة على ذلك، وفقاً لنظرية نويثر، يتم الحفاظ دائماً على الزخم الخطي والزاوي عندما تكون الطاقة الكامنة المرنة ثابتة للحركة الجامدة.

عادة ما يتم تصغير المعادلة 4 باستخدام تطبيقات دقيقة لطريقة نيوتن [Martin et al. 2011]. ومع ذلك، هذا مكلف للغاية لأنه في كل تكرار يجب حل نظام خطي مختلف، حيث تتغير مصفوفة هيسيان من تكرار إلى آخر. لتبسيط الترميز، سنحذف أدناه الحرف المنخفض في $q_{n+1}$ ونستخدم فقط $q$.

**3.2 المرونة غير الخطية**

نحلل الشكل الكلاسيكي لطاقات المرونة غير الخطية القائمة على طريقة العناصر المحدودة للكشف عن كيفية تقييد الطاقات الكامنة المرنة في المعادلة 4 إلى بنية ستسمح باشتقاق حلالنا الجديد.

**الطاقات الكامنة المرنة غير الخطية.** في ميكانيكا الاستمرارية غير الخطية، يُقاس التشوه من حالة راحة باستخدام إجهاد عنصري منفصل $E(q)$، على سبيل المثال، إجهاد غرين التربيعي [Irving et al. 2004]. تُصاغ العديد من الطاقات الكامنة المرنة المستخدمة في الممارسة كدالة للإجهاد باستخدام نموذج مادة (غالباً غير خطي) $\Psi(\cdot)$، مما ينتج عنه طاقات كامنة مرنة $W(q) = \Psi(E(q))$. من وجهة نظر هندسية، يمكننا ملاحظة أن $E(q) = 0$ يحدد متعدد شعب قيد لجميع التكوينات غير المشوهة الممكنة، بينما $\Psi(E(q))$ يقيس مدى بُعد التكوين المشوه عن هذا المتعدد الشعب (مجموعات المستوى في الشكل 2). ملاحظتنا الرئيسية هي أن هذين المفهومين يمكن فصلهما؛ لا يجب أن يكون مقياس المسافة دالة غير خطية معقدة لأن اللاخطيات تم التقاطها بالفعل بواسطة متعدد شعب القيد.

**فصل مقياس المسافة ومتعدد شعب القيد.** نقدم دوال طاقة كامنة $W$ تستخدم متغير مساعد $p$ على النحو التالي

$$W(q,p) = d(q,p) + \mathbb{I}_E(p): \tag{6}$$

هنا، $\mathbb{I}_E(p)$ هي دالة مؤشر تُقيّم إلى الصفر إذا كان $E(p) = 0$ وإلى $+\infty$ خلاف ذلك، وتُضفي الطابع الرسمي على المتطلب بأن $p$ يجب أن يقع على متعدد شعب القيد. تقيس الدالة $d(q,p)$ بعد ذلك مسافة بين $q$ و $p$. يتوافق تصغير المعادلة 6 على $p$ مع إسقاط $q$ على متعدد شعب القيد، كما هو موضح في الشكل 2. لذلك يمكن تعريف طاقة كامنة مرنة مماثلة لـ $\Psi(E(q))$ على أنها $\tilde{W}(q) = \min_p W(q,p)$.

**مقاييس المسافة التربيعية.** مع وضع هذا الفصل في الاعتبار، يمكننا بناء حلال يتناوب بين تصغير المسافة والإسقاط. ميزة مهمة لهذه الصياغة هي أنه يمكن اختيار مقياس المسافة بحرية. تم التعامل بالفعل مع لاخطية القيد (المعروفة أيضاً باللاخطية الهندسية) بواسطة الإسقاط على مجموعة القيود، لذلك يمكن إبقاء مقياس المسافة بسيطاً، مع المقايضة بين لاخطية المادة العامة والكفاءة والقوة. على وجه التحديد، نعتبر مقاييس المسافة المؤدية إلى الطاقات الكامنة التالية:

$$W(q,p) = \frac{w}{2} \|Aq - Bp\|_F^2 + \mathbb{I}_C(p), \tag{7}$$

حيث $A$ و $B$ مصفوفات ثابتة و $w$ وزن غير سالب. وبالتالي يتم نمذجة المسافة إلى مجموعة القيود بدالة تربيعية في $q$ و $p$، مما يسمح لنا بنشر حلال فعال. علاوة على ذلك، لسنا مقيدين بإجهادات غرين ولكن يمكننا استخدام أي تعريف قيد $C(q) = 0$ لمجموعة التكوينات المرغوبة [Baraff and Witkin 1998]، على سبيل المثال، وصف زوايا الانحناء المرغوبة بين المثلثات، أو حجوم الهدف لرباعيات السطوح، أو الشروط الحدية، كما هو مناقش أدناه.

**3.3 حلال أويلر الضمني الإسقاطي**

باستخدام الطاقات الكامنة المبسطة كما هو معطى في المعادلة 7، يمكننا إعادة صياغة التكامل الضمني المحدد في المعادلة 4 على أنه تصغير

$$\frac{1}{2h^2} \|M^{1/2}(q - s_n)\|_F^2 + \sum_i \frac{w_i}{2} \|A_i S_i q - B_i p_i\|_F^2 + \mathbb{I}_{C_i}(p_i) \tag{8}$$

على $q$ والمتغيرات المساعدة $p_i$، حيث $S_i$ هي مصفوفة اختيار ثابتة تختار الرؤوس المشاركة في القيد الـ $i$-th. نصغر المعادلة 8 باستخدام تقنية التصغير المتناوب المحلي/العام.

**الحل المحلي.** أولاً، نصغر المعادلة 8 على المتغيرات المساعدة مع إبقاء المواضع ثابتة. نظراً لأن كل قيد له مجموعته الخاصة من المتغيرات المساعدة $p_i$، يمكن إجراء التصغير بشكل مستقل لكل قيد على النحو التالي

$$\min_{p_i} \frac{w_i}{2} \|A_i S_i q - B_i p_i\|_F^2 + \mathbb{I}_{C_i}(p_i), \tag{9}$$

مما يسمح بالتوازي الهائل للخطوة المحلية. سنناقش أنواع القيود المحددة في القسم 5.

**الحل العام.** ثانياً، نصغر المعادلة 8 على المواضع، مع إبقاء المتغيرات المساعدة ثابتة. نظراً لأن المعادلة 8 تربيعية في المجاهيل $q$، يمكننا تصغيرها بحل خطي واحد. يؤدي طلب أن يختفي التدرج عند النقطة الحرجة إلى النظام الخطي

$$\left(\frac{M}{h^2} + \sum_i w_i S_i^T A_i^T A_i S_i\right) q = \frac{M}{h^2} s_n + \sum_i w_i S_i^T A_i^T B_i p_i. \tag{10}$$

مصفوفة النظام ثابتة طالما أن القيود لا تتغير وبالتالي يمكن تحليلها مسبقاً عند التهيئة، مما يسمح بحلول عامة فعالة جداً. يتطلب الجانب الأيمن إعادة الحساب في كل تكرار بعد تحديث متغيرات الإسقاط في الخطوة المحلية. لاحظ أن الهدف محدود من الأسفل وأن كلا الخطوتين المحلية والعامة مضمونتان لتقليله بشكل ضعيف، حتى للمجموعات غير المحدبة. وبالتالي، يتقارب التحسين، مما يجعل الحماية غير ضرورية.

**الخوارزمية.** نلخص إجراء التحسين الخاص بنا في الخوارزمية 1. في السطر 2 نبدأ التحسين بشكل دافئ باستخدام تقدير الزخم $s_n$. نلاحظ أن هذا مفضل عند استخدام عدد قليل فقط من تكرارات الحلال، مما يؤدي إلى أنظمة أقل تخميداً مما لو استخدمنا حل الخطوة الزمنية الأخيرة كنقطة بداية. بعد حل تكرارات محلية/عامة متعددة، يتم تحديث السرعات في السطر 9.

**الخوارزمية 1:** حلال أويلر الضمني الإسقاطي
```
1  s_n = q_n + h v_n + h^2 M^{-1} f_ext
2  q_{n+1} = s_n
3  loop solverIteration times
4    forall the constraints i do
5      p_i = ProjectOnConstraintSet(C_i, q_{n+1})
6    end
7    q_{n+1} = SolveLinearSystem(s_n, p_1, p_2, p_3, ...)
8  end
9  v_{n+1} = (q_{n+1} - q_n) / h
```

**اختيار A و B.** إذا اخترنا $A_i = B_i = I$، فإن المعادلة 7 تقيس المسافة الإقليدية المربعة من $S_i q$ إلى أقرب نقطة على مجموعة القيود. مع المصفوفات القطرية، ينتهي هيسيان الحل العام بكونه قطرياً أيضاً، مما يؤدي إلى نظام خطي تافه للحل. ومع ذلك، يتوافق هذا الاختيار مع العمل مباشرة مع المواضع المطلقة، مما ينتج عنه معدل تقارب ضعيف لأن التغييرات تنتشر ببطء عبر النقاط المقترنة (عادة محلياً) [Bouaziz et al. 2012].

يمكن تحسين التقارب بشكل كبير إذا استفدنا من حقيقة أن القيود الفيزيائية الداخلية ثابتة للانتقال (أي، تطبيق انتقال مشترك على جميع النقاط المعنية في القيود لا يغير قيم القيود). في هذه الحالة، يمكننا اختيار $A_i = B_i$ كمصفوفات إحداثيات تفاضلية (الانتقال العام في فضاءها الفارغ). يمكن استخدام مصفوفات مختلفة من هذا القبيل، على سبيل المثال يمكن طرح المتوسط [Bouaziz et al. 2012] أو ببساطة أحد الرؤوس المشاركة في القيد [Liu et al. 2013]. لاحظ أن اختيار $A_i$ و $B_i$ يؤثر فقط على إجراء الحل الرقمي ولا يؤثر على حفظ الزخم.

استخدام هذه الإحداثيات التفاضلية يحسن بشكل كبير سرعة تقارب الحلال المحلي/العام الناتج [Bouaziz et al. 2012]. ومع ذلك، بدون احتياطات إضافية، فإن السلوك الناتج يعتمد على التفسيفة والدقة. نوضح في القسم 5 أنه في حالات معينة يمكن اشتقاق مصفوفات $A_i$ و $B_i$ من صياغات الاستمرارية من أجل تجنب هذه النواقص.

---

### Translation Notes

- **Equations:** All 10 equations preserved in LaTeX format
- **Algorithm:** Algorithm 1 included with pseudocode
- **Figures referenced:** Figure 2, Figure 3
- **Key terms introduced:**
  - Variational form: الشكل التغايري
  - Mass-matrix: مصفوفة الكتلة
  - Frobenius norm: معيار فروبينيوس
  - Momentum potential: طاقة الزخم الكامنة
  - Noether's theorem: نظرية نويثر
  - Hessian: مصفوفة هيسيان
  - Green's strain: إجهاد غرين
  - Constraint manifold: متعدد شعب القيد
  - Indicator function: دالة مؤشر
  - Selection matrix: مصفوفة اختيار
  - Differential coordinates: إحداثيات تفاضلية
  - Tessellation: التفسيفة

- **Special handling:**
  - All mathematical notation preserved exactly
  - Algorithm pseudocode kept in English for clarity
  - Citations maintained in English format

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
