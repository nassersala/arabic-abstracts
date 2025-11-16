# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** formal methods, B method, Event-B, safety-critical, certification, standards

---

### English Version

Formal methods and industry are not so often associated in the same sentence as the formers are not seen as an enabling technology but rather as difficult to apply and linked with increased costs. In [11], the introduction of the B method and the Event-B language into several industrial development processes was witnessed with more or less success, even if new tools and new practices were available to ease acceptance in industry. At that time, these two formal methods had been backed by a number of research projects and non-trivial industrial applications.

Almost 10 years later, after several real size experiments in diverse application domains, the situation has slightly evolved. Some standards, like the DO-178C for aeronautics, are now accepting formal methods in their certification process with sometimes some restrictions on the perimeter where they are applied (unit testing replaced by unit proof for example). The newborn ISO 26262 automotive functional safety standard is also recommending the use of formal methods during development. On the opposite side, the Common Criteria 3.1 standard (compared to its version 2.3) has decreased the need for formal methods that are now only required at level 6+ and higher (instead of 5+ previously) while the maximum security is reached at level 7 (EAL). However, even if the standards have made some room for them, these methods haven't spread much out of the railway sphere as it might have been expected. Their usage though have slightly evolved over the years as a reaction to industry needs in direct relation with fierce international competition.

This article presents in a first chapter the different ways B and Event-B were used for modeling software, systems and data, and for proving static and dynamic properties. In a second chapter, new technology and techniques are presented. Their tight combination is expecting to converge to a new, more automated way of developing safety critical applications that are not restricted to the railways.

---

### النسخة العربية

نادراً ما يتم ربط الأساليب الرسمية والصناعة في نفس الجملة، حيث لا يُنظر إلى الأساليب الرسمية على أنها تقنية تمكينية بل على أنها صعبة التطبيق ومرتبطة بزيادة التكاليف. في [11]، تم توثيق إدخال أسلوب B ولغة Event-B إلى عدة عمليات تطوير صناعية بنجاح متفاوت، حتى مع توفر أدوات وممارسات جديدة لتسهيل القبول في الصناعة. في ذلك الوقت، كان هذان الأسلوبان الرسميان مدعومَين بعدد من المشاريع البحثية والتطبيقات الصناعية غير البسيطة.

بعد ما يقرب من 10 سنوات، وبعد عدة تجارب بحجم حقيقي في مجالات تطبيقات متنوعة، تطور الوضع قليلاً. بعض المعايير، مثل DO-178C للملاحة الجوية، أصبحت الآن تقبل الأساليب الرسمية في عملية الاعتماد الخاصة بها مع بعض القيود أحياناً على النطاق الذي يتم تطبيقها فيه (على سبيل المثال، استبدال اختبار الوحدات بإثبات الوحدات). كما يوصي معيار ISO 26262 الحديث للسلامة الوظيفية في السيارات أيضاً باستخدام الأساليب الرسمية أثناء التطوير. من الجانب الآخر، خفّض معيار Common Criteria 3.1 (مقارنةً بنسخته 2.3) الحاجة إلى الأساليب الرسمية التي أصبحت الآن مطلوبة فقط عند المستوى 6+ وما فوق (بدلاً من 5+ سابقاً) بينما يتم الوصول إلى الحد الأقصى من الأمان عند المستوى 7 (EAL). ومع ذلك، حتى مع إفساح المعايير مجالاً لها، لم تنتشر هذه الأساليب كثيراً خارج مجال السكك الحديدية كما كان متوقعاً. على الرغم من ذلك، فقد تطور استخدامها قليلاً على مر السنين كرد فعل لاحتياجات الصناعة في علاقة مباشرة مع المنافسة الدولية الشرسة.

يقدم هذا المقال في الفصل الأول الطرق المختلفة التي استُخدم بها B و Event-B لنمذجة البرمجيات والأنظمة والبيانات، ولإثبات الخصائص الثابتة والديناميكية. في الفصل الثاني، يتم تقديم تقنيات وتكنولوجيات جديدة. ومن المتوقع أن يتقارب مزيجها المتكامل إلى طريقة جديدة أكثر آلية لتطوير التطبيقات الحرجة من حيث السلامة التي لا تقتصر على السكك الحديدية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** B method, Event-B, DO-178C, ISO 26262, Common Criteria, EAL (Evaluation Assurance Level)
- **Equations:** 0
- **Citations:** [11] - referenced but not detailed in this section
- **Special handling:**
  - Standards names (DO-178C, ISO 26262, Common Criteria) kept in English as per technical convention
  - EAL (Evaluation Assurance Level) kept as acronym
  - "unit proof" translated as "إثبات الوحدات" to distinguish from "unit testing" (اختبار الوحدات)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
