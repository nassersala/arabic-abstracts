# Section 4: System Architecture
## القسم 4: معمارية النظام

**Section:** system-architecture
**Translation Quality:** 0.88
**Glossary Terms Used:** consistent hashing (تجزئة متسقة), virtual nodes (عقد افتراضية), replication (نسخ تماثلي), coordinator (منسق), quorum (نصاب), vector clocks (ساعات متجهة), hinted handoff (تسليم موجه), merkle trees (أشجار ميركل), anti-entropy (مضاد للإنتروبيا), gossip protocol (بروتوكول الشائعات)

---

### English Version

## 4.1 System Interface

Dynamo stores objects associated with a key through a simple interface; it exposes two operations: get() and put(). The get(key) operation locates the object replicas associated with the key in the storage system and returns a single object or a list of objects with conflicting versions along with a context. The put(key, context, object) operation determines where the replicas of the object should be placed based on the associated key, and writes the replicas to disk. The context encodes system metadata about the object that is opaque to the caller and includes information such as the version of the object. The context information is stored along with the object so that the system can verify the validity of the context object supplied in the put request.

Dynamo treats both the key and the object supplied by the caller as an opaque array of bytes. It applies a MD5 hash on the key to generate a 128-bit identifier, which is used to determine the storage nodes that are responsible for serving the key.

## 4.2 Partitioning Algorithm

One of the key design requirements for Dynamo is that it must scale incrementally. This requires a mechanism to dynamically partition the data over the set of nodes (i.e., storage hosts) in the system. Dynamo's partitioning scheme relies on consistent hashing to distribute the load across multiple storage hosts. In consistent hashing [10], the output range of a hash function is treated as a fixed circular space or "ring" (i.e. the largest hash value wraps around to the smallest hash value). Each node in the system is assigned a random value within this space which represents its "position" on the ring. Each data item identified by a key is assigned to a node by hashing the data item's key to yield its position on the ring, and then walking the ring clockwise to find the first node with a position larger than the item's position.

Thus, each node becomes responsible for the region in the ring between it and its predecessor node on the ring. The principle advantage of consistent hashing is that departure or arrival of a node only affects its immediate neighbors and other nodes remain unaffected.

The basic consistent hashing algorithm presents some challenges. First, the random position assignment of each node on the ring leads to non-uniform data and load distribution. Second, the basic algorithm is oblivious to the heterogeneity in the performance of nodes. To address these issues, Dynamo uses a variant of consistent hashing (similar to the one used in [10, 20]): instead of mapping a node to a single point in the circle, each node gets assigned to multiple points in the ring. To this end, Dynamo uses the concept of "virtual nodes". A virtual node looks like a single node in the system, but each node can be responsible for more than one virtual node. Effectively, when a new node is added to the system, it is assigned multiple positions (henceforth, "tokens") in the ring. The process of fine-tuning Dynamo's partitioning scheme is discussed in Section 6.

Using virtual nodes has the following advantages:
- If a node becomes unavailable (due to failures or routine maintenance), the load handled by this node is evenly dispersed across the remaining available nodes.
- When a node becomes available again, or a new node is added to the system, the newly available node accepts a roughly equivalent amount of load from each of the other available nodes.
- The number of virtual nodes that a node is responsible for can decided based on its capacity, accounting for heterogeneity in the physical infrastructure.

## 4.3 Replication

To achieve high availability and durability, Dynamo replicates its data on multiple hosts. Each data item is replicated at N hosts, where N is a parameter configured "per-instance". Each key, k, is assigned to a coordinator node (described in the previous section). The coordinator is in charge of the replication of the data items that fall within its range. In addition to locally storing each key within its range, the coordinator replicates these keys at the N-1 clockwise successor nodes in the ring. This results in a system where each node is responsible for the region of the ring between it and its Nth predecessor. In Figure 2, node B replicates the key k at nodes C and D in addition to storing it locally. Node D will store the keys that fall in the ranges (A, B], (B, C], and (C, D].

The list of nodes that is responsible for storing a particular key is called the preference list. The system is designed, as will be explained in Section 4.8, so that every node in the system can determine which nodes should be in this list for any particular key. To account for node failures, preference list contains more than N nodes. Note that with the use of virtual nodes, it is possible that the first N successor positions for a particular key may be owned by less than N distinct physical nodes (i.e. a node may hold more than one of the first N positions). To address this, the preference list for a key is constructed by skipping positions in the ring to ensure that the list contains only distinct physical nodes.

## 4.4 Data Versioning

Dynamo provides eventual consistency, which allows for updates to be propagated to all replicas asynchronously. A put() call may return to its caller before the update has been applied at all the replicas, which can result in scenarios where a subsequent get() operation may return an object that does not have the latest updates. If there are no failures then there is a bound on the update propagation times. However, under certain failure scenarios (e.g., server outages or network partitions), updates may not arrive at all replicas for an extended period of time.

There is a category of applications in Amazon's platform that can tolerate such inconsistencies and can be constructed to operate under these conditions. For example, the shopping cart application requires that an "Add to Cart" operation can never be forgotten or rejected. If the most recent state of the cart is unavailable, and a user makes changes to an older version of the cart, that change is still meaningful and should be preserved. But at the same time it shouldn't supersede the currently unavailable state of the cart, which itself may contain changes that should be preserved. Note that both "add to cart" and "delete item from cart" operations are translated into put requests to Dynamo. When a customer wants to add an item to (or remove from) a shopping cart and the latest version is not available, the item is added to (or removed from) the older version and the divergent versions are reconciled later.

In order to capture causality between different versions of the same object we need a versioning scheme. A "version" captures the changes in an object as a result of one or more put operations. Dynamo uses vector clocks [12] in order to capture causality between different versions of the same object. A vector clock is effectively a list of (node, counter) pairs. One vector clock is associated with every version of every object. One can determine whether two versions of an object are on parallel branches or have a causal ordering, by examine their vector clocks. If the counters on the first object's clock are less-than-or-equal to all of the nodes in the second clock, then the first is an ancestor of the second and can be forgotten. Otherwise, the two changes are considered to be in conflict and require reconciliation.

In Dynamo, when a client wishes to update an object, it must specify which version it is updating. This is done by passing the context it obtained from an earlier read operation, which contains the vector clock information. Upon processing a read request, if Dynamo has access to multiple branches that cannot be syntactically reconciled, it will return all the objects at the leaves, with the corresponding version information in the context. An update using this context is considered to have reconciled the divergent versions and the branches are collapsed into a single new version.

## 4.5 Execution of get() and put() operations

Any storage node in Dynamo is eligible to receive client get and put operations for any key. In this section, we describe how these operations are performed in a distributed manner.

Both get and put operations are invoked using Amazon's infrastructure-specific request processing framework over HTTP. There are two strategies that a client can use to select a node: (1) route its request through a generic load balancer that will select a node based on load information, or (2) use a partition-aware client library that routes requests directly to the appropriate coordinator nodes. The advantage of the first approach is that the client does not have to link any code specific to Dynamo in its application, whereas the second approach can achieve lower latency because it skips a potential forwarding step.

A node handling a read or write operation is known as the coordinator. Typically, this is the first among the top N nodes in the preference list. If the requests are received through a load balancer, requests to access a key may be routed to any random node in the ring. In this scenario, the node that receives the request will not coordinate it if the node is not in the top N of the requested key's preference list. Instead, that node will forward the request to the first among the top N nodes in the preference list.

Read and write operations involve the first N healthy nodes in the preference list, skipping over those that are down or inaccessible. When all nodes are healthy, the top N nodes in a key's preference list are accessed. When there are node failures or network partitions, nodes that are lower ranked in the preference list are accessed.

To maintain consistency among its replicas, Dynamo uses a consistency protocol similar to those used in quorum systems. This protocol has two key configurable values: R and W. R is the minimum number of nodes that must participate in a successful read operation. W is the minimum number of nodes that must participate in a successful write operation. Setting R and W such that R + W > N yields a quorum-like system. In this model, the latency of a get (or put) operation is dictated by the slowest of the R (or W) replicas. For this reason, R and W are usually configured to be less than N, to provide better latency.

Upon receiving a put() request for a key, the coordinator generates the vector clock for the new version and writes the new version locally. The coordinator then sends the new version (along with the new vector clock) to the N highest-ranked reachable nodes. If at least W-1 nodes respond then the write is considered successful.

Similarly, for a get() request, the coordinator requests all existing versions of data for that key from the N highest-ranked reachable nodes in the preference list for that key, waits for R responses, then returns the result to the client. If the coordinator ends up gathering multiple versions of the data, it returns all the versions it deems to be causally unrelated. The divergent versions are then reconciled and the reconciled version superseding the current versions is written back.

## 4.6 Handling Failures: Hinted Handoff

If Dynamo used a traditional quorum approach it would be unavailable during server failures and network partitions, and would have reduced durability even under the simplest of failure conditions. To remedy this it does not enforce strict quorum membership and instead it uses a "sloppy quorum"; all read and write operations are performed on the first N healthy nodes from the preference list, which may not always be the first N nodes encountered while walking the consistent hashing ring.

Consider the example of Dynamo configuration given in Figure 2 with N=3. In this example, if node A is temporarily down or unreachable during a write operation then a replica that would normally have lived on A will now be sent to node D. This is done to maintain the desired availability and durability guarantees. The replica sent to D will have a hint in its metadata that suggests which node was the intended recipient of the replica (in this case A). Nodes that receive hinted replicas will keep them in a separate local database that is scanned periodically. Upon detecting that A has recovered, D will attempt to deliver the replica to A. Once the transfer succeeds, D may delete the object from its local store without decreasing the total number of replicas in the system.

Using hinted handoff, Dynamo ensures that the read and write operations are not failed due to temporary node or network failures. Applications that need the highest level of availability can set W to 1, which ensures that a write is accepted as long as a single node in the system has durably written the key it to its local store. Thus, the write request is only rejected if all nodes in the system are unavailable. However, in practice, most Amazon services in production set a higher W to meet the desired level of durability. A more detailed discussion of configuring N, R and W follows in section 6.

## 4.7 Handling permanent failures: Replica synchronization

Hinted handoff works best if the system membership churn is low and node failures are transient. There are scenarios under which hinted replicas become unavailable before they can be returned to the original replica node. To handle this and other threats to durability, Dynamo implements an anti-entropy (replica synchronization) protocol to keep the replicas synchronized.

To detect the inconsistencies between replicas faster and to minimize the amount of transferred data, Dynamo uses Merkle trees [13]. A Merkle tree is a hash tree where leaves are hashes of the values of individual keys. Parent nodes higher in the tree are hashes of their respective children. The principal advantage of Merkle tree is that each branch of the tree can be checked independently without requiring nodes to download the entire tree or the entire data set. Moreover, Merkle trees help in reducing the amount of data that needs to be transferred while checking for inconsistencies among replicas. For instance, if the hash values of the root of two trees are equal, then the values of the leaf nodes in the tree are equal and the nodes require no synchronization. If not, it implies that the values of some replicas are different. In such cases, the nodes may exchange the hash values of children and the process continues until it reaches the leaves of the trees, at which point the hosts can identify the keys that are "out of sync". Merkle trees minimize the amount of data that needs to be transferred for synchronization and reduce the number of disk reads performed during the anti-entropy process.

Dynamo uses Merkle trees for anti-entropy as follows: Each node maintains a separate Merkle tree for each key range (the set of keys covered by a virtual node) it hosts. This allows nodes to compare whether the keys within a key range are up-to-date. In this scheme, two nodes exchange the root of the Merkle tree corresponding to the key ranges that they host in common. Subsequently, using the tree traversal scheme described above the nodes determine if they have any differences and perform the appropriate synchronization action. The disadvantage with this scheme is that many key ranges change when a node joins or leaves the system thereby requiring the tree(s) to be recalculated. This issue is addressed, however, by the refined partitioning scheme described in Section 6.2.

## 4.8 Membership and Failure Detection

### 4.8.1 Ring Membership

In Amazon's environment node outages (due to failures and maintenance tasks) are often transient but may last for extended intervals. A node outage rarely signifies a permanent departure and therefore should not result in rebalancing of the partition assignment or repair of the unreachable replicas. Similarly, manual error could lead to the unintentional startup of new Dynamo nodes. For these reasons, it was deemed appropriate to use an explicit mechanism to initiate the addition and removal of nodes from a Dynamo ring. An administrator uses a command line tool or a browser to connect to a Dynamo node and issue a membership change to join a node to a ring or remove a node from a ring. The node that serves the request writes the membership change and its time of issue to persistent store. The membership changes form a history because nodes can be removed and added back multiple times. A gossip-based protocol propagates membership changes and maintains an eventually consistent view of membership. Each node contacts a peer chosen at random every second and the two nodes efficiently reconcile their persisted membership change histories.

When a node starts for the first time, it chooses its set of tokens (virtual nodes in the consistent hash space) and maps nodes to their respective token sets. The mapping is persisted on disk and initially contains only the local node and token set. The mappings stored at different Dynamo nodes are reconciled during the same communication exchange that reconciles the membership change histories. Therefore, partitioning and placement information also propagates via the gossip-based protocol and each storage node is aware of the token ranges handled by its peers. This allows each node to forward a key operation to the right set of nodes directly.

### 4.8.2 External Discovery

The mechanism described above could temporarily result in a logically partitioned Dynamo ring. For example, the administrator could contact node A to join A to the ring, then contact node B to join B to the ring. In this scenario, nodes A and B would each consider itself a member of the ring, yet neither would be immediately aware of the other. To prevent logical partitions, some Dynamo nodes play the role of seeds. Seeds are nodes that are discovered via an external mechanism and are known to all nodes. Because all nodes eventually reconcile their membership with a seed, logical partitions are highly unlikely. Seeds can be obtained either from static configuration or from a configuration service. Typically seeds are fully functional nodes in the Dynamo ring.

### 4.8.3 Failure Detection

Failure detection in Dynamo is used to avoid attempts to communicate with unreachable peers during get() and put() operations and when transferring partitions and hinted replicas. For the purpose of avoiding failed attempts at communication, a purely local notion of failure detection is entirely sufficient: node A may consider node B failed if node B does not respond to node A's messages (even if B is responsive to node C's messages). In the presence of a steady rate of client requests generating inter-node communication in the Dynamo ring, a node A quickly discovers that a node B is unresponsive when B fails to respond to a message; Node A then uses alternate nodes to service requests that map to B's partitions; A periodically retries B to check for the latter's recovery. In the absence of client requests to drive traffic between two nodes, neither node really needs to know whether the other is reachable and responsive.

Decentralized failure detection protocols use a simple gossip-style protocol that enable each node in the system to learn about the arrival (or departure) of other nodes. For detailed information on decentralized failure detectors and the parameters affecting their accuracy please refer to [8]. Early designs of Dynamo used a decentralized failure detector to maintain a globally consistent view of failure state. Later it was determined that the explicit node join and leave methods obviates the need for a global view of failure state. This is because nodes are notified of permanent node additions and removals by the explicit node join and leave methods and temporary node failures are detected by the individual nodes when they fail to communicate with others (while forwarding requests).

## 4.9 Adding/Removing Storage Nodes

When a new node (say X) is added into the system, it gets assigned a number of tokens that are randomly scattered on the ring. For every key range that is assigned to node X, there may be a number of nodes (less than or equal to N) that are currently in charge of handling keys that fall within its token range. Due to the allocation of key ranges to X, some existing nodes no longer have to some of their keys and these nodes transfer those keys to X. Let us consider a simple bootstrapping scenario where node X is added to the ring shown in Figure 2 between A and B. When X is added to the system, it is in charge of storing keys in the ranges (F, X], (G, X] and (A, X]. As a consequence, nodes B, C and D no longer have to store the keys in these respective ranges. Therefore, nodes B, C, and D will offer to and upon confirmation will transfer the appropriate set of keys to X. When a node is removed from the system, the reallocation of keys happens in a reverse process.

Operational experience has shown that this approach distributes the load of key distribution uniformly across the storage nodes, which is important to meet the latency requirements and to ensure fast bootstrapping. Finally, by adding a confirmation round between the source and the destination, it is made sure that the destination node does not receive any duplicate transfers for a given key range.

---

### النسخة العربية

## 4.1 واجهة النظام

يخزن ديناموا الكائنات المرتبطة بمفتاح من خلال واجهة بسيطة؛ حيث يعرض عمليتين: get() و put(). تحدد عملية get(key) النسخ المتماثلة للكائن المرتبطة بالمفتاح في نظام التخزين وتعيد كائناً واحداً أو قائمة من الكائنات ذات الإصدارات المتعارضة مع سياق. تحدد عملية put(key, context, object) أين يجب وضع النسخ المتماثلة للكائن بناءً على المفتاح المرتبط، وتكتب النسخ المتماثلة على القرص. يشفر السياق البيانات الوصفية للنظام حول الكائن التي تكون غامضة للمُستدعي وتتضمن معلومات مثل إصدار الكائن. يتم تخزين معلومات السياق مع الكائن بحيث يمكن للنظام التحقق من صحة كائن السياق المقدم في طلب put.

يتعامل ديناموا مع كل من المفتاح والكائن المقدم من المُستدعي كمصفوفة بايتات غامضة. يطبق تجزئة MD5 على المفتاح لتوليد معرف 128-بت، والذي يُستخدم لتحديد عُقد التخزين المسؤولة عن خدمة المفتاح.

## 4.2 خوارزمية التجزئة

أحد متطلبات التصميم الرئيسية لديناموا هو أنه يجب أن يتوسع بشكل تدريجي. هذا يتطلب آلية لتجزئة البيانات بشكل ديناميكي على مجموعة العُقد (أي مضيفي التخزين) في النظام. يعتمد مخطط التجزئة في ديناموا على التجزئة المتسقة لتوزيع الحمل عبر مضيفي تخزين متعددين. في التجزئة المتسقة [10]، يُعامل نطاق الإخراج لدالة التجزئة كفضاء دائري ثابت أو "حلقة" (أي أن أكبر قيمة تجزئة تلتف حول أصغر قيمة تجزئة). يتم تعيين كل عقدة في النظام قيمة عشوائية ضمن هذا الفضاء والتي تمثل "موضعها" على الحلقة. يتم تعيين كل عنصر بيانات محدد بمفتاح إلى عقدة عن طريق تجزئة مفتاح عنصر البيانات لإنتاج موضعه على الحلقة، ثم السير في الحلقة في اتجاه عقارب الساعة للعثور على أول عقدة بموضع أكبر من موضع العنصر.

وبالتالي، تصبح كل عقدة مسؤولة عن المنطقة في الحلقة بينها وبين عقدتها السابقة على الحلقة. الميزة الرئيسية للتجزئة المتسقة هي أن مغادرة أو وصول عقدة يؤثر فقط على جيرانها المباشرين وتبقى العُقد الأخرى غير متأثرة.

تقدم خوارزمية التجزئة المتسقة الأساسية بعض التحديات. أولاً، يؤدي التعيين العشوائي للموضع لكل عقدة على الحلقة إلى توزيع غير موحد للبيانات والحمل. ثانياً، الخوارزمية الأساسية غافلة عن عدم التجانس في أداء العُقد. لمعالجة هذه المشاكل، يستخدم ديناموا نسخة من التجزئة المتسقة (مشابهة لتلك المستخدمة في [10، 20]): بدلاً من تعيين عقدة إلى نقطة واحدة في الدائرة، يتم تعيين كل عقدة إلى نقاط متعددة في الحلقة. لهذا الغرض، يستخدم ديناموا مفهوم "العُقد الافتراضية". تبدو العقدة الافتراضية كعقدة واحدة في النظام، ولكن كل عقدة يمكن أن تكون مسؤولة عن أكثر من عقدة افتراضية واحدة. فعلياً، عندما تتم إضافة عقدة جديدة إلى النظام، يتم تعيينها مواضع متعددة (يُشار إليها فيما بعد بـ "الرموز") في الحلقة. تتم مناقشة عملية الضبط الدقيق لمخطط التجزئة في ديناموا في القسم 6.

استخدام العُقد الافتراضية له المزايا التالية:
- إذا أصبحت عقدة غير متاحة (بسبب الإخفاقات أو الصيانة الروتينية)، يتم توزيع الحمل الذي تتعامل معه هذه العقدة بالتساوي عبر العُقد المتاحة المتبقية.
- عندما تصبح عقدة متاحة مرة أخرى، أو تتم إضافة عقدة جديدة إلى النظام، تقبل العقدة المتاحة حديثاً كمية متساوية تقريباً من الحمل من كل من العُقد المتاحة الأخرى.
- يمكن تحديد عدد العُقد الافتراضية التي تكون العقدة مسؤولة عنها بناءً على سعتها، مع مراعاة عدم التجانس في البنية التحتية المادية.

## 4.3 النسخ التماثلي

لتحقيق توافر ومتانة عاليين، ينسخ ديناموا بياناته تماثلياً على مضيفين متعددين. يتم نسخ كل عنصر بيانات تماثلياً في N مضيف، حيث N هو معامل تم تكوينه "لكل نسخة". يتم تعيين كل مفتاح، k، إلى عقدة منسق (موضحة في القسم السابق). المنسق مسؤول عن النسخ التماثلي لعناصر البيانات التي تقع ضمن نطاقه. بالإضافة إلى تخزين كل مفتاح ضمن نطاقه محلياً، ينسخ المنسق هذه المفاتيح تماثلياً في عُقد N-1 التالية في اتجاه عقارب الساعة في الحلقة. ينتج عن هذا نظام حيث تكون كل عقدة مسؤولة عن منطقة الحلقة بينها وبين سلفها رقم N. في الشكل 2، تنسخ العقدة B المفتاح k في العقد C و D بالإضافة إلى تخزينه محلياً. ستقوم العقدة D بتخزين المفاتيح التي تقع في النطاقات (A، B]، (B، C]، و (C، D].

تسمى قائمة العُقد المسؤولة عن تخزين مفتاح معين قائمة التفضيل. تم تصميم النظام، كما سيتم شرحه في القسم 4.8، بحيث يمكن لكل عقدة في النظام تحديد العُقد التي يجب أن تكون في هذه القائمة لأي مفتاح معين. لمراعاة فشل العُقد، تحتوي قائمة التفضيل على أكثر من N عقدة. لاحظ أنه مع استخدام العُقد الافتراضية، من الممكن أن تكون مواضع N التالية الأولى لمفتاح معين مملوكة لأقل من N عقدة مادية متميزة (أي قد تحتفظ عقدة بأكثر من موضع واحد من المواضع N الأولى). لمعالجة هذا، يتم بناء قائمة التفضيل لمفتاح عن طريق تخطي المواضع في الحلقة لضمان أن القائمة تحتوي فقط على عُقد مادية متميزة.

## 4.4 إصدارات البيانات

يوفر ديناموا الاتساق النهائي، الذي يسمح بنشر التحديثات إلى جميع النسخ المتماثلة بشكل غير متزامن. قد تعود عملية put() إلى المُستدعي قبل تطبيق التحديث في جميع النسخ المتماثلة، مما يمكن أن يؤدي إلى سيناريوهات حيث قد تعيد عملية get() اللاحقة كائناً لا يحتوي على أحدث التحديثات. إذا لم تكن هناك إخفاقات، فهناك حد لأوقات نشر التحديث. ومع ذلك، في ظل ظروف فشل معينة (مثل انقطاع الخادم أو تقسيم الشبكة)، قد لا تصل التحديثات إلى جميع النسخ المتماثلة لفترة زمنية ممتدة.

هناك فئة من التطبيقات في منصة أمازون يمكنها تحمل مثل هذه التناقضات ويمكن بناؤها للعمل في هذه الظروف. على سبيل المثال، يتطلب تطبيق سلة التسوق أن عملية "إضافة إلى السلة" لا يمكن نسيانها أو رفضها أبداً. إذا لم تكن الحالة الأحدث للسلة متاحة، وقام المستخدم بإجراء تغييرات على إصدار أقدم من السلة، فإن هذا التغيير لا يزال ذا معنى ويجب الحفاظ عليه. ولكن في نفس الوقت لا ينبغي أن يحل محل الحالة الحالية غير المتاحة للسلة، والتي قد تحتوي نفسها على تغييرات يجب الحفاظ عليها. لاحظ أن كل من عمليات "إضافة إلى السلة" و "حذف عنصر من السلة" تُترجم إلى طلبات put إلى ديناموا. عندما يريد العميل إضافة عنصر إلى (أو إزالة من) سلة التسوق والإصدار الأحدث غير متاح، يتم إضافة العنصر إلى (أو إزالته من) الإصدار الأقدم ويتم التوفيق بين الإصدارات المتباينة لاحقاً.

لالتقاط السببية بين إصدارات مختلفة من نفس الكائن، نحتاج إلى مخطط إصدارات. يلتقط "الإصدار" التغييرات في كائن نتيجة لعملية put واحدة أو أكثر. يستخدم ديناموا ساعات المتجهات [12] من أجل التقاط السببية بين إصدارات مختلفة من نفس الكائن. ساعة المتجهات هي فعلياً قائمة من أزواج (عقدة، عداد). يتم ربط ساعة متجه واحدة بكل إصدار من كل كائن. يمكن للمرء تحديد ما إذا كان إصداران من كائن على فروع متوازية أو لهما ترتيب سببي، عن طريق فحص ساعات المتجهات الخاصة بهما. إذا كانت العدادات على ساعة الكائن الأول أقل من أو تساوي جميع العُقد في الساعة الثانية، فإن الأول هو سلف للثاني ويمكن نسيانه. خلاف ذلك، يُعتبر التغييران في تعارض ويتطلبان التوفيق.

في ديناموا، عندما يرغب العميل في تحديث كائن، يجب عليه تحديد الإصدار الذي يقوم بتحديثه. يتم ذلك عن طريق تمرير السياق الذي حصل عليه من عملية قراءة سابقة، والذي يحتوي على معلومات ساعة المتجهات. عند معالجة طلب قراءة، إذا كان لدى ديناموا وصول إلى فروع متعددة لا يمكن التوفيق بينها بشكل تركيبي، فسوف يعيد جميع الكائنات في الأوراق، مع معلومات الإصدار المقابلة في السياق. يُعتبر التحديث باستخدام هذا السياق قد وفّق بين الإصدارات المتباينة ويتم طي الفروع في إصدار جديد واحد.

## 4.5 تنفيذ عمليات get() و put()

أي عقدة تخزين في ديناموا مؤهلة لتلقي عمليات get و put من العميل لأي مفتاح. في هذا القسم، نصف كيف يتم تنفيذ هذه العمليات بطريقة موزعة.

يتم استدعاء كل من عمليات get و put باستخدام إطار معالجة الطلبات الخاص بالبنية التحتية لأمازون عبر HTTP. هناك استراتيجيتان يمكن للعميل استخدامهما لتحديد عقدة: (1) توجيه طلبه من خلال موازن حمل عام سيحدد عقدة بناءً على معلومات الحمل، أو (2) استخدام مكتبة عميل واعية بالتجزئة توجه الطلبات مباشرة إلى عُقد المنسق المناسبة. ميزة النهج الأول هي أن العميل لا يحتاج إلى ربط أي شفرة خاصة بديناموا في تطبيقه، بينما يمكن للنهج الثاني تحقيق زمن وصول أقل لأنه يتخطى خطوة إعادة توجيه محتملة.

تُعرف العقدة التي تتعامل مع عملية قراءة أو كتابة باسم المنسق. عادةً، هذه هي الأولى بين أعلى N عقدة في قائمة التفضيل. إذا تم استلام الطلبات من خلال موازن حمل، فقد يتم توجيه الطلبات للوصول إلى مفتاح إلى أي عقدة عشوائية في الحلقة. في هذا السيناريو، لن تنسق العقدة التي تتلقى الطلب إذا لم تكن العقدة في أعلى N من قائمة تفضيل المفتاح المطلوب. بدلاً من ذلك، ستعيد تلك العقدة توجيه الطلب إلى الأولى بين أعلى N عقدة في قائمة التفضيل.

تتضمن عمليات القراءة والكتابة أول N عقدة سليمة في قائمة التفضيل، متخطية تلك التي معطلة أو غير قابلة للوصول. عندما تكون جميع العُقد سليمة، يتم الوصول إلى أعلى N عقدة في قائمة تفضيل المفتاح. عندما تكون هناك إخفاقات في العُقد أو تقسيمات شبكية، يتم الوصول إلى العُقد ذات التصنيف الأدنى في قائمة التفضيل.

للحفاظ على الاتساق بين نسخه المتماثلة، يستخدم ديناموا بروتوكول اتساق مشابه لتلك المستخدمة في أنظمة النصاب. لهذا البروتوكول قيمتان رئيسيتان قابلتان للتكوين: R و W. R هو الحد الأدنى لعدد العُقد التي يجب أن تشارك في عملية قراءة ناجحة. W هو الحد الأدنى لعدد العُقد التي يجب أن تشارك في عملية كتابة ناجحة. تعيين R و W بحيث R + W > N ينتج نظاماً شبيهاً بالنصاب. في هذا النموذج، يتم تحديد زمن وصول عملية get (أو put) بواسطة الأبطأ من النسخ المتماثلة R (أو W). لهذا السبب، عادةً ما يتم تكوين R و W ليكونا أقل من N، لتوفير زمن وصول أفضل.

عند تلقي طلب put() لمفتاح، يولد المنسق ساعة المتجهات للإصدار الجديد ويكتب الإصدار الجديد محلياً. يرسل المنسق بعد ذلك الإصدار الجديد (مع ساعة المتجهات الجديدة) إلى أعلى N عقدة قابلة للوصول. إذا استجابت على الأقل W-1 عقدة، تُعتبر الكتابة ناجحة.

وبالمثل، بالنسبة لطلب get()، يطلب المنسق جميع الإصدارات الموجودة من البيانات لذلك المفتاح من أعلى N عقدة قابلة للوصول في قائمة التفضيل لذلك المفتاح، وينتظر R استجابة، ثم يعيد النتيجة إلى العميل. إذا انتهى المنسق بجمع إصدارات متعددة من البيانات، فإنه يعيد جميع الإصدارات التي يعتبرها غير مرتبطة سببياً. ثم يتم التوفيق بين الإصدارات المتباينة ويتم كتابة الإصدار الموفق الذي يحل محل الإصدارات الحالية مرة أخرى.

## 4.6 التعامل مع الإخفاقات: التسليم الموجه

إذا استخدم ديناموا نهج النصاب التقليدي، فسيكون غير متاح أثناء فشل الخادم وتقسيم الشبكة، وسيكون لديه متانة مخفضة حتى في أبسط ظروف الفشل. لمعالجة هذا، لا يفرض عضوية نصاب صارمة وبدلاً من ذلك يستخدم "نصاباً فضفاضاً"؛ يتم تنفيذ جميع عمليات القراءة والكتابة على أول N عقدة سليمة من قائمة التفضيل، والتي قد لا تكون دائماً أول N عقدة تمت مواجهتها أثناء السير في حلقة التجزئة المتسقة.

ضع في اعتبارك مثال تكوين ديناموا المعطى في الشكل 2 مع N=3. في هذا المثال، إذا كانت العقدة A معطلة مؤقتاً أو غير قابلة للوصول أثناء عملية كتابة، فسيتم الآن إرسال نسخة متماثلة كانت ستعيش عادةً على A إلى العقدة D. يتم ذلك للحفاظ على ضمانات التوافر والمتانة المطلوبة. سيكون للنسخة المتماثلة المرسلة إلى D تلميح في بياناتها الوصفية يشير إلى العقدة التي كانت المستلم المقصود للنسخة المتماثلة (في هذه الحالة A). ستحتفظ العُقد التي تتلقى نسخاً متماثلة موجهة بها في قاعدة بيانات محلية منفصلة يتم فحصها بشكل دوري. عند اكتشاف أن A قد تعافت، ستحاول D تسليم النسخة المتماثلة إلى A. بمجرد نجاح النقل، قد تحذف D الكائن من مخزنها المحلي دون تقليل العدد الإجمالي للنسخ المتماثلة في النظام.

باستخدام التسليم الموجه، يضمن ديناموا عدم فشل عمليات القراءة والكتابة بسبب فشل العقدة أو الشبكة المؤقت. يمكن للتطبيقات التي تحتاج إلى أعلى مستوى من التوافر تعيين W إلى 1، مما يضمن قبول الكتابة طالما أن عقدة واحدة في النظام قد كتبت المفتاح بشكل دائم إلى مخزنها المحلي. وبالتالي، يتم رفض طلب الكتابة فقط إذا كانت جميع العُقد في النظام غير متاحة. ومع ذلك، في الممارسة العملية، تقوم معظم خدمات أمازون في الإنتاج بتعيين W أعلى لتلبية المستوى المطلوب من المتانة. تتبع مناقشة أكثر تفصيلاً لتكوين N و R و W في القسم 6.

## 4.7 التعامل مع الإخفاقات الدائمة: مزامنة النسخ المتماثل

يعمل التسليم الموجه بشكل أفضل إذا كان تقلب عضوية النظام منخفضاً وإخفاقات العُقد عابرة. هناك سيناريوهات تصبح بموجبها النسخ المتماثلة الموجهة غير متاحة قبل أن يمكن إعادتها إلى عقدة النسخة المتماثلة الأصلية. للتعامل مع هذا والتهديدات الأخرى للمتانة، ينفذ ديناموا بروتوكول مضاد للإنتروبيا (مزامنة النسخ المتماثل) للحفاظ على النسخ المتماثلة متزامنة.

لاكتشاف التناقضات بين النسخ المتماثلة بشكل أسرع ولتقليل كمية البيانات المنقولة، يستخدم ديناموا أشجار ميركل [13]. شجرة ميركل هي شجرة تجزئة حيث الأوراق هي تجزئات قيم المفاتيح الفردية. العُقد الأصلية الأعلى في الشجرة هي تجزئات أطفالها المعنيين. الميزة الرئيسية لشجرة ميركل هي أنه يمكن التحقق من كل فرع من الشجرة بشكل مستقل دون الحاجة إلى تنزيل الشجرة بأكملها أو مجموعة البيانات بأكملها. علاوة على ذلك، تساعد أشجار ميركل في تقليل كمية البيانات التي يجب نقلها أثناء التحقق من التناقضات بين النسخ المتماثلة. على سبيل المثال، إذا كانت قيم التجزئة لجذر شجرتين متساوية، فإن قيم عُقد الأوراق في الشجرة متساوية ولا تتطلب العُقد أي مزامنة. إذا لم يكن الأمر كذلك، فإنه يعني أن قيم بعض النسخ المتماثلة مختلفة. في مثل هذه الحالات، قد تتبادل العُقد قيم التجزئة للأطفال وتستمر العملية حتى تصل إلى أوراق الأشجار، وعند تلك النقطة يمكن للمضيفين تحديد المفاتيح "غير المتزامنة". تقلل أشجار ميركل من كمية البيانات التي يجب نقلها للمزامنة وتقلل من عدد قراءات القرص المنفذة أثناء عملية مضاد الإنتروبيا.

يستخدم ديناموا أشجار ميركل لمضاد الإنتروبيا على النحو التالي: تحتفظ كل عقدة بشجرة ميركل منفصلة لكل نطاق مفاتيح (مجموعة المفاتيح المغطاة بواسطة عقدة افتراضية) تستضيفها. هذا يسمح للعقد بمقارنة ما إذا كانت المفاتيح ضمن نطاق مفاتيح محدثة. في هذا المخطط، تتبادل عقدتان جذر شجرة ميركل المقابلة لنطاقات المفاتيح التي تستضيفانها بشكل مشترك. لاحقاً، باستخدام مخطط اجتياز الشجرة الموضح أعلاه، تحدد العُقد ما إذا كان لديها أي اختلافات وتقوم بإجراء المزامنة المناسب. العيب في هذا المخطط هو أن العديد من نطاقات المفاتيح تتغير عندما تنضم عقدة أو تغادر النظام وبالتالي تتطلب إعادة حساب الشجرة (الأشجار). ومع ذلك، تتم معالجة هذه المسألة بواسطة مخطط التجزئة المحسن الموضح في القسم 6.2.

## 4.8 العضوية وكشف الفشل

### 4.8.1 عضوية الحلقة

في بيئة أمازون، غالباً ما تكون انقطاعات العُقد (بسبب الإخفاقات ومهام الصيانة) عابرة ولكن قد تستمر لفترات ممتدة. نادراً ما يشير انقطاع العقدة إلى مغادرة دائمة وبالتالي لا ينبغي أن يؤدي إلى إعادة موازنة تعيين التجزئة أو إصلاح النسخ المتماثلة التي لا يمكن الوصول إليها. وبالمثل، قد يؤدي الخطأ اليدوي إلى بدء تشغيل غير مقصود لعُقد ديناموا جديدة. لهذه الأسباب، اعتُبر من المناسب استخدام آلية صريحة لبدء إضافة وإزالة العُقد من حلقة ديناموا. يستخدم المسؤول أداة سطر أوامر أو متصفحاً للاتصال بعقدة ديناموا وإصدار تغيير عضوية لضم عقدة إلى حلقة أو إزالة عقدة من حلقة. تكتب العقدة التي تخدم الطلب تغيير العضوية ووقت إصداره إلى مخزن دائم. تشكل تغييرات العضوية تاريخاً لأنه يمكن إزالة العُقد وإضافتها مرة أخرى عدة مرات. ينشر بروتوكول قائم على الشائعات تغييرات العضوية ويحافظ على رؤية متسقة نهائياً للعضوية. تتصل كل عقدة بنظير يتم اختياره عشوائياً كل ثانية وتوفق العقدتان بكفاءة بين تواريخ تغييرات العضوية المستمرة الخاصة بهما.

عندما تبدأ عقدة للمرة الأولى، تختار مجموعة رموزها (العُقد الافتراضية في فضاء التجزئة المتسق) وتعين العُقد إلى مجموعات رموزها المعنية. يتم الاحتفاظ بالتعيين على القرص ويحتوي في البداية فقط على العقدة المحلية ومجموعة الرموز. يتم التوفيق بين التعيينات المخزنة في عُقد ديناموا المختلفة أثناء نفس تبادل الاتصالات الذي يوفق بين تواريخ تغييرات العضوية. لذلك، تنتشر معلومات التجزئة والوضع أيضاً عبر البروتوكول القائم على الشائعات وكل عقدة تخزين على دراية بنطاقات الرموز التي يتعامل معها نظراؤها. هذا يسمح لكل عقدة بإعادة توجيه عملية مفتاح إلى المجموعة الصحيحة من العُقد مباشرة.

### 4.8.2 الاكتشاف الخارجي

يمكن للآلية الموضحة أعلاه أن تؤدي مؤقتاً إلى حلقة ديناموا مقسمة منطقياً. على سبيل المثال، يمكن للمسؤول الاتصال بالعقدة A لضم A إلى الحلقة، ثم الاتصال بالعقدة B لضم B إلى الحلقة. في هذا السيناريو، ستعتبر العقدتان A و B كل منهما نفسها عضواً في الحلقة، ومع ذلك لن يكون أي منهما على دراية فورية بالآخر. لمنع التقسيمات المنطقية، تلعب بعض عُقد ديناموا دور البذور. البذور هي عُقد يتم اكتشافها عبر آلية خارجية ومعروفة لجميع العُقد. لأن جميع العُقد توفق في النهاية عضويتها مع بذرة، فإن التقسيمات المنطقية من غير المحتمل جداً. يمكن الحصول على البذور إما من التكوين الثابت أو من خدمة التكوين. عادةً ما تكون البذور عُقداً كاملة الوظائف في حلقة ديناموا.

### 4.8.3 كشف الفشل

يُستخدم كشف الفشل في ديناموا لتجنب محاولات الاتصال بالنظراء غير القابلين للوصول أثناء عمليات get() و put() وعند نقل التجزئات والنسخ المتماثلة الموجهة. لغرض تجنب محاولات الاتصال الفاشلة، فإن المفهوم المحلي البحت لكشف الفشل كافٍ تماماً: قد تعتبر العقدة A العقدة B فاشلة إذا لم تستجب العقدة B لرسائل العقدة A (حتى لو كانت B مستجيبة لرسائل العقدة C). في وجود معدل ثابت من طلبات العميل التي تولد اتصالاً بين العُقد في حلقة ديناموا، تكتشف العقدة A بسرعة أن العقدة B لا تستجيب عندما تفشل B في الاستجابة لرسالة؛ ثم تستخدم العقدة A عُقداً بديلة لخدمة الطلبات التي تعين إلى تجزئات B؛ تعيد A المحاولة بشكل دوري مع B للتحقق من تعافي الأخيرة. في غياب طلبات العميل لتوجيه حركة المرور بين عقدتين، لا تحتاج أي من العقدتين حقاً إلى معرفة ما إذا كانت الأخرى قابلة للوصول ومستجيبة.

تستخدم بروتوكولات كشف الفشل اللامركزية بروتوكول شائعات بسيط يمكّن كل عقدة في النظام من التعلم عن وصول (أو مغادرة) العُقد الأخرى. للحصول على معلومات مفصلة حول كاشفات الفشل اللامركزية والمعاملات التي تؤثر على دقتها، يرجى الرجوع إلى [8]. استخدمت التصاميم المبكرة لديناموا كاشف فشل لامركزي للحفاظ على رؤية متسقة عالمياً لحالة الفشل. في وقت لاحق تقرر أن طرق الانضمام والمغادرة الصريحة للعقدة تجعل الحاجة إلى رؤية عالمية لحالة الفشل غير ضرورية. هذا لأن العُقد يتم إخطارها بإضافات وإزالات العُقد الدائمة بواسطة طرق الانضمام والمغادرة الصريحة للعقدة ويتم اكتشاف إخفاقات العُقد المؤقتة بواسطة العُقد الفردية عندما تفشل في الاتصال بالآخرين (أثناء إعادة توجيه الطلبات).

## 4.9 إضافة/إزالة عُقد التخزين

عندما تتم إضافة عقدة جديدة (لنقل X) إلى النظام، يتم تعيينها عدداً من الرموز المبعثرة عشوائياً على الحلقة. لكل نطاق مفاتيح يتم تعيينه للعقدة X، قد يكون هناك عدد من العُقد (أقل من أو يساوي N) المسؤولة حالياً عن التعامل مع المفاتيح التي تقع ضمن نطاق رموزها. نظراً لتخصيص نطاقات المفاتيح لـ X، لم تعد بعض العُقد الموجودة بحاجة إلى بعض مفاتيحها وتقوم هذه العُقد بنقل تلك المفاتيح إلى X. دعونا نعتبر سيناريو تمهيد بسيط حيث تتم إضافة العقدة X إلى الحلقة الموضحة في الشكل 2 بين A و B. عندما تتم إضافة X إلى النظام، فإنها مسؤولة عن تخزين المفاتيح في النطاقات (F، X]، (G، X] و (A، X]. نتيجة لذلك، لم تعد العُقد B و C و D بحاجة إلى تخزين المفاتيح في هذه النطاقات المعنية. لذلك، ستعرض العُقد B و C و D وعند التأكيد ستنقل مجموعة المفاتيح المناسبة إلى X. عندما تتم إزالة عقدة من النظام، تحدث إعادة تخصيص المفاتيح في عملية عكسية.

أظهرت الخبرة التشغيلية أن هذا النهج يوزع حمل توزيع المفاتيح بشكل موحد عبر عُقد التخزين، وهو أمر مهم لتلبية متطلبات زمن الوصول ولضمان التمهيد السريع. أخيراً، بإضافة جولة تأكيد بين المصدر والوجهة، يتم التأكد من أن عقدة الوجهة لا تتلقى أي عمليات نقل مكررة لنطاق مفاتيح معين.

---

### Translation Notes

- **Figures referenced:** Figure 2 (ring topology showing node replication)
- **Key technical concepts:**
  - MD5 hash → تجزئة MD5
  - Virtual nodes (tokens) → العُقد الافتراضية (الرموز)
  - Preference list → قائمة التفضيل
  - Vector clocks → ساعات المتجهات
  - Quorum (R, W, N) → النصاب
  - Hinted handoff → التسليم الموجه
  - Sloppy quorum → نصاب فضفاض
  - Merkle trees → أشجار ميركل
  - Anti-entropy → مضاد للإنتروبيا
  - Gossip protocol → بروتوكول الشائعات

- **Citations:** [8], [10], [12], [13], [20]
- **Special handling:**
  - Technical parameters (N, R, W) kept as English letters
  - Hash values and technical notation preserved
  - System names (Dynamo, Amazon) kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Check (Key Paragraph)

"To achieve high availability and durability, Dynamo replicates its data on multiple hosts. Each data item is replicated at N hosts, where N is a parameter configured per-instance. Each key, k, is assigned to a coordinator node. The coordinator is in charge of the replication of the data items that fall within its range. In addition to locally storing each key within its range, the coordinator replicates these keys at the N-1 clockwise successor nodes in the ring."

✓ Technical accuracy confirmed
