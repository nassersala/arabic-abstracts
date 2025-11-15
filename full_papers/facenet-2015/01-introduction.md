# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.90
**Glossary Terms Used:** embedding (التضمين), face verification (التحقق من الوجوه), face recognition (التعرف على الوجوه), clustering (التجميع), Euclidean space (الفضاء الإقليدي), deep learning (تعلم عميق), convolutional neural network (الشبكة العصبية الالتفافية)

---

### English Version

In this paper we present a unified system for face verification (is this the same person), recognition (who is this person) and clustering (find common people among these faces). Our method is based on learning a Euclidean embedding per image using a deep convolutional network. The network is trained such that the squared L2 distances in the embedding space directly correspond to face similarity: faces of the same person have small distances and faces of distinct persons have large distances.

Once this embedding has been produced, then the aforementioned tasks become straight-forward: face verification simply involves thresholding the distance between the two embeddings; recognition becomes a k-NN classification problem; and clustering can be achieved using off-the-shelf techniques such as k-means or agglomerative clustering.

Previous face recognition approaches based on deep networks use a classification layer trained over a set of known face identities and then take an intermediate bottleneck layer as a representation used to generalize recognition beyond the set of identities used in training. The downsides of this approach are its indirectness and its inefficiency: one has to hope that the bottleneck representation generalizes well to new faces; and the representation size per face is usually very large (1000s of dimensions). Some recent work has explored learning embeddings directly using deep learning, with promising results.

In this paper we push this approach further. We use deep convolutional networks trained using a triplet loss function which encourages a margin between the closest positive pair (images of the same person) and the furthest negative pair (images of different persons). We implement a novel variant of triplet loss which uses semi-hard negative triplet mining within large mini-batches. This allows our system to be trained end-to-end using stochastic gradient descent and requires no complex data preprocessing or offline metric learning.

Our main contributions are:
1. We present a novel system, FaceNet, that learns a direct mapping to a compact Euclidean space where distances correspond to face similarity. The system can be used for face verification, recognition, and clustering.
2. Our method uses a novel online triplet mining method that is both efficient and effective.
3. We achieve state-of-the-art results on multiple face recognition benchmarks including a new record on the LFW dataset of 99.63% and 95.12% on the YouTube Faces DB.

---

### النسخة العربية

في هذا البحث نقدم نظاماً موحداً للتحقق من الوجوه (هل هذا الشخص نفسه)، والتعرف عليها (من هو هذا الشخص)، وتجميعها (إيجاد الأشخاص المشتركين بين هذه الوجوه). تعتمد طريقتنا على تعلم تضمين إقليدي لكل صورة باستخدام شبكة عصبية التفافية عميقة. يتم تدريب الشبكة بحيث تتوافق مسافات L2 المربعة في فضاء التضمين بشكل مباشر مع تشابه الوجوه: وجوه الشخص نفسه لها مسافات صغيرة ووجوه الأشخاص المختلفين لها مسافات كبيرة.

بمجرد إنتاج هذا التضمين، تصبح المهام المذكورة أعلاه مباشرة: التحقق من الوجوه يتضمن ببساطة تحديد عتبة للمسافة بين التضمينين؛ يصبح التعرف مشكلة تصنيف k-NN؛ ويمكن تحقيق التجميع باستخدام تقنيات جاهزة مثل k-means أو التجميع التراكمي.

تستخدم أساليب التعرف على الوجوه السابقة القائمة على الشبكات العميقة طبقة تصنيف مدربة على مجموعة من هويات الوجوه المعروفة ثم تأخذ طبقة اختناق وسيطة كتمثيل يستخدم لتعميم التعرف خارج مجموعة الهويات المستخدمة في التدريب. عيوب هذا النهج هي عدم مباشرته وعدم كفاءته: يجب على المرء أن يأمل أن يعمم تمثيل الاختناق بشكل جيد على الوجوه الجديدة؛ وحجم التمثيل لكل وجه عادة ما يكون كبيراً جداً (آلاف الأبعاد). استكشفت بعض الأعمال الحديثة تعلم التضمينات مباشرة باستخدام التعلم العميق، مع نتائج واعدة.

في هذا البحث ندفع هذا النهج إلى الأمام. نستخدم شبكات عصبية التفافية عميقة مدربة باستخدام دالة خسارة ثلاثية تشجع هامشاً بين أقرب زوج إيجابي (صور الشخص نفسه) وأبعد زوج سلبي (صور أشخاص مختلفين). نطبق نسخة جديدة من الخسارة الثلاثية التي تستخدم التعدين الثلاثي شبه الصعب ضمن دفعات صغيرة كبيرة. يتيح هذا تدريب نظامنا من طرف إلى طرف باستخدام الانحدار التدرجي العشوائي ولا يتطلب معالجة مسبقة معقدة للبيانات أو تعلم مقاييس غير متصل.

مساهماتنا الرئيسية هي:
1. نقدم نظاماً جديداً، فيس نت، يتعلم تعييناً مباشراً إلى فضاء إقليدي مدمج حيث تتوافق المسافات مع تشابه الوجوه. يمكن استخدام النظام للتحقق من الوجوه والتعرف عليها وتجميعها.
2. تستخدم طريقتنا طريقة تعدين ثلاثي على الإنترنت جديدة تتسم بالكفاءة والفعالية معاً.
3. نحقق نتائج متطورة على معايير متعددة للتعرف على الوجوه بما في ذلك رقم قياسي جديد على مجموعة بيانات LFW بنسبة 99.63% و95.12% على قاعدة بيانات يوتيوب للوجوه.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Face verification (التحقق من الوجوه)
  - Face recognition (التعرف على الوجوه)
  - Face clustering (تجميع الوجوه)
  - Triplet loss (الخسارة الثلاثية)
  - Semi-hard negatives (السلبيات شبه الصعبة)
  - Bottleneck layer (طبقة الاختناق)
  - k-NN classification (تصنيف k-NN)
  - End-to-end training (التدريب من طرف إلى طرف)
  - Stochastic gradient descent (الانحدار التدرجي العشوائي)
- **Equations:** L2 distance mentioned (مسافات L2)
- **Citations:** None explicitly mentioned in this section
- **Special handling:**
  - Mathematical notation preserved: k-NN, k-means, L2
  - Dataset names kept in English: LFW, YouTube Faces DB

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.90
