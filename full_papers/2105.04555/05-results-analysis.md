# Section 5: Results and Analysis
## القسم 5: النتائج والتحليل

**Section:** results
**Translation Quality:** 0.87
**Glossary Terms Used:** speedup, performance, configuration, pragma, tile size, parallelization, decision tree, regression, MCTS, convergence, restart, exploration, exploitation

---

### English Version

Figure 4 shows the speedup (with respect to O3P) of the best configuration found over the number of evaluations for different search methods. We observe that the customized MCTS finds high-performing configurations within few iterations (100 to 200) when compared with other search methods. Moreover, because of the restart search strategy, the MCTS is not trapped in a local solution as other search algorithms are (see gemm, 2mm, and covariance).

We investigated why Polly's heuristic was performing well on the eight kernels. We found out that there are transformations that we currently cannot do with directives but that Polly can by using its heuristics. These include unroll-and-jam, loop fusion, loop peeling except for peel(rectangular), wavefronting/skewing, index set splitting, and code motion. The Polly heuristics can also add annotations that help the LoopVectorizer do a better loop optimization.

Figure 5 shows depths of the tree at which the best configuration was found for the search methods. The MCTS finds the best configuration mostly at depth 2 or 3, while other search algorithms find depth 1 or 2. Regarding directives of the best configuration, `#pragma clang loop parallelize_thread` is included in the best configuration in most cases.

Table 2 shows a performance comparison of autotuning results on ECP proxy applications. Similar to PolyBench results, we find that our MCTS performs better than O3P, BF, GG, and RS, obtaining the highest speedup over O3P, 1.38, 8.41, and 1.20 for CoMD, miniAMR, and SW4lite, respectively.

To analyze the effectiveness of the search methods, we gathered speedups from all the algorithms and computed a cutoff based on the top 5% speedup values. We then counted the number of configurations that are above this cutoff value over the number of evaluations. Figure 6 shows the results. Besides obtaining the highest speedup configuration, MCTS finds a larger number of configurations above the cutoff value. Moreover, upon further inspection of the best configurations, we found that MCTS finds configurations that contain different pragmas for each application, namely, unrolling and array packing for CoMD, thread parallelization for miniAMR, and tiling with different size selections for SW4lite.

**4.2 Analysis**

We select the gemm kernel for further analysis. First, we employ a decision tree regression method [9] to model the relationship between the pragmas and the observed speedups. We use the resulting decision tree to understand the most important pragmas for the gemm kernel. Specifically, the pragmas that contribute to maximum variance in the speedups are placed at the top of the tree. The decision tree is implemented and visualized by using a Python library, dtreeviz. Figure 7 shows a decision tree, where we can observe that the most important pragma is `#pragma clang loop parallelize_thread`. Note that given a pragma in the tree, the right (left) of the tree means presence (absence) of the pragma. In addition, the speedup with this pragma is higher in the leaf nodes in the right part of the decision tree than in the left. In the following level of the decision tree, pragmas of different tile sizes are selected as important pragmas, while `#pragma clang loop parallelize_thread` and `#pragma clang loop tile_size(256)` emerge as important pragmas for several restarts.

Figure 8 shows the trajectory of the depth explored and the speedup obtained over the number of evaluations. We observe that the search has repetitive phases due to restart. Each phase is characterized by the random walk and the MCTS run. The random walk results in configurations with an equal number of depths. The MCTS exploits the promising configuration found in the random walk by sampling more configurations nearby. The search reaches a convergence, and a restart is performed. The effect of restart is also visible in the second phase. While the search stagnates with a speedup of 13x over the unoptimized code, restart helps MCTS find configurations with a speedup of 14x in the second phase.

We benchmarked Intel's Math Kernel Library (MKL) dgemm routine. It was implemented on the same machine as we used in our other experiments. The execution times obtained by MKL, MCTS, and O3P are 0.0056, 0.0272, and 0.1897, respectively. Even though MCTS outperforms O3P on gemm as well as other kernels, MKL's optimization obtains the fastest time for gemm since it is designed to achieve the highest performance on the Intel machine.

---

### النسخة العربية

يُظهر الشكل 4 تسريع (فيما يتعلق بـ O3P) أفضل تكوين تم العثور عليه على عدد التقييمات لطرق البحث المختلفة. نلاحظ أن MCTS المخصص يجد تكوينات عالية الأداء في تكرارات قليلة (100 إلى 200) عند مقارنتها بطرق البحث الأخرى. علاوة على ذلك، بسبب استراتيجية البحث بإعادة التشغيل، لا ينحصر MCTS في حل محلي كما تفعل خوارزميات البحث الأخرى (انظر gemm و2mm وcovariance).

حققنا في سبب أداء استدلالات Polly بشكل جيد على النوى الثمانية. اكتشفنا أن هناك تحويلات لا يمكننا القيام بها حالياً بالتوجيهات ولكن يمكن لـ Polly القيام بها باستخدام استدلالاته. تشمل هذه فك الحلقات والدمج (unroll-and-jam)، ودمج الحلقات (loop fusion)، وتقشير الحلقات باستثناء peel(rectangular)، والموجة الأمامية/الانحراف (wavefronting/skewing)، وتقسيم مجموعة الفهرس (index set splitting)، وحركة الشفرة (code motion). يمكن لاستدلالات Polly أيضاً إضافة تعليقات توضيحية تساعد LoopVectorizer في القيام بتحسين أفضل للحلقات.

يُظهر الشكل 5 أعماق الشجرة التي تم فيها العثور على أفضل تكوين لطرق البحث. يجد MCTS أفضل تكوين في الغالب عند عمق 2 أو 3، بينما تجد خوارزميات البحث الأخرى عمق 1 أو 2. فيما يتعلق بتوجيهات أفضل تكوين، يتم تضمين `#pragma clang loop parallelize_thread` في أفضل تكوين في معظم الحالات.

يُظهر الجدول 2 مقارنة أداء نتائج الضبط التلقائي على تطبيقات ECP البديلة. على غرار نتائج PolyBench، نجد أن MCTS الخاص بنا يؤدي بشكل أفضل من O3P وBF وGG وRS، ويحصل على أعلى تسريع على O3P، 1.38 و8.41 و1.20 لـ CoMD وminiAMR وSW4lite، على التوالي.

لتحليل فعالية طرق البحث، جمعنا التسريعات من جميع الخوارزميات وحسبنا عتبة قطع بناءً على أعلى 5٪ من قيم التسريع. ثم قمنا بعد عدد التكوينات التي تفوق قيمة العتبة هذه على عدد التقييمات. يُظهر الشكل 6 النتائج. بالإضافة إلى الحصول على أعلى تكوين تسريع، يجد MCTS عدداً أكبر من التكوينات فوق قيمة العتبة. علاوة على ذلك، عند المزيد من الفحص لأفضل التكوينات، وجدنا أن MCTS يجد تكوينات تحتوي على pragmas مختلفة لكل تطبيق، وهي فك الحلقات وتعبئة المصفوفة لـ CoMD، والتوازي بالخيوط لـ miniAMR، والتجزئة مع اختيارات أحجام مختلفة لـ SW4lite.

**4.2 التحليل**

نختار نواة gemm لمزيد من التحليل. أولاً، نستخدم طريقة انحدار شجرة القرار [9] لنمذجة العلاقة بين pragmas والتسريعات الملحوظة. نستخدم شجرة القرار الناتجة لفهم أهم pragmas لنواة gemm. على وجه التحديد، يتم وضع pragmas التي تساهم في أقصى تباين في التسريعات في الجزء العلوي من الشجرة. يتم تنفيذ شجرة القرار وتصويرها باستخدام مكتبة Python، dtreeviz. يُظهر الشكل 7 شجرة قرار، حيث يمكننا ملاحظة أن أهم pragma هو `#pragma clang loop parallelize_thread`. لاحظ أنه بالنسبة لـ pragma معين في الشجرة، فإن اليمين (اليسار) من الشجرة يعني وجود (عدم وجود) pragma. بالإضافة إلى ذلك، فإن التسريع بهذه pragma أعلى في العقد الورقية في الجزء الأيمن من شجرة القرار منه في اليسار. في المستوى التالي من شجرة القرار، يتم اختيار pragmas لأحجام تجزئة مختلفة كـ pragmas مهمة، بينما تظهر `#pragma clang loop parallelize_thread` و`#pragma clang loop tile_size(256)` كـ pragmas مهمة لعدة إعادات تشغيل.

يُظهر الشكل 8 مسار العمق المستكشف والتسريع الذي تم الحصول عليه على عدد التقييمات. نلاحظ أن البحث له مراحل متكررة بسبب إعادة التشغيل. تتميز كل مرحلة بالسير العشوائي وتشغيل MCTS. ينتج عن السير العشوائي تكوينات بعدد متساوٍ من الأعماق. يستغل MCTS التكوين الواعد الموجود في السير العشوائي من خلال أخذ عينات من المزيد من التكوينات القريبة. يصل البحث إلى تقارب، ويتم إجراء إعادة تشغيل. يظهر تأثير إعادة التشغيل أيضاً في المرحلة الثانية. بينما يركد البحث بتسريع 13x عن الشفرة غير المحسنة، تساعد إعادة التشغيل MCTS في إيجاد تكوينات بتسريع 14x في المرحلة الثانية.

قمنا بقياس أداء روتين dgemm من مكتبة Intel Math Kernel Library (MKL). تم تنفيذه على نفس الجهاز الذي استخدمناه في تجاربنا الأخرى. أوقات التنفيذ التي تم الحصول عليها بواسطة MKL وMCTS وO3P هي 0.0056 و0.0272 و0.1897، على التوالي. على الرغم من أن MCTS يتفوق على O3P في gemm وكذلك النوى الأخرى، إلا أن تحسين MKL يحصل على أسرع وقت لـ gemm حيث تم تصميمه لتحقيق أعلى أداء على جهاز Intel.

---

### Translation Notes

- **Figures referenced:**
  - Figure 4: Speedup of best configuration over evaluations for different search methods (6 subfigures: gemm, 2mm, durbin, floyd-warshall, adi, covariance)
  - Figure 5: Depth of best configuration found by different search methods on PolyBench kernels
  - Figure 6: Number of configurations above cutoff value over evaluations (3 subfigures: CoMD, miniAMR, SW4lite)
  - Figure 7: Decision tree visualizing relationships between pragmas and observed speedup for gemm kernel
  - Figure 8: Trajectory of depth and speedup by MCTS algorithm
- **Tables referenced:**
  - Table 2: Performance comparison on three ECP proxy applications
- **Key terms introduced:** decision tree regression, variance, cutoff value, quantile, MKL (Math Kernel Library), convergence, stagnation
- **Performance results:**
  - MCTS speedup: 2.13× average on PolyBench, 3.7× average on ECP proxy apps
  - Best PolyBench speedups: 1.01× (durbin) to 8.54× (floyd-warshall)
  - ECP speedups: CoMD (1.38×), miniAMR (8.41×), SW4lite (1.20×)
  - MCTS finds best configuration in 10/24 PolyBench kernels
- **Key insights:**
  - MCTS finds high-performing configurations quickly (100-200 iterations)
  - Restart mechanism prevents local optima
  - Best configurations typically at depth 2-3
  - Thread parallelization most important pragma
  - Different pragmas optimal for different applications
- **Citations:** [9]
- **Special handling:**
  - Pragma directives kept in English (standard syntax)
  - Kernel names preserved (gemm, CoMD, miniAMR, etc.)
  - Library names: MKL, LoopVectorizer, dtreeviz
  - Transformation names: unroll-and-jam, loop fusion, wavefronting/skewing, etc.

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
