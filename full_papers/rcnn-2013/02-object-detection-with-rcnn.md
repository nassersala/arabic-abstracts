# Section 2: Object detection with R-CNN
## القسم 2: الكشف عن الأجسام باستخدام R-CNN

**Section:** object-detection-with-rcnn
**Translation Quality:** 0.87
**Glossary Terms Used:** object detection, region proposals, convolutional neural network, feature vector, SVM, fine-tuning, supervised pre-training, mean average precision, bounding box, intersection-over-union

---

### English Version

## 2. Object detection with R-CNN

Our object detection system consists of three modules. The first generates category-independent region proposals. These proposals define the set of candidate detections available to our detector. The second module is a large convolutional neural network that extracts a fixed-length feature vector from each region. The third module is a set of class-specific linear SVMs. In this section, we present our design decisions for each module, describe their test-time usage, detail how their parameters are learned, and show detection results on PASCAL VOC 2010-12 and on ILSVRC2013.

### 2.1. Module design

**Region proposals.** A variety of recent papers offer methods for generating category-independent region proposals. Examples include: objectness [1], selective search [39], category-independent object proposals [14], constrained parametric min-cuts (CPMC) [5], multi-scale combinatorial grouping [3], and Ciresan et al. [6], who detect mitotic cells by applying a CNN to regularly-spaced square crops, which are a special case of region proposals. While R-CNN is agnostic to the particular region proposal method, we use selective search to enable a controlled comparison with prior detection work (e.g., [39, 41]).

**Feature extraction.** We extract a 4096-dimensional feature vector from each region proposal using the Caffe [24] implementation of the CNN described by Krizhevsky et al. [25]. Features are computed by forward propagating a mean-subtracted 227×227 RGB image through five convolutional layers and two fully connected layers. We refer readers to [24, 25] for more network architecture details.

In order to compute features for a region proposal, we must first convert the image data in that region into a form that is compatible with the CNN (its architecture requires inputs of a fixed 227×227 pixel size). Of the many possible transformations of our arbitrary-shaped regions, we opt for the simplest. Regardless of the size or aspect ratio of the candidate region, we warp all pixels in a tight bounding box around it to the required size. Prior to warping, we dilate the tight bounding box so that at the warped size there are exactly p pixels of warped image context around the original box (we use p=16). Figure 2 shows a random sampling of warped training regions. Alternatives to warping are discussed in Appendix A.

### 2.2. Test-time detection

At test time, we run selective search on the test image to extract around 2000 region proposals (we use selective search's "fast mode" in all experiments). We warp each proposal and forward propagate it through the CNN in order to compute features. Then, for each class, we score each extracted feature vector using the SVM trained for that class. Given all scored regions in an image, we apply a greedy non-maximum suppression (for each class independently) that rejects a region if it has an intersection-over-union (IoU) overlap with a higher scoring selected region larger than a learned threshold.

**Run-time analysis.** Two properties make detection efficient. First, all CNN parameters are shared across all categories. Second, the feature vectors computed by the CNN are low-dimensional when compared to other common approaches, such as spatial pyramids with bag-of-visual-word encodings. The features used in the UVA detection system [39], for example, are two orders of magnitude larger than ours (360k vs. 4k-dimensional).

The result of such sharing is that the time spent computing region proposals and features (13s/image on a GPU or 53s/image on a CPU) is amortized over all classes. The only class-specific computations are dot products between features and SVM weights and non-maximum suppression. In practice, all dot products for an image are batched into a single matrix-matrix product. The feature matrix is typically 2000×4096 and the SVM weight matrix is 4096×N, where N is the number of classes.

This analysis shows that R-CNN can scale to thousands of object classes without resorting to approximate techniques, such as hashing. Even if there were 100k classes, the resulting matrix multiplication takes only 10 seconds on a modern multi-core CPU. This efficiency is not merely the result of using region proposals and shared features. The UVA system, due to its high-dimensional features, would be two orders of magnitude slower while requiring 134GB of memory just to store 100k linear predictors, compared to just 1.5GB for our lower-dimensional features.

It is also interesting to contrast R-CNN with the recent work from Dean et al. on scalable detection using DPMs and hashing [8]. They report a mAP of around 16% on VOC 2007 at a run-time of 5 minutes per image when introducing 10k distractor classes. With our approach, 10k detectors can run in about a minute on a CPU, and because no approximations are made mAP would remain at 59% (Section 3.2).

### 2.3. Training

**Supervised pre-training.** We discriminatively pre-trained the CNN on a large auxiliary dataset (ILSVRC2012 classification) using image-level annotations only (bounding-box labels are not available for this data). Pre-training was performed using the open source Caffe CNN library [24]. In brief, our CNN nearly matches the performance of Krizhevsky et al. [25], obtaining a top-1 error rate 2.2 percentage points higher on the ILSVRC2012 classification validation set. This discrepancy is due to simplifications in the training process.

**Domain-specific fine-tuning.** To adapt our CNN to the new task (detection) and the new domain (warped proposal windows), we continue stochastic gradient descent (SGD) training of the CNN parameters using only warped region proposals. Aside from replacing the CNN's ImageNet-specific 1000-way classification layer with a randomly initialized (N+1)-way classification layer (where N is the number of object classes, plus 1 for background), the CNN architecture is unchanged. For VOC, N=20 and for ILSVRC2013, N=200. We treat all region proposals with ≥0.5 IoU overlap with a ground-truth box as positives for that box's class and the rest as negatives. We start SGD at a learning rate of 0.001 (1/10th of the initial pre-training rate), which allows fine-tuning to make progress while not clobbering the initialization. In each SGD iteration, we uniformly sample 32 positive windows (over all classes) and 96 background windows to construct a mini-batch of size 128. We bias the sampling towards positive windows because they are extremely rare compared to background.

**Object category classifiers.** Consider training a binary classifier to detect cars. It's clear that an image region tightly enclosing a car should be a positive example. Similarly, it's clear that a background region, which has nothing to do with cars, should be a negative example. Less clear is how to label a region that partially overlaps a car. We resolve this issue with an IoU overlap threshold, below which regions are defined as negatives. The overlap threshold, 0.3, was selected by a grid search over {0, 0.1, ..., 0.5} on a validation set. We found that selecting this threshold carefully is important. Setting it to 0.5, as in [39], decreased mAP by 5 points. Similarly, setting it to 0 decreased mAP by 4 points. Positive examples are defined simply to be the ground-truth bounding boxes for each class.

Once features are extracted and training labels are applied, we optimize one linear SVM per class. Since the training data is too large to fit in memory, we adopt the standard hard negative mining method [17, 37]. Hard negative mining converges quickly and in practice mAP stops increasing after only a single pass over all images.

In Appendix B we discuss why the positive and negative examples are defined differently in fine-tuning versus SVM training. We also discuss the trade-offs involved in training detection SVMs rather than simply using the outputs from the final softmax layer of the fine-tuned CNN.

### 2.4. Results on PASCAL VOC 2010-12

Following the PASCAL VOC best practices [15], we validated all design decisions and hyperparameters on the VOC 2007 dataset (Section 3.2). For final results on the VOC 2010-12 datasets, we fine-tuned the CNN on VOC 2012 train and optimized our detection SVMs on VOC 2012 trainval. We submitted test results to the evaluation server only once for each of the two major algorithm variants (with and without bounding-box regression).

Table 1 shows complete results on VOC 2010. We compare our method against four strong baselines, including SegDPM [18], which combines DPM detectors with the output of a semantic segmentation system [4] and uses additional inter-detector context and image-classifier rescoring. The most germane comparison is to the UVA system from Uijlings et al. [39], since our systems use the same region proposal algorithm. To classify regions, their method builds a four-level spatial pyramid and populates it with densely sampled SIFT, Extended OpponentSIFT, and RGB-SIFT descriptors, each vector quantized with 4000-word codebooks. Classification is performed with a histogram intersection kernel SVM. Compared to their multi-feature, non-linear kernel SVM approach, we achieve a large improvement in mAP, from 35.1% to 53.7% mAP, while also being much faster (Section 2.2). Our method achieves similar performance (53.3% mAP) on VOC 2011/12 test.

### 2.5. Results on ILSVRC2013 detection

We ran R-CNN on the 200-class ILSVRC2013 detection dataset using the same system hyperparameters that we used for PASCAL VOC. We followed the same protocol of submitting test results to the ILSVRC2013 evaluation server only twice, once with and once without bounding-box regression.

Figure 3 compares R-CNN to the entries in the ILSVRC 2013 competition and to the post-competition OverFeat result [34]. R-CNN achieves a mAP of 31.4%, which is significantly ahead of the second-best result of 24.3% from OverFeat. To give a sense of the AP distribution over classes, box plots are also presented and a table of per-class APs follows at the end of the paper in Table 8. Most of the competing submissions (OverFeat, NEC-MU, UvA-Euvision, Toronto A, and UIUC-IFP) used convolutional neural networks, indicating that there is significant nuance in how CNNs can be applied to object detection, leading to greatly varying outcomes.

In Section 4, we give an overview of the ILSVRC2013 detection dataset and provide details about choices that we made when running R-CNN on it.

---

### النسخة العربية

## 2. الكشف عن الأجسام باستخدام R-CNN

يتكون نظام الكشف عن الأجسام الخاص بنا من ثلاث وحدات. تولّد الوحدة الأولى مقترحات مناطق مستقلة عن الفئة. تحدد هذه المقترحات مجموعة الكشوفات المرشحة المتاحة للكاشف الخاص بنا. الوحدة الثانية هي شبكة عصبية التفافية كبيرة تستخرج متجه ميزات ذو طول ثابت من كل منطقة. الوحدة الثالثة هي مجموعة من آلات المتجهات الداعمة (SVMs) الخطية الخاصة بكل صنف. في هذا القسم، نعرض قراراتنا التصميمية لكل وحدة، ونصف استخدامها في وقت الاختبار، ونفصّل كيفية تعلم معاملاتها، ونعرض نتائج الكشف على PASCAL VOC 2010-12 وعلى ILSVRC2013.

### 2.1. تصميم الوحدات

**مقترحات المناطق.** تقدم مجموعة متنوعة من الأبحاث الحديثة طرقاً لتوليد مقترحات مناطق مستقلة عن الفئة. تشمل الأمثلة: objectness [1]، والبحث الانتقائي (selective search) [39]، ومقترحات الأجسام المستقلة عن الفئة [14]، والقطوع الصغرى البارامترية المقيدة (CPMC) [5]، والتجميع التجميعي متعدد المقاييس [3]، و Ciresan وآخرون [6] الذين يكشفون عن الخلايا الانقسامية من خلال تطبيق شبكة عصبية التفافية على قصاصات مربعة متباعدة بشكل منتظم، والتي تمثل حالة خاصة من مقترحات المناطق. بينما R-CNN لا يعتمد على طريقة معينة لمقترحات المناطق، نستخدم البحث الانتقائي لتمكين مقارنة محكومة مع أعمال الكشف السابقة (مثل [39, 41]).

**استخراج الميزات.** نستخرج متجه ميزات بُعد 4096 من كل مقترح منطقة باستخدام تنفيذ Caffe [24] للشبكة العصبية الالتفافية الموصوفة من قبل Krizhevsky وآخرين [25]. يتم حساب الميزات من خلال الانتشار الأمامي لصورة RGB بحجم 227×227 بعد طرح المتوسط عبر خمس طبقات التفافية وطبقتين متصلتين بالكامل. نحيل القراء إلى [24, 25] لمزيد من التفاصيل حول معمارية الشبكة.

لحساب الميزات لمقترح منطقة، يجب علينا أولاً تحويل بيانات الصورة في تلك المنطقة إلى شكل متوافق مع الشبكة العصبية الالتفافية (تتطلب معماريتها مدخلات بحجم بكسل ثابت 227×227). من بين العديد من التحويلات الممكنة لمناطقنا ذات الأشكال التعسفية، اخترنا الأبسط. بغض النظر عن حجم أو نسبة أبعاد المنطقة المرشحة، نقوم بتشويه جميع البكسلات في صندوق التحديد الضيق حولها إلى الحجم المطلوب. قبل التشويه، نوسع صندوق التحديد الضيق بحيث يكون هناك بالضبط p بكسل من سياق الصورة المشوهة حول الصندوق الأصلي في الحجم المشوه (نستخدم p=16). يُظهر الشكل 2 عينة عشوائية من مناطق التدريب المشوهة. تُناقش البدائل للتشويه في الملحق A.

### 2.2. الكشف في وقت الاختبار

في وقت الاختبار، نقوم بتشغيل البحث الانتقائي على صورة الاختبار لاستخراج حوالي 2000 مقترح منطقة (نستخدم "الوضع السريع" للبحث الانتقائي في جميع التجارب). نقوم بتشويه كل مقترح والانتشار الأمامي له عبر الشبكة العصبية الالتفافية من أجل حساب الميزات. ثم، لكل صنف، نقوم بتسجيل كل متجه ميزات مستخرج باستخدام آلة المتجهات الداعمة المدربة لذلك الصنف. بالنظر إلى جميع المناطق المسجلة في صورة، نطبق كبت غير الحد الأقصى الجشع (لكل صنف بشكل مستقل) الذي يرفض منطقة إذا كان لديها تداخل تقاطع على اتحاد (IoU) مع منطقة مختارة ذات درجة أعلى أكبر من عتبة متعلمة.

**تحليل وقت التشغيل.** تجعل خاصيتان الكشف فعالاً. أولاً، تتم مشاركة جميع معاملات الشبكة العصبية الالتفافية عبر جميع الفئات. ثانياً، متجهات الميزات المحسوبة بواسطة الشبكة العصبية الالتفافية منخفضة الأبعاد مقارنة بالمناهج الشائعة الأخرى، مثل الأهرامات المكانية مع ترميزات كيس الكلمات المرئية. الميزات المستخدمة في نظام الكشف UVA [39]، على سبيل المثال، أكبر بمقدار رتبتين من رتبنا (360k مقابل 4k بُعد).

نتيجة لهذه المشاركة هي أن الوقت المستغرق في حساب مقترحات المناطق والميزات (13 ثانية/صورة على GPU أو 53 ثانية/صورة على CPU) يتم توزيعه على جميع الأصناف. الحسابات الوحيدة الخاصة بالصنف هي حاصل الضرب النقطي بين الميزات وأوزان آلة المتجهات الداعمة وكبت غير الحد الأقصى. في الممارسة العملية، يتم تجميع جميع حواصل الضرب النقطي لصورة في حاصل ضرب مصفوفة-مصفوفة واحد. مصفوفة الميزات عادة 2000×4096 ومصفوفة أوزان آلة المتجهات الداعمة هي 4096×N، حيث N هو عدد الأصناف.

يُظهر هذا التحليل أن R-CNN يمكن أن يتوسع إلى آلاف أصناف الأجسام دون اللجوء إلى تقنيات تقريبية، مثل التجزئة. حتى لو كان هناك 100 ألف صنف، فإن ضرب المصفوفة الناتج يستغرق 10 ثوانٍ فقط على وحدة معالجة مركزية حديثة متعددة النوى. هذه الكفاءة ليست مجرد نتيجة لاستخدام مقترحات المناطق والميزات المشتركة. نظام UVA، بسبب ميزاته عالية الأبعاد، سيكون أبطأ بمقدار رتبتين بينما يتطلب 134 جيجابايت من الذاكرة فقط لتخزين 100 ألف متنبئ خطي، مقارنة بـ 1.5 جيجابايت فقط لميزاتنا منخفضة الأبعاد.

من المثير للاهتمام أيضاً مقارنة R-CNN مع العمل الحديث من Dean وآخرين حول الكشف القابل للتوسع باستخدام DPMs والتجزئة [8]. يبلغون عن mAP حوالي 16% على VOC 2007 في وقت تشغيل 5 دقائق لكل صورة عند إدخال 10 آلاف صنف مشتت. مع نهجنا، يمكن تشغيل 10 آلاف كاشف في حوالي دقيقة على وحدة المعالجة المركزية، ولأنه لا يتم إجراء تقريبات، سيبقى mAP عند 59% (القسم 3.2).

### 2.3. التدريب

**التدريب المسبق الموجّه.** قمنا بالتدريب المسبق التمييزي للشبكة العصبية الالتفافية على مجموعة بيانات مساعدة كبيرة (تصنيف ILSVRC2012) باستخدام تعليقات توضيحية على مستوى الصورة فقط (تسميات صناديق التحديد غير متاحة لهذه البيانات). تم إجراء التدريب المسبق باستخدام مكتبة Caffe للشبكات العصبية الالتفافية مفتوحة المصدر [24]. باختصار، شبكتنا العصبية الالتفافية تقارب أداء Krizhevsky وآخرين [25]، محققة معدل خطأ top-1 أعلى بـ 2.2 نقطة مئوية على مجموعة التحقق من تصنيف ILSVRC2012. هذا التباين يرجع إلى التبسيطات في عملية التدريب.

**الضبط الدقيق الخاص بالمجال.** لتكييف شبكتنا العصبية الالتفافية مع المهمة الجديدة (الكشف) والمجال الجديد (نوافذ المقترحات المشوهة)، نواصل تدريب الانحدار التدرجي العشوائي (SGD) لمعاملات الشبكة العصبية الالتفافية باستخدام مقترحات المناطق المشوهة فقط. بصرف النظر عن استبدال طبقة التصنيف الخاصة بـ ImageNet ذات 1000 اتجاه للشبكة العصبية الالتفافية بطبقة تصنيف ذات (N+1) اتجاه مُهيأة عشوائياً (حيث N هو عدد أصناف الأجسام، بالإضافة إلى 1 للخلفية)، تظل معمارية الشبكة العصبية الالتفافية دون تغيير. بالنسبة لـ VOC، N=20 وبالنسبة لـ ILSVRC2013، N=200. نعامل جميع مقترحات المناطق ذات التداخل ≥0.5 IoU مع صندوق الحقيقة الأرضية كإيجابيات لصنف ذلك الصندوق والباقي كسلبيات. نبدأ SGD بمعدل تعلم 0.001 (1/10 من معدل التدريب المسبق الأولي)، مما يسمح للضبط الدقيق بإحراز تقدم دون إتلاف التهيئة. في كل تكرار SGD، نقوم بأخذ عينات موحدة من 32 نافذة إيجابية (عبر جميع الأصناف) و96 نافذة خلفية لبناء دفعة صغيرة بحجم 128. نحيّز العينات نحو النوافذ الإيجابية لأنها نادرة للغاية مقارنة بالخلفية.

**مصنفات فئات الأجسام.** لنفكر في تدريب مصنف ثنائي لاكتشاف السيارات. من الواضح أن منطقة صورة تحيط بسيارة بإحكام يجب أن تكون مثالاً إيجابياً. وبالمثل، من الواضح أن منطقة خلفية، ليس لها علاقة بالسيارات، يجب أن تكون مثالاً سلبياً. الأقل وضوحاً هو كيفية تصنيف منطقة تتداخل جزئياً مع سيارة. نحل هذه المشكلة بعتبة تداخل IoU، يتم تحت تعريف المناطق كسلبيات. تم اختيار عتبة التداخل، 0.3، من خلال بحث شبكي على {0، 0.1، ...، 0.5} على مجموعة التحقق. وجدنا أن اختيار هذه العتبة بعناية مهم. تعيينها إلى 0.5، كما في [39]، قلل mAP بمقدار 5 نقاط. وبالمثل، تعيينها إلى 0 قلل mAP بمقدار 4 نقاط. يتم تعريف الأمثلة الإيجابية ببساطة بأنها صناديق التحديد للحقيقة الأرضية لكل صنف.

بمجرد استخراج الميزات وتطبيق تسميات التدريب، نحسّن آلة متجهات داعمة خطية واحدة لكل صنف. نظراً لأن بيانات التدريب كبيرة جداً بحيث لا تتسع في الذاكرة، نتبنى طريقة تعدين السلبيات الصعبة القياسية [17، 37]. يتقارب تعدين السلبيات الصعبة بسرعة وفي الممارسة العملية يتوقف mAP عن الزيادة بعد مرور واحد فقط على جميع الصور.

في الملحق B نناقش سبب تعريف الأمثلة الإيجابية والسلبية بشكل مختلف في الضبط الدقيق مقابل تدريب آلة المتجهات الداعمة. نناقش أيضاً المقايضات المعنية في تدريب آلات المتجهات الداعمة للكشف بدلاً من مجرد استخدام المخرجات من طبقة softmax النهائية للشبكة العصبية الالتفافية المضبوطة بدقة.

### 2.4. النتائج على PASCAL VOC 2010-12

باتباع أفضل ممارسات PASCAL VOC [15]، قمنا بالتحقق من جميع القرارات التصميمية والمعاملات الفائقة على مجموعة بيانات VOC 2007 (القسم 3.2). للنتائج النهائية على مجموعات بيانات VOC 2010-12، قمنا بالضبط الدقيق للشبكة العصبية الالتفافية على VOC 2012 train وحسّنا آلات المتجهات الداعمة للكشف الخاصة بنا على VOC 2012 trainval. قدمنا نتائج الاختبار إلى خادم التقييم مرة واحدة فقط لكل من متغيري الخوارزمية الرئيسيين (مع وبدون انحدار صندوق التحديد).

يُظهر الجدول 1 النتائج الكاملة على VOC 2010. نقارن طريقتنا مع أربعة خطوط أساس قوية، بما في ذلك SegDPM [18]، الذي يجمع كواشف DPM مع مخرجات نظام التقسيم الدلالي [4] ويستخدم سياق إضافي بين الكواشف وإعادة تسجيل مصنف الصور. المقارنة الأكثر صلة هي مع نظام UVA من Uijlings وآخرين [39]، حيث تستخدم أنظمتنا نفس خوارزمية مقترحات المناطق. لتصنيف المناطق، تبني طريقتهم هرماً مكانياً من أربعة مستويات وتملأه بواصفات SIFT، Extended OpponentSIFT، وRGB-SIFT المأخوذة بكثافة، كل منها مُكمّم بناقل مع كتب رموز من 4000 كلمة. يتم التصنيف باستخدام آلة متجهات داعمة بنواة تقاطع الرسم البياني الهيستوغرامي. مقارنة بنهجهم متعدد الميزات وآلة المتجهات الداعمة بالنواة غير الخطية، نحقق تحسناً كبيراً في mAP، من 35.1% إلى 53.7% mAP، بينما نكون أيضاً أسرع بكثير (القسم 2.2). تحقق طريقتنا أداءً مماثلاً (53.3% mAP) على اختبار VOC 2011/12.

### 2.5. النتائج على كشف ILSVRC2013

قمنا بتشغيل R-CNN على مجموعة بيانات كشف ILSVRC2013 المكونة من 200 صنف باستخدام نفس المعاملات الفائقة للنظام التي استخدمناها لـ PASCAL VOC. اتبعنا نفس البروتوكول لتقديم نتائج الاختبار إلى خادم تقييم ILSVRC2013 مرتين فقط، مرة مع ومرة بدون انحدار صندوق التحديد.

يقارن الشكل 3 بين R-CNN والمشاركات في مسابقة ILSVRC 2013 ونتيجة OverFeat بعد المسابقة [34]. يحقق R-CNN mAP بنسبة 31.4%، وهو متقدم بشكل كبير على ثاني أفضل نتيجة بنسبة 24.3% من OverFeat. لإعطاء فكرة عن توزيع AP عبر الأصناف، يتم أيضاً عرض مخططات صندوقية وجدول APs لكل صنف يتبع في نهاية الورقة في الجدول 8. استخدمت معظم المشاركات المنافسة (OverFeat، NEC-MU، UvA-Euvision، Toronto A، وUIUC-IFP) الشبكات العصبية الالتفافية، مما يشير إلى أن هناك فروقاً دقيقة كبيرة في كيفية تطبيق الشبكات العصبية الالتفافية على كشف الأجسام، مما يؤدي إلى نتائج متباينة للغاية.

في القسم 4، نقدم نظرة عامة على مجموعة بيانات كشف ILSVRC2013 ونقدم تفاصيل حول الاختيارات التي قمنا بها عند تشغيل R-CNN عليها.

---

### Translation Notes

- **Figures referenced:** Figure 2 (warped training samples), Figure 3 (ILSVRC2013 results), Table 1 (VOC 2010 results), Table 8 (per-class APs)
- **Key terms introduced:** region proposals (مقترحات المناطق), selective search (البحث الانتقائي), feature extraction (استخراج الميزات), fine-tuning (الضبط الدقيق), hard negative mining (تعدين السلبيات الصعبة), bounding-box regression (انحدار صندوق التحديد)
- **Equations:** None in main text
- **Citations:** Multiple references [1-41] cited throughout
- **Special handling:**
  - Preserved technical acronyms: R-CNN, CNN, SVM, IoU, mAP, SGD, DPM
  - Translated dataset names consistently: PASCAL VOC, ILSVRC2013, ImageNet
  - Kept numeric values and percentages as-is
  - Maintained reference formatting [number]
  - Preserved mathematical notation (227×227, 2000×4096, etc.)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87
