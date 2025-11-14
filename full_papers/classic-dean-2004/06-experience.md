# Section 6: Experience
## القسم 6: الخبرة

**Section:** Experience
**Translation Quality:** 0.87
**Glossary Terms Used:** machine learning, clustering, data mining, graph computations, indexing, production system, distributed system, fault tolerance, load balancing, prototyping

---

### English Version

## 6 Experience

We wrote the first version of the MapReduce library in February of 2003, and made significant enhancements to it in August of 2003, including the locality optimization, dynamic load balancing of task execution across worker machines, etc. Since that time, we have been pleasantly surprised at how broadly applicable the MapReduce library has been for the kinds of problems we work on. It has been used across a wide range of domains within Google, including:

- large-scale machine learning problems,
- clustering problems for the Google News and Froogle products,
- extraction of data used to produce reports of popular queries (e.g. Google Zeitgeist),
- extraction of properties of web pages for new experiments and products (e.g. extraction of geographical locations from a large corpus of web pages for localized search), and
- large-scale graph computations.

Figure 4 shows the significant growth in the number of separate MapReduce programs checked into our primary source code management system over time, from 0 in early 2003 to almost 900 separate instances as of late September 2004. MapReduce has been so successful because it makes it possible to write a simple program and run it efficiently on a thousand machines in the course of half an hour, greatly speeding up the development and prototyping cycle. Furthermore, it allows programmers who have no experience with distributed and/or parallel systems to exploit large amounts of resources easily.

At the end of each job, the MapReduce library logs statistics about the computational resources used by the job. In Table 1, we show some statistics for a subset of MapReduce jobs run at Google in August 2004.

**Table 1: MapReduce jobs run in August 2004**

| Metric | Value |
|--------|-------|
| Number of jobs | 29,423 |
| Average job completion time | 634 secs |
| Machine days used | 79,186 days |
| Input data read | 3,288 TB |
| Intermediate data produced | 758 TB |
| Output data written | 193 TB |
| Average worker machines per job | 157 |
| Average worker deaths per job | 1.2 |
| Average map tasks per job | 3,351 |
| Average reduce tasks per job | 55 |
| Unique map implementations | 395 |
| Unique reduce implementations | 269 |
| Unique map/reduce combinations | 426 |

### 6.1 Large-Scale Indexing

One of our most significant uses of MapReduce to date has been a complete rewrite of the production indexing system that produces the data structures used for the Google web search service. The indexing system takes as input a large set of documents that have been retrieved by our crawling system, stored as a set of GFS files. The raw contents for these documents are more than 20 terabytes of data. The indexing process runs as a sequence of five to ten MapReduce operations. Using MapReduce (instead of the ad-hoc distributed passes in the prior version of the indexing system) has provided several benefits:

- The indexing code is simpler, smaller, and easier to understand, because the code that deals with fault tolerance, distribution and parallelization is hidden within the MapReduce library. For example, the size of one phase of the computation dropped from approximately 3800 lines of C++ code to approximately 700 lines when expressed using MapReduce.

- The performance of the MapReduce library is good enough that we can keep conceptually unrelated computations separate, instead of mixing them together to avoid extra passes over the data. This makes it easy to change the indexing process. For example, one change that took a few months to make in our old indexing system took only a few days to implement in the new system.

- The indexing process has become much easier to operate, because most of the problems caused by machine failures, slow machines, and networking hiccups are dealt with automatically by the MapReduce library without operator intervention. Furthermore, it is easy to improve the performance of the indexing process by adding new machines to the indexing cluster.

---

### النسخة العربية

## 6 الخبرة

كتبنا الإصدار الأول من مكتبة MapReduce في فبراير 2003، وقمنا بتحسينات كبيرة عليها في أغسطس 2003، بما في ذلك تحسين المحلية، وموازنة الحمل الديناميكي لتنفيذ المهام عبر أجهزة العمال، وما إلى ذلك. منذ ذلك الوقت، فوجئنا بسرور بمدى قابلية تطبيق مكتبة MapReduce على نطاق واسع على أنواع المشاكل التي نعمل عليها. تم استخدامها عبر مجموعة واسعة من المجالات داخل Google، بما في ذلك:

- مشاكل التعلم الآلي واسعة النطاق،
- مشاكل التجميع لمنتجات Google News و Froogle،
- استخراج البيانات المستخدمة لإنتاج تقارير الاستعلامات الشائعة (على سبيل المثال Google Zeitgeist)،
- استخراج خصائص صفحات الويب للتجارب والمنتجات الجديدة (على سبيل المثال استخراج المواقع الجغرافية من مدونة كبيرة من صفحات الويب للبحث المحلي)، و
- حسابات الرسوم البيانية واسعة النطاق.

يُظهر الشكل 4 النمو الكبير في عدد برامج MapReduce المنفصلة المسجلة في نظام إدارة الشفرة المصدرية الأساسي لدينا مع مرور الوقت، من 0 في أوائل 2003 إلى ما يقرب من 900 نسخة منفصلة اعتباراً من أواخر سبتمبر 2004. كانت MapReduce ناجحة للغاية لأنها تجعل من الممكن كتابة برنامج بسيط وتشغيله بكفاءة على ألف جهاز في غضون نصف ساعة، مما يسرع بشكل كبير دورة التطوير والنماذج الأولية. علاوة على ذلك، فإنه يسمح للمبرمجين الذين ليس لديهم خبرة في الأنظمة الموزعة و/أو المتوازية باستغلال كميات كبيرة من الموارد بسهولة.

في نهاية كل وظيفة، تسجل مكتبة MapReduce إحصائيات حول الموارد الحسابية المستخدمة من قبل الوظيفة. في الجدول 1، نُظهر بعض الإحصائيات لمجموعة فرعية من وظائف MapReduce التي تم تشغيلها في Google في أغسطس 2004.

**الجدول 1: وظائف MapReduce التي تم تشغيلها في أغسطس 2004**

| المقياس | القيمة |
|---------|--------|
| عدد الوظائف | 29,423 |
| متوسط وقت إكمال الوظيفة | 634 ثانية |
| أيام الأجهزة المستخدمة | 79,186 يوم |
| بيانات الإدخال المقروءة | 3,288 تيرابايت |
| البيانات الوسيطة المنتجة | 758 تيرابايت |
| بيانات الإخراج المكتوبة | 193 تيرابايت |
| متوسط أجهزة العمال لكل وظيفة | 157 |
| متوسط وفيات العمال لكل وظيفة | 1.2 |
| متوسط مهام map لكل وظيفة | 3,351 |
| متوسط مهام reduce لكل وظيفة | 55 |
| تنفيذات map فريدة | 395 |
| تنفيذات reduce فريدة | 269 |
| مجموعات map/reduce فريدة | 426 |

### 6.1 الفهرسة واسعة النطاق

أحد أهم استخداماتنا لـ MapReduce حتى الآن كانت إعادة كتابة كاملة لنظام الفهرسة الإنتاجي الذي ينتج بنى البيانات المستخدمة لخدمة البحث على الويب من Google. يأخذ نظام الفهرسة كإدخال مجموعة كبيرة من المستندات التي تم استردادها بواسطة نظام الزحف الخاص بنا، المخزنة كمجموعة من ملفات GFS. المحتويات الخام لهذه المستندات أكثر من 20 تيرابايت من البيانات. تعمل عملية الفهرسة كسلسلة من خمس إلى عشر عمليات MapReduce. قدم استخدام MapReduce (بدلاً من الممرات الموزعة المخصصة في الإصدار السابق من نظام الفهرسة) عدة فوائد:

- شفرة الفهرسة أبسط وأصغر وأسهل في الفهم، لأن الشفرة التي تتعامل مع تحمل الأخطاء والتوزيع والتوازي مخفية داخل مكتبة MapReduce. على سبيل المثال، انخفض حجم مرحلة واحدة من الحساب من حوالي 3800 سطر من شفرة C++ إلى حوالي 700 سطر عند التعبير عنها باستخدام MapReduce.

- أداء مكتبة MapReduce جيد بما يكفي بحيث يمكننا إبقاء الحسابات غير المرتبطة مفاهيمياً منفصلة، بدلاً من خلطها معاً لتجنب ممرات إضافية على البيانات. هذا يجعل من السهل تغيير عملية الفهرسة. على سبيل المثال، تغيير واحد استغرق بضعة أشهر لإجرائه في نظام الفهرسة القديم لدينا استغرق بضعة أيام فقط لتنفيذه في النظام الجديد.

- أصبحت عملية الفهرسة أسهل بكثير في التشغيل، لأن معظم المشاكل الناجمة عن أعطال الأجهزة والأجهزة البطيئة والخلل في الشبكات يتم التعامل معها تلقائياً بواسطة مكتبة MapReduce دون تدخل المشغل. علاوة على ذلك، من السهل تحسين أداء عملية الفهرسة عن طريق إضافة أجهزة جديدة إلى عنقود الفهرسة.

---

### Translation Notes

- **Real-world usage at Google:**
  - Library first written: February 2003
  - Major enhancements: August 2003
  - Growth: 0 to ~900 programs (early 2003 to Sept 2004)

- **Application domains:**
  - Machine learning → التعلم الآلي
  - Clustering → التجميع
  - Data mining → استخراج البيانات
  - Graph computations → حسابات الرسوم البيانية
  - Web indexing → فهرسة الويب

- **Production statistics (August 2004):**
  - 29,423 jobs total
  - 3,288 TB input data
  - 758 TB intermediate data
  - 193 TB output data
  - Average 157 worker machines per job
  - Average 3,351 map tasks per job

- **Indexing system benefits:**
  - Code reduction: 3,800 lines → 700 lines (C++)
  - Easier to modify: months → days for changes
  - Automatic fault tolerance and load balancing
  - Easy scalability by adding machines

- **Key terms:**
  - Prototyping cycle → دورة النماذج الأولية
  - Source code management → إدارة الشفرة المصدرية
  - Production indexing system → نظام الفهرسة الإنتاجي
  - Crawling system → نظام الزحف
  - Ad-hoc distributed passes → الممرات الموزعة المخصصة

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
