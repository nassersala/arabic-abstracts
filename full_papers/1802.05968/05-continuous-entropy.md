# Section 5: Entropy of Continuous Variables
## القسم 5: إنتروبيا المتغيرات المستمرة

**Section:** continuous-variables
**Translation Quality:** 0.86
**Glossary Terms Used:** entropy, continuous variables, discrete variables, differential entropy

---

### English Version

For discrete variables, entropy is well-defined. However, for all continuous variables, entropy is effectively infinite. Consider the difference between a discrete variable $x_d$ with $n$ possible values and a continuous variable $x_c$ with an uncountably infinite number of possible values; for simplicity, assume that all values are equally probable. The probability of observing each value of the discrete variable is $P_d = 1/m$, so the entropy of $x_d$ is $H(x_d) = \log m$. In contrast, the probability of observing each value of the continuous variable is $P_c = 1/\infty = 0$, so the entropy of $x_c$ is $H(x_c) = \log \infty = \infty$. In one respect, this makes sense, because each value of of a continuous variable is implicitly specified with infinite precision, from which it follows that the amount of information conveyed by each value is infinite. However, this result implies that all continuous variables have the same entropy. In order to assign different values to different variables, all infinite terms are simply ignored, which yields the differential entropy

$$H(x_c) = \int p(x_c) \log \frac{1}{p(x_c)} dx_c.$$ (5)

It is worth noting that the technical difficulties associated with entropy of continuous variables disappear for quantities like mutual information, which involve the difference between two entropies. For convenience, we use the term entropy for both continuous and discrete variables below.

---

### النسخة العربية

بالنسبة للمتغيرات المنفصلة، الإنتروبيا محددة جيداً. ومع ذلك، بالنسبة لجميع المتغيرات المستمرة، الإنتروبيا لا نهائية فعلياً. فكر في الفرق بين متغير منفصل $x_d$ بـ $n$ قيمة محتملة ومتغير مستمر $x_c$ بعدد لا نهائي غير قابل للعد من القيم المحتملة؛ للتبسيط، افترض أن جميع القيم محتملة بشكل متساوٍ. احتمال ملاحظة كل قيمة من المتغير المنفصل هو $P_d = 1/m$، لذلك إنتروبيا $x_d$ هي $H(x_d) = \log m$. في المقابل، احتمال ملاحظة كل قيمة من المتغير المستمر هو $P_c = 1/\infty = 0$، لذلك إنتروبيا $x_c$ هي $H(x_c) = \log \infty = \infty$. من ناحية واحدة، هذا منطقي، لأن كل قيمة من متغير مستمر محددة ضمنياً بدقة لا نهائية، ومن ذلك يتبع أن كمية المعلومات التي تنقلها كل قيمة لا نهائية. ومع ذلك، تشير هذه النتيجة إلى أن جميع المتغيرات المستمرة لها نفس الإنتروبيا. من أجل تخصيص قيم مختلفة لمتغيرات مختلفة، يتم تجاهل جميع الحدود اللانهائية ببساطة، مما ينتج الإنتروبيا التفاضلية

$$H(x_c) = \int p(x_c) \log \frac{1}{p(x_c)} dx_c.$$ (5)

من الجدير بالذكر أن الصعوبات التقنية المرتبطة بإنتروبيا المتغيرات المستمرة تختفي بالنسبة لكميات مثل المعلومات المشتركة، التي تتضمن الفرق بين إنتروبيتين. للراحة، نستخدم مصطلح الإنتروبيا لكل من المتغيرات المستمرة والمنفصلة أدناه.

---

### Quality Metrics
- **Overall section score:** 0.86
