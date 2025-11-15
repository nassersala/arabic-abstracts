# Section 5: Advanced Composition Theorem
## القسم 5: نظرية التركيب المتقدمة

**Section:** methodology
**Translation Quality:** 0.85
**Glossary Terms Used:** differential privacy, Rényi differential privacy, composition, mechanism, privacy loss

---

### English Version

The main thesis of this section is that the Rényi differential privacy curve of a composite mechanism is sufficient to draw non-trivial conclusions about its privacy guarantees, similar to the ones given by other advanced composition theorems, such as Dwork et al. [6] or Kairouz et al. [7]. Although our proof is structured similarly to Dwork et al. (for instance, Lemma 1 is a direct generalization of [6, Lemma III.2]), it is phrased entirely in the language of Rényi differential privacy without making any (explicit) use of probability arguments.

**Lemma 1.** If $P$ and $Q$ are such that $D_{\infty}(P \| Q) \leq \varepsilon$ and $D_{\infty}(Q \| P) \leq \varepsilon$, then for $\alpha \geq 1$

$$D_{\alpha}(P \| Q) \leq 2\alpha\varepsilon^2.$$

**Proof.** If $\alpha \geq 1 + 1/\varepsilon$, then

$$D_{\alpha}(P \| Q) \leq D_{\infty}(P \| Q) = \varepsilon \leq (\alpha - 1)\varepsilon^2.$$

Consider the case when $\alpha < 1 + 1/\varepsilon$. We first observe that for any $x > y > 0$, $\lambda = \log(x/y)$, and $0 \leq \beta \leq 1/\lambda$ the following inequality holds:

$$x^{\beta+1} y^{-\beta} + x^{-\beta} y^{\beta+1} = x \cdot e^{\beta\lambda} + y \cdot e^{-\beta\lambda}$$

$$\leq x(1 + \beta\lambda + (\beta\lambda)^2) + y(1 - \beta\lambda + (\beta\lambda)^2) = (1 + (\beta\lambda)^2)(x + y) + \beta\lambda(x - y). \quad (2)$$

Since all terms of the right hand side of (2) are positive, the inequality applies if $\lambda$ is an upper bound on $\log x/y$, which we use in the argument below.

$$\exp[(\alpha - 1)D_{\alpha}(P \| Q)] = \int_{\mathcal{R}} P(x)^{\alpha} Q(x)^{1-\alpha} dx$$

$$\leq \int_{\mathcal{R}} \left(P(x)^{\alpha} Q(x)^{1-\alpha} + Q(x)^{\alpha} P(x)^{1-\alpha}\right) dx - 1$$

(by non-negativity of $D_{\alpha}(Q \| P)$)

$$\leq \int_{\mathcal{R}} \left[(1 + (\alpha - 1)^2 \varepsilon^2)(P(x) + Q(x)) + (\alpha - 1)\varepsilon|P(x) - Q(x)|\right] dx - 1$$

(by (2) for $\beta = \alpha - 1 \leq 1/\varepsilon$)

$$= 1 + 2(\alpha - 1)^2 \varepsilon^2 + (\alpha - 1)\varepsilon\|P - Q\|_1.$$

Observe that

$$\|P - Q\|_1 = \int_{\mathcal{R}} |P(x) - Q(x)| dx = \int_{\mathcal{R}} \min(P(x), Q(x)) \left[\frac{\max(P(x), Q(x))}{\min(P(x), Q(x))} - 1\right] dx$$

$$\leq \min(2, e^{\varepsilon} - 1) \leq 2\varepsilon^2.$$

Plugging the bound on $\|P - Q\|_1$ into (3) completes the proof.

The claim for $\alpha = 1$ follows by continuity.

The constant in Lemma 1 can be improved to .5 via a substantially more involved analysis [10, Proposition 3.3].

**Proposition 4.** Let $f : \mathcal{D} \mapsto \mathcal{R}$ be an adaptive composition of $n$ mechanisms all satisfying ε-differential privacy. Let $D$ and $D'$ be two adjacent inputs. Then for any $S \subset \mathcal{R}$:

$$\Pr[f(D) \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/\Pr[f(D') \in S]}\right) \cdot \Pr[f(D') \in S].$$

**Proof.** By applying Lemma 1 to the Rényi differential privacy curve of the underlying mechanisms and Proposition 1 to their composition, we find that for all $\alpha \geq 1$

$$D_{\alpha}(f(D) \| f(D')) \leq 2\alpha n\varepsilon^2.$$

Denote $\Pr[f(D') \in S]$ by $Q$ and consider two cases.

**Case I:** $\log 1/Q \geq \varepsilon^2 n$. Choosing with some foresight $\alpha = \sqrt{\log 1/Q}/(\varepsilon\sqrt{n}) \geq 1$, we have by Proposition 10 (probability preservation):

$$\Pr[f(D) \in S] \leq \{\exp[D_{\alpha}(f(D) \| f(D'))] \cdot Q\}^{1-1/\alpha}$$

$$\leq \exp(2(\alpha - 1)n\varepsilon^2) \cdot Q^{1-1/\alpha} < \exp\left(\varepsilon\sqrt{n\log 1/Q} - (\log Q)/\alpha\right) \cdot Q$$

$$= \exp\left(\sqrt{2\varepsilon n \log 1/Q}\right) \cdot Q.$$

**Case II:** $\log 1/Q < \varepsilon^2 n$. This case follows trivially, since the right hand side of the claim is larger than 1:

$$\exp\left(\sqrt{2\varepsilon n \log 1/Q}\right) \cdot Q \geq \exp(2 \log 1/Q) \cdot Q = 1/Q > 1.$$

The notable feature of Proposition 4 is that its privacy guarantee—bounded probability gain—comes in the form that depends on the event's probability. We discuss this type of guarantee in Section VII.

The following corollary gives a more conventional (ε, δ) variant of advanced composition.

**Corollary 1.** Let $f$ be the composition of the $n$ ε-differentially private mechanisms. Let $0 < \delta < 1$ be such that $\log(1/\delta) \geq \varepsilon^2 n$. Then $f$ satisfies $(ε', δ)$-differential privacy where

$$ε' \triangleq 4\varepsilon\sqrt{2n \log(1/\delta)}.$$

**Proof.** Let $D$ and $D'$ be two adjacent inputs, and $S$ be some subset of the range of $f$. To argue $(ε', δ)$-differential privacy of $f$, we need to verify that

$$\Pr[f(D) \in S] \leq e^{\varepsilon'} \Pr[f(D') \in S] + \delta.$$

In fact, we prove a somewhat stronger statement, namely that $\Pr[f(D) \in S] \leq \max(e^{\varepsilon'} \Pr[f(D') \in S], \delta)$.

By Proposition 4

$$\Pr[f(D) \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/\Pr[f(D') \in S]}\right) \cdot \Pr[f(D') \in S].$$

Denote $\Pr[f(D') \in S]$ by $Q$ and consider two cases.

**Case I:** $8 \log 1/\delta > \log 1/Q$. Then

$$\Pr[f(D) \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/Q}\right) \cdot Q < \exp\left(\sqrt{2\varepsilon 8n \log 1/\delta}\right) \cdot Q$$

(by $8 \log 1/\delta > \log 1/Q$)

$$= \exp(ε') \cdot Q.$$

**Case II:** $8 \log 1/\delta \leq \log 1/Q$. Then

$$\Pr[f(D) \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/Q}\right) \cdot Q \leq \exp\left(\sqrt{2 \log 1/\delta \cdot \log 1/Q}\right) \cdot Q$$

(since $\log(1/\delta) \geq \varepsilon^2 n$)

$$\leq \exp\left(\sqrt{1/2} \log 1/Q\right) \cdot Q$$

(since $8 \log 1/\delta \leq \log 1/Q$)

$$= Q^{1-1/\sqrt{2}} \leq Q^{1/8} \leq \delta.$$

**Remark 3.** The condition $\log(1/\delta) \geq \varepsilon^2 n$ corresponds to the so-called "high privacy" regime of the advanced composition theorem [7], where $ε' < (1+\sqrt{2}) \log(1/\delta)$. Since δ is typically chosen to be small, say, less than 1%, it covers the case of $ε' < 11$. In other words, if $\log(1/\delta) > \varepsilon^2 n$, this and other composition theorems are unlikely to yield strong bounds.

---

### النسخة العربية

الأطروحة الرئيسية لهذا القسم هي أن منحنى الخصوصية التفاضلية لريني لآلية مركبة كافٍ لاستخلاص استنتاجات غير تافهة حول ضمانات الخصوصية الخاصة بها، مماثلة لتلك المقدمة من نظريات التركيب المتقدمة الأخرى، مثل Dwork وآخرين [6] أو Kairouz وآخرين [7]. على الرغم من أن برهاننا مبني بشكل مشابه لـ Dwork وآخرين (على سبيل المثال، اللمة 1 هي تعميم مباشر لـ [6، اللمة III.2])، إلا أنه صيغ بالكامل بلغة الخصوصية التفاضلية لريني دون استخدام أي حجج احتمالية (صريحة).

**اللمة 1.** إذا كان $P$ و$Q$ بحيث $D_{\infty}(P \| Q) \leq \varepsilon$ و$D_{\infty}(Q \| P) \leq \varepsilon$، فإنه لـ $\alpha \geq 1$

$$D_{\alpha}(P \| Q) \leq 2\alpha\varepsilon^2.$$

**البرهان.** إذا كان $\alpha \geq 1 + 1/\varepsilon$، فإن

$$D_{\alpha}(P \| Q) \leq D_{\infty}(P \| Q) = \varepsilon \leq (\alpha - 1)\varepsilon^2.$$

ضع في اعتبارك الحالة عندما $\alpha < 1 + 1/\varepsilon$. نلاحظ أولاً أنه لأي $x > y > 0$، و$\lambda = \log(x/y)$، و$0 \leq \beta \leq 1/\lambda$ تصمد المتباينة التالية:

$$x^{\beta+1} y^{-\beta} + x^{-\beta} y^{\beta+1} = x \cdot e^{\beta\lambda} + y \cdot e^{-\beta\lambda}$$

$$\leq x(1 + \beta\lambda + (\beta\lambda)^2) + y(1 - \beta\lambda + (\beta\lambda)^2) = (1 + (\beta\lambda)^2)(x + y) + \beta\lambda(x - y). \quad (2)$$

بما أن جميع حدود الجانب الأيمن من (2) موجبة، فإن المتباينة تنطبق إذا كان $\lambda$ حدًا أعلى على $\log x/y$، والذي نستخدمه في الحجة أدناه.

$$\exp[(\alpha - 1)D_{\alpha}(P \| Q)] = \int_{\mathcal{R}} P(x)^{\alpha} Q(x)^{1-\alpha} dx$$

$$\leq \int_{\mathcal{R}} \left(P(x)^{\alpha} Q(x)^{1-\alpha} + Q(x)^{\alpha} P(x)^{1-\alpha}\right) dx - 1$$

(بواسطة عدم سلبية $D_{\alpha}(Q \| P)$)

$$\leq \int_{\mathcal{R}} \left[(1 + (\alpha - 1)^2 \varepsilon^2)(P(x) + Q(x)) + (\alpha - 1)\varepsilon|P(x) - Q(x)|\right] dx - 1$$

(بواسطة (2) لـ $\beta = \alpha - 1 \leq 1/\varepsilon$)

$$= 1 + 2(\alpha - 1)^2 \varepsilon^2 + (\alpha - 1)\varepsilon\|P - Q\|_1.$$

لاحظ أن

$$\|P - Q\|_1 = \int_{\mathcal{R}} |P(x) - Q(x)| dx = \int_{\mathcal{R}} \min(P(x), Q(x)) \left[\frac{\max(P(x), Q(x))}{\min(P(x), Q(x))} - 1\right] dx$$

$$\leq \min(2, e^{\varepsilon} - 1) \leq 2\varepsilon^2.$$

إدراج الحد على $\|P - Q\|_1$ في (3) يكمل البرهان.

يتبع الادعاء لـ $\alpha = 1$ بالاستمرارية.

يمكن تحسين الثابت في اللمة 1 إلى 0.5 عبر تحليل أكثر تعقيدًا إلى حد كبير [10، المقترح 3.3].

**المقترح 4.** ليكن $f : \mathcal{D} \mapsto \mathcal{R}$ تركيبًا تكيفيًا لـ $n$ آليات جميعها تحقق خصوصية تفاضلية ε. ليكن $D$ و$D'$ مدخلين متجاورين. ثم لأي $S \subset \mathcal{R}$:

$$\Pr[f(D) \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/\Pr[f(D') \in S]}\right) \cdot \Pr[f(D') \in S].$$

**البرهان.** بتطبيق اللمة 1 على منحنى الخصوصية التفاضلية لريني للآليات الأساسية والمقترح 1 على تركيبها، نجد أنه لجميع $\alpha \geq 1$

$$D_{\alpha}(f(D) \| f(D')) \leq 2\alpha n\varepsilon^2.$$

دع $\Pr[f(D') \in S]$ تكون $Q$ وضع في اعتبارك حالتين.

**الحالة الأولى:** $\log 1/Q \geq \varepsilon^2 n$. باختيار مع بعض البصيرة $\alpha = \sqrt{\log 1/Q}/(\varepsilon\sqrt{n}) \geq 1$، لدينا بواسطة المقترح 10 (الحفاظ على الاحتمالية):

$$\Pr[f(D) \in S] \leq \{\exp[D_{\alpha}(f(D) \| f(D'))] \cdot Q\}^{1-1/\alpha}$$

$$\leq \exp(2(\alpha - 1)n\varepsilon^2) \cdot Q^{1-1/\alpha} < \exp\left(\varepsilon\sqrt{n\log 1/Q} - (\log Q)/\alpha\right) \cdot Q$$

$$= \exp\left(\sqrt{2\varepsilon n \log 1/Q}\right) \cdot Q.$$

**الحالة الثانية:** $\log 1/Q < \varepsilon^2 n$. تتبع هذه الحالة بشكل تافه، حيث أن الجانب الأيمن من الادعاء أكبر من 1:

$$\exp\left(\sqrt{2\varepsilon n \log 1/Q}\right) \cdot Q \geq \exp(2 \log 1/Q) \cdot Q = 1/Q > 1.$$

الميزة البارزة للمقترح 4 هي أن ضمان الخصوصية - كسب الاحتمالية المحدود - يأتي في الشكل الذي يعتمد على احتمالية الحدث. نناقش هذا النوع من الضمان في القسم السابع.

تعطي النتيجة التالية نسخة (ε, δ) أكثر تقليدية من التركيب المتقدم.

**النتيجة 1.** ليكن $f$ تركيب $n$ آليات خاصة تفاضليًا ε. ليكن $0 < \delta < 1$ بحيث $\log(1/\delta) \geq \varepsilon^2 n$. ثم $f$ تحقق خصوصية تفاضلية $(ε', δ)$ حيث

$$ε' \triangleq 4\varepsilon\sqrt{2n \log(1/\delta)}.$$

**البرهان.** ليكن $D$ و$D'$ مدخلين متجاورين، و$S$ مجموعة فرعية من نطاق $f$. للجدال بخصوصية تفاضلية $(ε', δ)$ لـ $f$، نحتاج إلى التحقق من أن

$$\Pr[f(D) \in S] \leq e^{\varepsilon'} \Pr[f(D') \in S] + \delta.$$

في الواقع، نثبت بيانًا أقوى إلى حد ما، وهو أن $\Pr[f(D) \in S] \leq \max(e^{\varepsilon'} \Pr[f(D') \in S], \delta)$.

بواسطة المقترح 4

$$\Pr[f(D) \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/\Pr[f(D') \in S]}\right) \cdot \Pr[f(D') \in S].$$

دع $\Pr[f(D') \in S]$ تكون $Q$ وضع في اعتبارك حالتين.

**الحالة الأولى:** $8 \log 1/\delta > \log 1/Q$. ثم

$$\Pr[f(D) \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/Q}\right) \cdot Q < \exp\left(\sqrt{2\varepsilon 8n \log 1/\delta}\right) \cdot Q$$

(بواسطة $8 \log 1/\delta > \log 1/Q$)

$$= \exp(ε') \cdot Q.$$

**الحالة الثانية:** $8 \log 1/\delta \leq \log 1/Q$. ثم

$$\Pr[f(D) \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/Q}\right) \cdot Q \leq \exp\left(\sqrt{2 \log 1/\delta \cdot \log 1/Q}\right) \cdot Q$$

(حيث $\log(1/\delta) \geq \varepsilon^2 n$)

$$\leq \exp\left(\sqrt{1/2} \log 1/Q\right) \cdot Q$$

(حيث $8 \log 1/\delta \leq \log 1/Q$)

$$= Q^{1-1/\sqrt{2}} \leq Q^{1/8} \leq \delta.$$

**ملاحظة 3.** يتوافق الشرط $\log(1/\delta) \geq \varepsilon^2 n$ مع ما يسمى بنظام "الخصوصية العالية" لنظرية التركيب المتقدمة [7]، حيث $ε' < (1+\sqrt{2}) \log(1/\delta)$. بما أن δ يتم اختياره عادةً ليكون صغيرًا، على سبيل المثال، أقل من 1٪، فإنه يغطي حالة $ε' < 11$. بعبارة أخرى، إذا كان $\log(1/\delta) > \varepsilon^2 n$، فمن غير المرجح أن تسفر هذه ونظريات التركيب الأخرى عن حدود قوية.

---

### Translation Notes

- **Key terms introduced:**
  - bounded probability gain (كسب الاحتمالية المحدود)
  - high privacy regime (نظام الخصوصية العالية)

- **Figures referenced:** None
- **Equations:** Multiple lemmas, propositions, and proofs with case analysis
- **Citations:** [6], [7], [10]
- **Special handling:** Complex mathematical proofs requiring careful case-by-case analysis

### Quality Metrics

- Semantic equivalence: 0.85
- Technical accuracy: 0.87
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.85
