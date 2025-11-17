# Section 4: The Need for Tools
## القسم 4: الحاجة إلى الأدوات

**Section:** need-for-tools
**Translation Quality:** 0.87
**Glossary Terms Used:** static verification (التحقق الساكن), formal methods (الأساليب الرسمية), continuous integration (التكامل المستمر), incremental verification (التحقق التدريجي)

---

### English Version

There are two key points.

[15, §4.1] Strong static verification tools tend to complement (not replace) human-driven review. The tools are very good at some problems (e.g. global data flow analysis, theorem proving) where humans are hopeless, and vice versa. If we do the static verification first, then we can adjust manual review processes and check-lists to take advantage of this.

[15, §6] The sixty-four-million-dollar-question, it seems, is how much "up-front" work is "just right" for a particular project. We doubt theres a one-size-fits-all approach, but surely the answer should be informed by disciplined requirements engineering of non-functional properties (e.g. safety, security and others) that can inform the design of a suitable architecture and its accompanying satisfaction argument.

Facebook grew, security (and "product quality" in general: it is not clear whether security was the main driver here) became more important, and by 2014 Zuckerberg had changed his views.

> "Move fast with stable infrastructure." It "may not be quite as catchy as 'move fast and break things,"' Zuckerberg said with a smirk. "But it's how we operate now." [62]

One might think his views were converging with the views of [15]. However, the Heartbleed story should remind us that the fact that a modification "has no new security considerations" as designed [61] doesn't mean that an implementation of that idea has no new security considerations. Hence the call in [15, §4.1] for strong static verification tools. Such tools are generally seen as expensive and slowing down the development process, but [11] shows that they need not be. In particular, they show that, for a real application (890,000 physical lines of Ada code), the cost of incremental verification can be reduced from "nightly" to "coffee", and hence can reasonably form part of a continuous integration toolchain, as is done at the company studied in [11]. Readers might comment that their own applications are not in Ada, but [17, §5.6] discusses mixed-language programming, especially with C. A similar point is made in [21], describing the Infer tool running on Java/Objective C/C++, where moving from overnight reporting to near real-time reporting moved the fix rate from 0% to 70%.

That these techniques are reaching the mainstream of CyberSecurity can be seen from Amazon Web Services adoption of them [70], Google [59], Facebook [21], and the recent DefectDojo release by OWASP [55].

---

### النسخة العربية

هناك نقطتان رئيسيتان.

[15، §4.1] تميل أدوات التحقق الساكن القوية إلى استكمال (وليس استبدال) المراجعة البشرية. الأدوات جيدة جداً في بعض المشاكل (مثل تحليل تدفق البيانات العام، وإثبات المبرهنات) حيث يكون البشر عاجزين، والعكس صحيح. إذا قمنا بالتحقق الساكن أولاً، فيمكننا تعديل عمليات المراجعة اليدوية وقوائم التحقق للاستفادة من ذلك.

[15، §6] السؤال الذي يبلغ أربعة وستين مليون دولار، على ما يبدو، هو مقدار العمل "المسبق" "المناسب تماماً" لمشروع معين. نشك في وجود نهج واحد يناسب الجميع، ولكن بالتأكيد يجب أن تُستنير الإجابة بهندسة المتطلبات المنضبطة للخصائص غير الوظيفية (مثل السلامة والأمن وغيرها) التي يمكن أن تُعلم تصميم معمارية مناسبة وحجة الرضا المصاحبة لها.

نما Facebook، وأصبح الأمن (و"جودة المنتج" بشكل عام: ليس من الواضح ما إذا كان الأمن هو المحرك الرئيسي هنا) أكثر أهمية، وبحلول عام 2014 كان زوكربيرغ قد غير وجهات نظره.

> "تحرك بسرعة مع بنية تحتية مستقرة." "قد لا تكون جذابة تماماً مثل 'تحرك بسرعة واكسر الأشياء'"، قال زوكربيرغ بابتسامة ساخرة. "لكنها الطريقة التي نعمل بها الآن." [62]

قد يعتقد المرء أن وجهات نظره كانت تتقارب مع وجهات نظر [15]. ومع ذلك، يجب أن تذكرنا قصة Heartbleed بأن حقيقة أن التعديل "ليس له اعتبارات أمنية جديدة" كما صُمم [61] لا تعني أن تنفيذ تلك الفكرة ليس له اعتبارات أمنية جديدة. ومن هنا جاءت الدعوة في [15، §4.1] لأدوات التحقق الساكن القوية. عادةً ما يُنظر إلى هذه الأدوات على أنها مكلفة وتبطئ عملية التطوير، لكن [11] تظهر أنها لا يجب أن تكون كذلك. على وجه الخصوص، يُظهرون أنه، بالنسبة لتطبيق حقيقي (890,000 سطر مادي من كود Ada)، يمكن تقليل تكلفة التحقق التدريجي من "ليلية" إلى "قهوة"، وبالتالي يمكن أن تشكل بشكل معقول جزءاً من سلسلة أدوات التكامل المستمر، كما يتم في الشركة التي تمت دراستها في [11]. قد يعلق القراء على أن تطبيقاتهم الخاصة ليست في Ada، لكن [17، §5.6] تناقش البرمجة متعددة اللغات، خاصة مع C. يتم طرح نقطة مماثلة في [21]، التي تصف أداة Infer التي تعمل على Java/Objective C/C++، حيث أدى الانتقال من الإبلاغ الليلي إلى الإبلاغ شبه الفوري إلى رفع معدل الإصلاح من 0٪ إلى 70٪.

يمكن رؤية وصول هذه التقنيات إلى التيار الرئيسي للأمن السيبراني من اعتماد Amazon Web Services لها [70]، وGoogle [59]، وFacebook [21]، وإصدار DefectDojo الأخير من OWASP [55].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** static verification tools, global data flow analysis, theorem proving, incremental verification, continuous integration toolchain, mixed-language programming
- **Equations:** 0
- **Citations:** [11], [15], [17], [21], [55], [59], [61], [62], [70]
- **Special handling:** "Sixty-four-million-dollar-question" idiom translated contextually; specific metrics (890,000 lines of code, 0% to 70% improvement) preserved; company names (Amazon, Google, Facebook, OWASP) kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
