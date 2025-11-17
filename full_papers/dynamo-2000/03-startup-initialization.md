# Section 3: Startup and Initialization
## القسم 3: بدء التشغيل والتهيئة

**Section:** startup-and-initialization
**Translation Quality:** 0.88
**Glossary Terms Used:** dynamically linked library, shared library, stack, runtime stack, interpreter, fragment cache, transparent operation, memory mapping, context switch

---

### English Version

Dynamo is provided as a user-mode dynamically linked library (shared library). The entry point into this library is the routine dynamo_exec. When dynamo_exec is invoked by an application, the remainder of the application code after return from the dynamo_exec call will execute under Dynamo control.

As outlined in Figure 2, dynamo_exec first saves a snapshot of the application's context (i.e., the machine registers and stack environment) to an internal app-context data structure. It then swaps the stack environment so that Dynamo's own code uses a custom runtime stack allocated separately for its use. Dynamo's operation thus does not interfere with the runtime stack of the application running on it. The interpreter (box A in Figure 1) is eventually invoked with the return-pc corresponding to the application's dynamo_exec call. The interpreter starts interpreting the application code from this return-pc, using the context saved in app-context. The interpreter never returns to dynamo_exec (unless a special bailout condition occurs, which is discussed later), and Dynamo has gained control over the application. From this point onwards, an application instruction is either interpreted, or a copy of it is executed in the fragment cache. The original instruction is never executed in place the way it would have been if the application were running directly on the processor.

We provide a custom version of the execution startup code crt0.o, that checks to see if the Dynamo library is installed on the system, and if it is, invokes dynamo_start prior to the jump to _start (the application's main entry point). Application binaries that are linked with this version of crt0.o will transparently invoke Dynamo if Dynamo is installed on the system, otherwise they will execute normally. The application binary itself remains unchanged whether or not it is run under Dynamo. This strategy allows Dynamo to preserve the original mapping of the application's text segment, a key requirement for transparent operation.

As part of the initialization done in dynamo_exec prior to actually invoking the interpreter, Dynamo mmaps a separate area of memory that it manages itself. All dynamically allocated objects in Dynamo code are created in this area of memory. Access to this area is protected to prevent the application from inadvertently or maliciously corrupting Dynamo's state.

---

### النسخة العربية

يُقدَّم دينامو كمكتبة مرتبطة ديناميكياً في وضع المستخدم (مكتبة مشتركة). نقطة الدخول إلى هذه المكتبة هي الدالة dynamo_exec. عندما يستدعي تطبيق dynamo_exec، فإن بقية شيفرة التطبيق بعد العودة من استدعاء dynamo_exec ستُنفَّذ تحت سيطرة دينامو.

كما هو موضح في الشكل 2، يحفظ dynamo_exec أولاً لقطة من سياق التطبيق (أي سجلات الآلة وبيئة المكدس) في بنية بيانات داخلية تُسمى app-context. ثم يبدِّل بيئة المكدس بحيث تستخدم شيفرة دينامو نفسها مكدس تشغيل مخصص مُخصَّص بشكل منفصل لاستخدامه. وبالتالي فإن عمل دينامو لا يتداخل مع مكدس التشغيل للتطبيق الذي يعمل عليه. يُستدعى المفسِّر (المربع A في الشكل 1) في النهاية مع return-pc المقابل لاستدعاء dynamo_exec للتطبيق. يبدأ المفسِّر في تفسير شيفرة التطبيق من هذا return-pc، باستخدام السياق المحفوظ في app-context. لا يعود المفسِّر أبداً إلى dynamo_exec (ما لم تحدث حالة خروج طارئ خاصة، والتي تُناقَش لاحقاً)، وبذلك يكون دينامو قد حصل على السيطرة على التطبيق. من هذه النقطة فصاعداً، إما أن تُفسَّر تعليمة التطبيق، أو تُنفَّذ نسخة منها في ذاكرة الأجزاء المؤقتة. لا تُنفَّذ التعليمة الأصلية أبداً في مكانها بالطريقة التي كانت ستُنفَّذ بها لو كان التطبيق يعمل مباشرة على المعالج.

نوفر نسخة مخصصة من شيفرة بدء التنفيذ crt0.o، التي تتحقق مما إذا كانت مكتبة دينامو مثبتة على النظام، وإذا كانت كذلك، تستدعي dynamo_start قبل القفز إلى _start (نقطة الدخول الرئيسية للتطبيق). الملفات الثنائية للتطبيقات المرتبطة بهذه النسخة من crt0.o ستستدعي دينامو بشكل شفاف إذا كان دينامو مثبتاً على النظام، وإلا فستُنفَّذ بشكل طبيعي. يظل الملف الثنائي للتطبيق نفسه دون تغيير سواء تم تشغيله تحت دينامو أم لا. تسمح هذه الاستراتيجية لدينامو بالحفاظ على التخطيط الأصلي لقطعة النص للتطبيق، وهو متطلب رئيسي للعمل الشفاف.

كجزء من التهيئة التي تتم في dynamo_exec قبل استدعاء المفسِّر فعلياً، يعيِّن دينامو (mmap) منطقة منفصلة من الذاكرة يديرها بنفسه. جميع الكائنات المُخصَّصة ديناميكياً في شيفرة دينامو تُنشأ في هذه المنطقة من الذاكرة. يُحمى الوصول إلى هذه المنطقة لمنع التطبيق من إتلاف حالة دينامو عن طريق الخطأ أو بشكل متعمد.

---

### Translation Notes

- **Figures referenced:** Figure 2 (how Dynamo gains control over the application), Figure 1 (box A - interpreter)
- **Key terms introduced:** dynamo_exec, app-context, return-pc, crt0.o, _start, text segment, mmap, bailout condition
- **System details:** User-mode library, stack swapping, memory protection
- **Code elements:** dynamo_exec (function name), app-context (data structure), crt0.o (startup code), _start (entry point)
- **Special handling:**
  - Kept technical function names (dynamo_exec, dynamo_start, _start) in English as is standard practice
  - Preserved crt0.o as a file name
  - Used mmap in transliteration (عيِّن/mmap) to indicate the system call

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation

Key paragraph back-translated:
"Dynamo is provided as a dynamically linked library in user mode (shared library). The entry point to this library is the dynamo_exec function. When an application invokes dynamo_exec, the rest of the application code after returning from the dynamo_exec call will execute under Dynamo's control.

As shown in Figure 2, dynamo_exec first saves a snapshot of the application context (i.e., machine registers and stack environment) in an internal data structure called app-context. It then swaps the stack environment so that Dynamo's own code uses a custom runtime stack allocated separately for its use..."

Semantic match: ✓ Excellent
Technical accuracy: ✓ Excellent
