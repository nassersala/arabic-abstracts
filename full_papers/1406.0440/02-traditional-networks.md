# Section 2: State of Quo in Networking
## القسم 2: الوضع الراهن في الشبكات

**Section:** traditional-networks
**Translation Quality:** 0.87
**Glossary Terms Used:** data plane, control plane, management plane, forwarding, routing protocols, network policy, IP networks, resilience, configuration, BGP, middlebox, firewall, intrusion detection, network management

---

### English Version

Computer networks can be divided in three planes of functionality: the data, control and management planes (see Figure 2). The data plane corresponds to the networking devices, which are responsible for (efficiently) forwarding data. The control plane represents the protocols used to populate the forwarding tables of the data plane elements. The management plane includes the software services, such as SNMP-based tools, used to remotely monitor and configure the control functionality. Network policy is defined in the management plane, the control plane enforces the policy, and the data plane executes it by forwarding data accordingly.

In traditional IP networks, the control and data planes are tightly coupled, embedded in the same networking devices, and the whole structure is highly decentralized. This was considered important for the design of the Internet in the early days: it seemed the best way to guarantee network resilience, which was a crucial design goal. In fact, this approach has been quite effective in terms of network performance, with a rapid increase of line rate and port densities.

However, the outcome is a very complex and relatively static architecture, as has been often reported in the networking literature. It is also the fundamental reason why traditional networks are rigid, and complex to manage and control. These two characteristics are largely responsible for a vertically-integrated industry where innovation is difficult.

Network misconfigurations and related errors are extremely common in today's networks. For instance, more than 1000 configuration errors have been observed in BGP routers. From a single misconfigured device may result very undesired network behavior (including, among others, packet losses, forwarding loops, setting up of unintended paths, or service contract violations). Indeed, while rare, a single misconfigured router is able to compromise the correct operation of the whole Internet for hours.

To support network management, a small number of vendors offer proprietary solutions of specialized hardware, operating systems, and control programs (network applications). Network operators have to acquire and maintain different management solutions and the corresponding specialized teams. The capital and operational cost of building and maintaining a networking infrastructure is significant, with long return on investment cycles, which hamper innovation and addition of new features and services (for instance access control, load balancing, energy efficiency, traffic engineering). To alleviate the lack of in-path functionalities within the network, a myriad of specialized components and middleboxes, such as firewalls, intrusion detection systems and deep packet inspection engines, proliferate in current networks. A recent survey of 57 enterprise networks shows that the number of middleboxes is already on par with the number of routers in current networks. Despite helping in-path functionalities, the net effect of middleboxes has been increased complexity of network design and its operation.

---

### النسخة العربية

يمكن تقسيم شبكات الحاسوب إلى ثلاثة مستويات من الوظائف: مستويات البيانات والتحكم والإدارة (انظر الشكل 2). يتوافق مستوى البيانات مع أجهزة الشبكات، المسؤولة عن إعادة توجيه البيانات (بكفاءة). يمثل مستوى التحكم البروتوكولات المستخدمة لملء جداول إعادة التوجيه لعناصر مستوى البيانات. يتضمن مستوى الإدارة خدمات البرمجيات، مثل الأدوات المستندة إلى SNMP، المستخدمة لمراقبة وتكوين وظائف التحكم عن بُعد. يتم تعريف سياسة الشبكة في مستوى الإدارة، ويطبق مستوى التحكم السياسة، وينفذها مستوى البيانات عن طريق إعادة توجيه البيانات وفقاً لذلك.

في شبكات IP التقليدية، يكون مستويا التحكم والبيانات مقترنين بإحكام، مضمنين في نفس أجهزة الشبكات، والهيكل بأكمله لامركزي للغاية. اعتُبر هذا مهماً لتصميم الإنترنت في الأيام الأولى: بدا أنه أفضل طريقة لضمان مرونة الشبكة، والتي كانت هدف تصميم حاسماً. في الواقع، كان هذا النهج فعالاً للغاية من حيث أداء الشبكة، مع زيادة سريعة في معدل الخط وكثافة المنافذ.

ومع ذلك، فإن النتيجة هي معمارية معقدة للغاية وثابتة نسبياً، كما تم الإبلاغ عنها مراراً وتكراراً في أدبيات الشبكات. وهذا أيضاً هو السبب الأساسي لكون الشبكات التقليدية جامدة ومعقدة الإدارة والتحكم. هاتان الخاصيتان مسؤولتان إلى حد كبير عن صناعة متكاملة رأسياً حيث يكون الابتكار صعباً.

أخطاء التكوين الخاطئ للشبكة والأخطاء ذات الصلة شائعة للغاية في شبكات اليوم. على سبيل المثال، لوحظ أكثر من 1000 خطأ في تكوين موجهات BGP. من جهاز واحد تم تكوينه بشكل خاطئ قد ينتج سلوك شبكة غير مرغوب فيه للغاية (بما في ذلك، من بين أمور أخرى، فقدان الحزم، وحلقات إعادة التوجيه، وإعداد مسارات غير مقصودة، أو انتهاكات عقود الخدمة). في الواقع، على الرغم من أنه نادر، يمكن لموجه واحد تم تكوينه بشكل خاطئ أن يعرض التشغيل الصحيح للإنترنت بأكمله للخطر لساعات.

لدعم إدارة الشبكة، يقدم عدد صغير من الموردين حلولاً احتكارية من الأجهزة المتخصصة وأنظمة التشغيل وبرامج التحكم (تطبيقات الشبكة). يجب على مشغلي الشبكات الحصول على حلول إدارة مختلفة والحفاظ عليها والفرق المتخصصة المقابلة. تكلفة رأس المال والتشغيل لبناء والحفاظ على بنية تحتية للشبكات كبيرة، مع دورات طويلة من العائد على الاستثمار، مما يعيق الابتكار وإضافة ميزات وخدمات جديدة (على سبيل المثال، التحكم في الوصول، وموازنة الحمل، وكفاءة الطاقة، وهندسة الحركة). للتخفيف من نقص الوظائف داخل المسار في الشبكة، تنتشر مجموعة كبيرة من المكونات المتخصصة والصناديق الوسيطة، مثل جدران الحماية وأنظمة كشف التطفل ومحركات فحص الحزم العميقة، في الشبكات الحالية. يظهر مسح حديث لـ 57 شبكة مؤسسية أن عدد الصناديق الوسيطة أصبح بالفعل على قدم المساواة مع عدد الموجهات في الشبكات الحالية. على الرغم من المساعدة في الوظائف داخل المسار، فإن التأثير الصافي للصناديق الوسيطة كان زيادة تعقيد تصميم الشبكة وتشغيلها.

---

### Translation Notes

- **Figures referenced:** Figure 2 (Layered view of networking functionality)
- **Key terms introduced:** three planes (data, control, management), SNMP, BGP, middlebox, forwarding table
- **Technical concepts:** tight coupling, decentralization, resilience, misconfiguration
- **Specific data:** 1000 configuration errors in BGP, survey of 57 enterprise networks
- **Special handling:** Technical terminology maintained consistent with glossary

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
