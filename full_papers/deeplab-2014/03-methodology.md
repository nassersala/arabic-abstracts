# Section 3: Convolutional Neural Networks for Dense Image Labeling
## القسم 3: الشبكات العصبية الالتفافية لوسم الصور الكثيف

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** convolutional neural network, dense, feature extraction, semantic segmentation, sliding window, max-pooling, subsampling, stride, convolutional filter, feature maps, fine-tuning, loss function, cross-entropy, bilinear interpolation, receptive field

---

### English Version

Herein we describe how we have re-purposed and finetuned the publicly available Imagenet-pretrained state-of-art 16-layer classification network of (Simonyan & Zisserman, 2014) (VGG-16) into an efficient and effective dense feature extractor for our dense semantic image segmentation system.

## 3.1 Efficient Dense Sliding Window Feature Extraction with the Hole Algorithm

Dense spatial score evaluation is instrumental in the success of our dense CNN feature extractor. As a first step to implement this, we convert the fully-connected layers of VGG-16 into convolutional ones and run the network in a convolutional fashion on the image at its original resolution. However this is not enough as it yields very sparsely computed detection scores (with a stride of 32 pixels). To compute scores more densely at our target stride of 8 pixels, we develop a variation of the method previously employed by Giusti et al. (2013); Sermanet et al. (2013). We skip subsampling after the last two max-pooling layers in the network of Simonyan & Zisserman (2014) and modify the convolutional filters in the layers that follow them by introducing zeros to increase their length (2× in the last three convolutional layers and 4× in the first fully connected layer). We can implement this more efficiently by keeping the filters intact and instead sparsely sample the feature maps on which they are applied on using an input stride of 2 or 4 pixels, respectively. This approach, illustrated in Fig. 1 is known as the 'hole algorithm' ('atrous algorithm') and has been developed before for efficient computation of the undecimated wavelet transform (Mallat, 1999). We have implemented this within the Caffe framework (Jia et al., 2014) by adding to the im2col function (it converts multi-channel feature maps to vectorized patches) the option to sparsely sample the underlying feature map. This approach is generally applicable and allows us to efficiently compute dense CNN feature maps at any target subsampling rate without introducing any approximations.

We finetune the model weights of the Imagenet-pretrained VGG-16 network to adapt it to the image classification task in a straightforward fashion, following the procedure of Long et al. (2014). We replace the 1000-way Imagenet classifier in the last layer of VGG-16 with a 21-way one. Our loss function is the sum of cross-entropy terms for each spatial position in the CNN output map (subsampled by 8 compared to the original image). All positions and labels are equally weighted in the overall loss function. Our targets are the ground truth labels (subsampled by 8). We optimize the objective function with respect to the weights at all network layers by the standard SGD procedure of Krizhevsky et al. (2013).

During testing, we need class score maps at the original image resolution. As illustrated in Figure 2 and further elaborated in Section 4.1, the class score maps (corresponding to log-probabilities) are quite smooth, which allows us to use simple bilinear interpolation to increase their resolution by a factor of 8 at a negligible computational cost. Note that the method of Long et al. (2014) does not use the hole algorithm and produces very coarse scores (subsampled by a factor of 32) at the CNN output. This forced them to use learned upsampling layers, significantly increasing the complexity and training time of their system: Fine-tuning our network on PASCAL VOC 2012 takes about 10 hours, while they report a training time of several days (both timings on a modern GPU).

## 3.2 Controlling the Receptive Field Size and Accelerating Dense Computation with Convolutional Nets

Another key ingredient in re-purposing our network for dense score computation is explicitly controlling the network's receptive field size. Most recent DCNN-based image recognition methods rely on networks pre-trained on the Imagenet large-scale classification task. These networks typically have large receptive field size: in the case of the VGG-16 net we consider, its receptive field is 224 × 224 (with zero-padding) and 404 × 404 pixels if the net is applied convolutionally. After converting the network to a fully convolutional one, the first fully connected layer has 4,096 filters of large 7 × 7 spatial size and becomes the computational bottleneck in our dense score map computation.

We have addressed this practical problem by spatially subsampling (by simple decimation) the first FC layer to 4×4 (or 3×3) spatial size. This has reduced the receptive field of the network down to 128×128 (with zero-padding) or 308×308 (in convolutional mode) and has reduced computation time for the first FC layer by 2-3 times. Using our Caffe-based implementation and a Titan GPU, the resulting VGG-derived network is very efficient: Given a 306×306 input image, it produces 39×39 dense raw feature scores at the top of the network at a rate of about 8 frames/sec during testing. The speed during training is 3 frames/sec. We have also successfully experimented with reducing the number of channels at the fully connected layers from 4,096 down to 1,024, considerably further decreasing computation time and memory footprint without sacrificing performance, as detailed in Section 5. Using smaller networks such as Krizhevsky et al. (2013) could allow video-rate test-time dense feature computation even on light-weight GPUs.

---

### النسخة العربية

نصف هنا كيف أعدنا توظيف وضبط شبكة التصنيف المتقدمة المكونة من 16 طبقة والمدربة مسبقاً على Imagenet والمتاحة للعامة من (Simonyan & Zisserman, 2014) (VGG-16) لتصبح مستخرج ميزات كثيف فعال وكفؤ لنظام التقسيم الدلالي الكثيف للصور.

## 3.1 استخراج ميزات النافذة المنزلقة الكثيفة بكفاءة باستخدام خوارزمية الثقوب

يعد تقييم الدرجات المكاني الكثيف أساسياً في نجاح مستخرج ميزات الشبكة العصبية الالتفافية الكثيفة. كخطوة أولى لتنفيذ هذا، نحول الطبقات المترابطة بالكامل من VGG-16 إلى طبقات التفافية ونشغل الشبكة بطريقة التفافية على الصورة بدقتها الأصلية. ومع ذلك، هذا ليس كافياً لأنه ينتج درجات كشف محسوبة بشكل متفرق جداً (بخطوة 32 بكسل). لحساب الدرجات بشكل أكثر كثافة عند خطوتنا المستهدفة البالغة 8 بكسلات، نطور تنويعاً على الطريقة المستخدمة سابقاً من قبل Giusti et al. (2013); Sermanet et al. (2013). نتخطى تقليص العينات بعد آخر طبقتي تجميع أعظمي في شبكة Simonyan & Zisserman (2014) ونعدل المرشحات الالتفافية في الطبقات التي تليها من خلال إدخال أصفار لزيادة طولها (2× في آخر ثلاث طبقات التفافية و4× في أول طبقة مترابطة بالكامل). يمكننا تنفيذ هذا بشكل أكثر كفاءة من خلال الحفاظ على المرشحات سليمة وبدلاً من ذلك أخذ عينات متفرقة من خرائط الميزات التي يتم تطبيقها عليها باستخدام خطوة إدخال 2 أو 4 بكسلات، على التوالي. هذا النهج، الموضح في الشكل 1، يُعرف باسم "خوارزمية الثقوب" ("خوارزمية atrous") وقد تم تطويره من قبل للحساب الفعال لتحويل المويجات المنفصل غير المقلص (Mallat, 1999). قمنا بتنفيذ هذا ضمن إطار عمل Caffe (Jia et al., 2014) من خلال إضافة خيار أخذ العينات المتفرقة من خريطة الميزات الأساسية إلى دالة im2col (التي تحول خرائط الميزات متعددة القنوات إلى رقع متجهة). هذا النهج قابل للتطبيق بشكل عام ويسمح لنا بحساب خرائط ميزات الشبكة العصبية الالتفافية الكثيفة بكفاءة بأي معدل تقليص عينات مستهدف دون إدخال أي تقريبات.

نضبط بدقة أوزان نموذج شبكة VGG-16 المدربة مسبقاً على Imagenet لتكييفها مع مهمة تصنيف الصور بطريقة مباشرة، باتباع إجراء Long et al. (2014). نستبدل مصنف Imagenet ذو 1000 اتجاه في الطبقة الأخيرة من VGG-16 بمصنف ذو 21 اتجاه. دالة الخسارة لدينا هي مجموع حدود التقاطع-الإنتروبيا لكل موضع مكاني في خريطة إخراج الشبكة العصبية الالتفافية (مقلصة العينات بمعامل 8 مقارنة بالصورة الأصلية). جميع المواضع والتسميات لها أوزان متساوية في دالة الخسارة الإجمالية. أهدافنا هي تسميات الحقيقة الأرضية (مقلصة العينات بمعامل 8). نحسّن الدالة الهدفية فيما يتعلق بالأوزان في جميع طبقات الشبكة من خلال إجراء الانحدار التدرجي العشوائي (SGD) القياسي من Krizhevsky et al. (2013).

أثناء الاختبار، نحتاج إلى خرائط درجات الفئات بدقة الصورة الأصلية. كما هو موضح في الشكل 2 ومُفصّل أكثر في القسم 4.1، فإن خرائط درجات الفئات (المقابلة للوغاريتمات الاحتمالات) ناعمة تماماً، مما يسمح لنا باستخدام استيفاء خطي ثنائي بسيط لزيادة دقتها بمعامل 8 بتكلفة حسابية ضئيلة. لاحظ أن طريقة Long et al. (2014) لا تستخدم خوارزمية الثقوب وتنتج درجات خشنة جداً (مقلصة العينات بمعامل 32) في إخراج الشبكة العصبية الالتفافية. أجبرهم هذا على استخدام طبقات زيادة عينات متعلمة، مما زاد بشكل كبير من تعقيد ووقت تدريب نظامهم: يستغرق الضبط الدقيق لشبكتنا على PASCAL VOC 2012 حوالي 10 ساعات، بينما يبلغون عن وقت تدريب عدة أيام (كلا التوقيتين على وحدة معالجة رسومات حديثة).

## 3.2 التحكم في حجم الحقل الاستقبالي وتسريع الحساب الكثيف باستخدام الشبكات الالتفافية

مكون رئيسي آخر في إعادة توظيف شبكتنا لحساب الدرجات الكثيف هو التحكم الصريح في حجم الحقل الاستقبالي للشبكة. تعتمد معظم أساليب التعرف على الصور الحديثة القائمة على الشبكات العصبية الالتفافية العميقة على شبكات مدربة مسبقاً على مهمة تصنيف Imagenet واسعة النطاق. عادة ما يكون لهذه الشبكات حجم حقل استقبالي كبير: في حالة شبكة VGG-16 التي نعتبرها، حقلها الاستقبالي هو 224 × 224 (مع الحشو بالأصفار) و404 × 404 بكسل إذا تم تطبيق الشبكة التفافياً. بعد تحويل الشبكة إلى شبكة التفافية بالكامل، تحتوي أول طبقة مترابطة بالكامل على 4,096 مرشح بحجم مكاني كبير 7 × 7 وتصبح عنق الزجاجة الحسابي في حساب خريطة الدرجات الكثيفة.

عالجنا هذه المشكلة العملية من خلال تقليص العينات المكانية (بالتقليص البسيط) للطبقة FC الأولى إلى حجم مكاني 4×4 (أو 3×3). أدى هذا إلى تقليل الحقل الاستقبالي للشبكة إلى 128×128 (مع الحشو بالأصفار) أو 308×308 (في الوضع الالتفافي) وقلل وقت الحساب للطبقة FC الأولى بمقدار 2-3 مرات. باستخدام تطبيقنا القائم على Caffe ووحدة معالجة رسومات Titan، فإن الشبكة الناتجة المشتقة من VGG فعالة جداً: بإعطاء صورة إدخال بحجم 306×306، تنتج درجات ميزات خام كثيفة 39×39 في أعلى الشبكة بمعدل حوالي 8 إطارات في الثانية أثناء الاختبار. السرعة أثناء التدريب هي 3 إطارات في الثانية. نجحنا أيضاً في التجربة مع تقليل عدد القنوات في الطبقات المترابطة بالكامل من 4,096 إلى 1,024، مما يقلل بشكل كبير من وقت الحساب والبصمة الذاكرية دون التضحية بالأداء، كما هو مفصل في القسم 5. يمكن أن يسمح استخدام شبكات أصغر مثل Krizhevsky et al. (2013) بحساب ميزات كثيفة بمعدل الفيديو في وقت الاختبار حتى على وحدات معالجة رسومات خفيفة الوزن.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:**
  - Re-purposed: أعدنا توظيف
  - Fine-tuning: الضبط الدقيق
  - Dense feature extractor: مستخرج ميزات كثيف
  - Stride: خطوة
  - Hole algorithm/Atrous algorithm: خوارزمية الثقوب / خوارزمية atrous
  - Sparsely computed: محسوبة بشكل متفرق
  - Undecimated: غير مقلص
  - im2col function: دالة im2col
  - Vectorized patches: رقع متجهة
  - Cross-entropy: التقاطع-الإنتروبيا
  - Ground truth: الحقيقة الأرضية
  - SGD (Stochastic Gradient Descent): الانحدار التدرجي العشوائي
  - Log-probabilities: لوغاريتمات الاحتمالات
  - Bilinear interpolation: استيفاء خطي ثنائي
  - Upsampling layers: طبقات زيادة عينات
  - Receptive field: الحقل الاستقبالي
  - Zero-padding: الحشو بالأصفار
  - Computational bottleneck: عنق الزجاجة الحسابي
  - Decimation: التقليص
  - Memory footprint: البصمة الذاكرية

- **Equations:** Mathematical expressions for stride and filter sizes preserved
- **Citations:** References to VGG-16, Imagenet, Caffe framework, etc.
- **Dataset:** PASCAL VOC 2012
- **Performance metrics:**
  - 8 pixels target stride
  - 10 hours training time vs several days
  - 8 fps testing speed, 3 fps training speed
  - 306×306 input producing 39×39 output

### Quality Metrics

- **Semantic equivalence:** 0.87 - Technical methodology accurately preserved
- **Technical accuracy:** 0.86 - Complex technical details maintained correctly
- **Readability:** 0.85 - Dense technical content flows in Arabic
- **Glossary consistency:** 0.87 - Consistent terminology throughout

**Overall section score:** 0.86

### Back-Translation Check

**Original (Section 3.1 key sentence):** "This approach, illustrated in Fig. 1 is known as the 'hole algorithm' ('atrous algorithm') and has been developed before for efficient computation of the undecimated wavelet transform."

**Back-translation:** "This approach, illustrated in Figure 1, is known as the 'hole algorithm' ('atrous algorithm') and was previously developed for efficient computation of the undecimated wavelet transform."

✅ **Semantic match:** Excellent

**Original (Performance claim):** "Fine-tuning our network on PASCAL VOC 2012 takes about 10 hours, while they report a training time of several days."

**Back-translation:** "Fine-tuning our network on PASCAL VOC 2012 takes about 10 hours, while they report a training time of several days."

✅ **Semantic match:** Perfect - comparative advantage clearly preserved
