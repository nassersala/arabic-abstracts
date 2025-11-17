# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** distributed data processing, Apache Spark, HPC, CFD, HEP, PIC, data movement, POSIX, columnar layout, computation-enabled object storage, filter, project, aggregate, query offloading

---

### English Version

In modern scientific research, vast amounts of data are generated through simulations and experiments in domains such as Computational Fluid Dynamics (CFD), High-Energy Physics (HEP), and Particle-In-Cell (PIC) simulations. These datasets are typically structured in tabular formats with well-defined schemas, where each record–such as a CFD cell or particle–contains a consistent set of fields [1]–[4]. This tabular structure aligns well with the relational model, enabling researchers to perform post hoc analysis using SQL-style queries (§II-A) [5]. To support scalable analysis of such large datasets, distributed data processing frameworks–most notably Apache Spark [6]–have been widely adopted on High-Performance Computing (HPC) systems for scientific data analytics [7], [8].

Meanwhile, recent advances in HPC simulations and scientific instrumentation have further accelerated data growth, placing increasing pressure on analytics systems to keep pace [9]. For example, supercomputers such as Frontier [10] at Oak Ridge National Laboratory (ORNL) enable massive simulations that produce structured outputs across thousands of timesteps. Likewise, facilities like the High-Luminosity Large Hadron Collider (HL-LHC) [11] substantially increase data acquisition rates through enhanced detector resolution and higher event frequency. As data volumes continue to grow, their rate of increase is rapidly outpacing improvements in I/O and network bandwidth, leading to two key challenges:

**First**, data movement has become a major bottleneck in HPC analytics, exacerbated not only by increasing data volumes but also by low-selectivity queries that focus on narrow regions of interest (§II-B). While processing power has advanced for large-scale post-hoc analysis, storage I/O has not kept pace, causing transfer delays, idle compute nodes, and reduced system efficiency [12]–[15].

**Second**, traditional POSIX-based file systems struggle with efficient data placement at scale [16]. Their flat byte-stream model lacks structural awareness, making it difficult to selectively place hot columns on fast storage. This often results in hot data being placed on slow storage or in fast-tier overuse, degrading I/O performance [17]. These limitations highlight the need for storage systems that minimize data movement and support column-aware layout (§II-C).

To address these challenges, Computation-Enabled Object Storage (COS) systems–such as MinIO [18], Ceph [19] with S3 Select [20], and Ceph with SkyhookDM support [21]–have emerged as promising solutions that augment object storage with lightweight computation at the storage layer (§II-D) [21]–[25]. These systems can perform filter and project operations near the data, mitigating data movement bottlenecks in HPC environments. COS also improves data placement by supporting column-level granularity through its object abstraction, enabling selective tiering based on access frequency. This addresses the data placement limitations of POSIX systems and aligns data layout with workload behavior.

To enable compute offloading to storage, COS systems are designed following two distinct architectural approaches: executing query operations at the interface layer (e.g., Ceph S3 Select [23], MinIO Select [22]), or embedding computation within the internal layers of the storage stack (e.g., SkyhookDM [21]). While these systems differ in their offloading mechanisms, they share common limitations that hinder support for complex, high-throughput analytics. These limitations stem from architectural constraints and limited expressiveness in query execution, and are summarized as follows (§III-B).

• **Inflexible Output Format Limits Optimization and Integration:** Existing COS systems return offloaded query results in fixed output formats such as CSV and JSON, which lack structural metadata and require additional parsing, or Apache Arrow [26], which offers efficient columnar access but is not universally supported by all analytics engines.

• **Limited Offloading Capability for Various Operators and Array Semantics:** Most existing COS systems support only filter and project operations with scalar conditions, lacking essential advanced operators such as aggregate and array-based expressions common in HPC queries (§III-A). As a result, for queries involving such unsupported operators or array-based conditions, COS systems still need to transfer entire files or row groups to the compute layer, increasing data movement and slowing analysis.

• **Excessive Inter-Storage Data Movement Due to Fixed Execution Layer:** Current COS systems execute queries at a single fixed layer, such as the gateway node that interfaces with compute clients, and thus fail to minimize internal data transfers. This inflexible design prevents early-stage data reduction in lower layers of the storage stack, such as storage array nodes, thus limiting the benefits of offloading.

To overcome the aforementioned limitations, we propose OASIS, a new COS system designed for analytical workflows in HPC environments (§IV-A). OASIS is composed of a frontend node (OASIS-FE) as a object interface gateway and multiple storage arrays (OASIS-A), interconnected via high-speed NVMe-over-Fabrics (NVMe-oF) over RDMA (§IV-B).

OASIS implements the following key features: **First**, OASIS generates both intermediate and final results of offloaded query execution in the Arrow columnar format, within storage nodes and during transmission to compute nodes. This design reduces serialization overhead and enables efficient data exchange across system layers. Final outputs can also be serialized in CSV or JSON format for compatibility with legacy tools. **Second**, OASIS provides advanced operators such as aggregation, sorting, and array-level computations, including element-wise arithmetic and conditional evaluation. These operations are executed directly by the storage-layer Query Executor, which is implemented using DuckDB [27] due to its lightweight design, embeddability, and support for complex SQL semantics that align well with OASIS's core requirements (§IV-E). **Third**, OASIS deploys Query Executors on both the OASIS-FE and the OASIS-A. It then employs a Local Optimizer that analyzes the offloaded query plan and applies the Storage-side Query Plan Offloading and Decomposition Algorithm (SODA) to partition the plan into subplans for distributed execution across the OASIS-FE and OASIS-A nodes (§IV-F).

Based on operator characteristics, SODA selects between two decomposition strategies (§IV-G): (1) Coefficient-Aware Decomposition (CAD) and (2) Structure-Aware Placement (SAP). CAD applies to queries with scalar comparisons or simple scalar computations, where data movement can be reasonably estimated using precomputed statistics. It identifies a partitioning point that minimizes total data movement based on estimated input-output ratios. In contrast, SAP targets queries for which data movement is difficult to estimate by statistics, such as those with array-level conditions or computations. SAP executes these operators close to the data and employs a lazy strategy. Specifically, it measures intermediate result sizes at runtime and forwards results to upper layers only when they fit within available internal bandwidth.

Figure 1 compares the storage architecture of OASIS with that of existing COS solutions. While existing COS systems reduce storage-to-compute data transfers by executing queries at the gateway layer within the storage system, they still incur substantial internal data movement across layers. In contrast, OASIS minimizes both inter-layer and storage-to-compute data transfers by initiating early-stage query processing in lower storage layers, guided by data movement cost.

We implemented a prototype of OASIS by building key components on SPDK v23.09 and DuckDB v1.3.0, where DuckDB serves as the in-storage Query Executor deployed across OASIS-FE and OASIS-A. We integrated OASIS with Apache Spark 4.0.0 to support query offloading. Our evaluation was conducted on a multi-node Spark cluster and an RDMA-connected OASIS setup, comprising 36–112 core servers with up to 386 GB of memory.

We evaluated OASIS using a diverse set of real-world analytical queries from representative workflows, including CFD and HEP domains. Evaluation results show that OASIS achieves up to 70.59% speedup over the traditional storage system and up to 32.7% speed up compared to existing COS-based setups. Furthermore, the SODA demonstrated its effectiveness in minimizing query execution time by optimally partitioning the query plan for complex queries composed of multiple operators (e.g., Q1 in Table IV).

**In summary, our key contributions are as follows:**

• We collect and analyze real-world tabular queries from HPC workflows in domains such as CFD, HEP, and PIC, with a focus on identifying operator patterns and structural traits that impact data movement and offloading opportunities.

• We design and implement OASIS, a novel object-based, computation-enabled analytical storage system that supports columnar formats, advanced operators with array-level expressions, and dataflow-aware query path optimization across hierarchical internal storage layers.

• We propose SODA, a query decomposition mechanism that partitions full offloaded query plans into subplans for hierarchical internal storage layers of OASIS-FE and OASIS-A. It applies CAD for scalar-centric workloads and SAP for array-centric workloads to enable efficient offloading.

---

### النسخة العربية

في البحث العلمي الحديث، يتم توليد كميات هائلة من البيانات من خلال المحاكاة والتجارب في مجالات مثل ديناميكا الموائع الحسابية (CFD)، وفيزياء الطاقة العالية (HEP)، ومحاكاة الجسيمات في الخلايا (PIC). عادةً ما تكون مجموعات البيانات هذه منظمة بتنسيقات جدولية ذات مخططات محددة جيداً، حيث يحتوي كل سجل - مثل خلية CFD أو جسيم - على مجموعة ثابتة من الحقول [1]–[4]. يتوافق هذا الهيكل الجدولي بشكل جيد مع النموذج العلائقي، مما يمكّن الباحثين من إجراء تحليل لاحق باستخدام استعلامات بأسلوب SQL (§II-A) [5]. لدعم التحليل القابل للتوسع لمجموعات البيانات الكبيرة هذه، تم اعتماد أطر معالجة البيانات الموزعة - وأبرزها Apache Spark [6] - على نطاق واسع في أنظمة الحوسبة عالية الأداء (HPC) لتحليلات البيانات العلمية [7]، [8].

في الوقت نفسه، أدت التطورات الأخيرة في محاكاة HPC والأجهزة العلمية إلى تسريع نمو البيانات بشكل أكبر، مما يضع ضغطاً متزايداً على أنظمة التحليلات لمواكبة هذا النمو [9]. على سبيل المثال، تتيح الحواسيب الفائقة مثل Frontier [10] في مختبر أوك ريدج الوطني (ORNL) محاكاة ضخمة تنتج مخرجات منظمة عبر آلاف الخطوات الزمنية. وبالمثل، تزيد المنشآت مثل مصادم الهادرونات الكبير عالي الإضاءة (HL-LHC) [11] بشكل كبير من معدلات اكتساب البيانات من خلال دقة محسّنة للكاشفات وتكرار أعلى للأحداث. مع استمرار نمو أحجام البيانات، فإن معدل زيادتها يتجاوز بسرعة التحسينات في عرض نطاق الإدخال/الإخراج والشبكة، مما يؤدي إلى تحديين رئيسيين:

**أولاً**، أصبحت حركة البيانات عائقاً رئيسياً في تحليلات HPC، تفاقمت ليس فقط بسبب تزايد أحجام البيانات ولكن أيضاً بسبب الاستعلامات منخفضة الانتقائية التي تركز على مناطق ضيقة محل الاهتمام (§II-B). بينما تقدمت قوة المعالجة للتحليل اللاحق واسع النطاق، لم تواكب إدخال/إخراج التخزين هذا التقدم، مما يسبب تأخيرات في النقل، وعقد حاسوبية خاملة، وانخفاض كفاءة النظام [12]–[15].

**ثانياً**، تكافح أنظمة الملفات التقليدية القائمة على POSIX مع وضع البيانات الفعال على نطاق واسع [16]. يفتقر نموذجها المسطح لتدفق البايتات إلى الوعي الهيكلي، مما يجعل من الصعب وضع الأعمدة الساخنة بشكل انتقائي على التخزين السريع. غالباً ما يؤدي هذا إلى وضع البيانات الساخنة على التخزين البطيء أو الإفراط في استخدام الطبقة السريعة، مما يُدهور أداء الإدخال/الإخراج [17]. تسلط هذه القيود الضوء على الحاجة إلى أنظمة تخزين تقلل من حركة البيانات وتدعم التخطيط الواعي بالأعمدة (§II-C).

لمعالجة هذه التحديات، ظهرت أنظمة تخزين الكائنات الممكّنة حسابياً (COS) - مثل MinIO [18]، وCeph [19] مع S3 Select [20]، وCeph مع دعم SkyhookDM [21] - كحلول واعدة تعزز تخزين الكائنات بحساب خفيف الوزن في طبقة التخزين (§II-D) [21]–[25]. يمكن لهذه الأنظمة تنفيذ عمليات الترشيح والإسقاط بالقرب من البيانات، مما يخفف من اختناقات حركة البيانات في بيئات HPC. يُحسّن COS أيضاً وضع البيانات من خلال دعم الدقة على مستوى الأعمدة من خلال تجريد الكائنات الخاص به، مما يتيح التدريج الانتقائي بناءً على تكرار الوصول. يعالج هذا قيود وضع البيانات في أنظمة POSIX ويوائم تخطيط البيانات مع سلوك حمل العمل.

لتمكين تفريغ الحساب إلى التخزين، تم تصميم أنظمة COS باتباع نهجين معماريين متميزين: تنفيذ عمليات الاستعلام في طبقة الواجهة (مثل Ceph S3 Select [23]، وMinIO Select [22])، أو تضمين الحساب ضمن الطبقات الداخلية لمكدس التخزين (مثل SkyhookDM [21]). بينما تختلف هذه الأنظمة في آليات التفريغ الخاصة بها، فإنها تشترك في قيود مشتركة تعيق دعم التحليلات المعقدة عالية الإنتاجية. تنبع هذه القيود من القيود المعمارية والتعبيرية المحدودة في تنفيذ الاستعلامات، ويمكن تلخيصها على النحو التالي (§III-B).

• **تنسيق الإخراج غير المرن يحد من التحسين والتكامل:** تُرجع أنظمة COS الحالية نتائج الاستعلامات المفرغة بتنسيقات إخراج ثابتة مثل CSV وJSON، التي تفتقر إلى البيانات الوصفية الهيكلية وتتطلب تحليلاً إضافياً، أو Apache Arrow [26]، الذي يوفر وصولاً عمودياً فعالاً ولكنه غير مدعوم عالمياً من قبل جميع محركات التحليلات.

• **قدرة تفريغ محدودة لمعاملات متنوعة ودلالات المصفوفات:** تدعم معظم أنظمة COS الحالية فقط عمليات الترشيح والإسقاط مع شروط قياسية، وتفتقر إلى المعاملات المتقدمة الأساسية مثل التجميع والتعبيرات القائمة على المصفوفات الشائعة في استعلامات HPC (§III-A). نتيجة لذلك، بالنسبة للاستعلامات التي تتضمن مثل هذه المعاملات غير المدعومة أو الشروط القائمة على المصفوفات، لا تزال أنظمة COS بحاجة إلى نقل ملفات كاملة أو مجموعات صفوف إلى طبقة الحساب، مما يزيد من حركة البيانات ويبطئ التحليل.

• **حركة بيانات مفرطة بين التخزين بسبب طبقة التنفيذ الثابتة:** تنفذ أنظمة COS الحالية الاستعلامات في طبقة واحدة ثابتة، مثل عقدة البوابة التي تتواصل مع عملاء الحساب، وبالتالي تفشل في تقليل عمليات النقل الداخلية للبيانات. يمنع هذا التصميم غير المرن تقليل البيانات في مرحلة مبكرة في الطبقات السفلى من مكدس التخزين، مثل عقد مصفوفة التخزين، مما يحد من فوائد التفريغ.

للتغلب على القيود المذكورة أعلاه، نقترح OASIS، وهو نظام COS جديد مصمم لسير العمل التحليلي في بيئات HPC (§IV-A). يتكون OASIS من عقدة أمامية (OASIS-FE) كبوابة واجهة كائنات ومصفوفات تخزين متعددة (OASIS-A)، مترابطة عبر NVMe-over-Fabrics (NVMe-oF) عالي السرعة عبر RDMA (§IV-B).

ينفذ OASIS الميزات الرئيسية التالية: **أولاً**، يولد OASIS كلاً من النتائج الوسيطة والنهائية لتنفيذ الاستعلام المفرغ بتنسيق Arrow العمودي، داخل عقد التخزين وأثناء النقل إلى عقد الحساب. يقلل هذا التصميم من عبء التسلسل ويمكّن تبادل البيانات الفعال عبر طبقات النظام. يمكن أيضاً تسلسل المخرجات النهائية بتنسيق CSV أو JSON للتوافق مع الأدوات القديمة. **ثانياً**، يوفر OASIS معاملات متقدمة مثل التجميع والفرز والحسابات على مستوى المصفوفات، بما في ذلك الحساب العنصري والتقييم الشرطي. يتم تنفيذ هذه العمليات مباشرة بواسطة منفذ الاستعلام في طبقة التخزين، الذي يتم تنفيذه باستخدام DuckDB [27] نظراً لتصميمه الخفيف الوزن، وقابليته للتضمين، ودعمه لدلالات SQL المعقدة التي تتوافق بشكل جيد مع المتطلبات الأساسية لـ OASIS (§IV-E). **ثالثاً**، ينشر OASIS منفذي استعلامات على كل من OASIS-FE وOASIS-A. ثم يستخدم محسّناً محلياً يحلل خطة الاستعلام المفرغة ويطبق خوارزمية تفريغ وتحليل خطة الاستعلام من جانب التخزين (SODA) لتقسيم الخطة إلى خطط فرعية للتنفيذ الموزع عبر عقد OASIS-FE وOASIS-A (§IV-F).

بناءً على خصائص المعاملات، يختار SODA بين استراتيجيتي تحليل (§IV-G): (1) التحليل الواعي بالمعامل (CAD) و(2) الوضع الواعي بالبنية (SAP). ينطبق CAD على الاستعلامات ذات المقارنات القياسية أو الحسابات القياسية البسيطة، حيث يمكن تقدير حركة البيانات بشكل معقول باستخدام الإحصائيات المحسوبة مسبقاً. يحدد نقطة تقسيم تقلل من إجمالي حركة البيانات بناءً على نسب الإدخال-الإخراج المقدرة. في المقابل، يستهدف SAP الاستعلامات التي يصعب فيها تقدير حركة البيانات بالإحصائيات، مثل تلك ذات الشروط أو الحسابات على مستوى المصفوفات. ينفذ SAP هذه المعاملات بالقرب من البيانات ويستخدم استراتيجية كسولة. على وجه التحديد، يقيس أحجام النتائج الوسيطة في وقت التشغيل ويُحوّل النتائج إلى الطبقات العليا فقط عندما تتناسب مع عرض النطاق الداخلي المتاح.

يقارن الشكل 1 معمارية التخزين لـ OASIS مع حلول COS الحالية. بينما تقلل أنظمة COS الحالية من عمليات نقل البيانات من التخزين إلى الحساب من خلال تنفيذ الاستعلامات في طبقة البوابة داخل نظام التخزين، فإنها لا تزال تتحمل حركة بيانات داخلية كبيرة عبر الطبقات. في المقابل، يقلل OASIS من كل من النقل بين الطبقات والنقل من التخزين إلى الحساب من خلال بدء معالجة الاستعلامات في مرحلة مبكرة في طبقات التخزين السفلى، موجهة بتكلفة حركة البيانات.

قمنا بتنفيذ نموذج أولي لـ OASIS من خلال بناء المكونات الرئيسية على SPDK v23.09 وDuckDB v1.3.0، حيث يعمل DuckDB كمنفذ استعلام داخل التخزين منتشر عبر OASIS-FE وOASIS-A. دمجنا OASIS مع Apache Spark 4.0.0 لدعم تفريغ الاستعلامات. تم إجراء تقييمنا على مجموعة Spark متعددة العقد وإعداد OASIS متصل بـ RDMA، يتألف من خوادم 36-112 نواة مع ذاكرة تصل إلى 386 جيجابايت.

قيّمنا OASIS باستخدام مجموعة متنوعة من الاستعلامات التحليلية الحقيقية من سير العمل التمثيلية، بما في ذلك مجالات CFD وHEP. تُظهر نتائج التقييم أن OASIS يحقق تسريعاً يصل إلى 70.59٪ مقارنة بنظام التخزين التقليدي وتسريعاً يصل إلى 32.7٪ مقارنة بإعدادات COS الحالية. علاوة على ذلك، أثبتت SODA فعاليتها في تقليل وقت تنفيذ الاستعلام من خلال تقسيم خطة الاستعلام على النحو الأمثل للاستعلامات المعقدة المكونة من معاملات متعددة (مثل Q1 في الجدول IV).

**باختصار، مساهماتنا الرئيسية هي كما يلي:**

• نجمع ونحلل استعلامات جدولية حقيقية من سير عمل HPC في مجالات مثل CFD وHEP وPIC، مع التركيز على تحديد أنماط المعاملات والسمات الهيكلية التي تؤثر على حركة البيانات وفرص التفريغ.

• نصمم وننفذ OASIS، وهو نظام تخزين تحليلي جديد قائم على الكائنات وممكّن حسابياً يدعم التنسيقات العمودية، والمعاملات المتقدمة مع تعبيرات على مستوى المصفوفات، وتحسين مسار الاستعلام الواعي بتدفق البيانات عبر طبقات التخزين الداخلية الهرمية.

• نقترح SODA، وهي آلية تحليل استعلام تقسم خطط الاستعلام المفرغة الكاملة إلى خطط فرعية لطبقات التخزين الداخلية الهرمية لـ OASIS-FE وOASIS-A. تطبق CAD لأحمال العمل التي تركز على القياسية وSAP لأحمال العمل التي تركز على المصفوفات لتمكين التفريغ الفعال.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** CFD, HEP, PIC, POSIX, SkyhookDM, NVMe-oF, RDMA, SODA, CAD, SAP, DuckDB
- **Equations:** None
- **Citations:** [1]-[27] referenced in this section
- **Special handling:**
  - Technical acronyms kept in English (CFD, HEP, PIC, POSIX, NVMe-oF, RDMA, SODA, CAD, SAP)
  - Software names kept in English (Apache Spark, MinIO, Ceph, S3 Select, SkyhookDM, DuckDB, SPDK)
  - Facility names kept in English (ORNL, HL-LHC, Frontier)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
