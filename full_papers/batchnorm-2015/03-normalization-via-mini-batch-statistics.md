# Section 3: Normalization via Mini-Batch Statistics
## القسم 3: التطبيع عبر إحصائيات الحزمة الصغيرة

**Section:** Normalization via Mini-Batch Statistics
**Translation Quality:** 0.88
**Glossary Terms Used:** mini-batch, training, inference, backpropagation, gradient, layer, activation, normalization, network, parameters

---

### English Version

Since we normalize activations in a mini-batch, the statistics used for normalization are computed from that mini-batch. During training, we keep a running average of the mini-batch means and variances to use for normalization at inference time. During inference, we use the population statistics rather than mini-batch statistics.

Let us now look at batch normalization through the lens of gradient computation. The BN transform is a differentiable transformation that introduces normalized activations into the network. To train with batch normalization, we need to backpropagate the gradients through this transformation. The chain rule gives us:

$$\frac{∂ℓ}{∂\hat{x}_i} = \frac{∂ℓ}{∂y_i} · γ$$

$$\frac{∂ℓ}{∂σ_\mathcal{B}^2} = \sum_{i=1}^m \frac{∂ℓ}{∂\hat{x}_i} · (x_i - μ_\mathcal{B}) · \frac{-1}{2}(σ_\mathcal{B}^2 + ε)^{-3/2}$$

$$\frac{∂ℓ}{∂μ_\mathcal{B}} = \left(\sum_{i=1}^m \frac{∂ℓ}{∂\hat{x}_i} · \frac{-1}{\sqrt{σ_\mathcal{B}^2 + ε}}\right) + \frac{∂ℓ}{∂σ_\mathcal{B}^2} · \frac{\sum_{i=1}^m -2(x_i - μ_\mathcal{B})}{m}$$

$$\frac{∂ℓ}{∂x_i} = \frac{∂ℓ}{∂\hat{x}_i} · \frac{1}{\sqrt{σ_\mathcal{B}^2 + ε}} + \frac{∂ℓ}{∂σ_\mathcal{B}^2} · \frac{2(x_i - μ_\mathcal{B})}{m} + \frac{∂ℓ}{∂μ_\mathcal{B}} · \frac{1}{m}$$

$$\frac{∂ℓ}{∂γ} = \sum_{i=1}^m \frac{∂ℓ}{∂y_i} · \hat{x}_i$$

$$\frac{∂ℓ}{∂β} = \sum_{i=1}^m \frac{∂ℓ}{∂y_i}$$

Thus, BN transform is a differentiable transformation that introduces normalized activations into the network. This ensures that as the model trains, layers can continue learning on input distributions that exhibit less internal covariate shift, thus accelerating the training. Furthermore, the learned affine transform applied to these normalized activations allows the BN transform to represent the identity transformation and preserves the network capacity.

### 3.1 Training Batch-Normalized Networks

To Batch-Normalize a network, we specify a subset of activations and insert the BN transform for each of them, according to Alg. 1. Any layer that previously received $x$ as the input, now receives BN($x$). A model employing Batch Normalization can be trained using batch gradient descent, or Stochastic Gradient Descent with a mini-batch size $m > 1$, or with any of its variants such as Adagrad or Adam. The normalization of activations that depends on the mini-batch allows efficient training, but is neither necessary nor desirable during inference; we want the output to depend only on the input, deterministically. For this, once the network has been trained, we use the normalization

$$\hat{x} = \frac{x - E[x]}{\sqrt{\text{Var}[x] + ε}}$$

using the population, rather than mini-batch, statistics. Neglecting $ε$, these normalized activations have the same mean 0 and variance 1 as during training. We use the unbiased variance estimate $\text{Var}[x] = \frac{m}{m-1} · E_\mathcal{B}[σ_\mathcal{B}^2]$, where the expectation is over training mini-batches of size $m$ and $σ_\mathcal{B}^2$ are their sample variances. Using moving averages instead, we can track the accuracy of a model as it trains. Since the means and variances are fixed during inference, the normalization is simply a linear transform applied to each activation. It may further be composed with the scaling by $γ$ and shift by $β$, to yield a single linear transform that replaces BN($x$). Algorithm 2 summarizes the procedure for training batch-normalized networks.

**Algorithm 2: Training a Batch-Normalized Network**

**Input:** Network $N$ with trainable parameters $Θ$;
subset of activations $\{x^{(k)}\}_{k=1}^K$

$$\begin{aligned}
&N_{\text{BN}} ← N \text{ // Training batch-normalized network} \\
&\text{for } k = 1, ..., K \text{ do} \\
&\quad \text{Add transformation } y^{(k)} = \text{BN}_{γ^{(k)},β^{(k)}}(x^{(k)}) \text{ to } N_{\text{BN}} \text{ (Alg. 1)} \\
&\quad \text{Modify each layer in } N_{\text{BN}} \text{ with input } x^{(k)} \text{ to take } y^{(k)} \text{ instead} \\
&\text{end for} \\
&\text{Train } N_{\text{BN}} \text{ to optimize the parameters } Θ ∪ \{γ^{(k)}, β^{(k)}\}_{k=1}^K \\
&\text{// Inference with batch-normalized network} \\
&\text{for } k = 1, ..., K \text{ do} \\
&\quad \text{// For clarity, } x \equiv x^{(k)}, γ \equiv γ^{(k)}, β \equiv β^{(k)} \\
&\quad \text{Process multiple training mini-batches } \mathcal{B}, \text{ each of size } m, \text{ and average} \\
&\quad \text{over them:} \\
&\quad E[x] ← E_\mathcal{B}[μ_\mathcal{B}] \\
&\quad \text{Var}[x] ← \frac{m}{m-1} E_\mathcal{B}[σ_\mathcal{B}^2] \\
&\quad y ← \frac{γ}{\sqrt{\text{Var}[x] + ε}} · x + \left(β - \frac{γE[x]}{\sqrt{\text{Var}[x] + ε}}\right) \\
&\text{end for}
\end{aligned}$$

### 3.2 Batch-Normalized Convolutional Networks

Batch Normalization can be applied to any set of activations in the network. Here, we focus on transforms that consist of an affine transformation followed by an element-wise nonlinearity:

$$z = g(Wu + b)$$

where $W$ and $b$ are learned parameters of the model, and $g(·)$ is the nonlinearity such as sigmoid or ReLU. This formulation covers both fully-connected and convolutional layers. We add the BN transform immediately before the nonlinearity, by normalizing $x = Wu + b$. We could have also normalized the layer inputs $u$, but since $u$ is likely the output of another nonlinearity, the shape of its distribution is likely to change during training, and constraining its first and second moments would not eliminate the covariate shift. In contrast, $Wu + b$ is more likely to have a symmetric, non-sparse distribution, that is "more Gaussian"; normalizing it is likely to produce activations with a stable distribution.

Note that, since we normalize $Wu + b$, the bias $b$ can be ignored since its effect will be canceled by the subsequent mean subtraction (the role of the bias is subsumed by $β$ in Alg. 1). Thus, $z = g(Wu + b)$ is replaced with

$$z = g(\text{BN}(Wu))$$

where the BN transform is applied independently to each dimension of $x = Wu$, with a separate pair of learned parameters $γ^{(k)}$, $β^{(k)}$ per dimension.

For convolutional layers, we additionally want the normalization to obey the convolutional property – so that different elements of the same feature map, at different locations, are normalized in the same way. To achieve this, we jointly normalize all the activations in a mini-batch, over all locations. In Alg. 1, we let $\mathcal{B}$ be the set of all values in a feature map across both the elements of a mini-batch and spatial locations – so for a mini-batch of size $m$ and feature maps of size $p × q$, we use the effective mini-batch of size $m' = ||\mathcal{B}|| = m · pq$. We learn a pair of parameters $γ^{(k)}$ and $β^{(k)}$ per feature map, rather than per activation. Alg. 2 is modified similarly, so that during inference the BN transform applies the same linear transformation to each activation in a given feature map.

### 3.3 Batch Normalization enables higher learning rates

In traditional deep networks, too-high learning rates may result in the gradients that explode or vanish, as well as getting stuck in poor local minima. Batch Normalization helps address these issues in several ways. First, it makes the parameterization more stable. For a layer with a specific input distribution, and for any values of $γ$ and $β$, the output of $\text{BN}(Wu)$ has zero mean and unit variance. This is beneficial for gradient propagation: each layer is guaranteed to have activations with predictable distributions. Second, batch normalization makes the layer Jacobians have singular values close to 1, which is known to be beneficial for training. The reduction in internal covariate shift may also mean that we do not require dropout or other forms of regularization as much, or can employ them with less strength.

Furthermore, Batch Normalization makes it possible to use saturating nonlinearities by preventing the network from getting stuck in the saturated modes. Consider a layer with normalized inputs. As we noted earlier, since $\hat{x}$ has zero mean and unit variance, its linear combination $z = γ\hat{x} + β$ will also have a relatively bounded distribution. In contrast, without Batch Normalization, the layer inputs can have arbitrary scale and shift. As the network trains, these can move into the saturated regime of the activation function. Batch Normalization prevents this from happening, by ensuring that nonlinearities do not saturate.

---

### النسخة العربية

بما أننا نطبّع التفعيلات في حزمة صغيرة، فإن الإحصائيات المستخدمة للتطبيع تُحسب من تلك الحزمة الصغيرة. أثناء التدريب، نحتفظ بمتوسط متحرك لمتوسطات وتباينات الحزمة الصغيرة لاستخدامها للتطبيع في وقت الاستدلال. أثناء الاستدلال، نستخدم إحصائيات المجتمع بدلاً من إحصائيات الحزمة الصغيرة.

لننظر الآن إلى تطبيع الحزمة من خلال عدسة حساب التدرج. تحويل BN هو تحويل قابل للاشتقاق يُدخل تفعيلات مطبعة في الشبكة. للتدريب باستخدام تطبيع الحزمة، نحتاج إلى نشر التدرجات عكسياً عبر هذا التحويل. تعطينا قاعدة السلسلة:

$$\frac{∂ℓ}{∂\hat{x}_i} = \frac{∂ℓ}{∂y_i} · γ$$

$$\frac{∂ℓ}{∂σ_\mathcal{B}^2} = \sum_{i=1}^m \frac{∂ℓ}{∂\hat{x}_i} · (x_i - μ_\mathcal{B}) · \frac{-1}{2}(σ_\mathcal{B}^2 + ε)^{-3/2}$$

$$\frac{∂ℓ}{∂μ_\mathcal{B}} = \left(\sum_{i=1}^m \frac{∂ℓ}{∂\hat{x}_i} · \frac{-1}{\sqrt{σ_\mathcal{B}^2 + ε}}\right) + \frac{∂ℓ}{∂σ_\mathcal{B}^2} · \frac{\sum_{i=1}^m -2(x_i - μ_\mathcal{B})}{m}$$

$$\frac{∂ℓ}{∂x_i} = \frac{∂ℓ}{∂\hat{x}_i} · \frac{1}{\sqrt{σ_\mathcal{B}^2 + ε}} + \frac{∂ℓ}{∂σ_\mathcal{B}^2} · \frac{2(x_i - μ_\mathcal{B})}{m} + \frac{∂ℓ}{∂μ_\mathcal{B}} · \frac{1}{m}$$

$$\frac{∂ℓ}{∂γ} = \sum_{i=1}^m \frac{∂ℓ}{∂y_i} · \hat{x}_i$$

$$\frac{∂ℓ}{∂β} = \sum_{i=1}^m \frac{∂ℓ}{∂y_i}$$

وبالتالي، فإن تحويل BN هو تحويل قابل للاشتقاق يُدخل تفعيلات مطبعة في الشبكة. يضمن هذا أنه مع تدريب النموذج، يمكن للطبقات مواصلة التعلم على توزيعات المدخلات التي تُظهر تحولاً تبايناً داخلياً أقل، وبالتالي تسريع التدريب. علاوة على ذلك، فإن التحويل الأفيني المُتعلَّم المُطبق على هذه التفعيلات المطبعة يسمح لتحويل BN بتمثيل تحويل المطابقة ويحافظ على سعة الشبكة.

### 3.1 تدريب الشبكات المُطبّعة بالحزمة

لتطبيع شبكة بالحزمة، نحدد مجموعة فرعية من التفعيلات وندرج تحويل BN لكل منها، وفقاً للخوارزمية 1. أي طبقة كانت تستقبل $x$ كمدخل سابقاً، تستقبل الآن BN($x$). يمكن تدريب نموذج يستخدم تطبيع الحزمة باستخدام الانحدار التدرجي للحزمة، أو الانحدار التدرجي العشوائي بحجم حزمة صغيرة $m > 1$، أو باستخدام أي من متغيراته مثل Adagrad أو Adam. يسمح تطبيع التفعيلات الذي يعتمد على الحزمة الصغيرة بالتدريب الفعال، ولكنه ليس ضرورياً ولا مرغوباً أثناء الاستدلال؛ نريد أن يعتمد المخرج على المدخل فقط، بشكل حتمي. لهذا، بمجرد تدريب الشبكة، نستخدم التطبيع

$$\hat{x} = \frac{x - E[x]}{\sqrt{\text{Var}[x] + ε}}$$

باستخدام إحصائيات المجتمع، بدلاً من إحصائيات الحزمة الصغيرة. بإهمال $ε$، فإن هذه التفعيلات المطبعة لها نفس المتوسط 0 والتباين 1 كما هو الحال أثناء التدريب. نستخدم تقدير التباين غير المتحيز $\text{Var}[x] = \frac{m}{m-1} · E_\mathcal{B}[σ_\mathcal{B}^2]$، حيث التوقع على حزم التدريب الصغيرة بحجم $m$ و $σ_\mathcal{B}^2$ هي تباينات عيناتها. باستخدام المتوسطات المتحركة بدلاً من ذلك، يمكننا تتبع دقة النموذج أثناء تدريبه. نظراً لأن المتوسطات والتباينات ثابتة أثناء الاستدلال، فإن التطبيع هو ببساطة تحويل خطي يُطبق على كل تفعيل. قد يتم تركيبه بشكل أكبر مع إعادة القياس بـ $γ$ والإزاحة بـ $β$، لإنتاج تحويل خطي واحد يحل محل BN($x$). تلخص الخوارزمية 2 الإجراء لتدريب الشبكات المُطبّعة بالحزمة.

**الخوارزمية 2: تدريب شبكة مُطبّعة بالحزمة**

**المدخلات:** شبكة $N$ بمعاملات قابلة للتدريب $Θ$؛
مجموعة فرعية من التفعيلات $\{x^{(k)}\}_{k=1}^K$

$$\begin{aligned}
&N_{\text{BN}} ← N \text{ // تدريب شبكة مُطبّعة بالحزمة} \\
&\text{for } k = 1, ..., K \text{ do} \\
&\quad \text{إضافة تحويل } y^{(k)} = \text{BN}_{γ^{(k)},β^{(k)}}(x^{(k)}) \text{ إلى } N_{\text{BN}} \text{ (الخوارزمية 1)} \\
&\quad \text{تعديل كل طبقة في } N_{\text{BN}} \text{ بمدخل } x^{(k)} \text{ لتأخذ } y^{(k)} \text{ بدلاً من ذلك} \\
&\text{end for} \\
&\text{تدريب } N_{\text{BN}} \text{ لتحسين المعاملات } Θ ∪ \{γ^{(k)}, β^{(k)}\}_{k=1}^K \\
&\text{// الاستدلال مع شبكة مُطبّعة بالحزمة} \\
&\text{for } k = 1, ..., K \text{ do} \\
&\quad \text{// للوضوح، } x \equiv x^{(k)}, γ \equiv γ^{(k)}, β \equiv β^{(k)} \\
&\quad \text{معالجة حزم تدريب صغيرة متعددة } \mathcal{B}\text{، كل منها بحجم } m\text{، وحساب المتوسط} \\
&\quad \text{عبرها:} \\
&\quad E[x] ← E_\mathcal{B}[μ_\mathcal{B}] \\
&\quad \text{Var}[x] ← \frac{m}{m-1} E_\mathcal{B}[σ_\mathcal{B}^2] \\
&\quad y ← \frac{γ}{\sqrt{\text{Var}[x] + ε}} · x + \left(β - \frac{γE[x]}{\sqrt{\text{Var}[x] + ε}}\right) \\
&\text{end for}
\end{aligned}$$

### 3.2 الشبكات الالتفافية المُطبّعة بالحزمة

يمكن تطبيق تطبيع الحزمة على أي مجموعة من التفعيلات في الشبكة. هنا، نركز على التحويلات التي تتكون من تحويل أفيني يتبعه لاخطية عنصرية:

$$z = g(Wu + b)$$

حيث $W$ و $b$ هما معاملات مُتعلَّمة للنموذج، و $g(·)$ هي اللاخطية مثل سيغمويد أو ReLU. تغطي هذه الصيغة كلاً من الطبقات المتصلة بالكامل والطبقات الالتفافية. نضيف تحويل BN مباشرة قبل اللاخطية، بتطبيع $x = Wu + b$. كان يمكننا أيضاً تطبيع مدخلات الطبقة $u$، لكن نظراً لأن $u$ من المحتمل أن يكون مخرج لاخطية أخرى، فمن المحتمل أن يتغير شكل توزيعه أثناء التدريب، وتقييد عزومه الأولى والثانية لن يزيل تحول التباين. على النقيض، فإن $Wu + b$ من المرجح أن يحصل على توزيع متماثل، غير متفرق، أي "أكثر غاوسية"؛ تطبيعه من المرجح أن ينتج تفعيلات بتوزيع مستقر.

لاحظ أنه، نظراً لأننا نطبّع $Wu + b$، يمكن تجاهل الانحياز $b$ لأن تأثيره سيتم إلغاؤه بواسطة طرح المتوسط اللاحق (يتم استيعاب دور الانحياز بواسطة $β$ في الخوارزمية 1). وبالتالي، يتم استبدال $z = g(Wu + b)$ بـ

$$z = g(\text{BN}(Wu))$$

حيث يُطبق تحويل BN بشكل مستقل على كل بُعد من $x = Wu$، مع زوج منفصل من المعاملات المُتعلَّمة $γ^{(k)}$، $β^{(k)}$ لكل بُعد.

للطبقات الالتفافية، نريد بالإضافة إلى ذلك أن يطيع التطبيع الخاصية الالتفافية - بحيث تُطبّع العناصر المختلفة لنفس خريطة الميزات، في مواقع مختلفة، بنفس الطريقة. لتحقيق ذلك، نطبّع جميع التفعيلات بشكل مشترك في حزمة صغيرة، عبر جميع المواقع. في الخوارزمية 1، نجعل $\mathcal{B}$ مجموعة جميع القيم في خريطة ميزات عبر كل من عناصر الحزمة الصغيرة والمواقع المكانية - لذلك لحزمة صغيرة بحجم $m$ وخرائط ميزات بحجم $p × q$، نستخدم حجم الحزمة الصغيرة الفعلي $m' = ||\mathcal{B}|| = m · pq$. نتعلم زوجاً من المعاملات $γ^{(k)}$ و $β^{(k)}$ لكل خريطة ميزات، بدلاً من كل تفعيل. يتم تعديل الخوارزمية 2 بالمثل، بحيث أثناء الاستدلال يطبق تحويل BN نفس التحويل الخطي على كل تفعيل في خريطة ميزات معينة.

### 3.3 يُمكّن تطبيع الحزمة من معدلات تعلم أعلى

في الشبكات العميقة التقليدية، قد تؤدي معدلات التعلم العالية جداً إلى تدرجات تنفجر أو تتلاشى، بالإضافة إلى التعثر في أدنى محلية سيئة. يساعد تطبيع الحزمة في معالجة هذه المشكلات بعدة طرق. أولاً، يجعل المعاملات أكثر استقراراً. لطبقة بتوزيع مدخلات محدد، ولأي قيم لـ $γ$ و $β$، فإن مخرج $\text{BN}(Wu)$ له متوسط صفر وتباين وحدوي. هذا مفيد لنشر التدرج: كل طبقة مضمونة أن يكون لها تفعيلات بتوزيعات يمكن التنبؤ بها. ثانياً، يجعل تطبيع الحزمة الجاكوبيات للطبقة لها قيم مفردة قريبة من 1، وهو ما يُعرف أنه مفيد للتدريب. قد يعني أيضاً تقليل التحول التباين الداخلي أننا لا نتطلب dropout أو أشكال أخرى من التنظيم بنفس القدر، أو يمكننا استخدامها بقوة أقل.

علاوة على ذلك، يجعل تطبيع الحزمة من الممكن استخدام اللاخطيات المشبعة من خلال منع الشبكة من التعثر في الأوضاع المشبعة. لننظر إلى طبقة بمدخلات مطبعة. كما لاحظنا سابقاً، نظراً لأن $\hat{x}$ له متوسط صفر وتباين وحدوي، فإن تركيبته الخطية $z = γ\hat{x} + β$ سيكون له أيضاً توزيع محدود نسبياً. على النقيض، بدون تطبيع الحزمة، يمكن أن يكون لمدخلات الطبقة مقياس وإزاحة تعسفيين. مع تدريب الشبكة، يمكن أن تنتقل هذه إلى النظام المشبع لدالة التفعيل. يمنع تطبيع الحزمة حدوث ذلك، من خلال ضمان عدم تشبع اللاخطيات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Population statistics (إحصائيات المجتمع)
  - Chain rule (قاعدة السلسلة)
  - Affine transformation (تحويل أفيني)
  - Moving averages (المتوسطات المتحركة)
  - Unbiased variance estimate (تقدير التباين غير المتحيز)
  - Feature map (خريطة الميزات)
  - Fully-connected layers (الطبقات المتصلة بالكامل)
  - Convolutional property (الخاصية الالتفافية)
  - Jacobians (الجاكوبيات)
  - Singular values (القيم المفردة)
  - Exploding/vanishing gradients (التدرجات المنفجرة/المتلاشية)
- **Equations:** Multiple gradient equations and algorithms
- **Algorithms:** Algorithm 2 - Training Batch-Normalized Networks
- **Citations:** None in this section
- **Special handling:**
  - Complex mathematical derivations preserved
  - Subsections properly formatted
  - Technical terminology consistently applied

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
