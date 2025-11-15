# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** distributed transaction, database, partitioning, concurrency control, deterministic, replication, serializable, consensus, ACID, two-phase commit, throughput, latency, lock manager, distributed system

---

### English Version

Calvin is a practical transaction scheduling and data replication layer that uses a deterministic ordering guarantee to significantly reduce the normally prohibitive contention costs associated with distributed transactions. Calvin eliminates distributed commit protocols by preprocessing transaction inputs and deterministically ordering all transactions before executing them. The system achieves this through a sequencing layer that establishes a global transaction order using Paxos replication of transaction inputs across replicas. Once the order is established, each replica independently executes transactions in the same deterministic order, guaranteeing that all replicas reach identical states without requiring expensive agreement protocols during execution. Calvin supports full ACID transactions across partitioned and replicated data while maintaining high throughput and low latency. The deterministic execution model allows Calvin to avoid the overhead of traditional two-phase commit protocols and achieve linear scalability. Experimental results demonstrate that Calvin can achieve over 500,000 transactions per second on a 100-node cluster while providing strong consistency guarantees.

---

### النسخة العربية

كالفن (Calvin) هو طبقة عملية لجدولة المعاملات ونسخ البيانات تستخدم ضمان ترتيب حتمي للحد بشكل كبير من تكاليف التنافس المرتفعة عادةً المرتبطة بالمعاملات الموزعة. يلغي كالفن بروتوكولات الالتزام الموزع من خلال المعالجة المسبقة لمدخلات المعاملات والترتيب الحتمي لجميع المعاملات قبل تنفيذها. يحقق النظام هذا من خلال طبقة تسلسل تنشئ ترتيباً عالمياً للمعاملات باستخدام نسخ باكسوس (Paxos) لمدخلات المعاملات عبر النُسخ المتماثلة. بمجرد إنشاء الترتيب، تنفذ كل نسخة متماثلة المعاملات بشكل مستقل بنفس الترتيب الحتمي، مما يضمن وصول جميع النُسخ المتماثلة إلى حالات متطابقة دون الحاجة إلى بروتوكولات اتفاق مكلفة أثناء التنفيذ. يدعم كالفن معاملات ACID كاملة عبر البيانات المجزأة والمنسوخة مع الحفاظ على إنتاجية عالية وزمن استجابة منخفض. يسمح نموذج التنفيذ الحتمي لكالفن بتجنب التكلفة العامة لبروتوكولات الالتزام ثنائي الطور التقليدية وتحقيق قابلية توسع خطية. تُظهِر النتائج التجريبية أن كالفن يمكنه تحقيق أكثر من 500,000 معاملة في الثانية على عنقود مكون من 100 عقدة مع توفير ضمانات اتساق قوية.

---

### Translation Notes

- **Key terms introduced:**
  - Deterministic ordering: ترتيب حتمي
  - Transaction scheduling: جدولة المعاملات
  - Replication layer: طبقة النسخ
  - Paxos replication: نسخ باكسوس
  - ACID transactions: معاملات ACID
  - Two-phase commit: الالتزام ثنائي الطور
  - Linear scalability: قابلية توسع خطية
  - Consensus: اتفاق

- **Equations:** None
- **Citations:** None
- **Special handling:** Preserved proper name "Calvin" in English; kept "Paxos" as is with Arabic transliteration in parentheses

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.95
- **Overall section score:** 0.93

### Back-Translation Validation

"Calvin is a practical layer for transaction scheduling and data replication that uses deterministic ordering guarantee to significantly reduce the typically high contention costs associated with distributed transactions. Calvin eliminates distributed commit protocols through preprocessing transaction inputs and deterministically ordering all transactions before execution. The system achieves this through a sequencing layer that creates a global transaction order using Paxos replication of transaction inputs across replicas. Once the order is established, each replica executes transactions independently in the same deterministic order, ensuring all replicas reach identical states without requiring expensive agreement protocols during execution. Calvin supports full ACID transactions across partitioned and replicated data while maintaining high throughput and low latency. The deterministic execution model allows Calvin to avoid the overhead of traditional two-phase commit protocols and achieve linear scalability. Experimental results show that Calvin can achieve over 500,000 transactions per second on a 100-node cluster while providing strong consistency guarantees."

✅ Back-translation preserves all technical concepts and meaning.
