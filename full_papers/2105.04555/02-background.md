# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** loop transformation, pragma, compiler, polyhedral, IR (intermediate representation), metadata, tile size, loop interchange, parallelization, loop unrolling, loop reversal, array packing, MCTS, UCT, exploration, exploitation

---

### English Version

In this section we first describe loop transformation pragmas implemented in LLVM Clang/Polly and our treelike search space that grows dynamically. We then provide the mathematical background and explain the algorithmic mechanism of MCTS.

**2.1 Loop transformation directives**

Loop transformation directives—in our case in the form of pragma annotations in the source code—instruct the compiler to apply a specific optimization to a loop instead of using its own profitability heuristics. If multiple transformations are applied to the same loop, the order in which they are applied is significant. For example, in the following example the loop is first tiled by using a tile size of 32; then the tiling's floor loop (the outer loop) is parallelized.

```c
#pragma clang loop parallelize_thread
#pragma clang loop sizes(32)
for(int i = 0; i < n; ++i)
    Body(i);
```

The effect of these directives becomes more evident when we explicitly expand the tiling into loops as shown below. It also illustrates that although the `parallelize_thread` textually appears before the tile directive, it is applied second because the directives apply to what is on the next line.

```c
#pragma clang loop parallelize_thread
for(int i1 = 0; i1 < n; i1 += 32) /* floor */
    for(int i2 = i1; i2 < i1 + 32 && i2 < n; ++i2) /* tile */
        Body(i2);
```

The implementation described in [29] consists of a parser component for LLVM/Clang and a loop transformer with Polly, the polyhedral loop optimizer, as illustrated in Figure 1. It is publicly available in GitHub. Clang parses the pragma directives and attaches them as metadata nodes to the loop represented in LLVM-IR. In LLVM's optimization pipeline, these are seen by Polly. Before applying the directives to the intermediate representation (IR), it first checks whether the code's semantics is preserved and rejects the transformation if it is not preserved. This step can be leveraged within autotuning to check loop transformations that produce incorrect code. The compiler has converted the input into an IR that is intended for easier processing and has implemented analyses required to detect violations to semantic constraints that are not included in the transformation search space.

As an alternative to user-directed loop transformations, Polly can use heuristics to optimize a loop nest. The heuristic used by Polly is implemented in ISL [45] using PLuTO [8]. It tries to maximize parallelism and minimize distance. Additionally, Polly applies tiling and vectorization where possible and detects code that implements matrix-matrix multiplication-like algorithms to which it applies a dedicated optimization.

**2.2 Search space**

Most autotuning frameworks and algorithms [3, 5, 38] assume that the tunable parameters can be expressed in a flat list and that the search space is composed of all possible parameter combinations. Nevertheless, the search space of composable loop transformations cannot be expressed in this way. One reason is that the search space is potentially infinite: Any transformation that results in at least one output loop can be applied an arbitrary number of times. This may often not make a lot of sense; for instance, partial unrolling twice with a tile size of four is effectively the same as unrolling with a factor of 16. We consider this domain knowledge for search space pruning. The second reason is that the loop nest structures changes after applying a transformation and therefore the set of choices is changing. As a result, tile sizes from one configuration may be unrelated to the tile sizes of another configuration since they apply to different loops.

In our trials, we use the same search space as in [31] with some additional transformations and other improvements, such as the ability to sparsely instantiate a configuration by a numeric id that does not require instantiating all sibling configurations just to know how many there are. This search space takes the form of a tree, as illustrated in Figure 2. The root node represents the configuration with no loop transformation, in other words, the original program. Every node also represents a loop nest structure to determine which transformations could be applied. The loop nest structure of the root node is determined by Clang, written to a JSON file and processed by the search space generator. Every child node then represents a choice of adding one more transformation, which results in a new configuration.

Each node/configuration represents a complete program that can be compiled and executed, and its execution time can be measured. The autotuning optimization goal is to find the configuration with the minimal execution time, namely, the best performance. As previously mentioned, however, the compiler may reject a configuration when it cannot ensure that all transformations preserve the program's semantics. In that case, the configuration has to be discarded.

The search space generator applies the following transformations to a node, some of which result in multiple loop transformations with different settings.

- **Loop tiling** (`#pragma clang loop tile`): This applies to multiple loops in a perfectly nested loop and applies all possible tile sizes from a preconfigured set. It results in twice as many loops as in the perfect loop nest. The optional clause `peel(rectangular)` instructs Polly to build a separate loop for the partial tiles, such that the complete tiles do not require conditionals.

- **Loop interchange** (`#pragma clang loop interchange`): A new configuration is derived for each permutation of its loops for each perfect loop nest.

- **Thread parallelization** (`parallelize_thread`): This parallelizes a single loop using OpenMP, creating the equivalent of `#pragma omp parallel for schedule(static)`. The reason for not using the OpenMP directive directly is that it is not composable with other loop transformations. In Clang/LLVM, OpenMP lowering is implemented in the front end (see Figure 1), whereas loop transformations are implemented by Polly. It is not possible to directly apply `#pragma omp parallel for` in the mid-end. Furthermore, the OpenMP implementation does not verify the legality of the transformation.

- **Loop unrolling** (`#pragma clang loop unrolling`): This involves fully unrolling a loop or partially unrolling by a factor from a predefined set.

- **Loop reversal** (`#pragma clang loop reverse`): This executes the iterations of loop in reverse order.

- **Array packing** (`#pragma clang loop pack`): Unlike the other directives, this is a data layout transformation. It determines the working set of array elements used in a loop and copies them into a temporary array for the duration of the loop. Polly tries to make the order of the elements in the temporary array resemble the access order. When array elements are also written in the loop, the elements are also written back to the original array. The transformation is most useful either to make the loop's working set fit into a closer cache in the memory hierarchy or to transpose a matrix to make its accesses consecutive within the loop.

**2.3 Monte Carlo tree search**

Monte Carlo tree search (MCTS) is a heuristic search method that seeks to solve a class of computationally intractable sequential decision-making problems, typically represented by trees. In these trees, a node represents a state (decision) in the sequential decision-making process, and the directed edges represent sequential transitions from one state to another. MCTS is an iterative approach that performs four phases at each iteration: selection, expansion, simulation, and backpropagation (see Figure 3 for an illustration).

The selection phase traverses only the part of the tree that was already visited. It starts from the root node and selects the next node according to a tree policy. It typically ends in a leaf node of a visited tree. The expansion phase expands the tree by considering children nodes of the ending leaf node of the previous phase and selects one from among them. The simulation phase performs simulations for the new node by visiting subsequent nodes that can be reached from the new node. Typically, this involves several random walks from the new node to various terminal nodes that have outcomes. Based on these outcomes, the reward for each explored random walk is computed starting from the root node. The backpropagation phase propagates the path-specific reward back to the nodes in the given path from the terminal node to the root node. Consequently, the nodes that are common in the high reward branches get reinforced and have a high probability of getting selected in the subsequent iterations.

The tree policy used in the selection phase plays a critical role in balancing the exploration of the search space and the exploitation of the already-found promising regions in the search space. A widely used policy is Upper Confidence Bounds applied to Trees (UCT) [4, 28], where a child node $j$ is selected to maximize

$$UCT(j) = \bar{r}_j + C \sqrt{\frac{2\ln n}{n_j}}$$

where $\bar{r}_j$ is the average reward of the node $j$, $n$ is the number of times the current (parent) node has been visited, $n_j$ is the number of times child $j$ has been visited, and $C$ is a constant to balance the exploration and exploitation. The reward range is $[0,1]$ [10].

---

### النسخة العربية

في هذا القسم نصف أولاً توجيهات pragma لتحويل الحلقات المنفذة في LLVM Clang/Polly وفضاء البحث الشجري الذي ينمو ديناميكياً. ثم نقدم الخلفية الرياضية ونشرح الآلية الخوارزمية لـ MCTS.

**2.1 توجيهات تحويل الحلقات**

توجيهات تحويل الحلقات - في حالتنا على شكل تعليقات pragma في الشفرة المصدرية - تُوجّه المترجم لتطبيق تحسين معين على حلقة بدلاً من استخدام استدلالات الربحية الخاصة به. إذا تم تطبيق عدة تحويلات على نفس الحلقة، فإن الترتيب الذي يتم تطبيقها فيه مهم. على سبيل المثال، في المثال التالي يتم أولاً تجزئة الحلقة باستخدام حجم تجزئة 32؛ ثم يتم جعل حلقة الأرضية للتجزئة (الحلقة الخارجية) متوازية.

```c
#pragma clang loop parallelize_thread
#pragma clang loop sizes(32)
for(int i = 0; i < n; ++i)
    Body(i);
```

يصبح تأثير هذه التوجيهات أكثر وضوحاً عندما نوسع التجزئة صراحة إلى حلقات كما هو موضح أدناه. يوضح أيضاً أنه على الرغم من أن `parallelize_thread` يظهر نصياً قبل توجيه tile، إلا أنه يُطبق ثانياً لأن التوجيهات تنطبق على ما هو موجود في السطر التالي.

```c
#pragma clang loop parallelize_thread
for(int i1 = 0; i1 < n; i1 += 32) /* أرضية */
    for(int i2 = i1; i2 < i1 + 32 && i2 < n; ++i2) /* تجزئة */
        Body(i2);
```

يتكون التنفيذ الموصوف في [29] من مكون محلل لـ LLVM/Clang ومحول حلقات مع Polly، محسِّن الحلقات متعدد السطوح، كما هو موضح في الشكل 1. وهو متاح للجمهور في GitHub. يقوم Clang بتحليل توجيهات pragma ويرفقها كعقد بيانات وصفية للحلقة الممثلة في LLVM-IR. في خط تحسين LLVM، تُرى هذه بواسطة Polly. قبل تطبيق التوجيهات على التمثيل الوسيط (IR)، يتحقق أولاً مما إذا كانت دلالات الشفرة محفوظة ويرفض التحويل إذا لم يتم حفظها. يمكن الاستفادة من هذه الخطوة ضمن الضبط التلقائي للتحقق من تحويلات الحلقات التي تنتج شفرة غير صحيحة. قام المترجم بتحويل المدخلات إلى IR مصمم لمعالجة أسهل ونفذ التحليلات المطلوبة لاكتشاف الانتهاكات للقيود الدلالية التي لا تدخل في فضاء بحث التحويل.

كبديل لتحويلات الحلقات الموجهة بواسطة المستخدم، يمكن لـ Polly استخدام استدلالات لتحسين عش الحلقة. يتم تنفيذ الاستدلال المستخدم بواسطة Polly في ISL [45] باستخدام PLuTo [8]. يحاول زيادة التوازي إلى الحد الأقصى وتقليل المسافة. بالإضافة إلى ذلك، يطبق Polly التجزئة والتمتيه حيثما أمكن ويكتشف الشفرة التي تنفذ خوارزميات شبيهة بضرب المصفوفات التي يطبق عليها تحسيناً مخصصاً.

**2.2 فضاء البحث**

تفترض معظم أطر عمل وخوارزميات الضبط التلقائي [3, 5, 38] أنه يمكن التعبير عن المعاملات القابلة للضبط في قائمة مسطحة وأن فضاء البحث يتكون من جميع مجموعات المعاملات الممكنة. ومع ذلك، لا يمكن التعبير عن فضاء البحث لتحويلات الحلقات القابلة للتركيب بهذه الطريقة. أحد الأسباب هو أن فضاء البحث قد يكون لا نهائياً: يمكن تطبيق أي تحويل ينتج عنه حلقة إخراج واحدة على الأقل عدداً تعسفياً من المرات. قد لا يكون هذا منطقياً في كثير من الأحيان؛ على سبيل المثال، فك الحلقات الجزئي مرتين بحجم تجزئة أربعة هو فعلياً نفس الفك بعامل 16. نعتبر هذا معرفة مجالية لتقليم فضاء البحث. السبب الثاني هو أن هياكل عش الحلقة تتغير بعد تطبيق تحويل وبالتالي تتغير مجموعة الاختيارات. ونتيجة لذلك، قد لا ترتبط أحجام التجزئة من تكوين واحد بأحجام التجزئة لتكوين آخر لأنها تنطبق على حلقات مختلفة.

في تجاربنا، نستخدم نفس فضاء البحث كما في [31] مع بعض التحويلات الإضافية والتحسينات الأخرى، مثل القدرة على إنشاء تكوين بشكل متناثر بمعرف رقمي لا يتطلب إنشاء جميع التكوينات الشقيقة فقط لمعرفة عددها. يأخذ فضاء البحث هذا شكل شجرة، كما هو موضح في الشكل 2. تمثل العقدة الجذر التكوين بدون تحويل حلقة، بمعنى آخر، البرنامج الأصلي. تمثل كل عقدة أيضاً هيكل عش حلقة لتحديد التحويلات التي يمكن تطبيقها. يتم تحديد هيكل عش الحلقة للعقدة الجذر بواسطة Clang، ويُكتب في ملف JSON وتتم معالجته بواسطة مولد فضاء البحث. تمثل كل عقدة فرعية بعد ذلك اختيار إضافة تحويل آخر، مما ينتج عنه تكوين جديد.

تمثل كل عقدة/تكوين برنامجاً كاملاً يمكن تجميعه وتنفيذه، ويمكن قياس وقت تنفيذه. هدف تحسين الضبط التلقائي هو إيجاد التكوين بأقل وقت تنفيذ، أي أفضل أداء. كما ذكرنا سابقاً، قد يرفض المترجم تكويناً عندما لا يمكنه التأكد من أن جميع التحويلات تحفظ دلالات البرنامج. في هذه الحالة، يجب التخلص من التكوين.

يطبق مولد فضاء البحث التحويلات التالية على عقدة، بعضها ينتج عنه عدة تحويلات حلقة بإعدادات مختلفة.

- **تجزئة الحلقة** (`#pragma clang loop tile`): ينطبق هذا على حلقات متعددة في حلقة متداخلة بشكل مثالي ويطبق جميع أحجام التجزئة الممكنة من مجموعة مكونة مسبقاً. ينتج عنه ضعف عدد الحلقات كما في عش الحلقة المثالي. يُوجّه البند الاختياري `peel(rectangular)` Polly لبناء حلقة منفصلة للتجزئات الجزئية، بحيث لا تتطلب التجزئات الكاملة شروط.

- **تبديل الحلقة** (`#pragma clang loop interchange`): يتم اشتقاق تكوين جديد لكل تباديل لحلقاته لكل عش حلقة مثالي.

- **التوازي بالخيوط** (`parallelize_thread`): يجعل هذا حلقة واحدة متوازية باستخدام OpenMP، مما ينشئ ما يعادل `#pragma omp parallel for schedule(static)`. سبب عدم استخدام توجيه OpenMP مباشرة هو أنه غير قابل للتركيب مع تحويلات الحلقات الأخرى. في Clang/LLVM، يتم تنفيذ خفض OpenMP في الواجهة الأمامية (انظر الشكل 1)، بينما يتم تنفيذ تحويلات الحلقات بواسطة Polly. من غير الممكن تطبيق `#pragma omp parallel for` مباشرة في الطرف الأوسط. علاوة على ذلك، لا يتحقق تنفيذ OpenMP من شرعية التحويل.

- **فك الحلقات** (`#pragma clang loop unrolling`): يتضمن هذا فك حلقة بالكامل أو فكها جزئياً بعامل من مجموعة محددة مسبقاً.

- **عكس الحلقة** (`#pragma clang loop reverse`): ينفذ هذا تكرارات الحلقة بترتيب عكسي.

- **تعبئة المصفوفة** (`#pragma clang loop pack`): على عكس التوجيهات الأخرى، هذا تحويل لتخطيط البيانات. يحدد مجموعة العمل لعناصر المصفوفة المستخدمة في حلقة وينسخها إلى مصفوفة مؤقتة لمدة الحلقة. يحاول Polly جعل ترتيب العناصر في المصفوفة المؤقتة يشبه ترتيب الوصول. عندما تُكتب عناصر المصفوفة أيضاً في الحلقة، تُكتب العناصر أيضاً مرة أخرى إلى المصفوفة الأصلية. يكون التحويل مفيداً للغاية إما لجعل مجموعة عمل الحلقة تناسب ذاكرة تخزين مؤقت أقرب في التسلسل الهرمي للذاكرة أو لنقل مصفوفة لجعل وصولاتها متتالية داخل الحلقة.

**2.3 بحث شجرة مونت كارلو**

بحث شجرة مونت كارلو (MCTS) هو طريقة بحث استدلالية تسعى لحل فئة من مشاكل اتخاذ القرار المتسلسل المعقدة حسابياً، والتي تُمثل عادة بأشجار. في هذه الأشجار، تمثل العقدة حالة (قرار) في عملية اتخاذ القرار المتسلسل، وتمثل الحواف الموجهة انتقالات متسلسلة من حالة إلى أخرى. MCTS هو نهج تكراري ينفذ أربع مراحل في كل تكرار: الاختيار، والتوسع، والمحاكاة، والانتشار العكسي (انظر الشكل 3 للتوضيح).

تجتاز مرحلة الاختيار فقط الجزء من الشجرة الذي تمت زيارته بالفعل. تبدأ من العقدة الجذر وتختار العقدة التالية وفقاً لسياسة الشجرة. عادة ما تنتهي في عقدة ورقة من شجرة تمت زيارتها. تقوم مرحلة التوسع بتوسيع الشجرة من خلال النظر في العقد الفرعية للعقدة الورقة النهائية للمرحلة السابقة وتختار واحدة من بينها. تنفذ مرحلة المحاكاة محاكاة للعقدة الجديدة من خلال زيارة العقد اللاحقة التي يمكن الوصول إليها من العقدة الجديدة. عادة، يتضمن هذا عدة سيرات عشوائية من العقدة الجديدة إلى عقد طرفية مختلفة لها نتائج. بناءً على هذه النتائج، يتم حساب المكافأة لكل سير عشوائي مستكشف بدءاً من العقدة الجذر. تنشر مرحلة الانتشار العكسي المكافأة الخاصة بالمسار إلى العقد في المسار المحدد من العقدة الطرفية إلى العقدة الجذر. وبالتالي، تحصل العقد المشتركة في الفروع ذات المكافآت العالية على تعزيز ولديها احتمالية عالية للاختيار في التكرارات اللاحقة.

تلعب سياسة الشجرة المستخدمة في مرحلة الاختيار دوراً حاسماً في موازنة استكشاف فضاء البحث واستغلال المناطق الواعدة التي تم العثور عليها بالفعل في فضاء البحث. السياسة المستخدمة على نطاق واسع هي حدود الثقة العليا المطبقة على الأشجار (UCT) [4, 28]، حيث يتم اختيار العقدة الفرعية $j$ لتعظيم

$$UCT(j) = \bar{r}_j + C \sqrt{\frac{2\ln n}{n_j}}$$

حيث $\bar{r}_j$ هي متوسط المكافأة للعقدة $j$، و$n$ هو عدد مرات زيارة العقدة الحالية (الأب)، و$n_j$ هو عدد مرات زيارة الابن $j$، و$C$ هو ثابت لموازنة الاستكشاف والاستغلال. نطاق المكافأة هو $[0,1]$ [10].

---

### Translation Notes

- **Figures referenced:** Figure 1 (Clang/LLVM compiler architecture), Figure 2 (Example of loop transformation search space), Figure 3 (Four phases of MCTS)
- **Key terms introduced:** pragma directives, loop tiling, loop interchange, thread parallelization, loop unrolling, loop reversal, array packing, MCTS phases (selection, expansion, simulation, backpropagation), UCT, tree policy
- **Equations:** 1 (UCT formula)
- **Citations:** [3], [4], [5], [8], [10], [28], [29], [31], [38], [45]
- **Special handling:**
  - Code examples preserved in English with Arabic comments
  - Mathematical formula kept in LaTeX notation
  - Proper nouns: LLVM, Polly, Clang, OpenMP, ISL, PLuTo, UCT
  - Technical terms: pragma, IR, JSON, GitHub

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
