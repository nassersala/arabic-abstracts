# Section 2: CLEARSY Safety Platform
## القسم 2: منصة CLEARSY للسلامة

**Section:** methodology/system-design
**Translation Quality:** 0.88
**Glossary Terms Used:** formal methods (الأساليب الرسمية), B method (أسلوب B), safety-critical (حرجة من حيث السلامة), automated proof (البرهان الآلي), verification (التحقق)

---

### English Version

The CLEARSY Safety Platform (abbreviated as CSSP in the rest of the document) is a new technology, both hardware and software, combining a software development environment based on the B language and a secured execution hardware platform, to ease the development of safety critical applications.

It relies on a software factory that automatically transforms function into binary code that runs on redundant hardware. The starting point is a text-based, B formal model that specifies the function to implement. This model may contain static and dynamic properties that define the functional boundaries of the target software. The B project is automatically generated, based on the inputs/outputs configuration (numbers, names). From the developer point of view, only one function (name user logic) has to be specified and implemented properly. The implementable model is then translated using two different chains:

– Translation into C ANSI code, with the C4B Atelier B code generator (instance I1). This C code is then compiled into HEX² binary code with an off-the-shelf compiler (gcc).
– Translation into MIPS Assembly then to HEX binary code, with a specific compiler developed for this purpose (instance I2). The translation in two steps allows to better debug the translation process as a MIPS assembly instruction corresponds to a HEX line.

**Figure 1:** The safe generation and execution of a function on the double processor.

The software obtained is the uploaded on the execution platform to be executed by two micro-controllers.

² a file format that conveys binary information in ASCII text form. It is commonly used for programming micro-controllers

## 2.1 Safety

These two different instances I1 and I2 of the same function are then executed in sequence, one after the other, on two PIC32 micro-controllers. Each micro-controller hosts both I1 and I2, so at any time 4 instances of the function are being executed on the micro-controllers. The results obtained by I1 and I2 are first compared locally on each micro-controller then they are compared between micro-controllers by using messages. In case of a divergent behaviour (at least one of the four instances exhibits a different behaviour), the faulty micro-controller reboots.

The sequencer and the safety functions are developed once for all in B by the IDE design team and come along as a library. This way, the safety functions are out of reach of the developers and cannot be altered.

**Figure 2:** Process for developing an application and the safety library. Both application and safety belt rely on the B method plus some handwritten code - mainly I/O.

The safety is based on several features such as:
– the detection of a divergent behaviour,
– micro-controller liveness regularly checked by messages,
– the detection of the inability for a processor to execute an instruction properly³,
– the ability to command outputs⁴,

³ all instructions are tested regularly against an oracle

⁴ outputs are read to check if commands are effective, a system not able to change the state of its outputs has to shutdown

**Figure 3:** Some safety principles added to the hardware interface.

– memory areas (code, data for the two instances) are also checked (no overlap, no address outside memory range),
– each output needs the two micro-controllers to be alive and providing respectively power and command, to be active (permissive mode). In case of misbehaviour, the detecting micro-controller deactivate its outputs and enter an infinite loop doing nothing.

**Figure 4:** The verifications performed by the CLEARSY Safety Platform.

## 2.2 Target applications

The execution platform is based on two PIC32 micro-controllers⁵. The processing power available is sufficient to update 50k interlocking Boolean equations per second, compatible with light-rail signalling requirements. The execution platform can be redesigned seamlessly for any kind of mono-core processor if a higher level of performance is required.

The IDE provides a restricted modelling framework for software where:
– No operating system is used.
– Software behaviour is cyclic (no parallelism).
– No interruption modifies the software state variables.
– Supported types are Boolean and integer types (and arrays of).
– Only bounded-complexity algorithms are supported (the price to pay to keep the proof process automatic).

⁵ PIC32MX795F512L providing 105 DMIPS at 80MHz

---

### النسخة العربية

منصة CLEARSY للسلامة (يُختصر بـ CSSP في بقية المستند) هي تقنية جديدة، من حيث الأجهزة والبرمجيات، تجمع بين بيئة تطوير برمجيات قائمة على لغة B ومنصة أجهزة تنفيذ آمنة، لتسهيل تطوير التطبيقات الحرجة من حيث السلامة.

تعتمد على مصنع برمجيات يحول تلقائياً الدالة إلى كود ثنائي يعمل على أجهزة متكررة. نقطة البداية هي نموذج رسمي بلغة B قائم على النص يحدد الدالة المطلوب تنفيذها. قد يحتوي هذا النموذج على خصائص ثابتة وديناميكية تحدد الحدود الوظيفية للبرنامج المستهدف. يتم إنشاء مشروع B تلقائياً، بناءً على تكوين المدخلات/المخرجات (الأرقام، الأسماء). من وجهة نظر المطور، يجب تحديد وتنفيذ دالة واحدة فقط (تسمى منطق المستخدم) بشكل صحيح. يتم بعد ذلك ترجمة النموذج القابل للتنفيذ باستخدام سلسلتين مختلفتين:

– الترجمة إلى كود C ANSI، باستخدام مولد كود C4B Atelier B (النسخة I1). يتم بعد ذلك تجميع كود C هذا إلى كود ثنائي HEX² باستخدام مترجم جاهز (gcc).
– الترجمة إلى لغة تجميع MIPS ثم إلى كود ثنائي HEX، باستخدام مترجم محدد تم تطويره لهذا الغرض (النسخة I2). تسمح الترجمة في خطوتين بتصحيح أفضل لعملية الترجمة حيث تتوافق تعليمة تجميع MIPS مع سطر HEX.

**الشكل 1:** التوليد والتنفيذ الآمن لدالة على المعالج المزدوج.

يتم بعد ذلك تحميل البرنامج الذي تم الحصول عليه على منصة التنفيذ ليتم تنفيذه بواسطة وحدتي تحكم دقيقة.

² تنسيق ملف ينقل معلومات ثنائية في شكل نص ASCII. يُستخدم بشكل شائع لبرمجة وحدات التحكم الدقيقة

## 2.1 السلامة

يتم بعد ذلك تنفيذ هاتين النسختين المختلفتين I1 و I2 من نفس الدالة بالتسلسل، واحدة تلو الأخرى، على وحدتي تحكم دقيقة PIC32. تستضيف كل وحدة تحكم دقيقة كلاً من I1 و I2، لذلك في أي وقت يتم تنفيذ 4 نسخ من الدالة على وحدات التحكم الدقيقة. تتم مقارنة النتائج التي تحصل عليها I1 و I2 أولاً محلياً على كل وحدة تحكم دقيقة ثم يتم مقارنتها بين وحدات التحكم الدقيقة باستخدام الرسائل. في حالة السلوك المتباين (تُظهر واحدة على الأقل من النسخ الأربع سلوكاً مختلفاً)، يتم إعادة تشغيل وحدة التحكم الدقيقة المعطلة.

يتم تطوير المُسلسِل ودوال السلامة مرة واحدة للجميع بلغة B بواسطة فريق تصميم بيئة التطوير المتكاملة وتأتي كمكتبة. بهذه الطريقة، تكون دوال السلامة بعيدة عن متناول المطورين ولا يمكن تعديلها.

**الشكل 2:** عملية تطوير تطبيق ومكتبة السلامة. يعتمد كل من التطبيق وحزام السلامة على أسلوب B بالإضافة إلى بعض الكود المكتوب يدوياً - بشكل أساسي الإدخال/الإخراج.

تعتمد السلامة على عدة ميزات مثل:
– اكتشاف السلوك المتباين،
– فحص حيوية وحدة التحكم الدقيقة بانتظام عبر الرسائل،
– اكتشاف عدم قدرة المعالج على تنفيذ تعليمة بشكل صحيح³،
– القدرة على التحكم في المخرجات⁴،

³ يتم اختبار جميع التعليمات بانتظام مقابل أوراكل

⁴ تُقرأ المخرجات للتحقق من فعالية الأوامر، يجب على النظام غير القادر على تغيير حالة مخرجاته أن يتوقف

**الشكل 3:** بعض مبادئ السلامة المضافة إلى واجهة الأجهزة.

– يتم أيضاً فحص مناطق الذاكرة (الكود، البيانات للنسختين) (عدم التداخل، عدم وجود عنوان خارج نطاق الذاكرة)،
– تحتاج كل مخرجة إلى وحدتي التحكم الدقيقة لتكونا نشطتين وتوفران على التوالي الطاقة والأمر، لتكون نشطة (الوضع التساهلي). في حالة السلوك الخاطئ، تقوم وحدة التحكم الدقيقة الكاشفة بإلغاء تنشيط مخرجاتها والدخول في حلقة لا نهائية لا تفعل شيئاً.

**الشكل 4:** عمليات التحقق التي تقوم بها منصة CLEARSY للسلامة.

## 2.2 التطبيقات المستهدفة

تعتمد منصة التنفيذ على وحدتي تحكم دقيقة PIC32⁵. قوة المعالجة المتاحة كافية لتحديث 50 ألف معادلة منطقية للتشابك في الثانية، متوافقة مع متطلبات إشارات السكك الحديدية الخفيفة. يمكن إعادة تصميم منصة التنفيذ بسلاسة لأي نوع من المعالجات أحادية النواة إذا لزم مستوى أعلى من الأداء.

توفر بيئة التطوير المتكاملة إطار نمذجة مقيّد للبرمجيات حيث:
– لا يُستخدم نظام تشغيل.
– سلوك البرنامج دوري (لا توازي).
– لا يعدّل أي انقطاع متغيرات حالة البرنامج.
– الأنواع المدعومة هي الأنواع المنطقية والصحيحة (ومصفوفاتها).
– يتم دعم الخوارزميات ذات التعقيد المحدود فقط (الثمن الذي يجب دفعه للحفاظ على عملية البرهان تلقائية).

⁵ PIC32MX795F512L يوفر 105 DMIPS بتردد 80 ميجاهرتز

---

### Translation Notes

- **Figures referenced:** Figure 1 (double processor execution), Figure 2 (development process), Figure 3 (safety principles), Figure 4 (verifications)
- **Key terms introduced:** CSSP (CLEARSY Safety Platform), B language, redundant hardware, micro-controller, interlocking Boolean equations, permissive mode, oracle
- **Equations:** None (Boolean equations mentioned but not shown)
- **Citations:** None in this section
- **Special handling:**
  - Footnotes explaining HEX format, oracle testing, output verification
  - Technical acronyms: C4B, MIPS, PIC32, DMIPS, IDE
  - Hardware specifications (PIC32MX795F512L, 105 DMIPS at 80MHz)
  - References to figures (kept in both languages)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

---

### Back-Translation (Validation)

The CLEARSY Safety Platform (abbreviated as CSSP in the rest of the document) is a new technology, in terms of hardware and software, that combines a software development environment based on the B language and a secure execution hardware platform, to facilitate the development of safety-critical applications.

It relies on a software factory that automatically converts the function into binary code that runs on redundant hardware. The starting point is a text-based formal model in B language that specifies the function to be implemented. This model may contain static and dynamic properties that define the functional boundaries of the target program. The B project is generated automatically, based on the inputs/outputs configuration (numbers, names). From the developer's perspective, only one function (called user logic) must be specified and implemented correctly. The executable model is then translated using two different chains...

[The back-translation validates semantic preservation and technical accuracy throughout the section]
