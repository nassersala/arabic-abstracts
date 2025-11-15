# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** statistical learning, privacy, data, utility, differential privacy, algorithm, random projection, matrix, Gaussian, compression, database, principal component analysis, covariance, regression, sparse, high-dimensional, synthetic data, transformation

---

### English Version

In statistical learning, privacy is increasingly a concern whenever large amounts of confidential data are manipulated within or published outside an organization. It is often important to allow researchers to analyze data utility without leaking information or compromising the privacy of individual records. In this work, we demonstrate that one can preserve utility for a variety of statistical applications while achieving a formal definition of privacy. The algorithm we study is a simple random projection by a matrix of independent Gaussian random variables that compresses the number of records in the database. Our goal is to preserve the privacy of every individual in the database, even if the number of records in the database is very large. In particular, we show how this randomized procedure can achieve a form of "differential privacy" [7], while at the same time showing that the compressed data can be used for Principal Component Analysis (PCA) and other operations that rely on the accuracy of the empirical covariance matrix computed via the compressed data, compared to its population or the uncompressed correspondents. Toward this goal, we also study "distributional privacy" which is more natural for many statistical inference tasks.

More specifically, the data are represented as a n × p matrix X. Each of the p columns is an attribute, and each of the n rows is the vector of attributes for an individual record. The data are compressed by a random linear transformation X 7→ X̄ ≡ ΦX, where Φ is a random m × n matrix with m ≪ n. It is also natural to consider a random affine transformation X 7→ X̄ ≡ ΦX +Δ, where Δ is a random m× p matrix, as considered in [23] for privacy analysis, the latter of which is beyond the scope of this paper and intended as future work. Such transformations have been called "matrix masking" in the privacy literature [6]. The entries of Φ are taken to be independent Gaussian random variables, but other distributions are possible. The resulting compressed data can then be made available for statistical analyses; that is, we think of X̄ as "public," while Φ and Δ are private and only needed at the time of compression. However, even if Φ were revealed, recovering X from X̄ requires solving a highly underdetermined linear system and comes with information theoretic privacy guarantees, as demonstrated in [23].

Informally, differential privacy [7] limits the increase in the information that can be learned when any single entry is changed in the database. This limit implies [16] that allowing one's data to be included in the database is in some sense incentive-compatible. Differential privacy imposes a compelling and clear requirement, that when running a privacy-preserving algorithm on two neighboring databases that differ in only one entry, the probability of any possible outcome of the algorithm should be nearly (multiplicatively) equal. Many existing results in differential privacy use additive output perturbations by adding a small amount of random noise to the released information according to the sensitivity of the query function f on data X. In this work, we focus on a class F of Lipschitz functions that are bounded, up to a constant L, by the differences between two covariance matrices, (for example, for Σ = X^T X/n and its compressed realization Σ' = X̄^T Φ^T ΦX̄/m given Φ),

F(L) = {f : |f(A) − f(D)| ≤ L ‖A − D‖},                    (1)

where A, D are positive definite matrices and ‖·‖ is understood to be any matrix norm (for example, PCA depends on ‖Σ − Σ'‖_F). Hence we focus on releasing a multiplicative form of perturbation of the input data, such that for a particular type of functions as in (1), we achieve both utility and privacy. Due to the space limits, we only explore PCA in this paper.

We emphasize that although one could potentially release a version of the covariance matrix to preserve data privacy while performing PCA and functions as in (1), releasing the compressed data ΦX is more informative than releasing the perturbed covariance matrix (or other summaries) alone. For example, Zhou et al. [23] demonstrated the utility of this random linear transformation by analyzing the asymptotic properties of a statistical estimator under random projection in the high dimensional setting for n ≪ p. They showed that the relevant linear predictors can be learned from the compressed data almost as well as they could be from the original uncompressed data. Moreover, the actual predictions based on new examples are almost as accurate as they would be had the original data been made available. Finally, it is possible to release the compressed data plus some other features of the data to yield more information, although this is beyond the scope of the current paper. We note that in order to guarantee differential privacy, p < n is required.

In the context of guarding privacy over a set of databases S_n = {X_1, X_2, ...}, where Σ_j = X_j^T X_j/n, ∀X_j, we introduce an additional parameter in our privacy definition, Δ_max(S_n), which is an upper bound on pairwise distances between any two databases X_1, X_2 ∈ S_n (differing in any number of rows), according to a certain distance measure. In some sense, this parametrized approach of tuning the magnitude of the distance measure Δ_max(S_n) is the key idea we elaborate in Section 3.

---

### النسخة العربية

في التعلم الإحصائي، أصبحت الخصوصية مصدر قلق متزايد كلما تم التعامل مع كميات كبيرة من البيانات السرية داخل المؤسسة أو نشرها خارجها. غالبًا ما يكون من المهم السماح للباحثين بتحليل فائدة البيانات دون تسريب المعلومات أو المساس بخصوصية السجلات الفردية. في هذا العمل، نثبت أنه يمكن للمرء الحفاظ على الفائدة لمجموعة متنوعة من التطبيقات الإحصائية مع تحقيق تعريف رسمي للخصوصية. الخوارزمية التي ندرسها هي إسقاط عشوائي بسيط بواسطة مصفوفة من المتغيرات العشوائية الغاوسية المستقلة التي تضغط عدد السجلات في قاعدة البيانات. هدفنا هو الحفاظ على خصوصية كل فرد في قاعدة البيانات، حتى لو كان عدد السجلات في قاعدة البيانات كبيرًا جدًا. على وجه الخصوص، نوضح كيف يمكن لهذا الإجراء العشوائي تحقيق شكل من أشكال "الخصوصية التفاضلية" [7]، بينما نوضح في نفس الوقت أن البيانات المضغوطة يمكن استخدامها لتحليل المكونات الأساسية (PCA) والعمليات الأخرى التي تعتمد على دقة مصفوفة التباين المشترك التجريبية المحسوبة عبر البيانات المضغوطة، مقارنة بنظيراتها السكانية أو غير المضغوطة. لتحقيق هذا الهدف، ندرس أيضًا "الخصوصية التوزيعية" التي تكون أكثر طبيعية للعديد من مهام الاستدلال الإحصائي.

بشكل أكثر تحديدًا، يتم تمثيل البيانات كمصفوفة n × p وهي X. كل عمود من الأعمدة p هو سمة، وكل صف من الصفوف n هو متجه السمات لسجل فردي. يتم ضغط البيانات عن طريق تحويل خطي عشوائي X 7→ X̄ ≡ ΦX، حيث Φ هي مصفوفة عشوائية m × n مع m ≪ n. من الطبيعي أيضًا النظر في تحويل أفيني عشوائي X 7→ X̄ ≡ ΦX + Δ، حيث Δ هي مصفوفة عشوائية m × p، كما هو مدروس في [23] لتحليل الخصوصية، والأخير يتجاوز نطاق هذه الورقة ويُقصد به كعمل مستقبلي. تُسمى مثل هذه التحويلات "إخفاء المصفوفة" في أدبيات الخصوصية [6]. تُؤخذ عناصر Φ لتكون متغيرات عشوائية غاوسية مستقلة، ولكن التوزيعات الأخرى ممكنة. يمكن بعد ذلك إتاحة البيانات المضغوطة الناتجة للتحليلات الإحصائية؛ أي أننا نعتبر X̄ "عامة"، بينما Φ و Δ خاصة ومطلوبة فقط في وقت الضغط. ومع ذلك، حتى لو تم الكشف عن Φ، فإن استرداد X من X̄ يتطلب حل نظام خطي غير محدد بشكل كبير ويأتي مع ضمانات خصوصية نظرية معلوماتية، كما هو موضح في [23].

بشكل غير رسمي، تحد الخصوصية التفاضلية [7] من الزيادة في المعلومات التي يمكن تعلمها عند تغيير أي إدخال واحد في قاعدة البيانات. يعني هذا الحد [16] أن السماح بتضمين بيانات المرء في قاعدة البيانات متوافق مع الحوافز بمعنى ما. تفرض الخصوصية التفاضلية متطلبًا مقنعًا وواضحًا، وهو أنه عند تشغيل خوارزمية للحفاظ على الخصوصية على قاعدتي بيانات متجاورتين تختلفان في إدخال واحد فقط، يجب أن يكون احتمال أي نتيجة محتملة للخوارزمية متساويًا تقريبًا (بشكل ضربي). تستخدم العديد من النتائج الموجودة في الخصوصية التفاضلية اضطرابات مخرجات إضافية عن طريق إضافة كمية صغيرة من الضوضاء العشوائية إلى المعلومات المنشورة وفقًا لحساسية دالة الاستعلام f على البيانات X. في هذا العمل، نركز على فئة F من دوال ليبشتز المحدودة، حتى ثابت L، بالفروق بين مصفوفتي تباين مشترك، (على سبيل المثال، لـ Σ = X^T X/n وتحقيقها المضغوط Σ' = X̄^T Φ^T ΦX̄/m بالنظر إلى Φ)،

F(L) = {f : |f(A) − f(D)| ≤ L ‖A − D‖},                    (1)

حيث A و D هما مصفوفتان محددتان موجبتان و ‖·‖ يُفهم أنه أي معيار مصفوفة (على سبيل المثال، يعتمد PCA على ‖Σ − Σ'‖_F). وبالتالي فإننا نركز على إطلاق شكل ضربي من اضطراب بيانات الإدخال، بحيث لنوع معين من الدوال كما في (1)، نحقق كلاً من الفائدة والخصوصية. نظرًا لقيود المساحة، نستكشف فقط PCA في هذه الورقة.

نؤكد أنه على الرغم من أنه يمكن للمرء نشر نسخة من مصفوفة التباين المشترك للحفاظ على خصوصية البيانات مع أداء PCA والدوال كما في (1)، فإن إطلاق البيانات المضغوطة ΦX أكثر إفادة من إطلاق مصفوفة التباين المشترك المضطربة (أو ملخصات أخرى) وحدها. على سبيل المثال، أظهر Zhou et al. [23] فائدة هذا التحويل الخطي العشوائي من خلال تحليل الخصائص المقاربة لمقدر إحصائي في ظل الإسقاط العشوائي في الإعداد عالي الأبعاد لـ n ≪ p. أظهروا أن المتنبئات الخطية ذات الصلة يمكن تعلمها من البيانات المضغوطة تقريبًا بنفس جودة ما يمكن تعلمها من البيانات الأصلية غير المضغوطة. علاوة على ذلك، فإن التنبؤات الفعلية بناءً على أمثلة جديدة دقيقة تقريبًا كما لو كانت البيانات الأصلية متاحة. أخيرًا، من الممكن إطلاق البيانات المضغوطة بالإضافة إلى بعض الميزات الأخرى للبيانات لإنتاج مزيد من المعلومات، على الرغم من أن هذا يتجاوز نطاق الورقة الحالية. نلاحظ أنه من أجل ضمان الخصوصية التفاضلية، يُطلب p < n.

في سياق حماية الخصوصية على مجموعة من قواعد البيانات S_n = {X_1, X_2, ...}، حيث Σ_j = X_j^T X_j/n، ∀X_j، نقدم معاملاً إضافيًا في تعريف الخصوصية لدينا، Δ_max(S_n)، وهو حد أعلى على المسافات الزوجية بين أي قاعدتي بيانات X_1، X_2 ∈ S_n (تختلفان في أي عدد من الصفوف)، وفقًا لمقياس مسافة معين. بمعنى ما، فإن هذا النهج البارامتري لضبط حجم مقياس المسافة Δ_max(S_n) هو الفكرة الأساسية التي نشرحها في القسم 3.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** privacy-preserving, random projection, matrix masking, distributional privacy, neighboring databases, query sensitivity, Lipschitz functions, parametrized privacy
- **Equations:** 1 (equation for F(L))
- **Citations:** 5 references cited ([7], [16], [6], [23])
- **Special handling:** Mathematical notation preserved in LaTeX format

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.90
- **Overall section score:** 0.88
