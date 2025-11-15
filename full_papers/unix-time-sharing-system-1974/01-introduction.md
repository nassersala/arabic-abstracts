# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** operating system, time-sharing, interactive, file system, hierarchical, processes, compiler, implementation

---

### English Version

There have been three versions of UNIX. The earliest version (circa 1969-70) ran on the Digital Equipment Corporation PDP-7 and -9 computers. The second version ran on the unprotected PDP-11/20 computer. This paper describes only the PDP-11/40 and /45 [l] system since it is more modern and many of the differences between it and older UNIX systems result from redesign of features found to be deficient or lacking.

Since PDP-11 UNIX became operational in February 1971, about 40 installations have been put into service; they are generally smaller than the system described here. Most of them are engaged in applications such as the preparation and formatting of patent applications and other textual material, the collection and processing of trouble data from various switching machines within the Bell System, and recording and checking telephone service orders. Our own installation is used mainly for research in operating systems, languages, computer networks, and other topics in computer science, and also for document preparation.

Perhaps the most important achievement of UNIX is to demonstrate that a powerful operating system for interactive use need not be expensive either in equipment or in human effort: UNIX can run on hardware costing as little as $40,000, and less than two man years were spent on the main system software. Yet UNIX contains a number of features seldom offered even in much larger systems. It is hoped, however, the users of UNIX will find that the most important characteristics of the system are its simplicity, elegance, and ease of use.

Besides the system proper, the major programs available under UNIX are: an assembler, text editor, linking loader, symbolic debugger, compiler for a language resembling BCPL [2] with types and structures (C), interpreter for a dialect of BASIC, text formatting program, Fortran compiler, Snobol interpreter, top-down compiler-compiler (TMG) [3], bottom-up compiler-compiler (YACC), form letter generator, macro processor (M6) [4], and permuted index program.

There is also a host of maintenance, utility, recreation, and novelty programs. All of these programs were written locally. It is worth noting that the system is totally self-supporting. All UNIX software is maintained under UNIX; likewise, UNIX documents are generated and formatted by the UNIX editor and text formatting program.

---

### النسخة العربية

كان هناك ثلاث إصدارات من يونكس. أقدم إصدار (حوالي 1969-1970) عمل على حاسوبي ديجيتال إيكويبمنت كوربوريشن PDP-7 و PDP-9. الإصدار الثاني عمل على حاسوب PDP-11/20 غير المحمي. تصف هذه الورقة فقط نظام PDP-11/40 و /45 [1] لأنه أكثر حداثة والعديد من الاختلافات بينه وبين أنظمة يونكس الأقدم ناتجة عن إعادة تصميم ميزات تبين أنها ناقصة أو غير كافية.

منذ أن أصبح نظام PDP-11 يونكس تشغيلياً في فبراير 1971، تم وضع حوالي 40 تثبيتاً في الخدمة؛ وهي بشكل عام أصغر من النظام الموصوف هنا. معظمها مشغول في تطبيقات مثل إعداد وتنسيق طلبات براءات الاختراع والمواد النصية الأخرى، وجمع ومعالجة بيانات الأعطال من مختلف آلات التبديل داخل نظام بِل، وتسجيل والتحقق من أوامر خدمة الهاتف. يُستخدم تثبيتنا الخاص بشكل أساسي للبحث في أنظمة التشغيل واللغات وشبكات الحاسوب وموضوعات أخرى في علوم الحاسوب، وأيضاً لإعداد المستندات.

ربما يكون أهم إنجاز ليونكس هو إثبات أن نظام تشغيل قوي للاستخدام التفاعلي لا يحتاج إلى أن يكون مكلفاً سواء من حيث المعدات أو الجهد البشري: يمكن ليونكس العمل على أجهزة لا تتكلف أكثر من 40,000 دولار، وأقل من سنتين رجل أُنفقت على برمجيات النظام الرئيسية. ومع ذلك، يحتوي يونكس على عدد من الميزات نادراً ما تُقدم حتى في الأنظمة الأكبر بكثير. يُأمل، مع ذلك، أن يجد مستخدمو يونكس أن أهم خصائص النظام هي بساطته وأناقته وسهولة استخدامه.

إلى جانب النظام نفسه، البرامج الرئيسية المتاحة تحت يونكس هي: مُجمّع، محرر نصوص، محمل ربط، مُنقح رمزي، مترجم للغة تشبه BCPL [2] مع أنواع وبنى (C)، مفسر للهجة من BASIC، برنامج تنسيق نصوص، مترجم فورتران، مفسر سنوبول، مترجم-مترجم من أعلى لأسفل (TMG) [3]، مترجم-مترجم من أسفل لأعلى (YACC)، مولد رسائل نموذجية، معالج ماكرو (M6) [4]، وبرنامج فهرس مُبدّل.

هناك أيضاً مجموعة من برامج الصيانة والخدمات والترفيه والبرامج الطريفة. كُتبت كل هذه البرامج محلياً. تجدر الإشارة إلى أن النظام ذاتي الدعم تماماً. تتم صيانة جميع برمجيات يونكس تحت يونكس؛ وبالمثل، يتم إنشاء مستندات يونكس وتنسيقها بواسطة محرر يونكس وبرنامج تنسيق النصوص.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - time-sharing (المشاركة الزمنية)
  - interactive use (الاستخدام التفاعلي)
  - man years (سنتين رجل) - standard software engineering term
  - assembler (مُجمّع)
  - compiler (مترجم)
  - interpreter (مفسر)
  - debugger (مُنقح)
  - self-supporting (ذاتي الدعم)
- **Equations:** None
- **Citations:** [1], [2], [3], [4]
- **Special handling:**
  - Programming language names (BCPL, C, BASIC, Fortran, Snobol, TMG, YACC, M6) kept in English
  - Hardware names (PDP-7, PDP-9, PDP-11/20, PDP-11/40, PDP-11/45) kept in English
  - Bell System translated as "نظام بِل" (proper noun)
  - Cost figure ($40,000) preserved

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation

There were three versions of UNIX. The oldest version (around 1969-1970) ran on Digital Equipment Corporation PDP-7 and PDP-9 computers. The second version ran on the unprotected PDP-11/20 computer. This paper describes only the PDP-11/40 and /45 [1] system because it is more modern and many of the differences between it and older UNIX systems result from redesigning features that proved to be deficient or insufficient.

Since the PDP-11 UNIX system became operational in February 1971, about 40 installations have been put into service; they are generally smaller than the system described here. Most of them are engaged in applications such as preparing and formatting patent applications and other textual materials, collecting and processing failure data from various switching machines within the Bell system, and recording and verifying telephone service orders. Our own installation is used primarily for research in operating systems, languages, computer networks, and other topics in computer science, and also for document preparation.

Perhaps the most important achievement of UNIX is demonstrating that a powerful operating system for interactive use does not need to be expensive either in terms of equipment or human effort: UNIX can run on hardware costing no more than $40,000, and less than two man-years were spent on the main system software. Nevertheless, UNIX contains a number of features rarely offered even in much larger systems. It is hoped, however, that UNIX users will find that the most important characteristics of the system are its simplicity, elegance, and ease of use.

Besides the system itself, the main programs available under UNIX are: an assembler, text editor, linking loader, symbolic debugger, compiler for a language resembling BCPL [2] with types and structures (C), interpreter for a BASIC dialect, text formatting program, Fortran compiler, Snobol interpreter, top-down compiler-compiler (TMG) [3], bottom-up compiler-compiler (YACC), form letter generator, macro processor (M6) [4], and permuted index program.

There is also a set of maintenance, utility, recreation, and novelty programs. All these programs were written locally. It is worth noting that the system is completely self-supporting. All UNIX software is maintained under UNIX; similarly, UNIX documents are generated and formatted by the UNIX editor and text formatting program.
