# Section 7: A Variant of the Algorithm
## القسم 7: شكل بديل للخوارزمية

**Section:** methodology-variant
**Translation Quality:** 0.86
**Glossary Terms Used:** independent set, graph, vertex, Hamming weight, hypercube, adjacency matrix, quantum walk, subroutine

---

### English Version

We are now going to give a variant of the basic algorithm which is suited to situations where the search space is a complicated subset of the n bit strings. We work with an example that illustrates the basic idea. Consider the problem of finding a large independent set in a given graph of n vertices. An independent set is a subset of the vertices with the property that no two vertices in the subset have an edge between them. With the vertices labeled 1 to n, a subset of the vertices corresponds to the string $z = z_1z_2 \ldots z_n$ with each bit being 1 if the corresponding vertex is in the subset and the bit is 0 if the vertex is not. We restrict to strings which correspond to independent sets in the graph. The size of the independent set is the Hamming weight of the string z which we denote by C(z),

$$C(z) = \sum_{j=1}^{n} z_j$$

and the goal is to find a string z that makes C(z) large.

The Hilbert space for our quantum algorithm has an orthonormal basis $|z⟩$ where z is any string corresponding to an independent set. In cases of interest, the Hilbert space dimension is exponentially large in n, though not as big as $2^n$. The Hilbert space is not a simple tensor product of qubits. The operator C is associated with the γ dependent unitary

$$U(C, γ) = e^{-iγC}$$

where γ lies between 0 and 2π because C has integer eigenvalues. We define the quantum operator B that connects the basis states:

$$⟨z|B|z'⟩ = \begin{cases} 1 & : \text{z and z' differ in one bit} \\ 0 & : \text{otherwise} \end{cases}$$

Note that B is the adjacency matrix of the hypercube restricted to the legal strings, that is, those that correspond to independent sets in the given graph. Now, in general, B does not have integer eigenvalues so we define

$$U(B, b) = e^{-ibB}$$

where b is a real number.

For the starting state of our algorithm we take the easy to construct state $|z = 0⟩$ corresponding to the empty independent set which has the minimum value of C. For $p \geq 1$, we have p real numbers $b_1, b_2 \ldots b_p \equiv \mathbf{b}$ and $p - 1$ angles $γ_1, γ_2, \ldots γ_{p-1} \equiv γ$. The quantum state

$$|\mathbf{b}, γ⟩ = U(B, b_p)U(C, γ_{p-1}) \cdots U(B, b_1)|z = 0⟩$$

is what we get after the application of an alternation of the operators associated with B and C. Now we can define

$$F_p(\mathbf{b}, γ) = ⟨\mathbf{b}, γ|C|\mathbf{b}, γ⟩$$

as the expectation of C in the state $|\mathbf{b}, γ⟩$. And finally we define the maximum,

$$M_p = \max_{\mathbf{b},γ} F_p(\mathbf{b}, γ)$$

The maximization at $p - 1$ is the maximization at p with $b_p = 0$ and $γ_{p-1} = 0$ so we have

$$M_p \geq M_{p-1}$$

Furthermore,

$$\lim_{p→∞} M_p = \max_{z \text{ legal}} C(z)$$

To see why (45) is true note that the initial state is the ground state of C, which we view as the state with the maximum eigenvalue of −C. We are trying to reach a state which is an eigenstate of +C with maximum eigenvalue. There is an adiabatic path (which stays at the top of the spectrum throughout) with run time T that achieves this as T goes to infinity. This path has two parts. In the first we interpolate between the beginning Hamiltonian −C and the Hamiltonian B,

$$H(t) = \left(1 - \frac{2t}{T}\right)(-C) + \frac{2t}{T}B, \quad 0 \leq t \leq \frac{T}{2}$$

We evolve the initial state with this Hamiltonian for time T/2 ending arbitrarily close to the top state of B. Next we interpolate between the Hamiltonian B and the Hamiltonian +C,

$$H(t) = \left(2 - \frac{2t}{T}\right)B + \left(\frac{2t}{T} - 1\right)C, \quad \frac{T}{2} \leq t \leq T$$

evolving the quantum state just produced from time $t = T/2$ to $t = T$. As in section VI, using the Perron-Frobenius Theorem, the Adiabatic Theorem and Trotterization we get the result given in (45).

Together (41) through (45) suggest a quantum subroutine for an independent set algorithm. For a given p and a given $(\mathbf{b}, γ)$ produce the quantum state $|\mathbf{b}, γ⟩$ of (41). Measure in the computational basis to get a string z which labels an independent set whose size is the Hamming weight of z. Repeat with the same $(\mathbf{b}, γ)$ to get an estimate of $F_p(\mathbf{b}, γ)$ in (42). This subroutine can be called by a program whose goal is to get close to $M_p$ given by (43). This enveloping program can be designed using either the methods outlined in this paper or novel techniques.

For p = 1, the subroutine can be thought of as evolving the initial state $|z = 0⟩$ with the Hamlitonian B for a time b. B is the adjacency matrix of a big graph whose vertices correspond to the independent sets of the input graph and whose edges can be read off (39). We view this as a continuous time quantum walk entering the big graph at a particular vertex [5]. In the extreme case where the input graph has no edges, all strings of length n represent independent sets so the Hilbert space dimension is $2^n$. In this case B is the adjacency matrix of the hypercube, realizable as in (3). Setting $b = π/2$, the state (41) (with p = 1 there is only one unitary) is $|z = 11 \ldots 11⟩$ which maximizes the objective function. In the more general case we can view (41) as a succession of quantum walks punctuated by applications of C dependent unitaries which aid the walk in achieving its objective. The algorithm of the previous sections can also be viewed this way although the starting state is not a single vertex.

---

### النسخة العربية

سنقدم الآن شكلاً بديلاً للخوارزمية الأساسية مناسباً للحالات التي يكون فيها فضاء البحث مجموعة فرعية معقدة من سلاسل n بت. نعمل مع مثال يوضح الفكرة الأساسية. لنفكر في مسألة إيجاد مجموعة مستقلة كبيرة في رسم بياني معطى بـ n رأساً. المجموعة المستقلة هي مجموعة فرعية من الرؤوس بخاصية أنه لا يوجد رأسان في المجموعة الفرعية بينهما حافة. مع ترقيم الرؤوس من 1 إلى n، تتوافق مجموعة فرعية من الرؤوس مع السلسلة $z = z_1z_2 \ldots z_n$ حيث كل بت يكون 1 إذا كان الرأس المقابل في المجموعة الفرعية والبت 0 إذا لم يكن الرأس فيها. نقيد السلاسل التي تتوافق مع مجموعات مستقلة في الرسم البياني. حجم المجموعة المستقلة هو وزن هامينج للسلسلة z الذي نرمز له بـ C(z):

$$C(z) = \sum_{j=1}^{n} z_j$$

والهدف هو إيجاد سلسلة z تجعل C(z) كبيرة.

فضاء هيلبرت لخوارزميتنا الكمومية له أساس متعامد متعامد $|z⟩$ حيث z هي أي سلسلة تتوافق مع مجموعة مستقلة. في الحالات محل الاهتمام، يكون بُعد فضاء هيلبرت كبيراً أسياً في n، رغم أنه ليس كبيراً مثل $2^n$. فضاء هيلبرت ليس جداء تنسوري بسيط للكيوبتات. المؤثر C مرتبط بالمؤثر الوحدوي المعتمد على γ:

$$U(C, γ) = e^{-iγC}$$

حيث γ تقع بين 0 و 2π لأن C له قيم ذاتية صحيحة. نعرّف المؤثر الكمومي B الذي يربط حالات الأساس:

$$⟨z|B|z'⟩ = \begin{cases} 1 & : \text{z و z' تختلفان في بت واحد} \\ 0 & : \text{بخلاف ذلك} \end{cases}$$

لاحظ أن B هي مصفوفة الجوار للمكعب الفائق مقيدة بالسلاسل القانونية، أي تلك التي تتوافق مع مجموعات مستقلة في الرسم البياني المعطى. الآن، بشكل عام، B ليس لها قيم ذاتية صحيحة لذا نعرّف:

$$U(B, b) = e^{-ibB}$$

حيث b عدد حقيقي.

للحالة البدائية لخوارزميتنا نأخذ الحالة السهلة البناء $|z = 0⟩$ المقابلة للمجموعة المستقلة الفارغة التي لها القيمة الدنيا لـ C. لـ $p \geq 1$، لدينا p أعداد حقيقية $b_1, b_2 \ldots b_p \equiv \mathbf{b}$ و $p - 1$ زاوية $γ_1, γ_2, \ldots γ_{p-1} \equiv γ$. الحالة الكمومية

$$|\mathbf{b}, γ⟩ = U(B, b_p)U(C, γ_{p-1}) \cdots U(B, b_1)|z = 0⟩$$

هي ما نحصل عليه بعد تطبيق تناوب المؤثرات المرتبطة بـ B و C. الآن يمكننا تعريف:

$$F_p(\mathbf{b}, γ) = ⟨\mathbf{b}, γ|C|\mathbf{b}, γ⟩$$

كتوقع C في الحالة $|\mathbf{b}, γ⟩$. وأخيراً نعرّف القيمة العظمى:

$$M_p = \max_{\mathbf{b},γ} F_p(\mathbf{b}, γ)$$

التعظيم عند $p - 1$ هو التعظيم عند p مع $b_p = 0$ و $γ_{p-1} = 0$ لذا لدينا:

$$M_p \geq M_{p-1}$$

علاوة على ذلك:

$$\lim_{p→∞} M_p = \max_{z \text{ قانونية}} C(z)$$

لنرى لماذا (45) صحيحة، لاحظ أن الحالة الابتدائية هي الحالة الأرضية لـ C، التي نعتبرها الحالة ذات القيمة الذاتية العظمى لـ −C. نحاول الوصول إلى حالة هي حالة ذاتية لـ +C بقيمة ذاتية عظمى. يوجد مسار أديباتي (يبقى في قمة الطيف طوال الوقت) بوقت تشغيل T يحقق هذا مع ذهاب T إلى ما لا نهاية. هذا المسار له جزءان. في الأول نستكمل بين الهاميلتونية البدائية −C والهاميلتونية B:

$$H(t) = \left(1 - \frac{2t}{T}\right)(-C) + \frac{2t}{T}B, \quad 0 \leq t \leq \frac{T}{2}$$

نطور الحالة الابتدائية بهذه الهاميلتونية للزمن T/2 منتهين قريبين تعسفياً من الحالة العليا لـ B. بعد ذلك نستكمل بين الهاميلتونية B والهاميلتونية +C:

$$H(t) = \left(2 - \frac{2t}{T}\right)B + \left(\frac{2t}{T} - 1\right)C, \quad \frac{T}{2} \leq t \leq T$$

مطورين الحالة الكمومية المنتجة للتو من الزمن $t = T/2$ إلى $t = T$. كما في القسم VI، باستخدام مبرهنة بيرون-فروبينيوس، والمبرهنة الأديباتية، والتروتر نحصل على النتيجة المعطاة في (45).

معاً، تقترح (41) خلال (45) برنامج فرعي كمومي لخوارزمية مجموعة مستقلة. لقيمة p معطاة و $(\mathbf{b}, γ)$ معطى، أنتِج الحالة الكمومية $|\mathbf{b}, γ⟩$ من (41). قِس في الأساس الحسابي للحصول على سلسلة z تُعنوِن مجموعة مستقلة حجمها هو وزن هامينج لـ z. كرر بنفس $(\mathbf{b}, γ)$ للحصول على تقدير لـ $F_p(\mathbf{b}, γ)$ في (42). يمكن استدعاء هذا البرنامج الفرعي بواسطة برنامج هدفه الاقتراب من $M_p$ المعطاة بـ (43). يمكن تصميم هذا البرنامج المُحيط باستخدام الطرق الموضحة في هذا البحث أو تقنيات جديدة.

لـ p = 1، يمكن اعتبار البرنامج الفرعي تطويراً للحالة الابتدائية $|z = 0⟩$ بالهاميلتونية B لزمن b. B هي مصفوفة الجوار لرسم بياني كبير رؤوسه تتوافق مع المجموعات المستقلة للرسم البياني المدخل وحوافه يمكن قراءتها من (39). نعتبر هذا مشياً كمومياً مستمر الزمن يدخل الرسم البياني الكبير عند رأس معين [5]. في الحالة القصوى حيث لا يكون للرسم البياني المدخل حواف، فإن جميع السلاسل بطول n تمثل مجموعات مستقلة لذا فإن بُعد فضاء هيلبرت هو $2^n$. في هذه الحالة B هي مصفوفة الجوار للمكعب الفائق، القابلة للتحقيق كما في (3). بتعيين $b = π/2$، فإن الحالة (41) (مع p = 1 يوجد مؤثر وحدوي واحد فقط) هي $|z = 11 \ldots 11⟩$ التي تعظّم الدالة الهدفية. في الحالة الأعم يمكننا اعتبار (41) تتابعاً من المشي الكمومي متقطعاً بتطبيقات للمؤثرات الوحدوية المعتمدة على C التي تساعد المشي في تحقيق هدفه. يمكن أيضاً اعتبار خوارزمية الأقسام السابقة بهذه الطريقة رغم أن الحالة البدائية ليست رأساً واحداً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** independent set (مجموعة مستقلة), Hamming weight (وزن هامينج), hypercube (المكعب الفائق), adjacency matrix (مصفوفة الجوار), quantum walk (مشي كمومي), subroutine (برنامج فرعي), legal strings (سلاسل قانونية)
- **Equations:** 9 mathematical equations
- **Citations:** Reference [5] on quantum walks
- **Special handling:** Variant algorithm formulation; independent set problem; continuous time quantum walk interpretation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
