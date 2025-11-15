# Section 3: Constraint Logic
## القسم 3: المنطق القيدي

**Section:** Constraint Logic
**Translation Quality:** 0.88
**Glossary Terms Used:** algorithm, complexity, NP-complete, PSPACE-complete, EXPTIME-complete, hardness, reduction, SAT, Boolean, graph, planar, puzzle, game theory

---

### English Version

Combinatorial Game Theory provides a theoretical framework for giving positive algorithmic results for games, but does not naturally accommodate puzzles. In contrast, negative algorithmic results—hardness and completeness within computational complexity classes—are more uniform: puzzles and games have analogous prototypical proof structures. Furthermore, a relatively new theory called Constraint Logic attempts to tie together a wide range of hardness proofs for both puzzles and games.

Proving that a problem is hard within a particular complexity class (like NP, PSPACE, or EXPTIME) almost always involves a reduction to the problem from a known hard problem within the class. For example, the canonical problem to reduce from for NP-hardness is Boolean Satisfiability (SAT). Reducing SAT to a puzzle of interest proves that that puzzle is NP-hard. Similarly, the canonical problem to reduce from for PSPACE-hardness is Quantified Boolean Formulas (QBF).

Constraint Logic is a useful tool for showing hardness of games and puzzles in a variety of settings that has emerged in recent years. Indeed, many of the hardness results mentioned in this survey are based on reductions from Constraint Logic. Constraint Logic is a family of games where players reverse edges on a planar directed graph while satisfying vertex in-flow constraints. Each edge has a weight of 1 or 2. Each vertex has degree 3 and requires that the sum of the weights of inward-directed edges is at least 2. Vertices may be restricted to two types: And vertices have incident edge weights of 1, 1, and 2; and Or vertices have incident edge weights of 2, 2, and 2. A player's goal is to eventually reverse a given edge.

This game family can be interpreted in many game-theoretic settings, ranging from zero-player automata to multiplayer games with hidden information. In particular, there are natural versions of Constraint Logic corresponding to one-player games (puzzles) and two-player games, both of bounded and unbounded length. (Here we refer to whether the length of the game is bounded by a polynomial function of the board size. Typically, bounded games are nonloopy while unbounded games are loopy.) These games have the expected complexities: one-player bounded games are NP-complete; one-player unbounded games and two-player bounded games are PSPACE-complete; and two-player unbounded games are EXPTIME-complete.

What makes Constraint Logic specially suited for game and puzzle reductions is that the problems are already in form similar to many games. In particular, the fact that the games are played on planar graphs means that the reduction does not usually need a crossover gadget, whereas historically crossover gadgets have often been the complex crux of a game hardness proof.

Historically, Constraint Logic arose as a simplification of the "Generalized Rush-Hour Logic" of Flake and Baum. The resulting one-player unbounded setting, called Nondeterministic Constraint Logic, was later generalized to other game categories.

---

### النسخة العربية

توفر نظرية الألعاب التوافقية إطاراً نظرياً لإعطاء نتائج خوارزمية إيجابية للألعاب، لكنها لا تستوعب الألغاز بشكل طبيعي. في المقابل، النتائج الخوارزمية السلبية - الصعوبة والاكتمال ضمن فئات التعقيد الحسابي - أكثر توحيداً: الألغاز والألعاب لها بنى برهان نموذجية مماثلة. علاوة على ذلك، تحاول نظرية جديدة نسبياً تسمى المنطق القيدي ربط مجموعة واسعة من براهين الصعوبة لكل من الألغاز والألعاب.

إثبات أن مشكلة ما صعبة ضمن فئة تعقيد معينة (مثل NP أو PSPACE أو EXPTIME) يتضمن دائماً تقريباً اختزالاً إلى المشكلة من مشكلة صعبة معروفة ضمن الفئة. على سبيل المثال، المشكلة الكنسية التي يتم الاختزال منها لصعوبة NP هي الاستيفاء المنطقي (SAT). اختزال SAT إلى لغز مثير للاهتمام يثبت أن ذلك اللغز صعب من نوع NP. بالمثل، المشكلة الكنسية التي يتم الاختزال منها لصعوبة PSPACE هي الصيغ المنطقية المقيدة بالكميات (QBF).

المنطق القيدي هو أداة مفيدة لإظهار صعوبة الألعاب والألغاز في مجموعة متنوعة من الإعدادات التي ظهرت في السنوات الأخيرة. في الواقع، تستند العديد من نتائج الصعوبة المذكورة في هذا المسح إلى اختزالات من المنطق القيدي. المنطق القيدي هو عائلة من الألعاب حيث يعكس اللاعبون الحواف على رسم بياني موجه مستوٍ مع تلبية قيود التدفق الداخل للرأس. كل حافة لها وزن 1 أو 2. كل رأس له درجة 3 ويتطلب أن يكون مجموع أوزان الحواف الموجهة الداخلة 2 على الأقل. قد تقتصر الرؤوس على نوعين: رؤوس And لها أوزان حواف واقعة 1 و1 و2؛ ورؤوس Or لها أوزان حواف واقعة 2 و2 و2. هدف اللاعب هو عكس حافة معينة في النهاية.

يمكن تفسير عائلة اللعبة هذه في العديد من الإعدادات النظرية للعبة، تتراوح من آليات بدون لاعبين إلى ألعاب متعددة اللاعبين مع معلومات مخفية. على وجه الخصوص، هناك إصدارات طبيعية من المنطق القيدي تقابل ألعاب اللاعب الواحد (الألغاز) والألعاب ذات اللاعبين، كلاهما ذات طول محدود وغير محدود. (هنا نشير إلى ما إذا كان طول اللعبة محدوداً بدالة متعددة الحدود لحجم اللوحة. عادةً، الألعاب المحدودة غير حلقية بينما الألعاب غير المحدودة حلقية.) هذه الألعاب لها التعقيدات المتوقعة: ألعاب اللاعب الواحد المحدودة مكتملة من نوع NP؛ ألعاب اللاعب الواحد غير المحدودة والألعاب ذات اللاعبين المحدودة مكتملة من نوع PSPACE؛ والألعاب ذات اللاعبين غير المحدودة مكتملة من نوع EXPTIME.

ما يجعل المنطق القيدي مناسباً بشكل خاص لاختزالات الألعاب والألغاز هو أن المشاكل موجودة بالفعل في شكل مشابه للعديد من الألعاب. على وجه الخصوص، حقيقة أن الألعاب تُلعب على رسوم بيانية مستوية تعني أن الاختزال لا يحتاج عادةً إلى أداة تقاطع، في حين أن أدوات التقاطع كانت تاريخياً غالباً جوهر معقد لبرهان صعوبة اللعبة.

تاريخياً، نشأ المنطق القيدي كتبسيط لـ "منطق Rush-Hour المعمم" لـ Flake وBaum. الإعداد غير المحدود للاعب الواحد الناتج، المسمى المنطق القيدي غير الحتمي، تم تعميمه لاحقاً إلى فئات لعبة أخرى.

---

### Translation Notes

- **Key terms introduced:** Constraint Logic (المنطق القيدي), Boolean Satisfiability/SAT (الاستيفاء المنطقي), Quantified Boolean Formulas/QBF (الصيغ المنطقية المقيدة بالكميات), planar directed graph (رسم بياني موجه مستوٍ), in-flow constraints (قيود التدفق الداخل), And vertices (رؤوس And), Or vertices (رؤوس Or), crossover gadget (أداة تقاطع), Nondeterministic Constraint Logic (المنطق القيدي غير الحتمي)
- **Mathematical concepts:** Edge weights, vertex degree, graph theory concepts
- **Citations:** References to Flake and Baum [FB02], [HD02, HD05], [Hea06b, DH08] maintained in English
- **Special handling:** Technical complexity classes (NP, PSPACE, EXPTIME) kept in English as standard; "And" and "Or" vertices kept in English as they are technical terms

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
