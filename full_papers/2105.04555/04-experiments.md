# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** benchmark, kernel, proxy application, loop transformation, tile size, unroll factor, parallelization, compiler optimization, search space, MCTS, greedy, breadth-first search

---

### English Version

We use the PolyBench 4.2 [47] benchmark test suite and ECP proxy applications to evaluate our customized MCTS method. PolyBench consists of 30 numerical computations extracted from various application domains. It covers kernels that include 19 linear algebra computations, 3 image-processing applications, 6 physics simulations, and 2 data-mining processes. We selected 24 kernels with the most levels of nested loops. They are as follows:

**Linear Algebra:**
- BLAS (7): gemm, gemver, gesummv, symm, syr2k, syrk, trmm
- Kernels (6): 2mm, 3mm, atax, bicg, doitgen, mvt
- Solvers (3): durbin, lu, ludcmp

**Medley (image processing) (2):** floyd-warshall, nussinov

**Physics simulation (stencils) (5):** adi, fdtd-2d, jacobi-1d, jacobi-2d, seidel-2d

**Data mining (1):** covariance

We use CoMD, miniAMR, and SW4lite from the ECP proxy applications suite. CoMD is a reference implementation for algorithms used in molecular dynamics; miniAMR implements a basic adaptive mesh refinement method that is often used in physical simulations; and SW4lite is a bare-bones version of the larger SW4 application intended for testing performance optimizations in SW4's most important numerical kernels.

Because of loop distribution, we manually applied loop transformation to increase the number of perfectly nested loops and thus the number of possible transformations such as tiling. That is, we split independent computations in a loop body into two or more separate loops. The kernels from the ECP proxy applications also needed to be customized in order to make them transformable by Polly.

We compared our customized MCTS method with the following search methods.

**Polly compile-time heuristics (O3P):** This is a baseline without autotuning. It uses Clang's highest optimization level -O3 with Polly's optimization heuristic enabled. Additional command line flags are `-march=native -mllvm -polly-position=early -mllvm -polly-parallel -mllvm -polly-omp-backend=LLVM -mllvm -polly-scheduling=static` that tune the machine code for the target and also enable Polly's auto-parallelizer.

**Random search (RS):** It samples each configuration randomly, wherein a depth is selected at random and a random walk is performed for the selected depth in the search tree.

**Breadth first (BF):** This is the commonly used breadth-first search method.

**Global greedy (GG):** This is a greedy algorithm proposed in [31] for treelike search spaces. For a given node, it evaluates all its children and adds them to a priority queue, starting with the root node. The queue is sorted with the most promising configurations first to be expanded next. We refer the reader to [31] for a detailed exposition of this method.

The experiments were conducted on a Linux machine with 2x Intel Xeon Platinum 8180M CPU @ 2.50 GHz with 384 GB RAM memory; GCC 9.2.0; and Clang 13.0.0 with Polly. The search space includes six loop transformations: loop tiling, loop interchange, thread parallelization, loop unrolling, loop reversal, and array packing. The possible tile sizes are 2, 3, 4, 5, 8, 16, 32, 64, 128, and 256. The choices for unroll factors are 2, 4, and 8. Each configuration was executed five times, and the median of the five was selected as the execution time for the configuration to minimize the impact of noise. We used the execution time measured by PolyBench itself using the `-DPOLYBENCH_TIME` preprocessor option. This measures only the kernel execution time and excludes overhead such as executable startup time and array initialization. All the search methods except O3P were allowed to run for a wall-clock time of six hours or until 1,000 unique configurations were evaluated. For MCTS, we used an exploration weight of 0.1 and $q$ of 0.05. Since the first phase does exploration, a relatively small value of exploration weight was selected such that the second phase focused on the exploitation. In the search experiments, $d_{\max}$ is set to five based on a preliminary experiment on depth. Specifically, we found that most of the configurations with the depth value greater than 5 fail to compile or result in code transformation errors. We limit each MCTS run to 300 evaluations. The convergence in the search is detected by lack of improvements for 50 iterations or visiting the same configuration for 10 iterations in a row.

**4.1 Comparison between search methods**

Table 1 shows the comparison of different search methods. For a given kernel, the speedup is given by the ratio of runtimes of the O3P and the best configuration obtained by the search method. We observe that the MCTS obtains better performance than the O3P on 16 out of 24 kernels (speedup values greater than 1). The observed speedups range from 1.01 (durbin) to 8.54 (floyd-warshall). The BF, GG, and RS outperform the O3P only on 8, 11, and 11 kernels, respectively. The average speedups over O3P on 24 kernels are 2.13, 1.42, 1.38, and 1.04 for MCTS, GG, RS, and BF, respectively. Moreover, we observe that MCTS obtains the best speedup values for 10 out of 24 kernels (boldfaced for each kernel). The GG, BF, and RS methods obtain the best speedup values for 4, 1, and 1 kernels, respectively. On 8 kernels, none of the search methods was able to outperform O3P (italicized in the table).

---

### النسخة العربية

نستخدم مجموعة معايير اختبار PolyBench 4.2 [47] وتطبيقات ECP البديلة لتقييم طريقة MCTS المخصصة الخاصة بنا. تتكون PolyBench من 30 حساباً رقمياً مستخرجاً من مجالات تطبيق مختلفة. تغطي نوى تتضمن 19 حساباً للجبر الخطي، و3 تطبيقات لمعالجة الصور، و6 محاكيات فيزيائية، وعمليتين لاستخراج البيانات. اخترنا 24 نواة بأكبر عدد من مستويات الحلقات المتداخلة. هم كما يلي:

**الجبر الخطي:**
- BLAS (7): gemm, gemver, gesummv, symm, syr2k, syrk, trmm
- النوى (6): 2mm, 3mm, atax, bicg, doitgen, mvt
- الحلالين (3): durbin, lu, ludcmp

**مشكلات متنوعة (معالجة الصور) (2):** floyd-warshall, nussinov

**محاكاة الفيزياء (القوالب) (5):** adi, fdtd-2d, jacobi-1d, jacobi-2d, seidel-2d

**استخراج البيانات (1):** covariance

نستخدم CoMD وminiAMR وSW4lite من مجموعة تطبيقات ECP البديلة. CoMD هو تنفيذ مرجعي للخوارزميات المستخدمة في الديناميكيات الجزيئية؛ ينفذ miniAMR طريقة تنقيح شبكة تكيفية أساسية تُستخدم غالباً في المحاكيات الفيزيائية؛ وSW4lite هو نسخة أساسية من تطبيق SW4 الأكبر المخصصة لاختبار تحسينات الأداء في النوى الرقمية الأكثر أهمية لـ SW4.

بسبب توزيع الحلقات، طبقنا يدوياً تحويل الحلقات لزيادة عدد الحلقات المتداخلة بشكل مثالي وبالتالي عدد التحويلات الممكنة مثل التجزئة. أي أننا قسمنا الحسابات المستقلة في جسم الحلقة إلى حلقتين منفصلتين أو أكثر. احتاجت النوى من تطبيقات ECP البديلة أيضاً إلى تخصيص من أجل جعلها قابلة للتحويل بواسطة Polly.

قارنا طريقة MCTS المخصصة الخاصة بنا بطرق البحث التالية.

**استدلالات وقت التجميع لـ Polly (O3P):** هذا خط أساس بدون ضبط تلقائي. يستخدم أعلى مستوى تحسين لـ Clang -O3 مع تمكين استدلالات تحسين Polly. علامات سطر الأوامر الإضافية هي `-march=native -mllvm -polly-position=early -mllvm -polly-parallel -mllvm -polly-omp-backend=LLVM -mllvm -polly-scheduling=static` التي تضبط شفرة الآلة للهدف وتمكن أيضاً الموازي التلقائي لـ Polly.

**البحث العشوائي (RS):** يأخذ عينات من كل تكوين بشكل عشوائي، حيث يتم اختيار عمق عشوائياً ويتم إجراء سير عشوائي للعمق المحدد في شجرة البحث.

**البحث بالعرض أولاً (BF):** هذه طريقة البحث بالعرض أولاً الشائعة الاستخدام.

**الجشع العالمي (GG):** هذه خوارزمية جشعة مقترحة في [31] لفضاءات البحث الشجرية. بالنسبة لعقدة معينة، يقيّم جميع أبنائها ويضيفهم إلى قائمة انتظار الأولوية، بدءاً من العقدة الجذر. يتم فرز القائمة بالتكوينات الأكثر واعدة أولاً ليتم توسيعها بعد ذلك. نحيل القارئ إلى [31] للحصول على عرض تفصيلي لهذه الطريقة.

تم إجراء التجارب على جهاز Linux بمعالج Intel Xeon Platinum 8180M @ 2.50 GHz مزدوج مع ذاكرة RAM بسعة 384 جيجابايت؛ وGCC 9.2.0؛ وClang 13.0.0 مع Polly. يتضمن فضاء البحث ستة تحويلات للحلقات: تجزئة الحلقة، وتبديل الحلقة، والتوازي بالخيوط، وفك الحلقات، وعكس الحلقة، وتعبئة المصفوفة. أحجام التجزئة الممكنة هي 2، 3، 4، 5، 8، 16، 32، 64، 128، و256. خيارات عوامل الفك هي 2، 4، و8. تم تنفيذ كل تكوين خمس مرات، وتم اختيار متوسط الخمسة كوقت تنفيذ للتكوين لتقليل تأثير الضوضاء. استخدمنا وقت التنفيذ المقاس بواسطة PolyBench نفسها باستخدام خيار المعالج المسبق `-DPOLYBENCH_TIME`. يقيس هذا وقت تنفيذ النواة فقط ويستبعد النفقات العامة مثل وقت بدء التشغيل القابل للتنفيذ وتهيئة المصفوفة. سُمح لجميع طرق البحث باستثناء O3P بالعمل لمدة ست ساعات من وقت الحائط أو حتى يتم تقييم 1,000 تكوين فريد. بالنسبة لـ MCTS، استخدمنا وزن استكشاف 0.1 و$q$ من 0.05. نظراً لأن المرحلة الأولى تقوم بالاستكشاف، تم اختيار قيمة صغيرة نسبياً لوزن الاستكشاف بحيث تركز المرحلة الثانية على الاستغلال. في تجارب البحث، يتم تعيين $d_{\max}$ إلى خمسة بناءً على تجربة أولية على العمق. على وجه التحديد، وجدنا أن معظم التكوينات ذات قيمة العمق الأكبر من 5 تفشل في التجميع أو تؤدي إلى أخطاء تحويل الشفرة. نحد كل تشغيل MCTS إلى 300 تقييم. يتم اكتشاف التقارب في البحث من خلال عدم وجود تحسينات لمدة 50 تكراراً أو زيارة نفس التكوين لمدة 10 تكرارات متتالية.

**4.1 المقارنة بين طرق البحث**

يظهر الجدول 1 مقارنة طرق البحث المختلفة. بالنسبة لنواة معينة، يُعطى التسريع بنسبة أوقات تشغيل O3P وأفضل تكوين تم الحصول عليه بواسطة طريقة البحث. نلاحظ أن MCTS يحصل على أداء أفضل من O3P في 16 من أصل 24 نواة (قيم تسريع أكبر من 1). تتراوح التسريعات الملحوظة من 1.01 (durbin) إلى 8.54 (floyd-warshall). يتفوق BF وGG وRS على O3P فقط في 8 و11 و11 نواة، على التوالي. متوسط التسريعات على O3P على 24 نواة هي 2.13، 1.42، 1.38، و1.04 لـ MCTS، GG، RS، وBF، على التوالي. علاوة على ذلك، نلاحظ أن MCTS يحصل على أفضل قيم تسريع لـ 10 من أصل 24 نواة (مكتوبة بخط عريض لكل نواة). تحصل طرق GG وBF وRS على أفضل قيم تسريع لـ 4 و1 و1 نواة، على التوالي. في 8 نوى، لم تتمكن أي من طرق البحث من التفوق على O3P (مكتوبة بخط مائل في الجدول).

---

### Translation Notes

- **Figures referenced:** None in this section
- **Tables referenced:** Table 1 (Performance comparison on 24 PolyBench kernels) - mentioned but not shown in this section
- **Key terms introduced:** PolyBench, ECP proxy applications, BLAS kernels, stencil computations, adaptive mesh refinement, molecular dynamics, breadth-first search, greedy algorithm, priority queue
- **Benchmarks:**
  - PolyBench: 24 kernels from linear algebra, image processing, physics simulation, and data mining
  - ECP proxy apps: CoMD, miniAMR, SW4lite
- **Experimental setup:**
  - Hardware: 2x Intel Xeon Platinum 8180M @ 2.50 GHz, 384 GB RAM
  - Compilers: GCC 9.2.0, Clang 13.0.0 with Polly
  - Search space: 6 transformations with varying tile sizes (2-256) and unroll factors (2,4,8)
  - Time budget: 6 hours or 1,000 configurations
  - MCTS parameters: exploration weight 0.1, q=0.05, d_max=5, 300 evaluations per run
- **Citations:** [31], [47]
- **Special handling:**
  - Kernel names kept in English as they are standard benchmark names
  - Compiler flags preserved as-is
  - Proper nouns: PolyBench, ECP, CoMD, miniAMR, SW4lite, Intel Xeon, GCC, Clang, Polly, OpenMP

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
