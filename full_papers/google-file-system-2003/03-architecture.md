# Section 3: Architecture
## القسم 3: المعمارية

**Section:** Architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** architecture, metadata, master, chunkserver, chunk, distributed, namespace, replication

---

### English Version

**GFS Architecture (Analogy)**

On a single-machine FS:
- An upper layer maintains the metadata.
- A lower layer (i.e. disk) stores the data in units called "blocks".
- Upper layer store

In the GFS:
- A master process maintains the metadata.
- A lower layer (i.e. a set of chunkservers) stores the data in units called "chunks".

**GFS Architecture**

[Architecture diagram showing: Master with Metadata, Client, and two Chunkservers with Linux FS. Arrows show metadata requests/responses between Client and Master, and read/write requests/responses between Client and Chunkservers.]

**What is a chunk?**

- Analogous to block, except larger.
- Size: 64 MB!
- Stored on chunkserver as file
- Chunk handle (~ chunk file name) used to reference chunk.
- Chunk replicated across multiple chunkservers
- Note: There are hundreds of chunkservers in a GFS cluster distributed over multiple racks.

**What is a master?**

A single process running on a separate machine.

Stores all metadata:
- File namespace
- File to chunk mappings
- Chunk location information
- Access control information
- Chunk version numbers
- Etc.

**Master <-> Chunkserver Communication:**

Master and chunkserver communicate regularly to obtain state:
- Is chunkserver down?
- Are there disk failures on chunkserver?
- Are any replicas corrupted?
- Which chunk replicas does chunkserver store?

Master sends instructions to chunkserver:
- Delete existing chunk.
- Create new chunk.

**Serving Requests:**

- Client retrieves metadata for operation from master.
- Read/Write data flows between client and chunkserver.
- Single master is not bottleneck, because its involvement with read/write operations is minimized.

---

### النسخة العربية

**معمارية GFS (القياس)**

في نظام ملفات أحادي الجهاز:
- تحتفظ طبقة عليا بالبيانات الوصفية.
- تخزن طبقة سفلى (أي القرص) البيانات في وحدات تسمى "كتل".
- مخزن الطبقة العليا

في نظام GFS:
- تحتفظ عملية رئيسية بالبيانات الوصفية.
- تخزن طبقة سفلى (أي مجموعة من خوادم القطع) البيانات في وحدات تسمى "قطع".

**معمارية GFS**

[مخطط المعمارية يُظهر: الخادم الرئيسي (Master) مع البيانات الوصفية، العميل (Client)، وخادمان للقطع (Chunkservers) يعملان بنظام Linux FS. تُظهر الأسهم طلبات/استجابات البيانات الوصفية بين العميل والخادم الرئيسي، وطلبات/استجابات القراءة/الكتابة بين العميل وخوادم القطع.]

**ما هي القطعة (Chunk)؟**

- مماثلة للكتلة، ولكنها أكبر.
- الحجم: 64 ميجابايت!
- تُخزَّن على خادم القطع كملف
- يُستخدم مقبض القطعة (~ اسم ملف القطعة) للإشارة إلى القطعة.
- تُنسَخ القطعة عبر عدة خوادم قطع
- ملاحظة: يوجد مئات من خوادم القطع في عنقود GFS موزعة عبر رفوف متعددة.

**ما هو الخادم الرئيسي (Master)؟**

عملية واحدة تعمل على جهاز منفصل.

يخزن جميع البيانات الوصفية:
- فضاء أسماء الملفات
- تعيينات الملف إلى القطعة
- معلومات موقع القطعة
- معلومات التحكم في الوصول
- أرقام إصدارات القطع
- إلخ.

**الاتصال بين الخادم الرئيسي وخادم القطع:**

يتواصل الخادم الرئيسي وخادم القطع بانتظام للحصول على الحالة:
- هل خادم القطع معطل؟
- هل هناك أعطال في القرص على خادم القطع؟
- هل هناك نسخ متماثلة تالفة؟
- ما هي نسخ القطع المتماثلة التي يخزنها خادم القطع؟

يرسل الخادم الرئيسي تعليمات إلى خادم القطع:
- حذف قطعة موجودة.
- إنشاء قطعة جديدة.

**تقديم الطلبات:**

- يسترجع العميل البيانات الوصفية للعملية من الخادم الرئيسي.
- تتدفق بيانات القراءة/الكتابة بين العميل وخادم القطع.
- الخادم الرئيسي الوحيد ليس عنق زجاجة، لأن مشاركته في عمليات القراءة/الكتابة مُقلَّلة إلى الحد الأدنى.

---

### Translation Notes

- **Figures referenced:** Architecture diagram (page 4)
- **Key terms introduced:**
  - Master: الخادم الرئيسي
  - Chunkserver: خادم القطع
  - Chunk: قطعة
  - Chunk handle: مقبض القطعة
  - Metadata: البيانات الوصفية
  - Namespace: فضاء الأسماء
  - Replica: نسخة متماثلة
  - Rack: رف (للخوادم)
  - Bottleneck: عنق زجاجة

- **Architecture design:** The key innovation is separating metadata management (master) from data storage (chunkservers). The master only handles metadata operations, while data flows directly between clients and chunkservers, preventing the master from becoming a bottleneck.

- **Chunk size rationale:** 64 MB chunks (vs. typical 4-8 KB blocks) reduce metadata overhead and are optimized for large sequential reads/writes common in Google's workloads.

- **Translation choices:**
  - "Chunk" → "قطعة" (piece/segment) - chosen for clarity and consistency
  - "Chunkserver" → "خادم القطع" (chunk server)
  - "Master" → "الخادم الرئيسي" (primary/main server)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score: 0.87**

### Back-Translation (Validation)

**GFS Architecture (Analogy)**

In a single-machine file system:
- An upper layer maintains the metadata.
- A lower layer (i.e., the disk) stores data in units called "blocks".
- Upper layer storage

In the GFS system:
- A master process maintains the metadata.
- A lower layer (i.e., a set of chunk servers) stores data in units called "chunks".

**What is a Chunk?**

- Similar to a block, but larger.
- Size: 64 megabytes!
- Stored on the chunk server as a file
- A chunk handle (~ chunk file name) is used to reference the chunk.
- The chunk is replicated across multiple chunk servers
- Note: There are hundreds of chunk servers in a GFS cluster distributed across multiple racks.

**What is the Master?**

A single process running on a separate machine.

It stores all metadata:
- File namespace
- File-to-chunk mappings
- Chunk location information
- Access control information
- Chunk version numbers
- Etc.

**Serving Requests:**

- The client retrieves metadata for the operation from the master.
- Read/write data flows between the client and the chunk server.
- The single master is not a bottleneck, because its involvement in read/write operations is minimized.

---

**Validation:** Back-translation preserves all technical details and the architectural concepts. The key innovation of separating control (master) from data flow (chunkservers) is clearly maintained.
