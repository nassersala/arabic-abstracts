# Section 12: Related Work
## القسم 12: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.85
**Glossary Terms Used:** recovery, write-ahead logging, shadow paging, System R, IMS, database systems

---

### English Version

This section reviews related work in database recovery and positions ARIES in the context of prior research.

## 12.1 Early Recovery Methods

**System R Recovery:**
- One of the first WAL-based recovery systems
- Used Force policy (all modified pages written at commit)
- No-Steal policy (uncommitted changes not written to disk)
- ARIES improves on this with No-Force/Steal
- Significant performance advantages

**IMS Fast Path:**
- Main-memory database with recovery
- Deferred updates (similar to No-Force)
- Influenced ARIES design
- Limited to specific workloads

**Shadow Paging:**
- Used in early versions of System R
- No in-place updates - creates new page versions
- Pros: Simple recovery, no undo needed
- Cons: Poor performance, fragmentation, complex garbage collection
- ARIES provides better performance with in-place updates

## 12.2 Write-Ahead Logging Predecessors

**Gray's WAL Protocol:**
- Foundational work defining WAL principles
- Log records must precede data writes
- Commit records must be forced to stable storage
- ARIES implements and extends these principles

**Redo/Undo Logging:**
- Standard approach before ARIES
- ARIES refines this with:
  - LSN-based page versioning
  - CLRs for idempotent recovery
  - Repeating history principle
  - Physiological logging

## 12.3 Transaction Management

**Two-Phase Locking (2PL):**
- Standard concurrency control
- Eswaran et al. formalized 2PL
- ARIES works with various locking protocols
- Independent of concurrency control mechanism

**Multi-Version Concurrency Control (MVCC):**
- Alternative to locking
- ARIES principles applicable with modifications
- Snapshot isolation compatible

## 12.4 Checkpoint Techniques

**Consistent Checkpoints:**
- Quiesce system, flush all pages
- Simple but high overhead
- Long pause in processing

**Fuzzy Checkpoints:**
- ARIES innovation
- No system quiescing required
- Only record system state in log
- Minimal overhead

**Action-Consistent Checkpoints:**
- Middle ground between consistent and fuzzy
- Wait for operations to complete
- ARIES fuzzy checkpoints are simpler and more efficient

## 12.5 B-tree Recovery

**ARIES/IM:**
- Specialized recovery for indexes
- Handles B-tree splits without logging all details
- Uses nested top actions and logical logging
- Significant overhead reduction for indexes

**Mohan and Narang:**
- Recovery and coherency-control protocols for B-trees
- Exploits B-tree semantics
- Influenced ARIES/IM design

## 12.6 Distributed Database Recovery

**Two-Phase Commit (2PC):**
- Gray and Lampson
- Standard atomic commitment protocol
- ARIES integrates with 2PC naturally
- Each site uses ARIES for local recovery

**Presumed Abort/Commit:**
- Optimizations to 2PC
- ARIES supports these optimizations
- Reduces log forcing and message overhead

## 12.7 Object-Oriented Databases

**Persistent Programming Languages:**
- C++, Smalltalk with persistence
- ARIES principles applicable
- Object versioning and recovery

**ORION, O2, ObjectStore:**
- Commercial OO databases
- Many adopted ARIES-like recovery
- Extended to object-level granularity

## 12.8 Contributions of ARIES

ARIES synthesized and extended prior work:

**Novel Contributions:**
1. **Repeating History**: Simplifies redo pass
2. **CLRs**: Enable idempotent undo
3. **LSN-based page versioning**: Precise recovery control
4. **Fuzzy checkpoints**: Minimal overhead
5. **Physiological logging**: Balance simplicity and flexibility
6. **Nested top actions**: Handle non-undoable operations
7. **Comprehensive framework**: Unifies many recovery concepts

**Influence:**
- Widely adopted in commercial systems (DB2, SQL Server, PostgreSQL)
- Influenced academic research
- Established best practices for recovery

---

### النسخة العربية

يراجع هذا القسم الأعمال ذات الصلة في استرداد قاعدة البيانات ويضع ARIES في سياق البحث السابق.

## 12.1 طرق الاسترداد المبكرة

**استرداد System R:**
- واحد من أوائل أنظمة الاسترداد القائمة على WAL
- استخدم سياسة الإجبار (كتابة جميع الصفحات المعدلة عند التثبيت)
- سياسة عدم السرقة (لا تُكتب التغييرات غير المثبتة على القرص)
- تحسن ARIES على هذا بـ عدم الإجبار/السرقة
- مزايا أداء كبيرة

**IMS Fast Path:**
- قاعدة بيانات الذاكرة الرئيسية مع الاسترداد
- تحديثات مؤجلة (مشابه لعدم الإجبار)
- أثرت على تصميم ARIES
- محدودة لأحمال عمل محددة

**Shadow Paging:**
- استُخدم في الإصدارات المبكرة من System R
- لا توجد تحديثات في مكانها - ينشئ إصدارات صفحة جديدة
- الإيجابيات: استرداد بسيط، لا حاجة للتراجع
- السلبيات: أداء ضعيف، تجزئة، جمع قمامة معقد
- توفر ARIES أداءً أفضل مع التحديثات في مكانها

## 12.2 أسلاف التسجيل المسبق للكتابة

**بروتوكول WAL لـ Gray:**
- عمل تأسيسي يحدد مبادئ WAL
- يجب أن تسبق سجلات السجل عمليات كتابة البيانات
- يجب فرض سجلات التثبيت على التخزين المستقر
- تنفذ ARIES وتوسع هذه المبادئ

**تسجيل Redo/Undo:**
- النهج القياسي قبل ARIES
- تحسن ARIES هذا بـ:
  - إصدار الصفحة القائم على LSN
  - CLRs للاسترداد متماثل القوة
  - مبدأ تكرار التاريخ
  - التسجيل الفسيولوجي

## 12.3 إدارة المعاملات

**القفل ثنائي المراحل (2PL):**
- التحكم في التزامن القياسي
- رسمّ Eswaran وآخرون 2PL
- تعمل ARIES مع بروتوكولات قفل مختلفة
- مستقلة عن آلية التحكم في التزامن

**التحكم في التزامن متعدد الإصدارات (MVCC):**
- بديل للقفل
- مبادئ ARIES قابلة للتطبيق مع تعديلات
- عزل اللقطة متوافق

## 12.4 تقنيات نقاط التحقق

**نقاط التحقق المتسقة:**
- إيقاف النظام، مسح جميع الصفحات
- بسيط ولكن حمل زائد عالٍ
- توقف طويل في المعالجة

**نقاط التحقق الضبابية:**
- ابتكار ARIES
- لا حاجة لإيقاف النظام
- فقط تسجيل حالة النظام في السجل
- حمل زائد ضئيل

**نقاط التحقق المتسقة للإجراء:**
- حل وسط بين المتسقة والضبابية
- انتظار اكتمال العمليات
- نقاط التحقق الضبابية لـ ARIES أبسط وأكثر كفاءة

## 12.5 استرداد شجرة B

**ARIES/IM:**
- استرداد متخصص للفهارس
- يتعامل مع انقسامات شجرة B دون تسجيل جميع التفاصيل
- يستخدم إجراءات علوية متداخلة وتسجيل منطقي
- تقليل كبير في الحمل الزائد للفهارس

**Mohan و Narang:**
- بروتوكولات الاسترداد والتحكم في التماسك لأشجار B
- يستغل دلالات شجرة B
- أثر على تصميم ARIES/IM

## 12.6 استرداد قاعدة البيانات الموزعة

**التثبيت ثنائي المراحل (2PC):**
- Gray و Lampson
- بروتوكول الالتزام الذري القياسي
- تتكامل ARIES مع 2PC بشكل طبيعي
- يستخدم كل موقع ARIES للاسترداد المحلي

**الإلغاء/التثبيت المفترض:**
- تحسينات لـ 2PC
- تدعم ARIES هذه التحسينات
- تقلل فرض السجل والحمل الزائد للرسائل

## 12.7 قواعد البيانات الموجهة نحو الكائنات

**لغات البرمجة الدائمة:**
- C++، Smalltalk مع الديمومة
- مبادئ ARIES قابلة للتطبيق
- إصدار الكائن والاسترداد

**ORION, O2, ObjectStore:**
- قواعد بيانات OO تجارية
- اعتمد الكثير منها استرداداً شبيهاً بـ ARIES
- امتدت إلى درجة تفصيل مستوى الكائن

## 12.8 مساهمات ARIES

جمعت ARIES ووسعت العمل السابق:

**المساهمات الجديدة:**
1. **تكرار التاريخ**: يبسط مرحلة الإعادة
2. **CLRs**: تمكّن التراجع متماثل القوة
3. **إصدار الصفحة القائم على LSN**: تحكم دقيق في الاسترداد
4. **نقاط التحقق الضبابية**: حمل زائد ضئيل
5. **التسجيل الفسيولوجي**: توازن البساطة والمرونة
6. **الإجراءات العلوية المتداخلة**: تتعامل مع عمليات غير قابلة للتراجع
7. **إطار عمل شامل**: يوحد العديد من مفاهيم الاسترداد

**التأثير:**
- اعتُمدت على نطاق واسع في الأنظمة التجارية (DB2, SQL Server, PostgreSQL)
- أثرت على البحث الأكاديمي
- وضعت أفضل الممارسات للاسترداد

---

### Translation Notes

- **Key systems:** System R, IMS, ORION, O2, ObjectStore
- **Protocols:** WAL, 2PC, 2PL, MVCC
- **Comparisons:** Shadow paging vs. WAL, fuzzy vs. consistent checkpoints
- **Historical context:** Evolution of recovery methods

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.85
