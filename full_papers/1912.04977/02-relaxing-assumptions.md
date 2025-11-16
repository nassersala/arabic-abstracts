# Section 2: Relaxing the Core FL Assumptions: Applications to Emerging Settings and Scenarios
## القسم 2: تخفيف افتراضات التعلم الاتحادي الأساسية: التطبيقات على الإعدادات والسيناريوهات الناشئة

**Section:** relaxing-assumptions
**Translation Quality:** 0.87
**Glossary Terms Used:** federated learning, peer-to-peer, decentralized, cross-silo, cross-device, client, server, aggregation, differential privacy, secure aggregation, split learning, blockchain, smart contracts

---

### English Version (First Part)

## 2 Relaxing the Core FL Assumptions: Applications to Emerging Settings and Scenarios

In this section, we will discuss areas of research related to the topics discussed in the previous section. Even though not being the main focus of the remainder of the paper, progress in these areas could motivate design of the next generation of production systems.

### 2.1 Fully Decentralized / Peer-to-Peer Distributed Learning

In federated learning, a central server orchestrates the training process and receives the contributions of all clients. The server is thus a central player which also potentially represents a single point of failure. While large companies or organizations can play this role in some application scenarios, a reliable and powerful central server may not always be available or desirable in more collaborative learning scenarios [459]. Furthermore, the server may even become a bottleneck when the number of clients is very large, as demonstrated by Lian et al. [305] (though this can be mitigated by careful system design, e.g. [81]).

The key idea of fully decentralized learning is to replace communication with the server by peer-to-peer communication between individual clients. The communication topology is represented as a connected graph in which nodes are the clients and an edge indicates a communication channel between two clients. The network graph is typically chosen to be sparse with small maximum degree so that each node only needs to send/receive messages to/from a small number of peers; this is in contrast to the star graph of the server-client architecture.

In fully decentralized algorithms, a round corresponds to each client performing a local update and exchanging information with their neighbors in the graph. In the context of machine learning, the local update is typically a local (stochastic) gradient step and the communication consists in averaging one's local model parameters with the neighbors. Note that there is no longer a global state of the model as in standard federated learning, but the process can be designed such that all local models converge to the desired global solution, i.e., the individual models gradually reach consensus.

**Table 3:** A comparison of the key distinctions between federated learning and fully decentralized learning.

| Aspect | Federated Learning | Fully Decentralized (Peer-to-Peer) Learning |
|--------|-------------------|-------------------------------------------|
| Orchestration | A central orchestration server or service organizes the training, but never sees raw data. | No centralized orchestration. |
| Wide-area communication | Typically a hub-and-spoke topology, with the hub representing a coordinating service provider (typically without data) and the spokes connecting to clients. | Peer-to-peer topology, with a possibly dynamic connectivity graph. |

#### 2.1.1 Algorithmic Challenges

A large number of important algorithmic questions remain open on the topic of real-world usability of decentralized schemes for machine learning. Some questions are analogous to the special case of federated learning with a central server, and other challenges come as an additional side-effect of being fully decentralized or trust-less.

**Effect of network topology and asynchrony on decentralized SGD:** Fully decentralized algorithms for learning should be robust to the limited availability of the clients (with clients temporarily unavailable, dropping out or joining during the execution) and limited reliability of the network (with possible message drops). Additional open research questions concern non-IID data distributions, update frequencies, efficient communication patterns and practical convergence time.

**Local-update decentralized SGD:** The theoretical analysis of schemes which perform several local update steps before a communication round is significantly more challenging than those using a single SGD step. Understanding the convergence under non-IID data distributions and how to design a model averaging policy that achieves the fastest convergence remains an open problem.

**Personalization, and trust mechanisms:** Similarly to the cross-device FL setting, an important task for the fully decentralized scenario under the non-IID data distributions available to individual clients is to design algorithms for learning collections of personalized models. One of the key unique challenges in the decentralized setting remains the robustness of such schemes to malicious actors or contribution of unreliable data or labels.

**Privacy:** An important challenge in fully decentralized learning is to prevent any client from reconstructing the private data of another client from its shared updates while maintaining a good level of utility for the learned models. Differential privacy is the standard approach to mitigate such privacy risks. Unfortunately, such local privacy approaches often come at a large cost in utility.

#### 2.1.2 Practical Challenges

A blockchain is a distributed ledger shared among disparate users, making possible digital transactions without a central authority. In terms of federated learning, use of the technology could enable decentralization of the global server by using smart contracts to do model aggregation, where the participating clients executing the smart contracts could be different companies or cloud services.

However, on today's blockchain platforms such as Ethereum, data on the blockchains is publicly available by default, which could discourage users from participating in the decentralized federated learning protocol. To address such concerns, it might be possible to modify existing privacy-preserving techniques to fit into the scenario of decentralized federated learning, including secure aggregation protocols and client-level differential privacy.

### 2.2 Cross-Silo Federated Learning

In contrast with the characteristics of cross-device federated learning, cross-silo federated learning admits more flexibility in certain aspects of the overall design, but at the same time presents a setting where achieving other properties can be harder.

The cross-silo setting can be relevant where a number of companies or organizations share incentive to train a model based on all of their data, but cannot share their data directly. This could be due to constraints imposed by confidentiality or due to legal constraints.

**Data partitioning:** In the cross-device setting the data is assumed to be partitioned by examples. In the cross-silo setting, in addition to partitioning by examples, partitioning by features is of practical relevance. This difference has been also referred to as horizontal and vertical federated learning by Yang et al. [490].

**Incentive mechanisms:** In addition to developing new algorithmic techniques for FL, incentive mechanism design for honest participation is an important practical research question. This need may arise in cross-device settings, but is particularly relevant in the cross-silo setting, where participants may at the same time also be business competitors.

**Differential privacy:** The discussion of actors and threat models is largely relevant also for the cross-silo FL. However, protecting against different actors might have different priorities. For example, in many practical scenarios, the final trained model would be released only to those who participate in the training, which makes the concerns about "the rest of the world" less important.

### 2.3 Split Learning

In contrast with the previous settings which focus on data partitioning and communication patterns, the key idea behind split learning is to split the execution of a model on a per-layer basis between the clients and the server. This can be done for both training and inference.

In the simplest configuration of split learning, each client computes the forward pass through a deep network up to a specific layer referred to as the cut layer. The outputs at the cut layer, referred to as smashed data, are sent to another entity (either the server or another client), which completes the rest of the computation. The gradients can then be back propagated from its last layer until the cut layer in a similar fashion.

The values communicated can nevertheless, in general, reveal information about the underlying data. How much, and whether this is acceptable, is likely going to be application and configuration specific. Overall, much of the discussion in Section 4 is relevant here as well, and analysis providing formal privacy guarantees specifically for split learning is still an open problem.

### 2.4 Executive Summary

The motivation for federated learning is relevant for a number of related areas of research:

• **Fully decentralized learning** (Section 2.1) removes the need for a central server coordinating the overall computation. Apart from algorithmic challenges, open problems are in practical realization of the idea and in understanding of what form of trusted central authority is needed to set up the task.

• **Cross-silo federated learning** (Section 2.2) admits problems with different kinds of modelling constraints, such as data partitioned by examples and/or features, and faces different set of concerns when formulating formal privacy guarantees or incentive mechanisms for clients to participate.

• **Split learning** (Section 2.3) is an approach to partition the execution of a model between the clients and the server. It can deliver different options for overall communication constraints, but detailed analysis of when the communicated values reveal sensitive information is still missing.

---

### النسخة العربية (الجزء الأول)

## 2 تخفيف افتراضات التعلم الاتحادي الأساسية: التطبيقات على الإعدادات والسيناريوهات الناشئة

في هذا القسم، سنناقش مجالات البحث المتعلقة بالموضوعات التي تمت مناقشتها في القسم السابق. على الرغم من أنها ليست التركيز الرئيسي لبقية الورقة، إلا أن التقدم في هذه المجالات يمكن أن يحفز تصميم الجيل التالي من أنظمة الإنتاج.

### 2.1 التعلم الموزع اللامركزي بالكامل / نظير إلى نظير

في التعلم الاتحادي، ينسق خادم مركزي عملية التدريب ويتلقى مساهمات جميع العملاء. وبالتالي فإن الخادم هو لاعب مركزي يمثل أيضًا نقطة فشل واحدة محتملة. بينما يمكن للشركات أو المنظمات الكبيرة أن تلعب هذا الدور في بعض سيناريوهات التطبيق، قد لا يكون الخادم المركزي الموثوق والقوي متاحًا أو مرغوبًا دائمًا في سيناريوهات التعلم التعاوني [459]. علاوة على ذلك، قد يصبح الخادم حتى عنق زجاجة عندما يكون عدد العملاء كبيرًا جدًا، كما أظهر Lian وآخرون [305] (على الرغم من أنه يمكن التخفيف من ذلك من خلال تصميم نظام دقيق، على سبيل المثال [81]).

الفكرة الأساسية للتعلم اللامركزي بالكامل هي استبدال الاتصال مع الخادم بالاتصال نظير إلى نظير بين العملاء الفرديين. يتم تمثيل طوبولوجيا الاتصال كرسم بياني متصل تكون فيه العقد هي العملاء وتشير الحافة إلى قناة اتصال بين عميلين. عادةً ما يتم اختيار الرسم البياني للشبكة ليكون متفرقًا بحد أقصى صغير للدرجة بحيث تحتاج كل عقدة فقط إلى إرسال/استقبال رسائل من/إلى عدد صغير من النظراء؛ هذا على النقيض من الرسم البياني النجمي لمعمارية خادم-عميل.

في الخوارزميات اللامركزية بالكامل، تتوافق جولة مع كل عميل يقوم بإجراء تحديث محلي وتبادل المعلومات مع جيرانه في الرسم البياني. في سياق تعلم الآلة، عادةً ما يكون التحديث المحلي خطوة تدرج محلية (عشوائية) ويتكون الاتصال في حساب متوسط معاملات النموذج المحلي مع الجيران. لاحظ أنه لم يعد هناك حالة عامة للنموذج كما في التعلم الاتحادي القياسي، ولكن يمكن تصميم العملية بحيث تتقارب جميع النماذج المحلية إلى الحل العام المطلوب، أي أن النماذج الفردية تصل تدريجيًا إلى إجماع.

**الجدول 3:** مقارنة الفروق الرئيسية بين التعلم الاتحادي والتعلم اللامركزي بالكامل.

| الجانب | التعلم الاتحادي | التعلم اللامركزي بالكامل (نظير إلى نظير) |
|--------|-------------------|-------------------------------------------|
| التنسيق | خادم أو خدمة تنسيق مركزية تنظم التدريب، ولكن لا ترى البيانات الخام أبدًا. | لا يوجد تنسيق مركزي. |
| الاتصال واسع النطاق | عادةً طوبولوجيا محور وأشعة، مع المحور يمثل مزود خدمة التنسيق (عادةً بدون بيانات) والأشعة تتصل بالعملاء. | طوبولوجيا نظير إلى نظير، مع رسم بياني للاتصال قد يكون ديناميكيًا. |

#### 2.1.1 التحديات الخوارزمية

يظل عدد كبير من الأسئلة الخوارزمية المهمة مفتوحًا حول موضوع قابلية استخدام المخططات اللامركزية في العالم الحقيقي لتعلم الآلة. بعض الأسئلة مماثلة للحالة الخاصة للتعلم الاتحادي مع خادم مركزي، وتأتي تحديات أخرى كأثر جانبي إضافي لكونها لامركزية بالكامل أو بدون ثقة.

**تأثير طوبولوجيا الشبكة واللاتزامن على SGD اللامركزي:** يجب أن تكون الخوارزميات اللامركزية بالكامل للتعلم قوية لتوافر العملاء المحدود (مع العملاء غير متاحين مؤقتًا، أو يتركون أو ينضمون أثناء التنفيذ) والموثوقية المحدودة للشبكة (مع احتمالية سقوط الرسائل). تتعلق أسئلة البحث المفتوحة الإضافية بتوزيعات البيانات غير المستقلة وغير متطابقة التوزيع، وترددات التحديث، وأنماط الاتصال الفعالة ووقت التقارب العملي.

**SGD اللامركزي مع التحديث المحلي:** التحليل النظري للمخططات التي تؤدي عدة خطوات تحديث محلية قبل جولة الاتصال أكثر تحديًا بكثير من تلك التي تستخدم خطوة SGD واحدة. لا يزال فهم التقارب تحت توزيعات البيانات غير المستقلة وغير متطابقة التوزيع وكيفية تصميم سياسة حساب متوسط النموذج التي تحقق أسرع تقارب مشكلة مفتوحة.

**التخصيص، وآليات الثقة:** بشكل مماثل لإعداد التعلم الاتحادي عبر الأجهزة، مهمة مهمة للسيناريو اللامركزي بالكامل تحت توزيعات البيانات غير المستقلة وغير متطابقة التوزيع المتاحة للعملاء الفرديين هي تصميم خوارزميات لتعلم مجموعات من النماذج المخصصة. أحد التحديات الفريدة الرئيسية في الإعداد اللامركزي يبقى صلابة مثل هذه المخططات للجهات الفاعلة الخبيثة أو المساهمة بالبيانات أو التسميات غير الموثوقة.

**الخصوصية:** تحدٍ مهم في التعلم اللامركزي بالكامل هو منع أي عميل من إعادة بناء البيانات الخاصة لعميل آخر من تحديثاته المشتركة مع الحفاظ على مستوى جيد من الفائدة للنماذج المتعلمة. الخصوصية التفاضلية هي النهج القياسي للتخفيف من مخاطر الخصوصية هذه. لسوء الحظ، غالبًا ما تأتي مثل هذه النهج الخصوصية المحلية بتكلفة كبيرة في الفائدة.

#### 2.1.2 التحديات العملية

البلوكشين هو دفتر أستاذ موزع مشترك بين مستخدمين متباينين، مما يجعل المعاملات الرقمية ممكنة بدون سلطة مركزية. من حيث التعلم الاتحادي، يمكن أن يمكّن استخدام التكنولوجيا من لامركزية الخادم العام باستخدام العقود الذكية لإجراء تجميع النموذج، حيث يمكن أن يكون العملاء المشاركون الذين ينفذون العقود الذكية شركات أو خدمات سحابية مختلفة.

ومع ذلك، على منصات البلوكشين اليوم مثل Ethereum، فإن البيانات على البلوكشين متاحة للجمهور بشكل افتراضي، وهذا يمكن أن يثبط المستخدمين من المشاركة في بروتوكول التعلم الاتحادي اللامركزي. لمعالجة مثل هذه المخاوف، قد يكون من الممكن تعديل تقنيات الحفاظ على الخصوصية الحالية لتناسب سيناريو التعلم الاتحادي اللامركزي، بما في ذلك بروتوكولات التجميع الآمن والخصوصية التفاضلية على مستوى العميل.

### 2.2 التعلم الاتحادي عبر الصوامع

على النقيض من خصائص التعلم الاتحادي عبر الأجهزة، يتيح التعلم الاتحادي عبر الصوامع مرونة أكبر في جوانب معينة من التصميم الشامل، ولكن في نفس الوقت يقدم إعدادًا حيث يمكن أن يكون تحقيق خصائص أخرى أصعب.

يمكن أن يكون إعداد عبر الصوامع ذا صلة حيث يشترك عدد من الشركات أو المنظمات في حافز لتدريب نموذج بناءً على جميع بياناتهم، لكن لا يمكنهم مشاركة بياناتهم مباشرة. قد يكون هذا بسبب القيود المفروضة على السرية أو بسبب القيود القانونية.

**تقسيم البيانات:** في إعداد عبر الأجهزة، يُفترض أن البيانات مقسمة حسب الأمثلة. في إعداد عبر الصوامع، بالإضافة إلى التقسيم حسب الأمثلة، فإن التقسيم حسب الميزات له أهمية عملية. تمت الإشارة إلى هذا الاختلاف أيضًا على أنه التعلم الاتحادي الأفقي والرأسي من قبل Yang وآخرون [490].

**آليات الحوافز:** بالإضافة إلى تطوير تقنيات خوارزمية جديدة للتعلم الاتحادي، فإن تصميم آلية الحوافز للمشاركة الصادقة هو سؤال بحثي عملي مهم. قد تنشأ هذه الحاجة في إعدادات عبر الأجهزة، لكنها ذات صلة خاصة في إعداد عبر الصوامع، حيث قد يكون المشاركون في نفس الوقت أيضًا منافسين تجاريين.

**الخصوصية التفاضلية:** مناقشة الجهات الفاعلة ونماذج التهديد ذات صلة إلى حد كبير أيضًا بالتعلم الاتحادي عبر الصوامع. ومع ذلك، قد يكون للحماية ضد جهات فاعلة مختلفة أولويات مختلفة. على سبيل المثال، في العديد من السيناريوهات العملية، سيتم إصدار النموذج المدرب النهائي فقط لأولئك الذين يشاركون في التدريب، مما يجعل المخاوف بشأن "بقية العالم" أقل أهمية.

### 2.3 التعلم المقسم

على النقيض من الإعدادات السابقة التي تركز على تقسيم البيانات وأنماط الاتصال، فإن الفكرة الأساسية وراء التعلم المقسم هي تقسيم تنفيذ النموذج على أساس كل طبقة بين العملاء والخادم. يمكن القيام بذلك لكل من التدريب والاستدلال.

في أبسط تكوين للتعلم المقسم، يحسب كل عميل التمرير الأمامي عبر شبكة عميقة حتى طبقة معينة يشار إليها باسم طبقة القطع. يتم إرسال المخرجات في طبقة القطع، والمشار إليها باسم البيانات المهروسة، إلى كيان آخر (إما الخادم أو عميل آخر)، الذي يكمل بقية الحساب. يمكن بعد ذلك نشر التدرجات من طبقتها الأخيرة حتى طبقة القطع بطريقة مماثلة.

القيم المنقولة يمكن أن تكشف مع ذلك، بشكل عام، معلومات حول البيانات الأساسية. كم، وما إذا كان هذا مقبولاً، من المحتمل أن يكون خاصًا بالتطبيق والتكوين. بشكل عام، الكثير من المناقشة في القسم 4 ذات صلة هنا أيضًا، والتحليل الذي يوفر ضمانات خصوصية رسمية خصيصًا للتعلم المقسم لا يزال مشكلة مفتوحة.

### 2.4 الملخص التنفيذي

الدافع للتعلم الاتحادي ذو صلة بعدد من مجالات البحث ذات الصلة:

• **التعلم اللامركزي بالكامل** (القسم 2.1) يزيل الحاجة إلى خادم مركزي ينسق الحساب الشامل. بصرف النظر عن التحديات الخوارزمية، المشاكل المفتوحة في التحقيق العملي للفكرة وفي فهم ما هو شكل السلطة المركزية الموثوقة اللازمة لإعداد المهمة.

• **التعلم الاتحادي عبر الصوامع** (القسم 2.2) يقبل مشاكل مع أنواع مختلفة من قيود النمذجة، مثل البيانات المقسمة حسب الأمثلة و/أو الميزات، ويواجه مجموعة مختلفة من المخاوف عند صياغة ضمانات الخصوصية الرسمية أو آليات الحوافز للعملاء للمشاركة.

• **التعلم المقسم** (القسم 2.3) هو نهج لتقسيم تنفيذ النموذج بين العملاء والخادم. يمكن أن يوفر خيارات مختلفة لقيود الاتصال الشاملة، ولكن التحليل التفصيلي لمتى تكشف القيم المنقولة معلومات حساسة لا يزال مفقودًا.

---

### Translation Notes

- **Tables referenced:** Table 3 (comparison between federated and peer-to-peer learning)
- **Key terms introduced:** peer-to-peer (نظير إلى نظير), fully decentralized (لامركزي بالكامل), cross-silo (عبر الصوامع), blockchain (بلوكشين), smart contracts (العقود الذكية), split learning (التعلم المقسم), cut layer (طبقة القطع), smashed data (البيانات المهروسة), horizontal and vertical federated learning (التعلم الاتحادي الأفقي والرأسي)
- **Equations:** None in this section
- **Citations:** Multiple references [459], [305], [81], [337], [490], [80], etc.
- **Special handling:** Technical terms like Ethereum, FATE, ADMM kept partially in English where appropriate

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
