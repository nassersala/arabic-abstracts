# Section 4: The Tiramisu IR
## القسم 4: التمثيل الوسيط لـ Tiramisu

**Section:** tiramisu-ir
**Translation Quality:** 0.88
**Glossary Terms Used:** intermediate representation (IR), polyhedral model, integer sets, maps, iteration domain, affine constraints, loop transformation, data layout, memory hierarchy, scheduling, code generation, lexicographical order, ISL (Integer Set Library)

---

### English Version

The main goal of TIRAMISU's multi-layer intermediate representation is to simplify the implementation of scheduling commands by applying them in a specific order. This section illustrates why, and describes the layers of the TIRAMISU IR.

**A. Rationale for a Multi-layer IR**

In this section we provide examples showing why current intermediate representations are not adequate for TIRAMISU and why we need a multi-layer IR.

Most current intermediate representations use memory to communicate between program statements. This creates memory-based dependencies in the program, and forces compilers to choose data layout before deciding on optimizations and mapping to hardware. Optimizing a program for different hardware architectures usually requires modifying the data layout and eliminating memory-based dependencies since they restrict optimizations [31]. Thus, any data layout specified before scheduling must be undone to allow more freedom for scheduling, and the code must be adapted to use the data-layout best-suited for the target hardware. Applying these data-layout transformations and the elimination of memory-based dependencies is challenging [23], [45], [30], [17], [33], [32], [29], [38], [13].

Another example that demonstrates the complexity of code generation is mapping buffers to shared and local memory on GPU. The amount of data that needs to be copied to shared memory and when to perform synchronization both depend on how the code is optimized (for example, whether the code has two-level tiling or not). The same applies to deciding the amount of data to send or receive when generating distributed code. Therefore, buffer mapping to memory hierarchies, communication management, and synchronization should not occur before scheduling.

TIRAMISU addresses these complexities in code generation by using a multi-layer IR that fully separates the architecture-independent algorithm from loop transformations, data layout and communication. The first layer representation describes the pure algorithm using producer-consumer relationships without memory locations. The second layer specifies the order of computation, along with which processor computes each value; this layer is suitable for performing a vast number of optimizations without dealing with concrete memory layouts. The third layer specifies where to store intermediate data before they are consumed. The fourth layer adds all the necessary communication and synchronization operations.

The separation of layers defines a specific order for applying optimizations and ensures that compiler passes in a given layer need not to worry about modifying or undoing a decision made in an earlier layer. For example, the phase that specifies the order of computations and where they occur can safely assume that no data-layout transformations are required. This simple assumption allows TIRAMISU to avoid the need to rely on a large body of research that focuses on data-layout transformations to allow scheduling [23], [45], [30], [17], [33], [32], [29], [38], [13].

**B. Background**

In this section, we provide an overview of two main concepts used in the polyhedral model: integer sets and maps. These two concepts will be used in later sections to define the different IR layers.

Integer sets represent iteration domains while maps are used to represent memory accesses and to transform iteration domains and memory accesses (apply loop nest and memory access transformations). More details and formal definitions for these concepts are provided in [47], [2], [36].

An integer set is a set of integer tuples described using affine constraints. An example of a set of integer tuples is:

{(1, 1); (2, 1); (3, 1); (1, 2); (2, 2); (3, 2)}

Instead of listing all the tuples as we do in the previous set, we can describe the set using affine constraints over loop iterators and symbolic constants as follows:

{S(i, j) : 1 ≤ i ≤ 3 ∧ 1 ≤ j ≤ 2}

where i and j are the dimensions of the tuples in the set.

A map is a relation between two integer sets. For example:

{S1(i, j) → S2(i + 2, j + 2) : 1 ≤ i ≤ 3 ∧ 1 ≤ j ≤ 2}

is a map between tuples in the set S1 and tuples in the set S2 (e.g. the tuple S1(i, j) maps to the tuple S2(i + 2, j + 2)).

All sets and maps in TIRAMISU are implemented using the Integer Set Library (ISL) [47]. We also use the ISL library notation for sets and maps throughout the paper.

**C. The Multi-Layer IR**

A typical workflow for using TIRAMISU is illustrated in Figure 4. The user writes the pure algorithm and provides a set of scheduling commands. The first layer of the IR is then transformed into lower layers, and finally TIRAMISU generates LLVM or other appropriate low-level IR. TIRAMISU uses integer sets to represent each of the four IR layers and uses maps to represent transformations on the iteration domain and data layout. The remainder of this section describes the four layers of the TIRAMISU IR.

**1) Layer I (Abstract Algorithm):** Layer I of TIRAMISU specifies the algorithm without specifying when and where computations occur, how data should be stored in memory, or communication. Values are communicated via explicit producer-consumer relationships.

For example, the Layer I representation of the code in Figure 2 for the computation by is as follows:

{by(i, j, c) : 0 ≤ i < N − 2 ∧ 0 ≤ j < M − 2 ∧ 0 ≤ c < 3} :
(bx(i, j, c) + bx(i + 1, j, c) + bx(i + 2, j, c))/3

The first part specifies the iteration domain of the computation by, while the second part is the computed expression. Computations in Layer I are not ordered; declaration order does not affect the order of execution, which is specified in Layer II.

**2) Layer II (Computation Management):** Layer II of TIRAMISU specifies the order of execution of computations and the processor on which they execute. This layer does not specify how intermediate values are stored in memory; this simplifies optimization passes since these transformations do not need to perform complicated data-layout transformations. The transformation of Layer I into Layer II is done automatically using scheduling commands.

Computations in Layer II are ordered based on their lexicographical order. The set before the colon in the representation is an ordered set of computations. Tags like gpuB indicate that iterations are mapped to specific hardware (GPU blocks, threads, etc.).

Computations in this layer are ordered and assigned to a particular processor; the order is dictated by time dimensions and space dimensions. Time dimensions specify the order of execution relative to other computations while space dimensions specify on which processor each computation executes. Space dimensions are distinguished from time dimensions using tags.

Currently, TIRAMISU supports the following space tags:
- **cpu:** the dimension runs on a CPU in a shared memory system
- **node:** the dimension maps to nodes in a distributed system
- **gpuT:** the dimension maps to a gpu thread dimension
- **gpuB:** the dimension maps to a gpu block dimension

Other tags that transform a dimension include:
- **vec(s):** vectorize the dimension (s is the vector length)
- **unroll:** unroll the dimension

**3) Layer III (Data Management):** Layer III makes the data layout concrete by specifying where intermediate values are stored. Any necessary buffer allocations/deallocations are also constructed in this level. TIRAMISU generates this layer automatically from Layer II by applying the scheduling commands for data mapping.

The data management layer specifies memory locations for storing computed values. It consists of the Layer II representation along with allocation/deallocation statements, and a set of access relations, which map a computation from Layer II to array elements read or written by that computation.

Data mapping in TIRAMISU is an affine relation that maps each computation to a buffer element. TIRAMISU allows any data-layout mapping expressible as an affine relation.

**4) Layer IV (Communication Management):** Layer IV adds synchronization and communication operations to the representation, mapping them to the time-space domain, and concretizes when statements for buffer allocation/deallocation occur. This layer is generated automatically from Layer III by applying user-specified commands.

---

### النسخة العربية

الهدف الرئيسي للتمثيل الوسيط متعدد الطبقات لـ TIRAMISU هو تبسيط تنفيذ أوامر الجدولة من خلال تطبيقها بترتيب محدد. يوضح هذا القسم السبب، ويصف طبقات التمثيل الوسيط لـ TIRAMISU.

**أ. الأساس المنطقي للتمثيل الوسيط متعدد الطبقات**

في هذا القسم نقدم أمثلة توضح لماذا التمثيلات الوسيطة الحالية غير كافية لـ TIRAMISU ولماذا نحتاج إلى تمثيل وسيط متعدد الطبقات.

تستخدم معظم التمثيلات الوسيطة الحالية الذاكرة للتواصل بين عبارات البرنامج. هذا ينشئ اعتماديات قائمة على الذاكرة في البرنامج، ويجبر المترجمات على اختيار تخطيط البيانات قبل اتخاذ قرار بشأن التحسينات والتخطيط على الأجهزة. عادةً ما يتطلب تحسين برنامج لمعماريات أجهزة مختلفة تعديل تخطيط البيانات والقضاء على الاعتماديات القائمة على الذاكرة لأنها تقيد التحسينات [31]. وبالتالي، يجب التراجع عن أي تخطيط بيانات محدد قبل الجدولة للسماح بمزيد من الحرية للجدولة، ويجب تكييف الشفرة لاستخدام تخطيط البيانات الأنسب للأجهزة المستهدفة. إن تطبيق تحويلات تخطيط البيانات هذه والقضاء على الاعتماديات القائمة على الذاكرة يمثل تحدياً [23]، [45]، [30]، [17]، [33]، [32]، [29]، [38]، [13].

مثال آخر يوضح تعقيد توليد الشفرة هو تخطيط المخازن المؤقتة على الذاكرة المشتركة والمحلية في GPU. كمية البيانات التي تحتاج إلى النسخ إلى الذاكرة المشتركة ومتى يتم تنفيذ المزامنة يعتمدان على كيفية تحسين الشفرة (على سبيل المثال، ما إذا كانت الشفرة تحتوي على تبليط ثنائي المستوى أم لا). وينطبق الشيء نفسه على تحديد كمية البيانات المراد إرسالها أو استقبالها عند توليد الشفرة الموزعة. لذلك، لا ينبغي أن يحدث تخطيط المخزن المؤقت على التسلسلات الهرمية للذاكرة، وإدارة الاتصال، والمزامنة قبل الجدولة.

يعالج TIRAMISU هذه التعقيدات في توليد الشفرة باستخدام تمثيل وسيط متعدد الطبقات يفصل بشكل كامل الخوارزمية المستقلة عن المعمارية عن تحويلات الحلقات وتخطيط البيانات والاتصال. يصف تمثيل الطبقة الأولى الخوارزمية النقية باستخدام علاقات منتج-مستهلك بدون مواقع ذاكرة. تحدد الطبقة الثانية ترتيب الحساب، جنباً إلى جنب مع المعالج الذي يحسب كل قيمة؛ هذه الطبقة مناسبة لإجراء عدد كبير من التحسينات دون التعامل مع تخطيطات ذاكرة ملموسة. تحدد الطبقة الثالثة مكان تخزين البيانات الوسيطة قبل استهلاكها. تضيف الطبقة الرابعة جميع عمليات الاتصال والمزامنة اللازمة.

يحدد فصل الطبقات ترتيباً محدداً لتطبيق التحسينات ويضمن أن تمريرات المترجم في طبقة معينة لا تحتاج إلى القلق بشأن تعديل أو التراجع عن قرار تم اتخاذه في طبقة سابقة. على سبيل المثال، يمكن للمرحلة التي تحدد ترتيب الحسابات ومكان حدوثها أن تفترض بأمان أنه لا حاجة لتحويلات تخطيط البيانات. يسمح هذا الافتراض البسيط لـ TIRAMISU بتجنب الحاجة إلى الاعتماد على مجموعة كبيرة من الأبحاث التي تركز على تحويلات تخطيط البيانات للسماح بالجدولة [23]، [45]، [30]، [17]، [33]، [32]، [29]، [38]، [13].

**ب. الخلفية**

في هذا القسم، نقدم نظرة عامة على مفهومين رئيسيين يُستخدمان في النموذج متعدد السطوح: مجموعات الأعداد الصحيحة والتخطيطات. سيتم استخدام هذين المفهومين في الأقسام اللاحقة لتحديد طبقات التمثيل الوسيط المختلفة.

تمثل مجموعات الأعداد الصحيحة مجالات التكرار بينما تُستخدم التخطيطات لتمثيل وصولات الذاكرة ولتحويل مجالات التكرار ووصولات الذاكرة (تطبيق تحويلات أعشاش الحلقات ووصولات الذاكرة). يتم توفير مزيد من التفاصيل والتعريفات الرسمية لهذه المفاهيم في [47]، [2]، [36].

مجموعة الأعداد الصحيحة هي مجموعة من صفوف الأعداد الصحيحة الموصوفة باستخدام قيود أفينية. مثال على مجموعة من صفوف الأعداد الصحيحة هو:

{(1, 1); (2, 1); (3, 1); (1, 2); (2, 2); (3, 2)}

بدلاً من سرد جميع الصفوف كما نفعل في المجموعة السابقة، يمكننا وصف المجموعة باستخدام قيود أفينية على متكررات الحلقات والثوابت الرمزية كما يلي:

{S(i, j) : 1 ≤ i ≤ 3 ∧ 1 ≤ j ≤ 2}

حيث i وj هما أبعاد الصفوف في المجموعة.

التخطيط هو علاقة بين مجموعتي أعداد صحيحة. على سبيل المثال:

{S1(i, j) → S2(i + 2, j + 2) : 1 ≤ i ≤ 3 ∧ 1 ≤ j ≤ 2}

هو تخطيط بين الصفوف في المجموعة S1 والصفوف في المجموعة S2 (مثلاً، الصف S1(i, j) يُخطط إلى الصف S2(i + 2, j + 2)).

يتم تنفيذ جميع المجموعات والتخطيطات في TIRAMISU باستخدام مكتبة مجموعات الأعداد الصحيحة (ISL) [47]. نستخدم أيضاً ترميز مكتبة ISL للمجموعات والتخطيطات في جميع أنحاء الورقة.

**ج. التمثيل الوسيط متعدد الطبقات**

يوضح الشكل 4 سير العمل النموذجي لاستخدام TIRAMISU. يكتب المستخدم الخوارزمية النقية ويوفر مجموعة من أوامر الجدولة. ثم يتم تحويل الطبقة الأولى من التمثيل الوسيط إلى طبقات أدنى، وأخيراً يولد TIRAMISU LLVM أو تمثيل وسيط منخفض المستوى آخر مناسب. يستخدم TIRAMISU مجموعات الأعداد الصحيحة لتمثيل كل من طبقات التمثيل الوسيط الأربع ويستخدم التخطيطات لتمثيل التحويلات على مجال التكرار وتخطيط البيانات. يصف ما تبقى من هذا القسم الطبقات الأربع للتمثيل الوسيط لـ TIRAMISU.

**1) الطبقة I (الخوارزمية المجردة):** تحدد الطبقة I من TIRAMISU الخوارزمية دون تحديد متى وأين تحدث الحسابات، أو كيف يجب تخزين البيانات في الذاكرة، أو الاتصال. يتم نقل القيم عبر علاقات منتج-مستهلك صريحة.

على سبيل المثال، تمثيل الطبقة I للشفرة في الشكل 2 للحساب by هو كما يلي:

{by(i, j, c) : 0 ≤ i < N − 2 ∧ 0 ≤ j < M − 2 ∧ 0 ≤ c < 3} :
(bx(i, j, c) + bx(i + 1, j, c) + bx(i + 2, j, c))/3

يحدد الجزء الأول مجال التكرار للحساب by، بينما الجزء الثاني هو التعبير المحسوب. الحسابات في الطبقة I غير مرتبة؛ ترتيب الإعلان لا يؤثر على ترتيب التنفيذ، الذي يتم تحديده في الطبقة II.

**2) الطبقة II (إدارة الحساب):** تحدد الطبقة II من TIRAMISU ترتيب تنفيذ الحسابات والمعالج الذي تُنفذ عليه. لا تحدد هذه الطبقة كيفية تخزين القيم الوسيطة في الذاكرة؛ هذا يبسط تمريرات التحسين حيث لا تحتاج هذه التحويلات إلى إجراء تحويلات معقدة لتخطيط البيانات. يتم تحويل الطبقة I إلى الطبقة II تلقائياً باستخدام أوامر الجدولة.

يتم ترتيب الحسابات في الطبقة II بناءً على ترتيبها المعجمي. المجموعة قبل النقطتين في التمثيل هي مجموعة مرتبة من الحسابات. العلامات مثل gpuB تشير إلى أن التكرارات مخططة على أجهزة محددة (كتل GPU، خيوط، إلخ).

يتم ترتيب الحسابات في هذه الطبقة وتعيينها لمعالج معين؛ يتم تحديد الترتيب بواسطة أبعاد الزمن وأبعاد المكان. تحدد أبعاد الزمن ترتيب التنفيذ بالنسبة للحسابات الأخرى بينما تحدد أبعاد المكان على أي معالج يُنفذ كل حساب. يتم تمييز أبعاد المكان عن أبعاد الزمن باستخدام العلامات.

حالياً، يدعم TIRAMISU علامات المكان التالية:
- **cpu:** يعمل البعد على CPU في نظام ذاكرة مشتركة
- **node:** يُخطط البعد على عقد في نظام موزع
- **gpuT:** يُخطط البعد على بعد خيط gpu
- **gpuB:** يُخطط البعد على بعد كتلة gpu

العلامات الأخرى التي تحول بعداً تتضمن:
- **vec(s):** توجيه متجه للبعد (s هو طول المتجه)
- **unroll:** فك البعد

**3) الطبقة III (إدارة البيانات):** تجعل الطبقة III تخطيط البيانات ملموساً من خلال تحديد مكان تخزين القيم الوسيطة. يتم أيضاً إنشاء أي تخصيصات/إلغاء تخصيصات مخزن مؤقت ضرورية في هذا المستوى. يولد TIRAMISU هذه الطبقة تلقائياً من الطبقة II من خلال تطبيق أوامر الجدولة لتخطيط البيانات.

تحدد طبقة إدارة البيانات مواقع الذاكرة لتخزين القيم المحسوبة. تتكون من تمثيل الطبقة II جنباً إلى جنب مع عبارات التخصيص/إلغاء التخصيص، ومجموعة من علاقات الوصول، التي تخطط حساباً من الطبقة II إلى عناصر المصفوفة التي يقرأها أو يكتبها ذلك الحساب.

تخطيط البيانات في TIRAMISU هو علاقة أفينية تخطط كل حساب إلى عنصر مخزن مؤقت. يسمح TIRAMISU بأي تخطيط بيانات يمكن التعبير عنه كعلاقة أفينية.

**4) الطبقة IV (إدارة الاتصال):** تضيف الطبقة IV عمليات المزامنة والاتصال إلى التمثيل، وتخططها على مجال الزمان-المكان، وتحدد متى تحدث عبارات تخصيص/إلغاء تخصيص المخزن المؤقت. يتم توليد هذه الطبقة تلقائياً من الطبقة III من خلال تطبيق الأوامر المحددة من قبل المستخدم.

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 4 (workflow diagram)
- **Key terms introduced:** multi-layer IR, memory-based dependencies, producer-consumer relationships, integer sets, maps, affine constraints, integer tuples, ISL (Integer Set Library), lexicographical order, time dimensions, space dimensions, access relations
- **Equations:** Set notation examples, map examples
- **Citations:** Multiple references to polyhedral model literature [2], [13], [17], [23], [29], [30], [31], [32], [33], [36], [38], [45], [47]
- **Special handling:** Mathematical set notation preserved, ISL library references

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
