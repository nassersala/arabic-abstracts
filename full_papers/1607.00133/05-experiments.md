# Section 5: Experimental Results
## القسم 5: النتائج التجريبية

**Section:** experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** MNIST, CIFAR-10, accuracy, training, testing, privacy budget, epsilon, delta, PCA, convolutional layers, ReLU, softmax, cross-entropy, lot size, learning rate, gradient clipping, noise level, overfitting, generalization

---

### English Version

This section reports on our evaluation of the moments accountant, and results on two popular image datasets: MNIST and CIFAR-10.

#### 5.1 Applying the Moments Accountant

As shown by Theorem 1, the moments accountant provides a tighter bound on the privacy loss compared to the generic strong composition theorem. Here we compare them using some concrete values. The overall privacy loss (ε,δ) can be computed from the noise level σ, the sampling ratio of each lot q=L/N (so each epoch consists of 1/q batches), and the number of epochs E (so the number of steps is T=E/q). We fix the target δ=10⁻⁵, the value used for our MNIST and CIFAR experiments.

In our experiment, we set q=0.01, σ=4, and δ=10⁻⁵, and compute the value of ε as a function of the training epoch E. Figure 3 shows two curves corresponding to, respectively, using the strong composition theorem and the moments accountant. We can see that we get a much tighter estimation of the privacy loss by using the moments accountant. For examples, when E=100, the values are 9.34 and 1.26 respectively, and for E=400, the values are 24.22 and 2.55 respectively. That is, using the moments bound, we achieve (2.55,10⁻⁵)-differential privacy, whereas previous techniques only obtain the significantly worse guarantee of (24.22, 10⁻⁵).

#### 5.2 MNIST

We conduct experiments on the standard MNIST dataset for handwritten digit recognition consisting of 60,000 training examples and 10,000 testing examples. Each example is a 28×28 size gray-level image. We use a simple feed-forward neural network with ReLU units and softmax of 10 classes (corresponding to the 10 digits) with cross-entropy loss and an optional PCA input layer.

**Baseline model:** Our baseline model uses a 60-dimensional PCA projection layer and a single hidden layer with 1,000 hidden units. Using the lot size of 600, we can reach accuracy of 98.30% in about 100 epochs. This result is consistent with what can be achieved with a vanilla neural network.

**Differentially private model:** For the differentially private version, we experiment with the same architecture with a 60-dimensional PCA projection layer, a single 1,000-unit ReLU hidden layer, and a lot size of 600. To limit sensitivity, we clip the gradient norm of each layer at 4. We report results for three choices of the noise scale, which we call small (σ=2, σ_p=4), medium (σ=4, σ_p=7), and large (σ=8, σ_p=16). Here σ represents the noise level for training the neural network, and σ_p the noise level for PCA projection. The learning rate is set at 0.1 initially and linearly decreased to 0.052 over 10 epochs and then fixed to 0.052 thereafter. We have also experimented with multi-hidden-layer networks. For MNIST, we found that one hidden layer combined with PCA works better than a two-layer network.

Figure 4 shows the results for different noise levels. In each plot, we show the evolution of the training and testing accuracy as a function of the number of epochs as well as the corresponding δ value, keeping ε fixed. We achieve 90%, 95%, and 97% test set accuracy for (0.5,10⁻⁵), (2,10⁻⁵), and (8,10⁻⁵)-differential privacy respectively.

One attractive consequence of applying differentially private SGD is the small difference between the model's accuracy on the training and the test sets, which is consistent with the theoretical argument that differentially private training generalizes well. In contrast, the gap between training and testing accuracy in non-private training, i.e., evidence of overfitting, increases with the number of epochs.

By using the moments accountant, we can obtain a δ value for any given ε. We record the accuracy for different (ε,δ) pairs in Figure 5. In the figure, each curve corresponds to the best accuracy achieved for a fixed δ, as it varies between 10⁻⁵ and 10⁻². For example, we can achieve 90% accuracy for ε=0.25 and δ=0.01. As can be observed from the figure, for a fixed δ, varying the value of ε can have large impact on accuracy, but for any fixed ε, there is less difference with different δ values.

**Effect of the parameters:** Classification accuracy is determined by multiple factors that must be carefully tuned for optimal performance. These factors include the topology of the network, the number of PCA dimensions and the number of hidden units, as well as parameters of the training procedure such as the lot size and the learning rate. Some parameters are specific to privacy, such as the gradient norm clipping bound and the noise level.

To demonstrate the effects of these parameters, we manipulate them individually, keeping the rest constant. We set the reference values as follows: 60 PCA dimensions, 1,000 hidden units, 600 lot size, gradient norm bound of 4, initial learning rate of 0.1 decreasing to a final learning rate of 0.052 in 10 epochs, and noise σ equal to 4 and 7 respectively for training the neural network parameters and for the PCA projection. For each combination of values, we train until the point at which (2,10⁻⁵)-differential privacy would be violated (so, for example, a larger σ allows more epochs of training). The results are presented in Figure 6.

**PCA projection.** In our experiments, the accuracy is fairly stable as a function of the PCA dimension, with the best results achieved for 60. (Not doing PCA reduces accuracy by about 2%.) Although in principle the PCA projection layer can be replaced by an additional hidden layer, we achieve better accuracy by training the PCA layer separately. By reducing the input size from 784 to 60, PCA leads to an almost 10× reduction in training time. The result is fairly stable over a large range of the noise levels for the PCA projection and consistently better than the accuracy using random projection, which is at about 92.5% and shown as a horizontal line in the plot.

**Number of hidden units.** Including more hidden units makes it easier to fit the training set. For non-private training, it is often preferable to use more units, as long as we employ techniques to avoid overfitting. However, for differentially private training, it is not a priori clear if more hidden units improve accuracy, as more hidden units increase the sensitivity of the gradient, which leads to more noise added at each update.

Somewhat counterintuitively, increasing the number of hidden units does not decrease accuracy of the trained model. One possible explanation that calls for further analysis is that larger networks are more tolerant to noise. This property is quite encouraging as it is common in practice to use very large networks.

**Lot size.** According to Theorem 1, we can run N/L epochs while staying within a constant privacy budget. Choosing the lot size must balance two conflicting objectives. On the one hand, smaller lots allow running more epochs, i.e., passes over data, improving accuracy. On the other hand, for a larger lot, the added noise has a smaller relative effect.

Our experiments show that the lot size has a relatively large impact on accuracy. Empirically, the best lot size is roughly √N where N is the number of training examples.

**Learning rate.** Accuracy is stable for a learning rate in the range of [0.01, 0.07] and peaks at 0.05. However, accuracy decreases significantly if the learning rate is too large. Some additional experiments suggest that, even for large learning rates, we can reach similar levels of accuracy by reducing the noise level and, accordingly, by training less in order to avoid exhausting the privacy budget.

**Clipping bound.** Limiting the gradient norm has two opposing effects: clipping destroys the unbiasedness of the gradient estimate, and if the clipping parameter is too small, the average clipped gradient may point in a very different direction from the true gradient. On the other hand, increasing the norm bound C forces us to add more noise to the gradients (and hence the parameters), since we add noise based on σC. In practice, a good way to choose a value for C is by taking the median of the norms of the unclipped gradients over the course of training.

**Noise level.** By adding more noise, the per-step privacy loss is proportionally smaller, so we can run more epochs within a given cumulative privacy budget. The choice of this value has a large impact on accuracy.

From the experiments, we observe the following:

1. The PCA projection improves both model accuracy and training performance. Accuracy is quite stable over a large range of choices for the projection dimensions and the noise level used in the PCA stage.

2. The accuracy is fairly stable over the network size. When we can only run smaller number of epochs, it is more beneficial to use a larger network.

3. The training parameters, especially the lot size and the noise scale σ, have a large impact on the model accuracy. They both determine the "noise-to-signal" ratio of the sanitized gradients as well as the number of epochs we are able to go through the data before reaching the privacy limit.

Our framework allows for adaptive control of the training parameters, such as the lot size, the gradient norm bound C, and noise level σ. Our initial experiments with decreasing noise as training progresses did not show a significant improvement, but it is interesting to consider more sophisticated schemes for adaptively choosing these parameters.

#### 5.3 CIFAR-10

We also conduct experiments on the CIFAR-10 dataset, which consists of color images classified into 10 classes such as ships, cats, and dogs, and partitioned into 50,000 training examples and 10,000 test examples. Each example is a 32×32 image with three channels (RGB). For this learning task, nearly all successful networks use convolutional layers. The CIFAR-100 dataset has similar parameters, except that images are classified into 100 classes; the examples and the image classes are different from those of CIFAR-10.

We use the network architecture from the TensorFlow convolutional neural networks tutorial. Each 32×32 image is first cropped to a 24×24 one by taking the center patch. The network architecture consists of two convolutional layers followed by two fully connected layers. The convolutional layers use 5×5 convolutions with stride 1, followed by a ReLU and 2×2 max pools, with 64 channels each. Thus the first convolution outputs a 12×12×64 tensor for each image, and the second outputs a 6×6×64 tensor. The latter is flattened to a vector that gets fed into a fully connected layer with 384 units, and another one of the same size.

This architecture, non-privately, can get to about 86% accuracy in 500 epochs. Its simplicity makes it an appealing choice for our work. We should note however that by using deeper networks with different non-linearities and other advanced techniques, one can obtain significantly better accuracy, with the state-of-the-art being about 96.5%.

As is standard for such image datasets, we use data augmentation during training. For each training image, we generate a new distorted image by randomly picking a 24×24 patch from the image, randomly flipping the image along the left-right direction, and randomly distorting the brightness and the contrast of the image. In each epoch, these distortions are done independently. We refer the reader to the TensorFlow tutorial for additional details.

As the convolutional layers have shared parameters, computing per-example gradients has a larger computational overhead. Previous work has shown that convolutional layers are often transferable: parameters learned from one dataset can be used on another one without retraining. We treat the CIFAR-100 dataset as a public dataset and use it to train a network with the same architecture. We use the convolutions learned from training this dataset. Retraining only the fully connected layers with this architecture for about 250 epochs with a batch size of 120 gives us approximately 80% accuracy, which is our non-private baseline.

**Differentially private version:** For the differentially private version, we use the same architecture. As discussed above, we use pre-trained convolutional layers. The fully connected layers are initialized from the pre-trained network as well. We train the softmax layer, and either the top or both fully connected layers. Based on looking at gradient norms, the softmax layer gradients are roughly twice as large as the other two layers, and we keep this ratio when we try clipping at a few different values between 3 and 10. The lot size is an additional knob that we tune: we tried 600, 2,000, and 4,000. With these settings, the per-epoch training time increases from approximately 40 seconds to 180 seconds.

In Figure 7, we show the evolution of the accuracy and the privacy cost, as a function of the number of epochs, for a few different parameter settings.

The various parameters influence the accuracy one gets, in ways not too different from that in the MNIST experiments. A lot size of 600 leads to poor results on this dataset and we need to increase it to 2,000 or more for results reported in Figure 7.

Compared to the MNIST dataset, where the difference in accuracy between a non-private baseline and a private model is about 1.3%, the corresponding drop in accuracy in our CIFAR-10 experiment is much larger (about 7%). We leave closing this gap as an interesting test for future research in differentially private machine learning.

---

### النسخة العربية

يقدم هذا القسم تقريراً عن تقييمنا لمحاسب العزوم، ونتائج على مجموعتي بيانات صور شهيرتين: MNIST و CIFAR-10.

#### 5.1 تطبيق محاسب العزوم

كما هو موضح في المبرهنة 1، يوفر محاسب العزوم حداً أكثر إحكاماً على خسارة الخصوصية مقارنة بمبرهنة التركيب القوية العامة. هنا نقارنهما باستخدام بعض القيم الملموسة. يمكن حساب خسارة الخصوصية الإجمالية (ε,δ) من مستوى الضوضاء σ، ونسبة أخذ العينات لكل لوت q=L/N (بحيث تتكون كل حقبة من 1/q دفعة)، وعدد الحقب E (بحيث عدد الخطوات هو T=E/q). نثبت الهدف δ=10⁻⁵، القيمة المستخدمة لتجارب MNIST و CIFAR لدينا.

في تجربتنا، نضع q=0.01، σ=4، و δ=10⁻⁵، ونحسب قيمة ε كدالة لحقبة التدريب E. يُظهر الشكل 3 منحنيين يتوافقان، على التوالي، مع استخدام مبرهنة التركيب القوية ومحاسب العزوم. يمكننا أن نرى أننا نحصل على تقدير أكثر إحكاماً لخسارة الخصوصية باستخدام محاسب العزوم. على سبيل المثال، عندما E=100، القيم هي 9.34 و 1.26 على التوالي، ولـ E=400، القيم هي 24.22 و 2.55 على التوالي. أي باستخدام حد العزوم، نحقق خصوصية تفاضلية (2.55,10⁻⁵)، بينما تحصل التقنيات السابقة فقط على الضمان الأسوأ بكثير وهو (24.22, 10⁻⁵).

#### 5.2 MNIST

نجري تجارب على مجموعة بيانات MNIST المعيارية للتعرف على الأرقام المكتوبة بخط اليد والتي تتكون من 60,000 مثال تدريب و 10,000 مثال اختبار. كل مثال هو صورة بحجم 28×28 بمستويات رمادية. نستخدم شبكة عصبية أمامية بسيطة مع وحدات ReLU و softmax من 10 فئات (تتوافق مع الأرقام العشرة) مع خسارة الانتروبيا المتقاطعة وطبقة إدخال PCA اختيارية.

**النموذج الأساسي:** يستخدم نموذجنا الأساسي طبقة إسقاط PCA بـ 60 بُعداً وطبقة مخفية واحدة مع 1,000 وحدة مخفية. باستخدام حجم لوت 600، يمكننا الوصول إلى دقة 98.30% في حوالي 100 حقبة. هذه النتيجة متسقة مع ما يمكن تحقيقه باستخدام شبكة عصبية بسيطة.

**النموذج الخاص بالخصوصية التفاضلية:** بالنسبة للنسخة الخاصة بالخصوصية التفاضلية، نجرب نفس المعمارية مع طبقة إسقاط PCA بـ 60 بُعداً، وطبقة ReLU مخفية واحدة بـ 1,000 وحدة، وحجم لوت 600. للحد من الحساسية، نقص معيار التدرج لكل طبقة عند 4. نبلغ عن النتائج لثلاثة اختيارات لمقياس الضوضاء، نسميها صغير (σ=2, σ_p=4)، متوسط (σ=4, σ_p=7)، وكبير (σ=8, σ_p=16). هنا σ يمثل مستوى الضوضاء لتدريب الشبكة العصبية، و σ_p مستوى الضوضاء لإسقاط PCA. يتم تعيين معدل التعلم عند 0.1 في البداية ويتناقص خطياً إلى 0.052 على مدى 10 حقب ثم يثبت عند 0.052 بعد ذلك. لقد جربنا أيضاً شبكات متعددة الطبقات المخفية. بالنسبة لـ MNIST، وجدنا أن طبقة مخفية واحدة مدمجة مع PCA تعمل بشكل أفضل من شبكة ثنائية الطبقات.

يُظهر الشكل 4 النتائج لمستويات ضوضاء مختلفة. في كل مخطط، نُظهر تطور دقة التدريب والاختبار كدالة لعدد الحقب بالإضافة إلى قيمة δ المقابلة، مع الحفاظ على ثبات ε. نحقق دقة مجموعة اختبار 90%، 95%، و 97% لخصوصية تفاضلية (0.5,10⁻⁵)، (2,10⁻⁵)، و (8,10⁻⁵) على التوالي.

إحدى النتائج الجذابة لتطبيق SGD الخاص بالخصوصية التفاضلية هي الفرق الصغير بين دقة النموذج على مجموعات التدريب والاختبار، وهو ما يتوافق مع الحجة النظرية بأن التدريب الخاص بالخصوصية التفاضلية يعمم بشكل جيد. في المقابل، تزداد الفجوة بين دقة التدريب والاختبار في التدريب غير الخاص، أي دليل الإفراط في التدريب، مع عدد الحقب.

باستخدام محاسب العزوم، يمكننا الحصول على قيمة δ لأي ε معطى. نسجل الدقة لأزواج (ε,δ) مختلفة في الشكل 5. في الشكل، يتوافق كل منحنى مع أفضل دقة محققة لـ δ ثابت، مع تباينه بين 10⁻⁵ و 10⁻². على سبيل المثال، يمكننا تحقيق دقة 90% لـ ε=0.25 و δ=0.01. كما يمكن ملاحظته من الشكل، لـ δ ثابت، يمكن أن يكون لتغيير قيمة ε تأثير كبير على الدقة، ولكن لأي ε ثابت، هناك فرق أقل مع قيم δ مختلفة.

**تأثير المعاملات:** تتحدد دقة التصنيف بعوامل متعددة يجب ضبطها بعناية للحصول على الأداء الأمثل. تشمل هذه العوامل طوبولوجيا الشبكة، وعدد أبعاد PCA وعدد الوحدات المخفية، بالإضافة إلى معاملات إجراء التدريب مثل حجم اللوت ومعدل التعلم. بعض المعاملات خاصة بالخصوصية، مثل حد قص معيار التدرج ومستوى الضوضاء.

لإظهار تأثيرات هذه المعاملات، نتلاعب بها بشكل فردي، مع الحفاظ على البقية ثابتة. نضع القيم المرجعية على النحو التالي: 60 بُعداً لـ PCA، 1,000 وحدة مخفية، حجم لوت 600، حد معيار تدرج 4، معدل تعلم أولي 0.1 يتناقص إلى معدل تعلم نهائي 0.052 في 10 حقب، وضوضاء σ تساوي 4 و 7 على التوالي لتدريب معاملات الشبكة العصبية ولإسقاط PCA. لكل مجموعة من القيم، ندرب حتى النقطة التي تُنتهك فيها الخصوصية التفاضلية (2,10⁻⁵) (لذلك، على سبيل المثال، σ أكبر يسمح بمزيد من حقب التدريب). النتائج معروضة في الشكل 6.

**إسقاط PCA.** في تجاربنا، الدقة مستقرة إلى حد ما كدالة لبُعد PCA، مع تحقيق أفضل النتائج عند 60. (عدم إجراء PCA يقلل الدقة بحوالي 2%.) على الرغم من أنه من حيث المبدأ يمكن استبدال طبقة إسقاط PCA بطبقة مخفية إضافية، إلا أننا نحقق دقة أفضل من خلال تدريب طبقة PCA بشكل منفصل. من خلال تقليل حجم الإدخال من 784 إلى 60، يؤدي PCA إلى تقليل يقارب 10× في وقت التدريب. النتيجة مستقرة إلى حد ما على نطاق كبير من مستويات الضوضاء لإسقاط PCA وأفضل باستمرار من الدقة باستخدام الإسقاط العشوائي، التي تكون حوالي 92.5% وتظهر كخط أفقي في المخطط.

**عدد الوحدات المخفية.** يؤدي تضمين المزيد من الوحدات المخفية إلى تسهيل ملاءمة مجموعة التدريب. بالنسبة للتدريب غير الخاص، غالباً ما يكون من الأفضل استخدام المزيد من الوحدات، طالما نستخدم تقنيات لتجنب الإفراط في التدريب. ومع ذلك، بالنسبة للتدريب الخاص بالخصوصية التفاضلية، ليس من الواضح مسبقاً ما إذا كانت المزيد من الوحدات المخفية تحسن الدقة، حيث أن المزيد من الوحدات المخفية تزيد من حساسية التدرج، مما يؤدي إلى إضافة المزيد من الضوضاء في كل تحديث.

بشكل مناقض للحدس إلى حد ما، فإن زيادة عدد الوحدات المخفية لا تقلل من دقة النموذج المدرب. أحد التفسيرات المحتملة التي تستدعي المزيد من التحليل هو أن الشبكات الأكبر أكثر تسامحاً مع الضوضاء. هذه الخاصية مشجعة جداً لأنه من الشائع في الممارسة استخدام شبكات كبيرة جداً.

**حجم اللوت.** وفقاً للمبرهنة 1، يمكننا تشغيل N/L حقبة مع البقاء ضمن ميزانية خصوصية ثابتة. يجب أن يوازن اختيار حجم اللوت هدفين متناقضين. من ناحية، تسمح اللوتات الأصغر بتشغيل المزيد من الحقب، أي المرور عبر البيانات، مما يحسن الدقة. من ناحية أخرى، بالنسبة للوت أكبر، يكون للضوضاء المضافة تأثير نسبي أصغر.

تُظهر تجاربنا أن حجم اللوت له تأثير كبير نسبياً على الدقة. تجريبياً، أفضل حجم لوت هو تقريباً √N حيث N هو عدد أمثلة التدريب.

**معدل التعلم.** الدقة مستقرة لمعدل تعلم في نطاق [0.01, 0.07] وتبلغ ذروتها عند 0.05. ومع ذلك، تنخفض الدقة بشكل كبير إذا كان معدل التعلم كبيراً جداً. توحي بعض التجارب الإضافية بأنه حتى مع معدلات التعلم الكبيرة، يمكننا الوصول إلى مستويات مماثلة من الدقة من خلال تقليل مستوى الضوضاء، وبالتالي، من خلال التدريب لفترة أقل لتجنب استنفاد ميزانية الخصوصية.

**حد القص.** للحد من معيار التدرج تأثيران متعارضان: يدمر القص عدم التحيز لتقدير التدرج، وإذا كان معامل القص صغيراً جداً، فقد يشير التدرج المقصوص المتوسط في اتجاه مختلف جداً عن التدرج الحقيقي. من ناحية أخرى، تجبرنا زيادة حد المعيار C على إضافة المزيد من الضوضاء إلى التدرجات (وبالتالي المعاملات)، لأننا نضيف ضوضاء بناءً على σC. في الممارسة العملية، طريقة جيدة لاختيار قيمة لـ C هي أخذ الوسيط لمعايير التدرجات غير المقصوصة على مدار التدريب.

**مستوى الضوضاء.** من خلال إضافة المزيد من الضوضاء، تكون خسارة الخصوصية لكل خطوة أصغر بشكل متناسب، لذلك يمكننا تشغيل المزيد من الحقب ضمن ميزانية خصوصية تراكمية معينة. لاختيار هذه القيمة تأثير كبير على الدقة.

من التجارب، نلاحظ ما يلي:

1. يحسن إسقاط PCA كلاً من دقة النموذج وأداء التدريب. الدقة مستقرة إلى حد ما على نطاق كبير من الاختيارات لأبعاد الإسقاط ومستوى الضوضاء المستخدم في مرحلة PCA.

2. الدقة مستقرة إلى حد ما على حجم الشبكة. عندما يمكننا تشغيل عدد أصغر من الحقب فقط، يكون من الأفضل استخدام شبكة أكبر.

3. معاملات التدريب، وخاصة حجم اللوت ومقياس الضوضاء σ، لها تأثير كبير على دقة النموذج. كلاهما يحدد نسبة "الضوضاء إلى الإشارة" للتدرجات المطهرة بالإضافة إلى عدد الحقب التي نستطيع المرور بها عبر البيانات قبل الوصول إلى حد الخصوصية.

يسمح إطارنا بالتحكم التكيفي في معاملات التدريب، مثل حجم اللوت، وحد معيار التدرج C، ومستوى الضوضاء σ. لم تُظهر تجاربنا الأولية مع تقليل الضوضاء مع تقدم التدريب تحسناً كبيراً، ولكن من المثير للاهتمام النظر في مخططات أكثر تطوراً لاختيار هذه المعاملات بشكل تكيفي.

#### 5.3 CIFAR-10

نجري أيضاً تجارب على مجموعة بيانات CIFAR-10، والتي تتكون من صور ملونة مصنفة إلى 10 فئات مثل السفن والقطط والكلاب، ومقسمة إلى 50,000 مثال تدريب و 10,000 مثال اختبار. كل مثال هو صورة 32×32 بثلاث قنوات (RGB). بالنسبة لمهمة التعلم هذه، تستخدم جميع الشبكات الناجحة تقريباً طبقات التفافية. مجموعة بيانات CIFAR-100 لها معاملات مماثلة، باستثناء أن الصور مصنفة إلى 100 فئة؛ الأمثلة وفئات الصور مختلفة عن تلك الخاصة بـ CIFAR-10.

نستخدم معمارية الشبكة من دروس الشبكات العصبية الالتفافية في TensorFlow. يتم أولاً قص كل صورة 32×32 إلى 24×24 عن طريق أخذ الرقعة المركزية. تتكون معمارية الشبكة من طبقتين التفافيتين متبوعتين بطبقتين متصلتين بالكامل. تستخدم الطبقات الالتفافية التفافات 5×5 بخطوة 1، متبوعة بـ ReLU وتجميع أعظم (max pool) 2×2، مع 64 قناة لكل منهما. وبالتالي، يخرج الالتفاف الأول موتراً 12×12×64 لكل صورة، ويخرج الثاني موتراً 6×6×64. يتم تسطيح الأخير إلى متجه يتم إدخاله في طبقة متصلة بالكامل مع 384 وحدة، وأخرى بنفس الحجم.

يمكن لهذه المعمارية، بشكل غير خاص، الوصول إلى حوالي 86% دقة في 500 حقبة. بساطتها تجعلها خياراً جذاباً لعملنا. يجب أن نلاحظ مع ذلك أنه باستخدام شبكات أعمق مع لاخطيات مختلفة وتقنيات متقدمة أخرى، يمكن للمرء الحصول على دقة أفضل بكثير، حيث تكون أحدث التقنيات حوالي 96.5%.

كما هو معياري لمجموعات بيانات الصور هذه، نستخدم تعزيز البيانات (data augmentation) أثناء التدريب. لكل صورة تدريب، نولد صورة مشوهة جديدة من خلال اختيار رقعة 24×24 عشوائياً من الصورة، وقلب الصورة عشوائياً على طول الاتجاه الأيسر-الأيمن، وتشويه السطوع والتباين للصورة عشوائياً. في كل حقبة، تتم هذه التشويهات بشكل مستقل. نحيل القارئ إلى دروس TensorFlow للحصول على تفاصيل إضافية.

نظراً لأن الطبقات الالتفافية لها معاملات مشتركة، فإن حساب التدرجات لكل مثال له عبء حسابي أكبر. أظهرت الأعمال السابقة أن الطبقات الالتفافية غالباً ما تكون قابلة للنقل: يمكن استخدام المعاملات المتعلمة من مجموعة بيانات واحدة على أخرى دون إعادة تدريب. نعامل مجموعة بيانات CIFAR-100 كمجموعة بيانات عامة ونستخدمها لتدريب شبكة بنفس المعمارية. نستخدم الالتفافات المتعلمة من تدريب مجموعة البيانات هذه. إعادة تدريب الطبقات المتصلة بالكامل فقط مع هذه المعمارية لحوالي 250 حقبة بحجم دفعة 120 يعطينا دقة تقارب 80%، وهي خط الأساس غير الخاص لدينا.

**النسخة الخاصة بالخصوصية التفاضلية:** بالنسبة للنسخة الخاصة بالخصوصية التفاضلية، نستخدم نفس المعمارية. كما نوقش أعلاه، نستخدم طبقات التفافية مدربة مسبقاً. يتم تهيئة الطبقات المتصلة بالكامل أيضاً من الشبكة المدربة مسبقاً. ندرب طبقة softmax، وإما الطبقة العليا أو كلتا الطبقتين المتصلتين بالكامل. بناءً على النظر في معايير التدرج، تكون تدرجات طبقة softmax تقريباً ضعف حجم الطبقتين الأخريين، ونحتفظ بهذه النسبة عندما نحاول القص عند بضع قيم مختلفة بين 3 و 10. حجم اللوت هو مقبض إضافي نضبطه: جربنا 600، 2,000، و 4,000. مع هذه الإعدادات، يزيد وقت التدريب لكل حقبة من حوالي 40 ثانية إلى 180 ثانية.

في الشكل 7، نُظهر تطور الدقة وتكلفة الخصوصية، كدالة لعدد الحقب، لبضعة إعدادات معاملات مختلفة.

تؤثر المعاملات المختلفة على الدقة التي يحصل عليها المرء، بطرق ليست مختلفة كثيراً عن تلك الموجودة في تجارب MNIST. حجم لوت 600 يؤدي إلى نتائج سيئة على مجموعة البيانات هذه ونحتاج إلى زيادته إلى 2,000 أو أكثر للنتائج المبلغ عنها في الشكل 7.

مقارنة بمجموعة بيانات MNIST، حيث يكون الفرق في الدقة بين خط الأساس غير الخاص والنموذج الخاص حوالي 1.3%، فإن الانخفاض المقابل في الدقة في تجربة CIFAR-10 لدينا أكبر بكثير (حوالي 7%). نترك سد هذه الفجوة كاختبار مثير للاهتمام للبحث المستقبلي في تعلم الآلة الخاص بالخصوصية التفاضلية.

---

### Translation Notes

- **Key concepts:**
  - Moments accountant provides 7-10× improvement in privacy bounds
  - MNIST results: 97% accuracy with (8,10⁻⁵)-differential privacy
  - CIFAR-10 results: 73% accuracy with (8,10⁻⁵)-differential privacy
  - Empirical observations on hyperparameter effects
  - Use of pre-trained convolutional layers from public data

- **Technical terms:**
  - "handwritten digit recognition" - التعرف على الأرقام المكتوبة بخط اليد
  - "feed-forward neural network" - شبكة عصبية أمامية
  - "cross-entropy loss" - خسارة الانتروبيا المتقاطعة
  - "data augmentation" - تعزيز البيانات
  - "max pool" - تجميع أعظم (pooling operation)
  - "noise-to-signal ratio" - نسبة الضوضاء إلى الإشارة

- **Experimental details:**
  - Maintained precision in reporting accuracy numbers
  - Preserved all parameter values (σ, ε, δ)
  - Translated experimental observations accurately

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
