# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** graph, node, edge, deep learning, graph convolution, hyperparameter, optimization, Bayesian optimization

---

### English Version

The geometry of three-dimensional (3D) graphs, consisting of nodes and edges, plays a crucial role in many important applications. An excellent example is molecular graphs, whose geometry influences important properties of a molecule including its reactivity and biological activity.

The geometry of 3D graphs is often specified in terms of the Cartesian coordinates of nodes. However, such specification depends on the (arbitrary) choice of origin and is too general for specifying geometry. We focus on 3D graphs whose geometry can be fully specified in terms of edge distances (d), angles (θ) and dihedrals (φ). A key advantage of such specification is its invariance to rotation and translation of the graph.

Distance geometry [15] is the characterization and study of the geometry of 3D graphs based only on given values of the distances between pairs of nodes. From the perspective of distance geometry, the geometry of 3D graphs can be equivalently specified in terms of edge distances (d), angle distances (dθ) and dihedral distances (dφ). In addition to invariance to rotation and translation of the graph, such specification adopts a unified scheme (distance) and reflects pair-wise node interactions and their generally local nature, which are additional advantages.

To facilitate the incorporation of geometry in deep learning on 3D graphs, we define three types of geometric graph representations: positional, angle-geometric and distance-geometric. The positional graph representation is based on node positions, i.e., Cartesian coordinates of nodes. The angle-geometric graph representation centers on edge distances, angles and dihedrals; it is invariant to rotation and translation of the graph. The distance-geometric graph representation is based on distances: edge distances, angle distances and dihedral distances; it is invariant to rotation and translation of the graph and it reflects pair-wise node interactions and their generally local nature.

For proof of concept, we use the distance-geometric graph representation for geometric graph convolutions. Further, to utilize standard graph convolutional networks (GCNs) [4] for geometric graph convolutions, we employ a simple edge weight / edge distance correlations scheme, whose parameters can be fixed using reference values or determined using Bayesian hyperparameter optimization [2].

GCNs have been applied to deep learning on graphs. However, standard graph convolutions do not take spatial arrangements of the nodes and edges into account. Therefore, they can accommodate only graph constitution, but not graph geometry. Recently, there have been efforts to extend GCNs by incorporating 3D node coordinates in graph convolutions [5-6]. The proposed schemes, however, only consider adjacent nodes. They do not consider other nodes that are important to graph geometry. These include second-neighbor nodes which are part of the edges that form angles and third-neighbor nodes which are part of the edges that form dihedrals.

The combination of using the distance-geometric graph representation and employing an edge weight / edge distance correlations scheme enables us to incorporate the full geometry of 3D graphs in graph convolutions utilizing standard GCNs by (1) expanding the kinds of edges involved to include not just edges with neighbor nodes, but also angle edges with second-neighbor nodes and dihedral edges with third-neighbor nodes and (2) assigning different weights to different edges based on their kind and their distance.

For molecular graphs, edge distance corresponds to bond length and edge weight to bond strength. Bond strength is empirically related to bond length through power laws with parameters R0 and N [11-12]. We leverage this knowledge and correlate edge weight with edge length through power laws with parameters R0 and N in the feasibility study, which is on molecular graphs. However, this is not necessary in general. For other types of 3D graphs, even for molecular graphs, other forms of edge weight / edge distance correlations can be used, e.g., exponential functions.

For the feasibility study, we implemented geometric graph convolutions using PyTorch Geometric (PyG) [1, 3] and Bayesian hyperparameter optimization using BoTorch, GPyTorch and Ax [2, 24-30]. We used the ESOL and FreeSolv datasets provided by geo-GCN [6], which contain molecular graph data including three-dimensional node coordinates.

---

### النسخة العربية

تلعب هندسة الرسوم البيانية ثلاثية الأبعاد، المكونة من العقد والحواف، دوراً حاسماً في العديد من التطبيقات المهمة. مثال ممتاز على ذلك هو الرسوم البيانية الجزيئية، التي تؤثر هندستها على خصائص مهمة للجزيء بما في ذلك تفاعله ونشاطه البيولوجي.

غالباً ما يتم تحديد هندسة الرسوم البيانية ثلاثية الأبعاد من حيث الإحداثيات الديكارتية للعقد. ومع ذلك، يعتمد هذا التحديد على الاختيار (التعسفي) للأصل ويكون عاماً جداً لتحديد الهندسة. نركز على الرسوم البيانية ثلاثية الأبعاد التي يمكن تحديد هندستها بالكامل من حيث مسافات الحواف (d)، والزوايا (θ)، والزوايا الثنائية السطحية (φ). الميزة الرئيسية لهذا التحديد هي ثباته تجاه الدوران والانتقال للرسم البياني.

الهندسة المسافية [15] هي توصيف ودراسة هندسة الرسوم البيانية ثلاثية الأبعاد بناءً فقط على القيم المعطاة للمسافات بين أزواج العقد. من منظور الهندسة المسافية، يمكن تحديد هندسة الرسوم البيانية ثلاثية الأبعاد بشكل مكافئ من حيث مسافات الحواف (d)، ومسافات الزوايا (dθ)، ومسافات الزوايا الثنائية السطحية (dφ). بالإضافة إلى الثبات تجاه الدوران والانتقال للرسم البياني، يعتمد هذا التحديد مخططاً موحداً (المسافة) ويعكس التفاعلات الثنائية بين العقد وطبيعتها المحلية عموماً، وهي مزايا إضافية.

لتسهيل دمج الهندسة في التعلم العميق على الرسوم البيانية ثلاثية الأبعاد، نحدد ثلاثة أنواع من تمثيلات الرسوم البيانية الهندسية: الموضعية، والهندسية الزاوية، والهندسية المسافية. يعتمد التمثيل الموضعي للرسم البياني على مواضع العقد، أي الإحداثيات الديكارتية للعقد. يتمحور التمثيل الهندسي الزاوي للرسم البياني حول مسافات الحواف والزوايا والزوايا الثنائية السطحية؛ وهو ثابت تجاه الدوران والانتقال للرسم البياني. يعتمد التمثيل الهندسي المسافي للرسم البياني على المسافات: مسافات الحواف، ومسافات الزوايا، ومسافات الزوايا الثنائية السطحية؛ وهو ثابت تجاه الدوران والانتقال للرسم البياني ويعكس التفاعلات الثنائية بين العقد وطبيعتها المحلية عموماً.

كإثبات للمفهوم، نستخدم التمثيل الهندسي المسافي للرسم البياني للتفافات الرسوم البيانية الهندسية. علاوة على ذلك، للاستفادة من شبكات التفاف الرسوم البيانية القياسية (GCNs) [4] للتفافات الرسوم البيانية الهندسية، نستخدم مخططاً بسيطاً لارتباطات وزن الحافة ومسافة الحافة، يمكن تثبيت معاملاته باستخدام قيم مرجعية أو تحديدها باستخدام التحسين البايزي للمعاملات الفائقة [2].

تم تطبيق شبكات GCN على التعلم العميق على الرسوم البيانية. ومع ذلك، لا تأخذ التفافات الرسوم البيانية القياسية الترتيبات المكانية للعقد والحواف في الاعتبار. لذلك، يمكنها استيعاب تكوين الرسم البياني فقط، وليس هندسة الرسم البياني. في الآونة الأخيرة، كانت هناك جهود لتوسيع شبكات GCN من خلال دمج الإحداثيات ثلاثية الأبعاد للعقد في التفافات الرسوم البيانية [5-6]. ومع ذلك، فإن المخططات المقترحة تأخذ في الاعتبار العقد المجاورة فقط. لا تأخذ في الاعتبار العقد الأخرى المهمة لهندسة الرسم البياني. تشمل هذه عقد الجوار الثانية التي تشكل جزءاً من الحواف التي تشكل زوايا وعقد الجوار الثالثة التي تشكل جزءاً من الحواف التي تشكل زوايا ثنائية سطحية.

يمكّننا الجمع بين استخدام التمثيل الهندسي المسافي للرسم البياني واستخدام مخطط ارتباطات وزن الحافة ومسافة الحافة من دمج الهندسة الكاملة للرسوم البيانية ثلاثية الأبعاد في التفافات الرسوم البيانية باستخدام شبكات GCN القياسية من خلال (1) توسيع أنواع الحواف المعنية لتشمل ليس فقط الحواف مع عقد الجوار، ولكن أيضاً حواف الزوايا مع عقد الجوار الثانية وحواف الزوايا الثنائية السطحية مع عقد الجوار الثالثة و(2) تخصيص أوزان مختلفة لحواف مختلفة بناءً على نوعها ومسافتها.

بالنسبة للرسوم البيانية الجزيئية، تتوافق مسافة الحافة مع طول الرابطة ووزن الحافة مع قوة الرابطة. ترتبط قوة الرابطة تجريبياً بطول الرابطة من خلال قوانين القوة مع المعاملات R0 و N [11-12]. نستفيد من هذه المعرفة ونربط وزن الحافة بطول الحافة من خلال قوانين القوة مع المعاملات R0 و N في دراسة الجدوى، التي تتم على الرسوم البيانية الجزيئية. ومع ذلك، هذا ليس ضرورياً بشكل عام. بالنسبة لأنواع أخرى من الرسوم البيانية ثلاثية الأبعاد، حتى للرسوم البيانية الجزيئية، يمكن استخدام أشكال أخرى من ارتباطات وزن الحافة ومسافة الحافة، على سبيل المثال، الدوال الأسية.

لدراسة الجدوى، قمنا بتطبيق التفافات الرسوم البيانية الهندسية باستخدام PyTorch Geometric (PyG) [1، 3] والتحسين البايزي للمعاملات الفائقة باستخدام BoTorch و GPyTorch و Ax [2، 24-30]. استخدمنا مجموعات بيانات ESOL و FreeSolv المقدمة من geo-GCN [6]، والتي تحتوي على بيانات الرسوم البيانية الجزيئية بما في ذلك الإحداثيات ثلاثية الأبعاد للعقد.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** distance geometry, positional graph representation, angle-geometric graph representation, distance-geometric graph representation, edge distance, angle distance, dihedral distance, second-neighbor nodes, third-neighbor nodes, bond strength, power laws
- **Equations:** 0
- **Citations:** [2], [4], [5-6], [11-12], [1, 3], [24-30]
- **Special handling:** Technical terminology related to graph geometry, molecular graphs, and GCNs

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
