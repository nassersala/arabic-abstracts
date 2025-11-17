# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.87
**Glossary Terms Used:** continuum mechanics, physics, simulation, integration, optimization, constraint, dynamics

---

### English Version

Since the pioneering work of Terzopoulos and colleagues [1987], models derived from continuum mechanics play an important role in physics-based animation. The basic principle is that the resistance of an elastic object to deformations is quantified using an elastic potential energy – a scalar function whose variational derivative leads to the elastic force [Sifakis and Barbic 2012]. Unfortunately, the elastic forces are usually non-linear even for basic material models, which complicates time integration of the resulting equations of motion.

The simplest time integration schemes used in computer graphics are explicit and very fragile to large time steps [Press et al. 2007]. Implicit Euler methods significantly improve robustness [Baraff and Witkin 1998], but at the cost of solving a system of non-linear equations at every step. As shown in [Martin et al. 2011], this can be equivalently formulated as a non-convex optimization problem that operates directly on elastic potentials instead of forces. One of the main shortcomings of implicit Euler integration is artificial numerical damping. This motivated the development of symplectic integrators [Hairer et al. 2002; Kharevych et al. 2006] and mixed implicit-explicit methods (IMEX) [Bridson et al. 2003; Stern and Grinspun 2009], featuring better energy conservation properties. Another approach is energy budgeting [Su et al. 2013] which enforces energy conservation explicitly. However, implicit Euler integration continues to be one of the popular choices in applications of physics-based animation where robustness is an important criterion and numerical damping is not a major concern. Our solver is derived from the variational form of implicit Euler integration [Martin et al. 2011] as it gives an intuitive way of thinking about time integration in our framework – simply by adding another constraint to the system. This further allows us to draw connections between PBD and the implicit Euler integration scheme and results in a robust and efficient approach that is stable under large time steps.

Regardless of the particular flavor and formulation of implicit integration, Newton's method remains the computational workhorse for solving the system of non-linear equations. However, its robust implementation requires precautions such as conservative line search procedures and safeguards against indefinite Hessians [Boyd and Vandenberghe 2004]. From a performance standpoint, a serious drawback of Newton's method is the fact that the Hessian matrix and the gradient change at every iteration. Quasi-Newton methods therefore employ approximate Hessians, trading faster linear system solves for suboptimal descent directions (and therefore slower convergence) as demonstrated by [Desbrun et al. 1999; Hahn et al. 2012]. A similar strategy, explored in the context of co-rotated elasticity, is to use carefully scheduled updates of sparse Cholesky factorization [Hecht et al. 2012]. Recently, Liu and colleagues [2013] presented a method for efficient implicit time integration of mass-spring systems by introducing auxiliary variables that enable alternating local/global optimization. This approach, also known as block coordinate descent, has been previously used with great success in geometry processing [Sorkine and Alexa 2007; Bouaziz et al. 2012]. We also employ local/global alternation in our approach, but contrary to [Liu et al. 2013], which is limited to mass-spring systems and assumes only linear springs (Hooke's law), we show how to generalize this concept employing projection onto constraint sets to simulate general nodal dynamical systems.

Our constraint-based formulation bears some similarity with recent non-traditional approaches based on constraint projection. The idea of constraint projection is central to the Nucleus system [Stam 2009] and Position Based Dynamics [Müller et al. 2007; Bender et al. 2013]. In contrast to our solution, these methods do not treat the constraints in a global manner, but iteratively project onto them in a (non-linear) Gauss-Seidel-like fashion [Müller et al. 2007]. While the resulting algorithm is very easy to implement, this approach has a number of shortcomings: the Gauss-Seidel optimization does not converge very rapidly, the material stiffness depends on the number of iterations, and the result depends on the traversal order. In contrast, our method uses constraints to formulate elastic potentials that are rigorously combined with inertial terms as dictated by Newton's laws of motion. Our solver first computes all constraint projections separately and then finds the best compromise between them, which makes the solution independent of the order of constraints. To obtain faster convergence, constraints are expressed using differential coordinates, which often yields satisfactory results after just a few iterations. Furthermore, our solver converges to a true implicit Euler solution with our elastic energy, in contrast to Position Based Dynamics which converges to completely inelastic behavior.

Another closely related concept is shape matching [Müller et al. 2005; Rivers and James 2007] where, in contrast to our method, constraint projections are used to directly build elastic forces instead of potentials to simulate deformable objects. Constraint projections were also used in strain limiting [Provot 1995; Goldenthal et al. 2007; Thomaszewski et al. 2009; Wang et al. 2010; Narain et al. 2012] not as a standalone simulation technique but rather as a way to improve handling of stiff systems with standard time integration methods. In our approach we can also perform strain limiting but it is directly included in the implicit solver.

---

### النسخة العربية

منذ العمل الرائد لـ Terzopoulos وزملائه [1987]، تلعب النماذج المشتقة من ميكانيكا الاستمرارية دوراً مهماً في الرسوم المتحركة القائمة على الفيزياء. المبدأ الأساسي هو أن مقاومة الجسم المرن للتشوهات تُقاس باستخدام طاقة كامنة مرنة - دالة قياسية يؤدي مشتقها التغايري إلى القوة المرنة [Sifakis and Barbic 2012]. لسوء الحظ، عادة ما تكون القوى المرنة غير خطية حتى بالنسبة لنماذج المواد الأساسية، مما يعقد التكامل الزمني لمعادلات الحركة الناتجة.

أبسط مخططات التكامل الزمني المستخدمة في رسومات الحاسوب هي صريحة وهشة جداً للخطوات الزمنية الكبيرة [Press et al. 2007]. تحسن طرق أويلر الضمنية القوة بشكل كبير [Baraff and Witkin 1998]، ولكن على حساب حل نظام من المعادلات غير الخطية في كل خطوة. كما هو موضح في [Martin et al. 2011]، يمكن صياغة هذا بشكل مكافئ كمشكلة تحسين غير محدبة تعمل مباشرة على الطاقات الكامنة المرنة بدلاً من القوى. أحد أوجه القصور الرئيسية للتكامل الضمني لأويلر هو التخميد الرقمي الاصطناعي. وقد حفز هذا تطوير المكاملات التكافلية [Hairer et al. 2002; Kharevych et al. 2006] والطرق المختلطة الضمنية-الصريحة (IMEX) [Bridson et al. 2003; Stern and Grinspun 2009]، والتي تتميز بخصائص حفظ طاقة أفضل. نهج آخر هو ميزانية الطاقة [Su et al. 2013] الذي يفرض حفظ الطاقة بشكل صريح. ومع ذلك، يستمر التكامل الضمني لأويلر في كونه أحد الخيارات الشائعة في تطبيقات الرسوم المتحركة القائمة على الفيزياء حيث تكون القوة معياراً مهماً والتخميد الرقمي ليس مصدر قلق رئيسي. يُشتق حلالنا من الشكل التغايري للتكامل الضمني لأويلر [Martin et al. 2011] لأنه يوفر طريقة بديهية للتفكير في التكامل الزمني في إطار عملنا - ببساطة عن طريق إضافة قيد آخر إلى النظام. وهذا يسمح لنا كذلك برسم روابط بين PBD ومخطط التكامل الضمني لأويلر ويؤدي إلى نهج قوي وفعال مستقر تحت الخطوات الزمنية الكبيرة.

بغض النظر عن النكهة والصياغة المحددة للتكامل الضمني، تظل طريقة نيوتن المحرك الحسابي لحل نظام المعادلات غير الخطية. ومع ذلك، يتطلب تنفيذها القوي احتياطات مثل إجراءات البحث الخطي المحافظة والحماية ضد مصفوفات هيسيان غير المحددة [Boyd and Vandenberghe 2004]. من وجهة نظر الأداء، فإن عيباً خطيراً لطريقة نيوتن هو حقيقة أن مصفوفة هيسيان والتدرج يتغيران في كل تكرار. لذلك تستخدم طرق شبه نيوتن مصفوفات هيسيان تقريبية، مع المقايضة بين حل نظام خطي أسرع واتجاهات هبوط دون المستوى الأمثل (وبالتالي تقارب أبطأ) كما هو موضح في [Desbrun et al. 1999; Hahn et al. 2012]. استراتيجية مماثلة، تم استكشافها في سياق المرونة المشتركة الدوران، هي استخدام تحديثات مجدولة بعناية لتحليل تشوليسكي المتناثر [Hecht et al. 2012]. مؤخراً، قدم Liu وزملاؤه [2013] طريقة للتكامل الزمني الضمني الفعال لأنظمة الكتلة-النابض من خلال إدخال متغيرات مساعدة تمكّن من التحسين المحلي/العام المتناوب. هذا النهج، المعروف أيضاً بالهبوط المنسق على الكتل، تم استخدامه سابقاً بنجاح كبير في معالجة الأشكال الهندسية [Sorkine and Alexa 2007; Bouaziz et al. 2012]. نستخدم أيضاً التناوب المحلي/العام في نهجنا، ولكن على عكس [Liu et al. 2013]، والذي يقتصر على أنظمة الكتلة-النابض ويفترض فقط نوابض خطية (قانون هوك)، نُظهر كيفية تعميم هذا المفهوم باستخدام الإسقاط على مجموعات القيود لمحاكاة الأنظمة الديناميكية العقدية العامة.

صياغتنا القائمة على القيود تحمل بعض التشابه مع النُهُج غير التقليدية الحديثة القائمة على إسقاط القيود. فكرة إسقاط القيود مركزية في نظام Nucleus [Stam 2009] والديناميكيات القائمة على الموضع [Müller et al. 2007; Bender et al. 2013]. على عكس حلنا، هذه الطرق لا تعامل القيود بطريقة عامة، بل تُسقط عليها بشكل متكرر بطريقة تشبه Gauss-Seidel (غير خطية) [Müller et al. 2007]. في حين أن الخوارزمية الناتجة سهلة التنفيذ للغاية، فإن هذا النهج له عدد من أوجه القصور: تحسين Gauss-Seidel لا يتقارب بسرعة كبيرة، وصلابة المادة تعتمد على عدد التكرارات، والنتيجة تعتمد على ترتيب الاجتياز. على النقيض من ذلك، تستخدم طريقتنا القيود لصياغة طاقات كامنة مرنة يتم دمجها بصرامة مع الحدود القصورية كما تمليه قوانين نيوتن للحركة. يحسب حلالنا أولاً جميع إسقاطات القيود بشكل منفصل ثم يجد أفضل حل وسط بينها، مما يجعل الحل مستقلاً عن ترتيب القيود. للحصول على تقارب أسرع، يتم التعبير عن القيود باستخدام الإحداثيات التفاضلية، والتي غالباً ما تنتج نتائج مرضية بعد بضع تكرارات فقط. علاوة على ذلك، يتقارب حلالنا إلى حل أويلر ضمني حقيقي مع طاقتنا المرنة، على عكس الديناميكيات القائمة على الموضع التي تتقارب إلى سلوك غير مرن تماماً.

مفهوم آخر وثيق الصلة هو مطابقة الشكل [Müller et al. 2005; Rivers and James 2007] حيث، على عكس طريقتنا، تُستخدم إسقاطات القيود لبناء القوى المرنة مباشرة بدلاً من الطاقات الكامنة لمحاكاة الأجسام القابلة للتشوه. تم استخدام إسقاطات القيود أيضاً في الحد من الإجهاد [Provot 1995; Goldenthal et al. 2007; Thomaszewski et al. 2009; Wang et al. 2010; Narain et al. 2012] ليس كتقنية محاكاة قائمة بذاتها بل كوسيلة لتحسين التعامل مع الأنظمة الصلبة بطرق التكامل الزمني القياسية. في نهجنا يمكننا أيضاً إجراء الحد من الإجهاد ولكنه مُدرج مباشرة في الحلال الضمني.

---

### Translation Notes

- **Citations:** Numerous citations maintained in English format [Author et al. Year]
- **Key terms introduced:**
  - Elastic potential energy: طاقة كامنة مرنة
  - Variational derivative: مشتق تغايري
  - Implicit Euler methods: طرق أويلر الضمنية
  - Symplectic integrators: المكاملات التكافلية
  - Energy conservation: حفظ الطاقة
  - Quasi-Newton methods: طرق شبه نيوتن
  - Cholesky factorization: تحليل تشوليسكي
  - Mass-spring systems: أنظمة الكتلة-النابض
  - Hooke's law: قانون هوك
  - Gauss-Seidel: Gauss-Seidel (kept as is - proper name)
  - Shape matching: مطابقة الشكل
  - Strain limiting: الحد من الإجهاد

- **Special handling:**
  - System names (Nucleus) kept in English
  - Author names kept in English
  - IMEX acronym kept as is

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
