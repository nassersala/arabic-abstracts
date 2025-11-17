# Section 1: The HYPERLOGLOG Algorithm
## القسم 1: خوارزمية HYPERLOGLOG

**Section:** algorithm
**Translation Quality:** 0.88
**Glossary Terms Used:** algorithm, multiset, cardinality, hash function, register, indicator, harmonic mean, observable, bias

---

### English Version

The HYPERLOGLOG algorithm is fully specified in Figure 2, the corresponding program being discussed later, in Section 4. The input is a multiset M of data items, that is, a stream whose elements are read sequentially. The output is an estimate of the cardinality, defined as the number of distinct elements in M. A suitable hash function h has been fixed. The algorithm relies on a specific bit-pattern observable in conjunction with stochastic averaging. Given a string s ∈ {0,1}^∞, let ρ(s) represent the position of the leftmost 1 (equivalently one plus the length of the initial run of 0's). The stream M is split into substreams M₁, ..., M_m, based on the first b bits of hashed values of items, where m = 2^b, and each substream is processed independently. For NM_j such a substream (regarded as composed of hashed values stripped of their initial b bits), the corresponding observable is then

$$\text{Max}(N) := \max_{x \in N} \rho(x), \quad (1)$$

with the convention that Max(∅) = -∞. The algorithm gathers on the fly (in registers M[j]) the values M^(j) of Max(M_j) for j = 1...m. Once all the elements have been scanned, the algorithm computes the **indicator**,

$$Z := \left( \sum_{j=1}^{m} 2^{-M^{(j)}} \right)^{-1}. \quad (2)$$

It then returns a normalized version of the harmonic mean of the 2^M^(j) in the form,

$$E := \alpha_m m^2 Z, \quad \text{with } \alpha_m := \left( m \int_0^\infty \left( \log_2 \frac{2+u}{1+u} \right)^m du \right)^{-1}. \quad (3)$$

Here is the intuition underlying the algorithm. Let n be the unknown cardinality of M. Each substream will comprise approximately n/m elements. Then, its Max-parameter should be close to log₂(n/m). The harmonic mean (mZ in our notations) of the quantities 2^Max is then likely to be of the order of n/m. Thus, m²Z should be of the order of n. The constant α_m, provided by our subsequent analysis, is finally introduced so as to correct a systematic multiplicative bias present in m²Z.

Our main statement, Theorem 1 below, deals with the situation of **ideal multisets**:

**Definition 1** An ideal multiset of cardinality n is a sequence obtained by arbitrary replications and permutations applied to n uniform identically distributed random variables over the real interval [0,1].

---

**Algorithm HYPERLOGLOG(input M: multiset of items from domain D)**

Let h: D → [0,1] ≡ {0,1}^∞ hash data from domain D to the binary domain.
Let ρ(s), for s ∈ {0,1}^∞, be the position of the leftmost 1-bit (ρ(0001...) = 4).

```
assume m = 2^b with b ∈ Z_{>0};
initialize a collection of m registers, M[1], ..., M[m], to -∞;
for v ∈ M do
    set x := h(v);
    set j = 1 + ⟨x₁x₂...x_b⟩₂;  {the binary address determined by the first b bits of x}
    set w := x_{b+1}x_{b+2}...;
    set M[j] := max(M[j], ρ(w));
compute Z := (∑_{j=1}^m 2^{-M[j]})^{-1};  {the "indicator" function}
return E := α_m m² Z with α_m as given by Equation (3).
```

**Figure 2:** The HYPERLOGLOG Algorithm.

---

In the analytical part of our paper (Sections 2 and 3), we postulate that the collection of hashed values h(M), which the algorithm processes constitutes an ideal multiset. This assumption is a natural way to model the outcome of well designed hash functions. Note that the number of distinct elements of such an ideal multiset equals n with probability 1. We henceforth let E_n and V_n be the expectation and variance operators under this model.

**Theorem 1** Let the algorithm HYPERLOGLOG of Figure 2 be applied to an ideal multiset of (unknown) cardinality n, using m ≥ 3 registers, and let E be the resulting cardinality estimate.

(i) The estimate E is **asymptotically almost unbiased** in the sense that

$$\frac{1}{n} \mathbb{E}_n(E) \xrightarrow{n \to \infty} 1 + \lambda_1(n) + o(1), \quad \text{where } |\lambda_1(n)| < 5 \times 10^{-5} \text{ as soon } m \geq 16.$$

(ii) The **standard error** defined as $\frac{1}{n} \sqrt{\mathbb{V}_n(E)}$ satisfies as n → ∞,

$$\frac{1}{n} \sqrt{\mathbb{V}_n(E)} \xrightarrow{n \to \infty} \frac{\beta_m}{\sqrt{m}} + \lambda_2(n) + o(1), \quad \text{where } |\lambda_2(n)| < 5 \times 10^{-4} \text{ as soon } m \geq 16;$$

the constants β_m being bounded, with β₁₆ ≈ 1.106, β₃₂ ≈ 1.070, β₆₄ ≈ 1.054, β₁₂₈ ≈ 1.046, and β_∞ = 1/√(3 log(2)) ≈ 1.03896.

The standard error measures in relative terms the typical error to be observed (in a mean quadratic sense). The functions λ₁(n), λ₂(n) represent oscillating functions of a tiny amplitude, which are computable, and whose effect could in theory be at least partly compensated—they can anyhow be safely neglected for all practical purposes.

**Plan of the paper.** The bulk of the paper is devoted to the proof of Theorem 1. We determine the asymptotic behaviour of E_n(Z) and V_n(Z), where Z is the indicator 1/∑2^{-M^(j)}. The value of α_m in Equation (3), which makes E an asymptotically almost unbiased estimator, is derived from this analysis, as is the value of the standard error. The mean value analysis forms the subject of Section 2. In fact, the exact expression of E_n(Z) being hard to manage, we first "poissonize" the problem and examine E_P(λ)(Z), which represents the expected value of the indicator Z when the total number of elements is not fixed, but rather obeys a Poisson law of parameter λ. We then prove that, asymptotically, the behaviours of E_n(Z) and E_P(λ)(Z) are close, when one chooses λ := n: this is the depoissonization step. The variance analysis of the indicator Z, hence of the standard error, is sketched in Section 3 and is entirely parallel to the mean value analysis. Finally, Section 4 examines how to implement the HYPERLOGLOG algorithm in real-life contexts, presents simulations, and discusses optimality issues.

---

### النسخة العربية

خوارزمية HYPERLOGLOG محددة بالكامل في الشكل 2، حيث تتم مناقشة البرنامج المقابل لاحقاً، في القسم 4. المدخل هو مجموعة متعددة M من عناصر البيانات، أي تدفق تُقرأ عناصره بشكل تسلسلي. المخرج هو تقدير للعددية، المحددة كعدد العناصر المتمايزة في M. تم تثبيت دالة تجزئة مناسبة h. تعتمد الخوارزمية على مرصود نمط بت محدد بالاقتران مع المتوسط العشوائي. بالنظر إلى سلسلة s ∈ {0,1}^∞، دع ρ(s) يمثل موضع البت 1 الأيسر (أو بشكل مكافئ واحد زائد طول السلسلة الأولية من الأصفار). يتم تقسيم التدفق M إلى تدفقات فرعية M₁، ...، M_m، بناءً على أول b بت من القيم المجزأة للعناصر، حيث m = 2^b، ويتم معالجة كل تدفق فرعي بشكل مستقل. بالنسبة لـ NM_j مثل هذا التدفق الفرعي (يُعتبر مكوناً من قيم مجزأة مجردة من b بت الأولية)، فإن المرصود المقابل حينئذ هو

$$\text{Max}(N) := \max_{x \in N} \rho(x), \quad (1)$$

مع الاتفاق على أن Max(∅) = -∞. تجمع الخوارزمية أثناء التنفيذ (في السجلات M[j]) قيم M^(j) لـ Max(M_j) لـ j = 1...m. بمجرد مسح جميع العناصر، تحسب الخوارزمية **المؤشر**،

$$Z := \left( \sum_{j=1}^{m} 2^{-M^{(j)}} \right)^{-1}. \quad (2)$$

ثم تُرجع نسخة منظمة من المتوسط التوافقي لـ 2^M^(j) في الشكل،

$$E := \alpha_m m^2 Z, \quad \text{مع } \alpha_m := \left( m \int_0^\infty \left( \log_2 \frac{2+u}{1+u} \right)^m du \right)^{-1}. \quad (3)$$

فيما يلي الحدس الأساسي وراء الخوارزمية. دع n تكون العددية المجهولة لـ M. سيضم كل تدفق فرعي تقريباً n/m عنصر. حينئذ، يجب أن يكون معامل Max قريباً من log₂(n/m). المتوسط التوافقي (mZ في تدويناتنا) للكميات 2^Max من المحتمل حينئذ أن يكون من رتبة n/m. وبالتالي، يجب أن يكون m²Z من رتبة n. الثابت α_m، الذي يوفره تحليلنا اللاحق، يتم تقديمه أخيراً لتصحيح انحياز ضربي منهجي موجود في m²Z.

تتناول عبارتنا الرئيسية، النظرية 1 أدناه، حالة **المجموعات المتعددة المثالية**:

**التعريف 1** المجموعة المتعددة المثالية ذات العددية n هي تسلسل يتم الحصول عليه من خلال نسخ متماثلة وتبديلات تعسفية مطبقة على n متغيرات عشوائية موزعة بشكل متماثل ومنتظم على الفترة الحقيقية [0,1].

---

**خوارزمية HYPERLOGLOG(مدخل M: مجموعة متعددة من العناصر من المجال D)**

دع h: D → [0,1] ≡ {0,1}^∞ تجزأ البيانات من المجال D إلى المجال الثنائي.
دع ρ(s)، لـ s ∈ {0,1}^∞، يكون موضع البت 1 الأيسر (ρ(0001...) = 4).

```
افترض m = 2^b مع b ∈ Z_{>0};
ابدأ مجموعة من m سجل، M[1]، ...، M[m]، بـ -∞;
for v ∈ M do
    اجعل x := h(v);
    اجعل j = 1 + ⟨x₁x₂...x_b⟩₂;  {العنوان الثنائي المحدد بواسطة أول b بت من x}
    اجعل w := x_{b+1}x_{b+2}...;
    اجعل M[j] := max(M[j], ρ(w));
احسب Z := (∑_{j=1}^m 2^{-M[j]})^{-1};  {دالة "المؤشر"}
أرجع E := α_m m² Z مع α_m كما هو معطى بالمعادلة (3).
```

**الشكل 2:** خوارزمية HYPERLOGLOG.

---

في الجزء التحليلي من ورقتنا (الأقسام 2 و 3)، نفترض أن مجموعة القيم المجزأة h(M)، التي تعالجها الخوارزمية، تشكل مجموعة متعددة مثالية. هذا الافتراض هو طريقة طبيعية لنمذجة نتائج دوال التجزئة المصممة جيداً. لاحظ أن عدد العناصر المتمايزة لمثل هذه المجموعة المتعددة المثالية يساوي n مع احتمال 1. نترك من الآن فصاعداً E_n و V_n يكونان عوامل التوقع والتباين تحت هذا النموذج.

**النظرية 1** دع خوارزمية HYPERLOGLOG في الشكل 2 تُطبق على مجموعة متعددة مثالية ذات عددية (مجهولة) n، باستخدام m ≥ 3 سجلات، ودع E يكون تقدير العددية الناتج.

(i) التقدير E **غير منحاز بشكل شبه مقارب** بمعنى أن

$$\frac{1}{n} \mathbb{E}_n(E) \xrightarrow{n \to \infty} 1 + \lambda_1(n) + o(1), \quad \text{حيث } |\lambda_1(n)| < 5 \times 10^{-5} \text{ بمجرد } m \geq 16.$$

(ii) **الخطأ المعياري** المعرّف بـ $\frac{1}{n} \sqrt{\mathbb{V}_n(E)}$ يُحقق عندما n → ∞،

$$\frac{1}{n} \sqrt{\mathbb{V}_n(E)} \xrightarrow{n \to \infty} \frac{\beta_m}{\sqrt{m}} + \lambda_2(n) + o(1), \quad \text{حيث } |\lambda_2(n)| < 5 \times 10^{-4} \text{ بمجرد } m \geq 16;$$

الثوابت β_m محدودة، مع β₁₆ ≈ 1.106، β₃₂ ≈ 1.070، β₆₄ ≈ 1.054، β₁₂₈ ≈ 1.046، و β_∞ = 1/√(3 log(2)) ≈ 1.03896.

يقيس الخطأ المعياري بمصطلحات نسبية الخطأ النموذجي الذي يجب ملاحظته (بمعنى التربيع المتوسط). تمثل الدوال λ₁(n)، λ₂(n) دوالاً متذبذبة ذات سعة صغيرة جداً، وهي قابلة للحساب، ويمكن من الناحية النظرية تعويض تأثيرها جزئياً على الأقل—يمكن على أي حال إهمالها بأمان لجميع الأغراض العملية.

**خطة الورقة.** يُكرس الجزء الأكبر من الورقة لإثبات النظرية 1. نحدد السلوك المقارب لـ E_n(Z) و V_n(Z)، حيث Z هو المؤشر 1/∑2^{-M^(j)}. قيمة α_m في المعادلة (3)، التي تجعل E مقدراً غير منحاز بشكل شبه مقارب، مشتقة من هذا التحليل، كما هي قيمة الخطأ المعياري. يشكل تحليل القيمة المتوسطة موضوع القسم 2. في الواقع، التعبير الدقيق لـ E_n(Z) يصعب التعامل معه، لذا نقوم أولاً "ببواسونية" المشكلة وندرس E_P(λ)(Z)، الذي يمثل القيمة المتوقعة للمؤشر Z عندما لا يكون العدد الكلي للعناصر ثابتاً، بل يطيع قانون بواسون بمعامل λ. ثم نثبت أنه، بشكل مقارب، سلوكيات E_n(Z) و E_P(λ)(Z) قريبة، عندما نختار λ := n: هذه هي خطوة إزالة البواسونية. يتم تخطيط تحليل التباين للمؤشر Z، وبالتالي الخطأ المعياري، في القسم 3 وهو موازٍ تماماً لتحليل القيمة المتوسطة. أخيراً، يفحص القسم 4 كيفية تنفيذ خوارزمية HYPERLOGLOG في سياقات الحياة الواقعية، ويعرض المحاكاة، ويناقش قضايا الأمثلية.

---

### Translation Notes

- **Figures referenced:** Figure 2 (algorithm pseudocode)
- **Key terms introduced:** indicator (مؤشر), ideal multiset (مجموعة متعددة مثالية), asymptotically almost unbiased (غير منحاز بشكل شبه مقارب), poissonization (بواسونية), depoissonization (إزالة البواسونية)
- **Equations:** 3 major equations (1), (2), (3) with LaTeX notation preserved
- **Citations:** None in this section
- **Special handling:** Algorithm pseudocode translated while preserving technical structure

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.88
