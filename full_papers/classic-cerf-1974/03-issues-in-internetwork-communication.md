# Section III: Issues in Internetwork Communication
## القسم الثالث: قضايا التواصل بين الشبكات

**Section:** Issues in Internetwork Communication
**Translation Quality:** 0.86
**Glossary Terms Used:** addressing, fragmentation, reassembly, sequencing, retransmission, acknowledgment, timeout, routing, gateway, packet loss, duplication

---

### English Version

Several problems arise when attempting to interconnect diverse packet-switching networks:

**A. Addressing**

Each host and gateway in the internet must have a unique address. The address must identify both the network and the specific host within that network. We propose a hierarchical addressing scheme where an internet address consists of two parts: a NETWORK identifier and a HOST identifier within that network.

The network identifier is assigned by a central authority to ensure uniqueness across the internet. Within each network, local authorities assign host identifiers. This two-level hierarchy allows networks to manage their own address space while maintaining global uniqueness.

**B. Fragmentation and Reassembly**

Different networks may have different maximum packet sizes. When a gateway must forward a packet to a network with a smaller maximum packet size, it must fragment the packet into smaller pieces. Each fragment is transmitted as a separate internet packet with its own internet header.

The fragments must contain sufficient information to permit reassembly at the destination. We include a fragment identifier, fragment offset, and flags to indicate whether more fragments follow. The destination host is responsible for collecting all fragments and reassembling them in the correct order to reconstruct the original packet.

Fragmentation may occur at multiple gateways along the path. A fragment may itself be fragmented if it encounters a network with an even smaller maximum packet size. The reassembly process must handle arbitrary levels of fragmentation.

**C. Sequencing and Retransmission**

Packets may arrive out of order, be lost, or be duplicated during transmission. The TCP must detect these conditions and take corrective action.

Each byte of data is assigned a SEQUENCE NUMBER. The receiver uses these sequence numbers to detect missing data, reorder packets that arrive out of sequence, and discard duplicate packets. The sender maintains a retransmission queue containing copies of all transmitted but unacknowledged data.

When the receiver successfully receives data, it sends an ACKNOWLEDGMENT back to the sender indicating the sequence number of the next byte it expects to receive. If the sender does not receive an acknowledgment within a specified timeout period, it retransmits the data.

**D. Flow Control**

The receiver must have a mechanism to prevent the sender from transmitting data faster than the receiver can process it. We use a WINDOW mechanism for flow control.

The receiver advertises a WINDOW SIZE indicating the amount of data it is willing to accept. The sender must not send more data than the receiver's window allows. As the receiver processes data and frees buffer space, it updates the window size in subsequent acknowledgments.

The window mechanism serves two purposes: it prevents buffer overflow at the receiver, and it allows the receiver to control the rate of data transmission based on its processing capacity.

**E. Error Detection**

Transmission errors may corrupt packet contents. We include a CHECKSUM in each TCP segment to detect transmission errors. The checksum covers both the TCP header and the data portion.

When a receiver detects a checksum error, it discards the corrupted segment without acknowledging it. The sender's timeout mechanism will eventually trigger retransmission of the lost data.

**F. Routing**

Gateways must determine the appropriate path for forwarding packets toward their destination. Routing decisions are based on the network portion of the destination address.

Each gateway maintains a ROUTING TABLE that maps destination networks to next-hop gateways. The routing table may be configured statically or updated dynamically by routing protocols.

When a gateway receives a packet, it extracts the network identifier from the destination address, looks up the next hop in its routing table, and forwards the packet to the appropriate network interface. If no route exists, the gateway may send an error indication back to the source.

**G. Timeouts**

Timeouts are necessary for detecting lost packets and triggering retransmissions. However, setting appropriate timeout values is challenging in an internetwork environment where delays can vary significantly.

If timeouts are too short, unnecessary retransmissions waste network bandwidth. If timeouts are too long, the protocol responds slowly to packet loss, reducing throughput.

We propose that hosts measure the round-trip time to their correspondents and set timeout values based on observed delays. The timeout should be longer than the typical round-trip time but not so long as to cause excessive delays in loss recovery.

**H. Precedence and Security**

Different applications may have different requirements for service quality and security. The protocol should provide mechanisms to indicate the priority and security classification of data.

Higher precedence traffic may receive preferential treatment at gateways during congestion. Security mechanisms may include access control and encryption, though the basic protocol focuses on identifying security requirements rather than implementing specific security mechanisms.

---

### النسخة العربية

تظهر عدة مشاكل عند محاولة ربط شبكات تبديل الحزم المتنوعة:

**أ. العنونة**

يجب أن يكون لكل مضيف وبوابة في الإنترنت عنوان فريد. يجب أن يحدد العنوان كلاً من الشبكة والمضيف المحدد داخل تلك الشبكة. نقترح مخطط عنونة هرمياً حيث يتكون عنوان الإنترنت من جزأين: معرّف الشبكة (NETWORK) ومعرّف المضيف (HOST) داخل تلك الشبكة.

يتم تعيين معرّف الشبكة بواسطة سلطة مركزية لضمان التفرد عبر الإنترنت. داخل كل شبكة، تقوم السلطات المحلية بتعيين معرّفات المضيف. يسمح هذا التسلسل الهرمي ذو المستويين للشبكات بإدارة فضاء العناوين الخاص بها مع الحفاظ على التفرد العالمي.

**ب. التجزئة وإعادة التجميع**

قد يكون للشبكات المختلفة أحجام حزم قصوى مختلفة. عندما يجب على البوابة إرسال حزمة إلى شبكة ذات حجم حزمة أقصى أصغر، يجب عليها تجزئة الحزمة إلى قطع أصغر. يتم إرسال كل جزء كحزمة إنترنت منفصلة مع رأس الإنترنت الخاص بها.

يجب أن تحتوي الأجزاء على معلومات كافية للسماح بإعادة التجميع في الوجهة. نقوم بتضمين معرّف الجزء، وإزاحة الجزء، وأعلام للإشارة إلى ما إذا كانت هناك أجزاء أخرى تتبع. المضيف الوجهة مسؤول عن جمع جميع الأجزاء وإعادة تجميعها بالترتيب الصحيح لإعادة بناء الحزمة الأصلية.

قد تحدث التجزئة في بوابات متعددة على طول المسار. قد يتم تجزئة الجزء نفسه إذا واجه شبكة ذات حجم حزمة أقصى أصغر. يجب أن تتعامل عملية إعادة التجميع مع مستويات تجزئة عشوائية.

**ج. التسلسل وإعادة الإرسال**

قد تصل الحزم خارج الترتيب، أو تُفقد، أو تتكرر أثناء النقل. يجب أن يكتشف TCP هذه الحالات ويتخذ إجراءً تصحيحياً.

يتم تعيين رقم تسلسلي (SEQUENCE NUMBER) لكل بايت من البيانات. يستخدم المستقبل أرقام التسلسل هذه لاكتشاف البيانات المفقودة، وإعادة ترتيب الحزم التي تصل خارج التسلسل، وتجاهل الحزم المكررة. يحتفظ المرسل بقائمة انتظار لإعادة الإرسال تحتوي على نسخ من جميع البيانات المرسلة ولكن غير المعترف بها.

عندما يستقبل المستقبل البيانات بنجاح، يرسل إقراراً (ACKNOWLEDGMENT) إلى المرسل يشير إلى رقم التسلسل للبايت التالي الذي يتوقع استقباله. إذا لم يستقبل المرسل إقراراً خلال فترة مهلة محددة، فإنه يعيد إرسال البيانات.

**د. التحكم في التدفق**

يجب أن يكون لدى المستقبل آلية لمنع المرسل من إرسال البيانات بشكل أسرع من قدرة المستقبل على معالجتها. نستخدم آلية النافذة (WINDOW) للتحكم في التدفق.

يعلن المستقبل عن حجم النافذة (WINDOW SIZE) مشيراً إلى كمية البيانات التي يرغب في قبولها. يجب ألا يرسل المرسل بيانات أكثر مما تسمح به نافذة المستقبل. مع قيام المستقبل بمعالجة البيانات وتحرير مساحة المخزن المؤقت، يقوم بتحديث حجم النافذة في الإقرارات اللاحقة.

تخدم آلية النافذة غرضين: فهي تمنع تجاوز المخزن المؤقت في المستقبل، وتسمح للمستقبل بالتحكم في معدل نقل البيانات بناءً على قدرته على المعالجة.

**هـ. الكشف عن الأخطاء**

قد تفسد أخطاء النقل محتويات الحزمة. نقوم بتضمين مجموع فحص (CHECKSUM) في كل مقطع TCP لاكتشاف أخطاء النقل. يغطي مجموع الفحص كلاً من رأس TCP وجزء البيانات.

عندما يكتشف المستقبل خطأ في مجموع الفحص، يتجاهل المقطع التالف دون الإقرار به. ستؤدي آلية المهلة الزمنية للمرسل في النهاية إلى إعادة إرسال البيانات المفقودة.

**و. التوجيه**

يجب أن تحدد البوابات المسار المناسب لإرسال الحزم نحو وجهتها. تعتمد قرارات التوجيه على جزء الشبكة من عنوان الوجهة.

تحتفظ كل بوابة بجدول توجيه (ROUTING TABLE) يربط شبكات الوجهة ببوابات القفزة التالية. قد يتم تكوين جدول التوجيه بشكل ثابت أو يتم تحديثه ديناميكياً بواسطة بروتوكولات التوجيه.

عندما تستقبل البوابة حزمة، تستخرج معرّف الشبكة من عنوان الوجهة، وتبحث عن القفزة التالية في جدول التوجيه، وتُرسل الحزمة إلى واجهة الشبكة المناسبة. إذا لم يكن هناك مسار موجود، قد ترسل البوابة إشارة خطأ إلى المصدر.

**ز. المهلات الزمنية**

المهلات الزمنية ضرورية لاكتشاف الحزم المفقودة وتفعيل إعادة الإرسال. ومع ذلك، فإن تحديد قيم المهلة المناسبة أمر صعب في بيئة الإنترنت حيث يمكن أن تتباين التأخيرات بشكل كبير.

إذا كانت المهلات قصيرة جداً، فإن عمليات إعادة الإرسال غير الضرورية تهدر عرض النطاق الترددي للشبكة. إذا كانت المهلات طويلة جداً، يستجيب البروتوكول ببطء لفقدان الحزم، مما يقلل من الإنتاجية.

نقترح أن تقيس المضيفات وقت الرحلة ذهاباً وإياباً إلى مراسليها وتحدد قيم المهلة بناءً على التأخيرات المرصودة. يجب أن تكون المهلة أطول من وقت الرحلة ذهاباً وإياباً النموذجي ولكن ليست طويلة جداً لدرجة تسبب تأخيرات مفرطة في استرداد الفقدان.

**ح. الأولوية والأمان**

قد يكون للتطبيقات المختلفة متطلبات مختلفة لجودة الخدمة والأمان. يجب أن يوفر البروتوكول آليات للإشارة إلى أولوية وتصنيف أمان البيانات.

قد تحصل حركة المرور ذات الأولوية الأعلى على معاملة تفضيلية في البوابات أثناء الازدحام. قد تتضمن آليات الأمان التحكم في الوصول والتشفير، على الرغم من أن البروتوكول الأساسي يركز على تحديد متطلبات الأمان بدلاً من تنفيذ آليات أمان محددة.

---

### Translation Notes

- **Key technical issues covered:**
  1. Addressing (العنونة) - hierarchical scheme
  2. Fragmentation/Reassembly (التجزئة/إعادة التجميع) - handling different MTUs
  3. Sequencing/Retransmission (التسلسل/إعادة الإرسال) - reliability
  4. Flow Control (التحكم في التدفق) - window mechanism
  5. Error Detection (الكشف عن الأخطاء) - checksums
  6. Routing (التوجيه) - path determination
  7. Timeouts (المهلات الزمنية) - loss detection
  8. Precedence/Security (الأولوية/الأمان) - QoS and security

- **New terminology introduced:**
  - Sequence number (رقم تسلسلي) - fundamental to TCP reliability
  - Acknowledgment (إقرار) - confirmation of receipt
  - Window size (حجم النافذة) - flow control mechanism
  - Checksum (مجموع فحص) - error detection
  - Routing table (جدول التوجيه) - forwarding information base
  - Fragment offset (إزاحة الجزء) - position within original packet
  - Round-trip time (وقت الرحلة ذهاباً وإياباً) - RTT measurement
  - Next hop (القفزة التالية) - routing concept

- **Important concepts:**
  - Two-level hierarchical addressing (network + host)
  - Recursive fragmentation possible
  - Byte-level sequencing
  - Window-based flow control
  - Adaptive timeout based on RTT measurement

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
