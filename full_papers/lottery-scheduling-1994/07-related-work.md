# Section 7: Related Work
## القسم 7: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** priority, fair share scheduler, microeconomic scheduler, decay-usage scheduling, auction, escalator algorithm, Spawn, market-based, statistical matching, bandwidth allocation

---

### English Version

Conventional operating systems commonly employ a simple notion of priority in scheduling tasks. A task with higher priority is given absolute precedence over a task with lower priority. Priorities may be static, or they may be allowed to vary dynamically. Many sophisticated priority schemes are somewhat arbitrary, since priorities themselves are rarely meaningfully assigned [Dei90]. The ability to express priorities provides absolute, but extremely crude, control over scheduling, since resource rights do not vary smoothly with priorities. Conventional priority mechanisms are also inadequate for insulating the resource allocation policies of separate modules. Since priorities are absolute, it is difficult to compose or abstract inter-module priority relationships.

Fair share schedulers allocate resources so that users get fair machine shares over long periods of time [Hen84, Kay88]. These schedulers monitor CPU usage and dynamically adjust conventional priorities to push actual usage closer to entitled shares. However, the algorithms used by these systems are complex, requiring periodic usage updates, complicated dynamic priority adjustments, and administrative parameter setting to ensure fairness on a time scale of minutes. A technique also exists for achieving service rate objectives in systems that employ decay-usage scheduling by manipulating base priorities and various scheduler parameters [Hel93]. While this technique avoids the addition of feedback loops introduced by other fair share schedulers, it still assumes a fixed workload consisting of long-running compute-bound processes to ensure steady-state fairness at a time scale of minutes.

Microeconomic schedulers [Dre88, Fer88, Wal92] use auctions to allocate resources among clients that bid monetary funds. Funds encapsulate resource rights and serve as a form of priority. Both the escalator algorithm proposed for uniprocessor scheduling [Dre88] and the distributed Spawn system [Wal89, Wal92] rely upon auctions in which bidders increase their bids linearly over time. The Spawn system successfully allocated resources proportional to client funding in a network of heterogeneous workstations. However, experience with Spawn revealed that auction dynamics can be unexpectedly volatile. The overhead of bidding also limits the applicability of auctions to relatively coarse-grain tasks.

A market-based approach for memory allocation has also been developed to allow memory-intensive applications to optimize their memory consumption in a decentralized manner [Har92]. This scheme charges applications for both memory leases and I/O capacity, allowing application-specific tradeoffs to be made. However, unlike a true market, prices are not permitted to vary with demand, and ancillary parameters are introduced to restrict resource consumption [Che93].

The statistical matching technique for fair switching in the AN2 network exploits randomness to support frequent changes of bandwidth allocation [And93]. This work is similar to our proposed application of lottery scheduling to communication channels.

---

### النسخة العربية

تستخدم أنظمة التشغيل التقليدية عادة مفهوماً بسيطاً للأولوية في جدولة المهام. تُعطى مهمة ذات أولوية أعلى الأسبقية المطلقة على مهمة ذات أولوية أقل. قد تكون الأولويات ثابتة، أو قد يُسمح لها بالتغير ديناميكياً. العديد من مخططات الأولوية المتطورة تعسفية إلى حد ما، حيث نادراً ما يتم تعيين الأولويات نفسها بشكل مفيد [Dei90]. توفر القدرة على التعبير عن الأولويات تحكماً مطلقاً، ولكنه خشن للغاية، في الجدولة، حيث لا تتغير حقوق الموارد بسلاسة مع الأولويات. آليات الأولوية التقليدية أيضاً غير كافية لعزل سياسات تخصيص الموارد للوحدات المنفصلة. نظراً لأن الأولويات مطلقة، فمن الصعب تكوين أو تجريد علاقات الأولوية بين الوحدات.

تخصص مجدولات المشاركة العادلة الموارد بحيث يحصل المستخدمون على حصص عادلة من الآلة على مدى فترات زمنية طويلة [Hen84, Kay88]. تراقب هذه المجدولات استخدام المعالج وتضبط الأولويات التقليدية ديناميكياً لدفع الاستخدام الفعلي بالقرب من الحصص المستحقة. ومع ذلك، فإن الخوارزميات المستخدمة بواسطة هذه الأنظمة معقدة، وتتطلب تحديثات استخدام دورية، وتعديلات أولوية ديناميكية معقدة، وتعيين معاملات إدارية لضمان العدالة على مقياس زمني من الدقائق. توجد أيضاً تقنية لتحقيق أهداف معدل الخدمة في الأنظمة التي توظف جدولة تناقص الاستخدام عن طريق التلاعب بالأولويات الأساسية ومعاملات المجدول المختلفة [Hel93]. في حين أن هذه التقنية تتجنب إضافة حلقات التغذية الراجعة التي أدخلتها مجدولات المشاركة العادلة الأخرى، فإنها لا تزال تفترض حملاً ثابتاً يتكون من عمليات طويلة الأمد مقيدة بالحوسبة لضمان عدالة الحالة المستقرة على مقياس زمني من الدقائق.

تستخدم مجدولات الاقتصاد الجزئي [Dre88, Fer88, Wal92] المزادات لتخصيص الموارد بين العملاء الذين يقدمون عطاءات بأموال نقدية. تغلف الأموال حقوق الموارد وتعمل كشكل من أشكال الأولوية. كل من خوارزمية المصعد المقترحة لجدولة المعالج الأحادي [Dre88] ونظام Spawn الموزع [Wal89, Wal92] يعتمدان على مزادات يزيد فيها المزايدون عطاءاتهم بشكل خطي مع مرور الوقت. نجح نظام Spawn في تخصيص الموارد بما يتناسب مع تمويل العملاء في شبكة من محطات العمل غير المتجانسة. ومع ذلك، كشفت التجربة مع Spawn أن ديناميكيات المزاد يمكن أن تكون متقلبة بشكل غير متوقع. تحد التكلفة الإضافية للمزايدة أيضاً من قابلية تطبيق المزادات على المهام الخشنة نسبياً.

تم أيضاً تطوير نهج قائم على السوق لتخصيص الذاكرة للسماح للتطبيقات المكثفة للذاكرة بتحسين استهلاكها للذاكرة بطريقة لامركزية [Har92]. يفرض هذا المخطط رسوماً على التطبيقات لكل من إيجارات الذاكرة وسعة الإدخال/الإخراج، مما يسمح بإجراء مقايضات خاصة بالتطبيق. ومع ذلك، على عكس السوق الحقيقية، لا يُسمح للأسعار بالتباين مع الطلب، ويتم إدخال معاملات إضافية لتقييد استهلاك الموارد [Che93].

تستغل تقنية المطابقة الإحصائية للتبديل العادل في شبكة AN2 العشوائية لدعم التغييرات المتكررة في تخصيص عرض النطاق [And93]. هذا العمل مشابه لتطبيقنا المقترح للجدولة اليانصيبية على قنوات الاتصال.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - escalator algorithm: خوارزمية المصعد
  - Spawn system: نظام Spawn
  - market-based approach: نهج قائم على السوق
  - statistical matching: مطابقة إحصائية
  - bandwidth allocation: تخصيص عرض النطاق
- **Equations:** None
- **Citations:** [Dei90], [Hen84, Kay88], [Hel93], [Dre88, Fer88, Wal92], [Wal89], [Har92], [Che93], [And93]
- **Special handling:** System names (Spawn, AN2) kept as is

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
