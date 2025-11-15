# Section 4: EfficientNet Architecture
## القسم 4: معمارية EfficientNet

**Section:** efficientnet-architecture
**Translation Quality:** 0.88
**Glossary Terms Used:** neural architecture search, baseline, accuracy, FLOPS, convolutional neural networks, architecture, depth, width, resolution, optimization

---

### English Version

Since model scaling does not change layer operators $\hat{F}_i$ in baseline network, having a good baseline network is also critical. We will evaluate our scaling method using existing ConvNets, but in order to better demonstrate the effectiveness of our scaling method, we have also developed a new mobile-size baseline, called EfficientNet-B0, by leveraging a multi-objective neural architecture search that optimizes both accuracy and FLOPS.

Specifically, we use the same search space as MnasNet, and use $ACC(m) \times [FLOPS(m)/T]^w$ as the optimization goal, where $ACC(m)$ and $FLOPS(m)$ denote the accuracy and FLOPS of model $m$, $T$ is the target FLOPS and $w=-0.07$ is a hyperparameter for controlling the trade-off between accuracy and FLOPS. Unlike MnasNet, here we optimize FLOPS rather than latency since we are not targeting any specific hardware device. Our search produces an efficient network, which we name EfficientNet-B0. Since we use the same search space, its architecture is similar to MnasNet, except EfficientNet-B0 is slightly bigger due to larger FLOPS target (our FLOPS target is 400M). Table 1 shows the architecture of EfficientNet-B0. Its main building block is mobile inverted bottleneck MBConv, to which we also add squeeze-and-excitation optimization.

**Table 1. EfficientNet-B0 baseline network** – Each row describes a stage $i$ with $\hat{L}_i$ layers, with input resolution $<\hat{H}_i, \hat{W}_i>$ and output channels $\hat{C}_i$. Notations are adopted from equation 2.

| Stage | Operator | Resolution | #Channels | #Layers |
|-------|----------|------------|-----------|---------|
| 1 | Conv3x3 | 224×224 | 32 | 1 |
| 2 | MBConv1, k3x3 | 112×112 | 16 | 1 |
| 3 | MBConv6, k3x3 | 112×112 | 24 | 2 |
| 4 | MBConv6, k5x5 | 56×56 | 40 | 2 |
| 5 | MBConv6, k3x3 | 28×28 | 80 | 3 |
| 6 | MBConv6, k5x5 | 14×14 | 112 | 3 |
| 7 | MBConv6, k5x5 | 14×14 | 192 | 4 |
| 8 | MBConv6, k3x3 | 7×7 | 320 | 1 |
| 9 | Conv1x1 & Pooling & FC | 7×7 | 1280 | 1 |

Starting from the baseline EfficientNet-B0, we apply our compound scaling method to scale it up with two steps:

- **STEP 1:** we first fix $\phi = 1$, assuming twice more resources available, and do a small grid search of $\alpha$, $\beta$, $\gamma$ based on Equation 2 and 3. In particular, we find the best values for EfficientNet-B0 are $\alpha = 1.2$, $\beta = 1.1$, $\gamma = 1.15$, under constraint of $\alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$.

- **STEP 2:** we then fix $\alpha$, $\beta$, $\gamma$ as constants and scale up baseline network with different $\phi$ using Equation 3, to obtain EfficientNet-B1 to B7 (Details in Table 2).

Notably, it is possible to achieve even better performance by searching for $\alpha$, $\beta$, $\gamma$ directly around a large model, but the search cost becomes prohibitively more expensive on larger models. Our method solves this issue by only doing search once on the small baseline network (step 1), and then use the same scaling coefficients for all other models (step 2).

---

### النسخة العربية

نظراً لأن توسيع النموذج لا يغير معاملات الطبقة $\hat{F}_i$ في شبكة خط الأساس، فإن وجود شبكة خط أساس جيدة أمر بالغ الأهمية أيضاً. سنقوم بتقييم طريقة التوسيع الخاصة بنا باستخدام الشبكات الالتفافية الموجودة، ولكن من أجل إثبات فعالية طريقة التوسيع الخاصة بنا بشكل أفضل، قمنا أيضاً بتطوير خط أساس جديد بحجم الهاتف المحمول، يسمى EfficientNet-B0، من خلال الاستفادة من البحث عن معمارية عصبية متعددة الأهداف التي تحسن كلاً من الدقة وFLOPS.

على وجه التحديد، نستخدم نفس مساحة البحث الخاصة بـ MnasNet، ونستخدم $ACC(m) \times [FLOPS(m)/T]^w$ كهدف للتحسين، حيث $ACC(m)$ و$FLOPS(m)$ تشير إلى دقة النموذج $m$ وFLOPS، و$T$ هو FLOPS المستهدف و$w=-0.07$ هو معامل فائق للتحكم في المفاضلة بين الدقة وFLOPS. على عكس MnasNet، نحسن هنا FLOPS بدلاً من الكمون لأننا لا نستهدف أي جهاز محدد. ينتج بحثنا شبكة فعالة، نسميها EfficientNet-B0. نظراً لأننا نستخدم نفس مساحة البحث، فإن معماريتها مشابهة لـ MnasNet، باستثناء أن EfficientNet-B0 أكبر قليلاً بسبب هدف FLOPS الأكبر (هدف FLOPS الخاص بنا هو 400 مليون). يوضح الجدول 1 معمارية EfficientNet-B0. الكتلة البنائية الرئيسية لها هي عنق الزجاجة المقلوب المحمول MBConv، والتي نضيف إليها أيضاً تحسين الضغط والإثارة.

**الجدول 1. شبكة خط الأساس EfficientNet-B0** – يصف كل صف مرحلة $i$ مع $\hat{L}_i$ طبقة، بدقة وضوح إدخال $<\hat{H}_i, \hat{W}_i>$ وقنوات مخرجات $\hat{C}_i$. تم اعتماد الترميزات من المعادلة 2.

| المرحلة | المعامل | دقة الوضوح | عدد القنوات | عدد الطبقات |
|-------|----------|------------|-----------|---------|
| 1 | Conv3x3 | 224×224 | 32 | 1 |
| 2 | MBConv1, k3x3 | 112×112 | 16 | 1 |
| 3 | MBConv6, k3x3 | 112×112 | 24 | 2 |
| 4 | MBConv6, k5x5 | 56×56 | 40 | 2 |
| 5 | MBConv6, k3x3 | 28×28 | 80 | 3 |
| 6 | MBConv6, k5x5 | 14×14 | 112 | 3 |
| 7 | MBConv6, k5x5 | 14×14 | 192 | 4 |
| 8 | MBConv6, k3x3 | 7×7 | 320 | 1 |
| 9 | Conv1x1 & Pooling & FC | 7×7 | 1280 | 1 |

بدءاً من خط الأساس EfficientNet-B0، نطبق طريقة التوسيع المركبة الخاصة بنا لتوسيعه بخطوتين:

- **الخطوة 1:** نثبت أولاً $\phi = 1$، بافتراض توفر ضعف الموارد، ونقوم ببحث شبكي صغير عن $\alpha$ و$\beta$ و$\gamma$ بناءً على المعادلتين 2 و3. على وجه الخصوص، نجد أن أفضل القيم لـ EfficientNet-B0 هي $\alpha = 1.2$ و$\beta = 1.1$ و$\gamma = 1.15$، تحت قيد $\alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$.

- **الخطوة 2:** نثبت بعد ذلك $\alpha$ و$\beta$ و$\gamma$ كثوابت ونوسع شبكة خط الأساس بـ $\phi$ مختلفة باستخدام المعادلة 3، للحصول على EfficientNet-B1 إلى B7 (التفاصيل في الجدول 2).

والجدير بالذكر أنه من الممكن تحقيق أداء أفضل من خلال البحث عن $\alpha$ و$\beta$ و$\gamma$ مباشرة حول نموذج كبير، ولكن تكلفة البحث تصبح باهظة بشكل كبير على النماذج الأكبر. تحل طريقتنا هذه المشكلة من خلال إجراء البحث مرة واحدة فقط على شبكة خط الأساس الصغيرة (الخطوة 1)، ثم استخدام نفس معاملات التوسيع لجميع النماذج الأخرى (الخطوة 2).

---

### Translation Notes

- **Figures referenced:** None directly, but references Table 1 and Table 2
- **Key terms introduced:** Mobile inverted bottleneck (MBConv), squeeze-and-excitation, multi-objective optimization, latency, hyperparameter
- **Equations:** References to Equations 2 and 3 from previous section
- **Tables:** Table 1 showing EfficientNet-B0 architecture details
- **Citations:** MnasNet
- **Special handling:** Table structure preserved with Arabic headers, technical operators kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation (Key Paragraph)

"Starting from the baseline EfficientNet-B0, we apply our compound scaling method to scale it up in two steps: STEP 1: we first fix φ = 1, assuming twice the resources are available, and do a small grid search for α, β, γ based on Equations 2 and 3. Specifically, we find that the best values for EfficientNet-B0 are α = 1.2, β = 1.1, γ = 1.15, under the constraint α · β² · γ² ≈ 2. STEP 2: we then fix α, β, γ as constants and scale up the baseline network with different φ using Equation 3, to obtain EfficientNet-B1 to B7."
