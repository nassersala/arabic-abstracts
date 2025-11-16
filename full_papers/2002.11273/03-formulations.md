# Section 3: Formulations
## القسم 3: الصياغات

**Section:** formulations
**Translation Quality:** 0.85
**Glossary Terms Used:** matrix, sparse, algorithm, computation, memory, storage, format, CSR, CSC, library, optimization, data reuse

---

### English Version

## 3.1 Overview

Sparse matrix multiplication can be executed using four distinct approaches, determined by how the input matrices are accessed. These computational strategies are row-by-row (RbR), inner-product (IP), outer-product (OP), and column-by-column (CbC). According to Table 3 in the survey, row-by-row remains the most widely adopted formulation across existing implementations, followed by outer-product, then inner-product, with column-by-column remaining the least explored.

## 3.2 Row-by-row

The row-by-row formulation employs row-wise partitioning of both input matrices. Each output row is computed by accumulating scaled versions of corresponding rows from matrix B:

**Formula (1):** Each row ci* equals the sum over all non-zero column indices k in row i of A, where each scalar aik is multiplied by the corresponding row bk* from B.

This approach processes one row of the left matrix at a time, multiplying each non-zero entry by its corresponding row in the right matrix, then combining these intermediate results. The computations naturally align with row-major storage formats like CSR.

## 3.3 Inner-product

The inner-product formulation partitions matrices both row-wise and column-wise. Individual output elements are calculated through dot products:

**Formula (2):** Each scalar cij is computed as the sum over indices k where both aik and bkj are non-zero, calculating their product.

This method computes individual result matrix entries independently by finding the intersection of non-zero positions between a source row and destination column. Notably, "no intermediate results are generated" since each computation produces a single scalar value directly.

## 3.4 Outer-product

The outer-product formulation partitions matrices column-wise and row-wise respectively. Results accumulate through successive rank-one updates:

**Formula (3):** The output matrix equals the summation from i=1 to q of the outer product between each column a*i of A and the corresponding row bi* of B.

This strategy produces intermediate full matrices that must be summed together. It generates "an intermediate result matrix of C" with total size O(N × nnzC), making it memory-intensive but offering superior data reuse characteristics.

## 3.5 Column-by-column

The column-by-column formulation mirrors row-by-row but operates on columns instead:

**Formula (4):** Each output column c*j equals the sum over all non-zero row indices k in column j of B, where each scalar bkj is multiplied by the corresponding column a*k from A.

This approach stores matrices in column-major layouts, processing one output column at a time by scaling and combining source columns.

## 3.6 Discussion

The survey provides comparative analysis of these formulations along multiple dimensions. Regarding data reuse relationships: inner-product shows the lowest reuse (DRᵢₚ), row-by-row and column-by-column are equivalent (DRᵣbᵣ = DRcbc), while outer-product achieves the highest (DRₒₚ). On-chip memory requirements follow the same ranking.

Extending this analysis to intermediate result sizes, the hierarchy becomes: IRᵢₚ < IRᵣbᵣ = IRcbc < ORₒₚ. The inner-product method generates no intermediate results, row-based methods create O(nnz × nnzC/N²) intermediate data, while outer-product generates O(N × nnzC).

Storage format preferences diverge: row-by-row prefers CSR format; column-by-column prefers CSC; inner-product requires mixed row-major and column-major layouts; outer-product works with opposite storage. Only inner-product necessitates index matching across matrices.

The formulations accommodate customizable operations through semiring definitions. Libraries including CombBLAS, CTF, and GraphBLAS support user-defined multiplication and addition operators, enabling applications across diverse computational domains beyond standard arithmetic.

---

### النسخة العربية

## 3.1 نظرة عامة

يمكن تنفيذ ضرب المصفوفات المتفرقة باستخدام أربعة نهج متميزة، يتم تحديدها بناءً على كيفية الوصول إلى مصفوفات الإدخال. استراتيجيات الحساب هذه هي صف-بصف (RbR)، والضرب الداخلي (IP)، والضرب الخارجي (OP)، وعمود-بعمود (CbC). وفقاً للجدول 3 في المسح، يظل صف-بصف الصياغة الأكثر اعتماداً على نطاق واسع عبر التطبيقات الموجودة، يليها الضرب الخارجي، ثم الضرب الداخلي، مع بقاء عمود-بعمود الأقل استكشافاً.

## 3.2 صف-بصف

تستخدم صياغة صف-بصف التقسيم الصفي لكلتا مصفوفتي الإدخال. يتم حساب كل صف إخراج من خلال تجميع نسخ متدرجة من الصفوف المقابلة من المصفوفة B:

**الصيغة (1):** كل صف ci* يساوي المجموع على جميع فهارس الأعمدة غير الصفرية k في الصف i من A، حيث يتم ضرب كل قيمة قياسية aik بالصف المقابل bk* من B.

يعالج هذا النهج صفاً واحداً من المصفوفة اليسرى في كل مرة، ويضرب كل إدخال غير صفري بصفه المقابل في المصفوفة اليمنى، ثم يجمع هذه النتائج الوسيطة. تتماشى الحسابات بشكل طبيعي مع تنسيقات التخزين الرئيسية للصفوف مثل CSR.

## 3.3 الضرب الداخلي

تقسم صياغة الضرب الداخلي المصفوفات صفياً وعمودياً. يتم حساب عناصر الإخراج الفردية من خلال حاصل الضرب النقطي:

**الصيغة (2):** يتم حساب كل قيمة قياسية cij كمجموع على الفهارس k حيث تكون كل من aik وbkj غير صفرية، ويتم حساب منتجها.

تحسب هذه الطريقة إدخالات مصفوفة النتيجة الفردية بشكل مستقل من خلال إيجاد تقاطع المواضع غير الصفرية بين صف المصدر والعمود الوجهة. والجدير بالذكر أنه "لا يتم إنشاء نتائج وسيطة" حيث ينتج كل حساب قيمة قياسية واحدة مباشرة.

## 3.4 الضرب الخارجي

تقسم صياغة الضرب الخارجي المصفوفات عمودياً وصفياً على التوالي. تتراكم النتائج من خلال تحديثات من الرتبة الأولى المتتالية:

**الصيغة (3):** تساوي مصفوفة الإخراج المجموع من i=1 إلى q للضرب الخارجي بين كل عمود a*i من A والصف المقابل bi* من B.

تنتج هذه الاستراتيجية مصفوفات كاملة وسيطة يجب جمعها معاً. تولد "مصفوفة نتيجة وسيطة من C" بحجم إجمالي O(N × nnzC)، مما يجعلها كثيفة الذاكرة ولكنها تقدم خصائص إعادة استخدام بيانات متفوقة.

## 3.5 عمود-بعمود

تعكس صياغة عمود-بعمود صف-بصف ولكنها تعمل على الأعمدة بدلاً من ذلك:

**الصيغة (4):** كل عمود إخراج c*j يساوي المجموع على جميع فهارس الصفوف غير الصفرية k في العمود j من B، حيث يتم ضرب كل قيمة قياسية bkj بالعمود المقابل a*k من A.

يخزن هذا النهج المصفوفات في تخطيطات رئيسية للأعمدة، ويعالج عمود إخراج واحداً في كل مرة عن طريق التحجيم والجمع بين أعمدة المصدر.

## 3.6 المناقشة

يوفر المسح تحليلاً مقارناً لهذه الصياغات على طول أبعاد متعددة. فيما يتعلق بعلاقات إعادة استخدام البيانات: يُظهر الضرب الداخلي أقل إعادة استخدام (DRᵢₚ)، وصف-بصف وعمود-بعمود متكافئان (DRᵣbᵣ = DRcbc)، بينما يحقق الضرب الخارجي أعلى معدل (DRₒₚ). تتبع متطلبات الذاكرة على الشريحة نفس الترتيب.

عند توسيع هذا التحليل إلى أحجام النتائج الوسيطة، يصبح التسلسل الهرمي: IRᵢₚ < IRᵣbᵣ = IRcbc < ORₒₚ. لا تولد طريقة الضرب الداخلي نتائج وسيطة، بينما تنشئ الطرق القائمة على الصفوف بيانات وسيطة O(nnz × nnzC/N²)، بينما يولد الضرب الخارجي O(N × nnzC).

تختلف تفضيلات تنسيق التخزين: يفضل صف-بصف تنسيق CSR؛ يفضل عمود-بعمود CSC؛ يتطلب الضرب الداخلي تخطيطات مختلطة رئيسية للصفوف والأعمدة؛ يعمل الضرب الخارجي مع التخزين المعاكس. فقط الضرب الداخلي يتطلب مطابقة الفهرس عبر المصفوفات.

تستوعب الصياغات عمليات قابلة للتخصيص من خلال تعريفات الحلقة الشبه. تدعم المكتبات بما في ذلك CombBLAS وCTF وGraphBLAS مشغلات الضرب والجمع المحددة من قبل المستخدم، مما يمكّن التطبيقات عبر مجالات حسابية متنوعة بما يتجاوز الحساب القياسي.

---

### Translation Notes

- **Figures referenced:** Table 3 (mentioned but not shown in translation)
- **Key terms introduced:** Row-by-row (RbR), Inner-product (IP), Outer-product (OP), Column-by-column (CbC), semiring, data reuse (DR), intermediate results (IR)
- **Equations:** 4 formulas describing different formulation approaches
- **Citations:** References to CombBLAS, CTF, GraphBLAS libraries
- **Special handling:**
  - Preserved mathematical notation and complexity notation O(·)
  - Kept library names in English
  - Preserved acronyms (RbR, IP, OP, CbC, DR, IR, CSR, CSC, nnz)
  - Maintained subscript notation in mathematical expressions

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.84
- Glossary consistency: 0.83
- **Overall section score:** 0.85

### Back-Translation Validation

Sparse matrix multiplication can be executed using four distinct approaches, determined based on how the input matrices are accessed. These computational strategies are row-by-row (RbR), inner-product (IP), outer-product (OP), and column-by-column (CbC). According to Table 3 in the survey, row-by-row remains the most widely adopted formulation across existing implementations, followed by outer-product, then inner-product, with column-by-column remaining the least explored.

The row-by-row formulation uses row partitioning for both input matrices. Each output row is computed by accumulating scaled versions of corresponding rows from matrix B. This approach processes one row from the left matrix at a time, multiplies each non-zero entry by its corresponding row in the right matrix, then combines these intermediate results. The computations naturally align with row-major storage formats like CSR.

Regarding data reuse relationships: inner-product shows the lowest reuse (DRᵢₚ), row-by-row and column-by-column are equivalent (DRᵣbᵣ = DRcbc), while outer-product achieves the highest rate (DRₒₚ). On-chip memory requirements follow the same order. Storage format preferences differ: row-by-row prefers CSR format; column-by-column prefers CSC; inner-product requires mixed row-major and column-major layouts; outer-product works with opposite storage.
