# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** federated learning (تعلم اتحادي), neural network (شبكة عصبية), privacy (خصوصية), distributed (موزع), model (نموذج), training (التدريب), optimization (التحسين), client (عميل), SGD (الانحدار التدرجي العشوائي), non-IID (غير مستقل ومتماثل التوزيع), communication (الاتصال), convergence (تقارب)

---

### English Version

**1. Introduction**

Increasingly, phones and tablets are the primary computing devices for many people, and these devices hold a wealth of data suitable for learning models. However, these rich datasets are often privacy-sensitive or too large to directly collect and centralize for training. We advocate an alternative that leaves the training data distributed on the mobile devices, and learns a shared model by aggregating locally-computed updates. We term this decentralized approach Federated Learning.

The term Federated Learning was introduced because the learning task is solved by a loose federation of participating devices (which we refer to as *clients*) which are coordinated by a central *server*. Each client has a local training dataset that is never uploaded to the server. Instead, each client computes an update to the current global model maintained by the server, and only this update is communicated.

The decoupling of model training from the need for direct access to the raw training data represents a significant step forward in privacy protection for user data. It directly embodies the principle of focused collection, or data minimization, articulated in the Fair Information Practice Principles and in the 2012 White House report on privacy in the age of big data. Moreover, the updates themselves can be ephemeral, and as we only need to protect them during the very brief window when they are used by the server to update the model, secure computation techniques can be applied. We can also avoid tagging the updates with identifying metadata by using anonymous communication protocols or proxies such as Tor.

There are three main contributions of this paper. First, we identify the problem of training on decentralized data from mobile devices as an important research direction with significant practical applications. Second, we select a straightforward and practical algorithm that can be applied to this setting, and show that it works well. Third, we perform an extensive empirical evaluation of our proposed approach. While there has been significant progress on the related problems of privacy and communication efficiency, there has not been, to our knowledge, any previous work that combines both of these concerns with the distributional issues that arise when training on real-world data from mobile devices.

Our proposed algorithm, which we term FederatedAveraging, can train deep networks for many realistic supervised learning tasks using a number of communication rounds that is dramatically smaller than both the number of training examples and the number of training batches required to train the model via standard SGD. The algorithm combines local stochastic gradient descent (SGD) on each client with a server that performs model averaging.

The ideal federated learning problem has several additional properties that further complicate the setting, and distinguish it from typical distributed optimization problems:
- **Non-IID.** The training data on a given client is typically based on the usage of the mobile device by a particular user, and hence any particular user's local dataset will not be representative of the population distribution.
- **Unbalanced.** Similarly, some users will make much heavier use of the service or app than others, leading to varying amounts of local training data.
- **Massively distributed.** We expect the number of clients participating in an optimization to be much larger than the average number of examples per client.
- **Limited communication.** Mobile devices are frequently offline or on slow or expensive connections.

Many of these issues are fundamental to the federated learning setting, and for this work we focus primarily on the non-IID and unbalanced properties of the data, and on the critical issue of communication efficiency. To simplify our presentation and allow for controlled experiments, we employ a synchronous update scheme that proceeds in rounds of communication. For the purposes of this work, we assume a fixed set of K clients, each with a fixed local dataset.

At the beginning of each round, a random fraction of clients is selected, and the server sends the current global model to those clients. The selected clients then perform local computation based on the global state and their local dataset, and send an update to the server. The server then applies these updates to the global model, and the process repeats. Although it is not the primary focus of this paper, we note that asynchronous methods (Dean et al., 2012), methods that allow clients to be added or dropped during the training process, and methods to further reduce communication costs through quantization and subsampling are all important directions for future work.

We formulate the optimization problem implicit in federated learning as follows. We assume we have K clients, indexed by k, each with a local dataset D_k. At a high level, federated optimization seeks to minimize the following objective:

$$f(w) = \sum_{k=1}^{K} \frac{n_k}{n} F_k(w)$$

where $n_k = |D_k|$ is the number of data points on client k, $n = \sum_k n_k$ is the total number of data points, and $F_k(w) = \frac{1}{n_k} \sum_{i \in D_k} f_i(w)$ is the local objective function for client k.

We can rewrite this as $f(w) = \mathbb{E}_{k \sim P}[F_k(w)]$ where the expectation is over a uniform distribution on clients. This formulation captures the "average over clients" objective. In typical applications of distributed optimization, the data is distributed across workers such that each local dataset $D_k$ is a uniformly drawn random sample from the full dataset. Under the IID assumption, $F_k$ is an unbiased estimate of the full objective f, and we can use a wide array of existing optimization techniques. However, in the federated learning setting, there is no particular reason to assume data on different clients comes from the same underlying distribution (the non-IID case).

One central challenge in federated optimization is that communication costs dominate—we will typically be limited by an upload bandwidth of 1 MB/s or less. Furthermore, in the federated learning setting, clients are only available for training when they are idle, charged, plugged-in, and on an unmetered wi-fi connection; thus, clients may participate in only a small number of communication rounds.

In distributed settings where communication is expensive, two primary approaches can add computation to decrease communication costs: (1) Increased parallelism, where we use more clients working independently between each communication round. (2) Increased computation on each client, where rather than performing a simple computation like a gradient calculation, each client performs a more complex calculation between each communication round. Our experiments show that for our applications, the speedups we are able to achieve in federated optimization are due primarily to adding more computation on each client, and to a lesser extent (at most 2×) from adding more parallelism.

**Prior and Related Work.** The problem of training a model using an iterative averaging process of locally trained models has been studied in prior work (McDonald et al., 2009; Mann et al., 2009; Zinkevich et al., 2010; Neverova et al., 2014; Agarwal & Duchi, 2011), but in cluster settings with IID balanced data distributions. As argued above, these properties do not hold in the federated setting—data is massively distributed and is both unbalanced and non-IID.

Prior work on model-parallel training of neural networks, such as Dean et al. (2012), uses hundreds or thousands of nodes with the goal of training a single model faster. This work focuses on data parallelism where computation is distributed across clients, each with a completely independent dataset. The related problem of split learning (Gupta & Raskar, 2018) distributes model training to protect privacy, but relies on a different set of assumptions.

One-shot averaging of SGD-trained models (Zhang et al., 2015, 2016; Povey et al., 2014) has also been studied for distributed settings. These approaches iteratively average models that have each been trained to completion in isolation. Our experiments suggest that the more frequent averaging performed by FedAvg produces models that are at least as accurate while being much more communication efficient.

There has been significant recent work on asynchronous methods for distributed learning, including both general convex objectives (Richtárik & Takáč, 2016; McMahan & Streeter, 2014) and deep learning (Dean et al., 2012; Chilimbi et al., 2014; Recht et al., 2011; Xing et al., 2015). While such approaches do not require clients to synchronize, they still need to communicate with the server multiple times during training. Given the limited communication bandwidth in federated settings and the constraints on client availability discussed above, we focus on synchronous updates in this work.

There is significant recent interest in privacy-preserving machine learning (Fredrikson et al., 2015; Shokri & Shmatikov, 2015; Abadi et al., 2016). The approach of federated learning itself provides a privacy advantage, as the raw training data never leaves the device. Additional techniques such as differential privacy (Dwork et al., 2006) and secure multi-party computation can provide even stronger privacy guarantees. We view the combination of federated optimization with differential privacy or secure computation as a promising direction for future work.

---

### النسخة العربية

**1. المقدمة**

بشكل متزايد، أصبحت الهواتف والأجهزة اللوحية هي أجهزة الحوسبة الأساسية للكثير من الناس، وتحتوي هذه الأجهزة على ثروة من البيانات المناسبة لتعلم النماذج. ومع ذلك، فإن مجموعات البيانات الغنية هذه غالباً ما تكون حساسة للخصوصية أو كبيرة جداً بحيث لا يمكن جمعها ومركزتها مباشرة للتدريب. نحن ندعو إلى بديل يترك بيانات التدريب موزعة على الأجهزة المحمولة، ويتعلم نموذجاً مشتركاً من خلال تجميع التحديثات المحسوبة محلياً. نطلق على هذا النهج اللامركزي اسم التعلم الاتحادي.

تم تقديم مصطلح التعلم الاتحادي لأن مهمة التعلم يتم حلها من خلال اتحاد فضفاض من الأجهزة المشاركة (التي نشير إليها بـ *العملاء*) والتي يتم تنسيقها بواسطة *خادم* مركزي. كل عميل لديه مجموعة بيانات تدريب محلية لا يتم تحميلها أبداً إلى الخادم. بدلاً من ذلك، يحسب كل عميل تحديثاً للنموذج العام الحالي الذي يحتفظ به الخادم، ويتم إرسال هذا التحديث فقط.

يمثل فصل تدريب النموذج عن الحاجة إلى الوصول المباشر إلى بيانات التدريب الأولية خطوة كبيرة إلى الأمام في حماية الخصوصية لبيانات المستخدم. إنه يجسد مباشرة مبدأ الجمع المركز، أو تقليل البيانات، المنصوص عليه في مبادئ ممارسات المعلومات العادلة وفي تقرير البيت الأبيض لعام 2012 حول الخصوصية في عصر البيانات الضخمة. علاوة على ذلك، يمكن أن تكون التحديثات نفسها مؤقتة، وبما أننا نحتاج فقط إلى حمايتها خلال النافذة القصيرة جداً عندما يستخدمها الخادم لتحديث النموذج، يمكن تطبيق تقنيات الحوسبة الآمنة. يمكننا أيضاً تجنب وضع علامات على التحديثات بالبيانات الوصفية المعرفة باستخدام بروتوكولات الاتصال المجهولة أو الوكلاء مثل Tor.

هناك ثلاث مساهمات رئيسية لهذا البحث. أولاً، نحدد مشكلة التدريب على البيانات اللامركزية من الأجهزة المحمولة كاتجاه بحثي مهم له تطبيقات عملية كبيرة. ثانياً، نختار خوارزمية مباشرة وعملية يمكن تطبيقها في هذا السياق، ونوضح أنها تعمل بشكل جيد. ثالثاً، نجري تقييماً تجريبياً موسعاً للنهج المقترح. في حين كان هناك تقدم كبير في المشاكل ذات الصلة بالخصوصية وكفاءة الاتصال، لم يكن هناك، على حد علمنا، أي عمل سابق يجمع بين كل من هذه الاهتمامات مع المسائل التوزيعية التي تنشأ عند التدريب على بيانات واقعية من الأجهزة المحمولة.

الخوارزمية المقترحة، والتي نطلق عليها اسم متوسط الاتحادي (FederatedAveraging)، يمكنها تدريب الشبكات العميقة للعديد من مهام التعلم الخاضع للإشراف الواقعية باستخدام عدد من جولات الاتصال أصغر بكثير من عدد أمثلة التدريب وعدد دفعات التدريب المطلوبة لتدريب النموذج عبر الانحدار التدرجي العشوائي القياسي. تجمع الخوارزمية بين الانحدار التدرجي العشوائي المحلي على كل عميل مع خادم يقوم بحساب متوسط النماذج.

تحتوي مشكلة التعلم الاتحادي المثالية على عدة خصائص إضافية تزيد من تعقيد الإعداد، وتميزه عن مشاكل التحسين الموزعة النموذجية:
- **غير مستقل ومتماثل التوزيع (Non-IID).** بيانات التدريب على عميل معين عادة ما تكون مبنية على استخدام الجهاز المحمول من قبل مستخدم معين، وبالتالي فإن مجموعة البيانات المحلية لأي مستخدم معين لن تكون ممثلة لتوزيع السكان.
- **غير متوازنة.** بالمثل، سيستخدم بعض المستخدمين الخدمة أو التطبيق بشكل أكثر كثافة من غيرهم، مما يؤدي إلى كميات متفاوتة من بيانات التدريب المحلية.
- **موزعة بشكل ضخم.** نتوقع أن يكون عدد العملاء المشاركين في التحسين أكبر بكثير من متوسط عدد الأمثلة لكل عميل.
- **اتصال محدود.** الأجهزة المحمولة غالباً ما تكون غير متصلة بالإنترنت أو على اتصالات بطيئة أو مكلفة.

العديد من هذه المسائل أساسية لإعداد التعلم الاتحادي، وفي هذا العمل نركز بشكل أساسي على الخصائص غير المستقلة وغير المتوازنة للبيانات، وعلى القضية الحرجة المتعلقة بكفاءة الاتصال. لتبسيط عرضنا والسماح بتجارب محكومة، نستخدم مخطط تحديث متزامن يتقدم في جولات من الاتصال. لأغراض هذا العمل، نفترض مجموعة ثابتة من K عميل، كل منهم لديه مجموعة بيانات محلية ثابتة.

في بداية كل جولة، يتم اختيار جزء عشوائي من العملاء، ويرسل الخادم النموذج العام الحالي إلى هؤلاء العملاء. ثم يقوم العملاء المختارون بإجراء حساب محلي بناءً على الحالة العامة ومجموعة بياناتهم المحلية، ويرسلون تحديثاً إلى الخادم. ثم يطبق الخادم هذه التحديثات على النموذج العام، وتتكرر العملية. على الرغم من أنه ليس التركيز الأساسي لهذا البحث، نلاحظ أن الطرق اللامتزامنة (Dean et al., 2012)، والطرق التي تسمح بإضافة أو إسقاط العملاء خلال عملية التدريب، والطرق لتقليل تكاليف الاتصال بشكل أكبر من خلال التكميم والاختزال هي كلها اتجاهات مهمة للعمل المستقبلي.

نصيغ مشكلة التحسين الضمنية في التعلم الاتحادي على النحو التالي. نفترض أن لدينا K عميل، مفهرس بـ k، كل منهم لديه مجموعة بيانات محلية $D_k$. على مستوى عالٍ، يسعى التحسين الاتحادي إلى تقليل الدالة الهدفية التالية:

$$f(w) = \sum_{k=1}^{K} \frac{n_k}{n} F_k(w)$$

حيث $n_k = |D_k|$ هو عدد نقاط البيانات على العميل k، و $n = \sum_k n_k$ هو إجمالي عدد نقاط البيانات، و $F_k(w) = \frac{1}{n_k} \sum_{i \in D_k} f_i(w)$ هي الدالة الهدفية المحلية للعميل k.

يمكننا إعادة كتابة هذا كـ $f(w) = \mathbb{E}_{k \sim P}[F_k(w)]$ حيث التوقع هو على توزيع موحد على العملاء. تلتقط هذه الصياغة هدف "المتوسط عبر العملاء". في التطبيقات النموذجية للتحسين الموزع، يتم توزيع البيانات عبر العمال بحيث تكون كل مجموعة بيانات محلية $D_k$ عينة عشوائية مسحوبة بشكل موحد من مجموعة البيانات الكاملة. في ظل افتراض IID، فإن $F_k$ هو تقدير غير متحيز للهدف الكامل f، ويمكننا استخدام مجموعة واسعة من تقنيات التحسين الموجودة. ومع ذلك، في إعداد التعلم الاتحادي، لا يوجد سبب خاص لافتراض أن البيانات على العملاء المختلفين تأتي من نفس التوزيع الأساسي (حالة non-IID).

أحد التحديات المركزية في التحسين الاتحادي هو أن تكاليف الاتصال تهيمن - سنكون عادةً محدودين بنطاق ترددي للتحميل يبلغ 1 ميجابايت/ثانية أو أقل. علاوة على ذلك، في إعداد التعلم الاتحادي، لا يكون العملاء متاحين للتدريب إلا عندما يكونون في وضع الخمول، مشحونين، موصولين بالكهرباء، وعلى اتصال wi-fi غير محدود؛ وبالتالي، قد يشارك العملاء في عدد صغير فقط من جولات الاتصال.

في الإعدادات الموزعة حيث يكون الاتصال مكلفاً، يمكن لنهجين رئيسيين إضافة حساب لتقليل تكاليف الاتصال: (1) زيادة التوازي، حيث نستخدم المزيد من العملاء الذين يعملون بشكل مستقل بين كل جولة اتصال. (2) زيادة الحساب على كل عميل، حيث بدلاً من إجراء حساب بسيط مثل حساب التدرج، يقوم كل عميل بإجراء حساب أكثر تعقيداً بين كل جولة اتصال. تظهر تجاربنا أنه بالنسبة لتطبيقاتنا، فإن التسريعات التي نحن قادرون على تحقيقها في التحسين الاتحادي تعود بشكل أساسي إلى إضافة المزيد من الحساب على كل عميل، وإلى حد أقل (على الأكثر 2×) من إضافة المزيد من التوازي.

**الأعمال السابقة وذات الصلة.** تمت دراسة مشكلة تدريب نموذج باستخدام عملية متوسط تكرارية للنماذج المدربة محلياً في أعمال سابقة (McDonald et al., 2009; Mann et al., 2009; Zinkevich et al., 2010; Neverova et al., 2014; Agarwal & Duchi, 2011)، ولكن في إعدادات الكتلة مع توزيعات بيانات IID متوازنة. كما جادلنا أعلاه، هذه الخصائص لا تنطبق على الإعداد الاتحادي - البيانات موزعة بشكل ضخم وكل من غير متوازنة وغير IID.

الأعمال السابقة على التدريب الموازي للنموذج للشبكات العصبية، مثل Dean et al. (2012)، تستخدم مئات أو آلاف العقد بهدف تدريب نموذج واحد بشكل أسرع. يركز هذا العمل على توازي البيانات حيث يتم توزيع الحساب عبر العملاء، كل منهم لديه مجموعة بيانات مستقلة تماماً. المشكلة ذات الصلة بالتعلم المقسم (Gupta & Raskar, 2018) توزع تدريب النموذج لحماية الخصوصية، ولكنها تعتمد على مجموعة مختلفة من الافتراضات.

تمت أيضاً دراسة متوسط لقطة واحدة للنماذج المدربة بـ SGD (Zhang et al., 2015, 2016; Povey et al., 2014) للإعدادات الموزعة. تحسب هذه الأساليب بشكل تكراري متوسط النماذج التي تم تدريب كل منها حتى الاكتمال في عزلة. تشير تجاربنا إلى أن المتوسط الأكثر تكراراً الذي يقوم به FedAvg ينتج نماذج دقيقة على الأقل مع كونها أكثر كفاءة في الاتصال بكثير.

كان هناك عمل حديث كبير على الطرق اللامتزامنة للتعلم الموزع، بما في ذلك كل من الأهداف المحدبة العامة (Richtárik & Takáč, 2016; McMahan & Streeter, 2014) والتعلم العميق (Dean et al., 2012; Chilimbi et al., 2014; Recht et al., 2011; Xing et al., 2015). في حين أن مثل هذه الأساليب لا تتطلب من العملاء المزامنة، فإنهم لا يزالون بحاجة إلى الاتصال بالخادم عدة مرات أثناء التدريب. نظراً لنطاق الاتصال المحدود في الإعدادات الاتحادية والقيود على توفر العميل المذكورة أعلاه، نركز على التحديثات المتزامنة في هذا العمل.

هناك اهتمام حديث كبير في التعلم الآلي الذي يحافظ على الخصوصية (Fredrikson et al., 2015; Shokri & Shmatikov, 2015; Abadi et al., 2016). يوفر نهج التعلم الاتحادي نفسه ميزة خصوصية، حيث لا تغادر بيانات التدريب الأولية الجهاز أبداً. يمكن لتقنيات إضافية مثل الخصوصية التفاضلية (Dwork et al., 2006) والحوسبة متعددة الأطراف الآمنة توفير ضمانات خصوصية أقوى. نرى الجمع بين التحسين الاتحادي مع الخصوصية التفاضلية أو الحوسبة الآمنة كاتجاه واعد للعمل المستقبلي.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** Federated Learning (التعلم الاتحادي), FederatedAveraging (متوسط الاتحادي), client (عميل), server (خادم), non-IID (غير مستقل ومتماثل التوزيع), unbalanced (غير متوازنة)
- **Equations:** 2 main equations (objective function and expectation formulation)
- **Citations:** Approximately 20 references cited
- **Special handling:** Mathematical notation preserved in LaTeX format; technical terms kept consistent with glossary

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
