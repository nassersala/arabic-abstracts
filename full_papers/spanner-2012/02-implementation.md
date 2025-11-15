# Section 2: Implementation
## القسم 2: التنفيذ

**Section:** implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** zone (منطقة), tablet (لوحة), Paxos (باكسوس), replication (النسخ المتماثل), directory (دليل), schema (مخطط), sharding (التجزئة), transaction manager (مدير المعاملات), lock table (جدول الأقفال), two-phase commit (التنفيذ ثنائي المرحلة)

---

### English Version

This section describes the structure of and rationale underlying Spanner's implementation. It then describes the directory abstraction, which is used to manage replication and locality, and is the unit of data movement. Finally, it describes our data model, why Spanner looks like a relational database instead of a key-value store, and how applications can control data locality.

A Spanner deployment is called a universe. Given that Spanner manages data globally, there will be only a handful of running universes. We currently run a test/playground universe, a development/production universe, and a production-only universe.

Spanner is organized as a set of zones, where each zone is the rough analog of a deployment of Bigtable servers [9]. Zones are the unit of administrative deployment. The set of zones is also the set of locations across which data can be replicated. Zones can be added to or removed from a running system as new datacenters are brought into service and old ones are turned off, respectively. Zones are also the unit of physical isolation: there may be one or more zones in a datacenter, for example, if different applications' data must be partitioned across different sets of servers in the same datacenter.

Figure 1 illustrates the servers in a Spanner universe. A zone has one zonemaster and between one hundred and several thousand spanservers. The former assigns data to spanservers; the latter serve data to clients. The per-zone location proxies are used by clients to locate the spanservers assigned to serve their data. The universe master and the placement driver are currently singletons. The universe master is primarily a console that displays status information about all the zones for interactive debugging. The placement driver handles automated movement of data across zones on the timescale of minutes. The placement driver periodically communicates with the spanservers to find data that needs to be moved, either to meet updated replication constraints or to balance load. For space reasons, we will only describe the spanserver in any detail.

**2.1 Spanserver Software Stack**

This section focuses on the spanserver implementation to illustrate how replication and distributed transactions have been layered onto our Bigtable-based implementation. The software stack is shown in Figure 2. At the bottom, each spanserver is responsible for between 100 and 1000 instances of a data structure called a tablet. A tablet is similar to Bigtable's tablet abstraction, in that it implements a bag of the following mappings:

(key:string, timestamp:int64) → string

Unlike Bigtable, Spanner assigns timestamps to data, which is an important way in which Spanner is more like a multi-version database than a key-value store. A tablet's state is stored in set of B-tree-like files and a write-ahead log, all on a distributed file system called Colossus (the successor to the Google File System [15]).

To support replication, each spanserver implements a single Paxos state machine on top of each tablet. (An early Spanner incarnation supported multiple Paxos state machines per tablet, which allowed for more flexible replication configurations. The complexity of that design led us to abandon it.) Each state machine stores its metadata and log in its corresponding tablet. Our Paxos implementation supports long-lived leaders with time-based leader leases, whose length defaults to 10 seconds. The current Spanner implementation logs every Paxos write twice: once in the tablet's log, and once in the Paxos log. This choice was made out of expediency, and we are likely to remedy this eventually. Our implementation of Paxos is pipelined, so as to improve Spanner's throughput in the presence of WAN latencies; but writes are applied by Paxos in order (a fact on which we will depend in Section 4).

The Paxos state machines are used to implement a consistently replicated bag of mappings. The key-value mapping state of each replica is stored in its corresponding tablet. Writes must initiate the Paxos protocol at the leader; reads access state directly from the underlying tablet at any replica that is sufficiently up-to-date. The set of replicas is collectively a Paxos group.

At every replica that is a leader, each spanserver implements a lock table to implement concurrency control. The lock table contains the state for two-phase locking: it maps ranges of keys to lock states. (Note that having a long-lived Paxos leader is critical to efficiently managing the lock table.) In both Bigtable and Spanner, we designed for long-lived transactions (for example, for report generation, which might take on the order of minutes), which perform poorly under optimistic concurrency control in the presence of conflicts. Operations that require synchronization, such as transactional reads, acquire locks in the lock table; other operations bypass the lock table.

At every replica that is a leader, each spanserver also implements a transaction manager to support distributed transactions. The transaction manager is used to implement a participant leader; the other replicas in the group will be referred to as participant slaves. If a transaction involves only one Paxos group (as is the case for most transactions), it can bypass the transaction manager, since the lock table and Paxos together provide transactionality. If a transaction involves more than one Paxos group, those groups' leaders coordinate to perform two-phase commit. One of the participant groups is chosen as the coordinator: the participant leader of that group will be referred to as the coordinator leader, and the slaves of that group as coordinator slaves. The state of each transaction manager is stored in the underlying Paxos group (and therefore is replicated).

**2.2 Directories and Placement**

On top of the bag of key-value mappings, the Spanner implementation supports a bucketing abstraction called a directory, which is a set of contiguous keys that share a common prefix. (The choice of the term directory is a historical accident; a better term might be bucket.) We will explain the source of that prefix in Section 2.3. Supporting directories allows applications to control the locality of their data by choosing keys carefully.

A directory is the unit of data placement. All data in a directory has the same replication configuration. When data is moved between Paxos groups, it is moved directory by directory, as shown in Figure 3. Spanner might move a directory to shed load from a Paxos group; to put directories that are frequently accessed together into the same group; or to move a directory into a group that is closer to its accessors. Directories can be moved while client operations are ongoing. One could expect that a 50MB directory can be moved in a few seconds.

The fact that a Paxos group may contain multiple directories implies that a Spanner tablet is different from a Bigtable tablet: the former is not necessarily a single lexicographically contiguous partition of the row space. Instead, a Spanner tablet is a container that may encapsulate multiple partitions of the row space. We made this decision so that it would be possible to colocate multiple directories that are frequently accessed together.

Movedir is the background task used to move directories between Paxos groups [14]. Movedir is also used to add or remove replicas to Paxos groups [25], because Spanner does not yet support in-Paxos configuration changes. Movedir is not implemented as a single transaction, so as to avoid blocking ongoing reads and writes on a bulky data move. Instead, movedir registers the fact that it is starting to move data and moves the data in the background. When it has moved all but a nominal amount of the data, it uses a transaction to atomically move that nominal amount and update the metadata for the two Paxos groups.

A directory is also the smallest unit whose geographic-replication properties (or placement, for short) can be specified by an application. The design of our placement-specification language separates responsibilities for managing replication configurations. Administrators control two dimensions: the number and types of replicas, and the geographic placement of those replicas. They create a menu of named options in these two dimensions (e.g., North America, replicated 5 ways with 1 witness). An application controls how data is replicated, by tagging each database and/or individual directories with a combination of those options. For example, an application might store each end-user's data in its own directory, which would enable user A's data to have three replicas in Europe, and user B's data to have five replicas in North America.

For expository clarity we have over-simplified. In fact, Spanner will shard a directory into multiple fragments if it grows too large. Fragments may be served from different Paxos groups (and therefore different servers). Movedir actually moves fragments, and not whole directories, between groups.

**2.3 Data Model**

Spanner exposes the following set of data features to applications: a data model based on schematized semi-relational tables, a query language, and general-purpose transactions. The move towards supporting these features was driven by many factors. The need to support schematized semi-relational tables and synchronous replication is supported by the popularity of Megastore [5]. At least 300 applications within Google use Megastore (despite its relatively low performance) because its data model is simpler to manage than Bigtable's, and because of its support for synchronous replication across datacenters. (Bigtable only supports eventually-consistent replication across datacenters.) Examples of well-known Google applications that use Megastore are Gmail, Picasa, Calendar, Android Market, and AppEngine. The need to support a SQL-like query language in Spanner was also clear, given the popularity of Dremel [28] as an interactive data-analysis tool. Finally, the lack of cross-row transactions in Bigtable led to frequent complaints; Percolator [32] was in part built to address this failing. Some authors have claimed that general two-phase commit is too expensive to support, because of the performance or availability problems that it brings [9, 10, 19]. We believe it is better to have application programmers deal with performance problems due to overuse of transactions as bottlenecks arise, rather than always coding around the lack of transactions. Running two-phase commit over Paxos mitigates the availability problems.

The application data model is layered on top of the directory-bucketed key-value mappings supported by the implementation. An application creates one or more databases in a universe. Each database can contain an unlimited number of schematized tables. Tables look like relational-database tables, with rows, columns, and versioned values. We will not go into detail about the query language for Spanner. It looks like SQL with some extensions to support protocol-buffer-valued fields.

Spanner's data model is not purely relational, in that rows must have names. More precisely, every table is required to have an ordered set of one or more primary-key columns. This requirement is where Spanner still looks like a key-value store: the primary keys form the name for a row, and each table defines a mapping from the primary-key columns to the non-primary-key columns. A row has existence only if some value (even if it is NULL) is defined for the row's keys. Imposing this structure is useful because it lets applications control data locality through their choices of keys.

Figure 4 contains an example Spanner schema for storing photo metadata on a per-user, per-album basis. The schema language is similar to Megastore's, with the additional requirement that every Spanner database must be partitioned by clients into one or more hierarchies of tables. Client applications declare the hierarchies in database schemas via the INTERLEAVE IN declarations. The table at the top of a hierarchy is a directory table. Each row in a directory table with key K, together with all of the rows in descendant tables that start with K in lexicographic order, forms a directory. ON DELETE CASCADE says that deleting a row in the directory table deletes any associated child rows. The figure also illustrates the interleaved layout for the example database: for example, Albums(2,1) represents the row from the Albums table for user id 2, album id 1. This interleaving of tables to form directories is significant because it allows clients to describe the locality relationships that exist between multiple tables, which is necessary for good performance in a sharded, distributed database. Without it, Spanner would not know the most important locality relationships.

---

### النسخة العربية

يصف هذا القسم بنية التنفيذ الخاص بسبانر والأساس المنطقي الكامن وراءه. ثم يصف تجريد الدليل (directory)، الذي يُستخدم لإدارة النسخ المتماثل والموضعية، وهو وحدة حركة البيانات. وأخيراً، يصف نموذج البيانات الخاص بنا، ولماذا تبدو سبانر كقاعدة بيانات علائقية بدلاً من مخزن مفاتيح-قيم، وكيف يمكن للتطبيقات التحكم في موضعية البيانات.

يُطلق على نشر سبانر اسم "كون" (universe). نظراً لأن سبانر تدير البيانات عالمياً، سيكون هناك عدد قليل فقط من الأكوان قيد التشغيل. نقوم حالياً بتشغيل كون اختبار/تجريبي، وكون تطوير/إنتاج، وكون إنتاج فقط.

تنظم سبانر كمجموعة من المناطق (zones)، حيث تعتبر كل منطقة تقريباً مماثلة لنشر خوادم Bigtable [9]. المناطق هي وحدة النشر الإداري. مجموعة المناطق هي أيضاً مجموعة المواقع التي يمكن نسخ البيانات عبرها. يمكن إضافة المناطق أو إزالتها من نظام قيد التشغيل عند إدخال مراكز بيانات جديدة في الخدمة وإيقاف تشغيل القديمة، على التوالي. المناطق هي أيضاً وحدة العزل الفيزيائي: قد يكون هناك منطقة واحدة أو أكثر في مركز بيانات، على سبيل المثال، إذا كان يجب تقسيم بيانات التطبيقات المختلفة عبر مجموعات مختلفة من الخوادم في نفس مركز البيانات.

يوضح الشكل 1 الخوادم في كون سبانر. تحتوي المنطقة على سيد منطقة واحد (zonemaster) وما بين مئة وعدة آلاف من خوادم سبان (spanservers). يقوم الأول بتعيين البيانات لخوادم سبان؛ بينما يقدم الأخير البيانات للعملاء. يستخدم العملاء وكلاء الموقع لكل منطقة (per-zone location proxies) لتحديد موقع خوادم سبان المعينة لخدمة بياناتهم. سيد الكون (universe master) وبرنامج تشغيل التموضع (placement driver) هما حالياً مفردان (singletons). سيد الكون هو في المقام الأول وحدة تحكم تعرض معلومات الحالة حول جميع المناطق لتصحيح الأخطاء التفاعلي. يتعامل برنامج تشغيل التموضع مع الحركة التلقائية للبيانات عبر المناطق على مقياس زمني من الدقائق. يتواصل برنامج تشغيل التموضع بشكل دوري مع خوادم سبان للعثور على البيانات التي تحتاج إلى نقل، إما لتلبية قيود النسخ المتماثل المحدثة أو لموازنة الحمل. لأسباب تتعلق بالمساحة، سنصف خادم سبان فقط بالتفصيل.

**2.1 كومة برمجيات خادم سبان**

يركز هذا القسم على تنفيذ خادم سبان لتوضيح كيف تم وضع النسخ المتماثل والمعاملات الموزعة على شكل طبقات فوق تنفيذنا القائم على Bigtable. يظهر كومة البرمجيات في الشكل 2. في الأسفل، يكون كل خادم سبان مسؤولاً عن ما بين 100 و 1000 مثيل من بنية بيانات تسمى لوحة (tablet). اللوحة مشابهة لتجريد اللوحة في Bigtable، من حيث أنها تنفذ مجموعة من التعيينات التالية:

(key:string, timestamp:int64) → string

على عكس Bigtable، تعين سبانر طوابع زمنية للبيانات، وهي طريقة مهمة تجعل سبانر أقرب إلى قاعدة بيانات متعددة الإصدارات منها إلى مخزن مفاتيح-قيم. يتم تخزين حالة اللوحة في مجموعة من ملفات شبيهة بأشجار B وسجل كتابة مسبقة (write-ahead log)، كلها على نظام ملفات موزع يسمى Colossus (خليفة نظام ملفات جوجل [15]).

لدعم النسخ المتماثل، ينفذ كل خادم سبان آلة حالة باكسوس واحدة فوق كل لوحة. (دعم تجسيد مبكر لسبانر عدة آلات حالة باكسوس لكل لوحة، مما سمح بتكوينات نسخ متماثل أكثر مرونة. أدت تعقيدات هذا التصميم إلى التخلي عنه.) تخزن كل آلة حالة بياناتها الوصفية وسجلها في اللوحة المقابلة لها. يدعم تنفيذنا لباكسوس قادة طويلي العمر مع عقود إيجار قيادة قائمة على الوقت، يبلغ طولها الافتراضي 10 ثوانٍ. يسجل تنفيذ سبانر الحالي كل كتابة باكسوس مرتين: مرة في سجل اللوحة، ومرة في سجل باكسوس. تم اتخاذ هذا الاختيار من باب السرعة، ومن المحتمل أن نصلح هذا في النهاية. تنفيذنا لباكسوس مُنفَّذ بخطوط الأنابيب (pipelined)، لتحسين إنتاجية سبانر في وجود زمن انتقال شبكة المنطقة الواسعة (WAN)؛ ولكن يتم تطبيق الكتابات بواسطة باكسوس بالترتيب (حقيقة سنعتمد عليها في القسم 4).

تُستخدم آلات حالة باكسوس لتنفيذ مجموعة من التعيينات المنسوخة بشكل متسق. يتم تخزين حالة تعيين المفتاح-القيمة لكل نسخة في اللوحة المقابلة لها. يجب أن تبدأ الكتابات بروتوكول باكسوس عند القائد؛ تصل القراءات إلى الحالة مباشرة من اللوحة الأساسية في أي نسخة محدثة بما فيه الكفاية. مجموعة النسخ المتماثلة تشكل معاً مجموعة باكسوس.

في كل نسخة تكون قائدة، ينفذ كل خادم سبان جدول أقفال لتنفيذ التحكم في التزامن. يحتوي جدول الأقفال على الحالة للقفل ثنائي المرحلة: يعيّن نطاقات المفاتيح إلى حالات القفل. (لاحظ أن وجود قائد باكسوس طويل العمر أمر بالغ الأهمية لإدارة جدول الأقفال بكفاءة.) في كل من Bigtable وسبانر، صممنا لمعاملات طويلة العمر (على سبيل المثال، لتوليد التقارير، والتي قد تستغرق دقائق)، والتي تؤدي أداءً ضعيفاً تحت التحكم التفاؤلي في التزامن في وجود تعارضات. العمليات التي تتطلب المزامنة، مثل القراءات المعاملاتية، تحصل على أقفال في جدول الأقفال؛ تتجاوز العمليات الأخرى جدول الأقفال.

في كل نسخة تكون قائدة، ينفذ كل خادم سبان أيضاً مدير معاملات لدعم المعاملات الموزعة. يُستخدم مدير المعاملات لتنفيذ قائد مشارك؛ سيتم الإشارة إلى النسخ الأخرى في المجموعة كعبيد مشاركين. إذا كانت المعاملة تتضمن مجموعة باكسوس واحدة فقط (كما هو الحال في معظم المعاملات)، يمكنها تجاوز مدير المعاملات، حيث يوفر جدول الأقفال وباكسوس معاً المعاملاتية. إذا كانت المعاملة تتضمن أكثر من مجموعة باكسوس واحدة، تتنسق قادة تلك المجموعات لأداء التنفيذ ثنائي المرحلة. يتم اختيار إحدى مجموعات المشاركين كمنسق: سيتم الإشارة إلى القائد المشارك لتلك المجموعة كقائد المنسق، وعبيد تلك المجموعة كعبيد المنسق. يتم تخزين حالة كل مدير معاملات في مجموعة باكسوس الأساسية (وبالتالي يتم نسخها).

**2.2 الأدلة والتموضع**

فوق مجموعة تعيينات المفتاح-القيمة، يدعم تنفيذ سبانر تجريداً للتجميع يسمى دليل (directory)، وهو مجموعة من المفاتيح المتجاورة التي تشترك في بادئة مشتركة. (اختيار مصطلح دليل هو حادثة تاريخية؛ قد يكون مصطلح أفضل هو حاوية bucket.) سنشرح مصدر تلك البادئة في القسم 2.3. يسمح دعم الأدلة للتطبيقات بالتحكم في موضعية بياناتها عن طريق اختيار المفاتيح بعناية.

الدليل هو وحدة تموضع البيانات. جميع البيانات في الدليل لها نفس تكوين النسخ المتماثل. عندما يتم نقل البيانات بين مجموعات باكسوس، يتم نقلها دليلاً بدليل، كما هو موضح في الشكل 3. قد تنقل سبانر دليلاً للتخلص من الحمل من مجموعة باكسوس؛ لوضع أدلة يتم الوصول إليها بشكل متكرر معاً في نفس المجموعة؛ أو لنقل دليل إلى مجموعة أقرب إلى الوصول إليها. يمكن نقل الأدلة أثناء استمرار عمليات العميل. يمكن أن نتوقع أن دليل 50 ميجابايت يمكن نقله في بضع ثوانٍ.

حقيقة أن مجموعة باكسوس قد تحتوي على عدة أدلة تعني أن لوحة سبانر تختلف عن لوحة Bigtable: الأولى ليست بالضرورة قسماً واحداً متجاوراً معجمياً من فضاء الصفوف. بدلاً من ذلك، لوحة سبانر هي حاوية قد تحتوي على عدة أقسام من فضاء الصفوف. اتخذنا هذا القرار حتى يكون من الممكن وضع عدة أدلة يتم الوصول إليها بشكل متكرر معاً في نفس الموقع.

Movedir هي المهمة الخلفية المستخدمة لنقل الأدلة بين مجموعات باكسوس [14]. يُستخدم Movedir أيضاً لإضافة أو إزالة النسخ المتماثلة إلى مجموعات باكسوس [25]، لأن سبانر لا تدعم بعد تغييرات التكوين داخل باكسوس. لا يتم تنفيذ Movedir كمعاملة واحدة، لتجنب حجب القراءات والكتابات الجارية على نقل بيانات كبير. بدلاً من ذلك، يسجل movedir حقيقة أنه بدأ في نقل البيانات وينقل البيانات في الخلفية. عندما ينقل كل البيانات إلا كمية اسمية، يستخدم معاملة لنقل تلك الكمية الاسمية بشكل ذري وتحديث البيانات الوصفية لمجموعتي باكسوس.

الدليل هو أيضاً أصغر وحدة يمكن تحديد خصائص النسخ المتماثل الجغرافي (أو التموضع، باختصار) بواسطة تطبيق. يفصل تصميم لغة مواصفات التموضع الخاصة بنا المسؤوليات لإدارة تكوينات النسخ المتماثل. يتحكم المسؤولون في بعدين: عدد وأنواع النسخ المتماثلة، والتموضع الجغرافي لتلك النسخ. ينشئون قائمة من الخيارات المسماة في هذين البعدين (على سبيل المثال، أمريكا الشمالية، منسوخة 5 مرات مع شاهد واحد). يتحكم التطبيق في كيفية نسخ البيانات، عن طريق وضع علامة على كل قاعدة بيانات و/أو أدلة فردية بمزيج من تلك الخيارات. على سبيل المثال، قد يخزن تطبيق بيانات كل مستخدم نهائي في دليله الخاص، مما يمكّن بيانات المستخدم A من الحصول على ثلاث نسخ في أوروبا، وبيانات المستخدم B من الحصول على خمس نسخ في أمريكا الشمالية.

من أجل الوضوح التوضيحي، قمنا بالتبسيط المفرط. في الواقع، ستقوم سبانر بتجزئة دليل إلى عدة شظايا إذا كان كبيراً جداً. قد يتم تقديم الشظايا من مجموعات باكسوس مختلفة (وبالتالي خوادم مختلفة). في الواقع، ينقل Movedir الشظايا، وليس الأدلة بأكملها، بين المجموعات.

**2.3 نموذج البيانات**

تعرض سبانر مجموعة ميزات البيانات التالية للتطبيقات: نموذج بيانات يعتمد على جداول شبه علائقية ذات مخططات، ولغة استعلام، ومعاملات ذات أغراض عامة. كانت الحركة نحو دعم هذه الميزات مدفوعة بالعديد من العوامل. يتم دعم الحاجة إلى دعم جداول شبه علائقية ذات مخططات ونسخ متماثل متزامن من خلال شعبية Megastore [5]. تستخدم ما لا يقل عن 300 تطبيق داخل جوجل Megastore (على الرغم من أدائه المنخفض نسبياً) لأن نموذج بياناته أبسط في الإدارة من Bigtable، وبسبب دعمه للنسخ المتماثل المتزامن عبر مراكز البيانات. (يدعم Bigtable فقط النسخ المتماثل المتسق في النهاية عبر مراكز البيانات.) أمثلة على تطبيقات جوجل المعروفة التي تستخدم Megastore هي Gmail و Picasa و Calendar و Android Market و AppEngine. كانت الحاجة إلى دعم لغة استعلام شبيهة بـ SQL في سبانر واضحة أيضاً، نظراً لشعبية Dremel [28] كأداة تحليل بيانات تفاعلية. أخيراً، أدى عدم وجود معاملات عبر الصفوف في Bigtable إلى شكاوى متكررة؛ تم بناء Percolator [32] جزئياً لمعالجة هذا القصور. ادعى بعض المؤلفين أن التنفيذ ثنائي المرحلة العام مكلف جداً للدعم، بسبب مشاكل الأداء أو التوافر التي يجلبها [9، 10، 19]. نعتقد أنه من الأفضل أن يتعامل مبرمجو التطبيقات مع مشاكل الأداء بسبب الاستخدام المفرط للمعاملات عندما تنشأ الاختناقات، بدلاً من البرمجة دائماً حول عدم وجود معاملات. تشغيل التنفيذ ثنائي المرحلة فوق باكسوس يخفف من مشاكل التوافر.

يتم وضع نموذج بيانات التطبيق على شكل طبقات فوق تعيينات المفتاح-القيمة المجمعة في الأدلة التي يدعمها التنفيذ. ينشئ التطبيق واحدة أو أكثر من قواعد البيانات في الكون. يمكن أن تحتوي كل قاعدة بيانات على عدد غير محدود من الجداول ذات المخططات. تبدو الجداول مثل جداول قواعد البيانات العلائقية، مع صفوف وأعمدة وقيم متعددة الإصدارات. لن ندخل في تفاصيل حول لغة الاستعلام لسبانر. تبدو مثل SQL مع بعض الامتدادات لدعم حقول قيم مخزنات البروتوكول (protocol buffer).

نموذج بيانات سبانر ليس علائقياً بحتاً، من حيث أن الصفوف يجب أن يكون لها أسماء. بشكل أكثر دقة، يُطلب من كل جدول أن يحتوي على مجموعة مرتبة من عمود مفتاح أساسي واحد أو أكثر. هذا المتطلب هو المكان الذي لا تزال فيه سبانر تبدو مثل مخزن مفاتيح-قيم: تشكل المفاتيح الأساسية اسم الصف، ويحدد كل جدول تعييناً من أعمدة المفتاح الأساسي إلى الأعمدة غير الأساسية. للصف وجود فقط إذا تم تحديد قيمة (حتى لو كانت NULL) لمفاتيح الصف. فرض هذا الهيكل مفيد لأنه يتيح للتطبيقات التحكم في موضعية البيانات من خلال اختياراتها للمفاتيح.

يحتوي الشكل 4 على مثال على مخطط سبانر لتخزين بيانات الصور الوصفية على أساس كل مستخدم، كل ألبوم. لغة المخطط مماثلة لـ Megastore، مع المتطلب الإضافي بأن كل قاعدة بيانات سبانر يجب أن يتم تقسيمها بواسطة العملاء إلى تسلسل هرمي واحد أو أكثر من الجداول. تعلن تطبيقات العميل عن التسلسلات الهرمية في مخططات قواعد البيانات عبر تصريحات INTERLEAVE IN. الجدول في أعلى التسلسل الهرمي هو جدول الدليل. كل صف في جدول الدليل بمفتاح K، مع كل الصفوف في الجداول التابعة التي تبدأ بـ K بترتيب معجمي، يشكل دليلاً. ON DELETE CASCADE تعني أن حذف صف في جدول الدليل يحذف أي صفوف فرعية مرتبطة. يوضح الشكل أيضاً التخطيط المتداخل لقاعدة البيانات النموذجية: على سبيل المثال، Albums(2,1) يمثل الصف من جدول Albums للمستخدم id 2، الألبوم id 1. هذا التداخل للجداول لتشكيل الأدلة مهم لأنه يسمح للعملاء بوصف علاقات الموضعية الموجودة بين جداول متعددة، وهو أمر ضروري للأداء الجيد في قاعدة بيانات موزعة ومجزأة. بدونه، لن تعرف سبانر علاقات الموضعية الأكثر أهمية.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2, Figure 3, Figure 4
- **Key terms introduced:**
  - Universe (كون)
  - Zone (منطقة)
  - Spanserver (خادم سبان)
  - Zonemaster (سيد المنطقة)
  - Tablet (لوحة)
  - Paxos group (مجموعة باكسوس)
  - Lock table (جدول الأقفال)
  - Transaction manager (مدير المعاملات)
  - Two-phase locking (القفل ثنائي المرحلة)
  - Two-phase commit (التنفيذ ثنائي المرحلة)
  - Directory (دليل)
  - Placement (التموضع)
  - Colossus (كولوسوس)
  - Write-ahead log (سجل الكتابة المسبقة)
  - Leader leases (عقود إيجار القيادة)
  - Participant leader/slaves (قائد/عبيد المشارك)
  - Coordinator leader/slaves (قائد/عبيد المنسق)
  - INTERLEAVE IN (تصريح INTERLEAVE IN)
- **Equations:** 1 mapping notation
- **Citations:** [5], [9], [10], [14], [15], [19], [25], [28], [32]
- **Special handling:**
  - Product/system names kept in English: Bigtable, Colossus, Megastore, Dremel, Percolator, F1, Gmail, Picasa, Calendar, Android Market, AppEngine
  - SQL keywords kept in English: PRIMARY KEY, DIRECTORY, INTERLEAVE IN, ON DELETE CASCADE, NULL
  - Code/schema examples kept in original format

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.92
- Readability: 0.84
- Glossary consistency: 0.95
- **Overall section score:** 0.87
