# Section 6: RDP via Sensitivity Analysis
## القسم 6: RDP عبر تحليل الحساسية

**Section:** sensitivity-analysis
**Translation Quality:** 0.86
**Glossary Terms Used:** sensitivity, random differential privacy, Laplace distribution, quantile, empirical CDF, DKW inequality

---

### English Version

We next demonstrate that RDP allows schemes for release of other kinds of statistics (besides histograms). A common technique used to establish a differentially private technique is to use Laplace noise with variance proportional to the "global sensitivity" of the function [6]. We show that there is an analog of this technique for RDP. We next demonstrate a method for the RDP release of an arbitrary function $g_n(x_1, \ldots, x_n) \in \mathbb{R}$.

We consider the algorithm which samples the distribution

$$Q_n(z|x_1, \ldots, x_n) \propto \exp\left\{ \frac{-\alpha |z - g_n(x_1, \ldots, x_n)|}{s_n(x_1, \ldots, x_n)} \right\}$$

It is well known that when $s_n$ is the constant function which gives an upper bound of the global sensitivity [6] of $g_n$, this method enjoys the $\alpha$-DP. As we allow $s_n$ to depend on the data we may make use of the local sensitivity framework of [14]. There it is demonstrated that whenever:

$$\forall X \sim X' \quad s_n(X) \leq e^{\beta}s_n(X')$$

and

$$\forall X \quad \sup_{X' \sim X} |g_n(X) - g_n(X')| \leq s_n(X)$$

then (6) gives $(2\alpha, \eta)$-DP with:

$$\eta = e^{-\frac{\alpha}{2\beta}}$$

(see [14] definition 2.1, lemma 2.5 and example 3). In moving from DP to RDP we may now require that conditions (7) and (8) hold only with the requisite probability $1 - \gamma$. Then (6) will achieve $(2\alpha, \eta, \gamma)$-RDP.

We consider a special subset of functions for which:

$$\sup_{X \sim X'} |g_n(X) - g_n(X')| = n^{-1}\sup_{x,x'} h(x, x').$$

Examples of functions satisfying this property are e.g., statistical point estimators [15] and regularized logistic regression estimates [4]. In particular in these cases it is assumed that $\mathcal{X}$ is some compact subset of $\mathbb{R}^d$ and then e.g., $\sup_{x,x'} h(x, x') = ||x - x'||_2$ gives the diameter of this set.

We replace conditions (7) and (8) with:

$$\mathbb{P}(s_n(X) \leq e^{\beta}s_n(X')) \geq 1 - \gamma_1$$

and

$$\mathbb{P}(n^{-1}h(x, x') \leq \min\{s_n(X), s_n(X')\}) \geq 1 - \gamma_2.$$

Note that $x, x'$ are random draws from $P$ which are independent of the random vectors $X, X'$. The first condition simply requires (7), to hold except on a set of measure $\gamma_1$. The second condition implies that both $s_n(X)$ and $s_n(X')$ give upper bounds to the local sensitivity, except on a set of measure $\gamma_2$. Putting these together along with the above considerations will yield a $(2\alpha, \eta, \gamma_1 + \gamma_2)$-RDP method. We note that we are essentially asking that $s_n(X)$ and $s_n(X')$ both give valid quantiles for the random variable $h(x, x')$, and that they give similar values with high probability.

We consider the empirical process based on $h$ and the data sample $X$ given by:

$$D(X, t) = \frac{2}{n}\sum_{i=1}^{n/2} \mathbf{1}\{h(x_i, x_{i+n/2}) \leq t\}$$

This is exactly an empirical CDF for the distribution of $h(x, x')$, based on $n/2$ independent samples of $h(x, x')$. We may anticipate that sample quantiles of this empirical CDF will be close to the quantiles from the true CDF, which we denote by $H(t) = \mathbb{P}(h \leq t)$. This is made precise by the DKW inequality (see e.g., [13]), which in this case yields:

$$\mathbb{P}\left(\sup_t |H(t) - D(X, t)| \geq \epsilon\right) \leq 2e^{-n\epsilon^2}.$$

Thus taking $d_{\delta}(X)$ to be the smallest $d$ with $D(X, d) = 1 - \delta$, and $h_{\delta'}$ to give the $1 - \delta'$ quantile of $h$, with $\delta < \delta'$, we have:

$$\mathbb{P}(h(x, x') > d_{\delta}) \leq \delta' + \mathbb{P}(d_{\delta}(X) < h_{\delta'})$$
$$\leq \delta' + 2e^{-(\delta' - \delta)^2 n}.$$

The second inequality comes from applying the monotone function $D(X, \cdot)$ to both sides of the inequality statement in the probability, and then rearranging, to yield $\mathbb{P}(D(X, h_{\delta'}) - H(h_{\delta'}) > (\delta' - \delta))$ which is bounded due to the DKW inequality (12). Thus for some appropriate choice of $\delta, \delta'$ we may take $s_n(X) = n^{-1}d_{\delta}(X)$, and thus achieve (11).

Now to achieve (10) we turn to the Bahadur-Kiefer representation of sample quantiles (see [11]). We have that:

$$d_{\delta}(X) - h_{\delta} = \frac{D(X, h_{\delta}) - H(h_{\delta})}{H'(h_{\delta})} + O_p(n^{-3/4})$$

where $H'$ is the derivative of $H$ (namely the density). Hence we concentrate on the case when $h$ is a continuous random variable. We find the ratio to be bounded in probability:

$$\frac{d_{\delta}(X)}{d_{\delta}(X')} \leq 1 + \frac{|d_{\delta}(X) - d_{\delta}(X')|}{d_{\delta}(X')} = 1 + \frac{O_p(n^{-1/2})}{h_{\delta} + O_p(n^{-1/2})}$$

where the final equality stems from using DKW to bound the $D(X, h_{\delta}) - H(h_{\delta})$ and along with the triangle inequality to bound $|D(X, h_{\delta}) - D(X', h_{\delta})|$. This therefore demonstrates that:

$$\frac{d_{\delta}(X)}{d_{\delta}(X')} \leq 1 + O_p(n^{-1/2}) = O_p(e^{n^{-1/2}})$$

This means that for large enough $n$, and some probability $1-\gamma_2$, the ratio is bounded by $e^{\beta}$ where $\beta$ is polynomial in $n^{-1/2}$. Examining (9) we find $\eta$ to be negligible for such a choice of $\beta$. Therefore the use of $s_n(X) = n^{-1}d_{\delta}$ achieves the RDP as required.

We note that in principle this same approach would work, were we to replace $D(X, t)$ with the U-statistic process:

$$U(X, t) = \frac{1}{\binom{n}{2}}\sum_{i>j} \mathbf{1}\{h(x_i, x_j) \leq t\}.$$

Though this is essentially another empirical CDF, it is based on non-independent samples since each $x_i$ participates in $n - 1$ of the evaluations of $h$. Nevertheless an analog of the DKW inequality still applies to this process, and we still have the same behavior of the quantiles (see e.g., [1]).

---

### النسخة العربية

نوضح بعد ذلك أن RDP يسمح بمخططات لإصدار أنواع أخرى من الإحصاءات (بالإضافة إلى الرسوم البيانية الهيستوغرامية). التقنية الشائعة المستخدمة لإنشاء تقنية خاصة تفاضلياً هي استخدام ضوضاء لابلاس بتباين يتناسب مع "الحساسية العامة" للدالة [6]. نُظهر أن هناك نظيراً لهذه التقنية لـ RDP. نوضح بعد ذلك طريقة لإصدار RDP لدالة تعسفية $g_n(x_1, \ldots, x_n) \in \mathbb{R}$.

نأخذ في الاعتبار الخوارزمية التي تعاين التوزيع

$$Q_n(z|x_1, \ldots, x_n) \propto \exp\left\{ \frac{-\alpha |z - g_n(x_1, \ldots, x_n)|}{s_n(x_1, \ldots, x_n)} \right\}$$

من المعروف أنه عندما تكون $s_n$ دالة ثابتة تعطي حداً أعلى للحساسية العامة [6] لـ $g_n$، فإن هذه الطريقة تتمتع بـ $\alpha$-DP. بما أننا نسمح لـ $s_n$ بالاعتماد على البيانات، يمكننا الاستفادة من إطار الحساسية المحلية لـ [14]. هناك يتم إثبات أنه كلما:

$$\forall X \sim X' \quad s_n(X) \leq e^{\beta}s_n(X')$$

و

$$\forall X \quad \sup_{X' \sim X} |g_n(X) - g_n(X')| \leq s_n(X)$$

عندئذ (6) يعطي $(2\alpha, \eta)$-DP مع:

$$\eta = e^{-\frac{\alpha}{2\beta}}$$

(انظر [14] التعريف 2.1، المبرهنة 2.5 والمثال 3). في الانتقال من DP إلى RDP يمكننا الآن أن نطلب أن الشرطين (7) و (8) يحملان فقط بالاحتمال المطلوب $1 - \gamma$. عندئذ (6) سيحقق $(2\alpha, \eta, \gamma)$-RDP.

نأخذ في الاعتبار مجموعة فرعية خاصة من الدوال التي:

$$\sup_{X \sim X'} |g_n(X) - g_n(X')| = n^{-1}\sup_{x,x'} h(x, x').$$

أمثلة على الدوال التي تحقق هذه الخاصية هي على سبيل المثال، المقدرات النقطية الإحصائية [15] وتقديرات الانحدار اللوجستي المنظم [4]. على وجه الخصوص، في هذه الحالات يُفترض أن $\mathcal{X}$ هي مجموعة فرعية مدمجة من $\mathbb{R}^d$ وبعد ذلك على سبيل المثال، $\sup_{x,x'} h(x, x') = ||x - x'||_2$ يعطي قطر هذه المجموعة.

نستبدل الشرطين (7) و (8) بـ:

$$\mathbb{P}(s_n(X) \leq e^{\beta}s_n(X')) \geq 1 - \gamma_1$$

و

$$\mathbb{P}(n^{-1}h(x, x') \leq \min\{s_n(X), s_n(X')\}) \geq 1 - \gamma_2.$$

لاحظ أن $x, x'$ هي سحوبات عشوائية من $P$ مستقلة عن المتجهات العشوائية $X, X'$. الشرط الأول ببساطة يتطلب (7)، أن يحمل باستثناء مجموعة بقياس $\gamma_1$. الشرط الثاني يعني أن كلاً من $s_n(X)$ و $s_n(X')$ يعطيان حدوداً عليا للحساسية المحلية، باستثناء مجموعة بقياس $\gamma_2$. وضع هذه معاً جنباً إلى جنب مع الاعتبارات أعلاه سينتج طريقة $(2\alpha, \eta, \gamma_1 + \gamma_2)$-RDP. نلاحظ أننا نطلب في الأساس أن كلاً من $s_n(X)$ و $s_n(X')$ يعطيان كميات صالحة للمتغير العشوائي $h(x, x')$، وأنهما يعطيان قيماً مماثلة باحتمال عالٍ.

نأخذ في الاعتبار العملية التجريبية المستندة إلى $h$ وعينة البيانات $X$ المعطاة بـ:

$$D(X, t) = \frac{2}{n}\sum_{i=1}^{n/2} \mathbf{1}\{h(x_i, x_{i+n/2}) \leq t\}$$

هذا بالضبط هو CDF تجريبي لتوزيع $h(x, x')$، بناءً على $n/2$ عينة مستقلة من $h(x, x')$. يمكننا توقع أن الكميات العينية لهذا CDF التجريبي ستكون قريبة من الكميات من CDF الحقيقي، والتي نرمز لها بـ $H(t) = \mathbb{P}(h \leq t)$. هذا يتم توضيحه بدقة بواسطة متباينة DKW (انظر على سبيل المثال [13])، والتي في هذه الحالة تعطي:

$$\mathbb{P}\left(\sup_t |H(t) - D(X, t)| \geq \epsilon\right) \leq 2e^{-n\epsilon^2}.$$

وبالتالي بأخذ $d_{\delta}(X)$ لتكون أصغر $d$ مع $D(X, d) = 1 - \delta$، و $h_{\delta'}$ لإعطاء الكمية $1 - \delta'$ لـ $h$، مع $\delta < \delta'$، لدينا:

$$\mathbb{P}(h(x, x') > d_{\delta}) \leq \delta' + \mathbb{P}(d_{\delta}(X) < h_{\delta'})$$
$$\leq \delta' + 2e^{-(\delta' - \delta)^2 n}.$$

تأتي المتباينة الثانية من تطبيق الدالة الرتيبة $D(X, \cdot)$ على كلا جانبي بيان المتباينة في الاحتمال، ثم إعادة الترتيب، لإعطاء $\mathbb{P}(D(X, h_{\delta'}) - H(h_{\delta'}) > (\delta' - \delta))$ والتي محدودة بسبب متباينة DKW (12). وبالتالي لبعض الاختيار المناسب لـ $\delta, \delta'$ يمكننا أخذ $s_n(X) = n^{-1}d_{\delta}(X)$، وبالتالي تحقيق (11).

الآن لتحقيق (10) نلجأ إلى تمثيل باهادور-كيفر للكميات العينية (انظر [11]). لدينا:

$$d_{\delta}(X) - h_{\delta} = \frac{D(X, h_{\delta}) - H(h_{\delta})}{H'(h_{\delta})} + O_p(n^{-3/4})$$

حيث $H'$ هو مشتقة $H$ (أي الكثافة). ومن ثم نركز على الحالة عندما يكون $h$ متغيراً عشوائياً مستمراً. نجد أن النسبة محدودة في الاحتمال:

$$\frac{d_{\delta}(X)}{d_{\delta}(X')} \leq 1 + \frac{|d_{\delta}(X) - d_{\delta}(X')|}{d_{\delta}(X')} = 1 + \frac{O_p(n^{-1/2})}{h_{\delta} + O_p(n^{-1/2})}$$

حيث تنبع المساواة النهائية من استخدام DKW لتحديد $D(X, h_{\delta}) - H(h_{\delta})$ ومع متباينة المثلث لتحديد $|D(X, h_{\delta}) - D(X', h_{\delta})|$. وبالتالي يوضح هذا أن:

$$\frac{d_{\delta}(X)}{d_{\delta}(X')} \leq 1 + O_p(n^{-1/2}) = O_p(e^{n^{-1/2}})$$

هذا يعني أنه لـ $n$ كبيرة بما فيه الكفاية، وبعض الاحتمال $1-\gamma_2$، فإن النسبة محدودة بـ $e^{\beta}$ حيث $\beta$ كثيرة حدود في $n^{-1/2}$. بفحص (9) نجد أن $\eta$ ضئيلة لمثل هذا الاختيار من $\beta$. لذلك فإن استخدام $s_n(X) = n^{-1}d_{\delta}$ يحقق RDP كما هو مطلوب.

نلاحظ أنه من حيث المبدأ سيعمل نفس النهج هذا، لو استبدلنا $D(X, t)$ بعملية إحصاء U:

$$U(X, t) = \frac{1}{\binom{n}{2}}\sum_{i>j} \mathbf{1}\{h(x_i, x_j) \leq t\}.$$

على الرغم من أن هذا في الأساس CDF تجريبي آخر، إلا أنه يستند إلى عينات غير مستقلة لأن كل $x_i$ يشارك في $n - 1$ من تقييمات $h$. ومع ذلك، لا يزال نظير متباينة DKW ينطبق على هذه العملية، ولا يزال لدينا نفس سلوك الكميات (انظر على سبيل المثال [1]).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** global sensitivity, local sensitivity, empirical CDF, DKW inequality, Bahadur-Kiefer representation, U-statistic, quantile
- **Equations:** 14 equations with statistical analysis
- **Citations:** [1], [4], [6], [11], [13], [14], [15]
- **Special handling:** Advanced statistical concepts; stochastic order notation O_p

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.86
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.86
