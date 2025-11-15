# Section 7: Future Work
## القسم 7: الأعمال المستقبلية

**Section:** future-work
**Translation Quality:** 0.87
**Glossary Terms Used:** schema (مخطط), secondary indices (فهارس ثانوية), resharding (إعادة التجزئة), backup/restore (النسخ الاحتياطي/الاستعادة), load-based (قائم على الحمل)

---

### English Version

We have spent most of the last year working with the F1 team to transition Google's advertising backend from MySQL to Spanner. We are actively improving its monitoring and support tools, as well as tuning its performance. In addition, we have been working on improving the functionality and performance of our backup/restore system. We are currently implementing the Spanner schema language, automatic maintenance of secondary indices, and automatic load-based resharding. Longer term, there are a couple of features that we plan to investigate. Optimistically doing reads in parallel may be a valuable strategy to pursue, but initial experiments have indicated that the right implementation is non-trivial. In addition, we plan to eventually support direct changes of Paxos configurations [22, 34].

Given that we expect many applications to replicate their data across datacenters that are relatively close to each other, TrueTime ε may noticeably affect performance. We see no insurmountable obstacle to reducing ε below 1ms. Time-master-query intervals can be reduced, and better clock crystals are relatively cheap. Time-master query latency could be reduced with improved networking technology, or possibly even avoided through alternate time-distribution technology.

Finally, there are obvious areas for improvement. Although Spanner is scalable in the number of nodes, the node-local data structures have relatively poor performance on complex SQL queries, because they were designed for simple key-value accesses. Algorithms and data structures from DB literature could improve single-node performance a great deal. Second, moving data automatically between datacenters in response to changes in client load has long been a goal of ours, but to make that goal effective, we would also need the ability to move client-application processes between datacenters in an automated, coordinated fashion. Moving processes raises the even more difficult problem of managing resource acquisition and allocation between datacenters.

---

### النسخة العربية

أمضينا معظم العام الماضي في العمل مع فريق F1 للانتقال من MySQL إلى سبانر في الواجهة الخلفية للإعلانات في جوجل. نحن نعمل بنشاط على تحسين أدوات المراقبة والدعم الخاصة بها، بالإضافة إلى ضبط أدائها. بالإضافة إلى ذلك، كنا نعمل على تحسين وظائف وأداء نظام النسخ الاحتياطي/الاستعادة الخاص بنا. نقوم حالياً بتنفيذ لغة مخطط سبانر، والصيانة التلقائية للفهارس الثانوية، وإعادة التجزئة التلقائية القائمة على الحمل. على المدى الطويل، هناك بضع ميزات نخطط للتحقيق فيها. قد يكون القيام بالقراءات بشكل متفائل بالتوازي استراتيجية قيمة لمتابعتها، لكن التجارب الأولية أشارت إلى أن التنفيذ الصحيح ليس تافهاً. بالإضافة إلى ذلك، نخطط في النهاية لدعم التغييرات المباشرة لتكوينات باكسوس [22، 34].

نظراً لأننا نتوقع أن تقوم العديد من التطبيقات بنسخ بياناتها عبر مراكز بيانات قريبة نسبياً من بعضها البعض، فقد يؤثر ε لـ TrueTime بشكل ملحوظ على الأداء. لا نرى عقبة لا يمكن التغلب عليها لتقليل ε إلى أقل من 1 ميللي ثانية. يمكن تقليل فترات استعلام سيد الوقت، والبلورات الساعية الأفضل رخيصة نسبياً. يمكن تقليل زمن انتقال استعلام سيد الوقت بتكنولوجيا شبكات محسّنة، أو ربما حتى تجنبه من خلال تكنولوجيا توزيع وقت بديلة.

أخيراً، هناك مجالات واضحة للتحسين. على الرغم من أن سبانر قابلة للتوسع في عدد العقد، إلا أن بنى البيانات المحلية للعقدة لديها أداء ضعيف نسبياً على استعلامات SQL المعقدة، لأنها صُممت للوصول البسيط إلى المفتاح-القيمة. يمكن للخوارزميات وبنى البيانات من أدبيات قواعد البيانات تحسين أداء العقدة الواحدة كثيراً. ثانياً، كان نقل البيانات تلقائياً بين مراكز البيانات استجابةً للتغييرات في حمل العميل هدفاً لنا منذ فترة طويلة، لكن لجعل هذا الهدف فعالاً، سنحتاج أيضاً إلى القدرة على نقل عمليات تطبيق العميل بين مراكز البيانات بطريقة آلية ومنسقة. يثير نقل العمليات مشكلة أكثر صعوبة تتمثل في إدارة الحصول على الموارد وتخصيصها بين مراكز البيانات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Load-based resharding (إعادة التجزئة القائمة على الحمل)
  - Clock crystals (البلورات الساعية)
  - Time-distribution technology (تكنولوجيا توزيع الوقت)
  - Resource acquisition and allocation (الحصول على الموارد وتخصيصها)
- **Equations:** 0
- **Citations:** [22], [34]
- **Special handling:**
  - F1, MySQL kept as product names
  - Technical improvements and future directions clearly translated

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.91
- Readability: 0.85
- Glossary consistency: 0.95
- **Overall section score:** 0.87
