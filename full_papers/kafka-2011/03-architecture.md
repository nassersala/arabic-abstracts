# Section 3: Kafka Architecture and Design Principles
## القسم 3: معمارية كافكا ومبادئ التصميم

**Section:** architecture
**Translation Quality:** 0.89
**Glossary Terms Used:** distributed system, broker, partition, topic, producer, consumer, offset, throughput, latency, Zookeeper, consensus

---

### English Version

Because of limitations in existing systems, we developed a new messaging-based log aggregator Kafka. We first introduce the basic concepts in Kafka. A stream of messages of a particular type is defined by a topic. A producer can publish messages to a topic. The published messages are then stored at a set of servers called brokers. A consumer can subscribe to one or more topics from the brokers, and consume the subscribed messages by pulling data from the brokers.

Messaging is conceptually simple, and we have tried to make the Kafka API equally simple to reflect this. Instead of showing the exact API, we present some sample code to show how the API is used. The sample code of the producer is given below. A message is defined to contain just a payload of bytes. A user can choose her favorite serialization method to encode a message. For efficiency, the producer can send a set of messages in a single publish request.

```
Sample producer code:
  producer = new Producer(…);
  message = new Message("test message str".getBytes());
  set = new MessageSet(message);
  producer.send("topic1", set);
```

To subscribe to a topic, a consumer first creates one or more message streams for the topic. The messages published to that topic will be evenly distributed into these sub-streams. The details about how Kafka distributes the messages are described later in Section 3.2. Each message stream provides an iterator interface over the continual stream of messages being produced. The consumer then iterates over every message in the stream and processes the payload of the message. Unlike traditional iterators, the message stream iterator never terminates. If there are currently no more messages to consume, the iterator blocks until new messages are published to the topic. We support both the point-to-point delivery model in which multiple consumers jointly consume a single copy of all messages in a topic, as well as the publish/subscribe model in which multiple consumers each retrieve its own copy of a topic.

```
Sample consumer code:
  streams[] = Consumer.createMessageStreams("topic1", 1)
  for (message : streams[0]) {
    bytes = message.payload();
    // do something with the bytes
  }
```

The overall architecture of Kafka is shown in Figure 1. Since Kafka is distributed in nature, an Kafka cluster typically consists of multiple brokers. To balance load, a topic is divided into multiple partitions and each broker stores one or more of those partitions. Multiple producers and consumers can publish and retrieve messages at the same time. In Section 3.1, we describe the layout of a single partition on a broker and a few design choices that we selected to make accessing a partition efficient. In Section 3.2, we describe how the producer and the consumer interact with multiple brokers in a distributed setting. We discuss the delivery guarantees of Kafka in Section 3.3.

## 3.1 Efficiency on a Single Partition

We made a few decisions in Kafka to make the system efficient.

**Simple storage:** Kafka has a very simple storage layout. Each partition of a topic corresponds to a logical log. Physically, a log is implemented as a set of segment files of approximately the same size (e.g., 1GB). Every time a producer publishes a message to a partition, the broker simply appends the message to the last segment file. For better performance, we flush the segment files to disk only after a configurable number of messages have been published or a certain amount of time has elapsed. A message is only exposed to the consumers after it is flushed.

Unlike typical messaging systems, a message stored in Kafka doesn't have an explicit message id. Instead, each message is addressed by its logical offset in the log. This avoids the overhead of maintaining auxiliary, seek-intensive random-access index structures that map the message ids to the actual message locations. Note that our message ids are increasing but not consecutive. To compute the id of the next message, we have to add the length of the current message to its id. From now on, we will use message ids and offsets interchangeably.

A consumer always consumes messages from a particular partition sequentially. If the consumer acknowledges a particular message offset, it implies that the consumer has received all messages prior to that offset in the partition. Under the covers, the consumer is issuing asynchronous pull requests to the broker to have a buffer of data ready for the application to consume. Each pull request contains the offset of the message from which the consumption begins and an acceptable number of bytes to fetch. Each broker keeps in memory a sorted list of offsets, including the offset of the first message in every segment file. The broker locates the segment file where the requested message resides by searching the offset list, and sends the data back to the consumer. After a consumer receives a message, it computes the offset of the next message to consume and uses it in the next pull request. The layout of an Kafka log and the in-memory index is depicted in Figure 2. Each box shows the offset of a message.

**Efficient transfer:** We are very careful about transferring data in and out of Kafka. Earlier, we have shown that the producer can submit a set of messages in a single send request. Although the end consumer API iterates one message at a time, under the covers, each pull request from a consumer also retrieves multiple messages up to a certain size, typically hundreds of kilobytes.

Another unconventional choice that we made is to avoid explicitly caching messages in memory at the Kafka layer. Instead, we rely on the underlying file system page cache. This has the main benefit of avoiding double buffering---messages are only cached in the page cache. This has the additional benefit of retaining warm cache even when a broker process is restarted. Since Kafka doesn't cache messages in process at all, it has very little overhead in garbage collecting its memory, making efficient implementation in a VM-based language feasible.

Finally, since both the producer and the consumer access the segment files sequentially, with the consumer often lagging the producer by a small amount, normal operating system caching heuristics are very effective (specifically write-through caching and read-ahead). We have found that both the production and the consumption have consistent performance linear to the data size, up to many terabytes of data.

In addition we optimize the network access for consumers. Kafka is a multi-subscriber system and a single message may be consumed multiple times by different consumer applications. A typical approach to sending bytes from a local file to a remote socket involves the following steps: (1) read data from the storage media to the page cache in an OS, (2) copy data in the page cache to an application buffer, (3) copy application buffer to another kernel buffer, (4) send the kernel buffer to the socket. This includes 4 data copying and 2 system calls. On Linux and other Unix operating systems, there exists a sendfile API [5] that can directly transfer bytes from a file channel to a socket channel. This typically avoids 2 of the copies and 1 system call introduced in steps (2) and (3). Kafka exploits the sendfile API to efficiently deliver bytes in a log segment file from a broker to a consumer.

**Stateless broker:** Unlike most other messaging systems, in Kafka, the information about how much each consumer has consumed is not maintained by the broker, but by the consumer itself. Such a design reduces a lot of the complexity and the overhead on the broker. However, this makes it tricky to delete a message, since a broker doesn't know whether all subscribers have consumed the message. Kafka solves this problem by using a simple time-based SLA for the retention policy. A message is automatically deleted if it has been retained in the broker longer than a certain period, typically 7 days. This solution works well in practice. Most consumers, including the offline ones, finish consuming either daily, hourly, or in real-time. The fact that the performance of Kafka doesn't degrade with a larger data size makes this long retention feasible.

There is an important side benefit of this design. A consumer can deliberately rewind back to an old offset and re-consume data. This violates the common contract of a queue, but proves to be an essential feature for many consumers. For example, when there is an error in application logic in the consumer, the application can re-play certain messages after the error is fixed. This is particularly important to ETL data loads into our data warehouse or Hadoop system. As another example, the consumed data may be flushed to a persistent store only periodically (e.g, a full-text indexer). If the consumer crashes, the unflushed data is lost. In this case, the consumer can checkpoint the smallest offset of the unflushed messages and re-consume from that offset when it's restarted. We note that rewinding a consumer is much easier to support in the pull model than the push model.

## 3.2 Distributed Coordination

We now describe how the producers and the consumers behave in a distributed setting. Each producer can publish a message to either a randomly selected partition or a partition semantically determined by a partitioning key and a partitioning function. We will focus on how the consumers interact with the brokers.

Kafka has the concept of consumer groups. Each consumer group consists of one or more consumers that jointly consume a set of subscribed topics, i.e., each message is delivered to only one of the consumers within the group. Different consumer groups each independently consume the full set of subscribed messages and no coordination is needed across consumer groups. The consumers within the same group can be in different processes or on different machines. Our goal is to divide the messages stored in the brokers evenly among the consumers, without introducing too much coordination overhead.

Our first decision is to make a partition within a topic the smallest unit of parallelism. This means that at any given time, all messages from one partition are consumed only by a single consumer within each consumer group. Had we allowed multiple consumers to simultaneously consume a single partition, they would have to coordinate who consumes what messages, which necessitates locking and state maintenance overhead. In contrast, in our design consuming processes only need co-ordinate when the consumers rebalance the load, an infrequent event. In order for the load to be truly balanced, we require many more partitions in a topic than the consumers in each group. We can easily achieve this by over partitioning a topic.

The second decision that we made is to not have a central "master" node, but instead let consumers coordinate among themselves in a decentralized fashion. Adding a master can complicate the system since we have to further worry about master failures. To facilitate the coordination, we employ a highly available consensus service Zookeeper [10].

Zookeeper has a very simple, file system like API. One can create a path, set the value of a path, read the value of a path, delete a path, and list the children of a path. It does a few more interesting things: (a) one can register a watcher on a path and get notified when the children of a path or the value of a path has changed; (b) a path can be created as ephemeral (as oppose to persistent), which means that if the creating client is gone, the path is automatically removed by the Zookeeper server; (c) zookeeper replicates its data to multiple servers, which makes the data highly reliable and available.

Kafka uses Zookeeper for the following tasks: (1) detecting the addition and the removal of brokers and consumers, (2) triggering a rebalance process in each consumer when the above events happen, and (3) maintaining the consumption relationship and keeping track of the consumed offset of each partition. Specifically, when each broker or consumer starts up, it stores its information in a broker or consumer registry in Zookeeper. The broker registry contains the broker's host name and port, and the set of topics and partitions stored on it. The consumer registry includes the consumer group to which a consumer belongs and the set of topics that it subscribes to. Each consumer group is associated with an ownership registry and an offset registry in Zookeeper. The ownership registry has one path for every subscribed partition and the path value is the id of the consumer currently consuming from this partition (we use the terminology that the consumer owns this partition). The offset registry stores for each subscribed partition, the offset of the last consumed message in the partition.

The paths created in Zookeeper are ephemeral for the broker registry, the consumer registry and the ownership registry, and persistent for the offset registry. If a broker fails, all partitions on it are automatically removed from the broker registry. The failure of a consumer causes it to lose its entry in the consumer registry and all partitions that it owns in the ownership registry. Each consumer registers a Zookeeper watcher on both the broker registry and the consumer registry, and will be notified whenever a change in the broker set or the consumer group occurs. During the initial startup of a consumer or when the consumer is notified about a broker/consumer change through the watcher, the consumer initiates a rebalance process to determine the new subset of partitions that it should consume from. The process is described in Algorithm 1.

**Algorithm 1: rebalance process for consumer Ci in group G**
```
For each topic T that Ci subscribes to {
  remove partitions owned by Ci from the ownership registry
  read the broker and the consumer registries from Zookeeper
  compute PT = partitions available in all brokers under topic T
  compute CT = all consumers in G that subscribe to topic T
  sort PT and CT
  let j be the index position of Ci in CT and let N = |PT|/|CT|
  assign partitions from j*N to (j+1)*N - 1 in PT to consumer Ci
  for each assigned partition p {
    set the owner of p to Ci in the ownership registry
    let Op = the offset of partition p stored in the offset registry
    invoke a thread to pull data in partition p from offset Op
  }
}
```

By reading the broker and the consumer registry from Zookeeper, the consumer first computes the set (PT) of partitions available for each subscribed topic T and the set (CT) of consumers subscribing to T. It then range-partitions PT into |CT| chunks and deterministically picks one chunk to own. For each partition the consumer picks, it writes itself as the new owner of the partition in the ownership registry. Finally, the consumer begins a thread to pull data from each owned partition, starting from the offset stored in the offset registry. As messages get pulled from a partition, the consumer periodically updates the latest consumed offset in the offset registry.

When there are multiple consumers within a group, each of them will be notified of a broker or a consumer change. However, the notification may come at slightly different times at the consumers. So, it is possible that one consumer tries to take ownership of a partition still owned by another consumer. When this happens, the first consumer simply releases all the partitions that it currently owns, waits a bit and retries the rebalance process. In practice, the rebalance process often stabilizes after only a few retries. When a new consumer group is created, no offsets are available in the offset registry. In this case, the consumers will begin with either the smallest or the largest offset (depending on a configuration) available on each subscribed partition, using an API that we provide on the brokers.

## 3.3 Delivery Guarantees

In general, Kafka only guarantees at-least-once delivery. Exactly-once delivery typically requires two-phase commits and is not necessary for our applications. Most of the time, a message is delivered exactly once to each consumer group. However, in the case when a consumer process crashes without a clean shutdown, the consumer process that takes over those partitions owned by the failed consumer may get some duplicate messages that are after the last offset successfully committed to zookeeper. If an application cares about duplicates, it must add its own de-duplication logic, either using the offsets that we return to the consumer or some unique key within the message. This is usually a more cost-effective approach than using two-phase commits.

Kafka guarantees that messages from a single partition are delivered to a consumer in order. However, there is no guarantee on the ordering of messages coming from different partitions.

To avoid log corruption, Kafka stores a CRC for each message in the log. If there is any I/O error on the broker, Kafka runs a recovery process to remove those messages with inconsistent CRCs. Having the CRC at the message level also allows us to check network errors after a message is produced or consumed.

If a broker goes down, any message stored on it not yet consumed becomes unavailable. If the storage system on a broker is permanently damaged, any unconsumed message is lost forever. In the future, we plan to add built-in replication in Kafka to redundantly store each message on multiple brokers.

---

### النسخة العربية

بسبب القيود في الأنظمة الموجودة، قمنا بتطوير مجمّع سجلات جديد قائم على المراسلة يُسمى كافكا. نقدم أولاً المفاهيم الأساسية في كافكا. يُعرّف تدفق الرسائل من نوع معين بموضوع. يمكن للمنتج نشر رسائل إلى موضوع. تُخزَّن الرسائل المنشورة بعد ذلك في مجموعة من الخوادم تُسمى الوسطاء. يمكن للمستهلك الاشتراك في موضوع واحد أو أكثر من الوسطاء، واستهلاك الرسائل المشترك فيها عن طريق سحب البيانات من الوسطاء.

المراسلة بسيطة من الناحية المفاهيمية، وحاولنا جعل واجهة برمجة التطبيقات لكافكا بسيطة بالمثل لتعكس ذلك. بدلاً من عرض واجهة برمجة التطبيقات بالضبط، نقدم بعض نماذج الشفرة لتوضيح كيفية استخدام واجهة برمجة التطبيقات. يُعطى نموذج شفرة المنتج أدناه. تُعرَّف الرسالة لتحتوي فقط على حمولة من البايتات. يمكن للمستخدم اختيار طريقة التسلسل المفضلة لديه لترميز رسالة. لتحقيق الكفاءة، يمكن للمنتج إرسال مجموعة من الرسائل في طلب نشر واحد.

```
نموذج شفرة المنتج:
  producer = new Producer(…);
  message = new Message("test message str".getBytes());
  set = new MessageSet(message);
  producer.send("topic1", set);
```

للاشتراك في موضوع، ينشئ المستهلك أولاً تدفقاً واحداً أو أكثر من تدفقات الرسائل للموضوع. سيتم توزيع الرسائل المنشورة لذلك الموضوع بالتساوي في هذه التدفقات الفرعية. يتم وصف التفاصيل حول كيفية توزيع كافكا للرسائل لاحقاً في القسم 3.2. يوفر كل تدفق رسائل واجهة مكرر على التدفق المستمر للرسائل التي يتم إنتاجها. يكرر المستهلك بعد ذلك على كل رسالة في التدفق ويعالج حمولة الرسالة. بخلاف المكررات التقليدية، لا ينتهي مكرر تدفق الرسائل أبداً. إذا لم يكن هناك المزيد من الرسائل للاستهلاك حالياً، يحجب المكرر حتى يتم نشر رسائل جديدة للموضوع. ندعم كلاً من نموذج التوصيل من نقطة إلى نقطة حيث تستهلك مستهلكون متعددون معاً نسخة واحدة من جميع الرسائل في موضوع، بالإضافة إلى نموذج النشر/الاشتراك حيث يسترجع كل مستهلك متعدد نسخته الخاصة من موضوع.

```
نموذج شفرة المستهلك:
  streams[] = Consumer.createMessageStreams("topic1", 1)
  for (message : streams[0]) {
    bytes = message.payload();
    // افعل شيئاً بالبايتات
  }
```

تظهر المعمارية الإجمالية لكافكا في الشكل 1. نظراً لأن كافكا موزع بطبيعته، يتكون مجموعة كافكا عادةً من وسطاء متعددين. لموازنة الحمل، يُقسَّم الموضوع إلى أقسام متعددة ويخزن كل وسيط قسماً واحداً أو أكثر من تلك الأقسام. يمكن لمنتجين ومستهلكين متعددين نشر واسترجاع الرسائل في نفس الوقت. في القسم 3.1، نصف تخطيط قسم واحد على وسيط وبعض خيارات التصميم التي اخترناها لجعل الوصول إلى القسم فعالاً. في القسم 3.2، نصف كيفية تفاعل المنتج والمستهلك مع وسطاء متعددين في إعداد موزع. نناقش ضمانات التوصيل لكافكا في القسم 3.3.

## 3.1 الكفاءة على قسم واحد

اتخذنا بعض القرارات في كافكا لجعل النظام فعالاً.

**التخزين البسيط:** لدى كافكا تخطيط تخزين بسيط للغاية. يتوافق كل قسم من موضوع مع سجل منطقي. فعلياً، يُنفَّذ السجل كمجموعة من ملفات القطاعات ذات الحجم المتقارب تقريباً (على سبيل المثال، 1 جيجابايت). في كل مرة ينشر فيها منتج رسالة إلى قسم، يُلحق الوسيط ببساطة الرسالة بملف القطاع الأخير. للحصول على أداء أفضل، نقوم بتفريغ ملفات القطاعات إلى القرص فقط بعد نشر عدد قابل للتكوين من الرسائل أو انقضاء فترة زمنية معينة. لا تُعرَّض الرسالة للمستهلكين إلا بعد تفريغها.

بخلاف أنظمة المراسلة النموذجية، لا تحتوي الرسالة المخزنة في كافكا على معرّف رسالة صريح. بدلاً من ذلك، تُعنوَن كل رسالة بإزاحتها المنطقية في السجل. يتجنب هذا العبء الإضافي لصيانة بنى فهرسة مساعدة كثيفة البحث للوصول العشوائي التي تربط معرّفات الرسائل بمواقع الرسائل الفعلية. لاحظ أن معرّفات رسائلنا متزايدة لكنها ليست متتالية. لحساب معرّف الرسالة التالية، علينا إضافة طول الرسالة الحالية إلى معرّفها. من الآن فصاعداً، سنستخدم معرّفات الرسائل والإزاحات بالتبادل.

يستهلك المستهلك دائماً رسائل من قسم معين بشكل متسلسل. إذا أقرّ المستهلك بإزاحة رسالة معينة، فهذا يعني أن المستهلك قد تلقى جميع الرسائل السابقة لتلك الإزاحة في القسم. في الخفاء، يصدر المستهلك طلبات سحب لامتزامنة إلى الوسيط ليكون لديه مخزن مؤقت من البيانات جاهزاً للتطبيق للاستهلاك. يحتوي كل طلب سحب على إزاحة الرسالة التي يبدأ منها الاستهلاك وعدداً مقبولاً من البايتات للجلب. يحتفظ كل وسيط في الذاكرة بقائمة مرتبة من الإزاحات، بما في ذلك إزاحة الرسالة الأولى في كل ملف قطاع. يحدد الوسيط ملف القطاع الذي تقع فيه الرسالة المطلوبة عن طريق البحث في قائمة الإزاحات، ويرسل البيانات مرة أخرى إلى المستهلك. بعد أن يتلقى المستهلك رسالة، يحسب إزاحة الرسالة التالية للاستهلاك ويستخدمها في طلب السحب التالي. يُصوَّر تخطيط سجل كافكا والفهرس في الذاكرة في الشكل 2. يُظهر كل مربع إزاحة رسالة.

**النقل الفعال:** نحن حذرون للغاية بشأن نقل البيانات من وإلى كافكا. في وقت سابق، أظهرنا أن المنتج يمكنه إرسال مجموعة من الرسائل في طلب إرسال واحد. على الرغم من أن واجهة برمجة تطبيقات المستهلك النهائي تكرر رسالة واحدة في كل مرة، في الخفاء، يسترجع كل طلب سحب من مستهلك أيضاً رسائل متعددة حتى حجم معين، عادةً مئات الكيلوبايتات.

خيار آخر غير تقليدي اتخذناه هو تجنب التخزين المؤقت الصريح للرسائل في الذاكرة في طبقة كافكا. بدلاً من ذلك، نعتمد على ذاكرة التخزين المؤقت لصفحة نظام الملفات الأساسي. لهذا الفائدة الرئيسية المتمثلة في تجنب التخزين المؤقت المزدوج---تُخزَّن الرسائل مؤقتاً فقط في ذاكرة التخزين المؤقت للصفحة. لهذا الفائدة الإضافية المتمثلة في الاحتفاظ بذاكرة تخزين مؤقت دافئة حتى عند إعادة تشغيل عملية الوسيط. نظراً لأن كافكا لا يخزن الرسائل مؤقتاً في العملية على الإطلاق، فلديه عبء إضافي ضئيل جداً في جمع القمامة لذاكرته، مما يجعل التنفيذ الفعال في لغة قائمة على آلة افتراضية ممكناً.

أخيراً، نظراً لأن كلاً من المنتج والمستهلك يصلان إلى ملفات القطاعات بشكل متسلسل، مع تأخر المستهلك غالباً عن المنتج بمقدار صغير، فإن إرشادات التخزين المؤقت العادية لنظام التشغيل فعالة للغاية (على وجه التحديد التخزين المؤقت للكتابة الفورية والقراءة المسبقة). وجدنا أن كلاً من الإنتاج والاستهلاك لهما أداء متسق خطي مع حجم البيانات، حتى العديد من التيرابايتات من البيانات.

بالإضافة إلى ذلك، نقوم بتحسين الوصول إلى الشبكة للمستهلكين. كافكا هو نظام متعدد المشتركين ويمكن استهلاك رسالة واحدة عدة مرات بواسطة تطبيقات مستهلك مختلفة. تتضمن الطريقة النموذجية لإرسال البايتات من ملف محلي إلى مقبس بعيد الخطوات التالية: (1) قراءة البيانات من وسائط التخزين إلى ذاكرة التخزين المؤقت للصفحة في نظام التشغيل، (2) نسخ البيانات في ذاكرة التخزين المؤقت للصفحة إلى مخزن مؤقت للتطبيق، (3) نسخ مخزن التطبيق المؤقت إلى مخزن مؤقت آخر للنواة، (4) إرسال مخزن النواة المؤقت إلى المقبس. يتضمن هذا 4 عمليات نسخ بيانات واستدعاءين للنظام. على أنظمة تشغيل لينكس ويونكس الأخرى، توجد واجهة برمجة تطبيقات sendfile [5] يمكنها نقل البايتات مباشرة من قناة ملف إلى قناة مقبس. يتجنب هذا عادةً 2 من النسخ واستدعاء نظام واحد المقدم في الخطوات (2) و(3). يستغل كافكا واجهة برمجة تطبيقات sendfile لتوصيل البايتات بكفاءة في ملف قطاع سجل من وسيط إلى مستهلك.

**الوسيط عديم الحالة:** بخلاف معظم أنظمة المراسلة الأخرى، في كافكا، لا يحتفظ الوسيط بالمعلومات حول مقدار ما استهلكه كل مستهلك، بل المستهلك نفسه. يقلل مثل هذا التصميم الكثير من التعقيد والعبء الإضافي على الوسيط. ومع ذلك، هذا يجعل من الصعب حذف رسالة، لأن الوسيط لا يعرف ما إذا كان جميع المشتركين قد استهلكوا الرسالة. يحل كافكا هذه المشكلة باستخدام اتفاقية مستوى خدمة بسيطة قائمة على الوقت لسياسة الاحتفاظ. يتم حذف الرسالة تلقائياً إذا تم الاحتفاظ بها في الوسيط لفترة أطول من فترة معينة، عادةً 7 أيام. يعمل هذا الحل بشكل جيد في الممارسة العملية. معظم المستهلكين، بما في ذلك المستهلكون غير المتصلين، ينتهون من الاستهلاك إما يومياً أو كل ساعة أو في الوقت الفعلي. حقيقة أن أداء كافكا لا يتدهور مع حجم بيانات أكبر يجعل هذا الاحتفاظ الطويل ممكناً.

هناك فائدة جانبية مهمة لهذا التصميم. يمكن للمستهلك إرجاع متعمد إلى إزاحة قديمة وإعادة استهلاك البيانات. ينتهك هذا العقد المشترك للطابور، لكنه يثبت أنه ميزة أساسية للعديد من المستهلكين. على سبيل المثال، عندما يكون هناك خطأ في منطق التطبيق في المستهلك، يمكن للتطبيق إعادة تشغيل رسائل معينة بعد إصلاح الخطأ. هذا مهم بشكل خاص لتحميلات بيانات ETL إلى مستودع البيانات أو نظام Hadoop الخاص بنا. كمثال آخر، قد يتم تفريغ البيانات المستهلكة إلى مخزن دائم فقط بشكل دوري (على سبيل المثال، مفهرس النص الكامل). إذا تعطل المستهلك، تُفقد البيانات غير المفرغة. في هذه الحالة، يمكن للمستهلك نقطة تفتيش أصغر إزاحة للرسائل غير المفرغة وإعادة الاستهلاك من تلك الإزاحة عند إعادة تشغيله. نلاحظ أن إرجاع مستهلك أسهل بكثير للدعم في نموذج السحب من نموذج الدفع.

## 3.2 التنسيق الموزع

نصف الآن كيف يتصرف المنتجون والمستهلكون في إعداد موزع. يمكن لكل منتج نشر رسالة إما إلى قسم مختار عشوائياً أو قسم محدد دلالياً بواسطة مفتاح تجزئة ودالة تجزئة. سنركز على كيفية تفاعل المستهلكين مع الوسطاء.

لدى كافكا مفهوم مجموعات المستهلكين. تتكون كل مجموعة مستهلكين من مستهلك واحد أو أكثر يستهلكون معاً مجموعة من المواضيع المشترك فيها، أي يتم توصيل كل رسالة إلى واحد فقط من المستهلكين داخل المجموعة. تستهلك كل مجموعة مستهلكين مختلفة المجموعة الكاملة من الرسائل المشترك فيها بشكل مستقل ولا حاجة للتنسيق عبر مجموعات المستهلكين. يمكن أن يكون المستهلكون داخل نفس المجموعة في عمليات مختلفة أو على أجهزة مختلفة. هدفنا هو تقسيم الرسائل المخزنة في الوسطاء بالتساوي بين المستهلكين، دون إدخال عبء تنسيق كبير.

قرارنا الأول هو جعل القسم داخل الموضوع أصغر وحدة من التوازي. هذا يعني أنه في أي وقت معين، يتم استهلاك جميع الرسائل من قسم واحد بواسطة مستهلك واحد فقط داخل كل مجموعة مستهلكين. لو سمحنا لمستهلكين متعددين باستهلاك قسم واحد في وقت واحد، لكان عليهم التنسيق حول من يستهلك أي رسائل، مما يستلزم عبء قفل وصيانة حالة. على النقيض من ذلك، في تصميمنا، تحتاج عمليات الاستهلاك إلى التنسيق فقط عندما يعيد المستهلكون موازنة الحمل، وهو حدث نادر. لكي يكون الحمل متوازناً حقاً، نتطلب أقساماً أكثر بكثير في موضوع من المستهلكين في كل مجموعة. يمكننا تحقيق ذلك بسهولة عن طريق التجزئة الزائدة لموضوع.

القرار الثاني الذي اتخذناه هو عدم وجود عقدة "رئيسية" مركزية، بل السماح للمستهلكين بالتنسيق فيما بينهم بطريقة لامركزية. يمكن أن تؤدي إضافة رئيس إلى تعقيد النظام لأننا يجب أن نقلق أكثر بشأن فشل الرئيس. لتسهيل التنسيق، نستخدم خدمة إجماع عالية التوافر Zookeeper [10].

لدى Zookeeper واجهة برمجة تطبيقات بسيطة للغاية، تشبه نظام الملفات. يمكن للمرء إنشاء مسار، وتعيين قيمة مسار، وقراءة قيمة مسار، وحذف مسار، وإدراج أبناء مسار. يقوم ببعض الأشياء المثيرة للاهتمام: (أ) يمكن للمرء تسجيل مراقب على مسار والحصول على إشعار عندما يتغير أبناء مسار أو قيمة مسار؛ (ب) يمكن إنشاء مسار كعابر (على عكس دائم)، مما يعني أنه إذا اختفى العميل المنشئ، تتم إزالة المسار تلقائياً بواسطة خادم Zookeeper؛ (ج) يستنسخ zookeeper بياناته إلى خوادم متعددة، مما يجعل البيانات موثوقة ومتاحة للغاية.

يستخدم كافكا Zookeeper للمهام التالية: (1) اكتشاف إضافة وإزالة الوسطاء والمستهلكين، (2) تفعيل عملية إعادة التوازن في كل مستهلك عندما تحدث الأحداث أعلاه، و(3) الحفاظ على علاقة الاستهلاك وتتبع الإزاحة المستهلكة لكل قسم. على وجه التحديد، عندما يبدأ كل وسيط أو مستهلك، يخزن معلوماته في سجل وسيط أو مستهلك في Zookeeper. يحتوي سجل الوسيط على اسم المضيف والمنفذ للوسيط، ومجموعة المواضيع والأقسام المخزنة عليه. يتضمن سجل المستهلك مجموعة المستهلكين التي ينتمي إليها المستهلك ومجموعة المواضيع التي يشترك فيها. ترتبط كل مجموعة مستهلكين بسجل ملكية وسجل إزاحة في Zookeeper. يحتوي سجل الملكية على مسار واحد لكل قسم مشترك فيه وقيمة المسار هي معرّف المستهلك الذي يستهلك حالياً من هذا القسم (نستخدم المصطلح أن المستهلك يمتلك هذا القسم). يخزن سجل الإزاحة لكل قسم مشترك فيه، إزاحة آخر رسالة مستهلكة في القسم.

المسارات المنشأة في Zookeeper عابرة لسجل الوسيط وسجل المستهلك وسجل الملكية، ودائمة لسجل الإزاحة. إذا فشل وسيط، تتم إزالة جميع الأقسام عليه تلقائياً من سجل الوسيط. يتسبب فشل المستهلك في فقدان إدخاله في سجل المستهلك وجميع الأقسام التي يمتلكها في سجل الملكية. يسجل كل مستهلك مراقب Zookeeper على كل من سجل الوسيط وسجل المستهلك، وسيتم إخطاره كلما حدث تغيير في مجموعة الوسطاء أو مجموعة المستهلكين. أثناء بدء التشغيل الأولي للمستهلك أو عندما يتم إخطار المستهلك بتغيير وسيط/مستهلك من خلال المراقب، يبدأ المستهلك عملية إعادة توازن لتحديد المجموعة الفرعية الجديدة من الأقسام التي يجب أن يستهلك منها. يتم وصف العملية في الخوارزمية 1.

**الخوارزمية 1: عملية إعادة التوازن للمستهلك Ci في المجموعة G**
```
لكل موضوع T يشترك فيه Ci {
  إزالة الأقسام المملوكة لـ Ci من سجل الملكية
  قراءة سجلات الوسيط والمستهلك من Zookeeper
  حساب PT = الأقسام المتاحة في جميع الوسطاء تحت الموضوع T
  حساب CT = جميع المستهلكين في G الذين يشتركون في T
  ترتيب PT و CT
  ليكن j موضع الفهرس لـ Ci في CT وليكن N = |PT|/|CT|
  تعيين أقسام من j*N إلى (j+1)*N - 1 في PT للمستهلك Ci
  لكل قسم معين p {
    تعيين مالك p إلى Ci في سجل الملكية
    ليكن Op = إزاحة القسم p المخزنة في سجل الإزاحة
    استدعاء خيط لسحب البيانات في القسم p من الإزاحة Op
  }
}
```

من خلال قراءة سجل الوسيط والمستهلك من Zookeeper، يحسب المستهلك أولاً المجموعة (PT) من الأقسام المتاحة لكل موضوع مشترك فيه T والمجموعة (CT) من المستهلكين المشتركين في T. ثم يقسم PT إلى مدى |CT| قطعاً ويختار بشكل حتمي قطعة واحدة ليمتلكها. لكل قسم يختاره المستهلك، يكتب نفسه كمالك جديد للقسم في سجل الملكية. أخيراً، يبدأ المستهلك خيطاً لسحب البيانات من كل قسم مملوك، بدءاً من الإزاحة المخزنة في سجل الإزاحة. مع سحب الرسائل من قسم، يحدث المستهلك دورياً أحدث إزاحة مستهلكة في سجل الإزاحة.

عندما يكون هناك مستهلكون متعددون داخل مجموعة، سيتم إخطار كل منهم بتغيير وسيط أو مستهلك. ومع ذلك، قد يأتي الإخطار في أوقات مختلفة قليلاً عند المستهلكين. لذلك، من الممكن أن يحاول مستهلك واحد أخذ ملكية قسم لا يزال مملوكاً لمستهلك آخر. عندما يحدث هذا، يحرر المستهلك الأول ببساطة جميع الأقسام التي يمتلكها حالياً، وينتظر قليلاً ويعيد محاولة عملية إعادة التوازن. في الممارسة العملية، غالباً ما تستقر عملية إعادة التوازن بعد بضع محاولات فقط. عند إنشاء مجموعة مستهلكين جديدة، لا تتوفر إزاحات في سجل الإزاحة. في هذه الحالة، سيبدأ المستهلكون بأصغر أو أكبر إزاحة (حسب التكوين) متاحة على كل قسم مشترك فيه، باستخدام واجهة برمجة تطبيقات نوفرها على الوسطاء.

## 3.3 ضمانات التوصيل

بشكل عام، يضمن كافكا فقط التوصيل مرة واحدة على الأقل. يتطلب التوصيل مرة واحدة بالضبط عادةً التزامات ثنائية الطور وهو غير ضروري لتطبيقاتنا. في معظم الأوقات، يتم توصيل رسالة بالضبط مرة واحدة إلى كل مجموعة مستهلكين. ومع ذلك، في حالة تعطل عملية مستهلك بدون إيقاف نظيف، قد تحصل عملية المستهلك التي تتولى تلك الأقسام المملوكة للمستهلك الفاشل على بعض الرسائل المكررة التي تكون بعد آخر إزاحة تم الالتزام بها بنجاح في zookeeper. إذا كان التطبيق يهتم بالتكرارات، فيجب عليه إضافة منطق إلغاء التكرار الخاص به، إما باستخدام الإزاحات التي نعيدها إلى المستهلك أو بعض المفتاح الفريد داخل الرسالة. هذا عادةً نهج أكثر فعالية من حيث التكلفة من استخدام التزامات ثنائية الطور.

يضمن كافكا توصيل الرسائل من قسم واحد إلى مستهلك بالترتيب. ومع ذلك، لا يوجد ضمان على ترتيب الرسائل القادمة من أقسام مختلفة.

لتجنب تلف السجل، يخزن كافكا CRC لكل رسالة في السجل. إذا كان هناك أي خطأ إدخال/إخراج على الوسيط، يقوم كافكا بتشغيل عملية استرداد لإزالة تلك الرسائل ذات CRC غير المتسقة. كما يسمح لنا وجود CRC على مستوى الرسالة بالتحقق من أخطاء الشبكة بعد إنتاج أو استهلاك رسالة.

إذا تعطل وسيط، تصبح أي رسالة مخزنة عليه لم تُستهلك بعد غير متاحة. إذا تضرر نظام التخزين على وسيط بشكل دائم، تُفقد أي رسالة غير مستهلكة إلى الأبد. في المستقبل، نخطط لإضافة تكرار مدمج في كافكا لتخزين كل رسالة بشكل متكرر على وسطاء متعددين.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Kafka Architecture), Figure 2 (Kafka log and in-memory index)
- **Key terms introduced:**
  - Topic: موضوع
  - Producer: منتج
  - Consumer: مستهلك
  - Broker: وسيط
  - Partition: قسم
  - Offset: إزاحة
  - Message stream: تدفق الرسائل
  - Iterator: مكرر
  - Payload: حمولة
  - Point-to-point: من نقطة إلى نقطة
  - Publish/subscribe: نشر/اشتراك
  - Segment files: ملفات القطاعات
  - Logical log: سجل منطقي
  - Page cache: ذاكرة التخزين المؤقت للصفحة
  - Double buffering: التخزين المؤقت المزدوج
  - Garbage collection: جمع القمامة
  - sendfile API: واجهة برمجة تطبيقات sendfile
  - Stateless: عديم الحالة
  - Retention policy: سياسة الاحتفاظ
  - Consumer groups: مجموعات المستهلكين
  - Zookeeper: Zookeeper (kept in English)
  - Rebalance: إعادة التوازن
  - Registry: سجل
  - Ephemeral: عابر
  - Persistent: دائم
  - At-least-once delivery: التوصيل مرة واحدة على الأقل
  - Exactly-once delivery: التوصيل مرة واحدة بالضبط
  - Two-phase commits: التزامات ثنائية الطور
  - CRC: CRC (kept as acronym)
  - De-duplication: إلغاء التكرار

- **Equations:** None
- **Citations:** [5], [10]
- **Algorithms:** Algorithm 1 (rebalance process)

- **Special handling:**
  - Code samples provided in both English and partially translated comments
  - Algorithm 1 translated with pseudocode structure preserved
  - Technical terms like Zookeeper, HDFS, NFS kept in original English
  - CRC kept as acronym as commonly used in technical contexts

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.89
