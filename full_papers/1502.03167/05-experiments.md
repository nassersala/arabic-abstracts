# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** ImageNet, MNIST, training, validation, accuracy, convergence, mini-batch, learning rate, ensemble

---

### English Version

### 5.1 Activations over time

To verify the effects of internal covariate shift on training, and the ability of Batch Normalization to combat it, we considered the problem of predicting the digit class on the MNIST dataset (LeCun et al., 1998a). We used a very simple network, with a 28x28 binary image as input, and 3 fully-connected hidden layers with 100 activations each. Each hidden layer computes $y = g(Wu+b)$ with sigmoid nonlinearity, and the weights $W$ are initialized to small random Gaussian values. The last hidden layer is followed by a fully-connected layer with 10 activations (one per class) and cross-entropy loss. We trained the network for 50000 steps, with 60 examples per mini-batch. We added Batch Normalization to each hidden layer of the network, as in Algorithm 1. We were interested in the comparison between the baseline and batch-normalized networks, rather than achieving the state of the art performance on MNIST (which the described architecture does not).

Figure 1 (a) shows the fraction of correct predictions by the two networks on held-out test data, as training progresses. The batch-normalized network enjoys the higher test accuracy. Figure 1 (b) shows, for the last hidden layer of the baseline network and the batch-normalized network, how the distribution of the inputs to the sigmoid in the last hidden layer evolves. As training progresses, the distribution for the baseline network shifts significantly, which makes training slow and difficult. By contrast, the distribution for the batch-normalized network remains much more stable, enabling faster training.

### 5.2 ImageNet classification

We applied Batch Normalization to a new variant of the Inception network (Szegedy et al., 2014), trained on the ImageNet classification task (Russakovsky et al., 2014). The network has a large number of convolutional and pooling layers, with a softmax layer to predict the image class, out of 1000 possibilities. Convolutional layers use ReLU as the nonlinearity. The main difference to the network described in (Szegedy et al., 2014) is that the 5x5 convolutional layers are replaced by two consecutive layers of 3x3 convolutions with up to 128 filters. The network contains 13.6·10^6 parameters, and, other than the top softmax layer, has no fully-connected layers. More details are given in the Appendix.

We evaluate the trained networks on the validation data set using the standard metric of top-5 error rate. Top-5 error rate is the fraction of test images for which the correct label is not among the top 5 labels considered most probable by the model.

The leading approach for ImageNet classification is Ensemble learning. In the remainder of this section, we describe the results for single network classification.

#### 5.2.1 Accelerating BN Networks

Simply adding Batch Normalization to a network does not take full advantage of our method. To do so, we further changed the network and its training parameters, as follows:

**Increase learning rate.** In a batch-normalized model, we have been able to achieve a training speedup from higher learning rates, with no ill side effects.

**Remove Dropout.** As described in Section 4.2, Batch Normalization fulfills some of the same goals as Dropout. Removing Dropout from the modified Batch Normalization Inception speeds up training, without increasing overfitting.

**Reduce the L2 weight regularization.** While in the original Inception L2 weight cost is used, we have found that this can be reduced by a factor of 5. This is because Batch Normalization already provides much of the necessary regularization.

**Accelerate the learning rate decay.** In training Inception, the learning rate was decayed exponentially. Because our network trains faster than the Inception, we lower the learning rate 6 times faster.

**Remove Local Response Normalization.** While Inception and other networks (Srivastava et al., 2014) benefit from it, we found that with Batch Normalization it is not necessary.

**Shuffle training examples more thoroughly.** We enabled within-shard shuffling of the training data, which prevents the same examples from always appearing in a mini-batch together. This led to about 1% improvements in the validation accuracy, which is consistent with the view of Batch Normalization as a regularizer (Section 4.2): the randomization inherent in our method should be most beneficial when it affects an example differently each time it is seen.

**Reduce the photometric distortions.** Because batch-normalized networks train faster and observe each training example fewer times, we let the trainer focus on more "real" images by distorting them less.

#### 5.2.2 Single-Network Classification

We evaluated the following networks, all trained on the ILSVRC2012 training data, and tested on the validation data:

**Inception:** the network described at the beginning of Section 5.2, trained with the initial learning rate of 0.0015.

**BN-Baseline:** Same as Inception with Batch Normalization before each nonlinearity.

**BN-x5:** Inception with Batch Normalization and the modifications in Section 5.2.1. The initial learning rate was increased by a factor of 5, to 0.0075. The same learning rate increase with the original Inception caused the model parameters to reach machine infinity.

**BN-x30:** Like BN-x5, but with the initial learning rate 0.045 (30 times that of Inception).

**BN-x5-Sigmoid:** Like BN-x5, but with sigmoid nonlinearity $g(t) = \frac{1}{1+\exp(-x)}$ instead of ReLU. We also attempted to train the original Inception with sigmoid, but the model remained at the accuracy equivalent to chance.

In Figure 2, we show the validation accuracy of the networks, as a function of the number of training steps. Inception reached the accuracy of 72.2% after 31·10^6 training steps. The Figure 3 shows, for each network, the number of training steps required to reach the same 72.2% accuracy, as well as the maximum validation accuracy reached by the network and the number of steps to reach it.

By adding Batch Normalization to Inception (BN-Baseline), we significantly accelerate training. The network BN-x5 is faster than Inception by a factor of more than 5, reaching 72.2% in less than half the number of training steps. Interestingly, increasing the learning rate further (BN-x30) causes the model to train somewhat slower initially, but allows it to reach a higher final accuracy. This network reaches 74.8% after 6·10^6 steps, i.e. 5 times faster than Inception, and 1% better in terms of the final accuracy.

#### 5.2.3 Ensemble Classification

The current reported best results on the ImageNet Large Scale Visual Recognition Competition are reached by the Deep Image ensemble of traditional models (Russakovsky et al., 2014) and the ensemble model of (Szegedy et al., 2014), both of which reported top-5 error rate of 4.94%. Here we report a competitive result using an ensemble of 6 networks. Each network was based on BN-x30, modified via some of the following: increased initial weights in the convolutional layers; using Dropout (with the Dropout probability of 5% or 10%, vs. 40% for the original Inception); and using non-convolutional, per-activation Batch Normalization with last hidden layers of the model. Each network achieved its maximum accuracy after about 6·10^6 training steps. The ensemble prediction was based on the arithmetic average of class probabilities predicted by the constituent networks. The details of ensemble and multi-crop inference are similar to (Szegedy et al., 2014).

We evaluate our ensemble on the test set released for the ILSVRC-2012 competition. The best published result for this dataset is 4.94% top-5 error, for an ensemble of traditional networks. Our ensemble of BN networks achieves 4.82% top-5 error, which improves upon the best published result and is competitive with the winning entry of ILSVRC 2014 (4.8%).

---

### النسخة العربية

### 5.1 التنشيطات عبر الزمن

للتحقق من تأثيرات التحول التبايني الداخلي على التدريب، وقدرة تطبيع الحزمة على مكافحته، اعتبرنا مشكلة التنبؤ بفئة الرقم على مجموعة بيانات MNIST (LeCun et al., 1998a). استخدمنا شبكة بسيطة جداً، مع صورة ثنائية 28x28 كمدخل، و3 طبقات مخفية متصلة بالكامل مع 100 تنشيط لكل منها. تحسب كل طبقة مخفية $y = g(Wu+b)$ مع لاخطية sigmoid، ويتم تهيئة الأوزان $W$ إلى قيم غاوسية عشوائية صغيرة. تُتبع الطبقة المخفية الأخيرة بطبقة متصلة بالكامل مع 10 تنشيطات (واحد لكل فئة) ودالة خسارة التشابك المتقاطع (Cross-entropy). درّبنا الشبكة لـ 50000 خطوة، مع 60 مثالاً لكل حزمة صغيرة. أضفنا تطبيع الحزمة إلى كل طبقة مخفية في الشبكة، كما في الخوارزمية 1. كنا مهتمين بالمقارنة بين الشبكة الأساسية والشبكة المطبعة بالحزمة، بدلاً من تحقيق أداء متقدم على MNIST (وهو ما لا تفعله المعمارية الموصوفة).

يُظهر الشكل 1 (أ) نسبة التنبؤات الصحيحة بواسطة الشبكتين على بيانات الاختبار المحجوزة، مع تقدم التدريب. تتمتع الشبكة المطبعة بالحزمة بدقة اختبار أعلى. يُظهر الشكل 1 (ب)، للطبقة المخفية الأخيرة من الشبكة الأساسية والشبكة المطبعة بالحزمة، كيف يتطور توزيع المدخلات إلى sigmoid في الطبقة المخفية الأخيرة. مع تقدم التدريب، يتحول التوزيع للشبكة الأساسية بشكل كبير، مما يجعل التدريب بطيئاً وصعباً. في المقابل، يبقى التوزيع للشبكة المطبعة بالحزمة أكثر استقراراً بكثير، مما يمكّن من تدريب أسرع.

### 5.2 تصنيف ImageNet

طبقنا تطبيع الحزمة على متغير جديد من شبكة Inception (Szegedy et al., 2014)، مدرب على مهمة تصنيف ImageNet (Russakovsky et al., 2014). تحتوي الشبكة على عدد كبير من الطبقات الالتفافية وطبقات التجميع (Pooling)، مع طبقة softmax للتنبؤ بفئة الصورة، من بين 1000 احتمال. تستخدم الطبقات الالتفافية ReLU كلاخطية. الفرق الرئيسي عن الشبكة الموصوفة في (Szegedy et al., 2014) هو أن الطبقات الالتفافية 5x5 تم استبدالها بطبقتين متتاليتين من الالتفافات 3x3 مع ما يصل إلى 128 مرشحاً. تحتوي الشبكة على 13.6·10^6 معامل، وبخلاف طبقة softmax العلوية، لا تحتوي على طبقات متصلة بالكامل. مزيد من التفاصيل موجودة في الملحق.

نقيّم الشبكات المدربة على مجموعة بيانات التحقق باستخدام المقياس القياسي لمعدل خطأ أفضل 5 (Top-5 Error Rate). معدل خطأ أفضل 5 هو نسبة صور الاختبار التي لا تكون التسمية الصحيحة فيها من بين أفضل 5 تسميات تعتبرها النموذج الأكثر احتمالاً.

النهج الرائد لتصنيف ImageNet هو التعلم الجماعي (Ensemble Learning). في بقية هذا القسم، نصف النتائج لتصنيف الشبكة الواحدة.

#### 5.2.1 تسريع شبكات BN

مجرد إضافة تطبيع الحزمة إلى شبكة لا يستفيد بالكامل من طريقتنا. للقيام بذلك، قمنا بتغيير الشبكة ومعاملات تدريبها بشكل أكبر، على النحو التالي:

**زيادة معدل التعلم.** في نموذج مطبع بالحزمة، تمكنا من تحقيق تسريع في التدريب من معدلات تعلم أعلى، بدون أي آثار جانبية سيئة.

**إزالة Dropout.** كما هو موضح في القسم 4.2، يحقق تطبيع الحزمة بعض الأهداف نفسها مثل Dropout. إزالة Dropout من Inception المعدل بتطبيع الحزمة يسرّع التدريب، دون زيادة الإفراط في التعميم.

**تقليل تنظيم الأوزان L2.** بينما يُستخدم تكلفة أوزان L2 في Inception الأصلي، وجدنا أنه يمكن تقليل ذلك بمعامل 5. هذا لأن تطبيع الحزمة يوفر بالفعل الكثير من التنظيم الضروري.

**تسريع تناقص معدل التعلم.** في تدريب Inception، تناقص معدل التعلم بشكل أسي. نظراً لأن شبكتنا تتدرب أسرع من Inception، نخفض معدل التعلم 6 مرات أسرع.

**إزالة تطبيع الاستجابة المحلية (Local Response Normalization).** بينما تستفيد Inception والشبكات الأخرى (Srivastava et al., 2014) منه، وجدنا أنه مع تطبيع الحزمة ليس ضرورياً.

**خلط أمثلة التدريب بشكل أكثر شمولاً.** مكّنا خلط بيانات التدريب داخل الشريحة، مما يمنع ظهور نفس الأمثلة دائماً في حزمة صغيرة معاً. أدى هذا إلى تحسينات بنسبة 1٪ تقريباً في دقة التحقق، وهو ما يتفق مع وجهة نظر تطبيع الحزمة كمنظم (القسم 4.2): يجب أن يكون العشوائية الكامنة في طريقتنا أكثر فائدة عندما تؤثر على مثال بشكل مختلف في كل مرة يُرى فيها.

**تقليل التشوهات الضوئية.** نظراً لأن الشبكات المطبعة بالحزمة تتدرب بشكل أسرع وتراقب كل مثال تدريب عدداً أقل من المرات، سمحنا للمدرب بالتركيز على صور "حقيقية" أكثر من خلال تشويهها بشكل أقل.

#### 5.2.2 تصنيف الشبكة الواحدة

قيّمنا الشبكات التالية، جميعها مدربة على بيانات تدريب ILSVRC2012، واختبرت على بيانات التحقق:

**Inception:** الشبكة الموصوفة في بداية القسم 5.2، مدربة بمعدل تعلم أولي 0.0015.

**BN-Baseline:** نفس Inception مع تطبيع الحزمة قبل كل لاخطية.

**BN-x5:** Inception مع تطبيع الحزمة والتعديلات في القسم 5.2.1. تم زيادة معدل التعلم الأولي بمعامل 5، إلى 0.0075. نفس زيادة معدل التعلم مع Inception الأصلي تسببت في وصول معاملات النموذج إلى اللانهاية الآلية.

**BN-x30:** مثل BN-x5، لكن مع معدل تعلم أولي 0.045 (30 ضعف معدل Inception).

**BN-x5-Sigmoid:** مثل BN-x5، لكن مع لاخطية sigmoid $g(t) = \frac{1}{1+\exp(-x)}$ بدلاً من ReLU. حاولنا أيضاً تدريب Inception الأصلي مع sigmoid، لكن النموذج بقي عند دقة تعادل الصدفة.

في الشكل 2، نُظهر دقة التحقق للشبكات، كدالة لعدد خطوات التدريب. وصل Inception إلى دقة 72.2٪ بعد 31·10^6 خطوة تدريب. يُظهر الشكل 3، لكل شبكة، عدد خطوات التدريب المطلوبة للوصول إلى نفس دقة 72.2٪، بالإضافة إلى أقصى دقة تحقق وصلت إليها الشبكة وعدد الخطوات للوصول إليها.

من خلال إضافة تطبيع الحزمة إلى Inception (BN-Baseline)، نسرّع التدريب بشكل كبير. الشبكة BN-x5 أسرع من Inception بمعامل أكثر من 5، وتصل إلى 72.2٪ في أقل من نصف عدد خطوات التدريب. من المثير للاهتمام، أن زيادة معدل التعلم بشكل أكبر (BN-x30) تتسبب في تدريب النموذج بشكل أبطأ قليلاً في البداية، لكنها تسمح له بالوصول إلى دقة نهائية أعلى. تصل هذه الشبكة إلى 74.8٪ بعد 6·10^6 خطوة، أي 5 مرات أسرع من Inception، وأفضل بنسبة 1٪ من حيث الدقة النهائية.

#### 5.2.3 التصنيف الجماعي

أفضل النتائج المُبلغ عنها حالياً في مسابقة ImageNet للتعرف البصري واسع النطاق يتم الوصول إليها بواسطة مجموعة Deep Image من النماذج التقليدية (Russakovsky et al., 2014) ونموذج المجموعة من (Szegedy et al., 2014)، وكلاهما أبلغ عن معدل خطأ أفضل 5 بنسبة 4.94٪. هنا نبلغ عن نتيجة تنافسية باستخدام مجموعة من 6 شبكات. كانت كل شبكة تستند إلى BN-x30، معدلة عبر بعض مما يلي: زيادة الأوزان الأولية في الطبقات الالتفافية؛ استخدام Dropout (مع احتمالية Dropout 5٪ أو 10٪، مقابل 40٪ لـ Inception الأصلي)؛ واستخدام تطبيع الحزمة غير الالتفافي، لكل تنشيط مع الطبقات المخفية الأخيرة من النموذج. حققت كل شبكة أقصى دقة لها بعد حوالي 6·10^6 خطوة تدريب. استند التنبؤ الجماعي إلى المتوسط الحسابي لاحتمالات الفئة المتنبأ بها بواسطة الشبكات المكونة. تفاصيل المجموعة والاستدلال متعدد المحاصيل (Multi-crop) مماثلة لـ (Szegedy et al., 2014).

نقيّم مجموعتنا على مجموعة الاختبار المُصدرة لمسابقة ILSVRC-2012. أفضل نتيجة منشورة لمجموعة البيانات هذه هي 4.94٪ خطأ أفضل 5، لمجموعة من الشبكات التقليدية. تحقق مجموعة شبكات BN لدينا 4.82٪ خطأ أفضل 5، مما يحسّن أفضل نتيجة منشورة وتنافسي مع الدخول الفائز في ILSVRC 2014 (4.8٪).

---

### Translation Notes

- **Figures referenced:** Figure 1 (a), Figure 1 (b), Figure 2, Figure 3
- **Key terms introduced:**
  - Top-5 error rate (معدل خطأ أفضل 5)
  - Ensemble learning (التعلم الجماعي)
  - Cross-entropy loss (دالة خسارة التشابك المتقاطع)
  - Softmax layer (طبقة softmax)
  - Pooling layers (طبقات التجميع)
  - Multi-crop inference (الاستدلال متعدد المحاصيل)
  - Photometric distortions (التشوهات الضوئية)
  - Within-shard shuffling (الخلط داخل الشريحة)
- **Equations:** 1 equation (sigmoid function)
- **Citations:** LeCun et al., 1998a; Szegedy et al., 2014; Russakovsky et al., 2014; Srivastava et al., 2014
- **Tables/Results:** Multiple experimental results and comparisons
- **Special handling:** Experimental setup and results described with precision; numerical results preserved exactly

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
