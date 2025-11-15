# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** distributed system, storage, scalable, performance, throughput, latency, commodity servers, fault-tolerant, data model

---

### English Version

Over the last two and a half years we have designed, implemented, and deployed a distributed storage system for managing structured data at Google called Bigtable. Bigtable is designed to reliably scale to petabytes of data and thousands of machines. Bigtable has achieved several goals: wide applicability, scalability, high performance, and high availability. Bigtable is used by more than sixty Google products and projects, including Google Analytics, Google Finance, Orkut, Personalized Search, Writely, and Google Earth. These products use Bigtable for a variety of demanding workloads, which range from throughput-oriented batch-processing jobs to latency-sensitive serving of data to end users. The Bigtable clusters used by these products span a wide range of configurations, from a handful of servers to thousands of servers, and store up to several hundred terabytes of data.

In many ways, Bigtable resembles a database: it shares many implementation strategies with databases. Parallel databases and main-memory databases have achieved scalability and high performance, but Bigtable provides a different interface than such systems. Bigtable does not support a full relational data model; instead, it provides clients with a simple data model that supports dynamic control over data layout and format, and allows clients to reason about the locality properties of the data represented in the underlying storage. Data is indexed using row and column names that can be arbitrary strings. Bigtable also treats data as uninterpreted strings, although clients often serialize various forms of structured and semi-structured data into these strings. Clients can control the locality of their data through careful choices in their schemas. Finally, Bigtable schema parameters let clients dynamically control whether to serve data out of memory or from disk.

Section 2 describes the data model in more detail, and Section 3 provides an overview of the client API. Section 4 describes the Google File System (GFS), which is the underlying storage system that Bigtable uses, and Chubby, a highly-available and persistent distributed lock service. Section 5 describes the implementation of the Bigtable system. Section 6 describes some of the refinements that we made to the Bigtable design. Section 7 provides performance numbers for Bigtable. Section 8 describes several examples of how Bigtable is used at Google. Section 9 discusses some lessons we learned in the design, implementation, deployment, and support of Bigtable. Section 10 describes related work, and Section 11 presents our conclusions.

---

### النسخة العربية

على مدى السنتين والنصف الماضية، قمنا بتصميم وتنفيذ ونشر نظام تخزين موزع لإدارة البيانات المنظمة في جوجل يسمى بيجتيبل (Bigtable). صُمم بيجتيبل للتوسع بشكل موثوق إلى بيتابايتات من البيانات وآلاف الأجهزة. حقق بيجتيبل عدة أهداف: قابلية تطبيق واسعة، وقابلية التوسع، وأداء عالٍ، وتوفر عالٍ. يُستخدم بيجتيبل من قبل أكثر من ستين منتجاً ومشروعاً في جوجل، بما في ذلك Google Analytics وGoogle Finance وOrkut والبحث الشخصي (Personalized Search) وWritely وGoogle Earth. تستخدم هذه المنتجات بيجتيبل لمجموعة متنوعة من أحمال العمل الصعبة، التي تتراوح من وظائف المعالجة الدفعية الموجهة نحو الإنتاجية إلى تقديم البيانات الحساسة لزمن الاستجابة للمستخدمين النهائيين. تمتد مجموعات بيجتيبل المستخدمة من قبل هذه المنتجات عبر نطاق واسع من التكوينات، من حفنة من الخوادم إلى آلاف الخوادم، وتخزن ما يصل إلى عدة مئات من التيرابايتات من البيانات.

من نواحٍ عديدة، يشبه بيجتيبل قاعدة بيانات: فهو يشترك في العديد من استراتيجيات التنفيذ مع قواعد البيانات. حققت قواعد البيانات المتوازية وقواعد بيانات الذاكرة الرئيسية قابلية التوسع والأداء العالي، لكن بيجتيبل يوفر واجهة مختلفة عن مثل هذه الأنظمة. لا يدعم بيجتيبل نموذج بيانات علائقي كامل؛ بدلاً من ذلك، يوفر للعملاء نموذج بيانات بسيطاً يدعم التحكم الديناميكي في تخطيط البيانات وتنسيقها، ويسمح للعملاء بالاستدلال حول خصائص الموضعية للبيانات الممثلة في التخزين الأساسي. تتم فهرسة البيانات باستخدام أسماء الصفوف والأعمدة التي يمكن أن تكون سلاسل نصية تعسفية. يعامل بيجتيبل أيضاً البيانات كسلاسل نصية غير مفسرة، على الرغم من أن العملاء غالباً ما يقومون بتسلسل أشكال مختلفة من البيانات المنظمة وشبه المنظمة في هذه السلاسل. يمكن للعملاء التحكم في موضعية بياناتهم من خلال اختيارات دقيقة في مخططاتهم. أخيراً، تتيح معاملات مخطط بيجتيبل للعملاء التحكم الديناميكي في ما إذا كان سيتم تقديم البيانات من الذاكرة أو من القرص.

يصف القسم 2 نموذج البيانات بمزيد من التفصيل، ويقدم القسم 3 نظرة عامة على واجهة برمجة التطبيقات للعميل. يصف القسم 4 نظام ملفات جوجل (GFS)، وهو نظام التخزين الأساسي الذي يستخدمه بيجتيبل، وChubby، وهي خدمة قفل موزعة عالية التوفر ودائمة. يصف القسم 5 تنفيذ نظام بيجتيبل. يصف القسم 6 بعض التحسينات التي أجريناها على تصميم بيجتيبل. يوفر القسم 7 أرقام الأداء لبيجتيبل. يصف القسم 8 عدة أمثلة على كيفية استخدام بيجتيبل في جوجل. يناقش القسم 9 بعض الدروس التي تعلمناها في تصميم وتنفيذ ونشر ودعم بيجتيبل. يصف القسم 10 العمل ذي الصلة، ويقدم القسم 11 استنتاجاتنا.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - wide applicability (قابلية تطبيق واسعة)
  - high availability (توفر عالٍ)
  - throughput-oriented (موجهة نحو الإنتاجية)
  - latency-sensitive (حساسة لزمن الاستجابة)
  - relational data model (نموذج بيانات علائقي)
  - locality properties (خصائص الموضعية)
  - uninterpreted strings (سلاسل نصية غير مفسرة)
  - schema (مخطط)
- **Citations:** References to GFS and Chubby systems
- **Special handling:** Product names kept in English (Google Analytics, Orkut, etc.)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
