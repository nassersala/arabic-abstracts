# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** federated learning, client, server, model, training, privacy, decentralized, non-IID, aggregation, differential privacy, secure aggregation, cross-device, cross-silo, optimization

---

### English Version

## 1 Introduction

Federated learning (FL) is a machine learning setting where many clients (e.g. mobile devices or whole organizations) collaboratively train a model under the orchestration of a central server (e.g. service provider), while keeping the training data decentralized. It embodies the principles of focused collection and data minimization, and can mitigate many of the systemic privacy risks and costs resulting from traditional, centralized machine learning. This area has received significant interest recently, both from research and applied perspectives. This paper describes the defining characteristics and challenges of the federated learning setting, highlights important practical constraints and considerations, and then enumerates a range of valuable research directions. The goals of this work are to highlight research problems that are of significant theoretical and practical interest, and to encourage research on problems that could have significant real-world impact.

The term federated learning was introduced in 2016 by McMahan et al. [337]: "We term our approach Federated Learning, since the learning task is solved by a loose federation of participating devices (which we refer to as clients) which are coordinated by a central server." An unbalanced and non-IID (identically and independently distributed) data partitioning across a massive number of unreliable devices with limited communication bandwidth was introduced as the defining set of challenges.

Significant related work predates the introduction of the term federated learning. A longstanding goal pursued by many research communities (including cryptography, databases, and machine learning) is to analyze and learn from data distributed among many owners without exposing that data. Cryptographic methods for computing on encrypted data were developed starting in the early 1980s [396, 492], and Agrawal and Srikant [11] and Vaidya et al. [457] are early examples of work that sought to learn from local data using a centralized server while preserving privacy. Conversely, even since the introduction of the term federated learning, we are aware of no single work that directly addresses the full set of FL challenges. Thus, the term federated learning provides a convenient shorthand for a set of characteristics, constraints, and challenges that often co-occur in applied ML problems on decentralized data where privacy is paramount.

This paper originated at the Workshop on Federated Learning and Analytics held June 17–18th, 2019, hosted at Google's Seattle office. During the course of this two-day event, the need for a broad paper surveying the many open challenges in the area of federated learning became clear.

A key property of many of the problems discussed is that they are inherently interdisciplinary — solving them likely requires not just machine learning, but techniques from distributed optimization, cryptography, security, differential privacy, fairness, compressed sensing, systems, information theory, statistics, and more. Many of the hardest problems are at the intersections of these areas, and so we believe collaboration will be essential to ongoing progress. One of the goals of this work is to highlight the ways in which techniques from these fields can potentially be combined, raising both interesting possibilities as well as new challenges.

Since the term federated learning was initially introduced with an emphasis on mobile and edge device applications [337, 334], interest in applying FL to other applications has greatly increased, including some which might involve only a small number of relatively reliable clients, for example multiple organizations collaborating to train a model. We term these two federated learning settings "cross-device" and "cross-silo" respectively. Given these variations, we propose a somewhat broader definition of federated learning:

**Federated learning is a machine learning setting where multiple entities (clients) collaborate in solving a machine learning problem, under the coordination of a central server or service provider. Each client's raw data is stored locally and not exchanged or transferred; instead, focused updates intended for immediate aggregation are used to achieve the learning objective.**

Focused updates are updates narrowly scoped to contain the minimum information necessary for the specific learning task at hand; aggregation is performed as early as possible in the service of data minimization. We note that this definition distinguishes federated learning from fully decentralized (peer-to-peer) learning techniques as discussed in Section 2.1.

Although privacy-preserving data analysis has been studied for more than 50 years, only in the past decade have solutions been widely deployed at scale (e.g. [177, 154]). Cross-device federated learning and federated data analysis are now being applied in consumer digital products. Google makes extensive use of federated learning in the Gboard mobile keyboard [376, 222, 491, 112, 383], as well as in features on Pixel phones [14] and in Android Messages [439]. While Google has pioneered cross-device FL, interest in this setting is now much broader, for example: Apple is using cross-device FL in iOS 13 [25], for applications like the QuickType keyboard and the vocal classifier for "Hey Siri" [26]; doc.ai is developing cross-device FL solutions for medical research [149], and Snips has explored cross-device FL for hotword detection [298].

Cross-silo applications have also been proposed or described in myriad domains including finance risk prediction for reinsurance [476], pharmaceuticals discovery [179], electronic health records mining [184], medical data segmentation [15, 139], and smart manufacturing [354].

The growing demand for federated learning technology has resulted in a number of tools and frameworks becoming available. These include TensorFlow Federated [38], Federated AI Technology Enabler [33], PySyft [399], Leaf [35], PaddleFL [36] and Clara Training Framework [125]; more details in Appendix A. Commercial data platforms incorporating federated learning are in development from established technology companies as well as smaller start-ups.

Table 1 contrasts both cross-device and cross-silo federated learning with traditional single-datacenter distributed learning across a range of axes. These characteristics establish many of the constraints that practical federated learning systems must typically satisfy, and hence serve to both motivate and inform the open challenges in federated learning. They will be discussed at length in the sections that follow.

These two FL variants are called out as representative and important examples, but different FL settings may have different combinations of these characteristics. For the remainder of this paper, we consider the cross-device FL setting unless otherwise noted, though many of the problems apply to other FL settings as well. Section 2 specifically addresses some of the many other variations and applications.

Next, we consider cross-device federated learning in more detail, focusing on practical aspects common to a typical large-scale deployment of the technology; Bonawitz et al. [81] provides even more detail for a particular production system, including a discussion of specific architectural choices and considerations.

### 1.1 The Cross-Device Federated Learning Setting

This section takes an applied perspective, and unlike the previous section, does not attempt to be definitional. Rather, the goal is to describe some of the practical issues in cross-device FL and how they might fit into a broader machine learning development and deployment ecosystem. The hope is to provide useful context and motivation for the open problems that follow, as well as to aid researchers in estimating how straightforward it would be to deploy a particular new approach in a real-world system. We begin by sketching the lifecycle of a model before considering a FL training process.

#### 1.1.1 The Lifecycle of a Model in Federated Learning

The FL process is typically driven by a model engineer developing a model for a particular application. For example, a domain expert in natural language processing may develop a next word prediction model for use in a virtual keyboard. Figure 1 shows the primary components and actors. At a high level, a typical workflow is:

1. **Problem identification:** The model engineer identifies a problem to be solved with FL.

2. **Client instrumentation:** If needed, the clients (e.g. an app running on mobile phones) are instrumented to store locally (with limits on time and quantity) the necessary training data. In many cases, the app already will have stored this data (e.g. a text messaging app must store text messages, a photo management app already stores photos). However, in some cases additional data or metadata might need to be maintained, e.g. user interaction data to provide labels for a supervised learning task.

3. **Simulation prototyping (optional):** The model engineer may prototype model architectures and test learning hyperparameters in an FL simulation using a proxy dataset.

4. **Federated model training:** Multiple federated training tasks are started to train different variations of the model, or use different optimization hyperparameters.

5. **(Federated) model evaluation:** After the tasks have trained sufficiently (typically a few days, see below), the models are analyzed and good candidates selected. Analysis may include metrics computed on standard datasets in the datacenter, or federated evaluation wherein the models are pushed to held-out clients for evaluation on local client data.

6. **Deployment:** Finally, once a good model is selected, it goes through a standard model launch process, including manual quality assurance, live A/B testing (usually by using the new model on some devices and the previous generation model on other devices to compare their in-vivo performance), and a staged rollout (so that poor behavior can be discovered and rolled back before affecting too many users). The specific launch process for a model is set by the owner of the application and is usually independent of how the model is trained. In other words, this step would apply equally to a model trained with federated learning or with a traditional datacenter approach.

One of the primary practical challenges an FL system faces is making the above workflow as straightforward as possible, ideally approaching the ease-of-use achieved by ML systems for centralized training. While much of this paper concerns federated training specifically, there are many other components including federated analytics tasks like model evaluation and debugging. Improving these is the focus of Section 3.4. For now, we consider in more detail the training of a single FL model (Step 4 above).

#### 1.1.2 A Typical Federated Training Process

We now consider a template for FL training that encompasses the Federated Averaging algorithm of McMahan et al. [337] and many others; again, variations are possible, but this gives a common starting point.

A server (service provider) orchestrates the training process, by repeating the following steps until training is stopped (at the discretion of the model engineer who is monitoring the training process):

1. **Client selection:** The server samples from a set of clients meeting eligibility requirements. For example, mobile phones might only check in to the server if they are plugged in, on an unmetered wi-fi connection, and idle, in order to avoid impacting the user of the device.

2. **Broadcast:** The selected clients download the current model weights and a training program (e.g. a TensorFlow graph [2]) from the server.

3. **Client computation:** Each selected device locally computes an update to the model by executing the training program, which might for example run SGD on the local data (as in Federated Averaging).

4. **Aggregation:** The server collects an aggregate of the device updates. For efficiency, stragglers might be dropped at this point once a sufficient number of devices have reported results. This stage is also the integration point for many other techniques which will be discussed later, possibly including: secure aggregation for added privacy, lossy compression of aggregates for communication efficiency, and noise addition and update clipping for differential privacy.

5. **Model update:** The server locally updates the shared model based on the aggregated update computed from the clients that participated in the current round.

**Table 2:** Order-of-magnitude sizes for typical cross-device federated learning applications.

| Metric | Scale |
|--------|-------|
| Total population size | 10⁶–10¹⁰ devices |
| Devices selected for one round of training | 50 – 5000 |
| Total devices that participate in training one model | 10⁵–10⁷ |
| Number of rounds for model convergence | 500 – 10000 |
| Wall-clock training time | 1 – 10 days |

The separation of the client computation, aggregation, and model update phases is not a strict requirement of federated learning, and it indeed excludes certain classes of algorithms, for example asynchronous SGD where each client's update is immediately applied to the model, before any aggregation with updates from other clients. Such asynchronous approaches may simplify some aspects of system design, and also be beneficial from an optimization perspective (though this point can be debated). However, the approach presented above has a substantial advantage in affording a separation of concerns between different lines of research: advances in compression, differential privacy, and secure multi-party computation can be developed for standard primitives like computing sums or means over decentralized updates, and then composed with arbitrary optimization or analytics algorithms, so long as those algorithms are expressed in terms of aggregation primitives.

It is also worth emphasizing that in two respects, the FL training process should not impact the user experience. First, as outlined above, even though model parameters are typically sent to some devices during the broadcast phase of each round of federated training, these models are an ephemeral part of the training process, and not used to make "live" predictions shown to the user. This is crucial, because training ML models is challenging, and a misconfiguration of hyperparameters can produce a model that makes bad predictions. Instead, user-visible use of the model is deferred to a rollout process as detailed above in Step 6 of the model lifecycle. Second, the training itself is intended to be invisible to the user — as described under client selection, training does not slow the device or drain the battery because it only executes when the device is idle and connected to power. However, the limited availability these constraints introduce leads directly to open research challenges which will be discussed subsequently, such as semi-cyclic data availability and the potential for bias in client selection.

### 1.2 Federated Learning Research

The remainder of this paper surveys many open problems that are motivated by the constraints and challenges of real-world federated learning settings, from training models on medical data from a hospital system to training using hundreds of millions of mobile devices. Needless to say, most researchers working on federated learning problems will likely not be deploying production FL systems, nor have access to fleets of millions of real-world devices. This leads to a key distinction between the practical settings that motivate the work and experiments conducted in simulation which provide evidence of the suitability of a given approach to the motivating problem.

This makes FL research somewhat different than other ML fields from an experimental perspective, leading to additional considerations in conducting FL research. In particular, when highlighting open problems, we have attempted, when possible, to also indicate relevant performance metrics which can be measured in simulation, the characteristics of datasets which will make them more representative of real-world performance, etc. The need for simulation also has ramifications for the presentation of FL research. While not intended to be authoritative or absolute, we make the following modest suggestions for presenting FL research that addresses the open problems we describe:

• As shown in Table 1, the FL setting can encompass a wide range of problems. Compared to fields where the setting and goals are well-established, it is important to precisely describe the details of the particular FL setting of interest, particularly when the proposed approach makes assumptions that may not be appropriate in all settings (e.g. stateful clients that participate in all rounds).

• Of course, details of any simulations should be presented in order to make the research reproducible. But it is also important to explain which aspects of the real-world setting the simulation is designed to capture (and which it is not), in order to effectively make the case that success on the simulated problem implies useful progress on the real-world objective. We hope that the guidance in this paper will help with this.

• Privacy and communication efficiency are always first-order concerns in FL, even if the experiments are simulations running on a single machine using public data. More so than with other types of ML, for any proposed approach it is important to be unambiguous about where computation happens as well as what is communicated.

Software libraries for federated learning simulation as well as standard datasets can help ease the challenges of conducting effective FL research; Appendix A summarizes some of the currently available options. Developing standard evaluation metrics and establishing standard benchmark datasets for different federated learning settings (cross-device and cross-silo) remain highly important directions for ongoing work.

### 1.3 Organization

Section 2 builds on the ideas in Table 1, exploring other FL settings and problems beyond the original focus on cross-device settings. Section 3 then turns to core questions around improving the efficiency and effectiveness of federated learning. Section 4 undertakes a careful consideration of threat models and considers a range of technologies toward the goal of achieving rigorous privacy protections. As with all machine learning systems, in federated learning applications there may be incentives to manipulate the models being trained, and failures of various kinds are inevitable; these challenges are discussed in Section 5. Finally, we address the important challenges of providing fair and unbiased models in Section 6.

---

### النسخة العربية

## 1 المقدمة

التعلم الاتحادي (FL) هو إعداد لتعلم الآلة حيث يقوم العديد من العملاء (مثل الأجهزة المحمولة أو المنظمات بأكملها) بتدريب نموذج بشكل تعاوني تحت تنسيق خادم مركزي (مثل مزود الخدمة)، مع الحفاظ على بيانات التدريب لامركزية. يجسد التعلم الاتحادي مبادئ جمع البيانات المركز وتقليلها، ويمكن أن يخفف من العديد من مخاطر الخصوصية النظامية والتكاليف الناتجة عن تعلم الآلة المركزي التقليدي. حظيت هذه المنطقة باهتمام كبير مؤخرًا، من منظوري البحث والتطبيق العملي. تصف هذه الورقة الخصائص والتحديات المميزة لإعداد التعلم الاتحادي، وتسلط الضوء على القيود والاعتبارات العملية المهمة، ثم تعدد مجموعة من الاتجاهات البحثية القيمة. أهداف هذا العمل هي تسليط الضوء على المشاكل البحثية ذات الأهمية النظرية والعملية الكبيرة، وتشجيع البحث في المشاكل التي يمكن أن يكون لها تأثير كبير في العالم الحقيقي.

تم تقديم مصطلح التعلم الاتحادي في عام 2016 من قبل McMahan وآخرون [337]: "نطلق على نهجنا اسم التعلم الاتحادي، حيث يتم حل مهمة التعلم بواسطة اتحاد فضفاض من الأجهزة المشاركة (التي نشير إليها كعملاء) والتي يتم تنسيقها بواسطة خادم مركزي". تم تقديم تقسيم البيانات غير المتوازن وغير المستقل وغير متطابق التوزيع (non-IID) عبر عدد هائل من الأجهزة غير الموثوقة ذات عرض النطاق الترددي المحدود للاتصالات كمجموعة التحديات المميزة.

يسبق العمل ذو الصلة الكبير تقديم مصطلح التعلم الاتحادي. الهدف طويل الأمد الذي تسعى إليه العديد من مجتمعات البحث (بما في ذلك التشفير وقواعد البيانات وتعلم الآلة) هو تحليل البيانات الموزعة بين العديد من المالكين والتعلم منها دون الكشف عن تلك البيانات. تم تطوير الأساليب التشفيرية للحساب على البيانات المشفرة بدءًا من أوائل الثمانينيات [396، 492]، و Agrawal و Srikant [11] و Vaidya وآخرون [457] هي أمثلة مبكرة على الأعمال التي سعت إلى التعلم من البيانات المحلية باستخدام خادم مركزي مع الحفاظ على الخصوصية. على العكس، حتى منذ تقديم مصطلح التعلم الاتحادي، لسنا على علم بأي عمل واحد يعالج بشكل مباشر المجموعة الكاملة من تحديات التعلم الاتحادي. وبالتالي، فإن مصطلح التعلم الاتحادي يوفر اختصارًا مناسبًا لمجموعة من الخصائص والقيود والتحديات التي غالبًا ما تحدث معًا في مشاكل تعلم الآلة التطبيقية على البيانات اللامركزية حيث تكون الخصوصية هي الأولوية.

نشأت هذه الورقة في ورشة العمل حول التعلم الاتحادي والتحليلات التي عُقدت في 17-18 يونيو 2019، واستضافتها Google في مكتبها في سياتل. خلال هذا الحدث الذي استمر يومين، أصبحت الحاجة إلى ورقة واسعة تستطلع العديد من التحديات المفتوحة في مجال التعلم الاتحادي واضحة.

خاصية رئيسية للعديد من المشاكل التي نوقشت هي أنها متعددة التخصصات بطبيعتها - حلها يتطلب على الأرجح ليس فقط تعلم الآلة، ولكن تقنيات من التحسين الموزع والتشفير والأمن والخصوصية التفاضلية والعدالة والاستشعار المضغوط والأنظمة ونظرية المعلومات والإحصاء وأكثر من ذلك. العديد من أصعب المشاكل موجودة عند تقاطعات هذه المجالات، ولذلك نعتقد أن التعاون سيكون ضروريًا للتقدم المستمر. أحد أهداف هذا العمل هو تسليط الضوء على الطرق التي يمكن من خلالها دمج التقنيات من هذه المجالات، مما يثير إمكانيات مثيرة للاهتمام بالإضافة إلى تحديات جديدة.

نظرًا لأن مصطلح التعلم الاتحادي تم تقديمه في البداية مع التركيز على تطبيقات الأجهزة المحمولة والطرفية [337، 334]، فقد زاد الاهتمام بتطبيق التعلم الاتحادي على تطبيقات أخرى بشكل كبير، بما في ذلك بعض التطبيقات التي قد تتضمن عددًا صغيرًا فقط من العملاء الموثوقين نسبيًا، على سبيل المثال عدة منظمات تتعاون لتدريب نموذج. نطلق على إعدادي التعلم الاتحادي هذين اسم "عبر الأجهزة" و "عبر الصوامع" على التوالي. بالنظر إلى هذه الاختلافات، نقترح تعريفًا أوسع إلى حد ما للتعلم الاتحادي:

**التعلم الاتحادي هو إعداد لتعلم الآلة حيث تتعاون كيانات متعددة (عملاء) في حل مشكلة تعلم آلة، تحت تنسيق خادم مركزي أو مزود خدمة. يتم تخزين البيانات الخام لكل عميل محليًا ولا يتم تبادلها أو نقلها؛ بدلاً من ذلك، يتم استخدام التحديثات المركزة المخصصة للتجميع الفوري لتحقيق هدف التعلم.**

التحديثات المركزة هي تحديثات محددة النطاق بشكل ضيق لتحتوي على الحد الأدنى من المعلومات الضرورية لمهمة التعلم المحددة؛ يتم إجراء التجميع في أقرب وقت ممكن في خدمة تقليل البيانات. نلاحظ أن هذا التعريف يميز التعلم الاتحادي عن تقنيات التعلم اللامركزية بالكامل (نظير إلى نظير) كما هو موضح في القسم 2.1.

على الرغم من أن تحليل البيانات الذي يحافظ على الخصوصية قد تمت دراسته لأكثر من 50 عامًا، إلا أنه في العقد الماضي فقط تم نشر الحلول على نطاق واسع (على سبيل المثال [177، 154]). يتم الآن تطبيق التعلم الاتحادي عبر الأجهزة وتحليل البيانات الاتحادية في المنتجات الرقمية الاستهلاكية. تستخدم Google بشكل مكثف التعلم الاتحادي في لوحة مفاتيح Gboard المحمولة [376، 222، 491، 112، 383]، بالإضافة إلى الميزات في هواتف Pixel [14] وفي Android Messages [439]. بينما كانت Google رائدة في التعلم الاتحادي عبر الأجهزة، فإن الاهتمام بهذا الإعداد الآن أوسع بكثير، على سبيل المثال: تستخدم Apple التعلم الاتحادي عبر الأجهزة في iOS 13 [25]، لتطبيقات مثل لوحة مفاتيح QuickType ومصنف الصوت لـ "Hey Siri" [26]؛ تطور doc.ai حلول التعلم الاتحادي عبر الأجهزة للبحث الطبي [149]، واستكشفت Snips التعلم الاتحادي عبر الأجهزة لاكتشاف الكلمات الساخنة [298].

تم اقتراح أو وصف تطبيقات عبر الصوامع في مجالات لا حصر لها بما في ذلك التنبؤ بمخاطر التمويل لإعادة التأمين [476]، واكتشاف الأدوية [179]، وتعدين السجلات الصحية الإلكترونية [184]، وتقسيم البيانات الطبية [15، 139]، والتصنيع الذكي [354].

أدى الطلب المتزايد على تكنولوجيا التعلم الاتحادي إلى توفر عدد من الأدوات والأطر. تشمل هذه TensorFlow Federated [38]، و Federated AI Technology Enabler [33]، و PySyft [399]، و Leaf [35]، و PaddleFL [36] و Clara Training Framework [125]؛ المزيد من التفاصيل في الملحق أ. منصات البيانات التجارية التي تدمج التعلم الاتحادي قيد التطوير من شركات التكنولوجيا الراسخة بالإضافة إلى الشركات الناشئة الأصغر.

يقارن الجدول 1 كلاً من التعلم الاتحادي عبر الأجهزة وعبر الصوامع مع التعلم الموزع التقليدي في مركز بيانات واحد عبر مجموعة من المحاور. تحدد هذه الخصائص العديد من القيود التي يجب أن تلبيها أنظمة التعلم الاتحادي العملية عادةً، وبالتالي تخدم كلاً من تحفيز وإعلام التحديات المفتوحة في التعلم الاتحادي. سيتم مناقشتها بالتفصيل في الأقسام التالية.

يتم استدعاء هذين المتغيرين من التعلم الاتحادي كأمثلة تمثيلية ومهمة، ولكن قد يكون لإعدادات التعلم الاتحادي المختلفة مجموعات مختلفة من هذه الخصائص. لبقية هذه الورقة، نعتبر إعداد التعلم الاتحادي عبر الأجهزة ما لم يُذكر خلاف ذلك، على الرغم من أن العديد من المشاكل تنطبق على إعدادات التعلم الاتحادي الأخرى أيضًا. يتناول القسم 2 على وجه التحديد بعض الاختلافات والتطبيقات الأخرى العديدة.

بعد ذلك، نعتبر التعلم الاتحادي عبر الأجهزة بمزيد من التفصيل، مع التركيز على الجوانب العملية الشائعة في النشر الواسع النطاق النموذجي للتكنولوجيا؛ يوفر Bonawitz وآخرون [81] مزيدًا من التفاصيل لنظام إنتاج معين، بما في ذلك مناقشة الخيارات والاعتبارات المعمارية المحددة.

### 1.1 إعداد التعلم الاتحادي عبر الأجهزة

يأخذ هذا القسم منظورًا تطبيقيًا، وعلى عكس القسم السابق، لا يحاول أن يكون تعريفيًا. بدلاً من ذلك، الهدف هو وصف بعض القضايا العملية في التعلم الاتحادي عبر الأجهزة وكيف يمكن أن تتناسب مع نظام بيئي أوسع لتطوير ونشر تعلم الآلة. الأمل هو توفير سياق وتحفيز مفيدين للمشاكل المفتوحة التي تلي، بالإضافة إلى مساعدة الباحثين في تقدير مدى سهولة نشر نهج جديد معين في نظام حقيقي. نبدأ برسم دورة حياة النموذج قبل النظر في عملية تدريب التعلم الاتحادي.

#### 1.1.1 دورة حياة النموذج في التعلم الاتحادي

تُدفع عملية التعلم الاتحادي عادةً بواسطة مهندس نماذج يطور نموذجًا لتطبيق معين. على سبيل المثال، قد يطور خبير مجال في معالجة اللغة الطبيعية نموذج تنبؤ بالكلمة التالية للاستخدام في لوحة مفاتيح افتراضية. يوضح الشكل 1 المكونات والجهات الفاعلة الأساسية. على مستوى عالٍ، سير العمل النموذجي هو:

1. **تحديد المشكلة:** يحدد مهندس النموذج مشكلة يجب حلها بالتعلم الاتحادي.

2. **أتمتة العملاء:** إذا لزم الأمر، يتم أتمتة العملاء (على سبيل المثال تطبيق يعمل على الهواتف المحمولة) لتخزين بيانات التدريب الضرورية محليًا (مع حدود على الوقت والكمية). في كثير من الحالات، سيكون التطبيق قد خزن بالفعل هذه البيانات (على سبيل المثال يجب على تطبيق المراسلة النصية تخزين الرسائل النصية، تطبيق إدارة الصور يخزن بالفعل الصور). ومع ذلك، في بعض الحالات قد يلزم الحفاظ على بيانات أو بيانات وصفية إضافية، على سبيل المثال بيانات تفاعل المستخدم لتوفير تسميات لمهمة تعلم خاضع للإشراف.

3. **النموذج الأولي للمحاكاة (اختياري):** قد يقوم مهندس النموذج بإنشاء نماذج أولية لمعماريات النموذج واختبار معاملات التعلم الفائقة في محاكاة التعلم الاتحادي باستخدام مجموعة بيانات بديلة.

4. **تدريب النموذج الاتحادي:** يتم بدء مهام تدريب اتحادية متعددة لتدريب أشكال مختلفة من النموذج، أو استخدام معاملات تحسين فائقة مختلفة.

5. **تقييم النموذج (الاتحادي):** بعد أن تم تدريب المهام بشكل كافٍ (عادةً بضعة أيام، انظر أدناه)، يتم تحليل النماذج واختيار المرشحين الجيدين. قد يشمل التحليل مقاييس محسوبة على مجموعات بيانات قياسية في مركز البيانات، أو التقييم الاتحادي حيث يتم دفع النماذج إلى عملاء محتفظ بهم للتقييم على بيانات العميل المحلية.

6. **النشر:** أخيرًا، بمجرد اختيار نموذج جيد، يمر عبر عملية إطلاق نموذج قياسية، بما في ذلك ضمان الجودة اليدوي، واختبار A/B المباشر (عادةً باستخدام النموذج الجديد على بعض الأجهزة ونموذج الجيل السابق على أجهزة أخرى لمقارنة أدائها في الحياة الواقعية)، والنشر المرحلي (بحيث يمكن اكتشاف السلوك السيئ والتراجع عنه قبل التأثير على عدد كبير جدًا من المستخدمين). يتم تعيين عملية الإطلاق المحددة للنموذج من قبل مالك التطبيق وعادةً ما تكون مستقلة عن كيفية تدريب النموذج. بعبارة أخرى، ستنطبق هذه الخطوة بالتساوي على نموذج مدرب بالتعلم الاتحادي أو بنهج مركز بيانات تقليدي.

أحد التحديات العملية الأساسية التي يواجهها نظام التعلم الاتحادي هو جعل سير العمل أعلاه مباشرًا قدر الإمكان، من الناحية المثالية الاقتراب من سهولة الاستخدام التي تحققها أنظمة تعلم الآلة للتدريب المركزي. بينما يتعلق الكثير من هذه الورقة بالتدريب الاتحادي على وجه التحديد، هناك العديد من المكونات الأخرى بما في ذلك مهام التحليلات الاتحادية مثل تقييم النموذج وتصحيح الأخطاء. تحسين هذه هو محور القسم 3.4. في الوقت الحالي، نعتبر بمزيد من التفصيل تدريب نموذج اتحادي واحد (الخطوة 4 أعلاه).

#### 1.1.2 عملية التدريب الاتحادي النموذجية

نعتبر الآن قالبًا لتدريب التعلم الاتحادي يشمل خوارزمية Federated Averaging لـ McMahan وآخرون [337] والعديد من الخوارزميات الأخرى؛ مرة أخرى، الاختلافات ممكنة، لكن هذا يعطي نقطة انطلاق مشتركة.

يقوم خادم (مزود الخدمة) بتنسيق عملية التدريب، عن طريق تكرار الخطوات التالية حتى يتوقف التدريب (حسب تقدير مهندس النموذج الذي يراقب عملية التدريب):

1. **اختيار العميل:** يقوم الخادم بأخذ عينات من مجموعة من العملاء الذين يستوفون متطلبات الأهلية. على سبيل المثال، قد تسجل الهواتف المحمولة فقط مع الخادم إذا كانت متصلة بالكهرباء، وعلى اتصال wi-fi غير محدود، وخاملة، من أجل تجنب التأثير على مستخدم الجهاز.

2. **البث:** يقوم العملاء المحددون بتنزيل أوزان النموذج الحالية وبرنامج تدريب (على سبيل المثال رسم بياني TensorFlow [2]) من الخادم.

3. **حساب العميل:** يقوم كل جهاز محدد محليًا بحساب تحديث للنموذج عن طريق تنفيذ برنامج التدريب، والذي قد يقوم على سبيل المثال بتشغيل SGD على البيانات المحلية (كما في Federated Averaging).

4. **التجميع:** يجمع الخادم مجموعًا من تحديثات الأجهزة. من أجل الكفاءة، قد يتم إسقاط الأجهزة المتأخرة في هذه المرحلة بمجرد أن يبلغ عدد كافٍ من الأجهزة عن النتائج. تعتبر هذه المرحلة أيضًا نقطة التكامل للعديد من التقنيات الأخرى التي سيتم مناقشتها لاحقًا، بما في ذلك ربما: التجميع الآمن لمزيد من الخصوصية، وضغط المجاميع الفاقد لكفاءة الاتصال، وإضافة الضوضاء وقص التحديث للخصوصية التفاضلية.

5. **تحديث النموذج:** يقوم الخادم محليًا بتحديث النموذج المشترك بناءً على التحديث المجمع المحسوب من العملاء الذين شاركوا في الجولة الحالية.

**الجدول 2:** أحجام الرتبة العظمى لتطبيقات التعلم الاتحادي عبر الأجهزة النموذجية.

| المقياس | النطاق |
|--------|-------|
| حجم السكان الإجمالي | 10⁶–10¹⁰ جهاز |
| الأجهزة المحددة لجولة تدريب واحدة | 50 – 5000 |
| إجمالي الأجهزة التي تشارك في تدريب نموذج واحد | 10⁵–10⁷ |
| عدد الجولات لتقارب النموذج | 500 – 10000 |
| وقت التدريب بالساعة الحقيقية | 1 – 10 أيام |

إن فصل مراحل حساب العميل والتجميع وتحديث النموذج ليس متطلبًا صارمًا للتعلم الاتحادي، وهو في الواقع يستبعد فئات معينة من الخوارزميات، على سبيل المثال SGD غير المتزامن حيث يتم تطبيق تحديث كل عميل على الفور على النموذج، قبل أي تجميع مع تحديثات من عملاء آخرين. قد تبسط مثل هذه الأساليب غير المتزامنة بعض جوانب تصميم النظام، وتكون مفيدة أيضًا من منظور التحسين (على الرغم من أن هذه النقطة يمكن مناقشتها). ومع ذلك، فإن النهج المقدم أعلاه له ميزة كبيرة في توفير فصل المخاوف بين خطوط البحث المختلفة: يمكن تطوير التقدم في الضغط والخصوصية التفاضلية والحساب الآمن متعدد الأطراف لبدائيات قياسية مثل حساب المجاميع أو المتوسطات على التحديثات اللامركزية، ثم تركيبها مع خوارزميات التحسين أو التحليلات التعسفية، طالما أن هذه الخوارزميات معبر عنها من حيث بدائيات التجميع.

من المفيد أيضًا التأكيد على أنه من ناحيتين، يجب ألا تؤثر عملية التدريب الاتحادي على تجربة المستخدم. أولاً، كما هو موضح أعلاه، على الرغم من أن معاملات النموذج يتم إرسالها عادةً إلى بعض الأجهزة خلال مرحلة البث من كل جولة من التدريب الاتحادي، إلا أن هذه النماذج جزء مؤقت من عملية التدريب، ولا تستخدم لإجراء تنبؤات "حية" تظهر للمستخدم. هذا أمر بالغ الأهمية، لأن تدريب نماذج تعلم الآلة أمر صعب، ويمكن أن يؤدي سوء تكوين المعاملات الفائقة إلى إنتاج نموذج يقوم بتنبؤات سيئة. بدلاً من ذلك، يتم تأجيل الاستخدام المرئي للمستخدم للنموذج إلى عملية نشر كما هو مفصل أعلاه في الخطوة 6 من دورة حياة النموذج. ثانيًا، يُقصد من التدريب نفسه أن يكون غير مرئي للمستخدم - كما هو موضح تحت اختيار العميل، لا يبطئ التدريب الجهاز أو يستنزف البطارية لأنه يتم تنفيذه فقط عندما يكون الجهاز خاملاً ومتصلاً بالطاقة. ومع ذلك، فإن التوافر المحدود الذي تقدمه هذه القيود يؤدي مباشرة إلى تحديات بحثية مفتوحة سيتم مناقشتها لاحقًا، مثل توفر البيانات شبه الدوري وإمكانية التحيز في اختيار العميل.

### 1.2 بحث التعلم الاتحادي

تستطلع بقية هذه الورقة العديد من المشاكل المفتوحة التي تحفزها القيود والتحديات لإعدادات التعلم الاتحادي في العالم الحقيقي، من تدريب النماذج على البيانات الطبية من نظام مستشفى إلى التدريب باستخدام مئات الملايين من الأجهزة المحمولة. غني عن القول، من المحتمل ألا يقوم معظم الباحثين الذين يعملون على مشاكل التعلم الاتحادي بنشر أنظمة إنتاج التعلم الاتحادي، ولن يكون لديهم إمكانية الوصول إلى أساطيل من ملايين الأجهزة الحقيقية. يؤدي هذا إلى تمييز رئيسي بين الإعدادات العملية التي تحفز العمل والتجارب التي تُجرى في المحاكاة والتي توفر دليلاً على ملاءمة نهج معين للمشكلة المحفزة.

يجعل هذا بحث التعلم الاتحادي مختلفًا إلى حد ما عن مجالات تعلم الآلة الأخرى من منظور تجريبي، مما يؤدي إلى اعتبارات إضافية في إجراء بحث التعلم الاتحادي. على وجه الخصوص، عند تسليط الضوء على المشاكل المفتوحة، حاولنا، عندما يكون ذلك ممكنًا، أيضًا الإشارة إلى مقاييس الأداء ذات الصلة التي يمكن قياسها في المحاكاة، وخصائص مجموعات البيانات التي ستجعلها أكثر تمثيلاً للأداء في العالم الحقيقي، وما إلى ذلك. الحاجة إلى المحاكاة لها أيضًا تأثيرات على عرض بحث التعلم الاتحادي. بينما لا يُقصد أن تكون موثوقة أو مطلقة، فإننا نقدم الاقتراحات المتواضعة التالية لعرض بحث التعلم الاتحادي الذي يعالج المشاكل المفتوحة التي نصفها:

• كما هو موضح في الجدول 1، يمكن أن يشمل إعداد التعلم الاتحادي مجموعة واسعة من المشاكل. بالمقارنة مع المجالات التي يتم فيها تحديد الإعداد والأهداف بشكل جيد، من المهم وصف تفاصيل إعداد التعلم الاتحادي المعين محل الاهتمام بدقة، خاصة عندما يقوم النهج المقترح بافتراضات قد لا تكون مناسبة في جميع الإعدادات (على سبيل المثال عملاء ذوي حالة يشاركون في جميع الجولات).

• بالطبع، يجب تقديم تفاصيل أي محاكاة من أجل جعل البحث قابلاً للتكرار. لكن من المهم أيضًا شرح الجوانب من الإعداد الحقيقي التي صُممت المحاكاة لالتقاطها (وأيها لا)، من أجل إثبات الحالة بشكل فعال أن النجاح في المشكلة المحاكاة يعني تقدمًا مفيدًا نحو الهدف الحقيقي. نأمل أن تساعد التوجيهات في هذه الورقة في ذلك.

• الخصوصية وكفاءة الاتصال هي دائمًا مخاوف من الدرجة الأولى في التعلم الاتحادي، حتى لو كانت التجارب عبارة عن محاكاة تعمل على جهاز واحد باستخدام بيانات عامة. أكثر مما هو عليه مع أنواع أخرى من تعلم الآلة، بالنسبة لأي نهج مقترح من المهم أن تكون واضحًا بشأن مكان حدوث الحساب وكذلك ما يتم إرساله.

يمكن أن تساعد مكتبات البرامج لمحاكاة التعلم الاتحادي بالإضافة إلى مجموعات البيانات القياسية في تخفيف تحديات إجراء بحث فعال في التعلم الاتحادي؛ يلخص الملحق أ بعض الخيارات المتاحة حاليًا. لا يزال تطوير مقاييس التقييم القياسية وإنشاء مجموعات بيانات معيارية قياسية لإعدادات التعلم الاتحادي المختلفة (عبر الأجهزة وعبر الصوامع) اتجاهات مهمة للغاية للعمل المستمر.

### 1.3 التنظيم

يبني القسم 2 على الأفكار في الجدول 1، مستكشفًا إعدادات ومشاكل التعلم الاتحادي الأخرى بخلاف التركيز الأصلي على الإعدادات عبر الأجهزة. يتجه القسم 3 بعد ذلك إلى الأسئلة الأساسية حول تحسين كفاءة وفعالية التعلم الاتحادي. يتولى القسم 4 دراسة دقيقة لنماذج التهديد ويأخذ في الاعتبار مجموعة من التقنيات نحو هدف تحقيق حماية صارمة للخصوصية. كما هو الحال مع جميع أنظمة تعلم الآلة، في تطبيقات التعلم الاتحادي قد تكون هناك حوافز للتلاعب بالنماذج التي يتم تدريبها، والفشل من أنواع مختلفة أمر لا مفر منه؛ تتم مناقشة هذه التحديات في القسم 5. أخيرًا، نتناول التحديات المهمة لتوفير نماذج عادلة وغير منحازة في القسم 6.

---

### Translation Notes

- **Figures referenced:** Figure 1 (The lifecycle of an FL-trained model), Table 1 (comparison table), Table 2 (order-of-magnitude sizes)
- **Key terms introduced:** federated learning (تعلم اتحادي), cross-device (عبر الأجهزة), cross-silo (عبر الصوامع), non-IID (غير مستقل وغير متطابق التوزيع), focused updates (التحديثات المركزة), aggregation (تجميع), secure aggregation (التجميع الآمن), stragglers (الأجهزة المتأخرة), federated analytics (التحليلات الاتحادية)
- **Equations:** None in this section
- **Citations:** Multiple references [337], [11], [457], [396], [492], [81], etc.
- **Special handling:** Technical framework names kept in English (TensorFlow Federated, PySyft, etc.), Company names kept in English (Google, Apple, etc.)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89
