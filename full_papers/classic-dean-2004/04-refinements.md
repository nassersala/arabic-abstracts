# Section 4: Refinements
## القسم 4: التحسينات

**Section:** Refinements
**Translation Quality:** 0.87
**Glossary Terms Used:** partitioning function, hash function, ordering, combiner function, input/output types, side-effects, atomic, deterministic, debugging, counters, distributed system

---

### English Version

## 4 Refinements

Although the basic functionality provided by simply writing Map and Reduce functions is sufficient for most needs, we have found a few extensions useful. These are described in this section.

### 4.1 Partitioning Function

The users of MapReduce specify the number of reduce tasks/output files that they desire (R). Data gets partitioned across these tasks using a partitioning function on the intermediate key. A default partitioning function is provided that uses hashing (e.g. "hash(key) mod R"). This tends to result in fairly well-balanced partitions. In some cases, however, it is useful to partition data by some other function of the key. For example, sometimes the output keys are URLs, and we want all entries for a single host to end up in the same output file. To support situations like this, the user of the MapReduce library can provide a special partitioning function. For example, using "hash(Hostname(urlkey)) mod R" as the partitioning function causes all URLs from the same host to end up in the same output file.

### 4.2 Ordering Guarantees

We guarantee that within a given partition, the intermediate key/value pairs are processed in increasing key order. This ordering guarantee makes it easy to generate a sorted output file per partition, which is useful when the output file format needs to support efficient random access lookups by key, or users of the output find it convenient to have the data sorted.

### 4.3 Combiner Function

In some cases, there is significant repetition in the intermediate keys produced by each map task, and the user-specified Reduce function is commutative and associative. A good example of this is the word counting example in Section 2.1. Since word frequencies tend to follow a Zipf distribution, each map task will produce hundreds or thousands of records of the form <the, 1>. All of these counts will be sent over the network to a single reduce task and then added together by the Reduce function to produce one number. We allow the user to specify an optional Combiner function that does partial merging of this data before it is sent over the network.

The Combiner function is executed on each machine that performs a map task. Typically the same code is used to implement both the combiner and the reduce functions. The only difference between a reduce function and a combiner function is how the MapReduce library handles the output of the function. The output of a reduce function is written to the final output file. The output of a combiner function is written to an intermediate file that will be sent to a reduce task.

Partial combining significantly speeds up certain classes of MapReduce operations. Appendix A contains an example that uses a combiner.

### 4.4 Input and Output Types

The MapReduce library provides support for reading input data in several different formats. For example, "text" mode input treats each line as a key/value pair: the key is the offset in the file and the value is the contents of the line. Another common supported format stores a sequence of key/value pairs sorted by key. Each input type implementation knows how to split itself into meaningful ranges for processing as separate map tasks (e.g. text mode's range splitting ensures that range splits occur only at line boundaries). Users can add support for a new input type by providing an implementation of a simple reader interface, though most users just use one of a small number of predefined input types.

A reader does not necessarily need to provide data read from a file. For example, it is easy to define a reader that reads records from a database, or from data structures mapped in memory.

In a similar fashion, we support a set of output types for producing data in different formats and it is easy for user code to add support for new output types.

### 4.5 Side-effects

In some cases, users of MapReduce have found it convenient to produce auxiliary files as additional outputs from their map and/or reduce operators. We rely on the application writer to make such side-effects atomic and idempotent. Typically the application writes to a temporary file and atomically renames this file once it has been fully generated.

We do not provide support for atomic two-phase commits of multiple output files produced by a single task. Therefore, tasks that produce multiple output files with cross-file consistency requirements should be deterministic. This restriction has never been an issue in practice.

### 4.6 Skipping Bad Records

Sometimes there are bugs in user code that cause the Map or Reduce functions to crash deterministically on certain records. Such bugs prevent a MapReduce operation from completing. The usual course of action is to fix the bug, but sometimes this is not feasible; perhaps the bug is in a third-party library for which source code is unavailable. Also, sometimes it is acceptable to ignore a few records, for example when doing statistical analysis on a large data set. We provide an optional mode of execution where the MapReduce library detects which records cause deterministic crashes and skips these records in order to make forward progress.

Each worker process installs a signal handler that catches segmentation violations and bus errors. Before invoking a user Map or Reduce operation, the MapReduce library stores the sequence number of the argument in a global variable. If the user code generates a signal, the signal handler sends a "last gasp" UDP packet that contains the sequence number to the MapReduce master. When the master has seen more than one failure on a particular record, it indicates that the record should be skipped when it issues the next re-execution of the corresponding Map or Reduce task.

### 4.7 Local Execution

Debugging problems in Map or Reduce functions can be tricky, since the actual computation happens in a distributed system, often on several thousand machines, with work assignment decisions made dynamically by the master. To help facilitate debugging, profiling, and small-scale testing, we have developed an alternative implementation of the MapReduce library that sequentially executes all of the work for a MapReduce operation on the local machine. Controls are provided to the user so that the computation can be limited to particular map tasks. Users invoke their program with a special flag and can then easily use any debugging or testing tools they find useful (e.g. gdb).

### 4.8 Status Information

The master runs an internal HTTP server and exports a set of status pages for human consumption. The status pages show the progress of the computation, such as how many tasks have been completed, how many are in progress, bytes of input, bytes of intermediate data, bytes of output, processing rates, etc. The pages also contain links to the standard error and standard output files generated by each task. The user can use this data to predict how long the computation will take, and whether or not more resources should be added to the computation. These pages can also be used to figure out when the computation is much slower than expected.

In addition, the top-level status page shows which workers have failed, and which map and reduce tasks they were processing when they failed. This information is useful when attempting to diagnose bugs in the user code.

### 4.9 Counters

The MapReduce library provides a counter facility to count occurrences of various events. For example, user code may want to count total number of words processed or the number of German documents indexed, etc.

To use this facility, user code creates a named counter object and then increments the counter appropriately in the Map and/or Reduce function. For example:

```cpp
Counter* uppercase;
uppercase = GetCounter("uppercase");

map(String name, String contents):
  for each word w in contents:
    if (IsCapitalized(w)):
      uppercase->Increment();
    EmitIntermediate(w, "1");
```

The counter values from individual worker machines are periodically propagated to the master (piggybacked on the ping response). The master aggregates the counter values from successful map and reduce tasks and returns them to the user code when the MapReduce operation is completed. The current counter values are also displayed on the master status page so that a human can watch the progress of the live computation. When aggregating counter values, the master eliminates the effects of duplicate executions of the same map or reduce task to avoid double counting. (Duplicate executions can arise from our use of backup tasks and from re-execution of tasks due to failures.)

Some counter values are automatically maintained by the MapReduce library, such as the number of input key/value pairs processed and the number of output key/value pairs produced.

Users have found the counter facility useful for sanity checking the behavior of MapReduce operations. For example, in some MapReduce operations, the user code may want to ensure that the number of output pairs produced exactly equals the number of input pairs processed, or that the fraction of German documents processed is within some tolerable fraction of the total number of documents processed.

---

### النسخة العربية

## 4 التحسينات

على الرغم من أن الوظائف الأساسية التي توفرها كتابة دالتي Map و Reduce ببساطة كافية لمعظم الاحتياجات، فقد وجدنا بعض الامتدادات مفيدة. يتم وصفها في هذا القسم.

### 4.1 دالة التقسيم

يحدد مستخدمو MapReduce عدد مهام reduce/ملفات الإخراج التي يرغبون فيها (R). يتم تقسيم البيانات عبر هذه المهام باستخدام دالة تقسيم على المفتاح الوسيط. يتم توفير دالة تقسيم افتراضية تستخدم التجزئة (على سبيل المثال "hash(key) mod R"). يميل هذا إلى إنتاج تقسيمات متوازنة بشكل جيد. ومع ذلك، في بعض الحالات، من المفيد تقسيم البيانات حسب دالة أخرى للمفتاح. على سبيل المثال، في بعض الأحيان تكون مفاتيح الإخراج عبارة عن عناوين URL، ونريد أن تنتهي جميع الإدخالات لمضيف واحد في نفس ملف الإخراج. لدعم مواقف مثل هذا، يمكن لمستخدم مكتبة MapReduce توفير دالة تقسيم خاصة. على سبيل المثال، استخدام "hash(Hostname(urlkey)) mod R" كدالة تقسيم يتسبب في انتهاء جميع عناوين URL من نفس المضيف في نفس ملف الإخراج.

### 4.2 ضمانات الترتيب

نضمن أنه ضمن تقسيم معين، تتم معالجة أزواج المفتاح/القيمة الوسيطة بترتيب مفاتيح متزايد. يجعل ضمان الترتيب هذا من السهل إنشاء ملف إخراج مرتب لكل تقسيم، وهو أمر مفيد عندما يحتاج تنسيق ملف الإخراج إلى دعم عمليات بحث الوصول العشوائي الفعالة حسب المفتاح، أو يجد مستخدمو الإخراج أنه من المناسب ترتيب البيانات.

### 4.3 دالة الدمج

في بعض الحالات، هناك تكرار كبير في المفاتيح الوسيطة التي تنتجها كل مهمة map، ودالة Reduce المحددة من قبل المستخدم تبادلية وتجميعية. مثال جيد على ذلك هو مثال عد الكلمات في القسم 2.1. نظراً لأن ترددات الكلمات تميل إلى اتباع توزيع Zipf، فإن كل مهمة map ستنتج مئات أو آلاف من السجلات بالشكل <the, 1>. سيتم إرسال جميع هذه العدادات عبر الشبكة إلى مهمة reduce واحدة ثم يتم جمعها معاً بواسطة دالة Reduce لإنتاج رقم واحد. نسمح للمستخدم بتحديد دالة دمج اختيارية تقوم بدمج جزئي لهذه البيانات قبل إرسالها عبر الشبكة.

يتم تنفيذ دالة الدمج على كل جهاز يؤدي مهمة map. عادة ما يتم استخدام نفس الشفرة لتنفيذ كل من دالتي الدمج و reduce. الفرق الوحيد بين دالة reduce ودالة الدمج هو كيفية تعامل مكتبة MapReduce مع إخراج الدالة. يتم كتابة إخراج دالة reduce إلى ملف الإخراج النهائي. يتم كتابة إخراج دالة الدمج إلى ملف وسيط سيتم إرساله إلى مهمة reduce.

يؤدي الدمج الجزئي إلى تسريع فئات معينة من عمليات MapReduce بشكل كبير. يحتوي الملحق A على مثال يستخدم دالة دمج.

### 4.4 أنواع الإدخال والإخراج

توفر مكتبة MapReduce دعماً لقراءة بيانات الإدخال بعدة تنسيقات مختلفة. على سبيل المثال، يعامل إدخال وضع "النص" كل سطر كزوج مفتاح/قيمة: المفتاح هو الإزاحة في الملف والقيمة هي محتويات السطر. تنسيق آخر مدعوم شائع يخزن سلسلة من أزواج المفتاح/القيمة مرتبة حسب المفتاح. يعرف كل تنفيذ لنوع إدخال كيفية تقسيم نفسه إلى نطاقات ذات معنى للمعالجة كمهام map منفصلة (على سبيل المثال، يضمن تقسيم النطاق في وضع النص أن تقسيمات النطاق تحدث فقط عند حدود الأسطر). يمكن للمستخدمين إضافة دعم لنوع إدخال جديد من خلال توفير تنفيذ لواجهة قارئ بسيطة، على الرغم من أن معظم المستخدمين يستخدمون فقط واحداً من عدد صغير من أنواع الإدخال المحددة مسبقاً.

لا يحتاج القارئ بالضرورة إلى توفير بيانات مقروءة من ملف. على سبيل المثال، من السهل تحديد قارئ يقرأ السجلات من قاعدة بيانات، أو من بنى البيانات المعينة في الذاكرة.

بطريقة مماثلة، ندعم مجموعة من أنواع الإخراج لإنتاج بيانات بتنسيقات مختلفة ومن السهل على شفرة المستخدم إضافة دعم لأنواع إخراج جديدة.

### 4.5 الآثار الجانبية

في بعض الحالات، وجد مستخدمو MapReduce أنه من المناسب إنتاج ملفات مساعدة كإخراجات إضافية من عمليات map و/أو reduce الخاصة بهم. نعتمد على كاتب التطبيق لجعل هذه الآثار الجانبية ذرية وخالية من التكرار. عادة ما يكتب التطبيق إلى ملف مؤقت ويعيد تسمية هذا الملف ذرياً بمجرد إنشائه بالكامل.

لا نقدم دعماً للالتزامات الذرية ذات الطورين لملفات إخراج متعددة تنتجها مهمة واحدة. لذلك، يجب أن تكون المهام التي تنتج ملفات إخراج متعددة مع متطلبات اتساق عبر الملفات حتمية. لم يكن هذا القيد مشكلة أبداً في الممارسة العملية.

### 4.6 تخطي السجلات السيئة

في بعض الأحيان توجد أخطاء في شفرة المستخدم تتسبب في تعطل دالتي Map أو Reduce بشكل حتمي على سجلات معينة. مثل هذه الأخطاء تمنع عملية MapReduce من الاكتمال. مسار الإجراء المعتاد هو إصلاح الخطأ، ولكن في بعض الأحيان لا يكون هذا ممكناً؛ ربما يكون الخطأ في مكتبة طرف ثالث لا تتوفر لها شفرة المصدر. أيضاً، في بعض الأحيان يكون من المقبول تجاهل بضعة سجلات، على سبيل المثال عند إجراء تحليل إحصائي على مجموعة بيانات كبيرة. نوفر وضع تنفيذ اختياري حيث تكتشف مكتبة MapReduce السجلات التي تتسبب في أعطال حتمية وتتخطى هذه السجلات من أجل إحراز تقدم.

تثبت كل عملية عامل معالج إشارة يلتقط انتهاكات التجزئة وأخطاء الناقل. قبل استدعاء عملية Map أو Reduce للمستخدم، تخزن مكتبة MapReduce رقم التسلسل للوسيط في متغير عام. إذا أنشأت شفرة المستخدم إشارة، فإن معالج الإشارة يرسل حزمة UDP "آخر نفس" تحتوي على رقم التسلسل إلى منسق MapReduce. عندما يرى المنسق أكثر من فشل واحد على سجل معين، فإنه يشير إلى أنه يجب تخطي السجل عندما يصدر إعادة التنفيذ التالية لمهمة Map أو Reduce المقابلة.

### 4.7 التنفيذ المحلي

يمكن أن يكون تصحيح المشاكل في دالتي Map أو Reduce صعباً، حيث يحدث الحساب الفعلي في نظام موزع، غالباً على عدة آلاف من الأجهزة، مع اتخاذ قرارات تعيين العمل ديناميكياً بواسطة المنسق. للمساعدة في تسهيل تصحيح الأخطاء والتحليل والاختبار على نطاق صغير، قمنا بتطوير تنفيذ بديل لمكتبة MapReduce ينفذ تسلسلياً جميع الأعمال لعملية MapReduce على الجهاز المحلي. يتم توفير عناصر تحكم للمستخدم بحيث يمكن تقييد الحساب لمهام map معينة. يستدعي المستخدمون برنامجهم بعلامة خاصة ويمكنهم بعد ذلك استخدام أي أدوات تصحيح أو اختبار يجدونها مفيدة بسهولة (على سبيل المثال gdb).

### 4.8 معلومات الحالة

يشغل المنسق خادم HTTP داخلي ويصدر مجموعة من صفحات الحالة للاستهلاك البشري. تُظهر صفحات الحالة تقدم الحساب، مثل عدد المهام التي تم إكمالها، وعدد المهام قيد التنفيذ، وبايتات الإدخال، وبايتات البيانات الوسيطة، وبايتات الإخراج، ومعدلات المعالجة، وما إلى ذلك. تحتوي الصفحات أيضاً على روابط لملفات الخطأ القياسي والإخراج القياسي التي تم إنشاؤها بواسطة كل مهمة. يمكن للمستخدم استخدام هذه البيانات للتنبؤ بالمدة التي سيستغرقها الحساب، وما إذا كان يجب إضافة المزيد من الموارد إلى الحساب أم لا. يمكن أيضاً استخدام هذه الصفحات لمعرفة متى يكون الحساب أبطأ بكثير من المتوقع.

بالإضافة إلى ذلك، تُظهر صفحة الحالة ذات المستوى الأعلى العمال الذين فشلوا، ومهام map و reduce التي كانوا يعالجونها عندما فشلوا. هذه المعلومات مفيدة عند محاولة تشخيص الأخطاء في شفرة المستخدم.

### 4.9 العدادات

توفر مكتبة MapReduce ميزة عداد لعد حدوث أحداث مختلفة. على سبيل المثال، قد ترغب شفرة المستخدم في عد إجمالي عدد الكلمات المعالجة أو عدد المستندات الألمانية المفهرسة، وما إلى ذلك.

لاستخدام هذه الميزة، تنشئ شفرة المستخدم كائن عداد مسمى ثم تزيد العداد بشكل مناسب في دالة Map و/أو Reduce. على سبيل المثال:

```cpp
Counter* uppercase;
uppercase = GetCounter("uppercase");

map(String name, String contents):
  for each word w in contents:
    if (IsCapitalized(w)):
      uppercase->Increment();
    EmitIntermediate(w, "1");
```

يتم نشر قيم العداد من أجهزة العمال الفردية بشكل دوري إلى المنسق (محمولة على استجابة الفحص). يجمع المنسق قيم العداد من مهام map و reduce الناجحة ويعيدها إلى شفرة المستخدم عند اكتمال عملية MapReduce. يتم أيضاً عرض قيم العداد الحالية على صفحة حالة المنسق بحيث يمكن للإنسان مشاهدة تقدم الحساب المباشر. عند تجميع قيم العداد، يزيل المنسق آثار التنفيذات المكررة لنفس مهمة map أو reduce لتجنب العد المزدوج. (يمكن أن تنشأ التنفيذات المكررة من استخدامنا للمهام الاحتياطية ومن إعادة تنفيذ المهام بسبب الأعطال.)

يتم صيانة بعض قيم العداد تلقائياً بواسطة مكتبة MapReduce، مثل عدد أزواج المفتاح/القيمة المعالجة للإدخال وعدد أزواج المفتاح/القيمة المنتجة للإخراج.

وجد المستخدمون أن ميزة العداد مفيدة للتحقق من سلامة سلوك عمليات MapReduce. على سبيل المثال، في بعض عمليات MapReduce، قد ترغب شفرة المستخدم في التأكد من أن عدد أزواج الإخراج المنتجة يساوي بالضبط عدد أزواج الإدخال المعالجة، أو أن جزء المستندات الألمانية المعالجة يقع ضمن بعض الجزء المسموح به من إجمالي عدد المستندات المعالجة.

---

### Translation Notes

- **Key refinements covered:**
  1. Partitioning Function (دالة التقسيم)
  2. Ordering Guarantees (ضمانات الترتيب)
  3. Combiner Function (دالة الدمج)
  4. Input/Output Types (أنواع الإدخال/الإخراج)
  5. Side-effects (الآثار الجانبية)
  6. Skipping Bad Records (تخطي السجلات السيئة)
  7. Local Execution (التنفيذ المحلي)
  8. Status Information (معلومات الحالة)
  9. Counters (العدادات)

- **Technical terms:**
  - Partitioning function → دالة التقسيم
  - Hash function → دالة التجزئة
  - Combiner → دالة الدمج
  - Zipf distribution → توزيع Zipf
  - Commutative and associative → تبادلية وتجميعية
  - Atomic and idempotent → ذرية وخالية من التكرار
  - Signal handler → معالج الإشارة
  - Segmentation violations → انتهاكات التجزئة

- **Code examples:** C++ code maintained in original form with translated comments

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
