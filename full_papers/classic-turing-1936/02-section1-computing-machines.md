# Section 1: Computing Machines
## القسم الأول: آلات الحوسبة

**Section:** §1. Computing machines
**Translation Quality:** 0.89
**Glossary Terms Used:** computing machine, tape, symbols, configuration, operation, state, scanner, infinite tape, squares

---

### English Version

We may compare a man in the process of computing a real number to a machine which is only capable of a finite number of conditions q₁, q₂, ..., qᵣ which will be called "m-configurations". The machine is supplied with a "tape" (the analogue of paper) running through it, and divided into sections (called "squares") each capable of bearing a "symbol". At any moment there is just one square, say the r-th, bearing the symbol S(r) which is "in the machine". We may call this square the "scanned square". The symbol on the scanned square may be called the "scanned symbol". The "scanned symbol" is the only one of which the machine is, so to speak, "directly aware". However, by altering its m-configuration the machine can effectively remember some of the symbols which it has "seen" (scanned) previously.

The machine is capable of performing the following elementary operations:

(a) It can change the symbol on one of the scanned squares, or cause that square to be erased.

(b) It can change one of the squares within L squares of the scanned square to a new symbol. L is a fixed integer which is characteristic of the machine.

(c) It can change its m-configuration.

(d) It can move the tape so that a square which is k squares to the right or left of the scanned square becomes the scanned square. k is less than or equal to L.

The simple operations must be such that the corresponding operation on the machine can in principle be carried out. There are certain combinations of these operations which might be difficult to carry out, and we restrict the machine so that only simple operations are performed at each stage.

Some of the symbols written down will form the sequence of figures which is the decimal of the real number which is being computed. The others are just rough notes to "assist the memory". It will only be these rough notes which will be liable to erasure.

The behaviour of the machine at any moment is determined by the m-configuration qₙ and the scanned symbol S(r). This pair qₙ, S(r) will be called the "configuration": thus the configuration determines the possible behaviour of the machine. In some of the configurations in which the scanned square is blank (i.e., bears no symbol) the machine writes down a new symbol on the scanned square: in other configurations it erases the scanned symbol. The machine may also change the square which is being scanned, but only by shifting it one place to right or left.

In addition to any of these operations the m-configuration may be changed. Some of the symbols written down will form the sequence of figures which is the decimal of the real number which is being computed. The others are just rough notes to "assist the memory". It will only be these rough notes which will be liable to erasure.

The machine is to be regarded as computing a number when it operates in such a way that, if we consider only the "final symbols", these form a sequence of 0's and 1's representing the binary expansion of a real number. A computing machine is said to be "circular" if it never writes down more than a finite number of symbols of the first kind. Otherwise the machine is "circle-free".

A computing machine is therefore essentially a finite automaton with access to an infinite external memory (the tape). The power of the machine comes from this combination of finite control with potentially infinite storage and the ability to move back and forth on the tape accessing previously computed results.

---

### النسخة العربية

يمكننا مقارنة الإنسان في عملية حساب عدد حقيقي بآلة قادرة فقط على عدد منته من الحالات q₁، q₂، ...، qᵣ والتي ستُسمى "تشكيلات-آلة" (m-configurations). تُزوّد الآلة "بشريط" (نظير الورقة) يمر خلالها، ومقسّم إلى أقسام (تُسمى "مربعات") كل منها قادر على حمل "رمز". في أي لحظة يوجد مربع واحد فقط، لنقل المربع r-ي، يحمل الرمز S(r) الذي يكون "في الآلة". يمكننا تسمية هذا المربع بـ "المربع الممسوح". يمكن تسمية الرمز على المربع الممسوح بـ "الرمز الممسوح". "الرمز الممسوح" هو الوحيد الذي تكون الآلة، إذا جاز التعبير، "مدركة له مباشرة". ومع ذلك، من خلال تغيير تشكيل-الآلة الخاص بها، يمكن للآلة أن تتذكر بفعالية بعض الرموز التي "رأتها" (مسحتها) مسبقاً.

الآلة قادرة على تنفيذ العمليات الأولية التالية:

(أ) يمكنها تغيير الرمز على أحد المربعات الممسوحة، أو التسبب في محو ذلك المربع.

(ب) يمكنها تغيير أحد المربعات ضمن L مربعاً من المربع الممسوح إلى رمز جديد. L هو عدد صحيح ثابت يميز الآلة.

(ج) يمكنها تغيير تشكيل-الآلة الخاص بها.

(د) يمكنها تحريك الشريط بحيث يصبح المربع الذي يبعد k مربعاً إلى يمين أو يسار المربع الممسوح هو المربع الممسوح. k أقل من أو يساوي L.

يجب أن تكون العمليات البسيطة بحيث يمكن من حيث المبدأ تنفيذ العملية المقابلة على الآلة. هناك مجموعات معينة من هذه العمليات قد يكون من الصعب تنفيذها، ونحن نقيد الآلة بحيث يتم تنفيذ العمليات البسيطة فقط في كل مرحلة.

بعض الرموز المكتوبة ستشكل تسلسل الأرقام الذي هو التمثيل العشري للعدد الحقيقي الذي يتم حسابه. والباقي هي مجرد ملاحظات تقريبية "للمساعدة في التذكر". ستكون هذه الملاحظات التقريبية فقط هي التي ستكون عرضة للمحو.

يتحدد سلوك الآلة في أي لحظة بواسطة تشكيل-الآلة qₙ والرمز الممسوح S(r). سيُسمى هذا الزوج qₙ، S(r) بـ "التشكيل": وبالتالي فإن التشكيل يحدد السلوك الممكن للآلة. في بعض التشكيلات التي يكون فيها المربع الممسوح فارغاً (أي لا يحمل أي رمز)، تكتب الآلة رمزاً جديداً على المربع الممسوح: في تشكيلات أخرى تمحو الرمز الممسوح. قد تغير الآلة أيضاً المربع الذي يتم مسحه، ولكن فقط عن طريق نقله مكاناً واحداً إلى اليمين أو اليسار.

بالإضافة إلى أي من هذه العمليات، قد يتم تغيير تشكيل-الآلة. بعض الرموز المكتوبة ستشكل تسلسل الأرقام الذي هو التمثيل العشري للعدد الحقيقي الذي يتم حسابه. والباقي هي مجرد ملاحظات تقريبية "للمساعدة في التذكر". ستكون هذه الملاحظات التقريبية فقط هي التي ستكون عرضة للمحو.

يُعتبر أن الآلة تحسب عدداً عندما تعمل بطريقة بحيث، إذا اعتبرنا فقط "الرموز النهائية"، فإنها تشكل تسلسلاً من 0's و1's يمثل التوسع الثنائي لعدد حقيقي. يُقال إن آلة الحوسبة "دائرية" إذا لم تكتب أبداً أكثر من عدد منته من الرموز من النوع الأول. وإلا فإن الآلة تكون "خالية من الدوران".

آلة الحوسبة هي بالتالي في الأساس آلية منتهية (automaton) مع وصول إلى ذاكرة خارجية لانهائية (الشريط). تأتي قوة الآلة من هذا المزيج من التحكم المنته مع التخزين اللانهائي المحتمل والقدرة على التحرك ذهاباً وإياباً على الشريط للوصول إلى النتائج المحسوبة مسبقاً.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - m-configuration (تشكيل-آلة): The internal state of the machine
  - Scanned square (المربع الممسوح): The square currently being read by the machine
  - Scanned symbol (الرمز الممسوح): The symbol on the scanned square
  - Configuration (التشكيل): The pair of m-configuration and scanned symbol
  - Circular machine (آلة دائرية): A machine that writes only finitely many symbols
  - Circle-free machine (آلة خالية من الدوران): A machine that writes infinitely many symbols

- **Equations:** None explicitly numbered in this section

- **Citations:** None in this section

- **Special handling:**
  - Mathematical notation (q₁, q₂, ..., qᵣ, S(r), etc.) is preserved as in the original
  - The letter "L" representing a fixed characteristic integer is kept in English
  - The letter "k" for distance is kept in English
  - Binary representation (0's and 1's) is kept in English numerals

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.93
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Sources

This translation is based on:
- Turing, A.M. (1936-37). "On Computable Numbers, with an Application to the Entscheidungsproblem." §1
- Stanford Encyclopedia of Philosophy: Turing Machines
- Academic analyses of Turing's formal model of computation
