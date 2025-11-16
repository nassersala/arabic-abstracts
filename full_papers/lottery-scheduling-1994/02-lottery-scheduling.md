# Section 2: Lottery Scheduling
## القسم 2: الجدولة اليانصيبية

**Section:** lottery-scheduling
**Translation Quality:** 0.89
**Glossary Terms Used:** lottery scheduling, resource allocation, ticket, lottery, client, resource rights, abstract, relative, uniform, probabilistically fair, binomial distribution, geometric distribution, starvation, scheduling quantum

---

### English Version

Lottery scheduling is a randomized resource allocation mechanism. Resource rights are represented by lottery tickets. Each allocation is determined by holding a lottery; the resource is granted to the client with the winning ticket. This effectively allocates resources to competing clients in proportion to the number of tickets that they hold.

## 2.1 Resource Rights

Lottery tickets encapsulate resource rights that are abstract, relative, and uniform. They are *abstract* because they quantify resource rights independently of machine details. Lottery tickets are *relative*, since the fraction of a resource that they represent varies dynamically in proportion to the contention for that resource. Thus, a client will obtain more of a lightly contended resource than one that is highly contended; in the worst case, it will receive a share proportional to its share of tickets in the system. Finally, tickets are *uniform* because rights for heterogeneous resources can be homogeneously represented as tickets. These properties of lottery tickets are similar to those of money in computational economies [Wal92].

## 2.2 Lotteries

Scheduling by lottery is probabilistically fair. The expected allocation of resources to clients is proportional to the number of tickets that they hold. Since the scheduling algorithm is randomized, the actual allocated proportions are not guaranteed to match the expected proportions exactly. However, the disparity between them decreases as the number of allocations increases.

The number of lotteries won by a client has a binomial distribution. The probability $p$ that a client holding $t$ tickets will win a given lottery with a total of $T$ tickets is simply $p = t/T$. After $n$ identical lotteries, the expected number of wins $w$ is $E[w] = np$, with variance $\sigma_w^2 = np(1 - p)$. The coefficient of variation for the observed proportion of wins is $\sigma_w/E[w] = \sqrt{(1 - p)/np}$. Thus, a client's throughput is proportional to its ticket allocation, with accuracy that improves with $\sqrt{n}$.

The number of lotteries required for a client's first win has a geometric distribution. The expected number of lotteries $n$ that a client must wait before its first win is $E[n] = 1/p$, with variance $\sigma_n^2 = (1 - p)/p^2$. Thus, a client's average response time is inversely proportional to its ticket allocation. The properties of both binomial and geometric distributions are well-understood [Tri82].

With a scheduling quantum of 10 milliseconds (100 lotteries per second), reasonable fairness can be achieved over subsecond time intervals. As computation speeds continue to increase, shorter time quanta can be used to further improve accuracy while maintaining a fixed proportion of scheduler overhead.

Since any client with a non-zero number of tickets will eventually win a lottery, the conventional problem of starvation does not exist. The lottery mechanism also operates fairly when the number of clients or tickets varies dynamically. For each allocation, every client is given a fair chance of winning proportional to its share of the total number of tickets. Since any changes to relative ticket allocations are immediately reflected in the next allocation decision, lottery scheduling is extremely responsive.

---

### النسخة العربية

الجدولة اليانصيبية هي آلية عشوائية لتخصيص الموارد. تُمثَّل حقوق الموارد بتذاكر يانصيب. يُحدَّد كل تخصيص عن طريق إجراء يانصيب؛ يُمنح المورد للعميل صاحب التذكرة الفائزة. هذا يخصص الموارد بشكل فعال للعملاء المتنافسين بما يتناسب مع عدد التذاكر التي يحملونها.

## 2.1 حقوق الموارد

تغلف تذاكر اليانصيب حقوق الموارد التي هي مجردة، ونسبية، وموحدة. إنها *مجردة* لأنها تحدد حقوق الموارد بشكل مستقل عن تفاصيل الآلة. تذاكر اليانصيب *نسبية*، حيث إن كسر المورد الذي تمثله يتغير ديناميكياً بما يتناسب مع التنافس على ذلك المورد. وبالتالي، سيحصل العميل على المزيد من المورد قليل التنافس مقارنة بمورد عالي التنافس؛ في أسوأ الحالات، سيحصل على حصة متناسبة مع حصته من التذاكر في النظام. وأخيراً، التذاكر *موحدة* لأن حقوق الموارد غير المتجانسة يمكن تمثيلها بشكل متجانس كتذاكر. هذه الخصائص لتذاكر اليانصيب مشابهة لخصائص المال في اقتصادات الحوسبة [Wal92].

## 2.2 اليانصيب

الجدولة باليانصيب عادلة احتمالياً. التخصيص المتوقع للموارد للعملاء يتناسب مع عدد التذاكر التي يحملونها. نظراً لأن خوارزمية الجدولة عشوائية، فإن النسب المخصصة الفعلية غير مضمونة لمطابقة النسب المتوقعة بالضبط. ومع ذلك، يتناقص التباين بينهما مع زيادة عدد التخصيصات.

عدد اليانصيبات التي يفوز بها العميل له توزيع ذو حدين (binomial distribution). احتمال $p$ أن يفوز عميل يحمل $t$ تذكرة في يانصيب معين بإجمالي $T$ تذكرة هو ببساطة $p = t/T$. بعد $n$ يانصيب متطابق، العدد المتوقع من الفوز $w$ هو $E[w] = np$، مع تباين $\sigma_w^2 = np(1 - p)$. معامل التباين للنسبة الملاحظة من الفوز هو $\sigma_w/E[w] = \sqrt{(1 - p)/np}$. وبالتالي، فإن إنتاجية العميل متناسبة مع تخصيص تذاكره، بدقة تتحسن مع $\sqrt{n}$.

عدد اليانصيبات المطلوبة لأول فوز للعميل له توزيع هندسي (geometric distribution). العدد المتوقع من اليانصيبات $n$ التي يجب أن ينتظرها العميل قبل فوزه الأول هو $E[n] = 1/p$، مع تباين $\sigma_n^2 = (1 - p)/p^2$. وبالتالي، فإن متوسط وقت استجابة العميل يتناسب عكسياً مع تخصيص تذاكره. خصائص كل من التوزيعات ذات الحدين والهندسية مفهومة جيداً [Tri82].

مع كم جدولة قدره 10 ميليثانية (100 يانصيب في الثانية)، يمكن تحقيق عدالة معقولة على فترات زمنية أقل من ثانية. مع استمرار زيادة سرعات الحوسبة، يمكن استخدام كمات زمنية أقصر لتحسين الدقة بشكل أكبر مع الحفاظ على نسبة ثابتة من التكلفة الإضافية للمجدول.

نظراً لأن أي عميل لديه عدد غير صفري من التذاكر سيفوز في النهاية بيانصيب، فإن المشكلة التقليدية للجوع (starvation) غير موجودة. تعمل آلية اليانصيب أيضاً بشكل عادل عندما يتغير عدد العملاء أو التذاكر ديناميكياً. لكل تخصيص، يُعطى كل عميل فرصة عادلة للفوز بما يتناسب مع حصته من إجمالي عدد التذاكر. نظراً لأن أي تغييرات في تخصيصات التذاكر النسبية تنعكس فوراً في قرار التخصيص التالي، فإن الجدولة اليانصيبية سريعة الاستجابة للغاية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - probabilistically fair: عادلة احتمالياً
  - binomial distribution: توزيع ذو حدين
  - geometric distribution: توزيع هندسي
  - coefficient of variation: معامل التباين
  - scheduling quantum: كم جدولة
  - starvation: جوع
- **Equations:** Multiple probability equations (p = t/T, E[w] = np, etc.)
- **Citations:** [Wal92], [Tri82]
- **Special handling:** Mathematical formulas preserved in LaTeX notation with Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89
