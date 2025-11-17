# Section 3: Motivation
## القسم 3: الدافع

**Section:** motivation
**Translation Quality:** 0.87
**Glossary Terms Used:** query characteristics, operator composition, filter, project, aggregate, sort, join, scalar, array, predicate, columnar I/O, Arrow IPC, CSV, JSON

---

### English Version

While COS solutions have gained attention for supporting query processing at the storage layer, their alignment with the query characteristics of real-world HPC workloads remains largely limited. The effectiveness of query offloading varies significantly depending on the types of operators involved [48], [49]. For instance, filter operations, which can substantially reduce data volume, are well-suited for execution at the storage layer. In contrast, high-complexity operations such as join incur greater computational overhead and offer limited reductions in data transfer, making them less suitable for offloading. Nevertheless, there has been little quantitative analysis of the query patterns employed in HPC workloads that process large-scale tabular data, such as those in the CFD, PIC, and HEP domains. Consequently, empirical evidence remains insufficient for evaluating the applicability and limitations of storage-based query offloading in these contexts.

## A. Query Characteristics of Tabular HPC Workloads

To quantitatively analyze the query patterns observed in HPC workloads of CFD, HEP, and PIC domains, we collected real-world queries from publicly available analytical workloads released by institutions such as CERN, LANL, and ORNL [34], [40], [50]–[52]. All collected queries operate on tabular scientific datasets. We performed a quantitative structural analysis based on the types of operators used and the ways in which they are composed.

For this analysis, we classified the queries into four categories based on their operator composition:
• **Filter:** Queries that include only simple filter predicates.
• **Filter+Agg/Sort:** Queries that combine filter with aggregate or sort operations.
• **Project:** Queries that include only project operation
• **Join:** Queries that involve complex operators such as join.

Table I summarizes the clustering results of queries across each scientific domain. In the table, **Predicate** indicates whether the data fields used in operator predicates are scalar or array-based, while **Type** distinguishes between arithmetic (Arith.) and comparison (Comp.) operations. Among all queries in the table, Filter appeared in 33 cases, Filter+Agg/Sort in 6 cases, and Project in 27 cases. Notably, there was not a single instance of a complex query involving a join operation across multiple columns. The Filter and Filter+Agg/Sort applied predicates exclusively to individual column values, while Project either selected specific columns or generated new ones through column-wise computation.

These results suggest that the majority of queries operate on a narrow set of columns, without engaging in row-wise processing over entire records. An in-depth analysis further reveals that all queries explicitly reference only the required columns, with non-essential fields excluded from computation.

Publicly available HPC queries primarily consist of simple operations centered around filter or project. This aligns with the typical usage patterns of COS systems and suggests that SQL offloading techniques such as filter pushdown can reduce data transfer and improve analytic performance. Meanwhile, as shown in the Array section of Table I, complex operator conditions frequently involve computations that go beyond simple scalar comparisons. For example, expressions such as Muon_charge[0] != Muon_charge[1] involve element-wise comparisons or computations within array-structured columns.

This analysis yields the following three key observations.

**Observation 1.** Most queries follow a column-based analytics pattern, selectively accessing only the required columns without scanning entire rows.

**Observation 2.** The core operations are concentrated on filter, project, aggregate, and sort, with no occurrence of relational operations such as join.

**Observation 3.** Predicate conditions frequently go beyond simple scalar range comparisons, often involving computations between elements within array-structured columns.

These three observations clearly articulate the core requirements for designing next-generation COS storage systems. Specifically, such systems should (i) support columnar I/O and processing, (ii) enable efficient in-storage execution of core relational operators such as filter, project, aggregate, and sort, and (iii) support predicate evaluation involving element-wise computation over array-valued columns. Satisfying these requirements is critical to fully realizing the performance advantages of compute offloading in HPC analytical workloads.

## B. Limitations of Existing COS Systems

**Limitation#1–Limited Output Formats for Columnar Semantics and Compatibility:** MinIO Select and Ceph S3 Select support filtering at the storage layer but serialize the results in a row-oriented format. This necessitates reconstructing the data into a columnar layout, during which column statistics and structural metadata are lost. As a consequence, downstream analytical engines are unable to apply optimizations such as filter skipping or projection pruning, potentially resulting in redundant reprocessing along the full query path.

SkyhookDM returns query results exclusively in the Arrow IPC format. While this preserves columnar locality, the fixed output format reduces interoperability. Engines that do not provide native support for Arrow, such as Presto [53], require an additional conversion layer, which complicates integration.

**Limitation#2–Restricted Support for SQL Operators and Array Expressions:** Current COS solutions exhibit limited operator support and lack the ability to express array-level expressions, even though HPC queries are often simple and structurally well-defined. MinIO Select and Ceph S3 Select support only simple filtering conditions, basic projection, and regular expression matching, but do not support more advanced operators such as aggregate, sort or predicate evaluation over array elements [54]. These limitations prevent the storage layer from processing queries involving array-based predicates and aggregate or sort, both of which are frequently observed in real HPC workloads. The absence of these features requires entire files or row groups to be transferred to compute nodes, resulting in significant inefficiencies.

SkyhookDM leverages Apache Arrow's compute kernels to offload filter operations, including array element indexing and arithmetic conditions. Although it supports extensibility via user-defined kernels for operations not natively available in Arrow, integrating such kernels requires recompiling the Skyhook-specific libraries within the Arrow ecosystem. This requirement limits flexibility and imposes additional overhead on users. More critically, aggregate and sort are not natively supported, and the project operator handles only direct column selection. As a result, projections involving computed expressions must be executed on the compute node. Consequently, analytical queries with advanced operators or complex array logic cannot be flexibly offloaded, reducing the overall effectiveness of storage-side computation.

**Limitation#3–Excessive Inter-Layer Data Movement Due to Fixed Execution Layer:** Existing COS systems typically support computation at only a single logical layer, which leads to structural inefficiencies. For example, systems like MinIO Select or Ceph S3 Select perform operations at the S3 interface level, requiring data to be collected from storage nodes to a gateway node that handles client S3 requests and storage backend coordination. This architecture incurs data movement bottlenecks between storage backend and the gateway. Even systems such as SkyhookDM, which execute computation at the Object Storage Daemon (OSD) level, are restricted to single-layer execution. This limitation prevents the effective use of emerging lower-tier compute resources, such as DPU-based Just a Bunch of Flash (JBOF) arrays [55], [56], whose computational capabilities remain largely underutilized.

In hierarchical storage environments, data movement occurs not only across networks but also between internal layers. Fixing computation at a single layer prevents early-stage reduction and results in excessive inter-layer data transfers. To alleviate this, computations should be initiated at lower layers closer to the data, to progressively reduce volume before reaching upper layers.

---

### النسخة العربية

بينما حظيت حلول COS باهتمام لدعم معالجة الاستعلامات في طبقة التخزين، يبقى توافقها مع خصائص استعلامات أحمال عمل HPC الحقيقية محدوداً إلى حد كبير. تختلف فعالية تفريغ الاستعلام بشكل كبير اعتماداً على أنواع المعاملات المعنية [48]، [49]. على سبيل المثال، عمليات الترشيح، التي يمكن أن تقلل بشكل كبير من حجم البيانات، مناسبة بشكل جيد للتنفيذ في طبقة التخزين. في المقابل، تتحمل العمليات عالية التعقيد مثل الضم عبئاً حسابياً أكبر وتقدم تخفيضات محدودة في نقل البيانات، مما يجعلها أقل ملاءمة للتفريغ. ومع ذلك، كان هناك القليل من التحليل الكمي لأنماط الاستعلام المستخدمة في أحمال عمل HPC التي تعالج البيانات الجدولية واسعة النطاق، مثل تلك في مجالات CFD وPIC وHEP. وبالتالي، تظل الأدلة التجريبية غير كافية لتقييم قابلية التطبيق والقيود الخاصة بتفريغ الاستعلام القائم على التخزين في هذه السياقات.

## أ. خصائص الاستعلام لأحمال العمل الجدولية في HPC

لتحليل أنماط الاستعلام الملحوظة كمياً في أحمال عمل HPC في مجالات CFD وHEP وPIC، جمعنا استعلامات حقيقية من أحمال العمل التحليلية المتاحة للعموم الصادرة عن مؤسسات مثل CERN وLANL وORNL [34]، [40]، [50]–[52]. تعمل جميع الاستعلامات المجمعة على مجموعات بيانات علمية جدولية. أجرينا تحليلاً هيكلياً كمياً بناءً على أنواع المعاملات المستخدمة والطرق التي يتم تركيبها بها.

لهذا التحليل، صنفنا الاستعلامات إلى أربع فئات بناءً على تركيبة معاملاتها:
• **الترشيح (Filter):** استعلامات تتضمن فقط محمولات ترشيح بسيطة.
• **الترشيح+التجميع/الفرز (Filter+Agg/Sort):** استعلامات تدمج الترشيح مع عمليات التجميع أو الفرز.
• **الإسقاط (Project):** استعلامات تتضمن فقط عملية الإسقاط
• **الضم (Join):** استعلامات تتضمن معاملات معقدة مثل الضم.

يلخص الجدول I نتائج تجميع الاستعلامات عبر كل مجال علمي. في الجدول، يشير **المحمول (Predicate)** إلى ما إذا كانت حقول البيانات المستخدمة في محمولات المعاملات قياسية أو قائمة على المصفوفات، بينما يميز **النوع (Type)** بين العمليات الحسابية (Arith.) والمقارنة (Comp.). من بين جميع الاستعلامات في الجدول، ظهر الترشيح في 33 حالة، والترشيح+التجميع/الفرز في 6 حالات، والإسقاط في 27 حالة. والجدير بالذكر أنه لم تكن هناك حالة واحدة لاستعلام معقد يتضمن عملية ضم عبر أعمدة متعددة. طبّق الترشيح والترشيح+التجميع/الفرز المحمولات حصرياً على قيم الأعمدة الفردية، بينما اختار الإسقاط إما أعمدة محددة أو ولّد أعمدة جديدة من خلال الحساب على مستوى الأعمدة.

تشير هذه النتائج إلى أن غالبية الاستعلامات تعمل على مجموعة ضيقة من الأعمدة، دون الانخراط في معالجة على مستوى الصفوف عبر السجلات بأكملها. يكشف التحليل المتعمق كذلك أن جميع الاستعلامات تشير صراحةً فقط إلى الأعمدة المطلوبة، مع استبعاد الحقول غير الأساسية من الحساب.

تتكون استعلامات HPC المتاحة للعموم بشكل أساسي من عمليات بسيطة تتمحور حول الترشيح أو الإسقاط. يتوافق هذا مع أنماط الاستخدام النموذجية لأنظمة COS ويشير إلى أن تقنيات تفريغ SQL مثل دفع المرشحات إلى أسفل يمكن أن تقلل من نقل البيانات وتحسن أداء التحليلات. في الوقت نفسه، كما هو موضح في قسم المصفوفات في الجدول I، تتضمن شروط المعاملات المعقدة بشكل متكرر حسابات تتجاوز المقارنات القياسية البسيطة. على سبيل المثال، تتضمن التعبيرات مثل Muon_charge[0] != Muon_charge[1] مقارنات عنصرية أو حسابات داخل أعمدة منظمة كمصفوفات.

يسفر هذا التحليل عن الملاحظات الثلاث الرئيسية التالية.

**الملاحظة 1.** تتبع معظم الاستعلامات نمط تحليلات قائم على الأعمدة، مع الوصول الانتقائي فقط إلى الأعمدة المطلوبة دون مسح صفوف كاملة.

**الملاحظة 2.** تتركز العمليات الأساسية على الترشيح والإسقاط والتجميع والفرز، دون حدوث عمليات علائقية مثل الضم.

**الملاحظة 3.** تتجاوز شروط المحمولات بشكل متكرر مقارنات النطاق القياسية البسيطة، وغالباً ما تتضمن حسابات بين العناصر داخل الأعمدة المنظمة كمصفوفات.

تُوضح هذه الملاحظات الثلاث بوضوح المتطلبات الأساسية لتصميم أنظمة تخزين COS من الجيل التالي. على وجه التحديد، يجب أن تدعم مثل هذه الأنظمة (i) الإدخال/الإخراج العمودي والمعالجة، (ii) تمكين التنفيذ الفعال داخل التخزين للمعاملات العلائقية الأساسية مثل الترشيح والإسقاط والتجميع والفرز، و(iii) دعم تقييم المحمولات الذي يتضمن حسابات عنصرية على الأعمدة ذات القيم المصفوفية. إن تلبية هذه المتطلبات أمر بالغ الأهمية لتحقيق مزايا الأداء الكاملة لتفريغ الحساب في أحمال العمل التحليلية لـ HPC.

## ب. قيود أنظمة COS الحالية

**القيد رقم 1 - تنسيقات إخراج محدودة للدلالات العمودية والتوافق:** تدعم MinIO Select وCeph S3 Select الترشيح في طبقة التخزين لكنها تُسلسل النتائج بتنسيق موجه نحو الصفوف. يتطلب هذا إعادة بناء البيانات إلى تخطيط عمودي، يتم خلاله فقدان إحصائيات الأعمدة والبيانات الوصفية الهيكلية. نتيجة لذلك، لا تستطيع محركات التحليلات اللاحقة تطبيق التحسينات مثل تخطي المرشحات أو تقليص الإسقاط، مما قد يؤدي إلى إعادة معالجة زائدة على طول مسار الاستعلام الكامل.

يُرجع SkyhookDM نتائج الاستعلام حصرياً بتنسيق Arrow IPC. بينما يحافظ هذا على الموضعية العمودية، يقلل تنسيق الإخراج الثابت من قابلية التشغيل البيني. تتطلب المحركات التي لا توفر دعماً أصلياً لـ Arrow، مثل Presto [53]، طبقة تحويل إضافية، مما يعقد التكامل.

**القيد رقم 2 - دعم مقيد لمعاملات SQL وتعبيرات المصفوفات:** تُظهر حلول COS الحالية دعماً محدوداً للمعاملات وتفتقر إلى القدرة على التعبير عن تعبيرات على مستوى المصفوفات، على الرغم من أن استعلامات HPC غالباً ما تكون بسيطة ومحددة جيداً هيكلياً. تدعم MinIO Select وCeph S3 Select فقط شروط الترشيح البسيطة، والإسقاط الأساسي، ومطابقة التعبيرات العادية، لكنها لا تدعم معاملات أكثر تقدماً مثل التجميع أو الفرز أو تقييم المحمولات على عناصر المصفوفات [54]. تمنع هذه القيود طبقة التخزين من معالجة الاستعلامات التي تتضمن محمولات قائمة على المصفوفات والتجميع أو الفرز، وكلاهما يُلاحظ بشكل متكرر في أحمال عمل HPC الحقيقية. يتطلب غياب هذه الميزات نقل ملفات كاملة أو مجموعات صفوف إلى عقد الحساب، مما ينتج عنه عدم كفاءة كبيرة.

يستفيد SkyhookDM من نوى حساب Apache Arrow لتفريغ عمليات الترشيح، بما في ذلك فهرسة عناصر المصفوفة والشروط الحسابية. على الرغم من أنه يدعم قابلية التوسع عبر نوى معرّفة من قبل المستخدم للعمليات غير المتاحة بشكل أصلي في Arrow، فإن دمج مثل هذه النوى يتطلب إعادة تجميع مكتبات Skyhook المحددة ضمن نظام Arrow البيئي. يحد هذا المطلب من المرونة ويفرض عبئاً إضافياً على المستخدمين. والأكثر أهمية، أن التجميع والفرز غير مدعومين بشكل أصلي، ومعامل الإسقاط يتعامل فقط مع اختيار الأعمدة المباشر. نتيجة لذلك، يجب تنفيذ الإسقاطات التي تتضمن تعبيرات محسوبة على عقدة الحساب. وبالتالي، لا يمكن تفريغ الاستعلامات التحليلية مع معاملات متقدمة أو منطق مصفوفات معقد بمرونة، مما يقلل من الفعالية الإجمالية للحساب من جانب التخزين.

**القيد رقم 3 - حركة بيانات مفرطة بين الطبقات بسبب طبقة التنفيذ الثابتة:** تدعم أنظمة COS الحالية عادةً الحساب في طبقة منطقية واحدة فقط، مما يؤدي إلى عدم كفاءة هيكلية. على سبيل المثال، تنفذ الأنظمة مثل MinIO Select أو Ceph S3 Select العمليات على مستوى واجهة S3، مما يتطلب جمع البيانات من عقد التخزين إلى عقدة بوابة تتعامل مع طلبات S3 من العملاء وتنسيق الواجهة الخلفية للتخزين. تتحمل هذه المعمارية اختناقات حركة البيانات بين الواجهة الخلفية للتخزين والبوابة. حتى الأنظمة مثل SkyhookDM، التي تنفذ الحساب على مستوى خدمة تخزين الكائنات (OSD)، مقيدة بالتنفيذ أحادي الطبقة. يمنع هذا القيد الاستخدام الفعال لموارد الحساب من الطبقة السفلى الناشئة، مثل مصفوفات JBOF القائمة على DPU [55]، [56]، التي تظل قدراتها الحسابية غير مستغلة إلى حد كبير.

في بيئات التخزين الهرمية، تحدث حركة البيانات ليس فقط عبر الشبكات ولكن أيضاً بين الطبقات الداخلية. يمنع تثبيت الحساب في طبقة واحدة التقليل في مرحلة مبكرة وينتج عنه عمليات نقل بيانات مفرطة بين الطبقات. للتخفيف من ذلك، يجب بدء الحسابات في الطبقات السفلى الأقرب إلى البيانات، لتقليل الحجم تدريجياً قبل الوصول إلى الطبقات العليا.

---

### Translation Notes

- **Tables referenced:** Table I
- **Key terms introduced:** query characteristics, operator composition, scalar vs array predicates, columnar I/O, Arrow IPC, filter pushdown, DPU, JBOF
- **Equations:** None
- **Citations:** [34], [40], [48]-[56] referenced
- **Special handling:**
  - Technical terms like "filter", "project", "aggregate", "sort", "join" kept consistent with glossary
  - Array-based expressions kept with original syntax (e.g., Muon_charge[0])
  - Product names kept in English (MinIO Select, Ceph S3 Select, SkyhookDM, Presto)
  - Acronyms kept in English (DPU, JBOF, OSD, IPC)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
