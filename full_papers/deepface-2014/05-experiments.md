# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** dataset, benchmark, accuracy, training, evaluation, deep neural network, GPU, stochastic gradient descent, ensemble, ROC curve

---

### English Version

We evaluate the proposed DeepFace system, by learning the face representation on a very large-scale labeled face dataset collected online. In this section, we first introduce the datasets used in the experiments, then present the detailed evaluation and comparison with the state-of-the-art, as well as some insights and findings about learning and transferring the deep face representations.

## 5.1. Datasets

The proposed face representation is learned from a large collection of photos from Facebook, referred to as the Social Face Classification (SFC) dataset. The representations are then applied to the Labeled Faces in the Wild database (LFW), which is the de facto benchmark dataset for face verification in unconstrained environments, and the YouTube Faces (YTF) dataset, which is modeled similarly to the LFW but focuses on video clips.

The SFC dataset includes 4.4 million labeled faces from 4,030 people each with 800 to 1200 faces, where the most recent 5% of face images of each identity are left out for testing. This is done according to the images' time-stamp in order to simulate continuous identification through aging. The large number of images per person provides a unique opportunity for learning the invariance needed for the core problem of face recognition. We have validated using several automatic methods, that the identities used for training do not intersect with any of the identities in the below-mentioned datasets, by checking their name labels.

The LFW dataset [18] consists of 13,323 web photos of 5,749 celebrities which are divided into 6,000 face pairs in 10 splits. Performance is measured by mean recognition accuracy using A) the restricted protocol, in which only same and not same labels are available in training; B) the unrestricted protocol, where additional training pairs are accessible in training; and C) an unsupervised setting in which no training whatsoever is performed on LFW images.

The YTF dataset [30] collects 3,425 YouTube videos of 1,595 subjects (a subset of the celebrities in the LFW). These videos are divided into 5,000 video pairs and 10 splits and used to evaluate the video-level face verification.

The face identities in SFC were labeled by humans, which typically incorporate about 3% errors. Social face photos have even larger variations in image quality, lighting, and expressions than the web images of celebrities in the LFW and YTF which were normally taken by professional photographers rather than smartphones.

## 5.2. Training on the SFC

We first train the deep neural network on the SFC as a multi-class classification problem using a GPU-based engine, implementing the standard back-propagation on feed-forward nets by stochastic gradient descent (SGD) with momentum (set to 0.9). Our mini-batch size is 128, and we have set an equal learning rate for all trainable layers to 0.01, which was manually decreased, each time by an order of magnitude once the validation error stopped decreasing, to a final rate of 0.0001. We initialized the weights in each layer from a zero-mean Gaussian distribution with σ = 0.01, and biases are set to 0.5. We trained the network for roughly 15 sweeps (epochs) over the whole data which took 3 days. As described in Sec. 3, the responses of the fully connected layer F7 are extracted to serve as the face representation.

We evaluated different design choices of DNN in terms of the classification error on 5% data of SFC as the test set. This validated the necessity of using a large-scale face dataset and a deep architecture. First, we vary the train/test dataset size by using a subset of the persons in the SFC. Subsets of sizes 1.5K, 3K and 4K persons (1.5M, 3.3M, and 4.4M faces, respectively) are used. Using the architecture in Fig. 2, we trained three networks, denoted by DF-1.5K, DF-3.3K, and DF-4.4K. Table 1 (left column) shows that the classification error grows only modestly from 7.0% on 1.5K persons to 7.2% when classifying 3K persons, which indicates that the capacity of the network can well accommodate the scale of 3M training images. The error rate rises to 8.7% for 4K persons with 4.4M images, showing the network scales comfortably to more persons. We've also varied the global number of samples in SFC to 10%, 20%, 50%, leaving the number of identities in place, denoted by DF-10%, DF-20%, DF-50% in the middle column of Table 1. We observed the test errors rise up to 20.7%, because of overfitting on the reduced training set. Since performance does not saturate at 4M images, this shows that the network would benefit from even larger datasets.

We also vary the depth of the networks by chopping off the C3 layer, the two local L4 and L5 layers, or all these 3 layers, referred respectively as DF-sub1, DF-sub2, and DF-sub3. For example, only four trainable layers remain in DF-sub3 which is a considerably shallower structure compared to the 9 layers of the proposed network in Fig. 2. In training such networks with 4.4M faces, the classification errors stop decreasing after a few epochs and remains at a level higher than that of the deep network, as can be seen in Table 1 (right column). This verifies the necessity of network depth when training on a large face dataset.

## 5.3. Results on the LFW dataset

The vision community has made significant progress on face verification in unconstrained environments in recent years. The mean recognition accuracy on LFW [18] marches steadily towards the human performance of over 97.5% [20]. Given some very hard cases due to aging effects, large lighting and face pose variations in LFW, any improvement over the state-of-the-art is very remarkable and the system has to be composed by highly optimized modules. There is a strong diminishing return effect and any progress now requires a substantial effort to reduce the number of errors of state-of-the-art methods. DeepFace couples large feedforward-based models with fine 3D alignment. Regarding the importance of each component: 1) Without frontalization: when using only the 2D alignment, the obtained accuracy is "only" 94.3%. Without alignment at all, i.e., using the center crop of face detection, the accuracy is 87.9% as parts of the facial region may fall out of the crop. 2) Without learning: when using frontalization only, and a naive LBP/SVM combination, the accuracy is 91.4% which is already notable given the simplicity of such a classifier.

All the LFW images are processed in the same pipeline that was used to train on the SFC dataset, denoted as DeepFace-single. To evaluate the discriminative capability of the face representation in isolation, we follow the unsupervised setting to directly compare the inner product of a pair of normalized features. Quite remarkably, this achieves a mean accuracy of 95.92% which is almost on par with the best performance to date, achieved by supervised transfer learning [5]. Next, we learn a kernel SVM (with C=1) on top of the χ²-distance vector (Sec. 4.1) following the restricted protocol, i.e., where only the 5,400 pair labels per split are available for the SVM training. This achieves an accuracy 97.00%, reducing significantly the error of the state-of-the-art [7, 5], see Table 3.

**Ensembles of DNNs** Next, we combine multiple networks trained by feeding different types of inputs to the DNN: 1) The network DeepFace-single described above based on 3D aligned RGB inputs; 2) The gray-level image plus image gradient magnitude and orientation; and 3) the 2D-aligned RGB images. We combine those distances using a non-linear SVM (with C=1) with a simple sum of power CPD-kernels: $K_{Combined} := K_{single} + K_{gradient} + K_{align2d}$, where $K(x, y) := -||x - y||^2$, and following the restricted protocol, achieve an accuracy 97.15%.

The unrestricted protocol provides the operator with knowledge about the identities in the training sets, hence enabling the generation of many more training pairs to be added to the training set. We further experiment with training a Siamese Network (Sec. 4.2) to learn a verification metric by fine-tuning the Siamese's (shared) pre-trained feature extractor. Following this procedure, we have observed substantial overfitting to the training data. The training pairs generated using the LFW training data are redundant as they are generated out of roughly 9K photos, which are insufficient to reliably estimate more than 120M parameters. To address these issues, we have collected an additional dataset following the same procedure as with the SFC, containing an additional new 100K identities, each with only 30 samples to generate same and not-same pairs from. We then trained the Siamese Network on it followed by 2 training epochs on the LFW unrestricted training splits to correct for some of the data set dependent biases. The slightly-refined representation is handled similarly as before. Combining it into the above-mentioned ensemble, i.e., $K_{Combined} += K_{Siamese}$, yields the accuracy 97.25%, under the unrestricted protocol. By adding four additional DeepFace-single networks to the ensemble, each trained from scratch with different random seeds, i.e., $K_{Combined} += \sum K_{DeepFace-Single}$, the obtained accuracy is 97.35%. The performances of the individual networks, before combination, are presented in Table 2.

The comparisons with the recent state-of-the-art methods in terms of the mean accuracy and ROC curves are presented in Table 3 and Fig. 3, including human performance on the cropped faces. The proposed DeepFace method advances the state-of-the-art, closely approaching human performance in face verification.

## 5.4. Results on the YTF dataset

We further validate DeepFace on the recent video-level face verification dataset. The image quality of YouTube video frames is generally worse than that of web photos, mainly due to motion blur or viewing distance. We employ the DeepFace-single representation directly by creating, for every pair of training videos, 50 pairs of frames, one from each video, and label these as same or not-same in accordance with the video training pair. Then a weighted χ² model is learned as in Sec. 4.1. Given a test-pair, we sample 100 random pairs of frames, one from each video, and use the mean value of the learned weighed similarity.

The comparison with recent methods is shown in Table 4 and Fig. 4. We report an accuracy of 91.4% which reduces the error of the previous best methods by more than 50%. Note that there are about 100 wrong labels for video pairs, recently updated to the YTF webpage. After these are corrected, DeepFace-single actually reaches 92.5%. This experiment verifies again that the DeepFace method easily generalizes to a new target domain.

## 5.5. Computational efficiency

We have efficiently implemented a CPU-based feed-forward operator, which exploits both the CPU's Single Instruction Multiple Data (SIMD) instructions and its cache by leveraging the locality of floating-point computations across the kernels and the image. Using a single core Intel 2.2GHz CPU, the operator takes 0.18 seconds to extract features from the raw input pixels. Efficient warping techniques were implemented for alignment; alignment alone takes about 0.05 seconds. Overall, the DeepFace runs at 0.33 seconds per image, accounting for image decoding, face detection and alignment, the feedforward network, and the final classification output.

---

### النسخة العربية

نقيّم نظام DeepFace المقترح، من خلال تعلم تمثيل الوجه على مجموعة بيانات وجوه مُسمَّاة واسعة النطاق جدًا تم جمعها عبر الإنترنت. في هذا القسم، نقدم أولاً مجموعات البيانات المستخدمة في التجارب، ثم نقدم التقييم التفصيلي والمقارنة مع أحدث التقنيات، بالإضافة إلى بعض الرؤى والنتائج حول تعلم ونقل تمثيلات الوجه العميقة.

## 5.1. مجموعات البيانات

يتم تعلم تمثيل الوجه المقترح من مجموعة كبيرة من الصور من Facebook، يشار إليها باسم مجموعة بيانات تصنيف الوجوه الاجتماعية (SFC). يتم بعد ذلك تطبيق التمثيلات على قاعدة بيانات Labeled Faces in the Wild (LFW)، وهي المعيار الفعلي لمجموعة بيانات التحقق من الوجوه في البيئات غير المقيدة، ومجموعة بيانات YouTube Faces (YTF)، التي تم تصميمها بشكل مماثل لـ LFW ولكنها تركز على مقاطع الفيديو.

تتضمن مجموعة بيانات SFC 4.4 مليون وجه مُسمَّى من 4,030 شخصًا كل منهم لديه من 800 إلى 1200 وجه، حيث يتم استبعاد أحدث 5% من صور الوجوه لكل هوية للاختبار. يتم ذلك وفقًا للطابع الزمني للصور من أجل محاكاة التعريف المستمر من خلال الشيخوخة. يوفر العدد الكبير من الصور لكل شخص فرصة فريدة لتعلم الثبات اللازم للمشكلة الأساسية للتعرف على الوجوه. لقد تحققنا باستخدام عدة طرق تلقائية، من أن الهويات المستخدمة للتدريب لا تتقاطع مع أي من الهويات في مجموعات البيانات المذكورة أدناه، من خلال فحص تسميات أسمائها.

تتكون مجموعة بيانات LFW [18] من 13,323 صورة ويب لـ 5,749 من المشاهير والتي تنقسم إلى 6,000 زوج وجوه في 10 تقسيمات. يتم قياس الأداء من خلال متوسط دقة التعرف باستخدام أ) البروتوكول المقيد، الذي تتوفر فيه فقط تسميات نفس وليس نفس في التدريب؛ ب) البروتوكول غير المقيد، حيث يمكن الوصول إلى أزواج تدريب إضافية في التدريب؛ و ج) إعداد غير خاضع للإشراف لا يتم فيه إجراء أي تدريب على الإطلاق على صور LFW.

تجمع مجموعة بيانات YTF [30] 3,425 مقطع فيديو من YouTube لـ 1,595 موضوعًا (مجموعة فرعية من المشاهير في LFW). يتم تقسيم مقاطع الفيديو هذه إلى 5,000 زوج فيديو و10 تقسيمات وتُستخدم لتقييم التحقق من الوجه على مستوى الفيديو.

تم وسم هويات الوجوه في SFC بواسطة البشر، والتي عادة ما تتضمن حوالي 3% أخطاء. تحتوي صور الوجوه الاجتماعية على تباينات أكبر في جودة الصورة والإضاءة والتعبيرات من صور الويب للمشاهير في LFW و YTF والتي تم التقاطها عادةً بواسطة مصورين محترفين بدلاً من الهواتف الذكية.

## 5.2. التدريب على SFC

ندرب أولاً الشبكة العصبية العميقة على SFC كمشكلة تصنيف متعددة الفئات باستخدام محرك قائم على وحدة معالجة الرسومات، وتنفيذ الانتشار العكسي القياسي على شبكات التغذية الأمامية بواسطة الانحدار التدرجي العشوائي (SGD) مع الزخم (مضبوط على 0.9). حجم دفعتنا الصغيرة هو 128، وقد حددنا معدل تعلم متساو لجميع الطبقات القابلة للتدريب عند 0.01، والذي تم تخفيضه يدويًا، في كل مرة بمقدار درجة من حيث الحجم بمجرد توقف خطأ التحقق عن الانخفاض، إلى معدل نهائي قدره 0.0001. قمنا بتهيئة الأوزان في كل طبقة من توزيع غاوسي صفري المتوسط مع σ = 0.01، ويتم ضبط الانحيازات على 0.5. دربنا الشبكة لحوالي 15 دورة (epochs) على جميع البيانات والتي استغرقت 3 أيام. كما هو موضح في القسم 3، يتم استخراج استجابات الطبقة المتصلة بالكامل F7 لتكون بمثابة تمثيل الوجه.

قمنا بتقييم خيارات التصميم المختلفة للشبكة العصبية العميقة من حيث خطأ التصنيف على 5% من بيانات SFC كمجموعة اختبار. وهذا أكد ضرورة استخدام مجموعة بيانات وجوه واسعة النطاق ومعمارية عميقة. أولاً، نغير حجم مجموعة بيانات التدريب/الاختبار باستخدام مجموعة فرعية من الأشخاص في SFC. يتم استخدام مجموعات فرعية بأحجام 1.5K و 3K و 4K شخص (1.5 مليون و 3.3 مليون و 4.4 مليون وجه، على التوالي). باستخدام المعمارية في الشكل 2، قمنا بتدريب ثلاث شبكات، يُشار إليها بـ DF-1.5K و DF-3.3K و DF-4.4K. يوضح الجدول 1 (العمود الأيسر) أن خطأ التصنيف ينمو بشكل متواضع فقط من 7.0% على 1.5K شخص إلى 7.2% عند تصنيف 3K شخص، مما يشير إلى أن سعة الشبكة يمكن أن تستوعب بشكل جيد حجم 3 ملايين صورة تدريب. يرتفع معدل الخطأ إلى 8.7% لـ 4K شخص مع 4.4 مليون صورة، مما يُظهر أن الشبكة تتوسع بشكل مريح لمزيد من الأشخاص. لقد غيرنا أيضًا العدد الإجمالي للعينات في SFC إلى 10% و 20% و 50%، مع ترك عدد الهويات في مكانها، يُشار إليها بـ DF-10% و DF-20% و DF-50% في العمود الأوسط من الجدول 1. لاحظنا أن أخطاء الاختبار ترتفع إلى 20.7%، بسبب فرط الملاءمة على مجموعة التدريب المخفضة. نظرًا لأن الأداء لا يتشبع عند 4 ملايين صورة، فهذا يُظهر أن الشبكة ستستفيد من مجموعات بيانات أكبر.

نغير أيضًا عمق الشبكات عن طريق قطع طبقة C3، أو طبقتي L4 و L5 المحليتين، أو كل هذه الطبقات الثلاث، المشار إليها على التوالي باسم DF-sub1 و DF-sub2 و DF-sub3. على سبيل المثال، تبقى أربع طبقات قابلة للتدريب فقط في DF-sub3 وهي بنية أقل عمقًا بكثير مقارنة بـ 9 طبقات من الشبكة المقترحة في الشكل 2. في تدريب مثل هذه الشبكات بـ 4.4 مليون وجه، تتوقف أخطاء التصنيف عن الانخفاض بعد بضع حقب وتبقى عند مستوى أعلى من مستوى الشبكة العميقة، كما يمكن رؤيته في الجدول 1 (العمود الأيمن). هذا يؤكد ضرورة عمق الشبكة عند التدريب على مجموعة بيانات وجوه كبيرة.

## 5.3. النتائج على مجموعة بيانات LFW

حققت مجتمع الرؤية تقدمًا كبيرًا في التحقق من الوجوه في البيئات غير المقيدة في السنوات الأخيرة. يتحرك متوسط دقة التعرف على LFW [18] بثبات نحو الأداء البشري البالغ أكثر من 97.5% [20]. في ظل بعض الحالات الصعبة جدًا بسبب تأثيرات الشيخوخة وتباينات الإضاءة الكبيرة ووضعيات الوجه في LFW، فإن أي تحسين على أحدث التقنيات ملحوظ جدًا ويجب أن يكون النظام مكونًا من وحدات محسّنة للغاية. هناك تأثير عوائد متناقصة قوي وأي تقدم الآن يتطلب جهدًا كبيرًا لتقليل عدد أخطاء طرق أحدث التقنيات. يقترن DeepFace بنماذج كبيرة قائمة على التغذية الأمامية مع محاذاة ثلاثية الأبعاد دقيقة. فيما يتعلق بأهمية كل مكون: 1) بدون التحويل الأمامي: عند استخدام المحاذاة ثنائية الأبعاد فقط، تكون الدقة المحصلة "فقط" 94.3%. بدون محاذاة على الإطلاق، أي باستخدام الاقتصاص المركزي لاكتشاف الوجه، تكون الدقة 87.9% حيث قد تسقط أجزاء من منطقة الوجه خارج الاقتصاص. 2) بدون التعلم: عند استخدام التحويل الأمامي فقط، ومزيج LBP/SVM ساذج، تكون الدقة 91.4% وهو بالفعل ملحوظ نظرًا لبساطة مثل هذا المصنف.

يتم معالجة جميع صور LFW في نفس خط الأنابيب الذي تم استخدامه للتدريب على مجموعة بيانات SFC، يُشار إليه باسم DeepFace-single. لتقييم القدرة التمييزية لتمثيل الوجه بشكل منفصل، نتبع الإعداد غير الخاضع للإشراف لمقارنة الضرب الداخلي لزوج من الميزات المطبَّعة مباشرة. بشكل ملحوظ للغاية، هذا يحقق متوسط دقة 95.92% وهو تقريبًا على قدم المساواة مع أفضل أداء حتى الآن، والذي تم تحقيقه من خلال تعلم النقل الخاضع للإشراف [5]. بعد ذلك، نتعلم kernel SVM (مع C=1) على متجه مسافة χ² (القسم 4.1) باتباع البروتوكول المقيد، أي حيث تتوفر فقط 5,400 تسمية زوج لكل تقسيم لتدريب SVM. هذا يحقق دقة 97.00%، مما يقلل بشكل كبير خطأ أحدث التقنيات [7، 5]، انظر الجدول 3.

**مجموعات الشبكات العصبية العميقة** بعد ذلك، نجمع شبكات متعددة مدربة من خلال تغذية أنواع مختلفة من المدخلات إلى الشبكة العصبية العميقة: 1) الشبكة DeepFace-single الموصوفة أعلاه بناءً على مدخلات RGB محاذاة ثلاثية الأبعاد؛ 2) الصورة ذات المستوى الرمادي بالإضافة إلى حجم واتجاه تدرج الصورة؛ و 3) صور RGB المحاذاة ثنائية الأبعاد. نجمع تلك المسافات باستخدام SVM غير خطي (مع C=1) مع مجموع بسيط من نوى CPD القوية: $K_{Combined} := K_{single} + K_{gradient} + K_{align2d}$، حيث $K(x, y) := -||x - y||^2$، وباتباع البروتوكول المقيد، نحقق دقة 97.15%.

يوفر البروتوكول غير المقيد للمشغل معرفة بالهويات في مجموعات التدريب، وبالتالي تمكين إنشاء العديد من أزواج التدريب الإضافية لإضافتها إلى مجموعة التدريب. نجري مزيدًا من التجارب مع تدريب شبكة سيامية (القسم 4.2) لتعلم مقياس تحقق من خلال ضبط دقيق لمستخرج الميزات المُدرَّب مسبقًا للسيامية (المشترك). باتباع هذا الإجراء، لاحظنا فرط ملاءمة كبيرًا على بيانات التدريب. الأزواج التدريبية المولدة باستخدام بيانات تدريب LFW زائدة عن الحاجة حيث يتم إنشاؤها من حوالي 9K صورة، والتي غير كافية لتقدير أكثر من 120 مليون معامل بشكل موثوق. لمعالجة هذه المشكلات، قمنا بجمع مجموعة بيانات إضافية باتباع نفس الإجراء كما هو الحال مع SFC، تحتوي على 100K هوية جديدة إضافية، كل منها مع 30 عينة فقط لإنشاء أزواج نفس وليس نفس منها. ثم قمنا بتدريب الشبكة السيامية عليها متبوعة بحقبتي تدريب على تقسيمات تدريب LFW غير المقيدة لتصحيح بعض الانحيازات التابعة لمجموعة البيانات. يتم التعامل مع التمثيل المحسن قليلاً بشكل مشابه كما كان من قبل. دمجه في المجموعة المذكورة أعلاه، أي $K_{Combined} += K_{Siamese}$، ينتج دقة 97.25%، بموجب البروتوكول غير المقيد. من خلال إضافة أربع شبكات DeepFace-single إضافية إلى المجموعة، كل منها مدرب من الصفر ببذور عشوائية مختلفة، أي $K_{Combined} += \sum K_{DeepFace-Single}$، تكون الدقة المحصلة 97.35%. يتم تقديم أداء الشبكات الفردية، قبل الجمع، في الجدول 2.

تُقدَّم المقارنات مع طرق أحدث التقنيات الحديثة من حيث متوسط الدقة ومنحنيات ROC في الجدول 3 والشكل 3، بما في ذلك الأداء البشري على الوجوه المقتصة. تقدم طريقة DeepFace المقترحة أحدث التقنيات، مقتربة بشكل وثيق من الأداء البشري في التحقق من الوجوه.

## 5.4. النتائج على مجموعة بيانات YTF

نؤكد صحة DeepFace بشكل أكبر على مجموعة بيانات التحقق من الوجوه على مستوى الفيديو الحديثة. جودة صورة إطارات فيديو YouTube بشكل عام أسوأ من صور الويب، ويرجع ذلك أساسًا إلى ضبابية الحركة أو مسافة المشاهدة. نستخدم تمثيل DeepFace-single مباشرة عن طريق إنشاء، لكل زوج من مقاطع الفيديو التدريبية، 50 زوجًا من الإطارات، واحد من كل فيديو، ونسمّي هذه كنفس أو ليس نفس وفقًا لزوج الفيديو التدريبي. ثم يتم تعلم نموذج χ² موزون كما في القسم 4.1. في حالة زوج اختبار، نأخذ عينة من 100 زوج عشوائي من الإطارات، واحد من كل فيديو، ونستخدم القيمة المتوسطة للتشابه الموزون المتعلم.

تُظهَر المقارنة مع الطرق الحديثة في الجدول 4 والشكل 4. نُبلغ عن دقة 91.4% مما يقلل خطأ أفضل الطرق السابقة بأكثر من 50%. لاحظ أن هناك حوالي 100 تسمية خاطئة لأزواج الفيديو، تم تحديثها مؤخرًا إلى صفحة ويب YTF. بعد تصحيح هذه، يصل DeepFace-single في الواقع إلى 92.5%. تؤكد هذه التجربة مرة أخرى أن طريقة DeepFace تتعمم بسهولة على مجال مستهدف جديد.

## 5.5. الكفاءة الحسابية

لقد نفذنا بكفاءة مشغل تغذية أمامية قائم على وحدة المعالجة المركزية، والذي يستغل كل من تعليمات SIMD لوحدة المعالجة المركزية وذاكرتها التخزينية المؤقتة من خلال الاستفادة من محلية الحسابات ذات الفاصلة العائمة عبر النوى والصورة. باستخدام وحدة معالجة مركزية Intel أحادية النواة بسرعة 2.2 جيجاهرتز، يستغرق المشغل 0.18 ثانية لاستخراج الميزات من بكسلات الإدخال الخام. تم تنفيذ تقنيات تشويه فعالة للمحاذاة؛ تستغرق المحاذاة وحدها حوالي 0.05 ثانية. بشكل عام، يعمل DeepFace بسرعة 0.33 ثانية لكل صورة، مع احتساب فك تشفير الصورة واكتشاف الوجه والمحاذاة وشبكة التغذية الأمامية ومخرج التصنيف النهائي.

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 3 (ROC curves on LFW), Figure 4 (ROC curves on YTF)
- **Tables referenced:** Table 1, Table 2, Table 3, Table 4
- **Key terms introduced:**
  - Social Face Classification (تصنيف الوجوه الاجتماعية)
  - Labeled Faces in the Wild (Labeled Faces in the Wild)
  - YouTube Faces (YouTube Faces)
  - De facto benchmark (المعيار الفعلي)
  - Restricted protocol (البروتوكول المقيد)
  - Unrestricted protocol (البروتوكول غير المقيد)
  - Mini-batch (دفعة صغيرة)
  - Learning rate (معدل التعلم)
  - Momentum (زخم)
  - Epochs (حقب/epochs)
  - Validation error (خطأ التحقق)
  - Overfitting (فرط الملاءمة)
  - Network depth (عمق الشبكة)
  - Diminishing return (عوائد متناقصة)
  - Ensemble (مجموعة)
  - ROC curves (منحنيات ROC)
  - Video-level verification (التحقق على مستوى الفيديو)
  - Motion blur (ضبابية الحركة)
  - SIMD instructions (تعليمات SIMD)
- **Equations:**
  - Kernel combination formulas
- **Citations:** [5], [7], [18], [20], [30]
- **Special handling:**
  - Kept dataset names (SFC, LFW, YTF) as is
  - Preserved network variant names (DF-1.5K, DF-3.3K, etc.)
  - Maintained accuracy percentages and numerical values
  - Kept protocol names in context

### Quality Metrics

- **Semantic equivalence:** 0.88
- **Technical accuracy:** 0.89
- **Readability:** 0.87
- **Glossary consistency:** 0.88
- **Overall section score:** 0.88

### Back-translation Check

Key sentences:
"تتضمن مجموعة بيانات SFC 4.4 مليون وجه مُسمَّى من 4,030 شخصًا"
→ "The SFC dataset includes 4.4 million labeled faces from 4,030 people"
✓ Accurate

"نحقق دقة 97.00%، مما يقلل بشكل كبير خطأ أحدث التقنيات"
→ "This achieves an accuracy of 97.00%, significantly reducing the error of state-of-the-art"
✓ Semantically equivalent
