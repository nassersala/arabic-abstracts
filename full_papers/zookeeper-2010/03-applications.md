# Section 3: ZooKeeper Applications
## القسم 3: تطبيقات زوكيبر

**Section:** applications
**Translation Quality:** 0.89
**Glossary Terms Used:** coordination, distributed system, lock, synchronization, consensus, configuration, leader election

---

### English Version

In this section we show how to use the ZooKeeper API to implement more powerful primitives. The ZooKeeper service knows nothing about these more powerful primitives since they are entirely implemented at the client using the ZooKeeper client API. Some common primitives that we discuss in this section are specific instances of more general techniques used for implementing different coordination problems with ZooKeeper. The use of ZooKeeper in critical applications motivated us to implement a Java library of such primitives with thoroughly tested implementations so that developers do not need to implement their own.

#### 3.1 Configuration Management

ZooKeeper can be used to implement dynamic configuration in a distributed application in its simplest form. Configuration is stored in a znode, zc, and processes start up with the full pathname of zc. Starting processes obtain their configuration by reading zc with the watch flag set to true. If the configuration in zc is ever updated, the processes are notified and read the new configuration, again setting the watch flag to true.

Note that in this scheme, as in most others that use watches, watches are used to make sure that a process has the most recent information. For example, if a process watching zc learns that the value of zc has changed, the new value the process reads may not be the one that caused the watch event. It is important that processes should have the most recent configuration information, if configuration data can change rather than once; it is less important to know of every change. More formally, this schema guarantees that eventually a reading process gets the latest configuration value (assuming configurations are set more slowly than the time required by notification plus a read operation).

#### 3.2 Rendezvous

Sometimes in distributed systems, it is not always clear a priori what the final system configuration will be. For example, a client may want to start a master process and several worker processes, but the starting processes is done by a scheduler, so the client does not know ahead of time information such as address and port that it will use to communicate with them.

We handle this scenario with ZooKeeper using a rendezvous znode, zr, which is an node created by the client. The client passes the full pathname of zr as a startup parameter of the master and worker processes. When the master starts it fills in zr with information about addresses and ports it is using. When workers start, they read zr with watch set to true. If zr has not been filled in yet, the worker waits to be notified when zr is updated. If zr is a ephemeral node, master and worker processes can watch for zr to be deleted and clean themselves up when the client ends.

#### 3.3 Group Membership

We take advantage of ephemeral nodes to implement group membership. Specifically, we use the fact that ephemeral nodes allow us to see the state of the session that created the node. We start by designating a znode, zg to represent the group. When a process member of the group starts, it creates an ephemeral child znode under zg. If each process has a unique name or identifier, then that name is used as the name of the child znode; otherwise, the process creates the znode with the SEQUENTIAL flag to obtain a unique name assignment. Processes may put process information in the data of the child znode, addresses and ports used by the process, for example.

After the child znode is created under zg the process normally does not need to do anything else. If the process fails or ends, the znode that represents it under zg is automatically removed.

Processes can obtain group information by simply listing the children of zg. If a process wants to monitor changes in group membership, the process can set the watch flag to true and refresh the group information (always setting the watch flag to true) when change notifications are received.

#### 3.4 Simple Locks

Although ZooKeeper is not a lock service, it can be used to implement locks. Applications using ZooKeeper generally do not use it in this way since the applications generally use the ordering and watch mechanisms of ZooKeeper to implement application-specific synchronization primitives. Here we show how locks can be implemented directly using ZooKeeper to show that it can implement a wide variety of general synchronization primitives.

The simplest lock implementation uses "lock files". The lock is represented by a znode. To acquire a lock, a client tries to create the designated znode with the EPHEMERAL flag. If the create succeeds, the client holds the lock. Otherwise, the client can read the znode with the watch flag set to be notified if the current leader dies. A client releases the lock when it dies or explicitly deletes the znode. Other clients that are waiting for a lock try again to acquire a lock once they observe the znode being deleted.

While this simple locking protocol works, it does have some problems. First, it suffers from the herd effect. If there are many clients waiting to acquire a lock, they will all vie for the lock when it is released even though only one client can acquire the lock. Second, it only implements exclusive locking. The following two primitives show how both of these problems can be overcome.

#### 3.5 Simple Locks without Herd Effect

We define a lock znode l to implement such locks. Intuitively we line up all the clients requesting the lock and each client obtains the lock in order of request arrival. Thus, clients wishing to obtain the lock do the following:

```
Lock
1. n = create(l + "/lock-", EPHEMERAL|SEQUENTIAL)
2. C = getChildren(l, false)
3. if n is lowest znode in C, exit
4. p = znode in C ordered just before n
5. if exists(p, true) wait for watch event
6. goto 2
```

```
Unlock
1. delete(n)
```

The use of the SEQUENTIAL flag in line 1 of the locking protocol orders client lock requests with respect to each other. If the client's znode has the lowest sequence number at line 3, the client holds the lock. Otherwise, the client waits for deletion of the znode that either has the lock or will receive the lock before the client in question. By only watching the znode that precedes the client's znode, we avoid the herd effect by only waking up one process when a lock is released or a lock request is abandoned. Once the client is notified that the previous znode has been deleted, the client must check if it now holds the lock. (The previous lock request may have been abandoned and there may be other clients with earlier sequence numbers still waiting for, or holding, the lock.)

#### 3.6 Read/Write Locks

To implement read/write locks, we change the lock procedure slightly, and we have separate read lock and write lock procedures.

```
Write Lock
1. n = create(l + "/write-", EPHEMERAL|SEQUENTIAL)
2. C = getChildren(l, false)
3. if n is lowest znode in C, exit
4. p = znode in C ordered just before n
5. if exists(p, true) wait for event
6. goto 2
```

```
Read Lock
1. n = create(l + "/read-", EPHEMERAL|SEQUENTIAL)
2. C = getChildren(l, false)
3. if no write znodes lower than n in C, exit
4. p = write znode in C ordered just before n
5. if exists(p, true) wait for event
6. goto 3
```

This lock procedure is slightly different from the previous algorithms in a couple of ways. First, removal of a znode could potentially wake up more than one process because of the difference in granting read and write locks. Second, both read and write lock procedures include the same code, but differ in what they do in lines 3 and 4 since this allows us to reuse most of the lock code.

#### 3.7 Double Barrier

Double barriers enable clients to synchronize the beginning and the end of a computation. When enough processes, defined by a barrier threshold, have joined the barrier, processes start their computation and leave the barrier once they have finished. We represent a barrier in ZooKeeper with a znode, referred to as b. Every process p registers with b by creating a znode as a child of b on entry, and unregisters by removing that child when it is ready to leave.

Processes can enter the barrier when the number of children of b exceeds the barrier threshold. Processes can leave the barrier when all the processes have removed their children. We use watches to efficiently wait for enter and exit conditions to be satisfied. To enter, processes watch for the existence of a ready child of b that will be created by the process that causes the number of children to exceed the barrier threshold (the ready child is an implementation convenience and could be eliminated in favor of using a new protocol where each process watches for the number of children to exceed the threshold). To leave, processes watch for the disappearance of a particular child.

---

### النسخة العربية

في هذا القسم، نوضح كيفية استخدام واجهة برمجة تطبيقات زوكيبر لتنفيذ بدائيات أكثر قوة. لا تعرف خدمة زوكيبر شيئاً عن هذه البدائيات الأكثر قوة لأنها منفذة بالكامل على العميل باستخدام واجهة برمجة تطبيقات عميل زوكيبر. بعض البدائيات الشائعة التي نناقشها في هذا القسم هي حالات محددة من تقنيات أكثر عمومية تُستخدم لتنفيذ مشاكل تنسيق مختلفة مع زوكيبر. دفعنا استخدام زوكيبر في التطبيقات الحيوية إلى تنفيذ مكتبة Java لهذه البدائيات مع تنفيذات تم اختبارها بشكل شامل بحيث لا يحتاج المطورون إلى تنفيذ بدائياتهم الخاصة.

#### 3.1 إدارة التكوين

يمكن استخدام زوكيبر لتنفيذ تكوين ديناميكي في تطبيق موزع في شكله الأبسط. يتم تخزين التكوين في عقدة بيانات، zc، وتبدأ العمليات بالمسار الكامل لـ zc. تحصل العمليات البادئة على تكوينها بقراءة zc مع تعيين علامة المراقبة على true. إذا تم تحديث التكوين في zc في أي وقت، يتم إخطار العمليات وتقرأ التكوين الجديد، مرة أخرى تعيين علامة المراقبة على true.

لاحظ أنه في هذا المخطط، كما هو الحال في معظم المخططات الأخرى التي تستخدم المراقبات، يتم استخدام المراقبات للتأكد من أن العملية لديها أحدث المعلومات. على سبيل المثال، إذا علمت عملية تراقب zc أن قيمة zc قد تغيرت، فقد لا تكون القيمة الجديدة التي تقرأها العملية هي التي تسببت في حدث المراقبة. من المهم أن يكون لدى العمليات أحدث معلومات التكوين، إذا كانت بيانات التكوين يمكن أن تتغير بدلاً من مرة واحدة؛ من الأقل أهمية معرفة كل تغيير. بشكل أكثر رسمية، يضمن هذا المخطط أن تحصل العملية القارئة في النهاية على أحدث قيمة تكوين (بافتراض أن التكوينات يتم تعيينها بشكل أبطأ من الوقت المطلوب للإخطار بالإضافة إلى عملية قراءة).

#### 3.2 نقطة اللقاء

في بعض الأحيان في الأنظمة الموزعة، ليس من الواضح دائماً مسبقاً ما هو تكوين النظام النهائي. على سبيل المثال، قد يرغب عميل في بدء عملية رئيسية وعدة عمليات عاملة، لكن بدء العمليات يتم بواسطة جدولة، لذا لا يعرف العميل مسبقاً معلومات مثل العنوان والمنفذ الذي سيستخدمه للتواصل معها.

نتعامل مع هذا السيناريو باستخدام زوكيبر باستخدام عقدة بيانات نقطة لقاء، zr، وهي عقدة أنشأها العميل. يمرر العميل المسار الكامل لـ zr كمعامل بدء لعمليات الرئيسية والعاملة. عندما يبدأ الرئيسي، يملأ zr بمعلومات حول العناوين والمنافذ التي يستخدمها. عندما يبدأ العمال، يقرؤون zr مع تعيين المراقبة على true. إذا لم يتم ملء zr بعد، ينتظر العامل الإخطار عند تحديث zr. إذا كانت zr عقدة مؤقتة، يمكن لعمليات الرئيسية والعاملة مراقبة حذف zr وتنظيف أنفسها عندما ينتهي العميل.

#### 3.3 عضوية المجموعة

نستفيد من العقد المؤقتة لتنفيذ عضوية المجموعة. على وجه الخصوص، نستخدم حقيقة أن العقد المؤقتة تسمح لنا برؤية حالة الجلسة التي أنشأت العقدة. نبدأ بتعيين عقدة بيانات، zg لتمثيل المجموعة. عندما تبدأ عملية عضو في المجموعة، تنشئ عقدة بيانات فرعية مؤقتة تحت zg. إذا كان لكل عملية اسم أو معرف فريد، فسيتم استخدام هذا الاسم كاسم لعقدة البيانات الفرعية؛ وإلا، تنشئ العملية عقدة البيانات مع علامة SEQUENTIAL للحصول على تعيين اسم فريد. قد تضع العمليات معلومات العملية في بيانات عقدة البيانات الفرعية، العناوين والمنافذ التي تستخدمها العملية، على سبيل المثال.

بعد إنشاء عقدة البيانات الفرعية تحت zg، لا تحتاج العملية عادةً إلى فعل أي شيء آخر. إذا فشلت العملية أو انتهت، يتم إزالة عقدة البيانات التي تمثلها تحت zg تلقائياً.

يمكن للعمليات الحصول على معلومات المجموعة ببساطة عن طريق سرد أطفال zg. إذا أرادت عملية مراقبة التغييرات في عضوية المجموعة، يمكن للعملية تعيين علامة المراقبة على true وتحديث معلومات المجموعة (دائماً تعيين علامة المراقبة على true) عندما يتم تلقي إشعارات التغيير.

#### 3.4 أقفال بسيطة

على الرغم من أن زوكيبر ليست خدمة قفل، إلا أنه يمكن استخدامها لتنفيذ الأقفال. التطبيقات التي تستخدم زوكيبر عموماً لا تستخدمها بهذه الطريقة لأن التطبيقات عموماً تستخدم آليات الترتيب والمراقبة في زوكيبر لتنفيذ بدائيات تزامن خاصة بالتطبيق. هنا نوضح كيف يمكن تنفيذ الأقفال مباشرة باستخدام زوكيبر لإظهار أنه يمكن تنفيذ مجموعة واسعة من بدائيات التزامن العامة.

أبسط تنفيذ للقفل يستخدم "ملفات القفل". يتم تمثيل القفل بعقدة بيانات. للحصول على قفل، يحاول العميل إنشاء عقدة البيانات المحددة مع علامة EPHEMERAL. إذا نجح الإنشاء، يحتفظ العميل بالقفل. وإلا، يمكن للعميل قراءة عقدة البيانات مع تعيين علامة المراقبة لإخطاره إذا مات القائد الحالي. يُطلق العميل القفل عندما يموت أو يحذف عقدة البيانات بشكل صريح. العملاء الآخرون الذين ينتظرون القفل يحاولون مرة أخرى الحصول على قفل بمجرد ملاحظتهم حذف عقدة البيانات.

بينما يعمل بروتوكول القفل البسيط هذا، إلا أنه يعاني من بعض المشاكل. أولاً، يعاني من تأثير القطيع. إذا كان هناك العديد من العملاء ينتظرون الحصول على قفل، فسيتنافسون جميعاً على القفل عند إطلاقه على الرغم من أن عميلاً واحداً فقط يمكنه الحصول على القفل. ثانياً، ينفذ فقط القفل الحصري. تُظهر البدائيات التاليتان كيف يمكن التغلب على كلتا هاتين المشكلتين.

#### 3.5 أقفال بسيطة بدون تأثير القطيع

نحدد عقدة بيانات قفل l لتنفيذ مثل هذه الأقفال. بشكل حدسي، نصطف جميع العملاء الذين يطلبون القفل ويحصل كل عميل على القفل بترتيب وصول الطلب. وبالتالي، يفعل العملاء الراغبون في الحصول على القفل ما يلي:

```
القفل
1. n = create(l + "/lock-", EPHEMERAL|SEQUENTIAL)
2. C = getChildren(l, false)
3. if n is lowest znode in C, exit
4. p = znode in C ordered just before n
5. if exists(p, true) wait for watch event
6. goto 2
```

```
فك القفل
1. delete(n)
```

يؤدي استخدام علامة SEQUENTIAL في السطر 1 من بروتوكول القفل إلى ترتيب طلبات قفل العميل فيما يتعلق ببعضها البعض. إذا كانت عقدة بيانات العميل لديها أقل رقم تسلسلي في السطر 3، يحتفظ العميل بالقفل. وإلا، ينتظر العميل حذف عقدة البيانات التي إما لديها القفل أو ستتلقى القفل قبل العميل المعني. من خلال مراقبة عقدة البيانات التي تسبق عقدة بيانات العميل فقط، نتجنب تأثير القطيع بإيقاظ عملية واحدة فقط عند إطلاق القفل أو التخلي عن طلب القفل. بمجرد إخطار العميل بحذف عقدة البيانات السابقة، يجب على العميل التحقق مما إذا كان يحتفظ الآن بالقفل. (قد يكون طلب القفل السابق قد تم التخلي عنه وقد يكون هناك عملاء آخرون بأرقام تسلسلية سابقة لا يزالون ينتظرون، أو يحتفظون بالقفل.)

#### 3.6 أقفال القراءة/الكتابة

لتنفيذ أقفال القراءة/الكتابة، نغير إجراء القفل قليلاً، ولدينا إجراءات منفصلة لقفل القراءة وقفل الكتابة.

```
قفل الكتابة
1. n = create(l + "/write-", EPHEMERAL|SEQUENTIAL)
2. C = getChildren(l, false)
3. if n is lowest znode in C, exit
4. p = znode in C ordered just before n
5. if exists(p, true) wait for event
6. goto 2
```

```
قفل القراءة
1. n = create(l + "/read-", EPHEMERAL|SEQUENTIAL)
2. C = getChildren(l, false)
3. if no write znodes lower than n in C, exit
4. p = write znode in C ordered just before n
5. if exists(p, true) wait for event
6. goto 3
```

يختلف إجراء القفل هذا قليلاً عن الخوارزميات السابقة بطريقتين. أولاً، يمكن أن تؤدي إزالة عقدة بيانات إلى إيقاظ أكثر من عملية واحدة بسبب الاختلاف في منح أقفال القراءة والكتابة. ثانياً، يتضمن كل من إجراءات قفل القراءة والكتابة نفس الكود، لكنهما يختلفان في ما يفعلانه في السطور 3 و 4 لأن هذا يسمح لنا بإعادة استخدام معظم كود القفل.

#### 3.7 حاجز مزدوج

تمكّن الحواجز المزدوجة العملاء من مزامنة بداية ونهاية الحساب. عندما تنضم عمليات كافية، محددة بعتبة حاجز، إلى الحاجز، تبدأ العمليات حسابها وتغادر الحاجز بمجرد انتهائها. نمثل حاجزاً في زوكيبر بعقدة بيانات، يشار إليها باسم b. تسجل كل عملية p مع b عن طريق إنشاء عقدة بيانات كطفل لـ b عند الدخول، وتلغي التسجيل بإزالة هذا الطفل عندما تكون جاهزة للمغادرة.

يمكن للعمليات دخول الحاجز عندما يتجاوز عدد أطفال b عتبة الحاجز. يمكن للعمليات مغادرة الحاجز عندما تزيل جميع العمليات أطفالها. نستخدم المراقبات للانتظار بكفاءة لشروط الدخول والخروج لكي يتم استيفاؤها. للدخول، تراقب العمليات وجود طفل جاهز لـ b سيتم إنشاؤه بواسطة العملية التي تتسبب في تجاوز عدد الأطفال لعتبة الحاجز (الطفل الجاهز هو راحة في التنفيذ ويمكن إزالته لصالح استخدام بروتوكول جديد حيث تراقب كل عملية تجاوز عدد الأطفال للعتبة). للمغادرة، تراقب العمليات اختفاء طفل معين.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Lock files (ملفات القفل) - simple lock mechanism
  - Herd effect (تأثير القطيع) - performance problem
  - Rendezvous (نقطة اللقاء) - synchronization point
  - Double barrier (حاجز مزدوج) - synchronization primitive
  - Read/write locks (أقفال القراءة/الكتابة) - concurrency control

- **Equations:** None
- **Citations:** None in this section
- **Special handling:**
  - Pseudocode preserved in original format
  - API calls (create, getChildren, exists, delete) kept in English
  - Variable names (n, C, p, l, zc, zr, zg, b) kept as in original
  - Code blocks formatted consistently

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-translation Check

First paragraph back-translation: "In this section, we show how to use the ZooKeeper API to implement more powerful primitives. The ZooKeeper service knows nothing about these more powerful primitives because they are entirely implemented on the client using the ZooKeeper client API..."

✅ Semantically equivalent to original
