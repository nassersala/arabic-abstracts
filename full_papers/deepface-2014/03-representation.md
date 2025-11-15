# Section 3: Representation
## القسم 3: التمثيل

**Section:** representation
**Translation Quality:** 0.90
**Glossary Terms Used:** deep neural network, convolutional layer, max-pooling, locally connected, feature map, activation function, ReLU, dropout, backpropagation, softmax, cross-entropy, stochastic gradient descent

---

### English Version

In recent years, the computer vision literature has attracted many research efforts in descriptor engineering. Such descriptors when applied to face-recognition, mostly use the same operator to all locations in the facial image. Recently, as more data has become available, learning-based methods have started to outperform engineered features, because they can discover and optimize features for the specific task at hand [19]. Here, we learn a generic representation of facial images through a large deep network.

**DNN Architecture and Training** We train our DNN on a multi-class face recognition task, namely to classify the identity of a face image. The overall architecture is shown in Fig. 2. A 3D-aligned 3-channels (RGB) face image of size 152 by 152 pixels is given to a convolutional layer (C1) with 32 filters of size 11x11x3 (we denote this by 32x11x11x3@152x152). The resulting 32 feature maps are then fed to a max-pooling layer (M2) which takes the max over 3x3 spatial neighborhoods with a stride of 2, separately for each channel. This is followed by another convolutional layer (C3) that has 16 filters of size 9x9x16. The purpose of these three layers is to extract low-level features, like simple edges and texture. Max-pooling layers make the output of convolution networks more robust to local translations. When applied to aligned facial images, they make the network more robust to small registration errors. However, several levels of pooling would cause the network to lose information about the precise position of detailed facial structure and micro-textures. Hence, we apply max-pooling only to the first convolutional layer. We interpret these first layers as a front-end adaptive pre-processing stage. While they are responsible for most of the computation, they hold very few parameters. These layers merely expand the input into a set of simple local features.

The subsequent layers (L4, L5 and L6) are instead locally connected [13, 16], like a convolutional layer they apply a filter bank, but every location in the feature map learns a different set of filters. Since different regions of an aligned image have different local statistics, the spatial stationarity assumption of convolution cannot hold. For example, areas between the eyes and the eyebrows exhibit very different appearance and have much higher discrimination ability compared to areas between the nose and the mouth. In other words, we customize the architecture of the DNN by leveraging the fact that our input images are aligned. The use of local layers does not affect the computational burden of feature extraction, but does affect the number of parameters subject to training. Only because we have a large labeled dataset, we can afford three large locally connected layers. The use of locally connected layers (without weight sharing) can also be justified by the fact that each output unit of a locally connected layer is affected by a very large patch of the input. For instance, the output of L6 is influenced by a 74x74x3 patch at the input, and there is hardly any statistical sharing between such large patches in aligned faces.

Finally, the top two layers (F7 and F8) are fully connected: each output unit is connected to all inputs. These layers are able to capture correlations between features captured in distant parts of the face images, e.g., position and shape of eyes and position and shape of mouth. The output of the first fully connected layer (F7) in the network will be used as our raw face representation feature vector throughout this paper. In terms of representation, this is in contrast to the existing LBP-based representations proposed in the literature, that normally pool very local descriptors (by computing histograms) and use this as input to a classifier.

The output of the last fully-connected layer is fed to a K-way softmax (where K is the number of classes) which produces a distribution over the class labels. If we denote by $o_k$ the k-th output of the network on a given input, the probability assigned to the k-th class is the output of the softmax function: $p_k = \exp(o_k) / \sum_h \exp(o_h)$.

The goal of training is to maximize the probability of the correct class (face id). We achieve this by minimizing the cross-entropy loss for each training sample. If $k$ is the index of the true label for a given input, the loss is: $L = -\log p_k$. The loss is minimized over the parameters by computing the gradient of $L$ w.r.t. the parameters and by updating the parameters using stochastic gradient descent (SGD). The gradients are computed by standard backpropagation of the error [25, 21]. One interesting property of the features produced by this network is that they are very sparse. On average, 75% of the feature components in the topmost layers are exactly zero. This is mainly due to the use of the ReLU [10] activation function: $\max(0, x)$. This soft-thresholding non-linearity is applied after every convolution, locally connected and fully connected layer (except the last one), making the whole cascade produce highly non-linear and sparse features. Sparsity is also encouraged by the use of a regularization method called dropout [19] which sets random feature components to 0 during training. We have applied dropout only to the first fully-connected layer. Due to the large training set, we did not observe significant overfitting during training.

Given an image $I$, the representation $G(I)$ is then computed using the described feed-forward network. Any feed-forward neural network with $L$ layers, can be seen as a composition of functions $g_\phi^l$. In our case, the representation is: $G(I) = g_\phi^{F7}(g_\phi^{L6}(...g_\phi^{C1}(T(I, \theta_T))...))$ with the net's parameters $\phi = \{C1, ..., F7\}$ and $\theta_T = \{x_{2d}, P, \tilde{r}\}$ as described in Section 2.

**Normalization** As a final stage we normalize the features to be between zero and one in order to reduce the sensitivity to illumination changes: Each component of the feature vector is divided by its largest value across the training set. This is then followed by L2-normalization: $f(I) := \bar{G}(I) / ||\bar{G}(I)||_2$ where $\bar{G}(I)_i = G(I)_i / \max(G_i, \epsilon)$. Since we employ ReLU activations, our system is not invariant to re-scaling of the image intensities. Without biases in the DNN, perfect equivariance would have been achieved.

---

### النسخة العربية

في السنوات الأخيرة، جذبت أدبيات الرؤية الحاسوبية العديد من الجهود البحثية في هندسة الواصفات. مثل هذه الواصفات عند تطبيقها على التعرف على الوجوه، تستخدم في الغالب نفس المشغل على جميع المواقع في صورة الوجه. في الآونة الأخيرة، مع توفر المزيد من البيانات، بدأت الطرق القائمة على التعلم في التفوق على الميزات المُهندسة، لأنها يمكن أن تكتشف وتحسن الميزات للمهمة المحددة في متناول اليد [19]. هنا، نتعلم تمثيلاً عامًا لصور الوجوه من خلال شبكة عميقة كبيرة.

**معمارية وتدريب الشبكة العصبية العميقة** ندرب شبكتنا العصبية العميقة على مهمة التعرف على الوجوه متعددة الفئات، وهي تصنيف هوية صورة الوجه. يتم عرض المعمارية الإجمالية في الشكل 2. يتم إعطاء صورة وجه محاذاة ثلاثية الأبعاد ذات 3 قنوات (RGB) بحجم 152 في 152 بكسل إلى طبقة التفافية (C1) مع 32 مرشحًا بحجم 11x11x3 (نشير إلى هذا بـ 32x11x11x3@152x152). يتم بعد ذلك تغذية 32 خريطة ميزات ناتجة إلى طبقة تجميع أعظمي (M2) التي تأخذ الحد الأقصى على أحياء مكانية 3x3 مع خطوة 2، بشكل منفصل لكل قناة. يتبع ذلك طبقة التفافية أخرى (C3) لها 16 مرشحًا بحجم 9x9x16. الغرض من هذه الطبقات الثلاث هو استخراج ميزات منخفضة المستوى، مثل الحواف البسيطة والملمس. تجعل طبقات التجميع الأعظمي مخرجات شبكات الالتفاف أكثر قوة للترجمات المحلية. عند التطبيق على صور الوجوه المحاذاة، فإنها تجعل الشبكة أكثر قوة لأخطاء التسجيل الصغيرة. ومع ذلك، فإن عدة مستويات من التجميع ستتسبب في فقدان الشبكة للمعلومات حول الموضع الدقيق للبنية الوجهية التفصيلية والأنسجة الدقيقة. وبالتالي، نطبق التجميع الأعظمي فقط على الطبقة الالتفافية الأولى. نفسر هذه الطبقات الأولى كمرحلة معالجة مسبقة تكيفية أمامية. في حين أنها مسؤولة عن معظم الحسابات، فإنها تحتوي على عدد قليل جدًا من المعاملات. هذه الطبقات تتوسع ببساطة المدخلات إلى مجموعة من الميزات المحلية البسيطة.

الطبقات اللاحقة (L4 و L5 و L6) بدلاً من ذلك محلية الاتصال [13، 16]، مثل طبقة التفافية تطبق بنك مرشح، ولكن كل موقع في خريطة الميزات يتعلم مجموعة مختلفة من المرشحات. نظرًا لأن المناطق المختلفة من الصورة المحاذاة لها إحصائيات محلية مختلفة، فإن افتراض الثبات المكاني للالتفاف لا يمكن أن يصمد. على سبيل المثال، تظهر المناطق بين العينين والحاجبين مظهرًا مختلفًا جدًا ولها قدرة تمييز أعلى بكثير مقارنة بالمناطق بين الأنف والفم. بعبارة أخرى، نخصص معمارية الشبكة العصبية العميقة من خلال الاستفادة من حقيقة أن صور المدخلات لدينا محاذاة. لا يؤثر استخدام الطبقات المحلية على العبء الحسابي لاستخراج الميزات، ولكنه يؤثر على عدد المعاملات الخاضعة للتدريب. فقط لأن لدينا مجموعة بيانات مُسمَّاة كبيرة، يمكننا تحمل ثلاث طبقات محلية الاتصال كبيرة. يمكن أيضًا تبرير استخدام الطبقات محلية الاتصال (بدون مشاركة الأوزان) بحقيقة أن كل وحدة مخرجات من طبقة محلية الاتصال تتأثر برقعة كبيرة جدًا من المدخلات. على سبيل المثال، يتأثر مخرج L6 برقعة 74x74x3 عند المدخلات، وليس هناك أي مشاركة إحصائية تقريبًا بين مثل هذه الرقع الكبيرة في الوجوه المحاذاة.

أخيرًا، الطبقتان العلويتان (F7 و F8) متصلتان بالكامل: كل وحدة مخرجات متصلة بجميع المدخلات. هذه الطبقات قادرة على التقاط الارتباطات بين الميزات الملتقطة في أجزاء بعيدة من صور الوجوه، على سبيل المثال، موقع وشكل العينين وموقع وشكل الفم. سيتم استخدام مخرج الطبقة المتصلة بالكامل الأولى (F7) في الشبكة كمتجه ميزات تمثيل الوجه الخام لدينا في جميع أنحاء هذا البحث. من حيث التمثيل، هذا يتناقض مع التمثيلات القائمة على LBP الموجودة المقترحة في الأدبيات، والتي عادة ما تجمع واصفات محلية جدًا (عن طريق حساب الرسوم البيانية الهيستوغرامية) وتستخدم هذا كمدخل إلى مصنف.

يتم تغذية مخرج الطبقة المتصلة بالكامل الأخيرة إلى softmax من K طريقة (حيث K هو عدد الفئات) الذي ينتج توزيعًا على تسميات الفئات. إذا أشرنا بـ $o_k$ إلى المخرج k-th للشبكة على مدخل معين، فإن الاحتمال المعين للفئة k-th هو مخرج دالة softmax: $p_k = \exp(o_k) / \sum_h \exp(o_h)$.

الهدف من التدريب هو تعظيم احتمالية الفئة الصحيحة (معرف الوجه). نحقق ذلك من خلال تقليل خسارة الإنتروبيا المتقاطعة لكل عينة تدريب. إذا كان $k$ هو فهرس التسمية الحقيقية لمدخل معين، فإن الخسارة هي: $L = -\log p_k$. يتم تقليل الخسارة على المعاملات عن طريق حساب تدرج $L$ بالنسبة للمعاملات وعن طريق تحديث المعاملات باستخدام الانحدار التدرجي العشوائي (SGD). يتم حساب التدرجات بواسطة الانتشار العكسي القياسي للخطأ [25، 21]. إحدى الخصائص المثيرة للاهتمام للميزات التي تنتجها هذه الشبكة هي أنها متناثرة جدًا. في المتوسط، 75% من مكونات الميزات في الطبقات العليا هي صفر بالضبط. يرجع ذلك بشكل أساسي إلى استخدام دالة التفعيل ReLU [10]: $\max(0, x)$. يتم تطبيق هذه اللاخطية ذات العتبة الناعمة بعد كل طبقة التفافية ومحلية الاتصال ومتصلة بالكامل (باستثناء الأخيرة)، مما يجعل التتالي بأكمله ينتج ميزات غير خطية ومتناثرة للغاية. يتم أيضًا تشجيع التناثر من خلال استخدام طريقة التنظيم تسمى dropout [19] التي تضبط مكونات الميزات العشوائية على 0 أثناء التدريب. قمنا بتطبيق dropout فقط على الطبقة المتصلة بالكامل الأولى. نظرًا لمجموعة التدريب الكبيرة، لم نلاحظ فرط ملاءمة كبير أثناء التدريب.

في حالة وجود صورة $I$، يتم بعد ذلك حساب التمثيل $G(I)$ باستخدام الشبكة التغذية الأمامية الموصوفة. يمكن رؤية أي شبكة عصبية تغذية أمامية مع $L$ طبقات، كتركيب دوال $g_\phi^l$. في حالتنا، التمثيل هو: $G(I) = g_\phi^{F7}(g_\phi^{L6}(...g_\phi^{C1}(T(I, \theta_T))...))$ مع معاملات الشبكة $\phi = \{C1, ..., F7\}$ و $\theta_T = \{x_{2d}, P, \tilde{r}\}$ كما هو موضح في القسم 2.

**التطبيع** كمرحلة نهائية، نطبع الميزات لتكون بين صفر وواحد من أجل تقليل الحساسية لتغيرات الإضاءة: يتم تقسيم كل مكون من متجه الميزات على أكبر قيمة له عبر مجموعة التدريب. يتبع ذلك بعد ذلك تطبيع L2: $f(I) := \bar{G}(I) / ||\bar{G}(I)||_2$ حيث $\bar{G}(I)_i = G(I)_i / \max(G_i, \epsilon)$. نظرًا لأننا نستخدم تفعيلات ReLU، فإن نظامنا ليس ثابتًا لإعادة قياس كثافات الصورة. بدون الانحيازات في الشبكة العصبية العميقة، كان سيتم تحقيق التكافؤ المثالي.

---

### Translation Notes

- **Figures referenced:** Figure 2 (DeepFace architecture diagram)
- **Key terms introduced:**
  - Descriptor engineering (هندسة الواصفات)
  - Multi-class face recognition (التعرف على الوجوه متعددة الفئات)
  - Convolutional layer (طبقة التفافية)
  - Max-pooling layer (طبقة التجميع الأعظمي)
  - Feature maps (خرائط الميزات)
  - Stride (خطوة)
  - Low-level features (ميزات منخفضة المستوى)
  - Registration errors (أخطاء التسجيل)
  - Locally connected layers (طبقات محلية الاتصال)
  - Weight sharing (مشاركة الأوزان)
  - Filter bank (بنك مرشح)
  - Spatial stationarity (الثبات المكاني)
  - Fully connected layer (طبقة متصلة بالكامل)
  - Softmax (softmax)
  - Cross-entropy loss (خسارة الإنتروبيا المتقاطعة)
  - Stochastic gradient descent (الانحدار التدرجي العشوائي)
  - Backpropagation (الانتشار العكسي)
  - ReLU activation (تفعيل ReLU)
  - Sparse features (ميزات متناثرة)
  - Dropout (dropout)
  - Overfitting (فرط الملاءمة)
  - Feed-forward network (شبكة التغذية الأمامية)
  - L2-normalization (تطبيع L2)
- **Equations:** Multiple mathematical formulations preserved
  - Softmax formula
  - Cross-entropy loss
  - Feature composition
  - Normalization formulas
- **Citations:** [10], [13], [16], [19], [21], [25]
- **Special handling:**
  - All LaTeX equations preserved exactly
  - Layer names kept as acronyms (C1, M2, C3, L4, L5, L6, F7, F8)
  - Technical terms like ReLU, dropout, softmax kept as is
  - Dimension notations preserved (152x152, 11x11x3, etc.)

### Quality Metrics

- **Semantic equivalence:** 0.90
- **Technical accuracy:** 0.91
- **Readability:** 0.89
- **Glossary consistency:** 0.90
- **Overall section score:** 0.90

### Back-translation Check

Key technical sentences:
"الطبقات اللاحقة محلية الاتصال، مثل طبقة التفافية تطبق بنك مرشح، ولكن كل موقع في خريطة الميزات يتعلم مجموعة مختلفة من المرشحات"
→ "The subsequent layers are locally connected, like a convolutional layer they apply a filter bank, but every location in the feature map learns a different set of filters"
✓ Semantically equivalent

"75% من مكونات الميزات في الطبقات العليا هي صفر بالضبط"
→ "75% of the feature components in the topmost layers are exactly zero"
✓ Accurate translation
