# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.88
**Glossary Terms Used:** consistent replication (النسخ المتماثل المتسق), external consistency (الاتساق الخارجي), snapshot isolation (عزل اللقطة), concurrency control (التحكم في التزامن), two-phase commit (التنفيذ ثنائي المرحلة), distributed transactions (المعاملات الموزعة)

---

### English Version

Consistent replication across datacenters as a storage service has been provided by Megastore [5] and DynamoDB [3]. DynamoDB presents a key-value interface, and only replicates within a region. Spanner follows Megastore in providing a semi-relational data model, and even a similar schema language. Megastore does not achieve high performance. It is layered on top of Bigtable, which imposes high communication costs. It also does not support long-lived leaders: multiple replicas may initiate writes. All writes from different replicas necessarily conflict in the Paxos protocol, even if they do not logically conflict: throughput collapses on a Paxos group at several writes per second. Spanner provides higher performance, general-purpose transactions, and external consistency.

Pavlo et al. [31] have compared the performance of databases and MapReduce [12]. They point to several other efforts that have been made to explore database functionality layered on distributed key-value stores [1, 4, 7, 41] as evidence that the two worlds are converging. We agree with the conclusion, but demonstrate that integrating multiple layers has its advantages: integrating concurrency control with replication reduces the cost of commit wait in Spanner, for example.

The notion of layering transactions on top of a replicated store dates at least as far back as Gifford's dissertation [16]. Scatter [17] is a recent DHT-based key-value store that layers transactions on top of consistent replication. Spanner focuses on providing a higher-level interface than Scatter does. Gray and Lamport [18] describe a non-blocking commit protocol based on Paxos. Their protocol incurs more messaging costs than two-phase commit, which would aggravate the cost of commit over widely distributed groups. Walter [36] provides a variant of snapshot isolation that works within, but not across datacenters. In contrast, our read-only transactions provide a more natural semantics, because we support external consistency over all operations.

There has been a spate of recent work on reducing or eliminating locking overheads. Calvin [40] eliminates concurrency control: it pre-assigns timestamps and then executes the transactions in timestamp order. H-Store [39] and Granola [11] each supported their own classification of transaction types, some of which could avoid locking. None of these systems provides external consistency. Spanner addresses the contention issue by providing support for snapshot isolation.

VoltDB [42] is a sharded in-memory database that supports master-slave replication over the wide area for disaster recovery, but not more general replication configurations. It is an example of what has been called NewSQL, which is a marketplace push to support scalable SQL [38]. A number of commercial databases implement reads in the past, such as MarkLogic [26] and Oracle's Total Recall [30]. Lomet and Li [24] describe an implementation strategy for such a temporal database.

Farsite derived bounds on clock uncertainty (much looser than TrueTime's) relative to a trusted clock reference [13]: server leases in Farsite were maintained in the same way that Spanner maintains Paxos leases. Loosely synchronized clocks have been used for concurrency-control purposes in prior work [2, 23]. We have shown that TrueTime lets one reason about global time across sets of Paxos state machines.

---

### النسخة العربية

تم توفير النسخ المتماثل المتسق عبر مراكز البيانات كخدمة تخزين بواسطة Megastore [5] و DynamoDB [3]. يقدم DynamoDB واجهة مفتاح-قيمة، ويكرر فقط داخل منطقة. تتبع سبانر Megastore في توفير نموذج بيانات شبه علائقي، وحتى لغة مخطط مماثلة. لا يحقق Megastore أداءً عالياً. إنه مطبق على طبقات فوق Bigtable، مما يفرض تكاليف اتصال عالية. كما أنه لا يدعم القادة طويلي العمر: قد تبدأ نسخ متعددة الكتابات. تتعارض جميع الكتابات من نسخ مختلفة بالضرورة في بروتوكول باكسوس، حتى لو لم تتعارض منطقياً: تنهار الإنتاجية على مجموعة باكسوس عند عدة كتابات في الثانية. توفر سبانر أداءً أعلى ومعاملات ذات أغراض عامة واتساقاً خارجياً.

قارن Pavlo وآخرون [31] أداء قواعد البيانات و MapReduce [12]. يشيرون إلى عدة جهود أخرى بُذلت لاستكشاف وظائف قاعدة البيانات المطبقة على طبقات فوق مخازن المفتاح-القيمة الموزعة [1، 4، 7، 41] كدليل على أن العالمين يتقاربان. نتفق مع الاستنتاج، لكننا نوضح أن دمج طبقات متعددة له مزاياه: يقلل دمج التحكم في التزامن مع النسخ المتماثل من تكلفة انتظار التنفيذ في سبانر، على سبيل المثال.

تعود فكرة تطبيق المعاملات على طبقات فوق مخزن منسوخ على الأقل إلى أطروحة Gifford [16]. Scatter [17] هو مخزن مفتاح-قيمة حديث قائم على DHT يطبق المعاملات على طبقات فوق النسخ المتماثل المتسق. تركز سبانر على توفير واجهة مستوى أعلى من Scatter. يصف Gray و Lamport [18] بروتوكول تنفيذ غير محجوب يعتمد على باكسوس. يتكبد بروتوكولهما تكاليف مراسلة أكثر من التنفيذ ثنائي المرحلة، مما سيؤدي إلى تفاقم تكلفة التنفيذ عبر المجموعات الموزعة على نطاق واسع. يوفر Walter [36] نوعاً مختلفاً من عزل اللقطة يعمل داخل مراكز البيانات، لكن ليس عبرها. على النقيض من ذلك، توفر معاملات القراءة فقط الخاصة بنا دلالات أكثر طبيعية، لأننا ندعم الاتساق الخارجي عبر جميع العمليات.

كانت هناك موجة من الأعمال الحديثة حول تقليل أو إزالة حمل الأقفال الزائد. يزيل Calvin [40] التحكم في التزامن: يعين طوابع زمنية مسبقاً ثم ينفذ المعاملات بترتيب الطابع الزمني. دعم كل من H-Store [39] و Granola [11] تصنيفهما الخاص لأنواع المعاملات، يمكن لبعضها تجنب القفل. لا يوفر أي من هذه الأنظمة الاتساق الخارجي. تتناول سبانر قضية التنازع من خلال توفير دعم لعزل اللقطة.

VoltDB [42] هي قاعدة بيانات مجزأة في الذاكرة تدعم النسخ المتماثل سيد-عبد عبر المنطقة الواسعة للتعافي من الكوارث، ولكن ليس تكوينات نسخ متماثل أكثر عمومية. إنها مثال على ما يسمى NewSQL، وهو دفع السوق لدعم SQL القابل للتوسع [38]. يُنفذ عدد من قواعد البيانات التجارية القراءات في الماضي، مثل MarkLogic [26] و Total Recall من Oracle [30]. يصف Lomet و Li [24] استراتيجية تنفيذ لمثل هذه قاعدة البيانات الزمنية.

اشتق Farsite حدوداً على عدم اليقين في الساعة (أكثر فضفاضة بكثير من TrueTime) بالنسبة لمرجع ساعة موثوق [13]: تم الحفاظ على عقود إيجار الخادم في Farsite بنفس الطريقة التي تحافظ بها سبانر على عقود إيجار باكسوس. تم استخدام الساعات المتزامنة بشكل فضفاض لأغراض التحكم في التزامن في العمل السابق [2، 23]. لقد أظهرنا أن TrueTime يتيح التفكير في الوقت العالمي عبر مجموعات من آلات حالة باكسوس.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - NewSQL (NewSQL)
  - Temporal database (قاعدة بيانات زمنية)
  - DHT (جدول التجزئة الموزع)
  - Master-slave replication (النسخ المتماثل سيد-عبد)
- **Equations:** 0
- **Citations:** [1], [2], [3], [4], [5], [7], [11], [12], [13], [16], [17], [18], [23], [24], [26], [30], [31], [36], [38], [39], [40], [41], [42]
- **Special handling:**
  - System names kept in English: Megastore, DynamoDB, Bigtable, Scatter, Calvin, H-Store, Granola, VoltDB, MarkLogic, Oracle Total Recall, Farsite
  - "NewSQL" kept as proper term

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.93
- Readability: 0.86
- Glossary consistency: 0.95
- **Overall section score:** 0.88
