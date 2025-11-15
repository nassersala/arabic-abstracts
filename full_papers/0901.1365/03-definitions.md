# Section 2: Definitions and Preliminaries
## القسم 2: التعريفات والمقدمات

**Section:** definitions
**Translation Quality:** 0.86
**Glossary Terms Used:** database, privacy, algorithm, differential privacy, distribution, probability measure, density function, randomized function, neighboring databases, Radon-Nikodym derivative

---

### English Version

For a database D, let A be a database access mechanism. We present non-interactive database privacy mechanisms, meaning that A(D) induces a distribution over sanitized output databases D'. We first recall the standard differential privacy definition from Dwork [7].

**Definition 2.1. (α-DIFFERENTIAL PRIVACY)** [7] A randomized function A gives α-differential privacy if for all data sets D₁ and D₂ differing on at most one element, and all S ⊆ Range(A), P[A(D₁) ∈ S] ≤ e^α P[A(D₂) ∈ S].

We now formalize our notation.

**Notation:** Let D be a collection of all records (potentially coming from some underlying distribution) and σ(D) represent the entire set of input databases with elements drawn from D. Let S_n = {X₁, X₂, ...} ⊂ σ(D), where X_i ∈ σ(D), ∀i, denote a set of databases, each with n elements drawn from D. Although differential privacy is defined with respect to all D, E ∈ σ(D), we constrain the definition of distributional privacy to the scope of S_n, which becomes clear in Definition 2.4. We let D' be the entire set of possible output databases.

**Definition 2.2.** A privacy algorithm A takes an input database D ∈ σ(D) and outputs a probability measure P_D on D', where D' is allowed to be different from σ(D). Let P denote all probability measures on D'. Then a privacy algorithm is a map A : σ(D) → P where A(D) = P_D, ∀D ∈ σ(D).

We now define differential privacy for continuous output. We introduce an additional parameter δ which measures how different two databases are according to V below.

**Definition 2.3.** Let V(D, E) be the distance between D and E according to a certain metric, which is related to the utility we aim to provide. Let d(D, E) denote the number of rows in which D and E differ. δ-constrained α-Differential ((α, δ)-Differential Privacy) requires the following condition,

sup_{D,E:d(D,E)=1,V(D,E)≤δ} Δ(P_D, P_E) ≤ e^α,                    (2)

where Δ(P, Q) = ess sup_{D∈D'} dP/dQ(D) denotes the essential supremum over D' for the Radon-Nikodym derivative dP/dQ.

Let S_n = {X₁, X₂, ...} be a set of databases of n records. Let Δ_max(S_n) bound the pairwise distance between X_i, X_j ∈ S_n, ∀i, j. We now introduce a notion of distributional privacy, that is similar in spirit to that in [3].

**Definition 2.4. (DISTRIBUTIONAL PRIVACY FOR CONTINUOUS OUTCOME)** An algorithm A satisfies (α, δ)-distributional privacy on S_n, for which a global parameter Δ_max(S_n) is specified, if for any two databases X₁, X₂ ∈ S_n such that each consists of n elements drawn from D, where X₁ ∩ X₂ may not be empty, and for all sanitized outputs X̄ ∈ D',

f_{X₁}(X̄) ≤ e^α f_{X₂}(X̄), ∀X₁, X₂ s.t. V(X₁, X₂) ≤ δ                    (3)

where f_{X_j}(·) is the density function for the conditional distribution with law L(·|X_j), ∀i given X_j.

Note that this composes nicely if one is considering databases that differ in multiple rows. In particular, randomness in X_j is not directly exploited in the definition as we treat elements in X_j ∈ σ(D) as fixed data. One could assume that they come from an underlying distribution, e.g., a multivariate Gaussian N(0, Σ*), and infer the distance between Σ_i and its population correspondent Σ*. We now show that distributional privacy is a stronger concept than differential privacy.

**Theorem 2.5.** Given S_n, if A satisfies (α, δ)-distributional privacy as in Definition 2.4 for all X_j ∈ S_n, then A satisfies (α, δ)-Differential Privacy as in Definition 2.3 for all X_j ∈ S.

**Proof.** For the same constraint parameter δ, if we guarantee that (3) is satisfied, for all X_i, X_j ∈ S_n that differ only in a single row such that V(X_i, X_j) ≤ δ, we have shown the α-differential privacy on S_n; clearly, this type of guarantee is necessary in order to guarantee α-distributional privacy over all X_i, X_j ∈ S_n that satisfy the δ constraint. □

---

### النسخة العربية

لقاعدة بيانات D، دع A تكون آلية للوصول إلى قاعدة البيانات. نقدم آليات خصوصية قاعدة بيانات غير تفاعلية، مما يعني أن A(D) يحفز توزيعًا على قواعد بيانات مخرجات معقمة D'. نتذكر أولاً تعريف الخصوصية التفاضلية القياسي من Dwork [7].

**التعريف 2.1. (الخصوصية التفاضلية α)** [7] دالة عشوائية A تعطي خصوصية تفاضلية α إذا كان لجميع مجموعات البيانات D₁ و D₂ التي تختلف في عنصر واحد على الأكثر، ولجميع S ⊆ Range(A)، P[A(D₁) ∈ S] ≤ e^α P[A(D₂) ∈ S].

نقوم الآن بإضفاء الطابع الرسمي على ترميزنا.

**الترميز:** دع D تكون مجموعة من جميع السجلات (التي قد تأتي من توزيع أساسي) و σ(D) تمثل المجموعة الكاملة لقواعد بيانات الإدخال مع عناصر مسحوبة من D. دع S_n = {X₁, X₂, ...} ⊂ σ(D)، حيث X_i ∈ σ(D)، ∀i، تشير إلى مجموعة من قواعد البيانات، كل منها يحتوي على n عنصرًا مسحوبًا من D. على الرغم من أن الخصوصية التفاضلية محددة فيما يتعلق بجميع D، E ∈ σ(D)، فإننا نقيد تعريف الخصوصية التوزيعية بنطاق S_n، وهو ما يصبح واضحًا في التعريف 2.4. ندع D' تكون المجموعة الكاملة من قواعد بيانات المخرجات الممكنة.

**التعريف 2.2.** خوارزمية خصوصية A تأخذ قاعدة بيانات إدخال D ∈ σ(D) وتخرج مقياس احتمال P_D على D'، حيث يُسمح لـ D' أن تكون مختلفة عن σ(D). دع P تشير إلى جميع مقاييس الاحتمال على D'. ثم خوارزمية الخصوصية هي تعيين A : σ(D) → P حيث A(D) = P_D، ∀D ∈ σ(D).

نحدد الآن الخصوصية التفاضلية للمخرجات المستمرة. نقدم معاملاً إضافيًا δ الذي يقيس مدى اختلاف قاعدتي بيانات وفقًا لـ V أدناه.

**التعريف 2.3.** دع V(D, E) تكون المسافة بين D و E وفقًا لمقياس معين، والذي يرتبط بالفائدة التي نهدف إلى توفيرها. دع d(D, E) يشير إلى عدد الصفوف التي تختلف فيها D و E. الخصوصية التفاضلية α المقيدة بـ δ (خصوصية تفاضلية (α، δ)) تتطلب الشرط التالي،

sup_{D,E:d(D,E)=1,V(D,E)≤δ} Δ(P_D, P_E) ≤ e^α,                    (2)

حيث Δ(P, Q) = ess sup_{D∈D'} dP/dQ(D) يشير إلى الحد الأعلى الأساسي على D' لمشتق رادون-نيكوديم dP/dQ.

دع S_n = {X₁, X₂, ...} تكون مجموعة من قواعد البيانات من n سجلات. دع Δ_max(S_n) يحد المسافة الزوجية بين X_i، X_j ∈ S_n، ∀i, j. نقدم الآن فكرة الخصوصية التوزيعية، التي تشبه في روحها تلك في [3].

**التعريف 2.4. (الخصوصية التوزيعية للنتائج المستمرة)** خوارزمية A تحقق خصوصية توزيعية (α، δ) على S_n، والتي يتم تحديد معامل عام Δ_max(S_n) لها، إذا كان لأي قاعدتي بيانات X₁، X₂ ∈ S_n بحيث تتكون كل منهما من n عنصرًا مسحوبًا من D، حيث قد لا يكون X₁ ∩ X₂ فارغًا، ولجميع المخرجات المعقمة X̄ ∈ D'،

f_{X₁}(X̄) ≤ e^α f_{X₂}(X̄), ∀X₁, X₂ s.t. V(X₁, X₂) ≤ δ                    (3)

حيث f_{X_j}(·) هي دالة الكثافة للتوزيع الشرطي مع القانون L(·|X_j)، ∀i معطى X_j.

لاحظ أن هذا يتكون بشكل جيد إذا كان المرء يعتبر قواعد بيانات تختلف في صفوف متعددة. على وجه الخصوص، لا يتم استغلال العشوائية في X_j بشكل مباشر في التعريف حيث نتعامل مع العناصر في X_j ∈ σ(D) كبيانات ثابتة. يمكن للمرء أن يفترض أنها تأتي من توزيع أساسي، على سبيل المثال، غاوسي متعدد المتغيرات N(0, Σ*)، واستنتاج المسافة بين Σ_i ونظيرها السكاني Σ*. نوضح الآن أن الخصوصية التوزيعية هي مفهوم أقوى من الخصوصية التفاضلية.

**المبرهنة 2.5.** معطى S_n، إذا كان A يحقق خصوصية توزيعية (α، δ) كما في التعريف 2.4 لجميع X_j ∈ S_n، فإن A يحقق خصوصية تفاضلية (α، δ) كما في التعريف 2.3 لجميع X_j ∈ S.

**البرهان.** لنفس معامل القيد δ، إذا ضمننا أن (3) راضية، لجميع X_i، X_j ∈ S_n التي تختلف فقط في صف واحد بحيث V(X_i, X_j) ≤ δ، فقد أظهرنا الخصوصية التفاضلية α على S_n؛ من الواضح أن هذا النوع من الضمان ضروري من أجل ضمان الخصوصية التوزيعية α على جميع X_i، X_j ∈ S_n التي تحقق قيد δ. □

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** sanitized database, essential supremum, Radon-Nikodym derivative, distributional privacy, constraint parameter
- **Equations:** 2 (equations 2 and 3)
- **Citations:** 2 references ([7], [3])
- **Special handling:** Mathematical definitions preserved with Arabic translations, formal proof included

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
