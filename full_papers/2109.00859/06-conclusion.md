# Section 6: Conclusion
## القسم 6: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** مشفر-فك تشفير, التدريب المسبق, المعرفات, التوليد المزدوج ثنائي الوضع, التعلم متعدد المهام, فهم الشفرة, توليد الشفرة, ذكاء البرمجيات, التحيز, التكلفة الحسابية

---

### English Version

**6 Conclusion**

We have presented CodeT5, a pre-trained encoder-decoder model that incorporates the token type information from code. We propose a novel identifier-aware pre-training objective to better leverage the identifiers and propose a bimodal dual generation task to learn a better NL-PL alignment using code and its comments. Our unified model can support both code understanding and generation tasks and allow for multi-task learning. Experiments show that CodeT5 significantly outperforms all prior work in most CodeXGLUE tasks. Further analysis also reveals its better code comprehension capability across various programming languages.

**Broader Impact and Ethical Consideration**

Our work generally belongs to NLP applications for software intelligence. With the goal of improving the development productivity of software with machine learning methods, software intelligence research has attracted increasing attention in both academia and industries over the last decade. Software code intelligence techniques can help developers to reduce tedious repetitive workloads, enhance the programming quality and improve the overall software development productivity. This would considerably decrease their working time and also could potentially reduce the computation and operational cost, as a bug might degrade the system performance or even crash the entire system. Our work addresses the fundamental challenge of software code pre-training, our study covers a wide range of code intelligence applications in the software development lifecycle, and the proposed CodeT5 method achieves the state-of-the-art performance on many of the benchmark tasks, showing its great potential benefit towards this goal.

We further discuss the ethical consideration of training CodeT5 and the potential risks when applying it into real-world downstream applications:

**Dataset bias.** The training datasets in our study are source code including user-written comments from open source Github repositories and publicly available, which do not tie to any specific application. However, it is possible that these datasets would encode some stereotypes like race and gender from the text comments or even from the source code such as variables, function and class names. As such, social biases would be intrinsically embedded into the models trained on them. As suggested by Chen et al. (2021), interventions such as filtration or modulation of generated outputs may help to mitigate these biases in code corpus.

**Computational cost.** Our model pre-training requires non-trivial computational resources though we have tried our best to carefully design our experiments and improve experiments to save unnecessary computation costs. In fact, compared to the recent large-scale language model Codex (Chen et al., 2021), our CodeT5-base has a much smaller model size of 220M than theirs of 12B (~55×). In addition, we experiment on Google Cloud Platform which purchases carbon credits to reduce its carbon footprint, e.g., training CodeT5-base produced around 49.25 kg CO₂ which was totally offset by the provider. Furthermore, we release our pre-trained models publicly to avoid repeated training for the code intelligence research community.

**Automation bias.** As CodeT5 can be deployed to provide coding assistance such as code generation for aiding developers, automation bias of machine learning systems should be carefully considered, especially for developers who tend to over-rely on the model-generated outputs. Sometimes these systems might produce functions that superficially appear correct but do not actually align with the developer's intents. If developers unintentionally adopt these incorrect code suggestions, it might cause them much longer time on debugging and even lead to some significant safety issues. We suggest practitioners using CodeT5 should always bear in mind that its generation outputs should be only taken as references which require domain experts for further correctness and security checking.

**Security implications.** We train CodeT5 on existing code corpus including CodeSearchNet (Husain et al., 2019) and a small fraction of Google BigQuery, both of which are originally collected from public Github repositories. Pre-trained models might encode some sensitive information (e.g., personal addresses or identification numbers) from the training data. Though we have conducted multi-rounds of data cleaning to mitigate this before training our models, it is still possible that some sensitive information cannot be completely removed. Besides, due to the non-deterministic nature of generation models like CodeT5, it might produce some vulnerable code to harmfully affect the software and even be able to benefit more advanced malware development when deliberately misused.

---

### النسخة العربية

**6 الخلاصة**

قدمنا CodeT5، وهو نموذج مشفر-فك تشفير مُدرب مسبقاً يدمج معلومات نوع الرمز من الشفرة. نقترح هدفاً جديداً للتدريب المسبق مدركاً للمعرفات للاستفادة بشكل أفضل من المعرفات ونقترح مهمة توليد مزدوجة ثنائية الوضع لتعلم محاذاة أفضل بين اللغة الطبيعية ولغة البرمجة باستخدام الشفرة وتعليقاتها. يمكن لنموذجنا الموحد دعم كل من مهام فهم الشفرة وتوليدها ويسمح بالتعلم متعدد المهام. تُظهر التجارب أن CodeT5 يتفوق بشكل كبير على جميع الأعمال السابقة في معظم مهام CodeXGLUE. يكشف التحليل الإضافي أيضاً عن قدرته الأفضل على فهم الشفرة عبر لغات البرمجة المختلفة.

**الأثر الأوسع والاعتبارات الأخلاقية**

ينتمي عملنا بشكل عام إلى تطبيقات معالجة اللغة الطبيعية لذكاء البرمجيات. مع هدف تحسين إنتاجية تطوير البرمجيات بأساليب التعلم الآلي، اجتذبت أبحاث ذكاء البرمجيات اهتماماً متزايداً في كل من الأوساط الأكاديمية والصناعات على مدى العقد الماضي. يمكن لتقنيات ذكاء شفرة البرمجيات مساعدة المطورين على تقليل أعباء العمل المتكررة المملة، وتعزيز جودة البرمجة وتحسين إنتاجية تطوير البرمجيات الإجمالية. سيؤدي هذا إلى تقليل وقت عملهم بشكل كبير وقد يقلل أيضاً من التكلفة الحسابية والتشغيلية، حيث قد يؤدي الخطأ إلى تدهور أداء النظام أو حتى تعطل النظام بالكامل. يعالج عملنا التحدي الأساسي للتدريب المسبق لشفرة البرمجيات، تغطي دراستنا مجموعة واسعة من تطبيقات ذكاء الشفرة في دورة حياة تطوير البرمجيات، وتحقق طريقة CodeT5 المقترحة أداءً متقدماً في العديد من مهام المعايير، مما يُظهر فائدتها المحتملة الكبيرة نحو هذا الهدف.

نناقش أيضاً الاعتبارات الأخلاقية لتدريب CodeT5 والمخاطر المحتملة عند تطبيقه في التطبيقات اللاحقة في العالم الحقيقي:

**تحيز مجموعة البيانات.** مجموعات بيانات التدريب في دراستنا هي شفرة مصدرية بما في ذلك تعليقات مكتوبة من قبل المستخدمين من مستودعات Github مفتوحة المصدر ومتاحة للجمهور، والتي لا ترتبط بأي تطبيق محدد. ومع ذلك، من الممكن أن تُرمّز هذه مجموعات البيانات بعض الصور النمطية مثل العرق والجنس من تعليقات النص أو حتى من الشفرة المصدرية مثل أسماء المتغيرات والدوال والفئات. على هذا النحو، ستُدمج التحيزات الاجتماعية بشكل جوهري في النماذج المُدربة عليها. كما اقترح Chen et al. (2021)، قد تساعد التدخلات مثل الترشيح أو تعديل المخرجات المولدة في تخفيف هذه التحيزات في مدونة الشفرة.

**التكلفة الحسابية.** يتطلب التدريب المسبق لنموذجنا موارد حسابية غير تافهة على الرغم من أننا حاولنا جاهدين تصميم تجاربنا بعناية وتحسين التجارب لتوفير تكاليف الحساب غير الضرورية. في الواقع، بالمقارنة مع نموذج اللغة واسع النطاق الحديث Codex (Chen et al., 2021)، يحتوي CodeT5-base الخاص بنا على حجم نموذج أصغر بكثير وهو 220M من حجمهم البالغ 12B (~55 مرة). بالإضافة إلى ذلك، نجري التجارب على منصة Google Cloud التي تشتري أرصدة الكربون لتقليل بصمتها الكربونية، على سبيل المثال، أنتج تدريب CodeT5-base حوالي 49.25 كجم CO₂ والذي تم تعويضه بالكامل من قبل المزود. علاوة على ذلك، نصدر نماذجنا المُدربة مسبقاً بشكل عام لتجنب التدريب المتكرر لمجتمع أبحاث ذكاء الشفرة.

**تحيز الأتمتة.** نظراً لأنه يمكن نشر CodeT5 لتوفير مساعدة في البرمجة مثل توليد الشفرة لمساعدة المطورين، يجب النظر بعناية في تحيز الأتمتة لأنظمة التعلم الآلي، خاصة للمطورين الذين يميلون إلى الاعتماد المفرط على المخرجات المولدة من النموذج. في بعض الأحيان قد تنتج هذه الأنظمة دوال تبدو صحيحة ظاهرياً ولكنها لا تتماشى فعلياً مع نوايا المطور. إذا تبنى المطورون عن غير قصد اقتراحات الشفرة غير الصحيحة هذه، فقد يتسبب ذلك في قضائهم وقتاً أطول بكثير في تصحيح الأخطاء وحتى يؤدي إلى بعض مشاكل السلامة الكبيرة. نقترح أن الممارسين الذين يستخدمون CodeT5 يجب أن يضعوا دائماً في اعتبارهم أن مخرجات التوليد الخاصة به يجب أن تُؤخذ فقط كمراجع تتطلب خبراء في المجال لمزيد من التحقق من الصحة والأمان.

**الآثار الأمنية.** ندرب CodeT5 على مدونة شفرة موجودة بما في ذلك CodeSearchNet (Husain et al., 2019) وجزء صغير من Google BigQuery، كلاهما تم جمعهما في الأصل من مستودعات Github العامة. قد ترمّز النماذج المُدربة مسبقاً بعض المعلومات الحساسة (على سبيل المثال، العناوين الشخصية أو أرقام الهوية) من بيانات التدريب. على الرغم من أننا أجرينا جولات متعددة من تنظيف البيانات للتخفيف من هذا قبل تدريب نماذجنا، لا يزال من الممكن أن بعض المعلومات الحساسة لا يمكن إزالتها بالكامل. بالإضافة إلى ذلك، نظراً للطبيعة غير الحتمية لنماذج التوليد مثل CodeT5، قد ينتج بعض الشفرات الضعيفة للتأثير بشكل ضار على البرمجيات وحتى القدرة على الاستفادة من تطوير برامج ضارة أكثر تقدماً عند إساءة استخدامها عمداً.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** None
- **Key terms introduced:** ذكاء البرمجيات (software intelligence), تحيز مجموعة البيانات (dataset bias), التحيزات الاجتماعية (social biases), التكلفة الحسابية (computational cost), البصمة الكربونية (carbon footprint), تحيز الأتمتة (automation bias), الآثار الأمنية (security implications), معلومات حساسة (sensitive information), برامج ضارة (malware)
- **Equations:** 0
- **Citations:** 3 references cited (Chen 2021, Husain 2019)
- **Special handling:**
  - Preserved model names (CodeT5, Codex) in English
  - Preserved dataset names (CodeXGLUE, CodeSearchNet, Google BigQuery) in English
  - Maintained ethical considerations section structure
  - Preserved CO₂ notation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
