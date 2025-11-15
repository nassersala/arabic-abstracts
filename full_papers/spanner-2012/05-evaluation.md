# Section 5: Evaluation
## القسم 5: التقييم

**Section:** evaluation
**Translation Quality:** 0.87
**Glossary Terms Used:** throughput (الإنتاجية), latency (زمن الانتقال), availability (التوافر), replication (النسخ المتماثل), benchmark (معيار مرجعي), snapshot read (قراءة لقطة), read-only transaction (معاملة قراءة فقط), two-phase commit (التنفيذ ثنائي المرحلة)

---

### English Version

We first measure Spanner's performance with respect to replication, transactions, and availability. We then provide some data on TrueTime behavior, and a case study of our first client, F1.

**5.1 Microbenchmarks**

Table 3 presents some microbenchmarks for Spanner. These measurements were taken on timeshared machines: each spanserver ran on scheduling units of 4GB RAM and 4 cores (AMD Barcelona 2200MHz). Clients were run on separate machines. Each zone contained one spanserver. Clients and zones were placed in a set of datacenters with network distance of less than 1ms. (Such a layout should be commonplace: most applications do not need to distribute all of their data worldwide.) The test database was created with 50 Paxos groups with 2500 directories. Operations were standalone reads and writes of 4KB. All reads were served out of memory after a compaction, so that we are only measuring the overhead of Spanner's call stack. In addition, one unmeasured round of reads was done first to warm any location caches.

For the latency experiments, clients issued sufficiently few operations so as to avoid queuing at the servers. From the 1-replica experiments, commit wait is about 5ms, and Paxos latency is about 9ms. As the number of replicas increases, the latency stays roughly constant with less standard deviation because Paxos executes in parallel at a group's replicas. As the number of replicas increases, the latency to achieve a quorum becomes less sensitive to slowness at one slave replica.

For the throughput experiments, clients issued sufficiently many operations so as to saturate the servers' CPUs. Snapshot reads can execute at any up-to-date replicas, so their throughput increases almost linearly with the number of replicas. Single-read read-only transactions only execute at leaders because timestamp assignment must happen at leaders. Read-only-transaction throughput increases with the number of replicas because the number of effective spanservers increases: in the experimental setup, the number of spanservers equaled the number of replicas, and leaders were randomly distributed among the zones. Write throughput benefits from the same experimental artifact (which explains the increase in throughput from 3 to 5 replicas), but that benefit is outweighed by the linear increase in the amount of work performed per write, as the number of replicas increases.

Table 4 demonstrates that two-phase commit can scale to a reasonable number of participants: it summarizes a set of experiments run across 3 zones, each with 25 spanservers. Scaling up to 50 participants is reasonable in both mean and 99th-percentile, and latencies start to rise noticeably at 100 participants.

**Table 4: Two-phase commit scalability**

| Participants | Mean (ms) | 99th Percentile (ms) |
|--------------|-----------|----------------------|
| 1 | 17.0±1.4 | 75.0±34.9 |
| 2 | 24.5±2.5 | 87.6±35.9 |
| 5 | 31.5±6.2 | 104.5±52.2 |
| 10 | 30.0±3.7 | 95.6±25.4 |
| 25 | 35.5±5.6 | 100.4±42.7 |
| 50 | 42.7±4.1 | 93.7±22.9 |
| 100 | 71.4±7.6 | 131.2±17.6 |
| 200 | 150.5±11.0 | 320.3±35.1 |

**5.2 Availability**

Figure 5 illustrates the availability benefits of running Spanner in multiple datacenters. It shows the results of three experiments on throughput in the presence of datacenter failure, all of which are overlaid onto the same time scale. The test universe consisted of 5 zones Zᵢ, each of which had 25 spanservers. The test database was sharded into 1250 Paxos groups, and 100 test clients constantly issued non-snapshot reads at an aggregate rate of 50K reads/second. All of the leaders were explicitly placed in Z₁. Five seconds into each test, all of the servers in one zone were killed: non-leader kills Z₂; leader-hard kills Z₁; leader-soft kills Z₁, but it gives notifications to all of the servers that they should handoff leadership first.

Killing Z₂ has no effect on read throughput. Killing Z₁ while giving the leaders time to handoff leadership to a different zone has a minor effect: the throughput drop is not visible in the graph, but is around 3-4%. On the other hand, killing Z₁ with no warning has a severe effect: the rate of completion drops almost to 0. As leaders get re-elected, though, the throughput of the system rises to approximately 100K reads/second because of two artifacts of our experiment: there is extra capacity in the system, and operations are queued while the leader is unavailable. As a result, the throughput of the system rises before leveling off again at its steady-state rate.

We can also see the effect of the fact that Paxos leader leases are set to 10 seconds. When we kill the zone, the leader-lease expiration times for the groups should be evenly distributed over the next 10 seconds. Soon after each lease from a dead leader expires, a new leader is elected. Approximately 10 seconds after the kill time, all of the groups have leaders and throughput has recovered. Shorter lease times would reduce the effect of server deaths on availability, but would require greater amounts of lease-renewal network traffic. We are in the process of designing and implementing a mechanism that will cause slaves to release Paxos leader leases upon leader failure.

**5.3 TrueTime**

Two questions must be answered with respect to TrueTime: is ε truly a bound on clock uncertainty, and how bad does ε get? For the former, the most serious problem would be if a local clock's drift were greater than 200us/sec: that would break assumptions made by TrueTime. Our machine statistics show that bad CPUs are 6 times more likely than bad clocks. That is, clock issues are extremely infrequent, relative to much more serious hardware problems. As a result, we believe that TrueTime's implementation is as trustworthy as any other piece of software upon which Spanner depends.

Figure 6 presents TrueTime data taken at several thousand spanserver machines across datacenters up to 2200 km apart. It plots the 90th, 99th, and 99.9th percentiles of ε, sampled at timeslave daemons immediately after polling the time masters. This sampling elides the sawtooth in ε due to local-clock uncertainty, and therefore measures time-master uncertainty (which is generally 0) plus communication delay to the time masters.

The data shows that these two factors in determining the base value of ε are generally not a problem. However, there can be significant tail-latency issues that cause higher values of ε. The reduction in tail latencies beginning on March 30 were due to networking improvements that reduced transient network-link congestion. The increase in ε on April 13, approximately one hour in duration, resulted from the shutdown of 2 time masters at a datacenter for routine maintenance. We continue to investigate and remove causes of TrueTime spikes.

**5.4 F1**

Spanner started being experimentally evaluated under production workloads in early 2011, as part of a rewrite of Google's advertising backend called F1 [35]. This backend was originally based on a MySQL database that was manually sharded many ways. The uncompressed dataset is tens of terabytes, which is small compared to many NoSQL instances, but was large enough to cause difficulties with sharded MySQL. The MySQL sharding scheme assigned each customer and all related data to a fixed shard. This layout enabled the use of indexes and complex query processing on a per-customer basis, but required some knowledge of the sharding in application business logic. Resharding this revenue-critical database as it grew in the number of customers and their data was extremely costly. The last resharding took over two years of intense effort, and involved coordination and testing across dozens of teams to minimize risk. This operation was too complex to do regularly: as a result, the team had to limit growth on the MySQL database by storing some data in external Bigtables, which compromised transactional behavior and the ability to query across all data.

The F1 team chose to use Spanner for several reasons. First, Spanner removes the need to manually reshard. Second, Spanner provides synchronous replication and automatic failover. With MySQL master-slave replication, failover was difficult, and risked data loss and downtime. Third, F1 requires strong transactional semantics, which made using other NoSQL systems impractical. Application semantics requires transactions across arbitrary data, and consistent reads. The F1 team also needed secondary indexes on their data (since Spanner does not yet provide automatic support for secondary indexes), and was able to implement their own consistent global indexes using Spanner transactions.

All application writes are now by default sent through F1 to Spanner, instead of the MySQL-based application stack. F1 has 2 replicas on the west coast of the US, and 3 on the east coast. This choice of replica sites was made to cope with outages due to potential major natural disasters, and also the choice of their frontend sites. Anecdotally, Spanner's automatic failover has been nearly invisible to them. Although there have been unplanned cluster failures in the last few months, the most that the F1 team has had to do is update their database's schema to tell Spanner where to preferentially place Paxos leaders, so as to keep them close to where their frontends moved.

Spanner's timestamp semantics made it efficient for F1 to maintain in-memory data structures computed from the database state. F1 maintains a logical history log of all changes, which is written into Spanner itself as part of every transaction. F1 takes full snapshots of data at a timestamp to initialize its data structures, and then reads incremental changes to update them.

Table 5 illustrates the distribution of the number of fragments per directory in F1. Each directory typically corresponds to a customer in the application stack above F1. The vast majority of directories (and therefore customers) consist of only 1 fragment, which means that reads and writes to those customers' data are guaranteed to occur on only a single server. The directories with more than 100 fragments are all tables that contain F1 secondary indexes: writes to more than a few fragments of such tables are extremely uncommon. The F1 team has only seen such behavior when they do untuned bulk data loads as transactions.

**Table 5: Distribution of directory-fragment counts in F1**

| # fragments | # directories |
|-------------|---------------|
| 1 | >100M |
| 2–4 | 341 |
| 5–9 | 5336 |
| 10–14 | 232 |
| 15–99 | 34 |
| 100–500 | 7 |

Table 6 presents Spanner operation latencies as measured from F1 servers. Replicas in the east-coast data centers are given higher priority in choosing Paxos leaders. The data in the table is measured from F1 servers in those data centers. The large standard deviation in write latencies is caused by a pretty fat tail due to lock conflicts. The even larger standard deviation in read latencies is partially due to the fact that Paxos leaders are spread across two data centers, only one of which has machines with SSDs. In addition, the measurement includes every read in the system from two datacenters: the mean and standard deviation of the bytes read were roughly 1.6KB and 119KB, respectively.

**Table 6: F1-perceived operation latencies (24 hours)**

| Operation | Mean (ms) | Std Dev (ms) | Count |
|-----------|-----------|--------------|--------|
| All reads | 8.7 | 376.4 | 21.5B |
| Single-site commit | 72.3 | 112.8 | 31.2M |
| Multi-site commit | 103.0 | 52.2 | 32.1M |

---

### النسخة العربية

نقيس أولاً أداء سبانر فيما يتعلق بالنسخ المتماثل والمعاملات والتوافر. ثم نقدم بعض البيانات حول سلوك TrueTime، ودراسة حالة لعميلنا الأول، F1.

**5.1 المعايير المرجعية الدقيقة**

يعرض الجدول 3 بعض المعايير المرجعية الدقيقة لسبانر. تم أخذ هذه القياسات على آلات مشتركة الوقت: عمل كل خادم سبان على وحدات جدولة بسعة 4 جيجابايت من الذاكرة و 4 أنوية (AMD Barcelona 2200MHz). تم تشغيل العملاء على آلات منفصلة. احتوت كل منطقة على خادم سبان واحد. تم وضع العملاء والمناطق في مجموعة من مراكز البيانات بمسافة شبكة أقل من 1 ميللي ثانية. (يجب أن يكون مثل هذا التخطيط شائعاً: معظم التطبيقات لا تحتاج إلى توزيع جميع بياناتها في جميع أنحاء العالم.) تم إنشاء قاعدة البيانات الاختبارية بـ 50 مجموعة باكسوس مع 2500 دليل. كانت العمليات قراءات وكتابات مستقلة بحجم 4 كيلوبايت. تم تقديم جميع القراءات من الذاكرة بعد الضغط، بحيث نقيس فقط الحمل الزائد لكومة استدعاءات سبانر. بالإضافة إلى ذلك، تم إجراء جولة غير مقاسة من القراءات أولاً لتدفئة أي ذاكرات تخزين مؤقت للموقع.

بالنسبة لتجارب زمن الانتقال، أصدر العملاء عمليات قليلة بما يكفي لتجنب الانتظار في قوائم الانتظار عند الخوادم. من تجارب النسخة الواحدة، يبلغ انتظار التنفيذ حوالي 5 ميللي ثانية، وزمن انتقال باكسوس حوالي 9 ميللي ثانية. مع زيادة عدد النسخ المتماثلة، يبقى زمن الانتقال ثابتاً تقريباً مع انحراف معياري أقل لأن باكسوس يُنفذ بالتوازي عند النسخ المتماثلة للمجموعة. مع زيادة عدد النسخ المتماثلة، يصبح زمن الانتقال لتحقيق النصاب أقل حساسية للبطء عند نسخة عبد واحدة.

بالنسبة لتجارب الإنتاجية، أصدر العملاء عمليات كافية لتشبع وحدات المعالجة المركزية للخوادم. يمكن لقراءات اللقطة التنفيذ عند أي نسخ محدثة، لذا تزداد إنتاجيتها بشكل شبه خطي مع عدد النسخ المتماثلة. تُنفذ معاملات القراءة فقط أحادية القراءة فقط عند القادة لأن تعيين الطابع الزمني يجب أن يحدث عند القادة. تزداد إنتاجية معاملات القراءة فقط مع عدد النسخ المتماثلة لأن عدد خوادم سبان الفعالة يزداد: في الإعداد التجريبي، كان عدد خوادم سبان يساوي عدد النسخ المتماثلة، وتم توزيع القادة عشوائياً بين المناطق. تستفيد إنتاجية الكتابة من نفس القطعة التجريبية (والتي تفسر الزيادة في الإنتاجية من 3 إلى 5 نسخ)، لكن تلك الفائدة يتم التغلب عليها بالزيادة الخطية في كمية العمل المنجز لكل كتابة، مع زيادة عدد النسخ المتماثلة.

يوضح الجدول 4 أن التنفيذ ثنائي المرحلة يمكن أن يتوسع إلى عدد معقول من المشاركين: يلخص مجموعة من التجارب التي أجريت عبر 3 مناطق، كل منها بـ 25 خادم سبان. التوسع حتى 50 مشاركاً معقول في كل من المتوسط والمئين 99، وتبدأ أزمنة الانتقال في الارتفاع بشكل ملحوظ عند 100 مشارك.

**الجدول 4: قابلية التوسع للتنفيذ ثنائي المرحلة**

| المشاركون | المتوسط (ميللي ثانية) | المئين 99 (ميللي ثانية) |
|-----------|----------------------|------------------------|
| 1 | 17.0±1.4 | 75.0±34.9 |
| 2 | 24.5±2.5 | 87.6±35.9 |
| 5 | 31.5±6.2 | 104.5±52.2 |
| 10 | 30.0±3.7 | 95.6±25.4 |
| 25 | 35.5±5.6 | 100.4±42.7 |
| 50 | 42.7±4.1 | 93.7±22.9 |
| 100 | 71.4±7.6 | 131.2±17.6 |
| 200 | 150.5±11.0 | 320.3±35.1 |

**5.2 التوافر**

يوضح الشكل 5 فوائد التوافر من تشغيل سبانر في مراكز بيانات متعددة. يظهر نتائج ثلاث تجارب على الإنتاجية في وجود فشل مركز البيانات، والتي تم تراكبها جميعاً على نفس المقياس الزمني. تكون كون الاختبار من 5 مناطق Zᵢ، كل منها بـ 25 خادم سبان. تم تجزئة قاعدة البيانات الاختبارية إلى 1250 مجموعة باكسوس، وأصدر 100 عميل اختبار باستمرار قراءات غير لقطة بمعدل إجمالي 50 ألف قراءة/ثانية. تم وضع جميع القادة صراحةً في Z₁. بعد خمس ثوانٍ من كل اختبار، تم قتل جميع الخوادم في منطقة واحدة: القتل غير القائد يقتل Z₂؛ القتل الصعب للقائد يقتل Z₁؛ القتل اللين للقائد يقتل Z₁، لكنه يعطي إشعارات لجميع الخوادم بأنه يجب عليها تسليم القيادة أولاً.

قتل Z₂ ليس له تأثير على إنتاجية القراءة. قتل Z₁ مع إعطاء القادة وقتاً لتسليم القيادة إلى منطقة مختلفة له تأثير بسيط: انخفاض الإنتاجية غير مرئي في الرسم البياني، لكنه حوالي 3-4٪. من ناحية أخرى، قتل Z₁ بدون تحذير له تأثير شديد: ينخفض معدل الإكمال تقريباً إلى 0. مع إعادة انتخاب القادة، ترتفع إنتاجية النظام إلى حوالي 100 ألف قراءة/ثانية بسبب قطعتين من تجربتنا: هناك سعة إضافية في النظام، والعمليات في قائمة انتظار بينما القائد غير متاح. ونتيجة لذلك، ترتفع إنتاجية النظام قبل الاستقرار مرة أخرى عند معدلها الثابت.

يمكننا أيضاً رؤية تأثير حقيقة أن عقود إيجار قائد باكسوس مضبوطة على 10 ثوانٍ. عندما نقتل المنطقة، يجب أن تكون أوقات انتهاء صلاحية عقد إيجار القائد للمجموعات موزعة بالتساوي على مدى الـ 10 ثوانٍ التالية. بعد وقت قصير من انتهاء صلاحية كل عقد إيجار من قائد ميت، يتم انتخاب قائد جديد. بعد حوالي 10 ثوانٍ من وقت القتل، يكون لدى جميع المجموعات قادة وقد تعافت الإنتاجية. ستقلل أوقات عقد الإيجار الأقصر من تأثير وفيات الخوادم على التوافر، لكنها ستتطلب كميات أكبر من حركة مرور شبكة تجديد عقد الإيجار. نحن في عملية تصميم وتنفيذ آلية ستتسبب في قيام العبيد بإطلاق عقود إيجار قائد باكسوس عند فشل القائد.

**5.3 TrueTime**

يجب الإجابة على سؤالين فيما يتعلق بـ TrueTime: هل ε حقاً حد على عدم اليقين في الساعة، وإلى أي مدى يسوء ε؟ بالنسبة للأول، ستكون المشكلة الأكثر خطورة إذا كان انحراف الساعة المحلية أكبر من 200 ميكروثانية/ثانية: سيؤدي ذلك إلى كسر الافتراضات التي وضعها TrueTime. تُظهر إحصائيات آلاتنا أن وحدات المعالجة المركزية السيئة أكثر احتمالاً بـ 6 مرات من الساعات السيئة. أي أن مشكلات الساعة نادرة للغاية، بالنسبة لمشاكل الأجهزة الأكثر خطورة. ونتيجة لذلك، نعتقد أن تنفيذ TrueTime جدير بالثقة مثل أي قطعة أخرى من البرمجيات التي تعتمد عليها سبانر.

يعرض الشكل 6 بيانات TrueTime المأخوذة من عدة آلاف من آلات خادم سبان عبر مراكز البيانات حتى 2200 كم بعيدة. يرسم المئينات 90 و 99 و 99.9 من ε، المأخوذة عينات عند عفاريت عبد الوقت مباشرة بعد استقصاء أسياد الوقت. يزيل هذا أخذ العينات المنشار في ε بسبب عدم اليقين في الساعة المحلية، وبالتالي يقيس عدم يقين سيد الوقت (الذي يكون عموماً 0) بالإضافة إلى تأخير الاتصال بأسياد الوقت.

تُظهر البيانات أن هذين العاملين في تحديد القيمة الأساسية لـ ε ليسا مشكلة عموماً. ومع ذلك، يمكن أن تكون هناك مشاكل كبيرة في زمن الانتقال الذيلي تتسبب في قيم أعلى لـ ε. كان الانخفاض في أزمنة الانتقال الذيلية بدءاً من 30 مارس بسبب تحسينات الشبكات التي قللت من احتقان رابط الشبكة العابر. نتجت الزيادة في ε في 13 أبريل، حوالي ساعة واحدة من المدة، عن إيقاف تشغيل 2 من أسياد الوقت في مركز بيانات للصيانة الروتينية. نواصل التحقيق وإزالة أسباب ارتفاعات TrueTime.

**5.4 F1**

بدأت سبانر في التقييم التجريبي تحت أحمال عمل الإنتاج في أوائل عام 2011، كجزء من إعادة كتابة للواجهة الخلفية للإعلانات في جوجل تسمى F1 [35]. كانت هذه الواجهة الخلفية في الأصل تعتمد على قاعدة بيانات MySQL تم تجزئتها يدوياً بعدة طرق. مجموعة البيانات غير المضغوطة عشرات التيرابايتات، وهي صغيرة مقارنة بالعديد من حالات NoSQL، لكنها كانت كبيرة بما يكفي للتسبب في صعوبات مع MySQL المجزأة. عيّن مخطط تجزئة MySQL كل عميل وجميع البيانات ذات الصلة إلى جزء ثابت. مكّن هذا التخطيط من استخدام الفهارس ومعالجة الاستعلام المعقدة على أساس كل عميل، لكنه تطلب بعض المعرفة بالتجزئة في منطق أعمال التطبيق. كانت إعادة تجزئة قاعدة البيانات الحرجة للإيرادات هذه مع نموها في عدد العملاء وبياناتهم مكلفة للغاية. استغرقت آخر إعادة تجزئة أكثر من عامين من الجهد المكثف، وتضمنت التنسيق والاختبار عبر عشرات الفرق لتقليل المخاطر. كانت هذه العملية معقدة جداً للقيام بها بانتظام: ونتيجة لذلك، اضطر الفريق إلى الحد من النمو على قاعدة بيانات MySQL عن طريق تخزين بعض البيانات في Bigtables خارجية، مما أضر بالسلوك المعاملاتي والقدرة على الاستعلام عبر جميع البيانات.

اختار فريق F1 استخدام سبانر لعدة أسباب. أولاً، تزيل سبانر الحاجة إلى إعادة التجزئة يدوياً. ثانياً، توفر سبانر النسخ المتماثل المتزامن والتحويل التلقائي عند الفشل. مع النسخ المتماثل سيد-عبد لـ MySQL، كان التحويل عند الفشل صعباً، وخاطر بفقدان البيانات ووقت التوقف. ثالثاً، يتطلب F1 دلالات معاملاتية قوية، مما جعل استخدام أنظمة NoSQL الأخرى غير عملي. تتطلب دلالات التطبيق معاملات عبر البيانات التعسفية، والقراءات المتسقة. احتاج فريق F1 أيضاً إلى فهارس ثانوية على بياناتهم (حيث لا توفر سبانر بعد دعماً تلقائياً للفهارس الثانوية)، وكانوا قادرين على تنفيذ فهارسهم العالمية المتسقة الخاصة باستخدام معاملات سبانر.

يتم الآن إرسال جميع كتابات التطبيق افتراضياً عبر F1 إلى سبانر، بدلاً من كومة التطبيق القائمة على MySQL. لدى F1 نسختان على الساحل الغربي للولايات المتحدة، و 3 على الساحل الشرقي. تم اتخاذ هذا الاختيار لمواقع النسخ المتماثلة للتعامل مع الانقطاعات بسبب الكوارث الطبيعية الكبرى المحتملة، وأيضاً اختيار مواقع الواجهة الأمامية الخاصة بهم. بشكل قصصي، كان التحويل التلقائي عند الفشل لسبانر غير مرئي تقريباً لهم. على الرغم من وجود حالات فشل عنقودية غير مخططة في الأشهر القليلة الماضية، كان أقصى ما اضطر فريق F1 للقيام به هو تحديث مخطط قاعدة بياناتهم لإخبار سبانر أين يضع قادة باكسوس تفضيلياً، للحفاظ عليهم بالقرب من المكان الذي انتقلت إليه واجهاتهم الأمامية.

جعلت دلالات الطابع الزمني لسبانر من الفعال لـ F1 الحفاظ على بنى بيانات في الذاكرة محسوبة من حالة قاعدة البيانات. يحافظ F1 على سجل تاريخ منطقي لجميع التغييرات، والذي يُكتب في سبانر نفسها كجزء من كل معاملة. يأخذ F1 لقطات كاملة من البيانات عند طابع زمني لتهيئة بنى بياناته، ثم يقرأ التغييرات التدريجية لتحديثها.

يوضح الجدول 5 توزيع عدد الشظايا لكل دليل في F1. يتوافق كل دليل عادةً مع عميل في كومة التطبيق فوق F1. الغالبية العظمى من الأدلة (وبالتالي العملاء) تتكون من شظية واحدة فقط، مما يعني أن القراءات والكتابات لبيانات هؤلاء العملاء مضمونة أن تحدث على خادم واحد فقط. الأدلة التي تحتوي على أكثر من 100 شظية هي جميع الجداول التي تحتوي على فهارس F1 الثانوية: الكتابات إلى أكثر من بضع شظايا من هذه الجداول نادرة للغاية. رأى فريق F1 فقط مثل هذا السلوك عندما يقومون بتحميل بيانات كبيرة غير محسّنة كمعاملات.

**الجدول 5: توزيع أعداد شظايا الدليل في F1**

| # الشظايا | # الأدلة |
|-----------|----------|
| 1 | >100M |
| 2–4 | 341 |
| 5–9 | 5336 |
| 10–14 | 232 |
| 15–99 | 34 |
| 100–500 | 7 |

يعرض الجدول 6 أزمنة انتقال عمليات سبانر كما تم قياسها من خوادم F1. يتم إعطاء النسخ في مراكز البيانات على الساحل الشرقي أولوية أعلى في اختيار قادة باكسوس. البيانات في الجدول مقاسة من خوادم F1 في تلك مراكز البيانات. الانحراف المعياري الكبير في أزمنة انتقال الكتابة ناتج عن ذيل سمين جداً بسبب تعارضات الأقفال. الانحراف المعياري الأكبر في أزمنة انتقال القراءة يرجع جزئياً إلى حقيقة أن قادة باكسوس منتشرون عبر مركزي بيانات، واحد منهما فقط لديه آلات مع أقراص SSD. بالإضافة إلى ذلك، يتضمن القياس كل قراءة في النظام من مركزي بيانات: كان متوسط والانحراف المعياري للبايتات المقروءة حوالي 1.6 كيلوبايت و 119 كيلوبايت، على التوالي.

**الجدول 6: أزمنة انتقال العمليات المدركة لـ F1 (24 ساعة)**

| العملية | المتوسط (ميللي ثانية) | الانحراف المعياري (ميللي ثانية) | العدد |
|---------|----------------------|--------------------------------|--------|
| جميع القراءات | 8.7 | 376.4 | 21.5B |
| تنفيذ أحادي الموقع | 72.3 | 112.8 | 31.2M |
| تنفيذ متعدد المواقع | 103.0 | 52.2 | 32.1M |

---

### Translation Notes

- **Figures referenced:** Figure 5 (throughput with datacenter failures), Figure 6 (TrueTime ε distribution)
- **Tables referenced:** Table 3 (microbenchmarks), Table 4 (two-phase commit scalability), Table 5 (F1 directory fragments), Table 6 (F1 operation latencies)
- **Key terms introduced:**
  - Microbenchmark (معيار مرجعي دقيق)
  - Throughput (الإنتاجية)
  - Quorum (النصاب)
  - Handoff (تسليم)
  - Failover (التحويل عند الفشل)
  - Tail latency (زمن الانتقال الذيلي)
  - Sharding/Resharding (التجزئة/إعادة التجزئة)
  - Secondary index (فهرس ثانوي)
  - Percentile (المئين)
- **Performance data:** Multiple tables with benchmark results
- **Citations:** [35]
- **Special handling:**
  - Performance numbers and statistics kept precise
  - Product names kept: F1, MySQL, Bigtable, NoSQL, AMD Barcelona
  - Statistical notation: mean±std dev preserved
  - Units: ms, KB, GB preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.92
- Readability: 0.85
- Glossary consistency: 0.95
- **Overall section score:** 0.87
