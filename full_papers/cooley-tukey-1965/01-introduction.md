# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** algorithm, computation, operation, matrix, vector, data point, Fourier series, complexity, efficient

---

### English Version

The electronic computer has greatly increased our ability to do computations. This has led to the investigation of methods by which one can replace large sums by procedures which are more efficient in terms of the number of operations involved.

One problem of this sort is the calculation of the values of a finite Fourier series

$$X_k = \sum_{j=0}^{N-1} x_j e^{2\pi ijk/N}, \quad k = 0, 1, \ldots, N-1$$

from given values $x_0, x_1, \ldots, x_{N-1}$. This requires $N^2$ complex multiplications and $N(N-1)$ complex additions.

I. J. Good [1, 2] has described a method (a modification of Danielson and Lanczos [3]) which reduces the number of operations considerably. Good's method is applicable to certain problems in which one must multiply an $N$-vector by an $N \times N$ matrix which can be factored into $m$ sparse matrices, where $m$ is proportional to $\log N$. This results in a procedure requiring a number of operations proportional to $N \log N$ rather than $N^2$.

The purpose of this paper is to present such a method for the calculation of complex Fourier series. The method is especially useful when the number of data points is, or can be chosen to be, a highly composite number, that is, a number with many factors.

---

### النسخة العربية

لقد زاد الحاسوب الإلكتروني بشكل كبير من قدرتنا على إجراء الحسابات. وقد أدى ذلك إلى البحث في طرق يمكن من خلالها استبدال المجاميع الكبيرة بإجراءات أكثر كفاءة من حيث عدد العمليات المطلوبة.

إحدى المسائل من هذا النوع هي حساب قيم متسلسلة فورييه المنتهية

$$X_k = \sum_{j=0}^{N-1} x_j e^{2\pi ijk/N}, \quad k = 0, 1, \ldots, N-1$$

من قيم معطاة $x_0, x_1, \ldots, x_{N-1}$. يتطلب هذا $N^2$ عملية ضرب مركبة و $N(N-1)$ عملية جمع مركبة.

وصف آي. جيه. غود [1، 2] طريقة (تعديل لطريقة دانيلسون ولانكزوس [3]) تقلل من عدد العمليات بشكل كبير. طريقة غود قابلة للتطبيق على مسائل معينة يجب فيها ضرب متجه من الرتبة $N$ بمصفوفة بحجم $N \times N$ يمكن تحليلها إلى $m$ مصفوفة متفرقة، حيث $m$ يتناسب مع $\log N$. ينتج عن هذا إجراء يتطلب عددًا من العمليات يتناسب مع $N \log N$ بدلاً من $N^2$.

الغرض من هذه الورقة هو تقديم مثل هذه الطريقة لحساب متسلسلات فورييه المركبة. الطريقة مفيدة بشكل خاص عندما يكون عدد نقاط البيانات، أو يمكن اختياره ليكون، عددًا مركبًا بدرجة عالية، أي عددًا له عوامل كثيرة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Fourier series, complex multiplication, sparse matrices, highly composite number, computational efficiency
- **Equations:** 1 (finite Fourier series formula)
- **Citations:** References to Good [1, 2] and Danielson & Lanczos [3]
- **Special handling:** Mathematical notation preserved in LaTeX format

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
