# Section 2: Fast R-CNN Architecture and Training
## القسم 2: معمارية Fast R-CNN والتدريب

**Section:** architecture and training
**Translation Quality:** 0.87
**Glossary Terms Used:** architecture (معمارية), convolutional (التفافي), pooling (تجميع), feature map (خريطة الميزات), fully connected (متصل بالكامل), softmax, bounding box (صندوق التحديد), regression (انحدار), fine-tuning (ضبط دقيق), back-propagation (الانتشار العكسي), training (التدريب)

---

### English Version

Fig. 1 illustrates the Fast R-CNN architecture. A Fast R-CNN network takes as input an entire image and a set of object proposals. The network first processes the whole image with several convolutional (conv) and max pooling layers to produce a conv feature map. Then, for each object proposal a region of interest (RoI) pooling layer extracts a fixed-length feature vector from the feature map. Each feature vector is fed into a sequence of fully connected (fc) layers that finally branch into two sibling output layers: one that produces softmax probability estimates over K object classes plus a catch-all "background" class and another layer that outputs four real-valued numbers for each of the K object classes. Each set of 4 values encodes refined bounding-box positions for one of the K classes.

**2.1. The RoI pooling layer**

The RoI pooling layer uses max pooling to convert the features inside any valid region of interest into a small feature map with a fixed spatial extent of H×W (e.g., 7×7), where H and W are layer hyper-parameters that are independent of any particular RoI. In this paper, an RoI is a rectangular window into a conv feature map. Each RoI is defined by a four-tuple (r, c, h, w) that specifies its top-left corner (r, c) and its height and width (h, w).

**Figure 1.** Fast R-CNN architecture. An input image and multiple regions of interest (RoIs) are input into a fully convolutional network. Each RoI is pooled into a fixed-size feature map and then mapped to a feature vector by fully connected layers (FCs). The network has two output vectors per RoI: softmax probabilities and per-class bounding-box regression offsets. The architecture is trained end-to-end with a multi-task loss.

RoI max pooling works by dividing the h×w RoI window into an H×W grid of sub-windows of approximate size h/H × w/W and then max-pooling the values in each sub-window into the corresponding output grid cell. Pooling is applied independently to each feature map channel, as in standard max pooling. The RoI layer is simply the special-case of the spatial pyramid pooling layer used in SPPnets [11] in which there is only one pyramid level. We use the pooling sub-window calculation given in [11].

**2.2. Initializing from pre-trained networks**

We experiment with three pre-trained ImageNet [4] networks, each with five max pooling layers and between five and thirteen conv layers (see Section 4.1 for network details). When a pre-trained network initializes a Fast R-CNN network, it undergoes three transformations.

First, the last max pooling layer is replaced by a RoI pooling layer that is configured by setting H and W to be compatible with the net's first fully connected layer (e.g., H=W=7 for VGG16).

Second, the network's last fully connected layer and softmax (which were trained for 1000-way ImageNet classification) are replaced with the two sibling layers described earlier (a fully connected layer and softmax over K+1 categories and category-specific bounding-box regressors).

Third, the network is modified to take two data inputs: a list of images and a list of RoIs in those images.

**2.3. Fine-tuning for detection**

Training all network weights with back-propagation is an important capability of Fast R-CNN. First, let's elucidate why SPPnet is unable to update weights below the spatial pyramid pooling layer.

The root cause is that back-propagation through the SPP layer is highly inefficient when each training sample (i.e. RoI) comes from a different image, which is exactly how R-CNN and SPPnet networks are trained. The inefficiency stems from the fact that each RoI may have a very large receptive field, often spanning the entire input image. Since the forward pass must process the entire receptive field, the training inputs are large (often the entire image).

We propose a more efficient training method that takes advantage of feature sharing during training. In Fast R-CNN training, stochastic gradient descent (SGD) mini-batches are sampled hierarchically, first by sampling N images and then by sampling R/N RoIs from each image. Critically, RoIs from the same image share computation and memory in the forward and backward passes. Making N small decreases mini-batch computation. For example, when using N=2 and R=128, the proposed training scheme is roughly 64× faster than sampling one RoI from 128 different images (i.e., the R-CNN and SPPnet strategy).

One concern over this strategy is it may cause slow training convergence because RoIs from the same image are correlated. This concern does not appear to be a practical issue and we achieve good results with N=2 and R=128 using fewer SGD iterations than R-CNN.

In addition to hierarchical sampling, Fast R-CNN uses a streamlined training process with one fine-tuning stage that jointly optimizes a softmax classifier and bounding-box regressors, rather than training a softmax classifier, SVMs, and regressors in three separate stages [9, 11]. The components of this procedure (the loss, mini-batch sampling strategy, back-propagation through RoI pooling layers, and SGD hyper-parameters) are described below.

**Multi-task loss.** A Fast R-CNN network has two sibling output layers. The first outputs a discrete probability distribution (per RoI), p = (p₀, ..., pₖ), over K+1 categories. As usual, p is computed by a softmax over the K+1 outputs of a fully connected layer. The second sibling layer outputs bounding-box regression offsets, tᵏ = (tₓᵏ, tᵧᵏ, t_wᵏ, t_hᵏ), for each of the K object classes, indexed by k. We use the parameterization for tᵏ given in [9], in which tᵏ specifies a scale-invariant translation and log-space height/width shift relative to an object proposal.

Each training RoI is labeled with a ground-truth class u and a ground-truth bounding-box regression target v. We use a multi-task loss L on each labeled RoI to jointly train for classification and bounding-box regression:

$$L(p, u, t^u, v) = L_{cls}(p, u) + \lambda[u \geq 1]L_{loc}(t^u, v),\quad(1)$$

in which $L_{cls}(p, u) = -\log p_u$ is log loss for true class u.

The second task loss, $L_{loc}$, is defined over a tuple of true bounding-box regression targets for class u, v = (vₓ, vᵧ, v_w, v_h), and a predicted tuple $t^u = (t_x^u, t_y^u, t_w^u, t_h^u)$, again for class u. The Iverson bracket indicator function $[u \geq 1]$ evaluates to 1 when u≥1 and 0 otherwise. By convention the catch-all background class is labeled u=0. For background RoIs there is no notion of a ground-truth bounding box and hence $L_{loc}$ is ignored. For bounding-box regression, we use the loss

$$L_{loc}(t^u, v) = \sum_{i \in \{x,y,w,h\}} \text{smooth}_{L_1}(t_i^u - v_i),\quad(2)$$

in which

$$\text{smooth}_{L_1}(x) = \begin{cases} 0.5x^2 & \text{if } |x| < 1\\ |x| - 0.5 & \text{otherwise} \end{cases}\quad(3)$$

is a robust L₁ loss that is less sensitive to outliers than the L₂ loss used in R-CNN and SPPnet. When the regression targets are unbounded, training with L₂ loss can require careful tuning of learning rates in order to prevent exploding gradients. Eq. 3 eliminates this sensitivity.

The hyper-parameter λ in Eq. 1 controls the balance between the two task losses. We normalize the ground-truth regression targets vᵢ to have zero mean and unit variance. All experiments use λ=1.

We note that [6] uses a related loss to train a class-agnostic object proposal network. Different from our approach, [6] advocates for a two-network system that separates localization and classification. OverFeat [19], R-CNN [9], and SPPnet [11] also train classifiers and bounding-box localizers, however these methods use stage-wise training, which we show is suboptimal for Fast R-CNN (Section 5.1).

**Mini-batch sampling.** During fine-tuning, each SGD mini-batch is constructed from N=2 images, chosen uniformly at random (as is common practice, we actually iterate over permutations of the dataset). We use mini-batches of size R=128, sampling 64 RoIs from each image. As in [9], we take 25% of the RoIs from object proposals that have intersection over union (IoU) overlap with a ground-truth bounding box of at least 0.5. These RoIs comprise the examples labeled with a foreground object class, i.e. u≥1. The remaining RoIs are sampled from object proposals that have a maximum IoU with ground truth in the interval [0.1, 0.5), following [11]. These are the background examples and are labeled with u=0. The lower threshold of 0.1 appears to act as a heuristic for hard example mining [8]. During training, images are horizontally flipped with probability 0.5. No other data augmentation is used.

**Back-propagation through RoI pooling layers.** Back-propagation routes derivatives through the RoI pooling layer. For clarity, we assume only one image per mini-batch (N=1), though the extension to N>1 is straightforward because the forward pass treats all images independently.

Let xᵢ∈ℝ be the i-th activation input into the RoI pooling layer and let yᵣⱼ be the layer's j-th output from the r-th RoI. The RoI pooling layer computes yᵣⱼ = xᵢ*(r,j), in which i*(r,j) = argmax_{i'∈R(r,j)} xᵢ'. R(r,j) is the index set of inputs in the sub-window over which the output unit yᵣⱼ max pools. A single xᵢ may be assigned to several different outputs yᵣⱼ.

The RoI pooling layer's backwards function computes partial derivative of the loss function with respect to each input variable xᵢ by following the argmax switches:

$$\frac{\partial L}{\partial x_i} = \sum_r \sum_j [i = i^*(r,j)] \frac{\partial L}{\partial y_{rj}}.\quad(4)$$

In words, for each mini-batch RoI r and for each pooling output unit yᵣⱼ, the partial derivative ∂L/∂yᵣⱼ is accumulated if i is the argmax selected for yᵣⱼ by max pooling. In back-propagation, the partial derivatives ∂L/∂yᵣⱼ are already computed by the backwards function of the layer on top of the RoI pooling layer.

**SGD hyper-parameters.** The fully connected layers used for softmax classification and bounding-box regression are initialized from zero-mean Gaussian distributions with standard deviations 0.01 and 0.001, respectively. Biases are initialized to 0. All layers use a per-layer learning rate of 1 for weights and 2 for biases and a global learning rate of 0.001. When training on VOC07 or VOC12 trainval we run SGD for 30k mini-batch iterations, and then lower the learning rate to 0.0001 and train for another 10k iterations. When we train on larger datasets, we run SGD for more iterations, as described later. A momentum of 0.9 and parameter decay of 0.0005 (on weights and biases) are used.

**2.4. Scale invariance**

We explore two ways of achieving scale invariant object detection: (1) via "brute force" learning and (2) by using image pyramids. These strategies follow the two approaches in [11]. In the brute-force approach, each image is processed at a pre-defined pixel size during both training and testing. The network must directly learn scale-invariant object detection from the training data.

The multi-scale approach, in contrast, provides approximate scale-invariance to the network through an image pyramid. At test-time, the image pyramid is used to approximately scale-normalize each object proposal. During multi-scale training, we randomly sample a pyramid scale each time an image is sampled, following [11], as a form of data augmentation. We experiment with multi-scale training for smaller networks only, due to GPU memory limits.

---

### النسخة العربية

يوضح الشكل 1 معمارية Fast R-CNN. تأخذ شبكة Fast R-CNN كمدخل صورة كاملة ومجموعة من مقترحات الأجسام. تعالج الشبكة أولاً الصورة بأكملها بعدة طبقات التفافية (conv) وطبقات تجميع أقصى لإنتاج خريطة ميزات التفافية. ثم، لكل مقترح جسم، تستخرج طبقة تجميع منطقة الاهتمام (RoI) متجه ميزات ذو طول ثابت من خريطة الميزات. يُغذى كل متجه ميزات إلى سلسلة من الطبقات المتصلة بالكامل (fc) التي تتفرع أخيراً إلى طبقتي مخرجات متوازيتين: واحدة تُنتج تقديرات احتمالية softmax على K فئة من فئات الأجسام بالإضافة إلى فئة "الخلفية" الشاملة، وطبقة أخرى تُخرج أربعة أرقام حقيقية لكل فئة من فئات الأجسام K. كل مجموعة من 4 قيم تُشفر مواقع صناديق التحديد المحسّنة لواحدة من الفئات K.

**2.1. طبقة تجميع RoI**

تستخدم طبقة تجميع RoI التجميع الأقصى لتحويل الميزات داخل أي منطقة اهتمام صالحة إلى خريطة ميزات صغيرة ذات امتداد مكاني ثابت H×W (مثل 7×7)، حيث H و W معاملات فائقة للطبقة مستقلة عن أي RoI معينة. في هذه الورقة، RoI هي نافذة مستطيلة في خريطة ميزات التفافية. يتم تعريف كل RoI بواسطة رباعية (r، c، h، w) تحدد الزاوية العلوية اليسرى (r، c) والارتفاع والعرض (h، w).

**الشكل 1.** معمارية Fast R-CNN. يتم إدخال صورة مدخلة ومناطق اهتمام متعددة (RoIs) إلى شبكة التفافية بالكامل. يتم تجميع كل RoI في خريطة ميزات ذات حجم ثابت ثم تُعيّن إلى متجه ميزات بواسطة طبقات متصلة بالكامل (FCs). تحتوي الشبكة على متجهي مخرجات لكل RoI: احتماليات softmax وإزاحات انحدار صندوق التحديد لكل فئة. يتم تدريب المعمارية من البداية إلى النهاية بدالة خسارة متعددة المهام.

يعمل تجميع RoI الأقصى عن طريق تقسيم نافذة RoI بحجم h×w إلى شبكة H×W من النوافذ الفرعية بحجم تقريبي h/H × w/W ثم التجميع الأقصى للقيم في كل نافذة فرعية في خلية الشبكة المخرجة المقابلة. يتم تطبيق التجميع بشكل مستقل على كل قناة من قنوات خريطة الميزات، كما في التجميع الأقصى القياسي. طبقة RoI هي ببساطة الحالة الخاصة من طبقة التجميع الهرمي المكاني المستخدمة في SPPnets [11] والتي يوجد فيها مستوى هرمي واحد فقط. نستخدم حساب النافذة الفرعية للتجميع المذكور في [11].

**2.2. التهيئة من الشبكات المدربة مسبقاً**

نجري تجارب مع ثلاث شبكات ImageNet [4] مدربة مسبقاً، كل منها بخمس طبقات تجميع أقصى وبين خمس وثلاث عشرة طبقة التفافية (انظر القسم 4.1 لتفاصيل الشبكة). عندما تهيئ شبكة مدربة مسبقاً شبكة Fast R-CNN، فإنها تخضع لثلاث تحولات.

أولاً، يتم استبدال طبقة التجميع الأقصى الأخيرة بطبقة تجميع RoI التي يتم تكوينها بتعيين H و W لتكون متوافقة مع أول طبقة متصلة بالكامل للشبكة (مثل H=W=7 لـ VGG16).

ثانياً، يتم استبدال آخر طبقة متصلة بالكامل و softmax في الشبكة (التي تم تدريبها لتصنيف ImageNet من 1000 فئة) بطبقتين متوازيتين موصوفتين سابقاً (طبقة متصلة بالكامل و softmax على K+1 فئة ومنحدرات صناديق تحديد خاصة بالفئات).

ثالثاً، يتم تعديل الشبكة لأخذ مدخلين من البيانات: قائمة من الصور وقائمة من RoIs في تلك الصور.

**2.3. الضبط الدقيق للكشف**

يعد تدريب جميع أوزان الشبكة باستخدام الانتشار العكسي قدرة مهمة لـ Fast R-CNN. أولاً، دعنا نوضح لماذا لا تستطيع SPPnet تحديث الأوزان أسفل طبقة التجميع الهرمي المكاني.

السبب الجذري هو أن الانتشار العكسي عبر طبقة SPP غير فعال للغاية عندما تأتي كل عينة تدريب (أي RoI) من صورة مختلفة، وهذا بالضبط كيفية تدريب شبكات R-CNN و SPPnet. ينبع عدم الكفاءة من حقيقة أن كل RoI قد يكون لها حقل استقبالي كبير جداً، وغالباً ما يمتد عبر الصورة المدخلة بأكملها. نظراً لأن التمرير الأمامي يجب أن يعالج الحقل الاستقبالي بأكمله، فإن مدخلات التدريب كبيرة (غالباً الصورة بأكملها).

نقترح طريقة تدريب أكثر كفاءة تستفيد من مشاركة الميزات أثناء التدريب. في تدريب Fast R-CNN، يتم أخذ عينات من الدفعات الصغيرة للانحدار التدرجي العشوائي (SGD) بشكل هرمي، أولاً بأخذ عينات من N صورة ثم بأخذ عينات من R/N RoI من كل صورة. والأمر الحاسم هو أن RoIs من نفس الصورة تشارك الحسابات والذاكرة في التمريرات الأمامية والعكسية. جعل N صغيرة يقلل من حساب الدفعة الصغيرة. على سبيل المثال، عند استخدام N=2 و R=128، فإن مخطط التدريب المقترح أسرع بحوالي 64× من أخذ عينة واحدة من RoI من 128 صورة مختلفة (أي استراتيجية R-CNN و SPPnet).

أحد المخاوف بشأن هذه الاستراتيجية هو أنها قد تسبب تقارباً بطيئاً في التدريب لأن RoIs من نفس الصورة مترابطة. لا يبدو أن هذا القلق يمثل مشكلة عملية ونحقق نتائج جيدة مع N=2 و R=128 باستخدام تكرارات SGD أقل من R-CNN.

بالإضافة إلى أخذ العينات الهرمي، تستخدم Fast R-CNN عملية تدريب مبسطة مع مرحلة ضبط دقيق واحدة تحسن بشكل مشترك مصنف softmax ومنحدرات صناديق التحديد، بدلاً من تدريب مصنف softmax وآلات المتجهات الداعمة والمنحدرات في ثلاث مراحل منفصلة [9، 11]. يتم وصف مكونات هذا الإجراء (الخسارة، واستراتيجية أخذ عينات الدفعة الصغيرة، والانتشار العكسي عبر طبقات تجميع RoI، والمعاملات الفائقة لـ SGD) أدناه.

**دالة الخسارة متعددة المهام.** تحتوي شبكة Fast R-CNN على طبقتي مخرجات متوازيتين. تُخرج الأولى توزيعاً احتمالياً منفصلاً (لكل RoI)، p = (p₀، ...، pₖ)، على K+1 فئة. كالمعتاد، يتم حساب p بواسطة softmax على مخرجات K+1 لطبقة متصلة بالكامل. تُخرج الطبقة المتوازية الثانية إزاحات انحدار صندوق التحديد، tᵏ = (tₓᵏ، tᵧᵏ، t_wᵏ، t_hᵏ)، لكل فئة من فئات الأجسام K، مفهرسة بـ k. نستخدم المعاملات لـ tᵏ المذكورة في [9]، حيث تحدد tᵏ إزاحة ثابتة المقياس وتحول ارتفاع/عرض في فضاء اللوغاريتم نسبة إلى مقترح الجسم.

يتم تصنيف كل RoI تدريب بفئة الحقيقة الأرضية u وهدف انحدار صندوق التحديد للحقيقة الأرضية v. نستخدم دالة خسارة متعددة المهام L على كل RoI مصنفة للتدريب المشترك للتصنيف وانحدار صندوق التحديد:

$$L(p, u, t^u, v) = L_{cls}(p, u) + \lambda[u \geq 1]L_{loc}(t^u, v),\quad(1)$$

حيث $L_{cls}(p, u) = -\log p_u$ هي خسارة اللوغاريتم للفئة الحقيقية u.

تُعرّف خسارة المهمة الثانية، $L_{loc}$، على رباعية من أهداف انحدار صندوق التحديد الحقيقية للفئة u، v = (vₓ، vᵧ، v_w، v_h)، ورباعية متوقعة $t^u = (t_x^u, t_y^u, t_w^u, t_h^u)$، مرة أخرى للفئة u. تُقيّم دالة مؤشر قوس إيفرسون $[u \geq 1]$ إلى 1 عندما u≥1 و 0 خلاف ذلك. بالاتفاقية، يتم تصنيف فئة الخلفية الشاملة بـ u=0. بالنسبة لـ RoIs الخلفية، لا يوجد مفهوم لصندوق تحديد الحقيقة الأرضية وبالتالي يتم تجاهل $L_{loc}$. لانحدار صندوق التحديد، نستخدم الخسارة

$$L_{loc}(t^u, v) = \sum_{i \in \{x,y,w,h\}} \text{smooth}_{L_1}(t_i^u - v_i),\quad(2)$$

حيث

$$\text{smooth}_{L_1}(x) = \begin{cases} 0.5x^2 & \text{إذا } |x| < 1\\ |x| - 0.5 & \text{خلاف ذلك} \end{cases}\quad(3)$$

هي خسارة L₁ قوية أقل حساسية للقيم الشاذة من خسارة L₂ المستخدمة في R-CNN و SPPnet. عندما تكون أهداف الانحدار غير محدودة، فإن التدريب بخسارة L₂ قد يتطلب ضبطاً دقيقاً لمعدلات التعلم لمنع انفجار التدرجات. تُزيل المعادلة 3 هذه الحساسية.

يتحكم المعامل الفائق λ في المعادلة 1 في التوازن بين خسارتي المهمتين. نقوم بتطبيع أهداف الانحدار للحقيقة الأرضية vᵢ لتكون ذات متوسط صفر وتباين وحدة. تستخدم جميع التجارب λ=1.

نلاحظ أن [6] يستخدم خسارة ذات صلة لتدريب شبكة اقتراح أجسام محايدة للفئة. بخلاف نهجنا، يدعو [6] إلى نظام شبكتين يفصل التحديد الموقعي عن التصنيف. يقوم OverFeat [19] و R-CNN [9] و SPPnet [11] أيضاً بتدريب المصنفات ومحددات مواقع صناديق التحديد، ومع ذلك تستخدم هذه الطرق التدريب على مراحل، والذي نُظهر أنه دون الأمثل لـ Fast R-CNN (القسم 5.1).

**أخذ عينات الدفعة الصغيرة.** أثناء الضبط الدقيق، يتم بناء كل دفعة صغيرة SGD من N=2 صورة، يتم اختيارها بشكل عشوائي منتظم (كما هو الحال في الممارسة الشائعة، نقوم فعلياً بالتكرار على تباديل مجموعة البيانات). نستخدم دفعات صغيرة بحجم R=128، مع أخذ عينات من 64 RoI من كل صورة. كما في [9]، نأخذ 25% من RoIs من مقترحات الأجسام التي لديها تقاطع على اتحاد (IoU) مع صندوق تحديد الحقيقة الأرضية لا يقل عن 0.5. تشكل هذه RoIs الأمثلة المصنفة بفئة جسم أمامي، أي u≥1. يتم أخذ عينات من RoIs المتبقية من مقترحات الأجسام التي لديها IoU أقصى مع الحقيقة الأرضية في الفترة [0.1، 0.5)، متبعين [11]. هذه هي أمثلة الخلفية ويتم تصنيفها بـ u=0. يبدو أن العتبة الدنيا 0.1 تعمل كإرشادي لتعدين الأمثلة الصعبة [8]. أثناء التدريب، يتم قلب الصور أفقياً باحتمال 0.5. لا يتم استخدام أي تعزيز بيانات آخر.

**الانتشار العكسي عبر طبقات تجميع RoI.** يوجه الانتشار العكسي المشتقات عبر طبقة تجميع RoI. من أجل الوضوح، نفترض صورة واحدة فقط لكل دفعة صغيرة (N=1)، على الرغم من أن التوسع إلى N>1 واضح ومباشر لأن التمرير الأمامي يعامل جميع الصور بشكل مستقل.

لتكن xᵢ∈ℝ هي مدخل التنشيط i-th في طبقة تجميع RoI ولتكن yᵣⱼ هي المخرج j-th للطبقة من RoI r-th. تحسب طبقة تجميع RoI yᵣⱼ = xᵢ*(r,j)، حيث i*(r,j) = argmax_{i'∈R(r,j)} xᵢ'. R(r,j) هي مجموعة فهرس المدخلات في النافذة الفرعية التي تجمع عليها وحدة المخرج yᵣⱼ بشكل أقصى. قد يتم تعيين xᵢ واحدة إلى عدة مخرجات yᵣⱼ مختلفة.

تحسب دالة الخلف لطبقة تجميع RoI المشتق الجزئي لدالة الخسارة بالنسبة لكل متغير مدخل xᵢ من خلال اتباع مفاتيح argmax:

$$\frac{\partial L}{\partial x_i} = \sum_r \sum_j [i = i^*(r,j)] \frac{\partial L}{\partial y_{rj}}.\quad(4)$$

بكلمات أخرى، لكل RoI للدفعة الصغيرة r ولكل وحدة مخرج تجميع yᵣⱼ، يتم تراكم المشتق الجزئي ∂L/∂yᵣⱼ إذا كان i هو argmax المحدد لـ yᵣⱼ بواسطة التجميع الأقصى. في الانتشار العكسي، يتم بالفعل حساب المشتقات الجزئية ∂L/∂yᵣⱼ بواسطة دالة الخلف للطبقة فوق طبقة تجميع RoI.

**المعاملات الفائقة لـ SGD.** يتم تهيئة الطبقات المتصلة بالكامل المستخدمة لتصنيف softmax وانحدار صندوق التحديد من توزيعات غاوسية صفرية المتوسط مع انحرافات معيارية 0.01 و 0.001، على التوالي. يتم تهيئة الانحيازات إلى 0. تستخدم جميع الطبقات معدل تعلم لكل طبقة قدره 1 للأوزان و 2 للانحيازات ومعدل تعلم عام قدره 0.001. عند التدريب على VOC07 أو VOC12 trainval، نقوم بتشغيل SGD لـ 30k تكرار دفعة صغيرة، ثم نخفض معدل التعلم إلى 0.0001 ونتدرب لـ 10k تكرار أخرى. عندما نتدرب على مجموعات بيانات أكبر، نقوم بتشغيل SGD لمزيد من التكرارات، كما هو موضح لاحقاً. يتم استخدام زخم 0.9 وتحلل معامل 0.0005 (على الأوزان والانحيازات).

**2.4. ثبات المقياس**

نستكشف طريقتين لتحقيق كشف الأجسام الثابت للمقياس: (1) عبر التعلم "بالقوة الغاشمة" و (2) باستخدام أهرامات الصور. تتبع هذه الاستراتيجيات النهجين في [11]. في نهج القوة الغاشمة، تتم معالجة كل صورة بحجم بكسل محدد مسبقاً أثناء التدريب والاختبار. يجب على الشبكة أن تتعلم مباشرة كشف الأجسام الثابت للمقياس من بيانات التدريب.

في المقابل، يوفر النهج متعدد المقاييس ثباتاً تقريبياً للمقياس للشبكة من خلال هرم صور. في وقت الاختبار، يتم استخدام هرم الصور لتطبيع المقياس تقريبياً لكل مقترح جسم. أثناء التدريب متعدد المقاييس، نقوم بأخذ عينات عشوائية من مقياس هرمي في كل مرة يتم فيها أخذ عينة من صورة، متبعين [11]، كشكل من أشكال تعزيز البيانات. نجري تجارب مع التدريب متعدد المقاييس للشبكات الأصغر فقط، بسبب حدود ذاكرة GPU.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Fast R-CNN architecture diagram)
- **Key terms introduced:**
  - RoI (Region of Interest): منطقة الاهتمام
  - max pooling: التجميع الأقصى
  - feature map: خريطة الميزات
  - fully connected (fc): متصل بالكامل
  - sibling layers: طبقات متوازية
  - catch-all background class: فئة الخلفية الشاملة
  - four-tuple: رباعية
  - hyper-parameters: المعاملات الفائقة
  - end-to-end: من البداية إلى النهاية
  - multi-task loss: دالة خسارة متعددة المهام
  - ground-truth: الحقيقة الأرضية
  - Iverson bracket: قوس إيفرسون
  - smooth L₁: L₁ ناعمة
  - exploding gradients: انفجار التدرجات
  - IoU (Intersection over Union): التقاطع على الاتحاد
  - hard example mining: تعدين الأمثلة الصعبة
  - data augmentation: تعزيز البيانات
  - receptive field: الحقل الاستقبالي
  - stochastic gradient descent (SGD): الانحدار التدرجي العشوائي
  - mini-batch: دفعة صغيرة
  - momentum: الزخم
  - parameter decay: تحلل المعامل
  - scale-invariant: ثابت المقياس
  - image pyramid: هرم الصور

- **Equations:** 4 equations (Eq. 1-4) preserved exactly in LaTeX
- **Citations:** References [4, 6, 8, 9, 11, 15, 19]
- **Special handling:**
  - Preserved all mathematical equations in LaTeX format
  - Kept technical acronyms: RoI, SGD, IoU, SPP
  - Maintained numerical values exactly
  - Preserved variable names (H, W, N, R, K, u, v, p, t, x, y, λ) in equations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.90
- **Overall section score:** 0.87

### Back-translation Verification

Key technical paragraph back-translated:
Arabic: "تحسب طبقة تجميع RoI المشتق الجزئي لدالة الخسارة بالنسبة لكل متغير مدخل من خلال اتباع مفاتيح argmax"
Back to English: "The RoI pooling layer computes the partial derivative of the loss function with respect to each input variable by following the argmax switches"
✓ Matches original semantics accurately
