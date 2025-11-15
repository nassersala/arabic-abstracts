# Section 4: Concurrency Control
## القسم 4: التحكم في التزامن

**Section:** concurrency-control
**Translation Quality:** 0.86
**Glossary Terms Used:** concurrency control (التحكم في التزامن), external consistency (الاتساق الخارجي), linearizability (الخطية), two-phase locking (القفل ثنائي المرحلة), two-phase commit (التنفيذ ثنائي المرحلة), snapshot isolation (عزل اللقطة), read-write transaction (معاملة قراءة-كتابة), read-only transaction (معاملة قراءة فقط), timestamp (طابع زمني), safe time (وقت آمن)

---

### English Version

This section describes how TrueTime is used to guarantee the correctness properties around concurrency control, and how those properties are used to implement features such as externally consistent transactions, lock-free read-only transactions, and non-blocking reads in the past. These features enable, for example, the guarantee that a whole-database audit read at a timestamp t will see exactly the effects of every transaction that has committed as of t.

Going forward, it will be important to distinguish writes as seen by Paxos (which we will refer to as Paxos writes unless the context is clear) from Spanner client writes. For example, two-phase commit generates a Paxos write for the prepare phase that has no corresponding Spanner client write.

**4.1 Timestamp Management**

Table 2 lists the types of operations that Spanner supports. The Spanner implementation supports read-write transactions, read-only transactions (predeclared snapshot-isolation transactions), and snapshot reads. Standalone writes are implemented as read-write transactions; non-snapshot standalone reads are implemented as read-only transactions. Both are internally retried (clients need not write their own retry loops).

A read-only transaction is a kind of transaction that has the performance benefits of snapshot isolation [6]. A read-only transaction must be predeclared as not having any writes; it is not simply a read-write transaction without any writes. Reads in a read-only transaction execute at a system-chosen timestamp without locking, so that incoming writes are not blocked. The execution of the reads in a read-only transaction can proceed on any replica that is sufficiently up-to-date (Section 4.1.3).

A snapshot read is a read in the past that executes without locking. A client can either specify a timestamp for a snapshot read, or provide an upper bound on the desired timestamp's staleness and let Spanner choose a timestamp. In either case, the execution of a snapshot read proceeds at any replica that is sufficiently up-to-date.

For both read-only transactions and snapshot reads, commit is inevitable once a timestamp has been chosen, unless the data at that timestamp has been garbage-collected. As a result, clients can avoid buffering results inside a retry loop. When a server fails, clients can internally continue the query on a different server by repeating the timestamp and the current read position.

**4.1.1 Paxos Leader Leases**

Spanner's Paxos implementation uses timed leases to make leadership long-lived (10 seconds by default). A potential leader sends requests for timed lease votes; upon receiving a quorum of lease votes the leader knows it has a lease. A replica extends its lease vote implicitly on a successful write, and the leader requests lease-vote extensions if they are near expiration. Define a leader's lease interval as starting when it discovers it has a quorum of lease votes, and as ending when it no longer has a quorum of lease votes (because some have expired). Spanner depends on the following disjointness invariant: for each Paxos group, each Paxos leader's lease interval is disjoint from every other leader's. Appendix A describes how this invariant is enforced.

The Spanner implementation permits a Paxos leader to abdicate by releasing its slaves from their lease votes. To preserve the disjointness invariant, Spanner constrains when abdication is permissible. Define s_max to be the maximum timestamp used by a leader. Subsequent sections will describe when s_max is advanced. Before abdicating, a leader must wait until TT.after(s_max) is true.

**4.1.2 Assigning Timestamps to RW Transactions**

Transactional reads and writes use two-phase locking. As a result, they can be assigned timestamps at any time when all locks have been acquired, but before any locks have been released. For a given transaction, Spanner assigns it the timestamp that Paxos assigns to the Paxos write that represents the transaction commit.

Spanner depends on the following monotonicity invariant: within each Paxos group, Spanner assigns timestamps to Paxos writes in monotonically increasing order, even across leaders. A single leader replica can trivially assign timestamps in monotonically increasing order. This invariant is enforced across leaders by making use of the disjointness invariant: a leader must only assign timestamps within the interval of its leader lease. Note that whenever a timestamp s is assigned, s_max is advanced to s to preserve disjointness.

Spanner also enforces the following external-consistency invariant: if the start of a transaction T₂ occurs after the commit of a transaction T₁, then the commit timestamp of T₂ must be greater than the commit timestamp of T₁. Define the start and commit events for a transaction Tᵢ by e^start_i and e^commit_i; and the commit timestamp of a transaction Tᵢ by sᵢ. The invariant becomes t_abs(e^commit_1) < t_abs(e^start_2) ⇒ s₁ < s₂.

The protocol for executing transactions and assigning timestamps obeys two rules, which together guarantee this invariant, as shown below. Define the arrival event of the commit request at the coordinator leader for a write Tᵢ to be e^server_i.

**Start:** The coordinator leader for a write Tᵢ assigns a commit timestamp sᵢ no less than the value of TT.now().latest, computed after e^server_i. Note that the participant leaders do not matter here; Section 4.2.1 describes how they are involved in the implementation of the next rule.

**Commit Wait:** The coordinator leader ensures that clients cannot see any data committed by Tᵢ until TT.after(sᵢ) is true. Commit wait ensures that sᵢ is less than the absolute commit time of Tᵢ, or sᵢ < t_abs(e^commit_i). The implementation of commit wait is described in Section 4.2.1.

**Proof:**
```
s₁ < t_abs(e^commit_1)     (commit wait)
t_abs(e^commit_1) < t_abs(e^start_2)     (assumption)
t_abs(e^start_2) ≤ t_abs(e^server_2)     (causality)
t_abs(e^server_2) ≤ s₂     (start)
s₁ < s₂     (transitivity)
```

**4.1.3 Serving Reads at a Timestamp**

The monotonicity invariant described in Section 4.1.2 allows Spanner to correctly determine whether a replica's state is sufficiently up-to-date to satisfy a read. Every replica tracks a value called safe time t_safe which is the maximum timestamp at which a replica is up-to-date. A replica can satisfy a read at a timestamp t if t ≤ t_safe.

Define t_safe = min(t^Paxos_safe, t^TM_safe), where each Paxos state machine has a safe time t^Paxos_safe and each transaction manager has a safe time t^TM_safe. t^Paxos_safe is simpler: it is the timestamp of the highest-applied Paxos write. Because timestamps increase monotonically and writes are applied in order, writes will no longer occur at or below t^Paxos_safe with respect to Paxos.

t^TM_safe is ∞ at a replica if there are zero prepared (but not committed) transactions—that is, transactions in between the two phases of two-phase commit. (For a participant slave, t^TM_safe actually refers to the replica's leader's transaction manager, whose state the slave can infer through metadata passed on Paxos writes.) If there are any such transactions, then the state affected by those transactions is indeterminate: a participant replica does not know yet whether such transactions will commit. As we discuss in Section 4.2.1, the commit protocol ensures that every participant knows a lower bound on a prepared transaction's timestamp. Every participant leader (for a group g) for a transaction Tᵢ assigns a prepare timestamp s^prepare_i,g to its prepare record. The coordinator leader ensures that the transaction's commit timestamp sᵢ ≥ s^prepare_i,g over all participant groups g. Therefore, for every replica in a group g, over all transactions Tᵢ prepared at g, t^TM_safe = minᵢ(s^prepare_i,g) - 1 over all transactions prepared at g.

**4.1.4 Assigning Timestamps to RO Transactions**

A read-only transaction executes in two phases: assign a timestamp s_read [8], and then execute the transaction's reads as snapshot reads at s_read. The snapshot reads can execute at any replicas that are sufficiently up-to-date.

The simple assignment of s_read = TT.now().latest, at any time after a transaction starts, preserves external consistency by an argument analogous to that presented for writes in Section 4.1.2. However, such a timestamp may require the execution of the data reads at s_read to block if t_safe has not advanced sufficiently. (In addition, note that choosing a value of s_read may also advance s_max to preserve disjointness.) To reduce the chances of blocking, Spanner should assign the oldest timestamp that preserves external consistency. Section 4.2.2 explains how such a timestamp can be chosen.

**4.2 Details**

This section explains some of the practical details of read-write transactions and read-only transactions elided earlier, as well as the implementation of a special transaction type used to implement atomic schema changes. It then describes some refinements of the basic schemes as described.

**4.2.1 Read-Write Transactions**

Like Bigtable, writes that occur in a transaction are buffered at the client until commit. As a result, reads in a transaction do not see the effects of the transaction's writes. This design works well in Spanner because a read returns the timestamps of any data read, and uncommitted writes have not yet been assigned timestamps.

Reads within read-write transactions use wound-wait [33] to avoid deadlocks. The client issues reads to the leader replica of the appropriate group, which acquires read locks and then reads the most recent data. While a client transaction remains open, it sends keepalive messages to prevent participant leaders from timing out its transaction. When a client has completed all reads and buffered all writes, it begins two-phase commit. The client chooses a coordinator group and sends a commit message to each participant's leader with the identity of the coordinator and any buffered writes. Having the client drive two-phase commit avoids sending data twice across wide-area links.

A non-coordinator-participant leader first acquires write locks. It then chooses a prepare timestamp that must be larger than any timestamps it has assigned to previous transactions (to preserve monotonicity), and logs a prepare record through Paxos. Each participant then notifies the coordinator of its prepare timestamp.

The coordinator leader also first acquires write locks, but skips the prepare phase. It chooses a timestamp for the entire transaction after hearing from all other participant leaders. The commit timestamp s must be greater or equal to all prepare timestamps (to satisfy the constraints discussed in Section 4.1.3), greater than TT.now().latest at the time the coordinator received its commit message, and greater than any timestamps the leader has assigned to previous transactions (again, to preserve monotonicity). The coordinator leader then logs a commit record through Paxos (or an abort if it timed out while waiting on the other participants).

Before allowing any coordinator replica to apply the commit record, the coordinator leader waits until TT.after(s), so as to obey the commit-wait rule described in Section 4.1.2. Because the coordinator leader chose s based on TT.now().latest, and now waits until that timestamp is guaranteed to be in the past, the expected wait is at least 2*ε̄. This wait is typically overlapped with Paxos communication. After commit wait, the coordinator sends the commit timestamp to the client and all other participant leaders. Each participant leader logs the transaction's outcome through Paxos. All participants apply at the same timestamp and then release locks.

**4.2.2 Read-Only Transactions**

Assigning a timestamp requires a negotiation phase between all of the Paxos groups that are involved in the reads. As a result, Spanner requires a scope expression for every read-only transaction, which is an expression that summarizes the keys that will be read by the entire transaction. Spanner automatically infers the scope for standalone queries.

If the scope's values are served by a single Paxos group, then the client issues the read-only transaction to that group's leader. (The current Spanner implementation only chooses a timestamp for a read-only transaction at a Paxos leader.) That leader assigns s_read and executes the read. For a single-site read, Spanner generally does better than TT.now().latest. Define LastTS() to be the timestamp of the last committed write at a Paxos group. If there are no prepared transactions, the assignment s_read = LastTS() trivially satisfies external consistency: the transaction will see the result of the last write, and therefore be ordered after it.

If the scope's values are served by multiple Paxos groups, there are several options. The most complicated option is to do a round of communication with all of the groups's leaders to negotiate s_read based on LastTS(). Spanner currently implements a simpler choice. The client avoids a negotiation round, and just has its reads execute at s_read = TT.now().latest (which may wait for safe time to advance). All reads in the transaction can be sent to replicas that are sufficiently up-to-date.

**4.2.3 Schema-Change Transactions**

TrueTime enables Spanner to support atomic schema changes. It would be infeasible to use a standard transaction, because the number of participants (the number of groups in a database) could be in the millions. Bigtable supports atomic schema changes in one datacenter, but its schema changes block all operations.

A Spanner schema-change transaction is a generally non-blocking variant of a standard transaction. First, it is explicitly assigned a timestamp in the future, which is registered in the prepare phase. As a result, schema changes across thousands of servers can complete with minimal disruption to other concurrent activity. Second, reads and writes, which implicitly depend on the schema, synchronize with any registered schema-change timestamp at time t: they may proceed if their timestamps precede t, but they must block behind the schema-change transaction if their timestamps are after t. Without TrueTime, defining the schema change to happen at t would be meaningless.

**4.2.4 Refinements**

t^TM_safe as defined above has a weakness, in that a single prepared transaction prevents t_safe from advancing. As a result, no reads can occur at later timestamps, even if the reads do not conflict with the transaction. Such false conflicts can be removed by augmenting t^TM_safe with a fine-grained mapping from key ranges to prepared-transaction timestamps. This information can be stored in the lock table, which already maps key ranges to lock metadata. When a read arrives, it only needs to be checked against the fine-grained safe time for key ranges with which the read conflicts.

LastTS() as defined above has a similar weakness: if a transaction has just committed, a non-conflicting read-only transaction must still be assigned s_read so as to follow that transaction. As a result, the execution of the read could be delayed. This weakness can be remedied similarly by augmenting LastTS() with a fine-grained mapping from key ranges to commit timestamps in the lock table. (We have not yet implemented this optimization.) When a read-only transaction arrives, its timestamp can be assigned by taking the maximum value of LastTS() for the key ranges with which the transaction conflicts, unless there is a conflicting prepared transaction (which can be determined from fine-grained safe time).

t^Paxos_safe as defined above has a weakness in that it cannot advance in the absence of Paxos writes. That is, a snapshot read at t cannot execute at Paxos groups whose last write happened before t. Spanner addresses this problem by taking advantage of the disjointness of leader-lease intervals. Each Paxos leader advances t^Paxos_safe by keeping a threshold above which future writes' timestamps will occur: it maintains a mapping MinNextTS(n) from Paxos sequence number n to the minimum timestamp that may be assigned to Paxos sequence number n+1. A replica can advance t^Paxos_safe to MinNextTS(n) - 1 when it has applied through n.

A single leader can enforce its MinNextTS() promises easily. Because the timestamps promised by MinNextTS() lie within a leader's lease, the disjointness invariant enforces MinNextTS() promises across leaders. If a leader wishes to advance MinNextTS() beyond the end of its leader lease, it must first extend its lease. Note that s_max is always advanced to the highest value in MinNextTS() to preserve disjointness.

A leader by default advances MinNextTS() values every 8 seconds. Thus, in the absence of prepared transactions, healthy slaves in an idle Paxos group can serve reads at timestamps greater than 8 seconds old in the worst case. A leader may also advance MinNextTS() values on demand from slaves.

---

### النسخة العربية

يصف هذا القسم كيفية استخدام TrueTime لضمان خصائص الصحة المتعلقة بالتحكم في التزامن، وكيفية استخدام هذه الخصائص لتنفيذ ميزات مثل المعاملات ذات الاتساق الخارجي، والمعاملات للقراءة فقط الخالية من الأقفال، والقراءات غير المحجوبة في الماضي. تمكّن هذه الميزات، على سبيل المثال، الضمان بأن قراءة تدقيق لقاعدة البيانات بأكملها عند طابع زمني t سترى بالضبط آثار كل معاملة تم تنفيذها حتى t.

في المستقبل، سيكون من المهم التمييز بين الكتابات كما يراها باكسوس (والتي سنشير إليها باسم كتابات باكسوس ما لم يكن السياق واضحاً) من كتابات عميل سبانر. على سبيل المثال، يولد التنفيذ ثنائي المرحلة كتابة باكسوس لمرحلة الإعداد ليس لها كتابة عميل سبانر مقابلة.

**4.1 إدارة الطوابع الزمنية**

يسرد الجدول 2 أنواع العمليات التي تدعمها سبانر. يدعم تنفيذ سبانر معاملات القراءة-الكتابة، ومعاملات القراءة فقط (معاملات عزل اللقطة المعلنة مسبقاً)، وقراءات اللقطة. يتم تنفيذ الكتابات المستقلة كمعاملات قراءة-كتابة؛ ويتم تنفيذ القراءات المستقلة غير اللقطة كمعاملات قراءة فقط. كلاهما يتم إعادة محاولته داخلياً (لا يحتاج العملاء إلى كتابة حلقات إعادة محاولة خاصة بهم).

معاملة القراءة فقط هي نوع من المعاملات التي لها فوائد أداء عزل اللقطة [6]. يجب التصريح مسبقاً بأن معاملة القراءة فقط ليس لها أي كتابات؛ إنها ليست مجرد معاملة قراءة-كتابة بدون أي كتابات. تُنفذ القراءات في معاملة القراءة فقط عند طابع زمني يختاره النظام بدون قفل، بحيث لا يتم حجب الكتابات الواردة. يمكن أن يستمر تنفيذ القراءات في معاملة القراءة فقط على أي نسخة محدثة بما فيه الكفاية (القسم 4.1.3).

قراءة اللقطة هي قراءة في الماضي تُنفذ بدون قفل. يمكن للعميل إما تحديد طابع زمني لقراءة اللقطة، أو توفير حد أعلى على القدم المرغوب للطابع الزمني والسماح لسبانر باختيار طابع زمني. في كلتا الحالتين، يستمر تنفيذ قراءة اللقطة على أي نسخة محدثة بما فيه الكفاية.

لكل من معاملات القراءة فقط وقراءات اللقطة، يكون التنفيذ حتمياً بمجرد اختيار طابع زمني، ما لم يتم جمع البيانات عند ذلك الطابع الزمني كقمامة. ونتيجة لذلك، يمكن للعملاء تجنب تخزين النتائج مؤقتاً داخل حلقة إعادة محاولة. عندما يفشل خادم، يمكن للعملاء متابعة الاستعلام داخلياً على خادم مختلف عن طريق تكرار الطابع الزمني وموضع القراءة الحالي.

**4.1.1 عقود إيجار قائد باكسوس**

يستخدم تنفيذ باكسوس في سبانر عقود إيجار موقوتة لجعل القيادة طويلة العمر (10 ثوانٍ افتراضياً). يرسل القائد المحتمل طلبات لأصوات عقد الإيجار الموقوتة؛ عند تلقي النصاب من أصوات عقد الإيجار يعلم القائد أن لديه عقد إيجار. تمدد النسخة تصويتها لعقد الإيجار ضمنياً عند كتابة ناجحة، ويطلب القائد تمديدات أصوات عقد الإيجار إذا كانت قريبة من انتهاء الصلاحية. عرّف فترة عقد إيجار القائد على أنها تبدأ عندما يكتشف أن لديه نصاباً من أصوات عقد الإيجار، وتنتهي عندما لا يعود لديه نصاب من أصوات عقد الإيجار (لأن البعض قد انتهت صلاحيته). تعتمد سبانر على ثابت الانفصال التالي: لكل مجموعة باكسوس، فترة عقد إيجار كل قائد باكسوس منفصلة عن كل قائد آخر. يصف الملحق A كيفية فرض هذا الثابت.

يسمح تنفيذ سبانر لقائد باكسوس بالتنازل عن طريق إطلاق عبيده من أصوات عقد الإيجار الخاصة بهم. للحفاظ على ثابت الانفصال، تقيد سبانر متى يكون التنازل مسموحاً. عرّف s_max كأكبر طابع زمني يستخدمه القائد. ستصف الأقسام اللاحقة متى يتم تقديم s_max. قبل التنازل، يجب على القائد الانتظار حتى يصبح TT.after(s_max) صحيحاً.

**4.1.2 تعيين الطوابع الزمنية لمعاملات القراءة-الكتابة**

تستخدم القراءات والكتابات المعاملاتية القفل ثنائي المرحلة. ونتيجة لذلك، يمكن تعيين طوابع زمنية لها في أي وقت عندما يتم الحصول على جميع الأقفال، ولكن قبل إطلاق أي أقفال. لمعاملة معينة، تعين سبانر لها الطابع الزمني الذي يعينه باكسوس لكتابة باكسوس التي تمثل تنفيذ المعاملة.

تعتمد سبانر على ثابت الرتابة التالي: داخل كل مجموعة باكسوس، تعين سبانر طوابع زمنية لكتابات باكسوس بترتيب تزايدي رتيب، حتى عبر القادة. يمكن لنسخة قائد واحدة ببساطة تعيين طوابع زمنية بترتيب تزايدي رتيب. يتم فرض هذا الثابت عبر القادة عن طريق الاستفادة من ثابت الانفصال: يجب على القائد تعيين طوابع زمنية فقط ضمن فترة عقد إيجار قيادته. لاحظ أنه كلما تم تعيين طابع زمني s، يتم تقديم s_max إلى s للحفاظ على الانفصال.

تفرض سبانر أيضاً ثابت الاتساق الخارجي التالي: إذا حدث بدء معاملة T₂ بعد تنفيذ معاملة T₁، فإن طابع تنفيذ T₂ يجب أن يكون أكبر من طابع تنفيذ T₁. عرّف أحداث البدء والتنفيذ لمعاملة Tᵢ بـ e^start_i و e^commit_i؛ وطابع تنفيذ معاملة Tᵢ بـ sᵢ. يصبح الثابت t_abs(e^commit_1) < t_abs(e^start_2) ⇒ s₁ < s₂.

يطيع بروتوكول تنفيذ المعاملات وتعيين الطوابع الزمنية قاعدتين، اللتان تضمنان معاً هذا الثابت، كما هو موضح أدناه. عرّف حدث وصول طلب التنفيذ عند قائد المنسق لكتابة Tᵢ ليكون e^server_i.

**البدء:** يعين قائد المنسق لكتابة Tᵢ طابع تنفيذ sᵢ لا يقل عن قيمة TT.now().latest، المحسوبة بعد e^server_i. لاحظ أن قادة المشاركين لا يهمون هنا؛ يصف القسم 4.2.1 كيف يشاركون في تنفيذ القاعدة التالية.

**انتظار التنفيذ:** يضمن قائد المنسق أن العملاء لا يمكنهم رؤية أي بيانات تم تنفيذها بواسطة Tᵢ حتى يصبح TT.after(sᵢ) صحيحاً. يضمن انتظار التنفيذ أن sᵢ أقل من وقت التنفيذ المطلق لـ Tᵢ، أو sᵢ < t_abs(e^commit_i). يتم وصف تنفيذ انتظار التنفيذ في القسم 4.2.1.

**البرهان:**
```
s₁ < t_abs(e^commit_1)     (انتظار التنفيذ)
t_abs(e^commit_1) < t_abs(e^start_2)     (افتراض)
t_abs(e^start_2) ≤ t_abs(e^server_2)     (السببية)
t_abs(e^server_2) ≤ s₂     (البدء)
s₁ < s₂     (التعدية)
```

**4.1.3 تقديم القراءات عند طابع زمني**

يسمح ثابت الرتابة الموصوف في القسم 4.1.2 لسبانر بتحديد ما إذا كانت حالة النسخة محدثة بما فيه الكفاية لتلبية قراءة بشكل صحيح. تتتبع كل نسخة قيمة تسمى الوقت الآمن t_safe وهو أقصى طابع زمني تكون عنده النسخة محدثة. يمكن للنسخة تلبية قراءة عند طابع زمني t إذا كان t ≤ t_safe.

عرّف t_safe = min(t^Paxos_safe, t^TM_safe)، حيث لكل آلة حالة باكسوس وقت آمن t^Paxos_safe ولكل مدير معاملات وقت آمن t^TM_safe. t^Paxos_safe أبسط: إنه الطابع الزمني لأعلى كتابة باكسوس مطبقة. نظراً لأن الطوابع الزمنية تزداد بشكل رتيب ويتم تطبيق الكتابات بالترتيب، لن تحدث الكتابات بعد الآن عند أو أقل من t^Paxos_safe فيما يتعلق بباكسوس.

t^TM_safe هو ∞ عند نسخة إذا كان هناك صفر معاملة محضرة (ولكن غير منفذة)—أي المعاملات بين المرحلتين من التنفيذ ثنائي المرحلة. (بالنسبة لعبد مشارك، يشير t^TM_safe في الواقع إلى مدير معاملات قائد النسخة، الذي يمكن للعبد استنتاج حالته من خلال البيانات الوصفية الممررة على كتابات باكسوس.) إذا كان هناك أي من هذه المعاملات، فإن الحالة المتأثرة بتلك المعاملات غير محددة: لا تعلم نسخة المشارك بعد ما إذا كانت هذه المعاملات ستنفذ. كما نناقش في القسم 4.2.1، يضمن بروتوكول التنفيذ أن كل مشارك يعلم حداً أدنى على طابع زمني المعاملة المحضرة. يعين كل قائد مشارك (لمجموعة g) لمعاملة Tᵢ طابع إعداد s^prepare_i,g لسجل إعداده. يضمن قائد المنسق أن طابع تنفيذ المعاملة sᵢ ≥ s^prepare_i,g عبر جميع مجموعات المشاركين g. لذلك، لكل نسخة في مجموعة g، عبر جميع المعاملات Tᵢ المحضرة في g، t^TM_safe = minᵢ(s^prepare_i,g) - 1 عبر جميع المعاملات المحضرة في g.

**4.1.4 تعيين الطوابع الزمنية لمعاملات القراءة فقط**

تُنفذ معاملة القراءة فقط في مرحلتين: تعيين طابع زمني s_read [8]، ثم تنفيذ قراءات المعاملة كقراءات لقطة عند s_read. يمكن أن تُنفذ قراءات اللقطة عند أي نسخ محدثة بما فيه الكفاية.

التعيين البسيط s_read = TT.now().latest، في أي وقت بعد بدء المعاملة، يحفظ الاتساق الخارجي بحجة مماثلة لتلك المقدمة للكتابات في القسم 4.1.2. ومع ذلك، قد يتطلب مثل هذا الطابع الزمني أن يُحجب تنفيذ قراءات البيانات عند s_read إذا لم يتقدم t_safe بما فيه الكفاية. (بالإضافة إلى ذلك، لاحظ أن اختيار قيمة s_read قد يقدم أيضاً s_max للحفاظ على الانفصال.) لتقليل فرص الحجب، يجب على سبانر تعيين أقدم طابع زمني يحفظ الاتساق الخارجي. يشرح القسم 4.2.2 كيف يمكن اختيار مثل هذا الطابع الزمني.

**4.2 التفاصيل**

يشرح هذا القسم بعض التفاصيل العملية لمعاملات القراءة-الكتابة ومعاملات القراءة فقط التي تم حذفها سابقاً، بالإضافة إلى تنفيذ نوع معاملة خاص يُستخدم لتنفيذ تغييرات المخطط الذرية. ثم يصف بعض التحسينات على المخططات الأساسية كما هو موصوف.

**4.2.1 معاملات القراءة-الكتابة**

مثل Bigtable، الكتابات التي تحدث في معاملة يتم تخزينها مؤقتاً في العميل حتى التنفيذ. ونتيجة لذلك، لا ترى القراءات في المعاملة آثار كتابات المعاملة. يعمل هذا التصميم بشكل جيد في سبانر لأن القراءة تعيد الطوابع الزمنية لأي بيانات مقروءة، والكتابات غير المنفذة لم يتم تعيين طوابع زمنية لها بعد.

تستخدم القراءات ضمن معاملات القراءة-الكتابة الجرح-انتظار (wound-wait) [33] لتجنب الجمود. يصدر العميل قراءات إلى النسخة القائدة للمجموعة المناسبة، والتي تحصل على أقفال القراءة ثم تقرأ أحدث البيانات. طالما ظلت معاملة العميل مفتوحة، فإنها ترسل رسائل حفظ الحياة لمنع قادة المشاركين من انتهاء مهلة معاملتها. عندما يكمل العميل جميع القراءات ويخزن جميع الكتابات مؤقتاً، يبدأ التنفيذ ثنائي المرحلة. يختار العميل مجموعة منسق ويرسل رسالة تنفيذ إلى قائد كل مشارك مع هوية المنسق وأي كتابات مخزنة مؤقتاً. قيادة العميل للتنفيذ ثنائي المرحلة تتجنب إرسال البيانات مرتين عبر روابط المنطقة الواسعة.

يحصل قائد المشارك غير المنسق أولاً على أقفال الكتابة. ثم يختار طابع إعداد يجب أن يكون أكبر من أي طوابع زمنية عينها للمعاملات السابقة (للحفاظ على الرتابة)، ويسجل سجل إعداد من خلال باكسوس. ثم يخطر كل مشارك المنسق بطابع إعداده.

يحصل قائد المنسق أيضاً أولاً على أقفال الكتابة، لكنه يتخطى مرحلة الإعداد. يختار طابعاً زمنياً للمعاملة بأكملها بعد سماعه من جميع قادة المشاركين الآخرين. يجب أن يكون طابع التنفيذ s أكبر من أو يساوي جميع طوابع الإعداد (لتلبية القيود المناقشة في القسم 4.1.3)، وأكبر من TT.now().latest في الوقت الذي تلقى فيه المنسق رسالة تنفيذه، وأكبر من أي طوابع زمنية عينها القائد للمعاملات السابقة (مرة أخرى، للحفاظ على الرتابة). ثم يسجل قائد المنسق سجل تنفيذ من خلال باكسوس (أو إجهاض إذا انتهت المهلة أثناء الانتظار على المشاركين الآخرين).

قبل السماح لأي نسخة منسق بتطبيق سجل التنفيذ، ينتظر قائد المنسق حتى TT.after(s)، من أجل إطاعة قاعدة انتظار التنفيذ الموصوفة في القسم 4.1.2. نظراً لأن قائد المنسق اختار s بناءً على TT.now().latest، والآن ينتظر حتى يُضمن أن يكون ذلك الطابع الزمني في الماضي، فإن الانتظار المتوقع هو على الأقل 2*ε̄. عادةً ما يتداخل هذا الانتظار مع اتصال باكسوس. بعد انتظار التنفيذ، يرسل المنسق طابع التنفيذ إلى العميل وجميع قادة المشاركين الآخرين. يسجل كل قائد مشارك نتيجة المعاملة من خلال باكسوس. يطبق جميع المشاركين عند نفس الطابع الزمني ثم يطلقون الأقفال.

**4.2.2 معاملات القراءة فقط**

يتطلب تعيين طابع زمني مرحلة تفاوض بين جميع مجموعات باكسوس المشاركة في القراءات. ونتيجة لذلك، تتطلب سبانر تعبير نطاق لكل معاملة قراءة فقط، وهو تعبير يلخص المفاتيح التي ستقرأها المعاملة بأكملها. تستنتج سبانر تلقائياً النطاق للاستعلامات المستقلة.

إذا تم تقديم قيم النطاق بواسطة مجموعة باكسوس واحدة، فإن العميل يصدر معاملة القراءة فقط إلى قائد تلك المجموعة. (التنفيذ الحالي لسبانر يختار فقط طابعاً زمنياً لمعاملة قراءة فقط عند قائد باكسوس.) يعين ذلك القائد s_read وينفذ القراءة. للقراءة أحادية الموقع، تقوم سبانر عموماً بعمل أفضل من TT.now().latest. عرّف LastTS() ليكون طابع آخر كتابة منفذة في مجموعة باكسوس. إذا لم يكن هناك معاملات محضرة، فإن التعيين s_read = LastTS() يلبي الاتساق الخارجي بشكل تافه: سترى المعاملة نتيجة آخر كتابة، وبالتالي سيتم ترتيبها بعدها.

إذا تم تقديم قيم النطاق بواسطة مجموعات باكسوس متعددة، هناك عدة خيارات. الخيار الأكثر تعقيداً هو القيام بجولة اتصال مع جميع قادة المجموعات للتفاوض على s_read بناءً على LastTS(). تنفذ سبانر حالياً اختياراً أبسط. يتجنب العميل جولة تفاوض، ويجعل قراءاته تُنفذ عند s_read = TT.now().latest (والتي قد تنتظر تقدم الوقت الآمن). يمكن إرسال جميع القراءات في المعاملة إلى النسخ المحدثة بما فيه الكفاية.

**4.2.3 معاملات تغيير المخطط**

تمكّن TrueTime سبانر من دعم تغييرات المخطط الذرية. سيكون من غير الممكن استخدام معاملة قياسية، لأن عدد المشاركين (عدد المجموعات في قاعدة بيانات) يمكن أن يكون بالملايين. يدعم Bigtable تغييرات المخطط الذرية في مركز بيانات واحد، لكن تغييرات مخططه تحجب جميع العمليات.

معاملة تغيير مخطط سبانر هي نوع غير محجوب عموماً من معاملة قياسية. أولاً، يتم تعيين طابع زمني لها صراحةً في المستقبل، والذي يتم تسجيله في مرحلة الإعداد. ونتيجة لذلك، يمكن أن تكتمل تغييرات المخطط عبر آلاف الخوادم مع الحد الأدنى من التعطيل للنشاط المتزامن الآخر. ثانياً، القراءات والكتابات، التي تعتمد ضمنياً على المخطط، تتزامن مع أي طابع زمني مسجل لتغيير المخطط في الوقت t: قد تستمر إذا كانت طوابعها الزمنية تسبق t، لكن يجب أن تُحجب خلف معاملة تغيير المخطط إذا كانت طوابعها الزمنية بعد t. بدون TrueTime، سيكون تحديد تغيير المخطط ليحدث عند t بلا معنى.

**4.2.4 التحسينات**

t^TM_safe كما هو معرف أعلاه له نقطة ضعف، من حيث أن معاملة محضرة واحدة تمنع t_safe من التقدم. ونتيجة لذلك، لا يمكن أن تحدث قراءات عند طوابع زمنية لاحقة، حتى لو لم تتعارض القراءات مع المعاملة. يمكن إزالة هذه التعارضات الخاطئة عن طريق إضافة تعيين دقيق من نطاقات المفاتيح إلى طوابع زمنية المعاملات المحضرة إلى t^TM_safe. يمكن تخزين هذه المعلومات في جدول الأقفال، الذي يعيّن بالفعل نطاقات المفاتيح إلى بيانات تعريف الأقفال. عندما تصل قراءة، يحتاج فقط إلى التحقق منها مقابل الوقت الآمن الدقيق لنطاقات المفاتيح التي تتعارض معها القراءة.

LastTS() كما هو معرف أعلاه له نقطة ضعف مماثلة: إذا كانت معاملة قد نُفذت للتو، يجب أن يتم تعيين s_read لمعاملة قراءة فقط غير متعارضة بحيث تتبع تلك المعاملة. ونتيجة لذلك، يمكن أن يتأخر تنفيذ القراءة. يمكن معالجة نقطة الضعف هذه بالمثل عن طريق إضافة تعيين دقيق من نطاقات المفاتيح إلى طوابع تنفيذ في جدول الأقفال إلى LastTS(). (لم ننفذ هذا التحسين بعد.) عندما تصل معاملة قراءة فقط، يمكن تعيين طابعها الزمني عن طريق أخذ القيمة القصوى لـ LastTS() لنطاقات المفاتيح التي تتعارض معها المعاملة، ما لم تكن هناك معاملة محضرة متعارضة (والتي يمكن تحديدها من الوقت الآمن الدقيق).

t^Paxos_safe كما هو معرف أعلاه له نقطة ضعف من حيث أنه لا يمكن أن يتقدم في غياب كتابات باكسوس. أي أن قراءة لقطة عند t لا يمكن أن تُنفذ في مجموعات باكسوس التي حدثت آخر كتابة لها قبل t. تعالج سبانر هذه المشكلة عن طريق الاستفادة من انفصال فترات عقد إيجار القائد. يقدم كل قائد باكسوس t^Paxos_safe من خلال الاحتفاظ بعتبة فوقها ستحدث طوابع زمنية الكتابات المستقبلية: يحافظ على تعيين MinNextTS(n) من رقم تسلسل باكسوس n إلى الطابع الزمني الأدنى الذي قد يتم تعيينه لرقم تسلسل باكسوس n+1. يمكن للنسخة تقديم t^Paxos_safe إلى MinNextTS(n) - 1 عندما تطبق حتى n.

يمكن لقائد واحد فرض وعود MinNextTS() الخاصة به بسهولة. نظراً لأن الطوابع الزمنية الموعودة بواسطة MinNextTS() تقع ضمن عقد إيجار القائد، فإن ثابت الانفصال يفرض وعود MinNextTS() عبر القادة. إذا أراد قائد تقديم MinNextTS() إلى ما بعد نهاية عقد إيجار قيادته، يجب عليه أولاً تمديد عقد إيجاره. لاحظ أن s_max يتم تقديمه دائماً إلى أعلى قيمة في MinNextTS() للحفاظ على الانفصال.

يقدم القائد افتراضياً قيم MinNextTS() كل 8 ثوانٍ. وبالتالي، في غياب المعاملات المحضرة، يمكن للعبيد الأصحاء في مجموعة باكسوس خاملة تقديم قراءات عند طوابع زمنية أكبر من 8 ثوانٍ قديمة في أسوأ الحالات. قد يقدم القائد أيضاً قيم MinNextTS() عند الطلب من العبيد.

---

### Translation Notes

- **Figures referenced:** None in text, Table 2 and Table 3 mentioned
- **Tables referenced:** Table 2 (Types of reads and writes), Table 3 (Operation microbenchmarks - at end)
- **Key terms introduced:**
  - External consistency (الاتساق الخارجي)
  - Linearizability (الخطية)
  - Snapshot isolation (عزل اللقطة)
  - Read-write transaction (معاملة قراءة-كتابة)
  - Read-only transaction (معاملة قراءة فقط)
  - Snapshot read (قراءة اللقطة)
  - Safe time (الوقت الآمن)
  - Paxos leader lease (عقد إيجار قائد باكسوس)
  - Disjointness invariant (ثابت الانفصال)
  - Monotonicity invariant (ثابت الرتابة)
  - Commit wait (انتظار التنفيذ)
  - Wound-wait (الجرح-انتظار)
  - Scope expression (تعبير النطاق)
  - Schema-change transaction (معاملة تغيير المخطط)
  - LastTS() (آخر طابع زمني)
  - MinNextTS() (أدنى طابع زمني تالٍ)
- **Equations/Formal logic:**
  - t_abs(e^commit_1) < t_abs(e^start_2) ⇒ s₁ < s₂
  - t ≤ t_safe
  - t_safe = min(t^Paxos_safe, t^TM_safe)
  - t^TM_safe = minᵢ(s^prepare_i,g) - 1
  - Expected wait: 2*ε̄
- **Citations:** [6], [8], [33]
- **Special handling:**
  - Mathematical notation preserved with subscripts/superscripts
  - Proof structure maintained
  - Algorithm names kept in English (wound-wait)
  - Function names kept as-is: TT.now(), TT.after(), LastTS(), MinNextTS()

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.92
- Readability: 0.82
- Glossary consistency: 0.95
- **Overall section score:** 0.86
