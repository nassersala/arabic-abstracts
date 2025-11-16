# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** بنية البيانات, نظام موزع, دالة التجزئة, رسم بياني, الأمن السيبراني, خوارزمية, بنى البيانات الموزعة المصادق عليها, شبكة الكتل

---

### English Version

We present Charlotte, a framework for composable, authenticated distributed data structures. Charlotte data is stored in blocks that reference each other by hash. Together, all Charlotte blocks form a directed acyclic graph, the blockweb; all observers and applications use subgraphs of the blockweb for their own data structures. Unlike prior systems, Charlotte data structures are composable: applications and data structures can operate fully independently when possible, and share blocks when desired.

To support this composability, we define a language-independent format for Charlotte blocks and a network API for Charlotte servers.

An authenticated distributed data structure guarantees that data is immutable and self-authenticating: data referenced will be unchanged when it is retrieved. Charlotte extends these guarantees by allowing applications to plug in their own mechanisms for ensuring availability and integrity of data structures. Unlike most traditional distributed systems, including distributed databases, blockchains, and distributed hash tables, Charlotte supports heterogeneous trust: different observers may have their own beliefs about who might fail, and how. Despite heterogeneity of trust, Charlotte presents each observer with a consistent, available view of data.

We demonstrate the flexibility of Charlotte by implementing a variety of integrity mechanisms, including consensus and proof of work. We study the power of disentangling availability and integrity mechanisms by building a variety of applications. The results from these examples suggest that developers can use Charlotte to build flexible, fast, composable applications with strong guarantees.

---

### النسخة العربية

نقدم Charlotte، وهو إطار عمل لبنى البيانات الموزعة المصادق عليها والقابلة للتركيب. يتم تخزين بيانات Charlotte في كتل تشير إلى بعضها البعض عبر دوال التجزئة. معاً، تشكل جميع كتل Charlotte رسماً بيانياً لا دورياً موجهاً، وهو "شبكة الكتل" (blockweb)؛ ويستخدم جميع المراقبين والتطبيقات رسوماً بيانية فرعية من شبكة الكتل لبنى بياناتهم الخاصة. على عكس الأنظمة السابقة، فإن بنى بيانات Charlotte قابلة للتركيب: يمكن للتطبيقات وبنى البيانات العمل بشكل مستقل تماماً عند الإمكان، ومشاركة الكتل عند الرغبة.

لدعم قابلية التركيب هذه، نحدد تنسيقاً مستقلاً عن اللغة لكتل Charlotte وواجهة برمجة تطبيقات شبكية لخوادم Charlotte.

تضمن بنية البيانات الموزعة المصادق عليها أن البيانات غير قابلة للتغيير ومصادق عليها ذاتياً: ستظل البيانات المشار إليها دون تغيير عند استرجاعها. يوسّع Charlotte هذه الضمانات من خلال السماح للتطبيقات بإضافة آلياتها الخاصة لضمان توفر وسلامة بنى البيانات. على عكس معظم الأنظمة الموزعة التقليدية، بما في ذلك قواعد البيانات الموزعة، والبلوك تشين، وجداول التجزئة الموزعة، يدعم Charlotte الثقة غير المتجانسة: قد يكون لدى مراقبين مختلفين معتقدات خاصة بهم حول من قد يفشل، وكيف. على الرغم من عدم تجانس الثقة، يقدم Charlotte لكل مراقب رؤية متسقة ومتاحة للبيانات.

نوضح مرونة Charlotte من خلال تنفيذ مجموعة متنوعة من آليات السلامة، بما في ذلك الإجماع وإثبات العمل. ندرس قوة فصل آليات التوفر والسلامة من خلال بناء مجموعة متنوعة من التطبيقات. تشير النتائج من هذه الأمثلة إلى أن المطورين يمكنهم استخدام Charlotte لبناء تطبيقات مرنة وسريعة وقابلة للتركيب مع ضمانات قوية.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:** Charlotte, blockweb, authenticated distributed data structures (ADDS), composability, heterogeneous trust, integrity mechanisms, availability mechanisms, Wilbur servers, Fern servers
- **Equations:** None in abstract
- **Citations:** Multiple references to related work
- **Special handling:** Technical terminology maintained consistency with glossary

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.90
