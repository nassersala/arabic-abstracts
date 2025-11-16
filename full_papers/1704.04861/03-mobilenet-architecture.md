# Section 3: MobileNet Architecture
## القسم 3: معمارية MobileNet

**Section:** methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** architecture, depthwise separable convolutions, convolution, neural network, hyperparameter, width multiplier, resolution multiplier, latency, efficient, layer, batch normalization

---

### English Version

In this section we first describe the core layers that MobileNet is built on which are depthwise separable filters. We then describe the MobileNet network structure and conclude with descriptions of the two model shrinking hyper-parameters width multiplier and resolution multiplier.

#### 3.1. Depthwise Separable Convolution

The MobileNet model is based on depthwise separable convolutions which is a form of factorized convolutions which factorize a standard convolution into a depthwise convolution and a 1×1 convolution called a pointwise convolution. For MobileNets the depthwise convolution applies a single filter to each input channel. The pointwise convolution then applies a 1×1 convolution to combine the outputs the depthwise convolution. A standard convolution both filters and combines inputs into a new set of outputs in one step. The depthwise separable convolution splits this into two layers, a separate layer for filtering and a separate layer for combining. This factorization has the effect of drastically reducing computation and model size. Figure 2 shows how a standard convolution 2(a) is factorized into a depthwise convolution 2(b) and a 1×1 pointwise convolution 2(c).

A standard convolutional layer takes as input a D_F × D_F × M feature map F and produces a D_F × D_F × N feature map G where D_F is the spatial width and height of a square input feature map, M is the number of input channels (input depth), D_G is the spatial width and height of a square output feature map and N is the number of output channel (output depth).

The standard convolutional layer is parameterized by convolution kernel K of size D_K × D_K × M × N where D_K is the spatial dimension of the kernel assumed to be square and M is number of input channels and N is the number of output channels as defined previously.

The output feature map for standard convolution assuming stride one and padding is computed as:

$$G_{k,l,n} = \sum_{i,j,m} K_{i,j,m,n} \cdot F_{k+i-1,l+j-1,m}$$

Standard convolutions have the computational cost of:

$$D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F$$

where the computational cost depends multiplicatively on the number of input channels M, the number of output channels N the kernel size D_k × D_k and the feature map size D_F × D_F. MobileNet models address each of these terms and their interactions. First it uses depthwise separable convolutions to break the interaction between the number of output channels and the size of the kernel.

The standard convolution operation has the effect of filtering features based on the convolutional kernels and combining features in order to produce a new representation. The filtering and combination steps can be split into two steps via the use of factorized convolutions called depthwise separable convolutions for substantial reduction in computational cost.

Depthwise separable convolution are made up of two layers: depthwise convolutions and pointwise convolutions. We use depthwise convolutions to apply a single filter per each input channel (input depth). Pointwise convolution, a simple 1×1 convolution, is then used to create a linear combination of the output of the depthwise layer. MobileNets use both batchnorm and ReLU nonlinearities for both layers.

Depthwise convolution with one filter per input channel (input depth) can be written as:

$$\hat{G}_{k,l,m} = \sum_{i,j} \hat{K}_{i,j,m} \cdot F_{k+i-1,l+j-1,m}$$

where $\hat{K}$ is the depthwise convolutional kernel of size D_K × D_K × M where the m-th filter in $\hat{K}$ is applied to the m-th channel in F to produce the m-th channel of the filtered output feature map $\hat{G}$.

Depthwise convolution has a computational cost of:

$$D_K \cdot D_K \cdot M \cdot D_F \cdot D_F$$

Depthwise convolution is extremely efficient relative to standard convolution. However it only filters input channels, it does not combine them to create new features. So an additional layer that computes a linear combination of the output of depthwise convolution via 1×1 convolution is needed in order to generate these new features.

The combination of depthwise convolution and 1×1 (pointwise) convolution is called depthwise separable convolution which was originally introduced in [26].

Depthwise separable convolutions cost:

$$D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F$$

which is the sum of the depthwise and 1×1 pointwise convolutions.

By expressing convolution as a two step process of filtering and combining we get a reduction in computation of:

$$\frac{D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F}{D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F} = \frac{1}{N} + \frac{1}{D_K^2}$$

MobileNet uses 3×3 depthwise separable convolutions which uses between 8 to 9 times less computation than standard convolutions at only a small reduction in accuracy as seen in Section 4.

Additional factorization in spatial dimension such as in [16, 31] does not save much additional computation as very little computation is spent in depthwise convolutions.

#### 3.2. Network Structure and Training

The MobileNet structure is built on depthwise separable convolutions as mentioned in the previous section except for the first layer which is a full convolution. By defining the network in such simple terms we are able to easily explore network topologies to find a good network. The MobileNet architecture is defined in Table 1. All layers are followed by a batchnorm [13] and ReLU nonlinearity with the exception of the final fully connected layer which has no nonlinearity and feeds into a softmax layer for classification. Figure 3 contrasts a layer with regular convolutions, batchnorm and ReLU nonlinearity to the factorized layer with depthwise convolution, 1×1 pointwise convolution as well as batchnorm and ReLU after each convolutional layer. Down sampling is handled with strided convolution in the depthwise convolutions as well as in the first layer. A final average pooling reduces the spatial resolution to 1 before the fully connected layer. Counting depthwise and pointwise convolutions as separate layers, MobileNet has 28 layers.

It is not enough to simply define networks in terms of a small number of Mult-Adds. It is also important to make sure these operations can be efficiently implementable. For instance unstructured sparse matrix operations are not typically faster than dense matrix operations until a very high level of sparsity. Our model structure puts nearly all of the computation into dense 1×1 convolutions. This can be implemented with highly optimized general matrix multiply (GEMM) functions. Often convolutions are implemented by a GEMM but require an initial reordering in memory called im2col in order to map it to a GEMM. For instance, this approach is used in the popular Caffe package [15]. 1×1 convolutions do not require this reordering in memory and can be implemented directly with GEMM which is one of the most optimized numerical linear algebra algorithms. MobileNet spends 95% of it's computation time in 1×1 convolutions which also has 75% of the parameters as can be seen in Table 2. Nearly all of the additional parameters are in the fully connected layer.

MobileNet models were trained in TensorFlow [1] using RMSprop [33] with asynchronous gradient descent similar to Inception V3 [31]. However, contrary to training large models we use less regularization and data augmentation techniques because small models have less trouble with overfitting. When training MobileNets we do not use side heads or label smoothing and additionally reduce the amount image of distortions by limiting the size of small crops that are used in large Inception training [31]. Additionally, we found that it was important to put very little or no weight decay (l2 regularization) on the depthwise filters since their are so few parameters in them. For the ImageNet benchmarks in the next section all models were trained with same training parameters regardless of the size of the model.

#### 3.3. Width Multiplier: Thinner Models

Although the base MobileNet architecture is already small and low latency, many times a specific use case or application may require the model to be smaller and faster. In order to construct these smaller and less computationally expensive models we introduce a very simple parameter α called width multiplier. The role of the width multiplier is to thin a network uniformly at each layer. For a given layer and width multiplier α, the number of input channels M becomes αM and the number of output channels N becomes αN.

The computational cost of a depthwise separable convolution with width multiplier α is:

$$D_K \cdot D_K \cdot \alpha M \cdot D_F \cdot D_F + \alpha M \cdot \alpha N \cdot D_F \cdot D_F$$

where α ∈ (0,1] with typical settings of 1, 0.75, 0.5 and 0.25. α = 1 is the baseline MobileNet and α < 1 are reduced MobileNets. Width multiplier has the effect of reducing computational cost and the number of parameters quadratically by roughly α². Width multiplier can be applied to any model structure to define a new smaller model with a reasonable accuracy, latency and size trade off. It is used to define a new reduced structure that needs to be trained from scratch.

#### 3.4. Resolution Multiplier: Reduced Representation

The second hyper-parameter to reduce the computational cost of a neural network is a resolution multiplier ρ. We apply this to the input image and the internal representation of every layer is subsequently reduced by the same multiplier. In practice we implicitly set ρ by setting the input resolution.

We can now express the computational cost for the core layers of our network as depthwise separable convolutions with width multiplier α and resolution multiplier ρ:

$$D_K \cdot D_K \cdot \alpha M \cdot \rho D_F \cdot \rho D_F + \alpha M \cdot \alpha N \cdot \rho D_F \cdot \rho D_F$$

where ρ ∈ (0,1] which is typically set implicitly so that the input resolution of the network is 224, 192, 160 or 128. ρ = 1 is the baseline MobileNet and ρ < 1 are reduced computation MobileNets. Resolution multiplier has the effect of reducing computational cost by ρ².

As an example we can look at a typical layer in MobileNet and see how depthwise separable convolutions, width multiplier and resolution multiplier reduce the cost and parameters. Table 3 shows the computation and number of parameters for a layer as architecture shrinking methods are sequentially applied to the layer. The first row shows the Mult-Adds and parameters for a full convolutional layer with an input feature map of size 14×14×512 with a kernel K of size 3×3×512×512. We will look in detail in the next section at the trade offs between resources and accuracy.

---

### النسخة العربية

في هذا القسم، نصف أولاً الطبقات الأساسية التي تُبنى عليها MobileNet وهي المرشحات القابلة للفصل حسب العمق. ثم نصف بنية شبكة MobileNet ونختتم بأوصاف المعاملين الفائقين لتقليص النموذج وهما مضاعف العرض ومضاعف دقة الوضوح.

#### 3.1. الالتفاف القابل للفصل حسب العمق

يستند نموذج MobileNet إلى التفافات قابلة للفصل حسب العمق وهي شكل من أشكال التفافات المُحللة التي تُحلل التفافاً قياسياً إلى التفاف حسب العمق والتفاف 1×1 يسمى الالتفاف النقطي. بالنسبة لـ MobileNets، يطبق الالتفاف حسب العمق مرشحاً واحداً على كل قناة إدخال. ثم يطبق الالتفاف النقطي التفاف 1×1 لدمج مخرجات الالتفاف حسب العمق. يقوم الالتفاف القياسي بترشيح ودمج المدخلات في مجموعة جديدة من المخرجات في خطوة واحدة. يقسم الالتفاف القابل للفصل حسب العمق هذا إلى طبقتين، طبقة منفصلة للترشيح وطبقة منفصلة للدمج. هذا التحليل له تأثير تقليل العمليات الحسابية وحجم النموذج بشكل كبير. يوضح الشكل 2 كيف يتم تحليل التفاف قياسي 2(a) إلى التفاف حسب العمق 2(b) والتفاف نقطي 1×1 2(c).

تأخذ طبقة الالتفاف القياسية كمدخل خريطة ميزات F بحجم D_F × D_F × M وتنتج خريطة ميزات G بحجم D_F × D_F × N حيث D_F هو العرض والارتفاع المكاني لخريطة ميزات الإدخال المربعة، وM هو عدد قنوات الإدخال (عمق الإدخال)، وD_G هو العرض والارتفاع المكاني لخريطة ميزات الإخراج المربعة وN هو عدد قنوات الإخراج (عمق الإخراج).

يتم تحديد طبقة الالتفاف القياسية بواسطة نواة التفاف K بحجم D_K × D_K × M × N حيث D_K هو البعد المكاني للنواة المفترض أن يكون مربعاً وM هو عدد قنوات الإدخال وN هو عدد قنوات الإخراج كما هو محدد سابقاً.

يتم حساب خريطة ميزات الإخراج للالتفاف القياسي بافتراض خطوة واحدة وحشو كما يلي:

$$G_{k,l,n} = \sum_{i,j,m} K_{i,j,m,n} \cdot F_{k+i-1,l+j-1,m}$$

التفافات القياسية لها تكلفة حسابية قدرها:

$$D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F$$

حيث تعتمد التكلفة الحسابية بشكل تضاعفي على عدد قنوات الإدخال M، وعدد قنوات الإخراج N، وحجم النواة D_k × D_k، وحجم خريطة الميزات D_F × D_F. تعالج نماذج MobileNet كل واحد من هذه المصطلحات وتفاعلاتها. أولاً، تستخدم التفافات قابلة للفصل حسب العمق لكسر التفاعل بين عدد قنوات الإخراج وحجم النواة.

عملية الالتفاف القياسية لها تأثير ترشيح الميزات بناءً على نوى الالتفاف ودمج الميزات لإنتاج تمثيل جديد. يمكن تقسيم خطوات الترشيح والدمج إلى خطوتين عبر استخدام التفافات مُحللة تسمى التفافات قابلة للفصل حسب العمق لتقليل كبير في التكلفة الحسابية.

تتكون التفافات القابلة للفصل حسب العمق من طبقتين: التفافات حسب العمق والتفافات نقطية. نستخدم التفافات حسب العمق لتطبيق مرشح واحد لكل قناة إدخال (عمق الإدخال). ثم يُستخدم الالتفاف النقطي، وهو التفاف 1×1 بسيط، لإنشاء تركيبة خطية من مخرجات طبقة العمق. تستخدم MobileNets كل من التطبيع الدفعي ودوال التنشيط ReLU لكلتا الطبقتين.

يمكن كتابة الالتفاف حسب العمق بمرشح واحد لكل قناة إدخال (عمق الإدخال) كما يلي:

$$\hat{G}_{k,l,m} = \sum_{i,j} \hat{K}_{i,j,m} \cdot F_{k+i-1,l+j-1,m}$$

حيث $\hat{K}$ هي نواة الالتفاف حسب العمق بحجم D_K × D_K × M حيث المرشح الـ m في $\hat{K}$ يُطبق على القناة الـ m في F لإنتاج القناة الـ m من خريطة ميزات الإخراج المُرشحة $\hat{G}$.

الالتفاف حسب العمق له تكلفة حسابية قدرها:

$$D_K \cdot D_K \cdot M \cdot D_F \cdot D_F$$

الالتفاف حسب العمق فعال للغاية مقارنة بالالتفاف القياسي. ومع ذلك، فهو يرشح قنوات الإدخال فقط، ولا يدمجها لإنشاء ميزات جديدة. لذلك، هناك حاجة إلى طبقة إضافية تحسب تركيبة خطية من مخرجات الالتفاف حسب العمق عبر التفاف 1×1 لتوليد هذه الميزات الجديدة.

يُسمى مزيج الالتفاف حسب العمق والالتفاف 1×1 (النقطي) بالالتفاف القابل للفصل حسب العمق والذي تم تقديمه في الأصل في [26].

تكلفة التفافات القابلة للفصل حسب العمق:

$$D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F$$

وهو مجموع التفافات حسب العمق والالتفافات النقطية 1×1.

من خلال التعبير عن الالتفاف كعملية من خطوتين للترشيح والدمج، نحصل على تقليل في العمليات الحسابية قدره:

$$\frac{D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F}{D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F} = \frac{1}{N} + \frac{1}{D_K^2}$$

تستخدم MobileNet التفافات قابلة للفصل حسب العمق 3×3 والتي تستخدم ما بين 8 إلى 9 مرات أقل من العمليات الحسابية مقارنة بالتفافات القياسية مع تقليل طفيف فقط في الدقة كما هو موضح في القسم 4.

التحليل الإضافي في البعد المكاني كما في [16, 31] لا يوفر الكثير من العمليات الحسابية الإضافية حيث يتم إنفاق القليل جداً من العمليات الحسابية في التفافات حسب العمق.

#### 3.2. بنية الشبكة والتدريب

تُبنى بنية MobileNet على التفافات قابلة للفصل حسب العمق كما ذُكر في القسم السابق باستثناء الطبقة الأولى التي هي التفاف كامل. من خلال تعريف الشبكة بمثل هذه المصطلحات البسيطة، نحن قادرون على استكشاف طوبولوجيات الشبكة بسهولة لإيجاد شبكة جيدة. معمارية MobileNet محددة في الجدول 1. جميع الطبقات متبوعة بالتطبيع الدفعي [13] ودالة التنشيط ReLU باستثناء الطبقة المتصلة بالكامل النهائية التي ليس لها دالة تنشيط وتغذي طبقة softmax للتصنيف. يقارن الشكل 3 طبقة بالتفافات عادية والتطبيع الدفعي ودالة التنشيط ReLU بالطبقة المُحللة مع التفاف حسب العمق والتفاف نقطي 1×1 بالإضافة إلى التطبيع الدفعي وReLU بعد كل طبقة التفاف. يتم التعامل مع أخذ العينات الهابط بالتفاف متدرج في التفافات حسب العمق وكذلك في الطبقة الأولى. يقلل التجميع المتوسط النهائي دقة الوضوح المكانية إلى 1 قبل الطبقة المتصلة بالكامل. عند عد التفافات حسب العمق والنقطية كطبقات منفصلة، فإن MobileNet لديها 28 طبقة.

ليس كافياً مجرد تعريف الشبكات من حيث عدد صغير من Mult-Adds. من المهم أيضاً التأكد من أن هذه العمليات يمكن تنفيذها بكفاءة. على سبيل المثال، عمليات المصفوفات المتناثرة غير المنظمة ليست عادةً أسرع من عمليات المصفوفات الكثيفة حتى مستوى عالٍ جداً من التناثر. تضع بنية نموذجنا تقريباً كل العمليات الحسابية في التفافات كثيفة 1×1. يمكن تنفيذ هذا بدوال ضرب المصفوفات العامة المُحسّنة للغاية (GEMM). غالباً ما يتم تنفيذ التفافات بواسطة GEMM ولكنها تتطلب إعادة ترتيب أولية في الذاكرة تسمى im2col لتعيينها إلى GEMM. على سبيل المثال، يُستخدم هذا النهج في حزمة Caffe الشائعة [15]. التفافات 1×1 لا تتطلب إعادة الترتيب هذه في الذاكرة ويمكن تنفيذها مباشرة باستخدام GEMM وهي واحدة من خوارزميات الجبر الخطي العددي الأكثر تحسيناً. تقضي MobileNet 95% من وقت الحوسبة في التفافات 1×1 والتي تحتوي أيضاً على 75% من المعاملات كما يمكن رؤيته في الجدول 2. تقريباً جميع المعاملات الإضافية موجودة في الطبقة المتصلة بالكامل.

تم تدريب نماذج MobileNet في TensorFlow [1] باستخدام RMSprop [33] مع الانحدار التدرجي غير المتزامن مشابهاً لـ Inception V3 [31]. ومع ذلك، على عكس تدريب النماذج الكبيرة، نستخدم تقنيات تنظيم وتكبير البيانات أقل لأن النماذج الصغيرة لديها مشكلة أقل مع الإفراط في التناسب. عند تدريب MobileNets، لا نستخدم الرؤوس الجانبية أو تنعيم التسميات ونقلل أيضاً كمية تشوهات الصور عن طريق الحد من حجم القصاصات الصغيرة المستخدمة في تدريب Inception الكبير [31]. بالإضافة إلى ذلك، وجدنا أنه من المهم وضع القليل جداً أو عدم وضع تضاؤل الأوزان (تنظيم l2) على مرشحات حسب العمق حيث يوجد عدد قليل جداً من المعاملات فيها. بالنسبة لمعايير ImageNet في القسم التالي، تم تدريب جميع النماذج بنفس معاملات التدريب بغض النظر عن حجم النموذج.

#### 3.3. مضاعف العرض: نماذج أنحف

على الرغم من أن معمارية MobileNet الأساسية صغيرة بالفعل وذات زمن استجابة منخفض، في كثير من الأحيان قد تتطلب حالة استخدام أو تطبيق معين أن يكون النموذج أصغر وأسرع. لبناء هذه النماذج الأصغر والأقل تكلفة حسابياً، نقدم معاملاً بسيطاً جداً α يسمى مضاعف العرض. دور مضاعف العرض هو ترقيق الشبكة بشكل موحد في كل طبقة. لطبقة معينة ومضاعف عرض α، يصبح عدد قنوات الإدخال M هو αM ويصبح عدد قنوات الإخراج N هو αN.

التكلفة الحسابية للالتفاف القابل للفصل حسب العمق مع مضاعف العرض α هي:

$$D_K \cdot D_K \cdot \alpha M \cdot D_F \cdot D_F + \alpha M \cdot \alpha N \cdot D_F \cdot D_F$$

حيث α ∈ (0,1] مع إعدادات نموذجية 1، 0.75، 0.5 و 0.25. α = 1 هو MobileNet الأساسي و α < 1 هي MobileNets مخفضة. لمضاعف العرض تأثير تقليل التكلفة الحسابية وعدد المعاملات بشكل تربيعي بحوالي α². يمكن تطبيق مضاعف العرض على أي بنية نموذج لتعريف نموذج أصغر جديد مع مقايضة معقولة بين الدقة وزمن الاستجابة والحجم. يُستخدم لتعريف بنية مخفضة جديدة تحتاج إلى التدريب من الصفر.

#### 3.4. مضاعف دقة الوضوح: تمثيل مخفض

المعامل الفائق الثاني لتقليل التكلفة الحسابية للشبكة العصبية هو مضاعف دقة الوضوح ρ. نطبق هذا على صورة الإدخال ويتم تقليل التمثيل الداخلي لكل طبقة لاحقاً بنفس المضاعف. في الممارسة العملية، نحدد ρ بشكل ضمني عن طريق تحديد دقة وضوح الإدخال.

يمكننا الآن التعبير عن التكلفة الحسابية للطبقات الأساسية لشبكتنا كالتفافات قابلة للفصل حسب العمق مع مضاعف العرض α ومضاعف دقة الوضوح ρ:

$$D_K \cdot D_K \cdot \alpha M \cdot \rho D_F \cdot \rho D_F + \alpha M \cdot \alpha N \cdot \rho D_F \cdot \rho D_F$$

حيث ρ ∈ (0,1] والذي يتم تعيينه عادةً بشكل ضمني بحيث تكون دقة وضوح الإدخال للشبكة 224، 192، 160 أو 128. ρ = 1 هو MobileNet الأساسي و ρ < 1 هي MobileNets مخفضة العمليات الحسابية. لمضاعف دقة الوضوح تأثير تقليل التكلفة الحسابية بمقدار ρ².

كمثال، يمكننا النظر إلى طبقة نموذجية في MobileNet ونرى كيف تقلل التفافات القابلة للفصل حسب العمق ومضاعف العرض ومضاعف دقة الوضوح التكلفة والمعاملات. يوضح الجدول 3 العمليات الحسابية وعدد المعاملات لطبقة مع تطبيق طرق تقليص المعمارية بشكل تسلسلي على الطبقة. يوضح الصف الأول Mult-Adds والمعاملات لطبقة التفاف كاملة مع خريطة ميزات إدخال بحجم 14×14×512 مع نواة K بحجم 3×3×512×512. سننظر بالتفصيل في القسم التالي إلى المفاضلات بين الموارد والدقة.

---

### Translation Notes

- **Figures referenced:** Figure 2 (depthwise separable convolution visualization), Figure 3 (layer comparison), Table 1 (MobileNet architecture), Table 2 (resource per layer type), Table 3 (resource usage modifications)
- **Key terms introduced:** depthwise separable convolution, pointwise convolution, factorized convolutions, feature map, kernel, stride, padding, width multiplier, resolution multiplier, batchnorm, ReLU, GEMM, im2col, RMSprop, overfitting, softmax
- **Equations:** 7 major equations describing computational costs and convolution operations
- **Citations:** [26], [13], [16, 31], [15], [1], [33]
- **Special handling:**
  - Mathematical equations preserved in LaTeX format
  - "depthwise separable convolutions" = "التفافات قابلة للفصل حسب العمق"
  - "pointwise convolution" = "الالتفاف النقطي"
  - "width multiplier" = "مضاعف العرض"
  - "resolution multiplier" = "مضاعف دقة الوضوح"
  - "feature map" = "خريطة ميزات"
  - "batch normalization" = "التطبيع الدفعي"
  - Technical terms GEMM, im2col, RMSprop, TensorFlow, Caffe kept in English
  - Greek letters α and ρ preserved in equations

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
