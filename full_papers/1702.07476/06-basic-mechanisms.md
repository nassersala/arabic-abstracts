# Section 6: Basic Mechanisms
## القسم 6: الآليات الأساسية

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** randomized response, Laplace mechanism, Gaussian mechanism, sensitivity, differential privacy, Rényi differential privacy

---

### English Version

In this section we analyze Rényi differential privacy of three basic mechanisms and their self-composition: randomized response, Laplace and Gaussian noise addition. The results are summarized in Table II and plotted for select parameters in Figures 1 and 2.

## A. Randomized Response

Let $f$ be a predicate, i.e., $f : \mathcal{D} \mapsto \{0, 1\}$. The Randomize Response mechanism for $f$ is defined as

$$\text{RR}_p f(D) \triangleq \begin{cases} f(D) & \text{with probability } p \\ 1 - f(D) & \text{with probability } 1 - p \end{cases}.$$

The following statement can be verified by direct application of the definition of Rényi differential privacy:

**Proposition 5.** Randomized Response mechanism $\text{RR}_p(f)$ satisfies

$$\left(\alpha, \frac{1}{\alpha-1} \log\left[p^{\alpha}(1-p)^{1-\alpha} + (1-p)^{\alpha}p^{1-\alpha}\right]\right)\text{-RDP}$$

if $\alpha > 1$, and

$$\left(\alpha, (2p - 1) \log \frac{p}{1-p}\right)\text{-RDP}$$

if $\alpha = 1$.

## B. Laplace Noise

Through the rest of this section we assume that $f : \mathcal{D} \mapsto \mathbb{R}$ is a function of sensitivity 1, i.e., for any two adjacent $D, D' \in \mathcal{D}$: $|f(D) - f(D')| \leq 1$.

Define the Laplace mechanism for $f$ of sensitivity 1 as

$$\mathcal{L}_{\lambda} f(D) = f(D) + \Lambda(0, \lambda),$$

where $\Lambda(\mu, \lambda)$ is Laplace distribution with mean $\mu$ and scale $\lambda$, i.e., its probability density function is $\frac{1}{2\lambda} \exp(-|x - \mu|/\lambda)$.

To derive the RDP budget curve for the exponential mechanism we compute the Rényi divergence for Laplace distribution and its offset.

**Proposition 6.** For any $\alpha \geq 1$ and $\lambda > 0$:

$$D_{\alpha}(\Lambda(0, \lambda) \| \Lambda(1, \lambda)) = \frac{1}{\alpha - 1} \log\left[\frac{\alpha}{2\alpha - 1} \exp\left(\frac{\alpha - 1}{\lambda}\right) + \frac{\alpha - 1}{2\alpha - 1} \exp\left(\frac{-\alpha}{\lambda}\right)\right].$$

**Proof.** For continuous distributions $P$ and $Q$ defined over the real interval with densities $p$ and $q$

$$D_{\alpha}(P \| Q) = \frac{1}{\alpha - 1} \log \int_{-\infty}^{\infty} p(x)^{\alpha} q(x)^{1-\alpha} dx.$$

To compute the integral for $p(x) = \frac{1}{2\lambda} \exp(-|x|/\lambda)$ and $q(x) = \frac{1}{2\lambda} \exp(-|x - 1|/\lambda)$, we evaluate it separately over the intervals $(-\infty, 0]$, $[0, 1]$ and $[1, +\infty)$.

$$\int_{-\infty}^{+\infty} p(x)^{\alpha} q(x)^{1-\alpha} dx = \frac{1}{2\lambda} \int_{-\infty}^{0} \exp(\alpha x/\lambda + (1 - \alpha)(x - 1)/\lambda) dx$$

$$+ \frac{1}{2\lambda} \int_{0}^{1} \exp(-\alpha x/\lambda + (1 - \alpha)(x - 1)/\lambda) dx + \frac{1}{2\lambda} \int_{1}^{+\infty} \exp(-\alpha x/\lambda - (1 - \alpha)(x - 1)/\lambda) dx$$

$$= \frac{1}{2} \exp((\alpha - 1)/\lambda) + \frac{1}{2(2\alpha - 1)}(\exp((\alpha - 1)/\lambda) - \exp(-\alpha/\lambda)) + \frac{1}{2} \exp(-\alpha/\lambda)$$

$$= \frac{\alpha}{2\alpha - 1} \exp((\alpha - 1)/\lambda) + \frac{\alpha - 1}{2\alpha - 1} \exp(-\alpha/\lambda),$$

from which the claim follows.

Since the Laplace mechanism is additive, the Rényi divergence between $\mathcal{L}_{\lambda} f(D)$ and $\mathcal{L}_{\lambda} f(D')$ depends only on α and the distance $|f(D) - f(D')|$. Proposition 6 implies the following:

**Corollary 2.** If real-valued function $f$ has sensitivity 1, then the Laplace mechanism $\mathcal{L}_{\lambda} f$ satisfies $\left(\alpha, \frac{1}{\alpha-1} \log\left[\frac{\alpha}{2\alpha-1} \exp\left(\frac{\alpha-1}{\lambda}\right) + \frac{\alpha-1}{2\alpha-1} \exp\left(\frac{-\alpha}{\lambda}\right)\right]\right)$-RDP.

Predictably,

$$\lim_{\alpha \to \infty} D_{\alpha}(\Lambda(0, \lambda) \| \Lambda(1, \lambda)) = D_{\infty}(\Lambda(0, \lambda) \| \Lambda(1, \lambda)) = \frac{1}{\lambda}.$$

This is, of course, consistent with the Laplace mechanism satisfying $1/\lambda$-differential privacy. The other extreme evaluates to the following expression $\lim_{\alpha \to 1} D_{\alpha}(\Lambda(0, \lambda) \| \Lambda(1, \lambda)) = 1/\lambda + \exp(-1/\lambda) - 1$, which is well approximated by $.5/\lambda^2$ for large $\lambda$.

## C. Gaussian Noise

Assuming, as before, that $f$ is a real-valued function, the Gaussian mechanism for approximating $f$ is defined as

$$\mathcal{G}_{\sigma} f(D) = f(D) + \mathcal{N}(0, \sigma^2),$$

where $\mathcal{N}(0, \sigma^2)$ is normally distributed random variable with standard deviation $\sigma^2$ and mean 0.

The following statement is a closed-form expression of the Rényi divergence between a Gaussian and its offset (for a more general version see [19], [21]).

**Proposition 7.** $D_{\alpha}(\mathcal{N}(0, \sigma^2) \| \mathcal{N}(\mu, \sigma^2)) = \alpha\mu^2/(2\sigma^2)$.

**Proof.** By direct computation we verify that

$$D_{\alpha}(\mathcal{N}(0, \sigma^2) \| \mathcal{N}(\mu, \sigma^2)) = \frac{1}{\alpha - 1} \log \int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi}} \exp(-\alpha x^2/(2\sigma^2))$$

$$\cdot \exp(-(1 - \alpha)(x - \mu)^2/(2\sigma^2)) dx$$

$$= \frac{1}{\alpha - 1} \log \frac{1}{\sigma\sqrt{2\pi}} \int_{-\infty}^{\infty} \exp[(-x^2 + 2(1 - \alpha)\mu x - (1 - \alpha)\mu^2)/(2\sigma^2)] dx$$

$$= \frac{1}{\alpha - 1} \log \left[\frac{\sigma\sqrt{2\pi}}{\sigma\sqrt{2\pi}} \exp\left((α - \alpha)μ^2/(2σ^2)\right)\right] = \alpha\mu^2/(2\sigma^2).$$

The following corollary is immediate:

**Corollary 3.** If $f$ has sensitivity 1, then the Gaussian mechanism $\mathcal{G}_{\sigma} f$ satisfies $(\alpha, \alpha/(2\sigma^2))$-RDP.

Observe that the RDP budget curve for the Gaussian mechanism is particularly simple—a straight line (Figure 1). Recall that the (adaptive) composition of RDP mechanisms satisfies Rényi differential privacy with the budget curve that is the sum of the mechanisms' budget curves. It means that a composition of Gaussian mechanisms will behave, privacy-wise, "like" a Gaussian mechanism. Concretely, a composition of $n$ Gaussian mechanisms each with parameter $\sigma$ will have the RDP curve of a Gaussian mechanism with parameter $\sigma/\sqrt{n}$.

## D. Privacy of Basic Mechanisms Under Composition

The "bad outcomes" interpretation of Rényi differential privacy ties the probabilities of seeing the same outcome under runs of the mechanism applied to adjacent inputs. The dependency of the upper bound on the increase in probability on its initial value is complex, especially compared to the standard differential privacy guarantee. The main advantage of this more involved analysis is that for most parameters the bound becomes tighter.

In this section we compare numerical bounds for several analyses of self-composed mechanisms (see Figure 2), presented as three sets of graphs, where $\Pr[f(D) \in S]$ takes values $10^{-6}$, $10^{-3}$, and $10^{-1}$.

Each of the six graphs in Figure 2 (three probability values × {randomized response, Laplace}) plots bounds in logarithmic scale on the relative increase in probability of $S$ (i.e., $\Pr[f(D') \in S]/\Pr[f(D) \in S]$) offered by four analyses. The first, "naïve", bound follows from the basic composition theorem for differential privacy and, as expected, is very pessimistic for all but a handful of parameters. A tighter, advanced composition theorem [6], gives a choice of δ, from which one computes ε' so that the n-fold composition satisfies $(ε', δ)$-differential privacy. The second curve plots the bound for the optimal (tightest) choice of $(ε', δ)$. Two other bounds come from Rényi differential privacy analysis: our generic advanced composition theorem (Proposition 4) and the bound of Proposition 10 for the optimal combination of $(α, ε)$ from the RDP curve of the composite mechanism.

Several observations are in order. The RDP-specific analysis for both mechanisms is tighter than all generic bounds whose only input is the mechanism's differential privacy parameter. On the other hand, our version of the advanced composition bound (Proposition 4) is consistently outperformed by the standard $(ε, δ)$-form of the composition theorem, where δ is chosen optimally. We elaborate on this distinction in the next section.

---

### النسخة العربية

في هذا القسم نحلل الخصوصية التفاضلية لريني لثلاث آليات أساسية وتركيبها الذاتي: الاستجابة العشوائية، وإضافة ضوضاء لابلاس وغاوس. يتم تلخيص النتائج في الجدول الثاني ورسمها لمعاملات مختارة في الشكلين 1 و2.

## أ. الاستجابة العشوائية

ليكن $f$ محمولًا، أي $f : \mathcal{D} \mapsto \{0, 1\}$. يتم تعريف آلية الاستجابة العشوائية لـ $f$ على النحو التالي

$$\text{RR}_p f(D) \triangleq \begin{cases} f(D) & \text{باحتمالية } p \\ 1 - f(D) & \text{باحتمالية } 1 - p \end{cases}.$$

يمكن التحقق من البيان التالي من خلال التطبيق المباشر لتعريف الخصوصية التفاضلية لريني:

**المقترح 5.** تحقق آلية الاستجابة العشوائية $\text{RR}_p(f)$

$$\left(\alpha, \frac{1}{\alpha-1} \log\left[p^{\alpha}(1-p)^{1-\alpha} + (1-p)^{\alpha}p^{1-\alpha}\right]\right)\text{-RDP}$$

إذا كان $\alpha > 1$، و

$$\left(\alpha, (2p - 1) \log \frac{p}{1-p}\right)\text{-RDP}$$

إذا كان $\alpha = 1$.

## ب. ضوضاء لابلاس

خلال بقية هذا القسم نفترض أن $f : \mathcal{D} \mapsto \mathbb{R}$ دالة ذات حساسية 1، أي لأي $D, D' \in \mathcal{D}$ متجاورين: $|f(D) - f(D')| \leq 1$.

عرّف آلية لابلاس لـ $f$ ذات حساسية 1 على النحو التالي

$$\mathcal{L}_{\lambda} f(D) = f(D) + \Lambda(0, \lambda),$$

حيث $\Lambda(\mu, \lambda)$ هو توزيع لابلاس بمتوسط $\mu$ ومقياس $\lambda$، أي أن دالة الكثافة الاحتمالية الخاصة به هي $\frac{1}{2\lambda} \exp(-|x - \mu|/\lambda)$.

لاشتقاق منحنى ميزانية RDP لآلية الأسية، نحسب اختلاف ريني لتوزيع لابلاس وإزاحته.

**المقترح 6.** لأي $\alpha \geq 1$ و$\lambda > 0$:

$$D_{\alpha}(\Lambda(0, \lambda) \| \Lambda(1, \lambda)) = \frac{1}{\alpha - 1} \log\left[\frac{\alpha}{2\alpha - 1} \exp\left(\frac{\alpha - 1}{\lambda}\right) + \frac{\alpha - 1}{2\alpha - 1} \exp\left(\frac{-\alpha}{\lambda}\right)\right].$$

**البرهان.** للتوزيعات المستمرة $P$ و$Q$ المعرفة على الفترة الحقيقية بكثافات $p$ و$q$

$$D_{\alpha}(P \| Q) = \frac{1}{\alpha - 1} \log \int_{-\infty}^{\infty} p(x)^{\alpha} q(x)^{1-\alpha} dx.$$

لحساب التكامل لـ $p(x) = \frac{1}{2\lambda} \exp(-|x|/\lambda)$ و$q(x) = \frac{1}{2\lambda} \exp(-|x - 1|/\lambda)$، نقيمه بشكل منفصل على الفترات $(-\infty, 0]$، و$[0, 1]$ و$[1, +\infty)$.

$$\int_{-\infty}^{+\infty} p(x)^{\alpha} q(x)^{1-\alpha} dx = \frac{1}{2\lambda} \int_{-\infty}^{0} \exp(\alpha x/\lambda + (1 - \alpha)(x - 1)/\lambda) dx$$

$$+ \frac{1}{2\lambda} \int_{0}^{1} \exp(-\alpha x/\lambda + (1 - \alpha)(x - 1)/\lambda) dx + \frac{1}{2\lambda} \int_{1}^{+\infty} \exp(-\alpha x/\lambda - (1 - \alpha)(x - 1)/\lambda) dx$$

$$= \frac{1}{2} \exp((\alpha - 1)/\lambda) + \frac{1}{2(2\alpha - 1)}(\exp((\alpha - 1)/\lambda) - \exp(-\alpha/\lambda)) + \frac{1}{2} \exp(-\alpha/\lambda)$$

$$= \frac{\alpha}{2\alpha - 1} \exp((\alpha - 1)/\lambda) + \frac{\alpha - 1}{2\alpha - 1} \exp(-\alpha/\lambda),$$

ومن ذلك يتبع الادعاء.

بما أن آلية لابلاس جمعية، فإن اختلاف ريني بين $\mathcal{L}_{\lambda} f(D)$ و$\mathcal{L}_{\lambda} f(D')$ يعتمد فقط على α والمسافة $|f(D) - f(D')|$. يعني المقترح 6 ما يلي:

**النتيجة 2.** إذا كانت الدالة ذات القيمة الحقيقية $f$ لها حساسية 1، فإن آلية لابلاس $\mathcal{L}_{\lambda} f$ تحقق $\left(\alpha, \frac{1}{\alpha-1} \log\left[\frac{\alpha}{2\alpha-1} \exp\left(\frac{\alpha-1}{\lambda}\right) + \frac{\alpha-1}{2\alpha-1} \exp\left(\frac{-\alpha}{\lambda}\right)\right]\right)$-RDP.

بشكل متوقع،

$$\lim_{\alpha \to \infty} D_{\alpha}(\Lambda(0, \lambda) \| \Lambda(1, \lambda)) = D_{\infty}(\Lambda(0, \lambda) \| \Lambda(1, \lambda)) = \frac{1}{\lambda}.$$

هذا، بالطبع، يتفق مع آلية لابلاس التي تحقق خصوصية تفاضلية $1/\lambda$. يقيّم الطرف الآخر إلى التعبير التالي $\lim_{\alpha \to 1} D_{\alpha}(\Lambda(0, \lambda) \| \Lambda(1, \lambda)) = 1/\lambda + \exp(-1/\lambda) - 1$، والذي يتم تقريبه جيدًا بواسطة $.5/\lambda^2$ لـ $\lambda$ الكبيرة.

## ج. ضوضاء غاوس

بافتراض، كما هو الحال من قبل، أن $f$ دالة ذات قيمة حقيقية، يتم تعريف آلية غاوس لتقريب $f$ على النحو التالي

$$\mathcal{G}_{\sigma} f(D) = f(D) + \mathcal{N}(0, \sigma^2),$$

حيث $\mathcal{N}(0, \sigma^2)$ هو متغير عشوائي موزع طبيعيًا بانحراف معياري $\sigma^2$ ومتوسط 0.

البيان التالي هو تعبير في شكل مغلق لاختلاف ريني بين غاوس وإزاحته (لنسخة أكثر عمومية، راجع [19]، [21]).

**المقترح 7.** $D_{\alpha}(\mathcal{N}(0, \sigma^2) \| \mathcal{N}(\mu, \sigma^2)) = \alpha\mu^2/(2\sigma^2)$.

**البرهان.** من خلال الحساب المباشر نتحقق من أن

$$D_{\alpha}(\mathcal{N}(0, \sigma^2) \| \mathcal{N}(\mu, \sigma^2)) = \frac{1}{\alpha - 1} \log \int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi}} \exp(-\alpha x^2/(2\sigma^2))$$

$$\cdot \exp(-(1 - \alpha)(x - \mu)^2/(2\sigma^2)) dx$$

$$= \frac{1}{\alpha - 1} \log \frac{1}{\sigma\sqrt{2\pi}} \int_{-\infty}^{\infty} \exp[(-x^2 + 2(1 - \alpha)\mu x - (1 - \alpha)\mu^2)/(2\sigma^2)] dx$$

$$= \frac{1}{\alpha - 1} \log \left[\frac{\sigma\sqrt{2\pi}}{\sigma\sqrt{2\pi}} \exp\left((α - \alpha)μ^2/(2σ^2)\right)\right] = \alpha\mu^2/(2\sigma^2).$$

النتيجة التالية فورية:

**النتيجة 3.** إذا كان لـ $f$ حساسية 1، فإن آلية غاوس $\mathcal{G}_{\sigma} f$ تحقق $(\alpha, \alpha/(2\sigma^2))$-RDP.

لاحظ أن منحنى ميزانية RDP لآلية غاوس بسيط بشكل خاص - خط مستقيم (الشكل 1). تذكر أن التركيب (التكيفي) لآليات RDP يحقق خصوصية تفاضلية لريني مع منحنى الميزانية الذي هو مجموع منحنيات ميزانية الآليات. هذا يعني أن تركيب آليات غاوس سيتصرف، من ناحية الخصوصية، "مثل" آلية غاوس. بشكل ملموس، فإن تركيب $n$ آليات غاوس كل منها بمعامل $\sigma$ سيكون لها منحنى RDP لآلية غاوس بمعامل $\sigma/\sqrt{n}$.

## د. خصوصية الآليات الأساسية تحت التركيب

يربط تفسير "النتائج السيئة" للخصوصية التفاضلية لريني احتماليات رؤية نفس النتيجة تحت تشغيل الآلية المطبقة على المدخلات المتجاورة. إن اعتماد الحد الأعلى على الزيادة في الاحتمالية على قيمتها الأولية معقد، خاصة بالمقارنة مع ضمان الخصوصية التفاضلية القياسية. الميزة الرئيسية لهذا التحليل الأكثر تعقيدًا هي أنه بالنسبة لمعظم المعاملات يصبح الحد أكثر إحكامًا.

في هذا القسم نقارن الحدود الرقمية لعدة تحليلات للآليات المركبة ذاتيًا (انظر الشكل 2)، المقدمة كثلاث مجموعات من الرسوم البيانية، حيث تأخذ $\Pr[f(D) \in S]$ القيم $10^{-6}$، و$10^{-3}$، و$10^{-1}$.

يرسم كل من الرسوم البيانية الستة في الشكل 2 (ثلاث قيم احتمالية × {الاستجابة العشوائية، لابلاس}) حدودًا على مقياس لوغاريتمي على الزيادة النسبية في احتمالية $S$ (أي $\Pr[f(D') \in S]/\Pr[f(D) \in S]$) المقدمة من أربعة تحليلات. يتبع الحد الأول، "الساذج"، من نظرية التركيب الأساسية للخصوصية التفاضلية، وكما هو متوقع، متشائم جدًا لجميع المعاملات باستثناء حفنة منها. تعطي نظرية تركيب متقدمة أكثر إحكامًا [6]، اختيار δ، ومن ذلك يحسب المرء ε' بحيث يحقق التركيب n-fold خصوصية تفاضلية $(ε', δ)$. يرسم المنحنى الثاني الحد للاختيار الأمثل (الأكثر إحكامًا) لـ $(ε', δ)$. تأتي حدان آخران من تحليل الخصوصية التفاضلية لريني: نظرية التركيب المتقدمة العامة لدينا (المقترح 4) وحد المقترح 10 للمزيج الأمثل من $(α, ε)$ من منحنى RDP للآلية المركبة.

عدة ملاحظات في محلها. التحليل الخاص بـ RDP لكلتا الآليتين أكثر إحكامًا من جميع الحدود العامة التي مدخلها الوحيد هو معامل الخصوصية التفاضلية للآلية. من ناحية أخرى، فإن نسختنا من حد التركيب المتقدم (المقترح 4) يتفوق عليها باستمرار شكل $(ε, δ)$ القياسي لنظرية التركيب، حيث يتم اختيار δ بشكل أمثل. نوضح هذا التمييز في القسم التالي.

---

### Translation Notes

- **Key terms introduced:**
  - predicate (محمول)
  - exponential mechanism (آلية الأسية)
  - additive (جمعية)

- **Figures referenced:** Table II (الجدول الثاني), Figure 1 (الشكل 1), Figure 2 (الشكل 2)
- **Equations:** Multiple propositions and corollaries with closed-form expressions
- **Citations:** [6], [19], [21]
- **Special handling:** Mathematical derivations requiring integration over intervals

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
