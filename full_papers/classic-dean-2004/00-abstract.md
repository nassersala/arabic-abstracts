# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.90 (from translations/classic-dean-2004.md)
**Glossary Terms Used:** programming model, data processing, dataset, cluster, function, parallelization, machine failure, scheduling, communication, network, disk, distributed computing

---

### English Version

MapReduce is a programming model and an associated implementation for processing and generating large data sets. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key. Many real world tasks are expressible in this model, as shown in the paper.

Programs written in this functional style are automatically parallelized and executed on a large cluster of commodity machines. The run-time system takes care of the details of partitioning the input data, scheduling the program's execution across a set of machines, handling machine failures, and managing the required inter-machine communication. This allows programmers without any experience with parallel and distributed systems to easily utilize the resources of a large distributed system.

Our implementation of MapReduce runs on a large cluster of commodity machines and is highly scalable: a typical MapReduce computation processes many terabytes of data on thousands of machines. Programmers find the system easy to use: hundreds of MapReduce programs have been implemented and upwards of one thousand MapReduce jobs are executed on Google's clusters every day.

---

### النسخة العربية

MapReduce هو نموذج برمجي وتطبيق مرتبط به لمعالجة وتوليد مجموعات البيانات الكبيرة. يحدد المستخدمون دالة map التي تعالج زوج مفتاح/قيمة لتوليد مجموعة من أزواج المفتاح/القيمة الوسيطة، ودالة reduce التي تدمج جميع القيم الوسيطة المرتبطة بنفس المفتاح الوسيط. العديد من المهام الواقعية يمكن التعبير عنها بهذا النموذج، كما هو موضح في الورقة.

البرامج المكتوبة بهذا الأسلوب الوظيفي يتم توزيعها وتنفيذها تلقائياً على عنقود كبير من الأجهزة التجارية. يتولى نظام وقت التشغيل تفاصيل تقسيم بيانات الإدخال، وجدولة تنفيذ البرنامج عبر مجموعة من الأجهزة، والتعامل مع فشل الأجهزة، وإدارة الاتصال المطلوب بين الأجهزة. هذا يسمح للمبرمجين الذين ليس لديهم أي خبرة في الأنظمة المتوازية والموزعة باستخدام موارد نظام موزع كبير بسهولة.

يعمل تطبيقنا لـ MapReduce على عنقود كبير من الأجهزة التجارية وقابل للتوسع بشكل كبير: حساب MapReduce النموذجي يعالج العديد من التيرابايتات من البيانات على آلاف الأجهزة. يجد المبرمجون أن النظام سهل الاستخدام: تم تطبيق مئات من برامج MapReduce ويتم تنفيذ أكثر من ألف وظيفة MapReduce على عناقيد Google يومياً.

---

### Translation Notes

- **Key terms:**
  - "programming model": نموذج برمجي
  - "map function": دالة map (kept technical term in English)
  - "reduce function": دالة reduce (kept technical term in English)
  - "cluster": عنقود/عناقيد
  - "commodity machines": الأجهزة التجارية (off-the-shelf computers)
  - "distributed system": نظام موزع
  - "parallelized": يتم توزيعها (automatically distributed)

- **Style notes:**
  - Maintained formal academic Arabic style
  - Kept "MapReduce", "map", and "reduce" as technical terms in English (standard practice)
  - Used plural forms appropriately (أجهزة for machines, عناقيد for clusters)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.95
- Readability: 0.88
- Glossary consistency: 0.92
- **Overall section score:** 0.90

### Back-Translation Check

MapReduce is a programming model and associated implementation for processing and generating large datasets. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key. Many real-world tasks can be expressed in this model, as shown in the paper.

Programs written in this functional style are automatically distributed and executed on a large cluster of commodity machines. The runtime system handles the details of input data partitioning, scheduling program execution across a set of machines, handling machine failures, and managing required inter-machine communication. This allows programmers with no experience in parallel and distributed systems to easily use the resources of a large distributed system.

Our MapReduce implementation runs on a large cluster of commodity machines and is highly scalable: a typical MapReduce computation processes many terabytes of data on thousands of machines. Programmers find the system easy to use: hundreds of MapReduce programs have been implemented and more than a thousand MapReduce jobs are executed on Google clusters daily.
