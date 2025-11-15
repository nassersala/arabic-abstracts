# Section 2: Background on Inductive Program Synthesis
## القسم 2: خلفية عن التوليد الاستقرائي للبرامج

**Section:** Background
**Translation Quality:** 0.87
**Glossary Terms Used:** inductive program synthesis, domain-specific language, search techniques, SMT solver, constraint, enumeration, dynamic programming, genetic algorithm, ranking

---

### English Version

We begin by providing background on Inductive Program Synthesis, including a brief overview of how it is typically formulated and solved in the programming languages community.

The Inductive Program Synthesis (IPS) problem is the following: given input-output examples, produce a program that has behavior consistent with the examples.

Building an IPS system requires solving two problems. First, the search problem: to find consistent programs we need to search over a suitable set of possible programs. We need to define the set (i.e., the program space) and search procedure. Second, the ranking problem: if there are multiple programs consistent with the input-output examples, which one do we return? Both of these problems are dependent on the specifics of the problem formulation. Thus, the first important decision in formulating an approach to program synthesis is the choice of a Domain Specific Language.

**Domain Specific Languages (DSLs).** DSLs are programming languages that are suitable for a specialized domain but are more restrictive than full-featured programming languages. For example, one might disallow loops or other control flow, and only allow string data types and a small number of primitive operations like concatenation. Most of program synthesis research focuses on synthesizing programs in DSLs, because full-featured languages like C++ enlarge the search space and complicate synthesis. Restricted DSLs can also enable more efficient special-purpose search algorithms. For example, if a DSL only allows concatenations of substrings of an input string, a dynamic programming algorithm can efficiently search over all possible programs (Polozov & Gulwani, 2015). The choice of DSL also affects the difficulty of the ranking problem. For example, in a DSL without if statements, the same algorithm is applied to all inputs, reducing the number of programs consistent with any set of input-output examples, and thus the ranking problem becomes easier. Of course, the restrictiveness of the chosen DSL also determines which problems the system can solve at all.

**Search Techniques.** There are many techniques for searching for programs consistent with input-output examples. Perhaps the simplest approach is to define a grammar and then enumerate all derivations of the grammar, checking each one for consistency with the examples. This approach can be combined with pruning based on types and other logical reasoning (Feser et al., 2015). While simple, these approaches can be implemented efficiently, and they can be surprisingly effective.

In restricted domains such as the concatenation example discussed above, special-purpose algorithms can be used. FlashMeta (Polozov & Gulwani, 2015) describes a framework for DSLs which allow decomposition of the search problem, e.g., where the production of an output string from an input string can be reduced to finding a program for producing the first part of the output and concatenating it with a program for producing the latter part of the output string.

Another class of systems is based on Satisfiability Modulo Theories (SMT) solving. SMT combines SAT-style search with theories like arithmetic and inequalities, with the benefit that theory-dependent subproblems can be handled by special-purpose solvers. For example, a special-purpose solver can easily find integers x, y such that x < y and y < −100 hold, whereas an enumeration strategy may need to consider many values before satisfying the constraints. Many program synthesis engines based on SMT solvers exist, e.g., Sketch (Solar-Lezama, 2008) and Brahma (Gulwani et al., 2011). They convert the semantics of a DSL into a set of constraints between variables representing the program and the input-output values, and then call an SMT solver to find a satisfying setting of the program variables. This approach shines when special-purpose reasoning can be leveraged, but complex DSLs can lead to very large constraint problems where constructing and manipulating the constraints can be a lot slower than an enumerative approach.

Finally, stochastic local search can be employed to search over program space, and there is a long history of applying genetic algorithms to this problem. One of the most successful recent examples is the STOKE super-optimization system (Schkufza et al., 2016), which uses stochastic local search to find assembly programs that have the same semantics as an input program but execute faster.

**Ranking.** While we focus on the search problem in this work, we briefly mention the ranking problem here. A popular choice for ranking is to choose the shortest program consistent with input-output examples (Gulwani, 2016). A more sophisticated approach is employed by FlashFill (Singh & Gulwani, 2015). It works in a manner similar to max-margin structured prediction, where known ground truth programs are given, and the learning task is to assign scores to programs such that the ground truth programs score higher than other programs that satisfy the input-output specification.

---

### النسخة العربية

نبدأ بتقديم خلفية عن التوليد الاستقرائي للبرامج، بما في ذلك نظرة عامة موجزة عن كيفية صياغتها وحلها عادةً في مجتمع لغات البرمجة.

مشكلة التوليد الاستقرائي للبرامج (IPS) هي كالتالي: بالنظر إلى أمثلة الإدخال والإخراج، إنتاج برنامج يكون سلوكه متسقاً مع الأمثلة.

بناء نظام IPS يتطلب حل مشكلتين. أولاً، مشكلة البحث: لإيجاد برامج متسقة نحتاج إلى البحث عبر مجموعة مناسبة من البرامج الممكنة. نحتاج إلى تحديد المجموعة (أي فضاء البرامج) وإجراء البحث. ثانياً، مشكلة الترتيب: إذا كانت هناك برامج متعددة متسقة مع أمثلة الإدخال والإخراج، أيها نعيد؟ كلتا هاتين المشكلتين تعتمد على تفاصيل صياغة المشكلة. وبالتالي، فإن القرار الأول المهم في صياغة نهج لتوليد البرامج هو اختيار لغة خاصة بالمجال.

**اللغات الخاصة بالمجال (DSLs).** اللغات الخاصة بالمجال هي لغات برمجة مناسبة لمجال متخصص ولكنها أكثر تقييداً من لغات البرمجة كاملة الميزات. على سبيل المثال، قد يُمنع استخدام الحلقات أو تدفق التحكم الآخر، والسماح فقط بأنواع بيانات السلاسل النصية وعدد صغير من العمليات الأولية مثل السلسلة. يركز معظم أبحاث توليد البرامج على توليد البرامج في اللغات الخاصة بالمجال، لأن اللغات كاملة الميزات مثل C++ توسع فضاء البحث وتعقد التوليد. يمكن أيضاً للغات الخاصة بالمجال المقيدة أن تمكّن خوارزميات بحث أكثر كفاءة مخصصة للغرض. على سبيل المثال، إذا كانت لغة خاصة بالمجال تسمح فقط بسلسلة السلاسل الفرعية من سلسلة إدخال، فيمكن لخوارزمية البرمجة الديناميكية البحث بكفاءة عبر جميع البرامج الممكنة (Polozov و Gulwani، 2015). يؤثر اختيار اللغة الخاصة بالمجال أيضاً على صعوبة مشكلة الترتيب. على سبيل المثال، في لغة خاصة بالمجال بدون عبارات if، يتم تطبيق نفس الخوارزمية على جميع المدخلات، مما يقلل من عدد البرامج المتسقة مع أي مجموعة من أمثلة الإدخال والإخراج، وبالتالي تصبح مشكلة الترتيب أسهل. بالطبع، فإن تقييد اللغة الخاصة بالمجال المختارة يحدد أيضاً المشاكل التي يمكن للنظام حلها على الإطلاق.

**تقنيات البحث.** هناك العديد من التقنيات للبحث عن البرامج المتسقة مع أمثلة الإدخال والإخراج. ربما يكون النهج الأبسط هو تحديد قواعد نحوية ثم تعداد جميع اشتقاقات القواعد، والتحقق من كل واحدة للتناسق مع الأمثلة. يمكن دمج هذا النهج مع التقليم بناءً على الأنواع والاستدلال المنطقي الآخر (Feser وآخرون، 2015). بينما بسيطة، يمكن تنفيذ هذه النهج بكفاءة، ويمكن أن تكون فعالة بشكل مفاجئ.

في المجالات المقيدة مثل مثال السلسلة المذكور أعلاه، يمكن استخدام خوارزميات مخصصة للغرض. يصف FlashMeta (Polozov و Gulwani، 2015) إطار عمل للغات خاصة بالمجال والتي تسمح بتحلل مشكلة البحث، على سبيل المثال، حيث يمكن تقليل إنتاج سلسلة إخراج من سلسلة إدخال إلى إيجاد برنامج لإنتاج الجزء الأول من الإخراج وسلسلته مع برنامج لإنتاج الجزء الأخير من سلسلة الإخراج.

فئة أخرى من الأنظمة تستند إلى حل إشباع القيود النمطية (Satisfiability Modulo Theories - SMT). يجمع SMT بين بحث على نمط SAT مع نظريات مثل الحساب والمتباينات، مع الفائدة التي تتمثل في أن المشاكل الفرعية المعتمدة على النظرية يمكن معالجتها بواسطة حلالات مخصصة للغرض. على سبيل المثال، يمكن لحلال مخصص للغرض العثور بسهولة على الأعداد الصحيحة x، y بحيث يكون x < y و y < −100، في حين قد تحتاج استراتيجية التعداد إلى النظر في العديد من القيم قبل إرضاء القيود. توجد العديد من محركات توليد البرامج القائمة على حلالات SMT، على سبيل المثال، Sketch (Solar-Lezama، 2008) و Brahma (Gulwani وآخرون، 2011). تحوّل دلالات اللغة الخاصة بالمجال إلى مجموعة من القيود بين المتغيرات التي تمثل البرنامج وقيم الإدخال والإخراج، ثم تستدعي حلال SMT للعثور على إعداد مُرضٍ لمتغيرات البرنامج. يتألق هذا النهج عندما يمكن الاستفادة من الاستدلال المخصص للغرض، لكن اللغات الخاصة بالمجال المعقدة يمكن أن تؤدي إلى مشاكل قيود كبيرة جداً حيث يمكن أن يكون إنشاء القيود ومعالجتها أبطأ بكثير من نهج التعداد.

أخيراً، يمكن استخدام البحث المحلي العشوائي للبحث عبر فضاء البرامج، وهناك تاريخ طويل لتطبيق الخوارزميات الجينية على هذه المشكلة. أحد الأمثلة الناجحة الحديثة هو نظام التحسين الفائق STOKE (Schkufza وآخرون، 2016)، الذي يستخدم البحث المحلي العشوائي للعثور على برامج تجميع لها نفس دلالات برنامج الإدخال ولكنها تعمل بشكل أسرع.

**الترتيب.** بينما نركز على مشكلة البحث في هذا العمل، نذكر بإيجاز مشكلة الترتيب هنا. الاختيار الشائع للترتيب هو اختيار أقصر برنامج متسق مع أمثلة الإدخال والإخراج (Gulwani، 2016). يتم استخدام نهج أكثر تطوراً بواسطة FlashFill (Singh و Gulwani، 2015). يعمل بطريقة مماثلة للتنبؤ المنظم بأقصى هامش، حيث يتم إعطاء برامج الحقيقة الأرضية المعروفة، ومهمة التعلم هي تعيين درجات للبرامج بحيث تحصل برامج الحقيقة الأرضية على درجات أعلى من البرامج الأخرى التي تفي بمواصفات الإدخال والإخراج.

---

### Translation Notes

- **Key terms introduced:**
  - Domain Specific Language (DSL) = لغة خاصة بالمجال
  - search problem = مشكلة البحث
  - ranking problem = مشكلة الترتيب
  - program space = فضاء البرامج
  - Satisfiability Modulo Theories (SMT) = إشباع القيود النمطية
  - enumeration = تعداد
  - constraint = قيد
  - dynamic programming = البرمجة الديناميكية
  - genetic algorithm = الخوارزمية الجينية
  - stochastic local search = البحث المحلي العشوائي
  - max-margin structured prediction = التنبؤ المنظم بأقصى هامش

- **Figures referenced:** None
- **Equations:** Mathematical notation preserved (x < y and y < −100)
- **Citations:** Multiple references (Polozov & Gulwani, Feser et al., Solar-Lezama, Gulwani et al., Schkufza et al., Singh & Gulwani)
- **Special handling:** System names preserved in English (FlashMeta, Sketch, Brahma, STOKE, FlashFill)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
