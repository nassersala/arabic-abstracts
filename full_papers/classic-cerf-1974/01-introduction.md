# Section I: Introduction
## القسم الأول: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** packet switching, network, gateway, host, protocol, communication, transmission, addressing, routing

---

### English Version

In the last few years considerable work has been done on the development of packet switching technology. A number of packet switching networks now exist throughout the world, including the ARPANET in the United States, CYCLADES in France, NPL in the United Kingdom, and several others in Japan and Europe.

These networks differ in many respects: their geographical location, performance characteristics (speed, delay), the sizes of packets which can be handled, and the techniques used for handling addressing, routing, and transmission priorities. Furthermore, at the host level, programs may use widely different techniques for formatting and controlling exchanges of information.

Despite these differences, we wish to develop a common protocol capable of operating in diverse packet-switched network environments. The goal is to develop a set of general-purpose protocols which can accommodate present and future network technologies. We refer to the resulting communications environment as an "internet" (i.e., a network of networks).

In this paper, we describe a protocol which supports the sharing of resources among the constituent networks. The protocol provides for variation in individual network packet sizes, transmission failures, sequencing, end-to-end error checking, and the creation and destruction of process-to-process connections. Some implementation issues are considered, and problems such as internetwork routing, accounting, and timeouts are exposed.

The protocol we describe permits the interconnection of existing networks without requiring modification of the individual networks, and is host-to-host oriented. The basic function of the protocol is to provide a standard communication environment for processes running in various hosts. Since processes do not share memory, some form of interprocess communication facility is needed. The protocol forms the foundation for a standard interface between processes and networks.

---

### النسخة العربية

في السنوات القليلة الماضية، تم إنجاز عمل كبير في تطوير تقنية تبديل الحزم. يوجد حالياً عدد من شبكات تبديل الحزم في جميع أنحاء العالم، بما في ذلك ARPANET في الولايات المتحدة، وCYCLADES في فرنسا، وNPL في المملكة المتحدة، والعديد من الشبكات الأخرى في اليابان وأوروبا.

تختلف هذه الشبكات في نواحٍ عديدة: موقعها الجغرافي، وخصائص الأداء (السرعة، والتأخير)، وأحجام الحزم التي يمكن التعامل معها، والتقنيات المستخدمة للتعامل مع العنونة والتوجيه وأولويات النقل. علاوة على ذلك، على مستوى المضيف، قد تستخدم البرامج تقنيات مختلفة جداً لتنسيق وتحكم تبادل المعلومات.

على الرغم من هذه الاختلافات، نرغب في تطوير بروتوكول مشترك قادر على العمل في بيئات شبكات تبديل الحزم المتنوعة. الهدف هو تطوير مجموعة من البروتوكولات ذات الأغراض العامة التي يمكنها استيعاب تقنيات الشبكات الحالية والمستقبلية. نشير إلى بيئة الاتصالات الناتجة باسم "إنترنت" (أي، شبكة من الشبكات).

في هذه الورقة، نصف بروتوكولاً يدعم مشاركة الموارد بين الشبكات المكونة. يوفر البروتوكول إمكانية التعامل مع التباين في أحجام حزم الشبكات الفردية، وفشل النقل، والتسلسل، والفحص الشامل للأخطاء من طرف إلى طرف، وإنشاء وإتلاف الاتصالات بين العمليات. تُؤخذ بعض قضايا التطبيق في الاعتبار، وتُكشف مشاكل مثل التوجيه بين الشبكات والمحاسبة والمهلات الزمنية.

البروتوكول الذي نصفه يسمح بالربط بين الشبكات الموجودة دون الحاجة إلى تعديل الشبكات الفردية، وهو موجّه من مضيف إلى مضيف. الوظيفة الأساسية للبروتوكول هي توفير بيئة اتصالات موحدة للعمليات التي تعمل في مضيفات مختلفة. نظراً لأن العمليات لا تشترك في الذاكرة، فإن هناك حاجة إلى نوع من آلية الاتصال بين العمليات. يشكل البروتوكول الأساس لواجهة موحدة بين العمليات والشبكات.

---

### Translation Notes

- **Key historical networks:** ARPANET, CYCLADES, NPL preserved as proper nouns
- **Key terms introduced:**
  - internet (إنترنت) - first use of this term with lowercase 'i' meaning "network of networks"
  - host (مضيف) - computer connected to network
  - gateway (بوابة) - device connecting networks
  - end-to-end (من طرف إلى طرف) - crucial concept in Internet architecture
  - interprocess communication (الاتصال بين العمليات)

- **Technical concepts:**
  - Packet switching networks (شبكات تبديل الحزم)
  - Host-to-host oriented (موجّه من مضيف إلى مضيف)
  - Process-to-process connections (الاتصالات بين العمليات)

- **Historical significance:** This section introduces the concept of "internet" (lowercase) as a network of networks, which later became the Internet (capitalized)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
