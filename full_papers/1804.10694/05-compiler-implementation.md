# Section 5: Compiler Implementation
## القسم 5: تنفيذ المترجم

**Section:** compiler-implementation
**Translation Quality:** 0.86
**Glossary Terms Used:** code generation, scheduling, transformation, intermediate representation, AST (abstract syntax tree), LLVM IR, CUDA, Halide, ISL, Cloog, polyhedral model, non-affine, predicate, loop bounds

---

### English Version

Since the main contribution of this paper is not in introducing new techniques for code generation, we only provide a high level overview of how TIRAMISU generates the IR layers and target code. Throughout the section, we refer the reader to the appropriate literature for more details.

In the rest of this section we describe how scheduling commands transform Layers I, II, III and IV. We also describe how target code is generated from Layer IV.

**a) Transforming Layer I into Layer II:** Transforming Layer I into Layer II is done using two types of scheduling commands: (1) commands for loop nest transformations (such as tile(), split(), shift(), interchange()); and (2) commands for mapping loop levels to hardware (including parallelize(), vectorize(), gpu()).

The first type of scheduling command applies a map that transforms the iteration domain. For example, when a tiling command is applied on the by computation in Figure 2, it gets translated into the following map:

{by(i, j, c) → by(i0, j0, i1, j1, c) : i0 = floor(i/32) ∧ i1 = i%32 ∧ j0 = floor(j/32) ∧ j1 = j%32 ∧ 0 ≤ i < N ∧ 0 ≤ j < N}

This map is then applied on the Layer I representation, producing the Layer II representation. Composing transformations is done by composing different maps, since the composition of two affine maps is an affine map.

The second type of command adds space tags to dimensions to indicate which loop levels to parallelize, vectorize, map to GPU blocks, and so on.

**b) Transforming Layer II into Layer III:** This is done by augmenting Layer II with access relations. By default, TIRAMISU uses identity access relations (i.e., access relations that store a computation C(i,j) into a buffer C[i,j]).

If the store_in() command is used, the access relation is deduced from that command instead. Buffer allocations are also added while transforming Layer II into Layer III. The scheduling command b.allocate_at(C, i) creates a new statement that allocates the buffer b in the same loop nest of the computation C but at loop level i.

**c) Transforming Layer III into Layer IV:** Scheduling commands for data communication (send and receive), synchronization, and for copying data between global, shared and local memory are all translated into statements. For example, the send() and receive() commands are translated into function calls that will be translated into MPI calls during code generation.

**A. Code Generation**

Generating code from the set of computations in Layer IV amounts to generating nested loops that visit each computation in the set, once and only once, while following the lexicographical ordering between the computations [5], [27], [38]. TIRAMISU relies on an implementation of the Cloog [5] code generation algorithm provided by the ISL library [47]. The TIRAMISU code generator takes Layer IV IR and generates an abstract syntax tree (AST). The AST is then traversed to generate lower level code for specific hardware architectures (depending on the target backend).

The multicore CPU code generator generates LLVM IR from the AST. In order to generate LLVM IR, we use Halide as a library: we first generate the Halide IR then we lower the Halide IR to LLVM IR using Halide. We do not use Halide to perform any high level code optimization. All the code optimizations are performed by TIRAMISU before generating the Halide IR. The Halide compiler then lowers the Halide IR loops into LLVM IR.

The GPU code generator generates LLVM IR for the host code and CUDA for the kernel code. Data copy commands and information about where to store buffers (shared, constant, or global memory) are all provided in Layer IV. TIRAMISU translates these into the equivalent CUDA data copy calls and buffer allocations in the generated code. Computation dimensions tagged with GPU thread or GPU block tags are translated into the appropriate GPU thread and block IDs in the lowered code. The TIRAMISU code generator can generate coalesced array accesses and can use shared and constant memories. It can also avoid thread divergence by separating full tiles (loop nests with a size that is multiple of the tile size) from partial tiles (the remaining part of a loop).

The code generator for distributed memory systems utilizes MPI. During code generation, all the function calls for data copying are translated to the equivalent MPI function calls. The generated code is postprocessed and each distributed loop is converted into a conditional based on the MPI rank of the executing process. For example:

```
for(q in 1..N-1) {...} // distribute on q
```

becomes:

```
q = get_rank(); if (q≥1 and q<N-1) {...}
```

**B. Support for Non-Affine Iteration Spaces**

TIRAMISU represents non-affine array accesses, non-affine loop bounds, and non-affine conditionals in a way similar to Benabderrahmane et al. [6]. For example, a conditional is transformed into a predicate and attached to the computation. The list of accesses of the computation is the union of the accesses of the computation in the two branches of the conditional; this is an over-approximation. During code generation, a preprocessing step inserts the conditional back into the generated code. The efficiency of these techniques was demonstrated by Benabderrahmane et al. [6] and was confirmed in the PENCIL compiler [4]. Our experiences in general, as well as the experiments in this paper, show that these approximations do not hamper performance.

---

### النسخة العربية

نظراً لأن المساهمة الرئيسية لهذه الورقة ليست في تقديم تقنيات جديدة لتوليد الشفرة، فإننا نقدم فقط نظرة عامة عالية المستوى لكيفية توليد TIRAMISU لطبقات التمثيل الوسيط والشفرة المستهدفة. في جميع أنحاء القسم، نوجه القارئ إلى الأدبيات المناسبة لمزيد من التفاصيل.

في بقية هذا القسم نصف كيف تحول أوامر الجدولة الطبقات I وII وIII وIV. نصف أيضاً كيفية توليد الشفرة المستهدفة من الطبقة IV.

**أ) تحويل الطبقة I إلى الطبقة II:** يتم تحويل الطبقة I إلى الطبقة II باستخدام نوعين من أوامر الجدولة: (1) أوامر تحويلات أعشاش الحلقات (مثل tile() وsplit() وshift() وinterchange())؛ و(2) أوامر تخطيط مستويات الحلقات على الأجهزة (بما في ذلك parallelize() وvectorize() وgpu()).

يطبق النوع الأول من أوامر الجدولة تخطيطاً يحول مجال التكرار. على سبيل المثال، عندما يتم تطبيق أمر تبليط على الحساب by في الشكل 2، يتم ترجمته إلى التخطيط التالي:

{by(i, j, c) → by(i0, j0, i1, j1, c) : i0 = floor(i/32) ∧ i1 = i%32 ∧ j0 = floor(j/32) ∧ j1 = j%32 ∧ 0 ≤ i < N ∧ 0 ≤ j < N}

ثم يتم تطبيق هذا التخطيط على تمثيل الطبقة I، مما ينتج تمثيل الطبقة II. يتم تركيب التحويلات من خلال تركيب تخطيطات مختلفة، حيث أن تركيب تخطيطين أفينيين هو تخطيط أفيني.

يضيف النوع الثاني من الأوامر علامات مكانية للأبعاد للإشارة إلى مستويات الحلقات المراد توازيها، أو توجيهها متجهياً، أو تخطيطها على كتل GPU، وهكذا.

**ب) تحويل الطبقة II إلى الطبقة III:** يتم ذلك من خلال إضافة علاقات الوصول إلى الطبقة II. بشكل افتراضي، يستخدم TIRAMISU علاقات وصول الهوية (أي، علاقات الوصول التي تخزن حساباً C(i,j) في مخزن مؤقت C[i,j]).

إذا تم استخدام أمر store_in()، يتم استنتاج علاقة الوصول من هذا الأمر بدلاً من ذلك. تُضاف أيضاً تخصيصات المخزن المؤقت أثناء تحويل الطبقة II إلى الطبقة III. ينشئ أمر الجدولة b.allocate_at(C, i) عبارة جديدة تخصص المخزن المؤقت b في نفس عش الحلقة للحساب C ولكن عند مستوى الحلقة i.

**ج) تحويل الطبقة III إلى الطبقة IV:** يتم ترجمة أوامر الجدولة لاتصال البيانات (الإرسال والاستقبال)، والمزامنة، ولنسخ البيانات بين الذاكرة العامة والمشتركة والمحلية جميعها إلى عبارات. على سبيل المثال، يتم ترجمة أوامر send() وreceive() إلى استدعاءات دوال سيتم ترجمتها إلى استدعاءات MPI أثناء توليد الشفرة.

**أ. توليد الشفرة**

يتلخص توليد الشفرة من مجموعة الحسابات في الطبقة IV في توليد حلقات متداخلة تزور كل حساب في المجموعة، مرة واحدة فقط، مع اتباع الترتيب المعجمي بين الحسابات [5]، [27]، [38]. يعتمد TIRAMISU على تطبيق لخوارزمية توليد شفرة Cloog [5] المقدمة من مكتبة ISL [47]. يأخذ مولد شفرة TIRAMISU تمثيل الطبقة IV الوسيط ويولد شجرة بناء جملة مجردة (AST). ثم يتم عبور AST لتوليد شفرة منخفضة المستوى لمعماريات أجهزة محددة (اعتماداً على الواجهة الخلفية المستهدفة).

يولد مولد شفرة CPU متعدد الأنوية LLVM IR من AST. من أجل توليد LLVM IR، نستخدم Halide كمكتبة: نولد أولاً Halide IR ثم نخفض Halide IR إلى LLVM IR باستخدام Halide. لا نستخدم Halide لتنفيذ أي تحسين شفرة عالي المستوى. يتم تنفيذ جميع تحسينات الشفرة بواسطة TIRAMISU قبل توليد Halide IR. يقوم مترجم Halide بعد ذلك بخفض حلقات Halide IR إلى LLVM IR.

يولد مولد شفرة GPU LLVM IR لشفرة المضيف وCUDA لشفرة النواة. يتم توفير أوامر نسخ البيانات ومعلومات حول مكان تخزين المخازن المؤقتة (الذاكرة المشتركة أو الثابتة أو العامة) جميعها في الطبقة IV. يترجم TIRAMISU هذه إلى استدعاءات نسخ بيانات CUDA المكافئة وتخصيصات المخزن المؤقت في الشفرة المولدة. يتم ترجمة أبعاد الحساب الموسومة بعلامات خيط GPU أو كتلة GPU إلى معرفات خيوط وكتل GPU المناسبة في الشفرة المخفضة. يمكن لمولد شفرة TIRAMISU توليد وصولات مصفوفات مدمجة ويمكنه استخدام الذاكرات المشتركة والثابتة. يمكنه أيضاً تجنب تباين الخيوط من خلال فصل البلاطات الكاملة (أعشاش الحلقات بحجم مضاعف لحجم البلاطة) عن البلاطات الجزئية (الجزء المتبقي من الحلقة).

يستخدم مولد الشفرة للأنظمة الموزعة للذاكرة MPI. أثناء توليد الشفرة، يتم ترجمة جميع استدعاءات الدوال لنسخ البيانات إلى استدعاءات دوال MPI المكافئة. تتم معالجة الشفرة المولدة لاحقاً ويتم تحويل كل حلقة موزعة إلى شرط بناءً على رتبة MPI للعملية التي تُنفذ. على سبيل المثال:

```
for(q in 1..N-1) {...} // distribute on q
```

يصبح:

```
q = get_rank(); if (q≥1 and q<N-1) {...}
```

**ب. الدعم لفضاءات التكرار غير الأفينية**

يمثل TIRAMISU وصولات المصفوفات غير الأفينية، وحدود الحلقات غير الأفينية، والشروط غير الأفينية بطريقة مماثلة لـ Benabderrahmane et al. [6]. على سبيل المثال، يتم تحويل الشرط إلى محمول وإرفاقه بالحساب. قائمة وصولات الحساب هي اتحاد وصولات الحساب في فرعي الشرط؛ هذا تقدير مبالغ فيه. أثناء توليد الشفرة، تدرج خطوة معالجة مسبقة الشرط مرة أخرى في الشفرة المولدة. تم إثبات كفاءة هذه التقنيات من قبل Benabderrahmane et al. [6] وتم تأكيدها في مترجم PENCIL [4]. تظهر تجاربنا بشكل عام، بالإضافة إلى التجارب في هذه الورقة، أن هذه التقديرات لا تعيق الأداء.

---

### Translation Notes

- **Figures referenced:** Figure 2
- **Key terms introduced:** Cloog algorithm, AST (abstract syntax tree), Halide library, MPI rank, thread divergence, full tiles, partial tiles, predicates, over-approximation
- **Equations:** Map notation, conditional examples
- **Citations:** [4], [5], [6], [27], [38], [47]
- **Special handling:** Code examples preserved, algorithm names kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
