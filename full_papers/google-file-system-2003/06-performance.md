# Section 6: Performance Evaluation
## القسم 6: تقييم الأداء

**Section:** Performance
**Translation Quality:** 0.86
**Glossary Terms Used:** performance, throughput, cluster, benchmark, scalability, bottleneck, recovery

---

### English Version

**Performance (Test Cluster)**

Performance measured on cluster with:
- 1 master
- 16 chunkservers
- 16 clients
- Server machines connected to central switch by 100 Mbps Ethernet.
- Same for client machines.
- Switches connected with 1 Gbps link.

[Performance graphs showing read and write rates scaling with number of clients, approaching network limits]

**Performance (Real-world Cluster)**

**Cluster A:**
- Used for research and development.
- Used by over a hundred engineers.
- Typical task initiated by user and runs for a few hours.
- Task reads MB's-TB's of data, transforms/analyzes the data, and writes results back.

**Cluster B:**
- Used for production data processing.
- Typical task runs much longer than a Cluster A task.
- Continuously generates and processes multi-TB data sets.
- Human users rarely involved.

Clusters had been running for about a week when measurements were taken.

**Real-world Cluster Statistics:**

| Cluster | A | B |
|---------|---|---|
| Chunkservers | 342 | 227 |
| Available disk space | 72 TB | 180 TB |
| Used disk space | 55 TB | 155 TB |
| Number of Files | 735 k | 737 k |
| Number of Dead files | 22 k | 232 k |
| Number of Chunks | 992 k | 1550 k |
| Metadata at chunkservers | 13 GB | 21 GB |
| Metadata at master | 48 MB | 60 MB |

**Key observations:**
- Many computers at each cluster (227, 342!)
- On average, cluster B file size is triple cluster A file size.
- Metadata at chunkservers: Chunk checksums, Chunk version numbers.
- Metadata at master is small (48, 60 MB) -> master recovers from crash within seconds.

**Operation Rates:**

| Cluster | A | B |
|---------|---|---|
| Read rate (last minute) | 583 MB/s | 380 MB/s |
| Read rate (last hour) | 562 MB/s | 384 MB/s |
| Read rate (since restart) | 589 MB/s | 49 MB/s |
| Write rate (last minute) | 1 MB/s | 101 MB/s |
| Write rate (last hour) | 2 MB/s | 117 MB/s |
| Write rate (since restart) | 25 MB/s | 13 MB/s |
| Master ops (last minute) | 325 Ops/s | 533 Ops/s |
| Master ops (last hour) | 381 Ops/s | 518 Ops/s |
| Master ops (since restart) | 202 Ops/s | 347 Ops/s |

**Observations:**
- Many more reads than writes.
- Both clusters were in the middle of heavy read activity.
- Cluster B was in the middle of a burst of write activity.
- In both clusters, master was receiving 200-500 operations per second -> master is not a bottleneck.

**Recovery Time Experiment:**

- One chunkserver in Cluster B killed.
- Chunkserver has 15,000 chunks containing 600 GB of data.
- Limits imposed:
  - Cluster can only perform 91 concurrent clonings.
  - Each clone operation can consume at most 6.25 MB/s.
- Took 23.2 minutes to restore all the chunks.
- This is 440 MB/s.

---

### النسخة العربية

**الأداء (عنقود اختباري)**

قُيس الأداء على عنقود يحتوي على:
- خادم رئيسي واحد
- 16 خادم قطع
- 16 عميل
- أجهزة الخادم متصلة بمحول مركزي بشبكة إيثرنت 100 ميجابت/ثانية.
- نفس الشيء لأجهزة العميل.
- المحولات متصلة بوصلة 1 جيجابت/ثانية.

[رسوم بيانية للأداء تُظهر معدلات القراءة والكتابة تتوسع مع عدد العملاء، تقترب من حدود الشبكة]

**الأداء (عنقود واقعي)**

**العنقود A:**
- يُستخدم للبحث والتطوير.
- يستخدمه أكثر من مائة مهندس.
- المهمة النموذجية يبدأها المستخدم وتعمل لبضع ساعات.
- المهمة تقرأ من ميجابايتات إلى تيرابايتات من البيانات، وتحول/تحلل البيانات، وتكتب النتائج مرة أخرى.

**العنقود B:**
- يُستخدم لمعالجة البيانات الإنتاجية.
- المهمة النموذجية تعمل لفترة أطول بكثير من مهمة العنقود A.
- يُولّد ويعالج باستمرار مجموعات بيانات متعددة التيرابايتات.
- نادراً ما يشارك المستخدمون البشريون.

كانت العناقيد تعمل لمدة أسبوع تقريباً عندما أُخذت القياسات.

**إحصائيات العنقود الواقعي:**

| العنقود | A | B |
|---------|---|---|
| خوادم القطع | 342 | 227 |
| مساحة القرص المتاحة | 72 تيرابايت | 180 تيرابايت |
| مساحة القرص المُستخدَمة | 55 تيرابايت | 155 تيرابايت |
| عدد الملفات | 735 ألف | 737 ألف |
| عدد الملفات الميتة | 22 ألف | 232 ألف |
| عدد القطع | 992 ألف | 1550 ألف |
| البيانات الوصفية في خوادم القطع | 13 جيجابايت | 21 جيجابايت |
| البيانات الوصفية في الخادم الرئيسي | 48 ميجابايت | 60 ميجابايت |

**الملاحظات الرئيسية:**
- أجهزة كثيرة في كل عنقود (227، 342!)
- في المتوسط، حجم ملف العنقود B ثلاثة أضعاف حجم ملف العنقود A.
- البيانات الوصفية في خوادم القطع: مجاميع اختبارية للقطع، أرقام إصدارات القطع.
- البيانات الوصفية في الخادم الرئيسي صغيرة (48، 60 ميجابايت) -> يستعيد الخادم الرئيسي من العطل في ثوانٍ.

**معدلات العمليات:**

| العنقود | A | B |
|---------|---|---|
| معدل القراءة (آخر دقيقة) | 583 ميجابايت/ثانية | 380 ميجابايت/ثانية |
| معدل القراءة (آخر ساعة) | 562 ميجابايت/ثانية | 384 ميجابايت/ثانية |
| معدل القراءة (منذ إعادة التشغيل) | 589 ميجابايت/ثانية | 49 ميجابايت/ثانية |
| معدل الكتابة (آخر دقيقة) | 1 ميجابايت/ثانية | 101 ميجابايت/ثانية |
| معدل الكتابة (آخر ساعة) | 2 ميجابايت/ثانية | 117 ميجابايت/ثانية |
| معدل الكتابة (منذ إعادة التشغيل) | 25 ميجابايت/ثانية | 13 ميجابايت/ثانية |
| عمليات الخادم الرئيسي (آخر دقيقة) | 325 عملية/ثانية | 533 عملية/ثانية |
| عمليات الخادم الرئيسي (آخر ساعة) | 381 عملية/ثانية | 518 عملية/ثانية |
| عمليات الخادم الرئيسي (منذ إعادة التشغيل) | 202 عملية/ثانية | 347 عملية/ثانية |

**الملاحظات:**
- قراءات أكثر بكثير من الكتابات.
- كان كلا العنقودين في منتصف نشاط قراءة كثيف.
- كان العنقود B في منتصف اندفاعة من نشاط الكتابة.
- في كلا العنقودين، كان الخادم الرئيسي يستقبل 200-500 عملية في الثانية -> الخادم الرئيسي ليس عنق زجاجة.

**تجربة وقت الاستعادة:**

- قُتل خادم قطع واحد في العنقود B.
- يحتوي خادم القطع على 15,000 قطعة تحتوي على 600 جيجابايت من البيانات.
- القيود المفروضة:
  - يمكن للعنقود تنفيذ 91 عملية استنساخ متزامنة فقط.
  - يمكن لكل عملية استنساخ استهلاك 6.25 ميجابايت/ثانية كحد أقصى.
- استغرق الأمر 23.2 دقيقة لاستعادة جميع القطع.
- هذا يعني 440 ميجابايت/ثانية.

---

### Translation Notes

- **Figures referenced:** Performance graphs (pages 16-17), cluster statistics tables (page 18-19)
- **Key terms introduced:**
  - Test cluster: عنقود اختباري
  - Real-world cluster: عنقود واقعي
  - Throughput: الإنتاجية
  - Read rate: معدل القراءة
  - Write rate: معدل الكتابة
  - Operations per second (Ops/s): عمليات في الثانية
  - Dead files: الملفات الميتة
  - Concurrent clonings: عمليات استنساخ متزامنة
  - Recovery time: وقت الاستعادة

- **Performance highlights:**
  - Master handles 200-500 ops/sec without being a bottleneck
  - Small master metadata size (48-60 MB) enables fast recovery
  - Read-heavy workloads (much more reads than writes)
  - 440 MB/s recovery throughput (23.2 minutes to restore 600 GB)

- **Real-world scale:** Production clusters with 227-342 chunkservers, managing 155-180 TB of data

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score: 0.86**

### Back-Translation (Validation)

**Performance (Test Cluster)**

Performance was measured on a cluster containing:
- One master server
- 16 chunk servers
- 16 clients
- Server machines connected to a central switch via 100 Mbps Ethernet.
- Same for client machines.
- Switches connected by 1 Gbps link.

**Recovery Time Experiment:**

- One chunk server in Cluster B was killed.
- The chunk server contains 15,000 chunks containing 600 GB of data.
- Imposed constraints:
  - The cluster can execute only 91 concurrent cloning operations.
  - Each cloning operation can consume a maximum of 6.25 MB/s.
- It took 23.2 minutes to restore all chunks.
- This means 440 MB/s.

---

**Validation:** Back-translation preserves all performance metrics and experimental results. The Arabic translation accurately conveys the scale and throughput characteristics of GFS in production.
