# Customized Monte Carlo Tree Search for LLVM/Polly's Composable Loop Optimization Transformations
## بحث شجرة مونت كارلو المخصص لتحويلات تحسين الحلقات القابلة للتركيب في LLVM/Polly

**Section:** Abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** LLVM, Polly, polyhedral, loop optimization, loop transformation, compiler, Monte Carlo Tree Search, search algorithm, exploration, exploitation, heuristic optimization, speedup

---

### English Version

Polly is the LLVM project's polyhedral loop nest optimizer. Recently, user-directed loop transformation pragmas were proposed based on LLVM/Clang and Polly. The search space exposed by the transformation pragmas is a tree, wherein each node represents a specific combination of loop transformations that can be applied to the code resulting from the parent node's loop transformations. We have developed a search algorithm based on Monte Carlo tree search (MCTS) to find the best combination of loop transformations. Our algorithm consists of two phases: exploring loop transformations at different depths of the tree to identify promising regions in the tree search space and exploiting those regions by performing a local search. Moreover, a restart mechanism is used to avoid the MCTS getting trapped in a local solution. The best and worst solutions are transferred from the previous phases of the restarts to leverage the search history. We compare our approach with random, greedy, and breadth-first search methods on PolyBench kernels and ECP proxy applications. Experimental results show that our MCTS algorithm finds pragma combinations with a speedup of 2.3x over Polly's heuristic optimizations on average.

---

### النسخة العربية

Polly هو محسِّن أعشاش الحلقات متعدد السطوح لمشروع LLVM. مؤخراً، تم اقتراح توجيهات pragma لتحويل الحلقات الموجهة بواسطة المستخدم بناءً على LLVM/Clang وPolly. فضاء البحث المكشوف بواسطة توجيهات التحويل pragma هو شجرة، حيث تمثل كل عقدة مجموعة محددة من تحويلات الحلقات التي يمكن تطبيقها على الشفرة الناتجة عن تحويلات الحلقات للعقدة الأم. طورنا خوارزمية بحث قائمة على بحث شجرة مونت كارلو (MCTS) لإيجاد أفضل مجموعة من تحويلات الحلقات. تتكون خوارزميتنا من مرحلتين: استكشاف تحويلات الحلقات على أعماق مختلفة من الشجرة لتحديد المناطق الواعدة في فضاء بحث الشجرة واستغلال تلك المناطق من خلال إجراء بحث محلي. علاوة على ذلك، يتم استخدام آلية إعادة التشغيل لتجنب انحصار MCTS في حل محلي. يتم نقل الحلول الأفضل والأسوأ من المراحل السابقة لإعادة التشغيل للاستفادة من سجل البحث. نقارن نهجنا بطرق البحث العشوائية والجشعة والبحث بالعرض أولاً على نوى PolyBench وتطبيقات ECP البديلة. تظهر النتائج التجريبية أن خوارزمية MCTS الخاصة بنا تجد مجموعات pragma بتسريع 2.3 مرة عن تحسينات Polly الاستدلالية في المتوسط.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** polyhedral loop nest optimizer, pragma, MCTS, search space, exploration, exploitation
- **Equations:** 0
- **Citations:** PolyBench, ECP proxy applications
- **Special handling:** Proper nouns (LLVM, Polly, Clang, MCTS) kept in English

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.90
- Glossary consistency: 0.89
- **Overall section score:** 0.91
