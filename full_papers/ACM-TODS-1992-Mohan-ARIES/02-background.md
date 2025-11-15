# Section 2: Background and Terminology
## القسم 2: الخلفية والمصطلحات

**Section:** background
**Translation Quality:** 0.88
**Glossary Terms Used:** transaction, database, recovery, log, checkpoint, commit, abort, rollback, write-ahead logging, page, buffer, disk, memory, concurrency control, locking

---

### English Version

This section introduces fundamental concepts and terminology used throughout the paper.

## 2.1 Transactions and ACID Properties

A **transaction** is a sequence of operations that must execute atomically - either all operations complete successfully, or none do. Transactions must satisfy the ACID properties:

- **Atomicity**: A transaction's effects are atomic - either all changes are applied or none are.
- **Consistency**: A transaction transforms the database from one consistent state to another.
- **Isolation**: Concurrent transactions appear to execute in isolation from each other.
- **Durability**: Once a transaction commits, its effects persist despite subsequent failures.

The recovery system is primarily concerned with ensuring atomicity and durability.

## 2.2 Write-Ahead Logging (WAL)

Write-Ahead Logging is the fundamental protocol used by ARIES. The WAL protocol requires:

1. **Log records must be written to stable storage before the corresponding data pages are written**. This ensures that the system can undo or redo operations during recovery.

2. **All log records for a transaction must be written to stable storage before the transaction commits**. This ensures durability.

The log is a sequential file of log records stored on stable storage (typically disk). Each log record describes an update to the database or a transaction management action (such as commit or abort).

## 2.3 Log Sequence Numbers (LSNs)

Each log record is assigned a unique, monotonically increasing **Log Sequence Number (LSN)**. LSNs typically represent the log record's position in the log file (e.g., byte offset). The LSN serves multiple purposes:

- Uniquely identifies each log record
- Defines the temporal order of log records
- Enables efficient log scanning and searching
- Tracks the state of pages (via Page LSN)
- Tracks transaction progress (via Transaction LSN table)

## 2.4 Page Structure

Each data page in the database contains a **Page LSN**, which is the LSN of the log record that describes the most recent update to that page. The Page LSN is crucial for recovery:

- During redo, if the Page LSN ≥ the update's LSN, the update has already been applied and need not be redone
- During undo, the Page LSN helps determine which undos are needed

## 2.5 Transaction Table and Dirty Page Table

The system maintains two key tables in memory:

**Transaction Table**: Contains one entry for each active (uncommitted) transaction, including:
- Transaction ID
- Transaction state (active, preparing, committed, aborting)
- LastLSN: LSN of the most recent log record for this transaction
- UndoNxtLSN: LSN of next log record to undo (for rollback)

**Dirty Page Table (DPT)**: Contains one entry for each dirty page (modified but not yet written to disk), including:
- Page ID
- RecLSN: LSN of the first log record that made this page dirty since it was last written to disk

The RecLSN is crucial for determining the starting point for the redo pass during recovery.

## 2.6 Checkpoints

A **checkpoint** is a point in the log where the system records its current state to reduce recovery time. ARIES uses fuzzy checkpoints that do not require quiescing the system or flushing all dirty pages. A checkpoint records:

- Contents of the transaction table
- Contents of the dirty page table
- LSN of the checkpoint record itself

## 2.7 Force and Steal Policies

Buffer management policies significantly impact recovery design:

- **Force**: Requires all pages modified by a transaction to be written to disk before commit
- **No-Force**: Allows commit without writing modified pages to disk
- **Steal**: Allows uncommitted changes to be written to disk (buffer pages can be "stolen" for reuse)
- **No-Steal**: Prevents uncommitted changes from being written to disk

ARIES uses a **No-Force, Steal** policy, which provides maximum flexibility for buffer management but requires sophisticated recovery protocols. No-Force improves performance by avoiding forced writes at commit time. Steal improves buffer utilization by allowing any page to be written to disk when needed.

## 2.8 Redo and Undo

During recovery, two types of operations may be needed:

- **Redo**: Reapply a logged update to the database. Redo is idempotent - redoing an operation multiple times has the same effect as doing it once. Redo uses physical or physiological logging.

- **Undo**: Reverse a logged update to the database. Undo operations are logged as Compensation Log Records (CLRs) to ensure recovery is idempotent. Undo typically uses logical or physiological logging.

## 2.9 Repeating History

ARIES follows the principle of "repeating history" during recovery. The redo pass reapplies all logged updates, reconstructing the database state as it existed at the time of failure, including uncommitted changes. After repeating history, the undo pass removes uncommitted changes. This approach simplifies recovery and makes it more robust.

---

### النسخة العربية

يقدم هذا القسم المفاهيم الأساسية والمصطلحات المستخدمة في جميع أنحاء البحث.

## 2.1 المعاملات وخصائص ACID

**المعاملة** هي تسلسل من العمليات التي يجب أن تنفذ بشكل ذري - إما أن تكتمل جميع العمليات بنجاح، أو لا تكتمل أي منها. يجب أن تستوفي المعاملات خصائص ACID:

- **الذرية (Atomicity)**: تأثيرات المعاملة ذرية - إما يتم تطبيق جميع التغييرات أو لا يتم تطبيق أي منها.
- **الاتساق (Consistency)**: تحول المعاملة قاعدة البيانات من حالة متسقة إلى أخرى.
- **العزل (Isolation)**: تظهر المعاملات المتزامنة وكأنها تنفذ بمعزل عن بعضها البعض.
- **الديمومة (Durability)**: بمجرد تثبيت المعاملة، تستمر تأثيراتها على الرغم من الأعطال اللاحقة.

يهتم نظام الاسترداد في المقام الأول بضمان الذرية والديمومة.

## 2.2 التسجيل المسبق للكتابة (WAL)

التسجيل المسبق للكتابة هو البروتوكول الأساسي الذي تستخدمه ARIES. يتطلب بروتوكول WAL:

1. **يجب كتابة سجلات السجل إلى التخزين المستقر قبل كتابة صفحات البيانات المقابلة**. هذا يضمن أن النظام يمكنه التراجع عن العمليات أو إعادتها أثناء الاسترداد.

2. **يجب كتابة جميع سجلات السجل لمعاملة إلى التخزين المستقر قبل تثبيت المعاملة**. هذا يضمن الديمومة.

السجل هو ملف تسلسلي من سجلات السجل المخزنة على تخزين مستقر (عادة القرص). يصف كل سجل تحديثاً لقاعدة البيانات أو إجراء إدارة معاملة (مثل التثبيت أو الإلغاء).

## 2.3 أرقام تسلسل السجل (LSNs)

يتم تعيين **رقم تسلسل سجل (LSN)** فريد ومتزايد بشكل رتيب لكل سجل. تمثل LSNs عادةً موضع سجل السجل في ملف السجل (على سبيل المثال، إزاحة البايت). يخدم LSN أغراضاً متعددة:

- تحديد كل سجل بشكل فريد
- تحديد الترتيب الزمني لسجلات السجل
- تمكين المسح والبحث الفعال في السجل
- تتبع حالة الصفحات (عبر Page LSN)
- تتبع تقدم المعاملة (عبر جدول LSN للمعاملة)

## 2.4 بنية الصفحة

تحتوي كل صفحة بيانات في قاعدة البيانات على **Page LSN**، وهو LSN لسجل السجل الذي يصف أحدث تحديث لتلك الصفحة. يعد Page LSN أمراً بالغ الأهمية للاسترداد:

- أثناء الإعادة، إذا كان Page LSN ≥ LSN التحديث، فقد تم تطبيق التحديث بالفعل ولا يحتاج إلى إعادة
- أثناء التراجع، يساعد Page LSN في تحديد التراجعات المطلوبة

## 2.5 جدول المعاملات وجدول الصفحات المعدلة

يحتفظ النظام بجدولين رئيسيين في الذاكرة:

**جدول المعاملات**: يحتوي على إدخال واحد لكل معاملة نشطة (غير مثبتة)، بما في ذلك:
- معرّف المعاملة
- حالة المعاملة (نشطة، قيد الإعداد، مثبتة، قيد الإلغاء)
- LastLSN: LSN لأحدث سجل لهذه المعاملة
- UndoNxtLSN: LSN لسجل السجل التالي للتراجع عنه (للتراجع)

**جدول الصفحات المعدلة (DPT)**: يحتوي على إدخال واحد لكل صفحة معدلة (تم تعديلها ولكن لم تُكتب بعد على القرص)، بما في ذلك:
- معرّف الصفحة
- RecLSN: LSN لأول سجل جعل هذه الصفحة معدلة منذ آخر كتابة لها على القرص

RecLSN ضروري لتحديد نقطة البداية لمرحلة الإعادة أثناء الاسترداد.

## 2.6 نقاط التحقق

**نقطة التحقق** هي نقطة في السجل حيث يسجل النظام حالته الحالية لتقليل وقت الاسترداد. تستخدم ARIES نقاط تحقق ضبابية لا تتطلب إيقاف النظام أو مسح جميع الصفحات المعدلة. تسجل نقطة التحقق:

- محتويات جدول المعاملات
- محتويات جدول الصفحات المعدلة
- LSN لسجل نقطة التحقق نفسه

## 2.7 سياسات الإجبار والسرقة

تؤثر سياسات إدارة المخزن المؤقت بشكل كبير على تصميم الاسترداد:

- **الإجبار (Force)**: يتطلب كتابة جميع الصفحات المعدلة بواسطة معاملة على القرص قبل التثبيت
- **عدم الإجبار (No-Force)**: يسمح بالتثبيت دون كتابة الصفحات المعدلة على القرص
- **السرقة (Steal)**: يسمح بكتابة التغييرات غير المثبتة على القرص (يمكن "سرقة" صفحات المخزن المؤقت لإعادة الاستخدام)
- **عدم السرقة (No-Steal)**: يمنع كتابة التغييرات غير المثبتة على القرص

تستخدم ARIES سياسة **عدم الإجبار والسرقة**، والتي توفر أقصى قدر من المرونة لإدارة المخزن المؤقت ولكنها تتطلب بروتوكولات استرداد متطورة. يحسن عدم الإجبار الأداء عن طريق تجنب عمليات الكتابة الإجبارية في وقت التثبيت. تحسن السرقة استخدام المخزن المؤقت عن طريق السماح بكتابة أي صفحة على القرص عند الحاجة.

## 2.8 الإعادة والتراجع

أثناء الاسترداد، قد تكون هناك حاجة إلى نوعين من العمليات:

- **الإعادة (Redo)**: إعادة تطبيق تحديث مسجل على قاعدة البيانات. الإعادة متماثلة القوة - إعادة عملية عدة مرات لها نفس تأثير القيام بها مرة واحدة. تستخدم الإعادة التسجيل الفيزيائي أو الفسيولوجي.

- **التراجع (Undo)**: عكس تحديث مسجل على قاعدة البيانات. يتم تسجيل عمليات التراجع كسجلات تعويض (CLRs) لضمان أن الاسترداد متماثل القوة. يستخدم التراجع عادةً التسجيل المنطقي أو الفسيولوجي.

## 2.9 تكرار التاريخ

تتبع ARIES مبدأ "تكرار التاريخ" أثناء الاسترداد. تعيد مرحلة الإعادة تطبيق جميع التحديثات المسجلة، وإعادة بناء حالة قاعدة البيانات كما كانت موجودة وقت الفشل، بما في ذلك التغييرات غير المثبتة. بعد تكرار التاريخ، تزيل مرحلة التراجع التغييرات غير المثبتة. يبسط هذا النهج الاسترداد ويجعله أكثر قوة.

---

### Translation Notes

- **Key concepts introduced:** ACID properties, WAL protocol, LSNs, Page LSN, RecLSN, LastLSN, Transaction Table, Dirty Page Table, Checkpoints, Force/No-Force, Steal/No-Steal, Redo/Undo, Repeating History
- **Technical terms:** Stable storage, buffer management, idempotent, physical/physiological/logical logging
- **Equations/Formulas:** LSN comparison operations (≥)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
