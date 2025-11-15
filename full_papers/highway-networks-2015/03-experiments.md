# Section 3: Experiments
## القسم 3: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** training, SGD, momentum, learning rate, convolutional, activation function, rectified linear, validation set, hyperparameter, initialization, MNIST, CIFAR-10, CIFAR-100, dataset, accuracy, test set, optimization, network depth

---

### English Version

All networks were trained using SGD with momentum. An exponentially decaying learning rate was used in Section 3.1. For the rest of the experiments, a simpler commonly used strategy was employed where the learning rate starts at a value λ and decays according to a fixed schedule by a factor γ. λ, γ and the schedule were selected once based on validation set performance on the CIFAR-10 dataset, and kept fixed for all experiments. All convolutional highway networks utilize the rectified linear activation function [16] to compute the block state H. To provide a better estimate of the variability of classification results due to random initialization, we report our results in the format Best (mean ± std.dev.) based on 5 runs wherever available. Experiments were conducted using Caffe [33] and Brainstorm (https://github.com/IDSIA/brainstorm) frameworks. Source code, hyperparameter search results and related scripts are publicly available at http://people.idsia.ch/˜rupesh/very_deep_learning/.

### 3.1 Optimization

To support the hypothesis that highway networks do not suffer from increasing depth, we conducted a series of rigorous optimization experiments, comparing them to plain networks with normalized initialization [16, 17].

We trained both plain and highway networks of varying varying depths on the MNIST digit classification dataset. All networks are thin: each layer has 50 blocks for highway networks and 71 units for plain networks, yielding roughly identical numbers of parameters (≈5000) per layer. In all networks, the first layer is a fully connected plain layer followed by 9, 19, 49, or 99 fully connected plain or highway layers. Finally, the network output is produced by a softmax layer. We performed a random search of 100 runs for both plain and highway networks to find good settings for the following hyperparameters: initial learning rate, momentum, learning rate exponential decay factor & activation function (either rectified linear or tanh). For highway networks, an additional hyperparameter was the initial value for the transform gate bias (between -1 and -10). Other weights were initialized using the same normalized initialization as plain networks.

The training curves for the best performing networks for each depth are shown in Figure 1. As expected, 10 and 20-layer plain networks exhibit very good performance (mean loss < 1e−4), which significantly degrades as depth increases, even though network capacity increases. Highway networks do not suffer from an increase in depth, and 50/100 layer highway networks perform similar to 10/20 layer networks. The 100-layer highway network performed more than 2 orders of magnitude better compared to a similarly-sized plain network. It was also observed that highway networks consistently converged significantly faster than plain ones.

### 3.2 Pilot Experiments on MNIST Digit Classification

As a sanity check for the generalization capability of highway networks, we trained 10-layer convolutional highway networks on MNIST, using two architectures, each with 9 convolutional layers followed by a softmax output. The number of filter maps (width) was set to 16 and 32 for all the layers. We obtained test set performance competitive with state-of-the-art methods with much fewer parameters, as show in Table 1.

**Table 1: Test set classification accuracy for pilot experiments on the MNIST dataset.**

| Network | No. of parameters | Test Accuracy (in %) |
|---------|------------------|----------------------|
| Highway Networks 10-layer (width 16) | 39K | 99.43 (99.4±0.03) |
| Highway Networks 10-layer (width 32) | 151K | 99.55 (99.54±0.02) |
| Maxout [20] | 420K | 99.55 |
| DSN [24] | 350K | 99.61 |

### 3.3 Experiments on CIFAR-10 and CIFAR-100 Object Recognition

#### 3.3.1 Comparison to Fitnets

Fitnet training Maxout networks can cope much better with increased depth than those with traditional activation functions [20]. However, Romero et. al. [25] recently reported that training on CIFAR-10 through plain backpropagation was only possible for maxout networks with a depth up to 5 layers when the number of parameters was limited to ∼250K and the number of multiplications to ∼30M. Similar limitations were observed for higher computational budgets. Training of deeper networks was only possible through the use of a two-stage training procedure and addition of soft targets produced from a pre-trained shallow teacher network (hint-based training).

We found that it was easy to train highway networks with numbers of parameters and operations comparable to those of fitnets in a single stage using SGD. As shown in Table 2, Highway A and Highway B, which are based on the architectures of Fitnet A and Fitnet B, respectively, obtain similar or higher accuracy on the test set. We were also able to train thinner and deeper networks: for example a 32-layer highway network consisting of alternating receptive fields of size 3x3 and 1x1 with ∼1.25M parameters performs better than the earlier teacher network [20].

**Table 2: CIFAR-10 test set accuracy of convolutional highway networks. Architectures tested were based on fitnets trained by Romero et. al. [25] using two-stage hint based training. Highway networks were trained in a single stage without hints, matching or exceeding the performance of fitnets.**

| Network | No. of Layers | No. of Parameters | Accuracy (in %) |
|---------|--------------|-------------------|-----------------|
| Fitnet Results (reported by Romero et. al.[25]): | | | |
| Teacher | 5 | ∼9M | 90.18 |
| Fitnet A | 11 | ∼250K | 89.01 |
| Fitnet B | 19 | ∼2.5M | 91.61 |
| Highway networks: | | | |
| Highway A (Fitnet A) | 11 | ∼236K | 89.18 |
| Highway B (Fitnet B) | 19 | ∼2.3M | 92.46 (92.28±0.16) |
| Highway C | 32 | ∼1.25M | 91.20 |

#### 3.3.2 Comparison to State-of-the-art Methods

It is possible to obtain high performance on the CIFAR-10 and CIFAR-100 datasets by utilizing very large networks and extensive data augmentation. This approach was popularized by Ciresan et. al. [5] and recently extended by Graham [34]. Since our aim is only to demonstrate that deeper networks can be trained without sacrificing ease of training or generalization ability, we only performed experiments in the more common setting of global contrast normalization, small translations and mirroring of images. Following Lin et. al. [35], we replaced the fully connected layer used in the networks in the previous section with a convolutional layer with a receptive field of size one and a global average pooling layer. The hyperparameters from the last section were re-used for both CIFAR-10 and CIFAR-100, therefore it is quite possible to obtain much better results with better architectures/hyperparameters. The results are tabulated in Table 3.

**Table 3: Test set accuracy of convolutional highway networks on the CIFAR-10 and CIFAR-100 object recognition datasets with typical data augmentation. For comparison, we list the accuracy reported by recent studies in similar experimental settings.**

| Network | CIFAR-10 Accuracy (in %) | CIFAR-100 Accuracy (in %) |
|---------|-------------------------|---------------------------|
| Maxout [20] | 90.62 | 61.42 |
| dasNet [36] | 90.78 | 66.22 |
| NiN [35] | 91.19 | 64.32 |
| DSN [24] | 92.03 | 65.43 |
| All-CNN [37] | 92.75 | 66.29 |
| Highway Network | 92.40 (92.31±0.12) | 67.76 (67.61±0.15) |

---

### النسخة العربية

تم تدريب جميع الشبكات باستخدام الانحدار التدرجي العشوائي (SGD) مع الزخم. تم استخدام معدل تعلم متناقص أسياً في القسم 3.1. بالنسبة لبقية التجارب، تم استخدام استراتيجية بسيطة شائعة الاستخدام حيث يبدأ معدل التعلم بقيمة λ ويتناقص وفقاً لجدول ثابت بعامل γ. تم اختيار λ و γ والجدول الزمني مرة واحدة بناءً على أداء مجموعة التحقق على مجموعة بيانات CIFAR-10، وتم الحفاظ عليها ثابتة لجميع التجارب. تستخدم جميع شبكات الطرق السريعة الالتفافية دالة التنشيط الخطية المقومة [16] لحساب حالة الكتلة H. لتقديم تقدير أفضل لتباين نتائج التصنيف بسبب التهيئة العشوائية، نبلغ عن نتائجنا بصيغة الأفضل (المتوسط ± الانحراف المعياري) بناءً على 5 تشغيلات حيثما كان ذلك متاحاً. تم إجراء التجارب باستخدام أطر عمل Caffe [33] و Brainstorm (https://github.com/IDSIA/brainstorm). الشفرة المصدرية ونتائج البحث عن المعاملات الفائقة والنصوص البرمجية ذات الصلة متاحة للعموم على http://people.idsia.ch/˜rupesh/very_deep_learning/.

### 3.1 التحسين

لدعم الفرضية القائلة بأن شبكات الطرق السريعة لا تعاني من زيادة العمق، أجرينا سلسلة من تجارب التحسين الصارمة، مقارنة إياها بالشبكات العادية ذات التهيئة الطبيعية [16، 17].

درّبنا كلاً من الشبكات العادية وشبكات الطرق السريعة بأعماق متفاوتة على مجموعة بيانات تصنيف أرقام MNIST. جميع الشبكات رفيعة: كل طبقة تحتوي على 50 كتلة لشبكات الطرق السريعة و71 وحدة للشبكات العادية، مما ينتج أعداداً متطابقة تقريباً من المعاملات (≈5000) لكل طبقة. في جميع الشبكات، الطبقة الأولى هي طبقة عادية متصلة بالكامل متبوعة بـ 9 أو 19 أو 49 أو 99 طبقة عادية أو طرق سريعة متصلة بالكامل. أخيراً، يتم إنتاج مخرجات الشبكة بواسطة طبقة softmax. قمنا بإجراء بحث عشوائي لـ 100 تشغيل لكل من الشبكات العادية وشبكات الطرق السريعة للعثور على إعدادات جيدة للمعاملات الفائقة التالية: معدل التعلم الأولي، والزخم، وعامل التناقص الأسي لمعدل التعلم، ودالة التنشيط (إما خطية مقومة أو tanh). بالنسبة لشبكات الطرق السريعة، كان هناك معامل فائق إضافي وهو القيمة الأولية لانحياز بوابة التحويل (بين -1 و -10). تم تهيئة الأوزان الأخرى باستخدام نفس التهيئة الطبيعية المستخدمة في الشبكات العادية.

يتم عرض منحنيات التدريب للشبكات الأفضل أداءً لكل عمق في الشكل 1. كما كان متوقعاً، تُظهر الشبكات العادية ذات 10 و20 طبقة أداءً جيداً جداً (متوسط الخسارة < 1e−4)، والذي يتدهور بشكل كبير مع زيادة العمق، على الرغم من زيادة سعة الشبكة. لا تعاني شبكات الطرق السريعة من زيادة العمق، وتؤدي شبكات الطرق السريعة ذات 50/100 طبقة أداءً مماثلاً لشبكات 10/20 طبقة. أدت شبكة الطريق السريع ذات 100 طبقة أداءً أفضل بأكثر من رتبتين من حيث الحجم مقارنة بشبكة عادية بحجم مماثل. لوحظ أيضاً أن شبكات الطرق السريعة تقاربت باستمرار بشكل أسرع بكثير من الشبكات العادية.

### 3.2 تجارب تجريبية على تصنيف أرقام MNIST

كفحص للتأكد من قدرة التعميم لشبكات الطرق السريعة، درّبنا شبكات طرق سريعة التفافية من 10 طبقات على MNIST، باستخدام معماريتين، كل منهما بـ 9 طبقات التفافية متبوعة بمخرج softmax. تم تعيين عدد خرائط المرشحات (العرض) إلى 16 و32 لجميع الطبقات. حصلنا على أداء مجموعة اختبار تنافسي مع الأساليب الحديثة بمعاملات أقل بكثير، كما هو موضح في الجدول 1.

**الجدول 1: دقة التصنيف على مجموعة الاختبار للتجارب التجريبية على مجموعة بيانات MNIST.**

| الشبكة | عدد المعاملات | دقة الاختبار (بالنسبة المئوية) |
|---------|------------------|----------------------|
| شبكات الطرق السريعة 10 طبقات (عرض 16) | 39K | 99.43 (99.4±0.03) |
| شبكات الطرق السريعة 10 طبقات (عرض 32) | 151K | 99.55 (99.54±0.02) |
| Maxout [20] | 420K | 99.55 |
| DSN [24] | 350K | 99.61 |

### 3.3 تجارب على التعرف على الكائنات CIFAR-10 و CIFAR-100

#### 3.3.1 المقارنة مع Fitnets

تدريب Fitnet يمكن لشبكات Maxout التعامل بشكل أفضل بكثير مع زيادة العمق مقارنة بتلك ذات دوال التنشيط التقليدية [20]. ومع ذلك، أفاد Romero وآخرون [25] مؤخراً أن التدريب على CIFAR-10 من خلال الانتشار العكسي العادي كان ممكناً فقط لشبكات maxout بعمق يصل إلى 5 طبقات عندما كان عدد المعاملات محدوداً بـ ∼250K وعدد عمليات الضرب بـ ∼30M. لوحظت قيود مماثلة لميزانيات حسابية أعلى. كان تدريب الشبكات الأعمق ممكناً فقط من خلال استخدام إجراء تدريب من مرحلتين وإضافة أهداف ناعمة منتجة من شبكة معلم ضحلة مُدربة مسبقاً (التدريب القائم على التلميحات).

وجدنا أنه من السهل تدريب شبكات الطرق السريعة بأعداد معاملات وعمليات مماثلة لتلك الخاصة بـ fitnets في مرحلة واحدة باستخدام SGD. كما هو موضح في الجدول 2، تحصل Highway A و Highway B، المبنية على معماريات Fitnet A و Fitnet B على التوالي، على دقة مماثلة أو أعلى على مجموعة الاختبار. تمكنا أيضاً من تدريب شبكات أرفع وأعمق: على سبيل المثال، شبكة طريق سريع من 32 طبقة تتكون من حقول استقبالية متناوبة بحجم 3x3 و 1x1 مع ∼1.25M معامل تؤدي أداءً أفضل من شبكة المعلم السابقة [20].

**الجدول 2: دقة مجموعة اختبار CIFAR-10 لشبكات الطرق السريعة الالتفافية. تم اختبار المعماريات بناءً على fitnets المدربة بواسطة Romero وآخرون [25] باستخدام التدريب القائم على التلميحات من مرحلتين. تم تدريب شبكات الطرق السريعة في مرحلة واحدة بدون تلميحات، مطابقة أو تجاوز أداء fitnets.**

| الشبكة | عدد الطبقات | عدد المعاملات | الدقة (بالنسبة المئوية) |
|---------|--------------|-------------------|-----------------|
| نتائج Fitnet (كما أبلغ عنها Romero وآخرون [25]): | | | |
| المعلم | 5 | ∼9M | 90.18 |
| Fitnet A | 11 | ∼250K | 89.01 |
| Fitnet B | 19 | ∼2.5M | 91.61 |
| شبكات الطرق السريعة: | | | |
| Highway A (Fitnet A) | 11 | ∼236K | 89.18 |
| Highway B (Fitnet B) | 19 | ∼2.3M | 92.46 (92.28±0.16) |
| Highway C | 32 | ∼1.25M | 91.20 |

#### 3.3.2 المقارنة مع الأساليب الحديثة

من الممكن الحصول على أداء عالٍ على مجموعتي بيانات CIFAR-10 و CIFAR-100 باستخدام شبكات كبيرة جداً وزيادة بيانات واسعة النطاق. تم نشر هذا النهج بواسطة Ciresan وآخرين [5] وتم توسيعه مؤخراً بواسطة Graham [34]. بما أن هدفنا هو فقط إثبات أنه يمكن تدريب الشبكات الأعمق دون التضحية بسهولة التدريب أو قدرة التعميم، فقد أجرينا تجارب فقط في الإعداد الأكثر شيوعاً للتطبيع العالمي للتباين، والترجمات الصغيرة، والانعكاس للصور. بعد Lin وآخرين [35]، استبدلنا الطبقة المتصلة بالكامل المستخدمة في الشبكات في القسم السابق بطبقة التفافية بحقل استقبالي بحجم واحد وطبقة تجميع متوسط عالمية. تم إعادة استخدام المعاملات الفائقة من القسم الأخير لكل من CIFAR-10 و CIFAR-100، وبالتالي من الممكن تماماً الحصول على نتائج أفضل بكثير باستخدام معماريات/معاملات فائقة أفضل. النتائج موضحة في الجدول 3.

**الجدول 3: دقة مجموعة الاختبار لشبكات الطرق السريعة الالتفافية على مجموعتي بيانات التعرف على الكائنات CIFAR-10 و CIFAR-100 مع زيادة البيانات النموذجية. للمقارنة، نسرد الدقة المبلغ عنها من قبل الدراسات الحديثة في إعدادات تجريبية مماثلة.**

| الشبكة | دقة CIFAR-10 (بالنسبة المئوية) | دقة CIFAR-100 (بالنسبة المئوية) |
|---------|-------------------------|---------------------------|
| Maxout [20] | 90.62 | 61.42 |
| dasNet [36] | 90.78 | 66.22 |
| NiN [35] | 91.19 | 64.32 |
| DSN [24] | 92.03 | 65.43 |
| All-CNN [37] | 92.75 | 66.29 |
| شبكة الطريق السريع | 92.40 (92.31±0.12) | 67.76 (67.61±0.15) |

---

### Translation Notes

- **Figures referenced:** Figure 1 (training curves for plain vs highway networks)
- **Tables:** 3 tables with experimental results translated
- **Key terms introduced:**
  - momentum → الزخم
  - exponentially decaying → متناقص أسياً
  - learning rate → معدل التعلم
  - validation set → مجموعة التحقق
  - rectified linear activation → التنشيط الخطي المقوم
  - random initialization → التهيئة العشوائية
  - standard deviation → الانحراف المعياري
  - softmax layer → طبقة softmax
  - test set → مجموعة الاختبار
  - data augmentation → زيادة البيانات
  - global average pooling → تجميع متوسط عالمي
  - contrast normalization → التطبيع للتباين
  - filter maps → خرائط المرشحات
  - backpropagation → الانتشار العكسي
- **Equations:** None in this section
- **Citations:** Multiple references [5, 16, 17, 20, 24, 25, 33-37]
- **Special handling:**
  - Preserved all numerical results and statistical notations
  - Translated table headers and content
  - Maintained citation numbers
  - Kept technical acronyms (MNIST, CIFAR-10, CIFAR-100, SGD)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
