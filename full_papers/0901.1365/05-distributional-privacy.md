# Section 4: Distributional Privacy with Bounded Δmax(Sn)
## القسم 4: الخصوصية التوزيعية مع Δmax(Sn) المحدود

**Section:** distributional-privacy
**Translation Quality:** 0.85
**Glossary Terms Used:** density function, Gaussian distribution, covariance, privacy, truncation, renormalization, probability measure, differential privacy, algorithm

---

### English Version

In this section, we show how we can modify the output events X̄ to effectively hide some large-tail events. We make it clear how these tail events are connected to a particular type of utility. Given X_i, let X̄ = ΦX_i = (x̄_1, ..., x̄_m)^T. Let f_{Σ_i}(x̄_j) = exp{−1/2 x̄_j^T Σ_i^{−1} x̄_j}/|Σ_i|^{1/2}(2π)^{p/2} be the density for Gaussian distribution N(0, Σ_i). Before modification, the density function f_{Σ_i}(X̄) is

f_{Σ_i}(X̄) = ∏_{j=1}^m f_{Σ_i}(x̄_j).                    (11)

We focus on defining two procedures that lead to both distributional and differential types of privacy. Indeed, the proof of Theorem 4.6 applies to both, as the distance metric V(X_1, X_2) does not specify how many rows X_1 and X_2 differ in. We use Δ_max as a shorthand for Δ_max(S_n) when it is clear.

**Procedure 4.1. (TRUNCATION OF THE TAIL FOR RANDOM VECTORS IN R^p)** We require Φ to be an independent random draw each time we generate a X̄ for compression (or when we apply it to the same dataset for handling a truncation event). W.l.o.g, we choose Σ_1 to be a reference point. Now we only examine output databases X̄ ∈ R^{m×p} such that for C = √(2(C_1 + C_2)), where C_1 ≈ 2.5 and C_2 ≈ 7.7,

max_{j,k} |(X̄^T X̄/m)_{jk} − Σ_1(j, k)| ≤ C√(ln 2np/m) + Δ_max,                    (12)

where Δ_max(S_n) = O(√(log n/n)). Algorithmically, one can imagine that for an input X, each time we see an output X̄ = ΦX that does not satisfy our need in the sense of (12), we throw the output database X̄ away, and generate a new random draw Φ' to calculate Φ'X and repeat until Φ'X indeed satisfies (12). We also note that the adversary neither sees the databases we throw away nor finds out that we did so.

Given X_i ∈ S_n, let P_{Σ_i} be the probability measure over random outcomes of ΦX_i. Upon truncation,

**Procedure 4.2. (RENORMALIZATION)** We set f'_{Σ_i}(X̄) = 0 for all X̄ ∈ R^{m×p} belonging to set E, where

E = {X̄ : max_{j,k} |(X̄^T X̄/m)_{jk} − Σ_1(j, k)| > C√(ln 2np/m) + Δ_max},                    (13)

corresponds to the bad events that we truncate from the outcome in Procedure 4.1; We then renormalize the density as in (11) on the remaining X̄ that satisfies (12) to obtain:

f'_{Σ_i}(X̄) = f_{Σ_i}(X̄)/(1 − P_{Σ_i}[E]).                    (14)

**Remark 4.3.** Hence f'_{Σ_1}(X̄)/f'_{Σ_2}(X̄) = f_{Σ_1}(X̄)(1−P_{Σ_2}[E])/(f_{Σ_2}(X̄)(1−P_{Σ_1}[E])), which changes α(m, δ) that we bounded below based on original density prior to truncation of E by a constant in the order of ln(1+ε) = O(ε), where ε = O(1/n^2). Hence we safely ignore this normalization issue given it only changes α(m, δ) by O(1/n^2).

The following lemma bounds the probability on the events that we truncate in Procedure 4.1. Proof of Lemma 4.4 appears in Section B.

**Lemma 4.4.** According to any individual probability measure P_{Σ_i} which corresponds to the sample space for outcomes of ΦX_i, suppose that the columns of (X_i) have been normalized to have ‖(X_i^T)_j‖_2^2 = n, ∀i, j = 1, ..., p and m ≥ 2(C_1 + C_2)ln 2np, then for E as defined in (13), P_{Σ_i}[E] ≤ 1/n^2.

As hinted after Definition 2.4 regarding distributional privacy, we can think of the input data as coming from a distribution, such that Δ_max(S_n) in (5) can be derived with a typical large deviation bound between the sample and population covariances. For example, for multivariate Gaussian,

**Lemma 4.5.** ([19]) Suppose (X_i)_j ~ N(0, Σ*), ∀j = 1, ..., n for all X_i ∈ S_n, then Δ_max(S_n) = O_P(√(log p/n)).

We now state the main result of this section. Proof of Theorem 4.6 appears in Section C.

**Theorem 4.6.** Under Assumption 1, let m and ‖(X_i^T)_j‖_2, ∀i, j satisfy conditions in Lemma 4.4. By truncating a subset of measure at most 1/n^2 from each P_{Σ_i}, in the sense of Procedure 4.1 and renormalizing the density functions according to Procedure 4.2, we have

α(m, δ) ≤ (mp‖Δ‖_F)/(2λ_min(Σ_i)λ_min(Σ_1)) · (C√(ln 2np/m) + Δ_max + (2‖Δ‖_F‖Σ_1‖_2^2)/(pλ_min(Σ_i)λ_min(Σ_1))) + o(1)                    (15)

when comparing all X_i ∈ S_n with X_1, where ‖Γ̂‖_F is bounded as in (7) for i = 2.

**Remark 4.7.** While the theorem only states results for comparing f_{Σ_1}(·)/f_{Σ_i}(·), we note ∀X_k, X_j ∈ S_n,

|ln(f_{Σ_k}(·)/f_{Σ_j}(·))| = |ln(f_{Σ_k}(·)/f_{Σ_1}(·) · f_{Σ_1}(·)/f_{Σ_j}(·))| ≤ |ln(f_{Σ_1}(·)/f_{Σ_k}(·))| + |ln(f_{Σ_1}(·)/f_{Σ_j}(·))|,

which is simply a sum of terms as bounded as in (15).

---

### النسخة العربية

في هذا القسم، نوضح كيف يمكننا تعديل أحداث المخرجات X̄ لإخفاء بعض الأحداث ذات الذيل الكبير بشكل فعال. نوضح كيف ترتبط أحداث الذيل هذه بنوع معين من الفائدة. بالنظر إلى X_i، دع X̄ = ΦX_i = (x̄_1، ...، x̄_m)^T. دع f_{Σ_i}(x̄_j) = exp{−1/2 x̄_j^T Σ_i^{−1} x̄_j}/|Σ_i|^{1/2}(2π)^{p/2} تكون الكثافة للتوزيع الغاوسي N(0، Σ_i). قبل التعديل، دالة الكثافة f_{Σ_i}(X̄) هي

f_{Σ_i}(X̄) = ∏_{j=1}^m f_{Σ_i}(x̄_j).                    (11)

نركز على تحديد إجراءين يؤديان إلى أنواع توزيعية وتفاضلية من الخصوصية. في الواقع، ينطبق برهان المبرهنة 4.6 على كليهما، حيث أن مقياس المسافة V(X_1، X_2) لا يحدد عدد الصفوف التي تختلف فيها X_1 و X_2. نستخدم Δ_max كاختصار لـ Δ_max(S_n) عندما يكون واضحًا.

**الإجراء 4.1. (اقتطاع الذيل للمتجهات العشوائية في R^p)** نطلب أن تكون Φ سحبًا عشوائيًا مستقلاً في كل مرة نولد فيها X̄ للضغط (أو عندما نطبقه على نفس مجموعة البيانات للتعامل مع حدث اقتطاع). دون فقدان العمومية، نختار Σ_1 لتكون نقطة مرجعية. الآن نفحص فقط قواعد بيانات المخرجات X̄ ∈ R^{m×p} بحيث لـ C = √(2(C_1 + C_2))، حيث C_1 ≈ 2.5 و C_2 ≈ 7.7،

max_{j,k} |(X̄^T X̄/m)_{jk} − Σ_1(j، k)| ≤ C√(ln 2np/m) + Δ_max،                    (12)

حيث Δ_max(S_n) = O(√(log n/n)). خوارزميًا، يمكن للمرء أن يتخيل أنه لإدخال X، في كل مرة نرى فيها مخرجًا X̄ = ΦX لا يلبي حاجتنا بمعنى (12)، نتخلص من قاعدة بيانات المخرجات X̄، ونولد سحبًا عشوائيًا جديدًا Φ' لحساب Φ'X ونكرر حتى يلبي Φ'X بالفعل (12). نلاحظ أيضًا أن الخصم لا يرى قواعد البيانات التي نتخلص منها ولا يكتشف أننا فعلنا ذلك.

بالنظر إلى X_i ∈ S_n، دع P_{Σ_i} تكون مقياس الاحتمال على النتائج العشوائية لـ ΦX_i. عند الاقتطاع،

**الإجراء 4.2. (إعادة التطبيع)** نضع f'_{Σ_i}(X̄) = 0 لجميع X̄ ∈ R^{m×p} المنتمية إلى المجموعة E، حيث

E = {X̄ : max_{j,k} |(X̄^T X̄/m)_{jk} − Σ_1(j، k)| > C√(ln 2np/m) + Δ_max}،                    (13)

يتوافق مع الأحداث السيئة التي نقتطعها من النتيجة في الإجراء 4.1؛ ثم نعيد تطبيع الكثافة كما في (11) على X̄ المتبقي الذي يلبي (12) للحصول على:

f'_{Σ_i}(X̄) = f_{Σ_i}(X̄)/(1 − P_{Σ_i}[E]).                    (14)

**ملاحظة 4.3.** وبالتالي f'_{Σ_1}(X̄)/f'_{Σ_2}(X̄) = f_{Σ_1}(X̄)(1−P_{Σ_2}[E])/(f_{Σ_2}(X̄)(1−P_{Σ_1}[E]))، والتي تغير α(m، δ) التي حددناها أدناه بناءً على الكثافة الأصلية قبل اقتطاع E بثابت بترتيب ln(1+ε) = O(ε)، حيث ε = O(1/n^2). وبالتالي نتجاهل بأمان مشكلة إعادة التطبيع هذه نظرًا لأنها تغير فقط α(m، δ) بمقدار O(1/n^2).

المبرهنة المساعدة التالية تحد احتمال الأحداث التي نقتطعها في الإجراء 4.1. يظهر برهان المبرهنة المساعدة 4.4 في القسم B.

**المبرهنة المساعدة 4.4.** وفقًا لأي مقياس احتمال فردي P_{Σ_i} والذي يتوافق مع فضاء العينة لنتائج ΦX_i، افترض أن أعمدة (X_i) قد تم تطبيعها لتكون ‖(X_i^T)_j‖_2^2 = n، ∀i، j = 1، ...، p و m ≥ 2(C_1 + C_2)ln 2np، إذن لـ E كما هو محدد في (13)، P_{Σ_i}[E] ≤ 1/n^2.

كما ألمحنا بعد التعريف 2.4 فيما يتعلق بالخصوصية التوزيعية، يمكننا أن نفكر في بيانات الإدخال على أنها قادمة من توزيع، بحيث يمكن اشتقاق Δ_max(S_n) في (5) مع حد انحراف كبير نموذجي بين التباينات المشتركة للعينة والسكان. على سبيل المثال، لغاوسي متعدد المتغيرات،

**المبرهنة المساعدة 4.5.** ([19]) افترض (X_i)_j ~ N(0، Σ*)، ∀j = 1، ...، n لجميع X_i ∈ S_n، إذن Δ_max(S_n) = O_P(√(log p/n)).

نذكر الآن النتيجة الرئيسية لهذا القسم. يظهر برهان المبرهنة 4.6 في القسم C.

**المبرهنة 4.6.** تحت الافتراض 1، دع m و ‖(X_i^T)_j‖_2، ∀i، j تحقق الشروط في المبرهنة المساعدة 4.4. عن طريق اقتطاع مجموعة فرعية من المقياس 1/n^2 على الأكثر من كل P_{Σ_i}، بمعنى الإجراء 4.1 وإعادة تطبيع دوال الكثافة وفقًا للإجراء 4.2، لدينا

α(m، δ) ≤ (mp‖Δ‖_F)/(2λ_min(Σ_i)λ_min(Σ_1)) · (C√(ln 2np/m) + Δ_max + (2‖Δ‖_F‖Σ_1‖_2^2)/(pλ_min(Σ_i)λ_min(Σ_1))) + o(1)                    (15)

عند مقارنة جميع X_i ∈ S_n مع X_1، حيث ‖Γ̂‖_F محدود كما في (7) لـ i = 2.

**ملاحظة 4.7.** بينما تذكر المبرهنة فقط النتائج لمقارنة f_{Σ_1}(·)/f_{Σ_i}(·)، نلاحظ ∀X_k، X_j ∈ S_n،

|ln(f_{Σ_k}(·)/f_{Σ_j}(·))| = |ln(f_{Σ_k}(·)/f_{Σ_1}(·) · f_{Σ_1}(·)/f_{Σ_j}(·))| ≤ |ln(f_{Σ_1}(·)/f_{Σ_k}(·))| + |ln(f_{Σ_1}(·)/f_{Σ_j}(·))|،

والذي هو ببساطة مجموع الحدود المحدودة كما في (15).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** tail truncation, renormalization, bad events, measure truncation, large deviation bound
- **Equations:** 5 equations (11-15)
- **Citations:** Reference [19]
- **Special handling:** Procedures formatted clearly; mathematical proofs and bounds preserved

### Quality Metrics

- Semantic equivalence: 0.85
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.85
