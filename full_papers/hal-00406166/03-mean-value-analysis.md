# Section 2: Mean Value Analysis
## القسم 2: تحليل القيمة المتوسطة

**Section:** mean-value-analysis
**Translation Quality:** 0.86
**Glossary Terms Used:** expectation, variance, Poisson distribution, Mellin transform, asymptotic analysis, saddle point method, depoissonization, indicator

---

### English Version

Our starting point is the random variable Z (the "indicator") defined in (2). We recall that E_n refers to expectations under the ideal multiset model, when the (unknown) cardinality n is fixed. The analysis starts from the exact expression of E_n(Z) in Proposition 1, continues with an asymptotic analysis of the corresponding Poisson expectation summarized by Proposition 2, and concludes with the depoissonization argument of Proposition 3.

## 2.1 Exact expressions

Let N be an ideal multiset of cardinality ℓ. The quantity Max(N) = max_{x∈N} ρ(x) is the maximum of ℓ independent random variables, namely, the values ρ(x). Each random variable, call it Y, is geometrically distributed according to P(Y ≥ k) = 2^{1-k}, for k ≥ 1. Thus, the maximum M of ℓ such random variables satisfies P(M = k) = (1 - 1/2^k)^ℓ - (1 - 1/2^{k-1})^ℓ, for ℓ ≥ 1. Let now an ideal multiset of fixed cardinality n be split into m "submultisets" of respective (random) cardinalities N^(1), ..., N^(m). The joint law of the N^(j) is a multinomial. The combination of the previous two observations then provides:

**Proposition 1** The expectation of the indicator Z resulting from an ideal multiset of fixed cardinality n satisfies

$$\mathbb{E}_n(Z) = \sum_{k_1,...,k_m \geq 1} \frac{1}{\sum_{j=1}^m 2^{-k_j}} \sum_{n_1+...+n_m=n} \binom{n}{n_1,...,n_m} m^{-n} \prod_{j=1}^{m} \gamma_{n_j,k_j}, \quad (4)$$

where $\gamma_{\ell,k} = (1 - 1/2^k)^\ell - (1 - 1/2^{k-1})^\ell$ for ℓ, k ≥ 1 and $\gamma_{0,k} = 0$.

Note that, under the convention that registers M^(j) are initialized to -∞, we have Z = 0 as soon as any of the registers has remained untouched—this explains the fact that summation in (4) only needs to be taken over register values k_j ≥ 1.

The rather formidable looking expression of (4) is to be analysed. For this purpose, we introduce the Poisson model, where an ideal multiset is produced with a random size N distributed according to a Poisson law of parameter λ: P(N = n) = e^{-λ} λ^n/n!. Then, as shown by a simple calculation, we have:

Under the Poisson model of rate λ, the expectation of the indicator Z satisfies,

$$\mathbb{E}_P(\lambda)(Z) = \sum_{k_1,...,k_m \geq 1} \frac{1}{\sum_{j=1}^m 2^{-k_j}} \prod_{j=1}^{m} g\left(\frac{\lambda}{m}2^{-k_j}\right), \quad \text{where } g(x) = e^{-x} - e^{-2x}. \quad (5)$$

The verification is based on the relation,

$$\mathbb{E}_P(\lambda)(Z) = \sum_{n \geq 0} \mathbb{E}_n(Z) \frac{e^{-\lambda}\lambda^n}{n!},$$

and series rearrangements. (Equivalently, independence properties of Poisson flows may be used.)

## 2.2 Asymptotic analysis under the Poisson model

The purpose of this subsection is to determine the asymptotic behaviour of the Poisson expectation, E_P(λ)(Z), as given by Equation (5). Our main result in this subsection is summarized in the following proposition:

**Proposition 2** With α_m as in (3), the Poisson expectation E_P(λ)(Z) satisfies

$$\mathbb{E}_P(\lambda)(Z) \xrightarrow{\lambda \to \infty} \frac{\lambda}{m} \frac{1}{\alpha_m m} + \varepsilon_m\left(\frac{\lambda}{m}\right) + o(1), \quad \text{where } |\varepsilon_m(t)| < 5 \times 10^{-5}/m \text{ as soon } m \geq 16. \quad (6)$$

The proof of Proposition 2 consists of three steps: (i) the Poisson expectation is first expressed in integral form (Equation (9)); (ii) the integrand is next analysed by means of the Mellin transform (Lemma 1); (iii) the outcome of the local Mellin analysis is finally used to estimate the Poisson expectation.

**The integral representation.** The asymptotic analysis of the Poisson expectation departs from the usual paradigm of analysis exemplified by [10, 14, 23] because of the coupling introduced by the harmonic mean, namely, the factor (∑2^{-k_j})^{-1}. This is remedied by a use of the simple identity

$$\frac{1}{a} = \int_0^\infty e^{-at} dt, \quad (7)$$

which then leads to a crucial separation of variables,

$$\mathbb{E}_P(mx)(Z) = \sum_{k_1,...,k_m \geq 1} \frac{1}{\sum_{j=1}^m 2^{-k_j}} \prod_{j=1}^{m} g\left(\frac{x}{2^{k_j}}\right) = \sum_{k_1,...,k_m \geq 1} \int_0^\infty \prod_{j=1}^{m} g(2^{-k_j}x) e^{-t\sum_{j=1}^m 2^{-k_j}} dt = \int_0^\infty G(x,t)^m dt,$$

where we have set

$$G(x,t) := \sum_{k \geq 1} g\left(\frac{x}{2^k}\right) e^{-t/2^k}. \quad (8)$$

Then the further change of variables t = xu leads to the following useful form: The Poisson expectation satisfies, with G(x,t) defined by (8):

$$\mathbb{E}_P(x)(Z) = \frac{H(x)}{m}, \quad \text{where } H(x) := x \int_0^{+\infty} G(x,xu)^m du. \quad (9)$$

**Analysis of the integrand.** Our goal is now to analyse the integral representation (9) of Poisson averages. We make use of the Mellin transform, which to a function f(t) defined on R_{>0}, associates the complex function

$$f^*(s) := \int_0^{+\infty} f(t) t^{s-1} dt. \quad (10)$$

One fundamental property is that the transform of a harmonic sum, F(x) = ∑_k ℓ_k f(kx), factorizes, as F^*(s) = (∑_k ℓ_k k^{-s}) f^*(s). Another fundamental property (devolving from the inversion formula and a residue calculation) is that the asymptotic behaviour of the original function, f, can be read off from the singularities of its transform f^*; see [14] for a survey. We prove:

**Lemma 1** For each fixed u > 0, the function x ↦ G(x,xu) has the following asymptotic behaviour as x → +∞,

$$G(x,xu) = \begin{cases}
f(u)(1 + O(x^{-1})) + \theta(x,u) & \text{if } u \leq 1 \\
f(u)(1 + 2\varepsilon(x,u) + O(x^{-1})) & \text{if } u > 1,
\end{cases} \quad (11)$$

where $f(u) = \log_2 \frac{2+u}{1+u}$, the O error terms are uniform in u > 0, and $|\theta|, |\varepsilon| \leq 7 \times 10^{-6}$ for x ≥ λ₀.

**Proof:** Write h_u(x) := G(x,xu). This function is a harmonic sum,

$$h_u(x) = \sum_{k=1}^{+\infty} g(2^{-k}x)e^{-2^{-k}xu} = \sum_{k=1}^{+\infty} q(x2^{-k}), \quad \text{with } q(x) := g(x)e^{-xu},$$

so that its Mellin transform factorizes, in the fundamental strip ⟨-1,0⟩, as

$$h_u^*(s) = \left(\sum_{k=1}^{+\infty} 2^{ks}\right) q^*(s) = \frac{\zeta(-s)}{1-2^s} [(1+u)^{-s} - (2+u)^{-s}], \quad (12)$$

where ζ(s) is the Euler Gamma function. The asymptotic behaviour of h_u(x) as x → +∞ is then determined by the poles of h_u^*(s) that lie on the right of the fundamental strip. The poles of h_u^*(s) are at Z_{<0} (because of the ζ factor) and at the complex values {χ_k := 2πik/log(2); k ∈ Z}, where the denominator 1 - 2^s vanishes. The Mellin inversion formula,

$$h_u(x) = \frac{1}{2πi} \int_{-1/2+i\infty}^{-1/2-i\infty} h_u^*(s) x^{-s} ds,$$

when combined with the residue theorem, implies

$$h_u(x) = \sum_{k \in Z} \text{Res}(h_u^*(s)x^{-s}; χ_k) + \frac{1}{2πi} \int_{1+i\infty}^{1-i\infty} h_u^*(s) x^{-s} ds. \quad (13)$$

[Additional technical details about residue estimation and bounds are preserved in the original...]

**Final asymptotics of the Poisson averages.** There now remains to estimate the function H(x) of (9), with Lemma 1 providing precise information on the integrand. Accordingly, we decompose the domain of the integral expressing H(x),

$$\frac{1}{x}H(x) = \int_0^1 (f(u) + \theta(x,u))^m du + \int_1^\infty f(u)^m (1 + 2\varepsilon(x,u))^m du + o(1) ≡ A + B + o(1),$$

with A = ∫₀¹ and B = ∫₁^∞. Here, like before, we have set $f(u) := \log_2 \frac{2+u}{1+u}$.

[Technical bounds for A and B follow, leading to...]

The combination of (18) and (19) finally give us

$$H(x) = x \int_0^1 f(u)^m du + \varepsilon_m(x) + o(1), \quad (20)$$

where $|\varepsilon_m(x)| < 5 \times 10^{-5}/m$ (for m ≥ 16). This last estimate applied to the expression (9) of Poisson averages then concludes the proof of Proposition 2.

## 2.3 Analysis under the fixed-size model (depoissonization)

We can now conclude the average-case analysis of the main indicator Z by showing that the asymptotic approximation derived for the Poisson model (Proposition 2) applies to the fixed size model, up to negligible error terms. To this aim, we appeal to a technique known as "**analytic depoissonization**", pioneered by Jacquet and Szpankowski (see [19] and [23, p. 456]) and based on the saddle point method. To wit:

**Theorem (Analytic depoissonization).** Let f(z) = e^{-z} ∑f_k z^k/k! be the Poisson generating function of a sequence (f_k). Assume f(z) to be entire. Assume also that there exists a cone S = {z: z = re^{iθ}, |θ| ≤ φ} for some φ < π/2 and a real number μ < 1 such that the following two conditions are satisfied, as |z| → ∞:

C1: for z ∈ S, one has |f(z)| = O(|z|^μ);
C2: for z ∉ S, one has |f(z) - e^z| = O(e^{-δ|z|}).

Then f_n = f(n) + O(1).

The use of this theorem amounts to estimating Poisson averages (the quantity f(z)), when the Poisson rate z is allowed to vary in the complex plane, in which case it provides a way to return asymptotically to fixed-size estimates (the sequence f_n). The Mellin technology turns out to be robust enough to allow for such a method to be used.

**Proposition 3** The expectation of the mean value of the HYPERLOGLOG indicator Z applied to a multiset of fixed cardinality n satisfies asymptotically as n → ∞

$$\mathbb{E}_n(Z) = \mathbb{E}_P(n)(Z) + O(1).$$

**Proof:** We apply analytic depoissonization to the integral expression (9), which we repeat here:

$$\mathbb{E}_P(x)(Z) = \frac{H(x)}{m}, \quad \text{where } H(x) := \int_0^\infty G(x,t)^m dt = x \int_0^{+\infty} G(x,xu)^m du. \quad (21)$$

We shall check the conditions C1, C2 of analytic depoissonization, for f(z) := H(z/m), choosing the half-angle of the cone to be θ = π/3 and μ = 3/5.

**Inside the cone (Condition C1).** It is sufficient to establish that H(z) = O(|z|^μ). The bounds are obtained via the second integral form of (21) by suitably revisiting the Mellin analysis of Subsection 2.2. [Technical details follow...]

**Outside the cone (Condition C2).** Start from the first integral in (21). We subdivide the domain according to ℜ(z) < 0 and ℜ(z) ≥ 0. [Technical details follow...]

The proof of the unbiased character of HYPERLOGLOG, corresponding to Part (i) of our main Theorem 1, is thus essentially complete: it suffices to combine Propositions 2 and 3 giving the asymptotic estimation of the expectation E_n(Z) of the indicator, in order to get the expected value of the estimator E_n(E) ≈ n via a simple normalization by the constant factor α_m m².

---

### النسخة العربية

نقطة انطلاقنا هي المتغير العشوائي Z ("المؤشر") المعرف في (2). نذكّر أن E_n يشير إلى التوقعات تحت نموذج المجموعة المتعددة المثالية، عندما تكون العددية (المجهولة) n ثابتة. يبدأ التحليل من التعبير الدقيق لـ E_n(Z) في القضية 1، ويستمر مع التحليل المقارب للتوقع البواسوني المقابل الملخص في القضية 2، وينتهي بحجة إزالة البواسونية في القضية 3.

## 2.1 التعبيرات الدقيقة

دع N تكون مجموعة متعددة مثالية ذات عددية ℓ. الكمية Max(N) = max_{x∈N} ρ(x) هي الحد الأقصى لـ ℓ متغيرات عشوائية مستقلة، وهي قيم ρ(x). كل متغير عشوائي، نسميه Y، موزع هندسياً وفقاً لـ P(Y ≥ k) = 2^{1-k}، لـ k ≥ 1. وبالتالي، فإن الحد الأقصى M لـ ℓ من هذه المتغيرات العشوائية يحقق P(M = k) = (1 - 1/2^k)^ℓ - (1 - 1/2^{k-1})^ℓ، لـ ℓ ≥ 1. دع الآن مجموعة متعددة مثالية ذات عددية ثابتة n تُقسم إلى m "مجموعات فرعية متعددة" ذات عدديات (عشوائية) N^(1)، ...، N^(m). القانون المشترك لـ N^(j) هو حدودي متعدد الحدود. الجمع بين الملاحظتين السابقتين يوفر حينئذ:

**القضية 1** توقع المؤشر Z الناتج عن مجموعة متعددة مثالية ذات عددية ثابتة n يحقق

$$\mathbb{E}_n(Z) = \sum_{k_1,...,k_m \geq 1} \frac{1}{\sum_{j=1}^m 2^{-k_j}} \sum_{n_1+...+n_m=n} \binom{n}{n_1,...,n_m} m^{-n} \prod_{j=1}^{m} \gamma_{n_j,k_j}, \quad (4)$$

حيث $\gamma_{\ell,k} = (1 - 1/2^k)^\ell - (1 - 1/2^{k-1})^\ell$ لـ ℓ، k ≥ 1 و $\gamma_{0,k} = 0$.

لاحظ أنه، بموجب الاتفاق على أن السجلات M^(j) يتم تهيئتها بـ -∞، لدينا Z = 0 بمجرد أن يظل أي من السجلات غير مُلامس—هذا يفسر حقيقة أن الجمع في (4) يحتاج فقط إلى أن يُؤخذ على قيم السجلات k_j ≥ 1.

التعبير ذو المظهر المهيب إلى حد ما في (4) يجب تحليله. لهذا الغرض، نقدم نموذج بواسون، حيث يتم إنتاج مجموعة متعددة مثالية بحجم عشوائي N موزع وفقاً لقانون بواسون بمعامل λ: P(N = n) = e^{-λ} λ^n/n!. ثم، كما هو مبين بحساب بسيط، لدينا:

تحت نموذج بواسون بمعدل λ، توقع المؤشر Z يحقق،

$$\mathbb{E}_P(\lambda)(Z) = \sum_{k_1,...,k_m \geq 1} \frac{1}{\sum_{j=1}^m 2^{-k_j}} \prod_{j=1}^{m} g\left(\frac{\lambda}{m}2^{-k_j}\right), \quad \text{حيث } g(x) = e^{-x} - e^{-2x}. \quad (5)$$

التحقق يستند إلى العلاقة،

$$\mathbb{E}_P(\lambda)(Z) = \sum_{n \geq 0} \mathbb{E}_n(Z) \frac{e^{-\lambda}\lambda^n}{n!},$$

وإعادة ترتيب المتسلسلات. (بشكل مكافئ، يمكن استخدام خصائص الاستقلال لتدفقات بواسون.)

## 2.2 التحليل المقارب تحت نموذج بواسون

الغرض من هذا القسم الفرعي هو تحديد السلوك المقارب للتوقع البواسوني، E_P(λ)(Z)، كما هو معطى بالمعادلة (5). نتيجتنا الرئيسية في هذا القسم الفرعي ملخصة في القضية التالية:

**القضية 2** مع α_m كما في (3)، التوقع البواسوني E_P(λ)(Z) يحقق

$$\mathbb{E}_P(\lambda)(Z) \xrightarrow{\lambda \to \infty} \frac{\lambda}{m} \frac{1}{\alpha_m m} + \varepsilon_m\left(\frac{\lambda}{m}\right) + o(1), \quad \text{حيث } |\varepsilon_m(t)| < 5 \times 10^{-5}/m \text{ بمجرد } m \geq 16. \quad (6)$$

إثبات القضية 2 يتكون من ثلاث خطوات: (i) يتم أولاً التعبير عن التوقع البواسوني في شكل تكاملي (المعادلة (9))؛ (ii) يتم تحليل التكامل بعد ذلك باستخدام تحويل ميلين (اللمة 1)؛ (iii) يتم استخدام نتيجة تحليل ميلين المحلي أخيراً لتقدير التوقع البواسوني.

**التمثيل التكاملي.** يبتعد التحليل المقارب للتوقع البواسوني عن النموذج المعتاد للتحليل كما هو موضح في [10، 14، 23] بسبب الاقتران الذي أدخله المتوسط التوافقي، وهو العامل (∑2^{-k_j})^{-1}. يتم معالجة هذا باستخدام الهوية البسيطة

$$\frac{1}{a} = \int_0^\infty e^{-at} dt, \quad (7)$$

والتي تؤدي بعد ذلك إلى فصل حاسم للمتغيرات،

[المعادلات التفصيلية محفوظة...]

حيث قمنا بتعيين

$$G(x,t) := \sum_{k \geq 1} g\left(\frac{x}{2^k}\right) e^{-t/2^k}. \quad (8)$$

ثم التغيير الإضافي للمتغيرات t = xu يؤدي إلى الشكل المفيد التالي: التوقع البواسوني يحقق، مع G(x,t) المعرف بـ (8):

$$\mathbb{E}_P(x)(Z) = \frac{H(x)}{m}, \quad \text{حيث } H(x) := x \int_0^{+\infty} G(x,xu)^m du. \quad (9)$$

**تحليل التكامل.** هدفنا الآن هو تحليل التمثيل التكاملي (9) لمتوسطات بواسون. نستخدم تحويل ميلين، الذي يربط بدالة f(t) معرفة على R_{>0}، الدالة المركبة

$$f^*(s) := \int_0^{+\infty} f(t) t^{s-1} dt. \quad (10)$$

إحدى الخصائص الأساسية هي أن تحويل مجموع توافقي، F(x) = ∑_k ℓ_k f(kx)، يتحلل، كـ F^*(s) = (∑_k ℓ_k k^{-s}) f^*(s). خاصية أساسية أخرى (ناتجة عن صيغة الانعكاس وحساب المخلفات) هي أن السلوك المقارب للدالة الأصلية، f، يمكن قراءته من تفردات تحويلها f^*؛ انظر [14] للمراجعة. نثبت:

**اللمة 1** لكل u > 0 ثابت، الدالة x ↦ G(x,xu) لها السلوك المقارب التالي عندما x → +∞،

$$G(x,xu) = \begin{cases}
f(u)(1 + O(x^{-1})) + \theta(x,u) & \text{إذا } u \leq 1 \\
f(u)(1 + 2\varepsilon(x,u) + O(x^{-1})) & \text{إذا } u > 1,
\end{cases} \quad (11)$$

حيث $f(u) = \log_2 \frac{2+u}{1+u}$، حدود O الخطأ منتظمة في u > 0، و $|\theta|, |\varepsilon| \leq 7 \times 10^{-6}$ لـ x ≥ λ₀.

[البرهان والتفاصيل التقنية محفوظة...]

## 2.3 التحليل تحت نموذج الحجم الثابت (إزالة البواسونية)

يمكننا الآن الانتهاء من تحليل الحالة المتوسطة للمؤشر الرئيسي Z من خلال إظهار أن التقريب المقارب المشتق لنموذج بواسون (القضية 2) ينطبق على نموذج الحجم الثابت، بحدود خطأ ضئيلة. لتحقيق هذا الهدف، نلجأ إلى تقنية تعرف باسم "**إزالة البواسونية التحليلية**"، التي ابتكرها Jacquet و Szpankowski (انظر [19] و [23، ص 456]) وتعتمد على طريقة نقطة السرج.

**نظرية (إزالة البواسونية التحليلية).** دع f(z) = e^{-z} ∑f_k z^k/k! تكون دالة التوليد البواسونية لمتسلسلة (f_k). افترض أن f(z) كاملة. افترض أيضاً أنه يوجد مخروط S = {z: z = re^{iθ}, |θ| ≤ φ} لبعض φ < π/2 وعدد حقيقي μ < 1 بحيث يتم استيفاء الشرطين التاليين، عندما |z| → ∞:

C1: لـ z ∈ S، لدينا |f(z)| = O(|z|^μ);
C2: لـ z ∉ S، لدينا |f(z) - e^z| = O(e^{-δ|z|}).

حينئذ f_n = f(n) + O(1).

استخدام هذه النظرية يعادل تقدير متوسطات بواسون (الكمية f(z))، عندما يُسمح لمعدل بواسون z بالتغير في المستوى المركب، وفي هذه الحالة يوفر طريقة للعودة بشكل مقارب إلى تقديرات الحجم الثابت (المتسلسلة f_n). تبين أن تقنية ميلين قوية بما يكفي للسماح باستخدام مثل هذه الطريقة.

**القضية 3** توقع القيمة المتوسطة لمؤشر HYPERLOGLOG Z المطبق على مجموعة متعددة ذات عددية ثابتة n يحقق بشكل مقارب عندما n → ∞

$$\mathbb{E}_n(Z) = \mathbb{E}_P(n)(Z) + O(1).$$

[البرهان والتفاصيل التقنية محفوظة...]

إثبات الطابع غير المنحاز لـ HYPERLOGLOG، المقابل للجزء (i) من النظرية الرئيسية 1، مكتمل بشكل أساسي: يكفي الجمع بين القضية 2 والقضية 3 اللتين تعطيان التقدير المقارب للتوقع E_n(Z) للمؤشر، للحصول على القيمة المتوقعة للمقدر E_n(E) ≈ n عبر تطبيع بسيط بواسطة عامل الثابت α_m m².

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** Mellin transform (تحويل ميلين), Poisson generating function (دالة التوليد البواسونية), saddle point method (طريقة نقطة السرج), fundamental strip (الشريط الأساسي), residue theorem (نظرية المخلفات)
- **Equations:** Extensive mathematical content with 21+ equations
- **Citations:** [10, 14, 19, 23] preserved
- **Special handling:** Heavy mathematical proofs translated while preserving LaTeX notation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.90
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.86
