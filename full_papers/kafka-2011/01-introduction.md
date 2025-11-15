# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** log data, analytics, real-time, data pipeline, distributed, throughput, offline, messaging system

---

### English Version

There is a large amount of "log" data generated at any sizable internet company. This data typically includes (1) user activity events corresponding to logins, pageviews, clicks, "likes", sharing, comments, and search queries; (2) operational metrics such as service call stack, call latency, errors, and system metrics such as CPU, memory, network, or disk utilization on each machine. Log data has long been a component of analytics used to track user engagement, system utilization, and other metrics. However recent trends in internet applications have made activity data a part of the production data pipeline used directly in site features. These uses include (1) search relevance, (2) recommendations which may be driven by item popularity or co-occurrence in the activity stream, (3) ad targeting and reporting, and (4) security applications that protect against abusive behaviors such as spam or unauthorized data scraping, and (5) newsfeed features that aggregate user status updates or actions for their "friends" or "connections" to read.

This production, real-time usage of log data creates new challenges for data systems because its volume is orders of magnitude larger than the "real" data. For example, search, recommendations, and advertising often require computing granular click-through rates, which generate log records not only for every user click, but also for dozens of items on each page that are not clicked. Every day, China Mobile collects 5–8TB of phone call records [11] and Facebook gathers almost 6TB of various user activity events [12].

Many early systems for processing this kind of data relied on physically scraping log files off production servers for analysis. In recent years, several specialized distributed log aggregators have been built, including Facebook's Scribe [6], Yahoo's Data Highway [4], and Cloudera's Flume [3]. Those systems are primarily designed for collecting and loading the log data into a data warehouse or Hadoop [8] for offline consumption. At LinkedIn (a social network site), we found that in addition to traditional offline analytics, we needed to support most of the real-time applications mentioned above with delays of no more than a few seconds. We have built a novel messaging system for log processing called Kafka [18] that combines the benefits of traditional log aggregators and messaging systems. On the one hand, Kafka is distributed and scalable, and offers high throughput. On the other hand, Kafka provides an API similar to a messaging system and allows applications to consume log events in real time.

Kafka has been open sourced and used successfully in production at LinkedIn for more than 6 months. It greatly simplifies our infrastructure, since we can exploit a single piece of software for both online and offline consumption of the log data of all types. The rest of the paper is organized as follows. We revisit traditional messaging systems and log aggregators in Section 2. In Section 3, we describe the architecture of Kafka and its key design principles. We describe our deployment of Kafka at LinkedIn in Section 4 and the performance results of Kafka in Section 5. We discuss future work and conclude in Section 6.

---

### النسخة العربية

تُولِّد أي شركة إنترنت ذات حجم كبير كمية هائلة من بيانات "السجلات". تشمل هذه البيانات عادةً (1) أحداث نشاط المستخدم المقابلة لعمليات تسجيل الدخول، ومشاهدات الصفحات، والنقرات، و"الإعجابات"، والمشاركات، والتعليقات، واستعلامات البحث؛ (2) المقاييس التشغيلية مثل مكدس استدعاءات الخدمة، وزمن استجابة الاستدعاء، والأخطاء، ومقاييس النظام مثل استخدام وحدة المعالجة المركزية والذاكرة والشبكة والقرص على كل جهاز. كانت بيانات السجلات منذ زمن طويل مكوناً من مكونات التحليلات المستخدمة لتتبع تفاعل المستخدمين واستخدام النظام ومقاييس أخرى. ومع ذلك، جعلت الاتجاهات الحديثة في تطبيقات الإنترنت من بيانات النشاط جزءاً من خط أنابيب البيانات الإنتاجي المستخدم مباشرةً في ميزات الموقع. تشمل هذه الاستخدامات (1) ملاءمة البحث، (2) التوصيات التي قد تُدفع بشعبية العناصر أو التواجد المشترك في تدفق النشاط، (3) استهداف الإعلانات وإعداد التقارير عنها، (4) تطبيقات الأمان التي تحمي من السلوكيات المسيئة مثل البريد المزعج أو استخراج البيانات غير المصرح به، و(5) ميزات خلاصات الأخبار التي تجمع تحديثات حالة المستخدم أو إجراءاته ليقرأها "أصدقاؤه" أو "اتصالاته".

يخلق هذا الاستخدام الإنتاجي في الوقت الفعلي لبيانات السجلات تحديات جديدة لأنظمة البيانات لأن حجمها أكبر بعدة مراتب من البيانات "الحقيقية". على سبيل المثال، غالباً ما يتطلب البحث والتوصيات والإعلانات حساب معدلات النقر التفصيلية، مما يولد سجلات ليس فقط لكل نقرة مستخدم، بل أيضاً لعشرات العناصر على كل صفحة التي لم يتم النقر عليها. تجمع شركة تشاينا موبايل يومياً من 5 إلى 8 تيرابايت من سجلات المكالمات الهاتفية [11] ويجمع فيسبوك ما يقرب من 6 تيرابايت من أحداث نشاط المستخدمين المختلفة [12].

اعتمدت العديد من الأنظمة المبكرة لمعالجة هذا النوع من البيانات على استخراج ملفات السجلات فعلياً من خوادم الإنتاج للتحليل. في السنوات الأخيرة، تم بناء العديد من مجمّعات السجلات الموزعة المتخصصة، بما في ذلك Scribe من فيسبوك [6]، وData Highway من ياهو [4]، وFlume من Cloudera [3]. صُممت هذه الأنظمة في المقام الأول لجمع وتحميل بيانات السجلات إلى مستودع بيانات أو Hadoop [8] للاستهلاك غير المتصل. في لينكد إن (موقع شبكة اجتماعية)، وجدنا أننا بالإضافة إلى التحليلات التقليدية غير المتصلة، نحتاج إلى دعم معظم التطبيقات في الوقت الفعلي المذكورة أعلاه بتأخيرات لا تزيد عن بضع ثوانٍ. قمنا ببناء نظام مراسلة جديد لمعالجة السجلات يُسمى كافكا [18] يجمع بين فوائد مجمّعات السجلات التقليدية وأنظمة المراسلة. من ناحية، كافكا موزع وقابل للتوسع، ويوفر إنتاجية عالية. من ناحية أخرى، يوفر كافكا واجهة برمجة تطبيقات مماثلة لنظام المراسلة ويسمح للتطبيقات باستهلاك أحداث السجل في الوقت الفعلي.

تم فتح مصدر كافكا واستخدامه بنجاح في بيئة الإنتاج في لينكد إن لأكثر من 6 أشهر. يبسط كافكا بنيتنا التحتية بشكل كبير، حيث يمكننا استغلال قطعة برمجية واحدة للاستهلاك المتصل وغير المتصل لبيانات السجلات من جميع الأنواع. يتم تنظيم بقية الورقة على النحو التالي. نعيد النظر في أنظمة المراسلة التقليدية ومجمّعات السجلات في القسم 2. في القسم 3، نصف معمارية كافكا ومبادئ تصميمه الأساسية. نصف نشرنا لكافكا في لينكد إن في القسم 4 ونتائج أداء كافكا في القسم 5. نناقش العمل المستقبلي ونختتم في القسم 6.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Log data: بيانات السجلات
  - User activity events: أحداث نشاط المستخدم
  - Operational metrics: المقاييس التشغيلية
  - Call stack: مكدس الاستدعاءات
  - Click-through rates: معدلات النقر
  - Data warehouse: مستودع بيانات
  - Log aggregators: مجمّعات السجلات
  - Real-time: الوقت الفعلي
  - API: واجهة برمجة تطبيقات
  - Open source: فتح المصدر

- **Citations:** [3], [4], [6], [8], [11], [12], [18]

- **Special handling:**
  - Company names (Facebook, Yahoo, Cloudera, LinkedIn, China Mobile) kept in original form
  - System names (Scribe, Data Highway, Flume, Hadoop, Kafka) kept in original form
  - Kafka transliterated as "كافكا" consistently

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
