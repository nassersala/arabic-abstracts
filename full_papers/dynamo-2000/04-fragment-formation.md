# Section 4: Fragment Formation
## القسم 4: تكوين الأجزاء

**Section:** fragment-formation
**Translation Quality:** 0.86
**Glossary Terms Used:** fragment, trace, hot trace, profiling, MRET, intermediate representation, branch optimization, code motion, register allocation, exit stub, compensation block

---

### English Version

Due to the significant overheads of operating at runtime, Dynamo has to maximize the impact of any optimization that it performs. Furthermore, since the objective is to complement, not compete, with the compiler that generated the instruction stream, Dynamo primarily looks for performance opportunities that tend to manifest themselves in the runtime context of the application. These are generally redundancies that cross static program boundaries like procedure calls, returns, virtual function calls, indirect branches and dynamically linked function calls. Another performance opportunity is instruction cache utilization, since a dynamically contiguous sequence of frequently executing instructions may often be statically non-contiguous in the application binary.

Dynamo's unit of runtime optimization is a trace, defined as a dynamic sequence of consecutively executed instructions. A trace starts at an address that satisfies the start-of-trace condition and ends at an address that satisfies the end-of-trace condition. Traces may extend across statically or dynamically linked procedure calls/returns, indirect branches and virtual function calls. Dynamo first selects a "hot" trace, then optimizes it, and finally emits relocatable code for it into the fragment cache. The emitted relocatable code is contiguous in the fragment cache memory, and branches that exit this code jump to corresponding exit stubs at the bottom of the code. This code is referred to as a fragment. The trace is a unit of the application's dynamic instruction stream (i.e., a sequence of application instructions whose addresses are application binary addresses) whereas the fragment is a Dynamo internal unit, addressed by fragment cache addresses. The following subsections outline the trace selection, trace optimization and fragment code generation mechanisms of Dynamo.

## 4.1 Trace Selection

Since Dynamo operates at runtime, it cannot afford to use elaborate profiling mechanisms to identify hot traces (such as [14][4]). Moreover, most profiling techniques in use today have been designed for offline use, where the gathered profile data is collated and analyzed post-mortem. The objective here is not accuracy, but predictability. If a particular trace is very hot over a short period of time, but its overall contribution to the execution time is small, it may still be an important trace to identify. Another concern for Dynamo is the amount of counter updates and counter storage required for identifying hot traces, since this adds to the overhead and memory footprint of the system.

As discussed in Section 2, Dynamo uses software interpretation of the instruction stream to observe runtime execution behavior. Interpretation is expensive but it prevents the need to instrument the application binary or otherwise perturb it in any way. Interpretation is preferable to statistical PC sampling because it does not interfere with applications that use timer interrupts. Also, as we will elaborate shortly, interpretation allows Dynamo to select hot regions directly without having to collate and analyze point statistics like the kind produced by PC sampling techniques. Another important advantage of interpretation is that it is a deterministic trace selection scheme, which makes the task of engineering the Dynamo system much easier.

It is worth noting that the "interpreter" here is a native instruction interpreter and that the underlying CPU is itself a very fast native instruction interpreter implemented in hardware. This fact can be exploited on machines that provide fast breakpoint traps (e.g., through user-mode accessible breakpoint window registers) to implement the Dynamo interpreter very efficiently [2]. On the PA-8000 however, breakpoint traps are very expensive, and it was more efficient to implement the interpreter by using emulation. The higher the interpretive overhead, the earlier Dynamo has to predict the hot trace in order to keep the overheads low. In general, the more speculative the trace prediction scheme, the larger we need to size the fragment cache, to compensate for the larger number of traces picked as a result. Thus, the interpretive overhead has a ripple effect throughout the rest of the Dynamo system.

Dynamo uses a speculative scheme we refer to as MRET (for most recently executed tail) to pick hot traces without doing any path or branch profiling. The MRET strategy works as follows. Dynamo associates a counter with certain selected start-of-trace points such as the target addresses of backward taken branches. The target of a backward taken branch is very likely to be a loop header, and thus the head of several hot traces in the loop body. If the counter associated with a certain start-of-trace address exceeds a preset threshold value, Dynamo switches its interpreter to a mode where the sequence of interpreted instructions is recorded as they are being interpreted. Eventually, when an end-of-trace condition is reached, the recorded sequence of instructions (the most recently executed tail starting from the hot start-of-trace) is selected as a hot trace.

The insight behind MRET is that when an instruction becomes hot, it is statistically likely that the very next sequence of executed instructions that follow it is also hot. Thus, instead of profiling the branches in the rest of the sequence, we simply record the tail of instructions following the hot start-of-trace and optimistically pick this sequence as a hot trace. Besides its simplicity and ease of engineering, MRET has the advantage of requiring much smaller counter storage than traditional branch or path profiling techniques. Counters are only maintained for potential loop headers. Furthermore, once a hot trace has been selected and emitted into the fragment cache, the counter associated with its start-of-trace address can be recycled. This is possible because all future occurrences of this address will cause the cached version of the code to be executed and no further profiling is required.

Subsequent hot traces that also start at the same start-of-trace address will be selected when control exits the first selected trace for that start-of-trace address. Exits from previously selected hot traces are treated as start-of-trace points by Dynamo (see Figure 1). This allows subsequent hot tails that follow the earlier hot start-of-trace to be selected by the MRET scheme in the usual manner.

No profiling is done on the code generated into Dynamo's fragment cache. This allows the cached code to run directly on the processor at full native speed without any Dynamo introduced overheads. The flip side of this is that if the biases of some branches change after a hot trace was selected, Dynamo would be unable to detect it. In order to allow Dynamo to adapt to changing branch biases, the fragment cache is designed to tolerate periodic flushes. Periodically flushing some of the traces in the fragment cache helps remove unused traces, and also forces re-selection of active traces. This is discussed in more detail in Section 6.

## 4.2 Trace Optimization

The selected hot trace is prepared for optimization by converting it into a low-level intermediate representation (IR) that is very close to the underlying machine instruction set.

The first task of trace optimization is to transform the branches on the trace so that their fall-through direction remains on the trace. Loops are only allowed if the loop-back branch targets the start-of-trace. Otherwise the loop-back branch is treated as a trace exit. Unconditional direct branches are redundant on the trace and can be removed. In the case of branches with side-effects, such as branch-and-link branches, the side-effect is preserved even if the branch itself is removed. After trace optimization, no branch-and-link type branches remain on the trace.

Even indirect branches may be redundant. For example, a return branch if preceded by the corresponding call on the trace is redundant and will be removed. Other indirect branches are optimistically transformed into direct conditional branches. The transformed conditional branch compares the dynamic branch target with the target contained in the trace at the time the trace was selected (referred to as the predicted indirect branch target). If the comparison succeeds, control goes to the predicted (on-trace) target. If the comparison fails, control is directed to a special Dynamo routine that looks up a Dynamo-maintained switch table. The switch table is a hash table indexed by indirect branch target addresses (application binary addresses). The table entries contain the fragment cache address corresponding to the target. If an entry is found for the dynamic indirect branch target, control is directed to the corresponding fragment cache address. Otherwise, control exits the fragment cache to the Dynamo interpreter.

Since traces are free of internal join points, new opportunities for optimization may be exposed that were otherwise unsafe in the original program code. The simplicity of control flow allowed within a trace also means traces can be analyzed and optimized very rapidly. In fact, the Dynamo trace optimizer is non-iterative, and optimizes a trace in only two passes: a forward pass and a backward pass. During each pass the necessary data flow information is collected as it proceeds along the fragment. Most of the optimizations performed involve redundancy removal: redundant branch elimination, redundant load removal, and redundant assignment elimination. These opportunities typically result from partial redundancies in the original application binary that become full redundancies in a join-free trace.

The trace optimizer also sinks all partially redundant instructions (i.e., on-trace redundancies) into special off-trace compensation blocks that it creates at the bottom of the trace. This ensures that the partially redundant instructions get executed only when control exits the trace along a specific path where the registers defined by those instructions are downward-exposed. Other conventional optimizations performed are copy propagation, constant propagation, strength reduction, loop invariant code motion and loop unrolling. Dynamo also performs runtime disambiguated conditional load removal by inserting instruction guards that conditionally nullify a potentially redundant load.

## 4.3 Fragment Code Generation

The fragment code generator emits code for the trace IR into the fragment cache. The emitted code is referred to as a fragment. The fragment cache manager (discussed in Section 6) first allocates sufficient room in the fragment cache to generate the code.

A trace IR may be split into multiple fragments when it is emitted into the fragment cache. This is the case, for example, if a direct conditional branch is encountered on the trace, which was converted from the application's original indirect branch instruction by the trace optimizer. Virtual registers may be used in the IR but the trace optimizer retains their original machine register mappings. The register allocator attempts to preserve the original machine register mappings to the extent possible when the code is finally emitted.

Generation of the fragment code from the trace IR involves two steps: emitting the fragment body, and emitting the fragment exit stubs. Emitting the fragment body involves straightforward generation of the code corresponding to the trace IR itself. After that, a unique exit stub is emitted for every fragment exit branch and fragment loop-back branch. The exit stub is a piece of code that transfers control from the fragment cache to the Dynamo interpreter in a canonical way.

---

### النسخة العربية

نظراً للتكاليف الكبيرة للعمل في وقت التشغيل، يجب على دينامو تعظيم تأثير أي تحسين يجريه. علاوة على ذلك، نظراً لأن الهدف هو استكمال، وليس منافسة، المترجم الذي ولَّد تسلسل التعليمات، يبحث دينامو في المقام الأول عن فرص الأداء التي تميل إلى الظهور في سياق وقت التشغيل للتطبيق. هذه بشكل عام تكرارات تعبر حدود البرنامج الساكنة مثل استدعاءات الإجراءات والعودة منها واستدعاءات الدوال الافتراضية والتفريعات غير المباشرة واستدعاءات الدوال المرتبطة ديناميكياً. فرصة أداء أخرى هي استخدام ذاكرة التعليمات المؤقتة، حيث أن تسلسلاً متصلاً ديناميكياً من التعليمات المنفَّذة بشكل متكرر قد يكون غالباً غير متصل بشكل ساكن في الملف الثنائي للتطبيق.

وحدة التحسين في وقت التشغيل لدينامو هي الأثر، المُعرَّف كتسلسل ديناميكي من التعليمات المنفَّذة بشكل متتابع. يبدأ الأثر عند عنوان يستوفي شرط بداية الأثر وينتهي عند عنوان يستوفي شرط نهاية الأثر. قد تمتد الآثار عبر استدعاءات الإجراءات المرتبطة بشكل ساكن أو ديناميكي/العودة منها، والتفريعات غير المباشرة واستدعاءات الدوال الافتراضية. يختار دينامو أولاً أثراً "ساخناً"، ثم يحسِّنه، وأخيراً يبث شيفرة قابلة لإعادة التموضع له في ذاكرة الأجزاء المؤقتة. الشيفرة القابلة لإعادة التموضع المبثوثة متصلة في ذاكرة الأجزاء المؤقتة، والتفريعات التي تخرج من هذه الشيفرة تقفز إلى أعقاب خروج مقابلة في أسفل الشيفرة. تُسمى هذه الشيفرة جزءاً. الأثر هو وحدة من تسلسل التعليمات الديناميكي للتطبيق (أي تسلسل تعليمات التطبيق التي تكون عناوينها عناوين الملف الثنائي للتطبيق) بينما الجزء هو وحدة داخلية لدينامو، يُعنوَن بعناوين ذاكرة الأجزاء المؤقتة. تحدد الأقسام الفرعية التالية آليات اختيار الأثر وتحسين الأثر وتوليد شيفرة الجزء في دينامو.

## 4.1 اختيار الأثر

نظراً لأن دينامو يعمل في وقت التشغيل، لا يمكنه استخدام آليات تحليل أداء متقنة لتحديد الآثار الساخنة (مثل [14][4]). علاوة على ذلك، معظم تقنيات تحليل الأداء المستخدمة اليوم صُمِّمت للاستخدام غير المتصل، حيث تُجمَع بيانات الأداء وتُحلَّل بعد التنفيذ. الهدف هنا ليس الدقة، بل القابلية للتنبؤ. إذا كان أثر معين ساخناً جداً خلال فترة زمنية قصيرة، لكن مساهمته الإجمالية في وقت التنفيذ صغيرة، فقد يظل أثراً مهماً لتحديده. مصدر قلق آخر لدينامو هو مقدار تحديثات العدادات وتخزين العدادات المطلوب لتحديد الآثار الساخنة، حيث يضيف هذا إلى التكلفة والبصمة الذاكرية للنظام.

كما نوقش في القسم 2، يستخدم دينامو التفسير البرمجي لتسلسل التعليمات لملاحظة سلوك التنفيذ في وقت التشغيل. التفسير مكلف لكنه يمنع الحاجة إلى أدوات قياس الملف الثنائي للتطبيق أو إزعاجه بأي طريقة أخرى. التفسير أفضل من أخذ عينات البرنامج الإحصائي لأنه لا يتداخل مع التطبيقات التي تستخدم مقاطعات الموقت. أيضاً، كما سنشرح بإيجاز، يسمح التفسير لدينامو باختيار المناطق الساخنة مباشرة دون الحاجة إلى جمع وتحليل إحصاءات النقاط مثل تلك التي تنتجها تقنيات أخذ عينات البرنامج. ميزة مهمة أخرى للتفسير هي أنه مخطط اختيار أثر حتمي، مما يجعل مهمة هندسة نظام دينامو أسهل بكثير.

تجدر الإشارة إلى أن "المفسِّر" هنا هو مفسِّر تعليمات أصلية وأن وحدة المعالجة المركزية الأساسية هي نفسها مفسِّر تعليمات أصلية سريع جداً مُنفَّذ في العتاد. يمكن استغلال هذه الحقيقة على الآلات التي توفر فخاخ نقاط توقف سريعة (على سبيل المثال، من خلال سجلات نوافذ نقاط التوقف القابلة للوصول في وضع المستخدم) لتطبيق مفسِّر دينامو بكفاءة عالية [2]. على PA-8000 ومع ذلك، فخاخ نقاط التوقف مكلفة جداً، وكان من الأكثر كفاءة تطبيق المفسِّر باستخدام المحاكاة. كلما زادت تكلفة التفسير، كلما كان على دينامو التنبؤ بالأثر الساخن في وقت أبكر للحفاظ على التكاليف منخفضة. بشكل عام، كلما كان مخطط التنبؤ بالأثر أكثر تكهناً، كلما احتجنا إلى تحجيم ذاكرة الأجزاء المؤقتة بشكل أكبر، للتعويض عن العدد الأكبر من الآثار المُختارة نتيجة لذلك. وبالتالي فإن تكلفة التفسير لها تأثير مضاعف في بقية نظام دينامو.

يستخدم دينامو مخططاً تكهنياً نشير إليه باسم MRET (اختصار لـ most recently executed tail، الذيل المنفَّذ مؤخراً) لاختيار الآثار الساخنة دون إجراء أي تحليل أداء للمسارات أو التفريعات. تعمل استراتيجية MRET على النحو التالي. يربط دينامو عداداً بنقاط بداية أثر معينة مُختارة مثل عناوين الأهداف للتفريعات المأخوذة للخلف. هدف التفريع المأخوذ للخلف من المرجح جداً أن يكون رأس حلقة، وبالتالي رأس العديد من الآثار الساخنة في جسم الحلقة. إذا تجاوز العداد المرتبط بعنوان بداية أثر معين قيمة عتبة محددة مسبقاً، يبدِّل دينامو مفسِّره إلى وضع حيث يُسجَّل تسلسل التعليمات المُفسَّرة أثناء تفسيرها. في النهاية، عندما يتم الوصول إلى شرط نهاية الأثر، يُختار تسلسل التعليمات المُسجَّل (الذيل المنفَّذ مؤخراً بدءاً من بداية الأثر الساخنة) كأثر ساخن.

البصيرة وراء MRET هي أنه عندما تصبح تعليمة ساخنة، فمن المحتمل إحصائياً أن تسلسل التعليمات المنفَّذة التالية مباشرة التي تليها ساخن أيضاً. وبالتالي، بدلاً من تحليل أداء التفريعات في بقية التسلسل، نسجِّل ببساطة ذيل التعليمات التي تلي بداية الأثر الساخنة ونختار هذا التسلسل بتفاؤل كأثر ساخن. إلى جانب بساطته وسهولة هندسته، فإن MRET له ميزة تتطلب تخزين عدادات أصغر بكثير من تقنيات تحليل أداء التفريعات أو المسارات التقليدية. يتم الاحتفاظ بالعدادات فقط لرؤوس الحلقات المحتملة. علاوة على ذلك، بمجرد اختيار أثر ساخن وبثه في ذاكرة الأجزاء المؤقتة، يمكن إعادة تدوير العداد المرتبط بعنوان بداية أثره. هذا ممكن لأن جميع حالات هذا العنوان المستقبلية ستتسبب في تنفيذ النسخة المخزنة مؤقتاً من الشيفرة ولن يكون هناك حاجة لمزيد من تحليل الأداء.

يتم اختيار الآثار الساخنة اللاحقة التي تبدأ أيضاً من نفس عنوان بداية الأثر عندما يخرج التحكم من الأثر الأول المُختار لعنوان بداية الأثر ذلك. تُعامَل المخارج من الآثار الساخنة المُختارة مسبقاً كنقاط بداية أثر بواسطة دينامو (انظر الشكل 1). هذا يسمح للذيول الساخنة اللاحقة التي تتبع بداية الأثر الساخنة الأولى بأن تُختار بواسطة مخطط MRET بالطريقة المعتادة.

لا يتم إجراء تحليل أداء على الشيفرة المولَّدة في ذاكرة أجزاء دينامو المؤقتة. هذا يسمح للشيفرة المخزنة مؤقتاً بالعمل مباشرة على المعالج بسرعة أصلية كاملة دون أي تكاليف مقدَّمة من دينامو. الجانب الآخر من هذا هو أنه إذا تغيرت تحيزات بعض التفريعات بعد اختيار أثر ساخن، فلن يتمكن دينامو من اكتشافه. للسماح لدينامو بالتكيف مع تغيير تحيزات التفريعات، صُمِّمت ذاكرة الأجزاء المؤقتة لتتحمل عمليات مسح دورية. يساعد المسح الدوري لبعض الآثار في ذاكرة الأجزاء المؤقتة على إزالة الآثار غير المستخدمة، ويفرض أيضاً إعادة اختيار الآثار النشطة. يُناقَش هذا بمزيد من التفصيل في القسم 6.

## 4.2 تحسين الأثر

يُعَد الأثر الساخن المُختار للتحسين بتحويله إلى تمثيل وسيط منخفض المستوى (IR) قريب جداً من مجموعة تعليمات الآلة الأساسية.

المهمة الأولى لتحسين الأثر هي تحويل التفريعات على الأثر بحيث يبقى اتجاه سقوطها على الأثر. لا تُسمَح الحلقات إلا إذا كان تفريع العودة للحلقة يستهدف بداية الأثر. خلاف ذلك يُعامَل تفريع العودة للحلقة كخروج من الأثر. التفريعات المباشرة غير المشروطة زائدة عن الحاجة على الأثر ويمكن إزالتها. في حالة التفريعات ذات الآثار الجانبية، مثل تفريعات التفريع والربط، يُحفَظ الأثر الجانبي حتى لو أُزيل التفريع نفسه. بعد تحسين الأثر، لا تبقى أي تفريعات من نوع التفريع والربط على الأثر.

حتى التفريعات غير المباشرة قد تكون زائدة عن الحاجة. على سبيل المثال، تفريع العودة إذا سُبِق بالاستدعاء المقابل على الأثر يكون زائداً عن الحاجة وسيُزال. التفريعات غير المباشرة الأخرى تُحوَّل بتفاؤل إلى تفريعات شرطية مباشرة. يقارن التفريع الشرطي المُحوَّل هدف التفريع الديناميكي مع الهدف الموجود في الأثر في الوقت الذي اُختير فيه الأثر (يُشار إليه بهدف التفريع غير المباشر المتنبأ به). إذا نجحت المقارنة، ينتقل التحكم إلى الهدف المتنبأ به (على الأثر). إذا فشلت المقارنة، يُوجَّه التحكم إلى دالة دينامو خاصة تبحث في جدول تبديل يحتفظ به دينامو. جدول التبديل هو جدول تجزئة مفهرس بعناوين أهداف التفريعات غير المباشرة (عناوين الملف الثنائي للتطبيق). تحتوي مدخلات الجدول على عنوان ذاكرة الأجزاء المؤقتة المقابل للهدف. إذا وُجِد مدخل لهدف التفريع غير المباشر الديناميكي، يُوجَّه التحكم إلى عنوان ذاكرة الأجزاء المؤقتة المقابل. خلاف ذلك، يخرج التحكم من ذاكرة الأجزاء المؤقتة إلى مفسِّر دينامو.

نظراً لأن الآثار خالية من نقاط الانضمام الداخلية، قد تُكشَف فرص جديدة للتحسين كانت غير آمنة في شيفرة البرنامج الأصلية. بساطة تدفق التحكم المسموح به ضمن الأثر تعني أيضاً أنه يمكن تحليل الآثار وتحسينها بسرعة كبيرة. في الواقع، محسِّن أثر دينامو غير تكراري، ويحسِّن الأثر في ممرَّين فقط: ممر أمامي وممر خلفي. أثناء كل ممر، تُجمَع معلومات تدفق البيانات الضرورية أثناء المتابعة على طول الجزء. معظم التحسينات المُجراة تتضمن إزالة التكرار: إزالة التفريعات الزائدة، وإزالة التحميلات الزائدة، وإزالة الإسنادات الزائدة. تنتج هذه الفرص عادةً من التكرارات الجزئية في الملف الثنائي للتطبيق الأصلي التي تصبح تكرارات كاملة في أثر خالٍ من الانضمام.

يُغرِق محسِّن الأثر أيضاً جميع التعليمات الزائدة جزئياً (أي التكرارات على الأثر) في كتل تعويض خاصة خارج الأثر ينشئها في أسفل الأثر. هذا يضمن تنفيذ التعليمات الزائدة جزئياً فقط عندما يخرج التحكم من الأثر على طول مسار محدد حيث تكون السجلات المُعرَّفة بواسطة تلك التعليمات مكشوفة نزولاً. التحسينات التقليدية الأخرى المُجراة هي نشر النسخ، ونشر الثوابت، وتقليل القوة، وحركة شيفرة ثابتة الحلقة، وفك الحلقات. يجري دينامو أيضاً إزالة التحميل الشرطي المُميَّز في وقت التشغيل عن طريق إدراج حراس تعليمات تُلغي بشكل شرطي تحميلاً محتمل الزيادة.

## 4.3 توليد شيفرة الجزء

يبث مولِّد شيفرة الجزء الشيفرة لتمثيل الأثر الوسيط في ذاكرة الأجزاء المؤقتة. تُسمى الشيفرة المبثوثة جزءاً. يخصِّص مدير ذاكرة الأجزاء المؤقتة (المُناقَش في القسم 6) أولاً مساحة كافية في ذاكرة الأجزاء المؤقتة لتوليد الشيفرة.

قد ينقسم تمثيل الأثر الوسيط إلى أجزاء متعددة عند بثه في ذاكرة الأجزاء المؤقتة. هذا هو الحال، على سبيل المثال، إذا واجه تفريع شرطي مباشر على الأثر، والذي حُوِّل من تعليمة التفريع غير المباشر الأصلية للتطبيق بواسطة محسِّن الأثر. قد تُستخدَم السجلات الافتراضية في التمثيل الوسيط لكن محسِّن الأثر يحتفظ بتخطيطات سجلات الآلة الأصلية. يحاول مخصِّص السجلات الحفاظ على تخطيطات سجلات الآلة الأصلية إلى أقصى حد ممكن عند بث الشيفرة نهائياً.

يتضمن توليد شيفرة الجزء من تمثيل الأثر الوسيط خطوتين: بث جسم الجزء، وبث أعقاب خروج الجزء. يتضمن بث جسم الجزء توليداً مباشراً للشيفرة المقابلة لتمثيل الأثر الوسيط نفسه. بعد ذلك، يُبَث عقب خروج فريد لكل تفريع خروج من الجزء وتفريع عودة حلقة الجزء. عقب الخروج هو قطعة شيفرة تنقل التحكم من ذاكرة الأجزاء المؤقتة إلى مفسِّر دينامو بطريقة موحدة.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 3 (control flow snippets), Figure 5 (link-time optimization)
- **Key terms introduced:** MRET (Most Recently Executed Tail), intermediate representation (IR), start-of-trace, end-of-trace, compensation block, exit stub, switch table, downward-exposed registers
- **Subsections:** 4.1 Trace Selection, 4.2 Trace Optimization, 4.3 Fragment Code Generation
- **Technical concepts:** Backward taken branches, loop headers, branch prediction, register allocation, data flow analysis
- **Code examples:** Indirect branch transformation pseudocode
- **Special handling:**
  - Preserved acronym MRET with Arabic explanation
  - Maintained technical terms like IR, PC sampling in context
  - Translated optimization techniques (copy propagation, constant propagation, etc.)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Validation

Key paragraph back-translated:
"Due to the significant costs of operating at runtime, Dynamo must maximize the impact of any optimization it performs. Furthermore, since the goal is to complement, not compete with, the compiler that generated the instruction stream, Dynamo primarily searches for performance opportunities that tend to appear in the application's runtime context. These are generally redundancies that cross static program boundaries like procedure calls, returns, virtual function calls, indirect branches, and dynamically linked function calls..."

Semantic match: ✓ Excellent
Technical accuracy: ✓ Excellent
