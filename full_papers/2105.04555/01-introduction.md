# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** compiler, loop optimization, loop transformation, autotuning, domain-specific language, pragma, polyhedral, LLVM, Polly, Clang, MCTS, search space

---

### English Version

Most compute-intensive programs, in particular scientific applications in high-performance computing, spend a significant amount of execution time in loops, thus making them the prime target for performance optimizations. Common strategies include replacing them by vendor-provided library calls (such as for BLAS [32] or FFT [14]). However, these are available only for a limited set of kernels, which require the use of a specific data layout in memory and may not be available on all platforms. Therefore, researchers have inevitably sought to optimize the loops in the application itself.

Unfortunately, manual optimization is a time-consuming process that requires intimate knowledge about the target hardware and often results in less maintainable code. Code generators promise solutions by automatically optimizing the synthesized code [18] from a domain-specific problem description but specialized for specific kinds of algorithms, such as LIFT [40] for BLAS and SPIRAL [34]. Such code generators have performance-relevant choices to make that are different for each platform. Often, the choice is determined by using autotuning [6]: the process of generating a search space of possible implementations/configurations of a kernel or an application and evaluating a subset of implementations/configurations on a target platform through empirical measurements to identify the high-performing implementation/configuration.

The semantics of a program and its performance optimization can be considered as two separate concerns. With the semantics of an algorithm fixed, the goal of autotuning is to find a variant of the program with the lowest time to solution on a given hardware without changing how the algorithm works. Separation of semantics and optimization parameters is one of the motivations of Halide [37], wherein a kernel and an iteration space are specified in a domain-specific language. This is assigned a separate schedule that determines the threads and loop nest that execute the kernel over the entire iteration space. The schedule can be optimized automatically [1, 35, 48] via machine learning (ML) methods.

Another approach is to use directives inside the source code that describe the optimizations to apply, whereas the code itself describes only the semantics. This realizes the separation of concerns on any source code containing loops, without being specific to a domain. In C/C++, pragmas are the most straightforward syntax to convey loop optimization directives [16, 30]. Such pragmas, when added to a loop nest, tell the compiler to apply a specific transformation to the loop, such as unrolling or parallelization.

Polly [22] is the LLVM subproject that adds a polyhedral loop optimizer to LLVM's optimization pipeline. By default, it uses various heuristics to optimize a loop nest, including PLuTo's [8] memory locality optimizer, and generalizes matrix-multiplication recognition and optimization [20], tiling, auto-parallelization, and GPU offloading [23]. Recent work exposed Polly's loop transformations as source code directives to the programmer [29] by parsing pragmas in the source code using Clang [33] and passing them to Polly. These pragmas also build up a search space that can be used for autotuning [31]. These directives are composable; in other words, after applying a transformation, more transformations can be applied to the results of a transformation. The set of additional loop transformations that can be applied depends on the sequence of prior loop transformations. Consequently, the search space for autotuning a sequence of loop transformations is tree-shaped [31] where each node represents a sequence of loop transformations, or configurations. The tree search space is potentially unbounded in depth (e.g., the choice of tile size can be any positive integer and another loop transformation can always be added). Consequently, the number of potentially useful configurations is too large to search exhaustively.

Monte Carlo tree search (MCTS) [28], originally proposed to solve games in artificial intelligence, is a promising heuristic method to explore treelike search space. However, out-of-the-box MCTS has several limitations for the treelike search space exposed by Polly's loop transformation pragmas. To address these limitations, we introduce a customized MCTS to explore the configuration space of loop transformation pragmas. The contributions of the paper are threefold:

- We develop an autotuning framework to efficiently explore a dynamically growing treelike search space of the newly developed Clang loop optimization pragmas.
- We design a customized MCTS method with a new reward mechanism, restart strategy, and transfer learning to improve the search efficiency.
- We show that the customized MCTS outperforms Polly's optimization heuristic in 16 out of 24 PolyBench kernels and obtains a speedup of 2.1 on average. On three Exascale Computing Project (ECP) proxy applications, our MCTS surpasses Polly in all three and achieves a speedup of 3.7 on average.

---

### النسخة العربية

تقضي معظم البرامج كثيفة الحساب، وخاصة التطبيقات العلمية في الحوسبة عالية الأداء، قدراً كبيراً من وقت التنفيذ في الحلقات، مما يجعلها الهدف الرئيسي لتحسينات الأداء. تشمل الاستراتيجيات الشائعة استبدالها باستدعاءات مكتبات مقدمة من المورّدين (مثل BLAS [32] أو FFT [14]). ومع ذلك، هذه المكتبات متاحة فقط لمجموعة محدودة من النوى، والتي تتطلب استخدام تخطيط بيانات محدد في الذاكرة وقد لا تكون متاحة على جميع المنصات. لذلك، سعى الباحثون حتماً إلى تحسين الحلقات في التطبيق نفسه.

لسوء الحظ، يعد التحسين اليدوي عملية تستغرق وقتاً طويلاً وتتطلب معرفة عميقة بالعتاد المستهدف وغالباً ما ينتج عنها شفرة أقل قابلية للصيانة. تَعِدُ مولدات الشفرة بتوفير حلول من خلال تحسين الشفرة المُصنَّعة تلقائياً [18] من وصف مشكلة خاص بالمجال ولكنها متخصصة لأنواع معينة من الخوارزميات، مثل LIFT [40] لـ BLAS و SPIRAL [34]. لدى مولدات الشفرة هذه خيارات ذات صلة بالأداء يجب اتخاذها والتي تختلف لكل منصة. غالباً ما يتم تحديد الاختيار باستخدام الضبط التلقائي (autotuning) [6]: عملية توليد فضاء بحث من التنفيذات/التكوينات المحتملة لنواة أو تطبيق وتقييم مجموعة فرعية من التنفيذات/التكوينات على منصة مستهدفة من خلال قياسات تجريبية لتحديد التنفيذ/التكوين عالي الأداء.

يمكن اعتبار دلالات البرنامج وتحسين أدائه كاهتمامين منفصلين. مع تثبيت دلالات الخوارزمية، فإن هدف الضبط التلقائي هو إيجاد متغير من البرنامج بأقل وقت للحل على عتاد معين دون تغيير كيفية عمل الخوارزمية. يُعد فصل الدلالات ومعاملات التحسين أحد دوافع Halide [37]، حيث يتم تحديد النواة وفضاء التكرار في لغة خاصة بالمجال. يتم تعيين جدول منفصل يحدد الخيوط وعش الحلقة التي تنفذ النواة على فضاء التكرار بأكمله. يمكن تحسين الجدول تلقائياً [1, 35, 48] عبر طرق التعلم الآلي (ML).

نهج آخر هو استخدام توجيهات داخل الشفرة المصدرية تصف التحسينات المراد تطبيقها، بينما تصف الشفرة نفسها الدلالات فقط. يحقق هذا فصل الاهتمامات على أي شفرة مصدرية تحتوي على حلقات، دون أن يكون خاصاً بمجال معين. في C/C++، تعد توجيهات pragma أبسط بناء جملة لنقل توجيهات تحسين الحلقات [16, 30]. هذه التوجيهات pragma، عند إضافتها إلى عش حلقة، تخبر المترجم بتطبيق تحويل معين على الحلقة، مثل فك الحلقات أو التوازي.

Polly [22] هو المشروع الفرعي لـ LLVM الذي يضيف محسِّن حلقات متعدد السطوح إلى خط تحسين LLVM. افتراضياً، يستخدم استدلالات مختلفة لتحسين عش الحلقة، بما في ذلك محسِّن محلية الذاكرة لـ PLuTo [8]، ويعمم التعرف على ضرب المصفوفات وتحسينه [20]، والتجزئة (tiling)، والتوازي التلقائي، ونقل العمل إلى GPU [23]. كشف عمل حديث تحويلات حلقات Polly كتوجيهات شفرة مصدرية للمبرمج [29] من خلال تحليل توجيهات pragma في الشفرة المصدرية باستخدام Clang [33] وتمريرها إلى Polly. تبني هذه التوجيهات pragma أيضاً فضاء بحث يمكن استخدامه للضبط التلقائي [31]. هذه التوجيهات قابلة للتركيب؛ بمعنى آخر، بعد تطبيق تحويل، يمكن تطبيق المزيد من التحويلات على نتائج التحويل. تعتمد مجموعة تحويلات الحلقات الإضافية التي يمكن تطبيقها على تسلسل تحويلات الحلقات السابقة. وبالتالي، فإن فضاء البحث للضبط التلقائي لتسلسل من تحويلات الحلقات على شكل شجرة [31] حيث تمثل كل عقدة تسلسلاً من تحويلات الحلقات، أو التكوينات. فضاء البحث الشجري غير محدود في العمق (على سبيل المثال، يمكن أن يكون اختيار حجم التجزئة أي عدد صحيح موجب ويمكن دائماً إضافة تحويل حلقة آخر). وبالتالي، فإن عدد التكوينات المفيدة المحتملة كبير جداً بحيث لا يمكن البحث فيها بشكل شامل.

بحث شجرة مونت كارلو (MCTS) [28]، الذي تم اقتراحه في الأصل لحل الألعاب في الذكاء الاصطناعي، هو طريقة استدلالية واعدة لاستكشاف فضاء البحث الشجري. ومع ذلك، فإن MCTS الجاهز له عدة قيود على فضاء البحث الشجري المكشوف بواسطة توجيهات pragma لتحويل الحلقات في Polly. لمعالجة هذه القيود، نقدم MCTS مخصصاً لاستكشاف فضاء التكوين لتوجيهات pragma لتحويل الحلقات. مساهمات الورقة ثلاثية:

- نطور إطار ضبط تلقائي لاستكشاف فضاء بحث شجري متنامٍ ديناميكياً من توجيهات pragma لتحسين حلقات Clang المطورة حديثاً بكفاءة.
- نصمم طريقة MCTS مخصصة بآلية مكافأة جديدة، واستراتيجية إعادة تشغيل، ونقل تعلم لتحسين كفاءة البحث.
- نُظهر أن MCTS المخصص يتفوق على استدلالات تحسين Polly في 16 من أصل 24 نواة في PolyBench ويحصل على تسريع بمعدل 2.1 في المتوسط. في ثلاثة تطبيقات بديلة لمشروع الحوسبة في النطاق الإكسا (ECP)، يتفوق MCTS الخاص بنا على Polly في التطبيقات الثلاثة جميعها ويحقق تسريعاً بمعدل 3.7 في المتوسط.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** loop optimization, autotuning, pragma directives, polyhedral optimizer, composable transformations, tree search space, MCTS
- **Equations:** 0
- **Citations:** [6], [8], [14], [16], [18], [20], [22], [23], [28], [29], [30], [31], [32], [33], [34], [37], [40], [48]
- **Special handling:**
  - Proper nouns kept in English: LLVM, Polly, Clang, BLAS, FFT, LIFT, SPIRAL, Halide, PLuTo, PolyBench, ECP
  - Technical terms: pragma, tiling, autotuning, polyhedral
  - Acronyms: ML (التعلم الآلي), GPU (kept as GPU), MCTS (kept as MCTS)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
