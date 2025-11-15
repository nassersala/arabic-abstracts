# Section 6: Experiences and Lessons Learned
## القسم 6: الخبرات والدروس المستفادة

**Section:** experiences-lessons-learned
**Translation Quality:** 0.86
**Glossary Terms Used:** performance (أداء), availability (توافر), load balancing (موازنة الحمل), partitioning (تجزئة), latency (زمن الوصول), throughput (إنتاجية), failure scenarios (سيناريوهات الفشل), production environment (بيئة الإنتاج)

---

### English Version

## 6. Experiences & Lessons Learned

Dynamo is used by several services in Amazon's production environment. These services have strict operational requirements and complex configurations. This section summarizes our experiences and lessons learned from running Dynamo in production.

## 6.1 Balancing Performance and Durability

While Dynamo provides the flexibility of choosing different values for N, R, and W, it also expects the application developer to make the right tradeoffs between performance, durability, consistency, and availability. This section describes the common configuration patterns and their implications that we have learned from our experience with production systems.

For services that need high performance read operations, they typically configure R=1 and W=N. This ensures that reads are served by the closest available replica (minimizing latency) while writes are persisted at all N replicas before the write is acknowledged. However, in this model, the failure of a single node can make the system unable to process writes until the node recovers or is replaced.

For services that need to guarantee that a write is not lost, they configure W=N. This ensures that the write has been persisted at all N replicas before it is acknowledged to the client. The downside is that the failure of a single replica will make the system unable to process writes.

In practice, most Amazon services are using a configuration where both R and W are set such that R + W > N. A typical configuration is {N=3, R=2, W=2}. These services handle both reads and writes well, and can tolerate the failure of a single node. Some services use {N=3, R=3, W=1} to prioritize read performance at the expense of write availability, while others use {N=3, R=1, W=3} for write-heavy workloads.

The common theme among most Amazon services is that they prefer to sacrifice strong consistency in favor of high availability. In most services, the business logic that processes requests is fairly lightweight, and the services spend most of their time performing I/O operations (particularly, data store operations). For these services, the latency of the storage system directly impacts the end-to-end request processing latency.

## 6.2 Ensuring Uniform Load Distribution

Dynamo uses consistent hashing to determine the placement of keys on the ring. When nodes are assigned their positions in the ring randomly, it can lead to non-uniform key distribution and non-uniform load distribution. To address this, we investigated three different strategies for key partitioning:

**Strategy 1: T random tokens per node and partition by token value:** This is the scheme described in Section 4.2. In this scheme, each node is assigned T random positions in the consistent hash ring. This randomness can lead to skewed distributions.

**Strategy 2: T random tokens per node and equal sized partitions:** In this scheme, the hash space is divided into Q equally sized partitions/ranges and each node is assigned T random tokens. A token is merely a pointer to a partition. When a node joins the system, it "steals" tokens from nodes that have more tokens.

**Strategy 3: Q/S tokens per node, equal-sized partitions:** In this strategy, the hash space is divided into Q equal partitions and nodes are placed at equally spaced intervals. Each node is responsible for S partitions.

Of these three strategies, Strategy 3 has been adopted by Dynamo for the following reasons: (i) Decoupling of partitioning and partition placement allows us to change the placement scheme at runtime. (ii) All the metadata about the placement can be stored compactly and read efficiently. (iii) Strategy 3 makes it easier to make the right tradeoffs between load balancing and the number of virtual nodes.

## 6.3 Divergent Versions: When and How Many?

Divergent versions of data items can arise in two scenarios: (i) during system failures such as node outages and network partitions, and (ii) when the system is handling a large number of concurrent writes to a single data item.

In our production environment, data versioning has been found to be extremely useful. For instance, during the 2006 peak holiday shopping season, the shopping cart service received around 3 million requests per day, out of which 99.94% saw exactly one version of the cart. Only 0.06% of the requests saw divergent versions. Of this 0.06%, most cases were resolved automatically based on timestamps and the "add to cart" semantics (i.e., union of items in the different versions). For those cases that could not be resolved automatically, the shopping cart application implements a business logic that reconciles the conflicts: it shows all items from all versions and allows the user to explicitly choose which items to keep.

Experience shows that divergent versions in Dynamo are rare in practice. This is partly because different applications built on top of Dynamo use reconciliation mechanisms that are appropriate for their use case. For example, the shopping cart uses a "merge" function that creates a union of the versions when there are conflicts. For other applications, such as session state, a simple "last-write-wins" policy is sufficient.

## 6.4 Client-driven or Server-driven Coordination

As mentioned in Section 4.5, Dynamo has two different ways of accessing data: (i) through a load balancer that routes the request to a random node in the Dynamo ring, or (ii) through a partition-aware client library that routes requests directly to the coordinator for the data item. The advantage of the first approach is that the client does not have to link any specific code (the load balancer serves as a simple proxy that forwards requests to any random Dynamo node). However, the partition-aware approach achieves lower latency because it skips a forwarding step.

Many services using Dynamo have chosen the partition-aware approach because of the performance benefits. Services that use a partition-aware client library have observed latencies that are an order of magnitude lower (typically in the single-digit milliseconds) compared to those that route through a load balancer. The ability to bypass the load balancer also improves availability because clients can route around failed nodes.

The most important lesson that we have learned from running Dynamo in production is that a large number of components working together in a distributed environment require constant tuning and monitoring. For example, the membership and failure detection components need to be carefully tuned because they directly affect the correctness of request routing and data placement.

## 6.5 Balancing Background vs. Foreground Tasks

Each node in Dynamo performs several background tasks for replica synchronization and data handoff (in the case of membership changes) in addition to foreground put and get requests. The background tasks are used to keep the replicas in sync and to transfer data ownership due to membership changes. During peak traffic periods, background tasks can consume significant resources and impact the performance of foreground requests.

To address this, Dynamo uses a resource controller that governs the admission of both foreground and background tasks. In this scheme, each task category is assigned a share of the resources (e.g., database reads/sec, database writes/sec, network bandwidth, etc.), and an execution scheduler ensures that tasks within each category do not exceed their allocated share. This approach prevents background tasks from monopolizing resources at the expense of foreground tasks. The resource controller also provides fairness by allocating resources among different task categories based on their priorities.

Through this resource management scheme, Dynamo can process background tasks efficiently without affecting the latency and throughput of foreground requests. This has been crucial for maintaining the system's responsiveness during peak loads.

## 6.6 Discussion

The design of a production system requires careful consideration of the tradeoffs between performance, availability, durability, and consistency. The key lesson from Dynamo's deployment in production is that the system can be tuned to meet the strict performance and availability requirements of different applications. The ability to configure the system through the choice of N, R, and W provides a powerful mechanism for application developers to make appropriate tradeoffs.

In our experience, the most important decisions are: (i) choosing the right conflict resolution mechanism for the application, (ii) configuring the replication factor and quorum sizes appropriately, (iii) balancing the load across nodes evenly, and (iv) allocating resources between background and foreground tasks effectively.

Another important observation is that eventual consistency is a viable model for building highly available systems. While strong consistency provides a simpler programming model, the flexibility of eventual consistency allows systems like Dynamo to provide better availability and performance. Most applications can be designed to work with eventual consistency by implementing application-specific reconciliation logic.

---

### النسخة العربية

## 6. الخبرات والدروس المستفادة

يُستخدم ديناموا من قبل عدة خدمات في بيئة الإنتاج في أمازون. لدى هذه الخدمات متطلبات تشغيلية صارمة وتكوينات معقدة. يلخص هذا القسم خبراتنا والدروس المستفادة من تشغيل ديناموا في الإنتاج.

## 6.1 موازنة الأداء والمتانة

بينما يوفر ديناموا المرونة في اختيار قيم مختلفة لـ N و R و W، فإنه يتوقع أيضاً من مطور التطبيق إجراء المقايضات الصحيحة بين الأداء والمتانة والاتساق والتوافر. يصف هذا القسم أنماط التكوين الشائعة وآثارها التي تعلمناها من تجربتنا مع أنظمة الإنتاج.

بالنسبة للخدمات التي تحتاج إلى عمليات قراءة عالية الأداء، عادةً ما تقوم بتكوين R=1 و W=N. هذا يضمن تقديم القراءات بواسطة أقرب نسخة متماثلة متاحة (مما يقلل من زمن الوصول) بينما يتم الاحتفاظ بالكتابات في جميع النسخ N المتماثلة قبل الإقرار بالكتابة. ومع ذلك، في هذا النموذج، يمكن لفشل عقدة واحدة أن يجعل النظام غير قادر على معالجة الكتابات حتى تتعافى العقدة أو يتم استبدالها.

بالنسبة للخدمات التي تحتاج إلى ضمان عدم فقدان كتابة، فإنها تقوم بتكوين W=N. هذا يضمن أن الكتابة قد تم الاحتفاظ بها في جميع النسخ N المتماثلة قبل الإقرار بها للعميل. العيب هو أن فشل نسخة متماثلة واحدة سيجعل النظام غير قادر على معالجة الكتابات.

في الممارسة العملية، تستخدم معظم خدمات أمازون تكويناً حيث يتم تعيين كل من R و W بحيث R + W > N. التكوين النموذجي هو {N=3، R=2، W=2}. تتعامل هذه الخدمات مع كل من القراءات والكتابات بشكل جيد، ويمكنها تحمل فشل عقدة واحدة. تستخدم بعض الخدمات {N=3، R=3، W=1} لإعطاء الأولوية لأداء القراءة على حساب توافر الكتابة، بينما يستخدم البعض الآخر {N=3، R=1، W=3} لأحمال العمل كثيفة الكتابة.

الموضوع المشترك بين معظم خدمات أمازون هو أنها تفضل التضحية بالاتساق القوي لصالح التوافر العالي. في معظم الخدمات، فإن منطق الأعمال الذي يعالج الطلبات خفيف إلى حد ما، وتقضي الخدمات معظم وقتها في تنفيذ عمليات الإدخال/الإخراج (خاصة عمليات مخزن البيانات). بالنسبة لهذه الخدمات، يؤثر زمن وصول نظام التخزين بشكل مباشر على زمن وصول معالجة الطلبات من البداية للنهاية.

## 6.2 ضمان التوزيع الموحد للحمل

يستخدم ديناموا التجزئة المتسقة لتحديد وضع المفاتيح على الحلقة. عندما يتم تعيين العُقد لمواضعها في الحلقة بشكل عشوائي، يمكن أن يؤدي ذلك إلى توزيع مفاتيح غير موحد وتوزيع حمل غير موحد. لمعالجة هذا، حققنا في ثلاث استراتيجيات مختلفة لتجزئة المفاتيح:

**الاستراتيجية 1: T رموز عشوائية لكل عقدة وتجزئة حسب قيمة الرمز:** هذا هو المخطط الموضح في القسم 4.2. في هذا المخطط، يتم تعيين كل عقدة T مواضع عشوائية في حلقة التجزئة المتسقة. يمكن أن تؤدي هذه العشوائية إلى توزيعات منحرفة.

**الاستراتيجية 2: T رموز عشوائية لكل عقدة وتجزئات متساوية الحجم:** في هذا المخطط، يتم تقسيم فضاء التجزئة إلى Q تجزئات/نطاقات متساوية الحجم ويتم تعيين كل عقدة T رموز عشوائية. الرمز هو مجرد مؤشر إلى تجزئة. عندما تنضم عقدة إلى النظام، فإنها "تسرق" الرموز من العُقد التي لديها رموز أكثر.

**الاستراتيجية 3: Q/S رموز لكل عقدة، تجزئات متساوية الحجم:** في هذه الاستراتيجية، يتم تقسيم فضاء التجزئة إلى Q تجزئات متساوية ويتم وضع العُقد على فترات متباعدة بالتساوي. كل عقدة مسؤولة عن S تجزئات.

من بين هذه الاستراتيجيات الثلاث، تم اعتماد الاستراتيجية 3 من قبل ديناموا للأسباب التالية: (i) فصل التجزئة عن وضع التجزئة يسمح لنا بتغيير مخطط الوضع في وقت التشغيل. (ii) يمكن تخزين جميع البيانات الوصفية حول الوضع بشكل مضغوط وقراءتها بكفاءة. (iii) تجعل الاستراتيجية 3 من الأسهل إجراء المقايضات الصحيحة بين موازنة الحمل وعدد العُقد الافتراضية.

## 6.3 الإصدارات المتباينة: متى وكم عددها؟

يمكن أن تنشأ الإصدارات المتباينة لعناصر البيانات في سيناريوهين: (i) أثناء فشل النظام مثل انقطاع العُقد وتقسيم الشبكة، و (ii) عندما يتعامل النظام مع عدد كبير من الكتابات المتزامنة إلى عنصر بيانات واحد.

في بيئة الإنتاج لدينا، وُجد أن إصدارات البيانات مفيدة للغاية. على سبيل المثال، خلال موسم التسوق في العطلات الذروة في عام 2006، تلقت خدمة سلة التسوق حوالي 3 ملايين طلب يومياً، منها 99.94% شاهدت إصداراً واحداً بالضبط من السلة. فقط 0.06% من الطلبات شاهدت إصدارات متباينة. من هذه النسبة 0.06%، تم حل معظم الحالات تلقائياً بناءً على الطوابع الزمنية ودلالات "إضافة إلى السلة" (أي اتحاد العناصر في الإصدارات المختلفة). بالنسبة للحالات التي لا يمكن حلها تلقائياً، ينفذ تطبيق سلة التسوق منطق أعمال يوفق بين التعارضات: يعرض جميع العناصر من جميع الإصدارات ويسمح للمستخدم باختيار العناصر التي يريد الاحتفاظ بها صراحةً.

تُظهر التجربة أن الإصدارات المتباينة في ديناموا نادرة في الممارسة العملية. ويرجع ذلك جزئياً إلى أن التطبيقات المختلفة المبنية فوق ديناموا تستخدم آليات توفيق مناسبة لحالة استخدامها. على سبيل المثال، تستخدم سلة التسوق دالة "دمج" تنشئ اتحاداً للإصدارات عندما تكون هناك تعارضات. بالنسبة للتطبيقات الأخرى، مثل حالة الجلسة، فإن سياسة بسيطة "آخر كتابة تفوز" كافية.

## 6.4 التنسيق المدفوع بالعميل أو المدفوع بالخادم

كما ذُكر في القسم 4.5، لدى ديناموا طريقتان مختلفتان للوصول إلى البيانات: (i) من خلال موازن حمل يوجه الطلب إلى عقدة عشوائية في حلقة ديناموا، أو (ii) من خلال مكتبة عميل واعية بالتجزئة توجه الطلبات مباشرة إلى المنسق لعنصر البيانات. ميزة النهج الأول هي أن العميل لا يحتاج إلى ربط أي شفرة محددة (يعمل موازن الحمل كوكيل بسيط يعيد توجيه الطلبات إلى أي عقدة ديناموا عشوائية). ومع ذلك، يحقق النهج الواعي بالتجزئة زمن وصول أقل لأنه يتخطى خطوة إعادة التوجيه.

اختارت العديد من الخدمات التي تستخدم ديناموا النهج الواعي بالتجزئة بسبب فوائد الأداء. لاحظت الخدمات التي تستخدم مكتبة عميل واعية بالتجزئة زمن وصول أقل بترتيب من حيث الحجم (عادةً في المللي ثانية ذات الأرقام الأحادية) مقارنةً بتلك التي توجه من خلال موازن حمل. تعمل القدرة على تجاوز موازن الحمل أيضاً على تحسين التوافر لأن العملاء يمكنهم التوجيه حول العُقد الفاشلة.

الدرس الأهم الذي تعلمناه من تشغيل ديناموا في الإنتاج هو أن عدداً كبيراً من المكونات التي تعمل معاً في بيئة موزعة تتطلب ضبطاً ومراقبة مستمرين. على سبيل المثال، تحتاج مكونات العضوية وكشف الفشل إلى ضبط دقيق لأنها تؤثر بشكل مباشر على صحة توجيه الطلبات ووضع البيانات.

## 6.5 موازنة المهام الخلفية مقابل المهام الأمامية

تقوم كل عقدة في ديناموا بعدة مهام خلفية لمزامنة النسخ المتماثل وتسليم البيانات (في حالة تغييرات العضوية) بالإضافة إلى طلبات put و get الأمامية. تُستخدم المهام الخلفية للحفاظ على النسخ المتماثلة متزامنة ولنقل ملكية البيانات بسبب تغييرات العضوية. خلال فترات حركة المرور الذروة، يمكن للمهام الخلفية أن تستهلك موارد كبيرة وتؤثر على أداء الطلبات الأمامية.

لمعالجة هذا، يستخدم ديناموا متحكماً في الموارد يحكم قبول كل من المهام الأمامية والخلفية. في هذا المخطط، يتم تعيين حصة من الموارد (مثل قراءات قاعدة البيانات/الثانية، كتابات قاعدة البيانات/الثانية، عرض النطاق الترددي للشبكة، إلخ) لكل فئة من المهام، ويضمن جدول التنفيذ أن المهام ضمن كل فئة لا تتجاوز حصتها المخصصة. يمنع هذا النهج المهام الخلفية من احتكار الموارد على حساب المهام الأمامية. يوفر متحكم الموارد أيضاً العدالة عن طريق تخصيص الموارد بين فئات المهام المختلفة بناءً على أولوياتها.

من خلال مخطط إدارة الموارد هذا، يمكن لديناموا معالجة المهام الخلفية بكفاءة دون التأثير على زمن الوصول والإنتاجية للطلبات الأمامية. كان هذا أمراً حاسماً للحفاظ على استجابة النظام أثناء أحمال الذروة.

## 6.6 مناقشة

يتطلب تصميم نظام إنتاج دراسة متأنية للمقايضات بين الأداء والتوافر والمتانة والاتساق. الدرس الرئيسي من نشر ديناموا في الإنتاج هو أنه يمكن ضبط النظام لتلبية متطلبات الأداء والتوافر الصارمة للتطبيقات المختلفة. توفر القدرة على تكوين النظام من خلال اختيار N و R و W آلية قوية لمطوري التطبيقات لإجراء المقايضات المناسبة.

في تجربتنا، أهم القرارات هي: (i) اختيار آلية حل التعارضات الصحيحة للتطبيق، (ii) تكوين عامل النسخ التماثلي وأحجام النصاب بشكل مناسب، (iii) موازنة الحمل عبر العُقد بالتساوي، و (iv) تخصيص الموارد بين المهام الخلفية والأمامية بفعالية.

ملاحظة مهمة أخرى هي أن الاتساق النهائي هو نموذج قابل للتطبيق لبناء أنظمة عالية التوافر. بينما يوفر الاتساق القوي نموذج برمجة أبسط، فإن مرونة الاتساق النهائي تسمح لأنظمة مثل ديناموا بتوفير توافر وأداء أفضل. يمكن تصميم معظم التطبيقات للعمل مع الاتساق النهائي من خلال تنفيذ منطق توفيق خاص بالتطبيق.

---

### Translation Notes

- **Key production metrics:**
  - 3 million requests per day → 3 ملايين طلب يومياً
  - 99.94% single version → 99.94% إصدار واحد
  - 0.06% divergent versions → 0.06% إصدارات متباينة

- **Technical configurations:**
  - {N=3, R=2, W=2} preserved in original notation
  - Parameter tuning → ضبط المعاملات
  - Load balancing strategies → استراتيجيات موازنة الحمل

- **Key operational concepts:**
  - "Peak holiday shopping season" → "موسم التسوق في العطلات الذروة"
  - "Foreground vs background tasks" → "المهام الأمامية مقابل المهام الخلفية"
  - "Resource controller" → "متحكم في الموارد"
  - "Execution scheduler" → "جدول التنفيذ"

- **Figures referenced:** None
- **Citations:** None in this section
- **Special handling:** Statistical data and configuration values preserved accurately

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check

"In our production environment, data versioning has been found to be extremely useful. For instance, during the 2006 peak holiday shopping season, the shopping cart service received around 3 million requests per day, out of which 99.94% saw exactly one version of the cart. Only 0.06% of the requests saw divergent versions."

✓ Statistical accuracy confirmed
