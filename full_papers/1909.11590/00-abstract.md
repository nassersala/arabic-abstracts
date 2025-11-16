# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** blockchain, Merkle tree, transaction, throughput, architecture, security, processing, storage, smart contract, sharding, distributed, I/O bottleneck

---

### English Version

Public blockchains like Ethereum use Merkle trees to verify transactions received from untrusted servers before applying them to the blockchain. We empirically show that the low throughput of such blockchains is due to the I/O bottleneck associated with using Merkle trees for processing transactions. We present RAINBLOCK, a new architecture for public blockchains that increases throughput without affecting security. RAINBLOCK achieves this by tackling the I/O bottleneck on two fronts: first, decoupling transaction processing from I/O, and removing I/O from the critical path; second, reducing I/O amplification by customizing storage for blockchains. RAINBLOCK uses a novel variant of the Merkle tree, the Distributed Sharded Merkle tree (DSM-TREE) to store system state. We evaluate RAINBLOCK using workloads based on public Ethereum traces (including smart contracts) and show that RAINBLOCK processes 20K transactions per second in a geo-distributed setting with four regions spread across three continents.

---

### النسخة العربية

تستخدم سلاسل الكتل العامة مثل إيثيريوم أشجار ميركل للتحقق من المعاملات المستلمة من خوادم غير موثوقة قبل تطبيقها على البلوك تشين. نُظهر تجريبياً أن الإنتاجية المنخفضة لمثل هذه السلاسل يعود إلى عنق الزجاجة في الإدخال/الإخراج المرتبط باستخدام أشجار ميركل لمعالجة المعاملات. نقدم RAINBLOCK، وهي معمارية جديدة لسلاسل الكتل العامة تزيد من الإنتاجية دون التأثير على الأمان. يحقق RAINBLOCK ذلك من خلال معالجة عنق الزجاجة في الإدخال/الإخراج على جبهتين: أولاً، فصل معالجة المعاملات عن الإدخال/الإخراج، وإزالة الإدخال/الإخراج من المسار الحرج؛ ثانياً، تقليل تضخيم الإدخال/الإخراج من خلال تخصيص التخزين لسلاسل الكتل. يستخدم RAINBLOCK نوعاً جديداً من شجرة ميركل، وهي شجرة ميركل المجزأة الموزعة (DSM-TREE) لتخزين حالة النظام. نقيّم RAINBLOCK باستخدام أحمال عمل قائمة على آثار إيثيريوم العامة (بما في ذلك العقود الذكية) ونُظهر أن RAINBLOCK يعالج 20 ألف معاملة في الثانية في بيئة موزعة جغرافياً مع أربع مناطق موزعة عبر ثلاث قارات.

---

### Translation Notes

- **Key terms introduced:** RAINBLOCK, DSM-TREE (Distributed Sharded Merkle Tree), I/O bottleneck, critical path, I/O amplification
- **Technical terms:** Merkle tree (شجرة ميركل), blockchain (البلوك تشين/سلاسل الكتل), transaction (معاملة), throughput (إنتاجية), smart contracts (العقود الذكية)
- **Performance metrics:** 20K transactions per second, geo-distributed setting, four regions, three continents
- **Special handling:** Kept "RAINBLOCK" and "DSM-TREE" as English acronyms as is standard for system names

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.92
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.91
