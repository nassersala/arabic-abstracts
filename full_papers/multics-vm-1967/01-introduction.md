# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** virtual memory, process, multiprogramming, paging, segmentation, operating system, protection, sharing, auxiliary storage, dynamic linking

---

### English Version

In Multics (Multiplexed Information and Computing Service), fundamental design decisions were made so the system would effectively serve the computing needs of a large community of users with diverse interests, operating principally from remote terminals. Among the objectives were these three:

1. **To give the system responsibility for managing the distribution of information among the levels of the physical storage hierarchy.**

   The efficient multiprogramming of many computations makes this essential, but of greater importance is the fact that users are relieved of the burden of pre-planning the transfer of information between storage levels, and programs become independent of the nature of the auxiliary storage devices in the system.

2. **To permit a degree of programming generality not previously practical.**

   This includes the ability of one procedure to use another procedure knowing only its name, and without knowledge of its requirements for storage, or the additional procedures upon which it may in turn call.

3. **To permit sharing of procedures and data among users subject only to proper authorization.**

   Sharing of procedures in core memory is extremely valuable in a multiplexed system so that the cluttering of auxiliary storage with myriad copies of routines is avoided, and so unnecessary information transfers are eliminated. The sharing of data objects in core memory is necessary to permit efficient and close interaction between processes.

These objectives led to the design of a computer system [6] (the General Electric Model 645) embodying the concepts of paging [8] and segmentation [3] on which the initial implementation of Multics will run.

This paper explains some of the more fundamental aspects of the Multics design. The concepts of "process" and "address space" as implemented in Multics are defined, some details of the addressing mechanism are given, and the mechanism by which "dynamic linking" is accomplished is explained.

---

### النسخة العربية

في مَلتِكس (خدمة المعلومات والحوسبة المتعددة)، اتُّخذت قرارات تصميم أساسية بحيث يخدم النظام بفعالية الاحتياجات الحاسوبية لمجتمع كبير من المستخدمين ذوي اهتمامات متنوعة، يعملون بشكل أساسي من محطات طرفية بعيدة. كانت الأهداف الثلاثة التالية من بين الأهداف الرئيسية:

1. **منح النظام مسؤولية إدارة توزيع المعلومات بين مستويات التسلسل الهرمي للتخزين الفيزيائي.**

   إن البرمجة المتعددة الفعالة للعديد من العمليات الحسابية تجعل هذا ضرورياً، ولكن الأهم من ذلك هو أن المستخدمين يُعفَون من عبء التخطيط المسبق لنقل المعلومات بين مستويات التخزين، وتصبح البرامج مستقلة عن طبيعة أجهزة التخزين المساعدة في النظام.

2. **السماح بدرجة من عمومية البرمجة لم تكن عملية سابقاً.**

   يشمل ذلك قدرة إجراء واحد على استخدام إجراء آخر مع معرفة اسمه فقط، ودون معرفة متطلباته من التخزين، أو الإجراءات الإضافية التي قد يستدعيها بدوره.

3. **السماح بمشاركة الإجراءات والبيانات بين المستخدمين مع مراعاة التفويض المناسب فقط.**

   تُعدّ مشاركة الإجراءات في الذاكرة الأساسية ذات قيمة كبيرة في نظام متعدد الوصول بحيث يُتجنب ازدحام التخزين المساعد بنسخ لا حصر لها من الروتينات، وبالتالي يتم القضاء على عمليات نقل المعلومات غير الضرورية. إن مشاركة كائنات البيانات في الذاكرة الأساسية ضرورية للسماح بتفاعل فعال ووثيق بين العمليات.

أدت هذه الأهداف إلى تصميم نظام حاسوبي [6] (طراز جنرال إلكتريك 645) يجسد مفاهيم الترحيل [8] والتجزئة [3] الذي سيعمل عليه التطبيق الأولي لمَلتِكس.

تشرح هذه الورقة بعض الجوانب الأساسية لتصميم مَلتِكس. يتم تعريف مفاهيم "العملية" و"فضاء العنونة" كما هي مطبقة في مَلتِكس، وتُقدَّم بعض تفاصيل آلية العنونة، وتُشرح الآلية التي يتم من خلالها "الربط الديناميكي".

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Multiplexed Information and Computing Service (خدمة المعلومات والحوسبة المتعددة)
  - Remote terminals (محطات طرفية بعيدة)
  - Storage hierarchy (التسلسل الهرمي للتخزين)
  - Core memory (الذاكرة الأساسية)
  - Auxiliary storage (التخزين المساعد)
  - Programming generality (عمومية البرمجة)
  - Authorization (التفويض)
  - General Electric Model 645 (طراز جنرال إلكتريك 645)
- **Equations:** None
- **Citations:** References [3], [6], [8]
- **Special handling:** Three numbered objectives presented as a list

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Check

In MULTICS (Multiplexed Information and Computing Service), fundamental design decisions were made so that the system would effectively serve the computational needs of a large community of users with diverse interests, operating primarily from remote terminals. The following three objectives were among the main goals:

1. Giving the system responsibility for managing the distribution of information among the levels of the physical storage hierarchy. Efficient multiprogramming of many computational processes makes this necessary, but more importantly, users are relieved of the burden of pre-planning information transfer between storage levels, and programs become independent of the nature of auxiliary storage devices in the system.

2. Allowing a degree of programming generality that was not previously practical. This includes the ability of one procedure to use another procedure knowing only its name, without knowledge of its storage requirements or additional procedures it may call in turn.

3. Allowing sharing of procedures and data among users with consideration of proper authorization only. Sharing procedures in main memory is of great value in a multiplexed system so that auxiliary storage is not cluttered with countless copies of routines, thus eliminating unnecessary information transfers. Sharing data objects in main memory is necessary to allow efficient and close interaction between processes.

These objectives led to the design of a computer system [6] (General Electric Model 645) that embodies the concepts of paging [8] and segmentation [3] on which the initial implementation of MULTICS will run.

This paper explains some fundamental aspects of MULTICS design. The concepts of "process" and "address space" as implemented in MULTICS are defined, some details of the addressing mechanism are provided, and the mechanism by which "dynamic linking" is accomplished is explained.

**Validation:** ✓ Back-translation accurately preserves the three objectives and their explanations, maintaining technical precision.
