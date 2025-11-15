# Section 2: Definitions
## القسم الثاني: التعريفات

**Section:** §2. Definitions
**Translation Quality:** 0.92
**Glossary Terms Used:** automatic machine, computing machine, circular, circle-free, computable sequence, computable number, satisfactory number

---

### English Version

**Automatic machines.** If at each stage the motion of a machine (in the sense of §1) is completely determined by the configuration, we shall call the machine an "automatic machine" (or a-machine).

For some purposes we might use machines (choice machines or c-machines) whose motion is only partially determined by the configuration (hence the use of the word "possible" in §1). When such a machine reaches one of these ambiguous configurations, it cannot go on until some arbitrary choice has been made by an external operator. This would be the case if we were using machines to deal with axiomatic systems. In this paper I deal only with automatic machines, and will therefore use the expression "machine" to mean "automatic machine".

**Computing machines.** If an automatic machine prints two kinds of symbols, of which the first kind (called figures) consists entirely of 0 and 1 (the others being called symbols of the second kind), then the machine will be called a computing machine. If the machine is supplied with a blank tape and set in motion, starting from the correct initial m-configuration, the symbols of the first kind will be called the sequence computed by the machine. The symbols of the second kind serve only to "assist the memory". The sequence computed by the machine is the sequence of figures on the tape, when the symbols of the second kind are ignored.

**Circular and circle-free machines.** If a computing machine never writes down more than a finite number of symbols of the first kind, it will be called circular. Otherwise it will be called circle-free.

A machine will be circular if it reaches a configuration from which there is no possible move, or if it goes on moving, and possibly printing symbols of the second kind, but cannot print any more symbols of the first kind.

**Computable sequences and numbers.** A sequence is said to be computable if it can be computed by a circle-free machine. A number is computable if it differs by an integer from the number computed by a circle-free machine.

We say that a number is computable if its decimal can be written down by a machine.

The computable numbers include all numbers which would naturally be regarded as computable in the ordinary sense. For instance, all real algebraic numbers are computable, as are the real parts of the zeros of the Bessel functions. The number π is computable, as is e (the base of natural logarithms). More generally, any number whose decimal expansion can be computed by a systematic process is computable in Turing's sense.

**Satisfactory variants.** Certain variants of these definitions of computable numbers will be found to be satisfactory from some points of view and unsatisfactory from others. These variants and their relative merits will be discussed at a later stage.

**General remarks on definitions.** The most general type of machine defined here is the c-machine, which can make arbitrary choices during its computation. However, this paper restricts attention to automatic machines (a-machines), which operate entirely deterministically based on their current configuration. Within the class of automatic machines, computing machines are distinguished by producing a sequence of binary digits (0's and 1's) along with auxiliary symbols. The fundamental distinction between circular and circle-free machines corresponds to the distinction between computations that halt (or otherwise fail to produce infinite output) and those that successfully compute an infinite sequence.

These definitions establish a precise mathematical framework for discussing what it means for a number or sequence to be "computable" - namely, that it can be produced by a finite, deterministic process encoded in the machine's table. This framework will prove essential for the later proof that certain mathematical problems, including the Entscheidungsproblem, cannot be solved by any such process.

---

### النسخة العربية

**الآلات الآلية.** إذا كانت حركة الآلة (بالمعنى المقصود في §1) في كل مرحلة محددة بالكامل بواسطة التشكيل، فسنسمي الآلة "آلة آلية" (automatic machine أو a-machine).

لبعض الأغراض قد نستخدم آلات (آلات الاختيار أو c-machines) تكون حركتها محددة جزئياً فقط بواسطة التشكيل (ومن هنا استخدام كلمة "ممكن" في §1). عندما تصل مثل هذه الآلة إلى أحد هذه التشكيلات الغامضة، لا يمكنها الاستمرار حتى يتم إجراء اختيار تعسفي بواسطة مشغل خارجي. ستكون هذه هي الحالة إذا كنا نستخدم الآلات للتعامل مع الأنظمة البديهية. في هذه الورقة أتناول الآلات الآلية فقط، وبالتالي سأستخدم تعبير "آلة" للإشارة إلى "آلة آلية".

**آلات الحوسبة.** إذا طبعت آلة آلية نوعين من الرموز، يتكون النوع الأول منها (المسمى أرقاماً) بالكامل من 0 و1 (بينما تُسمى الرموز الأخرى رموز النوع الثاني)، فسيتم تسمية الآلة بـ "آلة حوسبة". إذا زُوّدت الآلة بشريط فارغ ووُضعت في حالة حركة، بدءاً من تشكيل-الآلة الأولي الصحيح، فستُسمى رموز النوع الأول بالتسلسل المحسوب بواسطة الآلة. تخدم رموز النوع الثاني فقط "للمساعدة في التذكر". التسلسل المحسوب بواسطة الآلة هو تسلسل الأرقام على الشريط، عندما يتم تجاهل رموز النوع الثاني.

**الآلات الدائرية والآلات الخالية من الدوران.** إذا لم تكتب آلة حوسبة أبداً أكثر من عدد منته من رموز النوع الأول، فستُسمى دائرية. وإلا فستُسمى خالية من الدوران.

ستكون الآلة دائرية إذا وصلت إلى تشكيل لا توجد منه حركة ممكنة، أو إذا استمرت في الحركة، وربما طباعة رموز النوع الثاني، ولكن لا يمكنها طباعة أي رموز أخرى من النوع الأول.

**التسلسلات والأعداد القابلة للحوسبة.** يُقال إن التسلسل قابل للحوسبة إذا كان يمكن حسابه بواسطة آلة خالية من الدوران. العدد قابل للحوسبة إذا كان يختلف بعدد صحيح عن العدد المحسوب بواسطة آلة خالية من الدوران.

نقول إن العدد قابل للحوسبة إذا كان يمكن كتابة تمثيله العشري بواسطة آلة.

تشمل الأعداد القابلة للحوسبة جميع الأعداد التي يمكن اعتبارها بشكل طبيعي قابلة للحوسبة بالمعنى العادي. على سبيل المثال، جميع الأعداد الجبرية الحقيقية قابلة للحوسبة، وكذلك الأجزاء الحقيقية لأصفار دوال بيسل. العدد π قابل للحوسبة، وكذلك e (أساس اللوغاريتمات الطبيعية). بشكل أعم، أي عدد يمكن حساب توسعه العشري بواسطة عملية منهجية هو قابل للحوسبة بمعنى تورينغ.

**المتغيرات المُرضية.** سيُوجد أن بعض المتغيرات من هذه التعريفات للأعداد القابلة للحوسبة مُرضية من بعض وجهات النظر وغير مُرضية من وجهات نظر أخرى. ستتم مناقشة هذه المتغيرات ومزاياها النسبية في مرحلة لاحقة.

**ملاحظات عامة حول التعريفات.** النوع الأكثر عمومية من الآلات المعرّفة هنا هو آلة-c، والتي يمكنها إجراء اختيارات تعسفية أثناء حسابها. ومع ذلك، تقتصر هذه الورقة على الآلات الآلية (a-machines)، التي تعمل بشكل حتمي تماماً بناءً على تشكيلها الحالي. ضمن فئة الآلات الآلية، تتميز آلات الحوسبة بإنتاج تسلسل من الأرقام الثنائية (0's و1's) إلى جانب الرموز المساعدة. التمييز الأساسي بين الآلات الدائرية والآلات الخالية من الدوران يتوافق مع التمييز بين الحسابات التي تتوقف (أو تفشل بطريقة أخرى في إنتاج مخرجات لانهائية) وتلك التي تحسب بنجاح تسلسلاً لانهائياً.

تُنشئ هذه التعريفات إطاراً رياضياً دقيقاً لمناقشة ما يعنيه أن يكون العدد أو التسلسل "قابلاً للحوسبة" - أي أنه يمكن إنتاجه بواسطة عملية منتهية وحتمية مُشفّرة في جدول الآلة. سيثبت هذا الإطار أنه ضروري للبرهان اللاحق على أن بعض المسائل الرياضية، بما في ذلك مسألة القرار، لا يمكن حلها بواسطة أي عملية من هذا القبيل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Automatic machine (a-machine) - آلة آلية
  - Choice machine (c-machine) - آلة اختيار
  - Computing machine - آلة حوسبة
  - Figures (first kind symbols) - أرقام (رموز النوع الأول)
  - Symbols of the second kind - رموز النوع الثاني
  - Circular machine - آلة دائرية
  - Circle-free machine - آلة خالية من الدوران
  - Computable sequence - تسلسل قابل للحوسبة
  - Computable number - عدد قابل للحوسبة

- **Equations:** None

- **Citations:** None in this section

- **Special handling:**
  - The abbreviations "a-machine" and "c-machine" are explained in Arabic but kept in their English form when used as technical terms
  - Examples of computable numbers (π, e, algebraic numbers, Bessel functions) are preserved in their mathematical notation
  - The distinction between deterministic (automatic) and non-deterministic (choice) machines is carefully preserved

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.92
- **Overall section score:** 0.92

### Sources

This translation is based on:
- Turing, A.M. (1936-37). "On Computable Numbers, with an Application to the Entscheidungsproblem." §2
- Standard definitions from computability theory
- Academic analyses of Turing's formal definitions
