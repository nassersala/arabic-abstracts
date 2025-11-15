# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.91
**Glossary Terms Used:** convolutional neural networks (الشبكات العصبية التلافيفية), deep learning (تعلم عميق), architecture (معمارية), layers (طبقات), gradient (تدرج), vanishing gradient (اختفاء التدرج), identity connections (اتصالات الهوية), ResNets (شبكات ResNet), Highway Networks (شبكات الطرق السريعة), stochastic depth (عمق عشوائي), FractalNets (شبكات كسورية), feature-maps (خرائط الميزات)

---

### English Version

Convolutional neural networks (CNNs) have become the dominant machine learning approach for visual object recognition. Although they were originally introduced over 20 years ago [18], improvements in computer hardware and network structure have enabled the training of truly deep CNNs only recently. The original LeNet5 [19] consisted of 5 layers, VGG featured 19 [29], and only last year Highway Networks [34] and Residual Networks (ResNets) [11] have surpassed the 100-layer barrier.

As CNNs become increasingly deep, a new research problem emerges: as information about the input or gradient passes through many layers, it can vanish and "wash out" by the time it reaches the end (or beginning) of the network. Many recent publications address this or related problems. ResNets [11] and Highway Networks [34] bypass signal from one layer to the next via identity connections. Stochastic depth [13] shortens ResNets by randomly dropping layers during training to allow better information and gradient flow. FractalNets [17] repeatedly combine several parallel layer sequences with different number of convolutional blocks to obtain a large nominal depth, while maintaining many short paths in the network. Although these different approaches vary in network topology and training procedure, they all share a key characteristic: they create short paths from early layers to later layers.

In this paper, we propose an architecture that distills this insight into a simple connectivity pattern: to ensure maximum information flow between layers in the network, we connect all layers (with matching feature-map sizes) directly with each other. To preserve the feed-forward nature, each layer obtains additional inputs from all preceding layers and passes on its own feature-maps to all subsequent layers. Figure 1 illustrates this layout schematically. Crucially, in contrast to ResNets, we never combine features through summation before they are passed into a layer; instead, we combine features by concatenating them. Hence, the ℓth layer has ℓ inputs, consisting of the feature-maps of all preceding convolutional blocks. Its own feature-maps are passed on to all L − ℓ subsequent layers. This introduces L(L+1)/2 connections in an L-layer network, instead of just L, as in traditional architectures. Because of its dense connectivity pattern, we refer to our approach as Dense Convolutional Network (DenseNet).

A possibly counter-intuitive effect of this dense connectivity pattern is that it requires fewer parameters than traditional convolutional networks, as there is no need to re-learn redundant feature-maps. Traditional feed-forward architectures can be viewed as algorithms with a state, which is passed on from layer to layer. Each layer reads the state from its preceding layer and writes to the subsequent layer. It changes the state but also passes on information that needs to be preserved. ResNets [11] make this information preservation explicit through additive identity transformations. Recent variations of ResNets [13] show that many layers contribute very little and can in fact be randomly dropped during training. This makes the state of ResNets similar to (unrolled) recurrent neural networks [21], but the number of parameters of ResNets is substantially larger because each layer has its own weights. Our proposed DenseNet architecture explicitly differentiates between information that is added to the network and information that is preserved. DenseNet layers are very narrow (e.g., 12 filters per layer), adding only a small set of feature-maps to the "collective knowledge" of the network and keep the remaining feature-maps unchanged—and the final classifier makes a decision based on all feature-maps in the network.

Besides better parameter efficiency, one big advantage of DenseNets is their improved flow of information and gradients throughout the network, which makes them easy to train. Each layer has direct access to the gradients from the loss function and the original input signal, leading to an implicit deep supervision [20]. This helps training of deeper network architectures. Further, we also observe that dense connections have a regularizing effect, which reduces overfitting on tasks with smaller training set sizes.

We evaluate DenseNets on four highly competitive benchmark datasets (CIFAR-10, CIFAR-100, SVHN, and ImageNet). Our models tend to require much fewer parameters than existing algorithms with comparable accuracy. Further, we significantly outperform the current state-of-the-art results on most of the benchmark tasks.

---

### النسخة العربية

أصبحت الشبكات العصبية التلافيفية (CNNs) النهج السائد في التعلم الآلي للتعرف على الأجسام المرئية. على الرغم من أنها قُدمت في الأصل منذ أكثر من 20 عاماً [18]، إلا أن التحسينات في أجهزة الكمبيوتر وبنية الشبكات مكّنت من تدريب شبكات CNNs عميقة حقاً مؤخراً فقط. تكونت شبكة LeNet5 الأصلية [19] من 5 طبقات، وتميزت VGG بـ 19 طبقة [29]، وفي العام الماضي فقط تجاوزت شبكات الطرق السريعة (Highway Networks) [34] والشبكات المتبقية (ResNets) [11] حاجز 100 طبقة.

مع ازدياد عمق شبكات CNNs، تظهر مشكلة بحثية جديدة: حيث أن المعلومات حول المدخلات أو التدرج تمر عبر العديد من الطبقات، يمكن أن تختفي وتتلاشى بحلول الوقت الذي تصل فيه إلى نهاية الشبكة (أو بدايتها). تتناول العديد من المنشورات الحديثة هذه المشكلة أو المشاكل ذات الصلة. تتجاوز شبكات ResNets [11] وشبكات Highway [34] الإشارة من طبقة إلى أخرى عبر اتصالات الهوية. يقصر العمق العشوائي (Stochastic depth) [13] شبكات ResNets من خلال إسقاط الطبقات عشوائياً أثناء التدريب للسماح بتدفق أفضل للمعلومات والتدرج. تجمع شبكات FractalNets [17] بشكل متكرر عدة تسلسلات طبقات متوازية بعدد مختلف من الكتل التلافيفية للحصول على عمق اسمي كبير، مع الحفاظ على العديد من المسارات القصيرة في الشبكة. على الرغم من أن هذه الأساليب المختلفة تختلف في طوبولوجيا الشبكة وإجراءات التدريب، إلا أنها جميعاً تشترك في خاصية رئيسية: فهي تخلق مسارات قصيرة من الطبقات المبكرة إلى الطبقات اللاحقة.

في هذه الورقة، نقترح معمارية تقطر هذه الرؤية إلى نمط اتصال بسيط: لضمان أقصى تدفق للمعلومات بين الطبقات في الشبكة، نربط جميع الطبقات (ذات أحجام خرائط الميزات المتطابقة) مباشرة ببعضها البعض. للحفاظ على طبيعة التغذية الأمامية، تحصل كل طبقة على مدخلات إضافية من جميع الطبقات السابقة وتمرر خرائط ميزاتها الخاصة إلى جميع الطبقات اللاحقة. يوضح الشكل 1 هذا التخطيط بشكل تخطيطي. والأهم من ذلك، على النقيض من شبكات ResNets، لا نجمع الميزات أبداً من خلال الجمع قبل تمريرها إلى طبقة؛ بدلاً من ذلك، نجمع الميزات عن طريق ربطها. وبالتالي، فإن الطبقة ℓ لها ℓ مدخلات، تتكون من خرائط الميزات لجميع الكتل التلافيفية السابقة. يتم تمرير خرائط ميزاتها الخاصة إلى جميع الطبقات اللاحقة L − ℓ. يؤدي هذا إلى إدخال L(L+1)/2 اتصالاً في شبكة من L طبقة، بدلاً من L فقط، كما هو الحال في المعماريات التقليدية. بسبب نمط الاتصال الكثيف هذا، نشير إلى نهجنا باسم الشبكة التلافيفية الكثيفة (DenseNet).

التأثير المحتمل المضاد للحدس لنمط الاتصال الكثيف هذا هو أنه يتطلب معاملات أقل من الشبكات التلافيفية التقليدية، حيث لا حاجة لإعادة تعلم خرائط الميزات الزائدة. يمكن النظر إلى معماريات التغذية الأمامية التقليدية على أنها خوارزميات ذات حالة، يتم تمريرها من طبقة إلى طبقة. تقرأ كل طبقة الحالة من الطبقة السابقة لها وتكتب إلى الطبقة اللاحقة. إنها تغير الحالة ولكنها تمرر أيضاً المعلومات التي تحتاج إلى الحفاظ عليها. تجعل شبكات ResNets [11] هذا الحفاظ على المعلومات صريحاً من خلال تحويلات الهوية الجمعية. تُظهر الاختلافات الحديثة لشبكات ResNets [13] أن العديد من الطبقات تساهم بالقليل جداً ويمكن في الواقع إسقاطها عشوائياً أثناء التدريب. هذا يجعل حالة شبكات ResNets مشابهة للشبكات العصبية المتكررة (غير المطوية) [21]، لكن عدد معاملات شبكات ResNets أكبر بكثير لأن كل طبقة لها أوزانها الخاصة. تميز معمارية DenseNet المقترحة بشكل صريح بين المعلومات التي تضاف إلى الشبكة والمعلومات التي يتم الحفاظ عليها. طبقات DenseNet ضيقة جداً (مثلاً، 12 مرشحاً لكل طبقة)، وتضيف مجموعة صغيرة فقط من خرائط الميزات إلى "المعرفة الجماعية" للشبكة وتحافظ على خرائط الميزات المتبقية دون تغيير—ويتخذ المصنف النهائي قراراً بناءً على جميع خرائط الميزات في الشبكة.

بالإضافة إلى كفاءة المعاملات الأفضل، فإن إحدى المزايا الكبيرة لشبكات DenseNets هي تدفق المعلومات والتدرجات المحسّن في جميع أنحاء الشبكة، مما يجعلها سهلة التدريب. كل طبقة لديها وصول مباشر إلى التدرجات من دالة الخسارة وإشارة المدخلات الأصلية، مما يؤدي إلى إشراف عميق ضمني [20]. يساعد هذا في تدريب معماريات الشبكات الأعمق. علاوة على ذلك، نلاحظ أيضاً أن الاتصالات الكثيفة لها تأثير منظم، مما يقلل من الإفراط في التكيف على المهام ذات أحجام مجموعات التدريب الأصغر.

نقوم بتقييم شبكات DenseNets على أربع مجموعات بيانات معيارية تنافسية للغاية (CIFAR-10 وCIFAR-100 وSVHN وImageNet). تميل نماذجنا إلى أن تتطلب معاملات أقل بكثير من الخوارزميات الموجودة ذات الدقة المماثلة. علاوة على ذلك، نتفوق بشكل كبير على نتائج أحدث ما توصل إليه العلم الحالية في معظم مهام المعايير.

---

### Translation Notes

- **Figures referenced:** Figure 1 (dense block illustration)
- **Key terms introduced:** Dense Convolutional Network (DenseNet), dense connectivity, collective knowledge, implicit deep supervision
- **Equations:** L(L+1)/2 connections formula
- **Citations:** [18], [19], [29], [34], [11], [13], [17], [21], [20]
- **Special handling:** Mathematical notation (ℓ, L) preserved, network names kept recognizable (LeNet5, VGG, ResNets)

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.89
- Glossary consistency: 0.91
- **Overall section score:** 0.91

### Back-translation Check

Key concept back-translated: "الشبكة التلافيفية الكثيفة (DenseNet) تربط جميع الطبقات ذات أحجام خرائط الميزات المتطابقة مباشرة ببعضها البعض" → "Dense Convolutional Network (DenseNet) connects all layers with matching feature-map sizes directly to each other" - preserves original meaning accurately.
