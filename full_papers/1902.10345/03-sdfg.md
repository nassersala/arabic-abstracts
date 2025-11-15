# Section 3: Stateful Dataflow Multigraphs
## القسم 3: الرسوم البيانية المتعددة لتدفق البيانات الحافظة للحالة

**Section:** SDFG Definition and Components
**Translation Quality:** 0.86
**Glossary Terms Used:** dataflow, state machine, parallelism, concurrency, GPU, FPGA, CPU

---

### English Version

We define an SDFG as a directed graph of directed acyclic multigraphs, whose components are summarized in Table 1. Briefly, the SDFG is composed of acyclic dataflow multigraphs, in which nodes represent containers or computation, and edges (memlets) represent data movement. To support cyclic data dependencies and control-flow, these multigraphs reside in State nodes at the top-level graph. Following complete execution of the dataflow in a state, state transition edges on the top-level graph specify conditions and assignments, forming a state machine.

**3.1 Containers**

As a data-centric model, SDFGs offer two forms of data containers: Data and Stream nodes. Data nodes represent a location in memory that is mapped to a multi-dimensional array, whereas Stream nodes are defined as multi-dimensional arrays of concurrent queues, which can be accessed using push/pop semantics. Containers are tied to a specific storage location (as a node property), which may be on a GPU or even a file. In the generated code, memlets between containers either generate appropriate memory copy operations or fail with illegal accesses. In FPGAs, Stream nodes instantiate FIFO interfaces that can be used to connect hardware modules. Another property of containers is whether they are transient, i.e., only allocated for the duration of SDFG execution.

**3.2 Computation**

Tasklet nodes contain stateless, arbitrary computational functions of any granularity. The SDFG is designed for fine-grained tasklets, so as to enable performance engineers to analyze and optimize the most out of the code, leaving computational semantics intact. Throughout the process of data-centric transformations and compilation, the tasklet code remains immutable.

**3.3 Concurrency**

Expressing parallelism is inherent in SDFGs by design, supported by the Map and Consume scopes. Map scopes represent parallel computation on all levels, and can be nested hierarchically. This feature consolidates many parallel programming concepts, including multi-threading, GPU kernels, multi-GPU synchronization, and multiple processing elements on FPGAs. When mapped to multicore CPUs, Map scopes generate OpenMP parallel for loops; for GPUs, device schedules generate CUDA kernels, whereas thread-block schedules determine the dimensions of blocks; for FPGAs, Maps synthesize different hardware modules as processing elements.

Consume scopes enable producer/consumer relationships via dynamic processing of streams. Different connected components within an SDFG multigraph also run concurrently (by definition). These concepts are automatically managed by the SDFG's representation of concurrency.

**3.4 State**

Sequential operation in SDFGs either implicitly occurs following data dependencies, or explicitly specified using multiple states. State transition edges define a condition, which can depend on data in containers, and a list of assignments to inter-state symbols. The concept of a state machine enables both complex control flow patterns, such as imperfectly nested loops, and data-dependent execution.

To enable control-flow within data-flow, or a parametric number of state machines, SDFGs can be nested via the Invoke node. The semantics of Invoke are equivalent to a tasklet, thereby disallowing access to external memory without memlets.

---

### النسخة العربية

نعرّف SDFG كرسم بياني موجه من الرسوم البيانية المتعددة اللاحلقية الموجهة، التي يتم تلخيص مكوناتها في الجدول 1. باختصار، يتكون SDFG من رسوم بيانية متعددة لاحلقية لتدفق البيانات، حيث تمثل العقد الحاويات أو الحسابات، وتمثل الحواف (memlets) حركة البيانات. لدعم الاعتماديات الدورية للبيانات وتدفق التحكم، تتواجد هذه الرسوم البيانية المتعددة في عقد الحالة على الرسم البياني عالي المستوى. بعد الانتهاء من تنفيذ تدفق البيانات في حالة ما، تحدد حواف انتقال الحالة على الرسم البياني عالي المستوى الشروط والتعيينات، مكونةً آلة حالة.

**3.1 الحاويات**

كنموذج محوري للبيانات، توفر SDFGs شكلين من حاويات البيانات: عقد البيانات والتدفق. تمثل عقد البيانات موقعًا في الذاكرة يتم تخطيطه إلى مصفوفة متعددة الأبعاد، بينما يتم تعريف عقد التدفق كمصفوفات متعددة الأبعاد من قوائم الانتظار المتزامنة، والتي يمكن الوصول إليها باستخدام دلالات الدفع/السحب. ترتبط الحاويات بموقع تخزين محدد (كخاصية عقدة)، والذي قد يكون على GPU أو حتى ملف. في الشفرة المولدة، تولد memlets بين الحاويات إما عمليات نسخ الذاكرة المناسبة أو تفشل مع وصولات غير قانونية. في FPGAs، تُنشئ عقد التدفق واجهات FIFO التي يمكن استخدامها لربط وحدات الأجهزة. خاصية أخرى للحاويات هي ما إذا كانت عابرة، أي يتم تخصيصها فقط لمدة تنفيذ SDFG.

**3.2 الحساب**

تحتوي عقد Tasklet على دوال حسابية عديمة الحالة وعشوائية بأي حبيبة. تم تصميم SDFG لـ tasklets دقيقة الحبيبات، لتمكين مهندسي الأداء من تحليل وتحسين معظم الشفرة، مع ترك دلالات الحساب سليمة. طوال عملية التحويلات المحورية للبيانات والتجميع، تظل شفرة tasklet غير قابلة للتغيير.

**3.3 التزامن**

التعبير عن التوازي متأصل في SDFGs بالتصميم، مدعومًا بنطاقات Map وConsume. تمثل نطاقات Map الحساب المتوازي على جميع المستويات، ويمكن تداخلها بشكل هرمي. تدمج هذه الميزة العديد من مفاهيم البرمجة المتوازية، بما في ذلك تعدد الخيوط، ونوى GPU، ومزامنة multi-GPU، وعناصر المعالجة المتعددة على FPGAs. عند التخطيط إلى وحدات المعالجة المركزية متعددة النوى، تولد نطاقات Map حلقات OpenMP parallel for؛ لـ GPUs، تولد جداول الأجهزة نوى CUDA، بينما تحدد جداول كتلة الخيط أبعاد الكتل؛ لـ FPGAs، تركب Maps وحدات أجهزة مختلفة كعناصر معالجة.

تمكّن نطاقات Consume علاقات المنتج/المستهلك عبر المعالجة الديناميكية للتدفقات. المكونات المتصلة المختلفة داخل رسم بياني متعدد SDFG تعمل أيضًا بشكل متزامن (بالتعريف). تتم إدارة هذه المفاهيم تلقائيًا بواسطة تمثيل SDFG للتزامن.

**3.4 الحالة**

العملية التسلسلية في SDFGs إما تحدث ضمنيًا بعد اعتماديات البيانات، أو محددة بشكل صريح باستخدام حالات متعددة. تحدد حواف انتقال الحالة شرطًا، يمكن أن يعتمد على البيانات في الحاويات، وقائمة من التعيينات لرموز بين الحالات. يتيح مفهوم آلة الحالة كلاً من أنماط تدفق التحكم المعقدة، مثل الحلقات المتداخلة بشكل غير كامل، والتنفيذ المعتمد على البيانات.

لتمكين تدفق التحكم داخل تدفق البيانات، أو عدد بارامتري من آلات الحالة، يمكن تداخل SDFGs عبر عقدة Invoke. دلالات Invoke مكافئة لـ tasklet، وبالتالي تمنع الوصول إلى الذاكرة الخارجية بدون memlets.

---

### Translation Notes

- **Figures referenced:** Table 1, Figures 6-10
- **Key terms introduced:** Map scope, Consume scope, State machine, Invoke node, memlets, tasklets
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Technical terminology for graph structures and parallel programming

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
