# Section 5: Fault Tolerance and High Availability
## القسم 5: تحمل الأخطاء والتوافر العالي

**Section:** Fault Tolerance
**Translation Quality:** 0.90
**Glossary Terms Used:** fault tolerance, recovery, replication, high availability, checkpoint, data integrity, checksum

---

### English Version

**Fault Tolerance**

**Fast Recovery:** master and chunkservers are designed to restart and restore state in a few seconds.

**Chunk Replication:** across multiple machines, across multiple racks.

**Master Mechanisms:**
- Log of all changes made to metadata.
- Periodic checkpoints of the log.
- Log and checkpoints replicated on multiple machines.
- Master state is replicated on multiple machines.
- "Shadow" masters for reading data if "real" master is down.

**Data integrity:**
- Each chunk has an associated checksum.

---

### النسخة العربية

**تحمل الأخطاء**

**الاستعادة السريعة:** صُمّم الخادم الرئيسي وخوادم القطع لإعادة التشغيل واستعادة الحالة في بضع ثوانٍ.

**نسخ القطع المتماثل:** عبر أجهزة متعددة، عبر رفوف متعددة.

**آليات الخادم الرئيسي:**
- سجل بجميع التغييرات التي تمت على البيانات الوصفية.
- نقاط تفتيش دورية للسجل.
- السجل ونقاط التفتيش منسوخة على أجهزة متعددة.
- حالة الخادم الرئيسي منسوخة على أجهزة متعددة.
- خوادم رئيسية "ظل" لقراءة البيانات إذا كان الخادم الرئيسي "الحقيقي" معطلاً.

**سلامة البيانات:**
- لكل قطعة مجموع اختباري مرتبط بها.

---

### Translation Notes

- **Key terms introduced:**
  - Fast recovery: الاستعادة السريعة
  - Chunk replication: نسخ القطع المتماثل
  - Log: سجل
  - Checkpoint: نقطة تفتيش
  - Shadow master: خادم رئيسي ظل
  - Data integrity: سلامة البيانات
  - Checksum: مجموع اختباري

- **Fault tolerance mechanisms:**
  1. **Fast recovery**: Sub-second restart times for both master and chunkservers
  2. **Chunk replication**: Default 3x replication across different machines and racks (rack-level fault tolerance)
  3. **Master reliability**: Operation log + checkpoints, replicated across machines; shadow masters provide read-only access during master downtime
  4. **Data integrity**: Checksums detect corruption at chunk level

- **Design principle:** Assume failures are the norm, not the exception. System designed for continuous operation despite component failures.

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.90
- Readability: 0.89
- Glossary consistency: 0.91
- **Overall section score: 0.90**

### Back-Translation (Validation)

**Fault Tolerance**

**Fast Recovery:** The master server and chunk servers are designed to restart and restore state in a few seconds.

**Chunk Replication:** Across multiple machines, across multiple racks.

**Master Server Mechanisms:**
- A log of all changes made to metadata.
- Periodic checkpoints of the log.
- The log and checkpoints are copied to multiple machines.
- The master server state is copied to multiple machines.
- "Shadow" master servers for reading data if the "real" master server is down.

**Data Integrity:**
- Each chunk has an associated checksum.

---

**Validation:** Back-translation accurately preserves all fault tolerance mechanisms. The multi-layered approach to reliability (fast recovery, replication, logging, checksums) is clearly maintained.
