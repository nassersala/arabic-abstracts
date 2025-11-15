# Section 3: Normalization via Mini-Batch Statistics
## القسم 3: التطبيع عبر إحصائيات الحزمة الصغيرة

**Section:** methodology
**Translation Quality:** 0.89
**Glossary Terms Used:** mini-batch, normalization, mean, variance, gradient, backpropagation, parameters, activation, training, inference

---

### English Version

Since the full whitening of each layer's inputs is costly and not everywhere differentiable, we make two necessary simplifications. The first is that instead of whitening the features in layer inputs and outputs jointly, we will normalize each scalar feature independently, by making it have zero mean and unit variance. For a layer with $d$-dimensional input $x = (x^{(1)} ... x^{(d)})$, we will normalize each dimension

$$\hat{x}^{(k)} = \frac{x^{(k)} - \text{E}[x^{(k)}]}{\sqrt{\text{Var}[x^{(k)}]}}$$

where the expectation and variance are computed over the training data set. As shown in LeCun et al. (1998b), such normalization speeds up convergence, even when the features are not decorrelated.

Note that simply normalizing each input of a layer may change what the layer can represent. For instance, normalizing the inputs of a sigmoid would constrain them to the linear regime of the nonlinearity. To address this, we make sure that the transformation inserted in the network can represent the identity transform. To accomplish this, we introduce, for each activation $x^{(k)}$, a pair of parameters $\gamma^{(k)}$, $\beta^{(k)}$, which scale and shift the normalized value:

$$y^{(k)} = \gamma^{(k)} \hat{x}^{(k)} + \beta^{(k)}$$

These parameters are learned along with the original model parameters, and restore the representation power of the network. Indeed, by setting $\gamma^{(k)} = \sqrt{\text{Var}[x^{(k)}]}$ and $\beta^{(k)} = \text{E}[x^{(k)}]$, we could recover the original activations, if that were the optimal thing to do.

In the batch setting where each training step is based on the entire training set, we would use the whole set to normalize activations. However, this is impractical when using stochastic optimization. Therefore, we make the second simplification: since we use mini-batches in stochastic gradient training, each mini-batch produces estimates of the mean and variance of each activation. This way, the statistics used for normalization can fully participate in the gradient backpropagation. Note that the use of mini-batches is enabled by the computation of per-dimension variances rather than joint covariances; in the joint case, regularization would be required since the mini-batch size is likely to be smaller than the number of activations being whitened, resulting in singular covariance matrices.

Consider a mini-batch $\mathcal{B}$ of size $m$. Since the normalization is applied to each activation independently, let us focus on a particular activation $x^{(k)}$ and omit $k$ for clarity. We have $m$ values of this activation in the mini-batch,

$$\mathcal{B} = \{x_{1...m}\}$$

Let the normalized values be $\hat{x}_{1...m}$, and their linear transformations be $y_{1...m}$. We refer to the transform

$$\text{BN}_{\gamma,\beta}: x_{1...m} \rightarrow y_{1...m}$$

as the Batch Normalizing Transform. We present the BN Transform in Algorithm 1. In the algorithm, $\epsilon$ is a constant added to the mini-batch variance for numerical stability.

**Algorithm 1: Batch Normalizing Transform, applied to activation $x$ over a mini-batch**

---

**Input:** Values of $x$ over a mini-batch: $\mathcal{B} = \{x_1, ..., x_m\}$;
Parameters to be learned: $\gamma, \beta$

**Output:** $\{y_i = \text{BN}_{\gamma,\beta}(x_i)\}$

$$\mu_{\mathcal{B}} \leftarrow \frac{1}{m} \sum_{i=1}^{m} x_i \quad \text{// mini-batch mean}$$

$$\sigma_{\mathcal{B}}^2 \leftarrow \frac{1}{m} \sum_{i=1}^{m} (x_i - \mu_{\mathcal{B}})^2 \quad \text{// mini-batch variance}$$

$$\hat{x}_i \leftarrow \frac{x_i - \mu_{\mathcal{B}}}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}} \quad \text{// normalize}$$

$$y_i \leftarrow \gamma \hat{x}_i + \beta \equiv \text{BN}_{\gamma,\beta}(x_i) \quad \text{// scale and shift}$$

---

The BN transform can be added to a network to manipulate any activation. In the notation $y = \text{BN}_{\gamma,\beta}(x)$, we indicate that the parameters $\gamma$ and $\beta$ are to be learned, but it should be noted that the BN transform does not independently process the activation in each training example. Rather, $\text{BN}_{\gamma,\beta}(x)$ depends both on the training example and the other examples in the mini-batch. The scaled and shifted values $y$ are passed to other network layers. The normalized activations $\hat{x}$ are internal to our transformation, but their presence is crucial. The distributions of values of any $\hat{x}$ has the expected value of 0 and the variance of 1, as long as the elements of each mini-batch are sampled from the same distribution, and if we neglect $\epsilon$. This holds even if the $x$ values have some other distribution. Each $\hat{x}^{(k)}$ can thus be viewed as an input to a sub-network composed of the linear transform $y^{(k)} = \gamma^{(k)} \hat{x}^{(k)} + \beta^{(k)}$, followed by the other processing done by the original network. These sub-network inputs all have fixed means and variances, and although the joint distribution of these normalized $\hat{x}^{(k)}$ can change over the course of training, we expect that the introduction of normalized inputs accelerates the training of the sub-network and, consequently, the network as a whole.

During training we need to backpropagate the gradient of loss $\ell$ through this transformation, as well as compute the gradients with respect to the parameters of the BN transform. We use chain rule, as follows (before simplification):

$$\frac{\partial \ell}{\partial \hat{x}_i} = \frac{\partial \ell}{\partial y_i} \cdot \gamma$$

$$\frac{\partial \ell}{\partial \sigma_{\mathcal{B}}^2} = \sum_{i=1}^{m} \frac{\partial \ell}{\partial \hat{x}_i} \cdot (x_i - \mu_{\mathcal{B}}) \cdot \frac{-1}{2}(\sigma_{\mathcal{B}}^2 + \epsilon)^{-3/2}$$

$$\frac{\partial \ell}{\partial \mu_{\mathcal{B}}} = \left(\sum_{i=1}^{m} \frac{\partial \ell}{\partial \hat{x}_i} \cdot \frac{-1}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}}\right) + \frac{\partial \ell}{\partial \sigma_{\mathcal{B}}^2} \cdot \frac{\sum_{i=1}^{m} -2(x_i - \mu_{\mathcal{B}})}{m}$$

$$\frac{\partial \ell}{\partial x_i} = \frac{\partial \ell}{\partial \hat{x}_i} \cdot \frac{1}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}} + \frac{\partial \ell}{\partial \sigma_{\mathcal{B}}^2} \cdot \frac{2(x_i - \mu_{\mathcal{B}})}{m} + \frac{\partial \ell}{\partial \mu_{\mathcal{B}}} \cdot \frac{1}{m}$$

$$\frac{\partial \ell}{\partial \gamma} = \sum_{i=1}^{m} \frac{\partial \ell}{\partial y_i} \cdot \hat{x}_i$$

$$\frac{\partial \ell}{\partial \beta} = \sum_{i=1}^{m} \frac{\partial \ell}{\partial y_i}$$

Thus, BN transform is a differentiable transformation that introduces normalized activations into the network. This ensures that as the model is training, layers can continue learning on input distributions that exhibit less internal covariate shift, thus accelerating the training. Furthermore, the learned affine transform applied to these normalized activations allows the BN transform to represent the identity transformation and preserves the network capacity.

### 3.1 Training and Inference with Batch-Normalized Networks

To Batch-Normalize a network, we specify a subset of activations and insert the BN transform for each of them, according to Algorithm 1. Any layer that previously received $x$ as the input, now receives $\text{BN}(x)$. A model employing Batch Normalization can be trained using batch gradient descent, or Stochastic Gradient Descent with a mini-batch size $m > 1$, or with any of its variants such as Adagrad (Duchi et al., 2011) or Adam (Kingma & Ba, 2014). The normalization of activations that depends on the mini-batch allows efficient training, but is neither necessary nor desirable during inference; we want the output to depend only on the input, deterministically. For this, once the network has been trained, we use the normalization

$$\hat{x} = \frac{x - \text{E}[x]}{\sqrt{\text{Var}[x] + \epsilon}}$$

using the population, rather than mini-batch, statistics. Neglecting $\epsilon$, these normalized activations have the same mean 0 and variance 1 as during training. We use the unbiased variance estimate $\text{Var}[x] = \frac{m}{m-1} \cdot \text{E}_{\mathcal{B}}[\sigma_{\mathcal{B}}^2]$, where the expectation is over training mini-batches of size $m$ and $\sigma_{\mathcal{B}}^2$ are their sample variances. Using moving averages instead, we can track the accuracy of a model as it trains. Since the means and variances are fixed during inference, the normalization is simply a linear transform applied to each activation. It may further be composed with the scaling by $\gamma$ and shift by $\beta$, to yield a single linear transform that replaces $\text{BN}(x)$. Algorithm 2 summarizes the procedure for training batch-normalized networks.

**Algorithm 2: Training a Batch-Normalized Network**

---

**Input:** Network $N$ with trainable parameters $\Theta$;
subset of activations $\{x^{(k)}\}_{k=1}^{K}$

1. $N_{\text{BN}} \leftarrow N$ // Training BN network
2. **for** $k = 1, ..., K$ **do**
3. $\quad$ Add transformation $y^{(k)} = \text{BN}_{\gamma^{(k)},\beta^{(k)}}(x^{(k)})$ to $N_{\text{BN}}$ (Algorithm 1)
4. $\quad$ Modify each layer in $N_{\text{BN}}$ with input $x^{(k)}$ to take $y^{(k)}$ instead
5. **end for**
6. Train $N_{\text{BN}}$ to optimize the parameters $\Theta \cup \{\gamma^{(k)}, \beta^{(k)}\}_{k=1}^{K}$
7. $N_{\text{BN}}^{\text{Inf}} \leftarrow N_{\text{BN}}$ // Inference BN network with frozen parameters
8. **for** $k = 1, ..., K$ **do**
9. $\quad$ // For clarity, $x \equiv x^{(k)}$, $\gamma \equiv \gamma^{(k)}$, $\beta \equiv \beta^{(k)}$
10. $\quad$ Process multiple training mini-batches $\mathcal{B}$, each of size $m$, and average over them:
11. $\quad$ $\text{E}[x] \leftarrow \text{E}_{\mathcal{B}}[\mu_{\mathcal{B}}]$
12. $\quad$ $\text{Var}[x] \leftarrow \frac{m}{m-1} \text{E}_{\mathcal{B}}[\sigma_{\mathcal{B}}^2]$
13. $\quad$ In $N_{\text{BN}}^{\text{Inf}}$, replace the transform $y = \text{BN}_{\gamma,\beta}(x)$ with $y = \frac{\gamma}{\sqrt{\text{Var}[x] + \epsilon}} \cdot x + \left(\beta - \frac{\gamma \text{E}[x]}{\sqrt{\text{Var}[x] + \epsilon}}\right)$
14. **end for**

---

### النسخة العربية

نظراً لأن التبييض الكامل لمدخلات كل طبقة مكلف وليس قابلاً للتفاضل في كل مكان، نقوم بتبسيطين ضروريين. الأول هو أنه بدلاً من تبييض الميزات في مدخلات ومخرجات الطبقة معاً، سنقوم بتطبيع كل ميزة عددية بشكل مستقل، من خلال جعلها ذات متوسط صفري وتباين أحادي. لطبقة ذات مدخل $d$-الأبعاد $x = (x^{(1)} ... x^{(d)})$، سنقوم بتطبيع كل بُعد:

$$\hat{x}^{(k)} = \frac{x^{(k)} - \text{E}[x^{(k)}]}{\sqrt{\text{Var}[x^{(k)}]}}$$

حيث يتم حساب القيمة المتوقعة والتباين على مجموعة بيانات التدريب. كما هو موضح في LeCun et al. (1998b)، فإن هذا التطبيع يسرّع التقارب، حتى عندما لا تكون الميزات غير مرتبطة.

لاحظ أن مجرد تطبيع كل مدخل لطبقة قد يغير ما يمكن أن تمثله الطبقة. على سبيل المثال، تطبيع مدخلات دالة سيغمويد سيقيدها إلى النظام الخطي للاخطية. لمعالجة هذا، نتأكد من أن التحويل المُدرج في الشبكة يمكنه تمثيل تحويل الهوية (Identity Transform). لتحقيق ذلك، نقدم، لكل تنشيط $x^{(k)}$، زوجاً من المعاملات $\gamma^{(k)}$، $\beta^{(k)}$، اللذان يقومان بقياس وإزاحة القيمة المطبعة:

$$y^{(k)} = \gamma^{(k)} \hat{x}^{(k)} + \beta^{(k)}$$

يتم تعلم هذه المعاملات جنباً إلى جنب مع معاملات النموذج الأصلية، وتستعيد قوة التمثيل للشبكة. في الواقع، من خلال تعيين $\gamma^{(k)} = \sqrt{\text{Var}[x^{(k)}]}$ و $\beta^{(k)} = \text{E}[x^{(k)}]$، يمكننا استعادة التنشيطات الأصلية، إذا كان ذلك هو الشيء الأمثل للقيام به.

في إعداد الحزمة حيث تعتمد كل خطوة تدريب على مجموعة التدريب بأكملها، سنستخدم المجموعة بأكملها لتطبيع التنشيطات. ومع ذلك، هذا غير عملي عند استخدام التحسين العشوائي. لذلك، نقوم بالتبسيط الثاني: نظراً لأننا نستخدم الحزم الصغيرة في التدريب بالانحدار التدرجي العشوائي، تنتج كل حزمة صغيرة تقديرات للمتوسط والتباين لكل تنشيط. بهذه الطريقة، يمكن للإحصائيات المستخدمة في التطبيع أن تشارك بالكامل في الانتشار العكسي للتدرج. لاحظ أن استخدام الحزم الصغيرة يتم تمكينه من خلال حساب التباينات لكل بُعد بدلاً من التباينات المشتركة؛ في الحالة المشتركة، سيكون التنظيم مطلوباً حيث من المحتمل أن يكون حجم الحزمة الصغيرة أصغر من عدد التنشيطات التي يتم تبييضها، مما يؤدي إلى مصفوفات تباين متفردة.

لنعتبر حزمة صغيرة $\mathcal{B}$ بحجم $m$. نظراً لأن التطبيع يُطبق على كل تنشيط بشكل مستقل، دعونا نركز على تنشيط معين $x^{(k)}$ ونحذف $k$ من أجل الوضوح. لدينا $m$ قيمة لهذا التنشيط في الحزمة الصغيرة:

$$\mathcal{B} = \{x_{1...m}\}$$

لتكن القيم المطبعة $\hat{x}_{1...m}$، وتحويلاتها الخطية $y_{1...m}$. نشير إلى التحويل:

$$\text{BN}_{\gamma,\beta}: x_{1...m} \rightarrow y_{1...m}$$

باسم تحويل تطبيع الحزمة (Batch Normalizing Transform). نقدم تحويل BN في الخوارزمية 1. في الخوارزمية، $\epsilon$ هو ثابت يُضاف إلى تباين الحزمة الصغيرة من أجل الاستقرار العددي.

**الخوارزمية 1: تحويل تطبيع الحزمة، المطبق على التنشيط $x$ على حزمة صغيرة**

---

**المدخل:** قيم $x$ على حزمة صغيرة: $\mathcal{B} = \{x_1, ..., x_m\}$;
المعاملات التي سيتم تعلمها: $\gamma, \beta$

**المخرج:** $\{y_i = \text{BN}_{\gamma,\beta}(x_i)\}$

$$\mu_{\mathcal{B}} \leftarrow \frac{1}{m} \sum_{i=1}^{m} x_i \quad \text{// متوسط الحزمة الصغيرة}$$

$$\sigma_{\mathcal{B}}^2 \leftarrow \frac{1}{m} \sum_{i=1}^{m} (x_i - \mu_{\mathcal{B}})^2 \quad \text{// تباين الحزمة الصغيرة}$$

$$\hat{x}_i \leftarrow \frac{x_i - \mu_{\mathcal{B}}}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}} \quad \text{// التطبيع}$$

$$y_i \leftarrow \gamma \hat{x}_i + \beta \equiv \text{BN}_{\gamma,\beta}(x_i) \quad \text{// القياس والإزاحة}$$

---

يمكن إضافة تحويل BN إلى الشبكة للتعامل مع أي تنشيط. في الترميز $y = \text{BN}_{\gamma,\beta}(x)$، نشير إلى أن المعاملات $\gamma$ و $\beta$ يجب تعلمها، ولكن يجب ملاحظة أن تحويل BN لا يعالج التنشيط بشكل مستقل في كل مثال تدريب. بدلاً من ذلك، يعتمد $\text{BN}_{\gamma,\beta}(x)$ على كل من مثال التدريب والأمثلة الأخرى في الحزمة الصغيرة. تُمرر القيم المقاسة والمزاحة $y$ إلى طبقات الشبكة الأخرى. التنشيطات المطبعة $\hat{x}$ داخلية لتحويلنا، لكن وجودها حاسم. توزيعات قيم أي $\hat{x}$ لها قيمة متوقعة 0 وتباين 1، طالما يتم أخذ عينات من عناصر كل حزمة صغيرة من نفس التوزيع، وإذا تجاهلنا $\epsilon$. هذا صحيح حتى لو كانت قيم $x$ لها توزيع آخر. يمكن النظر إلى كل $\hat{x}^{(k)}$ على أنه مدخل إلى شبكة فرعية تتكون من التحويل الخطي $y^{(k)} = \gamma^{(k)} \hat{x}^{(k)} + \beta^{(k)}$، متبوعاً بالمعالجة الأخرى التي تقوم بها الشبكة الأصلية. جميع مدخلات الشبكة الفرعية هذه لها متوسطات وتباينات ثابتة، وعلى الرغم من أن التوزيع المشترك لهذه $\hat{x}^{(k)}$ المطبعة يمكن أن يتغير خلال التدريب، فإننا نتوقع أن إدخال المدخلات المطبعة يسرّع تدريب الشبكة الفرعية، وبالتالي الشبكة ككل.

أثناء التدريب نحتاج إلى إجراء الانتشار العكسي لتدرج الخسارة $\ell$ من خلال هذا التحويل، وكذلك حساب التدرجات بالنسبة لمعاملات تحويل BN. نستخدم قاعدة السلسلة، على النحو التالي (قبل التبسيط):

$$\frac{\partial \ell}{\partial \hat{x}_i} = \frac{\partial \ell}{\partial y_i} \cdot \gamma$$

$$\frac{\partial \ell}{\partial \sigma_{\mathcal{B}}^2} = \sum_{i=1}^{m} \frac{\partial \ell}{\partial \hat{x}_i} \cdot (x_i - \mu_{\mathcal{B}}) \cdot \frac{-1}{2}(\sigma_{\mathcal{B}}^2 + \epsilon)^{-3/2}$$

$$\frac{\partial \ell}{\partial \mu_{\mathcal{B}}} = \left(\sum_{i=1}^{m} \frac{\partial \ell}{\partial \hat{x}_i} \cdot \frac{-1}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}}\right) + \frac{\partial \ell}{\partial \sigma_{\mathcal{B}}^2} \cdot \frac{\sum_{i=1}^{m} -2(x_i - \mu_{\mathcal{B}})}{m}$$

$$\frac{\partial \ell}{\partial x_i} = \frac{\partial \ell}{\partial \hat{x}_i} \cdot \frac{1}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}} + \frac{\partial \ell}{\partial \sigma_{\mathcal{B}}^2} \cdot \frac{2(x_i - \mu_{\mathcal{B}})}{m} + \frac{\partial \ell}{\partial \mu_{\mathcal{B}}} \cdot \frac{1}{m}$$

$$\frac{\partial \ell}{\partial \gamma} = \sum_{i=1}^{m} \frac{\partial \ell}{\partial y_i} \cdot \hat{x}_i$$

$$\frac{\partial \ell}{\partial \beta} = \sum_{i=1}^{m} \frac{\partial \ell}{\partial y_i}$$

وبالتالي، فإن تحويل BN هو تحويل قابل للتفاضل يُدخل تنشيطات مطبعة إلى الشبكة. هذا يضمن أنه مع تدريب النموذج، يمكن للطبقات الاستمرار في التعلم على توزيعات المدخلات التي تظهر تحولاً تبايناً داخلياً أقل، وبالتالي تسريع التدريب. علاوة على ذلك، فإن التحويل الأفيني المتعلم المطبق على هذه التنشيطات المطبعة يسمح لتحويل BN بتمثيل تحويل الهوية ويحافظ على سعة الشبكة.

### 3.1 التدريب والاستدلال مع الشبكات المطبعة بالحزمة

لتطبيع شبكة بالحزمة، نحدد مجموعة فرعية من التنشيطات وندرج تحويل BN لكل منها، وفقاً للخوارزمية 1. أي طبقة كانت تتلقى سابقاً $x$ كمدخل، تتلقى الآن $\text{BN}(x)$. يمكن تدريب نموذج يستخدم تطبيع الحزمة باستخدام الانحدار التدرجي للحزمة، أو الانحدار التدرجي العشوائي بحجم حزمة صغيرة $m > 1$، أو مع أي من متغيراته مثل Adagrad (Duchi et al., 2011) أو Adam (Kingma & Ba, 2014). تطبيع التنشيطات الذي يعتمد على الحزمة الصغيرة يسمح بالتدريب الفعال، لكنه ليس ضرورياً ولا مرغوباً فيه أثناء الاستدلال؛ نريد أن يعتمد المخرج فقط على المدخل، بشكل حتمي. لهذا، بمجرد تدريب الشبكة، نستخدم التطبيع:

$$\hat{x} = \frac{x - \text{E}[x]}{\sqrt{\text{Var}[x] + \epsilon}}$$

باستخدام إحصائيات السكان، بدلاً من إحصائيات الحزمة الصغيرة. بإهمال $\epsilon$، فإن هذه التنشيطات المطبعة لها نفس المتوسط 0 والتباين 1 كما هو الحال أثناء التدريب. نستخدم تقدير التباين غير المتحيز $\text{Var}[x] = \frac{m}{m-1} \cdot \text{E}_{\mathcal{B}}[\sigma_{\mathcal{B}}^2]$، حيث القيمة المتوقعة هي على حزم التدريب الصغيرة بحجم $m$ و $\sigma_{\mathcal{B}}^2$ هي تباينات عيناتها. باستخدام المتوسطات المتحركة بدلاً من ذلك، يمكننا تتبع دقة النموذج أثناء تدريبه. نظراً لأن المتوسطات والتباينات ثابتة أثناء الاستدلال، فإن التطبيع هو ببساطة تحويل خطي مطبق على كل تنشيط. قد يتم تركيبه أيضاً مع القياس بواسطة $\gamma$ والإزاحة بواسطة $\beta$، لإنتاج تحويل خطي واحد يحل محل $\text{BN}(x)$. تلخص الخوارزمية 2 إجراء تدريب الشبكات المطبعة بالحزمة.

**الخوارزمية 2: تدريب شبكة مطبعة بالحزمة**

---

**المدخل:** شبكة $N$ مع معاملات قابلة للتدريب $\Theta$;
مجموعة فرعية من التنشيطات $\{x^{(k)}\}_{k=1}^{K}$

1. $N_{\text{BN}} \leftarrow N$ // شبكة BN للتدريب
2. **لـ** $k = 1, ..., K$ **افعل**
3. $\quad$ أضف التحويل $y^{(k)} = \text{BN}_{\gamma^{(k)},\beta^{(k)}}(x^{(k)})$ إلى $N_{\text{BN}}$ (الخوارزمية 1)
4. $\quad$ عدّل كل طبقة في $N_{\text{BN}}$ مع مدخل $x^{(k)}$ لتأخذ $y^{(k)}$ بدلاً من ذلك
5. **نهاية لـ**
6. درّب $N_{\text{BN}}$ لتحسين المعاملات $\Theta \cup \{\gamma^{(k)}, \beta^{(k)}\}_{k=1}^{K}$
7. $N_{\text{BN}}^{\text{Inf}} \leftarrow N_{\text{BN}}$ // شبكة BN للاستدلال مع معاملات مجمدة
8. **لـ** $k = 1, ..., K$ **افعل**
9. $\quad$ // من أجل الوضوح، $x \equiv x^{(k)}$، $\gamma \equiv \gamma^{(k)}$، $\beta \equiv \beta^{(k)}$
10. $\quad$ عالج عدة حزم تدريب صغيرة $\mathcal{B}$، كل منها بحجم $m$، وخذ المتوسط عليها:
11. $\quad$ $\text{E}[x] \leftarrow \text{E}_{\mathcal{B}}[\mu_{\mathcal{B}}]$
12. $\quad$ $\text{Var}[x] \leftarrow \frac{m}{m-1} \text{E}_{\mathcal{B}}[\sigma_{\mathcal{B}}^2]$
13. $\quad$ في $N_{\text{BN}}^{\text{Inf}}$، استبدل التحويل $y = \text{BN}_{\gamma,\beta}(x)$ بـ $y = \frac{\gamma}{\sqrt{\text{Var}[x] + \epsilon}} \cdot x + \left(\beta - \frac{\gamma \text{E}[x]}{\sqrt{\text{Var}[x] + \epsilon}}\right)$
14. **نهاية لـ**

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Identity transform (تحويل الهوية)
  - Scale and shift (القياس والإزاحة)
  - Affine transform (التحويل الأفيني)
  - Population statistics (إحصائيات السكان)
  - Moving averages (المتوسطات المتحركة)
  - Unbiased variance estimate (تقدير التباين غير المتحيز)
- **Equations:** 14 mathematical equations
- **Algorithms:** 2 algorithms (BN Transform, Training BN Networks)
- **Citations:** LeCun et al., 1998b; Duchi et al., 2011; Kingma & Ba, 2014
- **Special handling:** Algorithms translated with code comments in Arabic; mathematical notation preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
