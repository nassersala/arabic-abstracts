# Section 2: Statement of Method
## القسم 2: بيان الطريقة

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** algorithm, matrix, vector, factorization, operation, computation, data point, complex number, index

---

### English Version

Let $N = r_1 r_2$, and consider the $N$ points $x_j$ as a doubly indexed array $x_{j_1, j_2}$ where

$$j = r_2 j_1 + j_2, \quad j_1 = 0, 1, \ldots, r_1 - 1, \quad j_2 = 0, 1, \ldots, r_2 - 1$$

Similarly, let

$$k = r_1 k_2 + k_1, \quad k_1 = 0, 1, \ldots, r_1 - 1, \quad k_2 = 0, 1, \ldots, r_2 - 1$$

Then the Fourier series becomes

$$X_{k_1, k_2} = \sum_{j_1=0}^{r_1-1} \sum_{j_2=0}^{r_2-1} x_{j_1, j_2} W_N^{(r_2 j_1 + j_2)(r_1 k_2 + k_1)}$$

where $W_N = e^{2\pi i/N}$.

The exponent can be rewritten as

$$(r_2 j_1 + j_2)(r_1 k_2 + k_1) = r_1 r_2 j_1 k_2 + r_2 j_1 k_1 + r_1 j_2 k_2 + j_2 k_1$$

Since $W_N^{r_1 r_2} = W_N^N = 1$, we have

$$X_{k_1, k_2} = \sum_{j_1=0}^{r_1-1} \sum_{j_2=0}^{r_2-1} x_{j_1, j_2} W_N^{r_2 j_1 k_1} W_N^{r_1 j_2 k_2} W_N^{j_2 k_1}$$

This can be written as

$$X_{k_1, k_2} = \sum_{j_1=0}^{r_1-1} W_{r_1}^{j_1 k_1} \left[ \sum_{j_2=0}^{r_2-1} x_{j_1, j_2} W_{r_2}^{j_2 k_2} W_N^{j_2 k_1} \right]$$

where $W_{r_1} = e^{2\pi i/r_1}$ and $W_{r_2} = e^{2\pi i/r_2}$.

The computation proceeds in three steps:

1. For each $j_1$, compute the $r_2$ transforms over $j_2$ of length $r_2$, multiplying each term by $W_N^{j_2 k_1}$ (called "twiddle factors").

2. Multiply the resulting array by the twiddle factors $W_N^{j_2 k_1}$.

3. For each $k_2$, compute the $r_1$ transforms over $j_1$ of length $r_1$.

This method can be generalized to any number of factors. If $N = r_1 r_2 \cdots r_m$, the computation can be done with $m$ passes through the data, each involving transforms of smaller size.

---

### النسخة العربية

لنفترض أن $N = r_1 r_2$، ولنعتبر النقاط $N$ من $x_j$ كمصفوفة ذات فهرسة مزدوجة $x_{j_1, j_2}$ حيث

$$j = r_2 j_1 + j_2, \quad j_1 = 0, 1, \ldots, r_1 - 1, \quad j_2 = 0, 1, \ldots, r_2 - 1$$

بالمثل، لنفترض

$$k = r_1 k_2 + k_1, \quad k_1 = 0, 1, \ldots, r_1 - 1, \quad k_2 = 0, 1, \ldots, r_2 - 1$$

عندئذ تصبح متسلسلة فورييه

$$X_{k_1, k_2} = \sum_{j_1=0}^{r_1-1} \sum_{j_2=0}^{r_2-1} x_{j_1, j_2} W_N^{(r_2 j_1 + j_2)(r_1 k_2 + k_1)}$$

حيث $W_N = e^{2\pi i/N}$.

يمكن إعادة كتابة الأس على النحو التالي

$$(r_2 j_1 + j_2)(r_1 k_2 + k_1) = r_1 r_2 j_1 k_2 + r_2 j_1 k_1 + r_1 j_2 k_2 + j_2 k_1$$

بما أن $W_N^{r_1 r_2} = W_N^N = 1$، لدينا

$$X_{k_1, k_2} = \sum_{j_1=0}^{r_1-1} \sum_{j_2=0}^{r_2-1} x_{j_1, j_2} W_N^{r_2 j_1 k_1} W_N^{r_1 j_2 k_2} W_N^{j_2 k_1}$$

يمكن كتابة هذا على النحو التالي

$$X_{k_1, k_2} = \sum_{j_1=0}^{r_1-1} W_{r_1}^{j_1 k_1} \left[ \sum_{j_2=0}^{r_2-1} x_{j_1, j_2} W_{r_2}^{j_2 k_2} W_N^{j_2 k_1} \right]$$

حيث $W_{r_1} = e^{2\pi i/r_1}$ و $W_{r_2} = e^{2\pi i/r_2}$.

يتم الحساب في ثلاث خطوات:

1. لكل $j_1$، احسب التحويلات $r_2$ على $j_2$ بطول $r_2$، مع ضرب كل حد بـ $W_N^{j_2 k_1}$ (تسمى "عوامل الدوران").

2. اضرب المصفوفة الناتجة بعوامل الدوران $W_N^{j_2 k_1}$.

3. لكل $k_2$، احسب التحويلات $r_1$ على $j_1$ بطول $r_1$.

يمكن تعميم هذه الطريقة على أي عدد من العوامل. إذا كان $N = r_1 r_2 \cdots r_m$، يمكن إجراء الحساب مع $m$ تمريرة عبر البيانات، تتضمن كل منها تحويلات بحجم أصغر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** twiddle factors, double indexing, multi-pass computation, factored transforms
- **Equations:** 7 major equations showing the mathematical derivation
- **Citations:** None in this section
- **Special handling:** Extensive mathematical notation preserved; introduced technical term "عوامل الدوران" for "twiddle factors"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.87
