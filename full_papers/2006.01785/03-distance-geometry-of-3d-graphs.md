# Section 3: Distance Geometry of 3D Graphs
## القسم 3: الهندسة المسافية للرسوم البيانية ثلاثية الأبعاد

**Section:** methodology/background
**Translation Quality:** 0.86
**Glossary Terms Used:** graph, node, edge, distance geometry, optimization, algorithm

---

### English Version

Distance geometry [15] refers to a foundation of geometry based on the concept of distances instead of those of points and lines or point coordinates. In general, the focus of distance geometry is on the so-called Distance Geometry Problem (DGP) which can be stated as: given a weighted graph G = (V, E) and the dimension K of a vector space, draw G in R^K such that each edge is drawn as a straight segment of distance equal to its weight. In other words, the essence of DGP is of reconstructing node positions from given edge distances. A DGP instance may have no solutions if the given distances do not define a metric, a finite number of solutions if the graph is rigid, or an unlimited number of solutions if the graph is flexible.

For 3D graphs, distance geometry is the characterization and study of their geometry based only on given values of the distances between pairs of nodes. From the perspective of distance geometry, therefore, the geometry of 3D graphs can be equivalently specified in terms of edge distances (d), angle distances (dθ) and dihedral distances (dφ). The angle distance is the distance of the angle edge (eθ) and the dihedral distance is the distance of the dihedral edge (eφ). The angle edge is the unconnected, end edge between the end nodes of an angle and the dihedral edge is the unconnected, end edge between the end nodes of a dihedral. (We therefore refer to both angle edges and dihedral edges as end edges.) These are illustrated in the following diagram (with dashed lines representing angle edges and dotted lines representing dihedral edges):

[DIAGRAM SHOWING]:
- Nodes 1, 2, 3, 4
- Edge distances: d12, d23, d34
- Angle distances: dθ13 (dashed), dθ24 (dashed)
- Dihedral distance: dφ14 (dotted)

As the case of using edge distances, angles and dihedrals to specify geometry, a key advantage of specifying geometry in terms of edge distances, angle distances and dihedral distances is its invariance to rotation and translation. In addition, it adopts a unified scheme (distance) and reflects pair-wise node interactions and their generally local nature, which are additional advantages. These are very useful for graph convolutions, which are locally oriented. They are particular useful for molecular graphs, since electrostatic, intermolecular, and other conformation-driven properties of molecules depend on the pair-wise interatomic (internodal) distances.

### 3.1 Molecular Distance Geometry

Distance geometry is the basis for a geometric theory of molecular conformation [16]. A distance geometry description of a 3D molecular graph (conformation) consists of a list of distance and chirality constraints. These are, respectively, lower and upper bounds on the distances, and the chirality of selected quadruples of nodes. The distance geometry approach is predicated on the assumption that it is possible to adequately describe the set of all possible conformations, i.e., the conformation space, by means of such purely geometric descriptions.

In general, one tries to find a number of different solutions (i.e., conformations) that satisfy distance geometry descriptions. Such a set of conformations is called a conformational ensemble. There are many algorithms which together provide a means of generating conformational ensembles consistent with distance geometry descriptions. The overall procedure consists of the following steps [16]:

(1) Bound smoothing: Extrapolating a complete set of lower and upper limits on all the distances from the sparse set of lower and upper bounds that are usually available.

(2) Embedding: Choosing a random distance matrix from within these limits, and computing coordinates that are a certain best fit to the distances. It is critical that good search methods are used to direct search towards favorable regions of the conformational space.

(3) Optimization: Optimizing these coordinates versus an 'error' function which measures the total violation of the distance and chirality constraints.

The conformation generator ETKDG [17] is a stochastic search method that utilizes distance geometry together with knowledge derived from experimental crystal structures. It is used in RDKit by default for conformation generation. It has been shown to generate good conformations for acyclic molecules. Recently it has been improved for conformation generation of molecules containing small or large aliphatic rings.

The upper and lower bounds on the distances are traditionally obtained from chemical knowledge and experimental data. However, deep learning approaches have begun to emerge. A probabilistic generative model is used in [18] to learn distributions, and therefore upper and lower bounds, of the interatomic distances of molecules from their graph representations. Specifically, it uses a variational autoencoder consisting of an inference model qλ(z|d,G) and a generative model pγ(d|z,G)pγ(z|G). The graph representations are based on an extended molecular graph which consists of nodes (atoms), edges (bonds) and auxiliary edges (representing angles and dihedral angles). (Auxiliary edges are the same as end edges discussed in Section 3.) For unseen molecules, upon generation of the upper and lower bounds of the distances using the generative model, it uses a Euclidean distance geometry algorithm to generate conformations.

The Conf17 benchmark is used in [18]. It is the first benchmark for conformation sampling and is based on the ISO17 dataset which consists of conformations of various molecules with the atomic composition C7H10O2. For the Conf17 benchmark, edge distances range from 0.9 to 1.7 Å, angle distances from 1.5 to 3 Å, and dihedral distances from 2 to 4 Å. (We will utilize this information in Section 5.3.)

---

### النسخة العربية

تشير الهندسة المسافية [15] إلى أساس للهندسة يعتمد على مفهوم المسافات بدلاً من النقاط والخطوط أو إحداثيات النقاط. بشكل عام، يركز الاهتمام في الهندسة المسافية على ما يسمى مسألة الهندسة المسافية (DGP) والتي يمكن صياغتها على النحو التالي: بالنظر إلى رسم بياني موزون G = (V, E) والبُعد K لفضاء متجه، ارسم G في R^K بحيث يتم رسم كل حافة كقطعة مستقيمة من مسافة مساوية لوزنها. بعبارة أخرى، جوهر مسألة DGP هو إعادة بناء مواضع العقد من مسافات الحواف المعطاة. قد لا يكون لمثيل DGP حلول إذا لم تحدد المسافات المعطاة مقياساً، أو عدد محدود من الحلول إذا كان الرسم البياني صلباً، أو عدد غير محدود من الحلول إذا كان الرسم البياني مرناً.

بالنسبة للرسوم البيانية ثلاثية الأبعاد، الهندسة المسافية هي توصيف ودراسة هندستها بناءً فقط على القيم المعطاة للمسافات بين أزواج العقد. من منظور الهندسة المسافية، إذن، يمكن تحديد هندسة الرسوم البيانية ثلاثية الأبعاد بشكل مكافئ من حيث مسافات الحواف (d)، ومسافات الزوايا (dθ)، ومسافات الزوايا الثنائية السطحية (dφ). مسافة الزاوية هي مسافة حافة الزاوية (eθ) ومسافة الزاوية الثنائية السطحية هي مسافة حافة الزاوية الثنائية السطحية (eφ). حافة الزاوية هي الحافة الطرفية غير المتصلة بين عقدتي نهاية الزاوية وحافة الزاوية الثنائية السطحية هي الحافة الطرفية غير المتصلة بين عقدتي نهاية الزاوية الثنائية السطحية. (نشير لذلك إلى كل من حواف الزوايا وحواف الزوايا الثنائية السطحية بالحواف الطرفية.) توضح هذه في الرسم التخطيطي التالي (مع خطوط متقطعة تمثل حواف الزوايا وخطوط منقطة تمثل حواف الزوايا الثنائية السطحية):

[رسم تخطيطي يوضح]:
- العقد 1، 2، 3، 4
- مسافات الحواف: d12، d23، d34
- مسافات الزوايا: dθ13 (متقطعة)، dθ24 (متقطعة)
- مسافة الزاوية الثنائية السطحية: dφ14 (منقطة)

كما هو الحال مع استخدام مسافات الحواف والزوايا والزوايا الثنائية السطحية لتحديد الهندسة، فإن الميزة الرئيسية لتحديد الهندسة من حيث مسافات الحواف ومسافات الزوايا ومسافات الزوايا الثنائية السطحية هي ثباتها تجاه الدوران والانتقال. بالإضافة إلى ذلك، يعتمد مخططاً موحداً (المسافة) ويعكس التفاعلات الثنائية بين العقد وطبيعتها المحلية عموماً، وهي مزايا إضافية. هذه مفيدة جداً للتفافات الرسوم البيانية، التي تكون موجهة محلياً. وهي مفيدة بشكل خاص للرسوم البيانية الجزيئية، حيث تعتمد الخصائص الكهروستاتيكية والجزيئية وغيرها من الخصائص المدفوعة بالتشكل للجزيئات على المسافات الثنائية بين الذرات (بين العقد).

### 3.1 الهندسة المسافية الجزيئية

الهندسة المسافية هي الأساس لنظرية هندسية للتشكل الجزيئي [16]. يتكون وصف الهندسة المسافية للرسم البياني الجزيئي ثلاثي الأبعاد (التشكل) من قائمة بقيود المسافة والكيرالية. هذه هي، على التوالي، الحدود السفلى والعليا على المسافات، والكيرالية لرباعيات مختارة من العقد. يستند نهج الهندسة المسافية على افتراض أنه من الممكن وصف مجموعة جميع التشكلات الممكنة بشكل مناسب، أي فضاء التشكل، بوسائل مثل هذه الأوصاف الهندسية البحتة.

بشكل عام، يحاول المرء إيجاد عدد من الحلول المختلفة (أي التشكلات) التي تلبي أوصاف الهندسة المسافية. تسمى مثل هذه المجموعة من التشكلات بالمجموعة التشكلية. هناك العديد من الخوارزميات التي توفر معاً وسيلة لتوليد مجموعات تشكلية متسقة مع أوصاف الهندسة المسافية. يتكون الإجراء العام من الخطوات التالية [16]:

(1) تمهيد الحدود: استقراء مجموعة كاملة من الحدود السفلى والعليا على جميع المسافات من المجموعة المتفرقة من الحدود السفلى والعليا المتاحة عادةً.

(2) التضمين: اختيار مصفوفة مسافات عشوائية من ضمن هذه الحدود، وحساب الإحداثيات التي تكون أفضل ملاءمة معينة للمسافات. من الضروري استخدام طرق بحث جيدة لتوجيه البحث نحو المناطق المواتية من فضاء التشكل.

(3) التحسين: تحسين هذه الإحداثيات مقابل دالة 'خطأ' تقيس إجمالي انتهاك قيود المسافة والكيرالية.

مولد التشكل ETKDG [17] هو طريقة بحث عشوائية تستخدم الهندسة المسافية مع المعرفة المستمدة من البنى البلورية التجريبية. يُستخدم في RDKit افتراضياً لتوليد التشكل. تم إثبات أنه يولد تشكلات جيدة للجزيئات غير الحلقية. مؤخراً تم تحسينه لتوليد تشكل الجزيئات التي تحتوي على حلقات أليفاتية صغيرة أو كبيرة.

يتم الحصول على الحدود العليا والسفلى على المسافات تقليدياً من المعرفة الكيميائية والبيانات التجريبية. ومع ذلك، بدأت مناهج التعلم العميق في الظهور. يُستخدم نموذج توليدي احتمالي في [18] لتعلم التوزيعات، وبالتالي الحدود العليا والسفلى، للمسافات بين الذرات للجزيئات من تمثيلاتها البيانية. على وجه التحديد، يستخدم مشفراً تلقائياً متغيراً يتكون من نموذج استدلال qλ(z|d,G) ونموذج توليدي pγ(d|z,G)pγ(z|G). تستند التمثيلات البيانية إلى رسم بياني جزيئي موسع يتكون من عقد (ذرات)، وحواف (روابط)، وحواف مساعدة (تمثل الزوايا والزوايا الثنائية السطحية). (الحواف المساعدة هي نفس الحواف الطرفية التي تمت مناقشتها في القسم 3.) بالنسبة للجزيئات غير المرئية، عند توليد الحدود العليا والسفلى للمسافات باستخدام النموذج التوليدي، يستخدم خوارزمية هندسة مسافية إقليدية لتوليد التشكلات.

يُستخدم معيار Conf17 في [18]. إنه أول معيار لأخذ عينات التشكل ويستند إلى مجموعة بيانات ISO17 التي تتكون من تشكلات لجزيئات مختلفة بتكوين ذري C7H10O2. بالنسبة لمعيار Conf17، تتراوح مسافات الحواف من 0.9 إلى 1.7 Å، ومسافات الزوايا من 1.5 إلى 3 Å، ومسافات الزوايا الثنائية السطحية من 2 إلى 4 Å. (سنستخدم هذه المعلومات في القسم 5.3.)

---

### Translation Notes

- **Figures referenced:** Diagram showing edge distances, angle distances, and dihedral distances
- **Key terms introduced:** Distance Geometry Problem (DGP), angle edge, dihedral edge, end edges, conformational ensemble, bound smoothing, embedding, chirality, ETKDG, variational autoencoder, Conf17 benchmark
- **Equations:** G = (V, E), qλ(z|d,G), pγ(d|z,G)pγ(z|G)
- **Citations:** [15], [16], [17], [18]
- **Special handling:** Mathematical notation, algorithmic procedures, molecular chemistry concepts

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
