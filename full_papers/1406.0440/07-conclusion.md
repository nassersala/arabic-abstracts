# Section 7: Conclusion
## القسم 7: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** traditional networks, vertical integration, vendor lock-in, SDN, programmability, southbound interface, control plane, data plane, decoupling, logical centralization, controller, network operating system, paradigm shift, layered approach

---

### English Version

Traditional networks are complex and hard to manage. One of the reasons is that the control and data planes are vertically integrated and vendor specific. Another, concurring reason, is that typical networking devices are also tightly tied to line products and versions. In other words, each line of product may have its own particular configuration and management interfaces, implying long cycles for producing product updates (e.g., new firmware) or upgrades (e.g., new versions of the devices). All this has given rise to vendor lock-in problems for network infrastructure owners, as well as posing severe restrictions to change and innovation.

Software-Defined Networking (SDN) created an opportunity for solving these long-standing problems. Some of the key ideas of SDN are the introduction of dynamic programmability in forwarding devices through open southbound interfaces, the decoupling of the control and data plane, and the global view of the network by logical centralization of the "network brain". While data plane elements became dumb, but highly efficient and programmable packet forwarding devices, the control plane elements are now represented by a single entity, the controller or network operating system. Applications implementing the network logic run on top of the controller and are much easier to develop and deploy when compared to traditional networks. Given the global view, consistency of policies is straightforward to enforce. SDN represents a major paradigm shift in the development and evolution of networks, introducing a new pace of innovation in networking infrastructure.

In spite of recent and interesting attempts to survey this new chapter in the history of networks, the literature was still lacking, to the best of our knowledge, a single extensive and comprehensive overview of the building blocks, concepts, and challenges of SDNs. Trying to address this gap, the present paper used a layered approach to methodically dissect the state of the art in terms of concepts, ideas and components of software-defined networking, covering a broad range of existing solutions, as well as future directions.

We started by comparing this new paradigm with traditional networks and discussing how academy and industry helped shape software-defined networking. Following a bottom-up approach, we provided an in-depth overview of what we consider the eight fundamental facets of the SDN problem: 1) hardware infrastructure, 2) southbound interfaces, 3) network virtualization (hypervisor layer between the forwarding devices and the network operating systems), 4) network operating systems (SDN controllers and control platforms), 5) northbound interfaces (common programming abstractions offered to network applications), 6) virtualization using slicing techniques provided by special purpose libraries and/or programming languages and compilers, 7) network programming languages, and finally, 8) network applications.

SDN has successfully managed to pave the way towards a next generation networking, spawning an innovative research and development environment, promoting advances in several areas: switch and controller platform design, evolution of scalability and performance of devices and architectures, promotion of security and dependability.

We will continue to witness extensive activity around SDN in the near future. Emerging topics requiring further research are, for example: the migration path to SDN, extending SDN towards carrier transport networks, realization of the network-as-a-service cloud computing paradigm, or software-defined environments (SDE). As such, we would like to receive feedback from the networking/SDN community as this novel paradigm evolves, to make this a "live document" that gets updated and improved based on the community feedback. We have set up a github page for this purpose, and we invite our readers to join us in this communal effort.

---

### النسخة العربية

الشبكات التقليدية معقدة ويصعب إدارتها. أحد الأسباب هو أن مستويي التحكم والبيانات متكاملان رأسياً وخاصان بالمورّد. سبب آخر متزامن هو أن أجهزة الشبكات النموذجية مرتبطة أيضاً بإحكام بخطوط الإنتاج والإصدارات. بعبارة أخرى، قد يكون لكل خط من الإنتاج واجهات تكوين وإدارة خاصة به، مما يعني دورات طويلة لإنتاج تحديثات المنتج (على سبيل المثال، البرامج الثابتة الجديدة) أو الترقيات (على سبيل المثال، إصدارات جديدة من الأجهزة). كل هذا أدى إلى مشاكل الارتباط بالمورّد لأصحاب البنية التحتية للشبكة، بالإضافة إلى فرض قيود شديدة على التغيير والابتكار.

أوجدت الشبكات المُعرَّفة بالبرمجيات (SDN) فرصة لحل هذه المشكلات طويلة الأمد. بعض الأفكار الرئيسية لـ SDN هي إدخال قابلية البرمجة الديناميكية في أجهزة إعادة التوجيه من خلال الواجهات الجنوبية المفتوحة، وفصل مستوى التحكم والبيانات، والعرض العالمي للشبكة من خلال المركزية المنطقية لـ "دماغ الشبكة". بينما أصبحت عناصر مستوى البيانات غبية، لكنها أجهزة إعادة توجيه حزم فعالة للغاية وقابلة للبرمجة، يتم الآن تمثيل عناصر مستوى التحكم بواسطة كيان واحد، المتحكم أو نظام تشغيل الشبكة. التطبيقات التي تنفذ منطق الشبكة تعمل على قمة المتحكم وأسهل بكثير في التطوير والنشر مقارنة بالشبكات التقليدية. بالنظر إلى العرض العالمي، فإن تطبيق اتساق السياسات أمر مباشر. تمثل SDN تحولاً نموذجياً رئيسياً في تطوير وتطور الشبكات، مما يقدم وتيرة جديدة للابتكار في البنية التحتية للشبكات.

على الرغم من المحاولات الأخيرة والمثيرة للاهتمام لمسح هذا الفصل الجديد في تاريخ الشبكات، كانت الأدبيات لا تزال تفتقر، على حد علمنا، إلى نظرة عامة واسعة وشاملة واحدة للكتل البنائية والمفاهيم والتحديات الخاصة بـ SDN. في محاولة لمعالجة هذه الفجوة، استخدمت هذه الورقة نهجاً طبقياً لتشريح حالة الفن منهجياً من حيث المفاهيم والأفكار ومكونات الشبكات المُعرَّفة بالبرمجيات، بما يغطي مجموعة واسعة من الحلول الموجودة، بالإضافة إلى الاتجاهات المستقبلية.

بدأنا بمقارنة هذا النموذج الجديد مع الشبكات التقليدية ومناقشة كيف ساعدت الأكاديمية والصناعة في تشكيل الشبكات المُعرَّفة بالبرمجيات. باتباع نهج من الأسفل إلى الأعلى، قدمنا نظرة عامة متعمقة لما نعتبره الجوانب الثمانية الأساسية لمشكلة SDN: 1) البنية التحتية للأجهزة، 2) الواجهات الجنوبية، 3) افتراض الشبكة (طبقة المحاكي الافتراضي بين أجهزة إعادة التوجيه وأنظمة تشغيل الشبكة)، 4) أنظمة تشغيل الشبكة (متحكمات SDN ومنصات التحكم)، 5) الواجهات الشمالية (التجريدات البرمجية المشتركة المقدمة لتطبيقات الشبكة)، 6) الافتراض باستخدام تقنيات التقسيم المقدمة من مكتبات خاصة و/أو لغات برمجة ومترجمات، 7) لغات برمجة الشبكة، وأخيراً، 8) تطبيقات الشبكة.

نجحت SDN في تمهيد الطريق نحو شبكات الجيل التالي، مما أدى إلى ظهور بيئة بحث وتطوير مبتكرة، وتعزيز التقدم في عدة مجالات: تصميم منصات المحول والمتحكم، وتطور قابلية التوسع والأداء للأجهزة والمعماريات، وتعزيز الأمان والموثوقية.

سنستمر في مشاهدة نشاط واسع حول SDN في المستقبل القريب. الموضوعات الناشئة التي تتطلب مزيداً من البحث هي، على سبيل المثال: مسار الهجرة إلى SDN، وتوسيع SDN نحو شبكات النقل الناقل، وتحقيق نموذج الحوسبة السحابية للشبكة كخدمة، أو البيئات المُعرَّفة بالبرمجيات (SDE). على هذا النحو، نود أن نتلقى تعليقات من مجتمع الشبكات/SDN مع تطور هذا النموذج الجديد، لجعل هذه "وثيقة حية" يتم تحديثها وتحسينها بناءً على تعليقات المجتمع. لقد أنشأنا صفحة github لهذا الغرض، وندعو قراءنا للانضمام إلينا في هذا الجهد المجتمعي.

---

### Translation Notes

- **Key Messages:**
  - Traditional networks: complex, vendor-locked, slow innovation
  - SDN solution: programmability, decoupling, centralization, global view
  - Survey contribution: comprehensive layered approach covering 8 facets
  - Future directions: migration, carrier networks, NaaS, SDEs
  - Community engagement: living document, github collaboration
- **Major Achievements:** Paradigm shift in networking, innovation pace, research environment
- **Eight SDN Layers Reviewed:** Infrastructure → Southbound → Virtualization → NOS → Northbound → Language virtualization → Programming languages → Applications
- **Research Areas Advanced:** Switch/controller design, scalability, performance, security, dependability
- **Future Topics:** Migration paths, carrier-grade, cloud computing, SDEs
- **Special Note:** Invitation for community feedback and collaboration

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
