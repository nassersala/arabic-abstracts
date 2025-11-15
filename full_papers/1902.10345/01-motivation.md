# Section 1: Motivation
## القسم 1: الدافع

**Section:** Introduction/Motivation
**Translation Quality:** 0.88
**Glossary Terms Used:** HPC, performance portability, heterogeneous, CPU, GPU, FPGA, optimization, dataflow, parallelism

---

### English Version

HPC programmers have long sacrificed ease of programming and portability for achieving better performance. This mindset was established at a time when computer nodes had a single processor/core and were programmed with C/Fortran and MPI. The last decade, witnessing the end of Dennard scaling and Moore's law, brought a flurry of new technologies into the compute nodes. Those range from simple multi-core and manycore CPUs to heterogeneous GPUs and specialized FPGAs. To support those architectures, the complexity of OpenMP's specification grew by more than an order of magnitude from 63 pages in OpenMP 1.0 to 666 pages in OpenMP 5.0. This one example illustrates how (performance) programming complexity shifted from network scalability to node utilization. Programmers would now not only worry about communication (fortunately, the MPI specification grew by less than 4x from MPI-1.0 to 3.1) but also about the much more complex on-node heterogeneous programming. The sheer number of new approaches, such as OpenACC, OpenCL, or CUDA demonstrate the difficult situation in on-node programming. This increasing complexity makes it nearly impossible for domain scientists to write portable and performant code today.

The growing complexity in performance programming led to a specialization of roles into domain scientists and performance engineers. Performance engineers typically optimize codes by moving functionality to performance libraries such as BLAS or LAPACK. If this is insufficient, they translate the user-code to optimized versions, often in different languages such as assembly code, CUDA, or tuned OpenCL. Both libraries and manual tuning reduce code maintainability, because the optimized versions are not only hard to understand for the original author (the domain scientist) but also cannot be changed without major effort.

Code annotations as used by OpenMP or OpenACC do not change the original code that then remains understandable to the domain programmer. However, the annotations must re-state (or modify) some of the semantics of the annotated code (e.g., data placement or reduction operators). This means that a (domain scientist) programmer who modifies the code, must modify some annotations or she may introduce hard-to-find bugs. With heterogeneous target devices, it now becomes common that the complexity of annotations is higher than the code they describe. Thus, scientific programmers can barely manage the complexity of the code targeted at heterogeneous devices.

The main focus of the community thus moved from scalability to performance portability as a major research target. We call a code-base performance-portable if the domain scientist's view ("what is computed") does not change while the code is optimized to different target architectures, achieving consistently high performance. The execution should be approximately as performant (e.g., attaining similar ratio of peak performance) as the best-known implementation or theoretical best performance on the target architecture. As discussed before, hardly any existing programming model that supports portability to different accelerators satisfies this definition.

Our Data-centric Parallel Programming (DAPP) concept addresses performance portability. It uses a data-centric viewpoint of an application to separate the roles of domain scientist and performance programmer, as shown in Fig. 1. DAPP relies on Stateful DataFlow multiGraphs (SDFGs) to represent code semantics and transformations, and supports modifying them to tune for particular target architectures. It bases on the observation that data-movement dominates time and energy in today's computing systems and pioneers the necessary fundamental change of view in parallel programming. As such, it builds on ideas of data-centric mappers and schedule annotations such as Legion and Halide and extends them with a multi-level visualization of data movement, code transformation and compilation for heterogeneous targets, and strict separation of concerns for programming roles. The domain programmer thus works in a convenient and well-known language such as (restricted) Python or MATLAB. The compiler transforms the code into an SDFG, on which the performance engineer solely works on, specifying transformations that match certain data-flow structures on all levels (from registers to inter-node communication) and modify them. Our transformation language can implement arbitrary changes to the SDFG and supports creating libraries of transformations to optimize workflows. Thus, SDFGs separate the concerns of the domain scientist and the performance engineers through a clearly defined interface, enabling highest productivity of both roles.

We provide a full implementation of this concept in our DataCentric (DaCe) programming environment, which supports (limited) Python, MATLAB, and TensorFlow as frontends, as well as support for selected DSLs. DaCe is easily extensible to other frontends through an SDFG builder interface. Performance engineers develop potentially domain-specific transformation libraries (e.g., for stencil-patterns) and can tune them through DaCe's Interactive Optimization Environment (DIODE). The current implementation focuses on on-node parallelism as the most challenging problem in scientific computing today. However, it is conceivable that the principles can be extended beyond node-boundaries to support large-scale parallelism using MPI as a backend.

The key contributions of our work are as follows:
• We introduce the principle of Data-centric Parallel Programming, in which we use Stateful Dataflow Multigraphs, a data-centric Intermediate Representation that enables separating code definition from its optimization.
• We provide an open-source implementation of the data-centric environment and its performance-optimization IDE.
• We demonstrate performance portability on fundamental kernels, graph algorithms, and a real-world quantum transport simulator — results are competitive with and faster than expert-tuned libraries from Intel and NVIDIA, approaching peak hardware performance, and up to five orders of magnitude faster than naïve FPGA code written with High-Level Synthesis, all from the same program source code.

---

### النسخة العربية

ضحى مبرمجو الحوسبة عالية الأداء منذ فترة طويلة بسهولة البرمجة وقابلية النقل لتحقيق أداء أفضل. تأسست هذه العقلية في وقت كانت فيه عقد الحاسوب تحتوي على معالج/نواة واحدة ويتم برمجتها بلغات C/Fortran وMPI. أحضر العقد الأخير، الذي شهد نهاية قانون دينارد وقانون مور، مجموعة من التقنيات الجديدة إلى عقد الحوسبة. تتراوح هذه من وحدات المعالجة المركزية متعددة النوى والكثيرة النوى البسيطة إلى وحدات معالجة الرسومات غير المتجانسة ومصفوفات البوابات القابلة للبرمجة المتخصصة. لدعم هذه المعماريات، نمت تعقيدات مواصفات OpenMP بأكثر من ترتيب من الحجم من 63 صفحة في OpenMP 1.0 إلى 666 صفحة في OpenMP 5.0. يوضح هذا المثال الواحد كيف تحول تعقيد البرمجة (الأداء) من قابلية التوسع للشبكة إلى استخدام العقدة. لن يقلق المبرمجون الآن فقط بشأن الاتصال (لحسن الحظ، نمت مواصفات MPI بأقل من 4 أضعاف من MPI-1.0 إلى 3.1) ولكن أيضًا بشأن البرمجة غير المتجانسة الأكثر تعقيدًا داخل العقدة. يُظهر العدد الهائل من الأساليب الجديدة، مثل OpenACC وOpenCL أو CUDA، الوضع الصعب في البرمجة داخل العقدة. هذا التعقيد المتزايد يجعل من المستحيل تقريبًا على علماء المجال كتابة شفرة محمولة وعالية الأداء اليوم.

أدى التعقيد المتزايد في برمجة الأداء إلى تخصص الأدوار إلى علماء مجال ومهندسي أداء. يقوم مهندسو الأداء عادةً بتحسين الشفرات عن طريق نقل الوظائف إلى مكتبات الأداء مثل BLAS أو LAPACK. إذا كان هذا غير كافٍ، فإنهم يترجمون شفرة المستخدم إلى إصدارات محسنة، غالبًا بلغات مختلفة مثل شفرة التجميع أو CUDA أو OpenCL المضبوط. تقلل المكتبات والضبط اليدوي من قابلية صيانة الشفرة، لأن الإصدارات المحسنة ليست صعبة الفهم فقط للمؤلف الأصلي (عالم المجال) ولكن أيضًا لا يمكن تغييرها دون جهد كبير.

تعليقات الشفرة كما تستخدم في OpenMP أو OpenACC لا تغير الشفرة الأصلية التي تبقى مفهومة لمبرمج المجال. ومع ذلك، يجب أن تعيد التعليقات صياغة (أو تعديل) بعض دلالات الشفرة المعلقة (على سبيل المثال، وضع البيانات أو عوامل الاختزال). هذا يعني أن المبرمج (عالم المجال) الذي يعدل الشفرة، يجب أن يعدل بعض التعليقات أو قد يقدم أخطاء يصعب العثور عليها. مع الأجهزة المستهدفة غير المتجانسة، أصبح من الشائع الآن أن تعقيد التعليقات أعلى من الشفرة التي تصفها. وبالتالي، بالكاد يمكن للمبرمجين العلميين إدارة تعقيد الشفرة المستهدفة للأجهزة غير المتجانسة.

وبالتالي، انتقل التركيز الرئيسي للمجتمع من قابلية التوسع إلى قابلية نقل الأداء كهدف بحثي رئيسي. نسمي قاعدة الشفرة قابلة لنقل الأداء إذا لم تتغير وجهة نظر عالم المجال ("ما يتم حسابه") أثناء تحسين الشفرة لمعماريات مستهدفة مختلفة، مع تحقيق أداء عالٍ باستمرار. يجب أن يكون التنفيذ عالي الأداء تقريبًا (على سبيل المثال، تحقيق نسبة مماثلة من أداء الذروة) كأفضل تطبيق معروف أو أفضل أداء نظري على المعمارية المستهدفة. كما نوقش من قبل، بالكاد يلبي أي نموذج برمجة موجود يدعم قابلية النقل إلى مسرعات مختلفة هذا التعريف.

يعالج مفهوم البرمجة المتوازية المحورية للبيانات (DAPP) الخاص بنا قابلية نقل الأداء. يستخدم وجهة نظر محورية للبيانات لتطبيق لفصل أدوار عالم المجال ومبرمج الأداء، كما هو موضح في الشكل 1. يعتمد DAPP على الرسوم البيانية المتعددة لتدفق البيانات الحافظة للحالة (SDFGs) لتمثيل دلالات الشفرة والتحويلات، ويدعم تعديلها للضبط لمعماريات مستهدفة محددة. يستند إلى الملاحظة بأن حركة البيانات تهيمن على الوقت والطاقة في أنظمة الحوسبة اليوم ويرائد التغيير الأساسي الضروري في وجهة النظر في البرمجة المتوازية. على هذا النحو، فإنه يبني على أفكار الخرائط المحورية للبيانات وتعليقات الجدولة مثل Legion وHalide ويوسعها بتصور متعدد المستويات لحركة البيانات، وتحويل الشفرة والتجميع للأهداف غير المتجانسة، والفصل الصارم للمخاوف لأدوار البرمجة. وبالتالي، يعمل مبرمج المجال بلغة مناسبة ومعروفة مثل Python (المقيدة) أو MATLAB. يحول المترجم الشفرة إلى SDFG، الذي يعمل عليه مهندس الأداء فقط، محددًا التحويلات التي تطابق بعض هياكل تدفق البيانات على جميع المستويات (من السجلات إلى الاتصال بين العقد) وتعديلها. يمكن للغة التحويل الخاصة بنا تنفيذ تغييرات عشوائية على SDFG وتدعم إنشاء مكتبات من التحويلات لتحسين سير العمل. وبالتالي، تفصل SDFGs مخاوف عالم المجال ومهندسي الأداء من خلال واجهة محددة بوضوح، مما يتيح أعلى إنتاجية لكلا الدورين.

نوفر تطبيقًا كاملاً لهذا المفهوم في بيئة البرمجة المحورية للبيانات (DaCe) الخاصة بنا، والتي تدعم Python (المحدودة) وMATLAB وTensorFlow كواجهات أمامية، بالإضافة إلى دعم DSLs محددة. DaCe قابل للتوسيع بسهولة لواجهات أمامية أخرى من خلال واجهة بناء SDFG. يطور مهندسو الأداء مكتبات تحويل خاصة بالمجال (على سبيل المثال، لأنماط الاستنسل) ويمكنهم ضبطها من خلال بيئة التحسين التفاعلية (DIODE) الخاصة بـ DaCe. يركز التطبيق الحالي على التوازي داخل العقدة كمشكلة الأكثر تحديًا في الحوسبة العلمية اليوم. ومع ذلك، من المتصور أن يمكن توسيع المبادئ إلى ما وراء حدود العقدة لدعم التوازي واسع النطاق باستخدام MPI كخلفية.

المساهمات الرئيسية لعملنا هي كما يلي:
• نقدم مبدأ البرمجة المتوازية المحورية للبيانات، حيث نستخدم الرسوم البيانية المتعددة لتدفق البيانات الحافظة للحالة، وهي تمثيل وسيط محوري للبيانات يتيح فصل تعريف الشفرة عن تحسينها.
• نوفر تطبيقًا مفتوح المصدر للبيئة المحورية للبيانات وبيئة التطوير المتكاملة لتحسين الأداء الخاصة بها.
• نوضح قابلية نقل الأداء على النوى الأساسية، وخوارزميات الرسوم البيانية، ومحاكي نقل كمي من العالم الحقيقي - النتائج تنافسية وأسرع من المكتبات المضبوطة من قبل الخبراء من Intel وNVIDIA، تقترب من ذروة أداء الأجهزة، وحتى خمسة أوامر من الحجم أسرع من شفرة FPGA الساذجة المكتوبة بالتركيب عالي المستوى، كل ذلك من نفس شفرة مصدر البرنامج.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** SDFG, DAPP, DaCe, DIODE, performance portability, data-centric
- **Equations:** 0
- **Citations:** Multiple references to OpenMP, MPI, CUDA, OpenCL, Legion, Halide
- **Special handling:** Technical terminology for HPC and parallel programming

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
