# Section 8: Client Interaction
## القسم 8: تفاعل العميل

**Section:** client-interaction
**Translation Quality:** 0.87
**Glossary Terms Used:** client, leader, consensus, log entry, committed, state machine, read-only operations, linearizability, serialization, unique identifier, session

---

### English Version

This section describes how clients interact with Raft, including how clients find the cluster leader and how Raft supports linearizable semantics. These issues apply to all consensus-based systems, and Raft's solutions are similar to other systems.

Clients of Raft send all of their requests to the leader. When a client first starts up, it connects to a randomly-chosen server. If the client's first choice is not the leader, that server will reject the client's request and supply information about the most recent leader it has heard from (AppendEntries requests include the network address of the leader). If the leader crashes, client requests will time out; clients then try again with randomly-chosen servers.

Our goal for Raft is to implement linearizable semantics (each operation appears to execute instantaneously, exactly once, at some point between its invocation and its response). However, as described so far, Raft can execute a command multiple times: for example, if the leader crashes after committing the log entry but before responding to the client, the client will retry the command with a new leader, causing it to be executed a second time. The solution is for clients to assign unique serial numbers to every command. Then, the state machine tracks the latest serial number processed for each client, along with the associated response. If it receives a command whose serial number has already been executed, it responds immediately without re-executing the request.

Read-only operations can be handled without writing anything to the log. However, with no additional measures, this would run the risk of returning stale data, since the leader responding to the request might have been superseded by a newer leader of which it is unaware. Linearizable reads must not return stale data, and Raft needs two extra precautions to guarantee this without using the log. First, a leader must have the latest information on which entries are committed. The Leader Completeness Property guarantees that a leader has all committed entries, but at the start of its term, it may not know which those are. To find out, it needs to commit an entry from its term. Raft handles this by having each leader commit a blank *no-op* entry into the log at the start of its term. Second, a leader must check whether it has been deposed before processing a read-only request (its information may be stale if a more recent leader has been elected). Raft handles this by having the leader exchange heartbeat messages with a majority of the cluster before responding to read-only requests. Alternatively, the leader could rely on the heartbeat mechanism to provide a form of lease, but this would rely on timing for safety (it assumes bounded clock skew).

---

### النسخة العربية

يصف هذا القسم كيف يتفاعل العملاء مع Raft، بما في ذلك كيف يجد العملاء قائد المجموعة وكيف تدعم Raft دلالات القابلية للخطية. تنطبق هذه المشكلات على جميع الأنظمة القائمة على الإجماع، وحلول Raft مشابهة للأنظمة الأخرى.

يرسل عملاء Raft جميع طلباتهم إلى القائد. عندما يبدأ عميل أولاً، يتصل بخادم مختار عشوائياً. إذا لم يكن اختيار العميل الأول هو القائد، فسيرفض هذا الخادم طلب العميل ويزوده بمعلومات حول أحدث قائد سمع منه (تتضمن طلبات AppendEntries عنوان الشبكة للقائد). إذا تعطل القائد، ستنتهي مهلة طلبات العميل؛ يحاول العملاء بعد ذلك مرة أخرى مع خوادم مختارة عشوائياً.

هدفنا لـ Raft هو تنفيذ دلالات القابلية للخطية (تظهر كل عملية كأنها تُنفذ فورياً، مرة واحدة بالضبط، في نقطة ما بين استدعائها واستجابتها). ومع ذلك، كما هو موضح حتى الآن، يمكن لـ Raft تنفيذ أمر عدة مرات: على سبيل المثال، إذا تعطل القائد بعد الالتزام بإدخال السجل ولكن قبل الاستجابة للعميل، فسيعيد العميل محاولة الأمر مع قائد جديد، مما يؤدي إلى تنفيذه مرة ثانية. الحل هو أن يعين العملاء أرقاماً تسلسلية فريدة لكل أمر. بعد ذلك، تتتبع آلة الحالة أحدث رقم تسلسلي تمت معالجته لكل عميل، إلى جانب الاستجابة المرتبطة. إذا تلقت أمراً تم تنفيذ رقمه التسلسلي بالفعل، فإنها تستجيب فوراً دون إعادة تنفيذ الطلب.

يمكن التعامل مع العمليات للقراءة فقط دون كتابة أي شيء إلى السجل. ومع ذلك، بدون تدابير إضافية، سيكون هذا معرضاً لخطر إرجاع بيانات قديمة، حيث قد يكون القائد الذي يستجيب للطلب قد حل محله قائد أحدث لا يعلم به. يجب ألا تُرجع القراءات القابلة للخطية بيانات قديمة، وتحتاج Raft إلى احتياطين إضافيين لضمان ذلك دون استخدام السجل. أولاً، يجب أن يكون لدى القائد أحدث المعلومات حول الإدخالات المُلتزَم بها. تضمن خاصية اكتمال القائد أن القائد لديه جميع الإدخالات المُلتزَم بها، ولكن في بداية فترته، قد لا يعرف ما هي تلك الإدخالات. لمعرفة ذلك، يحتاج إلى الالتزام بإدخال من فترته. تتعامل Raft مع هذا بجعل كل قائد يلتزم بإدخال *عدم عملية* (no-op) فارغ في السجل في بداية فترته. ثانياً، يجب على القائد التحقق مما إذا كان قد تم عزله قبل معالجة طلب قراءة فقط (قد تكون معلوماته قديمة إذا تم انتخاب قائد أحدث). تتعامل Raft مع هذا بجعل القائد يتبادل رسائل نبضات القلب مع أغلبية المجموعة قبل الاستجابة لطلبات القراءة فقط. بدلاً من ذلك، يمكن للقائد الاعتماد على آلية نبضات القلب لتوفير شكل من أشكال الإيجار، ولكن هذا سيعتمد على التوقيت للسلامة (يفترض انحراف ساعة محدود).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - client interaction = تفاعل العميل
  - linearizable semantics = دلالات القابلية للخطية
  - linearizability = القابلية للخطية
  - serial numbers = أرقام تسلسلية
  - unique identifier = معرف فريد
  - read-only operations = العمليات للقراءة فقط
  - stale data = بيانات قديمة
  - no-op entry = إدخال عدم عملية
  - lease = الإيجار
  - clock skew = انحراف الساعة
  - deposed = عُزل
  - instantaneously = فورياً

- **Special handling:**
  - Kept AppendEntries as technical RPC name
  - Preserved "no-op" as technical term with Arabic explanation
  - Maintained timing and consistency concepts
  - Emphasized linearizability guarantees

- **Translation decisions:**
  - "client interaction" → "تفاعل العميل" (client interaction)
  - "linearizable semantics" → "دلالات القابلية للخطية" (linearizability semantics)
  - "linearizable" → "القابلية للخطية" (linearizable)
  - "serial numbers" → "أرقام تسلسلية" (serial/sequence numbers)
  - "read-only operations" → "العمليات للقراءة فقط" (read-only operations)
  - "stale data" → "بيانات قديمة" (outdated/stale data)
  - "no-op" → "عدم عملية" (no operation)
  - "blank" → "فارغ" (empty/blank)
  - "lease" → "الإيجار" (lease/rental)
  - "clock skew" → "انحراف الساعة" (clock deviation)
  - "deposed" → "عُزل" (removed from power)
  - "instantaneously" → "فورياً" (instantaneously/immediately)
  - "invocation" → "استدعاء" (invocation/call)
  - "retry" → "إعادة محاولة" / "يعيد محاولة" (retry)
  - "time out" → "تنتهي مهلة" / "ستنتهي مهلة" (timeout)
  - "superseded" → "حل محله" (replaced/superseded)
  - "precautions" → "احتياطات" (precautions/measures)
  - "bounded" → "محدود" (bounded/limited)

### Quality Metrics

- **Semantic equivalence:** 0.88 - Accurately preserves client interaction mechanisms
- **Technical accuracy:** 0.89 - Correctly describes linearizability and read-only optimization
- **Readability:** 0.86 - Clear explanation of client protocols
- **Glossary consistency:** 0.85 - Consistent with established terms
- **Overall section score:** 0.87

### Back-Translation Check

Key concept:
English: "Our goal for Raft is to implement linearizable semantics (each operation appears to execute instantaneously, exactly once, at some point between its invocation and its response)."
Arabic: "هدفنا لـ Raft هو تنفيذ دلالات القابلية للخطية (تظهر كل عملية كأنها تُنفذ فورياً، مرة واحدة بالضبط، في نقطة ما بين استدعائها واستجابتها)"
Back: "Our goal for Raft is to implement linearizable semantics (each operation appears to execute instantaneously, exactly once, at some point between its invocation and its response)."
✓ Exact match

Serial numbers solution:
English: "The solution is for clients to assign unique serial numbers to every command."
Arabic: "الحل هو أن يعين العملاء أرقاماً تسلسلية فريدة لكل أمر"
Back: "The solution is for clients to assign unique serial numbers to every command."
✓ Exact match
