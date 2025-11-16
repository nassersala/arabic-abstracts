# Section 1: Introduction
## القسم الأول: المقدمة

### English Version

Many machine learning algorithms are data hungry, and in reality, data are dispersed over different organizations under the protection of privacy restrictions. Due to these factors, federated learning (FL) [129, 207, 85] has become a hot research topic in machine learning. For example, data of different hospitals are isolated and become "data islands". Since each data island has limitations in size and approximating real distributions, a single hospital may not be able to train a high-quality model that has a good predictive accuracy for a specific task. Ideally, hospitals can benefit more if they can collaboratively train a machine learning model on the union of their data. However, the data cannot simply be shared among the hospitals due to various policies and regulations. Such phenomena on "data islands" are commonly seen in many areas such as finance, government, and supply chains. Policies such as General Data Protection Regulation (GDPR) [10] stipulate rules on data sharing among different organizations. Thus, it is challenging to develop a federated learning system which has a good predictive accuracy while obeying policies and regulations to protect privacy.

Many efforts have recently been devoted to implementing federated learning algorithms to support effective machine learning models. Specifically, researchers try to support more machine learning models with different privacy-preserving approaches, including deep neural networks (NNs) [119, 213, 24, 158, 129], gradient boosted decision trees (GBDTs) [217, 38, 104], logistics regression [141, 36] and support vector machines (SVMs) [169]. For instance, Nikolaenko et al. [141] and Chen et al. [36] propose approaches to conduct FL based on linear regression. Since GBDTs have become very successful in recent years [34, 200], the corresponding Federated Learning Systems (FLSs) have also been proposed by Zhao et al. [217], Cheng et al. [38], Li et al. [104]. Moreover, there are many FLSs supporting the training of NNs. Google proposes a scalable production system which enables tens of millions of devices to train a deep neural network [24].

As there are common methods and building blocks (e.g., privacy mechanisms such as differential privacy) for building FL algorithms, it makes sense to develop systems and infrastructures to ease the development of various FL algorithms. Systems and infrastructures allow algorithm developers to reuse the common building blocks, and avoid building algorithms every time from scratch. Similar to deep learning systems such as PyTorch [148, 149] and TensorFlow [7] that boost the development of deep learning algorithms, FLSs are equivalently important for the success of FL. However, building a successful FLS is challenging, which needs to consider multiple aspects such as effectiveness, efficiency, privacy, and autonomy.

In this paper, we take a survey on the existing FLSs from a system view. First, we show the definition of FLSs, and compare it with conventional federated systems. Second, we analyze the system components of FLSs, including the parties, the manager, and the computation-communication framework. Third, we categorize FLSs based on six different aspects: data distribution, machine learning model, privacy mechanism, communication architecture, scale of federation, and motivation of federation. These aspects can direct the design of an FLS as common building blocks and system abstractions. Fourth, based on these aspects, we systematically summarize the existing studies, which can be used to direct the design of FLSs. Last, to make FL more practical and powerful, we present future research directions to work on. We believe that systems and infrastructures are essential for the success of FL. More work has to be carried out to address the system research issues in effectiveness, efficiency, privacy, and autonomy.

### النسخة العربية

تتطلب العديد من خوارزميات تعلم الآلة كميات كبيرة من البيانات، وفي الواقع، تكون البيانات مبعثرة عبر منظمات مختلفة تحت حماية قيود الخصوصية. بسبب هذه العوامل، أصبح التعلم الاتحادي [129، 207، 85] موضوع بحث ساخن في تعلم الآلة. على سبيل المثال، تكون بيانات المستشفيات المختلفة معزولة وتصبح "جزر بيانات". نظرًا لأن كل جزيرة بيانات لها قيود من حيث الحجم وتقريب التوزيعات الحقيقية، فقد لا تتمكن مستشفى واحدة من تدريب نموذج عالي الجودة يتمتع بدقة تنبؤية جيدة لمهمة محددة. من الناحية المثالية، يمكن للمستشفيات الاستفادة أكثر إذا تمكنت من تدريب نموذج تعلم آلة بشكل تعاوني على اتحاد بياناتها. ومع ذلك، لا يمكن مشاركة البيانات ببساطة بين المستشفيات بسبب السياسات واللوائح المختلفة. تُشاهد هذه الظاهرة المتعلقة بـ "جزر البيانات" بشكل شائع في العديد من المجالات مثل التمويل والحكومة وسلاسل التوريد. تنص السياسات مثل اللائحة العامة لحماية البيانات (GDPR) [10] على قواعد مشاركة البيانات بين المنظمات المختلفة. وبالتالي، يشكل تطوير نظام تعلم اتحادي يتمتع بدقة تنبؤية جيدة مع الامتثال للسياسات واللوائح لحماية الخصوصية تحديًا كبيرًا.

تم تكريس العديد من الجهود مؤخرًا لتنفيذ خوارزميات التعلم الاتحادي لدعم نماذج تعلم الآلة الفعالة. على وجه التحديد، يحاول الباحثون دعم المزيد من نماذج تعلم الآلة بأساليب مختلفة للحفاظ على الخصوصية، بما في ذلك الشبكات العصبية العميقة [119، 213، 24، 158، 129]، وأشجار القرار المعززة بالتدرج [217، 38، 104]، والانحدار اللوجستي [141، 36]، وآلات المتجهات الداعمة [169]. على سبيل المثال، اقترح Nikolaenko وآخرون [141] وChen وآخرون [36] أساليب لإجراء التعلم الاتحادي بناءً على الانحدار الخطي. نظرًا لأن أشجار القرار المعززة بالتدرج أصبحت ناجحة جدًا في السنوات الأخيرة [34، 200]، فقد تم اقتراح أنظمة التعلم الاتحادي المقابلة من قبل Zhao وآخرين [217]، وCheng وآخرين [38]، وLi وآخرين [104]. علاوة على ذلك، هناك العديد من أنظمة التعلم الاتحادي التي تدعم تدريب الشبكات العصبية. تقترح Google نظام إنتاج قابل للتوسع يمكّن عشرات الملايين من الأجهزة من تدريب شبكة عصبية عميقة [24].

نظرًا لوجود طرق ومكونات بناء مشتركة (مثل آليات الخصوصية مثل الخصوصية التفاضلية) لبناء خوارزميات التعلم الاتحادي، فمن المنطقي تطوير أنظمة وبنى تحتية لتسهيل تطوير خوارزميات التعلم الاتحادي المختلفة. تسمح الأنظمة والبنى التحتية لمطوري الخوارزميات بإعادة استخدام المكونات الأساسية المشتركة، وتجنب بناء الخوارزميات في كل مرة من الصفر. على غرار أنظمة التعلم العميق مثل PyTorch [148، 149] وTensorFlow [7] التي تعزز تطوير خوارزميات التعلم العميق، فإن أنظمة التعلم الاتحادي لها أهمية مماثلة لنجاح التعلم الاتحادي. ومع ذلك، فإن بناء نظام تعلم اتحادي ناجح يشكل تحديًا، حيث يحتاج إلى النظر في جوانب متعددة مثل الفعالية والكفاءة والخصوصية والاستقلالية.

في هذه الورقة، نجري مسحًا شاملاً لأنظمة التعلم الاتحادي الموجودة من منظور النظام. أولاً، نعرض تعريف أنظمة التعلم الاتحادي، ونقارنها بالأنظمة الاتحادية التقليدية. ثانيًا، نحلل مكونات النظام لأنظمة التعلم الاتحادي، بما في ذلك الأطراف، والمدير، وإطار الحوسبة والاتصالات. ثالثًا، نصنف أنظمة التعلم الاتحادي بناءً على ستة جوانب مختلفة: توزيع البيانات، ونموذج تعلم الآلة، وآلية الخصوصية، ومعمارية الاتصال، وحجم الاتحاد، ودافع الاتحاد. يمكن لهذه الجوانب توجيه تصميم نظام التعلم الاتحادي كمكونات بناء مشتركة وتجريدات نظامية. رابعًا، استنادًا إلى هذه الجوانب، نلخص الدراسات الموجودة بشكل منهجي، والتي يمكن استخدامها لتوجيه تصميم أنظمة التعلم الاتحادي. أخيرًا، لجعل التعلم الاتحادي أكثر عملية وقوة، نقدم اتجاهات البحث المستقبلية للعمل عليها. نعتقد أن الأنظمة والبنى التحتية ضرورية لنجاح التعلم الاتحادي. يجب القيام بمزيد من العمل لمعالجة قضايا البحث النظامية في الفعالية والكفاءة والخصوصية والاستقلالية.

---

## 1.1 Related Surveys
## ١.١ المسوحات ذات الصلة

### English Version

There have been several surveys on FL. A seminal survey written by Yang et al. [207] introduces the basics and concepts in FL, and further proposes a comprehensive secure FL framework. The paper mainly target at a relatively small number of parties which are typically enterprise data owners. Li et al. [109] summarize challenges and future directions of FL in massive networks of mobile and edge devices. Recently, Kairouz et al. [85] have a comprehensive description about the characteristics and challenges on FL from different research topics. However, they mainly focus on cross-device FL, where the participants are a very large number of mobile or IoT devices. More recently, another survey [11] summarizes the platforms, protocols and applications of federated learning. Some surveys only focus on an aspect of federated learning. For example, Lim et al. [113] conduct a survey of FL specific to mobile edge computing, while [125] focuses on the threats to federated learning.

### النسخة العربية

كانت هناك عدة مسوحات شاملة حول التعلم الاتحادي. يقدم المسح الأساسي الذي كتبه Yang وآخرون [207] الأساسيات والمفاهيم في التعلم الاتحادي، ويقترح كذلك إطار عمل شامل للتعلم الاتحادي الآمن. تستهدف الورقة بشكل أساسي عددًا صغيرًا نسبيًا من الأطراف التي عادة ما تكون مالكي بيانات المؤسسات. يلخص Li وآخرون [109] التحديات والاتجاهات المستقبلية للتعلم الاتحادي في الشبكات الضخمة من أجهزة الهواتف المحمولة والأجهزة الطرفية. مؤخرًا، قدم Kairouz وآخرون [85] وصفًا شاملاً للخصائص والتحديات المتعلقة بالتعلم الاتحادي من موضوعات بحثية مختلفة. ومع ذلك، فإنهم يركزون بشكل أساسي على التعلم الاتحادي عبر الأجهزة، حيث يكون المشاركون عددًا كبيرًا جدًا من الأجهزة المحمولة أو أجهزة إنترنت الأشياء. في الآونة الأخيرة، يلخص مسح آخر [11] منصات وبروتوكولات وتطبيقات التعلم الاتحادي. تركز بعض المسوحات فقط على جانب واحد من جوانب التعلم الاتحادي. على سبيل المثال، يجري Lim وآخرون [113] مسحًا للتعلم الاتحادي الخاص بالحوسبة الطرفية المحمولة، بينما يركز [125] على التهديدات للتعلم الاتحادي.

---

## 1.2 Our Contribution
## ١.٢ مساهمتنا

### English Version

To the best of our knowledge, there lacks a survey on reviewing existing systems and infrastructure of FLSs and on boosting the attention of creating systems for FL (Similar to prosperous system research in deep learning). In comparison with the previous surveys, the main contributions of this paper are as follows. (1) Our survey is the first one to provide a comprehensive analysis on FL from a system's point of view, including system components, taxonomy, summary, design, and vision. (2) We provide a comprehensive taxonomy against FLSs on six different aspects, including data distribution, machine learning model, privacy mechanism, communication architecture, scale of federation, and motivation of federation, which can be used as common building blocks and system abstractions of FLSs. (3) We summarize existing typical and state-of-the-art studies according to their domains, which is convenient for researchers and developers to refer to. (4) We present the design factors for a successful FLS and comprehensively review solutions for each scenario. (5) We propose interesting research directions and challenges for future generations of FLSs.

### النسخة العربية

على حد علمنا، لا يوجد مسح شامل حول مراجعة الأنظمة والبنية التحتية الموجودة لأنظمة التعلم الاتحادي وتعزيز الاهتمام بإنشاء أنظمة للتعلم الاتحادي (على غرار البحث النظامي المزدهر في التعلم العميق). بالمقارنة مع المسوحات السابقة، فإن المساهمات الرئيسية لهذه الورقة هي كما يلي. (١) يعد مسحنا الشامل الأول الذي يقدم تحليلاً شاملاً للتعلم الاتحادي من منظور النظام، بما في ذلك مكونات النظام، والتصنيف، والملخص، والتصميم، والرؤية. (٢) نقدم تصنيفًا شاملاً لأنظمة التعلم الاتحادي على ستة جوانب مختلفة، بما في ذلك توزيع البيانات، ونموذج تعلم الآلة، وآلية الخصوصية، ومعمارية الاتصال، وحجم الاتحاد، ودافع الاتحاد، والتي يمكن استخدامها كمكونات بناء مشتركة وتجريدات نظامية لأنظمة التعلم الاتحادي. (٣) نلخص الدراسات النموذجية والحديثة الموجودة وفقًا لمجالاتها، مما يسهل على الباحثين والمطورين الرجوع إليها. (٤) نقدم عوامل التصميم لنظام تعلم اتحادي ناجح ونراجع بشكل شامل الحلول لكل سيناريو. (٥) نقترح اتجاهات بحثية مثيرة للاهتمام وتحديات للأجيال المستقبلية من أنظمة التعلم الاتحادي.

---

### Translation Notes

**Key Terms Used:**
- Federated Learning: التعلم الاتحادي
- Data islands: جزر البيانات
- Privacy: الخصوصية
- Machine Learning: تعلم الآلة
- Deep Neural Networks: الشبكات العصبية العميقة
- Gradient Boosted Decision Trees (GBDTs): أشجار القرار المعززة بالتدرج
- Differential Privacy: الخصوصية التفاضلية
- System Components: مكونات النظام
- Communication Architecture: معمارية الاتصال
- Cross-device: عبر الأجهزة
- Cross-silo: عبر الصوامع

**Translation Quality Metrics:**
- Section length: ~800 words
- Technical accuracy: Maintained all technical terms and citations
- Glossary consistency: All terms match established glossary
- Flow: Natural Arabic sentence structure
- Completeness: All subsections translated (1.1, 1.2)
