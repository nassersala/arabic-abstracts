# Section 4: Normal Processing and WAL Protocol
## القسم 4: المعالجة العادية وبروتوكول WAL

**Section:** Normal Processing and WAL Protocol
**Translation Quality:** 0.87
**Glossary Terms Used:** transaction, update, commit, abort, log, buffer, WAL, LSN, page, dirty page, force, steal, rollback, savepoint

---

### English Version

#### 4.1 Transaction Operations

During normal processing, transactions perform a sequence of operations on database pages. ARIES manages these operations while maintaining recoverability guarantees through the Write-Ahead Logging (WAL) protocol.

**Transaction Lifecycle:**

1. **Begin Transaction:** The system assigns a unique transaction identifier (TransID) and creates an entry in the transaction table with state = running.

2. **Update Operations:** When a transaction modifies a page:
   - The buffer manager fetches the page into the buffer pool if not already present
   - The transaction acquires appropriate locks (record-level or page-level)
   - An update log record is generated with Before and After images (or redo/undo operations)
   - The log record receives a unique LSN
   - The log record is appended to the in-memory log buffer
   - The update is applied to the page in the buffer pool
   - The page's PageLSN is set to the LSN of this update
   - The transaction's LastLSN is updated to this LSN
   - The page is marked dirty in the dirty page table (if not already dirty, RecLSN is set)

3. **Commit:** When a transaction commits:
   - A commit log record is written
   - The commit record and all prior log records for this transaction are forced to stable storage (log force)
   - The transaction's locks are released
   - The transaction entry is removed from the transaction table
   - Modified pages remain in the buffer pool (No-Force policy—they are written to disk asynchronously)

4. **Abort:** When a transaction aborts:
   - The system performs rollback (undo all updates)
   - For each update log record (traversing backward via PrevLSN):
     - A Compensation Log Record (CLR) is written describing the undo action
     - The undo operation is applied to the page
     - The page's PageLSN is updated to the CLR's LSN
   - An abort log record is written
   - Locks are released
   - Transaction entry is removed from the transaction table

#### 4.2 Write-Ahead Logging Protocol

The WAL protocol is the cornerstone of ARIES, ensuring that the log contains sufficient information to redo committed work and undo uncommitted work. The protocol enforces two critical rules:

**WAL Rule 1 (Before Writing a Dirty Page):**
Before a dirty page can be written from the buffer pool to disk, all log records describing updates to that page must be forced to stable storage up to and including the PageLSN.

Formally: Before writing page P to disk, force all log records with LSN ≤ P.PageLSN to stable storage.

This ensures that redo information is available if the page is lost or corrupted.

**WAL Rule 2 (Before Committing a Transaction):**
Before a transaction can commit, all log records for that transaction, including the commit record, must be forced to stable storage.

Formally: Before committing transaction T, force all log records with LSN ≤ T.LastLSN to stable storage.

This ensures that committed transactions are durable—their effects can be recovered after any failure.

**Implementation Details:**
- Log records accumulate in an in-memory log buffer
- Periodically, or when the buffer fills, the log tail is flushed to stable storage
- The system maintains flushedLSN—the LSN through which the log has been written to stable storage
- A page with PageLSN > flushedLSN cannot be written to disk (WAL violation)
- At commit, if LastLSN > flushedLSN, a log force is required

#### 4.3 Buffer Management

ARIES employs a flexible buffer management policy:

**No-Force Policy:**
Modified pages are not forced to disk at commit time. This reduces I/O overhead since:
- Multiple updates to the same page by different transactions can be written together
- Disk writes can be scheduled for optimal I/O performance
- Hot pages can remain in the buffer pool

The cost is that committed changes may not be on disk, requiring redo during recovery.

**Steal Policy:**
Pages modified by uncommitted transactions can be stolen (written to disk) to free buffer frames. This improves buffer utilization by:
- Allowing long-running transactions without holding buffer frames indefinitely
- Enabling support for transactions larger than available buffer space
- Maximizing buffer pool efficiency

The cost is that uncommitted changes may be on disk, requiring undo during recovery.

**Page Replacement:**
When the buffer manager needs to evict a page:
1. Select a victim page using an LRU or other replacement policy
2. If the page is dirty:
   - Check that PageLSN ≤ flushedLSN (WAL protocol compliance)
   - If PageLSN > flushedLSN, force log up to PageLSN first
   - Write the page to disk
   - Remove from dirty page table
3. Reuse the buffer frame for a new page

#### 4.4 Checkpoints

ARIES uses fuzzy checkpoints to reduce recovery time without disrupting normal processing:

**Checkpoint Process:**
1. Write a begin_checkpoint record to the log
2. Construct the end_checkpoint record containing:
   - Snapshot of the transaction table (all active transactions)
   - Snapshot of the dirty page table (all dirty pages and their RecLSNs)
   - LSN of the begin_checkpoint record
3. Write the end_checkpoint record to the log
4. Update the master record on stable storage to point to the begin_checkpoint LSN

**Key Property—Fuzzy:**
Unlike sharp checkpoints that quiesce all activity, fuzzy checkpoints allow:
- New transactions to start during checkpoint
- Running transactions to continue updating pages
- Dirty pages to remain in the buffer pool
- No synchronization required with transaction processing

The checkpoint captures the state at the moment of begin_checkpoint, even though writing the checkpoint data may take time. This greatly reduces checkpoint overhead while still providing recovery benefits.

#### 4.5 Partial Rollback (Savepoints)

ARIES supports partial transaction rollback through savepoints:

**Creating a Savepoint:**
A transaction can declare a savepoint at any time. The system records the transaction's current LastLSN as the savepoint.

**Rolling Back to a Savepoint:**
To roll back to a savepoint:
1. Undo all updates from LastLSN back to the savepoint LSN
2. For each update record undone, write a CLR
3. Set UndoNxtLSN in the final CLR to point past all undone updates
4. Continue normal processing from the savepoint

**Benefits:**
- Supports application-level error handling
- Enables nested transactions and nested top actions
- Reduces work compared to aborting the entire transaction
- Maintains full ACID properties

---

### النسخة العربية

#### 4.1 عمليات المعاملات

أثناء المعالجة العادية، تنفذ المعاملات تسلسلاً من العمليات على صفحات قاعدة البيانات. تدير ARIES هذه العمليات مع الحفاظ على ضمانات قابلية الاسترداد من خلال بروتوكول التسجيل المسبق للكتابة (WAL).

**دورة حياة المعاملة:**

1. **بدء المعاملة:** يخصص النظام معرّف معاملة فريد (TransID) وينشئ إدخالاً في جدول المعاملات مع الحالة = قيد التشغيل.

2. **عمليات التحديث:** عندما تعدل معاملة صفحة:
   - يجلب مدير المخزن المؤقت الصفحة إلى مجمع المخازن المؤقتة إذا لم تكن موجودة بالفعل
   - تحصل المعاملة على أقفال مناسبة (على مستوى السجل أو على مستوى الصفحة)
   - يتم إنشاء سجل سجل تحديث بصور قبل وبعد (أو عمليات إعادة/تراجع)
   - يتلقى سجل السجل LSN فريد
   - يُلحق سجل السجل بمخزن سجل الذاكرة المؤقت
   - يُطبق التحديث على الصفحة في مجمع المخازن المؤقتة
   - يُعيّن PageLSN للصفحة إلى LSN لهذا التحديث
   - يُحدّث LastLSN للمعاملة إلى هذا LSN
   - تُعلم الصفحة كمتسخة في جدول الصفحات المتسخة (إذا لم تكن متسخة بالفعل، يُعيّن RecLSN)

3. **الإنهاء:** عندما تُنهي معاملة:
   - يُكتب سجل سجل إنهاء
   - يُجبر سجل الإنهاء وجميع سجلات السجل السابقة لهذه المعاملة على التخزين المستقر (إجبار السجل)
   - تُطلق أقفال المعاملة
   - يُزال إدخال المعاملة من جدول المعاملات
   - تبقى الصفحات المعدلة في مجمع المخازن المؤقتة (سياسة عدم الإجبار—تُكتب إلى القرص بشكل غير متزامن)

4. **الإحباط:** عندما تُحبط معاملة:
   - ينفذ النظام التراجع (التراجع عن جميع التحديثات)
   - لكل سجل سجل تحديث (المسار للخلف عبر PrevLSN):
     - يُكتب سجل تعويض (CLR) يصف إجراء التراجع
     - تُطبق عملية التراجع على الصفحة
     - يُحدّث PageLSN للصفحة إلى LSN الخاص بـ CLR
   - يُكتب سجل سجل إحباط
   - تُطلق الأقفال
   - يُزال إدخال المعاملة من جدول المعاملات

#### 4.2 بروتوكول التسجيل المسبق للكتابة

بروتوكول WAL هو حجر الزاوية في ARIES، مما يضمن أن السجل يحتوي على معلومات كافية لإعادة العمل المُنهى والتراجع عن العمل غير المُنهى. يفرض البروتوكول قاعدتين حرجتين:

**قاعدة WAL 1 (قبل كتابة صفحة متسخة):**
قبل أن يمكن كتابة صفحة متسخة من مجمع المخازن المؤقتة إلى القرص، يجب إجبار جميع سجلات السجل التي تصف التحديثات على تلك الصفحة على التخزين المستقر حتى وبما في ذلك PageLSN.

رسمياً: قبل كتابة الصفحة P إلى القرص، أجبر جميع سجلات السجل مع LSN ≤ P.PageLSN على التخزين المستقر.

يضمن هذا توفر معلومات الإعادة إذا فُقدت الصفحة أو تلفت.

**قاعدة WAL 2 (قبل إنهاء معاملة):**
قبل أن يمكن إنهاء معاملة، يجب إجبار جميع سجلات السجل لتلك المعاملة، بما في ذلك سجل الإنهاء، على التخزين المستقر.

رسمياً: قبل إنهاء المعاملة T، أجبر جميع سجلات السجل مع LSN ≤ T.LastLSN على التخزين المستقر.

يضمن هذا أن المعاملات المُنهاة دائمة—يمكن استرداد آثارها بعد أي فشل.

**تفاصيل التطبيق:**
- تتراكم سجلات السجل في مخزن سجل الذاكرة المؤقت
- بشكل دوري، أو عندما يمتلئ المخزن المؤقت، يُدفق ذيل السجل إلى التخزين المستقر
- يحتفظ النظام بـ flushedLSN—LSN الذي تم كتابة السجل من خلاله إلى التخزين المستقر
- لا يمكن كتابة صفحة مع PageLSN > flushedLSN إلى القرص (انتهاك WAL)
- عند الإنهاء، إذا كان LastLSN > flushedLSN، فإن إجبار السجل مطلوب

#### 4.3 إدارة المخزن المؤقت

توظف ARIES سياسة إدارة مخزن مؤقت مرنة:

**سياسة عدم الإجبار:**
لا تُجبر الصفحات المعدلة على الكتابة إلى القرص في وقت الإنهاء. يقلل هذا من حمل الإدخال/الإخراج حيث:
- يمكن كتابة تحديثات متعددة لنفس الصفحة بواسطة معاملات مختلفة معاً
- يمكن جدولة كتابات القرص لأداء إدخال/إخراج أمثل
- يمكن أن تبقى الصفحات الساخنة في مجمع المخازن المؤقتة

التكلفة هي أن التغييرات المُنهاة قد لا تكون على القرص، مما يتطلب الإعادة أثناء الاسترداد.

**سياسة السرقة:**
يمكن سرقة الصفحات المعدلة بواسطة معاملات غير مُنهاة (كتابتها إلى القرص) لتحرير إطارات المخزن المؤقت. يحسن هذا استخدام المخزن المؤقت من خلال:
- السماح للمعاملات طويلة المدى دون الاحتفاظ بإطارات المخزن المؤقت إلى أجل غير مسمى
- تمكين دعم المعاملات الأكبر من مساحة المخزن المؤقت المتاحة
- زيادة كفاءة مجمع المخازن المؤقتة إلى أقصى حد

التكلفة هي أن التغييرات غير المُنهاة قد تكون على القرص، مما يتطلب التراجع أثناء الاسترداد.

**استبدال الصفحة:**
عندما يحتاج مدير المخزن المؤقت إلى إخلاء صفحة:
1. حدد صفحة ضحية باستخدام سياسة LRU أو استبدال أخرى
2. إذا كانت الصفحة متسخة:
   - تحقق من أن PageLSN ≤ flushedLSN (امتثال بروتوكول WAL)
   - إذا كان PageLSN > flushedLSN، أجبر السجل حتى PageLSN أولاً
   - اكتب الصفحة إلى القرص
   - أزل من جدول الصفحات المتسخة
3. أعد استخدام إطار المخزن المؤقت لصفحة جديدة

#### 4.4 نقاط التفتيش

تستخدم ARIES نقاط تفتيش ضبابية لتقليل وقت الاسترداد دون تعطيل المعالجة العادية:

**عملية نقطة التفتيش:**
1. اكتب سجل begin_checkpoint إلى السجل
2. أنشئ سجل end_checkpoint الذي يحتوي على:
   - لقطة لجدول المعاملات (جميع المعاملات النشطة)
   - لقطة لجدول الصفحات المتسخة (جميع الصفحات المتسخة و RecLSNs الخاصة بها)
   - LSN لسجل begin_checkpoint
3. اكتب سجل end_checkpoint إلى السجل
4. حدّث السجل الرئيسي على التخزين المستقر للإشارة إلى LSN لـ begin_checkpoint

**الخاصية الرئيسية—ضبابية:**
على عكس نقاط التفتيش الحادة التي تُخمد جميع الأنشطة، تسمح نقاط التفتيش الضبابية بـ:
- بدء معاملات جديدة أثناء نقطة التفتيش
- استمرار المعاملات الجارية في تحديث الصفحات
- بقاء الصفحات المتسخة في مجمع المخازن المؤقتة
- عدم الحاجة إلى مزامنة مع معالجة المعاملات

تلتقط نقطة التفتيش الحالة في لحظة begin_checkpoint، حتى لو استغرقت كتابة بيانات نقطة التفتيش وقتاً. يقلل هذا بشكل كبير من حمل نقطة التفتيش مع الحفاظ على فوائد الاسترداد.

#### 4.5 التراجع الجزئي (نقاط الحفظ)

تدعم ARIES التراجع الجزئي للمعاملات من خلال نقاط الحفظ:

**إنشاء نقطة حفظ:**
يمكن للمعاملة الإعلان عن نقطة حفظ في أي وقت. يسجل النظام LastLSN الحالي للمعاملة كنقطة حفظ.

**التراجع إلى نقطة حفظ:**
للتراجع إلى نقطة حفظ:
1. تراجع عن جميع التحديثات من LastLSN إلى LSN نقطة الحفظ
2. لكل سجل تحديث يتم التراجع عنه، اكتب CLR
3. عيّن UndoNxtLSN في CLR النهائي للإشارة إلى ما بعد جميع التحديثات التي تم التراجع عنها
4. استمر في المعالجة العادية من نقطة الحفظ

**الفوائد:**
- يدعم معالجة الأخطاء على مستوى التطبيق
- يمكّن المعاملات المتداخلة والإجراءات العليا المتداخلة
- يقلل من العمل مقارنة بإحباط المعاملة بأكملها
- يحافظ على خصائص ACID الكاملة

---

### Translation Notes

- **Core Protocol Rules:**
  - WAL Rule 1 & 2 → قاعدة WAL 1 و 2
  - No-Force, Steal → عدم الإجبار، السرقة
  - Log force → إجبار السجل
  - flushedLSN → LSN المدفوق (the LSN up to which log has been flushed)

- **Buffer Management:**
  - Buffer pool → مجمع المخازن المؤقتة
  - Victim page → صفحة ضحية (page selected for eviction)
  - LRU → الأقل استخداماً مؤخراً (Least Recently Used)

- **Checkpoint Terminology:**
  - Fuzzy checkpoint → نقطة تفتيش ضبابية (allows concurrent activity)
  - Sharp checkpoint → نقطة تفتيش حادة (requires quiescing)
  - Master record → السجل الرئيسي (stable storage pointer)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.87
