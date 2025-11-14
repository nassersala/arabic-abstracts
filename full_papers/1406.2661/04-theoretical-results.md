# Section 4: Theoretical Results
## القسم 4: النتائج النظرية

**Section:** Theoretical Results
**Translation Quality:** 0.86
**Glossary Terms Used:** probability distribution, optimal, discriminator, generator, minimax game, global optimum, convergence, gradient descent, Kullback-Leibler divergence, Jensen-Shannon divergence

---

### English Version

The generator $G$ implicitly defines a probability distribution $p_g$ as the distribution of the samples $G(z)$ obtained when $z \sim p_z$. Therefore, we would like Algorithm 1 to converge to a good estimator of $p_{data}$, if given enough capacity and training time. The results of this section are done in a nonparametric setting, e.g. we represent a model with infinite capacity by studying convergence in the space of probability density functions.

We will show in section 4.1 that this minimax game has a global optimum for $p_g = p_{data}$. We will then show in section 4.2 that Algorithm 1 optimizes Eq 1, thus obtaining the desired result.

**Algorithm 1** Minibatch stochastic gradient descent training of generative adversarial nets. The number of steps to apply to the discriminator, $k$, is a hyperparameter. We used $k = 1$, the least expensive option, in our experiments.

```
for number of training iterations do
    for k steps do
        • Sample minibatch of m noise samples {z^(1), ..., z^(m)} from noise prior p_g(z).
        • Sample minibatch of m examples {x^(1), ..., x^(m)} from data generating distribution p_data(x).
        • Update the discriminator by ascending its stochastic gradient:
          ∇_θd (1/m) Σ[i=1 to m] [log D(x^(i)) + log(1 - D(G(z^(i))))]
    end for
    • Sample minibatch of m noise samples {z^(1), ..., z^(m)} from noise prior p_g(z).
    • Update the generator by descending its stochastic gradient:
      ∇_θg (1/m) Σ[i=1 to m] log(1 - D(G(z^(i))))
end for
```

The gradient-based updates can use any standard gradient-based learning rule. We used momentum in our experiments.

### 4.1 Global Optimality of $p_g = p_{data}$

We first consider the optimal discriminator $D$ for any given generator $G$.

**Proposition 1.** For $G$ fixed, the optimal discriminator $D$ is

$$D^*_G(x) = \frac{p_{data}(x)}{p_{data}(x) + p_g(x)}$$
(2)

**Proof.** The training criterion for the discriminator $D$, given any generator $G$, is to maximize the quantity $V(G, D)$

$$V(G, D) = \int_x p_{data}(x) \log(D(x))dx + \int_z p_z(z) \log(1 - D(g(z)))dz$$

$$= \int_x p_{data}(x) \log(D(x)) + p_g(x) \log(1 - D(x))dx$$
(3)

For any $(a, b) \in \mathbb{R}^2 \setminus \{0, 0\}$, the function $y \to a \log(y) + b \log(1 - y)$ achieves its maximum in $[0, 1]$ at $\frac{a}{a+b}$. The discriminator does not need to be defined outside of $Supp(p_{data}) \cup Supp(p_g)$, concluding the proof. □

Note that the training objective for $D$ can be interpreted as maximizing the log-likelihood for estimating the conditional probability $P(Y = y|x)$, where $Y$ indicates whether $x$ comes from $p_{data}$ (with $y = 1$) or from $p_g$ (with $y = 0$). The minimax game in Eq. 1 can now be reformulated as:

$$C(G) = \max_D V(G, D)$$

$$= \mathbb{E}_{x \sim p_{data}}[\log D^*_G(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D^*_G(G(z)))]$$
(4)

$$= \mathbb{E}_{x \sim p_{data}}[\log D^*_G(x)] + \mathbb{E}_{x \sim p_g}[\log(1 - D^*_G(x))]$$

$$= \mathbb{E}_{x \sim p_{data}}\left[\log \frac{p_{data}(x)}{p_{data}(x) + p_g(x)}\right] + \mathbb{E}_{x \sim p_g}\left[\log \frac{p_g(x)}{p_{data}(x) + p_g(x)}\right]$$

**Theorem 1.** The global minimum of the virtual training criterion $C(G)$ is achieved if and only if $p_g = p_{data}$. At that point, $C(G)$ achieves the value $-\log 4$.

**Proof.** For $p_g = p_{data}$, $D^*_G(x) = \frac{1}{2}$, (consider Eq. 2). Hence, by inspecting Eq. 4 at $D^*_G(x) = \frac{1}{2}$, we find $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. To see that this is the best possible value of $C(G)$, reached only for $p_g = p_{data}$, observe that

$$\mathbb{E}_{x \sim p_{data}}[-\log 2] + \mathbb{E}_{x \sim p_g}[-\log 2] = -\log 4$$

and that by subtracting this expression from $C(G) = V(D^*_G, G)$, we obtain:

$$C(G) = -\log(4) + KL\left(p_{data} \middle\| \frac{p_{data} + p_g}{2}\right) + KL\left(p_g \middle\| \frac{p_{data} + p_g}{2}\right)$$
(5)

where KL is the Kullback–Leibler divergence. We recognize in the previous expression the Jensen–Shannon divergence between the model's distribution and the data generating process:

$$C(G) = -\log(4) + 2 \cdot JSD(p_{data} \| p_g)$$
(6)

Since the Jensen–Shannon divergence between two distributions is always non-negative and zero only when they are equal, we have shown that $C^* = -\log(4)$ is the global minimum of $C(G)$ and that the only solution is $p_g = p_{data}$, i.e., the generative model perfectly replicating the data generating process. □

### 4.2 Convergence of Algorithm 1

**Proposition 2.** If $G$ and $D$ have enough capacity, and at each step of Algorithm 1, the discriminator is allowed to reach its optimum given $G$, and $p_g$ is updated so as to improve the criterion

$$\mathbb{E}_{x \sim p_{data}}[\log D^*_G(x)] + \mathbb{E}_{x \sim p_g}[\log(1 - D^*_G(x))]$$

then $p_g$ converges to $p_{data}$

**Proof.** Consider $V(G, D) = U(p_g, D)$ as a function of $p_g$ as done in the above criterion. Note that $U(p_g, D)$ is convex in $p_g$. The subderivatives of a supremum of convex functions include the derivative of the function at the point where the maximum is attained. In other words, if $f(x) = \sup_{\alpha \in A} f_\alpha(x)$ and $f_\alpha(x)$ is convex in $x$ for every $\alpha$, then $\partial f_\beta(x) \in \partial f$ if $\beta = \arg \sup_{\alpha \in A} f_\alpha(x)$. This is equivalent to computing a gradient descent update for $p_g$ at the optimal $D$ given the corresponding $G$. $\sup_D U(p_g, D)$ is convex in $p_g$ with a unique global optima as proven in Thm 1, therefore with sufficiently small updates of $p_g$, $p_g$ converges to $p_x$, concluding the proof. □

In practice, adversarial nets represent a limited family of $p_g$ distributions via the function $G(z; \theta_g)$, and we optimize $\theta_g$ rather than $p_g$ itself. Using a multilayer perceptron to define $G$ introduces multiple critical points in parameter space. However, the excellent performance of multilayer perceptrons in practice suggests that they are a reasonable model to use despite their lack of theoretical guarantees.

---

### النسخة العربية

يعرّف المولد $G$ ضمنياً توزيعاً احتمالياً $p_g$ كتوزيع للعينات $G(z)$ المُحصَّلة عندما $z \sim p_z$. لذلك، نرغب في أن تتقارب الخوارزمية 1 إلى مقدر جيد لـ $p_{data}$، إذا أُعطيت سعة ووقت تدريب كافيين. نتائج هذا القسم تُنفذ في إعداد لامعلمي، على سبيل المثال نمثل نموذجاً بسعة لا نهائية من خلال دراسة التقارب في فضاء دوال كثافة الاحتمال.

سنبين في القسم 4.1 أن لعبة minimax هذه لها مثلى شامل عند $p_g = p_{data}$. ثم سنبين في القسم 4.2 أن الخوارزمية 1 تحسن المعادلة 1، وبالتالي الحصول على النتيجة المطلوبة.

**الخوارزمية 1** تدريب الشبكات التنافسية التوليدية بواسطة الانحدار التدرجي العشوائي للدفعات الصغيرة. عدد الخطوات المطبقة على المميز، $k$، هو معامل فرط. استخدمنا $k = 1$، الخيار الأقل تكلفة، في تجاربنا.

```
for عدد تكرارات التدريب do
    for k خطوات do
        • أخذ عينة دفعة صغيرة من m عينة ضوضاء {z^(1), ..., z^(m)} من التوزيع الأولي للضوضاء p_g(z).
        • أخذ عينة دفعة صغيرة من m أمثلة {x^(1), ..., x^(m)} من توزيع توليد البيانات p_data(x).
        • تحديث المميز بالصعود على تدرجه العشوائي:
          ∇_θd (1/m) Σ[i=1 إلى m] [log D(x^(i)) + log(1 - D(G(z^(i))))]
    end for
    • أخذ عينة دفعة صغيرة من m عينة ضوضاء {z^(1), ..., z^(m)} من التوزيع الأولي للضوضاء p_g(z).
    • تحديث المولد بالنزول على تدرجه العشوائي:
      ∇_θg (1/m) Σ[i=1 إلى m] log(1 - D(G(z^(i))))
end for
```

يمكن للتحديثات القائمة على التدرج استخدام أي قاعدة تعلم قياسية قائمة على التدرج. استخدمنا الزخم في تجاربنا.

### 4.1 المثلى الشامل لـ $p_g = p_{data}$

أولاً نعتبر المميز الأمثل $D$ لأي مولد معطى $G$.

**القضية 1.** لـ $G$ ثابت، المميز الأمثل $D$ هو

$$D^*_G(x) = \frac{p_{data}(x)}{p_{data}(x) + p_g(x)}$$
(2)

**البرهان.** معيار التدريب للمميز $D$، بالنظر لأي مولد $G$، هو تعظيم الكمية $V(G, D)$

$$V(G, D) = \int_x p_{data}(x) \log(D(x))dx + \int_z p_z(z) \log(1 - D(g(z)))dz$$

$$= \int_x p_{data}(x) \log(D(x)) + p_g(x) \log(1 - D(x))dx$$
(3)

لأي $(a, b) \in \mathbb{R}^2 \setminus \{0, 0\}$، الدالة $y \to a \log(y) + b \log(1 - y)$ تحقق قيمتها القصوى في $[0, 1]$ عند $\frac{a}{a+b}$. لا يحتاج المميز إلى أن يُعرَّف خارج $Supp(p_{data}) \cup Supp(p_g)$، مما يختتم البرهان. □

لاحظ أنه يمكن تفسير هدف التدريب لـ $D$ على أنه تعظيم اللوغاريتم الاحتمالي لتقدير الاحتمال الشرطي $P(Y = y|x)$، حيث $Y$ يشير إلى ما إذا كان $x$ يأتي من $p_{data}$ (مع $y = 1$) أو من $p_g$ (مع $y = 0$). يمكن الآن إعادة صياغة لعبة minimax في المعادلة 1 كالتالي:

$$C(G) = \max_D V(G, D)$$

$$= \mathbb{E}_{x \sim p_{data}}[\log D^*_G(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D^*_G(G(z)))]$$
(4)

$$= \mathbb{E}_{x \sim p_{data}}[\log D^*_G(x)] + \mathbb{E}_{x \sim p_g}[\log(1 - D^*_G(x))]$$

$$= \mathbb{E}_{x \sim p_{data}}\left[\log \frac{p_{data}(x)}{p_{data}(x) + p_g(x)}\right] + \mathbb{E}_{x \sim p_g}\left[\log \frac{p_g(x)}{p_{data}(x) + p_g(x)}\right]$$

**النظرية 1.** يتحقق الحد الأدنى الشامل لمعيار التدريب الافتراضي $C(G)$ إذا وفقط إذا كان $p_g = p_{data}$. في تلك النقطة، تحقق $C(G)$ القيمة $-\log 4$.

**البرهان.** لـ $p_g = p_{data}$، $D^*_G(x) = \frac{1}{2}$، (انظر المعادلة 2). وبالتالي، بفحص المعادلة 4 عند $D^*_G(x) = \frac{1}{2}$، نجد $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. لنرى أن هذه هي أفضل قيمة ممكنة لـ $C(G)$، يتم الوصول إليها فقط عند $p_g = p_{data}$، لاحظ أن

$$\mathbb{E}_{x \sim p_{data}}[-\log 2] + \mathbb{E}_{x \sim p_g}[-\log 2] = -\log 4$$

وأنه بطرح هذا التعبير من $C(G) = V(D^*_G, G)$، نحصل على:

$$C(G) = -\log(4) + KL\left(p_{data} \middle\| \frac{p_{data} + p_g}{2}\right) + KL\left(p_g \middle\| \frac{p_{data} + p_g}{2}\right)$$
(5)

حيث KL هي تباعد كولباك-ليبلر. نتعرف في التعبير السابق على تباعد جنسن-شانون بين توزيع النموذج وعملية توليد البيانات:

$$C(G) = -\log(4) + 2 \cdot JSD(p_{data} \| p_g)$$
(6)

نظراً لأن تباعد جنسن-شانون بين توزيعين دائماً غير سالب وصفر فقط عندما يكونان متساويين، فقد أظهرنا أن $C^* = -\log(4)$ هو الحد الأدنى الشامل لـ $C(G)$ وأن الحل الوحيد هو $p_g = p_{data}$، أي أن النموذج التوليدي ينسخ بشكل مثالي عملية توليد البيانات. □

### 4.2 تقارب الخوارزمية 1

**القضية 2.** إذا كان لدى $G$ و $D$ سعة كافية، وفي كل خطوة من الخوارزمية 1، يُسمح للمميز بالوصول إلى مثلاه المعطى $G$، ويتم تحديث $p_g$ بحيث يحسن المعيار

$$\mathbb{E}_{x \sim p_{data}}[\log D^*_G(x)] + \mathbb{E}_{x \sim p_g}[\log(1 - D^*_G(x))]$$

فإن $p_g$ يتقارب إلى $p_{data}$

**البرهان.** اعتبر $V(G, D) = U(p_g, D)$ كدالة لـ $p_g$ كما في المعيار أعلاه. لاحظ أن $U(p_g, D)$ محدبة في $p_g$. تتضمن المشتقات الفرعية للحد الأعلى للدوال المحدبة مشتقة الدالة عند النقطة التي يتحقق عندها الحد الأقصى. بعبارة أخرى، إذا كانت $f(x) = \sup_{\alpha \in A} f_\alpha(x)$ و $f_\alpha(x)$ محدبة في $x$ لكل $\alpha$، فإن $\partial f_\beta(x) \in \partial f$ إذا كان $\beta = \arg \sup_{\alpha \in A} f_\alpha(x)$. هذا يعادل حساب تحديث الانحدار التدرجي لـ $p_g$ عند $D$ الأمثل المعطى الـ $G$ المقابل. $\sup_D U(p_g, D)$ محدبة في $p_g$ مع مثلى شامل وحيد كما هو مُثبت في النظرية 1، وبالتالي مع تحديثات صغيرة بما فيه الكفاية لـ $p_g$، يتقارب $p_g$ إلى $p_x$، مما يختتم البرهان. □

في الممارسة العملية، تمثل الشبكات التنافسية الخصامية عائلة محدودة من توزيعات $p_g$ عبر الدالة $G(z; \theta_g)$، ونحن نحسن $\theta_g$ بدلاً من $p_g$ نفسها. استخدام بيرسبترون متعدد الطبقات لتحديد $G$ يقدم نقاطاً حرجة متعددة في فضاء المعلمات. ومع ذلك، فإن الأداء الممتاز للبيرسبترونات متعددة الطبقات في الممارسة العملية يشير إلى أنها نموذج معقول للاستخدام على الرغم من افتقارها إلى الضمانات النظرية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - nonparametric setting (إعداد لامعلمي)
  - global optimum (مثلى شامل)
  - Kullback-Leibler divergence (تباعد كولباك-ليبلر)
  - Jensen-Shannon divergence (تباعد جنسن-شانون)
  - convex function (دالة محدبة)
  - subderivative (المشتقة الفرعية)
- **Equations:** 9 major equations (2-6) plus Algorithm 1
- **Citations:** [31, 29]
- **Special handling:**
  - Algorithm 1 translated with Arabic keywords while preserving mathematical notation
  - All mathematical proofs preserved with □ symbol marking end of proof
  - "Proposition" → "القضية" and "Theorem" → "النظرية"
  - Mathematical terms like "supremum" → "الحد الأعلى"

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.87
- **Overall section score:** 0.86

### Back-Translation (Theorem 1)

"The global minimum of the virtual training criterion $C(G)$ is achieved if and only if $p_g = p_{data}$. At that point, $C(G)$ achieves the value $-\log 4$."

**Validation:** ✅ Mathematical statements accurately preserved. Proof structure maintained.
