# Section 2: Virtual Memory Architecture
## القسم 2: معمارية الذاكرة الافتراضية

**Section:** virtual-memory
**Translation Quality:** 0.87
**Glossary Terms Used:** virtual memory, address space, segment, virtual address, physical memory, segment number, word address, descriptor segment

---

### English Version

The MULTICS virtual memory system provides each process with a two-dimensional address space. A virtual address consists of two components: a segment number and a word address within that segment. This contrasts with conventional one-dimensional address spaces where all memory locations are numbered sequentially.

#### Address Structure

A virtual address in MULTICS has the form:

```
(s, w)
```

where:
- `s` is the segment number (18 bits)
- `w` is the word offset within the segment (18 bits on the GE-645 implementation)

This two-level addressing scheme provides several advantages:

1. **Large Address Space**: With 18-bit segment numbers and 18-bit word addresses, the theoretical virtual address space can accommodate 2^18 segments, each containing up to 2^18 words. This provides an address space far larger than could be supported with a single-level addressing scheme given the word size of the hardware.

2. **Logical Modularity**: The segment serves as a natural unit of program modularity. Procedures, data structures, and subsystems can each occupy separate segments, making program structure more explicit.

3. **Independent Growth**: Different segments can grow or shrink independently without affecting other segments. This eliminates the memory allocation problems that arise when a contiguous allocation must be expanded.

4. **Protection and Sharing**: Access rights and sharing can be controlled on a per-segment basis, providing fine-grained protection.

#### Segment Descriptor

Each segment in a process's address space is described by a segment descriptor that contains:

1. **Base Address**: The physical memory address where the segment begins (if the segment is in core memory)
2. **Length**: The current length of the segment in words
3. **Access Permissions**: Read, write, and execute permissions for the segment
4. **Presence Bit**: Indicates whether the segment is currently in physical memory
5. **Modified Bit**: Indicates whether the segment has been modified since being loaded from secondary storage

#### Descriptor Segment

Each process has a special segment called the descriptor segment that contains an array of segment descriptors. The descriptor segment serves as the process's segment table. When a program references virtual address (s, w), the system:

1. Uses segment number `s` as an index into the descriptor segment
2. Retrieves the segment descriptor for segment `s`
3. Checks the access permissions
4. If the segment is present in memory, adds the base address from the descriptor to the word offset `w` to compute the physical address
5. If the segment is not present, initiates a segment fault to load the segment from secondary storage

#### Segment Addressing and Naming

Segments are named using a hierarchical directory structure similar to a file system. A segment name consists of a sequence of component names separated by greater-than signs, for example:

```
>system>library>sine_cosine
```

The system maintains a directory hierarchy where each directory is itself a segment containing entries that map component names to segment numbers. To resolve a pathname to a segment number, the system traverses the directory tree, starting from the root directory.

Each process has a set of known segments - segments that the process has referenced and for which segment descriptors exist in the process's descriptor segment. When a program first references a segment by name, the system:

1. Resolves the pathname through the directory hierarchy to obtain the segment number
2. Creates a segment descriptor in the process's descriptor segment
3. Adds the segment number to the process's known segment list

Subsequent references to the same segment use the segment number directly, avoiding the overhead of pathname resolution.

#### Address Translation Hardware

The GE-645 hardware implementation includes specialized support for MULTICS addressing:

1. **Segment Associative Memory**: A small, fast associative memory that caches recently used segment descriptors. This avoids the need to access the descriptor segment in memory for every virtual address translation.

2. **Address Formation**: The hardware automatically combines the segment number and word offset to form virtual addresses. Special instructions allow programs to manipulate segment numbers and construct inter-segment references.

3. **Bounds Checking**: The hardware automatically checks that word addresses are within segment bounds and that the requested access mode (read, write, or execute) is permitted by the segment descriptor.

The virtual memory mechanism is transparent to most programs. Programs reference virtual addresses using ordinary load and store instructions. The hardware and operating system cooperate to translate virtual addresses to physical addresses and to handle segment faults when referenced segments are not in memory.

---

### النسخة العربية

يوفر نظام الذاكرة الافتراضية في مَلتِكس لكل عملية فضاء عنونة ثنائي الأبعاد. يتكون العنوان الافتراضي من مكونين: رقم مقطع وعنوان كلمة داخل ذلك المقطع. يتناقض هذا مع فضاءات العنونة أحادية البعد التقليدية حيث يتم ترقيم جميع مواقع الذاكرة بشكل تسلسلي.

#### بنية العنوان

العنوان الافتراضي في مَلتِكس له الشكل:

```
(s, w)
```

حيث:
- `s` هو رقم المقطع (18 بت)
- `w` هو إزاحة الكلمة داخل المقطع (18 بت في تطبيق GE-645)

يوفر نظام العنونة ثنائي المستوى هذا عدة مزايا:

1. **فضاء عنونة كبير**: مع أرقام مقاطع من 18 بت وعناوين كلمات من 18 بت، يمكن لفضاء العنونة الافتراضي النظري استيعاب 2^18 مقطع، كل منها يحتوي على ما يصل إلى 2^18 كلمة. يوفر هذا فضاء عنونة أكبر بكثير مما يمكن دعمه بنظام عنونة أحادي المستوى بالنظر إلى حجم كلمة الأجهزة.

2. **النمطية المنطقية**: يعمل المقطع كوحدة طبيعية لنمطية البرنامج. يمكن أن تشغل الإجراءات وبنى البيانات والأنظمة الفرعية مقاطع منفصلة، مما يجعل بنية البرنامج أكثر وضوحاً.

3. **النمو المستقل**: يمكن للمقاطع المختلفة أن تنمو أو تنكمش بشكل مستقل دون التأثير على المقاطع الأخرى. يلغي هذا مشاكل تخصيص الذاكرة التي تنشأ عندما يجب توسيع التخصيص المتجاور.

4. **الحماية والمشاركة**: يمكن التحكم في حقوق الوصول والمشاركة على أساس كل مقطع، مما يوفر حماية دقيقة التفاصيل.

#### واصف المقطع

يوصف كل مقطع في فضاء عنونة العملية بواصف مقطع يحتوي على:

1. **العنوان الأساسي**: عنوان الذاكرة الفيزيائية حيث يبدأ المقطع (إذا كان المقطع في الذاكرة الأساسية)
2. **الطول**: الطول الحالي للمقطع بالكلمات
3. **أذونات الوصول**: أذونات القراءة والكتابة والتنفيذ للمقطع
4. **بت الحضور**: يشير إلى ما إذا كان المقطع موجوداً حالياً في الذاكرة الفيزيائية
5. **بت التعديل**: يشير إلى ما إذا كان المقطع قد تم تعديله منذ تحميله من التخزين الثانوي

#### مقطع الواصفات

لكل عملية مقطع خاص يسمى مقطع الواصفات يحتوي على مصفوفة من واصفات المقاطع. يعمل مقطع الواصفات كجدول مقاطع العملية. عندما يشير البرنامج إلى العنوان الافتراضي (s, w)، يقوم النظام بـ:

1. استخدام رقم المقطع `s` كمؤشر في مقطع الواصفات
2. استرجاع واصف المقطع للمقطع `s`
3. فحص أذونات الوصول
4. إذا كان المقطع موجوداً في الذاكرة، يضيف العنوان الأساسي من الواصف إلى إزاحة الكلمة `w` لحساب العنوان الفيزيائي
5. إذا لم يكن المقطع موجوداً، يبدأ خطأ مقطع لتحميل المقطع من التخزين الثانوي

#### عنونة وتسمية المقاطع

يتم تسمية المقاطع باستخدام بنية دليل هرمية مشابهة لنظام الملفات. يتكون اسم المقطع من تسلسل أسماء مكونات مفصولة بعلامات أكبر من، على سبيل المثال:

```
>system>library>sine_cosine
```

يحتفظ النظام بتسلسل هرمي للدليل حيث كل دليل هو نفسه مقطع يحتوي على إدخالات تربط أسماء المكونات بأرقام المقاطع. لحل مسار إلى رقم مقطع، يجتاز النظام شجرة الدليل، بدءاً من الدليل الجذر.

لكل عملية مجموعة من المقاطع المعروفة - المقاطع التي أشارت إليها العملية والتي توجد لها واصفات مقاطع في مقطع واصفات العملية. عندما يشير البرنامج لأول مرة إلى مقطع بالاسم، يقوم النظام بـ:

1. حل المسار من خلال التسلسل الهرمي للدليل للحصول على رقم المقطع
2. إنشاء واصف مقطع في مقطع واصفات العملية
3. إضافة رقم المقطع إلى قائمة المقاطع المعروفة للعملية

تستخدم الإشارات اللاحقة لنفس المقطع رقم المقطع مباشرة، مما يتجنب الحمل الزائد لحل المسار.

#### أجهزة ترجمة العناوين

يتضمن تطبيق الأجهزة GE-645 دعماً متخصصاً لعنونة مَلتِكس:

1. **ذاكرة مقاطع ترابطية**: ذاكرة ترابطية صغيرة وسريعة تخزن مؤقتاً واصفات المقاطع المستخدمة مؤخراً. يتجنب هذا الحاجة إلى الوصول إلى مقطع الواصفات في الذاكرة لكل ترجمة عنوان افتراضي.

2. **تكوين العنوان**: تجمع الأجهزة تلقائياً رقم المقطع وإزاحة الكلمة لتكوين عناوين افتراضية. تسمح التعليمات الخاصة للبرامج بمعالجة أرقام المقاطع وبناء مراجع بين المقاطع.

3. **فحص الحدود**: تتحقق الأجهزة تلقائياً من أن عناوين الكلمات ضمن حدود المقطع وأن وضع الوصول المطلوب (قراءة أو كتابة أو تنفيذ) مسموح به بواسطة واصف المقطع.

آلية الذاكرة الافتراضية شفافة لمعظم البرامج. تشير البرامج إلى العناوين الافتراضية باستخدام تعليمات التحميل والتخزين العادية. تتعاون الأجهزة ونظام التشغيل لترجمة العناوين الافتراضية إلى عناوين فيزيائية ولمعالجة أخطاء المقاطع عندما لا تكون المقاطع المشار إليها في الذاكرة.

---

### Translation Notes

- **Figures referenced:** None explicitly, but describes address structure conceptually
- **Key terms introduced:** two-dimensional address space (فضاء عنونة ثنائي الأبعاد), segment descriptor (واصف المقطع), descriptor segment (مقطع الواصفات), segment fault (خطأ مقطع), associative memory (ذاكرة ترابطية), bounds checking (فحص الحدود)
- **Equations:** Address format (s, w) and address space size calculations (2^18)
- **Citations:** Reference to GE-645 hardware
- **Special handling:** Preserved code examples showing pathname notation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
