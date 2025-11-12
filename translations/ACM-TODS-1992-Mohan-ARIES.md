# ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging
## ARIES: طريقة استرداد المعاملات الداعمة للقفل دقيق التفصيل والتراجع الجزئي باستخدام التسجيل المسبق للكتابة

**Publication:** ACM Transactions on Database Systems (TODS), Vol. 17, No. 1, March 1992, pp. 94-162
**DOI:** 10.1145/128765.128770
**Authors:** C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, Peter Schwarz
**Year:** 1992
**Translation Quality:** 0.94
**Glossary Terms Used:** algorithm, database, transaction, state, method, performance, implementation, recovery, rollback, write-ahead logging, Log Sequence Number (LSN), Compensation Log Record (CLR), redo, undo, restart, system failure

### English Abstract
In this paper, we present ARIES (Algorithm for Recovery and Isolation Exploiting Semantics), a recovery method based on the write-ahead logging protocol. ARIES supports fine-granularity locking and provides efficient support for transaction rollback. The recovery method uses a novel concept of Log Sequence Numbers (LSNs) to track the state of pages and log records. During restart after a system failure, ARIES uses a three-pass algorithm: Analysis pass to determine the state of the transactions and pages at the time of failure, Redo pass to restore the database to its state at the time of failure, and Undo pass to rollback the incomplete transactions. ARIES introduces Compensation Log Records (CLRs) which are redo-only log records that describe actions taken during transaction rollback and recovery. The method follows a No-Force, Steal policy allowing maximum performance flexibility. ARIES is applicable not only to database management systems but also to persistent object-oriented languages, recoverable file systems and transaction-based operating systems. ARIES has been implemented, to varying degrees, in IBM's OS/2 Extended Edition Database Manager, DB2, IMS, Workstation Data Save Facility/VM, Starburst and QuickSilver, and in the University of Wisconsin's EXODUS and Gamma database machine.

### الملخص العربي
في هذا البحث، نقدم ARIES (خوارزمية الاسترداد والعزل باستغلال الدلالات)، وهي طريقة استرداد تعتمد على بروتوكول التسجيل المسبق للكتابة. تدعم ARIES القفل دقيق التفصيل وتوفر دعماً فعالاً لتراجع المعاملات. تستخدم طريقة الاسترداد مفهوماً مبتكراً لأرقام تسلسل السجل (LSNs) لتتبع حالة الصفحات وسجلات السجل. أثناء إعادة التشغيل بعد فشل النظام، تستخدم ARIES خوارزمية ثلاثية المراحل: مرحلة التحليل لتحديد حالة المعاملات والصفحات وقت الفشل، ومرحلة الإعادة لاستعادة قاعدة البيانات إلى حالتها وقت الفشل، ومرحلة التراجع لإلغاء المعاملات غير المكتملة. تقدم ARIES سجلات التعويض (CLRs)، وهي سجلات للإعادة فقط تصف الإجراءات المتخذة أثناء تراجع المعاملات والاسترداد. تتبع الطريقة سياسة عدم الإجبار والسرقة مما يسمح بمرونة أداء قصوى. تنطبق ARIES ليس فقط على أنظمة إدارة قواعد البيانات ولكن أيضاً على اللغات الكائنية الدائمة وأنظمة الملفات القابلة للاسترداد وأنظمة التشغيل القائمة على المعاملات. تم تطبيق ARIES بدرجات متفاوتة في مدير قاعدة بيانات OS/2 Extended Edition من IBM، وDB2، وIMS، وWorkstation Data Save Facility/VM، وStarburst، وQuickSilver، وفي آلة قاعدة البيانات EXODUS وGamma التابعة لجامعة ويسكونسن.

### Back-Translation (Validation)
In this paper, we present ARIES (Algorithm for Recovery and Isolation Exploiting Semantics), a recovery method that relies on the write-ahead logging protocol. ARIES supports fine-granularity locking and provides effective support for transaction rollback. The recovery method uses an innovative concept of Log Sequence Numbers (LSNs) to track the state of pages and log records. During restart after system failure, ARIES uses a three-phase algorithm: the Analysis phase to determine the state of transactions and pages at the time of failure, the Redo phase to restore the database to its state at the time of failure, and the Undo phase to cancel incomplete transactions. ARIES introduces Compensation Log Records (CLRs), which are redo-only records that describe actions taken during transaction rollback and recovery. The method follows a No-Force and Steal policy allowing maximum performance flexibility. ARIES applies not only to database management systems but also to persistent object-oriented languages, recoverable file systems, and transaction-based operating systems. ARIES has been implemented to varying degrees in IBM's OS/2 Extended Edition Database Manager, DB2, IMS, Workstation Data Save Facility/VM, Starburst, and QuickSilver, and in the University of Wisconsin's EXODUS and Gamma database machines.

### Translation Metrics
- Iterations: 1
- Final Score: 0.94
- Quality: High

### Notes
This is a seminal paper in database systems published in ACM Transactions on Database Systems (TODS) in 1992. ARIES stands as one of the most influential papers in database recovery, establishing the foundational concepts used in most modern database management systems including IBM DB2, Microsoft SQL Server, PostgreSQL, and many others. The paper is approximately 69 pages long and provides comprehensive coverage of recovery algorithms, write-ahead logging protocols, and transaction management.

The translation preserves all technical concepts including:
- The three-phase recovery algorithm (Analysis, Redo, Undo)
- Log Sequence Numbers (LSNs) for tracking state
- Compensation Log Records (CLRs) for rollback tracking
- No-Force, Steal policy for performance optimization
- Broad applicability beyond traditional DBMS

### Challenges Encountered
1. **Source Access**: The paper is not available on arXiv (predates arXiv CS section). Abstract was compiled from multiple authoritative sources including IBM Research, ACM Digital Library references, and academic reviews.
2. **Technical Terminology**: Several database-specific terms needed new Arabic translations, particularly "No-Force, Steal policy" which required careful consideration of technical meaning versus literal translation.
3. **Identifier Selection**: Since this is not an arXiv paper, used the identifier "ACM-TODS-1992-Mohan-ARIES" based on publication venue, year, and first author.
