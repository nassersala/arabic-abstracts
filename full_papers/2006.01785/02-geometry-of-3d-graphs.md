# Section 2: Geometry of 3D Graphs
## القسم 2: هندسة الرسوم البيانية ثلاثية الأبعاد

**Section:** methodology/background
**Translation Quality:** 0.86
**Glossary Terms Used:** graph, node, edge, dihedral

---

### English Version

The geometry of 3D graphs is the three-dimensional arrangement of the nodes and edges in a graph. It is often specified in terms of the Cartesian coordinates of nodes. However, such specification depends on the (arbitrary) choice of origin and is too general for specifying geometry.

We focus on 3D graphs whose geometry can be fully specified in terms of edge distances (d), angles (θ) and dihedrals (φ). Molecular graphs are excellent examples of such graphs. The edge distance is the distance between two nodes connected together. The angle is the angle formed between three nodes across two edges. For three edges connected in a chain, the dihedral is the angle between the plane formed by the first two edges and the plane formed by the last two edges. These are illustrated in the following diagram:

[DIAGRAM SHOWING]:
- Nodes 1, 2, 3, 4
- Edge distance d12 between nodes 1 and 2
- Edge distance d23 between nodes 2 and 3
- Edge distance d34 between nodes 3 and 4
- Angle θ123 at node 2
- Angle θ234 at node 3
- Dihedral φ1234 between planes (1,2,3) and (2,3,4)

A key advantage of using edge distances, angles and dihedrals to specify geometry is its invariance to rotation and translation of the graph.

### 2.1 Molecular Geometry

Molecular geometry (https://en.wikipedia.org/wiki/Molecular_geometry) is the three-dimensional arrangement of the atoms (nodes) and bonds (edges) in a molecule. It influences important properties of a molecule including its reactivity and biological activity. An excellent example is 3D-QSAR [7-8] which exploits the three-dimensional properties of the molecules (ligands) to predict their biological activities. Chemical compounds containing one or more single bonds exist at each moment in many different conformations. Therefore, it is necessary to include various such conformations (geometries) of the molecules in a QSAR (Quantitative Structure Activity Relationship) study.

Molecular geometry can be specified in terms of bond lengths (i.e., edge distances), bond angles (i.e., angles) and dihedral angles (i.e., dihedrals). The bond length is the average distance between two atoms bonded together. The bond angle is the angle formed between three atoms across two bonds. For three bonds in a chain, the dihedral angle is the angle between the plane formed by the first two bonds and the plane formed by the last two bonds. These are no different from the general case of 3D graphs. Bond lengths, bond angles and dihedral angles can be calculated from the Cartesian coordinates of atoms in a molecule, which are generally expressed in the unit of angstrom (Å).

Bond lengths (https://en.wikipedia.org/wiki/Bond_length) of carbon with other elements are in the range of 1 to 3 Å. Bond lengths in organic compounds generally range from 1.08 to 1.54 Å. However, the existence of a very long C–C bond length of up to 3.05 Å has been found in dimers. The longest covalent bond is the bismuth-iodine single bond with length 2.81 Å. The bond length between a given pair of atoms may vary between different molecules.

Bond length is related to bond order, or bond type (single, double, triple, aromatic), and the correlation is decreasing and bend in conjugated hydrocarbons [9]. Bond lengths have been used for automatic bond perception [10], whose aim is to identify bond types, via decision-trees based machine learning. Bond order can be used to represent bond strength. However, there is no unique definition of bond strength. Other bond properties have been associated with bond strength, e.g., bond dissociation energy, the force constant of the bond, and the interatomic electron density of the bond.

Bond strength is inversely related to bond length: all other factors being equal, a stronger bond will be shorter. For oxides, the relationship is of the form s = (R/Ro)^-N [11] where s = bond strength, R = bond length and Ro and N are fitted parameters, with Ro in the range of 1.1 to 2.9 Å and N from 2.2 to 6.0. The (inverse) relationship can also be expressed by the power law R/R0 = p^-n [12] where p = bond strength, with Ro = 1.39 Å and n = 0.22 (thus n ≈ 1/N). In both cases, ln(s), or ln(p), has a linear dependence on ln(R). It should be noted that these correlations are empirical and they are not fundamental rules or laws [13]. (We will utilize the above information in Section 5.3.)

Predicting an accurate 3D molecular geometry is a crucial task for cheminformatics. Various methods are available including: RDKit (based on ETKDG, See Section 3.1), OpenBabel and fragment-based. These are discussed and compared in [14]. The outcomes of prediction include coordinates, bond lengths, bond angles and dihedral angles, among other things.

The RDKit (https://www.rdkit.org/) provides the method GetBondLength() to get the bond length in Å between bonded atoms i and j. It also provides the method GetAngleDegree() and GetAngleRad() to get the bond angle between bonded atoms i, j and k, as well as GetDihedralDegree() and GetDihedralRad() to get the dihedral angle between bonded atoms i, j, k and l.

---

### النسخة العربية

هندسة الرسوم البيانية ثلاثية الأبعاد هي الترتيب ثلاثي الأبعاد للعقد والحواف في الرسم البياني. غالباً ما يتم تحديدها من حيث الإحداثيات الديكارتية للعقد. ومع ذلك، يعتمد هذا التحديد على الاختيار (التعسفي) للأصل ويكون عاماً جداً لتحديد الهندسة.

نركز على الرسوم البيانية ثلاثية الأبعاد التي يمكن تحديد هندستها بالكامل من حيث مسافات الحواف (d)، والزوايا (θ)، والزوايا الثنائية السطحية (φ). الرسوم البيانية الجزيئية هي أمثلة ممتازة لمثل هذه الرسوم البيانية. مسافة الحافة هي المسافة بين عقدتين متصلتين معاً. الزاوية هي الزاوية المتشكلة بين ثلاث عقد عبر حافتين. بالنسبة لثلاث حواف متصلة في سلسلة، الزاوية الثنائية السطحية هي الزاوية بين المستوى المتشكل من الحافتين الأوليين والمستوى المتشكل من الحافتين الأخيرتين. توضح هذه في الرسم التخطيطي التالي:

[رسم تخطيطي يوضح]:
- العقد 1، 2، 3، 4
- مسافة الحافة d12 بين العقدتين 1 و 2
- مسافة الحافة d23 بين العقدتين 2 و 3
- مسافة الحافة d34 بين العقدتين 3 و 4
- الزاوية θ123 عند العقدة 2
- الزاوية θ234 عند العقدة 3
- الزاوية الثنائية السطحية φ1234 بين المستويين (1،2،3) و(2،3،4)

الميزة الرئيسية لاستخدام مسافات الحواف والزوايا والزوايا الثنائية السطحية لتحديد الهندسة هي ثباتها تجاه الدوران والانتقال للرسم البياني.

### 2.1 الهندسة الجزيئية

الهندسة الجزيئية (https://en.wikipedia.org/wiki/Molecular_geometry) هي الترتيب ثلاثي الأبعاد للذرات (العقد) والروابط (الحواف) في الجزيء. تؤثر على خصائص مهمة للجزيء بما في ذلك تفاعله ونشاطه البيولوجي. مثال ممتاز هو 3D-QSAR [7-8] الذي يستغل الخصائص ثلاثية الأبعاد للجزيئات (الروابط) للتنبؤ بأنشطتها البيولوجية. المركبات الكيميائية التي تحتوي على رابطة واحدة أو أكثر من الروابط المفردة موجودة في كل لحظة في العديد من التشكلات المختلفة. لذلك، من الضروري تضمين مختلف هذه التشكلات (الهندسات) للجزيئات في دراسة QSAR (العلاقة الكمية بين البنية والنشاط).

يمكن تحديد الهندسة الجزيئية من حيث أطوال الروابط (أي مسافات الحواف)، وزوايا الروابط (أي الزوايا)، والزوايا الثنائية السطحية (أي الزوايا الثنائية السطحية). طول الرابطة هو متوسط المسافة بين ذرتين مرتبطتين معاً. زاوية الرابطة هي الزاوية المتشكلة بين ثلاث ذرات عبر رابطتين. بالنسبة لثلاث روابط في سلسلة، الزاوية الثنائية السطحية هي الزاوية بين المستوى المتشكل من الرابطتين الأوليين والمستوى المتشكل من الرابطتين الأخيرتين. هذه لا تختلف عن الحالة العامة للرسوم البيانية ثلاثية الأبعاد. يمكن حساب أطوال الروابط وزوايا الروابط والزوايا الثنائية السطحية من الإحداثيات الديكارتية للذرات في الجزيء، والتي يتم التعبير عنها عموماً بوحدة الأنجستروم (Å).

أطوال الروابط (https://en.wikipedia.org/wiki/Bond_length) للكربون مع العناصر الأخرى تتراوح بين 1 إلى 3 Å. أطوال الروابط في المركبات العضوية تتراوح عموماً من 1.08 إلى 1.54 Å. ومع ذلك، تم العثور على وجود طول رابطة C-C طويل جداً يصل إلى 3.05 Å في الثنائيات. أطول رابطة تساهمية هي الرابطة المفردة بين البزموت واليود بطول 2.81 Å. قد يختلف طول الرابطة بين زوج معين من الذرات بين جزيئات مختلفة.

يرتبط طول الرابطة برتبة الرابطة، أو نوع الرابطة (مفردة، مزدوجة، ثلاثية، أروماتية)، والارتباط متناقص ومنحني في الهيدروكربونات المترافقة [9]. تم استخدام أطوال الروابط للإدراك الآلي للروابط [10]، والذي يهدف إلى تحديد أنواع الروابط، عبر التعلم الآلي القائم على أشجار القرار. يمكن استخدام رتبة الرابطة لتمثيل قوة الرابطة. ومع ذلك، لا يوجد تعريف فريد لقوة الرابطة. تم ربط خصائص روابط أخرى بقوة الرابطة، على سبيل المثال، طاقة تفكك الرابطة، وثابت القوة للرابطة، وكثافة الإلكترون بين الذرات للرابطة.

قوة الرابطة مرتبطة عكسياً بطول الرابطة: مع تساوي جميع العوامل الأخرى، ستكون الرابطة الأقوى أقصر. بالنسبة للأكاسيد، العلاقة من الشكل s = (R/Ro)^-N [11] حيث s = قوة الرابطة، R = طول الرابطة و Ro و N معاملات مُطابقة، مع Ro في نطاق 1.1 إلى 2.9 Å و N من 2.2 إلى 6.0. يمكن أيضاً التعبير عن العلاقة (العكسية) بقانون القوة R/R0 = p^-n [12] حيث p = قوة الرابطة، مع Ro = 1.39 Å و n = 0.22 (وبالتالي n ≈ 1/N). في كلتا الحالتين، ln(s)، أو ln(p)، له اعتماد خطي على ln(R). تجدر الإشارة إلى أن هذه الارتباطات تجريبية وليست قواعد أو قوانين أساسية [13]. (سنستخدم المعلومات أعلاه في القسم 5.3.)

التنبؤ بهندسة جزيئية ثلاثية الأبعاد دقيقة هو مهمة حاسمة للمعلوماتية الكيميائية. تتوفر طرق مختلفة بما في ذلك: RDKit (بناءً على ETKDG، انظر القسم 3.1)، وOpenBabel والطرق القائمة على الأجزاء. تمت مناقشة هذه ومقارنتها في [14]. تشمل نتائج التنبؤ الإحداثيات وأطوال الروابط وزوايا الروابط والزوايا الثنائية السطحية، من بين أشياء أخرى.

يوفر RDKit (https://www.rdkit.org/) الطريقة GetBondLength() للحصول على طول الرابطة بالـ Å بين الذرات المرتبطة i و j. كما يوفر الطريقتين GetAngleDegree() و GetAngleRad() للحصول على زاوية الرابطة بين الذرات المرتبطة i و j و k، وكذلك GetDihedralDegree() و GetDihedralRad() للحصول على الزاوية الثنائية السطحية بين الذرات المرتبطة i و j و k و l.

---

### Translation Notes

- **Figures referenced:** Diagram showing edge distances, angles, and dihedrals
- **Key terms introduced:** molecular geometry, bond length, bond angle, dihedral angle, bond strength, bond order, 3D-QSAR, conformation, angstrom
- **Equations:** s = (R/Ro)^-N, R/R0 = p^-n
- **Citations:** [7-8], [9], [10], [11], [12], [13], [14]
- **Special handling:** Chemical terminology, molecular concepts, RDKit methods

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
