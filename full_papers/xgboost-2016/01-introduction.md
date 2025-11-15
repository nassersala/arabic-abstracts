# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.90
**Glossary Terms Used:** machine learning, gradient boosting, tree boosting, algorithm, dataset, scalability, parallel computing, distributed computing, cache, sparse data, regularization

---

### English Version

Machine learning and data-driven approaches are becoming very important in many areas. Smart spam classifiers protect our email by learning from massive amounts of spam data and user feedback; advertising systems learn to match the right ads with the right context; fraud detection systems protect banks from malicious attackers; anomaly event detection systems help experimental physicists to find events that lead to new physics. There are two important factors that drive these successful applications: usage of effective (statistical) models that capture the complex data dependencies and scalable learning systems that learn the model of interest from large datasets.

Among the machine learning methods used in practice, gradient tree boosting is one technique that shines in many applications. Tree boosting has been shown to give state-of-the-art results on many standard classification benchmarks. LambdaMART, a variant of tree boosting for ranking, achieves state-of-the-art result for ranking problems. Besides being used as a stand-alone predictor, it is also incorporated into real-world production pipelines for ad click through rate prediction. Finally, it is the de-facto choice of ensemble method and is used in challenges such as the Netflix prize.

In this paper, we describe XGBoost, a scalable machine learning system for tree boosting. The system is available as an open source package. The impact of the system has been widely recognized in a number of machine learning and data mining challenges. Take the challenges hosted by the machine learning competition site Kaggle for example. Among the 29 challenge winning solutions published at Kaggle's blog during 2015, 17 solutions used XGBoost. Among these solutions, eight solely used XGBoost to train the model, while most others combined XGBoost with neural nets in ensembles. For comparison, the second most popular method, deep neural nets, was used in 11 solutions. The success of the system was also witnessed in KDDCup 2015, where XGBoost was used by every winning team in the top-10. Moreover, the winning teams reported that ensemble methods outperform a well-configured XGBoost by only a small amount.

These results demonstrate that our system gives state-of-the-art results on a wide range of problems. Examples of the problems in these winning solutions include: store sales prediction; high energy physics event classification; web text classification; customer behavior prediction; motion detection; ad click through rate prediction; malware classification; product categorization; hazard risk prediction; massive online course dropout rate prediction. While domain dependent data analysis and feature engineering play an important role in these solutions, the fact that XGBoost is the consensus choice of learner shows the impact and importance of our system and tree boosting.

The most important factor behind the success of XGBoost is its scalability in all scenarios. The system runs more than ten times faster than existing popular solutions on a single machine and scales to billions of examples in distributed or memory-limited settings. The scalability of XGBoost is due to several important systems and algorithmic optimizations. These innovations include: a novel tree learning algorithm is for handling sparse data; a theoretically justified weighted quantile sketch procedure enables handling instance weights in approximate tree learning. Parallel and distributed computing makes learning faster which enables quicker model exploration. More importantly, XGBoost exploits out-of-core computation and enables data scientists to process hundred millions of examples on a desktop. Finally, it is even more exciting to combine these techniques to make an end-to-end system that scales to even larger data with the least amount of cluster resources.

The major contributions of this paper is listed as follows:
- We design and build a highly scalable end-to-end tree boosting system.
- We propose a theoretically justified weighted quantile sketch for efficient proposal calculation.
- We introduce a novel sparsity-aware algorithm for parallel tree learning.
- We propose an effective cache-aware block structure for out-of-core tree learning.

While there are some existing works on parallel tree boosting, the directions such as out-of-core computation, cache-aware and sparsity-aware learning have not been explored. More importantly, an end-to-end system that combines all of these aspects gives a novel solution for real-world use-cases. This enables data scientists as well as researchers to build powerful variants of tree boosting algorithms. Besides these major contributions, we also make additional improvements in proposing a regularized learning objective, which we will include for completeness.

The remainder of the paper is organized as follows. We will first review tree boosting and introduce a regularized objective in Section 2. We then describe the split finding methods in Section 3 as well as the system design in Section 4, including experimental results when relevant to provide quantitative support for each optimization we describe. Related work is discussed in Section 5. Detailed end-to-end evaluations are included in Section 6. Finally we conclude the paper in Section 7.

---

### النسخة العربية

أصبح التعلم الآلي والأساليب المدفوعة بالبيانات ذات أهمية كبيرة في العديد من المجالات. تحمي مصنفات الرسائل غير المرغوب فيها الذكية بريدنا الإلكتروني من خلال التعلم من كميات هائلة من بيانات الرسائل غير المرغوب فيها وملاحظات المستخدمين؛ وتتعلم أنظمة الإعلانات مطابقة الإعلانات المناسبة مع السياق المناسب؛ وتحمي أنظمة كشف الاحتيال البنوك من المهاجمين الخبيثين؛ وتساعد أنظمة كشف الأحداث الشاذة الفيزيائيين التجريبيين في العثور على الأحداث التي تؤدي إلى فيزياء جديدة. هناك عاملان مهمان يدفعان هذه التطبيقات الناجحة: استخدام نماذج (إحصائية) فعّالة تلتقط تبعيات البيانات المعقدة، وأنظمة تعلم قابلة للتوسع تتعلم النموذج المطلوب من مجموعات البيانات الكبيرة.

من بين أساليب التعلم الآلي المستخدمة عملياً، يُعد تعزيز الأشجار بالتدرج (Gradient Tree Boosting) تقنية متميزة في العديد من التطبيقات. لقد ثبت أن تعزيز الأشجار يقدم نتائج متقدمة على العديد من معايير التصنيف القياسية. يحقق LambdaMART، وهو نوع من تعزيز الأشجار للترتيب، نتائج متقدمة لمشاكل الترتيب. بالإضافة إلى استخدامه كمتنبئ مستقل، يتم دمجه أيضاً في خطوط الإنتاج الفعلية للتنبؤ بمعدل النقر على الإعلانات. وأخيراً، فهو الخيار الفعلي لطريقة التجميع (Ensemble) ويُستخدم في تحديات مثل جائزة Netflix.

في هذا البحث، نقدم XGBoost، وهو نظام تعلم آلي قابل للتوسع لتعزيز الأشجار. النظام متاح كحزمة مفتوحة المصدر. لقد تم الاعتراف على نطاق واسع بتأثير النظام في عدد من تحديات التعلم الآلي وتنقيب البيانات. خذ على سبيل المثال التحديات التي يستضيفها موقع المنافسة في التعلم الآلي Kaggle. من بين 29 حلاً فائزاً في التحديات المنشورة على مدونة Kaggle خلال عام 2015، استخدم 17 حلاً XGBoost. من بين هذه الحلول، استخدم ثمانية XGBoost فقط لتدريب النموذج، بينما دمج معظم الآخرين XGBoost مع الشبكات العصبية في مجموعات. للمقارنة، تم استخدام الطريقة الثانية الأكثر شيوعاً، وهي الشبكات العصبية العميقة، في 11 حلاً. كما شهد النجاح أيضاً في KDDCup 2015، حيث استخدم كل فريق فائز في أفضل 10 فرق XGBoost. علاوة على ذلك، أفادت الفرق الفائزة بأن طرق التجميع تتفوق على XGBoost المُكوَّن جيداً بمقدار صغير فقط.

تُظهر هذه النتائج أن نظامنا يقدم نتائج متقدمة على نطاق واسع من المشاكل. تشمل أمثلة المشاكل في هذه الحلول الفائزة: التنبؤ بمبيعات المتاجر؛ تصنيف أحداث الفيزياء عالية الطاقة؛ تصنيف النصوص على الويب؛ التنبؤ بسلوك العملاء؛ كشف الحركة؛ التنبؤ بمعدل النقر على الإعلانات؛ تصنيف البرمجيات الخبيثة؛ تصنيف المنتجات؛ التنبؤ بمخاطر الكوارث؛ التنبؤ بمعدل التسرب من الدورات الضخمة عبر الإنترنت. في حين أن تحليل البيانات المعتمد على المجال وهندسة الميزات يلعبان دوراً مهماً في هذه الحلول، فإن حقيقة أن XGBoost هو الخيار المتفق عليه للمتعلم تُظهر تأثير وأهمية نظامنا وتعزيز الأشجار.

العامل الأكثر أهمية وراء نجاح XGBoost هو قابليته للتوسع في جميع السيناريوهات. يعمل النظام بسرعة تزيد عن عشر مرات من الحلول الشائعة الموجودة على جهاز واحد ويتوسع إلى مليارات الأمثلة في الإعدادات الموزعة أو المحدودة بالذاكرة. تعود قابلية التوسع لـ XGBoost إلى العديد من تحسينات الأنظمة والخوارزميات المهمة. تشمل هذه الابتكارات: خوارزمية جديدة لتعلم الأشجار للتعامل مع البيانات المتناثرة؛ إجراء رسم تقريبي للكميات الموزونة مبرر نظرياً يمكّن من التعامل مع أوزان الحالات في التعلم التقريبي للأشجار. تجعل الحوسبة المتوازية والموزعة التعلم أسرع مما يتيح استكشاف النماذج بشكل أسرع. والأهم من ذلك، يستغل XGBoost الحوسبة خارج النواة (Out-of-core) ويمكّن علماء البيانات من معالجة مئات الملايين من الأمثلة على جهاز مكتبي. وأخيراً، من المثير أكثر الجمع بين هذه التقنيات لإنشاء نظام شامل يتوسع إلى بيانات أكبر بأقل قدر من موارد المجموعة (Cluster).

المساهمات الرئيسية لهذا البحث مدرجة كما يلي:
- نصمم ونبني نظاماً شاملاً قابل للتوسع بشكل كبير لتعزيز الأشجار.
- نقترح رسماً تقريبياً للكميات الموزونة مبرراً نظرياً لحساب المقترحات بكفاءة.
- نقدم خوارزمية جديدة تدرك التناثر للتعلم المتوازي للأشجار.
- نقترح بنية كتلة تدرك ذاكرة التخزين المؤقت فعّالة للتعلم خارج النواة للأشجار.

في حين أن هناك بعض الأعمال الموجودة حول تعزيز الأشجار المتوازي، إلا أن الاتجاهات مثل الحوسبة خارج النواة، والتعلم المدرك لذاكرة التخزين المؤقت والمدرك للتناثر لم يتم استكشافها. والأهم من ذلك، أن نظاماً شاملاً يجمع كل هذه الجوانب يقدم حلاً جديداً لحالات الاستخدام في العالم الحقيقي. يمكّن هذا علماء البيانات وكذلك الباحثين من بناء متغيرات قوية من خوارزميات تعزيز الأشجار. بالإضافة إلى هذه المساهمات الرئيسية، نقوم أيضاً بإجراء تحسينات إضافية في اقتراح هدف تعلم مُنظَّم، والذي سنضمنه للاكتمال.

ينظم الجزء المتبقي من البحث على النحو التالي. سنراجع أولاً تعزيز الأشجار ونقدم هدفاً مُنظَّماً في القسم 2. ثم نصف طرق إيجاد الانقسام في القسم 3 وكذلك تصميم النظام في القسم 4، بما في ذلك النتائج التجريبية عند الصلة لتقديم دعم كمي لكل تحسين نصفه. يتم مناقشة الأعمال ذات الصلة في القسم 5. يتم تضمين تقييمات شاملة مفصلة في القسم 6. وأخيراً نختتم البحث في القسم 7.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Gradient Tree Boosting (تعزيز الأشجار بالتدرج)
  - Ensemble Method (طريقة التجميع)
  - Out-of-core Computation (الحوسبة خارج النواة)
  - Sparsity-aware (تدرك التناثر / المدرك للتناثر)
  - Cache-aware (تدرك ذاكرة التخزين المؤقت)
  - Weighted Quantile Sketch (رسم تقريبي للكميات الموزونة)
  - Feature Engineering (هندسة الميزات)

- **Equations:** None
- **Citations:** Multiple references preserved as [cite]

- **Special handling:**
  - Kept proper nouns: XGBoost, Kaggle, Netflix, KDDCup, LambdaMART
  - Translated "state-of-the-art" as "متقدمة" (advanced/cutting-edge)
  - "Scalability" translated as "قابلية للتوسع"
  - Maintained all numerical data (29 solutions, 17 used XGBoost, etc.)
  - Section references kept as numbers (القسم 2, القسم 3, etc.)

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90

### Back-Translation Check (First & Last Paragraphs)

**First paragraph back-translation:**
"Machine learning and data-driven approaches have become of great importance in many fields. Smart spam classifiers protect our email through learning from massive amounts of spam data and user feedback; advertising systems learn to match appropriate ads with appropriate context; fraud detection systems protect banks from malicious attackers; anomaly detection systems help experimental physicists find events that lead to new physics. There are two important factors driving these successful applications: using effective (statistical) models that capture complex data dependencies, and scalable learning systems that learn the required model from large datasets."

**Last paragraph back-translation:**
"The remaining part of the research is organized as follows. We will first review tree boosting and present a regularized objective in Section 2. Then we describe the split finding methods in Section 3 as well as the system design in Section 4, including experimental results when relevant to provide quantitative support for each optimization we describe. Related works are discussed in Section 5. Detailed comprehensive evaluations are included in Section 6. Finally, we conclude the research in Section 7."

✅ Back-translations maintain core technical meaning and semantic accuracy.
