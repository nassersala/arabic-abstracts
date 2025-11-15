# Section 4: Ordering the Events Totally
## القسم 4: الترتيب الكامل للأحداث

**Section:** ordering-totally
**Translation Quality:** 0.86
**Glossary Terms Used:** total ordering, partial ordering, logical clock, distributed system, mutual exclusion, state machine, synchronization

---

### English Version

We can use the system of clocks described above to place a total ordering on the set of all system events. We simply order the events by the times at which they occur. To break ties, we use any arbitrary total ordering < of the processes. More precisely, we define a relation ⇒ as follows: if a is an event in process P_i and b is an event in process P_j, then a ⇒ b if and only if either (i) C_i⟨a⟩ < C_j⟨b⟩ or (ii) C_i⟨a⟩ = C_j⟨b⟩ and P_i < P_j.

It is easy to show that this defines a total ordering, and that the Clock Condition implies that if a → b then a ⇒ b. In other words, the relation ⇒ is a way of completing the "happened before" partial ordering to a total ordering.

The ordering ⇒ depends upon the system of clocks C_i, and is not unique. Different choices of clocks which satisfy the Clock Condition yield different total orderings. Given any total ordering ⇒' which extends the partial ordering "→", there exists a system of clocks satisfying the Clock Condition which yields that total ordering according to the above construction.

We can now give a simple method for solving any synchronization problem. We state the problem in terms of a set of commands which are to be executed by the processes. A solution to the problem consists of an algorithm which satisfies a simple correctness condition. For example, in the mutual exclusion problem, the commands are of the form "Process P_i enters critical section" and "Process P_i leaves critical section". The correctness condition is that each process which has entered its critical section must leave it before another process can enter its critical section.

The main point is that the correctness of the algorithm need only be maintained with respect to the ordering ⇒. In other words, all that we require is that the algorithm work under the assumption that if a ⇒ b then a happened before b. It need not work if some event b happens before an event a even though a ⇒ b. This may seem like a rather weak requirement. However, we will show that any algorithm which meets this requirement can be implemented with our logical clocks.

**The Mutual Exclusion Problem**

As an illustration of the method, we consider the mutual exclusion problem. We assume that the system is composed of a fixed collection of processes which share a single resource. Only one process can use the resource at a time. We wish to find an algorithm for granting the resource to a process which satisfies the following three conditions:

(I) A process which has been granted the resource must release it before it can be granted to another process.

(II) Different requests for the resource must be granted in the order in which they are made.

(III) If every process which is granted the resource eventually releases it, then every request is eventually granted.

We assume that the processes are completely deterministic, so that if a process is granted the resource, then its subsequent behavior (including when it releases the resource) is completely determined.

Condition II is the interesting one. We wish to grant requests in their order according to the relation ⇒ defined above. (Note that this is only a conceptual requirement. A process has no way of knowing if its request "really" happened before another process's request in the total ordering ⇒.)

The algorithm is quite simple. Each process maintains its own request queue which is never seen by any other process. We assume that the messages are received in the same order that they are sent. (This assumption is not necessary, but it simplifies the presentation.) The algorithm is defined by the following five rules. For convenience, the actions defined by each rule are assumed to form a single event.

1. To request the resource, process P_i sends the message "P_i requests resource" with timestamp T_m to every other process, and puts that message on its request queue, where T_m is the timestamp of the message.

2. When process P_j receives the message "P_i requests resource" with timestamp T_m, it places it on its request queue and sends a timestamped acknowledgment message to P_i.

3. To release the resource, process P_i removes any "P_i requests resource" message from its request queue and sends a timestamped "P_i releases resource" message to every other process.

4. When process P_j receives a "P_i releases resource" message, it removes any "P_i requests resource" message from its request queue.

5. Process P_i is granted the resource when the following two conditions are satisfied: (i) There is a "P_i requests resource" message in its request queue which is ordered before any other request message in its queue by the relation ⇒. (ii) P_i has received a message from every other process timestamped later than T_m.

Note that conditions (i) and (ii) of rule 5 are tested locally by P_i. It is easy to verify that the algorithm defined by rules 1-5 satisfies conditions I-III. Observe that if the anomalous behavior described in the introduction can occur, then the ordering of events perceived by a process may differ from the total ordering ⇒, and the algorithm may fail to satisfy condition II.

This is a distributed algorithm. Each process independently follows the algorithm, and there is no central synchronizing process or central storage.

---

### النسخة العربية

يمكننا استخدام نظام الساعات الموصوف أعلاه لوضع ترتيب كامل على مجموعة جميع أحداث النظام. ببساطة نرتب الأحداث حسب الأوقات التي تحدث فيها. لكسر التعادل، نستخدم أي ترتيب كامل تعسفي < للعمليات. بشكل أكثر دقة، نُعرّف العلاقة ⇒ كما يلي: إذا كان a حدثاً في العملية P_i و b حدثاً في العملية P_j، فإن a ⇒ b إذا وفقط إذا كان إما (i) C_i⟨a⟩ < C_j⟨b⟩ أو (ii) C_i⟨a⟩ = C_j⟨b⟩ و P_i < P_j.

من السهل إظهار أن هذا يُعرّف ترتيباً كاملاً، وأن شرط الساعة يعني أنه إذا كان a → b فإن a ⇒ b. بعبارة أخرى، العلاقة ⇒ هي طريقة لإكمال الترتيب الجزئي "حدث قبل" إلى ترتيب كامل.

يعتمد الترتيب ⇒ على نظام الساعات C_i، وليس فريداً. الخيارات المختلفة للساعات التي تحقق شرط الساعة تنتج ترتيبات كاملة مختلفة. بالنسبة لأي ترتيب كامل ⇒' الذي يوسع الترتيب الجزئي "→"، يوجد نظام من الساعات يحقق شرط الساعة والذي ينتج ذلك الترتيب الكامل وفقاً للبناء أعلاه.

يمكننا الآن تقديم طريقة بسيطة لحل أي مسألة تزامن. نصوغ المسألة من حيث مجموعة من الأوامر التي يجب تنفيذها بواسطة العمليات. يتكون الحل للمسألة من خوارزمية تحقق شرط صحة بسيط. على سبيل المثال، في مسألة الاستبعاد المتبادل، تكون الأوامر من شكل "العملية P_i تدخل القسم الحرج" و "العملية P_i تغادر القسم الحرج". شرط الصحة هو أن كل عملية دخلت قسمها الحرج يجب أن تغادره قبل أن تتمكن عملية أخرى من الدخول إلى قسمها الحرج.

النقطة الرئيسية هي أن صحة الخوارزمية تحتاج فقط إلى الحفاظ عليها بالنسبة للترتيب ⇒. بعبارة أخرى، كل ما نطلبه هو أن تعمل الخوارزمية تحت افتراض أنه إذا كان a ⇒ b فإن a حدث قبل b. لا يلزم أن تعمل إذا حدث حدث b قبل حدث a حتى لو كان a ⇒ b. قد يبدو هذا متطلباً ضعيفاً إلى حد ما. ومع ذلك، سنُظهر أن أي خوارزمية تلبي هذا المتطلب يمكن تنفيذها بساعاتنا المنطقية.

**مسألة الاستبعاد المتبادل**

كتوضيح للطريقة، ننظر في مسألة الاستبعاد المتبادل. نفترض أن النظام يتكون من مجموعة ثابتة من العمليات التي تشترك في مورد واحد. يمكن لعملية واحدة فقط استخدام المورد في كل مرة. نرغب في إيجاد خوارزمية لمنح المورد لعملية تحقق الشروط الثلاثة التالية:

(I) العملية التي مُنحت المورد يجب أن تُطلقه قبل أن يمكن منحه لعملية أخرى.

(II) يجب منح الطلبات المختلفة للمورد بالترتيب الذي تم تقديمها به.

(III) إذا كانت كل عملية مُنحت المورد تُطلقه في النهاية، فإن كل طلب يُمنح في النهاية.

نفترض أن العمليات حتمية تماماً، بحيث إذا مُنحت عملية المورد، فإن سلوكها اللاحق (بما في ذلك متى تُطلق المورد) محدد تماماً.

الشرط II هو المثير للاهتمام. نرغب في منح الطلبات بترتيبها وفقاً للعلاقة ⇒ المُعرَّفة أعلاه. (لاحظ أن هذا مجرد متطلب مفاهيمي. ليس لدى العملية طريقة لمعرفة ما إذا كان طلبها "حقاً" حدث قبل طلب عملية أخرى في الترتيب الكامل ⇒.)

الخوارزمية بسيطة للغاية. كل عملية تحتفظ بقائمة طلباتها الخاصة والتي لا تُرى أبداً من قبل أي عملية أخرى. نفترض أن الرسائل تُستقبل بنفس الترتيب الذي تُرسل به. (هذا الافتراض ليس ضرورياً، لكنه يبسط العرض.) تُعرَّف الخوارزمية بالقواعد الخمس التالية. للراحة، يُفترض أن الإجراءات المُعرَّفة بواسطة كل قاعدة تشكل حدثاً واحداً.

1. لطلب المورد، ترسل العملية P_i الرسالة "P_i تطلب المورد" بطابع زمني T_m إلى كل عملية أخرى، وتضع تلك الرسالة في قائمة طلباتها، حيث T_m هو الطابع الزمني للرسالة.

2. عندما تستقبل العملية P_j الرسالة "P_i تطلب المورد" بطابع زمني T_m، تضعها في قائمة طلباتها وترسل رسالة إقرار بطابع زمني إلى P_i.

3. لإطلاق المورد، تزيل العملية P_i أي رسالة "P_i تطلب المورد" من قائمة طلباتها وترسل رسالة "P_i تُطلق المورد" بطابع زمني إلى كل عملية أخرى.

4. عندما تستقبل العملية P_j رسالة "P_i تُطلق المورد"، تزيل أي رسالة "P_i تطلب المورد" من قائمة طلباتها.

5. تُمنح العملية P_i المورد عندما يتحقق الشرطان التاليان: (i) يوجد رسالة "P_i تطلب المورد" في قائمة طلباتها مرتبة قبل أي رسالة طلب أخرى في قائمتها بواسطة العلاقة ⇒. (ii) استقبلت P_i رسالة من كل عملية أخرى بطابع زمني لاحق لـ T_m.

لاحظ أن الشرطين (i) و (ii) من القاعدة 5 يُختبران محلياً بواسطة P_i. من السهل التحقق من أن الخوارزمية المُعرَّفة بواسطة القواعد 1-5 تحقق الشروط I-III. لاحظ أنه إذا كان السلوك الشاذ الموصوف في المقدمة يمكن أن يحدث، فإن ترتيب الأحداث كما تراه العملية قد يختلف عن الترتيب الكامل ⇒، وقد تفشل الخوارزمية في تحقيق الشرط II.

هذه خوارزمية موزعة. كل عملية تتبع الخوارزمية بشكل مستقل، ولا توجد عملية تزامن مركزية أو تخزين مركزي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** total ordering (⇒), tie-breaking, mutual exclusion, critical section, request queue, acknowledgment
- **Equations:** a ⇒ b relation definition
- **Citations:** 0
- **Special handling:** Five-rule algorithm preserved with numbered rules; conditions I-III labeled consistently

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
