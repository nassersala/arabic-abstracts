# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.88
**Glossary Terms Used:** formal methods, specification, property-based testing, validation, QuickCheck, TLA+, model checker, abstraction

---

### English Version

## 2.1 Formal Methods

Formal methods were introduced as a means of clearly specifying system requirements. Hinchey [10] argues that although formal methods are essential in the development of critical systems, they have not achieved the level of acceptance, nor level of use, that many believe they should. The uptake of formal methods has been far from ideal because many still believe that formal methods are difficult to use and require great mathematical expertise [10]. Spichkova reports [21] that in many cases simple changes of a specification method can make it more understandable and usable. She argues that such a simple kind of optimisation is often overlooked just because of its obviousness, and it would be wrong to ignore the possibility to optimise the language without much effort. For example, simply adding an enumeration to the formulas in a large formal specification makes its validation on the level of specification and discussion with cooperating experts much easier.

Hinchey [10] also assert that in addition to the benefits of abstraction, clarification, and disambiguation, using formal methods at the formal specification level are invaluable documentation that greatly assist future system maintenance. This research incorporates specifications used in property-based testing to further help in precisely documenting the system.

Lamport [14] states two reasons for using formal methods formulas instead of programming language tailored to the specific problem:

– Specialized languages often have limited realms of applicability. A language that permits a simple specification for one system require a very complicated one for a different kind of system. The Duration Calculus seems to work well for real-time properties; but it cannot express simple liveness properties. A formalism like TLA+ that, with no built-in primitives for real-time systems or procedures, can easily specify gas burner for example, it is not likely to have difficulty with a different kind of gas burner.

– Formalisms are easy to invent. However, practical methods must have a precise language and robust tools.

There are many examples where applying formal methods has lead to increasing reliability of systems. For example, a model checker TLC was developed for TLA formula was used to find errors in the cache coherence protocol for a Compaq multiprocessor [26]. In addition, [4] includes many examples of successfully using formal methods to design systems.

## 2.2 Property-Based Testing

There are many styles in testing software. One popular style is that of example based testing. In this style, test cases requires one to provide an example scenario for each feature. That is, each example may exercise one feature of the system under test and the test runs only once with relevant input. Dually, property based testing allows for the use of randomly generated tests based on system properties to test systems against their specifications and one test can run hundreds of times with different input values. An example of such library in Haskell programming language is QuickCheck. Hughes (inventor of QuickCheck) showed that using this library allowed him to discover hundreds of bugs in critical systems such as automobiles and the DropBox file sharing service [7]. However, QuickCheck uses Haskell programming language specific constructs (such as arrays, integers) and more complicated data types (such as algebraic data types) to model the specification of a system. Therefore, this research will investigate the possibility to have formal models (BeSpaceD, TLA+ or FocusST formulas) as specifications instead of Haskell constructs, as well as applicability of this approach for property based testing of real systems.

Hughes [12] asserts that Dijkstra was wrong when he claimed that testing can never demonstrate the absence of bugs in software, only their presence. Hughes argues that if we test properties that completely specify a function (such as the properties of reversing a list) then property based testing will eventually find every possible bug. In practice this is not true, since we usually do not have a complete specification, but this style of testing is very effective in exploring scenarios that no human can think of trying.

QuickCheck started as a testing framework for testing pure functional programs [7]. However, recent development in the area of property-based testing [9,13] incorporates the state-fulness of systems. That allowed for the testing of state-ful systems and even test programs written in imperative languages such as C. Hughes assert that testing state-ful systems is challenging. He argues that the state is an implicit argument to and result from every API call, yet it is not directly accessible to the test code. Therefore, his solution was to model the state abstractly and introduce state transition function that model the operations in API under test.

However, the state transition in QuickCheck is modelled manually using pre, post and next functions for every operation in the system under test. On the other hand, our framework will generate these transitions automatically using specification formulas.

---

### النسخة العربية

## 2.1 الأساليب الرسمية

تم تقديم الأساليب الرسمية كوسيلة لتحديد متطلبات النظام بوضوح. يجادل Hinchey [10] بأنه على الرغم من أن الأساليب الرسمية ضرورية في تطوير الأنظمة الحرجة، إلا أنها لم تحقق مستوى القبول، ولا مستوى الاستخدام، الذي يعتقد الكثيرون أنها يجب أن تحققه. لم يكن اعتماد الأساليب الرسمية مثالياً لأن الكثيرين لا يزالون يعتقدون أن الأساليب الرسمية صعبة الاستخدام وتتطلب خبرة رياضية كبيرة [10]. تفيد Spichkova [21] أن التغييرات البسيطة في طريقة المواصفات في كثير من الحالات يمكن أن تجعلها أكثر قابلية للفهم والاستخدام. تجادل بأن هذا النوع البسيط من التحسين غالباً ما يتم تجاهله بسبب وضوحه، وسيكون من الخطأ تجاهل إمكانية تحسين اللغة دون بذل الكثير من الجهد. على سبيل المثال، مجرد إضافة ترقيم إلى الصيغ في مواصفات رسمية كبيرة يجعل التحقق من صحتها على مستوى المواصفات والنقاش مع الخبراء المتعاونين أسهل بكثير.

يؤكد Hinchey [10] أيضاً أنه بالإضافة إلى فوائد التجريد والتوضيح وإزالة الغموض، فإن استخدام الأساليب الرسمية على مستوى المواصفات الرسمية يوفر توثيقاً لا يقدر بثمن يساعد بشكل كبير في صيانة النظام في المستقبل. يدمج هذا البحث المواصفات المستخدمة في الاختبار القائم على الخصائص لمزيد من المساعدة في توثيق النظام بدقة.

يذكر Lamport [14] سببين لاستخدام صيغ الأساليب الرسمية بدلاً من لغة البرمجة المصممة خصيصاً للمشكلة المحددة:

- غالباً ما يكون للغات المتخصصة نطاقات تطبيق محدودة. اللغة التي تسمح بمواصفات بسيطة لنظام واحد تتطلب واحدة معقدة جداً لنوع مختلف من النظام. يبدو أن Duration Calculus يعمل بشكل جيد للخصائص الزمنية الفعلية؛ لكنه لا يمكنه التعبير عن خصائص الحيوية البسيطة. صيغة مثل TLA+ التي، بدون بنيات مدمجة للأنظمة الزمنية الفعلية أو الإجراءات، يمكنها بسهولة تحديد موقد غاز على سبيل المثال، فمن غير المرجح أن تواجه صعوبة مع نوع مختلف من موقد الغاز.

- من السهل ابتكار الصيغ الشكلية. ومع ذلك، يجب أن تحتوي الطرق العملية على لغة دقيقة وأدوات قوية.

هناك العديد من الأمثلة على أن تطبيق الأساليب الرسمية أدى إلى زيادة موثوقية الأنظمة. على سبيل المثال، تم تطوير فاحص النماذج TLC لصيغة TLA واستُخدم للعثور على أخطاء في بروتوكول التماسك في ذاكرة التخزين المؤقت لمعالج Compaq متعدد المعالجات [26]. بالإضافة إلى ذلك، يتضمن [4] العديد من الأمثلة على الاستخدام الناجح للأساليب الرسمية في تصميم الأنظمة.

## 2.2 الاختبار القائم على الخصائص

هناك العديد من الأساليب في اختبار البرمجيات. أحد الأساليب الشائعة هو الاختبار القائم على الأمثلة. في هذا الأسلوب، تتطلب حالات الاختبار من المرء توفير سيناريو مثال لكل ميزة. أي أن كل مثال قد يمارس ميزة واحدة من النظام قيد الاختبار ويعمل الاختبار مرة واحدة فقط مع المدخلات ذات الصلة. على العكس من ذلك، يسمح الاختبار القائم على الخصائص باستخدام اختبارات متولدة عشوائياً بناءً على خصائص النظام لاختبار الأنظمة مقابل مواصفاتها ويمكن أن يعمل اختبار واحد مئات المرات بقيم مدخلات مختلفة. مثال على مثل هذه المكتبة في لغة برمجة Haskell هو QuickCheck. أظهر Hughes (مخترع QuickCheck) أن استخدام هذه المكتبة سمح له باكتشاف مئات الأخطاء في الأنظمة الحرجة مثل السيارات وخدمة مشاركة الملفات DropBox [7]. ومع ذلك، يستخدم QuickCheck تراكيب خاصة بلغة برمجة Haskell (مثل المصفوفات والأعداد الصحيحة) وأنواع بيانات أكثر تعقيداً (مثل أنواع البيانات الجبرية) لنمذجة مواصفات النظام. لذلك، سيبحث هذا البحث في إمكانية استخدام النماذج الرسمية (صيغ BeSpaceD أو TLA+ أو FocusST) كمواصفات بدلاً من تراكيب Haskell، بالإضافة إلى قابلية تطبيق هذا النهج للاختبار القائم على الخصائص للأنظمة الحقيقية.

يؤكد Hughes [12] أن Dijkstra كان مخطئاً عندما ادعى أن الاختبار لا يمكنه أبداً إثبات عدم وجود أخطاء في البرمجيات، بل وجودها فقط. يجادل Hughes بأنه إذا اختبرنا الخصائص التي تحدد دالة بشكل كامل (مثل خصائص عكس قائمة) فإن الاختبار القائم على الخصائص سيجد في النهاية كل خطأ ممكن. في الممارسة العملية هذا ليس صحيحاً، حيث أننا عادة لا نمتلك مواصفات كاملة، لكن هذا النمط من الاختبار فعال جداً في استكشاف سيناريوهات لا يمكن لأي إنسان التفكير في تجربتها.

بدأ QuickCheck كإطار اختبار لاختبار البرامج الوظيفية النقية [7]. ومع ذلك، فإن التطوير الحديث في مجال الاختبار القائم على الخصائص [9،13] يدمج الحالات ذات الحالة للأنظمة. سمح ذلك باختبار الأنظمة ذات الحالة وحتى اختبار البرامج المكتوبة بلغات حتمية مثل C. يؤكد Hughes أن اختبار الأنظمة ذات الحالة أمر صعب. يجادل بأن الحالة هي وسيطة ضمنية ونتيجة من كل استدعاء لواجهة برمجة التطبيقات، ومع ذلك فهي غير متاحة بشكل مباشر لشفرة الاختبار. لذلك، كان حله هو نمذجة الحالة بشكل مجرد وتقديم دالة انتقال الحالة التي تنمذج العمليات في واجهة برمجة التطبيقات قيد الاختبار.

ومع ذلك، يتم نمذجة انتقال الحالة في QuickCheck يدوياً باستخدام دوال pre و post و next لكل عملية في النظام قيد الاختبار. من ناحية أخرى، سيولد إطار عملنا هذه الانتقالات تلقائياً باستخدام صيغ المواصفات.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** QuickCheck, Duration Calculus, TLC model checker, state transition functions, example-based testing vs property-based testing
- **Equations:** None
- **Citations:** [4, 7, 9, 10, 12, 13, 14, 21, 26]
- **Special handling:** Comparison between different testing paradigms and formal methods

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
