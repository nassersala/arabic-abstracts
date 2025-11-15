# Section 13: Fourier Analysis
## القسم 13: تحليل فورييه

**Section:** fourier-analysis
**Translation Quality:** 0.86
**Glossary Terms Used:** Fourier analysis, bandwidth, frequency, Nyquist sample rate, power spectrum

---

### English Version

If a sinusoidal signal has a period of $\lambda$ seconds then it has a frequency of $f = 1/\lambda$ periods per second, measured in Hertz (Hz). A sinusoid with a frequency of $W$ Hz can be represented perfectly if its value is measured at the Nyquist sample rate[6] of $2W$ times per second. Indeed, Fourier analysis allows almost any signal $x$ to be represented as a mixture of sinusoidal Fourier components $x(f) : (f = 0, \ldots, W)$, shown in Figure 10. A signal which includes frequencies between 0 Hz and $W$Hz has a bandwidth of $W$ Hz.

**Fourier Analysis.** Fourier analysis allows any signal to be represented as a weighted sum of sine and cosine functions. More formally, consider a signal $x$ with a value $x_t$ at time $t$, which spans a time interval of $T$ seconds. This signal can be represented as a weighted average of sine and cosine functions

$$x_t = x_0 + \sum_{n=1}^{\infty} a_n \cos(f_n t) + \sum_{n=1}^{\infty} b_n \sin(f_n t),$$ (25)

where $f_n = 2\pi n/T$ represents frequency, $a_n$ is the Fourier coefficient (amplitude) of a cosine with frequency $f_n$, and $b_n$ is the Fourier coefficient of a sine with frequency $f_n$; and $x_0$ represents the background amplitude (usually assumed to be zero). Taken over all frequencies, these pairs of coefficients represent the Fourier transform of $x$.

The Fourier coefficients can be found from the integrals

$$a_n = \frac{2}{T} \int_0^T x_t \cos(f_n t) dt$$ (26)

$$b_n = \frac{2}{T} \int_0^T x_t \sin(f_n t) dt.$$ (27)

Each coefficient $a_n$ specifies how much of the signal $x$ consists of a cosine at the frequency $f_n$, and $b_n$ specifies how much consists of a sine. Each pair of coefficients specifies the power and phase of one frequency component; the power at frequency $f_n$ is $S_f = (a_n^2 + b_n^2)$, and the phase is $\arctan(b_n/a_n)$. If $x$ has a bandwidth of $W$Hz then its power spectrum is the set of $W$ values $S_0, \ldots, S_W$.

An extremely useful property of Fourier analysis is that, when applied to any variable, the resultant Fourier components are mutually uncorrelated[7], and, when applied to any Gaussian variable, these Fourier components are also mutually independent. This means that the entropy of any Gaussian variable can be estimated by adding up the entropies of its Fourier components, which can be used to estimate the mutual information between Gaussian variables.

Consider a variable $y = x + \eta$, which is the sum of a Gaussian signal $x$ with variance $S$, and Gaussian noise with variance $N$. If the highest frequency in $y$ is $W$ Hz, and if values of $x$ are transmitted at the Nyquist rate of $2W$ Hz, then the channel capacity is $2W C$ bits per second, (where $C$ is defined in Equation 23). Thus, when expressed in terms of bits per second, this yields a channel capacity of

$$C = W \log \left(1 + \frac{S}{N}\right) \text{ bits/s.}$$ (28)

If the signal power of Fourier component $x(f)$ is $S(f)$, and the noise power of component $\eta(f)$ is $N(f)$ then the signal to noise ratio is $S(f)/N(f)$. The mutual information at frequency $f$ is therefore

$$I(x(f), y(f)) = \log \left(1 + \frac{S(f)}{N(f)}\right) \text{ bits/s.}$$ (29)

Because the Fourier components of any Gaussian variable are mutually independent, the mutual information between Gaussian variables can be obtained by summing $I(x(f), y(f))$ over frequency

$$I(x, y) = \int_{f=0}^W I(x(f), y(f)) df \text{ bits/s.}$$ (30)

If each Gaussian variable $x, y$ and $\eta$ is also iid then $I(x, y) = C$ bits/s, otherwise $I(x, y) < C$ bits/s[2]. If the signal spectrum is sculpted so that the signal plus noise spectrum is flat then the logarithmic relation in Equation 23 yields improved, albeit still diminishing, returns[7] $C \propto (S/N)^{1/3}$ bits/s.

---

### النسخة العربية

إذا كانت للإشارة الجيبية فترة $\lambda$ ثانية فإن لها تردداً $f = 1/\lambda$ فترة في الثانية، مُقاساً بالهرتز (Hz). يمكن تمثيل موجة جيبية بتردد $W$ Hz بشكل مثالي إذا قيست قيمتها عند معدل عينة نايكويست[6] البالغ $2W$ مرة في الثانية. في الواقع، يسمح تحليل فورييه لأي إشارة $x$ تقريباً بأن تُمثل كمزيج من مكونات فورييه الجيبية $x(f) : (f = 0, \ldots, W)$، الموضحة في الشكل 10. الإشارة التي تتضمن ترددات بين 0 Hz و $W$Hz لها عرض نطاق $W$ Hz.

**تحليل فورييه.** يسمح تحليل فورييه لأي إشارة بأن تُمثل كمجموع موزون من دوال الجيب وجيب التمام. بشكل أكثر رسمية، فكر في إشارة $x$ بقيمة $x_t$ عند الوقت $t$، والتي تمتد لفترة زمنية $T$ ثانية. يمكن تمثيل هذه الإشارة كمتوسط موزون من دوال الجيب وجيب التمام

$$x_t = x_0 + \sum_{n=1}^{\infty} a_n \cos(f_n t) + \sum_{n=1}^{\infty} b_n \sin(f_n t),$$ (25)

حيث $f_n = 2\pi n/T$ يمثل التردد، $a_n$ هو معامل فورييه (السعة) لجيب تمام بتردد $f_n$، و $b_n$ هو معامل فورييه لجيب بتردد $f_n$؛ و $x_0$ يمثل سعة الخلفية (يُفترض عادة أن تكون صفراً). عندما تؤخذ عبر جميع الترددات، تمثل هذه الأزواج من المعاملات تحويل فورييه لـ $x$.

يمكن إيجاد معاملات فورييه من التكاملات

$$a_n = \frac{2}{T} \int_0^T x_t \cos(f_n t) dt$$ (26)

$$b_n = \frac{2}{T} \int_0^T x_t \sin(f_n t) dt.$$ (27)

يحدد كل معامل $a_n$ مقدار الإشارة $x$ المكونة من جيب تمام عند التردد $f_n$، و $b_n$ يحدد مقدار ما يتكون من جيب. يحدد كل زوج من المعاملات القدرة والطور لمكون تردد واحد؛ القدرة عند التردد $f_n$ هي $S_f = (a_n^2 + b_n^2)$، والطور هو $\arctan(b_n/a_n)$. إذا كان لـ $x$ عرض نطاق $W$Hz فإن طيف القدرة الخاص به هو مجموعة القيم $W$ $S_0, \ldots, S_W$.

خاصية مفيدة للغاية لتحليل فورييه هي أنه، عند تطبيقه على أي متغير، فإن مكونات فورييه الناتجة غير مترابطة بشكل متبادل[7]، وعند تطبيقه على أي متغير غاوسي، تكون مكونات فورييه هذه أيضاً مستقلة بشكل متبادل. هذا يعني أنه يمكن تقدير إنتروبيا أي متغير غاوسي بجمع إنتروبيات مكونات فورييه الخاصة به، والتي يمكن استخدامها لتقدير المعلومات المشتركة بين متغيرات غاوسية.

فكر في متغير $y = x + \eta$، وهو مجموع إشارة غاوسية $x$ بتباين $S$، وضوضاء غاوسية بتباين $N$. إذا كان أعلى تردد في $y$ هو $W$ Hz، وإذا نُقلت قيم $x$ بمعدل نايكويست $2W$ Hz، فإن سعة القناة هي $2W C$ بتة في الثانية، (حيث $C$ محددة في المعادلة 23). وبالتالي، عندما يُعبر عنها بدلالة بتات في الثانية، ينتج هذا سعة قناة

$$C = W \log \left(1 + \frac{S}{N}\right) \text{ بتات/ث.}$$ (28)

إذا كانت قدرة الإشارة لمكون فورييه $x(f)$ هي $S(f)$، وقدرة الضوضاء لمكون $\eta(f)$ هي $N(f)$ فإن نسبة الإشارة إلى الضوضاء هي $S(f)/N(f)$. المعلومات المشتركة عند التردد $f$ هي بالتالي

$$I(x(f), y(f)) = \log \left(1 + \frac{S(f)}{N(f)}\right) \text{ بتات/ث.}$$ (29)

نظراً لأن مكونات فورييه لأي متغير غاوسي مستقلة بشكل متبادل، يمكن الحصول على المعلومات المشتركة بين متغيرات غاوسية بجمع $I(x(f), y(f))$ عبر التردد

$$I(x, y) = \int_{f=0}^W I(x(f), y(f)) df \text{ بتات/ث.}$$ (30)

إذا كان كل متغير غاوسي $x, y$ و $\eta$ أيضاً مستقلاً ومتطابق التوزيع فإن $I(x, y) = C$ بتات/ث، وإلا $I(x, y) < C$ بتات/ث[2]. إذا نُحت طيف الإشارة بحيث يكون طيف الإشارة زائد الضوضاء مسطحاً فإن العلاقة اللوغاريتمية في المعادلة 23 تنتج عوائد محسّنة، وإن كانت لا تزال متناقصة،[7] $C \propto (S/N)^{1/3}$ بتات/ث.

---

### Quality Metrics
- **Overall section score:** 0.86
