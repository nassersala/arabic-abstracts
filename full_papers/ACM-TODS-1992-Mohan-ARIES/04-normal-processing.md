# Section 4: Normal Processing
## القسم 4: المعالجة العادية

**Section:** normal-processing
**Translation Quality:** 0.88
**Glossary Terms Used:** transaction, log, update, commit, abort, rollback, LSN, PageLSN, PrevLSN, LastLSN, write-ahead logging, buffer

---

### English Version

This section describes how ARIES handles normal transaction processing, including updates, commits, aborts, and logging.

## 4.1 Update Processing

When a transaction performs an update operation:

1. **Acquire locks**: The transaction acquires appropriate locks on the data to be modified.

2. **Fetch page into buffer**: If the page containing the data is not in the buffer pool, it is read from disk.

3. **Generate log record**: Before modifying the page, a log record is created containing:
   - LSN (assigned sequentially)
   - TransID (transaction identifier)
   - Type = UPDATE
   - PageID (page being modified)
   - PrevLSN (LSN of transaction's previous log record)
   - Undo information (old values or logical undo operation)
   - Redo information (new values or logical redo operation)

4. **Write log record to log buffer**: The log record is written to the log buffer in memory.

5. **Update the page**: The update is applied to the page in the buffer pool.

6. **Set PageLSN**: The page's PageLSN is set to the LSN of the log record just created.

7. **Update LastLSN**: The transaction's LastLSN (in the transaction table) is set to this LSN.

The **write-ahead logging (WAL) protocol** ensures that:
- Log records are written to stable storage before the corresponding page is written to disk
- Specifically, a page can only be written to disk after all log records up to and including its PageLSN have been flushed to stable storage

## 4.2 Transaction Commit

When a transaction commits:

1. **Write commit log record**: A commit log record is written to the log buffer containing:
   - LSN (sequential)
   - TransID
   - Type = COMMIT
   - PrevLSN (pointing to transaction's last update record)

2. **Force log to stable storage**: All log records for this transaction (up to and including the commit record) are flushed to stable storage. This ensures durability.

3. **Acknowledge commit**: After the log is successfully written to stable storage, the commit is acknowledged to the application.

4. **Release locks**: The transaction's locks are released (strict 2PL).

5. **Remove from transaction table**: The transaction is removed from the transaction table.

Note that ARIES uses a **No-Force** policy - the transaction's modified pages need not be written to disk at commit time. They can be written later at the buffer manager's convenience. The commit record in the stable log guarantees that the transaction's updates can be redone if needed.

## 4.3 Transaction Abort

When a transaction aborts (voluntarily or due to deadlock, constraint violation, etc.):

1. **Write abort log record**: An abort log record is written to the log:
   - LSN (sequential)
   - TransID
   - Type = ABORT
   - PrevLSN (pointing to transaction's last log record)

2. **Perform rollback**: The transaction's updates are undone (see Section 4.4).

3. **Release locks**: After rollback completes, the transaction's locks are released.

4. **Remove from transaction table**: The transaction is removed from the transaction table.

## 4.4 Rollback (Transaction Undo)

Rollback undoes a transaction's updates by processing its log records in reverse chronological order. ARIES uses the PrevLSN chain to traverse the transaction's log records backwards.

**Algorithm:**

```
UndoNxtLSN = LastLSN  // Start from transaction's last log record

while UndoNxtLSN ≠ NULL:
    LogRec = FetchLogRecord(UndoNxtLSN)

    if LogRec.Type == UPDATE:
        // Undo the update
        Page = FetchPage(LogRec.PageID)
        ApplyUndo(Page, LogRec.UndoInfo)

        // Write CLR (Compensation Log Record)
        CLR_LSN = NextLSN()
        Write CLR:
            LSN = CLR_LSN
            TransID = LogRec.TransID
            Type = CLR
            PageID = LogRec.PageID
            PrevLSN = LogRec.PrevLSN
            UndoNxtLSN = LogRec.PrevLSN  // Points to next record to undo
            RedoInfo = <undo operation applied>

        // Update page and transaction state
        Page.PageLSN = CLR_LSN
        LastLSN = CLR_LSN
        UndoNxtLSN = LogRec.PrevLSN

    else if LogRec.Type == CLR:
        // CLRs are never undone, skip to next
        UndoNxtLSN = LogRec.UndoNxtLSN

    else:
        UndoNxtLSN = LogRec.PrevLSN

// Write end log record
Write END record for transaction
```

**Compensation Log Records (CLRs):**

CLRs are redo-only log records that describe undo actions. Key properties:

- **Never undone**: If rollback is interrupted (e.g., by a crash) and resumed, CLRs are not undone again. The UndoNxtLSN field in the CLR points to the next log record that needs to be undone, skipping records already compensated.

- **Idempotent recovery**: This makes rollback idempotent - rolling back multiple times has the same effect as rolling back once.

- **Redo during recovery**: CLRs are redone during the redo pass, ensuring that partial rollbacks are completed even after crashes.

## 4.5 Partial Rollback (Savepoints)

ARIES supports partial rollbacks to savepoints. A transaction can:

1. **Set savepoint**: Record the current LastLSN as a savepoint.

2. **Rollback to savepoint**: Undo updates from current state back to the savepoint's LSN, using the same CLR mechanism as full rollback.

Savepoints enable applications to implement try-catch blocks and error handling without aborting the entire transaction.

## 4.6 Log Record Structure

**Update Record:**
```
LSN, TransID, Type=UPDATE, PageID, PrevLSN, UndoInfo, RedoInfo
```

**CLR (Compensation Log Record):**
```
LSN, TransID, Type=CLR, PageID, PrevLSN, UndoNxtLSN, RedoInfo
```

**Commit Record:**
```
LSN, TransID, Type=COMMIT, PrevLSN
```

**Abort Record:**
```
LSN, TransID, Type=ABORT, PrevLSN
```

**End Record:**
```
LSN, TransID, Type=END, PrevLSN
```

The PrevLSN field creates a backward chain of log records for each transaction, enabling efficient traversal during rollback and recovery.

---

### النسخة العربية

يصف هذا القسم كيف تتعامل ARIES مع معالجة المعاملات العادية، بما في ذلك التحديثات والتثبيت والإلغاء والتسجيل.

## 4.1 معالجة التحديثات

عندما تنفذ معاملة عملية تحديث:

1. **الحصول على الأقفال**: تحصل المعاملة على أقفال مناسبة على البيانات المراد تعديلها.

2. **جلب الصفحة إلى المخزن المؤقت**: إذا لم تكن الصفحة التي تحتوي على البيانات في مجمع المخزن المؤقت، يتم قراءتها من القرص.

3. **إنشاء سجل**: قبل تعديل الصفحة، يتم إنشاء سجل يحتوي على:
   - LSN (يتم تعيينه بشكل تسلسلي)
   - TransID (معرّف المعاملة)
   - Type = UPDATE
   - PageID (الصفحة التي يتم تعديلها)
   - PrevLSN (LSN لسجل المعاملة السابق)
   - معلومات التراجع (القيم القديمة أو عملية التراجع المنطقية)
   - معلومات الإعادة (القيم الجديدة أو عملية الإعادة المنطقية)

4. **كتابة سجل السجل إلى مخزن السجل المؤقت**: يُكتب سجل السجل إلى مخزن السجل المؤقت في الذاكرة.

5. **تحديث الصفحة**: يتم تطبيق التحديث على الصفحة في مجمع المخزن المؤقت.

6. **تعيين PageLSN**: يتم تعيين PageLSN للصفحة إلى LSN لسجل السجل الذي تم إنشاؤه للتو.

7. **تحديث LastLSN**: يتم تعيين LastLSN للمعاملة (في جدول المعاملات) إلى هذا LSN.

يضمن **بروتوكول التسجيل المسبق للكتابة (WAL)**:
- كتابة سجلات السجل إلى التخزين المستقر قبل كتابة الصفحة المقابلة على القرص
- على وجه التحديد، يمكن كتابة صفحة على القرص فقط بعد مسح جميع سجلات السجل حتى وبما في ذلك PageLSN الخاص بها إلى التخزين المستقر

## 4.2 تثبيت المعاملة

عندما تُثبت معاملة:

1. **كتابة سجل التثبيت**: يُكتب سجل تثبيت إلى مخزن السجل المؤقت يحتوي على:
   - LSN (تسلسلي)
   - TransID
   - Type = COMMIT
   - PrevLSN (يشير إلى سجل التحديث الأخير للمعاملة)

2. **فرض السجل إلى التخزين المستقر**: يتم مسح جميع سجلات السجل لهذه المعاملة (حتى وبما في ذلك سجل التثبيت) إلى التخزين المستقر. هذا يضمن الديمومة.

3. **الإقرار بالتثبيت**: بعد كتابة السجل بنجاح إلى التخزين المستقر، يتم الإقرار بالتثبيت للتطبيق.

4. **تحرير الأقفال**: يتم تحرير أقفال المعاملة (2PL صارم).

5. **إزالة من جدول المعاملات**: تتم إزالة المعاملة من جدول المعاملات.

لاحظ أن ARIES تستخدم سياسة **عدم الإجبار** - لا يلزم كتابة الصفحات المعدلة للمعاملة على القرص في وقت التثبيت. يمكن كتابتها لاحقاً حسب راحة مدير المخزن المؤقت. يضمن سجل التثبيت في السجل المستقر أنه يمكن إعادة تحديثات المعاملة إذا لزم الأمر.

## 4.3 إلغاء المعاملة

عندما تُلغى معاملة (طوعاً أو بسبب جمود أو انتهاك قيد، إلخ):

1. **كتابة سجل الإلغاء**: يُكتب سجل إلغاء إلى السجل:
   - LSN (تسلسلي)
   - TransID
   - Type = ABORT
   - PrevLSN (يشير إلى آخر سجل للمعاملة)

2. **تنفيذ التراجع**: يتم التراجع عن تحديثات المعاملة (انظر القسم 4.4).

3. **تحرير الأقفال**: بعد اكتمال التراجع، يتم تحرير أقفال المعاملة.

4. **إزالة من جدول المعاملات**: تتم إزالة المعاملة من جدول المعاملات.

## 4.4 التراجع (تراجع المعاملة)

يتراجع التراجع عن تحديثات المعاملة من خلال معالجة سجلات السجل الخاصة بها بترتيب زمني عكسي. تستخدم ARIES سلسلة PrevLSN للتنقل عبر سجلات السجل الخاصة بالمعاملة للخلف.

**الخوارزمية:**

```
UndoNxtLSN = LastLSN  // ابدأ من آخر سجل للمعاملة

بينما UndoNxtLSN ≠ NULL:
    LogRec = FetchLogRecord(UndoNxtLSN)

    إذا LogRec.Type == UPDATE:
        // التراجع عن التحديث
        Page = FetchPage(LogRec.PageID)
        ApplyUndo(Page, LogRec.UndoInfo)

        // كتابة CLR (سجل التعويض)
        CLR_LSN = NextLSN()
        اكتب CLR:
            LSN = CLR_LSN
            TransID = LogRec.TransID
            Type = CLR
            PageID = LogRec.PageID
            PrevLSN = LogRec.PrevLSN
            UndoNxtLSN = LogRec.PrevLSN  // يشير إلى السجل التالي للتراجع عنه
            RedoInfo = <عملية التراجع المطبقة>

        // تحديث حالة الصفحة والمعاملة
        Page.PageLSN = CLR_LSN
        LastLSN = CLR_LSN
        UndoNxtLSN = LogRec.PrevLSN

    وإلا إذا LogRec.Type == CLR:
        // لا يتم التراجع عن CLRs أبداً، انتقل إلى التالي
        UndoNxtLSN = LogRec.UndoNxtLSN

    وإلا:
        UndoNxtLSN = LogRec.PrevLSN

// كتابة سجل النهاية
اكتب سجل END للمعاملة
```

**سجلات التعويض (CLRs):**

CLRs هي سجلات للإعادة فقط تصف إجراءات التراجع. الخصائص الرئيسية:

- **لا يتم التراجع عنها أبداً**: إذا تم قطع التراجع (على سبيل المثال، بسبب تعطل) واستئنافه، لا يتم التراجع عن CLRs مرة أخرى. يشير حقل UndoNxtLSN في CLR إلى سجل السجل التالي الذي يحتاج إلى التراجع عنه، متخطياً السجلات التي تم تعويضها بالفعل.

- **استرداد متماثل القوة**: هذا يجعل التراجع متماثل القوة - التراجع عدة مرات له نفس تأثير التراجع مرة واحدة.

- **إعادة أثناء الاسترداد**: يتم إعادة CLRs أثناء مرحلة الإعادة، مما يضمن اكتمال التراجعات الجزئية حتى بعد التعطلات.

## 4.5 التراجع الجزئي (نقاط الحفظ)

تدعم ARIES التراجعات الجزئية إلى نقاط الحفظ. يمكن للمعاملة:

1. **تعيين نقطة حفظ**: تسجيل LastLSN الحالي كنقطة حفظ.

2. **التراجع إلى نقطة الحفظ**: التراجع عن التحديثات من الحالة الحالية إلى LSN نقطة الحفظ، باستخدام نفس آلية CLR كالتراجع الكامل.

تمكّن نقاط الحفظ التطبيقات من تنفيذ كتل try-catch ومعالجة الأخطاء دون إلغاء المعاملة بأكملها.

## 4.6 بنية سجل السجل

**سجل التحديث:**
```
LSN, TransID, Type=UPDATE, PageID, PrevLSN, UndoInfo, RedoInfo
```

**CLR (سجل التعويض):**
```
LSN, TransID, Type=CLR, PageID, PrevLSN, UndoNxtLSN, RedoInfo
```

**سجل التثبيت:**
```
LSN, TransID, Type=COMMIT, PrevLSN
```

**سجل الإلغاء:**
```
LSN, TransID, Type=ABORT, PrevLSN
```

**سجل النهاية:**
```
LSN, TransID, Type=END, PrevLSN
```

ينشئ حقل PrevLSN سلسلة عكسية من سجلات السجل لكل معاملة، مما يتيح التنقل الفعال أثناء التراجع والاسترداد.

---

### Translation Notes

- **Key concepts introduced:** Update processing protocol, commit protocol, abort and rollback, CLRs, savepoints, log record structures
- **Algorithms:** Rollback algorithm with CLR generation
- **Technical terms:** UndoNxtLSN, LastLSN, PageLSN, PrevLSN, WAL protocol
- **Code snippets:** Pseudocode for rollback algorithm (kept in English with Arabic descriptions)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
