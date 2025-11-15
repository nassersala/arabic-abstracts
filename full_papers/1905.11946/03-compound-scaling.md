# Section 3: Compound Model Scaling
## القسم 3: التوسيع المركب للنموذج

**Section:** compound-scaling
**Translation Quality:** 0.88
**Glossary Terms Used:** ConvNet, layer, operator, tensor, shape, spatial dimension, channel dimension, stage, depth, width, resolution, scaling, compound coefficient, FLOPS, accuracy, vanishing gradient, batch normalization, receptive field

---

### English Version

In this section, we will formulate the scaling problem, study different approaches, and propose our new scaling method.

### 3.1. Problem Formulation

A ConvNet Layer i can be defined as a function: Yi = Fi(Xi), where Fi is the operator, Yi is output tensor, Xi is input tensor, with tensor shape <Hi, Wi, Ci>, where Hi and Wi are spatial dimension and Ci is the channel dimension. A ConvNet N can be represented by a list of composed layers: N = Fk ◦ ... ◦ F2 ◦ F1(X1) = ⊙j=1...k Fj(X1). In practice, ConvNet layers are often partitioned into multiple stages and all layers in each stage share the same architecture: for example, ResNet (He et al., 2016) has five stages, and all layers in each stage has the same convolutional type except the first layer performs down-sampling. Therefore, we can define a ConvNet as:

$$N = \bigodot_{i=1...s} F_i^{L_i} \left( X_{\langle H_i, W_i, C_i \rangle} \right)$$ ... (1)

where F^Li_i denotes layer Fi is repeated Li times in stage i, <Hi, Wi, Ci> denotes the shape of input tensor X of layer i. Figure 2(a) illustrate a representative ConvNet, where the spatial dimension is gradually shrunk but the channel dimension is expanded over layers, for example, from initial input shape <224, 224, 3> to final output shape <7, 7, 512>.

Unlike regular ConvNet designs that mostly focus on finding the best layer architecture Fi, model scaling tries to expand the network length (Li), width (Ci), and/or resolution (Hi, Wi) without changing Fi predefined in the baseline network. By fixing Fi, model scaling simplifies the design problem for new resource constraints, but it still remains a large design space to explore different Li, Ci, Hi, Wi for each layer. In order to further reduce the design space, we restrict that all layers must be scaled uniformly with constant ratio. Our target is to maximize the model accuracy for any given resource constraints, which can be formulated as an optimization problem:

$$\max_{d,w,r} \text{Accuracy}(\mathcal{N}(d, w, r))$$

$$s.t. \quad \mathcal{N}(d, w, r) = \bigodot_{i=1...s} \hat{F}_i^{d \cdot \hat{L}_i} \left( X_{\langle r \cdot \hat{H}_i, r \cdot \hat{W}_i, w \cdot \hat{C}_i \rangle} \right)$$

$$\text{Memory}(\mathcal{N}) \leq \text{target memory}$$

$$\text{FLOPS}(\mathcal{N}) \leq \text{target flops}$$ ... (2)

where w, d, r are coefficients for scaling network width, depth, and resolution; F̂i, L̂i, Ĥi, Ŵi, Ĉi are predefined parameters in baseline network (see Table 1 as an example).

### 3.2. Scaling Dimensions

The main difficulty of problem 2 is that the optimal d, w, r depend on each other and the values change under different resource constraints. Due to this difficulty, conventional methods mostly scale ConvNets in one of these dimensions:

**Depth (d):** Scaling network depth is the most common way used by many ConvNets (He et al., 2016; Huang et al., 2017; Szegedy et al., 2015; 2016). The intuition is that deeper ConvNet can capture richer and more complex features, and generalize well on new tasks. However, deeper networks are also more difficult to train due to the vanishing gradient problem (Zagoruyko & Komodakis, 2016). Although several techniques, such as skip connections (He et al., 2016) and batch normalization (Ioffe & Szegedy, 2015), alleviate the training problem, the accuracy gain of very deep network diminishes: for example, ResNet-1000 has similar accuracy as ResNet-101 even though it has much more layers. Figure 3 (middle) shows our empirical study on scaling a baseline model with different depth coefficient d, further suggesting the diminishing accuracy return for very deep ConvNets.

**Width (w):** Scaling network width is commonly used for small size models (Howard et al., 2017; Sandler et al., 2018; Tan et al., 2019). As discussed in (Zagoruyko & Komodakis, 2016), wider networks tend to be able to capture more fine-grained features and are easier to train. However, extremely wide but shallow networks tend to have difficulties in capturing higher level features. Our empirical results in Figure 3 (left) show that the accuracy quickly saturates when networks become much wider with larger w.

**Resolution (r):** With higher resolution input images, ConvNets can potentially capture more fine-grained patterns. Starting from 224x224 in early ConvNets, modern ConvNets tend to use 299x299 (Szegedy et al., 2016) or 331x331 (Zoph et al., 2018) for better accuracy. Recently, GPipe (Huang et al., 2018) achieves state-of-the-art ImageNet accuracy with 480x480 resolution. Higher resolutions, such as 600x600, are also widely used in object detection ConvNets (He et al., 2017; Lin et al., 2017). Figure 3 (right) shows the results of scaling network resolutions, where indeed higher resolutions improve accuracy, but the accuracy gain diminishes for very high resolutions (r = 1.0 denotes resolution 224x224 and r = 2.5 denotes resolution 560x560).

The above analyses lead us to the first observation:

**Observation 1** – Scaling up any dimension of network width, depth, or resolution improves accuracy, but the accuracy gain diminishes for bigger models.

### 3.3. Compound Scaling

We empirically observe that different scaling dimensions are not independent. Intuitively, for higher resolution images, we should increase network depth, such that the larger receptive fields can help capture similar features that include more pixels in bigger images. Correspondingly, we should also increase network width when resolution is higher, in order to capture more fine-grained patterns with more pixels in high resolution images. These intuitions suggest that we need to coordinate and balance different scaling dimensions rather than conventional single-dimension scaling.

To validate our intuitions, we compare width scaling under different network depths and resolutions, as shown in Figure 4. If we only scale network width w without changing depth (d=1.0) and resolution (r=1.0), the accuracy saturates quickly. With deeper (d=2.0) and higher resolution (r=2.0), width scaling achieves much better accuracy under the same FLOPS cost. These results lead us to the second observation:

**Observation 2** – In order to pursue better accuracy and efficiency, it is critical to balance all dimensions of network width, depth, and resolution during ConvNet scaling.

In fact, a few prior work (Zoph et al., 2018; Real et al., 2019) have already tried to arbitrarily balance network width and depth, but they all require tedious manual tuning.

In this paper, we propose a new **compound scaling method**, which use a compound coefficient φ to uniformly scales network width, depth, and resolution in a principled way:

depth: $d = \alpha^\phi$

width: $w = \beta^\phi$

resolution: $r = \gamma^\phi$

$$s.t. \quad \alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$$

$$\alpha \geq 1, \beta \geq 1, \gamma \geq 1$$ ... (3)

where α, β, γ are constants that can be determined by a small grid search. Intuitively, φ is a user-specified coefficient that controls how many more resources are available for model scaling, while α, β, γ specify how to assign these extra resources to network width, depth, and resolution respectively. Notably, the FLOPS of a regular convolution op is proportional to d, w², r², i.e., doubling network depth will double FLOPS, but doubling network width or resolution will increase FLOPS by four times. Since convolution ops usually dominate the computation cost in ConvNets, scaling a ConvNet with equation 3 will approximately increase total FLOPS by (α · β² · γ²)^φ. In this paper, we constraint α · β² · γ² ≈ 2 such that for any new φ, the total FLOPS will approximately increase by 2^φ.

---

### النسخة العربية

في هذا القسم، سنصيغ مشكلة التوسيع، وندرس المناهج المختلفة، ونقترح طريقة التوسيع الجديدة الخاصة بنا.

### 3.1. صياغة المشكلة

يمكن تعريف طبقة الشبكة الالتفافية i كدالة: Yi = Fi(Xi)، حيث Fi هو المعامل، وYi هو موتر المُخرجات، وXi هو موتر المُدخلات، بشكل موتر <Hi, Wi, Ci>، حيث Hi وWi هما البُعد المكاني وCi هو بُعد القناة. يمكن تمثيل الشبكة الالتفافية N بقائمة من الطبقات المُركبة: N = Fk ◦ ... ◦ F2 ◦ F1(X1) = ⊙j=1...k Fj(X1). عملياً، غالباً ما يتم تقسيم طبقات الشبكة الالتفافية إلى مراحل متعددة وتشترك جميع الطبقات في كل مرحلة في نفس المعمارية: على سبيل المثال، ResNet (He et al., 2016) لديه خمس مراحل، وجميع الطبقات في كل مرحلة لها نفس نوع الالتفاف باستثناء الطبقة الأولى التي تنفذ تقليل العينة. لذلك، يمكننا تعريف الشبكة الالتفافية على النحو التالي:

$$N = \bigodot_{i=1...s} F_i^{L_i} \left( X_{\langle H_i, W_i, C_i \rangle} \right)$$ ... (1)

حيث F^Li_i تشير إلى أن الطبقة Fi تتكرر Li مرة في المرحلة i، و<Hi, Wi, Ci> تشير إلى شكل موتر المُدخلات X للطبقة i. يوضح الشكل 2(أ) شبكة التفافية تمثيلية، حيث يتم تقليص البُعد المكاني تدريجياً ولكن يتم توسيع بُعد القناة عبر الطبقات، على سبيل المثال، من شكل المُدخلات الأولي <224, 224, 3> إلى شكل المُخرجات النهائي <7, 7, 512>.

على عكس تصاميم الشبكات الالتفافية العادية التي تركز في الغالب على إيجاد أفضل معمارية طبقة Fi، يحاول توسيع النموذج توسيع طول الشبكة (Li)، والعرض (Ci)، و/أو دقة الوضوح (Hi, Wi) دون تغيير Fi المُحدد مسبقاً في شبكة خط الأساس. من خلال إصلاح Fi، يبسط توسيع النموذج مشكلة التصميم لقيود الموارد الجديدة، لكنه لا يزال يترك مساحة تصميم كبيرة لاستكشاف Li وCi وHi وWi مختلفة لكل طبقة. من أجل تقليل مساحة التصميم بشكل أكبر، نقيد أن جميع الطبقات يجب أن يتم توسيعها بشكل موحد بنسبة ثابتة. هدفنا هو تعظيم دقة النموذج لأي قيود موارد معينة، والتي يمكن صياغتها كمشكلة تحسين:

$$\max_{d,w,r} \text{Accuracy}(\mathcal{N}(d, w, r))$$

$$s.t. \quad \mathcal{N}(d, w, r) = \bigodot_{i=1...s} \hat{F}_i^{d \cdot \hat{L}_i} \left( X_{\langle r \cdot \hat{H}_i, r \cdot \hat{W}_i, w \cdot \hat{C}_i \rangle} \right)$$

$$\text{Memory}(\mathcal{N}) \leq \text{target memory}$$

$$\text{FLOPS}(\mathcal{N}) \leq \text{target flops}$$ ... (2)

حيث w وd وr هي معاملات توسيع عرض الشبكة وعمقها ودقة الوضوح؛ F̂i وL̂i وĤi وŴi وĈi هي معاملات مُحددة مسبقاً في شبكة خط الأساس (انظر الجدول 1 كمثال).

### 3.2. أبعاد التوسيع

الصعوبة الرئيسية في المشكلة 2 هي أن d وw وr الأمثل يعتمدون على بعضهم البعض وتتغير القيم تحت قيود موارد مختلفة. بسبب هذه الصعوبة، تقوم الطرق التقليدية في الغالب بتوسيع الشبكات الالتفافية في أحد هذه الأبعاد:

**العمق (d):** توسيع عمق الشبكة هو الطريقة الأكثر شيوعاً المستخدمة من قبل العديد من الشبكات الالتفافية (He et al., 2016; Huang et al., 2017; Szegedy et al., 2015; 2016). الحدس هو أن الشبكة الالتفافية الأعمق يمكن أن تلتقط ميزات أكثر ثراءً وأكثر تعقيداً، وتعمم بشكل جيد على المهام الجديدة. ومع ذلك، فإن الشبكات الأعمق أيضاً أكثر صعوبة في التدريب بسبب مشكلة التدرج المتلاشي (Zagoruyko & Komodakis, 2016). على الرغم من أن العديد من التقنيات، مثل اتصالات التخطي (He et al., 2016) والتطبيع الدفعي (Ioffe & Szegedy, 2015)، تخفف من مشكلة التدريب، إلا أن مكسب الدقة للشبكة العميقة جداً يتناقص: على سبيل المثال، ResNet-1000 لديه دقة مماثلة لـ ResNet-101 على الرغم من أنه يحتوي على طبقات أكثر بكثير. يُظهر الشكل 3 (الوسط) دراستنا التجريبية حول توسيع نموذج خط أساس بمعامل عمق d مختلف، مما يشير بشكل أكبر إلى تناقص عائد الدقة للشبكات الالتفافية العميقة جداً.

**العرض (w):** يُستخدم توسيع عرض الشبكة بشكل شائع للنماذج ذات الحجم الصغير (Howard et al., 2017; Sandler et al., 2018; Tan et al., 2019). كما نوقش في (Zagoruyko & Komodakis, 2016)، تميل الشبكات الأوسع إلى القدرة على التقاط ميزات أكثر دقة وتكون أسهل في التدريب. ومع ذلك، فإن الشبكات الواسعة للغاية ولكن الضحلة تميل إلى مواجهة صعوبات في التقاط الميزات ذات المستوى الأعلى. تُظهر نتائجنا التجريبية في الشكل 3 (اليسار) أن الدقة تتشبع بسرعة عندما تصبح الشبكات أوسع بكثير مع w أكبر.

**دقة الوضوح (r):** مع صور مُدخلات ذات دقة وضوح أعلى، يمكن للشبكات الالتفافية التقاط أنماط أكثر دقة. بدءاً من 224×224 في الشبكات الالتفافية المبكرة، تميل الشبكات الالتفافية الحديثة إلى استخدام 299×299 (Szegedy et al., 2016) أو 331×331 (Zoph et al., 2018) للحصول على دقة أفضل. مؤخراً، حقق GPipe (Huang et al., 2018) دقة ImageNet المتقدمة بدقة وضوح 480×480. دقة الوضوح الأعلى، مثل 600×600، تُستخدم أيضاً على نطاق واسع في شبكات التفافية لكشف الأشياء (He et al., 2017; Lin et al., 2017). يُظهر الشكل 3 (اليمين) نتائج توسيع دقة الوضوح للشبكات، حيث تحسن دقة الوضوح الأعلى الدقة بالفعل، لكن مكسب الدقة يتناقص لدقة الوضوح العالية جداً (r = 1.0 تشير إلى دقة وضوح 224×224 وr = 2.5 تشير إلى دقة وضوح 560×560).

تقودنا التحليلات أعلاه إلى الملاحظة الأولى:

**الملاحظة 1** - توسيع أي بُعد من عرض الشبكة أو عمقها أو دقة الوضوح يحسن الدقة، لكن مكسب الدقة يتناقص للنماذج الأكبر.

### 3.3. التوسيع المركب

نلاحظ تجريبياً أن أبعاد التوسيع المختلفة ليست مستقلة. بشكل بديهي، للصور ذات دقة الوضوح الأعلى، يجب أن نزيد عمق الشبكة، بحيث يمكن أن تساعد مجالات الاستقبال الأكبر في التقاط ميزات مماثلة تتضمن المزيد من البكسلات في الصور الأكبر. وبالمقابل، يجب علينا أيضاً زيادة عرض الشبكة عندما تكون دقة الوضوح أعلى، من أجل التقاط أنماط أكثر دقة مع المزيد من البكسلات في صور دقة الوضوح العالية. تشير هذه الحدسيات إلى أننا بحاجة إلى تنسيق وموازنة أبعاد التوسيع المختلفة بدلاً من التوسيع التقليدي أحادي البُعد.

للتحقق من حدسياتنا، نقارن توسيع العرض تحت أعماق ودقة وضوح مختلفة للشبكة، كما هو موضح في الشكل 4. إذا قمنا بتوسيع عرض الشبكة w فقط دون تغيير العمق (d=1.0) ودقة الوضوح (r=1.0)، فإن الدقة تتشبع بسرعة. مع عمق أكبر (d=2.0) ودقة وضوح أعلى (r=2.0)، يحقق توسيع العرض دقة أفضل بكثير تحت نفس تكلفة FLOPS. تقودنا هذه النتائج إلى الملاحظة الثانية:

**الملاحظة 2** - من أجل تحقيق دقة وكفاءة أفضل، من الضروري موازنة جميع أبعاد عرض الشبكة وعمقها ودقة الوضوح أثناء توسيع الشبكة الالتفافية.

في الواقع، حاولت بعض الأعمال السابقة (Zoph et al., 2018; Real et al., 2019) بالفعل موازنة عرض الشبكة وعمقها بشكل تعسفي، لكنها جميعاً تتطلب ضبطاً يدوياً مُرهقاً.

في هذه الورقة، نقترح **طريقة توسيع مركب** جديدة، تستخدم معامل مركب φ لتوسيع عرض الشبكة وعمقها ودقة الوضوح بشكل موحد بطريقة منهجية:

العمق: $d = \alpha^\phi$

العرض: $w = \beta^\phi$

دقة الوضوح: $r = \gamma^\phi$

$$s.t. \quad \alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$$

$$\alpha \geq 1, \beta \geq 1, \gamma \geq 1$$ ... (3)

حيث α وβ وγ هي ثوابت يمكن تحديدها من خلال بحث شبكي صغير. بشكل بديهي، φ هو معامل مُحدد من قبل المستخدم يتحكم في عدد الموارد الإضافية المتاحة لتوسيع النموذج، بينما تحدد α وβ وγ كيفية تعيين هذه الموارد الإضافية لعرض الشبكة وعمقها ودقة الوضوح على التوالي. والجدير بالذكر أن FLOPS لعملية الالتفاف العادية تتناسب مع d وw² وr²، أي أن مضاعفة عمق الشبكة سيضاعف FLOPS، لكن مضاعفة عرض الشبكة أو دقة الوضوح ستزيد FLOPS بأربعة أضعاف. نظراً لأن عمليات الالتفاف عادة ما تهيمن على تكلفة الحساب في الشبكات الالتفافية، فإن توسيع شبكة التفافية بالمعادلة 3 سيزيد تقريباً إجمالي FLOPS بمقدار (α · β² · γ²)^φ. في هذه الورقة، نقيد α · β² · γ² ≈ 2 بحيث لأي φ جديد، سيزداد إجمالي FLOPS تقريباً بمقدار 2^φ.

---

### Translation Notes

- **Figures referenced:** Figure 2(a), Figure 3 (left, middle, right), Figure 4
- **Key terms introduced:** problem formulation (صياغة المشكلة), composed layers (طبقات مُركبة), down-sampling (تقليل العينة), vanishing gradient (التدرج المتلاشي), skip connections (اتصالات التخطي), compound coefficient (معامل مركب)
- **Equations:** 3 major equations (Equation 1, 2, 3)
- **Citations:** Multiple references throughout
- **Special handling:** Preserved all mathematical notation; explained Arabic technical terms after equations

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
