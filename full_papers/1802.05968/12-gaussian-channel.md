# Section 12: The Gaussian Channel
## القسم 12: القناة الغاوسية

**Section:** gaussian-channel
**Translation Quality:** 0.87
**Glossary Terms Used:** Gaussian distribution, channel capacity, signal-to-noise ratio, variance, iid

---

### English Version

If the noise values in a channel are drawn independently from a Gaussian distribution (i.e. $\eta \sim N(\mu_\eta, v_\eta)$, as defined in Equation 6) then this defines a Gaussian channel.

Given that $y = x + \eta$, if we want $p(y)$ to be Gaussian then we should ensure that $p(x)$ and $p(\eta)$ are Gaussian, because the sum of two independent Gaussian variables is also Gaussian[3]. So, $p(x)$ must be (iid) Gaussian in order to maximise $H(x)$, which maximises $H(y)$, which maximises $I(x, y)$. Thus, if each input, output, and noise variable is (iid) Gaussian then the average amount of information communicated per output value is the channel capacity, so that $I(x, y) = C$ bits. This is an informal statement of Shannon's continuous noisy channel coding theorem for Gaussian channels. We can use this to express capacity in terms of the input, output, and noise.

If the channel input $x \sim N(\mu_x, v_x)$ then the continuous analogue (integral) of Equation 4 yields the differential entropy

$$H(x) = (1/2) \log 2\pi e v_x \text{ bits.}$$ (19)

The distinction between differential entropy effectively disappears when considering the difference between entropies, and we will therefore find that we can safely ignore this distinction here. Given that the channel noise is iid Gaussian, its entropy is

$$H(\eta) = (1/2) \log 2\pi e v_\eta \text{ bits.}$$ (20)

Because the output is the sum $y = x + \eta$, it is also iid Gaussian with variance $v_y = v_x + v_\eta$, and its entropy is

$$H(y) = (1/2) \log 2\pi e(v_x + v_\eta) \text{ bits.}$$ (21)

Substituting Equations 20 and 21 into Equation 16 yields

$$I(x, y) = \frac{1}{2} \log \left(1 + \frac{v_x}{v_\eta}\right) \text{ bits,}$$ (22)

which allows us to choose one out of $m = 2^I$ equiprobable values. For a Gaussian channel, $I(x, y)$ attains its maximal value of $C$ bits.

The variance of any signal with a mean of zero is equal to its power, which is the rate at which energy is expended per second, and the physical unit of power is measured in Joules per second (J/s) or Watts, where 1 Watt = 1 J/s. Accordingly, the signal power is $S = v_x$ J/s, and the noise power is $N = v_\eta$ J/s. This yields Shannon's famous equation for the capacity of a Gaussian channel

$$C = \frac{1}{2} \log \left(1 + \frac{S}{N}\right) \text{ bits,}$$ (23)

where the ratio of variances $S/N$ is the signal to noise ratio (SNR), as in Figure 9.

---

### النسخة العربية

إذا كانت قيم الضوضاء في قناة مسحوبة بشكل مستقل من توزيع غاوسي (أي $\eta \sim N(\mu_\eta, v_\eta)$، كما هو محدد في المعادلة 6) فإن هذا يعرّف قناة غاوسية.

بالنظر إلى أن $y = x + \eta$، إذا أردنا أن يكون $p(y)$ غاوسياً فيجب علينا التأكد من أن $p(x)$ و $p(\eta)$ غاوسيان، لأن مجموع متغيرين غاوسيين مستقلين هو أيضاً غاوسي[3]. لذلك، يجب أن يكون $p(x)$ غاوسياً (مستقلاً ومتطابق التوزيع) من أجل تعظيم $H(x)$، مما يعظم $H(y)$، مما يعظم $I(x, y)$. وبالتالي، إذا كان كل متغير دخل وخرج وضوضاء غاوسياً (مستقلاً ومتطابق التوزيع) فإن متوسط كمية المعلومات المنقولة لكل قيمة خرج هو سعة القناة، بحيث $I(x, y) = C$ بتات. هذا بيان غير رسمي لنظرية الترميز للقناة المشوشة المستمرة لشانون للقنوات الغاوسية. يمكننا استخدام هذا للتعبير عن السعة من حيث الدخل والخرج والضوضاء.

إذا كان دخل القناة $x \sim N(\mu_x, v_x)$ فإن النظير المستمر (التكامل) للمعادلة 4 ينتج الإنتروبيا التفاضلية

$$H(x) = (1/2) \log 2\pi e v_x \text{ بتات.}$$ (19)

يختفي التمييز بين الإنتروبيا التفاضلية فعلياً عند النظر في الفرق بين الإنتروبيات، وبالتالي سنجد أنه يمكننا تجاهل هذا التمييز بأمان هنا. بالنظر إلى أن ضوضاء القناة غاوسية مستقلة ومتطابقة التوزيع، فإن إنتروبيتها هي

$$H(\eta) = (1/2) \log 2\pi e v_\eta \text{ بتات.}$$ (20)

نظراً لأن الخرج هو المجموع $y = x + \eta$، فهو أيضاً غاوسي مستقل ومتطابق التوزيع بتباين $v_y = v_x + v_\eta$، وإنتروبيته هي

$$H(y) = (1/2) \log 2\pi e(v_x + v_\eta) \text{ بتات.}$$ (21)

بتعويض المعادلات 20 و 21 في المعادلة 16 ينتج

$$I(x, y) = \frac{1}{2} \log \left(1 + \frac{v_x}{v_\eta}\right) \text{ بتات،}$$ (22)

مما يسمح لنا بالاختيار واحدة من $m = 2^I$ قيمة متساوية الاحتمال. بالنسبة لقناة غاوسية، تصل $I(x, y)$ إلى قيمتها القصوى $C$ بتات.

تباين أي إشارة بمتوسط صفر يساوي قدرتها، وهي المعدل الذي يتم به إنفاق الطاقة في الثانية، والوحدة الفيزيائية للقدرة تُقاس بالجول في الثانية (ج/ث) أو الواط، حيث 1 واط = 1 ج/ث. وفقاً لذلك، قدرة الإشارة هي $S = v_x$ ج/ث، وقدرة الضوضاء هي $N = v_\eta$ ج/ث. ينتج هذا معادلة شانون الشهيرة لسعة القناة الغاوسية

$$C = \frac{1}{2} \log \left(1 + \frac{S}{N}\right) \text{ بتات،}$$ (23)

حيث نسبة التباينات $S/N$ هي نسبة الإشارة إلى الضوضاء (SNR)، كما في الشكل 9.

---

### Quality Metrics
- **Overall section score:** 0.87
