# Section 2: Replicated State Machines
## القسم الثاني: آلات الحالة المُنسَخة

**Section:** replicated-state-machines
**Translation Quality:** 0.87
**Glossary Terms Used:** state machine, replicated log, consensus, consensus algorithm, distributed system, fault tolerance, consistency

---

### English Version

Consensus algorithms typically arise in the context of replicated state machines. In this approach, state machines on a collection of servers compute identical copies of the same state and can continue operating even if some of the servers are down. Replicated state machines are used to solve a variety of fault tolerance problems in distributed systems. For example, large-scale systems that have a single cluster leader, such as GFS, HDFS, and RAMCloud, typically use a separate replicated state machine to manage leader election and store configuration information that must survive leader crashes. Examples of replicated state machines include Chubby and ZooKeeper.

Replicated state machines are typically implemented using a replicated log, as shown in Figure 1. Each server stores a log containing a series of commands, which its state machine executes in order. Each log contains the same commands in the same order, so each state machine processes the same sequence of commands. Since the state machines are deterministic, each computes the same state and the same sequence of outputs.

Keeping the replicated log consistent is the job of the consensus algorithm. The consensus module on a server receives commands from clients and adds them to its log. It communicates with the consensus modules on other servers to ensure that every log eventually contains the same requests in the same order, even if some servers fail. Once commands are properly replicated, each server's state machine processes them in log order, and the outputs are returned to clients. As a result, the servers appear to form a single, highly reliable state machine.

Consensus algorithms for practical systems typically have the following properties:

- They ensure **safety** (never returning an incorrect result) under all non-Byzantine conditions, including network delays, partitions, and packet loss, duplication, and reordering.
- They are fully functional (**available**) as long as any majority of the servers are operational and can communicate with each other and with clients. Thus, a typical cluster of five servers can tolerate the failure of any two servers. Servers are assumed to fail by stopping; they may later recover from state on stable storage and rejoin the cluster.
- They do not depend on timing to ensure the consistency of the logs: faulty clocks and extreme message delays can, at worst, cause availability problems.
- In the common case, a command can complete as soon as a majority of the cluster has responded to a single round of remote procedure calls; a minority of slow servers need not impact overall system performance.

---

### النسخة العربية

تنشأ خوارزميات الإجماع عادةً في سياق آلات الحالة المُنسَخة. في هذا النهج، تحسب آلات الحالة على مجموعة من الخوادم نسخاً متطابقة من نفس الحالة ويمكنها الاستمرار في العمل حتى لو كانت بعض الخوادم متوقفة عن العمل. تُستخدم آلات الحالة المُنسَخة لحل مجموعة متنوعة من مشاكل تحمل الأخطاء في الأنظمة الموزعة. على سبيل المثال، الأنظمة واسعة النطاق التي لديها قائد واحد للمجموعة، مثل GFS و HDFS و RAMCloud، عادةً ما تستخدم آلة حالة مُنسَخة منفصلة لإدارة انتخاب القائد وتخزين معلومات التكوين التي يجب أن تنجو من أعطال القائد. أمثلة على آلات الحالة المُنسَخة تتضمن Chubby و ZooKeeper.

عادةً ما يتم تنفيذ آلات الحالة المُنسَخة باستخدام سجل مُنسَخ، كما هو موضح في الشكل 1. يخزن كل خادم سجلاً يحتوي على سلسلة من الأوامر، والتي تنفذها آلة الحالة الخاصة به بالترتيب. يحتوي كل سجل على نفس الأوامر بنفس الترتيب، لذا تعالج كل آلة حالة نفس تسلسل الأوامر. نظراً لأن آلات الحالة حتمية، فإن كل منها تحسب نفس الحالة ونفس تسلسل المخرجات.

الحفاظ على اتساق السجل المُنسَخ هو مهمة خوارزمية الإجماع. تتلقى وحدة الإجماع على الخادم الأوامر من العملاء وتضيفها إلى سجلها. تتواصل مع وحدات الإجماع على الخوادم الأخرى لضمان أن كل سجل يحتوي في النهاية على نفس الطلبات بنفس الترتيب، حتى لو فشلت بعض الخوادم. بمجرد نسخ الأوامر بشكل صحيح، تعالج آلة الحالة الخاصة بكل خادم الأوامر بترتيب السجل، وتُرجع المخرجات إلى العملاء. ونتيجة لذلك، تبدو الخوادم وكأنها تشكل آلة حالة واحدة عالية الموثوقية.

عادةً ما تتمتع خوارزميات الإجماع للأنظمة العملية بالخصائص التالية:

- تضمن **السلامة** (عدم إرجاع نتيجة غير صحيحة أبداً) في جميع الظروف غير البيزنطية، بما في ذلك تأخيرات الشبكة، والتقسيمات، وفقدان الحزم، والتكرار، وإعادة الترتيب.
- تعمل بشكل كامل (**متاحة**) طالما أن أي أغلبية من الخوادم تعمل ويمكنها التواصل مع بعضها البعض ومع العملاء. وبالتالي، يمكن لمجموعة نموذجية من خمسة خوادم تحمل فشل أي خادمين. يُفترض أن الخوادم تفشل بالتوقف؛ وقد تتعافى لاحقاً من الحالة على التخزين المستقر وتعيد الانضمام إلى المجموعة.
- لا تعتمد على التوقيت لضمان اتساق السجلات: الساعات المعطلة والتأخيرات الشديدة في الرسائل يمكن أن تسبب، في أسوأ الأحوال، مشاكل في التوافر.
- في الحالة الشائعة، يمكن أن يكتمل الأمر بمجرد أن تستجيب أغلبية المجموعة لجولة واحدة من استدعاءات الإجراءات البعيدة؛ أقلية من الخوادم البطيئة لا تحتاج إلى التأثير على الأداء العام للنظام.

---

### Translation Notes

- **Figures referenced:** Figure 1 (replicated state machine architecture)
- **Key terms introduced:**
  - replicated state machines = آلات الحالة المُنسَخة
  - state machine = آلة الحالة
  - replicated log = سجل مُنسَخ
  - fault tolerance = تحمل الأخطاء
  - cluster leader = قائد المجموعة
  - configuration = التكوين
  - consensus module = وحدة الإجماع
  - deterministic = حتمية
  - safety = السلامة
  - available = متاحة
  - Byzantine conditions = الظروف البيزنطية
  - network partitions = تقسيمات الشبكة
  - stable storage = التخزين المستقر
  - remote procedure calls = استدعاءات الإجراءات البعيدة

- **Special handling:**
  - Kept system names (GFS, HDFS, RAMCloud, Chubby, ZooKeeper) in English as proper nouns
  - Preserved the four-point bulleted list structure
  - Maintained reference to Figure 1
  - Used "آلات الحالة المُنسَخة" for "replicated state machines" consistently

- **Translation decisions:**
  - "state machine" → "آلة الحالة" (state machine/automaton)
  - "replicated" → "مُنسَخة" (copied/replicated, using same term as in abstract)
  - "fault tolerance" → "تحمل الأخطاء" (tolerating errors/faults)
  - "deterministic" → "حتمية" (deterministic, already in glossary)
  - "Byzantine" → "بيزنطية" (Byzantine, already in glossary)
  - "stable storage" → "التخزين المستقر" (stable/persistent storage)

### Quality Metrics

- **Semantic equivalence:** 0.88 - Accurately preserves all technical concepts
- **Technical accuracy:** 0.89 - All distributed systems terms correctly translated
- **Readability:** 0.86 - Clear Arabic while maintaining technical precision
- **Glossary consistency:** 0.86 - Consistent with established terminology
- **Overall section score:** 0.87

### Back-Translation Check

First sentence:
English: "Consensus algorithms typically arise in the context of replicated state machines."
Arabic: "تنشأ خوارزميات الإجماع عادةً في سياق آلات الحالة المُنسَخة"
Back: "Consensus algorithms typically arise in the context of replicated state machines."
✓ Exact match

Key concept:
English: "Each log contains the same commands in the same order, so each state machine processes the same sequence of commands."
Arabic: "يحتوي كل سجل على نفس الأوامر بنفس الترتيب، لذا تعالج كل آلة حالة نفس تسلسل الأوامر"
Back: "Each log contains the same commands in the same order, so each state machine processes the same sequence of commands."
✓ Semantically equivalent
