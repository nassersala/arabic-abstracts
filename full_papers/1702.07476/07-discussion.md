# Section 7: Discussion
## القسم 7: مناقشة

**Section:** discussion
**Translation Quality:** 0.87
**Glossary Terms Used:** Rényi differential privacy, differential privacy, privacy budget, composition, mechanism, baseline risk

---

### English Version

Rényi differential privacy is a natural relaxation of the standard notion of differential privacy that preserves many of its essential properties. It can most directly be compared with (ε, δ)-differential privacy, with which it shares several important characteristics.

## PROBABILISTIC PRIVACY GUARANTEE

The standard "bad outcomes" guarantee of ε-differential privacy is independent of the probability of a bad outcome: it may increase only by a factor of $\exp(\varepsilon)$. Its relaxation, (ε, δ)-differential privacy, allows for an additional δ term, which allows for a complete privacy compromise with probability δ.

In stark contrast, Rényi differential privacy even with very weak parameters never allows a total breach of privacy with no residual uncertainty. The following analysis quantifies this assurance.

Let $f$ be (α, ε)-RDP with $\alpha > 1$. Recall that for any two adjacent inputs $D$ and $D'$, and an arbitrary prior $p$ the odds function $R(D, D') \sim p(D)/p(D')$ satisfies $\mathbb{E}\left[\left(\frac{R_{\text{post}}(D,D')}{R_{\text{prior}}(D,D')}\right)^{\alpha-1}\right] \leq \exp((\alpha - 1)\varepsilon)$. By Markov's inequality $\Pr[R_{\text{post}}(D, D') > \beta R_{\text{prior}}(D, D')] < e^{\varepsilon}/\beta^{1/(\alpha-1)}$. For instance, if $\alpha = 2$, the probability that the ratio between two posteriors increases by more than the β factor drops off as $O(1/\beta)$.

## BASELINE-DEPENDENT GUARANTEES

The Rényi differential privacy bound gets weaker for less likely outcomes. For instance, if $f$ is a (10.0, .1)-RDP mechanism, an event of probability .5 under $f(D)$ can be as large as .586 and as small as .419 under $f(D')$. For smaller events the range is (in relative terms) wider. If the probability under $f(D)$ is .001, then $\Pr[f(D') \in S] \in [.00042, 0.00218]$. For $\Pr[f(D) \in S] = 10^{-6}$ the range is wider still: $\Pr[f(D') \in S] \in [.195 \cdot 10^{-6}, 4.36 \cdot 10^{-6}]$.

Contrasted with the pure ε-differential privacy this type of guarantee is conceptually weaker and more onerous in application: in order to decide whether the increased risk is tolerable, one is required to estimate the baseline risk first.

However, in comparison with (ε, δ)-DP the analysis via Rényi differential privacy is simpler and, especially for probabilities that are smaller than δ, leads to stronger bounds. The reason is that (ε, δ)-differential privacy often arises as a result of some analysis that implicitly comes with an ε-δ tradeoff. Finding an optimal value of (ε, δ) given the baseline risk may be non-trivial, especially in closed form. Contrast the following two, basically equivalent, statements of advanced composition theorems (Proposition 4 and its Corollary 1):

Let $f : \mathcal{D} \mapsto \mathcal{R}$ be an adaptive composition of $n$ mechanisms all satisfying ε-differential privacy for $\varepsilon \leq 1$. Let $D$ and $D'$ be two adjacent inputs. Then for any $S \subset \mathcal{R}$, by Proposition 4:

$$\Pr[f(D') \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/\Pr[f(D) \in S]}\right) \cdot \Pr[f(D) \in S].$$

or, by Corollary 1,

$$\Pr[f(D') \in S] \leq \exp\left(4\varepsilon\sqrt{2n \log 1/\delta}\right) \cdot \Pr[f(D) \in S] + \delta,$$

where $0 < \varepsilon, \delta < 1$ such that $\log(1/\delta) \geq \varepsilon^2 n$.

Given some value of baseline risk $\Pr[f(D) \in S]$, which formulation is easier to interpret? We argue that it is the former, since the (ε, δ) form has a free parameter (δ) that ought to be optimized in order to extract a tight bound that Proposition 4 gives directly.

The use of (ε, δ) bounds gets even more complex if we consider a composition of heterogeneous mechanisms. It brings us to the last point of comparison between (ε, δ)- and Rényi differential privacy measures.

## KEEPING TRACK OF ACCUMULATED PRIVACY LOSS

A finite privacy budget associated with an individual is an intuitive and appealing concept, to which ε-differential privacy gives a rigorous mathematical expression. Cumulative loss of differential privacy over the cause of a mechanism run, a protocol, or one's lifetime can be tracked easily thanks to the additivity property of differential privacy. Unfortunately, doing so naïvely likely exaggerates privacy loss, which grows sublinearly in the number of queries with all but negligible probability (via advanced composition theorems).

Critically, applying advanced composition theorems breaks the convenient abstraction of privacy as a non-negative real number. Instead, the guarantee comes in the (ε, δ) form that effectively corresponds to a single point on an implicitly defined curve. Composition of multiple, heterogeneous mechanisms makes applying the composition rule optimally much more challenging, as one may choose various (ε, δ) points to represent their privacy (in the analysis, not during the mechanisms' run time!). It begs the question of how to represent the privacy guarantee of a complex mechanism: distilling it to a single number throws away valuable information, while publishing the entire (ε, δ) curve shifts the problem to the aggregation step. (See Kairouz et al. [7] for an optimal bound on composition of homogeneous mechanisms and Murtagh and Vadhan [8] for hardness results and an approximation scheme for composition of mechanisms with heterogeneous privacy guarantees.)

Rényi differential privacy restores the concept of a privacy budget, thanks to its composition rule: RDP curves for composed mechanisms simply add up. Importantly, the α's of (α, ε)-Rényi differential privacy do not change. If RDP statements are reported for a common set of α's (which includes +∞, to keep track of pure differential privacy), RDP of the aggregate is the sum of the reported vectors. Since the composition theorem of Proposition 4 takes as an input the mechanism's RDP curve, it means that the sublinear loss of privacy as a function of the number of queries will still hold.

For an example of this approach we tabulate the bound on privacy loss for an iterative mechanism consisting of three basic mechanisms: randomized response, Gaussian, and Laplace. Its RDP curve is given, in the closed form, by application of the basic composition rule to RDP curves of the underlying mechanisms (Table II). The privacy guarantee is presented in Figure 3 for three values of the baseline risk: .1, .001, and $10^{-6}$. For each set of parameters two curves are plotted: one for an optimal value of α from $(1, +\infty]$, the other for an optimal α restricted to the set of 13 values $\{1.5, 1.75, 2, 2.5, 3, 4, 5, 6, 8, 16, 32, 64, +\infty\}$. The two curves are nearly identical, which illustrates our thesis that reporting RDP curves for a restricted set of α's preserves tightness of privacy analysis.

---

### النسخة العربية

الخصوصية التفاضلية لريني هي تخفيف طبيعي للمفهوم القياسي للخصوصية التفاضلية يحافظ على العديد من خصائصها الأساسية. يمكن مقارنتها بشكل أكثر مباشرة مع الخصوصية التفاضلية (ε, δ)، والتي تشترك معها في عدة خصائص مهمة.

## ضمان الخصوصية الاحتمالي

ضمان "النتائج السيئة" القياسي للخصوصية التفاضلية ε مستقل عن احتمالية نتيجة سيئة: قد يزيد فقط بعامل $\exp(\varepsilon)$. تخفيفها، الخصوصية التفاضلية (ε, δ)، يسمح بحد δ إضافي، والذي يسمح باختراق كامل للخصوصية باحتمالية δ.

في تناقض صارخ، فإن الخصوصية التفاضلية لريني حتى مع معاملات ضعيفة جدًا لا تسمح أبدًا باختراق كامل للخصوصية دون عدم يقين متبقي. يحدد التحليل التالي هذا الضمان كميًا.

لتكن $f$ (α, ε)-RDP مع $\alpha > 1$. تذكر أنه لأي مدخلين متجاورين $D$ و$D'$، ومعرفة سابقة تعسفية $p$، فإن دالة الاحتمالات $R(D, D') \sim p(D)/p(D')$ تحقق $\mathbb{E}\left[\left(\frac{R_{\text{post}}(D,D')}{R_{\text{prior}}(D,D')}\right)^{\alpha-1}\right] \leq \exp((\alpha - 1)\varepsilon)$. بواسطة متباينة ماركوف $\Pr[R_{\text{post}}(D, D') > \beta R_{\text{prior}}(D, D')] < e^{\varepsilon}/\beta^{1/(\alpha-1)}$. على سبيل المثال، إذا كان $\alpha = 2$، فإن احتمالية زيادة النسبة بين معرفتين لاحقتين بأكثر من عامل β تنخفض كـ $O(1/\beta)$.

## ضمانات تعتمد على خط الأساس

يصبح حد الخصوصية التفاضلية لريني أضعف للنتائج الأقل احتمالاً. على سبيل المثال، إذا كانت $f$ آلية (10.0, .1)-RDP، فإن حدثًا باحتمالية 0.5 تحت $f(D)$ يمكن أن يكون كبيرًا كـ 0.586 وصغيرًا كـ 0.419 تحت $f(D')$. بالنسبة للأحداث الأصغر، يكون النطاق (من الناحية النسبية) أوسع. إذا كانت الاحتمالية تحت $f(D)$ هي 0.001، فإن $\Pr[f(D') \in S] \in [.00042, 0.00218]$. لـ $\Pr[f(D) \in S] = 10^{-6}$ النطاق أوسع أيضًا: $\Pr[f(D') \in S] \in [.195 \cdot 10^{-6}, 4.36 \cdot 10^{-6}]$.

بالمقارنة مع الخصوصية التفاضلية النقية ε، فإن هذا النوع من الضمان أضعف من الناحية المفاهيمية وأكثر عبئًا في التطبيق: من أجل تحديد ما إذا كانت المخاطر المتزايدة مقبولة، يُطلب من المرء تقدير مخاطر خط الأساس أولاً.

ومع ذلك، بالمقارنة مع (ε, δ)-DP، فإن التحليل عبر الخصوصية التفاضلية لريني أبسط، وخاصة للاحتماليات الأصغر من δ، يؤدي إلى حدود أقوى. السبب هو أن الخصوصية التفاضلية (ε, δ) غالبًا ما تنشأ كنتيجة لبعض التحليل الذي يأتي ضمنيًا مع مقايضة ε-δ. قد لا يكون إيجاد قيمة مثلى لـ (ε, δ) معطاة مخاطر خط الأساس تافهًا، خاصة في الشكل المغلق. قارن البيانين التاليين، المتكافئين بشكل أساسي، لنظريات التركيب المتقدمة (المقترح 4 والنتيجة 1):

لتكن $f : \mathcal{D} \mapsto \mathcal{R}$ تركيبًا تكيفيًا لـ $n$ آليات جميعها تحقق خصوصية تفاضلية ε لـ $\varepsilon \leq 1$. لتكن $D$ و$D'$ مدخلين متجاورين. ثم لأي $S \subset \mathcal{R}$، بواسطة المقترح 4:

$$\Pr[f(D') \in S] \leq \exp\left(\sqrt{2\varepsilon n \log 1/\Pr[f(D) \in S]}\right) \cdot \Pr[f(D) \in S].$$

أو، بواسطة النتيجة 1،

$$\Pr[f(D') \in S] \leq \exp\left(4\varepsilon\sqrt{2n \log 1/\delta}\right) \cdot \Pr[f(D) \in S] + \delta,$$

حيث $0 < \varepsilon, \delta < 1$ بحيث $\log(1/\delta) \geq \varepsilon^2 n$.

معطاة بعض قيمة مخاطر خط الأساس $\Pr[f(D) \in S]$، أي صيغة أسهل في التفسير؟ نجادل بأنها الأولى، حيث أن شكل (ε, δ) له معامل حر (δ) يجب تحسينه من أجل استخراج حد محكم يعطيه المقترح 4 مباشرة.

يصبح استخدام حدود (ε, δ) أكثر تعقيدًا إذا اعتبرنا تركيبًا لآليات غير متجانسة. هذا يقودنا إلى نقطة المقارنة الأخيرة بين مقاييس الخصوصية التفاضلية (ε, δ) ولريني.

## متابعة خسارة الخصوصية المتراكمة

ميزانية خصوصية محدودة مرتبطة بفرد هي مفهوم بديهي وجذاب، تعطيه الخصوصية التفاضلية ε تعبيرًا رياضيًا صارمًا. يمكن تتبع الخسارة التراكمية للخصوصية التفاضلية على مدار تشغيل آلية، أو بروتوكول، أو حياة المرء بسهولة بفضل خاصية الجمعية للخصوصية التفاضلية. للأسف، فإن القيام بذلك بسذاجة من المحتمل أن يبالغ في تقدير خسارة الخصوصية، والتي تنمو بشكل دون خطي في عدد الاستعلامات مع احتمالية ليست ضئيلة (عبر نظريات التركيب المتقدمة).

الأهم من ذلك، أن تطبيق نظريات التركيب المتقدمة يكسر التجريد المريح للخصوصية كعدد حقيقي غير سالب. بدلاً من ذلك، يأتي الضمان في شكل (ε, δ) الذي يتوافق فعليًا مع نقطة واحدة على منحنى معرف ضمنيًا. يجعل تركيب آليات متعددة غير متجانسة تطبيق قاعدة التركيب بشكل أمثل أكثر صعوبة، حيث قد يختار المرء نقاط (ε, δ) مختلفة لتمثيل خصوصيتهم (في التحليل، وليس أثناء وقت تشغيل الآليات!). هذا يطرح سؤالاً حول كيفية تمثيل ضمان الخصوصية لآلية معقدة: تقطيره إلى رقم واحد يتخلص من معلومات قيمة، بينما نشر منحنى (ε, δ) الكامل ينقل المشكلة إلى خطوة التجميع. (راجع Kairouz وآخرين [7] للحصول على حد أمثل على تركيب الآليات المتجانسة وMurtagh وVadhan [8] لنتائج الصعوبة ومخطط تقريب لتركيب الآليات مع ضمانات خصوصية غير متجانسة.)

تستعيد الخصوصية التفاضلية لريني مفهوم ميزانية الخصوصية، بفضل قاعدة التركيب الخاصة بها: منحنيات RDP للآليات المركبة تتجمع ببساطة. والأهم من ذلك، أن α's من الخصوصية التفاضلية (α, ε)-لريني لا تتغير. إذا تم الإبلاغ عن بيانات RDP لمجموعة مشتركة من α's (والتي تتضمن +∞، لتتبع الخصوصية التفاضلية النقية)، فإن RDP للكلية هي مجموع المتجهات المُبلغ عنها. بما أن نظرية التركيب للمقترح 4 تأخذ كمدخل منحنى RDP للآلية، فهذا يعني أن الخسارة دون الخطية للخصوصية كدالة لعدد الاستعلامات ستظل تصمد.

كمثال على هذا النهج، نجدول الحد على خسارة الخصوصية لآلية تكرارية تتكون من ثلاث آليات أساسية: الاستجابة العشوائية، وغاوس، ولابلاس. يتم إعطاء منحنى RDP الخاص بها، في الشكل المغلق، من خلال تطبيق قاعدة التركيب الأساسية على منحنيات RDP للآليات الأساسية (الجدول الثاني). يتم عرض ضمان الخصوصية في الشكل 3 لثلاث قيم لمخاطر خط الأساس: 0.1، و0.001، و$10^{-6}$. لكل مجموعة من المعاملات يتم رسم منحنيين: واحد لقيمة α مثلى من $(1, +\infty]$، والآخر لـ α مثلى مقيد بمجموعة 13 قيمة $\{1.5, 1.75, 2, 2.5, 3, 4, 5, 6, 8, 16, 32, 64, +\infty\}$. المنحنيان متطابقان تقريبًا، مما يوضح أطروحتنا بأن الإبلاغ عن منحنيات RDP لمجموعة مقيدة من α's يحافظ على إحكام تحليل الخصوصية.

---

### Translation Notes

- **Key terms introduced:**
  - baseline risk (مخاطر خط الأساس)
  - accumulated privacy loss (خسارة الخصوصية المتراكمة)
  - heterogeneous mechanisms (آليات غير متجانسة)
  - homogeneous mechanisms (آليات متجانسة)

- **Figures referenced:** Figure 3 (الشكل 3), Table II (الجدول الثاني)
- **Equations:** Mathematical expressions for bounds and guarantees
- **Citations:** [7], [8]
- **Special handling:** Discussion of conceptual tradeoffs between different privacy notions

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
