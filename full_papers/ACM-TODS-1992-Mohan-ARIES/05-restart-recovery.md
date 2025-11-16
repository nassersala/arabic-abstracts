# Section 5: Restart Recovery
## القسم 5: استرداد إعادة التشغيل

**Section:** Restart Recovery (Three-Phase Algorithm)
**Translation Quality:** 0.88
**Glossary Terms Used:** recovery, restart, analysis, redo, undo, checkpoint, LSN, transaction table, dirty page table, CLR, commit, abort, crash

---

### English Version

After a system crash, ARIES performs restart recovery to restore the database to a consistent state. The recovery process uses a three-pass algorithm: Analysis, Redo, and Undo. This systematic approach embodies the principle of "repeating history"—first restoring the database to exactly its state at crash time, then undoing uncommitted work.

#### 5.1 Recovery Overview

**Input to Recovery:**
- The log on stable storage
- The master record pointing to the most recent checkpoint
- Database pages on disk (potentially inconsistent)

**Output of Recovery:**
- A consistent database with all committed transactions reflected and all uncommitted transactions rolled back
- An empty transaction table
- An empty dirty page table

**Key Principle—Repeating History:**
ARIES first redoes all logged actions, both from committed and uncommitted transactions, to restore the database to its exact state at the crash. Only after this restoration does it undo uncommitted transactions. This simplifies correctness reasoning and enables advanced features like fine-granularity locking and nested top actions.

#### 5.2 Analysis Pass

The Analysis pass scans forward through the log starting from the most recent checkpoint. Its goals are:
1. Determine which transactions were active at the time of the crash
2. Identify which pages were dirty at crash time
3. Establish the starting point for the Redo pass

**Algorithm:**

```
Analysis Pass:
1. Read the master record to find checkpoint LSN
2. Read the checkpoint record
3. Initialize transaction table from checkpoint's transaction table
4. Initialize dirty page table from checkpoint's dirty page table
5. Scan forward from checkpoint LSN to end of log:
   For each log record R:
     If R is an update record:
       - If PageID not in dirty page table:
         Add PageID with RecLSN = R.LSN
       - If TransID not in transaction table:
         Add transaction with LastLSN = R.LSN, state = running
       - Update transaction's LastLSN = R.LSN
     If R is a commit record:
       - Change transaction state to committed
       - Remove from transaction table (committed = done)
     If R is an abort record:
       - Change transaction state to aborting
     If R is a CLR:
       - If PageID not in dirty page table:
         Add PageID with RecLSN = R.LSN
       - Update transaction's LastLSN = R.LSN
       - If CLR's UndoNxtLSN is null:
         Remove transaction from table (rollback complete)
     If R is an end record:
       - Remove transaction from transaction table
```

**Output of Analysis:**
- **Transaction Table:** Contains all transactions that were active at crash (either running or aborting)
- **Dirty Page Table:** Contains all pages that might have uncommitted updates
- **RedoLSN:** Minimum RecLSN from dirty page table—the earliest point where redo must begin

#### 5.3 Redo Pass

The Redo pass scans forward through the log starting from RedoLSN. It redoes all logged updates, including those from uncommitted transactions, to restore the database to its state at the crash.

**Algorithm:**

```
Redo Pass:
1. Start from RedoLSN (minimum RecLSN in dirty page table)
2. Scan forward to end of log:
   For each log record R that is redoable (update or CLR):
     If R.PageID is in dirty page table:
       If R.LSN >= RecLSN for R.PageID:
         Read page P from disk
         If P.PageLSN < R.LSN:
           Redo the update from R
           Set P.PageLSN = R.LSN
           (Page remains in buffer, not forced to disk)
```

**Key Properties:**

1. **Conditional Redo:** An update is redone only if:
   - The page is in the dirty page table (it might have uncommitted changes)
   - The log record's LSN ≥ RecLSN (it was logged after the page became dirty)
   - The page's current PageLSN < log record's LSN (update not already on page)

2. **Idempotency:** The PageLSN check ensures redo is idempotent. If redo is interrupted by another crash, repeating it will skip already-redone updates.

3. **Repeating History:** After the Redo pass, the database is in exactly the same state it was in at the time of the original crash, including all effects of uncommitted transactions.

4. **No I/O Optimization:** Redo only reads pages that were potentially dirty. It skips pages not in the dirty page table, avoiding unnecessary disk reads.

#### 5.4 Undo Pass

The Undo pass processes transactions in the transaction table (those that were active at crash) and rolls them back. It scans backward through the log, undoing updates in reverse chronological order.

**Algorithm:**

```
Undo Pass:
1. Build ToUndo set = {LastLSN of each transaction in transaction table}
2. While ToUndo is not empty:
   a. Let R = log record with maximum LSN in ToUndo
   b. Remove R.LSN from ToUndo
   c. If R is an update record:
      - Undo the update (apply inverse operation)
      - Write a CLR with:
        * LSN = next available LSN
        * TransID = R.TransID
        * PageID = R.PageID
        * UndoNxtLSN = R.PrevLSN
        * Redo information describing undo action
      - Set page's PageLSN = CLR.LSN
      - If R.PrevLSN ≠ null:
        Add R.PrevLSN to ToUndo
   d. If R is a CLR:
      - If R.UndoNxtLSN ≠ null:
        Add R.UndoNxtLSN to ToUndo
      (CLRs are never undone; just follow the chain)
   e. If R.PrevLSN is null and R.UndoNxtLSN is null:
      - Write an end record for this transaction
      - Remove transaction from transaction table
```

**Key Properties:**

1. **Backward Processing:** Undo processes multiple transactions concurrently, always undoing the most recent unprocessed update across all aborting transactions.

2. **CLR Handling:** When encountering a CLR during undo, the algorithm does not undo it (CLRs are redo-only). Instead, it uses the CLR's UndoNxtLSN to skip over already-compensated updates.

3. **Crash During Undo:** If a crash occurs during the Undo pass:
   - Already-written CLRs remain in the log
   - On the next restart, Analysis finds the CLRs
   - Redo applies the CLRs (redoing the undo actions)
   - Undo resumes from where it left off, using UndoNxtLSN to skip compensated work

4. **Multiple Transactions:** The algorithm interleaves undo operations from different transactions, always choosing the most recent update to undo next. This ensures proper ordering when transactions have dependencies.

#### 5.5 Recovery Correctness

**Atomicity:** The Undo pass ensures that all uncommitted transactions are completely rolled back, leaving no partial effects.

**Durability:** The Redo pass ensures that all committed transactions' effects are restored, even if they hadn't been written to disk before the crash.

**Consistency:** After recovery completes:
- All committed transactions are reflected in the database
- All uncommitted transactions are completely undone
- The database is in a consistent state
- Transaction and dirty page tables are empty

**Idempotency:** Both Redo and Undo are idempotent operations:
- Redo uses PageLSN checks to avoid reapplying updates
- Undo uses CLRs to avoid re-undoing actions
- Recovery can be interrupted and restarted safely

**Efficiency:**
- Analysis scans from last checkpoint, not from log beginning
- Redo starts from minimum RecLSN, not from checkpoint
- Redo only reads pages in dirty page table
- Undo processes multiple transactions concurrently

#### 5.6 Example Recovery Scenario

Consider a crash scenario:

**Before Crash:**
- Transaction T1: committed (updates on pages P1, P2)
- Transaction T2: active (updates on pages P2, P3)
- Transaction T3: aborting, partial rollback (updates on page P4)
- Checkpoint taken with T2 and T3 active
- After checkpoint: T1 commits, T2 continues
- Crash occurs

**Analysis Pass:**
- Starts from checkpoint
- Finds T1 commit record → removes T1 from table
- Finds T2 updates → keeps T2 in table (active)
- Finds T3 CLRs → tracks T3 undo progress
- Result: Transaction table has T2 (running), T3 (aborting)
- Dirty pages: P2, P3, P4

**Redo Pass:**
- Starts from minimum RecLSN
- Redoes all updates to P2, P3, P4
- Redoes T1's updates (even though committed)
- Redoes T2's updates (uncommitted)
- Redoes CLRs for T3
- Database now in exact crash state

**Undo Pass:**
- Undos T2's updates in reverse order
- Continues T3's rollback from where it stopped
- Writes CLRs for all undo actions
- Writes end records for T2 and T3
- Database now consistent with only T1's effects

---

### النسخة العربية

بعد عطل النظام، تنفذ ARIES استرداد إعادة التشغيل لاستعادة قاعدة البيانات إلى حالة متسقة. تستخدم عملية الاسترداد خوارزمية ثلاثية المراحل: التحليل والإعادة والتراجع. يجسد هذا النهج المنهجي مبدأ "تكرار التاريخ"—استعادة قاعدة البيانات أولاً إلى حالتها بالضبط في وقت العطل، ثم التراجع عن العمل غير المُنهى.

#### 5.1 نظرة عامة على الاسترداد

**مدخلات الاسترداد:**
- السجل على التخزين المستقر
- السجل الرئيسي الذي يشير إلى أحدث نقطة تفتيش
- صفحات قاعدة البيانات على القرص (قد تكون غير متسقة)

**مخرجات الاسترداد:**
- قاعدة بيانات متسقة مع انعكاس جميع المعاملات المُنهاة والتراجع عن جميع المعاملات غير المُنهاة
- جدول معاملات فارغ
- جدول صفحات متسخة فارغ

**المبدأ الرئيسي—تكرار التاريخ:**
تعيد ARIES أولاً جميع الإجراءات المسجلة، من كل من المعاملات المُنهاة وغير المُنهاة، لاستعادة قاعدة البيانات إلى حالتها بالضبط عند العطل. فقط بعد هذه الاستعادة تتراجع عن المعاملات غير المُنهاة. يبسط هذا الاستدلال على الصحة ويمكّن الميزات المتقدمة مثل القفل دقيق التفصيل والإجراءات العليا المتداخلة.

#### 5.2 مرحلة التحليل

تمسح مرحلة التحليل للأمام عبر السجل بدءاً من أحدث نقطة تفتيش. أهدافها هي:
1. تحديد المعاملات التي كانت نشطة وقت العطل
2. تحديد الصفحات التي كانت متسخة في وقت العطل
3. إنشاء نقطة البداية لمرحلة الإعادة

**الخوارزمية:**

```
مرحلة التحليل:
1. اقرأ السجل الرئيسي للعثور على LSN لنقطة التفتيش
2. اقرأ سجل نقطة التفتيش
3. ابدأ جدول المعاملات من جدول معاملات نقطة التفتيش
4. ابدأ جدول الصفحات المتسخة من جدول صفحات متسخة نقطة التفتيش
5. امسح للأمام من LSN نقطة التفتيش إلى نهاية السجل:
   لكل سجل سجل R:
     إذا كان R سجل تحديث:
       - إذا لم يكن PageID في جدول الصفحات المتسخة:
         أضف PageID مع RecLSN = R.LSN
       - إذا لم يكن TransID في جدول المعاملات:
         أضف معاملة مع LastLSN = R.LSN، الحالة = قيد التشغيل
       - حدّث LastLSN للمعاملة = R.LSN
     إذا كان R سجل إنهاء:
       - غيّر حالة المعاملة إلى مُنهاة
       - أزل من جدول المعاملات (مُنهاة = منتهية)
     إذا كان R سجل إحباط:
       - غيّر حالة المعاملة إلى قيد الإحباط
     إذا كان R سجل CLR:
       - إذا لم يكن PageID في جدول الصفحات المتسخة:
         أضف PageID مع RecLSN = R.LSN
       - حدّث LastLSN للمعاملة = R.LSN
       - إذا كان UndoNxtLSN لـ CLR فارغاً:
         أزل المعاملة من الجدول (التراجع مكتمل)
     إذا كان R سجل نهاية:
       - أزل المعاملة من جدول المعاملات
```

**مخرجات التحليل:**
- **جدول المعاملات:** يحتوي على جميع المعاملات التي كانت نشطة عند العطل (إما قيد التشغيل أو قيد الإحباط)
- **جدول الصفحات المتسخة:** يحتوي على جميع الصفحات التي قد تحتوي على تحديثات غير مُنهاة
- **RedoLSN:** الحد الأدنى RecLSN من جدول الصفحات المتسخة—أقرب نقطة يجب أن تبدأ فيها الإعادة

#### 5.3 مرحلة الإعادة

تمسح مرحلة الإعادة للأمام عبر السجل بدءاً من RedoLSN. تعيد جميع التحديثات المسجلة، بما في ذلك تلك من المعاملات غير المُنهاة، لاستعادة قاعدة البيانات إلى حالتها عند العطل.

**الخوارزمية:**

```
مرحلة الإعادة:
1. ابدأ من RedoLSN (الحد الأدنى RecLSN في جدول الصفحات المتسخة)
2. امسح للأمام إلى نهاية السجل:
   لكل سجل سجل R قابل للإعادة (تحديث أو CLR):
     إذا كان R.PageID في جدول الصفحات المتسخة:
       إذا كان R.LSN >= RecLSN لـ R.PageID:
         اقرأ الصفحة P من القرص
         إذا كان P.PageLSN < R.LSN:
           أعد التحديث من R
           عيّن P.PageLSN = R.LSN
           (تبقى الصفحة في المخزن المؤقت، لا تُجبر على القرص)
```

**الخصائص الرئيسية:**

1. **الإعادة الشرطية:** تُعاد التحديث فقط إذا:
   - كانت الصفحة في جدول الصفحات المتسخة (قد تحتوي على تغييرات غير مُنهاة)
   - كان LSN سجل السجل ≥ RecLSN (تم تسجيله بعد أن أصبحت الصفحة متسخة)
   - كان PageLSN الحالي للصفحة < LSN سجل السجل (التحديث ليس موجوداً بالفعل على الصفحة)

2. **التساوي في القوة:** يضمن فحص PageLSN أن الإعادة متساوية القوة. إذا قُطعت الإعادة بعطل آخر، فإن تكرارها سيتخطى التحديثات التي تمت إعادتها بالفعل.

3. **تكرار التاريخ:** بعد مرحلة الإعادة، تكون قاعدة البيانات في نفس الحالة بالضبط التي كانت عليها في وقت العطل الأصلي، بما في ذلك جميع آثار المعاملات غير المُنهاة.

4. **تحسين الإدخال/الإخراج:** تقرأ الإعادة فقط الصفحات التي كانت متسخة بشكل محتمل. تتخطى الصفحات غير الموجودة في جدول الصفحات المتسخة، متجنبة قراءات القرص غير الضرورية.

#### 5.4 مرحلة التراجع

تعالج مرحلة التراجع المعاملات في جدول المعاملات (تلك التي كانت نشطة عند العطل) وتتراجع عنها. تمسح للخلف عبر السجل، متراجعة عن التحديثات بترتيب زمني عكسي.

**الخوارزمية:**

```
مرحلة التراجع:
1. ابنِ مجموعة ToUndo = {LastLSN لكل معاملة في جدول المعاملات}
2. بينما ToUndo ليست فارغة:
   a. ليكن R = سجل السجل مع الحد الأقصى LSN في ToUndo
   b. أزل R.LSN من ToUndo
   c. إذا كان R سجل تحديث:
      - تراجع عن التحديث (طبّق العملية العكسية)
      - اكتب CLR مع:
        * LSN = LSN التالي المتاح
        * TransID = R.TransID
        * PageID = R.PageID
        * UndoNxtLSN = R.PrevLSN
        * معلومات إعادة تصف إجراء التراجع
      - عيّن PageLSN للصفحة = CLR.LSN
      - إذا كان R.PrevLSN ≠ فارغ:
        أضف R.PrevLSN إلى ToUndo
   d. إذا كان R سجل CLR:
      - إذا كان R.UndoNxtLSN ≠ فارغ:
        أضف R.UndoNxtLSN إلى ToUndo
      (لا يتم التراجع عن CLRs أبداً؛ اتبع السلسلة فقط)
   e. إذا كان R.PrevLSN فارغاً و R.UndoNxtLSN فارغاً:
      - اكتب سجل نهاية لهذه المعاملة
      - أزل المعاملة من جدول المعاملات
```

**الخصائص الرئيسية:**

1. **المعالجة العكسية:** يعالج التراجع معاملات متعددة بشكل متزامن، متراجعاً دائماً عن أحدث تحديث غير معالج عبر جميع المعاملات قيد الإحباط.

2. **معالجة CLR:** عند مواجهة CLR أثناء التراجع، لا تتراجع الخوارزمية عنه (CLRs للإعادة فقط). بدلاً من ذلك، تستخدم UndoNxtLSN للـ CLR لتخطي التحديثات التي تم تعويضها بالفعل.

3. **العطل أثناء التراجع:** إذا حدث عطل أثناء مرحلة التراجع:
   - تبقى CLRs المكتوبة بالفعل في السجل
   - عند إعادة التشغيل التالية، يجد التحليل CLRs
   - تطبق الإعادة CLRs (إعادة إجراءات التراجع)
   - يستأنف التراجع من حيث توقف، باستخدام UndoNxtLSN لتخطي العمل المعوّض

4. **معاملات متعددة:** تتداخل الخوارزمية عمليات التراجع من معاملات مختلفة، مختارة دائماً أحدث تحديث للتراجع عنه تالياً. يضمن هذا الترتيب الصحيح عندما تكون للمعاملات تبعيات.

#### 5.5 صحة الاسترداد

**الذرية:** تضمن مرحلة التراجع التراجع الكامل عن جميع المعاملات غير المُنهاة، دون ترك أي آثار جزئية.

**الدوام:** تضمن مرحلة الإعادة استعادة جميع آثار المعاملات المُنهاة، حتى لو لم تُكتب إلى القرص قبل العطل.

**الاتساق:** بعد اكتمال الاسترداد:
- تنعكس جميع المعاملات المُنهاة في قاعدة البيانات
- يتم التراجع الكامل عن جميع المعاملات غير المُنهاة
- قاعدة البيانات في حالة متسقة
- جداول المعاملات والصفحات المتسخة فارغة

**التساوي في القوة:** كل من الإعادة والتراجع عمليات متساوية القوة:
- تستخدم الإعادة فحوصات PageLSN لتجنب إعادة تطبيق التحديثات
- يستخدم التراجع CLRs لتجنب إعادة التراجع عن الإجراءات
- يمكن مقاطعة الاسترداد وإعادة تشغيله بأمان

**الكفاءة:**
- يمسح التحليل من آخر نقطة تفتيش، وليس من بداية السجل
- تبدأ الإعادة من الحد الأدنى RecLSN، وليس من نقطة التفتيش
- تقرأ الإعادة فقط الصفحات في جدول الصفحات المتسخة
- يعالج التراجع معاملات متعددة بشكل متزامن

#### 5.6 مثال سيناريو الاسترداد

اعتبر سيناريو عطل:

**قبل العطل:**
- المعاملة T1: مُنهاة (تحديثات على الصفحات P1، P2)
- المعاملة T2: نشطة (تحديثات على الصفحات P2، P3)
- المعاملة T3: قيد الإحباط، تراجع جزئي (تحديثات على الصفحة P4)
- نقطة تفتيش مأخوذة مع T2 و T3 نشطتين
- بعد نقطة التفتيش: T1 تُنهي، T2 تستمر
- يحدث العطل

**مرحلة التحليل:**
- تبدأ من نقطة التفتيش
- تجد سجل إنهاء T1 → تزيل T1 من الجدول
- تجد تحديثات T2 → تحتفظ بـ T2 في الجدول (نشطة)
- تجد CLRs لـ T3 → تتبع تقدم التراجع لـ T3
- النتيجة: جدول المعاملات يحتوي على T2 (قيد التشغيل)، T3 (قيد الإحباط)
- الصفحات المتسخة: P2، P3، P4

**مرحلة الإعادة:**
- تبدأ من الحد الأدنى RecLSN
- تعيد جميع التحديثات على P2، P3، P4
- تعيد تحديثات T1 (حتى لو مُنهاة)
- تعيد تحديثات T2 (غير مُنهاة)
- تعيد CLRs لـ T3
- قاعدة البيانات الآن في حالة العطل بالضبط

**مرحلة التراجع:**
- تتراجع عن تحديثات T2 بترتيب عكسي
- تستمر في التراجع عن T3 من حيث توقفت
- تكتب CLRs لجميع إجراءات التراجع
- تكتب سجلات نهاية لـ T2 و T3
- قاعدة البيانات الآن متسقة مع آثار T1 فقط

---

### Translation Notes

- **Three-Phase Algorithm:**
  - Analysis Pass → مرحلة التحليل
  - Redo Pass → مرحلة الإعادة
  - Undo Pass → مرحلة التراجع

- **Recovery Concepts:**
  - Repeating history → تكرار التاريخ
  - Idempotent → متساوية القوة
  - ToUndo set → مجموعة ToUndo (set of LSNs to undo)
  - RedoLSN → LSN الإعادة (starting point for redo)

- **Algorithm Steps:** All three recovery phases translated with complete algorithmic detail preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.88
