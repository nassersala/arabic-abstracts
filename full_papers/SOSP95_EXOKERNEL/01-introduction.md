# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** operating system, application, resource, interface, abstraction, virtual memory, interprocess communication, address space, process, file, implementation, performance, flexibility, functionality, domain-specific optimization, library, exokernel, architecture, multiplexing, kernel, primitive, exception handling, signal, TLB

---

### English Version

Operating systems define the interface between applications and physical resources. Unfortunately, this interface can significantly limit the performance and implementation freedom of applications. Traditionally, operating systems hide information about machine resources behind high-level abstractions such as processes, files, address spaces and interprocess communication. These abstractions define a virtual machine on which applications execute; their implementation cannot be replaced or modified by untrusted applications. Hardcoding the implementations of these abstractions is inappropriate for three main reasons: it denies applications the advantages of domain-specific optimizations, it discourages changes to the implementations of existing abstractions, and it restricts the flexibility of application builders, since new abstractions can only be added by awkward emulation on top of existing ones (if they can be added at all).

We believe these problems can be solved through application-level (i.e., untrusted) resource management. To this end, we have designed a new operating system architecture, exokernel, in which traditional operating system abstractions, such as virtual memory (VM) and interprocess communication (IPC), are implemented entirely at application level by untrusted software. In this architecture, a minimal kernel—which we call an exokernel—securely multiplexes available hardware resources. Library operating systems, working above the exokernel interface, implement higher-level abstractions. Application writers select libraries or implement their own. New implementations of library operating systems are incorporated by simply relinking application executables.

Substantial evidence exists that applications can benefit greatly from having more control over how machine resources are used to implement higher-level abstractions. Appel and Li [5] reported that the high cost of general-purpose virtual memory primitives reduces the performance of persistent stores, garbage collectors, and distributed shared memory systems. Cao et al. [10] reported that application-level control over file caching can reduce application running time by 45%. Harty and Cheriton [26] and Krueger et al. [30] showed how application-specific virtual memory policies can increase application performance. Stonebraker [47] argued that inappropriate file-system implementation decisions can have a dramatic impact on the performance of databases. Thekkath and Levy [50] demonstrated that exceptions can be made an order of magnitude faster by deferring signal handling to applications.

To provide applications control over machine resources, an exokernel defines a low-level interface. The exokernel architecture is founded on and motivated by a single, simple, and old observation: the lower the level of a primitive, the more efficiently it can be implemented, and the more latitude it grants to implementors of higher-level abstractions.

To provide an interface that is as low-level as possible (ideally, just the hardware interface), an exokernel designer has a single overriding goal: to separate protection from management. For instance, an exokernel should protect framebuffers without understanding windowing systems and disks without understanding file systems. One approach is to give each application its own virtual machine [17]. As we discuss in Section 8, virtual machines can have severe performance penalties. Therefore, an exokernel uses a different approach: it exports hardware resources rather than emulating them, which allows an efficient and simple implementation. An exokernel employs three techniques to export resources securely. First, by using secure bindings, applications can securely bind to machine resources and handle events. Second, by using visible revocation, applications participate in a resource revocation protocol. Third, by using an abort protocol, an exokernel can break secure bindings of uncooperative applications by force.

We have implemented a prototype exokernel system based on secure bindings, visible revocation, and abort protocols. It includes an exokernel (Aegis) and an untrusted library operating system (ExOS). We use this system to demonstrate several important properties of the exokernel architecture: (1) exokernels can be made efficient due to the limited number of simple primitives they must provide; (2) low-level secure multiplexing of hardware resources can be provided with low overhead; (3) traditional abstractions, such as VM and IPC, can be implemented efficiently at application level, where they can be easily extended, specialized, or replaced; and (4) applications can create special-purpose implementations of abstractions, tailored to their functionality and performance needs.

In practice, our prototype exokernel system provides applications with greater flexibility and better performance than monolithic and microkernel systems. Aegis's low-level interface allows application-level software such as ExOS to manipulate resources very efficiently. Aegis's protected control transfer is almost seven times faster than the best reported implementation [33]. Aegis's exception dispatch is five times faster than the best reported implementation [50]. On identical hardware, Aegis's exception dispatch and control transfer are roughly two orders of magnitude faster than in Ultrix 4.2, a mature monolithic system.

Aegis also gives ExOS (and other application-level software) flexibility that is not available in microkernel-based systems. For instance, virtual memory is implemented at application level, where it can be tightly integrated with distributed shared memory systems and garbage collectors. Aegis's efficient protected control transfer allows applications to construct a wide array of efficient IPC primitives by trading performance for additional functionality. In contrast, microkernel systems such as Amoeba [48], Chorus [43], Mach [2], and V [15] do not allow untrusted application software to define specialized IPC primitives because virtual memory and message passing services are implemented by the kernel and trusted servers. Similarly, many other abstractions, such as page-table structures and process abstractions, cannot be modified in microkernels. Finally, many of the hardware resources in microkernel systems, such as the network, screen, and disk, are encapsulated in heavyweight servers that cannot be bypassed or tailored to application-specific needs. These heavyweight servers can be viewed as fixed kernel subsystems that run in user-space.

This paper focuses on the exokernel architecture design and how it can be implemented securely and efficiently. Section 2 provides a more detailed case for exokernels. Section 3 discusses the issues that arise in their design. Section 4 overviews the status of our prototype and explains our experimental methodology. Sections 5 and 6 present the implementation and summarize performance measurements of Aegis and ExOS. Section 7 reports on experiments that demonstrate the flexibility of the exokernel architecture. Section 8 summarizes related work and Section 9 concludes.

---

### النسخة العربية

تحدد أنظمة التشغيل الواجهة بين التطبيقات والموارد المادية. لسوء الحظ، يمكن لهذه الواجهة أن تحد بشكل كبير من أداء وحرية التطبيق للتطبيقات. تقليدياً، تخفي أنظمة التشغيل المعلومات حول موارد الآلة خلف تجريدات عالية المستوى مثل العمليات والملفات وفضاءات العنونة والاتصال بين العمليات. تحدد هذه التجريدات آلة افتراضية تعمل عليها التطبيقات؛ ولا يمكن استبدال أو تعديل تطبيقها بواسطة تطبيقات غير موثوقة. إن الترميز الصلب لتطبيقات هذه التجريدات غير ملائم لثلاثة أسباب رئيسية: فهو يحرم التطبيقات من مزايا التحسينات الخاصة بالمجال، ويثبط التغييرات على تطبيقات التجريدات الموجودة، ويقيد مرونة بناة التطبيقات، حيث لا يمكن إضافة تجريدات جديدة إلا عن طريق المحاكاة غير الملائمة فوق التجريدات الموجودة (إن أمكن إضافتها على الإطلاق).

نعتقد أنه يمكن حل هذه المشكلات من خلال إدارة الموارد على مستوى التطبيقات (أي غير الموثوقة). لهذا الغرض، قمنا بتصميم معمارية جديدة لنظام التشغيل، الإكسوكيرنل، حيث يتم تطبيق تجريدات نظام التشغيل التقليدية، مثل الذاكرة الافتراضية (VM) والاتصال بين العمليات (IPC)، بالكامل على مستوى التطبيقات بواسطة برامج غير موثوقة. في هذه المعمارية، تقوم نواة صغيرة - نسميها إكسوكيرنل - بتعدد إرسال موارد الأجهزة المتاحة بشكل آمن. تعمل أنظمة التشغيل المكتبية، التي تعمل فوق واجهة الإكسوكيرنل، على تطبيق تجريدات أعلى مستوى. يختار كتاب التطبيقات المكتبات أو ينفذون مكتباتهم الخاصة. يتم دمج التطبيقات الجديدة لأنظمة التشغيل المكتبية ببساطة عن طريق إعادة ربط الملفات التنفيذية للتطبيقات.

توجد أدلة كبيرة على أن التطبيقات يمكن أن تستفيد بشكل كبير من وجود مزيد من التحكم في كيفية استخدام موارد الآلة لتطبيق تجريدات أعلى مستوى. أفاد Appel وLi [5] أن التكلفة العالية للعناصر الأولية للذاكرة الافتراضية ذات الأغراض العامة تقلل من أداء المخازن الدائمة وجامعي القمامة وأنظمة الذاكرة المشتركة الموزعة. أفاد Cao وآخرون [10] أن التحكم على مستوى التطبيقات في التخزين المؤقت للملفات يمكن أن يقلل من وقت تشغيل التطبيق بنسبة 45%. أظهر Harty وCheriton [26] وKrueger وآخرون [30] كيف يمكن لسياسات الذاكرة الافتراضية الخاصة بالتطبيقات زيادة أداء التطبيقات. جادل Stonebraker [47] بأن قرارات التطبيق غير المناسبة لنظام الملفات يمكن أن يكون لها تأثير كبير على أداء قواعد البيانات. أظهر Thekkath وLevy [50] أنه يمكن جعل الاستثناءات أسرع بمقدار من المقدار من خلال تأجيل معالجة الإشارات إلى التطبيقات.

لتزويد التطبيقات بالتحكم في موارد الآلة، يحدد الإكسوكيرنل واجهة منخفضة المستوى. تقوم معمارية الإكسوكيرنل على ملاحظة واحدة بسيطة وقديمة وتحفزها: كلما انخفض مستوى العنصر الأولي، كان من الممكن تطبيقه بشكل أكثر كفاءة، وكلما زادت الحرية التي يمنحها لمنفذي التجريدات ذات المستوى الأعلى.

لتوفير واجهة منخفضة المستوى قدر الإمكان (في الحالة المثالية، مجرد واجهة الأجهزة)، لدى مصمم الإكسوكيرنل هدف رئيسي واحد: فصل الحماية عن الإدارة. على سبيل المثال، يجب أن يحمي الإكسوكيرنل المخازن المؤقتة للإطارات دون فهم أنظمة النوافذ والأقراص دون فهم أنظمة الملفات. أحد الأساليب هو إعطاء كل تطبيق آلته الافتراضية الخاصة [17]. كما نناقش في القسم 8، يمكن أن يكون للآلات الافتراضية عقوبات أداء شديدة. لذلك، يستخدم الإكسوكيرنل نهجاً مختلفاً: فهو يصدر موارد الأجهزة بدلاً من محاكاتها، مما يسمح بتطبيق فعال وبسيط. يستخدم الإكسوكيرنل ثلاث تقنيات لتصدير الموارد بشكل آمن. أولاً، باستخدام الارتباطات الآمنة، يمكن للتطبيقات الارتباط بشكل آمن بموارد الآلة ومعالجة الأحداث. ثانياً، باستخدام الإبطال المرئي، تشارك التطبيقات في بروتوكول إبطال الموارد. ثالثاً، باستخدام بروتوكول الإجهاض، يمكن للإكسوكيرنل كسر الارتباطات الآمنة للتطبيقات غير المتعاونة بالقوة.

قمنا بتطبيق نظام إكسوكيرنل نموذجي بناءً على الارتباطات الآمنة والإبطال المرئي وبروتوكولات الإجهاض. يتضمن إكسوكيرنل (Aegis) ونظام تشغيل مكتبي غير موثوق (ExOS). نستخدم هذا النظام لإظهار العديد من الخصائص المهمة لمعمارية الإكسوكيرنل: (1) يمكن جعل الإكسوكيرنل فعالاً بسبب العدد المحدود من العناصر الأولية البسيطة التي يجب أن يوفرها؛ (2) يمكن توفير تعدد إرسال آمن منخفض المستوى لموارد الأجهزة مع حمل منخفض؛ (3) يمكن تطبيق التجريدات التقليدية، مثل VM وIPC، بكفاءة على مستوى التطبيقات، حيث يمكن توسيعها أو تخصيصها أو استبدالها بسهولة؛ و (4) يمكن للتطبيقات إنشاء تطبيقات ذات أغراض خاصة للتجريدات، مصممة خصيصاً لوظائفها واحتياجات أدائها.

في الممارسة العملية، يوفر نظام الإكسوكيرنل النموذجي الخاص بنا للتطبيقات مرونة أكبر وأداءً أفضل من الأنظمة الأحادية وأنظمة النواة الدقيقة. تسمح واجهة Aegis منخفضة المستوى للبرامج على مستوى التطبيقات مثل ExOS بمعالجة الموارد بكفاءة عالية. نقل التحكم المحمي في Aegis أسرع بنحو سبع مرات من أفضل تطبيق تم الإبلاغ عنه [33]. إرسال الاستثناءات في Aegis أسرع بخمس مرات من أفضل تطبيق تم الإبلاغ عنه [50]. على نفس الأجهزة، فإن إرسال الاستثناءات ونقل التحكم في Aegis أسرع تقريباً بمقدارين من حيث المقدار من Ultrix 4.2، وهو نظام أحادي ناضج.

يمنح Aegis أيضاً ExOS (والبرامج الأخرى على مستوى التطبيقات) مرونة غير متوفرة في الأنظمة القائمة على النواة الدقيقة. على سبيل المثال، يتم تطبيق الذاكرة الافتراضية على مستوى التطبيقات، حيث يمكن دمجها بإحكام مع أنظمة الذاكرة المشتركة الموزعة وجامعي القمامة. يسمح نقل التحكم المحمي الفعال في Aegis للتطبيقات ببناء مجموعة واسعة من عناصر IPC الفعالة من خلال تبادل الأداء بوظائف إضافية. في المقابل، فإن أنظمة النواة الدقيقة مثل Amoeba [48] وChorus [43] وMach [2] وV [15] لا تسمح للبرامج التطبيقية غير الموثوقة بتحديد عناصر IPC متخصصة لأن الذاكرة الافتراضية وخدمات تمرير الرسائل يتم تطبيقها بواسطة النواة والخوادم الموثوقة. وبالمثل، لا يمكن تعديل العديد من التجريدات الأخرى، مثل هياكل جداول الصفحات وتجريدات العمليات، في النوى الدقيقة. أخيراً، يتم تغليف العديد من موارد الأجهزة في أنظمة النواة الدقيقة، مثل الشبكة والشاشة والقرص، في خوادم ثقيلة الوزن لا يمكن تجاوزها أو تخصيصها للاحتياجات الخاصة بالتطبيقات. يمكن النظر إلى هذه الخوادم الثقيلة الوزن كأنظمة فرعية ثابتة للنواة تعمل في فضاء المستخدم.

يركز هذا البحث على تصميم معمارية الإكسوكيرنل وكيف يمكن تطبيقها بشكل آمن وفعال. يوفر القسم 2 حجة أكثر تفصيلاً للإكسوكيرنل. يناقش القسم 3 القضايا التي تنشأ في تصميمها. يعطي القسم 4 نظرة عامة على حالة نموذجنا الأولي ويشرح منهجيتنا التجريبية. يعرض القسمان 5 و6 التطبيق ويلخصان قياسات الأداء لـ Aegis وExOS. يقدم القسم 7 تقريراً عن التجارب التي توضح مرونة معمارية الإكسوكيرنل. يلخص القسم 8 الأعمال ذات الصلة ويختتم القسم 9.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:** exokernel, library operating system (libOS), application-level resource management, secure bindings, visible revocation, abort protocol, Aegis (exokernel implementation), ExOS (library OS)
- **Equations:** None
- **Citations:** 12 references cited ([5], [10], [26], [30], [47], [50], [17], [33], [48], [43], [2], [15])
- **Special handling:**
  - Performance comparisons with Ultrix and other systems
  - System names (Aegis, ExOS, Ultrix, Amoeba, Chorus, Mach, V) kept in English as proper names
  - Technical terms like "exokernel", "libOS" require transliteration and explanation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Key Translation Choices

- "hardcoding" → "الترميز الصلب"
- "domain-specific optimizations" → "التحسينات الخاصة بالمجال"
- "secure multiplexes" → "تعدد إرسال آمن"
- "library operating systems" → "أنظمة التشغيل المكتبية"
- "secure bindings" → "الارتباطات الآمنة"
- "visible revocation" → "الإبطال المرئي"
- "abort protocol" → "بروتوكول الإجهاض"
- "protected control transfer" → "نقل التحكم المحمي"
- "exception dispatch" → "إرسال الاستثناءات"
- "heavyweight servers" → "خوادم ثقيلة الوزن"
- "microkernel" → "النواة الدقيقة"
- "monolithic" → "أحادي"
- "framebuffers" → "المخازن المؤقتة للإطارات"
