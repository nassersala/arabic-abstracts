# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** database (قاعدة بيانات), distributed (موزع), Paxos (باكسوس), replication (النسخ المتماثل), consistency (اتساق), transactions (معاملات), sharding (التجزئة), failover (التحويل التلقائي عند الفشل), latency (زمن الانتقال), schema (مخطط)

---

### English Version

Spanner is a scalable, globally-distributed database designed, built, and deployed at Google. At the highest level of abstraction, it is a database that shards data across many sets of Paxos [21] state machines in datacenters spread all over the world. Replication is used for global availability and geographic locality; clients automatically failover between replicas. Spanner automatically reshards data across machines as the amount of data or the number of servers changes, and it automatically migrates data across machines (even across datacenters) to balance load and in response to failures. Spanner is designed to scale up to millions of machines across hundreds of datacenters and trillions of database rows.

Applications can use Spanner for high availability, even in the face of wide-area natural disasters, by replicating their data within or even across continents. Our initial customer was F1 [35], a rewrite of Google's advertising backend. F1 uses five replicas spread across the United States. Most other applications will probably replicate their data across 3 to 5 datacenters in one geographic region, but with relatively independent failure modes. That is, most applications will choose lower latency over higher availability, as long as they can survive 1 or 2 datacenter failures.

Spanner's main focus is managing cross-datacenter replicated data, but we have also spent a great deal of time in designing and implementing important database features on top of our distributed-systems infrastructure. Even though many projects happily use Bigtable [9], we have also consistently received complaints from users that Bigtable can be difficult to use for some kinds of applications: those that have complex, evolving schemas, or those that want strong consistency in the presence of wide-area replication. (Similar claims have been made by other authors [37].) Many applications at Google have chosen to use Megastore [5] because of its semi-relational data model and support for synchronous replication, despite its relatively poor write throughput. As a consequence, Spanner has evolved from a Bigtable-like versioned key-value store into a temporal multi-version database. Data is stored in schematized semi-relational tables; data is versioned, and each version is automatically timestamped with its commit time; old versions of data are subject to configurable garbage-collection policies; and applications can read data at old timestamps. Spanner supports general-purpose transactions, and provides a SQL-based query language.

As a globally-distributed database, Spanner provides several interesting features. First, the replication configurations for data can be dynamically controlled at a fine grain by applications. Applications can specify constraints to control which datacenters contain which data, how far data is from its users (to control read latency), how far replicas are from each other (to control write latency), and how many replicas are maintained (to control durability, availability, and read performance). Data can also be dynamically and transparently moved between datacenters by the system to balance resource usage across datacenters. Second, Spanner has two features that are difficult to implement in a distributed database: it provides externally consistent [16] reads and writes, and globally-consistent reads across the database at a timestamp. These features enable Spanner to support consistent backups, consistent MapReduce executions [12], and atomic schema updates, all at global scale, and even in the presence of ongoing transactions.

These features are enabled by the fact that Spanner assigns globally-meaningful commit timestamps to transactions, even though transactions may be distributed. The timestamps reflect serialization order. In addition, the serialization order satisfies external consistency (or equivalently, linearizability [20]): if a transaction T₁ commits before another transaction T₂ starts, then T₁'s commit timestamp is smaller than T₂'s. Spanner is the first system to provide such guarantees at global scale.

The key enabler of these properties is a new TrueTime API and its implementation. The API directly exposes clock uncertainty, and the guarantees on Spanner's timestamps depend on the bounds that the implementation provides. If the uncertainty is large, Spanner slows down to wait out that uncertainty. Google's cluster-management software provides an implementation of the TrueTime API. This implementation keeps uncertainty small (generally less than 10ms) by using multiple modern clock references (GPS and atomic clocks).

Section 2 describes the structure of Spanner's implementation, its feature set, and the engineering decisions that went into their design. Section 3 describes our new TrueTime API and sketches its implementation. Section 4 describes how Spanner uses TrueTime to implement externally-consistent distributed transactions, lock-free read-only transactions, and atomic schema updates. Section 5 provides some benchmarks on Spanner's performance and TrueTime behavior, and discusses the experiences of F1. Sections 6, 7, and 8 describe related and future work, and summarize our conclusions.

---

### النسخة العربية

سبانر (Spanner) هي قاعدة بيانات قابلة للتوسع وموزعة عالمياً تم تصميمها وبناؤها ونشرها في جوجل. على أعلى مستوى من التجريد، هي قاعدة بيانات تقوم بتجزئة البيانات عبر العديد من مجموعات آلات الحالة القائمة على باكسوس [21] في مراكز البيانات المنتشرة في جميع أنحاء العالم. يُستخدم النسخ المتماثل لتحقيق التوافر العالمي والقرب الجغرافي؛ حيث يتم التحويل التلقائي للعملاء بين النسخ المتماثلة عند الفشل. تعيد سبانر تجزئة البيانات تلقائياً عبر الأجهزة مع تغير كمية البيانات أو عدد الخوادم، وتقوم تلقائياً بترحيل البيانات عبر الأجهزة (حتى عبر مراكز البيانات) لموازنة الحمل واستجابةً للأعطال. صُممت سبانر للتوسع لتصل إلى ملايين الأجهزة عبر مئات مراكز البيانات وتريليونات من صفوف قواعد البيانات.

يمكن للتطبيقات استخدام سبانر لتحقيق التوافر العالي، حتى في مواجهة الكوارث الطبيعية واسعة النطاق، عن طريق نسخ بياناتها داخل القارات أو حتى عبرها. كان العميل الأولي لنا هو F1 [35]، وهو إعادة كتابة للواجهة الخلفية للإعلانات في جوجل. يستخدم F1 خمس نسخ متماثلة منتشرة عبر الولايات المتحدة. ستقوم معظم التطبيقات الأخرى على الأرجح بنسخ بياناتها عبر 3 إلى 5 مراكز بيانات في منطقة جغرافية واحدة، ولكن مع أنماط فشل مستقلة نسبياً. أي أن معظم التطبيقات ستختار زمن انتقال أقل على حساب التوافر الأعلى، طالما أنها يمكن أن تنجو من فشل مركز بيانات أو اثنين.

التركيز الرئيسي لسبانر هو إدارة البيانات المنسوخة عبر مراكز البيانات، لكننا قضينا أيضاً وقتاً طويلاً في تصميم وتنفيذ ميزات قاعدة بيانات مهمة فوق البنية التحتية للأنظمة الموزعة الخاصة بنا. على الرغم من أن العديد من المشاريع تستخدم Bigtable [9] بسعادة، إلا أننا تلقينا أيضاً شكاوى متسقة من المستخدمين بأن Bigtable يمكن أن يكون صعب الاستخدام لبعض أنواع التطبيقات: تلك التي لديها مخططات معقدة ومتطورة، أو تلك التي تريد اتساقاً قوياً في وجود النسخ المتماثل واسع النطاق. (تم تقديم ادعاءات مماثلة من قبل مؤلفين آخرين [37].) اختارت العديد من التطبيقات في جوجل استخدام Megastore [5] بسبب نموذج بياناته شبه العلائقي ودعمه للنسخ المتماثل المتزامن، على الرغم من إنتاجية الكتابة الضعيفة نسبياً. ونتيجة لذلك، تطورت سبانر من مخزن مفاتيح-قيم متعدد الإصدارات مشابه لـ Bigtable إلى قاعدة بيانات زمنية متعددة الإصدارات. تُخزن البيانات في جداول شبه علائقية ذات مخططات؛ وتكون البيانات متعددة الإصدارات، ويتم وضع طابع زمني تلقائي لكل إصدار بوقت التنفيذ الخاص به؛ وتخضع الإصدارات القديمة من البيانات لسياسات قابلة للتكوين لجمع القمامة؛ ويمكن للتطبيقات قراءة البيانات عند الطوابع الزمنية القديمة. تدعم سبانر المعاملات ذات الأغراض العامة، وتوفر لغة استعلام قائمة على SQL.

باعتبارها قاعدة بيانات موزعة عالمياً، توفر سبانر عدة ميزات مثيرة للاهتمام. أولاً، يمكن للتطبيقات التحكم الديناميكي في تكوينات النسخ المتماثل للبيانات بدقة عالية. يمكن للتطبيقات تحديد قيود للتحكم في مراكز البيانات التي تحتوي على البيانات، ومدى بُعد البيانات عن مستخدميها (للتحكم في زمن انتقال القراءة)، ومدى بُعد النسخ المتماثلة عن بعضها البعض (للتحكم في زمن انتقال الكتابة)، وعدد النسخ المتماثلة التي يتم الاحتفاظ بها (للتحكم في المتانة والتوافر وأداء القراءة). يمكن أيضاً نقل البيانات ديناميكياً وبشكل شفاف بين مراكز البيانات بواسطة النظام لموازنة استخدام الموارد عبر مراكز البيانات. ثانياً، تمتلك سبانر ميزتين يصعب تنفيذهما في قاعدة بيانات موزعة: فهي توفر قراءات وكتابات متسقة خارجياً [16]، وقراءات متسقة عالمياً عبر قاعدة البيانات عند طابع زمني محدد. تمكّن هذه الميزات سبانر من دعم النسخ الاحتياطية المتسقة، وتنفيذات MapReduce المتسقة [12]، والتحديثات الذرية للمخططات، كل ذلك على نطاق عالمي، وحتى في وجود معاملات جارية.

يتم تمكين هذه الميزات من خلال حقيقة أن سبانر تعين طوابع زمنية للتنفيذ ذات معنى عالمي للمعاملات، حتى لو كانت المعاملات موزعة. تعكس الطوابع الزمنية ترتيب التسلسل. بالإضافة إلى ذلك، يحقق ترتيب التسلسل الاتساق الخارجي (أو ما يعادله، الخطية [20]): إذا تم تنفيذ معاملة T₁ قبل أن تبدأ معاملة أخرى T₂، فإن الطابع الزمني للتنفيذ الخاص بـ T₁ يكون أصغر من الخاص بـ T₂. سبانر هي أول نظام يوفر مثل هذه الضمانات على نطاق عالمي.

المُمكِّن الرئيسي لهذه الخصائص هو واجهة برمجة تطبيقات TrueTime الجديدة وتنفيذها. تكشف الواجهة بشكل مباشر عن عدم اليقين في الساعات، وتعتمد الضمانات على الطوابع الزمنية لسبانر على الحدود التي يوفرها التنفيذ. إذا كان عدم اليقين كبيراً، تتباطأ سبانر للانتظار حتى ينتهي عدم اليقين هذا. توفر برمجيات إدارة العناقيد (cluster) في جوجل تنفيذاً لواجهة برمجة تطبيقات TrueTime. يحافظ هذا التنفيذ على عدم اليقين صغيراً (عادةً أقل من 10 ميللي ثانية) باستخدام مراجع ساعات حديثة متعددة (GPS والساعات الذرية).

يصف القسم 2 بنية تنفيذ سبانر، ومجموعة ميزاتها، والقرارات الهندسية التي دخلت في تصميمها. يصف القسم 3 واجهة برمجة تطبيقات TrueTime الجديدة ويرسم ملامح تنفيذها. يصف القسم 4 كيف تستخدم سبانر TrueTime لتنفيذ المعاملات الموزعة ذات الاتساق الخارجي، والمعاملات للقراءة فقط الخالية من الأقفال، والتحديثات الذرية للمخططات. يوفر القسم 5 بعض المعايير المرجعية حول أداء سبانر وسلوك TrueTime، ويناقش تجارب F1. تصف الأقسام 6 و 7 و 8 الأعمال ذات الصلة والأعمال المستقبلية، وتلخص استنتاجاتنا.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Paxos state machines (آلات الحالة القائمة على باكسوس)
  - Sharding/resharding (التجزئة/إعادة التجزئة)
  - Failover (التحويل التلقائي عند الفشل)
  - Geographic locality (القرب الجغرافي)
  - External consistency (الاتساق الخارجي)
  - Linearizability (الخطية)
  - Serialization order (ترتيب التسلسل)
  - Commit timestamp (الطابع الزمني للتنفيذ)
  - Clock uncertainty (عدم اليقين في الساعات)
  - Semi-relational tables (جداول شبه علائقية)
  - Garbage collection (جمع القمامة)
  - Atomic clocks (الساعات الذرية)
- **Equations:** 0
- **Citations:** [5], [9], [12], [16], [20], [21], [35], [37]
- **Special handling:**
  - Product names kept in English: Spanner, F1, Bigtable, Megastore, TrueTime, MapReduce
  - Technical subscripts preserved: T₁, T₂
  - GPS kept as-is (widely known acronym)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.85
- Glossary consistency: 0.95
- **Overall section score:** 0.88
