# Section 4: The Hierarchical System Structure
## القسم 4: البنية الهرمية للنظام

**Section:** Hierarchical System Structure (Six Levels)
**Translation Quality:** 0.89
**Glossary Terms Used:** hierarchical, level, abstraction, process, interrupt, segment controller, message interpreter, buffering, user program, operator

---

### English Version

## The Hierarchical System Structure

The central contribution of this paper is the demonstration that a complex multiprogramming system can be organized as a strict hierarchy of levels, where each level provides a well-defined abstraction for the levels above it. This hierarchical organization proved essential for systematic verification of correctness.

### The Six Levels

The THE system comprises six distinct levels, numbered 0 through 5:

**Level 0: Processor Allocation**

The lowest level implements processor allocation and multiprogramming. At this level:

- A real-time clock generates periodic interrupts
- The processor is allocated among multiple sequential processes
- Context switching between processes is managed
- The abstraction provided: Higher levels see the processor as if there were multiple independent processors, one for each process

This level hides the reality that a single physical processor is being time-shared among many processes. Above Level 0, programmers can think in terms of sequential processes without concerning themselves with interrupt handling or processor scheduling.

**Level 1: Segment Controller**

Level 1 implements the memory abstraction described earlier. Responsibilities include:

- Managing the segment-to-page mapping
- Handling drum interrupts for secondary storage access
- Ensuring that segments referenced by processes are available in core memory
- Implementing the paging mechanism between core and drum

The abstraction provided: Higher levels see memory as if it were infinite. Programs can reference segments without worrying about physical memory limitations or the mechanics of paging.

This level synchronizes with drum rotation, optimizing drum access by minimizing latency.

**Level 2: Message Interpreter**

Level 2 manages console communication. Functions include:

- Handling keyboard input interrupts
- Managing teleprinter output
- Providing each process with the abstraction of a private console
- Preventing processes from consuming excessive core memory for console I/O

The abstraction provided: Each process appears to have its own dedicated console for conversational interaction, even though physically there may be limited console hardware.

**Level 3: Buffering for I/O Streams**

Level 3 provides buffered input and output for peripheral devices:

- Input buffering: Incoming data streams are buffered, allowing processes to consume data at their own pace
- Output unbuffering: Processes can produce output without waiting for slow peripherals
- Abstraction of peripheral devices as logical communication channels

The abstraction provided: Processes interact with peripheral devices through clean stream interfaces without concerning themselves with device-specific timing or buffering requirements.

**Level 4: Independent User Programs**

At this level reside the user programs themselves. Each user program is an independent sequential process with access to all the abstractions provided by Levels 0-3:

- Virtual infinite memory (from Level 1)
- No concern for processor scheduling (from Level 0)
- Simple I/O through standard interfaces (from Levels 2-3)

User programs can be developed and tested independently without knowledge of other programs running concurrently in the system.

**Level 5: The Operator**

The highest level is the system operator. As Dijkstra noted, this level is "not implemented by us" - it represents the human operator who interacts with the complete system.

### Hierarchical Dependency Rules

A critical design constraint governs the hierarchy:

**"Processes can only generate tasks for processes at lower levels."**

This rule ensures:

1. **No circular dependencies**: Higher levels depend on lower levels, but never vice versa. This prevents circular waiting and potential deadlocks.

2. **Independent verification**: Each level can be tested and verified independently by assuming lower levels are correct and ignoring higher levels entirely.

3. **Incremental development**: The system could be built and tested level by level, starting from Level 0 and progressively adding higher levels only after thorough verification of lower levels.

4. **Conceptual clarity**: The strict layering makes it easier to reason about system behavior and to localize the effects of changes.

### Abstractions at Each Level

Each level introduces one or more independent abstractions:

- **Level 0**: Abstract processors (illusion of multiple CPUs)
- **Level 1**: Virtual memory (segments abstracted from physical pages)
- **Level 2**: Virtual consoles (each process has private console)
- **Level 3**: Buffered streams (abstract peripheral devices)
- **Level 4**: User computation space
- **Level 5**: System operation and control

### Significance of the Hierarchical Structure

The hierarchical organization was not merely an organizational convenience - it was fundamental to achieving verified correctness. By structuring the system as strict layers:

- The complexity of verification was reduced from multiplicative (testing all combinations of interactions) to additive (testing each level independently)
- Reasoning about system properties could proceed by mathematical induction over levels
- Errors were localized to specific levels, simplifying debugging
- The design could be communicated and understood more readily

This layered architecture became a foundational principle in operating system design and software engineering more broadly.

---

### النسخة العربية

## البنية الهرمية للنظام

المساهمة المركزية لهذه الورقة البحثية هي إثبات أن نظام برمجة متعددة معقداً يمكن تنظيمه كتسلسل هرمي صارم من المستويات، حيث يوفر كل مستوى تجريداً محدداً جيداً للمستويات الأعلى منه. أثبت هذا التنظيم الهرمي أنه ضروري للتحقق المنهجي من الصحة.

### المستويات الستة

يتألف نظام THE من ستة مستويات متميزة، مرقمة من 0 إلى 5:

**المستوى 0: تخصيص المعالج**

ينفذ المستوى الأدنى تخصيص المعالج والبرمجة المتعددة. في هذا المستوى:

- تولد ساعة الوقت الفعلي مقاطعات دورية
- يُخصص المعالج بين عمليات تسلسلية متعددة
- تُدار عملية تبديل السياق بين العمليات
- التجريد المقدم: ترى المستويات الأعلى المعالج كما لو كانت هناك معالجات مستقلة متعددة، واحد لكل عملية

يخفي هذا المستوى حقيقة أن معالجاً فيزيائياً واحداً تتم مشاركته زمنياً بين عمليات عديدة. فوق المستوى 0، يمكن للمبرمجين التفكير من حيث العمليات التسلسلية دون القلق بشأن معالجة المقاطعات أو جدولة المعالج.

**المستوى 1: متحكم المقاطع**

ينفذ المستوى 1 تجريد الذاكرة الموصوف سابقاً. تشمل المسؤوليات:

- إدارة تعيين المقاطع إلى الصفحات
- معالجة مقاطعات الأسطوانة للوصول إلى التخزين الثانوي
- التأكد من توفر المقاطع التي تشير إليها العمليات في ذاكرة النواة
- تطبيق آلية الترحيل بين النواة والأسطوانة

التجريد المقدم: ترى المستويات الأعلى الذاكرة كما لو كانت لا نهائية. يمكن للبرامج الإشارة إلى المقاطع دون القلق بشأن قيود الذاكرة الفيزيائية أو آليات الترحيل.

يتزامن هذا المستوى مع دوران الأسطوانة، محسناً الوصول إلى الأسطوانة بتقليل زمن الوصول.

**المستوى 2: مفسر الرسائل**

يدير المستوى 2 الاتصال بوحدة التحكم. تشمل الوظائف:

- معالجة مقاطعات إدخال لوحة المفاتيح
- إدارة إخراج الطابعة الكاتبة
- توفير تجريد وحدة تحكم خاصة لكل عملية
- منع العمليات من استهلاك ذاكرة نواة مفرطة لإدخال/إخراج وحدة التحكم

التجريد المقدم: يبدو أن كل عملية لها وحدة تحكم مخصصة خاصة بها للتفاعل الحواري، حتى لو كان هناك فعلياً عتاد محدود لوحدة التحكم.

**المستوى 3: التخزين المؤقت لتدفقات الإدخال/الإخراج**

يوفر المستوى 3 إدخالاً وإخراجاً مخزناً مؤقتاً للأجهزة الطرفية:

- التخزين المؤقت للإدخال: تُخزن تدفقات البيانات الواردة مؤقتاً، مما يسمح للعمليات باستهلاك البيانات بالوتيرة الخاصة بها
- إلغاء التخزين المؤقت للإخراج: يمكن للعمليات إنتاج الإخراج دون انتظار الأجهزة الطرفية البطيئة
- تجريد الأجهزة الطرفية كقنوات اتصال منطقية

التجريد المقدم: تتفاعل العمليات مع الأجهزة الطرفية من خلال واجهات تدفق نظيفة دون القلق بشأن التوقيت الخاص بالجهاز أو متطلبات التخزين المؤقت.

**المستوى 4: برامج المستخدم المستقلة**

في هذا المستوى توجد برامج المستخدم نفسها. كل برنامج مستخدم هو عملية تسلسلية مستقلة لها وصول إلى جميع التجريدات المقدمة من المستويات 0-3:

- ذاكرة افتراضية لا نهائية (من المستوى 1)
- لا قلق بشأن جدولة المعالج (من المستوى 0)
- إدخال/إخراج بسيط من خلال واجهات قياسية (من المستويات 2-3)

يمكن تطوير واختبار برامج المستخدم بشكل مستقل دون معرفة البرامج الأخرى التي تعمل بشكل متزامن في النظام.

**المستوى 5: المشغّل**

المستوى الأعلى هو مشغّل النظام. كما لاحظ ديكسترا، هذا المستوى "لم نطبقه نحن" - إنه يمثل المشغّل البشري الذي يتفاعل مع النظام الكامل.

### قواعد التبعية الهرمية

قيد تصميم حاسم يحكم التسلسل الهرمي:

**"يمكن للعمليات فقط توليد مهام للعمليات في المستويات الأدنى."**

تضمن هذه القاعدة:

1. **عدم وجود تبعيات دائرية**: تعتمد المستويات الأعلى على المستويات الأدنى، ولكن العكس ليس صحيحاً أبداً. وهذا يمنع الانتظار الدائري والمآزق المحتملة.

2. **التحقق المستقل**: يمكن اختبار والتحقق من كل مستوى بشكل مستقل من خلال افتراض صحة المستويات الأدنى وتجاهل المستويات الأعلى تماماً.

3. **التطوير التدريجي**: يمكن بناء واختبار النظام مستوى تلو الآخر، بدءاً من المستوى 0 والإضافة التدريجية للمستويات الأعلى فقط بعد التحقق الشامل من المستويات الأدنى.

4. **الوضوح المفاهيمي**: يجعل التطبيق الصارم من الأسهل الاستدلال على سلوك النظام وتحديد آثار التغييرات.

### التجريدات في كل مستوى

يقدم كل مستوى تجريداً واحداً أو أكثر بشكل مستقل:

- **المستوى 0**: معالجات مجردة (وهم وجود معالجات متعددة)
- **المستوى 1**: ذاكرة افتراضية (مقاطع مجردة من الصفحات الفيزيائية)
- **المستوى 2**: وحدات تحكم افتراضية (كل عملية لها وحدة تحكم خاصة)
- **المستوى 3**: تدفقات مخزنة مؤقتاً (تجريد الأجهزة الطرفية)
- **المستوى 4**: مساحة حساب المستخدم
- **المستوى 5**: تشغيل وتحكم النظام

### أهمية البنية الهرمية

لم يكن التنظيم الهرمي مجرد ملاءمة تنظيمية - بل كان أساسياً لتحقيق الصحة المتحقق منها. من خلال هيكلة النظام كطبقات صارمة:

- انخفضت تعقيدات التحقق من ضربية (اختبار جميع تركيبات التفاعلات) إلى جمعية (اختبار كل مستوى بشكل مستقل)
- يمكن أن يمضي الاستدلال على خصائص النظام بالاستقراء الرياضي عبر المستويات
- تم توطين الأخطاء في مستويات محددة، مما يبسط تصحيح الأخطاء
- يمكن توصيل التصميم وفهمه بسهولة أكبر

أصبحت هذه المعمارية الطبقية مبدأً أساسياً في تصميم أنظمة التشغيل وهندسة البرمجيات بشكل أوسع.

---

### Translation Notes

- **Key terms introduced:**
  - hierarchical structure (البنية الهرمية)
  - levels (المستويات)
  - processor allocation (تخصيص المعالج)
  - segment controller (متحكم المقاطع)
  - message interpreter (مفسر الرسائل)
  - buffering (التخزين المؤقت)
  - user programs (برامج المستخدم)
  - operator (المشغّل)
  - circular dependencies (التبعيات الدائرية)
  - incremental development (التطوير التدريجي)
  - independent verification (التحقق المستقل)

- **Special handling:**
  - Clearly numbered and described all six levels
  - Maintained the strict separation between levels
  - Emphasized the "only downward dependencies" rule
  - Explained both the technical and verification benefits

- **Structural notes:**
  - This is the core section of the paper
  - The six-level hierarchy is THE system's main contribution
  - Each level's abstraction is clearly defined

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89

### Back-Translation Validation

**Sample back-translation (dependency rule):**
"'Processes can only generate tasks for processes at lower levels.' This rule ensures: (1) No circular dependencies: Higher levels depend on lower levels, but never vice versa."

**Validation:** ✓ Accurately captures the fundamental architectural constraint and its implications.
