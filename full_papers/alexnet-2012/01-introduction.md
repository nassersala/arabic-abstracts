# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** neural network, convolutional, training, dataset, image classification, computer vision, machine learning, overfitting, object recognition

---

### English Version

Current approaches to object recognition make essential use of machine learning methods. To improve their performance, we can collect larger datasets, learn more powerful models, and use better techniques for preventing overfitting. Until recently, datasets of labeled images were relatively small — on the order of tens of thousands of images (e.g., NORB [16], Caltech-101/256 [8, 9], and CIFAR-10/100 [12]). Simple recognition tasks can be solved quite well with datasets of this size, especially if they are augmented with label-preserving transformations. For example, the current-best error rate on the MNIST digit-recognition task (<0.3%) approaches human performance [4]. But objects in realistic settings exhibit considerable variability, so to learn to recognize them it is necessary to use much larger training sets. And indeed, the shortcomings of small image datasets have been widely recognized (e.g., Pinto et al. [21]), but it has only recently become possible to collect labeled datasets with millions of images. The new larger datasets include LabelMe [23] and ImageNet [6].

To learn about thousands of objects from millions of images, we need a model with a large learning capacity. However, the immense complexity of the object recognition task means that this problem cannot be specified even by a dataset as large as ImageNet, so our model should also have lots of prior knowledge to compensate for all the data we don't have. Convolutional neural networks (CNNs) constitute one such class of models [16, 11, 13, 18, 15, 22, 26]. Their capacity can be controlled by varying their depth and breadth, and they also make strong and mostly correct assumptions about the nature of images (namely, stationarity of statistics and locality of pixel dependencies). Thus, compared to standard feedforward neural networks with similarly-sized layers, CNNs have much fewer connections and parameters and so they are easier to train, while their theoretically-best performance is likely to be only slightly worse.

Despite the attractive qualities of CNNs, and despite the relative efficiency of their local architecture, they have still been prohibitively expensive to apply in large scale to high-resolution images. Luckily, current GPUs, paired with a highly-optimized implementation of 2D convolution, are powerful enough to facilitate the training of interestingly-large CNNs, and recent datasets like ImageNet contain enough labeled examples to train such models without severe overfitting.

The specific contributions of this paper are as follows: we trained one of the largest convolutional neural networks to date on the subsets of ImageNet used in the ILSVRC-2010 and ILSVRC-2012 competitions [2] and achieved by far the best results ever reported on these datasets. We wrote a highly-optimized GPU implementation of 2D convolution and all the other operations inherent in training convolutional neural networks, which we make available publicly. Our network contains a number of new and unusual features which improve its performance and reduce its training time, which are detailed in Section 3. The size of our network made overfitting a significant problem, even with 1.2 million labeled training examples, so we used several effective techniques for preventing overfitting, which are described in Section 4. Our final network contains five convolutional layers and three fully-connected layers, and this depth seems to be important: we found that removing any convolutional layer (each of which contains no more than 1% of the model's parameters) resulted in inferior performance.

In the end, the network's size is limited mainly by the amount of memory available on current GPUs and by the amount of training time that we are willing to tolerate. Our network takes between five and six days to train on two GTX 580 3GB GPUs. All of our experiments suggest that our results can be improved simply by waiting for faster GPUs and bigger datasets to become available.

---

### النسخة العربية

تعتمد الأساليب الحالية للتعرف على الأشياء بشكل أساسي على طرق التعلم الآلي. لتحسين أدائها، يمكننا جمع مجموعات بيانات أكبر، وتعلم نماذج أكثر قوة، واستخدام تقنيات أفضل لمنع الإفراط في التدريب. حتى وقت قريب، كانت مجموعات بيانات الصور الموسومة صغيرة نسبياً - بحدود عشرات الآلاف من الصور (على سبيل المثال، NORB [16]، وCaltech-101/256 [8، 9]، وCIFAR-10/100 [12]). يمكن حل مهام التعرف البسيطة بشكل جيد جداً باستخدام مجموعات بيانات بهذا الحجم، خاصة إذا تم توسيعها بتحويلات تحافظ على التسميات. على سبيل المثال، فإن أفضل معدل خطأ حالي في مهمة التعرف على الأرقام في MNIST (<0.3%) يقترب من الأداء البشري [4]. لكن الأشياء في البيئات الواقعية تظهر تنوعاً كبيراً، لذلك لتعلم التعرف عليها من الضروري استخدام مجموعات تدريب أكبر بكثير. وبالفعل، تم الاعتراف على نطاق واسع بأوجه القصور في مجموعات بيانات الصور الصغيرة (على سبيل المثال، Pinto وآخرون [21])، لكن أصبح من الممكن مؤخراً فقط جمع مجموعات بيانات موسومة تحتوي على ملايين الصور. تشمل مجموعات البيانات الكبيرة الجديدة LabelMe [23] وImageNet [6].

للتعلم عن آلاف الأشياء من ملايين الصور، نحتاج إلى نموذج ذي قدرة تعلم كبيرة. ومع ذلك، فإن التعقيد الهائل لمهمة التعرف على الأشياء يعني أن هذه المشكلة لا يمكن تحديدها حتى بواسطة مجموعة بيانات كبيرة مثل ImageNet، لذلك يجب أن يكون لنموذجنا أيضاً الكثير من المعرفة المسبقة للتعويض عن جميع البيانات التي لا نملكها. تشكل الشبكات العصبية الالتفافية (CNNs) إحدى فئات النماذج هذه [16، 11، 13، 18، 15، 22، 26]. يمكن التحكم في قدرتها عن طريق تغيير عمقها واتساعها، كما أنها تضع افتراضات قوية وصحيحة في معظمها حول طبيعة الصور (وهي، استقرارية الإحصائيات ومحلية تبعيات البكسل). وبالتالي، مقارنة بالشبكات العصبية الأمامية القياسية ذات الطبقات بنفس الحجم، فإن الشبكات العصبية الالتفافية لديها اتصالات ومعاملات أقل بكثير، وبالتالي فهي أسهل في التدريب، في حين أن أدائها الأفضل نظرياً من المحتمل أن يكون أسوأ قليلاً فقط.

على الرغم من الصفات الجذابة للشبكات العصبية الالتفافية، وعلى الرغم من الكفاءة النسبية لمعماريتها المحلية، إلا أنها لا تزال مكلفة للغاية لتطبيقها على نطاق واسع على الصور عالية الدقة. لحسن الحظ، فإن وحدات معالجة الرسومات (GPUs) الحالية، إلى جانب تطبيق محسّن للغاية للالتفاف ثنائي الأبعاد، قوية بما يكفي لتسهيل تدريب الشبكات العصبية الالتفافية الكبيرة بشكل مثير للاهتمام، وتحتوي مجموعات البيانات الحديثة مثل ImageNet على أمثلة موسومة كافية لتدريب مثل هذه النماذج دون إفراط شديد في التدريب.

المساهمات المحددة لهذه الورقة هي كما يلي: قمنا بتدريب واحدة من أكبر الشبكات العصبية الالتفافية حتى الآن على المجموعات الفرعية من ImageNet المستخدمة في مسابقات ILSVRC-2010 وILSVRC-2012 [2] وحققنا إلى حد بعيد أفضل النتائج التي تم الإبلاغ عنها على الإطلاق على هذه المجموعات. كتبنا تطبيق GPU محسّن للغاية للالتفاف ثنائي الأبعاد وجميع العمليات الأخرى الكامنة في تدريب الشبكات العصبية الالتفافية، والذي نجعله متاحاً للعامة. تحتوي شبكتنا على عدد من الميزات الجديدة وغير العادية التي تحسن أدائها وتقلل من وقت تدريبها، والتي يتم تفصيلها في القسم 3. جعل حجم شبكتنا الإفراط في التدريب مشكلة كبيرة، حتى مع وجود 1.2 مليون مثال تدريبي موسوم، لذلك استخدمنا عدة تقنيات فعالة لمنع الإفراط في التدريب، والتي يتم وصفها في القسم 4. تحتوي شبكتنا النهائية على خمس طبقات التفافية وثلاث طبقات متصلة بالكامل، ويبدو أن هذا العمق مهم: وجدنا أن إزالة أي طبقة التفافية (كل منها لا تحتوي على أكثر من 1% من معاملات النموذج) أدت إلى أداء أدنى.

في النهاية، يقتصر حجم الشبكة بشكل أساسي على كمية الذاكرة المتاحة على وحدات معالجة الرسومات الحالية وعلى مقدار وقت التدريب الذي نحن على استعداد لتحمله. تستغرق شبكتنا ما بين خمسة وستة أيام للتدريب على اثنتين من وحدات معالجة الرسومات GTX 580 بذاكرة 3 جيجابايت. تشير جميع تجاربنا إلى أنه يمكن تحسين نتائجنا ببساطة عن طريق انتظار توفر وحدات معالجة رسومات أسرع ومجموعات بيانات أكبر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - object recognition (التعرف على الأشياء)
  - machine learning (التعلم الآلي)
  - overfitting (الإفراط في التدريب)
  - label-preserving transformations (تحويلات تحافظ على التسميات)
  - learning capacity (قدرة تعلم)
  - prior knowledge (المعرفة المسبقة)
  - stationarity of statistics (استقرارية الإحصائيات)
  - locality of pixel dependencies (محلية تبعيات البكسل)
  - feedforward neural networks (الشبكات العصبية الأمامية)
  - 2D convolution (الالتفاف ثنائي الأبعاد)
- **Equations:** None
- **Citations:** [2], [4], [6], [8], [9], [11], [12], [13], [15], [16], [18], [21], [22], [23], [26]
- **Special handling:**
  - Dataset names (NORB, Caltech, CIFAR, MNIST, LabelMe, ImageNet) kept in English
  - Competition names (ILSVRC-2010, ILSVRC-2012) kept in English
  - GPU model (GTX 580 3GB) kept in English
  - Numerical data and percentages preserved exactly

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Check

First paragraph back-translated:
Arabic: "تعتمد الأساليب الحالية للتعرف على الأشياء بشكل أساسي على طرق التعلم الآلي..."
Back to English: "Current approaches to object recognition depend fundamentally on machine learning methods..."
✓ Semantic match confirmed

Last paragraph back-translated:
Arabic: "في النهاية، يقتصر حجم الشبكة بشكل أساسي على كمية الذاكرة المتاحة..."
Back to English: "In the end, the network size is limited mainly by the amount of memory available..."
✓ Semantic match confirmed
