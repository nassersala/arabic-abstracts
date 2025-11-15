# Section 3: DenseNets
## القسم 3: شبكات DenseNet

**Section:** DenseNets (Methodology)
**Translation Quality:** 0.89
**Glossary Terms Used:** convolutional network (شبكة تلافيفية), layers (طبقات), non-linear transformation (تحويل غير خطي), Batch Normalization (التطبيع الدفعي), ReLU (وحدة خطية مصححة), convolution (التفاف), pooling (تجميع), feature-maps (خرائط الميزات), ResNets (شبكات ResNet), identity function (دالة الهوية), gradient (تدرج), concatenation (ربط), dense connectivity (اتصال كثيف), composite function (دالة مركبة), down-sampling (تقليل العينات), dense blocks (كتل كثيفة), transition layers (طبقات انتقالية), growth rate (معدل النمو), bottleneck layers (طبقات عنق الزجاجة), compression (ضغط), global average pooling (تجميع متوسط شامل), softmax (softmax)

---

### English Version

Consider a single image x₀ that is passed through a convolutional network. The network comprises L layers, each of which implements a non-linear transformation Hₗ(·), where ℓ indexes the layer. Hₗ(·) can be a composite function of operations such as Batch Normalization (BN) [14], rectified linear units (ReLU) [6], Pooling [19], or Convolution (Conv). We denote the output of the ℓth layer as xₗ.

**ResNets.** Traditional convolutional feed-forward networks connect the output of the ℓth layer as input to the (ℓ+1)th layer [16], which gives rise to the following layer transition: xₗ = Hₗ(xₗ₋₁). ResNets [11] add a skip-connection that bypasses the non-linear transformations with an identity function:

xₗ = Hₗ(xₗ₋₁) + xₗ₋₁    (1)

An advantage of ResNets is that the gradient can flow directly through the identity function from later layers to the earlier layers. However, the identity function and the output of Hₗ are combined by summation, which may impede the information flow in the network.

**Dense connectivity.** To further improve the information flow between layers we propose a different connectivity pattern: we introduce direct connections from any layer to all subsequent layers. Figure 1 illustrates the layout of the resulting DenseNet schematically. Consequently, the ℓth layer receives the feature-maps of all preceding layers, x₀, ..., xₗ₋₁, as input:

xₗ = Hₗ([x₀, x₁, ..., xₗ₋₁])    (2)

where [x₀, x₁, ..., xₗ₋₁] refers to the concatenation of the feature-maps produced in layers 0, ..., ℓ−1. Because of its dense connectivity we refer to this network architecture as Dense Convolutional Network (DenseNet). For ease of implementation, we concatenate the multiple inputs of Hₗ(·) in eq. (2) into a single tensor.

**Composite function.** Motivated by [12], we define Hₗ(·) as a composite function of three consecutive operations: batch normalization (BN) [14], followed by a rectified linear unit (ReLU) [6] and a 3×3 convolution (Conv).

**Pooling layers.** The concatenation operation used in Eq. (2) is not viable when the size of feature-maps changes. However, an essential part of convolutional networks is down-sampling layers that change the size of feature-maps. To facilitate down-sampling in our architecture we divide the network into multiple densely connected dense blocks; see Figure 2. We refer to layers between blocks as transition layers, which do convolution and pooling. The transition layers used in our experiments consist of a batch normalization layer and an 1×1 convolutional layer followed by a 2×2 average pooling layer.

**Growth rate.** If each function Hₗ produces k feature-maps, it follows that the ℓth layer has k₀ + k × (ℓ−1) input feature-maps, where k₀ is the number of channels in the input layer. An important difference between DenseNet and existing network architectures is that DenseNet can have very narrow layers, e.g., k = 12. We refer to the hyperparameter k as the growth rate of the network. We show in Section 4 that a relatively small growth rate is sufficient to obtain state-of-the-art results on the datasets that we tested on. One explanation for this is that each layer has access to all the preceding feature-maps in its block and, therefore, to the network's "collective knowledge". One can view the feature-maps as the global state of the network. Each layer adds k feature-maps of its own to this state. The growth rate regulates how much new information each layer contributes to the global state. The global state, once written, can be accessed from everywhere within the network and, unlike in traditional network architectures, there is no need to replicate it from layer to layer.

**Bottleneck layers.** Although each layer only produces k output feature-maps, it typically has many more inputs. It has been noted in [37, 11] that a 1×1 convolution can be introduced as bottleneck layer before each 3×3 convolution to reduce the number of input feature-maps, and thus to improve computational efficiency. We find this design especially effective for DenseNet and we refer to our network with such a bottleneck layer, i.e., to the BN-ReLU-Conv(1×1)-BN-ReLU-Conv(3×3) version of Hₗ, as DenseNet-B. In our experiments, we let each 1×1 convolution produce 4k feature-maps.

**Compression.** To further improve model compactness, we can reduce the number of feature-maps at transition layers. If a dense block contains m feature-maps, we let the following transition layer generate ⌊θm⌋ output feature-maps, where 0 < θ ≤ 1 is referred to as the compression factor. When θ = 1, the number of feature-maps across transition layers remains unchanged. We refer the DenseNet with θ < 1 as DenseNet-C, and we set θ = 0.5 in our experiment. When both the bottleneck and transition layers with θ < 1 are used, we refer to our model as DenseNet-BC.

**Implementation Details.** On all datasets except ImageNet, the DenseNet used in our experiments has three dense blocks that each has an equal number of layers. Before entering the first dense block, a convolution with 16 (or twice the growth rate for DenseNet-BC) output channels is performed on the input images. For convolutional layers with kernel size 3×3, each side of the inputs is zero-padded by one pixel to keep the feature-map size fixed. We use 1×1 convolution followed by 2×2 average pooling as transition layers between two contiguous dense blocks. At the end of the last dense block, a global average pooling is performed and then a softmax classifier is attached. The feature-map sizes in the three dense blocks are 32×32, 16×16, and 8×8, respectively. We experiment with the basic DenseNet structure with configurations {L=40, k=12}, {L=100, k=12} and {L=100, k=24}. For DenseNet-BC, the networks with configurations {L=100, k=12}, {L=250, k=24} and {L=190, k=40} are evaluated.

In our experiments on ImageNet, we use a DenseNet-BC structure with 4 dense blocks on 224×224 input images. The initial convolution layer comprises 2k convolutions of size 7×7 with stride 2; the number of feature-maps in all other layers also follow from setting k. The exact network configurations we used on ImageNet are shown in Table 1.

---

### النسخة العربية

لننظر في صورة واحدة x₀ يتم تمريرها عبر شبكة تلافيفية. تتكون الشبكة من L طبقة، كل منها تنفذ تحويلاً غير خطي Hₗ(·)، حيث ℓ هو مؤشر الطبقة. يمكن أن يكون Hₗ(·) دالة مركبة من عمليات مثل التطبيع الدفعي (BN) [14]، ووحدات خطية مصححة (ReLU) [6]، والتجميع [19]، أو الالتفاف (Conv). نشير إلى مخرجات الطبقة ℓ بـ xₗ.

**شبكات ResNets.** تربط شبكات التغذية الأمامية التلافيفية التقليدية مخرجات الطبقة ℓ كمدخلات للطبقة (ℓ+1) [16]، مما يؤدي إلى الانتقال التالي للطبقة: xₗ = Hₗ(xₗ₋₁). تضيف شبكات ResNets [11] اتصال قفز يتجاوز التحويلات غير الخطية بدالة هوية:

xₗ = Hₗ(xₗ₋₁) + xₗ₋₁    (1)

ميزة شبكات ResNets هي أن التدرج يمكن أن يتدفق مباشرة عبر دالة الهوية من الطبقات اللاحقة إلى الطبقات السابقة. ومع ذلك، يتم دمج دالة الهوية ومخرجات Hₗ بالجمع، مما قد يعيق تدفق المعلومات في الشبكة.

**الاتصال الكثيف.** لتحسين تدفق المعلومات بين الطبقات بشكل أكبر، نقترح نمط اتصال مختلفاً: نقدم اتصالات مباشرة من أي طبقة إلى جميع الطبقات اللاحقة. يوضح الشكل 1 تخطيط شبكة DenseNet الناتجة بشكل تخطيطي. وبالتالي، تتلقى الطبقة ℓ خرائط الميزات لجميع الطبقات السابقة، x₀، ...، xₗ₋₁، كمدخلات:

xₗ = Hₗ([x₀, x₁, ..., xₗ₋₁])    (2)

حيث يشير [x₀، x₁، ...، xₗ₋₁] إلى ربط خرائط الميزات المنتجة في الطبقات 0، ...، ℓ−1. بسبب اتصالها الكثيف، نشير إلى معمارية الشبكة هذه باسم الشبكة التلافيفية الكثيفة (DenseNet). لسهولة التنفيذ، نربط المدخلات المتعددة لـ Hₗ(·) في المعادلة (2) في موتر واحد.

**الدالة المركبة.** بدافع من [12]، نعرف Hₗ(·) كدالة مركبة من ثلاث عمليات متتالية: التطبيع الدفعي (BN) [14]، يليها وحدة خطية مصححة (ReLU) [6] والتفاف 3×3 (Conv).

**طبقات التجميع.** عملية الربط المستخدمة في المعادلة (2) ليست قابلة للتطبيق عندما يتغير حجم خرائط الميزات. ومع ذلك، فإن جزءاً أساسياً من الشبكات التلافيفية هو طبقات تقليل العينات التي تغير حجم خرائط الميزات. لتسهيل تقليل العينات في معماريتنا، نقسم الشبكة إلى عدة كتل كثيفة متصلة بشكل كثيف؛ انظر الشكل 2. نشير إلى الطبقات بين الكتل على أنها طبقات انتقالية، والتي تقوم بالالتفاف والتجميع. تتكون الطبقات الانتقالية المستخدمة في تجاربنا من طبقة تطبيع دفعي وطبقة التفاف 1×1 متبوعة بطبقة تجميع متوسط 2×2.

**معدل النمو.** إذا أنتجت كل دالة Hₗ خرائط ميزات k، فإنه يترتب على ذلك أن الطبقة ℓ لديها k₀ + k × (ℓ−1) خريطة ميزات مدخلة، حيث k₀ هو عدد القنوات في طبقة المدخلات. الفرق المهم بين DenseNet ومعماريات الشبكات الموجودة هو أن DenseNet يمكن أن يكون لها طبقات ضيقة جداً، على سبيل المثال، k = 12. نشير إلى المعامل الفائق k على أنه معدل النمو للشبكة. نُظهر في القسم 4 أن معدل نمو صغير نسبياً كافٍ للحصول على أحدث النتائج على مجموعات البيانات التي اختبرناها. أحد التفسيرات لهذا هو أن كل طبقة لديها وصول إلى جميع خرائط الميزات السابقة في كتلتها، وبالتالي، إلى "المعرفة الجماعية" للشبكة. يمكن للمرء أن ينظر إلى خرائط الميزات على أنها الحالة العامة للشبكة. تضيف كل طبقة خرائط ميزات k خاصة بها إلى هذه الحالة. ينظم معدل النمو مقدار المعلومات الجديدة التي تساهم بها كل طبقة في الحالة العامة. الحالة العامة، بمجرد كتابتها، يمكن الوصول إليها من أي مكان داخل الشبكة، وعلى عكس معماريات الشبكات التقليدية، لا حاجة لتكرارها من طبقة إلى طبقة.

**طبقات عنق الزجاجة.** على الرغم من أن كل طبقة تنتج فقط k خريطة ميزات مخرجة، إلا أنها عادة ما يكون لديها مدخلات أكثر بكثير. لوحظ في [37، 11] أنه يمكن إدخال التفاف 1×1 كطبقة عنق زجاجة قبل كل التفاف 3×3 لتقليل عدد خرائط الميزات المدخلة، وبالتالي لتحسين الكفاءة الحسابية. نجد هذا التصميم فعالاً بشكل خاص لـ DenseNet ونشير إلى شبكتنا بمثل هذه الطبقة عنق الزجاجة، أي إلى نسخة BN-ReLU-Conv(1×1)-BN-ReLU-Conv(3×3) من Hₗ، باسم DenseNet-B. في تجاربنا، نسمح لكل التفاف 1×1 بإنتاج خرائط ميزات 4k.

**الضغط.** لتحسين إدماج النموذج بشكل أكبر، يمكننا تقليل عدد خرائط الميزات في الطبقات الانتقالية. إذا كانت الكتلة الكثيفة تحتوي على m خريطة ميزات، فإننا نسمح لطبقة الانتقال التالية بتوليد ⌊θm⌋ خريطة ميزات مخرجة، حيث 0 < θ ≤ 1 يُشار إليه على أنه عامل الضغط. عندما θ = 1، يبقى عدد خرائط الميزات عبر الطبقات الانتقالية دون تغيير. نشير إلى DenseNet مع θ < 1 باسم DenseNet-C، ونضع θ = 0.5 في تجربتنا. عندما يتم استخدام كل من طبقات عنق الزجاجة والطبقات الانتقالية مع θ < 1، نشير إلى نموذجنا باسم DenseNet-BC.

**تفاصيل التنفيذ.** على جميع مجموعات البيانات باستثناء ImageNet، فإن DenseNet المستخدم في تجاربنا يحتوي على ثلاث كتل كثيفة، كل منها يحتوي على عدد متساوٍ من الطبقات. قبل الدخول إلى الكتلة الكثيفة الأولى، يتم إجراء التفاف مع 16 قناة مخرجة (أو ضعف معدل النمو لـ DenseNet-BC) على الصور المدخلة. بالنسبة للطبقات التلافيفية ذات حجم نواة 3×3، يتم ملء كل جانب من المدخلات بصفر بواحد بكسل للحفاظ على حجم خريطة الميزات ثابتاً. نستخدم التفاف 1×1 متبوعاً بتجميع متوسط 2×2 كطبقات انتقالية بين كتلتين كثيفتين متجاورتين. في نهاية الكتلة الكثيفة الأخيرة، يتم إجراء تجميع متوسط شامل ثم يتم إرفاق مصنف softmax. أحجام خرائط الميزات في الكتل الكثيفة الثلاث هي 32×32 و16×16 و8×8، على التوالي. نجري تجارب مع بنية DenseNet الأساسية مع التكوينات {L=40، k=12}، {L=100، k=12} و{L=100، k=24}. بالنسبة لـ DenseNet-BC، يتم تقييم الشبكات ذات التكوينات {L=100، k=12}، {L=250، k=24} و{L=190، k=40}.

في تجاربنا على ImageNet، نستخدم بنية DenseNet-BC مع 4 كتل كثيفة على صور مدخلة 224×224. تتكون طبقة الالتفاف الأولية من التفافات 2k بحجم 7×7 مع خطوة 2؛ يتبع عدد خرائط الميزات في جميع الطبقات الأخرى أيضاً من ضبط k. تكوينات الشبكة الدقيقة التي استخدمناها على ImageNet موضحة في الجدول 1.

---

### Translation Notes

- **Figures referenced:** Figure 1 (dense block), Figure 2 (DenseNet architecture)
- **Tables referenced:** Table 1 (ImageNet configurations)
- **Key terms introduced:** Dense connectivity, growth rate (k), bottleneck layers, compression factor (θ), DenseNet-B, DenseNet-C, DenseNet-BC, collective knowledge, global state
- **Equations:** Equations (1) and (2) - ResNet and DenseNet formulations
- **Citations:** [16], [11], [14], [6], [19], [12], [37]
- **Special handling:** Mathematical notation preserved (subscripts, Greek letters), architectural details maintained precisely

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.86
- Glossary consistency: 0.89
- **Overall section score:** 0.89

### Back-translation Check

Key equation back-translated: "xₗ = Hₗ([x₀، x₁، ...، xₗ₋₁])" maintains mathematical precision. Technical concept: "معدل النمو ينظم مقدار المعلومات الجديدة التي تساهم بها كل طبقة" → "growth rate regulates how much new information each layer contributes" - accurately preserves meaning.
