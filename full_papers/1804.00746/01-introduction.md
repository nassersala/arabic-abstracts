# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** automatic differentiation, backpropagation, deep learning, neural network, gradient, optimization, compiler, functional programming, derivative

---

### English Version

Introduction

Accurate, efficient, and reliable computation of derivatives has become increasingly important over the last several years, thanks in large part to the successful use of backpropagation in machine learning, including multi-layer neural networks, also known as "deep learning" [Lecun et al., 2015; Goodfellow et al., 2016]. Backpropagation is a specialization and independent invention of the reverse mode of automatic differentiation (AD) and is used to tune a parametric model to closely match observed data, using gradient descent (or stochastic gradient descent). Machine learning and other gradient-based optimization problems typically rely on derivatives of functions with very high dimensional domains and a scalar codomain—exactly the conditions under which reverse-mode AD is much more efficient than forward-mode AD (by a factor proportional to the domain dimension).

Unfortunately, while forward-mode AD (FAD) is easily understood and implemented, reverse-mode AD (RAD) and backpropagation have had much more complicated explanations and implementations, involving mutation, graph construction and traversal, and "tapes" (sequences of reified, interpretable assignments, also called "traces" or "Wengert lists"). Mutation, while motivated by efficiency concerns, makes parallel execution difficult and so undermines efficiency as well. Construction and interpretation (or compilation) of graphs and tapes also add execution overhead. The importance of RAD makes its current complicated and bulky implementations especially problematic. The increasingly large machine learning (and other optimization) problems being solved with RAD (usually via backpropagation) suggest the need to find more streamlined, efficient implementations, especially with the massive hardware parallelism now readily and inexpensively available in the form of graphics processors (GPUs) and FPGAs.

Another difficulty in the practical application of AD in machine learning (ML) comes from the nature of many currently popular ML frameworks, including Caffe [Jia et al., 2014], TensorFlow [Abadi et al., 2016], and Keras [Chollet, 2016]. These frameworks are designed around the notion of a "graph" (or "network") of interconnected nodes, each of which represents a mathematical operation—a sort of data flow graph. Application programs construct these graphs explicitly, creating nodes and connecting them to other nodes. After construction, the graphs must then be processed into a representation that is more efficient to train and to evaluate. These graphs are essentially mathematical expressions with sharing, hence directed acyclic graphs (DAGs). This paradigm of graph construction, compilation, and execution bears a striking resemblance to what programmers and compilers do all the time:

• Programs are written by a human.
• The compiler or interpreter front-end parses the program into a DAG representation.
• The compiler back-end transforms the DAGs into a form efficient for execution.
• A human runs the result of compilation.

When using a typical ML framework, programmers experience this sequence of steps at two levels: working with their code and with the graphs that their code generates. Both levels have notions of operations, variables, information flow, values, types, and parametrization. Both have execution models that must be understood.

A much simpler and cleaner foundation for ML would be to have just the programming language, omitting the graphs/networks altogether. Since ML is about (mathematical) functions, one would want to choose a programming language that supports functions well, i.e., a functional language, or at least a language with strong functional features. One might call this alternative "differentiable functional programming". In this paradigm, programmers directly define their functions of interest, using the standard tools of functional programming, with the addition of a differentiation operator (a typed higher-order function, though partial since not all computable functions are differentiable). Assuming a purely functional language or language subset (with simple and precise mathematical denotation), the meaning of differentiation is exactly as defined in traditional calculus.

How can we realize this vision of differentiable functional programming? One way is to create new languages, but doing so requires enormous effort to define and implement efficiently, and perhaps still more effort to evangelize. Alternatively, we might choose a suitable purely functional language like Haskell and then add differentiation. The present paper embodies the latter choice, augmenting the popular Haskell compiler GHC with a plugin that converts standard Haskell code into categorical form to be instantiated in any of a variety of categories, including differentiable functions [Elliott, 2017].

This paper makes the following specific contributions:

• Beginning with a simple category of derivative-augmented functions, specify AD simply and precisely by requiring this augmentation (relative to regular functions) to be homomorphic with respect to a collection of standard categorical abstractions and primitive mathematical operations.

• Calculate a correct-by-construction AD implementation from the homomorphic specification.

• Generalizing AD by replacing linear maps (general derivative values) with an arbitrary cartesian category [Elliott, 2017], define several AD variations, all stemming from different representations of linear maps: functions (satisfying linearity), "generalized matrices" (composed representable functors), continuation-based transformations of any linear map representation, and dualized versions of any linear map representation. The latter two variations yield correct-by-construction implementations of reverse-mode AD that are much simpler than previously known and are composed from generally useful components. The choice of dualized linear functions for gradient computations is particularly compelling in simplicity. It also appears to be quite efficient—requiring no matrix-level representations or computations—and is suitable for gradient-based optimization, e.g., for machine learning. In contrast to conventional reverse-mode AD algorithms, all algorithms in this paper are free of mutation and hence naturally parallel. A similar construction yields forward-mode AD.

---

### النسخة العربية

المقدمة

أصبح الحساب الدقيق والفعّال والموثوق للمشتقات ذا أهمية متزايدة على مدى السنوات الأخيرة، ويرجع ذلك إلى حد كبير إلى الاستخدام الناجح للانتشار العكسي في التعلم الآلي، بما في ذلك الشبكات العصبية متعددة الطبقات، المعروفة أيضاً باسم "التعلم العميق" [Lecun et al., 2015; Goodfellow et al., 2016]. الانتشار العكسي هو تخصيص واختراع مستقل للنمط العكسي من التفاضل الآلي (AD)، ويُستخدم لضبط نموذج معلمي ليطابق البيانات المرصودة عن كثب، باستخدام الانحدار التدرجي (أو الانحدار التدرجي العشوائي). تعتمد مسائل التعلم الآلي وغيرها من مسائل التحسين القائمة على التدرج عادةً على مشتقات الدوال ذات المجالات عالية الأبعاد ومجال مشترك قياسي - وهي بالضبط الظروف التي يكون فيها التفاضل الآلي ذو النمط العكسي أكثر كفاءة بكثير من التفاضل الآلي ذي النمط الأمامي (بعامل يتناسب مع بُعد المجال).

لسوء الحظ، بينما يسهل فهم وتنفيذ التفاضل الآلي ذي النمط الأمامي (FAD)، فإن التفاضل الآلي ذي النمط العكسي (RAD) والانتشار العكسي لهما تفسيرات وتنفيذات أكثر تعقيداً بكثير، تشمل التغيير، وبناء الرسوم البيانية واجتيازها، و"الأشرطة" (تسلسلات من الإسنادات القابلة للتفسير، تسمى أيضاً "التتبعات" أو "قوائم Wengert"). التغيير، رغم أنه مدفوع بدواعي الكفاءة، يجعل التنفيذ المتوازي صعباً وبالتالي يقوض الكفاءة أيضاً. كما أن بناء وتفسير (أو ترجمة) الرسوم البيانية والأشرطة يضيف حمل تنفيذ إضافي. إن أهمية RAD تجعل تنفيذاته المعقدة والضخمة الحالية إشكالية بشكل خاص. تشير مسائل التعلم الآلي الكبيرة المتزايدة (ومسائل التحسين الأخرى) التي يتم حلها باستخدام RAD (عادةً عبر الانتشار العكسي) إلى الحاجة لإيجاد تنفيذات أكثر انسيابية وكفاءة، خاصة مع التوازي الهائل للأجهزة المتاح الآن بسهولة وبتكلفة منخفضة في شكل معالجات الرسوميات (GPUs) والـ FPGAs.

تأتي صعوبة أخرى في التطبيق العملي للتفاضل الآلي في التعلم الآلي (ML) من طبيعة العديد من أطر العمل الشائعة حالياً للتعلم الآلي، بما في ذلك Caffe [Jia et al., 2014]، وTensorFlow [Abadi et al., 2016]، وKeras [Chollet, 2016]. تم تصميم هذه الأطر حول مفهوم "الرسم البياني" (أو "الشبكة") من العُقد المترابطة، كل منها يمثل عملية رياضية - نوع من رسم تدفق البيانات. تقوم البرامج التطبيقية ببناء هذه الرسوم البيانية بشكل صريح، مُنشئةً العُقد وموصلةً إياها بعقد أخرى. بعد البناء، يجب معالجة الرسوم البيانية إلى تمثيل أكثر كفاءة للتدريب والتقييم. هذه الرسوم البيانية هي في الأساس تعبيرات رياضية مع مشاركة، وبالتالي فهي رسوم بيانية موجهة لا دورية (DAGs). يحمل هذا النموذج من بناء الرسم البياني والترجمة والتنفيذ تشابهاً ملحوظاً مع ما يفعله المبرمجون والمترجمون طوال الوقت:

• يتم كتابة البرامج بواسطة إنسان.
• يقوم الواجهة الأمامية للمترجم أو المفسر بتحليل البرنامج إلى تمثيل DAG.
• تقوم الواجهة الخلفية للمترجم بتحويل DAGs إلى شكل فعّال للتنفيذ.
• يقوم إنسان بتشغيل نتيجة الترجمة.

عند استخدام إطار عمل تعلم آلي نموذجي، يختبر المبرمجون تسلسل الخطوات هذا على مستويين: العمل مع الكود الخاص بهم ومع الرسوم البيانية التي يولدها كودهم. كلا المستويين لهما مفاهيم العمليات والمتغيرات وتدفق المعلومات والقيم والأنواع والمعاملات. كلاهما لهما نماذج تنفيذ يجب فهمها.

ستكون أساساً أبسط بكثير وأنظف للتعلم الآلي هو وجود لغة البرمجة فقط، مع حذف الرسوم البيانية/الشبكات تماماً. نظراً لأن التعلم الآلي يتعلق بالدوال (الرياضية)، فسيرغب المرء في اختيار لغة برمجة تدعم الدوال بشكل جيد، أي لغة وظيفية، أو على الأقل لغة ذات ميزات وظيفية قوية. يمكن للمرء تسمية هذا البديل "البرمجة الوظيفية القابلة للتفاضل". في هذا النموذج، يحدد المبرمجون مباشرةً الدوال ذات الاهتمام، باستخدام الأدوات القياسية للبرمجة الوظيفية، مع إضافة عامل تفاضل (دالة ذات ترتيب أعلى منطّقة، رغم أنها جزئية لأن ليس كل الدوال القابلة للحساب قابلة للتفاضل). بافتراض لغة وظيفية نقية أو مجموعة فرعية من لغة (مع دلالة رياضية بسيطة ودقيقة)، فإن معنى التفاضل هو بالضبط كما هو معرّف في الحساب التفاضلي التقليدي.

كيف يمكننا تحقيق هذه الرؤية للبرمجة الوظيفية القابلة للتفاضل؟ إحدى الطرق هي إنشاء لغات جديدة، ولكن القيام بذلك يتطلب جهداً هائلاً للتعريف والتنفيذ بكفاءة، وربما جهداً أكبر للترويج. بدلاً من ذلك، قد نختار لغة وظيفية نقية مناسبة مثل Haskell ثم نضيف التفاضل. تجسد هذه الورقة الخيار الأخير، حيث تعزز مترجم Haskell الشهير GHC بمكوّن إضافي يحول كود Haskell القياسي إلى شكل فئوي ليتم تمثيله في أي من مجموعة متنوعة من الفئات، بما في ذلك الدوال القابلة للتفاضل [Elliott, 2017].

تقدم هذه الورقة المساهمات المحددة التالية:

• بدءاً من فئة بسيطة من الدوال المعززة بالمشتقات، نحدد التفاضل الآلي بشكل بسيط ودقيق من خلال طلب أن يكون هذا التعزيز (بالنسبة للدوال العادية) متماثل الشكل فيما يتعلق بمجموعة من التجريدات الفئوية القياسية والعمليات الرياضية الأولية.

• حساب تنفيذ للتفاضل الآلي صحيح بالبناء من المواصفات المتماثلة الشكل.

• تعميم التفاضل الآلي باستبدال الخرائط الخطية (قيم المشتقات العامة) بفئة ديكارتية تعسفية [Elliott, 2017]، نحدد عدة أشكال متنوعة من التفاضل الآلي، جميعها ناتجة عن تمثيلات مختلفة للخرائط الخطية: الدوال (التي تُرضي الخطية)، و"المصفوفات المعممة" (المُركبات التمثيلية القابلة للتكوين)، والتحويلات القائمة على الاستمرار لأي تمثيل خريطة خطية، والنسخ المزدوجة من أي تمثيل خريطة خطية. ينتج عن الصيغتين الأخيرتين تنفيذات صحيحة بالبناء للتفاضل الآلي ذي النمط العكسي أبسط بكثير من المعروفة سابقاً وتتكون من مكونات مفيدة بشكل عام. إن اختيار الدوال الخطية المزدوجة لحسابات التدرج مقنع بشكل خاص في البساطة. كما يبدو أنه فعّال جداً - لا يتطلب تمثيلات أو حسابات على مستوى المصفوفة - ومناسب للتحسين القائم على التدرج، على سبيل المثال، للتعلم الآلي. على النقيض من خوارزميات التفاضل الآلي ذي النمط العكسي التقليدية، جميع الخوارزميات في هذه الورقة خالية من التغيير وبالتالي متوازية بشكل طبيعي. بناء مماثل ينتج عنه التفاضل الآلي ذو النمط الأمامي.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** automatic differentiation (AD), reverse-mode AD (RAD), forward-mode AD (FAD), backpropagation, gradient descent, differentiable functional programming, Haskell, GHC compiler, category theory, linear maps
- **Equations:** None in this section
- **Citations:** 6 references cited [Lecun et al. 2015, Goodfellow et al. 2016, Jia et al. 2014, Abadi et al. 2016, Chollet 2016, Elliott 2017]
- **Special handling:** Technical concepts like "tapes", "traces", "Wengert lists", DAGs, GPUs, FPGAs kept in English or transliterated where appropriate

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation

Key paragraph (first paragraph):

"الحساب الدقيق والفعّال والموثوق للمشتقات أصبح ذا أهمية متزايدة..."

Back-translates to: "Accurate, efficient, and reliable computation of derivatives has become increasingly important over recent years, largely due to the successful use of backpropagation in machine learning, including multi-layer neural networks, also known as 'deep learning'. Backpropagation is a specialization and independent invention of the reverse mode of automatic differentiation..."

This matches the original semantically and preserves all key technical concepts.
