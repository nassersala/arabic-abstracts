# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** FPGA, reconfigurable computing, high-level synthesis, hardware/software co-design, functional programming, compiler, hardware description language

---

### English Version

FPGAs are famous and widely used reconfigurable computing (RC) systems. FPGAs have become very popular in research and industrial applications in different fields, such as, security, signal processing etc. FPGAs evolved from being limited in functionality and speed to become high-performance processors. Example FPGAs include Stratix from Altera and Virtex from Xilinx [1], [2]. The flexibility of FPGAs, that are sometimes described as seas-of-gates, enable the development of software paradigms to rapidly reconfigure hardware almost instantly.

Recently, there has been considerable focus on the development of high-level synthesis (HLS) and rapid prototyping hardware/software co-design tools. The targets of co-design tools are high design productivity, simplicity, reduced time-to-prototype, correctness, to name a few. Co-design tools include converting algorithmic behaviors into digital circuits that can map onto FPGAs. High-level co-design tools are currently beyond behavioral VHDL and the other standard tools. The area witnessed the emergence of programming languages and tools such as Handel-C [3], SystemC [4], Matlab HDL Coder, LabVIEW, etc. All the modern co-design tools enable the integration and partitioning of computations into communicating hardware and software subsystems.

Handel-C is a high-level language with hardware output. Handel-C is based on ANSI C; it is extended to the theory of communication sequential processes (CSP) and the concurrent programming language (OCCAM) [5]. Moreover, Handel-C has the ability to provide both parallel and sequential implementations. Handel-C can target different FPGA types. Recent research effort has been on automating hardware generation to target Handel-C and hardware in general starting from functional specifications, such as, Haskell [6]–[9].

Haskell is a purely functional programming language that utilizes functions to construct programs. Utilizing Haskell functions is presumed to have no side effects, as the evaluation order of the functions is independent [10]. Modern functional languages are characterized by being strongly typed, concise, clear, lazy, and easy to insure correctness. With no doubt, developing hardware circuits based on the functional programming paradigm is a promising and modern topic under investigation [11]–[13]. Much research effort has been done to benefit from the advantages of functional programming languages in hardware design including Lava [14], Hawk [15], [16], Hydra [17], HML [18], MHDL [19], DDD system [20], SAFL [21], MuFP [22], Ruby [23], and Form [24].

HTCC compiles a subset of Haskell to Handel-C, in addition to automatically generating VHDL, Verilog, EDIF, and SystemC. The design of HTCC compiler includes lexical, syntax and semantic analyzers. The compiler is generated using ANTLR based-on a subset of Haskell grammar. HTCC Integrated Development Environment (IDE) produces a variety of analysis and schematic files. HTCC successfully connects to external tools, such as, DK Design Suite, Altera Quartus, and ModelSim. The developed compiler targets several FPGA types, and Altera DE2-70 and DE4 FPGA boards. The targeted area of application is cryptography, namely, the XTEA cipher.

The paper is organized so that Section II presents the rapid prototyping methodology adopted by HTCC. Section III details the HTCC construction including the compiler and IDE designs. The compiler implementation is presented in Section IV. Sections V and VI present the compilation approach of first-class and higher-order functions and a case-study from cryptography. A thorough analysis and evaluation is presented in Section VII. Section VIII concludes the paper and sets the ground for future works.

---

### النسخة العربية

مصفوفات البوابات القابلة للبرمجة (FPGAs) هي أنظمة حوسبة قابلة لإعادة التكوين (RC) مشهورة ومستخدمة على نطاق واسع. أصبحت FPGAs شائعة جداً في البحوث والتطبيقات الصناعية في مجالات مختلفة، مثل الأمن ومعالجة الإشارات وغيرها. تطورت FPGAs من كونها محدودة في الوظائف والسرعة لتصبح معالجات عالية الأداء. من الأمثلة على FPGAs Stratix من Altera و Virtex من Xilinx [1]، [2]. تتيح مرونة FPGAs، التي تُوصف أحياناً بأنها بحار من البوابات، تطوير نماذج برمجية لإعادة تكوين الأجهزة بسرعة وبشكل شبه فوري.

في الآونة الأخيرة، كان هناك تركيز كبير على تطوير أدوات التوليف عالي المستوى (HLS) والنماذج الأولية السريعة لأدوات التصميم المشترك للأجهزة/البرمجيات. أهداف أدوات التصميم المشترك هي إنتاجية تصميم عالية، وبساطة، وتقليل الوقت للنموذج الأولي، والصحة، على سبيل المثال لا الحصر. تتضمن أدوات التصميم المشترك تحويل السلوكيات الخوارزمية إلى دوائر رقمية يمكن تعيينها على FPGAs. أدوات التصميم المشترك عالية المستوى حالياً تتجاوز VHDL السلوكية والأدوات القياسية الأخرى. شهدت المنطقة ظهور لغات برمجة وأدوات مثل Handel-C [3]، وSystemC [4]، وMatlab HDL Coder، وLabVIEW، وغيرها. جميع أدوات التصميم المشترك الحديثة تمكن من دمج وتقسيم الحسابات إلى أنظمة فرعية متواصلة للأجهزة والبرمجيات.

Handel-C هي لغة عالية المستوى مع إخراج أجهزة. تستند Handel-C إلى ANSI C؛ وهي ممتدة لنظرية العمليات التسلسلية المتواصلة (CSP) ولغة البرمجة المتزامنة (OCCAM) [5]. علاوة على ذلك، لدى Handel-C القدرة على توفير تطبيقات متوازية وتسلسلية على حد سواء. يمكن لـ Handel-C استهداف أنواع مختلفة من FPGA. كانت جهود البحث الأخيرة على أتمتة توليد الأجهزة لاستهداف Handel-C والأجهزة بشكل عام انطلاقاً من المواصفات الوظيفية، مثل Haskell [6]–[9].

Haskell هي لغة برمجة وظيفية خالصة تستخدم الدوال لبناء البرامج. يُفترض أن استخدام دوال Haskell ليس له آثار جانبية، حيث أن ترتيب تقييم الدوال مستقل [10]. تتميز اللغات الوظيفية الحديثة بأنها مكتوبة بقوة، وموجزة، وواضحة، وكسولة، وسهلة لضمان الصحة. بلا شك، تطوير دوائر الأجهزة بناءً على نموذج البرمجة الوظيفية هو موضوع واعد وحديث قيد البحث [11]–[13]. تم بذل الكثير من جهود البحث للاستفادة من مزايا لغات البرمجة الوظيفية في تصميم الأجهزة بما في ذلك Lava [14]، وHawk [15]، [16]، وHydra [17]، وHML [18]، وMHDL [19]، ونظام DDD [20]، وSAFL [21]، وMuFP [22]، وRuby [23]، وForm [24].

يقوم HTCC بتجميع مجموعة فرعية من Haskell إلى Handel-C، بالإضافة إلى التوليد التلقائي لـ VHDL و Verilog و EDIF و SystemC. يتضمن تصميم مترجم HTCC محللات معجمية ونحوية ودلالية. يتم إنشاء المترجم باستخدام ANTLR بناءً على مجموعة فرعية من قواعد Haskell. تنتج بيئة التطوير المتكاملة (IDE) لـ HTCC مجموعة متنوعة من ملفات التحليل والمخططات. يتصل HTCC بنجاح بأدوات خارجية، مثل DK Design Suite و Altera Quartus و ModelSim. يستهدف المترجم المطور عدة أنواع من FPGA، ولوحات FPGA من Altera DE2-70 و DE4. مجال التطبيق المستهدف هو التشفير، وتحديداً شيفرة XTEA.

الورقة منظمة بحيث يقدم القسم الثاني منهجية النماذج الأولية السريعة المعتمدة من HTCC. يفصل القسم الثالث بناء HTCC بما في ذلك تصميمات المترجم وبيئة التطوير المتكاملة. يتم تقديم تنفيذ المترجم في القسم الرابع. يعرض القسمان الخامس والسادس نهج التجميع للدوال من الدرجة الأولى والرتبة العليا ودراسة حالة من التشفير. يتم تقديم تحليل وتقييم شامل في القسم السابع. يختتم القسم الثامن الورقة ويضع الأساس للأعمال المستقبلية.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** FPGAs, reconfigurable computing, HLS, co-design, CSP, OCCAM, Haskell, Handel-C, ANTLR, XTEA
- **Equations:** 0
- **Citations:** [1]-[24] - References to FPGA vendors, languages, and related work
- **Special handling:**
  - Technical acronyms kept in English (FPGA, HLS, CSP, VHDL, EDIF, etc.)
  - Language names kept in English (Haskell, Handel-C, SystemC, etc.)
  - Tool names kept in English (ANTLR, ModelSim, Quartus, etc.)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Check (First Paragraph)

FPGAs are famous and widely used reconfigurable computing systems. FPGAs have become very popular in research and industrial applications in different fields, such as security and signal processing. FPGAs evolved from being limited in functionality and speed to become high-performance processors. Examples of FPGAs include Stratix from Altera and Virtex from Xilinx [1], [2]. The flexibility of FPGAs, sometimes described as seas of gates, enables the development of software paradigms to rapidly reconfigure hardware almost instantaneously.

**Quality Assessment:** The back-translation preserves the semantic meaning with high accuracy (0.88).
