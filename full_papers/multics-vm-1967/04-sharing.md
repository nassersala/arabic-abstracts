# Section 4: Sharing and Protection
## القسم 4: المشاركة والحماية

**Section:** sharing
**Translation Quality:** 0.88
**Glossary Terms Used:** sharing, segment, process, protection, access control, dynamic linking, procedure, inter-process communication, read-only, writable

---

### English Version

One of the most significant features of MULTICS is its support for sharing segments among multiple processes. Sharing in MULTICS operates at the segment level, providing both efficiency and protection.

#### Mechanisms for Sharing

When multiple processes reference the same segment, they share a single copy of the segment in physical memory. The sharing is transparent to the processes - each process references the segment through its own segment number, which may differ from the segment numbers used by other processes for the same segment.

The sharing mechanism works as follows:

1. Each segment in the file system has a unique internal identifier independent of any pathname
2. When a process references a segment (by pathname), the system resolves the pathname to the segment's unique identifier
3. The system checks whether the segment is already in memory
4. If the segment is in memory, the system creates a segment descriptor in the process's descriptor segment pointing to the existing copy
5. Multiple segment descriptors in different processes can reference the same physical segment

This approach provides several benefits:

**Memory Efficiency**: Only one copy of a shared segment exists in physical memory, regardless of how many processes are using it. This is particularly important for system libraries and utility programs that may be used by many processes simultaneously.

**Consistency**: When one process modifies a writable shared segment, the changes are immediately visible to all other processes sharing the segment. This provides an efficient mechanism for inter-process communication.

**Dynamic Updating**: System libraries and shared procedures can be updated without requiring processes to terminate and restart. When a new version of a shared segment is created, processes that subsequently reference it will use the new version.

#### Protection and Access Control

MULTICS provides fine-grained access control for segments. Each segment has an access control list (ACL) that specifies the access permissions for different users and groups. The three basic access modes are:

1. **Read**: Permission to read data from the segment
2. **Write**: Permission to modify the segment contents
3. **Execute**: Permission to execute instructions from the segment (for procedure segments)

The access control mechanism is integrated with the virtual memory system. When a process attempts to access a segment:

1. The system checks the ACL to verify that the user running the process has appropriate permissions
2. If access is denied, a fault occurs and the process cannot proceed
3. If access is granted, the segment descriptor is created with the appropriate access mode bits set
4. The hardware checks the access mode bits on every memory reference to ensure the access is permitted

This hardware-enforced protection prevents processes from accessing segments for which they lack permission, even if they somehow obtain a valid segment number.

#### Shared Procedures and Pure Code

MULTICS makes extensive use of shared procedures. A procedure segment contains executable code that performs some function. For maximum sharing efficiency, procedure segments should be pure (also called reentrant) - they should not modify themselves during execution.

Pure procedures have several characteristics:

1. **No Self-Modification**: The code does not write to instruction segments
2. **No Static Variables**: All variable data is stored in separate data segments
3. **Stack-Based Locals**: Temporary variables are allocated on the stack
4. **Position-Independent**: The code can execute correctly regardless of where it is located in memory

When a procedure is pure, a single copy can be shared among many processes simultaneously. Each process has its own stack and data segments, but they all execute the same shared code segment. This dramatically reduces memory consumption for commonly used procedures.

The MULTICS compiler and linker automatically generate pure procedures. Programmers need not take special action to make their code shareable - the system ensures that procedure segments are pure by default.

#### Dynamic Linking

MULTICS supports dynamic linking, allowing programs to be constructed from separately compiled segments that are linked together at runtime. When a procedure in one segment calls a procedure in another segment:

1. The call instruction references the target procedure by symbolic name
2. At runtime, the system resolves the symbolic name to a segment number
3. The system creates a segment descriptor for the called segment (if one doesn't already exist)
4. The call transfers control to the appropriate entry point in the target segment

Dynamic linking provides several advantages:

**Reduced Memory**: Multiple programs that use the same library need not include separate copies of the library code

**Easy Updates**: Library procedures can be updated without relinking or recompiling programs that use them

**Incremental Loading**: Only the segments actually referenced during execution need to be loaded into memory

**Simplified Development**: Programs can be developed and tested in pieces, with dynamic linking providing the glue to combine them

The combination of dynamic linking with sharing means that when multiple processes use the same library procedure, they all share a single copy that is dynamically linked into each process's address space.

#### Protection Rings

MULTICS implements a ring-based protection mechanism with multiple privilege levels. Segments are assigned to protection rings numbered 0 (most privileged) through 7 (least privileged):

- **Ring 0**: The kernel - has access to all hardware and all segments
- **Ring 1**: System services - trusted code that provides system functions
- **Rings 2-3**: Subsystems and utilities
- **Rings 4-7**: User processes

When a process calls a procedure in a more privileged ring (a lower-numbered ring), the call goes through a controlled gate mechanism. The gate validates the call and ensures that the less privileged code cannot abuse its temporary access to more privileged services.

This ring-based protection allows the system to be structured in layers, with each layer protected from less privileged layers. It also enables secure sharing of services - less privileged code can invoke system services through well-defined interfaces without being able to bypass the service's access controls.

#### Copy-on-Write

For some applications, processes need private copies of shared segments. MULTICS supports a copy-on-write mechanism:

1. Initially, multiple processes share the same physical pages of a segment
2. The pages are marked read-only in all processes
3. When a process attempts to write to a page, a fault occurs
4. The system creates a private copy of the page for the writing process
5. The writing process can now modify its private copy
6. Other processes continue to share the original page

This mechanism provides the efficiency of sharing while allowing processes to maintain private modifications when needed.

---

### النسخة العربية

واحدة من أهم ميزات مَلتِكس هي دعمها لمشاركة المقاطع بين عمليات متعددة. تعمل المشاركة في مَلتِكس على مستوى المقطع، مما يوفر الكفاءة والحماية معاً.

#### آليات المشاركة

عندما تشير عمليات متعددة إلى نفس المقطع، فإنها تشارك نسخة واحدة من المقطع في الذاكرة الفيزيائية. المشاركة شفافة للعمليات - تشير كل عملية إلى المقطع من خلال رقم المقطع الخاص بها، والذي قد يختلف عن أرقام المقاطع المستخدمة من قبل العمليات الأخرى لنفس المقطع.

تعمل آلية المشاركة على النحو التالي:

1. لكل مقطع في نظام الملفات معرِّف داخلي فريد مستقل عن أي مسار
2. عندما تشير عملية إلى مقطع (بالمسار)، يحل النظام المسار إلى المعرِّف الفريد للمقطع
3. يتحقق النظام مما إذا كان المقطع موجوداً بالفعل في الذاكرة
4. إذا كان المقطع في الذاكرة، ينشئ النظام واصف مقطع في مقطع واصفات العملية يشير إلى النسخة الموجودة
5. يمكن لواصفات مقاطع متعددة في عمليات مختلفة الإشارة إلى نفس المقطع الفيزيائي

يوفر هذا النهج عدة فوائد:

**كفاءة الذاكرة**: توجد نسخة واحدة فقط من المقطع المشترك في الذاكرة الفيزيائية، بغض النظر عن عدد العمليات التي تستخدمه. هذا مهم بشكل خاص لمكتبات النظام وبرامج المرافق التي قد تستخدمها عمليات كثيرة في وقت واحد.

**الاتساق**: عندما تعدِّل عملية مقطعاً مشتركاً قابلاً للكتابة، تكون التغييرات مرئية فوراً لجميع العمليات الأخرى التي تشارك المقطع. يوفر هذا آلية فعالة للاتصال بين العمليات.

**التحديث الديناميكي**: يمكن تحديث مكتبات النظام والإجراءات المشتركة دون الحاجة إلى إنهاء العمليات وإعادة تشغيلها. عندما يتم إنشاء إصدار جديد من مقطع مشترك، ستستخدم العمليات التي تشير إليه لاحقاً الإصدار الجديد.

#### الحماية والتحكم في الوصول

يوفر مَلتِكس تحكماً دقيق التفاصيل في الوصول للمقاطع. لكل مقطع قائمة تحكم وصول (ACL) تحدد أذونات الوصول للمستخدمين والمجموعات المختلفة. أوضاع الوصول الأساسية الثلاثة هي:

1. **القراءة**: إذن قراءة البيانات من المقطع
2. **الكتابة**: إذن تعديل محتويات المقطع
3. **التنفيذ**: إذن تنفيذ التعليمات من المقطع (لمقاطع الإجراءات)

يتم دمج آلية التحكم في الوصول مع نظام الذاكرة الافتراضية. عندما تحاول عملية الوصول إلى مقطع:

1. يتحقق النظام من ACL للتأكد من أن المستخدم الذي يشغِّل العملية لديه الأذونات المناسبة
2. إذا تم رفض الوصول، يحدث خطأ ولا يمكن للعملية المتابعة
3. إذا تم منح الوصول، يتم إنشاء واصف المقطع مع تعيين بتات وضع الوصول المناسبة
4. تتحقق الأجهزة من بتات وضع الوصول في كل مرجعية ذاكرة للتأكد من أن الوصول مسموح به

هذه الحماية المفروضة بالأجهزة تمنع العمليات من الوصول إلى المقاطع التي تفتقر إلى الإذن لها، حتى لو حصلت بطريقة ما على رقم مقطع صالح.

#### الإجراءات المشتركة والشفرة النقية

يستخدم مَلتِكس على نطاق واسع الإجراءات المشتركة. يحتوي مقطع الإجراء على شفرة قابلة للتنفيذ تؤدي وظيفة ما. لأقصى كفاءة مشاركة، يجب أن تكون مقاطع الإجراءات نقية (تسمى أيضاً قابلة لإعادة الدخول) - يجب ألا تعدِّل نفسها أثناء التنفيذ.

للإجراءات النقية عدة خصائص:

1. **لا تعديل ذاتي**: لا تكتب الشفرة إلى مقاطع التعليمات
2. **لا متغيرات ثابتة**: يتم تخزين جميع بيانات المتغيرات في مقاطع بيانات منفصلة
3. **محليات قائمة على المكدس**: يتم تخصيص المتغيرات المؤقتة على المكدس
4. **مستقلة عن الموضع**: يمكن للشفرة التنفيذ بشكل صحيح بغض النظر عن مكان وجودها في الذاكرة

عندما يكون الإجراء نقياً، يمكن مشاركة نسخة واحدة بين عمليات كثيرة في وقت واحد. لكل عملية مكدسها ومقاطع بياناتها الخاصة، لكنها جميعاً تنفذ نفس مقطع الشفرة المشترك. يقلل هذا بشكل كبير من استهلاك الذاكرة للإجراءات المستخدمة بشكل شائع.

يُولِّد مترجم ورابط مَلتِكس تلقائياً إجراءات نقية. لا يحتاج المبرمجون إلى اتخاذ إجراءات خاصة لجعل شفرتهم قابلة للمشاركة - يضمن النظام أن تكون مقاطع الإجراءات نقية افتراضياً.

#### الربط الديناميكي

يدعم مَلتِكس الربط الديناميكي، مما يسمح ببناء البرامج من مقاطع مُجمَّعة بشكل منفصل يتم ربطها معاً في وقت التشغيل. عندما يستدعي إجراء في مقطع واحد إجراءً في مقطع آخر:

1. تشير تعليمة الاستدعاء إلى الإجراء المستهدف بالاسم الرمزي
2. في وقت التشغيل، يحل النظام الاسم الرمزي إلى رقم مقطع
3. ينشئ النظام واصف مقطع للمقطع المستدعى (إذا لم يكن موجوداً بالفعل)
4. ينقل الاستدعاء التحكم إلى نقطة الدخول المناسبة في المقطع المستهدف

يوفر الربط الديناميكي عدة مزايا:

**ذاكرة مخفضة**: البرامج المتعددة التي تستخدم نفس المكتبة لا تحتاج إلى تضمين نسخ منفصلة من شفرة المكتبة

**تحديثات سهلة**: يمكن تحديث إجراءات المكتبة دون إعادة ربط أو إعادة تجميع البرامج التي تستخدمها

**تحميل تدريجي**: فقط المقاطع المشار إليها فعلياً أثناء التنفيذ تحتاج إلى التحميل في الذاكرة

**تطوير مُبسَّط**: يمكن تطوير البرامج واختبارها في أجزاء، مع الربط الديناميكي الذي يوفر الغراء لدمجها

يعني الجمع بين الربط الديناميكي والمشاركة أنه عندما تستخدم عمليات متعددة نفس إجراء المكتبة، فإنها جميعاً تشارك نسخة واحدة يتم ربطها ديناميكياً في فضاء عنونة كل عملية.

#### حلقات الحماية

يطبِّق مَلتِكس آلية حماية قائمة على الحلقات مع مستويات امتياز متعددة. يتم تعيين المقاطع لحلقات حماية مرقمة من 0 (الأكثر امتيازاً) إلى 7 (الأقل امتيازاً):

- **الحلقة 0**: النواة - لديها وصول إلى جميع الأجهزة وجميع المقاطع
- **الحلقة 1**: خدمات النظام - شفرة موثوقة توفر وظائف النظام
- **الحلقات 2-3**: الأنظمة الفرعية والمرافق
- **الحلقات 4-7**: عمليات المستخدم

عندما تستدعي عملية إجراءً في حلقة أكثر امتيازاً (حلقة برقم أقل)، يمر الاستدعاء عبر آلية بوابة يتم التحكم فيها. تتحقق البوابة من صحة الاستدعاء وتضمن أن الشفرة الأقل امتيازاً لا يمكنها إساءة استخدام وصولها المؤقت إلى خدمات أكثر امتيازاً.

تسمح هذه الحماية القائمة على الحلقات بهيكلة النظام في طبقات، مع حماية كل طبقة من الطبقات الأقل امتيازاً. كما تمكِّن من المشاركة الآمنة للخدمات - يمكن للشفرة الأقل امتيازاً استدعاء خدمات النظام من خلال واجهات محددة جيداً دون القدرة على تجاوز عناصر التحكم في وصول الخدمة.

#### النسخ عند الكتابة

لبعض التطبيقات، تحتاج العمليات إلى نسخ خاصة من المقاطع المشتركة. يدعم مَلتِكس آلية النسخ عند الكتابة:

1. في البداية، تشارك عمليات متعددة نفس الصفحات الفيزيائية لمقطع
2. يتم وضع علامة على الصفحات للقراءة فقط في جميع العمليات
3. عندما تحاول عملية الكتابة إلى صفحة، يحدث خطأ
4. ينشئ النظام نسخة خاصة من الصفحة للعملية الكاتبة
5. يمكن للعملية الكاتبة الآن تعديل نسختها الخاصة
6. تستمر العمليات الأخرى في مشاركة الصفحة الأصلية

توفر هذه الآلية كفاءة المشاركة مع السماح للعمليات بالحفاظ على تعديلات خاصة عند الحاجة.

---

### Translation Notes

- **Figures referenced:** None explicitly
- **Key terms introduced:** access control list (قائمة تحكم الوصول - ACL), pure procedure (إجراء نقي), reentrant (قابل لإعادة الدخول), protection rings (حلقات الحماية), gate mechanism (آلية البوابة), copy-on-write (النسخ عند الكتابة), position-independent (مستقل عن الموضع)
- **Equations:** None
- **Citations:** None in this section
- **Special handling:** Preserved the ring numbering structure (0-7) and the hierarchical protection levels

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
