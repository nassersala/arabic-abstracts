# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** multiprogramming, time-sharing, virtual memory, process, address space, segment, file system, protection, operating system

---

### English Version

The MULTICS (Multiplexed Information and Computing Service) system is designed to provide computing service to a large community of users through time-sharing on a single computer installation. The system supports multiprogramming, allowing many users to execute programs concurrently while maintaining the illusion that each user has exclusive access to a complete computing system.

A fundamental objective of MULTICS is to provide a storage system that eliminates the distinction between files and core memory. In conventional systems, programmers must explicitly manage data movement between primary storage (core memory) and secondary storage (files on disk or tape). This two-level storage organization complicates programming and requires careful attention to data organization and transfer timing.

MULTICS addresses this problem through a single-level storage system based on virtual memory. All information is stored in segments - units of storage that can be referenced by programs. Segments may contain procedures, data structures, or entire subsystems. The system automatically manages the movement of segment contents between primary and secondary storage, making this transparent to programs.

The virtual memory mechanism provides each process with its own large address space, divided into segments of variable length. Programs reference virtual addresses, and the system automatically translates these to physical memory locations. When a referenced segment is not in primary memory, the system automatically retrieves it from secondary storage. This demand-paging mechanism allows the total virtual address space of all active processes to greatly exceed the available physical memory.

Segments serve multiple purposes in MULTICS:

1. **Naming and Addressing**: Each segment has a unique symbolic name and can be referenced through a hierarchical naming structure similar to a file system directory.

2. **Protection**: Access to segments can be controlled at a fine granularity. Each segment has an associated access control list specifying which users and processes may read, write, or execute its contents.

3. **Sharing**: Segments can be shared among multiple processes. When one process modifies a shared segment, the changes are immediately visible to other processes sharing the same segment. This provides an efficient mechanism for inter-process communication and data sharing.

4. **Dynamic Linking**: Procedure segments can reference other segments, with the actual linkage established dynamically at runtime. This allows programs to be constructed from separately compiled components and permits easy updating of shared procedure libraries.

The combination of segmentation and paging provides both logical modularity and efficient storage management. Segmentation divides the address space into logical units that correspond to program modules, data structures, and subsystems. Paging divides each segment into fixed-size pages for efficient allocation of physical memory and simplified address translation.

This paper describes the virtual memory architecture of MULTICS, the implementation of processes and segments, and the mechanisms that support efficient sharing of code and data among processes.

---

### النسخة العربية

صُمِّم نظام مَلتِكس (خدمة المعلومات والحوسبة المتعددة الإرسال) لتوفير خدمة حوسبية لمجتمع كبير من المستخدمين من خلال المشاركة الزمنية على منشأة حاسوبية واحدة. يدعم النظام البرمجة المتعددة، مما يسمح للعديد من المستخدمين بتنفيذ البرامج بشكل متزامن مع الحفاظ على وهم أن كل مستخدم لديه وصول حصري إلى نظام حوسبة كامل.

الهدف الأساسي لنظام مَلتِكس هو توفير نظام تخزين يلغي التمييز بين الملفات والذاكرة الأساسية. في الأنظمة التقليدية، يجب على المبرمجين إدارة حركة البيانات بشكل صريح بين التخزين الأساسي (الذاكرة الأساسية) والتخزين الثانوي (الملفات على القرص أو الشريط). هذا التنظيم ثنائي المستوى للتخزين يعقِّد البرمجة ويتطلب اهتماماً دقيقاً بتنظيم البيانات وتوقيت النقل.

يعالج مَلتِكس هذه المشكلة من خلال نظام تخزين أحادي المستوى يعتمد على الذاكرة الافتراضية. يتم تخزين جميع المعلومات في مقاطع - وحدات تخزين يمكن للبرامج الإشارة إليها. قد تحتوي المقاطع على إجراءات أو بنى بيانات أو أنظمة فرعية كاملة. يدير النظام تلقائياً حركة محتويات المقاطع بين التخزين الأساسي والثانوي، مما يجعل ذلك شفافاً للبرامج.

توفر آلية الذاكرة الافتراضية لكل عملية فضاء عنونة كبير خاص بها، مقسَّم إلى مقاطع ذات طول متغير. تشير البرامج إلى عناوين افتراضية، ويقوم النظام تلقائياً بترجمة هذه العناوين إلى مواقع الذاكرة الفيزيائية. عندما لا يكون المقطع المشار إليه في الذاكرة الأساسية، يقوم النظام تلقائياً باسترجاعه من التخزين الثانوي. تسمح آلية الترحيل عند الطلب هذه لإجمالي فضاء العنونة الافتراضي لجميع العمليات النشطة بأن يتجاوز بكثير الذاكرة الفيزيائية المتاحة.

تخدم المقاطع أغراضاً متعددة في مَلتِكس:

1. **التسمية والعنونة**: لكل مقطع اسم رمزي فريد ويمكن الإشارة إليه من خلال بنية تسمية هرمية مشابهة لدليل نظام الملفات.

2. **الحماية**: يمكن التحكم في الوصول إلى المقاطع بدقة عالية. لكل مقطع قائمة تحكم وصول مرتبطة تحدد المستخدمين والعمليات التي يمكنها قراءة محتوياته أو كتابتها أو تنفيذها.

3. **المشاركة**: يمكن مشاركة المقاطع بين عمليات متعددة. عندما تقوم عملية بتعديل مقطع مشترك، تكون التغييرات مرئية فوراً للعمليات الأخرى التي تشارك نفس المقطع. يوفر هذا آلية فعالة للاتصال بين العمليات ومشاركة البيانات.

4. **الربط الديناميكي**: يمكن لمقاطع الإجراءات الإشارة إلى مقاطع أخرى، مع إنشاء الربط الفعلي ديناميكياً في وقت التشغيل. يتيح ذلك بناء البرامج من مكونات مُجمَّعة بشكل منفصل ويسمح بتحديث سهل لمكتبات الإجراءات المشتركة.

يوفر الجمع بين التجزئة والترحيل النمطية المنطقية وإدارة التخزين الفعالة. تقسِّم التجزئة فضاء العنونة إلى وحدات منطقية تتوافق مع وحدات البرنامج وبنى البيانات والأنظمة الفرعية. يقسِّم الترحيل كل مقطع إلى صفحات ذات حجم ثابت لتخصيص فعال للذاكرة الفيزيائية وترجمة عنونة مُبسَّطة.

تصف هذه الورقة معمارية الذاكرة الافتراضية لنظام مَلتِكس، وتطبيق العمليات والمقاطع، والآليات التي تدعم المشاركة الفعالة للشفرة والبيانات بين العمليات.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** MULTICS (مَلتِكس), multiprogramming (البرمجة المتعددة), time-sharing (المشاركة الزمنية), single-level storage (تخزين أحادي المستوى), demand-paging (الترحيل عند الطلب), access control list (قائمة تحكم الوصول)
- **Equations:** None
- **Citations:** None in this section
- **Special handling:** Maintained the hierarchical structure of the four purposes of segments

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
