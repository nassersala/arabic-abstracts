# Section 3: Compound Model Scaling
## القسم 3: التوسيع المركب للنموذج

**Section:** compound-scaling
**Translation Quality:** 0.89
**Glossary Terms Used:** convolutional neural networks, depth, width, resolution, accuracy, computational cost, FLOPS, parameters, baseline, optimization, receptive field

---

### English Version

#### 3.1 Problem Formulation

A ConvNet Layer i can be defined as a function: Y_i = F_i(X_i), where F_i is the operator, Y_i is output tensor, X_i is input tensor, with tensor shape <H_i, W_i, C_i>, where H_i and W_i are spatial dimensions, and C_i is the channel dimension. A ConvNet N can be defined as a list of composed layers: N = F_k ⊙ ... ⊙ F_2 ⊙ F_1(X_1) = ⊙_j=1..k F_j(X_1). In practice, ConvNet layers are often partitioned into multiple stages and all layers in each stage share the same architecture: for example, ResNet has five stages, and all layers in each stage has the same convolutional type except the first layer that performs down-sampling. Therefore, we can define a ConvNet as:

$$N = ⊙_{i=1..s} F_i^{L_i}(X_{<H_i,W_i,C_i>})$$

where $F_i^{L_i}$ denotes layer $F_i$ is repeated $L_i$ times in stage $i$, $<H_i, W_i, C_i>$ denotes the shape of input tensor X of layer $i$. Figure 3(a) shows a representative ConvNet, where the spatial dimension is gradually shrunk but the channel dimension is expanded over layers, for example, from initial input shape <224, 224, 3> to final output shape <7, 7, 512>.

Unlike regular ConvNet designs that mostly focus on finding the best layer architecture $F_i$, model scaling tries to expand the network length ($L_i$), width ($C_i$), and/or resolution ($H_i$, $W_i$) without changing $F_i$ predefined in the baseline network. By fixing $F_i$, model scaling simplifies the design problem for new resource constraints, but it still remains a large design space to explore different $L_i$, $C_i$, $H_i$, $W_i$ for each layer. In order to further reduce the design space, we restrict that all layers must be scaled uniformly with constant ratio. Our target is to maximize the model accuracy for any given resource constraints, which can be formulated as an optimization problem:

$$\max_{d,w,r} \text{Accuracy}(N(d, w, r))$$
$$\text{s.t. } N(d, w, r) = ⊙_{i=1..s} \hat{F}_i^{d \cdot \hat{L}_i}(X_{<r \cdot \hat{H}_i, r \cdot \hat{W}_i, w \cdot \hat{C}_i>})$$
$$\text{Memory}(N) \leq \text{target\_memory}$$
$$\text{FLOPS}(N) \leq \text{target\_flops}$$

where $w$, $d$, $r$ are coefficients for scaling network width, depth, and resolution; $\hat{F}_i$, $\hat{L}_i$, $\hat{H}_i$, $\hat{W}_i$, $\hat{C}_i$ are predefined parameters in baseline network (see Table 1 as an example).

#### 3.2 Scaling Dimensions

The main difficulty of the above optimization problem is that the optimal $d$, $w$, $r$ depend on each other and the values change under different resource constraints. Due to this difficulty, conventional methods mostly scale ConvNets in one of these dimensions:

**Depth (d):** Scaling network depth is the most common way used by many ConvNets. The intuition is that deeper ConvNet can capture richer and more complex features, and generalize well on new tasks. However, deeper networks are also more difficult to train due to the vanishing gradient problem. Although several techniques, such as skip connections and batch normalization, alleviate the training problem, the accuracy gain of very deep networks diminishes: for example, ResNet-1000 has similar accuracy as ResNet-101 even though it has much more layers. Figure 3 (middle) shows our empirical study on scaling a baseline model with different depth coefficient $d$, further suggesting the diminishing accuracy return for very deep ConvNets.

**Width (w):** Scaling network width is commonly used for small size models. As discussed in, wider networks tend to be able to capture more fine-grained features and are easier to train. However, extremely wide but shallow networks tend to have difficulties in capturing higher level features. Our empirical results in Figure 3 (left) show that the accuracy quickly saturates when networks become much wider with larger $w$.

**Resolution (r):** With higher resolution input images, ConvNets can potentially capture more fine-grained patterns. Starting from 224x224 in early ConvNets, modern ConvNets tend to use 299x299 or 331x331 for better accuracy. Recently, GPipe achieves state-of-the-art ImageNet accuracy with 480x480 resolution. Higher resolutions, such as 600x600, are also widely used in object detection ConvNets. Figure 3 (right) shows that scaling up resolution improves accuracy, but the accuracy gain diminishes for very high resolutions.

**Observation 1** – Scaling up any dimension of network width, depth, or resolution improves accuracy, but the accuracy gain diminishes for bigger models.

#### 3.3 Compound Scaling

We empirically observe that different scaling dimensions are not independent. Intuitively, for higher resolution images, we should increase network depth, so the larger receptive fields can help capture similar features that include more pixels in bigger images. Correspondingly, we should also increase network width when resolution is higher, in order to capture more fine-grained patterns with more pixels in high resolution images. These intuitions suggest that we need to coordinate and balance different scaling dimensions rather than conventional single-dimension scaling.

To validate our intuitions, we compare width scaling under different network depths and resolutions, as shown in Figure 4. If we only scale network width w without changing depth (d=1.0) and resolution (r=1.0), the accuracy saturates quickly. With deeper (d=2.0) and higher resolution (r=2.0), width scaling achieves much better accuracy under the same FLOPS cost. These results lead us to the second observation:

**Observation 2** – In order to pursue better accuracy and efficiency, it is critical to balance all dimensions of network width, depth, and resolution during ConvNet scaling.

In fact, a few prior works have already tried to arbitrarily balance network width and depth, but they all require tedious manual tuning. In this paper, we propose a new compound scaling method, which use a compound coefficient φ to uniformly scale network width, depth, and resolution in a principled way:

$$\text{depth: } d = \alpha^\phi$$
$$\text{width: } w = \beta^\phi$$
$$\text{resolution: } r = \gamma^\phi$$
$$\text{s.t. } \alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$$
$$\alpha \geq 1, \beta \geq 1, \gamma \geq 1$$

where $\alpha$, $\beta$, $\gamma$ are constants that can be determined by a small grid search. Intuitively, $\phi$ is a user-specified coefficient that controls how many more resources are available for model scaling, while $\alpha$, $\beta$, $\gamma$ specify how to assign these extra resources to network width, depth, and resolution respectively. Notably, the FLOPS of a regular convolution op is proportional to $d$, $w^2$, $r^2$, i.e., doubling network depth will double FLOPS, but doubling network width or resolution will increase FLOPS by four times. Since convolution ops usually dominate the computation cost in ConvNets, scaling a ConvNet with equation 3 will approximately increase total FLOPS by $(\alpha \cdot \beta^2 \cdot \gamma^2)^\phi$. In this paper, we constraint $\alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$ such that for any new $\phi$, the total FLOPS will approximately increase by $2^\phi$.

---

### النسخة العربية

#### 3.1 صياغة المسألة

يمكن تعريف طبقة الشبكة الالتفافية i على أنها دالة: Y_i = F_i(X_i)، حيث F_i هو المعامل، وY_i هو موتر المخرجات، وX_i هو موتر المدخلات، بشكل موتر <H_i, W_i, C_i>، حيث H_i وW_i هما الأبعاد المكانية، وC_i هو بُعد القناة. يمكن تعريف الشبكة الالتفافية N على أنها قائمة من الطبقات المركبة: N = F_k ⊙ ... ⊙ F_2 ⊙ F_1(X_1) = ⊙_j=1..k F_j(X_1). عملياً، غالباً ما يتم تقسيم طبقات الشبكة الالتفافية إلى مراحل متعددة وجميع الطبقات في كل مرحلة تشترك في نفس المعمارية: على سبيل المثال، لدى ResNet خمس مراحل، وجميع الطبقات في كل مرحلة لها نفس النوع الالتفافي باستثناء الطبقة الأولى التي تقوم بأخذ عينات منخفضة. لذلك، يمكننا تعريف الشبكة الالتفافية على النحو التالي:

$$N = ⊙_{i=1..s} F_i^{L_i}(X_{<H_i,W_i,C_i>})$$

حيث $F_i^{L_i}$ يشير إلى أن الطبقة $F_i$ تتكرر $L_i$ مرة في المرحلة $i$، و$<H_i, W_i, C_i>$ يشير إلى شكل موتر المدخلات X للطبقة $i$. يوضح الشكل 3(a) شبكة التفافية تمثيلية، حيث يتقلص البُعد المكاني تدريجياً ولكن بُعد القناة يتوسع عبر الطبقات، على سبيل المثال، من شكل الإدخال الأولي <224, 224, 3> إلى شكل المخرجات النهائي <7, 7, 512>.

على عكس تصميمات الشبكة الالتفافية العادية التي تركز في الغالب على إيجاد أفضل معمارية طبقة $F_i$، يحاول توسيع النموذج توسيع طول الشبكة ($L_i$)، والعرض ($C_i$)، و/أو دقة الوضوح ($H_i$، $W_i$) دون تغيير $F_i$ المحدد مسبقاً في شبكة خط الأساس. من خلال إصلاح $F_i$، يبسط توسيع النموذج مشكلة التصميم لقيود الموارد الجديدة، ولكن لا يزال هناك مساحة تصميم كبيرة لاستكشاف $L_i$ و$C_i$ و$H_i$ و$W_i$ مختلفة لكل طبقة. من أجل تقليل مساحة التصميم بشكل أكبر، نقيد أن جميع الطبقات يجب أن يتم توسيعها بشكل موحد بنسبة ثابتة. هدفنا هو تعظيم دقة النموذج لأي قيود موارد معينة، والتي يمكن صياغتها كمسألة تحسين:

$$\max_{d,w,r} \text{Accuracy}(N(d, w, r))$$
$$\text{s.t. } N(d, w, r) = ⊙_{i=1..s} \hat{F}_i^{d \cdot \hat{L}_i}(X_{<r \cdot \hat{H}_i, r \cdot \hat{W}_i, w \cdot \hat{C}_i>})$$
$$\text{Memory}(N) \leq \text{target\_memory}$$
$$\text{FLOPS}(N) \leq \text{target\_flops}$$

حيث $w$ و$d$ و$r$ هي معاملات لتوسيع عرض الشبكة وعمقها ودقة وضوحها؛ و$\hat{F}_i$ و$\hat{L}_i$ و$\hat{H}_i$ و$\hat{W}_i$ و$\hat{C}_i$ هي معاملات محددة مسبقاً في شبكة خط الأساس (انظر الجدول 1 كمثال).

#### 3.2 أبعاد التوسيع

تكمن الصعوبة الرئيسية لمسألة التحسين أعلاه في أن القيم المثلى لـ $d$ و$w$ و$r$ تعتمد على بعضها البعض والقيم تتغير في ظل قيود الموارد المختلفة. بسبب هذه الصعوبة، تقوم الطرق التقليدية في الغالب بتوسيع الشبكات الالتفافية في أحد هذه الأبعاد:

**العمق (d):** توسيع عمق الشبكة هو الطريقة الأكثر شيوعاً المستخدمة من قبل العديد من الشبكات الالتفافية. الفكرة البديهية هي أن الشبكة الالتفافية الأعمق يمكنها التقاط ميزات أكثر ثراءً وتعقيداً، وتعمم بشكل جيد على مهام جديدة. ومع ذلك، فإن الشبكات الأعمق أيضاً أكثر صعوبة في التدريب بسبب مشكلة التدرج المتلاشي. على الرغم من أن العديد من التقنيات، مثل اتصالات التخطي والتطبيع الدفعي، تخفف من مشكلة التدريب، إلا أن مكاسب الدقة للشبكات العميقة جداً تتناقص: على سبيل المثال، ResNet-1000 لديه دقة مماثلة لـ ResNet-101 على الرغم من أن لديه طبقات أكثر بكثير. يوضح الشكل 3 (الوسط) دراستنا التجريبية حول توسيع نموذج خط الأساس بمعامل عمق $d$ مختلف، مما يشير بشكل أكبر إلى عائد الدقة المتناقص للشبكات الالتفافية العميقة جداً.

**العرض (w):** يُستخدم توسيع عرض الشبكة بشكل شائع للنماذج صغيرة الحجم. كما نوقش في، تميل الشبكات الأوسع إلى أن تكون قادرة على التقاط ميزات أكثر دقة وتكون أسهل في التدريب. ومع ذلك، تميل الشبكات الواسعة للغاية ولكن الضحلة إلى مواجهة صعوبات في التقاط الميزات عالية المستوى. تُظهر نتائجنا التجريبية في الشكل 3 (اليسار) أن الدقة تتشبع بسرعة عندما تصبح الشبكات أوسع بكثير مع $w$ أكبر.

**دقة الوضوح (r):** مع صور إدخال بدقة وضوح أعلى، يمكن للشبكات الالتفافية أن تلتقط أنماطاً أكثر دقة. بدءاً من 224×224 في الشبكات الالتفافية المبكرة، تميل الشبكات الالتفافية الحديثة إلى استخدام 299×299 أو 331×331 للحصول على دقة أفضل. مؤخراً، حقق GPipe دقة ImageNet المتقدمة بدقة وضوح 480×480. تُستخدم أيضاً دقة الوضوح الأعلى، مثل 600×600، على نطاق واسع في الشبكات الالتفافية لكشف الكائنات. يوضح الشكل 3 (اليمين) أن توسيع دقة الوضوح يحسن الدقة، ولكن مكسب الدقة يتناقص لدقة الوضوح العالية جداً.

**الملاحظة 1** – توسيع أي بُعد من عرض الشبكة أو عمقها أو دقة الوضوح يحسن الدقة، ولكن مكسب الدقة يتناقص للنماذج الأكبر.

#### 3.3 التوسيع المركب

نلاحظ تجريبياً أن أبعاد التوسيع المختلفة ليست مستقلة. بشكل بديهي، بالنسبة لصور بدقة وضوح أعلى، يجب علينا زيادة عمق الشبكة، بحيث يمكن للحقول الاستقبالية الأكبر أن تساعد في التقاط ميزات مماثلة تشمل المزيد من البكسل في الصور الأكبر. وبالمثل، يجب علينا أيضاً زيادة عرض الشبكة عندما تكون دقة الوضوح أعلى، من أجل التقاط أنماط أكثر دقة مع المزيد من البكسل في الصور عالية دقة الوضوح. تشير هذه الأفكار البديهية إلى أننا بحاجة إلى تنسيق وموازنة أبعاد التوسيع المختلفة بدلاً من التوسيع التقليدي أحادي البُعد.

للتحقق من صحة أفكارنا البديهية، نقارن توسيع العرض في ظل أعماق الشبكة ودقة الوضوح المختلفة، كما هو موضح في الشكل 4. إذا قمنا فقط بتوسيع عرض الشبكة w دون تغيير العمق (d=1.0) ودقة الوضوح (r=1.0)، فإن الدقة تتشبع بسرعة. مع عمق أكبر (d=2.0) ودقة وضوح أعلى (r=2.0)، يحقق توسيع العرض دقة أفضل بكثير تحت نفس تكلفة FLOPS. تقودنا هذه النتائج إلى الملاحظة الثانية:

**الملاحظة 2** – من أجل تحقيق دقة وكفاءة أفضل، من الأهمية بمكان موازنة جميع أبعاد عرض الشبكة وعمقها ودقة الوضوح أثناء توسيع الشبكة الالتفافية.

في الواقع، حاولت بعض الأعمال السابقة بالفعل موازنة عرض الشبكة وعمقها بشكل تعسفي، لكنها جميعاً تتطلب ضبطاً يدوياً مملاً. في هذه الورقة، نقترح طريقة توسيع مركبة جديدة، تستخدم معامل مركب φ لتوسيع عرض الشبكة وعمقها ودقة وضوحها بشكل موحد بطريقة منهجية:

$$\text{depth: } d = \alpha^\phi$$
$$\text{width: } w = \beta^\phi$$
$$\text{resolution: } r = \gamma^\phi$$
$$\text{s.t. } \alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$$
$$\alpha \geq 1, \beta \geq 1, \gamma \geq 1$$

حيث $\alpha$ و$\beta$ و$\gamma$ هي ثوابت يمكن تحديدها عن طريق بحث شبكي صغير. بشكل بديهي، $\phi$ هو معامل محدد من قبل المستخدم يتحكم في عدد الموارد الإضافية المتاحة لتوسيع النموذج، بينما يحدد $\alpha$ و$\beta$ و$\gamma$ كيفية تخصيص هذه الموارد الإضافية لعرض الشبكة وعمقها ودقة وضوحها على التوالي. والجدير بالذكر أن FLOPS لعملية التفاف عادية يتناسب مع $d$ و$w^2$ و$r^2$، أي أن مضاعفة عمق الشبكة ستضاعف FLOPS، ولكن مضاعفة عرض الشبكة أو دقة الوضوح ستزيد FLOPS بمقدار أربع مرات. نظراً لأن عمليات الالتفاف عادة ما تهيمن على تكلفة الحساب في الشبكات الالتفافية، فإن توسيع الشبكة الالتفافية بالمعادلة 3 سيزيد تقريباً إجمالي FLOPS بمقدار $(\alpha \cdot \beta^2 \cdot \gamma^2)^\phi$. في هذه الورقة، نقيد $\alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$ بحيث لأي $\phi$ جديد، سيزيد إجمالي FLOPS تقريباً بمقدار $2^\phi$.

---

### Translation Notes

- **Figures referenced:** Figure 3 (scaling dimensions comparison), Figure 4 (width scaling under different depths/resolutions)
- **Key terms introduced:** Compound coefficient, grid search, vanishing gradient, skip connections, batch normalization, receptive field
- **Equations:** 7 major equations for problem formulation and compound scaling
- **Citations:** References to ResNet variants
- **Special handling:** All mathematical notation preserved in LaTeX format, tensor notation kept in English

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89

### Back-Translation (Key Formulation)

"We propose a new compound scaling method, which uses a compound coefficient φ to uniformly scale network width, depth, and resolution in a systematic way: depth: d = α^φ, width: w = β^φ, resolution: r = γ^φ, subject to α · β² · γ² ≈ 2, where α ≥ 1, β ≥ 1, γ ≥ 1, where α, β, γ are constants that can be determined by a small grid search."
