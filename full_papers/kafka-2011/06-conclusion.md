# Section 6: Conclusion and Future Works
## القسم 6: الخلاصة والأعمال المستقبلية

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** distributed system, messaging system, throughput, pull-based model, replication, stream processing

---

### English Version

We present a novel system called Kafka for processing huge volume of log data streams. Like a messaging system, Kafka employs a pull-based consumption model that allows an application to consume data at its own rate and rewind the consumption whenever needed. By focusing on log processing applications, Kafka achieves much higher throughput than conventional messaging systems. It also provides integrated distributed support and can scale out. We have been using Kafka successfully at LinkedIn for both offline and online applications. There are a number of directions that we'd like to pursue in the future. First, we plan to add built-in replication of messages across multiple brokers to allow durability and data availability guarantees even in the case of unrecoverable machine failures. We'd like to support both asynchronous and synchronous replication models to allow some tradeoff between producer latency and the strength of the guarantees provided. An application can choose the right level of redundancy based on its requirement on durability, availability and throughput. Second, we want to add some stream processing capability in Kafka. After retrieving messages from Kafka, real time applications often perform similar operations such as window-based counting and joining each message with records in a secondary store or with messages in another stream. At the lowest level this is supported by semantically partitioning messages on the join key during publishing so that all messages sent with a particular key go to the same partition and hence arrive at a single consumer process. This provides the foundation for processing distributed streams across a cluster of consumer machines. On top of this we feel a library of helpful stream utilities, such as different windowing functions or join techniques will be beneficial to this kind of applications.

---

### النسخة العربية

نقدم نظاماً جديداً يُسمى كافكا لمعالجة حجم هائل من تدفقات بيانات السجلات. مثل نظام المراسلة، يستخدم كافكا نموذج استهلاك قائم على السحب يسمح لتطبيق باستهلاك البيانات بمعدله الخاص وإرجاع الاستهلاك كلما دعت الحاجة. من خلال التركيز على تطبيقات معالجة السجلات، يحقق كافكا إنتاجية أعلى بكثير من أنظمة المراسلة التقليدية. كما أنه يوفر دعماً موزعاً متكاملاً ويمكنه التوسع. نستخدم كافكا بنجاح في لينكد إن للتطبيقات غير المتصلة والمتصلة على حد سواء. هناك عدد من الاتجاهات التي نود متابعتها في المستقبل. أولاً، نخطط لإضافة تكرار مدمج للرسائل عبر وسطاء متعددين للسماح بضمانات المتانة وتوافر البيانات حتى في حالة فشل الأجهزة غير القابل للاسترداد. نود دعم نماذج التكرار اللامتزامن والمتزامن للسماح ببعض المقايضة بين زمن استجابة المنتج وقوة الضمانات المقدمة. يمكن لتطبيق اختيار المستوى المناسب من التكرار بناءً على متطلباته في المتانة والتوافر والإنتاجية. ثانياً، نريد إضافة بعض قدرة معالجة التدفق في كافكا. بعد استرجاع الرسائل من كافكا، غالباً ما تؤدي تطبيقات الوقت الفعلي عمليات مماثلة مثل العد القائم على النافذة وربط كل رسالة بسجلات في مخزن ثانوي أو برسائل في تدفق آخر. على أدنى مستوى، يتم دعم ذلك عن طريق تجزئة الرسائل دلالياً على مفتاح الربط أثناء النشر بحيث تذهب جميع الرسائل المرسلة بمفتاح معين إلى نفس القسم وبالتالي تصل إلى عملية مستهلك واحد. يوفر هذا الأساس لمعالجة التدفقات الموزعة عبر مجموعة من أجهزة المستهلك. علاوة على ذلك، نشعر أن مكتبة من أدوات التدفق المفيدة، مثل دوال النوافذ المختلفة أو تقنيات الربط ستكون مفيدة لهذا النوع من التطبيقات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Novel system: نظام جديد
  - Log data streams: تدفقات بيانات السجلات
  - Pull-based consumption model: نموذج استهلاك قائم على السحب
  - Rewind: إرجاع
  - Conventional messaging systems: أنظمة المراسلة التقليدية
  - Integrated distributed support: دعم موزع متكامل
  - Scale out: التوسع
  - Built-in replication: تكرار مدمج
  - Durability: متانة
  - Data availability guarantees: ضمانات توافر البيانات
  - Unrecoverable machine failures: فشل الأجهزة غير القابل للاسترداد
  - Asynchronous replication: التكرار اللامتزامن
  - Synchronous replication: التكرار المتزامن
  - Tradeoff: مقايضة
  - Producer latency: زمن استجابة المنتج
  - Redundancy: التكرار
  - Stream processing capability: قدرة معالجة التدفق
  - Real time applications: تطبيقات الوقت الفعلي
  - Window-based counting: العد القائم على النافذة
  - Joining: ربط
  - Secondary store: مخزن ثانوي
  - Semantically partitioning: تجزئة دلالياً
  - Join key: مفتاح الربط
  - Distributed streams: التدفقات الموزعة
  - Consumer machines: أجهزة المستهلك
  - Stream utilities: أدوات التدفق
  - Windowing functions: دوال النوافذ
  - Join techniques: تقنيات الربط

- **Citations:** None

- **Special handling:**
  - "Future work" section discusses planned features, translated in future tense
  - Technical concepts like replication models and stream processing explained clearly in Arabic

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
