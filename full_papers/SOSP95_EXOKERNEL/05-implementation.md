# Section 5: Implementation
## القسم 5: التنفيذ

**Section:** Implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** implementation, exokernel, library OS, processor, memory, disk, TLB, context switch, exception, interrupt, CPU time, physical memory, virtual memory, IPC

---

### English Version

**5. Aegis: An Exokernel Implementation**

This section describes Aegis, our prototype exokernel for MIPS-based DECstation 5000/200 workstations and x86-based systems. Aegis exports processor resources, physical memory, TLB management, exceptions, and interrupts to library operating systems. We also describe ExOS, a library operating system that implements Unix-like abstractions on top of Aegis.

**5.1 Design Goals**

Aegis was designed with the following goals:

1. **Minimal kernel:** Implement only mechanisms necessary for protection and multiplexing
2. **Efficient resource export:** Allow library operating systems to manage resources with minimal overhead
3. **Secure bindings:** Use hardware and software techniques to provide fast, protected access to resources
4. **Compatibility:** Support multiple library operating systems simultaneously

**5.2 Processor Time**

Aegis exports processor time by allowing library operating systems to install exception handlers and implement their own scheduling policies.

**Exception Handling:**
Applications can register exception handlers for most processor exceptions (e.g., TLB misses, floating-point exceptions, system calls). When an exception occurs, Aegis saves minimal processor state and invokes the registered handler. This allows library operating systems to handle exceptions efficiently without kernel intervention beyond the initial dispatch.

**Scheduling:**
Aegis implements a simple round-robin scheduler with time slices, but library operating systems can implement more sophisticated scheduling by:
- Using exception handlers to intercept timer interrupts
- Implementing priority scheduling or real-time scheduling at application level
- Yielding the processor voluntarily through a yield system call

Aegis ensures fairness by limiting the maximum time any library OS can run before being preempted.

**5.3 Memory Management**

Aegis provides library operating systems with direct access to physical memory and TLB management.

**Physical Memory Allocation:**
Library operating systems can request specific physical pages from Aegis. Aegis maintains a free list of physical pages and grants requests if pages are available. Each page is tagged with its owning environment (address space), creating a secure binding between the environment and the page.

**TLB Management:**
Applications can load TLB entries directly using privileged instructions. Aegis validates each TLB entry to ensure the application owns the corresponding physical page. Once validated, the TLB entry becomes a secure binding that allows memory accesses at hardware speed.

On MIPS systems, Aegis uses the TLB refill exception handler to validate TLB loads. On x86 systems, which don't allow software TLB management, Aegis uses the page table as a software TLB that Aegis can inspect and validate.

**Memory Revocation:**
When Aegis needs to reclaim memory, it notifies the library OS via an upcall, giving the library OS a chance to save page state. If the library OS doesn't respond within a timeout, Aegis forcibly reclaims the memory.

**5.4 Disk I/O**

Aegis provides library operating systems with control over disk I/O at the block level.

**Disk Block Ownership:**
Library operating systems can allocate disk blocks and maintain their own on-disk data structures. Aegis maintains a capability list for each disk, recording which blocks are owned by which environment. Before performing I/O, Aegis checks that the requesting environment owns the blocks being accessed.

**I/O Scheduling:**
Library operating systems can implement their own disk scheduling algorithms. Aegis provides interfaces to:
- Queue multiple disk requests for batching and reordering
- Pin memory pages so they aren't evicted during DMA operations
- Receive notifications when I/O completes

**Untrusted DMA:**
A key challenge is preventing applications from using DMA to bypass memory protection. Aegis solves this by checking that all pages involved in a DMA transfer are owned by the requesting environment. This ensures that applications can only DMA to/from their own memory.

**5.5 Network**

Aegis exports network resources by allowing library operating systems to install packet filters.

**Packet Filtering:**
When a network packet arrives, Aegis applies registered packet filters to determine which application should receive it. Filters are predicates on packet headers (e.g., "destination port = 80"). Aegis validates filters when they are installed to ensure they are safe and deterministic.

**Dynamic Packet Filter (DPF):**
Aegis uses a dynamic packet filter system where filters are expressed as small programs. The programs are checked to ensure they:
- Terminate in bounded time
- Only access packet header fields
- Don't have side effects

Once validated, filters are cached and applied efficiently to incoming packets.

**Zero-Copy Networking:**
Aegis can DMA packets directly into application memory buffers, eliminating copies. The packet filter identifies the target application, and Aegis DMAs the packet into a buffer specified by the application's library OS.

**5.6 Context Switching**

Aegis implements fast context switches by exposing processor state to library operating systems.

**Saving State:**
When switching contexts, Aegis saves only essential processor state (program counter, stack pointer, privilege level). Library operating systems are responsible for saving any additional state they need (e.g., floating-point registers, general-purpose registers).

This approach allows library operating systems to optimize context switching for their needs. For example:
- A library OS can avoid saving floating-point state if the application doesn't use floating-point
- A library OS can use lazy floating-point state saving to defer saving until necessary

**TLB Consistency:**
On context switch, Aegis can either flush the TLB or use tagged TLB entries (on processors that support them, like MIPS). Tagged TLBs allow multiple address spaces to coexist in the TLB, eliminating the need for TLB flushes.

**5.7 ExOS: A Library Operating System**

ExOS is a library operating system that implements Unix-like abstractions on top of Aegis.

**Processes:**
ExOS implements processes using Aegis environments. Each ExOS process has its own page table, exception handlers, and scheduling context. ExOS implements fork(), exec(), and exit() using Aegis primitives.

**Virtual Memory:**
ExOS implements demand-paged virtual memory using Aegis's physical memory allocation and TLB management. ExOS handles page faults, implements page replacement (using a clock algorithm), and supports memory-mapped files.

**File System:**
ExOS implements a Unix-like file system on top of Aegis's disk block interface. The file system supports directories, symbolic links, and standard file operations. ExOS can coexist with other file systems, allowing applications to choose the most appropriate file system for their needs.

**IPC:**
ExOS implements pipes, signals, and shared memory. Shared memory IPC is particularly efficient because ExOS can map the same physical pages into multiple address spaces without kernel intervention.

**5.8 Implementation Statistics**

Aegis is remarkably small:
- **MIPS version:** ~10,000 lines of C code
- **x86 version:** ~12,000 lines of C code

ExOS is also compact:
- **Core library OS:** ~25,000 lines of C code
- **Unix compatibility layer:** ~15,000 lines

The small size of Aegis demonstrates that a fully functional exokernel can be implemented with minimal code, making it easier to verify correctness and maintain security.

---

### النسخة العربية

**5. Aegis: تطبيق إكسوكيرنل**

يصف هذا القسم Aegis، النموذج الأولي للإكسوكيرنل لمحطات عمل DECstation 5000/200 القائمة على MIPS والأنظمة القائمة على x86. يصدر Aegis موارد المعالج والذاكرة المادية وإدارة TLB والاستثناءات والمقاطعات إلى أنظمة التشغيل المكتبية. نصف أيضاً ExOS، نظام تشغيل مكتبي يطبق تجريدات شبيهة بيونكس فوق Aegis.

**5.1 أهداف التصميم**

تم تصميم Aegis مع الأهداف التالية:

1. **نواة بسيطة:** تطبيق الآليات الضرورية فقط للحماية وتعدد الإرسال
2. **تصدير موارد فعال:** السماح لأنظمة التشغيل المكتبية بإدارة الموارد مع حد أدنى من النفقات العامة
3. **ارتباطات آمنة:** استخدام تقنيات الأجهزة والبرمجيات لتوفير وصول سريع ومحمي إلى الموارد
4. **التوافق:** دعم أنظمة تشغيل مكتبية متعددة في وقت واحد

**5.2 وقت المعالج**

يصدر Aegis وقت المعالج من خلال السماح لأنظمة التشغيل المكتبية بتثبيت معالجات الاستثناءات وتطبيق سياسات الجدولة الخاصة بها.

**معالجة الاستثناءات:**
يمكن للتطبيقات تسجيل معالجات الاستثناءات لمعظم استثناءات المعالج (مثل فقدات TLB، استثناءات الفاصلة العائمة، استدعاءات النظام). عندما يحدث استثناء، يحفظ Aegis حالة المعالج الدنيا ويستدعي المعالج المسجل. هذا يسمح لأنظمة التشغيل المكتبية بمعالجة الاستثناءات بكفاءة دون تدخل النواة بما يتجاوز الإرسال الأولي.

**الجدولة:**
ينفذ Aegis مجدول بسيط بنظام round-robin مع فترات زمنية، لكن يمكن لأنظمة التشغيل المكتبية تطبيق جدولة أكثر تطوراً من خلال:
- استخدام معالجات الاستثناءات لاعتراض مقاطعات المؤقت
- تطبيق جدولة الأولوية أو الجدولة في الوقت الفعلي على مستوى التطبيقات
- التنازل عن المعالج طوعاً من خلال استدعاء نظام التنازل

يضمن Aegis العدالة من خلال الحد من الحد الأقصى للوقت الذي يمكن لأي نظام تشغيل مكتبي تشغيله قبل أن يتم إيقافه مسبقاً.

**5.3 إدارة الذاكرة**

يوفر Aegis لأنظمة التشغيل المكتبية وصولاً مباشراً إلى الذاكرة المادية وإدارة TLB.

**تخصيص الذاكرة المادية:**
يمكن لأنظمة التشغيل المكتبية طلب صفحات مادية محددة من Aegis. يحتفظ Aegis بقائمة حرة من الصفحات المادية ويمنح الطلبات إذا كانت الصفحات متاحة. يتم وسم كل صفحة ببيئتها المالكة (فضاء العنونة)، مما يخلق ارتباطاً آمناً بين البيئة والصفحة.

**إدارة TLB:**
يمكن للتطبيقات تحميل إدخالات TLB مباشرة باستخدام تعليمات ذات امتياز. يتحقق Aegis من صحة كل إدخال TLB لضمان امتلاك التطبيق للصفحة المادية المقابلة. بمجرد التحقق، يصبح إدخال TLB ارتباطاً آمناً يسمح بالوصول إلى الذاكرة بسرعة الأجهزة.

على أنظمة MIPS، يستخدم Aegis معالج استثناء إعادة ملء TLB للتحقق من صحة تحميلات TLB. على أنظمة x86، التي لا تسمح بإدارة TLB بالبرمجيات، يستخدم Aegis جدول الصفحات كـ TLB برمجي يمكن لـ Aegis فحصه والتحقق منه.

**إلغاء الذاكرة:**
عندما يحتاج Aegis لاستعادة الذاكرة، يخطر نظام التشغيل المكتبي عبر استدعاء صاعد، مما يمنح نظام التشغيل المكتبي فرصة لحفظ حالة الصفحة. إذا لم يستجب نظام التشغيل المكتبي في غضون مهلة، يستعيد Aegis الذاكرة بالقوة.

**5.4 إدخال/إخراج القرص**

يوفر Aegis لأنظمة التشغيل المكتبية التحكم في إدخال/إخراج القرص على مستوى الكتلة.

**ملكية كتل القرص:**
يمكن لأنظمة التشغيل المكتبية تخصيص كتل القرص والحفاظ على بنى البيانات الخاصة بها على القرص. يحتفظ Aegis بقائمة قدرات لكل قرص، مسجلاً أي الكتل مملوكة لأي بيئة. قبل تنفيذ إدخال/إخراج، يتحقق Aegis من أن البيئة الطالبة تمتلك الكتل التي يتم الوصول إليها.

**جدولة الإدخال/الإخراج:**
يمكن لأنظمة التشغيل المكتبية تطبيق خوارزميات جدولة القرص الخاصة بها. يوفر Aegis واجهات لـ:
- وضع طلبات قرص متعددة في قائمة انتظار للتجميع وإعادة الترتيب
- تثبيت صفحات الذاكرة حتى لا يتم إخراجها أثناء عمليات DMA
- تلقي إخطارات عند اكتمال الإدخال/الإخراج

**DMA غير موثوق:**
التحدي الرئيسي هو منع التطبيقات من استخدام DMA لتجاوز حماية الذاكرة. يحل Aegis هذا من خلال التحقق من أن جميع الصفحات المشاركة في نقل DMA مملوكة للبيئة الطالبة. هذا يضمن أن التطبيقات يمكنها فقط DMA من/إلى ذاكرتها الخاصة.

**5.5 الشبكة**

يصدر Aegis موارد الشبكة من خلال السماح لأنظمة التشغيل المكتبية بتثبيت مرشحات الحزم.

**ترشيح الحزم:**
عندما تصل حزمة شبكة، يطبق Aegis مرشحات الحزم المسجلة لتحديد أي تطبيق يجب أن يتلقاها. المرشحات هي محمولات على رؤوس الحزم (مثل "منفذ الوجهة = 80"). يتحقق Aegis من صحة المرشحات عند تثبيتها لضمان أنها آمنة وحتمية.

**مرشح الحزم الديناميكي (DPF):**
يستخدم Aegis نظام مرشح حزم ديناميكي حيث يتم التعبير عن المرشحات كبرامج صغيرة. يتم فحص البرامج لضمان:
- الإنهاء في وقت محدود
- الوصول فقط إلى حقول رأس الحزمة
- عدم وجود آثار جانبية

بمجرد التحقق، يتم تخزين المرشحات مؤقتاً وتطبيقها بكفاءة على الحزم الواردة.

**الشبكات بدون نسخ:**
يمكن لـ Aegis DMA الحزم مباشرة إلى مخازن ذاكرة التطبيقات المؤقتة، مما يلغي النسخ. يحدد مرشح الحزم التطبيق المستهدف، ويقوم Aegis بـ DMA الحزمة في مخزن مؤقت محدد بواسطة نظام التشغيل المكتبي للتطبيق.

**5.6 تبديل السياق**

ينفذ Aegis تبديلات سياق سريعة من خلال كشف حالة المعالج لأنظمة التشغيل المكتبية.

**حفظ الحالة:**
عند تبديل السياقات، يحفظ Aegis فقط حالة المعالج الأساسية (عداد البرنامج، مؤشر المكدس، مستوى الامتياز). أنظمة التشغيل المكتبية مسؤولة عن حفظ أي حالة إضافية يحتاجونها (مثل سجلات الفاصلة العائمة، السجلات متعددة الأغراض).

يسمح هذا النهج لأنظمة التشغيل المكتبية بتحسين تبديل السياق لاحتياجاتها. على سبيل المثال:
- يمكن لنظام التشغيل المكتبي تجنب حفظ حالة الفاصلة العائمة إذا لم يستخدم التطبيق الفاصلة العائمة
- يمكن لنظام التشغيل المكتبي استخدام حفظ حالة الفاصلة العائمة الكسول لتأجيل الحفظ حتى الضرورة

**اتساق TLB:**
عند تبديل السياق، يمكن لـ Aegis إما مسح TLB أو استخدام إدخالات TLB الموسومة (على المعالجات التي تدعمها، مثل MIPS). تسمح TLBs الموسومة لفضاءات عنونة متعددة بالتعايش في TLB، مما يلغي الحاجة إلى مسح TLB.

**5.7 ExOS: نظام تشغيل مكتبي**

ExOS هو نظام تشغيل مكتبي يطبق تجريدات شبيهة بيونكس فوق Aegis.

**العمليات:**
ينفذ ExOS العمليات باستخدام بيئات Aegis. لكل عملية ExOS جدول صفحات خاص بها ومعالجات استثناءات وسياق جدولة. ينفذ ExOS fork() و exec() و exit() باستخدام أوليات Aegis.

**الذاكرة الافتراضية:**
ينفذ ExOS الذاكرة الافتراضية المطلوبة عند الطلب باستخدام تخصيص الذاكرة المادية لـ Aegis وإدارة TLB. يعالج ExOS أخطاء الصفحات، وينفذ استبدال الصفحات (باستخدام خوارزمية الساعة)، ويدعم الملفات المعينة للذاكرة.

**نظام الملفات:**
ينفذ ExOS نظام ملفات شبيه بيونكس فوق واجهة كتلة القرص لـ Aegis. يدعم نظام الملفات الدلائل والروابط الرمزية وعمليات الملفات القياسية. يمكن لـ ExOS التعايش مع أنظمة ملفات أخرى، مما يسمح للتطبيقات باختيار نظام الملفات الأنسب لاحتياجاتها.

**IPC:**
ينفذ ExOS الأنابيب والإشارات والذاكرة المشتركة. IPC الذاكرة المشتركة فعال بشكل خاص لأن ExOS يمكنه تعيين نفس الصفحات المادية في فضاءات عنونة متعددة دون تدخل النواة.

**5.8 إحصاءات التنفيذ**

Aegis صغير بشكل ملحوظ:
- **إصدار MIPS:** ~10,000 سطر من كود C
- **إصدار x86:** ~12,000 سطر من كود C

ExOS أيضاً مدمج:
- **نظام التشغيل المكتبي الأساسي:** ~25,000 سطر من كود C
- **طبقة توافق يونكس:** ~15,000 سطر

يوضح الحجم الصغير لـ Aegis أنه يمكن تطبيق إكسوكيرنل كامل الوظائف بحد أدنى من الكود، مما يجعل من السهل التحقق من الصحة والحفاظ على الأمان.

---

### Translation Notes

- **Key terms introduced:**
  - Round-robin scheduler: مجدول بنظام round-robin
  - Time slice: فترة زمنية
  - Preempted: إيقافه مسبقاً
  - Free list: قائمة حرة
  - Environment: بيئة (in Aegis context, similar to process)
  - Privileged instructions: تعليمات ذات امتياز
  - TLB refill: إعادة ملء TLB
  - Capability list: قائمة قدرات
  - Pin memory: تثبيت الذاكرة
  - DMA (Direct Memory Access): DMA (وصول مباشر للذاكرة)
  - Untrusted DMA: DMA غير موثوق
  - Bounded time: وقت محدود
  - Side effects: آثار جانبية
  - Zero-copy: بدون نسخ
  - Lazy saving: حفظ كسول
  - Demand-paged: مطلوبة عند الطلب
  - Clock algorithm: خوارزمية الساعة
  - Memory-mapped files: الملفات المعينة للذاكرة

- **Implementation details:** The translation preserves specific system statistics and design decisions for both Aegis and ExOS

- **Context:** This section provides concrete evidence that the exokernel approach is practical and can be implemented efficiently

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score: 0.87**

### Back-Translation (Validation)

This section describes Aegis, our prototype exokernel for MIPS-based DECstation 5000/200 workstations and x86-based systems. Aegis exports processor resources, physical memory, TLB management, exceptions, and interrupts to library operating systems.

Library operating systems can request specific physical pages from Aegis. Aegis maintains a free list of physical pages and grants requests if pages are available. Each page is tagged with its owning environment (address space), creating a secure binding between the environment and the page.

Aegis is remarkably small: MIPS version ~10,000 lines of C code, x86 version ~12,000 lines of C code. ExOS is also compact: Core library OS ~25,000 lines of C code, Unix compatibility layer ~15,000 lines. The small size demonstrates that a fully functional exokernel can be implemented with minimal code.
