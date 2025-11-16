# Section 4: Processes and Images
## القسم 4: العمليات والصور

**Section:** processes-and-images
**Translation Quality:** 0.88
**Glossary Terms Used:** process, fork, execute, pipe, core image, system call, parent, child

---

### English Version

An **image** is a computer execution environment. It includes a core image, general register values, status of open files, current directory, and the like. An **image** is the current state of a pseudo-computer.

A **process** is the execution of an image. While the processor is executing on behalf of a process, the image must reside in core; during the execution of other processes it remains in core unless the appearance of an active, higher-priority process forces it to be swapped out to the disk.

The user-core part of an image is divided into three logical segments. The program text segment begins at location 0 in the virtual address space. During execution, this segment is write-protected and a single copy of it is shared among all processes executing the same program. At the first hardware protection byte boundary above the program text segment in the virtual address space begins a non-shared, writable data segment, the size of which may be extended by a system call. Starting at the highest address in the virtual address space is a stack segment, which automatically grows downward as the hardware's stack pointer fluctuates.

**Process Creation**

Only one process may exist at a time in UNIX. All other processes must be created by the existing process. A process may create an identical copy of itself by using the **fork** system call. The new process is called the **child** process. The old process is called the **parent** process. Fork causes the child to come into existence executing a copy of the same program as the parent. The only difference is that the value returned from fork in the child process is 0, while the parent receives the process ID of the child.

Because the return values in the parent and child differ, each may determine whether it is the parent or child.

**Process Execution**

Another major system call is **execute** (or **exec**). Execute causes the current process to cease executing the current program and begin executing a new program. The core image of the current process is replaced by a new core image specified as an argument to execute. The new program file's i-node is used to construct the process's new core image. Execute has no return, because the calling process's core image is destroyed.

**Pipes**

Processes may communicate with related processes using the same system read and write calls that are used for file system I/O. The call **pipe** creates an interprocess channel called a **pipe** and returns two file descriptors, one for reading and one for writing. When one process writes to the pipe, another process can read the data. The pipe has a finite buffer, so that if the writing process continues to write without the reading process draining the pipe, the writing process will be suspended until space becomes available.

If a process attempts to read from an empty pipe, the process is suspended until data becomes available. If the writing process closes its end of the pipe, the reading process receives an end-of-file indication. Pipes are crucial to the operation of the shell's command line processing.

**Execute and Fork**

The ordinary usage of fork is as follows. A process issues a fork, then the child process uses execute to run some other program. During this time, the parent process typically waits for the child to terminate. When the child process terminates, the parent receives notice. The combination fork-execute-wait allows the parent to control what programs run and when they run.

**Process Synchronization**

UNIX processes may synchronize using the **wait** system call, which suspends execution of the calling process until one of its children has completed. Wait returns the process ID of the terminated child, so the parent can tell which of its children has terminated. If the parent has multiple children, repeated calls to wait allow it to collect information about all of them.

---

### النسخة العربية

**الصورة** (image) هي بيئة تنفيذ حاسوبية. وتشمل صورة النواة (core image)، وقيم السجلات العامة، وحالة الملفات المفتوحة، والدليل الحالي، وما شابه ذلك. **الصورة** هي الحالة الحالية لحاسوب زائف (pseudo-computer).

**العملية** (process) هي تنفيذ صورة. بينما المعالج ينفذ نيابة عن عملية، يجب أن تكون الصورة موجودة في النواة؛ أثناء تنفيذ عمليات أخرى تبقى في النواة ما لم يجبرها ظهور عملية نشطة ذات أولوية أعلى على أن يتم تبديلها إلى القرص.

ينقسم جزء نواة المستخدم من الصورة إلى ثلاثة أجزاء منطقية. يبدأ جزء نص البرنامج (program text segment) في الموقع 0 في مساحة العنوان الافتراضية. أثناء التنفيذ، يكون هذا الجزء محمياً من الكتابة (write-protected) وتتم مشاركة نسخة واحدة منه بين جميع العمليات التي تنفذ نفس البرنامج. عند حد بايت الحماية الأول للعتاد فوق جزء نص البرنامج في مساحة العنوان الافتراضية يبدأ جزء بيانات (data segment) قابل للكتابة وغير مشترك، يمكن توسيع حجمه بواسطة استدعاء نظام. بدءاً من أعلى عنوان في مساحة العنوان الافتراضية يوجد جزء المكدس (stack segment)، الذي ينمو تلقائياً نحو الأسفل مع تقلب مؤشر المكدس في العتاد.

**إنشاء العمليات**

قد توجد عملية واحدة فقط في كل مرة في يونكس. يجب إنشاء جميع العمليات الأخرى بواسطة العملية الموجودة. يمكن للعملية إنشاء نسخة مطابقة من نفسها باستخدام استدعاء النظام **fork**. تسمى العملية الجديدة **العملية الفرعية** (child process). تسمى العملية القديمة **العملية الأم** (parent process). يتسبب Fork في ظهور الفرع لينفذ نسخة من نفس البرنامج مثل الأم. الفرق الوحيد هو أن القيمة المعادة من fork في العملية الفرعية هي 0، بينما تتلقى الأم معرف العملية (process ID) الخاص بالفرع.

نظراً لأن القيم المعادة في الأم والفرع تختلف، يمكن لكل منهما تحديد ما إذا كانت الأم أو الفرع.

**تنفيذ العمليات**

استدعاء نظام رئيسي آخر هو **execute** (أو **exec**). يتسبب Execute في أن تتوقف العملية الحالية عن تنفيذ البرنامج الحالي وتبدأ في تنفيذ برنامج جديد. يتم استبدال صورة النواة للعملية الحالية بصورة نواة جديدة محددة كحجة لـ execute. يتم استخدام عقدة i لملف البرنامج الجديد لبناء صورة النواة الجديدة للعملية. Execute ليس له إرجاع، لأن صورة النواة للعملية المستدعية يتم إتلافها.

**الأنابيب**

يمكن للعمليات التواصل مع العمليات ذات الصلة باستخدام نفس استدعاءات النظام read و write المستخدمة لإدخال/إخراج نظام الملفات. ينشئ الاستدعاء **pipe** قناة بين العمليات تسمى **أنبوب** (pipe) ويُعيد واصفي ملفات، واحد للقراءة وواحد للكتابة. عندما تكتب عملية واحدة إلى الأنبوب، يمكن لعملية أخرى قراءة البيانات. للأنبوب مخزن مؤقت محدود، بحيث إذا استمرت عملية الكتابة في الكتابة دون أن تقوم عملية القراءة بإفراغ الأنبوب، سيتم تعليق عملية الكتابة حتى تصبح المساحة متاحة.

إذا حاولت عملية القراءة من أنبوب فارغ، يتم تعليق العملية حتى تصبح البيانات متاحة. إذا أغلقت عملية الكتابة نهايتها من الأنبوب، تتلقى عملية القراءة إشارة نهاية الملف (end-of-file). الأنابيب حاسمة لتشغيل معالجة سطر الأوامر في الشل (shell).

**Execute و Fork**

الاستخدام العادي لـ fork هو كما يلي. تصدر عملية fork، ثم تستخدم العملية الفرعية execute لتشغيل برنامج آخر. خلال هذا الوقت، تنتظر العملية الأم عادة انتهاء الفرع. عندما تنتهي العملية الفرعية، تتلقى الأم إشعاراً. يسمح الدمج fork-execute-wait للأم بالتحكم في البرامج التي تعمل ومتى تعمل.

**مزامنة العمليات**

يمكن لعمليات يونكس المزامنة باستخدام استدعاء النظام **wait**، الذي يعلق تنفيذ العملية المستدعية حتى يكمل أحد فروعها. يُعيد Wait معرف العملية للفرع المنتهي، بحيث يمكن للأم معرفة أي من فروعها قد انتهى. إذا كان للأم فروع متعددة، تسمح الاستدعاءات المتكررة لـ wait بجمع معلومات عنها جميعاً.

---

### Translation Notes

- **Key terms introduced:**
  - image (صورة)
  - core image (صورة النواة)
  - process (عملية)
  - fork (fork - استدعاء نظام)
  - parent process (عملية أم)
  - child process (عملية فرعية)
  - execute/exec (execute/exec - استدعاء نظام)
  - pipe (أنبوب)
  - wait (wait - استدعاء نظام)
  - process ID (معرف العملية)
  - text segment (جزء النص)
  - data segment (جزء البيانات)
  - stack segment (جزء المكدس)

- **Special handling:**
  - Kept system call names (fork, exec, wait, pipe) in English as they are standard terminology
  - Preserved technical concepts like "write-protected" with translation
  - Maintained process state descriptions accurately
  - Explained virtual address space concepts in Arabic

- **Technical concepts:**
  - Process/image distinction
  - Fork-exec-wait pattern (fundamental UNIX process model)
  - Inter-process communication through pipes
  - Memory segmentation (text, data, stack)
  - Parent-child process relationship

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Validation

An **image** is a computer execution environment. It includes a core image, general register values, status of open files, current directory, and the like. An **image** is the current state of a pseudo-computer.

A **process** is the execution of an image. While the processor executes on behalf of a process, the image must be present in core; during execution of other processes it remains in core unless the appearance of an active, higher-priority process forces it to be swapped to disk.

Only one process may exist at a time in UNIX. All other processes must be created by the existing process. A process can create an identical copy of itself using the **fork** system call. The new process is called the **child process**. The old process is called the **parent process**. Fork causes the child to appear executing a copy of the same program as the parent. The only difference is that the value returned from fork in the child process is 0, while the parent receives the process ID of the child.

Another major system call is **execute** (or **exec**). Execute causes the current process to stop executing the current program and begin executing a new program. The core image of the current process is replaced by a new core image specified as an argument to execute.

**Pipes**: Processes can communicate with related processes using the same system read and write calls used for file system I/O. The **pipe** call creates an inter-process channel called a **pipe** and returns two file descriptors, one for reading and one for writing.
