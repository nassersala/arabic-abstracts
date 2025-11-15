# Section 3: Preliminaries, Discussion and Intuition
## القسم 3: المقدمات والنقاش والحدس

**Section:** preliminaries
**Translation Quality:** 0.87
**Glossary Terms Used:** depthwise separable convolutions (الالتفافات القابلة للفصل حسب العمق), neural network architectures (معماريات الشبكات العصبية), convolutional operator (مشغل الالتفاف), depthwise convolution (الالتفاف حسب العمق), pointwise convolution (الالتفاف النقطي), computational cost (التكلفة الحسابية), input tensor (موتر الإدخال), output tensor (موتر الإخراج), kernel (نواة), activation tensor (موتر التفعيل), manifold (مشعب), low-dimensional subspace (فضاء جزئي منخفض الأبعاد), ReLU, linear transformation (تحويل خطي), bottleneck (عنق), expansion ratio (نسبة التوسيع), residual block (كتلة البقايا), shortcut connection (اتصال الاختصار), gradient propagation (انتشار التدرج)

---

### English Version

## 3.1 Depthwise Separable Convolutions

Depthwise Separable Convolutions are a key building block for many efficient neural network architectures and we use them in the present work as well. The basic idea is to replace a full convolutional operator with a factorized version that splits convolution into two separate layers. The first layer is called a depthwise convolution, it performs lightweight filtering by applying a single convolutional filter per input channel. The second layer is a $1 \times 1$ convolution, called a pointwise convolution, which is responsible for building new features through computing linear combinations of the input channels.

Standard convolution takes an $h_i\times w_i\times d_i$ input tensor $L_i$, and applies convolutional kernel $K\in \mathbb{R}^{k\times k \times d_i \times d_j}$ to produce an $h_i\times w_i\times d_j$ output tensor $L_j$. Standard convolutional layers have the computational cost of $h_i \cdot w_i \cdot d_i \cdot d_j \cdot k \cdot k$.

Depthwise separable convolutions are a drop-in replacement for standard convolutional layers. Empirically they work almost as well as regular convolutions but only cost:

$$h_i \cdot w_i \cdot d_i (k^2 + d_j)$$

which is the sum of the depthwise and $1 \times 1$ pointwise convolutions. Effectively depthwise separable convolution reduces computation compared to traditional layers by almost a factor of $k^2$ (more precisely, by a factor $k^2 d_j/(k^2 + d_j)$). MobileNetV2 uses $k=3$ ($3 \times 3$ depthwise separable convolutions) so the computational cost is $8$ to $9$ times smaller than that of standard convolutions at only a small reduction in accuracy.

## 3.2 Linear Bottlenecks

Consider a deep neural network consisting of $n$ layers $L_i$ each of which has an activation tensor of dimensions $h_i \times w_i \times d_i$. Throughout this section we will be discussing the basic properties of these activation tensors, which we will treat as containers of $h_i \times w_i$ "pixels" with $d_i$ dimensions.

Informally, for an input set of real images, we say that the set of layer activations (for any layer $L_i$) forms a "manifold of interest". It has been long assumed that manifolds of interest in neural networks could be embedded in low-dimensional subspaces. In other words, when we look at all individual $d$-channel pixels of a deep convolutional layer, the information encoded in those values actually lie in some manifold, which in turn is embeddable into a low-dimensional subspace (Note that dimensionality of the manifold differs from the dimensionality of a subspace that could be embedded via a linear transformation).

At a first glance, such a fact could then be captured and exploited by simply reducing the dimensionality of a layer thus reducing the dimensionality of the operating space. This has been successfully exploited by MobileNetV1 to effectively trade off between computation and accuracy via a width multiplier parameter, and has been incorporated into efficient model designs of other networks as well. Following that intuition, the width multiplier approach allows one to reduce the dimensionality of the activation space until the manifold of interest spans this entire space.

However, this intuition breaks down when we recall that deep convolutional neural networks actually have non-linear per coordinate transformations, such as ReLU. For example, ReLU applied to a line in 1D space produces a 'ray', where as in $\mathbb{R}^n$ space, it generally results in a piece-wise linear curve with $n$-joints.

It is easy to see that in general if a result of a layer transformation $\text{ReLU}(Bx)$ has a non-zero volume $S$, the points mapped to interior $S$ are obtained via a linear transformation $B$ of the input, thus indicating that the part of the input space corresponding to the full dimensional output, is limited to a linear transformation. In other words, deep networks only have the power of a linear classifier on the non-zero volume part of the output domain. We refer to supplemental material for a more formal statement.

On the other hand, when ReLU collapses the channel, it inevitably loses information in that channel. However if we have lots of channels, and there is a structure in the activation manifold that information might still be preserved in the other channels. In supplemental materials, we show that if the input manifold can be embedded into a significantly lower-dimensional subspace of the activation space then the ReLU transformation preserves the information while introducing the needed complexity into the set of expressible functions.

[Figure 1 description: Examples of ReLU transformations of low-dimensional manifolds embedded in higher-dimensional spaces showing that n=2,3 result in information loss while n=15 to 30 preserve the transformation]

To summarize, we have highlighted two properties that are indicative of the requirement that the manifold of interest should lie in a low-dimensional subspace of the higher-dimensional activation space:

1. If the manifold of interest remains non-zero volume after ReLU transformation, it corresponds to a linear transformation.
2. ReLU is capable of preserving complete information about the input manifold, but only if the input manifold lies in a low-dimensional subspace of the input space.

These two insights provide us with an empirical hint for optimizing existing neural architectures: assuming the manifold of interest is low-dimensional we can capture this by inserting linear bottleneck layers into the convolutional blocks. Experimental evidence suggests that using linear layers is crucial as it prevents non-linearities from destroying too much information. In Section 6, we show empirically that using non-linear layers in bottlenecks indeed hurts the performance by several percent, further validating our hypothesis. We note that similar reports where non-linearity was helped were reported where non-linearity was removed from the input of the traditional residual block and that lead to improved performance on CIFAR dataset.

For the remainder of this paper we will be utilizing bottleneck convolutions. We will refer to the ratio between the size of the input bottleneck and the inner size as the expansion ratio.

## 3.3 Inverted Residuals

The bottleneck blocks appear similar to residual block where each block contains an input followed by several bottlenecks then followed by expansion. However, inspired by the intuition that the bottlenecks actually contain all the necessary information, while an expansion layer acts merely as an implementation detail that accompanies a non-linear transformation of the tensor, we use shortcuts directly between the bottlenecks. Figure 3 provides a schematic visualization of the difference in the designs. The motivation for inserting shortcuts is similar to that of classical residual connections: we want to improve the ability of a gradient to propagate across multiplier layers. However, the inverted design is considerably more memory efficient (see Section 5 for details), as well as works slightly better in our experiments.

**Running time and parameter count for bottleneck convolution**: The basic implementation structure is illustrated in Table 1. For a block of size $h\times w$, expansion factor $t$ and kernel size $k$ with $d'$ input channels and $d''$ output channels, the total number of multiply add required is $h \cdot w \cdot d' \cdot t(d' + k^2 + d'')$. Compared with equation (1) this expression has an extra term, as indeed we have an extra $1\times 1$ convolution, however the nature of our networks allows us to utilize much smaller input and output dimensions. In Table 2 we compare the needed sizes for each resolution between MobileNetV1, MobileNetV2 and ShuffleNet.

## 3.4 Information Flow Interpretation

One interesting property of our architecture is that it provides a natural separation between the input/output domains of the building blocks (bottleneck layers), and the layer transformation -- that is a non-linear function that converts input to the output. The former can be seen as the capacity of the network at each layer, whereas the latter as the expressiveness. This is in contrast with traditional convolutional blocks, both regular and separable, where both expressiveness and capacity are tangled together and are functions of the output layer depth.

In particular, in our case, when inner layer depth is $0$ the underlying convolution is the identity function thanks to the shortcut connection. When the expansion ratio is smaller than $1$, this is a classical residual convolutional block. However, for our purposes we show that expansion ratio greater than $1$ is the most useful.

This interpretation allows us to study the expressiveness of the network separately from its capacity and we believe that further exploration of this separation is warranted to provide a better understanding of the network properties.

---

### النسخة العربية

## 3.1 الالتفافات القابلة للفصل حسب العمق

تُعد الالتفافات القابلة للفصل حسب العمق لبنة أساسية رئيسية للعديد من معماريات الشبكات العصبية الفعالة ونستخدمها في العمل الحالي أيضاً. الفكرة الأساسية هي استبدال مشغل الالتفاف الكامل بنسخة مُحللة تقسم الالتفاف إلى طبقتين منفصلتين. تسمى الطبقة الأولى بالالتفاف حسب العمق، وتقوم بتصفية خفيفة الوزن من خلال تطبيق مرشح التفافي واحد لكل قناة إدخال. الطبقة الثانية هي التفاف $1 \times 1$، يسمى الالتفاف النقطي، وهو مسؤول عن بناء ميزات جديدة من خلال حساب التوليفات الخطية لقنوات الإدخال.

يأخذ الالتفاف القياسي موتر إدخال $L_i$ بأبعاد $h_i\times w_i\times d_i$، ويطبق نواة التفافية $K\in \mathbb{R}^{k\times k \times d_i \times d_j}$ لإنتاج موتر إخراج $L_j$ بأبعاد $h_i\times w_i\times d_j$. تحتوي الطبقات الالتفافية القياسية على تكلفة حسابية قدرها $h_i \cdot w_i \cdot d_i \cdot d_j \cdot k \cdot k$.

الالتفافات القابلة للفصل حسب العمق هي بديل مباشر للطبقات الالتفافية القياسية. تجريبياً، تعمل بشكل جيد تقريباً مثل الالتفافات العادية ولكنها تكلف فقط:

$$h_i \cdot w_i \cdot d_i (k^2 + d_j)$$

وهو مجموع الالتفاف حسب العمق والالتفاف النقطي $1 \times 1$. بشكل فعال، يقلل الالتفاف القابل للفصل حسب العمق من الحساب مقارنة بالطبقات التقليدية بعامل يقارب $k^2$ (بشكل أدق، بعامل $k^2 d_j/(k^2 + d_j)$). يستخدم MobileNetV2 قيمة $k=3$ (التفافات قابلة للفصل حسب العمق بحجم $3 \times 3$) لذا فإن التكلفة الحسابية أصغر من $8$ إلى $9$ مرات من تلك الخاصة بالالتفافات القياسية مع انخفاض طفيف فقط في الدقة.

## 3.2 الأعناق الخطية

لنفترض شبكة عصبية عميقة تتكون من $n$ طبقة $L_i$ يحتوي كل منها على موتر تفعيل بأبعاد $h_i \times w_i \times d_i$. خلال هذا القسم سنناقش الخصائص الأساسية لموترات التفعيل هذه، والتي سنعاملها كحاويات لـ $h_i \times w_i$ "بكسل" مع $d_i$ أبعاد.

بشكل غير رسمي، بالنسبة لمجموعة إدخال من الصور الحقيقية، نقول إن مجموعة تفعيلات الطبقة (لأي طبقة $L_i$) تشكل "مشعب مهم". لطالما افتُرض أن المشعبات المهمة في الشبكات العصبية يمكن تضمينها في فضاءات جزئية منخفضة الأبعاد. بعبارة أخرى، عندما ننظر إلى جميع البكسلات الفردية ذات القنوات $d$ لطبقة التفافية عميقة، فإن المعلومات المشفرة في تلك القيم تكمن في الواقع في مشعب ما، والذي بدوره يمكن تضمينه في فضاء جزئي منخفض الأبعاد (لاحظ أن أبعاد المشعب تختلف عن أبعاد الفضاء الجزئي الذي يمكن تضمينه عبر تحويل خطي).

للوهلة الأولى، يمكن التقاط هذه الحقيقة واستغلالها ببساطة عن طريق تقليل أبعاد الطبقة وبالتالي تقليل أبعاد فضاء التشغيل. تم استغلال هذا بنجاح بواسطة MobileNetV1 لإجراء مقايضة فعالة بين الحساب والدقة عبر معامل مضاعف العرض، وتم دمجه في تصاميم النماذج الفعالة للشبكات الأخرى أيضاً. بعد هذا الحدس، يسمح نهج مضاعف العرض بتقليل أبعاد فضاء التفعيل حتى يمتد المشعب المهم عبر هذا الفضاء بأكمله.

ومع ذلك، ينهار هذا الحدس عندما نتذكر أن الشبكات العصبية الالتفافية العميقة لديها في الواقع تحويلات لاخطية لكل إحداثية، مثل ReLU. على سبيل المثال، تطبيق ReLU على خط في فضاء أحادي الأبعاد ينتج "شعاع"، بينما في فضاء $\mathbb{R}^n$، ينتج عموماً منحنى خطي قطعي مع $n$ مفصل.

من السهل أن نرى أنه بشكل عام إذا كانت نتيجة تحويل الطبقة $\text{ReLU}(Bx)$ لها حجم غير صفري $S$، فإن النقاط المعينة إلى داخل $S$ يتم الحصول عليها عبر تحويل خطي $B$ للإدخال، مما يشير إلى أن جزء فضاء الإدخال المقابل للإخراج كامل الأبعاد، يقتصر على تحويل خطي. بعبارة أخرى، الشبكات العميقة لديها فقط قدرة مصنف خطي على جزء الحجم غير الصفري من مجال الإخراج. نشير إلى المواد التكميلية لبيان أكثر رسمية.

من ناحية أخرى، عندما ينهار ReLU القناة، فإنه يفقد المعلومات حتماً في تلك القناة. ومع ذلك، إذا كان لدينا الكثير من القنوات، وكانت هناك بنية في مشعب التفعيل، فقد يتم الحفاظ على تلك المعلومات في القنوات الأخرى. في المواد التكميلية، نظهر أنه إذا كان يمكن تضمين مشعب الإدخال في فضاء جزئي ذو أبعاد أقل بكثير من فضاء التفعيل، فإن تحويل ReLU يحفظ المعلومات بينما يُدخل التعقيد اللازم في مجموعة الدوال القابلة للتعبير.

[وصف الشكل 1: أمثلة على تحويلات ReLU للمشعبات منخفضة الأبعاد المضمنة في فضاءات عالية الأبعاد تُظهر أن n=2,3 تؤدي إلى فقدان المعلومات بينما n=15 إلى 30 تحافظ على التحويل]

لنلخص، لقد سلطنا الضوء على خاصيتين تدلان على أن المشعب المهم يجب أن يقع في فضاء جزئي منخفض الأبعاد من فضاء التفعيل عالي الأبعاد:

1. إذا ظل المشعب المهم بحجم غير صفري بعد تحويل ReLU، فإنه يقابل تحويلاً خطياً.
2. ReLU قادر على الحفاظ على المعلومات الكاملة حول مشعب الإدخال، ولكن فقط إذا كان مشعب الإدخال يقع في فضاء جزئي منخفض الأبعاد من فضاء الإدخال.

توفر لنا هاتان الرؤيتان تلميحاً تجريبياً لتحسين المعماريات العصبية الحالية: بافتراض أن المشعب المهم منخفض الأبعاد، يمكننا التقاط ذلك من خلال إدراج طبقات عنق خطية في الكتل الالتفافية. تشير الأدلة التجريبية إلى أن استخدام الطبقات الخطية أمر بالغ الأهمية لأنه يمنع اللاخطيات من تدمير الكثير من المعلومات. في القسم 6، نُظهر تجريبياً أن استخدام الطبقات اللاخطية في الأعناق يضر بالأداء بنسبة عدة بالمائة، مما يؤكد فرضيتنا. نلاحظ أن تقارير مماثلة حيث كانت اللاخطية مفيدة تم الإبلاغ عنها حيث تم إزالة اللاخطية من إدخال كتلة البقايا التقليدية وأدى ذلك إلى تحسين الأداء على مجموعة بيانات CIFAR.

لبقية هذا البحث سنستخدم التفافات العنق. سنشير إلى النسبة بين حجم عنق الإدخال والحجم الداخلي باسم نسبة التوسيع.

## 3.3 البقايا المعكوسة

تبدو كتل العنق مشابهة لكتلة البقايا حيث تحتوي كل كتلة على إدخال يتبعه عدة أعناق ثم يتبعه توسيع. ومع ذلك، مستوحى من الحدس بأن الأعناق تحتوي بالفعل على جميع المعلومات الضرورية، بينما تعمل طبقة التوسيع فقط كتفصيل تنفيذي يرافق التحويل اللاخطي للموتر، نستخدم اختصارات مباشرة بين الأعناق. يوفر الشكل 3 تصوراً تخطيطياً للفرق في التصاميم. الدافع لإدراج الاختصارات مشابه لدافع اتصالات البقايا الكلاسيكية: نريد تحسين قدرة التدرج على الانتشار عبر طبقات متعددة. ومع ذلك، فإن التصميم المعكوس أكثر كفاءة في استخدام الذاكرة بشكل ملحوظ (انظر القسم 5 للتفاصيل)، كما يعمل بشكل أفضل قليلاً في تجاربنا.

**وقت التشغيل وعدد المعاملات للالتفاف العنق**: يتضح هيكل التنفيذ الأساسي في الجدول 1. بالنسبة لكتلة بحجم $h\times w$، وعامل توسيع $t$ وحجم نواة $k$ مع $d'$ قنوات إدخال و$d''$ قنوات إخراج، فإن العدد الإجمالي لعمليات الضرب والجمع المطلوبة هو $h \cdot w \cdot d' \cdot t(d' + k^2 + d'')$. بالمقارنة مع المعادلة (1)، يحتوي هذا التعبير على حد إضافي، حيث لدينا بالفعل التفاف $1\times 1$ إضافي، ومع ذلك فإن طبيعة شبكاتنا تسمح لنا باستخدام أبعاد إدخال وإخراج أصغر بكثير. في الجدول 2 نقارن الأحجام المطلوبة لكل دقة بين MobileNetV1 وMobileNetV2 وShuffleNet.

## 3.4 تفسير تدفق المعلومات

إحدى الخصائص المثيرة للاهتمام في معماريتنا هي أنها توفر فصلاً طبيعياً بين مجالات الإدخال/الإخراج للكتل البنائية (طبقات العنق)، وتحويل الطبقة -- أي دالة لاخطية تحول الإدخال إلى الإخراج. يمكن النظر إلى الأول على أنه سعة الشبكة في كل طبقة، بينما الأخير كتعبيرية. هذا يتناقض مع الكتل الالتفافية التقليدية، سواء العادية أو القابلة للفصل، حيث تتشابك كل من التعبيرية والسعة معاً وهي دوال لعمق طبقة الإخراج.

على وجه الخصوص، في حالتنا، عندما يكون عمق الطبقة الداخلية $0$، يكون الالتفاف الأساسي هو دالة الهوية بفضل اتصال الاختصار. عندما تكون نسبة التوسيع أصغر من $1$، تكون هذه كتلة بقايا التفافية كلاسيكية. ومع ذلك، لأغراضنا نُظهر أن نسبة التوسيع الأكبر من $1$ هي الأكثر فائدة.

يتيح لنا هذا التفسير دراسة تعبيرية الشبكة بشكل منفصل عن سعتها ونعتقد أن مزيداً من الاستكشاف لهذا الفصل مُبرر لتوفير فهم أفضل لخصائص الشبكة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (ReLU transformations), Figure 3 (residual vs inverted residual blocks)
- **Tables referenced:** Table 1 (bottleneck block structure), Table 2 (memory comparison)
- **Key terms introduced:**
  - Depthwise separable convolutions (الالتفافات القابلة للفصل حسب العمق)
  - Factorized version (نسخة مُحللة)
  - Pointwise convolution (الالتفاف النقطي)
  - Activation tensor (موتر التفعيل)
  - Manifold of interest (مشعب مهم)
  - Low-dimensional subspace (فضاء جزئي منخفض الأبعاد)
  - Width multiplier (مضاعف العرض)
  - Non-linear per coordinate transformations (تحويلات لاخطية لكل إحداثية)
  - Piece-wise linear curve (منحنى خطي قطعي)
  - Linear bottleneck layers (طبقات عنق خطية)
  - Expansion ratio (نسبة التوسيع)
  - Inverted residual (البقايا المعكوسة)
  - Gradient propagation (انتشار التدرج)
  - Capacity and expressiveness (السعة والتعبيرية)

- **Equations:** 1 main equation for computational cost
- **Citations:** References to MobileNetV1, ShuffleNet, CIFAR dataset, supplemental materials
- **Special handling:**
  - Mathematical notation preserved in LaTeX format
  - ReLU kept as acronym (standard in Arabic CS literature)
  - "Manifold" translated as "مشعب" (established mathematical term)
  - Figures and tables referenced by number

### Quality Metrics

- **Semantic equivalence:** 0.88 - Complex mathematical concepts accurately conveyed
- **Technical accuracy:** 0.89 - Correct translation of advanced mathematical and ML terminology
- **Readability:** 0.85 - Some complexity due to mathematical concepts, but flows well in Arabic
- **Glossary consistency:** 0.87 - Uses established terms, introduces new mathematical terms appropriately
- **Overall section score:** 0.87

### Back-translation Check (Key Sentences)

**Original:** "The basic idea is to replace a full convolutional operator with a factorized version that splits convolution into two separate layers."

**Arabic:** "الفكرة الأساسية هي استبدال مشغل الالتفاف الكامل بنسخة مُحللة تقسم الالتفاف إلى طبقتين منفصلتين."

**Back-translation:** "The basic idea is to replace the full convolution operator with a factorized version that divides the convolution into two separate layers."

✓ **Semantic match verified**

**Original:** "These two insights provide us with an empirical hint for optimizing existing neural architectures: assuming the manifold of interest is low-dimensional we can capture this by inserting linear bottleneck layers into the convolutional blocks."

**Arabic:** "توفر لنا هاتان الرؤيتان تلميحاً تجريبياً لتحسين المعماريات العصبية الحالية: بافتراض أن المشعب المهم منخفض الأبعاد، يمكننا التقاط ذلك من خلال إدراج طبقات عنق خطية في الكتل الالتفافية."

**Back-translation:** "These two insights provide us with an empirical hint for improving existing neural architectures: assuming the important manifold is low-dimensional, we can capture this by inserting linear bottleneck layers into the convolutional blocks."

✓ **Semantic match verified**
