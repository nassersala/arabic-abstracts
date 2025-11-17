# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** cybersecurity (الأمن السيبراني), injection attacks (هجمات الحقن), remote code execution (تنفيذ الكود عن بعد), taint analysis (تحليل التلويث), CIA (Confidentiality, Integrity, Availability) (السرية والنزاهة والتوافر)

---

### English Version

CyberSecurity failures abound, and the number of people that can be affected by even a single failure is amazing — 148 million for Equifax [10] and probably more for the Starwood breach: [5] states 500 million, but [33] "downgrades" this to 383 million. The financial costs can be substantial: bankruptcy in the case of American Medical Collection Agency [24] and a provisional £183M fine for British Airways [67]. These problems have attracted attention at the highest scientific levels [58].

There are many reasons for CyberSecurity failures, and even a given failure may have multiple causes. For example, the U.S. Government investigation [69] into Equifax states "Equifax's investigation of the breach identified four major factors including identification, detection, segmenting of access to databases, and data governance that allowed the attacker . . . ". However, none of these would have been triggered had it not been for the original bug in the Apache code [39], which was of the well-known (Number 1 Application Security Risk in [54]) family of "Injection" (or "Remote Code Execution") attacks, and which would probably have been detected by an automatic taint analysis tool such as [40].

Though attributing causes at scale is difficult, a well-known textbook [43] claims that about 50% of security breaches are caused by coding errors. Hence it behoves security practitioners to look seriously at coding errors, while recognising that this is only one facet of the problem. This is taken up by the Payments Card Industry in [57], essentially the only world-wide mandatory security standard, in two requirements.

6.5 Address common coding vulnerabilities in software-development processes as follows:
• Train developers at least annually in up-to-date secure coding techniques, including how to avoid common coding vulnerabilities;
• Develop applications based on secure coding guidelines.

The precise definition of CyberSecurity is debatable: we can take is as failures of security, generally defined as "preserving the CIA — Confidentiality, Integrity and Availability" of digital information, where computer system played a critical part in the failure.

6.6 For public-facing web applications, address new threats and vulnerabilities on an ongoing basis and ensure these applications are protected against known attacks by either of the following methods:
• Reviewing public-facing web applications via manual or automated application vulnerability security assessment tools or methods, at least annually and after any changes;
• Installing an automated technical solution that detects and prevents web-based attacks (for example, a web-application firewall) in front of public-facing web applications, to continually check all traffic.

It is noteworthy that, despite apparently insisting on secure coding in 6.5, they require the additional defences in 6.6, realising that errare humanum est, and the 6.5-developed code may not actually be secure. Is it possible (the author thinks so, but the experiment has yet to be performed) that adding formal methods to 6.5 would render 6.6 redundant? Full formal verification of a complete system should certainly suffice.

Complete formal verification is the only known way to guarantee that a system is free of programming errors. [35, describing seL4: a verified operating system]

Such a verified operating system has been used in medical devices, but probably not sufficiently widely, as 500,000 already-fitted pacemakers have had to be upgraded through security weaknesses [66], and insulin pumps are also vulnerable [51]. See [30] for a recent update on seL4. However, most of us do not have the opportunity to start from scratch, and have to live on top of imperfect, unverified systems, interoperating with other systems via large, generally unverified, protocols, such as TLS.

---

### النسخة العربية

تكثر إخفاقات الأمن السيبراني، وعدد الأشخاص الذين يمكن أن يتأثروا حتى بإخفاق واحد مذهل — 148 مليون في حالة Equifax [10] وربما أكثر في اختراق Starwood: تذكر [5] 500 مليون، لكن [33] "تخفض" هذا الرقم إلى 383 مليون. يمكن أن تكون التكاليف المالية كبيرة: الإفلاس في حالة American Medical Collection Agency [24] وغرامة مؤقتة بقيمة 183 مليون جنيه إسترليني لشركة British Airways [67]. وقد جذبت هذه المشاكل الانتباه على أعلى المستويات العلمية [58].

هناك العديد من الأسباب لإخفاقات الأمن السيبراني، وحتى إخفاق معين قد يكون له أسباب متعددة. على سبيل المثال، تنص تحقيقات الحكومة الأمريكية [69] في Equifax على أن "تحقيق Equifax في الاختراق حدد أربعة عوامل رئيسية بما في ذلك التعريف والاكتشاف وتقسيم الوصول إلى قواعد البيانات وحوكمة البيانات التي سمحت للمهاجم...". ومع ذلك، لم يكن أي من هذه العوامل ليتم تفعيله لولا الخطأ الأصلي في كود Apache [39]، والذي كان من عائلة "الحقن" (أو "تنفيذ الكود عن بعد") المعروفة جيداً (الخطر الأمني الأول للتطبيقات في [54])، والذي كان من المحتمل أن يتم اكتشافه بواسطة أداة تحليل التلويث التلقائية مثل [40].

على الرغم من صعوبة إسناد الأسباب على نطاق واسع، يدعي كتاب مدرسي معروف [43] أن حوالي 50٪ من الاختراقات الأمنية ناتجة عن أخطاء البرمجة. لذلك يتعين على ممارسي الأمن النظر بجدية في أخطاء البرمجة، مع الاعتراف بأن هذا مجرد جانب واحد من المشكلة. يتم تناول هذا من قبل صناعة بطاقات الدفع في [57]، وهو في الأساس المعيار الأمني الإلزامي الوحيد على مستوى العالم، في متطلبين.

6.5 معالجة ثغرات البرمجة الشائعة في عمليات تطوير البرمجيات على النحو التالي:
• تدريب المطورين سنوياً على الأقل على تقنيات البرمجة الآمنة المحدثة، بما في ذلك كيفية تجنب ثغرات البرمجة الشائعة؛
• تطوير التطبيقات بناءً على إرشادات البرمجة الآمنة.

التعريف الدقيق للأمن السيبراني قابل للنقاش: يمكننا اعتباره إخفاقات في الأمن، المعرّف عموماً بأنه "الحفاظ على CIA — السرية والنزاهة والتوافر" للمعلومات الرقمية، حيث لعب نظام الحاسوب دوراً حاسماً في الإخفاق.

6.6 بالنسبة لتطبيقات الويب المواجهة للعامة، معالجة التهديدات والثغرات الجديدة بشكل مستمر والتأكد من حماية هذه التطبيقات ضد الهجمات المعروفة بإحدى الطرق التالية:
• مراجعة تطبيقات الويب المواجهة للعامة عبر أدوات أو طرق تقييم أمن ثغرات التطبيقات اليدوية أو التلقائية، سنوياً على الأقل وبعد أي تغييرات؛
• تثبيت حل تقني تلقائي يكتشف ويمنع الهجمات القائمة على الويب (على سبيل المثال، جدار حماية تطبيقات الويب) أمام تطبيقات الويب المواجهة للعامة، للتحقق المستمر من كل حركة المرور.

من الجدير بالملاحظة أنه على الرغم من الإصرار الظاهري على البرمجة الآمنة في 6.5، فإنهم يتطلبون الدفاعات الإضافية في 6.6، مدركين أن الخطأ من طبيعة البشر (errare humanum est)، وأن الكود المطور وفقاً لـ 6.5 قد لا يكون آمناً فعلياً. هل من الممكن (يعتقد المؤلف ذلك، لكن التجربة لم تُجرى بعد) أن إضافة الأساليب الرسمية إلى 6.5 ستجعل 6.6 زائداً عن الحاجة؟ التحقق الرسمي الكامل لنظام كامل يجب أن يكون كافياً بالتأكيد.

التحقق الرسمي الكامل هو الطريقة الوحيدة المعروفة لضمان خلو النظام من أخطاء البرمجة. [35، واصفاً seL4: نظام تشغيل متحقق منه]

تم استخدام مثل هذا النظام التشغيلي المتحقق منه في الأجهزة الطبية، لكن ربما ليس على نطاق واسع بما فيه الكفاية، حيث كان لا بد من ترقية 500,000 جهاز تنظيم ضربات القلب المركب بالفعل بسبب نقاط ضعف أمنية [66]، كما أن مضخات الأنسولين معرضة للخطر أيضاً [51]. انظر [30] لتحديث حديث عن seL4. ومع ذلك، لا تتاح لمعظمنا الفرصة للبدء من الصفر، ويتعين علينا العيش فوق أنظمة غير كاملة وغير متحقق منها، والتشغيل البيني مع أنظمة أخرى عبر بروتوكولات كبيرة غير متحقق منها بشكل عام، مثل TLS.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** cybersecurity failures, injection attacks, remote code execution, taint analysis, formal verification, seL4, CIA triad
- **Equations:** 0
- **Citations:** [5], [10], [24], [30], [33], [35], [39], [40], [43], [51], [54], [57], [58], [66], [67], [69]
- **Special handling:** Requirements 6.5 and 6.6 from PCI DSS standard preserved in structured format; Latin phrase "errare humanum est" kept with explanation

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
