# Section 6: Managing Diverse Resources
## القسم 6: إدارة موارد متنوعة

**Section:** managing-diverse-resources
**Translation Quality:** 0.86
**Glossary Terms Used:** I/O bandwidth, mutex, synchronization, inverse lottery, space-shared resources, time-shared resources, virtual circuit, ATM, priority inversion, waiting time, throughput

---

### English Version

Lotteries can be used to manage many diverse resources, such as processor time, I/O bandwidth, and access to locks. Lottery scheduling also appears promising for scheduling communication resources, such as access to network ports. For example, ATM switches schedule virtual circuits to determine which buffered cell should next be forwarded. Lottery scheduling could be used to provide different levels of service to virtual circuits competing for congested channels. In general, a lottery can be used to allocate resources wherever queueing is necessary for resource access.

## 6.1 Synchronization Resources

Contention due to synchronization can substantially affect computation rates. Lottery scheduling can be used to control the relative waiting times of threads competing for lock access. We have extended the Mach CThreads library to support a lottery-scheduled mutex type in addition to the standard mutex implementation. A lottery-scheduled mutex has an associated *mutex currency* and an *inheritance ticket* issued in that currency.

All threads that are blocked waiting to acquire the mutex perform ticket transfers to fund the mutex currency. The mutex transfers its inheritance ticket to the thread which currently holds the mutex. The net effect of these transfers is that a thread which acquires the mutex executes with its own funding plus the funding of all waiting threads, as depicted in Figure 10. This solves the priority inversion problem [Sha90], in which a mutex owner with little funding could execute very slowly due to competition with other threads for the processor, while a highly funded thread remains blocked on the mutex.

When a thread releases a lottery-scheduled mutex, it holds a lottery among the waiting threads to determine the next mutex owner. The thread then moves the mutex inheritance ticket to the winner, and yields the processor. The next thread to execute may be the selected waiter or some other thread that does not need the mutex; the normal processor lottery will choose fairly based on relative funding.

We have experimented with our mutex implementation using a synthetic multithreaded application in which $n$ threads compete for the same mutex. Each thread repeatedly acquires the mutex, holds it for $h$ milliseconds, releases the mutex, and computes for another $t$ milliseconds. Figure 11 provides frequency histograms for a typical experiment with $n = 8$, $h = 50$, and $t = 50$. The eight threads were divided into two groups (A, B) of four threads each, with the ticket allocation A:B = 2:1. Over the entire two-minute experiment, group A threads acquired the mutex a total of 763 times, while group B threads completed 423 acquisitions, for a relative throughput ratio of 1.80:1. The group A threads had a mean waiting time of $\mu = 450$ milliseconds, while the group B threads had a mean waiting time of $\mu = 948$ milliseconds, for a relative waiting time ratio of 1:2.11. Thus, both throughput and response time closely tracked the specified 2:1 ticket allocation.

## 6.2 Space-Shared Resources

Lotteries are useful for allocating indivisible time-shared resources, such as an entire processor. A variant of lottery scheduling can efficiently provide the same type of probabilistic proportional-share guarantees for finely divisible space-shared resources, such as memory. The basic idea is to use an *inverse lottery*, in which a "loser" is chosen to relinquish a unit of a resource that it holds. Conducting an inverse lottery is similar to holding a normal lottery, except that inverse probabilities are used. The probability $p$ that a client holding $t$ tickets will be selected by an inverse lottery with a total of $n$ clients and $T$ tickets is $p = \frac{1}{n-1}(1 - t/T)$. Thus, the more tickets a client has, the more likely it is to avoid having a unit of its resource revoked.

For example, consider the problem of allocating a physical page to service a virtual memory page fault when all physical pages are in use. A proportional-share policy based on inverse lotteries could choose a client from which to select a victim page with probability proportional to both $(1 - t/T)$ and the fraction of physical memory in use by that client.

## 6.3 Multiple Resources

Since rights for numerous resources are uniformly represented by lottery tickets, clients can use quantitative comparisons to make decisions involving tradeoffs between different resources. This raises some interesting questions regarding application funding policies in environments with multiple resources. For example, when does it make sense to shift funding from one resource to another? How frequently should funding allocations be reconsidered?

One way to abstract the evaluation of resource management options is to associate a separate *manager thread* with each application. A manager thread could be allocated a small fixed percentage (e.g., 1%) of an application's overall funding, causing it to be periodically scheduled while limiting its overall resource consumption. For inverse lotteries, it may be appropriate to allow the losing client to execute a short manager code fragment in order to adjust funding levels. The system should supply default managers for most applications; sophisticated applications could define their own management strategies. We plan to explore these preliminary ideas and other alternatives for more complex environments with multiple resources.

---

### النسخة العربية

يمكن استخدام اليانصيبات لإدارة العديد من الموارد المتنوعة، مثل وقت المعالج، وعرض نطاق الإدخال/الإخراج، والوصول إلى الأقفال. تبدو الجدولة اليانصيبية أيضاً واعدة لجدولة موارد الاتصالات، مثل الوصول إلى منافذ الشبكة. على سبيل المثال، تجدول مفاتيح ATM الدوائر الافتراضية لتحديد الخلية المخزنة مؤقتاً التي يجب إعادة توجيهها تالياً. يمكن استخدام الجدولة اليانصيبية لتوفير مستويات مختلفة من الخدمة للدوائر الافتراضية المتنافسة على القنوات المزدحمة. بشكل عام، يمكن استخدام يانصيب لتخصيص الموارد حيثما كان الانتظار في قائمة ضرورياً للوصول إلى الموارد.

## 6.1 موارد التزامن

يمكن أن يؤثر التنافس بسبب التزامن بشكل كبير على معدلات الحسابات. يمكن استخدام الجدولة اليانصيبية للتحكم في أوقات الانتظار النسبية للخيوط المتنافسة على الوصول إلى القفل. لقد قمنا بتوسيع مكتبة Mach CThreads لدعم نوع قفل تبادلي مجدول يانصيبياً بالإضافة إلى تطبيق القفل التبادلي القياسي. يحتوي القفل التبادلي المجدول يانصيبياً على *عملة قفل تبادلي* مرتبطة و *تذكرة وراثة* صادرة بتلك العملة.

تقوم جميع الخيوط المحظورة التي تنتظر الحصول على القفل التبادلي بنقل التذاكر لتمويل عملة القفل التبادلي. ينقل القفل التبادلي تذكرة وراثته إلى الخيط الذي يحمل القفل التبادلي حالياً. التأثير الصافي لهذه النقلات هو أن خيطاً يحصل على القفل التبادلي يُنفذ مع تمويله الخاص بالإضافة إلى تمويل جميع الخيوط المنتظرة، كما هو موضح في الشكل 10. هذا يحل مشكلة انعكاس الأولوية [Sha90]، حيث يمكن لمالك قفل تبادلي بتمويل قليل أن ينفذ ببطء شديد بسبب المنافسة مع خيوط أخرى على المعالج، بينما يظل خيط ممول بشكل كبير محظوراً على القفل التبادلي.

عندما يحرر خيط قفلاً تبادلياً مجدولاً يانصيبياً، فإنه يعقد يانصيباً بين الخيوط المنتظرة لتحديد مالك القفل التبادلي التالي. ثم ينقل الخيط تذكرة وراثة القفل التبادلي إلى الفائز، ويتنازل عن المعالج. قد يكون الخيط التالي الذي سيُنفذ هو المنتظر المحدد أو خيط آخر لا يحتاج إلى القفل التبادلي؛ سيختار يانصيب المعالج العادي بشكل عادل بناءً على التمويل النسبي.

لقد جربنا تطبيق القفل التبادلي الخاص بنا باستخدام تطبيق اصطناعي متعدد الخيوط حيث تتنافس $n$ خيوط على نفس القفل التبادلي. يحصل كل خيط بشكل متكرر على القفل التبادلي، ويحتفظ به لمدة $h$ ميليثانية، ويحرر القفل التبادلي، ويحسب لمدة $t$ ميليثانية أخرى. يوفر الشكل 11 رسوماً بيانية للتكرار لتجربة نموذجية مع $n = 8$ و $h = 50$ و $t = 50$. تم تقسيم الخيوط الثمانية إلى مجموعتين (A، B) من أربعة خيوط لكل منهما، مع تخصيص تذاكر A:B = 2:1. على مدار التجربة بأكملها التي استمرت دقيقتين، حصلت خيوط المجموعة A على القفل التبادلي إجمالي 763 مرة، بينما أكملت خيوط المجموعة B 423 عملية حصول، بنسبة إنتاجية نسبية 1.80:1. كان لخيوط المجموعة A متوسط وقت انتظار $\mu = 450$ ميليثانية، بينما كان لخيوط المجموعة B متوسط وقت انتظار $\mu = 948$ ميليثانية، بنسبة وقت انتظار نسبية 1:2.11. وبالتالي، تتبعت كل من الإنتاجية ووقت الاستجابة بشكل وثيق تخصيص التذاكر المحدد 2:1.

## 6.2 الموارد المشتركة بالمساحة

اليانصيبات مفيدة لتخصيص الموارد المشتركة بالوقت غير القابلة للتجزئة، مثل معالج كامل. يمكن لمتغير من الجدولة اليانصيبية توفير نفس نوع الضمانات الاحتمالية للمشاركة النسبية للموارد المشتركة بالمساحة القابلة للتقسيم بدقة، مثل الذاكرة. الفكرة الأساسية هي استخدام *يانصيب عكسي*، حيث يتم اختيار "خاسر" للتخلي عن وحدة من مورد يحمله. إجراء يانصيب عكسي مشابه لعقد يانصيب عادي، باستثناء أنه يتم استخدام احتمالات عكسية. احتمال $p$ أن يتم اختيار عميل يحمل $t$ تذاكر بواسطة يانصيب عكسي بإجمالي $n$ عملاء و $T$ تذاكر هو $p = \frac{1}{n-1}(1 - t/T)$. وبالتالي، كلما زاد عدد التذاكر التي يمتلكها العميل، زاد احتمال تجنبه إلغاء وحدة من موارده.

على سبيل المثال، ضع في اعتبارك مشكلة تخصيص صفحة فيزيائية لخدمة خطأ صفحة ذاكرة افتراضية عندما تكون جميع الصفحات الفيزيائية قيد الاستخدام. يمكن لسياسة مشاركة نسبية قائمة على يانصيبات عكسية أن تختار عميلاً لاختيار صفحة ضحية منه باحتمال متناسب مع كل من $(1 - t/T)$ والكسر من الذاكرة الفيزيائية المستخدمة بواسطة ذلك العميل.

## 6.3 موارد متعددة

نظراً لأن حقوق موارد عديدة ممثلة بشكل موحد بتذاكر يانصيب، يمكن للعملاء استخدام مقارنات كمية لاتخاذ قرارات تتضمن مقايضات بين موارد مختلفة. هذا يثير بعض الأسئلة المثيرة للاهتمام فيما يتعلق بسياسات تمويل التطبيقات في بيئات ذات موارد متعددة. على سبيل المثال، متى يكون من المنطقي تحويل التمويل من مورد إلى آخر؟ كم مرة يجب إعادة النظر في تخصيصات التمويل؟

إحدى طرق تجريد تقييم خيارات إدارة الموارد هي ربط *خيط مدير* منفصل بكل تطبيق. يمكن تخصيص خيط مدير نسبة مئوية ثابتة صغيرة (على سبيل المثال، 1٪) من التمويل الإجمالي للتطبيق، مما يتسبب في جدولته بشكل دوري مع تحديد استهلاكه الإجمالي للموارد. بالنسبة ليانصيبات العكسية، قد يكون من المناسب السماح للعميل الخاسر بتنفيذ جزء صغير من كود المدير من أجل تعديل مستويات التمويل. يجب على النظام توفير مديرين افتراضيين لمعظم التطبيقات؛ يمكن للتطبيقات المتطورة تحديد استراتيجيات الإدارة الخاصة بها. نخطط لاستكشاف هذه الأفكار الأولية وبدائل أخرى لبيئات أكثر تعقيداً مع موارد متعددة.

---

### Translation Notes

- **Figures referenced:** Figure 10 (Lock Funding), Figure 11 (Mutex Waiting Times)
- **Key terms introduced:**
  - inverse lottery: يانصيب عكسي
  - mutex currency: عملة قفل تبادلي
  - inheritance ticket: تذكرة وراثة
  - space-shared resources: موارد مشتركة بالمساحة
  - time-shared resources: موارد مشتركة بالوقت
  - virtual circuit: دائرة افتراضية
  - ATM switch: مفتاح ATM
  - manager thread: خيط مدير
- **Equations:** $p = \frac{1}{n-1}(1 - t/T)$, other probability expressions
- **Citations:** [Sha90]
- **Special handling:** Mathematical formulas preserved with Arabic context

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
