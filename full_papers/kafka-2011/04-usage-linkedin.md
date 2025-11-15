# Section 4: Kafka Usage at LinkedIn
## القسم 4: استخدام كافكا في لينكد إن

**Section:** usage-at-linkedin
**Translation Quality:** 0.88
**Glossary Terms Used:** distributed system, data pipeline, real-time, offline, Hadoop, schema, load balancer, monitoring

---

### English Version

In this section, we describe how we use Kafka at LinkedIn. Figure 3 shows a simplified version of our deployment. We have one Kafka cluster co-located with each datacenter where our user-facing services run. The frontend services generate various kinds of log data and publish it to the local Kafka brokers in batches. We rely on a hardware load-balancer to distribute the publish requests to the set of Kafka brokers evenly. The online consumers of Kafka run in services within the same datacenter.

We also deploy a cluster of Kafka in a separate datacenter for offline analysis, located geographically close to our Hadoop cluster and other data warehouse infrastructure. This instance of Kafka runs a set of embedded consumers to pull data from the Kafka instances in the live datacenters. We then run data load jobs to pull data from this replica cluster of Kafka into Hadoop and our data warehouse, where we run various reporting jobs and analytical process on the data. We also use this Kafka cluster for prototyping and have the ability to run simple scripts against the raw event streams for ad hoc querying.

Without too much tuning, the end-to-end latency for the complete pipeline is about 10 seconds on average, good enough for our requirements. Currently, Kafka accumulates hundreds of gigabytes of data and close to a billion messages per day, which we expect will grow significantly as we finish converting legacy systems to take advantage of Kafka. More types of messages will be added in the future. The rebalance process is able to automatically redirect the consumption when the operation staffs start or stop brokers for software or hardware maintenance.

Our tracking also includes an auditing system to verify that there is no data loss along the whole pipeline. To facilitate that, each message carries the timestamp and the server name when they are generated. We instrument each producer such that it periodically generates a monitoring event, which records the number of messages published by that producer for each topic within a fixed time window. The producer publishes the monitoring events to Kafka in a separate topic. The consumers can then count the number of messages that they have received from a given topic and validate those counts with the monitoring events to validate the correctness of data.

Loading into the Hadoop cluster is accomplished by implementing a special Kafka input format that allows MapReduce jobs to directly read data from Kafka. A MapReduce job loads the raw data and then groups and compresses it for efficient processing in the future. The stateless broker and client-side storage of message offsets again come into play here, allowing the MapReduce task management (which allows tasks to fail and be restarted) to handle the data load in a natural way without duplicating or losing messages in the event of a task restart. Both data and offsets are stored in HDFS only on the successful completion of the job.

We chose to use Avro [2] as our serialization protocol since it is efficient and supports schema evolution. For each message, we store the id of its Avro schema and the serialized bytes in the payload. This schema allows us to enforce a contract to ensure compatibility between data producers and consumers. We use a lightweight schema registry service to map the schema id to the actual schema. When a consumer gets a message, it looks up in the schema registry to retrieve the schema, which is used to decode the bytes into an object (this lookup need only be done once per schema, since the values are immutable).

---

### النسخة العربية

في هذا القسم، نصف كيف نستخدم كافكا في لينكد إن. يُظهر الشكل 3 نسخة مبسطة من نشرنا. لدينا مجموعة كافكا واحدة موضوعة مع كل مركز بيانات حيث تعمل خدماتنا الموجهة للمستخدم. تولد خدمات الواجهة الأمامية أنواعاً مختلفة من بيانات السجلات وتنشرها إلى وسطاء كافكا المحليين على دفعات. نعتمد على موازن حمل أجهزة لتوزيع طلبات النشر على مجموعة وسطاء كافكا بالتساوي. يعمل المستهلكون المتصلون لكافكا في خدمات داخل نفس مركز البيانات.

كما ننشر أيضاً مجموعة من كافكا في مركز بيانات منفصل للتحليل غير المتصل، يقع جغرافياً بالقرب من مجموعة Hadoop الخاصة بنا وبنية مستودع البيانات الأخرى. تشغل نسخة كافكا هذه مجموعة من المستهلكين المدمجين لسحب البيانات من نسخ كافكا في مراكز البيانات النشطة. ثم نقوم بتشغيل مهام تحميل البيانات لسحب البيانات من مجموعة كافكا المُنسخة هذه إلى Hadoop ومستودع البيانات الخاص بنا، حيث نقوم بتشغيل مهام تقارير مختلفة وعمليات تحليلية على البيانات. نستخدم أيضاً مجموعة كافكا هذه للنماذج الأولية ولدينا القدرة على تشغيل نصوص بسيطة ضد تدفقات الأحداث الأولية للاستعلام المخصص.

دون الكثير من الضبط، يبلغ زمن الاستجابة من طرف إلى طرف لخط الأنابيب الكامل حوالي 10 ثوانٍ في المتوسط، وهو جيد بما يكفي لمتطلباتنا. حالياً، يجمع كافكا مئات الجيجابايتات من البيانات وما يقرب من مليار رسالة يومياً، ونتوقع أن ينمو بشكل كبير عندما ننتهي من تحويل الأنظمة القديمة للاستفادة من كافكا. ستُضاف المزيد من أنواع الرسائل في المستقبل. تستطيع عملية إعادة التوازن إعادة توجيه الاستهلاك تلقائياً عندما يبدأ موظفو التشغيل أو يوقفون الوسطاء لصيانة البرامج أو الأجهزة.

يتضمن تتبعنا أيضاً نظام تدقيق للتحقق من عدم وجود فقدان للبيانات على طول خط الأنابيب بالكامل. لتسهيل ذلك، تحمل كل رسالة الطابع الزمني واسم الخادم عند توليدها. نقيس كل منتج بحيث يولد دورياً حدث مراقبة، يسجل عدد الرسائل المنشورة بواسطة ذلك المنتج لكل موضوع ضمن نافذة زمنية ثابتة. ينشر المنتج أحداث المراقبة إلى كافكا في موضوع منفصل. يمكن للمستهلكين بعد ذلك عد عدد الرسائل التي تلقوها من موضوع معين والتحقق من صحة تلك الأعداد مع أحداث المراقبة للتحقق من صحة البيانات.

يتم التحميل في مجموعة Hadoop من خلال تنفيذ صيغة إدخال كافكا خاصة تسمح لمهام MapReduce بقراءة البيانات مباشرة من كافكا. تقوم مهمة MapReduce بتحميل البيانات الأولية ثم تجميعها وضغطها لمعالجة فعالة في المستقبل. يأتي الوسيط عديم الحالة والتخزين على جانب العميل لإزاحات الرسائل مرة أخرى للعب دوراً هنا، مما يسمح لإدارة مهام MapReduce (التي تسمح بفشل المهام وإعادة تشغيلها) بالتعامل مع تحميل البيانات بطريقة طبيعية دون تكرار أو فقدان الرسائل في حالة إعادة تشغيل المهمة. يتم تخزين كل من البيانات والإزاحات في HDFS فقط عند الانتهاء الناجح من المهمة.

اخترنا استخدام Avro [2] كبروتوكول التسلسل الخاص بنا لأنه فعال ويدعم تطور المخطط. لكل رسالة، نخزن معرّف مخطط Avro الخاص بها والبايتات المتسلسلة في الحمولة. يسمح لنا هذا المخطط بفرض عقد لضمان التوافق بين منتجي البيانات ومستهلكيها. نستخدم خدمة سجل مخطط خفيفة الوزن لربط معرّف المخطط بالمخطط الفعلي. عندما يحصل مستهلك على رسالة، يبحث في سجل المخطط لاسترجاع المخطط، الذي يُستخدم لفك تشفير البايتات إلى كائن (يجب إجراء هذا البحث مرة واحدة فقط لكل مخطط، لأن القيم غير قابلة للتغيير).

---

### Translation Notes

- **Figures referenced:** Figure 3 (Kafka Deployment)
- **Key terms introduced:**
  - Datacenter: مركز بيانات
  - User-facing services: خدمات موجهة للمستخدم
  - Frontend services: خدمات الواجهة الأمامية
  - Hardware load-balancer: موازن حمل أجهزة
  - Online consumers: المستهلكون المتصلون
  - Offline analysis: التحليل غير المتصل
  - Embedded consumers: المستهلكون المدمجون
  - Live datacenters: مراكز البيانات النشطة
  - Replica cluster: مجموعة مُنسخة
  - Data load jobs: مهام تحميل البيانات
  - Reporting jobs: مهام تقارير
  - Analytical process: عمليات تحليلية
  - Prototyping: النماذج الأولية
  - Ad hoc querying: الاستعلام المخصص
  - End-to-end latency: زمن الاستجابة من طرف إلى طرف
  - Legacy systems: الأنظمة القديمة
  - Auditing system: نظام تدقيق
  - Timestamp: الطابع الزمني
  - Monitoring event: حدث مراقبة
  - Time window: نافذة زمنية
  - MapReduce: MapReduce (kept in English)
  - Input format: صيغة إدخال
  - Task management: إدارة مهام
  - Schema evolution: تطور المخطط
  - Serialization protocol: بروتوكول التسلسل
  - Schema registry: سجل مخطط
  - Immutable: غير قابلة للتغيير

- **Citations:** [2]

- **Special handling:**
  - System/product names (Hadoop, HDFS, MapReduce, Avro) kept in original English form
  - "10 seconds" kept as number
  - "hundreds of gigabytes" and "close to a billion" translated with Arabic numerals

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
