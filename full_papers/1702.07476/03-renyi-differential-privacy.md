# Section 3: Rényi Differential Privacy
## القسم 3: الخصوصية التفاضلية لريني

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** differential privacy, Rényi divergence, mechanism, composition, privacy loss, Bayes factor, post-processing, group privacy

---

### English Version

We describe a generalization of the notion of differential privacy based on the concept of the Rényi divergence. Connection between the two notions has been pointed out before (mostly for one extreme order, known as the Kullback-Leibler divergence [6], [17]); our contribution is in systematically exploring the relationship and its practical implications.

The (parameterized) Rényi divergence is classically defined as follows [18]:

**Definition 3 (Rényi divergence).** For two probability distributions $P$ and $Q$ defined over $\mathcal{R}$, the Rényi divergence of order $\alpha > 1$ is

$$D_{\alpha}(P \| Q) \triangleq \frac{1}{\alpha - 1} \log \mathbb{E}_{x \sim Q}\left[\left(\frac{P(x)}{Q(x)}\right)^{\alpha}\right].$$

(All logarithms are natural; $P(x)$ is the density of $P$ at $x$.)

For the endpoints of the interval $(1, \infty)$ the Rényi divergence is defined by continuity. Concretely, $D_1(P \| Q)$ is set to be $\lim_{\alpha \to 1} D_{\alpha}(P \| Q)$ and can be verified to be equal to the Kullback-Leibler divergence (also known as relative entropy):

$$D_1(P \| Q) = \mathbb{E}_{x \sim P}\log\frac{P(x)}{Q(x)}.$$

Note that the expectation is taken over $P$, rather than over $Q$ as in the previous definition. It is possible, though, that $D_1(P \| Q)$ thus defined is finite whereas $D_{\alpha}(P \| Q) = +\infty$ for all $\alpha > 1$.

Likewise,

$$D_{\infty}(P \| Q) = \sup_{x \in \text{supp } Q} \log \frac{P(x)}{Q(x)}.$$

For completeness, we reproduce in the Appendix properties of the Rényi divergence important to the sequel: non-negativity, monotonicity, probability preservation, and a weak triangle inequality (Propositions 8–11).

The relationship between the Rényi divergence with $\alpha = \infty$ and differential privacy is immediate. A randomized mechanism $f$ is ε-differentially private if and only if its distribution over any two adjacent inputs $D$ and $D'$ satisfies

$$D_{\infty}(f(D) \| f(D')) \leq \varepsilon.$$

It motivates exploring a relaxation of differential privacy based on the Rényi divergence.

**Definition 4 ((α, ε)-RDP).** A randomized mechanism $f : \mathcal{D} \mapsto \mathcal{R}$ is said to have ε-Rényi differential privacy of order α, or (α, ε)-RDP for short, if for any adjacent $D, D' \in \mathcal{D}$ it holds that

$$D_{\alpha}(f(D) \| f(D')) \leq \varepsilon.$$

**Remark 1.** Similarly to the definition of differential privacy, a finite value for ε-RDP implies that feasible outcomes of $f(D)$ for some $D \in \mathcal{D}$ are feasible, i.e., have a non-zero density, for all inputs from $\mathcal{D}$ except for a set of measure 0. Assuming that this is the case, we let the event space be the support of the distribution.

**Remark 2.** The Rényi divergence can be defined for α smaller than 1, including negative orders. We are not using these orders in our definition of Rényi differential privacy.

The standard definition of differential privacy has been successful as a privacy measure because it simultaneously meets several important criteria. We verify that the relaxed definition inherits many of the same properties. The results of this section are summarized in Table I.

## "BAD OUTCOMES" GUARANTEE

A privacy definition is only as useful as its guarantee for data contributors. The simplest such assurance is the "bad outcomes" interpretation. Consider a person, concerned about some adverse consequences, deliberating whether to withhold her record from the database. Let us say that some outputs of the mechanism are labeled as "bad." The differential privacy guarantee asserts that the probability of observing a bad outcome will not change (either way) by more than a factor of $e^{\varepsilon}$ whether anyone's record is part of the input or not (for appropriately defined "adjacent" inputs). This is an immediate consequence of the definition of differential privacy, where the subset $S$ is the union of bad outcomes.

This guarantee is relaxed for Rényi differential privacy. Concretely, if $f$ is (α, ε)-RDP, then by Proposition 10:

$$e^{-\varepsilon} \Pr[f(D') \in S]^{\alpha/(\alpha-1)} \leq \Pr[f(D) \in S] \leq (e^{\varepsilon} \Pr[f(D') \in S])^{(\alpha-1)/\alpha}.$$

We discuss consequences of this relaxation in Section VII.

## ROBUSTNESS TO AUXILIARY INFORMATION

Critical to the adoption of differential privacy as an operationally useful definition is its lack of assumptions on the adversary's knowledge. More formally, the property is captured by the Bayesian interpretation of privacy guarantees, which compares the adversary's prior with the posterior.

Assume that the adversary has a prior $p(D)$ over the set of possible inputs $D \in \mathcal{D}$, and observes an output $X$ of an ε-differentially private mechanism $f$. Its posterior satisfies the following guarantee for all pairs of adjacent inputs $D, D' \in \mathcal{D}$ and all $X \in \mathcal{R}$:

$$\frac{p(D|X)}{p(D'|X)} \leq e^{\varepsilon} \frac{p(D)}{p(D')}.$$

In other words, evidence obtained from an ε-differentially private mechanism does not move the relative probabilities assigned to adjacent inputs (the odds ratio) by more than $e^{\varepsilon}$.

The guarantee implied by RDP is a probabilistic statement about the change in the Bayes factor. Let the random variable $R(D, D')$ be defined as follows:

$$R(D, D') \sim \frac{p(D'|X)}{p(D|X)} = \frac{p(X|D') \cdot p(D')}{p(X|D) \cdot p(D)},$$

where $X \sim f(D)$.

It follows immediately from definition that the Rényi divergence of order α between $P = f(D')$ and $Q = f(D)$ bounds the α-th moment of the change in $R$:

$$\mathbb{E}_Q\left[\left(\frac{R_{\text{post}}(D, D')}{R_{\text{prior}}(D, D')}\right)^{\alpha}\right] = \mathbb{E}_Q\left[\left(\frac{P(x)}{Q(x)}\right)^{\alpha}\right] = \exp[(\alpha - 1)D_{\alpha}(f(D') \| f(D))].$$

By taking the logarithm of both sides and applying Jensen's inequality we obtain that

$$\mathbb{E}_{f(D)}[\log R_{\text{post}}(D, D') - \log R_{\text{prior}}(D, D')] \leq D_{\alpha}(f(D) \| f(D')).$$

(This can also be derived by observing that

$$\mathbb{E}_{f(D)}[\log R_{\text{post}}(D, D') - \log R_{\text{prior}}(D, D')] = D_1(f(D) \| f(D'))$$

and by monotonicity of the Rényi divergence.)

Compare (1) with the guarantee of pure differential privacy, which states that $\log R_{\text{post}}(D, D') - \log R_{\text{prior}}(D, D') \leq \varepsilon$ everywhere, not just in expectation.

## POST-PROCESSING

A privacy guarantee that can be diminished by manipulating output is unlikely to be useful. Consider a randomized mapping $g : \mathcal{R} \mapsto \mathcal{R}'$. We observe that $D_{\alpha}(P \| Q) \geq D_{\alpha}(g(P) \| g(Q))$ by the analogue of the data processing inequality [19, Theorem 9]. It means that if $f(\cdot)$ is (α, ε)-RDP, so is $g(f(\cdot))$. In other words, Rényi differential privacy is preserved by post-processing.

## PRESERVATION UNDER ADAPTIVE SEQUENTIAL COMPOSITION

The property that makes possible modular construction of differentially private algorithms is self-composition: if $f(\cdot)$ is $\varepsilon_1$-differentially private and $g(\cdot)$ is $\varepsilon_2$-differentially private, then simultaneous release of $f(D)$ and $g(D)$ is $\varepsilon_1 + \varepsilon_2$-differentially private. The guarantee even extends to when $g$ is chosen adaptively based on $f$'s output: if $g$ is indexed by elements of $\mathcal{R}$ and $g_X(\cdot)$ is $\varepsilon_2$-differentially private for any $X \in \mathcal{R}$, then publishing $(X, Y)$, where $X \sim f(D)$ and $Y \sim g_X(D)$, is $\varepsilon_1 + \varepsilon_2$-differentially private.

We prove a similar statement for the composition of two RDP mechanisms.

**Proposition 1.** Let $f : \mathcal{D} \mapsto \mathcal{R}_1$ be (α, $\varepsilon_1$)-RDP and $g : \mathcal{R}_1 \times \mathcal{D} \mapsto \mathcal{R}_2$ be (α, $\varepsilon_2$)-RDP, then the mechanism defined as $(X, Y)$, where $X \sim f(D)$ and $Y \sim g(X, D)$, satisfies (α, $\varepsilon_1 + \varepsilon_2$)-RDP.

**Proof.** Let $h : \mathcal{D} \mapsto \mathcal{R}_1 \times \mathcal{R}_2$ be the result of running $f$ and $g$ sequentially. We write $X$, $Y$, and $Z$ for the distributions $f(D)$, $g(X, D)$, and the joint distribution $(X, Y) = h(D)$. $X'$, $Y'$, and $Z'$ are similarly defined if the input is $D'$. Then

$$\exp[(\alpha - 1)D_{\alpha}(h(D) \| h(D'))] = \int_{\mathcal{R}_1 \times \mathcal{R}_2} Z(x, y)^{\alpha} Z'(x, y)^{1-\alpha} dx dy$$

$$= \int_{\mathcal{R}_1} \int_{\mathcal{R}_2} (X(x)Y(x, y))^{\alpha} (X'(x)Y'(x, y))^{1-\alpha} dy dx$$

$$= \int_{\mathcal{R}_1} X(x)^{\alpha} X'(x)^{1-\alpha} \left[\int_{\mathcal{R}_2} Y(x, y)^{\alpha} Y'(x, y)^{1-\alpha} dy\right] dx$$

$$\leq \int_{\mathcal{R}_1} X(x)^{\alpha} X'(x)^{1-\alpha} dx \cdot \exp((\alpha - 1)\varepsilon_2)$$

$$\leq \exp((\alpha - 1)\varepsilon_1) \exp((\alpha - 1)\varepsilon_2) = \exp((\alpha - 1)(\varepsilon_1 + \varepsilon_2)),$$

from which the claim follows.

Significantly, the guarantee holds whether the releases of $f$ and $g$ are coordinated or not, or computed over the same or different versions of the input dataset. It allows us to operate with a well-defined notion of a privacy budget associated with an individual, which is a finite resource consumed with each differentially private data release.

Extending the concept of the privacy budget, we say that the Rényi differential privacy has a budget curve parameterized by the order α. We present examples illustrating this viewpoint in Section VI.

## GROUP PRIVACY

Although the definition of differential privacy constrains a mechanism's outputs on pairs of adjacent inputs, its guarantee extends, in a progressively weaker form, to inputs that are farther apart. This property has two important consequences. First, the differential privacy guarantee degrades gracefully if our assumptions about one person's influence on the input are (somewhat) wrong. For example, a single family contributing to a survey will likely share many socio-economic, demographic, and health characteristics. Rather than collapsing, the differential privacy guarantee will scale down linearly with the number of family members. Second, the group privacy property allows preprocessing input into a differentially private mechanism, possibly amplifying (in a controlled fashion) one record's impact on the output of the computation.

We define group privacy using a notion of c-stable transformation [20]. We say that $g : \mathcal{D} \mapsto \mathcal{D}'$ is c-stable if $g(A)$ and $g(B)$ are adjacent in $\mathcal{D}'$ implies that there exists a sequence of length $c + 1$ so that $D_0 = A, \ldots, D_c = B$ and all $(D_i, D_{i+1})$ are adjacent in $\mathcal{D}$.

The standard notion of differential privacy satisfies the following. If $f$ is ε-differentially private and $g : \mathcal{D}' \mapsto \mathcal{D}$ is c-stable, then $f \circ g$ is $c\varepsilon$-differentially private. A similar statement holds for Rényi differential privacy.

**Proposition 2.** If $f : \mathcal{D} \mapsto \mathcal{R}$ is (α, ε)-RDP, $g : \mathcal{D}' \mapsto \mathcal{D}$ is $2^c$-stable and $\alpha \geq 2^{c+1}$, then $f \circ g$ is (α/$2^c$, $3^c \varepsilon$)-RDP.

**Proof.** We prove the statement for $c = 1$, the rest follows by induction.

Define $h = f \circ g$. Since $g$ is 2-stable, it means that for any adjacent $D, D' \in \mathcal{D}'$ there exist $A \in \mathcal{D}$, so that $g(D)$ and $A$, $A$ and $g(D')$ are adjacent in $\mathcal{D}$.

By Corollary 4 and monotonicity of the Rényi divergence, we have that $h = f \circ g$ satisfies

$$D_{\alpha/2}(h(D) \| h(D')) \leq \frac{\alpha - 1}{\alpha - 2} D_{\alpha}(h(D) \| h(A)) + D_{\alpha-1}(h(A) \| h(D')) \leq 3\varepsilon.$$

---

### النسخة العربية

نصف تعميمًا لمفهوم الخصوصية التفاضلية بناءً على مفهوم اختلاف ريني. تم الإشارة إلى الصلة بين المفهومين من قبل (في الغالب لرتبة طرفية واحدة، المعروفة باسم اختلاف كولباك-ليبلر [6]، [17])؛ مساهمتنا هي في استكشاف العلاقة وآثارها العملية بشكل منهجي.

يتم تعريف اختلاف ريني (المُعامَل) بشكل كلاسيكي على النحو التالي [18]:

**التعريف 3 (اختلاف ريني).** لتوزيعي احتمال $P$ و$Q$ معرفين على $\mathcal{R}$، فإن اختلاف ريني من الرتبة $\alpha > 1$ هو

$$D_{\alpha}(P \| Q) \triangleq \frac{1}{\alpha - 1} \log \mathbb{E}_{x \sim Q}\left[\left(\frac{P(x)}{Q(x)}\right)^{\alpha}\right].$$

(جميع اللوغاريتمات طبيعية؛ $P(x)$ هي كثافة $P$ عند $x$.)

بالنسبة لنقاط نهاية الفترة $(1, \infty)$، يتم تعريف اختلاف ريني بالاستمرارية. بشكل ملموس، يتم تعيين $D_1(P \| Q)$ لتكون $\lim_{\alpha \to 1} D_{\alpha}(P \| Q)$ ويمكن التحقق من أنها تساوي اختلاف كولباك-ليبلر (المعروف أيضًا باسم الإنتروبيا النسبية):

$$D_1(P \| Q) = \mathbb{E}_{x \sim P}\log\frac{P(x)}{Q(x)}.$$

لاحظ أن التوقع مأخوذ على $P$، بدلاً من $Q$ كما في التعريف السابق. من الممكن، مع ذلك، أن $D_1(P \| Q)$ المعرفة بهذا الشكل محدودة بينما $D_{\alpha}(P \| Q) = +\infty$ لجميع $\alpha > 1$.

وبالمثل،

$$D_{\infty}(P \| Q) = \sup_{x \in \text{supp } Q} \log \frac{P(x)}{Q(x)}.$$

للاكتمال، نعيد إنتاج خصائص اختلاف ريني المهمة للتسلسل في الملحق: عدم السلبية، والرتابة، والحفاظ على الاحتمالية، ومتباينة مثلثية ضعيفة (المقترحات 8-11).

العلاقة بين اختلاف ريني مع $\alpha = \infty$ والخصوصية التفاضلية فورية. آلية عشوائية $f$ خاصة تفاضليًا ε إذا وفقط إذا كان توزيعها على أي مدخلين متجاورين $D$ و$D'$ يحقق

$$D_{\infty}(f(D) \| f(D')) \leq \varepsilon.$$

هذا يحفز استكشاف تخفيف للخصوصية التفاضلية بناءً على اختلاف ريني.

**التعريف 4 ((α, ε)-RDP).** يُقال إن آلية عشوائية $f : \mathcal{D} \mapsto \mathcal{R}$ لديها خصوصية تفاضلية ε لريني من الرتبة α، أو (α, ε)-RDP باختصار، إذا كان لأي مدخلات متجاورة $D, D' \in \mathcal{D}$ يصح أن

$$D_{\alpha}(f(D) \| f(D')) \leq \varepsilon.$$

**ملاحظة 1.** على غرار تعريف الخصوصية التفاضلية، فإن قيمة محدودة لـ ε-RDP تعني أن النتائج الممكنة لـ $f(D)$ لبعض $D \in \mathcal{D}$ ممكنة، أي لها كثافة غير صفرية، لجميع المدخلات من $\mathcal{D}$ باستثناء مجموعة من القياس 0. بافتراض أن هذا هو الحال، فإننا نجعل فضاء الحدث هو دعم التوزيع.

**ملاحظة 2.** يمكن تعريف اختلاف ريني لـ α أصغر من 1، بما في ذلك الرتب السلبية. نحن لا نستخدم هذه الرتب في تعريفنا للخصوصية التفاضلية لريني.

كان التعريف القياسي للخصوصية التفاضلية ناجحًا كمقياس للخصوصية لأنه يلبي في وقت واحد عدة معايير مهمة. نتحقق من أن التعريف المخفف يرث العديد من نفس الخصائص. يتم تلخيص نتائج هذا القسم في الجدول الأول.

## ضمان "النتائج السيئة"

تعريف الخصوصية مفيد فقط بقدر ضمانه للمساهمين بالبيانات. أبسط ضمان من هذا القبيل هو تفسير "النتائج السيئة". ضع في اعتبارك شخصًا، قلقًا بشأن بعض العواقب السلبية، يفكر فيما إذا كان سيحجب سجله من قاعدة البيانات. لنفترض أن بعض مخرجات الآلية موسومة على أنها "سيئة". يؤكد ضمان الخصوصية التفاضلية أن احتمالية ملاحظة نتيجة سيئة لن تتغير (في أي من الاتجاهين) بأكثر من عامل $e^{\varepsilon}$ سواء كان سجل أي شخص جزءًا من المدخل أم لا (للمدخلات "المتجاورة" المعرفة بشكل مناسب). هذه نتيجة فورية لتعريف الخصوصية التفاضلية، حيث المجموعة الفرعية $S$ هي اتحاد النتائج السيئة.

هذا الضمان مخفف للخصوصية التفاضلية لريني. بشكل ملموس، إذا كانت $f$ هي (α, ε)-RDP، فبواسطة المقترح 10:

$$e^{-\varepsilon} \Pr[f(D') \in S]^{\alpha/(\alpha-1)} \leq \Pr[f(D) \in S] \leq (e^{\varepsilon} \Pr[f(D') \in S])^{(\alpha-1)/\alpha}.$$

نناقش عواقب هذا التخفيف في القسم السابع.

## المتانة للمعلومات المساعدة

أمر حاسم لاعتماد الخصوصية التفاضلية كتعريف مفيد تشغيليًا هو عدم وجود افتراضات حول معرفة الخصم. بشكل أكثر رسمية، يتم التقاط الخاصية من خلال التفسير البايزي لضمانات الخصوصية، والذي يقارن المعرفة السابقة للخصم مع اللاحقة.

افترض أن الخصم لديه معرفة سابقة $p(D)$ على مجموعة المدخلات الممكنة $D \in \mathcal{D}$، ويلاحظ مخرجًا $X$ لآلية خاصة تفاضليًا ε $f$. تحقق المعرفة اللاحقة الضمان التالي لجميع أزواج المدخلات المتجاورة $D, D' \in \mathcal{D}$ وجميع $X \in \mathcal{R}$:

$$\frac{p(D|X)}{p(D'|X)} \leq e^{\varepsilon} \frac{p(D)}{p(D')}.$$

بعبارة أخرى، فإن الأدلة التي تم الحصول عليها من آلية خاصة تفاضليًا ε لا تحرك الاحتماليات النسبية المخصصة للمدخلات المتجاورة (نسبة الاحتمالات) بأكثر من $e^{\varepsilon}$.

الضمان الذي تنطوي عليه RDP هو بيان احتمالي حول التغيير في عامل بايز. دع المتغير العشوائي $R(D, D')$ يتم تعريفه على النحو التالي:

$$R(D, D') \sim \frac{p(D'|X)}{p(D|X)} = \frac{p(X|D') \cdot p(D')}{p(X|D) \cdot p(D)},$$

حيث $X \sim f(D)$.

يتبع مباشرة من التعريف أن اختلاف ريني من الرتبة α بين $P = f(D')$ و$Q = f(D)$ يحد العزم α-th للتغيير في $R$:

$$\mathbb{E}_Q\left[\left(\frac{R_{\text{post}}(D, D')}{R_{\text{prior}}(D, D')}\right)^{\alpha}\right] = \mathbb{E}_Q\left[\left(\frac{P(x)}{Q(x)}\right)^{\alpha}\right] = \exp[(\alpha - 1)D_{\alpha}(f(D') \| f(D))].$$

بأخذ اللوغاريتم لكلا الجانبين وتطبيق متباينة جنسن نحصل على

$$\mathbb{E}_{f(D)}[\log R_{\text{post}}(D, D') - \log R_{\text{prior}}(D, D')] \leq D_{\alpha}(f(D) \| f(D')).$$

(يمكن أيضًا اشتقاق ذلك من خلال ملاحظة أن

$$\mathbb{E}_{f(D)}[\log R_{\text{post}}(D, D') - \log R_{\text{prior}}(D, D')] = D_1(f(D) \| f(D'))$$

ومن خلال رتابة اختلاف ريني.)

قارن (1) مع ضمان الخصوصية التفاضلية النقية، والذي ينص على أن $\log R_{\text{post}}(D, D') - \log R_{\text{prior}}(D, D') \leq \varepsilon$ في كل مكان، وليس فقط في التوقع.

## المعالجة اللاحقة

من غير المرجح أن يكون ضمان الخصوصية الذي يمكن تقليله عن طريق معالجة المخرجات مفيدًا. ضع في اعتبارك تعيينًا عشوائيًا $g : \mathcal{R} \mapsto \mathcal{R}'$. نلاحظ أن $D_{\alpha}(P \| Q) \geq D_{\alpha}(g(P) \| g(Q))$ بواسطة نظير متباينة معالجة البيانات [19، النظرية 9]. هذا يعني أنه إذا كانت $f(\cdot)$ هي (α, ε)-RDP، فكذلك $g(f(\cdot))$. بعبارة أخرى، يتم الحفاظ على الخصوصية التفاضلية لريني بواسطة المعالجة اللاحقة.

## الحفاظ تحت التركيب المتسلسل التكيفي

الخاصية التي تجعل من الممكن البناء المعياري للخوارزميات الخاصة تفاضليًا هي التركيب الذاتي: إذا كانت $f(\cdot)$ خاصة تفاضليًا $\varepsilon_1$ و$g(\cdot)$ خاصة تفاضليًا $\varepsilon_2$، فإن الإصدار المتزامن لـ $f(D)$ و$g(D)$ خاص تفاضليًا $\varepsilon_1 + \varepsilon_2$. يمتد الضمان حتى عندما يتم اختيار $g$ بشكل تكيفي بناءً على مخرجات $f$: إذا تم فهرسة $g$ بواسطة عناصر $\mathcal{R}$ و$g_X(\cdot)$ خاص تفاضليًا $\varepsilon_2$ لأي $X \in \mathcal{R}$، فإن نشر $(X, Y)$، حيث $X \sim f(D)$ و$Y \sim g_X(D)$، خاص تفاضليًا $\varepsilon_1 + \varepsilon_2$.

نثبت بيانًا مشابهًا لتركيب آليتي RDP.

**المقترح 1.** ليكن $f : \mathcal{D} \mapsto \mathcal{R}_1$ هو (α, $\varepsilon_1$)-RDP و$g : \mathcal{R}_1 \times \mathcal{D} \mapsto \mathcal{R}_2$ هو (α, $\varepsilon_2$)-RDP، فإن الآلية المعرفة على أنها $(X, Y)$، حيث $X \sim f(D)$ و$Y \sim g(X, D)$، تحقق (α, $\varepsilon_1 + \varepsilon_2$)-RDP.

**البرهان.** ليكن $h : \mathcal{D} \mapsto \mathcal{R}_1 \times \mathcal{R}_2$ هي نتيجة تشغيل $f$ و$g$ بالتسلسل. نكتب $X$، $Y$، و$Z$ للتوزيعات $f(D)$، $g(X, D)$، والتوزيع المشترك $(X, Y) = h(D)$. $X'$، $Y'$، و$Z'$ معرفة بشكل مماثل إذا كان المدخل هو $D'$. ثم

$$\exp[(\alpha - 1)D_{\alpha}(h(D) \| h(D'))] = \int_{\mathcal{R}_1 \times \mathcal{R}_2} Z(x, y)^{\alpha} Z'(x, y)^{1-\alpha} dx dy$$

$$= \int_{\mathcal{R}_1} \int_{\mathcal{R}_2} (X(x)Y(x, y))^{\alpha} (X'(x)Y'(x, y))^{1-\alpha} dy dx$$

$$= \int_{\mathcal{R}_1} X(x)^{\alpha} X'(x)^{1-\alpha} \left[\int_{\mathcal{R}_2} Y(x, y)^{\alpha} Y'(x, y)^{1-\alpha} dy\right] dx$$

$$\leq \int_{\mathcal{R}_1} X(x)^{\alpha} X'(x)^{1-\alpha} dx \cdot \exp((\alpha - 1)\varepsilon_2)$$

$$\leq \exp((\alpha - 1)\varepsilon_1) \exp((\alpha - 1)\varepsilon_2) = \exp((\alpha - 1)(\varepsilon_1 + \varepsilon_2)),$$

ومن ذلك يتبع الادعاء.

والمهم أن الضمان يصمد سواء كانت إصدارات $f$ و$g$ منسقة أم لا، أو محسوبة على نفس الإصدار أو إصدارات مختلفة من مجموعة البيانات المدخلة. يسمح لنا بالعمل مع مفهوم محدد جيدًا لميزانية الخصوصية المرتبطة بفرد، وهو مورد محدود يتم استهلاكه مع كل إصدار بيانات خاص تفاضليًا.

توسيعًا لمفهوم ميزانية الخصوصية، نقول إن الخصوصية التفاضلية لريني لها منحنى ميزانية معامل بالرتبة α. نقدم أمثلة توضح هذا المنظور في القسم السادس.

## خصوصية المجموعة

على الرغم من أن تعريف الخصوصية التفاضلية يقيد مخرجات الآلية على أزواج من المدخلات المتجاورة، فإن ضمانها يمتد، في شكل أضعف تدريجيًا، إلى المدخلات الأبعد. لهذه الخاصية عواقب مهمتان. أولاً، يتدهور ضمان الخصوصية التفاضلية بلطف إذا كانت افتراضاتنا حول تأثير شخص واحد على المدخل (إلى حد ما) خاطئة. على سبيل المثال، من المحتمل أن تشترك عائلة واحدة تساهم في استطلاع في العديد من الخصائص الاجتماعية والاقتصادية والديموغرافية والصحية. بدلاً من الانهيار، سيتم تقليل ضمان الخصوصية التفاضلية خطيًا مع عدد أفراد الأسرة. ثانيًا، تسمح خاصية خصوصية المجموعة بالمعالجة المسبقة للمدخلات في آلية خاصة تفاضليًا، مما قد يضخم (بطريقة خاضعة للرقابة) تأثير سجل واحد على مخرجات الحساب.

نحدد خصوصية المجموعة باستخدام مفهوم التحويل c-stable [20]. نقول إن $g : \mathcal{D} \mapsto \mathcal{D}'$ هي c-stable إذا كان $g(A)$ و$g(B)$ متجاورين في $\mathcal{D}'$ يعني أنه يوجد تسلسل بطول $c + 1$ بحيث $D_0 = A, \ldots, D_c = B$ وجميع $(D_i, D_{i+1})$ متجاورون في $\mathcal{D}$.

يحقق المفهوم القياسي للخصوصية التفاضلية ما يلي. إذا كانت $f$ خاصة تفاضليًا ε و$g : \mathcal{D}' \mapsto \mathcal{D}$ هي c-stable، فإن $f \circ g$ خاصة تفاضليًا $c\varepsilon$. يصمد بيان مماثل للخصوصية التفاضلية لريني.

**المقترح 2.** إذا كانت $f : \mathcal{D} \mapsto \mathcal{R}$ هي (α, ε)-RDP، و$g : \mathcal{D}' \mapsto \mathcal{D}$ هي $2^c$-stable و$\alpha \geq 2^{c+1}$، فإن $f \circ g$ هي (α/$2^c$, $3^c \varepsilon$)-RDP.

**البرهان.** نثبت البيان لـ $c = 1$، والباقي يتبع بالحث.

عرّف $h = f \circ g$. بما أن $g$ هي 2-stable، فهذا يعني أنه لأي $D, D' \in \mathcal{D}'$ متجاورين يوجد $A \in \mathcal{D}$، بحيث $g(D)$ و$A$، و$A$ و$g(D')$ متجاورون في $\mathcal{D}$.

بواسطة النتيجة 4 ورتابة اختلاف ريني، لدينا أن $h = f \circ g$ يحقق

$$D_{\alpha/2}(h(D) \| h(D')) \leq \frac{\alpha - 1}{\alpha - 2} D_{\alpha}(h(D) \| h(A)) + D_{\alpha-1}(h(A) \| h(D')) \leq 3\varepsilon.$$

---

### Translation Notes

- **Key terms introduced:**
  - Rényi divergence (اختلاف ريني)
  - Kullback-Leibler divergence (اختلاف كولباك-ليبلر)
  - relative entropy (الإنتروبيا النسبية)
  - Bayes factor (عامل بايز)
  - odds ratio (نسبة الاحتمالات)
  - post-processing (المعالجة اللاحقة)
  - adaptive sequential composition (التركيب المتسلسل التكيفي)
  - budget curve (منحنى الميزانية)
  - group privacy (خصوصية المجموعة)
  - c-stable transformation (التحويل c-stable)

- **Figures referenced:** Table I (الجدول الأول)
- **Equations:** Multiple mathematical definitions, propositions, and proofs
- **Citations:** [6], [17], [18], [19], [20]
- **Special handling:** Complex mathematical proofs require careful preservation of logical flow

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
