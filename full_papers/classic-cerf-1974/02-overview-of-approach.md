# Section II: Overview of Approach
## القسم الثاني: نظرة عامة على النهج

**Section:** Overview of Approach
**Translation Quality:** 0.87
**Glossary Terms Used:** gateway, packet, network, host, protocol, TCP, header, destination, source, fragmentation, reassembly

---

### English Version

The goal of the protocol design is to allow various networks to be interconnected so that they appear as one logical network to the processes using them. To permit this, we assume the existence of computers, called GATEWAYS, which serve as the interface between networks. A GATEWAY has interfaces to two or more packet-switching networks and is capable of sending and receiving packets from these networks.

In its simplest form, a gateway receives a packet from one network and passes it through to another network. When networks differ in the size of packets they can handle, the gateway may fragment a large packet into smaller pieces and transmit these individually to the next network. At the destination, the fragments are reassembled into the original packet.

We envision a communications architecture made up of PROCESSES which communicate through a process level protocol. Processes are supported by HOSTS, and hosts are embedded in NETWORKS. A NETWORK is connected to other networks through GATEWAYS, which appear to a packet-switching network to be ordinary hosts.

The transmission path between processes may traverse several networks and gateways. We use the term INTERNET to denote the total communications environment created by interconnecting networks through gateways. The internet provides a packet transportation service between hosts. We assume the availability of a LOCAL NETWORK PROTOCOL which provides communication services within each individual packet-switching network.

The TRANSMISSION CONTROL PROTOCOL (TCP) is a host-to-host protocol which provides the following services:

1. **Connection management:** Establishes and terminates connections between processes running in different hosts.

2. **Reliable delivery:** Ensures that data is delivered accurately and in order, recovering from transmission errors, lost packets, and duplicate packets.

3. **Multiplexing:** Allows multiple connections to exist simultaneously between processes in the same pair of hosts.

4. **Flow control:** Prevents a fast sender from overwhelming a slow receiver.

5. **Precedence and security:** Provides mechanisms for indicating the priority and security classification of data.

The basic approach is to encapsulate data from processes in SEGMENTS, which are then transmitted in one or more INTERNET PACKETS. An internet packet consists of an INTERNET HEADER and a DATA portion. The internet header contains addressing and control information, while the data portion contains the TCP segment.

The GATEWAY is responsible for routing internet packets from source to destination. When a gateway receives a packet, it examines the destination address and determines which network to forward the packet to. If the packet is too large for the next network, the gateway fragments it into smaller packets, each with its own internet header.

---

### النسخة العربية

الهدف من تصميم البروتوكول هو السماح بربط شبكات متنوعة بحيث تظهر كشبكة منطقية واحدة للعمليات التي تستخدمها. للسماح بذلك، نفترض وجود أجهزة كمبيوتر، تسمى البوابات (GATEWAYS)، والتي تعمل كواجهة بين الشبكات. تحتوي البوابة على واجهات لشبكتين أو أكثر من شبكات تبديل الحزم وهي قادرة على إرسال واستقبال الحزم من هذه الشبكات.

في أبسط أشكالها، تستقبل البوابة حزمة من شبكة واحدة وتمررها إلى شبكة أخرى. عندما تختلف الشبكات في حجم الحزم التي يمكنها التعامل معها، قد تقوم البوابة بتجزئة حزمة كبيرة إلى قطع أصغر وإرسالها بشكل فردي إلى الشبكة التالية. في الوجهة، يتم إعادة تجميع الأجزاء إلى الحزمة الأصلية.

نتصور معمارية اتصالات تتكون من عمليات (PROCESSES) تتواصل من خلال بروتوكول على مستوى العملية. يتم دعم العمليات بواسطة المضيفات (HOSTS)، والمضيفات مضمنة في الشبكات (NETWORKS). ترتبط الشبكة بشبكات أخرى من خلال البوابات (GATEWAYS)، والتي تظهر لشبكة تبديل الحزم كمضيفات عادية.

قد يمر مسار النقل بين العمليات عبر عدة شبكات وبوابات. نستخدم مصطلح الإنترنت (INTERNET) للدلالة على بيئة الاتصالات الكلية التي تم إنشاؤها بربط الشبكات من خلال البوابات. يوفر الإنترنت خدمة نقل الحزم بين المضيفات. نفترض توفر بروتوكول شبكة محلية (LOCAL NETWORK PROTOCOL) الذي يوفر خدمات الاتصال داخل كل شبكة تبديل حزم فردية.

بروتوكول التحكم في النقل (TCP) هو بروتوكول من مضيف إلى مضيف يوفر الخدمات التالية:

1. **إدارة الاتصال:** إنشاء وإنهاء الاتصالات بين العمليات التي تعمل في مضيفات مختلفة.

2. **التسليم الموثوق:** يضمن تسليم البيانات بدقة وبالترتيب، مع التعافي من أخطاء النقل، والحزم المفقودة، والحزم المكررة.

3. **تعدد الإرسال:** يسمح بوجود اتصالات متعددة في وقت واحد بين العمليات في نفس زوج المضيفات.

4. **التحكم في التدفق:** يمنع المرسل السريع من إغراق المستقبل البطيء.

5. **الأولوية والأمان:** يوفر آليات للإشارة إلى أولوية وتصنيف أمان البيانات.

النهج الأساسي هو تغليف البيانات من العمليات في مقاطع (SEGMENTS)، والتي يتم نقلها بعد ذلك في حزمة أو أكثر من حزم الإنترنت (INTERNET PACKETS). تتكون حزمة الإنترنت من رأس الإنترنت (INTERNET HEADER) وجزء البيانات (DATA). يحتوي رأس الإنترنت على معلومات العنونة والتحكم، بينما يحتوي جزء البيانات على مقطع TCP.

البوابة مسؤولة عن توجيه حزم الإنترنت من المصدر إلى الوجهة. عندما تستقبل البوابة حزمة، تفحص عنوان الوجهة وتحدد الشبكة التي سيتم إرسال الحزمة إليها. إذا كانت الحزمة كبيرة جداً بالنسبة للشبكة التالية، تقوم البوابة بتجزئتها إلى حزم أصغر، كل منها مع رأس الإنترنت الخاص بها.

---

### Translation Notes

- **Key architectural concepts introduced:**
  - GATEWAY (البوابة) - intermediate system connecting networks
  - HOST (المضيف) - end system running processes
  - PROCESS (العملية) - program or application
  - SEGMENT (المقطع) - TCP unit of data
  - INTERNET PACKET (حزمة الإنترنت) - fundamental unit of internetwork transmission
  - INTERNET HEADER (رأس الإنترنت) - addressing and control information

- **Key operations:**
  - Fragmentation (التجزئة) - breaking large packets into smaller pieces
  - Reassembly (إعادة التجميع) - reconstructing original packet from fragments
  - Encapsulation (التغليف) - wrapping data in protocol headers
  - Routing (التوجيه) - determining path through network

- **TCP services listed:**
  1. Connection management (إدارة الاتصال)
  2. Reliable delivery (التسليم الموثوق)
  3. Multiplexing (تعدد الإرسال)
  4. Flow control (التحكم في التدفق)
  5. Precedence and security (الأولوية والأمان)

- **Terminology notes:**
  - "Internet" used here as generic term for network of networks
  - Capital letters used in original to emphasize new technical terms
  - Clear layered architecture: Process → Host → Network → Gateway → Internet

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
