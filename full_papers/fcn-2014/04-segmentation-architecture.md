# Section 4: Segmentation Architecture
## القسم 4: معمارية التجزئة

**Section:** segmentation-architecture
**Translation Quality:** 0.88
**Glossary Terms Used:** semantic segmentation, fine-tuning, architecture, fully convolutional network, skip connections, upsampling, pooling, convolutional layers, mean IU, validation, optimization, SGD, momentum, learning rate, dropout

---

### English Version

We cast ILSVRC classifiers into FCNs and augment them for dense prediction with in-network upsampling and a pixelwise loss. We train for segmentation by fine-tuning. Next, we build a novel skip architecture that combines coarse, semantic and local, appearance information to refine prediction.

For this investigation, we train and validate on the PASCAL VOC 2011 segmentation challenge [7]. We train with a per-pixel multinomial logistic loss and validate with the standard metric of mean pixel intersection over union, with the mean taken over all classes, including background. The training ignores pixels that are masked out (as ambiguous or difficult) in the ground truth.

**4.1. From classifier to dense FCN**

We begin by convolutionalizing proven classification architectures as in Section 3. We consider the AlexNet³ architecture [19] that won ILSVRC12, as well as the VGG nets [31] and the GoogLeNet⁴ [32] which did exceptionally well in ILSVRC14. We pick the VGG 16-layer net⁵, which we found to be equivalent to the 19-layer net on this task. For GoogLeNet, we use only the final loss layer, and improve performance by discarding the final average pooling layer. We decapitate each net by discarding the final classifier layer, and convert all fully connected layers to convolutions. We append a 1 × 1 convolution with channel dimension 21 to predict scores for each of the PASCAL classes (including background) at each of the coarse output locations, followed by a deconvolution layer to bilinearly upsample the coarse outputs to pixel-dense outputs as described in Section 3.3. Table 1 compares the preliminary validation results along with the basic characteristics of each net. We report the best results achieved after convergence at a fixed learning rate (at least 175 epochs).

Fine-tuning from classification to segmentation gave reasonable predictions for each net. Even the worst model achieved ∼ 75% of state-of-the-art performance. The segmentation-equipped VGG net (FCN-VGG16) already appears to be state-of-the-art at 56.0 mean IU on val, compared to 52.6 on test [16]. Training on extra data raises performance to 59.4 mean IU on a subset of val⁷. Training details are given in Section 4.3.

Despite similar classification accuracy, our implementation of GoogLeNet did not match this segmentation result.

**4.2. Combining what and where**

We define a new fully convolutional net (FCN) for segmentation that combines layers of the feature hierarchy and refines the spatial precision of the output. See Figure 3.

While fully convolutionalized classifiers can be fine-tuned to segmentation as shown in 4.1, and even score highly on the standard metric, their output is dissatisfyingly coarse (see Figure 4). The 32 pixel stride at the final prediction layer limits the scale of detail in the upsampled output.

We address this by adding links that combine the final prediction layer with lower layers with finer strides. This turns a line topology into a DAG, with edges that skip ahead from lower layers to higher ones (Figure 3). As they see fewer pixels, the finer scale predictions should need fewer layers, so it makes sense to make them from shallower net outputs. Combining fine layers and coarse layers lets the model make local predictions that respect global structure. By analogy to the multiscale local jet of Florack et al. [10], we call our nonlinear local feature hierarchy the deep jet.

We first divide the output stride in half by predicting from a 16 pixel stride layer. We add a 1 × 1 convolution layer on top of pool4 to produce additional class predictions. We fuse this output with the predictions computed on top of conv7 (convolutionalized fc7) at stride 32 by adding a 2× upsampling layer and summing⁶ both predictions. (See Figure 3). We initialize the 2× upsampling to bilinear interpolation, but allow the parameters to be learned as described in Section 3.3. Finally, the stride 16 predictions are upsampled back to the image. We call this net FCN-16s. FCN-16s is learned end-to-end, initialized with the parameters of the last, coarser net, which we now call FCN-32s. The new parameters acting on pool4 are zero-initialized so that the net starts with unmodified predictions. The learning rate is decreased by a factor of 100.

Learning this skip net improves performance on the validation set by 3.0 mean IU to 62.4. Figure 4 shows improvement in the fine structure of the output. We compared this fusion with learning only from the pool4 layer (which resulted in poor performance), and simply decreasing the learning rate without adding the extra link (which results in an insignificant performance improvement, without improving the quality of the output).

We continue in this fashion by fusing predictions from pool3 with a 2× upsampling of predictions fused from pool4 and conv7, building the net FCN-8s. We obtain a minor additional improvement to 62.7 mean IU, and find a slight improvement in the smoothness and detail of our output. At this point our fusion improvements have met diminishing returns, both with respect to the IU metric which emphasizes large-scale correctness, and also in terms of the improvement visible e.g. in Figure 4, so we do not continue fusing even lower layers.

**Refinement by other means** Decreasing the stride of pooling layers is the most straightforward way to obtain finer predictions. However, doing so is problematic for our VGG16-based net. Setting the pool5 layer to have stride 1 requires our convolutionalized fc6 to have a kernel size of 14 × 14 in order to maintain its receptive field size. In addition to their computational cost, we had difficulty learning such large filters. We made an attempt to re-architect the layers above pool5 with smaller filters, but were not successful in achieving comparable performance; one possible explanation is that the initialization from ImageNet-trained weights in the upper layers is important.

Another way to obtain finer predictions is to use the shift-and-stitch trick described in Section 3.2. In limited experiments, we found the cost to improvement ratio from this method to be worse than layer fusion.

**4.3. Experimental framework**

**Optimization** We train by SGD with momentum. We use a minibatch size of 20 images and fixed learning rates of 10⁻³, 10⁻⁴, and 5⁻⁵ for FCN-AlexNet, FCN-VGG16, and FCN-GoogLeNet, respectively, chosen by line search. We use momentum 0.9, weight decay of 5⁻⁴ or 2⁻⁴, and doubled the learning rate for biases, although we found training to be insensitive to these parameters (but sensitive to the learning rate). We zero-initialize the class scoring convolution layer, finding random initialization to yield neither better performance nor faster convergence. Dropout was included where used in the original classifier nets.

**Fine-tuning** We fine-tune all layers by backpropagation through the whole net. Fine-tuning the output classifier alone yields only 70% of the full fine-tuning performance as compared in Table 2. Training from scratch is not feasible considering the time required to learn the base classification nets. (Note that the VGG net is trained in stages, while we initialize from the full 16-layer version.) Fine-tuning takes three days on a single GPU for the coarse FCN-32s version, and about one day each to upgrade to the FCN-16s and FCN-8s versions.

**Patch Sampling** As explained in Section 3.4, our full image training effectively batches each image into a regular grid of large, overlapping patches. By contrast, prior work randomly samples patches over a full dataset [27, 2, 8, 28, 11], potentially resulting in higher variance batches that may accelerate convergence [22]. We study this tradeoff by spatially sampling the loss in the manner described earlier, making an independent choice to ignore each final layer cell with some probability 1−p. To avoid changing the effective batch size, we simultaneously increase the number of images per batch by a factor 1/p. Note that due to the efficiency of convolution, this form of rejection sampling is still faster than patchwise training for large enough values of p (e.g., at least for p > 0.2 according to the numbers in Section 3.1). Figure 5 shows the effect of this form of sampling on convergence. We find that sampling does not have a significant effect on convergence rate compared to whole image training, but takes significantly more time due to the larger number of images that need to be considered per batch. We therefore choose unsampled, whole image training in our other experiments.

**Class Balancing** Fully convolutional training can balance classes by weighting or sampling the loss. Although our labels are mildly unbalanced (about 3/4 are background), we find class balancing unnecessary.

**Dense Prediction** The scores are upsampled to the input dimensions by deconvolution layers within the net. Final layer deconvolutional filters are fixed to bilinear interpolation, while intermediate upsampling layers are initialized to bilinear upsampling, and then learned. Shift-and-stitch (Section 3.2), or the filter rarefaction equivalent, are not used.

**Augmentation** We tried augmenting the training data by randomly mirroring and "jittering" the images by translating them up to 32 pixels (the coarsest scale of prediction) in each direction. This yielded no noticeable improvement.

**More Training Data** The PASCAL VOC 2011 segmentation challenge training set, which we used for Table 1, labels 1112 images. Hariharan et al. [15] have collected labels for a much larger set of 8498 PASCAL training images, which was used to train the previous state-of-the-art system, SDS [16]. This training data improves the FCN-VGG16 validation score⁷ by 3.4 points to 59.4 mean IU.

**Implementation** All models are trained and tested with Caffe [18] on a single NVIDIA Tesla K40c. The models and code will be released open-source on publication.

---

³ Using the publicly available CaffeNet reference model.
⁴ Since there is no publicly available version of GoogLeNet, we use our own reimplementation. Our version is trained with less extensive data augmentation, and gets 68.5% top-1 and 88.4% top-5 ILSVRC accuracy.
⁵ Using the publicly available version from the Caffe model zoo.
⁶ Max fusion made learning difficult due to gradient switching.
⁷ There are training images from [15] included in the PASCAL VOC 2011 val set, so we validate on the non-intersecting set of 736 images.

---

### النسخة العربية

نحول مصنفات ILSVRC إلى شبكات FCN ونعززها للتنبؤ الكثيف بالرفع الداخلي في الشبكة وخسارة على مستوى البكسل. نتدرب على التجزئة عن طريق الضبط الدقيق. بعد ذلك، نبني معمارية تخطي جديدة تجمع بين المعلومات الدلالية الخشنة ومعلومات المظهر الموضعية لتحسين التنبؤ.

لهذا التحقيق، نتدرب ونتحقق على تحدي تجزئة PASCAL VOC 2011 [7]. نتدرب بخسارة لوجستية متعددة الحدود على مستوى البكسل ونتحقق باستخدام المقياس القياسي لمتوسط تقاطع البكسل على الاتحاد، مع أخذ المتوسط على جميع الفئات، بما في ذلك الخلفية. يتجاهل التدريب البكسلات التي تم حجبها (على أنها غامضة أو صعبة) في الحقيقة الأرضية.

**4.1. من المصنف إلى FCN الكثيف**

نبدأ بتحويل معماريات التصنيف المثبتة إلى التفافية كما في القسم 3. نعتبر معمارية AlexNet³ [19] التي فازت بـ ILSVRC12، بالإضافة إلى شبكات VGG [31] وGoogLeNet⁴ [32] التي كان أداؤها استثنائياً في ILSVRC14. نختار شبكة VGG ذات الـ 16 طبقة⁵، والتي وجدنا أنها معادلة لشبكة الـ 19 طبقة في هذه المهمة. بالنسبة لـ GoogLeNet، نستخدم فقط طبقة الخسارة النهائية، ونحسن الأداء من خلال التخلص من طبقة التجميع المتوسط النهائية. نقوم بقطع رأس كل شبكة من خلال التخلص من طبقة المصنف النهائية، وتحويل جميع الطبقات المتصلة بالكامل إلى التفافات. نلحق التفافاً 1 × 1 ببُعد قناة 21 للتنبؤ بالدرجات لكل من فئات PASCAL (بما في ذلك الخلفية) في كل من مواقع الإخراج الخشنة، متبوعاً بطبقة فك التفاف لرفع المخرجات الخشنة بشكل خطي ثنائي إلى مخرجات كثيفة البكسل كما هو موضح في القسم 3.3. يقارن الجدول 1 نتائج التحقق الأولية مع الخصائص الأساسية لكل شبكة. نبلغ عن أفضل النتائج التي تم تحقيقها بعد التقارب عند معدل تعلم ثابت (175 حقبة على الأقل).

أعطى الضبط الدقيق من التصنيف إلى التجزئة تنبؤات معقولة لكل شبكة. حتى أسوأ نموذج حقق ∼ 75% من أداء أحدث ما توصلت إليه التقنية. تبدو شبكة VGG المجهزة بالتجزئة (FCN-VGG16) بالفعل أنها أحدث ما توصلت إليه التقنية بمتوسط IU يبلغ 56.0 على val، مقارنة بـ 52.6 على test [16]. يرفع التدريب على بيانات إضافية الأداء إلى 59.4 متوسط IU على مجموعة فرعية من val⁷. تُعطى تفاصيل التدريب في القسم 4.3.

على الرغم من دقة التصنيف المماثلة، لم يطابق تطبيقنا لـ GoogLeNet نتيجة التجزئة هذه.

**4.2. الجمع بين ماذا وأين**

نُعرّف شبكة التفافية كاملة جديدة (FCN) للتجزئة تجمع بين طبقات التسلسل الهرمي للميزات وتحسن الدقة المكانية للمخرجات. انظر الشكل 3.

بينما يمكن ضبط المصنفات المحولة التفافياً بالكامل بشكل دقيق للتجزئة كما هو موضح في 4.1، وحتى الحصول على درجات عالية على المقياس القياسي، فإن مخرجاتها خشنة بشكل غير مُرضٍ (انظر الشكل 4). تحد الخطوة البالغة 32 بكسلاً في طبقة التنبؤ النهائية من مقياس التفاصيل في المخرجات المرفوعة.

نعالج هذا بإضافة روابط تجمع بين طبقة التنبؤ النهائية والطبقات السفلى ذات الخطوات الأدق. يؤدي هذا إلى تحويل طوبولوجيا خطية إلى DAG، مع حواف تتخطى من الطبقات السفلى إلى الأعلى (الشكل 3). نظراً لأنها ترى بكسلات أقل، يجب أن تحتاج التنبؤات ذات المقياس الأدق إلى طبقات أقل، لذلك من المنطقي صنعها من مخرجات شبكة أكثر سطحية. يتيح الجمع بين الطبقات الدقيقة والطبقات الخشنة للنموذج إجراء تنبؤات موضعية تحترم البنية العامة. بالقياس على النفث الموضعي متعدد المقاييس لـ Florack وآخرون [10]، نسمي تسلسلنا الهرمي للميزات الموضعية اللاخطية النفث العميق.

نقسم أولاً خطوة الإخراج إلى النصف من خلال التنبؤ من طبقة بخطوة 16 بكسلاً. نضيف طبقة التفاف 1 × 1 فوق pool4 لإنتاج تنبؤات فئة إضافية. ندمج هذا الإخراج مع التنبؤات المحسوبة فوق conv7 (fc7 المحولة التفافياً) بخطوة 32 من خلال إضافة طبقة رفع 2× وجمع⁶ كلا التنبؤين. (انظر الشكل 3). نقوم بتهيئة الرفع 2× إلى الاستيفاء الخطي الثنائي، لكننا نسمح بتعلم المعاملات كما هو موضح في القسم 3.3. أخيراً، يتم رفع تنبؤات الخطوة 16 مرة أخرى إلى الصورة. نسمي هذه الشبكة FCN-16s. يتم تعلم FCN-16s من البداية إلى النهاية، مُهيأة بمعاملات الشبكة الأخيرة الأكثر خشونة، والتي نسميها الآن FCN-32s. المعاملات الجديدة التي تعمل على pool4 مُهيأة بالصفر بحيث تبدأ الشبكة بتنبؤات غير معدلة. ينخفض معدل التعلم بعامل 100.

يحسن تعلم شبكة التخطي هذه الأداء على مجموعة التحقق بمقدار 3.0 متوسط IU إلى 62.4. يوضح الشكل 4 التحسن في البنية الدقيقة للمخرجات. قارنّا هذا الدمج مع التعلم فقط من طبقة pool4 (مما أدى إلى أداء ضعيف)، وببساطة تقليل معدل التعلم دون إضافة الرابط الإضافي (مما ينتج عنه تحسن غير ملحوظ في الأداء، دون تحسين جودة المخرجات).

نواصل بهذه الطريقة من خلال دمج التنبؤات من pool3 مع رفع 2× للتنبؤات المدمجة من pool4 وconv7، لبناء الشبكة FCN-8s. نحصل على تحسن إضافي طفيف إلى 62.7 متوسط IU، ونجد تحسناً طفيفاً في سلاسة وتفاصيل مخرجاتنا. في هذه المرحلة، لقيت تحسينات الدمج لدينا عوائد متناقصة، سواء فيما يتعلق بمقياس IU الذي يؤكد على الصحة واسعة النطاق، وأيضاً من حيث التحسن المرئي على سبيل المثال في الشكل 4، لذلك لا نستمر في دمج الطبقات الأدنى.

**التحسين بوسائل أخرى** إن تقليل خطوة طبقات التجميع هو الطريقة الأكثر مباشرة للحصول على تنبؤات أدق. ومع ذلك، فإن القيام بذلك يمثل مشكلة لشبكتنا المستندة إلى VGG16. يتطلب تعيين طبقة pool5 لتكون لها خطوة 1 أن يكون لدى fc6 المحولة التفافياً حجم نواة 14 × 14 للحفاظ على حجم حقلها الاستقبالي. بالإضافة إلى تكلفتها الحسابية، واجهنا صعوبة في تعلم مثل هذه المرشحات الكبيرة. حاولنا إعادة تصميم الطبقات فوق pool5 بمرشحات أصغر، لكننا لم ننجح في تحقيق أداء مماثل؛ أحد التفسيرات المحتملة هو أن التهيئة من الأوزان المدربة على ImageNet في الطبقات العليا مهمة.

طريقة أخرى للحصول على تنبؤات أدق هي استخدام حيلة التحويل والتشابك الموصوفة في القسم 3.2. في التجارب المحدودة، وجدنا أن نسبة التكلفة إلى التحسين من هذه الطريقة أسوأ من دمج الطبقات.

**4.3. إطار العمل التجريبي**

**التحسين** نتدرب بواسطة SGD مع الزخم. نستخدم حجم حزمة صغيرة من 20 صورة ومعدلات تعلم ثابتة 10⁻³، و10⁻⁴، و5⁻⁵ لـ FCN-AlexNet، وFCN-VGG16، وFCN-GoogLeNet، على التوالي، المختارة عن طريق البحث الخطي. نستخدم زخماً 0.9، وتسوس وزن 5⁻⁴ أو 2⁻⁴، وضاعفنا معدل التعلم للتحيزات، على الرغم من أننا وجدنا أن التدريب غير حساس لهذه المعاملات (لكنه حساس لمعدل التعلم). نقوم بتهيئة طبقة الالتفاف لتسجيل الفئات بالصفر، حيث نجد أن التهيئة العشوائية لا تنتج أداءً أفضل ولا تقارباً أسرع. تم تضمين Dropout حيث تم استخدامه في شبكات المصنفات الأصلية.

**الضبط الدقيق** نضبط بدقة جميع الطبقات عن طريق الانتشار العكسي خلال الشبكة بأكملها. ينتج الضبط الدقيق لمصنف المخرجات وحده 70% فقط من أداء الضبط الدقيق الكامل كما تمت المقارنة في الجدول 2. التدريب من الصفر غير ممكن بالنظر إلى الوقت المطلوب لتعلم شبكات التصنيف الأساسية. (لاحظ أن شبكة VGG مدربة على مراحل، بينما نقوم بالتهيئة من النسخة الكاملة ذات الـ 16 طبقة.) يستغرق الضبط الدقيق ثلاثة أيام على وحدة معالجة رسومات واحدة لنسخة FCN-32s الخشنة، وحوالي يوم واحد لكل ترقية إلى نسخ FCN-16s وFCN-8s.

**أخذ عينات الرقع** كما هو موضح في القسم 3.4، فإن تدريبنا بالصورة الكاملة يجمع بشكل فعال كل صورة في شبكة منتظمة من الرقع الكبيرة المتداخلة. على النقيض من ذلك، تأخذ الأعمال السابقة عينات رقع عشوائية على مجموعة بيانات كاملة [27، 2، 8، 28، 11]، مما قد ينتج عنه حزم ذات تباين أعلى قد تسرع التقارب [22]. ندرس هذه المقايضة من خلال أخذ عينات الخسارة مكانياً بالطريقة الموصوفة سابقاً، مع اتخاذ خيار مستقل لتجاهل كل خلية طبقة نهائية باحتمال 1−p. لتجنب تغيير حجم الحزمة الفعال، نزيد في الوقت نفسه عدد الصور لكل حزمة بعامل 1/p. لاحظ أنه بسبب كفاءة الالتفاف، فإن هذا الشكل من أخذ عينات الرفض لا يزال أسرع من التدريب القائم على الرقع لقيم p كبيرة بما فيه الكفاية (على سبيل المثال، على الأقل لـ p > 0.2 وفقاً للأرقام في القسم 3.1). يوضح الشكل 5 تأثير هذا الشكل من أخذ العينات على التقارب. نجد أن أخذ العينات ليس له تأثير كبير على معدل التقارب مقارنة بتدريب الصورة الكاملة، لكنه يستغرق وقتاً أطول بكثير بسبب العدد الأكبر من الصور التي يجب مراعاتها لكل حزمة. لذلك نختار التدريب بالصورة الكاملة دون أخذ عينات في تجاربنا الأخرى.

**موازنة الفئات** يمكن للتدريب الالتفافي الكامل موازنة الفئات عن طريق ترجيح أو أخذ عينات الخسارة. على الرغم من أن تسمياتنا غير متوازنة بشكل طفيف (حوالي 3/4 خلفية)، نجد أن موازنة الفئات غير ضرورية.

**التنبؤ الكثيف** يتم رفع الدرجات إلى أبعاد الإدخال بواسطة طبقات فك الالتفاف داخل الشبكة. تُثبّت مرشحات فك الالتفاف للطبقة النهائية على الاستيفاء الخطي الثنائي، بينما يتم تهيئة طبقات الرفع الوسيطة إلى الرفع الخطي الثنائي، ثم يتم تعلمها. لا يُستخدم التحويل والتشابك (القسم 3.2)، أو ما يعادله من ترقيق المرشح.

**التضخيم** جربنا تضخيم بيانات التدريب عن طريق الانعكاس العشوائي و"الاهتزاز" للصور عن طريق ترجمتها حتى 32 بكسلاً (المقياس الأكثر خشونة للتنبؤ) في كل اتجاه. لم ينتج عن هذا تحسن ملحوظ.

**المزيد من بيانات التدريب** مجموعة تدريب تحدي تجزئة PASCAL VOC 2011، التي استخدمناها للجدول 1، تحتوي على تسميات لـ 1112 صورة. جمع Hariharan وآخرون [15] تسميات لمجموعة أكبر بكثير من 8498 صورة تدريب PASCAL، والتي استُخدمت لتدريب نظام أحدث ما توصلت إليه التقنية السابق، SDS [16]. تحسن بيانات التدريب هذه درجة التحقق من FCN-VGG16⁷ بمقدار 3.4 نقطة إلى 59.4 متوسط IU.

**التطبيق** يتم تدريب واختبار جميع النماذج باستخدام Caffe [18] على NVIDIA Tesla K40c واحدة. سيتم إصدار النماذج والكود مفتوح المصدر عند النشر.

---

³ باستخدام نموذج مرجع CaffeNet المتاح للعموم.
⁴ نظراً لعدم وجود نسخة متاحة للعموم من GoogLeNet، نستخدم إعادة تطبيقنا الخاصة. نسختنا مدربة بتضخيم بيانات أقل شمولاً، وتحصل على دقة ILSVRC بنسبة 68.5% في الأعلى-1 و88.4% في الأعلى-5.
⁵ باستخدام النسخة المتاحة للعموم من Caffe model zoo.
⁶ جعل الدمج الأقصى التعلم صعباً بسبب تبديل التدرج.
⁷ هناك صور تدريب من [15] مضمنة في مجموعة PASCAL VOC 2011 val، لذلك نتحقق على المجموعة غير المتقاطعة المكونة من 736 صورة.

---

### Translation Notes

- **Figures referenced:** Figure 3 (skip architecture DAG), Figure 4 (comparison of FCN-32s, FCN-16s, FCN-8s), Figure 5 (sampling convergence)
- **Tables referenced:** Table 1 (comparison of FCN architectures), Table 2 (fine-tuning comparison)
- **Key terms introduced:**
  - ILSVRC classifiers (مصنفات ILSVRC)
  - Skip architecture (معمارية التخطي)
  - Multinomial logistic loss (خسارة لوجستية متعددة الحدود)
  - Mean pixel intersection over union - mean IU (متوسط تقاطع البكسل على الاتحاد - متوسط IU)
  - Convolutionalizing (تحويل التفافياً)
  - Decapitate (قطع رأس)
  - DAG - Directed Acyclic Graph (DAG - رسم بياني لا دوري موجه)
  - Deep jet (النفث العميق)
  - Pool layers (طبقات pool)
  - Conv layers (طبقات conv)
  - Zero-initialize (تهيئة بالصفر)
  - Line search (البحث الخطي)
  - Weight decay (تسوس الوزن)
  - Minibatch (حزمة صغيرة)
  - Jittering (الاهتزاز)

- **Equations:** None explicitly shown, but references to mathematical concepts
- **Citations:** References [2, 7, 8, 10, 11, 15, 16, 18, 19, 22, 27, 28, 31, 32]
- **Special handling:**
  - Preserved network names (AlexNet, VGG, GoogLeNet, FCN-32s, FCN-16s, FCN-8s)
  - Kept dataset names (PASCAL VOC, ILSVRC, ImageNet) in English
  - Maintained table and figure references
  - Translated footnotes at bottom
  - Preserved technical precision throughout

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-translation Check

Key sentence:
Arabic: "نبني معمارية تخطي جديدة تجمع بين المعلومات الدلالية الخشنة ومعلومات المظهر الموضعية لتحسين التنبؤ"
Back: "We build a novel skip architecture that combines coarse semantic information with local appearance information to improve prediction"
Original: "we build a novel skip architecture that combines coarse, semantic and local, appearance information to refine prediction"
✓ Semantic equivalence confirmed (slight wording variation)
