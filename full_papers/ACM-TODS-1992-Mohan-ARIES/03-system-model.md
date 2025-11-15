# Section 3: System Model and Assumptions
## القسم 3: نموذج النظام والافتراضات

**Section:** system-model
**Translation Quality:** 0.87
**Glossary Terms Used:** database, transaction, page, buffer, disk, memory, concurrency control, locking, log, stable storage

---

### English Version

This section describes the system model and assumptions underlying ARIES.

## 3.1 Database and Storage Organization

The database consists of a collection of **pages** stored on non-volatile storage (disk). Each page has a unique identifier (PageID) and a fixed size (typically 4KB-16KB). Pages contain data records, index entries, or other database structures.

The system maintains a **buffer pool** in main memory to cache frequently accessed pages. The buffer manager controls which pages reside in memory and when dirty pages are written to disk (flushed).

All updates to pages go through the buffer pool - pages are read into the buffer, modified in memory, and eventually written back to disk. The buffer manager uses a page replacement policy (such as LRU) to decide which pages to evict when the buffer pool is full.

## 3.2 Transaction Model

Transactions are units of work that access and modify the database. Each transaction has a unique identifier (TransactionID or TID). A transaction consists of:

- **Read operations**: Access data without modifying it
- **Write operations**: Modify data (insert, update, delete)
- **Commit or Abort**: Transaction termination

ARIES assumes a transaction processes records by:
1. Acquiring locks on the data to be accessed (concurrency control)
2. Reading pages containing the data into the buffer pool
3. Modifying pages in the buffer (updates are logged before being applied)
4. Releasing locks at commit or abort

## 3.3 Locking and Concurrency Control

ARIES is compatible with various concurrency control mechanisms but assumes a locking-based protocol. The system supports:

- **Multiple lock granularities**: Record-level, page-level, table-level locks
- **Multiple lock modes**: Shared (S) locks for reads, Exclusive (X) locks for writes
- **Lock hierarchy**: Intention locks (IS, IX, SIX) for efficient multi-granularity locking

Locks are held according to the strict two-phase locking (2PL) protocol:
- Locks are acquired as needed during transaction execution
- All locks are held until the transaction commits or aborts
- This ensures serializability of concurrent transactions

## 3.4 Log Organization

The **log** is a sequential append-only file stored on stable storage. Each log record contains:

- **LSN**: Log Sequence Number (unique identifier)
- **TransID**: Transaction identifier
- **Type**: Type of log record (update, commit, abort, CLR, checkpoint, etc.)
- **PageID**: Identifier of the page affected (for update records)
- **PrevLSN**: LSN of the previous log record for this transaction (forms a backward chain)
- **Undo information**: Data needed to undo the operation
- **Redo information**: Data needed to redo the operation

Log records are written to a log buffer in memory and periodically flushed to stable storage. The **write-ahead logging (WAL) protocol** ensures log records reach stable storage before corresponding page updates.

## 3.5 Failure Model

ARIES handles the following types of failures:

**Transaction Abort**: A transaction voluntarily aborts or is aborted by the system (e.g., due to deadlock). The transaction's effects must be undone.

**System Crash**: The system fails due to power loss, operating system crash, or software bug. Main memory contents (buffer pool, transaction table, dirty page table) are lost, but stable storage (disk, log) contents survive.

**Media Failure**: Disk failure results in loss of database pages. Recovery requires restoring from backups and replaying the log (not covered in detail in the base ARIES paper).

ARIES does **not** assume:
- That the buffer pool is empty at the time of crash (dirty pages may exist)
- That all committed transactions have written their pages to disk
- That uncommitted transactions have not written pages to disk

These assumptions necessitate the sophisticated recovery algorithm.

## 3.6 Page Structure

Each database page contains:

- **PageLSN**: LSN of the most recent update to this page
- **Data**: The actual data stored on the page (records, index entries, etc.)

The PageLSN is crucial for recovery. Before writing a page to disk, the buffer manager ensures that all log records up to and including PageLSN have been written to stable storage (enforcing WAL).

During recovery, PageLSN is compared with log record LSNs to determine whether an update needs to be reapplied (redone).

## 3.7 Stable Storage

**Stable storage** refers to storage that survives system crashes. In practice, this is typically:
- Mirrored disks (RAID)
- Battery-backed non-volatile memory
- Multiple copies of critical data

The log is stored on stable storage to ensure recoverability. ARIES assumes that writes to stable storage are atomic at the block level - either a complete block is written or the old contents remain.

---

### النسخة العربية

يصف هذا القسم نموذج النظام والافتراضات الكامنة وراء ARIES.

## 3.1 تنظيم قاعدة البيانات والتخزين

تتكون قاعدة البيانات من مجموعة من **الصفحات** المخزنة على تخزين غير متطاير (القرص). كل صفحة لها معرّف فريد (PageID) وحجم ثابت (عادةً 4KB-16KB). تحتوي الصفحات على سجلات البيانات أو إدخالات الفهرس أو بنى قاعدة البيانات الأخرى.

يحتفظ النظام **بمجمع مخزن مؤقت** في الذاكرة الرئيسية للتخزين المؤقت للصفحات التي يتم الوصول إليها بشكل متكرر. يتحكم مدير المخزن المؤقت في الصفحات الموجودة في الذاكرة ومتى يتم كتابة الصفحات المعدلة على القرص (المسح).

تمر جميع التحديثات على الصفحات عبر مجمع المخزن المؤقت - يتم قراءة الصفحات في المخزن المؤقت، وتعديلها في الذاكرة، وكتابتها في النهاية مرة أخرى على القرص. يستخدم مدير المخزن المؤقت سياسة استبدال الصفحة (مثل LRU) لتحديد الصفحات التي يجب إخلاؤها عندما يكون مجمع المخزن المؤقت ممتلئاً.

## 3.2 نموذج المعاملات

المعاملات هي وحدات عمل تصل إلى قاعدة البيانات وتعدلها. كل معاملة لها معرّف فريد (TransactionID أو TID). تتكون المعاملة من:

- **عمليات القراءة**: الوصول إلى البيانات دون تعديلها
- **عمليات الكتابة**: تعديل البيانات (إدراج، تحديث، حذف)
- **التثبيت أو الإلغاء**: إنهاء المعاملة

تفترض ARIES أن المعاملة تعالج السجلات من خلال:
1. الحصول على أقفال على البيانات المراد الوصول إليها (التحكم في التزامن)
2. قراءة الصفحات التي تحتوي على البيانات في مجمع المخزن المؤقت
3. تعديل الصفحات في المخزن المؤقت (يتم تسجيل التحديثات قبل تطبيقها)
4. إطلاق الأقفال عند التثبيت أو الإلغاء

## 3.3 القفل والتحكم في التزامن

ARIES متوافقة مع آليات التحكم في التزامن المختلفة ولكنها تفترض بروتوكولاً قائماً على القفل. يدعم النظام:

- **درجات تفصيل قفل متعددة**: أقفال مستوى السجل والصفحة والجدول
- **أوضاع قفل متعددة**: أقفال مشتركة (S) للقراءة، أقفال حصرية (X) للكتابة
- **تسلسل هرمي للقفل**: أقفال النوايا (IS, IX, SIX) للقفل متعدد الدرجات الفعال

يتم الاحتفاظ بالأقفال وفقاً لبروتوكول القفل الصارم ثنائي المراحل (2PL):
- يتم الحصول على الأقفال حسب الحاجة أثناء تنفيذ المعاملة
- يتم الاحتفاظ بجميع الأقفال حتى تثبيت المعاملة أو إلغاؤها
- هذا يضمن قابلية التسلسل للمعاملات المتزامنة

## 3.4 تنظيم السجل

**السجل** هو ملف تسلسلي للإلحاق فقط مخزن على تخزين مستقر. يحتوي كل سجل على:

- **LSN**: رقم تسلسل السجل (معرّف فريد)
- **TransID**: معرّف المعاملة
- **Type**: نوع سجل السجل (تحديث، تثبيت، إلغاء، CLR، نقطة تحقق، إلخ)
- **PageID**: معرّف الصفحة المتأثرة (لسجلات التحديث)
- **PrevLSN**: LSN لسجل السجل السابق لهذه المعاملة (يشكل سلسلة عكسية)
- **معلومات التراجع**: البيانات اللازمة للتراجع عن العملية
- **معلومات الإعادة**: البيانات اللازمة لإعادة العملية

تُكتب سجلات السجل في مخزن مؤقت للسجل في الذاكرة ويتم مسحها بشكل دوري إلى التخزين المستقر. يضمن **بروتوكول التسجيل المسبق للكتابة (WAL)** وصول سجلات السجل إلى التخزين المستقر قبل تحديثات الصفحة المقابلة.

## 3.5 نموذج الفشل

تتعامل ARIES مع أنواع الأعطال التالية:

**إلغاء المعاملة**: معاملة تلغي طوعاً أو يتم إلغاؤها بواسطة النظام (على سبيل المثال، بسبب الجمود). يجب التراجع عن تأثيرات المعاملة.

**تعطل النظام**: يفشل النظام بسبب فقدان الطاقة أو تعطل نظام التشغيل أو خطأ برمجي. تُفقد محتويات الذاكرة الرئيسية (مجمع المخزن المؤقت، جدول المعاملات، جدول الصفحات المعدلة)، لكن محتويات التخزين المستقر (القرص، السجل) تبقى.

**فشل الوسائط**: يؤدي فشل القرص إلى فقدان صفحات قاعدة البيانات. يتطلب الاسترداد الاستعادة من النسخ الاحتياطية وإعادة تشغيل السجل (غير مغطى بالتفصيل في بحث ARIES الأساسي).

لا تفترض ARIES:
- أن مجمع المخزن المؤقت فارغ وقت التعطل (قد توجد صفحات معدلة)
- أن جميع المعاملات المثبتة كتبت صفحاتها على القرص
- أن المعاملات غير المثبتة لم تكتب صفحات على القرص

تتطلب هذه الافتراضات خوارزمية استرداد متطورة.

## 3.6 بنية الصفحة

تحتوي كل صفحة قاعدة بيانات على:

- **PageLSN**: LSN لأحدث تحديث لهذه الصفحة
- **البيانات**: البيانات الفعلية المخزنة على الصفحة (السجلات، إدخالات الفهرس، إلخ)

PageLSN أمر بالغ الأهمية للاسترداد. قبل كتابة صفحة على القرص، يضمن مدير المخزن المؤقت أن جميع سجلات السجل حتى وبما في ذلك PageLSN قد تمت كتابتها إلى التخزين المستقر (تطبيق WAL).

أثناء الاسترداد، تتم مقارنة PageLSN مع LSNs سجلات السجل لتحديد ما إذا كان يجب إعادة تطبيق تحديث (إعادة).

## 3.7 التخزين المستقر

**التخزين المستقر** يشير إلى التخزين الذي ينجو من تعطل النظام. عملياً، هذا عادة:
- أقراص معكوسة (RAID)
- ذاكرة غير متطايرة مدعومة بالبطارية
- نسخ متعددة من البيانات الحرجة

يُخزن السجل على تخزين مستقر لضمان قابلية الاسترداد. تفترض ARIES أن عمليات الكتابة إلى التخزين المستقر ذرية على مستوى الكتلة - إما يتم كتابة كتلة كاملة أو تبقى المحتويات القديمة.

---

### Translation Notes

- **Key concepts introduced:** Buffer pool, page structure, transaction model, locking protocols, log structure, failure types, stable storage
- **Technical terms:** PageID, TransactionID, PageLSN, PrevLSN, LRU, RAID, 2PL, WAL
- **Lock modes:** S (Shared), X (Exclusive), IS (Intention Shared), IX (Intention Exclusive), SIX (Shared+Intention Exclusive)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
