# Section 4: Applications and Bit-Reversal
## القسم 4: التطبيقات وعكس البتات

**Section:** applications
**Translation Quality:** 0.85
**Glossary Terms Used:** algorithm, bit, binary, array, storage location, index, parallel computation, difference equation, Fourier series, in-place computation

---

### English Version

Writing out the sum this appears as

$$A_i(j_0, \cdots, j_{i-1}, k_{m-i-1}, \cdots, k_0)$$

$$(20) \qquad \begin{aligned}
&= A_{i-1}(j_0, \cdots, j_{i-2}, 0, k_{m-i-1}, \cdots, k_0) \\
&\quad + (-1)^{j_{i-1}} j^{i-2} A_{i-1}(j_0, \cdots, j_{i-2}, 1, k_{m-i-1}, \cdots, k_0) \\
&\quad \cdot W^{(j_{i-1} \cdot 2^{i-1} + \cdots + j_0) \cdot 2^{m-i}}, \qquad j_{i-1} = 0, 1.
\end{aligned}$$

According to the indexing convention, this is stored in a location whose index is

$$(21) \qquad j_0 \cdot 2^{m-1} + \cdots + j_{i-1} \cdot 2^{m-i} + k_{m-i-1} \cdot 2^{m-i-1} + \cdots + k_0.$$

It can be seen in (20) that only the two storage locations with indices having 0 and 1 in the $2^{m-i}$ bit position are involved in the computation. Parallel computation is permitted since the operation described by (20) can be carried out with all values of $j_0, \cdots, j_{i-2}$, and $k_0, \cdots, k_{m-i-1}$ simultaneously. In some applications* it is convenient to use (20) to express $A_i$ in terms of $A_{i-2}$, giving what is equivalent to an algorithm with $r = 4$.

The last array calculated gives the desired Fourier sums,

$$(22) \qquad X(j_{m-1}, \cdots, j_0) = A_m(j_0, \cdots, j_{m-1})$$

in such an order that the index of an $X$ must have its binary bits put in reverse order to yield its index in the array $A_m$.

In some applications, where Fourier sums are to be evaluated twice, the above procedure could be programmed so that no bit-inversion is necessary. For example, consider the solution of the difference equation,

$$(23) \qquad aX(j + 1) + bX(j) + cX(j - 1) = F(j).$$

The present method could be first applied to calculate the Fourier amplitudes of $F(j)$ from the formula

$$(24) \qquad B(k) = \frac{1}{N} \sum_j F(j)W^{-jk}.$$

The Fourier amplitudes of the solution are, then,

$$(25) \qquad A(k) = \frac{B(k)}{aW^k + b + cW^{-k}}.$$

The $B(k)$ and $A(k)$ arrays are in bit-inverted order, but with an obvious modification of (20), $A(k)$ can be used to yield the solution with correct indexing.

A computer program for the IBM 7094 has been written which calculates three-dimensional Fourier sums by the above method. The computing time taken for computing three-dimensional $2^r \times 2^r \times 2^r$ arrays of data points was as follows:

---

### النسخة العربية

بكتابة المجموع، يظهر هذا كالآتي

$$A_i(j_0, \cdots, j_{i-1}, k_{m-i-1}, \cdots, k_0)$$

$$(20) \qquad \begin{aligned}
&= A_{i-1}(j_0, \cdots, j_{i-2}, 0, k_{m-i-1}, \cdots, k_0) \\
&\quad + (-1)^{j_{i-1}} j^{i-2} A_{i-1}(j_0, \cdots, j_{i-2}, 1, k_{m-i-1}, \cdots, k_0) \\
&\quad \cdot W^{(j_{i-1} \cdot 2^{i-1} + \cdots + j_0) \cdot 2^{m-i}}, \qquad j_{i-1} = 0, 1.
\end{aligned}$$

وفقًا لاصطلاح الفهرسة، يُخزَّن هذا في موقع يكون مؤشره

$$(21) \qquad j_0 \cdot 2^{m-1} + \cdots + j_{i-1} \cdot 2^{m-i} + k_{m-i-1} \cdot 2^{m-i-1} + \cdots + k_0.$$

يمكن ملاحظة في (20) أن موقعي التخزين الوحيدين اللذين لهما مؤشرات بقيمة 0 و 1 في موقع البت $2^{m-i}$ هما المشاركان في الحساب. الحساب المتوازي ممكن لأن العملية الموصوفة بـ (20) يمكن تنفيذها مع جميع قيم $j_0, \cdots, j_{i-2}$، و $k_0, \cdots, k_{m-i-1}$ في وقت واحد. في بعض التطبيقات* من المناسب استخدام (20) للتعبير عن $A_i$ بدلالة $A_{i-2}$، ما يعطي ما يكافئ خوارزمية مع $r = 4$.

تُعطي المصفوفة الأخيرة المحسوبة مجاميع فورييه المطلوبة،

$$(22) \qquad X(j_{m-1}, \cdots, j_0) = A_m(j_0, \cdots, j_{m-1})$$

بترتيب يجب فيه أن يكون لمؤشر $X$ بتاته الثنائية معكوسة لإنتاج مؤشره في المصفوفة $A_m$.

في بعض التطبيقات، حيث يجب حساب مجاميع فورييه مرتين، يمكن برمجة الإجراء أعلاه بحيث لا تكون عملية عكس البتات ضرورية. على سبيل المثال، لنتأمل حل معادلة الفروق،

$$(23) \qquad aX(j + 1) + bX(j) + cX(j - 1) = F(j).$$

يمكن تطبيق الطريقة الحالية أولاً لحساب سعات فورييه لـ $F(j)$ من الصيغة

$$(24) \qquad B(k) = \frac{1}{N} \sum_j F(j)W^{-jk}.$$

تكون سعات فورييه للحل، إذن،

$$(25) \qquad A(k) = \frac{B(k)}{aW^k + b + cW^{-k}}.$$

مصفوفتا $B(k)$ و $A(k)$ بترتيب معكوس البتات، لكن مع تعديل واضح لـ (20)، يمكن استخدام $A(k)$ لإنتاج الحل مع فهرسة صحيحة.

كُتِب برنامج حاسوبي لجهاز IBM 7094 يحسب مجاميع فورييه ثلاثية الأبعاد بالطريقة أعلاه. كان الوقت الحسابي المستغرق لحساب مصفوفات ثلاثية الأبعاد $2^r \times 2^r \times 2^r$ من نقاط البيانات كالتالي:

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Bit-reversal - عكس البتات
  - Bit position - موقع البت
  - Parallel computation - الحساب المتوازي
  - In-place computation - الحساب في المكان نفسه
  - Indexing convention - اصطلاح الفهرسة
  - Storage location - موقع التخزين
  - Difference equation - معادلة الفروق
  - Fourier amplitudes - سعات فورييه
  - Three-dimensional - ثلاثي الأبعاد
  - Bit-inverted order - ترتيب معكوس البتات

- **Equations:** 6 equations (20-25)
- **Citations:** None in this section
- **Special handling:**
  - Footnote marked with * (refers to IBM Watson Research Center work)
  - Difference equation application example
  - Implementation details for IBM 7094
  - Discussion of bit-reversal optimization

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.83
- Glossary consistency: 0.84
- **Overall section score:** 0.85

### Back-Translation Validation

By writing the sum, this appears as follows [equation 20]. According to the indexing convention, this is stored in a location whose index is [equation 21]. It can be observed in (20) that the only two storage locations that have indices with values 0 and 1 in bit position 2^(m-i) are the ones participating in the computation. Parallel computation is possible because the operation described by (20) can be executed with all values of j₀, ..., j_{i-2}, and k₀, ..., k_{m-i-1} at the same time. In some applications, it is convenient to use (20) to express A_i in terms of A_{i-2}, giving what is equivalent to an algorithm with r = 4. The last calculated array gives the desired Fourier sums [equation 22] in an order where the index of X must have its binary bits reversed to produce its index in array A_m. In some applications, where Fourier sums must be calculated twice, the above procedure can be programmed so that bit-reversal is not necessary. For example, let us consider solving the difference equation [equation 23]. The current method can be applied first to calculate the Fourier amplitudes of F(j) from the formula [equation 24]. The Fourier amplitudes of the solution are then [equation 25]. The B(k) and A(k) arrays are in bit-reversed order, but with an obvious modification to (20), A(k) can be used to produce the solution with correct indexing. A computer program for the IBM 7094 was written that calculates three-dimensional Fourier sums by the above method.

**Validation:** Back-translation accurately captures the technical content and implementation details. Score: 0.85 ✓
