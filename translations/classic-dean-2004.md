---
# MapReduce: Simplified Data Processing on Large Clusters
## MapReduce: معالجة البيانات المبسطة على العناقيد الكبيرة

**Publication:** Proceedings of OSDI, pages 137-150, 2004
**Authors:** Jeff Dean, Sanjay Ghemawat
**Year:** 2004
**Domain:** Big Data/Distributed Computing
**Translation Quality:** 0.90
**Glossary Terms Used:** programming model, data processing, dataset, cluster, function, parallelization, machine failure, scheduling, communication, network, disk, distributed computing

### English Abstract
MapReduce is a programming model and an associated implementation for processing and generating large datasets that is amenable to a broad variety of real-world tasks. Users specify the computation in terms of a map and a reduce function, and the underlying runtime system automatically parallelizes the computation across large-scale clusters of machines, handles machine failures, and schedules inter-machine communication to make efficient use of the network and disks. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key. Programs written in this functional style are automatically parallelized and executed on a large cluster of commodity machines. The runtime system takes care of partitioning input data, scheduling execution, handling machine failures, and managing inter-machine communication. More than ten thousand distinct MapReduce programs have been implemented internally at Google, with an average of one hundred thousand MapReduce jobs executed daily, processing over twenty petabytes of data per day.

### الملخص العربي
MapReduce هو نموذج برمجي وتطبيق مرتبط به لمعالجة وتوليد مجموعات البيانات الكبيرة القابل للتطبيق على مجموعة واسعة من المهام الواقعية. يحدد المستخدمون الحساب من حيث دالة map ودالة reduce، ويقوم نظام وقت التشغيل الأساسي تلقائياً بتوزيع الحساب على نطاق واسع عبر عناقيد كبيرة من الأجهزة، ويتعامل مع فشل الأجهزة، ويجدول الاتصال بين الأجهزة لاستخدام الشبكة والأقراص بكفاءة. يحدد المستخدمون دالة map التي تعالج زوج مفتاح/قيمة لتوليد مجموعة من أزواج المفتاح/القيمة الوسيطة، ودالة reduce التي تدمج جميع القيم الوسيطة المرتبطة بنفس المفتاح الوسيط. البرامج المكتوبة بهذا الأسلوب الوظيفي يتم توزيعها وتنفيذها تلقائياً على عنقود كبير من الأجهزة التجارية. يتولى نظام وقت التشغيل تقسيم بيانات الإدخال، وجدولة التنفيذ، والتعامل مع فشل الأجهزة، وإدارة الاتصال بين الأجهزة. تم تطبيق أكثر من عشرة آلاف برنامج MapReduce مميز داخلياً في Google، بمتوسط مئة ألف وظيفة MapReduce يتم تنفيذها يومياً، تعالج أكثر من عشرين بيتابايت من البيانات يومياً.

### Back-Translation (Validation)
MapReduce is a programming model and associated implementation for processing and generating large datasets applicable to a wide range of real-world tasks. Users specify the computation in terms of a map function and a reduce function, and the underlying runtime system automatically distributes the computation widely across large clusters of machines, handles machine failures, and schedules inter-machine communication to efficiently use the network and disks. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key. Programs written in this functional style are automatically distributed and executed on a large cluster of commodity machines. The runtime system handles input data partitioning, execution scheduling, handling machine failures, and managing inter-machine communication. More than ten thousand distinct MapReduce programs have been implemented internally at Google, with an average of one hundred thousand MapReduce jobs executed daily, processing more than twenty petabytes of data daily.

### Translation Metrics
- Iterations: 1
- Final Score: 0.90
- Quality: High
---
