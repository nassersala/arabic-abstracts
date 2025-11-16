# Glossary Additions from ARIES Translation

## New Database Recovery Terms to Add to translations/glossary.md

| English | Arabic | Confidence | Usage Count | Notes |
|---------|--------|------------|-------------|-------|
| ARIES | ARIES | 1.0 | 15 | Algorithm for Recovery and Isolation Exploiting Semantics |
| Write-Ahead Logging (WAL) | التسجيل المسبق للكتابة | 0.95 | 12 | Core recovery protocol |
| Log Sequence Number (LSN) | رقم تسلسل السجل | 0.95 | 20 | Monotonically increasing log identifier |
| Compensation Log Record (CLR) | سجل التعويض | 0.95 | 15 | Redo-only log record for undo operations |
| No-Force policy | سياسة عدم الإجبار | 0.90 | 8 | Pages not forced to disk at commit |
| Steal policy | سياسة السرقة | 0.90 | 8 | Uncommitted pages can be written to disk |
| PageLSN | رقم تسلسل سجل الصفحة | 0.95 | 10 | LSN of most recent update on page |
| RecLSN | رقم تسلسل سجل الاسترداد | 0.90 | 8 | LSN when page first became dirty |
| UndoNxtLSN | رقم تسلسل التراجع التالي | 0.90 | 8 | Next LSN to process during undo |
| Dirty page | صفحة متسخة | 0.95 | 12 | Modified page not yet written to disk |
| Dirty page table | جدول الصفحات المتسخة | 0.95 | 10 | Tracks dirty pages in buffer pool |
| Transaction table | جدول المعاملات | 0.95 | 10 | Tracks active transactions |
| Fuzzy checkpoint | نقطة تفتيش ضبابية | 0.90 | 8 | Checkpoint without quiescing system |
| Sharp checkpoint | نقطة تفتيش حادة | 0.85 | 3 | Checkpoint requiring system quiesce |
| Repeating history | تكرار التاريخ | 0.90 | 6 | ARIES principle of redoing all logged actions |
| Analysis pass | مرحلة التحليل | 0.95 | 8 | First recovery phase |
| Redo pass | مرحلة الإعادة | 0.95 | 8 | Second recovery phase |
| Undo pass | مرحلة التراجع | 0.95 | 8 | Third recovery phase |
| Nested top action | إجراء علوي متداخل | 0.85 | 6 | Operation not undone if transaction aborts |
| Dummy CLR | CLR وهمي | 0.85 | 4 | CLR with UndoNxtLSN but no undo info |
| Savepoint | نقطة حفظ | 0.95 | 5 | Point for partial transaction rollback |
| Buffer pool | مجمع المخازن المؤقتة | 0.95 | 10 | In-memory cache of disk pages |
| Stable storage | التخزين المستقر | 0.95 | 8 | Persistent storage surviving failures |
| Archive log | سجل الأرشيف | 0.95 | 5 | Historical log for media recovery |
| Image copy | نسخة صورة | 0.90 | 4 | Backup copy of database |
| Fuzzy dump | تفريغ ضبابي | 0.85 | 3 | Backup taken while system running |
| Media recovery | استرداد الوسائط | 0.95 | 6 | Recovery from disk failures |
| Physical logging | التسجيل الفيزيائي | 0.90 | 5 | Logging before/after images |
| Logical logging | التسجيل المنطقي | 0.90 | 5 | Logging operations and parameters |
| Operation logging | تسجيل العمليات | 0.90 | 5 | Logging logical operations |
| Physiological logging | التسجيل الفسيولوجي | 0.85 | 3 | Page-oriented physical logging |
| Idempotent | متساوي القوة | 0.85 | 8 | Operation safe to repeat |
| flushedLSN | LSN المدفوق | 0.85 | 5 | LSN through which log is on stable storage |
| RedoLSN | LSN الإعادة | 0.85 | 4 | Starting point for redo pass |
| ToUndo set | مجموعة ToUndo | 0.85 | 4 | Set of LSNs to be undone |
| Latch | مزلاج | 0.90 | 6 | Short-term physical page lock |
| Lock granularity | دقة القفل | 0.90 | 5 | Level of locking (page, record, etc.) |
| Fine-granularity locking | القفل دقيق التفصيل | 0.95 | 8 | Record-level or key-level locking |
| Before image | صورة قبل | 0.95 | 6 | Original value before update |
| After image | صورة بعد | 0.95 | 6 | New value after update |
| Master record | السجل الرئيسي | 0.90 | 4 | Pointer to last checkpoint on stable storage |
| Victim page | صفحة ضحية | 0.85 | 3 | Page selected for buffer eviction |
| Crash recovery | استرداد العطل | 0.95 | 6 | Recovery from system crash |
| Restart recovery | استرداد إعادة التشغيل | 0.95 | 8 | Recovery during system restart |

## Updated Terms (Already in Glossary)

These terms were already in the glossary but usage count should be incremented:

- transaction (معاملة) - add 30 uses
- database (قاعدة البيانات) - add 20 uses
- recovery (استرداد) - add 25 uses
- commit (إنهاء/التزام) - add 15 uses
- abort (إحباط) - add 12 uses
- rollback (تراجع) - add 15 uses
- checkpoint (نقطة تفتيش) - add 10 uses
- log (سجل) - add 20 uses
- page (صفحة) - add 25 uses
- buffer (مخزن مؤقت) - add 15 uses
- atomicity (ذرية) - add 8 uses
- durability (دوام) - add 6 uses
- consistency (اتساق) - add 6 uses
- isolation (عزل) - add 6 uses
- concurrency (تزامن) - add 10 uses

## Term Notes

- **ARIES** is kept in English as it's an acronym that's universally recognized
- **LSN** derivatives (PageLSN, RecLSN, UndoNxtLSN, flushedLSN, RedoLSN) all follow the pattern of "رقم تسلسل سجل" + descriptor
- **Idempotent** (متساوي القوة) literally "equal in strength" - conveys the meaning that operations can be repeated without changing the outcome
- **Latch vs Lock** distinction is important: latches are short-term physical locks, while locks are transaction-duration logical locks
- **Fuzzy vs Sharp** for checkpoints: fuzzy (ضبابية) allows concurrent activity, sharp (حادة) requires quiescing
- **Force/No-Force** and **Steal/No-Steal** are buffer management policies that are fundamental to ARIES
