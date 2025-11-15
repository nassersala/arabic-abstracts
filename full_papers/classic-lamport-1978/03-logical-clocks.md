# Section 3: Logical Clocks
## القسم 3: الساعات المنطقية

**Section:** logical-clocks
**Translation Quality:** 0.89
**Glossary Terms Used:** logical clock, timestamp, event, process, algorithm, message, happened before

---

### English Version

We now introduce clocks into the system. We begin with an abstract point of view in which a clock is just a way of assigning a number to an event, where the number is thought of as the time at which the event occurred. More precisely, we define a clock C_i for each process P_i to be a function which assigns a number C_i⟨a⟩ to any event a in that process. The entire system of clocks is represented by the function C which assigns to any event b the number C⟨b⟩, where C⟨b⟩ = C_j⟨b⟩ if b is an event in process P_j. For now, we make no assumption about the relation of the numbers C_i⟨a⟩ to physical time, so we can think of the clocks C_i as logical clocks. They may be implemented by counters with no actual timing mechanism.

We now consider what it means for such a system of clocks to be correct. We cannot base "correctness" on physical time, since we have no way to measure physical time. Therefore, we base it upon the happened before relation "→". The correct time order of events is the one defined by the relation "→". Our first requirement for the system of clocks is:

**Clock Condition.** For any events a, b: if a → b then C⟨a⟩ < C⟨b⟩.

Note that we cannot expect the converse condition to hold as well, since if a and b are concurrent events, then neither a → b nor b → a, so we can have C⟨a⟩ < C⟨b⟩ or C⟨b⟩ < C⟨a⟩.

From the definition of the relation "→", it follows that the Clock Condition is satisfied if the following two conditions hold:

**C1.** If a and b are events in process P_i, and a comes before b, then C_i⟨a⟩ < C_i⟨b⟩.

**C2.** If a is the sending of a message by process P_i and b is the receipt of that message by process P_j, then C_i⟨a⟩ < C_j⟨b⟩.

We can regard a process as a sequence of events. Between any two successive events, the process performs some internal algorithm which changes its state. Assuming that an event is represented by a change in the local state and that all state changes occur one at a time, we can regard a process as a sequence of events a_1, a_2, a_3, ... .

We now give an algorithm for implementing a system of logical clocks which satisfies conditions C1 and C2. The algorithm consists of the following implementation rules which each process must follow:

**IR1.** Each process P_i increments C_i between any two successive events.

**IR2.** (a) If event a is the sending of a message m by process P_i, then the message m contains a timestamp T_m = C_i⟨a⟩.
     (b) Upon receiving a message m, process P_j sets C_j greater than or equal to its present value and greater than T_m.

More precisely, IR2(b) can be stated as follows: if the event b is the receipt of a message m by P_j, then P_j sets C_j to be greater than or equal to max(C_j, T_m) + 1 upon executing the event b. (Adding 1 is necessary to ensure that C_j⟨b⟩ > T_m.)

It is easy to see that this algorithm ensures that conditions C1 and C2 are satisfied. From C1 and C2 it follows that the Clock Condition is satisfied, so the partial ordering "→" is preserved by the function C.

Note that the algorithm gives us a way of assigning times to events which is consistent with the "→" relation. However, it does not tell us how fast the clocks should run. For a totally asynchronous system, we can make them run as slowly as we wish. In Section 4, we will consider the case in which the clocks must run at approximately the rate of physical time.

---

### النسخة العربية

نقدم الآن الساعات في النظام. نبدأ بوجهة نظر مجردة حيث تكون الساعة مجرد طريقة لتعيين رقم لحدث ما، حيث يُفهم الرقم على أنه الوقت الذي وقع فيه الحدث. وبشكل أكثر دقة، نُعرّف ساعة C_i لكل عملية P_i لتكون دالة تُسند رقماً C_i⟨a⟩ لأي حدث a في تلك العملية. يُمثَّل النظام الكامل للساعات بالدالة C التي تُسند لأي حدث b الرقم C⟨b⟩، حيث C⟨b⟩ = C_j⟨b⟩ إذا كان b حدثاً في العملية P_j. في الوقت الحالي، لا نقدم أي افتراض حول علاقة الأرقام C_i⟨a⟩ بالوقت الفيزيائي، لذلك يمكننا التفكير في الساعات C_i كساعات منطقية. يمكن تنفيذها بواسطة عدادات بدون آلية توقيت فعلية.

نعتبر الآن ما يعنيه أن يكون نظام الساعات هذا صحيحاً. لا يمكننا أن نبني "الصحة" على الوقت الفيزيائي، لأنه ليس لدينا طريقة لقياس الوقت الفيزيائي. لذلك، نبنيها على علاقة "حدث قبل" "→". الترتيب الزمني الصحيح للأحداث هو الذي تحدده العلاقة "→". متطلبنا الأول لنظام الساعات هو:

**شرط الساعة.** لأي حدثين a، b: إذا كان a → b فإن C⟨a⟩ < C⟨b⟩.

لاحظ أننا لا يمكن أن نتوقع أن يصح الشرط العكسي أيضاً، لأنه إذا كان a و b حدثين متزامنين، فإنه لا a → b ولا b → a، لذلك يمكن أن يكون C⟨a⟩ < C⟨b⟩ أو C⟨b⟩ < C⟨a⟩.

من تعريف العلاقة "→"، يتبع أن شرط الساعة يتحقق إذا تحقق الشرطان التاليان:

**C1.** إذا كان a و b حدثين في العملية P_i، وجاء a قبل b، فإن C_i⟨a⟩ < C_i⟨b⟩.

**C2.** إذا كان a هو إرسال رسالة من العملية P_i و b هو استلام تلك الرسالة من العملية P_j، فإن C_i⟨a⟩ < C_j⟨b⟩.

يمكننا اعتبار العملية تسلسلاً من الأحداث. بين أي حدثين متتاليين، تؤدي العملية بعض الخوارزمية الداخلية التي تغير حالتها. بافتراض أن الحدث يُمثَّل بتغيير في الحالة المحلية وأن جميع تغييرات الحالة تحدث واحداً تلو الآخر، يمكننا اعتبار العملية تسلسلاً من الأحداث a_1، a_2، a_3، ...

نقدم الآن خوارزمية لتنفيذ نظام من الساعات المنطقية التي تحقق الشرطين C1 و C2. تتكون الخوارزمية من قواعد التنفيذ التالية التي يجب على كل عملية اتباعها:

**IR1.** كل عملية P_i تزيد C_i بين أي حدثين متتاليين.

**IR2.** (أ) إذا كان الحدث a هو إرسال رسالة m من العملية P_i، فإن الرسالة m تحتوي على طابع زمني T_m = C_i⟨a⟩.
     (ب) عند استلام رسالة m، تضع العملية P_j قيمة C_j أكبر من أو تساوي قيمتها الحالية وأكبر من T_m.

بشكل أكثر دقة، يمكن صياغة IR2(ب) كما يلي: إذا كان الحدث b هو استلام رسالة m بواسطة P_j، فإن P_j تضع C_j لتكون أكبر من أو تساوي max(C_j, T_m) + 1 عند تنفيذ الحدث b. (إضافة 1 ضرورية لضمان أن C_j⟨b⟩ > T_m.)

من السهل رؤية أن هذه الخوارزمية تضمن تحقيق الشرطين C1 و C2. من C1 و C2 يتبع أن شرط الساعة محقق، وبالتالي يُحفظ الترتيب الجزئي "→" بواسطة الدالة C.

لاحظ أن الخوارزمية تعطينا طريقة لتعيين أوقات للأحداث تتسق مع العلاقة "→". ومع ذلك، لا تخبرنا بمدى سرعة تشغيل الساعات. بالنسبة لنظام لامتزامن تماماً، يمكننا جعلها تعمل ببطء كما نريد. في القسم 4، سننظر في الحالة التي يجب فيها أن تعمل الساعات بمعدل قريب من معدل الوقت الفيزيائي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** logical clock, timestamp, Clock Condition, implementation rules (IR1, IR2)
- **Equations:** C_i⟨a⟩, C⟨b⟩, max(C_j, T_m) + 1
- **Citations:** 0
- **Special handling:** Mathematical notation preserved; conditions C1, C2, IR1, IR2 kept with same labels for consistency

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
