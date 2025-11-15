# Section 4: EfficientNet Architecture
## القسم 4: معمارية EfficientNet

**Section:** architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** model scaling, baseline, neural architecture search, accuracy, FLOPS, mobile inverted bottleneck, squeeze-and-excitation, compound scaling, grid search

---

### English Version

Since model scaling does not change layer operators F̂i in baseline network, having a good baseline network is also critical. We will evaluate our scaling method using existing ConvNets, but in order to better demonstrate the effectiveness of our scaling method, we have also developed a new mobile-size baseline, called EfficientNet.

Inspired by (Tan et al., 2019), we develop our baseline network by leveraging a multi-objective neural architecture search that optimizes both accuracy and FLOPS. Specifically, we use the same search space as (Tan et al., 2019), and use ACC(m) × [FLOPS(m)/T]^w as the optimization goal, where ACC(m) and FLOPS(m) denote the accuracy and FLOPS of model m, T is the target FLOPS and w=-0.07 is a hyperparameter for controlling the trade-off between accuracy and FLOPS. Unlike (Tan et al., 2019; Cai et al., 2019), here we optimize FLOPS rather than latency since we are not targeting any specific hardware device. Our search produces an efficient network, which we name EfficientNet-B0. Since we use the same search space as (Tan et al., 2019), the architecture is similar to MnasNet, except our EfficientNet-B0 is slightly bigger due to the larger FLOPS target (our FLOPS target is 400M). Table 1 shows the architecture of EfficientNet-B0. Its main building block is mobile inverted bottleneck MBConv (Sandler et al., 2018; Tan et al., 2019), to which we also add squeeze-and-excitation optimization (Hu et al., 2018).

**Table 1. EfficientNet-B0 baseline network** – Each row describes a stage i with L̂i layers, with input resolution <Ĥi, Ŵi> and output channels Ĉi. Notations are adopted from equation 2.

| Stage i | Operator F̂i | Resolution Ĥi × Ŵi | #Channels Ĉi | #Layers L̂i |
|---------|-------------|-------------------|--------------|------------|
| 1 | Conv3x3 | 224 × 224 | 32 | 1 |
| 2 | MBConv1, k3x3 | 112 × 112 | 16 | 1 |
| 3 | MBConv6, k3x3 | 112 × 112 | 24 | 2 |
| 4 | MBConv6, k5x5 | 56 × 56 | 40 | 2 |
| 5 | MBConv6, k3x3 | 28 × 28 | 80 | 3 |
| 6 | MBConv6, k5x5 | 14 × 14 | 112 | 3 |
| 7 | MBConv6, k5x5 | 14 × 14 | 192 | 4 |
| 8 | MBConv6, k3x3 | 7 × 7 | 320 | 1 |
| 9 | Conv1x1 & Pooling & FC | 7 × 7 | 1280 | 1 |

Starting from the baseline EfficientNet-B0, we apply our compound scaling method to scale it up with two steps:

• **STEP 1:** we first fix φ = 1, assuming twice more resources available, and do a small grid search of α, β, γ based on Equation 2 and 3. In particular, we find the best values for EfficientNet-B0 are α = 1.2, β = 1.1, γ = 1.15, under constraint of α · β² · γ² ≈ 2.

• **STEP 2:** we then fix α, β, γ as constants and scale up baseline network with different φ using Equation 3, to obtain EfficientNet-B1 to B7 (Details in Table 2).

Notably, it is possible to achieve even better performance by searching for α, β, γ directly around a large model, but the search cost becomes prohibitively more expensive on larger models. Our method solves this issue by only doing search once on the small baseline network (step 1), and then use the same scaling coefficients for all other models (step 2).

---

### النسخة العربية

نظراً لأن توسيع النموذج لا يغير معاملات الطبقة F̂i في شبكة خط الأساس، فإن الحصول على شبكة خط أساس جيدة أمر حاسم أيضاً. سنقيم طريقة التوسيع الخاصة بنا باستخدام الشبكات الالتفافية الموجودة، ولكن من أجل إظهار فعالية طريقة التوسيع الخاصة بنا بشكل أفضل، قمنا أيضاً بتطوير خط أساس جديد بحجم الهاتف المحمول، يسمى EfficientNet.

مستوحى من (Tan et al., 2019)، نطور شبكة خط الأساس الخاصة بنا من خلال الاستفادة من البحث عن معمارية عصبية متعدد الأهداف يحسن كلاً من الدقة وFLOPS. على وجه الخصوص، نستخدم نفس مساحة البحث كما في (Tan et al., 2019)، ونستخدم ACC(m) × [FLOPS(m)/T]^w كهدف التحسين، حيث تشير ACC(m) وFLOPS(m) إلى دقة وFLOPS للنموذج m، وT هو FLOPS المستهدف وw=-0.07 هو معامل فائق للتحكم في المقايضة بين الدقة وFLOPS. على عكس (Tan et al., 2019; Cai et al., 2019)، نقوم هنا بتحسين FLOPS بدلاً من زمن الاستجابة لأننا لا نستهدف أي جهاز معين. ينتج عن بحثنا شبكة فعالة، نسميها EfficientNet-B0. نظراً لأننا نستخدم نفس مساحة البحث كما في (Tan et al., 2019)، فإن المعمارية مشابهة لـ MnasNet، باستثناء أن EfficientNet-B0 الخاص بنا أكبر قليلاً بسبب هدف FLOPS الأكبر (هدف FLOPS الخاص بنا هو 400 مليون). يُظهر الجدول 1 معمارية EfficientNet-B0. كتلة البناء الرئيسية الخاصة به هي عنق الزجاجة المقلوب للهاتف المحمول MBConv (Sandler et al., 2018; Tan et al., 2019)، الذي نضيف إليه أيضاً تحسين الضغط والإثارة (Hu et al., 2018).

**الجدول 1. شبكة خط الأساس EfficientNet-B0** - يصف كل صف مرحلة i بـ L̂i طبقات، مع دقة وضوح المُدخلات <Ĥi, Ŵi> وقنوات المُخرجات Ĉi. الترميزات مأخوذة من المعادلة 2.

| المرحلة i | المعامل F̂i | دقة الوضوح Ĥi × Ŵi | عدد القنوات Ĉi | عدد الطبقات L̂i |
|---------|-------------|-------------------|--------------|------------|
| 1 | Conv3x3 | 224 × 224 | 32 | 1 |
| 2 | MBConv1, k3x3 | 112 × 112 | 16 | 1 |
| 3 | MBConv6, k3x3 | 112 × 112 | 24 | 2 |
| 4 | MBConv6, k5x5 | 56 × 56 | 40 | 2 |
| 5 | MBConv6, k3x3 | 28 × 28 | 80 | 3 |
| 6 | MBConv6, k5x5 | 14 × 14 | 112 | 3 |
| 7 | MBConv6, k5x5 | 14 × 14 | 192 | 4 |
| 8 | MBConv6, k3x3 | 7 × 7 | 320 | 1 |
| 9 | Conv1x1 & Pooling & FC | 7 × 7 | 1280 | 1 |

بدءاً من خط الأساس EfficientNet-B0، نطبق طريقة التوسيع المركب الخاصة بنا لتوسيعه بخطوتين:

• **الخطوة 1:** نقوم أولاً بإصلاح φ = 1، بافتراض توافر موارد أكثر بمقدار الضعف، ونقوم ببحث شبكي صغير لـ α وβ وγ بناءً على المعادلتين 2 و3. على وجه الخصوص، نجد أن أفضل القيم لـ EfficientNet-B0 هي α = 1.2 وβ = 1.1 وγ = 1.15، تحت قيد α · β² · γ² ≈ 2.

• **الخطوة 2:** نقوم بعد ذلك بإصلاح α وβ وγ كثوابت وتوسيع شبكة خط الأساس بقيم φ مختلفة باستخدام المعادلة 3، للحصول على EfficientNet-B1 إلى B7 (التفاصيل في الجدول 2).

والجدير بالذكر أنه من الممكن تحقيق أداء أفضل من خلال البحث عن α وβ وγ مباشرة حول نموذج كبير، ولكن تكلفة البحث تصبح باهظة بشكل أكبر على النماذج الأكبر. تحل طريقتنا هذه المشكلة من خلال إجراء البحث مرة واحدة فقط على شبكة خط الأساس الصغيرة (الخطوة 1)، ثم استخدام نفس معاملات التوسيع لجميع النماذج الأخرى (الخطوة 2).

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 1 (EfficientNet-B0 architecture), Table 2 (mentioned)
- **Key terms introduced:** mobile inverted bottleneck (عنق الزجاجة المقلوب للهاتف المحمول), squeeze-and-excitation (الضغط والإثارة), multi-objective (متعدد الأهداف), hyperparameter (معامل فائق), latency (زمن الاستجابة)
- **Equations:** References to Equations 2 and 3
- **Citations:** Multiple references to prior work
- **Special handling:** Table structure translated; kept technical notation (MBConv, Conv3x3, etc.) in English; preserved mathematical formulas

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
