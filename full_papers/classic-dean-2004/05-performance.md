# Section 5: Performance
## القسم 5: الأداء

**Section:** Performance
**Translation Quality:** 0.86
**Glossary Terms Used:** cluster, benchmark, grep, sort, throughput, input rate, shuffle rate, output rate, backup tasks, machine failures, locality optimization, network bandwidth, terabyte

---

### English Version

## 5 Performance

In this section we measure the performance of MapReduce on two computations running on a large cluster of machines. One computation searches through approximately one terabyte of data looking for a particular pattern. The other computation sorts approximately one terabyte of data.

These two programs are representative of a large subset of the real programs written by users of MapReduce – one class of programs shuffles data from one representation to another, and another class extracts a small amount of interesting data from a large data set.

### 5.1 Cluster Configuration

All of the programs were executed on a cluster that consisted of approximately 1800 machines. Each machine had two 2GHz Intel Xeon processors with Hyper-Threading enabled, 4GB of memory, two 160GB IDE disks, and a gigabit Ethernet link. The machines were arranged in a two-level tree-shaped switched network with approximately 100-200 Gbps of aggregate bandwidth available at the root. All of the machines were in the same hosting facility and therefore the round-trip time between any pair of machines was less than a millisecond.

Out of the 4GB of memory, approximately 1-1.5GB was reserved by other tasks running on the cluster. The programs were executed on a weekend afternoon, when the CPUs, disks, and network were mostly idle.

### 5.2 Grep

The grep program scans through 10^10 100-byte records, searching for a relatively rare three-character pattern (the pattern occurs in 92,337 records). The input is split into approximately 64MB pieces (M = 15000), and the entire output is placed in one file (R = 1).

Figure 2 shows the progress of the computation over time. The Y-axis shows the rate at which the input data is scanned. The rate gradually picks up as more machines are assigned to this MapReduce computation, and peaks at over 30 GB/s when 1764 workers have been assigned. As the map tasks finish, the rate starts dropping and hits zero about 80 seconds into the computation. The entire computation takes approximately 150 seconds from start to finish. This includes about a minute of startup overhead. The overhead is due to the propagation of the program to all worker machines, and delays interacting with GFS to open the set of 1000 input files and to get the information needed for the locality optimization.

### 5.3 Sort

The sort program sorts 10^10 100-byte records (approximately 1 terabyte of data). This program is modeled after the TeraSort benchmark [10].

The sorting program consists of less than 50 lines of user code. A three-line Map function extracts a 10-byte sorting key from a text line and emits the key and the original text line as the intermediate key/value pair. We used a built-in Identity function as the Reduce operator. This functions passes the intermediate key/value pair unchanged as the output key/value pair. The final sorted output is written to a set of 2-way replicated GFS files (i.e., 2 terabytes are written as the output of the program).

As before, the input data is split into 64MB pieces (M = 15000). We partition the sorted output into 4000 files (R = 4000). The partitioning function uses the initial bytes of the key to segregate it into one of R pieces.

Our partitioning function for this benchmark has built-in knowledge of the distribution of keys. In a general sorting program, we would add a pre-pass MapReduce operation that would collect a sample of the keys and use the distribution of the sampled keys to compute split-points for the final sorting pass.

Figure 3 (a) shows the progress of a normal execution of the sort program. The top-left graph shows the rate at which input is read. The rate peaks at about 13 GB/s and dies off fairly quickly since all map tasks finish before 200 seconds have elapsed. Note that the input rate is less than for grep. This is because the sort map tasks spend about half their time and I/O bandwidth writing intermediate output to their local disks. The corresponding intermediate output for grep had negligible size.

The middle-left graph shows the rate at which data is sent over the network from the map tasks to the reduce tasks. This shuffling starts as soon as the first map task completes. The first hump in the graph is for the first batch of approximately 1700 reduce tasks (the entire MapReduce was assigned about 1700 machines, and each machine executes at most one reduce task at a time). Roughly 300 seconds into the computation, some of these first batch of reduce tasks finish and we start shuffling data for the remaining reduce tasks. All of the shuffling is done about 600 seconds into the computation.

The bottom-left graph shows the rate at which sorted data is written to the final output files by the reduce tasks. There is a delay between the end of the first shuffling period and the start of the writing period because the machines are busy sorting the intermediate data. The writes continue at a rate of about 2-4 GB/s for a while. All of the writes finish about 850 seconds into the computation. Including startup overhead, the entire computation takes 891 seconds. This is similar to the current best reported result of 1057 seconds for the TeraSort benchmark [18].

A few things to note: the input rate is higher than the shuffle rate and the output rate because of our locality optimization – most data is read from a local disk and bypasses our relatively bandwidth constrained network. The shuffle rate is higher than the output rate because the output phase writes two copies of the sorted data (we make two replicas of the output for reliability and availability reasons). We write two replicas because that is the mechanism for reliability and availability provided by our underlying file system. Network bandwidth requirements for writing data would be reduced if the underlying file system used erasure coding [14] rather than replication.

### 5.4 Effect of Backup Tasks

In Figure 3 (b), we show an execution of the sort program with backup tasks disabled. The execution flow is similar to that shown in Figure 3 (a), except that there is a very long tail where hardly any write activity occurs. After 960 seconds, all except 5 of the reduce tasks are completed. However these last few stragglers don't finish until 300 seconds later. The entire computation takes 1283 seconds, an increase of 44% in elapsed time.

### 5.5 Machine Failures

In Figure 3 (c), we show an execution of the sort program where we intentionally killed 200 out of 1746 worker processes several minutes into the computation. The underlying cluster scheduler immediately restarted new worker processes on these machines (since only the processes were killed, the machines were still functioning properly).

The worker deaths show up as a negative input rate since some previously completed map work disappears (since the corresponding map workers were killed) and needs to be redone. The re-execution of this map work happens relatively quickly. The entire computation finishes in 933 seconds including startup overhead (just an increase of 5% over the normal execution time).

---

### النسخة العربية

## 5 الأداء

في هذا القسم نقيس أداء MapReduce على حسابين يعملان على عنقود كبير من الأجهزة. يبحث أحد الحسابات في حوالي تيرابايت واحد من البيانات بحثاً عن نمط معين. يقوم الحساب الآخر بفرز حوالي تيرابايت واحد من البيانات.

هذان البرنامجان ممثلان لمجموعة فرعية كبيرة من البرامج الحقيقية المكتوبة من قبل مستخدمي MapReduce - فئة واحدة من البرامج تخلط البيانات من تمثيل إلى آخر، وفئة أخرى تستخرج كمية صغيرة من البيانات المثيرة للاهتمام من مجموعة بيانات كبيرة.

### 5.1 تكوين العنقود

تم تنفيذ جميع البرامج على عنقود يتكون من حوالي 1800 جهاز. كان كل جهاز يحتوي على معالجين Intel Xeon بسرعة 2 جيجاهرتز مع تمكين Hyper-Threading، و 4 جيجابايت من الذاكرة، وقرصين IDE بسعة 160 جيجابايت، ورابط Ethernet بسرعة جيجابت. تم ترتيب الأجهزة في شبكة مبدلة على شكل شجرة ذات مستويين مع حوالي 100-200 جيجابت في الثانية من عرض النطاق الترددي الإجمالي المتاح عند الجذر. كانت جميع الأجهزة في نفس منشأة الاستضافة وبالتالي كان وقت الرحلة ذهاباً وإياباً بين أي زوج من الأجهزة أقل من ميلي ثانية.

من أصل 4 جيجابايت من الذاكرة، تم حجز حوالي 1-1.5 جيجابايت بواسطة مهام أخرى تعمل على العنقود. تم تنفيذ البرامج في فترة ما بعد ظهر نهاية الأسبوع، عندما كانت وحدات المعالجة المركزية والأقراص والشبكة خاملة في الغالب.

### 5.2 Grep

يفحص برنامج grep من خلال 10^10 سجل بحجم 100 بايت، بحثاً عن نمط نادر نسبياً من ثلاثة أحرف (يحدث النمط في 92,337 سجلاً). يتم تقسيم الإدخال إلى قطع بحجم حوالي 64 ميجابايت (M = 15000)، ويتم وضع الإخراج بأكمله في ملف واحد (R = 1).

يوضح الشكل 2 تقدم الحساب مع مرور الوقت. يُظهر المحور Y المعدل الذي يتم به فحص بيانات الإدخال. يتزايد المعدل تدريجياً مع تعيين المزيد من الأجهزة لحساب MapReduce هذا، ويبلغ ذروته عند أكثر من 30 جيجابايت/ثانية عندما يتم تعيين 1764 عاملاً. عندما تنتهي مهام map، يبدأ المعدل في الانخفاض ويصل إلى الصفر بعد حوالي 80 ثانية من بداية الحساب. يستغرق الحساب بأكمله حوالي 150 ثانية من البداية إلى النهاية. يتضمن ذلك حوالي دقيقة من النفقات العامة للبدء. تعود النفقات العامة إلى نشر البرنامج إلى جميع أجهزة العمال، والتأخيرات في التفاعل مع GFS لفتح مجموعة من 1000 ملف إدخال والحصول على المعلومات اللازمة لتحسين المحلية.

### 5.3 الفرز

يقوم برنامج الفرز بفرز 10^10 سجل بحجم 100 بايت (حوالي 1 تيرابايت من البيانات). هذا البرنامج مصمم على غرار معيار TeraSort [10].

يتكون برنامج الفرز من أقل من 50 سطراً من شفرة المستخدم. تستخرج دالة Map المكونة من ثلاثة أسطر مفتاح فرز بحجم 10 بايتات من سطر نصي وتصدر المفتاح وسطر النص الأصلي كزوج المفتاح/القيمة الوسيط. استخدمنا دالة Identity المضمنة كعامل Reduce. تمرر هذه الدالة زوج المفتاح/القيمة الوسيط دون تغيير كزوج المفتاح/القيمة للإخراج. يُكتب الإخراج المرتب النهائي إلى مجموعة من ملفات GFS المنسوخة بشكل ثنائي (أي، يتم كتابة 2 تيرابايت كإخراج للبرنامج).

كما هو الحال من قبل، يتم تقسيم بيانات الإدخال إلى قطع بحجم 64 ميجابايت (M = 15000). نقسم الإخراج المرتب إلى 4000 ملف (R = 4000). تستخدم دالة التقسيم البايتات الأولية للمفتاح لفصله إلى واحدة من قطع R.

لدى دالة التقسيم الخاصة بنا لهذا المعيار معرفة مدمجة بتوزيع المفاتيح. في برنامج فرز عام، سنضيف عملية MapReduce تمهيدية من شأنها أن تجمع عينة من المفاتيح وتستخدم توزيع المفاتيح المعاينة لحساب نقاط التقسيم للممر النهائي للفرز.

يُظهر الشكل 3 (a) تقدم التنفيذ العادي لبرنامج الفرز. يُظهر الرسم البياني في الأعلى اليسار المعدل الذي يتم به قراءة الإدخال. يبلغ المعدل ذروته عند حوالي 13 جيجابايت/ثانية وينخفض بسرعة إلى حد ما حيث تنتهي جميع مهام map قبل مرور 200 ثانية. لاحظ أن معدل الإدخال أقل منه لـ grep. هذا لأن مهام map للفرز تقضي حوالي نصف وقتها وعرض النطاق الترددي للإدخال/الإخراج في كتابة الإخراج الوسيط إلى أقراصها المحلية. كان الإخراج الوسيط المقابل لـ grep ذا حجم ضئيل.

يُظهر الرسم البياني الأوسط الأيسر المعدل الذي يتم به إرسال البيانات عبر الشبكة من مهام map إلى مهام reduce. يبدأ هذا الخلط بمجرد اكتمال أول مهمة map. الحدبة الأولى في الرسم البياني هي للدفعة الأولى من حوالي 1700 مهمة reduce (تم تعيين MapReduce بأكملها حوالي 1700 جهاز، وينفذ كل جهاز مهمة reduce واحدة على الأكثر في كل مرة). بعد حوالي 300 ثانية من بداية الحساب، تنتهي بعض هذه الدفعة الأولى من مهام reduce ونبدأ في خلط البيانات لمهام reduce المتبقية. يتم الانتهاء من جميع عمليات الخلط بعد حوالي 600 ثانية من بداية الحساب.

يُظهر الرسم البياني السفلي الأيسر المعدل الذي يتم به كتابة البيانات المرتبة إلى ملفات الإخراج النهائية بواسطة مهام reduce. هناك تأخير بين نهاية فترة الخلط الأولى وبداية فترة الكتابة لأن الأجهزة مشغولة بفرز البيانات الوسيطة. تستمر عمليات الكتابة بمعدل حوالي 2-4 جيجابايت/ثانية لفترة من الوقت. تنتهي جميع عمليات الكتابة بعد حوالي 850 ثانية من بداية الحساب. بما في ذلك النفقات العامة للبدء، يستغرق الحساب بأكمله 891 ثانية. هذا مشابه لأفضل نتيجة مبلغ عنها حالياً وهي 1057 ثانية لمعيار TeraSort [18].

بعض الأشياء التي يجب ملاحظتها: معدل الإدخال أعلى من معدل الخلط ومعدل الإخراج بسبب تحسين المحلية لدينا - يتم قراءة معظم البيانات من قرص محلي وتتجاوز شبكتنا ذات عرض النطاق الترددي المقيد نسبياً. معدل الخلط أعلى من معدل الإخراج لأن مرحلة الإخراج تكتب نسختين من البيانات المرتبة (نصنع نسختين متماثلتين من الإخراج لأسباب الموثوقية والتوافر). نكتب نسختين لأن هذه هي الآلية للموثوقية والتوافر التي يوفرها نظام الملفات الأساسي لدينا. ستنخفض متطلبات عرض النطاق الترددي للشبكة لكتابة البيانات إذا كان نظام الملفات الأساسي يستخدم ترميز المحو [14] بدلاً من النسخ المتماثل.

### 5.4 تأثير المهام الاحتياطية

في الشكل 3 (b)، نُظهر تنفيذاً لبرنامج الفرز مع تعطيل المهام الاحتياطية. تدفق التنفيذ مشابه لما هو موضح في الشكل 3 (a)، باستثناء أن هناك ذيلاً طويلاً جداً حيث بالكاد يحدث أي نشاط كتابة. بعد 960 ثانية، تم إكمال جميع مهام reduce باستثناء 5. ومع ذلك، لا تنتهي هذه المتأخرات القليلة الأخيرة حتى 300 ثانية في وقت لاحق. يستغرق الحساب بأكمله 1283 ثانية، بزيادة قدرها 44% في الوقت المنقضي.

### 5.5 أعطال الأجهزة

في الشكل 3 (c)، نُظهر تنفيذاً لبرنامج الفرز حيث قتلنا عمداً 200 من أصل 1746 عملية عامل بعد عدة دقائق من بداية الحساب. أعاد مجدول العنقود الأساسي على الفور بدء عمليات عامل جديدة على هذه الأجهزة (نظراً لأنه تم قتل العمليات فقط، كانت الأجهزة لا تزال تعمل بشكل صحيح).

تظهر وفيات العمال كمعدل إدخال سلبي حيث يختفي بعض عمل map المكتمل سابقاً (نظراً لأن عمال map المقابلين تم قتلهم) ويحتاج إلى إعادة إجراء. تحدث إعادة تنفيذ عمل map هذا بسرعة نسبية. ينتهي الحساب بأكمله في 933 ثانية بما في ذلك النفقات العامة للبدء (مجرد زيادة بنسبة 5% عن وقت التنفيذ العادي).

---

### Translation Notes

- **Figures referenced:**
  - Figure 2: Data transfer rate over time (grep benchmark)
  - Figure 3: Data transfer rates for sort program
    - (a) Normal execution
    - (b) No backup tasks
    - (c) 200 tasks killed

- **Benchmark details:**
  - Grep: 10 billion records (10^10), 100-byte each, searching for 3-character pattern
  - Sort: 10 billion records, ~1 TB total data, modeled after TeraSort benchmark

- **Performance metrics:**
  - Cluster: ~1800 machines, dual 2GHz Xeon, 4GB RAM, 160GB disks
  - Grep: 150 seconds total, 30 GB/s peak input rate
  - Sort: 891 seconds normal, 1283 seconds without backup tasks (+44%)
  - With 200 failures: 933 seconds (+5%)

- **Key terms:**
  - Throughput → معدل الإنتاجية
  - Input rate → معدل الإدخال
  - Shuffle rate → معدل الخلط
  - Output rate → معدل الإخراج
  - Straggler → المتأخر
  - Backup tasks → المهام الاحتياطية
  - Locality optimization → تحسين المحلية

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
