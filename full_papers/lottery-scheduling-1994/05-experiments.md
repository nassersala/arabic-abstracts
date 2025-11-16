# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** fairness, throughput, response time, benchmark, Dhrystone, Monte-Carlo, client-server, MPEG, multimedia, ticket allocation, observed ratio, variance, standard deviation, overhead

---

### English Version

In order to evaluate our prototype lottery scheduler, we conducted experiments designed to quantify its ability to flexibly, responsively, and efficiently control the relative execution rates of computations. The applications used in our experiments include the compute-bound Dhrystone benchmark, a Monte-Carlo numerical integration program, a multithreaded client-server application for searching text, and competing MPEG video viewers.

## 5.1 Fairness

Our first experiment measured the accuracy with which our lottery scheduler could control the relative execution rates of computations. Each point plotted in Figure 4 indicates the relative execution rate that was observed for two tasks executing the Dhrystone benchmark [Wei84] for sixty seconds with a given relative ticket allocation. Three runs were executed for each integral ratio between one and ten.

With the exception of the run for which the 10:1 allocation resulted in an average ratio of 13.42:1, all of the observed ratios are close to their corresponding allocations. As expected, the variance is greater for larger ratios. However, even large ratios converge toward their allocated values over longer time intervals. For example, the observed ratio averaged over a three minute period for a 20:1 allocation was 19.08:1.

Although the results presented in Figure 4 indicate that the scheduler can successfully control computation rates, we should also examine its behavior over shorter time intervals. Figure 5 plots average iteration counts over a series of 8 second time windows during a single 200 second execution with a 2:1 allocation. Although there is clearly some variation, the two tasks remain close to their allocated ratios throughout the experiment. Note that if a scheduling quantum of 10 milliseconds were used instead of the 100 millisecond Mach quantum, the same degree of fairness would be observed over a series of subsecond time windows.

## 5.2 Flexible Control

A more interesting use of lottery scheduling involves dynamically controlled ticket inflation. A practical application that benefits from such control is the Monte-Carlo algorithm [Pre88]. Monte-Carlo is a probabilistic algorithm that is widely used in the physical sciences for computing average properties of systems. Since errors in the computed average are proportional to $1/\sqrt{n}$, where $n$ is the number of trials, accurate results require a large number of trials.

Scientists frequently execute several separate Monte-Carlo experiments to explore various hypotheses. It is often desirable to obtain approximate results quickly whenever a new experiment is started, while allowing older experiments to continue reducing their error at a slower rate [Hog88]. This goal would be impossible with conventional schedulers, but can be easily achieved in our system by dynamically adjusting an experiment's ticket value as a function of its current relative error. This allows a new experiment with high error to quickly catch up to older experiments by executing at a rate that starts high but then tapers off as its relative error approaches that of its older counterparts.

Figure 6 plots the total number of trials computed by each of three staggered Monte-Carlo tasks. Each task is based on the sample code presented in [Pre88], and is allocated a share of time that is proportional to the square of its relative error. When a new task is started, it initially receives a large share of the processor. This share diminishes as the task reduces its error to a value closer to that of the other executing tasks.

A similar form of dynamic control may also be useful in graphics-intensive programs. For example, a rendering operation could be granted a large share of processing resources until it has displayed a crude outline or wire-frame, and then given a smaller share of resources to compute a more polished image.

## 5.3 Client-Server Computation

As mentioned in Section 4.6, the Mach IPC primitive mach_msg was modified to temporarily transfer tickets from client to server on synchronous remote procedure calls. Thus, a client automatically redirects its resource rights to the server that is computing on its behalf. Multithreaded servers will process requests from different clients at the rates defined by their respective ticket allocations.

We developed a simple multithreaded client-server application that shares properties with real databases and information retrieval systems. Our server initially loads a 4.6 Mbyte text file "database" containing the complete text to all of William Shakespeare's plays. It then forks off several worker threads to process incoming queries from clients. One query operation supported by the server is a case-insensitive substring search over the entire database, which returns a count of the matches found.

Figure 7 presents the results of executing three database clients with an 8:3:1 ticket allocation. The server has no tickets of its own, and relies completely upon the tickets transferred by clients. Each client repeatedly sends requests to the server to count the occurrences of the same search string. The high-priority client issues a total of 20 queries and then terminates. The other two clients continue to issue queries for the duration of the entire experiment.

The ticket allocations affect both response time and throughput. When the high-priority client has completed its 20 requests, the other clients have completed a total of 10 requests, matching their overall 8:4 allocation. Over the entire experiment, the clients with a 3:1 ticket allocation respectively complete 38 and 13 queries, which closely matches their allocation, despite their transient competition with the high-priority client. While the high-priority client is active, the average response times seen by the clients are 17.19, 43.19, and 132.20 seconds, yielding relative speeds of 7.69:2.51:1. After the high-priority client terminates, the response times are 44.17 and 15.18 seconds, for a 2.91:1 ratio. For all average response times, the standard deviation is less than 7% of the average.

A similar form of control could be employed by database or transaction-processing applications to manage the response times seen by competing clients or transactions. This would be useful in providing different levels of service to clients or transactions with varying importance (or real monetary funding).

## 5.4 Multimedia Applications

Media-based applications are another domain that can benefit from lottery scheduling. Compton and Tennenhouse described the need to control the quality of service when two or more video viewers are displayed — a level of control not offered by current operating systems [Com94]. They attempted, with mixed success, to control video display rates at the application level among a group of mutually trusting viewers. Cooperating viewers employed feedback mechanisms to adjust their relative frame rates. Inadequate and unstable metrics for system load necessitated substantial tuning, based in part on the number of active viewers. Unexpected positive feedback loops also developed, leading to significant divergence from intended allocations.

Lottery scheduling enables the desired control at the operating-system level, eliminating the need for mutually trusting or well-behaved applications. Figure 8 depicts the execution of three mpeg_play video viewers (A, B, and C) displaying the same music video. Tickets were initially allocated to achieve relative display rates of A:B:C = 3:2:1, and were then changed to 3:1:2 at the time indicated by the arrow. The observed per-second frame rates were initially 2.03:1.59:1.06 (1.92:1.50:1 ratio), and then 2.02:1.05:1.61 (1.92:1:1.53 ratio) after the change.

Unfortunately, these results were distorted by the round-robin processing of client requests by the single-threaded X11R5 server. When run with the -no_display option, frame rates such as 6.83:4.56:2.23 (3.06:2.04:1 ratio) were typical.

## 5.5 Load Insulation

Support for multiple ticket currencies facilitates modular resource management. A currency defines a resource management abstraction barrier that locally contains intra-currency fluctuations such as inflation. The currency abstraction can be used to flexibly isolate or group users, tasks, and threads.

Figure 9 plots the progress of five tasks executing the Dhrystone benchmark. Let amount.currency denote a ticket allocation of amount denominated in currency. Currencies A and B have identical funding. Tasks A1 and A2 have allocations of 100.A and 200.A, respectively. Tasks B1 and B2 have allocations of 100.B and 200.B, respectively. Halfway through the experiment, a new task, B3, is started with an allocation of 300.B. Although this inflates the total number of tickets denominated in currency B from 300 to 600, there is no effect on tasks in currency A. The aggregate iteration ratio of A tasks to B tasks is 1.01:1 before B3 is started, and 1.00:1 after B3 is started. The slopes for the individual tasks indicate that A1 and A2 are not affected by task B3, while B1 and B2 are slowed to approximately half their original rates, corresponding to the factor of two inflation caused by B3.

## 5.6 System Overhead

The core lottery scheduling mechanism is extremely lightweight; a tree-based lottery need only generate a random number and perform $\lg n$ additions and comparisons to select a winner among $n$ clients. Thus, low-overhead lottery scheduling is possible in systems with a scheduling granularity as small as a thousand RISC instructions.

Our prototype scheduler, which includes full support for currencies, has not been optimized. To assess system overhead, we used the same executables and workloads under both our kernel and the unmodified Mach kernel; three separate runs were performed for each experiment. Overall, we found that the overhead imposed by our prototype lottery scheduler is comparable to that of the standard Mach timesharing policy. Since numerous optimizations could be made to our list-based lottery, simple currency conversion scheme, and other untuned aspects of our implementation, efficient lottery scheduling does not pose any challenging problems.

Our first experiment consisted of three Dhrystone benchmark tasks running concurrently for 200 seconds. Compared to unmodified Mach, 2.7% fewer iterations were executed under lottery scheduling. For the same experiment with eight tasks, lottery scheduling was observed to be 0.8% slower. However, the standard deviations across individual runs for unmodified Mach were comparable to the absolute differences observed between the kernels. Thus, the measured differences are not very significant.

We also ran a performance test using the multithreaded database server described in Section 5.3. Five client tasks each performed 20 queries, and the time between the start of the first query and the completion of the last query was measured. We found that this application executed 1.7% faster under lottery scheduling. For unmodified Mach, the average run time was 1155.5 seconds; with lottery scheduling, the average time was 1135.5 seconds. The standard deviations across runs for this experiment were less than 0.1% of the averages, indicating that the small measured differences are significant.

---

### النسخة العربية

من أجل تقييم نموذجنا الأولي للمجدول اليانصيبي، أجرينا تجارب مصممة لقياس قدرته على التحكم بمرونة وسرعة استجابة وكفاءة في معدلات التنفيذ النسبية للحسابات. تشمل التطبيقات المستخدمة في تجاربنا معيار Dhrystone المقيد بالحوسبة، وبرنامج تكامل عددي مونت كارلو، وتطبيق عميل-خادم متعدد الخيوط للبحث في النصوص، وعارضي فيديو MPEG المتنافسين.

## 5.1 العدالة

قاست تجربتنا الأولى الدقة التي يمكن بها لمجدولنا اليانصيبي التحكم في معدلات التنفيذ النسبية للحسابات. تشير كل نقطة مرسومة في الشكل 4 إلى معدل التنفيذ النسبي الذي لوحظ لمهمتين تنفذان معيار Dhrystone [Wei84] لمدة ستين ثانية مع تخصيص تذاكر نسبي معين. تم تنفيذ ثلاث عمليات تشغيل لكل نسبة صحيحة بين واحد وعشرة.

باستثناء عملية التشغيل التي أدى فيها التخصيص 10:1 إلى نسبة متوسطة 13.42:1، فإن جميع النسب الملاحظة قريبة من تخصيصاتها المقابلة. كما هو متوقع، التباين أكبر للنسب الأكبر. ومع ذلك، حتى النسب الكبيرة تتقارب نحو قيمها المخصصة على فترات زمنية أطول. على سبيل المثال، كانت النسبة الملاحظة بمتوسط على مدى فترة ثلاث دقائق لتخصيص 20:1 هي 19.08:1.

على الرغم من أن النتائج المقدمة في الشكل 4 تشير إلى أن المجدول يمكنه التحكم بنجاح في معدلات الحسابات، يجب علينا أيضاً فحص سلوكه على فترات زمنية أقصر. يرسم الشكل 5 متوسطات أعداد التكرارات على سلسلة من نوافذ زمنية مدتها 8 ثوانٍ أثناء تنفيذ واحد مدته 200 ثانية مع تخصيص 2:1. على الرغم من وجود بعض التباين بوضوح، تظل المهمتان قريبتين من نسبهما المخصصة طوال التجربة. لاحظ أنه إذا تم استخدام كم جدولة بمقدار 10 ميليثانية بدلاً من كم ماخ البالغ 100 ميليثانية، فسيتم ملاحظة نفس درجة العدالة على سلسلة من نوافذ زمنية أقل من ثانية.

## 5.2 التحكم المرن

يتضمن استخدام أكثر إثارة للجدولة اليانصيبية تضخم التذاكر المتحكم فيه ديناميكياً. تطبيق عملي يستفيد من هذا التحكم هو خوارزمية مونت كارلو [Pre88]. مونت كارلو هي خوارزمية احتمالية تُستخدم على نطاق واسع في العلوم الفيزيائية لحساب الخصائص المتوسطة للأنظمة. نظراً لأن الأخطاء في المتوسط المحسوب تتناسب مع $1/\sqrt{n}$، حيث $n$ هو عدد المحاولات، فإن النتائج الدقيقة تتطلب عدداً كبيراً من المحاولات.

غالباً ما ينفذ العلماء عدة تجارب مونت كارلو منفصلة لاستكشاف فرضيات مختلفة. غالباً ما يكون من المرغوب فيه الحصول على نتائج تقريبية بسرعة كلما بدأت تجربة جديدة، مع السماح للتجارب الأقدم بالاستمرار في تقليل خطأها بمعدل أبطأ [Hog88]. سيكون هذا الهدف مستحيلاً مع المجدولات التقليدية، ولكن يمكن تحقيقه بسهولة في نظامنا عن طريق تعديل قيمة تذكرة التجربة ديناميكياً كدالة لخطأها النسبي الحالي. هذا يسمح لتجربة جديدة ذات خطأ عالٍ باللحاق بسرعة بالتجارب الأقدم عن طريق التنفيذ بمعدل يبدأ عالياً ولكنه يتناقص بعد ذلك مع اقتراب خطأها النسبي من خطأ نظيراتها الأقدم.

يرسم الشكل 6 إجمالي عدد المحاولات المحسوبة بواسطة كل من ثلاث مهام مونت كارلو متداخلة. تستند كل مهمة إلى الكود النموذجي المقدم في [Pre88]، ويُخصص لها حصة من الوقت متناسبة مع مربع خطأها النسبي. عندما تبدأ مهمة جديدة، تتلقى في البداية حصة كبيرة من المعالج. تتناقص هذه الحصة عندما تقلل المهمة خطأها إلى قيمة أقرب إلى قيمة المهام الأخرى التي يتم تنفيذها.

قد يكون شكل مماثل من التحكم الديناميكي مفيداً أيضاً في البرامج المكثفة للرسومات. على سبيل المثال، يمكن منح عملية تقديم حصة كبيرة من موارد المعالجة حتى تعرض مخططاً خشناً أو إطاراً سلكياً، ثم إعطاؤها حصة أصغر من الموارد لحساب صورة أكثر صقلاً.

## 5.3 حسابات العميل-الخادم

كما ذُكر في القسم 4.6، تم تعديل بدائية IPC لماخ mach_msg لنقل التذاكر مؤقتاً من العميل إلى الخادم في استدعاءات الإجراءات البعيدة المتزامنة. وبالتالي، يعيد العميل توجيه حقوق موارده تلقائياً إلى الخادم الذي يحسب نيابة عنه. ستعالج الخوادم متعددة الخيوط الطلبات من عملاء مختلفين بالمعدلات المحددة بواسطة تخصيصات تذاكرهم المعنية.

طورنا تطبيق عميل-خادم بسيطاً متعدد الخيوط يشترك في خصائص مع قواعد البيانات الحقيقية وأنظمة استرجاع المعلومات. يقوم خادمنا في البداية بتحميل ملف نصي "قاعدة بيانات" بحجم 4.6 ميجابايت يحتوي على النص الكامل لجميع مسرحيات ويليام شكسبير. ثم يتفرع إلى عدة خيوط عاملة لمعالجة الاستعلامات الواردة من العملاء. عملية استعلام واحدة يدعمها الخادم هي بحث سلسلة فرعية غير حساسة لحالة الأحرف على قاعدة البيانات بأكملها، والتي تُرجع عدد المطابقات التي تم العثور عليها.

يقدم الشكل 7 نتائج تنفيذ ثلاثة عملاء قاعدة بيانات مع تخصيص تذاكر 8:3:1. لا يمتلك الخادم تذاكر خاصة به، ويعتمد بالكامل على التذاكر المنقولة من العملاء. يرسل كل عميل بشكل متكرر طلبات إلى الخادم لعد حدوث نفس سلسلة البحث. يُصدر العميل ذو الأولوية العالية إجمالي 20 استعلاماً ثم ينتهي. يستمر العميلان الآخران في إصدار استعلامات طوال مدة التجربة بأكملها.

تؤثر تخصيصات التذاكر على كل من وقت الاستجابة والإنتاجية. عندما أكمل العميل ذو الأولوية العالية طلباته العشرين، أكمل العميلان الآخران إجمالي 10 طلبات، مطابقين لتخصيصهم الإجمالي 8:4. على مدار التجربة بأكملها، أكمل العميلان بتخصيص تذاكر 3:1 38 و 13 استعلاماً على التوالي، مما يطابق تخصيصهما بشكل وثيق، على الرغم من منافستهما العابرة مع العميل ذي الأولوية العالية. بينما يكون العميل ذو الأولوية العالية نشطاً، فإن متوسطات أوقات الاستجابة التي يراها العملاء هي 17.19 و 43.19 و 132.20 ثانية، مما ينتج عنه سرعات نسبية 7.69:2.51:1. بعد إنهاء العميل ذي الأولوية العالية، تكون أوقات الاستجابة 44.17 و 15.18 ثانية، بنسبة 2.91:1. لجميع متوسطات أوقات الاستجابة، الانحراف المعياري أقل من 7٪ من المتوسط.

يمكن استخدام شكل مماثل من التحكم بواسطة تطبيقات قاعدة البيانات أو معالجة المعاملات لإدارة أوقات الاستجابة التي يراها العملاء أو المعاملات المتنافسة. سيكون هذا مفيداً في توفير مستويات مختلفة من الخدمة للعملاء أو المعاملات ذات الأهمية المتفاوتة (أو التمويل النقدي الحقيقي).

## 5.4 تطبيقات الوسائط المتعددة

تُعد التطبيقات القائمة على الوسائط مجالاً آخر يمكن أن يستفيد من الجدولة اليانصيبية. وصف كومبتون وتينينهاوس الحاجة إلى التحكم في جودة الخدمة عند عرض عارضي فيديو أو أكثر — مستوى من التحكم لا توفره أنظمة التشغيل الحالية [Com94]. حاولوا، بنجاح متباين، التحكم في معدلات عرض الفيديو على مستوى التطبيق بين مجموعة من العارضين الموثوقين المتبادلين. استخدم العارضون المتعاونون آليات التغذية الراجعة لتعديل معدلات إطاراتهم النسبية. استلزمت المقاييس غير الكافية وغير المستقرة لحمل النظام ضبطاً كبيراً، استناداً جزئياً إلى عدد العارضين النشطين. تطورت أيضاً حلقات تغذية راجعة إيجابية غير متوقعة، مما أدى إلى اختلاف كبير عن التخصيصات المقصودة.

تمكن الجدولة اليانصيبية من التحكم المطلوب على مستوى نظام التشغيل، مما يلغي الحاجة إلى تطبيقات موثوقة متبادلة أو حسنة السلوك. يصور الشكل 8 تنفيذ ثلاثة عارضي فيديو mpeg_play (A و B و C) يعرضون نفس فيديو الموسيقى. تم تخصيص التذاكر في البداية لتحقيق معدلات عرض نسبية A:B:C = 3:2:1، ثم تم تغييرها إلى 3:1:2 في الوقت المشار إليه بالسهم. كانت معدلات الإطارات لكل ثانية الملاحظة في البداية 2.03:1.59:1.06 (نسبة 1.92:1.50:1)، ثم 2.02:1.05:1.61 (نسبة 1.92:1:1.53) بعد التغيير.

لسوء الحظ، تشوهت هذه النتائج بسبب معالجة دائرية (round-robin) لطلبات العملاء بواسطة خادم X11R5 أحادي الخيط. عند التشغيل مع الخيار -no_display، كانت معدلات الإطارات مثل 6.83:4.56:2.23 (نسبة 3.06:2.04:1) نموذجية.

## 5.5 عزل الحمل

يسهل الدعم لعملات تذاكر متعددة الإدارة النمطية للموارد. تُحدد العملة حاجز تجريد إدارة الموارد الذي يحتوي محلياً على التقلبات داخل العملة مثل التضخم. يمكن استخدام تجريد العملة لعزل أو تجميع المستخدمين والمهام والخيوط بمرونة.

يرسم الشكل 9 تقدم خمس مهام تنفذ معيار Dhrystone. لنفترض أن amount.currency تشير إلى تخصيص تذاكر amount مسمى بـ currency. العملتان A و B لديهما تمويل متطابق. المهمتان A1 و A2 لديهما تخصيصات 100.A و 200.A على التوالي. المهمتان B1 و B2 لديهما تخصيصات 100.B و 200.B على التوالي. في منتصف التجربة، يتم بدء مهمة جديدة، B3، مع تخصيص 300.B. على الرغم من أن هذا يضخم إجمالي عدد التذاكر المسماة بالعملة B من 300 إلى 600، لا يوجد تأثير على المهام في العملة A. نسبة التكرار الإجمالية لمهام A إلى مهام B هي 1.01:1 قبل بدء B3، و 1.00:1 بعد بدء B3. تشير الميول للمهام الفردية إلى أن A1 و A2 لا تتأثران بالمهمة B3، بينما تتباطأ B1 و B2 إلى حوالي نصف معدلاتهما الأصلية، مطابقة لعامل التضخم اثنين الناجم عن B3.

## 5.6 التكلفة الإضافية للنظام

آلية الجدولة اليانصيبية الأساسية خفيفة الوزن للغاية؛ يحتاج يانصيب قائم على شجرة فقط إلى توليد عدد عشوائي وإجراء $\lg n$ عمليات جمع ومقارنات لاختيار فائز بين $n$ من العملاء. وبالتالي، فإن الجدولة اليانصيبية منخفضة التكلفة الإضافية ممكنة في الأنظمة ذات دقة جدولة صغيرة تصل إلى ألف تعليمة RISC.

لم يتم تحسين مجدولنا النموذجي الأولي، الذي يتضمن دعماً كاملاً للعملات. لتقييم التكلفة الإضافية للنظام، استخدمنا نفس الملفات التنفيذية وأحمال العمل تحت كل من نواتنا ونواة ماخ غير المعدلة؛ تم إجراء ثلاث عمليات تشغيل منفصلة لكل تجربة. بشكل عام، وجدنا أن التكلفة الإضافية التي يفرضها نموذجنا الأولي للمجدول اليانصيبي مماثلة لتلك الخاصة بسياسة المشاركة الزمنية القياسية لماخ. نظراً لأنه يمكن إجراء تحسينات عديدة على يانصيبنا القائم على القائمة، ومخطط تحويل العملات البسيط، والجوانب الأخرى غير المُحسنة لتطبيقنا، فإن الجدولة اليانصيبية الفعالة لا تطرح أي مشاكل صعبة.

تألفت تجربتنا الأولى من ثلاث مهام معيار Dhrystone تعمل بشكل متزامن لمدة 200 ثانية. مقارنة بماخ غير المعدل، تم تنفيذ 2.7٪ أقل من التكرارات تحت الجدولة اليانصيبية. لنفس التجربة مع ثماني مهام، لوحظ أن الجدولة اليانصيبية أبطأ بنسبة 0.8٪. ومع ذلك، كانت الانحرافات المعيارية عبر عمليات التشغيل الفردية لماخ غير المعدل مماثلة للاختلافات المطلقة الملاحظة بين النوى. وبالتالي، فإن الاختلافات المقاسة ليست مهمة جداً.

أجرينا أيضاً اختبار أداء باستخدام خادم قاعدة البيانات متعدد الخيوط الموصوف في القسم 5.3. نفذت خمس مهام عميل كل منها 20 استعلاماً، وتم قياس الوقت بين بداية الاستعلام الأول واكتمال الاستعلام الأخير. وجدنا أن هذا التطبيق نُفذ بشكل أسرع بنسبة 1.7٪ تحت الجدولة اليانصيبية. بالنسبة لماخ غير المعدل، كان متوسط وقت التشغيل 1155.5 ثانية؛ مع الجدولة اليانصيبية، كان متوسط الوقت 1135.5 ثانية. كانت الانحرافات المعيارية عبر عمليات التشغيل لهذه التجربة أقل من 0.1٪ من المتوسطات، مما يشير إلى أن الاختلافات الصغيرة المقاسة مهمة.

---

### Translation Notes

- **Figures referenced:** Figure 4 (Relative Rate Accuracy), Figure 5 (Fairness Over Time), Figure 6 (Monte-Carlo Execution Rates), Figure 7 (Query Processing Rates), Figure 8 (Controlling Video Rates), Figure 9 (Currencies Insulate Loads)
- **Key terms introduced:**
  - Dhrystone benchmark: معيار Dhrystone
  - Monte-Carlo: مونت كارلو
  - MPEG viewer: عارض MPEG
  - round-robin: دائرية
  - overhead: تكلفة إضافية
- **Equations:** $1/\sqrt{n}$, $\lg n$
- **Citations:** [Wei84], [Pre88], [Hog88], [Com94]
- **Special handling:** Experimental results and numerical data preserved precisely

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
