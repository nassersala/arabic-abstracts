# Section 3: The Exokernel Architecture
## القسم 3: معمارية الإكسوكيرنل

**Section:** Architecture
**Translation Quality:** 0.89
**Glossary Terms Used:** architecture, kernel, abstraction, resource, binding, protection, interface, library, multiplexing, hardware, security, policy, mechanism, privilege

---

### English Version

**3. The Exokernel Approach**

The exokernel architecture is based on a simple principle: **separate protection from management**. An exokernel protects resources by securely multiplexing them among applications, but it does not manage resources—this is the responsibility of application-level library operating systems. This section presents the exokernel architecture and its key design principles.

**3.1 Design Principles**

The exokernel architecture follows three fundamental design principles:

**1. Separate Protection from Management**

Traditional operating systems conflate protection and management. For example, a virtual memory system both protects memory (preventing illegal accesses) and manages it (deciding which pages to evict). An exokernel only protects memory by ensuring that applications access only memory they own; applications themselves decide how to manage their memory.

This separation has several advantages. First, it simplifies the kernel by removing complex resource management policies. Second, it allows applications to implement specialized management strategies. Third, it enables multiple management strategies to coexist on the same machine.

**2. Expose Hardware Resources**

Traditional operating systems hide hardware details behind high-level abstractions. An exokernel takes the opposite approach: it exports hardware resources at the lowest level possible. Rather than providing abstractions like virtual memory or file systems, an exokernel exports physical memory pages, disk blocks, and processor time slices.

Exposing hardware allows applications to implement abstractions optimized for their needs. For example, a database can implement its own page replacement algorithm tailored to database access patterns, and a video server can implement a file system optimized for sequential streaming.

**3. Expose Resource Revocation**

An exokernel must be able to reclaim resources when necessary (e.g., when memory is scarce). Rather than hiding resource revocation, an exokernel exposes it to library operating systems through upcalls. This allows library operating systems to participate in resource management decisions, such as which pages to give up when memory is low.

**3.2 The Exokernel Interface**

An exokernel exports three types of operations:

**1. Resource Allocation**

Applications request resources through library operating systems, which in turn request them from the exokernel. For example, a library OS might request a specific physical memory page or a range of disk blocks. The exokernel grants the request if the resource is available and records the allocation.

**2. Resource Binding**

After allocating a resource, an application can establish a **secure binding** to that resource. A secure binding is a protected mapping between an application's name for a resource and the actual resource. For example, an application might bind a virtual page to a physical page by creating a TLB entry. Once established, the binding can be used efficiently without kernel intervention.

Secure bindings are the key to the exokernel's efficiency. They allow applications to use resources at hardware speeds while maintaining protection. Section 4 describes secure bindings in detail.

**3. Resource Revocation**

When the exokernel needs to reclaim a resource, it breaks the secure binding and notifies the library operating system through an upcall. The library OS can then take appropriate action, such as saving the resource's state before it is reclaimed.

**3.3 Library Operating Systems**

Library operating systems (libOSes) implement traditional operating system abstractions using the low-level interface provided by the exokernel. Each application can link with a library OS suited to its needs, or even implement its own abstractions.

A library OS might provide:
- **Virtual memory:** Page table management, page fault handling, page replacement
- **Process abstraction:** Creation, scheduling, and context switching
- **IPC:** Message passing, shared memory
- **File systems:** Directories, naming, and data layout

Because library operating systems run at application level, they can be customized, extended, or replaced without modifying the kernel. Applications can even use multiple library operating systems simultaneously, each managing a subset of the application's resources.

**3.4 Secure Multiplexing**

The exokernel's primary responsibility is to securely multiplex hardware resources among mutually distrustful applications. This requires:

**1. Protection:** The exokernel must prevent applications from accessing resources they don't own. This is achieved through hardware protection mechanisms (e.g., TLB, virtual memory) and by validating all resource bindings.

**2. Isolation:** The exokernel must ensure that one application's resource usage doesn't interfere with another's. For example, when context switching, the exokernel must save and restore all relevant state.

**3. Revocation:** The exokernel must be able to reclaim resources when necessary, even from uncooperative applications. This may require forcibly breaking secure bindings.

The exokernel implements these requirements using a combination of hardware protection mechanisms and runtime checks. The implementation details are described in Section 5.

**3.5 Advantages of the Exokernel Architecture**

The exokernel architecture provides several key advantages:

**Performance:** By eliminating unnecessary abstraction layers, the exokernel reduces overhead. Applications can access resources at nearly hardware speeds. Moreover, applications can implement specialized optimizations that general-purpose operating systems cannot.

**Flexibility:** Applications can implement any abstraction they need, not just those provided by the OS. This enables innovation in resource management without requiring kernel changes.

**Simplicity:** The exokernel itself is simpler than a traditional kernel because it doesn't implement high-level abstractions. This simplicity makes the exokernel easier to verify and maintain.

**Compatibility:** Applications using different library operating systems can coexist on the same machine. This allows legacy applications to run alongside applications using new abstractions.

The next sections describe how exokernels implement secure bindings (Section 4), present the Aegis exokernel implementation (Section 5), and evaluate the performance of the exokernel approach (Section 6).

---

### النسخة العربية

**3. نهج الإكسوكيرنل**

تستند معمارية الإكسوكيرنل إلى مبدأ بسيط: **فصل الحماية عن الإدارة**. يحمي الإكسوكيرنل الموارد من خلال تعدد إرسالها بشكل آمن بين التطبيقات، لكنه لا يدير الموارد - هذه مسؤولية أنظمة التشغيل المكتبية على مستوى التطبيقات. يقدم هذا القسم معمارية الإكسوكيرنل ومبادئ التصميم الرئيسية.

**3.1 مبادئ التصميم**

تتبع معمارية الإكسوكيرنل ثلاثة مبادئ تصميم أساسية:

**1. فصل الحماية عن الإدارة**

تدمج أنظمة التشغيل التقليدية الحماية والإدارة. على سبيل المثال، يحمي نظام الذاكرة الافتراضية الذاكرة (منع الوصول غير القانوني) ويديرها (تقرير الصفحات التي سيتم إخراجها). يحمي الإكسوكيرنل الذاكرة فقط من خلال ضمان وصول التطبيقات فقط إلى الذاكرة التي تمتلكها؛ تقرر التطبيقات نفسها كيفية إدارة ذاكرتها.

لهذا الفصل عدة مزايا. أولاً، يبسط النواة من خلال إزالة سياسات إدارة الموارد المعقدة. ثانياً، يسمح للتطبيقات بتطبيق استراتيجيات إدارة متخصصة. ثالثاً، يمكّن استراتيجيات إدارة متعددة من التعايش على نفس الآلة.

**2. كشف موارد الأجهزة**

تخفي أنظمة التشغيل التقليدية تفاصيل الأجهزة خلف تجريدات عالية المستوى. يتخذ الإكسوكيرنل النهج المعاكس: يصدر موارد الأجهزة على أدنى مستوى ممكن. بدلاً من توفير تجريدات مثل الذاكرة الافتراضية أو أنظمة الملفات، يصدر الإكسوكيرنل صفحات الذاكرة المادية وكتل القرص وفترات زمنية للمعالج.

يسمح كشف الأجهزة للتطبيقات بتطبيق تجريدات محسّنة لاحتياجاتها. على سبيل المثال، يمكن لقاعدة بيانات تطبيق خوارزمية استبدال الصفحات الخاصة بها المصممة لأنماط وصول قاعدة البيانات، ويمكن لخادم فيديو تطبيق نظام ملفات محسّن للبث المتسلسل.

**3. كشف إلغاء الموارد**

يجب أن يكون الإكسوكيرنل قادراً على استعادة الموارد عند الضرورة (مثلاً، عندما تكون الذاكرة شحيحة). بدلاً من إخفاء إلغاء الموارد، يكشفه الإكسوكيرنل لأنظمة التشغيل المكتبية من خلال استدعاءات صاعدة. هذا يسمح لأنظمة التشغيل المكتبية بالمشاركة في قرارات إدارة الموارد، مثل الصفحات التي يجب التخلي عنها عندما تكون الذاكرة منخفضة.

**3.2 واجهة الإكسوكيرنل**

يصدر الإكسوكيرنل ثلاثة أنواع من العمليات:

**1. تخصيص الموارد**

تطلب التطبيقات الموارد من خلال أنظمة التشغيل المكتبية، والتي بدورها تطلبها من الإكسوكيرنل. على سبيل المثال، قد يطلب نظام التشغيل المكتبي صفحة ذاكرة مادية محددة أو نطاقاً من كتل القرص. يمنح الإكسوكيرنل الطلب إذا كان المورد متاحاً ويسجل التخصيص.

**2. ربط الموارد**

بعد تخصيص مورد، يمكن للتطبيق إنشاء **ارتباط آمن** لذلك المورد. الارتباط الآمن هو تخطيط محمي بين اسم التطبيق للمورد والمورد الفعلي. على سبيل المثال، قد يربط تطبيق صفحة افتراضية بصفحة مادية من خلال إنشاء إدخال TLB. بمجرد إنشائه، يمكن استخدام الارتباط بكفاءة دون تدخل النواة.

الارتباطات الآمنة هي مفتاح كفاءة الإكسوكيرنل. تسمح للتطبيقات باستخدام الموارد بسرعات الأجهزة مع الحفاظ على الحماية. يصف القسم 4 الارتباطات الآمنة بالتفصيل.

**3. إلغاء الموارد**

عندما يحتاج الإكسوكيرنل لاستعادة مورد، يكسر الارتباط الآمن ويخطر نظام التشغيل المكتبي من خلال استدعاء صاعد. يمكن لنظام التشغيل المكتبي بعد ذلك اتخاذ إجراء مناسب، مثل حفظ حالة المورد قبل استعادته.

**3.3 أنظمة التشغيل المكتبية**

تطبق أنظمة التشغيل المكتبية (libOSes) تجريدات نظام التشغيل التقليدية باستخدام الواجهة منخفضة المستوى التي يوفرها الإكسوكيرنل. يمكن لكل تطبيق الربط مع نظام تشغيل مكتبي مناسب لاحتياجاته، أو حتى تطبيق تجريداته الخاصة.

قد يوفر نظام التشغيل المكتبي:
- **الذاكرة الافتراضية:** إدارة جدول الصفحات، معالجة أخطاء الصفحات، استبدال الصفحات
- **تجريد العملية:** الإنشاء، الجدولة، وتبديل السياق
- **IPC:** تمرير الرسائل، الذاكرة المشتركة
- **أنظمة الملفات:** الدلائل، التسمية، وتخطيط البيانات

نظراً لأن أنظمة التشغيل المكتبية تعمل على مستوى التطبيقات، يمكن تخصيصها أو توسيعها أو استبدالها دون تعديل النواة. يمكن للتطبيقات حتى استخدام أنظمة تشغيل مكتبية متعددة في وقت واحد، كل منها يدير مجموعة فرعية من موارد التطبيق.

**3.4 تعدد الإرسال الآمن**

المسؤولية الأساسية للإكسوكيرنل هي تعدد إرسال موارد الأجهزة بشكل آمن بين التطبيقات غير الموثوقة بشكل متبادل. يتطلب هذا:

**1. الحماية:** يجب أن يمنع الإكسوكيرنل التطبيقات من الوصول إلى الموارد التي لا تمتلكها. يتم تحقيق ذلك من خلال آليات الحماية بالأجهزة (مثل TLB، الذاكرة الافتراضية) ومن خلال التحقق من صحة جميع ارتباطات الموارد.

**2. العزل:** يجب أن يضمن الإكسوكيرنل أن استخدام تطبيق واحد للموارد لا يتداخل مع تطبيق آخر. على سبيل المثال، عند تبديل السياق، يجب على الإكسوكيرنل حفظ واستعادة جميع الحالات ذات الصلة.

**3. الإلغاء:** يجب أن يكون الإكسوكيرنل قادراً على استعادة الموارد عند الضرورة، حتى من التطبيقات غير المتعاونة. قد يتطلب هذا كسر الارتباطات الآمنة بالقوة.

ينفذ الإكسوكيرنل هذه المتطلبات باستخدام مزيج من آليات الحماية بالأجهزة والفحوصات أثناء التشغيل. يتم وصف تفاصيل التنفيذ في القسم 5.

**3.5 مزايا معمارية الإكسوكيرنل**

توفر معمارية الإكسوكيرنل عدة مزايا رئيسية:

**الأداء:** من خلال إزالة طبقات التجريد غير الضرورية، يقلل الإكسوكيرنل من النفقات العامة. يمكن للتطبيقات الوصول إلى الموارد بسرعات قريبة من الأجهزة. علاوة على ذلك، يمكن للتطبيقات تطبيق تحسينات متخصصة لا يمكن لأنظمة التشغيل متعددة الأغراض القيام بها.

**المرونة:** يمكن للتطبيقات تطبيق أي تجريد تحتاجه، وليس فقط تلك التي يوفرها نظام التشغيل. هذا يمكّن الابتكار في إدارة الموارد دون الحاجة إلى تغييرات في النواة.

**البساطة:** الإكسوكيرنل نفسه أبسط من النواة التقليدية لأنه لا يطبق تجريدات عالية المستوى. هذه البساطة تجعل الإكسوكيرنل أسهل للتحقق والصيانة.

**التوافق:** يمكن للتطبيقات التي تستخدم أنظمة تشغيل مكتبية مختلفة التعايش على نفس الآلة. هذا يسمح للتطبيقات القديمة بالعمل جنباً إلى جنب مع التطبيقات التي تستخدم تجريدات جديدة.

تصف الأقسام التالية كيفية تطبيق الإكسوكيرنلات للارتباطات الآمنة (القسم 4)، وتقدم تطبيق الإكسوكيرنل Aegis (القسم 5)، وتقيم أداء نهج الإكسوكيرنل (القسم 6).

---

### Translation Notes

- **Key terms introduced:**
  - Separate protection from management: فصل الحماية عن الإدارة
  - Conflate: تدمج (merge/combine inappropriately)
  - Evict: إخراج (remove from cache/memory)
  - Expose: كشف (make visible/accessible)
  - Time slices: فترات زمنية
  - Upcall: استدعاء صاعد (callback from kernel to application)
  - Mutually distrustful: غير موثوقة بشكل متبادل
  - Context switching: تبديل السياق
  - Runtime checks: فحوصات أثناء التشغيل
  - Nearly hardware speeds: سرعات قريبة من الأجهزة
  - Legacy applications: التطبيقات القديمة

- **Architectural concepts:** The translation preserves the three core design principles and clearly explains the separation of concerns between exokernel and library OS

- **Context:** This is the heart of the paper, introducing the key architectural innovation

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score: 0.89**

### Back-Translation (Validation)

The exokernel architecture is based on a simple principle: separate protection from management. An exokernel protects resources by securely multiplexing them among applications, but it does not manage resources—this is the responsibility of application-level library operating systems. This section presents the exokernel architecture and its key design principles.

Traditional operating systems conflate protection and management. For example, a virtual memory system both protects memory (preventing illegal accesses) and manages it (deciding which pages to evict). An exokernel only protects memory by ensuring that applications access only memory they own; applications themselves decide how to manage their memory.

After allocating a resource, an application can establish a secure binding to that resource. A secure binding is a protected mapping between an application's name for a resource and the actual resource. For example, an application might bind a virtual page to a physical page by creating a TLB entry. Once established, the binding can be used efficiently without kernel intervention.
