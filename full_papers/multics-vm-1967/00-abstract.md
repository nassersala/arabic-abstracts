# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** virtual memory, process, address space, segment, paging, memory management, sharing, operating system, multiprogramming, protection, file system, hierarchy

---

### English Version

The MULTICS system implements a single-level storage system using paged, segmented virtual memory. Programs reference a virtual memory that may be many times larger than the available physical memory. The system provides each process with a large virtual address space divided into segments of variable length. Segments serve as the basis for naming, protection, and dynamic linking. A segment may be shared among several processes, allowing efficient inter-process communication and shared access to procedures and data. The virtual memory system combines segmentation and paging: segments provide logical modularity and sharing granularity, while paging provides efficient memory utilization and simplified allocation. The file system and virtual memory are unified - files are simply segments that persist across process lifetimes. This design eliminates the traditional distinction between primary and secondary storage, presenting programmers with a uniform storage hierarchy managed automatically by the system.

---

### النسخة العربية

يُطبِّق نظام مَلتِكس نظام تخزين أحادي المستوى باستخدام ذاكرة افتراضية مجزأة ومقسَّمة إلى صفحات. تشير البرامج إلى ذاكرة افتراضية قد تكون أكبر بعدة مرات من الذاكرة الفيزيائية المتاحة. يوفر النظام لكل عملية فضاء عنونة افتراضي كبير مقسَّم إلى مقاطع ذات طول متغير. تعمل المقاطع كأساس للتسمية والحماية والربط الديناميكي. يمكن مشاركة مقطع بين عدة عمليات، مما يتيح اتصالاً فعالاً بين العمليات ووصولاً مشتركاً إلى الإجراءات والبيانات. يجمع نظام الذاكرة الافتراضية بين التجزئة والترحيل: توفر المقاطع النمطية المنطقية ودقة المشاركة، بينما يوفر الترحيل استخداماً فعالاً للذاكرة وتخصيصاً مُبسَّطاً. نظام الملفات والذاكرة الافتراضية موحَّدان - فالملفات ببساطة هي مقاطع تستمر عبر أعمار العمليات. يلغي هذا التصميم التمييز التقليدي بين التخزين الأساسي والثانوي، ويقدم للمبرمجين تسلسلاً هرمياً موحداً للتخزين تديره المنظومة تلقائياً.

---

### Translation Notes

- **Key terms introduced:** virtual memory, segmentation, paging, process, segment, address space, sharing, protection, dynamic linking, file system
- **Special handling:** Unified the concepts of files and memory segments, single-level storage system

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.91
- Readability: 0.90
- Glossary consistency: 0.91
- **Overall section score:** 0.91
