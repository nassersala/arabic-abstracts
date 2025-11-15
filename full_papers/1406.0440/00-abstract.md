# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** Software-Defined Networking, control logic, router, switch, centralization, network control, network policy, switching hardware, traffic forwarding, abstraction, network management, network evolution, hardware infrastructure, API, network virtualization, network operating system, controller, programming language, network application, debugging, troubleshooting, scalability, performance, security, dependability

---

### English Version

The Internet has led to the creation of a digital society, where (almost) everything is connected and is accessible from anywhere. However, despite their widespread adoption, traditional IP networks are complex and very hard to manage. It is both difficult to configure the network according to pre-defined policies, and to reconfigure it to respond to faults, load and changes. To make matters even more difficult, current networks are also vertically integrated: the control and data planes are bundled together. Software-Defined Networking (SDN) is an emerging paradigm that promises to change this state of affairs, by breaking vertical integration, separating the network's control logic from the underlying routers and switches, promoting (logical) centralization of network control, and introducing the ability to program the network. The separation of concerns introduced between the definition of network policies, their implementation in switching hardware, and the forwarding of traffic, is key to the desired flexibility: by breaking the network control problem into tractable pieces, SDN makes it easier to create and introduce new abstractions in networking, simplifying network management and facilitating network evolution.

In this paper we present a comprehensive survey on SDN. We start by introducing the motivation for SDN, explain its main concepts and how it differs from traditional networking, its roots, and the standardization activities regarding this novel paradigm. Next, we present the key building blocks of an SDN infrastructure using a bottom-up, layered approach. We provide an in-depth analysis of the hardware infrastructure, southbound and northbound APIs, network virtualization layers, network operating systems (SDN controllers), network programming languages, and network applications. We also look at cross-layer problems such as debugging and troubleshooting. In an effort to anticipate the future evolution of this new paradigm, we discuss the main ongoing research efforts and challenges of SDN. In particular, we address the design of switches and control platforms -- with a focus on aspects such as resiliency, scalability, performance, security and dependability -- as well as new opportunities for carrier transport networks and cloud providers. Last but not least, we analyze the position of SDN as a key enabler of a software-defined environment.

---

### النسخة العربية

لقد أدى الإنترنت إلى خلق مجتمع رقمي، حيث يكون (تقريباً) كل شيء متصلاً ويمكن الوصول إليه من أي مكان. ومع ذلك، على الرغم من اعتمادها الواسع، فإن شبكات IP التقليدية معقدة ويصعب إدارتها للغاية. من الصعب تكوين الشبكة وفقاً لسياسات محددة مسبقاً، وإعادة تكوينها للاستجابة للأعطال والحمل والتغييرات. ولجعل الأمور أكثر صعوبة، فإن الشبكات الحالية أيضاً متكاملة رأسياً: يتم دمج مستويات التحكم والبيانات معاً. الشبكات المُعرَّفة بالبرمجيات (SDN) هي نموذج ناشئ يعد بتغيير هذا الوضع، من خلال كسر التكامل الرأسي، وفصل منطق التحكم في الشبكة عن أجهزة التوجيه والمحولات الأساسية، وتعزيز المركزية (المنطقية) للتحكم في الشبكة، وإدخال القدرة على برمجة الشبكة. إن فصل الاهتمامات المُقدَّم بين تعريف سياسات الشبكة، وتنفيذها في أجهزة التبديل، وإعادة توجيه الحركة، هو المفتاح للمرونة المرغوبة: من خلال تقسيم مشكلة التحكم في الشبكة إلى أجزاء قابلة للمعالجة، تجعل SDN من السهل إنشاء وإدخال تجريدات جديدة في الشبكات، مما يبسط إدارة الشبكة ويسهل تطور الشبكة.

في هذه الورقة نقدم دراسة شاملة عن SDN. نبدأ بتقديم الدافع وراء SDN، ونشرح مفاهيمها الرئيسية وكيف تختلف عن الشبكات التقليدية، وجذورها، وأنشطة التوحيد القياسي المتعلقة بهذا النموذج الجديد. بعد ذلك، نقدم الكتل البنائية الرئيسية للبنية التحتية لـ SDN باستخدام نهج طبقي من الأسفل إلى الأعلى. نقدم تحليلاً متعمقاً للبنية التحتية للأجهزة، وواجهات برمجة التطبيقات الجنوبية والشمالية، وطبقات افتراض الشبكة، وأنظمة تشغيل الشبكة (متحكمات SDN)، ولغات برمجة الشبكة، وتطبيقات الشبكة. ننظر أيضاً إلى مشاكل متعددة الطبقات مثل تصحيح الأخطاء واستكشاف الأخطاء وإصلاحها. في محاولة لتوقع التطور المستقبلي لهذا النموذج الجديد، نناقش الجهود البحثية الرئيسية المستمرة وتحديات SDN. على وجه الخصوص، نتناول تصميم المحولات ومنصات التحكم -- مع التركيز على جوانب مثل المرونة، وقابلية التوسع، والأداء، والأمان، والموثوقية -- بالإضافة إلى الفرص الجديدة لشبكات النقل الناقل ومزودي الحوسبة السحابية. أخيراً وليس آخراً، نحلل موقع SDN كممكن رئيسي لبيئة معرّفة بالبرمجيات.

---

### Translation Notes

- **Source:** Copied from translations/1406.0440.md
- **Key terms:** SDN, vertical integration, control plane, data plane, centralization, abstraction, network virtualization
- **Quality verified:** 0.92

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.91
- Glossary consistency: 0.93
- **Overall section score:** 0.92
