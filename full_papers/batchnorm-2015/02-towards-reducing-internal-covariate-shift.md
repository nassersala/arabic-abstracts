# Section 2: Towards Reducing Internal Covariate Shift
## القسم 2: نحو تقليل التحول التباين الداخلي

**Section:** Towards Reducing Internal Covariate Shift
**Translation Quality:** 0.86
**Glossary Terms Used:** internal covariate shift, normalization, training, layer, activation, gradient, whitening, covariance matrix, backpropagation, parameters

---

### English Version

We define Internal Covariate Shift as the change in the distribution of network activations due to the change in network parameters during training. To improve the training, we seek to reduce internal covariate shift. By fixing the distribution of the layer inputs $x$ as the training progresses, we expect to improve the training speed. It has been long known that the network training converges faster if its inputs are whitened – i.e., linearly transformed to have zero means and unit variances, and decorrelated. As each layer observes the inputs produced by the layers below, it would be advantageous to achieve the same whitening of the inputs of each layer. By whitening the inputs to each layer, we would take a step towards achieving the fixed distributions of inputs that would remove the ill effects of the internal covariate shift.

We could consider whitening activations at every training step or at some interval, either by modifying the network directly or by changing the parameters of the optimization algorithm to depend on the network activation values. However, if we are to use gradient descent optimization, it is important to ensure that the gradient descent step does not require updating the normalization parameters, and ideally the normalization step should not reduce the expressive power of the network. Therefore, we seek a way to perform the input normalization such that it is differentiable and does not require analyzing the entire training set after every parameter update.

Some previous approaches, such as the use of centering and normalization as preprocessing for input data, have exploited this idea. However, these preprocessing schemes cannot be applied within deep networks in a way that would make backpropagation more efficient, because they would require, for every optimization step, the computation of statistics over all training examples.

Instead, we make two necessary simplifications. The first is that instead of whitening the features in layer inputs and outputs jointly, we will normalize each scalar feature independently, by making it have the mean of zero and the variance of 1. For a layer with $d$-dimensional input $x = (x^{(1)} ... x^{(d)})$, we will normalize each dimension

$$\hat{x}^{(k)} = \frac{x^{(k)} - E[x^{(k)}]}{\sqrt{\text{Var}[x^{(k)}]}}$$

where the expectation and variance are computed over the training data set. As shown in [LeCun et al., 1998b; Wiesler & Ney, 2011], such normalization speeds up convergence, even when the features are not decorrelated.

Note that simply normalizing each input of a layer may change what the layer can represent. For instance, normalizing the inputs of a sigmoid would constrain them to the linear regime of the nonlinearity. To address this, we make sure that the transformation inserted in the network can represent the identity transform. To accomplish this, we introduce, for each activation $x^{(k)}$, a pair of parameters $γ^{(k)}$, $β^{(k)}$, which scale and shift the normalized value:

$$y^{(k)} = γ^{(k)} \hat{x}^{(k)} + β^{(k)}$$

These parameters are learned along with the original model parameters, and restore the representation power of the network. Indeed, by setting $γ^{(k)} = \sqrt{\text{Var}[x^{(k)}]}$ and $β^{(k)} = E[x^{(k)}]$, we could recover the original activations, if that were the optimal thing to do.

In the batch setting where each training step is based on the entire training set, we would use the whole set to normalize activations. However, this is impractical when using stochastic optimization. Therefore, we make the second simplification: since we use mini-batches in stochastic gradient training, each mini-batch produces estimates of the mean and variance of each activation. This way, the statistics used for normalization can fully participate in the gradient backpropagation. Note that the use of mini-batches is enabled by the computation of per-dimension variances rather than joint covariances; in the joint case, regularization would be required since the mini-batch size is likely to be smaller than the number of activations being whitened, resulting in singular covariance matrices.

Consider a mini-batch $\mathcal{B}$ of size $m$. Since the normalization is applied to each activation independently, let us focus on a particular activation $x^{(k)}$ and omit $k$ for clarity. We have $m$ values of this activation in the mini-batch,

$$\mathcal{B} = \{x_{1...m}\}$$

Let the normalized values be $\hat{x}_{1...m}$, and their linear transformations be $y_{1...m}$. We refer to the transform

$$\text{BN}_{γ,β} : x_{1...m} → y_{1...m}$$

as the Batch Normalizing Transform. We present the BN Transform in Algorithm 1. In the algorithm, $ε$ is a constant added to the mini-batch variance for numerical stability.

**Algorithm 1: Batch Normalizing Transform, applied to activation $x$ over a mini-batch**

**Input:** Values of $x$ over a mini-batch: $\mathcal{B} = \{x_1, ..., x_m\}$;
Parameters to be learned: $γ, β$

**Output:** $\{y_i = \text{BN}_{γ,β}(x_i)\}$

$$\begin{aligned}
μ_\mathcal{B} &← \frac{1}{m} \sum_{i=1}^m x_i \quad &\text{// mini-batch mean} \\
σ_\mathcal{B}^2 &← \frac{1}{m} \sum_{i=1}^m (x_i - μ_\mathcal{B})^2 \quad &\text{// mini-batch variance} \\
\hat{x}_i &← \frac{x_i - μ_\mathcal{B}}{\sqrt{σ_\mathcal{B}^2 + ε}} \quad &\text{// normalize} \\
y_i &← γ\hat{x}_i + β \equiv \text{BN}_{γ,β}(x_i) \quad &\text{// scale and shift}
\end{aligned}$$

The BN transform can be added to a network to manipulate any activation. In the notation $y = \text{BN}_{γ,β}(x)$, we indicate that the parameters $γ$ and $β$ are to be learned, but it should be noted that the BN transform does not independently process the activation in each training example. Rather, $\text{BN}_{γ,β}(x)$ depends on the training example and the other examples in the mini-batch. The scaled and shifted values $y$ are passed to other network layers. The normalized activations $\hat{x}$ are internal to our transformation, but their presence is crucial. The distributions of values of any $\hat{x}$ has the expected value of 0 and the variance of 1, as long as the elements of each mini-batch are sampled from the same distribution, and if we neglect $ε$. This holds even if the elements of $x$ themselves have not followed this distribution. As such, the inputs to each layer have stable distributions, which makes training faster.

Note that $γ$ and $β$ have the effect of rescaling and recentering the activation value. We stress that these parameters are learned jointly with the rest of the model parameters, and can thus compensate for any change introduced by normalization while providing additional representational flexibility to the model.

---

### النسخة العربية

نُعرّف التحول التباين الداخلي على أنه التغيير في توزيع تفعيلات الشبكة بسبب التغيير في معاملات الشبكة أثناء التدريب. لتحسين التدريب، نسعى لتقليل التحول التباين الداخلي. من خلال تثبيت توزيع مدخلات الطبقة $x$ مع تقدم التدريب، نتوقع تحسين سرعة التدريب. من المعروف منذ زمن طويل أن تدريب الشبكة يتقارب بشكل أسرع إذا تم تبييض مدخلاتها - أي تحويلها خطياً لتحصل على متوسطات صفرية وتباينات وحدوية، وتكون غير مترابطة. نظراً لأن كل طبقة تلاحظ المدخلات التي تنتجها الطبقات الأدنى، سيكون من المفيد تحقيق نفس التبييض لمدخلات كل طبقة. من خلال تبييض المدخلات لكل طبقة، سنخطو خطوة نحو تحقيق توزيعات ثابتة للمدخلات من شأنها إزالة التأثيرات السيئة للتحول التباين الداخلي.

يمكننا النظر في تبييض التفعيلات في كل خطوة تدريب أو على فترات معينة، إما بتعديل الشبكة مباشرة أو بتغيير معاملات خوارزمية التحسين لتعتمد على قيم تفعيل الشبكة. ومع ذلك، إذا كنا سنستخدم تحسين الانحدار التدرجي، فمن المهم التأكد من أن خطوة الانحدار التدرجي لا تتطلب تحديث معاملات التطبيع، ومن الأفضل ألا تقلل خطوة التطبيع من القدرة التعبيرية للشبكة. لذلك، نسعى إلى طريقة لإجراء تطبيع المدخلات بحيث تكون قابلة للاشتقاق ولا تتطلب تحليل مجموعة التدريب بأكملها بعد كل تحديث للمعاملات.

بعض الأساليب السابقة، مثل استخدام التمركز والتطبيع كمعالجة مسبقة لبيانات المدخلات، استغلت هذه الفكرة. ومع ذلك، لا يمكن تطبيق مخططات المعالجة المسبقة هذه داخل الشبكات العميقة بطريقة تجعل الانتشار العكسي أكثر كفاءة، لأنها ستتطلب، لكل خطوة تحسين، حساب الإحصائيات على جميع أمثلة التدريب.

بدلاً من ذلك، نُجري تبسيطين ضروريين. الأول هو أنه بدلاً من تبييض الميزات في مدخلات ومخرجات الطبقة معاً، سنطبّع كل ميزة قياسية بشكل مستقل، بجعلها تحصل على متوسط صفر وتباين 1. لطبقة بمدخل $d$ أبعاد $x = (x^{(1)} ... x^{(d)})$، سنطبّع كل بُعد

$$\hat{x}^{(k)} = \frac{x^{(k)} - E[x^{(k)}]}{\sqrt{\text{Var}[x^{(k)}]}}$$

حيث يتم حساب التوقع والتباين على مجموعة بيانات التدريب. كما هو موضح في [LeCun وآخرون، 1998b؛ Wiesler & Ney، 2011]، فإن هذا التطبيع يُسرّع التقارب، حتى عندما لا تكون الميزات غير مترابطة.

لاحظ أن مجرد تطبيع كل مدخل لطبقة قد يغير ما يمكن للطبقة تمثيله. على سبيل المثال، تطبيع مدخلات سيغمويد سيقيدها بالنظام الخطي للاخطية. لمعالجة هذا، نتأكد من أن التحويل المُدرج في الشبكة يمكنه تمثيل التحويل المطابق. لتحقيق ذلك، نُدخل، لكل تفعيل $x^{(k)}$، زوجاً من المعاملات $γ^{(k)}$، $β^{(k)}$، اللذان يُعيدان قياس القيمة المطبعة ويزيحانها:

$$y^{(k)} = γ^{(k)} \hat{x}^{(k)} + β^{(k)}$$

يتم تعلم هذه المعاملات جنباً إلى جنب مع معاملات النموذج الأصلية، وتستعيد قوة التمثيل للشبكة. في الواقع، بتعيين $γ^{(k)} = \sqrt{\text{Var}[x^{(k)}]}$ و $β^{(k)} = E[x^{(k)}]$، يمكننا استرجاع التفعيلات الأصلية، إذا كان ذلك هو الشيء الأمثل للقيام به.

في إعداد الحزمة حيث تعتمد كل خطوة تدريب على مجموعة التدريب بأكملها، سنستخدم المجموعة بأكملها لتطبيع التفعيلات. ومع ذلك، هذا غير عملي عند استخدام التحسين العشوائي. لذلك، نُجري التبسيط الثاني: نظراً لأننا نستخدم حزماً صغيرة في تدريب التدرج العشوائي، تُنتج كل حزمة صغيرة تقديرات للمتوسط والتباين لكل تفعيل. بهذه الطريقة، يمكن للإحصائيات المستخدمة للتطبيع أن تشارك بشكل كامل في الانتشار العكسي للتدرج. لاحظ أن استخدام الحزم الصغيرة مُمكّن من خلال حساب التباينات لكل بُعد بدلاً من التباينات المشتركة؛ في الحالة المشتركة، سيكون التنظيم مطلوباً نظراً لأن حجم الحزمة الصغيرة من المحتمل أن يكون أصغر من عدد التفعيلات التي يتم تبييضها، مما يؤدي إلى مصفوفات تباين مشترك متفردة.

لننظر إلى حزمة صغيرة $\mathcal{B}$ بحجم $m$. نظراً لأن التطبيع يُطبق على كل تفعيل بشكل مستقل، دعونا نركز على تفعيل معين $x^{(k)}$ ونحذف $k$ للوضوح. لدينا $m$ قيم لهذا التفعيل في الحزمة الصغيرة،

$$\mathcal{B} = \{x_{1...m}\}$$

لتكن القيم المطبعة $\hat{x}_{1...m}$، وتحويلاتها الخطية $y_{1...m}$. نشير إلى التحويل

$$\text{BN}_{γ,β} : x_{1...m} → y_{1...m}$$

باسم تحويل تطبيع الحزمة. نقدم تحويل BN في الخوارزمية 1. في الخوارزمية، $ε$ هي ثابت يُضاف إلى تباين الحزمة الصغيرة للاستقرار العددي.

**الخوارزمية 1: تحويل تطبيع الحزمة، المُطبق على التفعيل $x$ على حزمة صغيرة**

**المدخلات:** قيم $x$ على حزمة صغيرة: $\mathcal{B} = \{x_1, ..., x_m\}$؛
المعاملات التي يجب تعلمها: $γ, β$

**المخرجات:** $\{y_i = \text{BN}_{γ,β}(x_i)\}$

$$\begin{aligned}
μ_\mathcal{B} &← \frac{1}{m} \sum_{i=1}^m x_i \quad &\text{// متوسط الحزمة الصغيرة} \\
σ_\mathcal{B}^2 &← \frac{1}{m} \sum_{i=1}^m (x_i - μ_\mathcal{B})^2 \quad &\text{// تباين الحزمة الصغيرة} \\
\hat{x}_i &← \frac{x_i - μ_\mathcal{B}}{\sqrt{σ_\mathcal{B}^2 + ε}} \quad &\text{// تطبيع} \\
y_i &← γ\hat{x}_i + β \equiv \text{BN}_{γ,β}(x_i) \quad &\text{// إعادة القياس والإزاحة}
\end{aligned}$$

يمكن إضافة تحويل BN إلى شبكة لمعالجة أي تفعيل. في الترميز $y = \text{BN}_{γ,β}(x)$، نشير إلى أن المعاملات $γ$ و $β$ يجب تعلمها، ولكن يجب ملاحظة أن تحويل BN لا يعالج التفعيل بشكل مستقل في كل مثال تدريب. بدلاً من ذلك، يعتمد $\text{BN}_{γ,β}(x)$ على مثال التدريب والأمثلة الأخرى في الحزمة الصغيرة. تُمرر القيم المُعاد قياسها والمُزاحة $y$ إلى طبقات الشبكة الأخرى. التفعيلات المطبعة $\hat{x}$ داخلية لتحويلنا، لكن وجودها حاسم. توزيعات قيم أي $\hat{x}$ لها قيمة متوقعة 0 وتباين 1، طالما أن عناصر كل حزمة صغيرة مأخوذة من نفس التوزيع، وإذا أهملنا $ε$. يحدث هذا حتى لو لم تتبع عناصر $x$ نفسها هذا التوزيع. على هذا النحو، فإن مدخلات كل طبقة لها توزيعات مستقرة، مما يجعل التدريب أسرع.

لاحظ أن $γ$ و $β$ لهما تأثير إعادة قياس قيمة التفعيل وإعادة تمركزها. نؤكد أن هذه المعاملات يتم تعلمها بشكل مشترك مع باقي معاملات النموذج، وبالتالي يمكنها التعويض عن أي تغيير يُدخله التطبيع مع توفير مرونة تمثيلية إضافية للنموذج.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Whitening (التبييض)
  - Decorrelated (غير مترابطة)
  - Identity transform (التحويل المطابق)
  - Scale and shift (إعادة القياس والإزاحة)
  - Numerical stability (الاستقرار العددي)
  - Covariance matrices (مصفوفات التباين المشترك)
  - Singular matrices (مصفوفات متفردة)
- **Equations:** Multiple equations including the BN transform algorithm
- **Algorithms:** Algorithm 1 - Batch Normalizing Transform
- **Citations:** LeCun et al., 1998b; Wiesler & Ney, 2011
- **Special handling:**
  - Algorithm presented in bilingual format
  - Mathematical notation preserved
  - Technical terms consistently translated

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.87
- **Overall section score:** 0.86
