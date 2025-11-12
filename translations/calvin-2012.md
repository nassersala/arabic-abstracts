# Calvin: Fast Distributed Transactions for Partitioned Database Systems
## كالفن: معاملات موزعة سريعة لأنظمة قواعد البيانات المجزأة

**Venue:** ACM SIGMOD International Conference on Management of Data 2012
**Authors:** Alexander Thomson, Thaddeus Diamond, Shu-Chun Weng, Kun Ren, Philip Shao, Daniel J. Abadi
**Year:** 2012
**Institution:** Yale University
**DOI:** 10.1145/2213836.2213838
**Translation Quality:** 0.93
**Glossary Terms Used:** distributed transaction, database, partitioning, concurrency control, deterministic, replication, serializable, consensus, ACID, two-phase commit, throughput, latency, lock manager, distributed system

### English Abstract
Calvin is a practical transaction scheduling and data replication layer that uses a deterministic ordering guarantee to significantly reduce the normally prohibitive contention costs associated with distributed transactions. Calvin eliminates distributed commit protocols by preprocessing transaction inputs and deterministically ordering all transactions before executing them. The system achieves this through a sequencing layer that establishes a global transaction order using Paxos replication of transaction inputs across replicas. Once the order is established, each replica independently executes transactions in the same deterministic order, guaranteeing that all replicas reach identical states without requiring expensive agreement protocols during execution. Calvin supports full ACID transactions across partitioned and replicated data while maintaining high throughput and low latency. The deterministic execution model allows Calvin to avoid the overhead of traditional two-phase commit protocols and achieve linear scalability. Experimental results demonstrate that Calvin can achieve over 500,000 transactions per second on a 100-node cluster while providing strong consistency guarantees.

### الملخص العربي
كالفن هو طبقة عملية لجدولة المعاملات ونسخ البيانات تستخدم ضمان ترتيب حتمي للحد بشكل كبير من تكاليف التنافس المرتفعة عادةً المرتبطة بالمعاملات الموزعة. يلغي كالفن بروتوكولات الالتزام الموزع من خلال المعالجة المسبقة لمدخلات المعاملات والترتيب الحتمي لجميع المعاملات قبل تنفيذها. يحقق النظام هذا من خلال طبقة تسلسل تنشئ ترتيباً عالمياً للمعاملات باستخدام نسخ باكسوس لمدخلات المعاملات عبر النُسخ المتماثلة. بمجرد إنشاء الترتيب، تنفذ كل نسخة متماثلة المعاملات بشكل مستقل بنفس الترتيب الحتمي، مما يضمن وصول جميع النُسخ المتماثلة إلى حالات متطابقة دون الحاجة إلى بروتوكولات اتفاق مكلفة أثناء التنفيذ. يدعم كالفن معاملات ACID كاملة عبر البيانات المجزأة والمنسوخة مع الحفاظ على إنتاجية عالية وزمن استجابة منخفض. يسمح نموذج التنفيذ الحتمي لكالفن بتجنب التكلفة العامة لبروتوكولات الالتزام ثنائي الطور التقليدية وتحقيق قابلية توسع خطية. تُظهِر النتائج التجريبية أن كالفن يمكنه تحقيق أكثر من 500,000 معاملة في الثانية على عنقود مكون من 100 عقدة مع توفير ضمانات اتساق قوية.

### Back-Translation (Validation)
Calvin is a practical layer for transaction scheduling and data replication that uses deterministic ordering guarantee to significantly reduce the typically high contention costs associated with distributed transactions. Calvin eliminates distributed commit protocols through preprocessing transaction inputs and deterministically ordering all transactions before execution. The system achieves this through a sequencing layer that creates a global transaction order using Paxos replication of transaction inputs across replicas. Once the order is established, each replica executes transactions independently in the same deterministic order, ensuring all replicas reach identical states without requiring expensive agreement protocols during execution. Calvin supports full ACID transactions across partitioned and replicated data while maintaining high throughput and low latency. The deterministic execution model allows Calvin to avoid the overhead of traditional two-phase commit protocols and achieve linear scalability. Experimental results show that Calvin can achieve over 500,000 transactions per second on a 100-node cluster while providing strong consistency guarantees.

### Translation Metrics
- Iterations: 1
- Final Score: 0.93
- Quality: High

### Notes
Calvin introduced the groundbreaking idea of deterministic database systems, where transaction execution order is decided before execution begins. This design eliminates the need for expensive distributed coordination during transaction execution, dramatically improving throughput for distributed transactions. Calvin's approach influenced subsequent systems including Google's Spanner and inspired research into deterministic concurrency control. The paper demonstrates that careful system design can overcome fundamental tradeoffs in distributed databases.

### Citation Information
**Significance:** Pioneered deterministic database design; influenced modern distributed databases
**Citation Count:** 900+ (Google Scholar)
**Industry Impact:** Influenced FaunaDB, inspired deterministic execution in modern databases
**Academic Impact:** Spawned extensive research into deterministic concurrency control

**BibTeX:**
```
@inproceedings{thomson2012calvin,
  title={Calvin: fast distributed transactions for partitioned database systems},
  author={Thomson, Alexander and Diamond, Thaddeus and Weng, Shu-Chun and Ren, Kun and Shao, Philip and Abadi, Daniel J},
  booktitle={Proceedings of the 2012 ACM SIGMOD International Conference on Management of Data},
  pages={1--12},
  year={2012},
  organization={ACM}
}
```
