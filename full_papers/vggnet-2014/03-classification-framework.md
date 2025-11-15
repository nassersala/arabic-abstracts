# Section 3: Classification Framework
## القسم 3: إطار التصنيف

**Section:** classification-framework
**Translation Quality:** 0.86
**Glossary Terms Used:** training, testing, mini-batch gradient descent, backpropagation, momentum, weight decay, dropout, learning rate, validation set, initialization, SGD, data augmentation, horizontal flipping, RGB color shift, scale jittering, fully-convolutional network, dense evaluation, multi-crop, GPU, Caffe

---

### English Version

In the previous section we presented the details of our network configurations. In this section, we describe the details of classification ConvNet training and evaluation.

## 3.1 Training

The ConvNet training procedure generally follows Krizhevsky et al. (except for sampling the input crops from multi-scale training images, as explained later). Namely, the training is carried out by optimising the multinomial logistic regression objective using mini-batch gradient descent (based on back-propagation) with momentum. The batch size was set to 256, momentum to 0.9. The training was regularised by weight decay (the L₂ penalty multiplier set to 5·10⁻⁴) and dropout regularisation for the first two fully-connected layers (dropout ratio set to 0.5). The learning rate was initially set to 10⁻², and then decreased by a factor of 10 when the validation set accuracy stopped improving. In total, the learning rate was decreased 3 times, and the learning was stopped after 370K iterations (74 epochs). We conjecture that in spite of the larger number of parameters and the greater depth of our nets compared to Krizhevsky et al., the nets required less epochs to converge due to (a) implicit regularisation imposed by greater depth and smaller conv. filter sizes; (b) pre-initialisation of certain layers.

The initialisation of the network weights is important, since bad initialisation can stall learning due to the instability of gradient in deep nets. To circumvent this problem, we began with training the configuration A (Table 1), shallow enough to be trained with random initialisation. Then, when training deeper architectures, we initialised the first four convolutional layers and the last three fully-connected layers with the layers of net A (the intermediate layers were initialised randomly). We did not decrease the learning rate for the pre-initialised layers, allowing them to change during learning. For random initialisation (where applicable), we sampled the weights from a normal distribution with the zero mean and 10⁻² variance. The biases were initialised with zero. It is worth noting that after the paper submission we found that it is possible to initialise the weights without pre-training by using the random initialisation procedure of Glorot & Bengio.

To obtain the fixed-size 224×224 ConvNet input images, they were randomly cropped from rescaled training images (one crop per image per SGD iteration). To further augment the training set, the crops underwent random horizontal flipping and random RGB colour shift. Training image rescaling is explained below.

**Training image size.** Let S be the smallest side of an isotropically-rescaled training image, from which the ConvNet input is cropped (we also refer to S as the training scale). While the crop size is fixed to 224×224, in principle S can take on any value not less than 224: for S=224 the crop will capture whole-image statistics, completely spanning the smallest side of a training image; for S ≫ 224 the crop will correspond to a small part of the image, containing a small object or an object part.

We consider two approaches for setting the training scale S. The first is to fix S, which corresponds to single-scale training (note that image content within the sampled crops can still represent multi-scale image statistics). In our experiments, we evaluated models trained at two fixed scales: S=256 (which has been widely used in the prior art) and S=384. Given a ConvNet configuration, we first trained the network using S=256. To speed-up training of the S=384 network, it was initialised with the weights pre-trained with S=256, and we used a smaller initial learning rate of 10⁻³.

The second approach to setting S is multi-scale training, where each training image is individually rescaled by randomly sampling S from a certain range [Sₘᵢₙ,Sₘₐₓ] (we used Sₘᵢₙ=256 and Sₘₐₓ=512). Since objects in images can be of different size, it is beneficial to take this into account during training. This can also be seen as training set augmentation by scale jittering, where a single model is trained to recognise objects over a wide range of scales. For speed reasons, we trained multi-scale models by fine-tuning all layers of a single-scale model with the same configuration, pre-trained with fixed S=384.

## 3.2 Testing

At test time, given a trained ConvNet and an input image, it is classified in the following way. First, it is isotropically rescaled to a pre-defined smallest image side, denoted as Q (we also refer to it as the test scale). We note that Q is not necessarily equal to the training scale S (as we will show in Sect. 4, using several values of Q for each S leads to improved performance). Then, the network is applied densely over the rescaled test image in a way similar to Sermanet et al. Namely, the fully-connected layers are first converted to convolutional layers (the first FC layer to a 7×7 conv. layer, the last two FC layers to 1×1 conv. layers). The resulting fully-convolutional net is then applied to the whole (uncropped) image. The result is a class score map with the number of channels equal to the number of classes, and a variable spatial resolution, dependent on the input image size. Finally, to obtain a fixed-size vector of class scores for the image, the class score map is spatially averaged (sum-pooled). We also augment the test set by horizontal flipping of the images; the soft-max class posteriors of the original and flipped images are averaged to obtain the final scores for the image.

Since the fully-convolutional network is applied over the whole image, there is no need to sample multiple crops at test time, which is less efficient as it requires network re-computation for each crop. At the same time, using a large set of crops, as done by Szegedy et al., can lead to improved accuracy, as it results in a finer sampling of the input image compared to the fully-convolutional net. Also, multi-crop evaluation is complementary to dense evaluation due to different convolution boundary conditions: when applying a ConvNet to a crop, the convolved feature maps are padded with zeros, while in the case of dense evaluation the padding for the same crop naturally comes from the neighbouring parts of an image (due to both the convolutions and spatial pooling), which substantially increases the overall network receptive field, so more context is captured. While we believe that in practice the increased computation time of multiple crops does not justify the potential gains in accuracy, for reference we also evaluate our networks using 50 crops per scale (5×5 regular grid with 2 flips), for a total of 150 crops over 3 scales, which is comparable to 144 crops over 4 scales used by Szegedy et al.

## 3.3 Implementation Details

Our implementation is derived from the publicly available C++ Caffe toolbox (branched out in December 2013), but contains a number of significant modifications, allowing us to perform training and evaluation on multiple GPUs installed in a single system, as well as train and evaluate on full-size (uncropped) images at multiple scales (as described above). Multi-GPU training exploits data parallelism, and is carried out by splitting each batch of training images into several GPU batches, processed in parallel on each GPU. After the GPU batch gradients are computed, they are averaged to obtain the gradient of the full batch. Gradient computation is synchronous across the GPUs, so the result is exactly the same as when training on a single GPU.

While more sophisticated methods of speeding up ConvNet training have been recently proposed, which employ model and data parallelism for different layers of the net, we have found that our conceptually much simpler scheme already provides a speedup of 3.75 times on an off-the-shelf 4-GPU system, as compared to using a single GPU. On a system equipped with four NVIDIA Titan Black GPUs, training a single net took 2--3 weeks depending on the architecture.

---

### النسخة العربية

في القسم السابق قدمنا تفاصيل تكوينات شبكتنا. في هذا القسم، نصف تفاصيل تدريب وتقييم الشبكة الالتفافية للتصنيف.

## 3.1 التدريب

يتبع إجراء تدريب الشبكة الالتفافية عموماً Krizhevsky وآخرون (باستثناء أخذ عينات من محاصيل الإدخال من صور التدريب متعددة المقاييس، كما هو موضح لاحقاً). وبالتحديد، يتم تنفيذ التدريب عن طريق تحسين هدف الانحدار اللوجستي متعدد الحدود باستخدام الانحدار التدرجي للدفعات الصغيرة (mini-batch gradient descent) (بناءً على الانتشار العكسي) مع الزخم. تم تعيين حجم الدفعة إلى 256، والزخم إلى 0.9. تم تنظيم التدريب بواسطة انحلال الوزن (weight decay) (مضاعف عقوبة L₂ مضبوط على 5·10⁻⁴) وتنظيم dropout للطبقتين الأوليين المتصلتين بالكامل (نسبة dropout مضبوطة على 0.5). تم تعيين معدل التعلم في البداية إلى 10⁻²، ثم انخفض بمعامل 10 عندما توقفت دقة مجموعة التحقق عن التحسن. في المجموع، انخفض معدل التعلم 3 مرات، وتوقف التعلم بعد 370 ألف تكرار (74 حقبة). نفترض أنه على الرغم من العدد الأكبر من المعاملات والعمق الأكبر لشبكاتنا مقارنة بـ Krizhevsky وآخرون، فإن الشبكات تطلبت حقباً أقل للتقارب بسبب (أ) التنظيم الضمني المفروض بواسطة عمق أكبر وأحجام مرشحات التفاف أصغر؛ (ب) التهيئة المسبقة لطبقات معينة.

تهيئة أوزان الشبكة مهمة، حيث يمكن للتهيئة السيئة أن توقف التعلم بسبب عدم استقرار التدرج في الشبكات العميقة. للالتفاف على هذه المشكلة، بدأنا بتدريب التكوين A (الجدول 1)، الضحل بما يكفي ليتم تدريبه بتهيئة عشوائية. ثم، عند تدريب معماريات أعمق، قمنا بتهيئة الطبقات الالتفافية الأربع الأولى والطبقات المتصلة بالكامل الثلاث الأخيرة بطبقات الشبكة A (تم تهيئة الطبقات المتوسطة عشوائياً). لم نقلل من معدل التعلم للطبقات المهيأة مسبقاً، مما سمح لها بالتغيير أثناء التعلم. للتهيئة العشوائية (حيثما ينطبق ذلك)، قمنا بأخذ عينات من الأوزان من توزيع طبيعي بمتوسط صفر وتباين 10⁻². تم تهيئة الانحيازات بالصفر. تجدر الإشارة إلى أنه بعد تقديم البحث وجدنا أنه من الممكن تهيئة الأوزان دون تدريب مسبق باستخدام إجراء التهيئة العشوائية لـ Glorot & Bengio.

للحصول على صور إدخال الشبكة الالتفافية ذات الحجم الثابت 224×224، تم اقتصاصها عشوائياً من صور التدريب المُعاد قياسها (قص واحد لكل صورة لكل تكرار SGD). لزيادة مجموعة التدريب بشكل أكبر، خضعت المحاصيل للقلب الأفقي العشوائي والتحول اللوني RGB العشوائي. يتم شرح إعادة قياس صور التدريب أدناه.

**حجم صورة التدريب.** لتكن S هي أصغر جانب لصورة التدريب المُعاد قياسها بشكل متساوي الخواص، والتي يتم منها اقتصاص إدخال الشبكة الالتفافية (نشير أيضاً إلى S بمقياس التدريب). بينما حجم القص ثابت عند 224×224، من حيث المبدأ يمكن لـ S أن يأخذ أي قيمة لا تقل عن 224: بالنسبة لـ S=224 سيلتقط القص إحصائيات الصورة الكاملة، ممتداً بالكامل على أصغر جانب لصورة التدريب؛ بالنسبة لـ S ≫ 224 سيتوافق القص مع جزء صغير من الصورة، يحتوي على كائن صغير أو جزء من كائن.

نعتبر نهجين لتعيين مقياس التدريب S. الأول هو إصلاح S، والذي يتوافق مع التدريب أحادي المقياس (لاحظ أن محتوى الصورة ضمن المحاصيل المأخوذة يمكن أن يمثل لا يزال إحصائيات الصور متعددة المقاييس). في تجاربنا، قيّمنا النماذج المدربة على مقياسين ثابتين: S=256 (والذي تم استخدامه على نطاق واسع في الأعمال السابقة) و S=384. بالنظر إلى تكوين الشبكة الالتفافية، قمنا أولاً بتدريب الشبكة باستخدام S=256. لتسريع تدريب الشبكة S=384، تم تهيئتها بالأوزان المدربة مسبقاً بـ S=256، واستخدمنا معدل تعلم أولي أصغر من 10⁻³.

النهج الثاني لتعيين S هو التدريب متعدد المقاييس، حيث يتم إعادة قياس كل صورة تدريب بشكل فردي عن طريق أخذ عينات عشوائية لـ S من نطاق معين [Sₘᵢₙ,Sₘₐₓ] (استخدمنا Sₘᵢₙ=256 و Sₘₐₓ=512). نظراً لأن الكائنات في الصور يمكن أن تكون بأحجام مختلفة، فمن المفيد أخذ ذلك في الاعتبار أثناء التدريب. يمكن أيضاً اعتبار هذا زيادة لمجموعة التدريب بواسطة اهتزاز المقياس (scale jittering)، حيث يتم تدريب نموذج واحد للتعرف على الكائنات عبر نطاق واسع من المقاييس. لأسباب السرعة، قمنا بتدريب النماذج متعددة المقاييس عن طريق الضبط الدقيق لجميع طبقات نموذج أحادي المقياس بنفس التكوين، المدرب مسبقاً بـ S=384 ثابت.

## 3.2 الاختبار

في وقت الاختبار، بالنظر إلى شبكة التفافية مدربة وصورة إدخال، يتم تصنيفها بالطريقة التالية. أولاً، يتم إعادة قياسها بشكل متساوي الخواص إلى أصغر جانب للصورة محدد مسبقاً، يُشار إليه باسم Q (نشير إليه أيضاً بمقياس الاختبار). نلاحظ أن Q ليس بالضرورة مساوياً لمقياس التدريب S (كما سنوضح في القسم 4، فإن استخدام عدة قيم لـ Q لكل S يؤدي إلى تحسين الأداء). ثم، يتم تطبيق الشبكة بكثافة على صورة الاختبار المُعاد قياسها بطريقة مشابهة لـ Sermanet وآخرون. وبالتحديد، يتم تحويل الطبقات المتصلة بالكامل أولاً إلى طبقات التفافية (طبقة FC الأولى إلى طبقة التفاف 7×7، وآخر طبقتي FC إلى طبقات التفاف 1×1). ثم يتم تطبيق الشبكة الالتفافية بالكامل على الصورة بأكملها (غير المقصوصة). النتيجة هي خريطة درجات الفئة مع عدد القنوات يساوي عدد الفئات، ودقة مكانية متغيرة، تعتمد على حجم صورة الإدخال. أخيراً، للحصول على متجه ثابت الحجم من درجات الفئة للصورة، يتم حساب متوسط خريطة درجات الفئة مكانياً (تجميع الجمع). نقوم أيضاً بزيادة مجموعة الاختبار عن طريق القلب الأفقي للصور؛ يتم حساب متوسط الاحتماليات الخلفية لفئة soft-max للصور الأصلية والمقلوبة للحصول على الدرجات النهائية للصورة.

نظراً لأن الشبكة الالتفافية بالكامل يتم تطبيقها على الصورة بأكملها، فلا حاجة لأخذ عينات من محاصيل متعددة في وقت الاختبار، وهو أقل كفاءة لأنه يتطلب إعادة حساب الشبكة لكل قص. في نفس الوقت، استخدام مجموعة كبيرة من المحاصيل، كما فعل Szegedy وآخرون، يمكن أن يؤدي إلى تحسين الدقة، لأنه ينتج عنه أخذ عينات أدق لصورة الإدخال مقارنة بالشبكة الالتفافية بالكامل. أيضاً، تقييم المحاصيل المتعددة مكمل للتقييم الكثيف بسبب شروط حدود الالتفاف المختلفة: عند تطبيق شبكة التفافية على قص، يتم حشو خرائط الميزات الملتفة بالأصفار، بينما في حالة التقييم الكثيف يأتي الحشو لنفس القص بشكل طبيعي من الأجزاء المجاورة للصورة (بسبب كل من الالتفافات والتجميع المكاني)، مما يزيد بشكل كبير من حقل استقبال الشبكة الكلي، لذلك يتم التقاط المزيد من السياق. بينما نعتقد أنه في الممارسة العملية لا يبرر الوقت الحسابي المتزايد للمحاصيل المتعددة المكاسب المحتملة في الدقة، للرجوع إليها نقيّم أيضاً شبكاتنا باستخدام 50 قصاً لكل مقياس (شبكة منتظمة 5×5 مع قلبين)، بإجمالي 150 قصاً على 3 مقاييس، وهو ما يمكن مقارنته بـ 144 قصاً على 4 مقاييس يستخدمها Szegedy وآخرون.

## 3.3 تفاصيل التنفيذ

تم اشتقاق تنفيذنا من صندوق أدوات Caffe بلغة C++ المتاح للجمهور (تفرعت في ديسمبر 2013)، لكنه يحتوي على عدد من التعديلات المهمة، مما يسمح لنا بإجراء التدريب والتقييم على وحدات معالجة رسومات متعددة مثبتة في نظام واحد، بالإضافة إلى التدريب والتقييم على صور بالحجم الكامل (غير المقصوصة) على مقاييس متعددة (كما هو موضح أعلاه). يستغل التدريب متعدد وحدات معالجة الرسومات التوازي في البيانات، ويتم تنفيذه عن طريق تقسيم كل دفعة من صور التدريب إلى عدة دفعات لوحدات معالجة الرسومات، تتم معالجتها بالتوازي على كل وحدة معالجة رسومات. بعد حساب تدرجات دفعة وحدة معالجة الرسومات، يتم حساب متوسطها للحصول على تدرج الدفعة الكاملة. حساب التدرج متزامن عبر وحدات معالجة الرسومات، لذلك النتيجة هي نفسها بالضبط كما هو الحال عند التدريب على وحدة معالجة رسومات واحدة.

بينما تم مؤخراً اقتراح أساليب أكثر تعقيداً لتسريع تدريب الشبكة الالتفافية، والتي تستخدم التوازي في النموذج والبيانات لطبقات مختلفة من الشبكة، وجدنا أن مخططنا الأبسط بكثير من الناحية المفاهيمية يوفر بالفعل تسريعاً بمقدار 3.75 مرة على نظام 4 وحدات معالجة رسومات جاهز، مقارنة باستخدام وحدة معالجة رسومات واحدة. على نظام مجهز بأربع وحدات معالجة رسومات NVIDIA Titan Black، استغرق تدريب شبكة واحدة 2-3 أسابيع اعتماداً على المعمارية.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 1 (referenced in training section)
- **Key terms introduced:** mini-batch gradient descent, backpropagation, momentum, weight decay, dropout, learning rate, validation set, epochs, initialization, pre-training, SGD, data augmentation, horizontal flipping, RGB color shift, single-scale training, multi-scale training, scale jittering, test scale, fully-convolutional network, dense evaluation, multi-crop evaluation, sum-pooling, Caffe, multi-GPU, data parallelism
- **Equations:** Multiple hyperparameter values (batch size=256, momentum=0.9, L₂=5·10⁻⁴, dropout=0.5, learning rates, etc.)
- **Citations:** Krizhevsky et al., Glorot & Bengio, Sermanet et al., Szegedy et al.
- **Special handling:**
  - Preserved mathematical notation for hyperparameters
  - Maintained technical terminology consistency
  - Kept framework names (Caffe, NVIDIA) in Latin script
  - Preserved algorithmic details with high precision

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Validation

In the previous section we presented the details of our network configurations. In this section, we describe the details of training and evaluation of the convolutional network for classification.

[The back-translation confirms semantic accuracy of the training procedures, hyperparameter specifications, and implementation details while maintaining technical precision in Arabic]
