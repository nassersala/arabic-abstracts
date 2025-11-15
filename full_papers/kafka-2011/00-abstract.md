# Section 0: Abstract
## القسم 0: المستخلص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** log processing, distributed system, messaging system, throughput, latency, offline, online

---

### English Version

Log processing has become a critical component of the data pipeline for consumer internet companies. We introduce Kafka, a distributed messaging system that we developed for collecting and delivering high volumes of log data with low latency. Our system incorporates ideas from existing log aggregators and messaging systems, and is suitable for both offline and online message consumption. We made quite a few unconventional yet practical design choices in Kafka to make our system efficient and scalable. Our experimental results show that Kafka has superior performance when compared to two popular messaging systems. We have been using Kafka in production for some time and it is processing hundreds of gigabytes of new data each day.

**General Terms:** Management, Performance, Design, Experimentation.

**Keywords:** messaging, distributed, log processing, throughput, online.

---

### النسخة العربية

أصبحت معالجة السجلات مكوناً حاسماً في خط أنابيب البيانات للشركات المقدمة لخدمات الإنترنت للمستهلكين. نقدم كافكا، وهو نظام مراسلة موزع قمنا بتطويره لجمع وتوصيل أحجام كبيرة من بيانات السجلات بزمن استجابة منخفض. يدمج نظامنا أفكاراً من مجمّعات السجلات الموجودة وأنظمة المراسلة، وهو مناسب لاستهلاك الرسائل في كل من الوضعين غير المتصل والمتصل. اتخذنا في كافكا عدداً كبيراً من خيارات التصميم غير التقليدية لكنها عملية لجعل نظامنا فعالاً وقابلاً للتوسع. تُظهر نتائجنا التجريبية أن كافكا يتمتع بأداء متفوق مقارنةً بنظامي مراسلة شائعين. نستخدم كافكا في بيئة الإنتاج منذ فترة وهو يعالج مئات الجيجابايتات من البيانات الجديدة كل يوم.

**المصطلحات العامة:** الإدارة، الأداء، التصميم، التجريب.

**الكلمات المفتاحية:** المراسلة، الموزع، معالجة السجلات، الإنتاجية، المتصل.

---

### Translation Notes

- **Key terms introduced:**
  - Log processing: معالجة السجلات
  - Distributed messaging system: نظام مراسلة موزع
  - Kafka: كافكا (transliterated)
  - Latency: زمن استجابة
  - Offline/online consumption: الوضعين غير المتصل والمتصل
  - Throughput: إنتاجية
  - Scalable: قابل للتوسع

- **Translation decisions:**
  - "Kafka" kept as "كافكا" (transliteration) as it's a proper name
  - "Consumer internet companies" translated as "الشركات المقدمة لخدمات الإنترنت للمستهلكين" for clarity
  - "Offline" and "online" rendered as "غير المتصل" and "المتصل" respectively
  - "Production" (environment) as "بيئة الإنتاج"

- **Special handling:** Abstract is complete and self-contained

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90
