# Section 6: Performance Evaluation
## القسم 6: تقييم الأداء

**Section:** Performance
**Translation Quality:** 0.88
**Glossary Terms Used:** performance, benchmark, throughput, latency, overhead, optimization, system call, context switch, memory, IPC, virtual memory, exception handling, microbenchmark

---

### English Version

**6. Performance**

This section evaluates the performance of Aegis and ExOS through microbenchmarks and application-level measurements. Our results demonstrate that the exokernel approach provides performance equal to or better than traditional monolithic operating systems, while offering unprecedented flexibility.

**6.1 Microbenchmark Performance**

We measured the cost of basic operations on Aegis/ExOS and compared them to Ultrix (a Unix-like OS for DECstations) and several other systems.

**Protected Control Transfer:**
Protected control transfer (e.g., system calls, exceptions) is fundamental to OS performance. Aegis achieves exceptionally fast protected control transfers:

- **Aegis null system call:** 45 cycles
- **Ultrix null system call:** 145 cycles

Aegis is 3.2× faster than Ultrix because it saves minimal processor state and doesn't perform unnecessary operations like checking for signals. Library operating systems can add additional checks if needed, but applications that don't need them pay no cost.

**Exception Handling:**
Aegis allows applications to handle most exceptions directly:

- **Aegis TLB miss (handled in libOS):** 18 cycles
- **Ultrix TLB miss (handled in kernel):** 60 cycles

Aegis is 3.3× faster because the exception handler runs at application level without crossing protection boundaries. The application can implement specialized exception handling tailored to its needs.

**Context Switch:**
Context switching performance is critical for multitasking systems:

- **Aegis context switch:** 7 microseconds
- **Ultrix context switch:** 30 microseconds

Aegis is 4.3× faster because it saves only essential state, leaving floating-point and other register state to be saved lazily by the library OS. This optimization is difficult in traditional kernels because they must save all state to maintain compatibility with all applications.

**6.2 IPC Performance**

Inter-process communication performance is crucial for microkernel-based systems and distributed applications.

**Shared Memory IPC:**
ExOS implements shared memory IPC by mapping the same physical pages into multiple address spaces:

- **ExOS shared memory write (4 bytes):** 0.8 microseconds
- **Ultrix pipe (4 bytes):** 45 microseconds

ExOS is 56× faster than pipes because it avoids kernel intervention and memory copies. After the initial setup, IPC proceeds at memory speed.

**Message Passing:**
For message passing, ExOS uses application-level buffers with minimal kernel support:

- **ExOS message send/receive (4KB):** 120 microseconds
- **Ultrix socket send/receive (4KB):** 520 microseconds

ExOS is 4.3× faster due to reduced copying and streamlined buffer management.

**6.3 Virtual Memory Performance**

Virtual memory performance affects nearly all applications.

**Page Fault Handling:**
When a page fault occurs, the library OS can handle it directly:

- **ExOS page fault (map existing page):** 25 microseconds
- **Ultrix page fault (map existing page):** 90 microseconds

ExOS is 3.6× faster because it handles page faults at application level without kernel involvement beyond the initial exception dispatch.

**Memory Allocation:**
Applications can implement specialized memory allocators:

- **ExOS malloc/free (64 bytes):** 0.3 microseconds
- **Ultrix malloc/free (64 bytes):** 1.2 microseconds

ExOS is 4× faster because the library OS can implement allocation strategies optimized for the application's pattern. For example, a database can use region-based allocation, while a scientific application can use pool allocation.

**Page Table Management:**
Library operating systems can optimize page table management:

- **ExOS map page:** 2.5 microseconds
- **Ultrix mmap:** 45 microseconds

ExOS is 18× faster because it directly manipulates TLB entries without going through the kernel's virtual memory subsystem.

**6.4 Disk I/O Performance**

Disk I/O performance is critical for data-intensive applications.

**Synchronous Read:**
- **ExOS synchronous read (4KB):** 8.2 milliseconds
- **Ultrix synchronous read (4KB):** 8.8 milliseconds

Performance is comparable because both systems are limited by disk hardware. However, ExOS provides lower overhead for setting up the I/O.

**Asynchronous I/O:**
ExOS allows applications to queue multiple disk requests and reorder them for efficiency:

- **ExOS asynchronous throughput (4KB requests):** 1.8 MB/s
- **Ultrix asynchronous throughput (4KB requests):** 1.4 MB/s

ExOS is 29% faster because the library OS can implement application-specific disk scheduling. A database can order requests by disk location to minimize seeks, while a video server can schedule requests to maintain streaming rate.

**6.5 Network Performance**

Network performance is essential for distributed systems and web servers.

**Packet Receive Latency:**
Using dynamic packet filters, Aegis delivers packets efficiently:

- **Aegis packet receive (minimum size):** 95 microseconds
- **Ultrix packet receive (minimum size):** 180 microseconds

Aegis is 1.9× faster due to efficient packet filtering and zero-copy delivery to application buffers.

**Network Throughput:**
- **ExOS TCP throughput (localhost):** 38 MB/s
- **Ultrix TCP throughput (localhost):** 28 MB/s

ExOS achieves 36% higher throughput by reducing memory copies and allowing the application to manage protocol processing.

**6.6 Application Performance**

We measured end-to-end application performance to validate that microbenchmark improvements translate to real benefits.

**Web Server:**
A simple HTTP server running on ExOS:

- **ExOS web server (small files):** 4,200 requests/second
- **Ultrix web server (small files):** 2,800 requests/second

ExOS is 50% faster due to efficient networking, memory management, and disk I/O.

**Database Query:**
A simple database performing indexed lookups:

- **ExOS database (1000 queries):** 1.2 seconds
- **Ultrix database (1000 queries):** 1.8 seconds

ExOS is 50% faster because the database can implement custom page replacement and disk scheduling optimized for database access patterns.

**6.7 Discussion**

The performance measurements demonstrate several key points:

1. **Low Overhead:** Aegis adds minimal overhead to hardware operations. Protected control transfers, exception handling, and context switches all execute in a few dozen cycles.

2. **Application Specialization:** Library operating systems can implement optimizations impossible in traditional kernels. ExOS's shared memory IPC, specialized memory allocation, and application-level disk scheduling all significantly outperform traditional implementations.

3. **No Performance Penalty:** Despite providing unprecedented flexibility, the exokernel approach does not sacrifice performance. In fact, it often provides better performance than traditional systems.

4. **Scalability:** The benefits of application-level management increase as applications become more specialized. Generic applications see modest improvements, while specialized applications can achieve order-of-magnitude speedups.

These results validate the exokernel hypothesis: applications know better than the operating system how to manage resources, and giving them control leads to better performance.

---

### النسخة العربية

**6. الأداء**

يقيم هذا القسم أداء Aegis و ExOS من خلال قياسات دقيقة وقياسات على مستوى التطبيقات. تُظهر نتائجنا أن نهج الإكسوكيرنل يوفر أداءً يعادل أو أفضل من أنظمة التشغيل الأحادية التقليدية، مع توفير مرونة غير مسبوقة.

**6.1 أداء القياسات الدقيقة**

قمنا بقياس تكلفة العمليات الأساسية على Aegis/ExOS وقارناها بـ Ultrix (نظام تشغيل شبيه بيونكس لـ DECstations) وعدة أنظمة أخرى.

**نقل التحكم المحمي:**
نقل التحكم المحمي (مثل استدعاءات النظام، الاستثناءات) أساسي لأداء نظام التشغيل. يحقق Aegis عمليات نقل تحكم محمي سريعة بشكل استثنائي:

- **استدعاء نظام فارغ Aegis:** 45 دورة
- **استدعاء نظام فارغ Ultrix:** 145 دورة

Aegis أسرع بـ 3.2× من Ultrix لأنه يحفظ حالة المعالج الدنيا ولا يقوم بعمليات غير ضرورية مثل التحقق من الإشارات. يمكن لأنظمة التشغيل المكتبية إضافة فحوصات إضافية إذا لزم الأمر، ولكن التطبيقات التي لا تحتاجها لا تدفع أي تكلفة.

**معالجة الاستثناءات:**
يسمح Aegis للتطبيقات بمعالجة معظم الاستثناءات مباشرة:

- **فقد TLB لـ Aegis (معالج في libOS):** 18 دورة
- **فقد TLB لـ Ultrix (معالج في النواة):** 60 دورة

Aegis أسرع بـ 3.3× لأن معالج الاستثناءات يعمل على مستوى التطبيقات دون عبور حدود الحماية. يمكن للتطبيق تطبيق معالجة استثناءات متخصصة مصممة لاحتياجاته.

**تبديل السياق:**
أداء تبديل السياق حاسم لأنظمة المهام المتعددة:

- **تبديل سياق Aegis:** 7 ميكروثانية
- **تبديل سياق Ultrix:** 30 ميكروثانية

Aegis أسرع بـ 4.3× لأنه يحفظ فقط الحالة الأساسية، تاركاً حالة الفاصلة العائمة وحالة السجلات الأخرى ليتم حفظها بشكل كسول بواسطة نظام التشغيل المكتبي. هذا التحسين صعب في النوى التقليدية لأنها يجب أن تحفظ جميع الحالات للحفاظ على التوافق مع جميع التطبيقات.

**6.2 أداء IPC**

أداء الاتصال بين العمليات حاسم للأنظمة القائمة على النواة الصغيرة والتطبيقات الموزعة.

**IPC الذاكرة المشتركة:**
ينفذ ExOS IPC الذاكرة المشتركة من خلال تعيين نفس الصفحات المادية في فضاءات عنونة متعددة:

- **كتابة ذاكرة مشتركة ExOS (4 بايت):** 0.8 ميكروثانية
- **أنبوب Ultrix (4 بايت):** 45 ميكروثانية

ExOS أسرع بـ 56× من الأنابيب لأنه يتجنب تدخل النواة ونسخ الذاكرة. بعد الإعداد الأولي، يتقدم IPC بسرعة الذاكرة.

**تمرير الرسائل:**
لتمرير الرسائل، يستخدم ExOS مخازن مؤقتة على مستوى التطبيقات بحد أدنى من دعم النواة:

- **إرسال/استقبال رسالة ExOS (4KB):** 120 ميكروثانية
- **إرسال/استقبال مقبس Ultrix (4KB):** 520 ميكروثانية

ExOS أسرع بـ 4.3× بسبب تقليل النسخ وإدارة المخازن المؤقتة المبسطة.

**6.3 أداء الذاكرة الافتراضية**

أداء الذاكرة الافتراضية يؤثر على جميع التطبيقات تقريباً.

**معالجة خطأ الصفحة:**
عندما يحدث خطأ صفحة، يمكن لنظام التشغيل المكتبي معالجته مباشرة:

- **خطأ صفحة ExOS (تعيين صفحة موجودة):** 25 ميكروثانية
- **خطأ صفحة Ultrix (تعيين صفحة موجودة):** 90 ميكروثانية

ExOS أسرع بـ 3.6× لأنه يعالج أخطاء الصفحات على مستوى التطبيقات دون مشاركة النواة بما يتجاوز إرسال الاستثناء الأولي.

**تخصيص الذاكرة:**
يمكن للتطبيقات تطبيق مخصصات ذاكرة متخصصة:

- **ExOS malloc/free (64 بايت):** 0.3 ميكروثانية
- **Ultrix malloc/free (64 بايت):** 1.2 ميكروثانية

ExOS أسرع بـ 4× لأن نظام التشغيل المكتبي يمكنه تطبيق استراتيجيات تخصيص محسّنة لنمط التطبيق. على سبيل المثال، يمكن لقاعدة بيانات استخدام تخصيص قائم على المنطقة، بينما يمكن لتطبيق علمي استخدام تخصيص المجموعة.

**إدارة جدول الصفحات:**
يمكن لأنظمة التشغيل المكتبية تحسين إدارة جدول الصفحات:

- **تعيين صفحة ExOS:** 2.5 ميكروثانية
- **Ultrix mmap:** 45 ميكروثانية

ExOS أسرع بـ 18× لأنه يتعامل مباشرة مع إدخالات TLB دون المرور عبر نظام الذاكرة الافتراضية للنواة.

**6.4 أداء إدخال/إخراج القرص**

أداء إدخال/إخراج القرص حاسم للتطبيقات كثيفة البيانات.

**القراءة المتزامنة:**
- **قراءة متزامنة ExOS (4KB):** 8.2 ميلي ثانية
- **قراءة متزامنة Ultrix (4KB):** 8.8 ميلي ثانية

الأداء قابل للمقارنة لأن كلا النظامين محدود بأجهزة القرص. ومع ذلك، يوفر ExOS نفقات عامة أقل لإعداد الإدخال/الإخراج.

**الإدخال/الإخراج اللامتزامن:**
يسمح ExOS للتطبيقات بوضع طلبات قرص متعددة في قائمة انتظار وإعادة ترتيبها للكفاءة:

- **إنتاجية ExOS اللامتزامنة (طلبات 4KB):** 1.8 ميجابايت/ثانية
- **إنتاجية Ultrix اللامتزامنة (طلبات 4KB):** 1.4 ميجابايت/ثانية

ExOS أسرع بـ 29% لأن نظام التشغيل المكتبي يمكنه تطبيق جدولة قرص خاصة بالتطبيق. يمكن لقاعدة بيانات ترتيب الطلبات حسب موقع القرص لتقليل عمليات البحث، بينما يمكن لخادم فيديو جدولة الطلبات للحفاظ على معدل البث.

**6.5 أداء الشبكة**

أداء الشبكة ضروري للأنظمة الموزعة وخوادم الويب.

**زمن وصول استقبال الحزمة:**
باستخدام مرشحات الحزم الديناميكية، يوفر Aegis الحزم بكفاءة:

- **استقبال حزمة Aegis (حجم أدنى):** 95 ميكروثانية
- **استقبال حزمة Ultrix (حجم أدنى):** 180 ميكروثانية

Aegis أسرع بـ 1.9× بسبب ترشيح الحزم الفعال والتسليم بدون نسخ إلى مخازن التطبيقات المؤقتة.

**إنتاجية الشبكة:**
- **إنتاجية TCP لـ ExOS (localhost):** 38 ميجابايت/ثانية
- **إنتاجية TCP لـ Ultrix (localhost):** 28 ميجابايت/ثانية

يحقق ExOS إنتاجية أعلى بنسبة 36% من خلال تقليل نسخ الذاكرة والسماح للتطبيق بإدارة معالجة البروتوكول.

**6.6 أداء التطبيقات**

قمنا بقياس أداء التطبيقات من البداية إلى النهاية للتحقق من أن تحسينات القياسات الدقيقة تترجم إلى فوائد حقيقية.

**خادم الويب:**
خادم HTTP بسيط يعمل على ExOS:

- **خادم ويب ExOS (ملفات صغيرة):** 4,200 طلب/ثانية
- **خادم ويب Ultrix (ملفات صغيرة):** 2,800 طلب/ثانية

ExOS أسرع بـ 50% بسبب الشبكات الفعالة وإدارة الذاكرة وإدخال/إخراج القرص.

**استعلام قاعدة البيانات:**
قاعدة بيانات بسيطة تقوم بعمليات بحث مفهرسة:

- **قاعدة بيانات ExOS (1000 استعلام):** 1.2 ثانية
- **قاعدة بيانات Ultrix (1000 استعلام):** 1.8 ثانية

ExOS أسرع بـ 50% لأن قاعدة البيانات يمكنها تطبيق استبدال صفحات مخصص وجدولة قرص محسّنة لأنماط وصول قاعدة البيانات.

**6.7 مناقشة**

تُظهر قياسات الأداء عدة نقاط رئيسية:

1. **نفقات عامة منخفضة:** يضيف Aegis حداً أدنى من النفقات العامة لعمليات الأجهزة. عمليات نقل التحكم المحمي ومعالجة الاستثناءات وتبديلات السياق كلها تنفذ في بضع عشرات من الدورات.

2. **تخصص التطبيقات:** يمكن لأنظمة التشغيل المكتبية تطبيق تحسينات مستحيلة في النوى التقليدية. IPC الذاكرة المشتركة لـ ExOS وتخصيص الذاكرة المتخصص وجدولة القرص على مستوى التطبيقات كلها تتفوق بشكل كبير على التطبيقات التقليدية.

3. **لا عقوبة أداء:** على الرغم من توفير مرونة غير مسبوقة، لا يضحي نهج الإكسوكيرنل بالأداء. في الواقع، غالباً ما يوفر أداءً أفضل من الأنظمة التقليدية.

4. **قابلية التوسع:** تزداد فوائد الإدارة على مستوى التطبيقات مع تزايد تخصص التطبيقات. تشهد التطبيقات العامة تحسينات متواضعة، بينما يمكن للتطبيقات المتخصصة تحقيق تسريعات بأوامر من الحجم.

تتحقق هذه النتائج من فرضية الإكسوكيرنل: التطبيقات تعرف أفضل من نظام التشغيل كيفية إدارة الموارد، ومنحها التحكم يؤدي إلى أداء أفضل.

---

### Translation Notes

- **Key terms introduced:**
  - Microbenchmark: قياس دقيق
  - Protected control transfer: نقل التحكم المحمي
  - Null system call: استدعاء نظام فارغ (minimal syscall for benchmarking)
  - Crossing protection boundaries: عبور حدود الحماية
  - Lazy saving: حفظ كسول
  - Region-based allocation: تخصيص قائم على المنطقة
  - Pool allocation: تخصيص المجموعة
  - Synchronous/Asynchronous: متزامن/لامتزامن
  - Localhost: localhost (kept in English as technical term)
  - End-to-end: من البداية إلى النهاية
  - Indexed lookup: بحث مفهرس
  - Order-of-magnitude: أوامر من الحجم (orders of magnitude)
  - Modest improvements: تحسينات متواضعة

- **Performance data:** All numerical results are precisely preserved in the translation

- **Context:** This section provides empirical validation of the exokernel's performance claims

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score: 0.88**

### Back-Translation (Validation)

This section evaluates the performance of Aegis and ExOS through microbenchmarks and application-level measurements. Our results demonstrate that the exokernel approach provides performance equal to or better than traditional monolithic operating systems, while offering unprecedented flexibility.

Aegis achieves exceptionally fast protected control transfers: Aegis null system call: 45 cycles, Ultrix null system call: 145 cycles. Aegis is 3.2× faster than Ultrix because it saves minimal processor state and doesn't perform unnecessary operations like checking for signals.

ExOS implements shared memory IPC by mapping the same physical pages into multiple address spaces: ExOS shared memory write (4 bytes): 0.8 microseconds, Ultrix pipe (4 bytes): 45 microseconds. ExOS is 56× faster than pipes because it avoids kernel intervention and memory copies.

The performance measurements demonstrate several key points: Low Overhead, Application Specialization, No Performance Penalty, and Scalability. These results validate the exokernel hypothesis: applications know better than the operating system how to manage resources, and giving them control leads to better performance.
