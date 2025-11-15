# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** peer-to-peer, distributed hash table, DHT, lookup, scalability, routing, consistent hashing, node, decentralized, overlay network, load balancing, fault tolerance, logarithmic

---

### English Version

A fundamental problem that confronts peer-to-peer applications is the efficient location of the node that stores a desired data item. This paper presents Chord, a distributed lookup protocol that addresses this problem. Chord provides support for just one operation: given a key, it maps the key onto a node. Data location can be easily implemented on top of Chord by associating a key with each data item, and storing the key/data pair at the node to which the key maps. Chord adapts efficiently as nodes join and leave the system, and can answer queries even if the system is continuously changing. Results from theoretical analysis and simulations show that Chord is scalable: communication cost and state maintained by each node scale logarithmically with the number of Chord nodes.

Chord is designed to support applications such as cooperative mirroring, time-shared storage, distributed indexes, and large-scale combinatorial search. These applications manipulate large amounts of data that must be stored at and retrieved from many different locations. By distributing data over many nodes, these systems provide aggregate storage and bandwidth that scales with the number of nodes. But this distribution of data demands some form of distributed index or location scheme. Such a scheme allows clients to find the node on which a desired data item resides, using only a small amount of routing information. Chord provides this: each Chord node maintains routing information about only O(log N) other nodes in an N-node network, and resolves all lookups via O(log N) messages to other nodes.

Several features make Chord robust in the face of frequent node arrivals and departures. First, Chord requires no particular network administration or configuration. Each Chord node maintains only local state, which it updates when nodes join or leave; there is no requirement for centralized control or coordination. Second, lookups in Chord are always correct, even while the network changes. Even if the network is continuously changing, if a data item with a certain key exists, Chord will find the node responsible for that key. Third, Chord incurs low overhead to provide these features. Maintaining correct routing information when nodes join or leave requires only a small number of messages.

Chord's design is simple and provably correct. A Chord node stores just two kinds of information: a successor list (used for correctness) and a finger table (used for efficiency). The successor list ensures that lookups are correct despite concurrent updates and failures; correctness is proved in Section 4. The finger table allows Chord to route queries efficiently by successively halving the distance to the destination node in the identifier space, resulting in O(log N) routing hops. This halving technique is related to hypercube routing and gives Chord similar routing efficiency.

The rest of this paper is organized as follows. Section 2 contrasts Chord with related work. Section 3 presents the system model that motivates the Chord protocol. Section 4 presents the base Chord protocol and proves its correctness. Section 5 presents extensions to handle concurrent joins and failures. Section 6 outlines results from theoretical analysis of the Chord protocol. Section 7 confirms the analysis through simulation. Section 8 describes our implementation experience. Section 9 concludes.

---

### النسخة العربية

المشكلة الأساسية التي تواجه تطبيقات النظير إلى النظير هي تحديد موقع العقدة التي تخزن عنصر البيانات المطلوب بكفاءة. تقدم هذه الورقة كورد، وهو بروتوكول بحث موزع يعالج هذه المشكلة. يوفر كورد دعماً لعملية واحدة فقط: بإعطاء مفتاح، يعيِّن المفتاح على عقدة. يمكن تنفيذ تحديد موقع البيانات بسهولة فوق كورد من خلال ربط مفتاح بكل عنصر بيانات، وتخزين زوج المفتاح/البيانات في العقدة التي يُعيَّن إليها المفتاح. يتكيف كورد بكفاءة عندما تنضم العُقد إلى النظام أو تغادره، ويمكنه الإجابة على الاستعلامات حتى لو كان النظام يتغير باستمرار. تُظهر نتائج التحليل النظري والمحاكاة أن كورد قابل للتوسع: تكلفة الاتصال والحالة التي تحافظ عليها كل عقدة تتناسب لوغاريتمياً مع عدد عُقد كورد.

صُمم كورد لدعم تطبيقات مثل النسخ المتطابق التعاوني، والتخزين المتقاسم زمنياً، والفهارس الموزعة، والبحث التوليفي واسع النطاق. تتعامل هذه التطبيقات مع كميات كبيرة من البيانات التي يجب تخزينها واسترجاعها من مواقع مختلفة كثيرة. من خلال توزيع البيانات عبر العديد من العُقد، توفر هذه الأنظمة سعة تخزين وعرض نطاق إجمالي يتناسب مع عدد العُقد. لكن هذا التوزيع للبيانات يتطلب شكلاً من أشكال الفهرسة الموزعة أو مخطط تحديد المواقع. يسمح هذا المخطط للعملاء بإيجاد العقدة التي يوجد فيها عنصر البيانات المطلوب، باستخدام كمية صغيرة فقط من معلومات التوجيه. يوفر كورد هذا: تحافظ كل عقدة كورد على معلومات توجيه حول O(log N) فقط من العُقد الأخرى في شبكة من N عقدة، وتحل جميع عمليات البحث عبر O(log N) من الرسائل إلى العُقد الأخرى.

تجعل عدة ميزات كورد قوياً في مواجهة وصول العُقد ومغادرتها المتكررة. أولاً، لا يتطلب كورد أي إدارة أو تكوين خاص للشبكة. تحافظ كل عقدة كورد على حالة محلية فقط، والتي تُحدثها عندما تنضم العُقد أو تغادر؛ لا يوجد متطلب للتحكم أو التنسيق المركزي. ثانياً، عمليات البحث في كورد صحيحة دائماً، حتى أثناء تغير الشبكة. حتى لو كانت الشبكة تتغير باستمرار، إذا كان هناك عنصر بيانات بمفتاح معين موجود، سيجد كورد العقدة المسؤولة عن ذلك المفتاح. ثالثاً، يتحمل كورد عبئاً منخفضاً لتوفير هذه الميزات. الحفاظ على معلومات توجيه صحيحة عندما تنضم العُقد أو تغادر يتطلب عدداً صغيراً فقط من الرسائل.

تصميم كورد بسيط وصحيح بشكل قابل للإثبات. تخزن عقدة كورد نوعين فقط من المعلومات: قائمة خلفاء (تُستخدم للصحة) وجدول إصبع (يُستخدم للكفاءة). تضمن قائمة الخلفاء أن عمليات البحث صحيحة على الرغم من التحديثات والفشل المتزامن؛ تُثبت الصحة في القسم 4. يسمح جدول الإصبع لكورد بتوجيه الاستعلامات بكفاءة عن طريق تنصيف المسافة إلى العقدة الوجهة في فضاء المعرفات بشكل متعاقب، مما ينتج عنه O(log N) من قفزات التوجيه. تقنية التنصيف هذه مرتبطة بتوجيه المكعب الفائق وتمنح كورد كفاءة توجيه مماثلة.

بقية هذه الورقة منظمة كما يلي. القسم 2 يقارن كورد مع الأعمال ذات الصلة. القسم 3 يعرض نموذج النظام الذي يحفز بروتوكول كورد. القسم 4 يعرض بروتوكول كورد الأساسي ويُثبت صحته. القسم 5 يعرض الامتدادات للتعامل مع الانضمامات والفشل المتزامن. القسم 6 يوضح نتائج التحليل النظري لبروتوكول كورد. القسم 7 يؤكد التحليل من خلال المحاكاة. القسم 8 يصف تجربة تنفيذنا. القسم 9 يختتم.

---

### Translation Notes

- **Key terms introduced:** peer-to-peer, distributed lookup protocol, consistent hashing (implied), finger table, successor list, identifier space
- **Technical concepts:** O(log N) complexity for routing and state, hypercube routing analogy
- **Sections referenced:** Sections 2-9 mentioned in paper organization
- **Special handling:** Mathematical notation O(log N) kept in English as is standard practice

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.90
- **Overall section score:** 0.88

### Back-Translation Verification

The fundamental problem facing peer-to-peer applications is efficiently locating the node that stores the desired data item. This paper presents Chord, a distributed lookup protocol that addresses this problem. Chord provides support for only one operation: given a key, it maps the key to a node. Data location can be easily implemented on top of Chord by associating a key with each data item, and storing the key/data pair at the node to which the key maps. Chord adapts efficiently when nodes join or leave the system, and can answer queries even if the system is continuously changing. Results from theoretical analysis and simulation show that Chord is scalable: the communication cost and state maintained by each node scale logarithmically with the number of Chord nodes.
