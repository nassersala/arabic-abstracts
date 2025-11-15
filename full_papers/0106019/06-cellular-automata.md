# Section 6: Cellular Automata and Life
## القسم 6: الآليات الخلوية والحياة

**Section:** Cellular Automata and Life
**Translation Quality:** 0.89
**Glossary Terms Used:** cellular automata, undecidable, PSPACE-complete, Turing machine, algorithm

---

### English Version

Conway's Game of Life is a zero-player cellular automaton played on the square tiling of the plane. Initially, certain cells (squares) are marked alive or dead. Each move globally evolves the cells: a live cell remains alive if between 2 and 3 of its 8 neighbors were alive, and a dead cell becomes alive if it had precisely 3 live neighbors.

Many questions can be asked about an initial configuration of Life; one key question is whether the population will ever completely die out (no cells are alive). Chapter 25 of Winning Ways describes a reduction showing that this question is undecidable. In particular, the same question about Life restricted within a polynomially bounded region is PSPACE-complete. More recently, Rendell constructed an explicit Turing machine in Life, which establishes the same results.

There are other open complexity-theoretic questions about Life. How hard is it to tell whether a configuration is a Garden of Eden, that is, cannot be the state that results from another? Given a rectangular pattern in Life, how hard is it to extend the pattern outside the rectangle to form a Still Life (which never changes)?

Several other cellular automata, with different survival and birth rules, have been studied; see, e.g., Wolfram's work.

---

### النسخة العربية

لعبة الحياة لكونواي هي آلية خلوية بدون لاعبين تُلعب على التبليط المربع للمستوى. في البداية، يتم وضع علامة على خلايا معينة (مربعات) على أنها حية أو ميتة. كل حركة تطور الخلايا عالمياً: تبقى الخلية الحية حية إذا كان ما بين 2 و3 من جيرانها الثمانية أحياء، وتصبح الخلية الميتة حية إذا كان لديها بالضبط 3 جيران أحياء.

يمكن طرح العديد من الأسئلة حول تكوين أولي للحياة؛ أحد الأسئلة الرئيسية هو ما إذا كان السكان سيموتون بالكامل في أي وقت (لا توجد خلايا حية). يصف الفصل 25 من Winning Ways اختزالاً يوضح أن هذا السؤال غير قابل للحسم. على وجه الخصوص، نفس السؤال حول الحياة المقيدة داخل منطقة محدودة بشكل متعدد الحدود هو مكتمل من نوع PSPACE. مؤخراً، بنى Rendell آلة تورينج صريحة في الحياة، والتي تثبت نفس النتائج.

هناك أسئلة أخرى مفتوحة نظرية التعقيد حول الحياة. ما مدى صعوبة معرفة ما إذا كان التكوين هو جنة عدن، أي لا يمكن أن يكون الحالة التي تنتج عن آخر؟ بالنظر إلى نمط مستطيل في الحياة، ما مدى صعوبة توسيع النمط خارج المستطيل لتشكيل حياة ثابتة (التي لا تتغير أبداً)؟

تمت دراسة العديد من الآليات الخلوية الأخرى، بقواعد بقاء وولادة مختلفة؛ انظر، على سبيل المثال، عمل Wolfram.

---

### Translation Notes

- **Key terms introduced:** cellular automata (آليات خلوية), Conway's Game of Life (لعبة الحياة لكونواي), Garden of Eden (جنة عدن), Still Life (حياة ثابتة), Turing machine (آلة تورينج), undecidable (غير قابل للحسم)
- **Mathematical concepts:** Polynomially bounded region, neighbor rules
- **Citations:** References to Winning Ways [BCG04], Rendell [Ren05], Wolfram [Wol94]
- **Special handling:** Game of Life rules carefully translated to maintain precision

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89
