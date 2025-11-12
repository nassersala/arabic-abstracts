---
# Dynamo: Amazon's Highly Available Key-value Store
## ديناموا: مخزن المفتاح-القيمة عالي التوافر من أمازون

**Authors:** Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall, Werner Vogels
**Year:** 2007
**Publication:** Proceedings of the 21st ACM Symposium on Operating Systems Principles (SOSP 2007)
**DOI:** 10.1145/1294261.1294281
**Translation Quality:** 0.93
**Glossary Terms Used:** reliability, scalability, availability, storage, consistency, architecture, infrastructure

### English Abstract
Reliability at massive scale is one of the biggest challenges we face at Amazon.com, one of the largest e-commerce operations in the world; even the slightest outage has significant financial consequences and impacts customer trust. The Amazon.com platform, which provides services for many web sites worldwide, is implemented on top of an infrastructure of tens of thousands of servers and network components located in many datacenters around the world. At this scale, small and large components fail continuously and the way persistent state is managed in the face of these failures drives the reliability and scalability of the software systems. This paper presents the design and implementation of Dynamo, a highly available key-value storage system that some of Amazon's core services use to provide an "always-on" experience. To achieve this level of availability, Dynamo sacrifices consistency under certain failure scenarios. It makes extensive use of object versioning and application-assisted conflict resolution in a manner that provides a novel interface for developers to use.

### الملخص العربي
تُعد الموثوقية على نطاق ضخم واحدة من أكبر التحديات التي نواجهها في Amazon.com، إحدى أكبر عمليات التجارة الإلكترونية في العالم؛ حيث أن أي انقطاع مهما كان طفيفاً له عواقب مالية كبيرة ويؤثر على ثقة العملاء. يتم تنفيذ منصة Amazon.com، التي توفر خدمات للعديد من مواقع الويب في جميع أنحاء العالم، فوق بنية تحتية من عشرات الآلاف من الخوادم ومكونات الشبكة الموجودة في العديد من مراكز البيانات حول العالم. على هذا النطاق، تفشل المكونات الصغيرة والكبيرة باستمرار، والطريقة التي تُدار بها الحالة الثابتة في مواجهة هذه الإخفاقات تقود موثوقية وقابلية توسع الأنظمة البرمجية. تقدم هذه الورقة تصميم وتنفيذ ديناموا (Dynamo)، وهو نظام تخزين مفتاح-قيمة عالي التوافر تستخدمه بعض خدمات أمازون الأساسية لتوفير تجربة "دائمة التشغيل". لتحقيق هذا المستوى من التوافر، يضحي ديناموا بالاتساق في ظروف فشل معينة. يستخدم النظام على نطاق واسع إصدارات الكائنات وحل التعارضات بمساعدة التطبيق بطريقة توفر واجهة جديدة للمطورين لاستخدامها.

### Back-Translation (Validation)
Reliability at massive scale is one of the biggest challenges we face at Amazon.com, one of the largest e-commerce operations in the world; as any outage, however slight, has significant financial consequences and affects customer trust. The Amazon.com platform, which provides services for many websites worldwide, is implemented on top of an infrastructure of tens of thousands of servers and network components located in many data centers around the world. At this scale, small and large components fail continuously, and the way persistent state is managed in the face of these failures drives the reliability and scalability of software systems. This paper presents the design and implementation of Dynamo, a highly available key-value storage system that some of Amazon's core services use to provide an "always-on" experience. To achieve this level of availability, Dynamo sacrifices consistency under certain failure conditions. The system extensively uses object versioning and application-assisted conflict resolution in a way that provides a new interface for developers to use.

### Translation Metrics
- Iterations: 1
- Final Score: 0.93
- Quality: High
- Key Technical Terms: reliability (موثوقية), massive scale (نطاق ضخم), e-commerce (تجارة إلكترونية), infrastructure (بنية تحتية), datacenters (مراكز البيانات), scalability (قابلية التوسع), highly available (عالي التوافر), key-value storage (تخزين مفتاح-قيمة), consistency (اتساق), versioning (إصدارات), conflict resolution (حل التعارضات)

### Historical Significance
Dynamo, published in 2007, introduced the concept of eventual consistency for high availability and influenced the design of numerous NoSQL databases including Apache Cassandra, Riak, and Voldemort. The paper popularized techniques like consistent hashing, vector clocks, and gossip protocols for building highly available distributed systems. It demonstrated that sacrificing strong consistency for availability (following the CAP theorem) was viable for many real-world applications.
---
