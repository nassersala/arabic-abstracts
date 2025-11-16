# Section 5: Geometric Graph Convolutions
## القسم 5: التفافات الرسوم البيانية الهندسية

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** graph convolution, deep learning, hyperparameter, Bayesian optimization, neural network, training

---

### English Version

Geometric graph convolutions extend standard graph convolutions [4] by incorporating the 3D geometry of graphs in the graph convolution process. Standard graph convolutions do not take spatial arrangements of the nodes and edges into account. Therefore, they can accommodate only graph constitution, but not graph geometry.

Recently, there have been efforts to extend GCNs by incorporating 3D node coordinates in graph convolutions [5-6]. The proposed schemes, however, only consider adjacent nodes. They do not consider other nodes that are important to graph geometry. These include second-neighbor nodes which are part of the edges that form angles and third-neighbor nodes which are part of the edges that form dihedrals.

### 5.1 Graph Convolutional Networks (GCNs)

As in [1], we use graph neural networks (GNNs) that employ the following message passing scheme for node i at layer k:

$$x_i^{(k)} = \gamma^{(k)}(x_i^{(k-1)}, \Pi_{j} \lambda^{(k)}(x_i^{(k-1)}, x_j^{(k-1)}, e_{ij}))$$

where j ∈ N(i) denotes a neighbor node of node i. $x_i$ is the node feature vector and $e_{ij}$ is the edge feature vector. γ and λ denote differentiable functions and Π denotes a differentiable aggregation function.

Specifically, we use GCNs [4] which implement message passing using the adjacency matrix A:

$$X^{(k)} = \tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}X^{(k-1)}\Omega$$

where $\tilde{A} = A + I$ denotes the adjacency matrix with inserted self-loops and $\tilde{D}_{ii}=\sum_{j=0} \tilde{A}_{ij}$ its diagonal degree matrix. $A_{ij}$ is one when there is an edge from node i to node j, and zero when there is no edge. Thus, all edges have a weight of one.

A graph in PyG is described by an instance of the Data class, which has the following attributes: x (node feature matrix), edge_index (edge indices), edge_attr (edge feature matrix), pos (node position matrix) and y (target). The PyG implementation of GCN, GCNConv, employs the edge_weight vector in graph convolutions. However, in standard (default) graph convolutions, the edge_weight vector has values of one, i.e., all edges have a weight of one.

### 5.2 Geometric Graph Convolutions

For proof of concept, we use the distance-geometric graph representation for geometric graph convolutions. This representation is based on distances: edge distances (d), angle distances (dθ) and dihedral distances (dφ), as discussed in Section 4.3. Further, to utilize standard GCNs for geometric graph convolutions, we employ a simple edge weight / edge distance correlations scheme whose parameters can be fixed using reference values or determined using Bayesian hyperparameter optimization.

The combination of using the distance-geometric graph representation and employing an edge weight / edge distance correlations scheme enables us to incorporate the full geometry of 3D graphs in graph convolutions utilizing standard GCNs by (1) expanding the kinds of edges involved to include not just edges (e) with neighbor nodes, but also angle edges (eθ) with second-neighbor nodes and dihedral edges (eφ) with third-neighbor nodes and (2) assigning different weights to different edges based on their kind and their distance.

The first extension to standard GCNs means that in Section 5.1 we now have j ∈ N(i) + N^θ(i) + N^φ(i), with N(i) being the first neighbors, N^θ(i) the second neighbors and N^φ(i) the third neighbors, of node i. The second extension is discussed below.

### 5.3 Edge Weight / Edge Distance Correlations

We employ a simple edge weight / edge distance correlations scheme whose parameters can be fixed using reference values or determined using Bayesian hyperparameter optimization, with the latter to be discussed in the next section.

We recall that, as discussed in Section 2.1, for molecular graphs, bond strength (edge weight) is empirically related to bond length (edge distance) through power laws s = (R/Ro)^-N with parameters R0 and N. We leverage this knowledge and correlate edge weight with edge distance through power laws with parameters R0 and N. However, this is not necessary in general. For other types of 3D graphs, even molecular graphs, other forms of edge weight / edge distance correlations can be used, e.g., exponential functions.

For edges (e), we define the edge weight (w) / edge distance (d) correlation as follows:

$$w = (d / R_0)^{-N}$$

For angle edges (eθ), we define the edge weight (wθ) / edge distance (dθ) correlation as:

$$w_\theta = (d_\theta / R_0^\theta)^{-N_\theta}$$

And for dihedral edges (eφ), we define the edge weight (wφ) / edge distance (dφ) correlation as:

$$w_\phi = (d_\phi / R_0^\phi)^{-N_\phi}$$

The variation of edge weight w.r.t. edge distance, as a function of R0 and N, is shown in the following table:

| Edge distance / R0 | Edge weight (N=2) | Edge weight (N=3) | Edge weight (N=4) | Edge weight (N=5) | Edge weight (N=6) |
|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| 1                 | 1                 | 1                 | 1                 | 1                 | 1                 |
| 1.5               | 0.444             | 0.296             | 0.198             | 0.132             | 0.088             |
| 2                 | 0.25              | 0.125             | 0.063             | 0.031             | 0.016             |
| 2.5               | 0.160             | 0.064             | 0.026             | 0.010             | 0.004             |
| 3                 | 0.111             | 0.037             | 0.012             | 0.004             | 0.001             |

In contrast to standard graph convolutions which use edge_weight with values of one, geometric graph convolutions use edge_weight with values calculated from edge distances in GCNConv (see Section 5.1).

### 5.4 Bayesian Hyperparameter Optimization

If no reference values are available, we can treat the parameters (R0, N), (R^θ_0, Nθ) and (R^φ_0, Nφ) as hyperparameters and use Bayesian hyperparameter optimization [2] to find the best values. Bayesian optimization [19-23] is a powerful tool for the joint optimization of hyperparameters, efficiently trading off exploration and exploitation of the hyperparameter space.

Following [2], we implement Bayesian hyperparameter optimization using BoTorch, GPyTorch and Ax [24-30]. Ax provides the optimize() function to construct and run a full OptimizationLoop, and to return the best hyperparameter configuration. We call the optimize() function with the following input parameters:

- hyperparameters: R0, N, R^θ_0, Nθ, R^φ_0, Nφ
- evaluation function: train_evaluate
- minimize: True
- total trials (default: 20)

The evaluation function, train_evaluate(parametrization), that we provide has three components:

1. model: geometric graph convolution (GGC)
2. train(training dataset, parametrization)
3. evaluate(validation dataset, parametrization)

The hyperparameter configuration (parametrization) is automatically generated by Ax for each Trial during a full run of the OptimizationLoop.

For each Trial, given a hyperparameter configuration, the train() function trains the GGC model (which employs GCNConv) using the training dataset. Once the GGC model is trained, the evaluate() function evaluates the model using the validation dataset and returns the RMSE (Root Mean Squares Error) which serves as the objective score for use in optimization.

---

### النسخة العربية

تعمل التفافات الرسوم البيانية الهندسية على توسيع التفافات الرسوم البيانية القياسية [4] من خلال دمج الهندسة ثلاثية الأبعاد للرسوم البيانية في عملية التفاف الرسم البياني. لا تأخذ التفافات الرسوم البيانية القياسية الترتيبات المكانية للعقد والحواف في الاعتبار. لذلك، يمكنها استيعاب تكوين الرسم البياني فقط، وليس هندسة الرسم البياني.

في الآونة الأخيرة، كانت هناك جهود لتوسيع شبكات GCN من خلال دمج الإحداثيات ثلاثية الأبعاد للعقد في التفافات الرسوم البيانية [5-6]. ومع ذلك، فإن المخططات المقترحة تأخذ في الاعتبار العقد المجاورة فقط. لا تأخذ في الاعتبار العقد الأخرى المهمة لهندسة الرسم البياني. تشمل هذه عقد الجوار الثانية التي تشكل جزءاً من الحواف التي تشكل زوايا وعقد الجوار الثالثة التي تشكل جزءاً من الحواف التي تشكل زوايا ثنائية سطحية.

### 5.1 شبكات التفاف الرسوم البيانية (GCNs)

كما في [1]، نستخدم الشبكات العصبية للرسوم البيانية (GNNs) التي تستخدم مخطط تمرير الرسائل التالي للعقدة i في الطبقة k:

$$x_i^{(k)} = \gamma^{(k)}(x_i^{(k-1)}, \Pi_{j} \lambda^{(k)}(x_i^{(k-1)}, x_j^{(k-1)}, e_{ij}))$$

حيث j ∈ N(i) تشير إلى عقدة مجاورة للعقدة i. $x_i$ هو متجه خصائص العقدة و $e_{ij}$ هو متجه خصائص الحافة. γ و λ تشير إلى دوال قابلة للتفاضل و Π تشير إلى دالة تجميع قابلة للتفاضل.

على وجه التحديد، نستخدم شبكات GCN [4] التي تنفذ تمرير الرسائل باستخدام مصفوفة المجاورة A:

$$X^{(k)} = \tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}X^{(k-1)}\Omega$$

حيث $\tilde{A} = A + I$ تشير إلى مصفوفة المجاورة مع حلقات ذاتية مُدرجة و $\tilde{D}_{ii}=\sum_{j=0} \tilde{A}_{ij}$ مصفوفة درجتها القطرية. $A_{ij}$ تساوي واحد عندما توجد حافة من العقدة i إلى العقدة j، وصفر عندما لا توجد حافة. وبالتالي، جميع الحواف لها وزن واحد.

يتم وصف رسم بياني في PyG بواسطة مثيل من فئة Data، والتي لها السمات التالية: x (مصفوفة خصائص العقد)، edge_index (مؤشرات الحواف)، edge_attr (مصفوفة خصائص الحواف)، pos (مصفوفة مواضع العقد) و y (الهدف). يستخدم تطبيق PyG لـ GCN، GCNConv، متجه edge_weight في التفافات الرسوم البيانية. ومع ذلك، في التفافات الرسوم البيانية القياسية (الافتراضية)، يحتوي متجه edge_weight على قيم واحد، أي أن جميع الحواف لها وزن واحد.

### 5.2 التفافات الرسوم البيانية الهندسية

كإثبات للمفهوم، نستخدم التمثيل الهندسي المسافي للرسم البياني للتفافات الرسوم البيانية الهندسية. يعتمد هذا التمثيل على المسافات: مسافات الحواف (d)، ومسافات الزوايا (dθ)، ومسافات الزوايا الثنائية السطحية (dφ)، كما تمت مناقشته في القسم 4.3. علاوة على ذلك، للاستفادة من شبكات GCN القياسية للتفافات الرسوم البيانية الهندسية، نستخدم مخططاً بسيطاً لارتباطات وزن الحافة ومسافة الحافة يمكن تثبيت معاملاته باستخدام قيم مرجعية أو تحديدها باستخدام التحسين البايزي للمعاملات الفائقة.

يمكّننا الجمع بين استخدام التمثيل الهندسي المسافي للرسم البياني واستخدام مخطط ارتباطات وزن الحافة ومسافة الحافة من دمج الهندسة الكاملة للرسوم البيانية ثلاثية الأبعاد في التفافات الرسوم البيانية باستخدام شبكات GCN القياسية من خلال (1) توسيع أنواع الحواف المعنية لتشمل ليس فقط الحواف (e) مع عقد الجوار، ولكن أيضاً حواف الزوايا (eθ) مع عقد الجوار الثانية وحواف الزوايا الثنائية السطحية (eφ) مع عقد الجوار الثالثة و(2) تخصيص أوزان مختلفة لحواف مختلفة بناءً على نوعها ومسافتها.

يعني التوسع الأول لشبكات GCN القياسية أنه في القسم 5.1 لدينا الآن j ∈ N(i) + N^θ(i) + N^φ(i)، مع N(i) الجيران الأوائل، N^θ(i) الجيران الثانية و N^φ(i) الجيران الثالثة، للعقدة i. تتم مناقشة التوسع الثاني أدناه.

### 5.3 ارتباطات وزن الحافة ومسافة الحافة

نستخدم مخططاً بسيطاً لارتباطات وزن الحافة ومسافة الحافة يمكن تثبيت معاملاته باستخدام قيم مرجعية أو تحديدها باستخدام التحسين البايزي للمعاملات الفائقة، مع مناقشة الأخير في القسم التالي.

نتذكر أنه، كما تمت مناقشته في القسم 2.1، بالنسبة للرسوم البيانية الجزيئية، ترتبط قوة الرابطة (وزن الحافة) تجريبياً بطول الرابطة (مسافة الحافة) من خلال قوانين القوة s = (R/Ro)^-N مع المعاملات R0 و N. نستفيد من هذه المعرفة ونربط وزن الحافة بمسافة الحافة من خلال قوانين القوة مع المعاملات R0 و N. ومع ذلك، هذا ليس ضرورياً بشكل عام. بالنسبة لأنواع أخرى من الرسوم البيانية ثلاثية الأبعاد، حتى للرسوم البيانية الجزيئية، يمكن استخدام أشكال أخرى من ارتباطات وزن الحافة ومسافة الحافة، على سبيل المثال، الدوال الأسية.

بالنسبة للحواف (e)، نحدد ارتباط وزن الحافة (w) / مسافة الحافة (d) على النحو التالي:

$$w = (d / R_0)^{-N}$$

بالنسبة لحواف الزوايا (eθ)، نحدد ارتباط وزن الحافة (wθ) / مسافة الحافة (dθ) على النحو:

$$w_\theta = (d_\theta / R_0^\theta)^{-N_\theta}$$

وبالنسبة لحواف الزوايا الثنائية السطحية (eφ)، نحدد ارتباط وزن الحافة (wφ) / مسافة الحافة (dφ) على النحو:

$$w_\phi = (d_\phi / R_0^\phi)^{-N_\phi}$$

يظهر تباين وزن الحافة بالنسبة لمسافة الحافة، كدالة لـ R0 و N، في الجدول التالي:

| مسافة الحافة / R0 | وزن الحافة (N=2) | وزن الحافة (N=3) | وزن الحافة (N=4) | وزن الحافة (N=5) | وزن الحافة (N=6) |
|------------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| 1                | 1               | 1               | 1               | 1               | 1               |
| 1.5              | 0.444           | 0.296           | 0.198           | 0.132           | 0.088           |
| 2                | 0.25            | 0.125           | 0.063           | 0.031           | 0.016           |
| 2.5              | 0.160           | 0.064           | 0.026           | 0.010           | 0.004           |
| 3                | 0.111           | 0.037           | 0.012           | 0.004           | 0.001           |

على عكس التفافات الرسوم البيانية القياسية التي تستخدم edge_weight بقيم واحد، تستخدم التفافات الرسوم البيانية الهندسية edge_weight بقيم محسوبة من مسافات الحواف في GCNConv (انظر القسم 5.1).

### 5.4 التحسين البايزي للمعاملات الفائقة

إذا لم تكن القيم المرجعية متاحة، يمكننا التعامل مع المعاملات (R0، N)، (R^θ_0، Nθ) و (R^φ_0، Nφ) كمعاملات فائقة واستخدام التحسين البايزي للمعاملات الفائقة [2] للعثور على أفضل القيم. التحسين البايزي [19-23] هو أداة قوية للتحسين المشترك للمعاملات الفائقة، يوازن بكفاءة بين الاستكشاف والاستغلال لفضاء المعاملات الفائقة.

باتباع [2]، نطبق التحسين البايزي للمعاملات الفائقة باستخدام BoTorch و GPyTorch و Ax [24-30]. يوفر Ax دالة optimize() لبناء وتشغيل حلقة تحسين كاملة (OptimizationLoop)، ولإرجاع أفضل تكوين للمعاملات الفائقة. نستدعي دالة optimize() بمعاملات الإدخال التالية:

- المعاملات الفائقة: R0، N، R^θ_0، Nθ، R^φ_0، Nφ
- دالة التقييم: train_evaluate
- التقليل: True
- إجمالي المحاولات (افتراضي: 20)

تحتوي دالة التقييم، train_evaluate(parametrization)، التي نوفرها على ثلاثة مكونات:

1. النموذج: التفاف الرسم البياني الهندسي (GGC)
2. train(مجموعة بيانات التدريب، parametrization)
3. evaluate(مجموعة بيانات التحقق، parametrization)

يتم توليد تكوين المعاملات الفائقة (parametrization) تلقائياً بواسطة Ax لكل محاولة (Trial) أثناء التشغيل الكامل لحلقة التحسين (OptimizationLoop).

لكل محاولة، بالنظر إلى تكوين معاملات فائقة، تدرب دالة train() نموذج GGC (الذي يستخدم GCNConv) باستخدام مجموعة بيانات التدريب. بمجرد تدريب نموذج GGC، تقيّم دالة evaluate() النموذج باستخدام مجموعة بيانات التحقق وتعيد RMSE (خطأ الجذر التربيعي للمتوسط) الذي يعمل كدرجة الهدف للاستخدام في التحسين.

---

### Translation Notes

- **Figures referenced:** Table showing edge weight variation
- **Key terms introduced:** geometric graph convolution, message passing, adjacency matrix, self-loops, degree matrix, PyTorch Geometric (PyG), GCNConv, power laws, BoTorch, GPyTorch, Ax, OptimizationLoop, RMSE
- **Equations:** Multiple mathematical formulas for GCN operations and edge weight correlations
- **Citations:** [4], [5-6], [1], [2], [19-23], [24-30]
- **Special handling:** Mathematical notation, PyG API terminology, Bayesian optimization framework

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
