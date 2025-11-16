# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** domain, hierarchical, distributed system, caching, network, database, protocol, implementation

---

### English Version

The Domain Name System (DNS) was designed to provide a general-purpose, distributed, and scalable mechanism for mapping between Internet host names and addresses. The DNS has several goals:

1. To provide a consistent naming scheme that would allow multiple networks to interoperate
2. To eliminate the need for a single centralized host table
3. To provide reliable and efficient name-to-address translation
4. To allow for decentralized administration and maintenance

Prior to DNS, the ARPANET used a centralized naming system based on a single file, HOSTS.TXT, which was maintained by the Network Information Center (NIC) at SRI International. This file contained a mapping of all host names to their corresponding network addresses. As the Internet grew, this approach became increasingly untenable for several reasons:

- **Scalability:** The single file grew too large to be easily distributed and managed
- **Traffic:** The load on the NIC became excessive as users continuously downloaded updated versions of the file
- **Name collisions:** With thousands of organizations, coordinating unique names through a single authority became difficult
- **Consistency:** Updates to the file were not immediately available to all hosts, leading to inconsistencies
- **Administrative overhead:** All name registrations had to go through a central authority

The DNS was developed as a solution to these problems. Instead of a single centralized database, DNS uses a hierarchical, distributed database with local caching. The database is partitioned both by function and by administrative domain, allowing different organizations to manage their own portion of the namespace independently.

The fundamental idea behind DNS is the delegation of authority over portions of the namespace. The namespace is organized as a tree, with the root at the top and individual hosts at the leaves. Each node in the tree represents a domain, and each domain can be managed by a different organization. A domain can delegate responsibility for subdomains to other organizations, creating a hierarchy of administrative responsibility that matches the structure of organizations using the Internet.

DNS also introduced the concept of resource records (RRs), which are general-purpose data structures that can store various types of information associated with domain names, not just address mappings. This extensibility has allowed DNS to grow beyond its original purpose to support applications such as electronic mail routing, service discovery, and security mechanisms.

The protocol and architecture described in this paper evolved from the initial design in 1983 through extensive experimentation and deployment. This paper examines the original design goals, the implementation strategies that were adopted, the evolution of the system as it was deployed, and lessons learned from operational experience.

---

### النسخة العربية

تم تصميم نظام أسماء النطاقات (DNS) لتوفير آلية متعددة الأغراض وموزعة وقابلة للتوسع للربط بين أسماء المضيفين وعناوينها على الإنترنت. لدى نظام DNS عدة أهداف:

1. توفير مخطط تسمية متسق يسمح لشبكات متعددة بالتشغيل البيني
2. إلغاء الحاجة إلى جدول مضيف مركزي واحد
3. توفير ترجمة موثوقة وفعالة من الاسم إلى العنوان
4. السماح بالإدارة والصيانة اللامركزية

قبل نظام DNS، كانت شبكة ARPANET تستخدم نظام تسمية مركزي يعتمد على ملف واحد، HOSTS.TXT، الذي كان يُحتفظ به في مركز معلومات الشبكة (NIC) في معهد SRI الدولي. احتوى هذا الملف على ربط لجميع أسماء المضيفين بعناوين شبكاتها المقابلة. مع نمو الإنترنت، أصبح هذا النهج غير قابل للاستمرار بشكل متزايد لعدة أسباب:

- **قابلية التوسع:** أصبح الملف الواحد كبيراً جداً بحيث لا يمكن توزيعه وإدارته بسهولة
- **حركة المرور:** أصبح الحمل على مركز NIC مفرطاً حيث كان المستخدمون يقومون بتنزيل نسخ محدثة من الملف باستمرار
- **تصادمات الأسماء:** مع آلاف المؤسسات، أصبح تنسيق الأسماء الفريدة من خلال سلطة واحدة أمراً صعباً
- **الاتساق:** لم تكن التحديثات على الملف متاحة فوراً لجميع المضيفين، مما أدى إلى عدم الاتساق
- **النفقات الإدارية:** كان لابد أن تمر جميع عمليات تسجيل الأسماء عبر سلطة مركزية

تم تطوير نظام DNS كحل لهذه المشاكل. بدلاً من قاعدة بيانات مركزية واحدة، يستخدم DNS قاعدة بيانات هرمية موزعة مع التخزين المؤقت المحلي. يتم تقسيم قاعدة البيانات حسب الوظيفة والنطاق الإداري، مما يسمح لمؤسسات مختلفة بإدارة جزءها الخاص من فضاء الأسماء بشكل مستقل.

الفكرة الأساسية وراء DNS هي تفويض السلطة على أجزاء من فضاء الأسماء. يتم تنظيم فضاء الأسماء كشجرة، مع الجذر في الأعلى والمضيفين الفرديين في الأوراق. تمثل كل عقدة في الشجرة نطاقاً، ويمكن إدارة كل نطاق من قبل مؤسسة مختلفة. يمكن للنطاق تفويض المسؤولية عن النطاقات الفرعية لمؤسسات أخرى، مما يخلق تسلسلاً هرمياً من المسؤولية الإدارية يتطابق مع هيكل المؤسسات التي تستخدم الإنترنت.

قدم DNS أيضاً مفهوم سجلات الموارد (RRs)، وهي بنى بيانات متعددة الأغراض يمكنها تخزين أنواع مختلفة من المعلومات المرتبطة بأسماء النطاقات، وليس فقط ربط العناوين. لقد سمحت هذه القابلية للتوسع لنظام DNS بالنمو إلى ما هو أبعد من غرضه الأصلي لدعم تطبيقات مثل توجيه البريد الإلكتروني، واكتشاف الخدمات، وآليات الأمان.

تطور البروتوكول والمعمارية الموصوفة في هذه الورقة من التصميم الأولي في عام 1983 من خلال التجريب والنشر المكثف. تفحص هذه الورقة أهداف التصميم الأصلية، واستراتيجيات التنفيذ التي تم اعتمادها، وتطور النظام عند نشره، والدروس المستفادة من الخبرة التشغيلية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Domain Name System (نظام أسماء النطاقات)
  - HOSTS.TXT (ملف HOSTS.TXT - kept as-is, technical file name)
  - Network Information Center (مركز معلومات الشبكة)
  - Delegation (تفويض)
  - Resource records (سجلات الموارد)
  - Namespace (فضاء الأسماء)
  - Hierarchical database (قاعدة بيانات هرمية)
  - Distributed system (نظام موزع)
- **Equations:** 0
- **Citations:** 0
- **Special handling:**
  - Preserved technical acronyms (DNS, NIC, RR, ARPANET)
  - Maintained bullet point structure
  - Kept file name "HOSTS.TXT" in original form

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Sample (First and Last Paragraphs)

**First paragraph back-translation:**
The Domain Name System (DNS) was designed to provide a multi-purpose, distributed, and scalable mechanism for mapping between Internet host names and their addresses. DNS has several goals: 1) Provide a consistent naming scheme that allows multiple networks to interoperate, 2) Eliminate the need for a single centralized host table, 3) Provide reliable and efficient name-to-address translation, 4) Allow for decentralized administration and maintenance.

**Last paragraph back-translation:**
The protocol and architecture described in this paper evolved from the initial design in 1983 through extensive experimentation and deployment. This paper examines the original design goals, the implementation strategies that were adopted, the evolution of the system when deployed, and lessons learned from operational experience.

**Validation:** ✅ Back-translation preserves technical meaning and structure.
