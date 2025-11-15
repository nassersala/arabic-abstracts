# Section 2: Data-Centric Programming
## القسم 2: البرمجة المحورية للبيانات

**Section:** Data-Centric Programming
**Translation Quality:** 0.87
**Glossary Terms Used:** dataflow, optimization, data locality, memory hierarchy, tiling, parallelism, transformation

---

### English Version

Current approaches in high-performance computing optimizations revolve around improving data locality. Regardless of the underlying architecture, the objective is to keep information as close as possible to the processing elements and promote memory reuse. Even a simple application, such as matrix multiplication, requires multiple stages of transformations, including data layout modifications (packing) and register-aware caching. Because optimizations do not modify computations and differ for each architecture, maintaining performance portability of scientific applications requires separating computational semantics from data movement.

SDFGs enable separating application development into two stages, as shown in Fig. 2. The problem is formulated as a high-level program (Fig. 2a), and is then transformed into a human-readable SDFG as an Intermediate Representation (IR, Fig. 2b). The SDFG can then be modified without changing the original code, and as long as the dataflow aspects do not change, the original code can be updated while keeping SDFG transformations intact. What differentiates the SDFG from other IRs is the ability to hierarchically and parametrically view data movement, where scopes in the graph contain overall data requirements. This enables reusing transformations (e.g., tiling) at different levels of the memory hierarchy, as well as performing cross-level optimizations.

The modifications to the SDFG are not completely automatic. Rather, they are made by the performance engineer as a result of informed decisions based on the program structure, hardware information, and intermediate performance results. To support this, a transformation interface and common optimization libraries should be at the performance engineer's disposal, enabling modification of the IR in a verifiable manner (i.e., without breaking semantics), either programmatically or interactively. The domain scientist, in turn, writes an entire application once for all architectures, and can freely update the underlying calculations without undoing optimizations on the SDFG.

Conceptually, we perform the separation of computation from data movement logic by viewing programs as data flowing between operations, much like Dataflow and Flow-Based Programming. One key difference between dataflow and data-centric parallel programming, however, is that in a pure dataflow model execution is stateless, which means that constructs such as loops have to be unrolled. At the other extreme, traditional, control-centric programs revolve around statements that are executed in order. Data-centric parallel programming promotes the use of stateful dataflow, in which execution order depends first on data dependencies, but also on a global execution state. The former fosters the expression of concurrency, whereas the latter increases expressiveness and compactness by enabling concepts such as loops and data-dependent execution. The resulting concurrency works in several granularities, from utilizing processing elements on the same chip, to ensuring overlapped copy and execution of programs on accelerators in clusters. A data-centric model combines the following concepts:

(1) **Separating Containers from Computation**: Data-holding constructs with volatile or non-volatile information are defined as separate entities from computations, which consist of stateless functional units that perform arithmetic or logical operations in any granularity.

(2) **Dataflow**: The concept of information moving from one container or computation to another. This may be translated to copying, communication, or other forms of movement.

(3) **States**: Constructs that provide a mechanism to introduce execution order independent of data movement.

(4) **Coarsening**: The ability to view parallel patterns in a hierarchical manner, e.g., by grouping repeating computations.

The resulting programming interface should thus enable these concepts without drastically modifying development process, both in terms of languages and integration with existing codebases.

**2.1 Domain Scientist Interface**

**Languages** Scientific applications typically employ different programming models and Domain-Specific Languages (DSLs) to solve problems. To cater to the versatile needs of the domain scientists, SDFGs should be easily generated from various languages. We thus implement SDFG frontends in high-level languages (Python, MATLAB, TensorFlow), and provide a low-level (builder) API to easily map other DSLs to SDFGs. In the rest of this section, we focus on the Python interface, which is the most extensible.

**Interface** The Python interface creates SDFGs from restricted Python code, supporting numpy operators and functions, as well as the option to explicitly specify dataflow. In Fig. 2a, we demonstrate the data-centric interface on a one-dimensional Laplace operator. DaCe programs exist as decorated, strongly-typed functions in the application ecosystem, so that they can interact with existing codes using array-based interfaces (bottom of figure). The Python interface contains primitives such as map and reduce (which translate directly into SDFG components), allows programmers to use multi-dimensional arrays, and implements an extensible subset of operators from numpy on such arrays to ease the use of linear algebra operators. For instance, the code A @ B generates the dataflow of a matrix multiplication.

**Extensibility** For operators and functions that are not implemented, a user can easily provide dataflow implementations using decorated functions (@dace.replaces('numpy.conj')) that describe the SDFG. Otherwise, unimplemented functions fall-back into Python, casting the array pointers (which may be defined internally in the DaCe program) into numpy arrays and emitting a "potential slowdown" warning. If the syntax is unsupported (e.g., dynamic dictionaries), an error is raised.

**Explicit Dataflow** If the programmer does not use predefined operators (e.g., for custom element-wise computation), dataflow "intrinsics" can be explicitly defined separately from code, in constructs which we call Tasklets. Specifically, tasklet functions cannot access data unless it was explicitly moved in or out using predeclared operators (<<, >>) on arrays, as shown in the code.

Data movement operations (memlets) can be versatile, and the Python syntax of explicit memlets is defined using the syntax shown in Fig. 3. First, a local variable (i.e., that can be used in computation) is defined, whether it is an input or an output. After the direction of the movement, the data container is specified, along with an optional range (or index). In some applications (e.g., with indirect or data-dependent access), it is a common occurrence that the subset of the accessed data is known, but not exact indices; specifying memory access constraints both enables this behavior and facilitates access tracking for decomposition, e.g., which data to send to an accelerator. Finally, the two optional values in parentheses govern the nature of the access — the number of data elements moved, used for performance modeling, and a lambda function that is called when write-conflicts may occur.

Using explicit dataflow is beneficial when defining nontrivial data accesses. Fig. 4 depicts a full implementation of Sparse Matrix-Vector multiplication (SpMV). In the implementation, the access x[A_col[j]] is translated into an indirect access subgraph that can be identified and used in transformations.

**External Code** Supporting scientific code, in terms of performance and productivity, requires the ability to call previously-defined functions or invoke custom code (e.g., intrinsics or assembly). In addition to falling back to Python, the frontend enables defining tasklet code in the generated code language directly. In Fig. 5 we see a DaCe program that calls a BLAS function directly. The semantics of such tasklets require that memlets are defined separately (for correctness); the code can in turn interact with the memory directly (memlets that are larger than one element are pointers). With this feature, users can use existing codes and benefit from concurrent scheduling that the SDFG provides.

**Parametric Dimensions** To support parametric sizes (e.g., of arrays and maps) in DaCe, we utilize symbolic math evaluation. In particular, we extend the SymPy library to support our expressions and strong typing. The code can thus define symbolic sizes and use complex memlet subset expressions, which will be analyzed during SDFG compilation. The separation of access and computation, flexible interface, and symbolic sizes are the core enablers of data-centric parallel programming, helping domain scientists create programs that are amenable to efficient hardware mapping.

---

### النسخة العربية

تدور الأساليب الحالية في تحسينات الحوسبة عالية الأداء حول تحسين موضعية البيانات. بغض النظر عن المعمارية الأساسية، الهدف هو الحفاظ على المعلومات قريبة قدر الإمكان من عناصر المعالجة وتعزيز إعادة استخدام الذاكرة. حتى التطبيق البسيط، مثل ضرب المصفوفات، يتطلب مراحل متعددة من التحويلات، بما في ذلك تعديلات تخطيط البيانات (التعبئة) والتخزين المؤقت المدرك للسجلات. لأن التحسينات لا تعدل الحسابات وتختلف لكل معمارية، فإن الحفاظ على قابلية نقل الأداء للتطبيقات العلمية يتطلب فصل دلالات الحساب عن حركة البيانات.

تتيح SDFGs فصل تطوير التطبيق إلى مرحلتين، كما هو موضح في الشكل 2. يتم صياغة المشكلة كبرنامج عالي المستوى (الشكل 2أ)، ثم يتم تحويله إلى SDFG قابل للقراءة من قبل الإنسان كتمثيل وسيط (IR، الشكل 2ب). يمكن بعد ذلك تعديل SDFG دون تغيير الشفرة الأصلية، وطالما أن جوانب تدفق البيانات لا تتغير، يمكن تحديث الشفرة الأصلية مع الحفاظ على تحويلات SDFG سليمة. ما يميز SDFG عن IRs الأخرى هو القدرة على عرض حركة البيانات بشكل هرمي وبارامتري، حيث تحتوي النطاقات في الرسم البياني على متطلبات البيانات الإجمالية. هذا يتيح إعادة استخدام التحويلات (على سبيل المثال، التبليط) على مستويات مختلفة من التسلسل الهرمي للذاكرة، بالإضافة إلى إجراء تحسينات عبر المستويات.

التعديلات على SDFG ليست تلقائية تمامًا. بدلاً من ذلك، يتم إجراؤها من قبل مهندس الأداء نتيجة لقرارات مستنيرة بناءً على بنية البرنامج ومعلومات الأجهزة ونتائج الأداء الوسيطة. لدعم هذا، يجب أن تكون واجهة التحويل ومكتبات التحسين الشائعة تحت تصرف مهندس الأداء، مما يتيح تعديل IR بطريقة قابلة للتحقق (أي دون كسر الدلالات)، إما برمجيًا أو تفاعليًا. في المقابل، يكتب عالم المجال تطبيقًا كاملاً مرة واحدة لجميع المعماريات، ويمكنه تحديث الحسابات الأساسية بحرية دون التراجع عن التحسينات على SDFG.

من الناحية المفاهيمية، نقوم بفصل الحساب عن منطق حركة البيانات من خلال عرض البرامج كبيانات تتدفق بين العمليات، تمامًا مثل تدفق البيانات والبرمجة القائمة على التدفق. ومع ذلك، فإن الفرق الرئيسي بين تدفق البيانات والبرمجة المتوازية المحورية للبيانات هو أنه في نموذج تدفق البيانات الخالص يكون التنفيذ عديم الحالة، مما يعني أن البنى مثل الحلقات يجب أن يتم فكها. في الطرف الآخر، تدور البرامج التقليدية المحورية للتحكم حول العبارات التي يتم تنفيذها بالترتيب. تعزز البرمجة المتوازية المحورية للبيانات استخدام تدفق البيانات الحافظ للحالة، حيث يعتمد ترتيب التنفيذ أولاً على اعتماديات البيانات، ولكن أيضًا على حالة تنفيذ عالمية. يعزز الأول التعبير عن التزامن، بينما يزيد الأخير من التعبير والضغط من خلال تمكين مفاهيم مثل الحلقات والتنفيذ المعتمد على البيانات. يعمل التزامن الناتج في عدة حبيبات، من استخدام عناصر المعالجة على نفس الرقاقة، إلى ضمان النسخ المتداخل وتنفيذ البرامج على المسرعات في المجموعات. يجمع النموذج المحوري للبيانات المفاهيم التالية:

(1) **فصل الحاويات عن الحساب**: يتم تعريف البنى التي تحتوي على بيانات متطايرة أو غير متطايرة ككيانات منفصلة عن الحسابات، والتي تتكون من وحدات وظيفية عديمة الحالة تقوم بعمليات حسابية أو منطقية في أي حبيبة.

(2) **تدفق البيانات**: مفهوم المعلومات التي تنتقل من حاوية أو حساب إلى آخر. قد يُترجم هذا إلى النسخ أو الاتصال أو أشكال أخرى من الحركة.

(3) **الحالات**: بنى توفر آلية لإدخال ترتيب التنفيذ بشكل مستقل عن حركة البيانات.

(4) **التخشين**: القدرة على عرض الأنماط المتوازية بطريقة هرمية، على سبيل المثال، عن طريق تجميع الحسابات المتكررة.

يجب أن تمكّن واجهة البرمجة الناتجة هذه المفاهيم دون تعديل عملية التطوير بشكل جذري، سواء من حيث اللغات أو التكامل مع قواعد الشفرات الموجودة.

**2.1 واجهة عالم المجال**

**اللغات** عادةً ما تستخدم التطبيقات العلمية نماذج برمجة مختلفة ولغات خاصة بالمجال (DSLs) لحل المشكلات. لتلبية الاحتياجات المتنوعة لعلماء المجال، يجب أن يتم إنشاء SDFGs بسهولة من لغات مختلفة. وبالتالي، نقوم بتنفيذ واجهات أمامية لـ SDFG في لغات عالية المستوى (Python وMATLAB وTensorFlow)، ونوفر واجهة برمجة تطبيقات منخفضة المستوى (البناء) لتخطيط DSLs الأخرى بسهولة إلى SDFGs. في بقية هذا القسم، نركز على واجهة Python، وهي الأكثر قابلية للتوسع.

**الواجهة** تنشئ واجهة Python SDFGs من شفرة Python المقيدة، ودعم عوامل ووظائف numpy، بالإضافة إلى خيار تحديد تدفق البيانات بشكل صريح. في الشكل 2أ، نوضح الواجهة المحورية للبيانات على مشغل لابلاس أحادي البعد. توجد برامج DaCe كدوال مزينة ومكتوبة بقوة في نظام التطبيق البيئي، بحيث يمكنها التفاعل مع الشفرات الموجودة باستخدام واجهات قائمة على المصفوفات (أسفل الشكل). تحتوي واجهة Python على عوامل أولية مثل map وreduce (التي تُترجم مباشرةً إلى مكونات SDFG)، وتسمح للمبرمجين باستخدام مصفوفات متعددة الأبعاد، وتنفذ مجموعة قابلة للتوسع من عوامل numpy على هذه المصفوفات لتسهيل استخدام عوامل الجبر الخطي. على سبيل المثال، الشفرة A @ B تولد تدفق بيانات لضرب المصفوفات.

**قابلية التوسع** للعوامل والوظائف غير المطبقة، يمكن للمستخدم توفير تطبيقات تدفق البيانات بسهولة باستخدام الدوال المزينة (@dace.replaces('numpy.conj')) التي تصف SDFG. خلاف ذلك، تعود الوظائف غير المطبقة إلى Python، وتلقي مؤشرات المصفوفة (التي قد يتم تعريفها داخليًا في برنامج DaCe) في مصفوفات numpy وتبعث تحذير "تباطؤ محتمل". إذا كان التركيب غير مدعوم (على سبيل المثال، القواميس الديناميكية)، يتم رفع خطأ.

**تدفق البيانات الصريح** إذا لم يستخدم المبرمج عوامل معرفة مسبقًا (على سبيل المثال، للحساب المخصص على مستوى العناصر)، يمكن تعريف "جوهريات" تدفق البيانات بشكل صريح بشكل منفصل عن الشفرة، في بنى نسميها Tasklets. على وجه التحديد، لا يمكن لدوال tasklet الوصول إلى البيانات ما لم يتم نقلها بشكل صريح داخل أو خارج باستخدام عوامل محددة مسبقًا (<<, >>) على المصفوفات، كما هو موضح في الشفرة.

يمكن أن تكون عمليات حركة البيانات (memlets) متنوعة، ويتم تعريف تركيب Python للـ memlets الصريحة باستخدام التركيب الموضح في الشكل 3. أولاً، يتم تعريف متغير محلي (أي يمكن استخدامه في الحساب)، سواء كان إدخالًا أو إخراجًا. بعد اتجاه الحركة، يتم تحديد حاوية البيانات، جنبًا إلى جنب مع نطاق اختياري (أو فهرس). في بعض التطبيقات (على سبيل المثال، مع الوصول غير المباشر أو المعتمد على البيانات)، من الشائع أن تكون مجموعة فرعية من البيانات التي يتم الوصول إليها معروفة، ولكن ليس الفهارس الدقيقة؛ يتيح تحديد قيود الوصول إلى الذاكرة هذا السلوك ويسهل تتبع الوصول للتحلل، على سبيل المثال، البيانات التي يتم إرسالها إلى مسرع. أخيرًا، تحكم القيمتان الاختياريتان بين الأقواس طبيعة الوصول - عدد عناصر البيانات المنقولة، المستخدمة لنمذجة الأداء، ودالة lambda التي يتم استدعاؤها عند حدوث تعارضات الكتابة.

استخدام تدفق البيانات الصريح مفيد عند تعريف وصولات البيانات غير البسيطة. يصور الشكل 4 تطبيقًا كاملاً لضرب المصفوفة المتفرقة-المتجه (SpMV). في التطبيق، يتم ترجمة الوصول x[A_col[j]] إلى رسم بياني فرعي للوصول غير المباشر يمكن تحديده واستخدامه في التحويلات.

**الشفرة الخارجية** دعم الشفرة العلمية، من حيث الأداء والإنتاجية، يتطلب القدرة على استدعاء الدوال المعرفة مسبقًا أو استدعاء شفرة مخصصة (على سبيل المثال، الجوهريات أو التجميع). بالإضافة إلى العودة إلى Python، تمكّن الواجهة الأمامية من تعريف شفرة tasklet في لغة الشفرة المولدة مباشرةً. في الشكل 5 نرى برنامج DaCe يستدعي دالة BLAS مباشرةً. تتطلب دلالات هذه tasklets أن يتم تعريف memlets بشكل منفصل (للصحة)؛ يمكن للشفرة بدورها التفاعل مع الذاكرة مباشرةً (memlets الأكبر من عنصر واحد هي مؤشرات). مع هذه الميزة، يمكن للمستخدمين استخدام الشفرات الموجودة والاستفادة من الجدولة المتزامنة التي توفرها SDFG.

**الأبعاد البارامترية** لدعم الأحجام البارامترية (على سبيل المثال، للمصفوفات والخرائط) في DaCe، نستخدم تقييم الرياضيات الرمزية. على وجه الخصوص، نوسع مكتبة SymPy لدعم تعبيراتنا والكتابة القوية. يمكن للشفرة بالتالي تعريف أحجام رمزية واستخدام تعبيرات مجموعة فرعية memlet معقدة، والتي سيتم تحليلها أثناء تجميع SDFG. الفصل بين الوصول والحساب، والواجهة المرنة، والأحجام الرمزية هي الممكّنات الأساسية للبرمجة المتوازية المحورية للبيانات، مما يساعد علماء المجال على إنشاء برامج قابلة للتخطيط الفعال للأجهزة.

---

### Translation Notes

- **Figures referenced:** Figure 2, 3, 4, 5
- **Key terms introduced:** memlets, tasklets, dataflow, data locality, coarsening
- **Equations:** 0
- **Citations:** References to SymPy, numpy, BLAS
- **Special handling:** Code examples preserved in English; technical syntax maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
