# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** related_work
**Translation Quality:** 0.86
**Glossary Terms Used:** autotuning, compiler optimization, machine learning, deep learning, reinforcement learning, neural network, tree search, beam search, vector space, search space, domain-specific language

---

### English Version

Several autotuning frameworks have been developed to support autotuning regardless of the domain, such as cTuning-cc/Milepost GCC [19], OpenTuner [3], ATF [38], ytopt [5], and mctree [31]. The autotuning frameworks described in [17, 39, 42] are developed for a user-defined sequence of transformations in which only a subset of transformation parameters can be autotuned. There are also domain-specific autotuning frameworks for image and array processing, such as HalideTuner [48], ProTuner [26], and the works in [1, 35]; AutoTVM [12] and ReLeASE [2] for ML model compilation and accelerators; and PATUS [13] and LIFT [24] for stencil computation.

Many approaches in the literature for solving loop optimization problems use ML and reinforcement learning (RL) and, recently, deep learning approaches. Early studies applied ML approaches to solve a code optimization problem. For example, Stock et al. [41] applied several ML models such as neural networks, binary trees, SVM, and linear regression with hand-crafted features to solve auto-vectorization for loop permutation, vectorized loop, and unroll. Killian et al. [27] proposed a heuristics algorithm for auto-vectorization based on SVM that provides optimized codes without expert knowledge. The authors investigated how to combine vectorization reports with iterative compilation and code generation to craft features. In their paper, SVM is used to predict the speedup of a program given a sequence of optimization steps.

Recently, state-of-the-art deep learning models are being introduced for loop optimization. In [15], Cummins et al. solved a loop optimization problem by a deep learning model developed based on recurrent neural networks with Long short-term memory. The proposed model takes codes as texts for input and predicts heterogeneous mapping for either GPU or CPUs and the size of thread coarsening factor $2^f \in \{2, \ldots, 32\}$. They verified their model by benchmarking the previous method based on decision tree [21] on several datasets such as NPB, PolyBench, Parboil, SHOC, and Rodinia. In [2], Ahn et al. developed an RL-based algorithm to solve a compilation problem for deep neural networks built on top of TVM [11]. Haj-Ali et al. [25] proposed a deep RL-based method for loop optimization that determines vectorized factors. Their DNN policy agent takes code embeddings as input states where the embeddings are computed by Code2Vec [43]. The agent determines two vectorized factors such as vectorization width and interleave counts, and run time is used for a reward. The researchers evaluated the proposed algorithm by benchmarking Polly, decision tree, feed-forward networks, and nearest-neighbor search. In [46], an autotuning framework based on Bayesian optimization (BO) was proposed to explore the parameter space search. BO models such as random forests, extra trees, gradient-boosted regression trees, and Gaussian processes are selected as a learner in the proposed framework. Performance of the framework is tested on six PolyBench kernels with the latest LLVM Clang/Polly loop optimization pragmas. However, these frameworks are limited to the search space expressed in a vector space. A search tree considered in the literature does not directly map to the space of a fixed number of knobs.

Recent literature solves loop optimization by defining search space as a tree, such as in [1] and [26] for the Halide scheduler, in [7] for Telamon, and in [31] for LLVM Clang/Polly loop optimization pragmas.

Tree search algorithms including MCTS are introduced to optimize Halide [36] schedules. To tackle the limitation of a vector search space for Halide studied in [48] and [35], Adams et al. [1] proposed an autotuning framework based on beam search over a tree-shaped search space. Since each node in the search tree represents an intermediate schedule, a cost model based on neural networks that output the dot product of a vector of hand-designed terms and a vector of coefficients is used to predict the runtime. The authors verified that the proposed framework finds better configurations than the previous method, HalideTuner [48], does. Haj-Ali et al. [26] further improved Halide schedule autotuning by applying MCTS, which tackles the non-global behavior of the previous beam search approach. The authors report that the schedules found by MCTS are up to 3.6 times faster than those found by existing search methods such as random search, greedy search with $k$ of 1, and the previous beam search. Since their problem space is only Halide schedules, however, these methods do not apply to arbitrary source C/C++ source codes as our schedules do.

---

### النسخة العربية

تم تطوير العديد من أطر الضبط التلقائي لدعم الضبط التلقائي بغض النظر عن المجال، مثل cTuning-cc/Milepost GCC [19] وOpenTuner [3] وATF [38] وytopt [5] وmctree [31]. تم تطوير أطر الضبط التلقائي الموصوفة في [17, 39, 42] لتسلسل معرف بواسطة المستخدم من التحويلات حيث يمكن ضبط مجموعة فرعية فقط من معاملات التحويل تلقائياً. هناك أيضاً أطر ضبط تلقائي خاصة بالمجال لمعالجة الصور والمصفوفات، مثل HalideTuner [48] وProTuner [26] والأعمال في [1, 35]؛ وAutoTVM [12] وReLeASE [2] لتجميع نماذج التعلم الآلي والمسرعات؛ وPATUS [13] وLIFT [24] لحساب القوالب.

تستخدم العديد من الأساليب في الأدبيات لحل مشاكل تحسين الحلقات التعلم الآلي والتعلم المعزز (RL)، ومؤخراً، نهج التعلم العميق. طبقت الدراسات المبكرة نهج التعلم الآلي لحل مشكلة تحسين الشفرة. على سبيل المثال، طبق Stock وآخرون [41] عدة نماذج تعلم آلي مثل الشبكات العصبية والأشجار الثنائية وSVM والانحدار الخطي مع ميزات مصنوعة يدوياً لحل التمتيه التلقائي لتبديل الحلقة، والحلقة المتمتهة، والفك. اقترح Killian وآخرون [27] خوارزمية استدلالية للتمتيه التلقائي بناءً على SVM توفر شفرات محسنة بدون معرفة خبراء. حقق المؤلفون في كيفية دمج تقارير التمتيه مع التجميع التكراري وتوليد الشفرة لصياغة الميزات. في ورقتهم، يُستخدم SVM للتنبؤ بتسريع برنامج معطى تسلسل من خطوات التحسين.

مؤخراً، يتم تقديم نماذج التعلم العميق الحديثة لتحسين الحلقات. في [15], حل Cummins وآخرون مشكلة تحسين الحلقة بنموذج تعلم عميق تم تطويره بناءً على الشبكات العصبية المتكررة مع ذاكرة قصيرة المدى الطويلة. يأخذ النموذج المقترح الشفرات كنصوص للإدخال ويتنبأ بتعيين غير متجانس إما لـ GPU أو CPUs وحجم عامل تخشين الخيوط $2^f \in \{2, \ldots, 32\}$. تحققوا من نموذجهم من خلال قياس الطريقة السابقة بناءً على شجرة القرار [21] على عدة مجموعات بيانات مثل NPB وPolyBench وParboil وSHOC وRodinia. في [2]، طور Ahn وآخرون خوارزمية قائمة على RL لحل مشكلة تجميع للشبكات العصبية العميقة المبنية على TVM [11]. اقترح Haj-Ali وآخرون [25] طريقة قائمة على RL العميق لتحسين الحلقة تحدد عوامل التمتيه. يأخذ وكيل سياسة DNN الخاص بهم تضمينات الشفرة كحالات إدخال حيث يتم حساب التضمينات بواسطة Code2Vec [43]. يحدد الوكيل عاملين متمتهين مثل عرض التمتيه وعدد التشابك، ويُستخدم وقت التشغيل كمكافأة. قيّم الباحثون الخوارزمية المقترحة من خلال قياس Polly وشجرة القرار والشبكات ذات التغذية الأمامية والبحث بأقرب جار. في [46], تم اقتراح إطار ضبط تلقائي قائم على تحسين بايزي (BO) لاستكشاف بحث فضاء المعاملات. يتم اختيار نماذج BO مثل الغابات العشوائية والأشجار الإضافية وأشجار الانحدار المعززة بالتدرج وعمليات غاوس كمتعلم في الإطار المقترح. يتم اختبار أداء الإطار على ستة نوى PolyBench مع أحدث توجيهات pragma لتحسين حلقات LLVM Clang/Polly. ومع ذلك، فإن هذه الأطر محدودة بفضاء البحث المعبر عنه في فضاء متجه. لا يُعيَّن شجرة البحث المعتبرة في الأدبيات مباشرة إلى فضاء عدد ثابت من المقابض.

تحل الأدبيات الحديثة تحسين الحلقة من خلال تعريف فضاء البحث كشجرة، مثل في [1] و[26] لجدولة Halide، وفي [7] لـ Telamon، وفي [31] لتوجيهات pragma لتحسين حلقات LLVM Clang/Polly.

تم تقديم خوارزميات البحث الشجري بما في ذلك MCTS لتحسين جداول Halide [36]. لمعالجة قيود فضاء البحث المتجه لـ Halide المدروسة في [48] و[35], اقترح Adams وآخرون [1] إطار ضبط تلقائي قائم على البحث الشعاعي على فضاء بحث على شكل شجرة. نظراً لأن كل عقدة في شجرة البحث تمثل جدولاً وسيطاً، يُستخدم نموذج تكلفة قائم على الشبكات العصبية يُخرج حاصل الضرب النقطي لمتجه من المصطلحات المصممة يدوياً ومتجه من المعاملات للتنبؤ بوقت التشغيل. تحقق المؤلفون من أن الإطار المقترح يجد تكوينات أفضل من الطريقة السابقة، HalideTuner [48]. حسّن Haj-Ali وآخرون [26] من الضبط التلقائي لجدول Halide بشكل أكبر من خلال تطبيق MCTS، الذي يعالج السلوك غير العالمي لنهج البحث الشعاعي السابق. يُبلغ المؤلفون أن الجداول التي وجدها MCTS أسرع بما يصل إلى 3.6 مرات من تلك التي وجدتها طرق البحث الحالية مثل البحث العشوائي والبحث الجشع مع $k$ من 1 والبحث الشعاعي السابق. ومع ذلك، نظراً لأن فضاء مشكلتهم هو جداول Halide فقط، فإن هذه الطرق لا تنطبق على شفرات مصدر C/C++ التعسفية كما تفعل جداولنا.

---

### Translation Notes

- **Key terms introduced:** autotuning frameworks, domain-specific frameworks, ML models, reinforcement learning, deep learning, recurrent neural networks, LSTM, SVM, decision tree, neural networks, code embeddings, Bayesian optimization, beam search, cost model, tree search
- **Frameworks and tools mentioned:**
  - General autotuning: cTuning-cc, Milepost GCC, OpenTuner, ATF, ytopt, mctree
  - Domain-specific: HalideTuner, ProTuner, AutoTVM, ReLeASE, PATUS, LIFT
  - ML frameworks: TVM, Code2Vec
  - Benchmarks: NPB, PolyBench, Parboil, SHOC, Rodinia
  - Compilers: LLVM, Clang, Polly
  - Languages/schedulers: Halide, Telamon
- **ML techniques discussed:**
  - Traditional ML: SVM, decision trees, linear regression, neural networks
  - Deep learning: RNNs, LSTM, feed-forward networks, DNN
  - RL: Deep RL, policy agents
  - Optimization: Bayesian optimization, random forests, Gaussian processes
  - Search algorithms: MCTS, beam search, greedy search, nearest-neighbor
- **Key comparisons:**
  - Vector space vs tree search space
  - Halide-specific vs general C/C++ source code
  - MCTS improvements: 3.6× speedup over beam search
- **Citations:** [1], [2], [3], [5], [7], [11], [12], [13], [15], [17], [19], [21], [24], [25], [26], [27], [31], [35], [36], [38], [39], [41], [42], [43], [46], [48]
- **Special handling:**
  - Framework names kept in English (standard in literature)
  - Benchmark names preserved
  - Mathematical notation: $2^f \in \{2, \ldots, 32\}$, $k$ of 1
  - Technical terms: auto-vectorization, thread coarsening, code embeddings, etc.

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
