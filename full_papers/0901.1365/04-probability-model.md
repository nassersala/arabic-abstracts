# Section 3: Probability Model and Summary of Results
## القسم 3: النموذج الاحتمالي وملخص النتائج

**Section:** probability-model
**Translation Quality:** 0.85
**Glossary Terms Used:** matrix, database, covariance, Gaussian, distribution, eigenvalue, Frobenius norm, normalization, theorem, lemma, principal component analysis

---

### English Version

Let (X_i) represent the matrix corresponding to X_i ∈ S_n. By default, we use (X_i)_j ∈ R^p, ∀j = 1, ..., n, and (X_i^T)_j ∈ R^n, ∀j = 1, ..., p to denote row vectors and column vectors of matrix (X_i) respectively. Throughout this paper, we assume that given any X_i ∈ S_n, columns are normalized,

‖(X_i^T)_j‖_2^2 = n, ∀j = 1, ..., p, ∀X_i ∈ S_n                    (4)

which can be taken as the first step of our sanitization scheme. Given X_j, Φ_{m×n} induces a distribution over all m × p matrices in R^{m×p} via X̄ = ΦX_j, where Φ_{ij} ~ N(0, 1/n), ∀i, j. Let L(·|X_j) denote the conditional distribution given X_j and P_{Σ_j} denote its probability measure, where Σ_j = X_j^T X_j/n, ∀X_j ∈ S_n. Hence X̄ = (x̄_1, ..., x̄_m)^T is a Gaussian Ensemble composed of m i.i.d. random vectors with L(x̄_i|X_j) ~ N(0, Σ_j), ∀i = 1, ..., m.

Given a set of databases S_n = {X_1, X_2, ...}, we do assume there is a true parameter Σ* such that Σ_1, Σ_2, ..., where Σ_j = X_j^T X_j/n, are just a sequence of empirical parameters computed from databases X_1, X_2, ... ∈ S_n. Define

Δ_max(S_n) := 2 sup_{X_j ∈ S_n} max_{ℓ,k} |Σ_j(ℓ, k) − Σ*(ℓ, k)|.                    (5)

Although we do not suppose we know Σ*, we do compute Σ_i, ∀i. Thus Δ_max(S_n) provides an upper bound on the perturbations between any two databases X_i, X_j ∈ S_n:

max_{ℓ,k} |Σ_i(ℓ, k) − Σ_j(ℓ, k)| ≤ Δ_max(S_n).                    (6)

We now relate two other parameters that measure pairwise distances between elements in S_n to Δ_max(S_n). For a symmetric matrix M, λ_min(M), λ_max(M) = ‖M‖_2 are the smallest and largest eigenvalues respectively and the Frobenius norm is given by ‖M‖_F = √(∑_i ∑_j M_{ij}^2).

**Proposition 3.1.** Subject to normalization as in (4), w.l.o.g., for any two databases X_1, X_j, let Δ = Σ_1−Σ_j and Γ̂ = Σ_j^{−1} − Σ_1^{−1} = Σ_j^{−1}(Σ_1 − Σ_j)Σ_1^{−1} = Σ_j^{−1}ΔΣ_1^{−1}. Suppose max_{ℓ,k} |(Σ_1 − Σ_j)_{ℓk}| ≤ Δ_max(S_n), ∀j then

‖Δ‖_F ≤ p Δ_max(S_n)   and                    (7)
‖Γ̂‖_F ≤ ‖Δ‖_F / (λ_min(Σ_1)λ_min(Σ_j)).                    (8)

Suppose we choose a reference point Σ_1 which can be thought of as an approximation to the true value Σ*.

**Assumption 1:** Let λ_min(Σ_1^{−1}) = 1/λ_max(Σ_1) ≥ C_min for some constant C_min > 0. Suppose ‖Γ̂‖_2 = o(1) and ‖Δ‖_2 = o(1).

Assumption 1 is crucial in the sense that it guarantees that all matrices in S_n stay away from being singular (see Lemma 3.3). We are now ready to state the first main result. Proof of the theorem appears in Section A.

**Theorem 3.2.** Suppose Assumption 1 holds. Assuming that ‖Σ_1‖_2, λ_min(Σ_1) and λ_min(Σ_i), ∀X_i ∈ S_n are all in the same order, and m ≥ Ω(ln 2np). Consider the worst case realization when ‖Δ‖_F = Θ(p Δ_max(S_n)), where Δ_max < 1.

In order to guard (distributional) privacy for all X_i ∈ S_n in the sense of Definition 2.4, it is sufficient if

Δ_max(S_n) = o(1/(p^2 √(m ln 2np))).                    (9)

The following lemma is a standard result on existence conditions for Σ_j^{−1} given Σ_1^{−1}. It also shows that all eigenvalue conditions in Theorem 3.2 indeed hold given Assumption 1.

**Lemma 3.3.** Let λ_min(Σ_1) > 0. Let Δ = Σ_1 − Σ_j and ‖Δ‖_2 < λ_min(Σ_1). Then λ_min(Σ_j) ≥ λ_min(Σ_1) − ‖Δ‖_2.

Next we use the result by Zwald and Blanchard for PCA as an instance from (1) to illustrate the tradeoff between parameters. Proof of Theorem 3.5 appears in Section 5.

**Proposition 3.4.** ([25]) Let A be a symmetric positive Hilbert-Schmidt operator of Hilbert space H with simple nonzero eigenvalues λ_1 > λ_2 > .... Let D > 0 be an integer such that λ_D > 0 and δ_D = 1/2(λ_D − λ_{D+1}). Let B ∈ HS(H) be another symmetric operator such that ‖B‖_F ≤ δ_D/2 and A + B is still a positive operator. Let P^D(A) (resp. P^D(A+ B)) denote the orthogonal projector onto the subspace spanned by the first D eigenvectors A (resp. (A + B)). Then these satisfy

‖P^D(A) − P^D(A + B)‖_F ≤ ‖B‖_F/δ_D.                    (10)

Subject to measure truncation of at most 1/n^2 in each P_{Σ_j}, ∀X ∈ S_n, as we show in Section 4, we have,

**Theorem 3.5.** Suppose Assumption 1 holds. If we allow Δ_max(S_n) = O(√(log p/n)), then we essentially perform PCA on the compressed sample covariance matrix X̄^T X̄/m effectively in the sense of Proposition 3.4: that is, in the form of (10) with A = X^T X/n and B = X̄^T X̄/m − A, where ‖B‖_F = o(1) for m = Ω(p^2 ln 2np). On the other hand, the databases in S_n are private in the sense of Definition 2.4, so long as p^2 = O(√(n/m)/log n). Hence in the worst case, we require

p = o(n^{1/6}/√(ln 2np)).

As a special case, we look at the following example.

**Example 3.6.** Let X_1 = {x̃_1, ..., x̃_n}^T be a matrix of {−1, 1}^{n×p}. A neighboring matrix X_2 is any matrix obtained via changing the signs on τp bits, where 0 ≤ τ < 1, on any x̃_i.

**Corollary 3.7.** For the Example 3.6, it suffices if p = o(n/log n)^{1/4}, in order to conduct PCA on compressed data, (subject to measure truncation of at most 1/n^2 in each P_{Σ_j}, ∀X ∈ S_n,) effectively in the sense of Proposition 3.4, while preserve the α-differential privacy for α = o(1).

---

### النسخة العربية

دع (X_i) تمثل المصفوفة المقابلة لـ X_i ∈ S_n. افتراضيًا، نستخدم (X_i)_j ∈ R^p، ∀j = 1، ...، n، و (X_i^T)_j ∈ R^n، ∀j = 1، ...، p للإشارة إلى متجهات الصفوف ومتجهات الأعمدة للمصفوفة (X_i) على التوالي. في جميع أنحاء هذه الورقة، نفترض أنه بالنظر إلى أي X_i ∈ S_n، الأعمدة منمطة،

‖(X_i^T)_j‖_2^2 = n، ∀j = 1، ...، p، ∀X_i ∈ S_n                    (4)

والتي يمكن أخذها كخطوة أولى في مخطط التعقيم لدينا. بالنظر إلى X_j، Φ_{m×n} يحفز توزيعًا على جميع مصفوفات m × p في R^{m×p} عبر X̄ = ΦX_j، حيث Φ_{ij} ~ N(0، 1/n)، ∀i، j. دع L(·|X_j) يشير إلى التوزيع الشرطي معطى X_j و P_{Σ_j} يشير إلى مقياس احتماله، حيث Σ_j = X_j^T X_j/n، ∀X_j ∈ S_n. وبالتالي فإن X̄ = (x̄_1، ...، x̄_m)^T هو مجموع غاوسي مكون من m متجهات عشوائية مستقلة ومتماثلة التوزيع مع L(x̄_i|X_j) ~ N(0، Σ_j)، ∀i = 1، ...، m.

بالنظر إلى مجموعة من قواعد البيانات S_n = {X_1، X_2، ...}، نفترض أن هناك معاملاً حقيقيًا Σ* بحيث أن Σ_1، Σ_2، ...، حيث Σ_j = X_j^T X_j/n، هي فقط سلسلة من المعاملات التجريبية المحسوبة من قواعد البيانات X_1، X_2، ... ∈ S_n. عرّف

Δ_max(S_n) := 2 sup_{X_j ∈ S_n} max_{ℓ,k} |Σ_j(ℓ، k) − Σ*(ℓ، k)|.                    (5)

على الرغم من أننا لا نفترض أننا نعرف Σ*، فإننا نحسب Σ_i، ∀i. وبالتالي فإن Δ_max(S_n) يوفر حدًا أعلى على الاضطرابات بين أي قاعدتي بيانات X_i، X_j ∈ S_n:

max_{ℓ,k} |Σ_i(ℓ، k) − Σ_j(ℓ، k)| ≤ Δ_max(S_n).                    (6)

نربط الآن معاملين آخرين يقيسان المسافات الزوجية بين العناصر في S_n بـ Δ_max(S_n). لمصفوفة متماثلة M، λ_min(M)، λ_max(M) = ‖M‖_2 هما القيمتان الذاتيتان الأصغر والأكبر على التوالي ومعيار فروبينيوس معطى بـ ‖M‖_F = √(∑_i ∑_j M_{ij}^2).

**القضية 3.1.** بشرط التطبيع كما في (4)، دون فقدان العمومية، لأي قاعدتي بيانات X_1، X_j، دع Δ = Σ_1−Σ_j و Γ̂ = Σ_j^{−1} − Σ_1^{−1} = Σ_j^{−1}(Σ_1 − Σ_j)Σ_1^{−1} = Σ_j^{−1}ΔΣ_1^{−1}. افترض max_{ℓ,k} |(Σ_1 − Σ_j)_{ℓk}| ≤ Δ_max(S_n)، ∀j إذن

‖Δ‖_F ≤ p Δ_max(S_n)   و                    (7)
‖Γ̂‖_F ≤ ‖Δ‖_F / (λ_min(Σ_1)λ_min(Σ_j)).                    (8)

افترض أننا نختار نقطة مرجعية Σ_1 والتي يمكن اعتبارها تقريبًا للقيمة الحقيقية Σ*.

**الافتراض 1:** دع λ_min(Σ_1^{−1}) = 1/λ_max(Σ_1) ≥ C_min لبعض الثابت C_min > 0. افترض ‖Γ̂‖_2 = o(1) و ‖Δ‖_2 = o(1).

الافتراض 1 حاسم بمعنى أنه يضمن أن جميع المصفوفات في S_n تبقى بعيدة عن كونها مفردة (انظر المبرهنة المساعدة 3.3). نحن الآن جاهزون لذكر النتيجة الرئيسية الأولى. يظهر برهان المبرهنة في القسم A.

**المبرهنة 3.2.** افترض أن الافتراض 1 صحيح. بافتراض أن ‖Σ_1‖_2، λ_min(Σ_1) و λ_min(Σ_i)، ∀X_i ∈ S_n كلها بنفس الترتيب، و m ≥ Ω(ln 2np). اعتبر الحالة الأسوأ عندما ‖Δ‖_F = Θ(p Δ_max(S_n))، حيث Δ_max < 1.

من أجل حماية الخصوصية (التوزيعية) لجميع X_i ∈ S_n بمعنى التعريف 2.4، يكفي إذا

Δ_max(S_n) = o(1/(p^2 √(m ln 2np))).                    (9)

المبرهنة المساعدة التالية هي نتيجة قياسية على شروط وجود Σ_j^{−1} معطى Σ_1^{−1}. كما يُظهر أن جميع شروط القيم الذاتية في المبرهنة 3.2 تتحقق بالفعل معطى الافتراض 1.

**المبرهنة المساعدة 3.3.** دع λ_min(Σ_1) > 0. دع Δ = Σ_1 − Σ_j و ‖Δ‖_2 < λ_min(Σ_1). إذن λ_min(Σ_j) ≥ λ_min(Σ_1) − ‖Δ‖_2.

بعد ذلك نستخدم النتيجة بواسطة Zwald و Blanchard لـ PCA كمثال من (1) لتوضيح المقايضة بين المعاملات. يظهر برهان المبرهنة 3.5 في القسم 5.

**القضية 3.4.** ([25]) دع A تكون مؤثرًا متماثلًا موجبًا لهلبرت-شميت لفضاء هلبرت H مع قيم ذاتية غير صفرية بسيطة λ_1 > λ_2 > .... دع D > 0 يكون عددًا صحيحًا بحيث λ_D > 0 و δ_D = 1/2(λ_D − λ_{D+1}). دع B ∈ HS(H) تكون مؤثرًا متماثلًا آخر بحيث ‖B‖_F ≤ δ_D/2 و A + B لا يزال مؤثرًا موجبًا. دع P^D(A) (أو P^D(A+ B)) تشير إلى المُسقِط المتعامد على الفضاء الجزئي الممتد بواسطة أول D متجهات ذاتية A (أو (A + B)). إذن هذه تحقق

‖P^D(A) − P^D(A + B)‖_F ≤ ‖B‖_F/δ_D.                    (10)

بشرط اقتطاع مقياس 1/n^2 على الأكثر في كل P_{Σ_j}، ∀X ∈ S_n، كما نوضح في القسم 4، لدينا،

**المبرهنة 3.5.** افترض أن الافتراض 1 صحيح. إذا سمحنا Δ_max(S_n) = O(√(log p/n))، فإننا نؤدي PCA بشكل أساسي على مصفوفة التباين المشترك للعينة المضغوطة X̄^T X̄/m بشكل فعال بمعنى القضية 3.4: أي، في شكل (10) مع A = X^T X/n و B = X̄^T X̄/m − A، حيث ‖B‖_F = o(1) لـ m = Ω(p^2 ln 2np). من ناحية أخرى، قواعد البيانات في S_n خاصة بمعنى التعريف 2.4، طالما p^2 = O(√(n/m)/log n). وبالتالي في الحالة الأسوأ، نطلب

p = o(n^{1/6}/√(ln 2np)).

كحالة خاصة، ننظر في المثال التالي.

**المثال 3.6.** دع X_1 = {x̃_1، ...، x̃_n}^T تكون مصفوفة من {−1، 1}^{n×p}. المصفوفة المجاورة X_2 هي أي مصفوفة يتم الحصول عليها عبر تغيير الإشارات على τp بت، حيث 0 ≤ τ < 1، على أي x̃_i.

**النتيجة 3.7.** للمثال 3.6، يكفي إذا كان p = o(n/log n)^{1/4}، من أجل إجراء PCA على البيانات المضغوطة، (بشرط اقتطاع مقياس 1/n^2 على الأكثر في كل P_{Σ_j}، ∀X ∈ S_n،) بشكل فعال بمعنى القضية 3.4، مع الحفاظ على الخصوصية التفاضلية α لـ α = o(1).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Gaussian ensemble, measure truncation, eigenvalue bounds, Hilbert-Schmidt operator, orthogonal projector
- **Equations:** 7 equations (4-10)
- **Citations:** Reference [25]
- **Special handling:** Mathematical notation and theorems carefully preserved with formal Arabic mathematical language

### Quality Metrics

- Semantic equivalence: 0.85
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.85
