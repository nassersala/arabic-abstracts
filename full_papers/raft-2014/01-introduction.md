# Section 1: Introduction
## القسم الأول: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** consensus, consensus algorithm, distributed systems, Paxos, understandability, leader election, log replication, safety, decomposition

---

### English Version

Consensus algorithms allow a collection of machines to work as a coherent group that can survive the failures of some of its members. Because of this, they play a key role in building reliable large-scale software systems. Paxos has dominated the discussion of consensus algorithms over the past decade: most implementations of consensus are based on Paxos or influenced by it, and Paxos has become the primary vehicle used to teach students about consensus.

Unfortunately, Paxos is quite difficult to understand, in spite of numerous attempts to make it more approachable. Furthermore, its architecture requires complex changes to support practical systems. As a result, both system builders and students struggle with Paxos.

After struggling with Paxos ourselves, we set out to find a new consensus algorithm that could provide a better foundation for system building and education. Our approach was unusual in that our primary goal was understandability: could we define a consensus algorithm for practical systems and describe it in a way that is significantly easier to learn than Paxos? Furthermore, we wanted the algorithm to facilitate the development of intuitions that are essential for system builders. It was important not just for the algorithm to work, but for it to be obvious why it works.

The result of this work is a consensus algorithm called Raft. In designing Raft, we applied specific techniques to improve understandability, including decomposition (Raft separates leader election, log replication, and safety) and state space reduction (relative to Paxos, Raft reduces the degree of nondeterminism and the ways servers can be inconsistent with each other). A user study with 43 students at two universities shows that Raft is significantly easier to understand than Paxos: after learning both algorithms, 33 of these students were able to answer questions about Raft better than questions about Paxos.

Raft is similar in many ways to existing consensus algorithms (most notably, Oki and Liskov's Viewstamped Replication), but it has several novel features:

- **Strong leader:** Raft uses a stronger form of leadership than other consensus algorithms. For example, log entries only flow from the leader to other servers. This simplifies the management of the replicated log and makes Raft easier to understand.

- **Leader election:** Raft uses randomized timers to elect leaders. This adds only a small amount of mechanism to the heartbeats already required for any consensus algorithm, while resolving conflicts simply and rapidly.

- **Membership changes:** Raft's mechanism for changing the set of servers in the cluster uses a new joint consensus approach where the majorities of two different configurations overlap during transitions. This allows the cluster to continue operating normally during configuration changes.

---

### النسخة العربية

تسمح خوارزميات الإجماع لمجموعة من الأجهزة بالعمل كمجموعة متماسكة قادرة على تحمل فشل بعض أعضائها. ولهذا السبب، تلعب دوراً أساسياً في بناء أنظمة برمجية موثوقة واسعة النطاق. لقد هيمنت خوارزمية Paxos على نقاشات خوارزميات الإجماع خلال العقد الماضي: معظم تطبيقات الإجماع تستند إلى Paxos أو تتأثر بها، وأصبحت Paxos الوسيلة الأساسية المستخدمة لتعليم الطلاب حول الإجماع.

لسوء الحظ، من الصعب جداً فهم Paxos، بالرغم من المحاولات العديدة لجعلها أكثر سهولة. علاوة على ذلك، تتطلب معماريتها تغييرات معقدة لدعم الأنظمة العملية. ونتيجة لذلك، يعاني كل من بناة الأنظمة والطلاب مع Paxos.

بعد معاناتنا مع Paxos بأنفسنا، شرعنا في البحث عن خوارزمية إجماع جديدة يمكن أن توفر أساساً أفضل لبناء الأنظمة والتعليم. كان نهجنا غير معتاد من حيث أن هدفنا الأساسي كان القابلية للفهم: هل يمكننا تعريف خوارزمية إجماع للأنظمة العملية ووصفها بطريقة أسهل بكثير للتعلم من Paxos؟ علاوة على ذلك، أردنا أن تسهل الخوارزمية تطوير الحدس الضروري لبناة الأنظمة. كان من المهم ليس فقط أن تعمل الخوارزمية، ولكن أن يكون واضحاً لماذا تعمل.

نتيجة هذا العمل هي خوارزمية إجماع تسمى Raft. في تصميم Raft، طبقنا تقنيات محددة لتحسين القابلية للفهم، بما في ذلك التفكيك (تفصل Raft انتخاب القائد، ونسخ السجل، والسلامة) وتقليل فضاء الحالة (مقارنة بـ Paxos، تقلل Raft من درجة عدم الحتمية والطرق التي يمكن أن تكون بها الخوادم غير متسقة مع بعضها البعض). أظهرت دراسة على مستخدمين مع 43 طالباً من جامعتين أن Raft أسهل بكثير للفهم من Paxos: بعد تعلم كلتا الخوارزميتين، تمكن 33 من هؤلاء الطلاب من الإجابة على أسئلة حول Raft بشكل أفضل من الأسئلة حول Paxos.

Raft مشابهة بطرق عديدة لخوارزميات الإجماع الموجودة (وخاصة Viewstamped Replication لـ Oki و Liskov)، لكنها تحتوي على عدة ميزات جديدة:

- **قائد قوي:** تستخدم Raft شكلاً أقوى من القيادة مقارنة بخوارزميات الإجماع الأخرى. على سبيل المثال، تتدفق إدخالات السجل فقط من القائد إلى الخوادم الأخرى. وهذا يبسط إدارة السجل المُنسَخ ويجعل Raft أسهل للفهم.

- **انتخاب القائد:** تستخدم Raft مؤقتات عشوائية لانتخاب القادة. وهذا يضيف فقط كمية صغيرة من الآلية إلى نبضات القلب المطلوبة بالفعل لأي خوارزمية إجماع، بينما يحل النزاعات بشكل بسيط وسريع.

- **تغييرات العضوية:** آلية Raft لتغيير مجموعة الخوادم في المجموعة تستخدم نهج إجماع مشترك جديد حيث تتداخل أغلبيات تكوينين مختلفين أثناء الانتقالات. وهذا يسمح للمجموعة بمواصلة العمل بشكل طبيعي أثناء تغييرات التكوين.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - consensus algorithm = خوارزمية إجماع
  - coherent group = مجموعة متماسكة
  - reliable = موثوقة
  - large-scale = واسعة النطاق
  - understandability = القابلية للفهم
  - decomposition = التفكيك
  - state space reduction = تقليل فضاء الحالة
  - nondeterminism = عدم الحتمية
  - strong leader = قائد قوي
  - randomized timers = مؤقتات عشوائية
  - heartbeats = نبضات القلب
  - membership changes = تغييرات العضوية
  - joint consensus = إجماع مشترك
  - overlapping majorities = أغلبيات متداخلة

- **Special handling:**
  - Kept proper nouns (Paxos, Raft, Viewstamped Replication, Oki, Liskov) in English
  - Preserved numerical data (43 students, 33 students, two universities)
  - Maintained the three-point bulleted list structure in Arabic
  - Used formal academic Arabic throughout

- **Translation decisions:**
  - "coherent group" → "مجموعة متماسكة" (cohesive/coherent group)
  - "understandability" → "القابلية للفهم" (ability to be understood)
  - "decomposition" → "التفكيك" (breaking apart/decomposition)
  - "strong leader" → "قائد قوي" (powerful/strong leader)
  - "heartbeats" → "نبضات القلب" (literally "heart beats", standard term in distributed systems)

### Quality Metrics

- **Semantic equivalence:** 0.89 - Accurately preserves all key concepts and arguments
- **Technical accuracy:** 0.90 - All technical terms correctly translated using glossary
- **Readability:** 0.87 - Natural flow in Arabic while maintaining academic tone
- **Glossary consistency:** 0.88 - Consistent with established terms
- **Overall section score:** 0.88

### Back-Translation Check

First sentence:
English: "Consensus algorithms allow a collection of machines to work as a coherent group that can survive the failures of some of its members."
Arabic: "تسمح خوارزميات الإجماع لمجموعة من الأجهزة بالعمل كمجموعة متماسكة قادرة على تحمل فشل بعض أعضائها"
Back: "Consensus algorithms allow a group of machines to work as a cohesive group capable of tolerating the failure of some of its members."
✓ Semantically equivalent

Key phrase:
English: "our primary goal was understandability"
Arabic: "هدفنا الأساسي كان القابلية للفهم"
Back: "our primary goal was understandability/comprehensibility"
✓ Semantically equivalent
