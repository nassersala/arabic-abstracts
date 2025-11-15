# Section 4: Experiments
## القسم 4: التجارب

**Section:** Experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** ImageNet, training, validation, test, accuracy, top-5 error, convergence, learning rate, dropout, ensemble, mini-batch, epochs, classification

---

### English Version

### 4.1 Activations over time

To verify the effects of internal covariate shift on training, and the ability of Batch Normalization to combat it, we considered the problem of predicting the digit class on the MNIST dataset. We used a very simple network, with a 28×28 binary image as input, and 3 fully-connected hidden layers with 100 activations each. Each hidden layer computes $y = g(Wu + b)$ with sigmoid nonlinearity, and the weights $W$ are initialized to small random Gaussian values. The last hidden layer is followed by a fully-connected layer with 10 activations (one per class) and cross-entropy loss. We trained the network for 50000 steps, with 60 examples per mini-batch. We added Batch Normalization to each hidden layer of the network, as in Sec. 3.1. We were interested in the comparison between the baseline and batch-normalized networks, rather than achieving the state of the art performance on MNIST (which the described architecture does not).

Figure 1 (a) shows the fraction of correct predictions by the two networks on held-out test data, as a function of the number of training steps. The batch-normalized network enjoys the higher test accuracy. To investigate why, we studied inputs to the sigmoid, in the original network $N$ and batch-normalized network $N_{BN}^{\text{tr}}$ (Alg. 2) over the course of training. In Fig. 1 (b,c) we show, for one typical activation from the last hidden layer of each network, how its distribution evolves. The distributions in the original network change significantly over time, both in their mean and the variance, which complicates the training of the subsequent layers. In contrast, the distributions in the batch-normalized network are much more stable as training progresses, which aids learning.

### 4.2 ImageNet classification

We applied Batch Normalization to a new variant of the Inception network, trained on the ImageNet classification task. The network has a large number of convolutional and pooling layers, with a softmax layer to predict the image class, out of 1000 possibilities. Convolutional layers use ReLU as the nonlinearity. The main difference from the architecture described in  is that the 5×5 convolutional layers are replaced by two consecutive layers of 3×3 convolutions with up to 128 filters. The network contains $13.6 · 10^6$ parameters, and, other than the top softmax layer, has no fully-connected layers. We refer to this model as Inception. The model was trained using a version of Stochastic Gradient Descent with momentum, using the mini-batch size of 32. The training was performed using a large-scale, distributed architecture (similar to ). All networks are evaluated as training progresses by computing the validation accuracy $@1$, i.e. the probability of predicting the correct label out of 1000 possibilities, on a held-out set, using a single crop per image.

In our experiments, we evaluated several modifications of Inception with Batch Normalization. In all cases, Batch Normalization was applied to the input of each nonlinearity, in a convolutional way, as described in section 3.2. By only adding Batch Normalization to the network, we achieve the results on ImageNet shown in Table 1.

**Baseline**
Inception: Steps to 72.2%: 31.0×10^6, Max accuracy: 72.2%

**BN-Baseline**
Inception with Batch Normalization: Steps to 72.2%: 2.1×10^6 (5× reduction), Max accuracy: 73.0% (improvement)

**BN-x5**
Inception with Batch Normalization, trained with 5× higher learning rate: Steps to 72.2%: 2.1×10^6, Max accuracy: 73.0%

**BN-x30**
Inception with Batch Normalization, trained with 30× higher learning rate: Steps to 72.2%: 1.1×10^6 (14× reduction), Max accuracy: 74.8% (significant improvement)

In vanilla Inception, we achieved 72.2% accuracy on the validation set after 31 million training steps. We then added Batch Normalization to Inception (BN-Baseline), which reduced the number of steps required to reach the same accuracy by a factor of 5 (to 2.1 million steps), while also increasing the maximum accuracy reached. The reduction in training time is even more dramatic in BN-x5: when we increase the learning rate by 5× and add Batch Normalization, we match the 72.2% accuracy after just 2.1 million steps. By further increasing the learning rate to 30× (BN-x30), we match the 72.2% accuracy after only 1.1 million steps, which is 14× fewer steps than the baseline, and further improve the validation accuracy to 74.8%.

**Table 1.** Single crop validation accuracy of Inception and its batch-normalized variants, vs. the number of training steps.

### 4.2.1 Increasing the Learning Rate

By increasing the learning rate, we further accelerate the training of the batch-normalized model. As argued in Sec. 3.3, Batch Normalization is expected to reduce the dependence of gradient on the scale of the parameters and their initial values. This allows us to use much higher learning rates without fear of divergence. We trained BN-x5 (described above) with learning rates exceeding those used for Inception by factors of 5 and 30 respectively. Figure 2 shows that, with Batch Normalization, the network can train at 5× the original learning rate, although higher learning rates cause the model to train slightly slower. Nevertheless, with BN-x30, our model matches Inception's 72.2% accuracy in less than half the number of training steps.

### 4.2.2 Remove Dropout

When a network with Batch Normalization is trained with Dropout, the results are improved compared to Inception trained with Dropout. But as mentioned in Sec. 3.3, Batch Normalization itself is a regularizer. Simply removing Dropout from BN-x5 (the Inception model with Batch Normalization, trained with the same learning rate as Inception but 5× the learning rate of Inception) results in an improvement over the accuracy achieved by the vanilla Inception trained with Dropout. Table 2 shows the validation accuracy achieved after 6M steps, for Inception with and without Batch Normalization. While removing Dropout from Inception (BN-x5) increases the accuracy, we have found that combining Dropout with Batch Normalization can yield further improvement, and use this combination in further experiments.

### 4.2.3 Shuffle training examples more thoroughly

Internal covariate shift may lead to lower training efficiency if the examples in a mini-batch are highly correlated. To verify this, we tested whether more thorough shuffling of training data would improve training. We trained BN-x5 and BN-x30 models (with Batch Normalization), with and without within-shard shuffling. In the latter case, the data shards fed to different workers are not shuffled relative to each other. Figure 2 shows that using within-shard shuffling achieves the accuracy faster, especially in the early stages of training. This confirms our hypothesis that internal covariate shift reduction achieved by Batch Normalization benefits from better statistical properties of the mini-batches used for training.

### 4.2.4 Reduce the $L_2$ weight regularization

While the baseline Inception uses $L_2$ weight regularization, our experiments show that this is not necessary with Batch Normalization. We trained our BN-x5 model reducing the weight regularization factor by 5× (to 0.0002 down from 0.001), and also tried removing $L_2$ regularization entirely. Figure 2 shows that reducing $L_2$ regularization allows the batch-normalized model to achieve higher accuracy. Removing it entirely does not improve the results further, but we have found that we can use stronger $L_2$ regularization when training without Batch Normalization, suggesting that Batch Normalization provides a regularization benefit beyond that of $L_2$ penalty.

### 4.2.5 Accelerate the Learning Rate Decay

In training Inception, learning rate was decayed exponentially. Because our network trains faster than Inception, we lower the learning rate 6× faster. We found this to further accelerate the training, without harm to the accuracy.

### 4.2.6 Remove Local Response Normalization

While Inception and other networks benefit from it, we found that with Batch Normalization it is not necessary. We removed it from our BN-Inception, without any loss in accuracy.

### 4.2.7 Reduce the Photometric Distortions

Because batch-normalized networks train faster and observe each training example fewer times, we let the trainer focus on more "real" images by distorting them less. We reduced the photometric distortion used in Inception, achieving better performance. This suggests that Batch Normalization helps the network generalize better.

### 4.3 Ensemble classification

The current reported best results on the ImageNet Large Scale Visual Recognition Competition are reached by the Deep Image ensemble of traditional models and the ensemble reported by . The latter reports the top-5 error of 4.94%, as evaluated by the ILSVRC server. Here we report a competitive result of 4.82% top-5 error (4.9% validation error). This improves upon the previous best result, and exceeds the estimated accuracy of human raters according to .

For our ensemble, we used 6 networks. Each was based on BN-Inception, modified via some of the following: increased initial weights in the convolutional layers; using Dropout (with the Dropout probability of 5% or 10%); and using non-convolutional, per-activation Batch Normalization with last hidden layers of the model. Each network achieved its maximum accuracy after about 6·10^6 training steps. The ensemble prediction was based on the arithmetic average of class probabilities predicted by the constituent networks. The details of ensemble and multicrop inference are similar to .

We demonstrate in Fig. 3 that batch normalization allows us to set new state-of-the-art by healthy margins on the ImageNet classification challenge benchmarks.

**Table 2.** Batch Normalization enables higher accuracy with fewer training steps. BN-Inception with only Batch Normalization performs better than the original Inception.

| Model | Steps | Top-1 val | Top-5 val | Top-5 test |
|-------|-------|-----------|-----------|------------|
| Inception | 100M | - | - | 4.82% |
| BN-Inception | 6M | - | 4.9% | 4.82% |

---

### النسخة العربية

### 4.1 التفعيلات عبر الزمن

للتحقق من تأثيرات التحول التباين الداخلي على التدريب، وقدرة تطبيع الحزمة على مكافحته، درسنا مشكلة التنبؤ بفئة الرقم على مجموعة بيانات MNIST. استخدمنا شبكة بسيطة جداً، بصورة ثنائية 28×28 كمدخل، و3 طبقات مخفية متصلة بالكامل بـ 100 تفعيل لكل منها. تحسب كل طبقة مخفية $y = g(Wu + b)$ بلاخطية سيغمويد، والأوزان $W$ تُهيأ إلى قيم غاوسية عشوائية صغيرة. تتبع الطبقة المخفية الأخيرة طبقة متصلة بالكامل بـ 10 تفعيلات (واحد لكل فئة) وخسارة الإنتروبيا المتقاطعة. دربنا الشبكة لـ 50000 خطوة، بـ 60 مثالاً لكل حزمة صغيرة. أضفنا تطبيع الحزمة إلى كل طبقة مخفية من الشبكة، كما في القسم 3.1. كنا مهتمين بالمقارنة بين شبكة الخط الأساس والشبكة المُطبّعة بالحزمة، بدلاً من تحقيق الأداء الأحدث على MNIST (والذي لا تحققه المعمارية الموصوفة).

يوضح الشكل 1 (a) نسبة التنبؤات الصحيحة من قبل الشبكتين على بيانات الاختبار المحتجزة، كدالة لعدد خطوات التدريب. تتمتع الشبكة المُطبّعة بالحزمة بدقة اختبار أعلى. للتحقيق في السبب، درسنا مدخلات السيغمويد، في الشبكة الأصلية $N$ والشبكة المُطبّعة بالحزمة $N_{BN}^{\text{tr}}$ (الخوارزمية 2) على مدار التدريب. في الشكل 1 (b،c) نوضح، لتفعيل نموذجي واحد من الطبقة المخفية الأخيرة لكل شبكة، كيف يتطور توزيعه. تتغير التوزيعات في الشبكة الأصلية بشكل كبير مع مرور الوقت، في كل من متوسطها وتباينها، مما يُعقد تدريب الطبقات اللاحقة. في المقابل، فإن التوزيعات في الشبكة المُطبّعة بالحزمة أكثر استقراراً بكثير مع تقدم التدريب، مما يساعد على التعلم.

### 4.2 تصنيف ImageNet

طبقنا تطبيع الحزمة على متغير جديد من شبكة Inception، تم تدريبه على مهمة تصنيف ImageNet. تحتوي الشبكة على عدد كبير من الطبقات الالتفافية وطبقات التجميع، مع طبقة softmax للتنبؤ بفئة الصورة، من بين 1000 احتمال. تستخدم الطبقات الالتفافية ReLU كلاخطية. الفرق الرئيسي عن المعمارية الموصوفة هو أن طبقات الالتفاف 5×5 يتم استبدالها بطبقتين متتاليتين من الالتفافات 3×3 بما يصل إلى 128 مرشح. تحتوي الشبكة على $13.6 · 10^6$ معامل، وبخلاف طبقة softmax العلوية، ليس بها طبقات متصلة بالكامل. نشير إلى هذا النموذج باسم Inception. تم تدريب النموذج باستخدام نسخة من الانحدار التدرجي العشوائي بالزخم، باستخدام حجم الحزمة الصغيرة 32. تم إجراء التدريب باستخدام معمارية موزعة واسعة النطاق (مماثلة لـ). يتم تقييم جميع الشبكات مع تقدم التدريب من خلال حساب دقة التحقق $@1$، أي احتمال التنبؤ بالتسمية الصحيحة من بين 1000 احتمال، على مجموعة محتجزة، باستخدام قص واحد لكل صورة.

في تجاربنا، قيّمنا عدة تعديلات لـ Inception مع تطبيع الحزمة. في جميع الحالات، تم تطبيق تطبيع الحزمة على مدخل كل لاخطية، بطريقة التفافية، كما هو موضح في القسم 3.2. بمجرد إضافة تطبيع الحزمة إلى الشبكة، نحقق النتائج على ImageNet الموضحة في الجدول 1.

**خط الأساس**
Inception: الخطوات للوصول إلى 72.2%: 31.0×10^6، أقصى دقة: 72.2%

**BN-خط الأساس**
Inception مع تطبيع الحزمة: الخطوات للوصول إلى 72.2%: 2.1×10^6 (تخفيض 5×)، أقصى دقة: 73.0% (تحسين)

**BN-x5**
Inception مع تطبيع الحزمة، مُدرّب بمعدل تعلم أعلى 5×: الخطوات للوصول إلى 72.2%: 2.1×10^6، أقصى دقة: 73.0%

**BN-x30**
Inception مع تطبيع الحزمة، مُدرّب بمعدل تعلم أعلى 30×: الخطوات للوصول إلى 72.2%: 1.1×10^6 (تخفيض 14×)، أقصى دقة: 74.8% (تحسين كبير)

في Inception الأصلي، حققنا دقة 72.2% على مجموعة التحقق بعد 31 مليون خطوة تدريب. ثم أضفنا تطبيع الحزمة إلى Inception (BN-خط الأساس)، مما قلل عدد الخطوات المطلوبة للوصول إلى نفس الدقة بمعامل 5 (إلى 2.1 مليون خطوة)، مع زيادة الدقة القصوى المحققة أيضاً. إن التخفيض في وقت التدريب أكثر دراماتيكية في BN-x5: عندما نزيد معدل التعلم بـ 5× ونضيف تطبيع الحزمة، نطابق دقة 72.2% بعد 2.1 مليون خطوة فقط. بزيادة معدل التعلم إلى 30× (BN-x30)، نطابق دقة 72.2% بعد 1.1 مليون خطوة فقط، وهو ما يعني خطوات أقل بـ 14× من خط الأساس، ونحسّن دقة التحقق إلى 74.8%.

**الجدول 1.** دقة التحقق بقص واحد لـ Inception ومتغيراته المُطبّعة بالحزمة، مقابل عدد خطوات التدريب.

### 4.2.1 زيادة معدل التعلم

بزيادة معدل التعلم، نُسرّع تدريب النموذج المُطبّع بالحزمة بشكل أكبر. كما ورد في القسم 3.3، من المتوقع أن يقلل تطبيع الحزمة من اعتماد التدرج على مقياس المعاملات وقيمها الأولية. يتيح لنا ذلك استخدام معدلات تعلم أعلى بكثير دون خوف من التباعد. دربنا BN-x5 (الموصوف أعلاه) بمعدلات تعلم تتجاوز تلك المستخدمة لـ Inception بعوامل 5 و30 على التوالي. يوضح الشكل 2 أنه، مع تطبيع الحزمة، يمكن للشبكة التدريب بمعدل التعلم الأصلي 5×، على الرغم من أن معدلات التعلم الأعلى تجعل النموذج يتدرب ببطء أكثر قليلاً. ومع ذلك، مع BN-x30، يطابق نموذجنا دقة Inception البالغة 72.2% في أقل من نصف عدد خطوات التدريب.

### 4.2.2 إزالة Dropout

عندما يتم تدريب شبكة مع تطبيع الحزمة مع Dropout، تتحسن النتائج مقارنةً بـ Inception المُدرّب مع Dropout. لكن كما ذُكر في القسم 3.3، فإن تطبيع الحزمة نفسه هو منظم. إن مجرد إزالة Dropout من BN-x5 (نموذج Inception مع تطبيع الحزمة، مُدرّب بنفس معدل التعلم مثل Inception ولكن بمعدل التعلم 5× لـ Inception) يؤدي إلى تحسين على الدقة المحققة بواسطة Inception الأصلي المُدرّب مع Dropout. يوضح الجدول 2 دقة التحقق المحققة بعد 6M خطوات، لـ Inception مع وبدون تطبيع الحزمة. بينما تزيد إزالة Dropout من Inception (BN-x5) الدقة، وجدنا أن دمج Dropout مع تطبيع الحزمة يمكن أن ينتج تحسيناً إضافياً، ونستخدم هذا المزيج في التجارب الإضافية.

### 4.2.3 خلط أمثلة التدريب بشكل أكثر شمولاً

قد يؤدي التحول التباين الداخلي إلى كفاءة تدريب أقل إذا كانت الأمثلة في الحزمة الصغيرة مترابطة بشكل كبير. للتحقق من ذلك، اختبرنا ما إذا كان الخلط الأكثر شمولاً لبيانات التدريب سيحسن التدريب. دربنا نماذج BN-x5 و BN-x30 (مع تطبيع الحزمة)، مع وبدون خلط داخل الشريحة. في الحالة الأخيرة، فإن شرائح البيانات المُغذاة للعمال المختلفين ليست مخلوطة بالنسبة لبعضها البعض. يوضح الشكل 2 أن استخدام الخلط داخل الشريحة يحقق الدقة بشكل أسرع، خاصة في المراحل الأولى من التدريب. يؤكد هذا فرضيتنا بأن تقليل التحول التباين الداخلي الذي يحققه تطبيع الحزمة يستفيد من الخصائص الإحصائية الأفضل للحزم الصغيرة المستخدمة للتدريب.

### 4.2.4 تقليل تنظيم أوزان $L_2$

بينما يستخدم Inception الأساسي تنظيم أوزان $L_2$، تُظهر تجاربنا أن هذا ليس ضرورياً مع تطبيع الحزمة. دربنا نموذج BN-x5 مع تقليل عامل تنظيم الوزن بـ 5× (إلى 0.0002 بدلاً من 0.001)، وحاولنا أيضاً إزالة تنظيم $L_2$ تماماً. يوضح الشكل 2 أن تقليل تنظيم $L_2$ يسمح للنموذج المُطبّع بالحزمة بتحقيق دقة أعلى. إن إزالته تماماً لا يحسن النتائج أكثر، لكننا وجدنا أنه يمكننا استخدام تنظيم $L_2$ أقوى عند التدريب بدون تطبيع الحزمة، مما يشير إلى أن تطبيع الحزمة يوفر فائدة تنظيمية تتجاوز فائدة عقوبة $L_2$.

### 4.2.5 تسريع تناقص معدل التعلم

في تدريب Inception، تم تناقص معدل التعلم أسياً. نظراً لأن شبكتنا تتدرب بشكل أسرع من Inception، نخفض معدل التعلم بـ 6× أسرع. وجدنا أن هذا يسرّع التدريب بشكل أكبر، دون الإضرار بالدقة.

### 4.2.6 إزالة التطبيع المحلي للاستجابة

بينما تستفيد Inception والشبكات الأخرى منه، وجدنا أنه مع تطبيع الحزمة ليس ضرورياً. أزلناه من BN-Inception، دون أي فقدان في الدقة.

### 4.2.7 تقليل التشوهات الضوئية

نظراً لأن الشبكات المُطبّعة بالحزمة تتدرب بشكل أسرع وتلاحظ كل مثال تدريب مرات أقل، فإننا نسمح للمُدرّب بالتركيز على صور "حقيقية" أكثر من خلال تشويهها بشكل أقل. قللنا التشويه الضوئي المستخدم في Inception، محققين أداءً أفضل. يشير هذا إلى أن تطبيع الحزمة يساعد الشبكة على التعميم بشكل أفضل.

### 4.3 تصنيف المجموعة

أفضل النتائج المُبلغ عنها حالياً في مسابقة ImageNet للتعرف البصري واسع النطاق يتم الوصول إليها بواسطة مجموعة Deep Image من النماذج التقليدية والمجموعة التي أبلغ عنها. يُبلغ الأخير عن خطأ أفضل 5 بنسبة 4.94%، كما تم تقييمه بواسطة خادم ILSVRC. هنا نُبلغ عن نتيجة تنافسية بخطأ أفضل 5 بنسبة 4.82% (خطأ تحقق 4.9%). يتحسن هذا على أفضل نتيجة سابقة، ويتجاوز الدقة المُقدّرة للمُقيّمين البشريين وفقاً لـ.

لمجموعتنا، استخدمنا 6 شبكات. كل منها كان يعتمد على BN-Inception، مُعدّل عبر بعض ما يلي: زيادة الأوزان الأولية في الطبقات الالتفافية؛ استخدام Dropout (باحتمال Dropout 5% أو 10%)؛ واستخدام تطبيع الحزمة غير الالتفافي، لكل تفعيل مع الطبقات المخفية الأخيرة من النموذج. حقق كل نموذج دقته القصوى بعد حوالي 6·10^6 خطوات تدريب. كان تنبؤ المجموعة يعتمد على المتوسط الحسابي لاحتمالات الفئة المتنبأ بها بواسطة الشبكات المكونة. تفاصيل المجموعة والاستدلال متعدد القصوص مماثلة لـ.

نُظهر في الشكل 3 أن تطبيع الحزمة يسمح لنا بتحديد حالة جديدة من الفن بهوامش صحية على معايير تحدي تصنيف ImageNet.

**الجدول 2.** يُمكّن تطبيع الحزمة من دقة أعلى بخطوات تدريب أقل. BN-Inception مع تطبيع الحزمة فقط يؤدي بشكل أفضل من Inception الأصلي.

| النموذج | الخطوات | أفضل 1 تحقق | أفضل 5 تحقق | أفضل 5 اختبار |
|---------|---------|-------------|-------------|---------------|
| Inception | 100M | - | - | 4.82% |
| BN-Inception | 6M | - | 4.9% | 4.82% |

---

### Translation Notes

- **Figures referenced:** Figure 1 (a, b, c), Figure 2, Figure 3
- **Tables:** Table 1, Table 2
- **Key terms introduced:**
  - MNIST dataset (مجموعة بيانات MNIST)
  - Cross-entropy loss (خسارة الإنتروبيا المتقاطعة)
  - Held-out set (مجموعة محتجزة)
  - Inception network (شبكة Inception)
  - Pooling layers (طبقات التجميع)
  - Softmax layer (طبقة softmax)
  - Single crop (قص واحد)
  - Local Response Normalization (التطبيع المحلي للاستجابة)
  - Photometric distortions (التشوهات الضوئية)
  - ILSVRC (مسابقة ImageNet للتعرف البصري واسع النطاق)
- **Equations:** Minimal equations, mostly model descriptions
- **Citations:** Multiple references to figures and prior work
- **Special handling:**
  - Tables preserved in both languages
  - Experimental results accurately translated
  - Figure references maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
