# Section 7: Related Work
## القسم 7: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** distributed system, fault-tolerant, parallel processing, commodity machine, cluster, locality optimization, backup task, scheduling, programming model

---

### English Version

Many systems have provided restricted programming models and used the restrictions to parallelize the computation automatically. For example, an associative function can be computed over all prefixes of an N element array in log N time on N processors using parallel prefix computations [6, 9, 13]. MapReduce can be considered a simplification and distillation of some of these models based on our experience with large real-world computations. More significantly, we provide a fault-tolerant implementation that scales to thousands of processors.

In contrast, most of the parallel processing systems have only been implemented on smaller scales and leave the details of handling machine failures to the programmer.

Bulk Synchronous Programming [17] and some MPI primitives [11] provide higher-level abstractions that make it easier for programmers to write parallel programs. A key difference between these systems and MapReduce is that MapReduce exploits a restricted programming model to parallelize the user program automatically and to provide transparent fault-tolerance.

Our locality optimization draws its inspiration from techniques such as active disks [12, 15], where computation is pushed into processing elements that are close to local disks, to reduce the amount of data sent across I/O subsystems or the network. We run on commodity processors to which a small number of disks are directly connected instead of running directly on disk controller processors, but the general approach is similar.

Our backup task mechanism is similar to the eager scheduling mechanism employed in the Charlotte System [3]. One of the shortcomings of simple eager scheduling is that if a given task causes repeated failures, the entire computation fails to complete. We fix some instances of this problem with our mechanism for skipping bad records.

The MapReduce implementation relies on an in-house cluster management system that is responsible for distributing and running user tasks on a large collection of shared machines. Though not the focus of this paper, the cluster management system is similar in spirit to other systems such as Condor [16].

The sorting facility that is a part of the MapReduce library is similar in operation to NOW-Sort [1]. Source machines (map workers) partition the data to be sorted and send it to one of R reduce workers. Each reduce worker sorts its data locally (in memory if possible). Of course NOW-Sort does not have the user-definable Map and Reduce functions that make our library widely applicable.

River [2] provides a programming model where processes communicate with each other by sending data over distributed queues. Like MapReduce, the River system tries to provide good average case performance even in the presence of non-uniformities introduced by heterogeneous hardware or system perturbations. River achieves this by careful scheduling of disk and network transfers to achieve balanced completion times. MapReduce has a different approach. By restricting the programming model, the MapReduce framework is able to partition the problem into a large number of fine-grained tasks. These tasks are dynamically scheduled on available workers so that faster workers process more tasks. The restricted programming model also allows us to schedule redundant executions of tasks near the end of the job which greatly reduces completion time in the presence of non-uniformities (such as slow or stuck workers).

BAD-FS [5] has a very different programming model from MapReduce, and unlike MapReduce, is targeted to the execution of jobs across a wide-area network. However, there are two fundamental similarities. (1) Both systems use redundant execution to recover from data loss caused by failures. (2) Both use locality-aware scheduling to reduce the amount of data sent across congested network links.

TACC [7] is a system designed to simplify construction of highly-available networked services. Like MapReduce, it relies on re-execution as a mechanism for implementing fault-tolerance.

---

### النسخة العربية

قدمت العديد من الأنظمة نماذج برمجية محدودة واستخدمت هذه القيود لتوازي الحساب تلقائياً. على سبيل المثال، يمكن حساب دالة تجميعية (associative function) على جميع بادئات مصفوفة من N عنصر في زمن log N على N معالج باستخدام حسابات البادئات المتوازية [6, 9, 13]. يمكن اعتبار MapReduce تبسيطاً وتقطيراً لبعض هذه النماذج بناءً على خبرتنا مع الحسابات الواقعية واسعة النطاق. والأهم من ذلك، نحن نقدم تطبيقاً متحملاً للأخطاء يتوسع ليشمل آلاف المعالجات.

على النقيض من ذلك، تم تنفيذ معظم أنظمة المعالجة المتوازية على نطاقات أصغر فقط وتترك تفاصيل التعامل مع أعطال الأجهزة للمبرمج.

توفر البرمجة المتزامنة المجمعة (Bulk Synchronous Programming) [17] وبعض الأوليات الأساسية في MPI [11] تجريدات عالية المستوى تسهل على المبرمجين كتابة برامج متوازية. يتمثل الفرق الرئيسي بين هذه الأنظمة وMapReduce في أن MapReduce يستغل نموذجاً برمجياً محدوداً لتوازي برنامج المستخدم تلقائياً ولتوفير تحمل شفاف للأخطاء.

يستمد تحسين الموضعية (locality optimization) لدينا إلهامه من تقنيات مثل الأقراص النشطة (active disks) [12, 15]، حيث يُدفع الحساب إلى عناصر المعالجة القريبة من الأقراص المحلية، لتقليل كمية البيانات المرسلة عبر أنظمة الإدخال/الإخراج الفرعية أو الشبكة. نحن نعمل على معالجات تجارية (commodity processors) متصلة مباشرة بعدد صغير من الأقراص بدلاً من العمل مباشرة على معالجات التحكم في الأقراص، لكن النهج العام مشابه.

آلية المهام الاحتياطية (backup task mechanism) لدينا مشابهة لآلية الجدولة المتحمسة (eager scheduling) المستخدمة في نظام Charlotte [3]. أحد أوجه القصور في الجدولة المتحمسة البسيطة هو أنه إذا تسببت مهمة معينة في فشل متكرر، فإن الحساب بأكمله يفشل في الاكتمال. نحن نعالج بعض حالات هذه المشكلة من خلال آليتنا لتخطي السجلات السيئة.

يعتمد تطبيق MapReduce على نظام إدارة عناقيد (cluster management system) داخلي مسؤول عن توزيع وتشغيل مهام المستخدم على مجموعة كبيرة من الأجهزة المشتركة. على الرغم من أن نظام إدارة العناقيد ليس محور هذا البحث، إلا أنه مشابه في الروح لأنظمة أخرى مثل Condor [16].

وسيلة الفرز التي تشكل جزءاً من مكتبة MapReduce مشابهة في العملية لـ NOW-Sort [1]. تقوم الأجهزة المصدر (عمال Map) بتقسيم البيانات المراد فرزها وإرسالها إلى أحد عمال Reduce من R عامل. يقوم كل عامل Reduce بفرز بياناته محلياً (في الذاكرة إن أمكن). بالطبع، NOW-Sort لا يحتوي على دوال Map وReduce القابلة للتعريف من قبل المستخدم التي تجعل مكتبتنا قابلة للتطبيق على نطاق واسع.

يوفر River [2] نموذجاً برمجياً حيث تتواصل العمليات مع بعضها البعض عن طريق إرسال البيانات عبر قوائم انتظار موزعة. مثل MapReduce، يحاول نظام River توفير أداء جيد للحالة المتوسطة حتى في وجود عدم توحّد (non-uniformities) ناتج عن أجهزة غير متجانسة أو اضطرابات النظام. يحقق River ذلك من خلال جدولة دقيقة لنقل البيانات عبر الأقراص والشبكة لتحقيق أوقات إنجاز متوازنة. MapReduce لديه نهج مختلف. من خلال تقييد النموذج البرمجي، يستطيع إطار عمل MapReduce تقسيم المشكلة إلى عدد كبير من المهام دقيقة التفاصيل (fine-grained tasks). يتم جدولة هذه المهام ديناميكياً على العمال المتاحين بحيث يعالج العمال الأسرع مزيداً من المهام. يسمح لنا النموذج البرمجي المقيد أيضاً بجدولة تنفيذات زائدة عن الحاجة للمهام بالقرب من نهاية الوظيفة، مما يقلل بشكل كبير من وقت الإنجاز في وجود عدم توحّد (مثل العمال البطيئين أو المتعطلين).

يحتوي BAD-FS [5] على نموذج برمجي مختلف تماماً عن MapReduce، وعلى عكس MapReduce، فهو يستهدف تنفيذ الوظائف عبر شبكة واسعة النطاق. ومع ذلك، هناك تشابهان أساسيان. (1) يستخدم كلا النظامين التنفيذ الزائد عن الحاجة للتعافي من فقدان البيانات الناجم عن الأعطال. (2) يستخدم كلاهما جدولة واعية بالموضعية (locality-aware scheduling) لتقليل كمية البيانات المرسلة عبر روابط الشبكة المزدحمة.

TACC [7] هو نظام مصمم لتبسيط بناء الخدمات الشبكية عالية التوافر. مثل MapReduce، يعتمد على إعادة التنفيذ كآلية لتنفيذ تحمل الأخطاء.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Bulk Synchronous Programming, MPI primitives, active disks, eager scheduling, commodity processors, cluster management, fine-grained tasks, locality-aware scheduling
- **Equations:** None
- **Citations:** [1], [2], [3], [5], [6], [7], [9], [11], [12], [13], [15], [16], [17] - extensive comparison with related systems
- **Special handling:** Multiple system comparisons (Bulk Synchronous Programming, MPI, active disks, Charlotte, Condor, NOW-Sort, River, BAD-FS, TACC)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
