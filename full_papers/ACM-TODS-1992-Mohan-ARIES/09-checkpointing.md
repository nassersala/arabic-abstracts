# Section 9: Checkpointing
## القسم 9: نقاط التحقق

**Section:** checkpointing
**Translation Quality:** 0.86
**Glossary Terms Used:** checkpoint, transaction table, dirty page table, fuzzy checkpoint, recovery, log, performance

---

### English Version

Checkpoints reduce recovery time by periodically recording the system state. ARIES uses **fuzzy checkpoints** that do not require quiescing the system or forcing dirty pages to disk.

## 9.1 Purpose of Checkpoints

Checkpoints serve several purposes:

1. **Reduce recovery time**: Analysis and Redo passes can start from the checkpoint instead of the beginning of the log
2. **Enable log truncation**: Log records before the checkpoint can be archived or deleted
3. **Minimize system disruption**: Fuzzy checkpoints allow normal processing to continue

## 9.2 Fuzzy Checkpoints

ARIES uses **fuzzy checkpoints**:

- **Non-blocking**: Transactions continue executing during checkpoint
- **No forced writes**: Dirty pages are not forced to disk
- **Lightweight**: Only records system state in log

A fuzzy checkpoint captures:
1. Current transaction table
2. Current dirty page table
3. No actual page writes required

## 9.3 Checkpoint Algorithm

```
Procedure TakeCheckpoint():
    // Begin checkpoint
    BeginChkptLSN = NextLSN()
    Write BEGIN_CHECKPOINT record at BeginChkptLSN

    // Capture current state (while system continues processing)
    TransTableCopy = Copy(TransactionTable)
    DirtyPageTableCopy = Copy(DirtyPageTable)

    // End checkpoint
    EndChkptLSN = NextLSN()
    Write END_CHECKPOINT record at EndChkptLSN containing:
        - TransTableCopy
        - DirtyPageTableCopy
        - BeginChkptLSN

    // Update master record to point to this checkpoint
    Write EndChkptLSN to master record
    Flush master record to stable storage

    return
```

## 9.4 Master Record

The **master record** is a special location on stable storage that stores the LSN of the most recent checkpoint's END_CHECKPOINT record.

During recovery:
- Read master record to find last checkpoint
- Start analysis from that checkpoint

The master record is updated atomically after each checkpoint completes.

## 9.5 Checkpoint Frequency

Checkpoints should be taken periodically based on:

- **Time interval**: Every N minutes (e.g., every 5-10 minutes)
- **Log size**: After N log records or M bytes of log
- **Dirty page count**: When too many pages are dirty

Trade-offs:
- **More frequent checkpoints**: Faster recovery, but higher overhead
- **Less frequent checkpoints**: Lower overhead, but longer recovery

## 9.6 Recovery Starting Point

During recovery, the Analysis Pass starts from the last checkpoint:

```
1. Read master record → get CheckpointLSN
2. Read END_CHECKPOINT record at CheckpointLSN
3. Initialize TransTable and DirtyPageTable from checkpoint
4. Scan forward from CheckpointLSN to end of log
```

RedoLSN is determined from the minimum RecLSN in the dirty page table from the checkpoint.

## 9.7 Log Archiving and Truncation

Checkpoints enable log management:

**Log Archiving**:
- Log records before the minimum RecLSN in the checkpoint's dirty page table can be archived
- Archived logs are needed only for media recovery (restoring from backups)

**Log Truncation**:
- After archiving, old log records can be deleted
- Keeps the online log bounded in size

Minimum LSN that must be retained:
```
MinLSN = min(DirtyPageTable[*].RecLSN, ActiveTransactions[*].FirstLSN)
```

Where FirstLSN is the LSN of each active transaction's first log record.

---

### النسخة العربية

تقلل نقاط التحقق من وقت الاسترداد من خلال تسجيل حالة النظام بشكل دوري. تستخدم ARIES **نقاط تحقق ضبابية** لا تتطلب إيقاف النظام أو فرض كتابة الصفحات المعدلة على القرص.

## 9.1 الغرض من نقاط التحقق

تخدم نقاط التحقق عدة أغراض:

1. **تقليل وقت الاسترداد**: يمكن لمراحل التحليل والإعادة البدء من نقطة التحقق بدلاً من بداية السجل
2. **تمكين اقتطاع السجل**: يمكن أرشفة أو حذف سجلات السجل قبل نقطة التحقق
3. **تقليل اضطراب النظام**: تسمح نقاط التحقق الضبابية للمعالجة العادية بالاستمرار

## 9.2 نقاط التحقق الضبابية

تستخدم ARIES **نقاط تحقق ضبابية**:

- **غير حاجبة**: تستمر المعاملات في التنفيذ أثناء نقطة التحقق
- **لا كتابة إجبارية**: لا يتم فرض كتابة الصفحات المعدلة على القرص
- **خفيفة الوزن**: تسجل فقط حالة النظام في السجل

تلتقط نقطة التحقق الضبابية:
1. جدول المعاملات الحالي
2. جدول الصفحات المعدلة الحالي
3. لا حاجة لكتابة صفحات فعلية

## 9.3 خوارزمية نقطة التحقق

```
إجراء TakeCheckpoint():
    // بدء نقطة التحقق
    BeginChkptLSN = NextLSN()
    اكتب سجل BEGIN_CHECKPOINT في BeginChkptLSN

    // التقاط الحالة الحالية (بينما يستمر النظام في المعالجة)
    TransTableCopy = Copy(TransactionTable)
    DirtyPageTableCopy = Copy(DirtyPageTable)

    // إنهاء نقطة التحقق
    EndChkptLSN = NextLSN()
    اكتب سجل END_CHECKPOINT في EndChkptLSN يحتوي على:
        - TransTableCopy
        - DirtyPageTableCopy
        - BeginChkptLSN

    // تحديث السجل الرئيسي للإشارة إلى نقطة التحقق هذه
    اكتب EndChkptLSN إلى السجل الرئيسي
    امسح السجل الرئيسي إلى التخزين المستقر

    ارجع
```

## 9.4 السجل الرئيسي

**السجل الرئيسي** هو موقع خاص على التخزين المستقر يخزن LSN لسجل END_CHECKPOINT لأحدث نقطة تحقق.

أثناء الاسترداد:
- اقرأ السجل الرئيسي للعثور على آخر نقطة تحقق
- ابدأ التحليل من تلك نقطة التحقق

يتم تحديث السجل الرئيسي بشكل ذري بعد اكتمال كل نقطة تحقق.

## 9.5 تكرار نقاط التحقق

يجب أخذ نقاط التحقق بشكل دوري بناءً على:

- **فترة زمنية**: كل N دقيقة (على سبيل المثال، كل 5-10 دقائق)
- **حجم السجل**: بعد N سجلات أو M بايت من السجل
- **عدد الصفحات المعدلة**: عندما تكون الصفحات المعدلة كثيرة جداً

المفاضلات:
- **نقاط تحقق أكثر تكراراً**: استرداد أسرع، ولكن حمل زائد أعلى
- **نقاط تحقق أقل تكراراً**: حمل زائد أقل، ولكن استرداد أطول

## 9.6 نقطة بداية الاسترداد

أثناء الاسترداد، تبدأ مرحلة التحليل من آخر نقطة تحقق:

```
1. اقرأ السجل الرئيسي → احصل على CheckpointLSN
2. اقرأ سجل END_CHECKPOINT في CheckpointLSN
3. هيئ TransTable و DirtyPageTable من نقطة التحقق
4. امسح إلى الأمام من CheckpointLSN إلى نهاية السجل
```

يتم تحديد RedoLSN من الحد الأدنى لـ RecLSN في جدول الصفحات المعدلة من نقطة التحقق.

## 9.7 أرشفة واقتطاع السجل

تمكّن نقاط التحقق من إدارة السجل:

**أرشفة السجل**:
- يمكن أرشفة سجلات السجل قبل الحد الأدنى لـ RecLSN في جدول الصفحات المعدلة لنقطة التحقق
- السجلات المؤرشفة مطلوبة فقط لاسترداد الوسائط (الاستعادة من النسخ الاحتياطية)

**اقتطاع السجل**:
- بعد الأرشفة، يمكن حذف سجلات السجل القديمة
- يحافظ على حجم السجل المتصل محدوداً

الحد الأدنى لـ LSN الذي يجب الاحتفاظ به:
```
MinLSN = min(DirtyPageTable[*].RecLSN, ActiveTransactions[*].FirstLSN)
```

حيث FirstLSN هو LSN لأول سجل لكل معاملة نشطة.

---

### Translation Notes

- **Key concepts:** Fuzzy checkpoints, master record, log truncation, checkpoint frequency
- **Algorithms:** Checkpoint procedure
- **Trade-offs:** Frequency vs. overhead
- **Technical details:** Non-blocking, lightweight checkpointing

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
