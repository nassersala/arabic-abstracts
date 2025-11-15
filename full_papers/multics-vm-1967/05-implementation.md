# Section 5: Implementation and Experience
## القسم 5: التطبيق والخبرة

**Section:** implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** process, segment, page fault, descriptor segment, page table, hardware, GE-645, supervisor, kernel, system call

---

### English Version

The MULTICS system was implemented on the General Electric GE-645 computer, a machine specifically designed to support the MULTICS architecture. The implementation required close cooperation between hardware design and system software.

#### Hardware Support

The GE-645 provided several hardware features essential for MULTICS:

**Segmented Addressing**: The hardware natively supports two-component addresses (segment number, word offset). Special registers hold segment numbers, and addressing modes allow programs to form inter-segment references.

**Descriptor Segment Base Register**: A dedicated register points to the current process's descriptor segment. This allows fast access to segment descriptors without requiring the descriptor segment location to be hard-coded.

**Associative Memory**: A 16-entry associative memory caches recently used segment descriptors and page table entries. On a memory reference, the hardware first checks the associative memory. If the required descriptor or page table entry is present (an associative memory hit), the address translation proceeds immediately without accessing main memory. This dramatically reduces the overhead of two-level address translation.

**Protection and Privilege Checking**: The hardware enforces access controls by checking permission bits in segment descriptors on every memory reference. It also enforces the protection ring mechanism, preventing less privileged code from directly accessing more privileged segments.

**Fault Handling**: The hardware generates distinct faults for different exceptional conditions:
- Segment fault: Referenced segment not in memory or not known to process
- Page fault: Referenced page not in physical memory
- Bounds fault: Address beyond segment length
- Access violation: Attempt to access segment without proper permissions

Each fault type is handled by the supervisor (operating system kernel) through a well-defined fault handling mechanism.

#### Software Organization

The MULTICS supervisor is organized in layers corresponding to the protection ring structure:

**Ring 0 - The Kernel**: The innermost ring contains the core supervisor functions:
- Process management and scheduling
- Memory management and page fault handling
- Device drivers and interrupt handling
- Low-level resource allocation

**Ring 1 - System Services**: This ring contains trusted system services:
- File system operations
- I/O stream management
- Directory management
- User authentication and access control

The layered structure allows most supervisor functions to execute in Ring 1, with only the most critical and hardware-dependent operations in Ring 0. This improves system maintainability and allows more of the system to be written in high-level languages.

#### Process Structure

Each MULTICS process has several components:

**Descriptor Segment**: Contains segment descriptors for all segments known to the process. The descriptor segment is referenced on every segment access through the Descriptor Segment Base Register.

**Stack Segments**: Each protection ring has its own stack segment. When a process calls from one ring to another, execution switches to the appropriate ring's stack. This prevents less privileged code from directly accessing more privileged stack frames.

**Linkage Sections**: Each procedure segment has an associated linkage section that contains information for dynamic linking. The linkage section includes entries for external references and calling sequences for inter-segment calls.

**Known Segment Table**: A table listing all segments currently known to the process, mapping segment names to segment numbers.

#### Page Fault Handling

When a page fault occurs, the hardware traps to the supervisor. The page fault handler:

1. Identifies which segment and page caused the fault
2. Locates the page in secondary storage (using the segment's page table)
3. Selects a physical page frame to hold the incoming page (possibly evicting another page)
4. Initiates an I/O operation to read the page from disk
5. Blocks the faulting process until the I/O completes
6. Updates the page table to record the page's physical location
7. Resumes the faulting process, which retries the memory reference

The page fault mechanism is transparent to processes. A process experiencing page faults simply runs more slowly while the required pages are loaded.

#### Segment Fault Handling

Segment faults occur when a process references a segment for which it has no descriptor. The segment fault handler:

1. Determines which segment was referenced (from the fault information)
2. Resolves the segment name through the directory hierarchy
3. Checks the segment's access control list to verify the process has permission
4. Creates a segment descriptor in the process's descriptor segment
5. Initializes the segment's page table
6. Resumes the process, which retries the segment reference

Like page faults, segment faults are transparent to programs. The first reference to a new segment may be slow (due to directory lookup and permission checking), but subsequent references use the cached descriptor.

#### Performance Considerations

The two-level address translation required by segmented paging could impose significant overhead. Several optimizations make this acceptable:

**Associative Memory**: The 16-entry associative memory eliminates the need to access the descriptor segment and page tables for most memory references. With good locality of reference, hit rates of 95% or higher are typical.

**Hardware Address Formation**: The GE-645 hardware combines segment numbers and word offsets without software intervention, allowing most instructions to execute at full speed.

**Efficient Fault Handling**: The supervisor's fault handlers are highly optimized, written in assembly language for speed-critical paths.

**Sharing**: Because segments are shared, the effective memory available to each process is increased. A system with 100 processes might have 500 segments in memory, but due to sharing, this might represent the working sets of all processes combined.

#### File System Integration

The integration of the file system with virtual memory is achieved through the segment mechanism. Each file is simply a segment that persists in secondary storage. To read or write a file, a program:

1. References the file by its pathname
2. The system creates a segment descriptor for the file
3. The program accesses the file contents through ordinary memory references
4. Page faults automatically bring file pages into memory as needed
5. Modified pages are automatically written back to secondary storage

This approach eliminates the traditional distinction between files and memory. Programmers can use memory reference instructions (load, store) to access file contents, rather than explicit I/O operations. The system handles all buffering and data transfer automatically.

#### Experience and Lessons

The MULTICS implementation revealed both the power and the complexity of the design:

**Advantages Realized**:
- The single-level storage abstraction simplified programming
- Sharing reduced memory requirements significantly
- Dynamic linking enabled easy system updates
- The protection mechanisms provided strong security

**Challenges Encountered**:
- The system was complex, requiring sophisticated hardware and software
- Performance tuning required careful attention to locality and working set behavior
- The rich functionality sometimes made the system harder to understand and debug

Despite its complexity, MULTICS demonstrated that advanced virtual memory concepts could be implemented practically, paving the way for modern operating systems.

---

### النسخة العربية

تم تطبيق نظام مَلتِكس على حاسوب جنرال إلكتريك GE-645، وهو جهاز مصمم خصيصاً لدعم معمارية مَلتِكس. تطلب التطبيق تعاوناً وثيقاً بين تصميم الأجهزة وبرمجيات النظام.

#### دعم الأجهزة

قدم GE-645 عدة ميزات أجهزة ضرورية لمَلتِكس:

**العنونة المجزأة**: تدعم الأجهزة أصلاً عناوين ثنائية المكونات (رقم المقطع، إزاحة الكلمة). تحتفظ السجلات الخاصة بأرقام المقاطع، وتسمح أوضاع العنونة للبرامج بتكوين مراجع بين المقاطع.

**سجل أساس مقطع الواصفات**: يشير سجل مخصص إلى مقطع واصفات العملية الحالية. يتيح ذلك وصولاً سريعاً إلى واصفات المقاطع دون الحاجة إلى ترميز موقع مقطع الواصفات بشكل صلب.

**الذاكرة الترابطية**: ذاكرة ترابطية من 16 إدخال تخزن مؤقتاً واصفات المقاطع وإدخالات جدول الصفحات المستخدمة مؤخراً. عند مرجعية ذاكرة، تتحقق الأجهزة أولاً من الذاكرة الترابطية. إذا كان الواصف المطلوب أو إدخال جدول الصفحات موجوداً (إصابة ذاكرة ترابطية)، تستمر ترجمة العنوان فوراً دون الوصول إلى الذاكرة الرئيسية. يقلل هذا بشكل كبير من الحمل الزائد لترجمة العناوين ثنائية المستوى.

**فحص الحماية والامتياز**: تفرض الأجهزة عناصر التحكم في الوصول من خلال فحص بتات الإذن في واصفات المقاطع في كل مرجعية ذاكرة. كما تفرض آلية حلقة الحماية، مما يمنع الشفرة الأقل امتيازاً من الوصول المباشر إلى المقاطع الأكثر امتيازاً.

**معالجة الأخطاء**: تُولِّد الأجهزة أخطاء متميزة لظروف استثنائية مختلفة:
- خطأ مقطع: المقطع المشار إليه غير موجود في الذاكرة أو غير معروف للعملية
- خطأ صفحة: الصفحة المشار إليها غير موجودة في الذاكرة الفيزيائية
- خطأ حدود: العنوان يتجاوز طول المقطع
- انتهاك وصول: محاولة الوصول إلى مقطع دون الأذونات المناسبة

يتم معالجة كل نوع خطأ بواسطة المشرف (نواة نظام التشغيل) من خلال آلية معالجة أخطاء محددة جيداً.

#### تنظيم البرمجيات

يتم تنظيم مشرف مَلتِكس في طبقات تتوافق مع بنية حلقة الحماية:

**الحلقة 0 - النواة**: تحتوي الحلقة الداخلية على وظائف المشرف الأساسية:
- إدارة العمليات والجدولة
- إدارة الذاكرة ومعالجة أخطاء الصفحات
- برامج تشغيل الأجهزة ومعالجة المقاطعات
- تخصيص الموارد منخفض المستوى

**الحلقة 1 - خدمات النظام**: تحتوي هذه الحلقة على خدمات النظام الموثوقة:
- عمليات نظام الملفات
- إدارة تدفق الإدخال/الإخراج
- إدارة الدليل
- مصادقة المستخدم والتحكم في الوصول

تسمح البنية الطبقية لمعظم وظائف المشرف بالتنفيذ في الحلقة 1، مع وجود العمليات الأكثر أهمية والمعتمدة على الأجهزة فقط في الحلقة 0. يحسِّن هذا قابلية صيانة النظام ويسمح بكتابة المزيد من النظام بلغات عالية المستوى.

#### بنية العملية

لكل عملية في مَلتِكس عدة مكونات:

**مقطع الواصفات**: يحتوي على واصفات المقاطع لجميع المقاطع المعروفة للعملية. تتم الإشارة إلى مقطع الواصفات في كل وصول مقطع من خلال سجل أساس مقطع الواصفات.

**مقاطع المكدس**: لكل حلقة حماية مقطع مكدس خاص بها. عندما تستدعي عملية من حلقة إلى أخرى، ينتقل التنفيذ إلى مكدس الحلقة المناسبة. يمنع هذا الشفرة الأقل امتيازاً من الوصول المباشر إلى إطارات مكدس أكثر امتيازاً.

**أقسام الربط**: لكل مقطع إجراء قسم ربط مرتبط يحتوي على معلومات للربط الديناميكي. يتضمن قسم الربط إدخالات للمراجع الخارجية وتسلسلات الاستدعاء لاستدعاءات بين المقاطع.

**جدول المقاطع المعروفة**: جدول يسرد جميع المقاطع المعروفة حالياً للعملية، يربط أسماء المقاطع بأرقام المقاطع.

#### معالجة أخطاء الصفحات

عندما يحدث خطأ صفحة، تحبس الأجهزة إلى المشرف. معالج خطأ الصفحة:

1. يحدد المقطع والصفحة التي تسببت في الخطأ
2. يحدد موقع الصفحة في التخزين الثانوي (باستخدام جدول صفحات المقطع)
3. يختار إطار صفحة فيزيائي لاحتواء الصفحة الواردة (ربما طرد صفحة أخرى)
4. يبدأ عملية إدخال/إخراج لقراءة الصفحة من القرص
5. يحظر العملية الخاطئة حتى يكتمل الإدخال/الإخراج
6. يحدِّث جدول الصفحات لتسجيل الموقع الفيزيائي للصفحة
7. يستأنف العملية الخاطئة، التي تعيد محاولة مرجعية الذاكرة

آلية خطأ الصفحة شفافة للعمليات. تعمل العملية التي تواجه أخطاء صفحات ببطء أكبر فقط أثناء تحميل الصفحات المطلوبة.

#### معالجة أخطاء المقاطع

تحدث أخطاء المقاطع عندما تشير عملية إلى مقطع ليس لديه واصف له. معالج خطأ المقطع:

1. يحدد المقطع الذي تمت الإشارة إليه (من معلومات الخطأ)
2. يحل اسم المقطع من خلال التسلسل الهرمي للدليل
3. يتحقق من قائمة التحكم في وصول المقطع للتأكد من أن العملية لديها إذن
4. ينشئ واصف مقطع في مقطع واصفات العملية
5. يبدأ جدول صفحات المقطع
6. يستأنف العملية، التي تعيد محاولة مرجعية المقطع

مثل أخطاء الصفحات، أخطاء المقاطع شفافة للبرامج. قد تكون المرجعية الأولى لمقطع جديد بطيئة (بسبب البحث في الدليل وفحص الأذونات)، لكن المراجع اللاحقة تستخدم الواصف المخزن مؤقتاً.

#### اعتبارات الأداء

يمكن أن تفرض ترجمة العناوين ثنائية المستوى المطلوبة بواسطة الترحيل المجزأ حملاً زائداً كبيراً. تجعل عدة تحسينات هذا مقبولاً:

**الذاكرة الترابطية**: تلغي الذاكرة الترابطية المكونة من 16 إدخال الحاجة إلى الوصول إلى مقطع الواصفات وجداول الصفحات لمعظم مراجع الذاكرة. مع وجود موضعية جيدة للمرجعية، تكون معدلات الإصابة 95٪ أو أعلى نموذجية.

**تكوين عنوان الأجهزة**: تجمع أجهزة GE-645 أرقام المقاطع وإزاحات الكلمات دون تدخل البرمجيات، مما يسمح لمعظم التعليمات بالتنفيذ بسرعة كاملة.

**معالجة فعالة للأخطاء**: معالجات أخطاء المشرف محسَّنة للغاية، مكتوبة بلغة التجميع للمسارات الحرجة للسرعة.

**المشاركة**: نظراً لأن المقاطع مشتركة، فإن الذاكرة الفعالة المتاحة لكل عملية تزداد. قد يكون لنظام به 100 عملية 500 مقطع في الذاكرة، ولكن بسبب المشاركة، قد يمثل هذا مجموعات العمل لجميع العمليات مجتمعة.

#### تكامل نظام الملفات

يتحقق تكامل نظام الملفات مع الذاكرة الافتراضية من خلال آلية المقطع. كل ملف هو ببساطة مقطع يستمر في التخزين الثانوي. لقراءة أو كتابة ملف، يقوم البرنامج بـ:

1. الإشارة إلى الملف بمساره
2. ينشئ النظام واصف مقطع للملف
3. يصل البرنامج إلى محتويات الملف من خلال مراجع ذاكرة عادية
4. تجلب أخطاء الصفحات تلقائياً صفحات الملفات إلى الذاكرة حسب الحاجة
5. يتم كتابة الصفحات المعدلة تلقائياً مرة أخرى إلى التخزين الثانوي

يلغي هذا النهج التمييز التقليدي بين الملفات والذاكرة. يمكن للمبرمجين استخدام تعليمات مرجعية الذاكرة (تحميل، تخزين) للوصول إلى محتويات الملفات، بدلاً من عمليات الإدخال/الإخراج الصريحة. يتعامل النظام مع جميع التخزين المؤقت ونقل البيانات تلقائياً.

#### الخبرة والدروس

كشف تطبيق مَلتِكس عن قوة التصميم وتعقيده:

**المزايا المحققة**:
- بسَّط تجريد التخزين أحادي المستوى البرمجة
- قللت المشاركة من متطلبات الذاكرة بشكل كبير
- مكّن الربط الديناميكي من تحديثات النظام السهلة
- وفرت آليات الحماية أماناً قوياً

**التحديات المواجهة**:
- كان النظام معقداً، يتطلب أجهزة وبرمجيات متطورة
- تطلب ضبط الأداء اهتماماً دقيقاً بالموضعية وسلوك مجموعة العمل
- جعلت الوظائف الغنية أحياناً النظام أصعب في الفهم والتصحيح

على الرغم من تعقيده، أظهر مَلتِكس أن مفاهيم الذاكرة الافتراضية المتقدمة يمكن تطبيقها عملياً، مما مهد الطريق لأنظمة التشغيل الحديثة.

---

### Translation Notes

- **Figures referenced:** None explicitly
- **Key terms introduced:** associative memory hit (إصابة ذاكرة ترابطية), supervisor (المشرف), interrupt handling (معالجة المقاطعات), linkage section (قسم الربط), working set (مجموعة العمل), locality of reference (موضعية المرجعية)
- **Equations:** Hit rate percentage (95%)
- **Citations:** Reference to GE-645 hardware
- **Special handling:** Preserved the technical detail of the 16-entry associative memory and the ring-based organization

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
