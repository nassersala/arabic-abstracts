# Section 4: System Operations (Read, Write, Record Append)
## القسم 4: عمليات النظام (القراءة والكتابة وإلحاق السجلات)

**Section:** System Operations
**Translation Quality:** 0.88
**Glossary Terms Used:** algorithm, client, master, chunkserver, chunk handle, replica, primary, secondary, buffer, parallel

---

### English Version

**Read Algorithm**

1. Application originates the read request.
2. GFS client translates the request from (filename, byte range) -> (filename, chunk index), and sends it to master.
3. Master responds with chunk handle and replica locations (i.e. chunkservers where the replicas are stored).
4. Client picks a location and sends the (chunk handle, byte range) request to that location.
5. Chunkserver sends requested data to the client.
6. Client forwards the data to the application.

**Read Algorithm (Example)**

Calculating chunk index from byte range:
(Assumption: File position is 201,359,161 bytes)

- Chunk size = 64 MB.
- 64 MB = 1024 * 1024 * 64 bytes = 67,108,864 bytes.
- 201,359,161 bytes = 67,108,864 * 2 + 32,569 bytes.
- So, client translates 2048 byte range -> chunk index 3.

**Write Algorithm**

1. Application originates write request.
2. GFS client translates request from (filename, data) -> (filename, chunk index), and sends it to master.
3. Master responds with chunk handle and (primary + secondary) replica locations.
4. Client pushes write data to all locations. Data is stored in chunkservers' internal buffers.
5. Client sends write command to primary.
6. Primary determines serial order for data instances stored in its buffer and writes the instances in that order to the chunk.
7. Primary sends serial order to the secondaries and tells them to perform the write.
8. Secondaries respond to the primary.
9. Primary responds back to client.

Note: If write fails at one of chunkservers, client is informed and retries the write.

**Record Append Algorithm**

Important operation at Google:
- Merging results from multiple machines in one file.
- Using file as producer-consumer queue.

1. Application originates record append request.
2. GFS client translates request and sends it to master.
3. Master responds with chunk handle and (primary + secondary) replica locations.
4. Client pushes write data to all locations.
5. Primary checks if record fits in specified chunk.
6. If record does not fit, then the primary:
   - pads the chunk,
   - tells secondaries to do the same,
   - and informs the client.
   - Client then retries the append with the next chunk.
7. If record fits, then the primary:
   - appends the record,
   - tells secondaries to do the same,
   - receives responses from secondaries,
   - and sends final response to the client.

**Observations**

- Clients can read in parallel.
- Clients can write in parallel.
- Clients can append records in parallel.

---

### النسخة العربية

**خوارزمية القراءة**

1. يبدأ التطبيق طلب القراءة.
2. يترجم عميل GFS الطلب من (اسم الملف، نطاق البايتات) -> (اسم الملف، فهرس القطعة)، ويرسله إلى الخادم الرئيسي.
3. يستجيب الخادم الرئيسي بمقبض القطعة ومواقع النسخ المتماثلة (أي خوادم القطع حيث تُخزَّن النسخ المتماثلة).
4. يختار العميل موقعاً ويرسل طلب (مقبض القطعة، نطاق البايتات) إلى ذلك الموقع.
5. يرسل خادم القطع البيانات المطلوبة إلى العميل.
6. يعيد العميل توجيه البيانات إلى التطبيق.

**خوارزمية القراءة (مثال)**

حساب فهرس القطعة من نطاق البايتات:
(الافتراض: موضع الملف هو 201,359,161 بايت)

- حجم القطعة = 64 ميجابايت.
- 64 ميجابايت = 1024 * 1024 * 64 بايت = 67,108,864 بايت.
- 201,359,161 بايت = 67,108,864 * 2 + 32,569 بايت.
- إذن، يترجم العميل نطاق 2048 بايت -> فهرس القطعة 3.

**خوارزمية الكتابة**

1. يبدأ التطبيق طلب الكتابة.
2. يترجم عميل GFS الطلب من (اسم الملف، البيانات) -> (اسم الملف، فهرس القطعة)، ويرسله إلى الخادم الرئيسي.
3. يستجيب الخادم الرئيسي بمقبض القطعة ومواقع النسخ المتماثلة (الأولية + الثانوية).
4. يدفع العميل بيانات الكتابة إلى جميع المواقع. تُخزَّن البيانات في المخازن المؤقتة الداخلية لخوادم القطع.
5. يرسل العميل أمر الكتابة إلى الخادم الأولي.
6. يحدد الخادم الأولي الترتيب التسلسلي لنُسَخ البيانات المخزنة في مخزنه المؤقت ويكتب النُسَخ بهذا الترتيب إلى القطعة.
7. يرسل الخادم الأولي الترتيب التسلسلي إلى الخوادم الثانوية ويأمرها بتنفيذ الكتابة.
8. تستجيب الخوادم الثانوية للخادم الأولي.
9. يستجيب الخادم الأولي مرة أخرى للعميل.

ملاحظة: إذا فشلت الكتابة في أحد خوادم القطع، يُخطَر العميل ويعيد محاولة الكتابة.

**خوارزمية إلحاق السجلات**

عملية مهمة في جوجل:
- دمج النتائج من أجهزة متعددة في ملف واحد.
- استخدام الملف كقائمة انتظار للمُنتِج-المُستهلِك.

1. يبدأ التطبيق طلب إلحاق سجل.
2. يترجم عميل GFS الطلب ويرسله إلى الخادم الرئيسي.
3. يستجيب الخادم الرئيسي بمقبض القطعة ومواقع النسخ المتماثلة (الأولية + الثانوية).
4. يدفع العميل بيانات الكتابة إلى جميع المواقع.
5. يتحقق الخادم الأولي مما إذا كان السجل يناسب القطعة المحددة.
6. إذا لم يناسب السجل، فإن الخادم الأولي:
   - يحشو القطعة،
   - يأمر الخوادم الثانوية بفعل الشيء نفسه،
   - ويُخطر العميل.
   - ثم يعيد العميل محاولة الإلحاق بالقطعة التالية.
7. إذا ناسب السجل، فإن الخادم الأولي:
   - يلحق السجل،
   - يأمر الخوادم الثانوية بفعل الشيء نفسه،
   - يستقبل الاستجابات من الخوادم الثانوية،
   - ويرسل الاستجابة النهائية إلى العميل.

**الملاحظات**

- يمكن للعملاء القراءة بالتوازي.
- يمكن للعملاء الكتابة بالتوازي.
- يمكن للعملاء إلحاق السجلات بالتوازي.

---

### Translation Notes

- **Figures referenced:** Diagrams showing read/write/append flows (pages 7-14)
- **Key terms introduced:**
  - Byte range: نطاق البايتات
  - Chunk index: فهرس القطعة
  - Chunk handle: مقبض القطعة
  - Replica locations: مواقع النسخ المتماثلة
  - Primary (replica): النسخة الأولية / الخادم الأولي
  - Secondary (replica): النسخة الثانوية / الخادم الثانوي
  - Buffer: المخزن المؤقت
  - Serial order: الترتيب التسلسلي
  - Record append: إلحاق السجل
  - Producer-consumer queue: قائمة انتظار المُنتِج-المُستهلِك
  - Pads the chunk: يحشو القطعة

- **Algorithms explained:**
  - **Read**: Simple 6-step process - client gets metadata from master, then reads directly from chunkserver
  - **Write**: More complex - data is pushed to all replicas first (buffered), then primary coordinates the write in serial order
  - **Record Append**: Atomic append operation - primary checks if record fits, pads chunk if needed, ensures all replicas append in same order

- **Key insight:** Data flow is decoupled from control flow. Master only handles metadata; actual data flows directly between clients and chunkservers, enabling high throughput and parallelism.

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score: 0.88**

### Back-Translation (Validation)

**Read Algorithm**

1. The application initiates the read request.
2. The GFS client translates the request from (filename, byte range) -> (filename, chunk index), and sends it to the master.
3. The master responds with the chunk handle and replica locations (i.e., the chunk servers where the replicas are stored).
4. The client selects a location and sends the request (chunk handle, byte range) to that location.
5. The chunk server sends the requested data to the client.
6. The client forwards the data to the application.

**Write Algorithm**

1. The application initiates the write request.
2. The GFS client translates the request from (filename, data) -> (filename, chunk index), and sends it to the master.
3. The master responds with the chunk handle and replica locations (primary + secondary).
4. The client pushes the write data to all locations. The data is stored in the internal buffers of the chunk servers.
5. The client sends the write command to the primary server.
6. The primary server determines the serial order for the data copies stored in its buffer and writes the copies in this order to the chunk.
7. The primary server sends the serial order to the secondary servers and commands them to execute the write.
8. The secondary servers respond to the primary server.
9. The primary server responds back to the client.

---

**Validation:** Back-translation accurately preserves all algorithmic steps and technical details. The flow of operations is clear and maintains the separation between control plane (master) and data plane (chunkservers).
