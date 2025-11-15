# Section 2: Unified Detection
## القسم 2: الكشف الموحد

**Section:** unified-detection
**Translation Quality:** 0.87
**Glossary Terms Used:** neural network, bounding box, grid cell, confidence score, IOU, ground truth, conditional probability, tensor, convolutional layers, fully connected layers, pretrain, loss function, sum-squared error, learning rate, dropout, data augmentation, overfitting, non-maximal suppression, activation function, gradient, batch size, momentum, decay

---

### English Version

We unify the separate components of object detection into a single neural network. Our network uses features from the entire image to predict each bounding box. It also predicts all bounding boxes across all classes for an image simultaneously. This means our network reasons globally about the full image and all the objects in the image. The YOLO design enables end-to-end training and real-time speeds while maintaining high average precision.

Our system divides the input image into an S×S grid. If the center of an object falls into a grid cell, that grid cell is responsible for detecting that object.

Each grid cell predicts B bounding boxes and confidence scores for those boxes. These confidence scores reflect how confident the model is that the box contains an object and also how accurate it thinks the box is that it predicts. Formally we define confidence as Pr(Object)∗IOU_pred^truth. If no object exists in that cell, the confidence scores should be zero. Otherwise we want the confidence score to equal the intersection over union (IOU) between the predicted box and the ground truth.

Each bounding box consists of 5 predictions: x, y, w, h, and confidence. The (x,y) coordinates represent the center of the box relative to the bounds of the grid cell. The width and height are predicted relative to the whole image. Finally the confidence prediction represents the IOU between the predicted box and any ground truth box.

Each grid cell also predicts C conditional class probabilities, Pr(Class_i|Object). These probabilities are conditioned on the grid cell containing an object. We only predict one set of class probabilities per grid cell, regardless of the number of boxes B.

At test time we multiply the conditional class probabilities and the individual box confidence predictions,

$$\text{Pr}(\text{Class}_i|\text{Object}) \ast \text{Pr}(\text{Object}) \ast \text{IOU}_{\text{pred}}^{\text{truth}} = \text{Pr}(\text{Class}_i) \ast \text{IOU}_{\text{pred}}^{\text{truth}}$$

(1)

which gives us class-specific confidence scores for each box. These scores encode both the probability of that class appearing in the box and how well the predicted box fits the object.

For evaluating YOLO on Pascal VOC, we use S=7, B=2. Pascal VOC has 20 labelled classes so C=20. Our final prediction is a 7×7×30 tensor.

#### 2.1 Network Design

We implement this model as a convolutional neural network and evaluate it on the Pascal VOC detection dataset. The initial convolutional layers of the network extract features from the image while the fully connected layers predict the output probabilities and coordinates.

Our network architecture is inspired by the GoogLeNet model for image classification. Our network has 24 convolutional layers followed by 2 fully connected layers. Instead of the inception modules used by GoogLeNet, we simply use 1×1 reduction layers followed by 3×3 convolutional layers, similar to Lin et al. The full network is shown in Figure 3.

We also train a fast version of YOLO designed to push the boundaries of fast object detection. Fast YOLO uses a neural network with fewer convolutional layers (9 instead of 24) and fewer filters in those layers. Other than the size of the network, all training and testing parameters are the same between YOLO and Fast YOLO.

The final output of our network is the 7×7×30 tensor of predictions.

#### 2.2 Training

We pretrain our convolutional layers on the ImageNet 1000-class competition dataset. For pretraining we use the first 20 convolutional layers from Figure 3 followed by a average-pooling layer and a fully connected layer. We train this network for approximately a week and achieve a single crop top-5 accuracy of 88% on the ImageNet 2012 validation set, comparable to the GoogLeNet models in Caffe's Model Zoo. We use the Darknet framework for all training and inference.

We then convert the model to perform detection. Ren et al. show that adding both convolutional and connected layers to pretrained networks can improve performance. Following their example, we add four convolutional layers and two fully connected layers with randomly initialized weights. Detection often requires fine-grained visual information so we increase the input resolution of the network from 224×224 to 448×448.

Our final layer predicts both class probabilities and bounding box coordinates. We normalize the bounding box width and height by the image width and height so that they fall between 0 and 1. We parametrize the bounding box x and y coordinates to be offsets of a particular grid cell location so they are also bounded between 0 and 1.

We use a linear activation function for the final layer and all other layers use the following leaky rectified linear activation:

$$\phi(x) = \begin{cases} x, & \text{if } x > 0 \\ 0.1x, & \text{otherwise} \end{cases}$$

(2)

We optimize for sum-squared error in the output of our model. We use sum-squared error because it is easy to optimize, however it does not perfectly align with our goal of maximizing average precision. It weights localization error equally with classification error which may not be ideal. Also, in every image many grid cells do not contain any object. This pushes the "confidence" scores of those cells towards zero, often overpowering the gradient from cells that do contain objects. This can lead to model instability, causing training to diverge early on.

To remedy this, we increase the loss from bounding box coordinate predictions and decrease the loss from confidence predictions for boxes that don't contain objects. We use two parameters, λ_coord and λ_noobj to accomplish this. We set λ_coord=5 and λ_noobj=0.5.

Sum-squared error also equally weights errors in large boxes and small boxes. Our error metric should reflect that small deviations in large boxes matter less than in small boxes. To partially address this we predict the square root of the bounding box width and height instead of the width and height directly.

YOLO predicts multiple bounding boxes per grid cell. At training time we only want one bounding box predictor to be responsible for each object. We assign one predictor to be "responsible" for predicting an object based on which prediction has the highest current IOU with the ground truth. This leads to specialization between the bounding box predictors. Each predictor gets better at predicting certain sizes, aspect ratios, or classes of object, improving overall recall.

During training we optimize the following, multi-part loss function:

$$\lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}} [(x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2]$$

$$+ \lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}} [(\sqrt{w_i} - \sqrt{\hat{w}_i})^2 + (\sqrt{h_i} - \sqrt{\hat{h}_i})^2]$$

$$+ \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}} (C_i - \hat{C}_i)^2$$

$$+ \lambda_{\text{noobj}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{noobj}} (C_i - \hat{C}_i)^2$$

$$+ \sum_{i=0}^{S^2} \mathbb{1}_{i}^{\text{obj}} \sum_{c \in \text{classes}} (p_i(c) - \hat{p}_i(c))^2$$

(3)

where 𝟙_i^obj denotes if object appears in cell i and 𝟙_ij^obj denotes that the jth bounding box predictor in cell i is "responsible" for that prediction.

Note that the loss function only penalizes classification error if an object is present in that grid cell (hence the conditional class probability discussed earlier). It also only penalizes bounding box coordinate error if that predictor is "responsible" for the ground truth box (i.e. has the highest IOU of any predictor in that grid cell).

We train the network for about 135 epochs on the training and validation data sets from Pascal VOC 2007 and 2012. When testing on 2012 we also include the VOC 2007 test data for training. Throughout training we use a batch size of 64, a momentum of 0.9 and a decay of 0.0005.

Our learning rate schedule is as follows: For the first epochs we slowly raise the learning rate from 10^-3 to 10^-2. If we start at a high learning rate our model often diverges due to unstable gradients. We continue training with 10^-2 for 75 epochs, then 10^-3 for 30 epochs, and finally 10^-4 for 30 epochs.

To avoid overfitting we use dropout and extensive data augmentation. A dropout layer with rate = 0.5 after the first connected layer prevents co-adaptation between layers. For data augmentation we introduce random scaling and translations of up to 20% of the original image size. We also randomly adjust the exposure and saturation of the image by up to a factor of 1.5 in the HSV color space.

#### 2.3 Inference

Just like in training, predicting detections for a test image only requires one network evaluation. On Pascal VOC the network predicts 98 bounding boxes per image and class probabilities for each box. YOLO is extremely fast at test time since it only requires a single network evaluation, unlike classifier-based methods.

The grid design enforces spatial diversity in the bounding box predictions. Often it is clear which grid cell an object falls in to and the network only predicts one box for each object. However, some large objects or objects near the border of multiple cells can be well localized by multiple cells. Non-maximal suppression can be used to fix these multiple detections. While not critical to performance as it is for R-CNN or DPM, non-maximal suppression adds 2-3% in mAP.

#### 2.4 Limitations of YOLO

YOLO imposes strong spatial constraints on bounding box predictions since each grid cell only predicts two boxes and can only have one class. This spatial constraint limits the number of nearby objects that our model can predict. Our model struggles with small objects that appear in groups, such as flocks of birds.

Since our model learns to predict bounding boxes from data, it struggles to generalize to objects in new or unusual aspect ratios or configurations. Our model also uses relatively coarse features for predicting bounding boxes since our architecture has multiple downsampling layers from the input image.

Finally, while we train on a loss function that approximates detection performance, our loss function treats errors the same in small bounding boxes versus large bounding boxes. A small error in a large box is generally benign but a small error in a small box has a much greater effect on IOU. Our main source of error is incorrect localizations.

---

### النسخة العربية

نوحد المكونات المنفصلة لكشف الأجسام في شبكة عصبية واحدة. تستخدم شبكتنا ميزات من الصورة بأكملها للتنبؤ بكل صندوق تحديد. كما تتنبأ بجميع صناديق التحديد عبر جميع الفئات للصورة في وقت واحد. هذا يعني أن شبكتنا تستدل بشكل شامل حول الصورة الكاملة وجميع الأجسام في الصورة. يتيح تصميم YOLO التدريب من البداية للنهاية والسرعات في الوقت الفعلي مع الحفاظ على متوسط دقة عالٍ.

يقسم نظامنا صورة الإدخال إلى شبكة بحجم S×S. إذا وقع مركز جسم ما في خلية شبكة، فإن تلك الخلية تكون مسؤولة عن اكتشاف ذلك الجسم.

تتنبأ كل خلية شبكة بـ B صندوق تحديد ودرجات ثقة لتلك الصناديق. تعكس درجات الثقة هذه مدى ثقة النموذج بأن الصندوق يحتوي على جسم ومدى دقة الصندوق الذي يتنبأ به. نعرف الثقة رسمياً بأنها Pr(Object)∗IOU_pred^truth. إذا لم يكن هناك جسم في تلك الخلية، يجب أن تكون درجات الثقة صفراً. وإلا فإننا نريد أن تساوي درجة الثقة التقاطع على الاتحاد (IOU) بين الصندوق المتنبأ به والحقيقة الأرضية.

يتكون كل صندوق تحديد من 5 تنبؤات: x, y, w, h، والثقة. تمثل إحداثيات (x,y) مركز الصندوق نسبة إلى حدود خلية الشبكة. يتم التنبؤ بالعرض والارتفاع نسبة إلى الصورة بأكملها. أخيراً، يمثل التنبؤ بالثقة IOU بين الصندوق المتنبأ به وأي صندوق حقيقة أرضية.

تتنبأ كل خلية شبكة أيضاً بـ C احتمالية فئة شرطية، Pr(Class_i|Object). تكون هذه الاحتماليات مشروطة بأن خلية الشبكة تحتوي على جسم. نتنبأ فقط بمجموعة واحدة من احتماليات الفئة لكل خلية شبكة، بغض النظر عن عدد الصناديق B.

في وقت الاختبار نضرب احتماليات الفئة الشرطية وتنبؤات ثقة الصندوق الفردية،

$$\text{Pr}(\text{Class}_i|\text{Object}) \ast \text{Pr}(\text{Object}) \ast \text{IOU}_{\text{pred}}^{\text{truth}} = \text{Pr}(\text{Class}_i) \ast \text{IOU}_{\text{pred}}^{\text{truth}}$$

(1)

مما يعطينا درجات ثقة خاصة بالفئة لكل صندوق. تشفر هذه الدرجات كلاً من احتمالية ظهور تلك الفئة في الصندوق ومدى ملاءمة الصندوق المتنبأ به للجسم.

لتقييم YOLO على Pascal VOC، نستخدم S=7، B=2. تحتوي Pascal VOC على 20 فئة مُصنفة لذلك C=20. تنبؤنا النهائي هو موتر بحجم 7×7×30.

#### 2.1 تصميم الشبكة

ننفذ هذا النموذج كشبكة عصبية التفافية ونقيمه على مجموعة بيانات الكشف Pascal VOC. تستخرج الطبقات الالتفافية الأولى من الشبكة الميزات من الصورة بينما تتنبأ الطبقات المتصلة بالكامل بالاحتماليات والإحداثيات الناتجة.

معمارية شبكتنا مستوحاة من نموذج GoogLeNet لتصنيف الصور. تحتوي شبكتنا على 24 طبقة التفافية متبوعة بطبقتين متصلتين بالكامل. بدلاً من وحدات الإنشاء (inception) المستخدمة في GoogLeNet، نستخدم ببساطة طبقات تخفيض 1×1 متبوعة بطبقات التفافية 3×3، مشابهة لـ Lin وآخرون. يظهر الشبكة الكاملة في الشكل 3.

نقوم أيضاً بتدريب نسخة سريعة من YOLO مصممة لدفع حدود الكشف السريع عن الأجسام. يستخدم Fast YOLO شبكة عصبية بطبقات التفافية أقل (9 بدلاً من 24) ومرشحات أقل في تلك الطبقات. بخلاف حجم الشبكة، جميع معاملات التدريب والاختبار هي نفسها بين YOLO وFast YOLO.

الناتج النهائي لشبكتنا هو موتر التنبؤات بحجم 7×7×30.

#### 2.2 التدريب

نقوم بالتدريب المسبق لطبقاتنا الالتفافية على مجموعة بيانات مسابقة ImageNet لـ 1000 فئة. للتدريب المسبق نستخدم أول 20 طبقة التفافية من الشكل 3 متبوعة بطبقة تجميع متوسط وطبقة متصلة بالكامل. نقوم بتدريب هذه الشبكة لمدة أسبوع تقريباً ونحقق دقة top-5 بنسبة 88% لقطع واحد على مجموعة التحقق ImageNet 2012، مقارنة بنماذج GoogLeNet في Caffe's Model Zoo. نستخدم إطار عمل Darknet لجميع التدريب والاستنتاج.

ثم نحول النموذج لأداء الكشف. أظهر Ren وآخرون أن إضافة طبقات التفافية ومتصلة إلى الشبكات المدربة مسبقاً يمكن أن يحسن الأداء. متبعين مثالهم، نضيف أربع طبقات التفافية وطبقتين متصلتين بالكامل بأوزان مهيأة عشوائياً. غالباً ما يتطلب الكشف معلومات بصرية دقيقة التفاصيل لذلك نزيد دقة إدخال الشبكة من 224×224 إلى 448×448.

تتنبأ طبقتنا النهائية بكل من احتماليات الفئة وإحداثيات صندوق التحديد. نقوم بتطبيع عرض وارتفاع صندوق التحديد حسب عرض وارتفاع الصورة بحيث تقع بين 0 و1. نحدد معاملات إحداثيات x وy لصندوق التحديد لتكون إزاحات لموقع خلية شبكة معينة بحيث تكون أيضاً محدودة بين 0 و1.

نستخدم دالة تنشيط خطية للطبقة النهائية وجميع الطبقات الأخرى تستخدم تنشيط خطي مصحح متسرب التالي:

$$\phi(x) = \begin{cases} x, & \text{إذا } x > 0 \\ 0.1x, & \text{خلاف ذلك} \end{cases}$$

(2)

نحسّن لخطأ مجموع المربعات في ناتج نموذجنا. نستخدم خطأ مجموع المربعات لأنه سهل التحسين، ومع ذلك فإنه لا يتماشى تماماً مع هدفنا المتمثل في تعظيم متوسط الدقة. إنه يوازن خطأ التحديد الموضعي بشكل متساوٍ مع خطأ التصنيف وهو ما قد لا يكون مثالياً. أيضاً، في كل صورة العديد من خلايا الشبكة لا تحتوي على أي جسم. يدفع هذا درجات "الثقة" لتلك الخلايا نحو الصفر، غالباً ما يتغلب على التدرج من الخلايا التي تحتوي على أجسام. يمكن أن يؤدي هذا إلى عدم استقرار النموذج، مما يتسبب في تباعد التدريب في وقت مبكر.

لمعالجة ذلك، نزيد الخسارة من تنبؤات إحداثيات صندوق التحديد ونقلل الخسارة من تنبؤات الثقة للصناديق التي لا تحتوي على أجسام. نستخدم معاملين، λ_coord وλ_noobj لتحقيق ذلك. نضبط λ_coord=5 وλ_noobj=0.5.

يوازن خطأ مجموع المربعات أيضاً الأخطاء في الصناديق الكبيرة والصناديق الصغيرة بشكل متساوٍ. يجب أن يعكس مقياس الخطأ لدينا أن الانحرافات الصغيرة في الصناديق الكبيرة أقل أهمية منها في الصناديق الصغيرة. لمعالجة هذا جزئياً نتنبأ بالجذر التربيعي لعرض وارتفاع صندوق التحديد بدلاً من العرض والارتفاع مباشرة.

يتنبأ YOLO بصناديق تحديد متعددة لكل خلية شبكة. في وقت التدريب نريد فقط أن يكون متنبئ صندوق تحديد واحد مسؤولاً عن كل جسم. نعيّن متنبئاً واحداً ليكون "مسؤولاً" عن التنبؤ بجسم بناءً على التنبؤ الذي لديه أعلى IOU حالي مع الحقيقة الأرضية. يؤدي هذا إلى تخصص بين متنبئي صناديق التحديد. يصبح كل متنبئ أفضل في التنبؤ بأحجام أو نسب أبعاد أو فئات معينة من الأجسام، مما يحسن الاستدعاء الإجمالي.

أثناء التدريب نحسّن دالة الخسارة متعددة الأجزاء التالية:

$$\lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}} [(x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2]$$

$$+ \lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}} [(\sqrt{w_i} - \sqrt{\hat{w}_i})^2 + (\sqrt{h_i} - \sqrt{\hat{h}_i})^2]$$

$$+ \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}} (C_i - \hat{C}_i)^2$$

$$+ \lambda_{\text{noobj}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{noobj}} (C_i - \hat{C}_i)^2$$

$$+ \sum_{i=0}^{S^2} \mathbb{1}_{i}^{\text{obj}} \sum_{c \in \text{classes}} (p_i(c) - \hat{p}_i(c))^2$$

(3)

حيث 𝟙_i^obj يشير إلى ما إذا كان جسم يظهر في الخلية i و𝟙_ij^obj يشير إلى أن متنبئ صندوق التحديد الـ j في الخلية i "مسؤول" عن ذلك التنبؤ.

لاحظ أن دالة الخسارة تعاقب فقط على خطأ التصنيف إذا كان هناك جسم موجود في خلية الشبكة تلك (ومن هنا احتمالية الفئة الشرطية التي تمت مناقشتها سابقاً). كما أنها تعاقب فقط على خطأ إحداثيات صندوق التحديد إذا كان ذلك المتنبئ "مسؤولاً" عن صندوق الحقيقة الأرضية (أي لديه أعلى IOU من أي متنبئ في تلك خلية الشبكة).

نقوم بتدريب الشبكة لحوالي 135 حقبة على مجموعات بيانات التدريب والتحقق من Pascal VOC 2007 و2012. عند الاختبار على 2012 نضمن أيضاً بيانات اختبار VOC 2007 للتدريب. طوال التدريب نستخدم حجم دفعة 64، وزخم 0.9، وتلاشي 0.0005.

جدول معدل التعلم لدينا كالتالي: للحقب الأولى نرفع معدل التعلم ببطء من 10^-3 إلى 10^-2. إذا بدأنا بمعدل تعلم مرتفع، فإن نموذجنا غالباً ما يتباعد بسبب التدرجات غير المستقرة. نستمر في التدريب بـ 10^-2 لمدة 75 حقبة، ثم 10^-3 لمدة 30 حقبة، وأخيراً 10^-4 لمدة 30 حقبة.

لتجنب الإفراط في التلاؤم نستخدم dropout وزيادة بيانات واسعة. طبقة dropout بمعدل = 0.5 بعد الطبقة المتصلة الأولى تمنع التكيف المشترك بين الطبقات. لزيادة البيانات نقدم تحجيماً وترجمات عشوائية تصل إلى 20% من حجم الصورة الأصلي. نقوم أيضاً بضبط التعرض والتشبع للصورة بشكل عشوائي بعامل يصل إلى 1.5 في فضاء ألوان HSV.

#### 2.3 الاستنتاج

تماماً كما في التدريب، يتطلب التنبؤ بالكشوفات لصورة اختبار تقييم شبكة واحد فقط. على Pascal VOC تتنبأ الشبكة بـ 98 صندوق تحديد لكل صورة واحتماليات الفئة لكل صندوق. YOLO سريع للغاية في وقت الاختبار لأنه يتطلب تقييم شبكة واحد فقط، على عكس الطرق القائمة على المصنفات.

يفرض تصميم الشبكة تنوعاً مكانياً في تنبؤات صندوق التحديد. غالباً ما يكون واضحاً في أي خلية شبكة يقع الجسم وتتنبأ الشبكة فقط بصندوق واحد لكل جسم. ومع ذلك، يمكن تحديد موقع بعض الأجسام الكبيرة أو الأجسام القريبة من حدود خلايا متعددة بشكل جيد بواسطة خلايا متعددة. يمكن استخدام قمع غير الأعظمي لإصلاح هذه الكشوفات المتعددة. بينما ليس حرجاً للأداء كما هو الحال في R-CNN أو DPM، يضيف قمع غير الأعظمي 2-3% في mAP.

#### 2.4 قيود YOLO

يفرض YOLO قيوداً مكانية قوية على تنبؤات صندوق التحديد نظراً لأن كل خلية شبكة تتنبأ فقط بصندوقين ويمكن أن يكون لها فئة واحدة فقط. يحد هذا القيد المكاني من عدد الأجسام القريبة التي يمكن لنموذجنا التنبؤ بها. يواجه نموذجنا صعوبة مع الأجسام الصغيرة التي تظهر في مجموعات، مثل أسراب الطيور.

نظراً لأن نموذجنا يتعلم التنبؤ بصناديق التحديد من البيانات، فإنه يواجه صعوبة في التعميم على الأجسام في نسب أبعاد أو تكوينات جديدة أو غير عادية. يستخدم نموذجنا أيضاً ميزات خشنة نسبياً للتنبؤ بصناديق التحديد نظراً لأن معماريتنا تحتوي على طبقات تقليل عينات متعددة من صورة الإدخال.

أخيراً، بينما نتدرب على دالة خسارة تقارب أداء الكشف، تعامل دالة الخسارة لدينا الأخطاء بنفس الطريقة في صناديق التحديد الصغيرة مقابل صناديق التحديد الكبيرة. الخطأ الصغير في صندوق كبير عموماً غير ضار ولكن الخطأ الصغير في صندوق صغير له تأثير أكبر بكثير على IOU. مصدر الخطأ الرئيسي لدينا هو التحديدات الموضعية غير الصحيحة.

---

### Translation Notes

- **Figures referenced:** Figure 2 (Detection Model), Figure 3 (Network Architecture)
- **Key terms introduced:** grid cell, confidence score, IOU, conditional class probability, tensor, network design, pretraining, loss function, leaky ReLU, non-maximal suppression
- **Equations:** 3 major equations (confidence calculation, leaky ReLU activation, multi-part loss function)
- **Datasets mentioned:** Pascal VOC 2007, Pascal VOC 2012, ImageNet
- **Technical details:** S=7, B=2, C=20, 7×7×30 tensor, 24 convolutional layers, 2 FC layers, 135 epochs, batch size 64
- **Special handling:** Preserved all mathematical notation, kept framework names (Darknet, Caffe), maintained equation formatting

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
