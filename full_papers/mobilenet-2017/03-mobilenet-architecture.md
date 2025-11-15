# Section 3: MobileNet Architecture
## القسم 3: معمارية MobileNet

**Section:** architecture
**Translation Quality:** 0.86
**Glossary Terms Used:** architecture, depthwise separable convolution, convolutional neural network, hyperparameter, computational cost, latency, efficient, feature map, convolution kernel

---

### English Version

**Section Introduction:**

In this section we first describe the core layers that MobileNet is built on which are depthwise separable filters. We then describe the MobileNet network structure and conclude with descriptions of the two model shrinking hyper-parameters width multiplier and resolution multiplier.

#### 3.1 Depthwise Separable Convolution

The MobileNet model is based on depthwise separable convolutions which is a form of factorized convolutions which factorize a standard convolution into a depthwise convolution and a $1\times 1$ convolution called a pointwise convolution. For MobileNets the depthwise convolution applies a single filter to each input channel. The pointwise convolution then applies a $1\times 1$ convolution to combine the outputs the depthwise convolution. A standard convolution both filters and combines inputs into a new set of outputs in one step. The depthwise separable convolution splits this into two layers, a separate layer for filtering and a separate layer for combining. This factorization has the effect of drastically reducing computation and model size. Figure 2 shows how a standard convolution (2a) is factorized into a depthwise convolution (2b) and a $1\times 1$ pointwise convolution (2c).

A standard convolutional layer takes as input a $D_{F}\times D_{F}\times M$ feature map $\mathbf{F}$ and produces a $D_{F}\times D_{F}\times N$ feature map $\mathbf{G}$ where $D_{F}$ is the spatial width and height of a square input feature map, $M$ is the number of input channels (input depth), $D_{G}$ is the spatial width and height of a square output feature map and $N$ is the number of output channel (output depth).

The standard convolutional layer is parameterized by convolution kernel $\mathbf{K}$ of size $D_{K}\times D_{K}\times M\times N$ where $D_{K}$ is the spatial dimension of the kernel assumed to be square and $M$ is number of input channels and $N$ is the number of output channels as defined previously.

Standard convolutions have the computational cost of:

$$D_{K} \cdot D_{K} \cdot M \cdot N \cdot D_{F} \cdot D_{F}$$

Depthwise separable convolutions are made up of two layers: depthwise convolutions and pointwise convolutions. Depthwise convolution with one filter per input channel can be written as:

$$\hat{G}_{k,l,m} = \sum_{i,j} \hat{K}_{i,j,m} \cdot F_{k+i-1,l+j-1,m}$$

Depthwise convolution has a computational cost of:

$$D_{K} \cdot D_{K} \cdot M \cdot D_{F} \cdot D_{F}$$

The depthwise separable convolution reduces computation compared to standard convolutions by a factor of:

$$\frac{D_{K} \cdot D_{K} \cdot M \cdot D_{F} \cdot D_{F} + M \cdot N \cdot D_{F} \cdot D_{F}}{D_{K} \cdot D_{K} \cdot M \cdot N \cdot D_{F} \cdot D_{F}} = \frac{1}{N} + \frac{1}{D_{K}^2}$$

MobileNet uses $3 \times 3$ depthwise separable convolutions which uses between 8 to 9 times less computation than standard convolutions at only a small reduction in accuracy.

#### 3.2 Network Structure and Training

The MobileNet structure is built on depthwise separable convolutions except for the first layer which is a full convolution. All layers are followed by a batchnorm and ReLU nonlinearity with the exception of the final fully connected layer which has no nonlinearity and feeds into a softmax layer for classification. Figure 3 contrasts a layer with regular convolutions, batchnorm and ReLU nonlinearity to the factorized layer with depthwise convolution, $1 \times 1$ pointwise convolution as well as batchnorm and ReLU after each convolutional layer. Down sampling is handled with strided convolution in the depthwise convolutions as well as in the first layer. A final average pooling reduces the spatial resolution to 1 before the fully connected layer. Counting depthwise and pointwise convolutions as separate layers, MobileNet has 28 layers.

#### 3.3 Width Multiplier: Thinner Models

The role of the width multiplier $\alpha$ is to thin a network uniformly at each layer. For a given layer and width multiplier $\alpha$, the number of input channels $M$ becomes $\alpha M$ and the number of output channels $N$ becomes $\alpha N$. The computational cost of a depthwise separable convolution with width multiplier $\alpha$ becomes:

$$D_{K} \cdot D_{K} \cdot \alpha M \cdot D_{F} \cdot D_{F} + \alpha M \cdot \alpha N \cdot D_{F} \cdot D_{F}$$

where $\alpha \in (0,1]$ with typical settings of 1, 0.75, 0.5 and 0.25. Width multiplier has the effect of reducing computational cost and the number of parameters quadratically by roughly $\alpha^2$.

#### 3.4 Resolution Multiplier: Reduced Representation

The second hyper-parameter to reduce the computational cost of a neural network is a resolution multiplier $\rho$. This is applied to the input image and the internal representation of every layer is subsequently reduced by the same multiplier. The computational cost for the core layers of our network with width multiplier $\alpha$ and resolution multiplier $\rho$ is:

$$D_{K} \cdot D_{K} \cdot \alpha M \cdot \rho D_{F} \cdot \rho D_{F} + \alpha M \cdot \alpha N \cdot \rho D_{F} \cdot \rho D_{F}$$

where $\rho \in (0,1]$ which is typically set implicitly so that the input resolution of the network is 224, 192, 160 or 128. Resolution multiplier has the effect of reducing computational cost by $\rho^2$.

---

### النسخة العربية

**مقدمة القسم:**

في هذا القسم، نصف أولاً الطبقات الأساسية التي تُبنى عليها MobileNet وهي المرشحات القابلة للفصل حسب العمق. ثم نصف بنية شبكة MobileNet ونختتم بأوصاف لمعاملين فائقين لتقليص النموذج هما مضاعف العرض ومضاعف الدقة.

#### 3.1 الالتفافات القابلة للفصل حسب العمق

يستند نموذج MobileNet إلى التفافات قابلة للفصل حسب العمق وهي شكل من أشكال التفافات المحللة التي تحلل التفافاً قياسياً إلى التفاف حسب العمق والتفاف $1\times 1$ يسمى الالتفاف النقطي. بالنسبة لـ MobileNets، يطبق الالتفاف حسب العمق مرشحاً واحداً على كل قناة إدخال. ثم يطبق الالتفاف النقطي التفافاً $1\times 1$ لدمج مخرجات الالتفاف حسب العمق. يقوم الالتفاف القياسي بترشيح ودمج المدخلات في مجموعة جديدة من المخرجات في خطوة واحدة. يقسم الالتفاف القابل للفصل حسب العمق هذا إلى طبقتين، طبقة منفصلة للترشيح وطبقة منفصلة للدمج. لهذا التحليل تأثير في تقليل الحساب وحجم النموذج بشكل كبير. يوضح الشكل 2 كيف يتم تحليل الالتفاف القياسي (2أ) إلى التفاف حسب العمق (2ب) والتفاف نقطي $1\times 1$ (2ج).

تأخذ الطبقة الالتفافية القياسية كمدخل خريطة ميزات $D_{F}\times D_{F}\times M$ تُرمز بـ $\mathbf{F}$ وتنتج خريطة ميزات $D_{F}\times D_{F}\times N$ تُرمز بـ $\mathbf{G}$ حيث $D_{F}$ هو العرض والارتفاع المكاني لخريطة ميزات الإدخال المربعة، و $M$ هو عدد قنوات الإدخال (عمق الإدخال)، و $D_{G}$ هو العرض والارتفاع المكاني لخريطة ميزات الإخراج المربعة و $N$ هو عدد قنوات الإخراج (عمق الإخراج).

تتحدد معاملات الطبقة الالتفافية القياسية بنواة الالتفاف $\mathbf{K}$ ذات الحجم $D_{K}\times D_{K}\times M\times N$ حيث $D_{K}$ هو البعد المكاني للنواة المفترض أن يكون مربعاً و $M$ هو عدد قنوات الإدخال و $N$ هو عدد قنوات الإخراج كما تم تعريفه سابقاً.

التفافات القياسية لها تكلفة حسابية قدرها:

$$D_{K} \cdot D_{K} \cdot M \cdot N \cdot D_{F} \cdot D_{F}$$

تتكون الالتفافات القابلة للفصل حسب العمق من طبقتين: التفافات حسب العمق والتفافات نقطية. يمكن كتابة الالتفاف حسب العمق مع مرشح واحد لكل قناة إدخال كما يلي:

$$\hat{G}_{k,l,m} = \sum_{i,j} \hat{K}_{i,j,m} \cdot F_{k+i-1,l+j-1,m}$$

للالتفاف حسب العمق تكلفة حسابية قدرها:

$$D_{K} \cdot D_{K} \cdot M \cdot D_{F} \cdot D_{F}$$

يقلل الالتفاف القابل للفصل حسب العمق الحساب مقارنة بالتفافات القياسية بمعامل:

$$\frac{D_{K} \cdot D_{K} \cdot M \cdot D_{F} \cdot D_{F} + M \cdot N \cdot D_{F} \cdot D_{F}}{D_{K} \cdot D_{K} \cdot M \cdot N \cdot D_{F} \cdot D_{F}} = \frac{1}{N} + \frac{1}{D_{K}^2}$$

تستخدم MobileNet التفافات قابلة للفصل حسب العمق بحجم $3 \times 3$ والتي تستخدم ما بين 8 إلى 9 مرات حسابات أقل من الالتفافات القياسية مع انخفاض طفيف فقط في الدقة.

#### 3.2 بنية الشبكة والتدريب

تُبنى بنية MobileNet على التفافات قابلة للفصل حسب العمق باستثناء الطبقة الأولى التي هي التفاف كامل. يتبع جميع الطبقات تطبيع دفعي (batchnorm) ولاخطية ReLU باستثناء الطبقة المتصلة بالكامل النهائية التي ليس لها لاخطية وتغذي طبقة softmax للتصنيف. يقارن الشكل 3 طبقة ذات التفافات منتظمة وتطبيع دفعي ولاخطية ReLU بالطبقة المحللة ذات الالتفاف حسب العمق والتفاف نقطي $1 \times 1$ بالإضافة إلى تطبيع دفعي و ReLU بعد كل طبقة التفافية. يتم التعامل مع أخذ العينات الهابط بالتفاف ذي خطوة في الالتفافات حسب العمق وكذلك في الطبقة الأولى. يقلل التجميع المتوسط النهائي الدقة المكانية إلى 1 قبل الطبقة المتصلة بالكامل. بعد حساب التفافات حسب العمق والالتفافات النقطية كطبقات منفصلة، تحتوي MobileNet على 28 طبقة.

#### 3.3 مضاعف العرض: نماذج أنحف

دور مضاعف العرض $\alpha$ هو ترقيق الشبكة بشكل موحد في كل طبقة. لطبقة معينة ومضاعف عرض $\alpha$، يصبح عدد قنوات الإدخال $M$ يساوي $\alpha M$ ويصبح عدد قنوات الإخراج $N$ يساوي $\alpha N$. تصبح التكلفة الحسابية للالتفاف القابل للفصل حسب العمق مع مضاعف العرض $\alpha$:

$$D_{K} \cdot D_{K} \cdot \alpha M \cdot D_{F} \cdot D_{F} + \alpha M \cdot \alpha N \cdot D_{F} \cdot D_{F}$$

حيث $\alpha \in (0,1]$ مع إعدادات نموذجية من 1، 0.75، 0.5 و 0.25. لمضاعف العرض تأثير في تقليل التكلفة الحسابية وعدد المعاملات بشكل تربيعي بحوالي $\alpha^2$.

#### 3.4 مضاعف الدقة: تمثيل مختزل

المعامل الفائق الثاني لتقليل التكلفة الحسابية للشبكة العصبية هو مضاعف الدقة $\rho$. يُطبق هذا على صورة الإدخال ويُقلل التمثيل الداخلي لكل طبقة لاحقاً بنفس المضاعف. التكلفة الحسابية للطبقات الأساسية لشبكتنا مع مضاعف العرض $\alpha$ ومضاعف الدقة $\rho$ هي:

$$D_{K} \cdot D_{K} \cdot \alpha M \cdot \rho D_{F} \cdot \rho D_{F} + \alpha M \cdot \alpha N \cdot \rho D_{F} \cdot \rho D_{F}$$

حيث $\rho \in (0,1]$ والذي يتم تعيينه عادةً بشكل ضمني بحيث تكون دقة إدخال الشبكة 224، 192، 160 أو 128. لمضاعف الدقة تأثير في تقليل التكلفة الحسابية بمقدار $\rho^2$.

---

### Translation Notes

- **Figures referenced:** Figure 2 (depthwise separable convolution visualization), Figure 3 (network structure comparison)
- **Key terms introduced:**
  - Depthwise separable convolution (الالتفاف القابل للفصل حسب العمق)
  - Pointwise convolution (الالتفاف النقطي)
  - Width multiplier (مضاعف العرض)
  - Resolution multiplier (مضاعف الدقة)
  - Batchnorm (تطبيع دفعي)
- **Equations:** Multiple equations for computational cost analysis preserved in LaTeX
- **Citations:** None in this section
- **Special handling:**
  - All mathematical notation preserved exactly
  - Greek letters (α, ρ) kept in original form
  - Subscripts and mathematical symbols maintained
  - Technical architecture terms translated consistently

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- Mathematical notation preservation: 0.95
- **Overall section score:** 0.86

### Back-Translation Check

The Arabic translation accurately conveys that MobileNet is built on depthwise separable convolutions, which factorize standard convolutions into depthwise and pointwise ($1\times 1$) convolutions. This reduces computation by 8-9x with minimal accuracy loss. The network has 28 layers with batchnorm and ReLU after each layer. Two hyperparameters are introduced: width multiplier $\alpha$ (reduces channels, cost scales as $\alpha^2$) and resolution multiplier $\rho$ (reduces spatial dimensions, cost scales as $\rho^2$). Typical values are $\alpha \in \{1, 0.75, 0.5, 0.25\}$ and input resolutions of 224, 192, 160, or 128 pixels.
