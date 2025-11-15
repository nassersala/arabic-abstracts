# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** database (قاعدة بيانات), distributed transactions (معاملات موزعة), API (واجهة برمجة التطبيقات), consistency (اتساق), replication (النسخ المتماثل)

---

### English Version

Spanner is Google's scalable, multi-version, globally-distributed, and synchronously-replicated database. It is the first system to distribute data at global scale and support externally-consistent distributed transactions. This paper describes how Spanner is structured, its feature set, the rationale underlying various design decisions, and a novel time API that exposes clock uncertainty. This API and its implementation are critical to supporting external consistency and a variety of powerful features: non-blocking reads in the past, lock-free read-only transactions, and atomic schema changes, across all of Spanner.

---

### النسخة العربية

سبانر (Spanner) هي قاعدة بيانات جوجل القابلة للتوسع، متعددة الإصدارات، الموزعة عالمياً، والمنسوخة بشكل متزامن. إنها أول نظام يوزع البيانات على نطاق عالمي ويدعم المعاملات الموزعة ذات الاتساق الخارجي. تصف هذه الورقة البحثية كيفية بناء سبانر، ومجموعة ميزاتها، والأساس المنطقي الكامن وراء مختلف قرارات التصميم، وواجهة برمجة تطبيقات الوقت المبتكرة (TrueTime API) التي تكشف عن عدم اليقين في الساعات. هذه الواجهة وتنفيذها حاسمان لدعم الاتساق الخارجي ومجموعة متنوعة من الميزات القوية: القراءات غير المحجوبة في الماضي، والمعاملات للقراءة فقط الخالية من الأقفال، والتغييرات الذرية في المخططات، عبر سبانر بأكملها.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - External consistency (الاتساق الخارجي)
  - Multi-version database (قاعدة بيانات متعددة الإصدارات)
  - Synchronous replication (النسخ المتماثل المتزامن)
  - TrueTime API (واجهة برمجة تطبيقات TrueTime)
  - Clock uncertainty (عدم اليقين في الساعات)
  - Non-blocking reads (القراءات غير المحجوبة)
  - Lock-free transactions (المعاملات الخالية من الأقفال)
  - Atomic schema changes (التغييرات الذرية في المخططات)
- **Equations:** 0
- **Citations:** 0
- **Special handling:** "TrueTime API" kept in English as it's a proper name, with Arabic descriptor

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.95
- Readability: 0.88
- Glossary consistency: 0.95
- **Overall section score:** 0.90
