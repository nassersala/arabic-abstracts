# Section 5: Syllabus of a Compulsory Formal Methods Course
## القسم 5: منهج لمقرر إلزامي في الأساليب الرسمية

**Section:** syllabus
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods (الأساليب الرسمية), syllabus (منهج), verification (التحقق), validation (التحقق من الصحة), specifications (المواصفات)

---

### English Version (Summary)

Besides increasing the visibility of formal methods throughout all courses and also having specialised advanced courses on formal methods, we suggest that curricula for computer science and software engineering should include a compulsory formal methods course.

The target audience for such a compulsory formal methods course would be the complete cohort of computer science/software engineering students in year 2 or year 3 of a 3-year BSc degree programme.

Due to the wealth of available formal methods, we refrain from proposing a unified or 'standard' syllabus. Local expertise in specific formal methods and application domains should be taken into account. Therefore, we rather capture the essence of an ideal course in a generic way:

**Introduction:**
- The role of formal methods in software engineering context
- Success stories of formal methods
- Relating formal methods to current trends (machine learning, big data)

**Main Part:**
The main part should offer one or two formal methods of different nature (e.g., "model-oriented" and "property-oriented"). Topics to cover:
- Modelling: going from informal to formal; traceability; validation
- Language design: expressivity vs. syntactic sugar
- Semantics: presenting essentials
- Software engineering context: formal methods throughout software lifecycle
- Method: systematically using tools
- Application domains: safety, security, HCI, e-contracts, non-computer areas

**Conclusion – Reflection on formal methods:**
- General limitations: what formal methods can/cannot deliver
- Scalability: toy examples vs. real-life challenges
- Costs/benefits: ROI of formal methods
- Acceptance: current uptake in industry
- Current trends: future of formal methods

**Learning outcomes:**
Students should:
- understand the thinking behind formal methods
- be fluent in applying one or two formal methods
- estimate the potential of formal methods for concrete challenges
- critically compare different formal approaches

---

### النسخة العربية

إلى جانب زيادة رؤية الأساليب الرسمية في جميع المقررات وكذلك وجود مقررات متقدمة متخصصة في الأساليب الرسمية، نقترح أن تتضمن مناهج علوم الحاسوب وهندسة البرمجيات مقرراً إلزامياً في الأساليب الرسمية.

سيكون الجمهور المستهدف لمثل هذا المقرر الإلزامي في الأساليب الرسمية هو المجموعة الكاملة من طلاب علوم الحاسوب/هندسة البرمجيات في السنة 2 أو السنة 3 من برنامج درجة بكالوريوس العلوم لمدة 3 سنوات.

نظراً لوفرة الأساليب الرسمية المتاحة، نمتنع عن اقتراح منهج موحد أو "قياسي". يجب أخذ الخبرة المحلية في أساليب رسمية ومجالات تطبيق محددة في الاعتبار. لذلك، نلتقط بالأحرى جوهر المقرر المثالي بطريقة عامة:

**المقدمة:**
- دور الأساليب الرسمية في سياق هندسة البرمجيات، انظر، على سبيل المثال، Roggenbach وآخرون [RCS+20]، الفصل 1، للحصول على مناقشة شاملة، و Barnes [Bar11] لدراسة حالة مقارنة.
- قصص نجاح الأساليب الرسمية، انظر، على سبيل المثال، Roggenbach وآخرون [RCS+20] لمجموعة من هذه القصص.
- ربط الأساليب الرسمية بالاتجاهات الحالية في علوم الحاسوب، مثل التعلم الآلي، حيث يمكن للمرء استخدام التعلم الآلي لتحسين الأساليب الرسمية [ALB18]، أو، مجال ناشئ ولكنه ينمو في الأهمية، تطبيق الأساليب الرسمية على البيانات الضخمة [vdA16, Cam14, MLM18] أو على التعلم الآلي [HKW17, SKS19, WPW+18].

**الجزء الرئيسي:**
يجب أن يقدم الجزء الرئيسي أسلوباً رسمياً واحداً أو اثنين من طبيعة مختلفة، على سبيل المثال، "موجه نحو النموذج" و"موجه نحو الخاصية"، راجع [Win90] لمزيد من المناقشة حول هذا التصنيف؛ لإظهار "عالمية" الأساليب الرسمية، سيكون من المفيد استخلاص أمثلة من مجالات مختلفة.

يجب تغطية الموضوعات التالية (مدرجة بدون ترتيب معين):
- **النمذجة:** الانتقال من غير الرسمي إلى الرسمي؛ إمكانية التتبع؛ التحقق من صحة النماذج.
- **تصميم اللغة:** شرح كيفية تصميم لغة أسلوب رسمي لأغراض محددة (ما هي الأساسيات الضرورية للتعبيرية، ما هي السكر النحوي الذي يسهل حياة المحدِّد؟).
- **الدلالات:** تقديم الأساسيات فقط - يجب أن يكون هذا موضوعاً واحداً من بين العديد وليس المهيمن، كما يحدث كثيراً في الممارسة الحالية.
- **سياق هندسة البرمجيات:** إظهار أن الأساليب الرسمية قابلة للتطبيق طوال دورة حياة البرمجيات بأكملها، على سبيل المثال، في تحليل التصميمات، في التحقق من البرمجيات، الاختبار من النماذج الرسمية.
- **الطريقة:** استخدام الأدوات بشكل منهجي لتوضيح جانب "الطريقة".
- **مجالات التطبيق:** توضيح مدى الأساليب الرسمية من خلال اختيار أمثلة من مجالات تطبيق مختلفة. السلامة، والأمن، والتفاعل بين الإنسان والحاسوب، والعقود الإلكترونية، والمجالات غير الحاسوبية (الأنظمة البيولوجية، البيئة، الكيمياء) هي بعض الأمثلة الممكنة.

تقليدياً، يدعو تدريس الأساليب الرسمية إلى استخدام الأساليب الرسمية للأنظمة الحرجة من حيث السلامة. الأساليب الرسمية مهمة للغاية بالطبع لتلك الأنظمة، لكن الخبرة في الصف (وغير ذلك) تشير إلى أن هذا لا يلهم وهو شبه مضاد للإنتاجية: معظم الطلاب لا يتوقعون تصميم نطاق ضيق جداً من الأنظمة الحرجة من حيث السلامة التي نميل إلى استخدامها كمثال (الطائرات، السيارات، الأجهزة الطبية، إلخ)؛ التركيز بشكل حصري تقريباً على الأنظمة الحرجة من حيث السلامة يمكن أن يكون في الواقع مضاداً للإنتاجية لأنه (يمكن أن يُنظر إليه على أنه) يرسل إشارات بأن الأساليب الرسمية قابلة للاستخدام فقط لمثل هذه الأنظمة.

نظراً لأن فشل الأمن السيبراني يحظى بتغطية كبيرة في الأخبار، قد ننظر إلى هذه ونرى كيف قد تكون الأساليب الرسمية قد وجدت هذه (على سبيل المثال Heartbleed)، أو يتم استخدامها (على سبيل المثال Chromium)، كطريقة للتأكيد على الفائدة السائدة للأساليب الرسمية.

**الخاتمة – التأمل في الأساليب الرسمية:**
نقدم أدناه بعض العناصر ذات الطبيعة التأملية التي يجب معالجتها في نهاية مقرر الأساليب الرسمية:
- **القيود العامة:** ما يمكن أن تقدمه الأساليب الرسمية، ما لا يمكن أن تقدمه الأساليب الرسمية، على سبيل المثال، بناءً على مقالة Levenson الاستفزازية "هل أنت متأكد من أن برمجياتك لن تقتل أحداً؟" [Lev20].
- **قابلية التوسع:** لماذا تعمل الأساليب الرسمية على الأمثلة التعليمية لكن تطبيقها قد يصبح مستحيلاً لأسباب تقنية عندما يتعلق الأمر بتحديات الحياة الواقعية، انظر، على سبيل المثال، [RMS+12] و[JMN+14].
- **التكاليف/الفوائد:** ما هي تكلفة والفوائد المالية للأساليب الرسمية [Bar11]. الرؤية الرئيسية "الأساليب الرسمية ممكنة بشكل مدهش لتطوير البرمجيات السائدة وتعطي عائداً جيداً على الاستثمار." من Newcombe وآخرون [NRZ+15] وعبارة أمازون "يمكننا الآن استخدام الاستدلال الآلي لتوفير ضمان غير مكلف وقابل للإثبات للعملاء" من J. Backes وآخرون [BBC+19] ربما تكون "يجب أن تكون موجودة"!
- **القبول:** الاستيعاب الحالي للأساليب الرسمية في الصناعة وأسباب القبول المنخفض.
- **الاتجاهات الحالية:** حيث يتوقع المرء أن يكون مجال الأساليب الرسمية، على سبيل المثال، في عقد من الزمان.

سيكون لكل محاضر رؤيته/رؤيتها الذاتية الخاصة فيما يتعلق بالقائمة أعلاه من الموضوعات. ربما تقدم نقطة جيدة للنقاش مع الطلاب. العنصر المنهجي الذي يقوم عليها هو أنه يجب معالجتها في نهاية مقرر الأساليب الرسمية.

**نتائج التعلم:**
مثل هذا المقرر سيوفر نتائج التعلم التي يحققها الطلاب:
- يفهمون التفكير وراء الأساليب الرسمية وكيف يختلف عن البرمجة المخصصة؛
- يتقنون تطبيق أسلوب رسمي واحد أو اثنين على أمثلة أكاديمية؛
- قادرون على تقدير إمكانات الأساليب الرسمية مع التحديات الملموسة؛
- قادرون على المقارنة النقدية بين النُهج الرسمية المختلفة واختيار الأنسب لتطبيق معين محدد.

---

### Translation Notes

- **Key terms:** compulsory course (مقرر إلزامي), learning outcomes (نتائج التعلم), model-oriented (موجه نحو النموذج), property-oriented (موجه نحو الخاصية), ROI (عائد على الاستثمار), software lifecycle (دورة حياة البرمجيات)
- **Citations:** [RCS+20], [Bar11], [ALB18], [vdA16], [Cam14], [MLM18], [HKW17], [SKS19], [WPW+18], [Win90], [Lev20], [RMS+12], [JMN+14], [NRZ+15], [BBC+19]

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
