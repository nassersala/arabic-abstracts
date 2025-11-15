# Section 5: Evaluation
## القسم 5: التقييم

**Section:** evaluation
**Translation Quality:** 0.88
**Glossary Terms Used:** throughput, latency, performance, benchmark, scalability, fault-tolerant, workload

---

### English Version

We performed all of our evaluation on a cluster of 50 servers. Each server has one Xeon dual-core 2.1GHz processor, 4GB of RAM, gigabit ethernet, and two SATA hard drives. We split the following discussion into two parts: throughput and latency of requests.

To evaluate our system, we benchmark it using a Java implementation and a C implementation of the client. Both implementations have synchronous and asynchronous versions of the API. For simplicity of presentation, we only present results using the Java version in the synchronput API mode since the results are similar for the C version.

We use the same saturation benchmark as used in the Chubby [6] performance evaluation: we have clients continuously issue outstanding requests, waiting until the outstanding request completes before issuing another one. To create this workload, we have clients maintain a set of watch events that correspond to state changes. If watches are triggered, but not explicitly read by the client, performance of ZooKeeper is better.

#### 5.1 Throughput

To assess the throughput of ZooKeeper, we vary the ratio of read to write requests of the workload and observe the number of operations completed by the server pool. Figure 3 shows the throughput of ZooKeeper across different R/W ratios. Each point represents 5 runs with different seeds, each running for 5 minutes. The error bars represent the standard deviation of all runs.

When the workload is dominated by reads (which is common for our target applications), the performance of ZooKeeper is excellent: with 13 ZooKeeper servers the measured throughput is about 100,000 operations per second for 100% reads, and the throughput stays above 40,000 operations per second through 50% writes. Read throughput is higher than write throughput because reads do not use atomic broadcast. One interesting observation from Figure 3 is that read throughput drops once we have more than 9 servers in the ensemble. This drop is caused by the TCP traffic of the pinging mechanism used to keep track of the state of clients. At around 9 servers, the aggregate network traffic becomes sufficiently high to interfere with the inter-server traffic needed to drive up the throughput.

The graph also shows that the number of servers also impacts the write performance. Write throughput falls with more servers because the agreement protocol requires a majority of servers to acknowledge a change, and with more servers there is more traffic. These experiments show that ZooKeeper can handle tens to hundreds of thousands of transactions per second for read-heavy workloads, a typical workload pattern for coordination.

#### 5.2 Latency

To assess the latency of requests, we created a benchmark for which we have a single client issuing a request and we measure the request latency directly. For writes, we log the time it takes to complete the atomic broadcast of a request. For reads, we log the time it takes to read the data from the local replica. Figure 4 shows the average latency of reads and writes across a three-server ensemble.

In a three-server ensemble, we observe read latencies on the order of 0.7ms and write latencies of about 8.5ms. Write latencies are much higher because they involve processing on all servers and require waiting for acknowledgements. We found that the dominant factor for latency is the time to write the transaction log entry to stable storage, as reported also by others [6]. In our environment, flushing a write to disk takes about 5ms. Because writes are processed in order, if there are several outstanding writes, batching by the disk provides some amortization and latency does not increase linearly with write load.

#### 5.3 Barriers

In this experiment we use ZooKeeper to implement barriers (described in Section 3.7). For this experiment, we use a varying number of barriers, b, where b ∈ {200, 400, 800, 1600}. We sequentially enter b barriers, where each barrier is composed of entering and leaving. To enter a barrier a client creates a znode until the total number of children of the barrier znode equals the size of the barrier. Once the threshold is reached, clients mark a ready child znode, signaling that the barrier is saturated. Clients wait for the ready child before entering the barrier. To leave, clients delete their corresponding child of the barrier znode and wait until all children have been deleted.

In each run of this experiment, we use 50, 100, and 200 clients to enter and leave each of b barriers sequentially. We vary the size of the barrier from 10 to 100. We measure the time to cross the b barriers with the exception of the first barrier because it initializes state in the file system. Because of the characteristics of the atomic broadcast protocol, the time to reach the barrier threshold depends on the time that the first client calls enter. On average, the time for an enter operation was about 3ms. We observed that the time to saturate b barriers (enter in all b barriers) increases with the number of barriers that a client process has to enter. The throughput for a give number of clients and a barrier size is roughly constant and independent of the number of barriers b. A client can complete about 1950 barriers per second for b = 200, and 3100 barriers per second for b = 1600 on 50 clients. With 200 clients the throughput increases considerably due to clients processing in parallel: 7000 for b = 200, and 8600 for b = 1600. The saturation point of ZooKeeper is mainly dominated by write throughput, as shown in Section 5.1.

#### 5.4 Atomic Broadcast Performance

ZooKeeper's atomic broadcast protocol spends most of its time writing to disk. Consequently, throughput of atomic broadcast is limited by how fast the disk writes can be committed. On one server driving the atomic broadcast throughput, we measured 15,000-16,000 requests per second. On faster hardware (Intel Xeon X5570 with RAID controller and dual battery backed SDRAM write caches), we were able to achieve approximately 35,000-40,000 requests per second throughput for atomic broadcast.

We note that ZooKeeper has been designed so that writes are handled by a single leader process that broadcasts changes to the ZooKeeper state. This design is ideal for write loads that are small-to-moderate. For extremely write-heavy loads, the system may be unable to achieve its throughput goal since the leader may be overwhelmed with preparing and committing state changes. However, practical deployments of ZooKeeper, such as at Yahoo!, typically exhibit read-to-write ratios of 10:1 or more.

#### 5.5 Data Tree Size

We also evaluated the impact of the size of the data tree on performance. For this experiment, we created trees of znodes of varying sizes from 0 to 1,000,000 znodes. Every znode contains 5 bytes of data. Figure 5 shows the throughput for 100% read, 100% write, and mixed read/write workloads. As can be seen, throughput is not impacted by the number of znodes, which indicates that our implementation can scale well with the number of znodes in the tree.

#### 5.6 Watch Events

ZooKeeper's ability to efficiently notify clients of state changes is critical to realizing many of the coordination recipes described in Section 3. To evaluate the notification performance, we created a simple experiment where we have 25 servers with a single leader, with a variable number of clients. Each of the clients creates a znode and sets a watch on the znode. After a 2-second warmup period, the clients update the znode once, which triggers the watch. In this experiment, we measure the total number of watches that could be processed per second.

Figure 6 shows the notification rate for a varying number of clients, demonstrating that ZooKeeper can handle tens of thousands of watches per second. For the experiment, we varied the number of clients from 100 to 800. At 100 clients, the total notification rate was about 50,000 watches per second. This rate increased to about 90,000 watches per second for 800 clients. To see why the increase occurs, we need to understand what happens when a watch event is triggered: the leader sends the notification to all followers, who in turn notify their connected clients. As the number of clients increases, more of them are distributed across the server ensemble, and thus receive notifications in parallel, improving overall notification throughput.

---

### النسخة العربية

أجرينا جميع تقييماتنا على مجموعة من 50 خادماً. يحتوي كل خادم على معالج Xeon ثنائي النواة بسرعة 2.1 جيجاهرتز، و 4 جيجابايت من ذاكرة الوصول العشوائي، وإيثرنت جيجابت، وقرصين صلبين من نوع SATA. نقسم المناقشة التالية إلى جزأين: إنتاجية وزمن وصول الطلبات.

لتقييم نظامنا، نقوم بقياسه باستخدام تنفيذ Java وتنفيذ C لواجهة برمجة تطبيقات العميل. كلا التنفيذين لهما إصدارات متزامنة وغير متزامنة من واجهة برمجة التطبيقات. من أجل بساطة العرض، نقدم فقط النتائج باستخدام إصدار Java في وضع واجهة برمجة التطبيقات المتزامنة لأن النتائج مماثلة لإصدار C.

نستخدم نفس معيار التشبع المستخدم في تقييم أداء Chubby [6]: لدينا عملاء يصدرون طلبات معلقة باستمرار، في انتظار اكتمال الطلب المعلق قبل إصدار طلب آخر. لإنشاء حمل العمل هذا، يحتفظ العملاء بمجموعة من أحداث المراقبة التي تتوافق مع تغييرات الحالة. إذا تم تحفيز المراقبات، ولكن لم يقرأها العميل بشكل صريح، فإن أداء زوكيبر يكون أفضل.

#### 5.1 الإنتاجية

لتقييم إنتاجية زوكيبر، نقوم بتغيير نسبة طلبات القراءة إلى الكتابة لحمل العمل ونراقب عدد العمليات التي أكملتها مجموعة الخوادم. يوضح الشكل 3 إنتاجية زوكيبر عبر نسب قراءة/كتابة مختلفة. تمثل كل نقطة 5 تشغيلات ببذور مختلفة، كل منها يعمل لمدة 5 دقائق. تمثل أشرطة الخطأ الانحراف المعياري لجميع التشغيلات.

عندما يهيمن على حمل العمل القراءات (وهو أمر شائع لتطبيقاتنا المستهدفة)، يكون أداء زوكيبر ممتازاً: مع 13 خادم زوكيبر، الإنتاجية المقاسة حوالي 100,000 عملية في الثانية لـ 100% قراءات، وتبقى الإنتاجية فوق 40,000 عملية في الثانية من خلال 50% كتابات. إنتاجية القراءة أعلى من إنتاجية الكتابة لأن القراءات لا تستخدم البث الذري. ملاحظة مثيرة للاهتمام من الشكل 3 هي أن إنتاجية القراءة تنخفض بمجرد أن يكون لدينا أكثر من 9 خوادم في المجموعة. يحدث هذا الانخفاض بسبب حركة مرور TCP لآلية الاختبار المستخدمة لتتبع حالة العملاء. في حوالي 9 خوادم، تصبح حركة مرور الشبكة المجمعة عالية بما يكفي للتداخل مع حركة المرور بين الخوادم اللازمة لرفع الإنتاجية.

يوضح الرسم البياني أيضاً أن عدد الخوادم يؤثر أيضاً على أداء الكتابة. تنخفض إنتاجية الكتابة مع المزيد من الخوادم لأن بروتوكول الاتفاق يتطلب من غالبية الخوادم الاعتراف بالتغيير، ومع المزيد من الخوادم تكون هناك المزيد من حركة المرور. تُظهر هذه التجارب أن زوكيبر يمكنها التعامل مع عشرات إلى مئات الآلاف من المعاملات في الثانية لأحمال العمل الثقيلة على القراءة، وهو نمط حمل عمل نموذجي للتنسيق.

#### 5.2 زمن الوصول

لتقييم زمن وصول الطلبات، أنشأنا معياراً لدينا فيه عميل واحد يصدر طلباً ونقيس زمن وصول الطلب مباشرة. بالنسبة للكتابات، نسجل الوقت الذي يستغرقه إكمال البث الذري للطلب. بالنسبة للقراءات، نسجل الوقت الذي يستغرقه قراءة البيانات من النسخة المحلية. يوضح الشكل 4 متوسط زمن الوصول للقراءات والكتابات عبر مجموعة من ثلاثة خوادم.

في مجموعة من ثلاثة خوادم، نلاحظ زمن وصول القراءة في حدود 0.7 ميلي ثانية وزمن وصول الكتابة حوالي 8.5 ميلي ثانية. زمن وصول الكتابة أعلى بكثير لأنها تتضمن معالجة على جميع الخوادم وتتطلب انتظار التأكيدات. وجدنا أن العامل المهيمن لزمن الوصول هو الوقت لكتابة إدخال سجل المعاملات إلى التخزين المستقر، كما أبلغ آخرون أيضاً [6]. في بيئتنا، يستغرق مسح الكتابة إلى القرص حوالي 5 ميلي ثانية. نظراً لأن الكتابات تتم معالجتها بالترتيب، إذا كانت هناك عدة كتابات معلقة، فإن الدُفعات من القرص توفر بعض الإطفاء ولا يزيد زمن الوصول خطياً مع حمل الكتابة.

#### 5.3 الحواجز

في هذه التجربة، نستخدم زوكيبر لتنفيذ الحواجز (الموصوفة في القسم 3.7). لهذه التجربة، نستخدم عدداً متفاوتاً من الحواجز، b، حيث b ∈ {200، 400، 800، 1600}. ندخل بشكل تسلسلي b حواجز، حيث يتكون كل حاجز من الدخول والمغادرة. لدخول حاجز، ينشئ العميل عقدة بيانات حتى يساوي العدد الإجمالي لأطفال عقدة بيانات الحاجز حجم الحاجز. بمجرد الوصول إلى العتبة، يميز العملاء عقدة بيانات فرعية جاهزة، للإشارة إلى أن الحاجز مشبع. ينتظر العملاء الطفل الجاهز قبل دخول الحاجز. للمغادرة، يحذف العملاء الطفل المقابل لعقدة بيانات الحاجز وينتظرون حتى يتم حذف جميع الأطفال.

في كل تشغيل لهذه التجربة، نستخدم 50 و 100 و 200 عميل لدخول ومغادرة كل من b حواجز بشكل تسلسلي. نغير حجم الحاجز من 10 إلى 100. نقيس الوقت لعبور b حواجز باستثناء الحاجز الأول لأنه يُهيئ الحالة في نظام الملفات. بسبب خصائص بروتوكول البث الذري، يعتمد الوقت للوصول إلى عتبة الحاجز على الوقت الذي يستدعي فيه العميل الأول الدخول. في المتوسط، كان الوقت لعملية الدخول حوالي 3 ميلي ثانية. لاحظنا أن الوقت لإشباع b حواجز (الدخول في جميع b حواجز) يزداد مع عدد الحواجز التي يجب أن تدخلها عملية العميل. الإنتاجية لعدد معين من العملاء وحجم حاجز ثابتة تقريباً ومستقلة عن عدد الحواجز b. يمكن للعميل إكمال حوالي 1950 حاجزاً في الثانية لـ b = 200، و 3100 حاجزاً في الثانية لـ b = 1600 على 50 عميلاً. مع 200 عميل، تزداد الإنتاجية بشكل كبير بسبب معالجة العملاء بالتوازي: 7000 لـ b = 200، و 8600 لـ b = 1600. نقطة التشبع لزوكيبر تهيمن عليها بشكل أساسي إنتاجية الكتابة، كما هو موضح في القسم 5.1.

#### 5.4 أداء البث الذري

يقضي بروتوكول البث الذري لزوكيبر معظم وقته في الكتابة على القرص. وبالتالي، فإن إنتاجية البث الذري محدودة بمدى سرعة الالتزام بكتابات القرص. على خادم واحد يقود إنتاجية البث الذري، قسنا 15,000-16,000 طلب في الثانية. على أجهزة أسرع (Intel Xeon X5570 مع وحدة تحكم RAID وذاكرة تخزين مؤقت كتابة SDRAM مزدوجة مدعومة بالبطارية)، تمكنا من تحقيق ما يقرب من 35,000-40,000 طلب في الثانية إنتاجية للبث الذري.

نلاحظ أن زوكيبر قد تم تصميمه بحيث يتم التعامل مع الكتابات بواسطة عملية قائد واحدة تبث التغييرات على حالة زوكيبر. هذا التصميم مثالي لأحمال الكتابة الصغيرة إلى المتوسطة. بالنسبة لأحمال الكتابة الثقيلة للغاية، قد لا يتمكن النظام من تحقيق هدف الإنتاجية لأن القائد قد يكون مرهقاً بإعداد والالتزام بتغييرات الحالة. ومع ذلك، فإن عمليات النشر العملية لزوكيبر، مثل في Yahoo!، تظهر عادةً نسب قراءة إلى كتابة 10:1 أو أكثر.

#### 5.5 حجم شجرة البيانات

قمنا أيضاً بتقييم تأثير حجم شجرة البيانات على الأداء. لهذه التجربة، أنشأنا أشجاراً من عقد البيانات بأحجام متفاوتة من 0 إلى 1,000,000 عقدة بيانات. تحتوي كل عقدة بيانات على 5 بايتات من البيانات. يوضح الشكل 5 الإنتاجية لـ 100% قراءة، 100% كتابة، وأحمال عمل قراءة/كتابة مختلطة. كما يمكن رؤيته، لا تتأثر الإنتاجية بعدد عقد البيانات، مما يشير إلى أن تنفيذنا يمكن أن يتوسع بشكل جيد مع عدد عقد البيانات في الشجرة.

#### 5.6 أحداث المراقبة

قدرة زوكيبر على إخطار العملاء بكفاءة بتغييرات الحالة أمر حاسم لتحقيق العديد من وصفات التنسيق الموصوفة في القسم 3. لتقييم أداء الإخطار، أنشأنا تجربة بسيطة حيث لدينا 25 خادماً مع قائد واحد، مع عدد متغير من العملاء. ينشئ كل من العملاء عقدة بيانات ويعين مراقبة على عقدة البيانات. بعد فترة إحماء مدتها ثانيتان، يحدث العملاء عقدة البيانات مرة واحدة، مما يحفز المراقبة. في هذه التجربة، نقيس العدد الإجمالي للمراقبات التي يمكن معالجتها في الثانية.

يوضح الشكل 6 معدل الإخطار لعدد متفاوت من العملاء، مما يدل على أن زوكيبر يمكنها التعامل مع عشرات الآلاف من المراقبات في الثانية. للتجربة، غيرنا عدد العملاء من 100 إلى 800. عند 100 عميل، كان معدل الإخطار الإجمالي حوالي 50,000 مراقبة في الثانية. زاد هذا المعدل إلى حوالي 90,000 مراقبة في الثانية لـ 800 عميل. لمعرفة سبب حدوث الزيادة، نحتاج إلى فهم ما يحدث عند تحفيز حدث مراقبة: يرسل القائد الإخطار إلى جميع المتابعين، الذين بدورهم يخطرون عملائهم المتصلين. مع زيادة عدد العملاء، يتم توزيع المزيد منهم عبر مجموعة الخوادم، وبالتالي يتلقون إخطارات بالتوازي، مما يحسن الإنتاجية الإجمالية للإخطار.

---

### Translation Notes

- **Figures referenced:** Figures 3, 4, 5, 6 (performance graphs)
- **Key terms introduced:**
  - Throughput (إنتاجية) - operations per second
  - Latency (زمن الوصول) - response time
  - Saturation benchmark (معيار التشبع) - performance test
  - Read-heavy workload (حمل عمل ثقيل على القراءة) - typical pattern
  - Stable storage (التخزين المستقر) - durable storage

- **Equations:** None
- **Citations:** [6] - Chubby reference
- **Special handling:**
  - Performance numbers preserved exactly (100,000 ops/sec, 0.7ms, etc.)
  - Hardware specifications kept in English (Xeon, SATA, RAID, etc.)
  - Mathematical notation (b ∈ {200, 400, 800, 1600}) preserved
  - Company names (Yahoo!) kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-translation Check

First paragraph back-translation: "We performed all our evaluations on a cluster of 50 servers. Each server has one Xeon dual-core 2.1GHz processor, 4GB of RAM, gigabit ethernet, and two SATA hard drives..."

✅ Semantically equivalent to original
