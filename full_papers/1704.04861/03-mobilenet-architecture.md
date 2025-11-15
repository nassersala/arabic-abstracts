# Section 3: MobileNet Architecture
## القسم 3: معمارية MobileNet

**Section:** mobilenet-architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** architecture, convolution, neural network, depthwise separable convolutions, hyperparameter, latency, accuracy, batchnorm, ReLU, optimization, gradient, overfitting, regularization

---

### English Version

In this section we first describe the core layers that MobileNet is built on which are depthwise separable filters. We then describe the MobileNet network structure and conclude with descriptions of the two model shrinking hyper-parameters width multiplier and resolution multiplier.

#### 3.1. Depthwise Separable Convolution

The MobileNet model is based on depthwise separable convolutions which is a form of factorized convolutions which factorize a standard convolution into a depthwise convolution and a 1 × 1 convolution called a pointwise convolution. For MobileNets the depthwise convolution applies a single filter to each input channel. The pointwise convolution then applies a 1 × 1 convolution to combine the outputs the depthwise convolution. A standard convolution both filters and combines inputs into a new set of outputs in one step. The depthwise separable convolution splits this into two layers, a separate layer for filtering and a separate layer for combining. This factorization has the effect of drastically reducing computation and model size. Figure 2 shows how a standard convolution 2(a) is factorized into a depthwise convolution 2(b) and a 1 × 1 pointwise convolution 2(c).

A standard convolutional layer takes as input a $D_F \times D_F \times M$ feature map F and produces a $D_F \times D_F \times N$ feature map G where $D_F$ is the spatial width and height of a square input feature map, M is the number of input channels (input depth), $D_G$ is the spatial width and height of a square output feature map and N is the number of output channel (output depth).

The standard convolutional layer is parameterized by convolution kernel K of size $D_K \times D_K \times M \times N$ where $D_K$ is the spatial dimension of the kernel assumed to be square and M is number of input channels and N is the number of output channels as defined previously.

The output feature map for standard convolution assuming stride one and padding is computed as:

$$G_{k,l,n} = \sum_{i,j,m} K_{i,j,m,n} \cdot F_{k+i-1,l+j-1,m} \qquad (1)$$

Standard convolutions have the computational cost of:

$$D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F \qquad (2)$$

where the computational cost depends multiplicatively on the number of input channels M, the number of output channels N the kernel size $D_k \times D_k$ and the feature map size $D_F \times D_F$. MobileNet models address each of these terms and their interactions. First it uses depthwise separable convolutions to break the interaction between the number of output channels and the size of the kernel.

The standard convolution operation has the effect of filtering features based on the convolutional kernels and combining features in order to produce a new representation. The filtering and combination steps can be split into two steps via the use of factorized convolutions called depthwise separable convolutions for substantial reduction in computational cost.

Depthwise separable convolution are made up of two layers: depthwise convolutions and pointwise convolutions. We use depthwise convolutions to apply a single filter per each input channel (input depth). Pointwise convolution, a simple 1×1 convolution, is then used to create a linear combination of the output of the depthwise layer. MobileNets use both batchnorm and ReLU nonlinearities for both layers.

Depthwise convolution with one filter per input channel (input depth) can be written as:

$$\hat{G}_{k,l,m} = \sum_{i,j} \hat{K}_{i,j,m} \cdot F_{k+i-1,l+j-1,m} \qquad (3)$$

where $\hat{K}$ is the depthwise convolutional kernel of size $D_K \times D_K \times M$ where the mth filter in $\hat{K}$ is applied to the mth channel in F to produce the mth channel of the filtered output feature map $\hat{G}$.

Depthwise convolution has a computational cost of:

$$D_K \cdot D_K \cdot M \cdot D_F \cdot D_F \qquad (4)$$

Depthwise convolution is extremely efficient relative to standard convolution. However it only filters input channels, it does not combine them to create new features. So an additional layer that computes a linear combination of the output of depthwise convolution via 1 × 1 convolution is needed in order to generate these new features.

The combination of depthwise convolution and 1 × 1 (pointwise) convolution is called depthwise separable convolution which was originally introduced in [26].

Depthwise separable convolutions cost:

$$D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F \qquad (5)$$

which is the sum of the depthwise and 1 × 1 pointwise convolutions.

By expressing convolution as a two step process of filtering and combining we get a reduction in computation of:

$$\frac{D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F}{D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F} = \frac{1}{N} + \frac{1}{D_K^2}$$

MobileNet uses 3 × 3 depthwise separable convolutions which uses between 8 to 9 times less computation than standard convolutions at only a small reduction in accuracy as seen in Section 4.

Additional factorization in spatial dimension such as in [16, 31] does not save much additional computation as very little computation is spent in depthwise convolutions.

#### 3.2. Network Structure and Training

The MobileNet structure is built on depthwise separable convolutions as mentioned in the previous section except for the first layer which is a full convolution. By defining the network in such simple terms we are able to easily explore network topologies to find a good network. The MobileNet architecture is defined in Table 1. All layers are followed by a batchnorm [13] and ReLU nonlinearity with the exception of the final fully connected layer which has no nonlinearity and feeds into a softmax layer for classification. Figure 3 contrasts a layer with regular convolutions, batchnorm and ReLU nonlinearity to the factorized layer with depthwise convolution, 1 × 1 pointwise convolution as well as batchnorm and ReLU after each convolutional layer. Down sampling is handled with strided convolution in the depthwise convolutions as well as in the first layer. A final average pooling reduces the spatial resolution to 1 before the fully connected layer. Counting depthwise and pointwise convolutions as separate layers, MobileNet has 28 layers.

It is not enough to simply define networks in terms of a small number of Mult-Adds. It is also important to make sure these operations can be efficiently implementable. For instance unstructured sparse matrix operations are not typically faster than dense matrix operations until a very high level of sparsity. Our model structure puts nearly all of the computation into dense 1 × 1 convolutions. This can be implemented with highly optimized general matrix multiply (GEMM) functions. Often convolutions are implemented by a GEMM but require an initial reordering in memory called im2col in order to map it to a GEMM. For instance, this approach is used in the popular Caffe package [15]. 1 × 1 convolutions do not require this reordering in memory and can be implemented directly with GEMM which is one of the most optimized numerical linear algebra algorithms. MobileNet spends 95% of it's computation time in 1 × 1 convolutions which also has 75% of the parameters as can be seen in Table 2. Nearly all of the additional parameters are in the fully connected layer.

MobileNet models were trained in TensorFlow [1] using RMSprop [33] with asynchronous gradient descent similar to Inception V3 [31]. However, contrary to training large models we use less regularization and data augmentation techniques because small models have less trouble with overfitting. When training MobileNets we do not use side heads or label smoothing and additionally reduce the amount image of distortions by limiting the size of small crops that are used in large Inception training [31]. Additionally, we found that it was important to put very little or no weight decay (l2 regularization) on the depthwise filters since their are so few parameters in them. For the ImageNet benchmarks in the next section all models were trained with same training parameters regardless of the size of the model.

#### 3.3. Width Multiplier: Thinner Models

Although the base MobileNet architecture is already small and low latency, many times a specific use case or application may require the model to be smaller and faster. In order to construct these smaller and less computationally expensive models we introduce a very simple parameter α called width multiplier. The role of the width multiplier α is to thin a network uniformly at each layer. For a given layer and width multiplier α, the number of input channels M becomes αM and the number of output channels N becomes αN.

The computational cost of a depthwise separable convolution with width multiplier α is:

$$D_K \cdot D_K \cdot \alpha M \cdot D_F \cdot D_F + \alpha M \cdot \alpha N \cdot D_F \cdot D_F \qquad (6)$$

where $\alpha \in (0, 1]$ with typical settings of 1, 0.75, 0.5 and 0.25. α = 1 is the baseline MobileNet and α < 1 are reduced MobileNets. Width multiplier has the effect of reducing computational cost and the number of parameters quadratically by roughly $\alpha^2$. Width multiplier can be applied to any model structure to define a new smaller model with a reasonable accuracy, latency and size trade off. It is used to define a new reduced structure that needs to be trained from scratch.

#### 3.4. Resolution Multiplier: Reduced Representation

The second hyper-parameter to reduce the computational cost of a neural network is a resolution multiplier ρ. We apply this to the input image and the internal representation of every layer is subsequently reduced by the same multiplier. In practice we implicitly set ρ by setting the input resolution.

We can now express the computational cost for the core layers of our network as depthwise separable convolutions with width multiplier α and resolution multiplier ρ:

$$D_K \cdot D_K \cdot \alpha M \cdot \rho D_F \cdot \rho D_F + \alpha M \cdot \alpha N \cdot \rho D_F \cdot \rho D_F \qquad (7)$$

where $\rho \in (0, 1]$ which is typically set implicitly so that the input resolution of the network is 224, 192, 160 or 128. ρ = 1 is the baseline MobileNet and ρ < 1 are reduced computation MobileNets. Resolution multiplier has the effect of reducing computational cost by $\rho^2$.

As an example we can look at a typical layer in MobileNet and see how depthwise separable convolutions, width multiplier and resolution multiplier reduce the cost and parameters. Table 3 shows the computation and number of parameters for a layer as architecture shrinking methods are sequentially applied to the layer. The first row shows the Mult-Adds and parameters for a full convolutional layer with an input feature map of size 14 × 14 × 512 with a kernel K of size 3 × 3 × 512 × 512. We will look in detail in the next section at the trade offs between resources and accuracy.

---

### النسخة العربية

في هذا القسم نصف أولاً الطبقات الأساسية التي بُنيت عليها MobileNet وهي المرشحات القابلة للفصل حسب العمق. ثم نصف بنية شبكة MobileNet ونختتم بوصف معاملين فائقين لتقليص النموذج هما مضاعف العرض ومضاعف الدقة.

#### 3.1. الالتفاف القابل للفصل حسب العمق

يستند نموذج MobileNet إلى الالتفافات القابلة للفصل حسب العمق وهي شكل من أشكال الالتفافات المحللة التي تحلل الالتفاف القياسي إلى التفاف حسب العمق والتفاف $1 \times 1$ يسمى الالتفاف النقطي. بالنسبة لـ MobileNets، يطبق الالتفاف حسب العمق مرشحاً واحداً على كل قناة إدخال. ثم يطبق الالتفاف النقطي التفاف $1 \times 1$ لدمج مخرجات الالتفاف حسب العمق. يقوم الالتفاف القياسي بترشيح ودمج المدخلات في مجموعة جديدة من المخرجات في خطوة واحدة. يقسم الالتفاف القابل للفصل حسب العمق هذا إلى طبقتين، طبقة منفصلة للترشيح وطبقة منفصلة للدمج. هذا التحليل له تأثير تقليل الحساب وحجم النموذج بشكل كبير. يوضح الشكل 2 كيف يتم تحليل الالتفاف القياسي 2(a) إلى التفاف حسب العمق 2(b) والتفاف نقطي $1 \times 1$ في 2(c).

تأخذ الطبقة الالتفافية القياسية كمدخل خريطة ميزات $D_F \times D_F \times M$ تسمى F وتنتج خريطة ميزات $D_F \times D_F \times N$ تسمى G حيث $D_F$ هو العرض والارتفاع المكاني لخريطة ميزات الإدخال المربعة، وM هو عدد قنوات الإدخال (عمق الإدخال)، و$D_G$ هو العرض والارتفاع المكاني لخريطة ميزات الإخراج المربعة وN هو عدد قنوات الإخراج (عمق الإخراج).

يتم تحديد معاملات الطبقة الالتفافية القياسية بواسطة نواة الالتفاف K بحجم $D_K \times D_K \times M \times N$ حيث $D_K$ هو البعد المكاني للنواة المفترضة أن تكون مربعة وM هو عدد قنوات الإدخال وN هو عدد قنوات الإخراج كما تم تعريفه سابقاً.

يتم حساب خريطة ميزات الإخراج للالتفاف القياسي بافتراض خطوة واحدة وحشو كالتالي:

$$G_{k,l,n} = \sum_{i,j,m} K_{i,j,m,n} \cdot F_{k+i-1,l+j-1,m} \qquad (1)$$

تكون التكلفة الحسابية للالتفافات القياسية:

$$D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F \qquad (2)$$

حيث تعتمد التكلفة الحسابية بشكل ضربي على عدد قنوات الإدخال M، وعدد قنوات الإخراج N، وحجم النواة $D_k \times D_k$، وحجم خريطة الميزات $D_F \times D_F$. تعالج نماذج MobileNet كل من هذه الحدود وتفاعلاتها. أولاً، تستخدم الالتفافات القابلة للفصل حسب العمق لكسر التفاعل بين عدد قنوات الإخراج وحجم النواة.

تتمثل عملية الالتفاف القياسية في ترشيح الميزات بناءً على نوى الالتفاف ودمج الميزات من أجل إنتاج تمثيل جديد. يمكن تقسيم خطوات الترشيح والدمج إلى خطوتين عبر استخدام الالتفافات المحللة المسماة الالتفافات القابلة للفصل حسب العمق لتحقيق تخفيض كبير في التكلفة الحسابية.

تتكون الالتفافات القابلة للفصل حسب العمق من طبقتين: الالتفافات حسب العمق والالتفافات النقطية. نستخدم الالتفافات حسب العمق لتطبيق مرشح واحد لكل قناة إدخال (عمق الإدخال). ثم يُستخدم الالتفاف النقطي، وهو التفاف بسيط $1 \times 1$، لإنشاء تركيبة خطية من مخرجات الطبقة حسب العمق. تستخدم MobileNets كلاً من batchnorm ودوال ReLU اللاخطية لكلتا الطبقتين.

يمكن كتابة الالتفاف حسب العمق مع مرشح واحد لكل قناة إدخال (عمق الإدخال) كالتالي:

$$\hat{G}_{k,l,m} = \sum_{i,j} \hat{K}_{i,j,m} \cdot F_{k+i-1,l+j-1,m} \qquad (3)$$

حيث $\hat{K}$ هي نواة الالتفاف حسب العمق بحجم $D_K \times D_K \times M$ حيث يتم تطبيق المرشح الـ m في $\hat{K}$ على القناة الـ m في F لإنتاج القناة الـ m من خريطة ميزات الإخراج المرشحة $\hat{G}$.

التكلفة الحسابية للالتفاف حسب العمق هي:

$$D_K \cdot D_K \cdot M \cdot D_F \cdot D_F \qquad (4)$$

الالتفاف حسب العمق فعال للغاية بالنسبة للالتفاف القياسي. ومع ذلك، فهو يرشح قنوات الإدخال فقط، ولا يدمجها لإنشاء ميزات جديدة. لذا فإن الحاجة إلى طبقة إضافية تحسب تركيبة خطية من مخرجات الالتفاف حسب العمق عبر التفاف $1 \times 1$ ضرورية لتوليد هذه الميزات الجديدة.

يُسمى الجمع بين الالتفاف حسب العمق والتفاف $1 \times 1$ (النقطي) بالالتفاف القابل للفصل حسب العمق والذي تم تقديمه في الأصل في [26].

تكلفة الالتفافات القابلة للفصل حسب العمق:

$$D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F \qquad (5)$$

وهو مجموع الالتفافات حسب العمق والالتفافات النقطية $1 \times 1$.

من خلال التعبير عن الالتفاف كعملية من خطوتين للترشيح والدمج، نحصل على تخفيض في الحساب قدره:

$$\frac{D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F}{D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F} = \frac{1}{N} + \frac{1}{D_K^2}$$

تستخدم MobileNet التفافات قابلة للفصل حسب العمق بحجم $3 \times 3$ والتي تستخدم ما بين 8 إلى 9 مرات حسابات أقل من الالتفافات القياسية مع انخفاض صغير فقط في الدقة كما هو موضح في القسم 4.

التحليل الإضافي في البعد المكاني كما في [16، 31] لا يوفر الكثير من الحسابات الإضافية حيث يتم إنفاق القليل جداً من الحساب في الالتفافات حسب العمق.

#### 3.2. بنية الشبكة والتدريب

تُبنى بنية MobileNet على الالتفافات القابلة للفصل حسب العمق كما ذُكر في القسم السابق باستثناء الطبقة الأولى وهي التفاف كامل. من خلال تعريف الشبكة بمثل هذه المصطلحات البسيطة، نكون قادرين على استكشاف طوبولوجيات الشبكات بسهولة للعثور على شبكة جيدة. يتم تعريف معمارية MobileNet في الجدول 1. يتبع جميع الطبقات batchnorm [13] ودالة ReLU اللاخطية باستثناء الطبقة المتصلة بالكامل النهائية التي ليس لها دالة لاخطية وتغذي طبقة softmax للتصنيف. يقارن الشكل 3 طبقة مع الالتفافات العادية وbatchnorm ودالة ReLU اللاخطية بالطبقة المحللة مع الالتفاف حسب العمق والتفاف نقطي $1 \times 1$ بالإضافة إلى batchnorm وReLU بعد كل طبقة التفافية. يتم التعامل مع أخذ العينات الهابطة بالتفاف متدرج في الالتفافات حسب العمق وكذلك في الطبقة الأولى. يقلل التجميع المتوسط النهائي الدقة المكانية إلى 1 قبل الطبقة المتصلة بالكامل. بعد عد الالتفافات حسب العمق والالتفافات النقطية كطبقات منفصلة، تحتوي MobileNet على 28 طبقة.

لا يكفي ببساطة تعريف الشبكات من حيث عدد صغير من Mult-Adds. من المهم أيضاً التأكد من أن هذه العمليات يمكن تنفيذها بكفاءة. على سبيل المثال، لا تكون عمليات المصفوفات المتفرقة غير المنظمة عادةً أسرع من عمليات المصفوفات الكثيفة حتى مستوى عالٍ جداً من التفرق. تضع بنية نموذجنا جميع الحسابات تقريباً في التفافات كثيفة $1 \times 1$. يمكن تنفيذ هذا باستخدام دوال ضرب المصفوفات العامة (GEMM) المُحسّنة بشكل كبير. غالباً ما يتم تنفيذ الالتفافات بواسطة GEMM ولكنها تتطلب إعادة ترتيب أولية في الذاكرة تسمى im2col من أجل تعيينها إلى GEMM. على سبيل المثال، يُستخدم هذا النهج في حزمة Caffe الشهيرة [15]. الالتفافات $1 \times 1$ لا تتطلب إعادة الترتيب هذه في الذاكرة ويمكن تنفيذها مباشرة باستخدام GEMM وهي واحدة من أكثر خوارزميات الجبر الخطي العددي تحسيناً. تنفق MobileNet 95% من وقت حسابها في التفافات $1 \times 1$ والتي لديها أيضاً 75% من المعاملات كما يمكن رؤيته في الجدول 2. جميع المعاملات الإضافية تقريباً موجودة في الطبقة المتصلة بالكامل.

تم تدريب نماذج MobileNet في TensorFlow [1] باستخدام RMSprop [33] مع الانحدار التدرجي اللامتزامن بشكل مشابه لـ Inception V3 [31]. ومع ذلك، على عكس تدريب النماذج الكبيرة، نستخدم تقنيات تنظيم وزيادة بيانات أقل لأن النماذج الصغيرة لديها مشكلة أقل مع الإفراط في التجهيز. عند تدريب MobileNets، لا نستخدم الرؤوس الجانبية أو تنعيم التسميات ونقلل أيضاً كمية تشوهات الصور من خلال الحد من حجم القصاصات الصغيرة المستخدمة في تدريب Inception الكبير [31]. بالإضافة إلى ذلك، وجدنا أنه من المهم وضع انحلال وزن قليل جداً أو عدم وضع انحلال وزن (تنظيم l2) على مرشحات العمق لأن هناك عدداً قليلاً جداً من المعاملات فيها. بالنسبة لمعايير ImageNet في القسم التالي، تم تدريب جميع النماذج بنفس معاملات التدريب بغض النظر عن حجم النموذج.

#### 3.3. مضاعف العرض: نماذج أرفع

على الرغم من أن معمارية MobileNet الأساسية صغيرة بالفعل ومنخفضة زمن الاستجابة، إلا أن حالة استخدام أو تطبيق معين قد يتطلب في كثير من الأحيان أن يكون النموذج أصغر وأسرع. من أجل بناء هذه النماذج الأصغر والأقل تكلفة حسابياً، نقدم معاملاً بسيطاً جداً α يسمى مضاعف العرض. دور مضاعف العرض α هو ترقيق الشبكة بشكل موحد في كل طبقة. بالنسبة لطبقة معينة ومضاعف عرض α، يصبح عدد قنوات الإدخال M هو αM ويصبح عدد قنوات الإخراج N هو αN.

التكلفة الحسابية للالتفاف القابل للفصل حسب العمق مع مضاعف العرض α هي:

$$D_K \cdot D_K \cdot \alpha M \cdot D_F \cdot D_F + \alpha M \cdot \alpha N \cdot D_F \cdot D_F \qquad (6)$$

حيث $\alpha \in (0, 1]$ مع إعدادات نموذجية 1، 0.75، 0.5 و0.25. α = 1 هي MobileNet الأساسية وα < 1 هي MobileNets المخفضة. لمضاعف العرض تأثير تقليل التكلفة الحسابية وعدد المعاملات بشكل تربيعي بحوالي $\alpha^2$. يمكن تطبيق مضاعف العرض على أي بنية نموذج لتعريف نموذج أصغر جديد مع توازن معقول بين الدقة وزمن الاستجابة والحجم. يُستخدم لتعريف بنية مخفضة جديدة تحتاج إلى تدريب من الصفر.

#### 3.4. مضاعف الدقة: تمثيل مخفض

المعامل الفائق الثاني لتقليل التكلفة الحسابية للشبكة العصبية هو مضاعف الدقة ρ. نطبق هذا على صورة الإدخال ويتم تقليل التمثيل الداخلي لكل طبقة لاحقاً بنفس المضاعف. في الممارسة، نحدد ρ ضمنياً عن طريق تحديد دقة الإدخال.

يمكننا الآن التعبير عن التكلفة الحسابية للطبقات الأساسية لشبكتنا كالتفافات قابلة للفصل حسب العمق مع مضاعف العرض α ومضاعف الدقة ρ:

$$D_K \cdot D_K \cdot \alpha M \cdot \rho D_F \cdot \rho D_F + \alpha M \cdot \alpha N \cdot \rho D_F \cdot \rho D_F \qquad (7)$$

حيث $\rho \in (0, 1]$ والذي يتم تحديده عادةً ضمنياً بحيث تكون دقة إدخال الشبكة 224، أو 192، أو 160، أو 128. ρ = 1 هي MobileNet الأساسية وρ < 1 هي MobileNets المخفضة الحساب. لمضاعف الدقة تأثير تقليل التكلفة الحسابية بمقدار $\rho^2$.

كمثال، يمكننا النظر إلى طبقة نموذجية في MobileNet ورؤية كيف تقلل الالتفافات القابلة للفصل حسب العمق ومضاعف العرض ومضاعف الدقة التكلفة والمعاملات. يوضح الجدول 3 الحساب وعدد المعاملات لطبقة حيث يتم تطبيق طرق تقليص المعمارية بشكل متسلسل على الطبقة. يُظهر الصف الأول Mult-Adds والمعاملات لطبقة التفافية كاملة مع خريطة ميزات إدخال بحجم 14 × 14 × 512 مع نواة K بحجم 3 × 3 × 512 × 512. سننظر بالتفصيل في القسم التالي إلى المفاضلات بين الموارد والدقة.

---

### Translation Notes

- **Figures referenced:** Figure 2 (a, b, c), Figure 3, Tables 1, 2, 3, 4, 5, 6, 7
- **Key terms introduced:** depthwise separable convolution (الالتفاف القابل للفصل حسب العمق), pointwise convolution (الالتفاف النقطي), width multiplier (مضاعف العرض), resolution multiplier (مضاعف الدقة), GEMM (ضرب المصفوفات العامة), im2col, RMSprop, batchnorm, stride (خطوة), padding (حشو), overfitting (الإفراط في التجهيز)
- **Equations:** 7 equations (1-7)
- **Citations:** [26], [13], [16], [31], [15], [1], [33]
- **Special handling:** Kept mathematical notation in LaTeX format, preserved technical terms like GEMM, im2col, RMSprop, TensorFlow, Caffe, ReLU, softmax in English as standard practice

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
