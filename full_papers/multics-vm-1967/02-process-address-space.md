# Section 2: The Multics Concepts of Process and Address Space
## القسم 2: مفاهيم مَلتِكس للعملية وفضاء العنونة

**Section:** process-address-space
**Translation Quality:** 0.88
**Glossary Terms Used:** process, virtual memory, address space, segment, word, paging, procedure, data, protection, file system, hierarchy, directory

---

### English Version

Several interpretations of the term "process" have come into recent use. The most common usage applies the term to the activity of a processor in carrying out the computation specified by a program.[4,5] In Multics, the concept of process is intimately connected with the concept of address space. Multics processes stand in one-to-one correspondence with virtual memories. Each process runs in its own address space which is established independently of other address spaces. Processes are run on a processor of the Multics system at the discretion of the **traffic controller** module of the Multics supervisor.

The virtual memory (or address space) of a Multics process is an ordered set of as many as 2^14 **segments** each consisting of as many as 2^18 36-bit **words**. The arguments for providing a generous address space having this structure have been given by Dennis.[3] Briefly, the motivation is to avoid the necessity of procedure overlays, or the movement of data within the address space, which generally lead to naming conflicts and severe difficulties in sharing information among many processes.

Each segment is a logically distinct unit of information having attributes of length and access privilege. For present purposes, we consider two segment types:

1. data

2. procedure

A segment is treated as procedure if it is intended to be accessed for instruction fetch by a processor. Other segments (including e.g. a source program file) are considered to be data. Instruction fetch references to procedure segments are allowed, as are internal data reads. Writing into a procedure segment is normally considered invalid and is prohibited by the system. (In certain cases, reading of a procedure segment by another procedure may also be prohibited while execution is allowed.) Thus procedure segments are non-self-modifying or **pure** procedures. Instruction fetches from data segments are invalid, and any data segment may be write protected. The overall design of Multics protection mechanisms is discussed by Graham.[7]

The size of address space provided to Multics processes makes it feasible to dispense with files as a separate mechanism for addressing information held in the computer system. No distinction need be drawn between files and segments!

**The Multics directory structure** [2] is a hierarchical arrangement of directories that associates at least one symbolic name (but perhaps many) with each segment. These names have meaning that is invariant over all processes in existence. Figure 1 portrays the Multics concept of a process as a virtual memory made up of segments selected from the directory structure.

**Figure 1:** Virtual memory of a Multics process. (Shows a hierarchical directory structure on the left with multiple levels, and on the right shows a process's virtual memory as a collection of segments numbered 0 through 2^14-1, with segments selected from the directory structure)

---

### النسخة العربية

ظهرت تفسيرات عديدة لمصطلح "العملية" في الاستخدام الحديث. يطبق الاستخدام الأكثر شيوعاً المصطلح على نشاط المعالج في تنفيذ الحساب المحدد بواسطة برنامج.[4,5] في مَلتِكس، يرتبط مفهوم العملية ارتباطاً وثيقاً بمفهوم فضاء العنونة. تقف عمليات مَلتِكس في تطابق واحد لواحد مع الذاكرات الافتراضية. تعمل كل عملية في فضاء عنونة خاص بها يُنشأ بشكل مستقل عن فضاءات العنونة الأخرى. تُشغَّل العمليات على معالج من نظام مَلتِكس حسب تقدير وحدة **متحكم الحركة** في مشرف مَلتِكس.

إن الذاكرة الافتراضية (أو فضاء العنونة) لعملية مَلتِكس هي مجموعة مرتبة من ما يصل إلى 2^14 **مقطعاً** يتكون كل منها من ما يصل إلى 2^18 **كلمة** من 36 بت. قدم دينيس الحجج لتوفير فضاء عنونة سخي بهذه البنية.[3] باختصار، الدافع هو تجنب ضرورة تراكبات الإجراءات، أو حركة البيانات داخل فضاء العنونة، والتي تؤدي عموماً إلى تضاربات في التسمية وصعوبات شديدة في مشاركة المعلومات بين العديد من العمليات.

كل مقطع هو وحدة معلومات متميزة منطقياً لها سمات الطول وامتياز الوصول. للأغراض الحالية، نعتبر نوعين من المقاطع:

1. البيانات

2. الإجراءات

يُعامَل المقطع كإجراء إذا كان المقصود الوصول إليه لجلب التعليمات بواسطة معالج. تُعتبر المقاطع الأخرى (بما في ذلك على سبيل المثال ملف برنامج مصدري) بيانات. يُسمح بمراجع جلب التعليمات لمقاطع الإجراءات، وكذلك قراءات البيانات الداخلية. تُعتبر الكتابة في مقطع إجراء عادةً غير صالحة ويحظرها النظام. (في حالات معينة، قد يُحظر أيضاً قراءة مقطع إجراء بواسطة إجراء آخر بينما يُسمح بالتنفيذ.) وبالتالي فإن مقاطع الإجراءات هي إجراءات غير ذاتية التعديل أو **نقية**. جلب التعليمات من مقاطع البيانات غير صالح، ويمكن حماية أي مقطع بيانات من الكتابة. تمت مناقشة التصميم الشامل لآليات الحماية في مَلتِكس بواسطة جراهام.[7]

إن حجم فضاء العنونة المقدم لعمليات مَلتِكس يجعل من الممكن الاستغناء عن الملفات كآلية منفصلة لعنونة المعلومات المحتفظ بها في نظام الحاسوب. لا حاجة لرسم تمييز بين الملفات والمقاطع!

**بنية دليل مَلتِكس** [2] هي ترتيب هرمي للأدلة يربط اسماً رمزياً واحداً على الأقل (ولكن ربما العديد) بكل مقطع. هذه الأسماء لها معنى ثابت عبر جميع العمليات الموجودة. يصور الشكل 1 مفهوم مَلتِكس للعملية كذاكرة افتراضية تتكون من مقاطع مختارة من بنية الدليل.

**الشكل 1:** الذاكرة الافتراضية لعملية مَلتِكس. (يُظهر بنية دليل هرمية على اليسار بمستويات متعددة، وعلى اليمين يُظهر الذاكرة الافتراضية للعملية كمجموعة من المقاطع المرقمة من 0 إلى 2^14-1، مع مقاطع مختارة من بنية الدليل)

---

### Translation Notes

- **Figures referenced:** Figure 1 (Virtual memory of a Multics process)
- **Key terms introduced:**
  - Traffic controller (متحكم الحركة)
  - Segment (مقطع)
  - Word (كلمة)
  - Pure procedure (إجراء نقي)
  - Non-self-modifying (غير ذاتي التعديل)
  - Instruction fetch (جلب التعليمات)
  - Access privilege (امتياز الوصول)
  - Directory structure (بنية الدليل)
  - Symbolic name (اسم رمزي)
  - Procedure overlay (تراكب الإجراءات)
- **Equations:**
  - 2^14 segments (up to 16,384 segments)
  - 2^18 words per segment (up to 262,144 words)
  - 36-bit words
- **Citations:** References [2], [3], [4], [5], [7]
- **Special handling:**
  - Description of segment types as enumerated list
  - Explanation of pure procedures and their non-modifiable nature

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Check

Several interpretations of the term "process" have appeared in recent use. The most common usage applies the term to the activity of the processor in executing the computation specified by a program.[4,5] In MULTICS, the concept of process is closely connected to the concept of address space. MULTICS processes stand in one-to-one correspondence with virtual memories. Each process operates in its own address space that is created independently of other address spaces. Processes are run on a processor of the MULTICS system at the discretion of the traffic controller module in the MULTICS supervisor.

The virtual memory (or address space) of a MULTICS process is an ordered set of up to 2^14 segments, each consisting of up to 2^18 36-bit words. Dennis provided the arguments for providing a generous address space with this structure.[3] Briefly, the motivation is to avoid the necessity of procedure overlays or data movement within the address space, which generally lead to naming conflicts and severe difficulties in sharing information among many processes.

Each segment is a logically distinct information unit with attributes of length and access privilege. For current purposes, we consider two types of segments: data and procedures. A segment is treated as a procedure if it is intended to be accessed for instruction fetch by a processor. Other segments (including for example a source program file) are considered data. Instruction fetch references to procedure segments are allowed, as are internal data reads. Writing to a procedure segment is normally considered invalid and is prohibited by the system. (In certain cases, reading a procedure segment by another procedure may also be prohibited while execution is allowed.) Therefore, procedure segments are non-self-modifying or pure procedures. Instruction fetches from data segments are invalid, and any data segment can be write-protected. The overall design of protection mechanisms in MULTICS was discussed by Graham.[7]

The size of address space provided to MULTICS processes makes it possible to dispense with files as a separate mechanism for addressing information held in the computer system. There is no need to draw a distinction between files and segments!

The MULTICS directory structure [2] is a hierarchical arrangement of directories that associates at least one symbolic name (but perhaps many) with each segment. These names have a meaning that is constant across all existing processes. Figure 1 depicts the MULTICS concept of a process as a virtual memory consisting of segments selected from the directory structure.

**Validation:** ✓ Back-translation accurately preserves the technical details about process structure, segment types, and the unification of files and segments.
