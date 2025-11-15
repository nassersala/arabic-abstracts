# Section 10: Nested Top Actions
## القسم 10: الإجراءات العلوية المتداخلة

**Section:** nested-top-actions
**Translation Quality:** 0.85
**Glossary Terms Used:** nested top action, subtransaction, atomic operation, CLR, undo, log

---

### English Version

Nested Top Actions are a mechanism for performing atomic operations within a transaction that should not be undone even if the transaction aborts.

## 10.1 Motivation

Some operations within a transaction should be atomic and permanent, regardless of whether the transaction commits or aborts:

- **Space allocation**: Allocating a new page should not be undone
- **Index page splits**: B-tree node splits should not be undone
- **Sequence number generation**: Generating unique IDs should not be undone

These operations have **external side effects** that cannot be easily reversed, or reversal would cause problems (e.g., space fragmentation, index inconsistency).

## 10.2 Definition

A **Nested Top Action** is a sequence of operations within a transaction that:
1. Forms an atomic unit
2. Is not undone if the containing transaction aborts
3. Has its own undo boundary

The nested top action effectively creates a "mini-transaction" within the larger transaction.

## 10.3 Implementation

Nested top actions are implemented using a special type of CLR called a **dummy CLR**:

```
To perform a nested top action:
1. Record current LastLSN as SaveLSN
2. Perform the nested operations (with logging)
3. Write a dummy CLR:
       LSN = NextLSN()
       Type = CLR
       UndoNxtLSN = SaveLSN  // Skip nested operations during undo
       (no redo information needed)
4. Update LastLSN to dummy CLR's LSN
```

During transaction undo:
- When the dummy CLR is encountered, undo skips to UndoNxtLSN
- The nested operations are not undone

## 10.4 Example: Page Allocation

```
Transaction T1 allocates a new page:

LSN 100: T1 UPDATE (some data modification)
LSN 110: T1 BEGIN_NESTED_TOP_ACTION
LSN 120: T1 UPDATE (modify space map)
LSN 130: T1 UPDATE (initialize new page)
LSN 140: T1 DUMMY_CLR (UndoNxtLSN=100)  // End nested top action
LSN 150: T1 UPDATE (use new page)

If T1 aborts:
- Undo starts at LSN 150
- LSN 150 is undone
- LSN 140 is dummy CLR, skip to UndoNxtLSN=100
- LSNs 120, 130 are NOT undone (page allocation permanent)
- LSN 100 is undone
```

The page allocation (LSNs 120, 130) is not undone, preventing space fragmentation and ensuring allocated pages remain allocated.

## 10.5 Nested Top Actions vs. Subtransactions

Nested top actions differ from subtransactions:

**Subtransactions:**
- Can be independently committed or aborted
- Have their own commit/abort protocols
- More complex implementation

**Nested Top Actions:**
- Simpler - just use CLRs
- Always "commit" (never undone)
- No separate commit protocol
- Lightweight

## 10.6 Use Cases

Common uses of nested top actions:

1. **Storage management**: Page allocation/deallocation
2. **Index operations**: B-tree splits, merges
3. **Sequence generation**: Unique ID generation
4. **Logging operations**: Writing special log records
5. **Resource acquisition**: Locking protocol operations

---

### النسخة العربية

الإجراءات العلوية المتداخلة هي آلية لأداء عمليات ذرية داخل معاملة لا ينبغي التراجع عنها حتى لو تم إلغاء المعاملة.

## 10.1 الدافع

يجب أن تكون بعض العمليات داخل المعاملة ذرية ودائمة، بغض النظر عما إذا كانت المعاملة مثبتة أم ملغاة:

- **تخصيص المساحة**: تخصيص صفحة جديدة لا ينبغي التراجع عنه
- **انقسامات صفحات الفهرس**: انقسامات عقدة شجرة B لا ينبغي التراجع عنها
- **توليد أرقام التسلسل**: توليد معرّفات فريدة لا ينبغي التراجع عنه

هذه العمليات لها **آثار جانبية خارجية** لا يمكن عكسها بسهولة، أو قد يسبب العكس مشاكل (على سبيل المثال، تجزئة المساحة، عدم اتساق الفهرس).

## 10.2 التعريف

**الإجراء العلوي المتداخل** هو تسلسل من العمليات داخل معاملة:
1. يشكل وحدة ذرية
2. لا يتم التراجع عنه إذا تم إلغاء المعاملة المحتوية
3. له حد تراجع خاص به

الإجراء العلوي المتداخل يخلق فعلياً "معاملة صغيرة" داخل المعاملة الأكبر.

## 10.3 التنفيذ

يتم تنفيذ الإجراءات العلوية المتداخلة باستخدام نوع خاص من CLR يسمى **CLR وهمي**:

```
لتنفيذ إجراء علوي متداخل:
1. سجل LastLSN الحالي كـ SaveLSN
2. نفذ العمليات المتداخلة (مع التسجيل)
3. اكتب CLR وهمي:
       LSN = NextLSN()
       Type = CLR
       UndoNxtLSN = SaveLSN  // تخطى العمليات المتداخلة أثناء التراجع
       (لا حاجة لمعلومات الإعادة)
4. حدث LastLSN إلى LSN الخاص بـ CLR الوهمي
```

أثناء تراجع المعاملة:
- عند مواجهة CLR الوهمي، يتخطى التراجع إلى UndoNxtLSN
- لا يتم التراجع عن العمليات المتداخلة

## 10.4 مثال: تخصيص الصفحة

```
المعاملة T1 تخصص صفحة جديدة:

LSN 100: T1 UPDATE (بعض تعديلات البيانات)
LSN 110: T1 BEGIN_NESTED_TOP_ACTION
LSN 120: T1 UPDATE (تعديل خريطة المساحة)
LSN 130: T1 UPDATE (تهيئة الصفحة الجديدة)
LSN 140: T1 DUMMY_CLR (UndoNxtLSN=100)  // إنهاء الإجراء العلوي المتداخل
LSN 150: T1 UPDATE (استخدام الصفحة الجديدة)

إذا تم إلغاء T1:
- يبدأ التراجع من LSN 150
- يتم التراجع عن LSN 150
- LSN 140 هو CLR وهمي، انتقل إلى UndoNxtLSN=100
- LSNs 120, 130 لا يتم التراجع عنها (تخصيص الصفحة دائم)
- يتم التراجع عن LSN 100
```

لا يتم التراجع عن تخصيص الصفحة (LSNs 120, 130)، مما يمنع تجزئة المساحة ويضمن بقاء الصفحات المخصصة مخصصة.

## 10.5 الإجراءات العلوية المتداخلة مقابل المعاملات الفرعية

تختلف الإجراءات العلوية المتداخلة عن المعاملات الفرعية:

**المعاملات الفرعية:**
- يمكن تثبيتها أو إلغاؤها بشكل مستقل
- لها بروتوكولات التثبيت/الإلغاء الخاصة بها
- تنفيذ أكثر تعقيداً

**الإجراءات العلوية المتداخلة:**
- أبسط - تستخدم فقط CLRs
- دائماً "تثبت" (لا يتم التراجع عنها أبداً)
- لا يوجد بروتوكول تثبيت منفصل
- خفيفة الوزن

## 10.6 حالات الاستخدام

الاستخدامات الشائعة للإجراءات العلوية المتداخلة:

1. **إدارة التخزين**: تخصيص/إلغاء تخصيص الصفحة
2. **عمليات الفهرس**: انقسامات ودمج شجرة B
3. **توليد التسلسل**: توليد معرّف فريد
4. **عمليات التسجيل**: كتابة سجلات سجل خاصة
5. **اكتساب الموارد**: عمليات بروتوكول القفل

---

### Translation Notes

- **Key concepts:** Nested top actions, dummy CLRs, atomic operations within transactions, undo boundaries
- **Use cases:** Space allocation, index operations, sequence generation
- **Comparison:** Nested top actions vs. subtransactions
- **Examples:** Page allocation scenario

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.85
