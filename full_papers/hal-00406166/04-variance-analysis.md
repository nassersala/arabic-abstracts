# Section 3: Variance and Other Stories
## القسم 3: التباين وقصص أخرى

**Section:** variance-analysis
**Translation Quality:** 0.85
**Glossary Terms Used:** variance, expectation, standard error, Laplace method, integral, asymptotic analysis, bias correction

---

### English Version

## 3.1 Variance analysis

The estimation of the variance of the indicator, namely V_n(Z) = E_n(Z²) - E²_n(Z), serves to justify Part (ii) of our main Theorem 1, and hence characterizes the accuracy of HYPERLOGLOG. Since the analysis develops along lines that are entirely parallel to those of Section 2, we content ourselves with a brief indication of the main steps of the proof.

The starting point is an expression of the moment of order 2 of the indicator Z under the Poisson model,

$$\mathbb{E}_P(\lambda)(Z^2) = \sum_{k_1,...,k_m \geq 1} \left( \frac{1}{\sum_{j=1}^m 2^{-k_j}} \right)^2 \prod_{j=1}^{m} g\left(\frac{\lambda}{m}2^{-k_j}\right), \quad (23)$$

which is the analogue of (5). Then, the use of the identity

$$\frac{1}{a^2} = \int_0^\infty t e^{-at} dt$$

leads to the integral form (compare with (9))

$$\mathbb{E}_P(\lambda)(Z^2) = \frac{K(\lambda)}{m}, \quad \text{where } K(x) := x^2 \int_0^{+\infty} u G(x,xu)^m du. \quad (24)$$

The integral being very close to the one that represents E_P(λ)(Z), the analysis of the integrand available from Lemma 1 can be entirely recycled. We then find

$$K(x) = x^2 \int_0^1 u f(u)^m du + \varepsilon'_m(x) + o(1), \quad (25)$$

where ε'(x) is a small oscillating function, implying

$$\mathbb{V}_P(\lambda)(Z) = \lambda^2 \left( \int_0^1 u f(u)^m du - \left[ \int_0^1 f(u)^m du \right]^2 \right) + \varepsilon''(\lambda) + o(1) \quad (26)$$

(with ε'' small), which constitutes the analogue of Proposition 2.

The last estimate (26) can then be subjected to depoissonization (with a proof similar to that of Proposition 3), to the effect that

$$\mathbb{V}_n(Z) = \mathbb{V}_P(n)(Z) + O(n). \quad (27)$$

This shows that the standard error, measured by $\frac{1}{n}\sqrt{\mathbb{V}_n(E)}$, is, for each fixed m, asymptotic to a constant as n → ∞, neglecting as we may tiny fluctuations. The stronger property that this constant is of the form β_m/√m (with β_m bounded) is established in the next subsection.

## 3.2 Constants

There only remains to discuss the proportionality constants that determine the shapes of the bias-correction constant α_m specified in (3) and of the standard-error constant β_m of the statement of Theorem 1. Define the special integrals

$$J_s(m) = \int_0^1 u^s f(u)^m du.$$

We have from Equations (3) and (26)

$$\alpha_m = \frac{1}{m J_0(m)}, \quad \beta_m = \sqrt{m} \sqrt{\frac{J_1(m)}{J_0(m)^2} - 1}.$$

The integrals J_s(m) are routinely amenable to the Laplace method [8]:

$$\begin{cases}
J_0(m) = \frac{2 \log 2}{m} \left[ 1 + \frac{1}{m}(3 \log 2 - 1) + O(m^{-2}) \right] \\
J_1(m) = \frac{(2 \log 2)^2}{m^2} \left[ 1 + \frac{3}{m}(3 \log 2 - 1) + O(m^{-2}) \right]
\end{cases} \quad (28)$$

Thus the bias correction α_m and the variance constant β_m satisfy

$$\alpha_m \sim \frac{1}{2 \log 2} ≈ 0.72134, \quad \beta_m \sim \sqrt{3 \log 2 - 1} ≈ 1.03896 \quad (m \to +\infty), \quad (29)$$

which turn out to provide good numerical approximations, even for relatively low values of m. These estimates imply in particular that β_m remains bounded for all m ≥ 3, which concludes the proof of Theorem 1.

Additionally, we observe that the constants α_m, β_m belong to an interesting arithmetic class: the integrals J_0(m), J_1(m) are expressible as rational combinations of L = log 2, values of the Riemann zeta function at the integers, and polylogarithms evaluated at 1/2. For instance:

$$J_0(2) = \frac{2\zeta(2)}{6L} - 2, \quad J_0(3) = \frac{3\zeta(3)}{4L} - \frac{3}{2},$$

and

$$J_0(4) = \frac{1}{L^4} \left[ 4\zeta(4) - 15\zeta(2)L^2 - 3L^4 - 21L\zeta(3) - 24 \text{Li}_4\left(\frac{1}{2}\right) \right], \quad \text{where } \text{Li}_r(z) := \sum_{n \geq 1} \frac{z^n}{n^r}.$$

They can thereby be computed to great accuracy.

---

### النسخة العربية

## 3.1 تحليل التباين

يخدم تقدير تباين المؤشر، وهو V_n(Z) = E_n(Z²) - E²_n(Z)، تبرير الجزء (ii) من النظرية الرئيسية 1، وبالتالي يميز دقة HYPERLOGLOG. بما أن التحليل يتطور على خطوط موازية تماماً لتلك الموجودة في القسم 2، نكتفي بإشارة موجزة إلى الخطوات الرئيسية للبرهان.

نقطة البداية هي تعبير عن عزم الرتبة 2 للمؤشر Z تحت نموذج بواسون،

$$\mathbb{E}_P(\lambda)(Z^2) = \sum_{k_1,...,k_m \geq 1} \left( \frac{1}{\sum_{j=1}^m 2^{-k_j}} \right)^2 \prod_{j=1}^{m} g\left(\frac{\lambda}{m}2^{-k_j}\right), \quad (23)$$

وهو نظير (5). ثم، استخدام الهوية

$$\frac{1}{a^2} = \int_0^\infty t e^{-at} dt$$

يؤدي إلى الشكل التكاملي (قارن مع (9))

$$\mathbb{E}_P(\lambda)(Z^2) = \frac{K(\lambda)}{m}, \quad \text{حيث } K(x) := x^2 \int_0^{+\infty} u G(x,xu)^m du. \quad (24)$$

نظراً لأن التكامل قريب جداً من ذلك الذي يمثل E_P(λ)(Z)، يمكن إعادة تدوير تحليل التكامل المتاح من اللمة 1 بالكامل. نجد حينئذ

$$K(x) = x^2 \int_0^1 u f(u)^m du + \varepsilon'_m(x) + o(1), \quad (25)$$

حيث ε'(x) دالة متذبذبة صغيرة، مما يعني

$$\mathbb{V}_P(\lambda)(Z) = \lambda^2 \left( \int_0^1 u f(u)^m du - \left[ \int_0^1 f(u)^m du \right]^2 \right) + \varepsilon''(\lambda) + o(1) \quad (26)$$

(مع ε'' صغيرة)، والتي تشكل نظير القضية 2.

يمكن بعد ذلك إخضاع التقدير الأخير (26) لإزالة البواسونية (مع برهان مشابه لبرهان القضية 3)، بحيث

$$\mathbb{V}_n(Z) = \mathbb{V}_P(n)(Z) + O(n). \quad (27)$$

هذا يُظهر أن الخطأ المعياري، المقاس بـ $\frac{1}{n}\sqrt{\mathbb{V}_n(E)}$، هو، لكل m ثابت، مقارب لثابت عندما n → ∞، متجاهلين كما يمكننا التقلبات الصغيرة. الخاصية الأقوى أن هذا الثابت من الشكل β_m/√m (مع β_m محدودة) يتم إثباتها في القسم الفرعي التالي.

## 3.2 الثوابت

يبقى فقط مناقشة ثوابت التناسب التي تحدد أشكال ثابت تصحيح الانحياز α_m المحدد في (3) وثابت الخطأ المعياري β_m من بيان النظرية 1. نعرّف التكاملات الخاصة

$$J_s(m) = \int_0^1 u^s f(u)^m du.$$

لدينا من المعادلات (3) و (26)

$$\alpha_m = \frac{1}{m J_0(m)}, \quad \beta_m = \sqrt{m} \sqrt{\frac{J_1(m)}{J_0(m)^2} - 1}.$$

التكاملات J_s(m) قابلة بشكل روتيني لطريقة لابلاس [8]:

$$\begin{cases}
J_0(m) = \frac{2 \log 2}{m} \left[ 1 + \frac{1}{m}(3 \log 2 - 1) + O(m^{-2}) \right] \\
J_1(m) = \frac{(2 \log 2)^2}{m^2} \left[ 1 + \frac{3}{m}(3 \log 2 - 1) + O(m^{-2}) \right]
\end{cases} \quad (28)$$

وبالتالي فإن تصحيح الانحياز α_m وثابت التباين β_m يحققان

$$\alpha_m \sim \frac{1}{2 \log 2} ≈ 0.72134, \quad \beta_m \sim \sqrt{3 \log 2 - 1} ≈ 1.03896 \quad (m \to +\infty), \quad (29)$$

والتي تبين أنها توفر تقريبات عددية جيدة، حتى لقيم منخفضة نسبياً من m. تعني هذه التقديرات على وجه الخصوص أن β_m تظل محدودة لجميع m ≥ 3، مما يختتم برهان النظرية 1.

بالإضافة إلى ذلك، نلاحظ أن الثوابت α_m، β_m تنتمي إلى فئة حسابية مثيرة للاهتمام: التكاملات J_0(m)، J_1(m) قابلة للتعبير كتركيبات نسبية من L = log 2، وقيم دالة زيتا لريمان عند الأعداد الصحيحة، واللوغاريتمات المتعددة المقيمة عند 1/2. على سبيل المثال:

$$J_0(2) = \frac{2\zeta(2)}{6L} - 2, \quad J_0(3) = \frac{3\zeta(3)}{4L} - \frac{3}{2},$$

و

$$J_0(4) = \frac{1}{L^4} \left[ 4\zeta(4) - 15\zeta(2)L^2 - 3L^4 - 21L\zeta(3) - 24 \text{Li}_4\left(\frac{1}{2}\right) \right], \quad \text{حيث } \text{Li}_r(z) := \sum_{n \geq 1} \frac{z^n}{n^r}.$$

يمكن بالتالي حسابها بدقة كبيرة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** Laplace method (طريقة لابلاس), Riemann zeta function (دالة زيتا لريمان), polylogarithm (اللوغاريتم المتعدد), moment (عزم)
- **Equations:** Multiple mathematical equations with LaTeX notation
- **Citations:** [8] (de Bruijn - Asymptotic Methods in Analysis)
- **Special handling:** Mathematical proofs and asymptotic expansions

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.89
- Readability: 0.83
- Glossary consistency: 0.84
- **Overall section score:** 0.85
