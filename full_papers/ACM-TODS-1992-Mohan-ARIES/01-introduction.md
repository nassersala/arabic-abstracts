# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** transaction, database, recovery, concurrency, performance, locking, atomicity, durability, consistency, write-ahead logging, checkpoint, buffer management

---

### English Version

Transaction-oriented systems require mechanisms to recover from failures while maintaining the ACID properties (Atomicity, Consistency, Isolation, and Durability). When failures occur, the system must ensure that committed transactions are not lost and that uncommitted transactions do not leave the database in an inconsistent state. Recovery algorithms must handle various failure scenarios including system crashes, media failures, and transaction aborts.

The design of a recovery algorithm is closely tied to other aspects of the database system, including the concurrency control mechanism, the buffer management policy, and the structure of the log. Several recovery methods have been proposed and implemented over the years, but many suffer from limitations in flexibility, performance, or complexity.

ARIES (Algorithm for Recovery and Isolation Exploiting Semantics) was designed to address these limitations and provide a comprehensive recovery framework that:

1. **Supports Fine-Granularity Locking**: ARIES works efficiently with lock granularities ranging from individual records to entire tables, supporting high concurrency without compromising recovery correctness.

2. **Enables Flexible Buffer Management**: The method follows a "No-Force" policy (not requiring dirty pages to be written before commit) and a "Steal" policy (allowing uncommitted changes to be written to disk), providing maximum flexibility for buffer management and performance optimization.

3. **Provides Efficient Partial Rollbacks**: ARIES supports savepoints and partial rollbacks efficiently, allowing transactions to undo only a portion of their work rather than completely aborting.

4. **Minimizes Recovery Time**: The three-pass recovery algorithm (Analysis, Redo, Undo) is designed to minimize the time needed to bring the system back online after a failure.

5. **Maintains Simplicity and Modularity**: Despite its comprehensive features, ARIES maintains a clean separation between normal processing and recovery processing, making it easier to understand, implement, and maintain.

The key innovation in ARIES is the use of Log Sequence Numbers (LSNs) to track the state of pages and transactions precisely. Each log record is assigned a monotonically increasing LSN, and each data page stores the LSN of the log record that describes its most recent update. This simple mechanism enables ARIES to determine exactly which updates need to be redone or undone during recovery, avoiding redundant work.

Another important contribution is the introduction of Compensation Log Records (CLRs). When a transaction is rolled back, either during normal processing or during recovery, the undo actions are themselves logged using CLRs. These records are redo-only (they describe actions that should never be undone), ensuring that recovery is idempotent and can be restarted at any point without corrupting the database.

ARIES has been widely adopted in commercial database systems and has influenced the design of recovery algorithms in many modern database management systems. The principles established in ARIES have proven applicable beyond traditional databases, extending to persistent programming languages, recoverable file systems, and transaction-based operating systems.

The remainder of this paper is organized as follows: Section 2 provides background on recovery concepts and terminology. Section 3 describes the system model and assumptions. Section 4 details the normal processing protocols including logging and page structure. Sections 5-8 describe the recovery algorithm in detail, covering the Analysis, Redo, and Undo passes. Section 9 discusses checkpointing. Section 10 covers nested top actions. Section 11 provides additional discussion and examples. Section 12 reviews related work. Section 13 concludes the paper.

---

### النسخة العربية

تتطلب الأنظمة الموجهة نحو المعاملات آليات للاسترداد من الأعطال مع الحفاظ على خصائص ACID (الذرية والاتساق والعزل والديمومة). عند حدوث أعطال، يجب على النظام التأكد من عدم فقدان المعاملات المُثبتة وأن المعاملات غير المُثبتة لا تترك قاعدة البيانات في حالة غير متسقة. يجب أن تتعامل خوارزميات الاسترداد مع سيناريوهات الفشل المختلفة بما في ذلك تعطل النظام وفشل الوسائط وإلغاء المعاملات.

يرتبط تصميم خوارزمية الاسترداد ارتباطاً وثيقاً بجوانب أخرى من نظام قاعدة البيانات، بما في ذلك آلية التحكم في التزامن وسياسة إدارة المخزن المؤقت وبنية السجل. تم اقتراح وتطبيق العديد من طرق الاسترداد على مر السنين، لكن الكثير منها يعاني من قيود في المرونة أو الأداء أو التعقيد.

تم تصميم ARIES (خوارزمية الاسترداد والعزل باستغلال الدلالات) لمعالجة هذه القيود وتوفير إطار عمل شامل للاسترداد يقوم بما يلي:

1. **دعم القفل دقيق التفصيل**: تعمل ARIES بكفاءة مع درجات تفصيل القفل التي تتراوح من السجلات الفردية إلى الجداول بأكملها، مما يدعم التزامن العالي دون المساس بصحة الاسترداد.

2. **تمكين إدارة مرنة للمخزن المؤقت**: تتبع الطريقة سياسة "عدم الإجبار" (عدم طلب كتابة الصفحات المعدلة قبل التثبيت) وسياسة "السرقة" (السماح بكتابة التغييرات غير المثبتة على القرص)، مما يوفر أقصى قدر من المرونة لإدارة المخزن المؤقت وتحسين الأداء.

3. **توفير تراجع جزئي فعال**: تدعم ARIES نقاط الحفظ والتراجع الجزئي بكفاءة، مما يسمح للمعاملات بالتراجع عن جزء فقط من عملها بدلاً من الإلغاء الكامل.

4. **تقليل وقت الاسترداد**: تم تصميم خوارزمية الاسترداد ثلاثية المراحل (التحليل والإعادة والتراجع) لتقليل الوقت اللازم لإعادة النظام إلى الاتصال بعد الفشل.

5. **الحفاظ على البساطة والنمطية**: على الرغم من ميزاتها الشاملة، تحافظ ARIES على فصل واضح بين المعالجة العادية ومعالجة الاسترداد، مما يسهل فهمها وتطبيقها وصيانتها.

الابتكار الرئيسي في ARIES هو استخدام أرقام تسلسل السجل (LSNs) لتتبع حالة الصفحات والمعاملات بدقة. يتم تعيين LSN متزايد بشكل رتيب لكل سجل، وتخزن كل صفحة بيانات LSN لسجل السجل الذي يصف أحدث تحديث لها. تمكن هذه الآلية البسيطة ARIES من تحديد التحديثات التي تحتاج إلى إعادة أو تراجع أثناء الاسترداد بالضبط، مع تجنب العمل الزائد.

مساهمة مهمة أخرى هي إدخال سجلات التعويض (CLRs). عند التراجع عن معاملة، سواء أثناء المعالجة العادية أو أثناء الاسترداد، يتم تسجيل إجراءات التراجع نفسها باستخدام CLRs. هذه السجلات للإعادة فقط (تصف إجراءات لا ينبغي أبداً التراجع عنها)، مما يضمن أن الاسترداد متماثل القوة ويمكن إعادة تشغيله في أي نقطة دون إفساد قاعدة البيانات.

تم اعتماد ARIES على نطاق واسع في أنظمة قواعد البيانات التجارية وقد أثرت على تصميم خوارزميات الاسترداد في العديد من أنظمة إدارة قواعد البيانات الحديثة. أثبتت المبادئ المنشأة في ARIES قابليتها للتطبيق خارج قواعد البيانات التقليدية، وامتدت إلى لغات البرمجة الدائمة وأنظمة الملفات القابلة للاسترداد وأنظمة التشغيل القائمة على المعاملات.

يتم تنظيم بقية هذا البحث على النحو التالي: يوفر القسم 2 خلفية عن مفاهيم الاسترداد والمصطلحات. يصف القسم 3 نموذج النظام والافتراضات. يفصل القسم 4 بروتوكولات المعالجة العادية بما في ذلك التسجيل وبنية الصفحة. تصف الأقسام 5-8 خوارزمية الاسترداد بالتفصيل، وتغطي مراحل التحليل والإعادة والتراجع. يناقش القسم 9 نقاط التحقق. يغطي القسم 10 الإجراءات العلوية المتداخلة. يوفر القسم 11 مناقشة وأمثلة إضافية. يراجع القسم 12 الأعمال ذات الصلة. يختتم القسم 13 البحث.

---

### Translation Notes

- **Key concepts introduced:** ACID properties, No-Force/Steal policy, LSNs, CLRs, three-pass recovery, idempotency, savepoints
- **Technical terms:** Transaction, recovery, concurrency control, buffer management, checkpoint, commit, rollback
- **Structure:** Introduction provides motivation, key innovations, and paper organization

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89
