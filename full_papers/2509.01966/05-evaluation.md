# Section 5: Evaluation
## القسم 5: التقييم

**Section:** evaluation and experiments
**Translation Quality:** 0.85
**Glossary Terms Used:** benchmark, throughput, execution time, selectivity, performance, Spark cluster, CFD, HEP, PIC, Laghos, CMS Open Data

---

### English Version

## A. Experimental Setup

**Implementation:** We implemented a prototype of OASIS by building the OASIS-A using SPDK [61] v23.09, extending its BDEV layer to incorporate the Storage Manager and Result Handler. The in-storage Query Executor is built on DuckDB [27] v1.3.0. On the OASIS-FE, we employ Versity Gateway [62] v2.49.2 for S3 compatibility and implement the Metadata Manager, Result Handler, and Local Optimizer in a C++ backend server. Communication between the OASIS-FE and OASIS-As is handled via the NVMe-oF initiator in the Linux kernel v5.15.0.

**OASIS and Analytics Cluster Setup:** To configure OASIS, we used a 48-core, 64 GB memory server as the OASIS-FE, and a server with identical specifications but limited to 16 cores as the OASIS-A and equipped 1 NVMe SSD.

We deployed a Spark cluster with Spark 4.0.0 consisting of a 64-core, 386 GB memory server as the Spark driver and two 112-core, 128 GB memory servers as Spark executor nodes. The server specifications for the OASIS-FE, OASIS-A, and the Spark cluster are listed in Table III. The OASIS-FE and OASIS-A are connected via a 10 GbE RDMA network for SPDK, while OASIS communicates with the Spark cluster over 10 GbE Ethernet network.

**Workload:** For evaluation, we selected three real-world scientific workloads: (1) Laghos [28] 3D Mesh Simulation, which models shock hydrodynamics in a Lagrangian framework, (2) DeepWater-Impact Simulation [63], which simulates the interaction of water with rigid bodies in marine environments; and (3) CMS Open Data [64], which consists of high-energy physics collision event records collected at the CERN LHC.

The Laghos dataset [40] is 20GB in size. The DeepWater-Impact workload comprises two datasets [50] of 13GB and 30GB, respectively, which differ in simulation resolution. The CMS dataset contains 12GB of data. All datasets were converted to the Parquet format for analysis and are publicly available.

Table IV shows the queries using these datasets. Q1 computes the average energy per vertex within a specified spatial region using the Laghos dataset. Q2 extracts fluid elements from the Deep Water Impact simulation based on the thresholds. Q3 analyzes the vertical extent of dynamic fluid activity over time in the high-resolution Deep Water dataset. Q4 identifies opposite-charge muon pairs with invariant mass between 60 and 120 GeV in CMS event data.

To evaluate the effectiveness of OASIS as a COS, we investigate the following research questions (RQs).

• **RQ#1:** Does OASIS provide object-level I/O performance for scientific datasets comparable to existing COSs?
• **RQ#2:** How effective is OASIS's hierarchical operator execution strategy in improving query performance when evaluated under a uniform storage configuration?
• **RQ#3:** Does the Arrow-based output of OASIS offer performance advantages over traditional CSV formats in analytical workflows?
• **RQ#4:** How does selectivity affect the performance of OASIS in scientific query workloads?
• **RQ#5:** How effective is OASIS's SODA strategy compared to other decomposition approaches in hierarchical execution?

**Comparison:** To answer these research questions, we conducted a series of experiments using the following four configurations.

• **Baseline:** Executes queries using standard Spark processing, where all computation is performed after retrieving data from storage.
• **Pred.:** Extends the Baseline by enabling predicate pushdown to the storage layer.
• **OASIS:** Represents our proposed design that employs hierarchical execution across storage layers by SODA.
• **COS:** Emulates how OASIS would operate under the computation model of COSs by executing all operators at the OASIS-FE. This configuration ensures that the execution layer follows the same layer as in existing COS systems, allowing to isolate the effects of hierarchical execution without interference such as I/O overhead.

## B. Object-Level I/O Performance

To evaluate I/O performance for RQ#1, we compared the object-level PUT and GET throughput of OASIS against MinIO, using 16 threads and object sizes from 64MB to 1GB. This reflects typical scientific workloads, where data is written in parallel in 64–256MB blocks, such as Parquet row groups.

Figure 6 shows the results, with the 10 Gbps network bandwidth used as the upper bound. In Figure 6(a), MinIO achieves up to 681.5MB/s, while OASIS peaks at 582.9MB/s but degrades with larger objects due to gRPC overhead from sending many small messages and lack of parallel buffer management. Neither system saturates the 10 GbE link, mainly due to checksum generation and verification. OASIS is further limited by gRPC costs, including message fragmentation and lack of parallel buffer handling. Figure 6(b) shows similar trends for GET. MinIO sustains over 1,080MB/s, while OASIS drops to 605.6MB/s at 1GB due to the same bottlenecks.

Overall, OASIS lags behind MinIO for large objects, but further optimization of buffer management and messaging is expected to close the gap and attain comparable performance.

## C. Effect of Hierarchical Execution on Query Performance

To evaluate the effectiveness of hierarchical execution in addressing RQ#2, we performed a series of experiments. OASIS leverages SODA for optimal execution planning, with a detailed analysis provided in §V-F.

**1) Queries involving Scalar-based Conditions:** We evaluated three queries (Q1-Q3) involving scalar-based conditions. Each query differs in form, as shown in Table IV. As illustrated in Figure 7, OASIS consistently achieves the lowest execution time across both queries. In scalar-based query evaluation, we assume that COS supports all candidate operators, as operator support may vary across systems. This assumption allows us to isolate and validate the impact of hierarchical execution across different queries.

For Q1 and Q2, OASIS outperforms COS by 15.27% in Q1 and 32.7% in Q2 by minimizing internal data movement between the storage and compute layers, resulting in sharper performance gains. In Q3, OASIS continues to deliver the best performance, although the performance gap between OASIS and COS narrows. This is because Q3 is compute-intensive, and the performance benefit from reducing data movement becomes less prominent due to the compute capability gap between the OASIS-A and the OASIS-FE.

To validate the results presented in Figure 7, we measured both the inter-layer data traffic and the size of the result data transferred to the compute layer. Across all queries, a consistent trend emerges: both COS and OASIS substantially reduce the volume of result data compared to the Baseline. For instance, in Q2, the result size is reduced from 13.18GB in the Baseline to 52.89MB (Arrow IPC) in OASIS and 29.08 MB (CSV) in COS, with the smaller size in COS attributed to the higher compression ratio of CSV format. For inter-layer traffic, COS transfers the entire dataset from the OASIS-A, while OASIS performs early filtering and reduces inter-layer transfer to 53MB. This demonstrates that OASIS minimizes internal data movement, leading to faster execution for scalar queries with lightweight predicates. Across all workloads, Pred is slightly slower than the Baseline, primarily due to the overhead of scanning Parquet metadata, with no records being filtered out in the target datasets.

**2) Queries involving Array-based Conditions:** Queries Q1–Q3 use scalar-based conditions, whereas Q4 involves an array-based condition. In this section, we evaluated Q4, derived from the HEP benchmark [65], to assess the array-aware processing capabilities of OASIS. Q4 involves array-based filter and project operations. COS, modeled after vanilla SkyhookDM, supports only array-based filter and simple column-level project.

Figure 7 illustrates the Q4 execution time of four configurations. OASIS completed the query in 87.203 seconds, 24.6% faster than COS and 64.0% faster than the Baseline, by offloading both the filter and project with array-based conditions to the storage layer. In contrast, COS offloads only the initial filter and must transfer intermediate results to the compute node for array-based project, even though it can execute subsequent filter operations. This failure to offload project results in additional data movement. Predicate Pushdown evaluates only the scalar predicate in storage, showing better performance than Baseline. These results highlight that OASIS's array-aware offloading reduces data movement and accelerates query execution.

## D. Impact of Output Format on System Efficiency

Figure 8 compares the data loading performance of Arrow and CSV formats when ingesting the output of Q1 into the Spark cluster for RQ#3. Arrow consistently outperforms CSV across all record sizes in terms of load time. The observed decrease in execution time from 1,000,000 to 10,000,000 records is due to Spark increasing the number of partitions from 112 to 1,000, thereby enhancing parallelism and improving overall data ingestion throughput. Since Arrow enables more efficient in-memory loading compared to CSV regardless of data size, these results suggest that Arrow is advantageous not only as a final output format but also as an intermediate data representation during multi-layer query execution.

## E. Performance Behavior of OASIS Across Diverse Selectivity

Figure 9 (a) presents the performance comparison between OASIS and the Baseline as the selectivity of Q1 varies. In contrast, (b) shows the results for a modified version of Q1 where the Group By (aggregation) operator is removed, with selectivity similarly adjusted.

In (a), OASIS consistently outperforms the Baseline even as selectivity increases. This is because the Group By operation limits the number of output rows based on the number of aggregation groups, preventing the output size from growing rapidly even as input data increases. In fact, for Q1, the maximum achievable selectivity was approximately 13%, constrained by the nature of the Group By. This suggests that aggregation operations impose a natural upper bound on output size, making them well-suited for query offloading.

On the other hand, (b) explores the case where the Group By operation is removed, allowing selectivity to increase up to approximately 75%. In this setting, the Baseline begins to outperform OASIS when selectivity exceeds around 25%. This indicates that when heavy operations such as sorting follow the filtering step, traditional cluster-based processing may become more efficient than storage-side offloading as the amount of data grows. These results highlight the need for dynamic offloading decisions based on both the query's operator characteristics and its selectivity.

## F. Effectiveness of SODA Decomposition

Figure 10 illustrates the evaluation of various split strategies to assess the effectiveness of SODA. Among the queries, Q1 contains the largest number of operators, while the others are relatively simple and do not undergo plan splitting. Therefore, Q1 is selected as the representative case to validate the behavior of SODA. Q1's query plan consists of four sequential stages: (1) read with filter, (2) aggregate, (3) project, and (4) sort (Figure 10(a)). We evaluate five different configurations within OASIS, where the Substrait Decomposer statically distributes operators between the OASIS-FE and OASIS-A without applying SODA. Among all configurations, SODA selected cfg4, which offloads read w/ filter, aggregate, and project to the OASIS-A, while executing only sort at the OASIS-FE. This configuration achieved the best runtime of 76 seconds, yielding a 45% reduction compared to the OASIS-FE-only setup that logically corresponds to the computation model of conventional COS systems. Configurations that offloaded only filter or filter with aggregate showed runtimes around 83 seconds, as the reduced data volume did not fully offset the remaining compute overhead at the OASIS-FE.

In our experiments, SODA introduces minimal overhead, with an average of just 126ms for selectivity estimation and 1,810ms for Substrait-based plan decomposition.

These results demonstrate that pushing low-cost, high-reduction operators closer to data, while reserving compute-heavy ones like sort for the OASIS-FE, yields better performance. SODA can be further improved by incorporating operator-level compute cost into its decision model.

---

### النسخة العربية

## أ. الإعداد التجريبي

**التنفيذ:** قمنا بتنفيذ نموذج أولي لـ OASIS من خلال بناء OASIS-A باستخدام SPDK [61] v23.09، وتوسيع طبقة BDEV الخاصة به لدمج مدير التخزين ومعالج النتائج. تم بناء منفذ الاستعلام داخل التخزين على DuckDB [27] v1.3.0. على OASIS-FE، نستخدم Versity Gateway [62] v2.49.2 للتوافق مع S3 وننفذ مدير البيانات الوصفية ومعالج النتائج والمحسّن المحلي في خادم واجهة خلفية C++. يتم التعامل مع الاتصال بين OASIS-FE وOASIS-As عبر بادئ NVMe-oF في نواة Linux v5.15.0.

**إعداد OASIS ومجموعة التحليلات:** لتكوين OASIS، استخدمنا خادماً بـ 48 نواة وذاكرة 64 جيجابايت كـ OASIS-FE، وخادماً بمواصفات متطابقة ولكن محدوداً بـ 16 نواة كـ OASIS-A ومجهزاً بقرص SSD NVMe واحد.

نشرنا مجموعة Spark مع Spark 4.0.0 تتألف من خادم بـ 64 نواة وذاكرة 386 جيجابايت كبرنامج تشغيل Spark وخادمين بـ 112 نواة وذاكرة 128 جيجابايت كعقد منفذة لـ Spark. مواصفات الخادم لـ OASIS-FE وOASIS-A ومجموعة Spark مدرجة في الجدول III. تتصل OASIS-FE وOASIS-A عبر شبكة RDMA بسرعة 10 GbE لـ SPDK، بينما يتواصل OASIS مع مجموعة Spark عبر شبكة Ethernet بسرعة 10 GbE.

**حمل العمل:** للتقييم، اخترنا ثلاثة أحمال عمل علمية حقيقية: (1) محاكاة Laghos [28] ثلاثية الأبعاد للشبكة، التي تمذجة ديناميكا الصدمة الهيدروديناميكية في إطار لاغرانجي، (2) محاكاة Deep Water-Impact [63]، التي تحاكي تفاعل الماء مع الأجسام الصلبة في البيئات البحرية؛ و(3) بيانات CMS المفتوحة [64]، التي تتكون من سجلات أحداث التصادم في فيزياء الطاقة العالية التي تم جمعها في مصادم الهادرونات الكبير في CERN.

مجموعة بيانات Laghos [40] بحجم 20 جيجابايت. يتألف حمل عمل Deep Water-Impact من مجموعتي بيانات [50] بحجم 13 جيجابايت و30 جيجابايت، على التوالي، تختلفان في دقة المحاكاة. تحتوي مجموعة بيانات CMS على 12 جيجابايت من البيانات. تم تحويل جميع مجموعات البيانات إلى تنسيق Parquet للتحليل وهي متاحة للعموم.

يوضح الجدول IV الاستعلامات باستخدام مجموعات البيانات هذه. يحسب Q1 متوسط الطاقة لكل رأس ضمن منطقة مكانية محددة باستخدام مجموعة بيانات Laghos. يستخرج Q2 عناصر السوائل من محاكاة Deep Water Impact بناءً على العتبات. يحلل Q3 المدى الرأسي للنشاط السائل الديناميكي عبر الزمن في مجموعة بيانات Deep Water عالية الدقة. يحدد Q4 أزواج الميونات ذات الشحنات المعاكسة مع كتلة ثابتة بين 60 و120 جيجا إلكترون فولت في بيانات أحداث CMS.

لتقييم فعالية OASIS كـ COS، نبحث في أسئلة البحث التالية (RQs).

• **RQ#1:** هل يوفر OASIS أداء إدخال/إخراج على مستوى الكائنات لمجموعات البيانات العلمية مقارناً بـ COSs الحالية؟
• **RQ#2:** ما مدى فعالية استراتيجية التنفيذ الهرمي للمعاملات في OASIS في تحسين أداء الاستعلام عند التقييم في ظل تكوين تخزين موحد؟
• **RQ#3:** هل يوفر إخراج OASIS القائم على Arrow مزايا أداء على تنسيقات CSV التقليدية في سير العمل التحليلي؟
• **RQ#4:** كيف تؤثر الانتقائية على أداء OASIS في أحمال عمل الاستعلام العلمي؟
• **RQ#5:** ما مدى فعالية استراتيجية SODA الخاصة بـ OASIS مقارنة بنهج التحليل الأخرى في التنفيذ الهرمي؟

**المقارنة:** للإجابة على أسئلة البحث هذه، أجرينا سلسلة من التجارب باستخدام التكوينات الأربعة التالية.

• **الأساس (Baseline):** ينفذ الاستعلامات باستخدام معالجة Spark القياسية، حيث يتم تنفيذ جميع العمليات الحسابية بعد استرجاع البيانات من التخزين.
• **Pred.:** يمتد الأساس من خلال تمكين دفع المحمولات إلى طبقة التخزين.
• **OASIS:** يمثل تصميمنا المقترح الذي يستخدم التنفيذ الهرمي عبر طبقات التخزين بواسطة SODA.
• **COS:** يحاكي كيفية عمل OASIS في ظل نموذج الحساب الخاص بأنظمة COS من خلال تنفيذ جميع المعاملات في OASIS-FE. يضمن هذا التكوين أن طبقة التنفيذ تتبع نفس الطبقة كما في أنظمة COS الحالية، مما يسمح بعزل آثار التنفيذ الهرمي دون تدخل مثل عبء الإدخال/الإخراج.

## ب. أداء الإدخال/الإخراج على مستوى الكائنات

لتقييم أداء الإدخال/الإخراج لـ RQ#1، قارنا إنتاجية PUT وGET على مستوى الكائنات لـ OASIS مقابل MinIO، باستخدام 16 خيطاً وأحجام كائنات من 64 ميجابايت إلى 1 جيجابايت. يعكس هذا أحمال العمل العلمية النموذجية، حيث يتم كتابة البيانات بالتوازي في كتل 64-256 ميجابايت، مثل مجموعات صفوف Parquet.

يوضح الشكل 6 النتائج، مع استخدام عرض نطاق الشبكة البالغ 10 جيجابت في الثانية كحد أعلى. في الشكل 6 (أ)، يحقق MinIO ما يصل إلى 681.5 ميجابايت/ثانية، بينما يصل OASIS إلى ذروة 582.9 ميجابايت/ثانية ولكنه يتدهور مع الكائنات الأكبر بسبب عبء gRPC من إرسال العديد من الرسائل الصغيرة ونقص إدارة المخازن المؤقتة المتوازية. لا يشبع أي من النظامين وصلة 10 GbE، بشكل أساسي بسبب إنشاء والتحقق من المجموع الاختباري. يقتصر OASIS بشكل أكبر على تكاليف gRPC، بما في ذلك تجزئة الرسائل ونقص التعامل المتوازي مع المخازن المؤقتة. يُظهر الشكل 6 (ب) اتجاهات مماثلة لـ GET. يحافظ MinIO على أكثر من 1,080 ميجابايت/ثانية، بينما ينخفض OASIS إلى 605.6 ميجابايت/ثانية عند 1 جيجابايت بسبب نفس الاختناقات.

بشكل عام، يتخلف OASIS عن MinIO للكائنات الكبيرة، لكن من المتوقع أن يؤدي مزيد من التحسين لإدارة المخازن المؤقتة والرسائل إلى سد الفجوة وتحقيق أداء مماثل.

## ج. تأثير التنفيذ الهرمي على أداء الاستعلام

لتقييم فعالية التنفيذ الهرمي في معالجة RQ#2، أجرينا سلسلة من التجارب. يستفيد OASIS من SODA للتخطيط الأمثل للتنفيذ، مع تحليل مفصل مقدم في §V-F.

**1) الاستعلامات التي تتضمن شروطاً قائمة على القياسية:** قيّمنا ثلاثة استعلامات (Q1-Q3) تتضمن شروطاً قائمة على القياسية. يختلف كل استعلام في الشكل، كما هو موضح في الجدول IV. كما هو موضح في الشكل 7، يحقق OASIS باستمرار أقل وقت تنفيذ عبر كلا الاستعلامين. في تقييم الاستعلام القائم على القياسية، نفترض أن COS يدعم جميع المعاملات المرشحة، حيث قد يختلف دعم المعاملات عبر الأنظمة. يتيح هذا الافتراض عزل والتحقق من تأثير التنفيذ الهرمي عبر استعلامات مختلفة.

بالنسبة لـ Q1 وQ2، يتفوق OASIS على COS بنسبة 15.27٪ في Q1 و32.7٪ في Q2 من خلال تقليل حركة البيانات الداخلية بين طبقات التخزين والحساب، مما ينتج عنه مكاسب أداء أكثر حدة. في Q3، يستمر OASIS في تقديم أفضل أداء، على الرغم من أن فجوة الأداء بين OASIS وCOS تضيق. هذا لأن Q3 كثيف الحساب، وتصبح فائدة الأداء من تقليل حركة البيانات أقل بروزاً بسبب فجوة قدرة الحساب بين OASIS-A وOASIS-FE.

للتحقق من النتائج المعروضة في الشكل 7، قسنا كلاً من حركة البيانات بين الطبقات وحجم بيانات النتيجة المنقولة إلى طبقة الحساب. عبر جميع الاستعلامات، يظهر اتجاه متسق: يقلل كل من COS وOASIS بشكل كبير من حجم بيانات النتيجة مقارنة بالأساس. على سبيل المثال، في Q2، ينخفض حجم النتيجة من 13.18 جيجابايت في الأساس إلى 52.89 ميجابايت (Arrow IPC) في OASIS و29.08 ميجابايت (CSV) في COS، مع الحجم الأصغر في COS يُعزى إلى نسبة ضغط أعلى لتنسيق CSV. بالنسبة لحركة المرور بين الطبقات، ينقل COS مجموعة البيانات بأكملها من OASIS-A، بينما ينفذ OASIS الترشيح المبكر ويقلل النقل بين الطبقات إلى 53 ميجابايت. يوضح هذا أن OASIS يقلل من حركة البيانات الداخلية، مما يؤدي إلى تنفيذ أسرع للاستعلامات القياسية مع محمولات خفيفة الوزن. عبر جميع أحمال العمل، Pred أبطأ قليلاً من الأساس، بشكل أساسي بسبب عبء مسح البيانات الوصفية لـ Parquet، دون تصفية أي سجلات في مجموعات البيانات المستهدفة.

**2) الاستعلامات التي تتضمن شروطاً قائمة على المصفوفات:** تستخدم الاستعلامات Q1-Q3 شروطاً قائمة على القياسية، بينما يتضمن Q4 شرطاً قائماً على المصفوفات. في هذا القسم، قيّمنا Q4، المستمد من معيار HEP [65]، لتقييم قدرات المعالجة الواعية بالمصفوفات لـ OASIS. يتضمن Q4 عمليات ترشيح وإسقاط قائمة على المصفوفات. COS، المصمم على غرار SkyhookDM الأساسي، يدعم فقط الترشيح القائم على المصفوفات والإسقاط البسيط على مستوى الأعمدة.

يوضح الشكل 7 وقت تنفيذ Q4 لأربعة تكوينات. أكمل OASIS الاستعلام في 87.203 ثانية، أسرع بنسبة 24.6٪ من COS و64.0٪ أسرع من الأساس، من خلال تفريغ كل من الترشيح والإسقاط مع الشروط القائمة على المصفوفات إلى طبقة التخزين. في المقابل، يفرّغ COS فقط الترشيح الأولي ويجب نقل النتائج الوسيطة إلى عقدة الحساب للإسقاط القائم على المصفوفات، على الرغم من أنه يمكنه تنفيذ عمليات الترشيح اللاحقة. يؤدي هذا الفشل في تفريغ الإسقاط إلى حركة بيانات إضافية. يقيّم دفع المحمولات فقط المحمول القياسي في التخزين، مما يُظهر أداءً أفضل من الأساس. تسلط هذه النتائج الضوء على أن تفريغ OASIS الواعي بالمصفوفات يقلل من حركة البيانات ويُسرّع تنفيذ الاستعلام.

## د. تأثير تنسيق الإخراج على كفاءة النظام

يقارن الشكل 8 أداء تحميل البيانات لتنسيقات Arrow وCSV عند استيعاب إخراج Q1 في مجموعة Spark لـ RQ#3. يتفوق Arrow باستمرار على CSV عبر جميع أحجام السجلات من حيث وقت التحميل. الانخفاض الملاحظ في وقت التنفيذ من 1,000,000 إلى 10,000,000 سجل يرجع إلى زيادة Spark لعدد الأقسام من 112 إلى 1,000، وبالتالي تعزيز التوازي وتحسين إنتاجية استيعاب البيانات الإجمالية. نظراً لأن Arrow يتيح تحميلاً أكثر كفاءة في الذاكرة مقارنة بـ CSV بغض النظر عن حجم البيانات، تشير هذه النتائج إلى أن Arrow مفيد ليس فقط كتنسيق إخراج نهائي ولكن أيضاً كتمثيل بيانات وسيط أثناء تنفيذ الاستعلام متعدد الطبقات.

## هـ. سلوك أداء OASIS عبر انتقائية متنوعة

يقدم الشكل 9 (أ) مقارنة الأداء بين OASIS والأساس مع تغير انتقائية Q1. في المقابل، يُظهر (ب) النتائج لنسخة معدلة من Q1 حيث تمت إزالة معامل Group By (التجميع)، مع تعديل الانتقائية بالمثل.

في (أ)، يتفوق OASIS باستمرار على الأساس حتى مع زيادة الانتقائية. هذا لأن عملية Group By تحد من عدد صفوف الإخراج بناءً على عدد مجموعات التجميع، مما يمنع حجم الإخراج من النمو بسرعة حتى مع زيادة بيانات الإدخال. في الواقع، بالنسبة لـ Q1، كانت الانتقائية القصوى القابلة للتحقيق حوالي 13٪، مقيدة بطبيعة Group By. يشير هذا إلى أن عمليات التجميع تفرض حداً أعلى طبيعياً على حجم الإخراج، مما يجعلها مناسبة بشكل جيد لتفريغ الاستعلام.

من ناحية أخرى، يستكشف (ب) الحالة التي تمت فيها إزالة عملية Group By، مما يسمح بزيادة الانتقائية حتى حوالي 75٪. في هذا الإعداد، يبدأ الأساس في التفوق على OASIS عندما تتجاوز الانتقائية حوالي 25٪. يشير هذا إلى أنه عندما تتبع العمليات الثقيلة مثل الفرز خطوة الترشيح، قد تصبح المعالجة التقليدية القائمة على المجموعة أكثر كفاءة من تفريغ جانب التخزين مع نمو كمية البيانات. تسلط هذه النتائج الضوء على الحاجة إلى قرارات تفريغ ديناميكية بناءً على كل من خصائص معامل الاستعلام وانتقائيته.

## و. فعالية تحليل SODA

يوضح الشكل 10 تقييم استراتيجيات التقسيم المختلفة لتقييم فعالية SODA. من بين الاستعلامات، يحتوي Q1 على أكبر عدد من المعاملات، بينما الأخرى بسيطة نسبياً ولا تخضع لتقسيم الخطة. لذلك، يتم اختيار Q1 كحالة تمثيلية للتحقق من سلوك SODA. تتكون خطة استعلام Q1 من أربع مراحل متسلسلة: (1) القراءة مع الترشيح، (2) التجميع، (3) الإسقاط، و(4) الفرز (الشكل 10 (أ)). نقيّم خمسة تكوينات مختلفة ضمن OASIS، حيث يوزع محلل Substrait بشكل ثابت المعاملات بين OASIS-FE وOASIS-A دون تطبيق SODA. من بين جميع التكوينات، اختارت SODA cfg4، التي تفرّغ القراءة مع الترشيح والتجميع والإسقاط إلى OASIS-A، بينما تنفذ فقط الفرز في OASIS-FE. حقق هذا التكوين أفضل وقت تشغيل يبلغ 76 ثانية، مما أدى إلى انخفاض بنسبة 45٪ مقارنة بإعداد OASIS-FE فقط الذي يتوافق منطقياً مع نموذج الحساب لأنظمة COS التقليدية. أظهرت التكوينات التي فرّغت فقط الترشيح أو الترشيح مع التجميع أوقات تشغيل حوالي 83 ثانية، حيث لم يعوض حجم البيانات المنخفض بالكامل عبء الحساب المتبقي في OASIS-FE.

في تجاربنا، تقدم SODA عبئاً ضئيلاً، بمتوسط 126 ملي ثانية فقط لتقدير الانتقائية و1,810 ملي ثانية لتحليل الخطة القائم على Substrait.

تُظهر هذه النتائج أن دفع المعاملات منخفضة التكلفة وعالية التخفيض أقرب إلى البيانات، مع الاحتفاظ بتلك الثقيلة في الحساب مثل الفرز لـ OASIS-FE، يحقق أداءً أفضل. يمكن تحسين SODA بشكل أكبر من خلال دمج تكلفة الحساب على مستوى المعامل في نموذج قراره.

---

### Translation Notes

- **Figures referenced:** Figure 6, Figure 7, Figure 8, Figure 9, Figure 10
- **Tables referenced:** Table III, Table IV
- **Key terms introduced:** PUT/GET throughput, selectivity, query execution time, inter-layer traffic, benchmark workloads
- **Equations:** None
- **Citations:** [27], [28], [40], [50], [61]-[65] referenced
- **Special handling:**
  - Dataset names kept in English (Laghos, DeepWater-Impact, CMS Open Data)
  - Software/protocol names kept in English (SPDK, DuckDB, Versity Gateway, Parquet, NVMe-oF, RDMA)
  - Query identifiers kept in English (Q1, Q2, Q3, Q4)
  - Configuration names kept in English (Baseline, Pred., OASIS, COS, cfg1-cfg5)
  - Performance metrics preserved (MB/s, Gbps, seconds, percentages)

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.85
