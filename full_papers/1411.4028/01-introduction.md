# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** combinatorial, optimization, objective function, algorithm, quantum circuit, unitary gate, locality, circuit depth, constraint, computational basis, operator, eigenvalue, Hilbert space

---

### English Version

Combinatorial optimization problems are specified by n bits and m clauses. Each clause is a constraint on a subset of the bits which is satisfied for certain assignments of those bits and unsatisfied for the other assignments. The objective function, defined on n bit strings, is the number of satisfied clauses,

$$C(z) = \sum_{α=1}^{m} C_α(z)$$

where $z = z_1z_2 \ldots z_n$ is the bit string and $C_α(z) = 1$ if z satisfies clause α and 0 otherwise. Typically $C_α$ depends on only a few of the n bits. Satisfiability asks if there is a string that satisfies every clause. MaxSat asks for a string that maximizes the objective function. Approximate optimization asks for a string z for which C(z) is close to the maximum of C.

In this paper we present a general quantum algorithm for approximate optimization. We study its performance in special cases of MaxCut and also propose an alternate form of the algorithm geared toward finding a large independent set of vertices of a graph.

The quantum computer works in a $2^n$ dimensional Hilbert space with computational basis vectors $|z\rangle$, and we view (1) as an operator which is diagonal in the computational basis. Define a unitary operator $U(C, γ)$ which depends on an angle γ,

$$U(C, γ) = e^{-iγC} = \prod_{α=1}^{m} e^{-iγC_α}$$

All of the terms in this product commute because they are diagonal in the computational basis and each term's locality is the locality of the clause α. Because C has integer eigenvalues we can restrict γ to lie between 0 and 2π. Define the operator B which is the sum of all single bit $σ^x$ operators,

$$B = \sum_{j=1}^{n} σ^x_j$$

Now define the β dependent product of commuting one bit operators

$$U(B, β) = e^{-iβB} = \prod_{j=1}^{n} e^{-iβσ^x_j}$$

where β runs from 0 to π. The initial state $|s\rangle$ will be the uniform superposition over computational basis states:

$$|s\rangle = \frac{1}{\sqrt{2^n}} \sum_z |z\rangle$$

For any integer $p \geq 1$ and 2p angles $γ_1 \ldots γ_p \equiv γ$ and $β_1 \ldots β_p \equiv β$ we define the angle dependent quantum state:

$$|γ, β\rangle = U(B, β_p) U(C, γ_p) \cdots U(B, β_1) U(C, γ_1) |s\rangle$$

Even without taking advantage of the structure of the instance, this state can be produced by a quantum circuit of depth at most $mp + p$. Let $F_p$ be the expectation of C in this state

$$F_p(γ, β) = \langle γ, β| C |γ, β\rangle$$

and let $M_p$ be the maximum of $F_p$ over the angles,

$$M_p = \max_{γ,β} F_p(γ, β)$$

Note that the maximization at p − 1 can be viewed as a constrained maximization at p so

$$M_p \geq M_{p-1}$$

Furthermore we will later show that

$$\lim_{p→∞} M_p = \max_z C(z)$$

These results suggest a way to design an algorithm. Pick a p and start with a set of angles (γ, β) that somehow make $F_p$ as large as possible. Use the quantum computer to get the state $|γ, β\rangle$. Measure in the computational basis to get a string z and evaluate C(z). Repeat with the same angles. Enough repetitions will produce a string z with C(z) very near or greater than $F_p(γ, β)$. The rub is that it is not obvious in advance how to pick good angles.

If p doesn't grow with n, one possibility is to run the quantum computer with angles (γ, β) chosen from a fine grid on the compact set $[0, 2π]^p × [0, π]^p$, moving through the grid to find the maximum of $F_p$. Since the partial derivatives of $F_p(γ, β)$ in (7) are bounded by $O(m^2 + mn)$ this search will efficiently produce a string z for which C(z) is close to $M_p$ or larger. However we show in the next section that if p does not grow with n and each bit is involved in no more than a fixed number of clauses, then there is an efficient classical calculation that determines the angles that maximize $F_p$. These angles are then used to run the quantum computer to produce the state $|γ, β\rangle$ which is measured in the computational basis to get a string z. The mean of C(z) for strings obtained in this way is $M_p$.

---

### النسخة العربية

تُحدَّد مسائل التحسين التجميعي بواسطة n بت و m جملة. كل جملة هي قيد على مجموعة فرعية من البتات يتم تحقيقه لتعيينات معينة لتلك البتات ولا يتحقق للتعيينات الأخرى. الدالة الهدفية، المعرَّفة على سلاسل n بت، هي عدد الجمل المحققة:

$$C(z) = \sum_{α=1}^{m} C_α(z)$$

حيث $z = z_1z_2 \ldots z_n$ هي سلسلة البتات و $C_α(z) = 1$ إذا كانت z تحقق الجملة α و 0 بخلاف ذلك. عادةً تعتمد $C_α$ على عدد قليل فقط من البتات n. تسأل مسألة الإرضاء إذا كانت هناك سلسلة تحقق كل جملة. تطلب مسألة MaxSat سلسلة تعظّم الدالة الهدفية. يطلب التحسين التقريبي سلسلة z بحيث يكون C(z) قريباً من القيمة العظمى لـ C.

في هذا البحث نقدم خوارزمية كمومية عامة للتحسين التقريبي. ندرس أداءها في حالات خاصة من مسألة القطع الأعظمي ونقترح أيضاً شكلاً بديلاً للخوارزمية موجهاً نحو إيجاد مجموعة مستقلة كبيرة من رؤوس رسم بياني.

يعمل الحاسوب الكمومي في فضاء هيلبرت ذي $2^n$ بُعد مع متجهات الأساس الحسابي $|z\rangle$، ونعتبر (1) مؤثراً قطرياً في الأساس الحسابي. نعرّف مؤثراً وحدوياً $U(C, γ)$ يعتمد على زاوية γ:

$$U(C, γ) = e^{-iγC} = \prod_{α=1}^{m} e^{-iγC_α}$$

جميع الحدود في هذا الجداء تبادلية لأنها قطرية في الأساس الحسابي وموضعية كل حد هي موضعية الجملة α. لأن C له قيم ذاتية صحيحة يمكننا تقييد γ لتكون بين 0 و 2π. نعرّف المؤثر B الذي هو مجموع جميع مؤثرات $σ^x$ أحادية البت:

$$B = \sum_{j=1}^{n} σ^x_j$$

الآن نعرّف جداء المؤثرات أحادية البت المتبادلة المعتمدة على β:

$$U(B, β) = e^{-iβB} = \prod_{j=1}^{n} e^{-iβσ^x_j}$$

حيث تتراوح β من 0 إلى π. الحالة الابتدائية $|s\rangle$ ستكون التراكب الموحد على حالات الأساس الحسابي:

$$|s\rangle = \frac{1}{\sqrt{2^n}} \sum_z |z\rangle$$

لأي عدد صحيح $p \geq 1$ و 2p زاوية $γ_1 \ldots γ_p \equiv γ$ و $β_1 \ldots β_p \equiv β$ نعرّف الحالة الكمومية المعتمدة على الزوايا:

$$|γ, β\rangle = U(B, β_p) U(C, γ_p) \cdots U(B, β_1) U(C, γ_1) |s\rangle$$

حتى دون الاستفادة من بنية المسألة، يمكن إنتاج هذه الحالة بواسطة دائرة كمومية بعمق على الأكثر $mp + p$. ليكن $F_p$ التوقع لـ C في هذه الحالة:

$$F_p(γ, β) = \langle γ, β| C |γ, β\rangle$$

وليكن $M_p$ القيمة العظمى لـ $F_p$ على الزوايا:

$$M_p = \max_{γ,β} F_p(γ, β)$$

لاحظ أن التعظيم عند p − 1 يمكن اعتباره تعظيماً مقيداً عند p لذلك:

$$M_p \geq M_{p-1}$$

علاوة على ذلك، سنبيّن لاحقاً أن:

$$\lim_{p→∞} M_p = \max_z C(z)$$

تقترح هذه النتائج طريقة لتصميم خوارزمية. اختر p وابدأ بمجموعة من الزوايا (γ, β) التي تجعل $F_p$ كبيراً قدر الإمكان بطريقة ما. استخدم الحاسوب الكمومي للحصول على الحالة $|γ, β\rangle$. قِس في الأساس الحسابي للحصول على سلسلة z واحسب C(z). كرر باستخدام نفس الزوايا. ستنتج تكرارات كافية سلسلة z بحيث يكون C(z) قريباً جداً من أو أكبر من $F_p(γ, β)$. المشكلة هي أنه ليس واضحاً مسبقاً كيفية اختيار زوايا جيدة.

إذا لم ينمُ p مع n، فإحدى الإمكانيات هي تشغيل الحاسوب الكمومي بزوايا (γ, β) مختارة من شبكة دقيقة على المجموعة المدمجة $[0, 2π]^p × [0, π]^p$، والتحرك عبر الشبكة لإيجاد القيمة العظمى لـ $F_p$. بما أن المشتقات الجزئية لـ $F_p(γ, β)$ في (7) محدودة بـ $O(m^2 + mn)$، فإن هذا البحث سينتج بكفاءة سلسلة z بحيث يكون C(z) قريباً من $M_p$ أو أكبر. لكننا نبيّن في القسم التالي أنه إذا لم ينمُ p مع n وكان كل بت متضمناً في ما لا يزيد عن عدد ثابت من الجمل، فإن هناك حساباً تقليدياً فعالاً يحدد الزوايا التي تعظّم $F_p$. تُستخدم هذه الزوايا بعد ذلك لتشغيل الحاسوب الكمومي لإنتاج الحالة $|γ, β\rangle$ التي تُقاس في الأساس الحسابي للحصول على سلسلة z. متوسط C(z) للسلاسل المحصلة بهذه الطريقة هو $M_p$.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** clause (جملة), satisfiability (الإرضاء), MaxSat, MaxCut (القطع الأعظمي), independent set (مجموعة مستقلة), uniform superposition (التراكب الموحد)
- **Equations:** 10 mathematical equations preserved in LaTeX format
- **Citations:** None in this section
- **Special handling:** Mathematical notation preserved; quantum computing terminology carefully translated using glossary

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
