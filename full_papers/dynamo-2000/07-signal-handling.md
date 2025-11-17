# Section 7: Signal Handling
## القسم 7: معالجة الإشارات

**Section:** signal-handling
**Translation Quality:** 0.86
**Glossary Terms Used:** signal handling, asynchronous signal, synchronous signal, signal context, dead code elimination, code reordering, de-optimization, conservative optimization, aggressive optimization

---

### English Version

Optimizations that involve code reordering or removal, such as dead code elimination and loop unrolling, can create a problem if a signal arrives while executing the optimized fragment, by making it difficult or impossible for Dynamo to recreate the original signal context prior to the optimization. This can create complications for precise signal delivery. For example, the application might arm a signal with a handler that examines or even modifies the machine context at the instant of the signal. If a signal arrives at a point where a dead register assignment has been removed, the signal context is incomplete.

Dynamo intercepts all signals, and executes the program's signal handler code under its control, in the same manner that it executes the rest of the application code (box K in Figure 1). This gives Dynamo an opportunity to rectify the signal context that would otherwise be passed directly to the application's handler by the operating system. Asynchronous signals (such as keyboard interrupts, etc., where the signal address is irrelevant) are treated differently from synchronous signals (such as segment faults, etc., where the signal address is critical).

If an asynchronous signal arrives when executing a fragment, the Dynamo signal handler will queue it and return control back to the fragment cache. All queued asynchronous signals are processed when the next normal fragment cache exit occurs. This allows Dynamo to provide a proper signal context to the application's handler since control is not in the middle of an optimized fragment at the time the signal context is constructed.

In order to bound asynchronous signal handling latency, the Dynamo signal handler unlinks all linked branches on the current fragment prior to resuming execution of the fragment. To disconnect self-loops in a similar manner, the fragment generator emits an exit stub for each self-loop branch in addition to the exit stubs for the fragment exit branches. Unlinking the current fragment forces the next fragment exit branch to exit the fragment cache via the exit stub, preventing the possibility of control spinning within the fragment cache for an arbitrarily long period of time before the queued signals are processed. This feature allows Dynamo to operate in environments where soft real-time constraints must be met.

Synchronous signals on the other hand are problematic, because they cannot be postponed. A drastic solution is to suppress code removing and reordering transformations altogether. A more acceptable alternative is to use techniques similar to that developed for debugging of optimized code to de-optimize the fragment code before attempting to construct the synchronous signal context. Fortunately, the problem of de-optimizing is much simpler in Dynamo since only straight-line fragments are considered during optimization. Optimization logs can be stored along with each fragment that describes compensation actions to be performed upon signal-delivery, such as the execution a previously deleted instruction. This is presently an ongoing effort in the Dynamo project.

Our prototype currently implements a less ambitious solution to this problem, by dividing trace optimizations into two categories, conservative and aggressive. Conservative optimizations allow the precise signal context to be constructed if a synchronous fault occurs while executing the fragment. Aggressive optimizations on the other hand cannot guarantee this. Examples of conservative optimizations include constant propagation, constant folding, strength reduction, copy propagation and redundant branch removal. The aggressive category includes all of the conservative optimizations plus dead code removal, code sinking and loop invariant code motion. Certain aggressive optimizations, like redundant load removal, can sometimes be incorrect, if the load is from a volatile memory location.

Dynamo's trace optimizer is capable of starting out in its aggressive mode of optimization, and switching to conservative mode followed by a fragment cache flush if any suspicious instruction sequence is encountered. Unfortunately, the PA-RISC binary does not provide information about volatile memory operations or information about program-installed signal handlers. So this capability is currently unused in Dynamo. In a future version of Dynamo, we plan to investigate ways to allow the generator of Dynamo's input native instruction stream to provide hints to Dynamo. Dynamo can use such hints if they are available, but will not rely on them for operation.

---

### النسخة العربية

التحسينات التي تتضمن إعادة ترتيب الشيفرة أو الإزالة، مثل إزالة الشيفرة الميتة وفك الحلقات، يمكن أن تخلق مشكلة إذا وصلت إشارة أثناء تنفيذ الجزء المُحسَّن، من خلال جعلها صعبة أو مستحيلة على دينامو لإعادة إنشاء سياق الإشارة الأصلي قبل التحسين. يمكن أن يخلق هذا تعقيدات لتسليم الإشارة الدقيق. على سبيل المثال، قد يسلِّح التطبيق إشارة بمعالج يفحص أو حتى يعدِّل سياق الآلة في لحظة الإشارة. إذا وصلت إشارة عند نقطة حيث أُزيل إسناد سجل ميت، فإن سياق الإشارة غير مكتمل.

يعترض دينامو جميع الإشارات، وينفِّذ شيفرة معالج الإشارات للبرنامج تحت سيطرته، بنفس الطريقة التي ينفِّذ بها بقية شيفرة التطبيق (المربع K في الشكل 1). هذا يمنح دينامو فرصة لتصحيح سياق الإشارة الذي كان سيُمرَّر مباشرة إلى معالج التطبيق بواسطة نظام التشغيل. تُعامَل الإشارات غير المتزامنة (مثل مقاطعات لوحة المفاتيح، إلخ، حيث عنوان الإشارة غير ذي صلة) بشكل مختلف عن الإشارات المتزامنة (مثل أخطاء القطع، إلخ، حيث عنوان الإشارة حاسم).

إذا وصلت إشارة غير متزامنة عند تنفيذ جزء، فإن معالج إشارات دينامو سيضعها في طابور ويعيد التحكم إلى ذاكرة الأجزاء المؤقتة. تُعالَج جميع الإشارات غير المتزامنة في الطابور عندما يحدث خروج عادي تالٍ من ذاكرة الأجزاء المؤقتة. هذا يسمح لدينامو بتوفير سياق إشارة مناسب لمعالج التطبيق حيث أن التحكم ليس في منتصف جزء محسَّن في الوقت الذي يُبنى فيه سياق الإشارة.

لتحديد زمن انتقال معالجة الإشارات غير المتزامنة، يفك معالج إشارات دينامو ربط جميع التفريعات المربوطة على الجزء الحالي قبل استئناف تنفيذ الجزء. لفصل الحلقات الذاتية بطريقة مماثلة، يبث مولِّد الأجزاء عقب خروج لكل تفريع حلقة ذاتية بالإضافة إلى أعقاب الخروج لتفريعات خروج الجزء. يجبر فك ربط الجزء الحالي تفريع خروج الجزء التالي على الخروج من ذاكرة الأجزاء المؤقتة عبر عقب الخروج، مما يمنع إمكانية دوران التحكم داخل ذاكرة الأجزاء المؤقتة لفترة طويلة بشكل تعسفي قبل معالجة الإشارات في الطابور. تسمح هذه الميزة لدينامو بالعمل في بيئات يجب فيها تلبية قيود الوقت الفعلي الناعم.

من ناحية أخرى، الإشارات المتزامنة إشكالية، لأنه لا يمكن تأجيلها. الحل الجذري هو قمع تحويلات إزالة الشيفرة وإعادة الترتيب تماماً. البديل الأكثر قبولاً هو استخدام تقنيات مماثلة لتلك المطورة لتصحيح الشيفرة المحسَّنة لإزالة التحسين من شيفرة الجزء قبل محاولة بناء سياق الإشارة المتزامنة. لحسن الحظ، مشكلة إزالة التحسين أبسط بكثير في دينامو حيث تُعتبَر فقط الأجزاء ذات الخط المستقيم أثناء التحسين. يمكن تخزين سجلات التحسين مع كل جزء يصف إجراءات التعويض التي يجب تنفيذها عند تسليم الإشارة، مثل تنفيذ تعليمة محذوفة سابقاً. هذا حالياً جهد مستمر في مشروع دينامو.

ينفِّذ نموذجنا الأولي حالياً حلاً أقل طموحاً لهذه المشكلة، بتقسيم تحسينات الأثر إلى فئتين، محافظ وعدواني. التحسينات المحافظة تسمح ببناء سياق الإشارة الدقيق إذا حدث خطأ متزامن أثناء تنفيذ الجزء. التحسينات العدوانية من ناحية أخرى لا يمكنها ضمان ذلك. تتضمن أمثلة التحسينات المحافظة نشر الثوابت وطي الثوابت وتقليل القوة ونشر النسخ وإزالة التفريعات الزائدة. تتضمن الفئة العدوانية جميع التحسينات المحافظة بالإضافة إلى إزالة الشيفرة الميتة وإغراق الشيفرة وحركة شيفرة ثابتة الحلقة. بعض التحسينات العدوانية، مثل إزالة التحميل الزائد، يمكن أن تكون أحياناً غير صحيحة، إذا كان التحميل من موقع ذاكرة متطاير.

محسِّن أثر دينامو قادر على البدء في وضع التحسين العدواني، والتحول إلى الوضع المحافظ متبوعاً بمسح ذاكرة الأجزاء المؤقتة إذا صودف أي تسلسل تعليمات مشبوه. لسوء الحظ، لا يوفر الملف الثنائي PA-RISC معلومات حول عمليات الذاكرة المتطايرة أو معلومات حول معالجات الإشارات المثبتة بالبرنامج. لذا فإن هذه القدرة غير مستخدمة حالياً في دينامو. في إصدار مستقبلي من دينامو، نخطط للتحقيق في طرق للسماح لمولِّد تسلسل التعليمات الأصلية المدخل لدينامو بتوفير تلميحات لدينامو. يمكن لدينامو استخدام مثل هذه التلميحات إذا كانت متاحة، لكنه لن يعتمد عليها في العمل.

---

### Translation Notes

- **Figures referenced:** Figure 1 (box K - signal handling)
- **Key concepts:** Signal context reconstruction, asynchronous vs. synchronous signals, signal queueing, de-optimization
- **Optimization categories:** Conservative (safe for signals) vs. aggressive (not signal-safe)
- **Examples:** Conservative (constant propagation, copy propagation) vs. aggressive (dead code removal, code sinking)
- **Real-time consideration:** Bounded signal latency through unlinking
- **Platform limitation:** PA-RISC binary lacks volatile memory and signal handler information

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
