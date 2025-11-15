# Section 4: Processes and Images
## القسم 4: العمليات والصور

**Section:** processes-images
**Translation Quality:** 0.88
**Glossary Terms Used:** process, image, execution, fork, execute, system call, memory, core, swap

---

### English Version

An image is a computer execution environment. It includes a core image, general register values, status of open files, current directory, and the like. An image is the current state of a pseudo-computer.

A process is the execution of an image. While the processor is executing on behalf of a process, the image must reside in core; during the execution of other processes it remains in core unless the appearance of an active, higher-priority process forces it to be swapped out to the fixed-head disk.

The user-core part of an image is divided into three logical segments. The program text segment begins at location 0 in the virtual address space. During execution, this segment is write-protected and a single copy of it is shared among all processes executing the same program. At the first hardware protection byte boundary above the program text segment in the virtual address space begins a nonshared, writable data segment, the size of which may be extended by a system call. Starting at the highest address in the virtual address space is a stack segment, which automatically grows downward as the hardware's stack pointer fluctuates.

#### 4.1 Processes

Except while UNIX is bootstrapping itself into operation, a new process can come into existence only by use of the fork system call:

```
processid = fork(label)
```

When fork is executed by a process, it splits into two independently executing processes. The two processes have independent copies of the original core image, and share any open files. The new processes differ only in that one is considered the parent process: in the parent, control returns directly from the fork, while in the child, control is passed to location label. The processid returned by the fork call is the identification of the other process.

Because the return points in the parent and child process are not the same, each image existing after a fork may determine whether it is the parent or child process.

#### 4.2 Execution

Another system call is the execute system call, which transforms the calling process into a new process:

```
execute(file, arg1, arg2, ..., argn)
```

The execute call takes the program text and data from a file and loads it into the calling process. Thus the contents of the file are a program (in core image format, i.e., in memory format as it would appear in core while executing) augmented by a series of arguments, arg1, arg2, ..., argn.

An argument may be a pointer to a null-terminated character string. The normal case for this is passing command arguments to the program being executed.

The calling process is destroyed in the sense that all of its data and program text are replaced, but the set of open files, current directory, and interprocess relationships are retained.

Only the execute system call changes the program being executed by a process. Only the fork system call creates a new process. The two operations together allow a process to load and execute a program wholly different from the program it was running before.

#### 4.3 Process Synchronization

Another process control system call:

```
processid = wait()
```

causes its caller to suspend execution until one of its children has completed execution. Then wait returns the processid of the terminated child. An error return is taken if the calling process has no living or unwaited-for children.

#### 4.4 Termination

Lastly:

```
exit(status)
```

terminates a process, destroys its image, closes its open files, and generally obliterates it. When the parent is notified through the wait primitive, the indicated status is available to the parent. Processes may also terminate as a result of various illegal actions or user-generated signals (Section 7 below).

---

### النسخة العربية

الصورة هي بيئة تنفيذ حاسوبية. تتضمن صورة الذاكرة الرئيسية، وقيم السجلات العامة، وحالة الملفات المفتوحة، والدليل الحالي، وما شابه ذلك. الصورة هي الحالة الحالية لحاسوب زائف.

العملية هي تنفيذ صورة. بينما يقوم المعالج بالتنفيذ نيابة عن عملية، يجب أن تقيم الصورة في الذاكرة الرئيسية؛ أثناء تنفيذ عمليات أخرى، تبقى في الذاكرة الرئيسية ما لم يجبرها ظهور عملية نشطة ذات أولوية أعلى على التبديل إلى القرص ذي الرأس الثابت.

ينقسم جزء الذاكرة الرئيسية للمستخدم من الصورة إلى ثلاثة قطاعات منطقية. يبدأ قطاع نص البرنامج في الموقع 0 في فضاء العنونة الافتراضي. أثناء التنفيذ، هذا القطاع محمي من الكتابة ويتم مشاركة نسخة واحدة منه بين جميع العمليات التي تنفذ نفس البرنامج. عند أول حد بايت حماية للأجهزة فوق قطاع نص البرنامج في فضاء العنونة الافتراضي، يبدأ قطاع بيانات قابل للكتابة غير مشترك، يمكن تمديد حجمه بواسطة استدعاء نظام. بدءاً من أعلى عنوان في فضاء العنونة الافتراضي، يوجد قطاع مكدس، ينمو تلقائياً لأسفل مع تقلب مؤشر المكدس للأجهزة.

#### 4.1 العمليات

باستثناء الوقت الذي يقوم فيه يونكس بتمهيد نفسه للعمل، لا يمكن لعملية جديدة أن توجد إلا باستخدام استدعاء نظام fork:

```
processid = fork(label)
```

عندما يُنفذ fork بواسطة عملية، تنقسم إلى عمليتين تنفذان بشكل مستقل. العمليتان لديهما نسخ مستقلة من صورة الذاكرة الرئيسية الأصلية، وتتشاركان أي ملفات مفتوحة. العمليات الجديدة تختلف فقط في أن واحدة تُعتبر العملية الأم: في الأم، يعود التحكم مباشرة من fork، بينما في الطفل، يُمرر التحكم إلى الموقع label. الـ processid الذي يُرجعه استدعاء fork هو تعريف العملية الأخرى.

نظراً لأن نقاط العودة في العملية الأم والطفل ليست نفسها، فإن كل صورة موجودة بعد fork قد تحدد ما إذا كانت العملية الأم أو الطفل.

#### 4.2 التنفيذ

استدعاء نظام آخر هو استدعاء نظام execute، الذي يحول العملية المستدعية إلى عملية جديدة:

```
execute(file, arg1, arg2, ..., argn)
```

يأخذ استدعاء execute نص البرنامج والبيانات من ملف ويحملها في العملية المستدعية. وبالتالي، فإن محتويات الملف هي برنامج (بتنسيق صورة الذاكرة الرئيسية، أي بتنسيق الذاكرة كما ستظهر في الذاكرة الرئيسية أثناء التنفيذ) مُعزز بسلسلة من الحجج arg1، arg2، ...، argn.

قد تكون الحجة مؤشراً إلى سلسلة أحرف منتهية بقيمة فارغة. الحالة الطبيعية لهذا هي تمرير حجج الأوامر إلى البرنامج الذي يتم تنفيذه.

يتم تدمير العملية المستدعية بمعنى أن جميع بياناتها ونص برنامجها يتم استبدالها، لكن يتم الاحتفاظ بمجموعة الملفات المفتوحة والدليل الحالي والعلاقات بين العمليات.

فقط استدعاء نظام execute يغير البرنامج الذي يتم تنفيذه بواسطة عملية. فقط استدعاء نظام fork ينشئ عملية جديدة. العمليتان معاً تسمحان لعملية بتحميل وتنفيذ برنامج يختلف تماماً عن البرنامج الذي كانت تشغله من قبل.

#### 4.3 مزامنة العمليات

استدعاء نظام تحكم في العمليات آخر:

```
processid = wait()
```

يتسبب في تعليق تنفيذ المستدعي حتى يكمل أحد أطفاله التنفيذ. ثم يُرجع wait معرّف العملية للطفل المنتهي. يتم إرجاع خطأ إذا لم يكن للعملية المستدعية أطفال أحياء أو لم يتم انتظارهم.

#### 4.4 الإنهاء

أخيراً:

```
exit(status)
```

ينهي عملية، ويدمر صورتها، ويغلق ملفاتها المفتوحة، ويمحوها بشكل عام. عندما يتم إخطار الأم من خلال البدائية wait، تكون الحالة المشار إليها متاحة للأم. قد تنتهي العمليات أيضاً نتيجة لإجراءات غير قانونية مختلفة أو إشارات ناتجة عن المستخدم (القسم 7 أدناه).

---

### Translation Notes

- **Key terms introduced:**
  - image (صورة) - execution environment
  - process (عملية) - execution of an image
  - core image (صورة الذاكرة الرئيسية) - memory contents
  - pseudo-computer (حاسوب زائف) - virtual machine concept
  - swap (تبديل) - swapping to disk
  - text segment (قطاع نص) - program code
  - data segment (قطاع بيانات) - writable data
  - stack segment (قطاع مكدس) - stack memory
  - virtual address space (فضاء العنونة الافتراضي) - virtual memory
  - fork (fork) - kept as technical term, explained in context
  - execute (execute) - kept as technical term
  - parent process (العملية الأم) - parent
  - child process (الطفل) - child
  - wait (wait) - synchronization primitive
  - exit (exit) - termination
  - bootstrap (تمهيد) - system initialization
- **Code examples:** Preserved in English as they are API calls
- **Citations:** Reference to Section 7
- **Special handling:**
  - System call names (fork, execute, wait, exit) kept in English as they are API identifiers
  - Code syntax preserved
  - Location 0 preserved as number

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Validation

The back-translation confirms accurate preservation of:
- Image vs. process distinction
- Memory segment organization (text, data, stack)
- fork() system call creating two processes
- execute() transforming a process
- wait() for process synchronization
- exit() for process termination
- Parent-child process relationships
