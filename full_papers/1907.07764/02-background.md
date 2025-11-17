# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** transformational derivation, refinement, functional programming, higher-order functions, parallel, datatype, process, message passing, stream, vector

---

### English Version

HTCC adopts the transformational derivation and refinement methodology of Abdallah et. al [8], [25]. The adopted methodology refines functional specifications into parallel hardware implementations in Handel-C. Several case-studies for the methodology were carried out by Damaj et. al [9], [26]–[28], however the implementations did not include a compiler that automates the refinement procedure.

Figure 1 depicts the step-wise refinement procedure, where functional specifications are refined to hardware. The adopted methodology is systematic in the sense that it is carried out using the following step-by-step procedure:
• Specify the algorithm in a functional setting relying on higher-order functions as the main building constructs wherever necessary.
• Apply the predefined set of rules to create the corresponding CSP networks according to a chosen degree of parallelism.
• Write the equivalent Handel-C code and complete the hardware compilation.

The refinement steps are aided by different compilers and integrated development environments. HTCC automates the development process including the background run of existing FPGA vendor interfaces and Haskell, Handel-C, VHDL, Verilog, EDIF, and SystemC compilers.

The adopted methodology refines both datatypes and functions. Datatypes are refined to Items, Streams, and Vectors to create communicating entities based-on the message passing technique. The Item corresponds to a basic type, such as an Integer data type, and it is to be communicated on a single communicating channel. The Stream is a purely sequential method of communicating a list of values. The Vector is a refinement of a simple list of items that communicates the entire structure in parallel [9].

In addition, the methodology refines functions to communicating processes. The refinement comprises a library of standard processes, such as, Produce and Store that aid the communication of refined datatypes. The Produce process is used to produce values on the channels of a certain communication construct (Item, Stream, Vector, etc.). These values are to be received and manipulated by another processes. The process Store stores a communication construct in a simple or composite variable [9].

The methodology also supports a rich set of refined higher-order functions, such as, map, zip, zipwith, etc. The refinement of higher-order functions to processes could be done in stream or vector settings, or a combination of them. In Handel-C, datatypes are refined to structures (struct), while processes are refined to macro procedures [9]. Handel-C compiler generates the required hardware circuits that can be mapped onto FPGAs.

---

### النسخة العربية

يتبنى HTCC منهجية الاشتقاق التحويلي والتنقيح لـ Abdallah وآخرون [8]، [25]. تنقح المنهجية المعتمدة المواصفات الوظيفية إلى تطبيقات أجهزة متوازية في Handel-C. تم إجراء العديد من دراسات الحالة للمنهجية بواسطة Damaj وآخرون [9]، [26]–[28]، ومع ذلك لم تتضمن التطبيقات مترجماً يؤتمت إجراء التنقيح.

يصور الشكل 1 إجراء التنقيح التدريجي، حيث يتم تنقيح المواصفات الوظيفية إلى أجهزة. المنهجية المعتمدة منهجية بمعنى أنها تُنفذ باستخدام الإجراء التدريجي التالي:
• تحديد الخوارزمية في إطار وظيفي بالاعتماد على الدوال من الرتبة العليا كعناصر البناء الرئيسية حيثما كان ذلك ضرورياً.
• تطبيق مجموعة القواعد المحددة مسبقاً لإنشاء شبكات CSP المقابلة وفقاً لدرجة التوازي المختارة.
• كتابة كود Handel-C المكافئ وإكمال تجميع الأجهزة.

يتم دعم خطوات التنقيح بواسطة مترجمات مختلفة وبيئات تطوير متكاملة. يؤتمت HTCC عملية التطوير بما في ذلك التشغيل الخلفي لواجهات موردي FPGA الموجودة ومترجمات Haskell و Handel-C و VHDL و Verilog و EDIF و SystemC.

تنقح المنهجية المعتمدة كل من أنواع البيانات والدوال. يتم تنقيح أنواع البيانات إلى عناصر (Items)، وتدفقات (Streams)، ومتجهات (Vectors) لإنشاء كيانات متواصلة بناءً على تقنية تمرير الرسائل. يتوافق العنصر (Item) مع نوع أساسي، مثل نوع بيانات عدد صحيح، ويجب أن يتم توصيله على قناة اتصال واحدة. التدفق (Stream) هو طريقة تسلسلية بحتة للتواصل بقائمة من القيم. المتجه (Vector) هو تنقيح لقائمة بسيطة من العناصر التي تتواصل بالهيكل بأكمله بشكل متوازٍ [9].

بالإضافة إلى ذلك، تنقح المنهجية الدوال إلى عمليات متواصلة. يشتمل التنقيح على مكتبة من العمليات القياسية، مثل Produce و Store التي تساعد في التواصل بأنواع البيانات المنقحة. تُستخدم عملية Produce لإنتاج قيم على قنوات بنية اتصال معينة (عنصر، تدفق، متجه، إلخ). هذه القيم يجب أن يتم استقبالها ومعالجتها بواسطة عمليات أخرى. تخزن عملية Store بنية اتصال في متغير بسيط أو مركب [9].

تدعم المنهجية أيضاً مجموعة غنية من الدوال من الرتبة العليا المنقحة، مثل map و zip و zipwith وغيرها. يمكن إجراء تنقيح الدوال من الرتبة العليا إلى عمليات في إعدادات التدفق أو المتجهات، أو مزيج منها. في Handel-C، يتم تنقيح أنواع البيانات إلى هياكل (struct)، بينما يتم تنقيح العمليات إلى إجراءات ماكرو [9]. يولد مترجم Handel-C دوائر الأجهزة المطلوبة التي يمكن تعيينها على FPGAs.

---

### Translation Notes

- **Figures referenced:** Figure 1 - The transformational derivation and refinement methodology
- **Key terms introduced:** transformational derivation, refinement, Item, Stream, Vector, Produce, Store, message passing, CSP networks
- **Equations:** 0
- **Citations:** [8], [9], [25], [26], [27], [28] - Methodology references
- **Special handling:**
  - Technical terms Items, Streams, Vectors kept with Arabic explanation in parentheses
  - Process names Produce and Store kept in English (standard terminology)
  - CSP kept as acronym

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Check (Key Paragraph)

The adopted methodology refines both datatypes and functions. Datatypes are refined to Items, Streams, and Vectors to create communicating entities based on the message passing technique. The Item corresponds to a basic type, such as an Integer data type, and is to be communicated on a single communication channel. The Stream is a purely sequential method of communicating a list of values. The Vector is a refinement of a simple list of items that communicates the entire structure in parallel [9].

**Quality Assessment:** The back-translation accurately preserves the technical meaning and structure (0.87).
