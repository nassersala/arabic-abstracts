# Section 2: Fixed p Algorithm
## القسم 2: خوارزمية p الثابت

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** preprocessing, algorithm, MaxCut, graph, edge, vertex, operator, qubit, subgraph, eigenstate, bounded degree, classical computation

---

### English Version

We now explain how for fixed p we can do classical preprocessing and determine the angles γ and β that maximize $F_p(γ, β)$. This approach will work more generally but we illustrate it for a specific problem, MaxCut for graphs with bounded degree. The input is a graph with n vertices and an edge set $\{⟨jk⟩\}$ of size m. The goal is to find a string z that makes

$$C = \sum_{⟨jk⟩} C_{⟨jk⟩}$$

where

$$C_{⟨jk⟩} = \frac{1}{2}(-σ^z_j σ^z_k + 1)$$

as large as possible. Now

$$F_p(γ, β) = \sum_{⟨jk⟩} ⟨s|U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨jk⟩} U(B, β_p) \cdots U(C, γ_1)|s⟩$$

Consider the operator associated with edge $⟨jk⟩$

$$U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨jk⟩} U(B, β_p) \cdots U(C, γ_1)$$

This operator only involves qubits j and k and those qubits whose distance on the graph from j or k is less than or equal to p. To see this consider p = 1 where the previous expression is

$$U^†(C, γ_1) U^†(B, β_1) C_{⟨jk⟩} U(B, β_1) U(C, γ_1)$$

The factors in the operator $U(B, β_1)$ which do not involve qubits j or k commute through $C_{⟨jk⟩}$ and we get

$$U^†(C, γ_1) e^{iβ_1(σ^x_j + σ^x_k)} C_{⟨jk⟩} e^{-iβ_1(σ^x_j + σ^x_k)} U(C, γ_1)$$

Any factors in the operator $U(C, γ_1)$ which do not involve qubits j or k will commute through and cancel out. So the operator in equation (16) only involves the edge $⟨jk⟩$ and edges adjacent to $⟨jk⟩$, and qubits on those edges. For any p we see that the operator in (14) only involves edges at most p steps away from $⟨jk⟩$ and qubits on those edges.

Return to equation (13) and note that the state $|s⟩$ is the product of $σ^x$ eigenstates

$$|s⟩ = |+⟩_1 |+⟩_2 \ldots |+⟩_n$$

so each term in equation (13) depends only on the subgraph involving qubits j and k and those at a distance no more than p away. These subgraphs each contain a number of qubits that is independent of n (because the degree is bounded) and this allows us to evaluate $F_p$ in terms of quantum subsystems whose sizes are independent of n.

As an illustration consider MaxCut restricted to input graphs of fixed degree 3. For p = 1, there are only these possible subgraphs for the edge $⟨jk⟩$:

[Three subgraph diagrams showing different configurations of vertices j and k with their neighbors]

We will return to this case later.

For any subgraph G define the operator $C_G$ which is C restricted to G,

$$C_G = \sum_{⟨ℓℓ'⟩ ∈ G} C_{⟨ℓℓ'⟩}$$

and the associated operator

$$U(C_G, γ) = e^{-iγC_G}$$

Also define

$$B_G = \sum_{j ∈ G} σ^x_j$$

and

$$U(B_G, β) = e^{-iβB_G}$$

Let the state $|s, G⟩$ be

$$|s, G⟩ = \prod_{ℓ ∈ G} |+⟩_ℓ$$

Return to equation (13). Each edge $⟨j, k⟩$ in the sum is associated with a subgraph $g(j, k)$ and makes a contribution to $F_p$ of

$$⟨s, g(j, k)|U^†(C_{g(j,k)}, γ_p) \cdots U^†(B_{g(j,k)}, β_1) C_{⟨jk⟩} U(B_{g(j,k)}, β_1) \cdots U(C_{g(j,k)}, γ_p)|s, g(j, k)⟩$$

The sum in (13) is over all edges, but if two edges $⟨jk⟩$ and $⟨j'k'⟩$ give rise to isomorphic subgraphs, then the corresponding functions of (γ, β) are the same. Therefore we can view the sum in (13) as a sum over subgraph types. Define

$$f_g(γ, β) = ⟨s, g(j, k)|U^†(C_{g(j,k)}, γ_1) \cdots U^†(B_{g(j,k)}, β_p) C_{⟨jk⟩} U(B_{g(j,k)}, β_p) \cdots U(C_{g(j,k)}, γ_1)|s, g(j, k)⟩$$

where $g(j, k)$ is a subgraph of type g. $F_p$ is then

$$F_p(γ, β) = \sum_g w_g f_g(γ, β)$$

where $w_g$ is the number of occurrences of the subgraph g in the original edge sum. The functions $f_g$ do not depend on n and m. The only dependence on n and m comes through the weights $w_g$ and these are just read off the original graph. Note that the expectation in (24) only involves the qubits in subgraph type g. The maximum number of qubits that can appear in (23) comes when the subgraph is a tree. For a graph with maximum degree v, the numbers of qubits in this tree is

$$q_{tree} = 2\left[\frac{(v-1)^{p+1} - 1}{(v-1) - 1}\right]$$

(or 2p + 2 if v = 2), which is n and m independent. For each p there are only finitely many subgraph types.

Using (24), $F_p(γ, β)$ in (25) can be evaluated on a classical computer whose resources are not growing with n. Each $f_g$ involves operators and states in a Hilbert space whose dimension is at most $2^{q_{tree}}$. Admittedly for large p this may be beyond current classical technology, but the resource requirements do not grow with n.

To run the quantum algorithm we first find the (γ, β) that maximize $F_p$. The only dependence on n and m is in the weights $w_g$ and these are easily evaluated. Given the best (γ, β) we turn to the quantum computer and produce the state $|γ, β⟩$ given in equation (6). We then measure in the computational basis and get a string z and evaluate C(z). Repeating gives a sample of values of C(z) between 0 and +m whose mean is $F_p(γ, β)$. An outcome of at least $F_p(γ, β) - 1$ will be obtained with probability $1 - 1/m$ with order $m \log m$ repetitions.

---

### النسخة العربية

نشرح الآن كيف يمكننا لقيمة p ثابتة إجراء معالجة مسبقة تقليدية وتحديد الزوايا γ و β التي تعظّم $F_p(γ, β)$. سيعمل هذا النهج بشكل أعم ولكننا نوضحه لمسألة محددة، وهي مسألة القطع الأعظمي للرسوم البيانية ذات الدرجة المحدودة. المدخل هو رسم بياني بـ n رأساً ومجموعة حواف $\{⟨jk⟩\}$ بحجم m. الهدف هو إيجاد سلسلة z تجعل

$$C = \sum_{⟨jk⟩} C_{⟨jk⟩}$$

حيث

$$C_{⟨jk⟩} = \frac{1}{2}(-σ^z_j σ^z_k + 1)$$

أكبر ما يمكن. الآن

$$F_p(γ, β) = \sum_{⟨jk⟩} ⟨s|U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨jk⟩} U(B, β_p) \cdots U(C, γ_1)|s⟩$$

لنفكر في المؤثر المرتبط بالحافة $⟨jk⟩$:

$$U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨jk⟩} U(B, β_p) \cdots U(C, γ_1)$$

هذا المؤثر يشمل فقط الكيوبتات j و k وتلك الكيوبتات التي تكون مسافتها على الرسم البياني من j أو k أقل من أو تساوي p. لنرى ذلك، لنفكر في p = 1 حيث يكون التعبير السابق:

$$U^†(C, γ_1) U^†(B, β_1) C_{⟨jk⟩} U(B, β_1) U(C, γ_1)$$

العوامل في المؤثر $U(B, β_1)$ التي لا تشمل الكيوبتات j أو k تتبادل عبر $C_{⟨jk⟩}$ ونحصل على:

$$U^†(C, γ_1) e^{iβ_1(σ^x_j + σ^x_k)} C_{⟨jk⟩} e^{-iβ_1(σ^x_j + σ^x_k)} U(C, γ_1)$$

أي عوامل في المؤثر $U(C, γ_1)$ التي لا تشمل الكيوبتات j أو k ستتبادل وتُلغى. لذلك المؤثر في المعادلة (16) يشمل فقط الحافة $⟨jk⟩$ والحواف المجاورة لـ $⟨jk⟩$، والكيوبتات على تلك الحواف. لأي p نرى أن المؤثر في (14) يشمل فقط الحواف التي تبعد على الأكثر p خطوات عن $⟨jk⟩$ والكيوبتات على تلك الحواف.

لنعد إلى المعادلة (13) ولنلاحظ أن الحالة $|s⟩$ هي جداء حالات $σ^x$ الذاتية:

$$|s⟩ = |+⟩_1 |+⟩_2 \ldots |+⟩_n$$

لذلك كل حد في المعادلة (13) يعتمد فقط على الرسم البياني الفرعي الذي يشمل الكيوبتات j و k وتلك التي على مسافة لا تزيد عن p. تحتوي هذه الرسوم البيانية الفرعية كل منها على عدد من الكيوبتات مستقل عن n (لأن الدرجة محدودة) وهذا يسمح لنا بحساب $F_p$ من حيث أنظمة كمومية فرعية أحجامها مستقلة عن n.

كتوضيح، لنفكر في مسألة القطع الأعظمي المقيدة بالرسوم البيانية المدخلة ذات الدرجة الثابتة 3. لـ p = 1، هناك فقط هذه الرسوم البيانية الفرعية الممكنة للحافة $⟨jk⟩$:

[ثلاثة مخططات للرسوم البيانية الفرعية تظهر تكوينات مختلفة للرؤوس j و k مع جيرانها]

سنعود إلى هذه الحالة لاحقاً.

لأي رسم بياني فرعي G، نعرّف المؤثر $C_G$ الذي هو C مقيداً بـ G:

$$C_G = \sum_{⟨ℓℓ'⟩ ∈ G} C_{⟨ℓℓ'⟩}$$

والمؤثر المرتبط:

$$U(C_G, γ) = e^{-iγC_G}$$

ونعرّف أيضاً:

$$B_G = \sum_{j ∈ G} σ^x_j$$

و

$$U(B_G, β) = e^{-iβB_G}$$

لتكن الحالة $|s, G⟩$ هي:

$$|s, G⟩ = \prod_{ℓ ∈ G} |+⟩_ℓ$$

لنعد إلى المعادلة (13). كل حافة $⟨j, k⟩$ في المجموع مرتبطة برسم بياني فرعي $g(j, k)$ وتقدم مساهمة في $F_p$ قدرها:

$$⟨s, g(j, k)|U^†(C_{g(j,k)}, γ_p) \cdots U^†(B_{g(j,k)}, β_1) C_{⟨jk⟩} U(B_{g(j,k)}, β_1) \cdots U(C_{g(j,k)}, γ_p)|s, g(j, k)⟩$$

المجموع في (13) على جميع الحواف، لكن إذا أعطت حافتان $⟨jk⟩$ و $⟨j'k'⟩$ رسوماً بيانية فرعية متشاكلة، فإن الدوال المقابلة لـ (γ, β) هي نفسها. لذلك يمكننا اعتبار المجموع في (13) مجموعاً على أنواع الرسوم البيانية الفرعية. نعرّف:

$$f_g(γ, β) = ⟨s, g(j, k)|U^†(C_{g(j,k)}, γ_1) \cdots U^†(B_{g(j,k)}, β_p) C_{⟨jk⟩} U(B_{g(j,k)}, β_p) \cdots U(C_{g(j,k)}, γ_1)|s, g(j, k)⟩$$

حيث $g(j, k)$ هو رسم بياني فرعي من النوع g. يكون $F_p$ حينئذٍ:

$$F_p(γ, β) = \sum_g w_g f_g(γ, β)$$

حيث $w_g$ هو عدد ظهورات الرسم البياني الفرعي g في مجموع الحواف الأصلي. الدوال $f_g$ لا تعتمد على n و m. الاعتماد الوحيد على n و m يأتي من خلال الأوزان $w_g$ وهذه تُقرأ مباشرة من الرسم البياني الأصلي. لاحظ أن التوقع في (24) يشمل فقط الكيوبتات في نوع الرسم البياني الفرعي g. العدد الأقصى من الكيوبتات التي يمكن أن تظهر في (23) يأتي عندما يكون الرسم البياني الفرعي شجرة. لرسم بياني بدرجة قصوى v، فإن عدد الكيوبتات في هذه الشجرة هو:

$$q_{tree} = 2\left[\frac{(v-1)^{p+1} - 1}{(v-1) - 1}\right]$$

(أو 2p + 2 إذا كان v = 2)، وهو مستقل عن n و m. لكل p يوجد عدد منتهٍ فقط من أنواع الرسوم البيانية الفرعية.

باستخدام (24)، يمكن حساب $F_p(γ, β)$ في (25) على حاسوب تقليدي لا تنمو موارده مع n. كل $f_g$ يشمل مؤثرات وحالات في فضاء هيلبرت بُعده على الأكثر $2^{q_{tree}}$. صحيح أنه لقيم p كبيرة قد يكون هذا خارج التكنولوجيا التقليدية الحالية، لكن متطلبات الموارد لا تنمو مع n.

لتشغيل الخوارزمية الكمومية، نجد أولاً (γ, β) التي تعظّم $F_p$. الاعتماد الوحيد على n و m هو في الأوزان $w_g$ وهذه يسهل حسابها. بإعطاء أفضل (γ, β) ننتقل إلى الحاسوب الكمومي وننتج الحالة $|γ, β⟩$ المعطاة في المعادلة (6). ثم نقيس في الأساس الحسابي ونحصل على سلسلة z ونحسب C(z). التكرار يعطي عينة من قيم C(z) بين 0 و +m متوسطها $F_p(γ, β)$. سيتم الحصول على نتيجة على الأقل $F_p(γ, β) - 1$ باحتمالية $1 - 1/m$ مع تكرارات من رتبة $m \log m$.

---

### Translation Notes

- **Figures referenced:** Subgraph diagrams (18) showing three possible configurations for degree-3 graphs
- **Key terms introduced:** bounded degree (الدرجة المحدودة), subgraph (رسم بياني فرعي), isomorphic (متشاكلة), qubit (كيوبت)
- **Equations:** 17 mathematical equations preserved in LaTeX format
- **Citations:** References to equations from previous section
- **Special handling:** Graph theory terminology; quantum state notation; classical preprocessing concept

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
