# Section 8: Undo Pass
## القسم 8: مرحلة التراجع

**Section:** undo-pass
**Translation Quality:** 0.87
**Glossary Terms Used:** undo, rollback, transaction, CLR, UndoNxtLSN, LastLSN, PrevLSN, log, atomicity

---

### English Version

The Undo Pass is the third and final phase of recovery. It processes transactions that were active at the time of the crash (uncommitted) and undoes their effects, ensuring atomicity.

## 8.1 Goals of Undo Pass

The Undo Pass:

1. **Ensures atomicity**: Removes effects of uncommitted transactions
2. **Handles multiple transactions concurrently**: Undoes all active transactions, potentially interleaving their undo operations
3. **Uses CLRs**: Logs all undo actions as Compensation Log Records
4. **Is idempotent and restartable**: Can be interrupted and restarted safely

## 8.2 Undo Pass Algorithm

```
Procedure UndoPass(TransTable):
    // Build list of transactions to undo
    ToUndo = {}
    for each T in TransTable:
        if T.state == ACTIVE or T.state == ABORTING:
            ToUndo = ToUndo ∪ {(T.LastLSN, T.TransID)}

    // Process undo operations in reverse LSN order
    while ToUndo ≠ ∅:
        // Select log record with maximum LSN
        (LSN, TransID) = max(ToUndo)
        Remove (LSN, TransID) from ToUndo

        LogRec = ReadLog(LSN)

        if LogRec.Type == UPDATE:
            // Undo the update
            Page = ReadPage(LogRec.PageID)
            ApplyUndo(Page, LogRec.UndoInfo)

            // Write CLR
            CLR_LSN = NextLSN()
            Write CLR:
                LSN = CLR_LSN
                TransID = LogRec.TransID
                Type = CLR
                PageID = LogRec.PageID
                PrevLSN = LogRec.PrevLSN
                UndoNxtLSN = LogRec.PrevLSN
                RedoInfo = <undo operation applied>

            // Update page
            Page.PageLSN = CLR_LSN

            // Continue with previous log record
            if LogRec.PrevLSN ≠ NULL:
                ToUndo = ToUndo ∪ {(LogRec.PrevLSN, TransID)}

        else if LogRec.Type == CLR:
            // CLR - skip to UndoNxtLSN
            if LogRec.UndoNxtLSN ≠ NULL:
                ToUndo = ToUndo ∪ {(LogRec.UndoNxtLSN, TransID)}

        else:
            // Other types (should not happen)
            if LogRec.PrevLSN ≠ NULL:
                ToUndo = ToUndo ∪ {(LogRec.PrevLSN, TransID)}

        // If this was the last record for the transaction
        if ToUndo does not contain TransID:
            // Write END record
            Write END record for TransID
            Remove TransID from TransTable

    // Undo complete
    return
```

## 8.3 Processing Multiple Transactions

Unlike normal transaction rollback (which processes one transaction at a time), the Undo Pass processes **all active transactions concurrently** in reverse chronological order of their log records.

This is achieved using a priority queue (or similar structure) containing the next log record LSN to process for each transaction:

1. Select the transaction with the **largest LSN** (most recent log record)
2. Process that log record (undo if UPDATE, skip if CLR)
3. Add the previous log record LSN to the queue
4. Repeat until queue is empty

This approach:
- **Optimizes I/O**: Processes log records in approximately reverse order, improving locality
- **Handles all transactions uniformly**: No special cases
- **Maintains correctness**: Each transaction's updates are undone in reverse order

## 8.4 Handling CLRs During Undo

When the undo pass encounters a CLR (written during a previous partial rollback), it does **not** undo the CLR. Instead:

- Skip to the log record pointed to by the CLR's **UndoNxtLSN** field
- This effectively skips log records that were already undone

Example:
```
Transaction T1's log chain:
LSN 100: UPDATE (PrevLSN=NULL)
LSN 120: UPDATE (PrevLSN=100)
LSN 140: UPDATE (PrevLSN=120)
[Partial rollback during normal processing]
LSN 160: CLR for LSN 140 (PrevLSN=140, UndoNxtLSN=120)
[CRASH]

During undo pass:
- Start at LSN 160 (LastLSN)
- LSN 160 is CLR, skip to UndoNxtLSN=120
- LSN 120 is UPDATE, undo it, write CLR, go to PrevLSN=100
- LSN 100 is UPDATE, undo it, write CLR, go to PrevLSN=NULL
- Done
```

This mechanism ensures that:
- Updates already undone (LSN 140) are not undone again
- Undo is idempotent
- Recovery can be restarted at any point

## 8.5 Writing CLRs

Each undo action is logged as a **Compensation Log Record (CLR)**:

```
CLR structure:
    LSN: New sequential LSN
    TransID: Transaction being undone
    Type: CLR
    PageID: Page being updated
    PrevLSN: Points to transaction's previous log record
    UndoNxtLSN: Points to next log record to undo
    RedoInfo: Describes the undo action applied (for redo during recovery restart)
```

The **UndoNxtLSN** field is crucial:
- It points to the next log record that needs to be undone
- Typically equals the UNDOne record's PrevLSN
- Allows recovery to skip already-compensated updates

CLRs are **redo-only**:
- They are redone during the Redo Pass if recovery restarts
- They are never undone

## 8.6 Transaction Completion

When a transaction's undo is complete (all its updates have been undone):

1. Write an **END record** to the log
2. Remove the transaction from the transaction table
3. The transaction is now fully rolled back

The END record marks the completion of the transaction's undo processing.

## 8.7 Example

Continuing from previous examples:

After Redo Pass, TransTable contains:
- T2: state=ABORTING, LastLSN=170, UndoNxtLSN=130

Undo Pass:
```
ToUndo = {(170, T2)}

Step 1: Process LSN 170
  - LogRec = CLR for T2, UndoNxtLSN=130
  - Skip to LSN 130
  - ToUndo = {(130, T2)}

Step 2: Process LSN 130
  - LogRec = UPDATE T2 P1
  - Undo the update to P1
  - Write CLR at LSN 180: UndoNxtLSN=PrevLSN(from LSN 130)
  - Update Page P1.PageLSN = 180
  - ToUndo = {(PrevLSN, T2)} or empty if PrevLSN=NULL

If there were more updates:
  - Continue processing in reverse chronological order
  - Write CLR for each undo
  - Until all T2's updates are undone

Final step:
  - Write END record for T2
  - Remove T2 from TransTable
```

Result:
- All of T2's effects have been removed
- Database is in a consistent state with only committed transactions' effects

---

### النسخة العربية

مرحلة التراجع هي المرحلة الثالثة والأخيرة من الاسترداد. تعالج المعاملات التي كانت نشطة وقت التعطل (غير مثبتة) وتتراجع عن تأثيراتها، مما يضمن الذرية.

## 8.1 أهداف مرحلة التراجع

مرحلة التراجع:

1. **تضمن الذرية**: تزيل تأثيرات المعاملات غير المثبتة
2. **تتعامل مع معاملات متعددة بشكل متزامن**: تتراجع عن جميع المعاملات النشطة، مع إمكانية تشابك عمليات التراجع الخاصة بها
3. **تستخدم CLRs**: تسجل جميع إجراءات التراجع كسجلات تعويض
4. **متماثلة القوة وقابلة لإعادة التشغيل**: يمكن مقاطعتها وإعادة تشغيلها بأمان

## 8.2 خوارزمية مرحلة التراجع

```
إجراء UndoPass(TransTable):
    // بناء قائمة المعاملات للتراجع عنها
    ToUndo = {}
    لكل T في TransTable:
        إذا T.state == ACTIVE أو T.state == ABORTING:
            ToUndo = ToUndo ∪ {(T.LastLSN, T.TransID)}

    // معالجة عمليات التراجع بترتيب LSN عكسي
    بينما ToUndo ≠ ∅:
        // اختر سجل السجل بأقصى LSN
        (LSN, TransID) = max(ToUndo)
        احذف (LSN, TransID) من ToUndo

        LogRec = ReadLog(LSN)

        إذا LogRec.Type == UPDATE:
            // التراجع عن التحديث
            Page = ReadPage(LogRec.PageID)
            ApplyUndo(Page, LogRec.UndoInfo)

            // كتابة CLR
            CLR_LSN = NextLSN()
            اكتب CLR:
                LSN = CLR_LSN
                TransID = LogRec.TransID
                Type = CLR
                PageID = LogRec.PageID
                PrevLSN = LogRec.PrevLSN
                UndoNxtLSN = LogRec.PrevLSN
                RedoInfo = <عملية التراجع المطبقة>

            // تحديث الصفحة
            Page.PageLSN = CLR_LSN

            // تابع مع سجل السجل السابق
            إذا LogRec.PrevLSN ≠ NULL:
                ToUndo = ToUndo ∪ {(LogRec.PrevLSN, TransID)}

        وإلا إذا LogRec.Type == CLR:
            // CLR - انتقل إلى UndoNxtLSN
            إذا LogRec.UndoNxtLSN ≠ NULL:
                ToUndo = ToUndo ∪ {(LogRec.UndoNxtLSN, TransID)}

        وإلا:
            // أنواع أخرى (لا يجب أن يحدث)
            إذا LogRec.PrevLSN ≠ NULL:
                ToUndo = ToUndo ∪ {(LogRec.PrevLSN, TransID)}

        // إذا كان هذا آخر سجل للمعاملة
        إذا لم يحتوِ ToUndo على TransID:
            // اكتب سجل END
            اكتب سجل END لـ TransID
            احذف TransID من TransTable

    // اكتمل التراجع
    ارجع
```

## 8.3 معالجة معاملات متعددة

على عكس تراجع المعاملة العادي (الذي يعالج معاملة واحدة في كل مرة)، تعالج مرحلة التراجع **جميع المعاملات النشطة بشكل متزامن** بترتيب زمني عكسي لسجلات السجل الخاصة بها.

يتم تحقيق ذلك باستخدام طابور أولوية (أو بنية مماثلة) يحتوي على LSN لسجل السجل التالي للمعالجة لكل معاملة:

1. اختر المعاملة ذات **أكبر LSN** (أحدث سجل)
2. عالج سجل السجل هذا (تراجع إذا كان UPDATE، تخطَّ إذا كان CLR)
3. أضف LSN لسجل السجل السابق إلى الطابور
4. كرر حتى يفرغ الطابور

هذا النهج:
- **يحسن I/O**: يعالج سجلات السجل بترتيب عكسي تقريباً، مما يحسن الموقع
- **يتعامل مع جميع المعاملات بشكل موحد**: لا توجد حالات خاصة
- **يحافظ على الصحة**: يتم التراجع عن تحديثات كل معاملة بترتيب عكسي

## 8.4 معالجة CLRs أثناء التراجع

عندما تواجه مرحلة التراجع CLR (مكتوب أثناء تراجع جزئي سابق)، فإنها **لا** تتراجع عن CLR. بدلاً من ذلك:

- انتقل إلى سجل السجل الذي يشير إليه حقل **UndoNxtLSN** الخاص بـ CLR
- هذا يتخطى بشكل فعال سجلات السجل التي تم التراجع عنها بالفعل

مثال:
```
سلسلة سجل المعاملة T1:
LSN 100: UPDATE (PrevLSN=NULL)
LSN 120: UPDATE (PrevLSN=100)
LSN 140: UPDATE (PrevLSN=120)
[تراجع جزئي أثناء المعالجة العادية]
LSN 160: CLR لـ LSN 140 (PrevLSN=140, UndoNxtLSN=120)
[CRASH]

أثناء مرحلة التراجع:
- ابدأ من LSN 160 (LastLSN)
- LSN 160 هو CLR، انتقل إلى UndoNxtLSN=120
- LSN 120 هو UPDATE، تراجع عنه، اكتب CLR، انتقل إلى PrevLSN=100
- LSN 100 هو UPDATE، تراجع عنه، اكتب CLR، انتقل إلى PrevLSN=NULL
- انتهى
```

هذه الآلية تضمن:
- لا يتم التراجع عن التحديثات التي تم التراجع عنها بالفعل (LSN 140) مرة أخرى
- التراجع متماثل القوة
- يمكن إعادة تشغيل الاسترداد في أي نقطة

## 8.5 كتابة CLRs

يتم تسجيل كل إجراء تراجع **كسجل تعويض (CLR)**:

```
بنية CLR:
    LSN: LSN تسلسلي جديد
    TransID: المعاملة التي يتم التراجع عنها
    Type: CLR
    PageID: الصفحة التي يتم تحديثها
    PrevLSN: يشير إلى سجل السجل السابق للمعاملة
    UndoNxtLSN: يشير إلى سجل السجل التالي للتراجع عنه
    RedoInfo: يصف إجراء التراجع المطبق (لإعادته أثناء إعادة تشغيل الاسترداد)
```

حقل **UndoNxtLSN** أمر بالغ الأهمية:
- يشير إلى سجل السجل التالي الذي يحتاج إلى التراجع عنه
- عادةً يساوي PrevLSN للسجل الذي تم التراجع عنه
- يسمح للاسترداد بتخطي التحديثات التي تم تعويضها بالفعل

CLRs **للإعادة فقط**:
- يتم إعادتها أثناء مرحلة الإعادة إذا أعيد تشغيل الاسترداد
- لا يتم التراجع عنها أبداً

## 8.6 اكتمال المعاملة

عندما يكتمل تراجع المعاملة (تم التراجع عن جميع تحديثاتها):

1. اكتب **سجل END** إلى السجل
2. احذف المعاملة من جدول المعاملات
3. تم الآن التراجع عن المعاملة بالكامل

يمثل سجل END اكتمال معالجة التراجع للمعاملة.

## 8.7 مثال

مواصلة من الأمثلة السابقة:

بعد مرحلة الإعادة، يحتوي TransTable على:
- T2: state=ABORTING, LastLSN=170, UndoNxtLSN=130

مرحلة التراجع:
```
ToUndo = {(170, T2)}

الخطوة 1: معالجة LSN 170
  - LogRec = CLR لـ T2, UndoNxtLSN=130
  - انتقل إلى LSN 130
  - ToUndo = {(130, T2)}

الخطوة 2: معالجة LSN 130
  - LogRec = UPDATE T2 P1
  - التراجع عن التحديث لـ P1
  - اكتب CLR في LSN 180: UndoNxtLSN=PrevLSN(من LSN 130)
  - حدث Page P1.PageLSN = 180
  - ToUndo = {(PrevLSN, T2)} أو فارغ إذا كان PrevLSN=NULL

إذا كانت هناك مزيد من التحديثات:
  - تابع المعالجة بترتيب زمني عكسي
  - اكتب CLR لكل تراجع
  - حتى يتم التراجع عن جميع تحديثات T2

الخطوة الأخيرة:
  - اكتب سجل END لـ T2
  - احذف T2 من TransTable
```

النتيجة:
- تمت إزالة جميع تأثيرات T2
- قاعدة البيانات في حالة متسقة مع تأثيرات المعاملات المثبتة فقط

---

### Translation Notes

- **Key concepts:** Multiple transaction undo, CLR handling, UndoNxtLSN, priority queue processing, END records
- **Algorithms:** Complete undo pass algorithm
- **Examples:** Detailed walkthrough showing CLR processing
- **Technical details:** Idempotency, restartability, atomicity guarantee

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
