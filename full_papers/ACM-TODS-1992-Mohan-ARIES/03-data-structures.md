# Section 3: Data Structures
## القسم 3: بنى البيانات

**Section:** Data Structures
**Translation Quality:** 0.86
**Glossary Terms Used:** log record, LSN, page, buffer, transaction table, dirty page table, checkpoint, undo, redo, CLR

---

### English Version

#### 3.1 Log Records

The log is a sequential file containing records that describe all changes to the database. Each log record has a unique Log Sequence Number (LSN) that increases monotonically. Log records contain the following key fields:

**Common Fields in All Log Records:**
- **LSN:** Unique identifier for this log record (monotonically increasing)
- **TransID:** Transaction identifier for the transaction that generated this record
- **Type:** Record type (update, commit, abort, CLR, checkpoint, etc.)
- **PrevLSN:** LSN of the previous log record for this transaction (forms a backward chain)

**Update Log Records:**
For update operations, additional fields include:
- **PageID:** Identifier of the page being modified
- **Length:** Length of the update information
- **Offset:** Location within the page where the update occurs
- **Before Image:** Original value (for undo)
- **After Image:** New value (for redo)

Alternatively, ARIES supports operation logging where instead of storing before/after images, the log contains:
- **Redo Operation:** Operation to reapply the change
- **Undo Operation:** Operation to reverse the change
- **Operation Parameters:** Parameters needed for both redo and undo

**Compensation Log Records (CLRs):**
CLRs are written when undoing an update during rollback or recovery. They contain:
- All standard log record fields
- **UndoNxtLSN:** Points to the next log record to be undone (skipping over the record being compensated)
- **Redo Information:** Describes the undo action (CLRs are redo-only)

CLRs ensure that undo operations are idempotent—if a failure occurs during rollback, the system can resume without re-undoing already compensated actions.

#### 3.2 Page Structure

Each database page contains:
- **PageLSN:** LSN of the most recent update applied to this page
- **Page Data:** The actual data records or index entries
- **Free Space Information:** Tracks available space on the page

The PageLSN is critical for recovery. During redo, the system compares the PageLSN with the LSN of a logged update. If PageLSN ≥ Update LSN, the update has already been applied and can be skipped (idempotent redo).

#### 3.3 Transaction Table

The transaction table maintains information about active transactions. Each entry contains:
- **TransID:** Transaction identifier
- **State:** Current transaction state (running, prepared, committed, aborting)
- **LastLSN:** LSN of the most recent log record for this transaction
- **UndoNxtLSN:** For transactions being rolled back, the next LSN to undo

During normal processing, the transaction table tracks all active transactions. During recovery, the Analysis phase reconstructs the transaction table to determine which transactions were active at the time of the crash.

#### 3.4 Dirty Page Table

The dirty page table tracks pages in the buffer pool that have been modified but not yet written to disk. Each entry contains:
- **PageID:** Identifier of the dirty page
- **RecLSN:** LSN of the first log record that made this page dirty since it was last written to disk

The RecLSN is crucial for determining where to start redo during recovery. The system must redo all updates starting from the minimum RecLSN in the dirty page table, ensuring that all logged changes are reflected on disk.

#### 3.5 Checkpoint Records

ARIES uses fuzzy checkpoints that do not quiesce system activity. A checkpoint consists of:
- **begin_checkpoint Record:** Marks the start of checkpoint processing
- **end_checkpoint Record:** Contains:
  - Snapshot of the transaction table (all active transactions)
  - Snapshot of the dirty page table (all dirty pages and their RecLSNs)
  - LSN of the begin_checkpoint record

The master record on stable storage points to the begin_checkpoint LSN of the most recent complete checkpoint.

#### 3.6 LSN Semantics and Usage

LSNs serve multiple purposes throughout ARIES:

**Ordering:** LSNs establish a total order on all logged operations. If LSN1 < LSN2, the operation logged by LSN1 occurred before the operation logged by LSN2.

**Page State Tracking:** The PageLSN on each page indicates which updates have been applied to that page. During recovery:
- If PageLSN ≥ LogRecord.LSN, the update is already on the page (skip redo)
- If PageLSN < LogRecord.LSN, the update needs to be redone

**Transaction Progress:** The LastLSN in each transaction table entry points to the most recent operation by that transaction, enabling backward traversal of the log during undo.

**Recovery Bounds:** The RecLSN in the dirty page table determines where redo must begin. The minimum RecLSN across all dirty pages is the earliest point where redo processing must start.

**Idempotency:** LSN comparisons ensure that redo and undo operations are idempotent—they can be safely repeated without changing the result. This property is essential for handling failures during recovery.

---

### النسخة العربية

#### 3.1 سجلات السجل

السجل هو ملف تسلسلي يحتوي على سجلات تصف جميع التغييرات على قاعدة البيانات. يحتوي كل سجل سجل على رقم تسلسل سجل فريد (LSN) يتزايد بشكل رتيب. تحتوي سجلات السجل على الحقول الرئيسية التالية:

**الحقول المشتركة في جميع سجلات السجل:**
- **LSN:** معرّف فريد لهذا السجل (متزايد بشكل رتيب)
- **TransID:** معرّف المعاملة للمعاملة التي أنشأت هذا السجل
- **Type:** نوع السجل (تحديث، إنهاء، إحباط، CLR، نقطة تفتيش، إلخ)
- **PrevLSN:** LSN لسجل السجل السابق لهذه المعاملة (يشكل سلسلة عكسية)

**سجلات سجل التحديث:**
لعمليات التحديث، تشمل الحقول الإضافية:
- **PageID:** معرّف الصفحة التي يتم تعديلها
- **Length:** طول معلومات التحديث
- **Offset:** الموقع داخل الصفحة حيث يحدث التحديث
- **Before Image:** القيمة الأصلية (للتراجع)
- **After Image:** القيمة الجديدة (للإعادة)

بدلاً من ذلك، تدعم ARIES تسجيل العمليات حيث بدلاً من تخزين صور قبل/بعد، يحتوي السجل على:
- **Redo Operation:** عملية لإعادة تطبيق التغيير
- **Undo Operation:** عملية لعكس التغيير
- **Operation Parameters:** معاملات مطلوبة لكل من الإعادة والتراجع

**سجلات التعويض (CLRs):**
تُكتب CLRs عند التراجع عن تحديث أثناء التراجع أو الاسترداد. تحتوي على:
- جميع حقول سجل السجل القياسية
- **UndoNxtLSN:** يشير إلى سجل السجل التالي الذي سيتم التراجع عنه (تخطي السجل الذي يتم تعويضه)
- **Redo Information:** يصف إجراء التراجع (CLRs للإعادة فقط)

تضمن CLRs أن عمليات التراجع متساوية القوة—إذا حدث فشل أثناء التراجع، يمكن للنظام الاستئناف دون إعادة التراجع عن الإجراءات التي تم تعويضها بالفعل.

#### 3.2 بنية الصفحة

تحتوي كل صفحة قاعدة بيانات على:
- **PageLSN:** LSN لأحدث تحديث مُطبق على هذه الصفحة
- **Page Data:** السجلات الفعلية أو مدخلات الفهرس
- **Free Space Information:** تتبع المساحة المتاحة على الصفحة

PageLSN حرج للاسترداد. أثناء الإعادة، يقارن النظام PageLSN مع LSN للتحديث المسجل. إذا كان PageLSN ≥ Update LSN، فقد تم تطبيق التحديث بالفعل ويمكن تخطيه (إعادة متساوية القوة).

#### 3.3 جدول المعاملات

يحتفظ جدول المعاملات بمعلومات حول المعاملات النشطة. يحتوي كل إدخال على:
- **TransID:** معرّف المعاملة
- **State:** حالة المعاملة الحالية (قيد التشغيل، مُعدة، مُنهاة، قيد الإحباط)
- **LastLSN:** LSN لأحدث سجل سجل لهذه المعاملة
- **UndoNxtLSN:** للمعاملات التي يتم التراجع عنها، LSN التالي للتراجع

أثناء المعالجة العادية، يتتبع جدول المعاملات جميع المعاملات النشطة. أثناء الاسترداد، تعيد مرحلة التحليل بناء جدول المعاملات لتحديد المعاملات التي كانت نشطة وقت العطل.

#### 3.4 جدول الصفحات المتسخة

يتتبع جدول الصفحات المتسخة الصفحات في مجمع المخازن المؤقتة التي تم تعديلها ولكن لم تُكتب بعد إلى القرص. يحتوي كل إدخال على:
- **PageID:** معرّف الصفحة المتسخة
- **RecLSN:** LSN لأول سجل سجل جعل هذه الصفحة متسخة منذ آخر كتابة لها إلى القرص

RecLSN حاسم لتحديد أين تبدأ الإعادة أثناء الاسترداد. يجب على النظام إعادة جميع التحديثات بدءاً من الحد الأدنى RecLSN في جدول الصفحات المتسخة، مما يضمن انعكاس جميع التغييرات المسجلة على القرص.

#### 3.5 سجلات نقطة التفتيش

تستخدم ARIES نقاط تفتيش ضبابية لا تُخمد نشاط النظام. تتكون نقطة التفتيش من:
- **سجل begin_checkpoint:** يضع علامة على بداية معالجة نقطة التفتيش
- **سجل end_checkpoint:** يحتوي على:
  - لقطة لجدول المعاملات (جميع المعاملات النشطة)
  - لقطة لجدول الصفحات المتسخة (جميع الصفحات المتسخة و RecLSNs الخاصة بها)
  - LSN لسجل begin_checkpoint

يشير السجل الرئيسي على التخزين المستقر إلى LSN لـ begin_checkpoint لأحدث نقطة تفتيش مكتملة.

#### 3.6 دلالات LSN واستخدامها

تخدم LSNs أغراضاً متعددة عبر ARIES:

**الترتيب:** تنشئ LSNs ترتيباً كلياً على جميع العمليات المسجلة. إذا كان LSN1 < LSN2، فإن العملية المسجلة بواسطة LSN1 حدثت قبل العملية المسجلة بواسطة LSN2.

**تتبع حالة الصفحة:** يشير PageLSN على كل صفحة إلى التحديثات التي تم تطبيقها على تلك الصفحة. أثناء الاسترداد:
- إذا كان PageLSN ≥ LogRecord.LSN، فإن التحديث موجود بالفعل على الصفحة (تخطي الإعادة)
- إذا كان PageLSN < LogRecord.LSN، فإن التحديث يحتاج إلى الإعادة

**تقدم المعاملة:** يشير LastLSN في كل إدخال جدول معاملات إلى أحدث عملية بواسطة تلك المعاملة، مما يمكّن المسار العكسي للسجل أثناء التراجع.

**حدود الاسترداد:** يحدد RecLSN في جدول الصفحات المتسخة أين يجب أن تبدأ الإعادة. الحد الأدنى RecLSN عبر جميع الصفحات المتسخة هو أقرب نقطة يجب أن تبدأ فيها معالجة الإعادة.

**التساوي في القوة:** تضمن مقارنات LSN أن عمليات الإعادة والتراجع متساوية القوة—يمكن تكرارها بأمان دون تغيير النتيجة. هذه الخاصية ضرورية للتعامل مع الفشل أثناء الاسترداد.

---

### Translation Notes

- **Data Structure Names:**
  - Transaction Table → جدول المعاملات
  - Dirty Page Table → جدول الصفحات المتسخة
  - Before/After Image → صورة قبل/بعد
  - Fuzzy checkpoint → نقطة تفتيش ضبابية
  - Master record → السجل الرئيسي

- **Technical Concepts:**
  - Idempotency → التساوي في القوة (operations that can be repeated safely)
  - Backward chain → سلسلة عكسية (linking log records via PrevLSN)
  - Redo-only → للإعادة فقط (CLRs that are never undone)

- **Key Fields Preserved:** All critical log record fields (LSN, TransID, PrevLSN, UndoNxtLSN, RecLSN, PageLSN) explained precisely

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.86
