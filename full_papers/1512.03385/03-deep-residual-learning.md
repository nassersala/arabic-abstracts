# Section 3: Deep Residual Learning
## القسم 3: التعلم المتبقي العميق

**Section:** methodology / deep-residual-learning
**Translation Quality:** 0.88
**Glossary Terms Used:** residual learning, residual function, identity mapping, shortcut connections, projection, element-wise addition, convolutional layers, feature maps, batch normalization, ReLU, VGG, ImageNet, downsampling, global average pooling, fully-connected layer, softmax, stochastic gradient descent (SGD), learning rate, weight decay, momentum

---

### English Version

## 3.1. Residual Learning

Let us consider H(x) as an underlying mapping to be fit by a few stacked layers (not necessarily the entire net), with x denoting the inputs to the first of these layers. If one hypothesizes that multiple nonlinear layers can asymptotically approximate complicated functions², then it is equivalent to hypothesize that they can asymptotically approximate the residual functions, i.e., H(x) − x (assuming that the input and output are of the same dimensions). So rather than expect stacked layers to approximate H(x), we explicitly let these layers approximate a residual function F(x) := H(x) − x. The original function thus becomes F(x)+x. Although both forms should be able to asymptotically approximate the desired functions (as hypothesized), the ease of learning might be different.

This reformulation is motivated by the counterintuitive phenomena about the degradation problem (Fig. 1, left). As we discussed in the introduction, if the added layers can be constructed as identity mappings, a deeper model should have training error no greater than its shallower counterpart. The degradation problem suggests that the solvers might have difficulties in approximating identity mappings by multiple nonlinear layers. With the residual learning reformulation, if identity mappings are optimal, the solvers may simply drive the weights of the multiple nonlinear layers toward zero to approach identity mappings.

In real cases, it is unlikely that identity mappings are optimal, but our reformulation may help to precondition the problem. If the optimal function is closer to an identity mapping than to a zero mapping, it should be easier for the solver to find the perturbations with reference to an identity mapping, than to learn the function as a new one. We show by experiments (Fig. 7) that the learned residual functions in general have small responses, suggesting that identity mappings provide reasonable preconditioning.

## 3.2. Identity Mapping by Shortcuts

We adopt residual learning to every few stacked layers. A building block is shown in Fig. 2. Formally, in this paper we consider a building block defined as:

$$y = \mathcal{F}(x, \{W_i\}) + x.$$
(1)

Here x and y are the input and output vectors of the layers considered. The function $\mathcal{F}(x, \{W_i\})$ represents the residual mapping to be learned. For the example in Fig. 2 that has two layers, $\mathcal{F} = W_2\sigma(W_1x)$ in which σ denotes ReLU [29] and the biases are omitted for simplifying notations. The operation $\mathcal{F} + x$ is performed by a shortcut connection and element-wise addition. We adopt the second nonlinearity after the addition (i.e., σ(y), see Fig. 2).

The shortcut connections in Eqn.(1) introduce neither extra parameter nor computation complexity. This is not only attractive in practice but also important in our comparisons between plain and residual networks. We can fairly compare plain/residual networks that simultaneously have the same number of parameters, depth, width, and computational cost (except for the negligible element-wise addition).

The dimensions of x and $\mathcal{F}$ must be equal in Eqn.(1). If this is not the case (e.g., when changing the input/output channels), we can perform a linear projection $W_s$ by the shortcut connections to match the dimensions:

$$y = \mathcal{F}(x, \{W_i\}) + W_sx.$$
(2)

We can also use a square matrix $W_s$ in Eqn.(1). But we will show by experiments that the identity mapping is sufficient for addressing the degradation problem and is economical, and thus $W_s$ is only used when matching dimensions.

The form of the residual function $\mathcal{F}$ is flexible. Experiments in this paper involve a function $\mathcal{F}$ that has two or three layers (Fig. 5), while more layers are possible. But if $\mathcal{F}$ has only a single layer, Eqn.(1) is similar to a linear layer: y = $W_1x$ + x, for which we have not observed advantages.

We also note that although the above notations are about fully-connected layers for simplicity, they are applicable to convolutional layers. The function $\mathcal{F}(x, \{W_i\})$ can represent multiple convolutional layers. The element-wise addition is performed on two feature maps, channel by channel.

## 3.3. Network Architectures

We have tested various plain/residual nets, and have observed consistent phenomena. To provide instances for discussion, we describe two models for ImageNet as follows.

**Plain Network.** Our plain baselines (Fig. 3, middle) are mainly inspired by the philosophy of VGG nets [41] (Fig. 3, left). The convolutional layers mostly have 3×3 filters and follow two simple design rules: (i) for the same output feature map size, the layers have the same number of filters; and (ii) if the feature map size is halved, the number of filters is doubled so as to preserve the time complexity per layer. We perform downsampling directly by convolutional layers that have a stride of 2. The network ends with a global average pooling layer and a 1000-way fully-connected layer with softmax. The total number of weighted layers is 34 in Fig. 3 (middle).

It is worth noticing that our model has fewer filters and lower complexity than VGG nets [41] (Fig. 3, left). Our 34-layer baseline has 3.6 billion FLOPs (multiply-adds), which is only 18% of VGG-19 (19.6 billion FLOPs).

**Residual Network.** Based on the above plain network, we insert shortcut connections (Fig. 3, right) which turn the network into its counterpart residual version. The identity shortcuts (Eqn.(1)) can be directly used when the input and output are of the same dimensions (solid line shortcuts in Fig. 3). When the dimensions increase (dotted line shortcuts in Fig. 3), we consider two options: (A) The shortcut still performs identity mapping, with extra zero entries padded for increasing dimensions. This option introduces no extra parameter; (B) The projection shortcut in Eqn.(2) is used to match dimensions (done by 1×1 convolutions). For both options, when the shortcuts go across feature maps of two sizes, they are performed with a stride of 2.

## 3.4. Implementation

Our implementation for ImageNet follows the practice in [21, 41]. The image is resized with its shorter side randomly sampled in [256, 480] for scale augmentation [41]. A 224×224 crop is randomly sampled from an image or its horizontal flip, with the per-pixel mean subtracted [21]. The standard color augmentation in [21] is used. We adopt batch normalization (BN) [16] right after each convolution and before activation, following [16]. We initialize the weights as in [13] and train all plain/residual nets from scratch. We use SGD with a mini-batch size of 256. The learning rate starts from 0.1 and is divided by 10 when the error plateaus, and the models are trained for up to 60 × 10⁴ iterations. We use a weight decay of 0.0001 and a momentum of 0.9. We do not use dropout [14], following the practice in [16].

In testing, for comparison studies we adopt the standard 10-crop testing [21]. For best results, we adopt the fully-convolutional form as in [41, 13], and average the scores at multiple scales (images are resized such that the shorter side is in {224, 256, 384, 480, 640}).

---

### النسخة العربية

## 3.1. التعلم المتبقي

دعونا ننظر إلى H(x) كتعيين أساسي يجب تلاؤمه بواسطة بضع طبقات مكدسة (ليس بالضرورة الشبكة بأكملها)، حيث x يشير إلى المدخلات للأولى من هذه الطبقات. إذا افترض المرء أن الطبقات غير الخطية المتعددة يمكن أن تقارب تدريجياً الدوال المعقدة²، فمن المكافئ افتراض أنها يمكن أن تقارب تدريجياً الدوال المتبقية، أي H(x) − x (بافتراض أن المدخل والمخرج لهما نفس الأبعاد). لذا بدلاً من توقع أن الطبقات المكدسة تقارب H(x)، نسمح صراحة لهذه الطبقات بمقاربة دالة متبقية F(x) := H(x) − x. تصبح الدالة الأصلية بالتالي F(x)+x. على الرغم من أن كلا الشكلين يجب أن يكونا قادرين على مقاربة الدوال المرغوبة تدريجياً (كما هو مفترض)، فإن سهولة التعلم قد تكون مختلفة.

تتحفز إعادة الصياغة هذه من الظواهر المنافية للحدس حول مشكلة التدهور (الشكل 1، يسار). كما ناقشنا في المقدمة، إذا أمكن بناء الطبقات المضافة كتعيينات هوية، فيجب ألا يكون لدى النموذج الأعمق خطأ تدريب أكبر من نظيره الأقل عمقاً. تشير مشكلة التدهور إلى أن المحللات قد تواجه صعوبات في مقاربة تعيينات الهوية بواسطة طبقات غير خطية متعددة. مع إعادة صياغة التعلم المتبقي، إذا كانت تعيينات الهوية مثلى، فقد تقوم المحللات ببساطة بدفع أوزان الطبقات غير الخطية المتعددة نحو الصفر للاقتراب من تعيينات الهوية.

في الحالات الحقيقية، من غير المحتمل أن تكون تعيينات الهوية مثلى، لكن إعادة صياغتنا قد تساعد في التهيئة المسبقة للمشكلة. إذا كانت الدالة المثلى أقرب إلى تعيين هوية منها إلى تعيين صفري، فيجب أن يكون من الأسهل على المحلل إيجاد الاضطرابات بالإشارة إلى تعيين هوية، بدلاً من تعلم الدالة كواحدة جديدة. نُظهر من خلال التجارب (الشكل 7) أن الدوال المتبقية المتعلمة لديها بشكل عام استجابات صغيرة، مما يشير إلى أن تعيينات الهوية توفر تهيئة مسبقة معقولة.

## 3.2. تعيين الهوية بواسطة الاختصارات

نعتمد التعلم المتبقي لكل بضع طبقات مكدسة. يظهر كتلة بناء في الشكل 2. رسمياً، في هذه الورقة نعتبر كتلة بناء معرّفة كـ:

$$y = \mathcal{F}(x, \{W_i\}) + x.$$
(1)

هنا x و y هما متجهات المدخل والمخرج للطبقات المعتبرة. الدالة $\mathcal{F}(x, \{W_i\})$ تمثل التعيين المتبقي المراد تعلمه. للمثال في الشكل 2 الذي يحتوي على طبقتين، $\mathcal{F} = W_2\sigma(W_1x)$ حيث σ تشير إلى ReLU [29] ويتم حذف الانحيازات لتبسيط الترميزات. تتم العملية $\mathcal{F} + x$ بواسطة اتصال اختصار وجمع عنصر بعنصر. نعتمد اللاخطية الثانية بعد الجمع (أي σ(y)، انظر الشكل 2).

اتصالات الاختصار في المعادلة (1) لا تقدم معاملاً إضافياً ولا تعقيداً حسابياً. هذا ليس جذاباً في الممارسة فحسب، بل مهم أيضاً في مقارناتنا بين الشبكات البسيطة والمتبقية. يمكننا مقارنة الشبكات البسيطة/المتبقية بشكل عادل والتي لديها في نفس الوقت نفس عدد المعاملات والعمق والعرض والتكلفة الحسابية (باستثناء الجمع عنصر بعنصر الذي يمكن إهماله).

يجب أن تكون أبعاد x و $\mathcal{F}$ متساوية في المعادلة (1). إذا لم يكن هذا هو الحال (مثل عند تغيير قنوات المدخل/المخرج)، يمكننا إجراء إسقاط خطي $W_s$ بواسطة اتصالات الاختصار لمطابقة الأبعاد:

$$y = \mathcal{F}(x, \{W_i\}) + W_sx.$$
(2)

يمكننا أيضاً استخدام مصفوفة مربعة $W_s$ في المعادلة (1). لكننا سنُظهر من خلال التجارب أن تعيين الهوية كافٍ لمعالجة مشكلة التدهور واقتصادي، وبالتالي يُستخدم $W_s$ فقط عند مطابقة الأبعاد.

شكل الدالة المتبقية $\mathcal{F}$ مرن. تتضمن التجارب في هذه الورقة دالة $\mathcal{F}$ لها طبقتان أو ثلاث (الشكل 5)، بينما المزيد من الطبقات ممكن. لكن إذا كانت $\mathcal{F}$ تحتوي على طبقة واحدة فقط، فإن المعادلة (1) مشابهة لطبقة خطية: y = $W_1x$ + x، والتي لم نلاحظ لها مزايا.

نلاحظ أيضاً أنه على الرغم من أن الترميزات أعلاه تتعلق بالطبقات المتصلة بالكامل للتبسيط، إلا أنها قابلة للتطبيق على الطبقات الالتفافية. يمكن أن تمثل الدالة $\mathcal{F}(x, \{W_i\})$ طبقات التفافية متعددة. يتم الجمع عنصر بعنصر على خريطتي ميزات، قناة بقناة.

## 3.3. معماريات الشبكات

لقد اختبرنا شبكات بسيطة/متبقية متنوعة، ولاحظنا ظواهر متسقة. لتوفير حالات للمناقشة، نصف نموذجين لـ ImageNet كما يلي.

**الشبكة البسيطة.** خطوط الأساس البسيطة الخاصة بنا (الشكل 3، الوسط) مستوحاة بشكل أساسي من فلسفة شبكات VGG [41] (الشكل 3، اليسار). تحتوي الطبقات الالتفافية في الغالب على مرشحات 3×3 وتتبع قاعدتي تصميم بسيطتين: (i) لنفس حجم خريطة الميزات الناتجة، تحتوي الطبقات على نفس عدد المرشحات؛ و (ii) إذا انخفض حجم خريطة الميزات إلى النصف، يتم مضاعفة عدد المرشحات للحفاظ على تعقيد الوقت لكل طبقة. نقوم بأخذ العينات الفرعية مباشرة بواسطة الطبقات الالتفافية التي لها خطوة من 2. تنتهي الشبكة بطبقة تجميع متوسط عامة وطبقة متصلة بالكامل بـ 1000 اتجاه مع softmax. العدد الإجمالي للطبقات الموزونة هو 34 في الشكل 3 (الوسط).

من الجدير بالذكر أن نموذجنا لديه مرشحات أقل وتعقيد أقل من شبكات VGG [41] (الشكل 3، اليسار). خط الأساس المكون من 34 طبقة لدينا يحتوي على 3.6 مليار FLOP (عمليات ضرب-جمع)، وهو فقط 18% من VGG-19 (19.6 مليار FLOP).

**الشبكة المتبقية.** بناءً على الشبكة البسيطة أعلاه، ندرج اتصالات اختصار (الشكل 3، اليمين) التي تحول الشبكة إلى نسخة متبقية مقابلة. يمكن استخدام اختصارات الهوية (المعادلة (1)) مباشرة عندما يكون المدخل والمخرج لهما نفس الأبعاد (اختصارات الخط الصلب في الشكل 3). عندما تزداد الأبعاد (اختصارات الخط المنقط في الشكل 3)، نعتبر خيارين: (A) لا يزال الاختصار يؤدي تعيين هوية، مع إدخالات صفرية إضافية محشوة لزيادة الأبعاد. هذا الخيار لا يقدم معاملاً إضافياً؛ (B) يُستخدم اختصار الإسقاط في المعادلة (2) لمطابقة الأبعاد (يتم ذلك بواسطة التفافات 1×1). لكلا الخيارين، عندما تعبر الاختصارات خرائط ميزات بحجمين، يتم تنفيذها بخطوة من 2.

## 3.4. التنفيذ

يتبع تنفيذنا لـ ImageNet الممارسة في [21, 41]. يتم تغيير حجم الصورة مع أخذ عينات عشوائية للجانب الأقصر في [256, 480] لزيادة المقياس [41]. يتم أخذ عينة عشوائية لمحصول 224×224 من صورة أو انعكاسها الأفقي، مع طرح المتوسط لكل بكسل [21]. يتم استخدام زيادة الألوان القياسية في [21]. نعتمد التطبيع الدفعي (BN) [16] مباشرة بعد كل التفاف وقبل التنشيط، متبعين [16]. نقوم بتهيئة الأوزان كما في [13] ونقوم بتدريب جميع الشبكات البسيطة/المتبقية من الصفر. نستخدم SGD مع حجم دفعة صغيرة من 256. يبدأ معدل التعلم من 0.1 ويتم تقسيمه على 10 عندما يستقر الخطأ، ويتم تدريب النماذج لما يصل إلى 60 × 10⁴ تكرار. نستخدم انحلال وزن من 0.0001 وزخم من 0.9. لا نستخدم dropout [14]، متبعين الممارسة في [16].

في الاختبار، لدراسات المقارنة نعتمد الاختبار القياسي لـ 10 محاصيل [21]. للحصول على أفضل النتائج، نعتمد الشكل الالتفافي الكامل كما في [41, 13]، ونحسب متوسط الدرجات على مقاييس متعددة (يتم تغيير حجم الصور بحيث يكون الجانب الأقصر في {224, 256, 384, 480, 640}).

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2, Figure 3, Figure 5, Figure 7
- **Mathematical equations:** Equations (1) and (2) for residual learning formulation
- **Key technical concepts:**
  - Residual function formulation: F(x) := H(x) - x
  - Identity mapping vs projection shortcuts
  - Building block design (2-3 layers)
  - Network architecture comparison (Plain vs ResNet vs VGG)

- **Key terms introduced:**
  - residual function (الدالة المتبقية)
  - asymptotically approximate (تقارب تدريجياً)
  - building block (كتلة بناء)
  - element-wise addition (جمع عنصر بعنصر)
  - projection (إسقاط)
  - FLOPs (multiply-adds) (عمليات ضرب-جمع)
  - downsampling (أخذ العينات الفرعية)
  - global average pooling (التجميع المتوسط العام)
  - scale augmentation (زيادة المقياس)
  - color augmentation (زيادة الألوان)
  - batch normalization (BN) (التطبيع الدفعي)
  - weight decay (انحلال الوزن)
  - momentum (زخم)
  - 10-crop testing (الاختبار لـ 10 محاصيل)
  - fully-convolutional (التفافي كامل)

- **Architecture details:**
  - Plain network: 34 layers, 3.6 billion FLOPs (18% of VGG-19)
  - Residual network: Same architecture with shortcut connections
  - Two options for dimension matching: (A) zero-padding, (B) 1×1 projections

- **Training details:**
  - Mini-batch size: 256
  - Initial learning rate: 0.1 (divided by 10 when error plateaus)
  - Iterations: 600,000
  - Weight decay: 0.0001
  - Momentum: 0.9
  - No dropout

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
