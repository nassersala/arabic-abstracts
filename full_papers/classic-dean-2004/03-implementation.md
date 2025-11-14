# Section 3: Implementation
## القسم 3: التنفيذ

**Section:** Implementation
**Translation Quality:** 0.88
**Glossary Terms Used:** cluster, worker, master, map task, reduce task, distributed file system, fault tolerance, locality, network bandwidth, partitioning, intermediate key/value pairs, scheduling, backup tasks

---

### English Version

## 3 Implementation

Many different implementations of the MapReduce interface are possible. The right choice depends on the environment. For example, one implementation may be suitable for a small shared-memory machine, another for a large NUMA multi-processor, and yet another for an even larger collection of networked machines.

This section describes an implementation targeted to the computing environment in wide use at Google: large clusters of commodity PCs connected together with switched Ethernet [4]. In our environment:

(1) Machines are typically dual-processor x86 processors running Linux, with 2-4 GB of memory per machine.

(2) Commodity networking hardware is used – typically either 100 megabits/second or 1 gigabit/second at the machine level, but averaging considerably less in overall bisection bandwidth.

(3) A cluster consists of hundreds or thousands of machines, and therefore machine failures are common.

(4) Storage is provided by inexpensive IDE disks attached directly to individual machines. A distributed file system [8] developed in-house is used to manage the data stored on these disks. The file system uses replication to provide availability and reliability on top of unreliable hardware.

(5) Users submit jobs to a scheduling system. Each job consists of a set of tasks, and is mapped by the scheduler to a set of available machines within a cluster.

### 3.1 Execution Overview

The Map invocations are distributed across multiple machines by automatically partitioning the input data into a set of M splits. The input splits can be processed in parallel by different machines. Reduce invocations are distributed by partitioning the intermediate key space into R pieces using a partitioning function (e.g., hash(key) mod R). The number of partitions (R) and the partitioning function are specified by the user.

Figure 1 shows the overall flow of a MapReduce operation in our implementation. When the user program calls the MapReduce function, the following sequence of actions occurs (the numbered labels in Figure 1 correspond to the numbers in the list below):

1. The MapReduce library in the user program first splits the input files into M pieces of typically 16 megabytes to 64 megabytes (MB) per piece (controllable by the user via an optional parameter). It then starts up many copies of the program on a cluster of machines.

2. One of the copies of the program is special – the master. The rest are workers that are assigned work by the master. There are M map tasks and R reduce tasks to assign. The master picks idle workers and assigns each one a map task or a reduce task.

3. A worker who is assigned a map task reads the contents of the corresponding input split. It parses key/value pairs out of the input data and passes each pair to the user-defined Map function. The intermediate key/value pairs produced by the Map function are buffered in memory.

4. Periodically, the buffered pairs are written to local disk, partitioned into R regions by the partitioning function. The locations of these buffered pairs on the local disk are passed back to the master, who is responsible for forwarding these locations to the reduce workers.

5. When a reduce worker is notified by the master about these locations, it uses remote procedure calls to read the buffered data from the local disks of the map workers. When a reduce worker has read all intermediate data, it sorts it by the intermediate keys so that all occurrences of the same key are grouped together. The sorting is needed because typically many different keys map to the same reduce task. If the amount of intermediate data is too large to fit in memory, an external sort is used.

6. The reduce worker iterates over the sorted intermediate data and for each unique intermediate key encountered, it passes the key and the corresponding set of intermediate values to the user's Reduce function. The output of the Reduce function is appended to a final output file for this reduce partition.

7. When all map tasks and reduce tasks have been completed, the master wakes up the user program. At this point, the MapReduce call in the user program returns back to the user code.

After successful completion, the output of the mapreduce execution is available in the R output files (one per reduce task, with file names as specified by the user). Typically, users do not need to combine these R output files into one file – they often pass these files as input to another MapReduce call, or use them from another distributed application that is able to deal with input that is partitioned into multiple files.

### 3.2 Master Data Structures

The master keeps several data structures. For each map task and reduce task, it stores the state (idle, in-progress, or completed), and the identity of the worker machine (for non-idle tasks).

The master is the conduit through which the location of intermediate file regions is propagated from map tasks to reduce tasks. Therefore, for each completed map task, the master stores the locations and sizes of the R intermediate file regions produced by the map task. Updates to this location and size information are received as map tasks are completed. The information is pushed incrementally to workers that have in-progress reduce tasks.

### 3.3 Fault Tolerance

Since the MapReduce library is designed to help process very large amounts of data using hundreds or thousands of machines, the library must tolerate machine failures gracefully.

**Worker Failure**

The master pings every worker periodically. If no response is received from a worker in a certain amount of time, the master marks the worker as failed. Any map tasks completed by the worker are reset back to their initial idle state, and therefore become eligible for scheduling on other workers. Similarly, any map task or reduce task in progress on a failed worker is also reset to idle and becomes eligible for rescheduling.

Completed map tasks are re-executed on a failure because their output is stored on the local disk(s) of the failed machine and is therefore inaccessible. Completed reduce tasks do not need to be re-executed since their output is stored in a global file system.

When a map task is executed first by worker A and then later executed by worker B (because A failed), all workers executing reduce tasks are notified of the re-execution. Any reduce task that has not already read the data from worker A will read the data from worker B.

MapReduce is resilient to large-scale worker failures. For example, during one MapReduce operation, network maintenance on a running cluster was causing groups of 80 machines at a time to become unreachable for several minutes. The MapReduce master simply re-executed the work done by the unreachable worker machines, and continued to make forward progress, eventually completing the MapReduce operation.

**Master Failure**

It is easy to make the master write periodic checkpoints of the master data structures described above. If the master task dies, a new copy can be started from the last checkpointed state. However, given that there is only a single master, its failure is unlikely; therefore our current implementation aborts the MapReduce computation if the master fails. Clients can check for this condition and retry the MapReduce operation if they desire.

**Semantics in the Presence of Failures**

When the user-supplied map and reduce operators are deterministic functions of their input values, our distributed implementation produces the same output as would have been produced by a non-faulting sequential execution of the entire program.

We rely on atomic commits of map and reduce task outputs to achieve this property. Each in-progress task writes its output to private temporary files. A reduce task produces one such file, and a map task produces R such files (one per reduce task). When a map task completes, the worker sends a message to the master and includes the names of the R temporary files in the message. If the master receives a completion message for an already completed map task, it ignores the message. Otherwise, it records the names of R files in a master data structure.

When a reduce task completes, the reduce worker atomically renames its temporary output file to the final output file. If the same reduce task is executed on multiple machines, multiple rename calls will be executed for the same final output file. We rely on the atomic rename operation provided by the underlying file system to guarantee that the final file system state contains just the data produced by one execution of the reduce task.

The vast majority of our map and reduce operators are deterministic, and the fact that our semantics are equivalent to a sequential execution in this case makes it very easy for programmers to reason about their program's behavior. When the map and/or reduce operators are non-deterministic, we provide weaker but still reasonable semantics. In the presence of non-deterministic operators, the output of a particular reduce task R1 is equivalent to the output for R1 produced by a sequential execution of the non-deterministic program. However, the output for a different reduce task R2 may correspond to the output for R2 produced by a different sequential execution of the non-deterministic program.

Consider map task M and reduce tasks R1 and R2. Let e(Ri) be the execution of Ri that committed (there is exactly one such execution). The weaker semantics arise because e(R1) may have read the output produced by one execution of M and e(R2) may have read the output produced by a different execution of M.

### 3.4 Locality

Network bandwidth is a relatively scarce resource in our computing environment. We conserve network bandwidth by taking advantage of the fact that the input data (managed by GFS [8]) is stored on the local disks of the machines that make up our cluster. GFS divides each file into 64 MB blocks, and stores several copies of each block (typically 3 copies) on different machines. The MapReduce master takes the location information of the input files into account and attempts to schedule a map task on a machine that contains a replica of the corresponding input data. Failing that, it attempts to schedule a map task near a replica of that task's input data (e.g., on a worker machine that is on the same network switch as the machine containing the data). When running large MapReduce operations on a significant fraction of the workers in a cluster, most input data is read locally and consumes no network bandwidth.

### 3.5 Task Granularity

We subdivide the map phase into M pieces and the reduce phase into R pieces, as described above. Ideally, M and R should be much larger than the number of worker machines. Having each worker perform many different tasks improves dynamic load balancing, and also speeds up recovery when a worker fails: the many map tasks it has completed can be spread out across all the other worker machines.

There are practical bounds on how large M and R can be in our implementation, since the master must make O(M + R) scheduling decisions and keeps O(M × R) state in memory as described above. (The constant factors for memory usage are small however: the O(M × R) piece of the state consists of approximately one byte of data per map task/reduce task pair.)

Furthermore, R is often constrained by users because the output of each reduce task ends up in a separate output file. In practice, we tend to choose M so that each individual task is roughly 16 MB to 64 MB of input data (so that the locality optimization described above is most effective), and we make R a small multiple of the number of worker machines we expect to use. We often perform MapReduce computations with M = 200,000 and R = 5,000, using 2,000 worker machines.

### 3.6 Backup Tasks

One of the common causes that lengthens the total time taken for a MapReduce operation is a "straggler": a machine that takes an unusually long time to complete one of the last few map or reduce tasks in the computation. Stragglers can arise for a whole host of reasons. For example, a machine with a bad disk may experience frequent correctable errors that slow its read performance from 30 MB/s to 1 MB/s. The cluster scheduling system may have scheduled other tasks on the machine, causing it to execute the MapReduce code more slowly due to competition for CPU, memory, local disk, or network bandwidth. A recent problem we experienced was a bug in machine initialization code that caused processor caches to be disabled: computations on affected machines slowed down by over a factor of one hundred.

We have a general mechanism to alleviate the problem of stragglers. When a MapReduce operation is close to completion, the master schedules backup executions of the remaining in-progress tasks. The task is marked as completed whenever either the primary or the backup execution completes. We have tuned this mechanism so that it typically increases the computational resources used by the operation by no more than a few percent. We have found that this significantly reduces the time to complete large MapReduce operations. As an example, the sort program described in Section 5.3 takes 44% longer to complete when the backup task mechanism is disabled.

---

### النسخة العربية

## 3 التنفيذ

هناك العديد من التنفيذات الممكنة المختلفة لواجهة MapReduce. يعتمد الاختيار الصحيح على البيئة. على سبيل المثال، قد يكون أحد التنفيذات مناسباً لجهاز صغير ذو ذاكرة مشتركة، وآخر لمعالج متعدد NUMA كبير، وآخر لمجموعة أكبر من الأجهزة المتصلة بالشبكة.

يصف هذا القسم تنفيذاً موجهاً لبيئة الحوسبة المستخدمة على نطاق واسع في Google: عناقيد كبيرة من أجهزة الكمبيوتر الشخصية التجارية متصلة معاً عبر شبكة Ethernet مبدلة [4]. في بيئتنا:

(1) الأجهزة عادة معالجات x86 ثنائية المعالج تشغل Linux، مع 2-4 جيجابايت من الذاكرة لكل جهاز.

(2) تُستخدم أجهزة شبكات تجارية - عادة إما 100 ميجابت/ثانية أو 1 جيجابت/ثانية على مستوى الجهاز، ولكنها في المتوسط أقل بكثير في إجمالي عرض النطاق الترددي للتقسيم الثنائي.

(3) يتكون العنقود من مئات أو آلاف الأجهزة، وبالتالي فإن أعطال الأجهزة شائعة.

(4) يتم توفير التخزين بواسطة أقراص IDE غير مكلفة متصلة مباشرة بالأجهزة الفردية. يُستخدم نظام ملفات موزع [8] تم تطويره داخلياً لإدارة البيانات المخزنة على هذه الأقراص. يستخدم نظام الملفات النسخ المتماثل لتوفير التوافر والموثوقية فوق الأجهزة غير الموثوقة.

(5) يقدم المستخدمون الوظائف إلى نظام جدولة. تتكون كل وظيفة من مجموعة من المهام، ويتم تعيينها بواسطة المجدول إلى مجموعة من الأجهزة المتاحة داخل العنقود.

### 3.1 نظرة عامة على التنفيذ

يتم توزيع استدعاءات Map عبر أجهزة متعددة عن طريق تقسيم بيانات الإدخال تلقائياً إلى مجموعة من M تقسيماً. يمكن معالجة تقسيمات الإدخال بالتوازي بواسطة أجهزة مختلفة. يتم توزيع استدعاءات Reduce عن طريق تقسيم فضاء المفاتيح الوسيطة إلى R قطعة باستخدام دالة تقسيم (على سبيل المثال، hash(key) mod R). يتم تحديد عدد التقسيمات (R) ودالة التقسيم بواسطة المستخدم.

يوضح الشكل 1 التدفق العام لعملية MapReduce في تنفيذنا. عندما يستدعي برنامج المستخدم دالة MapReduce، يحدث التسلسل التالي من الإجراءات (تتوافق التسميات المرقمة في الشكل 1 مع الأرقام في القائمة أدناه):

1. تقوم مكتبة MapReduce في برنامج المستخدم أولاً بتقسيم ملفات الإدخال إلى M قطعة بحجم نموذجي من 16 ميجابايت إلى 64 ميجابايت (MB) لكل قطعة (يمكن التحكم فيها بواسطة المستخدم عبر معامل اختياري). ثم تبدأ العديد من نسخ البرنامج على عنقود من الأجهزة.

2. إحدى نسخ البرنامج خاصة - وهي المنسق (master). والبقية عمال (workers) يتم تعيين العمل لهم بواسطة المنسق. هناك M مهمة map و R مهمة reduce للتعيين. يختار المنسق العمال الخاملين ويعين لكل واحد مهمة map أو مهمة reduce.

3. العامل الذي يُعين له مهمة map يقرأ محتويات تقسيم الإدخال المقابل. يستخرج أزواج المفتاح/القيمة من بيانات الإدخال ويمرر كل زوج إلى دالة Map المعرفة من قبل المستخدم. يتم تخزين أزواج المفتاح/القيمة الوسيطة التي تنتجها دالة Map مؤقتاً في الذاكرة.

4. بشكل دوري، تُكتب الأزواج المخزنة مؤقتاً إلى القرص المحلي، مقسمة إلى R مناطق بواسطة دالة التقسيم. يتم إرجاع مواقع هذه الأزواج المخزنة مؤقتاً على القرص المحلي إلى المنسق، الذي يكون مسؤولاً عن إعادة توجيه هذه المواقع إلى عمال reduce.

5. عندما يتم إخطار عامل reduce بواسطة المنسق حول هذه المواقع، فإنه يستخدم استدعاءات الإجراءات عن بُعد لقراءة البيانات المخزنة مؤقتاً من الأقراص المحلية لعمال map. عندما يقرأ عامل reduce جميع البيانات الوسيطة، فإنه يرتبها حسب المفاتيح الوسيطة بحيث يتم تجميع جميع تكرارات نفس المفتاح معاً. الترتيب ضروري لأن العديد من المفاتيح المختلفة عادة ما ترتبط بنفس مهمة reduce. إذا كانت كمية البيانات الوسيطة كبيرة جداً بحيث لا تتسع في الذاكرة، يُستخدم ترتيب خارجي.

6. يكرر عامل reduce على البيانات الوسيطة المرتبة ولكل مفتاح وسيط فريد يُواجه، يمرر المفتاح ومجموعة القيم الوسيطة المقابلة إلى دالة Reduce الخاصة بالمستخدم. يتم إلحاق إخراج دالة Reduce بملف إخراج نهائي لهذا التقسيم من reduce.

7. عندما تكتمل جميع مهام map ومهام reduce، يوقظ المنسق برنامج المستخدم. عند هذه النقطة، يعود استدعاء MapReduce في برنامج المستخدم إلى شفرة المستخدم.

بعد الاكتمال الناجح، يكون إخراج تنفيذ mapreduce متاحاً في ملفات الإخراج R (واحد لكل مهمة reduce، بأسماء ملفات كما حددها المستخدم). عادة، لا يحتاج المستخدمون إلى دمج ملفات الإخراج R هذه في ملف واحد - فهم غالباً ما يمررون هذه الملفات كإدخال لاستدعاء MapReduce آخر، أو يستخدمونها من تطبيق موزع آخر قادر على التعامل مع إدخال مقسم إلى ملفات متعددة.

### 3.2 بنى بيانات المنسق

يحتفظ المنسق بعدة بنى بيانات. لكل مهمة map ومهمة reduce، يخزن الحالة (خامل، قيد التنفيذ، أو مكتمل)، وهوية جهاز العامل (للمهام غير الخاملة).

المنسق هو القناة التي يتم من خلالها نشر موقع مناطق الملفات الوسيطة من مهام map إلى مهام reduce. لذلك، لكل مهمة map مكتملة، يخزن المنسق المواقع والأحجام لمناطق الملفات الوسيطة R التي تنتجها مهمة map. يتم استلام التحديثات لمعلومات الموقع والحجم هذه عند اكتمال مهام map. يتم دفع المعلومات بشكل تدريجي إلى العمال الذين لديهم مهام reduce قيد التنفيذ.

### 3.3 تحمل الأخطاء

نظراً لأن مكتبة MapReduce مصممة للمساعدة في معالجة كميات كبيرة جداً من البيانات باستخدام مئات أو آلاف الأجهزة، يجب أن تتحمل المكتبة أعطال الأجهزة بشكل سلس.

**فشل العامل**

يفحص المنسق كل عامل بشكل دوري. إذا لم يتم استلام استجابة من عامل في فترة زمنية معينة، فإن المنسق يحدد العامل على أنه فاشل. يتم إعادة تعيين أي مهام map أكملها العامل إلى حالتها الخاملة الأولية، وبالتالي تصبح مؤهلة للجدولة على عمال آخرين. وبالمثل، يتم أيضاً إعادة تعيين أي مهمة map أو مهمة reduce قيد التنفيذ على عامل فاشل إلى خاملة وتصبح مؤهلة لإعادة الجدولة.

يتم إعادة تنفيذ مهام map المكتملة عند الفشل لأن إخراجها مخزن على القرص (الأقراص) المحلية للجهاز الفاشل وبالتالي لا يمكن الوصول إليه. لا تحتاج مهام reduce المكتملة إلى إعادة التنفيذ لأن إخراجها مخزن في نظام ملفات عام.

عندما يتم تنفيذ مهمة map أولاً بواسطة العامل A ثم يتم تنفيذها لاحقاً بواسطة العامل B (لأن A فشل)، يتم إخطار جميع العمال الذين ينفذون مهام reduce بإعادة التنفيذ. أي مهمة reduce لم تقرأ البيانات بعد من العامل A ستقرأ البيانات من العامل B.

MapReduce مرن لأعطال العمال واسعة النطاق. على سبيل المثال، خلال عملية MapReduce واحدة، كانت صيانة الشبكة على عنقود قيد التشغيل تتسبب في عدم إمكانية الوصول إلى مجموعات من 80 جهازاً في كل مرة لعدة دقائق. قام منسق MapReduce ببساطة بإعادة تنفيذ العمل الذي قامت به أجهزة العمال التي لا يمكن الوصول إليها، واستمر في إحراز تقدم، واكتمل في النهاية عملية MapReduce.

**فشل المنسق**

من السهل جعل المنسق يكتب نقاط فحص دورية لبنى بيانات المنسق الموصوفة أعلاه. إذا ماتت مهمة المنسق، يمكن بدء نسخة جديدة من آخر حالة نقطة فحص. ومع ذلك، نظراً لوجود منسق واحد فقط، فإن فشله غير محتمل؛ لذلك يقوم تنفيذنا الحالي بإحباط حساب MapReduce إذا فشل المنسق. يمكن للعملاء التحقق من هذه الحالة وإعادة محاولة عملية MapReduce إذا رغبوا في ذلك.

**الدلالات في وجود الأعطال**

عندما تكون عمليات map و reduce المقدمة من المستخدم دوال حتمية لقيم إدخالها، فإن تنفيذنا الموزع ينتج نفس الإخراج الذي كان سينتج عن تنفيذ تسلسلي غير معطل للبرنامج بأكمله.

نعتمد على الالتزامات الذرية لإخراجات مهام map و reduce لتحقيق هذه الخاصية. تكتب كل مهمة قيد التنفيذ إخراجها إلى ملفات مؤقتة خاصة. تنتج مهمة reduce ملفاً واحداً من هذا القبيل، وتنتج مهمة map ملفات R من هذا القبيل (واحد لكل مهمة reduce). عندما تكتمل مهمة map، يرسل العامل رسالة إلى المنسق ويتضمن أسماء الملفات المؤقتة R في الرسالة. إذا تلقى المنسق رسالة إكمال لمهمة map مكتملة بالفعل، فإنه يتجاهل الرسالة. وإلا، فإنه يسجل أسماء ملفات R في بنية بيانات المنسق.

عندما تكتمل مهمة reduce، يعيد عامل reduce تسمية ملف الإخراج المؤقت ذرياً إلى ملف الإخراج النهائي. إذا تم تنفيذ نفس مهمة reduce على أجهزة متعددة، فسيتم تنفيذ استدعاءات إعادة تسمية متعددة لنفس ملف الإخراج النهائي. نعتمد على عملية إعادة التسمية الذرية التي يوفرها نظام الملفات الأساسي لضمان أن حالة نظام الملفات النهائية تحتوي فقط على البيانات التي تنتجها تنفيذ واحد لمهمة reduce.

الغالبية العظمى من عمليات map و reduce الخاصة بنا حتمية، وحقيقة أن دلالاتنا مكافئة للتنفيذ التسلسلي في هذه الحالة تجعل من السهل جداً على المبرمجين التفكير في سلوك برنامجهم. عندما تكون عمليات map و/أو reduce غير حتمية، نوفر دلالات أضعف ولكن لا تزال معقولة. في وجود عمليات غير حتمية، فإن إخراج مهمة reduce معينة R1 يعادل الإخراج لـ R1 الذي ينتج عن تنفيذ تسلسلي للبرنامج غير الحتمي. ومع ذلك، قد يتوافق الإخراج لمهمة reduce مختلفة R2 مع الإخراج لـ R2 الذي ينتج عن تنفيذ تسلسلي مختلف للبرنامج غير الحتمي.

لنتأمل مهمة map M ومهام reduce R1 و R2. لتكن e(Ri) تنفيذ Ri الذي التزم (يوجد بالضبط تنفيذ واحد من هذا القبيل). تنشأ الدلالات الأضعف لأن e(R1) قد يكون قد قرأ الإخراج الذي أنتجه تنفيذ واحد لـ M و e(R2) قد يكون قد قرأ الإخراج الذي أنتجه تنفيذ مختلف لـ M.

### 3.4 المحلية

عرض النطاق الترددي للشبكة هو مورد نادر نسبياً في بيئة الحوسبة لدينا. نحافظ على عرض النطاق الترددي للشبكة من خلال الاستفادة من حقيقة أن بيانات الإدخال (التي يديرها GFS [8]) مخزنة على الأقراص المحلية للأجهزة التي تشكل عنقودنا. يقسم GFS كل ملف إلى كتل بحجم 64 ميجابايت، ويخزن عدة نسخ من كل كتلة (عادة 3 نسخ) على أجهزة مختلفة. يأخذ منسق MapReduce معلومات الموقع لملفات الإدخال في الاعتبار ويحاول جدولة مهمة map على جهاز يحتوي على نسخة متماثلة من بيانات الإدخال المقابلة. في حالة الفشل في ذلك، يحاول جدولة مهمة map بالقرب من نسخة متماثلة من بيانات إدخال تلك المهمة (على سبيل المثال، على جهاز عامل موجود على نفس مفتاح الشبكة مثل الجهاز الذي يحتوي على البيانات). عند تشغيل عمليات MapReduce كبيرة على جزء كبير من العمال في عنقود، يتم قراءة معظم بيانات الإدخال محلياً ولا تستهلك عرض النطاق الترددي للشبكة.

### 3.5 تفصيل المهام

نقسم مرحلة map إلى M قطعة ومرحلة reduce إلى R قطعة، كما هو موضح أعلاه. من الناحية المثالية، يجب أن تكون M و R أكبر بكثير من عدد أجهزة العمال. إن قيام كل عامل بأداء العديد من المهام المختلفة يحسن موازنة الحمل الديناميكي، ويسرع أيضاً الاسترداد عند فشل عامل: يمكن توزيع مهام map العديدة التي أكملها على جميع أجهزة العمال الأخرى.

هناك حدود عملية على مدى كبر M و R في تنفيذنا، حيث يجب على المنسق اتخاذ قرارات جدولة O(M + R) ويحتفظ بحالة O(M × R) في الذاكرة كما هو موضح أعلاه. (عوامل الثابت لاستخدام الذاكرة صغيرة مع ذلك: تتكون قطعة O(M × R) من الحالة من حوالي بايت واحد من البيانات لكل زوج مهمة map/مهمة reduce.)

علاوة على ذلك، غالباً ما يكون R مقيداً من قبل المستخدمين لأن إخراج كل مهمة reduce ينتهي في ملف إخراج منفصل. في الممارسة، نميل إلى اختيار M بحيث تكون كل مهمة فردية حوالي 16 ميجابايت إلى 64 ميجابايت من بيانات الإدخال (بحيث يكون تحسين المحلية الموصوف أعلاه أكثر فعالية)، ونجعل R مضاعفاً صغيراً لعدد أجهزة العمال التي نتوقع استخدامها. غالباً ما نقوم بإجراء حسابات MapReduce مع M = 200,000 و R = 5,000، باستخدام 2,000 جهاز عامل.

### 3.6 المهام الاحتياطية

أحد الأسباب الشائعة التي تطيل إجمالي الوقت المستغرق لعملية MapReduce هو "المتأخر": جهاز يستغرق وقتاً طويلاً بشكل غير عادي لإكمال واحدة من آخر مهام map أو reduce القليلة في الحساب. يمكن أن تنشأ المتأخرات لعدد كبير من الأسباب. على سبيل المثال، قد يواجه جهاز به قرص سيئ أخطاء قابلة للتصحيح متكررة تبطئ أداء القراءة من 30 ميجابايت/ثانية إلى 1 ميجابايت/ثانية. قد يكون نظام جدولة العنقود قد جدول مهام أخرى على الجهاز، مما يتسبب في تنفيذ شفرة MapReduce بشكل أبطأ بسبب المنافسة على وحدة المعالجة المركزية أو الذاكرة أو القرص المحلي أو عرض النطاق الترددي للشبكة. مشكلة حديثة واجهناها كانت خطأ في شفرة تهيئة الجهاز تسبب في تعطيل ذاكرة التخزين المؤقت للمعالج: تباطأت الحسابات على الأجهزة المتأثرة بأكثر من عامل مائة.

لدينا آلية عامة لتخفيف مشكلة المتأخرات. عندما تكون عملية MapReduce قريبة من الاكتمال، يجدول المنسق عمليات تنفيذ احتياطية للمهام المتبقية قيد التنفيذ. يتم وضع علامة على المهمة على أنها مكتملة عندما يكتمل التنفيذ الأساسي أو الاحتياطي. لقد قمنا بضبط هذه الآلية بحيث تزيد عادةً الموارد الحسابية المستخدمة في العملية بما لا يزيد عن بضع بالمائة. وجدنا أن هذا يقلل بشكل كبير من الوقت اللازم لإكمال عمليات MapReduce الكبيرة. كمثال، يستغرق برنامج الفرز الموصوف في القسم 5.3 وقتاً أطول بنسبة 44% للاكتمال عند تعطيل آلية المهمة الاحتياطية.

---

### Translation Notes

- **Figure 1 referenced:** The execution overview diagram showing the flow from User Program → Master → Workers → Map/Reduce phases
- **Key terms maintained in English:** MapReduce, Map, Reduce, map task, reduce task, GFS (Google File System)
- **Technical concepts:**
  - Master/Worker architecture → منسق/عمال
  - Fault tolerance → تحمل الأخطاء
  - Locality optimization → تحسين المحلية
  - Backup tasks → المهام الاحتياطية
  - Straggler → المتأخر
- **Citations:** References [4] and [8] maintained as in original
- **Mathematical notation:** O(M + R), O(M × R) kept in original form

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
