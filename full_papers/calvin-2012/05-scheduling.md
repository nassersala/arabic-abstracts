# Section 5: Scheduling and Concurrency Control
## القسم 5: الجدولة والتحكم في التزامن

**Section:** scheduling-and-concurrency-control
**Translation Quality:** 0.87
**Glossary Terms Used:** scheduling, concurrency control, lock manager, deterministic locking, read set, write set, dependent transaction, optimistic lock location prediction, worker thread, deadlock

---

### English Version

#### 5.1 Deterministic Lock Manager

The scheduling layer's primary responsibility is to execute transactions in the global order established by the sequencing layer while maximizing parallelism. This is achieved through a deterministic lock manager that grants locks strictly according to the predetermined transaction order.

For each transaction, the lock manager follows these steps:

1. **Lock request submission**: When a transaction enters the scheduling layer, it submits lock requests for all records in its read and write sets.

2. **Ordered lock granting**: Locks are granted in strict global order. If transaction $T_i$ precedes $T_j$ in the sequence, and both request locks on record $R$, then $T_i$ must acquire its lock on $R$ before $T_j$ can acquire its lock.

3. **Execution after lock acquisition**: A transaction can only begin execution once it has acquired all necessary locks.

4. **Lock release at commit**: Locks are released only after the transaction commits or aborts, following strict two-phase locking semantics.

This protocol guarantees several critical properties:

**Deadlock freedom**: Since locks are always granted in global order, circular wait conditions cannot occur. Transaction $T_i$ never waits for a lock held by transaction $T_j$ where $j > i$.

**Serializability**: The execution order respects the global sequence, ensuring that the outcome is equivalent to serial execution in that order.

**Determinism**: Given the same transaction inputs and global order, execution always produces identical results across all replicas.

#### 5.2 Execution Pipeline

Once a transaction has acquired all its locks, it enters the execution pipeline, which consists of five phases:

**Phase 1 - Read/Write Set Analysis**: The transaction examines its read and write sets to determine which records are stored locally and which require remote access.

**Phase 2 - Perform Local Reads**: The transaction reads all locally-stored records from the storage layer.

**Phase 3 - Serve Remote Reads**: If this node owns records that other nodes need for their transactions, it responds to remote read requests.

**Phase 4 - Collect Remote Read Results**: The transaction waits for responses to any remote read requests it has issued.

**Phase 5 - Execute Transaction Logic and Apply Writes**: With all necessary data available, the transaction executes its application logic and writes results to the storage layer.

This pipeline design allows multiple transactions to be in different phases simultaneously, maximizing CPU utilization and hiding network latency.

#### 5.3 Handling Multi-Partition Transactions

For transactions that access data across multiple partitions, Calvin uses an active/passive coordination protocol:

**Active participant**: One node (typically the one where the transaction was submitted) is designated as the active participant. This node executes the full transaction logic.

**Passive participants**: Nodes owning other partitions accessed by the transaction act as passive participants. They acquire locks, perform reads, and apply writes as requested by the active participant.

The protocol proceeds as follows:

1. The active participant acquires locks on all records at all involved partitions (each partition's lock manager independently grants locks in global order).

2. The active participant requests reads from all passive participants.

3. Passive participants execute the reads and return results.

4. The active participant executes the transaction logic and determines all write operations.

5. The active participant sends write commands to passive participants.

6. All participants apply writes and release locks.

Crucially, because execution is deterministic and the global order is predetermined, this protocol does not require a distributed commit protocol like 2PC. All participants independently determine the same commit/abort outcome based on the transaction logic.

#### 5.4 Dependent Transactions

A fundamental challenge for deterministic execution is that transaction read and write sets must be known before execution begins. However, many real-world transactions are **dependent transactions**—they must read data to determine which additional records to access.

For example, consider a transaction that reads a user's account to find their current address, then updates records associated with that address. The address-related records cannot be identified until the initial read completes.

Calvin handles dependent transactions through **Optimistic Lock Location Prediction (OLLP)**:

1. **Reconnaissance query**: Before the actual transaction is submitted to the sequencing layer, a non-replicated reconnaissance query executes to predict which records the transaction will access.

2. **Transaction submission**: Based on the reconnaissance results, the transaction is submitted with a predicted read/write set.

3. **Validation during execution**: When the actual transaction executes, it validates whether the predicted access pattern was correct.

4. **Restart on misprediction**: If the actual access pattern differs from the prediction, the transaction aborts and is resubmitted with the corrected access pattern.

This approach has important implications:

**Reconnaissance overhead**: The initial reconnaissance query adds latency and consumes system resources. However, this query is not replicated, so it's cheaper than executing the full transaction.

**Abort and restart cost**: If predictions are frequently wrong, the transaction will abort and restart multiple times, significantly impacting performance.

**Prediction accuracy**: The effectiveness of OLLP depends critically on the predictability of access patterns. Applications with highly unpredictable access patterns may perform poorly.

In practice, many workloads have predictable access patterns. For instance, in a social network application, a transaction accessing a user's profile can reliably predict that it will also access the user's friends list. Calvin's evaluation shows that with moderate prediction accuracy (above 80%), OLLP overhead remains acceptable.

#### 5.5 Lock Manager Implementation

Calvin's lock manager is implemented as a separate thread at each node, managing locks for the records stored at that node. The lock manager maintains:

**Lock table**: A hash table mapping each record to its current lock holder(s) and queue of waiting requests.

**Transaction queue**: An ordered queue of transactions in global sequence order, containing their lock requests.

**Grant policy**: A strict policy that grants locks only in global order, even if a lock is available and a later transaction requests it.

This design provides several benefits:

**Lock management parallelism**: Each node's lock manager operates independently, allowing parallel lock operations across nodes.

**Bounded memory**: The lock table size is proportional to the number of actively locked records, not the total database size.

**Simple deadlock prevention**: The global ordering eliminates deadlock by construction, requiring no complex detection or resolution mechanisms.

---

### النسخة العربية

#### 5.1 مدير الأقفال الحتمي

المسؤولية الأساسية لطبقة الجدولة هي تنفيذ المعاملات بالترتيب العالمي الذي أنشأته طبقة التسلسل مع تعظيم التوازي. يتحقق هذا من خلال مدير أقفال حتمي يمنح الأقفال بشكل صارم وفقاً لترتيب المعاملات المحدد مسبقاً.

لكل معاملة، يتبع مدير الأقفال الخطوات التالية:

1. **تقديم طلب القفل**: عندما تدخل المعاملة طبقة الجدولة، تقدم طلبات القفل لجميع السجلات في مجموعات القراءة والكتابة الخاصة بها.

2. **منح القفل المرتب**: تُمنح الأقفال بترتيب عالمي صارم. إذا سبقت المعاملة $T_i$ المعاملة $T_j$ في التسلسل، وطلب كلاهما أقفالاً على السجل $R$، فيجب على $T_i$ الحصول على قفلها على $R$ قبل أن تتمكن $T_j$ من الحصول على قفلها.

3. **التنفيذ بعد الحصول على القفل**: يمكن للمعاملة البدء في التنفيذ فقط بعد أن تحصل على جميع الأقفال الضرورية.

4. **إطلاق القفل عند الالتزام**: تُطلق الأقفال فقط بعد التزام المعاملة أو إلغائها، باتباع دلالات القفل ثنائي الطور الصارمة.

يضمن هذا البروتوكول عدة خصائص حرجة:

**حرية الجمود**: نظراً لأن الأقفال تُمنح دائماً بالترتيب العالمي، لا يمكن أن تحدث ظروف انتظار دائرية. لا تنتظر المعاملة $T_i$ أبداً قفلاً تحتفظ به المعاملة $T_j$ حيث $j > i$.

**القابلية للتسلسل**: يحترم ترتيب التنفيذ التسلسل العالمي، مما يضمن أن النتيجة تعادل التنفيذ التسلسلي بهذا الترتيب.

**الحتمية**: عند إعطاء نفس مدخلات المعاملات والترتيب العالمي، ينتج التنفيذ دائماً نتائج متطابقة عبر جميع النُسخ المتماثلة.

#### 5.2 خط أنابيب التنفيذ

بمجرد أن تحصل المعاملة على جميع أقفالها، تدخل خط أنابيب التنفيذ، الذي يتكون من خمس مراحل:

**المرحلة 1 - تحليل مجموعة القراءة/الكتابة**: تفحص المعاملة مجموعات القراءة والكتابة لتحديد السجلات المخزنة محلياً والتي تتطلب وصولاً بعيداً.

**المرحلة 2 - تنفيذ القراءات المحلية**: تقرأ المعاملة جميع السجلات المخزنة محلياً من طبقة التخزين.

**المرحلة 3 - خدمة القراءات البعيدة**: إذا كانت هذه العقدة تمتلك سجلات تحتاجها العقد الأخرى لمعاملاتها، فإنها تستجيب لطلبات القراءة البعيدة.

**المرحلة 4 - جمع نتائج القراءة البعيدة**: تنتظر المعاملة الاستجابات لأي طلبات قراءة بعيدة أصدرتها.

**المرحلة 5 - تنفيذ منطق المعاملة وتطبيق الكتابات**: مع توفر جميع البيانات الضرورية، تنفذ المعاملة منطق التطبيق الخاص بها وتكتب النتائج إلى طبقة التخزين.

يسمح تصميم خط الأنابيب هذا بأن تكون معاملات متعددة في مراحل مختلفة في وقت واحد، مما يعظم استخدام المعالج ويخفي زمن استجابة الشبكة.

#### 5.3 التعامل مع المعاملات متعددة الأقسام

بالنسبة للمعاملات التي تصل إلى البيانات عبر أقسام متعددة، يستخدم كالفن بروتوكول تنسيق نشط/سلبي:

**المشارك النشط**: يتم تعيين عقدة واحدة (عادةً العقدة التي تم تقديم المعاملة فيها) كمشارك نشط. تنفذ هذه العقدة منطق المعاملة الكامل.

**المشاركون السلبيون**: تعمل العقد التي تمتلك أقساماً أخرى تصل إليها المعاملة كمشاركين سلبيين. يحصلون على أقفال، وينفذون القراءات، ويطبقون الكتابات كما يطلبه المشارك النشط.

يستمر البروتوكول على النحو التالي:

1. يحصل المشارك النشط على أقفال على جميع السجلات في جميع الأقسام المعنية (يمنح مدير الأقفال لكل قسم الأقفال بشكل مستقل بالترتيب العالمي).

2. يطلب المشارك النشط القراءات من جميع المشاركين السلبيين.

3. ينفذ المشاركون السلبيون القراءات ويعيدون النتائج.

4. ينفذ المشارك النشط منطق المعاملة ويحدد جميع عمليات الكتابة.

5. يرسل المشارك النشط أوامر الكتابة إلى المشاركين السلبيين.

6. يطبق جميع المشاركين الكتابات ويطلقون الأقفال.

بشكل حاسم، نظراً لأن التنفيذ حتمي والترتيب العالمي محدد مسبقاً، فإن هذا البروتوكول لا يتطلب بروتوكول التزام موزع مثل 2PC. يحدد جميع المشاركين بشكل مستقل نفس نتيجة الالتزام/الإلغاء بناءً على منطق المعاملة.

#### 5.4 المعاملات المعتمدة

التحدي الأساسي للتنفيذ الحتمي هو أن مجموعات القراءة والكتابة للمعاملة يجب أن تكون معروفة قبل بدء التنفيذ. ومع ذلك، فإن العديد من المعاملات في العالم الحقيقي هي **معاملات معتمدة**—يجب عليها قراءة البيانات لتحديد السجلات الإضافية للوصول إليها.

على سبيل المثال، ضع في اعتبارك معاملة تقرأ حساب المستخدم للعثور على عنوانه الحالي، ثم تحدث السجلات المرتبطة بهذا العنوان. لا يمكن تحديد السجلات المتعلقة بالعنوان حتى تكتمل القراءة الأولية.

يتعامل كالفن مع المعاملات المعتمدة من خلال **التنبؤ التفاؤلي بموقع القفل (OLLP)**:

1. **استعلام استطلاع**: قبل تقديم المعاملة الفعلية إلى طبقة التسلسل، ينفذ استعلام استطلاع غير منسوخ للتنبؤ بالسجلات التي ستصل إليها المعاملة.

2. **تقديم المعاملة**: بناءً على نتائج الاستطلاع، يتم تقديم المعاملة مع مجموعة قراءة/كتابة متوقعة.

3. **التحقق أثناء التنفيذ**: عندما تنفذ المعاملة الفعلية، تتحقق من صحة نمط الوصول المتوقع.

4. **إعادة التشغيل عند سوء التنبؤ**: إذا اختلف نمط الوصول الفعلي عن التنبؤ، فإن المعاملة تُلغى ويتم إعادة تقديمها مع نمط الوصول المصحح.

لهذا النهج آثار مهمة:

**تكلفة الاستطلاع العامة**: يضيف استعلام الاستطلاع الأولي زمن استجابة ويستهلك موارد النظام. ومع ذلك، لا يتم نسخ هذا الاستعلام، لذا فهو أرخص من تنفيذ المعاملة الكاملة.

**تكلفة الإلغاء وإعادة التشغيل**: إذا كانت التنبؤات خاطئة بشكل متكرر، فإن المعاملة ستُلغى وتعاد عدة مرات، مما يؤثر بشكل كبير على الأداء.

**دقة التنبؤ**: تعتمد فعالية OLLP بشكل حاسم على قابلية التنبؤ بأنماط الوصول. قد تؤدي التطبيقات ذات أنماط الوصول غير القابلة للتنبؤ بشكل كبير أداءً ضعيفاً.

في الممارسة العملية، تحتوي العديد من أحمال العمل على أنماط وصول قابلة للتنبؤ. على سبيل المثال، في تطبيق شبكة اجتماعية، يمكن للمعاملة التي تصل إلى ملف تعريف المستخدم أن تتنبأ بشكل موثوق أنها ستصل أيضاً إلى قائمة أصدقاء المستخدم. يُظهر تقييم كالفن أنه مع دقة تنبؤ معتدلة (أعلى من 80%)، تظل التكلفة العامة لـ OLLP مقبولة.

#### 5.5 تطبيق مدير الأقفال

يتم تطبيق مدير الأقفال في كالفن كخيط منفصل في كل عقدة، يدير الأقفال للسجلات المخزنة في تلك العقدة. يحتفظ مدير الأقفال بـ:

**جدول الأقفال**: جدول تجزئة يربط كل سجل بحامل (حاملي) القفل الحالي وطابور طلبات الانتظار.

**طابور المعاملات**: طابور مرتب من المعاملات بترتيب التسلسل العالمي، يحتوي على طلبات القفل الخاصة بها.

**سياسة المنح**: سياسة صارمة تمنح الأقفال فقط بالترتيب العالمي، حتى لو كان القفل متاحاً وطلبته معاملة لاحقة.

يوفر هذا التصميم عدة فوائد:

**توازي إدارة الأقفال**: يعمل مدير الأقفال لكل عقدة بشكل مستقل، مما يسمح بعمليات القفل المتوازية عبر العقد.

**ذاكرة محدودة**: حجم جدول الأقفال يتناسب مع عدد السجلات المقفلة بشكل نشط، وليس إجمالي حجم قاعدة البيانات.

**منع الجمود البسيط**: يلغي الترتيب العالمي الجمود بالبناء، ولا يتطلب آليات الكشف أو الحل المعقدة.

---

### Translation Notes

- **Key terms introduced:**
  - Execution pipeline: خط أنابيب التنفيذ
  - Active participant: مشارك نشط
  - Passive participant: مشارك سلبي
  - Dependent transaction: معاملة معتمدة
  - Reconnaissance query: استعلام استطلاع
  - Optimistic Lock Location Prediction (OLLP): التنبؤ التفاؤلي بموقع القفل
  - Misprediction: سوء التنبؤ
  - Lock table: جدول الأقفال
  - Grant policy: سياسة المنح
  - Circular wait: انتظار دائري

- **Equations:** Transaction ordering notation $T_i$, $T_j$, $j > i$
- **Citations:** None
- **Special handling:** Maintained technical precision for lock management and transaction coordination protocols

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Validation

The Arabic translation accurately preserves:
- Deterministic lock manager protocol
- Five-phase execution pipeline
- Active/passive coordination for multi-partition transactions
- OLLP mechanism for handling dependent transactions
- Lock manager implementation details

✅ Translation maintains technical accuracy for concurrency control mechanisms.
