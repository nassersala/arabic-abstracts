# Section 6: Experiments
## القسم 6: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** machine learning, deep learning, neural network, logistic regression, convolutional neural network, optimization, training, dataset, minibatch, hyperparameter, dropout, convergence, sparse gradients, MNIST, CIFAR-10, IMDB

---

### English Version

To empirically evaluate the proposed method, we investigated different popular machine learning models, including logistic regression, multilayer fully connected neural networks and deep convolutional neural networks. Using large models and datasets, we demonstrate Adam can efficiently solve practical deep learning problems.

We use the same parameter initialization when comparing different optimization algorithms. The hyper-parameters, such as learning rate and momentum, are searched over a dense grid and the results are reported using the best hyper-parameter setting.

**6.1 EXPERIMENT: LOGISTIC REGRESSION**

We evaluate our proposed method on L2-regularized multi-class logistic regression using the MNIST dataset. Logistic regression has a well-studied convex objective, making it suitable for comparison of different optimizers without worrying about local minimum issues. The stepsize $\alpha$ in our logistic regression experiments is adjusted by $1/\sqrt{t}$ decay, namely $\alpha_t = \frac{\alpha}{\sqrt{t}}$ that matches with our theoratical prediction from section 4. The logistic regression classifies the class label directly on the 784 dimension image vectors. We compare Adam to accelerated SGD with Nesterov momentum and Adagrad using minibatch size of 128. According to Figure 1, we found that the Adam yields similar convergence as SGD with momentum and both converge faster than Adagrad.

As discussed in (Duchi et al., 2011), Adagrad can efficiently deal with sparse features and gradients as one of its main theoretical results whereas SGD is low at learning rare features. Adam with $1/\sqrt{t}$ decay on its stepsize should theoratically match the performance of Adagrad. We examine the sparse feature problem using IMDB movie review dataset from (Maas et al., 2011). We pre-process the IMDB movie reviews into bag-of-words (BoW) feature vectors including the first 10,000 most frequent words. The 10,000 dimension BoW feature vector for each review is highly sparse. As suggested in (Wang & Manning, 2013), 50% dropout noise can be applied to the BoW features during training to prevent over-fitting. In figure 1, Adagrad outperforms SGD with Nesterov momentum by a large margin both with and without dropout noise. Adam converges as fast as Adagrad. The empirical performance of Adam is consistent with our theoretical findings in sections 2 and 4. Similar to Adagrad, Adam can take advantage of sparse features and obtain faster convergence rate than normal SGD with momentum.

**6.2 EXPERIMENT: MULTI-LAYER NEURAL NETWORKS**

Multi-layer neural network are powerful models with non-convex objective functions. Although our convergence analysis does not apply to non-convex problems, we empirically found that Adam often outperforms other methods in such cases. In our experiments, we made model choices that are consistent with previous publications in the area; a neural network model with two fully connected hidden layers with 1000 hidden units each and ReLU activation are used for this experiment with minibatch size of 128.

First, we study different optimizers using the standard deterministic cross-entropy objective function with L2 weight decay on the parameters to prevent over-fitting. The sum-of-functions (SFO) method (Sohl-Dickstein et al., 2014) is a recently proposed quasi-Newton method that works with minibatches of data and has shown good performance on optimization of multi-layer neural networks. We used their implementation and compared with Adam to train such models. Figure 2 shows that Adam makes faster progress in terms of both the number of iterations and wall-clock time. Due to the cost of updating curvature information, SFO is 5-10x slower per iteration compared to Adam, and has a memory requirement that is linear in the number minibatches.

Stochastic regularization methods, such as dropout, are an effective way to prevent over-fitting and often used in practice due to their simplicity. SFO assumes deterministic subfunctions, and indeed failed to converge on cost functions with stochastic regularization. We compare the effectiveness of Adam to other stochastic first order methods on multi-layer neural networks trained with dropout noise. Figure 2 shows our results; Adam shows better convergence than other methods.

**6.3 EXPERIMENT: CONVOLUTIONAL NEURAL NETWORKS**

Convolutional neural networks (CNNs) with several layers of convolution, pooling and non-linear units have shown considerable success in computer vision tasks. Unlike most fully connected neural nets, weight sharing in CNNs results in vastly different gradients in different layers. A smaller learning rate for the convolution layers is often used in practice when applying SGD. We show the effectiveness of Adam in deep CNNs. Our CNN architecture has three alternating stages of 5x5 convolution filters and 3x3 max pooling with stride of 2 that are followed by a fully connected layer of 1000 rectified linear hidden units (ReLU's). The input image are pre-processed by whitening, and dropout noise is applied to the input layer and fully connected layer. The minibatch size is also set to 128 similar to previous experiments.

Interestingly, although both Adam and Adagrad make rapid progress lowering the cost in the initial stage of the training, shown in Figure 3 (left), Adam and SGD eventually converge considerably faster than Adagrad for CNNs shown in Figure 3 (right). We notice the second moment estimate $\hat{v}_t$ vanishes to zeros after a few epochs and is dominated by the $\epsilon$ in algorithm 1. The second moment estimate is therefore a poor approximation to the geometry of the cost function in CNNs comparing to fully connected network from Section 6.2. Whereas, reducing the minibatch variance through the first moment is more important in CNNs and contributes to the speed-up. As a result, Adagrad converges much slower than others in this particular experiment. Though Adam shows marginal improvement over SGD with momentum, it adapts learning rate scale for different layers instead of hand picking manually as in SGD.

**6.4 EXPERIMENT: BIAS-CORRECTION TERM**

We also empirically evaluate the effect of the bias correction terms explained in sections 2 and 3. Discussed in section 5, removal of the bias correction terms results in a version of RMSProp (Tieleman & Hinton, 2012) with momentum. We vary the $\beta_1$ and $\beta_2$ when training a variational auto-encoder (VAE) with the same architecture as in (Kingma & Welling, 2013) with a single hidden layer with 500 hidden units with softplus nonlinearities and a 50-dimensional spherical Gaussian latent variable. We iterated over a broad range of hyper-parameter choices, i.e. $\beta_1 \in [0, 0.9]$ and $\beta_2 \in [0.99, 0.999, 0.9999]$, and $\log_{10}(\alpha) \in [-5, ..., -1]$. Values of $\beta_2$ close to 1, required for robustness to sparse gradients, results in larger initialization bias; therefore we expect the bias correction term is important in such cases of slow decay, preventing an adverse effect on optimization.

In Figure 4, values $\beta_2$ close to 1 indeed lead to instabilities in training when no bias correction term was present, especially at first few epochs of the training. The best results were achieved with small values of $(1-\beta_2)$ and bias correction; this was more apparent towards the end of optimization when gradients tends to become sparser as hidden units specialize to specific patterns. In summary, Adam performed equal or better than RMSProp, regardless of hyper-parameter setting.

---

### النسخة العربية

لتقييم الطريقة المقترحة تجريبياً، قمنا بالتحقيق في نماذج تعلم آلي شائعة مختلفة، بما في ذلك الانحدار اللوجستي، والشبكات العصبية متعددة الطبقات المتصلة بالكامل، والشبكات العصبية الالتفافية العميقة. باستخدام نماذج ومجموعات بيانات كبيرة، نُظهر أن Adam يمكنها حل مشاكل التعلم العميق العملية بكفاءة.

نستخدم نفس تهيئة المعاملات عند مقارنة خوارزميات التحسين المختلفة. يتم البحث عن المعاملات الفائقة، مثل معدل التعلم والزخم، على شبكة كثيفة ويتم الإبلاغ عن النتائج باستخدام أفضل إعداد للمعاملات الفائقة.

**6.1 التجربة: الانحدار اللوجستي**

نقيّم طريقتنا المقترحة على الانحدار اللوجستي متعدد الفئات المُنظَّم بـ L2 باستخدام مجموعة بيانات MNIST. الانحدار اللوجستي له هدف محدب مدروس جيداً، مما يجعله مناسباً لمقارنة المحسِّنات المختلفة دون القلق بشأن مشاكل الحد الأدنى المحلي. يتم ضبط حجم الخطوة $\alpha$ في تجارب الانحدار اللوجستي الخاصة بنا عن طريق اضمحلال $1/\sqrt{t}$، أي $\alpha_t = \frac{\alpha}{\sqrt{t}}$ الذي يتطابق مع تنبؤنا النظري من القسم 4. يصنف الانحدار اللوجستي تسمية الفئة مباشرة على متجهات الصور ذات البُعد 784. نقارن Adam بـ SGD المُسرَّع مع زخم نيستيروف و Adagrad باستخدام حجم دفعة صغيرة 128. وفقاً للشكل 1، وجدنا أن Adam يحقق تقارباً مشابهاً لـ SGD مع الزخم وكلاهما يتقارب أسرع من Adagrad.

كما نوقش في (Duchi et al., 2011)، يمكن لـ Adagrad التعامل بكفاءة مع الميزات والتدرجات المتفرقة كإحدى نتائجه النظرية الرئيسية بينما SGD منخفض في تعلم الميزات النادرة. Adam مع اضمحلال $1/\sqrt{t}$ على حجم خطوتها يجب أن تتطابق نظرياً مع أداء Adagrad. نفحص مشكلة الميزات المتفرقة باستخدام مجموعة بيانات مراجعات أفلام IMDB من (Maas et al., 2011). نعالج مراجعات أفلام IMDB مسبقاً إلى متجهات ميزات كيس الكلمات (BoW) بما في ذلك أول 10,000 كلمة الأكثر تكراراً. متجه ميزات BoW ذو البُعد 10,000 لكل مراجعة متفرق للغاية. كما هو مقترح في (Wang & Manning, 2013)، يمكن تطبيق ضوضاء dropout بنسبة 50% على ميزات BoW أثناء التدريب لمنع الإفراط في التخصيص. في الشكل 1، يتفوق Adagrad على SGD مع زخم نيستيروف بهامش كبير سواء مع أو بدون ضوضاء dropout. يتقارب Adam بنفس سرعة Adagrad. الأداء التجريبي لـ Adam متسق مع نتائجنا النظرية في القسمين 2 و 4. مثل Adagrad، يمكن لـ Adam الاستفادة من الميزات المتفرقة والحصول على معدل تقارب أسرع من SGD العادي مع الزخم.

**6.2 التجربة: الشبكات العصبية متعددة الطبقات**

الشبكات العصبية متعددة الطبقات هي نماذج قوية مع دوال هدفية غير محدبة. على الرغم من أن تحليل التقارب الخاص بنا لا ينطبق على المسائل غير المحدبة، وجدنا تجريبياً أن Adam غالباً ما تتفوق على الطرق الأخرى في مثل هذه الحالات. في تجاربنا، قمنا باختيارات نموذجية متسقة مع المنشورات السابقة في المجال؛ يتم استخدام نموذج شبكة عصبية مع طبقتين مخفيتين متصلتين بالكامل مع 1000 وحدة مخفية لكل منهما وتفعيل ReLU لهذه التجربة مع حجم دفعة صغيرة 128.

أولاً، ندرس محسِّنات مختلفة باستخدام دالة الهدف القياسية الحتمية للإنتروبيا المتقاطعة مع اضمحلال أوزان L2 على المعاملات لمنع الإفراط في التخصيص. طريقة مجموع الدوال (SFO) (Sohl-Dickstein et al., 2014) هي طريقة شبه نيوتن مقترحة مؤخراً تعمل مع دفعات صغيرة من البيانات وأظهرت أداءً جيداً في تحسين الشبكات العصبية متعددة الطبقات. استخدمنا تنفيذهم وقارنا مع Adam لتدريب مثل هذه النماذج. يُظهر الشكل 2 أن Adam تحرز تقدماً أسرع من حيث عدد التكرارات ووقت الساعة الجدارية. بسبب تكلفة تحديث معلومات الانحناء، فإن SFO أبطأ بـ 5-10 مرات لكل تكرار مقارنة بـ Adam، ولديها متطلب ذاكرة خطي في عدد الدفعات الصغيرة.

طرق التنظيم العشوائية، مثل dropout، هي طريقة فعالة لمنع الإفراط في التخصيص وتُستخدم غالباً في الممارسة العملية نظراً لبساطتها. يفترض SFO دوالاً فرعية حتمية، وفشل بالفعل في التقارب على دوال التكلفة مع التنظيم العشوائي. نقارن فعالية Adam بطرق الدرجة الأولى العشوائية الأخرى على الشبكات العصبية متعددة الطبقات المدربة مع ضوضاء dropout. يُظهر الشكل 2 نتائجنا؛ تُظهر Adam تقارباً أفضل من الطرق الأخرى.

**6.3 التجربة: الشبكات العصبية الالتفافية**

الشبكات العصبية الالتفافية (CNNs) مع عدة طبقات من الالتفاف والتجميع والوحدات غير الخطية أظهرت نجاحاً كبيراً في مهام الرؤية الحاسوبية. على عكس معظم الشبكات العصبية المتصلة بالكامل، فإن مشاركة الأوزان في CNNs تؤدي إلى تدرجات مختلفة بشكل كبير في الطبقات المختلفة. غالباً ما يُستخدم معدل تعلم أصغر لطبقات الالتفاف في الممارسة العملية عند تطبيق SGD. نُظهر فعالية Adam في CNNs العميقة. معمارية CNN الخاصة بنا لديها ثلاث مراحل متناوبة من مرشحات التفاف 5x5 وتجميع أقصى 3x3 مع خطوة 2 متبوعة بطبقة متصلة بالكامل من 1000 وحدة خطية مصححة مخفية (ReLU). يتم معالجة صورة الإدخال مسبقاً بالتبييض، ويتم تطبيق ضوضاء dropout على طبقة الإدخال والطبقة المتصلة بالكامل. حجم الدفعة الصغيرة مُعيَّن أيضاً إلى 128 مشابهاً للتجارب السابقة.

من المثير للاهتمام أنه على الرغم من أن كلاً من Adam و Adagrad يحرزان تقدماً سريعاً في خفض التكلفة في المرحلة الأولية من التدريب، كما هو موضح في الشكل 3 (يسار)، إلا أن Adam و SGD يتقاربان في النهاية بشكل أسرع بكثير من Adagrad لـ CNNs كما هو موضح في الشكل 3 (يمين). نلاحظ أن تقدير العزم الثاني $\hat{v}_t$ يتلاشى إلى أصفار بعد بضع حقب ويهيمن عليه $\epsilon$ في الخوارزمية 1. وبالتالي فإن تقدير العزم الثاني هو تقريب ضعيف لهندسة دالة التكلفة في CNNs مقارنة بالشبكة المتصلة بالكامل من القسم 6.2. بينما، فإن تقليل تباين الدفعة الصغيرة من خلال العزم الأول أكثر أهمية في CNNs ويساهم في التسريع. ونتيجة لذلك، يتقارب Adagrad بشكل أبطأ بكثير من الآخرين في هذه التجربة بالذات. على الرغم من أن Adam تُظهر تحسناً هامشياً على SGD مع الزخم، إلا أنها تتكيف مع مقياس معدل التعلم للطبقات المختلفة بدلاً من الاختيار اليدوي كما في SGD.

**6.4 التجربة: حد تصحيح الانحياز**

نقيّم أيضاً تجريبياً تأثير حدود تصحيح الانحياز الموضحة في القسمين 2 و 3. كما نوقش في القسم 5، فإن إزالة حدود تصحيح الانحياز تؤدي إلى نسخة من RMSProp (Tieleman & Hinton, 2012) مع الزخم. نغيّر $\beta_1$ و $\beta_2$ عند تدريب مشفر تلقائي متغير (VAE) بنفس المعمارية كما في (Kingma & Welling, 2013) مع طبقة مخفية واحدة مع 500 وحدة مخفية مع لاخطيات softplus ومتغير كامن غاوسي كروي بُعد 50. قمنا بالتكرار على نطاق واسع من خيارات المعاملات الفائقة، أي $\beta_1 \in [0, 0.9]$ و $\beta_2 \in [0.99, 0.999, 0.9999]$، و $\log_{10}(\alpha) \in [-5, ..., -1]$. قيم $\beta_2$ القريبة من 1، المطلوبة للمتانة تجاه التدرجات المتفرقة، تؤدي إلى انحياز تهيئة أكبر؛ لذلك نتوقع أن يكون حد تصحيح الانحياز مهماً في مثل هذه الحالات من الاضمحلال البطيء، مما يمنع التأثير السلبي على التحسين.

في الشكل 4، قيم $\beta_2$ القريبة من 1 تؤدي بالفعل إلى عدم استقرار في التدريب عندما لم يكن هناك حد تصحيح انحياز، خاصة في الحقب القليلة الأولى من التدريب. تم تحقيق أفضل النتائج مع قيم صغيرة من $(1-\beta_2)$ وتصحيح الانحياز؛ كان هذا أكثر وضوحاً نحو نهاية التحسين عندما تميل التدرجات إلى أن تصبح أكثر تفرقاً مع تخصص الوحدات المخفية لأنماط محددة. باختصار، أدت Adam أداءً مساوياً أو أفضل من RMSProp، بغض النظر عن إعداد المعاملات الفائقة.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2, Figure 3 (left/right), Figure 4
- **Key terms introduced:**
  - Bag-of-words (كيس الكلمات)
  - Wall-clock time (وقت الساعة الجدارية)
  - Variational auto-encoder (مشفر تلقائي متغير)
  - Cross-entropy (الإنتروبيا المتقاطعة)
  - Weight decay (اضمحلال الأوزان)
  - Overfitting (الإفراط في التخصيص)
  - Epochs (حقب)
  - Whitening (التبييض)
  - Convolution filters (مرشحات الالتفاف)
  - Max pooling (تجميع أقصى)
  - Stride (خطوة)
- **Equations:** Several equations showing decay rates and update rules
- **Citations:** Multiple citations throughout experiments
- **Special handling:**
  - Dataset names (MNIST, CIFAR-10, IMDB) kept in English
  - Algorithm names kept in English
  - Figure references maintained
  - Experimental parameters and settings carefully translated
  - Technical terms from glossary used consistently

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
