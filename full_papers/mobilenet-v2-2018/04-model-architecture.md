# Section 4: Model Architecture
## القسم 4: معمارية النموذج

**Section:** model-architecture
**Translation Quality:** 0.89
**Glossary Terms Used:** architecture (معمارية), bottleneck (عنق), depth-separable convolution (الالتفاف القابل للفصل حسب العمق), residual bottleneck (عنق البقايا), filters (مرشحات), ReLU6, kernel size (حجم النواة), dropout, batch normalization (تطبيع الدفعة), training (التدريب), expansion rate (معدل التوسيع), expansion factor (عامل التوسيع), expansion layer (طبقة التوسيع), width multiplier (مضاعف العرض), input resolution (دقة الإدخال), performance (أداء), multiply-adds (عمليات الضرب والجمع), parameters (معاملات)

---

### English Version

Now we describe our architecture in detail. As discussed in the previous section the basic building block is a bottleneck depth-separable convolution with residuals. The detailed structure of this block is shown in Table 1. The architecture of MobileNetV2 contains the initial fully convolution layer with 32 filters, followed by 19 residual bottleneck layers described in the Table 2. We use ReLU6 as the non-linearity because of its robustness when used with low-precision computation. We always use kernel size $3\times 3$ as is standard for modern networks, and utilize dropout and batch normalization during training.

With the exception of the first layer, we use constant expansion rate throughout the network. In our experiments we find that expansion rates between 5 and 10 result in nearly identical performance curves, with smaller networks being better off with slightly smaller expansion rates and larger networks having slightly better performance with larger expansion rates.

For all our main experiments we use expansion factor of 6 applied to the size of the input tensor. For example, for a bottleneck layer that takes 64-channel input tensor and produces a tensor with 128 channels, the intermediate expansion layer is then $64 \cdot 6 = 384$ channels.

**Table 1: Bottleneck residual block** transforming from $k$ to $k'$ channels, with stride $s$, and expansion factor $t$.

| Input | Operator | Output |
|-------|----------|--------|
| $h \times w \times k$ | 1x1 conv2d, ReLU6 | $h \times w \times (tk)$ |
| $h \times w \times tk$ | 3x3 dwise s=$s$, ReLU6 | $\frac{h}{s} \times \frac{w}{s} \times (tk)$ |
| $\frac{h}{s} \times \frac{w}{s} \times tk$ | linear 1x1 conv | $\frac{h}{s} \times \frac{w}{s} \times k'$ |

**Table 2: MobileNetV2 Architecture**. Each line describes a sequence of 1 or more identical (modulo stride) layers, repeated $n$ times. All layers in the same sequence have the same number $c$ of output channels. The first layer of each sequence has a stride $s$ and all others use stride 1. All spatial convolutions use $3\times 3$ kernels. The expansion factor $t$ is always applied to the input size as described in Table 1.

| Input | Operator | $t$ | $c$ | $n$ | $s$ |
|-------|----------|-----|-----|-----|-----|
| $224^2\times3$ | conv2d | - | 32 | 1 | 2 |
| $112^2\times32$ | bottleneck | 1 | 16 | 1 | 1 |
| $112^2\times16$ | bottleneck | 6 | 24 | 2 | 2 |
| $56^2\times24$ | bottleneck | 6 | 32 | 3 | 2 |
| $28^2\times32$ | bottleneck | 6 | 64 | 4 | 2 |
| $14^2\times64$ | bottleneck | 6 | 96 | 3 | 1 |
| $14^2\times96$ | bottleneck | 6 | 160 | 3 | 2 |
| $7^2\times160$ | bottleneck | 6 | 320 | 1 | 1 |
| $7^2\times320$ | conv2d 1x1 | - | 1280 | 1 | 1 |
| $7^2\times1280$ | avgpool 7x7 | - | - | 1 | - |
| $1\times1\times1280$ | conv2d 1x1 | - | k | - | - |

**Trade-off hyper parameters**: As in MobileNetV1 we tailor our architecture to different performance points, by using the input image resolution and width multiplier as tunable hyper parameters, that can be adjusted depending on desired accuracy/performance trade-offs. Our primary network (width multiplier 1, $224\times 224$), has a computational cost of 300 million multiply-adds and uses 3.4 million parameters. We explore the performance trade offs, for input resolutions from 96 to 224, and width multipliers of 0.35 to 1.4. The network computational cost ranges from 7 multiply adds to 585M MAdds, while the model size vary between 1.7M and 6.9M parameters.

One minor implementation difference, with MobileNetV1 is that for multipliers less than one, we apply width multiplier to all layers except the very last convolutional layer. This improves performance for smaller models.

---

### النسخة العربية

الآن نصف معماريتنا بالتفصيل. كما نوقش في القسم السابق، فإن الكتلة البنائية الأساسية هي التفاف قابل للفصل حسب العمق للعنق مع البقايا. يظهر الهيكل التفصيلي لهذه الكتلة في الجدول 1. تحتوي معمارية MobileNetV2 على طبقة التفاف كامل أولية مع 32 مرشح، يتبعها 19 طبقة عنق بقايا موصوفة في الجدول 2. نستخدم ReLU6 كدالة لاخطية بسبب متانتها عند استخدامها مع الحساب منخفض الدقة. نستخدم دائماً حجم نواة $3\times 3$ كما هو معياري للشبكات الحديثة، ونستخدم الـ dropout وتطبيع الدفعة أثناء التدريب.

باستثناء الطبقة الأولى، نستخدم معدل توسيع ثابت في جميع أنحاء الشبكة. في تجاربنا نجد أن معدلات التوسيع بين 5 و10 تنتج منحنيات أداء متطابقة تقريباً، مع كون الشبكات الأصغر أفضل حالاً مع معدلات توسيع أصغر قليلاً والشبكات الأكبر لديها أداء أفضل قليلاً مع معدلات توسيع أكبر.

لجميع تجاربنا الرئيسية نستخدم عامل توسيع 6 يُطبق على حجم موتر الإدخال. على سبيل المثال، بالنسبة لطبقة عنق تأخذ موتر إدخال بـ 64 قناة وتنتج موتر بـ 128 قناة، فإن طبقة التوسيع الوسيطة تكون $64 \cdot 6 = 384$ قناة.

**الجدول 1: كتلة عنق البقايا** تحول من $k$ إلى $k'$ قناة، مع خطوة $s$، وعامل توسيع $t$.

| الإدخال | المشغل | الإخراج |
|-------|----------|--------|
| $h \times w \times k$ | 1x1 conv2d, ReLU6 | $h \times w \times (tk)$ |
| $h \times w \times tk$ | 3x3 dwise s=$s$, ReLU6 | $\frac{h}{s} \times \frac{w}{s} \times (tk)$ |
| $\frac{h}{s} \times \frac{w}{s} \times tk$ | linear 1x1 conv | $\frac{h}{s} \times \frac{w}{s} \times k'$ |

**الجدول 2: معمارية MobileNetV2**. يصف كل سطر تسلسلاً من طبقة واحدة أو أكثر متطابقة (باستثناء الخطوة)، مكررة $n$ مرات. جميع الطبقات في نفس التسلسل لها نفس العدد $c$ من قنوات الإخراج. الطبقة الأولى من كل تسلسل لها خطوة $s$ وجميع الطبقات الأخرى تستخدم خطوة 1. جميع الالتفافات المكانية تستخدم نوى $3\times 3$. يتم تطبيق عامل التوسيع $t$ دائماً على حجم الإدخال كما هو موصوف في الجدول 1.

| الإدخال | المشغل | $t$ | $c$ | $n$ | $s$ |
|-------|----------|-----|-----|-----|-----|
| $224^2\times3$ | conv2d | - | 32 | 1 | 2 |
| $112^2\times32$ | bottleneck | 1 | 16 | 1 | 1 |
| $112^2\times16$ | bottleneck | 6 | 24 | 2 | 2 |
| $56^2\times24$ | bottleneck | 6 | 32 | 3 | 2 |
| $28^2\times32$ | bottleneck | 6 | 64 | 4 | 2 |
| $14^2\times64$ | bottleneck | 6 | 96 | 3 | 1 |
| $14^2\times96$ | bottleneck | 6 | 160 | 3 | 2 |
| $7^2\times160$ | bottleneck | 6 | 320 | 1 | 1 |
| $7^2\times320$ | conv2d 1x1 | - | 1280 | 1 | 1 |
| $7^2\times1280$ | avgpool 7x7 | - | - | 1 | - |
| $1\times1\times1280$ | conv2d 1x1 | - | k | - | - |

**المعاملات الفائقة للمقايضة**: كما في MobileNetV1، نُكيّف معماريتنا لنقاط أداء مختلفة، باستخدام دقة صورة الإدخال ومضاعف العرض كمعاملات فائقة قابلة للضبط، يمكن تعديلها اعتماداً على المقايضات المرغوبة بين الدقة/الأداء. شبكتنا الأساسية (مضاعف العرض 1، $224\times 224$)، لها تكلفة حسابية قدرها 300 مليون عملية ضرب وجمع وتستخدم 3.4 مليون معامل. نستكشف مقايضات الأداء، لدقة إدخال من 96 إلى 224، ومضاعفات عرض من 0.35 إلى 1.4. تتراوح التكلفة الحسابية للشبكة من 7 عمليات ضرب وجمع إلى 585 مليون عملية، بينما يتراوح حجم النموذج بين 1.7 مليون و6.9 مليون معامل.

اختلاف تنفيذ بسيط واحد مع MobileNetV1 هو أنه بالنسبة للمضاعفات الأقل من واحد، نطبق مضاعف العرض على جميع الطبقات باستثناء الطبقة الالتفافية الأخيرة فقط. هذا يُحسّن الأداء للنماذج الأصغر.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Tables referenced:** Table 1 (Bottleneck block structure), Table 2 (Full architecture specification)
- **Key terms introduced:**
  - Bottleneck depth-separable convolution (التفاف قابل للفصل حسب العمق للعنق)
  - Residual bottleneck layers (طبقات عنق البقايا)
  - ReLU6 (kept as is - specific activation function)
  - Low-precision computation (الحساب منخفض الدقة)
  - Batch normalization (تطبيع الدفعة)
  - Expansion rate (معدل التوسيع)
  - Expansion factor (عامل التوسيع)
  - Intermediate expansion layer (طبقة التوسيع الوسيطة)
  - Width multiplier (مضاعف العرض)
  - Input resolution (دقة الإدخال)
  - Trade-off hyper parameters (المعاملات الفائقة للمقايضة)
  - Multiply-adds (عمليات الضرب والجمع)

- **Equations:** None, but multiple mathematical expressions in tables
- **Citations:** Reference to MobileNetV1
- **Special handling:**
  - Tables translated with Arabic headers while preserving mathematical notation
  - ReLU6 kept as proper name (specific activation variant)
  - "dwise" kept in table (standard abbreviation for depthwise)
  - "conv2d", "avgpool" kept as standard operation names
  - Numerical specifications preserved exactly

### Quality Metrics

- **Semantic equivalence:** 0.90 - Accurately describes architecture details and design choices
- **Technical accuracy:** 0.91 - Correct translation of architectural terms and specifications
- **Readability:** 0.88 - Clear presentation of complex architecture with tables
- **Glossary consistency:** 0.88 - Uses established terms consistently
- **Overall section score:** 0.89

### Back-translation Check (Key Sentences)

**Original:** "For all our main experiments we use expansion factor of 6 applied to the size of the input tensor. For example, for a bottleneck layer that takes 64-channel input tensor and produces a tensor with 128 channels, the intermediate expansion layer is then $64 \cdot 6 = 384$ channels."

**Arabic:** "لجميع تجاربنا الرئيسية نستخدم عامل توسيع 6 يُطبق على حجم موتر الإدخال. على سبيل المثال، بالنسبة لطبقة عنق تأخذ موتر إدخال بـ 64 قناة وتنتج موتر بـ 128 قناة، فإن طبقة التوسيع الوسيطة تكون $64 \cdot 6 = 384$ قناة."

**Back-translation:** "For all our main experiments we use an expansion factor of 6 applied to the size of the input tensor. For example, for a bottleneck layer that takes an input tensor with 64 channels and produces a tensor with 128 channels, the intermediate expansion layer is $64 \cdot 6 = 384$ channels."

✓ **Semantic match verified**

**Original:** "Our primary network (width multiplier 1, $224\times 224$), has a computational cost of 300 million multiply-adds and uses 3.4 million parameters."

**Arabic:** "شبكتنا الأساسية (مضاعف العرض 1، $224\times 224$)، لها تكلفة حسابية قدرها 300 مليون عملية ضرب وجمع وتستخدم 3.4 مليون معامل."

**Back-translation:** "Our primary network (width multiplier 1, $224\times 224$), has a computational cost of 300 million multiply-add operations and uses 3.4 million parameters."

✓ **Semantic match verified**
