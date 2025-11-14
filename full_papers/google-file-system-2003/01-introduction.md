# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.91
**Glossary Terms Used:** distributed, scalable, fault tolerance, cluster, commodity hardware, data processing

---

### English Version

**The Google File System**

By Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung
(Presented at SOSP 2003)

**Introduction**

Google – search engine.

Applications process lots of data.

Need good file system.

Solution: Google File System (GFS).

**Motivational Facts**

- More than 15,000 commodity-class PC's.
- Multiple clusters distributed worldwide.
- Thousands of queries served per second.
- One query reads 100's of MB of data.
- One query consumes 10's of billions of CPU cycles.
- Google stores dozens of copies of the entire Web!

**Conclusion:** Need large, distributed, highly fault-tolerant file system.

---

### النسخة العربية

**نظام ملفات جوجل**

من إعداد سانجاي غيماوات، هوارد جوبيوف، وشون-تاك ليونغ
(قُدم في مؤتمر SOSP 2003)

**المقدمة**

جوجل – محرك بحث.

التطبيقات تعالج كميات كبيرة من البيانات.

نحتاج إلى نظام ملفات جيد.

الحل: نظام ملفات جوجل (GFS).

**الحقائق التحفيزية**

- أكثر من 15,000 حاسوب شخصي من الفئة السلعية.
- عناقيد متعددة موزعة في جميع أنحاء العالم.
- آلاف الاستعلامات المُقدَّمة في الثانية الواحدة.
- استعلام واحد يقرأ مئات الميجابايتات من البيانات.
- استعلام واحد يستهلك عشرات المليارات من دورات المعالج.
- تخزن جوجل عشرات النسخ من الويب بأكمله!

**الخلاصة:** نحتاج إلى نظام ملفات كبير وموزع وعالي التحمل للأخطاء.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Commodity-class PCs: حاسوب شخصي من الفئة السلعية
  - Search engine: محرك بحث
  - Cluster: عنقود
  - Query: استعلام
  - Fault-tolerant: عالي التحمل للأخطاء
  - CPU cycles: دورات المعالج

- **Technical details:** This introduction establishes the scale of Google's infrastructure (15,000+ machines, thousands of queries per second) and the motivation for building a custom distributed file system
- **Context:** Google needed to handle massive data processing workloads with commodity hardware, requiring a fundamentally different approach from traditional file systems

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.91
- Readability: 0.90
- Glossary consistency: 0.92
- **Overall section score: 0.91**

### Back-Translation (Validation)

**Google File System**

Prepared by Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung
(Presented at SOSP 2003 conference)

**Introduction**

Google – search engine.

Applications process large amounts of data.

We need a good file system.

The solution: Google File System (GFS).

**Motivational Facts**

- More than 15,000 commodity-class personal computers.
- Multiple clusters distributed worldwide.
- Thousands of queries served per second.
- One query reads hundreds of megabytes of data.
- One query consumes tens of billions of processor cycles.
- Google stores dozens of copies of the entire Web!

**Conclusion:** We need a large, distributed, highly fault-tolerant file system.

---

**Validation:** Back-translation preserves all key technical information and the motivational narrative. The Arabic translation accurately conveys the scale and requirements that drove GFS development.
