# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** transactional memory, concurrent, thread, atomicity, isolation, deadlock, monad, STM, opacity, synchronization, parallelism, composable

---

### English Version

The advent of multicore architectures has emphasized the importance of abstractions supporting correct and scalable multi-threaded programming. In this model, threads can collaborate by interacting on data structures (such as tables, message queues, buffers, etc.) kept in shared memory. Traditional lock-based mechanisms (like semaphores and monitors) used to regulate access to these shared data are notoriously difficult and error-prone, as they easily lead to deadlocks, race conditions and priority inversions; moreover, they are not composable and hinder parallelism, thus reducing efficiency and scalability. Transactional memory (TM) has emerged as a promising abstraction to replace locks. The basic idea is to mark blocks of code as atomic; then, execution of each block will appear either as if it was executed sequentially and instantaneously at some unique point in time, or, if aborted, as if it did not execute at all. This is obtained by means of optimistic executions: the blocks are allowed to run concurrently, and eventually if an interference is detected a transaction is restarted and its effects are rolled back. Thus, each transaction can be viewed in isolation as a single-threaded computation, significantly reducing the programmer's burden. Moreover, transactions are composable and ensure absence of deadlocks and priority inversions, automatic roll-back on exceptions, and increased concurrency.

However, in multi-threaded programming different transactions may need to interact and exchange data before committing. In this situation, transaction isolation is a severe shortcoming. A simple example is a request-response interaction between two transactions via a shared buffer, like in a master/worker situation. We could try to synchronize the threads accessing the buffer `b` by means of two semaphores `c1`, `c2` as follows:

```
// Party1 (Master)                    // Party2 (Worker)
atomically {                          atomically {
  <put request in b>                    down(c1); // wait for data
  up(c1);                               <get request from b>
  <some other code; may abort>          <compute answer; may abort>
  down(c2); // wait for answer          <put answer in b>
  <get answer from b; may abort>        up(c2);
}                                     }
```

Unfortunately, this solution does not work: any admissible execution requires an interleaved scheduling between the two transactions, thus violating isolation; hence, the transactions deadlock as none of them can progress. It is important to notice that this deadlock arises because interaction occurs between threads of different transactions; in fact, the solution above is perfectly fine for threads outside transactions or within the same transaction.

To overcome this limitation, in this paper we propose a programming model for safe, data-driven interactions between memory transactions. The key observation is that atomicity and isolation are two disjoint computational aspects:
- an atomic non-isolated block is executed "all-or-nothing", but its execution can overlap others' and uncontrolled access to shared data is allowed;
- a non-atomic isolated block is executed "as it were the only one" (i.e., in mutual exclusion with others), but no rollback on errors is provided.

Thus, a "normal" block of code is neither atomic nor isolated; a mutex block (like Java synchronized methods) is isolated but not atomic; and a usual TM transaction is a block which is both atomic and isolated. Our claim is that atomic non-isolated blocks can be fruitfully used for implementing safe composable interacting memory transactions—henceforth called open transactions.

In this model, a transaction is composed by several threads, called participants, which can cooperate on shared data. A transaction commits when all its participants commit, and aborts if any thread aborts. Threads participating to different transactions can access to shared data, but when this happens the transactions are transparently merged into a single one. For instance, the two transactions of the synchronization example above would automatically merge becoming the same transaction, so that the two threads can synchronize and proceed. Thus, this model relaxes the isolation requirement still guaranteeing atomicity and consistency; moreover, it allows for loosely-coupled interactions since transaction merging is driven only by run-time accesses to shared data, without any explicit coordination among the participants beforehand.

In summary, the contributions of this paper are the following:
- We present Open Transactional Memory, a transactional memory model where multi-threaded transactions can interact by non-isolated access to shared data. Consistency and atomicity are ensured by transparently merging transactions at runtime.
- We describe this model in the context of Concurrent Haskell (Section 3). Namely, we define two monads `OTM` and `ITM`, representing the computational aspects of atomic multi-threaded open (i.e., non-isolated) transactions and atomic single-threaded isolated transactions, respectively. Using the construct `atomic`, programs in the `OTM` monad are executed "all-or-nothing" but without isolation; hence these transactions can merge at runtime. When needed, blocks inside transactions can be executed in isolation by using the construct `isolated`. Both OTM and ITM transactions are composable, and we exploit Haskell type system to forbid irreversible effects inside these two monads. (In fact, OTM model can be implemented in any programming language, provided we have some means, either static or dynamic, to forbid irreversible effects inside transactions.)
- We provide a formal operational semantics of our system (Section 4). This semantics defines clearly the behaviour also in less intuitive situations, and serves as a reference for implementations. Using this semantics we prove that OTM satisfies the opacity correctness criterion for transactions.

Some concluding remarks and directions for future work are in Section 5.

---

### النسخة العربية

أكد ظهور معماريات متعددة النوى أهمية التجريدات التي تدعم البرمجة متعددة الخيوط الصحيحة والقابلة للتوسع. في هذا النموذج، يمكن للخيوط التعاون من خلال التفاعل على هياكل البيانات (مثل الجداول، وطوابير الرسائل، والمخازن المؤقتة، إلخ) المحفوظة في الذاكرة المشتركة. تُعد الآليات التقليدية المعتمدة على الأقفال (مثل العدادات السيمافورية والمراقبات) المستخدمة لتنظيم الوصول إلى هذه البيانات المشتركة صعبة بشكل معروف ومعرضة للأخطاء، حيث تؤدي بسهولة إلى الجمود، وحالات التسابق، وانعكاسات الأولوية؛ علاوة على ذلك، فهي غير قابلة للتركيب وتعيق التوازي، مما يقلل من الكفاءة وقابلية التوسع. ظهرت ذاكرة المعاملات (TM) كتجريد واعد لاستبدال الأقفال. الفكرة الأساسية هي وضع علامة على كتل الكود كذرية؛ بعد ذلك، سيبدو تنفيذ كل كتلة إما كما لو تم تنفيذها بشكل تسلسلي وفوري في نقطة زمنية فريدة، أو، إذا تم إحباطها، كما لو لم يتم تنفيذها على الإطلاق. يتم الحصول على ذلك من خلال التنفيذات المتفائلة: يُسمح للكتل بالتشغيل بشكل متزامن، وفي النهاية إذا تم اكتشاف تداخل، يتم إعادة تشغيل المعاملة والتراجع عن تأثيراتها. وبالتالي، يمكن النظر إلى كل معاملة بشكل معزول كحوسبة أحادية الخيط، مما يقلل بشكل كبير من عبء المبرمج. علاوة على ذلك، فإن المعاملات قابلة للتركيب وتضمن عدم وجود جمود وانعكاسات أولوية، والتراجع التلقائي عند الاستثناءات، والتزامن المتزايد.

ومع ذلك، في البرمجة متعددة الخيوط قد تحتاج المعاملات المختلفة إلى التفاعل وتبادل البيانات قبل الالتزام. في هذه الحالة، يعد عزل المعاملات قصوراً شديداً. مثال بسيط هو تفاعل الطلب-الاستجابة بين معاملتين عبر مخزن مؤقت مشترك، مثل حالة السيد/العامل. يمكننا محاولة مزامنة الخيوط التي تصل إلى المخزن المؤقت `b` باستخدام عدادين سيمافوريين `c1` و `c2` على النحو التالي:

```
// الطرف 1 (السيد)                      // الطرف 2 (العامل)
atomically {                          atomically {
  <وضع الطلب في b>                       down(c1); // انتظار البيانات
  up(c1);                               <الحصول على الطلب من b>
  <كود آخر; قد يُحبط>                     <حساب الإجابة; قد يُحبط>
  down(c2); // انتظار الإجابة             <وضع الإجابة في b>
  <الحصول على الإجابة من b; قد يُحبط>      up(c2);
}                                     }
```

لسوء الحظ، هذا الحل لا يعمل: أي تنفيذ مقبول يتطلب جدولة متشابكة بين المعاملتين، وبالتالي انتهاك العزل؛ وبالتالي، تتجمد المعاملات حيث لا يمكن لأي منهما التقدم. من المهم ملاحظة أن هذا الجمود ينشأ لأن التفاعل يحدث بين خيوط من معاملات مختلفة؛ في الواقع، الحل أعلاه مناسب تماماً للخيوط خارج المعاملات أو داخل نفس المعاملة.

للتغلب على هذا القيد، نقترح في هذا البحث نموذج برمجة للتفاعلات الآمنة والمدفوعة بالبيانات بين معاملات الذاكرة. الملاحظة الرئيسية هي أن الذرية والعزل هما جانبان حسابيان منفصلان:
- يتم تنفيذ الكتلة الذرية غير المعزولة بنمط "الكل أو لا شيء"، ولكن يمكن أن يتداخل تنفيذها مع الآخرين ويُسمح بالوصول غير المضبوط إلى البيانات المشتركة؛
- يتم تنفيذ الكتلة المعزولة غير الذرية "كما لو كانت الوحيدة" (أي، في استبعاد متبادل مع الآخرين)، ولكن لا يتم توفير التراجع عند الأخطاء.

وبالتالي، فإن الكتلة "العادية" من الكود ليست ذرية ولا معزولة؛ كتلة mutex (مثل طرق Java المتزامنة synchronized) معزولة ولكنها ليست ذرية؛ ومعاملة TM المعتادة هي كتلة ذرية ومعزولة في آن واحد. ادعاؤنا هو أن الكتل الذرية غير المعزولة يمكن استخدامها بشكل مثمر لتنفيذ معاملات ذاكرة متفاعلة قابلة للتركيب آمنة - والتي سنسميها من الآن فصاعداً المعاملات المفتوحة.

في هذا النموذج، تتكون المعاملة من عدة خيوط، تسمى المشاركين، والتي يمكن أن تتعاون على البيانات المشتركة. تلتزم المعاملة عندما يلتزم جميع المشاركين فيها، وتُحبط إذا أُحبط أي خيط. يمكن للخيوط المشاركة في معاملات مختلفة الوصول إلى البيانات المشتركة، ولكن عندما يحدث ذلك، يتم دمج المعاملات بشفافية في معاملة واحدة. على سبيل المثال، ستدمج المعاملتان في مثال المزامنة أعلاه تلقائياً لتصبحا نفس المعاملة، بحيث يمكن للخيطين المزامنة والمتابعة. وبالتالي، يخفف هذا النموذج من متطلبات العزل مع ضمان الذرية والاتساق؛ علاوة على ذلك، يسمح بالتفاعلات ضعيفة الاقتران حيث يتم دفع دمج المعاملات فقط من خلال الوصول في وقت التشغيل إلى البيانات المشتركة، دون أي تنسيق صريح بين المشاركين مسبقاً.

باختصار، مساهمات هذا البحث هي التالية:
- نقدم ذاكرة المعاملات المفتوحة، وهو نموذج ذاكرة معاملات حيث يمكن للمعاملات متعددة الخيوط التفاعل من خلال الوصول غير المعزول إلى البيانات المشتركة. يتم ضمان الاتساق والذرية من خلال دمج المعاملات بشفافية في وقت التشغيل.
- نصف هذا النموذج في سياق Haskell المتزامن (القسم 3). وتحديداً، نعرّف موناد `OTM` و `ITM`، اللذان يمثلان الجوانب الحسابية للمعاملات الذرية المفتوحة متعددة الخيوط (أي غير المعزولة) والمعاملات الذرية المعزولة أحادية الخيط، على التوالي. باستخدام البناء `atomic`، يتم تنفيذ البرامج في موناد `OTM` بنمط "الكل أو لا شيء" ولكن بدون عزل؛ وبالتالي يمكن دمج هذه المعاملات في وقت التشغيل. عند الحاجة، يمكن تنفيذ الكتل داخل المعاملات بشكل معزول باستخدام البناء `isolated`. كل من معاملات OTM و ITM قابلة للتركيب، ونستغل نظام أنواع Haskell لمنع التأثيرات غير القابلة للعكس داخل هذين الموناد. (في الواقع، يمكن تنفيذ نموذج OTM في أي لغة برمجة، شريطة أن يكون لدينا بعض الوسائل، إما ثابتة أو ديناميكية، لمنع التأثيرات غير القابلة للعكس داخل المعاملات.)
- نقدم دلالات تشغيلية رسمية لنظامنا (القسم 4). تحدد هذه الدلالات بوضوح السلوك أيضاً في المواقف الأقل حدسية، وتعمل كمرجع للتنفيذات. باستخدام هذه الدلالات نثبت أن OTM تحقق معيار الصحة المتمثل في العتامة للمعاملات.

بعض الملاحظات الختامية واتجاهات العمل المستقبلي موجودة في القسم 5.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Multicore architectures → معماريات متعددة النوى
  - Race conditions → حالات التسابق
  - Priority inversions → انعكاسات الأولوية
  - Optimistic executions → التنفيذات المتفائلة
  - Rolled back → التراجع
  - Single-threaded → أحادي الخيط
  - Request-response → الطلب-الاستجابة
  - Master/worker → السيد/العامل
  - Semaphore → عداد سيمافوري
  - Interleaved scheduling → جدولة متشابكة
  - Mutual exclusion → الاستبعاد المتبادل
  - Open transactions → المعاملات المفتوحة
  - Participants → المشاركين
  - Loosely-coupled → ضعيفة الاقتران
  - Conservative extension → امتداد محافظ
  - Operational semantics → دلالات تشغيلية

- **Equations:** None

- **Citations:**
  - [moss:transactionalmemorybook, st:dc1997]
  - [gk:ppopp08]

- **Special handling:**
  - Code examples preserved in original English with Arabic comments
  - Monad names (OTM, ITM) kept as-is
  - Haskell constructs (`atomic`, `isolated`) preserved

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
