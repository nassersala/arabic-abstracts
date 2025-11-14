# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** ImageNet, ILSVRC, classification, validation, test set, top-1 error, top-5 error, plain networks, residual networks, degradation problem, optimization, ensemble, bottleneck architecture, CIFAR-10, PASCAL VOC, MS COCO, object detection, Faster R-CNN, mAP, transfer learning

---

### English Version

## 4.1. ImageNet Classification

We evaluate our method on the ImageNet 2012 classification dataset [36] that consists of 1000 classes. The models are trained on the 1.28 million training images, and evaluated on the 50k validation images. We also obtain a final result on the 100k test images, reported by the test server. We evaluate both top-1 and top-5 error rates.

**Plain Networks.** We first evaluate 18-layer and 34-layer plain nets. The 34-layer plain net is in Fig. 3 (middle). The 18-layer plain net is of a similar form. See Table 1 for detailed architectures.

The results in Table 2 show that the deeper 34-layer plain net has higher validation error than the shallower 18-layer plain net. To reveal the reasons, in Fig. 4 (left) we compare their training/validation errors during the training procedure. We have observed the degradation problem - the 34-layer plain net has higher training error throughout the whole training procedure, even though the solution space of the 18-layer plain network is a subspace of that of the 34-layer one.

We argue that this optimization difficulty is unlikely to be caused by vanishing gradients. These plain networks are trained with BN [16], which ensures forward propagated signals to have non-zero variances. We also verify that the backward propagated gradients exhibit healthy norms with BN. So neither forward nor backward signals vanish. In fact, the 34-layer plain net is still able to achieve competitive accuracy (Table 3), suggesting that the solver works to some extent. We conjecture that the deep plain nets may have exponentially low convergence rates, which impact the reducing of the training error³. The reason for such optimization difficulties will be studied in the future.

**Residual Networks.** Next we evaluate 18-layer and 34-layer residual nets (ResNets). The baseline architectures are the same as the above plain nets, expect that a shortcut connection is added to each pair of 3×3 filters as in Fig. 3 (right). In the first comparison (Table 2 and Fig. 4 right), we use identity mapping for all shortcuts and zero-padding for increasing dimensions (option A). So they have no extra parameter compared to the plain counterparts.

We have three major observations from Table 2 and Fig. 4. First, the situation is reversed with residual learning – the 34-layer ResNet is better than the 18-layer ResNet (by 2.8%). More importantly, the 34-layer ResNet exhibits considerably lower training error and is generalizable to the validation data. This indicates that the degradation problem is well addressed in this setting and we manage to obtain accuracy gains from increased depth.

Second, compared to its plain counterpart, the 34-layer ResNet reduces the top-1 error by 3.5% (Table 2), resulting from the successfully reduced training error (Fig. 4 right vs. left). This comparison verifies the effectiveness of residual learning on extremely deep systems.

Last, we also note that the 18-layer plain/residual nets are comparably accurate (Table 2), but the 18-layer ResNet converges faster (Fig. 4 right vs. left). When the net is "not overly deep" (18 layers here), the current SGD solver is still able to find good solutions to the plain net. In this case, the ResNet eases the optimization by providing faster convergence at the early stage.

**Identity vs. Projection Shortcuts.** We have shown that parameter-free, identity shortcuts help with training. Next we investigate projection shortcuts (Eqn.(2)). In Table 3 we compare three options: (A) zero-padding shortcuts are used for increasing dimensions, and all shortcuts are parameter-free (the same as Table 2 and Fig. 4 right); (B) projection shortcuts are used for increasing dimensions, and other shortcuts are identity; and (C) all shortcuts are projections.

Table 3 shows that all three options are considerably better than the plain counterpart. B is slightly better than A. We argue that this is because the zero-padded dimensions in A indeed have no residual learning. C is marginally better than B, and we attribute this to the extra parameters introduced by many (thirteen) projection shortcuts. But the small differences among A/B/C indicate that projection shortcuts are not essential for addressing the degradation problem. So we do not use option C in the rest of this paper, to reduce memory/time complexity and model sizes. Identity shortcuts are particularly important for not increasing the complexity of the bottleneck architectures that are introduced below.

**Deeper Bottleneck Architectures.** Next we describe our deeper nets for ImageNet. Because of concerns on the training time that we can afford, we modify the building block as a bottleneck design⁴. For each residual function F, we use a stack of 3 layers instead of 2 (Fig. 5). The three layers are 1×1, 3×3, and 1×1 convolutions, where the 1×1 layers are responsible for reducing and then increasing (restoring) dimensions, leaving the 3×3 layer a bottleneck with smaller input/output dimensions. Fig. 5 shows an example, where both designs have similar time complexity.

The parameter-free identity shortcuts are particularly important for the bottleneck architectures. If the identity shortcut in Fig. 5 (right) is replaced with projection, one can show that the time complexity and model size are doubled, as the shortcut is connected to the two high-dimensional ends. So identity shortcuts lead to more efficient models for the bottleneck designs.

**50-layer ResNet:** We replace each 2-layer block in the 34-layer net with this 3-layer bottleneck block, resulting in a 50-layer ResNet (Table 1). We use option B for increasing dimensions. This model has 3.8 billion FLOPs.

**101-layer and 152-layer ResNets:** We construct 101-layer and 152-layer ResNets by using more 3-layer blocks (Table 1). Remarkably, although the depth is significantly increased, the 152-layer ResNet (11.3 billion FLOPs) still has lower complexity than VGG-16/19 nets (15.3/19.6 billion FLOPs).

The 50/101/152-layer ResNets are more accurate than the 34-layer ones by considerable margins (Table 3 and 4). We do not observe the degradation problem and thus enjoy significant accuracy gains from considerably increased depth. The benefits of depth are witnessed for all evaluation metrics (Table 3 and 4).

**Comparisons with State-of-the-art Methods.** In Table 4 we compare with the previous best single-model results. Our baseline 34-layer ResNets have achieved very competitive accuracy. Our 152-layer ResNet has a single-model top-5 validation error of 4.49%. This single-model result outperforms all previous ensemble results (Table 5). We combine six models of different depth to form an ensemble (only with two 152-layer ones at the time of submitting). This leads to 3.57% top-5 error on the test set (Table 5). This entry won the 1st place in ILSVRC 2015.

## 4.2. CIFAR-10 and Analysis

We conducted more studies on the CIFAR-10 dataset [20], which consists of 50k training images and 10k testing images in 10 classes. We present experiments trained on the training set and evaluated on the test set. Our focus is on the behaviors of extremely deep networks, but not on pushing the state-of-the-art results, so we intentionally use simple architectures as follows.

The plain/residual architectures follow the form in Fig. 3 (middle/right). The network inputs are 32×32 images, with the per-pixel mean subtracted. The first layer is 3×3 convolutions. Then we use a stack of 6n layers with 3×3 convolutions on the feature maps of sizes {32, 16, 8} respectively, with 2n layers for each feature map size. The numbers of filters are {16, 32, 64} respectively. The subsampling is performed by convolutions with a stride of 2. The network ends with a global average pooling, a 10-way fully-connected layer, and softmax. There are totally 6n+2 stacked weighted layers.

When shortcut connections are used, they are connected to the pairs of 3×3 layers (totally 3n shortcuts). On this dataset we use identity shortcuts in all cases (i.e., option A), so our residual models have exactly the same depth, width, and number of parameters as the plain counterparts.

We use a weight decay of 0.0001 and momentum of 0.9, and adopt the weight initialization in [13] and BN [16] but with no dropout. These models are trained with a mini-batch size of 128 on two GPUs. We start with a learning rate of 0.1, divide it by 10 at 32k and 48k iterations, and terminate training at 64k iterations, which is determined on a 45k/5k train/val split. We follow the simple data augmentation in [24] for training: 4 pixels are padded on each side, and a 32×32 crop is randomly sampled from the padded image or its horizontal flip. For testing, we only evaluate the single view of the original 32×32 image.

We compare n = {3, 5, 7, 9}, leading to 20, 32, 44, and 56-layer networks. Fig. 6 (left) shows the behaviors of the plain nets. The deep plain nets suffer from increased depth, and exhibit higher training error when going deeper. This phenomenon is similar to that on ImageNet (Fig. 4, left) and on MNIST (see [42]), suggesting that such an optimization difficulty is a fundamental problem.

Fig. 6 (middle) shows the behaviors of ResNets. Also similar to the ImageNet cases (Fig. 4, right), our ResNets manage to overcome the optimization difficulty and demonstrate accuracy gains when the depth increases.

We further explore n = 18 that leads to a 110-layer ResNet. In this case, we find that the initial learning rate of 0.1 is slightly too large to start converging⁵. So we use 0.01 to warm up the training until the training error is below 80% (about 400 iterations), and then go back to 0.1 and continue training. The rest of the learning schedule is as done previously. This 110-layer network converges well (Fig. 6, middle). It has fewer parameters than other deep and thin networks such as FitNet [35] and Highway [42] (Table 6), yet is among the state-of-the-art results (6.43%, Table 6).

**Analysis of Layer Responses.** Fig. 7 shows the standard deviations (std) of the layer responses. The responses are the outputs of each 3×3 layer, after BN and before other nonlinearity (ReLU/addition). For ResNets, this analysis reveals the response strength of the residual functions. Fig. 7 shows that ResNets have generally smaller responses than their plain counterparts. These results support our basic motivation (Sec.3.1) that the residual functions might be generally closer to zero than the non-residual functions. We also notice that the deeper ResNet has smaller magnitudes of responses, as evidenced by the comparisons among ResNet-20, 56, and 110 in Fig. 7. When there are more layers, an individual layer of ResNets tends to modify the signal less.

**Exploring Over 1000 layers.** We explore an aggressively deep model of over 1000 layers. We set n = 200 that leads to a 1202-layer network, which is trained as described above. Our method shows no optimization difficulty, and this 10³-layer network is able to achieve training error <0.1% (Fig. 6, right). Its test error is still fairly good (7.93%, Table 6).

But there are still open problems on such aggressively deep models. The testing result of this 1202-layer network is worse than that of our 110-layer network, although both have similar training error. We argue that this is because of overfitting. The 1202-layer network may be unnecessarily large (19.4M) for this small dataset. Strong regularization such as maxout [10] or dropout [14] is applied to obtain the best results ([10, 25, 24, 35]) on this dataset. In this paper, we use no maxout/dropout and just simply impose regularization via deep and thin architectures by design, without distracting from the focus on the difficulties of optimization. But combining with stronger regularization may improve results, which we will study in the future.

## 4.3. Object Detection on PASCAL and MS COCO

Our method has good generalization performance on other recognition tasks. Table 7 and 8 show the object detection baseline results on PASCAL VOC 2007 and 2012 [5] and COCO [26]. We adopt Faster R-CNN [32] as the detection method. Here we are interested in the improvements of replacing VGG-16 [41] with ResNet-101. The detection implementation (see appendix) of using both models is the same, so the gains can only be attributed to better networks. Most remarkably, on the challenging COCO dataset we obtain a 6.0% increase in COCO's standard metric (mAP@[.5, .95]), which is a 28% relative improvement. This gain is solely due to the learned representations.

Based on deep residual nets, we won the 1st places in several tracks in ILSVRC & COCO 2015 competitions: ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation. The details are in the appendix.

---

### النسخة العربية

## 4.1. تصنيف ImageNet

نقيّم طريقتنا على مجموعة بيانات تصنيف ImageNet 2012 [36] التي تتكون من 1000 صنف. يتم تدريب النماذج على 1.28 مليون صورة تدريب، وتقييمها على 50 ألف صورة تحقق. نحصل أيضاً على نتيجة نهائية على 100 ألف صورة اختبار، يتم الإبلاغ عنها بواسطة خادم الاختبار. نقيّم كلاً من معدلات خطأ أفضل 1 وأفضل 5.

**الشبكات البسيطة.** نقيّم أولاً الشبكات البسيطة المكونة من 18 و34 طبقة. الشبكة البسيطة المكونة من 34 طبقة موجودة في الشكل 3 (الوسط). الشبكة البسيطة المكونة من 18 طبقة لها شكل مماثل. انظر الجدول 1 للمعماريات التفصيلية.

تُظهر النتائج في الجدول 2 أن الشبكة البسيطة الأعمق المكونة من 34 طبقة لديها خطأ تحقق أعلى من الشبكة الأقل عمقاً المكونة من 18 طبقة. للكشف عن الأسباب، في الشكل 4 (يسار) نقارن أخطاء التدريب/التحقق الخاصة بهما خلال إجراء التدريب. لاحظنا مشكلة التدهور - الشبكة البسيطة المكونة من 34 طبقة لديها خطأ تدريب أعلى طوال إجراء التدريب بأكمله، على الرغم من أن فضاء الحلول للشبكة البسيطة المكونة من 18 طبقة هو فضاء فرعي من فضاء الشبكة المكونة من 34 طبقة.

نجادل بأن صعوبة التحسين هذه من غير المحتمل أن تكون ناجمة عن تلاشي التدرجات. يتم تدريب هذه الشبكات البسيطة باستخدام BN [16]، الذي يضمن أن الإشارات المنتشرة للأمام لديها تباينات غير صفرية. نتحقق أيضاً من أن التدرجات المنتشرة للخلف تظهر معايير صحية مع BN. لذا فإن الإشارات الأمامية ولا الخلفية تتلاشى. في الواقع، لا تزال الشبكة البسيطة المكونة من 34 طبقة قادرة على تحقيق دقة تنافسية (الجدول 3)، مما يشير إلى أن المحلل يعمل إلى حد ما. نفترض أن الشبكات البسيطة العميقة قد يكون لديها معدلات تقارب منخفضة بشكل أسي، مما يؤثر على تقليل خطأ التدريب³. سيتم دراسة سبب مثل هذه الصعوبات في التحسين في المستقبل.

**الشبكات المتبقية.** بعد ذلك نقيّم الشبكات المتبقية المكونة من 18 و34 طبقة (ResNets). معماريات خط الأساس هي نفسها الشبكات البسيطة أعلاه، باستثناء إضافة اتصال اختصار إلى كل زوج من مرشحات 3×3 كما في الشكل 3 (يمين). في المقارنة الأولى (الجدول 2 والشكل 4 يمين)، نستخدم تعيين الهوية لجميع الاختصارات والحشو بالأصفار لزيادة الأبعاد (الخيار A). لذا ليس لديهم معامل إضافي مقارنة بالنظراء البسطاء.

لدينا ثلاث ملاحظات رئيسية من الجدول 2 والشكل 4. أولاً، الوضع معكوس مع التعلم المتبقي - الشبكة المتبقية المكونة من 34 طبقة أفضل من الشبكة المتبقية المكونة من 18 طبقة (بنسبة 2.8%). والأهم من ذلك، تُظهر الشبكة المتبقية المكونة من 34 طبقة خطأ تدريب أقل بكثير وقابلة للتعميم على بيانات التحقق. هذا يشير إلى أن مشكلة التدهور تمت معالجتها بشكل جيد في هذا الإعداد وتمكنا من الحصول على مكاسب في الدقة من العمق المتزايد.

ثانياً، مقارنة بنظيرتها البسيطة، تقلل الشبكة المتبقية المكونة من 34 طبقة خطأ أفضل 1 بنسبة 3.5% (الجدول 2)، ناتجة عن خطأ التدريب المنخفض بنجاح (الشكل 4 يمين مقابل يسار). تتحقق هذه المقارنة من فعالية التعلم المتبقي على الأنظمة العميقة للغاية.

أخيراً، نلاحظ أيضاً أن الشبكات البسيطة/المتبقية المكونة من 18 طبقة دقيقة بشكل مماثل (الجدول 2)، لكن الشبكة المتبقية المكونة من 18 طبقة تتقارب بشكل أسرع (الشكل 4 يمين مقابل يسار). عندما لا تكون الشبكة "عميقة بشكل مفرط" (18 طبقة هنا)، لا يزال محلل SGD الحالي قادراً على إيجاد حلول جيدة للشبكة البسيطة. في هذه الحالة، تسهل الشبكة المتبقية التحسين من خلال توفير تقارب أسرع في المرحلة المبكرة.

**اختصارات الهوية مقابل اختصارات الإسقاط.** أظهرنا أن اختصارات الهوية الخالية من المعاملات تساعد في التدريب. بعد ذلك نبحث في اختصارات الإسقاط (المعادلة (2)). في الجدول 3 نقارن ثلاثة خيارات: (A) تُستخدم اختصارات الحشو بالأصفار لزيادة الأبعاد، وجميع الاختصارات خالية من المعاملات (نفس الجدول 2 والشكل 4 يمين)؛ (B) تُستخدم اختصارات الإسقاط لزيادة الأبعاد، والاختصارات الأخرى هي هوية؛ و (C) جميع الاختصارات هي إسقاطات.

يُظهر الجدول 3 أن جميع الخيارات الثلاثة أفضل بكثير من النظير البسيط. B أفضل قليلاً من A. نجادل بأن هذا لأن الأبعاد المحشوة بالأصفار في A ليس لديها فعلياً تعلم متبقي. C أفضل بشكل هامشي من B، ونعزو هذا إلى المعاملات الإضافية التي قدمتها اختصارات الإسقاط العديدة (ثلاثة عشر). لكن الفروق الصغيرة بين A/B/C تشير إلى أن اختصارات الإسقاط ليست ضرورية لمعالجة مشكلة التدهور. لذا لا نستخدم الخيار C في بقية هذه الورقة، لتقليل تعقيد الذاكرة/الوقت وأحجام النماذج. اختصارات الهوية مهمة بشكل خاص لعدم زيادة تعقيد معماريات الاختناق التي يتم تقديمها أدناه.

**معماريات الاختناق الأعمق.** بعد ذلك نصف شبكاتنا الأعمق لـ ImageNet. بسبب المخاوف بشأن وقت التدريب الذي يمكننا تحمله، نعدّل كتلة البناء كتصميم اختناق⁴. لكل دالة متبقية F، نستخدم كومة من 3 طبقات بدلاً من 2 (الشكل 5). الطبقات الثلاث هي التفافات 1×1 و3×3 و1×1، حيث تكون طبقات 1×1 مسؤولة عن تقليل ثم زيادة (استعادة) الأبعاد، تاركة طبقة 3×3 اختناقاً بأبعاد مدخل/مخرج أصغر. يُظهر الشكل 5 مثالاً، حيث كلا التصميمين لهما تعقيد وقت مماثل.

اختصارات الهوية الخالية من المعاملات مهمة بشكل خاص لمعماريات الاختناق. إذا تم استبدال اختصار الهوية في الشكل 5 (يمين) بإسقاط، يمكن للمرء أن يُظهر أن تعقيد الوقت وحجم النموذج يتضاعفان، حيث يتصل الاختصار بالطرفين عاليي الأبعاد. لذا تؤدي اختصارات الهوية إلى نماذج أكثر كفاءة لتصميمات الاختناق.

**شبكة متبقية مكونة من 50 طبقة:** نستبدل كل كتلة مكونة من طبقتين في الشبكة المكونة من 34 طبقة بهذه الكتلة المكونة من 3 طبقات اختناق، مما ينتج عنه شبكة متبقية مكونة من 50 طبقة (الجدول 1). نستخدم الخيار B لزيادة الأبعاد. هذا النموذج لديه 3.8 مليار FLOP.

**شبكات متبقية مكونة من 101 و152 طبقة:** نبني شبكات متبقية مكونة من 101 و152 طبقة باستخدام المزيد من الكتل المكونة من 3 طبقات (الجدول 1). بشكل ملحوظ، على الرغم من زيادة العمق بشكل كبير، لا تزال الشبكة المتبقية المكونة من 152 طبقة (11.3 مليار FLOP) لديها تعقيد أقل من شبكات VGG-16/19 (15.3/19.6 مليار FLOP).

الشبكات المتبقية المكونة من 50/101/152 طبقة أكثر دقة من تلك المكونة من 34 طبقة بفوارق كبيرة (الجداول 3 و4). لا نلاحظ مشكلة التدهور وبالتالي نستمتع بمكاسب دقة كبيرة من العمق المتزايد بشكل كبير. تُشهد فوائد العمق لجميع مقاييس التقييم (الجداول 3 و4).

**المقارنات مع الطرق الحديثة.** في الجدول 4 نقارن مع أفضل نتائج النموذج الفردي السابقة. حققت شبكاتنا المتبقية الأساسية المكونة من 34 طبقة دقة تنافسية جداً. تمتلك شبكتنا المتبقية المكونة من 152 طبقة خطأ تحقق أفضل 5 لنموذج فردي بنسبة 4.49%. هذه النتيجة للنموذج الفردي تتفوق على جميع نتائج المجموعات السابقة (الجدول 5). نجمع ستة نماذج بأعماق مختلفة لتشكيل مجموعة (فقط مع اثنين من النماذج المكونة من 152 طبقة في وقت التقديم). هذا يؤدي إلى خطأ أفضل 5 بنسبة 3.57% على مجموعة الاختبار (الجدول 5). فاز هذا الإدخال بالمركز الأول في ILSVRC 2015.

## 4.2. CIFAR-10 والتحليل

أجرينا المزيد من الدراسات على مجموعة بيانات CIFAR-10 [20]، التي تتكون من 50 ألف صورة تدريب و10 آلاف صورة اختبار في 10 أصناف. نقدم تجارب مدربة على مجموعة التدريب ومقيّمة على مجموعة الاختبار. تركيزنا على سلوكيات الشبكات العميقة للغاية، وليس على دفع نتائج الحديثة، لذا نستخدم عمداً معماريات بسيطة كما يلي.

تتبع المعماريات البسيطة/المتبقية الشكل في الشكل 3 (وسط/يمين). مدخلات الشبكة هي صور 32×32، مع طرح المتوسط لكل بكسل. الطبقة الأولى هي التفافات 3×3. ثم نستخدم كومة من 6n طبقة مع التفافات 3×3 على خرائط الميزات بأحجام {32، 16، 8} على التوالي، مع 2n طبقة لكل حجم خريطة ميزات. أعداد المرشحات هي {16، 32، 64} على التوالي. يتم إجراء أخذ العينات الفرعية بواسطة التفافات بخطوة من 2. تنتهي الشبكة بالتجميع المتوسط العام، طبقة متصلة بالكامل بـ 10 اتجاهات، و softmax. هناك إجمالي 6n+2 طبقة موزونة مكدسة.

عند استخدام اتصالات الاختصار، يتم توصيلها بأزواج طبقات 3×3 (إجمالي 3n اختصار). في مجموعة البيانات هذه نستخدم اختصارات الهوية في جميع الحالات (أي الخيار A)، لذا فإن نماذجنا المتبقية لديها نفس العمق والعرض وعدد المعاملات بالضبط مثل النظراء البسطاء.

نستخدم انحلال وزن من 0.0001 وزخم من 0.9، ونعتمد تهيئة الأوزان في [13] و BN [16] ولكن بدون dropout. يتم تدريب هذه النماذج بحجم دفعة صغيرة من 128 على اثنين من GPUs. نبدأ بمعدل تعلم من 0.1، ونقسمه على 10 عند 32 ألف و48 ألف تكرار، وننهي التدريب عند 64 ألف تكرار، والذي يتم تحديده على تقسيم تدريب/تحقق 45 ألف/5 آلاف. نتبع زيادة البيانات البسيطة في [24] للتدريب: يتم حشو 4 بكسلات على كل جانب، ويتم أخذ عينة عشوائية لمحصول 32×32 من الصورة المحشوة أو انعكاسها الأفقي. للاختبار، نقيّم فقط العرض الفردي للصورة الأصلية 32×32.

نقارن n = {3، 5، 7، 9}، مما يؤدي إلى شبكات مكونة من 20 و32 و44 و56 طبقة. يُظهر الشكل 6 (يسار) سلوكيات الشبكات البسيطة. تعاني الشبكات البسيطة العميقة من العمق المتزايد، وتظهر خطأ تدريب أعلى عند التعمق. هذه الظاهرة مشابهة لتلك على ImageNet (الشكل 4، يسار) وعلى MNIST (انظر [42])، مما يشير إلى أن مثل هذه الصعوبة في التحسين هي مشكلة أساسية.

يُظهر الشكل 6 (وسط) سلوكيات الشبكات المتبقية. أيضاً مشابهة لحالات ImageNet (الشكل 4، يمين)، تتمكن شبكاتنا المتبقية من التغلب على صعوبة التحسين وإظهار مكاسب دقة عندما يزداد العمق.

نستكشف أكثر n = 18 مما يؤدي إلى شبكة متبقية مكونة من 110 طبقة. في هذه الحالة، نجد أن معدل التعلم الأولي من 0.1 كبير قليلاً جداً لبدء التقارب⁵. لذا نستخدم 0.01 لتسخين التدريب حتى يكون خطأ التدريب أقل من 80% (حوالي 400 تكرار)، ثم نعود إلى 0.1 ونستمر في التدريب. بقية جدول التعلم كما تم سابقاً. تتقارب هذه الشبكة المكونة من 110 طبقة بشكل جيد (الشكل 6، وسط). لديها معاملات أقل من الشبكات العميقة والرقيقة الأخرى مثل FitNet [35] و Highway [42] (الجدول 6)، ومع ذلك فهي من بين النتائج الحديثة (6.43%، الجدول 6).

**تحليل استجابات الطبقات.** يُظهر الشكل 7 الانحرافات المعيارية (std) لاستجابات الطبقات. الاستجابات هي مخرجات كل طبقة 3×3، بعد BN وقبل اللاخطية الأخرى (ReLU/الجمع). بالنسبة للشبكات المتبقية، يكشف هذا التحليل عن قوة استجابة الدوال المتبقية. يُظهر الشكل 7 أن الشبكات المتبقية لديها بشكل عام استجابات أصغر من نظرائها البسطاء. تدعم هذه النتائج دافعنا الأساسي (القسم 3.1) أن الدوال المتبقية قد تكون بشكل عام أقرب إلى الصفر من الدوال غير المتبقية. نلاحظ أيضاً أن الشبكة المتبقية الأعمق لديها مقادير استجابات أصغر، كما يتضح من المقارنات بين ResNet-20 و56 و110 في الشكل 7. عندما يكون هناك المزيد من الطبقات، تميل الطبقة الفردية من الشبكات المتبقية إلى تعديل الإشارة بشكل أقل.

**استكشاف أكثر من 1000 طبقة.** نستكشف نموذجاً عميقاً بشكل قوي بأكثر من 1000 طبقة. نضبط n = 200 مما يؤدي إلى شبكة مكونة من 1202 طبقة، والتي يتم تدريبها كما هو موضح أعلاه. تُظهر طريقتنا عدم وجود صعوبة في التحسين، وهذه الشبكة المكونة من 10³ طبقة قادرة على تحقيق خطأ تدريب <0.1% (الشكل 6، يمين). خطأ اختبارها لا يزال جيداً إلى حد ما (7.93%، الجدول 6).

لكن لا تزال هناك مشاكل مفتوحة في مثل هذه النماذج العميقة بشكل قوي. نتيجة الاختبار لهذه الشبكة المكونة من 1202 طبقة أسوأ من تلك الخاصة بشبكتنا المكونة من 110 طبقة، على الرغم من أن كليهما لديه خطأ تدريب مماثل. نجادل بأن هذا بسبب فرط التلاؤم. قد تكون الشبكة المكونة من 1202 طبقة كبيرة بشكل غير ضروري (19.4M) لمجموعة البيانات الصغيرة هذه. يتم تطبيق التنظيم القوي مثل maxout [10] أو dropout [14] للحصول على أفضل النتائج ([10، 25، 24، 35]) على مجموعة البيانات هذه. في هذه الورقة، لا نستخدم maxout/dropout ونفرض ببساطة التنظيم عبر المعماريات العميقة والرقيقة بالتصميم، دون التشتت عن التركيز على صعوبات التحسين. لكن الجمع مع التنظيم الأقوى قد يحسن النتائج، والتي سندرسها في المستقبل.

## 4.3. كشف الأجسام على PASCAL و MS COCO

لطريقتنا أداء تعميم جيد في مهام التعرف الأخرى. تُظهر الجداول 7 و8 نتائج خط الأساس لكشف الأجسام على PASCAL VOC 2007 و2012 [5] و COCO [26]. نعتمد Faster R-CNN [32] كطريقة الكشف. هنا نحن مهتمون بتحسينات استبدال VGG-16 [41] بـ ResNet-101. تنفيذ الكشف (انظر الملحق) لاستخدام كلا النموذجين هو نفسه، لذا يمكن أن تُعزى المكاسب فقط إلى شبكات أفضل. بشكل ملحوظ، على مجموعة بيانات COCO الصعبة نحصل على زيادة 6.0% في المقياس القياسي لـ COCO (mAP@[.5، .95])، وهو تحسن نسبي بنسبة 28%. هذا المكسب يرجع فقط إلى التمثيلات المتعلمة.

بناءً على الشبكات المتبقية العميقة، فزنا بالمراكز الأولى في عدة مسارات في مسابقات ILSVRC وCOCO 2015: كشف ImageNet، وتوطين ImageNet، وكشف COCO، وتجزئة COCO. التفاصيل في الملحق.

---

### Translation Notes

- **Tables referenced:** Tables 1-8 (architecture details, error rates, comparisons)
- **Figures referenced:** Figures 3-7 (training curves, architectures, layer responses)
- **Datasets:** ImageNet (1.28M training, 50K validation, 100K test), CIFAR-10 (50K train, 10K test), PASCAL VOC 2007/2012, MS COCO
- **Key results:**
  - ResNet-152: 3.57% top-5 error on ImageNet (won ILSVRC 2015)
  - ResNet-110 on CIFAR-10: 6.43% error
  - ResNet-1202: Successfully trained but overfits on CIFAR-10
  - Object detection: 28% relative improvement on COCO

- **Key terms introduced:**
  - top-1 error / top-5 error (خطأ أفضل 1 / خطأ أفضل 5)
  - validation error (خطأ التحقق)
  - test set (مجموعة الاختبار)
  - ensemble (مجموعة)
  - bottleneck architecture (معمارية الاختناق)
  - convergence rate (معدل التقارب)
  - overfitting (فرط التلاؤم)
  - layer responses (استجابات الطبقات)
  - standard deviation (الانحراف المعياري)
  - warm up (تسخين)
  - Faster R-CNN (اسم النموذج يبقى كما هو)
  - mAP (mean Average Precision) (متوسط الدقة المتوسط)
  - transfer learning / generalization (التعميم)

- **Important observations:**
  - Degradation problem confirmed on both ImageNet and CIFAR-10
  - ResNets solve degradation and benefit from increased depth
  - Identity shortcuts sufficient (projections only marginally better)
  - Bottleneck design enables very deep networks efficiently
  - Layer responses in ResNets are smaller (closer to identity)
  - ResNet-1202 shows overfitting on small dataset
  - Strong transfer learning performance on detection tasks

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
