# Section 2: Goals, Assumptions, and Concepts
## القسم 2: الأهداف والافتراضات والمفاهيم

**Section:** Goals, Assumptions, and Concepts
**Translation Quality:** 0.87
**Glossary Terms Used:** transaction, atomicity, durability, consistency, isolation, ACID, concurrent, page, buffer, log, checkpoint, commit, abort, crash, recovery

---

### English Version

#### 2.1 Design Goals

ARIES was designed to meet several critical objectives that distinguish it from previous recovery methods:

**Performance Goals:**
- Minimize logging overhead during normal transaction processing
- Enable fast restart recovery with predictable recovery time bounds
- Support flexible buffer management policies (No-Force, Steal)
- Allow high concurrency through fine-granularity locking
- Reduce the amount of work during recovery

**Functionality Goals:**
- Support partial transaction rollback via savepoints
- Enable nested transactions and nested top actions
- Handle media failures independent of system crash recovery
- Support both value-based and operation-based logging
- Provide simple and modular recovery protocols

**Robustness Goals:**
- Ensure correctness under all failure scenarios
- Support recovery from arbitrary sequences of failures
- Enable online reorganization and media recovery
- Maintain backward traversal of log for selective undo

The fundamental principle underlying ARIES is the concept of **repeating history during restart recovery**. After a crash, the system first restores the database to exactly the state it was in at the time of the crash, including all changes made by both committed and uncommitted transactions. Only after reaching this point does the system begin rolling back uncommitted transactions. This approach simplifies recovery logic and enables many advanced features.

#### 2.2 System Model and Assumptions

ARIES makes several assumptions about the underlying system:

**Storage Hierarchy:**
- **Stable Storage:** The log resides on stable storage, implemented using redundancy (mirrored disks, battery-backed memory). Stable storage survives all failures except media failures.
- **Disk Storage:** Database pages reside on disk. Pages may be lost due to media failures but are recoverable using archive logs.
- **Volatile Storage:** Buffer pool in main memory holds cached copies of disk pages. Contents are lost on system crashes.

**Transaction Properties:**
- Transactions are sequences of actions that must appear atomic
- Each transaction has a unique transaction identifier (TID)
- Transactions may contain savepoints for partial rollback
- Transactions either commit (making changes permanent) or abort (undoing all changes)

**Page Model:**
- The database consists of fixed-size pages
- Each page has a unique page identifier
- Pages contain records or other data structures
- A page may be modified by multiple transactions concurrently

**Logging Model:**
- All changes are described in log records before being applied to database pages
- Log records are written sequentially to stable storage
- Each log record receives a unique Log Sequence Number (LSN)
- The log is the authoritative record of all database changes

#### 2.3 Fundamental Concepts

**Log Sequence Numbers (LSNs):**
LSNs are monotonically increasing identifiers assigned to each log record in the order they are written. LSNs serve multiple critical purposes:
- Uniquely identify log records
- Establish temporal ordering of updates
- Track the state of pages and transactions
- Determine which updates need to be redone or undone

Each page in the database maintains a **PageLSN**—the LSN of the most recent update applied to that page. This enables the system to determine whether logged changes have been written to disk.

**Write-Ahead Logging (WAL) Protocol:**
The WAL protocol enforces two critical rules:
1. **Before Writing a Dirty Page:** The log record describing every update on that page must be written to stable storage before the page can be written to disk. This ensures redo information is preserved.
2. **Before Committing a Transaction:** All log records for that transaction, including the commit record, must be written to stable storage. This ensures atomicity and durability.

**Transaction Table and Dirty Page Table:**
During normal processing and recovery, the system maintains two critical in-memory data structures:
- **Transaction Table:** Tracks active transactions, their current state, and their most recent LSN
- **Dirty Page Table:** Records which pages have been modified in the buffer pool and the LSN of the first log record that made each page dirty (RecLSN)

**Compensation Log Records (CLRs):**
When undoing an update (during transaction rollback or recovery), the system writes a CLR describing the undo action. CLRs are "redo-only" records—they are never undone themselves. Each CLR contains a **UndoNxtLSN** pointer indicating the next log record to be processed during undo, enabling the system to skip over already-compensated actions.

**Checkpoints:**
ARIES uses "fuzzy checkpoints" that do not require quiescing the system. A checkpoint record contains:
- Contents of the transaction table
- Contents of the dirty page table
- The LSN of the begin_checkpoint record

Fuzzy checkpoints reduce checkpoint overhead and enable continuous system operation.

**Force and Steal Policies:**
- **No-Force:** At commit time, modified pages need not be forced to disk. This reduces I/O but requires redo during recovery.
- **Steal:** Buffer frames containing uncommitted changes may be written to disk. This improves buffer utilization but requires undo during recovery.

These policies provide maximum flexibility but necessitate sophisticated recovery mechanisms to ensure correctness.

---

### النسخة العربية

#### 2.1 أهداف التصميم

تم تصميم ARIES لتحقيق عدة أهداف حرجة تميزها عن طرق الاسترداد السابقة:

**أهداف الأداء:**
- تقليل حمل التسجيل أثناء معالجة المعاملات العادية
- تمكين استرداد إعادة التشغيل السريع مع حدود زمنية متوقعة للاسترداد
- دعم سياسات إدارة مخازن مؤقتة مرنة (عدم الإجبار والسرقة)
- السماح بتزامن عالٍ من خلال القفل دقيق التفصيل
- تقليل حجم العمل أثناء الاسترداد

**أهداف الوظيفية:**
- دعم التراجع الجزئي للمعاملات عبر نقاط الحفظ
- تمكين المعاملات المتداخلة والإجراءات العليا المتداخلة
- معالجة فشل الوسائط بشكل مستقل عن استرداد أعطال النظام
- دعم التسجيل القائم على القيمة والتسجيل القائم على العمليات
- توفير بروتوكولات استرداد بسيطة ونمطية

**أهداف المتانة:**
- ضمان الصحة في جميع سيناريوهات الفشل
- دعم الاسترداد من تسلسلات عشوائية من الفشل
- تمكين إعادة التنظيم عبر الإنترنت واسترداد الوسائط
- الحفاظ على المسار العكسي للسجل للتراجع الانتقائي

المبدأ الأساسي الذي تقوم عليه ARIES هو مفهوم **تكرار التاريخ أثناء استرداد إعادة التشغيل**. بعد العطل، يستعيد النظام أولاً قاعدة البيانات إلى الحالة التي كانت عليها بالضبط وقت العطل، بما في ذلك جميع التغييرات التي أجرتها المعاملات المُنهاة وغير المُنهاة على حد سواء. فقط بعد الوصول إلى هذه النقطة يبدأ النظام في التراجع عن المعاملات غير المُنهاة. يبسط هذا النهج منطق الاسترداد ويمكّن العديد من الميزات المتقدمة.

#### 2.2 نموذج النظام والافتراضات

تفترض ARIES عدة افتراضات حول النظام الأساسي:

**تسلسل التخزين الهرمي:**
- **التخزين المستقر:** يوجد السجل على تخزين مستقر، يُطبق باستخدام التكرار (أقراص مُنسخة، ذاكرة مدعومة بالبطارية). يبقى التخزين المستقر في جميع الفشل باستثناء فشل الوسائط.
- **تخزين القرص:** توجد صفحات قاعدة البيانات على القرص. قد تُفقد الصفحات بسبب فشل الوسائط ولكن يمكن استردادها باستخدام سجلات الأرشيف.
- **التخزين المتطاير:** يحتفظ مجمع المخازن المؤقتة في الذاكرة الرئيسية بنسخ مخزنة مؤقتاً من صفحات القرص. تُفقد المحتويات عند أعطال النظام.

**خصائص المعاملات:**
- المعاملات هي تسلسلات من الإجراءات التي يجب أن تظهر ذرية
- لكل معاملة معرّف معاملة فريد (TID)
- قد تحتوي المعاملات على نقاط حفظ للتراجع الجزئي
- إما أن تُنهي المعاملات (جعل التغييرات دائمة) أو تُحبط (التراجع عن جميع التغييرات)

**نموذج الصفحة:**
- تتكون قاعدة البيانات من صفحات ذات حجم ثابت
- لكل صفحة معرّف صفحة فريد
- تحتوي الصفحات على سجلات أو بنى بيانات أخرى
- قد تُعدل الصفحة بواسطة معاملات متعددة بشكل متزامن

**نموذج التسجيل:**
- يتم وصف جميع التغييرات في سجلات السجل قبل تطبيقها على صفحات قاعدة البيانات
- تُكتب سجلات السجل بشكل تسلسلي إلى التخزين المستقر
- يتلقى كل سجل سجل رقم تسلسل سجل فريد (LSN)
- السجل هو السجل الموثوق لجميع تغييرات قاعدة البيانات

#### 2.3 المفاهيم الأساسية

**أرقام تسلسل السجل (LSNs):**
LSNs هي معرّفات متزايدة بشكل رتيب تُخصص لكل سجل سجل بالترتيب الذي تُكتب به. تخدم LSNs أغراضاً حرجة متعددة:
- تحديد سجلات السجل بشكل فريد
- إنشاء ترتيب زمني للتحديثات
- تتبع حالة الصفحات والمعاملات
- تحديد التحديثات التي تحتاج إلى الإعادة أو التراجع

تحتفظ كل صفحة في قاعدة البيانات بـ **PageLSN**—LSN لأحدث تحديث مُطبق على تلك الصفحة. يمكّن هذا النظام من تحديد ما إذا كانت التغييرات المسجلة قد كُتبت إلى القرص.

**بروتوكول التسجيل المسبق للكتابة (WAL):**
يفرض بروتوكول WAL قاعدتين حرجتين:
1. **قبل كتابة صفحة متسخة:** يجب كتابة سجل السجل الذي يصف كل تحديث على تلك الصفحة إلى التخزين المستقر قبل أن يمكن كتابة الصفحة إلى القرص. يضمن هذا الحفاظ على معلومات الإعادة.
2. **قبل إنهاء معاملة:** يجب كتابة جميع سجلات السجل لتلك المعاملة، بما في ذلك سجل الإنهاء، إلى التخزين المستقر. يضمن هذا الذرية والدوام.

**جدول المعاملات وجدول الصفحات المتسخة:**
أثناء المعالجة العادية والاسترداد، يحتفظ النظام ببنيتي بيانات حرجتين في الذاكرة:
- **جدول المعاملات:** يتتبع المعاملات النشطة وحالتها الحالية وأحدث LSN لها
- **جدول الصفحات المتسخة:** يسجل الصفحات التي تم تعديلها في مجمع المخازن المؤقتة و LSN لأول سجل سجل جعل كل صفحة متسخة (RecLSN)

**سجلات التعويض (CLRs):**
عند التراجع عن تحديث (أثناء تراجع المعاملات أو الاسترداد)، يكتب النظام CLR يصف إجراء التراجع. CLRs هي سجلات "للإعادة فقط"—لا يتم التراجع عنها أبداً. يحتوي كل CLR على مؤشر **UndoNxtLSN** يشير إلى سجل السجل التالي الذي يجب معالجته أثناء التراجع، مما يمكّن النظام من تخطي الإجراءات التي تم تعويضها بالفعل.

**نقاط التفتيش:**
تستخدم ARIES "نقاط تفتيش ضبابية" لا تتطلب إخماد النظام. يحتوي سجل نقطة التفتيش على:
- محتويات جدول المعاملات
- محتويات جدول الصفحات المتسخة
- LSN لسجل begin_checkpoint

تقلل نقاط التفتيش الضبابية من حمل نقاط التفتيش وتمكّن التشغيل المستمر للنظام.

**سياسات الإجبار والسرقة:**
- **عدم الإجبار:** في وقت الإنهاء، لا يلزم إجبار الصفحات المعدلة على الكتابة إلى القرص. يقلل هذا من الإدخال/الإخراج ولكن يتطلب الإعادة أثناء الاسترداد.
- **السرقة:** يمكن كتابة إطارات المخزن المؤقت التي تحتوي على تغييرات غير مُنهاة إلى القرص. يحسن هذا استخدام المخزن المؤقت ولكن يتطلب التراجع أثناء الاسترداد.

توفر هذه السياسات أقصى قدر من المرونة ولكنها تتطلب آليات استرداد متطورة لضمان الصحة.

---

### Translation Notes

- **Core Concepts:**
  - Repeating history → تكرار التاريخ
  - Stable storage → التخزين المستقر
  - Dirty page → صفحة متسخة
  - PageLSN → رقم تسلسل سجل الصفحة
  - RecLSN → رقم تسلسل سجل الاسترداد
  - UndoNxtLSN → رقم تسلسل التراجع التالي
  - Fuzzy checkpoint → نقطة تفتيش ضبابية

- **Technical Precision:** All ARIES-specific data structures and protocols translated with high fidelity

- **Key Principles:** WAL protocol rules, Force/Steal policies, repeating history concept all precisely preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.87
