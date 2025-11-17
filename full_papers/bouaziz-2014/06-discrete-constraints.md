# Section 6: Discrete Constraints
## القسم 6: القيود المنفصلة

**Section:** Discrete Constraints
**Translation Quality:** 0.87
**Glossary Terms Used:** constraint, collision, solver, boundary conditions

---

### English Version

The constraints derived from continuous energies presented in the previous section allow modeling a large variety of elastic bodies. For practical animation systems additional constraints are equally important. We model these directly as discrete constraints.

**Positional constraints.** As seen earlier, individual DoFs can be directly constrained by simply choosing $A_i = B_i = I$ in Equation 7. Dirichlet boundary conditions can then be realized by defining the constraint set as the desired goal positions, in order to fix objects or create interactive handles.

**Collisions.** Handling collisions in an implicit manner fits naturally into our general solver and allows respecting the equilibrium of momentum and internal constraints during the collision resolution. When detecting a collision, we dynamically add new unilateral plane constraints. As for positional constraints, we again choose $A_i = B_i = I$ in Equation 7. For a colliding point $q_c$ we first find the closest surface point $b$ with normal $n$, defining a collision plane, such that the constraint set $C$ is defined by the half space $n^T(q - b) \geq 0$. The projection into this half space in the local step is trivial as it is either a plane projection or the identity map. Note that defining the collision constraint unilaterally allows us to overcome the commonly known sticking problems in implicit collisions handling. Similar to PBD, we handle friction and restitution by changing the velocities of colliding vertices when updating velocities. A simple damping model can also be implemented by filtering velocities.

**More constraints.** General types of geometric constraints, as for example bending constraints using hinge angles, can be easily incorporated into our solver. The local solve can be performed in a general manner by minimizing Equation 7 over the auxiliary variables. For many geometric constraints closed-form solutions for this minimization can be found. If no closed-form solutions exist, the optimization can be solved using sequential quadratic programming (SQP). As shown in Section 4.1, for the case of $A = B = M^{-1/2}$ one step of SQP is similar to the PBD update.

---

### النسخة العربية

تسمح القيود المشتقة من الطاقات المستمرة المقدمة في القسم السابق بنمذجة مجموعة كبيرة ومتنوعة من الأجسام المرنة. بالنسبة لأنظمة الرسوم المتحركة العملية، فإن القيود الإضافية مهمة بنفس القدر. نمذج هذه مباشرة كقيود منفصلة.

**القيود الموضعية.** كما رأينا سابقاً، يمكن تقييد درجات الحرية الفردية مباشرة من خلال اختيار ببساطة $A_i = B_i = I$ في المعادلة 7. يمكن بعد ذلك تحقيق شروط ديريكليه الحدية من خلال تعريف مجموعة القيود على أنها مواضع الهدف المرغوبة، من أجل تثبيت الأجسام أو إنشاء مقابض تفاعلية.

**الاصطدامات.** التعامل مع الاصطدامات بطريقة ضمنية يتناسب بشكل طبيعي مع حلالنا العام ويسمح باحترام توازن الزخم والقيود الداخلية أثناء حل الاصطدام. عند اكتشاف اصطدام، نضيف ديناميكياً قيود مستوى أحادية الجانب جديدة. بالنسبة للقيود الموضعية، نختار مرة أخرى $A_i = B_i = I$ في المعادلة 7. لنقطة اصطدام $q_c$ نجد أولاً أقرب نقطة سطح $b$ بالعمودي $n$، مع تعريف مستوى الاصطدام، بحيث يتم تعريف مجموعة القيود $C$ بنصف الفضاء $n^T(q - b) \geq 0$. الإسقاط في نصف الفضاء هذا في الخطوة المحلية تافه لأنه إما إسقاط مستوى أو خريطة الهوية. لاحظ أن تعريف قيد الاصطدام أحادي الجانب يسمح لنا بالتغلب على مشاكل الالتصاق المعروفة عادة في التعامل الضمني مع الاصطدامات. على غرار PBD، نتعامل مع الاحتكاك والارتداد من خلال تغيير سرعات الرؤوس المصطدمة عند تحديث السرعات. يمكن أيضاً تنفيذ نموذج تخميد بسيط من خلال ترشيح السرعات.

**قيود إضافية.** يمكن بسهولة دمج الأنواع العامة من القيود الهندسية، مثل قيود الانحناء باستخدام زوايا المفصلة، في حلالنا. يمكن إجراء الحل المحلي بطريقة عامة من خلال تصغير المعادلة 7 على المتغيرات المساعدة. بالنسبة للعديد من القيود الهندسية، يمكن إيجاد حلول ذات شكل مغلق لهذا التصغير. إذا لم توجد حلول ذات شكل مغلق، يمكن حل التحسين باستخدام البرمجة التربيعية التسلسلية (SQP). كما هو موضح في القسم 4.1، بالنسبة لحالة $A = B = M^{-1/2}$ فإن خطوة واحدة من SQP مشابهة لتحديث PBD.

---

### Translation Notes

- **Key terms:** Dirichlet boundary conditions (شروط ديريكليه الحدية), Unilateral constraints (قيود أحادية الجانب), Friction (الاحتكاك), Restitution (الارتداد), Sequential quadratic programming (البرمجة التربيعية التسلسلية)
- **Figures referenced:** Figure 10
- **Mathematical notation:** Preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
