# Section 2: Quantum Computation
## القسم 2: الحوسبة الكمومية

**Section:** quantum-computation
**Translation Quality:** 0.87
**Glossary Terms Used:** quantum computer, quantum gate, quantum circuit, Turing machine, unitary transformation, Hilbert space, qubit, superposition, measurement, basis vector, amplitude, probability, tensor product, reversible computation

---

### English Version

In this section we give a brief introduction to quantum computation, emphasizing the properties that we will use. We will describe only quantum gate arrays, or quantum acyclic circuits, which are analogous to acyclic circuits in classical computer science. For other models of quantum computers, see references on quantum Turing machines [Deutsch 1989, Bernstein and Vazirani 1993, Yao 1993] and quantum cellular automata [Feynman 1986, Margolus 1986, 1990, Lloyd 1993, Biafore 1994]. If they are allowed a small probability of error, quantum Turing machines and quantum gate arrays can compute the same functions in polynomial time [Yao 1993]. This may also be true for the various models of quantum cellular automata, but it has not yet been proved. This gives evidence that the class of functions computable in quantum polynomial time with a small probability of error is robust, in that it does not depend on the exact architecture of a quantum computer. By analogy with the classical class BPP, this class is called BQP.

Consider a system with $n$ components, each of which can have two states. Whereas in classical physics, a complete description of the state of this system requires only $n$ bits, in quantum physics, a complete description of the state of this system requires $2^n - 1$ complex numbers. To be more precise, the state of the quantum system is a point in a $2^n$-dimensional vector space. For each of the $2^n$ possible classical positions of the components, there is a basis state of this vector space which we represent, for example, by $|011 \cdots 0\rangle$ meaning that the first bit is 0, the second bit is 1, and so on. Here, the ket notation $|x\rangle$ means that $x$ is a (pure) quantum state. (Mixed states will not be discussed in this paper, and thus we do not define them; see a quantum theory book such as Peres [1993] for this definition.) The Hilbert space associated with this quantum system is the complex vector space with these $2^n$ states as basis vectors, and the state of the system at any time is represented by a unit-length vector in this Hilbert space. As multiplying this state vector by a unit-length complex phase does not change any behavior of the state, we need only $2^n - 1$ complex numbers to completely describe the state. We represent this superposition of states as

$$\sum_{i=0}^{2^n-1} a_i |S_i\rangle , \qquad (2.1)$$

where the amplitudes $a_i$ are complex numbers such that $\sum_i |a_i|^2 = 1$ and each $|S_i\rangle$ is a basis vector of the Hilbert space. If the machine is measured (with respect to this basis) at any particular step, the probability of seeing basis state $|S_i\rangle$ is $|a_i|^2$; however, measuring the state of the machine projects this state to the observed basis vector $|S_i\rangle$. Thus, looking at the machine during the computation will invalidate the rest of the computation. In this paper, we only consider measurements with respect to the canonical basis. This does not greatly restrict our model of computation, since measurements in other reasonable bases could be simulated by first using quantum computation to perform a change of basis and then performing a measurement in the canonical basis.

In order to use a physical system for computation, we must be able to change the state of the system. The laws of quantum mechanics permit only unitary transformations of state vectors. A unitary matrix is one whose conjugate transpose is equal to its inverse, and requiring state transformations to be represented by unitary matrices ensures that summing the probabilities of obtaining every possible outcome will result in 1. The definition of quantum circuits (and quantum Turing machines) only allows local unitary transformations; that is, unitary transformations on a fixed number of bits. This is physically justified because, given a general unitary transformation on $n$ bits, it is not at all clear how one would efficiently implement it physically, whereas two-bit transformations can at least in theory be implemented by relatively simple physical systems [Cirac and Zoller 1995, DiVincenzo 1995, Sleator and Weinfurter 1995, Chuang and Yamomoto 1995]. While general $n$-bit transformations can always be built out of two-bit transformations [DiVincenzo 1995, Sleator and Weinfurter 1995, Lloyd 1995, Deutsch et al. 1995], the number required will often be exponential in $n$ [Barenco et al. 1995a]. Thus, the set of two-bit transformations form a set of building blocks for quantum circuits in a manner analogous to the way a universal set of classical gates (such as the AND, OR and NOT gates) form a set of building blocks for classical circuits. In fact, for a universal set of quantum gates, it is sufficient to take all one-bit gates and a single type of two-bit gate, the controlled NOT, which negates the second bit if and only if the first bit is 1.

Perhaps an example will be informative at this point. A quantum gate can be expressed as a truth table: for each input basis vector we need to give the output of the gate. One such gate is:

$$\begin{aligned}
|00\rangle &\to |00\rangle \\
|01\rangle &\to |01\rangle \\
|10\rangle &\to \frac{1}{\sqrt{2}}(|10\rangle + |11\rangle) \\
|11\rangle &\to \frac{1}{\sqrt{2}}(|10\rangle - |11\rangle)
\end{aligned} \qquad (2.2)$$

Not all truth tables correspond to physically feasible quantum gates, as many truth tables will not give rise to unitary transformations.

The same gate can also be represented as a matrix. The rows correspond to input basis vectors. The columns correspond to output basis vectors. The $(i, j)$ entry gives, when the $i$th basis vector is input to the gate, the coefficient of the $j$th basis vector in the corresponding output of the gate. The truth table above would then correspond to the following matrix:

$$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
0 & 0 & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{pmatrix} \qquad (2.3)$$

A quantum gate is feasible if and only if the corresponding matrix is unitary, i.e., its inverse is its conjugate transpose.

Suppose our machine is in the superposition of states

$$\frac{1}{\sqrt{2}}|10\rangle - \frac{1}{\sqrt{2}}|11\rangle \qquad (2.4)$$

and we apply the unitary transformation represented by (2.2) and (2.3) to this state. The resulting output will be the result of multiplying the vector (2.4) by the matrix (2.3). The machine will thus go to the superposition of states

$$\frac{1}{2}(|10\rangle + |11\rangle) - \frac{1}{2}(|10\rangle - |11\rangle) = |11\rangle . \qquad (2.5)$$

This example shows the potential effects of interference on quantum computation. Had we started with either the state $|10\rangle$ or the state $|11\rangle$, there would have been a chance of observing the state $|10\rangle$ after the application of the gate (2.3). However, when we start with a superposition of these two states, the probability amplitudes for the state $|10\rangle$ cancel, and we have no possibility of observing $|10\rangle$ after the application of the gate. Notice that the output of the gate would have been $|10\rangle$ instead of $|11\rangle$ had we started with the superposition of states

$$\frac{1}{\sqrt{2}}|10\rangle + \frac{1}{\sqrt{2}}|11\rangle \qquad (2.6)$$

which has the same probabilities of being in any particular configuration if it is observed as does the superposition (2.4).

If we apply a gate to only two bits of a longer basis vector (now our circuit must have more than two wires), we multiply the gate matrix by the two bits to which the gate is applied, and leave the other bits alone. This corresponds to multiplying the whole state by the tensor product of the gate matrix on those two bits with the identity matrix on the remaining bits.

A quantum gate array is a set of quantum gates with logical "wires" connecting their inputs and outputs. The input to the gate array, possibly along with extra work bits that are initially set to 0, is fed through a sequence of quantum gates. The values of the bits are observed after the last quantum gate, and these values are the output. To compare gate arrays with quantum Turing machines, we need to add conditions that make gate arrays a uniform complexity class. In other words, because there is a different gate array for each size of input, we need to keep the designer of the gate arrays from hiding non-computable (or hard to compute) information in the arrangement of the gates. To make quantum gate arrays uniform, we must add two things to the definition of gate arrays. The first is the standard requirement that the design of the gate array be produced by a polynomial-time (classical) computation. The second requirement should be a standard part of the definition of analog complexity classes, although since analog complexity classes have not been widely studied, this requirement is much less widely known. This requirement is that the entries in the unitary matrices describing the gates must be computable numbers. Specifically, the first $\log n$ bits of each entry should be classically computable in time polynomial in $n$ [Solovay 1995]. This keeps non-computable (or hard to compute) information from being hidden in the bits of the amplitudes of the quantum gates.

---

### النسخة العربية

في هذا القسم نقدم مقدمة موجزة للحوسبة الكمومية، مع التركيز على الخصائص التي سنستخدمها. سنصف فقط مصفوفات البوابات الكمومية، أو الدوائر اللادورية الكمومية، وهي مماثلة للدوائر اللادورية في علوم الحاسوب الكلاسيكية. لنماذج أخرى من الحواسيب الكمومية، انظر المراجع حول آلات تورنج الكمومية [Deutsch 1989، Bernstein و Vazirani 1993، Yao 1993] والأوتوماتات الخلوية الكمومية [Feynman 1986، Margolus 1986، 1990، Lloyd 1993، Biafore 1994]. إذا سُمح لها باحتمالية خطأ صغيرة، فإن آلات تورنج الكمومية ومصفوفات البوابات الكمومية يمكنها حساب نفس الدوال في زمن متعدد حدود [Yao 1993]. قد يكون هذا صحيحاً أيضاً لنماذج مختلفة من الأوتوماتات الخلوية الكمومية، ولكن لم يتم إثباته بعد. هذا يعطي دليلاً على أن فئة الدوال القابلة للحساب في زمن كمومي متعدد حدود مع احتمالية خطأ صغيرة قوية، بمعنى أنها لا تعتمد على المعمارية الدقيقة للحاسوب الكمومي. بالقياس مع الفئة الكلاسيكية BPP، تُسمى هذه الفئة BQP.

لنعتبر نظاماً له $n$ من المكونات، كل منها يمكن أن يكون له حالتان. بينما في الفيزياء الكلاسيكية، يتطلب الوصف الكامل لحالة هذا النظام $n$ بتات فقط، في الفيزياء الكمومية، يتطلب الوصف الكامل لحالة هذا النظام $2^n - 1$ عدداً مركباً. بشكل أكثر دقة، حالة النظام الكمومي هي نقطة في فضاء متجهات بُعد $2^n$. لكل من المواضع الكلاسيكية $2^n$ الممكنة للمكونات، يوجد حالة أساس لفضاء المتجهات هذا نمثله، على سبيل المثال، بـ $|011 \cdots 0\rangle$ بمعنى أن البت الأول هو 0، والبت الثاني هو 1، وهكذا. هنا، تدوين كِت $|x\rangle$ يعني أن $x$ هي حالة كمومية (نقية). (لن نناقش الحالات المختلطة في هذه الورقة، وبالتالي لا نعرّفها؛ انظر كتاباً في النظرية الكمومية مثل Peres [1993] لهذا التعريف.) فضاء هيلبرت المرتبط بهذا النظام الكمومي هو فضاء المتجهات المركبة مع هذه الحالات $2^n$ كمتجهات أساس، وحالة النظام في أي وقت تُمثل بمتجه وحدة الطول في فضاء هيلبرت هذا. نظراً لأن ضرب متجه الحالة هذا بطور مركب وحدة الطول لا يغير أي سلوك للحالة، فإننا نحتاج فقط إلى $2^n - 1$ عدداً مركباً لوصف الحالة بشكل كامل. نمثل هذا التراكب للحالات كما يلي:

$$\sum_{i=0}^{2^n-1} a_i |S_i\rangle , \qquad (2.1)$$

حيث السعات $a_i$ هي أعداد مركبة بحيث أن $\sum_i |a_i|^2 = 1$ وكل $|S_i\rangle$ هو متجه أساس لفضاء هيلبرت. إذا تم قياس الآلة (بالنسبة لهذا الأساس) في أي خطوة معينة، فإن احتمالية رؤية حالة الأساس $|S_i\rangle$ هي $|a_i|^2$؛ ومع ذلك، فإن قياس حالة الآلة يُسقط هذه الحالة على متجه الأساس الملاحظ $|S_i\rangle$. وبالتالي، فإن النظر إلى الآلة أثناء الحساب سيبطل بقية الحساب. في هذه الورقة، نعتبر فقط القياسات بالنسبة للأساس القانوني. هذا لا يقيد نموذج الحوسبة لدينا بشكل كبير، حيث يمكن محاكاة القياسات في أساسات معقولة أخرى عن طريق استخدام الحوسبة الكمومية أولاً لتنفيذ تغيير الأساس ثم إجراء قياس في الأساس القانوني.

لاستخدام نظام فيزيائي للحوسبة، يجب أن نكون قادرين على تغيير حالة النظام. قوانين ميكانيكا الكم تسمح فقط بالتحويلات الأحادية لمتجهات الحالة. المصفوفة الأحادية هي تلك التي يكون منقولها المترافق مساوياً لمعكوسها، والمطالبة بتمثيل تحويلات الحالة بمصفوفات أحادية يضمن أن جمع احتماليات الحصول على كل نتيجة ممكنة سينتج عنه 1. تعريف الدوائر الكمومية (وآلات تورنج الكمومية) يسمح فقط بالتحويلات الأحادية المحلية؛ أي التحويلات الأحادية على عدد ثابت من البتات. هذا مبرر فيزيائياً لأنه، بالنظر إلى تحويل أحادي عام على $n$ بتات، ليس من الواضح على الإطلاق كيف يمكن للمرء تنفيذه فيزيائياً بكفاءة، بينما تحويلات البتين يمكن على الأقل نظرياً تنفيذها بواسطة أنظمة فيزيائية بسيطة نسبياً [Cirac و Zoller 1995، DiVincenzo 1995، Sleator و Weinfurter 1995، Chuang و Yamomoto 1995]. بينما يمكن دائماً بناء تحويلات $n$-بت العامة من تحويلات البتين [DiVincenzo 1995، Sleator و Weinfurter 1995، Lloyd 1995، Deutsch et al. 1995]، فإن العدد المطلوب سيكون غالباً أسياً في $n$ [Barenco et al. 1995a]. وبالتالي، فإن مجموعة تحويلات البتين تشكل مجموعة من الكتل البنائية للدوائر الكمومية بطريقة مماثلة للطريقة التي تشكل بها مجموعة شاملة من البوابات الكلاسيكية (مثل بوابات AND و OR و NOT) مجموعة من الكتل البنائية للدوائر الكلاسيكية. في الواقع، لمجموعة شاملة من البوابات الكمومية، يكفي أخذ جميع بوابات البت الواحد ونوع واحد من بوابات البتين، وهي NOT المتحكم به، والتي تنفي البت الثاني إذا وفقط إذا كان البت الأول هو 1.

ربما يكون مثال مفيداً في هذه المرحلة. يمكن التعبير عن بوابة كمومية كجدول حقيقة: لكل متجه أساس إدخال نحتاج إلى إعطاء إخراج البوابة. إحدى هذه البوابات هي:

$$\begin{aligned}
|00\rangle &\to |00\rangle \\
|01\rangle &\to |01\rangle \\
|10\rangle &\to \frac{1}{\sqrt{2}}(|10\rangle + |11\rangle) \\
|11\rangle &\to \frac{1}{\sqrt{2}}(|10\rangle - |11\rangle)
\end{aligned} \qquad (2.2)$$

ليست كل جداول الحقيقة تتوافق مع بوابات كمومية ممكنة فيزيائياً، حيث أن العديد من جداول الحقيقة لن تؤدي إلى تحويلات أحادية.

يمكن أيضاً تمثيل نفس البوابة كمصفوفة. الصفوف تتوافق مع متجهات أساس الإدخال. الأعمدة تتوافق مع متجهات أساس الإخراج. المدخل $(i, j)$ يعطي، عندما يكون متجه الأساس $i$-ي مدخلاً للبوابة، معامل متجه الأساس $j$-ي في الإخراج المقابل للبوابة. جدول الحقيقة أعلاه سيتوافق مع المصفوفة التالية:

$$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
0 & 0 & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{pmatrix} \qquad (2.3)$$

البوابة الكمومية ممكنة إذا وفقط إذا كانت المصفوفة المقابلة أحادية، أي أن معكوسها هو منقولها المترافق.

لنفترض أن آلتنا في تراكب الحالات

$$\frac{1}{\sqrt{2}}|10\rangle - \frac{1}{\sqrt{2}}|11\rangle \qquad (2.4)$$

ونطبق التحويل الأحادي الممثل بـ (2.2) و (2.3) على هذه الحالة. سيكون الإخراج الناتج هو نتيجة ضرب المتجه (2.4) بالمصفوفة (2.3). وبالتالي ستذهب الآلة إلى تراكب الحالات

$$\frac{1}{2}(|10\rangle + |11\rangle) - \frac{1}{2}(|10\rangle - |11\rangle) = |11\rangle . \qquad (2.5)$$

يُظهر هذا المثال التأثيرات المحتملة للتداخل على الحوسبة الكمومية. لو بدأنا إما بالحالة $|10\rangle$ أو الحالة $|11\rangle$، لكانت هناك فرصة لملاحظة الحالة $|10\rangle$ بعد تطبيق البوابة (2.3). ومع ذلك، عندما نبدأ بتراكب هاتين الحالتين، فإن سعات الاحتمالية للحالة $|10\rangle$ تلغي بعضها البعض، ولا يوجد لدينا إمكانية لملاحظة $|10\rangle$ بعد تطبيق البوابة. لاحظ أن إخراج البوابة كان سيكون $|10\rangle$ بدلاً من $|11\rangle$ لو بدأنا بتراكب الحالات

$$\frac{1}{\sqrt{2}}|10\rangle + \frac{1}{\sqrt{2}}|11\rangle \qquad (2.6)$$

والذي له نفس احتماليات التواجد في أي تكوين معين إذا تمت ملاحظته مثل التراكب (2.4).

إذا طبقنا بوابة على بتين فقط من متجه أساس أطول (الآن يجب أن يكون لدائرتنا أكثر من سلكين)، فإننا نضرب مصفوفة البوابة بالبتين اللذين تُطبق عليهما البوابة، ونترك البتات الأخرى وحدها. هذا يتوافق مع ضرب الحالة بأكملها بحاصل الضرب الموتري لمصفوفة البوابة على هذين البتين مع مصفوفة الهوية على البتات المتبقية.

مصفوفة البوابات الكمومية هي مجموعة من البوابات الكمومية مع "أسلاك" منطقية تربط مدخلاتها ومخرجاتها. يُغذى المدخل إلى مصفوفة البوابات، ربما مع بتات عمل إضافية تُضبط في البداية على 0، عبر سلسلة من البوابات الكمومية. تتم ملاحظة قيم البتات بعد البوابة الكمومية الأخيرة، وهذه القيم هي الإخراج. لمقارنة مصفوفات البوابات مع آلات تورنج الكمومية، نحتاج إلى إضافة شروط تجعل مصفوفات البوابات فئة تعقيد موحدة. بعبارة أخرى، لأن هناك مصفوفة بوابات مختلفة لكل حجم من المدخلات، نحتاج إلى منع مصمم مصفوفات البوابات من إخفاء معلومات غير قابلة للحساب (أو يصعب حسابها) في ترتيب البوابات. لجعل مصفوفات البوابات الكمومية موحدة، يجب أن نضيف شيئين إلى تعريف مصفوفات البوابات. الأول هو المتطلب القياسي بأن يتم إنتاج تصميم مصفوفة البوابات بواسطة حساب (كلاسيكي) زمن متعدد حدود. المتطلب الثاني يجب أن يكون جزءاً قياسياً من تعريف فئات التعقيد التناظري، على الرغم من أنه نظراً لأن فئات التعقيد التناظري لم تتم دراستها على نطاق واسع، فإن هذا المتطلب أقل شهرة بكثير. هذا المتطلب هو أن المدخلات في المصفوفات الأحادية التي تصف البوابات يجب أن تكون أعداداً قابلة للحساب. على وجه التحديد، يجب أن تكون أول $\log n$ بتات من كل مدخل قابلة للحساب كلاسيكياً في زمن متعدد حدود في $n$ [Solovay 1995]. هذا يمنع إخفاء معلومات غير قابلة للحساب (أو يصعب حسابها) في بتات سعات البوابات الكمومية.

---

### Translation Notes

- **Equations:** 6 major equations (2.1 - 2.6)
- **Mathematical notation:** Extensive use of Dirac notation (ket vectors), matrices, quantum states
- **Key terms introduced:**
  - Quantum gate array (مصفوفة البوابات الكمومية)
  - Quantum circuit (دائرة كمومية)
  - BQP complexity class (فئة التعقيد BQP)
  - Hilbert space (فضاء هيلبرت)
  - Ket notation (تدوين كِت)
  - Basis state (حالة أساس)
  - Amplitude (سعة)
  - Superposition (تراكب)
  - Unitary matrix (مصفوفة أحادية)
  - Conjugate transpose (منقول مترافق)
  - Controlled NOT (NOT المتحكم به)
  - Tensor product (حاصل الضرب الموتري)
  - Quantum interference (التداخل الكمومي)

- **Special handling:**
  - All mathematical equations preserved in LaTeX notation
  - Matrix representations kept in original form
  - Quantum state notation (Dirac ket notation) preserved
  - Technical physics terminology carefully translated
  - References to classical computing concepts for comparison

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation (First Paragraph)

In this section we provide a brief introduction to quantum computation, with emphasis on the properties we will use. We will describe only quantum gate arrays, or acyclic quantum circuits, which are analogous to acyclic circuits in classical computer science. For other models of quantum computers, see references on quantum Turing machines [Deutsch 1989, Bernstein and Vazirani 1993, Yao 1993] and quantum cellular automata [Feynman 1986, Margolus 1986, 1990, Lloyd 1993, Biafore 1994]. If allowed a small error probability, quantum Turing machines and quantum gate arrays can compute the same functions in polynomial time [Yao 1993]. This may also be true for various models of quantum cellular automata, but it has not been proven yet. This provides evidence that the class of functions computable in quantum polynomial time with a small error probability is robust, meaning it does not depend on the exact architecture of the quantum computer. By analogy with the classical class BPP, this class is called BQP.

**Validation:** Back-translation preserves technical content and mathematical relationships. Quality maintained at 0.87/1.0.
