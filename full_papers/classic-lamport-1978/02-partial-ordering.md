# Section 2: The Partial Ordering
## القسم 2: الترتيب الجزئي

**Section:** partial-ordering
**Translation Quality:** 0.87
**Glossary Terms Used:** event, process, distributed system, message, causality, partial ordering, concurrent

---

### English Version

We begin by defining a relation "→" on the set of events of a system. (For mathematicians, this relation is a partial ordering on the events.) We say that an event a happened before an event b, written a → b, if:

(1) If a and b are events in the same process, and a comes before b, then a → b.

(2) If a is the sending of a message by one process and b is the receipt of the same message by another process, then a → b.

(3) If a → b and b → c then a → c (transitivity).

Another way of viewing the definition is to say that a → b means that it is possible for event a to causally affect event b. Two distinct events a and b are said to be concurrent if a ↛ b and b ↛ a (neither a → b nor b → a holds).

We assume that a → a for any event a. (Systems in which an event can happen before itself do not seem to be physically meaningful.) This means that "→" is an irreflexive partial ordering. It is possible to have a ≠ b and yet a ↛ b and b ↛ a—i.e., two distinct events can be concurrent.

The relation "→" depends upon the system—i.e., given a system of processes with certain communication patterns, "→" is determined. We are not concerned with the mechanism by which the system is implemented. The processes communicate only by sending messages. We assume that the messages are sent and received through FIFO channels—i.e., messages sent through a single channel arrive in the same order they were sent. (This assumption can be relaxed, but it simplifies the discussion.)

It is important to realize that the relation "→" is defined with respect to a particular system of events. If we change the system, then "→" changes. For example, if a process sends a message and then later receives a reply to that message, the sending and receiving would be related by "→" in the new system but not in the old one.

The relation "→" can be illustrated by a space-time diagram in which the horizontal direction represents space (different processes) and the vertical direction represents time increasing upward. Points on the diagram represent events. If a → b then a appears lower than b. This is just the standard way of depicting a partial ordering.

**Definition:** For events a and b of process P, a comes before b in P, denoted a ⇒_P b, if a → b and there exists no event c of P such that a → c and c → b.

We can extend the relation "→" to an arbitrary set of events E by defining E_1 → E_2 to mean that there exist events e_1 in E_1 and e_2 in E_2 such that e_1 → e_2.

---

### النسخة العربية

نبدأ بتعريف علاقة "→" على مجموعة أحداث النظام. (بالنسبة لعلماء الرياضيات، هذه العلاقة هي ترتيب جزئي على الأحداث.) نقول إن حدثاً a وقع قبل حدث b، ويُكتب a → b، إذا:

(1) إذا كان a و b حدثين في نفس العملية، وجاء a قبل b، فإن a → b.

(2) إذا كان a هو إرسال رسالة من عملية ما و b هو استلام نفس الرسالة من عملية أخرى، فإن a → b.

(3) إذا كان a → b و b → c فإن a → c (خاصية التعدية).

طريقة أخرى لعرض التعريف هي القول بأن a → b يعني أنه من الممكن للحدث a أن يؤثر سببياً على الحدث b. يُقال إن حدثين متمايزين a و b متزامنان (concurrent) إذا كان a ↛ b و b ↛ a (أي لا a → b ولا b → a صحيحة).

نفترض أن a ↛ a لأي حدث a. (الأنظمة التي يمكن فيها أن يحدث حدث قبل نفسه لا تبدو ذات معنى فيزيائي.) هذا يعني أن "→" هي ترتيب جزئي لا انعكاسي (irreflexive). من الممكن أن يكون a ≠ b ومع ذلك a ↛ b و b ↛ a—أي أن حدثين متمايزين يمكن أن يكونا متزامنين.

تعتمد العلاقة "→" على النظام—أي أنه بالنظر إلى نظام من العمليات بأنماط اتصال معينة، يتم تحديد "→". نحن لا نهتم بالآلية التي يُنفذ بها النظام. تتواصل العمليات فقط عن طريق إرسال الرسائل. نفترض أن الرسائل تُرسل وتُستقبل عبر قنوات FIFO—أي أن الرسائل المرسلة عبر قناة واحدة تصل بنفس الترتيب الذي أُرسلت به. (يمكن تخفيف هذا الافتراض، لكنه يبسط المناقشة.)

من المهم إدراك أن العلاقة "→" مُعرَّفة بالنسبة لنظام معين من الأحداث. إذا غيرنا النظام، فإن "→" تتغير. على سبيل المثال، إذا أرسلت عملية رسالة ثم استقبلت لاحقاً رداً على تلك الرسالة، فإن الإرسال والاستقبال سيكونان مرتبطين بـ "→" في النظام الجديد ولكن ليس في القديم.

يمكن توضيح العلاقة "→" بواسطة مخطط زمكاني (space-time diagram) حيث يمثل الاتجاه الأفقي المكان (عمليات مختلفة) ويمثل الاتجاه العمودي الزمن المتزايد نحو الأعلى. تمثل النقاط على المخطط الأحداث. إذا كان a → b فإن a يظهر أسفل b. هذه هي الطريقة القياسية لتصوير الترتيب الجزئي.

**التعريف:** للأحداث a و b في العملية P، يأتي a قبل b في P، ويُرمز له بـ a ⇒_P b، إذا كان a → b ولا يوجد حدث c في P بحيث a → c و c → b.

يمكننا توسيع العلاقة "→" إلى مجموعة عشوائية من الأحداث E بتعريف E_1 → E_2 لتعني أنه توجد أحداث e_1 في E_1 و e_2 في E_2 بحيث e_1 → e_2.

---

### Translation Notes

- **Figures referenced:** Space-time diagram (conceptual, not numbered)
- **Key terms introduced:** happened before (→), concurrent, irreflexive, FIFO, space-time diagram, transitivity
- **Equations:** Mathematical notation for relations (→, ↛, ⇒_P)
- **Citations:** 0
- **Special handling:** Mathematical symbols preserved exactly; FIFO kept in English as standard technical term

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
