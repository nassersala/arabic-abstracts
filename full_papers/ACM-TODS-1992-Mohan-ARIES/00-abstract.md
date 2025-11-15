# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.94
**Glossary Terms Used:** algorithm, database, transaction, recovery, rollback, write-ahead logging, Log Sequence Number (LSN), Compensation Log Record (CLR), redo, undo, restart, system failure, fine-granularity locking, performance

---

### English Version

In this paper, we present ARIES (Algorithm for Recovery and Isolation Exploiting Semantics), a recovery method based on the write-ahead logging protocol. ARIES supports fine-granularity locking and provides efficient support for transaction rollback. The recovery method uses a novel concept of Log Sequence Numbers (LSNs) to track the state of pages and log records. During restart after a system failure, ARIES uses a three-pass algorithm: Analysis pass to determine the state of the transactions and pages at the time of failure, Redo pass to restore the database to its state at the time of failure, and Undo pass to rollback the incomplete transactions. ARIES introduces Compensation Log Records (CLRs) which are redo-only log records that describe actions taken during transaction rollback and recovery. The method follows a No-Force, Steal policy allowing maximum performance flexibility. ARIES is applicable not only to database management systems but also to persistent object-oriented languages, recoverable file systems and transaction-based operating systems. ARIES has been implemented, to varying degrees, in IBM's OS/2 Extended Edition Database Manager, DB2, IMS, Workstation Data Save Facility/VM, Starburst and QuickSilver, and in the University of Wisconsin's EXODUS and Gamma database machine.

---

### النسخة العربية

في هذا البحث، نقدم ARIES (خوارزمية الاسترداد والعزل باستغلال الدلالات)، وهي طريقة استرداد تعتمد على بروتوكول التسجيل المسبق للكتابة. تدعم ARIES القفل دقيق التفصيل وتوفر دعماً فعالاً لتراجع المعاملات. تستخدم طريقة الاسترداد مفهوماً مبتكراً لأرقام تسلسل السجل (LSNs) لتتبع حالة الصفحات وسجلات السجل. أثناء إعادة التشغيل بعد فشل النظام، تستخدم ARIES خوارزمية ثلاثية المراحل: مرحلة التحليل لتحديد حالة المعاملات والصفحات وقت الفشل، ومرحلة الإعادة لاستعادة قاعدة البيانات إلى حالتها وقت الفشل، ومرحلة التراجع لإلغاء المعاملات غير المكتملة. تقدم ARIES سجلات التعويض (CLRs)، وهي سجلات للإعادة فقط تصف الإجراءات المتخذة أثناء تراجع المعاملات والاسترداد. تتبع الطريقة سياسة عدم الإجبار والسرقة مما يسمح بمرونة أداء قصوى. تنطبق ARIES ليس فقط على أنظمة إدارة قواعد البيانات ولكن أيضاً على اللغات الكائنية الدائمة وأنظمة الملفات القابلة للاسترداد وأنظمة التشغيل القائمة على المعاملات. تم تطبيق ARIES بدرجات متفاوتة في مدير قاعدة بيانات OS/2 Extended Edition من IBM، وDB2، وIMS، وWorkstation Data Save Facility/VM، وStarburst، وQuickSilver، وفي آلة قاعدة البيانات EXODUS وGamma التابعة لجامعة ويسكونسن.

---

### Translation Notes

- **Key concepts introduced:** ARIES, Write-Ahead Logging (WAL), Log Sequence Numbers (LSNs), Compensation Log Records (CLRs), Three-pass recovery algorithm (Analysis, Redo, Undo), No-Force/Steal policy
- **Technical terms:** Fine-granularity locking, transaction rollback, system failure, recovery algorithm
- **Implementation references:** IBM DB2, IMS, OS/2, Starburst, QuickSilver, EXODUS, Gamma

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.93
- Glossary consistency: 0.94
- **Overall section score:** 0.94
