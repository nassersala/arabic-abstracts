# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** scheduling, multithreaded, throughput, response time, computation, priority, fair share scheduler, microeconomic scheduler, proportional-share, resource management, lottery scheduling, time-shared, space-shared, I/O bandwidth, mutex

---

### English Version

Scheduling computations in multithreaded systems is a complex, challenging problem. Scarce resources must be multiplexed to service requests of varying importance, and the policy chosen to manage this multiplexing can have an enormous impact on throughput and response time. Accurate control over the quality of service provided to users and applications requires support for specifying relative computation rates. Such control is desirable across a wide spectrum of systems. For long-running computations such as scientific applications and simulations, the consumption of computing resources that are shared among users and applications of varying importance must be regulated [Hel93]. For interactive computations such as databases and media-based applications, programmers and users need the ability to rapidly focus available resources on tasks that are currently important [Dui90].

Few general-purpose schemes even come close to supporting flexible, responsive control over service rates. Those that do exist generally rely upon a simple notion of priority that does not provide the encapsulation and modularity properties required for the engineering of large software systems. In fact, with the exception of hard real-time systems, it has been observed that the assignment of priorities and dynamic priority adjustment schemes are often ad-hoc [Dei90]. Even popular priority-based schemes for CPU allocation such as decay-usage scheduling are poorly understood, despite the fact that they are employed by numerous operating systems, including Unix [Hel93].

Existing fair share schedulers [Hen84, Kay88] and microeconomic schedulers [Fer88, Wal92] successfully address some of the problems with absolute priority schemes. However, the assumptions and overheads associated with these systems limit them to relatively coarse control over long-running computations. Interactive systems require rapid, dynamic control over scheduling at a time scale of milliseconds to seconds.

We have developed lottery scheduling, a novel randomized mechanism that provides responsive control over the relative execution rates of computations. Lottery scheduling efficiently implements proportional-share resource management — the resource consumption rates of active computations are proportional to the relative shares that they are allocated. Lottery scheduling also provides excellent support for modular resource management. We have developed a prototype lottery scheduler for the Mach 3.0 microkernel, and found that it provides efficient, flexible control over the relative execution rates of compute-bound tasks, video-based applications, and client-server interactions. This level of control is not possible with current operating systems, in which adjusting scheduling parameters to achieve specific results is at best a black art.

Lottery scheduling can be generalized to manage many diverse resources, such as I/O bandwidth, memory, and access to locks. We have developed a prototype lottery-scheduled mutex implementation, and found that it provides flexible control over mutex acquisition rates. A variant of lottery scheduling can also be used to efficiently manage space-shared resources such as memory.

---

### النسخة العربية

جدولة الحسابات في الأنظمة متعددة الخيوط مشكلة معقدة وصعبة. يجب تعدد إرسال (multiplexing) الموارد النادرة لخدمة الطلبات ذات الأهمية المتفاوتة، ويمكن للسياسة المختارة لإدارة هذا التعدد أن يكون لها تأثير هائل على الإنتاجية ووقت الاستجابة. يتطلب التحكم الدقيق في جودة الخدمة المقدمة للمستخدمين والتطبيقات دعماً لتحديد معدلات الحسابات النسبية. يُعد مثل هذا التحكم مرغوباً فيه عبر طيف واسع من الأنظمة. بالنسبة للحسابات طويلة الأمد مثل التطبيقات العلمية والمحاكاة، يجب تنظيم استهلاك موارد الحوسبة المشتركة بين المستخدمين والتطبيقات ذات الأهمية المتفاوتة [Hel93]. بالنسبة للحسابات التفاعلية مثل قواعد البيانات والتطبيقات القائمة على الوسائط المتعددة، يحتاج المبرمجون والمستخدمون إلى القدرة على تركيز الموارد المتاحة بسرعة على المهام المهمة حالياً [Dui90].

قلة قليلة من المخططات متعددة الأغراض تقترب حتى من دعم التحكم المرن والسريع الاستجابة في معدلات الخدمة. تلك الموجودة تعتمد بشكل عام على مفهوم بسيط للأولوية لا يوفر خصائص التغليف والنمطية المطلوبة لهندسة أنظمة البرمجيات الكبيرة. في الواقع، باستثناء أنظمة الوقت الفعلي الصارمة، لوحظ أن تعيين الأولويات ومخططات التعديل الديناميكي للأولويات غالباً ما تكون عشوائية [Dei90]. حتى المخططات الشائعة القائمة على الأولوية لتخصيص المعالج مثل جدولة تناقص الاستخدام (decay-usage scheduling) مفهومة بشكل سيء، على الرغم من حقيقة أنها موظفة من قبل العديد من أنظمة التشغيل، بما في ذلك Unix [Hel93].

تتناول مجدولات المشاركة العادلة الحالية [Hen84, Kay88] ومجدولات الاقتصاد الجزئي [Fer88, Wal92] بنجاح بعض المشاكل المتعلقة بمخططات الأولوية المطلقة. ومع ذلك، فإن الافتراضات والتكاليف الإضافية المرتبطة بهذه الأنظمة تحدها إلى تحكم خشن نسبياً في الحسابات طويلة الأمد. تتطلب الأنظمة التفاعلية تحكماً ديناميكياً سريعاً في الجدولة على مقياس زمني من الميليثواني إلى الثواني.

لقد طورنا الجدولة اليانصيبية، وهي آلية عشوائية جديدة توفر تحكماً سريع الاستجابة في معدلات التنفيذ النسبية للحسابات. تطبق الجدولة اليانصيبية بكفاءة إدارة الموارد بالمشاركة النسبية — حيث تكون معدلات استهلاك الموارد للحسابات النشطة متناسبة مع الحصص النسبية المخصصة لها. توفر الجدولة اليانصيبية أيضاً دعماً ممتازاً للإدارة النمطية للموارد. لقد طورنا نموذجاً أولياً لمجدول يانصيبي لنواة ماخ 3.0 الدقيقة، ووجدنا أنه يوفر تحكماً فعالاً ومرناً في معدلات التنفيذ النسبية للمهام المقيدة بالحوسبة، وتطبيقات الفيديو، والتفاعلات بين العميل والخادم. هذا المستوى من التحكم غير ممكن مع أنظمة التشغيل الحالية، حيث يُعد تعديل معاملات الجدولة لتحقيق نتائج محددة في أحسن الأحوال فناً غامضاً.

يمكن تعميم الجدولة اليانصيبية لإدارة العديد من الموارد المتنوعة، مثل عرض نطاق الإدخال/الإخراج، والذاكرة، والوصول إلى الأقفال. لقد طورنا تطبيقاً نموذجياً أولياً لقفل تبادلي مجدول يانصيبياً، ووجدنا أنه يوفر تحكماً مرناً في معدلات الحصول على القفل التبادلي. يمكن أيضاً استخدام متغير من الجدولة اليانصيبية لإدارة الموارد المشتركة بالمساحة مثل الذاكرة بكفاءة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - multithreaded systems: الأنظمة متعددة الخيوط
  - multiplexing: تعدد الإرسال
  - decay-usage scheduling: جدولة تناقص الاستخدام
  - fair share scheduler: مجدول المشاركة العادلة
  - microeconomic scheduler: مجدول الاقتصاد الجزئي
  - black art: فن غامض
  - mutex: قفل تبادلي
  - space-shared resources: موارد مشتركة بالمساحة
- **Equations:** None
- **Citations:** [Hel93], [Dui90], [Dei90], [Hen84, Kay88], [Fer88, Wal92]
- **Special handling:** Technical terminology preserved with Arabic equivalents

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
