# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** domain-specific, accelerator, GPGPU, architecture, performance, power, pipeline, floating point, algorithm, optimization, memory hierarchy, bandwidth

---

### English Version

Domain specific computing platforms have gained immense popularity in the last decade. For domain specific computing, custom architectures are developed for efficient realization of several algorithms/computations pertaining to the domain of interest. Several architectural parameter such as size of the memory, bandwidth in the memory subsystem, and compute resource choices are chosen that are specific to the domain of interest. For domain specific computing, accelerators are preferred as an ideal underlying platform due to their better power performance over general purpose computers [1][2][3]. While accelerators like General Purpose Graphic Processing Units (GPGPUs) dissipate more power than desired, there are several domain specific accelerators designed to overcome this shortcoming of GPGPUs [2][4].

Domain customized platforms and/or accelerators are gaining popularity due to their area and power performance [5][6][7][8]. Performance in these accelerators is achieved by setting several architectural parameters that are well suited for computations pertaining to the domain. Parameters such as size of the memory at different levels and bandwidth of the memory that is nearest to the compute resources is well experimented in the literature [2]. Through pipelining of the processor and memory subsystem it is ensured that the processor is able to operate at the highest possible speed with lowest power penalty for the technology node [9][10]. Several design space exploration techniques are developed to arrive at an optimum architectural parameters for optimal performance in the domain. These techniques are computer architecture simulator based techniques and allow tweaking of parameters such as memory size and memory bandwidth.

Basic Linear Algebra Subprograms (BLAS) and Linear Algebra Package (LAPACK) and/or their platform dependent variants are the basic building block for several high level software packages like Intel's DAAL, Spark's MLlib, Berkeley's CAFFE, UTK's PLASMA, and MAGMA packages [11][12]. Performance of BLAS and LAPACK eventually decides performance of these packages. Hence, it is important to have a high performance realization of these packages. Efficient realization of BLAS and LAPACK on different contemporary platforms has been ever researched topic [1][2][13]. All these efforts of efficient realizations are through software optimizations and efficient exploitation of memory hierarchy [14][15]. Major reason for centralization of efforts toward software optimizations and efficient exploitation of memory hierarchy is mainly due to several architectural parameters that are not in the control of programmer [16]. For example, the depth of the pipeline (pipeline stages) in the underlying platform [17]. In this paper, we present a theoretical framework that assists in establishing a relation between pipeline depth of different floating point operations with size and type of the workload. Major contributions in this paper are as follows:

• We present a comprehensive theoretical framework that allows us to predict processor performance based on pipeline depths of different floating point operations like multiplier, adder, square root, and divider for BLAS and LAPACK

• Characterization of BLAS and LAPACK is presented where we try to determine several parameters to be fitted in our theoretical framework to arrive at optimum number of pipeline stages for floating point operations

• Extensive simulations are carried out to arrive at an optimum pipeline depth of multiplier, adder, square root, and divider for BLAS and LAPACK in a Processing Element (PE). It is shown that our theoretical curves corroborate to our simulations. Finally with synthesis results it is shown that our PE outperforms recently presented custom linear algebra accelerator

We choose a scalar processor for our initial theoretical framework and then extend framework for superscalar processor. The paper is organized as follows: In section 2, we discuss some of the works in the literature focusing on optimum pipeline depth of the processor. In section 3, we focus on theoretical framework and derive expression for optimum pipeline depth for several operations encountered in BLAS and LAPACK. Characterization of BLAS and LAPACK is presented in section 4. We present a Processing Element (PE) design in section 4 for experimental setup that is to validate our theoretical framework and discuss results in section 5. In section 6, we conclude our work.

---

### النسخة العربية

اكتسبت منصات الحوسبة الخاصة بالمجال شعبية هائلة في العقد الماضي. بالنسبة للحوسبة الخاصة بالمجال، يتم تطوير معماريات مخصصة للتنفيذ الفعال للعديد من الخوارزميات/الحسابات المتعلقة بمجال الاهتمام. يتم اختيار العديد من المعاملات المعمارية مثل حجم الذاكرة وعرض النطاق الترددي في النظام الفرعي للذاكرة وخيارات موارد الحوسبة بما يتناسب مع مجال الاهتمام. بالنسبة للحوسبة الخاصة بالمجال، تُفضل المسرّعات كمنصة أساسية مثالية نظراً لأدائها الأفضل في استهلاك الطاقة مقارنة بالحواسيب ذات الأغراض العامة [1][2][3]. بينما تستهلك المسرّعات مثل وحدات معالجة الرسومات ذات الأغراض العامة (GPGPUs) طاقة أكثر من المرغوب، هناك العديد من المسرّعات الخاصة بالمجال المصممة للتغلب على هذا القصور في GPGPUs [2][4].

تكتسب المنصات المخصصة للمجال و/أو المسرّعات شعبية بسبب أداء المساحة والطاقة [5][6][7][8]. يتم تحقيق الأداء في هذه المسرّعات من خلال تعيين العديد من المعاملات المعمارية المناسبة تماماً للحسابات المتعلقة بالمجال. تم تجربة معاملات مثل حجم الذاكرة على مستويات مختلفة وعرض النطاق الترددي للذاكرة الأقرب إلى موارد الحوسبة بشكل جيد في الأدبيات [2]. من خلال خطوط الأنابيب للمعالج والنظام الفرعي للذاكرة، يتم ضمان قدرة المعالج على العمل بأعلى سرعة ممكنة مع أقل عقوبة للطاقة لعقدة التكنولوجيا [9][10]. تم تطوير العديد من تقنيات استكشاف فضاء التصميم للوصول إلى المعاملات المعمارية المثلى للأداء الأمثل في المجال. هذه التقنيات هي تقنيات قائمة على محاكي معمارية الحاسوب وتسمح بضبط معاملات مثل حجم الذاكرة وعرض النطاق الترددي للذاكرة.

تعد البرامج الفرعية الأساسية للجبر الخطي (BLAS) وحزمة الجبر الخطي (LAPACK) و/أو متغيراتها التابعة للمنصة الوحدة البنائية الأساسية للعديد من حزم البرمجيات عالية المستوى مثل DAAL من Intel وMLlib من Spark وCAFFE من Berkeley وحزم PLASMA وMAGMA من UTK [11][12]. يحدد أداء BLAS و LAPACK في النهاية أداء هذه الحزم. لذلك، من المهم أن يكون لدينا تطبيق عالي الأداء لهذه الحزم. كان التطبيق الفعال لـ BLAS و LAPACK على منصات معاصرة مختلفة موضوعاً بحثياً دائماً [1][2][13]. جميع هذه الجهود للتطبيقات الفعالة تتم من خلال تحسينات البرمجيات والاستغلال الفعال للتسلسل الهرمي للذاكرة [14][15]. السبب الرئيسي لتركيز الجهود نحو تحسينات البرمجيات والاستغلال الفعال للتسلسل الهرمي للذاكرة هو بشكل أساسي بسبب العديد من المعاملات المعمارية التي ليست تحت سيطرة المبرمج [16]. على سبيل المثال، عمق خط الأنابيب (مراحل خط الأنابيب) في المنصة الأساسية [17]. في هذه الورقة، نقدم إطاراً نظرياً يساعد في إنشاء علاقة بين عمق خط الأنابيب لعمليات النقطة العائمة المختلفة مع حجم ونوع عبء العمل. المساهمات الرئيسية في هذه الورقة هي كما يلي:

• نقدم إطاراً نظرياً شاملاً يسمح لنا بالتنبؤ بأداء المعالج بناءً على أعماق خطوط الأنابيب لعمليات النقطة العائمة المختلفة مثل المضارب والجامع والجذر التربيعي والمقسم لـ BLAS و LAPACK

• يتم تقديم توصيف لـ BLAS و LAPACK حيث نحاول تحديد العديد من المعاملات التي سيتم ملاءمتها في إطارنا النظري للوصول إلى العدد الأمثل لمراحل خط الأنابيب لعمليات النقطة العائمة

• يتم إجراء محاكاة موسعة للوصول إلى عمق خط الأنابيب الأمثل للمضارب والجامع والجذر التربيعي والمقسم لـ BLAS و LAPACK في عنصر المعالجة (PE). يُظهر أن منحنياتنا النظرية تؤكد محاكاتنا. وأخيراً، مع نتائج التوليف، يُظهر أن PE الخاص بنا يتفوق على مسرّع الجبر الخطي المخصص المقدم مؤخراً

نختار معالجاً قياسياً لإطارنا النظري الأولي ثم نمد الإطار لمعالج فائق القياسية. يتم تنظيم الورقة كما يلي: في القسم 2، نناقش بعض الأعمال في الأدبيات التي تركز على عمق خط الأنابيب الأمثل للمعالج. في القسم 3، نركز على الإطار النظري ونشتق تعبيراً لعمق خط الأنابيب الأمثل لعدة عمليات تُواجه في BLAS و LAPACK. يتم تقديم توصيف لـ BLAS و LAPACK في القسم 4. نقدم تصميم عنصر المعالجة (PE) في القسم 4 للإعداد التجريبي الذي يهدف إلى التحقق من صحة إطارنا النظري ونناقش النتائج في القسم 5. في القسم 6، نختتم عملنا.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** domain-specific computing, accelerators, GPGPU, BLAS, LAPACK, pipeline depth, Processing Element (PE), memory hierarchy, superscalar processor
- **Equations:** None
- **Citations:** [1] through [17] referenced
- **Special handling:** Software package names kept in English (DAAL, MLlib, CAFFE, PLASMA, MAGMA); Technical acronyms maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
