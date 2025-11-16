# Section 3: Implementation Notes and Generalization
## القسم 3: ملاحظات التنفيذ والتعميم

**Section:** implementation-notes
**Translation Quality:** 0.86
**Glossary Terms Used:** algorithm, operation, binary, bit, factorization, composite number, array, parallel computation, storage location, index, optimization

---

### English Version

It is easy to see how successive applications of the above procedure, starting with its application to (6), give an m-step algorithm requiring

$$(9) \qquad T = N(r_1 + r_2 + \cdots + r_m)$$

operations, where

$$(10) \qquad N = r_1 \cdot r_2 \cdots r_m.$$

If $r_j = s_j t_j$ with $s_j, t_j > 1$, then $s_j + t_j < r_j$ unless $s_j = t_j = 2$, when $s_j + t_j = r_j$. In general, then, using as many factors as possible provides a minimum to (9), but factors of 2 can be combined in pairs without loss. If we are able to choose $N$ to be highly composite, we may make very real gains. If all $r_j$ are equal to $r$, then, from (10) we have

$$(11) \qquad m = \log_r N$$

and the total number of operations is

$$(12) \qquad T(r) = rN \log_r N.$$

If $N = r^m s^n t^p \cdots$, then we find that

$$(13) \qquad \begin{aligned}
\frac{T}{N} &= m \cdot r + n \cdot s + p \cdot t + \cdots, \\
\log_2 N &= m \cdot \log_2 r + n \cdot \log_2 s + p \cdot \log_2 t + \cdots,
\end{aligned}$$

so that

$$\frac{T}{N \log_2 N}$$

is a weighted mean of the quantities

$$\frac{r}{\log_2 r}, \quad \frac{s}{\log_2 s}, \quad \frac{t}{\log_2 t}, \cdots,$$

whose values run as follows

| $r$ | $\frac{r}{\log_2 r}$ |
|-----|----------------------|
| 2   | 2.00                 |
| 3   | 1.88                 |
| 4   | 2.00                 |
| 5   | 2.15                 |
| 6   | 2.31                 |
| 7   | 2.49                 |
| 8   | 2.67                 |
| 9   | 2.82                 |
| 10  | 3.01                 |

The use of $r_j = 3$ is formally most efficient, but the gain is only about 6% over the use of 2 or 4, which have other advantages. If necessary, the use of $r_j$ up to 10 can increase the number of computations by no more than 50%. Accordingly, we can find "highly composite" values of $N$ within a few percent of any given large number.

Whenever possible, the use of $N = r^m$ with $r = 2$ or 4 offers important advantages for computers with binary arithmetic, both in addressing and in multiplication economy.

The algorithm with $r = 2$ is derived by expressing the indices in the form

$$(14) \qquad \begin{aligned}
j &= j_{m-1} \cdot 2^{m-1} + \cdots + j_1 \cdot 2 + j_0, \\
k &= k_{m-1} \cdot 2^{m-1} + \cdots + k_1 \cdot 2 + k_0,
\end{aligned}$$

where $j_i$ and $k_i$ are equal to 0 or 1 and are the contents of the respective bit positions in the binary representation of $j$ and $k$. All arrays will now be written as functions of the bits of their indices. With this convention (1) is written

$$(15) \quad X(j_{m-1}, \cdots, j_0) = \sum_{k_0} \sum_{k_1} \cdots \sum_{k_{m-1}} A(k_{m-1}, \cdots, k_0) \cdot W^{j_{m-1} \cdot 2^{m-1} + \cdots + j_0k_0},$$

where the sums are over $k_i = 0, 1$. Since

$$(16) \qquad W^{jk_{m-1} \cdot 2^{m-1}} = W^{j_0k_{m-1} \cdot 2^{m-1}},$$

the innermost sum of (15), over $k_{m-1}$, depends only on $j_0$, $k_{m-2}$, $\cdots$, $k_0$ and can be written

$$(17) \quad A_1(j_0, k_{m-2}, \cdots, k_0) = \sum_{k_{m-1}} A(k_{m-1}, \cdots, k_0) \cdot W^{j_0k_{m-1} \cdot 2^{m-1}}.$$

Proceeding to the next innermost sum, over $k_{m-2}$, and so on, and using

$$(18) \qquad W^{j \cdot k_{m-i} \cdot 2^{m-i}} = W^{(j_{i-1} \cdot 2^{i-1} + \cdots + j_0) k_{m-i} \cdot 2^{m-i}},$$

one obtains successive arrays,

$$(19) \quad \begin{aligned}
&A_i(j_0, \cdots, j_{i-1}, k_{m-i-1}, \cdots, k_0) \\
&\qquad = \sum_{k_{m-i}} A_{i-1}(j_0, \cdots, j_{i-2}, k_{m-i}, \cdots, k_0) \cdot W^{(j_{i-1} \cdot 2^{i-1} + \cdots + j_0) \cdot k_{m-i} \cdot 2^{m-i}}
\end{aligned}$$

for $i = 1, 2, \cdots, m$.

---

### النسخة العربية

من السهل معرفة كيف أن التطبيقات المتتالية للإجراء أعلاه، بدءًا من تطبيقه على (6)، تُعطي خوارزمية من m خطوة تتطلب

$$(9) \qquad T = N(r_1 + r_2 + \cdots + r_m)$$

عملية، حيث

$$(10) \qquad N = r_1 \cdot r_2 \cdots r_m.$$

إذا كان $r_j = s_j t_j$ حيث $s_j, t_j > 1$، فإن $s_j + t_j < r_j$ إلا في حالة $s_j = t_j = 2$، عندما يكون $s_j + t_j = r_j$. بشكل عام، إذن، فإن استخدام أكبر عدد ممكن من العوامل يوفر الحد الأدنى لـ (9)، لكن يمكن دمج عوامل 2 في أزواج دون خسارة. إذا كنا قادرين على اختيار $N$ ليكون عددًا مركبًا بدرجة عالية، فقد نحقق مكاسب حقيقية. إذا كانت جميع $r_j$ تساوي $r$، فإننا نحصل من (10) على

$$(11) \qquad m = \log_r N$$

ويكون العدد الإجمالي للعمليات هو

$$(12) \qquad T(r) = rN \log_r N.$$

إذا كان $N = r^m s^n t^p \cdots$، فإننا نجد أن

$$(13) \qquad \begin{aligned}
\frac{T}{N} &= m \cdot r + n \cdot s + p \cdot t + \cdots, \\
\log_2 N &= m \cdot \log_2 r + n \cdot \log_2 s + p \cdot \log_2 t + \cdots,
\end{aligned}$$

بحيث أن

$$\frac{T}{N \log_2 N}$$

هو متوسط مرجّح للكميات

$$\frac{r}{\log_2 r}, \quad \frac{s}{\log_2 s}, \quad \frac{t}{\log_2 t}, \cdots,$$

التي تسير قيمها كالتالي

| $r$ | $\frac{r}{\log_2 r}$ |
|-----|----------------------|
| 2   | 2.00                 |
| 3   | 1.88                 |
| 4   | 2.00                 |
| 5   | 2.15                 |
| 6   | 2.31                 |
| 7   | 2.49                 |
| 8   | 2.67                 |
| 9   | 2.82                 |
| 10  | 3.01                 |

إن استخدام $r_j = 3$ هو الأكثر كفاءة رسميًا، لكن المكسب يبلغ حوالي 6% فقط مقارنة باستخدام 2 أو 4، اللذين لهما مزايا أخرى. إذا لزم الأمر، يمكن لاستخدام $r_j$ حتى 10 أن يزيد عدد العمليات الحسابية بما لا يزيد عن 50%. وبناءً عليه، يمكننا إيجاد قيم "مركبة بدرجة عالية" لـ $N$ ضمن نسبة مئوية قليلة من أي عدد كبير معطى.

كلما أمكن، فإن استخدام $N = r^m$ مع $r = 2$ أو 4 يوفر مزايا مهمة للحواسيب ذات الحساب الثنائي، سواء في العنونة أو في اقتصاد الضرب.

تُشتَق الخوارزمية مع $r = 2$ بالتعبير عن المؤشرات بالصورة

$$(14) \qquad \begin{aligned}
j &= j_{m-1} \cdot 2^{m-1} + \cdots + j_1 \cdot 2 + j_0, \\
k &= k_{m-1} \cdot 2^{m-1} + \cdots + k_1 \cdot 2 + k_0,
\end{aligned}$$

حيث $j_i$ و $k_i$ يساويان 0 أو 1 ويمثلان محتويات مواقع البتات المعنية في التمثيل الثنائي لـ $j$ و $k$. ستُكتَب الآن جميع المصفوفات كدوال لبتات مؤشراتها. باستخدام هذا الاصطلاح، تُكتَب (1) بالصورة

$$(15) \quad X(j_{m-1}, \cdots, j_0) = \sum_{k_0} \sum_{k_1} \cdots \sum_{k_{m-1}} A(k_{m-1}, \cdots, k_0) \cdot W^{j_{m-1} \cdot 2^{m-1} + \cdots + j_0k_0},$$

حيث المجاميع على $k_i = 0, 1$. بما أن

$$(16) \qquad W^{jk_{m-1} \cdot 2^{m-1}} = W^{j_0k_{m-1} \cdot 2^{m-1}},$$

فإن المجموع الأعمق في (15)، على $k_{m-1}$، يعتمد فقط على $j_0$، $k_{m-2}$، $\cdots$، $k_0$ ويمكن كتابته

$$(17) \quad A_1(j_0, k_{m-2}, \cdots, k_0) = \sum_{k_{m-1}} A(k_{m-1}, \cdots, k_0) \cdot W^{j_0k_{m-1} \cdot 2^{m-1}}.$$

بالانتقال إلى المجموع الأعمق التالي، على $k_{m-2}$، وهكذا دواليك، وباستخدام

$$(18) \qquad W^{j \cdot k_{m-i} \cdot 2^{m-i}} = W^{(j_{i-1} \cdot 2^{i-1} + \cdots + j_0) k_{m-i} \cdot 2^{m-i}},$$

نحصل على مصفوفات متتالية،

$$(19) \quad \begin{aligned}
&A_i(j_0, \cdots, j_{i-1}, k_{m-i-1}, \cdots, k_0) \\
&\qquad = \sum_{k_{m-i}} A_{i-1}(j_0, \cdots, j_{i-2}, k_{m-i}, \cdots, k_0) \cdot W^{(j_{i-1} \cdot 2^{i-1} + \cdots + j_0) \cdot k_{m-i} \cdot 2^{m-i}}
\end{aligned}$$

لـ $i = 1, 2, \cdots, m$.

---

### Translation Notes

- **Figures referenced:** None
- **Tables:** 1 table showing efficiency ratios for different radix values
- **Key terms introduced:**
  - m-step algorithm - خوارزمية من m خطوة
  - Highly composite - مركب بدرجة عالية
  - Weighted mean - متوسط مرجّح
  - Binary arithmetic - الحساب الثنائي
  - Multiplication economy - اقتصاد الضرب
  - Addressing - العنونة
  - Bit position - موقع البت
  - Binary representation - التمثيل الثنائي
  - Innermost sum - المجموع الأعمق
  - Successive arrays - مصفوفات متتالية
  - Radix - الأساس (في النظام العددي)

- **Equations:** 11 equations (9-19)
- **Citations:** None in this section
- **Special handling:**
  - Table translated with preserved numerical values
  - All LaTeX equations maintained
  - Binary notation and bit-level descriptions carefully translated
  - Technical optimization discussion preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation Validation

It is easy to know how successive applications of the above procedure, starting from its application to (6), give an m-step algorithm that requires [equation 9] operations, where [equation 10]. If r_j = s_j t_j where s_j, t_j > 1, then s_j + t_j < r_j except when s_j = t_j = 2, when s_j + t_j = r_j. In general, then, using the maximum number of possible factors provides the minimum for (9), but factors of 2 can be combined in pairs without loss. If we are able to choose N to be a highly composite number, we may achieve real gains. If all r_j equal r, then we get from (10) [equation 11] and the total number of operations is [equation 12]. The use of r_j = 3 is formally the most efficient, but the gain is only about 6% compared to using 2 or 4, which have other advantages. If necessary, using r_j up to 10 can increase the number of computations by no more than 50%. Accordingly, we can find "highly composite" values of N within a few percent of any given large number. Whenever possible, using N = r^m with r = 2 or 4 provides important advantages for computers with binary arithmetic, both in addressing and in multiplication economy. The algorithm with r = 2 is derived by expressing the indices in the form [equation 14], where j_i and k_i equal 0 or 1 and represent the contents of the respective bit positions in the binary representation of j and k.

**Validation:** Back-translation accurately preserves the mathematical and technical content. Score: 0.86 ✓
