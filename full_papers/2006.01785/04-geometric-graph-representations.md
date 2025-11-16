# Section 4: Geometric Graph Representations
## القسم 4: تمثيلات الرسوم البيانية الهندسية

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** graph, node, edge, matrix, feature, representation

---

### English Version

To facilitate the incorporation of geometry in deep learning on 3D graphs, we define three types of geometric graph representations: positional, angle-geometric and distance-geometric, as discussed in the following.

### 4.1 Positional Graph Representation

In general, a 3D graph can be represented as G = (X, (I, E), P) where X ∈ R^(N×d) is the node feature matrix, (I, E) is the sparse adjacency tuple, and P ∈ R^(N×3) is the node position matrix. I ∈ N^(2×U) encodes edge indices in coordinate (COO) format and E ∈ R^(U×s) is the edge feature matrix. P encodes the Cartesian coordinates of nodes. (N is the number of nodes, U is the number of edges, d is the number of node features, and s is the number of edge features.) This representation is based on node positions; therefore we refer to it as the positional graph representation. As discussed in Section 2, it depends on the (arbitrary) choice of the origin for the coordinates and it is too general for representing geometry.

### 4.2 Angle-Geometric Graph Representation

From the perspective of geometry, a 3D graph can be represented as G = (X, (I, E), (D, Θ, Φ)) where D ∈ R^(U×1) is the edge distance matrix, Θ ∈ R^(Uθ×1) is the angle matrix, and Φ ∈ R^(Uφ×1) is the dihedral matrix. (U is the number of edges, Uθ is the number of angles, and Uφ is the number of dihedrals.) This representation centers on (edge distances,) angles and dihedrals; therefore we refer to it as the angle-geometric graph representation. As discussed in Section 2, it is invariant to rotation and translation of the graph, which is a major advantage over the positional graph representation.

### 4.3 Distance-Geometric Graph Representation

From the perspective of distance geometry, a 3D graph can be represented as G = (X, (I, E), (D, Dθ, Dφ)) where D ∈ R^(U×1) is the edge distance matrix, Dθ ∈ R^(Uθ×1) is the angle distance matrix, and Dφ ∈ R^(Uφ×1) is the dihedral distance matrix. (U is the number of edges, Uθ is the number of angles, and Uφ is the number of dihedrals.) This representation is based on distances; therefore we refer to it as the distance-geometric graph representation. It is invariant to rotation and translation of the graph, same as the angle-geometric graph representation. In addition, as discussed in Section 3, it reflects pair-wise node interactions and their generally local nature, which is another major advantage.

---

### النسخة العربية

لتسهيل دمج الهندسة في التعلم العميق على الرسوم البيانية ثلاثية الأبعاد، نحدد ثلاثة أنواع من تمثيلات الرسوم البيانية الهندسية: الموضعية، والهندسية الزاوية، والهندسية المسافية، كما هو موضح في ما يلي.

### 4.1 التمثيل الموضعي للرسم البياني

بشكل عام، يمكن تمثيل رسم بياني ثلاثي الأبعاد على النحو G = (X, (I, E), P) حيث X ∈ R^(N×d) هي مصفوفة خصائص العقد، و(I, E) هي الثنائية المجاورة المتفرقة، و P ∈ R^(N×3) هي مصفوفة مواضع العقد. I ∈ N^(2×U) تشفر مؤشرات الحواف بتنسيق الإحداثيات (COO) و E ∈ R^(U×s) هي مصفوفة خصائص الحواف. P تشفر الإحداثيات الديكارتية للعقد. (N هو عدد العقد، U هو عدد الحواف، d هو عدد خصائص العقد، و s هو عدد خصائص الحواف.) يعتمد هذا التمثيل على مواضع العقد؛ لذلك نشير إليه بالتمثيل الموضعي للرسم البياني. كما تمت مناقشته في القسم 2، يعتمد على الاختيار (التعسفي) للأصل للإحداثيات ويكون عاماً جداً لتمثيل الهندسة.

### 4.2 التمثيل الهندسي الزاوي للرسم البياني

من منظور الهندسة، يمكن تمثيل رسم بياني ثلاثي الأبعاد على النحو G = (X, (I, E), (D, Θ, Φ)) حيث D ∈ R^(U×1) هي مصفوفة مسافات الحواف، Θ ∈ R^(Uθ×1) هي مصفوفة الزوايا، و Φ ∈ R^(Uφ×1) هي مصفوفة الزوايا الثنائية السطحية. (U هو عدد الحواف، Uθ هو عدد الزوايا، و Uφ هو عدد الزوايا الثنائية السطحية.) يتمحور هذا التمثيل حول (مسافات الحواف،) والزوايا والزوايا الثنائية السطحية؛ لذلك نشير إليه بالتمثيل الهندسي الزاوي للرسم البياني. كما تمت مناقشته في القسم 2، إنه ثابت تجاه الدوران والانتقال للرسم البياني، وهو ميزة رئيسية على التمثيل الموضعي للرسم البياني.

### 4.3 التمثيل الهندسي المسافي للرسم البياني

من منظور الهندسة المسافية، يمكن تمثيل رسم بياني ثلاثي الأبعاد على النحو G = (X, (I, E), (D, Dθ, Dφ)) حيث D ∈ R^(U×1) هي مصفوفة مسافات الحواف، Dθ ∈ R^(Uθ×1) هي مصفوفة مسافات الزوايا، و Dφ ∈ R^(Uφ×1) هي مصفوفة مسافات الزوايا الثنائية السطحية. (U هو عدد الحواف، Uθ هو عدد الزوايا، و Uφ هو عدد الزوايا الثنائية السطحية.) يعتمد هذا التمثيل على المسافات؛ لذلك نشير إليه بالتمثيل الهندسي المسافي للرسم البياني. إنه ثابت تجاه الدوران والانتقال للرسم البياني، تماماً مثل التمثيل الهندسي الزاوي للرسم البياني. بالإضافة إلى ذلك، كما تمت مناقشته في القسم 3، يعكس التفاعلات الثنائية بين العقد وطبيعتها المحلية عموماً، وهي ميزة رئيسية أخرى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** positional graph representation, angle-geometric graph representation, distance-geometric graph representation, node feature matrix, edge feature matrix, adjacency tuple, COO format
- **Equations:** G = (X, (I, E), P), G = (X, (I, E), (D, Θ, Φ)), G = (X, (I, E), (D, Dθ, Dφ))
- **Citations:** Sections 2 and 3
- **Special handling:** Mathematical notation with matrices and dimensions

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
