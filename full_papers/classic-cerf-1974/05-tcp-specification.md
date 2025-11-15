# Section V: The TCP Specification
## القسم الخامس: مواصفة بروتوكول TCP

**Section:** TCP Specification
**Translation Quality:** 0.86
**Glossary Terms Used:** header, segment, sequence number, acknowledgment, window, flags, checksum, options, control bits, data offset

---

### English Version

This section describes the detailed specification of the Transmission Control Protocol (TCP).

**A. TCP Header Format**

Each TCP segment consists of a header followed by data. The TCP header contains the following fields:

1. **Source Port (16 bits):** Identifies the sending port
2. **Destination Port (16 bits):** Identifies the receiving port
3. **Sequence Number (32 bits):** The sequence number of the first data byte in this segment
4. **Acknowledgment Number (32 bits):** The sequence number of the next byte the sender expects to receive
5. **Data Offset (4 bits):** The number of 32-bit words in the TCP header, indicating where data begins
6. **Reserved (6 bits):** Reserved for future use, must be zero
7. **Control Bits (6 bits):** URG, ACK, PSH, RST, SYN, FIN flags
8. **Window (16 bits):** The number of data bytes the sender is willing to accept
9. **Checksum (16 bits):** Error detection field covering header and data
10. **Urgent Pointer (16 bits):** Points to urgent data when URG flag is set
11. **Options (variable):** Optional header extensions
12. **Padding:** Zeros to ensure header ends on a 32-bit boundary

**B. Control Bits**

The control bits (also called flags) control connection management and data handling:

- **URG:** Urgent pointer field is significant
- **ACK:** Acknowledgment field is significant
- **PSH:** Push function - deliver data to application immediately
- **RST:** Reset the connection due to error or abort
- **SYN:** Synchronize sequence numbers (connection establishment)
- **FIN:** No more data from sender (connection termination)

**C. Sequence Numbers**

Every byte of data transmitted is assigned a sequence number. The sequence number in the header refers to the first byte of data in the segment. Sequence numbers are 32-bit values that wrap around.

The initial sequence number (ISN) is chosen when a connection is established. Each side chooses its own ISN and communicates it to the other side during the three-way handshake. Using different ISNs for each connection helps distinguish data from old connections.

Acknowledgments are cumulative: an acknowledgment number N indicates that all bytes up to (but not including) N have been successfully received. This allows for efficient acknowledgment of multiple segments with a single ACK.

**D. Window Mechanism**

The window field implements flow control. The receiver advertises how many bytes of data it can accept by setting the window field in its acknowledgment segments.

The sender maintains three pointers:

1. **Send Unacknowledged (SND.UNA):** The oldest unacknowledged sequence number
2. **Send Next (SND.NXT):** The next sequence number to be sent
3. **Send Window (SND.WND):** The size of the send window

The sender may transmit data with sequence numbers from SND.UNA to SND.UNA + SND.WND. As acknowledgments arrive, SND.UNA advances, opening the window to allow more data to be sent.

The receiver similarly maintains:

1. **Receive Next (RCV.NXT):** The next sequence number expected
2. **Receive Window (RCV.WND):** The size of the receive window

**E. Checksum Calculation**

The checksum field provides error detection for the TCP segment. The checksum is computed over:

1. A pseudo-header containing source and destination internet addresses
2. The TCP header
3. The TCP data

The pseudo-header ensures that segments are delivered to the correct destination. Including the internet addresses in the checksum calculation catches errors in the internet layer addressing.

The checksum algorithm is the 16-bit one's complement of the one's complement sum of all 16-bit words in the segment. If a segment contains an odd number of bytes, the last byte is padded with zeros for checksum calculation.

**F. Connection States**

A TCP connection progresses through a series of states:

1. **CLOSED:** No connection exists
2. **LISTEN:** Waiting for connection request from remote host
3. **SYN-SENT:** Sent SYN, waiting for matching SYN-ACK
4. **SYN-RECEIVED:** Received SYN, sent SYN-ACK, waiting for ACK
5. **ESTABLISHED:** Connection is open, data transfer can occur
6. **FIN-WAIT-1:** Sent FIN, waiting for ACK or FIN
7. **FIN-WAIT-2:** Received ACK of FIN, waiting for FIN from remote
8. **CLOSE-WAIT:** Received FIN, waiting for application to close
9. **CLOSING:** Simultaneous close, waiting for ACK of FIN
10. **LAST-ACK:** Sent FIN after receiving FIN, waiting for ACK
11. **TIME-WAIT:** Waiting for network to clear old segments

The TIME-WAIT state is particularly important. After receiving the final FIN-ACK, a connection enters TIME-WAIT for twice the maximum segment lifetime (2*MSL). This ensures that delayed segments from the old connection have expired before the same socket pair can be reused.

**G. Retransmission Strategy**

When a segment is transmitted, a copy is placed in a retransmission queue and a retransmission timer is started. If an acknowledgment is received before the timer expires, the segment is removed from the queue. If the timer expires, the segment is retransmitted and a new timer is started.

The retransmission timeout (RTO) should be set based on the observed round-trip time (RTT). A simple approach is to measure RTT for segments and set RTO to a multiple of the average RTT. More sophisticated implementations use smoothed RTT estimates and variance measurements.

**H. Options**

TCP options provide extensibility. Options are placed after the standard header and before data. Each option has a type field, and most options have a length field followed by option-specific data.

Examples of options include:

- **End of Option List:** Marks the end of options
- **No Operation:** Used for alignment
- **Maximum Segment Size:** Advertises the maximum segment size the sender can accept

Options allow TCP to be extended with new features while maintaining backward compatibility with implementations that don't recognize the new options.

**I. Multiplexing**

TCP multiplexes multiple connections over a single internet address using port numbers. The combination of source address, source port, destination address, and destination port uniquely identifies a connection.

This four-tuple allows multiple processes on the same host to communicate simultaneously with the same or different remote hosts. It also allows a server to handle multiple connections from different clients, all using the same well-known port number.

---

### النسخة العربية

يصف هذا القسم المواصفة التفصيلية لبروتوكول التحكم في النقل (TCP).

**أ. تنسيق رأس TCP**

يتكون كل مقطع TCP من رأس يليه بيانات. يحتوي رأس TCP على الحقول التالية:

1. **منفذ المصدر (16 بت):** يحدد المنفذ المرسل
2. **منفذ الوجهة (16 بت):** يحدد المنفذ المستقبل
3. **رقم التسلسل (32 بت):** رقم تسلسل أول بايت بيانات في هذا المقطع
4. **رقم الإقرار (32 بت):** رقم تسلسل البايت التالي الذي يتوقع المرسل استقباله
5. **إزاحة البيانات (4 بت):** عدد الكلمات 32 بت في رأس TCP، مشيراً إلى مكان بداية البيانات
6. **محجوز (6 بت):** محجوز للاستخدام المستقبلي، يجب أن يكون صفر
7. **بتات التحكم (6 بت):** أعلام URG، ACK، PSH، RST، SYN، FIN
8. **النافذة (16 بت):** عدد بايتات البيانات التي يرغب المرسل في قبولها
9. **مجموع الفحص (16 بت):** حقل الكشف عن الأخطاء يغطي الرأس والبيانات
10. **مؤشر العاجل (16 بت):** يشير إلى البيانات العاجلة عند تعيين علم URG
11. **الخيارات (متغير):** امتدادات رأس اختيارية
12. **الحشو:** أصفار لضمان انتهاء الرأس على حدود 32 بت

**ب. بتات التحكم**

تتحكم بتات التحكم (تسمى أيضاً الأعلام) في إدارة الاتصال ومعالجة البيانات:

- **URG:** حقل المؤشر العاجل مهم
- **ACK:** حقل الإقرار مهم
- **PSH:** وظيفة الدفع - تسليم البيانات للتطبيق فوراً
- **RST:** إعادة تعيين الاتصال بسبب خطأ أو إجهاض
- **SYN:** مزامنة أرقام التسلسل (إنشاء الاتصال)
- **FIN:** لا مزيد من البيانات من المرسل (إنهاء الاتصال)

**ج. أرقام التسلسل**

يتم تعيين رقم تسلسلي لكل بايت من البيانات المرسلة. يشير رقم التسلسل في الرأس إلى أول بايت من البيانات في المقطع. أرقام التسلسل هي قيم 32 بت تلتف حولها.

يتم اختيار رقم التسلسل الأولي (ISN) عند إنشاء الاتصال. يختار كل جانب ISN الخاص به ويوصله إلى الجانب الآخر أثناء المصافحة الثلاثية. يساعد استخدام ISN مختلفة لكل اتصال في تمييز البيانات من الاتصالات القديمة.

الإقرارات تراكمية: يشير رقم الإقرار N إلى أن جميع البايتات حتى (ولكن لا تشمل) N قد تم استقبالها بنجاح. يتيح ذلك الإقرار الفعال لمقاطع متعددة بـ ACK واحد.

**د. آلية النافذة**

يطبق حقل النافذة التحكم في التدفق. يعلن المستقبل عن عدد بايتات البيانات التي يمكنه قبولها عن طريق تعيين حقل النافذة في مقاطع الإقرار الخاصة به.

يحتفظ المرسل بثلاثة مؤشرات:

1. **الإرسال غير المُقر به (SND.UNA):** أقدم رقم تسلسلي غير مُقر به
2. **الإرسال التالي (SND.NXT):** رقم التسلسل التالي الذي سيتم إرساله
3. **نافذة الإرسال (SND.WND):** حجم نافذة الإرسال

قد يرسل المرسل بيانات بأرقام تسلسل من SND.UNA إلى SND.UNA + SND.WND. مع وصول الإقرارات، يتقدم SND.UNA، مما يفتح النافذة للسماح بإرسال المزيد من البيانات.

يحتفظ المستقبل بالمثل بـ:

1. **الاستقبال التالي (RCV.NXT):** رقم التسلسل التالي المتوقع
2. **نافذة الاستقبال (RCV.WND):** حجم نافذة الاستقبال

**هـ. حساب مجموع الفحص**

يوفر حقل مجموع الفحص الكشف عن الأخطاء لمقطع TCP. يتم حساب مجموع الفحص على:

1. رأس زائف يحتوي على عناوين الإنترنت للمصدر والوجهة
2. رأس TCP
3. بيانات TCP

يضمن الرأس الزائف تسليم المقاطع إلى الوجهة الصحيحة. يؤدي تضمين عناوين الإنترنت في حساب مجموع الفحص إلى اكتشاف الأخطاء في عنونة طبقة الإنترنت.

خوارزمية مجموع الفحص هي مكمل واحد 16 بت لمجموع مكمل واحد لجميع الكلمات 16 بت في المقطع. إذا كان المقطع يحتوي على عدد فردي من البايتات، يتم حشو البايت الأخير بأصفار لحساب مجموع الفحص.

**و. حالات الاتصال**

يتقدم اتصال TCP عبر سلسلة من الحالات:

1. **CLOSED (مغلق):** لا يوجد اتصال
2. **LISTEN (استماع):** انتظار طلب اتصال من مضيف بعيد
3. **SYN-SENT (SYN مُرسل):** تم إرسال SYN، انتظار SYN-ACK المطابق
4. **SYN-RECEIVED (SYN مُستلم):** تم استقبال SYN، تم إرسال SYN-ACK، انتظار ACK
5. **ESTABLISHED (مُنشأ):** الاتصال مفتوح، يمكن حدوث نقل البيانات
6. **FIN-WAIT-1 (انتظار FIN-1):** تم إرسال FIN، انتظار ACK أو FIN
7. **FIN-WAIT-2 (انتظار FIN-2):** تم استقبال ACK لـ FIN، انتظار FIN من البعيد
8. **CLOSE-WAIT (انتظار الإغلاق):** تم استقبال FIN، انتظار التطبيق للإغلاق
9. **CLOSING (إغلاق):** إغلاق متزامن، انتظار ACK لـ FIN
10. **LAST-ACK (ACK الأخير):** تم إرسال FIN بعد استقبال FIN، انتظار ACK
11. **TIME-WAIT (انتظار الوقت):** انتظار الشبكة لمسح المقاطع القديمة

حالة TIME-WAIT مهمة بشكل خاص. بعد استقبال FIN-ACK النهائي، يدخل الاتصال TIME-WAIT لضعف الحد الأقصى لعمر المقطع (2*MSL). يضمن ذلك انتهاء صلاحية المقاطع المتأخرة من الاتصال القديم قبل إمكانية إعادة استخدام نفس زوج المقابس.

**ز. استراتيجية إعادة الإرسال**

عند إرسال مقطع، يتم وضع نسخة في قائمة انتظار إعادة الإرسال ويبدأ مؤقت إعادة الإرسال. إذا تم استقبال إقرار قبل انتهاء صلاحية المؤقت، يتم إزالة المقطع من القائمة. إذا انتهى المؤقت، يتم إعادة إرسال المقطع ويبدأ مؤقت جديد.

يجب تعيين مهلة إعادة الإرسال (RTO) بناءً على وقت الرحلة ذهاباً وإياباً المرصود (RTT). النهج البسيط هو قياس RTT للمقاطع وتعيين RTO إلى مضاعف متوسط RTT. تستخدم التطبيقات الأكثر تطوراً تقديرات RTT المنعمة وقياسات التباين.

**ح. الخيارات**

توفر خيارات TCP قابلية التوسع. يتم وضع الخيارات بعد الرأس القياسي وقبل البيانات. كل خيار لديه حقل نوع، ومعظم الخيارات لديها حقل طول يليه بيانات خاصة بالخيار.

أمثلة على الخيارات تشمل:

- **نهاية قائمة الخيارات:** يحدد نهاية الخيارات
- **لا عملية:** يستخدم للمحاذاة
- **الحد الأقصى لحجم المقطع:** يعلن عن الحد الأقصى لحجم المقطع الذي يمكن للمرسل قبوله

تسمح الخيارات بتوسيع TCP بميزات جديدة مع الحفاظ على التوافق العكسي مع التطبيقات التي لا تتعرف على الخيارات الجديدة.

**ط. تعدد الإرسال**

يقوم TCP بمضاعفة اتصالات متعددة عبر عنوان إنترنت واحد باستخدام أرقام المنافذ. يحدد الجمع بين عنوان المصدر، ومنفذ المصدر، وعنوان الوجهة، ومنفذ الوجهة اتصالاً بشكل فريد.

تتيح هذه الرباعية لعمليات متعددة على نفس المضيف الاتصال في وقت واحد مع نفس المضيفات البعيدة أو مضيفات مختلفة. كما تتيح للخادم معالجة اتصالات متعددة من عملاء مختلفين، جميعهم يستخدمون نفس رقم المنفذ المعروف.

---

### Translation Notes

- **TCP Header Fields (حقول رأس TCP):**
  - Source Port (منفذ المصدر)
  - Destination Port (منفذ الوجهة)
  - Sequence Number (رقم التسلسل)
  - Acknowledgment Number (رقم الإقرار)
  - Data Offset (إزاحة البيانات)
  - Control Bits (بتات التحكم)
  - Window (النافذة)
  - Checksum (مجموع الفحص)
  - Urgent Pointer (مؤشر العاجل)
  - Options (الخيارات)
  - Padding (الحشو)

- **Control Flags (أعلام التحكم):**
  - URG (Urgent) - عاجل
  - ACK (Acknowledgment) - إقرار
  - PSH (Push) - دفع
  - RST (Reset) - إعادة تعيين
  - SYN (Synchronize) - مزامنة
  - FIN (Finish) - إنهاء

- **Connection States (حالات الاتصال):**
  All 11 states translated with clear Arabic equivalents

- **Key Technical Concepts:**
  - Initial Sequence Number (ISN) - رقم التسلسل الأولي
  - Retransmission Timeout (RTO) - مهلة إعادة الإرسال
  - Round-Trip Time (RTT) - وقت الرحلة ذهاباً وإياباً
  - Maximum Segment Lifetime (MSL) - الحد الأقصى لعمر المقطع
  - Pseudo-header (رأس زائف) - for checksum calculation
  - One's complement (مكمل واحد) - checksum algorithm

- **Window Management:**
  - Send/Receive pointers (مؤشرات الإرسال/الاستقبال)
  - Window size (حجم النافذة)
  - Cumulative acknowledgments (الإقرارات التراكمية)

- **Important Notes:**
  - Detailed specification requires precise technical translation
  - Bit-level fields and their sizes preserved
  - State machine transitions clearly described
  - Mathematical operations (checksums) explained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
