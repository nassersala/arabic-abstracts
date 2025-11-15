# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** consensus, consensus algorithm, replicated log, Paxos, leader election, log replication, safety, cluster membership

---

### English Version

Raft is a consensus algorithm for managing a replicated log. It produces a result equivalent to (multi-)Paxos, and it is as efficient as Paxos, but its structure is different from Paxos; this makes Raft more understandable than Paxos and also provides a better foundation for building practical systems. In order to enhance understandability, Raft separates the key elements of consensus, such as leader election, log replication, and safety, and it enforces a stronger degree of coherency to reduce the number of states that must be considered. Results from a user study demonstrate that Raft is easier for students to learn than Paxos. Raft also includes a new mechanism for changing the cluster membership, which uses overlapping majorities to guarantee safety.

---

### النسخة العربية

Raft هي خوارزمية إجماع لإدارة سجل مُنسَخ. تُنتج نتيجة مُكافئة لخوارزمية (Multi-)Paxos، وهي بنفس كفاءة Paxos، لكن بنيتها تختلف عن Paxos؛ مما يجعل Raft أكثر قابلية للفهم من Paxos كما توفر أساساً أفضل لبناء الأنظمة العملية. من أجل تعزيز القابلية للفهم، تفصل Raft العناصر الأساسية للإجماع، مثل انتخاب القائد، ونسخ السجل، والسلامة، كما تفرض درجة أقوى من التماسك لتقليل عدد الحالات التي يجب أخذها في الاعتبار. تُظهر نتائج دراسة على مستخدمين أن Raft أسهل للطلاب في التعلم من Paxos. تتضمن Raft أيضاً آلية جديدة لتغيير عضوية المجموعة، والتي تستخدم أغلبيات متداخلة لضمان السلامة.

---

### Translation Notes

- **Key terms introduced:**
  - consensus algorithm = خوارزمية إجماع
  - replicated log = سجل مُنسَخ
  - leader election = انتخاب القائد
  - log replication = نسخ السجل
  - safety = السلامة
  - cluster membership = عضوية المجموعة
  - overlapping majorities = أغلبيات متداخلة
  - understandability = القابلية للفهم

- **Translation decisions:**
  - Kept "Raft" and "Paxos" as proper nouns (algorithm names)
  - Used "سجل مُنسَخ" for "replicated log" (replicated/copied log)
  - Used "قائد" for "leader" (standard term in distributed systems)
  - Used "إجماع" for "consensus" (already in glossary)
  - Used "التماسك" for "coherency" (coherence/cohesion)

- **Style notes:**
  - Maintained formal academic Arabic
  - Preserved the comparative structure (Raft vs. Paxos)
  - Emphasized understandability as the main design goal

### Quality Metrics

- **Semantic equivalence:** 0.92 - Accurately preserves all key concepts
- **Technical accuracy:** 0.93 - All technical terms correctly translated
- **Readability:** 0.90 - Natural flow in Arabic while maintaining precision
- **Glossary consistency:** 0.90 - Consistent with established terms
- **Overall section score:** 0.91

### Back-Translation Check

Back-translating the first sentence:
"Raft is a consensus algorithm for managing a replicated log."
Arabic: "Raft هي خوارزمية إجماع لإدارة سجل مُنسَخ"
Back to English: "Raft is a consensus algorithm for managing a replicated/copied log."
✓ Semantically equivalent

Back-translating key phrase:
"this makes Raft more understandable than Paxos"
Arabic: "مما يجعل Raft أكثر قابلية للفهم من Paxos"
Back to English: "which makes Raft more understandable/comprehensible than Paxos"
✓ Semantically equivalent
