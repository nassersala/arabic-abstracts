# Section 3: Faster R-CNN
## القسم 3: Faster R-CNN

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** Region Proposal Network, anchor, convolutional, neural network, feature map, training, end-to-end, loss function, bounding box, objectness, regression, classification, IoU (Intersection over Union), gradient, backpropagation, fine-tuning, shared features

---

### English Version

Our object detection system, called Faster R-CNN, is composed of two modules. The first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector [4] that uses the proposed regions. The entire system is a single, unified network for object detection (Figure 2). Using the recently popular terminology of neural networks with "attention" [31] mechanisms, the RPN module tells the Fast R-CNN module where to look. In Section 3.1 we introduce the designs and properties of the network for region proposal. In Section 3.2 we develop algorithms for training both modules with features shared.

### 3.1 Region Proposal Networks

A Region Proposal Network (RPN) takes an image (of any size) as input and outputs a set of rectangular object proposals, each with an objectness score. We model this process with a fully convolutional network [7], which we describe in this section. Because our ultimate goal is to share computation with a Fast R-CNN object detection network [4], we assume that both nets share a common set of convolutional layers. In our experiments, we investigate the Zeiler and Fergus model [32] (ZF), which has 5 shareable convolutional layers and the Simonyan and Zisserman model [5] (VGG-16), which has 13 shareable convolutional layers.

To generate region proposals, we slide a small network over the convolutional feature map output by the last shared convolutional layer. This small network takes as input an n×n spatial window of the input convolutional feature map. Each sliding window is mapped to a lower-dimensional feature (256-d for ZF and 512-d for VGG, with ReLU [33] following). This feature is fed into two sibling fully-connected layers—a box-regression layer (reg) and a box-classification layer (cls). We use n = 3 in this paper, noting that the effective receptive field on the input image is large (171 and 228 pixels for ZF and VGG, respectively). This mini-network is illustrated at a single position in Figure 3 (left). Note that because the mini-network operates in a sliding-window fashion, the fully-connected layers are shared across all spatial locations. This architecture is naturally implemented with an n×n convolutional layer followed by two sibling 1×1 convolutional layers (for reg and cls, respectively).

#### 3.1.1 Anchors

At each sliding-window location, we simultaneously predict multiple region proposals, where the number of maximum possible proposals for each location is denoted as k. So the reg layer has 4k outputs encoding the coordinates of k boxes, and the cls layer outputs 2k scores that estimate probability of object or not object for each proposal. The k proposals are parameterized relative to k reference boxes, which we call anchors. An anchor is centered at the sliding window in question, and is associated with a scale and aspect ratio (Figure 3, left). By default we use 3 scales and 3 aspect ratios, yielding k = 9 anchors at each sliding position. For a convolutional feature map of a size W×H (typically ∼2,400), there are WHk anchors in total.

**Translation-Invariant Anchors.** An important property of our approach is that it is translation invariant, both in terms of the anchors and the functions that compute proposals relative to the anchors. If one translates an object in an image, the proposal should translate and the same function should be able to predict the proposal in either location. This translation-invariant property is guaranteed in our method. As a comparison, the MultiBox method [27] uses k-means to generate 800 anchors, which are not translation invariant. So MultiBox does not guarantee that the same proposal is generated if an object is translated.

The translation-invariant property also reduces the model size. MultiBox has a (4+1)×800-dimensional fully-connected output layer, whereas our method has a (4+2)×9-dimensional convolutional output layer in the case of k = 9 anchors. As a result, our output layer has 2.8×10⁴ parameters (512×(4+2)×9 for VGG-16), two orders of magnitude fewer than MultiBox's output layer that has 6.1×10⁶ parameters (1536×(4+1)×800 for GoogleNet [34] in MultiBox [27]). If considering the feature projection layers, our proposal layers still have an order of magnitude fewer parameters than MultiBox. We expect our method to have less risk of overfitting on small datasets, like PASCAL VOC.

**Multi-Scale Anchors as Regression References.** Our design of anchors presents a novel scheme for addressing multiple scales (and aspect ratios). As shown in Figure 1, there have been two popular ways for multi-scale predictions. The first way is based on image/feature pyramids, e.g., in DPM [37] and CNN-based methods [9], [3], [38]. The images are resized at multiple scales, and feature maps (HOG [37] or deep convolutional features [9], [3]) are computed for each scale (Figure 1(a)). This way is often useful but is time-consuming. The second way is to use sliding windows of multiple scales (and/or aspect ratios) on the feature maps. For example, in DPM [37], models of different aspect ratios are trained separately using different filter sizes (such as 5×7 and 7×5). If this way is used to address multiple scales, it can be thought of as a "pyramid of filters" (Figure 1(b)). The second way is usually adopted jointly with the first way [37].

As a comparison, our anchor-based method is built on a pyramid of anchors, which is more cost-efficient. Our method classifies and regresses bounding boxes with reference to anchor boxes of multiple scales and aspect ratios. It only relies on images and feature maps of a single scale, and uses filters (sliding windows on the feature map) of a single size. We show by experiments the effects of this scheme for addressing multiple scales and sizes (Table 8).

Because of this multi-scale design based on anchors, we can simply use the convolutional features computed on a single-scale image, as is also done by the Fast R-CNN detector [4]. The design of multi-scale anchors is a key component for sharing features without extra cost for addressing scales.

#### 3.1.2 Loss Function

For training RPNs, we assign a binary class label (of being an object or not) to each anchor. We assign a positive label to two kinds of anchors: (i) the anchor/anchors with the highest Intersection-over-Union (IoU) overlap with a ground-truth box, or (ii) an anchor that has an IoU overlap higher than 0.7 with any ground-truth box. Note that a single ground-truth box may assign positive labels to multiple anchors. Usually the second condition is sufficient to determine the positive samples; but we still adopt the first condition for the reason that in some rare cases the second condition may find no positive sample. We assign a negative label to a non-positive anchor if its IoU ratio is lower than 0.3 for all ground-truth boxes. Anchors that are neither positive nor negative do not contribute to the training objective.

With these definitions, we minimize an objective function following the multi-task loss in Fast R-CNN [4]. Our loss function for an image is defined as:

$$L(\\{p_i\\}, \\{t_i\\}) = \\frac{1}{N_{cls}} \\sum_i L_{cls}(p_i, p_i^*) + \\lambda \\frac{1}{N_{reg}} \\sum_i p_i^* L_{reg}(t_i, t_i^*)$$

Here, i is the index of an anchor in a mini-batch and $p_i$ is the predicted probability of anchor i being an object. The ground-truth label $p_i^*$ is 1 if the anchor is positive, and is 0 if the anchor is negative. $t_i$ is a vector representing the 4 parameterized coordinates of the predicted bounding box, and $t_i^*$ is that of the ground-truth box associated with a positive anchor. The classification loss $L_{cls}$ is log loss over two classes (object vs. not object). For the regression loss, we use $L_{reg}(t_i, t_i^*) = R(t_i - t_i^*)$ where R is the robust loss function (smooth L₁) defined in [4]. The term $p_i^* L_{reg}$ means the regression loss is activated only for positive anchors ($p_i^* = 1$) and is disabled otherwise ($p_i^* = 0$). The outputs of the cls and reg layers consist of {$p_i$} and {$t_i$} respectively.

The two terms are normalized by $N_{cls}$ and $N_{reg}$ and weighted by a balancing parameter λ. In our current implementation (as in the released code), the cls term in Eqn. (1) is normalized by the mini-batch size (i.e., $N_{cls}$ = 256) and the reg term is normalized by the number of anchor locations (i.e., $N_{reg}$ ∼ 2,400). By default we set λ = 10, and thus both cls and reg terms are roughly equally weighted. We show by experiments that the results are insensitive to the values of λ in a wide range (Table 9). We also note that the normalization as above is not required and could be simplified.

For bounding box regression, we adopt the parameterizations of the 4 coordinates following [2]:

$$t_x = (x - x_a)/w_a, \\quad t_y = (y - y_a)/h_a,$$
$$t_w = \\log(w/w_a), \\quad t_h = \\log(h/h_a),$$
$$t_x^* = (x^* - x_a)/w_a, \\quad t_y^* = (y^* - y_a)/h_a,$$
$$t_w^* = \\log(w^*/w_a), \\quad t_h^* = \\log(h^*/h_a),$$

where x, y, w, and h denote the box's center coordinates and its width and height. Variables x, $x_a$, and $x^*$ are for the predicted box, anchor box, and ground-truth box respectively (likewise for y, w, h). This can be thought of as bounding-box regression from an anchor box to a nearby ground-truth box.

Nevertheless, our method achieves bounding-box regression by a different manner from previous RoI-based (Region of Interest) methods [3], [4]. In [3], [4], bounding-box regression is performed on features pooled from arbitrarily sized RoIs, and the regression weights are shared by all region sizes. In our formulation, the features used for regression are of the same spatial size (3×3) on the feature maps. To account for varying sizes, a set of k bounding-box regressors are learned. Each regressor is responsible for one scale and one aspect ratio, and the k regressors do not share weights. As such, it is still possible to predict boxes of various sizes even though the features are of a fixed size/scale, thanks to the design of anchors.

#### 3.1.3 Training RPNs

The RPN can be trained end-to-end by back-propagation and stochastic gradient descent (SGD) [35]. We follow the "image-centric" sampling strategy from [4] to train this network. Each mini-batch arises from a single image that contains many positive and negative example anchors. It is possible to optimize for the loss functions of all anchors, but this will bias towards negative samples as they are dominate. Instead, we randomly sample 256 anchors in an image to compute the loss function of a mini-batch, where the sampled positive and negative anchors have a ratio of up to 1:1. If there are fewer than 128 positive samples in an image, we pad the mini-batch with negative ones.

We randomly initialize all new layers by drawing weights from a zero-mean Gaussian distribution with standard deviation 0.01. All other layers (i.e., the shared convolutional layers) are initialized by pretraining a model for ImageNet classification [36], as is standard practice [4]. We tune all layers of the ZF net, and conv3_1 and up for the VGG net to conserve memory [4]. We use a learning rate of 0.001 for 60k mini-batches, and 0.0001 for the next 20k mini-batches on the PASCAL VOC dataset. We use a momentum of 0.9 and a weight decay of 0.0005 [38]. Our implementation uses Caffe [39].

### 3.2 Sharing Features for RPN and Fast R-CNN

Thus far we have described how to train a network for region proposal generation, without considering the region-based object detection CNN that will utilize these proposals. For the detection network, we adopt Fast R-CNN [4]. Next we describe algorithms that learn a unified network composed of RPN and Fast R-CNN with shared convolutional layers (Figure 2).

Both RPN and Fast R-CNN, trained independently, will modify their convolutional layers in different ways. We therefore need to develop a technique that allows for sharing convolutional layers between the two networks, rather than learning two separate networks. We discuss three ways for training networks with features shared:

**(i) Alternating training.** In this solution, we first train RPN, and use the proposals to train Fast R-CNN. The network tuned by Fast R-CNN is then used to initialize RPN, and this process is iterated. This is the solution that is used in all experiments in this paper.

**(ii) Approximate joint training.** In this solution, the RPN and Fast R-CNN networks are merged into one network during training as in Figure 2. In each SGD iteration, the forward pass generates region proposals which are treated just like fixed, pre-computed proposals when training a Fast R-CNN detector. The backward propagation takes place as usual, where for the shared layers the backward propagated signals from both the RPN loss and the Fast R-CNN loss are combined. This solution is easy to implement. But this solution ignores the derivative w.r.t. the proposal boxes' coordinates that are also network responses, so is approximate. In our experiments, we have empirically found this solver produces close results, yet reduces the training time by about 25-50% compared with alternating training. This solver is included in our released Python code.

**(iii) Non-approximate joint training.** As discussed above, the bounding boxes predicted by RPN are also functions of the input. The RoI pooling layer [4] in Fast R-CNN accepts the convolutional features and also the predicted bounding boxes as input, so a theoretically valid backpropagation solver should also involve gradients w.r.t. the box coordinates. These gradients are ignored in the above approximate joint training. In a non-approximate joint training solution, we need an RoI pooling layer that is differentiable w.r.t. the box coordinates. This is a nontrivial problem and a solution can be given by an "RoI warping" layer as developed in [15], which is beyond the scope of this paper.

**4-Step Alternating Training.** In this paper, we adopt a pragmatic 4-step training algorithm to learn shared features via alternating optimization. In the first step, we train the RPN as described in Section 3.1.3. This network is initialized with an ImageNet-pre-trained model and fine-tuned end-to-end for the region proposal task. In the second step, we train a separate detection network by Fast R-CNN using the proposals generated by the step-1 RPN. This detection network is also initialized by the ImageNet-pre-trained model. At this point the two networks do not share convolutional layers. In the third step, we use the detector network to initialize RPN training, but we fix the shared convolutional layers and only fine-tune the layers unique to RPN. Now the two networks share convolutional layers. In the fourth step, keeping the shared convolutional layers fixed, we fine-tune the unique layers of Fast R-CNN. As such, both networks share the same convolutional layers and form a unified network. A similar alternating training can be run for more iterations, but we have observed negligible improvements.

### 3.3 Implementation Details

For both training and testing, we adopt single-scale images as described above. We re-scale the images such that their shorter side is s = 600 pixels [4]. Multi-scale feature extraction (using an image pyramid) may improve accuracy but does not exhibit a good speed-accuracy trade-off [4]. On the re-scaled images, the total stride for both ZF and VGG nets on the last convolutional layer is 16 pixels, and thus is ∼10 pixels on a typical PASCAL image before resizing (∼500×375). Even such a large stride provides good results, though accuracy may be further improved with a smaller stride.

For anchors, we use 3 scales with box areas of 128², 256², and 512² pixels, and 3 aspect ratios of 1:1, 1:2, and 2:1. These hyper-parameters are not carefully chosen for a particular dataset, and we provide ablation experiments on their effects in Section 4. As discussed, our solution does not need an image pyramid or filter pyramid to predict regions of multiple scales, saving considerable running time. Figure 1 (right) shows the capability of our method for a wide range of scales and aspect ratios. Table 1 shows the learned average proposal size for each anchor using the ZF net. We note that our algorithm allows predictions that are larger than the underlying receptive field. Such predictions are not impossible—one may still roughly infer the extent of an object if only the middle of the object is visible.

The anchor boxes that cross image boundaries need to be handled with care. During training, we ignore all cross-boundary anchors so they do not contribute to the loss. For a typical 1000×600 image, there will be roughly 20k (≈60×40×9) anchors in total. With the cross-boundary anchors ignored, there are about 6k anchors per image for training. If the boundary-crossing outliers are not ignored in training, they introduce large, difficult to correct error terms in the objective, and training does not converge. During testing, however, we still apply the fully convolutional RPN to the entire image. This may generate cross-boundary proposal boxes, which we clip to the image boundary.

Some RPN proposals highly overlap with each other. To reduce redundancy, we adopt non-maximum suppression (NMS) on the proposal regions based on their cls scores. We fix the IoU threshold for NMS at 0.7, which leaves us about 2000 proposal regions per image. As we will show, NMS does not harm the ultimate detection accuracy, but substantially reduces the number of proposals. After NMS, we use the top-N ranked proposal regions for detection. In the following, we train Fast R-CNN using 2000 RPN proposals, but evaluate different numbers of proposals at test-time.

---

### النسخة العربية

نظام كشف الأجسام لدينا، المسمى Faster R-CNN، يتكون من وحدتين. الوحدة الأولى هي شبكة التفافية عميقة بالكامل تقترح المناطق، والوحدة الثانية هي كاشف Fast R-CNN [4] الذي يستخدم المناطق المقترحة. النظام بأكمله عبارة عن شبكة واحدة موحدة لكشف الأجسام (الشكل 2). باستخدام المصطلحات الشائعة مؤخراً للشبكات العصبية ذات آليات "الانتباه" [31]، تخبر وحدة RPN وحدة Fast R-CNN عن المكان الذي يجب النظر إليه. في القسم 3.1 نقدم تصاميم وخصائص الشبكة لاقتراح المناطق. في القسم 3.2 نطور خوارزميات لتدريب كلتا الوحدتين مع ميزات مشتركة.

### 3.1 شبكات اقتراح المناطق

تأخذ شبكة اقتراح المناطق (RPN) صورة (بأي حجم) كمدخل وتخرج مجموعة من اقتراحات الأجسام المستطيلة، كل منها مع درجة وجود الجسم. نمذج هذه العملية باستخدام شبكة التفافية بالكامل [7]، والتي نصفها في هذا القسم. نظراً لأن هدفنا النهائي هو مشاركة الحساب مع شبكة كشف الأجسام Fast R-CNN [4]، نفترض أن كلتا الشبكتين تشتركان في مجموعة مشتركة من الطبقات الالتفافية. في تجاربنا، نحقق في نموذج Zeiler و Fergus [32] (ZF)، الذي يحتوي على 5 طبقات التفافية قابلة للمشاركة، ونموذج Simonyan و Zisserman [5] (VGG-16)، الذي يحتوي على 13 طبقة التفافية قابلة للمشاركة.

لتوليد اقتراحات المناطق، نمرر شبكة صغيرة فوق خريطة الميزات الالتفافية الناتجة عن آخر طبقة التفافية مشتركة. تأخذ هذه الشبكة الصغيرة كمدخل نافذة مكانية n×n من خريطة الميزات الالتفافية المدخلة. يتم تعيين كل نافذة منزلقة إلى ميزة ذات أبعاد أقل (256 بُعد لـ ZF و512 بُعد لـ VGG، مع ReLU [33] بعدها). تُغذى هذه الميزة في طبقتين متصلتين بالكامل شقيقتين - طبقة انحدار الصندوق (reg) وطبقة تصنيف الصندوق (cls). نستخدم n = 3 في هذه الورقة، مع ملاحظة أن المجال الاستقبالي الفعال على الصورة المدخلة كبير (171 و228 بكسل لـ ZF وVGG، على التوالي). هذه الشبكة الصغيرة موضحة في موضع واحد في الشكل 3 (يسار). لاحظ أنه بسبب عمل الشبكة الصغيرة بطريقة النافذة المنزلقة، فإن الطبقات المتصلة بالكامل مشتركة عبر جميع المواقع المكانية. يتم تطبيق هذه المعمارية بشكل طبيعي مع طبقة التفافية n×n متبوعة بطبقتين التفافيتين شقيقتين 1×1 (لـ reg وcls، على التوالي).

#### 3.1.1 المراسي

في كل موقع نافذة منزلقة، نتنبأ في آن واحد باقتراحات مناطق متعددة، حيث يُشار إلى عدد الاقتراحات القصوى الممكنة لكل موقع بـ k. لذا فإن طبقة reg لديها 4k مخرجات تشفر إحداثيات k صناديق، وطبقة cls تخرج 2k درجات تقدر احتمال وجود جسم أو عدم وجود جسم لكل اقتراح. يتم تحديد معاملات اقتراحات k بالنسبة إلى k صناديق مرجعية، نسميها المراسي. يتمركز المرساة في النافذة المنزلقة المعنية، ويرتبط بمقياس ونسبة أبعاد (الشكل 3، يسار). بشكل افتراضي نستخدم 3 مقاييس و3 نسب أبعاد، مما ينتج عنه k = 9 مراسٍ في كل موضع منزلق. بالنسبة لخريطة ميزات التفافية بحجم W×H (عادةً ∼2,400)، هناك WHk مرساة إجمالاً.

**المراسي غير المتغيرة بالإزاحة.** خاصية مهمة لنهجنا هي أنه غير متغير بالإزاحة، سواء من حيث المراسي أو الدوال التي تحسب الاقتراحات بالنسبة للمراسي. إذا قام المرء بإزاحة جسم في صورة، فيجب أن ينتقل الاقتراح وأن تكون نفس الدالة قادرة على التنبؤ بالاقتراح في أي من الموقعين. هذه الخاصية غير المتغيرة بالإزاحة مضمونة في طريقتنا. كمقارنة، تستخدم طريقة MultiBox [27] k-means لتوليد 800 مرساة، وهي ليست غير متغيرة بالإزاحة. لذا لا تضمن MultiBox أن نفس الاقتراح يتم توليده إذا تم إزاحة جسم.

الخاصية غير المتغيرة بالإزاحة تقلل أيضاً من حجم النموذج. لدى MultiBox طبقة مخرجات متصلة بالكامل ذات أبعاد (4+1)×800، بينما طريقتنا لديها طبقة مخرجات التفافية ذات أبعاد (4+2)×9 في حالة k = 9 مراسٍ. نتيجة لذلك، طبقة المخرجات لدينا تحتوي على 2.8×10⁴ معامل (512×(4+2)×9 لـ VGG-16)، أقل بمرتبين من حيث الحجم من طبقة مخرجات MultiBox التي تحتوي على 6.1×10⁶ معامل (1536×(4+1)×800 لـ GoogleNet [34] في MultiBox [27]). إذا أخذنا في الاعتبار طبقات إسقاط الميزات، فإن طبقات الاقتراح لدينا لا تزال تحتوي على معاملات أقل بمرتبة واحدة من MultiBox. نتوقع أن طريقتنا لديها مخاطر أقل من الإفراط في التوفيق على مجموعات البيانات الصغيرة، مثل PASCAL VOC.

**المراسي متعددة المقاييس كمراجع انحدار.** يقدم تصميم المراسي لدينا مخططاً جديداً لمعالجة مقاييس متعددة (ونسب أبعاد). كما هو موضح في الشكل 1، كانت هناك طريقتان شائعتان للتنبؤات متعددة المقاييس. الطريقة الأولى تعتمد على أهرامات الصور/الميزات، على سبيل المثال، في DPM [37] والطرق القائمة على CNN [9]، [3]، [38]. يتم تغيير حجم الصور بمقاييس متعددة، ويتم حساب خرائط الميزات (HOG [37] أو الميزات الالتفافية العميقة [9]، [3]) لكل مقياس (الشكل 1(أ)). هذه الطريقة غالباً ما تكون مفيدة ولكنها تستغرق وقتاً طويلاً. الطريقة الثانية هي استخدام نوافذ منزلقة بمقاييس متعددة (و/أو نسب أبعاد) على خرائط الميزات. على سبيل المثال، في DPM [37]، يتم تدريب نماذج نسب أبعاد مختلفة بشكل منفصل باستخدام أحجام مرشحات مختلفة (مثل 5×7 و7×5). إذا تم استخدام هذه الطريقة لمعالجة مقاييس متعددة، يمكن اعتبارها "هرم من المرشحات" (الشكل 1(ب)). عادةً ما يتم اعتماد الطريقة الثانية بالاشتراك مع الطريقة الأولى [37].

كمقارنة، طريقتنا القائمة على المراسي مبنية على هرم من المراسي، وهو أكثر كفاءة من حيث التكلفة. تصنف طريقتنا وتنحدر صناديق التحديد بالإشارة إلى صناديق المراسي بمقاييس ونسب أبعاد متعددة. تعتمد فقط على صور وخرائط ميزات من مقياس واحد، وتستخدم مرشحات (نوافذ منزلقة على خريطة الميزات) بحجم واحد. نُظهر بالتجارب تأثيرات هذا المخطط لمعالجة مقاييس وأحجام متعددة (الجدول 8).

بسبب هذا التصميم متعدد المقاييس القائم على المراسي، يمكننا ببساطة استخدام الميزات الالتفافية المحسوبة على صورة بمقياس واحد، كما يتم أيضاً بواسطة كاشف Fast R-CNN [4]. يُعد تصميم المراسي متعددة المقاييس مكوناً رئيسياً لمشاركة الميزات دون تكلفة إضافية لمعالجة المقاييس.

#### 3.1.2 دالة الخسارة

لتدريب شبكات RPN، نعين تسمية صنف ثنائي (لكونه جسماً أم لا) لكل مرساة. نعين تسمية إيجابية لنوعين من المراسي: (i) المرساة/المراسي ذات أعلى تداخل تقاطع على اتحاد (IoU) مع صندوق الحقيقة الأرضية، أو (ii) مرساة لديها تداخل IoU أعلى من 0.7 مع أي صندوق حقيقة أرضية. لاحظ أن صندوق حقيقة أرضية واحد قد يعين تسميات إيجابية لمراسٍ متعددة. عادةً ما يكون الشرط الثاني كافياً لتحديد العينات الإيجابية؛ لكننا لا نزال نعتمد الشرط الأول للسبب أنه في بعض الحالات النادرة قد لا يجد الشرط الثاني عينة إيجابية. نعين تسمية سلبية لمرساة غير إيجابية إذا كانت نسبة IoU أقل من 0.3 لجميع صناديق الحقيقة الأرضية. المراسي التي ليست إيجابية ولا سلبية لا تساهم في هدف التدريب.

مع هذه التعريفات، نُقلل دالة هدف تتبع خسارة المهام المتعددة في Fast R-CNN [4]. يتم تعريف دالة الخسارة لدينا لصورة على النحو التالي:

$$L(\\{p_i\\}, \\{t_i\\}) = \\frac{1}{N_{cls}} \\sum_i L_{cls}(p_i, p_i^*) + \\lambda \\frac{1}{N_{reg}} \\sum_i p_i^* L_{reg}(t_i, t_i^*)$$

هنا، i هو فهرس مرساة في دفعة صغيرة و$p_i$ هو الاحتمال المتنبأ به لمرساة i لكونها جسماً. تسمية الحقيقة الأرضية $p_i^*$ هي 1 إذا كانت المرساة إيجابية، و0 إذا كانت المرساة سلبية. $t_i$ هو متجه يمثل الإحداثيات الأربعة المحددة المعاملات لصندوق التحديد المتنبأ به، و$t_i^*$ هي إحداثيات صندوق الحقيقة الأرضية المرتبط بمرساة إيجابية. خسارة التصنيف $L_{cls}$ هي خسارة لوغاريتمية على صنفين (جسم مقابل ليس جسماً). بالنسبة لخسارة الانحدار، نستخدم $L_{reg}(t_i, t_i^*) = R(t_i - t_i^*)$ حيث R هي دالة الخسارة القوية (smooth L₁) المعرفة في [4]. المصطلح $p_i^* L_{reg}$ يعني أن خسارة الانحدار يتم تفعيلها فقط للمراسي الإيجابية ($p_i^* = 1$) ويتم تعطيلها خلاف ذلك ($p_i^* = 0$). تتكون مخرجات طبقتي cls وreg من {$p_i$} و{$t_i$} على التوالي.

يتم تطبيع المصطلحين بواسطة $N_{cls}$ و$N_{reg}$ ويتم وزنهما بواسطة معامل موازنة λ. في تطبيقنا الحالي (كما في الشفرة المصدرة)، يتم تطبيع مصطلح cls في المعادلة (1) بواسطة حجم الدفعة الصغيرة (أي، $N_{cls}$ = 256) ويتم تطبيع مصطلح reg بواسطة عدد مواقع المراسي (أي، $N_{reg}$ ∼ 2,400). بشكل افتراضي نضع λ = 10، وبالتالي فإن كلاً من مصطلحي cls وreg موزونان بشكل متساوٍ تقريباً. نُظهر بالتجارب أن النتائج غير حساسة لقيم λ في نطاق واسع (الجدول 9). نلاحظ أيضاً أن التطبيع كما هو أعلاه غير مطلوب ويمكن تبسيطه.

لانحدار صندوق التحديد، نعتمد تحديدات معاملات الإحداثيات الأربعة بعد [2]:

$$t_x = (x - x_a)/w_a, \\quad t_y = (y - y_a)/h_a,$$
$$t_w = \\log(w/w_a), \\quad t_h = \\log(h/h_a),$$
$$t_x^* = (x^* - x_a)/w_a, \\quad t_y^* = (y^* - y_a)/h_a,$$
$$t_w^* = \\log(w^*/w_a), \\quad t_h^* = \\log(h^*/h_a),$$

حيث x وy وw وh تشير إلى إحداثيات مركز الصندوق وعرضه وارتفاعه. المتغيرات x و$x_a$ و$x^*$ هي للصندوق المتنبأ به وصندوق المرساة وصندوق الحقيقة الأرضية على التوالي (وكذلك بالنسبة لـ y وw وh). يمكن اعتبار هذا انحدار صندوق التحديد من صندوق مرساة إلى صندوق حقيقة أرضية قريب.

ومع ذلك، تحقق طريقتنا انحدار صندوق التحديد بطريقة مختلفة عن الطرق السابقة القائمة على RoI (منطقة الاهتمام) [3]، [4]. في [3]، [4]، يتم إجراء انحدار صندوق التحديد على ميزات مجمعة من RoIs ذات أحجام تعسفية، ويتم مشاركة أوزان الانحدار بواسطة جميع أحجام المناطق. في صياغتنا، الميزات المستخدمة للانحدار لها نفس الحجم المكاني (3×3) على خرائط الميزات. لمراعاة الأحجام المتباينة، يتم تعلم مجموعة من k منحدرات صندوق التحديد. كل منحدر مسؤول عن مقياس واحد ونسبة أبعاد واحدة، ومنحدرات k لا تشارك الأوزان. على هذا النحو، لا يزال من الممكن التنبؤ بصناديق بأحجام مختلفة حتى لو كانت الميزات بحجم/مقياس ثابت، بفضل تصميم المراسي.

#### 3.1.3 تدريب شبكات RPN

يمكن تدريب RPN من طرف إلى طرف عن طريق الانتشار العكسي والانحدار التدرجي العشوائي (SGD) [35]. نتبع استراتيجية أخذ العينات "المتمركزة على الصورة" من [4] لتدريب هذه الشبكة. تنشأ كل دفعة صغيرة من صورة واحدة تحتوي على العديد من أمثلة المراسي الإيجابية والسلبية. من الممكن تحسين دوال الخسارة لجميع المراسي، لكن هذا سيميل نحو العينات السلبية لأنها مهيمنة. بدلاً من ذلك، نأخذ عينات عشوائياً من 256 مرساة في صورة لحساب دالة الخسارة لدفعة صغيرة، حيث تكون نسبة المراسي الإيجابية والسلبية المعاينة تصل إلى 1:1. إذا كان هناك أقل من 128 عينة إيجابية في صورة، نملأ الدفعة الصغيرة بعينات سلبية.

نبدأ عشوائياً جميع الطبقات الجديدة عن طريق سحب الأوزان من توزيع غاوسي بمتوسط صفر وانحراف معياري 0.01. يتم تهيئة جميع الطبقات الأخرى (أي الطبقات الالتفافية المشتركة) عن طريق التدريب المسبق لنموذج لتصنيف ImageNet [36]، كما هو ممارسة قياسية [4]. نضبط جميع طبقات شبكة ZF، ومن conv3_1 وما فوق لشبكة VGG للحفاظ على الذاكرة [4]. نستخدم معدل تعلم 0.001 لـ 60k دفعة صغيرة، و0.0001 للـ 20k دفعة صغيرة التالية على مجموعة بيانات PASCAL VOC. نستخدم زخماً قدره 0.9 وتحلل وزن قدره 0.0005 [38]. يستخدم تطبيقنا Caffe [39].

### 3.2 مشاركة الميزات لـ RPN وFast R-CNN

حتى الآن وصفنا كيفية تدريب شبكة لتوليد اقتراح المناطق، دون النظر في CNN لكشف الأجسام القائم على المناطق الذي سيستخدم هذه الاقتراحات. بالنسبة لشبكة الكشف، نعتمد Fast R-CNN [4]. بعد ذلك نصف خوارزميات تتعلم شبكة موحدة تتكون من RPN وFast R-CNN مع طبقات التفافية مشتركة (الشكل 2).

سوف تعدل كل من RPN وFast R-CNN، عند تدريبهما بشكل مستقل، طبقاتهما الالتفافية بطرق مختلفة. لذلك نحتاج إلى تطوير تقنية تسمح بمشاركة الطبقات الالتفافية بين الشبكتين، بدلاً من تعلم شبكتين منفصلتين. نناقش ثلاث طرق لتدريب الشبكات مع ميزات مشتركة:

**(i) التدريب المتناوب.** في هذا الحل، نقوم أولاً بتدريب RPN، ونستخدم الاقتراحات لتدريب Fast R-CNN. ثم تُستخدم الشبكة المضبوطة بواسطة Fast R-CNN لتهيئة RPN، وتتكرر هذه العملية. هذا هو الحل المستخدم في جميع التجارب في هذه الورقة.

**(ii) التدريب المشترك التقريبي.** في هذا الحل، يتم دمج شبكات RPN وFast R-CNN في شبكة واحدة أثناء التدريب كما في الشكل 2. في كل تكرار SGD، يولد الممر الأمامي اقتراحات المناطق التي تُعامل تماماً مثل الاقتراحات الثابتة المحسوبة مسبقاً عند تدريب كاشف Fast R-CNN. يحدث الانتشار العكسي كالمعتاد، حيث بالنسبة للطبقات المشتركة يتم دمج إشارات الانتشار العكسي من كل من خسارة RPN وخسارة Fast R-CNN. هذا الحل سهل التنفيذ. لكن هذا الحل يتجاهل المشتقة فيما يتعلق بإحداثيات صناديق الاقتراح التي هي أيضاً استجابات الشبكة، لذا فهو تقريبي. في تجاربنا، وجدنا تجريبياً أن هذا الحل ينتج نتائج قريبة، لكنه يقلل من وقت التدريب بحوالي 25-50٪ مقارنة بالتدريب المتناوب. هذا الحل مدرج في شفرة Python المصدرة لدينا.

**(iii) التدريب المشترك غير التقريبي.** كما نوقش أعلاه، صناديق التحديد المتنبأ بها بواسطة RPN هي أيضاً دوال للمدخل. تقبل طبقة تجميع RoI [4] في Fast R-CNN الميزات الالتفافية وأيضاً صناديق التحديد المتنبأ بها كمدخل، لذا يجب أن يتضمن حل الانتشار العكسي الصحيح نظرياً أيضاً تدرجات فيما يتعلق بإحداثيات الصندوق. يتم تجاهل هذه التدرجات في التدريب المشترك التقريبي أعلاه. في حل التدريب المشترك غير التقريبي، نحتاج إلى طبقة تجميع RoI قابلة للتفاضل فيما يتعلق بإحداثيات الصندوق. هذه مشكلة غير تافهة ويمكن تقديم حل بواسطة طبقة "تشويه RoI" كما تم تطويره في [15]، وهو ما يتجاوز نطاق هذه الورقة.

**التدريب المتناوب من 4 خطوات.** في هذه الورقة، نعتمد خوارزمية تدريب عملية من 4 خطوات لتعلم ميزات مشتركة عبر التحسين المتناوب. في الخطوة الأولى، نقوم بتدريب RPN كما هو موضح في القسم 3.1.3. يتم تهيئة هذه الشبكة بنموذج مدرب مسبقاً على ImageNet ويتم ضبطها بدقة من طرف إلى طرف لمهمة اقتراح المناطق. في الخطوة الثانية، نقوم بتدريب شبكة كشف منفصلة بواسطة Fast R-CNN باستخدام الاقتراحات المولدة بواسطة RPN من الخطوة 1. يتم أيضاً تهيئة شبكة الكشف هذه بواسطة نموذج مدرب مسبقاً على ImageNet. في هذه المرحلة، لا تشترك الشبكتان في طبقات التفافية. في الخطوة الثالثة، نستخدم شبكة الكاشف لتهيئة تدريب RPN، لكننا نثبت الطبقات الالتفافية المشتركة ونضبط بدقة فقط الطبقات الفريدة لـ RPN. الآن تشترك الشبكتان في طبقات التفافية. في الخطوة الرابعة، مع الحفاظ على الطبقات الالتفافية المشتركة ثابتة، نضبط بدقة الطبقات الفريدة لـ Fast R-CNN. على هذا النحو، تشترك كلتا الشبكتين في نفس الطبقات الالتفافية وتشكلان شبكة موحدة. يمكن تشغيل تدريب متناوب مماثل لمزيد من التكرارات، لكننا لاحظنا تحسينات ضئيلة.

### 3.3 تفاصيل التطبيق

لكل من التدريب والاختبار، نعتمد صور بمقياس واحد كما هو موضح أعلاه. نعيد قياس الصور بحيث يكون جانبها الأقصر s = 600 بكسل [4]. قد يحسن استخراج الميزات متعدد المقاييس (باستخدام هرم صور) من الدقة ولكن لا يُظهر توازناً جيداً بين السرعة والدقة [4]. على الصور المعاد قياسها، يكون إجمالي الخطوة لكل من شبكات ZF وVGG على آخر طبقة التفافية 16 بكسل، وبالتالي يكون ∼10 بكسل على صورة PASCAL نموذجية قبل تغيير الحجم (∼500×375). حتى مثل هذه الخطوة الكبيرة توفر نتائج جيدة، على الرغم من أن الدقة قد تتحسن أكثر مع خطوة أصغر.

بالنسبة للمراسي، نستخدم 3 مقاييس بمساحات صناديق 128² و256² و512² بكسل، و3 نسب أبعاد 1:1 و1:2 و2:1. لم يتم اختيار هذه المعاملات الفائقة بعناية لمجموعة بيانات معينة، ونقدم تجارب استئصالية على تأثيراتها في القسم 4. كما نوقش، لا يحتاج حلنا إلى هرم صور أو هرم مرشحات للتنبؤ بمناطق بمقاييس متعددة، مما يوفر وقت تشغيل كبير. يُظهر الشكل 1 (يمين) قدرة طريقتنا على نطاق واسع من المقاييس ونسب الأبعاد. يُظهر الجدول 1 متوسط حجم الاقتراح المتعلم لكل مرساة باستخدام شبكة ZF. نلاحظ أن خوارزميتنا تسمح بتنبؤات أكبر من المجال الاستقبالي الأساسي. مثل هذه التنبؤات ليست مستحيلة - قد لا يزال المرء يستنتج تقريباً امتداد جسم إذا كان منتصف الجسم فقط مرئياً.

صناديق المراسي التي تتجاوز حدود الصورة يجب التعامل معها بعناية. أثناء التدريب، نتجاهل جميع المراسي المتجاوزة للحدود حتى لا تساهم في الخسارة. بالنسبة لصورة نموذجية 1000×600، سيكون هناك حوالي 20k (≈60×40×9) مرساة إجمالاً. مع تجاهل المراسي المتجاوزة للحدود، هناك حوالي 6k مرساة لكل صورة للتدريب. إذا لم يتم تجاهل القيم المتطرفة المتجاوزة للحدود في التدريب، فإنها تُدخل مصطلحات خطأ كبيرة يصعب تصحيحها في الهدف، ولا يتقارب التدريب. أثناء الاختبار، مع ذلك، لا نزال نطبق RPN الالتفافية بالكامل على الصورة بأكملها. قد يولد هذا صناديق اقتراح متجاوزة للحدود، والتي نقصها إلى حدود الصورة.

بعض اقتراحات RPN تتداخل بشكل كبير مع بعضها البعض. لتقليل التكرار، نعتمد قمع غير الحد الأقصى (NMS) على مناطق الاقتراح بناءً على درجات cls الخاصة بها. نثبت عتبة IoU لـ NMS عند 0.7، مما يترك لنا حوالي 2000 منطقة اقتراح لكل صورة. كما سنُظهر، لا يضر NMS بدقة الكشف النهائية، لكنه يقلل بشكل كبير من عدد الاقتراحات. بعد NMS، نستخدم أعلى N من مناطق الاقتراح المصنفة للكشف. في ما يلي، نقوم بتدريب Fast R-CNN باستخدام 2000 اقتراح RPN، لكننا نقيّم أعداداً مختلفة من الاقتراحات في وقت الاختبار.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2, Figure 3
- **Tables referenced:** Table 1, Table 8, Table 9
- **Key terms introduced:**
  - Region Proposal Network (RPN) = شبكة اقتراح المناطق
  - Anchor = المرساة/المراسي
  - Objectness score = درجة وجود الجسم
  - Translation-invariant = غير متغير بالإزاحة
  - Receptive field = المجال الاستقبالي
  - Intersection-over-Union (IoU) = تقاطع على اتحاد
  - Ground-truth = الحقيقة الأرضية
  - Mini-batch = دفعة صغيرة
  - Non-maximum suppression (NMS) = قمع غير الحد الأقصى
  - Alternating training = التدريب المتناوب
  - Feature sharing = مشاركة الميزات
- **Equations:** 3 main equations (loss function, bounding box parameterization)
- **Citations:** [1-39] referenced
- **Special handling:**
  - All mathematical equations preserved in LaTeX format
  - Network names preserved: ZF, VGG-16, Fast R-CNN, GoogleNet
  - "End-to-end" = من طرف إلى طرف
  - "Fully convolutional" = التفافية بالكامل
  - "Bounding box regression" = انحدار صندوق التحديد
  - ReLU preserved as ReLU (standard in Arabic technical writing)
  - Caffe preserved as Caffe
  - "Smooth L₁" preserved with subscript

### Quality Metrics

- Semantic equivalence: 0.88 (preserves all technical details and mathematical formulations)
- Technical accuracy: 0.87 (correct terminology for deep learning and computer vision)
- Readability: 0.86 (maintains academic flow despite complexity)
- Glossary consistency: 0.87 (consistent use of established terms)
- **Overall section score:** 0.87

### Back-Translation Check (Key Technical Sentence)

Original: "At each sliding-window location, we simultaneously predict multiple region proposals, where the number of maximum possible proposals for each location is denoted as k."

Arabic: في كل موقع نافذة منزلقة، نتنبأ في آن واحد باقتراحات مناطق متعددة، حيث يُشار إلى عدد الاقتراحات القصوى الممكنة لكل موقع بـ k.

Back-translation: "At each sliding window location, we simultaneously predict multiple region proposals, where the number of maximum possible proposals for each location is denoted as k."

✓ Semantic match confirmed
