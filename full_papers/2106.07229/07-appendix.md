# Appendix
## الملحق

**Section:** appendix
**Translation Quality:** 0.86
**Glossary Terms Used:** ReLU, minimax approximation, sign function, polynomial, bootstrapping, modular reduction, failure probability, ciphertext, CKKS, Hamming weight, slots

---

### English Version

**A.1 Minimax Composition of ReLU**

Lee et al. [1] show that the ReLU function has to be approximated with sufficiently high precision if we use the pre-trained model parameters with the original ResNet-20 model. We need a polynomial with quite a large degree if the ReLU function is approximated by a single minimax polynomial, and it needs a pretty large running time to evaluate homomorphically. Instead of using the single minimax polynomial for the ReLU function, they use the formula $\text{ReLU}(x) = \frac{1}{2}x(1 + \text{sign}(x))$ and approximate $\text{sign}(x)$ by the minimax composition of the small polynomials [31]. It reduces the running time of the homomorphic evaluation of the ReLU function, and this approximation method makes more practical the homomorphic evaluation of the non-arithmetic functions such as the ReLU function.

**A.2 Analysis of Bootstrapping Failure**

We describe how the bootstrapping failure affects the evaluation of the whole ResNet, and propose a method to reduce the bootstrapping failure probability. As the bootstrapping of the CKKS scheme is based on the sparsity of the secret key, there is a failure probability of its bootstrapping.

Here is the reason why approximated modulus reduction in the previous CKKS bootstrapping has a certain failure probability. The decryption formula for a ciphertext $(a, b)$ of the CKKS scheme is given as $a \cdot s + b = m + e \pmod{R_q}$ for the secret key $s$; hence, $a \cdot s + b \approx m + q \cdot I \pmod{R_Q}$, where the Hamming weight of $s$ is $h$. As the coefficients of $a$ and $b$ are in $[-\frac{q_0}{2}, \frac{q_0}{2})$, we have that the coefficients of $a \cdot s + b$ have an absolute value less than $\frac{q_0(h+1)}{2}$. However, by LWE assumption, the coefficients of $a \cdot s + b$ follow a scaled Irwin-Hall distribution and it is previously assumed that the coefficients of $I < K = O(\sqrt{h})$ [27]. As the modulus reduction function is approximated in the domain $\{0, \pm1, \ldots, \pm(K-1)\} \times (-\epsilon, \epsilon)$, if a coefficient of $I$ has a value greater than or equal to $K$, the modulus reduction returns a useless value, and thus, failed.

$O(\sqrt{h})$ is a reasonable upper bound for a single bootstrapping, but it is not enough when the number of slots is large and there are many bootstrappings. Let $p$ be the probability of modulus reduction failure, $\Pr(|I_i| \geq K)$. If there are $n$ slots in the ciphertext, there are $2n$ coefficients to perform modulus reduction. Hence, the failure probability of single bootstrapping is $1 - (1 - p)^{2n} \approx 2n \cdot p$. Similarly, when there are $N_b$ bootstrappings in the evaluation of the whole network, the failure probability of the whole network is $2N_b \cdot n \cdot p$. As there are many slots in our ciphertext, and thousands of bootstrapping are performed, the failure probability is very high when we use previous approximate polynomials.

---

### النسخة العربية

**أ.1 التركيب الأصغري الأعظمي لـ ReLU**

يُظهر Lee وآخرون [1] أنه يجب تقريب دالة ReLU بدقة عالية كافية إذا استخدمنا معاملات النموذج المدرب مسبقًا مع نموذج ResNet-20 الأصلي. نحتاج إلى متعددة حدود بدرجة كبيرة جدًا إذا تم تقريب دالة ReLU بمتعددة حدود أصغرية أعظمية واحدة، ويحتاج ذلك إلى وقت تشغيل كبير جدًا للتقييم المتماثل. بدلاً من استخدام متعددة الحدود الأصغرية الأعظمية الواحدة لدالة ReLU، يستخدمون الصيغة $\text{ReLU}(x) = \frac{1}{2}x(1 + \text{sign}(x))$ ويقربون $\text{sign}(x)$ بالتركيب الأصغري الأعظمي لمتعددات الحدود الصغيرة [31]. يُقلل ذلك من وقت التشغيل للتقييم المتماثل لدالة ReLU، وتجعل طريقة التقريب هذه التقييم المتماثل للدوال غير الحسابية مثل دالة ReLU أكثر عملية.

**أ.2 تحليل فشل التمهيد الذاتي**

نصف كيف يؤثر فشل التمهيد الذاتي على تقييم ResNet بالكامل، ونقترح طريقة لتقليل احتمالية فشل التمهيد الذاتي. نظرًا لأن التمهيد الذاتي لمخطط CKKS يعتمد على تفرق المفتاح السري، فهناك احتمالية فشل لتمهيده الذاتي.

فيما يلي السبب في أن التقليل المعياري التقريبي في التمهيد الذاتي لـ CKKS السابق له احتمالية فشل معينة. صيغة فك التشفير لنص مشفر $(a, b)$ من مخطط CKKS تُعطى كـ $a \cdot s + b = m + e \pmod{R_q}$ للمفتاح السري $s$؛ وبالتالي، $a \cdot s + b \approx m + q \cdot I \pmod{R_Q}$، حيث وزن هامينغ لـ $s$ هو $h$. نظرًا لأن معاملات $a$ و$b$ في $[-\frac{q_0}{2}, \frac{q_0}{2})$، فلدينا أن معاملات $a \cdot s + b$ لها قيمة مطلقة أقل من $\frac{q_0(h+1)}{2}$. ومع ذلك، بافتراض LWE، تتبع معاملات $a \cdot s + b$ توزيع Irwin-Hall المقاس وتم افتراض سابقًا أن معاملات $I < K = O(\sqrt{h})$ [27]. نظرًا لأن دالة التقليل المعياري تُقرب في المجال $\{0, \pm1, \ldots, \pm(K-1)\} \times (-\epsilon, \epsilon)$، إذا كان لمعامل $I$ قيمة أكبر من أو تساوي $K$، فإن التقليل المعياري يُرجع قيمة عديمة الفائدة، وبالتالي، يفشل.

$O(\sqrt{h})$ هو حد أعلى معقول لتمهيد ذاتي واحد، لكنه ليس كافيًا عندما يكون عدد الخانات كبيرًا وهناك العديد من التمهيدات الذاتية. لنكن $p$ احتمالية فشل التقليل المعياري، $\Pr(|I_i| \geq K)$. إذا كان هناك $n$ خانات في النص المشفر، فهناك $2n$ معاملات لإجراء التقليل المعياري. وبالتالي، فإن احتمالية الفشل لتمهيد ذاتي واحد هي $1 - (1 - p)^{2n} \approx 2n \cdot p$. وبالمثل، عندما يكون هناك $N_b$ تمهيدات ذاتية في تقييم الشبكة بأكملها، فإن احتمالية فشل الشبكة بأكملها هي $2N_b \cdot n \cdot p$. نظرًا لوجود العديد من الخانات في نصنا المشفر، ويتم تنفيذ الآلاف من التمهيدات الذاتية، فإن احتمالية الفشل عالية جدًا عندما نستخدم متعددات الحدود التقريبية السابقة.

---

### Translation Notes

- **Figures referenced:** None
- **Key mathematical concepts:**
  - Minimax polynomial composition for ReLU
  - Sign function decomposition: $\text{ReLU}(x) = \frac{1}{2}x(1 + \text{sign}(x))$
  - Bootstrapping failure probability analysis
  - Irwin-Hall distribution for coefficients
  - Failure probability propagation: $1 - (1 - p)^{2n} \approx 2n \cdot p$
- **Equations:** Multiple mathematical formulas for bootstrapping failure analysis
- **Citations:** [1, 27, 31]
- **Special handling:**
  - Mathematical notation preserved exactly
  - Big-O notation: $O(\sqrt{h})$
  - Probability formulations maintained
  - LWE (Learning With Errors) kept as technical term

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
