# Section 2: The File System
## القسم 2: نظام الملفات

**Section:** file-system
**Translation Quality:** 0.88
**Glossary Terms Used:** file system, hierarchical, directory, device, I/O, special file, mount, path

---

### English Version

The most important job of UNIX is to provide a file system. From the user's point of view, there are three kinds of files: ordinary disk files, directories, and special files.

**Ordinary Files**

A file contains whatever information the user places on it, for example, symbolic or binary (object) programs. No particular structuring is expected by the system. Files of text consist simply of a string of characters, with lines demarcated by the new-line character. Binary programs are sequences of words as they will appear in core memory when the program starts executing. A few user programs manipulate files with more structure: the assembler generates, and the loader expects, an object file in a particular format. However, the structure of files is controlled by the programs which use them, not by the system.

**Directories**

Directories provide the mapping between the names of files and the files themselves, and thus induce a structure on the file system as a whole. Each user has a directory of his own files; he may also create subdirectories to contain groups of files conveniently grouped together. A directory behaves exactly like an ordinary file except that it cannot be written on by unprivileged programs, so that the system controls the contents of directories.

However, anyone with appropriate permission may read a directory just like any other file. The system maintains several directories for its own use. One of these is the root directory. All files in the system can be found by tracing a path through a chain of directories until the desired file is reached. The starting point for such a path is often the root.

Another system directory contains all the programs provided for general use; that is, all the commands. As will be seen, however, it is by no means necessary that a program reside in this directory for it to be executed.

Files are named by sequences of 14 or fewer characters. When the name of a file is specified to the system, it may be in the form of a path name, which is a sequence of directory names separated by slashes "/" and ending in a file name. If the sequence begins with a slash, the search begins in the root directory. The name /alpha/beta/gamma causes the system to search the root for directory alpha, then to search alpha for beta, and finally to search beta for gamma. If the first component is not preceded by a slash, the search begins in the user's current directory.

The length of a path name is variable; components of a path (such as alpha) have 14 characters or less. The total length is limited by the speed of searching.

**Special Files**

Special files constitute the most unusual feature of the UNIX file system. Each I/O device supported by UNIX is associated with at least one such file. Special files are read and written just like ordinary disk files, but requests to read or write result in activation of the associated device. An entry for each special file resides in directory /dev, although a link may be made to one of these files just as it may to an ordinary file. Thus, for example, to punch paper tape, one may write on the file /dev/ppt. Special files exist for each communication line, each disk, each tape drive, and for physical core memory. Of course, the active disks and the core special file are protected from indiscriminate access.

There is a threefold advantage in treating I/O devices this way: file and device I/O are as similar as possible; file and device names have the same syntax and meaning, so that a program expecting a file name as a parameter can be passed a device name; and finally, special files are subject to the same protection mechanism as regular files.

---

### النسخة العربية

إن أهم وظيفة ليونكس هي توفير نظام ملفات. من وجهة نظر المستخدم، هناك ثلاثة أنواع من الملفات: ملفات القرص العادية، والأدلة (الدلائل)، والملفات الخاصة.

**الملفات العادية**

يحتوي الملف على أي معلومات يضعها المستخدم فيه، على سبيل المثال، البرامج الرمزية أو الثنائية (الكائنية). لا يتوقع النظام أي هيكلة معينة. تتكون ملفات النص ببساطة من سلسلة من الأحرف، مع تحديد الأسطر بواسطة حرف السطر الجديد. البرامج الثنائية هي تسلسلات من الكلمات كما ستظهر في ذاكرة النواة عندما يبدأ البرنامج في التنفيذ. تتعامل بعض برامج المستخدم مع ملفات ذات هيكل أكثر: يولد المجمّع (assembler)، ويتوقع المحمّل (loader)، ملف كائن بتنسيق معين. ومع ذلك، يتم التحكم في هيكل الملفات بواسطة البرامج التي تستخدمها، وليس بواسطة النظام.

**الأدلة**

توفر الأدلة (الدلائل) التعيين بين أسماء الملفات والملفات نفسها، وبالتالي تفرض هيكلاً على نظام الملفات ككل. لكل مستخدم دليل خاص بملفاته؛ يمكنه أيضاً إنشاء أدلة فرعية لاحتواء مجموعات من الملفات المجمعة معاً بشكل ملائم. يتصرف الدليل تماماً مثل ملف عادي باستثناء أنه لا يمكن الكتابة عليه بواسطة برامج غير مصرح لها، بحيث يتحكم النظام في محتويات الأدلة.

ومع ذلك، يمكن لأي شخص لديه الإذن المناسب قراءة دليل تماماً مثل أي ملف آخر. يحتفظ النظام بعدة أدلة لاستخدامه الخاص. أحد هذه الأدلة هو الدليل الجذر (root directory). يمكن العثور على جميع الملفات في النظام عن طريق تتبع مسار عبر سلسلة من الأدلة حتى الوصول إلى الملف المطلوب. نقطة البداية لمثل هذا المسار غالباً ما تكون الجذر.

يحتوي دليل نظام آخر على جميع البرامج المقدمة للاستخدام العام؛ أي جميع الأوامر. كما سيتضح، ومع ذلك، ليس من الضروري على الإطلاق أن يكون البرنامج موجوداً في هذا الدليل لكي يتم تنفيذه.

تتم تسمية الملفات بتسلسلات من 14 حرفاً أو أقل. عندما يتم تحديد اسم ملف للنظام، قد يكون في شكل اسم مسار (path name)، وهو تسلسل من أسماء الأدلة مفصولة بشرطات مائلة "/" وينتهي باسم ملف. إذا بدأ التسلسل بشرطة مائلة، يبدأ البحث في الدليل الجذر. الاسم /alpha/beta/gamma يسبب للنظام البحث في الجذر عن الدليل alpha، ثم البحث في alpha عن beta، وأخيراً البحث في beta عن gamma. إذا لم يسبق المكون الأول بشرطة مائلة، يبدأ البحث في الدليل الحالي للمستخدم.

طول اسم المسار متغير؛ مكونات المسار (مثل alpha) تحتوي على 14 حرفاً أو أقل. يقتصر الطول الإجمالي بسرعة البحث.

**الملفات الخاصة**

تشكل الملفات الخاصة الميزة الأكثر غرابة في نظام ملفات يونكس. كل جهاز إدخال/إخراج (I/O) يدعمه يونكس مرتبط بملف واحد على الأقل من هذا القبيل. تتم قراءة الملفات الخاصة والكتابة عليها تماماً مثل ملفات القرص العادية، لكن طلبات القراءة أو الكتابة تؤدي إلى تنشيط الجهاز المرتبط. يوجد إدخال لكل ملف خاص في الدليل /dev، على الرغم من أنه يمكن إنشاء رابط (link) لأحد هذه الملفات تماماً كما يمكن لملف عادي. وبالتالي، على سبيل المثال، لثقب شريط ورقي، يمكن للمرء الكتابة على الملف /dev/ppt. توجد ملفات خاصة لكل خط اتصال، وكل قرص، وكل محرك شريط، ولذاكرة النواة الفيزيائية. بالطبع، الأقراص النشطة وملف النواة الخاص محميان من الوصول العشوائي.

هناك ميزة ثلاثية في معاملة أجهزة الإدخال/الإخراج بهذه الطريقة: إدخال/إخراج الملفات والأجهزة متشابهان قدر الإمكان؛ أسماء الملفات والأجهزة لها نفس البناء والمعنى، بحيث يمكن تمرير اسم جهاز إلى برنامج يتوقع اسم ملف كمعامل؛ وأخيراً، تخضع الملفات الخاصة لنفس آلية الحماية مثل الملفات العادية.

---

### Translation Notes

- **Key terms introduced:**
  - ordinary files (ملفات عادية)
  - directories (أدلة / دلائل)
  - special files (ملفات خاصة)
  - root directory (دليل جذر)
  - path name (اسم مسار)
  - I/O device (جهاز إدخال/إخراج)
  - core memory (ذاكرة النواة)
  - assembler (مجمّع)
  - loader (محمّل)

- **Special handling:**
  - Preserved UNIX command syntax ("/", "/dev/ppt", path structure) in English
  - Maintained file naming conventions (14 characters) as specified
  - Kept technical abbreviations (I/O) with Arabic explanation
  - Preserved directory structure examples (alpha/beta/gamma)

- **Technical concepts:**
  - The "everything is a file" philosophy - treating devices as files
  - Hierarchical file system structure
  - Path navigation from root
  - Unified I/O model

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Validation

The most important function of UNIX is to provide a file system. From the user's perspective, there are three types of files: ordinary disk files, directories, and special files.

**Ordinary Files**: A file contains any information the user places in it, for example, symbolic or binary (object) programs. The system does not expect any particular structure. Text files simply consist of a string of characters, with lines delimited by the new-line character. Binary programs are sequences of words as they will appear in core memory when the program begins execution. Some user programs deal with files with more structure: the assembler generates, and the loader expects, an object file in a specific format. However, file structure is controlled by the programs that use them, not by the system.

**Directories**: Directories provide the mapping between file names and the files themselves, and thus impose a structure on the file system as a whole. Each user has a directory for their files; they can also create subdirectories to contain groups of files conveniently grouped together. A directory behaves exactly like an ordinary file except that it cannot be written to by unauthorized programs, so the system controls the contents of directories. However, anyone with appropriate permission can read a directory just like any other file. The system maintains several directories for its own use. One of these is the root directory. All files in the system can be found by tracing a path through a chain of directories until the desired file is reached. The starting point for such a path is often the root.

**Special Files**: Special files constitute the most unusual feature of the UNIX file system. Each I/O device supported by UNIX is associated with at least one such file. Special files are read and written just like ordinary disk files, but read or write requests result in activation of the associated device.
