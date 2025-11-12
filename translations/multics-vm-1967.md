# Virtual Memory, Processes, and Sharing in MULTICS
## الذاكرة الافتراضية والعمليات والمشاركة في مَلتِكس

**Venue:** Communications of the ACM (CACM), Vol. 10, No. 5
**Authors:** Robert C. Daley, Jack B. Dennis
**Year:** 1967
**Institution:** MIT Project MAC
**DOI:** 10.1145/363095.363139
**Pages:** 306-312
**Translation Quality:** 0.91
**Glossary Terms Used:** virtual memory, process, address space, segment, paging, memory management, sharing, operating system, multiprogramming, protection, file system, hierarchy

### English Abstract
The MULTICS system implements a single-level storage system using paged, segmented virtual memory. Programs reference a virtual memory that may be many times larger than the available physical memory. The system provides each process with a large virtual address space divided into segments of variable length. Segments serve as the basis for naming, protection, and dynamic linking. A segment may be shared among several processes, allowing efficient inter-process communication and shared access to procedures and data. The virtual memory system combines segmentation and paging: segments provide logical modularity and sharing granularity, while paging provides efficient memory utilization and simplified allocation. The file system and virtual memory are unified - files are simply segments that persist across process lifetimes. This design eliminates the traditional distinction between primary and secondary storage, presenting programmers with a uniform storage hierarchy managed automatically by the system.

### الملخص العربي
يُطبِّق نظام مَلتِكس نظام تخزين أحادي المستوى باستخدام ذاكرة افتراضية مجزأة ومقسَّمة إلى صفحات. تشير البرامج إلى ذاكرة افتراضية قد تكون أكبر بعدة مرات من الذاكرة الفيزيائية المتاحة. يوفر النظام لكل عملية فضاء عنونة افتراضي كبير مقسَّم إلى مقاطع ذات طول متغير. تعمل المقاطع كأساس للتسمية والحماية والربط الديناميكي. يمكن مشاركة مقطع بين عدة عمليات، مما يتيح اتصالاً فعالاً بين العمليات ووصولاً مشتركاً إلى الإجراءات والبيانات. يجمع نظام الذاكرة الافتراضية بين التجزئة والترحيل: توفر المقاطع النمطية المنطقية ودقة المشاركة، بينما يوفر الترحيل استخداماً فعالاً للذاكرة وتخصيصاً مُبسَّطاً. نظام الملفات والذاكرة الافتراضية موحَّدان - فالملفات ببساطة هي مقاطع تستمر عبر أعمار العمليات. يلغي هذا التصميم التمييز التقليدي بين التخزين الأساسي والثانوي، ويقدم للمبرمجين تسلسلاً هرمياً موحداً للتخزين تديره المنظومة تلقائياً.

### Back-Translation (Validation)
The MULTICS system implements a single-level storage system using paged and segmented virtual memory. Programs reference virtual memory that may be several times larger than available physical memory. The system provides each process with a large virtual address space divided into segments of variable length. Segments serve as the basis for naming, protection, and dynamic linking. A segment can be shared among multiple processes, enabling efficient inter-process communication and shared access to procedures and data. The virtual memory system combines segmentation and paging: segments provide logical modularity and sharing granularity, while paging provides efficient memory utilization and simplified allocation. The file system and virtual memory are unified - files are simply segments that persist across process lifetimes. This design eliminates the traditional distinction between primary and secondary storage, presenting programmers with a unified storage hierarchy managed automatically by the system.

### Translation Metrics
- Iterations: 1
- Final Score: 0.91
- Quality: High

### Notes
MULTICS (Multiplexed Information and Computing Service) was one of the most influential operating systems in computer science history. This paper introduced revolutionary concepts including single-level storage, segmented virtual memory, and the unification of files and memory segments. These ideas profoundly influenced UNIX, modern operating systems, and the Intel x86 architecture's segmented memory model. The translation preserves the technical precision while adapting to Arabic linguistic conventions.

### Citation Information
**Significance:** Revolutionary OS design; influenced UNIX, modern virtual memory systems, and CPU architectures
**Historical Impact:** First practical implementation of paged segmentation; pioneered concepts still used today
**Legacy:** Influenced Intel x86 segmentation, modern VM systems, capability-based security

**BibTeX:**
```
@article{daley1967virtual,
  title={Virtual memory, processes, and sharing in MULTICS},
  author={Daley, Robert C and Dennis, Jack B},
  journal={Communications of the ACM},
  volume={10},
  number={5},
  pages={306--312},
  year={1967},
  publisher={ACM}
}
```
