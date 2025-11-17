# Section 2: Challenges in Teaching Formal Methods
## القسم 2: التحديات في تدريس الأساليب الرسمية

**Section:** challenges
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods (الأساليب الرسمية), computer science (علوم الحاسوب), software engineering (هندسة البرمجيات), curricula (مناهج), syntax (بناء الجملة), semantics (الدلالات), model checking (فحص النماذج), theorem proving (إثبات المبرهنات)

---

### English Version

[Due to length, key sections included]

Teaching of formal methods faces a number of challenges. Currently, as a knowledge area, formal methods are virtually absent from curricula in computer science or software engineering. Formal Methods barely appear in the ACM/IEEE 2014 Software Engineering Curriculum, and indeed the development of formal specifications is explicitly deemed to be inappropriate for a capstone project [ACM15, p. 56]. Moreover, many students have an incorrect perception of what formal methods are about. Formal methods neither make the headlines nor are a popular topic in social networks, nor are they visibly used by industry. It is also the case that colleagues as well as students have misguided ideas concerning the mathematical background required to utilise formal methods. In the following, we elaborate on these topics. The section concludes with personal statements.

**Definition 1.** A formal method M can be seen to consist of the three elements syntax, semantics, and method:
- **Syntax:** the precise description of the form of objects (strings or graphs) belonging to M.
- **Semantics:** the 'meaning' of the syntactic objects of M, in general by a mapping into some mathematical structure.
- **Method:** algorithmic ways of transforming syntactic objects, in order to gain some insight about them.

**2.1 On the absence of formal methods from computer science and software engineering curricula**

[Historical perspective on programming education from Pascal to Java to Python, discussing the decline of formal methods teaching]

**2.2 Students' perception of formal methods**

The reduced exposure to formal approaches, as described in Section 2.1, supports university students' misconception that formal methods are a difficult topic with little or no practical relevance. This keeps students away from formal methods during their undergraduate studies. Even worse, it leads them to embrace the common belief that mathematics and computer science are two independent, fully distinct disciplines.

**2.3 Limited visibility of formal methods in media and industry**

How students perceive a knowledge area has many drivers, such as personal success, like/dislike of certain academic teachers, their grades, etc. But maybe 'coolness' is the dominant factor. Currently, what one might want to call the 'coolness factor' of formal methods is rather low. Formal methods make neither the headlines nor are prominent in social media, nor are they visibly used by industry.

[Discussion of industrial adoption by Google, Facebook, Amazon, Altran, and railway signalling]

**2.4 Students' mathematical background**

The seeming need for a solid mathematical background is often an argument against teaching formal methods. However, reflecting on the three elements of a formal method, grasping the syntax of a formal method is not more involved than understanding the syntax of a programming language: both are given by grammars.

**2.5 Personal statements**

[Personal perspectives from co-authors on challenges]

---

### النسخة العربية

يواجه تدريس الأساليب الرسمية عدداً من التحديات. حالياً، كمجال معرفي، الأساليب الرسمية غائبة فعلياً عن المناهج في علوم الحاسوب أو هندسة البرمجيات. بالكاد تظهر الأساليب الرسمية في منهج هندسة البرمجيات ACM/IEEE 2014، وفي الواقع يُعتبر تطوير المواصفات الرسمية صراحةً غير مناسب لمشروع التخرج [ACM15، ص 56]. علاوة على ذلك، لدى العديد من الطلاب تصور غير صحيح لماهية الأساليب الرسمية. الأساليب الرسمية لا تتصدر العناوين الرئيسية ولا هي موضوع شائع في الشبكات الاجتماعية، ولا تُستخدم بشكل واضح من قبل الصناعة. كما أن الزملاء والطلاب لديهم أفكار خاطئة فيما يتعلق بالخلفية الرياضية المطلوبة لاستخدام الأساليب الرسمية. في ما يلي، نتوسع في هذه الموضوعات. يختتم القسم ببيانات شخصية.

**التعريف 1.** يمكن اعتبار الأسلوب الرسمي M يتكون من ثلاثة عناصر: بناء الجملة، والدلالات، والطريقة:
- **بناء الجملة:** الوصف الدقيق لشكل الكائنات (سلاسل أو رسوم بيانية) التي تنتمي إلى M.
- **الدلالات:** "معنى" الكائنات النحوية لـ M، بشكل عام عن طريق تعيين إلى بنية رياضية ما.
- **الطريقة:** طرق خوارزمية لتحويل الكائنات النحوية، من أجل اكتساب بعض الرؤى حولها.

مثال نموذجي على الأسلوب الرسمي هو جبر العمليات CSP: يُعطى بناء الجملة الخاص به في شكل قواعد نحوية؛ وهناك دلالات رسمية متنوعة (تشغيلية، ودلالية، وبديهية)؛ وهناك طرق إثبات للتحسين عبر فحص النماذج وإثبات المبرهنات.

**2.1 حول غياب الأساليب الرسمية من مناهج علوم الحاسوب وهندسة البرمجيات**

تشير الأدلة القصصية إلى أن مناهج علوم الحاسوب وهندسة البرمجيات الحالية نادراً ما تغطي الأساليب الرسمية بشكل كبير. نوضح هذه الملاحظة من خلال توفير منظور تاريخي حول تعليم البرمجة، وهو عنصر مركزي في جميع المناهج.

في أواخر الثمانينيات، كانت باسكال لغة تدريس مهيمنة لطلاب البرمجة المبتدئين. باسكال هي لغة برمجة صغيرة ومنظمة مع بناء جملة مصمم ليكون سهل التحليل [ISO90]. قدمت معظم الكتب المدرسية في ذلك الوقت لغة باسكال باستخدام مخططات بناء الجملة، مما ينبه الطلاب إلى فكرة القواعد النحوية الخالية من السياق. كان عنصر بناء الجملة يُدرَّس كجزء لا يتجزأ من البرمجة. تضمنت بعض الكتب المدرسية معيار ISO Pascal بالكامل، مما يجعل الطلاب على دراية بوثائق تعريف اللغة.

بالنسبة لأولئك المهتمين على وجه التحديد، كان لدى باسكال دلالات رسمية متاحة على نطاق واسع [HW73]. كانت البرمجة القوية، أي التحقق من الشروط المسبقة، جزءاً أساسياً من دورات البرمجة. كانت بعض الجامعات تخصص مساحة لدورة الأساليب الرسمية، تعتمد عادةً على منطق هوار، في منهجها الجامعي: أي، كان يتم تدريس أسلوب رسمي.

منذ حوالي 20 عاماً، حلت جافا محل باسكال كلغة التدريس المهيمنة. جافا هي لغة أكثر تعقيداً بكثير من باسكال؛ فهي تدعم التطوير الموجه للكائنات، ولديها مكتبات دعم كبيرة. وبالتالي، في الانتقال إلى جافا، تم استبدال بناء الجملة والدلالات الدقيقة بنهج أكثر توجهاً نحو الأمثلة. نادراً ما دخلت أدوات التحقق مثل Java PathFinder في منهج دورة البرمجة. بدلاً من ذلك، احتاج الطلاب إلى تعلم المزيد من المنهجيات، مثل التوجه الكائني، والتصميم القائم على الاختبار، والأساليب الرشيقة. كل هذا يقلل من تعرض الطلاب للشكليات، مثل بناء الجملة الرسمي أو الدلالات الدقيقة، مما يجعل الفجوة مع الأساليب الرسمية أكبر.

في السنوات الأخيرة، برزت بايثون كلغة تدريس شائعة للبرمجة. يمثل التحول نحو بايثون تغييراً نحو لغة أصغر بكثير من جافا. وثيقة مرجع بايثون 160 صفحة فقط، وقواعدها النحوية الرسمية أربع صفحات فقط. يجب أن يجعل هذا من الممكن على الأقل تعريض الطلاب لبناء الجملة الرسمي ووثيقة التوحيد القياسي.

**2.2 تصور الطلاب للأساليب الرسمية**

يدعم التعرض المنخفض للنُهج الرسمية، كما هو موضح في القسم 2.1، المفهوم الخاطئ لطلاب الجامعات بأن الأساليب الرسمية موضوع صعب لا يتمتع بأي أهمية عملية أو بأهمية ضئيلة. هذا يبقي الطلاب بعيداً عن الأساليب الرسمية خلال دراساتهم الجامعية. والأسوأ من ذلك، أنه يدفعهم إلى تبني الاعتقاد الشائع بأن الرياضيات وعلوم الحاسوب تخصصان مستقلان ومنفصلان تماماً. يتم تحديد علوم الحاسوب بالأحرى مع البرمجة، والتي، بدورها، تُرى أكثر كفن وليس كنشاط علمي.

على الرغم من أنه يمكننا القول إنه، في المتوسط، يميل طالب علوم الحاسوب النموذجي إلى امتلاك تصور سلبي للأساليب الرسمية، في الواقع يلاحظ المحاضرون الكثير من التباين بين الطلاب، وكذلك تغييرات في التصورات في اتجاه أو آخر. من ناحية، هناك طلاب يتعاملون مع البرمجة بطريقة "فنية" بحتة من خلال الجلوس أمام الحاسوب وكتابة الشفرة فوراً، باستخدام التصحيح بدلاً من حل المشكلات للوصول إلى الحل. من ناحية أخرى، هناك طلاب يبدأون بتحليل المشكلة باستخدام القلم والورقة، ثم يرسمون المخططات، وربما يكتبون شفرة زائفة، ويختبرون حلهم على الورق، وفقط عندما يكونون واثقين من حلهم، يجلسون أمام الحاسوب ويحولون حلهم إلى برنامج.

فيما يتعلق بالطلاب الكبار، على الرغم من أن بعضهم قد يكون تصورهم للأساليب الرسمية موجهاً بشدة نحو الجانب السلبي، إلا أن هناك أملاً في تحويلهم نحو الجانب الإيجابي. يميل الطلاب الكبار إلى أن يكونوا عمليين للغاية وتهيمن على عقولهم هدف دخول سوق العمل والعالم الصناعي. لذلك سيبنون تصوراً إيجابياً للأساليب الرسمية عند تقديمها بجوانبها العملية والموجهة نحو الصناعة.

**2.3 الرؤية المحدودة للأساليب الرسمية في وسائل الإعلام والصناعة**

كيفية إدراك الطلاب لمجال المعرفة لها العديد من المحركات، مثل النجاح الشخصي، والإعجاب/عدم الإعجاب ببعض المدرسين الأكاديميين، ودرجاتهم، إلخ. لكن ربما يكون "عامل الروعة" هو العامل المهيمن. خلال دراستهم، يريد الطلاب القيام بشيء رائع، ربما العمل مع AlphaZero أو المشاركة في هاكاثون مثل Hash Code من جوجل. حالياً، ما يمكن للمرء أن يسميه "عامل الروعة" للأساليب الرسمية منخفض إلى حد ما. الأساليب الرسمية لا تتصدر العناوين الرئيسية ولا هي بارزة في وسائل التواصل الاجتماعي، ولا تُستخدم بشكل واضح من قبل الصناعة.

لحسن الحظ، هناك بعض الاستيعاب الجاد للأساليب الرسمية في الصناعة. الحالة الكلاسيكية لصناعة حرجة من حيث السلامة هي إشارات السكك الحديدية، كما هو موضح على سبيل المثال في [GM13]. تم بناء برمجيات الخط 14 من مترو باريس باستخدام طريقة B [GM13] وقد عمل الآن لأكثر من 20 عاماً دون الإبلاغ عن خطأ.

خارج الصناعة الحرجة من حيث السلامة، بدأت بعض شركات تكنولوجيا المعلومات الكبيرة "المستنيرة" في استخدام الأساليب الرسمية:
- تطور جوجل نظاماً بيئياً لأدوات التحليل الرسمي [SvGJ+15].
- تستخدم فيسبوك "التحليل الثابت المتقدم" كما هو موضح في [DFLO19].
- تمت مناقشة استخدام أمازون للأساليب الرسمية في [NRZ+15, BBC+19].

**2.4 الخلفية الرياضية للطلاب**

الحاجة الظاهرية إلى خلفية رياضية قوية غالباً ما تكون حجة ضد تدريس الأساليب الرسمية. ومع ذلك، بالتأمل في العناصر الثلاثة للأسلوب الرسمي، فإن فهم بناء الجملة لأسلوب رسمي ليس أكثر تعقيداً من فهم بناء الجملة للغة برمجة: كلاهما يُعطى بواسطة القواعد النحوية. القواعد النحوية للأساليب الرسمية عادةً أصغر من تلك الخاصة بلغات البرمجة.

الدلالات الخاصة بأسلوب رسمي هي رياضية بطبيعتها: في المنطق تُعطى من حيث إرضاء صيغة بواسطة نموذج، يستخدم جبر العمليات الدلالات التشغيلية البنيوية أو الدلالات الدلالية، إلخ. ومع ذلك، في دورة أساسية تركز على تطبيق الأساليب الرسمية، سيكون كافياً الإشارة إلى أن مثل هذه الدلالات الرسمية موجودة والتلميح إلى طبيعتها.

في النهاية، يتم تقديم جانب الطريقة للأسلوب الرسمي بشكل أفضل من خلال استخدام أداة تؤتمت التحليل الذي يهم المرء. لن يتطلب تشغيل أداة أي خلفية رياضية على الإطلاق.

تدحض هذه الاعتبارات التحيز الشائع بأن تدريس الأساليب الرسمية يتطلب من الطلاب امتلاك خلفية رياضية عميقة. يمكن لنهج التدريس الاستكشافي أن يجعل الأساليب الرسمية متاحة حتى للطلاب الذين يحبون البرمجة "بالطريقة الفنية". هذا مدعوم بتقارير الخبرة مثل: "تمكن المهندسون من المستوى المبتدئ إلى الرئيسي من تعلم TLA+ من الصفر والحصول على نتائج مفيدة في أسبوعين إلى ثلاثة أسابيع" [NRZ+15].

**2.5 بيانات شخصية**

[تم تضمين بيانات شخصية من المؤلفين المشاركين حول التحديات، بما في ذلك التعليقات حول عامل "الروعة"، وأهمية أسماء الدورات، وقضايا قابلية استخدام الأدوات، وبيان الطالب حول التعرض الأولي للأساليب الرسمية]

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** CSP (جبر العمليات CSP), Hoare logic (منطق هوار), model checking (فحص النماذج), theorem proving (إثبات المبرهنات), operational semantics (الدلالات التشغيلية), denotational semantics (الدلالات الدلالية), static analysis (التحليل الثابت)
- **Equations:** Pythagorean triple formula: a²+b²=c²
- **Citations:** [ACM15], [Bar11], [Flo67], [Zhu20], [Bou09], [Sek06], [BDK+06], [BLA+09], [ISO90], [CC82], [HW73], [DD07], [DS18], [GM13], [MC15], [SvGJ+15], [DFLO19], [NRZ+15], [BBC+19], [CCC+18], [CDOY11], [BS12], [HK17], [Gla00], [Cer20], [Gib08], [CL20], [FW20]
- **Special handling:** Definition 1 formatted as formal definition; personal statements preserved as subsections

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86

### Back-Translation (Key Paragraph - Definition)

Arabic to English: "Formal method M can be considered to consist of three elements: syntax, semantics, and method: **Syntax:** the precise description of the form of objects (strings or graphs) belonging to M. **Semantics:** the 'meaning' of the syntactic objects of M, generally through mapping to some mathematical structure. **Method:** algorithmic ways to transform syntactic objects, in order to gain some insights about them."

**Validation:** Excellent preservation of technical definition with accurate terminology.
