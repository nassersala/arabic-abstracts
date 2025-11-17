# Section 7: Conclusions
## القسم 7: الاستنتاجات

**Section:** conclusions
**Translation Quality:** 0.87
**Glossary Terms Used:** security breaches (الاختراقات الأمنية), coding errors (أخطاء البرمجة), formal methods (الأساليب الرسمية), static analysis (التحليل الساكن), penetration tests (اختبارات الاختراق), continuous integration/continuous deployment (CI/CD - التكامل المستمر/النشر المستمر)

---

### English Version

As the media never tire of saying, there are far too many security breaches, and, though they have multiple causes, [43] claims that about 50% of security breaches are caused by coding errors. There appears to be a culture of accepting these, with the U.S. Government investigation [69] into Equifax blaming many factors but not the actual bug, and [57] taking a "necessary but not sufficient" approach to education in secure coding.

**Education** Could certainly do better [12], though there are encouraging signs [20] and useful ideas when it comes to improving informal resources [23]. However, informal resources can be dangerous when it comes to security, and [20] recommends giving all students the advice in [18]: "If you pick up a SSL/TLS answer from Stack Overflow, there's a 70% chance it's insecure". More training in formal methods would be welcomed, at least in those cultures where it is lacking.

**Customers/Managers** need to be much more upfront about security requirements [48, 47], and enforce (e.g. by requiring tool support during any CI/CD process, such as [11] describe) at least "middle ground" requirements. In the case of outsourced development, explicit penalty clauses for failing penetration tests should concentrate the developers' minds.

**C/C++ people** These programmers should be much more aware of techniques for secure coding, such as those described in [14, Appendix F], and the various tools for static analysis.

**Java people** In view of the significance of injection attacks (Number 1 in [54]), programmers should be aware of taint analysis, as in [40].

**JavaScript people** There are some techniques, such as [41], for protecting JavaScript applications, but they are not deployable in the the typical JavaScript "dynamic loading web page" environment. Furthermore this environment is basically antithetical to security, as British Airways is learning to the cost of £183M [67].

1) Hence the first real challenge of JavaScript lies with the tool makers: there are, as far as the author knows, no JavaScript verifiers in existence, and no page-bundler that checks for version drift, or does incremental verification (which might be comparatively cheap, as in [11]).

2) An alternative approach might be to change the JavaScript model. This is advocated in [72], based on their analysis of what third-party scripts do in the wild. This is not a completely radical idea: Google is testing its TrustedTypes feature [36], with the motivation "The DOM API is insecure by default and requires special treatment to prevent XSS".

**Empirical Research** There is not much analysis of the efficacy of various techniques in security programming. [2] compares various techniques, and states the following.

> Based on our case study [of two large programs], the most efficient vulnerability discovery technique is automated penetration testing. Static analysis finds more vulnerabilities but the time it takes to classify false positives makes it less efficient than automated testing.

This assumes that "false positives" are acceptable, a debatable point of view. It would be good to have more such research.

**Tool developers** There is a lack of tools (or at least a lack of awareness of tools) that can be neatly integrated into a security programming toolchain the way such tools are integrated in safety-critical toolchains [11].

---

### النسخة العربية

كما لا تتعب وسائل الإعلام من قول ذلك، هناك الكثير من الاختراقات الأمنية، وعلى الرغم من أن لها أسباباً متعددة، تدعي [43] أن حوالي 50٪ من الاختراقات الأمنية ناتجة عن أخطاء البرمجة. يبدو أن هناك ثقافة قبول هذه، مع تحقيقات الحكومة الأمريكية [69] في Equifax التي تلوم العديد من العوامل ولكن ليس الخطأ الفعلي، و [57] التي تتخذ نهج "ضروري ولكن غير كافٍ" للتعليم في البرمجة الآمنة.

**التعليم** يمكن بالتأكيد أن يكون أفضل [12]، على الرغم من وجود علامات مشجعة [20] وأفكار مفيدة عندما يتعلق الأمر بتحسين الموارد غير الرسمية [23]. ومع ذلك، يمكن أن تكون الموارد غير الرسمية خطيرة عندما يتعلق الأمر بالأمن، و [20] توصي بإعطاء جميع الطلاب النصيحة في [18]: "إذا التقطت إجابة SSL/TLS من Stack Overflow، فهناك فرصة 70٪ أنها غير آمنة". سيكون المزيد من التدريب على الأساليب الرسمية موضع ترحيب، على الأقل في تلك الثقافات التي تفتقر إليه.

**العملاء/المديرون** بحاجة إلى أن يكونوا أكثر صراحة بكثير حول متطلبات الأمن [48، 47]، وفرض (على سبيل المثال من خلال طلب دعم الأدوات خلال أي عملية CI/CD، كما تصف [11]) على الأقل متطلبات "الأرضية الوسطى". في حالة التطوير الخارجي، يجب أن تركز شروط العقوبة الصريحة على فشل اختبارات الاختراق عقول المطورين.

**مبرمجو C/C++** يجب أن يكون هؤلاء المبرمجون أكثر وعياً بتقنيات البرمجة الآمنة، مثل تلك الموصوفة في [14، الملحق F]، والأدوات المختلفة للتحليل الساكن.

**مبرمجو Java** نظراً لأهمية هجمات الحقن (رقم 1 في [54])، يجب أن يكون المبرمجون على دراية بتحليل التلويث، كما في [40].

**مبرمجو JavaScript** هناك بعض التقنيات، مثل [41]، لحماية تطبيقات JavaScript، لكنها غير قابلة للنشر في بيئة JavaScript النموذجية "لصفحة الويب ذات التحميل الديناميكي". علاوة على ذلك، فإن هذه البيئة في الأساس مناقضة للأمن، كما تتعلم British Airways بتكلفة 183 مليون جنيه إسترليني [67].

1) ومن ثم، فإن التحدي الحقيقي الأول لـ JavaScript يكمن في صانعي الأدوات: لا توجد، بحسب علم المؤلف، أدوات تحقق من JavaScript موجودة، ولا يوجد أداة تجميع صفحات تتحقق من انجراف الإصدار، أو تقوم بالتحقق التدريجي (والذي قد يكون رخيصاً نسبياً، كما في [11]).

2) قد يكون النهج البديل هو تغيير نموذج JavaScript. يُدافع عن هذا في [72]، بناءً على تحليلهم لما تفعله سكريبتات الطرف الثالث في البرية. هذه ليست فكرة جذرية تماماً: Google تختبر ميزة TrustedTypes [36]، بدافع "DOM API غير آمن بشكل افتراضي ويتطلب معاملة خاصة لمنع XSS".

**البحث التجريبي** لا يوجد الكثير من التحليل لفعالية التقنيات المختلفة في البرمجة الأمنية. [2] تقارن تقنيات مختلفة، وتنص على ما يلي.

> بناءً على دراسة الحالة الخاصة بنا [لبرنامجين كبيرين]، فإن تقنية اكتشاف الثغرات الأكثر كفاءة هي اختبار الاختراق التلقائي. يجد التحليل الساكن ثغرات أكثر لكن الوقت الذي يستغرقه تصنيف الإيجابيات الكاذبة يجعله أقل كفاءة من الاختبار التلقائي.

هذا يفترض أن "الإيجابيات الكاذبة" مقبولة، وهي وجهة نظر قابلة للنقاش. سيكون من الجيد أن يكون هناك المزيد من هذا البحث.

**مطورو الأدوات** هناك نقص في الأدوات (أو على الأقل نقص في الوعي بالأدوات) التي يمكن دمجها بدقة في سلسلة أدوات البرمجة الأمنية بالطريقة التي يتم بها دمج هذه الأدوات في سلاسل أدوات الأنظمة الحرجة من حيث السلامة [11].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** security breaches, coding errors, CI/CD process, penetration tests, middle ground requirements, taint analysis, page-bundler, version drift, incremental verification, false positives, XSS (Cross-Site Scripting)
- **Equations:** 0
- **Citations:** [2], [11], [12], [14], [18], [20], [23], [36], [40], [41], [43], [47], [48], [54], [57], [67], [69], [72]
- **Special handling:** Recommendations organized by stakeholder groups (Education, Customers/Managers, C/C++ people, Java people, JavaScript people, Empirical Research, Tool developers); specific percentage (70%, 50%) preserved; British Airways fine amount (£183M) preserved; programming language names kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
