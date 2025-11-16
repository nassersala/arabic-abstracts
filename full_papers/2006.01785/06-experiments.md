# Section 6: Experiments
## القسم 6: التجارب

**Section:** experiments/evaluation
**Translation Quality:** 0.87
**Glossary Terms Used:** benchmark, dataset, training, validation, RMSE, hyperparameter

---

### English Version

For the feasibility study, we carried out a number of experiments using the ESOL and FreeSolv datasets, which are used in [5-6] for training and evaluating 3D-extended GCNs. In particular, we used the dataset files provided by Geo-GCN [6], which contain molecular graph data including three-dimensional node coordinates. These are small datasets with 901 / 113 / 113 and 510 / 65 / 64 training / test / validation samples, respectively. Our focus, however, is on qualitatively comparing results of geometric graph convolutions with those of standard graph convolutions, all based on the same sample sizes. That is, our interest is on relative accuracy not absolute accuracy.

The results are listed in the following table. Standard GC (graph convolutions) utilizes the default GCNConv with all edges having a weight of one, discussed in Section 5.1, and serves as the baseline for comparison. Geometric GC utilizes the GCNConv with edge weights calculated from edge distances, discussed in Section 5.3.

Geometric GC (Ref) denotes the reference geometric GC which uses fixed R0 = 1.39 and N = 4.55 (i.e., 1/0.22), discussed in Sections 2.1. This applies to all three cases of geometric graph convolutions: edges (1st Nbrs) which include first-neighbor nodes, edges + angle edges (2nd Nbrs) which include first- and second-neighbor nodes, and edges + angle edges + dihedral edges (3rd Nbrs) which include first-, second- and third-neighbor nodes.

Geometric GC (BHO) represents the geometric GC which uses the best (R0, N)'s obtained through Bayesian hyperparameter optimization, discussed in Section 5.4. We adopted the following ranges for the hyperparameters: R0 (in Å) and N in the range of 1.0 to 3.0 and 2.0 to 6.0, respectively, as discussed in Section 2.1; R^θ_0 (in Å) and Nθ in the range of 1.0 to 3.0 (discussed in Section 3.1) and 2.0 to 6.0, respectively; R^φ_0 (in Å) and Nφ in the range of 1.0 to 4.0 (discussed in Section 3.1) and 2.0 to 6.0, respectively. For the study, we employed 40 trials and, for each trial, 50 epochs. This applies to all three cases of geometric graph convolutions: edges (1st Nbrs), edges + angle edges (2nd Nbrs), and edges + angle edges + dihedral edges (3rd Nbrs).

We include the 1st Nbrs and 2nd Nbrs cases to verify and show the consistency of Geometric GC results. The (full) geometric graph convolutions are represented by the 3rd Nbrs cases.

**Table: Experimental Results**

| Dataset  | Model                   | R0 (Å) | N      | R^θ_0 (Å) | N^θ    | R^φ_0 (Å) | N^φ    | RMSE   |
|----------|-------------------------|--------|--------|-----------|--------|-----------|--------|--------|
| ESOL     | Standard GC             | -      | -      | -         | -      | -         | -      | 0.4573 |
|          | Geometric GC (Ref) – 1st Nbrs | 1.39   | 4.55   | -         | -      | -         | -      | 0.4283 |
|          | Geometric GC (BHO) – 1st Nbrs | 1.0    | 2.6447 | -         | -      | -         | -      | 0.4163 |
|          | Geometric GC (Ref) – 2nd Nbrs | 1.39   | 4.55   | 1.39      | 4.55   | -         | -      | 0.4275 |
|          | Geometric GC (BHO) – 2nd Nbrs | 3.0    | 4.7603 | 1.4402    | 3.7508 | -         | -      | 0.4214 |
|          | Geometric GC (Ref) – 3rd Nbrs | 1.39   | 4.55   | 1.39      | 4.55   | 1.39      | 4.55   | 0.4273 |
|          | Geometric GC (BHO) – 3rd Nbrs | 1.3385 | 4.2756 | 1.6828    | 5.4836 | 1.8408    | 6.0    | 0.4261 |
| FreeSolv | Standard GC             | -      | -      | -         | -      | -         | -      | 0.4183 |
|          | Geometric GC (Ref) – 1st Nbrs | 1.39   | 4.55   | -         | -      | -         | -      | 0.3706 |
|          | Geometric GC (BHO) – 1st Nbrs | 1.5783 | 4.9247 | -         | -      | -         | -      | 0.3753 |
|          | Geometric GC (Ref) – 2nd Nbrs | 1.39   | 4.55   | 1.39      | 4.55   | -         | -      | 0.3711 |
|          | Geometric GC (BHO) – 2nd Nbrs | 2.6367 | 3.3691 | 1.5782    | 3.000  | -         | -      | 0.3745 |
|          | Geometric GC (Ref) – 3rd Nbrs | 1.39   | 4.55   | 1.39      | 4.55   | 1.39      | 4.55   | 0.3710 |
|          | Geometric GC (BHO) – 3rd Nbrs | 1.5146 | 3.8488 | 2.5738    | 3.3665 | 3.1133    | 2.4705 | 0.3764 |

It can be seen from the table, for both the ESOL and FreeSolv datasets, the results of Geometric GC show significant improvement over those of Standard GC. They demonstrate the importance of incorporating geometry, using the distance-geometric graph representation, in deep learning on 3D graphs.

---

### النسخة العربية

لدراسة الجدوى، أجرينا عدداً من التجارب باستخدام مجموعات بيانات ESOL و FreeSolv، والتي تُستخدم في [5-6] للتدريب والتقييم لشبكات GCN الممتدة ثلاثية الأبعاد. على وجه الخصوص، استخدمنا ملفات مجموعة البيانات المقدمة من Geo-GCN [6]، والتي تحتوي على بيانات الرسوم البيانية الجزيئية بما في ذلك الإحداثيات ثلاثية الأبعاد للعقد. هذه مجموعات بيانات صغيرة تحتوي على 901 / 113 / 113 و 510 / 65 / 64 عينة تدريب / اختبار / تحقق، على التوالي. ومع ذلك، فإن تركيزنا على المقارنة النوعية لنتائج التفافات الرسوم البيانية الهندسية مع نتائج التفافات الرسوم البيانية القياسية، جميعها بناءً على نفس أحجام العينات. أي أن اهتمامنا بالدقة النسبية وليس الدقة المطلقة.

النتائج مدرجة في الجدول التالي. التفافات الرسوم البيانية القياسية (Standard GC) تستخدم GCNConv الافتراضي مع جميع الحواف التي لها وزن واحد، كما تمت مناقشته في القسم 5.1، وتعمل كخط أساس للمقارنة. التفافات الرسوم البيانية الهندسية (Geometric GC) تستخدم GCNConv مع أوزان الحواف المحسوبة من مسافات الحواف، كما تمت مناقشته في القسم 5.3.

التفافات الرسوم البيانية الهندسية المرجعية (Geometric GC (Ref)) تشير إلى التفافات الرسوم البيانية الهندسية المرجعية التي تستخدم R0 = 1.39 و N = 4.55 الثابتين (أي 1/0.22)، كما تمت مناقشته في القسم 2.1. ينطبق هذا على جميع الحالات الثلاث لالتفافات الرسوم البيانية الهندسية: الحواف (1st Nbrs) التي تتضمن عقد الجوار الأولى، والحواف + حواف الزوايا (2nd Nbrs) التي تتضمن عقد الجوار الأولى والثانية، والحواف + حواف الزوايا + حواف الزوايا الثنائية السطحية (3rd Nbrs) التي تتضمن عقد الجوار الأولى والثانية والثالثة.

التفافات الرسوم البيانية الهندسية بالتحسين البايزي (Geometric GC (BHO)) تمثل التفافات الرسوم البيانية الهندسية التي تستخدم أفضل (R0، N) التي تم الحصول عليها من خلال التحسين البايزي للمعاملات الفائقة، كما تمت مناقشته في القسم 5.4. اعتمدنا النطاقات التالية للمعاملات الفائقة: R0 (بالـ Å) و N في نطاق 1.0 إلى 3.0 و 2.0 إلى 6.0، على التوالي، كما تمت مناقشته في القسم 2.1؛ R^θ_0 (بالـ Å) و Nθ في نطاق 1.0 إلى 3.0 (تمت مناقشته في القسم 3.1) و 2.0 إلى 6.0، على التوالي؛ R^φ_0 (بالـ Å) و Nφ في نطاق 1.0 إلى 4.0 (تمت مناقشته في القسم 3.1) و 2.0 إلى 6.0، على التوالي. للدراسة، استخدمنا 40 محاولة، ولكل محاولة، 50 حقبة. ينطبق هذا على جميع الحالات الثلاث لالتفافات الرسوم البيانية الهندسية: الحواف (1st Nbrs)، والحواف + حواف الزوايا (2nd Nbrs)، والحواف + حواف الزوايا + حواف الزوايا الثنائية السطحية (3rd Nbrs).

نضمّن حالات 1st Nbrs و 2nd Nbrs للتحقق من وإظهار اتساق نتائج التفافات الرسوم البيانية الهندسية. يتم تمثيل التفافات الرسوم البيانية الهندسية (الكاملة) بحالات 3rd Nbrs.

**جدول: نتائج التجارب**

| مجموعة البيانات | النموذج | R0 (Å) | N | R^θ_0 (Å) | N^θ | R^φ_0 (Å) | N^φ | RMSE |
|-----------------|---------|--------|---|-----------|-----|-----------|-----|------|
| ESOL | التفافات رسوم بيانية قياسية | - | - | - | - | - | - | 0.4573 |
| | التفافات رسوم بيانية هندسية (مرجعية) – 1st Nbrs | 1.39 | 4.55 | - | - | - | - | 0.4283 |
| | التفافات رسوم بيانية هندسية (تحسين بايزي) – 1st Nbrs | 1.0 | 2.6447 | - | - | - | - | 0.4163 |
| | التفافات رسوم بيانية هندسية (مرجعية) – 2nd Nbrs | 1.39 | 4.55 | 1.39 | 4.55 | - | - | 0.4275 |
| | التفافات رسوم بيانية هندسية (تحسين بايزي) – 2nd Nbrs | 3.0 | 4.7603 | 1.4402 | 3.7508 | - | - | 0.4214 |
| | التفافات رسوم بيانية هندسية (مرجعية) – 3rd Nbrs | 1.39 | 4.55 | 1.39 | 4.55 | 1.39 | 4.55 | 0.4273 |
| | التفافات رسوم بيانية هندسية (تحسين بايزي) – 3rd Nbrs | 1.3385 | 4.2756 | 1.6828 | 5.4836 | 1.8408 | 6.0 | 0.4261 |
| FreeSolv | التفافات رسوم بيانية قياسية | - | - | - | - | - | - | 0.4183 |
| | التفافات رسوم بيانية هندسية (مرجعية) – 1st Nbrs | 1.39 | 4.55 | - | - | - | - | 0.3706 |
| | التفافات رسوم بيانية هندسية (تحسين بايزي) – 1st Nbrs | 1.5783 | 4.9247 | - | - | - | - | 0.3753 |
| | التفافات رسوم بيانية هندسية (مرجعية) – 2nd Nbrs | 1.39 | 4.55 | 1.39 | 4.55 | - | - | 0.3711 |
| | التفافات رسوم بيانية هندسية (تحسين بايزي) – 2nd Nbrs | 2.6367 | 3.3691 | 1.5782 | 3.000 | - | - | 0.3745 |
| | التفافات رسوم بيانية هندسية (مرجعية) – 3rd Nbrs | 1.39 | 4.55 | 1.39 | 4.55 | 1.39 | 4.55 | 0.3710 |
| | التفافات رسوم بيانية هندسية (تحسين بايزي) – 3rd Nbrs | 1.5146 | 3.8488 | 2.5738 | 3.3665 | 3.1133 | 2.4705 | 0.3764 |

يمكن ملاحظة من الجدول، لكل من مجموعات بيانات ESOL و FreeSolv، أن نتائج التفافات الرسوم البيانية الهندسية تظهر تحسيناً كبيراً مقارنة بنتائج التفافات الرسوم البيانية القياسية. تُظهر أهمية دمج الهندسة، باستخدام التمثيل الهندسي المسافي للرسم البياني، في التعلم العميق على الرسوم البيانية ثلاثية الأبعاد.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** feasibility study, ESOL dataset, FreeSolv dataset, Geo-GCN, baseline, 1st/2nd/3rd neighbors
- **Equations:** 0
- **Citations:** [5-6], Sections 2.1, 3.1, 5.1, 5.3, 5.4
- **Special handling:** Large data table with experimental results, RMSE values, hyperparameter ranges

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
