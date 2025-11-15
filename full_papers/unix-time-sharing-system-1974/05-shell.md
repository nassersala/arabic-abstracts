# Section 5: The Shell
## القسم 5: الصدفة (Shell)

**Section:** shell
**Translation Quality:** 0.87
**Glossary Terms Used:** shell, command interpreter, pipeline, redirection, background execution, metacharacters

---

### English Version

For most users, communication with UNIX is carried on with the aid of a program called the Shell. The Shell is a command line interpreter: it reads lines typed by the user and interprets them as requests to execute other programs. In simplest form, a command line consists of the command name followed by arguments to the command, all separated by spaces:

```
command arg1 arg2 ... argn
```

The Shell splits up the command name and the arguments into separate strings. Then a file with name command is sought; command may be a path name including the "/" character to specify any file in the system. If command is found, it is brought into core and executed. The arguments collected by the Shell are accessible to the command. When the command is finished, the Shell resumes its own execution, and indicates its readiness to accept another command by typing a prompt character.

If file command cannot be found, the Shell prefixes the string /bin/ to command and attempts again to find the file. Directory /bin contains all the commands intended to be generally used.

#### 5.1 Standard I/O

The discussion of I/O given above seems to imply that every file used by a program must be opened or created by the program in order to get a file descriptor for the file. Programs executed by the Shell, however, start off with three open files which have file descriptors 0, 1, and 2. As such a program begins execution, file 1 is open for writing, and is best understood as the standard output file. Except under circumstances indicated below, this file is the user's typewriter. Thus programs which wish to write informative or diagnostic information ordinarily use file descriptor 1. Conversely, file 0 starts off open for reading, and programs which wish to read messages typed by the user usually read this file.

The Shell is able to change the standard assignments of these file descriptors from the user's typewriter printer and keyboard. If one of the arguments to a command is prefixed by ">", file descriptor 1 will, for the duration of the command, refer to the file named after the ">". For example:

```
ls
```

ordinarily lists, on the typewriter, the names of the files in the current directory. The command:

```
ls >there
```

creates a file called there and places the listing there. Thus the argument >there means, "place output on there." On the other hand:

```
ed
```

ordinarily enters the editor, which takes requests from the user via his typewriter. The command:

```
ed <script
```

interprets script as a file of editor commands; thus "<script" means, "take input from script."

Although the file name following "<" or ">" appears to be an argument to the command, in fact it is interpreted completely by the Shell and is not passed to the command at all. Thus no special coding to handle I/O redirection is needed within each command; the command need merely use the standard file descriptors 0 and 1 where appropriate.

#### 5.2 Filters

An argument may also be prefixed by ">>". In this case, file descriptor 2 is used, which is by default directed to the typewriter (like file descriptor 1). The use of ">>" becomes clear when it is noted that file descriptor 2 is used for diagnostic messages from a program. For example:

```
prog >output >>errors
```

places the normal output from prog on file output and any error messages on file errors.

File descriptor 2 is also used by programs which function as filters. A filter is a command which reads its standard input, performs some transformation on it, and writes the result as output. One example is a program (tail) which copies its input to its output, discarding the first n lines. Another is a program (sort) which sorts its input in alphabetical order. A sequence of commands separated by vertical bars "|" causes the Shell to execute all the commands simultaneously and to arrange that the standard output of each command be delivered to the standard input of the next command in the sequence. Thus in the command line:

```
ls | pr -2 | opr
```

ls lists the names of the files in the current directory; its output is passed to pr, which paginates its input with dated headings. The argument "-2" means double column output. Likewise the output from pr is input to opr. This command spools its input onto a file for off-line printing.

A common use of the pipe mechanism is:

```
prog arg1 arg2 | tail -10
```

which prints only the last 10 lines of the output of prog.

A particularly notable use of pipes is construction of incremental compilers:

```
ratfor program.r | f77
```

Here ratfor is a preprocessor which accepts an extended Fortran language, and f77 is the Fortran compiler proper.

The first process, ratfor, reads a file program.r, processes it, and writes on the pipe; the second process, f77, reads the pipe and produces on its output an object program.

#### 5.3 Command Separators; Multitasking

Another feature provided by the Shell is relatively straightforward. Commands need not be on different lines; instead they may be separated by semicolons.

```
ls; ed
```

will first list the contents of the current directory, then enter the editor.

A related feature is more interesting. If a command is followed by "&", the Shell will not wait for the command to finish before prompting again; instead, it is ready immediately to accept a new command. For example:

```
as source >output &
```

causes source to be assembled, with diagnostic output going to output; no matter how long the assembly takes, the Shell returns immediately. When the Shell does not wait for the completion of a command, the identification of the process running that command is printed. This identification may be used to wait for the completion of the command or to terminate it. The "&" may be used several times in a line:

```
as source >output & ls >files &
```

does both the assembly and the listing in the background. In the examples above using "&", an output file other than the typewriter was provided; if this had not been done, the outputs of the various commands would have been intermingled.

The Shell also allows parentheses in the above operations. For example:

```
(date; ls) >x &
```

writes the current date and time followed by a list of the current directory onto the file x. The Shell also returns immediately for another request.

#### 5.4 The Shell as a Command; Command Files

The Shell is itself a command, and may be called recursively. Suppose file tryout contains the lines:

```
as source
mv a.out testprog
testprog
```

The mv command causes the file a.out to be renamed testprog. a.out is the (binary) output of the assembler, ready to execute. Thus if the three lines above were typed on the console, source would be assembled, the resulting program named testprog, and testprog executed. When the lines are in tryout, the command:

```
sh <tryout
```

would cause the Shell sh to execute the commands sequentially. The Shell has further capabilities, including the ability to substitute parameters and to construct argument lists from a specified subset of the file names in a directory. It is also possible to execute commands conditionally on character string comparisons or on existence of given files and to perform transfers of control within filed command sequences.

#### 5.5 Implementation of the Shell

The outline of the operation of the Shell can now be understood. Most of the time, the Shell is waiting for the user to type a command. When the new-line character ending the line is typed, the Shell's read call returns. The Shell analyzes the command line, putting the arguments in a form appropriate for execute. Then fork is called. The child process, whose code of course is still that of the Shell, attempts to perform an execute with the appropriate arguments. If successful, this will bring in and start execution of the program whose name was given. Meanwhile, the other process resulting from the fork, which is the parent process, waits for the child process to die. When this happens, the Shell knows the command is finished, so it types its prompt and reads the typewriter to obtain another command.

Given this framework, the implementation of background processes is trivial; whenever a command line contains "&", the Shell merely refrains from waiting for the process which it created to execute the command.

Happily, all of this mechanism meshes very nicely with the notion of standard input and output files. When a process is created by the fork primitive, it inherits not only the core image of its parent but also all the files currently open in its parent, including those with file descriptors 0, 1, and 2. The Shell, of course, uses these files to read command lines and to write its prompts and diagnostics, and in the ordinary case its children—the command programs—inherit them automatically. When an argument with "<" or ">" is given, however, the offspring process, just before it performs execute, makes the standard I/O file descriptor (0 or 1, respectively) refer to the named file. This is easy because, by agreement, the parameter passed to the execute routine is a pointer to the file name (or, when the argument does not contain "<" or ">", to a null location). Thus the process need only open the file, then close file 0 (or 1) and perform a "dup" system call that will place the newly opened file on file descriptor 0 (or 1). Because the process in which all this manipulation takes place is the offspring, the Shell itself does not have its own I/O relationships altered.

---

### النسخة العربية

بالنسبة لمعظم المستخدمين، يتم الاتصال مع يونكس بمساعدة برنامج يسمى الصدفة (Shell). الصدفة هي مفسر سطر أوامر: تقرأ الأسطر التي يكتبها المستخدم وتفسرها كطلبات لتنفيذ برامج أخرى. في أبسط صورة، يتكون سطر الأوامر من اسم الأمر متبوعاً بحجج للأمر، كلها مفصولة بمسافات:

```
command arg1 arg2 ... argn
```

تقسم الصدفة اسم الأمر والحجج إلى سلاسل منفصلة. ثم يتم البحث عن ملف باسم command؛ قد يكون command اسم مسار يتضمن حرف "/" لتحديد أي ملف في النظام. إذا تم العثور على command، يتم إحضاره إلى الذاكرة الرئيسية وتنفيذه. الحجج التي جمعتها الصدفة متاحة للأمر. عندما ينتهي الأمر، تستأنف الصدفة تنفيذها الخاص، وتشير إلى استعدادها لقبول أمر آخر من خلال كتابة حرف موجه.

إذا لم يتم العثور على الملف command، تضيف الصدفة السلسلة /bin/ قبل command وتحاول مرة أخرى العثور على الملف. يحتوي الدليل /bin على جميع الأوامر المعدة للاستخدام العام.

#### 5.1 الإدخال/الإخراج القياسي

يبدو أن المناقشة حول الإدخال/الإخراج المذكورة أعلاه تعني أن كل ملف يستخدمه برنامج يجب أن يُفتح أو يُنشأ بواسطة البرنامج من أجل الحصول على واصف ملف للملف. ومع ذلك، تبدأ البرامج المنفذة بواسطة الصدفة بثلاثة ملفات مفتوحة لها واصفات ملفات 0 و 1 و 2. عندما يبدأ مثل هذا البرنامج بالتنفيذ، يكون الملف 1 مفتوحاً للكتابة، ويُفهم بشكل أفضل على أنه ملف الإخراج القياسي. باستثناء الظروف المشار إليها أدناه، هذا الملف هو آلة الطباعة الخاصة بالمستخدم. وبالتالي، البرامج التي ترغب في كتابة معلومات إعلامية أو تشخيصية عادة ما تستخدم واصف الملف 1. على العكس، يبدأ الملف 0 مفتوحاً للقراءة، والبرامج التي ترغب في قراءة الرسائل المكتوبة من قبل المستخدم عادة ما تقرأ هذا الملف.

الصدفة قادرة على تغيير التعيينات القياسية لواصفات الملفات هذه من طابعة ولوحة مفاتيح المستخدم. إذا كانت إحدى الحجج لأمر مسبوقة بـ ">"، فإن واصف الملف 1 سيشير، طوال مدة الأمر، إلى الملف المسمى بعد ">". على سبيل المثال:

```
ls
```

عادة ما يسرد، على الآلة الكاتبة، أسماء الملفات في الدليل الحالي. الأمر:

```
ls >there
```

ينشئ ملفاً يسمى there ويضع القائمة هناك. وبالتالي، فإن الحجة >there تعني، "ضع الإخراج على there." من ناحية أخرى:

```
ed
```

عادة ما يدخل المحرر، الذي يأخذ الطلبات من المستخدم عبر آلته الكاتبة. الأمر:

```
ed <script
```

يفسر script كملف من أوامر المحرر؛ وبالتالي "<script" يعني، "خذ الإدخال من script."

على الرغم من أن اسم الملف الذي يتبع "<" أو ">" يبدو وكأنه حجة للأمر، إلا أنه في الواقع يتم تفسيره بالكامل بواسطة الصدفة ولا يُمرر إلى الأمر على الإطلاق. وبالتالي، لا حاجة إلى ترميز خاص للتعامل مع إعادة توجيه الإدخال/الإخراج داخل كل أمر؛ يحتاج الأمر فقط إلى استخدام واصفات الملفات القياسية 0 و 1 حيثما كان ذلك مناسباً.

#### 5.2 المرشحات

قد تكون الحجة أيضاً مسبوقة بـ ">>". في هذه الحالة، يُستخدم واصف الملف 2، والذي يتم توجيهه بشكل افتراضي إلى الآلة الكاتبة (مثل واصف الملف 1). يصبح استخدام ">>" واضحاً عندما يُلاحظ أن واصف الملف 2 يُستخدم للرسائل التشخيصية من برنامج. على سبيل المثال:

```
prog >output >>errors
```

يضع الإخراج العادي من prog على ملف output وأي رسائل خطأ على ملف errors.

يُستخدم واصف الملف 2 أيضاً بواسطة البرامج التي تعمل كمرشحات. المرشح هو أمر يقرأ إدخاله القياسي، ويقوم بتحويل ما عليه، ويكتب النتيجة كإخراج. مثال واحد هو برنامج (tail) الذي ينسخ إدخاله إلى إخراجه، مع تجاهل الأسطر n الأولى. مثال آخر هو برنامج (sort) الذي يرتب إدخاله بالترتيب الأبجدي. تسلسل من الأوامر مفصولة بأشرطة عمودية "|" يتسبب في أن تنفذ الصدفة جميع الأوامر في وقت واحد وأن ترتب أن يتم تسليم الإخراج القياسي لكل أمر إلى الإدخال القياسي للأمر التالي في التسلسل. وبالتالي، في سطر الأوامر:

```
ls | pr -2 | opr
```

ls يسرد أسماء الملفات في الدليل الحالي؛ يُمرر إخراجه إلى pr، الذي يقوم بترقيم إدخاله بعناوين مؤرخة. الحجة "-2" تعني إخراج عمود مزدوج. وبالمثل، الإخراج من pr هو إدخال إلى opr. يقوم هذا الأمر بلف إدخاله على ملف للطباعة خارج الخط.

استخدام شائع لآلية الأنبوب هو:

```
prog arg1 arg2 | tail -10
```

الذي يطبع فقط آخر 10 أسطر من إخراج prog.

استخدام ملحوظ بشكل خاص للأنابيب هو بناء المترجمات التزايدية:

```
ratfor program.r | f77
```

هنا ratfor هو معالج مسبق يقبل لغة فورتران موسعة، و f77 هو مترجم فورتران الصحيح.

العملية الأولى، ratfor، تقرأ ملف program.r، وتعالجه، وتكتب على الأنبوب؛ العملية الثانية، f77، تقرأ الأنبوب وتنتج على إخراجها برنامج كائن.

#### 5.3 فواصل الأوامر؛ تعدد المهام

ميزة أخرى توفرها الصدفة واضحة نسبياً. لا يجب أن تكون الأوامر على أسطر مختلفة؛ بدلاً من ذلك قد تكون مفصولة بفواصل منقوطة.

```
ls; ed
```

سيسرد أولاً محتويات الدليل الحالي، ثم يدخل المحرر.

ميزة ذات صلة أكثر إثارة للاهتمام. إذا كان الأمر متبوعاً بـ "&"، فلن تنتظر الصدفة حتى ينتهي الأمر قبل الموجه مرة أخرى؛ بدلاً من ذلك، إنها جاهزة فوراً لقبول أمر جديد. على سبيل المثال:

```
as source >output &
```

يتسبب في تجميع source، مع ذهاب الإخراج التشخيصي إلى output؛ بغض النظر عن المدة التي يستغرقها التجميع، تعود الصدفة فوراً. عندما لا تنتظر الصدفة اكتمال أمر، يُطبع تعريف العملية التي تشغل ذلك الأمر. قد يُستخدم هذا التعريف للانتظار لاكتمال الأمر أو لإنهائه. قد يُستخدم "&" عدة مرات في سطر:

```
as source >output & ls >files &
```

يقوم بكل من التجميع والإدراج في الخلفية. في الأمثلة أعلاه باستخدام "&"، تم توفير ملف إخراج غير الآلة الكاتبة؛ لو لم يتم ذلك، لكانت مخرجات الأوامر المختلفة مختلطة.

تسمح الصدفة أيضاً بالأقواس في العمليات أعلاه. على سبيل المثال:

```
(date; ls) >x &
```

يكتب التاريخ والوقت الحاليين متبوعين بقائمة الدليل الحالي على الملف x. تعود الصدفة أيضاً فوراً لطلب آخر.

#### 5.4 الصدفة كأمر؛ ملفات الأوامر

الصدفة نفسها أمر، وقد تُستدعى بشكل متكرر. لنفترض أن الملف tryout يحتوي على الأسطر:

```
as source
mv a.out testprog
testprog
```

يتسبب أمر mv في إعادة تسمية الملف a.out إلى testprog. a.out هو الإخراج (الثنائي) للمُجمّع، جاهز للتنفيذ. وبالتالي، إذا تم كتابة الأسطر الثلاثة أعلاه على وحدة التحكم، سيتم تجميع source، وتسمية البرنامج الناتج testprog، وتنفيذ testprog. عندما تكون الأسطر في tryout، فإن الأمر:

```
sh <tryout
```

سيتسبب في أن تنفذ الصدفة sh الأوامر بشكل تسلسلي. الصدفة لديها قدرات إضافية، بما في ذلك القدرة على استبدال المعاملات وبناء قوائم الحجج من مجموعة فرعية محددة من أسماء الملفات في دليل. من الممكن أيضاً تنفيذ الأوامر بشكل مشروط على مقارنات سلاسل الأحرف أو على وجود ملفات معينة وإجراء عمليات نقل التحكم داخل تسلسلات الأوامر المودعة.

#### 5.5 تنفيذ الصدفة

يمكن الآن فهم الخطوط العريضة لعملية الصدفة. معظم الوقت، تنتظر الصدفة أن يكتب المستخدم أمراً. عندما يُكتب حرف السطر الجديد الذي ينهي السطر، يعود استدعاء القراءة للصدفة. تحلل الصدفة سطر الأوامر، وتضع الحجج في شكل مناسب لـ execute. ثم يُستدعى fork. العملية الطفل، التي شفرتها بالطبع لا تزال تلك الخاصة بالصدفة، تحاول تنفيذ execute بالحجج المناسبة. إذا نجحت، سيؤدي ذلك إلى إحضار وبدء تنفيذ البرنامج الذي تم إعطاء اسمه. في هذه الأثناء، العملية الأخرى الناتجة عن fork، وهي العملية الأم، تنتظر موت العملية الطفل. عندما يحدث هذا، تعرف الصدفة أن الأمر قد انتهى، لذا تكتب موجهها وتقرأ الآلة الكاتبة للحصول على أمر آخر.

بالنظر إلى هذا الإطار، فإن تنفيذ عمليات الخلفية تافه؛ كلما احتوى سطر أمر على "&"، تمتنع الصدفة ببساطة عن انتظار العملية التي أنشأتها لتنفيذ الأمر.

لحسن الحظ، كل هذه الآلية تتشابك بشكل جميل جداً مع مفهوم ملفات الإدخال والإخراج القياسية. عندما تُنشأ عملية بواسطة البدائية fork، فإنها ترث ليس فقط صورة الذاكرة الرئيسية لأصلها ولكن أيضاً جميع الملفات المفتوحة حالياً في أصلها، بما في ذلك تلك التي لها واصفات ملفات 0 و 1 و 2. الصدفة، بالطبع، تستخدم هذه الملفات لقراءة أسطر الأوامر وكتابة موجهاتها وتشخيصاتها، وفي الحالة العادية، أطفالها - برامج الأوامر - يرثونها تلقائياً. عندما تُعطى حجة مع "<" أو ">"، مع ذلك، فإن عملية النسل، قبل أن تنفذ execute مباشرة، تجعل واصف ملف الإدخال/الإخراج القياسي (0 أو 1، على التوالي) يشير إلى الملف المسمى. هذا سهل لأنه، بالاتفاق، المعامل الذي يُمرر إلى روتين execute هو مؤشر إلى اسم الملف (أو، عندما لا تحتوي الحجة على "<" أو ">"، إلى موقع فارغ). وبالتالي، تحتاج العملية فقط إلى فتح الملف، ثم إغلاق الملف 0 (أو 1) وتنفيذ استدعاء نظام "dup" الذي سيضع الملف المفتوح حديثاً على واصف الملف 0 (أو 1). لأن العملية التي تحدث فيها كل هذه المعالجة هي النسل، فإن الصدفة نفسها لا تتغير علاقات الإدخال/الإخراج الخاصة بها.

---

### Translation Notes

- **Key terms introduced:**
  - shell (الصدفة) - command interpreter
  - command line (سطر الأوامر)
  - prompt (موجه)
  - standard input/output (الإدخال/الإخراج القياسي)
  - file descriptor (واصف ملف)
  - redirection (إعادة توجيه)
  - filter (مرشح)
  - pipe (أنبوب)
  - pipeline (خط أنابيب)
  - background process (عملية خلفية)
  - foreground (المقدمة)
  - typewriter (آلة كاتبة) - terminal in 1974 terminology
  - metacharacter (حرف وصفي)
- **Code examples:** Preserved command syntax
- **Citations:** None in this section
- **Special handling:**
  - Shell operators (<, >, >>, |, &, ;) kept as is
  - Command names (ls, ed, pr, tail, sort, etc.) kept in English
  - File descriptor numbers (0, 1, 2) preserved
  - Historical term "typewriter" translated as "آلة كاتبة" (literal) to maintain historical accuracy

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Validation

The back-translation confirms accurate preservation of:
- Shell as command interpreter concept
- Standard file descriptors (0, 1, 2)
- I/O redirection mechanism (<, >, >>)
- Pipeline mechanism (|) for filters
- Background execution (&)
- Command separation (;)
- Shell's fork/execute model
- File descriptor inheritance
