# Section 3: Lower Bounds for Accuracy with Differential Privacy
## القسم 3: الحدود الدنيا للدقة مع الخصوصية التفاضلية

**Section:** lower-bounds
**Translation Quality:** 0.86
**Glossary Terms Used:** differential privacy, histogram, accuracy, risk, minimax, loss function, algorithm

---

### English Version

To motivate the need for relaxed versions of differential privacy, we consider here the accuracy of differentially private histograms. We evaluate a differentially private procedure in terms of its "risk" which is a natural measure of accuracy taken from statistics. We consider the $\ell_1$ loss function, and the associated risk:

$$R(\theta, Q_n) = \int_{\Theta} ||\hat{\theta} - \theta||_1 dQ_n(\hat{\theta}|\theta).$$

where $\hat{\theta}$ is the output of the differentially private algorithm, $\theta$ is the input histogram, and the distribution $Q_n$ is the one induced by the randomized algorithm. Typically this risk will be a non-constant function of the parameter $\theta$ and of the distribution $Q_n$. Therefore we consider the "minimax risk" which is the smallest achievable worst-case risk, and gives a measure of the hardness of the problem which does not depend on a particular choice of procedure:

$$R^* = \inf_{Q_n} \sup_{\theta \in \Theta} R(\theta, Q_n)$$

We next describe the minimax risk of the best fully differentially private mechanism $Q_n$.

**Proposition 3.1.**
$$R^* \geq c_0 \frac{k-1}{\alpha n}$$

*Proof.* The proof uses a standard method for deriving minimax lower bounds in statistical estimation. Consider the $k-1$-dimensional hypercube

$$\left\{ \left( \frac{\sigma_1\tau}{n}, \ldots, \frac{\sigma_{k-1}\tau}{n}, \frac{(n - \sum_{i=1}^{k-1}\sigma_i)\tau}{n} \right) : \sigma_i \in \{0,1\} \right\}.$$

Take $\theta, \theta'$, to be neighboring corners of this hypercube (namely two elements which differ in exactly one coordinate $\sigma_i$). Take the KL divergence between the conditional distributions at these corners to be:

$$KL(Q_n(\cdot|\theta) || Q_n(\cdot|\theta')) = \int_{\Theta} \log \frac{Q_n(\hat{\theta}|\theta)}{Q_n(\hat{\theta}|\theta')} dQ_n(\hat{\theta}|\theta)$$

By considering a sequence of points corresponding to neighboring inputs, we find the ratio of densities to have the upper bound: $\frac{Q_n(\hat{\theta}|\theta)}{Q_n(\hat{\theta}|\theta')} \leq e^{\alpha\tau}$ since $\tau$ elements of the input have to change to move from $\theta$ to $\theta'$, and the ratio at each step is bounded by $e^{\alpha}$. Therefore the KL divergence obeys $KL(Q_n(\cdot|\theta) || Q_n(\cdot|\theta')) \leq \alpha\tau$. The "affinity" between the two distributions is:

$$||Q_n(\cdot|\theta) \wedge Q_n(\cdot|\theta')|| = \int_{\Theta} \min\{Q_n(\hat{\theta}|\theta), Q_n(\hat{\theta}|\theta')\} d\hat{\theta}.$$

The Kullback-Csiszar-Kemperman inequality [17] yields a lower bound on the affinity between these distributions:

$$||Q_n(\cdot|\theta) \wedge Q_n(\cdot|\theta')|| \geq 1 - \sqrt{\frac{\alpha\tau}{2}}.$$

Assouad's lemma (see [17] again) thus gives the lower bound:

$$R^* \geq (k-1)\frac{\tau}{2n}\left( 1 - \sqrt{\frac{\alpha\tau}{2}} \right).$$

Taking $\tau = t/\alpha$ gives

$$R^* \geq (k-1)\frac{t}{2\alpha n}\left( 1 - \sqrt{\frac{t}{2}} \right).$$

For $\alpha < 1$ we may take $t < 1$, which results in the parenthetical expression being positive. □

**Remark 1.** The previous result demonstrates that the minimax risk of the differentially private histogram is of the order $O\left(\frac{k}{\alpha n}\right)$.

**Remark 2.** Hardt and Talwar [10] have a similar result although their setting is somewhat different. In particular, they do not restrict to the space of histograms based on $n$ observations.

The above results demonstrates that for every differentially private scheme, there is at least one input for which the risk is growing in the order shown (in fact, at least one point in every hypercube of side length $\tau/n$). However the prospect exists that at many other inputs the risk is much lower. We now demonstrate that this is not the case when $k = 2$, by presenting a uniform lower bound for the risk among all minimax schemes. In the case of $k = 2$ the output may be regarded as a single number $\frac{a}{n}$ where $a \in \{0, \ldots, n\}$, which gives the proportion of the data points in the first bin. Our result will show that in a sense, the minimax differential privacy schemes are similar to "equalizer rules" in the sense that the risk is on the same order for every input.

**Proposition 3.2.** For $k = 2$ for any $Q_n$ which achieves $\sup_{\theta} R(\theta, Q_n) \leq \frac{c_0}{\alpha n}$ we have that $\inf_{\theta} R(\theta, Q_n) \geq \frac{c_1}{\alpha n}$

*Proof.* Note that for any $\theta_1$ and $c > c_0$, due to the uniform upper bound on the risk, Markov's inequality gives

$$\int_{\mathcal{Z}} \mathbf{1}\{|\hat{\theta} - \theta_1| \leq \frac{c}{\alpha n}\} dQ_n(\hat{\theta}|\theta_1) \geq 1 - \frac{c_0}{c}.$$

Therefore, due to the constraint of differential privacy, we have that, for any $\theta_0$,

$$\int_{\mathcal{Z}} \mathbf{1}\{|\hat{\theta} - \theta_1| \leq \frac{c}{\alpha n}\} dQ_n(\hat{\theta}|\theta_0) \geq \left(1 - \frac{c_0}{c}\right) \exp\left\{-\frac{\alpha n}{2}||\theta_0 - \theta_1||_1\right\}$$

Since $\frac{n}{2}||\theta_0 - \theta_1||$ elements of the input change to move from $\theta_0$ to $\theta_1$. Therefore taking $\theta_1$ to give $||\theta_0 - \theta_1|| = \frac{2c}{\alpha n}$ gives

$$R(\theta_0, Q_n) \geq \frac{c}{\alpha n}\left(1 - \frac{c_0}{c}\right)e^{-c} = \frac{c_1}{\alpha n}.$$

As $\theta_0$ is arbitrary, this gives a uniform lower bound under the conditions above. □

For the relaxation of differential privacy given in definition 2.2 of [10], the above result remains intact for large enough $n$. The relaxation is:

$$Q_n(z|X) \leq Q_n(z|X')e^{\alpha} + \eta(n)$$

where $\eta(n)$ is negligible (i.e., tending to zero faster than any inverse polynomial in $n$). Thus via the same technique as above, we have

$$R(\theta_0, \delta, Q_n) \geq \frac{c}{\alpha n}\left[(1 - \frac{c_0}{c})e^{-c} - c_2\eta(n)\right] = \frac{c_1 - \eta(n)}{\alpha n}.$$

For large enough $n$ this latter term is bounded from below by $\frac{c_3}{\alpha n}$. This indicates that the above relaxation of differential privacy will not be useful in achieving higher accuracy.

For $k > 2$, we may write

$$R(\theta, Q_n) = \sum_{i=1}^k R_i(\theta, Q_n)$$

With

$$R_i(\theta, Q_n) \stackrel{\text{def}}{=} \int_{\mathcal{Z}} |\hat{\theta} - \theta_i|dQ_n(\hat{\theta}|\theta),$$

where the subscript means the $i$th coordinate. Thus, whenever we have that $R_i \leq \frac{c_0}{\alpha n}$ uniformly over $i$, we have that $R(\theta, \delta, Q_n) \geq \frac{c_1(k-1)}{\alpha n}$. Therefore the only opportunity to improve upon the rate of $\frac{k}{\alpha n}$ is when some $\theta$ have some coordinate $i$ at which the risk upper bound does not apply.

We conclude by remarking that we have demonstrated, that for a certain class of differentially private algorithms which achieve the "minimax rate," their risk is uniformly lower bounded at the same rate. The rate in question is linear in $k$, which is problematic when $k$ is large relative to $n$. It remains an open question whether there are different techniques which achieve the minimax rate, yet do not have this property. Such a technique would have to lose the uniform upper bound on the coordinate-wise risk. Below, we present a weakening of differential privacy, which admits release mechanisms, which both keep the uniform upper bound on the coordinate-wise risk, and also have a minimax risk which is growing only in the support of the histogram (namely, the number of cells which contain observations).

---

### النسخة العربية

لتحفيز الحاجة إلى نسخ مرنة من الخصوصية التفاضلية، نأخذ في الاعتبار هنا دقة الرسوم البيانية الهيستوغرامية الخاصة تفاضلياً. نقيّم إجراءً خاصاً تفاضلياً من حيث "مخاطره" وهي مقياس طبيعي للدقة مأخوذ من الإحصاء. نأخذ في الاعتبار دالة الخسارة $\ell_1$، والمخاطر المرتبطة:

$$R(\theta, Q_n) = \int_{\Theta} ||\hat{\theta} - \theta||_1 dQ_n(\hat{\theta}|\theta).$$

حيث $\hat{\theta}$ هو مخرج الخوارزمية الخاصة تفاضلياً، و $\theta$ هو الرسم البياني الهيستوغرامي المدخل، والتوزيع $Q_n$ هو الذي تحدثه الخوارزمية العشوائية. عادة ما تكون هذه المخاطر دالة غير ثابتة للمعامل $\theta$ وللتوزيع $Q_n$. لذلك نأخذ في الاعتبار "مخاطر المينيماكس" وهي أصغر مخاطر قابلة للتحقيق في أسوأ الحالات، وتعطي مقياساً لصعوبة المشكلة لا يعتمد على اختيار معين للإجراء:

$$R^* = \inf_{Q_n} \sup_{\theta \in \Theta} R(\theta, Q_n)$$

نصف بعد ذلك مخاطر المينيماكس لأفضل آلية خاصة تفاضلياً بالكامل $Q_n$.

**القضية 3.1.**
$$R^* \geq c_0 \frac{k-1}{\alpha n}$$

*البرهان.* يستخدم البرهان طريقة قياسية لاشتقاق حدود دنيا للمينيماكس في التقدير الإحصائي. لنأخذ في الاعتبار المكعب الفائق من البعد $k-1$

$$\left\{ \left( \frac{\sigma_1\tau}{n}, \ldots, \frac{\sigma_{k-1}\tau}{n}, \frac{(n - \sum_{i=1}^{k-1}\sigma_i)\tau}{n} \right) : \sigma_i \in \{0,1\} \right\}.$$

نأخذ $\theta, \theta'$، لتكونا ركنين متجاورين من هذا المكعب الفائق (أي عنصرين يختلفان في إحداثية واحدة بالضبط $\sigma_i$). نأخذ تباعد KL بين التوزيعات الشرطية عند هذين الركنين ليكون:

$$KL(Q_n(\cdot|\theta) || Q_n(\cdot|\theta')) = \int_{\Theta} \log \frac{Q_n(\hat{\theta}|\theta)}{Q_n(\hat{\theta}|\theta')} dQ_n(\hat{\theta}|\theta)$$

بالنظر إلى سلسلة من النقاط المقابلة للمدخلات المتجاورة، نجد أن نسبة الكثافات لها الحد الأعلى: $\frac{Q_n(\hat{\theta}|\theta)}{Q_n(\hat{\theta}|\theta')} \leq e^{\alpha\tau}$ لأن $\tau$ عنصراً من المدخل يجب أن تتغير للانتقال من $\theta$ إلى $\theta'$، والنسبة عند كل خطوة محدودة بـ $e^{\alpha}$. لذلك يخضع تباعد KL لـ $KL(Q_n(\cdot|\theta) || Q_n(\cdot|\theta')) \leq \alpha\tau$. "التقارب" بين التوزيعين هو:

$$||Q_n(\cdot|\theta) \wedge Q_n(\cdot|\theta')|| = \int_{\Theta} \min\{Q_n(\hat{\theta}|\theta), Q_n(\hat{\theta}|\theta')\} d\hat{\theta}.$$

تعطي متباينة كولباك-شيزار-كمبرمان [17] حداً أدنى على التقارب بين هذين التوزيعين:

$$||Q_n(\cdot|\theta) \wedge Q_n(\cdot|\theta')|| \geq 1 - \sqrt{\frac{\alpha\tau}{2}}.$$

وبالتالي تعطي مبرهنة أسواد (انظر [17] مرة أخرى) الحد الأدنى:

$$R^* \geq (k-1)\frac{\tau}{2n}\left( 1 - \sqrt{\frac{\alpha\tau}{2}} \right).$$

بأخذ $\tau = t/\alpha$ نحصل على

$$R^* \geq (k-1)\frac{t}{2\alpha n}\left( 1 - \sqrt{\frac{t}{2}} \right).$$

لـ $\alpha < 1$ يمكننا أخذ $t < 1$، مما ينتج عنه تعبير بين قوسين موجب. □

**ملاحظة 1.** توضح النتيجة السابقة أن مخاطر المينيماكس للرسم البياني الهيستوغرامي الخاص تفاضلياً من رتبة $O\left(\frac{k}{\alpha n}\right)$.

**ملاحظة 2.** لدى هاردت وتالوار [10] نتيجة مماثلة على الرغم من أن إعدادهم مختلف إلى حد ما. على وجه الخصوص، لا يقتصرون على فضاء الرسوم البيانية الهيستوغرامية بناءً على $n$ ملاحظة.

توضح النتائج أعلاه أنه لكل مخطط خاص تفاضلياً، هناك مدخل واحد على الأقل تنمو فيه المخاطر بالترتيب الموضح (في الواقع، نقطة واحدة على الأقل في كل مكعب فائق بطول ضلع $\tau/n$). ومع ذلك، هناك احتمال أن تكون المخاطر عند العديد من المدخلات الأخرى أقل بكثير. نوضح الآن أن هذا ليس هو الحال عندما $k = 2$، من خلال تقديم حد أدنى موحد للمخاطر بين جميع مخططات المينيماكس. في حالة $k = 2$ يمكن اعتبار المخرج رقماً واحداً $\frac{a}{n}$ حيث $a \in \{0, \ldots, n\}$، والذي يعطي نسبة نقاط البيانات في الحاوية الأولى. ستُظهر نتيجتنا أنه بمعنى ما، مخططات الخصوصية التفاضلية للمينيماكس مشابهة لـ "قواعد المعادل" بمعنى أن المخاطر من نفس الرتبة لكل مدخل.

**القضية 3.2.** لـ $k = 2$ لأي $Q_n$ تحقق $\sup_{\theta} R(\theta, Q_n) \leq \frac{c_0}{\alpha n}$ لدينا $\inf_{\theta} R(\theta, Q_n) \geq \frac{c_1}{\alpha n}$

*البرهان.* لاحظ أنه لأي $\theta_1$ و $c > c_0$، بسبب الحد الأعلى الموحد على المخاطر، تعطي متباينة ماركوف

$$\int_{\mathcal{Z}} \mathbf{1}\{|\hat{\theta} - \theta_1| \leq \frac{c}{\alpha n}\} dQ_n(\hat{\theta}|\theta_1) \geq 1 - \frac{c_0}{c}.$$

لذلك، بسبب قيد الخصوصية التفاضلية، لدينا، لأي $\theta_0$،

$$\int_{\mathcal{Z}} \mathbf{1}\{|\hat{\theta} - \theta_1| \leq \frac{c}{\alpha n}\} dQ_n(\hat{\theta}|\theta_0) \geq \left(1 - \frac{c_0}{c}\right) \exp\left\{-\frac{\alpha n}{2}||\theta_0 - \theta_1||_1\right\}$$

بما أن $\frac{n}{2}||\theta_0 - \theta_1||$ عنصراً من المدخل تتغير للانتقال من $\theta_0$ إلى $\theta_1$. لذلك بأخذ $\theta_1$ بحيث $||\theta_0 - \theta_1|| = \frac{2c}{\alpha n}$ نحصل على

$$R(\theta_0, Q_n) \geq \frac{c}{\alpha n}\left(1 - \frac{c_0}{c}\right)e^{-c} = \frac{c_1}{\alpha n}.$$

بما أن $\theta_0$ تعسفي، يعطي هذا حداً أدنى موحداً في ظل الشروط أعلاه. □

بالنسبة للإرخاء للخصوصية التفاضلية الوارد في التعريف 2.2 من [10]، تبقى النتيجة أعلاه سليمة لـ $n$ كبيرة بما فيه الكفاية. الإرخاء هو:

$$Q_n(z|X) \leq Q_n(z|X')e^{\alpha} + \eta(n)$$

حيث $\eta(n)$ ضئيلة (أي تتجه إلى الصفر أسرع من أي كثيرة حدود معكوسة في $n$). وبالتالي عبر نفس التقنية كما أعلاه، لدينا

$$R(\theta_0, \delta, Q_n) \geq \frac{c}{\alpha n}\left[(1 - \frac{c_0}{c})e^{-c} - c_2\eta(n)\right] = \frac{c_1 - \eta(n)}{\alpha n}.$$

لـ $n$ كبيرة بما فيه الكفاية، هذا الحد الأخير محدود من الأسفل بـ $\frac{c_3}{\alpha n}$. هذا يشير إلى أن الإرخاء أعلاه للخصوصية التفاضلية لن يكون مفيداً في تحقيق دقة أعلى.

لـ $k > 2$، يمكننا أن نكتب

$$R(\theta, Q_n) = \sum_{i=1}^k R_i(\theta, Q_n)$$

مع

$$R_i(\theta, Q_n) \stackrel{\text{def}}{=} \int_{\mathcal{Z}} |\hat{\theta} - \theta_i|dQ_n(\hat{\theta}|\theta),$$

حيث المؤشر السفلي يعني الإحداثية الـ $i$. وبالتالي، كلما كان لدينا $R_i \leq \frac{c_0}{\alpha n}$ بشكل موحد على $i$، لدينا $R(\theta, \delta, Q_n) \geq \frac{c_1(k-1)}{\alpha n}$. لذلك فإن الفرصة الوحيدة للتحسين على معدل $\frac{k}{\alpha n}$ هي عندما يكون لبعض $\theta$ إحداثية $i$ لا ينطبق عندها الحد الأعلى للمخاطر.

نختتم بملاحظة أننا أظهرنا، أنه لفئة معينة من الخوارزميات الخاصة تفاضلياً والتي تحقق "معدل المينيماكس"، فإن مخاطرها محدودة من الأسفل بشكل موحد بنفس المعدل. المعدل المعني خطي في $k$، وهو أمر إشكالي عندما يكون $k$ كبيراً بالنسبة إلى $n$. يبقى سؤالاً مفتوحاً ما إذا كانت هناك تقنيات مختلفة تحقق معدل المينيماكس، ومع ذلك لا تمتلك هذه الخاصية. مثل هذه التقنية يجب أن تفقد الحد الأعلى الموحد على مخاطر الإحداثيات. أدناه، نقدم إضعافاً للخصوصية التفاضلية، يسمح بآليات إصدار، تحافظ على الحد الأعلى الموحد على مخاطر الإحداثيات، ولديها أيضاً مخاطر مينيماكس تنمو فقط في دعم الرسم البياني الهيستوغرامي (أي عدد الخلايا التي تحتوي على ملاحظات).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** minimax risk, loss function, KL divergence, affinity, Assouad's lemma, Markov's inequality, equalizer rules
- **Equations:** 13 major equations with mathematical proofs
- **Citations:** [10], [17]
- **Special handling:** Mathematical proofs with complex notation; statistical terminology

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.86
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.86
