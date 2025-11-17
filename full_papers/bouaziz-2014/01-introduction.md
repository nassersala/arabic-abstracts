# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** simulation, dynamics, finite element, continuum mechanics, solver, optimization, constraint, position based dynamics

---

### English Version

Physics-based simulation of deformable material has become an indispensable tool in many areas of computer graphics. Virtual worlds, and more recently character animations, incorporate sophisticated simulations to greatly enhance visual experience, e.g., by simulating muscles, fat, hair, clothing, or vegetation. These models are often based on finite element discretizations of continuum-mechanics formulations, allowing highly accurate simulation of complex nonlinear materials.

Besides realism and accuracy, a number of other criteria are also important in computer graphics applications. By generality we mean the ability to simulate a large spectrum of behaviors, such as different types of geometries (solids, shells, rods), different material properties, or even art-directable extensions to classic physics-based simulation. Robustness refers to the capability to adequately handle difficult configurations, including large deformations, degenerate geometries, and large time steps. Robustness is especially important in real-time applications where there is no "second chance" to re-run a simulation, such as in computer games or medical training simulators. The simplicity of a solver is often important for its practical relevance. Building on simple, easily understandable concepts – and the resulting lightweight codebases – eases the maintenance of simulators and makes them adaptable to specific application needs. Performance is a critical enabling criterion for realtime applications. However, performance is no less important in offline simulations, where the turnaround time for testing new scenes and simulation parameters should be minimized.

Current continuum mechanics approaches often have unfavorable trade-offs between these criteria for certain computer graphics applications, which led to the development of alternative methods, such as Position Based Dynamics (PBD). Due to its generality, simplicity, robustness, and efficiency, PBD is now implemented in a wide range of high-end products including PhysX, Havok Cloth, Maya nCloth, and Bullet. While predominantly used in realtime applications, PBD is also often used in offline simulation. However, the desirable qualities of PBD come at the cost of limited accuracy, because PBD is not rigorously derived from continuum mechanical principles.

We propose a new implicit integration solver that bridges the gap between continuum mechanics and PBD. The key idea is to introduce energy potentials with a specific structure. More precisely, our potentials consist of a convex quadratic distance measure from a constraint. The constraints are general nonlinear functions that express the desired state of an element, for example, that the volume of a tetrahedron must remain within given bounds. The distance measure quantifies how much individual constraints are violated in a given deformed configuration. While our solver can handle arbitrary geometric constraints, we propose a specific set of constraints derived from continuous deformation energies. These continuum-based constraints are very practical because they considerably simplify parameter tuning especially when dealing with meshes of different resolutions and non-uniform tessellation.

The main advantage of our constraint-based potentials is that their structure enables an efficient local/global optimization (block coordinate descent). Specifically, the local step consists of projecting every element onto the constraint manifold, i.e., solving a small nonlinear problem per element. The global step combines the results of individuals projections, finding a compromise between all of the individual constraints, while also taking into account global effects such as inertia and external forces.

The local/global approach allows us to formulate an implicit integration solver that is guaranteed to weakly decrease the energy in every iteration without requiring any specific precautions. This contrasts with classical Newton's method which requires line search strategies and safeguards against singular or indefinite Hessians to guarantee robustness. Furthermore, with a fixed set of constraints, we can pre-factor the linear system of the global step, which greatly reduces computation time. The local steps consists of small independent optimization problems, which can be all executed in parallel.

To our knowledge, our method is the first to apply local/global optimization to simulate general dynamical systems. We demonstrate that this solution provides a robust and efficient approach to implicit integration, often significantly outperforming the classical Newton method. The connection between PBD and our solver reveals new insights on how PBD relates to traditional approaches based on finite element methods and Newtonian mechanics.

---

### النسخة العربية

أصبحت محاكاة المواد القابلة للتشوه القائمة على الفيزياء أداة لا غنى عنها في العديد من مجالات رسومات الحاسوب. تدمج العوالم الافتراضية، ومؤخراً رسوم الشخصيات المتحركة، محاكاة معقدة لتعزيز التجربة البصرية بشكل كبير، على سبيل المثال، من خلال محاكاة العضلات، والدهون، والشعر، والملابس، أو النباتات. غالباً ما تستند هذه النماذج إلى تقسيمات العناصر المحدودة لصياغات ميكانيكا الاستمرارية، مما يسمح بمحاكاة دقيقة للغاية للمواد غير الخطية المعقدة.

إلى جانب الواقعية والدقة، هناك عدد من المعايير الأخرى المهمة أيضاً في تطبيقات رسومات الحاسوب. نعني بالعمومية القدرة على محاكاة طيف واسع من السلوكيات، مثل أنواع مختلفة من الأشكال الهندسية (الأجسام الصلبة، والقشور، والقضبان)، وخصائص مواد مختلفة، أو حتى امتدادات قابلة للتوجيه الفني للمحاكاة القائمة على الفيزياء الكلاسيكية. تشير القوة إلى القدرة على التعامل بشكل مناسب مع التكوينات الصعبة، بما في ذلك التشوهات الكبيرة، والأشكال الهندسية المتدهورة، والخطوات الزمنية الكبيرة. القوة مهمة بشكل خاص في التطبيقات الفورية حيث لا توجد "فرصة ثانية" لإعادة تشغيل المحاكاة، مثل ألعاب الفيديو أو أجهزة محاكاة التدريب الطبي. غالباً ما تكون بساطة الحلال مهمة لأهميته العملية. البناء على مفاهيم بسيطة وسهلة الفهم - وما ينتج عنها من قواعد برمجية خفيفة الوزن - يسهل صيانة أجهزة المحاكاة ويجعلها قابلة للتكيف مع احتياجات تطبيقات محددة. الأداء معيار تمكيني حاسم للتطبيقات الفورية. ومع ذلك، فإن الأداء ليس أقل أهمية في المحاكاة غير المباشرة، حيث يجب تقليل وقت الدوران لاختبار مشاهد جديدة ومعاملات المحاكاة.

غالباً ما تحتوي نُهُج ميكانيكا الاستمرارية الحالية على مقايضات غير مواتية بين هذه المعايير لتطبيقات رسومات حاسوب معينة، مما أدى إلى تطوير طرق بديلة، مثل الديناميكيات القائمة على الموضع (PBD). نظراً لعموميتها وبساطتها وقوتها وكفاءتها، تم تنفيذ PBD الآن في مجموعة واسعة من المنتجات الراقية بما في ذلك PhysX وHavok Cloth وMaya nCloth وBullet. في حين تُستخدم في الغالب في التطبيقات الفورية، غالباً ما تُستخدم PBD أيضاً في المحاكاة غير المباشرة. ومع ذلك، تأتي الصفات المرغوبة لـ PBD على حساب الدقة المحدودة، لأن PBD لا تُشتق بصرامة من مبادئ ميكانيكا الاستمرارية.

نقترح حلالاً جديداً للتكامل الضمني يسد الفجوة بين ميكانيكا الاستمرارية وPBD. الفكرة الرئيسية هي إدخال طاقات كامنة ذات بنية محددة. بشكل أكثر دقة، تتكون طاقاتنا الكامنة من مقياس مسافة تربيعي محدب من قيد. القيود هي دوال غير خطية عامة تعبر عن الحالة المرغوبة لعنصر ما، على سبيل المثال، أن حجم رباعي السطوح يجب أن يبقى ضمن حدود معينة. يحدد مقياس المسافة مقدار انتهاك القيود الفردية في تكوين مشوه معين. بينما يمكن لحلالنا التعامل مع القيود الهندسية التعسفية، نقترح مجموعة محددة من القيود المشتقة من طاقات التشوه المستمرة. هذه القيود القائمة على الاستمرارية عملية جداً لأنها تبسط بشكل كبير ضبط المعاملات خاصة عند التعامل مع الشبكات ذات الدقة المختلفة والتفسيفة غير المنتظمة.

الميزة الرئيسية للطاقات الكامنة القائمة على القيود لدينا هي أن بنيتها تمكّن من التحسين المحلي/العام الفعال (الهبوط المنسق على الكتل). على وجه التحديد، تتكون الخطوة المحلية من إسقاط كل عنصر على متعدد شعب القيد، أي حل مشكلة غير خطية صغيرة لكل عنصر. تجمع الخطوة العامة نتائج الإسقاطات الفردية، مع إيجاد حل وسط بين جميع القيود الفردية، مع مراعاة التأثيرات العامة أيضاً مثل القصور الذاتي والقوى الخارجية.

يسمح لنا النهج المحلي/العام بصياغة حلال تكامل ضمني مضمون لتقليل الطاقة بشكل ضعيف في كل تكرار دون الحاجة إلى أي احتياطات محددة. هذا يتناقض مع طريقة نيوتن الكلاسيكية التي تتطلب استراتيجيات بحث خطي وحماية ضد مصفوفات هيسيان المفردة أو غير المحددة لضمان القوة. علاوة على ذلك، مع مجموعة ثابتة من القيود، يمكننا تحليل النظام الخطي للخطوة العامة مسبقاً، مما يقلل بشكل كبير من وقت الحساب. تتكون الخطوات المحلية من مشاكل تحسين صغيرة مستقلة، يمكن تنفيذها جميعاً بالتوازي.

على حد علمنا، طريقتنا هي الأولى التي تطبق التحسين المحلي/العام لمحاكاة الأنظمة الديناميكية العامة. نوضح أن هذا الحل يوفر نهجاً قوياً وفعالاً للتكامل الضمني، وغالباً ما يتفوق بشكل كبير على طريقة نيوتن الكلاسيكية. يكشف الارتباط بين PBD وحلالنا رؤى جديدة حول كيفية ارتباط PBD بالنُهُج التقليدية القائمة على طرق العناصر المحدودة وميكانيكا نيوتن.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:**
  - Deformable material: المواد القابلة للتشوه
  - Character animations: رسوم الشخصيات المتحركة
  - Finite element discretizations: تقسيمات العناصر المحدودة
  - Continuum mechanics: ميكانيكا الاستمرارية
  - Position Based Dynamics (PBD): الديناميكيات القائمة على الموضع
  - Implicit integration: التكامل الضمني
  - Energy potentials: طاقات كامنة
  - Constraint manifold: متعدد شعب القيد
  - Local/global optimization: التحسين المحلي/العام
  - Block coordinate descent: الهبوط المنسق على الكتل
  - Newton's method: طريقة نيوتن
  - Hessian: مصفوفة هيسيان

- **Special handling:**
  - Software names kept in English (PhysX, Havok Cloth, Maya nCloth, Bullet)
  - PBD acronym introduced in Arabic with English in parentheses

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
