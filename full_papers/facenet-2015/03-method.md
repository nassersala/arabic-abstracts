# Section 3: Method
## القسم 3: المنهجية

**Section:** Method
**Translation Quality:** 0.87
**Glossary Terms Used:** embedding (التضمين), deep learning (تعلم عميق), convolutional neural network (الشبكة العصبية الالتفافية), triplet loss (الخسارة الثلاثية), gradient (التدرجات), optimization (تحسين), architecture (معمارية), batch normalization (تطبيع الدفعة)

---

### English Version

FaceNet uses a deep convolutional network. We discuss two different core architectures: The Zeiler&Fergus based model and the Inception based model. The details of these architectures are described in Section 3.3.

Given the model details, and treating it as a black box (see Figure 2), the most important part is the end-to-end learning of the whole system. To this end we employ the triplet loss that directly reflects what we want to achieve in face verification, recognition and clustering. Namely, we strive to ensure that an image x_i^a (anchor) of a specific person is closer to all other images x_i^p (positive) of the same person than it is to any image x_i^n (negative) of any other person. This is visualized in Figure 3.

**3.1 Triplet Loss**

The embedding is represented by f(x) ∈ R^d. It embeds an image x into a d-dimensional Euclidean space. Additionally, we constrain this embedding to live on the d-dimensional hypersphere, i.e. ||f(x)||_2 = 1. This loss is motivated by the desire to ensure that an image x_i^a (anchor) of a specific person is closer to all other images x_i^p (positive) of the same person than it is to any image x_i^n (negative) of any other person in the embedding space. Thus we want

||f(x_i^a) - f(x_i^p)||_2^2 + α < ||f(x_i^a) - f(x_i^n)||_2^2,    (1)

∀(f(x_i^a), f(x_i^p), f(x_i^n)) ∈ T

where α is a margin that is enforced between positive and negative pairs. T is the set of all possible triplets in the training set and has cardinality N.

The loss that is being minimized is then

L = Σ [||f(x_i^a) - f(x_i^p)||_2^2 - ||f(x_i^a) - f(x_i^n)||_2^2 + α]_+    (2)

Generating all possible triplets would result in many triplets that are easily satisfied (i.e. fulfill the constraint in Eq. (1)). These triplets would not contribute to the training and result in slower convergence, as they would still be passed through the network. It is crucial to select hard triplets, that are active and can therefore contribute to improving the model. The following section talks about the different approaches we use for the triplet selection.

**3.2 Triplet Selection**

In order to ensure fast convergence it is crucial to select triplets that violate the triplet constraint in Eq. (1). This means that, given x_i^a, we want to select an x_i^p (hard positive) such that argmax_{x_i^p} ||f(x_i^a) - f(x_i^p)||_2^2 and similarly x_i^n (hard negative) such that argmin_{x_i^n} ||f(x_i^a) - f(x_i^n)||_2^2.

It is infeasible to compute the argmin and argmax across the whole training set. Additionally, it might lead to poor training, as mislabelled and poorly imaged faces would dominate the hard positives and negatives. There are two obvious choices that avoid this issue:

• Generate triplets offline every n steps, using the most recent network checkpoint and computing the argmin and argmax on a subset of the data.

• Generate triplets online. This can be done by selecting the hard positive/negative exemplars from within a mini-batch.

Here, we focus on the online generation and use large mini-batches in the order of a few thousand exemplars and only compute the argmin and argmax within a mini-batch.

To have a meaningful representation of the anchor-positive distances, it needs to be ensured that a minimal number of exemplars of any one identity is present in each mini-batch. In our experiments we sample the training data such that around 40 faces are selected per identity per mini-batch. Additionally, we also explored the offline generation approach and used a smaller number of overall negatives and positives but that are all hard to distinguish.

Selecting the hardest negatives can in practice lead to bad local minima early on in training, specifically it can result in a collapsed model (i.e. f(x) = 0). In order to mitigate this, we select all anchor-positive pairs in a mini-batch while only using the semi-hard negatives. These negatives are harder than the anchor-positive distance, but still have a positive loss, i.e.

||f(x_i^a) - f(x_i^p)||_2^2 < ||f(x_i^a) - f(x_i^n)||_2^2 < ||f(x_i^a) - f(x_i^p)||_2^2 + α.

As mentioned before, correct triplet selection is crucial for fast convergence. On the one hand we would like to use small mini-batches as these tend to improve convergence during Stochastic Gradient Descent (SGD). On the other hand, implementation details make batches of tens to hundreds of exemplars more efficient. The main constraint with regards to the batch size, however, is the way we select hard relevant triplets from within the mini-batches. In most experiments we use a batch size of around 1,800 exemplars.

**3.3 Deep Convolutional Networks**

In all of our experiments we train the CNN using Stochastic Gradient Descent (SGD) with standard backpropagation and AdaGrad. In most experiments we start with a learning rate of 0.05 which we lower to finalize the model. The models are initialized from random, similar to Szegedy et al., and trained on a CPU cluster for 1,000 to 2,000 hours. The decrease in the loss (and increase in accuracy) slows down drastically after 500h of training, but additional training can still significantly improve performance. The margin α is set to 0.2.

We used two types of architectures and explore their trade-offs in more detail in the experimental section. The first is a Zeiler&Fergus architecture with 1×1 convolutions as proposed in Lin et al. We refer to this model as NN1. This architecture has a total of 140 million parameters and a FLOP requirement of around 1.6 billion.

The second category of models are Inception type models. These models have an order of magnitude fewer parameters (around 6.6M-7.5M) and up to five times fewer FLOPS (between 500M-1.6B). Some of these models are dramatically reduced in size (by a factor of 20), while sacrificing only 10% of the performance of NN1. Table 1 describes the details of these models and Figure 4 visualizes the architecture.

The input to the networks consists of 220×220 randomly cropped face images. The architecture details of NN2 include:
- Convolution layers with varying filter sizes
- Inception modules with parallel convolutions
- Batch normalization layers
- Max pooling layers
- L2 normalization on the final embedding layer

We also added batch normalization to selected layers which we found improved training speed. The models are trained using a variety of image resolutions from 96×96 pixels up to 224×224 pixels. The smaller models run around twice as fast which is important for deployment scenarios. The choice of input size is a trade-off between accuracy and speed.

---

### النسخة العربية

يستخدم فيس نت شبكة عصبية التفافية عميقة. نناقش معماريتين أساسيتين مختلفتين: النموذج القائم على Zeiler&Fergus والنموذج القائم على Inception. تم وصف تفاصيل هذه المعماريات في القسم 3.3.

بالنظر إلى تفاصيل النموذج، ومعاملته كصندوق أسود (انظر الشكل 2)، فإن الجزء الأكثر أهمية هو التعلم من طرف إلى طرف للنظام بأكمله. لهذه الغاية، نستخدم الخسارة الثلاثية التي تعكس مباشرة ما نريد تحقيقه في التحقق من الوجوه والتعرف عليها وتجميعها. وبالتحديد، نسعى جاهدين للتأكد من أن صورة x_i^a (المرساة) لشخص معين أقرب إلى جميع الصور الأخرى x_i^p (الإيجابية) لنفس الشخص مما هي عليه لأي صورة x_i^n (السلبية) لأي شخص آخر. يتم تصور ذلك في الشكل 3.

**3.1 الخسارة الثلاثية**

يتم تمثيل التضمين بـ f(x) ∈ R^d. يضمن صورة x في فضاء إقليدي ذو d بُعد. بالإضافة إلى ذلك، نقيد هذا التضمين ليعيش على الكرة الفائقة ذات البُعد d، أي ||f(x)||_2 = 1. تحفز هذه الخسارة الرغبة في ضمان أن صورة x_i^a (مرساة) لشخص معين أقرب إلى جميع الصور الأخرى x_i^p (إيجابية) لنفس الشخص مما هي عليه لأي صورة x_i^n (سلبية) لأي شخص آخر في فضاء التضمين. وبالتالي نريد

||f(x_i^a) - f(x_i^p)||_2^2 + α < ||f(x_i^a) - f(x_i^n)||_2^2,    (1)

∀(f(x_i^a), f(x_i^p), f(x_i^n)) ∈ T

حيث α هو هامش يُفرض بين الأزواج الإيجابية والسلبية. T هي مجموعة جميع الثلاثيات الممكنة في مجموعة التدريب ولها عددية N.

الخسارة التي يتم تقليلها هي إذن

L = Σ [||f(x_i^a) - f(x_i^p)||_2^2 - ||f(x_i^a) - f(x_i^n)||_2^2 + α]_+    (2)

إن توليد جميع الثلاثيات الممكنة سيؤدي إلى العديد من الثلاثيات التي يسهل استيفاؤها (أي تفي بالقيد في المعادلة (1)). لن تساهم هذه الثلاثيات في التدريب وستؤدي إلى تقارب أبطأ، حيث سيظل يتم تمريرها عبر الشبكة. من الضروري اختيار ثلاثيات صعبة، نشطة وبالتالي يمكن أن تساهم في تحسين النموذج. يتحدث القسم التالي عن الأساليب المختلفة التي نستخدمها لاختيار الثلاثيات.

**3.2 اختيار الثلاثيات**

لضمان التقارب السريع، من الضروري اختيار ثلاثيات تنتهك قيد الثلاثية في المعادلة (1). وهذا يعني أنه بالنظر إلى x_i^a، نريد اختيار x_i^p (إيجابي صعب) بحيث argmax_{x_i^p} ||f(x_i^a) - f(x_i^p)||_2^2 وبالمثل x_i^n (سلبي صعب) بحيث argmin_{x_i^n} ||f(x_i^a) - f(x_i^n)||_2^2.

من غير الممكن حساب argmin و argmax عبر مجموعة التدريب بأكملها. بالإضافة إلى ذلك، قد يؤدي ذلك إلى تدريب ضعيف، حيث ستهيمن الوجوه الموسومة بشكل خاطئ والمصورة بشكل سيئ على الإيجابيات والسلبيات الصعبة. هناك خياران واضحان يتجنبان هذه المشكلة:

• توليد الثلاثيات غير متصل كل n خطوة، باستخدام أحدث نقطة تفتيش للشبكة وحساب argmin و argmax على مجموعة فرعية من البيانات.

• توليد الثلاثيات متصل. يمكن القيام بذلك عن طريق اختيار الأمثلة الإيجابية/السلبية الصعبة من داخل دفعة صغيرة.

هنا، نركز على التوليد المتصل ونستخدم دفعات صغيرة كبيرة في حدود بضعة آلاف من الأمثلة ونحسب فقط argmin و argmax داخل دفعة صغيرة.

للحصول على تمثيل ذي معنى لمسافات المرساة-الإيجابية، يجب التأكد من وجود عدد أدنى من الأمثلة لأي هوية واحدة في كل دفعة صغيرة. في تجاربنا، نقوم بأخذ عينات من بيانات التدريب بحيث يتم اختيار حوالي 40 وجهاً لكل هوية لكل دفعة صغيرة. بالإضافة إلى ذلك، استكشفنا أيضاً نهج التوليد غير المتصل واستخدمنا عدداً أقل إجمالاً من السلبيات والإيجابيات ولكن كلها صعبة التمييز.

يمكن أن يؤدي اختيار أصعب السلبيات عملياً إلى نقاط دنيا محلية سيئة في وقت مبكر من التدريب، وتحديداً يمكن أن يؤدي إلى نموذج منهار (أي f(x) = 0). للتخفيف من ذلك، نختار جميع أزواج المرساة-الإيجابية في دفعة صغيرة بينما نستخدم فقط السلبيات شبه الصعبة. هذه السلبيات أصعب من مسافة المرساة-الإيجابية، ولكن لا تزال لديها خسارة إيجابية، أي

||f(x_i^a) - f(x_i^p)||_2^2 < ||f(x_i^a) - f(x_i^n)||_2^2 < ||f(x_i^a) - f(x_i^p)||_2^2 + α.

كما ذكرنا من قبل، فإن الاختيار الصحيح للثلاثيات أمر بالغ الأهمية للتقارب السريع. من ناحية، نود استخدام دفعات صغيرة صغيرة لأن هذه تميل إلى تحسين التقارب أثناء الانحدار التدرجي العشوائي (SGD). من ناحية أخرى، تفاصيل التنفيذ تجعل دفعات من عشرات إلى مئات من الأمثلة أكثر كفاءة. ومع ذلك، فإن القيد الرئيسي فيما يتعلق بحجم الدفعة هو الطريقة التي نختار بها الثلاثيات الصعبة ذات الصلة من داخل الدفعات الصغيرة. في معظم التجارب نستخدم حجم دفعة يبلغ حوالي 1,800 مثال.

**3.3 الشبكات العصبية الالتفافية العميقة**

في جميع تجاربنا ندرب الشبكة العصبية الالتفافية باستخدام الانحدار التدرجي العشوائي (SGD) مع الانتشار العكسي القياسي و AdaGrad. في معظم التجارب نبدأ بمعدل تعلم 0.05 والذي نخفضه لإنهاء النموذج. يتم تهيئة النماذج بشكل عشوائي، على غرار Szegedy وآخرين، ويتم تدريبها على مجموعة وحدة معالجة مركزية لمدة 1,000 إلى 2,000 ساعة. ينخفض الانخفاض في الخسارة (والزيادة في الدقة) بشكل كبير بعد 500 ساعة من التدريب، ولكن التدريب الإضافي لا يزال بإمكانه تحسين الأداء بشكل كبير. الهامش α مضبوط على 0.2.

استخدمنا نوعين من المعماريات ونستكشف مفاضلاتهما بمزيد من التفصيل في قسم التجارب. الأول هو معمارية Zeiler&Fergus مع التفافات 1×1 كما هو مقترح في Lin وآخرين. نشير إلى هذا النموذج باسم NN1. تحتوي هذه المعمارية على إجمالي 140 مليون معامل ومتطلبات FLOP تبلغ حوالي 1.6 مليار.

الفئة الثانية من النماذج هي نماذج من نوع Inception. تحتوي هذه النماذج على عدد من المعاملات أقل بمرتبة واحدة (حوالي 6.6 مليون - 7.5 مليون) وحتى خمس مرات أقل من FLOPS (بين 500 مليون - 1.6 مليار). بعض هذه النماذج مخفضة بشكل كبير في الحجم (بعامل 20)، بينما تضحي فقط بـ 10% من أداء NN1. يصف الجدول 1 تفاصيل هذه النماذج ويصور الشكل 4 المعمارية.

يتكون الإدخال إلى الشبكات من صور وجوه مقصوصة بشكل عشوائي بحجم 220×220. تتضمن تفاصيل معمارية NN2:
- طبقات التفاف بأحجام مرشح متفاوتة
- وحدات Inception مع التفافات متوازية
- طبقات تطبيع الدفعة
- طبقات التجميع الأقصى
- تطبيع L2 على طبقة التضمين النهائية

أضفنا أيضاً تطبيع الدفعة إلى طبقات مختارة والتي وجدنا أنها تحسن سرعة التدريب. يتم تدريب النماذج باستخدام مجموعة متنوعة من دقات الصور من 96×96 بكسل حتى 224×224 بكسل. النماذج الأصغر تعمل بسرعة تقارب ضعفي السرعة وهو أمر مهم لسيناريوهات النشر. اختيار حجم الإدخال هو مفاضلة بين الدقة والسرعة.

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 3, Figure 4, Table 1
- **Key terms introduced:**
  - Triplet loss (الخسارة الثلاثية)
  - Anchor (المرساة)
  - Positive/Negative pairs (الأزواج الإيجابية/السلبية)
  - Hard positive/negative (إيجابي/سلبي صعب)
  - Semi-hard negatives (السلبيات شبه الصعبة)
  - Mini-batch (الدفعة الصغيرة)
  - End-to-end learning (التعلم من طرف إلى طرف)
  - Stochastic Gradient Descent (الانحدار التدرجي العشوائي)
  - AdaGrad (AdaGrad - kept as is)
  - Inception model (نموذج Inception)
  - Batch normalization (تطبيع الدفعة)
  - FLOPS (FLOPS - kept as is, computational operations)
  - Hypersphere (الكرة الفائقة)
  - Collapsed model (نموذج منهار)
  - Argmin/Argmax (argmin/argmax - kept as mathematical notation)
  - Online/Offline generation (التوليد المتصل/غير المتصل)

- **Equations:**
  - Equation (1): Triplet constraint
  - Equation (2): Triplet loss function
  - Mathematical notation preserved: L2 norm, squared distances

- **Citations:**
  - Zeiler&Fergus, Lin et al., Szegedy et al.

- **Special handling:**
  - Model names kept in English: NN1, NN2, Inception, Zeiler&Fergus
  - Mathematical symbols preserved in English
  - Technical parameters (learning rate, margin α, batch sizes) preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87
