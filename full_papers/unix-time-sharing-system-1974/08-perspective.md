# Section 8: Perspective
## القسم 8: منظور عام

**Section:** perspective
**Translation Quality:** 0.88
**Glossary Terms Used:** operating system, design philosophy, simplicity, elegance, file system, interactive

---

### English Version

Perhaps paradoxically, the success of UNIX is largely due to the fact that it was not designed to meet any predefined objectives. The first version was written when one of us (Thompson), dissatisfied with the available computer facilities, discovered a little-used PDP-7 and set out to create a more hospitable environment. This essentially personal effort was sufficiently successful to gain the interest of the remaining author and others, and later to justify the acquisition of the PDP-11/20, specifically to support a text editing and formatting system. The goals of generality and software flexibility were not achieved in spite of, but because of, the system's small size.

Then, and even more so now, the system is in a state of continual change. New system calls and system features are invented and installed and superseded. Indeed, the ease with which changes can be made in UNIX has been crucial to its development. Research and development cannot be performed with an operating system that never changes; on the other hand, gratuitous change is to be resisted. Ease of change must be tempered with patience.

The system provides a number of features seldom found even in larger operating systems. The file system is unified in the sense that file, device, and inter-process I/O are all treated in a similar manner. The file system also allows the user to mount his own private file systems. Because of the unified treatment of files, directories, and I/O devices, each user can construct his own file structures. The system has a high degree of software flexibility, and the Shell provides a higher level interface to the file system and its programs than is available in most systems. This flexibility is possible because the operating system is small, being only 8900 lines of assembly code for the system proper and about 1500 lines for the drivers of peripheral devices. This code could also be written in a higher level language. One of the authors (Thompson) has written a version of UNIX entirely in the language C [2], with only a slight code expansion.

The most important achievement of UNIX is to demonstrate that a powerful operating system for interactive use need not be expensive either in equipment or in human effort. It is hoped that the success of the system will lead others to consider the importance of interaction in the design of future operating systems.

---

### النسخة العربية

ربما بشكل متناقض، يعود نجاح يونكس إلى حد كبير إلى حقيقة أنه لم يُصمم لتلبية أي أهداف محددة مسبقاً. كُتبت النسخة الأولى عندما اكتشف أحدنا (طومسون)، غير راضٍ عن مرافق الحاسوب المتاحة، جهاز PDP-7 قليل الاستخدام وشرع في إنشاء بيئة أكثر ضيافة. كان هذا الجهد الشخصي أساساً ناجحاً بما فيه الكفاية لكسب اهتمام المؤلف المتبقي وآخرين، ولاحقاً لتبرير الحصول على PDP-11/20، خصيصاً لدعم نظام تحرير وتنسيق النصوص. لم تتحقق أهداف العمومية والمرونة البرمجية على الرغم من، بل بسبب صغر حجم النظام.

آنذاك، والآن أكثر من ذلك، يكون النظام في حالة تغيير مستمر. يتم اختراع وتثبيت واستبدال استدعاءات النظام الجديدة وميزات النظام. في الواقع، كانت السهولة التي يمكن بها إجراء تغييرات في يونكس حاسمة لتطويره. لا يمكن إجراء البحث والتطوير مع نظام تشغيل لا يتغير أبداً؛ من ناحية أخرى، يجب مقاومة التغيير غير المبرر. يجب أن تُمزج سهولة التغيير بالصبر.

يوفر النظام عدداً من الميزات نادراً ما توجد حتى في أنظمة التشغيل الأكبر. نظام الملفات موحد بمعنى أن الملف والجهاز والإدخال/الإخراج بين العمليات كلها تُعامل بطريقة مماثلة. يسمح نظام الملفات أيضاً للمستخدم بتركيب أنظمة ملفاته الخاصة. بسبب المعاملة الموحدة للملفات والدلائل وأجهزة الإدخال/الإخراج، يمكن لكل مستخدم بناء بنى ملفاته الخاصة. يتمتع النظام بدرجة عالية من المرونة البرمجية، وتوفر الصدفة واجهة مستوى أعلى لنظام الملفات وبرامجه مما هو متاح في معظم الأنظمة. هذه المرونة ممكنة لأن نظام التشغيل صغير، حيث يبلغ 8900 سطر فقط من شفرة التجميع للنظام نفسه وحوالي 1500 سطر لمحركات الأجهزة الطرفية. يمكن أيضاً كتابة هذه الشفرة بلغة أعلى مستوى. كتب أحد المؤلفين (طومسون) نسخة من يونكس بالكامل بلغة C [2]، مع توسع طفيف فقط في الشفرة.

أهم إنجاز ليونكس هو إثبات أن نظام تشغيل قوي للاستخدام التفاعلي لا يحتاج إلى أن يكون مكلفاً سواء من حيث المعدات أو الجهد البشري. يُأمل أن يؤدي نجاح النظام إلى أن يعتبر الآخرون أهمية التفاعل في تصميم أنظمة التشغيل المستقبلية.

---

### Translation Notes

- **Key terms used:**
  - predefined objectives (أهداف محددة مسبقاً)
  - hospitable environment (بيئة أكثر ضيافة)
  - generality (عمومية)
  - software flexibility (مرونة برمجية)
  - continual change (تغيير مستمر)
  - gratuitous change (تغيير غير مبرر)
  - unified treatment (معاملة موحدة)
  - assembly code (شفرة التجميع)
  - peripheral devices (أجهزة طرفية)
  - code expansion (توسع في الشفرة)
  - interactive use (استخدام تفاعلي)
- **Citations:** [2] - reference to C language paper
- **Statistics preserved:**
  - 8900 lines of assembly code
  - 1500 lines for device drivers
- **Special handling:**
  - Authors' names (Thompson) kept in English transliteration (طومسون)
  - Hardware names (PDP-7, PDP-11/20) kept as is
  - Language name "C" kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Validation

The back-translation confirms accurate preservation of:
- UNIX's organic development without predefined goals
- Emphasis on simplicity enabling flexibility
- Continuous evolution as a design principle
- Unified file system treatment
- Small code size (8900 + 1500 lines)
- C language implementation
- Core message: powerful interactive OS can be simple and inexpensive
- Hope for influence on future OS design
