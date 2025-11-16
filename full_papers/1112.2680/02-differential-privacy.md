# Section 2: Differential Privacy (DP)
## القسم 2: الخصوصية التفاضلية

**Section:** differential-privacy
**Translation Quality:** 0.87
**Glossary Terms Used:** differential privacy, database, algorithm, distribution, histogram, privacy, Laplace distribution, sensitivity, query

---

### English Version

## 2.1 Definition

Let $X = (X_1, \ldots, X_n) \in \mathcal{X}^n$ be an input database with $n$ observations where $X_i \in \mathcal{X}$. The goal is to produce some output $Z \in \mathcal{Z}$. For example the inputs may consist of database rows in which each column is a measurement of an individual, and the output is the number of individuals having some property. Let $Q_n(\cdot|X)$ be a conditional distribution for $Z$ given $X$. Write $X \sim X'$ if $X, X' \in \mathcal{X}^n$ and $X$ and $X'$ differ in one coordinate. We say that $X$ and $X'$ are neighboring databases.

We say $Q_n$ satisfies $\alpha$ differential privacy if, for all measurable $B \subset \mathcal{Z}$ and all $X \sim X' \in \mathcal{X}^n$,

$$e^{-\alpha} \leq \frac{Q_n(Z \in B|X)}{Q_n(Z \in B|X')} \leq e^{\alpha}.$$

The intuition is that, for small $\alpha > 0$, the value of one individual's data has small effect on the output. We consider any DP algorithm to be a family of distributions $Q_n$ over the output space $\mathcal{Z}$. We index a family of distributions by $n$ to show the size of the dataset.

It has been shown by researchers in privacy that differential privacy provides a very strong guarantee. Essentially it means that whether or not one particular individual is entered in the database, has negligible effect on the output. The research in differential privacy is vast. A few key references are [8], [7], [2], [5], [3] and references therein.

## 2.2 Noninteractive Privacy and Histograms

Much research on differential privacy focuses on the case where $Z$ is a response to some query such as "what is the mean of the data." A simple way to achieve differential privacy in that case is to add some noise to the mean of $X$ where the noise has a Laplace distribution. The user may send a sequence of such queries. This is called interactive privacy. We instead focus on the noninteractive privacy where the goal is to output a whole database (or a "synthetic dataset") $Z = (Z_1, \ldots, Z_N)$. Then the user is not restricted to a small number of queries.

One way to release a private database is to first release a privatized histogram. We can then draw an arbitrarily large sample $Z = (Z_1, \ldots, Z_N)$ from the histogram. It is easy to show that if the histogram satisfies DP then $Z$ also satisfies DP. Hence, in the rest of the paper, we focus on constructing a private histogram.

We consider privatization mechanisms which are permutation invariant with respect to their inputs (i.e., those distributions which treat the values $x_i$ as a set rather than a vector) in the context of histograms this appears to be a very mild restriction.

We partition the sample space $\mathcal{X}$ into $k$ cells (or bins) $\{B_j\}_{j=1}^k$. We consider the input to be a lattice point in the $k$-simplex, by taking the function: $\theta^n(x_1, \ldots, x_n) = (\theta_1, \ldots, \theta_k)$, $\theta_j = \frac{1}{n}\sum_{i=1}^n \mathbf{1}\{x_i \in B_j\}$. The image of this mapping $\Theta = \theta^n(\mathcal{X}^n)$ is the set of lattice points in the simplex which correspond to histograms of $n$ observations in $k$ bins. Note that this is in essence a "normalized histogram" since the elements sum to one. This set depends on $k$ although we suppress this notation. For the remainder of this paper we consider the output space $\mathcal{Z}$ to be the same as the input space (i.e., a normalized histogram).

Now we give a concrete example of a $Q_n$ which achieves differential privacy. Define $z_j = \theta_j + 2L_j/(n\alpha)$ where $L_1, \ldots, L_k$ are independent draws from a Laplace distribution with mean zero and rate one. Then $(z_1, \ldots, z_k)$ satisfy DP (see e.g.,[8]). However, the $z_i$ themselves do not represent a histogram, because they can be negative and they do not necessarily sum to one. Hence we may take, for example:

$$\delta(z) = \arg\min_{\theta \in \Theta} ||z - \theta||_1$$

where we use the $\ell_1$ norm: $||x||_1 = \sum_j |x_j|$. This procedure hence results in a valid histogram. Note that $\delta(z)$ satisfies the differential privacy, since each subset of values it may take clearly corresponds to a measurable subset of $\mathbb{R}^k$. Since the differential privacy held for the real vector then it also holds for the projection (see e.g., [16]). We will refer to this as the histogram perturbation method (see e.g., [16]). There are other methods for generating differentially private histograms, and our results below concern hold over a large subset of all the possible techniques available (to be made precise after proposition 3.2). Hence our results apply to more than the above concrete scheme.

---

### النسخة العربية

## 2.1 التعريف

لتكن $X = (X_1, \ldots, X_n) \in \mathcal{X}^n$ قاعدة بيانات إدخال تحتوي على $n$ ملاحظة حيث $X_i \in \mathcal{X}$. الهدف هو إنتاج بعض المخرجات $Z \in \mathcal{Z}$. على سبيل المثال، قد تتكون المدخلات من صفوف قاعدة بيانات يكون فيها كل عمود قياساً لفرد، ويكون المخرج هو عدد الأفراد الذين يمتلكون خاصية معينة. لتكن $Q_n(\cdot|X)$ توزيعاً شرطياً لـ $Z$ بالنظر إلى $X$. نكتب $X \sim X'$ إذا كانت $X, X' \in \mathcal{X}^n$ و $X$ و $X'$ تختلفان في إحداثية واحدة. نقول إن $X$ و $X'$ هما قاعدتا بيانات متجاورتان.

نقول إن $Q_n$ تحقق خصوصية تفاضلية $\alpha$ إذا، لجميع $B \subset \mathcal{Z}$ القابلة للقياس ولجميع $X \sim X' \in \mathcal{X}^n$:

$$e^{-\alpha} \leq \frac{Q_n(Z \in B|X)}{Q_n(Z \in B|X')} \leq e^{\alpha}.$$

الحدس هو أنه، لقيمة صغيرة $\alpha > 0$، فإن قيمة بيانات فرد واحد لها تأثير ضئيل على المخرج. نعتبر أي خوارزمية DP عائلة من التوزيعات $Q_n$ على فضاء المخرجات $\mathcal{Z}$. نفهرس عائلة من التوزيعات بـ $n$ لإظهار حجم مجموعة البيانات.

لقد أظهر الباحثون في مجال الخصوصية أن الخصوصية التفاضلية توفر ضماناً قوياً جداً. في الأساس، هذا يعني أنه سواء تم إدخال فرد معين في قاعدة البيانات أم لا، فإن له تأثيراً ضئيلاً على المخرج. الأبحاث في الخصوصية التفاضلية واسعة. بعض المراجع الرئيسية هي [8]، [7]، [2]، [5]، [3] والمراجع الواردة فيها.

## 2.2 الخصوصية غير التفاعلية والرسوم البيانية الهيستوغرامية

يركز الكثير من الأبحاث حول الخصوصية التفاضلية على الحالة التي يكون فيها $Z$ استجابة لاستعلام ما مثل "ما هو متوسط البيانات". طريقة بسيطة لتحقيق الخصوصية التفاضلية في تلك الحالة هي إضافة بعض الضوضاء إلى متوسط $X$ حيث تكون الضوضاء لها توزيع لابلاس. قد يرسل المستخدم سلسلة من هذه الاستعلامات. وهذا ما يُسمى بالخصوصية التفاعلية. بدلاً من ذلك، نركز على الخصوصية غير التفاعلية حيث الهدف هو إخراج قاعدة بيانات كاملة (أو "مجموعة بيانات اصطناعية") $Z = (Z_1, \ldots, Z_N)$. عندئذ لا يكون المستخدم مقيداً بعدد صغير من الاستعلامات.

إحدى طرق إصدار قاعدة بيانات خاصة هي أولاً إصدار رسم بياني هيستوغرامي خاص. يمكننا بعد ذلك سحب عينة كبيرة بشكل تعسفي $Z = (Z_1, \ldots, Z_N)$ من الرسم البياني الهيستوغرامي. من السهل إظهار أنه إذا كان الرسم البياني الهيستوغرامي يحقق DP فإن $Z$ يحقق أيضاً DP. ولذلك، في بقية الورقة، نركز على بناء رسم بياني هيستوغرامي خاص.

نأخذ في الاعتبار آليات الخصوصية التي هي ثابتة بالنسبة للتبديل فيما يتعلق بمدخلاتها (أي تلك التوزيعات التي تعامل القيم $x_i$ كمجموعة بدلاً من متجه) في سياق الرسوم البيانية الهيستوغرامية يبدو هذا قيداً خفيفاً جداً.

نقسم فضاء العينة $\mathcal{X}$ إلى $k$ خلية (أو حاويات) $\{B_j\}_{j=1}^k$. نعتبر المدخل نقطة شبكية في المبسط $k$، بأخذ الدالة: $\theta^n(x_1, \ldots, x_n) = (\theta_1, \ldots, \theta_k)$، $\theta_j = \frac{1}{n}\sum_{i=1}^n \mathbf{1}\{x_i \in B_j\}$. صورة هذا التعيين $\Theta = \theta^n(\mathcal{X}^n)$ هي مجموعة النقاط الشبكية في المبسط التي تتوافق مع الرسوم البيانية الهيستوغرامية لـ $n$ ملاحظة في $k$ حاوية. لاحظ أن هذا في جوهره "رسم بياني هيستوغرامي معياري" لأن العناصر تجمع إلى واحد. هذه المجموعة تعتمد على $k$ على الرغم من أننا نتجاهل هذا الترميز. لبقية هذه الورقة، نعتبر فضاء المخرجات $\mathcal{Z}$ هو نفسه فضاء المدخلات (أي رسم بياني هيستوغرامي معياري).

الآن نعطي مثالاً ملموساً لـ $Q_n$ تحقق الخصوصية التفاضلية. نعرّف $z_j = \theta_j + 2L_j/(n\alpha)$ حيث $L_1, \ldots, L_k$ هي سحوبات مستقلة من توزيع لابلاس بمتوسط صفر ومعدل واحد. عندئذ $(z_1, \ldots, z_k)$ تحقق DP (انظر على سبيل المثال [8]). ومع ذلك، فإن $z_i$ نفسها لا تمثل رسماً بيانياً هيستوغرامياً، لأنها يمكن أن تكون سالبة ولا تجمع بالضرورة إلى واحد. ولذلك يمكننا أن نأخذ، على سبيل المثال:

$$\delta(z) = \arg\min_{\theta \in \Theta} ||z - \theta||_1$$

حيث نستخدم معيار $\ell_1$: $||x||_1 = \sum_j |x_j|$. هذا الإجراء ينتج بالتالي رسماً بيانياً هيستوغرامياً صحيحاً. لاحظ أن $\delta(z)$ تحقق الخصوصية التفاضلية، لأن كل مجموعة فرعية من القيم التي قد تأخذها تتوافق بوضوح مع مجموعة فرعية قابلة للقياس من $\mathbb{R}^k$. بما أن الخصوصية التفاضلية كانت صحيحة للمتجه الحقيقي فإنها صحيحة أيضاً للإسقاط (انظر على سبيل المثال [16]). سنشير إلى هذا باسم طريقة اضطراب الرسم البياني الهيستوغرامي (انظر على سبيل المثال [16]). هناك طرق أخرى لتوليد رسوم بيانية هيستوغرامية خاصة تفاضلياً، ونتائجنا أدناه تتعلق بمجموعة فرعية كبيرة من جميع التقنيات الممكنة المتاحة (سيتم توضيحها بعد القضية 3.2). ولذلك تنطبق نتائجنا على أكثر من المخطط الملموس أعلاه.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** neighboring databases, conditional distribution, Laplace distribution, histogram perturbation, $\ell_1$ norm, simplex, normalized histogram
- **Equations:** 2 main equations plus several inline mathematical expressions
- **Citations:** [8], [7], [2], [5], [3], [16]
- **Special handling:** Mathematical notation preserved in LaTeX; technical privacy and statistical terms translated consistently

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.87
