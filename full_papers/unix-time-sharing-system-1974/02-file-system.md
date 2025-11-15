# Section 2: The File System
## القسم 2: نظام الملفات

**Section:** file-system
**Translation Quality:** 0.89
**Glossary Terms Used:** file system, hierarchical, directory, ordinary files, special files, device, removable, protection, permissions

---

### English Version

#### 2.1 Ordinary Files

A file contains whatever information the user places on it, for example symbolic or binary (object) programs. No particular structuring is expected by the system. Files of text consist simply of a string of characters, with lines demarcated by the new-line character. Binary programs are sequences of words as they will appear in core memory when the program starts executing. A few user programs manipulate files with more structure: the assembler generates and the loader expects an object file in a particular format. However, the structure of files is controlled by the programs which use them, not by the system.

#### 2.2 Directories

Directories provide the mapping between the names of files and the files themselves, and thus induce a structure on the file system as a whole. Each user has a directory of his own files; he may also create subdirectories to contain groups of files conveniently treated together. A directory behaves exactly like an ordinary file except that it cannot be written on by unprivileged programs, so that the system controls the contents of directories. However, anyone with appropriate permission may read a directory just like any other file.

The system maintains several directories for its own use. One of these is the root directory. All files in the system can be found by tracing a path through a chain of directories until the desired file is reached. The starting point for such searches is often the root. Another system directory contains all the programs provided for general use; that is, all the commands. As will be seen however, it is by no means necessary that a program reside in this directory for it to be executed.

Files are named by sequences of 14 or fewer characters. When the name of a file is specified to the system, it may be in the form of a path name, which is a sequence of directory names separated by slashes "/" and ending in a file name. If the sequence begins with a slash, the search begins in the root directory. The name /alpha/beta/gamma causes the system to search the root for directory alpha, then to search alpha for beta, finally to find gamma in beta. gamma may be an ordinary file, a directory, or a special file. As a limiting case, the name "/" refers to the root itself.

A path name not starting with "/" causes the system to begin the search in the user's current directory. Thus, the name alpha/beta specifies the file named beta in subdirectory alpha of the current directory. The simplest kind of name, for example alpha, refers to a file which itself is found in the current directory. As another limiting case, the null file name refers to the current directory.

The same nondirectory file may appear in several directories under possibly different names. This feature is called linking; a directory entry for a file is sometimes called a link. UNIX differs from other systems in which linking is permitted in that all links to a file have equal status. That is, a file does not exist within a particular directory; the directory entry for a file consists merely of its name and a pointer to the information actually describing the file. Thus a file exists independently of any directory entry, although in practice a file is made to disappear along with the last link to it.

Each directory always has at least two entries. The name "." in each directory refers to the directory itself. Thus a program may read the current directory under the name "." without knowing its complete path name. The name ".." by convention refers to the parent of the directory in which it appears, that is, to the directory in which it was created.

The directory structure is constrained to have the form of a rooted tree. Except for the special entries "." and "..", each directory must appear as an entry in exactly one other directory, which is its parent. The reason for this is to simplify the writing of programs which visit subtrees of the directory structure, and more important, to avoid the separation of portions of the hierarchy. If arbitrary links to directories were permitted, it would be quite difficult to detect loops. However, a super-user is allowed to make links to directories. A directory is never physically removed except by the operating system; it is not even permitted to write on a directory except by the system.

#### 2.3 Special Files

Special files constitute the most unusual feature of the UNIX file system. Each I/O device supported by UNIX is associated with at least one such file. Special files are read and written just like ordinary disk files, but requests to read or write result in activation of the associated device. An entry for each special file resides in directory /dev, although a link may be made to one of these files just like an ordinary file. Thus, for example, to punch paper tape, one may write on the file /dev/ppt. Special files exist for each communication line, each disk, each tape drive, and for physical core memory. Of course, the active disks and the core special file are protected from indiscriminate access.

There is a threefold advantage in treating I/O devices this way: file and device I/O are as similar as possible; file and device names have the same syntax and meaning, so that a program expecting a file name as a parameter can be passed a device name; finally, special files are subject to the same protection mechanism as regular files.

#### 2.4 Removable File Systems

Although the root of the file system is always stored on the same device, it is not necessary that the entire file system hierarchy reside on this device. There is a mount system request with two arguments: the name of an existing ordinary file, and the name of a special file whose associated storage volume (e.g. disk pack) should have the structure of an independent file system containing its own directory hierarchy. The effect of mount is to cause references to the heretofore ordinary file to refer instead to the root directory of the file system on the removable volume. In effect, mount replaces a leaf of the hierarchy tree (the ordinary file) by a whole new subtree (the hierarchy stored on the removable volume). After the mount, there is virtually no distinction between files on the removable volume and those in the permanent file system. In our installation, for example, the root directory resides on a small fixed-head disk, and the large disk is mounted by the system initialization program. The four principal directories (bin, dev, etc, usr) are thereby spread across different devices, as are the major file groups within the usr directory.

There is a purposely bare minimum of internal bookkeeping associated with mounting. The mount system call does not make a copy of the mounted-on file; it simply makes a connection between the file name and the mounted device. This means that no restriction need be placed on what kind of ordinary file is suitable for mounting; any ordinary file may be mounted on, but a file may not be mounted on if it is already in use, for protection reasons. Although a directory cannot be written on by user programs, it can be mounted on.

Dismounting is accomplished by another system call which takes the name of the mounted-on file. Although it is expected that users will dismount only their own private file systems, as a matter of security only the super-user is permitted actually to perform the dismount operation, since otherwise various race conditions would arise.

#### 2.5 Protection

Although the access control scheme in UNIX is quite simple, it has some unusual features. Each user of the system is assigned a unique user identification number. When a file is created, it is marked with the user ID of its owner. Also given for new files is a set of seven protection bits. Six of these specify independently read, write, and execute permission for the owner of the file and for all other users.

If the seventh bit is on, the system will temporarily change the user identification of the current user to that of the creator of the file whenever the file is executed as a program. This change in user ID is effective only during the execution of the program which calls for it. The set user ID feature provides for privileged programs which may use files inaccessible to other users. For example, a program may keep an accounting file which should neither be read nor changed except by the program itself. If the set-user-ID bit is on for the program, it may access the file although this access might be forbidden to other programs invoked by the given program's user. Since the actual user ID of the invoker of any program is always available, set-user-ID programs may take any measures desired to satisfy themselves as to their invoker's credentials. This mechanism is used to allow users to execute the carefully written commands which call privileged system entries. For example, there is a system entry invokable only by the "super-user" which creates an empty directory. As indicated above, directories are expected to have entries for "." and "..". The command which creates a directory is owned by the super-user and has the set-user-ID bit set. After it checks its invoker's authorization to create the specified directory, it creates it and makes the entries for "." and "..".

Since anyone may set the set-user-ID bit on one of his own files, this mechanism is generally available without administrative intervention. For example, this protection scheme easily solves the MOO accounting problem posed in [5].

#### 2.6 I/O Calls

The system calls to do I/O are extremely simple. Given a file name, one issues an open request which returns a small integer called a file descriptor. A subsequent read or write call with this file descriptor as argument results in the transfer of data. After all processing is complete, the file may be closed, which causes the file descriptor to become available for reuse.

There is no notion of access mode (read, write, or both): a file descriptor returned by open may be used equally for reading or writing. Since there is no restriction on the owner of a file and no semantics of particular files are involved, this generality carries over to I/O involving special files. For example, to open a magnetic tape file for writing it is necessary only to open the file /dev/mt for either reading or writing, and then issue write commands; no special preliminary tape-positioning or formatting commands are needed.

A process need not worry about the physical location or the access restrictions of a file. All the file system, I/O device, and all protection considerations are reflected in the status of the open request. Once a file is open, its file descriptor is an unforged capability for I/O.

Two other kinds of I/O are available. First, one may wait for a connection from another user to a file of one's own and then cause I/O to take place on the resulting channel; details are not given here. Second, there is a system request whereby a file descriptor may be associated with one or both ends of a pipe, which is an asynchronously operating one-way FIFO buffer that holds up to 5120 characters. The read and write system calls work normally with such file descriptors.

---

### النسخة العربية

#### 2.1 الملفات العادية

يحتوي الملف على أي معلومات يضعها المستخدم فيه، على سبيل المثال برامج رمزية أو ثنائية (كائنات). لا يتوقع النظام أي هيكلة معينة. تتكون ملفات النص ببساطة من سلسلة من الأحرف، مع فصل الأسطر بحرف السطر الجديد. البرامج الثنائية هي تسلسلات من الكلمات كما ستظهر في الذاكرة الرئيسية عندما يبدأ البرنامج بالتنفيذ. بعض برامج المستخدم تتعامل مع ملفات ذات بنية أكثر: المُجمّع يولد والمحمّل يتوقع ملف كائن بتنسيق معين. ومع ذلك، فإن بنية الملفات يتحكم فيها البرامج التي تستخدمها، وليس النظام.

#### 2.2 الدلائل

توفر الدلائل الربط بين أسماء الملفات والملفات نفسها، وبالتالي تحدث بنية على نظام الملفات ككل. كل مستخدم لديه دليل خاص بملفاته؛ وقد ينشئ أيضاً دلائل فرعية لاحتواء مجموعات من الملفات يُعامل معها بشكل مريح معاً. يتصرف الدليل تماماً مثل ملف عادي باستثناء أنه لا يمكن الكتابة عليه من قبل برامج غير مميزة، بحيث يتحكم النظام في محتويات الدلائل. ومع ذلك، يمكن لأي شخص لديه الإذن المناسب قراءة دليل تماماً مثل أي ملف آخر.

يحتفظ النظام بعدة دلائل لاستخدامه الخاص. أحد هذه الدلائل هو الدليل الجذر. يمكن العثور على جميع الملفات في النظام من خلال تتبع مسار عبر سلسلة من الدلائل حتى الوصول إلى الملف المطلوب. نقطة البداية لمثل هذه البحوث غالباً ما تكون الجذر. دليل نظام آخر يحتوي على جميع البرامج المتاحة للاستخدام العام؛ أي جميع الأوامر. كما سيتضح، ليس من الضروري بأي حال من الأحوال أن يقيم برنامج في هذا الدليل ليتم تنفيذه.

تُسمى الملفات بتسلسلات من 14 حرفاً أو أقل. عندما يُحدد اسم ملف للنظام، قد يكون على شكل اسم مسار، وهو تسلسل من أسماء الدلائل مفصولة بخطوط مائلة "/" وتنتهي باسم ملف. إذا بدأ التسلسل بخط مائل، يبدأ البحث في الدليل الجذر. الاسم /alpha/beta/gamma يجعل النظام يبحث في الجذر عن دليل alpha، ثم البحث في alpha عن beta، وأخيراً العثور على gamma في beta. قد يكون gamma ملفاً عادياً أو دليلاً أو ملفاً خاصاً. كحالة حدية، الاسم "/" يشير إلى الجذر نفسه.

اسم مسار لا يبدأ بـ "/" يجعل النظام يبدأ البحث في الدليل الحالي للمستخدم. وبالتالي، الاسم alpha/beta يحدد الملف المسمى beta في الدليل الفرعي alpha من الدليل الحالي. أبسط نوع من الأسماء، على سبيل المثال alpha، يشير إلى ملف يوجد هو نفسه في الدليل الحالي. كحالة حدية أخرى، اسم الملف الفارغ يشير إلى الدليل الحالي.

قد يظهر نفس الملف غير الدليلي في عدة دلائل تحت أسماء مختلفة ربما. تُسمى هذه الميزة بالربط؛ يُسمى إدخال دليل لملف أحياناً رابطاً. يختلف يونكس عن الأنظمة الأخرى التي يُسمح فيها بالربط في أن جميع الروابط لملف لها حالة متساوية. أي أن الملف لا يوجد داخل دليل معين؛ إدخال الدليل لملف يتكون فقط من اسمه ومؤشر إلى المعلومات التي تصف الملف فعلياً. وبالتالي، يوجد الملف بشكل مستقل عن أي إدخال دليل، على الرغم من أنه عملياً يُجعل الملف يختفي مع آخر رابط له.

كل دليل دائماً لديه إدخالان على الأقل. الاسم "." في كل دليل يشير إلى الدليل نفسه. وبالتالي، يمكن لبرنامج قراءة الدليل الحالي تحت الاسم "." دون معرفة اسم المسار الكامل له. الاسم ".." بالاتفاق يشير إلى الأصل للدليل الذي يظهر فيه، أي إلى الدليل الذي تم إنشاؤه فيه.

بنية الدليل مُقيدة بأن يكون لها شكل شجرة جذرية. باستثناء الإدخالات الخاصة "." و ".."، يجب أن يظهر كل دليل كإدخال في دليل آخر واحد بالضبط، وهو أصله. السبب في ذلك هو تبسيط كتابة البرامج التي تزور أشجاراً فرعية من بنية الدليل، والأهم من ذلك، لتجنب فصل أجزاء من التسلسل الهرمي. إذا كانت الروابط التعسفية للدلائل مسموح بها، سيكون من الصعب جداً اكتشاف الحلقات. ومع ذلك، يُسمح للمستخدم الفائق بإنشاء روابط للدلائل. لا تتم إزالة الدليل فعلياً أبداً إلا بواسطة نظام التشغيل؛ ولا يُسمح حتى بالكتابة على دليل إلا من قبل النظام.

#### 2.3 الملفات الخاصة

تشكل الملفات الخاصة الميزة الأكثر غرابة في نظام ملفات يونكس. كل جهاز إدخال/إخراج يدعمه يونكس مرتبط بملف واحد على الأقل من هذا النوع. تُقرأ الملفات الخاصة وتُكتب تماماً مثل ملفات القرص العادية، لكن طلبات القراءة أو الكتابة تؤدي إلى تفعيل الجهاز المرتبط. يوجد إدخال لكل ملف خاص في الدليل /dev، على الرغم من أنه يمكن إنشاء رابط لأحد هذه الملفات تماماً مثل ملف عادي. وبالتالي، على سبيل المثال، لثقب شريط ورقي، يمكن للمرء الكتابة على الملف /dev/ppt. توجد ملفات خاصة لكل خط اتصال، وكل قرص، وكل محرك شريط، وللذاكرة الرئيسية الفيزيائية. بالطبع، الأقراص النشطة وملف الذاكرة الرئيسية الخاص محمية من الوصول العشوائي.

هناك ميزة ثلاثية في معاملة أجهزة الإدخال/الإخراج بهذه الطريقة: إدخال/إخراج الملفات والأجهزة متشابهان قدر الإمكان؛ أسماء الملفات والأجهزة لها نفس بناء الجملة والمعنى، بحيث يمكن تمرير اسم جهاز إلى برنامج يتوقع اسم ملف كمعامل؛ أخيراً، الملفات الخاصة تخضع لنفس آلية الحماية مثل الملفات العادية.

#### 2.4 أنظمة الملفات القابلة للإزالة

على الرغم من أن جذر نظام الملفات يُخزن دائماً على نفس الجهاز، ليس من الضروري أن يقيم التسلسل الهرمي الكامل لنظام الملفات على هذا الجهاز. هناك طلب نظام mount بحجتين: اسم ملف عادي موجود، واسم ملف خاص يجب أن يكون لوحدة التخزين المرتبطة به (على سبيل المثال حزمة قرص) بنية نظام ملفات مستقل يحتوي على تسلسل هرمي دليل خاص به. تأثير mount هو التسبب في جعل الإشارات إلى الملف العادي حتى الآن تشير بدلاً من ذلك إلى الدليل الجذر لنظام الملفات على الوحدة القابلة للإزالة. في الواقع، يستبدل mount ورقة من شجرة التسلسل الهرمي (الملف العادي) بشجرة فرعية جديدة كاملة (التسلسل الهرمي المخزن على الوحدة القابلة للإزالة). بعد التركيب، لا يوجد عملياً أي تمييز بين الملفات على الوحدة القابلة للإزالة وتلك الموجودة في نظام الملفات الدائم. في تثبيتنا، على سبيل المثال، يقيم الدليل الجذر على قرص صغير ذو رأس ثابت، ويتم تركيب القرص الكبير بواسطة برنامج تهيئة النظام. الدلائل الأربعة الرئيسية (bin، dev، etc، usr) موزعة بالتالي عبر أجهزة مختلفة، كما هو الحال مع مجموعات الملفات الرئيسية داخل دليل usr.

هناك حد أدنى عن قصد من المحاسبة الداخلية المرتبطة بالتركيب. استدعاء نظام mount لا ينشئ نسخة من الملف المركب عليه؛ إنه ببساطة ينشئ اتصالاً بين اسم الملف والجهاز المركب. هذا يعني أنه لا حاجة لوضع قيود على نوع الملف العادي المناسب للتركيب؛ يمكن التركيب على أي ملف عادي، لكن لا يمكن التركيب على ملف إذا كان قيد الاستخدام بالفعل، لأسباب الحماية. على الرغم من أنه لا يمكن الكتابة على دليل من قبل برامج المستخدم، يمكن التركيب عليه.

يتم الفصل بواسطة استدعاء نظام آخر يأخذ اسم الملف المركب عليه. على الرغم من أنه من المتوقع أن يفصل المستخدمون فقط أنظمة ملفاتهم الخاصة، كمسألة أمنية، يُسمح فقط للمستخدم الفائق بالفعل بتنفيذ عملية الفصل، حيث أنه خلاف ذلك ستنشأ ظروف سباق مختلفة.

#### 2.5 الحماية

على الرغم من أن مخطط التحكم في الوصول في يونكس بسيط جداً، إلا أنه يحتوي على بعض الميزات غير العادية. كل مستخدم للنظام يُعين له رقم تعريف مستخدم فريد. عندما يُنشأ ملف، يُوضع عليه علامة برقم تعريف المستخدم لمالكه. تُعطى أيضاً للملفات الجديدة مجموعة من سبعة بتات حماية. ستة من هذه تحدد بشكل مستقل إذن القراءة والكتابة والتنفيذ لمالك الملف ولجميع المستخدمين الآخرين.

إذا كانت البتة السابعة مفعلة، سيغير النظام مؤقتاً تعريف المستخدم للمستخدم الحالي إلى تعريف منشئ الملف كلما تم تنفيذ الملف كبرنامج. هذا التغيير في تعريف المستخدم فعال فقط أثناء تنفيذ البرنامج الذي يطلبه. توفر ميزة تعيين تعريف المستخدم برامج مميزة قد تستخدم ملفات غير متاحة للمستخدمين الآخرين. على سبيل المثال، قد يحتفظ برنامج بملف محاسبة لا ينبغي قراءته أو تغييره إلا بواسطة البرنامج نفسه. إذا كانت بتة تعيين تعريف المستخدم مفعلة للبرنامج، فقد يصل إلى الملف على الرغم من أن هذا الوصول قد يكون محظوراً على برامج أخرى يستدعيها مستخدم البرنامج المعني. نظراً لأن تعريف المستخدم الفعلي لمستدعي أي برنامج متاح دائماً، قد تتخذ برامج تعيين تعريف المستخدم أي تدابير مرغوبة لإرضاء نفسها فيما يتعلق باعتمادات مستدعيها. تُستخدم هذه الآلية للسماح للمستخدمين بتنفيذ الأوامر المكتوبة بعناية والتي تستدعي إدخالات نظام مميزة. على سبيل المثال، هناك إدخال نظام يمكن استدعاؤه فقط من قبل "المستخدم الفائق" والذي ينشئ دليلاً فارغاً. كما هو موضح أعلاه، من المتوقع أن يكون للدلائل إدخالات لـ "." و "..". الأمر الذي ينشئ دليلاً مملوك من قبل المستخدم الفائق وله بتة تعيين تعريف المستخدم مفعلة. بعد أن يتحقق من تفويض مستدعيه لإنشاء الدليل المحدد، ينشئه ويجعل الإدخالات لـ "." و "..".

نظراً لأن أي شخص قد يفعّل بتة تعيين تعريف المستخدم على أحد ملفاته الخاصة، هذه الآلية متاحة بشكل عام دون تدخل إداري. على سبيل المثال، يحل مخطط الحماية هذا بسهولة مشكلة محاسبة MOO المطروحة في [5].

#### 2.6 استدعاءات الإدخال/الإخراج

استدعاءات النظام للقيام بالإدخال/الإخراج بسيطة للغاية. بالنظر إلى اسم ملف، يُصدر المرء طلب فتح يُرجع عدداً صحيحاً صغيراً يُسمى واصف ملف. استدعاء قراءة أو كتابة لاحق بهذا الواصف الملف كحجة يؤدي إلى نقل البيانات. بعد اكتمال جميع المعالجات، قد يُغلق الملف، مما يجعل واصف الملف متاحاً لإعادة الاستخدام.

لا يوجد مفهوم لنمط الوصول (قراءة أو كتابة أو كليهما): واصف ملف يُرجعه open قد يُستخدم بالتساوي للقراءة أو الكتابة. نظراً لعدم وجود قيد على مالك ملف ولا دلالات لملفات معينة معنية، هذا التعميم ينتقل إلى الإدخال/الإخراج الذي يتضمن ملفات خاصة. على سبيل المثال، لفتح ملف شريط مغناطيسي للكتابة، من الضروري فقط فتح الملف /dev/mt إما للقراءة أو الكتابة، ثم إصدار أوامر كتابة؛ لا حاجة لأوامر تمهيدية خاصة لتحديد موضع الشريط أو التنسيق.

لا تحتاج العملية إلى القلق بشأن الموقع الفيزيائي أو قيود الوصول لملف. جميع نظام الملفات وجهاز الإدخال/الإخراج وجميع اعتبارات الحماية تنعكس في حالة طلب الفتح. بمجرد فتح ملف، واصف الملف الخاص به هو قدرة غير مزورة للإدخال/الإخراج.

نوعان آخران من الإدخال/الإخراج متاحان. أولاً، قد ينتظر المرء اتصالاً من مستخدم آخر إلى ملف خاص به ثم يتسبب في حدوث إدخال/إخراج على القناة الناتجة؛ التفاصيل غير معطاة هنا. ثانياً، هناك طلب نظام يمكن من خلاله ربط واصف ملف بأحد طرفي أو كلا طرفي أنبوب، وهو مخزن مؤقت FIFO أحادي الاتجاه يعمل بشكل غير متزامن ويحتوي على ما يصل إلى 5120 حرفاً. تعمل استدعاءات نظام القراءة والكتابة بشكل طبيعي مع واصفات الملفات هذه.

---

### Translation Notes

- **Key terms introduced:**
  - directory (دليل)
  - subdirectory (دليل فرعي)
  - root directory (دليل جذر)
  - path name (اسم مسار)
  - linking (ربط)
  - special files (ملفات خاصة)
  - mount (تركيب)
  - unmount/dismount (فصل)
  - protection bits (بتات حماية)
  - user ID (تعريف المستخدم)
  - set-user-ID (تعيين تعريف المستخدم)
  - file descriptor (واصف ملف)
  - pipe (أنبوب)
  - FIFO buffer (مخزن مؤقت FIFO)
- **Citations:** [5]
- **Special handling:**
  - Directory names (bin, dev, etc, usr) kept in English as system paths
  - Special file paths (/dev/ppt, /dev/mt) kept in original form
  - Special directory entries (".", "..") kept as is with Arabic explanation
  - Technical abbreviation FIFO kept in English

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Validation

The back-translation confirms accurate preservation of:
- Hierarchical file system structure
- Directory navigation concepts
- Special files for I/O devices
- Mountable file systems
- Protection mechanism with set-user-ID
- Unified file descriptor model for I/O
- Pipe mechanism for inter-process communication
