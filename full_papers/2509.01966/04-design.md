# Section 4: Design of OASIS
## القسم 4: تصميم OASIS

**Section:** design and architecture
**Translation Quality:** 0.86
**Glossary Terms Used:** design principles, columnar output, array semantics, query path optimization, NVMe-oF, RDMA, Substrait IR, DuckDB, SODA, CAD, SAP, gRPC, S3 Gateway, metadata manager

---

### English Version

## A. Design Principle

To address the aforementioned limitations, we design a new COS architecture that preserves the benefits of columnar layout and in-storage computation, while introducing complex operators with array semantics and enabling flexible operator decomposition across execution tiers within the storage stack.

Guided by these goals, we present the core Design Principles (DP) that shape the architecture of OASIS.

• **DP#1: Column-Oriented Output Format Support for HPC Analytics.** OASIS should support both Arrow and CSV outputs to enable efficient columnar processing while preserving compatibility with applications that lack native Arrow support, such as Presto.

• **DP#2: Storage-Level Query Execution with Advanced Operator and Array Support.** As we analyzed in §III-A, HPC queries often involve aggregate and sort operations over simulation units, and array-level expressions on physical quantities. OASIS must support these operators and array semantics for effective and practical in-storage execution.

• **DP#3: Storage-Aware Query Path Optimization.** OASIS should reduce internal data movement by generating hierarchical query execution plans that place high data movement cost operations closer to storage and minimize interconnect and network traffic.

## B. Overview

The proposed OASIS system consists of a OASIS frontend (OASIS-FE) and multiple storage array (OASIS-A) servers. The OASIS-FE mainly comprises the following components (§IV-C): the S3 Gateway, the Local Optimizer, the Metadata Manager, the Query Executor and Result Handler, and the NVMe-over-Fabrics (NVMe-oF) Initiator module. Each OASIS-A is connected to the OASIS-FE via NVMe-oF, enabling high-throughput I/O. The OASIS-A consists of the following components (§IV-D): the NVMe-oF Target, the Storage Manager, and the Query Executor and Result Handler.

Figure 4 illustrates the end-to-end query offloading process in the OASIS system. ① The process begins when a client-side query engine submits an SQL query. ② The query is translated into an Intermediate Representation (IR), Substrait [57], which describes the operator-level execution plan (§IV-F). This IR plan is transmitted to the OASIS-FE via the OASIS-extended Pushdown (P/D) API integrated into the client-side query engine (§IV-H). ③ The S3 Gateway forwards the IR plan to the Local Optimizer. ④ The Local Optimizer partitions the IR plan into a OASIS-FE plan and a OASIS-A plan. The OASIS-FE plan depends on the intermediate result of the OASIS-A plan, establishing an execution dependency. ⑤ The OASIS-A plan is sent to the corresponding OASIS-A for execution. ⑥ The target object is retrieved from local storage via the Storage Manager. ⑦ The OASIS-A query engine executes the assigned plan and returns the intermediate result to the OASIS-FE. ⑧ The OASIS-FE registers the result into its query engine as a temporary table. ⑨ The OASIS-FE executes the OASIS-FE plan, ⑩ producing and ⑪ returning the final result.

## C. Core Components of OASIS-FE

**1) S3 Gateway:** This module acts as a network-facing entry point that bridges external S3 clients and the internal components of OASIS. It handles S3 protocol parsing and translates standard operations such as PutObject and GetObject into internal gRPC messages. These messages encapsulate request metadata and payloads, which are then forwarded to downstream modules for further processing, with responses returned in S3-compatible HTTP format.

**2) Local Optimizer:** This module analyzes and decomposes offloaded Substrait IR query plans using the Storage-side Query Plan Offloading and Decomposition Algorithm (SODA). It estimates the data transfer volume per operator to determine the optimal execution layer, either at the OASIS-FE or the OASIS-A. Then, the Local Optimizer generates subplans for the OASIS-FE and OASIS-A that account for both operator semantics and communication overhead, enabling efficient query execution while minimizing data movement.

**3) Metadata Manager:** This module manages execution-related metadata and performs logical-to-physical translation of requests received from the S3 Gateway. Upon receiving a gRPC message, it resolves the target object by mapping the S3 bucket name and object key to an internal Object Space ID and Object ID, maintained in its mapping table. It then generates the corresponding NVMe I/O commands and dispatches them to the appropriate OASIS-A for execution. When a new bucket is created, a corresponding OASIS-A is designated and allocates a unique Object Space ID for routing subsequent I/O requests. Additional metadata such as object size is included in each request.

To assist the Local Optimizer in operator-level query decomposition, the Metadata Manager collects lightweight statistical metadata during object ingestion. Specifically, when a PutObject operation occurs, a compact histogram is generated via sampling and stored locally on the OASIS-FE using the object key as an index. These histograms typically cover 0.5–5% of the object and capture column-level distributions for various data types such as double and int. The Local Optimizer later uses this metadata to estimate operator selectivity and output size, guiding plan partitioning and placement.

**4) Query Executor and Result Handler:** This module provides a lightweight, columnar-aware execution engine capable of running queries directly at the storage tier. It supports array-level expressions to efficiently evaluate scientific workloads involving nested or repeated structures. After execution, results are serialized into client-specified formats such as Arrow for high-throughput transfer or CSV/JSON for legacy compatibility. Further implementation details are described in §IV-E.

**5) NVMe-oF Initiator:** This component acts as a network interface that issues NVMe I/O commands to OASIS-A servers over NVMe-oF. The OASIS-FE converts object storage requests into NVMe commands and transmits them over a low-latency RDMA transport. Object data and metadata are encapsulated into a single extended NVMe command [58].

## D. Core Components of OASIS-A

**1) NVMe-oF Target:** The NVMe-oF Target module receives NVMe commands from the OASIS-FE and performs object I/O operations accordingly. Each command encapsulates both object data and metadata, allowing the OASIS-A to directly access memory and execute read/write operations without separate metadata handling. By leveraging an extended block command format, this design enables single-command execution with minimal data copying and supports high-throughput memory-based parallel I/O.

**2) Storage Manager:** The Storage Manager is responsible for handling storage and retrieval requests issued from the OASIS-FE using an internal object store. It manages data at the blob level through a Blob Property Table (BPT), which maps Object Space IDs and Object IDs to physical offsets on the storage device. Each blob follows an OPEN–RUN–CLOSE lifecycle during I/O, where DMA buffers and I/O channels are initialized for asynchronous execution. Write-Ahead Logging (WAL) ensures metadata consistency, and a slice-based address space is employed to improve scalability and physical alignment. While full implementation details are beyond the scope of this paper, this layer adopts core design principles from conventional object storage systems and provides a robust and scalable backend for upper-layer query execution.

**3) Query Executor and Result Handler:** This component mirrors the functionality of its counterpart in the OASIS-FE, executing assigned sub-plans and returning intermediate results. To enable fast and efficient communication between the OASIS-A and the OASIS-FE, intermediate results are serialized using the Arrow format and streamed back to the OASIS-FE. Further details are described in §IV-E.

## E. In-Storage Query Execution Engine and Result Transfer

The Query Executor and Result Handler are core components of OASIS, responsible for realizing DP#1 and DP#2 within the storage layer by enabling columnar query processing within the storage layer. Accordingly, the execution engine must satisfy three key requirements: (1) native support for columnar formats such as Arrow, (2) evaluation of expressions on individual elements within array-typed columns, and (3) a lightweight execution environment that operates reliably under constrained computational resources.

To fulfill these requirements, we adopt DuckDB [27] as the core execution engine within the storage layer. DuckDB is an open-source, embedded RDBMS optimized for Online Analytical Processing (OLAP) workloads, offering native support for columnar formats like Parquet and Arrow. It supports a wide range of SQL operators–including complex aggregations, sorts, and array-level functions–making it particularly effective for offloading diverse query fragments. Notably, DuckDB supports both in-memory processing and disk-based execution, allowing it to efficiently process large-scale columnar datasets ranging from tens to hundreds of gigabytes without requiring full in-memory loading. This makes it well-suited for lightweight, in-storage execution.

To enable execution across hierarchical layers while preserving the benefits of columnar processing for DP#3, the Query Executor serializes intermediate results and final outputs in compressed Arrow format for efficient transfer to the upper layer. For compatibility with legacy tools, final outputs can also be emitted in CSV or JSON format.

Arrow's columnar layout and zero-copy semantics minimize serialization overhead and enable efficient downstream execution. DuckDB natively supports this Arrow-based execution pipeline through Arrow Database Connectivity (ADBC) [59], allowing query execution result tables to be serialized into Arrow and exported to external memory buffers. These buffers can then be transferred with minimal overhead, using RDMA for intra-system communication and gRPC for external delivery. Result Handlers are deployed at both the OASIS-FE and the OASIS-A, where they work in conjunction with their local query engines to forward intermediate or final result tables to the next processing layer.

## F. Operator-Level Query Plan Optimizer and Decomposer

The Local Optimizer is responsible for analyzing the Substrait IR-based query plan received from the client and partitioning it across execution layers based on operator characteristics and data transfer cost. It consists of two core components. First, an optimization algorithm (§IV-G) identifies the optimal decomposition point for execution. Subsequently, the Substrait Decomposer utilizes this point to partition the original plan into two semantically equivalent subplans, thereby enabling efficient query execution across heterogeneous layers.

**Why Substrait IR?** OASIS adopts the Substrait IR [57] to enable fine-grained operator-level partitioning and modular execution across layers. Substrait is a cross-platform, language-agnostic IR designed for interoperability between query engines and execution backends. Compared to SQL, it offers a more structured and expressive form, explicitly encoding operator types, input/output schemas, and expression trees. This structure allows the system to efficiently isolate and recompose subplans with minimal transformation overhead [60]. It also facilitates extensibility through its extensionURI mechanism, enabling the use of user-defined functions and non-standard operators with formal external definitions. When the client submits a SQL query, the system translates it into a Substrait IR-based query plan, embedding all necessary metadata such as schema and object references (§IV-H).

**Substrait Decomposer:** The Substrait Decomposer divides the query plan into two parts based on the operator selected by the optimization algorithm as the decomposition point. The decomposition process begins by traversing the original relational tree to locate the target operator that serves as the decomposition point. Once identified, the subtree rooted at this operator is extracted to construct the OASIS-A subplan. In the original plan, the corresponding node is replaced with a new read operator, thereby forming the OASIS-FE subplan (Figure 5). Each resulting subplan is subsequently reconstructed to comply with the Substrait specification. Specifically, the extensionURI and extensions sections from the original plan are selectively replicated to ensure that all custom operators and functions used in each subplan are correctly defined. The schema of the intermediate result produced by the OASIS-A plan is inferred by analyzing the output structure of the extracted subtree, including operators such as aggregate, project, and read. This analysis captures grouping keys, column names, and data types. To avoid naming conflicts, temporary column names are systematically generated using a unique alphabetical naming convention. Once the intermediate schema is finalized, it is applied consistently to both subplans. The OASIS-A plan is explicitly configured to emit this schema, while the OASIS-FE plan introduces a new read operator that declares the same schema as its input.

This decomposition process forms a semantic bridge between subtree extraction and plan reconstruction. It preserves the logical continuity of data flow while enabling physical modularization of execution. Importantly, the resulting plans are not merely structurally separated but also logically ordered: since each operator in the original Substrait IR plan follows a Directed Acyclic Graph (DAG) based on data dependencies, the OASIS-A plan must be executed first to produce the intermediate output, which is then consumed by the OASIS-FE plan. This strict dependency preserves the original query semantics while enabling efficient execution across disaggregated compute-storage layers.

## G. Optimization Strategies for Query Plan Decomposition

The SODA employed in the Local Optimizer uses two strategies to split Substrait IR plans for HPC tabular queries. The first strategy, Coefficient-Aware Decomposition (CAD), estimates input-to-output ratios (coefficients) using pre-built histograms and selects a split point that minimizes data movement. It is suited for queries involving scalar-based conditions or simple computations. The second strategy, Structure-Aware Placement (SAP), applies when coefficients cannot be reliably estimated from statistics or histograms, such as in queries with array-level conditions or computations. SAP considers the physical data layout to place operators close to the data.

**1) Operator Classification:** It is critical to estimate the data movement introduced by each operator when decomposing a query plan into subplans for the OASIS-FE and OASIS-A. This cost primarily depends on the output size of the last operator executed on the OASIS-A, since its result is passed to the OASIS-FE when execution moves to the upper layer. If the transition occurs after the i-th operator, the output of that operator becomes the input to the (i+1)-th and constitutes the intermediate data that must be transferred. The size of this intermediate result directly impacts the total data movement overhead. To quantify this, OASIS defines a per-operator input-to-output coefficient based on Substrait operator semantics. Using these coefficients, it estimates the input and output sizes of each operator from the initial input size. Operators are then classified into four categories based on their data transformation behavior, as summarized in Table II.

As shown in §III-A, all operators involved in HPC tabular queries fall into either the Op-1 or Op-2 categories. Operators in Op-3 and Op-4 (e.g., join) are thus excluded from coefficient-based cost estimation. Op-1 operators have identical input and output sizes, yielding fixed coefficients. In contrast, Op-2 operators produce variable output sizes depending on filter selectivity or the number of projected columns, resulting in dynamic coefficients. To estimate this variability, OASIS constructs offline histograms at data ingestion time. These histograms capture column value distributions and are later used to estimate filter selectivity and projection effects, allowing accurate output size estimation for Op-2 operators.

Crucially, coefficient estimation is not only used to predict output sizes but also plays a central role in modeling total data movement. Starting from the input size of the initial read operator, OASIS performs chained inference across the operator tree, applying estimated coefficients to compute the input and output sizes of subsequent operators. By combining operator classification, histogram-based estimation, and coefficient inference, OASIS builds a cost model focused on data transfer. This enables the system to identify the optimal query plan split point between the OASIS-FE and OASIS-A, minimizing internal data movement and maximizing offloading efficiency.

**2) Coefficient-Aware Decomposition:** CAD is a strategy designed for query plans involving schemas with scalar-based conditions or computations, where output size can be predicted using coefficient estimation. CAD sequentially infers the input and output sizes of all operators based on their input-output coefficient and the initial input size. To determine the optimal split point, we make the following assumption: Query plans are split under the assumption of one-way data transfer from the lower layer (OASIS-A) to the upper layer (OASIS-FE), without return traffic. This assumption avoids unnecessary costs from round-trips and ensures that once sufficient data reduction occurs at the lower layer, intermediate results can be efficiently transferred and processed at the upper layer.

CAD determines the optimal split point through three sequential steps: (1) Estimate operator-specific input-to-output coefficients using prebuilt histograms; (2) Propagate input and output size estimates across the operator tree based on these coefficients and the initial input size; (3) Select a split point based on two criteria: (a) if a semantic boundary requiring centralized processing (e.g., global sort) is encountered before further data reduction is possible, the plan is split at that point; (b) If maximal data reduction is achieved, execution continues on the OASIS-A until a boundary appears, avoiding unnecessary memory transitions and operator materialization in the upper layer.

A representative boundary is the sort operator, which requires global ordering and must be merged at the upper layer after partial processing. In contrast, operators like aggregate can be safely offloaded, as their commutative and associative properties enable partial aggregation at the lower layer and finalization at the upper layer. Functions like MEDIAN, however, rely on global ordering and cannot be decomposed into partial forms.

**3) Structure-Aware Placement:** SAP is a decomposition strategy designed for query plans involving array-level conditions or computations, typically found in schemas with nested structures such as List or Array. In such cases, coefficient estimation using Parquet statistics or prebuilt histograms is infeasible, as these are collected at the column level and do not capture intra-array value distributions. Because the output size of such operations depends on runtime evaluations over individual array elements, the CAD strategy is not applicable.

To address this, SAP mandates that any condition or expression directly referencing array elements be evaluated at the OASIS-A level. For example, a predicate such as a[i] + a[j] < 0, which depends on the runtime values of individual array elements, cannot be statically predicted and must therefore be executed at the data-resident layer. SAP proceeds in three steps: (1) Analyze the query plan to detect array-aware predicates that reference internal items; (2) Enforce the evaluation of such predicates at the OASIS-A to ensure locality; (3) Evaluate the resulting data size at runtime, and apply a lazy execution strategy that transmits results to the OASIS-FE only when the output remains within acceptable transfer limits or when the boundary requiring centralized processing is encountered.

By statically determining the plan split while dynamically evaluating result transfer sizes, SAP enables effective offloading even when coefficient-based estimation is infeasible. This approach supports fine-grained filtering of nested structures near the data, reducing unnecessary transfers and improving overall processing efficiency.

## H. Client Integration via IR Producer and Pushdown API

Client-side integration with OASIS is enabled via a custom connector, illustrated here using Spark as a representative example. The connector consists of two main components (see Figure 4): (1) an IR Producer that translates the SQL query into a Substrait IR, and (2) a P/D API that transmits the IR plan to the OASIS-FE via gRPC for pushdown execution. Users can access data via the standard .read.format("...") interface without modifying their existing Spark applications. Final query results are serialized in Arrow format and returned to the client, where they can be deserialized directly into Spark DataFrames through the Arrow source interface for further analysis or visualization. This design enables drop-in compatibility with existing Spark pipelines while leveraging the flexibility of the Substrait IR to support integration with other query engines in the future.

---

### النسخة العربية

## أ. مبدأ التصميم

لمعالجة القيود المذكورة أعلاه، نصمم معمارية COS جديدة تحافظ على فوائد التخطيط العمودي والحساب داخل التخزين، مع إدخال معاملات معقدة بدلالات المصفوفات وتمكين تحليل المعاملات المرن عبر طبقات التنفيذ داخل مكدس التخزين.

بتوجيه من هذه الأهداف، نقدم مبادئ التصميم الأساسية (DP) التي تشكل معمارية OASIS.

• **DP#1: دعم تنسيق إخراج موجه نحو الأعمدة لتحليلات HPC.** يجب أن يدعم OASIS كلاً من مخرجات Arrow وCSV لتمكين المعالجة العمودية الفعالة مع الحفاظ على التوافق مع التطبيقات التي تفتقر إلى الدعم الأصلي لـ Arrow، مثل Presto.

• **DP#2: تنفيذ استعلام على مستوى التخزين مع دعم المعاملات المتقدمة والمصفوفات.** كما حللنا في §III-A، غالباً ما تتضمن استعلامات HPC عمليات التجميع والفرز على وحدات المحاكاة، وتعبيرات على مستوى المصفوفات على الكميات الفيزيائية. يجب أن يدعم OASIS هذه المعاملات ودلالات المصفوفات للتنفيذ الفعال والعملي داخل التخزين.

• **DP#3: تحسين مسار الاستعلام الواعي بالتخزين.** يجب أن يقلل OASIS من حركة البيانات الداخلية من خلال إنشاء خطط تنفيذ استعلام هرمية تضع عمليات عالية تكلفة حركة البيانات بالقرب من التخزين وتقلل من حركة الربط البيني والشبكة.

## ب. نظرة عامة

يتكون نظام OASIS المقترح من واجهة أمامية OASIS (OASIS-FE) وخوادم مصفوفات تخزين متعددة (OASIS-A). تتألف OASIS-FE بشكل أساسي من المكونات التالية (§IV-C): بوابة S3، والمحسّن المحلي، ومدير البيانات الوصفية، ومنفذ الاستعلام ومعالج النتائج، ووحدة بادئ NVMe-over-Fabrics (NVMe-oF). تتصل كل OASIS-A بـ OASIS-FE عبر NVMe-oF، مما يتيح إدخال/إخراج عالي الإنتاجية. تتكون OASIS-A من المكونات التالية (§IV-D): هدف NVMe-oF، ومدير التخزين، ومنفذ الاستعلام ومعالج النتائج.

يوضح الشكل 4 عملية تفريغ الاستعلام من البداية إلى النهاية في نظام OASIS. ① تبدأ العملية عندما يرسل محرك استعلام من جانب العميل استعلام SQL. ② يُترجم الاستعلام إلى تمثيل وسيط (IR)، Substrait [57]، الذي يصف خطة التنفيذ على مستوى المعامل (§IV-F). يتم إرسال خطة IR هذه إلى OASIS-FE عبر واجهة برمجة تطبيقات الدفع لأسفل (P/D) الممتدة من OASIS المدمجة في محرك الاستعلام من جانب العميل (§IV-H). ③ تُحوّل بوابة S3 خطة IR إلى المحسّن المحلي. ④ يقسم المحسّن المحلي خطة IR إلى خطة OASIS-FE وخطة OASIS-A. تعتمد خطة OASIS-FE على النتيجة الوسيطة لخطة OASIS-A، مما يُنشئ تبعية تنفيذ. ⑤ يتم إرسال خطة OASIS-A إلى OASIS-A المقابلة للتنفيذ. ⑥ يتم استرجاع الكائن المستهدف من التخزين المحلي عبر مدير التخزين. ⑦ ينفذ محرك استعلام OASIS-A الخطة المعينة ويعيد النتيجة الوسيطة إلى OASIS-FE. ⑧ تسجل OASIS-FE النتيجة في محرك الاستعلام الخاص بها كجدول مؤقت. ⑨ تنفذ OASIS-FE خطة OASIS-FE، ⑩ تنتج ⑪ وتُعيد النتيجة النهائية.

## ج. المكونات الأساسية لـ OASIS-FE

**1) بوابة S3:** تعمل هذه الوحدة كنقطة دخول متصلة بالشبكة تربط عملاء S3 الخارجيين بالمكونات الداخلية لـ OASIS. تتعامل مع تحليل بروتوكول S3 وتترجم العمليات القياسية مثل PutObject وGetObject إلى رسائل gRPC داخلية. تغلف هذه الرسائل البيانات الوصفية للطلب والحمولات، التي يتم إعادة توجيهها بعد ذلك إلى الوحدات اللاحقة لمزيد من المعالجة، مع إرجاع الاستجابات بتنسيق HTTP متوافق مع S3.

**2) المحسّن المحلي:** تحلل هذه الوحدة وتحلل خطط استعلام Substrait IR المفرغة باستخدام خوارزمية تفريغ وتحليل خطة الاستعلام من جانب التخزين (SODA). تقدّر حجم نقل البيانات لكل معامل لتحديد طبقة التنفيذ المثلى، إما في OASIS-FE أو OASIS-A. بعد ذلك، يولد المحسّن المحلي خططاً فرعية لـ OASIS-FE وOASIS-A تأخذ في الاعتبار كلاً من دلالات المعاملات وعبء الاتصال، مما يتيح تنفيذ استعلام فعال مع تقليل حركة البيانات.

**3) مدير البيانات الوصفية:** تدير هذه الوحدة البيانات الوصفية المتعلقة بالتنفيذ وتنفذ الترجمة من المنطقي إلى الفيزيائي للطلبات المستلمة من بوابة S3. عند تلقي رسالة gRPC، تحل الكائن المستهدف عن طريق تعيين اسم دلو S3 ومفتاح الكائن إلى معرف مساحة كائن داخلي ومعرف كائن، يتم الاحتفاظ بها في جدول التعيين الخاص بها. ثم تولد أوامر إدخال/إخراج NVMe المقابلة وترسلها إلى OASIS-A المناسبة للتنفيذ. عند إنشاء دلو جديد، يتم تعيين OASIS-A مقابلة وتخصيص معرف مساحة كائن فريد لتوجيه طلبات الإدخال/الإخراج اللاحقة. يتم تضمين البيانات الوصفية الإضافية مثل حجم الكائن في كل طلب.

لمساعدة المحسّن المحلي في تحليل الاستعلام على مستوى المعامل، يجمع مدير البيانات الوصفية البيانات الوصفية الإحصائية الخفيفة أثناء استيعاب الكائنات. على وجه التحديد، عند حدوث عملية PutObject، يتم إنشاء مخطط هيستوغرام مضغوط عبر العينات ويتم تخزينه محلياً على OASIS-FE باستخدام مفتاح الكائن كفهرس. تغطي هذه المخططات عادةً 0.5-5٪ من الكائن وتلتقط توزيعات على مستوى الأعمدة لأنواع البيانات المختلفة مثل double وint. يستخدم المحسّن المحلي لاحقاً هذه البيانات الوصفية لتقدير انتقائية المعامل وحجم الإخراج، موجهاً تقسيم الخطة ووضعها.

**4) منفذ الاستعلام ومعالج النتائج:** توفر هذه الوحدة محرك تنفيذ خفيف الوزن واعٍ بالأعمدة قادر على تشغيل الاستعلامات مباشرة في طبقة التخزين. يدعم التعبيرات على مستوى المصفوفات لتقييم أحمال العمل العلمية التي تتضمن بنى متداخلة أو متكررة بكفاءة. بعد التنفيذ، يتم تسلسل النتائج إلى تنسيقات محددة من العميل مثل Arrow لنقل عالي الإنتاجية أو CSV/JSON للتوافق مع الأدوات القديمة. يتم وصف تفاصيل التنفيذ الإضافية في §IV-E.

**5) بادئ NVMe-oF:** يعمل هذا المكون كواجهة شبكة تصدر أوامر إدخال/إخراج NVMe إلى خوادم OASIS-A عبر NVMe-oF. تحول OASIS-FE طلبات تخزين الكائنات إلى أوامر NVMe وترسلها عبر نقل RDMA منخفض زمن الاستجابة. يتم تغليف بيانات الكائن والبيانات الوصفية في أمر NVMe واحد ممتد [58].

## د. المكونات الأساسية لـ OASIS-A

**1) هدف NVMe-oF:** تستقبل وحدة هدف NVMe-oF أوامر NVMe من OASIS-FE وتنفذ عمليات إدخال/إخراج الكائنات وفقاً لذلك. يغلف كل أمر كلاً من بيانات الكائن والبيانات الوصفية، مما يسمح لـ OASIS-A بالوصول المباشر إلى الذاكرة وتنفيذ عمليات القراءة/الكتابة دون التعامل المنفصل مع البيانات الوصفية. من خلال الاستفادة من تنسيق أمر كتلة ممتد، يتيح هذا التصميم تنفيذ أمر واحد مع الحد الأدنى من نسخ البيانات ويدعم إدخال/إخراج متوازي قائم على الذاكرة عالي الإنتاجية.

**2) مدير التخزين:** يكون مدير التخزين مسؤولاً عن التعامل مع طلبات التخزين والاسترجاع الصادرة من OASIS-FE باستخدام مخزن كائنات داخلي. يدير البيانات على مستوى البقعة من خلال جدول خصائص البقعة (BPT)، الذي يعين معرفات مساحة الكائنات ومعرفات الكائنات إلى إزاحات فيزيائية على جهاز التخزين. تتبع كل بقعة دورة حياة OPEN–RUN–CLOSE أثناء الإدخال/الإخراج، حيث يتم تهيئة مخازن DMA المؤقتة وقنوات الإدخال/الإخراج للتنفيذ غير المتزامن. يضمن تسجيل الكتابة المسبقة (WAL) اتساق البيانات الوصفية، ويتم استخدام فضاء عنونة قائم على الشرائح لتحسين قابلية التوسع والمحاذاة الفيزيائية. بينما تفاصيل التنفيذ الكاملة خارج نطاق هذا البحث، تتبنى هذه الطبقة مبادئ التصميم الأساسية من أنظمة تخزين الكائنات التقليدية وتوفر واجهة خلفية قوية وقابلة للتوسع لتنفيذ الاستعلام في الطبقة العليا.

**3) منفذ الاستعلام ومعالج النتائج:** يعكس هذا المكون وظيفة نظيره في OASIS-FE، وينفذ الخطط الفرعية المعينة ويعيد النتائج الوسيطة. لتمكين الاتصال السريع والفعال بين OASIS-A وOASIS-FE، يتم تسلسل النتائج الوسيطة باستخدام تنسيق Arrow وإرسالها مرة أخرى إلى OASIS-FE. يتم وصف التفاصيل الإضافية في §IV-E.

## هـ. محرك تنفيذ الاستعلام داخل التخزين ونقل النتائج

منفذ الاستعلام ومعالج النتائج هما مكونان أساسيان في OASIS، مسؤولان عن تحقيق DP#1 وDP#2 داخل طبقة التخزين من خلال تمكين معالجة الاستعلام العمودي داخل طبقة التخزين. وفقاً لذلك، يجب أن يلبي محرك التنفيذ ثلاثة متطلبات رئيسية: (1) الدعم الأصلي للتنسيقات العمودية مثل Arrow، (2) تقييم التعبيرات على العناصر الفردية داخل الأعمدة من نوع المصفوفة، و(3) بيئة تنفيذ خفيفة الوزن تعمل بشكل موثوق في ظل موارد حسابية محدودة.

لتلبية هذه المتطلبات، نتبنى DuckDB [27] كمحرك تنفيذ أساسي داخل طبقة التخزين. DuckDB هو نظام إدارة قواعد بيانات علائقي مدمج مفتوح المصدر محسّن لأحمال عمل المعالجة التحليلية عبر الإنترنت (OLAP)، ويوفر دعماً أصلياً للتنسيقات العمودية مثل Parquet وArrow. يدعم مجموعة واسعة من معاملات SQL - بما في ذلك التجميعات المعقدة والفرز ودوال مستوى المصفوفات - مما يجعله فعالاً بشكل خاص لتفريغ أجزاء استعلام متنوعة. والجدير بالذكر أن DuckDB يدعم كلاً من المعالجة في الذاكرة والتنفيذ القائم على القرص، مما يسمح له بمعالجة مجموعات بيانات عمودية واسعة النطاق بكفاءة تتراوح من عشرات إلى مئات الجيجابايت دون الحاجة إلى تحميل كامل في الذاكرة. هذا يجعله مناسباً بشكل جيد للتنفيذ الخفيف الوزن داخل التخزين.

لتمكين التنفيذ عبر الطبقات الهرمية مع الحفاظ على فوائد المعالجة العمودية لـ DP#3، يسلسل منفذ الاستعلام النتائج الوسيطة والمخرجات النهائية بتنسيق Arrow المضغوط للنقل الفعال إلى الطبقة العليا. للتوافق مع الأدوات القديمة، يمكن أيضاً إخراج المخرجات النهائية بتنسيق CSV أو JSON.

يقلل تخطيط Arrow العمودي ودلالات النسخ الصفري من عبء التسلسل ويمكّن التنفيذ اللاحق الفعال. يدعم DuckDB بشكل أصلي خط أنابيب التنفيذ القائم على Arrow هذا من خلال اتصال قاعدة بيانات Arrow (ADBC) [59]، مما يسمح بتسلسل جداول نتائج تنفيذ الاستعلام إلى Arrow وتصديرها إلى مخازن ذاكرة خارجية مؤقتة. يمكن بعد ذلك نقل هذه المخازن المؤقتة مع الحد الأدنى من العبء، باستخدام RDMA للاتصال داخل النظام وgRPC للتسليم الخارجي. يتم نشر معالجات النتائج في كل من OASIS-FE وOASIS-A، حيث يعملون بالتنسيق مع محركات الاستعلام المحلية الخاصة بهم لإعادة توجيه جداول النتائج الوسيطة أو النهائية إلى طبقة المعالجة التالية.

## و. محسّن وم decomposer خطة الاستعلام على مستوى المعامل

المحسّن المحلي مسؤول عن تحليل خطة الاستعلام القائمة على Substrait IR المستلمة من العميل وتقسيمها عبر طبقات التنفيذ بناءً على خصائص المعاملات وتكلفة نقل البيانات. يتكون من مكونين أساسيين. أولاً، تحدد خوارزمية التحسين (§IV-G) نقطة التحليل المثلى للتنفيذ. بعد ذلك، يستخدم محلل Substrait هذه النقطة لتقسيم الخطة الأصلية إلى خطتين فرعيتين متكافئتين دلالياً، وبالتالي تمكين تنفيذ استعلام فعال عبر الطبقات غير المتجانسة.

**لماذا Substrait IR؟** يتبنى OASIS Substrait IR [57] لتمكين التقسيم الدقيق على مستوى المعامل والتنفيذ النمطي عبر الطبقات. Substrait هو IR عبر الأنظمة الأساسية ومستقل عن اللغة مصمم لقابلية التشغيل البيني بين محركات الاستعلام والواجهات الخلفية للتنفيذ. مقارنةً بـ SQL، يوفر شكلاً أكثر تنظيماً وتعبيراً، يشفر بشكل صريح أنواع المعاملات ومخططات الإدخال/الإخراج وأشجار التعبير. يسمح هذا الهيكل للنظام بعزل وإعادة تركيب الخطط الفرعية بكفاءة مع الحد الأدنى من عبء التحويل [60]. كما يسهل قابلية التوسع من خلال آلية extensionURI الخاصة به، مما يتيح استخدام دوال معرّفة من قبل المستخدم ومعاملات غير قياسية مع تعريفات خارجية رسمية. عندما يرسل العميل استعلام SQL، يترجمه النظام إلى خطة استعلام قائمة على Substrait IR، مضمناً جميع البيانات الوصفية الضرورية مثل المخطط ومراجع الكائنات (§IV-H).

**محلل Substrait:** يقسم محلل Substrait خطة الاستعلام إلى جزأين بناءً على المعامل المحدد بواسطة خوارزمية التحسين كنقطة تحليل. تبدأ عملية التحليل بالمرور على شجرة العلاقات الأصلية لتحديد موقع المعامل المستهدف الذي يعمل كنقطة تحليل. بمجرد تحديده، يتم استخراج الشجرة الفرعية المتجذرة في هذا المعامل لبناء خطة OASIS-A الفرعية. في الخطة الأصلية، يتم استبدال العقدة المقابلة بمعامل قراءة جديد، وبالتالي تشكيل خطة OASIS-FE الفرعية (الشكل 5). يتم بعد ذلك إعادة بناء كل خطة فرعية ناتجة للامتثال لمواصفات Substrait. على وجه التحديد، يتم نسخ أقسام extensionURI وextensions من الخطة الأصلية بشكل انتقائي لضمان تعريف جميع المعاملات والدوال المخصصة المستخدمة في كل خطة فرعية بشكل صحيح. يتم استنتاج مخطط النتيجة الوسيطة الذي تنتجه خطة OASIS-A من خلال تحليل بنية الإخراج للشجرة الفرعية المستخرجة، بما في ذلك المعاملات مثل التجميع والإسقاط والقراءة. يلتقط هذا التحليل مفاتيح التجميع وأسماء الأعمدة وأنواع البيانات. لتجنب تعارضات التسمية، يتم إنشاء أسماء أعمدة مؤقتة بشكل منهجي باستخدام اصطلاح تسمية أبجدي فريد. بمجرد الانتهاء من المخطط الوسيط، يتم تطبيقه بشكل متسق على كلتا الخطتين الفرعيتين. يتم تكوين خطة OASIS-A بشكل صريح لإخراج هذا المخطط، بينما تقدم خطة OASIS-FE معامل قراءة جديد يعلن نفس المخطط كمدخل له.

تشكل عملية التحليل هذه جسراً دلالياً بين استخراج الشجرة الفرعية وإعادة بناء الخطة. تحافظ على استمرارية منطقية لتدفق البيانات مع تمكين النمذجة الفيزيائية للتنفيذ. والأهم من ذلك، أن الخطط الناتجة ليست منفصلة هيكلياً فحسب، بل مرتبة منطقياً أيضاً: نظراً لأن كل معامل في خطة Substrait IR الأصلية يتبع رسماً بيانياً موجهاً لا دوري (DAG) بناءً على تبعيات البيانات، يجب تنفيذ خطة OASIS-A أولاً لإنتاج الإخراج الوسيط، الذي يتم استهلاكه بعد ذلك بواسطة خطة OASIS-FE. يحافظ هذا التبعية الصارمة على دلالات الاستعلام الأصلية مع تمكين التنفيذ الفعال عبر طبقات الحساب-التخزين المفصولة.

## ز. استراتيجيات التحسين لتحليل خطة الاستعلام

تستخدم SODA المستخدمة في المحسّن المحلي استراتيجيتين لتقسيم خطط Substrait IR لاستعلامات HPC الجدولية. الاستراتيجية الأولى، التحليل الواعي بالمعامل (CAD)، تقدر نسب الإدخال إلى الإخراج (المعاملات) باستخدام مخططات هيستوغرام مبنية مسبقاً وتختار نقطة تقسيم تقلل من حركة البيانات. إنها مناسبة للاستعلامات التي تتضمن شروطاً قائمة على القياسية أو حسابات بسيطة. الاستراتيجية الثانية، الوضع الواعي بالبنية (SAP)، تنطبق عندما لا يمكن تقدير المعاملات بشكل موثوق من الإحصائيات أو المخططات الهيستوغرامية، كما هو الحال في الاستعلامات ذات الشروط أو الحسابات على مستوى المصفوفات. يأخذ SAP في الاعتبار تخطيط البيانات الفيزيائي لوضع المعاملات بالقرب من البيانات.

**1) تصنيف المعاملات:** من الأهمية بمكان تقدير حركة البيانات التي يقدمها كل معامل عند تحليل خطة استعلام إلى خطط فرعية لـ OASIS-FE وOASIS-A. تعتمد هذه التكلفة بشكل أساسي على حجم إخراج المعامل الأخير المنفذ على OASIS-A، حيث يتم تمرير نتيجته إلى OASIS-FE عندما ينتقل التنفيذ إلى الطبقة العليا. إذا حدث الانتقال بعد المعامل i-th، يصبح إخراج هذا المعامل مدخلاً للمعامل (i+1)-th ويشكل البيانات الوسيطة التي يجب نقلها. يؤثر حجم هذه النتيجة الوسيطة بشكل مباشر على إجمالي عبء حركة البيانات. لقياس هذا كمياً، يحدد OASIS معاملاً من الإدخال إلى الإخراج لكل معامل بناءً على دلالات معامل Substrait. باستخدام هذه المعاملات، تقدر أحجام الإدخال والإخراج لكل معامل من حجم الإدخال الأولي. ثم يتم تصنيف المعاملات إلى أربع فئات بناءً على سلوك تحويل البيانات الخاص بها، كما هو ملخص في الجدول II.

كما هو موضح في §III-A، تقع جميع المعاملات المعنية في استعلامات HPC الجدولية ضمن فئتي Op-1 أو Op-2. وبالتالي، يتم استبعاد المعاملات في Op-3 وOp-4 (مثل الضم) من تقدير التكلفة القائم على المعاملات. معاملات Op-1 لها أحجام إدخال وإخراج متطابقة، مما ينتج معاملات ثابتة. في المقابل، تنتج معاملات Op-2 أحجام إخراج متغيرة اعتماداً على انتقائية المرشح أو عدد الأعمدة المسقطة، مما ينتج معاملات ديناميكية. لتقدير هذا التباين، يبني OASIS مخططات هيستوغرام دون اتصال في وقت استيعاب البيانات. تلتقط هذه المخططات توزيعات قيم الأعمدة وتُستخدم لاحقاً لتقدير انتقائية المرشح وتأثيرات الإسقاط، مما يسمح بتقدير دقيق لحجم الإخراج لمعاملات Op-2.

بشكل حاسم، لا يُستخدم تقدير المعامل فقط للتنبؤ بأحجام الإخراج ولكن يلعب أيضاً دوراً مركزياً في نمذجة إجمالي حركة البيانات. بدءاً من حجم إدخال معامل القراءة الأولي، ينفذ OASIS استدلالاً متسلسلاً عبر شجرة المعاملات، مطبقاً المعاملات المقدرة لحساب أحجام الإدخال والإخراج للمعاملات اللاحقة. من خلال الجمع بين تصنيف المعاملات والتقدير القائم على المخططات الهيستوغرامية واستنتاج المعاملات، يبني OASIS نموذج تكلفة يركز على نقل البيانات. يمكّن هذا النظام من تحديد نقطة تقسيم خطة الاستعلام المثلى بين OASIS-FE وOASIS-A، وتقليل حركة البيانات الداخلية وتعظيم كفاءة التفريغ.

**2) التحليل الواعي بالمعامل:** CAD هي استراتيجية مصممة لخطط الاستعلام التي تتضمن مخططات ذات شروط أو حسابات قائمة على القياسية، حيث يمكن التنبؤ بحجم الإخراج باستخدام تقدير المعاملات. يستنتج CAD بشكل متسلسل أحجام الإدخال والإخراج لجميع المعاملات بناءً على معامل الإدخال-الإخراج الخاص بها وحجم الإدخال الأولي. لتحديد نقطة التقسيم المثلى، نضع الافتراض التالي: يتم تقسيم خطط الاستعلام على افتراض نقل البيانات أحادي الاتجاه من الطبقة السفلى (OASIS-A) إلى الطبقة العليا (OASIS-FE)، دون حركة عودة. يتجنب هذا الافتراض التكاليف غير الضرورية من الرحلات ذهاباً وإياباً ويضمن أنه بمجرد حدوث تقليل كافٍ للبيانات في الطبقة السفلى، يمكن نقل النتائج الوسيطة ومعالجتها بكفاءة في الطبقة العليا.

يحدد CAD نقطة التقسيم المثلى من خلال ثلاث خطوات متسلسلة: (1) تقدير معاملات الإدخال إلى الإخراج الخاصة بالمعامل باستخدام مخططات هيستوغرام مبنية مسبقاً؛ (2) نشر تقديرات حجم الإدخال والإخراج عبر شجرة المعاملات بناءً على هذه المعاملات وحجم الإدخال الأولي؛ (3) اختيار نقطة تقسيم بناءً على معيارين: (أ) إذا تم مواجهة حدود دلالية تتطلب معالجة مركزية (مثل الفرز العام) قبل أن يكون من الممكن إجراء مزيد من تقليل البيانات، يتم تقسيم الخطة عند تلك النقطة؛ (ب) إذا تم تحقيق أقصى تقليل للبيانات، يستمر التنفيذ على OASIS-A حتى يظهر حد، متجنباً انتقالات الذاكرة غير الضرورية وتجسيد المعامل في الطبقة العليا.

حد تمثيلي هو معامل الفرز، الذي يتطلب ترتيباً عاماً ويجب دمجه في الطبقة العليا بعد المعالجة الجزئية. في المقابل، يمكن تفريغ المعاملات مثل التجميع بأمان، حيث تمكّن خصائصها التبديلية والترابطية التجميع الجزئي في الطبقة السفلى والانتهاء في الطبقة العليا. ومع ذلك، تعتمد الدوال مثل MEDIAN على الترتيب العام ولا يمكن تحليلها إلى أشكال جزئية.

**3) الوضع الواعي بالبنية:** SAP هي استراتيجية تحليل مصممة لخطط الاستعلام التي تتضمن شروطاً أو حسابات على مستوى المصفوفات، توجد عادةً في المخططات ذات البنى المتداخلة مثل List أو Array. في مثل هذه الحالات، يكون تقدير المعاملات باستخدام إحصائيات Parquet أو المخططات الهيستوغرامية المبنية مسبقاً غير ممكن، حيث يتم جمعها على مستوى الأعمدة ولا تلتقط توزيعات القيم داخل المصفوفة. نظراً لأن حجم إخراج مثل هذه العمليات يعتمد على تقييمات وقت التشغيل على عناصر المصفوفة الفردية، فإن استراتيجية CAD غير قابلة للتطبيق.

لمعالجة هذا، يفرض SAP أن يتم تقييم أي شرط أو تعبير يشير مباشرة إلى عناصر المصفوفة على مستوى OASIS-A. على سبيل المثال، محمول مثل a[i] + a[j] < 0، الذي يعتمد على قيم وقت التشغيل لعناصر المصفوفة الفردية، لا يمكن التنبؤ به بشكل ثابت ولذلك يجب تنفيذه في الطبقة المقيمة بالبيانات. يتقدم SAP في ثلاث خطوات: (1) تحليل خطة الاستعلام لاكتشاف المحمولات الواعية بالمصفوفات التي تشير إلى عناصر داخلية؛ (2) فرض تقييم مثل هذه المحمولات في OASIS-A لضمان الموضعية؛ (3) تقييم حجم البيانات الناتجة في وقت التشغيل، وتطبيق استراتيجية تنفيذ كسولة تنقل النتائج إلى OASIS-FE فقط عندما يبقى الإخراج ضمن حدود النقل المقبولة أو عندما يتم مواجهة الحد الذي يتطلب معالجة مركزية.

من خلال تحديد تقسيم الخطة بشكل ثابت مع تقييم أحجام نقل النتائج ديناميكياً، يتيح SAP التفريغ الفعال حتى عندما يكون التقدير القائم على المعاملات غير ممكن. يدعم هذا النهج الترشيح الدقيق للبنى المتداخلة بالقرب من البيانات، مما يقلل من عمليات النقل غير الضرورية ويحسن الكفاءة الإجمالية للمعالجة.

## ح. تكامل العميل عبر منتج IR وواجهة برمجة تطبيقات الدفع لأسفل

يتم تمكين التكامل من جانب العميل مع OASIS عبر موصل مخصص، موضح هنا باستخدام Spark كمثال تمثيلي. يتكون الموصل من مكونين رئيسيين (انظر الشكل 4): (1) منتج IR يترجم استعلام SQL إلى Substrait IR، و(2) واجهة برمجة تطبيقات P/D تنقل خطة IR إلى OASIS-FE عبر gRPC لتنفيذ الدفع لأسفل. يمكن للمستخدمين الوصول إلى البيانات عبر الواجهة القياسية .read.format("...") دون تعديل تطبيقات Spark الموجودة لديهم. يتم تسلسل نتائج الاستعلام النهائية بتنسيق Arrow وإعادتها إلى العميل، حيث يمكن إلغاء تسلسلها مباشرة إلى Spark DataFrames من خلال واجهة مصدر Arrow لمزيد من التحليل أو التصوير. يتيح هذا التصميم توافقاً مباشراً مع خطوط أنابيب Spark الموجودة مع الاستفادة من مرونة Substrait IR لدعم التكامل مع محركات استعلام أخرى في المستقبل.

---

### Translation Notes

- **Figures referenced:** Figure 4, Figure 5
- **Tables referenced:** Table II
- **Key terms introduced:** OASIS-FE, OASIS-A, NVMe-oF, Substrait IR, SODA, CAD, SAP, DuckDB, SPDK, gRPC, ADBC, DAG, BPT, WAL, OLAP
- **Equations:** None
- **Citations:** [27], [57]-[60] referenced
- **Special handling:**
  - Component names kept consistent (OASIS-FE, OASIS-A)
  - Software/protocol names kept in English (DuckDB, NVMe-oF, RDMA, Substrait, gRPC, Arrow, SPDK)
  - Algorithm names kept in English (SODA, CAD, SAP, ADBC, DAG, BPT, WAL)
  - Numbered steps in process flows maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
