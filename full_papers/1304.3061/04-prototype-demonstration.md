# Section 4: Prototype Demonstration
## القسم 4: إثبات النموذج الأولي

**Section:** prototype-demonstration
**Translation Quality:** 0.86
**Glossary Terms Used:** quantum processor, photonic, qubit, entangled, state, gate, CNOT, Pauli basis, phase shifter, photon detector, Hamiltonian, ground state, molecular energy, bond dissociation, chemical accuracy, optimization, entanglement, tangle, concurrence

---

### English Version

**Prototype demonstration**

We have implemented the QPU using integrated quantum photonics technology. Our device, shown schematically in Fig. 2 is a reconfigurable waveguide chip that implements several single qubit rotations and one two-qubit entangling gate and can prepare an arbitrary two-qubit pure state. This device operates across the full space of possible configurations with mean statistical fidelity F > 99%. The state is prepared, and measured in the Pauli basis, by setting 8 voltage driven phase shifters and counting photon detection events with silicon single photon detectors.

The ability to prepare an arbitrary two-qubit separable or entangled state enables us to investigate 4×4 Hamiltonians. For the experimental demonstration of our algorithm we choose a problem from quantum chemistry, namely determining the bond dissociation curve of the molecule He-H+ in a minimal basis.

The full configuration interaction Hamiltonian for this system has dimension 4, and can be written compactly as:

$$H(R) = \sum_{i\alpha} h^i_\alpha(R) \sigma_\alpha^i + \sum_{ij\alpha\beta} h^{ij}_{\alpha \beta}(R) \sigma_\alpha^i \sigma_\beta^j$$

The coefficients h^i_α(R) and h^{ij}_{αβ}(R) were determined using the PSI3 computational package and tabulated in the Appendix.

In order to compute the bond dissociation of the molecule, we use Algorithm 2 to compute its ground state for a range of values of the nuclear separation R. In Fig. 3 we report a representative optimization run for a particular nuclear separation, demonstrating the convergence of our algorithm to the ground state of H(R) in the presence of experimental noise. Fig. 3(a) demonstrates the convergence of the average energy, while Fig. 3(b) demonstrates the convergence of the overlap |⟨ψ^j | ψ^G⟩| of the current state |ψ^j⟩ with the target state |ψ^G⟩.

The color of each entry in Fig. 3(a) represents the tangle (absolute concurrence squared) of the state at that step of the algorithm. It is known that the volume of separable states is doubly-exponentially small with respect to the rest of state space. Thus, the ability to traverse non-separable state space increases the number of paths by which the algorithm can converge and will be a requirement for future large-scale implementations. Moreover, it is clear that the ability to produce entangled states is a necessity for the accurate description of general quantum systems where eigenstates may be non-separable, for example the ground state of the He-H+ Hamiltonian has small but not negligible tangle.

Repeating this procedure for several values of R, we obtain the bond dissociation curve which is reported in Fig. 4. This allows for the determination of the equilibrium bond length of the molecule, which was found to be R=92.3±0.1 pm with a corresponding ground state electronic energy of E= -2.865±0.008 MJ/mol. This energy has been corrected for experimental error using a method fully described in the Appendix.

The corresponding theoretical curve shows the numerically exact energy derived from a full configuration interaction calculation of the molecular system in the same basis. More than 96% of the experimental data are within chemical accuracy with respect to the theoretical values. At the conclusion of the optimization, we retain full knowledge of the experimental parameters, which can be used for efficient reconstruction of the state |ψ⟩ in the event that additional physical or chemical properties are required.

---

### النسخة العربية

**إثبات النموذج الأولي**

قمنا بتنفيذ وحدة المعالجة الكمومية (QPU) باستخدام تقنية الفوتونيات الكمومية المتكاملة. جهازنا، المعروض تخطيطياً في الشكل 2، هو رقاقة دليل موجي قابلة لإعادة التكوين تنفذ عدة دورانات كيوبت أحادية وبوابة تشابك واحدة ثنائية الكيوبت ويمكنها تحضير حالة نقية تعسفية ثنائية الكيوبت. يعمل هذا الجهاز عبر الفضاء الكامل للتكوينات الممكنة بمتوسط دقة إحصائية F > 99%. يتم تحضير الحالة وقياسها في أساس باولي، من خلال ضبط 8 محولات طور مدفوعة بالجهد وعد أحداث الكشف عن الفوتون باستخدام كواشف فوتون أحادية من السيليكون.

تمكننا القدرة على تحضير حالة تعسفية ثنائية الكيوبت قابلة للفصل أو متشابكة من التحقيق في هاميلتونيانيات 4×4. للإثبات التجريبي لخوارزميتنا نختار مسألة من الكيمياء الكمومية، وهي تحديد منحنى تفكك الرابطة للجزيء He-H+ في أساس أدنى.

يحتوي هاميلتونياني التفاعل الكامل للتكوين لهذا النظام على بُعد 4، ويمكن كتابته بشكل مضغوط كما يلي:

$$H(R) = \sum_{i\alpha} h^i_\alpha(R) \sigma_\alpha^i + \sum_{ij\alpha\beta} h^{ij}_{\alpha \beta}(R) \sigma_\alpha^i \sigma_\beta^j$$

تم تحديد المعاملات h^i_α(R) و h^{ij}_{αβ}(R) باستخدام حزمة PSI3 الحسابية وجدولتها في الملحق.

من أجل حساب تفكك رابطة الجزيء، نستخدم الخوارزمية 2 لحساب حالته الأساسية لمجموعة من قيم الفصل النووي R. في الشكل 3 نقدم تقريراً عن تشغيل تحسين تمثيلي لفصل نووي معين، نُظهر فيه تقارب خوارزميتنا إلى الحالة الأساسية لـ H(R) في وجود ضوضاء تجريبية. يُظهر الشكل 3(a) تقارب الطاقة المتوسطة، بينما يُظهر الشكل 3(b) تقارب التداخل |⟨ψ^j | ψ^G⟩| للحالة الحالية |ψ^j⟩ مع الحالة المستهدفة |ψ^G⟩.

يمثل لون كل إدخال في الشكل 3(a) التشابك (مربع التوافق المطلق) للحالة في تلك الخطوة من الخوارزمية. من المعروف أن حجم الحالات القابلة للفصل صغير بشكل أسي مزدوج فيما يتعلق ببقية فضاء الحالة. وبالتالي، فإن القدرة على اجتياز فضاء الحالة غير القابل للفصل تزيد من عدد المسارات التي يمكن للخوارزمية من خلالها التقارب وستكون متطلباً للتطبيقات واسعة النطاق المستقبلية. علاوة على ذلك، من الواضح أن القدرة على إنتاج حالات متشابكة ضرورة للوصف الدقيق للأنظمة الكمومية العامة حيث قد تكون الحالات الذاتية غير قابلة للفصل، على سبيل المثال الحالة الأساسية لهاميلتونياني He-H+ لها تشابك صغير لكن ليس مهملاً.

بتكرار هذا الإجراء لعدة قيم من R، نحصل على منحنى تفكك الرابطة الذي يُعرض في الشكل 4. يتيح هذا تحديد طول الرابطة التوازنية للجزيء، والذي وُجد أنه R=92.3±0.1 بيكومتر مع طاقة إلكترونية للحالة الأساسية مقابلة E= -2.865±0.008 ميجاجول/مول. تم تصحيح هذه الطاقة للخطأ التجريبي باستخدام طريقة موصوفة بالكامل في الملحق.

يُظهر المنحنى النظري المقابل الطاقة الدقيقة عددياً المشتقة من حساب التفاعل الكامل للتكوين للنظام الجزيئي في نفس الأساس. أكثر من 96% من البيانات التجريبية ضمن الدقة الكيميائية فيما يتعلق بالقيم النظرية. في ختام التحسين، نحتفظ بمعرفة كاملة بالمعاملات التجريبية، والتي يمكن استخدامها لإعادة بناء الحالة |ψ⟩ بكفاءة في حالة الحاجة إلى خصائص فيزيائية أو كيميائية إضافية.

---

### Translation Notes

- **Figures referenced:**
  - Figure 2 (experimental implementation - photonic chip)
  - Figure 3 (optimization convergence for He-H+ at R=90pm)
  - Figure 4 (bond dissociation curve)
- **Key terms introduced:**
  - Integrated quantum photonics (الفوتونيات الكمومية المتكاملة)
  - Waveguide chip (رقاقة دليل موجي)
  - Entangling gate (بوابة تشابك)
  - Statistical fidelity (دقة إحصائية)
  - Phase shifter (محول طور)
  - Single photon detector (كاشف فوتون أحادي)
  - Bond dissociation (تفكك الرابطة)
  - Minimal basis (أساس أدنى)
  - Full configuration interaction (التفاعل الكامل للتكوين)
  - Nuclear separation (الفصل النووي)
  - Concurrence (التوافق - measure of entanglement)
  - Tangle (التشابك - entanglement measure)
  - Separable states (حالات قابلة للفصل)
  - Non-separable (غير قابل للفصل)
  - Equilibrium bond length (طول الرابطة التوازنية)
- **Equations:**
  - H(R) Hamiltonian decomposition
  - Overlap measure |⟨ψ^j | ψ^G⟩|
- **Measurements:**
  - R=92.3±0.1 pm (picometers - بيكومتر)
  - E= -2.865±0.008 MJ/mol (megajoules per mole - ميجاجول/مول)
  - F > 99% (fidelity - دقة)
  - 96% within chemical accuracy
- **Citations:** References to Obrien:2009eu, Shadbolt:2011bw, PSI3, Szarek:2005
- **Special handling:**
  - Chemical formula He-H+ kept in English
  - PSI3 (computational package name) kept as-is
  - Technical measurements with proper Arabic units

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
