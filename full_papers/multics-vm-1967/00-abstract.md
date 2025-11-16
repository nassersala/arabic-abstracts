# Section 0: Summary
## القسم 0: الملخص

**Section:** abstract/summary
**Translation Quality:** 0.91
**Glossary Terms Used:** virtual memory, process, address space, segment, paging, segmentation, memory management, sharing, operating system, multiprogramming, protection, file system, hierarchy, dynamic linking

---

### English Version

The value of a computer system to its users is greatly enhanced if a user can, in a simple and general way, build his work upon procedures developed by others. The attainment of this essential generality requires that a computer system possess the features of equipment-independent addressing, an effectively infinite virtual memory, and provision for the dynamic linking of shared procedure and data objects. The paper explains how these features are realized in the Multics system.

The MULTICS system implements a single-level storage system using paged, segmented virtual memory. Programs reference a virtual memory that may be many times larger than the available physical memory. The system provides each process with a large virtual address space divided into segments of variable length. Segments serve as the basis for naming, protection, and dynamic linking. A segment may be shared among several processes, allowing efficient inter-process communication and shared access to procedures and data. The virtual memory system combines segmentation and paging: segments provide logical modularity and sharing granularity, while paging provides efficient memory utilization and simplified allocation. The file system and virtual memory are unified - files are simply segments that persist across process lifetimes. This design eliminates the traditional distinction between primary and secondary storage, presenting programmers with a uniform storage hierarchy managed automatically by the system.

---

### النسخة العربية

تتعزز قيمة نظام الحاسوب لمستخدميه بشكل كبير إذا كان بإمكان المستخدم، بطريقة بسيطة وعامة، أن يبني عمله على الإجراءات التي طورها آخرون. يتطلب تحقيق هذه العمومية الأساسية أن يمتلك نظام الحاسوب ميزات العنونة المستقلة عن المعدات، وذاكرة افتراضية فعالة لا نهائية، وتوفير الربط الديناميكي لكائنات الإجراءات والبيانات المشتركة. تشرح هذه الورقة كيفية تحقيق هذه الميزات في نظام مَلتِكس.

يُطبِّق نظام مَلتِكس نظام تخزين أحادي المستوى باستخدام ذاكرة افتراضية مجزأة ومقسَّمة إلى صفحات. تشير البرامج إلى ذاكرة افتراضية قد تكون أكبر بعدة مرات من الذاكرة الفيزيائية المتاحة. يوفر النظام لكل عملية فضاء عنونة افتراضي كبير مقسَّم إلى مقاطع ذات طول متغير. تعمل المقاطع كأساس للتسمية والحماية والربط الديناميكي. يمكن مشاركة مقطع بين عدة عمليات، مما يتيح اتصالاً فعالاً بين العمليات ووصولاً مشتركاً إلى الإجراءات والبيانات. يجمع نظام الذاكرة الافتراضية بين التجزئة والترحيل: توفر المقاطع النمطية المنطقية ودقة المشاركة، بينما يوفر الترحيل استخداماً فعالاً للذاكرة وتخصيصاً مُبسَّطاً. نظام الملفات والذاكرة الافتراضية موحَّدان - فالملفات ببساطة هي مقاطع تستمر عبر أعمار العمليات. يلغي هذا التصميم التمييز التقليدي بين التخزين الأساسي والثانوي، ويقدم للمبرمجين تسلسلاً هرمياً موحداً للتخزين تديره المنظومة تلقائياً.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Virtual memory of a Multics process)
- **Key terms introduced:**
  - Generalized address (عنوان معمم)
  - Segment (مقطع)
  - Pure procedure (إجراء نقي)
  - Dynamic linking (الربط الديناميكي)
  - Single-level storage (تخزين أحادي المستوى)
  - Traffic controller (متحكم الحركة)
- **Equations:** None in summary
- **Citations:** None in summary
- **Special handling:** MULTICS acronym transliterated as مَلتِكس

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.91

### Back-Translation Check

The MULTICS system implements a single-level storage system using paged and segmented virtual memory. Programs reference virtual memory that may be several times larger than available physical memory. The system provides each process with a large virtual address space divided into segments of variable length. Segments serve as the basis for naming, protection, and dynamic linking. A segment can be shared among multiple processes, enabling efficient inter-process communication and shared access to procedures and data. The virtual memory system combines segmentation and paging: segments provide logical modularity and sharing granularity, while paging provides efficient memory utilization and simplified allocation. The file system and virtual memory are unified - files are simply segments that persist across process lifetimes. This design eliminates the traditional distinction between primary and secondary storage, presenting programmers with a unified storage hierarchy managed automatically by the system.

**Validation:** ✓ Back-translation preserves all key concepts and technical details.
