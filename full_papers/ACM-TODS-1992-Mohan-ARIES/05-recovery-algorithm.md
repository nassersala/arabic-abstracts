# Section 5: Recovery Algorithm Overview
## القسم 5: نظرة عامة على خوارزمية الاسترداد

**Section:** recovery-algorithm
**Translation Quality:** 0.89
**Glossary Terms Used:** recovery, restart, analysis, redo, undo, transaction, log, LSN, checkpoint, dirty page table, transaction table

---

### English Version

When the system restarts after a crash, ARIES performs recovery in three sequential passes:

1. **Analysis Pass**: Reads the log forward from the last checkpoint to determine:
   - Which transactions were active at the time of the crash
   - Which pages might have been dirty (modified but not written to disk)
   - The starting point for the redo pass

2. **Redo Pass**: Reads the log forward from the earliest update that might not have been written to disk, and reapplies all logged updates. This reconstructs the database state as it existed at the time of the crash, following the principle of "repeating history."

3. **Undo Pass**: Reads the log backward to undo the updates of all transactions that were active at the time of the crash. This removes the effects of incomplete transactions.

## 5.1 Recovery Goals

The recovery algorithm must ensure:

- **Atomicity**: Uncommitted transactions have no effects on the database
- **Durability**: Committed transactions' effects persist
- **Efficiency**: Recovery completes as quickly as possible to minimize downtime
- **Correctness**: Recovery works correctly regardless of when the crash occurred
- **Idempotency**: Recovery can be interrupted and restarted without problems

## 5.2 Key Data Structures

During recovery, ARIES maintains:

**Transaction Table**: Rebuilt during the analysis pass. For each transaction that was active at the crash:
- TransID: Transaction identifier
- LastLSN: LSN of the transaction's most recent log record
- UndoNxtLSN: LSN of the next log record to undo

**Dirty Page Table (DPT)**: Rebuilt during the analysis pass. For each page that might have been dirty at the crash:
- PageID: Page identifier
- RecLSN: LSN of the first log record that dirtied this page

These tables allow ARIES to determine precisely which updates need to be redone and which transactions need to be undone.

## 5.3 Restart Process

When the system restarts after a crash:

```
Procedure Restart():
    // Phase 1: Analysis
    (TransTable, DirtyPageTable, RedoLSN) = AnalysisPass()

    // Phase 2: Redo
    RedoPass(RedoLSN, DirtyPageTable)

    // Phase 3: Undo
    UndoPass(TransTable)

    // Recovery complete
    Write checkpoint
    Normal processing resumes
```

## 5.4 Repeating History

A key principle of ARIES is **repeating history** during the redo pass. Rather than trying to determine which updates have been applied and which haven't, ARIES redoes all updates in the log, regardless of whether they were written to disk before the crash.

This approach:
- **Simplifies recovery logic**: No need for complex checks of what's on disk
- **Handles all cases uniformly**: Works correctly whether pages were written early, late, or not at all
- **Enables subsequent undo**: After redo, the database is in exactly the state it was at the crash, so undo can proceed using the same logic as normal transaction rollback

## 5.5 Using LSNs for Redo Avoidance

While ARIES redoes all logged updates, it uses **PageLSN** to avoid unnecessary work:

```
To redo an update with LSN:
    Fetch page from disk
    if page.PageLSN >= LSN:
        // Update already on disk, skip redo
        return
    else:
        // Apply redo
        ApplyUpdate(page, redo_info)
        page.PageLSN = LSN
        Write page to disk (eventually)
```

This optimization is crucial for performance - it allows redo to scan the entire log quickly without actually reapplying updates that have already been written to disk.

## 5.6 Using CLRs for Undo Idempotency

During normal transaction rollback or recovery undo, **Compensation Log Records (CLRs)** ensure idempotent undo:

- Each undo action is logged as a CLR
- CLRs are never undone (they are redo-only)
- The UndoNxtLSN field in each CLR points to the next record to undo, effectively skipping records that have already been compensated

If recovery is interrupted during the undo pass and restarted:
- The analysis pass discovers partially undone transactions
- The redo pass reapplies the CLRs (redoing the partial undo)
- The undo pass continues from where it left off

This makes recovery completely restartable and idempotent.

## 5.7 Recovery Example

Consider a simple example:

**Before crash:**
- Transaction T1: Committed (wrote log records L1, L2, COMMIT)
- Transaction T2: Active (wrote log records L3, L4)
- Some pages written to disk, some not

**After crash:**

**Analysis Pass:**
- Reads log from checkpoint
- Determines T1 was committed, T2 was active
- Builds dirty page table showing which pages need redo

**Redo Pass:**
- Redoes L1, L2 (T1's updates) if not already on disk
- Redoes L3, L4 (T2's updates) if not already on disk
- Database now reflects all logged updates

**Undo Pass:**
- Undoes L4, L3 (T2's updates in reverse order)
- Writes CLRs for each undo
- T2's effects are removed

**Result:**
- T1's effects are in the database (durability)
- T2's effects are removed (atomicity)
- Database is consistent

The following sections describe each pass in detail.

---

### النسخة العربية

عندما يعيد النظام التشغيل بعد التعطل، تنفذ ARIES الاسترداد في ثلاث مراحل تسلسلية:

1. **مرحلة التحليل**: تقرأ السجل إلى الأمام من آخر نقطة تحقق لتحديد:
   - المعاملات التي كانت نشطة وقت التعطل
   - الصفحات التي ربما كانت معدلة (تم تعديلها ولكن لم تُكتب على القرص)
   - نقطة البداية لمرحلة الإعادة

2. **مرحلة الإعادة**: تقرأ السجل إلى الأمام من أقدم تحديث قد لا يكون قد كُتب على القرص، وتعيد تطبيق جميع التحديثات المسجلة. هذا يعيد بناء حالة قاعدة البيانات كما كانت موجودة وقت التعطل، باتباع مبدأ "تكرار التاريخ".

3. **مرحلة التراجع**: تقرأ السجل إلى الوراء للتراجع عن تحديثات جميع المعاملات التي كانت نشطة وقت التعطل. هذا يزيل تأثيرات المعاملات غير المكتملة.

## 5.1 أهداف الاسترداد

يجب أن تضمن خوارزمية الاسترداد:

- **الذرية**: المعاملات غير المثبتة ليس لها تأثيرات على قاعدة البيانات
- **الديمومة**: تأثيرات المعاملات المثبتة تستمر
- **الكفاءة**: يكتمل الاسترداد بأسرع ما يمكن لتقليل وقت التوقف
- **الصحة**: يعمل الاسترداد بشكل صحيح بغض النظر عن وقت التعطل
- **تماثل القوة**: يمكن مقاطعة الاسترداد وإعادة تشغيله دون مشاكل

## 5.2 بنى البيانات الرئيسية

أثناء الاسترداد، تحتفظ ARIES بـ:

**جدول المعاملات**: يُعاد بناؤه أثناء مرحلة التحليل. لكل معاملة كانت نشطة عند التعطل:
- TransID: معرّف المعاملة
- LastLSN: LSN لأحدث سجل للمعاملة
- UndoNxtLSN: LSN لسجل السجل التالي للتراجع عنه

**جدول الصفحات المعدلة (DPT)**: يُعاد بناؤه أثناء مرحلة التحليل. لكل صفحة ربما كانت معدلة عند التعطل:
- PageID: معرّف الصفحة
- RecLSN: LSN لأول سجل جعل هذه الصفحة معدلة

تسمح هذه الجداول لـ ARIES بتحديد التحديثات التي تحتاج إلى إعادة والمعاملات التي تحتاج إلى التراجع بدقة.

## 5.3 عملية إعادة التشغيل

عندما يعيد النظام التشغيل بعد التعطل:

```
إجراء Restart():
    // المرحلة 1: التحليل
    (TransTable, DirtyPageTable, RedoLSN) = AnalysisPass()

    // المرحلة 2: الإعادة
    RedoPass(RedoLSN, DirtyPageTable)

    // المرحلة 3: التراجع
    UndoPass(TransTable)

    // اكتمل الاسترداد
    اكتب نقطة تحقق
    تستأنف المعالجة العادية
```

## 5.4 تكرار التاريخ

مبدأ رئيسي في ARIES هو **تكرار التاريخ** أثناء مرحلة الإعادة. بدلاً من محاولة تحديد التحديثات التي تم تطبيقها والتي لم يتم تطبيقها، تعيد ARIES جميع التحديثات في السجل، بغض النظر عما إذا كانت قد كُتبت على القرص قبل التعطل.

هذا النهج:
- **يبسط منطق الاسترداد**: لا حاجة لفحوصات معقدة لما هو على القرص
- **يتعامل مع جميع الحالات بشكل موحد**: يعمل بشكل صحيح سواء كُتبت الصفحات مبكراً أو متأخراً أو لم تُكتب على الإطلاق
- **يتيح التراجع اللاحق**: بعد الإعادة، تكون قاعدة البيانات في الحالة التي كانت عليها بالضبط عند التعطل، لذا يمكن أن يتم التراجع باستخدام نفس المنطق كتراجع المعاملة العادي

## 5.5 استخدام LSNs لتجنب الإعادة

بينما تعيد ARIES جميع التحديثات المسجلة، فإنها تستخدم **PageLSN** لتجنب العمل غير الضروري:

```
لإعادة تحديث بـ LSN:
    اجلب الصفحة من القرص
    إذا page.PageLSN >= LSN:
        // التحديث موجود بالفعل على القرص، تخطَّ الإعادة
        ارجع
    وإلا:
        // طبق الإعادة
        ApplyUpdate(page, redo_info)
        page.PageLSN = LSN
        اكتب الصفحة على القرص (في النهاية)
```

هذا التحسين أمر بالغ الأهمية للأداء - فهو يسمح للإعادة بمسح السجل بالكامل بسرعة دون إعادة تطبيق التحديثات التي كُتبت بالفعل على القرص.

## 5.6 استخدام CLRs لتماثل قوة التراجع

أثناء تراجع المعاملة العادي أو تراجع الاسترداد، تضمن **سجلات التعويض (CLRs)** تراجعاً متماثل القوة:

- يتم تسجيل كل إجراء تراجع كـ CLR
- لا يتم التراجع عن CLRs أبداً (هي للإعادة فقط)
- يشير حقل UndoNxtLSN في كل CLR إلى السجل التالي للتراجع عنه، متخطياً بشكل فعال السجلات التي تم تعويضها بالفعل

إذا تمت مقاطعة الاسترداد أثناء مرحلة التراجع وأعيد تشغيله:
- تكتشف مرحلة التحليل المعاملات التي تم التراجع عنها جزئياً
- تعيد مرحلة الإعادة تطبيق CLRs (إعادة التراجع الجزئي)
- تستمر مرحلة التراجع من حيث توقفت

هذا يجعل الاسترداد قابلاً لإعادة التشغيل بالكامل ومتماثل القوة.

## 5.7 مثال على الاسترداد

لنفكر في مثال بسيط:

**قبل التعطل:**
- معاملة T1: مثبتة (كتبت سجلات السجل L1, L2, COMMIT)
- معاملة T2: نشطة (كتبت سجلات السجل L3, L4)
- بعض الصفحات كُتبت على القرص، وبعضها لم يُكتب

**بعد التعطل:**

**مرحلة التحليل:**
- تقرأ السجل من نقطة التحقق
- تحدد أن T1 كانت مثبتة، T2 كانت نشطة
- تبني جدول الصفحات المعدلة الذي يوضح الصفحات التي تحتاج إلى إعادة

**مرحلة الإعادة:**
- تعيد L1, L2 (تحديثات T1) إذا لم تكن بالفعل على القرص
- تعيد L3, L4 (تحديثات T2) إذا لم تكن بالفعل على القرص
- قاعدة البيانات الآن تعكس جميع التحديثات المسجلة

**مرحلة التراجع:**
- تتراجع عن L4, L3 (تحديثات T2 بترتيب عكسي)
- تكتب CLRs لكل تراجع
- تُزال تأثيرات T2

**النتيجة:**
- تأثيرات T1 موجودة في قاعدة البيانات (الديمومة)
- تأثيرات T2 مُزالة (الذرية)
- قاعدة البيانات متسقة

تصف الأقسام التالية كل مرحلة بالتفصيل.

---

### Translation Notes

- **Key concepts introduced:** Three-pass recovery, repeating history, redo avoidance with PageLSN, undo idempotency with CLRs
- **Algorithms:** High-level restart procedure
- **Examples:** Simple recovery scenario
- **Technical terms:** Analysis pass, redo pass, undo pass, RedoLSN, RecLSN

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89
