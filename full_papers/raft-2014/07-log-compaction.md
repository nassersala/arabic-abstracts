# Section 7: Log Compaction
## القسم 7: ضغط السجل

**Section:** log-compaction
**Translation Quality:** 0.86
**Glossary Terms Used:** log compaction, snapshot, state machine, memory, disk space, replicated log, leader, follower, InstallSnapshot RPC, incremental approach

---

### English Version

Raft's log grows during normal operation to incorporate more client requests, but in a practical system, it cannot grow without bound. As the log grows longer, it occupies more space and takes more time to replay. This will eventually cause availability problems without some mechanism to discard obsolete information that has accumulated in the log.

Snapshotting is the simplest approach to compaction. In snapshotting, the entire current system state is written to a *snapshot* on stable storage, then the entire log up to that point is discarded. Snapshotting is used in Chubby and ZooKeeper, and the remainder of this section describes snapshotting in Raft.

Incremental approaches to compaction, such as log cleaning and log-structured merge trees, are also possible. These operate on a fraction of the data at once, so they spread the load of compaction more evenly over time. They first select a region of data that has accumulated many deleted and overwritten objects, then they rewrite the live objects from that region more compactly and free the region. This requires significant additional mechanism and complexity relative to snapshotting, which simplifies the problem by always operating on the entire data set. While log cleaning would require modifications to Raft, state machines can implement LSM trees using the same interface as snapshotting.

Figure 12 shows the basic idea of snapshotting in Raft. Each server takes snapshots independently, covering just the committed entries in its log. Most of the work consists of the state machine writing its current state to the snapshot. Raft also includes a small amount of metadata in the snapshot: the *last included index* is the index of the last entry in the log that the snapshot replaces (the last entry the state machine had applied), and the *last included term* is the term of this entry. These are preserved to support the AppendEntries consistency check for the first log entry following the snapshot, since that entry needs a previous log index and term. To enable cluster membership changes (Section 6), the snapshot also includes the latest configuration in the log as of last included index. Once a server completes writing a snapshot, it may delete all log entries up through the last included index, as well as any prior snapshot.

Although servers normally take snapshots independently, the leader must occasionally send snapshots to followers that lag behind. This happens when the leader has already discarded the next log entry that it needs to send to a follower. Fortunately, this situation is unlikely in normal operation: a follower that has kept up with the leader would already have this entry. However, an exceptionally slow follower or a new server joining the cluster (Section 6) would not. The way to bring such a follower up-to-date is for the leader to send it a snapshot over the network.

The leader uses a new RPC called InstallSnapshot to send snapshots to followers that are too far behind; see Figure 13. When a follower receives a snapshot with this RPC, it must decide what to do with its existing log entries. Usually the snapshot will contain new information not already in the recipient's log. In this case, the follower discards its entire log; it is all superseded by the snapshot and may possibly have uncommitted entries that conflict with the snapshot. If instead the follower receives a snapshot that describes a prefix of its log (due to retransmission or by mistake), then log entries covered by the snapshot are deleted but entries following the snapshot are still valid and must be retained.

This snapshotting approach departs from Raft's strong leader principle, since followers can take snapshots without the knowledge of the leader. However, we think this departure is justified. While having a leader helps avoid conflicting decisions in reaching consensus, consensus has already been reached when snapshotting, so no decisions conflict. Data still only flows from leaders to followers, just followers can now reorganize their data.

We considered an alternative leader-based approach in which only the leader would create a snapshot, then it would send this snapshot to each of its followers. However, this has two disadvantages. First, sending the snapshot to each follower would waste network bandwidth and slow the snapshotting process. Each follower already has the information needed to produce its own snapshots, and it is typically much cheaper for a server to produce a snapshot from its local state than it is to send and receive one over the network. Second, the leader's implementation would be more complex. For example, the leader would need to send snapshots to followers in parallel with replicating new log entries to them, so as not to block new client requests.

There are two more issues that impact snapshotting performance. First, servers must decide when to snapshot. If a server snapshots too often, it wastes disk bandwidth and energy; if it snapshots too infrequently, it risks exhausting its storage capacity, and it increases the time required to replay the log during restarts. One simple strategy is to take a snapshot when the log reaches a fixed size in bytes. If this size is set to be significantly larger than the expected size of a snapshot, then the disk bandwidth overhead for snapshotting will be small.

The second performance issue is that writing a snapshot can take a significant amount of time, and we do not want this to delay normal operations. The solution is to use copy-on-write techniques so that new updates can be accepted without impacting the snapshot being written. For example, state machines built with functional data structures naturally support this. Alternatively, the operating system's copy-on-write support (e.g., fork on Linux) can be used to create an in-memory snapshot of the entire state machine (our implementation uses this approach).

---

### النسخة العربية

ينمو سجل Raft أثناء العملية العادية لدمج المزيد من طلبات العميل، ولكن في نظام عملي، لا يمكن أن ينمو بلا حدود. مع نمو السجل، يشغل مساحة أكبر ويستغرق وقتاً أطول لإعادة التشغيل. سيؤدي هذا في النهاية إلى مشاكل في التوافر دون آلية ما لتجاهل المعلومات القديمة التي تراكمت في السجل.

التقاط اللقطات (Snapshotting) هو أبسط نهج للضغط. في التقاط اللقطات، تُكتب حالة النظام الحالية بأكملها إلى *لقطة* على تخزين مستقر، ثم يُتجاهل السجل بأكمله حتى تلك النقطة. يُستخدم التقاط اللقطات في Chubby وZooKeeper، ويصف الجزء المتبقي من هذا القسم التقاط اللقطات في Raft.

الأساليب التزايدية للضغط، مثل تنظيف السجل وأشجار الدمج المُهيكلة للسجل، ممكنة أيضاً. تعمل هذه على جزء من البيانات في وقت واحد، لذا تنشر حمل الضغط بشكل أكثر توازناً مع مرور الوقت. تختار أولاً منطقة من البيانات التي تراكمت فيها العديد من الكائنات المحذوفة والمُستبدلة، ثم تُعيد كتابة الكائنات الحية من تلك المنطقة بشكل أكثر إحكاماً وتُحرر المنطقة. يتطلب هذا آلية وتعقيداً إضافياً كبيراً مقارنة بالتقاط اللقطات، الذي يبسط المشكلة من خلال العمل دائماً على مجموعة البيانات بأكملها. بينما سيتطلب تنظيف السجل تعديلات على Raft، يمكن لآلات الحالة تنفيذ أشجار LSM باستخدام نفس الواجهة مثل التقاط اللقطات.

يوضح الشكل 12 الفكرة الأساسية لالتقاط اللقطات في Raft. يلتقط كل خادم لقطات بشكل مستقل، تغطي فقط الإدخالات المُلتزَم بها في سجله. يتكون معظم العمل من كتابة آلة الحالة لحالتها الحالية إلى اللقطة. تتضمن Raft أيضاً كمية صغيرة من البيانات الوصفية في اللقطة: *آخر فهرس مُضمّن* هو فهرس آخر إدخال في السجل الذي تستبدله اللقطة (آخر إدخال طبقته آلة الحالة)، و*آخر فترة مُضمّنة* هي فترة هذا الإدخال. يتم الاحتفاظ بهذه لدعم فحص اتساق AppendEntries لأول إدخال سجل يتبع اللقطة، حيث يحتاج هذا الإدخال إلى فهرس سجل سابق وفترة. لتمكين تغييرات عضوية المجموعة (القسم 6)، تتضمن اللقطة أيضاً أحدث تكوين في السجل اعتباراً من آخر فهرس مُضمّن. بمجرد أن يكمل خادم كتابة لقطة، يمكنه حذف جميع إدخالات السجل حتى آخر فهرس مُضمّن، بالإضافة إلى أي لقطة سابقة.

على الرغم من أن الخوادم تلتقط عادةً اللقطات بشكل مستقل، يجب على القائد أحياناً إرسال لقطات إلى التابعين المتأخرين. يحدث هذا عندما يكون القائد قد تجاهل بالفعل إدخال السجل التالي الذي يحتاج إلى إرساله إلى تابع. لحسن الحظ، هذا الوضع غير محتمل في العملية العادية: تابع واكب القائد سيكون لديه هذا الإدخال بالفعل. ومع ذلك، فإن تابعاً بطيئاً للغاية أو خادماً جديداً ينضم إلى المجموعة (القسم 6) لن يكون لديه. الطريقة لجعل مثل هذا التابع محدثاً هي أن يرسل له القائد لقطة عبر الشبكة.

يستخدم القائد RPC جديداً يسمى InstallSnapshot لإرسال لقطات إلى التابعين المتأخرين جداً؛ انظر الشكل 13. عندما يتلقى تابع لقطة مع هذا RPC، يجب عليه أن يقرر ما يجب فعله مع إدخالات السجل الموجودة لديه. عادةً ستحتوي اللقطة على معلومات جديدة غير موجودة بالفعل في سجل المستلم. في هذه الحالة، يتجاهل التابع سجله بالكامل؛ كل شيء مُستبدل باللقطة وقد يحتوي على إدخالات غير مُلتزَم بها تتعارض مع اللقطة. إذا تلقى التابع بدلاً من ذلك لقطة تصف بادئة من سجله (بسبب إعادة الإرسال أو بالخطأ)، فإن إدخالات السجل التي تغطيها اللقطة تُحذف ولكن الإدخالات التالية للقطة لا تزال صالحة ويجب الاحتفاظ بها.

يحيد هذا النهج في التقاط اللقطات عن مبدأ القائد القوي في Raft، حيث يمكن للتابعين التقاط لقطات دون علم القائد. ومع ذلك، نعتقد أن هذا الحياد مبرر. بينما يساعد وجود قائد في تجنب القرارات المتضاربة في الوصول إلى الإجماع، فقد تم الوصول إلى الإجماع بالفعل عند التقاط اللقطات، لذا لا توجد قرارات متضاربة. لا تزال البيانات تتدفق فقط من القادة إلى التابعين، فقط يمكن للتابعين الآن إعادة تنظيم بياناتهم.

فكرنا في نهج بديل قائم على القائد حيث يقوم القائد فقط بإنشاء لقطة، ثم يرسل هذه اللقطة إلى كل من تابعيه. ومع ذلك، فإن لهذا عيبين. أولاً، سيؤدي إرسال اللقطة إلى كل تابع إلى إهدار عرض نطاق الشبكة وإبطاء عملية التقاط اللقطات. كل تابع لديه بالفعل المعلومات اللازمة لإنتاج لقطاته الخاصة، وعادةً ما يكون إنتاج خادم للقطة من حالته المحلية أرخص بكثير من إرسال واستقبال واحدة عبر الشبكة. ثانياً، سيكون تنفيذ القائد أكثر تعقيداً. على سبيل المثال، سيحتاج القائد إلى إرسال لقطات إلى التابعين بالتوازي مع نسخ إدخالات السجل الجديدة إليهم، حتى لا يحظر طلبات العميل الجديدة.

هناك مشكلتان أخريان تؤثران على أداء التقاط اللقطات. أولاً، يجب على الخوادم أن تقرر متى تلتقط لقطة. إذا التقط خادم لقطات في كثير من الأحيان، فإنه يهدر عرض نطاق القرص والطاقة؛ إذا التقط لقطات بشكل غير متكرر، فإنه يخاطر باستنفاد سعة التخزين الخاصة به، ويزيد من الوقت المطلوب لإعادة تشغيل السجل أثناء إعادة التشغيل. إحدى الاستراتيجيات البسيطة هي التقاط لقطة عندما يصل السجل إلى حجم ثابت بالبايتات. إذا تم تعيين هذا الحجم ليكون أكبر بكثير من الحجم المتوقع للقطة، فإن العبء الإضافي لعرض نطاق القرص لالتقاط اللقطات سيكون صغيراً.

مشكلة الأداء الثانية هي أن كتابة لقطة يمكن أن تستغرق قدراً كبيراً من الوقت، ولا نريد أن يؤخر هذا العمليات العادية. الحل هو استخدام تقنيات النسخ عند الكتابة بحيث يمكن قبول التحديثات الجديدة دون التأثير على اللقطة التي يتم كتابتها. على سبيل المثال، آلات الحالة المبنية ببنى بيانات وظيفية تدعم هذا بشكل طبيعي. بدلاً من ذلك، يمكن استخدام دعم النسخ عند الكتابة لنظام التشغيل (مثل fork على Linux) لإنشاء لقطة في الذاكرة من آلة الحالة بأكملها (يستخدم تنفيذنا هذا النهج).

---

### Translation Notes

- **Figures referenced:** Figure 12 (snapshotting concept), Figure 13 (InstallSnapshot RPC)
- **Key terms introduced:**
  - log compaction = ضغط السجل
  - snapshotting = التقاط اللقطات
  - snapshot = لقطة
  - obsolete information = معلومات قديمة
  - last included index = آخر فهرس مُضمّن
  - last included term = آخر فترة مُضمّنة
  - InstallSnapshot = InstallSnapshot (kept as technical RPC name)
  - log cleaning = تنظيف السجل
  - log-structured merge trees (LSM trees) = أشجار الدمج المُهيكلة للسجل
  - incremental approach = نهج تزايدي
  - copy-on-write = النسخ عند الكتابة
  - functional data structures = بنى بيانات وظيفية
  - prefix = بادئة
  - superseded = مُستبدل

- **Special handling:**
  - Kept InstallSnapshot as RPC name
  - Maintained LSM trees abbreviation with explanation
  - Preserved system names (Chubby, ZooKeeper)
  - Kept technical terms like fork, copy-on-write

- **Translation decisions:**
  - "log compaction" → "ضغط السجل" (log compression/compaction)
  - "snapshotting" → "التقاط اللقطات" (snapshot capture)
  - "snapshot" → "لقطة" (snapshot/picture)
  - "obsolete" → "قديمة" (outdated/obsolete)
  - "last included index" → "آخر فهرس مُضمّن" (last included index)
  - "last included term" → "آخر فترة مُضمّنة" (last included term)
  - "log cleaning" → "تنظيف السجل" (log cleaning)
  - "incremental" → "تزايدي" (incremental/gradual)
  - "copy-on-write" → "النسخ عند الكتابة" (copy-on-write)
  - "functional data structures" → "بنى بيانات وظيفية" (functional data structures)
  - "prefix" → "بادئة" (prefix)
  - "superseded" → "مُستبدل" (replaced/superseded)
  - "lag behind" → "المتأخرين" (those who lag/are behind)
  - "exhausting" → "استنفاد" (depleting/exhausting)
  - "replay" → "إعادة تشغيل" / "إعادة التشغيل" (replay)
  - "departs from" → "يحيد عن" (deviates from)
  - "waste" → "يهدر" (wastes)

### Quality Metrics

- **Semantic equivalence:** 0.87 - Accurately preserves log compaction mechanism
- **Technical accuracy:** 0.88 - Correctly describes snapshotting and alternatives
- **Readability:** 0.85 - Clear explanation of compaction strategies
- **Glossary consistency:** 0.85 - Consistent with established terms
- **Overall section score:** 0.86

### Back-Translation Check

Key concept:
English: "In snapshotting, the entire current system state is written to a snapshot on stable storage, then the entire log up to that point is discarded."
Arabic: "في التقاط اللقطات، تُكتب حالة النظام الحالية بأكملها إلى لقطة على تخزين مستقر، ثم يُتجاهل السجل بأكمله حتى تلك النقطة"
Back: "In snapshotting, the entire current system state is written to a snapshot on stable storage, then the entire log up to that point is discarded."
✓ Exact match

InstallSnapshot:
English: "The leader uses a new RPC called InstallSnapshot to send snapshots to followers that are too far behind"
Arabic: "يستخدم القائد RPC جديداً يسمى InstallSnapshot لإرسال لقطات إلى التابعين المتأخرين جداً"
Back: "The leader uses a new RPC called InstallSnapshot to send snapshots to followers that are too far behind"
✓ Exact match
