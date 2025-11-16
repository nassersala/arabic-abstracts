# Section 4: Implementation
## القسم 4: التطبيق

**Section:** implementation
**Translation Quality:** 0.86
**Glossary Terms Used:** Mach microkernel, random number generator, Park-Miller algorithm, lottery, O(n), O(lg n), tree-based, kernel interface, currency, ticket, active, base units, scheduling quantum, move-to-front heuristic

---

### English Version

We have implemented a prototype lottery scheduler by modifying the Mach 3.0 microkernel (MK82) [Acc86, Loe92] on a 25MHz MIPS-based DECStation 5000/125. Full support is provided for ticket transfers, ticket inflation, ticket currencies, and compensation tickets. The scheduling quantum on this platform is 100 milliseconds.

## 4.1 Random Numbers

An efficient lottery scheduler requires a fast way to generate uniformly-distributed random numbers. We have implemented a pseudo-random number generator based on the Park-Miller algorithm [Par88, Car90] that executes in approximately 10 RISC instructions. Our assembly-language implementation is listed in Appendix A.

## 4.2 Lotteries

A straightforward way to implement a centralized lottery scheduler is to randomly select a winning ticket, and then search a list of clients to locate the client holding that ticket. This requires a random number generation and $O(n)$ operations to traverse a client list of length $n$, accumulating a running ticket sum until it reaches the winning value. An example list-based lottery is presented in Figure 1.

Various optimizations can reduce the average number of clients that must be examined. For example, if the distribution of tickets to clients is uneven, ordering the clients by decreasing ticket counts can substantially reduce the average search length. Since those clients with the largest number of tickets will be selected most frequently, a simple "move to front" heuristic can be very effective.

For large $n$, a more efficient implementation is to use a tree of partial ticket sums, with clients at the leaves. To locate the client holding a winning ticket, the tree is traversed starting at the root node, and ending with the winning client leaf node, requiring only $O(\lg n)$ operations. Such a tree-based implementation can also be used as the basis of a distributed lottery scheduler.

## 4.3 Mach Kernel Interface

The kernel representation of tickets and currencies is depicted in Figure 2. A minimal lottery scheduling interface is exported by the microkernel. It consists of operations to create and destroy tickets and currencies, operations to fund and unfund a currency (by adding or removing a ticket from its list of backing tickets), and operations to compute the current value of tickets and currencies in base units.

Our lottery scheduling policy co-exists with the standard timesharing and fixed-priority policies. A few high-priority threads (such as the Ethernet driver) created by the Unix server (UX41) remain at their original fixed priorities.

## 4.4 Ticket Currencies

Our prototype uses a simple scheme to convert ticket amounts into base units. Each currency maintains an *active amount* sum for all of its issued tickets. A ticket is *active* while it is being used by a thread to compete in a lottery. When a thread is removed from the run queue, its tickets are deactivated; they are reactivated when the thread rejoins the run queue. If a ticket deactivation changes a currency's active amount to zero, the deactivation propagates to each of its backing tickets. Similarly, if a ticket activation changes a currency's active amount from zero, the activation propagates to each of its backing tickets.

A currency's value is computed by summing the value of its backing tickets. A ticket's value is computed by multiplying the value of the currency in which it is denominated by its share of the active amount issued in that currency. The value of a ticket denominated in the base currency is defined to be its face value amount. An example currency graph with base value conversions is presented in Figure 3. Currency conversions can be accelerated by caching values or exchange rates, although this is not implemented in our prototype.

Our scheduler uses the simple list-based lottery with a move-to-front heuristic, as described earlier in Section 4.2. To handle multiple currencies, a winning ticket value is selected by generating a random number between zero and the total number of active tickets in the base currency. The run queue is then traversed as described earlier, except that the running ticket sum accumulates the value of each thread's currency in base units until the winning value is reached.

## 4.5 Compensation Tickets

As discussed in Section 3.4, a thread which consumes only a fraction $f$ of its allocated time quantum is automatically granted a compensation ticket that inflates its value by $1/f$ until the thread starts its next quantum. This is consistent with proportional sharing, and permits I/O-bound tasks that use few processor cycles to start quickly.

For example, suppose threads A and B each hold tickets valued at 400 base units. Thread A always consumes its entire 100 millisecond time quantum, while thread B uses only 20 milliseconds before yielding the processor. Since both A and B have equal funding, they are equally likely to win a lottery when both compete for the processor. However, thread B uses only $f = 1/5$ of its allocated time, allowing thread A to consume five times as much CPU, in violation of their 1:1 allocation ratio. To remedy this situation, thread B is granted a compensation ticket valued at 1600 base units when it yields the processor. When B next competes for the processor, its total funding will be $400/f = 2000$ base units. Thus, on average B will win the processor lottery five times as often as A, each time consuming $1/5$ as much of its quantum as A, achieving the desired 1:1 allocation ratio.

## 4.6 Ticket Transfers

The mach_msg system call was modified to temporarily transfer tickets from client to server for synchronous RPCs. This automatically redirects resource rights from a blocked client to the server computing on its behalf. A transfer is implemented by creating a new ticket denominated in the client's currency, and using it to fund the server's currency. If the server thread is already waiting when mach_msg performs a synchronous call, it is immediately funded with the transfer ticket. If no server thread is waiting, then the transfer ticket is placed on a list that is checked by the server thread when it attempts to receive the call message. During a reply, the transfer ticket is simply destroyed.

## 4.7 User Interface

Currencies and tickets can be manipulated via a command-line interface. User-level commands exist to create and destroy tickets and currencies (mktkt, rmtkt, mkcur, rmcur), fund and unfund currencies (fund, unfund), obtain information (lstkt, lscur), and to execute a shell command with specified funding (fundx). Since the Mach microkernel has no concept of user and we did not modify the Unix server, these commands are setuid root. A complete lottery scheduling system should protect currencies by using access control lists or Unix-style permissions based on user and group membership.

---

### النسخة العربية

لقد طبقنا نموذجاً أولياً لمجدول يانصيبي عن طريق تعديل نواة ماخ 3.0 الدقيقة (MK82) [Acc86, Loe92] على جهاز DECStation 5000/125 بمعالج MIPS بتردد 25 ميجاهرتز. يتم توفير دعم كامل لنقل التذاكر، وتضخم التذاكر، وعملات التذاكر، وتذاكر التعويض. كم الجدولة على هذه المنصة هو 100 ميليثانية.

## 4.1 الأعداد العشوائية

يتطلب المجدول اليانصيبي الفعال طريقة سريعة لتوليد أعداد عشوائية موزعة بشكل موحد. لقد طبقنا مولد أعداد شبه عشوائية يعتمد على خوارزمية بارك-ميلر [Par88, Car90] التي تُنفذ في حوالي 10 تعليمات RISC. تطبيقنا بلغة التجميع مدرج في الملحق أ.

## 4.2 اليانصيبات

طريقة مباشرة لتطبيق مجدول يانصيبي مركزي هي اختيار تذكرة فائزة عشوائياً، ثم البحث في قائمة العملاء لتحديد موقع العميل الذي يحمل تلك التذكرة. يتطلب هذا توليد عدد عشوائي وعمليات $O(n)$ لاجتياز قائمة عملاء بطول $n$، مع تراكم مجموع تذاكر جارٍ حتى يصل إلى القيمة الفائزة. يُقدم مثال على يانصيب قائم على قائمة في الشكل 1.

يمكن لتحسينات مختلفة تقليل متوسط عدد العملاء الذين يجب فحصهم. على سبيل المثال، إذا كان توزيع التذاكر على العملاء غير متساوٍ، فإن ترتيب العملاء حسب عدد التذاكر المتناقص يمكن أن يقلل بشكل كبير من متوسط طول البحث. نظراً لأن العملاء الذين لديهم أكبر عدد من التذاكر سيتم اختيارهم بشكل أكثر تكراراً، فإن استدلالية بسيطة "للنقل إلى المقدمة" يمكن أن تكون فعالة جداً.

بالنسبة لـ $n$ الكبيرة، فإن التطبيق الأكثر كفاءة هو استخدام شجرة من مجاميع التذاكر الجزئية، مع العملاء في الأوراق. لتحديد موقع العميل الذي يحمل تذكرة فائزة، يتم اجتياز الشجرة بدءاً من العقدة الجذر، وانتهاءً بعقدة ورقة العميل الفائز، مما يتطلب عمليات $O(\lg n)$ فقط. يمكن أيضاً استخدام مثل هذا التطبيق القائم على الشجرة كأساس لمجدول يانصيبي موزع.

## 4.3 واجهة نواة ماخ

يُصور تمثيل النواة للتذاكر والعملات في الشكل 2. تُصدر النواة الدقيقة واجهة جدولة يانصيبية بسيطة. تتكون من عمليات لإنشاء وتدمير التذاكر والعملات، وعمليات لتمويل وإلغاء تمويل عملة (عن طريق إضافة أو إزالة تذكرة من قائمة تذاكر الدعم الخاصة بها)، وعمليات لحساب القيمة الحالية للتذاكر والعملات بالوحدات الأساسية.

تتعايش سياسة الجدولة اليانصيبية الخاصة بنا مع سياسات المشاركة الزمنية القياسية والأولوية الثابتة. تظل بعض الخيوط عالية الأولوية (مثل مشغل Ethernet) التي أنشأها خادم Unix (UX41) في أولوياتها الثابتة الأصلية.

## 4.4 عملات التذاكر

يستخدم نموذجنا الأولي مخططاً بسيطاً لتحويل كميات التذاكر إلى وحدات أساسية. تحافظ كل عملة على مجموع *كمية نشطة* لجميع تذاكرها الصادرة. التذكرة *نشطة* بينما يستخدمها خيط للتنافس في يانصيب. عندما يُزال خيط من قائمة التشغيل، يتم إلغاء تنشيط تذاكره؛ ويعاد تنشيطها عندما ينضم الخيط مرة أخرى إلى قائمة التشغيل. إذا غيّر إلغاء تنشيط تذكرة الكمية النشطة لعملة إلى صفر، ينتشر إلغاء التنشيط إلى كل من تذاكر الدعم الخاصة بها. وبالمثل، إذا غيّر تنشيط تذكرة الكمية النشطة لعملة من صفر، ينتشر التنشيط إلى كل من تذاكر الدعم الخاصة بها.

تُحسب قيمة العملة بجمع قيمة تذاكر الدعم الخاصة بها. تُحسب قيمة التذكرة بضرب قيمة العملة التي سُميت بها في حصتها من الكمية النشطة الصادرة بتلك العملة. قيمة التذكرة المسماة بالعملة الأساسية محددة لتكون قيمتها الاسمية. يُقدم مثال على رسم بياني للعملات مع تحويلات القيمة الأساسية في الشكل 3. يمكن تسريع تحويلات العملات عن طريق تخزين القيم أو أسعار الصرف مؤقتاً، على الرغم من أن هذا غير مطبق في نموذجنا الأولي.

يستخدم مجدولنا اليانصيب البسيط القائم على القائمة مع استدلالية النقل إلى المقدمة، كما هو موضح سابقاً في القسم 4.2. للتعامل مع عملات متعددة، يتم اختيار قيمة تذكرة فائزة عن طريق توليد عدد عشوائي بين صفر وإجمالي عدد التذاكر النشطة بالعملة الأساسية. يتم بعد ذلك اجتياز قائمة التشغيل كما هو موضح سابقاً، باستثناء أن مجموع التذاكر الجاري يراكم قيمة عملة كل خيط بالوحدات الأساسية حتى يتم الوصول إلى القيمة الفائزة.

## 4.5 تذاكر التعويض

كما نوقش في القسم 3.4، يُمنح خيط يستهلك فقط كسراً $f$ من كمه الزمني المخصص تلقائياً تذكرة تعويض تضخم قيمته بمقدار $1/f$ حتى يبدأ الخيط كمه التالي. هذا متسق مع المشاركة النسبية، ويسمح للمهام المقيدة بالإدخال/الإخراج التي تستخدم دورات معالج قليلة بالبدء بسرعة.

على سبيل المثال، افترض أن الخيوط A و B يحمل كل منهما تذاكر بقيمة 400 وحدة أساسية. الخيط A يستهلك دائماً كمه الزمني الكامل البالغ 100 ميليثانية، بينما يستخدم الخيط B 20 ميليثانية فقط قبل التنازل عن المعالج. نظراً لأن كلاً من A و B لديهما تمويل متساوٍ، فمن المحتمل بنفس القدر أن يفوزا بيانصيب عندما يتنافس كلاهما على المعالج. ومع ذلك، يستخدم الخيط B فقط $f = 1/5$ من وقته المخصص، مما يسمح للخيط A باستهلاك خمسة أضعاف من المعالج، في انتهاك لنسبة التخصيص 1:1 الخاصة بهما. لمعالجة هذا الوضع، يُمنح الخيط B تذكرة تعويض بقيمة 1600 وحدة أساسية عندما يتنازل عن المعالج. عندما يتنافس B في المرة التالية على المعالج، سيكون إجمالي تمويله $400/f = 2000$ وحدة أساسية. وبالتالي، في المتوسط سيفوز B بيانصيب المعالج خمس مرات أكثر من A، وفي كل مرة يستهلك $1/5$ من كمه مثل A، محققاً نسبة التخصيص المطلوبة 1:1.

## 4.6 نقل التذاكر

تم تعديل استدعاء النظام mach_msg لنقل التذاكر مؤقتاً من العميل إلى الخادم للاستدعاءات الإجرائية البعيدة المتزامنة. هذا يعيد توجيه حقوق الموارد تلقائياً من عميل محظور إلى الخادم الذي يحسب نيابة عنه. يُطبق النقل عن طريق إنشاء تذكرة جديدة مسماة بعملة العميل، واستخدامها لتمويل عملة الخادم. إذا كان خيط الخادم ينتظر بالفعل عندما يُجري mach_msg استدعاءً متزامناً، يتم تمويله فوراً بتذكرة النقل. إذا لم يكن خيط الخادم ينتظر، فإن تذكرة النقل توضع في قائمة يفحصها خيط الخادم عندما يحاول استقبال رسالة الاستدعاء. أثناء الرد، يتم ببساطة تدمير تذكرة النقل.

## 4.7 واجهة المستخدم

يمكن التعامل مع العملات والتذاكر عبر واجهة سطر أوامر. توجد أوامر على مستوى المستخدم لإنشاء وتدمير التذاكر والعملات (mktkt, rmtkt, mkcur, rmcur)، وتمويل وإلغاء تمويل العملات (fund, unfund)، والحصول على معلومات (lstkt, lscur)، ولتنفيذ أمر شل بتمويل محدد (fundx). نظراً لأن نواة ماخ الدقيقة ليس لديها مفهوم المستخدم ولم نعدل خادم Unix، فإن هذه الأوامر هي setuid root. يجب أن يحمي نظام جدولة يانصيبية كامل العملات باستخدام قوائم التحكم في الوصول أو الأذونات بنمط Unix بناءً على عضوية المستخدم والمجموعة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Example Lottery), Figure 2 (Kernel Objects), Figure 3 (Example Currency Graph)
- **Key terms introduced:**
  - Park-Miller algorithm: خوارزمية بارك-ميلر
  - move-to-front heuristic: استدلالية النقل إلى المقدمة
  - active amount: كمية نشطة
  - backing tickets: تذاكر الدعم
  - base units: وحدات أساسية
  - setuid root: setuid root (kept as is - technical term)
- **Equations:** O(n), O(lg n), mathematical expressions for compensation
- **Citations:** [Acc86, Loe92], [Par88, Car90]
- **Special handling:** Command names (mktkt, rmtkt, etc.) kept in English as they are code

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
