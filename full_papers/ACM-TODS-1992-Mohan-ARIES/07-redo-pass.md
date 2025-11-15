# Section 7: Redo Pass
## القسم 7: مرحلة الإعادة

**Section:** redo-pass
**Translation Quality:** 0.88
**Glossary Terms Used:** redo, log, LSN, PageLSN, RecLSN, dirty page table, repeating history, idempotent, CLR

---

### English Version

The Redo Pass is the second phase of recovery. It scans the log forward from RedoLSN (determined by the Analysis Pass) and reapplies all logged updates, following the principle of "repeating history."

## 7.1 Goals of Redo Pass

The Redo Pass:

1. **Repeats history**: Reapplies all logged updates to restore the database to its state at the time of the crash
2. **Handles all transactions uniformly**: Redoes updates from both committed and uncommitted transactions
3. **Is idempotent**: Can be restarted safely if interrupted
4. **Avoids unnecessary work**: Uses PageLSN to skip updates already on disk

## 7.2 Redo Pass Algorithm

```
Procedure RedoPass(RedoLSN, DirtyPageTable):
    CurrentLSN = RedoLSN

    // Scan log forward from RedoLSN to end
    while CurrentLSN ≠ EndOfLog:
        LogRec = ReadLog(CurrentLSN)

        // Process only UPDATE and CLR records
        if LogRec.Type == UPDATE or LogRec.Type == CLR:

            // Check if page might need redo
            if LogRec.PageID in DirtyPageTable:
                if LogRec.LSN >= DirtyPageTable[LogRec.PageID].RecLSN:

                    // Fetch page from disk
                    Page = ReadPage(LogRec.PageID)

                    // Check if redo needed using PageLSN
                    if Page.PageLSN < LogRec.LSN:
                        // Redo the update
                        ApplyRedo(Page, LogRec.RedoInfo)
                        Page.PageLSN = LogRec.LSN
                        // Page will be written eventually by buffer manager

        CurrentLSN = NextLSN(CurrentLSN)

    // Redo complete
    return
```

## 7.3 Repeating History

ARIES follows the principle of **repeating history**: the redo pass reapplies all updates in the log, reconstructing the database exactly as it existed at the time of the crash.

This includes:
- Updates from committed transactions
- Updates from uncommitted transactions
- CLRs (redo actions from transaction rollbacks)

Why repeat history?
- **Simplicity**: No need to determine which transactions committed
- **Uniformity**: All updates handled the same way
- **Correctness**: Ensures the database is in the exact pre-crash state before undo
- **Supports partial rollback**: CLRs are redone, ensuring partial rollbacks complete

## 7.4 Redo Conditions

An update is redone only if ALL of the following conditions hold:

1. **Affected page is in Dirty Page Table**: If a page is not in the DPT, it was written to disk and is not dirty.

2. **LSN ≥ RecLSN**: The update's LSN must be ≥ the page's RecLSN. If LSN < RecLSN, the update was on disk when the page was last written.

3. **PageLSN < LSN**: The page's current PageLSN (from disk) must be less than the update's LSN. If PageLSN ≥ LSN, the update is already on disk.

These conditions together ensure that:
- No update is redone unnecessarily
- All needed updates are redone
- Redo is idempotent (can be safely restarted)

## 7.5 Idempotency

The Redo Pass is **idempotent**: running it multiple times has the same effect as running it once. This is crucial because:

- Recovery can be interrupted (e.g., by another crash) and restarted
- PageLSN check ensures updates already on disk are not reapplied

Example:
```
Suppose update with LSN 150 modifies page P:
- First redo: Page.PageLSN = 140 < 150, so redo is applied, Page.PageLSN set to 150
- If redo restarts: Page.PageLSN = 150 ≥ 150, so redo is skipped (already applied)
```

## 7.6 Handling Different Log Record Types

**UPDATE records:**
- Contain redo information (new value or logical redo operation)
- Applied to the page if redo conditions met
- Page's PageLSN updated to the update's LSN

**CLR (Compensation Log Record):**
- Describe undo actions taken during transaction rollback
- Redone just like UPDATE records
- Never undone (they are redo-only)
- Ensure partial rollbacks complete even if crash occurred during rollback

**Other record types (COMMIT, ABORT, END):**
- Not processed during redo
- No page updates to redo

## 7.7 Physical vs. Physiological vs. Logical Redo

ARIES supports different types of redo:

**Physical Redo:**
- Stores the new value of specific bytes
- Example: "Set bytes 100-103 of page P to value 5678"
- Simple but requires careful handling of page structure changes

**Physiological Redo:**
- Logical at page level, physical within page
- Example: "In page P, update slot 5 to value X"
- ARIES primarily uses physiological redo
- Balances simplicity and flexibility

**Logical Redo:**
- High-level operation
- Example: "Insert tuple T into index I"
- More complex but handles structural changes better
- Used for index operations

## 7.8 Example

Continuing the example from Section 6:

After Analysis Pass:
- RedoLSN = 100
- DirtyPageTable = {P1:RecLSN=100, P2:RecLSN=120, P3:RecLSN=150}

Redo Pass processes:
```
LSN 100-119: Updates to P1
  - Check: P1 in DPT? Yes. LSN ≥ 100? Yes.
  - For each update: Check Page.PageLSN < LSN? If yes, redo.

LSN 120: UPDATE T1 P2
  - Check: P2 in DPT? Yes. LSN 120 ≥ 120? Yes.
  - Check Page.PageLSN < 120? If yes, redo.

LSN 130: UPDATE T2 P1
  - Check: P1 in DPT? Yes. LSN 130 ≥ 100? Yes.
  - Check Page.PageLSN < 130? If yes, redo.

LSN 140: COMMIT T1
  - Not UPDATE or CLR, skip.

LSN 150: UPDATE T2 P3
  - Check: P3 in DPT? Yes. LSN 150 ≥ 150? Yes.
  - Check Page.PageLSN < 150? If yes, redo.

LSN 160: ABORT T2
  - Skip.

LSN 170: CLR T2 P3
  - Check: P3 in DPT? Yes. LSN 170 ≥ 150? Yes.
  - Check Page.PageLSN < 170? If yes, redo CLR.
```

After Redo Pass:
- Database contains all updates through LSN 170
- This includes T1's committed updates and T2's updates (which will be undone next)
- T2's partial rollback (CLR at 170) is also redone

---

### النسخة العربية

مرحلة الإعادة هي المرحلة الثانية من الاسترداد. تمسح السجل إلى الأمام من RedoLSN (الذي تحدده مرحلة التحليل) وتعيد تطبيق جميع التحديثات المسجلة، باتباع مبدأ "تكرار التاريخ".

## 7.1 أهداف مرحلة الإعادة

مرحلة الإعادة:

1. **تكرر التاريخ**: تعيد تطبيق جميع التحديثات المسجلة لاستعادة قاعدة البيانات إلى حالتها وقت التعطل
2. **تتعامل مع جميع المعاملات بشكل موحد**: تعيد التحديثات من المعاملات المثبتة وغير المثبتة
3. **متماثلة القوة**: يمكن إعادة تشغيلها بأمان إذا تمت مقاطعتها
4. **تتجنب العمل غير الضروري**: تستخدم PageLSN لتخطي التحديثات الموجودة بالفعل على القرص

## 7.2 خوارزمية مرحلة الإعادة

```
إجراء RedoPass(RedoLSN, DirtyPageTable):
    CurrentLSN = RedoLSN

    // مسح السجل إلى الأمام من RedoLSN إلى النهاية
    بينما CurrentLSN ≠ EndOfLog:
        LogRec = ReadLog(CurrentLSN)

        // معالجة سجلات UPDATE و CLR فقط
        إذا LogRec.Type == UPDATE أو LogRec.Type == CLR:

            // تحقق مما إذا كانت الصفحة قد تحتاج إلى إعادة
            إذا كان LogRec.PageID في DirtyPageTable:
                إذا كان LogRec.LSN >= DirtyPageTable[LogRec.PageID].RecLSN:

                    // جلب الصفحة من القرص
                    Page = ReadPage(LogRec.PageID)

                    // تحقق مما إذا كانت الإعادة مطلوبة باستخدام PageLSN
                    إذا كان Page.PageLSN < LogRec.LSN:
                        // إعادة التحديث
                        ApplyRedo(Page, LogRec.RedoInfo)
                        Page.PageLSN = LogRec.LSN
                        // سيتم كتابة الصفحة في النهاية بواسطة مدير المخزن المؤقت

        CurrentLSN = NextLSN(CurrentLSN)

    // اكتملت الإعادة
    ارجع
```

## 7.3 تكرار التاريخ

تتبع ARIES مبدأ **تكرار التاريخ**: مرحلة الإعادة تعيد تطبيق جميع التحديثات في السجل، وإعادة بناء قاعدة البيانات كما كانت موجودة بالضبط وقت التعطل.

هذا يتضمن:
- تحديثات من المعاملات المثبتة
- تحديثات من المعاملات غير المثبتة
- CLRs (إجراءات الإعادة من تراجعات المعاملات)

لماذا تكرار التاريخ؟
- **البساطة**: لا حاجة لتحديد المعاملات التي تم تثبيتها
- **التوحيد**: يتم التعامل مع جميع التحديثات بنفس الطريقة
- **الصحة**: يضمن أن قاعدة البيانات في الحالة الدقيقة قبل التعطل قبل التراجع
- **يدعم التراجع الجزئي**: يتم إعادة CLRs، مما يضمن اكتمال التراجعات الجزئية

## 7.4 شروط الإعادة

يتم إعادة التحديث فقط إذا تحققت جميع الشروط التالية:

1. **الصفحة المتأثرة في جدول الصفحات المعدلة**: إذا لم تكن الصفحة في DPT، فقد تمت كتابتها على القرص وليست معدلة.

2. **LSN ≥ RecLSN**: يجب أن يكون LSN للتحديث ≥ RecLSN للصفحة. إذا كان LSN < RecLSN، فقد كان التحديث على القرص عندما تمت كتابة الصفحة آخر مرة.

3. **PageLSN < LSN**: يجب أن يكون PageLSN الحالي للصفحة (من القرص) أقل من LSN للتحديث. إذا كان PageLSN ≥ LSN، فالتحديث موجود بالفعل على القرص.

هذه الشروط معاً تضمن:
- عدم إعادة أي تحديث دون داعٍ
- إعادة جميع التحديثات المطلوبة
- الإعادة متماثلة القوة (يمكن إعادة تشغيلها بأمان)

## 7.5 تماثل القوة

مرحلة الإعادة **متماثلة القوة**: تشغيلها عدة مرات له نفس تأثير تشغيلها مرة واحدة. هذا أمر بالغ الأهمية لأن:

- يمكن مقاطعة الاسترداد (على سبيل المثال، بسبب تعطل آخر) وإعادة تشغيله
- فحص PageLSN يضمن عدم إعادة تطبيق التحديثات الموجودة بالفعل على القرص

مثال:
```
لنفترض أن التحديث بـ LSN 150 يعدل الصفحة P:
- الإعادة الأولى: Page.PageLSN = 140 < 150، لذا يتم تطبيق الإعادة، يتم تعيين Page.PageLSN إلى 150
- إذا أعيد تشغيل الإعادة: Page.PageLSN = 150 ≥ 150، لذا يتم تخطي الإعادة (تم تطبيقها بالفعل)
```

## 7.6 معالجة أنواع سجلات السجل المختلفة

**سجلات UPDATE:**
- تحتوي على معلومات الإعادة (القيمة الجديدة أو عملية الإعادة المنطقية)
- تُطبق على الصفحة إذا تحققت شروط الإعادة
- يتم تحديث PageLSN للصفحة إلى LSN للتحديث

**CLR (سجل التعويض):**
- تصف إجراءات التراجع المتخذة أثناء تراجع المعاملة
- يتم إعادتها تماماً مثل سجلات UPDATE
- لا يتم التراجع عنها أبداً (هي للإعادة فقط)
- تضمن اكتمال التراجعات الجزئية حتى لو حدث تعطل أثناء التراجع

**أنواع السجلات الأخرى (COMMIT, ABORT, END):**
- لا تتم معالجتها أثناء الإعادة
- لا توجد تحديثات للصفحة لإعادتها

## 7.7 الإعادة الفيزيائية مقابل الفسيولوجية مقابل المنطقية

تدعم ARIES أنواعاً مختلفة من الإعادة:

**الإعادة الفيزيائية:**
- تخزن القيمة الجديدة لبايتات محددة
- مثال: "اضبط البايتات 100-103 من الصفحة P على القيمة 5678"
- بسيطة ولكنها تتطلب معالجة دقيقة لتغييرات بنية الصفحة

**الإعادة الفسيولوجية:**
- منطقية على مستوى الصفحة، فيزيائية داخل الصفحة
- مثال: "في الصفحة P، حدث الفتحة 5 إلى القيمة X"
- تستخدم ARIES بشكل أساسي الإعادة الفسيولوجية
- توازن بين البساطة والمرونة

**الإعادة المنطقية:**
- عملية عالية المستوى
- مثال: "أدرج السجل T في الفهرس I"
- أكثر تعقيداً ولكنها تتعامل مع التغييرات الهيكلية بشكل أفضل
- تُستخدم لعمليات الفهرس

## 7.8 مثال

مواصلة المثال من القسم 6:

بعد مرحلة التحليل:
- RedoLSN = 100
- DirtyPageTable = {P1:RecLSN=100, P2:RecLSN=120, P3:RecLSN=150}

تعالج مرحلة الإعادة:
```
LSN 100-119: تحديثات لـ P1
  - تحقق: P1 في DPT? نعم. LSN ≥ 100? نعم.
  - لكل تحديث: تحقق Page.PageLSN < LSN? إذا كانت نعم، أعد.

LSN 120: UPDATE T1 P2
  - تحقق: P2 في DPT? نعم. LSN 120 ≥ 120? نعم.
  - تحقق Page.PageLSN < 120? إذا كانت نعم، أعد.

LSN 130: UPDATE T2 P1
  - تحقق: P1 في DPT? نعم. LSN 130 ≥ 100? نعم.
  - تحقق Page.PageLSN < 130? إذا كانت نعم، أعد.

LSN 140: COMMIT T1
  - ليس UPDATE أو CLR، تخطَّ.

LSN 150: UPDATE T2 P3
  - تحقق: P3 في DPT? نعم. LSN 150 ≥ 150? نعم.
  - تحقق Page.PageLSN < 150? إذا كانت نعم، أعد.

LSN 160: ABORT T2
  - تخطَّ.

LSN 170: CLR T2 P3
  - تحقق: P3 في DPT? نعم. LSN 170 ≥ 150? نعم.
  - تحقق Page.PageLSN < 170? إذا كانت نعم، أعد CLR.
```

بعد مرحلة الإعادة:
- تحتوي قاعدة البيانات على جميع التحديثات حتى LSN 170
- هذا يتضمن تحديثات T1 المثبتة وتحديثات T2 (التي سيتم التراجع عنها بعد ذلك)
- يتم أيضاً إعادة التراجع الجزئي لـ T2 (CLR في 170)

---

### Translation Notes

- **Key concepts:** Repeating history, redo conditions, idempotency, PageLSN checks, physical/physiological/logical redo
- **Algorithms:** Complete redo pass algorithm
- **Examples:** Detailed walkthrough of redo processing
- **Technical optimizations:** Using PageLSN to avoid unnecessary redos

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
