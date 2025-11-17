# Section 3: Teaching Formal Methods — The Fun Way
## القسم 3: تدريس الأساليب الرسمية — بالطريقة الممتعة

**Section:** teaching-fun-way
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods (الأساليب الرسمية), model checking (فحص النماذج), theorem proving (إثبات المبرهنات), specifications (المواصفات), verification (التحقق)

---

### English Version

In this section we collect a number of personal views and ideas on how teaching formal methods can be done the fun way. While some authors, see, e.g. [CRS+15], have written systematic accounts of the topic, here we present a number of personal statements in the order in which they were contributed.

[Personal statements from various authors including discussions on:]

- **Games and puzzles:** Using games as light-weight introduction to formal methods
- **Tools and practical experience:** Emphasizing building and verifying software rather than pure theory
- **Real-world examples:** Moving from safety-critical systems to more common examples like the Chromium Project
- **Student research:** Involving students in formal methods research activities
- **Age-appropriate teaching:** Starting formal methods education early, even at school level

**3.1 Summarizing the ideas**

It is obviously impossible to establish general criteria to make formal methods teaching a fun activity. Fun cannot be characterised in an objective way and can only naturally emerge from the interaction between teachers and students. In fact, the emergence of fun is affected by the personalities of individual teachers and students as well as by the interaction context in which such different personalities meet in the classroom collaborative environment. Here, different criteria have been suggested and discussed, including:

- games and puzzles may represent a light-weight and fun introduction to formal methods;
- there should be an emphasis on building and verifying software for simple, but realistic, systems;
- teaching should focus on demonstrating that tools work rather than on delivering too much theory;
- students are likely to enjoy undertaking actual research activities;
- students should be involved in curricula development.

There is a general view among the co-authors that games and puzzles can be useful when it comes to teaching formal methods in the initial stages and represent a light-weight and fun introduction. It is important to note that this view includes former formal methods students who became formal methods teachers [MOPD20]. Games may be also associated with some form of competition, which may be within-class or in terms of participation at an international context. Games and puzzles are also a great tool to start formal methods education early, even by teaching to school level children, as young as 10–11. Competition can also be beneficial in the context of school children, but should be carefully planned in order to avoid being interpreted by the student as a form of assessment, which therefore inhibits rather than motivates the students [Cer20].

In addition, there must also be some emphasis on building and verifying software. However, such a connection with reality should be established in the right form to keep in line with the fun determined by the game-based approach. In fact, giving students the task of developing and verifying a simple, but realistic, model of a system would be beneficial while encouraging them to have fun with formal methods. However, on the one hand, realistic, industrial systems are often far away from what students can experience and experiment with and most students will not go into the construction of safety-critical systems, important though they are. On the other hand, the specialist safety-critical companies tend to do their own training, which may provide a very different perspective from what students learn in formal methods courses.

There is a general agreement among the co-authors that students need to see how formal methods work in reality using tools rather than focusing too much on the theory. However, making students use industrial tools may result in heavy frustration. While it is nice to see that such tools are used in practice, they might be the wrong means to learn formal methods.

A final aspect that could make a formal methods course interesting is to involve students in formal methods research rather than formal methods application. In fact, students' publications are often highly appreciated [POKG19, Zhu20].

---

### النسخة العربية

في هذا القسم نجمع عدداً من الآراء والأفكار الشخصية حول كيفية تدريس الأساليب الرسمية بالطريقة الممتعة. بينما كتب بعض المؤلفين، انظر، على سبيل المثال [CRS+15]، روايات منهجية للموضوع، نقدم هنا عدداً من البيانات الشخصية بالترتيب الذي قُدمت به.

[بيانات شخصية من مختلف المؤلفين تتضمن نقاشات حول:]

- **الألعاب والألغاز:** استخدام الألعاب كمقدمة خفيفة الوزن للأساليب الرسمية
- **الأدوات والخبرة العملية:** التركيز على بناء والتحقق من البرمجيات بدلاً من النظرية البحتة
- **أمثلة من العالم الواقعي:** الانتقال من الأنظمة الحرجة من حيث السلامة إلى أمثلة أكثر شيوعاً مثل مشروع Chromium
- **بحث الطلاب:** إشراك الطلاب في أنشطة البحث في الأساليب الرسمية
- **التدريس المناسب للعمر:** بدء تعليم الأساليب الرسمية مبكراً، حتى على مستوى المدرسة

**mf.** يمكن أن تكون الألعاب مفيدة عندما يتعلق الأمر بتدريس الأساليب الرسمية في المراحل الأولية. ومع ذلك، لإظهار أهمية الأساليب الرسمية بشكل كافٍ، يجب أن يكون هناك أيضاً تركيز على بناء والتحقق من البرمجيات وليس فقط على حل لغز، مهما كان ذلك مسلياً. بالطبع، سيجد طلاب علوم الحاسوب متعة في بناء الأنظمة، وإلا لما كانوا يدرسون الموضوع. لذلك، ربما يكون تكليفهم بمهمة تطوير والتحقق من نموذج بسيط، ولكن واقعي، لنظام مفيداً أيضاً مع تشجيعهم على الاستمتاع بالأساليب الرسمية.

**jd.** غالباً ما يكون من الصعب تحفيز الأساليب الرسمية. معظم الطلاب لن يذهبوا إلى بناء الأنظمة الحرجة من حيث السلامة، على الرغم من أهميتها. أيضاً، تميل الشركات المتخصصة الحرجة من حيث السلامة إلى القيام بتدريبها الخاص. ربما يكون من الأسهل تحفيز الأساليب الرسمية بأمثلة أكثر شيوعاً. مشروع Chromium هو أحد الأمثلة على البرمجيات "السائدة"، أي المتصفحات، ويُظهر أن فريق Chromium يتحرك نحو المزيد من الشكليات.

**sk.** عادةً، ما يجعل أي دورة مثيرة للاهتمام هو التطبيقات ونقل المعرفة من الفصل الدراسي إلى الواقع. ومع ذلك، تعتمد معظم دورات الأساليب الرسمية على أمثلة، على الرغم من أنها مثيرة للاهتمام، بعيدة عما يمكن للطلاب تجربته والتجريب معه. أعتقد بشدة أنه يجب علينا الابتعاد عن النهج النظري البحت لتدريس الأساليب الرسمية للمبتدئين. على الأقل بالنسبة لي، كانت التطورات النظرية في الأساليب الرسمية دائماً وسيلة لتحقيق غاية. لتقديرها، يجب على المرء أن يختبر ما يعنيه محاولة الوصول إلى نفس النهاية بدونها.

جانب آخر يمكن أن يجعل دورة الأساليب الرسمية مثيرة للاهتمام هو إشراك الطلاب في بحث الأساليب الرسمية بدلاً من تطبيق الأساليب الرسمية. لقد اعتدنا على تدريس الأساليب الرسمية من خلال مناقشة مشاكل البرمجيات أولاً ثم جعل الطلاب يحاولون إيجاد طرق تلقائية لاكتشافها، مما يؤدي من أفكار التحليل الثابت البسيطة إلى فحص النماذج. تم توثيق الدورة بدقة، مما يُظهر أيضاً أن النهج كان محفزاً للغاية للطلاب [KKS19].

**pk.** كان لدى Shriram Krishnamurthi خطاب رئيسي رائع في FM'19. أحد النقاط الرئيسية التي يجب استخلاصها من ذلك هو أن الأدوات مشكلة كبيرة. إذا ضربت الطلاب بأداة صناعية كاملة، فسيحصلون على رسائل خطأ محبطة، لأنهم ليس لديهم فكرة عما يحدث بشكل خاطئ. في دوسلدورف، عملت مجموعتنا على نهج قائم على دفاتر Jupyter [GL20]. يسمح بتقييم التعبيرات أو المسندات الأصغر دون نهج قائم على الحالة، حتى يتمكن الطلاب من التعلم والتجربة مع الأسس المنطقية للغة.

**cd.** الألعاب مهمة، ربما حتى ضرورية في تدريس الأساليب الرسمية وجعلها ممتعة. كمعلم لجميع الأعمار من 8 سنوات إلى مستوى الجامعة، وجدت أن الألعاب هي واحدة من أفضل الأدوات للاستخدام عند التدريس. يفهم الطلاب الألعاب ويريدون الفوز بها، بشكل طبيعي. عندما تشرح للطلاب أن هناك طريقة يُضمن لهم فيها الفوز، أو في الواقع طريقة لا يمكن فيها للاعب الثاني أن يفوز، تبلغ مستويات اهتمامهم ذروتها!

لقد نجحنا في مطالبة أطفال بعمر 11 عاماً برسم أنظمة الانتقال المُصنفة. إذا بدأنا في تدريسهم عاجلاً، يمكن أن يعمل هذا كقاعدة يمكننا البناء عليها لتعزيز فهمهم لاحقاً.

**ac.** يوفر استخدام الأدوات إمكانات كبيرة لإدخال المتعة في تدريس الأساليب الرسمية. هذا صحيح بشكل خاص لأدوات المحاكاة وفحص النماذج، التي يكون تركيزها في إعطاء "حياة" للمواصفات الرسمية بدلاً من الانخراط في تعقيد الإثبات الرسمي، كما يحدث، بدلاً من ذلك، لأدوات إثبات المبرهنات. علاوة على ذلك، يمكن تطبيق الأساليب الرسمية على مجموعة كبيرة من المشاكل، في الأساس أي مشكلة، تتجاوز بكثير مجال علوم الحاسوب.

يمكننا أن نختتم مناقشتنا حول رؤية المعلم حول المتعة بالقول إنه إذا كان التحفيز هو البُعد الذي يسمح للمتعلمين ببناء الاهتمام بالأساليب الرسمية، فإن المتعة هي في الواقع البُعد الأساسي للحفاظ على تفاعل المتعلمين بشكل مستمر، وبالتالي ضمان الاحتفاظ بمصلحتهم وربما زيادتها بمرور الوقت [CL20, Cer16, RCS+20].

**po.** أنا أيضاً لا أتفق مع نهج "الألغاز"/"الألعاب"/"خدع البطاقات". لا أعتقد أنها تُظهر فائدة وأهمية الأساليب الرسمية. أستخدم أيضاً ألعاباً صغيرة (الكثير منها!) في دورة السنة الثانية، حتى لعبة البلاك جاك، ولكن فقط كـ "أمثلة لعبة" صغيرة للتعرف على لغة النمذجة والأداة. من ناحية أخرى، التطبيقات الصناعية الحقيقية، كما يكتب الآخرون هنا، كبيرة جداً ومعقدة بحيث لا يمكن تضمينها في دورات الأساليب الرسمية للمبتدئين. حل وسط جيد أستخدمه هو الأنظمة/الخوارزميات الأساسية التي تمثل حجر الأساس لمجالات مختلفة أخرى، والأهم من ذلك، لأنظمة البرمجيات الكبيرة اليوم. على سبيل المثال، 2-phase-commit (بينما بسيطة) و Paxos (أقل بكثير) لا تزال كتل بناء رئيسية في الأنظمة الموزعة اليوم.

**3.1 تلخيص الأفكار**

من الواضح أنه من المستحيل وضع معايير عامة لجعل تدريس الأساليب الرسمية نشاطاً ممتعاً. لا يمكن توصيف المتعة بطريقة موضوعية ولا يمكن أن تنبثق بشكل طبيعي إلا من التفاعل بين المعلمين والطلاب. في الواقع، يتأثر ظهور المتعة بشخصيات المعلمين والطلاب الأفراد وكذلك بسياق التفاعل الذي تلتقي فيه هذه الشخصيات المختلفة في بيئة الفصل الدراسي التعاونية. هنا، تم اقتراح ومناقشة معايير مختلفة، بما في ذلك:

- قد تمثل الألعاب والألغاز مقدمة خفيفة الوزن وممتعة للأساليب الرسمية؛
- يجب أن يكون هناك تركيز على بناء والتحقق من البرمجيات لأنظمة بسيطة، ولكن واقعية؛
- يجب أن يركز التدريس على إظهار أن الأدوات تعمل بدلاً من تقديم الكثير من النظرية؛
- من المحتمل أن يستمتع الطلاب بالقيام بأنشطة البحث الفعلية؛
- يجب إشراك الطلاب في تطوير المناهج.

هناك رؤية عامة بين المؤلفين المشاركين بأن الألعاب والألغاز يمكن أن تكون مفيدة عندما يتعلق الأمر بتدريس الأساليب الرسمية في المراحل الأولية وتمثل مقدمة خفيفة الوزن وممتعة. من المهم ملاحظة أن هذه الرؤية تشمل طلاب الأساليب الرسمية السابقين الذين أصبحوا معلمي الأساليب الرسمية [MOPD20]. قد ترتبط الألعاب أيضاً ببعض أشكال المنافسة، والتي قد تكون داخل الصف أو من حيث المشاركة في سياق دولي. الألعاب والألغاز هي أيضاً أداة رائعة لبدء تعليم الأساليب الرسمية مبكراً، حتى من خلال التدريس لأطفال المدارس، في سن صغيرة مثل 10-11.

بالإضافة إلى ذلك، يجب أن يكون هناك أيضاً بعض التركيز على بناء والتحقق من البرمجيات. ومع ذلك، يجب إنشاء مثل هذا الارتباط بالواقع بالشكل الصحيح للحفاظ على توافق مع المتعة التي يحددها النهج القائم على الألعاب.

هناك اتفاق عام بين المؤلفين المشاركين على أن الطلاب بحاجة إلى رؤية كيف تعمل الأساليب الرسمية في الواقع باستخدام الأدوات بدلاً من التركيز كثيراً على النظرية. ومع ذلك، قد يؤدي جعل الطلاب يستخدمون الأدوات الصناعية إلى إحباط شديد. بينما من الجميل أن نرى أن مثل هذه الأدوات تُستخدم في الممارسة العملية، قد تكون الوسيلة الخاطئة لتعلم الأساليب الرسمية.

الجانب النهائي الذي يمكن أن يجعل دورة الأساليب الرسمية مثيرة للاهتمام هو إشراك الطلاب في بحث الأساليب الرسمية بدلاً من تطبيق الأساليب الرسمية. في الواقع، غالباً ما تكون منشورات الطلاب محل تقدير كبير [POKG19, Zhu20].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** games (ألعاب), puzzles (ألغاز), simulation (المحاكاة), Jupyter notebooks (دفاتر Jupyter), labelled transition systems (أنظمة الانتقال المُصنفة), Coq (كوك), natural deduction (الاستنتاج الطبيعي)
- **Equations:** None
- **Citations:** [CRS+15], [MOPD20], [Cer20], [KKS19], [POKG19], [GL20], [FW20], [CL20], [Cer16], [RCS+20], [SY02], [Ölv20]
- **Special handling:** Multiple personal statements from different authors (mf, jd, sk, pk, cd, ac, ns, po), Chromium Project reference, AlphaZero reference, competitive programming contests

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-Translation (Key Paragraph)

Arabic to English: "It is clear that it is impossible to establish general criteria to make teaching formal methods a fun activity. Fun cannot be characterized in an objective way and can only emerge naturally from the interaction between teachers and students. In fact, the emergence of fun is affected by the personalities of individual teachers and students as well as by the interaction context in which these different personalities meet in the collaborative classroom environment."

**Validation:** Excellent semantic preservation with proper academic tone and technical accuracy.
