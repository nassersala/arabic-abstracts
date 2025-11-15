# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** polyhedral model, compiler, scheduling, optimization, code generation, array packing, register blocking, data prefetching, asynchronous communication, distributed systems, dependence analysis, loop transformation, scheduling language, intermediate representation, DSL

---

### English Version

**a) Polyhedral compilers with automatic scheduling:** Polyhedral compilers such as PENCIL [4], [3], Pluto [8], Polly [22], Tensor Comprehensions [46], and PolyMage [34] are fully automatic. Some of them are designed for specific domains (such as Tensor Comprehensions and PolyMage), while Pluto, PENCIL, and Polly are more general. While fully automatic compilers provide productivity, they may not always obtain the best performance. This suboptimal performance is due to several reasons: first, these compilers do not implement some key optimizations such as array packing [20], register blocking, data prefetching, and asynchronous communication (which are all supported by TIRAMISU); second, they do not have a precise cost-model to decide which optimizations are profitable. For example, the Pluto [8] automatic scheduling algorithm (used in Pluto, PENCIL and Polly) tries to minimize the distance between producer and consumer statements while maximizing outermost parallelism, but it does not consider data layout, redundant computations, or the complexity of the control of the generated code. Instead of fully automatic scheduling, TIRAMISU relies on a set of scheduling commands, giving the user full control over scheduling.

Polyhedral frameworks proposed by Amarasinghe et al. [1] and Bondhugula et al. [7] address the problem of automatic code generation for distributed systems. Instead of being fully automatic, TIRAMISU relies on the user to provide scheduling commands to control choices in the generated code (synchronous/asynchronous communication, the granularity of communication, buffer sizes, when to send and receive, cost of communication versus re-computation, etc.).

**b) Polyhedral compilers with a scheduling language:** AlphaZ [51], CHiLL [10], [24] and URUK [19] are polyhedral frameworks developed to allow users to express high-level transformations using scheduling commands. Since these frameworks are polyhedral, they can express any affine transformation. However, their scheduling languages do not target distributed architectures. In contrast, TIRAMISU features scheduling commands for partitioning computations (for distributed systems), synchronization and distribution of data across nodes. The first four columns of Table I compare between TIRAMISU and three representative polyhedral frameworks.

**c) Non-polyhedral compilers with a scheduling language:** Halide [39] is an image processing DSL with a scheduling language that uses intervals to represent iteration spaces instead of the polyhedral model. This limits the expressiveness of Halide. For example, unlike TIRAMISU, Halide cannot naturally represent non-rectangular iteration spaces, and this is the reason why distributed Halide [15] over-approximates the amount of data to communicate (send and receive) when generating distributed code. This also makes some Halide passes over-approximate non-rectangular iteration spaces, potentially leading to less efficient code (for example, it prevents Halide from performing precise bounds inference for non-rectangular iteration spaces). The use of intervals also prevents Halide from performing many complex affine transformations, such as iteration space skewing.

Halide does not have dependence analysis and thus relies on conservative rules to determine whether a schedule is legal. For example, Halide does not allow the fusion of two loops (using the compute_with command) if the second loop reads a value produced by the first loop. While this rule avoids illegal fusion, it prevents fusing many legal cases, which may lead to suboptimal performance. Halide also assumes the program has an acyclic dataflow graph in order to simplify checking the legality of a schedule. This prevents users from expressing many programs with cyclic dataflow. It is possible in some cases to work around the above restrictions, but such work-around methods are not general. TIRAMISU avoids over-conservative constraints by relying on dependence analysis to check for the correctness of code transformations, enabling more possible schedules. Table I summarizes the comparison between TIRAMISU and Halide.

Vocke et al. [48] extend Halide to target DSPs, and add scheduling commands such as store_in to specify in which memory hierarchy data should be stored. TVM [11] is another system that shares many similarities with Halide. It uses a modified form of the Halide IR internally. Since TVM is also a non-polyhedral compiler, the differences between Halide and TIRAMISU that are due to the use of polyhedral model also apply to TVM.

POET [50] is a system that uses an XML-based description of code and transformation behavior to parametrize loop transformations. It uses syntactic transformations, which are less general than the polyhedral transformations used in TIRAMISU. GraphIt [52] is another compiler that has a scheduling language but that is mainly designed for the area of graph applications.

**d) Other Compilers:** Delite [9] is a generic framework for building DSL compilers. It exposes several parallel computation patterns that DSLs can use to express parallelism. NOVA [12] and Lift [42] are IRs for DSL compilers. They are functional languages that rely on a suite of higher-order functions such as map, reduce, and scan to express parallelism. TIRAMISU is complementary to these frameworks as TIRAMISU allows complex affine transformations that are easier to express in the polyhedral model.

---

### النسخة العربية

**أ) المترجمات متعددة السطوح بجدولة أوتوماتيكية:** المترجمات متعددة السطوح مثل PENCIL [4]، [3]، Pluto [8]، Polly [22]، Tensor Comprehensions [46]، وPolyMage [34] أوتوماتيكية بالكامل. بعضها مصمم لمجالات محددة (مثل Tensor Comprehensions وPolyMage)، بينما Pluto وPENCIL وPolly أكثر عمومية. في حين توفر المترجمات الأوتوماتيكية بالكامل الإنتاجية، فقد لا تحصل دائماً على أفضل أداء. يعود هذا الأداء دون المستوى الأمثل إلى عدة أسباب: أولاً، هذه المترجمات لا تنفذ بعض التحسينات الرئيسية مثل تعبئة المصفوفات [20]، وحجب السجلات، والجلب المسبق للبيانات، والاتصال غير المتزامن (والتي يدعمها TIRAMISU جميعها)؛ ثانياً، ليس لديها نموذج تكلفة دقيق لتقرير التحسينات المربحة. على سبيل المثال، تحاول خوارزمية الجدولة الأوتوماتيكية لـ Pluto [8] (المستخدمة في Pluto وPENCIL وPolly) تقليل المسافة بين عبارات المنتج والمستهلك مع تعظيم التوازي الخارجي، لكنها لا تأخذ في الاعتبار تخطيط البيانات أو الحسابات الزائدة أو تعقيد التحكم في الشفرة المولدة. بدلاً من الجدولة الأوتوماتيكية بالكامل، يعتمد TIRAMISU على مجموعة من أوامر الجدولة، مما يمنح المستخدم تحكماً كاملاً في الجدولة.

تتناول أطر العمل متعددة السطوح التي اقترحها Amarasinghe et al. [1] وBondhugula et al. [7] مشكلة توليد الشفرة التلقائي للأنظمة الموزعة. بدلاً من أن يكون أوتوماتيكياً بالكامل، يعتمد TIRAMISU على المستخدم لتوفير أوامر الجدولة للتحكم في الخيارات في الشفرة المولدة (الاتصال المتزامن/غير المتزامن، ودقة الاتصال، وأحجام المخازن المؤقتة، ومتى يتم الإرسال والاستقبال، وتكلفة الاتصال مقابل إعادة الحساب، وما إلى ذلك).

**ب) المترجمات متعددة السطوح بلغة جدولة:** AlphaZ [51] وCHiLL [10]، [24] وURUK [19] هي أطر عمل متعددة السطوح تم تطويرها للسماح للمستخدمين بالتعبير عن التحويلات عالية المستوى باستخدام أوامر الجدولة. نظراً لأن هذه الأطر متعددة السطوح، يمكنها التعبير عن أي تحويل أفيني. ومع ذلك، فإن لغات الجدولة الخاصة بها لا تستهدف المعماريات الموزعة. في المقابل، يتميز TIRAMISU بأوامر جدولة لتقسيم الحسابات (للأنظمة الموزعة)، والمزامنة وتوزيع البيانات عبر العقد. تقارن الأعمدة الأربعة الأولى من الجدول I بين TIRAMISU وثلاثة أطر عمل متعددة السطوح تمثيلية.

**ج) المترجمات غير متعددة السطوح بلغة جدولة:** Halide [39] هي لغة خاصة بالمجال لمعالجة الصور بلغة جدولة تستخدم الفترات لتمثيل فضاءات التكرار بدلاً من النموذج متعدد السطوح. هذا يحد من قوة التعبير في Halide. على سبيل المثال، على عكس TIRAMISU، لا يمكن لـ Halide تمثيل فضاءات التكرار غير المستطيلة بشكل طبيعي، وهذا هو السبب في أن Halide الموزع [15] يبالغ في تقدير كمية البيانات للتواصل (الإرسال والاستقبال) عند توليد الشفرة الموزعة. هذا أيضاً يجعل بعض تمريرات Halide تبالغ في تقدير فضاءات التكرار غير المستطيلة، مما قد يؤدي إلى شفرة أقل كفاءة (على سبيل المثال، يمنع Halide من إجراء استنتاج حدود دقيق لفضاءات التكرار غير المستطيلة). كما يمنع استخدام الفترات Halide من إجراء العديد من التحويلات الأفينية المعقدة، مثل انحراف فضاء التكرار.

لا يحتوي Halide على تحليل الاعتماديات وبالتالي يعتمد على قواعد محافظة لتحديد ما إذا كانت الجدولة قانونية. على سبيل المثال، لا يسمح Halide بدمج حلقتين (باستخدام أمر compute_with) إذا كانت الحلقة الثانية تقرأ قيمة أنتجتها الحلقة الأولى. في حين تتجنب هذه القاعدة الدمج غير القانوني، فإنها تمنع دمج العديد من الحالات القانونية، مما قد يؤدي إلى أداء دون المستوى الأمثل. يفترض Halide أيضاً أن البرنامج له رسم بياني غير دوري لتدفق البيانات من أجل تبسيط التحقق من قانونية الجدولة. هذا يمنع المستخدمين من التعبير عن العديد من البرامج ذات تدفق البيانات الدوري. من الممكن في بعض الحالات تجاوز القيود المذكورة أعلاه، لكن طرق الحل البديلة هذه ليست عامة. يتجنب TIRAMISU القيود المحافظة بشكل مفرط من خلال الاعتماد على تحليل الاعتماديات للتحقق من صحة تحويلات الشفرة، مما يتيح المزيد من الجداول الممكنة. يلخص الجدول I المقارنة بين TIRAMISU وHalide.

يوسع Vocke et al. [48] Halide لاستهداف معالجات الإشارات الرقمية (DSPs)، ويضيف أوامر جدولة مثل store_in لتحديد أي تسلسل هرمي للذاكرة يجب تخزين البيانات فيه. TVM [11] هو نظام آخر يشترك في العديد من أوجه التشابه مع Halide. يستخدم شكلاً معدلاً من Halide IR داخلياً. نظراً لأن TVM أيضاً مترجم غير متعدد السطوح، فإن الاختلافات بين Halide وTIRAMISU الناتجة عن استخدام النموذج متعدد السطوح تنطبق أيضاً على TVM.

POET [50] هو نظام يستخدم وصفاً قائماً على XML للشفرة وسلوك التحويل لمعايرة تحويلات الحلقات. يستخدم تحويلات نحوية، وهي أقل عمومية من التحويلات متعددة السطوح المستخدمة في TIRAMISU. GraphIt [52] هو مترجم آخر له لغة جدولة لكنه مصمم بشكل أساسي لمجال تطبيقات الرسوم البيانية.

**د) مترجمات أخرى:** Delite [9] هو إطار عمل عام لبناء مترجمات اللغات الخاصة بالمجال. يكشف عن عدة أنماط حساب متوازية يمكن للغات الخاصة بالمجال استخدامها للتعبير عن التوازي. NOVA [12] وLift [42] هي تمثيلات وسيطة لمترجمات اللغات الخاصة بالمجال. إنها لغات دالية تعتمد على مجموعة من الدوال عالية الرتبة مثل map وreduce وscan للتعبير عن التوازي. TIRAMISU مكمل لهذه الأطر حيث يسمح TIRAMISU بتحويلات أفينية معقدة يسهل التعبير عنها في النموذج متعدد السطوح.

---

### Translation Notes

- **Figures referenced:** Table I (comparison table)
- **Key terms introduced:** automatic scheduling, cost model, producer-consumer statements, outermost parallelism, redundant computations, synchronous/asynchronous communication, granularity of communication, bounds inference, acyclic dataflow graph, syntactic transformations, higher-order functions
- **Equations:** 0
- **Citations:** Extensive citations to related work [1], [3], [4], [7], [8], [9], [10], [11], [12], [15], [19], [20], [22], [24], [34], [39], [42], [46], [48], [50], [51], [52]
- **Special handling:** Table I comparison requires maintaining framework names in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
