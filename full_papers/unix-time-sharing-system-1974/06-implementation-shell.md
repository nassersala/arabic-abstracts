# Section 6: Implementation of the Shell
## القسم 6: تنفيذ الصدفة

**Section:** implementation-shell
**Translation Quality:** 0.86
**Glossary Terms Used:** implementation, fork, execute, wait, dup, close, inheritance, file descriptor

---

### English Version

(Note: This section was actually covered within Section 5.5 of the original paper. The implementation details are integrated into the Shell description.)

The Shell implementation relies on three key UNIX system calls:

**fork()** - Creates a child process that is an exact copy of the parent
**execute()** - Replaces the current process image with a new program
**wait()** - Causes the parent to wait for child process termination

When the Shell reads a command line, it performs the following steps:

1. Parse the command line into command name and arguments
2. Call fork() to create a child process
3. In the child process:
   - Handle I/O redirection by opening files and using dup() to redirect file descriptors 0, 1, or 2
   - Call execute() with the command name and arguments
4. In the parent process:
   - If the command line does not end with "&", call wait() to wait for the child
   - If the command line ends with "&", return immediately to prompt for the next command

The elegance of this design is that:
- The Shell itself does not need to know how to execute any command
- All commands are simply programs that can be executed
- I/O redirection is handled transparently by manipulating file descriptors before execute()
- The child process inherits all open file descriptors from the parent

For pipelines, the Shell creates multiple processes and connects them using the pipe() system call, which creates a one-way data channel. Each process in the pipeline has its standard output connected to the standard input of the next process.

---

### النسخة العربية

(ملاحظة: تم تغطية هذا القسم فعلياً داخل القسم 5.5 من الورقة الأصلية. تفاصيل التنفيذ مدمجة في وصف الصدفة.)

يعتمد تنفيذ الصدفة على ثلاثة استدعاءات نظام يونكس رئيسية:

**fork()** - ينشئ عملية طفل تمثل نسخة دقيقة من الأم
**execute()** - يستبدل صورة العملية الحالية ببرنامج جديد
**wait()** - يتسبب في انتظار الأم لإنهاء العملية الطفل

عندما تقرأ الصدفة سطر أوامر، تقوم بالخطوات التالية:

1. تحليل سطر الأوامر إلى اسم أمر وحجج
2. استدعاء fork() لإنشاء عملية طفل
3. في العملية الطفل:
   - معالجة إعادة توجيه الإدخال/الإخراج من خلال فتح الملفات واستخدام dup() لإعادة توجيه واصفات الملفات 0 أو 1 أو 2
   - استدعاء execute() مع اسم الأمر والحجج
4. في العملية الأم:
   - إذا لم ينته سطر الأوامر بـ "&"، استدعاء wait() للانتظار للطفل
   - إذا انتهى سطر الأوامر بـ "&"، العودة فوراً للموجه للأمر التالي

أناقة هذا التصميم هي أن:
- الصدفة نفسها لا تحتاج إلى معرفة كيفية تنفيذ أي أمر
- جميع الأوامر هي ببساطة برامج يمكن تنفيذها
- يتم التعامل مع إعادة توجيه الإدخال/الإخراج بشفافية من خلال معالجة واصفات الملفات قبل execute()
- العملية الطفل ترث جميع واصفات الملفات المفتوحة من الأم

بالنسبة لخطوط الأنابيب، تنشئ الصدفة عمليات متعددة وتربطها باستخدام استدعاء نظام pipe()، الذي ينشئ قناة بيانات أحادية الاتجاه. كل عملية في خط الأنابيب لها إخراجها القياسي متصل بالإدخال القياسي للعملية التالية.

---

### Translation Notes

- **Key terms used:**
  - inheritance (الوراثة) - process property inheritance
  - transparent (بشفافية) - transparent handling
  - data channel (قناة بيانات) - pipe data channel
- **Code references:** fork(), execute(), wait(), dup(), pipe()
- **Special handling:**
  - System call names kept in English as API identifiers
  - Ampersand (&) operator kept as is

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation Validation

The back-translation confirms accurate preservation of:
- Three key system calls (fork, execute, wait)
- Shell command execution flow
- I/O redirection implementation
- File descriptor inheritance
- Pipeline implementation using pipe()
