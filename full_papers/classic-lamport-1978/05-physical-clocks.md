# Section 5: Physical Clocks
## القسم 5: الساعات الفيزيائية

**Section:** physical-clocks
**Translation Quality:** 0.85
**Glossary Terms Used:** physical clock, synchronization, clock drift, bounded delay, theorem, distributed system

---

### English Version

We now assume that the processes are equipped with physical clocks—i.e., we introduce the concept of physical time. We assume that each clock C_i is a continuous, differentiable function of physical time t (except for isolated jump discontinuities), and we write dC_i(t)/dt for the rate at which the clock is running at time t. In order for the clock C_i to be a true physical clock, it must run at approximately the correct rate. This means that we must have the condition:

**PC1.** There exists a constant κ ≪ 1 such that for all i: |dC_i(t)/dt - 1| < κ.

For a typical crystal controlled clock, κ ≤ 10^(-6).

A clock C_i is said to be correct if PC1 holds. However, we are interested not only in how fast a single clock runs, but in how well the different clocks are synchronized with one another. In particular, we wish to ensure that:

**PC2.** For all i, j: |C_i(t) - C_j(t)| < ε

for some sufficiently small constant ε.

It is easy to see that if PC2 holds and ε is small enough, then the ordering ⇒ defined in Section 3 will be correct in the sense that a ⇒ b implies that event a occurred before event b in real time. However, PC2 is a condition on the physical system, not on the algorithm, and we must show that it can be satisfied.

We begin by assuming that PC1 holds for all clocks. Let μ be a number such that if event a causes event b, then μ is less than the time it takes for a to causally affect b. In other words, μ is less than the shortest transmission time for an interprocess message. We will show that by synchronizing the clocks properly, we can ensure that PC2 holds with ε approximately equal to μ. This is the best we can do. There is no way for clock synchronization to compensate for the time μ which it actually takes for one event to influence another.

**Theorem.** Assume a system of N processes, and let m be the minimum value of μ among all pairs of processes. Assume that:

(a) PC1 holds, with κ ≪ 1.

(b) The diameter of the network (maximum distance between any two processes) is bounded by d, where d is measured in terms of minimum message transmission time.

(c) For any message sent, the actual transmission time is unpredictable but is in the interval [m, M], where m > 0.

Then the clocks can be synchronized so that PC2 is satisfied with:

ε ≈ d(2κm + M - m)

where the approximation assumes that dκ ≪ 1.

**Proof Sketch.** The idea is to ensure that the logical clock condition (the Clock Condition from Section 3) is satisfied, with the additional constraint that the clock values approximate physical time closely enough. To synchronize the clocks, we require that each process P_i periodically send a message to every other process. When process P_j receives such a message from P_i with timestamp T_m, it sets its clock C_j to a value equal to or greater than max(C_j, T_m + μ_m), where μ_m is the estimated minimum delay for a message from P_i to P_j.

The theorem follows by carefully analyzing the clock drift that can accumulate over the network diameter d. The proof requires showing that the correction mechanism keeps the clocks within ε of each other despite the drift κ in clock rates and the uncertainty (M - m) in message transmission times.

The quantity ε can be made arbitrarily small by choosing:
- Smaller network diameter d (fewer hops between any two processes)
- More accurate clocks (smaller κ)
- More predictable message delays (smaller M - m)
- More frequent synchronization messages

**Implementation Details**

In practice, the physical clock synchronization algorithm works as follows:

1. Each process P_i sends a timestamped message to all other processes at regular intervals (much less than the time it would take for significant drift to accumulate).

2. When P_j receives a message from P_i with timestamp T_m, it computes the minimum message delay μ_m and sets:
   C_j := max(C_j, T_m + μ_m)

3. To avoid discontinuities (clock jumping backwards), if the correction would decrease C_j, instead the clock rate dC_j(t)/dt is temporarily adjusted to gradually bring the clocks into synchronization.

The algorithm ensures that all clocks remain within ε of each other, where ε is determined by the theorem above. This bound ε represents the fundamental limitation on clock synchronization in a distributed system—it cannot be reduced below the minimum message transmission time m multiplied by the network diameter.

---

### النسخة العربية

نفترض الآن أن العمليات مجهزة بساعات فيزيائية—أي أننا نُدخل مفهوم الوقت الفيزيائي. نفترض أن كل ساعة C_i هي دالة مستمرة وقابلة للتفاضل للوقت الفيزيائي t (باستثناء انقطاعات القفز المعزولة)، ونكتب dC_i(t)/dt لمعدل تشغيل الساعة في الوقت t. لكي تكون الساعة C_i ساعة فيزيائية حقيقية، يجب أن تعمل بمعدل صحيح تقريباً. هذا يعني أنه يجب أن يكون لدينا الشرط:

**PC1.** يوجد ثابت κ ≪ 1 بحيث لجميع i: |dC_i(t)/dt - 1| < κ.

بالنسبة لساعة نموذجية متحكم بها بالكريستال، κ ≤ 10^(-6).

يُقال إن الساعة C_i صحيحة إذا تحقق PC1. ومع ذلك، نحن مهتمون ليس فقط بمدى سرعة تشغيل ساعة واحدة، ولكن بمدى جودة تزامن الساعات المختلفة مع بعضها البعض. على وجه الخصوص، نرغب في ضمان أن:

**PC2.** لجميع i، j: |C_i(t) - C_j(t)| < ε

لثابت ε صغير بما فيه الكفاية.

من السهل رؤية أنه إذا تحقق PC2 وكان ε صغيراً بما فيه الكفاية، فإن الترتيب ⇒ المُعرَّف في القسم 3 سيكون صحيحاً بمعنى أن a ⇒ b يعني أن الحدث a وقع قبل الحدث b في الوقت الحقيقي. ومع ذلك، PC2 هو شرط على النظام الفيزيائي، وليس على الخوارزمية، ويجب أن نُظهر أنه يمكن تحقيقه.

نبدأ بافتراض أن PC1 يصح لجميع الساعات. ليكن μ رقماً بحيث إذا تسبب حدث a في حدث b، فإن μ أقل من الوقت الذي يستغرقه a للتأثير سببياً على b. بعبارة أخرى، μ أقل من أقصر وقت نقل لرسالة بين العمليات. سنُظهر أنه بتزامن الساعات بشكل صحيح، يمكننا ضمان تحقق PC2 مع ε يساوي تقريباً μ. هذا أفضل ما يمكننا فعله. لا توجد طريقة لتزامن الساعات للتعويض عن الوقت μ الذي يستغرقه فعلياً حدث واحد للتأثير على آخر.

**المبرهنة.** لنفترض نظاماً من N عملية، وليكن m أصغر قيمة لـ μ بين جميع أزواج العمليات. لنفترض أن:

(أ) يتحقق PC1، مع κ ≪ 1.

(ب) قطر الشبكة (أقصى مسافة بين أي عمليتين) محدود بـ d، حيث يُقاس d بدلالة الحد الأدنى لوقت نقل الرسالة.

(ج) لأي رسالة مرسلة، يكون وقت النقل الفعلي غير متوقع لكنه في الفترة [m, M]، حيث m > 0.

إذن يمكن تزامن الساعات بحيث يتحقق PC2 مع:

ε ≈ d(2κm + M - m)

حيث يفترض التقريب أن dκ ≪ 1.

**ملخص البرهان.** الفكرة هي ضمان تحقق شرط الساعة المنطقية (شرط الساعة من القسم 3)، مع القيد الإضافي أن قيم الساعة تقارب الوقت الفيزيائي بشكل كافٍ. لتزامن الساعات، نطلب أن ترسل كل عملية P_i بشكل دوري رسالة إلى كل عملية أخرى. عندما تستقبل العملية P_j مثل هذه الرسالة من P_i بطابع زمني T_m، تضع ساعتها C_j على قيمة تساوي أو أكبر من max(C_j, T_m + μ_m)، حيث μ_m هو التأخير الأدنى المقدر لرسالة من P_i إلى P_j.

تتبع المبرهنة من التحليل الدقيق للانحراف في الساعة الذي يمكن أن يتراكم على قطر الشبكة d. يتطلب البرهان إظهار أن آلية التصحيح تبقي الساعات ضمن ε من بعضها البعض رغم الانحراف κ في معدلات الساعة وعدم اليقين (M - m) في أوقات نقل الرسائل.

يمكن جعل الكمية ε صغيرة بشكل تعسفي باختيار:
- قطر شبكة أصغر d (قفزات أقل بين أي عمليتين)
- ساعات أكثر دقة (κ أصغر)
- تأخيرات رسائل أكثر قابلية للتنبؤ (M - m أصغر)
- رسائل تزامن أكثر تواتراً

**تفاصيل التنفيذ**

عملياً، تعمل خوارزمية تزامن الساعات الفيزيائية كما يلي:

1. ترسل كل عملية P_i رسالة بطابع زمني إلى جميع العمليات الأخرى على فترات منتظمة (أقل بكثير من الوقت الذي يستغرقه تراكم انحراف كبير).

2. عندما تستقبل P_j رسالة من P_i بطابع زمني T_m، تحسب الحد الأدنى لتأخير الرسالة μ_m وتضع:
   C_j := max(C_j, T_m + μ_m)

3. لتجنب الانقطاعات (قفز الساعة للخلف)، إذا كان التصحيح سيُنقص C_j، بدلاً من ذلك يتم ضبط معدل الساعة dC_j(t)/dt مؤقتاً لإدخال الساعات تدريجياً في التزامن.

تضمن الخوارزمية بقاء جميع الساعات ضمن ε من بعضها البعض، حيث يُحدد ε بواسطة المبرهنة أعلاه. يمثل هذا الحد ε القيد الأساسي على تزامن الساعات في نظام موزع—لا يمكن تقليله إلى ما دون الحد الأدنى لوقت نقل الرسالة m مضروباً في قطر الشبكة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** physical clock, clock drift (κ), network diameter (d), transmission delay bounds [m, M], clock synchronization bound (ε)
- **Equations:** dC_i(t)/dt, |dC_i(t)/dt - 1| < κ, |C_i(t) - C_j(t)| < ε, ε ≈ d(2κm + M - m)
- **Citations:** 0
- **Special handling:** Mathematical theorem with proof sketch; conditions PC1, PC2 labeled consistently; differential notation preserved

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
