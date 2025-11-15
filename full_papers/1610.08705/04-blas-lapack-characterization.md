# Section 4: BLAS and LAPACK Characterization
## القسم 4: توصيف BLAS و LAPACK

**Section:** blas-lapack-characterization
**Translation Quality:** 0.86
**Glossary Terms Used:** BLAS, LAPACK, linear algebra, matrix, vector, inner product, factorization, pipeline, floating point, optimization, directed acyclic graph

---

### English Version

Based on remarks in section 3 and theory presented in [9], and [10], we present detailed characterization of different routines in BLAS and LAPACK for determining several parameters that help us arriving at optimum pipeline depths of multiplier adder, square root and divider for these packages.

#### 4.1 Characterization of BLAS

For characterization of BLAS, we consider *inner product* (Level-1 BLAS), *matrix-vector multiplication* (Level-2 BLAS), and *general matrix-matrix multiplication* (Level-3 BLAS) as representative routines. These routines are known as `ddot`, `dgemv`, and `dgemm` respectively where 'd' is for double precision [22].

For vectors $x = [a_1\ a_2\ ...\ a_n]$, and $y = [b_1\ b_2\ ...\ b_n]$, inner product is given by

$$c = x^T y = [a_1\ a_2\ a_3\ a_4] \begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{bmatrix} \text{ for } n = 4$$
(8)

**Figure 5: 4-element Vector Inner Product**

Directed Acyclic Graph (DAG) for $n = 4$ is shown in figure 5. It can be observed in the figure 5 that all the multiplications in the inner product of 4-element vector can be performed in parallel. In general for $n$-element vector there are $n$ multiplications and all the multiplications can be executed in parallel. There are $n-1$ additions in the inner product, and there is a dependency from the output of the multiplier for the first level of the addition as shown in the figure 5 and there are dependencies in the addition for each next level from the additions in the previous level.

Considering, only dependency hazards, there will be no hazards in the multiplier pipeline. Associated parameters with multiplier, and adder pipelines shown in the figure 11 will be as follows:

$$N_I = N_I^M + N_I^A = n + n - 1 = 2n - 1$$

$$N_H^M = 0 \text{ (considering only dependency hazards)}$$

$$\gamma_M = \infty$$

Determining $\gamma_A$ is difficult as mentioned in [19]. Hence, we have to determine value of $\gamma_A$ through a theoretical curve shown in figure 6. It can be observed that for large value of $\gamma_A$, a sharp rise in TPI is observed. For small value of $\gamma_A$, the curve becomes almost flat. Near optimum value in the curve, it is considerably flat allowing designer multiple choices for the number of pipeline stages. For figure 6, we have considered $\frac{N_H}{N_I}$ = 0.1. Decreasing $\frac{N_H}{N_I}$ further gives a flat theoretical curve as observed in the figure 3. For multiplier, theoretical curve for TPI becomes a flat horizontal line as we increase the pipeline depth. This is mainly due to absence of dependency hazards in the multiplication.

**Figure 6: TPI for Different Pipeline Stages $p$ in Adder and $\gamma$ = 0.2, 0.4, 0.6, and 0.8 for 1000-Element Vector Inner Product**

**Figure 7: TPI for Different Pipeline Stages $p$ in Multiplier and $\gamma$ = 0.2, 0.4, 0.6, and 0.8 for 1000-Element Vector Inner Product**

**Figure 8: TPI for Different Pipeline Stages $p$ in Adder and $\frac{N_H}{N_I}$ = 0.01, 0.05, 0.15, 0.25, and 0.35**

For *matrix-vector*, and *matrix-matrix* multiplication,

$$y = Ax$$
(9)

$$C = AB$$
(10)

where $y$ and $x$ are vectors, and $A$, $B$, and $C$ are matrices. Since, *matrix-vector* multiplication, and *matrix-matrix* multiplication can be viewed as a series of calls of *inner products*, the optimum number of pipeline stages for these routines for adder and multiplier are expected to be the same as what we achieved for *inner product*. It is well established that, in practical implementations of *matrix-vector* multiplication (DGEMV in BLAS) and *matrix-matrix* multiplication (DGEMM in BLAS), due to compiler optimizations the dependency hazards reduce [23]. This reduction in the hazards will lead to increase in the $\gamma_A$ and decrease in the ratio $\frac{N_H}{N_I}$. In figure 8, TPI for different ratio of $\frac{N_H}{N_I}$ is shown. It can be observed in the figure 8 that as the ratio $\frac{N_H}{N_I}$ increases, the growth in TPI is sharper.

#### 4.2 Characterization of LAPACK

For LAPACK, we consider two most popular factorization routines namely DGEQRF (QR factorization), and DGETRF (LU factorization with partial pivoting) for characterization.

**Figure 9: QR and LU Factorizations**

For these factorizations, it can be observed in figure 9 that the *matrix-matrix* operations (DGEMM) are dominant, and hence the optimum number of pipeline stages for multiplier and adder would remain same as derived in section 4.1. It is important to arrive at an optimum pipeline depth of divider and square root shown in the figure 11 through characterization.

In QR factorization, division and square root operations are required in panel factorization and the order of division and square root operations is $O(n^2)$ while the total operations in the factorization are $O(n^3)$. There is always dependency in the square root operation that stalls the program execution. The ratios $\frac{N_H^D}{N_I^D}$, and $\frac{N_H^S}{N_I^S}$ are observed to be high in QR factorization. With varying pipeline and varying number of hazards in the square root pipeline $N_H^S$, the theoretical curve is shown in figure 10. For optimum number of stages in the divider, we expect trend that is similar to shown in the figure 10 since the number of dependency hazards in square root and divider are expected to be same in QR factorization.

**Figure 10: TPI for Different Pipeline Stages $p$ in Square root and $\frac{N_H^S}{N_I^S}$ = 0.01, 0.1, 0.2, 0.4, 0.6, and 0.8**

In LU factorization there are multiplications, additions, and divisions. Since the occurrence of division instruction in the program is similar to the square root/divider in the QR factorization, we expect similar trend for optimum pipeline stages for divider as shown in the figure 10.

---

### النسخة العربية

بناءً على الملاحظات في القسم 3 والنظرية المقدمة في [9] و[10]، نقدم توصيفاً تفصيلياً للبرامج المختلفة في BLAS و LAPACK لتحديد العديد من المعاملات التي تساعدنا في الوصول إلى أعماق خطوط أنابيب مثلى للمضارب والجامع والجذر التربيعي والمقسم لهذه الحزم.

#### 4.1 توصيف BLAS

لتوصيف BLAS، نعتبر *الضرب الداخلي* (BLAS من المستوى 1)، *ضرب المصفوفة بالمتجه* (BLAS من المستوى 2)، و*ضرب المصفوفة بالمصفوفة العام* (BLAS من المستوى 3) كبرامج تمثيلية. تُعرف هذه البرامج باسم `ddot` و `dgemv` و `dgemm` على التوالي حيث 'd' للدقة المزدوجة [22].

للمتجهات $x = [a_1\ a_2\ ...\ a_n]$ و $y = [b_1\ b_2\ ...\ b_n]$، يُعطى الضرب الداخلي بواسطة

$$c = x^T y = [a_1\ a_2\ a_3\ a_4] \begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{bmatrix} \text{ لـ } n = 4$$
(8)

**الشكل 5: الضرب الداخلي لمتجه من 4 عناصر**

يُظهر الرسم البياني غير الدوري الموجه (DAG) لـ $n = 4$ في الشكل 5. يمكن ملاحظة في الشكل 5 أن جميع عمليات الضرب في الضرب الداخلي لمتجه من 4 عناصر يمكن إجراؤها بشكل متوازٍ. بشكل عام لمتجه من $n$ عنصر هناك $n$ عملية ضرب ويمكن تنفيذ جميع عمليات الضرب بشكل متوازٍ. هناك $n-1$ عملية جمع في الضرب الداخلي، وهناك تبعية من مخرجات المضارب للمستوى الأول من الجمع كما هو موضح في الشكل 5 وهناك تبعيات في الجمع لكل مستوى تالٍ من عمليات الجمع في المستوى السابق.

مع اعتبار مخاطر التبعية فقط، لن تكون هناك مخاطر في خط أنابيب المضارب. ستكون المعاملات المرتبطة بخطوط أنابيب المضارب والجامع الموضحة في الشكل 11 كما يلي:

$$N_I = N_I^M + N_I^A = n + n - 1 = 2n - 1$$

$$N_H^M = 0 \text{ (مع اعتبار مخاطر التبعية فقط)}$$

$$\gamma_M = \infty$$

يصعب تحديد $\gamma_A$ كما ذُكر في [19]. لذلك، يجب علينا تحديد قيمة $\gamma_A$ من خلال منحنى نظري موضح في الشكل 6. يمكن ملاحظة أنه بالنسبة لقيمة كبيرة من $\gamma_A$، يُلاحظ ارتفاع حاد في TPI. بالنسبة لقيمة صغيرة من $\gamma_A$، يصبح المنحنى مسطحاً تقريباً. بالقرب من القيمة المثلى في المنحنى، يكون مسطحاً إلى حد كبير مما يسمح للمصمم بخيارات متعددة لعدد مراحل خط الأنابيب. للشكل 6، اعتبرنا $\frac{N_H}{N_I}$ = 0.1. يعطي تقليل $\frac{N_H}{N_I}$ بشكل أكبر منحنى نظرياً مسطحاً كما لوحظ في الشكل 3. بالنسبة للمضارب، يصبح المنحنى النظري لـ TPI خطاً أفقياً مسطحاً مع زيادة عمق خط الأنابيب. هذا يرجع بشكل أساسي إلى غياب مخاطر التبعية في الضرب.

**الشكل 6: TPI لمراحل خط أنابيب مختلفة $p$ في الجامع و $\gamma$ = 0.2 و 0.4 و 0.6 و 0.8 للضرب الداخلي لمتجه من 1000 عنصر**

**الشكل 7: TPI لمراحل خط أنابيب مختلفة $p$ في المضارب و $\gamma$ = 0.2 و 0.4 و 0.6 و 0.8 للضرب الداخلي لمتجه من 1000 عنصر**

**الشكل 8: TPI لمراحل خط أنابيب مختلفة $p$ في الجامع و $\frac{N_H}{N_I}$ = 0.01 و 0.05 و 0.15 و 0.25 و 0.35**

لـ *ضرب المصفوفة بالمتجه* و*ضرب المصفوفة بالمصفوفة*،

$$y = Ax$$
(9)

$$C = AB$$
(10)

حيث $y$ و $x$ متجهات، و $A$ و $B$ و $C$ مصفوفات. نظراً لأن *ضرب المصفوفة بالمتجه* و*ضرب المصفوفة بالمصفوفة* يمكن اعتبارهما سلسلة من استدعاءات *الضرب الداخلي*، فإن العدد الأمثل من مراحل خط الأنابيب لهذه البرامج للجامع والمضارب من المتوقع أن يكون نفس ما حققناه للضرب الداخلي. من الثابت جيداً أنه في التطبيقات العملية لـ *ضرب المصفوفة بالمتجه* (DGEMV في BLAS) و*ضرب المصفوفة بالمصفوفة* (DGEMM في BLAS)، بسبب تحسينات المترجم، تقل مخاطر التبعية [23]. سيؤدي هذا الانخفاض في المخاطر إلى زيادة في $\gamma_A$ وانخفاض في النسبة $\frac{N_H}{N_I}$. في الشكل 8، يُظهر TPI لنسب مختلفة من $\frac{N_H}{N_I}$. يمكن ملاحظة في الشكل 8 أنه مع زيادة النسبة $\frac{N_H}{N_I}$، يكون النمو في TPI أكثر حدة.

#### 4.2 توصيف LAPACK

بالنسبة لـ LAPACK، نعتبر برنامجين للتحليل الأكثر شيوعاً وهما DGEQRF (تحليل QR)، و DGETRF (تحليل LU مع محورية جزئية) للتوصيف.

**الشكل 9: تحليلات QR و LU**

لهذه التحليلات، يمكن ملاحظة في الشكل 9 أن عمليات *ضرب المصفوفة بالمصفوفة* (DGEMM) مهيمنة، وبالتالي فإن العدد الأمثل من مراحل خط الأنابيب للمضارب والجامع سيبقى نفسه كما استُمد في القسم 4.1. من المهم الوصول إلى عمق خط أنابيب أمثل للمقسم والجذر التربيعي الموضح في الشكل 11 من خلال التوصيف.

في تحليل QR، تكون عمليات القسمة والجذر التربيعي مطلوبة في تحليل اللوحة ورتبة عمليات القسمة والجذر التربيعي هي $O(n^2)$ بينما إجمالي العمليات في التحليل هي $O(n^3)$. هناك دائماً تبعية في عملية الجذر التربيعي التي توقف تنفيذ البرنامج. لوحظ أن النسب $\frac{N_H^D}{N_I^D}$ و $\frac{N_H^S}{N_I^S}$ عالية في تحليل QR. مع تغيير خط الأنابيب وتغيير عدد المخاطر في خط أنابيب الجذر التربيعي $N_H^S$، يُظهر المنحنى النظري في الشكل 10. بالنسبة للعدد الأمثل من المراحل في المقسم، نتوقع اتجاهاً مشابهاً لما هو موضح في الشكل 10 نظراً لأن عدد مخاطر التبعية في الجذر التربيعي والمقسم من المتوقع أن يكون نفسه في تحليل QR.

**الشكل 10: TPI لمراحل خط أنابيب مختلفة $p$ في الجذر التربيعي و $\frac{N_H^S}{N_I^S}$ = 0.01 و 0.1 و 0.2 و 0.4 و 0.6 و 0.8**

في تحليل LU هناك عمليات ضرب وجمع وقسمة. نظراً لأن حدوث تعليمة القسمة في البرنامج مشابه للجذر التربيعي/المقسم في تحليل QR، نتوقع اتجاهاً مشابهاً لمراحل خط الأنابيب المثلى للمقسم كما هو موضح في الشكل 10.

---

### Translation Notes

- **Figures referenced:** Figure 5 (4-element Vector Inner Product), Figure 6 (TPI for Adder stages), Figure 7 (TPI for Multiplier stages), Figure 8 (TPI for different hazard ratios), Figure 9 (QR and LU Factorizations), Figure 10 (TPI for Square root stages)
- **Key terms introduced:** inner product, matrix-vector multiplication, matrix-matrix multiplication, ddot, dgemv, dgemm, QR factorization, LU factorization, DGEQRF, DGETRF, panel factorization, DAG (Directed Acyclic Graph)
- **Equations:** 3 equations (equations 8, 9, 10) plus multiple inline mathematical expressions
- **Citations:** [19], [22], [23] referenced
- **Special handling:** BLAS routine names kept in English (ddot, dgemv, dgemm, DGEQRF, DGETRF); Mathematical notation preserved; Big-O notation maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
