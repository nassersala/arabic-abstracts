---
# The Google File System
## نظام ملفات جوجل

**Authors:** Sanjay Ghemawat, Howard Gobioff, Shun-Tak Leung
**Year:** 2003
**Publication:** Proceedings of the 19th ACM Symposium on Operating Systems Principles (SOSP 2003)
**DOI:** 10.1145/945445.945450
**Translation Quality:** 0.94
**Glossary Terms Used:** distributed, scalable, fault tolerance, architecture, performance, algorithm

### English Abstract
The authors designed and implemented the Google File System, a scalable distributed file system for large distributed data-intensive applications. It provides fault tolerance while running on inexpensive commodity hardware, and it delivers high aggregate performance to a large number of clients. While sharing many of the same goals as previous distributed file systems, the design has been driven by observations of application workloads and technological environment that reflect a marked departure from some earlier file system assumptions. This has led to reexamining traditional choices and exploring radically different design points. The file system successfully met their storage needs and was widely deployed within Google as the storage platform for generation and processing of data.

### الملخص العربي
صمم المؤلفون ونفذوا نظام ملفات جوجل (Google File System)، وهو نظام ملفات موزع قابل للتوسع للتطبيقات الموزعة الكبيرة كثيفة البيانات. يوفر النظام تحمل الأخطاء أثناء التشغيل على عتاد سلعي منخفض التكلفة، ويقدم أداءً إجمالياً عالياً لعدد كبير من العملاء. بينما يشترك النظام في العديد من الأهداف نفسها مع أنظمة الملفات الموزعة السابقة، فقد قادت الملاحظات لأحمال عمل التطبيقات والبيئة التقنية التصميم بما يعكس انحرافاً ملحوظاً عن بعض افتراضات أنظمة الملفات السابقة. أدى ذلك إلى إعادة فحص الخيارات التقليدية واستكشاف نقاط تصميم مختلفة جذرياً. نجح نظام الملفات في تلبية احتياجات التخزين الخاصة بهم وتم نشره على نطاق واسع داخل جوجل كمنصة تخزين لتوليد ومعالجة البيانات.

### Back-Translation (Validation)
The authors designed and implemented the Google File System, a scalable distributed file system for large distributed data-intensive applications. The system provides fault tolerance while operating on low-cost commodity hardware, and delivers high aggregate performance to a large number of clients. While the system shares many of the same goals with previous distributed file systems, observations of application workloads and the technological environment drove the design in a way that reflects a notable departure from some previous file system assumptions. This led to reexamining traditional choices and exploring radically different design points. The file system succeeded in meeting their storage needs and was widely deployed within Google as a storage platform for data generation and processing.

### Translation Metrics
- Iterations: 1
- Final Score: 0.94
- Quality: High
- Key Technical Terms: distributed file system (نظام ملفات موزع), scalable (قابل للتوسع), fault tolerance (تحمل الأخطاء), commodity hardware (عتاد سلعي), performance (أداء), workloads (أحمال عمل), storage (تخزين)

### Historical Significance
This 2003 paper from Google introduced GFS, which became the foundation for distributed file systems in the big data era. It influenced the design of Hadoop HDFS and many other large-scale storage systems. The paper demonstrated how to build reliable storage from commodity hardware, pioneering techniques for handling component failures at scale.
---
