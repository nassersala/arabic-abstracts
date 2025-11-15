# Section 4: ZooKeeper Implementation
## القسم 4: تنفيذ زوكيبر

**Section:** implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** distributed system, replication, consensus, atomicity, pipeline, throughput, fault-tolerant, crash recovery

---

### English Version

ZooKeeper provides high availability by replicating the ZooKeeper data on each server that composes the service. We assume that servers fail by crashing, and such faulty servers may later recover. Figure 2 shows the high-level components of the ZooKeeper service. Upon receiving a request, a server prepares it for execution (request processor). If such a request requires coordination among the servers (write requests), then they use an agreement protocol (an implementation of atomic broadcast), and finally servers commit changes to the ZooKeeper database fully replicated across all servers of the ensemble. In the case of read requests, a server simply reads the state of the local database and generates a response to the query.

The replicated database is an in-memory database containing the entire data tree. Each znode in the tree stores a maximum of 1MB of data by default, but this maximum value is a configuration parameter that can be changed in specific cases. For recoverability, we efficiently log updates to disk, and we force writes to be on the disk media before they are applied to the in-memory database. In fact, as Chubby [6], we keep a replay log (a write-ahead log, in database parlance) of committed operations and generate periodic snapshots of the in-memory database.

Every ZooKeeper server services clients. Clients connect to exactly one server to submit its requests. As we noted earlier, read requests are serviced from the local replica of each server database. Requests that change the state of the service, write requests, are processed by an agreement protocol.

As part of the agreement protocol write requests are forwarded to a single server, called the leader. The rest of the ZooKeeper servers, called followers, receive message proposals consisting of state changes from the leader and agree upon state changes. The messaging layer takes care of replacing leaders on failures and syncing followers with leaders.

#### 4.1 Request Processor

Since the messaging layer is atomic, we guarantee that the local replicas never diverge, although at any point in time some servers may have applied more transactions than others. Unlike the requests sent from clients, the transactions are idempotent. When the leader receives a write request, it calculates what the state of the system will be when the write is applied and transforms it into a transaction that captures this new state. The future state must be calculated because there may be outstanding transactions that have not yet been applied to the database. For example, if a client does a conditional setData and the version number in the request matches the future version number of the znode being updated, the service generates a setDataTXN that contains the new data, the new version number, and updated time stamps. If an error occurs, such as mismatched version numbers or the znode to be updated does not exist, an errorTXN is generated instead.

#### 4.2 Atomic Broadcast

All requests that update ZooKeeper state are forwarded to the leader. The leader executes the request and broadcasts the change to the ZooKeeper state through Zab [24], an atomic broadcast protocol. The server that receives the client request responds to the client when it delivers the corresponding state change. Zab guarantees that changes broadcast by a leader are delivered in the order they were sent and all changes from previous leaders are delivered to an established leader before it broadcasts its own changes.

There are a few implementation details that simplify our implementation and give us excellent performance. We use TCP for our transport so message order is maintained by the network, which allows us to simplify our implementation. We use the leader-based aspect of Zab to log proposals from the leader on all followers. Logging to disk is a bottleneck for performance, so using logging at the followers enables us to saturate the I/O channel and take advantage of group commits. The message count and size of broadcast messages is small enough that we are not at risk of flooding the network, and we do use batching and pipelining to make it easier to push messages to followers.

ZooKeeper uses Zab as its atomic broadcast protocol, but ZooKeeper does not use Zab to commit client requests directly; instead, ZooKeeper uses the total ordering Zab provides to order client requests and to order commit operations. In particular, ZooKeeper does not invoke Zab's agreement for read operations that do not modify state. Instead, each server checks that the read corresponds to the last committed state it has seen.

#### 4.3 Replicated Database

Each replica has a copy in memory of the ZooKeeper state. When a ZooKeeper server recovers from a crash, it needs to recover this internal state. Replaying all delivered messages to recover state would take prohibitively long after running for a while, so ZooKeeper uses periodic snapshots and only requires redelivery of messages since the start of the snapshot. We call ZooKeeper snapshots fuzzy snapshots since we do not lock the ZooKeeper state to take the snapshot; instead, we do a depth first scan of the tree atomically reading each znode's data and meta-data and writing them to disk. Since the resulting fuzzy snapshot may have applied some subset of the state changes delivered during the generation of the snapshot, the result may not correspond to the state of ZooKeeper at any point in time. However, since state changes are idempotent, we can apply them twice as long as we apply the state changes in order.

For example, assume that in a ZooKeeper data tree two nodes /foo and /goo have values f1 and g1 respectively and both are at version 1 when the fuzzy snapshot begins, and the following stream of state changes arrive having the form ⟨transactionType, path, value, new-version⟩:

⟨SetDataTXN, /foo, f2, 2⟩
⟨SetDataTXN, /goo, g2, 2⟩
⟨SetDataTXN, /foo, f3, 3⟩

After processing these state changes, /foo and /goo have values f3 and g2 with versions 3 and 2, respectively. However, the fuzzy snapshot may have recorded that /foo and /goo have values f3 and g1 with versions 3 and 1. When replaying the transactions during recovery, the SetDataTXN ⟨SetDataTXN, /foo, f2, 2⟩ will fail, but the remaining two transactions will succeed, and end with the correct state of the data tree.

#### 4.4 Client-Server Interactions

When a server processes a write request, it also sends out and clears notifications relative to any watch that corresponds to that update. Servers process writes in order and do not process other writes or reads concurrently. This ensures strict succession of notifications. Note that servers handle notifications locally. Only the server that a client is connected to tracks and triggers notifications for that client.

Read requests are handled locally at each server. Each read request is processed and tagged with a zxid that corresponds to the last transaction seen by the server. This zxid defines the partial order of the read requests with respect to the write requests. By processing reads locally, we obtain excellent read performance because it is just an in-memory operation on the local server, and there is no disk activity or agreement protocol to run. This design choice is key to achieving our goal of excellent performance with read-dominant workloads.

One drawback of using fast reads is not guaranteeing precedence order for read operations. That is, a read operation may return a stale value, even though a more recent update to the same znode has been committed. Not all of our applications require precedence order, but for applications that do require it, we have implemented sync. This primitive executes asynchronously and is ordered by the leader after all pending writes to its local replica. To guarantee that a given read operation returns the latest updated value, a client calls sync followed by the read operation. The FIFO order guarantee of client operations together with the global guarantee of sync enables the result of the read operation to reflect any changes that happened before the sync was issued. In our implementation, we do not need to atomically broadcast sync as we use a leader-based algorithm, and we simply place the sync operation at the end of the queue of requests between the leader and the server executing the call to sync. In order for this to work, the follower must be sure that the leader is still the leader. If there are pending transactions that commit, then the server does not suspect the leader. If the pending queue is empty, the leader needs to issue a null transaction to commit and orders the sync after that transaction. This has the nice property that when the leader is under load, no extra broadcast traffic is generated. In our implementation, timeouts are set such that leaders realize they are not leaders before followers abandon them, so we do not issue the null transaction.

ZooKeeper servers process requests from clients in FIFO order. Responses include the zxid that the response is relative to. Even heartbeat messages during intervals of no activity include the last zxid seen by the server that the client is connected to. If the client connects to a new server, that new server ensures that its view of the ZooKeeper data is at least as recent as the view of the client by checking the last zxid of the client against its last zxid. If the client has a more recent view than the server, the server does not reestablish the session with the client until the server has caught up. The client is guaranteed to be able to find another server that has a recent view of the system since the client only sees changes that have been replicated to a majority of the ZooKeeper servers. This behavior is important to guarantee durability.

To detect client session failures, ZooKeeper uses timeouts. The leader determines that there has been a failure if no other server receives anything from a client session within the session timeout. If the client sends requests frequently enough, then there is no need to send any other message. Otherwise, the client sends heartbeat messages during periods of low activity. If the client cannot communicate with a server to send a request or heartbeat, it connects to a different ZooKeeper server to re-establish its session. To prevent the session from timing out, the ZooKeeper client library sends a heartbeat after the session has been idle for s/3 ms and switch to a new server if it has not heard from a server for 2s/3 ms, where s is the session timeout parameter set by the client.

---

### النسخة العربية

يوفر زوكيبر توفراً عالياً عن طريق نسخ بيانات زوكيبر على كل خادم يشكل الخدمة. نفترض أن الخوادم تفشل بالتعطل، وقد تتعافى مثل هذه الخوادم المعيبة لاحقاً. يوضح الشكل 2 المكونات عالية المستوى لخدمة زوكيبر. عند تلقي طلب، يقوم الخادم بتحضيره للتنفيذ (معالج الطلب). إذا كان مثل هذا الطلب يتطلب تنسيقاً بين الخوادم (طلبات الكتابة)، فإنها تستخدم بروتوكول اتفاق (تنفيذ للبث الذري)، وأخيراً تلتزم الخوادم بالتغييرات على قاعدة بيانات زوكيبر المنسوخة بالكامل عبر جميع خوادم المجموعة. في حالة طلبات القراءة، يقرأ الخادم ببساطة حالة قاعدة البيانات المحلية ويولد استجابة للاستعلام.

قاعدة البيانات المُنسَخة هي قاعدة بيانات في الذاكرة تحتوي على شجرة البيانات الكاملة. تخزن كل عقدة بيانات في الشجرة بحد أقصى 1 ميجابايت من البيانات بشكل افتراضي، لكن هذه القيمة القصوى هي معامل تكوين يمكن تغييره في حالات محددة. من أجل القابلية للاسترداد، نقوم بتسجيل التحديثات على القرص بكفاءة، ونفرض أن تكون الكتابات على وسائط القرص قبل تطبيقها على قاعدة البيانات في الذاكرة. في الواقع، مثل Chubby [6]، نحتفظ بسجل إعادة تشغيل (سجل كتابة مسبقة، في مصطلحات قواعد البيانات) للعمليات الملتزم بها ونولد لقطات دورية لقاعدة البيانات في الذاكرة.

يخدم كل خادم زوكيبر العملاء. يتصل العملاء بخادم واحد بالضبط لتقديم طلباتهم. كما لاحظنا سابقاً، يتم تقديم طلبات القراءة من النسخة المحلية لقاعدة بيانات كل خادم. يتم معالجة الطلبات التي تغير حالة الخدمة، طلبات الكتابة، بواسطة بروتوكول اتفاق.

كجزء من بروتوكول الاتفاق، يتم إعادة توجيه طلبات الكتابة إلى خادم واحد، يسمى القائد. تستقبل بقية خوادم زوكيبر، التي تسمى المتابعين، مقترحات رسائل تتكون من تغييرات الحالة من القائد وتوافق على تغييرات الحالة. تعتني طبقة الرسائل باستبدال القادة عند الفشل ومزامنة المتابعين مع القادة.

#### 4.1 معالج الطلب

نظراً لأن طبقة الرسائل ذرية، فإننا نضمن أن النسخ المحلية لا تتباعد أبداً، على الرغم من أنه في أي نقطة زمنية قد تكون بعض الخوادم قد طبقت معاملات أكثر من غيرها. على عكس الطلبات المرسلة من العملاء، المعاملات متماثلة. عندما يتلقى القائد طلب كتابة، يحسب ما ستكون عليه حالة النظام عند تطبيق الكتابة ويحولها إلى معاملة تلتقط هذه الحالة الجديدة. يجب حساب الحالة المستقبلية لأنه قد تكون هناك معاملات معلقة لم يتم تطبيقها بعد على قاعدة البيانات. على سبيل المثال، إذا قام عميل بتنفيذ setData مشروط وتطابق رقم الإصدار في الطلب رقم الإصدار المستقبلي لعقدة البيانات التي يتم تحديثها، فإن الخدمة تولد setDataTXN يحتوي على البيانات الجديدة ورقم الإصدار الجديد والطوابع الزمنية المحدثة. إذا حدث خطأ، مثل عدم تطابق أرقام الإصدارات أو عقدة البيانات التي سيتم تحديثها غير موجودة، يتم إنشاء errorTXN بدلاً من ذلك.

#### 4.2 البث الذري

يتم إعادة توجيه جميع الطلبات التي تحدث حالة زوكيبر إلى القائد. ينفذ القائد الطلب ويبث التغيير على حالة زوكيبر من خلال Zab [24]، وهو بروتوكول بث ذري. يستجيب الخادم الذي يتلقى طلب العميل للعميل عندما يسلم تغيير الحالة المقابل. يضمن Zab أن التغييرات التي يبثها القائد يتم تسليمها بالترتيب الذي أُرسلت به وأن جميع التغييرات من القادة السابقين يتم تسليمها إلى قائد راسخ قبل أن يبث تغييراته الخاصة.

هناك بعض تفاصيل التنفيذ التي تبسط تنفيذنا وتمنحنا أداءً ممتازاً. نستخدم TCP للنقل لذا يتم الحفاظ على ترتيب الرسائل بواسطة الشبكة، مما يسمح لنا بتبسيط تنفيذنا. نستخدم الجانب القائم على القائد من Zab لتسجيل المقترحات من القائد على جميع المتابعين. يُعد التسجيل على القرص عنق زجاجة للأداء، لذا فإن استخدام التسجيل عند المتابعين يمكننا من إشباع قناة الإدخال/الإخراج والاستفادة من الالتزامات الجماعية. عدد الرسائل وحجم رسائل البث صغير بما يكفي بحيث لا نكون في خطر إغراق الشبكة، ونستخدم الدُفعات والتسلسل لتسهيل دفع الرسائل إلى المتابعين.

يستخدم زوكيبر Zab كبروتوكول بث ذري، لكن زوكيبر لا يستخدم Zab لالتزام طلبات العميل مباشرة؛ بدلاً من ذلك، يستخدم زوكيبر الترتيب الكلي الذي يوفره Zab لترتيب طلبات العميل ولترتيب عمليات الالتزام. على وجه الخصوص، لا يستدعي زوكيبر اتفاق Zab لعمليات القراءة التي لا تعدل الحالة. بدلاً من ذلك، يتحقق كل خادم من أن القراءة تتوافق مع آخر حالة ملتزم بها رآها.

#### 4.3 قاعدة البيانات المُنسَخة

لكل نسخة متماثلة نسخة في الذاكرة من حالة زوكيبر. عندما يتعافى خادم زوكيبر من التعطل، يحتاج إلى استرداد هذه الحالة الداخلية. ستستغرق إعادة تشغيل جميع الرسائل المسلمة لاسترداد الحالة وقتاً طويلاً بشكل يمنعها بعد التشغيل لفترة، لذا يستخدم زوكيبر لقطات دورية ويتطلب فقط إعادة تسليم الرسائل منذ بداية اللقطة. نسمي لقطات زوكيبر لقطات غامضة لأننا لا نقفل حالة زوكيبر لأخذ اللقطة؛ بدلاً من ذلك، نقوم بمسح عمق أولاً للشجرة بقراءة بيانات وبيانات وصفية لكل عقدة بيانات بشكل ذري وكتابتها على القرص. نظراً لأن اللقطة الغامضة الناتجة قد تكون قد طبقت بعض مجموعة فرعية من تغييرات الحالة المسلمة أثناء إنشاء اللقطة، فقد لا تتوافق النتيجة مع حالة زوكيبر في أي نقطة زمنية. ومع ذلك، نظراً لأن تغييرات الحالة متماثلة، يمكننا تطبيقها مرتين طالما أننا نطبق تغييرات الحالة بالترتيب.

على سبيل المثال، افترض أنه في شجرة بيانات زوكيبر، عقدتان /foo و /goo لهما قيم f1 و g1 على التوالي وكلاهما في الإصدار 1 عندما تبدأ اللقطة الغامضة، ويصل تدفق تغييرات الحالة التالي بالشكل ⟨transactionType, path, value, new-version⟩:

⟨SetDataTXN, /foo, f2, 2⟩
⟨SetDataTXN, /goo, g2, 2⟩
⟨SetDataTXN, /foo, f3, 3⟩

بعد معالجة تغييرات الحالة هذه، /foo و /goo لهما قيم f3 و g2 مع إصدارات 3 و 2، على التوالي. ومع ذلك، قد تكون اللقطة الغامضة قد سجلت أن /foo و /goo لهما قيم f3 و g1 مع إصدارات 3 و 1. عند إعادة تشغيل المعاملات أثناء الاسترداد، ستفشل SetDataTXN ⟨SetDataTXN, /foo, f2, 2⟩، لكن المعاملتين المتبقيتين ستنجحان، وتنتهيان بالحالة الصحيحة لشجرة البيانات.

#### 4.4 تفاعلات العميل-الخادم

عندما يعالج خادم طلب كتابة، فإنه يرسل أيضاً ويمسح الإشعارات المتعلقة بأي مراقبة تتوافق مع هذا التحديث. تعالج الخوادم الكتابات بالترتيب ولا تعالج الكتابات أو القراءات الأخرى بالتزامن. هذا يضمن تعاقب صارم للإشعارات. لاحظ أن الخوادم تتعامل مع الإشعارات محلياً. فقط الخادم الذي يتصل به العميل يتتبع ويُحفز الإشعارات لهذا العميل.

يتم معالجة طلبات القراءة محلياً على كل خادم. يتم معالجة كل طلب قراءة ووضع علامة عليه باستخدام zxid يتوافق مع آخر معاملة شاهدها الخادم. يحدد zxid هذا الترتيب الجزئي لطلبات القراءة فيما يتعلق بطلبات الكتابة. من خلال معالجة القراءات محلياً، نحصل على أداء قراءة ممتاز لأنها مجرد عملية في الذاكرة على الخادم المحلي، ولا يوجد نشاط قرص أو بروتوكول اتفاق لتشغيله. اختيار التصميم هذا هو مفتاح تحقيق هدفنا المتمثل في الأداء الممتاز مع أحمال العمل المهيمنة على القراءة.

أحد عيوب استخدام القراءات السريعة هو عدم ضمان ترتيب الأسبقية لعمليات القراءة. أي أن عملية القراءة قد ترجع قيمة قديمة، حتى لو تم الالتزام بتحديث أحدث لنفس عقدة البيانات. ليس كل تطبيقاتنا تتطلب ترتيب الأسبقية، ولكن بالنسبة للتطبيقات التي تتطلب ذلك، قمنا بتنفيذ sync. تُنفَّذ هذه البدائية بشكل غير متزامن ويتم ترتيبها بواسطة القائد بعد جميع الكتابات المعلقة إلى نسختها المحلية. لضمان أن عملية قراءة معينة ترجع أحدث قيمة محدثة، يستدعي العميل sync متبوعاً بعملية القراءة. يتيح ضمان ترتيب FIFO لعمليات العميل مع الضمان العام لـ sync أن تعكس نتيجة عملية القراءة أي تغييرات حدثت قبل إصدار sync. في تنفيذنا، لا نحتاج إلى بث sync بشكل ذري حيث نستخدم خوارزمية قائمة على القائد، ونضع ببساطة عملية sync في نهاية قائمة انتظار الطلبات بين القائد والخادم الذي ينفذ استدعاء sync. لكي يعمل هذا، يجب أن يكون المتابع متأكداً من أن القائد لا يزال القائد. إذا كانت هناك معاملات معلقة تلتزم، فإن الخادم لا يشك في القائد. إذا كانت قائمة الانتظار المعلقة فارغة، يحتاج القائد إلى إصدار معاملة فارغة للالتزام وترتيب sync بعد تلك المعاملة. هذا له خاصية جميلة أنه عندما يكون القائد تحت الحمل، لا يتم إنشاء حركة مرور بث إضافية. في تنفيذنا، يتم تعيين المهلات بحيث يدرك القادة أنهم ليسوا قادة قبل أن يتخلى المتابعون عنهم، لذا لا نصدر المعاملة الفارغة.

تعالج خوادم زوكيبر الطلبات من العملاء بترتيب FIFO. تتضمن الاستجابات zxid الذي تكون الاستجابة نسبية له. حتى رسائل نبضات القلب خلال فترات عدم النشاط تتضمن آخر zxid شاهده الخادم الذي يتصل به العميل. إذا اتصل العميل بخادم جديد، فإن هذا الخادم الجديد يضمن أن رؤيته لبيانات زوكيبر حديثة على الأقل مثل رؤية العميل عن طريق التحقق من آخر zxid للعميل مقابل آخر zxid له. إذا كان لدى العميل رؤية أحدث من الخادم، فإن الخادم لا يعيد إنشاء الجلسة مع العميل حتى يلحق الخادم. يُضمن للعميل أن يكون قادراً على العثور على خادم آخر لديه رؤية حديثة للنظام لأن العميل يرى فقط التغييرات التي تم نسخها إلى غالبية خوادم زوكيبر. هذا السلوك مهم لضمان المتانة.

للكشف عن إخفاقات جلسة العميل، يستخدم زوكيبر المهلات. يحدد القائد أن هناك فشلاً إذا لم يتلق أي خادم آخر أي شيء من جلسة عميل ضمن مهلة الجلسة. إذا أرسل العميل طلبات بشكل متكرر بما فيه الكفاية، فلا حاجة لإرسال أي رسالة أخرى. وإلا، يرسل العميل رسائل نبضات القلب خلال فترات النشاط المنخفض. إذا لم يتمكن العميل من الاتصال بخادم لإرسال طلب أو نبضة قلب، فإنه يتصل بخادم زوكيبر مختلف لإعادة إنشاء جلسته. لمنع انتهاء مهلة الجلسة، ترسل مكتبة عميل زوكيبر نبضة قلب بعد أن تكون الجلسة خاملة لمدة s/3 ميلي ثانية وتتحول إلى خادم جديد إذا لم تسمع من خادم لمدة 2s/3 ميلي ثانية، حيث s هو معامل مهلة الجلسة الذي حدده العميل.

---

### Translation Notes

- **Figures referenced:** Figure 2 (ZooKeeper components)
- **Key terms introduced:**
  - Atomic broadcast (بث ذري) - coordination protocol
  - Zab protocol (بروتوكول Zab) - ZooKeeper's atomic broadcast
  - Fuzzy snapshots (لقطات غامضة) - non-locked snapshots
  - Request processor (معالج الطلب) - component processing requests
  - Leader/follower (قائد/متابع) - replication roles
  - Write-ahead log (سجل كتابة مسبقة) - durability mechanism
  - zxid - transaction identifier (kept as is)

- **Equations:** Transaction format: ⟨transactionType, path, value, new-version⟩
- **Citations:** [6], [24] - preserved as in original
- **Special handling:**
  - Protocol names (Zab, TCP) kept in English
  - Transaction types (SetDataTXN, errorTXN) kept in English
  - Technical parameters (s/3 ms, 2s/3 ms) preserved exactly
  - Code examples preserved in original format

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-translation Check

First paragraph back-translation: "ZooKeeper provides high availability by replicating ZooKeeper data on each server that composes the service. We assume servers fail by crashing, and such faulty servers may later recover..."

✅ Semantically equivalent to original
