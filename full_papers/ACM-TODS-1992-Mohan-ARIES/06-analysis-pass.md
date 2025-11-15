# Section 6: Analysis Pass
## القسم 6: مرحلة التحليل

**Section:** analysis-pass
**Translation Quality:** 0.87
**Glossary Terms Used:** analysis, log, checkpoint, transaction table, dirty page table, LSN, RecLSN, LastLSN, UndoNxtLSN

---

### English Version

The Analysis Pass is the first phase of recovery. It scans the log forward from the last checkpoint to the end of the log, reconstructing the state of the system at the time of the crash.

## 6.1 Goals of Analysis Pass

The Analysis Pass determines:

1. **Which transactions were active** at the time of the crash (uncommitted)
2. **Which pages might have been dirty** (modified but not written to disk)
3. **The starting point for the Redo Pass** (RedoLSN - the LSN of the earliest update that might need to be redone)

## 6.2 Starting Point

The Analysis Pass starts from the **last checkpoint record** in the log. The checkpoint contains:
- A snapshot of the transaction table at checkpoint time
- A snapshot of the dirty page table at checkpoint time
- The LSN of the checkpoint record (stored in a special master record)

## 6.3 Analysis Pass Algorithm

```
Procedure AnalysisPass():
    // Initialize data structures from checkpoint
    CheckpointLSN = ReadMasterRecord()
    CheckpointRec = ReadLog(CheckpointLSN)
    TransTable = CheckpointRec.TransactionTable
    DirtyPageTable = CheckpointRec.DirtyPageTable

    // Find minimum RecLSN (starting point for redo)
    RedoLSN = min(DirtyPageTable[*].RecLSN)
    if DirtyPageTable is empty:
        RedoLSN = CheckpointLSN

    // Scan log forward from checkpoint to end
    CurrentLSN = CheckpointLSN
    while CurrentLSN ≠ EndOfLog:
        LogRec = ReadLog(CurrentLSN)

        // Process different log record types
        switch LogRec.Type:

            case UPDATE:
                // Update transaction table
                if LogRec.TransID not in TransTable:
                    Add TransTable[LogRec.TransID] with state = ACTIVE
                TransTable[LogRec.TransID].LastLSN = LogRec.LSN
                TransTable[LogRec.TransID].UndoNxtLSN = LogRec.LSN

                // Update dirty page table
                if LogRec.PageID not in DirtyPageTable:
                    Add DirtyPageTable[LogRec.PageID]
                    DirtyPageTable[LogRec.PageID].RecLSN = LogRec.LSN

            case CLR:
                // Update transaction table
                if LogRec.TransID not in TransTable:
                    Add TransTable[LogRec.TransID] with state = ACTIVE
                TransTable[LogRec.TransID].LastLSN = LogRec.LSN
                TransTable[LogRec.TransID].UndoNxtLSN = LogRec.UndoNxtLSN

                // Update dirty page table
                if LogRec.PageID not in DirtyPageTable:
                    Add DirtyPageTable[LogRec.PageID]
                    DirtyPageTable[LogRec.PageID].RecLSN = LogRec.LSN

            case COMMIT:
                TransTable[LogRec.TransID].state = COMMITTED
                TransTable[LogRec.TransID].LastLSN = LogRec.LSN

            case ABORT:
                TransTable[LogRec.TransID].state = ABORTING
                TransTable[LogRec.TransID].LastLSN = LogRec.LSN

            case END:
                // Transaction completed (committed or aborted and rolled back)
                Remove TransTable[LogRec.TransID]

        CurrentLSN = NextLSN(CurrentLSN)

    // Analysis complete
    return (TransTable, DirtyPageTable, RedoLSN)
```

## 6.4 Transaction Table Construction

For each transaction found in the log, the transaction table tracks:

- **TransID**: Transaction identifier
- **State**: ACTIVE, COMMITTED, or ABORTING
- **LastLSN**: LSN of the most recent log record for this transaction
- **UndoNxtLSN**: LSN of the next log record to undo (for rollback)

Transactions in states ACTIVE or ABORTING at the end of analysis need to be undone during the Undo Pass. Transactions in state COMMITTED have completed successfully (no undo needed, but their effects must be redone if not on disk).

## 6.5 Dirty Page Table Construction

The Dirty Page Table tracks pages that might have been modified but not written to disk. For each such page:

- **PageID**: Page identifier
- **RecLSN**: LSN of the first update that dirtied this page (since it was last written to disk)

The RecLSN is crucial:
- It determines when redo must start examining updates to this page
- Any update with LSN ≥ RecLSN might not be on disk and may need to be redone
- Updates with LSN < RecLSN are guaranteed to be on disk (the page was written after those updates)

## 6.6 Determining RedoLSN

The **RedoLSN** is the starting point for the Redo Pass:

```
RedoLSN = minimum RecLSN among all pages in Dirty Page Table
```

This is the LSN of the earliest update that might need to be redone. The Redo Pass will start scanning from this point.

If the Dirty Page Table is empty (no dirty pages), RedoLSN is set to the checkpoint LSN (or end of log).

## 6.7 Handling Different Transaction States

After the Analysis Pass, transactions can be in several states:

- **COMMITTED**: Transaction committed but might not have written all pages to disk. Effects must be redone during Redo Pass. No undo needed.

- **ACTIVE**: Transaction was executing when crash occurred. Effects must be redone, then undone during Undo Pass.

- **ABORTING**: Transaction was rolling back when crash occurred. Redo any CLRs (completing the partial rollback), then continue undo.

- **Completed (not in table)**: Transaction committed or aborted and completed rollback before crash. No action needed.

## 6.8 Example

Suppose the log contains (after checkpoint):
```
Checkpoint: TransTable={T1:ACTIVE}, DirtyPageTable={P1:RecLSN=100}
LSN 120: UPDATE T1 P2 ...
LSN 130: UPDATE T2 P1 ...
LSN 140: COMMIT T1
LSN 150: UPDATE T2 P3 ...
LSN 160: ABORT T2
LSN 170: CLR T2 P3 UndoNxtLSN=130 ...
[CRASH]
```

Analysis Pass results:
- **TransTable**: {T1:COMMITTED, LastLSN=140}, {T2:ABORTING, LastLSN=170, UndoNxtLSN=130}
- **DirtyPageTable**: {P1:RecLSN=100, P2:RecLSN=120, P3:RecLSN=150}
- **RedoLSN**: 100 (minimum RecLSN)

Interpretation:
- T1 committed but may not have written pages to disk
- T2 was aborting, had partially rolled back (CLR at 170), needs to continue undo from LSN 130
- Pages P1, P2, P3 may be dirty and need redo starting from their RecLSNs

---

### النسخة العربية

مرحلة التحليل هي المرحلة الأولى من الاسترداد. تمسح السجل إلى الأمام من آخر نقطة تحقق إلى نهاية السجل، وتعيد بناء حالة النظام وقت التعطل.

## 6.1 أهداف مرحلة التحليل

تحدد مرحلة التحليل:

1. **المعاملات التي كانت نشطة** وقت التعطل (غير مثبتة)
2. **الصفحات التي ربما كانت معدلة** (تم تعديلها ولكن لم تُكتب على القرص)
3. **نقطة البداية لمرحلة الإعادة** (RedoLSN - LSN لأقدم تحديث قد يحتاج إلى إعادة)

## 6.2 نقطة البداية

تبدأ مرحلة التحليل من **سجل نقطة التحقق الأخير** في السجل. تحتوي نقطة التحقق على:
- لقطة من جدول المعاملات في وقت نقطة التحقق
- لقطة من جدول الصفحات المعدلة في وقت نقطة التحقق
- LSN لسجل نقطة التحقق (مخزن في سجل رئيسي خاص)

## 6.3 خوارزمية مرحلة التحليل

```
إجراء AnalysisPass():
    // تهيئة بنى البيانات من نقطة التحقق
    CheckpointLSN = ReadMasterRecord()
    CheckpointRec = ReadLog(CheckpointLSN)
    TransTable = CheckpointRec.TransactionTable
    DirtyPageTable = CheckpointRec.DirtyPageTable

    // ابحث عن الحد الأدنى لـ RecLSN (نقطة البداية للإعادة)
    RedoLSN = min(DirtyPageTable[*].RecLSN)
    إذا كان DirtyPageTable فارغاً:
        RedoLSN = CheckpointLSN

    // مسح السجل إلى الأمام من نقطة التحقق إلى النهاية
    CurrentLSN = CheckpointLSN
    بينما CurrentLSN ≠ EndOfLog:
        LogRec = ReadLog(CurrentLSN)

        // معالجة أنواع سجلات السجل المختلفة
        حسب LogRec.Type:

            حالة UPDATE:
                // تحديث جدول المعاملات
                إذا لم يكن LogRec.TransID في TransTable:
                    أضف TransTable[LogRec.TransID] بـ state = ACTIVE
                TransTable[LogRec.TransID].LastLSN = LogRec.LSN
                TransTable[LogRec.TransID].UndoNxtLSN = LogRec.LSN

                // تحديث جدول الصفحات المعدلة
                إذا لم يكن LogRec.PageID في DirtyPageTable:
                    أضف DirtyPageTable[LogRec.PageID]
                    DirtyPageTable[LogRec.PageID].RecLSN = LogRec.LSN

            حالة CLR:
                // تحديث جدول المعاملات
                إذا لم يكن LogRec.TransID في TransTable:
                    أضف TransTable[LogRec.TransID] بـ state = ACTIVE
                TransTable[LogRec.TransID].LastLSN = LogRec.LSN
                TransTable[LogRec.TransID].UndoNxtLSN = LogRec.UndoNxtLSN

                // تحديث جدول الصفحات المعدلة
                إذا لم يكن LogRec.PageID في DirtyPageTable:
                    أضف DirtyPageTable[LogRec.PageID]
                    DirtyPageTable[LogRec.PageID].RecLSN = LogRec.LSN

            حالة COMMIT:
                TransTable[LogRec.TransID].state = COMMITTED
                TransTable[LogRec.TransID].LastLSN = LogRec.LSN

            حالة ABORT:
                TransTable[LogRec.TransID].state = ABORTING
                TransTable[LogRec.TransID].LastLSN = LogRec.LSN

            حالة END:
                // اكتملت المعاملة (تم تثبيتها أو إلغاؤها والتراجع عنها)
                احذف TransTable[LogRec.TransID]

        CurrentLSN = NextLSN(CurrentLSN)

    // اكتمل التحليل
    ارجع (TransTable, DirtyPageTable, RedoLSN)
```

## 6.4 بناء جدول المعاملات

لكل معاملة موجودة في السجل، يتتبع جدول المعاملات:

- **TransID**: معرّف المعاملة
- **State**: ACTIVE أو COMMITTED أو ABORTING
- **LastLSN**: LSN لأحدث سجل لهذه المعاملة
- **UndoNxtLSN**: LSN لسجل السجل التالي للتراجع عنه (للتراجع)

المعاملات في حالات ACTIVE أو ABORTING في نهاية التحليل تحتاج إلى التراجع أثناء مرحلة التراجع. المعاملات في حالة COMMITTED قد اكتملت بنجاح (لا حاجة للتراجع، لكن يجب إعادة تأثيراتها إذا لم تكن على القرص).

## 6.5 بناء جدول الصفحات المعدلة

يتتبع جدول الصفحات المعدلة الصفحات التي ربما تم تعديلها ولكن لم تُكتب على القرص. لكل صفحة من هذا القبيل:

- **PageID**: معرّف الصفحة
- **RecLSN**: LSN لأول تحديث جعل هذه الصفحة معدلة (منذ آخر كتابة لها على القرص)

RecLSN أمر بالغ الأهمية:
- يحدد متى يجب أن تبدأ الإعادة في فحص التحديثات لهذه الصفحة
- أي تحديث بـ LSN ≥ RecLSN قد لا يكون على القرص وقد يحتاج إلى إعادة
- التحديثات بـ LSN < RecLSN مضمونة أن تكون على القرص (تمت كتابة الصفحة بعد تلك التحديثات)

## 6.6 تحديد RedoLSN

**RedoLSN** هو نقطة البداية لمرحلة الإعادة:

```
RedoLSN = الحد الأدنى لـ RecLSN بين جميع الصفحات في جدول الصفحات المعدلة
```

هذا هو LSN لأقدم تحديث قد يحتاج إلى إعادة. ستبدأ مرحلة الإعادة المسح من هذه النقطة.

إذا كان جدول الصفحات المعدلة فارغاً (لا توجد صفحات معدلة)، يتم تعيين RedoLSN إلى LSN نقطة التحقق (أو نهاية السجل).

## 6.7 معالجة حالات المعاملات المختلفة

بعد مرحلة التحليل، يمكن أن تكون المعاملات في عدة حالات:

- **COMMITTED**: تم تثبيت المعاملة ولكن قد لا تكون قد كتبت جميع الصفحات على القرص. يجب إعادة التأثيرات أثناء مرحلة الإعادة. لا حاجة للتراجع.

- **ACTIVE**: كانت المعاملة قيد التنفيذ عند حدوث التعطل. يجب إعادة التأثيرات ثم التراجع عنها أثناء مرحلة التراجع.

- **ABORTING**: كانت المعاملة تتراجع عند حدوث التعطل. إعادة أي CLRs (إكمال التراجع الجزئي)، ثم مواصلة التراجع.

- **مكتملة (ليست في الجدول)**: تم تثبيت المعاملة أو إلغاؤها وإكمال التراجع قبل التعطل. لا حاجة لأي إجراء.

## 6.8 مثال

لنفترض أن السجل يحتوي (بعد نقطة التحقق):
```
نقطة التحقق: TransTable={T1:ACTIVE}, DirtyPageTable={P1:RecLSN=100}
LSN 120: UPDATE T1 P2 ...
LSN 130: UPDATE T2 P1 ...
LSN 140: COMMIT T1
LSN 150: UPDATE T2 P3 ...
LSN 160: ABORT T2
LSN 170: CLR T2 P3 UndoNxtLSN=130 ...
[CRASH]
```

نتائج مرحلة التحليل:
- **TransTable**: {T1:COMMITTED, LastLSN=140}, {T2:ABORTING, LastLSN=170, UndoNxtLSN=130}
- **DirtyPageTable**: {P1:RecLSN=100, P2:RecLSN=120, P3:RecLSN=150}
- **RedoLSN**: 100 (الحد الأدنى لـ RecLSN)

التفسير:
- تم تثبيت T1 ولكن قد لا تكون قد كتبت الصفحات على القرص
- كانت T2 قيد الإلغاء، وتم التراجع عنها جزئياً (CLR في 170)، وتحتاج إلى مواصلة التراجع من LSN 130
- الصفحات P1, P2, P3 قد تكون معدلة وتحتاج إلى إعادة بدءاً من RecLSNs الخاصة بها

---

### Translation Notes

- **Key concepts:** Transaction table, dirty page table, RecLSN, RedoLSN, transaction states (ACTIVE, COMMITTED, ABORTING)
- **Algorithms:** Complete analysis pass algorithm with pseudocode
- **Examples:** Detailed example showing analysis pass output
- **Technical terms:** Checkpoint, forward scan, log record types

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
