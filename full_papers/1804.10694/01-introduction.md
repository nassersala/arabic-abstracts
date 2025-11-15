# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** code generation, optimization, compiler, polyhedral model, loop transformation, vectorization, loop unrolling, array packing, register blocking, data prefetching, memory coalescing, scheduling language, intermediate representation, tiling

---

### English Version

Generating efficient code for high performance systems is becoming more and more difficult as these architectures are increasing in complexity and diversity. Obtaining the best performance requires complex code and data layout transformations, management of complex memory hierarchies, and efficient data communication and synchronization.

For example, consider generalized matrix multiplication (gemm), which computes C = αAB + βC and is a building block of numerous algorithms, including simulations and convolutional neural networks. Highly-tuned implementations require fusing the multiplication and addition loops, as well as applying two-level tiling, vectorization, loop unrolling, array packing [20], register blocking, and data prefetching. Furthermore, tuned implementations separate partial tiles from full tiles, since partial tiles cannot fully benefit from the same optimizations. High performance GPU implementations require even more optimizations, including coalescing memory accesses, managing data movement between global, shared, and register memory, and inserting synchronization primitives.

Automatically generating such complex code is still beyond the capabilities of state-of-the-art compilers. The importance of kernels such as gemm motivates vendors to release immensely complex hand-optimized libraries for these kernels. However, for most users, obtaining this level of performance for their own code is challenging, since the effort required to explore the space of possible implementations is intractable when hand-coding complicated code transformations.

Previous work using the polyhedral model has shown success in implementing complex iteration space transformations [49], [8], [44], [22], [46], [37], data locality optimizations [27], [21], and memory management optimizations [17], [43], [29], [38], [13]. Although polyhedral compilers can represent these program and data transformations, they still do not successfully select transformations that result in the best performance. Currently, these compilers do not match the performance of hand-optimized kernels for algorithms such as gemm. The blue bars in Figure 1 show the performance of state-of-the-art polyhedral compilers for gemm compared to the Intel MKL [26] and Nvidia cuBLAS [35] libraries. Fully-automatic polyhedral compilers such as Polly [22] and Pluto [8] improve productivity, but do not obtain the desired level of performance since their search techniques consider only a subset of the necessary optimizations and rely on less accurate machine models, leading the compiler to make suboptimal decisions. Other polyhedral frameworks, such as AlphaZ [51] and CHiLL [10], eschew full automation and instead expose a scheduling language that enables users to productively explore the space of possible transformations. While these frameworks achieve better performance, their scheduling languages are not designed to target distributed systems. For example, they do not allow the user to partition computations, send data across nodes, or insert required synchronization.

In this paper, we introduce TIRAMISU, a polyhedral compiler with a scheduling language featuring novel commands for targeting multiple high performance architectures. TIRAMISU is well-suited for implementing data parallel algorithms (loop nests manipulating arrays). It takes a high level representation of the program (a pure algorithm and a set of scheduling commands), applies the necessary code transformations, and generates highly-optimized code for the target architecture.

In addition to scheduling commands for loop and data-layout transformations, the TIRAMISU scheduling language introduces novel commands for explicit communication and synchronization, and for mapping buffers to different memory hierarchies. In order to simplify the implementation of the scheduling language, TIRAMISU explicitly divides the intermediate representation into four layers designed to hide the complexity and large variety of execution platforms by separating the architecture-independent algorithm from code transformations, data layout, and communication. TIRAMISU targets multicore CPUs, CUDA GPUs, distributed architectures, and FPGA. This paper presents the first three backends while Del Sozzo et al. [14] describe an FPGA backend.

The use of a scheduling language has been shown effective for generating efficient code by multiple compilers including CHiLL, AlphaZ, and Halide [39], [40]. In comparison with Halide in particular, not only does TIRAMISU introduce novel scheduling extensions, TIRAMISU fundamentally differs in that it relies on the expressive polyhedral representation instead of the interval-based representation used by Halide. This allows TIRAMISU to naturally express non-rectangular iteration spaces, to support programs with cyclic data-flow graphs, and to apply any affine transformation (including iteration space skewing), all of which are not naturally expressible in Halide.

This paper makes the following contributions:

• We introduce a polyhedral compiler with a scheduling language that features novel commands for controlling data communication, synchronization, and for mapping to different memory hierarchies. These extensions enable targeting multiple high-performance architectures including multicore CPUs, GPUs, and distributed machines.

• We explicitly divide the intermediate representation into four layers to simplify the implementation of the scheduling language. The four-layer IR separates the algorithm from code transformations and data-layout transformations, allowing for portability and simplifying the composition of architecture-specific lowering transformations.

• We evaluate TIRAMISU on a set of deep learning and linear algebra kernels and show that TIRAMISU can generate efficient code that outperforms Intel MKL by up to 2.3×. We also evaluate TIRAMISU on a set of image processing benchmarks and show that TIRAMISU matches or outperforms state-of-the-art compilers on different hardware architectures, including multicore CPUs, GPUs, and distributed machines.

---

### النسخة العربية

أصبح توليد شفرة فعالة لأنظمة الأداء العالي أكثر صعوبة مع تزايد تعقيد هذه المعماريات وتنوعها. يتطلب الحصول على أفضل أداء تحويلات معقدة للشفرة وتخطيط البيانات، وإدارة التسلسلات الهرمية المعقدة للذاكرة، واتصال فعال للبيانات ومزامنة.

على سبيل المثال، لننظر إلى ضرب المصفوفات المعمم (gemm)، الذي يحسب C = αAB + βC وهو لبنة بناء للعديد من الخوارزميات، بما في ذلك المحاكاة والشبكات العصبية الالتفافية. تتطلب التطبيقات المضبوطة بدقة دمج حلقات الضرب والجمع، بالإضافة إلى تطبيق تبليط ثنائي المستوى، والتوجيه المتجه، وفك الحلقات، وتعبئة المصفوفات [20]، وحجب السجلات، والجلب المسبق للبيانات. علاوة على ذلك، تفصل التطبيقات المضبوطة البلاطات الجزئية عن البلاطات الكاملة، نظراً لأن البلاطات الجزئية لا يمكنها الاستفادة الكاملة من نفس التحسينات. تتطلب تطبيقات GPU عالية الأداء المزيد من التحسينات، بما في ذلك دمج الوصول إلى الذاكرة، وإدارة نقل البيانات بين الذاكرة العامة والمشتركة وذاكرة السجلات، وإدراج بدائيات المزامنة.

لا يزال توليد مثل هذه الشفرة المعقدة تلقائياً يتجاوز قدرات المترجمات الحديثة. إن أهمية النوى مثل gemm تحفز البائعين على إصدار مكتبات معقدة للغاية محسنة يدوياً لهذه النوى. ومع ذلك، بالنسبة لمعظم المستخدمين، فإن الحصول على هذا المستوى من الأداء لشفرتهم الخاصة يمثل تحدياً، حيث أن الجهد المطلوب لاستكشاف مساحة التطبيقات الممكنة غير قابل للتنفيذ عند البرمجة اليدوية لتحويلات الشفرة المعقدة.

أظهرت الأعمال السابقة التي تستخدم النموذج متعدد السطوح نجاحاً في تنفيذ تحويلات معقدة لفضاء التكرار [49]، [8]، [44]، [22]، [46]، [37]، وتحسينات موضعية البيانات [27]، [21]، وتحسينات إدارة الذاكرة [17]، [43]، [29]، [38]، [13]. على الرغم من أن المترجمات متعددة السطوح يمكنها تمثيل تحويلات البرنامج والبيانات هذه، إلا أنها لا تزال لا تنجح في اختيار التحويلات التي تؤدي إلى أفضل أداء. حالياً، لا تطابق هذه المترجمات أداء النوى المحسنة يدوياً لخوارزميات مثل gemm. تُظهر الأشرطة الزرقاء في الشكل 1 أداء المترجمات متعددة السطوح الحديثة لـ gemm مقارنةً بمكتبات Intel MKL [26] وNvidia cuBLAS [35]. تعمل المترجمات متعددة السطوح الأوتوماتيكية بالكامل مثل Polly [22] وPluto [8] على تحسين الإنتاجية، لكنها لا تحصل على المستوى المطلوب من الأداء نظراً لأن تقنيات البحث الخاصة بها تأخذ في الاعتبار فقط مجموعة فرعية من التحسينات اللازمة وتعتمد على نماذج آلة أقل دقة، مما يؤدي إلى قيام المترجم باتخاذ قرارات دون المستوى الأمثل. تتجنب أطر العمل متعددة السطوح الأخرى، مثل AlphaZ [51] وCHiLL [10]، الأتمتة الكاملة وبدلاً من ذلك تكشف لغة جدولة تمكن المستخدمين من استكشاف مساحة التحويلات الممكنة بشكل منتج. في حين تحقق هذه الأطر أداءً أفضل، فإن لغات الجدولة الخاصة بها ليست مصممة لاستهداف الأنظمة الموزعة. على سبيل المثال، لا تسمح للمستخدم بتقسيم الحسابات، أو إرسال البيانات عبر العقد، أو إدراج المزامنة المطلوبة.

في هذه الورقة، نقدم TIRAMISU، وهو مترجم متعدد السطوح بلغة جدولة تتميز بأوامر جديدة لاستهداف معماريات أداء عالٍ متعددة. يعتبر TIRAMISU مناسباً تماماً لتنفيذ الخوارزميات المتوازية للبيانات (أعشاش الحلقات التي تعالج المصفوفات). إنه يأخذ تمثيلاً عالي المستوى للبرنامج (خوارزمية نقية ومجموعة من أوامر الجدولة)، ويطبق تحويلات الشفرة اللازمة، ويولد شفرة محسنة للغاية للمعمارية المستهدفة.

بالإضافة إلى أوامر الجدولة لتحويلات الحلقات وتخطيط البيانات، تقدم لغة جدولة TIRAMISU أوامر جديدة للاتصال والمزامنة الصريحة، ولتخطيط المخازن المؤقتة على تسلسلات هرمية مختلفة للذاكرة. من أجل تبسيط تنفيذ لغة الجدولة، يقسم TIRAMISU بشكل صريح التمثيل الوسيط إلى أربع طبقات مصممة لإخفاء التعقيد والتنوع الكبير لمنصات التنفيذ من خلال فصل الخوارزمية المستقلة عن المعمارية عن تحويلات الشفرة وتخطيط البيانات والاتصال. يستهدف TIRAMISU وحدات المعالجة المركزية متعددة الأنوية، ووحدات معالجة الرسومات CUDA، والمعماريات الموزعة، وFPGA. تقدم هذه الورقة الواجهات الخلفية الثلاثة الأولى بينما يصف Del Sozzo et al. [14] واجهة خلفية لـ FPGA.

لقد ثبت أن استخدام لغة الجدولة فعال لتوليد شفرة فعالة من قبل عدة مترجمات بما في ذلك CHiLL وAlphaZ وHalide [39]، [40]. بالمقارنة مع Halide على وجه الخصوص، لا يقدم TIRAMISU فقط امتدادات جدولة جديدة، بل يختلف TIRAMISU بشكل أساسي في أنه يعتمد على التمثيل متعدد السطوح التعبيري بدلاً من التمثيل القائم على الفترات المستخدم في Halide. يتيح ذلك لـ TIRAMISU التعبير بشكل طبيعي عن فضاءات تكرار غير مستطيلة، ودعم البرامج ذات الرسوم البيانية لتدفق البيانات الدورية، وتطبيق أي تحويل أفيني (بما في ذلك انحراف فضاء التكرار)، وكل ذلك لا يمكن التعبير عنه بشكل طبيعي في Halide.

تقدم هذه الورقة المساهمات التالية:

• نقدم مترجماً متعدد السطوح بلغة جدولة تتميز بأوامر جديدة للتحكم في اتصال البيانات والمزامنة، ولتخطيط التسلسلات الهرمية المختلفة للذاكرة. تمكّن هذه الامتدادات من استهداف معماريات أداء عالٍ متعددة بما في ذلك وحدات المعالجة المركزية متعددة الأنوية، ووحدات معالجة الرسومات، والآلات الموزعة.

• نقسم التمثيل الوسيط بشكل صريح إلى أربع طبقات لتبسيط تنفيذ لغة الجدولة. يفصل التمثيل الوسيط رباعي الطبقات الخوارزمية عن تحويلات الشفرة وتحويلات تخطيط البيانات، مما يسمح بقابلية النقل ويبسط تركيب تحويلات الخفض الخاصة بالمعمارية.

• نقيّم TIRAMISU على مجموعة من نوى التعلم العميق والجبر الخطي ونظهر أن TIRAMISU يمكنه توليد شفرة فعالة تتفوق على Intel MKL بما يصل إلى 2.3×. نقيّم أيضاً TIRAMISU على مجموعة من معايير معالجة الصور ونظهر أن TIRAMISU يطابق أو يتفوق على المترجمات الحديثة على معماريات أجهزة مختلفة، بما في ذلك وحدات المعالجة المركزية متعددة الأنوية، ووحدات معالجة الرسومات، والآلات الموزعة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (performance comparison chart)
- **Key terms introduced:** gemm (generalized matrix multiplication), two-level tiling, array packing, register blocking, data prefetching, memory coalescing, synchronization primitives, iteration space, data-flow graphs, affine transformation, iteration space skewing
- **Equations:** 1 (C = αAB + βC)
- **Citations:** Multiple references to prior work [8], [10], [13], [14], [17], [20], [21], [22], [26], [27], [29], [35], [37], [38], [39], [40], [43], [44], [46], [49], [51]
- **Special handling:** Technical compiler terminology requires careful translation to maintain precision

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
