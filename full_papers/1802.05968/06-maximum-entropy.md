# Section 6: Maximum Entropy Distributions
## القسم 6: توزيعات الإنتروبيا القصوى

**Section:** maximum-entropy
**Translation Quality:** 0.87
**Glossary Terms Used:** entropy, Gaussian distribution, exponential distribution, uniform distribution, variance

---

### English Version

A distribution of values that has as much entropy (information) as theoretically possible is a maximum entropy distribution. Maximum entropy distributions are important because, if we wish to use a variable to transmit as much information as possible then we had better make sure it has maximum entropy. For a given variable, the precise form of its maximum entropy distribution depends on the constraints placed on the values of that variable[3]. It will prove useful to summarise three important maximum entropy distributions. These are listed in order of decreasing numbers of constraints below.

**The Gaussian Distribution.** If a variable $x$ has a fixed variance, but is otherwise unconstrained, then the maximum entropy distribution is the Gaussian distribution (Figure 5a). This is particularly important in terms of energy efficiency because no other distribution can provide as much information at a lower energy cost per bit. If a variable has a Gaussian or normal distribution then the probability of observing a particular value $x$ is

$$p(x) = \frac{1}{\sqrt{2\pi v_x}} e^{-(\mu_x - x)^2/(2v_x)},$$ (6)

where $e = 2.7183$. This equation defines the bell-shaped curve in Figure 5a. The term $\mu_x$ is the mean of the variable $x$, and defines the central value of the distribution; we assume that all variables have a mean of zero (unless stated otherwise). The term $v_x$ is the variance of the variable $x$, which is the square of the standard deviation $\sigma_x$ of $x$, and defines the width of the bell curve. Equation 6 is a probability density function, and (strictly speaking) $p(x)$ is the probability density of $x$.

**The Exponential Distribution.** If a variable has no values below zero, and has a fixed mean $\mu$, but is otherwise unconstrained, then the maximum entropy distribution is exponential,

$$p(x) = \frac{1}{\mu} e^{-x/\mu},$$ (7)

which has a variance of $\text{var}(x) = \mu^2$, as shown in Figure 5b.

**The Uniform Distribution.** If a variable has a fixed lower bound $x_{\min}$ and upper bound $x_{\max}$, but is otherwise unconstrained, then the maximum entropy distribution is uniform,

$$p(x) = 1/(x_{\max} - x_{\min}),$$ (8)

which has a variance $(x_{\max} - x_{\min})^2/12$, as shown in Figure 5c.

---

### النسخة العربية

توزيع القيم الذي يحتوي على أكبر قدر ممكن من الإنتروبيا (المعلومات) نظرياً هو توزيع الإنتروبيا القصوى. توزيعات الإنتروبيا القصوى مهمة لأننا إذا أردنا استخدام متغير لنقل أكبر قدر ممكن من المعلومات فيجب علينا التأكد من أن لديه إنتروبيا قصوى. بالنسبة لمتغير معين، يعتمد الشكل الدقيق لتوزيع الإنتروبيا القصوى الخاص به على القيود الموضوعة على قيم ذلك المتغير[3]. سيكون من المفيد تلخيص ثلاثة توزيعات إنتروبيا قصوى مهمة. هذه مدرجة بترتيب تناقص أعداد القيود أدناه.

**التوزيع الغاوسي.** إذا كان للمتغير $x$ تباين ثابت، ولكنه غير مقيد بخلاف ذلك، فإن توزيع الإنتروبيا القصوى هو التوزيع الغاوسي (الشكل 5أ). هذا مهم بشكل خاص من حيث كفاءة الطاقة لأنه لا يوجد توزيع آخر يمكنه توفير معلومات أكثر بتكلفة طاقة أقل لكل بتة. إذا كان لمتغير توزيع غاوسي أو طبيعي فإن احتمال ملاحظة قيمة معينة $x$ هو

$$p(x) = \frac{1}{\sqrt{2\pi v_x}} e^{-(\mu_x - x)^2/(2v_x)},$$ (6)

حيث $e = 2.7183$. تُحدد هذه المعادلة المنحنى على شكل جرس في الشكل 5أ. الحد $\mu_x$ هو متوسط المتغير $x$، ويحدد القيمة المركزية للتوزيع؛ نفترض أن جميع المتغيرات لها متوسط صفر (ما لم يُذكر خلاف ذلك). الحد $v_x$ هو تباين المتغير $x$، وهو مربع الانحراف المعياري $\sigma_x$ لـ $x$، ويحدد عرض منحنى الجرس. المعادلة 6 هي دالة كثافة احتمالية، و(من الناحية الفنية) $p(x)$ هي كثافة احتمال $x$.

**التوزيع الأسي.** إذا لم يكن لمتغير قيم أقل من الصفر، وله متوسط ثابت $\mu$، ولكنه غير مقيد بخلاف ذلك، فإن توزيع الإنتروبيا القصوى أسي،

$$p(x) = \frac{1}{\mu} e^{-x/\mu},$$ (7)

والذي له تباين $\text{var}(x) = \mu^2$، كما هو موضح في الشكل 5ب.

**التوزيع المنتظم.** إذا كان لمتغير حد أدنى ثابت $x_{\min}$ وحد أقصى $x_{\max}$، ولكنه غير مقيد بخلاف ذلك، فإن توزيع الإنتروبيا القصوى منتظم،

$$p(x) = 1/(x_{\max} - x_{\min}),$$ (8)

والذي له تباين $(x_{\max} - x_{\min})^2/12$، كما هو موضح في الشكل 5ج.

---

### Quality Metrics
- **Overall section score:** 0.87
