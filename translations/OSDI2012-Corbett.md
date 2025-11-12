# Spanner: Google's Globally-Distributed Database
## سبانر: قاعدة بيانات جوجل الموزعة عالمياً

**Paper ID:** OSDI 2012 (Best Paper Award)
**Authors:** James C. Corbett, Jeffrey Dean, Michael Epstein, Andrew Fikes, Christopher Frost, JJ Furman, Sanjay Ghemawat, Andrey Gubarev, Christopher Heiser, Peter Hochschild, Wilson Hsieh, Sebastian Kanthak, Eugene Kogan, Hongyi Li, Alexander Lloyd, Sergey Melnik, David Mwaura, David Nagle, Sean Quinlan, Rajesh Rao, Lindsay Rolig, Yasushi Saito, Michal Szymaniak, Christopher Taylor, Ruth Wang, and Dale Woodford
**Conference:** 10th USENIX Symposium on Operating Systems Design and Implementation (OSDI 12)
**Year:** 2012
**Translation Quality:** 0.95
**Glossary Terms Used:** database, scalable, distributed system, transaction, consistency, lock-free, atomicity, uncertainty, implementation

### English Abstract
Spanner is Google's scalable, multi-version, globally-distributed, and synchronously-replicated database. It is the first system to distribute data at global scale and support externally-consistent distributed transactions. This paper describes how Spanner is structured, its feature set, the rationale underlying various design decisions, and a novel time API that exposes clock uncertainty. This API and its implementation are critical to supporting external consistency and a variety of powerful features: nonblocking reads in the past, lock-free read-only transactions, and atomic schema changes, across all of Spanner.

### الملخص العربي
سبانر هو قاعدة بيانات جوجل القابلة للتوسع، متعددة الإصدارات، الموزعة عالمياً، والمُنسَّخة بشكل متزامن. وهو أول نظام يقوم بتوزيع البيانات على نطاق عالمي ويدعم المعاملات الموزعة المتسقة خارجياً. تصف هذه الورقة البحثية كيفية بناء سبانر، ومجموعة ميزاته، والأساس المنطقي الذي يكمن وراء مختلف قرارات التصميم، وواجهة برمجة تطبيقات زمنية جديدة تكشف عدم اليقين في الساعة. هذه الواجهة البرمجية وتطبيقها حاسمان لدعم الاتساق الخارجي ومجموعة متنوعة من الميزات القوية: القراءات غير المعطّلة في الماضي، والمعاملات للقراءة فقط الخالية من القفل، والتغييرات الذرية في المخطط، عبر جميع أجزاء سبانر.

### Back-Translation (Validation)
Spanner is Google's scalable, multi-version, globally distributed, and synchronously replicated database. It is the first system to distribute data on a global scale and supports externally consistent distributed transactions. This research paper describes how Spanner is built, its feature set, the logical foundation underlying various design decisions, and a new temporal API that reveals clock uncertainty. This API and its implementation are critical for supporting external consistency and a diverse set of powerful features: non-blocking reads in the past, lock-free read-only transactions, and atomic changes to the schema, across all parts of Spanner.

### Translation Metrics
- Iterations: 1
- Final Score: 0.95
- Quality: High
- Semantic Equivalence: 0.95
- Technical Accuracy: 0.95
- Completeness: 1.0
- Coherence: 0.90
- Glossary Consistency: 0.95

### Notes
This is a landmark paper in distributed systems that introduced Google's Spanner database and the TrueTime API. The paper received the Jay Lepreau Best Paper Award at OSDI 2012. The translation preserves all technical concepts including the novel TrueTime API that exposes clock uncertainty, which is critical to Spanner's guarantees of external consistency.
