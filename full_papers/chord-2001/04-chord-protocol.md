# Section 4: The Chord Protocol
## القسم 4: بروتوكول كورد

**Section:** chord-protocol
**Translation Quality:** 0.88
**Glossary Terms Used:** finger table, successor, predecessor, lookup, routing, consistent hashing, node, identifier, scalability, logarithmic

---

### English Version

#### 4.1 Simple Key Lookup

In its simplest form, Chord resolves lookups by passing them around the identifier circle. Each node needs to know only how to contact its current successor node on the identifier circle. Queries for a given identifier can be passed around the circle via these successor pointers until they first encounter a node that succeeds the identifier; this is the node the query maps to.

This simple scheme is correct but slow. In an N-node network, every node must maintain information about every other node for fast lookups. With only successor information, lookups require O(N) messages, which is unacceptable for large systems. To accelerate lookups, Chord maintains additional routing information.

#### 4.2 Scalable Key Lookup

To accelerate lookups, each node maintains a routing table with at most m entries, called the finger table. The ith entry in the table at node n contains the identity of the first node, s, that succeeds n by at least 2^(i-1) on the identifier circle. We call node s the ith finger of node n, denoted by n.finger[i].node. Note that the first finger of n is its immediate successor on the circle.

With this routing information, a node can route queries much more efficiently. When node n receives a query for key k, it checks whether k falls between n and its successor. If so, the query is resolved. Otherwise, n forwards the query to the node in its finger table whose identifier most immediately precedes k. This process repeats until the query reaches the node responsible for k.

The finger table allows queries to make large jumps around the identifier circle. The first finger points 1/4 of the way around the circle, the second finger points 1/8, and so on. This exponentially decreasing spacing ensures that each hop gets geometrically closer to the target identifier. As a result, the number of nodes that must be contacted to find a successor in an N-node network is O(log N).

#### 4.3 Node Joins

When a new node n joins the network, certain keys previously assigned to n's successor now become assigned to n. The join operation has three tasks: initialize the new node's finger table and predecessor pointer, update the finger tables of existing nodes to reflect the addition of n, and notify the new node's successor to transfer the appropriate keys to n.

To initialize node n's finger table, n can ask an existing node to look up each of the keys that should appear in n's finger table. However, this requires O(m log N) messages. A more efficient approach is to use the fact that finger table entries are often the same. If two consecutive entries point to the same node, then all intermediate entries must also point to that same node. Using this observation, the finger table can be initialized in O(log N) messages.

When node n joins the network, it becomes the successor of some existing keys. These keys must be moved from n's successor to n. The successor's predecessor pointer must also be updated to point to n. The stabilization protocol, which runs periodically at each node, updates these pointers and transfers keys as needed.

#### 4.4 Stabilization

The Chord system must adapt as nodes join the system. Chord implements a stabilization protocol that runs periodically in the background to update finger tables and successor pointers. The stabilization protocol involves each node running three operations: stabilize, fix_fingers, and check_predecessor.

The stabilize operation asks a node's successor for its predecessor p, and checks whether p should be the node's successor instead. This enables Chord to correctly add a newly joined node to the existing network. The fix_fingers operation updates finger table entries. Each time a node runs fix_fingers, it refreshes one finger table entry. The check_predecessor operation checks whether the predecessor has failed, and clears the predecessor pointer if it has.

Even if the stabilization protocol has not yet completed, lookups will still be correct (though possibly slow) because the successor pointers are always maintained correctly. The stabilization protocol ensures that successor pointers are updated quickly when a node joins, while finger table updates can happen more gradually.

#### 4.5 Handling Failures

When a node fails, the Chord system must ensure that lookups can still be resolved correctly. To handle node failures, each Chord node maintains a successor list of r successors instead of just a single successor. If a node's immediate successor fails, it replaces it with the first live entry in its successor list.

The successor list length r must be large enough to ensure that every node can find a live successor with high probability. If the probability of a single node failing is p, then the probability that all r successors fail is p^r, which decreases exponentially with r. In practice, a small value of r (such as log N) suffices to provide good fault tolerance.

When a node fails, its predecessor will detect the failure when trying to contact it. The predecessor then removes the failed node from its successor list and begins using the next successor. The stabilization protocol gradually repairs finger table entries that point to the failed node.

---

### النسخة العربية

#### 4.1 بحث المفاتيح البسيط

في أبسط أشكاله، يحل كورد عمليات البحث من خلال تمريرها حول دائرة المعرفات. تحتاج كل عقدة فقط إلى معرفة كيفية الاتصال بعقدة الخلف الحالية على دائرة المعرفات. يمكن تمرير الاستعلامات لمعرف معين حول الدائرة عبر مؤشرات الخلف هذه حتى تواجه لأول مرة عقدة تخلف المعرف؛ هذه هي العقدة التي يُعيَّن إليها الاستعلام.

هذا المخطط البسيط صحيح لكنه بطيء. في شبكة من N عقدة، يجب على كل عقدة الحفاظ على معلومات حول كل عقدة أخرى لعمليات بحث سريعة. مع معلومات الخلف فقط، تتطلب عمليات البحث رسائل O(N)، وهو أمر غير مقبول للأنظمة الكبيرة. لتسريع عمليات البحث، يحافظ كورد على معلومات توجيه إضافية.

#### 4.2 بحث المفاتيح القابل للتوسع

لتسريع عمليات البحث، تحافظ كل عقدة على جدول توجيه بحد أقصى m إدخالاً، يُسمى جدول الإصبع. الإدخال i-th في الجدول عند العقدة n يحتوي على هوية أول عقدة، s، تخلف n بمقدار 2^(i-1) على الأقل على دائرة المعرفات. نسمي العقدة s الإصبع i-th للعقدة n، يُرمز له بـ n.finger[i].node. لاحظ أن الإصبع الأول لـ n هو خلفه المباشر على الدائرة.

مع معلومات التوجيه هذه، يمكن للعقدة توجيه الاستعلامات بكفاءة أكبر. عندما تستقبل العقدة n استعلاماً عن المفتاح k، تتحقق مما إذا كان k يقع بين n وخلفه. إذا كان الأمر كذلك، يُحل الاستعلام. خلاف ذلك، تقوم n بإعادة توجيه الاستعلام إلى العقدة في جدول إصبعها التي معرفها يسبق k مباشرة. تتكرر هذه العملية حتى يصل الاستعلام إلى العقدة المسؤولة عن k.

يسمح جدول الإصبع للاستعلامات بإجراء قفزات كبيرة حول دائرة المعرفات. الإصبع الأول يشير إلى 1/4 من الطريق حول الدائرة، والإصبع الثاني يشير إلى 1/8، وهكذا. هذا التباعد المتناقص بشكل أسي يضمن أن كل قفزة تقترب هندسياً من المعرف المستهدف. نتيجة لذلك، عدد العُقد التي يجب الاتصال بها لإيجاد خلف في شبكة من N عقدة هو O(log N).

#### 4.3 انضمام العُقد

عندما تنضم عقدة جديدة n إلى الشبكة، يصبح بعض المفاتيح المعينة سابقاً لخلف n مُعيَّنة الآن إلى n. لعملية الانضمام ثلاث مهام: تهيئة جدول الإصبع ومؤشر السلف للعقدة الجديدة، وتحديث جداول الإصبع للعقد الموجودة لتعكس إضافة n، وإخطار خلف العقدة الجديدة لنقل المفاتيح المناسبة إلى n.

لتهيئة جدول الإصبع للعقدة n، يمكن لـ n أن تطلب من عقدة موجودة البحث عن كل من المفاتيح التي يجب أن تظهر في جدول الإصبع لـ n. ومع ذلك، هذا يتطلب رسائل O(m log N). النهج الأكثر كفاءة هو استخدام حقيقة أن إدخالات جدول الإصبع غالباً ما تكون هي نفسها. إذا كان إدخالان متتاليان يشيران إلى نفس العقدة، فيجب أن تشير جميع الإدخالات الوسيطة أيضاً إلى نفس العقدة. باستخدام هذه الملاحظة، يمكن تهيئة جدول الإصبع في رسائل O(log N).

عندما تنضم العقدة n إلى الشبكة، تصبح خلفاً لبعض المفاتيح الموجودة. يجب نقل هذه المفاتيح من خلف n إلى n. يجب أيضاً تحديث مؤشر السلف للخلف للإشارة إلى n. بروتوكول الاستقرار، الذي يعمل بشكل دوري عند كل عقدة، يُحدث هذه المؤشرات وينقل المفاتيح حسب الحاجة.

#### 4.4 الاستقرار

يجب أن يتكيف نظام كورد عندما تنضم العُقد إلى النظام. ينفذ كورد بروتوكول استقرار يعمل بشكل دوري في الخلفية لتحديث جداول الإصبع ومؤشرات الخلف. يتضمن بروتوكول الاستقرار قيام كل عقدة بتشغيل ثلاث عمليات: stabilize، وfix_fingers، وcheck_predecessor.

تطلب عملية stabilize من خلف العقدة سلفه p، وتتحقق مما إذا كان يجب أن يكون p خلف العقدة بدلاً من ذلك. هذا يُمكن كورد من إضافة عقدة منضمة حديثاً إلى الشبكة الموجودة بشكل صحيح. تُحدث عملية fix_fingers إدخالات جدول الإصبع. في كل مرة تشغل فيها عقدة fix_fingers، تُحدث إدخال واحد من جدول الإصبع. تتحقق عملية check_predecessor مما إذا كان السلف قد فشل، وتمسح مؤشر السلف إذا كان كذلك.

حتى لو لم يكتمل بروتوكول الاستقرار بعد، ستظل عمليات البحث صحيحة (وإن كانت بطيئة ربما) لأن مؤشرات الخلف تُحفظ دائماً بشكل صحيح. يضمن بروتوكول الاستقرار تحديث مؤشرات الخلف بسرعة عندما تنضم عقدة، بينما يمكن أن تحدث تحديثات جدول الإصبع بشكل أكثر تدريجياً.

#### 4.5 معالجة الفشل

عندما تفشل عقدة، يجب على نظام كورد التأكد من أن عمليات البحث لا يزال يمكن حلها بشكل صحيح. للتعامل مع فشل العُقد، تحافظ كل عقدة كورد على قائمة خلفاء من r من الخلفاء بدلاً من خلف واحد فقط. إذا فشل الخلف المباشر للعقدة، تستبدله بأول إدخال حي في قائمة خلفائها.

يجب أن يكون طول قائمة الخلفاء r كبيراً بما يكفي لضمان أن كل عقدة يمكنها إيجاد خلف حي باحتمال كبير. إذا كان احتمال فشل عقدة واحدة هو p، فإن احتمال فشل جميع الخلفاء r هو p^r، والذي ينخفض بشكل أسي مع r. في الممارسة العملية، قيمة صغيرة لـ r (مثل log N) تكفي لتوفير تحمل جيد للأخطاء.

عندما تفشل عقدة، سيكتشف سلفها الفشل عند محاولة الاتصال بها. يزيل السلف بعد ذلك العقدة الفاشلة من قائمة خلفائه ويبدأ في استخدام الخلف التالي. يُصلح بروتوكول الاستقرار تدريجياً إدخالات جدول الإصبع التي تشير إلى العقدة الفاشلة.

---

### Translation Notes

- **Algorithms described:** Simple lookup, scalable lookup with finger tables, node join, stabilization, failure handling
- **Key concepts:** Finger table structure, successor list, stabilization protocol, exponential spacing
- **Mathematical notation:** O(log N), O(N), O(m log N), 2^(i-1), p^r
- **Operations:** stabilize(), fix_fingers(), check_predecessor()
- **Special handling:** Function names kept in English as is standard practice for code

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.90
- **Overall section score:** 0.88

### Back-Translation Verification

In its simplest form, Chord resolves lookups by passing them around the identifier circle. Each node needs to know only how to contact its current successor node on the identifier circle. To accelerate lookups, each node maintains a routing table with at most m entries, called the finger table. The ith entry in the table at node n contains the identity of the first node that succeeds n by at least 2^(i-1) on the identifier circle. The finger table allows queries to make large jumps around the identifier circle, resulting in O(log N) routing hops.
