# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.88
**Glossary Terms Used:** complexity, algorithm, theorem, proof, polynomial, nondeterministic, Turing machine, computational model, reduction, oracle, tautology, graph, NP-completeness

---

### English Version

It is shown that any recognition problem solved by a polynomial time-bounded nondeterministic Turing machine can be "reduced" to the problem of determining whether a given propositional formula is a tautology. Here "reduced" means, roughly speaking, that the first problem can be solved deterministically in polynomial time provided an oracle is available for solving the second. From this notion of reducible, polynomial degrees of difficulty are defined, and it is shown that the problem of determining tautologyhood has the same polynomial degree as the problem of determining whether the first of two given graphs is isomorphic to a subgraph of the second. Other problems of the same polynomial degree include the problem of determining whether a given graph has a clique of a given size, and the problem of determining whether a given propositional formula is satisfiable. This paper laid the foundation for the theory of NP-completeness.

---

### النسخة العربية

يُثبت أن أي مسألة تعرف يتم حلها بواسطة آلة تورينغ لا حتمية محدودة بزمن متعدد حدود يمكن "اختزالها" إلى مسألة تحديد ما إذا كانت صيغة قضوية معينة عبارة عن حقيقة منطقية (tautology). هنا "الاختزال" يعني، بشكل تقريبي، أن المسألة الأولى يمكن حلها بشكل حتمي في زمن متعدد حدود بشرط توفر أوراكل لحل المسألة الثانية. من هذا المفهوم للاختزال، يتم تعريف درجات الصعوبة متعددة الحدود، ويُثبت أن مسألة تحديد الحقيقة المنطقية لها نفس درجة التعقيد متعدد الحدود كمسألة تحديد ما إذا كان الأول من رسمين بيانيين معطيين متشاكل مع رسم بياني فرعي من الثاني. من بين المسائل الأخرى التي لها نفس درجة التعقيد متعدد الحدود: مسألة تحديد ما إذا كان رسم بياني معطى يحتوي على مجموعة كاملة (clique) بحجم معين، ومسألة تحديد ما إذا كانت صيغة قضوية معطاة قابلة للإرضاء (satisfiable). وضعت هذه الورقة الأساس لنظرية الاكتمال NP.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** nondeterministic Turing machine, polynomial time, reducibility, oracle, tautology, satisfiability, clique, graph isomorphism, NP-completeness
- **Equations:** None in abstract
- **Citations:** None in abstract
- **Special handling:** Technical terms preserved with Arabic equivalents; "tautology" and "satisfiable" kept in English with Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.90
- **Overall section score:** 0.88

### Back-Translation (Validation)

It is proven that any recognition problem solved by a polynomial time-bounded nondeterministic Turing machine can be "reduced" to the problem of determining whether a given propositional formula is a tautology. Here "reduction" means, approximately, that the first problem can be solved deterministically in polynomial time provided an oracle is available to solve the second problem. From this concept of reduction, polynomial degrees of difficulty are defined, and it is proven that the problem of determining tautologyhood has the same polynomial complexity degree as the problem of determining whether the first of two given graphs is isomorphic to a subgraph of the second. Among other problems with the same polynomial complexity degree: the problem of determining whether a given graph contains a clique of a given size, and the problem of determining whether a given propositional formula is satisfiable. This paper laid the foundation for the theory of NP-completeness.
