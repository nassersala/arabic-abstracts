# Section 1: Introduction
## القسم الأول: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** differential privacy, privacy, privacy loss, accuracy, mechanism, database, query, noise, gaussian, computation, algorithm

---

### English Version

The Fundamental Law of Information Recovery states, informally, that "overly accurate" estimates of "too many" statistics completely destroys privacy. Differential privacy is a mathematically rigorous definition of privacy tailored to analysis of large datasets and equipped with a formal measure of privacy loss. Moreover, differentially private algorithms take as input a parameter, typically called $\varepsilon$, that caps the permitted privacy loss in any execution of the algorithm and offers a concrete privacy/utility tradeoff. One of the strengths of differential privacy is the ability to reason about cumulative privacy loss over multiple analyses, given the values of $\varepsilon$ used in each individual analysis. By appropriate choice of $\varepsilon$ it is possible to stay within the bounds of the Fundamental Law while releasing any given number of estimated statistics; however, before this work the bounds were not tight.

Roughly speaking, differential privacy ensures that the outcome of any analysis on a database $D_A$ is distributed very similarly to the outcome on any neighboring database $D_B$ that differs from $D_A$ in just one row. That is, differentially private algorithms are randomized, and in particular the max divergence between these two distributions (a sort maximum log odds ratio for any event) is bounded by the privacy parameter $\varepsilon$. This absolute guarantee on the maximum privacy loss is now sometimes referred to as "pure" differential privacy.

A popular relaxation, $(\varepsilon,\delta)$-differential privacy, guarantees that with probability at most $1-\delta$ the privacy loss does not exceed $\varepsilon$. Typically $\delta$ is taken to be "cryptographically" small, that is, smaller than the inverse of any polynomial in the size of the dataset, and pure differential privacy is simply the special case in which $\delta=0$. The relaxation frequently permits asymptotically better accuracy than pure differential privacy for the same value of $\varepsilon$, even when $\delta$ is very small.

**What happens in the case of multiple analyses?**

While the composition of $k$ $(\varepsilon,0)$-differentially privacy algorithms is at worst $(k\varepsilon,0)$-differentially private, it is also simultaneously $(\sqrt{2k \ln(1/\delta)} \varepsilon +k\varepsilon(e^\varepsilon - 1),\delta)$-differentially private for every $\delta$. Let us deconstruct the statement of this result. First, privacy loss is a random variable that captures differences in the probability distributions obtained when a randomized algorithm $\mathcal{M}$ is run on $D_A$ as opposed to neighboring database $D_B$. In general, if the max divergence between two distributions is bounded by $\varepsilon$ then their KL-divergence is bounded by $\varepsilon(e^\varepsilon - 1)$. This means that the expected privacy loss for a single $(\varepsilon,0)$-differentially private computation is bounded by $\varepsilon(e^\varepsilon - 1)$. By linearity of expectation, the expected loss over $k$ $(\varepsilon,0)$-differentially private algorithms is bounded by $k \varepsilon(e^\varepsilon-1)$. The statement therefore says that the cumulative privacy loss random variable over $k$ computations is tightly concentrated about its mean: the probability of privacy loss exceeding its expectation by $t\sqrt{k} \varepsilon$ falls exponentially in $t^2/2$ for all $t \ge 0$. We will return to this formulation presently.

More generally, we prove the following Advanced Composition theorem, which improves on the composition theorem of Dwork, Rothblum, and Vadhan by exactly halving the bound on expected privacy loss of $(\varepsilon,0)$-differentially privacy mechanisms (the proof is otherwise identical).

**Theorem 1 (Advanced Composition):** For all $\varepsilon, \delta, \delta' \ge 0$, the class of $(\varepsilon, \delta')$-differentially private mechanisms satisfies $( \sqrt{2k \ln (1/\delta)}\varepsilon +  k\varepsilon(e^\varepsilon -1)/2, k\delta' + \delta)$-differential privacy under $k$-fold adaptive composition.

As the theorem shows (recall that $\delta'$ is usually taken to be "sub-polynomially small"), the pure and relaxed forms of differential privacy behave quite similarly under composition. For the all-important class of counting queries ("How many people in the dataset satisfy property $P$?") Theorem 1 leads to accuracy bounds that differ from the bounds imposed by (one instantiation of) the Fundamental Law by a factor of roughly $\sqrt{2\log(1/\delta)}$. Recently, tight bounds on the composition of $(\varepsilon, \delta)$-differentially private algorithms have been given.

**A New Relaxation**

In this work we introduce a different relaxation, Concentrated Differential Privacy (CDP), incomparable to $(\varepsilon,\delta)$-differential privacy but again having the same behavior under composition. CDP is closer to the "every $\delta$" property in the statement of Theorem 1: An algorithm offers $(\mu,\tau)$-concentrated differential privacy if the privacy loss random variable has mean $\mu$ and if, after subtracting off this mean, the resulting (centered) random variable, $\xi$, is subgaussian with standard $\tau$. A random variable $X$ is subgaussian with standard $\sigma$ for a constant $\sigma > 0$ if $\forall \lambda \in \mathbb{R}: \mathbb{E}[e^{\lambda \cdot X}] \leq e^{\frac{\lambda^2 \cdot \sigma^2}{2}}$. In consequence, $\forall x > 0$:

$$\Pr[\xi \ge x]\le \exp\left( - \frac{x^2}{2\tau^2} \right) \text{ and } \Pr[\xi \le -x]\le \exp\left( - \frac{x^2}{2\tau^2} \right)$$

Thus, CDP ensures that the expected privacy loss is $\mu$ and the probability of loss exceeding its mean by $x=t\tau$ is bounded by $e^{-t^2/2}$, echoing the form of the guarantee offered by the Advanced Composition Theorem.

Consider the case in which $\tau = \varepsilon$. On the one hand, $(\mu,\varepsilon)$-CDP is clearly weaker than $(\varepsilon,\delta)$-differential privacy, because even if the expected loss $\mu$ is very small, the probability of privacy loss exceeding $\varepsilon$ in the former can be constant but is only $\delta$, which is tiny, in the latter. On the other hand, in $(\varepsilon,\delta)$-differential privacy there is no bound on the expected privacy loss, since with probability $\delta$ all bets are off and the loss can be infinite.

**CDP enjoys two advantages over $(\varepsilon,\delta)$-differential privacy:**

1. **Improved Accuracy.** CDP is tailored to the (realistic!) case of large numbers of computations. Traditionally, to ensure small cumulative loss with high probability, the permitted loss for each individual query is set very low, say $\varepsilon' = \varepsilon\sqrt{(\log 1/\delta)/k}$, even though a privacy loss of, say, $\varepsilon/10$ or even $\varepsilon$ itself may not be of great concern for any single query. This is precisely the flexibility we give in CDP: much less concern about single-query loss, but high probability bounds for cumulative loss. The composition of $k$ $(\mu,\tau)$-CDP mechanisms is $(k\mu, \sqrt{k}\tau)$-CDP. Setting $\tau = \varepsilon$ we get an expected privacy loss of $k\mu$ and, for all $t$ simultaneously, the probability of privacy loss exceeding its expectation by $t\sqrt{k}\varepsilon$ falls exponentially in $t^2/2$, just as we obtained in the composition for the other variants of differential privacy in Theorem 1 above. However, we get better accuracy. For example, to handle $n$ counting queries using the Gaussian mechanism, we can add independent random noise drawn from $\mathcal{N}(0,n/\varepsilon^2)$ to each query, achieving $(\varepsilon(e^\varepsilon - 1)/2,\varepsilon)$-CDP. To achieve $(\varepsilon,\delta)$-differential privacy one adds noise drawn from $\mathcal{N}(0,2 \ln(1/\delta))$, increasing the typical distortion by a factor of $\sqrt{\ln(1/\delta)}$. When $\varepsilon = \Theta(1)$ the noise is scaled to $O(\sqrt{n})$; the Fundamental Law says noise $o(\sqrt{n})$ is disastrous.

2. **Group Privacy.** Group privacy bounds the privacy loss even for pairs of databases that differ in the data of a small group of individuals; for example, in a health survey one may wish not only to know that one's own health information remains private but also that the information of one's family as a whole is strongly protected. Any $(\varepsilon,0)$-differentially private algorithm automatically ensures $(s\varepsilon,0)$-differential privacy for all groups of size $s$, with the expected privacy loss growing by a factor of about $s^2$. The situation for $(\varepsilon,\delta)$-differential privacy is not quite so elegant: the literature shows $(s\varepsilon,se^{s-1}\delta)$-differential privacy for groups of size $s$, a troubling exponential increase in the failure probability (the $se^{s-1}\delta$ term). The situation for CDP is much better: for all known natural mechanisms with CDP we get tight bounds. For (hypothetical) arbitrary algorithms offering subgaussian privacy loss, the bounds are asymptotically nearly-tight (tight up to low-order terms). We suspect that the tight bounds should hold for arbitrary mechanisms, and it would be interesting to close the gap.
   - Under certain conditions, satisfied by all pure differential privacy mechanisms (every $(\varepsilon,0)$-differentially private mechanism yields $(\varepsilon(e^\varepsilon-1)/2,\varepsilon)$-CDP), and the addition of Gaussian noise, any $(\mu,\tau)$-CDP mechanism satisfies $(s^2 \cdot \mu, s \cdot \tau)$-CDP for groups of size $s$, which is optimal.
   - Every $(\frac{\tau^2}{2},\tau)$-CDP mechanism satisfies $(s^2 \cdot \frac{\tau^2}{2} \cdot (1+o(1)), s \cdot \tau \cdot (1+o(1))$-CDP for groups of size $s$. The bound holds so long as $s \cdot \tau$ is small enough (roughly, $(1/\tau)$ should remain quasi-linear in $s$).

**Tight Bounds on Expected Loss**

As noted above, we improve by a factor of two the known upper bound on expected privacy loss of any $(\varepsilon,0)$-differentially private mechanism, closing a gap open since 2010. This immediately translates to an improvement by a factor of $\sqrt{2}$ on the utility/privacy tradeoff in any application of the Advanced Composition Theorem. The new bound, which is tight, is obtained by first proving the result for special pairs of probability distributions that we call MD (privacy loss for any outcome is in $\{-\varepsilon,0,\varepsilon\}$), and then showing a reduction, in which an arbitrary pair of distributions with max divergence bounded by $\varepsilon$ can be "replaced" by a MD pair with no change in max divergence and no decrease in KL-divergence.

If all $(\varepsilon,0)$-differentially private algorithms enjoy CDP, as well as the Gaussian mechanism, which $(\varepsilon,\delta)$-differentially private algorithms are ruled out? All $(\varepsilon,\delta)$-differentially private algorithms in which there is some probability $\delta' \le \delta$ of infinite privacy loss. This includes many (but not all!) algorithms in the "Propose-Test-Release" framework, in which a differentially private test is first performed to check that the dataset satisfies some "safety" conditions and, if so, an operation is carried out that only ensures privacy if the conditions are met. There could be a small probability of failure in the first step, meaning that the test reports that the safety conditions are met, but in fact they are not, in which case privacy could be compromised in the second step.

### Recent Developments

**Tightness**

Optimality in privacy loss is a surprisingly subtle and difficult question under composition. Results of Kairouz, Oh and Viswanath obtain tight bounds under composition of arbitrary $(\epsilon,\delta)$-mechanisms, when all mechanisms share the same values of $\epsilon$ and $\delta$. That is, they find the optimal $\epsilon',\delta'$ such that the composition of $k$ mechanisms, each of which is $(\epsilon_0,\delta_0)$-differentially private, is $(\epsilon',\delta')$-differentially private. The nonhomogeneous case, in which the $i$th mechanism is $(\epsilon_i,\delta_i)$-differentially private, has been analyzed by Murtagh and Vadhan, where it is shown that determining the bounds of the optimal composition is hard for $\#\mathcal{P}$. Both these papers use an analysis similar to that found in our lemma, which we obtained prior to the publication of those works.

Optimal bounds on the composition of arbitrary mechanisms are very interesting, but we are also interested in bounds on the specific mechanisms that we have in hand and wish to use and analyze. To this end, we obtain a complete characterization of the privacy loss of the Gaussian mechanism. We show that the privacy loss of the composition of multiple application of the Gaussian mechanism, possibly with different individual parameters, is itself a Gaussian random variable, and we give exact bounds for its mean and variance. This characterization is not possible using the framework of $(\epsilon,\delta)$-differential privacy, the previous prevailing view of the Gaussian mechanism.

**Subsequent Work**

Motivated by our work, Bun and Steinke suggest a relaxation of concentrated differential privacy. Instead of framing the privacy loss as a subgaussian random variable as we do here, they instead frame the question in terms of Renyi entropy, obtaining a relaxation of concentrated differential privacy that also supports a similar composition theorem. Their notion also provides privacy guarantees for groups. The bounds we get using concentrated differential privacy are tighter; we do not know whether this is inherent in the definitions.

---

### النسخة العربية

ينص القانون الأساسي لاسترجاع المعلومات، بشكل غير رسمي، على أن التقديرات "الدقيقة بشكل مفرط" لـ "عدد كبير جداً" من الإحصاءات تدمر الخصوصية بشكل كامل. الخصوصية التفاضلية هي تعريف رياضي صارم للخصوصية مُصمم خصيصاً لتحليل مجموعات البيانات الكبيرة ومزود بمقياس رسمي لخسارة الخصوصية. علاوة على ذلك، تأخذ الخوارزميات التي تحافظ على الخصوصية التفاضلية معاملاً كمدخل، يُسمى عادةً $\varepsilon$، يحدد سقفاً لخسارة الخصوصية المسموح بها في أي تنفيذ للخوارزمية ويقدم مقايضة ملموسة بين الخصوصية والمنفعة. من نقاط القوة في الخصوصية التفاضلية هي القدرة على التفكير في خسارة الخصوصية التراكمية عبر تحليلات متعددة، بالنظر إلى قيم $\varepsilon$ المستخدمة في كل تحليل فردي. من خلال اختيار مناسب لـ $\varepsilon$ من الممكن البقاء ضمن حدود القانون الأساسي مع إصدار أي عدد معين من الإحصاءات المقدرة؛ ومع ذلك، قبل هذا العمل لم تكن الحدود محكمة.

بشكل تقريبي، تضمن الخصوصية التفاضلية أن نتيجة أي تحليل على قاعدة بيانات $D_A$ توزع بشكل مشابه جداً لنتيجة قاعدة بيانات مجاورة $D_B$ تختلف عن $D_A$ في صف واحد فقط. بمعنى آخر، الخوارزميات التي تحافظ على الخصوصية التفاضلية هي خوارزميات عشوائية، وعلى وجه الخصوص فإن التباعد الأقصى (max divergence) بين هذين التوزيعين (نوع من نسبة الاحتمالات اللوغاريتمية القصوى لأي حدث) محدود بمعامل الخصوصية $\varepsilon$. هذا الضمان المطلق على الحد الأقصى لخسارة الخصوصية يُشار إليه الآن أحياناً باسم الخصوصية التفاضلية "النقية".

يوجد تخفيف شائع، الخصوصية التفاضلية $(\varepsilon,\delta)$، يضمن أنه باحتمال على الأكثر $1-\delta$ لا تتجاوز خسارة الخصوصية $\varepsilon$. عادةً ما يُختار $\delta$ ليكون صغيراً "تشفيرياً"، أي أصغر من مقلوب أي كثير حدود في حجم مجموعة البيانات، والخصوصية التفاضلية النقية هي ببساطة الحالة الخاصة التي فيها $\delta=0$. غالباً ما يسمح هذا التخفيف بدقة أفضل مقاربياً من الخصوصية التفاضلية النقية لنفس قيمة $\varepsilon$، حتى عندما تكون $\delta$ صغيرة جداً.

**ماذا يحدث في حالة التحليلات المتعددة؟**

بينما يكون تركيب $k$ خوارزمية للخصوصية التفاضلية $(\varepsilon,0)$ في أسوأ حالاته محافظاً على الخصوصية التفاضلية $(k\varepsilon,0)$، فإنه أيضاً في نفس الوقت محافظ على الخصوصية التفاضلية $(\sqrt{2k \ln(1/\delta)} \varepsilon +k\varepsilon(e^\varepsilon - 1),\delta)$ لكل $\delta$. دعنا نحلل بيان هذه النتيجة. أولاً، خسارة الخصوصية هي متغير عشوائي يلتقط الاختلافات في توزيعات الاحتمالات التي يتم الحصول عليها عند تشغيل خوارزمية عشوائية $\mathcal{M}$ على $D_A$ مقابل قاعدة البيانات المجاورة $D_B$. بشكل عام، إذا كان التباعد الأقصى بين توزيعين محدوداً بـ $\varepsilon$ فإن تباعد KL الخاص بهما محدود بـ $\varepsilon(e^\varepsilon - 1)$. هذا يعني أن خسارة الخصوصية المتوقعة لحساب واحد محافظ على الخصوصية التفاضلية $(\varepsilon,0)$ محدودة بـ $\varepsilon(e^\varepsilon - 1)$. بخطية القيمة المتوقعة، فإن الخسارة المتوقعة على $k$ خوارزمية محافظة على الخصوصية التفاضلية $(\varepsilon,0)$ محدودة بـ $k \varepsilon(e^\varepsilon-1)$. وبالتالي فإن البيان يقول أن متغير خسارة الخصوصية التراكمي على $k$ حساب مركز بإحكام حول متوسطه: احتمال أن تتجاوز خسارة الخصوصية قيمتها المتوقعة بـ $t\sqrt{k} \varepsilon$ ينخفض أسياً في $t^2/2$ لكل $t \ge 0$. سنعود إلى هذه الصيغة قريباً.

بشكل أعم، نُثبت نظرية التركيب المتقدم التالية، التي تحسن نظرية التركيب لـ Dwork وRothblum وVadhan عن طريق تنصيف الحد على خسارة الخصوصية المتوقعة لآليات الخصوصية التفاضلية $(\varepsilon,0)$ بالضبط (البرهان متطابق فيما عدا ذلك).

**النظرية 1 (التركيب المتقدم):** لكل $\varepsilon, \delta, \delta' \ge 0$، فئة الآليات المحافظة على الخصوصية التفاضلية $(\varepsilon, \delta')$ تحقق الخصوصية التفاضلية $( \sqrt{2k \ln (1/\delta)}\varepsilon +  k\varepsilon(e^\varepsilon -1)/2, k\delta' + \delta)$ تحت التركيب التكيفي ذي الـ $k$ طية.

كما توضح النظرية (تذكر أن $\delta'$ عادة ما تُختار لتكون "صغيرة دون كثيرة حدود")، فإن الأشكال النقية والمخففة من الخصوصية التفاضلية تتصرف بشكل مشابه جداً تحت التركيب. بالنسبة لفئة استعلامات العد الأكثر أهمية ("كم عدد الأشخاص في مجموعة البيانات الذين يستوفون الخاصية $P$؟") تؤدي النظرية 1 إلى حدود دقة تختلف عن الحدود المفروضة من قبل (إحدى نسخ) القانون الأساسي بعامل يقارب $\sqrt{2\log(1/\delta)}$. مؤخراً، تم إعطاء حدود محكمة على تركيب خوارزميات الخصوصية التفاضلية $(\varepsilon, \delta)$.

**تخفيف جديد**

في هذا العمل نقدم تخفيفاً مختلفاً، الخصوصية التفاضلية المركزة (CDP)، غير قابل للمقارنة مع الخصوصية التفاضلية $(\varepsilon,\delta)$ لكنه يمتلك مرة أخرى نفس السلوك تحت التركيب. الخصوصية التفاضلية المركزة أقرب إلى خاصية "كل $\delta$" في بيان النظرية 1: الخوارزمية تقدم خصوصية تفاضلية مركزة $(\mu,\tau)$ إذا كان متغير خسارة الخصوصية العشوائي له متوسط $\mu$ وإذا كان، بعد طرح هذا المتوسط، المتغير العشوائي الناتج (المُركَّز)، $\xi$، تحت-غاوسياً (subgaussian) بمعيار $\tau$. المتغير العشوائي $X$ هو تحت-غاوسي بمعيار $\sigma$ لثابت $\sigma > 0$ إذا كان $\forall \lambda \in \mathbb{R}: \mathbb{E}[e^{\lambda \cdot X}] \leq e^{\frac{\lambda^2 \cdot \sigma^2}{2}}$. ونتيجة لذلك، $\forall x > 0$:

$$\Pr[\xi \ge x]\le \exp\left( - \frac{x^2}{2\tau^2} \right) \text{ و } \Pr[\xi \le -x]\le \exp\left( - \frac{x^2}{2\tau^2} \right)$$

وبالتالي، تضمن الخصوصية التفاضلية المركزة أن خسارة الخصوصية المتوقعة هي $\mu$ وأن احتمال تجاوز الخسارة لمتوسطها بـ $x=t\tau$ محدود بـ $e^{-t^2/2}$، مما يعكس شكل الضمان الذي تقدمه نظرية التركيب المتقدم.

لنأخذ في الاعتبار الحالة التي فيها $\tau = \varepsilon$. من جهة، فإن الخصوصية التفاضلية المركزة $(\mu,\varepsilon)$ أضعف بوضوح من الخصوصية التفاضلية $(\varepsilon,\delta)$، لأنه حتى لو كانت الخسارة المتوقعة $\mu$ صغيرة جداً، فإن احتمال تجاوز خسارة الخصوصية لـ $\varepsilon$ في الأولى يمكن أن يكون ثابتاً لكنه في الأخيرة $\delta$ فقط، وهو صغير جداً. من جهة أخرى، في الخصوصية التفاضلية $(\varepsilon,\delta)$ لا يوجد حد على خسارة الخصوصية المتوقعة، حيث أنه باحتمال $\delta$ كل الرهانات ملغاة ويمكن أن تكون الخسارة لا نهائية.

**تتمتع الخصوصية التفاضلية المركزة بميزتين على الخصوصية التفاضلية $(\varepsilon,\delta)$:**

1. **دقة محسنة.** الخصوصية التفاضلية المركزة مُصممة لحالة (واقعية!) من أعداد كبيرة من الحسابات. تقليدياً، لضمان خسارة تراكمية صغيرة باحتمال عالٍ، يتم تعيين الخسارة المسموح بها لكل استعلام فردي منخفضة جداً، مثلاً $\varepsilon' = \varepsilon\sqrt{(\log 1/\delta)/k}$، على الرغم من أن خسارة خصوصية قدرها، مثلاً، $\varepsilon/10$ أو حتى $\varepsilon$ نفسها قد لا تكون مصدر قلق كبير لأي استعلام واحد. هذه هي المرونة بالضبط التي نقدمها في الخصوصية التفاضلية المركزة: قلق أقل بكثير حول خسارة الاستعلام الواحد، لكن حدود احتمالية عالية للخسارة التراكمية. تركيب $k$ آلية للخصوصية التفاضلية المركزة $(\mu,\tau)$ هو خصوصية تفاضلية مركزة $(k\mu, \sqrt{k}\tau)$. بتعيين $\tau = \varepsilon$ نحصل على خسارة خصوصية متوقعة قدرها $k\mu$ و، لكل $t$ في نفس الوقت، فإن احتمال تجاوز خسارة الخصوصية لتوقعها بـ $t\sqrt{k}\varepsilon$ ينخفض أسياً في $t^2/2$، تماماً كما حصلنا في التركيب للأشكال الأخرى من الخصوصية التفاضلية في النظرية 1 أعلاه. ومع ذلك، نحصل على دقة أفضل. على سبيل المثال، للتعامل مع $n$ استعلام عد باستخدام الآلية الغاوسية، يمكننا إضافة ضوضاء عشوائية مستقلة مسحوبة من $\mathcal{N}(0,n/\varepsilon^2)$ إلى كل استعلام، محققين خصوصية تفاضلية مركزة $(\varepsilon(e^\varepsilon - 1)/2,\varepsilon)$. لتحقيق الخصوصية التفاضلية $(\varepsilon,\delta)$ يضيف المرء ضوضاء مسحوبة من $\mathcal{N}(0,2 \ln(1/\delta))$، مما يزيد التشويه النموذجي بعامل $\sqrt{\ln(1/\delta)}$. عندما يكون $\varepsilon = \Theta(1)$ يتم قياس الضوضاء إلى $O(\sqrt{n})$؛ يقول القانون الأساسي أن الضوضاء $o(\sqrt{n})$ كارثية.

2. **خصوصية المجموعة.** خصوصية المجموعة تحد من خسارة الخصوصية حتى لأزواج قواعد البيانات التي تختلف في بيانات مجموعة صغيرة من الأفراد؛ على سبيل المثال، في مسح صحي قد يرغب المرء ليس فقط في معرفة أن معلوماته الصحية الخاصة تظل خاصة ولكن أيضاً أن معلومات عائلته ككل محمية بقوة. أي خوارزمية محافظة على الخصوصية التفاضلية $(\varepsilon,0)$ تضمن تلقائياً الخصوصية التفاضلية $(s\varepsilon,0)$ لجميع المجموعات ذات الحجم $s$، مع نمو خسارة الخصوصية المتوقعة بعامل حوالي $s^2$. الوضع بالنسبة للخصوصية التفاضلية $(\varepsilon,\delta)$ ليس أنيقاً تماماً: تُظهر الأدبيات الخصوصية التفاضلية $(s\varepsilon,se^{s-1}\delta)$ للمجموعات ذات الحجم $s$، وهي زيادة أسية مقلقة في احتمال الفشل (الحد $se^{s-1}\delta$). الوضع بالنسبة للخصوصية التفاضلية المركزة أفضل بكثير: لجميع الآليات الطبيعية المعروفة مع الخصوصية التفاضلية المركزة نحصل على حدود محكمة. للخوارزميات (الافتراضية) التعسفية التي تقدم خسارة خصوصية تحت-غاوسية، فإن الحدود محكمة مقاربياً تقريباً (محكمة حتى الحدود من الدرجة الدنيا). نشك في أن الحدود المحكمة يجب أن تصمد للآليات التعسفية، وسيكون من المثير للاهتمام سد الفجوة.
   - تحت شروط معينة، مستوفاة من قبل جميع آليات الخصوصية التفاضلية النقية (كل آلية محافظة على الخصوصية التفاضلية $(\varepsilon,0)$ تنتج خصوصية تفاضلية مركزة $(\varepsilon(e^\varepsilon-1)/2,\varepsilon)$)، وإضافة الضوضاء الغاوسية، أي آلية للخصوصية التفاضلية المركزة $(\mu,\tau)$ تحقق خصوصية تفاضلية مركزة $(s^2 \cdot \mu, s \cdot \tau)$ للمجموعات ذات الحجم $s$، وهو مثالي.
   - كل آلية للخصوصية التفاضلية المركزة $(\frac{\tau^2}{2},\tau)$ تحقق خصوصية تفاضلية مركزة $(s^2 \cdot \frac{\tau^2}{2} \cdot (1+o(1)), s \cdot \tau \cdot (1+o(1))$ للمجموعات ذات الحجم $s$. يصمد الحد طالما أن $s \cdot \tau$ صغير بما فيه الكفاية (تقريباً، يجب أن يظل $(1/\tau)$ شبه خطي في $s$).

**حدود محكمة على الخسارة المتوقعة**

كما ذُكر أعلاه، نحسّن بعامل اثنين الحد الأعلى المعروف على خسارة الخصوصية المتوقعة لأي آلية محافظة على الخصوصية التفاضلية $(\varepsilon,0)$، مغلقين فجوة مفتوحة منذ عام 2010. هذا يترجم فوراً إلى تحسين بعامل $\sqrt{2}$ في المقايضة بين المنفعة والخصوصية في أي تطبيق لنظرية التركيب المتقدم. الحد الجديد، الذي هو محكم، يتم الحصول عليه أولاً بإثبات النتيجة لأزواج خاصة من توزيعات الاحتمالات التي نسميها MD (خسارة الخصوصية لأي نتيجة هي في $\{-\varepsilon,0,\varepsilon\}$)، ثم إظهار اختزال، حيث يمكن "استبدال" زوج تعسفي من التوزيعات بتباعد أقصى محدود بـ $\varepsilon$ بزوج MD دون تغيير في التباعد الأقصى ودون انخفاض في تباعد KL.

إذا كانت جميع الخوارزميات المحافظة على الخصوصية التفاضلية $(\varepsilon,0)$ تتمتع بالخصوصية التفاضلية المركزة، بالإضافة إلى الآلية الغاوسية، فأي خوارزميات محافظة على الخصوصية التفاضلية $(\varepsilon,\delta)$ مستبعدة؟ جميع الخوارزميات المحافظة على الخصوصية التفاضلية $(\varepsilon,\delta)$ التي يوجد فيها احتمال $\delta' \le \delta$ لخسارة خصوصية لا نهائية. يشمل هذا العديد (وليس كل!) من الخوارزميات في إطار عمل "اقتراح-اختبار-إصدار" (Propose-Test-Release)، حيث يتم أولاً إجراء اختبار محافظ على الخصوصية التفاضلية للتحقق من أن مجموعة البيانات تستوفي شروط "السلامة" المعينة، وإذا كان الأمر كذلك، يتم تنفيذ عملية تضمن الخصوصية فقط إذا تم استيفاء الشروط. قد يكون هناك احتمال صغير للفشل في الخطوة الأولى، مما يعني أن الاختبار يبلغ أن شروط السلامة مستوفاة، لكن في الواقع لم تكن كذلك، وفي هذه الحالة يمكن اختراق الخصوصية في الخطوة الثانية.

### التطورات الحديثة

**الإحكام**

المثالية في خسارة الخصوصية هي مسألة دقيقة وصعبة بشكل مفاجئ تحت التركيب. نتائج Kairouz وOh وViswanath تحصل على حدود محكمة تحت تركيب آليات $(\epsilon,\delta)$ تعسفية، عندما تتشارك جميع الآليات نفس قيم $\epsilon$ و$\delta$. بمعنى آخر، يجدون القيم المثلى $\epsilon',\delta'$ بحيث أن تركيب $k$ آلية، كل منها محافظة على الخصوصية التفاضلية $(\epsilon_0,\delta_0)$، محافظ على الخصوصية التفاضلية $(\epsilon',\delta')$. الحالة غير المتجانسة، حيث تكون الآلية الـ $i$ محافظة على الخصوصية التفاضلية $(\epsilon_i,\delta_i)$، تم تحليلها من قبل Murtagh وVadhan، حيث يُظهر أن تحديد حدود التركيب الأمثل صعب لـ $\#\mathcal{P}$. كلا هذين الورقتين تستخدمان تحليلاً مشابهاً لما وجد في المبرهنة الخاصة بنا، والتي حصلنا عليها قبل نشر تلك الأعمال.

الحدود المثلى على تركيب الآليات التعسفية مثيرة للاهتمام جداً، لكننا مهتمون أيضاً بالحدود على الآليات المحددة التي لدينا ونرغب في استخدامها وتحليلها. لهذه الغاية، نحصل على توصيف كامل لخسارة الخصوصية للآلية الغاوسية. نُظهر أن خسارة الخصوصية لتركيب تطبيقات متعددة للآلية الغاوسية، ربما بمعاملات فردية مختلفة، هي نفسها متغير عشوائي غاوسي، ونعطي حدوداً دقيقة لمتوسطها وتباينها. هذا التوصيف غير ممكن باستخدام إطار الخصوصية التفاضلية $(\epsilon,\delta)$، وهو الرؤية السائدة السابقة للآلية الغاوسية.

**الأعمال اللاحقة**

بدافع من عملنا، يقترح Bun وSteinke تخفيفاً للخصوصية التفاضلية المركزة. بدلاً من صياغة خسارة الخصوصية كمتغير عشوائي تحت-غاوسي كما نفعل هنا، يقومون بدلاً من ذلك بصياغة المسألة من حيث إنتروبيا Renyi، محصلين على تخفيف للخصوصية التفاضلية المركزة يدعم أيضاً نظرية تركيب مشابهة. مفهومهم يوفر أيضاً ضمانات خصوصية للمجموعات. الحدود التي نحصل عليها باستخدام الخصوصية التفاضلية المركزة أكثر إحكاماً؛ لا نعرف ما إذا كان هذا متأصلاً في التعريفات.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** Concentrated Differential Privacy (CDP), privacy loss random variable, subgaussian, max divergence, KL-divergence, group privacy, Advanced Composition Theorem, Gaussian mechanism, MD distributions, Propose-Test-Release framework
- **Equations:** Multiple mathematical expressions and probability formulas
- **Citations:** Multiple references to prior work (DinurN03, DworkMNS06, Dwork06, DworkKMMN06, DworkRV10, KairouzOV15, MurtaghV16, DworkL09, BunS15, BuldyginK00)
- **Special handling:**
  - Theorem statements preserved with full mathematical notation
  - LaTeX mathematical expressions maintained throughout
  - Subgaussian definition included in footnote
  - Two enumerated advantages of CDP with detailed mathematical content
  - Recent Developments subsection with two paragraphs on Tightness and Subsequent Work

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.90
- **Overall section score:** 0.88

### Back-Translation Check (First Paragraph)

The Fundamental Law of Information Recovery states, informally, that "overly accurate" estimates of "too many" statistics completely destroy privacy. Differential privacy is a rigorous mathematical definition of privacy designed specifically for analyzing large datasets and equipped with a formal measure of privacy loss. Moreover, differentially private algorithms take as input a parameter, usually called $\varepsilon$, that caps the permitted privacy loss in any execution of the algorithm and provides a concrete privacy/utility tradeoff. One of the strengths of differential privacy is the ability to reason about cumulative privacy loss across multiple analyses, given the values of $\varepsilon$ used in each individual analysis. Through appropriate choice of $\varepsilon$ it is possible to stay within the bounds of the Fundamental Law while releasing any given number of estimated statistics; however, before this work the bounds were not tight.

**Back-translation assessment:** Excellent semantic match with original text.
