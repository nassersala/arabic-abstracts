# Section 3: Split Finding Algorithms
## القسم 3: خوارزميات إيجاد الانقسام

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** algorithm, greedy algorithm, approximation, quantile, sparse data, sparsity-aware, weighted quantile sketch, distributed computing, bucket, histogram

---

### English Version

#### 3.1 Basic Exact Greedy Algorithm

**Algorithm 1: Exact Greedy Algorithm for Split Finding**
- Input: $I$, instance set of current node
- Input: $d$, feature dimension
- $gain\leftarrow 0$
- $G \leftarrow \sum_{i\in I} g_{i}$, $H \leftarrow \sum_{i \in I} h_{i}$
- For $k=1$ to $m$:
  - $G_L\leftarrow 0,\ H_L\leftarrow 0$
  - For $j$ in sorted($I$, by $\x_{jk}$):
    - $G_L\leftarrow G_L + g_j,\ H_L\leftarrow H_L + h_j$
    - $G_R\leftarrow G - G_L,\ H_R\leftarrow H - H_L$
    - $score \leftarrow \max(score, \frac{G_{L}^2}{H_{L}+\lambda} + \frac{G_{R}^2}{H_{R}+\lambda} - \frac{G^2}{H+\lambda})$
- Output: Split with max score

One of the key problems in tree learning is to find the best split as indicated by Eq (6). In order to do so, a split finding algorithm enumerates over all the possible splits on all the features. We call this the exact greedy algorithm. Most existing single machine tree boosting implementations, such as scikit-learn, R's gbm as well as the single machine version of XGBoost support the exact greedy algorithm. The exact greedy algorithm is shown in Algorithm 1. It is computationally demanding to enumerate all the possible splits for continuous features. In order to do so efficiently, the algorithm must first sort the data according to feature values and visit the data in sorted order to accumulate the gradient statistics for the structure score in Eq (6).

#### 3.2 Approximate Algorithm

**Algorithm 2: Approximate Algorithm for Split Finding**
- For $k=1$ to $m$:
  - Propose $S_k = \{s_{k1}, s_{k2}, \cdots s_{kl}\}$ by percentiles on feature $k$.
  - Proposal can be done per tree (global), or per split (local).
- For $k=1$ to $m$:
  - $G_{kv} \leftarrow = \sum_{j\in \{j| s_{k, v}\geq \x_{jk} > s_{k, v-1}\}} g_j$
  - $H_{kv} \leftarrow = \sum_{j\in \{j| s_{k, v}\geq \x_{jk} > s_{k, v-1}\}} h_j$
- Follow same step as in previous section to find max score only among proposed splits.

The exact greedy algorithm is very powerful since it enumerates over all possible splitting points greedily. However, it is impossible to efficiently do so when the data does not fit entirely into memory. Same problem also arises in the distributed setting. To support effective gradient tree boosting in these two settings, an approximate algorithm is needed.

We summarize an approximate framework, which resembles the ideas proposed in past literatures, in Algorithm 2. To summarize, the algorithm first proposes candidate splitting points according to percentiles of feature distribution (a specific criteria will be given in Section 3.3). The algorithm then maps the continuous features into buckets split by these candidate points, aggregates the statistics and finds the best solution among proposals based on the aggregated statistics.

**Figure 3:** Comparison of test AUC convergence on Higgs 10M dataset. The eps parameter corresponds to the accuracy of the approximate sketch. This roughly translates to 1/eps buckets in the proposal. We find that local proposals require fewer buckets, because it refine split candidates.

There are two variants of the algorithm, depending on when the proposal is given. The global variant proposes all the candidate splits during the initial phase of tree construction, and uses the same proposals for split finding at all levels. The local variant re-proposes after each split. The global method requires less proposal steps than the local method. However, usually more candidate points are needed for the global proposal because candidates are not refined after each split. The local proposal refines the candidates after splits, and can potentially be more appropriate for deeper trees. A comparison of different algorithms on a Higgs boson dataset is given by Figure 3. We find that the local proposal indeed requires fewer candidates. The global proposal can be as accurate as the local one given enough candidates.

Most existing approximate algorithms for distributed tree learning also follow this framework. Notably, it is also possible to directly construct approximate histograms of gradient statistics. It is also possible to use other variants of binning strategies instead of quantile. Quantile strategy benefit from being distributable and recomputable, which we will detail in next subsection. From Figure 3, we also find that the quantile strategy can get the same accuracy as exact greedy given reasonable approximation level.

Our system efficiently supports exact greedy for the single machine setting, as well as approximate algorithm with both local and global proposal methods for all settings. Users can freely choose between the methods according to their needs.

#### 3.3 Weighted Quantile Sketch

One important step in the approximate algorithm is to propose candidate split points. Usually percentiles of a feature are used to make candidates distribute evenly on the data. Formally, let multi-set $\sD_k=\{(x_{1k}, h_1), (x_{2k}, h_2) \cdots (x_{nk}, h_n)\}$ represent the $k$-th feature values and second order gradient statistics of each training instances. We can define a rank functions $r_{k} : \mathbb{R} \rightarrow \Rplus$ as

$$r_{k}(z) =\frac{1}{\sum_{(x, h)\in \sD_k} h} \sum_{(x, h)\in \sD_k, x < z} h,$$

which represents the proportion of instances whose feature value $k$ is smaller than $z$. The goal is to find candidate split points $\{s_{k1}, s_{k2}, \cdots s_{kl}\}$, such that

$$|r_{k}(s_{k,j})  - r_{k}(s_{k,j+1})| < \eps, \ \ s_{k1} = \min_i \x_{ik},  s_{kl} = \max_i \x_{ik}.$$

Here $\eps$ is an approximation factor. Intuitively, this means that there is roughly $1 / \eps$ candidate points. Here each data point is weighted by $h_i$. To see why $h_i$ represents the weight, we can rewrite Eq (3) as

$$\sum_{i=1}^n \frac{1}{2} h_i (f_t(\x_i) - g_i / h_i )^2 + \Omega(f_t) + constant,$$

which is exactly weighted squared loss with labels $g_i/h_i$ and weights $h_i$. For large datasets, it is non-trivial to find candidate splits that satisfy the criteria. When every instance has equal weights, an existing algorithm called quantile sketch solves the problem. However, there is no existing quantile sketch for the weighted datasets. Therefore, most existing approximate algorithms either resorted to sorting on a random subset of data which have a chance of failure or heuristics that do not have theoretical guarantee.

To solve this problem, we introduced a novel distributed weighted quantile sketch algorithm that can handle weighted data with a provable theoretical guarantee. The general idea is to propose a data structure that supports merge and prune operations, with each operation proven to maintain a certain accuracy level. A detailed description of the algorithm as well as proofs are given in the appendix.

#### 3.4 Sparsity-aware Split Finding

**Algorithm 3: Sparsity-aware Split Finding**
- Input: $I$, instance set of current node
- Input: $I_k =\{i\in I|x_{ik} \neq \mbox{missing}\}$
- Input: $d$, feature dimension
- Also applies to the approximate setting, only collect statistics of non-missing entries into buckets
- $gain\leftarrow 0$
- $G \leftarrow \sum_{i\in I},  g_{i}$,$H \leftarrow \sum_{i \in I} h_{i}$
- For $k=1$ to $m$:
  - // enumerate missing value goto right
  - $G_L\leftarrow 0,\ H_L\leftarrow 0$
  - For $j$ in sorted($I_k$, ascent order by $\x_{jk}$):
    - $G_L\leftarrow G_L + g_j,\ H_L\leftarrow H_L + h_j$
    - $G_R\leftarrow G - G_L,\ H_R\leftarrow H - H_L$
    - $score \leftarrow \max(score, \frac{G_{L}^2}{H_{L}+\lambda} + \frac{G_{R}^2}{H_{R}+\lambda} - \frac{G^2}{H+\lambda})$
  - // enumerate missing value goto left
  - $G_R\leftarrow 0,\ H_R\leftarrow 0$
  - For $j$ in sorted($I_k$, descent order by $\x_{jk}$):
    - $G_R\leftarrow G_R + g_j,\ H_R\leftarrow H_R + h_j$
    - $G_L\leftarrow G - G_R,\ H_L\leftarrow H - H_R$
    - $score \leftarrow \max(score, \frac{G_{L}^2}{H_{L}+\lambda} + \frac{G_{R}^2}{H_{R}+\lambda} - \frac{G^2}{H+\lambda})$
- Output: Split and default directions with max gain

**Figure 4:** Tree structure with default directions. An example will be classified into the default direction when the feature needed for the split is missing.

**Figure 5:** Impact of the sparsity aware algorithm on Allstate-10K. The dataset is sparse mainly due to one-hot encoding. The sparsity aware algorithm is more than 50 times faster than the naive version that does not take sparsity into consideration.

In many real-world problems, it is quite common for the input $\x$ to be sparse. There are multiple possible causes for sparsity: 1) presence of missing values in the data; 2) frequent zero entries in the statistics; and, 3) artifacts of feature engineering such as one-hot encoding. It is important to make the algorithm aware of the sparsity pattern in the data. In order to do so, we propose to add a default direction in each tree node, which is shown in Figure 4. When a value is missing in the sparse matrix $\x$, the instance is classified into the default direction. There are two choices of default direction in each branch. The optimal default directions are learnt from the data. The algorithm is shown in Algorithm 3. The key improvement is to only visit the non-missing entries $I_k$. The presented algorithm treats the non-presence as a missing value and learns the best direction to handle missing values. The same algorithm can also be applied when the non-presence corresponds to a user specified value by limiting the enumeration only to consistent solutions.

To the best of our knowledge, most existing tree learning algorithms are either only optimized for dense data, or need specific procedures to handle limited cases such as categorical encoding. XGBoost handles all sparsity patterns in a unified way. More importantly, our method exploits the sparsity to make computation complexity linear to number of non-missing entries in the input. Figure 5 shows the comparison of sparsity aware and a naive implementation on an Allstate-10K dataset (description of dataset given in Section 6). We find that the sparsity aware algorithm runs 50 times faster than the naive version. This confirms the importance of the sparsity aware algorithm.

**Figure 6:** Block structure for parallel learning. Each column in a block is sorted by the corresponding feature value. A linear scan over one column in the block is sufficient to enumerate all the split points.

**Figure 7:** Impact of cache-aware prefetching in exact greedy algorithm. We find that the cache-miss effect impacts the performance on the large datasets (10 million instances). Using cache aware prefetching improves the performance by factor of two when the dataset is large.

---

### النسخة العربية

#### 3.1 خوارزمية جشعة دقيقة أساسية

**الخوارزمية 1: خوارزمية جشعة دقيقة لإيجاد الانقسام**
- المدخلات: $I$، مجموعة الحالات للعقدة الحالية
- المدخلات: $d$، بُعد الميزات
- $gain\leftarrow 0$
- $G \leftarrow \sum_{i\in I} g_{i}$، $H \leftarrow \sum_{i \in I} h_{i}$
- لكل $k=1$ إلى $m$:
  - $G_L\leftarrow 0,\ H_L\leftarrow 0$
  - لكل $j$ في sorted($I$، حسب $\x_{jk}$):
    - $G_L\leftarrow G_L + g_j,\ H_L\leftarrow H_L + h_j$
    - $G_R\leftarrow G - G_L,\ H_R\leftarrow H - H_L$
    - $score \leftarrow \max(score, \frac{G_{L}^2}{H_{L}+\lambda} + \frac{G_{R}^2}{H_{R}+\lambda} - \frac{G^2}{H+\lambda})$
- المخرجات: الانقسام بأعلى درجة

واحدة من المشاكل الرئيسية في تعلم الأشجار هي إيجاد أفضل انقسام كما هو موضح في المعادلة (6). للقيام بذلك، تقوم خوارزمية إيجاد الانقسام بتعداد جميع الانقسامات الممكنة على جميع الميزات. نسمي هذه الخوارزمية الجشعة الدقيقة. معظم تطبيقات تعزيز الأشجار الموجودة على الأجهزة الفردية، مثل scikit-learn وgbm في R وكذلك نسخة الجهاز الواحد من XGBoost تدعم الخوارزمية الجشعة الدقيقة. تظهر الخوارزمية الجشعة الدقيقة في الخوارزمية 1. من المكلف حسابياً تعداد جميع الانقسامات الممكنة للميزات المستمرة. للقيام بذلك بكفاءة، يجب على الخوارزمية أولاً فرز البيانات وفقاً لقيم الميزات وزيارة البيانات بترتيب مفروز لتجميع إحصائيات التدرج لدرجة البنية في المعادلة (6).

#### 3.2 خوارزمية تقريبية

**الخوارزمية 2: خوارزمية تقريبية لإيجاد الانقسام**
- لكل $k=1$ إلى $m$:
  - اقترح $S_k = \{s_{k1}, s_{k2}, \cdots s_{kl}\}$ بواسطة النسب المئوية على الميزة $k$.
  - يمكن إجراء الاقتراح لكل شجرة (عام)، أو لكل انقسام (محلي).
- لكل $k=1$ إلى $m$:
  - $G_{kv} \leftarrow = \sum_{j\in \{j| s_{k, v}\geq \x_{jk} > s_{k, v-1}\}} g_j$
  - $H_{kv} \leftarrow = \sum_{j\in \{j| s_{k, v}\geq \x_{jk} > s_{k, v-1}\}} h_j$
- اتبع نفس الخطوة كما في القسم السابق لإيجاد أقصى درجة فقط بين الانقسامات المقترحة.

الخوارزمية الجشعة الدقيقة قوية جداً لأنها تعدد جميع نقاط الانقسام الممكنة بشكل جشع. ومع ذلك، من المستحيل القيام بذلك بكفاءة عندما لا تتناسب البيانات بالكامل في الذاكرة. تظهر نفس المشكلة أيضاً في الإعداد الموزع. لدعم تعزيز الأشجار بالتدرج الفعال في هذين الإعدادين، تحتاج خوارزمية تقريبية.

نلخص إطاراً تقريبياً، يشبه الأفكار المقترحة في الأدبيات السابقة، في الخوارزمية 2. باختصار، تقترح الخوارزمية أولاً نقاط انقسام مرشحة وفقاً للنسب المئوية لتوزيع الميزات (سيتم إعطاء معيار محدد في القسم 3.3). ثم تقوم الخوارزمية بتعيين الميزات المستمرة في دلاء (Buckets) مقسمة بواسطة نقاط المرشحين هذه، وتجميع الإحصائيات وإيجاد أفضل حل بين المقترحات بناءً على الإحصائيات المجمعة.

**الشكل 3:** مقارنة تقارب AUC للاختبار على مجموعة بيانات Higgs 10M. يتوافق معامل eps مع دقة الرسم التقريبي. هذا يُترجم تقريباً إلى 1/eps دلاء في الاقتراح. نجد أن الاقتراحات المحلية تتطلب دلاء أقل، لأنها تنقح مرشحي الانقسام.

هناك نوعان من الخوارزمية، اعتماداً على وقت تقديم الاقتراح. يقترح النوع العام جميع انقسامات المرشحين خلال المرحلة الأولية لبناء الشجرة، ويستخدم نفس المقترحات لإيجاد الانقسام على جميع المستويات. يعيد النوع المحلي الاقتراح بعد كل انقسام. تتطلب الطريقة العامة خطوات اقتراح أقل من الطريقة المحلية. ومع ذلك، عادةً ما تكون هناك حاجة إلى نقاط مرشحة أكثر للاقتراح العام لأن المرشحين لا يتم تنقيحهم بعد كل انقسام. يُنقح الاقتراح المحلي المرشحين بعد الانقسامات، ويمكن أن يكون أكثر ملاءمة للأشجار الأعمق. تُعطى مقارنة خوارزميات مختلفة على مجموعة بيانات Higgs boson في الشكل 3. نجد أن الاقتراح المحلي يتطلب فعلاً مرشحين أقل. يمكن أن يكون الاقتراح العام دقيقاً مثل المحلي بإعطاء مرشحين كافيين.

تتبع معظم الخوارزميات التقريبية الموجودة لتعلم الأشجار الموزعة هذا الإطار أيضاً. والجدير بالذكر أنه من الممكن أيضاً بناء رسوم بيانية هيستوغرامية تقريبية مباشرة لإحصائيات التدرج. من الممكن أيضاً استخدام متغيرات أخرى من استراتيجيات التجميع بدلاً من الكمية. تستفيد استراتيجية الكمية من كونها قابلة للتوزيع وإعادة الحساب، والتي سنفصلها في القسم الفرعي التالي. من الشكل 3، نجد أيضاً أن استراتيجية الكمية يمكن أن تحصل على نفس دقة الجشع الدقيق بمستوى تقريب معقول.

يدعم نظامنا بكفاءة الجشع الدقيق لإعداد الجهاز الواحد، وكذلك الخوارزمية التقريبية بكل من طرق الاقتراح المحلية والعامة لجميع الإعدادات. يمكن للمستخدمين الاختيار بحرية بين الطرق وفقاً لاحتياجاتهم.

#### 3.3 رسم تقريبي للكميات الموزونة

خطوة مهمة واحدة في الخوارزمية التقريبية هي اقتراح نقاط الانقسام المرشحة. عادةً ما تُستخدم النسب المئوية للميزة لجعل المرشحين يتوزعون بالتساوي على البيانات. رسمياً، دع المجموعة المتعددة $\sD_k=\{(x_{1k}, h_1), (x_{2k}, h_2) \cdots (x_{nk}, h_n)\}$ تمثل قيم الميزة $k$ وإحصائيات التدرج من الرتبة الثانية لكل حالة تدريب. يمكننا تعريف دالة رتبة $r_{k} : \mathbb{R} \rightarrow \Rplus$ كـ

$$r_{k}(z) =\frac{1}{\sum_{(x, h)\in \sD_k} h} \sum_{(x, h)\in \sD_k, x < z} h,$$

والتي تمثل نسبة الحالات التي قيمة ميزتها $k$ أصغر من $z$. الهدف هو إيجاد نقاط الانقسام المرشحة $\{s_{k1}, s_{k2}, \cdots s_{kl}\}$، بحيث

$$|r_{k}(s_{k,j})  - r_{k}(s_{k,j+1})| < \eps, \ \ s_{k1} = \min_i \x_{ik},  s_{kl} = \max_i \x_{ik}.$$

هنا $\eps$ هو عامل التقريب. بشكل بديهي، هذا يعني أن هناك تقريباً $1 / \eps$ نقطة مرشحة. هنا كل نقطة بيانات موزونة بـ $h_i$. لنرى لماذا يمثل $h_i$ الوزن، يمكننا إعادة كتابة المعادلة (3) كـ

$$\sum_{i=1}^n \frac{1}{2} h_i (f_t(\x_i) - g_i / h_i )^2 + \Omega(f_t) + constant,$$

وهو بالضبط خسارة مربعة موزونة مع تسميات $g_i/h_i$ وأوزان $h_i$. بالنسبة لمجموعات البيانات الكبيرة، ليس من التافه إيجاد انقسامات مرشحة تستوفي المعايير. عندما يكون لكل حالة أوزان متساوية، تحل خوارزمية موجودة تسمى رسم تقريبي للكميات (Quantile Sketch) المشكلة. ومع ذلك، لا يوجد رسم تقريبي للكميات موجود لمجموعات البيانات الموزونة. لذلك، لجأت معظم الخوارزميات التقريبية الموجودة إما إلى الفرز على مجموعة فرعية عشوائية من البيانات التي لها فرصة للفشل أو إلى استدلالات ليس لها ضمان نظري.

لحل هذه المشكلة، قدمنا خوارزمية رسم تقريبي للكميات الموزونة الموزعة جديدة يمكنها التعامل مع البيانات الموزونة بضمان نظري قابل للإثبات. الفكرة العامة هي اقتراح بنية بيانات تدعم عمليات الدمج (Merge) والتقليم (Prune)، مع إثبات أن كل عملية تحافظ على مستوى دقة معين. يُعطى وصف مفصل للخوارزمية وكذلك البراهين في الملحق.

#### 3.4 إيجاد انقسام مدرك للتناثر

**الخوارزمية 3: إيجاد انقسام مدرك للتناثر**
- المدخلات: $I$، مجموعة الحالات للعقدة الحالية
- المدخلات: $I_k =\{i\in I|x_{ik} \neq \mbox{مفقود}\}$
- المدخلات: $d$، بُعد الميزات
- ينطبق أيضاً على الإعداد التقريبي، اجمع فقط إحصائيات المدخلات غير المفقودة في الدلاء
- $gain\leftarrow 0$
- $G \leftarrow \sum_{i\in I},  g_{i}$، $H \leftarrow \sum_{i \in I} h_{i}$
- لكل $k=1$ إلى $m$:
  - // تعداد القيمة المفقودة اذهب إلى اليمين
  - $G_L\leftarrow 0,\ H_L\leftarrow 0$
  - لكل $j$ في sorted($I_k$، ترتيب تصاعدي حسب $\x_{jk}$):
    - $G_L\leftarrow G_L + g_j,\ H_L\leftarrow H_L + h_j$
    - $G_R\leftarrow G - G_L,\ H_R\leftarrow H - H_L$
    - $score \leftarrow \max(score, \frac{G_{L}^2}{H_{L}+\lambda} + \frac{G_{R}^2}{H_{R}+\lambda} - \frac{G^2}{H+\lambda})$
  - // تعداد القيمة المفقودة اذهب إلى اليسار
  - $G_R\leftarrow 0,\ H_R\leftarrow 0$
  - لكل $j$ في sorted($I_k$، ترتيب تنازلي حسب $\x_{jk}$):
    - $G_R\leftarrow G_R + g_j,\ H_R\leftarrow H_R + h_j$
    - $G_L\leftarrow G - G_R,\ H_L\leftarrow H - H_R$
    - $score \leftarrow \max(score, \frac{G_{L}^2}{H_{L}+\lambda} + \frac{G_{R}^2}{H_{R}+\lambda} - \frac{G^2}{H+\lambda})$
- المخرجات: الانقسام والاتجاهات الافتراضية بأعلى كسب

**الشكل 4:** بنية الشجرة مع الاتجاهات الافتراضية. سيتم تصنيف مثال في الاتجاه الافتراضي عندما تكون الميزة المطلوبة للانقسام مفقودة.

**الشكل 5:** تأثير الخوارزمية المدركة للتناثر على Allstate-10K. مجموعة البيانات متناثرة بشكل رئيسي بسبب الترميز الأحادي الساخن (One-hot encoding). الخوارزمية المدركة للتناثر أسرع بأكثر من 50 مرة من النسخة الساذجة التي لا تأخذ التناثر في الاعتبار.

في العديد من المشاكل الواقعية، من الشائع جداً أن يكون المدخل $\x$ متناثراً. هناك أسباب محتملة متعددة للتناثر: 1) وجود قيم مفقودة في البيانات؛ 2) مدخلات صفرية متكررة في الإحصائيات؛ و 3) منتجات هندسة الميزات مثل الترميز الأحادي الساخن. من المهم جعل الخوارزمية مدركة لنمط التناثر في البيانات. للقيام بذلك، نقترح إضافة اتجاه افتراضي في كل عقدة شجرة، والذي يظهر في الشكل 4. عندما تكون قيمة مفقودة في المصفوفة المتناثرة $\x$، يتم تصنيف الحالة في الاتجاه الافتراضي. هناك خياران للاتجاه الافتراضي في كل فرع. يتم تعلم الاتجاهات الافتراضية المثلى من البيانات. تظهر الخوارزمية في الخوارزمية 3. التحسين الرئيسي هو زيارة المدخلات غير المفقودة $I_k$ فقط. تتعامل الخوارزمية المقدمة مع عدم الوجود كقيمة مفقودة وتتعلم أفضل اتجاه للتعامل مع القيم المفقودة. يمكن أيضاً تطبيق نفس الخوارزمية عندما يتوافق عدم الوجود مع قيمة محددة من قبل المستخدم عن طريق تحديد التعداد فقط للحلول المتسقة.

على حد علمنا، معظم خوارزميات تعلم الأشجار الموجودة إما محسّنة فقط للبيانات الكثيفة، أو تحتاج إلى إجراءات محددة للتعامل مع حالات محدودة مثل الترميز الفئوي. يتعامل XGBoost مع جميع أنماط التناثر بطريقة موحدة. والأهم من ذلك، تستغل طريقتنا التناثر لجعل تعقيد الحساب خطياً لعدد المدخلات غير المفقودة في المدخل. يُظهر الشكل 5 مقارنة التطبيق المدرك للتناثر والتطبيق الساذج على مجموعة بيانات Allstate-10K (وصف مجموعة البيانات موجود في القسم 6). نجد أن الخوارزمية المدركة للتناثر تعمل بسرعة 50 مرة أسرع من النسخة الساذجة. هذا يؤكد أهمية الخوارزمية المدركة للتناثر.

**الشكل 6:** بنية الكتلة للتعلم المتوازي. كل عمود في كتلة مفروز حسب قيمة الميزة المقابلة. المسح الخطي على عمود واحد في الكتلة كافٍ لتعداد جميع نقاط الانقسام.

**الشكل 7:** تأثير الجلب المسبق المدرك لذاكرة التخزين المؤقت في الخوارزمية الجشعة الدقيقة. نجد أن تأثير فقدان ذاكرة التخزين المؤقت يؤثر على الأداء على مجموعات البيانات الكبيرة (10 ملايين حالة). استخدام الجلب المسبق المدرك لذاكرة التخزين المؤقت يحسن الأداء بعامل اثنين عندما تكون مجموعة البيانات كبيرة.

---

### Translation Notes

- **Algorithms:** 3 algorithms translated with pseudocode structure preserved
- **Figures referenced:** Figures 3-7 (various experimental comparisons and system architecture)
- **Key terms introduced:**
  - Exact Greedy Algorithm (خوارزمية جشعة دقيقة)
  - Approximate Algorithm (خوارزمية تقريبية)
  - Quantile Sketch (رسم تقريبي للكميات)
  - Weighted Quantile Sketch (رسم تقريبي للكميات الموزونة)
  - Sparsity-aware (مدرك للتناثر)
  - Default Direction (اتجاه افتراضي)
  - Bucket (دلو)
  - One-hot Encoding (الترميز الأحادي الساخن)
  - Cache-aware (مدرك لذاكرة التخزين المؤقت)
  - Prefetching (الجلب المسبق)

- **Equations:** 3 mathematical equations preserved
- **Citations:** References to scikit-learn, R's gbm, various research papers

- **Special handling:**
  - Algorithm pseudocode translated while maintaining structure
  - Comments in algorithms (// ...) translated
  - "For...to" loops translated as "لكل...إلى"
  - Input/Output declarations translated
  - Mathematical notation and variables preserved
  - "Merge" and "Prune" operations kept with Arabic translation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- Algorithm clarity: 0.86
- **Overall section score:** 0.87

### Back-Translation Check

**Key algorithm description:**
"One of the main problems in tree learning is finding the best split as shown in Equation (6). To do this, the split finding algorithm enumerates all possible splits on all features. We call this the exact greedy algorithm."

**Sparsity handling:**
"In many real-world problems, it is very common for input $\x$ to be sparse. There are multiple potential causes for sparsity: 1) presence of missing values in data; 2) frequent zero entries in statistics; and 3) feature engineering products like one-hot encoding."

✅ Back-translations maintain technical precision and algorithmic clarity.
