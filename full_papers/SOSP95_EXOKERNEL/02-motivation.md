# Section 2: Motivation for Exokernels
## القسم 2: الدافع للإكسوكيرنل

**Section:** Motivation
**Translation Quality:** 0.87
**Glossary Terms Used:** operating system, resource management, abstraction, application, performance, complexity, functionality, kernel, microkernel, user-level, privileged, interface, virtual memory, IPC, file system, process, page replacement, LRU, distributed shared memory, garbage collector, database, thread, exception, timer interrupt

---

### English Version

Traditionally, operating systems have centralized resource management via a set of abstractions that cannot be specialized, extended, or replaced. Whether provided by the kernel or by trusted user-level servers (as in microkernel-based systems), these abstractions are implemented by privileged software that must be used by all applications, and therefore cannot be changed by untrusted software. Typically, the abstractions include processes, files, address spaces, and interprocess communication. In this section we discuss the problems with general-purpose implementations of these abstractions and show how the exokernel architecture addresses these problems.

**2.1 The Cost of Fixed High-Level Abstractions**

The essential observation about abstractions in traditional operating systems is that they are overly general. Traditional operating systems attempt to provide all the features needed by all applications. As previously noted by Lampson and Sproull [32], Anderson et al. [4] and Massalin and Pu [36], general-purpose implementations of abstractions force applications that do not need a given feature to pay substantial overhead costs. This longstanding problem has become more important with explosive improvements in raw hardware performance and enormous growth in diversity of the application software base. We argue that preventing the modification of the implementation of these high-level abstractions can reduce the performance, increase the complexity, and limit the functionality of application programs.

Fixed high-level abstractions hurt application performance because there is no single way to abstract physical resources or to implement an abstraction that is best for all applications. In implementing an abstraction, an operating system is forced to make trade-offs between support for sparse or dense address spaces, read-intensive or write-intensive workloads, etc. Any such trade-off penalizes some class of applications. For example, relational databases and garbage collectors sometimes have very predictable data access patterns, and their performance suffers when a general-purpose page replacement strategy such as LRU is imposed by the operating system. The performance improvements of such application-specific policies can be substantial; Cao et al. [10] measured that application-controlled file caching can reduce application running time by as much as 45%.

Fixed high-level abstractions hide information from applications. For instance, most current systems do not make low-level exceptions, timer interrupts, or raw device I/O directly available to application-level software. Unfortunately, hiding this information makes it difficult or impossible for applications to implement their own resource management abstractions. For example, database implementors must struggle to emulate random-access record storage on top of file systems [47]. As another example, implementing lightweight threads on top of heavyweight processes usually requires compromises in correctness and performance, because the operating system hides page faults and timer interrupts [4]. In such cases, application complexity increases because of the difficulty of getting good performance from high-level abstractions.

Fixed high-level abstractions limit the functionality of applications, because they are the only available interface between applications and hardware resources. Because all applications must share one set of abstractions, changes to these abstractions occur rarely, if ever. This may explain why few good ideas from the last decade of operating systems research have been adopted into widespread use: how many production operating systems support scheduler activations [4], multiple protection domains within a single address space [11], efficient IPC [33], or efficient and flexible virtual memory primitives [5, 26, 30]?

**2.2 Exokernels: An End-to-End Argument**

The familiar "end-to-end" argument applies as well to low-level operating system software as it does to low-level communication protocols [44]. Applications know better than operating systems what the goal of their resource management decisions should be and therefore, they should be given as much control as possible over those decisions. Our solution is to allow traditional abstractions to be implemented entirely at application level.

To provide the maximum opportunity for application-level resource management, the exokernel architecture consists of a thin exokernel veneer that multiplexes and exports physical resources securely through a set of low-level primitives. Library operating systems, which use the low-level exokernel interface, implement higher-level abstractions and can define special-purpose implementations that best meet the performance and functionality goals of applications (see Figure 1). (For brevity, we sometimes refer to "library operating system" as "application.") This structure allows the extension, specialization and even replacement of abstractions. For instance, page-table structures can vary among library operating systems: an application can select a library with a particular implementation of a page table that is most suitable to its needs. To the best of our knowledge, no other secure operating system architecture allows applications so much useful freedom.

This paper demonstrates that the exokernel architecture is an effective way to address the problems listed in Section 2.1. Many of these problems are solved by simply moving the implementation of abstractions to application level, since conflicts between application needs and available abstractions can then be resolved without the intervention of kernel architects. Furthermore, secure multiplexing does not require complex algorithms; it mostly requires tables to track ownership. Therefore, the implementation of an exokernel can be simple. A simple kernel improves reliability and ease of maintenance, consumes few resources, and enables quick adaptation to new requirements (e.g., gigabit networking). Additionally, as is true with RISC instructions, the simplicity of exokernel operations allows them to be implemented efficiently.

**2.3 Library Operating Systems**

The implementations of abstractions in library operating systems can be simpler and more specialized than in-kernel implementations, because library operating systems need not multiplex a resource among competing applications with widely different demands. In addition, since libraries are not trusted by an exokernel, they are free to trust the application. For example, if an application passes the wrong arguments to a library, only that application will be affected. Finally, the number of kernel crossings in an exokernel system can be smaller, since most of the operating system runs in the address space of the application.

Library operating systems can provide as much portability and compatibility as is desirable. Applications that use an exokernel interface directly will not be portable, because the interface will include hardware-specific information. Applications that use library operating systems that implement standard interfaces (e.g., POSIX) will be portable across any system that provides the same interface. An application that runs on an exokernel can freely replace these library operating systems without any special privileges, which simplifies the addition and development of new standards and features.

We expect that most applications will use a handful of available library operating systems that implement the popular interfaces; only designers of more ambitious applications will develop new library operating systems that fit their needs. Library operating systems themselves can be made portable by designing them to use a low-level machine-independent layer to hide hardware details.

Extending or specializing a library operating system might be considerably simplified by modular design. It is possible that object-oriented programming methods, overloading, and inheritance can provide useful operating system service implementations that can be easily specialized and extended, as in the VM++ library [30]. To reduce the space required by these libraries, support for shared libraries and dynamic linking will be an essential part of a complete exokernel-based system.

As in microkernel systems, an exokernel can provide backward compatibility in three ways: one, binary emulation of the operating system and its programs; two, by implementing its hardware abstraction layer on top of an exokernel; and three, re-implementing the operating system's abstractions on top of an exokernel.

---

### النسخة العربية

تقليدياً، قامت أنظمة التشغيل بمركزة إدارة الموارد عبر مجموعة من التجريدات التي لا يمكن تخصيصها أو توسيعها أو استبدالها. سواء تم توفيرها بواسطة النواة أو بواسطة خوادم موثوقة على مستوى المستخدم (كما في الأنظمة القائمة على النواة الدقيقة)، يتم تطبيق هذه التجريدات بواسطة برامج ممتازة يجب أن تستخدمها جميع التطبيقات، وبالتالي لا يمكن تغييرها بواسطة برامج غير موثوقة. عادةً، تتضمن التجريدات العمليات والملفات وفضاءات العنونة والاتصال بين العمليات. في هذا القسم نناقش المشكلات المتعلقة بالتطبيقات ذات الأغراض العامة لهذه التجريدات ونُظهر كيف تعالج معمارية الإكسوكيرنل هذه المشكلات.

**2.1 تكلفة التجريدات الثابتة ذات المستوى العالي**

الملاحظة الأساسية حول التجريدات في أنظمة التشغيل التقليدية هي أنها عامة بشكل مفرط. تحاول أنظمة التشغيل التقليدية توفير جميع الميزات التي تحتاجها جميع التطبيقات. كما لوحظ سابقاً من قبل Lampson وSproull [32] وAnderson وآخرون [4] وMassalin وPu [36]، فإن التطبيقات ذات الأغراض العامة للتجريدات تجبر التطبيقات التي لا تحتاج إلى ميزة معينة على دفع تكاليف حمل كبيرة. أصبحت هذه المشكلة طويلة الأمد أكثر أهمية مع التحسينات الهائلة في أداء الأجهزة الخام والنمو الهائل في تنوع قاعدة برامج التطبيقات. نحن نرى أن منع تعديل تطبيق هذه التجريدات ذات المستوى العالي يمكن أن يقلل من الأداء، ويزيد من التعقيد، ويحد من وظائف برامج التطبيقات.

تضر التجريدات الثابتة ذات المستوى العالي بأداء التطبيقات لأنه لا توجد طريقة واحدة لتجريد الموارد المادية أو لتطبيق تجريد يكون الأفضل لجميع التطبيقات. في تطبيق التجريد، يُجبر نظام التشغيل على إجراء مقايضات بين الدعم لفضاءات العنونة المتفرقة أو الكثيفة، وأحمال العمل المكثفة في القراءة أو المكثفة في الكتابة، وما إلى ذلك. أي مقايضة من هذا القبيل تعاقب فئة من التطبيقات. على سبيل المثال، تحتوي قواعد البيانات العلائقية وجامعو القمامة أحياناً على أنماط وصول بيانات يمكن التنبؤ بها بشكل كبير، ويعاني أداؤها عندما تفرض نظام التشغيل استراتيجية استبدال صفحات ذات أغراض عامة مثل LRU. يمكن أن تكون تحسينات الأداء لمثل هذه السياسات الخاصة بالتطبيقات كبيرة؛ قاس Cao وآخرون [10] أن التحكم في التخزين المؤقت للملفات على مستوى التطبيقات يمكن أن يقلل من وقت تشغيل التطبيق بنسبة تصل إلى 45%.

تخفي التجريدات الثابتة ذات المستوى العالي المعلومات من التطبيقات. على سبيل المثال، معظم الأنظمة الحالية لا تجعل الاستثناءات منخفضة المستوى أو مقاطعات المؤقت أو إدخال/إخراج الأجهزة الخام متاحة مباشرة للبرامج على مستوى التطبيقات. لسوء الحظ، فإن إخفاء هذه المعلومات يجعل من الصعب أو المستحيل على التطبيقات تطبيق تجريدات إدارة الموارد الخاصة بها. على سبيل المثال، يجب على منفذي قواعد البيانات أن يكافحوا لمحاكاة تخزين السجلات بالوصول العشوائي فوق أنظمة الملفات [47]. كمثال آخر، يتطلب تطبيق الخيوط خفيفة الوزن فوق العمليات الثقيلة الوزن عادةً تنازلات في الصحة والأداء، لأن نظام التشغيل يخفي أخطاء الصفحات ومقاطعات المؤقت [4]. في مثل هذه الحالات، يزداد تعقيد التطبيق بسبب صعوبة الحصول على أداء جيد من التجريدات ذات المستوى العالي.

تحد التجريدات الثابتة ذات المستوى العالي من وظائف التطبيقات، لأنها الواجهة الوحيدة المتاحة بين التطبيقات وموارد الأجهزة. نظراً لأن جميع التطبيقات يجب أن تشترك في مجموعة واحدة من التجريدات، فإن التغييرات على هذه التجريدات تحدث نادراً، إن حدثت على الإطلاق. قد يفسر هذا سبب عدم اعتماد عدد قليل من الأفكار الجيدة من العقد الأخير من أبحاث أنظمة التشغيل في الاستخدام الواسع النطاق: كم عدد أنظمة التشغيل الإنتاجية التي تدعم تنشيطات المجدول [4]، ومجالات حماية متعددة ضمن فضاء عنونة واحد [11]، وIPC فعال [33]، أو عناصر ذاكرة افتراضية فعالة ومرنة [5، 26، 30]؟

**2.2 الإكسوكيرنل: حجة من النهاية إلى النهاية**

تنطبق حجة "من النهاية إلى النهاية" المألوفة على برامج نظام التشغيل منخفضة المستوى كما تنطبق على بروتوكولات الاتصال منخفضة المستوى [44]. تعرف التطبيقات بشكل أفضل من أنظمة التشغيل ما يجب أن يكون هدف قرارات إدارة مواردها وبالتالي، يجب منحها أكبر قدر ممكن من التحكم في هذه القرارات. حلنا هو السماح بتطبيق التجريدات التقليدية بالكامل على مستوى التطبيقات.

لتوفير أقصى فرصة لإدارة الموارد على مستوى التطبيقات، تتكون معمارية الإكسوكيرنل من طبقة إكسوكيرنل رقيقة تقوم بتعدد الإرسال وتصدير الموارد المادية بشكل آمن من خلال مجموعة من العناصر الأولية منخفضة المستوى. تستخدم أنظمة التشغيل المكتبية، التي تستخدم واجهة الإكسوكيرنل منخفضة المستوى، تطبيق تجريدات أعلى مستوى ويمكنها تحديد تطبيقات ذات أغراض خاصة تلبي بشكل أفضل أهداف الأداء والوظائف للتطبيقات (انظر الشكل 1). (من أجل الإيجاز، نشير أحياناً إلى "نظام التشغيل المكتبي" باسم "التطبيق".) يسمح هذا الهيكل بالتوسيع والتخصيص وحتى استبدال التجريدات. على سبيل المثال، يمكن أن تختلف هياكل جداول الصفحات بين أنظمة التشغيل المكتبية: يمكن للتطبيق تحديد مكتبة بتطبيق معين لجدول صفحات يكون الأنسب لاحتياجاته. على حد علمنا، لا توجد معمارية أخرى لنظام تشغيل آمنة تسمح للتطبيقات بمثل هذه الحرية المفيدة.

يوضح هذا البحث أن معمارية الإكسوكيرنل هي طريقة فعالة لمعالجة المشكلات المدرجة في القسم 2.1. يتم حل العديد من هذه المشكلات ببساطة عن طريق نقل تطبيق التجريدات إلى مستوى التطبيقات، حيث يمكن بعد ذلك حل النزاعات بين احتياجات التطبيقات والتجريدات المتاحة دون تدخل مصممي النواة. علاوة على ذلك، لا يتطلب تعدد الإرسال الآمن خوارزميات معقدة؛ يتطلب في الغالب جداول لتتبع الملكية. لذلك، يمكن أن يكون تطبيق الإكسوكيرنل بسيطاً. تعمل النواة البسيطة على تحسين الموثوقية وسهولة الصيانة، وتستهلك موارد قليلة، وتمكن من التكيف السريع مع المتطلبات الجديدة (على سبيل المثال، الشبكات بسرعة جيجابت). بالإضافة إلى ذلك، كما هو الحال مع تعليمات RISC، فإن بساطة عمليات الإكسوكيرنل تسمح بتطبيقها بكفاءة.

**2.3 أنظمة التشغيل المكتبية**

يمكن أن تكون تطبيقات التجريدات في أنظمة التشغيل المكتبية أبسط وأكثر تخصصاً من التطبيقات داخل النواة، لأن أنظمة التشغيل المكتبية لا تحتاج إلى تعدد إرسال مورد بين التطبيقات المتنافسة ذات المتطلبات المختلفة على نطاق واسع. بالإضافة إلى ذلك، نظراً لأن المكتبات غير موثوقة من قبل الإكسوكيرنل، فهي حرة في الوثوق بالتطبيق. على سبيل المثال، إذا مرر تطبيق ما وسائط خاطئة إلى مكتبة، فسيتأثر ذلك التطبيق فقط. أخيراً، يمكن أن يكون عدد عمليات العبور إلى النواة في نظام الإكسوكيرنل أصغر، حيث يعمل معظم نظام التشغيل في فضاء عنونة التطبيق.

يمكن لأنظمة التشغيل المكتبية توفير قدر من قابلية النقل والتوافق حسب الرغبة. لن تكون التطبيقات التي تستخدم واجهة الإكسوكيرنل مباشرة قابلة للنقل، لأن الواجهة ستتضمن معلومات خاصة بالأجهزة. ستكون التطبيقات التي تستخدم أنظمة تشغيل مكتبية تطبق واجهات قياسية (على سبيل المثال، POSIX) قابلة للنقل عبر أي نظام يوفر نفس الواجهة. يمكن للتطبيق الذي يعمل على إكسوكيرنل استبدال أنظمة التشغيل المكتبية هذه بحرية دون أي امتيازات خاصة، مما يبسط إضافة وتطوير معايير وميزات جديدة.

نتوقع أن معظم التطبيقات ستستخدم حفنة من أنظمة التشغيل المكتبية المتاحة التي تطبق الواجهات الشائعة؛ فقط مصممو التطبيقات الأكثر طموحاً سيطورون أنظمة تشغيل مكتبية جديدة تتناسب مع احتياجاتهم. يمكن جعل أنظمة التشغيل المكتبية نفسها قابلة للنقل من خلال تصميمها لاستخدام طبقة منخفضة المستوى مستقلة عن الآلة لإخفاء تفاصيل الأجهزة.

قد يتم تبسيط توسيع أو تخصيص نظام تشغيل مكتبي بشكل كبير من خلال التصميم النمطي. من الممكن أن توفر طرق البرمجة الموجهة للكائنات والتحميل الزائد والوراثة تطبيقات مفيدة لخدمات نظام التشغيل يمكن تخصيصها وتوسيعها بسهولة، كما في مكتبة VM++ [30]. لتقليل المساحة المطلوبة بواسطة هذه المكتبات، سيكون دعم المكتبات المشتركة والربط الديناميكي جزءاً أساسياً من نظام كامل قائم على الإكسوكيرنل.

كما هو الحال في أنظمة النواة الدقيقة، يمكن للإكسوكيرنل توفير التوافق مع الأنظمة السابقة بثلاث طرق: واحد، محاكاة ثنائية لنظام التشغيل وبرامجه؛ اثنان، من خلال تطبيق طبقة تجريد الأجهزة الخاصة به فوق الإكسوكيرنل؛ وثلاثة، إعادة تطبيق تجريدات نظام التشغيل فوق الإكسوكيرنل.

---

### Translation Notes

- **Figures referenced:** Figure 1 (exokernel architecture diagram)
- **Key terms introduced:** centralized resource management, fixed abstractions, general-purpose implementation, overhead costs, trade-offs, LRU page replacement, lightweight threads, heavyweight processes, scheduler activations, end-to-end argument, library operating system portability
- **Equations:** None
- **Citations:** 14 references ([32], [4], [36], [10], [47], [5], [26], [30], [11], [33], [44], [30])
- **Special handling:**
  - Discussion of design trade-offs
  - Comparison with microkernel-based systems
  - Explanation of libOS concept

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Key Translation Choices

- "centralized resource management" → "مركزة إدارة الموارد"
- "overly general" → "عامة بشكل مفرط"
- "sparse or dense address spaces" → "فضاءات العنونة المتفرقة أو الكثيفة"
- "read-intensive or write-intensive workloads" → "أحمال العمل المكثفة في القراءة أو المكثفة في الكتابة"
- "page replacement strategy" → "استراتيجية استبدال صفحات"
- "LRU" → "LRU" (kept as acronym)
- "lightweight threads" → "الخيوط خفيفة الوزن"
- "heavyweight processes" → "العمليات الثقيلة الوزن"
- "end-to-end argument" → "حجة من النهاية إلى النهاية"
- "thin exokernel veneer" → "طبقة إكسوكيرنل رقيقة"
- "shared libraries" → "المكتبات المشتركة"
- "dynamic linking" → "الربط الديناميكي"
- "binary emulation" → "محاكاة ثنائية"
