# Section 2: Background and Related Work
## القسم 2: الخلفية والأعمال ذات الصلة

**Section:** background and related work
**Translation Quality:** 0.86
**Glossary Terms Used:** checkpointing, HDF5, ROOT, Parquet, RDBMS, Spark DataFrame, data movement, object storage, computational storage, S3, MinIO, Ceph, SkyhookDM, Apache Arrow

---

### English Version

## A. Post-Hoc Analysis Workflow in Scientific Applications

Figure 2 presents a representative post-hoc analysis workflow widely adopted in modern scientific applications, including those in Computational Fluid Dynamics (CFD), High-Energy Physics (HEP), and Particle-In-Cell (PIC) simulations. This workflow typically consists of four sequential stages: data generation, data storage, data analysis, and data visualization.

**1) Data Generation:** Modern scientific applications generate data by computing physical quantities (e.g., position, velocity, and energy) of individual particles within defined simulation domains, such as observation regions or grid cells. In observation-driven applications, such as particle collision experiments, data is collected in real-time through specialized detectors and instrumentation systems.

**2) Data Storage:** The generated data is periodically persisted via checkpointing (①) as schema-consistent records, where identical attributes are recorded per timestep or event. Hierarchical formats such as HDF5 [29] and ROOT [30] are widely used to organize this data into nested groups and datasets. Due to their repetitive structure, such records are often convertible into tabular form. Recently, columnar formats like Parquet [31] has gained popularity for analytical workloads, leading to its adoption as a native storage format [32], [33] and motivating the conversion of HDF5 and ROOT data for improved compatibility and scalability [34].

**3) Data Analysis:** For analyzing tabular data, distributed data processing engines such as Apache Spark [6] and Relational Database Management Systems (RDBMS) are commonly used. In Spark-based environments, users can perform efficient analysis on specific Regions of Interest (ROI) using either SQL queries or high-level API such as the Spark DataFrame API [8], [35], [36]. Upon receiving an analysis request (②), the system loads relevant data from storage into compute nodes (③), where queries are executed to extract scientifically meaningful subsets (④).

**4) Data Visualization:** These extracted subsets are subsequently leveraged for downstream analytical tasks, including visualizing simulation results (⑤), comparing with experimental observations, and validating the accuracy and reliability of the simulation outcomes.

## B. Low-Selectivity Queries in Scientific Workflows

Prior studies have shown that, in many scientific workflows, queries often require only a small subset of data despite scanning the entire dataset [37]–[39]. To further understand this, we analyzed real-world queries from the CFD domain using the Laghos 3D Mesh Dataset [40] and representative query patterns from Los Alamos National Laboratory (LANL) (refer to the example SQL query in Figure 2).

Figure 3 visualizes the distribution density of records in the Laghos dataset that satisfy the filter condition 1.5 < x, y, z < 1.6. The horizontal axis denotes simulation timestep IDs, and the vertical axis divides the 1.500-1.600 value range into ten uniform bins of width 0.01. Subfigures (a)-(c) respectively illustrate the density distributions for x, y, and z dimensions (columns). Most bins exhibit zero density, and even the maximum bin value does not exceed 2‰. Given that the query requires all three coordinates to fall within the specified ROI range, only overlapping non-zero bins contribute to the result. The resulting compound selectivity is as low as 1.91×10⁻⁴%, indicating an extremely sparse subset of relevant records. This high sparsity reflects a common pattern in domain-specific workflows, where scientists often focus on localized regions or rare events within large-scale simulation outputs [41].

## C. Well-Known Challenges of Data Movement and Storage

Scientific workflows produce massive datasets that are persisted to storage and repeatedly moved between storage and compute nodes for post-hoc analysis. While distributed engines such as Spark support scalable analysis, their performance is constrained by access to remote data. Specifically, modern HPC storage systems face two key limitations that hinder scalable analysis: data movement and data placement.

**Challenge#1–Massive Data Movement.** While compute performance in HPC systems has improved rapidly, I/O bandwidth between storage and compute nodes has not scaled accordingly. As a result, data movement from storage to compute nodes dominates analysis runtimes [41], even when queries access only a small subset of the data. This imbalance is exacerbated by growing simulation output sizes and increasing demands for faster turnaround, leading to higher latency, energy consumption, and infrastructure costs [9].

**Challenge#2–Placement-Access Frequency Mismatch.** Scientific datasets in columnar formats often exhibit skewed access patterns, where certain columns are accessed far more frequently than others [16], [17]. Nevertheless, most HPC storage systems rely on POSIX-based flat file abstractions that lack semantic awareness of column-level locality. This limitation is especially problematic in tiered storage hierarchies comprising HDDs and SSDs, where all data is managed uniformly regardless of access frequency [16]. This mismatch leads to full-file reads from high-latency storage and underutilization of high-performance devices such as NVMe SSDs, degrading bandwidth efficiency and overall system performance.

## D. The Advent of Computation-Enabled Object Storage

**Computational Storage for Data Movement Reduction:** To mitigate the data transfer bottleneck, recent efforts have investigated computational storage, which enables basic operations such as filter and project to be offloaded to the storage layer [9], [41], [42]. This approach reduces the volume of data transferred to compute nodes, thereby accelerating analysis and alleviating pressure on network and I/O subsystems. It is particularly effective in low-selectivity scenarios where only a small portion of the dataset satisfies the query predicates.

**Improving Data Placement with Object Storage:** To overcome the limitations of uniform data placement, the HPC community is increasingly adopting object storage [43]. Unlike POSIX-based file systems, object storage manages data as discrete objects enriched with metadata, allowing more granular control over storage policies. This facilitates adaptive tiering, where frequently accessed columns can be placed on fast NVMe SSDs while rarely accessed data resides on high-capacity HDDs. Thus, AWS S3 [44]-compatible object storage systems such as Ceph [19] and MinIO [18] are already in wide use at large-scale research sites such as Conseil Européen pour la Recherche Nucléaire (CERN) and Institute of High Energy Physics (IHEP) [17], [45]. Furthermore, commercial offerings including IBM COS and NetApp StorageGRID which further accelerate this trend [46], [47].

**Computation-Enabled Object Storage:** To address the dual challenges of excessive data movement and suboptimal data placement, recent research has introduced Computation-Enabled Object Storage (COS) systems [21]–[23]. These systems integrate the flexible, metadata-rich structure of object storage with computation capabilities, enhancing both query efficiency and storage utilization.

There are two main design approaches. The **first** extends the object storage interface to support lightweight offloaded computation. Systems such as MinIO Select [22] and Ceph S3 Select [23] enable SQL-like filter queries to be executed directly at the object interface layer, reducing data transfer by pushing down simple operations. The **second** approach embeds computation deeper into the storage stack. A representative example is SkyhookDM [21], which integrates data processing capabilities into Ceph OSD layer using Apache Arrow [26]. While SkyhookDM supports basic operations such as filter and aggregate, it also allows users to define custom processing logic within the storage backend. By enabling more expressive query offloading at the storage layer, this integration establishes storage-side computation as a foundational building block for scalable and efficient scientific data analysis.

---

### النسخة العربية

## أ. سير عمل التحليل اللاحق في التطبيقات العلمية

يقدم الشكل 2 سير عمل تحليل لاحق تمثيلي معتمد على نطاق واسع في التطبيقات العلمية الحديثة، بما في ذلك تلك في ديناميكا الموائع الحسابية (CFD)، وفيزياء الطاقة العالية (HEP)، ومحاكاة الجسيمات في الخلايا (PIC). يتكون سير العمل هذا عادةً من أربع مراحل متسلسلة: توليد البيانات، وتخزين البيانات، وتحليل البيانات، وتصوير البيانات.

**1) توليد البيانات:** تولد التطبيقات العلمية الحديثة البيانات من خلال حساب الكميات الفيزيائية (مثل الموضع والسرعة والطاقة) للجسيمات الفردية ضمن نطاقات المحاكاة المحددة، مثل مناطق المراقبة أو خلايا الشبكة. في التطبيقات الموجهة بالمراقبة، مثل تجارب تصادم الجسيمات، يتم جمع البيانات في الوقت الفعلي من خلال كواشف وأنظمة أجهزة متخصصة.

**2) تخزين البيانات:** يتم حفظ البيانات المولدة بشكل دوري عبر نقاط التحقق (①) كسجلات متسقة في المخطط، حيث يتم تسجيل سمات متطابقة لكل خطوة زمنية أو حدث. تُستخدم التنسيقات الهرمية مثل HDF5 [29] وROOT [30] على نطاق واسع لتنظيم هذه البيانات في مجموعات ومجموعات بيانات متداخلة. نظراً لبنيتها المتكررة، غالباً ما يمكن تحويل هذه السجلات إلى شكل جدولي. في الآونة الأخيرة، اكتسبت التنسيقات العمودية مثل Parquet [31] شعبية لأحمال العمل التحليلية، مما أدى إلى اعتمادها كتنسيق تخزين أصلي [32]، [33] وحفّز على تحويل بيانات HDF5 وROOT لتحسين التوافق وقابلية التوسع [34].

**3) تحليل البيانات:** لتحليل البيانات الجدولية، تُستخدم عادة محركات معالجة البيانات الموزعة مثل Apache Spark [6] وأنظمة إدارة قواعد البيانات العلائقية (RDBMS). في بيئات قائمة على Spark، يمكن للمستخدمين إجراء تحليل فعال على مناطق اهتمام محددة (ROI) باستخدام إما استعلامات SQL أو واجهات برمجة التطبيقات عالية المستوى مثل Spark DataFrame API [8]، [35]، [36]. عند تلقي طلب تحليل (②)، يُحمّل النظام البيانات ذات الصلة من التخزين إلى عقد الحساب (③)، حيث يتم تنفيذ الاستعلامات لاستخراج مجموعات فرعية ذات معنى علمي (④).

**4) تصوير البيانات:** يتم استخدام هذه المجموعات الفرعية المستخرجة لاحقاً للمهام التحليلية اللاحقة، بما في ذلك تصوير نتائج المحاكاة (⑤)، والمقارنة مع الملاحظات التجريبية، والتحقق من دقة وموثوقية نتائج المحاكاة.

## ب. الاستعلامات منخفضة الانتقائية في سير العمل العلمي

أظهرت الدراسات السابقة أنه في العديد من سير العمل العلمي، غالباً ما تتطلب الاستعلامات مجموعة فرعية صغيرة فقط من البيانات على الرغم من مسح مجموعة البيانات بأكملها [37]–[39]. لفهم ذلك بشكل أفضل، حللنا استعلامات حقيقية من مجال CFD باستخدام مجموعة بيانات Laghos 3D Mesh [40] وأنماط استعلام تمثيلية من مختبر لوس ألاموس الوطني (LANL) (راجع مثال استعلام SQL في الشكل 2).

يُصوّر الشكل 3 كثافة توزيع السجلات في مجموعة بيانات Laghos التي تستوفي شرط الترشيح 1.5 < x, y, z < 1.6. يُشير المحور الأفقي إلى معرفات الخطوات الزمنية للمحاكاة، ويقسم المحور الرأسي نطاق القيم 1.500-1.600 إلى عشرة صناديق موحدة بعرض 0.01. توضح الأشكال الفرعية (a)-(c) على التوالي توزيعات الكثافة لأبعاد x وy وz (الأعمدة). تُظهر معظم الصناديق كثافة صفرية، وحتى القيمة القصوى للصندوق لا تتجاوز 2‰. بالنظر إلى أن الاستعلام يتطلب أن تقع جميع الإحداثيات الثلاثة ضمن نطاق ROI المحدد، فإن الصناديق غير الصفرية المتداخلة فقط تساهم في النتيجة. الانتقائية المركبة الناتجة منخفضة تصل إلى 1.91×10⁻⁴٪، مما يشير إلى مجموعة فرعية نادرة للغاية من السجلات ذات الصلة. يعكس هذا التناثر العالي نمطاً شائعاً في سير العمل الخاصة بالمجال، حيث يركز العلماء غالباً على مناطق موضعية أو أحداث نادرة ضمن مخرجات المحاكاة واسعة النطاق [41].

## ج. التحديات المعروفة لحركة البيانات والتخزين

تنتج سير العمل العلمية مجموعات بيانات ضخمة يتم حفظها في التخزين وتحريكها بشكل متكرر بين عقد التخزين والحساب للتحليل اللاحق. بينما تدعم المحركات الموزعة مثل Spark التحليل القابل للتوسع، يُقيد أداؤها بالوصول إلى البيانات البعيدة. على وجه التحديد، تواجه أنظمة تخزين HPC الحديثة قيدين رئيسيين يعيقان التحليل القابل للتوسع: حركة البيانات ووضع البيانات.

**التحدي رقم 1 - حركة البيانات الضخمة.** بينما تحسن أداء الحساب في أنظمة HPC بسرعة، لم يتوسع عرض نطاق الإدخال/الإخراج بين عقد التخزين والحساب وفقاً لذلك. نتيجة لذلك، تهيمن حركة البيانات من عقد التخزين إلى عقد الحساب على أوقات تشغيل التحليل [41]، حتى عندما تصل الاستعلامات فقط إلى مجموعة فرعية صغيرة من البيانات. يتفاقم هذا الاختلال بسبب تزايد أحجام مخرجات المحاكاة والمطالب المتزايدة لتحقيق دوران أسرع، مما يؤدي إلى زيادة زمن الاستجابة واستهلاك الطاقة وتكاليف البنية التحتية [9].

**التحدي رقم 2 - عدم تطابق الوضع مع تكرار الوصول.** غالباً ما تُظهر مجموعات البيانات العلمية بتنسيقات عمودية أنماط وصول منحرفة، حيث يتم الوصول إلى أعمدة معينة بشكل أكثر تكراراً من غيرها [16]، [17]. ومع ذلك، تعتمد معظم أنظمة تخزين HPC على تجريدات الملفات المسطحة القائمة على POSIX التي تفتقر إلى الوعي الدلالي بموضعية مستوى الأعمدة. هذا القيد إشكالي بشكل خاص في التسلسلات الهرمية للتخزين المتدرج التي تتألف من أقراص HDD وSSD، حيث تتم إدارة جميع البيانات بشكل موحد بغض النظر عن تكرار الوصول [16]. يؤدي هذا التناقض إلى قراءات ملفات كاملة من تخزين عالي زمن الاستجابة وعدم الاستفادة الكافية من الأجهزة عالية الأداء مثل أقراص SSD من نوع NVMe، مما يُدهور كفاءة عرض النطاق والأداء العام للنظام.

## د. ظهور تخزين الكائنات الممكّن حسابياً

**التخزين الحسابي لتقليل حركة البيانات:** للتخفيف من عنق زجاجة نقل البيانات، بحثت الجهود الأخيرة في التخزين الحسابي، الذي يُمكّن العمليات الأساسية مثل الترشيح والإسقاط من التفريغ إلى طبقة التخزين [9]، [41]، [42]. يقلل هذا النهج من حجم البيانات المنقولة إلى عقد الحساب، وبالتالي يُسرّع التحليل ويُخفف الضغط على أنظمة الشبكة والإدخال/الإخراج. إنه فعال بشكل خاص في سيناريوهات الانتقائية المنخفضة حيث يستوفي جزء صغير فقط من مجموعة البيانات محمولات الاستعلام.

**تحسين وضع البيانات بتخزين الكائنات:** للتغلب على قيود وضع البيانات الموحد، يتبنى مجتمع HPC بشكل متزايد تخزين الكائنات [43]. على عكس أنظمة الملفات القائمة على POSIX، يدير تخزين الكائنات البيانات ككائنات منفصلة مُثرية بالبيانات الوصفية، مما يسمح بتحكم أكثر دقة في سياسات التخزين. هذا يُسهّل التدريج التكيفي، حيث يمكن وضع الأعمدة التي يتم الوصول إليها بشكل متكرر على أقراص SSD من نوع NVMe السريعة بينما تتواجد البيانات التي نادراً ما يتم الوصول إليها على أقراص HDD عالية السعة. وبالتالي، فإن أنظمة تخزين الكائنات المتوافقة مع AWS S3 [44] مثل Ceph [19] وMinIO [18] مستخدمة بالفعل على نطاق واسع في مواقع الأبحاث واسعة النطاق مثل المجلس الأوروبي للبحوث النووية (CERN) ومعهد فيزياء الطاقة العالية (IHEP) [17]، [45]. علاوة على ذلك، تُسرّع العروض التجارية بما في ذلك IBM COS وNetApp StorageGRID هذا الاتجاه [46]، [47].

**تخزين الكائنات الممكّن حسابياً:** لمعالجة التحديات المزدوجة المتمثلة في حركة البيانات المفرطة ووضع البيانات دون المستوى الأمثل، قدمت الأبحاث الحديثة أنظمة تخزين الكائنات الممكّنة حسابياً (COS) [21]–[23]. تدمج هذه الأنظمة الهيكل المرن الغني بالبيانات الوصفية لتخزين الكائنات مع قدرات الحساب، مما يعزز كلاً من كفاءة الاستعلام واستخدام التخزين.

هناك نهجان رئيسيان للتصميم. **الأول** يمتد واجهة تخزين الكائنات لدعم الحساب المفرغ الخفيف الوزن. تمكّن الأنظمة مثل MinIO Select [22] وCeph S3 Select [23] من تنفيذ استعلامات ترشيح شبيهة بـ SQL مباشرة في طبقة واجهة الكائنات، مما يقلل من نقل البيانات عن طريق دفع العمليات البسيطة إلى أسفل. **النهج الثاني** يُضمّن الحساب بشكل أعمق في مكدس التخزين. مثال تمثيلي هو SkyhookDM [21]، الذي يدمج قدرات معالجة البيانات في طبقة Ceph OSD باستخدام Apache Arrow [26]. بينما يدعم SkyhookDM العمليات الأساسية مثل الترشيح والتجميع، فإنه يسمح أيضاً للمستخدمين بتحديد منطق معالجة مخصص داخل الواجهة الخلفية للتخزين. من خلال تمكين تفريغ استعلامات أكثر تعبيراً في طبقة التخزين، يُنشئ هذا التكامل الحساب من جانب التخزين كلبنة بناء أساسية للتحليل العلمي للبيانات القابل للتوسع والفعال.

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 3
- **Key terms introduced:** checkpointing, HDF5, ROOT, Parquet, RDBMS, ROI, CERN, IHEP, AWS S3, IBM COS, NetApp StorageGRID
- **Equations:** None
- **Citations:** [6], [8], [9], [16], [17], [18], [19], [21]-[23], [26], [29]-[47] referenced
- **Special handling:**
  - Storage format names kept in English (HDF5, ROOT, Parquet, Arrow)
  - Organization names kept in English (CERN, IHEP, LANL, ORNL)
  - Product names kept in English (MinIO, Ceph, SkyhookDM, AWS S3, IBM COS, NetApp StorageGRID)
  - Technical abbreviations kept in English (RDBMS, ROI, API, OSD)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
