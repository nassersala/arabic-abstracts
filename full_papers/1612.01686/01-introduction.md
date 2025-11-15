# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods, safety-critical systems, human factors, specification, framework, testing, software engineering, automation, formal specification, API

---

### English Version

Specifying safety-critical systems, it is not enough to use controlled languages and semiformal languages – the precise and easy-to-read formal specification is essential to ensure that the safety properties of the system really hold. Moreover, the software development process should include aspects of human factors engineering, to improve the quality of software and to deal with human factors in a systematic way, cf. [25]. Human factor aspects usually cover the design of human-computer interface of the software, human-related aspects of the development process, as well as the corresponding automatisation. By the Engineering Error Paradigm [20], humans are seen as a "component of the system" (almost equivalent to software and hardware components in the sense of operation with data and other components), which is the most unreliable in the system.

Software errors can cause wasting of resources [19,6]. An estimate of one trillion US dollars was spent on IT hardware, software and services by governments around the world. Software errors can also be fatal, and in many cases they might be prevented by having a more human-oriented development process and methods. As per statistics presented by Dhillon [8], humans are responsible for 30% to 60% the total errors which directly or indirectly lead to the accidents, and in the case of aviation and traffic accidents, 80% to 90% of the errors were due to humans. Thus, it is necessary to have human factors engineering as a part of the software development process. One of the widely cited accidents in safety-critical systems are the accidents involved massive radiation overdoses by the Therac-25 (a radiation therapy machine used in curing cancer) that lead to deaths and serious injuries of patients which received thousand times the normal dose of radiation [17,16]. The causes of these accidents were software failures as well as problems with the system interface. The error was improbable to reproduce because it required very specific sequence of commands in order to occur. The improbability of the sequence makes the error unlikely to be noticed with manual testing because it is almost impossible to think of all combinations of commands and edge cases. Automatisation might solve this problem, but the challenge is to create an automatisation which is not only efficient but also easy-to-use, i.e., is human-oriented.

One of the challenges in software engineering is to develop correct software. The software should meet user requirements, its properties should satisfy the model corresponding to design objective and the implementation should pass all functional tests. Rigorous reasoning is the only way to avoid subtle errors in algorithms, and it should be as simple as possible by making the underlying formalism simple tools [14]. Formal methods (FMs) refer to a class of mathematical techniques used in development of large scale complex systems. These techniques can result in high-quality systems that can be implemented on-time, within budgets and satisfy user requirements [4].

The value of FMs in real systems has far reaching consequences. For instance, FMs help engineers get the code right by getting the design right in the first place. Secondly, FMs help engineers gain a better understanding of the design. Despite all advantages, formal methods are not widely used in large-scale industrial software projects for many reasons [27]. One of the core obstacles is the lack of readability and usability. The syntax of FMs is often too complicated and unreadable for novices, which makes an impression that all the FMs require huge amount of training. There also is a prejudice that the return of investment is very minimal and only justified in critical systems such as medical devices, what is generally not true [18].

Spatio-temporal aspects of safety-critical systems are crucial to verify and to test a system, as in most cases the system properties should be analysed in relation to the time and to the location. To analyse spatio-temporal phenomena, we have to specify the corresponding spatial, temporal and event semantics formally and in a human-oriented way. The goal of our work is to increase usability of the analysis (in the sense of verification and testing) of the spatio-temporal aspects on the base of the corresponding formal models.

Property based testing allows us to generate huge numbers of system operations (e.g API calls or external events) and permute these operations in ways that is difficult for humans to think of. These combinations are then used to verify the system under test according to the spatio-temporal specification.

**Contributions:** The proposed framework will help to reduce the impedance mismatch between formal methods and model-based representations and system code, which in turn will help in increasing the adoption rate by practitioners. Our framework aims at providing a set of application programming interfaces (APIs) to map programming language constructs to the formal methods representation. The usability of formal methods will be improved indirectly, as the formal method constructs will be expressed in terms of system code.

---

### النسخة العربية

عند تحديد مواصفات الأنظمة الحرجة للسلامة، لا يكفي استخدام اللغات المحكومة واللغات شبه الرسمية - بل إن المواصفات الرسمية الدقيقة وسهلة القراءة ضرورية لضمان أن خصائص السلامة للنظام تتحقق فعلياً. علاوة على ذلك، يجب أن تتضمن عملية تطوير البرمجيات جوانب من هندسة العوامل البشرية، لتحسين جودة البرمجيات والتعامل مع العوامل البشرية بطريقة منهجية، راجع [25]. تغطي جوانب العوامل البشرية عادةً تصميم واجهة الإنسان-الحاسوب للبرمجيات، والجوانب المتعلقة بالإنسان في عملية التطوير، بالإضافة إلى الأتمتة المقابلة. وفقاً لنموذج خطأ الهندسة [20]، يُنظر إلى البشر على أنهم "مكون من النظام" (ما يعادل تقريباً مكونات البرمجيات والأجهزة من حيث العمل مع البيانات والمكونات الأخرى)، وهو المكون الأكثر عدم موثوقية في النظام.

يمكن أن تتسبب أخطاء البرمجيات في هدر الموارد [19،6]. تشير التقديرات إلى أن تريليون دولار أمريكي تم إنفاقه على أجهزة تكنولوجيا المعلومات والبرمجيات والخدمات من قبل الحكومات حول العالم. يمكن أن تكون أخطاء البرمجيات أيضاً مميتة، وفي كثير من الحالات يمكن الوقاية منها من خلال عملية وطرق تطوير أكثر توجهاً نحو الإنسان. وفقاً للإحصائيات المقدمة من Dhillon [8]، البشر مسؤولون عن 30٪ إلى 60٪ من إجمالي الأخطاء التي تؤدي بشكل مباشر أو غير مباشر إلى الحوادث، وفي حالة حوادث الطيران والمرور، كانت 80٪ إلى 90٪ من الأخطاء بسبب البشر. لذلك، من الضروري أن تكون هندسة العوامل البشرية جزءاً من عملية تطوير البرمجيات. أحد الحوادث المشهورة في الأنظمة الحرجة للسلامة هو الحوادث التي تضمنت جرعات إشعاع زائدة ضخمة من جهاز Therac-25 (جهاز علاج إشعاعي يُستخدم في علاج السرطان) والتي أدت إلى وفيات وإصابات خطيرة للمرضى الذين تلقوا ألف ضعف الجرعة الطبيعية من الإشعاع [17،16]. كانت أسباب هذه الحوادث هي فشل البرمجيات بالإضافة إلى مشاكل في واجهة النظام. كان من غير المحتمل إعادة إنتاج الخطأ لأنه يتطلب تسلسلاً محدداً جداً من الأوامر حتى يحدث. عدم احتمالية التسلسل يجعل من غير المحتمل ملاحظة الخطأ من خلال الاختبار اليدوي لأنه من المستحيل تقريباً التفكير في جميع تركيبات الأوامر والحالات الحدية. قد تحل الأتمتة هذه المشكلة، لكن التحدي يكمن في إنشاء أتمتة ليست فعالة فحسب، بل سهلة الاستخدام أيضاً، أي موجهة نحو الإنسان.

أحد التحديات في هندسة البرمجيات هو تطوير برمجيات صحيحة. يجب أن تلبي البرمجيات متطلبات المستخدم، ويجب أن تفي خصائصها بالنموذج المقابل لهدف التصميم ويجب أن تنجح في جميع الاختبارات الوظيفية. التفكير الدقيق هو الطريقة الوحيدة لتجنب الأخطاء الدقيقة في الخوارزميات، ويجب أن يكون بسيطاً قدر الإمكان من خلال جعل الأدوات الشكلية الأساسية بسيطة [14]. تشير الأساليب الرسمية (FMs) إلى فئة من التقنيات الرياضية المستخدمة في تطوير الأنظمة المعقدة واسعة النطاق. يمكن أن تؤدي هذه التقنيات إلى أنظمة عالية الجودة يمكن تنفيذها في الوقت المحدد، ضمن الميزانيات وتلبية متطلبات المستخدم [4].

قيمة الأساليب الرسمية في الأنظمة الحقيقية لها عواقب بعيدة المدى. على سبيل المثال، تساعد الأساليب الرسمية المهندسين في الحصول على الشفرة الصحيحة من خلال الحصول على التصميم الصحيح من البداية. ثانياً، تساعد الأساليب الرسمية المهندسين في اكتساب فهم أفضل للتصميم. على الرغم من جميع المزايا، لا تُستخدم الأساليب الرسمية على نطاق واسع في مشاريع البرمجيات الصناعية واسعة النطاق لأسباب عديدة [27]. أحد العوائق الأساسية هو نقص قابلية القراءة وسهولة الاستخدام. غالباً ما تكون صيغة الأساليب الرسمية معقدة جداً وغير قابلة للقراءة بالنسبة للمبتدئين، مما يعطي انطباعاً بأن جميع الأساليب الرسمية تتطلب قدراً هائلاً من التدريب. هناك أيضاً تحيز بأن عائد الاستثمار ضئيل جداً ولا يكون مبرراً إلا في الأنظمة الحرجة مثل الأجهزة الطبية، وهو ما ليس صحيحاً بشكل عام [18].

الجوانب الزمكانية للأنظمة الحرجة للسلامة حاسمة للتحقق من النظام واختباره، حيث يجب تحليل خصائص النظام في معظم الحالات فيما يتعلق بالوقت والموقع. لتحليل الظواهر الزمكانية، يجب علينا تحديد الدلالات المكانية والزمنية ودلالات الأحداث المقابلة بشكل رسمي وبطريقة موجهة نحو الإنسان. الهدف من عملنا هو زيادة قابلية استخدام التحليل (بمعنى التحقق والاختبار) للجوانب الزمكانية على أساس النماذج الرسمية المقابلة.

يتيح لنا الاختبار القائم على الخصائص توليد أعداد هائلة من عمليات النظام (مثل استدعاءات واجهة برمجة التطبيقات أو الأحداث الخارجية) وتبديل هذه العمليات بطرق يصعب على البشر التفكير فيها. تُستخدم هذه التركيبات بعد ذلك للتحقق من النظام قيد الاختبار وفقاً للمواصفات الزمكانية.

**المساهمات:** سيساعد إطار العمل المقترح في تقليل عدم التوافق بين الأساليب الرسمية والتمثيلات القائمة على النماذج وشفرة النظام، مما سيساعد بدوره في زيادة معدل الاعتماد من قبل الممارسين. يهدف إطارنا إلى توفير مجموعة من واجهات برمجة التطبيقات (APIs) لربط تراكيب لغة البرمجة بتمثيل الأساليب الرسمية. سيتم تحسين قابلية استخدام الأساليب الرسمية بشكل غير مباشر، حيث سيتم التعبير عن تراكيب الأساليب الرسمية من حيث شفرة النظام.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** spatio-temporal models, formal methods, property-based testing, human factors engineering, safety-critical systems, impedance mismatch
- **Equations:** None
- **Citations:** [4, 6, 8, 14, 17, 18, 19, 20, 25, 27]
- **Special handling:** Therac-25 case study mentioned as key example

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
