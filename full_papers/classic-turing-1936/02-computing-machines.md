# Section 2: Computing Machines
## القسم 2: آلات الحوسبة

**Section:** Computing Machines
**Translation Quality:** 0.87
**Glossary Terms Used:** machine, tape, symbol, state, configuration, m-configuration, operation, algorithm, finite, automaton

---

### English Version

We may compare a man in the process of computing a real number to a machine which is only capable of a finite number of conditions q₁, q₂, ..., qᵣ which will be called "m-configurations". The machine is supplied with a "tape" (the analogue of paper) running through it, and divided into sections (called "squares") each capable of bearing a "symbol". At any moment there is just one square, say the r-th, bearing the symbol S(r) which is "in the machine". We may call this square the "scanned square". The symbol on the scanned square may be called the "scanned symbol". The "scanned symbol" is the only one of which the machine is, so to speak, "directly aware". However, by altering its m-configuration the machine can effectively remember some of the symbols which it has "seen" (scanned) previously.

The possible behaviour of the machine at any moment is determined by the m-configuration qₙ and the scanned symbol S(r). This pair qₙ, S(r) will be called the "configuration": thus the configuration determines the possible behaviour of the machine. In some of the configurations in which the scanned square is blank (i.e., bears no symbol) the machine writes down a new symbol on the scanned square: in other configurations it erases the scanned symbol. The machine may also change the square which is being scanned, but only by shifting it one place to right or left. In addition to any of these operations the m-configuration may be changed.

Some of the symbols written down will form the sequence of figures which is the decimal of the real number which is being computed. The others are just rough notes to "assist the memory". It will only be these rough notes which will be liable to erasure.

The behaviour of the machine is determined by a finite table. In the complete configuration, the table gives the behaviour of the machine in every configuration. This table is called the "description" of the machine, or its "standard description" (S.D.). The entries in the table specify:
- The symbol to be written (if any)
- The direction to move (L for left, R for right, or N for no movement)
- The new m-configuration

A machine operating according to definite rules and proceeding from configuration to configuration is called "automatic". A machine which has a table of behaviour and which operates according to that table is said to be "circular" if it never writes down more than a finite number of symbols of the first kind (i.e., figures of the computed sequence). Otherwise it is said to be "circle-free".

---

### النسخة العربية

يمكننا مقارنة شخص في عملية حساب عدد حقيقي بآلة قادرة فقط على عدد منتهٍ من الحالات q₁, q₂, ..., qᵣ والتي ستُسمى "م-تشكيلات" (m-configurations). تُزود الآلة بـ"شريط" (نظير الورقة) يمر من خلالها، ومقسم إلى أقسام (تُسمى "مربعات") كل منها قادر على حمل "رمز". في أي لحظة يوجد مربع واحد فقط، لنقل المربع r، يحمل الرمز S(r) الذي يكون "في الآلة". يمكننا تسمية هذا المربع "المربع الممسوح ضوئياً". يمكن تسمية الرمز الموجود على المربع الممسوح ضوئياً "الرمز الممسوح ضوئياً". "الرمز الممسوح ضوئياً" هو الرمز الوحيد الذي تكون الآلة، إذا جاز التعبير، "مدركة له مباشرة". ومع ذلك، بتغيير م-تشكيلها يمكن للآلة بشكل فعال أن تتذكر بعض الرموز التي "رأتها" (مسحتها ضوئياً) سابقاً.

يتم تحديد السلوك المحتمل للآلة في أي لحظة بواسطة الم-تشكيل qₙ والرمز الممسوح ضوئياً S(r). سيُسمى هذا الزوج qₙ, S(r) "التشكيل" (configuration): وبالتالي فإن التشكيل يحدد السلوك المحتمل للآلة. في بعض التشكيلات التي يكون فيها المربع الممسوح ضوئياً فارغاً (أي لا يحمل رمزاً) تكتب الآلة رمزاً جديداً على المربع الممسوح ضوئياً: وفي تشكيلات أخرى تمحو الرمز الممسوح ضوئياً. قد تغير الآلة أيضاً المربع الذي يتم مسحه ضوئياً، ولكن فقط بإزاحته مكاناً واحداً إلى اليمين أو اليسار. بالإضافة إلى أي من هذه العمليات، قد يتم تغيير الم-تشكيل.

بعض الرموز المكتوبة ستشكل متتالية الأرقام التي هي الكسر العشري للعدد الحقيقي الذي يتم حسابه. والبعض الآخر هو مجرد ملاحظات تقريبية "للمساعدة في التذكر". وستكون هذه الملاحظات التقريبية فقط هي التي ستكون عرضة للمحو.

يتم تحديد سلوك الآلة بواسطة جدول منتهٍ. في التشكيل الكامل، يعطي الجدول سلوك الآلة في كل تشكيل. يُسمى هذا الجدول "وصف" الآلة، أو "الوصف القياسي" لها (S.D.). تحدد المدخلات في الجدول:
- الرمز الذي سيُكتب (إن وُجد)
- اتجاه الحركة (L لليسار، R لليمين، أو N لعدم الحركة)
- الم-تشكيل الجديد

تُسمى الآلة التي تعمل وفقاً لقواعد محددة وتنتقل من تشكيل إلى تشكيل "أوتوماتيكية" (automatic). يُقال عن الآلة التي لديها جدول سلوك وتعمل وفقاً لذلك الجدول أنها "دائرية" (circular) إذا لم تكتب أبداً أكثر من عدد منتهٍ من الرموز من النوع الأول (أي أرقام المتتالية المحسوبة). وإلا فيُقال إنها "خالية من الدوائر" (circle-free).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - m-configuration (م-تشكيل)
  - Scanned square (المربع الممسوح ضوئياً)
  - Scanned symbol (الرمز الممسوح ضوئياً)
  - Configuration (التشكيل)
  - Standard description (الوصف القياسي)
  - Automatic machine (آلة أوتوماتيكية)
  - Circular (دائرية)
  - Circle-free (خالية من الدوائر)
- **Equations:** Uses symbolic notation q₁, q₂, ..., qᵣ and S(r)
- **Citations:** None
- **Special handling:**
  - Preserved mathematical notation and subscripts
  - Maintained the distinction between m-configuration (internal state) and configuration (state + scanned symbol)
  - Kept technical abbreviations (S.D., L, R, N) with explanations in both languages

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
