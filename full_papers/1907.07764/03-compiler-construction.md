# Section 3: Compiler Construction
## القسم 3: بناء المترجم

**Section:** compiler-construction
**Translation Quality:** 0.88
**Glossary Terms Used:** compiler, lexical analyzer, syntax analyzer, semantic analysis, parse tree, ANTLR, IDE, integrated development environment

---

### English Version

HTCC is a compiler that automates the presented refinement methodology. The presented version of HTCC Integrated Development Environment (IDE) supports the following:
• Compiles a subset of Haskell to Handel-C
• Automatically connects to the DK Design Suite from Mentor Graphics to run the Handel-C Compiler; it verifies, generates, and analyzes the corresponding VHDL, Verilog, EDIF, or SystemC code
• Automatically connects to Glasgow Haskell Compiler (GHC) to run and test the Haskell code
• Automatically connects to Altera Quartus II to run, test, analyze hardware designs; place and route; produce bit files; and target specific FPGAs and FPGA boards.
• Provides an easy-to-use, rich, and modern development environment

## A. Compiler Design using ANTLR

HTCC is developed using the compiler-compiler tool ANTLR. ANTLR provides an easy-to-use compiler construction structure; ANTLR is efficient, reliable, and effective [26]. ANTLR uses an adaptive parsing technique that provides runtime grammar analysis [29]. Moreover, ANTLR uses the Extended BackusNaur Form (EBNF). The efficiency and effectiveness of utilizing ANTLR is primarily due to its ability to support direct left-recursion, side-effecting actions (mutators) and predictions from the corresponding grammar [30].

Figure 2 demonstrates the state machine diagram of HTCC compilation procedure. The Lexical Analyzer analyzes the input Haskell code by producing a numbered list of lexemes. In addition, the Lexical Analyzer divides the code based on the provided grammar to prepare it for the syntax analysis. The Lexical Analyzer removes all white space between tokens and ignores any input with comment symbol "–".

The syntax analyzer is also generated using ANTLR, where a new parse tree is constructed every compilation. ANTLR provides the required Java library to construct parse trees and to walk through them starting on the leftmost side. During the walk-through, the program being compiled is checked for any errors based-on the provided grammar to ANTLR.

The third stage of HTCC compiler is the semantic analysis, where all types of all functions are checked and stored in a table for further processing. Semantic Analysis checks the types of inputs and outputs of each function. The semantic analyzer walks through the parse tree nodes using ANTLR's tree walker. If any datatype is found to be not supported or mismatched, HTCC terminates the compilation processes and reports the error.

After a successful semantic analysis check, HTCC continues to the intermediate code generation and then to the final code generation. In the intermediate stage, all input and output interface buses and macros are generated. Then, the number of connections among macros is determined and passed to the final generation stage. During the final compilation stage, both Handel-C bus interfaces and Handel-C main method are generated. Moreover, the connections among all macros are generated. The current version of HTCC does not include an optimization stage.

Figure 3 depicts the correspondence used to generate Handel-C macros from Haskell functions. An example Haskell function is as follows:

```haskell
add3 :: Int → Int
add3 x = x + 3
```

The add3 function has one input and one output, where both are of type integer. The corresponding Handel-C macro for add3 is as follows:

```c
macro proc add3 (itemIn, itemOut){
typeof itemIn.message x;
itemIn.channel ? x;
itemOut.channel ! x+3;
}
```

It is very important to notice that add3 function can be utilized for list processing. The generation correspondence is shown in Figure 4.

```haskell
vector add3 :: [Int] → [Int]
vector add3 x = map(add3) x
```

The corresponding Handel-C code includes a version of add3 based on items; the generic implementation of the parallel version of the higher-order function map (VMAP); the implementation of function vector add3 that invokes VMAP macro; and a main function that calls vector add3 with its inputs, outputs, and the number of elements in each vector. The parallel instances of add3 are replicated using the par operator in Handel-C. The generated code is as follows:

```c
macro proc add3 (itemIn, itemOut){
typeof itemIn.message x;
itemIn.channel ? x;
itemOut.channel ! (x+3);}

macro proc VMAP(vectorIn,vectorOut,n,F){
typeof(n) c;
par(c=0;c<n;c++){
F(vectorIn.elements[c],
vectorOut.elements[c]);}}

macro proc vector_add3 (vectorIn,vectorOut,n){
VMAP(vectorIn,vectorOut,n,add3);
}

void main (){
..
vector_add3(vector0,vector1,5);
..
}
```

## B. IDE Design

The technique used in the development of the IDE separates the programming concern in structuring the code in different Jar files. HTCC IDE adopts the iterative and incremental design model (IIDM) [31]. In the IIDM, each component of the IDE is developed separately as a standalone project which allows it to be integrated into multiple projects. The IDE is implemented using Java under Netbeans [32]. The code editor is implemented using RSyntaxTextArea Java framework. The IDE theme is implemented using JTattoo Java framework. Figure 5 demonstrates the use-case diagram of HTCC IDE. The proposed IDE supports the following:
• Editing and storing project files
• Highlighting and automatic code completion
• File navigation, and allows to open multiple files simultaneously
• Running Haskell code under GHC
• Compiling Haskell code to Handel-C code. Accordingly simulating Handel-C code and generating VHDL, EDIF, Verilog, and SystemC implementations.
• Compiling the generated HDL files using Altera Quartus. Accordingly, producing analysis and FPGA mapping files.

The IDE connects HTCC Compiler to external tools, such as, DK Design Suite to simulate and generate VHDL, Verilog, EDIF, and SystemC files. In addition, the IDE connects the compiler to Altera Quartus using the TCL commands to synthesize and generate timing analyses, pin assignments for FPGA boards, and generate bit files to program the targeted FPGAs. GHC is also connected to the IDE to execute and verify Haskell functions. Figure 6 shows a snapshot of the HTCC IDE.

---

### النسخة العربية

HTCC هو مترجم يؤتمت منهجية التنقيح المقدمة. تدعم النسخة المقدمة من بيئة التطوير المتكاملة (IDE) لـ HTCC ما يلي:
• تجميع مجموعة فرعية من Haskell إلى Handel-C
• الاتصال تلقائياً بـ DK Design Suite من Mentor Graphics لتشغيل مترجم Handel-C؛ حيث يتحقق، ويولد، ويحلل كود VHDL أو Verilog أو EDIF أو SystemC المقابل
• الاتصال تلقائياً بمترجم Glasgow Haskell (GHC) لتشغيل واختبار كود Haskell
• الاتصال تلقائياً بـ Altera Quartus II لتشغيل واختبار وتحليل تصميمات الأجهزة؛ والوضع والتوجيه؛ وإنتاج ملفات البت؛ واستهداف FPGAs ولوحات FPGA محددة.
• توفير بيئة تطوير سهلة الاستخدام وغنية وحديثة

## أ. تصميم المترجم باستخدام ANTLR

تم تطوير HTCC باستخدام أداة مترجم المترجمات ANTLR. توفر ANTLR هيكل بناء مترجم سهل الاستخدام؛ ANTLR فعالة وموثوقة وفعالة [26]. تستخدم ANTLR تقنية تحليل تكيفية توفر تحليل قواعد في وقت التشغيل [29]. علاوة على ذلك، تستخدم ANTLR الشكل الموسع لباكوس-ناور (EBNF). ترجع كفاءة وفعالية استخدام ANTLR بشكل أساسي إلى قدرتها على دعم التكرار الأيسر المباشر، والإجراءات ذات الآثار الجانبية (المغيرات)، والتوقعات من القواعد المقابلة [30].

يوضح الشكل 2 مخطط آلة الحالة لإجراء تجميع HTCC. يحلل المحلل المعجمي كود Haskell المدخل بإنتاج قائمة مرقمة من الرموز المعجمية. بالإضافة إلى ذلك، يقسم المحلل المعجمي الكود بناءً على القواعد المقدمة لتحضيره للتحليل النحوي. يزيل المحلل المعجمي جميع المسافات البيضاء بين الرموز ويتجاهل أي إدخال برمز تعليق "–".

يتم أيضاً إنشاء المحلل النحوي باستخدام ANTLR، حيث يتم بناء شجرة تحليل جديدة في كل تجميع. توفر ANTLR مكتبة Java المطلوبة لبناء أشجار التحليل والسير عبرها بدءاً من الجانب الأيسر. أثناء المرور عبر الشجرة، يتم فحص البرنامج الذي يتم تجميعه للبحث عن أي أخطاء بناءً على القواعد المقدمة لـ ANTLR.

المرحلة الثالثة من مترجم HTCC هي التحليل الدلالي، حيث يتم فحص جميع أنواع جميع الدوال وتخزينها في جدول لمزيد من المعالجة. يفحص التحليل الدلالي أنواع المدخلات والمخرجات لكل دالة. يسير المحلل الدلالي عبر عقد شجرة التحليل باستخدام مستكشف الشجرة في ANTLR. إذا تم العثور على أي نوع بيانات غير مدعوم أو غير متطابق، ينهي HTCC عمليات التجميع ويبلغ عن الخطأ.

بعد فحص تحليل دلالي ناجح، يستمر HTCC في توليد الكود الوسيط ثم إلى توليد الكود النهائي. في المرحلة الوسيطة، يتم إنشاء جميع ناقلات واجهة الإدخال والإخراج والماكروهات. بعد ذلك، يتم تحديد عدد الاتصالات بين الماكروهات وتمريرها إلى مرحلة التوليد النهائية. أثناء مرحلة التجميع النهائية، يتم إنشاء كل من واجهات ناقل Handel-C ودالة main في Handel-C. علاوة على ذلك، يتم إنشاء الاتصالات بين جميع الماكروهات. النسخة الحالية من HTCC لا تتضمن مرحلة تحسين.

يصور الشكل 3 المراسلة المستخدمة لتوليد ماكروهات Handel-C من دوال Haskell. مثال على دالة Haskell كما يلي:

```haskell
add3 :: Int → Int
add3 x = x + 3
```

دالة add3 لها مدخل واحد ومخرج واحد، حيث كلاهما من نوع عدد صحيح. ماكرو Handel-C المقابل لـ add3 كما يلي:

```c
macro proc add3 (itemIn, itemOut){
typeof itemIn.message x;
itemIn.channel ? x;
itemOut.channel ! x+3;
}
```

من المهم جداً ملاحظة أنه يمكن استخدام دالة add3 لمعالجة القوائم. يتم عرض مراسلة التوليد في الشكل 4.

```haskell
vector add3 :: [Int] → [Int]
vector add3 x = map(add3) x
```

يتضمن كود Handel-C المقابل نسخة من add3 بناءً على العناصر؛ التطبيق العام للنسخة المتوازية من الدالة من الرتبة العليا map (VMAP)؛ تطبيق دالة vector add3 الذي يستدعي ماكرو VMAP؛ ودالة main التي تستدعي vector add3 مع مدخلاتها ومخرجاتها وعدد العناصر في كل متجه. يتم تكرار المثيلات المتوازية لـ add3 باستخدام مشغل par في Handel-C. الكود المولد كما يلي:

```c
macro proc add3 (itemIn, itemOut){
typeof itemIn.message x;
itemIn.channel ? x;
itemOut.channel ! (x+3);}

macro proc VMAP(vectorIn,vectorOut,n,F){
typeof(n) c;
par(c=0;c<n;c++){
F(vectorIn.elements[c],
vectorOut.elements[c]);}}

macro proc vector_add3 (vectorIn,vectorOut,n){
VMAP(vectorIn,vectorOut,n,add3);
}

void main (){
..
vector_add3(vector0,vector1,5);
..
}
```

## ب. تصميم بيئة التطوير المتكاملة

التقنية المستخدمة في تطوير بيئة التطوير المتكاملة تفصل شواغل البرمجة في هيكلة الكود في ملفات Jar مختلفة. تتبنى بيئة التطوير المتكاملة لـ HTCC نموذج التصميم التكراري والتدريجي (IIDM) [31]. في IIDM، يتم تطوير كل مكون من مكونات بيئة التطوير المتكاملة بشكل منفصل كمشروع مستقل مما يسمح بدمجه في مشاريع متعددة. يتم تنفيذ بيئة التطوير المتكاملة باستخدام Java تحت Netbeans [32]. يتم تنفيذ محرر الكود باستخدام إطار عمل Java RSyntaxTextArea. يتم تنفيذ مظهر بيئة التطوير المتكاملة باستخدام إطار عمل Java JTattoo. يوضح الشكل 5 مخطط حالة الاستخدام لبيئة التطوير المتكاملة HTCC. تدعم بيئة التطوير المتكاملة المقترحة ما يلي:
• تحرير وتخزين ملفات المشروع
• التمييز والإكمال التلقائي للكود
• التنقل بين الملفات، وتسمح بفتح ملفات متعددة في وقت واحد
• تشغيل كود Haskell تحت GHC
• تجميع كود Haskell إلى كود Handel-C. وفقاً لذلك محاكاة كود Handel-C وتوليد تطبيقات VHDL و EDIF و Verilog و SystemC.
• تجميع ملفات HDL المولدة باستخدام Altera Quartus. وفقاً لذلك، إنتاج ملفات التحليل وتعيين FPGA.

تربط بيئة التطوير المتكاملة مترجم HTCC بأدوات خارجية، مثل DK Design Suite لمحاكاة وتوليد ملفات VHDL و Verilog و EDIF و SystemC. بالإضافة إلى ذلك، تربط بيئة التطوير المتكاملة المترجم بـ Altera Quartus باستخدام أوامر TCL للتوليف وإنشاء تحليلات التوقيت، وتعيينات الدبابيس للوحات FPGA، وتوليد ملفات البت لبرمجة FPGAs المستهدفة. يتصل GHC أيضاً ببيئة التطوير المتكاملة لتنفيذ والتحقق من دوال Haskell. يوضح الشكل 6 لقطة شاشة من بيئة التطوير المتكاملة HTCC.

---

### Translation Notes

- **Figures referenced:** Figure 2 (HTCC compiler state machine), Figure 3 (Code generation of items), Figure 4 (Code generation of parallel list processing), Figure 5 (Use-Case diagram), Figure 6 (HTCC IDE)
- **Key terms introduced:** ANTLR, EBNF, lexical analyzer, syntax analyzer, semantic analysis, parse tree, tree walker, intermediate code, VMAP, IIDM
- **Equations:** 0
- **Citations:** [26], [29], [30], [31], [32]
- **Special handling:**
  - Code examples kept in English (Haskell and Handel-C)
  - Tool names kept in English (ANTLR, GHC, Quartus, Netbeans, etc.)
  - Framework names kept in English (RSyntaxTextArea, JTattoo)
  - Technical operators (?, !, par) kept in code

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Check (Key Technical Paragraph)

The third stage of the HTCC compiler is semantic analysis, where all types of all functions are checked and stored in a table for further processing. Semantic Analysis checks the types of inputs and outputs of each function. The semantic analyzer walks through parse tree nodes using ANTLR's tree walker. If any datatype is found to be unsupported or mismatched, HTCC terminates the compilation processes and reports the error.

**Quality Assessment:** The back-translation preserves the technical details accurately (0.88).
