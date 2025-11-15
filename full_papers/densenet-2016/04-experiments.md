# Section 4: Experiments
## القسم 4: التجارب

**Section:** Experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** datasets (مجموعات البيانات), benchmark (معيار), CIFAR, SVHN, ImageNet, data augmentation (زيادة البيانات), preprocessing (معالجة مسبقة), validation (تحقق), stochastic gradient descent (الانحدار التدرجي العشوائي), learning rate (معدل التعلم), batch size (حجم الدفعة), epochs (حقب), weight decay (تناقص الوزن), momentum (زخم), dropout (dropout), error rate (معدل الخطأ), accuracy (دقة), parameters (معاملات), state-of-the-art (أحدث ما توصل إليه العلم), overfitting (الإفراط في التكيف), capacity (سعة), parameter efficiency (كفاءة المعاملات)

---

### English Version

We empirically demonstrate DenseNet's effectiveness on several benchmark datasets and compare with state-of-the-art architectures, especially with ResNet and its variants.

**4.1. Datasets**

**CIFAR.** The two CIFAR datasets [15] consist of colored natural images with 32×32 pixels. CIFAR-10 (C10) consists of images drawn from 10 and CIFAR-100 (C100) from 100 classes. The training and test sets contain 50,000 and 10,000 images respectively, and we hold out 5,000 training images as a validation set. We adopt a standard data augmentation scheme (mirroring/shifting) that is widely used for these two datasets [11, 13, 17, 22, 28, 20, 32, 34]. We denote this data augmentation scheme by a "+" mark at the end of the dataset name (e.g., C10+). For preprocessing, we normalize the data using the channel means and standard deviations. For the final run we use all 50,000 training images and report the final test error at the end of training.

**SVHN.** The Street View House Numbers (SVHN) dataset [24] contains 32×32 colored digit images. There are 73,257 images in the training set, 26,032 images in the test set, and 531,131 images for additional training. Following common practice [7, 13, 20, 22, 30] we use all the training data without any data augmentation, and a validation set with 6,000 images is split from the training set. We select the model with the lowest validation error during training and report the test error. We follow [42] and divide the pixel values by 255 so they are in the [0, 1] range.

**ImageNet.** The ILSVRC 2012 classification dataset [2] consists 1.2 million images for training, and 50,000 for validation, from 1,000 classes. We adopt the same data augmentation scheme for training images as in [8, 11, 12], and apply a single-crop or 10-crop with size 224×224 at test time. Following [11, 12, 13], we report classification errors on the validation set.

**4.2. Training**

All the networks are trained using stochastic gradient descent (SGD). On CIFAR and SVHN we train using batch size 64 for 300 and 40 epochs, respectively. The initial learning rate is set to 0.1, and is divided by 10 at 50% and 75% of the total number of training epochs. On ImageNet, we train models for 90 epochs with a batch size of 256. The learning rate is set to 0.1 initially, and is lowered by 10 times at epoch 30 and 60. Note that a naive implementation of DenseNet may contain memory inefficiencies. To reduce the memory consumption on GPUs, please refer to our technical report on the memory-efficient implementation of DenseNets [26].

Following [8], we use a weight decay of 10⁻⁴ and a Nesterov momentum [35] of 0.9 without dampening. We adopt the weight initialization introduced by [10]. For the three datasets without data augmentation, i.e., C10, C100 and SVHN, we add a dropout layer [33] after each convolutional layer (except the first one) and set the dropout rate to 0.2. The test errors were only evaluated once for each task and model setting.

**4.3. Classification Results on CIFAR and SVHN**

We train DenseNets with different depths, L, and growth rates, k. The main results on CIFAR and SVHN are shown in Table 2. To highlight general trends, we mark all results that outperform the existing state-of-the-art in boldface and the overall best result in blue.

**Accuracy.** Possibly the most noticeable trend may originate from the bottom row of Table 2, which shows that DenseNet-BC with L = 190 and k = 40 outperforms the existing state-of-the-art consistently on all the CIFAR datasets. Its error rates of 3.46% on C10+ and 17.18% on C100+ are significantly lower than the error rates achieved by wide ResNet architecture [42]. Our best results on C10 and C100 (without data augmentation) are even more encouraging: both are close to 30% lower than FractalNet with drop-path regularization [17]. On SVHN, with dropout, the DenseNet with L = 100 and k = 24 also surpasses the current best result achieved by wide ResNet. However, the 250-layer DenseNet-BC doesn't further improve the performance over its shorter counterpart. This may be explained by that SVHN is a relatively easy task, and extremely deep models may overfit to the training set.

**Capacity.** Without compression or bottleneck layers, there is a general trend that DenseNets perform better as L and k increase. We attribute this primarily to the corresponding growth in model capacity. This is best demonstrated by the column of C10+ and C100+. On C10+, the error drops from 5.24% to 4.10% and finally to 3.74% as the number of parameters increases from 1.0M, over 7.0M to 27.2M. On C100+, we observe a similar trend. This suggests that DenseNets can utilize the increased representational power of bigger and deeper models. It also indicates that they do not suffer from overfitting or the optimization difficulties of residual networks [11].

**Parameter Efficiency.** The results in Table 2 indicate that DenseNets utilize parameters more efficiently than alternative architectures (in particular, ResNets). The DenseNet-BC with bottleneck structure and dimension reduction at transition layers is particularly parameter-efficient. For example, our 250-layer model only has 15.3M parameters, but it consistently outperforms other models such as FractalNet and Wide ResNets that have more than 30M parameters. We also highlight that DenseNet-BC with L = 100 and k = 12 achieves comparable performance (e.g., 4.51% vs 4.62% error on C10+, 22.27% vs 22.71% error on C100+) as the 1001-layer pre-activation ResNet using 90% fewer parameters. Figure 4 (right panel) shows the training loss and test errors of these two networks on C10+. The 1001-layer deep ResNet converges to a lower training loss value but a similar test error. We analyze this effect in more detail below.

**Overfitting.** One positive side-effect of the more efficient use of parameters is a tendency of DenseNets to be less prone to overfitting. We observe that on the datasets without data augmentation, the improvements of DenseNet architectures over prior work are particularly pronounced. On C10, the improvement denotes a 29% relative reduction in error from 7.33% to 5.19%. On C100, the reduction is about 30% from 28.20% to 19.64%. In our experiments, we observed potential overfitting in a single setting: on C10, a 4× growth of parameters produced by increasing k = 12 to k = 24 lead to a modest increase in error from 5.77% to 5.83%. The DenseNet-BC bottleneck and compression layers appear to be an effective way to counter this trend.

**4.4. Classification Results on ImageNet**

We evaluate DenseNet-BC with different depths and growth rates on the ImageNet classification task, and compare it with state-of-the-art ResNet architectures. To ensure a fair comparison between the two architectures, we eliminate all other factors such as differences in data preprocessing and optimization settings by adopting the publicly available Torch implementation for ResNet by [8]. We simply replace the ResNet model with the DenseNet-BC network, and keep all the experiment settings exactly the same as those used for ResNet.

We report the single-crop and 10-crop validation errors of DenseNets on ImageNet in Table 3. Figure 3 shows the single-crop top-1 validation errors of DenseNets and ResNets as a function of the number of parameters (left) and FLOPs (right). The results presented in the figure reveal that DenseNets perform on par with the state-of-the-art ResNets, whilst requiring significantly fewer parameters and computation to achieve comparable performance. For example, a DenseNet-201 with 20M parameters model yields similar validation error as a 101-layer ResNet with more than 40M parameters. Similar trends can be observed from the right panel, which plots the validation error as a function of the number of FLOPs: a DenseNet that requires as much computation as a ResNet-50 performs on par with a ResNet-101, which requires twice as much computation.

It is worth noting that our experimental setup implies that we use hyperparameter settings that are optimized for ResNets but not for DenseNets. It is conceivable that more extensive hyper-parameter searches may further improve the performance of DenseNet on ImageNet.

---

### النسخة العربية

نوضح تجريبياً فعالية DenseNet على العديد من مجموعات البيانات المعيارية ونقارنها بالمعماريات الأحدث، خاصة مع ResNet ومتغيراتها.

**4.1. مجموعات البيانات**

**CIFAR.** تتكون مجموعتا بيانات CIFAR [15] من صور طبيعية ملونة بحجم 32×32 بكسل. يتكون CIFAR-10 (C10) من صور مأخوذة من 10 فئات وCIFAR-100 (C100) من 100 فئة. تحتوي مجموعات التدريب والاختبار على 50,000 و10,000 صورة على التوالي، ونحتفظ بـ 5,000 صورة تدريب كمجموعة تحقق. نعتمد مخططاً قياسياً لزيادة البيانات (انعكاس/إزاحة) يُستخدم على نطاق واسع لهاتين المجموعتين [11، 13، 17، 22، 28، 20، 32، 34]. نشير إلى مخطط زيادة البيانات هذا بعلامة "+" في نهاية اسم مجموعة البيانات (على سبيل المثال، C10+). للمعالجة المسبقة، نقوم بتطبيع البيانات باستخدام متوسطات القنوات والانحرافات المعيارية. للتشغيل النهائي نستخدم جميع صور التدريب البالغ عددها 50,000 ونبلغ عن خطأ الاختبار النهائي في نهاية التدريب.

**SVHN.** تحتوي مجموعة بيانات أرقام المنازل من منظور الشارع (SVHN) [24] على صور أرقام ملونة بحجم 32×32. يوجد 73,257 صورة في مجموعة التدريب، و26,032 صورة في مجموعة الاختبار، و531,131 صورة للتدريب الإضافي. وفقاً للممارسة الشائعة [7، 13، 20، 22، 30] نستخدم جميع بيانات التدريب دون أي زيادة للبيانات، ويتم فصل مجموعة تحقق مع 6,000 صورة من مجموعة التدريب. نختار النموذج الذي يحتوي على أقل خطأ تحقق أثناء التدريب ونبلغ عن خطأ الاختبار. نتبع [42] ونقسم قيم البكسل على 255 بحيث تكون في نطاق [0، 1].

**ImageNet.** تتكون مجموعة بيانات تصنيف ILSVRC 2012 [2] من 1.2 مليون صورة للتدريب، و50,000 للتحقق، من 1,000 فئة. نعتمد نفس مخطط زيادة البيانات لصور التدريب كما في [8، 11، 12]، ونطبق قطعاً مفرداً أو 10 قطع بحجم 224×224 في وقت الاختبار. وفقاً لـ [11، 12، 13]، نبلغ عن أخطاء التصنيف على مجموعة التحقق.

**4.2. التدريب**

يتم تدريب جميع الشبكات باستخدام الانحدار التدرجي العشوائي (SGD). على CIFAR وSVHN نقوم بالتدريب باستخدام حجم دفعة 64 لمدة 300 و40 حقبة، على التوالي. يتم ضبط معدل التعلم الأولي على 0.1، ويتم قسمته على 10 عند 50% و75% من إجمالي عدد حقب التدريب. على ImageNet، نقوم بتدريب النماذج لمدة 90 حقبة مع حجم دفعة 256. يتم ضبط معدل التعلم على 0.1 في البداية، ويتم خفضه بمقدار 10 مرات في الحقبة 30 و60. لاحظ أن التنفيذ الساذج لـ DenseNet قد يحتوي على عدم كفاءة في الذاكرة. لتقليل استهلاك الذاكرة على وحدات معالجة الرسومات، يُرجى الرجوع إلى تقريرنا الفني حول التنفيذ الفعال للذاكرة لشبكات DenseNets [26].

وفقاً لـ [8]، نستخدم تناقص وزن قدره 10⁻⁴ وزخم نستروف [35] قدره 0.9 بدون تخميد. نعتمد تهيئة الوزن التي قدمها [10]. بالنسبة لمجموعات البيانات الثلاث بدون زيادة البيانات، أي C10 وC100 وSVHN، نضيف طبقة dropout [33] بعد كل طبقة التفافية (باستثناء الأولى) ونضبط معدل dropout على 0.2. تم تقييم أخطاء الاختبار مرة واحدة فقط لكل مهمة وإعداد نموذج.

**4.3. نتائج التصنيف على CIFAR وSVHN**

نقوم بتدريب شبكات DenseNets بأعماق مختلفة، L، ومعدلات نمو، k. النتائج الرئيسية على CIFAR وSVHN موضحة في الجدول 2. لتسليط الضوء على الاتجاهات العامة، نضع علامة على جميع النتائج التي تتفوق على أحدث ما توصل إليه العلم الموجود بخط عريض وأفضل نتيجة إجمالية باللون الأزرق.

**الدقة.** ربما يكون الاتجاه الأكثر وضوحاً قد ينشأ من الصف السفلي من الجدول 2، والذي يُظهر أن DenseNet-BC مع L = 190 وk = 40 يتفوق على أحدث ما توصل إليه العلم الموجود باستمرار على جميع مجموعات بيانات CIFAR. معدلات الخطأ البالغة 3.46% على C10+ و17.18% على C100+ أقل بكثير من معدلات الخطأ التي حققتها معمارية Wide ResNet [42]. نتائجنا الأفضل على C10 وC100 (بدون زيادة البيانات) أكثر تشجيعاً: كلاهما قريب من 30% أقل من FractalNet مع تنظيم drop-path [17]. على SVHN، مع dropout، فإن DenseNet مع L = 100 وk = 24 يتجاوز أيضاً أفضل نتيجة حالية حققتها Wide ResNet. ومع ذلك، فإن DenseNet-BC المكون من 250 طبقة لا يحسن الأداء أكثر على نظيره الأقصر. قد يُفسر هذا بأن SVHN مهمة سهلة نسبياً، وقد تتكيف النماذج العميقة للغاية بشكل مفرط مع مجموعة التدريب.

**السعة.** بدون طبقات الضغط أو عنق الزجاجة، هناك اتجاه عام أن شبكات DenseNets تؤدي بشكل أفضل مع زيادة L وk. نعزو هذا بشكل أساسي إلى النمو المقابل في سعة النموذج. يُظهر هذا بشكل أفضل من خلال عمود C10+ وC100+. على C10+، ينخفض الخطأ من 5.24% إلى 4.10% وأخيراً إلى 3.74% مع زيادة عدد المعاملات من 1.0M، إلى 7.0M إلى 27.2M. على C100+، نلاحظ اتجاهاً مماثلاً. يشير هذا إلى أن شبكات DenseNets يمكنها استخدام القوة التمثيلية المتزايدة للنماذج الأكبر والأعمق. كما يشير إلى أنها لا تعاني من الإفراط في التكيف أو صعوبات التحسين للشبكات المتبقية [11].

**كفاءة المعاملات.** تشير النتائج في الجدول 2 إلى أن شبكات DenseNets تستخدم المعاملات بشكل أكثر كفاءة من المعماريات البديلة (على وجه الخصوص، ResNets). إن DenseNet-BC مع بنية عنق الزجاجة وتقليل الأبعاد في الطبقات الانتقالية فعال بشكل خاص في المعاملات. على سبيل المثال، نموذجنا المكون من 250 طبقة يحتوي فقط على 15.3M معامل، لكنه يتفوق باستمرار على نماذج أخرى مثل FractalNet وWide ResNets التي تحتوي على أكثر من 30M معامل. نسلط الضوء أيضاً على أن DenseNet-BC مع L = 100 وk = 12 يحقق أداءً مماثلاً (على سبيل المثال، خطأ 4.51% مقابل 4.62% على C10+، خطأ 22.27% مقابل 22.71% على C100+) مثل ResNet التنشيط المسبق المكون من 1001 طبقة باستخدام معاملات أقل بنسبة 90%. يُظهر الشكل 4 (اللوحة اليمنى) خسارة التدريب وأخطاء الاختبار لهاتين الشبكتين على C10+. يتقارب ResNet العميق المكون من 1001 طبقة إلى قيمة خسارة تدريب أقل ولكن خطأ اختبار مماثل. نحلل هذا التأثير بمزيد من التفصيل أدناه.

**الإفراط في التكيف.** أحد الآثار الجانبية الإيجابية للاستخدام الأكثر كفاءة للمعاملات هو ميل شبكات DenseNets إلى أن تكون أقل عرضة للإفراط في التكيف. نلاحظ أنه على مجموعات البيانات بدون زيادة البيانات، فإن تحسينات معماريات DenseNet على العمل السابق واضحة بشكل خاص. على C10، يشير التحسين إلى تخفيض نسبي بنسبة 29% في الخطأ من 7.33% إلى 5.19%. على C100، يبلغ التخفيض حوالي 30% من 28.20% إلى 19.64%. في تجاربنا، لاحظنا إمكانية الإفراط في التكيف في إعداد واحد: على C10، أدى نمو المعاملات بمقدار 4× الناتج عن زيادة k = 12 إلى k = 24 إلى زيادة متواضعة في الخطأ من 5.77% إلى 5.83%. يبدو أن طبقات عنق الزجاجة والضغط في DenseNet-BC طريقة فعالة لمواجهة هذا الاتجاه.

**4.4. نتائج التصنيف على ImageNet**

نقوم بتقييم DenseNet-BC بأعماق ومعدلات نمو مختلفة على مهمة تصنيف ImageNet، ونقارنها بمعماريات ResNet الأحدث. لضمان مقارنة عادلة بين المعماريتين، نزيل جميع العوامل الأخرى مثل الاختلافات في المعالجة المسبقة للبيانات وإعدادات التحسين من خلال اعتماد تنفيذ Torch المتاح للعامة لـ ResNet بواسطة [8]. نستبدل ببساطة نموذج ResNet بشبكة DenseNet-BC، ونحافظ على جميع إعدادات التجربة بالضبط كما هي المستخدمة لـ ResNet.

نبلغ عن أخطاء التحقق أحادية القطع و10 قطع لشبكات DenseNets على ImageNet في الجدول 3. يُظهر الشكل 3 أخطاء التحقق top-1 أحادية القطع لشبكات DenseNets وResNets كدالة لعدد المعاملات (يساراً) وFLOPs (يميناً). تكشف النتائج المقدمة في الشكل أن شبكات DenseNets تؤدي على قدم المساواة مع شبكات ResNets الأحدث، بينما تتطلب معاملات وحسابات أقل بكثير لتحقيق أداء مماثل. على سبيل المثال، ينتج نموذج DenseNet-201 بمعاملات 20M خطأ تحقق مماثلاً لـ ResNet المكون من 101 طبقة بأكثر من 40M معامل. يمكن ملاحظة اتجاهات مماثلة من اللوحة اليمنى، والتي تخطط خطأ التحقق كدالة لعدد FLOPs: DenseNet الذي يتطلب نفس القدر من الحساب مثل ResNet-50 يؤدي على قدم المساواة مع ResNet-101، الذي يتطلب ضعف القدر من الحساب.

من الجدير بالذكر أن إعدادنا التجريبي يعني أننا نستخدم إعدادات المعاملات الفائقة المحسّنة لـ ResNets وليس لـ DenseNets. من المتصور أن عمليات البحث الأكثر شمولاً عن المعاملات الفائقة قد تحسن أداء DenseNet على ImageNet بشكل أكبر.

---

### Translation Notes

- **Tables referenced:** Table 2 (CIFAR and SVHN results), Table 3 (ImageNet results)
- **Figures referenced:** Figure 3 (parameter/FLOPs comparison), Figure 4 (training curves)
- **Key terms introduced:** ILSVRC, single-crop, 10-crop, FLOPs, validation error, Nesterov momentum
- **Equations:** None
- **Citations:** [15], [11, 13, 17, 22, 28, 20, 32, 34], [24], [7, 20, 30], [42], [2], [8, 11, 12], [26], [35], [10], [33]
- **Special handling:** Dataset names (CIFAR-10, CIFAR-100, SVHN, ImageNet) kept in English as they are standard benchmarks, numerical results preserved exactly

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-translation Check

Key result: "معدلات الخطأ البالغة 3.46% على C10+ و17.18% على C100+ أقل بكثير" → "error rates of 3.46% on C10+ and 17.18% on C100+ are significantly lower" - preserves numerical precision and comparative meaning.
