# Section 3: The Architecture
## القسم 3: المعمارية

**Section:** architecture
**Translation Quality:** 0.88
**Glossary Terms Used:** architecture, neural network, convolutional, activation, normalization, training, GPU, layer, pooling

---

### English Version

The architecture of our network is summarized in Figure 2. It contains eight learned layers — five convolutional and three fully-connected. Below, we describe some of the novel or unusual features of our network's architecture. Sections 3.1-3.4 are sorted according to our estimation of their importance, with the most important first.

#### 3.1 ReLU Nonlinearity

The standard way to model a neuron's output f as a function of its input x is with f(x) = tanh(x) or f(x) = (1 + e^−x)^−1. In terms of training time with gradient descent, these saturating nonlinearities are much slower than the non-saturating nonlinearity f(x) = max(0, x). Following Nair and Hinton [20], we refer to neurons with this nonlinearity as Rectified Linear Units (ReLUs). Deep convolutional neural networks with ReLUs train several times faster than their equivalents with tanh units. This is demonstrated in Figure 1, which shows the number of iterations required to reach 25% training error on the CIFAR-10 dataset for a particular four-layer convolutional network. This plot shows that we would not have been able to experiment with such large neural networks for this work if we had used traditional saturating neuron models.

We are not the first to consider alternatives to traditional neuron models in CNNs. For example, Jarrett et al. [11] claim that the nonlinearity f(x) = |tanh(x)| works particularly well with their type of contrast normalization followed by local average pooling on the Caltech-101 dataset. However, on this dataset the primary concern is preventing overfitting, so the effect they are observing is different from the accelerated ability to fit the training set which we report when using ReLUs. Faster learning has a great influence on the performance of large models trained on large datasets.

#### 3.2 Training on Multiple GPUs

A single GTX 580 GPU has only 3GB of memory, which limits the maximum size of the networks that can be trained on it. It turns out that 1.2 million training examples are enough to train networks which are too big to fit on one GPU. Therefore we spread the network across two GPUs. Current GPUs are particularly well-suited to cross-GPU parallelization, as they are able to read from and write to one another's memory directly, without going through host machine memory. The parallelization scheme that we employ essentially puts half of the kernels (or neurons) on each GPU, with one additional trick: the GPUs communicate only in certain layers. This means that, for example, the kernels of layer 3 take input from all kernel maps in layer 2. However, kernels in layer 4 take input only from those kernel maps in layer 3 which reside on the same GPU. Choosing the pattern of connectivity is a problem for cross-validation, but this allows us to precisely tune the amount of communication until it is an acceptable fraction of the amount of computation.

The resultant architecture is somewhat similar to that of the "columnar" CNN employed by Cireşan et al. [5], except that our columns are not independent (see Figure 2). This scheme reduces our top-1 and top-5 error rates by 1.7% and 1.2%, respectively, as compared with a net with half as many kernels in each convolutional layer trained on one GPU. The two-GPU net takes slightly less time to train than the one-GPU net.

#### 3.3 Local Response Normalization

ReLUs have the desirable property that they do not require input normalization to prevent them from saturating. If at least some training examples produce a positive input to a ReLU, learning will happen in that neuron. However, we still found that the following local normalization scheme aids generalization. Denoting by a^i_{x,y} the activity of a neuron computed by applying kernel i at position (x, y) and then applying the ReLU nonlinearity, the response-normalized activity b^i_{x,y} is given by the expression

$$b^i_{x,y} = a^i_{x,y} / \\left(k + \\alpha \\sum_{j=\\max(0,i-n/2)}^{\\min(N-1,i+n/2)} (a^j_{x,y})^2\\right)^{\\beta}$$

where the sum runs over n "adjacent" kernel maps at the same spatial position, and N is the total number of kernels in the layer. The ordering of the kernel maps is of course arbitrary and determined before training begins. This sort of response normalization implements a form of lateral inhibition inspired by the type found in real neurons, creating competition for big activities amongst neuron outputs computed using different kernels. The constants k, n, α, and β are hyper-parameters whose values are determined using a validation set; we used k = 2, n = 5, α = 10^−4, and β = 0.75. We applied this normalization after applying the ReLU nonlinearity in certain layers (see Section 3.5).

This scheme bears some resemblance to the local contrast normalization scheme of Jarrett et al. [11], but ours would be more correctly termed "brightness normalization", since we do not subtract the mean activity. Response normalization reduces our top-1 and top-5 error rates by 1.4% and 1.2%, respectively. We also verified the effectiveness of this scheme on the CIFAR-10 dataset: a four-layer CNN achieved a 13% test error rate without normalization and 11% with normalization.

#### 3.4 Overlapping Pooling

Pooling layers in CNNs summarize the outputs of neighboring groups of neurons in the same kernel map. Traditionally, the neighborhoods summarized by adjacent pooling units do not overlap (e.g., [17, 11, 4]). To be more precise, a pooling layer can be thought of as consisting of a grid of pooling units spaced s pixels apart, each summarizing a neighborhood of size z × z centered at the location of the pooling unit. If we set s = z, we obtain traditional local pooling as commonly employed in CNNs. If we set s < z, we obtain overlapping pooling. This is what we use throughout our network, with s = 2 and z = 3. This scheme reduces the top-1 and top-5 error rates by 0.4% and 0.3%, respectively, as compared with the non-overlapping scheme s = 2, z = 2, which produces output of equivalent dimensions. We generally observe during training that models with overlapping pooling find it slightly more difficult to overfit.

#### 3.5 Overall Architecture

Now we are ready to describe the overall architecture of our CNN. As depicted in Figure 2, the net contains eight layers with weights; the first five are convolutional and the remaining three are fully-connected. The output of the last fully-connected layer is fed to a 1000-way softmax which produces a distribution over the 1000 class labels. Our network maximizes the multinomial logistic regression objective, which is equivalent to maximizing the average across training cases of the log-probability of the correct label under the prediction distribution.

The kernels of the second, fourth, and fifth convolutional layers are connected only to those kernel maps in the previous layer which reside on the same GPU (see Figure 2). The kernels of the third convolutional layer are connected to all kernel maps in the second layer. The neurons in the fully-connected layers are connected to all neurons in the previous layer. Response-normalization layers follow the first and second convolutional layers. Max-pooling layers, of the kind described in Section 3.4, follow both response-normalization layers as well as the fifth convolutional layer. The ReLU non-linearity is applied to the output of every convolutional and fully-connected layer.

The first convolutional layer filters the 224 × 224 × 3 input image with 96 kernels of size 11 × 11 × 3 with a stride of 4 pixels (this is the distance between the receptive field centers of neighboring neurons in a kernel map). The second convolutional layer takes as input the (response-normalized and pooled) output of the first convolutional layer and filters it with 256 kernels of size 5 × 5 × 48. The third, fourth, and fifth convolutional layers are connected to one another without any intervening pooling or normalization layers. The third convolutional layer has 384 kernels of size 3 × 3 × 256 connected to the (normalized, pooled) outputs of the second convolutional layer. The fourth convolutional layer has 384 kernels of size 3 × 3 × 192, and the fifth convolutional layer has 256 kernels of size 3 × 3 × 192. The fully-connected layers have 4096 neurons each.

---

### النسخة العربية

يتم تلخيص معمارية شبكتنا في الشكل 2. تحتوي على ثماني طبقات قابلة للتعلم - خمس طبقات التفافية وثلاث طبقات متصلة بالكامل. فيما يلي، نصف بعض الميزات الجديدة أو غير العادية لمعمارية شبكتنا. تم ترتيب الأقسام 3.1-3.4 وفقاً لتقديرنا لأهميتها، مع الأهم أولاً.

#### 3.1 اللاخطية ReLU

الطريقة القياسية لنمذجة مخرج العصبون f كدالة لمدخله x هي باستخدام f(x) = tanh(x) أو f(x) = (1 + e^−x)^−1. من حيث وقت التدريب مع الانحدار التدرجي، فإن هذه اللاخطيات المشبعة أبطأ بكثير من اللاخطية غير المشبعة f(x) = max(0, x). تبعاً لـ Nair وHinton [20]، نشير إلى العصبونات ذات هذه اللاخطية باسم وحدات خطية مُصححة (Rectified Linear Units - ReLUs). تتدرب الشبكات العصبية الالتفافية العميقة مع ReLUs بشكل أسرع عدة مرات من نظيراتها التي تستخدم وحدات tanh. يتضح ذلك في الشكل 1، الذي يوضح عدد التكرارات المطلوبة للوصول إلى خطأ تدريب بنسبة 25% على مجموعة بيانات CIFAR-10 لشبكة التفافية معينة مكونة من أربع طبقات. يوضح هذا الرسم أننا لم نكن لنتمكن من التجربة مع شبكات عصبية كبيرة جداً لهذا العمل لو كنا قد استخدمنا نماذج العصبونات المشبعة التقليدية.

نحن لسنا الأوائل في النظر في بدائل لنماذج العصبونات التقليدية في الشبكات العصبية الالتفافية. على سبيل المثال، يدعي Jarrett وآخرون [11] أن اللاخطية f(x) = |tanh(x)| تعمل بشكل جيد بشكل خاص مع نوعهم من تطبيع التباين متبوعاً بالتجميع المتوسط المحلي على مجموعة بيانات Caltech-101. ومع ذلك، على هذه المجموعة فإن الاهتمام الأساسي هو منع الإفراط في التدريب، لذا فإن التأثير الذي يلاحظونه يختلف عن القدرة المعجلة على ملاءمة مجموعة التدريب التي نبلغ عنها عند استخدام ReLUs. للتعلم الأسرع تأثير كبير على أداء النماذج الكبيرة المدربة على مجموعات بيانات كبيرة.

#### 3.2 التدريب على وحدات معالجة رسومات متعددة

تحتوي وحدة معالجة رسومات GTX 580 واحدة فقط على 3 جيجابايت من الذاكرة، مما يحد من الحجم الأقصى للشبكات التي يمكن تدريبها عليها. اتضح أن 1.2 مليون مثال تدريبي كافية لتدريب شبكات كبيرة جداً بحيث لا تتسع على وحدة معالجة رسومات واحدة. لذلك قمنا بتوزيع الشبكة عبر وحدتي معالجة رسومات. وحدات معالجة الرسومات الحالية مناسبة بشكل خاص للتوازي عبر وحدات معالجة رسومات متعددة، حيث إنها قادرة على القراءة من والكتابة إلى ذاكرة بعضها البعض مباشرة، دون المرور عبر ذاكرة الجهاز المضيف. يضع نظام التوازي الذي نستخدمه بشكل أساسي نصف النوى (أو العصبونات) على كل وحدة معالجة رسومات، مع حيلة إضافية واحدة: تتواصل وحدتا معالجة الرسومات فقط في طبقات معينة. هذا يعني، على سبيل المثال، أن نوى الطبقة 3 تأخذ مدخلات من جميع خرائط النوى في الطبقة 2. ومع ذلك، فإن النوى في الطبقة 4 تأخذ مدخلات فقط من خرائط النوى تلك في الطبقة 3 التي تقع على نفس وحدة معالجة الرسومات. يعد اختيار نمط الاتصال مشكلة للتحقق المتقاطع، ولكن هذا يسمح لنا بضبط كمية الاتصال بدقة حتى تصبح جزءاً مقبولاً من كمية الحساب.

المعمارية الناتجة تشبه إلى حد ما معمارية الشبكة العصبية الالتفافية "العمودية" التي يستخدمها Cireşan وآخرون [5]، باستثناء أن أعمدتنا ليست مستقلة (انظر الشكل 2). يقلل هذا النظام معدلات الخطأ top-1 وtop-5 لدينا بنسبة 1.7% و1.2%، على التوالي، مقارنة بشبكة بها نصف عدد النوى في كل طبقة التفافية مدربة على وحدة معالجة رسومات واحدة. تستغرق شبكة وحدتي معالجة الرسومات وقتاً أقل قليلاً للتدريب من شبكة وحدة معالجة رسومات واحدة.

#### 3.3 تطبيع الاستجابة المحلية

تتميز ReLUs بخاصية مرغوبة وهي أنها لا تتطلب تطبيع المدخلات لمنعها من الإشباع. إذا أنتجت بعض أمثلة التدريب على الأقل مدخلاً موجباً لـ ReLU، فسيحدث التعلم في ذلك العصبون. ومع ذلك، وجدنا أن نظام التطبيع المحلي التالي يساعد في التعميم. بالإشارة إلى a^i_{x,y} نشاط عصبون محسوب بتطبيق النواة i عند الموضع (x، y) ثم تطبيق اللاخطية ReLU، يُعطى نشاط الاستجابة المطبع b^i_{x,y} بالتعبير

$$b^i_{x,y} = a^i_{x,y} / \\left(k + \\alpha \\sum_{j=\\max(0,i-n/2)}^{\\min(N-1,i+n/2)} (a^j_{x,y})^2\\right)^{\\beta}$$

حيث يمتد المجموع على n خرائط نوى "متجاورة" في نفس الموضع المكاني، وN هو العدد الإجمالي للنوى في الطبقة. ترتيب خرائط النوى بالطبع تعسفي ويتم تحديده قبل بدء التدريب. ينفذ هذا النوع من تطبيع الاستجابة شكلاً من أشكال التثبيط الجانبي مستوحى من النوع الموجود في العصبونات الحقيقية، مما يخلق منافسة على الأنشطة الكبيرة بين مخرجات العصبونات المحسوبة باستخدام نوى مختلفة. الثوابت k وn وα وβ هي معاملات فائقة يتم تحديد قيمها باستخدام مجموعة التحقق؛ استخدمنا k = 2 وn = 5 وα = 10^−4 وβ = 0.75. طبقنا هذا التطبيع بعد تطبيق اللاخطية ReLU في طبقات معينة (انظر القسم 3.5).

يحمل هذا النظام بعض التشابه مع نظام تطبيع التباين المحلي لـ Jarrett وآخرون [11]، لكن نظامنا سيكون أكثر صحة أن يطلق عليه "تطبيع السطوع"، لأننا لا نطرح متوسط النشاط. يقلل تطبيع الاستجابة معدلات الخطأ top-1 وtop-5 لدينا بنسبة 1.4% و1.2%، على التوالي. تحققنا أيضاً من فعالية هذا النظام على مجموعة بيانات CIFAR-10: حققت شبكة عصبية التفافية مكونة من أربع طبقات معدل خطأ اختبار بنسبة 13% بدون تطبيع و11% مع التطبيع.

#### 3.4 التجميع المتداخل

تلخص طبقات التجميع في الشبكات العصبية الالتفافية مخرجات مجموعات متجاورة من العصبونات في نفس خريطة النواة. تقليدياً، الأحياء التي تلخصها وحدات التجميع المتجاورة لا تتداخل (على سبيل المثال، [17، 11، 4]). لنكون أكثر دقة، يمكن التفكير في طبقة التجميع على أنها تتكون من شبكة من وحدات التجميع متباعدة s بكسل، كل منها يلخص حياً بحجم z × z متمركز في موقع وحدة التجميع. إذا قمنا بتعيين s = z، نحصل على التجميع المحلي التقليدي كما هو شائع الاستخدام في الشبكات العصبية الالتفافية. إذا قمنا بتعيين s < z، نحصل على التجميع المتداخل. هذا ما نستخدمه في جميع أنحاء شبكتنا، مع s = 2 وz = 3. يقلل هذا النظام معدلات الخطأ top-1 وtop-5 بنسبة 0.4% و0.3%، على التوالي، مقارنة بالنظام غير المتداخل s = 2، z = 2، الذي ينتج مخرجاً بأبعاد مكافئة. نلاحظ عموماً أثناء التدريب أن النماذج ذات التجميع المتداخل تجد صعوبة أكبر قليلاً في الإفراط في التدريب.

#### 3.5 المعمارية الشاملة

الآن نحن مستعدون لوصف المعمارية الشاملة لشبكتنا العصبية الالتفافية. كما هو موضح في الشكل 2، تحتوي الشبكة على ثماني طبقات ذات أوزان؛ الخمس الأولى التفافية والثلاث المتبقية متصلة بالكامل. يتم تغذية مخرج طبقة الاتصال الكامل الأخيرة إلى softmax ذات 1000 مخرج والتي تنتج توزيعاً على 1000 تسمية فئة. تعظم شبكتنا هدف الانحدار اللوجستي متعدد الحدود، وهو ما يعادل تعظيم المتوسط عبر حالات التدريب لاحتمالية اللوغاريتم للتسمية الصحيحة تحت توزيع التنبؤ.

ترتبط نوى الطبقات الالتفافية الثانية والرابعة والخامسة فقط بخرائط النوى تلك في الطبقة السابقة التي تقع على نفس وحدة معالجة الرسومات (انظر الشكل 2). ترتبط نوى الطبقة الالتفافية الثالثة بجميع خرائط النوى في الطبقة الثانية. ترتبط العصبونات في الطبقات المتصلة بالكامل بجميع العصبونات في الطبقة السابقة. تتبع طبقات تطبيع الاستجابة الطبقتين الالتفافيتين الأولى والثانية. تتبع طبقات التجميع الأعظمي، من النوع الموصوف في القسم 3.4، كلاً من طبقات تطبيع الاستجابة وكذلك الطبقة الالتفافية الخامسة. يتم تطبيق اللاخطية ReLU على مخرج كل طبقة التفافية ومتصلة بالكامل.

ترشح الطبقة الالتفافية الأولى صورة المدخل 224 × 224 × 3 بـ 96 نواة بحجم 11 × 11 × 3 بخطوة (stride) قدرها 4 بكسلات (هذه هي المسافة بين مراكز المجالات الحساسة للعصبونات المتجاورة في خريطة النواة). تأخذ الطبقة الالتفافية الثانية كمدخل مخرج (المطبع والمجمع) للطبقة الالتفافية الأولى وترشحه بـ 256 نواة بحجم 5 × 5 × 48. الطبقات الالتفافية الثالثة والرابعة والخامسة متصلة ببعضها البعض دون أي طبقات تجميع أو تطبيع متداخلة. تحتوي الطبقة الالتفافية الثالثة على 384 نواة بحجم 3 × 3 × 256 متصلة بمخرجات (المطبعة، المجمعة) للطبقة الالتفافية الثانية. تحتوي الطبقة الالتفافية الرابعة على 384 نواة بحجم 3 × 3 × 192، والطبقة الالتفافية الخامسة بها 256 نواة بحجم 3 × 3 × 192. تحتوي الطبقات المتصلة بالكامل على 4096 عصبون لكل منها.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2 (multiple times)
- **Key terms introduced:**
  - learned layers (طبقات قابلة للتعلم)
  - saturating nonlinearities (اللاخطيات المشبعة)
  - non-saturating nonlinearity (اللاخطية غير المشبعة)
  - Rectified Linear Units (ReLUs) (وحدات خطية مُصححة)
  - gradient descent (الانحدار التدرجي)
  - cross-GPU parallelization (التوازي عبر وحدات معالجة رسومات متعددة)
  - kernel maps (خرائط النوى)
  - kernel/kernels (نواة/نوى)
  - local normalization (التطبيع المحلي)
  - lateral inhibition (التثبيط الجانبي)
  - hyper-parameters (معاملات فائقة)
  - validation set (مجموعة التحقق)
  - overlapping pooling (التجميع المتداخل)
  - receptive field (المجال الحساس)
  - stride (خطوة)
  - multinomial logistic regression (الانحدار اللوجستي متعدد الحدود)
  - max-pooling (التجميع الأعظمي)
- **Equations:**
  - Response normalization equation (preserved in LaTeX)
  - Activation functions: f(x) = tanh(x), f(x) = (1 + e^−x)^−1, f(x) = max(0, x)
- **Citations:** [4], [5], [11], [17], [20]
- **Special handling:**
  - Mathematical notation preserved exactly
  - GPU model names kept in English (GTX 580)
  - Dataset names kept in English (CIFAR-10, Caltech-101)
  - Figure references maintained
  - Section cross-references maintained (Section 3.4, Section 3.5)
  - Greek letters in equations preserved (α, β)
  - Numerical specifications preserved (96 kernels, 11×11×3, etc.)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.92
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Check

ReLU description back-translated:
Arabic: "نشير إلى العصبونات ذات هذه اللاخطية باسم وحدات خطية مُصححة"
Back to English: "We refer to neurons with this nonlinearity as Rectified Linear Units"
✓ Semantic match confirmed

Architecture description back-translated:
Arabic: "تحتوي الشبكة على ثماني طبقات ذات أوزان؛ الخمس الأولى التفافية والثلاث المتبقية متصلة بالكامل"
Back to English: "The network contains eight layers with weights; the first five are convolutional and the remaining three are fully-connected"
✓ Semantic match confirmed
