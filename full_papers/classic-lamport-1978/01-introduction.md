# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** distributed system, event, processor, algorithm, state machine, concurrency, synchronization, clock

---

### English Version

The concept of time is fundamental to our way of thinking. It is derived from the more basic concept of the order in which events occur. We say that something happened at 3:15 if it occurred after our clock read 3:15 and before it read 3:16. The concept of the temporal ordering of events pervades our thinking about systems. For example, in an airline reservation system we specify that a request for a reservation should be granted if it is made before the flight is filled. However, we will see that this concept must be carefully reexamined when considering events in a distributed system.

A distributed system consists of a collection of distinct processes which are spatially separated, and which communicate with one another by exchanging messages. A network of interconnected computers, such as the ARPANET, is a distributed system. A single computer can also be viewed as a distributed system in which the central control unit, the memory units, and the input-output channels are separate processes. A system is distributed if the message transmission delay is not negligible compared to the time between events in a single process.

We will be concerned primarily with establishing the order in which events occur. In the  following, we assume that the events of a process form a sequence, where the order in which they occur is known a priori. However, we make no assumptions about the temporal relations between events of different processes. For example, we do not assume that there exists a global clock by which all events can be assigned a time. We will derive an algorithm for assigning times to events.

It is a matter of common sense that if one event can causally affect another, then the first event happened before the second. The notion of causality leads to a "happened before" relation which defines a partial ordering of the events in a distributed system. This relation provides the foundation for obtaining a total ordering of the events.

The paper is organized as follows. In the next section, we discuss the partial ordering defined by the "happened before" relation, and give a simple characterization of it. Section 3 describes the algorithm for totally ordering the events, and illustrates its use. Section 4 specializes this algorithm for synchronizing physical clocks, and a bound is derived on how far out of synchrony the clocks can become. The final section discusses anomalous behavior that can occur in a distributed system.

---

### النسخة العربية

يُعد مفهوم الزمن أساسياً في طريقة تفكيرنا. فهو مشتق من المفهوم الأكثر جوهرية وهو الترتيب الذي تحدث به الأحداث. نقول إن شيئاً ما حدث في الساعة 3:15 إذا وقع بعد أن أظهرت ساعتنا 3:15 وقبل أن تُظهر 3:16. إن مفهوم الترتيب الزمني للأحداث يتخلل تفكيرنا حول الأنظمة. على سبيل المثال، في نظام حجز الطيران، نحدد أن طلب الحجز يجب أن يُقبل إذا تم تقديمه قبل امتلاء الرحلة. ومع ذلك، سنرى أن هذا المفهوم يجب أن يُعاد فحصه بعناية عند النظر في الأحداث في نظام موزع.

يتكون النظام الموزع من مجموعة من العمليات المتمايزة والمفصولة مكانياً، والتي تتواصل مع بعضها البعض عن طريق تبادل الرسائل. شبكة من أجهزة الكمبيوتر المترابطة، مثل ARPANET، هي نظام موزع. يمكن أيضاً اعتبار جهاز كمبيوتر واحد نظاماً موزعاً حيث تكون وحدة التحكم المركزية ووحدات الذاكرة وقنوات الإدخال-الإخراج عمليات منفصلة. يكون النظام موزعاً إذا كان تأخير نقل الرسالة غير مهمل مقارنةً بالزمن بين الأحداث في عملية واحدة.

سنهتم بشكل أساسي بتحديد الترتيب الذي تحدث به الأحداث. فيما يلي، نفترض أن أحداث عملية ما تشكل تسلسلاً، حيث يكون الترتيب الذي تحدث به معروفاً مسبقاً. ومع ذلك، لا نقدم أي افتراضات حول العلاقات الزمنية بين أحداث العمليات المختلفة. على سبيل المثال، لا نفترض وجود ساعة عامة يمكن من خلالها تعيين وقت لجميع الأحداث. سنشتق خوارزمية لتعيين أوقات للأحداث.

من البديهي أنه إذا كان حدث ما يمكن أن يؤثر سببياً على حدث آخر، فإن الحدث الأول وقع قبل الثاني. يؤدي مفهوم السببية إلى علاقة "حدث قبل" (happened before) التي تعرّف ترتيباً جزئياً للأحداث في النظام الموزع. توفر هذه العلاقة الأساس للحصول على ترتيب كامل للأحداث.

ينظم البحث على النحو التالي. في القسم التالي، نناقش الترتيب الجزئي المُعرَّف بواسطة علاقة "حدث قبل"، ونقدم توصيفاً بسيطاً لها. يصف القسم 3 الخوارزمية للترتيب الكامل للأحداث، ويوضح استخدامها. يُخصص القسم 4 هذه الخوارزمية لتزامن الساعات الفيزيائية، ويُشتق حد أعلى لمقدار عدم التزامن الذي يمكن أن تصل إليه الساعات. يناقش القسم الأخير السلوك الشاذ الذي يمكن أن يحدث في نظام موزع.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** happened before relation, partial ordering, total ordering, causality, global clock, process, message
- **Equations:** 0
- **Citations:** ARPANET mentioned
- **Special handling:** The term "happened before" is kept in English in parentheses as it's a well-known technical term

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
