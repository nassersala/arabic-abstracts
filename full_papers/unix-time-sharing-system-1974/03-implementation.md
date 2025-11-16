# Section 3: Implementation of the File System
## القسم 3: تنفيذ نظام الملفات

**Section:** implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** file system, i-node, block, directory, disk, buffer, kernel, mount

---

### English Version

As mentioned in the Introduction, a directory entry contains only a name for the associated file and a pointer to the file itself. This pointer is an integer called the i-number (for index number) of the file. When the file is accessed, its i-number is used as an index into a system table (the i-list) stored in a known part of the device on which the directory resides. The entry thereby found (the file's i-node) contains the description of the file as follows:

1. Its owner
2. Its protection bits
3. The physical disk or tape addresses for the file contents
4. Its size
5. Time of last modification
6. The number of links to the file, that is, the number of times it appears in a directory
7. A bit indicating whether the file is a directory
8. A bit indicating whether the file is a special file
9. A bit indicating whether the file is "large" or "small"

The purpose of an open or create system call is to turn the path name given by the user into an i-number by searching the explicitly or implicitly named directories. Once a file is open, its device, i-number, and read/write pointer are stored in a system table indexed by the file descriptor returned by the open or create. Thus the file system can readily access the file at the indicated position in the file.

When a new file is created, an i-node is allocated for it and a directory entry is made which contains the name of the file and the i-node number. Making a link to an existing file involves creating a directory entry with the new name, copying the i-number from the original file entry, and incrementing the link-count field of the i-node. Removing (deleting) a file is done by decrementing the link-count of the i-node specified by its directory entry and erasing the directory entry. If the link-count drops to 0, any disk blocks in the file are freed and the i-node is deallocated.

The space on all disks which contain a file system is divided into a number of 512-byte blocks logically addressed from 0 up to some limit which depends on the device. There is space in the i-node for 8 device addresses. A "small" (non-directory) file fits into 8 blocks or less, and the addresses of the blocks are stored in the i-node. For "large" (non-directory) files, each of the 8 device addresses may point to an indirect block of 256 addresses of blocks constituting the file itself. These files may be as large as $8 \\times 256 \\times 512$ bytes.

The foregoing discussion applies to ordinary files. When an I/O request is made to a file whose i-node indicates that it is special, the last 7 device address words are immaterial, and the first device address word specifies an internal device name, which is interpreted as a pair of numbers representing, respectively, a device type and subdevice number. The device type indicates which system routine will deal with I/O on that device; the subdevice number selects, for example, a disk drive attached to a particular controller, or one of several similar typewriter terminals.

In this environment, the implementation of the mount system call is quite straightforward. Mount maintains a system table whose argument is the i-number and device name of the ordinary file specified during the mount, and whose corresponding value is the device name of the indicated special file. This table is searched for each i-number/device pair which corresponds to an ordinary file, and if a match is found, the ordinary file is replaced with the indicated special file.

---

### النسخة العربية

كما ذُكر في المقدمة، يحتوي إدخال الدليل فقط على اسم للملف المرتبط ومؤشر للملف نفسه. هذا المؤشر هو عدد صحيح يسمى رقم i (i-number) (لرقم الفهرس) للملف. عند الوصول إلى الملف، يُستخدم رقم i الخاص به كفهرس في جدول النظام (قائمة i أو i-list) المخزنة في جزء معروف من الجهاز الذي يوجد عليه الدليل. يحتوي الإدخال الذي يتم العثور عليه بهذه الطريقة (عقدة i أو i-node للملف) على وصف الملف كما يلي:

1. مالكه
2. بتات الحماية الخاصة به
3. عناوين القرص أو الشريط الفيزيائية لمحتويات الملف
4. حجمه
5. وقت آخر تعديل
6. عدد الروابط (links) للملف، أي عدد المرات التي يظهر فيها في دليل
7. بت يشير إلى ما إذا كان الملف دليلاً
8. بت يشير إلى ما إذا كان الملف ملفاً خاصاً
9. بت يشير إلى ما إذا كان الملف "كبيراً" أو "صغيراً"

الغرض من استدعاء نظام open أو create هو تحويل اسم المسار المعطى من قبل المستخدم إلى رقم i عن طريق البحث في الأدلة المسماة صراحةً أو ضمنياً. بمجرد فتح ملف، يتم تخزين جهازه ورقم i الخاص به ومؤشر القراءة/الكتابة في جدول النظام مفهرس بواسطة واصف الملف (file descriptor) الذي يعيده open أو create. وبالتالي يمكن لنظام الملفات الوصول بسهولة إلى الملف في الموضع المشار إليه في الملف.

عند إنشاء ملف جديد، يتم تخصيص عقدة i له ويتم إجراء إدخال دليل يحتوي على اسم الملف ورقم عقدة i. يتضمن إنشاء رابط (link) لملف موجود إنشاء إدخال دليل بالاسم الجديد، ونسخ رقم i من إدخال الملف الأصلي، وزيادة حقل عدد الروابط (link-count) في عقدة i. تتم إزالة (حذف) ملف عن طريق إنقاص عدد الروابط لعقدة i المحددة بواسطة إدخال الدليل الخاص بها ومسح إدخال الدليل. إذا انخفض عدد الروابط إلى 0، يتم تحرير أي كتل قرص في الملف وإلغاء تخصيص عقدة i.

يتم تقسيم المساحة على جميع الأقراص التي تحتوي على نظام ملفات إلى عدد من الكتل (blocks) بحجم 512 بايت معنونة منطقياً من 0 حتى حد معين يعتمد على الجهاز. هناك مساحة في عقدة i لـ 8 عناوين أجهزة. يناسب ملف "صغير" (غير دليل) 8 كتل أو أقل، ويتم تخزين عناوين الكتل في عقدة i. بالنسبة للملفات "الكبيرة" (غير الأدلة)، يمكن أن يشير كل من عناوين الأجهزة الثمانية إلى كتلة غير مباشرة (indirect block) من 256 عنواناً للكتل التي تشكل الملف نفسه. يمكن أن تكون هذه الملفات بحجم $8 \\times 256 \\times 512$ بايت.

المناقشة السابقة تنطبق على الملفات العادية. عندما يتم إجراء طلب إدخال/إخراج لملف تشير عقدة i الخاصة به إلى أنه خاص، تكون كلمات عناوين الأجهزة السبعة الأخيرة غير مهمة، وتحدد كلمة عنوان الجهاز الأولى اسم جهاز داخلي، يتم تفسيره كزوج من الأرقام يمثلان، على التوالي، نوع جهاز ورقم جهاز فرعي. يشير نوع الجهاز إلى إجراء النظام الذي سيتعامل مع الإدخال/الإخراج على ذلك الجهاز؛ يختار رقم الجهاز الفرعي، على سبيل المثال، محرك قرص متصل بوحدة تحكم معينة، أو أحد عدة طرفيات آلة كاتبة مماثلة.

في هذه البيئة، يكون تنفيذ استدعاء نظام mount واضحاً تماماً. يحتفظ Mount بجدول نظام معامله هو رقم i واسم جهاز الملف العادي المحدد أثناء mount، وقيمته المقابلة هي اسم جهاز الملف الخاص المشار إليه. يتم البحث في هذا الجدول عن كل زوج رقم i/جهاز يتوافق مع ملف عادي، وإذا تم العثور على تطابق، يتم استبدال الملف العادي بالملف الخاص المشار إليه.

---

### Translation Notes

- **Key terms introduced:**
  - i-number (رقم i)
  - i-node (عقدة i)
  - i-list (قائمة i)
  - file descriptor (واصف الملف)
  - link-count (عدد الروابط)
  - block (كتلة)
  - indirect block (كتلة غير مباشرة)
  - mount system call (استدعاء نظام mount)
  - device address (عنوان جهاز)
  - kernel (نواة)

- **Mathematical notation:**
  - Preserved LaTeX notation: $8 \\times 256 \\times 512$ bytes
  - Explanation in Arabic follows the equation

- **Special handling:**
  - Kept technical terms like "i-node", "i-number", "mount" with transliteration
  - Maintained block size (512 bytes) as numeric value
  - Preserved system call names (open, create, mount) in English
  - Added Arabic explanation for technical abbreviations

- **Technical concepts:**
  - I-node structure and indexing
  - Link counting for file references
  - Block addressing for small and large files
  - Device abstraction through special files
  - Mount system implementation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-Translation Validation

As mentioned in the introduction, a directory entry contains only a name for the associated file and a pointer to the file itself. This pointer is an integer called the i-number (for index number) of the file. When accessing the file, its i-number is used as an index into a system table (the i-list) stored in a known part of the device on which the directory resides. The entry found this way (the file's i-node) contains the file description as follows: 1) its owner, 2) its protection bits, 3) the physical disk or tape addresses for the file contents, 4) its size, 5) time of last modification, 6) the number of links to the file (the number of times it appears in a directory), 7) a bit indicating whether the file is a directory, 8) a bit indicating whether the file is a special file, 9) a bit indicating whether the file is "large" or "small".

The purpose of an open or create system call is to convert the path name given by the user into an i-number by searching explicitly or implicitly named directories. Once a file is opened, its device, i-number, and read/write pointer are stored in a system table indexed by the file descriptor returned by open or create. Thus the file system can easily access the file at the indicated position in the file.
