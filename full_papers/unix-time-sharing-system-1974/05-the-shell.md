# Section 5: The Shell
## القسم 5: الشل (Shell)

**Section:** the-shell
**Translation Quality:** 0.89
**Glossary Terms Used:** shell, command, process, pipe, I/O redirection, background, foreground

---

### English Version

For most users, communication with UNIX is carried on with the aid of a program called the **shell**. The shell is a command line interpreter: it reads lines typed by the user and interprets them as requests to execute other programs. In simplest form, a command line consists of the command name followed by arguments to the command, all separated by spaces:

```
command arg₁ arg₂ ... argₙ
```

The shell splits up the command name and the arguments into separate strings. Then a file with name *command* is sought; *command* may be a path name including the "/" character to specify any file in the system. If *command* is found, it is brought into core and executed. The arguments collected by the shell are passed to the command. When the command is finished, the shell resumes its own execution, and indicates its readiness to accept another command by typing a prompt character.

**Standard I/O**

The instances of I/O redirection already mentioned illustrate the fact that the shell arranges the environment for a command before the command is executed. In the simplest case, the shell opens its own input and output files and makes them available to the command. If the command reads from standard input or writes to standard output, it will use these pre-opened files.

The shell can be asked to redirect input or output to a file by using special notation. If any of the arguments to a command is of the form `>file` or `<file`, the shell will open the file for writing or reading respectively, and arrange for it to be used as standard output or standard input. For example:

```
command >outfile
```

causes the command to be executed with standard output connected to file `outfile` instead of the user's terminal. Similarly:

```
command <infile
```

causes the standard input to be taken from file `infile` rather than from the terminal.

**Filters and Pipes**

One of the most useful features of UNIX is the ability to connect programs together using pipes. The notation `|` is used to construct a pipeline. For example:

```
command₁ | command₂
```

This causes the shell to execute *command₁* and *command₂* simultaneously. The standard output of *command₁* is connected via a pipe to the standard input of *command₂*. The effect is that the output of the first command becomes the input to the second. This facility, combined with a set of small programs each of which does one simple task, allows very complex operations to be performed by combining simple commands.

A program such as *command₂* which takes input from another program, processes it, and produces output for use by other programs, is called a **filter**. A large set of filters provided with UNIX allows manipulation of text, sorting, searching, and many other operations.

**Background Processes**

The shell allows commands to be executed in the background. If a command line is terminated by the character `&`, the shell does not wait for the command to finish. Instead, it immediately prompts for the next command. The command executes asynchronously; its output will appear on the terminal intermixed with other activities. For example:

```
command &
```

This feature is particularly useful for long-running commands that do not require interaction with the user.

**The Shell as a Programming Language**

The shell is itself a programming language. Command lines stored in a file can be executed by naming the file as a command. Such a file is called a **shell procedure** or **shell script**. Arguments can be passed to shell procedures, and the shell provides control flow constructs including conditional execution and loops.

**Implementation**

The shell is a user-level program, not part of the kernel. This means it can be replaced by any other program. Different users can select different command interpreters. The shell executes commands using the standard fork-exec mechanism: it forks a child process, and the child executes the requested program. The parent shell waits for the child to complete (unless the command is executed in the background).

When the shell forks to create a child process to execute a command, the child inherits the shell's open file descriptors. Before executing the command, the child can close these and open new files for redirection. This is how I/O redirection is implemented. Pipes are created by the shell before forking; both the parent and child have access to the pipe file descriptors, allowing data to flow between commands.

---

### النسخة العربية

بالنسبة لمعظم المستخدمين، يتم التواصل مع يونكس بمساعدة برنامج يسمى **الشل** (shell). الشل هو مفسر سطر الأوامر: يقرأ الأسطر التي يكتبها المستخدم ويفسرها كطلبات لتنفيذ برامج أخرى. في أبسط صورة، يتكون سطر الأوامر من اسم الأمر متبوعاً بوسائط للأمر، كلها مفصولة بمسافات:

```
command arg₁ arg₂ ... argₙ
```

يقسم الشل اسم الأمر والوسائط إلى سلاسل منفصلة. ثم يتم البحث عن ملف باسم *command*؛ قد يكون *command* اسم مسار يتضمن حرف "/" لتحديد أي ملف في النظام. إذا تم العثور على *command*، يتم جلبه إلى النواة وتنفيذه. يتم تمرير الوسائط التي جمعها الشل إلى الأمر. عندما ينتهي الأمر، يستأنف الشل تنفيذه الخاص، ويشير إلى استعداده لقبول أمر آخر عن طريق كتابة حرف مطالبة (prompt).

**الإدخال/الإخراج القياسي**

توضح حالات إعادة توجيه الإدخال/الإخراج المذكورة بالفعل حقيقة أن الشل يرتب البيئة لأمر قبل تنفيذ الأمر. في أبسط حالة، يفتح الشل ملفات الإدخال والإخراج الخاصة به ويجعلها متاحة للأمر. إذا قرأ الأمر من الإدخال القياسي أو كتب إلى الإخراج القياسي، فسيستخدم هذه الملفات المفتوحة مسبقاً.

يمكن أن يُطلب من الشل إعادة توجيه الإدخال أو الإخراج إلى ملف باستخدام تدوين خاص. إذا كانت أي من وسائط الأمر من الشكل `>file` أو `<file`، فسيفتح الشل الملف للكتابة أو القراءة على التوالي، ويرتب لاستخدامه كإخراج قياسي أو إدخال قياسي. على سبيل المثال:

```
command >outfile
```

يتسبب في تنفيذ الأمر مع إخراج قياسي متصل بالملف `outfile` بدلاً من طرفية المستخدم. وبالمثل:

```
command <infile
```

يتسبب في أخذ الإدخال القياسي من الملف `infile` بدلاً من الطرفية.

**المرشحات والأنابيب**

واحدة من أكثر الميزات فائدة في يونكس هي القدرة على ربط البرامج معاً باستخدام الأنابيب (pipes). يُستخدم التدوين `|` لإنشاء خط أنابيب (pipeline). على سبيل المثال:

```
command₁ | command₂
```

يتسبب هذا في أن ينفذ الشل *command₁* و *command₂* في وقت واحد. يتم توصيل الإخراج القياسي لـ *command₁* عبر أنبوب إلى الإدخال القياسي لـ *command₂*. التأثير هو أن إخراج الأمر الأول يصبح إدخال الثاني. هذه المرفق، جنباً إلى جنب مع مجموعة من البرامج الصغيرة يقوم كل منها بمهمة بسيطة واحدة، يسمح بإجراء عمليات معقدة جداً عن طريق دمج أوامر بسيطة.

البرنامج مثل *command₂* الذي يأخذ الإدخال من برنامج آخر، ويعالجه، وينتج إخراجاً للاستخدام بواسطة برامج أخرى، يسمى **مرشح** (filter). مجموعة كبيرة من المرشحات المقدمة مع يونكس تسمح بمعالجة النص، والفرز، والبحث، والعديد من العمليات الأخرى.

**العمليات في الخلفية**

يسمح الشل بتنفيذ الأوامر في الخلفية (background). إذا انتهى سطر الأوامر بالحرف `&`, لا ينتظر الشل انتهاء الأمر. بدلاً من ذلك، يطالب فوراً بالأمر التالي. ينفذ الأمر بشكل لا متزامن؛ سيظهر إخراجه على الطرفية متداخلاً مع الأنشطة الأخرى. على سبيل المثال:

```
command &
```

هذه الميزة مفيدة بشكل خاص للأوامر طويلة المدة التي لا تتطلب تفاعلاً مع المستخدم.

**الشل كلغة برمجة**

الشل نفسه لغة برمجة. يمكن تنفيذ أسطر الأوامر المخزنة في ملف عن طريق تسمية الملف كأمر. يسمى هذا الملف **إجراء شل** (shell procedure) أو **نص شل** (shell script). يمكن تمرير الوسائط إلى إجراءات الشل، ويوفر الشل بنيات التحكم في التدفق بما في ذلك التنفيذ الشرطي والحلقات.

**التنفيذ**

الشل هو برنامج على مستوى المستخدم، وليس جزءاً من النواة (kernel). هذا يعني أنه يمكن استبداله بأي برنامج آخر. يمكن للمستخدمين المختلفين اختيار مفسرات أوامر مختلفة. ينفذ الشل الأوامر باستخدام آلية fork-exec القياسية: يقوم بعمل fork لعملية فرعية، وينفذ الفرع البرنامج المطلوب. ينتظر الشل الأم اكتمال الفرع (ما لم يتم تنفيذ الأمر في الخلفية).

عندما يقوم الشل بعمل fork لإنشاء عملية فرعية لتنفيذ أمر، يرث الفرع واصفات الملفات المفتوحة للشل. قبل تنفيذ الأمر، يمكن للفرع إغلاق هذه وفتح ملفات جديدة لإعادة التوجيه. هذه هي كيفية تنفيذ إعادة توجيه الإدخال/الإخراج. يتم إنشاء الأنابيب بواسطة الشل قبل fork؛ كل من الأم والفرع لديهما وصول إلى واصفات ملفات الأنبوب، مما يسمح بتدفق البيانات بين الأوامر.

---

### Translation Notes

- **Key terms introduced:**
  - shell (شل)
  - command line interpreter (مفسر سطر الأوامر)
  - prompt (مطالبة / حرف مطالبة)
  - I/O redirection (إعادة توجيه الإدخال/الإخراج)
  - standard input/output (إدخال/إخراج قياسي)
  - pipe (أنبوب)
  - pipeline (خط أنابيب)
  - filter (مرشح)
  - background process (عملية في الخلفية)
  - shell procedure/script (إجراء شل / نص شل)

- **Special handling:**
  - Preserved shell syntax (`>`, `<`, `|`, `&`) in code blocks
  - Kept command examples in English as they are programming syntax
  - Maintained subscript notation (arg₁, arg₂, command₁, command₂)
  - Explained technical operations in clear Arabic

- **Technical concepts:**
  - Shell as user-level program (not kernel component)
  - I/O redirection mechanism
  - Pipeline construction for command composition
  - Filter pattern for text processing
  - Background/foreground execution
  - Shell as programmable interface

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89

### Back-Translation Validation

For most users, communication with UNIX is carried out with the help of a program called the **shell**. The shell is a command line interpreter: it reads lines written by the user and interprets them as requests to execute other programs. In simplest form, a command line consists of the command name followed by parameters for the command, all separated by spaces.

The shell splits the command name and parameters into separate strings. Then a file named *command* is searched for; *command* may be a path name including the "/" character to specify any file in the system. If *command* is found, it is brought into core and executed. The parameters collected by the shell are passed to the command. When the command finishes, the shell resumes its own execution, and indicates its readiness to accept another command by writing a prompt character.

**Standard I/O**: The shell can be asked to redirect input or output to a file using special notation. If any command parameters are of the form `>file` or `<file`, the shell will open the file for writing or reading respectively, and arrange for it to be used as standard output or standard input.

**Filters and Pipes**: One of the most useful features in UNIX is the ability to connect programs together using pipes. The notation `|` is used to create a pipeline. A program that takes input from another program, processes it, and produces output for use by other programs is called a **filter**.

**Background Processes**: The shell allows commands to be executed in the background. If a command line ends with the `&` character, the shell does not wait for the command to finish. Instead, it immediately prompts for the next command.

**The Shell as a Programming Language**: The shell itself is a programming language. Command lines stored in a file can be executed by naming the file as a command. Such a file is called a **shell procedure** or **shell script**.

**Implementation**: The shell is a user-level program, not part of the kernel. This means it can be replaced by any other program. The shell executes commands using the standard fork-exec mechanism.
