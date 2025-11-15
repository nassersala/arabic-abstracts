# Section 7: Related Work
## القسم 7: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.85
**Glossary Terms Used:** performance portability, dataflow, transformation, polyhedral, Legion, Halide

---

### English Version

Multiple previous works locally address issues posed in this paper. We discuss those papers below, and summarize them in Fig. 19.

**Performance Portability** Performance-portable programming models consist of high-performance libraries and programming languages. Kokkos and RAJA are task-based HPC libraries that provide parallel primitives. The Legion programming model defines hierarchical parallelism and asynchronous tasking by inferring data dependencies from access sets. Language and directive-based standards such as OpenCL, OpenACC, and OpenMP also provide portability. However, true performance portability cannot be achieved with these standards, as optimized code/directives vastly differ on each platform.

**Separation of Concerns** Multiple frameworks explicitly separate the computational algorithm from subsequent optimization schemes. In CHiLL, a user may write high-level transformation scripts for existing code. Image processing pipelines written in the Halide embedded DSL are defined as operations, whose schedule is separately generated. Tiramisu operates in a similar manner. In SPIRAL, high-level specifications of computational kernels are written in a DSL, followed by using breakdown and rewrite rules to lower them to optimized implementations.

**Dataflow Representations** Several IRs combine dataflow with control flow in graph form. The LLVM IR is a control-flow graph composed of basic blocks. Program Dependence Graphs (PDGs) represent statements and predicate expressions with nodes. HPVM extends the LLVM IR by introducing hierarchical dataflow graphs for mapping to accelerators. Other representations include Bamboo, Dryad, and Naiad.

**Data-Centric Transformations** Several representations provide a fixed set of high-level program transformations. Halide's schedules are by definition data-centric. HPVM also applies optimization passes such as tiling, node fusion, and mapping of data to GPU constant memory. Lift programs use rewrite rules to optimize expressions and map them to OpenCL constructs.

**Summary** In essence, SDFGs provide the expressiveness of a general-purpose programming language, while enabling performance portability without interfering with the original code. The SDFG is not limited to specific application classes or hardware, and the extensible data-centric transformations generalize existing code optimization approaches.

---

### النسخة العربية

تعالج أعمال سابقة متعددة محليًا القضايا المطروحة في هذه الورقة. نناقش هذه الأوراق أدناه، ونلخصها في الشكل 19.

**قابلية نقل الأداء** تتكون نماذج البرمجة القابلة لنقل الأداء من مكتبات عالية الأداء ولغات برمجة. Kokkos وRAJA هما مكتبتان HPC قائمتان على المهام توفران عوامل أولية متوازية. يعرّف نموذج برمجة Legion التوازي الهرمي والمهام غير المتزامنة من خلال استنتاج اعتماديات البيانات من مجموعات الوصول. توفر المعايير القائمة على اللغة والتوجيهات مثل OpenCL وOpenACC وOpenMP أيضًا قابلية النقل. ومع ذلك، لا يمكن تحقيق قابلية نقل الأداء الحقيقية مع هذه المعايير، حيث تختلف الشفرة/التوجيهات المحسّنة بشكل كبير على كل منصة.

**فصل المخاوف** تفصل أطر عمل متعددة بشكل صريح الخوارزمية الحسابية عن مخططات التحسين اللاحقة. في CHiLL، يمكن للمستخدم كتابة نصوص تحويل عالية المستوى للشفرة الموجودة. يتم تعريف خطوط أنابيب معالجة الصور المكتوبة في DSL المضمنة Halide كعمليات، يتم إنشاء جدولها بشكل منفصل. يعمل Tiramisu بطريقة مماثلة. في SPIRAL، يتم كتابة مواصفات عالية المستوى للنوى الحسابية في DSL، تليها استخدام قواعد التحلل وإعادة الكتابة لخفضها إلى تطبيقات محسّنة.

**تمثيلات تدفق البيانات** تجمع عدة IRs بين تدفق البيانات وتدفق التحكم في شكل رسم بياني. LLVM IR هو رسم بياني لتدفق التحكم يتكون من كتل أساسية. تمثل رسوم الاعتماديات البرمجية (PDGs) العبارات والتعبيرات المسندة بالعقد. يوسع HPVM LLVM IR من خلال تقديم رسوم بيانية هرمية لتدفق البيانات للتخطيط إلى المسرعات. تشمل التمثيلات الأخرى Bamboo وDryad وNaiad.

**التحويلات المحورية للبيانات** توفر عدة تمثيلات مجموعة ثابتة من تحويلات البرنامج عالية المستوى. جداول Halide محورية للبيانات بالتعريف. يطبق HPVM أيضًا تمريرات التحسين مثل التبليط ودمج العقد وتخطيط البيانات إلى ذاكرة GPU الثابتة. تستخدم برامج Lift قواعد إعادة الكتابة لتحسين التعبيرات وتخطيطها إلى بنى OpenCL.

**الملخص** في الجوهر، توفر SDFGs التعبير عن لغة برمجة ذات أغراض عامة، مع تمكين قابلية نقل الأداء دون التدخل في الشفرة الأصلية. لا يقتصر SDFG على فئات تطبيقات أو أجهزة محددة، والتحويلات المحورية للبيانات القابلة للتوسع تعمم أساليب تحسين الشفرة الموجودة.

---

### Translation Notes

- **Figures referenced:** Figure 19
- **Key terms introduced:** Kokkos, RAJA, Legion, CHiLL, Halide, Tiramisu, SPIRAL, LLVM, PDG, HPVM
- **Equations:** 0
- **Citations:** Extensive references to related frameworks and tools
- **Special handling:** Comparative analysis of related systems

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
