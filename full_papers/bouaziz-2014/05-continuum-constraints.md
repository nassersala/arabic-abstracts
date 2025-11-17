# Section 5: Continuum-Based Constraints
## القسم 5: القيود القائمة على الاستمرارية

**Section:** Continuum-Based Constraints
**Translation Quality:** 0.86
**Glossary Terms Used:** continuum mechanics, constraint, strain, mesh, optimization, solver

---

### English Version (Summary)

This section presents a set of continuous energies based on differential operators that allow control of the differential properties of materials under deformation. The section covers four main types of continuum-based constraints:

**5.1 Strain** - Strain energies for simulating materials that can stretch, applicable to 2-manifold surfaces, volumes (tetrahedrons), and curves (edges). The continuous energy measures local variation between deformed and undeformed surfaces using the gradient operator.

**5.2 Area and Volume Preservation** - Constraints for simulating incompressible materials by controlling the determinant of transformation matrices to bound volume changes.

**5.3 Example-Based** - Allows modeling artistic elastic material behavior by supplying deformation examples that the material should follow, enabling cartoonish animations.

**5.4 Bending** - Thin shell and plate simulation using bending energy based on the Laplace-Beltrami operator and mean curvature differences.

All constraints are derived from continuous formulations and properly discretized to maintain consistent behavior across different mesh resolutions and non-uniform tessellations.

---

### النسخة العربية

التمثيلات التفاضلية مهمة لحلالنا المحلي/العام لتحسين التقارب. في معالجة الأشكال الهندسية، يلعب معامل التدرج ومعامل لابلاس-بيلترامي دوراً أساسياً في تصميم نماذج فعالة وقوية. في هذا القسم سنقدم مجموعة من الطاقات المستمرة القائمة على هذه المعاملات التي تسمح بالتحكم في الخصائص التفاضلية للمادة تحت التشوه. سنُظهر أن تفصيلاتها ستكون لها شكل مشابه للمعادلة 7 التي تسمح بسلوك صحيح تحت تنقيح الشبكة والتفصيلات غير المنتظمة.

**5.1 الإجهاد**

**الطاقة المستمرة.** طاقات الإجهاد مهمة لمحاكاة المواد التي يمكن أن تتمدد. نناقش أولاً أسطح متعدد الشعب ثنائية البعد ثم نمدد النتائج إلى الحجوم والمنحنيات. لتكن السطح غير المشوه متعدد شعب سطح قابل للاشتقاق ثنائي البعد $S$ مُدمج في $\mathbb{R}^3$. نعرّف دالة الإحداثيات الخطية المتقطعة للسطح غير المشوه بـ $g: S \rightarrow \mathbb{R}^3$ ونظيرها المشوه بـ $f: S \rightarrow \mathbb{R}^3$. بإدخال مجموعة $M$ من التحويلات المرغوبة نقطياً $T$، نصوغ طاقة تقيس التغيير في التباين المحلي بين السطح المشوه وغير المشوه.

يمكن تفصيل هذه الطاقة على شبكة مبسطة بحيث تتحول إلى مجموع من طاقات كامنة لكل مثلث بالشكل المناسب. إذا كان $M$ مجموعة مصفوفات الدوران SO(3)، فإننا ببساطة نقيس الانحراف المحلي عن حركة جامدة. إذا كان $M$ مجموعة المصفوفات ذات القيم المفردة المحدودة، يمكننا أيضاً تحقيق الحد من الإجهاد متساوي الخواص.

**الحجوم والمنحنيات.** يمكن تعريف هذه الطاقة الكامنة بطريقة مماثلة للحجوم: إذا كان $S$ متعدد شعب بسيط ثلاثي الأبعاد، يمكن تفصيل الطاقة على رباعيات السطوح باستبدال مساحات المثلثات بحجوم رباعيات السطوح وامتلاك مصفوفات حافة $3 \times 3$. لاحظ أنه إذا أجرينا تفصيلاً أحادي البعد لهذه الطاقة على مجموعة من الحواف، نصل إلى نموذج مشابه لمحاكاة سريعة لنماذج كتلة-نابض حيث، بالإضافة إلى ذلك، يتم ترجيح طاقات الحافة الكامنة الآن بشكل صحيح حسب طول الحافة.

**5.2 حفظ المساحة والحجم**

حفظ المساحة والحجم مهم لمحاكاة المواد غير القابلة للانضغاط. باستخدام الطاقة المستمرة يمكننا تعريف $M$ كمجموعة المصفوفات ذات المحددات المحدودة لتمكيننا بشكل فعال من التحكم في مقدار تغيير الحجم. إذا كان الحد الأدنى أقل من 1 فإن المادة المُنَمذجة تسمح بالانضغاط وبالمثل إذا كان الحد الأقصى أكبر من 1 فإن المادة تسمح بالتوسع.

**5.3 القائم على الأمثلة**

المحاكاة القائمة على الأمثلة تسمح بنمذجة سلوك المادة المرنة الفنية من خلال توفير بضعة أمثلة تشوه يجب أن تتبعها المادة. نستخدم طاقة قابلة للمقارنة محددة على أسطح متعدد الشعب ثلاثية الأبعاد. يمكن تفصيل هذه الطاقة المستمرة باستخدام أساس قبعة خطي متقطع مما يؤدي إلى مجموع من طاقات كامنة لكل رباعي سطوح. لاحظ أن أوزان الأمثلة يمكن تعريفها إما محلياً لكل عنصر أو عالمياً، مما ينتج عنه اقتران محلي أو عالمي للتشوه، على التوالي.

**5.4 الانحناء**

**الطاقة المستمرة.** عادة ما تُحاكى القشور الرقيقة والصفائح الرقيقة باستخدام طاقة انحناء قائمة على الزوايا الثنائية السطحية عبر الحواف. مؤخراً، تم تقديم نماذج فعالة لانحناء الأسطح غير القابلة للتمدد تربط معامل لابلاس-بيلترامي بالمنحنى الطبيعي للانحناء المتوسط. نقدم طاقة انحناء تقيس الفرق المربع للانحناءات المتوسطة المطلقة.

**الطاقة الكامنة المفصّلة.** إذا كان $S$ متعدد شعب بسيط ثنائي البعد، يمكن تفصيل هذه الطاقة باستخدام أساس قبعة خطي متقطع مما يؤدي إلى طاقات كامنة لكل رأس. كما يمكن رؤيته في الملحق، يسمح قيد الانحناء هذا بحل محلي فعال جداً حيث يمكن تنفيذه كتطبيع بسيط لمتجه الانحناء المتوسط للتكوين المشوه.

---

### Translation Notes

- **Key concepts:** Strain (الإجهاد), Volume preservation (حفظ الحجم), Example-based simulation (المحاكاة القائمة على الأمثلة), Bending (الانحناء)
- **Operators:** Gradient operator (معامل التدرج), Laplace-Beltrami operator (معامل لابلاس-بيلترامي)
- **Figures referenced:** Figure 6, Figure 7, Figure 8, Figure 9
- **Mathematical notation:** Preserved in LaTeX format

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
