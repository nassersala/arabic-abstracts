# Section 5: Discussion
## القسم 5: المناقشة

**Section:** discussion
**Translation Quality:** 0.89
**Glossary Terms Used:** quantum resources, coherence time, parallelism, quantum gates, CNOT, ansatz, device ansatz, variational, optimization, quantum hardware, fault tolerance, quantum simulator, Bell inequality

---

### English Version

**Discussion**

Algorithm 1 uses relatively few quantum resources compared to QPE. Broadly speaking, QPE requires a large number of n-qubit quantum controlled operations to be performed in series—placing considerable demands on the number of components and coherence time—while the inherent parallelism of our scheme enables a small number of n-qubit gates to be exploited many times, drastically reducing these demands. Moreover, adding control to arbitrary unitary operations in practice is difficult if not impossible for current quantum architectures (although a proposed scheme to add control to arbitrary unitary operations has recently been demonstrated). To give a numerical example, the QPE circuit for a 4 × 4 Hamiltonian such as that demonstrated here would require at least 12 CNOT gates, while our method only requires one.

In implementing Algorithm 2, the device prepares ansatz states that are defined by a polynomial set of parameters. This ansatz might be chosen based on knowledge of the physical system of interest (as for the unitary coupled cluster and typical quantum chemistry ansätze) thus determining the device design. However, our architecture allows for an alternative, and potentially more promising approach, where the device is first constructed based on the available resources and we define the set of states that the device can prepare as the "device ansatz". Due to the quantum nature of the device, this ansatz can be very distinct from those used in traditional quantum chemistry. With this alternative approach the physical implementation is then given by a known sequence of quantum operations with adjustable parameters—determined at the construction of the device—with a maximum depth fixed by the coherence time of the physical qubits. This approach, while approximate, provides a variationally optimal solution for the given quantum resources and may still be able to provide qualitatively correct solutions, just as approximate methods do in traditional quantum chemistry (for example Hartree Fock). The unitary coupled cluster ansatz provides a concrete example where our approach provides an exponential advantage over known classical techniques.

We have developed and experimentally implemented a new approach to solving the eigenvalue problem with quantum hardware. Algorithm 1 shares with QPE the need to prepare a good approximation to the ground state, but replaces a single long coherent evolution by a number of shorter coherent calculations proportional to the number of terms in the Hamiltonian. While the effect of errors on each of these calculations is the same as in QPE, the reliance on a number of separate calculations makes the algorithm sensitive to variations in state preparation between the separate quantum calculations. This effect requires further investigation.

In Algorithm 2, we experimentally implemented a ground state preparation procedure through a direct variational algorithm on the control parameters of the quantum hardware. Larger calculations will require a choice of ansatz, for which there are two possibilities. One could experimentally implement chemically motivated ansätze such as the unitary coupled cluster method described in the Appendix. Alternatively one could pursue those ansätze that are most easy to implement experimentally—creating a new set of device ansätze states which would require classification in terms of their overlap with chemical ground states. Such a classification would be a good way to determine the value of a given experimental advance—for ground state problems it is best to focus limited experimental resources on those efforts that will most enhance the overlap of preparable states with chemical ground states. In addition to the above issues, which we leave to future work, an interesting avenue of research is to ask whether the conceptual approach described here could be used to address other intractable problems with quantum-enhanced computation. Examples that can be mapped to the ground state problem, and where the n-representability problem does not occur, include search engine optimisation and image recognition.

It should be noted that the approach presented here requires no control or auxiliary qubits, relying only on measurement techniques that are already well established. For example, in the two qubit case, these measurements are identical to those performed in Bell inequality experiments.

Quantum simulators with only a few tens of qubits are expected to outperform the capabilities of conventional computers, not including open questions regarding fault tolerance and errors/precision. Our scheme would allow such devices to be implemented using dramatically less resources than the current best known approach.

---

### النسخة العربية

**المناقشة**

تستخدم الخوارزمية 1 موارد كمومية قليلة نسبياً مقارنة بـ QPE. بشكل عام، يتطلب QPE عدداً كبيراً من العمليات الكمومية المتحكم فيها من n-كيوبت يتم تنفيذها على التوالي - مما يضع متطلبات كبيرة على عدد المكونات وزمن التماسك - بينما يمكّن التوازي الكامن في مخططنا من استغلال عدد صغير من بوابات n-كيوبت عدة مرات، مما يقلل بشكل كبير من هذه المتطلبات. علاوة على ذلك، فإن إضافة التحكم إلى العمليات الوحدوية التعسفية في الممارسة العملية صعب إن لم يكن مستحيلاً للمعماريات الكمومية الحالية (على الرغم من أنه تم مؤخراً إثبات مخطط مقترح لإضافة التحكم إلى العمليات الوحدوية التعسفية). لإعطاء مثال عددي، ستتطلب دائرة QPE لهاميلتونياني 4 × 4 مثل ذلك الذي تم إثباته هنا ما لا يقل عن 12 بوابة CNOT، بينما تتطلب طريقتنا واحدة فقط.

في تنفيذ الخوارزمية 2، يحضر الجهاز حالات أنزاتز محددة بمجموعة كثيرة حدود من المعاملات. قد يتم اختيار هذا الأنزاتز بناءً على معرفة النظام الفيزيائي محل الاهتمام (كما هو الحال بالنسبة للكتلة المقترنة الوحدوية وأنزاتزات الكيمياء الكمومية النموذجية) مما يحدد تصميم الجهاز. ومع ذلك، تسمح معماريتنا بنهج بديل، وربما أكثر واعدة، حيث يتم أولاً بناء الجهاز بناءً على الموارد المتاحة ونعرّف مجموعة الحالات التي يمكن للجهاز تحضيرها باسم "أنزاتز الجهاز". نظراً للطبيعة الكمومية للجهاز، يمكن أن يكون هذا الأنزاتز مختلفاً جداً عن تلك المستخدمة في الكيمياء الكمومية التقليدية. مع هذا النهج البديل، يتم إعطاء التنفيذ الفيزيائي بعد ذلك بتسلسل معروف من العمليات الكمومية بمعاملات قابلة للتعديل - يتم تحديدها عند بناء الجهاز - مع عمق أقصى ثابت بزمن التماسك للكيوبتات الفيزيائية. هذا النهج، رغم أنه تقريبي، يوفر حلاً أمثلاً تباينياً للموارد الكمومية المعطاة وقد يظل قادراً على توفير حلول صحيحة نوعياً، تماماً كما تفعل الأساليب التقريبية في الكيمياء الكمومية التقليدية (على سبيل المثال هارتري-فوك). يوفر أنزاتز الكتلة المقترنة الوحدوية مثالاً ملموساً حيث يوفر نهجنا ميزة أسية على التقنيات الكلاسيكية المعروفة.

لقد طورنا ونفذنا تجريبياً نهجاً جديداً لحل مسألة القيمة الذاتية بالأجهزة الكمومية. تشترك الخوارزمية 1 مع QPE في الحاجة إلى تحضير تقريب جيد للحالة الأساسية، لكنها تستبدل تطوراً متماسكاً طويلاً واحداً بعدد من الحسابات المتماسكة الأقصر متناسب مع عدد الحدود في الهاميلتونياني. بينما تأثير الأخطاء على كل من هذه الحسابات هو نفسه كما في QPE، فإن الاعتماد على عدد من الحسابات المنفصلة يجعل الخوارزمية حساسة للتغيرات في تحضير الحالة بين الحسابات الكمومية المنفصلة. يتطلب هذا التأثير مزيداً من التحقيق.

في الخوارزمية 2، نفذنا تجريبياً إجراء تحضير الحالة الأساسية من خلال خوارزمية تباينية مباشرة على معاملات التحكم للأجهزة الكمومية. ستتطلب الحسابات الأكبر اختيار أنزاتز، والذي توجد له احتمالان. يمكن للمرء تنفيذ أنزاتزات مدفوعة كيميائياً تجريبياً مثل طريقة الكتلة المقترنة الوحدوية الموصوفة في الملحق. بدلاً من ذلك، يمكن للمرء متابعة تلك الأنزاتزات الأسهل في التنفيذ تجريبياً - مما يخلق مجموعة جديدة من حالات أنزاتزات الجهاز والتي ستتطلب تصنيفاً من حيث تداخلها مع الحالات الأساسية الكيميائية. سيكون مثل هذا التصنيف طريقة جيدة لتحديد قيمة تقدم تجريبي معين - بالنسبة لمسائل الحالة الأساسية، من الأفضل تركيز الموارد التجريبية المحدودة على تلك الجهود التي ستعزز بشكل أكبر تداخل الحالات القابلة للتحضير مع الحالات الأساسية الكيميائية. بالإضافة إلى القضايا المذكورة أعلاه، والتي نتركها للعمل المستقبلي، فإن سبيلاً مثيراً للبحث هو السؤال عما إذا كان يمكن استخدام النهج المفاهيمي الموصوف هنا لمعالجة مسائل أخرى مستعصية بالحوسبة المعززة كمومياً. تتضمن الأمثلة التي يمكن ربطها بمسألة الحالة الأساسية، وحيث لا تحدث مشكلة قابلية التمثيل-n، تحسين محركات البحث والتعرف على الصور.

تجدر الإشارة إلى أن النهج المقدم هنا لا يتطلب كيوبتات تحكم أو مساعدة، ويعتمد فقط على تقنيات القياس الراسخة بالفعل. على سبيل المثال، في حالة الكيوبتين، هذه القياسات مطابقة لتلك التي يتم إجراؤها في تجارب عدم المساواة لبيل.

من المتوقع أن تتفوق المحاكيات الكمومية التي لديها بضعة عشرات من الكيوبتات فقط على قدرات الحواسيب التقليدية، دون تضمين الأسئلة المفتوحة المتعلقة بتحمل الأخطاء والأخطاء/الدقة. سيسمح مخططنا بتنفيذ مثل هذه الأجهزة باستخدام موارد أقل بكثير من أفضل نهج معروف حالياً.

---

### Translation Notes

- **Figures referenced:** None directly in this section
- **Key terms introduced:**
  - Device ansatz (أنزاتز الجهاز)
  - Auxiliary qubits (كيوبتات مساعدة)
  - Control qubits (كيوبتات تحكم)
  - Bell inequality (عدم المساواة لبيل)
  - Fault tolerance (تحمل الأخطاء)
  - Quantum simulator (محاكي كمومي)
  - Search engine optimisation (تحسين محركات البحث)
  - Image recognition (التعرف على الصور)
  - Qualitatively correct (صحيح نوعياً)
  - Variationally optimal (أمثل تباينياً)
- **Equations:** None in this section
- **Measurements:**
  - At least 12 CNOT gates vs. 1 (comparison)
  - A few tens of qubits (بضعة عشرات من الكيوبتات)
- **Citations:** Reference to Zhou:2011
- **Special handling:**
  - Discussion of future directions and open problems
  - Comparison with QPE algorithm throughout
  - Technical trade-offs explained
  - Ansatz vs. ansätze (plural) - both translated as أنزاتز with context
  - Hartree-Fock kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89
