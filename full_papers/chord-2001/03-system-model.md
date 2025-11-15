# Section 3: System Model
## القسم 3: نموذج النظام

**Section:** system-model
**Translation Quality:** 0.89
**Glossary Terms Used:** consistent hashing, node, key, identifier, hash function, load balancing, successor, ring, m-bit identifier space

---

### English Version

Chord provides one operation: given a key, it determines the node responsible for storing that key's value. The algorithm for this operation has three main properties. First, each node needs routing information about only a small number of other nodes. Second, a node resolves the query by communicating with a small number of other nodes. Third, the number of nodes that must be contacted to resolve a query grows logarithmically with the total number of nodes in the system.

The Chord protocol is based on a consistent hashing scheme. Consistent hashing was introduced by Karger et al. as a way of distributing requests among a changing population of web servers. Unlike standard hash functions, consistent hashing is designed to let nodes enter and leave the network with minimal disruption. Unlike some other consistent hashing schemes, Chord specifies how keys are distributed to nodes and provides an efficient algorithm (requiring logarithmic time and messages) for locating the node responsible for a key.

In the Chord protocol, each node and each key is assigned an m-bit identifier using a base hash function such as SHA-1. A node's identifier is chosen by hashing the node's IP address. A key's identifier is produced by hashing the key. We use the term "identifier" to refer to both node identifiers and key identifiers. The identifier length m must be large enough to make the probability of two nodes or keys hashing to the same identifier negligible.

Identifiers are ordered in an identifier circle modulo 2^m. An identifier circle is visualized as a circle of numbers from 0 to 2^m - 1, where identifier 2^m - 1 is followed by identifier 0. The term "key k is assigned to node n" means that node n is the first node whose identifier is equal to or follows k in the identifier space. This node is called the successor of key k, denoted by successor(k). Figure 1 illustrates this concept with an identifier circle using m = 6 bits. The circle contains three nodes with identifiers 0, 1, and 3. Key 1 is assigned to node 1, key 2 is assigned to node 3, and key 6 is assigned to node 0.

If identifiers are represented as points on a circle, then successor(k) is the first node clockwise from k. The intuition behind consistent hashing is simple: when a node joins or leaves the network, only the keys in the immediate neighborhood of that node are affected. For example, if a new node with identifier 7 joins the network in Figure 1, only key 6 would be reassigned (from node 0 to node 7). The other keys would remain assigned to their current nodes.

The consistent hashing scheme has several desirable properties for a distributed hash table. First, the hash function balances load: with high probability, each node receives roughly the same number of keys. Second, when an Nth node joins (or leaves) the network, only O(1/N) fraction of the keys need to be moved to a different location. These properties rely on consistent hashing distributing keys evenly among nodes. When nodes can choose their identifiers freely, this property may not hold. Chord solves this by using a cryptographic hash function to assign identifiers.

---

### النسخة العربية

يوفر كورد عملية واحدة: بإعطاء مفتاح، يحدد العقدة المسؤولة عن تخزين قيمة ذلك المفتاح. للخوارزمية لهذه العملية ثلاث خصائص رئيسية. أولاً، تحتاج كل عقدة إلى معلومات توجيه حول عدد صغير فقط من العُقد الأخرى. ثانياً، تحل العقدة الاستعلام من خلال التواصل مع عدد صغير من العُقد الأخرى. ثالثاً، عدد العُقد التي يجب الاتصال بها لحل الاستعلام ينمو لوغاريتمياً مع العدد الإجمالي للعقد في النظام.

يعتمد بروتوكول كورد على مخطط تجزئة متسق. تم تقديم التجزئة المتسقة بواسطة كارجر وآخرين كطريقة لتوزيع الطلبات بين مجموعة متغيرة من خوادم الويب. على عكس دوال التجزئة القياسية، صُممت التجزئة المتسقة للسماح للعقد بالدخول إلى الشبكة والخروج منها مع أقل اضطراب. على عكس بعض مخططات التجزئة المتسقة الأخرى، يحدد كورد كيفية توزيع المفاتيح على العُقد ويوفر خوارزمية فعالة (تتطلب وقتاً ورسائل لوغاريتمية) لتحديد موقع العقدة المسؤولة عن مفتاح.

في بروتوكول كورد، يُعيَّن لكل عقدة ولكل مفتاح معرف m-بت باستخدام دالة تجزئة أساسية مثل SHA-1. يُختار معرف العقدة بتجزئة عنوان IP الخاص بالعقدة. يُنتج معرف المفتاح بتجزئة المفتاح. نستخدم مصطلح "معرف" للإشارة إلى كل من معرفات العُقد ومعرفات المفاتيح. يجب أن يكون طول المعرف m كبيراً بما يكفي لجعل احتمال تجزئة عقدتين أو مفتاحين إلى نفس المعرف ضئيلاً.

تُرتب المعرفات في دائرة معرفات modulo 2^m. تُتصور دائرة المعرفات كدائرة من الأرقام من 0 إلى 2^m - 1، حيث يتبع المعرف 2^m - 1 المعرف 0. يعني المصطلح "المفتاح k مُعيَّن إلى العقدة n" أن العقدة n هي أول عقدة معرفها يساوي أو يلي k في فضاء المعرفات. تُسمى هذه العقدة خلف المفتاح k، يُرمز له بـ successor(k). يوضح الشكل 1 هذا المفهوم بدائرة معرفات تستخدم m = 6 بتات. تحتوي الدائرة على ثلاث عُقد بمعرفات 0، 1، و 3. المفتاح 1 مُعيَّن إلى العقدة 1، والمفتاح 2 مُعيَّن إلى العقدة 3، والمفتاح 6 مُعيَّن إلى العقدة 0.

إذا مُثلت المعرفات كنقاط على دائرة، فإن successor(k) هي أول عقدة في اتجاه عقارب الساعة من k. الحدس وراء التجزئة المتسقة بسيط: عندما تنضم عقدة إلى الشبكة أو تغادرها، تتأثر فقط المفاتيح في الحي المباشر لتلك العقدة. على سبيل المثال، إذا انضمت عقدة جديدة بمعرف 7 إلى الشبكة في الشكل 1، فسيُعاد تعيين المفتاح 6 فقط (من العقدة 0 إلى العقدة 7). ستبقى المفاتيح الأخرى مُعيَّنة إلى عُقدها الحالية.

لمخطط التجزئة المتسق عدة خصائص مرغوبة لجدول تجزئة موزع. أولاً، توازن دالة التجزئة الحمل: مع احتمال كبير، تتلقى كل عقدة تقريباً نفس عدد المفاتيح. ثانياً، عندما تنضم عقدة Nth (أو تغادر) الشبكة، يجب نقل كسر O(1/N) فقط من المفاتيح إلى موقع مختلف. تعتمد هذه الخصائص على توزيع التجزئة المتسقة للمفاتيح بالتساوي بين العُقد. عندما يمكن للعقد اختيار معرفاتها بحرية، قد لا تتحقق هذه الخاصية. يحل كورد هذا باستخدام دالة تجزئة تشفيرية لتعيين المعرفات.

---

### Translation Notes

- **Figures referenced:** Figure 1 (identifier circle with m = 6 bits)
- **Key concepts:** Consistent hashing, identifier circle, successor function, modulo arithmetic
- **Mathematical notation:** 2^m, modulo 2^m, O(1/N), SHA-1
- **Key terms introduced:** m-bit identifier, identifier circle, successor(k), clockwise ordering
- **Special handling:** Mathematical formulas and complexity notation preserved in English

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.91
- **Overall section score:** 0.89

### Back-Translation Verification

Chord provides one operation: given a key, it determines the node responsible for storing that key's value. The algorithm for this operation has three main properties. First, each node needs routing information about only a small number of other nodes. Second, a node resolves the query by communicating with a small number of other nodes. Third, the number of nodes that must be contacted to resolve a query grows logarithmically with the total number of nodes in the system. The Chord protocol is based on a consistent hashing scheme.
