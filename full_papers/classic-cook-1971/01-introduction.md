# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** computational complexity, polynomial time, nondeterministic, Turing machine, algorithm, reducibility, tautology, satisfiability, theorem proving

---

### English Version

The question "How hard is it to prove theorems?" is of central interest in mathematical logic. One way to make this question precise is to consider the following problem: Given a set of axioms A and a sentence S in some formal system, is there a proof of S from A in which the total number of symbols is bounded by some integer n? Clearly this is decidable, since there are only a finite number of proofs to examine. But the number of possible proofs grows exponentially with n, so that we cannot expect to find a decision procedure which is substantially better than the exhaustive search through all proofs of the appropriate length.

A question closely related to theorem proving is that of recognizing tautologies in propositional logic. A formula in propositional logic is a tautology if it is true under all possible truth assignments to its propositional variables. The problem of determining whether a given formula is a tautology is clearly decidable, but no algorithm has been found which is substantially better than the obvious one of checking all possible truth assignments. On the other hand, determining whether a formula is satisfiable (i.e., true under at least one truth assignment) can be reduced to the tautology problem by simply negating the formula.

In this paper we consider the general class of decision problems which can be solved by polynomial time-bounded nondeterministic algorithms. We show that a large number of apparently unrelated problems belong to this class, including graph-theoretic problems such as finding cliques and node covers, as well as the satisfiability problem for propositional logic. Furthermore, we introduce the notion of polynomial reducibility, and show that all these problems are equivalent in the sense that if any one of them can be solved deterministically in polynomial time, then they all can be.

The central result of this paper is Theorem 1, which states that any problem solvable by a polynomial time-bounded nondeterministic Turing machine can be reduced to the problem of determining whether a propositional formula is a tautology. This reduction is accomplished by constructing, for each nondeterministic computation of length n, a formula which is a tautology if and only if the computation does not result in an accepting state. The formula has length bounded by a polynomial in n.

The notion of reducibility we introduce is related to, but different from, the classical reducibility introduced by Turing. In Turing reducibility, we say that problem A is Turing reducible to problem B if there is an algorithm for solving A which is allowed to use an oracle for solving B. Our notion of polynomial reducibility requires, in addition, that the algorithm run in polynomial time (counting each oracle call as a single step), and that the instances of B which are queried have size bounded by a polynomial in the size of the original instance of A.

---

### النسخة العربية

السؤال "ما مدى صعوبة إثبات النظريات؟" ذو أهمية مركزية في المنطق الرياضي. إحدى طرق جعل هذا السؤال دقيقاً هي النظر في المسألة التالية: بالنظر إلى مجموعة من البديهيات A وجملة S في نظام شكلي ما، هل يوجد برهان لـ S من A يكون فيه العدد الإجمالي للرموز محدوداً بعدد صحيح n؟ من الواضح أن هذا قابل للبت، لأن هناك عدداً محدوداً فقط من البراهين التي يجب فحصها. لكن عدد البراهين الممكنة ينمو بشكل أسي مع n، بحيث لا يمكننا أن نتوقع إيجاد إجراء قرار أفضل بشكل جوهري من البحث الشامل عبر جميع البراهين ذات الطول المناسب.

مسألة ترتبط ارتباطاً وثيقاً بإثبات النظريات هي مسألة التعرف على الحقائق المنطقية في المنطق القضوي. الصيغة في المنطق القضوي هي حقيقة منطقية (tautology) إذا كانت صحيحة تحت جميع الإسنادات الممكنة لقيم الحقيقة لمتغيراتها القضوية. مسألة تحديد ما إذا كانت صيغة معطاة حقيقة منطقية قابلة للبت بوضوح، لكن لم يتم العثور على خوارزمية أفضل بشكل جوهري من الخوارزمية الواضحة المتمثلة في فحص جميع إسنادات القيم الممكنة. من ناحية أخرى، يمكن اختزال تحديد ما إذا كانت الصيغة قابلة للإرضاء (satisfiable) (أي صحيحة تحت إسناد واحد على الأقل) إلى مسألة الحقيقة المنطقية بمجرد نفي الصيغة.

في هذه الورقة نعتبر الفئة العامة لمسائل القرار التي يمكن حلها بواسطة خوارزميات لا حتمية محدودة بزمن متعدد حدود. نُظهر أن عدداً كبيراً من المسائل التي تبدو غير مرتبطة تنتمي إلى هذه الفئة، بما في ذلك المسائل النظرية البيانية مثل إيجاد المجموعات الكاملة (cliques) والأغطية العقدية، وكذلك مسألة الإرضاء للمنطق القضوي. علاوة على ذلك، نقدم مفهوم الاختزال متعدد الحدود، ونُظهر أن جميع هذه المسائل متكافئة بمعنى أنه إذا أمكن حل أي واحدة منها بشكل حتمي في زمن متعدد حدود، فيمكن حلها جميعاً.

النتيجة المركزية في هذه الورقة هي النظرية 1، والتي تنص على أن أي مسألة قابلة للحل بواسطة آلة تورينغ لا حتمية محدودة بزمن متعدد حدود يمكن اختزالها إلى مسألة تحديد ما إذا كانت صيغة قضوية حقيقة منطقية. يتم تحقيق هذا الاختزال بإنشاء، لكل حساب لا حتمي بطول n، صيغة تكون حقيقة منطقية إذا وفقط إذا لم ينتج عن الحساب حالة قبول. الصيغة لها طول محدود بكثير حدود في n.

مفهوم الاختزال الذي نقدمه مرتبط بـ، لكنه يختلف عن، الاختزال الكلاسيكي الذي قدمه تورينغ. في اختزال تورينغ، نقول إن المسألة A قابلة للاختزال بتورينغ إلى المسألة B إذا كانت هناك خوارزمية لحل A يُسمح لها باستخدام أوراكل لحل B. يتطلب مفهومنا للاختزال متعدد الحدود، بالإضافة إلى ذلك، أن تعمل الخوارزمية في زمن متعدد حدود (مع عد كل استدعاء للأوراكل كخطوة واحدة)، وأن تكون حالات B التي يتم الاستعلام عنها ذات حجم محدود بكثير حدود في حجم الحالة الأصلية لـ A.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** polynomial time-bounded, nondeterministic algorithm, polynomial reducibility, Turing reducibility, oracle, decision problem, propositional logic, truth assignment, clique, node cover
- **Equations:** None
- **Citations:** Reference to Turing's work on reducibility
- **Special handling:**
  - Mathematical terms like "tautology" and "satisfiable" retained in English with Arabic explanations
  - Formal variables (A, S, n, B) kept in English as is standard practice
  - Technical concepts carefully explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation Validation

The question "How difficult is it to prove theorems?" is of central importance in mathematical logic. One way to make this question precise is to consider the following problem: Given a set of axioms A and a sentence S in some formal system, is there a proof of S from A where the total number of symbols is bounded by an integer n? It is clear that this is decidable, because there is only a finite number of proofs that must be checked. But the number of possible proofs grows exponentially with n, so we cannot expect to find a decision procedure substantially better than exhaustive search through all proofs of the appropriate length.

A problem closely related to theorem proving is the problem of recognizing tautologies in propositional logic. A formula in propositional logic is a tautology if it is true under all possible truth value assignments to its propositional variables. The problem of determining whether a given formula is a tautology is clearly decidable, but no algorithm has been found substantially better than the obvious algorithm of checking all possible value assignments. On the other hand, determining whether a formula is satisfiable (i.e., true under at least one assignment) can be reduced to the tautology problem by simply negating the formula.

In this paper we consider the general class of decision problems that can be solved by nondeterministic algorithms bounded by polynomial time. We show that a large number of apparently unrelated problems belong to this class, including graph-theoretic problems such as finding cliques and node covers, as well as the satisfiability problem for propositional logic. Furthermore, we introduce the concept of polynomial reduction, and show that all these problems are equivalent in the sense that if any one of them can be solved deterministically in polynomial time, then they all can be solved.

The central result in this paper is Theorem 1, which states that any problem solvable by a polynomial time-bounded nondeterministic Turing machine can be reduced to the problem of determining whether a propositional formula is a tautology. This reduction is achieved by constructing, for each nondeterministic computation of length n, a formula that is a tautology if and only if the computation does not result in an accepting state. The formula has length bounded by a polynomial in n.

The concept of reduction we introduce is related to, but different from, the classical reduction introduced by Turing. In Turing reduction, we say that problem A is Turing reducible to problem B if there is an algorithm for solving A that is allowed to use an oracle for solving B. Our concept of polynomial reduction requires, in addition, that the algorithm run in polynomial time (counting each oracle call as a single step), and that the instances of B that are queried have size bounded by a polynomial in the size of the original instance of A.
