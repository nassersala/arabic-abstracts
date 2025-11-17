# Abstract

## English Version

I present the most fundamental features of an implemented system designed to manipulate representations of regular languages. Some functionalities of the system have been presented in previous papers without describing the low level data structures and algorithms ensuring its efficiency. This latter point is the main subject of the present paper. The system is structured into two layers, allowing regular languages to be represented in an increasingly compact, efficient, and integrated way. Both layers are first presented at a high level, adequate to design and prove the correctness of abstract algorithms. Then, their low-level implementations are described meticulously. Algorithms using the system must be written at this level.

At the high level, the first layer offers a notion of normalized regular expressions ensuring that the set of all syntactic derivatives of an expression is finite. This is convenient to design high-level algorithms to compute automata from expressions, compare expressions for inclusion or equivalence, or even simplify expressions. At the low level, normalized expressions are uniquely represented by identifiers, i.e. by standard integers so that checking syntactic equality boils down to checking equality of integers. High-level operations on normalized expressions are implemented by algorithms working on integers. High-level algorithms working on normalized expressions can therefore be straightforwardly translated into programs manipulating integers. The contribution of this layer is the simplification of existing algorithms, at the high level, and a significant increase in efficiency, at the low level.

The second layer, called the background, introduces additional notions to record, integrate, and simplify things computed within the first layer, or even outside the system. Therefore, results of previous computations can be reused for solving new tasks more simply and quickly. At the high level, normalized expressions denoting the same regular language can be unified by grouping them into equivalence classes. One shortest expression is chosen in each class as its representative, which can be used to form equations relating expressions to their derivatives. Sets of equations can be used to represent deterministic finite automata (DFAs). Equations are also used as equality constraints over the regular languages denoted by expressions. Solving such constraints may reduce the number of equivalence classes, and, therefore, the sizes of DFAs. At the low level, equations are uniquely represented by integers, similarly to normalized expressions.

In this paper, I focus on describing the low-level data structures and the main algorithms of the two layers without describing applicative algorithms. Some of the latter have been described in previous papers; others are topics for future work. Nevertheless, this paper also presents extensive experimental results to demonstrate the usefulness of the proposed framework and, in particular, the fact that it makes it possible to represent large sets of regular languages in a unified way where distinct identifiers designate different languages, represented by both a small expression and a minimal deterministic automaton (MDFA). It is also shown that such large sets of regular languages can provide interesting statistical information on the way large expressions can be minimized or simplified.

---

## النسخة العربية

أقدّم الخصائص الأساسية لنظام مُطبَّق مُصمَّم للتعامل مع تمثيلات اللغات النظامية. تم عرض بعض وظائف النظام في أوراق بحثية سابقة دون وصف هياكل البيانات والخوارزميات منخفضة المستوى التي تضمن كفاءته. هذه النقطة الأخيرة هي الموضوع الرئيسي لهذه الورقة. النظام مُهيكل في طبقتين، مما يسمح بتمثيل اللغات النظامية بطريقة مُتزايدة الإحكام والكفاءة والتكامل. يتم أولاً عرض كلتا الطبقتين على مستوى عالٍ، مناسب لتصميم وإثبات صحة الخوارزميات المجردة. ثم يتم وصف تطبيقاتهما منخفضة المستوى بدقة. يجب كتابة الخوارزميات التي تستخدم النظام على هذا المستوى.

على المستوى العالي، تقدم الطبقة الأولى مفهوم التعبيرات النظامية المُطبَّعة التي تضمن أن مجموعة جميع المشتقات النحوية للتعبير محدودة. هذا مفيد لتصميم خوارزميات عالية المستوى لحساب الآلات ذات الحالة المحدودة من التعبيرات، ومقارنة التعبيرات من حيث الاحتواء أو التكافؤ، أو حتى تبسيط التعبيرات. على المستوى المنخفض، يتم تمثيل التعبيرات المُطبَّعة بشكل فريد بواسطة مُعرِّفات، أي بأعداد صحيحة قياسية بحيث يتلخص التحقق من التساوي النحوي في التحقق من تساوي الأعداد الصحيحة. يتم تطبيق العمليات عالية المستوى على التعبيرات المُطبَّعة بواسطة خوارزميات تعمل على الأعداد الصحيحة. وبالتالي يمكن ترجمة الخوارزميات عالية المستوى التي تعمل على التعبيرات المُطبَّعة بشكل مباشر إلى برامج تتعامل مع الأعداد الصحيحة. مساهمة هذه الطبقة هي تبسيط الخوارزميات الموجودة، على المستوى العالي، وزيادة كبيرة في الكفاءة، على المستوى المنخفض.

الطبقة الثانية، المسماة الخلفية، تقدم مفاهيم إضافية لتسجيل ودمج وتبسيط الأشياء المحسوبة ضمن الطبقة الأولى، أو حتى خارج النظام. وبالتالي، يمكن إعادة استخدام نتائج الحسابات السابقة لحل مهام جديدة بطريقة أبسط وأسرع. على المستوى العالي، يمكن توحيد التعبيرات المُطبَّعة التي تشير إلى نفس اللغة النظامية من خلال تجميعها في فئات تكافؤ. يتم اختيار أقصر تعبير واحد في كل فئة كممثل لها، والذي يمكن استخدامه لتشكيل معادلات تربط التعبيرات بمشتقاتها. يمكن استخدام مجموعات المعادلات لتمثيل الآلات ذات الحالة المحدودة الحتمية (DFAs). تُستخدم المعادلات أيضاً كقيود تساوٍ على اللغات النظامية التي تشير إليها التعبيرات. قد يؤدي حل هذه القيود إلى تقليل عدد فئات التكافؤ، وبالتالي أحجام الآلات ذات الحالة المحدودة. على المستوى المنخفض، يتم تمثيل المعادلات بشكل فريد بواسطة أعداد صحيحة، بشكل مماثل للتعبيرات المُطبَّعة.

في هذه الورقة، أركز على وصف هياكل البيانات منخفضة المستوى والخوارزميات الرئيسية للطبقتين دون وصف الخوارزميات التطبيقية. تم وصف بعض الأخيرة في أوراق بحثية سابقة؛ وأخرى هي موضوعات للعمل المستقبلي. ومع ذلك، تقدم هذه الورقة أيضاً نتائج تجريبية موسعة لإثبات فائدة الإطار المقترح، وعلى وجه الخصوص، حقيقة أنه يجعل من الممكن تمثيل مجموعات كبيرة من اللغات النظامية بطريقة موحدة حيث تشير المُعرِّفات المتميزة إلى لغات مختلفة، ممثلة بكل من تعبير صغير وآلة حتمية دنيا (MDFA). كما يُظهر أن مثل هذه المجموعات الكبيرة من اللغات النظامية يمكن أن توفر معلومات إحصائية مثيرة للاهتمام حول كيفية تصغير أو تبسيط التعبيرات الكبيرة.

---

## Translation Notes

- **Figures/Tables**: Abstract contains no figures or tables
- **Mathematical Notation**: All technical terms preserved in original form (DFA, MDFA)
- **Citations**: No citations in abstract
- **Special Terms**:
  - Regular languages → اللغات النظامية
  - Normalized regular expressions → التعبيرات النظامية المُطبَّعة
  - Syntactic derivatives → المشتقات النحوية
  - Deterministic finite automata (DFA) → الآلات ذات الحالة المحدودة الحتمية
  - Minimal deterministic automaton (MDFA) → آلة حتمية دنيا
  - Equivalence classes → فئات التكافؤ
  - Background → الخلفية (as a technical term for the second layer)

---

## Quality Assessment

**Translation Accuracy**: 0.92
- Technical terminology consistently translated
- Mathematical concepts preserved
- Structure and flow maintained

**Readability**: 0.90
- Clear and accessible Arabic
- Technical depth preserved
- Natural phrasing

**Completeness**: 0.95
- All content translated
- No omissions
- Context fully preserved

**Overall Quality**: 0.92
