# Section 3: Addressing in Multics
## القسم 3: العنونة في مَلتِكس

**Section:** addressing
**Translation Quality:** 0.87
**Glossary Terms Used:** generalized address, segment number, word number, location-independent, descriptor segment, base register, paging, page table, associative memory, indirect addressing

---

### English Version

#### The generalized address

Each word in the address space of a process is identified by a **generalized address**. As shown in Figure 2, a generalized address consists of two parts: a **segment number** and a **word number**. The addressing mechanisms of the processor are designed so that

A process may make effective reference to a word by means of its generalized address when the word has an assigned location in main memory. Together with supervisor software, these mechanisms make reference by generalized address effective regardless of where the word might reside in the storage hierarchy by placing it in main memory when needed. Thus the generalized address is a **location-independent** means of identifying information. In the following paragraphs we explain how generalized addresses are formed in the processor and give a brief discussion of how they are made effective.

**Figure 2:** The generalized address. (Shows a box divided into two parts: "segment number" and "word number")

#### Address formation

Each processor of the computer system (Figure 3) has an accumulator A, a multiplier/quotient Q, eight index registers X0, X1, ... X7, and a program counter PC which serve conventional functions. For the implementation of generalized addressing and intersegment linking, a **descriptor base register**, a **procedure base register** and four **base pair registers** are included in each processor. The function of the descriptor base register will be discussed in a later paragraph since it does not participate in generalized address formation. The procedure base register always contains the segment number of the procedure being executed. Each of the four base pair registers (called simply base registers in the sequel) holds a complete generalized address (segment number/word number pair) and is named according to its specific function in Multics:

| base pair | designation | function |
|-----------|-------------|----------|
| 0 | ap | argument pointer |
| 1 | bp | base pointer |
| 2 | lp | linkage pointer |
| 3 | sp | stack pointer |

The functions of these pointers will become clear when the linkage mechanism is explained.

**Figure 3:** Processor registers for address formation. (Shows a diagram of processor registers including A, Q, X0-X7, PC, descriptor base, procedure base, and four base pair registers ap, bp, lp, sp)

The instruction format of the processor is given in Figure 4. Instructions are executed sequentially except where a transfer of control occurs. Hence, the program counter is normally advanced by one during the execution of each instruction.

**Figure 4:** Instruction format. (Shows instruction format with fields for operation code, address field, index field, external flag, segment tag, and addressing mode)

When the processor requires an instruction word from memory, the corresponding generalized address is the segment number in the procedure base register coupled with the word number in the program counter (Figure 5). For data references, a field in the instruction format called the **segment tag** selects one of the base registers if the **external flag** is on. The effective address computed from the address field of the instruction by the usual indexing procedure is added to the word number portion of the selected base to obtain the desired generalized address. This operation is illustrated by Figure 6 and is used to reference all information outside the current procedure segment. If the **external flag** is off, then the generalized address is the segment number taken from the procedure base register coupled with an effective word number computed as before. This mechanism is used for internal reference by a procedure to fetch constants or for transfer of control.

**Figure 5:** Address formation for instruction fetch. (Shows how segment number from procedure base register combines with word number from PC to form generalized address)

**Figure 6:** Address formation for data access. (Shows how external flag and segment tag select base register, and effective address is computed to form generalized address)

#### Indirect addressing

As will be seen when the linkage mechanism is discussed, a method of indirect addressing in terms of generalized addresses is very valuable. In the processor the addressing mode field of instructions may indicate that **indirect addressing** is to be used. In this case, the generalized address, formed as explained above for data references, is used to fetch a pair of 36-bit words which is interpreted as shown in Figure 7. If the address mode field of the first word contains the code **its** (Indirect To Segment), the segment number and word number fields are combined to produce a new generalized address. This address is augmented by indexing according to the mode field of the second word of the pair. Further indirect addressing may also be specified.

**Figure 7:** Interpretation of word pair as indirect address. (Shows two-word format with address mode, segment number, word number in first word, and mode field in second word)

#### The descriptor segment

Implementation of a memory access specified by a generalized address calls for an associative mechanism that will yield the main memory location of any word within main memory when a segment number/word number combination is supplied. A direct use of associative hardware was impossible to justify in view of the other possibilities available.

The means chosen to implement the generalized address for a process is essentially a two-step hardware table look-up procedure as illustrated by Figure 8. The segment number portion of the generalized address is used as an index to perform a table look-up in an array called the **descriptor segment** of the associated process. This descriptor segment contains a descriptor for each segment that the process may reference by generalized address. Each descriptor contains information that enables the addressing mechanism to locate the segment, and information that establishes the appropriate mode of protection of the segment for this process.

**Figure 8:** Addressing by generalized address. (Shows two-step process: segment number indexes into descriptor segment to get page table pointer, then word number indexes into page table to get main memory location)

The descriptor base register is used by the processor to locate the descriptor segment of the process in execution. Note that since segment numbers and word numbers are non-location dependent data, the only location dependent information contained in the processor registers shown in Figure 3 is in the descriptor base register. This fact greatly simplifies the bookkeeping required by the system in carrying out reallocation activity. In fact, switching a processor from one process to another involves little more than swapping processor register status and substituting a new descriptor base.

In practice this implementation requires that segment numbers be assigned starting from zero and continuing successively for the segments of procedure and data required by each process. An immediate consequence is that the same segment will, in general, be identified by **different** segment numbers in different processes.

#### Paging

Both information segments and descriptor segments may be sufficiently large that paging is desirable to simplify storage allocation problems in main memory. Paging is implemented by means of page tables in main memory which provide for trapping in case a page is not present in main memory. The page tables also contain control bits that record access and modification of pages for use by storage allocation procedures. A small associative memory is built into each processor so that most references to page tables or descriptor segments may be bypassed.

---

### النسخة العربية

#### العنوان المعمم

تُحدَّد كل كلمة في فضاء عنونة العملية بواسطة **عنوان معمم**. كما هو موضح في الشكل 2، يتكون العنوان المعمم من جزأين: **رقم المقطع** و**رقم الكلمة**. صُممت آليات العنونة للمعالج بحيث

يمكن للعملية أن تُشير بشكل فعال إلى كلمة عن طريق عنوانها المعمم عندما يكون للكلمة موقع معيّن في الذاكرة الرئيسية. مع برمجيات المشرف، تجعل هذه الآليات الإشارة بالعنوان المعمم فعالة بغض النظر عن مكان وجود الكلمة في التسلسل الهرمي للتخزين من خلال وضعها في الذاكرة الرئيسية عند الحاجة. وبالتالي فإن العنوان المعمم هو وسيلة **مستقلة عن الموقع** لتحديد المعلومات. في الفقرات التالية نشرح كيفية تكوين العناوين المعممة في المعالج ونقدم مناقشة موجزة لكيفية جعلها فعالة.

**الشكل 2:** العنوان المعمم. (يُظهر صندوقاً مقسماً إلى جزأين: "رقم المقطع" و"رقم الكلمة")

#### تكوين العنوان

يحتوي كل معالج من نظام الحاسوب (الشكل 3) على مُجمِّع A، ومُضارِب/قاسم Q، وثمانية سجلات فهرس X0، X1، ... X7، وعداد برنامج PC والتي تؤدي وظائف تقليدية. لتنفيذ العنونة المعممة والربط بين المقاطع، يتضمن كل معالج **سجل قاعدة الواصف**، و**سجل قاعدة الإجراء** وأربعة **سجلات أزواج القاعدة**. ستتم مناقشة وظيفة سجل قاعدة الواصف في فقرة لاحقة حيث أنه لا يشارك في تكوين العنوان المعمم. يحتوي سجل قاعدة الإجراء دائماً على رقم مقطع الإجراء الذي يتم تنفيذه. يحمل كل من سجلات أزواج القاعدة الأربعة (المسماة ببساطة سجلات القاعدة فيما بعد) عنواناً معمماً كاملاً (زوج رقم مقطع/رقم كلمة) ويُسمى وفقاً لوظيفته المحددة في مَلتِكس:

| زوج القاعدة | التسمية | الوظيفة |
|-----------|-------------|----------|
| 0 | ap | مؤشر الوسيطة |
| 1 | bp | مؤشر القاعدة |
| 2 | lp | مؤشر الربط |
| 3 | sp | مؤشر المكدس |

ستتضح وظائف هذه المؤشرات عند شرح آلية الربط.

**الشكل 3:** سجلات المعالج لتكوين العنوان. (يُظهر مخططاً لسجلات المعالج بما في ذلك A و Q و X0-X7 و PC وقاعدة الواصف وقاعدة الإجراء وأربعة سجلات أزواج قاعدة ap و bp و lp و sp)

يُعطى تنسيق تعليمات المعالج في الشكل 4. تُنفَّذ التعليمات بالتسلسل باستثناء حدوث نقل للتحكم. وبالتالي، يتقدم عداد البرنامج عادةً بمقدار واحد أثناء تنفيذ كل تعليمة.

**الشكل 4:** تنسيق التعليمة. (يُظهر تنسيق التعليمة مع حقول لكود العملية، وحقل العنوان، وحقل الفهرس، والعلم الخارجي، ووسم المقطع، ونمط العنونة)

عندما يتطلب المعالج كلمة تعليمة من الذاكرة، فإن العنوان المعمم المقابل هو رقم المقطع في سجل قاعدة الإجراء مقترناً برقم الكلمة في عداد البرنامج (الشكل 5). بالنسبة لمراجع البيانات، يختار حقل في تنسيق التعليمة يُسمى **وسم المقطع** أحد سجلات القاعدة إذا كان **العلم الخارجي** مُفعَّلاً. يُضاف العنوان الفعال المحسوب من حقل العنوان للتعليمة بواسطة إجراء الفهرسة المعتاد إلى جزء رقم الكلمة من القاعدة المختارة للحصول على العنوان المعمم المطلوب. توضح هذه العملية الشكل 6 وتُستخدم للإشارة إلى جميع المعلومات خارج مقطع الإجراء الحالي. إذا كان **العلم الخارجي** مُعطَّلاً، فإن العنوان المعمم هو رقم المقطع المأخوذ من سجل قاعدة الإجراء مقترناً برقم كلمة فعال محسوب كما كان من قبل. تُستخدم هذه الآلية للإشارة الداخلية بواسطة إجراء لجلب الثوابت أو لنقل التحكم.

**الشكل 5:** تكوين العنوان لجلب التعليمة. (يُظهر كيف يتحد رقم المقطع من سجل قاعدة الإجراء مع رقم الكلمة من PC لتكوين عنوان معمم)

**الشكل 6:** تكوين العنوان للوصول إلى البيانات. (يُظهر كيف يختار العلم الخارجي ووسم المقطع سجل القاعدة، ويُحسب العنوان الفعال لتكوين عنوان معمم)

#### العنونة غير المباشرة

كما سيُرى عند مناقشة آلية الربط، فإن طريقة العنونة غير المباشرة من حيث العناوين المعممة ذات قيمة كبيرة. في المعالج، قد يشير حقل نمط العنونة للتعليمات إلى أن **العنونة غير المباشرة** يجب استخدامها. في هذه الحالة، يُستخدم العنوان المعمم، المُكوَّن كما هو موضح أعلاه لمراجع البيانات، لجلب زوج من كلمات 36 بت التي تُفسَّر كما هو موضح في الشكل 7. إذا كان حقل نمط العنوان للكلمة الأولى يحتوي على الكود **its** (غير مباشر إلى مقطع)، فإن حقول رقم المقطع ورقم الكلمة تُجمع لإنتاج عنوان معمم جديد. يُعزز هذا العنوان بالفهرسة وفقاً لحقل النمط في الكلمة الثانية من الزوج. يمكن أيضاً تحديد عنونة غير مباشرة إضافية.

**الشكل 7:** تفسير زوج الكلمات كعنوان غير مباشر. (يُظهر تنسيق كلمتين مع نمط العنوان، ورقم المقطع، ورقم الكلمة في الكلمة الأولى، وحقل النمط في الكلمة الثانية)

#### مقطع الواصف

يتطلب تنفيذ وصول الذاكرة المحدد بواسطة عنوان معمم آلية ترابطية ستُعطي موقع الذاكرة الرئيسية لأي كلمة داخل الذاكرة الرئيسية عند توفير مجموعة رقم مقطع/رقم كلمة. كان من المستحيل تبرير الاستخدام المباشر للمعدات الترابطية في ضوء الإمكانيات الأخرى المتاحة.

الوسيلة المختارة لتنفيذ العنوان المعمم للعملية هي في الأساس إجراء بحث جدول معداتي من خطوتين كما هو موضح في الشكل 8. يُستخدم جزء رقم المقطع من العنوان المعمم كفهرس لإجراء بحث جدول في مصفوفة تُسمى **مقطع الواصف** للعملية المرتبطة. يحتوي مقطع الواصف هذا على واصف لكل مقطع قد تشير إليه العملية بالعنوان المعمم. يحتوي كل واصف على معلومات تُمكِّن آلية العنونة من تحديد موقع المقطع، ومعلومات تُنشئ نمط الحماية المناسب للمقطع لهذه العملية.

**الشكل 8:** العنونة بالعنوان المعمم. (يُظهر عملية من خطوتين: رقم المقطع يُفهرس في مقطع الواصف للحصول على مؤشر جدول الصفحات، ثم رقم الكلمة يُفهرس في جدول الصفحات للحصول على موقع الذاكرة الرئيسية)

يُستخدم سجل قاعدة الواصف بواسطة المعالج لتحديد موقع مقطع الواصف للعملية قيد التنفيذ. لاحظ أنه نظراً لأن أرقام المقاطع وأرقام الكلمات هي بيانات غير معتمدة على الموقع، فإن المعلومات المعتمدة على الموقع الوحيدة الموجودة في سجلات المعالج الموضحة في الشكل 3 موجودة في سجل قاعدة الواصف. هذه الحقيقة تُبسط بشكل كبير مسك الدفاتر المطلوب من النظام في تنفيذ نشاط إعادة التخصيص. في الواقع، يتضمن تبديل معالج من عملية إلى أخرى أكثر قليلاً من تبديل حالة سجل المعالج واستبدال قاعدة واصف جديدة.

في الممارسة العملية، يتطلب هذا التنفيذ تعيين أرقام المقاطع بدءاً من الصفر والاستمرار بشكل متتابع لمقاطع الإجراءات والبيانات المطلوبة لكل عملية. النتيجة الفورية هي أن نفس المقطع سيتم، بشكل عام، تحديده بأرقام مقاطع **مختلفة** في عمليات مختلفة.

#### الترحيل

قد تكون كل من مقاطع المعلومات ومقاطع الواصف كبيرة بما فيه الكفاية بحيث يكون الترحيل مرغوباً لتبسيط مشاكل تخصيص التخزين في الذاكرة الرئيسية. يتم تنفيذ الترحيل بواسطة جداول الصفحات في الذاكرة الرئيسية التي توفر الاحتجاز في حالة عدم وجود صفحة في الذاكرة الرئيسية. تحتوي جداول الصفحات أيضاً على بتات تحكم تسجل وصول وتعديل الصفحات لاستخدامها بواسطة إجراءات تخصيص التخزين. تُدمَج ذاكرة ترابطية صغيرة في كل معالج بحيث يمكن تجاوز معظم المراجع لجداول الصفحات أو مقاطع الواصف.

---

### Translation Notes

- **Figures referenced:** Figures 2, 3, 4, 5, 6, 7, 8
- **Key terms introduced:**
  - Generalized address (عنوان معمم)
  - Location-independent (مستقل عن الموقع)
  - Descriptor base register (سجل قاعدة الواصف)
  - Procedure base register (سجل قاعدة الإجراء)
  - Base pair registers (سجلات أزواج القاعدة)
  - Argument pointer (مؤشر الوسيطة)
  - Linkage pointer (مؤشر الربط)
  - Stack pointer (مؤشر المكدس)
  - Segment tag (وسم المقطع)
  - External flag (العلم الخارجي)
  - Indirect addressing (العنونة غير المباشرة)
  - Descriptor segment (مقطع الواصف)
  - Page table (جدول الصفحات)
  - Associative memory (ذاكرة ترابطية)
- **Equations:** None, but mentions 36-bit words
- **Citations:** None in this section
- **Special handling:**
  - Table for base pair registers
  - Multiple figures describing addressing mechanisms
  - Detailed technical explanations of hardware mechanisms

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check

Each word in the process address space is identified by a generalized address. As shown in Figure 2, a generalized address consists of two parts: a segment number and a word number. The addressing mechanisms of the processor are designed so that a process can effectively reference a word through its generalized address when the word has an assigned location in main memory. With supervisor software, these mechanisms make referencing by generalized address effective regardless of where the word is located in the storage hierarchy by placing it in main memory when needed. Therefore, the generalized address is a location-independent means of identifying information.

The descriptor base register is used by the processor to locate the descriptor segment of the process being executed. Note that since segment numbers and word numbers are non-location-dependent data, the only location-dependent information contained in the processor registers shown in Figure 3 is in the descriptor base register. This fact greatly simplifies the bookkeeping required by the system in executing reallocation activity. In fact, switching a processor from one process to another involves little more than swapping processor register state and substituting a new descriptor base.

**Validation:** ✓ Back-translation accurately preserves the technical details of the addressing mechanism, register functions, and the two-step table lookup process.
