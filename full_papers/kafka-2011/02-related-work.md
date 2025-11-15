# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** messaging systems, delivery guarantees, throughput, distributed, push model, pull model

---

### English Version

Traditional enterprise messaging systems [1][7][15][17] have existed for a long time and often play a critical role as an event bus for processing asynchronous data flows. However, there are a few reasons why they tend not to be a good fit for log processing. First, there is a mismatch in features offered by enterprise systems. Those systems often focus on offering a rich set of delivery guarantees. For example, IBM Websphere MQ [7] has transactional supports that allow an application to insert messages into multiple queues atomically. The JMS [14] specification allows each individual message to be acknowledged after consumption, potentially out of order. Such delivery guarantees are often overkill for collecting log data. For instance, losing a few pageview events occasionally is certainly not the end of the world. Those unneeded features tend to increase the complexity of both the API and the underlying implementation of those systems. Second, many systems do not focus as strongly on throughput as their primary design constraint. For example, JMS has no API to allow the producer to explicitly batch multiple messages into a single request. This means each message requires a full TCP/IP roundtrip, which is not feasible for the throughput requirements of our domain. Third, those systems are weak in distributed support. There is no easy way to partition and store messages on multiple machines. Finally, many messaging systems assume near immediate consumption of messages, so the queue of unconsumed messages is always fairly small. Their performance degrades significantly if messages are allowed to accumulate, as is the case for offline consumers such as data warehousing applications that do periodic large loads rather than continuous consumption.

A number of specialized log aggregators have been built over the last few years. Facebook uses a system called Scribe. Each front-end machine can send log data to a set of Scribe machines over sockets. Each Scribe machine aggregates the log entries and periodically dumps them to HDFS [9] or an NFS device. Yahoo's data highway project has a similar dataflow. A set of machines aggregate events from the clients and roll out "minute" files, which are then added to HDFS. Flume is a relatively new log aggregator developed by Cloudera. It supports extensible "pipes" and "sinks", and makes streaming log data very flexible. It also has more integrated distributed support. However, most of those systems are built for consuming the log data offline, and often expose implementation details unnecessarily (e.g. "minute files") to the consumer. Additionally, most of them use a "push" model in which the broker forwards data to consumers. At LinkedIn, we find the "pull" model more suitable for our applications since each consumer can retrieve the messages at the maximum rate it can sustain and avoid being flooded by messages pushed faster than it can handle. The pull model also makes it easy to rewind a consumer and we discuss this benefit at the end of Section 3.2.

More recently, Yahoo! Research developed a new distributed pub/sub system called HedWig [13]. HedWig is highly scalable and available, and offers strong durability guarantees. However, it is mainly intended for storing the commit log of a data store.

---

### النسخة العربية

وُجدت أنظمة المراسلة المؤسسية التقليدية [1][7][15][17] منذ زمن طويل وغالباً ما تلعب دوراً حاسماً كناقل أحداث لمعالجة تدفقات البيانات اللامتزامنة. ومع ذلك، هناك بعض الأسباب التي تجعلها غير مناسبة لمعالجة السجلات. أولاً، هناك عدم تطابق في الميزات التي تقدمها الأنظمة المؤسسية. غالباً ما تركز هذه الأنظمة على تقديم مجموعة غنية من ضمانات التوصيل. على سبيل المثال، يحتوي IBM Websphere MQ [7] على دعم للمعاملات يسمح لتطبيق بإدراج رسائل في طوابير متعددة بشكل ذري. تسمح مواصفات JMS [14] بالإقرار بكل رسالة فردية بعد الاستهلاك، وربما بشكل غير مرتب. غالباً ما تكون ضمانات التوصيل هذه مبالغاً فيها لجمع بيانات السجلات. على سبيل المثال، فقدان بعض أحداث مشاهدة الصفحات من حين لآخر ليس بالتأكيد نهاية العالم. تميل هذه الميزات غير الضرورية إلى زيادة تعقيد كل من واجهة برمجة التطبيقات والتنفيذ الأساسي لتلك الأنظمة. ثانياً، العديد من الأنظمة لا تركز بقوة على الإنتاجية كقيد تصميمي أساسي. على سبيل المثال، لا يحتوي JMS على واجهة برمجة تطبيقات تسمح للمنتج بتجميع رسائل متعددة بشكل صريح في طلب واحد. هذا يعني أن كل رسالة تتطلب رحلة ذهاب وإياب كاملة عبر TCP/IP، وهو ما ليس ممكناً لمتطلبات الإنتاجية في مجالنا. ثالثاً، هذه الأنظمة ضعيفة في الدعم الموزع. لا توجد طريقة سهلة لتجزئة وتخزين الرسائل على أجهزة متعددة. أخيراً، تفترض العديد من أنظمة المراسلة الاستهلاك شبه الفوري للرسائل، لذا فإن طابور الرسائل غير المستهلكة يكون دائماً صغيراً نسبياً. ينخفض أداؤها بشكل كبير إذا سُمح للرسائل بالتراكم، كما هو الحال مع المستهلكين غير المتصلين مثل تطبيقات مستودعات البيانات التي تقوم بعمليات تحميل كبيرة دورية بدلاً من الاستهلاك المستمر.

تم بناء عدد من مجمّعات السجلات المتخصصة خلال السنوات القليلة الماضية. يستخدم فيسبوك نظاماً يُسمى Scribe. يمكن لكل جهاز واجهة أمامية إرسال بيانات السجلات إلى مجموعة من أجهزة Scribe عبر المقابس. يجمع كل جهاز Scribe إدخالات السجل ويفرغها بشكل دوري في HDFS [9] أو جهاز NFS. يحتوي مشروع Data Highway من ياهو على تدفق بيانات مماثل. تجمع مجموعة من الأجهزة الأحداث من العملاء وتنشئ ملفات "الدقيقة"، والتي تُضاف بعد ذلك إلى HDFS. يُعد Flume مجمّع سجلات جديد نسبياً طورته Cloudera. يدعم "الأنابيب" و"المصارف" القابلة للتوسيع، ويجعل بث بيانات السجل مرناً للغاية. كما أن لديه دعماً موزعاً أكثر تكاملاً. ومع ذلك، معظم هذه الأنظمة مبنية لاستهلاك بيانات السجل غير متصل، وغالباً ما تكشف تفاصيل التنفيذ بشكل غير ضروري (مثل ملفات "الدقيقة") للمستهلك. بالإضافة إلى ذلك، يستخدم معظمها نموذج "الدفع" الذي يُرسل فيه الوسيط البيانات إلى المستهلكين. في لينكد إن، نجد نموذج "السحب" أكثر ملاءمة لتطبيقاتنا حيث يمكن لكل مستهلك استرجاع الرسائل بأقصى معدل يمكنه تحمله وتجنب الغمر بالرسائل المدفوعة أسرع مما يمكنه التعامل معه. كما يسهل نموذج السحب إرجاع المستهلك إلى الوراء ونناقش هذه الفائدة في نهاية القسم 3.2.

في الآونة الأخيرة، طورت Yahoo! Research نظام نشر/اشتراك موزع جديد يُسمى HedWig [13]. يتمتع HedWig بقابلية عالية للتوسع والتوافر، ويوفر ضمانات متانة قوية. ومع ذلك، فهو مخصص بشكل أساسي لتخزين سجل الالتزام لمخزن البيانات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Enterprise messaging systems: أنظمة المراسلة المؤسسية
  - Event bus: ناقل أحداث
  - Asynchronous data flows: تدفقات البيانات اللامتزامنة
  - Delivery guarantees: ضمانات التوصيل
  - Transactional support: دعم المعاملات
  - Atomically: بشكل ذري
  - JMS (Java Message Service): JMS (kept as acronym)
  - Acknowledged: الإقرار
  - Batching: تجميع
  - TCP/IP roundtrip: رحلة ذهاب وإياب عبر TCP/IP
  - Push model: نموذج الدفع
  - Pull model: نموذج السحب
  - Pub/sub: نشر/اشتراك
  - Durability: متانة
  - Commit log: سجل الالتزام

- **Citations:** [1], [7], [9], [13], [14], [15], [17]

- **Special handling:**
  - System/product names (IBM Websphere MQ, JMS, Scribe, Data Highway, Flume, HDFS, NFS, HedWig) kept in original form
  - "minute files" kept with quotes and translated as ملفات "الدقيقة" to preserve the technical meaning
  - Company names kept in original form

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
