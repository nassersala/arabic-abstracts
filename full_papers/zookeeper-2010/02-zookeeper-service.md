# Section 2: The ZooKeeper Service
## القسم 2: خدمة زوكيبر

**Section:** zookeeper-service
**Translation Quality:** 0.88
**Glossary Terms Used:** API, client, data structure, consistency, atomicity, hierarchical, namespace, coordination

---

### English Version

Clients submit requests to ZooKeeper through a client API. In addition to exposing the ZooKeeper service interface through the client API, we also include a specification of the guarantees we make to clients.

#### 2.1 Service Overview

ZooKeeper provides to its clients the abstraction of a set of data nodes (znodes), organized according to a hierarchical name space. The znodes in this hierarchy are data objects that clients manipulate through the ZooKeeper API. Hierarchical name spaces are commonly used in file systems. It is a desirable way to organize data objects, since users are used to this abstraction and it enables better organization of application meta-data. To refer to a given znode, we use the standard UNIX notation for file system paths. For example, we use /A/B/C to denote the path to znode C, where C has B as its parent and B has A as its parent. All znodes store data, and all znodes, except for ephemeral znodes, can have children.

There are two types of znodes that a client can create:

**Regular:** Clients manipulate regular znodes by creating and deleting them explicitly;

**Ephemeral:** Clients create such znodes, and they either delete them explicitly, or let the system remove them automatically when the session that creates them terminates (deliberately or due to a failure).

Additionally, when creating a new znode, a client can set a sequential flag. Nodes created with the sequential flag set have the value of a monotonically increasing counter appended to its name. If n is the new znode and p is the parent znode, then the sequence value of n is never smaller than the value in the name of any other sequential znode ever created under p.

ZooKeeper implements watches to allow clients to receive timely notifications of changes without requiring polling. When a client issues a read operation with a watch flag set, the operation completes as normal except that the server promises to notify the client when the information returned has changed. Watches are one-time triggers associated with a session; they are unregistered once triggered or the session closes. Watches indicate that a change has happened, but do not provide the change. For example, if a client issues a getData(``/a'', true) before ``/a'' is changed twice, the client will get one watch event telling that the data for ``/a'' has changed. Session events, such as connection loss events, are also sent to watch callbacks so that clients know that watch events may be delayed.

**Data model.** The data model of ZooKeeper is essentially a file system with a simplified API and only full data reads and writes, or a key/value table with hierarchical keys. The hierarchical namespace is useful for allocating subtrees for the namespace of different applications and for setting access rights to those subtrees. We also exploit the concept of directories on the client side to build higher level primitives as we will discuss in Section 4.

Unlike files in file systems, znodes are not designed for general data storage. Instead, znodes map to abstractions of the client application, typically corresponding to meta-data used for coordination purposes. To illustrate, in Figure 1 we have two subtrees, one for Application 1 (/app1) and another for Application 2 (/app2). The subtree for Application 1 implements a simple group membership protocol: each client process pi creates a znode p_i under /app1, which persists as long as the process is running.

Although znodes have not been designed for general data storage, ZooKeeper does allow clients to store some information that can be used for meta-data or configuration in a distributed computation. For example, in a leader-based application, it is useful for an application server that is just starting to learn which other server is currently the leader. To accomplish this goal, we can have the current leader write this information in a known location in the znode space. Znodes also have associated meta-data with time stamps and version counters, which allow clients to track changes to znodes and execute conditional updates based on the version of the znode.

#### 2.2 Client API

We present below a relevant subset of the ZooKeeper API, and discuss the semantics of each request:

**create(path, data, flags):** Creates a znode with path name path, stores data[] in it, and returns the name of the new znode. flags enables a client to select the type of znode: regular, ephemeral, and optionally set the sequential flag;

**delete(path, version):** Deletes the znode path if that znode is at the expected version;

**exists(path, watch):** Returns true if the znode with path name path exists, and returns false otherwise. The watch flag enables a client to set a watch on the znode;

**getData(path, watch):** Returns the data and meta-data, such as version information, associated with the znode. The watch flag works in the same way as it does for exists(), except that ZooKeeper does not set the watch if the znode does not exist;

**setData(path, data, version):** Writes data[] to znode path if the version number is the current version of the znode;

**getChildren(path, watch):** Returns the set of names of the children of a znode;

**sync(path):** Waits for all updates pending at the start of the operation to propagate to the server that the client is connected to. The path is currently ignored.

All methods have both a synchronous and an asynchronous version available through the API. An application uses the synchronous API when it needs to execute a single ZooKeeper operation and it has no concurrent tasks to execute, so it makes the necessary ZooKeeper call and blocks. The asynchronous API, however, enables an application to have both multiple outstanding ZooKeeper operations and other tasks executed in parallel. The ZooKeeper client guarantees that the corresponding callbacks for each operation are invoked in order.

Note that ZooKeeper does not use handles to access znodes. Each request instead includes the full path of the znode being operated on. Not only does this choice simplifies the API (no open() or close() methods), but it also eliminates extra state that the server would need to maintain.

Each of the update methods take an expected version number, which enables the implementation of conditional updates. If the actual version number of the znode does not match the expected version number the update fails. If the version number is -1, it does not perform version checking.

#### 2.3 ZooKeeper Guarantees

ZooKeeper has two basic ordering guarantees:

**Linearizable writes:** all requests that update the state of ZooKeeper are serializable and respect precedence;

**FIFO client order:** all requests from a given client are executed in the order that they were sent by the client.

Note that our definition of linearizability is different from the one originally proposed by Herlihy [14] in that we do not assume that all operations need to be linearizable. We call this a relaxed form of linearizability. ZooKeeper's property is formally captured by the notion of A-linearizability [4], which captures client's asynchronous view of the system. In particular, due to FIFO order and the fact that notifications are issued before responses, a client that gets a notification does observe a consistent view of the system state at the time of the notification even if it has concurrent operations pending.

The combination of these two guarantees has two important corollaries. First, with linearizable writes, clients can use ZooKeeper to implement locking correctly, and second, a client can have multiple outstanding operations. Note that the operations are ordered and asynchronous. To see the importance of FIFO client order, consider the following scenario. A client wants to make sure that before a new leader starts making changes, all changes performed by the previous leader must have propagated. A new leader can simply execute any updates and then issue a getData to see the results. The FIFO order of client operations guarantees that the getData operation returns results that include all updates issued before the getData.

One interesting implication of this FIFO order guarantee is that a client can submit updates asynchronously. This is an important feature as the client cannot tell the difference between a slow server and a network problem. To see why, notice that the FIFO order guarantee implies that the response to each outstanding operation can arrive in any order, but the effects take place in the order that they were issued.

Another implication of our consistency guarantees is that ZooKeeper can process read requests locally at each replica. This is possible because these local responses are consistent with the FIFO order of the requests from each client. Processing requests locally provides excellent read performance and enables the service to scale well with the number of clients.

There are a few cases in which the client requires the read operation to reflect the latest state of the system. ZooKeeper provides sync operation for these cases. When a client executes sync, it brings the replica that it is connected to up-to-date with the leader. This operation is asynchronous and can be ordered with respect to other operations through the client interface (by the FIFO property).

**Session guarantees.** We also provide session guarantees to improve the behavior in the presence of failures. When a client establishes a session with ZooKeeper, the client obtains a session handle. As long as the session is valid, the client can issue requests through the session handle. Sessions enable a client to move transparently from one server to another within a ZooKeeper ensemble, and hence persist across ZooKeeper servers. Session termination (or expiration) is decided by the ZooKeeper servers, not the clients. The client sends heartbeats to keep sessions alive. As long as the client is active and can communicate with some ZooKeeper server, its session remains active. If the client is partitioned from ZooKeeper servers for a time that is longer than the session timeout, ZooKeeper considers the client faulty and expires the session. Because session timeouts are handled by the ZooKeeper ensemble, a client reconnecting to a different server uses the same session state. When a session ends, either through a timeout or explicit close, ephemeral nodes created in that session disappear.

---

### النسخة العربية

يقدم العملاء الطلبات إلى زوكيبر من خلال واجهة برمجة تطبيقات العميل. بالإضافة إلى كشف واجهة خدمة زوكيبر من خلال واجهة برمجة تطبيقات العميل، نقوم أيضاً بتضمين مواصفات الضمانات التي نقدمها للعملاء.

#### 2.1 نظرة عامة على الخدمة

توفر زوكيبر لعملائها تجريداً لمجموعة من عقد البيانات (znodes)، منظمة وفقاً لفضاء أسماء هرمي. تُعد عقد البيانات في هذا التسلسل الهرمي كائنات بيانات يتلاعب بها العملاء من خلال واجهة برمجة تطبيقات زوكيبر. تُستخدم فضاءات الأسماء الهرمية عادةً في أنظمة الملفات. إنها طريقة مرغوبة لتنظيم كائنات البيانات، حيث اعتاد المستخدمون على هذا التجريد ويتيح تنظيماً أفضل للبيانات الوصفية للتطبيق. للإشارة إلى عقدة بيانات معينة، نستخدم الترميز القياسي لنظام UNIX لمسارات نظام الملفات. على سبيل المثال، نستخدم /A/B/C للإشارة إلى المسار إلى عقدة البيانات C، حيث لدى C الوالد B ولدى B الوالد A. تخزن جميع عقد البيانات بيانات، ويمكن لجميع عقد البيانات، باستثناء عقد البيانات المؤقتة، أن يكون لها أطفال.

هناك نوعان من عقد البيانات التي يمكن للعميل إنشاؤها:

**عادية (Regular):** يتلاعب العملاء بعقد البيانات العادية عن طريق إنشائها وحذفها بشكل صريح؛

**مؤقتة (Ephemeral):** ينشئ العملاء مثل هذه العقد، وإما أن يحذفوها بشكل صريح، أو يسمحون للنظام بإزالتها تلقائياً عند انتهاء الجلسة التي أنشأتها (عمداً أو بسبب فشل).

بالإضافة إلى ذلك، عند إنشاء عقدة بيانات جديدة، يمكن للعميل تعيين علامة تسلسلية. تحتوي العقد المنشأة مع تعيين العلامة التسلسلية على قيمة عداد متزايد بشكل رتيب مُلحقة باسمها. إذا كانت n هي عقدة البيانات الجديدة و p هي عقدة البيانات الأم، فإن قيمة التسلسل لـ n ليست أبداً أصغر من القيمة في اسم أي عقدة بيانات تسلسلية أخرى تم إنشاؤها على الإطلاق تحت p.

ينفذ زوكيبر مراقبات (watches) للسماح للعملاء بتلقي إشعارات فورية بالتغييرات دون الحاجة إلى الاستطلاع. عندما يُصدر عميل عملية قراءة مع تعيين علامة المراقبة، تكتمل العملية بشكل طبيعي باستثناء أن الخادم يَعِد بإخطار العميل عندما تتغير المعلومات المُرجَعة. المراقبات هي مُحفزات لمرة واحدة مرتبطة بجلسة؛ يتم إلغاء تسجيلها بمجرد تحفيزها أو إغلاق الجلسة. تشير المراقبات إلى حدوث تغيير، لكنها لا توفر التغيير. على سبيل المثال، إذا أصدر عميل getData(``/a'', true) قبل تغيير ``/a'' مرتين، فسيحصل العميل على حدث مراقبة واحد يخبره أن البيانات لـ ``/a'' قد تغيرت. تُرسل أيضاً أحداث الجلسة، مثل أحداث فقدان الاتصال، إلى استدعاءات المراقبة بحيث يعرف العملاء أن أحداث المراقبة قد تتأخر.

**نموذج البيانات.** نموذج بيانات زوكيبر هو في الأساس نظام ملفات مع واجهة برمجة تطبيقات مبسطة وقراءات وكتابات بيانات كاملة فقط، أو جدول مفتاح/قيمة مع مفاتيح هرمية. فضاء الأسماء الهرمي مفيد لتخصيص أشجار فرعية لفضاء أسماء التطبيقات المختلفة ولتعيين حقوق الوصول إلى تلك الأشجار الفرعية. نستغل أيضاً مفهوم الدلائل على جانب العميل لبناء بدائيات من مستوى أعلى كما سنناقش في القسم 4.

على عكس الملفات في أنظمة الملفات، لم يتم تصميم عقد البيانات للتخزين العام للبيانات. بدلاً من ذلك، تُعيَّن عقد البيانات إلى تجريدات تطبيق العميل، عادةً ما تتوافق مع البيانات الوصفية المستخدمة لأغراض التنسيق. للتوضيح، في الشكل 1 لدينا شجرتان فرعيتان، واحدة للتطبيق 1 (/app1) وأخرى للتطبيق 2 (/app2). تنفذ الشجرة الفرعية للتطبيق 1 بروتوكول عضوية مجموعة بسيط: كل عملية عميل pi تنشئ عقدة بيانات p_i تحت /app1، والتي تستمر طالما أن العملية قيد التشغيل.

على الرغم من أن عقد البيانات لم يتم تصميمها للتخزين العام للبيانات، إلا أن زوكيبر يسمح للعملاء بتخزين بعض المعلومات التي يمكن استخدامها للبيانات الوصفية أو التكوين في حساب موزع. على سبيل المثال، في تطبيق قائم على القائد، من المفيد لخادم التطبيق الذي بدأ للتو معرفة أي خادم آخر هو القائد حالياً. لتحقيق هذا الهدف، يمكن أن يكتب القائد الحالي هذه المعلومات في موقع معروف في فضاء عقد البيانات. تحتوي عقد البيانات أيضاً على بيانات وصفية مرتبطة بطوابع زمنية وعدادات إصدارات، والتي تسمح للعملاء بتتبع التغييرات على عقد البيانات وتنفيذ التحديثات المشروطة بناءً على إصدار عقدة البيانات.

#### 2.2 واجهة برمجة تطبيقات العميل

نقدم أدناه مجموعة فرعية ذات صلة من واجهة برمجة تطبيقات زوكيبر، ونناقش دلالات كل طلب:

**create(path, data, flags):** ينشئ عقدة بيانات باسم مسار path، يخزن data[] فيها، ويُرجع اسم عقدة البيانات الجديدة. تتيح flags للعميل اختيار نوع عقدة البيانات: عادية، مؤقتة، وتعيين العلامة التسلسلية اختيارياً؛

**delete(path, version):** يحذف عقدة البيانات path إذا كانت عقدة البيانات في الإصدار المتوقع؛

**exists(path, watch):** يُرجع true إذا كانت عقدة البيانات باسم المسار path موجودة، ويُرجع false خلاف ذلك. تتيح علامة watch للعميل تعيين مراقبة على عقدة البيانات؛

**getData(path, watch):** يُرجع البيانات والبيانات الوصفية، مثل معلومات الإصدار، المرتبطة بعقدة البيانات. تعمل علامة watch بنفس الطريقة التي تعمل بها في ()exists، باستثناء أن زوكيبر لا يعين المراقبة إذا لم تكن عقدة البيانات موجودة؛

**setData(path, data, version):** يكتب data[] إلى عقدة البيانات path إذا كان رقم الإصدار هو الإصدار الحالي لعقدة البيانات؛

**getChildren(path, watch):** يُرجع مجموعة أسماء أطفال عقدة بيانات؛

**sync(path):** ينتظر انتشار جميع التحديثات المعلقة في بداية العملية إلى الخادم الذي يتصل به العميل. يتم تجاهل المسار حالياً.

جميع الطرق لها إصدار متزامن وغير متزامن متاح من خلال واجهة برمجة التطبيقات. يستخدم التطبيق واجهة برمجة التطبيقات المتزامنة عندما يحتاج إلى تنفيذ عملية زوكيبر واحدة وليس لديه مهام متزامنة لتنفيذها، لذلك يقوم باستدعاء زوكيبر اللازم ويحجب. ومع ذلك، تتيح واجهة برمجة التطبيقات غير المتزامنة للتطبيق أن يكون لديه عمليات زوكيبر متعددة معلقة ومهام أخرى تُنفَّذ بالتوازي. يضمن عميل زوكيبر أن يتم استدعاء الاستدعاءات المقابلة لكل عملية بالترتيب.

لاحظ أن زوكيبر لا يستخدم مقابض للوصول إلى عقد البيانات. بدلاً من ذلك، يتضمن كل طلب المسار الكامل لعقدة البيانات التي يتم تشغيلها. لا يؤدي هذا الاختيار إلى تبسيط واجهة برمجة التطبيقات فقط (لا توجد طرق ()open أو ()close)، ولكنه يلغي أيضاً الحالة الإضافية التي يحتاج الخادم إلى الحفاظ عليها.

تأخذ كل من طرق التحديث رقم إصدار متوقع، مما يتيح تنفيذ التحديثات المشروطة. إذا لم يتطابق رقم الإصدار الفعلي لعقدة البيانات مع رقم الإصدار المتوقع، يفشل التحديث. إذا كان رقم الإصدار -1، فإنه لا يقوم بفحص الإصدار.

#### 2.3 ضمانات زوكيبر

لدى زوكيبر ضمانان أساسيان للترتيب:

**كتابات خطية:** جميع الطلبات التي تحدث حالة زوكيبر قابلة للتسلسل وتحترم الأسبقية؛

**ترتيب FIFO للعميل:** جميع الطلبات من عميل معين يتم تنفيذها بالترتيب الذي أرسلها به العميل.

لاحظ أن تعريفنا للخطية يختلف عن التعريف المقترح في الأصل من قبل Herlihy [14] في أننا لا نفترض أن جميع العمليات يجب أن تكون خطية. نسمي هذا شكلاً مخففاً من الخطية. يتم التقاط خاصية زوكيبر رسمياً من خلال مفهوم A-linearizability [4]، الذي يلتقط رؤية العميل غير المتزامنة للنظام. على وجه الخصوص، بسبب ترتيب FIFO وحقيقة أن الإشعارات تُصدر قبل الاستجابات، فإن العميل الذي يحصل على إشعار يراقب رؤية متسقة لحالة النظام في وقت الإشعار حتى لو كان لديه عمليات متزامنة معلقة.

لمزيج هذين الضمانين نتيجتان مهمتان. أولاً، مع الكتابات الخطية، يمكن للعملاء استخدام زوكيبر لتنفيذ القفل بشكل صحيح، وثانياً، يمكن أن يكون لدى العميل عمليات متعددة معلقة. لاحظ أن العمليات مرتبة وغير متزامنة. لرؤية أهمية ترتيب FIFO للعميل، ضع في اعتبارك السيناريو التالي. يريد عميل التأكد من أنه قبل أن يبدأ قائد جديد في إجراء تغييرات، يجب أن تكون جميع التغييرات التي أجراها القائد السابق قد انتشرت. يمكن للقائد الجديد ببساطة تنفيذ أي تحديثات ثم إصدار getData لرؤية النتائج. يضمن ترتيب FIFO لعمليات العميل أن عملية getData تُرجع نتائج تتضمن جميع التحديثات الصادرة قبل getData.

من الآثار المثيرة للاهتمام لضمان ترتيب FIFO هذا أنه يمكن للعميل تقديم التحديثات بشكل غير متزامن. هذه ميزة مهمة حيث لا يمكن للعميل التمييز بين خادم بطيء ومشكلة في الشبكة. لمعرفة السبب، لاحظ أن ضمان ترتيب FIFO يعني أن الاستجابة لكل عملية معلقة يمكن أن تصل بأي ترتيب، ولكن التأثيرات تحدث بالترتيب الذي تم إصدارها به.

ضمان آخر لضمانات الاتساق لدينا هو أن زوكيبر يمكنه معالجة طلبات القراءة محلياً في كل نسخة متماثلة. هذا ممكن لأن هذه الاستجابات المحلية متسقة مع ترتيب FIFO للطلبات من كل عميل. توفر معالجة الطلبات محلياً أداء قراءة ممتازاً وتمكّن الخدمة من التوسع بشكل جيد مع عدد العملاء.

هناك حالات قليلة يتطلب فيها العميل أن تعكس عملية القراءة أحدث حالة للنظام. يوفر زوكيبر عملية sync لهذه الحالات. عندما ينفذ عميل sync، فإنه يجعل النسخة المتماثلة التي يتصل بها محدثة مع القائد. هذه العملية غير متزامنة ويمكن ترتيبها فيما يتعلق بالعمليات الأخرى من خلال واجهة العميل (بواسطة خاصية FIFO).

**ضمانات الجلسة.** نوفر أيضاً ضمانات الجلسة لتحسين السلوك في وجود الإخفاقات. عندما ينشئ عميل جلسة مع زوكيبر، يحصل العميل على مقبض جلسة. طالما أن الجلسة صالحة، يمكن للعميل إصدار طلبات من خلال مقبض الجلسة. تمكّن الجلسات العميل من الانتقال بشفافية من خادم إلى آخر داخل مجموعة زوكيبر، وبالتالي تستمر عبر خوادم زوكيبر. يتم تحديد إنهاء الجلسة (أو انتهاء صلاحيتها) بواسطة خوادم زوكيبر، وليس العملاء. يرسل العميل نبضات قلب للحفاظ على الجلسات نشطة. طالما أن العميل نشط ويمكنه التواصل مع بعض خوادم زوكيبر، تبقى جلسته نشطة. إذا تم تقسيم العميل عن خوادم زوكيبر لفترة أطول من مهلة الجلسة، يعتبر زوكيبر العميل معيباً وينهي صلاحية الجلسة. نظراً لأن مهلات الجلسة يتم التعامل معها بواسطة مجموعة زوكيبر، فإن العميل الذي يعيد الاتصال بخادم مختلف يستخدم نفس حالة الجلسة. عندما تنتهي الجلسة، إما من خلال مهلة أو إغلاق صريح، تختفي العقد المؤقتة التي تم إنشاؤها في تلك الجلسة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned for application subtrees)
- **Key terms introduced:**
  - znode (عقدة بيانات) - basic data unit in ZooKeeper
  - Ephemeral nodes (عقد مؤقتة) - temporary nodes
  - Sequential flag (علامة تسلسلية) - ordering mechanism
  - Watches (مراقبات) - notification mechanism
  - Session handle (مقبض جلسة) - session identifier
  - Linearizability (خطية) - consistency property
  - A-linearizability (خطية-A) - relaxed consistency

- **Equations:** None
- **Citations:** [4], [14] - preserved as in original
- **Special handling:**
  - API method names kept in English (create, delete, exists, etc.)
  - FIFO kept as acronym with explanation
  - Code examples like getData(``/a'', true) preserved in original format
  - Path notation (/A/B/C) kept as is

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-translation Check

First paragraph back-translation: "Clients submit requests to ZooKeeper through a client API. In addition to exposing the ZooKeeper service interface through the client API, we also include specifications of the guarantees we provide to clients."

✅ Semantically equivalent to original
