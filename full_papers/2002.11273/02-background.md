# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.86
**Glossary Terms Used:** matrix, sparse, vector, scalar, compression, format, graph, algorithm, adjacency matrix, breadth-first search, clustering, solver, distributed system, neural network, computation, memory, storage

---

### English Version

## 2.1 Preliminaries

### 2.1.1 Notation

The paper employs standardized mathematical notation throughout. Bold capital italics denote matrices (𝑨, 𝑩, 𝑪), while lowercase bold italics represent vectors, and lowercase italics represent scalars. Key symbolic representations include:

- 𝑨 and 𝑩 as input sparse matrices; 𝑪 as output sparse matrix
- 𝒂ᵢ₊ representing the i-th row vector of 𝑨
- 𝒂₊ⱼ representing the j-th column vector of 𝑨
- p, q, r denoting matrix dimensions where 𝑨 is p×q, 𝑩 is q×r, 𝑪 is p×r
- Inner product (·), outer product (⊗), and general multiplication (×) operations
- Element-wise multiplication (∘) between matrices

### 2.1.2 Sparse Matrix

Sparse matrices lack a universally accepted formal definition. The most widely adopted characterization comes from Wilkinson: "sparse matrix is any matrix with enough zeros that it pays to take advantage of them." An alternative quantitative approach defines a matrix 𝑨 as sparse when its nonzero count equals O(n).

### 2.1.3 Compression Format

Dense storage of sparse matrices generates unnecessary computation and memory waste. Compression formats address this inefficiency by storing only nonzero elements and their locations.

**Basic Formats:**

- **COO (Coordinate format)**: Stores row index, column index, and value of each nonzero in separate arrays—the simplest approach
- **CSR (Compressed Sparse Row)**: Row-major format replacing row indices with row pointers indicating the first nonzero per row
- **CSC (Compressed Sparse Column)**: Column-major variant replacing column indices with column pointers
- **ELL (ELLPACK)**: Compacts nonzeros leftward, storing column indices for each nonzero element
- **DIA (Diagonal format)**: Designed for diagonal matrices, storing nonzeros in each diagonal with offset information

**Advanced Formats:**

The survey documents numerous specialized formats developed for specific applications:

- DCSC and DCSR (Double Compressed variants) for hypersparse matrices, eliminating pointer repetition
- BCSR (Blocked CSR) for distributed computation
- HNI (Huffman-coded Non-zero Indication) using bitmap-based encoding
- CFM (Compressed Feature Map) for neural network sparse feature storage
- Bitmap/BitMask representations using 1s for nonzeros and 0s otherwise
- RLC (Run-Length Coded) variants for deep neural network weight matrices
- Tiled structures for hierarchical representation

## 2.2 Typical Applications

### 2.2.1 Multi-source BFS

Breadth-first search constitutes a fundamental graph analysis subroutine enabling connected component discovery, shortest path identification, and k-hop neighbor enumeration. Standard BFS traverses from a source vertex using sparse matrix-vector multiplication between graph adjacency matrix 𝑨 and sparse vectors representing sources.

Multi-source BFS (MS-BFS) executes multiple independent traversals concurrently, formulated as matrix multiplication operations. Given multiple source vertices, MS-BFS performs successive SpGEMM operations: first computing 𝑩¹ = 𝑨 × 𝑿 (where 𝑿 represents source vectors), then 𝑩² = 𝑨 × 𝑩¹, iterating until all reachable vertices are discovered.

This concurrent approach enables "sharing computation between different BFSs without paying the synchronization cost," making SpGEMM optimization critical for large-scale graph analysis.

### 2.2.2 Markov Clustering (MCL)

MCL is an unsupervised clustering algorithm for biological data that groups closely connected points through random walks on Markov chains. The algorithm iterates through expansion and inflation phases:

- **Expansion phase**: Computing 𝑩 = 𝑨 × 𝑨 strengthens connections and promotes convergence
- **Pruning step**: Removing entries below specified thresholds maintains sparsity
- **Inflation phase**: Element-wise powers weaken loosely connected point associations

The high computational and memory overhead prompted development of HipMCL (High-performance MCL) for accelerating clustering on distributed platforms.

### 2.2.3 Algebraic Multigrid Solvers

AMG solves large sparse linear systems (𝑨𝒙 = 𝒃) by automatically constructing grid hierarchies and transfer operators. The method comprises setup and solve phases:

- **Setup phase**: Constructs interpolation operator 𝑷ₗ, restriction operator 𝑹ₗ = 𝑷ₗᵀ, and coarse system via Galerkin product 𝑨ₗ₊₁ = 𝑹ₗ𝑨ₗ𝑷ₗ
- **Solve phase**: Dominated by sparse matrix-vector multiplication

The critical setup computation involves two SpGEMM operations implementing the Galerkin product. These operations consume "more than 80% of total construction time," and may execute repeatedly per timestep in transient or nonlinear problems, establishing SpGEMM optimization as essential for AMG efficiency.

### 2.2.4 Other Applications

SpGEMM serves as a critical computational component in genome assembly, NoSQL databases, triangle counting in graphs, graph contraction, graph coloring algorithms, all-pairs shortest path computations, subgraph matching, cycle detection and counting, and molecular dynamics simulations.

---

### النسخة العربية

## 2.1 المقدمات

### 2.1.1 الترميز

تستخدم الورقة ترميزاً رياضياً موحداً في جميع أنحائها. تشير الحروف المائلة الكبيرة الغامقة إلى المصفوفات (𝑨، 𝑩، 𝑪)، بينما تمثل الحروف المائلة الصغيرة الغامقة المتجهات، وتمثل الحروف المائلة الصغيرة القيم القياسية. تشمل التمثيلات الرمزية الرئيسية:

- 𝑨 و𝑩 كمصفوفات إدخال متفرقة؛ 𝑪 كمصفوفة إخراج متفرقة
- 𝒂ᵢ₊ يمثل متجه الصف i من 𝑨
- 𝒂₊ⱼ يمثل متجه العمود j من 𝑨
- p و q و r تشير إلى أبعاد المصفوفة حيث 𝑨 هي p×q، و𝑩 هي q×r، و𝑪 هي p×r
- عمليات الضرب الداخلي (·)، والضرب الخارجي (⊗)، والضرب العام (×)
- الضرب العنصري (∘) بين المصفوفات

### 2.1.2 المصفوفة المتفرقة

تفتقر المصفوفات المتفرقة إلى تعريف رسمي مقبول عالمياً. التوصيف الأكثر قبولاً يأتي من ويلكنسون: "المصفوفة المتفرقة هي أي مصفوفة بها أصفار كافية بحيث يكون من المفيد الاستفادة منها". يحدد نهج كمي بديل المصفوفة 𝑨 على أنها متفرقة عندما يكون عدد عناصرها غير الصفرية يساوي O(n).

### 2.1.3 تنسيق الضغط

يولد التخزين الكثيف للمصفوفات المتفرقة حساباً غير ضروري وهدراً للذاكرة. تعالج تنسيقات الضغط هذا القصور من خلال تخزين العناصر غير الصفرية ومواقعها فقط.

**التنسيقات الأساسية:**

- **COO (تنسيق الإحداثيات)**: يخزن فهرس الصف، وفهرس العمود، وقيمة كل عنصر غير صفري في مصفوفات منفصلة - النهج الأبسط
- **CSR (الصف المتفرق المضغوط)**: تنسيق رئيسي للصفوف يستبدل فهارس الصفوف بمؤشرات صفوف تشير إلى أول عنصر غير صفري لكل صف
- **CSC (العمود المتفرق المضغوط)**: متغير رئيسي للأعمدة يستبدل فهارس الأعمدة بمؤشرات أعمدة
- **ELL (ELLPACK)**: يضغط العناصر غير الصفرية نحو اليسار، ويخزن فهارس الأعمدة لكل عنصر غير صفري
- **DIA (تنسيق القطر)**: مصمم للمصفوفات القطرية، يخزن العناصر غير الصفرية في كل قطر مع معلومات الإزاحة

**التنسيقات المتقدمة:**

يوثق المسح العديد من التنسيقات المتخصصة المطورة لتطبيقات محددة:

- DCSC وDCSR (متغيرات مضغوطة مزدوجة) للمصفوفات فائقة التفرق، والتي تلغي تكرار المؤشرات
- BCSR (CSR المجزأ) للحساب الموزع
- HNI (إشارة غير صفرية مشفرة بهافمان) باستخدام ترميز قائم على خريطة البت
- CFM (خريطة الميزات المضغوطة) لتخزين الميزات المتفرقة للشبكات العصبية
- تمثيلات خريطة البت / قناع البت باستخدام 1 للعناصر غير الصفرية و0 بخلاف ذلك
- متغيرات RLC (مشفرة بطول التشغيل) لمصفوفات أوزان الشبكات العصبية العميقة
- بنى مبلطة للتمثيل الهرمي

## 2.2 التطبيقات النموذجية

### 2.2.1 البحث بالعرض أولاً متعدد المصادر

يشكل البحث بالعرض أولاً برنامجاً فرعياً أساسياً لتحليل الرسوم البيانية يمكّن من اكتشاف المكونات المتصلة، وتحديد أقصر مسار، وتعداد الجيران k-hop. يجتاز BFS القياسي من قمة مصدر باستخدام ضرب مصفوفة-متجه متفرق بين مصفوفة الجوار للرسم البياني 𝑨 والمتجهات المتفرقة التي تمثل المصادر.

ينفذ البحث بالعرض أولاً متعدد المصادر (MS-BFS) عمليات اجتياز مستقلة متعددة بشكل متزامن، يتم صياغتها كعمليات ضرب مصفوفات. بالنظر إلى قمم مصدر متعددة، يؤدي MS-BFS عمليات SpGEMM متتالية: أولاً حساب 𝑩¹ = 𝑨 × 𝑿 (حيث 𝑿 يمثل متجهات المصدر)، ثم 𝑩² = 𝑨 × 𝑩¹، مع التكرار حتى يتم اكتشاف جميع القمم القابلة للوصول.

يمكّن هذا النهج المتزامن من "مشاركة الحساب بين BFS مختلفة دون دفع تكلفة المزامنة"، مما يجعل تحسين SpGEMM أمراً بالغ الأهمية لتحليل الرسوم البيانية واسعة النطاق.

### 2.2.2 تجميع ماركوف (MCL)

MCL هي خوارزمية تجميع غير خاضعة للإشراف للبيانات البيولوجية التي تجمع النقاط المتصلة بشكل وثيق من خلال المشي العشوائي على سلاسل ماركوف. تتكرر الخوارزمية من خلال مراحل التوسع والتضخم:

- **مرحلة التوسع**: حساب 𝑩 = 𝑨 × 𝑨 يعزز الاتصالات ويعزز التقارب
- **خطوة التقليم**: إزالة الإدخالات أقل من عتبات محددة تحافظ على التفرق
- **مرحلة التضخم**: الأسس العنصرية تضعف ارتباطات النقاط المتصلة بشكل فضفاض

دفع العبء الحسابي والذاكرة العالي إلى تطوير HipMCL (MCL عالي الأداء) لتسريع التجميع على المنصات الموزعة.

### 2.2.3 حلالات الشبكات المتعددة الجبرية

يحل AMG أنظمة خطية متفرقة كبيرة (𝑨𝒙 = 𝒃) من خلال إنشاء تسلسلات هرمية للشبكات ومشغلات النقل تلقائياً. تتألف الطريقة من مراحل الإعداد والحل:

- **مرحلة الإعداد**: تنشئ مشغل الاستيفاء 𝑷ₗ، ومشغل التقييد 𝑹ₗ = 𝑷ₗᵀ، والنظام الخشن عبر منتج غاليركين 𝑨ₗ₊₁ = 𝑹ₗ𝑨ₗ𝑷ₗ
- **مرحلة الحل**: تهيمن عليها عملية ضرب مصفوفة-متجه متفرقة

يتضمن حساب الإعداد الحرج عمليتي SpGEMM تنفذان منتج غاليركين. تستهلك هذه العمليات "أكثر من 80٪ من إجمالي وقت البناء"، وقد تنفذ بشكل متكرر لكل خطوة زمنية في المشاكل العابرة أو غير الخطية، مما يؤسس تحسين SpGEMM كأمر أساسي لكفاءة AMG.

### 2.2.4 تطبيقات أخرى

يعمل SpGEMM كمكون حسابي بالغ الأهمية في تجميع الجينوم، وقواعد بيانات NoSQL، وعد المثلثات في الرسوم البيانية، وانكماش الرسم البياني، وخوارزميات تلوين الرسم البياني، وحسابات أقصر مسار لجميع الأزواج، ومطابقة الرسوم البيانية الفرعية، واكتشاف وعد الدورات، ومحاكاة الديناميكا الجزيئية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** COO, CSR, CSC, ELL, DIA, DCSC, DCSR, BCSR, HNI, CFM, RLC, MS-BFS, MCL, AMG, Galerkin product
- **Equations:** Multiple mathematical formulations including matrix operations, BFS iterations, and AMG setup
- **Citations:** References to Wilkinson's definition, HipMCL, and various compression formats
- **Special handling:**
  - Preserved mathematical notation (𝑨, 𝑩, 𝑪, etc.) in Arabic text
  - Kept compression format acronyms (COO, CSR, CSC, etc.) in English as standard practice
  - Translated technical terms while maintaining clarity
  - Preserved quoted text in English where appropriate

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86

### Back-Translation Validation

Section 2.1.1: The paper uses standardized mathematical notation throughout. Bold capital italics indicate matrices (𝑨, 𝑩, 𝑪), while lowercase bold italics represent vectors, and lowercase italics represent scalar values. Key symbolic representations include: 𝑨 and 𝑩 as sparse input matrices; 𝑪 as sparse output matrix; 𝒂ᵢ₊ represents row vector i from 𝑨; 𝒂₊ⱼ represents column vector j from 𝑨; p, q, r indicate matrix dimensions where 𝑨 is p×q, 𝑩 is q×r, 𝑪 is p×r; inner product (·), outer product (⊗), and general multiplication (×) operations; element-wise multiplication (∘) between matrices.

Section 2.1.2: Sparse matrices lack a universally accepted formal definition. The most widely accepted characterization comes from Wilkinson: "a sparse matrix is any matrix with enough zeros that it is beneficial to take advantage of them." An alternative quantitative approach defines matrix 𝑨 as sparse when its nonzero element count equals O(n).

Section 2.2.1: Multi-source BFS (MS-BFS) executes multiple independent traversals simultaneously, formulated as matrix multiplication operations. Given multiple source vertices, MS-BFS performs successive SpGEMM operations: first computing 𝑩¹ = 𝑨 × 𝑿 (where 𝑿 represents source vectors), then 𝑩² = 𝑨 × 𝑩¹, with iteration until all reachable vertices are discovered. This concurrent approach enables "sharing computation between different BFSs without paying synchronization cost," making SpGEMM optimization critically important for large-scale graph analysis.
