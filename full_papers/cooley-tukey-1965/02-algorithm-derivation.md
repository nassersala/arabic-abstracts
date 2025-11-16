# Section 2: Algorithm Derivation (Two-Factor Case)
## القسم 2: اشتقاق الخوارزمية (حالة العاملين)

**Section:** algorithm-derivation
**Translation Quality:** 0.87
**Glossary Terms Used:** algorithm, operation, computation, complex, vector, array, Fourier series, coefficient, principal root of unity, composite number, factorization

---

### English Version

Consider the problem of calculating the complex Fourier series

$$(1) \qquad X(j) = \sum_{k=0}^{N-1} A(k) \cdot W^{jk}, \qquad j = 0, 1, \cdots, N-1,$$

where the given Fourier coefficients $A(k)$ are complex and $W$ is the principal Nth root of unity,

$$(2) \qquad W = e^{2\pi i/N}.$$

A straightforward calculation using (1) would require $N^2$ operations where "operation" means, as it will throughout this note, a complex multiplication followed by a complex addition.

The algorithm described here iterates on the array of given complex Fourier amplitudes and yields the result in less than $2N \log_2 N$ operations without requiring more data storage than is required for the given array $A$. To derive the algorithm, suppose $N$ is a composite, i.e., $N = r_1 \cdot r_2$. Then let the indices in (1) be expressed

$$(3) \qquad \begin{aligned}
j &= j_1 r_1 + j_0, & j_0 &= 0, 1, \cdots, r_1 - 1, & j_1 &= 0, 1, \cdots, r_2 - 1, \\
k &= k_1 r_2 + k_0, & k_0 &= 0, 1, \cdots, r_2 - 1, & k_1 &= 0, 1, \cdots, r_1 - 1.
\end{aligned}$$

Then, one can write

$$(4) \qquad X(j_1, j_0) = \sum_{k_0} \sum_{k_1} A(k_1, k_0) \cdot W^{j_1k_1r_2} W^{j_2k_0}.$$

Since

$$(5) \qquad W^{jk_1r_2} = W^{j_0k_1r_2},$$

the inner sum, over $k_1$, depends only on $j_0$ and $k_0$ and can be defined as a new array,

$$(6) \qquad A_1(j_0, k_0) = \sum_{k_1} A(k_1, k_0) \cdot W^{j_0k_1r_2}.$$

The result can then be written

$$(7) \qquad X(j_1, j_0) = \sum_{k_0} A_1(j_0, k_0) \cdot W^{(j_1r_1+j_0)k_0}.$$

There are $N$ elements in the array $A_1$, each requiring $r_1$ operations, giving a total of $Nr_1$ operations to obtain $A_1$. Similarly, it takes $Nr_2$ operations to calculate $X$ from $A_1$. Therefore, this two-step algorithm, given by (6) and (7), requires a total of

$$(8) \qquad T = N(r_1 + r_2)$$

operations.

---

### النسخة العربية

لنتأمل مسألة حساب متسلسلة فورييه المركبة

$$(1) \qquad X(j) = \sum_{k=0}^{N-1} A(k) \cdot W^{jk}, \qquad j = 0, 1, \cdots, N-1,$$

حيث معاملات فورييه المعطاة $A(k)$ مركبة و $W$ هو الجذر الرئيسي للوحدة من الرتبة N،

$$(2) \qquad W = e^{2\pi i/N}.$$

يتطلب الحساب المباشر باستخدام (1) عدد $N^2$ من العمليات حيث تعني "العملية"، كما ستعني في جميع أنحاء هذه الملاحظة، ضرب مركب يليه جمع مركب.

تُكرِّر الخوارزمية الموصوفة هنا على مصفوفة سعات فورييه المركبة المعطاة وتُنتِج النتيجة في أقل من $2N \log_2 N$ عملية دون الحاجة إلى تخزين بيانات أكثر مما هو مطلوب للمصفوفة المعطاة $A$. لاشتقاق الخوارزمية، لنفترض أن $N$ عدد مركب، أي $N = r_1 \cdot r_2$. عندئذ، لتُعبَّر المؤشرات في (1) بالصورة

$$(3) \qquad \begin{aligned}
j &= j_1 r_1 + j_0, & j_0 &= 0, 1, \cdots, r_1 - 1, & j_1 &= 0, 1, \cdots, r_2 - 1, \\
k &= k_1 r_2 + k_0, & k_0 &= 0, 1, \cdots, r_2 - 1, & k_1 &= 0, 1, \cdots, r_1 - 1.
\end{aligned}$$

عندئذ، يمكن كتابة

$$(4) \qquad X(j_1, j_0) = \sum_{k_0} \sum_{k_1} A(k_1, k_0) \cdot W^{j_1k_1r_2} W^{j_2k_0}.$$

بما أن

$$(5) \qquad W^{jk_1r_2} = W^{j_0k_1r_2},$$

فإن المجموع الداخلي، على $k_1$، يعتمد فقط على $j_0$ و $k_0$ ويمكن تعريفه كمصفوفة جديدة،

$$(6) \qquad A_1(j_0, k_0) = \sum_{k_1} A(k_1, k_0) \cdot W^{j_0k_1r_2}.$$

يمكن بعد ذلك كتابة النتيجة بالصورة

$$(7) \qquad X(j_1, j_0) = \sum_{k_0} A_1(j_0, k_0) \cdot W^{(j_1r_1+j_0)k_0}.$$

توجد $N$ عنصر في المصفوفة $A_1$، كل منها يتطلب $r_1$ عملية، ما يُعطي إجمالي $Nr_1$ عملية للحصول على $A_1$. وبالمثل، يستغرق حساب $X$ من $A_1$ عدد $Nr_2$ من العمليات. لذلك، تتطلب هذه الخوارزمية ذات الخطوتين، المعطاة بـ (6) و (7)، إجماليًا

$$(8) \qquad T = N(r_1 + r_2)$$

من العمليات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Complex Fourier series - متسلسلة فورييه المركبة
  - Principal root of unity - الجذر الرئيسي للوحدة
  - Fourier coefficients - معاملات فورييه
  - Complex multiplication - ضرب مركب
  - Complex addition - جمع مركب
  - Composite number - عدد مركب
  - Two-step algorithm - خوارزمية ذات الخطوتين
  - Inner sum - المجموع الداخلي

- **Equations:** 8 equations (1-8)
- **Citations:** None in this section
- **Special handling:**
  - All LaTeX equations preserved exactly
  - Mathematical variables kept in Latin script ($j$, $k$, $N$, $W$, etc.)
  - Subscripts and superscripts maintained
  - Summation notation preserved
  - Arabic explanations flow naturally around equations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-Translation Validation

Let us consider the problem of calculating the complex Fourier series [equation 1], where the given Fourier coefficients A(k) are complex and W is the principal root of unity of order N, [equation 2]. Direct calculation using (1) requires N² operations where "operation" means, as it will mean throughout this note, a complex multiplication followed by a complex addition. The algorithm described here iterates on the array of given complex Fourier amplitudes and produces the result in less than 2N log₂ N operations without requiring more data storage than is required for the given array A. To derive the algorithm, let us assume that N is a composite number, i.e., N = r₁ · r₂. Then, let the indices in (1) be expressed in the form [equation 3]. Then, one can write [equation 4]. Since [equation 5], the inner sum, over k₁, depends only on j₀ and k₀ and can be defined as a new array [equation 6]. The result can then be written in the form [equation 7]. There are N elements in array A₁, each requiring r₁ operations, giving a total of Nr₁ operations to obtain A₁. Similarly, calculating X from A₁ requires Nr₂ operations. Therefore, this two-step algorithm, given by (6) and (7), requires a total of [equation 8] operations.

**Validation:** Back-translation accurately captures the mathematical content and flow. Score: 0.87 ✓
