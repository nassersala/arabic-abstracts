# Section IV: Process Level Communication
## القسم الرابع: الاتصال على مستوى العملية

**Section:** Process Level Communication
**Translation Quality:** 0.87
**Glossary Terms Used:** process, port, socket, connection, synchronization, data stream, full-duplex, half-duplex, multiplexing

---

### English Version

The TCP provides process-to-process communication services. Processes are identified by PORTS, which are local identifiers assigned within each host. The combination of an internet address and a port number uniquely identifies a process in the internet.

**A. Ports and Sockets**

A PORT is an abstraction representing a communication endpoint within a host. Ports are numbered, and processes bind to specific port numbers to send and receive data. Well-known services (such as file transfer or electronic mail) are assigned standard port numbers that are recognized throughout the internet.

A SOCKET is defined as the concatenation of an internet address and a port number. A socket uniquely identifies a communication endpoint in the internet. For example, the socket (Network A, Host 3, Port 27) identifies port 27 on host 3 in network A.

**B. Connections**

Communication between processes is organized around CONNECTIONS. A connection is a logical channel between two sockets, established by a connection establishment protocol and terminated by a connection termination protocol.

A connection is characterized by:

1. **Source socket:** The socket at the sending process
2. **Destination socket:** The socket at the receiving process
3. **Connection state:** Information maintained by each host about the connection
4. **Sequence space:** The range of sequence numbers used for this connection

Connections provide the following properties:

- **Reliability:** Data is delivered accurately and in order, or the sender is notified of delivery failure
- **Full-duplex operation:** Data can flow simultaneously in both directions
- **Stream interface:** Processes send and receive data as a continuous byte stream without message boundaries

**C. Connection Establishment**

Before data can be exchanged, processes must establish a connection using a three-way handshake:

1. **SYN:** The initiating process sends a synchronization segment (SYN) to the destination, containing an initial sequence number
2. **SYN-ACK:** The destination responds with its own SYN segment and acknowledges the initiator's sequence number
3. **ACK:** The initiator acknowledges the destination's sequence number, completing the handshake

This three-way handshake ensures that both sides agree on initial sequence numbers and are ready to exchange data. It also protects against old duplicate connection requests from previous connections.

**D. Data Transfer**

Once a connection is established, processes can send and receive data. The TCP segments data into manageable pieces and assigns sequence numbers to each byte. The receiver acknowledges received data and the sender retransmits any unacknowledged data after a timeout.

The protocol supports both PUSH and URGENT data mechanisms:

- **PUSH:** Indicates that data should be delivered to the receiving process immediately without waiting for additional data to arrive
- **URGENT:** Marks high-priority data that requires immediate attention from the receiving process

**E. Connection Termination**

When processes finish exchanging data, they terminate the connection gracefully:

1. **FIN:** The process wishing to close sends a finish (FIN) segment
2. **ACK:** The other side acknowledges the FIN
3. **FIN:** The second process sends its own FIN when ready to close
4. **ACK:** The first process acknowledges the second FIN

This four-way handshake ensures that both sides have finished sending data and all data has been acknowledged before the connection is closed. The connection state is maintained for a period after closure to handle delayed packets from the connection.

**F. Multiplexing**

Multiple connections can exist simultaneously between the same pair of hosts. Each connection is distinguished by its socket pair. This allows a single host to support many concurrent communications with other hosts.

For example, a host might simultaneously maintain connections for file transfer, remote login, and electronic mail with the same remote host. Each service uses a different port number, creating distinct socket pairs and therefore distinct connections.

**G. Half-Duplex vs. Full-Duplex**

While TCP supports full-duplex operation (simultaneous bidirectional data flow), some applications may choose to operate in half-duplex mode (alternating direction of data flow). The protocol accommodates both usage patterns.

**H. Precedence and Security**

Processes can specify precedence and security parameters for their connections. These parameters are included in TCP segments and may influence how gateways handle the traffic.

Higher precedence connections may receive preferential treatment during congestion. Security parameters indicate the sensitivity of the data and may restrict which paths the data can traverse.

---

### النسخة العربية

يوفر TCP خدمات الاتصال من عملية إلى عملية. يتم تحديد العمليات بواسطة المنافذ (PORTS)، وهي معرّفات محلية مخصصة داخل كل مضيف. يحدد الجمع بين عنوان الإنترنت ورقم المنفذ عملية بشكل فريد في الإنترنت.

**أ. المنافذ والمقابس**

المنفذ (PORT) هو تجريد يمثل نقطة نهاية الاتصال داخل المضيف. يتم ترقيم المنافذ، وترتبط العمليات بأرقام منافذ محددة لإرسال واستقبال البيانات. يتم تعيين أرقام منافذ قياسية للخدمات المعروفة (مثل نقل الملفات أو البريد الإلكتروني) والتي يتم التعرف عليها في جميع أنحاء الإنترنت.

يُعرّف المقبس (SOCKET) على أنه دمج عنوان الإنترنت ورقم المنفذ. يحدد المقبس نقطة نهاية الاتصال بشكل فريد في الإنترنت. على سبيل المثال، يحدد المقبس (الشبكة A، المضيف 3، المنفذ 27) المنفذ 27 على المضيف 3 في الشبكة A.

**ب. الاتصالات**

يتم تنظيم الاتصال بين العمليات حول الاتصالات (CONNECTIONS). الاتصال هو قناة منطقية بين مقبسين، يتم إنشاؤها بواسطة بروتوكول إنشاء الاتصال وإنهاؤها بواسطة بروتوكول إنهاء الاتصال.

يتميز الاتصال بما يلي:

1. **مقبس المصدر:** المقبس عند العملية المرسلة
2. **مقبس الوجهة:** المقبس عند العملية المستقبلة
3. **حالة الاتصال:** المعلومات التي يحتفظ بها كل مضيف حول الاتصال
4. **فضاء التسلسل:** نطاق أرقام التسلسل المستخدمة لهذا الاتصال

توفر الاتصالات الخصائص التالية:

- **الموثوقية:** يتم تسليم البيانات بدقة وبالترتيب، أو يتم إخطار المرسل بفشل التسليم
- **التشغيل الكامل الازدواجية:** يمكن أن تتدفق البيانات في كلا الاتجاهين في وقت واحد
- **واجهة التدفق:** ترسل العمليات وتستقبل البيانات كتدفق بايت مستمر دون حدود للرسائل

**ج. إنشاء الاتصال**

قبل أن يتم تبادل البيانات، يجب على العمليات إنشاء اتصال باستخدام مصافحة ثلاثية:

1. **SYN:** ترسل العملية البادئة مقطع مزامنة (SYN) إلى الوجهة، يحتوي على رقم تسلسلي أولي
2. **SYN-ACK:** تستجيب الوجهة بمقطع SYN خاص بها وتقر برقم تسلسل البادئ
3. **ACK:** يقر البادئ برقم تسلسل الوجهة، مكملاً المصافحة

تضمن هذه المصافحة الثلاثية أن كلا الجانبين يتفقان على أرقام التسلسل الأولية ومستعدان لتبادل البيانات. كما أنها تحمي من طلبات الاتصال المكررة القديمة من الاتصالات السابقة.

**د. نقل البيانات**

بمجرد إنشاء الاتصال، يمكن للعمليات إرسال واستقبال البيانات. يقسم TCP البيانات إلى قطع قابلة للإدارة ويخصص أرقام تسلسلية لكل بايت. يقر المستقبل بالبيانات المستلمة ويعيد المرسل إرسال أي بيانات غير معترف بها بعد انتهاء المهلة.

يدعم البروتوكول آليتي بيانات PUSH وURGENT:

- **PUSH:** يشير إلى أنه يجب تسليم البيانات إلى العملية المستقبلة فوراً دون انتظار وصول بيانات إضافية
- **URGENT:** يحدد البيانات ذات الأولوية العالية التي تتطلب اهتماماً فورياً من العملية المستقبلة

**هـ. إنهاء الاتصال**

عندما تنتهي العمليات من تبادل البيانات، تنهي الاتصال بشكل سلس:

1. **FIN:** ترسل العملية التي ترغب في الإغلاق مقطع إنهاء (FIN)
2. **ACK:** يقر الجانب الآخر بـ FIN
3. **FIN:** ترسل العملية الثانية FIN الخاص بها عندما تكون مستعدة للإغلاق
4. **ACK:** تقر العملية الأولى بـ FIN الثاني

تضمن هذه المصافحة الرباعية أن كلا الجانبين انتهيا من إرسال البيانات وأن جميع البيانات قد تم الإقرار بها قبل إغلاق الاتصال. يتم الاحتفاظ بحالة الاتصال لفترة بعد الإغلاق للتعامل مع الحزم المتأخرة من الاتصال.

**و. تعدد الإرسال**

يمكن أن توجد اتصالات متعددة في وقت واحد بين نفس زوج المضيفات. يتم تمييز كل اتصال بزوج المقابس الخاص به. يتيح ذلك لمضيف واحد دعم العديد من الاتصالات المتزامنة مع مضيفات أخرى.

على سبيل المثال، قد يحتفظ المضيف في وقت واحد باتصالات لنقل الملفات، وتسجيل الدخول عن بُعد، والبريد الإلكتروني مع نفس المضيف البعيد. تستخدم كل خدمة رقم منفذ مختلف، مما يخلق أزواج مقابس متميزة وبالتالي اتصالات متميزة.

**ز. نصف الازدواجية مقابل الكامل الازدواجية**

بينما يدعم TCP التشغيل الكامل الازدواجية (تدفق البيانات ثنائي الاتجاه في وقت واحد)، قد تختار بعض التطبيقات العمل في وضع نصف الازدواجية (اتجاه متناوب لتدفق البيانات). يستوعب البروتوكول كلا نمطي الاستخدام.

**ح. الأولوية والأمان**

يمكن للعمليات تحديد معاملات الأولوية والأمان لاتصالاتها. يتم تضمين هذه المعاملات في مقاطع TCP وقد تؤثر على كيفية تعامل البوابات مع حركة المرور.

قد تحصل الاتصالات ذات الأولوية الأعلى على معاملة تفضيلية أثناء الازدحام. تشير معاملات الأمان إلى حساسية البيانات وقد تقيد المسارات التي يمكن للبيانات أن تسلكها.

---

### Translation Notes

- **Key concepts introduced:**
  - PORT (المنفذ) - communication endpoint identifier within a host
  - SOCKET (المقبس) - combination of internet address + port number
  - CONNECTION (الاتصال) - logical channel between two sockets
  - Three-way handshake (المصافحة الثلاثية) - SYN, SYN-ACK, ACK
  - Four-way handshake (المصافحة الرباعية) - FIN, ACK, FIN, ACK

- **Connection lifecycle:**
  1. Establishment (إنشاء) - three-way handshake
  2. Data transfer (نقل البيانات) - bidirectional communication
  3. Termination (إنهاء) - four-way handshake

- **Data transfer modes:**
  - PUSH (دفع) - immediate delivery flag
  - URGENT (عاجل) - high-priority data marker
  - Full-duplex (كامل الازدواجية) - simultaneous bidirectional
  - Half-duplex (نصف الازدواجية) - alternating direction

- **Important terminology:**
  - Well-known ports (منافذ معروفة) - standard service ports
  - Socket pair (زوج المقابس) - source + destination sockets
  - Connection state (حالة الاتصال) - maintained information
  - Sequence space (فضاء التسلسل) - range of sequence numbers
  - Stream interface (واجهة التدفق) - byte stream abstraction

- **Protocol mechanisms:**
  - Multiplexing via port numbers
  - Reliable in-order delivery
  - Graceful connection termination
  - Support for precedence and security

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
