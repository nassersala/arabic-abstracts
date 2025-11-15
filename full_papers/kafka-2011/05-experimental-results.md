# Section 5: Experimental Results
## القسم 5: النتائج التجريبية

**Section:** experimental-results
**Translation Quality:** 0.87
**Glossary Terms Used:** throughput, performance, benchmark, latency, distributed system

---

### English Version

We conducted an experimental study, comparing the performance of Kafka with Apache ActiveMQ v5.4 [1], a popular open-source implementation of JMS, and RabbitMQ v2.4 [16], a message system known for its performance. We used ActiveMQ's default persistent message store KahaDB. Although not presented here, we also tested an alternative AMQ message store and found its performance very similar to that of KahaDB. Whenever possible, we tried to use comparable settings in all systems.

We ran our experiments on 2 Linux machines, each with 8 2GHz cores, 16GB of memory, 6 disks with RAID 10. The two machines are connected with a 1Gb network link. One of the machines was used as the broker and the other machine was used as the producer or the consumer.

**Producer Test:** We configured the broker in all systems to asynchronously flush messages to its persistence store. For each system, we ran a single producer to publish a total of 10 million messages, each of 200 bytes. We configured the Kafka producer to send messages in batches of size 1 and 50. ActiveMQ and RabbitMQ don't seem to have an easy way to batch messages and we assume that it used a batch size of 1. The results are shown in Figure 4. The x-axis represents the amount of data sent to the broker over time in MB, and the y-axis corresponds to the producer throughput in messages per second. On average, Kafka can publish messages at the rate of 50,000 and 400,000 messages per second for batch size of 1 and 50, respectively. These numbers are orders of magnitude higher than that of ActiveMQ, and at least 2 times higher than RabbitMQ. There are a few reasons why Kafka performed much better. First, the Kafka producer currently doesn't wait for acknowledgements from the broker and sends messages as faster as the broker can handle. This significantly increased the throughput of the publisher. With a batch size of 50, a single Kafka producer almost saturated the 1Gb link between the producer and the broker. This is a valid optimization for the log aggregation case, as data must be sent asynchronously to avoid introducing any latency into the live serving of traffic. We note that without acknowledging the producer, there is no guarantee that every published message is actually received by the broker. For many types of log data, it is desirable to trade durability for throughput, as long as the number of dropped messages is relatively small. However, we do plan to address the durability issue for more critical data in the future. Second, Kafka has a more efficient storage format. On average, each message had an overhead of 9 bytes in Kafka, versus 144 bytes in ActiveMQ. This means that ActiveMQ was using 70% more space than Kafka to store the same set of 10 million messages. One overhead in ActiveMQ came from the heavy message header, required by JMS. Another overhead was the cost of maintaining various indexing structures. We observed that one of the busiest threads in ActiveMQ spent most of its time accessing a B-Tree to maintain message metadata and state. Finally, batching greatly improved the throughput by amortizing the RPC overhead. In Kafka, a batch size of 50 messages improved the throughput by almost an order of magnitude.

**Consumer Test:** In the second experiment, we tested the performance of the consumer. Again, for all systems, we used a single consumer to retrieve a total of 10 millions messages. We configured all systems so that each pull request should prefetch approximately the same amount data---up to 1000 messages or about 200KB. For both ActiveMQ and RabbitMQ, we set the consumer acknowledge mode to be automatic. Since all messages fit in memory, all systems were serving data from the page cache of the underlying file system or some in-memory buffers. The results are presented in Figure 5. On average, Kafka consumed 22,000 messages per second, more than 4 times that of ActiveMQ and RabbitMQ. We can think of several reasons. First, since Kafka has a more efficient storage format, fewer bytes were transferred from the broker to the consumer in Kafka. Second, the broker in both ActiveMQ and RabbitMQ had to maintain the delivery state of every message. We observed that one of the ActiveMQ threads was busy writing KahaDB pages to disks during this test. In contrast, there were no disk write activities on the Kafka broker. Finally, by using the sendfile API, Kafka reduces the transmission overhead.

We close the section by noting that the purpose of the experiment is not to show that other messaging systems are inferior to Kafka. After all, both ActiveMQ and RabbitMQ have more features than Kafka. The main point is to illustrate the potential performance gain that can be achieved by a specialized system.

---

### النسخة العربية

أجرينا دراسة تجريبية، مقارنين أداء كافكا مع Apache ActiveMQ v5.4 [1]، وهو تنفيذ مفتوح المصدر شائع لـ JMS، وRabbitMQ v2.4 [16]، وهو نظام رسائل معروف بأدائه. استخدمنا مخزن الرسائل الدائم الافتراضي لـ ActiveMQ وهو KahaDB. على الرغم من عدم تقديمها هنا، اختبرنا أيضاً مخزن رسائل AMQ البديل ووجدنا أن أداءه مشابه جداً لأداء KahaDB. كلما أمكن، حاولنا استخدام إعدادات قابلة للمقارنة في جميع الأنظمة.

أجرينا تجاربنا على جهازي لينكس، كل منهما يحتوي على 8 أنوية بسرعة 2 جيجاهرتز، و16 جيجابايت من الذاكرة، و6 أقراص مع RAID 10. يتصل الجهازان برابط شبكة 1 جيجابت. استُخدم أحد الأجهزة كوسيط واستُخدم الجهاز الآخر كمنتج أو مستهلك.

**اختبار المنتج:** قمنا بتكوين الوسيط في جميع الأنظمة لتفريغ الرسائل بشكل لامتزامن إلى مخزن الثبات الخاص به. لكل نظام، قمنا بتشغيل منتج واحد لنشر إجمالي 10 ملايين رسالة، كل منها بحجم 200 بايت. قمنا بتكوين منتج كافكا لإرسال رسائل على دفعات بحجم 1 و50. يبدو أن ActiveMQ وRabbitMQ ليس لديهما طريقة سهلة لتجميع الرسائل ونفترض أنهما استخدما حجم دفعة 1. تظهر النتائج في الشكل 4. يمثل المحور السيني كمية البيانات المرسلة إلى الوسيط بمرور الوقت بالميجابايت، ويتوافق المحور الصادي مع إنتاجية المنتج بالرسائل في الثانية. في المتوسط، يمكن لكافكا نشر رسائل بمعدل 50,000 و400,000 رسالة في الثانية لأحجام دفعات 1 و50، على التوالي. هذه الأرقام أكبر بمراتب من ActiveMQ، وأعلى بمرتين على الأقل من RabbitMQ. هناك بعض الأسباب التي جعلت كافكا يؤدي أفضل بكثير. أولاً، لا ينتظر منتج كافكا حالياً إقرارات من الوسيط ويرسل الرسائل بأسرع ما يمكن للوسيط التعامل معه. زاد هذا بشكل كبير من إنتاجية الناشر. بحجم دفعة 50، شبع منتج كافكا الواحد تقريباً رابط 1 جيجابت بين المنتج والوسيط. هذا تحسين صالح لحالة تجميع السجلات، حيث يجب إرسال البيانات بشكل لامتزامن لتجنب إدخال أي زمن استجابة في الخدمة المباشرة للحركة. نلاحظ أنه بدون إقرار المنتج، لا يوجد ضمان أن كل رسالة منشورة يتم استلامها فعلياً من قبل الوسيط. بالنسبة للعديد من أنواع بيانات السجلات، من المرغوب التضحية بالمتانة من أجل الإنتاجية، طالما أن عدد الرسائل المسقطة صغير نسبياً. ومع ذلك، نخطط لمعالجة مسألة المتانة للبيانات الأكثر أهمية في المستقبل. ثانياً، لدى كافكا صيغة تخزين أكثر كفاءة. في المتوسط، كان لكل رسالة عبء إضافي قدره 9 بايتات في كافكا، مقابل 144 بايت في ActiveMQ. هذا يعني أن ActiveMQ كان يستخدم مساحة أكبر بنسبة 70% من كافكا لتخزين نفس مجموعة الـ 10 ملايين رسالة. جاء أحد الأعباء الإضافية في ActiveMQ من رأس الرسالة الثقيل، المطلوب بواسطة JMS. عبء إضافي آخر كان تكلفة صيانة بنى الفهرسة المختلفة. لاحظنا أن أحد الخيوط الأكثر انشغالاً في ActiveMQ أمضى معظم وقته في الوصول إلى شجرة B للحفاظ على بيانات وحالة الرسالة الوصفية. أخيراً، حسّن التجميع الإنتاجية بشكل كبير من خلال إطفاء العبء الإضافي لـ RPC. في كافكا، حسّن حجم دفعة 50 رسالة الإنتاجية بما يقرب من مرتبة من الحجم.

**اختبار المستهلك:** في التجربة الثانية، اختبرنا أداء المستهلك. مرة أخرى، لجميع الأنظمة، استخدمنا مستهلكاً واحداً لاسترجاع إجمالي 10 ملايين رسالة. قمنا بتكوين جميع الأنظمة بحيث يجب أن يجلب كل طلب سحب مسبقاً تقريباً نفس كمية البيانات---حتى 1000 رسالة أو حوالي 200 كيلوبايت. بالنسبة لكل من ActiveMQ وRabbitMQ، قمنا بتعيين وضع إقرار المستهلك ليكون تلقائياً. نظراً لأن جميع الرسائل تتناسب مع الذاكرة، كانت جميع الأنظمة تقدم البيانات من ذاكرة التخزين المؤقت للصفحة لنظام الملفات الأساسي أو بعض المخازن المؤقتة في الذاكرة. تُعرض النتائج في الشكل 5. في المتوسط، استهلك كافكا 22,000 رسالة في الثانية، أكثر من 4 أضعاف ActiveMQ وRabbitMQ. يمكننا التفكير في عدة أسباب. أولاً، نظراً لأن كافكا لديه صيغة تخزين أكثر كفاءة، تم نقل بايتات أقل من الوسيط إلى المستهلك في كافكا. ثانياً، كان على الوسيط في كل من ActiveMQ وRabbitMQ الحفاظ على حالة التوصيل لكل رسالة. لاحظنا أن أحد خيوط ActiveMQ كان مشغولاً بكتابة صفحات KahaDB إلى الأقراص أثناء هذا الاختبار. على النقيض من ذلك، لم تكن هناك أنشطة كتابة قرص على وسيط كافكا. أخيراً، باستخدام واجهة برمجة تطبيقات sendfile، يقلل كافكا من العبء الإضافي للإرسال.

نختتم القسم بملاحظة أن الغرض من التجربة ليس إظهار أن أنظمة المراسلة الأخرى أدنى من كافكا. بعد كل شيء، يحتوي كل من ActiveMQ وRabbitMQ على ميزات أكثر من كافكا. النقطة الرئيسية هي توضيح الكسب المحتمل في الأداء الذي يمكن تحقيقه بواسطة نظام متخصص.

---

### Translation Notes

- **Figures referenced:** Figure 4 (Producer Performance), Figure 5 (Consumer Performance)
- **Key terms introduced:**
  - Experimental study: دراسة تجريبية
  - Performance comparison: مقارنة الأداء
  - Open-source: مفتوح المصدر
  - Persistent message store: مخزن الرسائل الدائم
  - Comparable settings: إعدادات قابلة للمقارنة
  - RAID 10: RAID 10 (kept as technical term)
  - Network link: رابط شبكة
  - Asynchronously flush: تفريغ لامتزامن
  - Persistence store: مخزن الثبات
  - Batch size: حجم دفعة
  - Throughput: إنتاجية
  - Messages per second: رسائل في الثانية
  - Orders of magnitude: مراتب
  - Acknowledgements: إقرارات
  - Publisher: الناشر
  - Saturated: شبع
  - Durability: متانة
  - Storage format: صيغة تخزين
  - Message overhead: عبء إضافي للرسالة
  - Message header: رأس الرسالة
  - Indexing structures: بنى الفهرسة
  - B-Tree: شجرة B
  - Metadata: بيانات وصفية
  - Amortizing: إطفاء
  - RPC overhead: العبء الإضافي لـ RPC
  - Prefetch: جلب مسبق
  - Acknowledge mode: وضع إقرار
  - Page cache: ذاكرة التخزين المؤقت للصفحة
  - In-memory buffers: المخازن المؤقتة في الذاكرة
  - Delivery state: حالة التوصيل
  - Disk write activities: أنشطة كتابة قرص
  - Transmission overhead: العبء الإضافي للإرسال
  - Specialized system: نظام متخصص

- **Citations:** [1], [16]

- **Special handling:**
  - Numbers (10 million, 200 bytes, 50,000, 400,000, etc.) kept in standard format
  - System names (Apache ActiveMQ, RabbitMQ, KahaDB, AMQ, JMS) kept in original form
  - Technical acronyms (RAID 10, RPC, JMS) kept in English
  - Performance metrics translated with units preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
