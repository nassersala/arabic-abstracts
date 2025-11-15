# Section 4: Batch-Normalized Convolutional Networks
## القسم 4: الشبكات الالتفافية المطبعة بالحزمة

**Section:** application
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional neural networks, batch normalization, activation function, feature maps, sigmoid, learning rate, regularization

---

### English Version

Batch Normalization can be applied to any set of activations in the network. Here, we focus on transforms that consist of an affine transformation followed by an element-wise nonlinearity:

$$z = g(Wu + b)$$

where $W$ and $b$ are learned parameters of the model, and $g(\cdot)$ is the nonlinearity such as sigmoid or ReLU. This formulation covers both fully-connected and convolutional layers. We add the BN transform immediately before the nonlinearity, by normalizing $x = Wu+b$. We could have also normalized the layer inputs $u$, but since $u$ is likely the output of another nonlinearity, the shape of its distribution is likely to change during training, and constraining its first and second moments would not eliminate the covariate shift. In contrast, $Wu+b$ is more likely to have a symmetric, non-sparse distribution, that is "more Gaussian"; normalizing it is likely to produce activations with a stable distribution.

Note that, since we normalize $Wu+b$, the bias $b$ can be ignored since its effect will be canceled by the subsequent mean subtraction (the role of the bias is subsumed by $\beta$ in Equation (3.2)). Thus, $z = g(Wu + b)$ is replaced with

$$z = g(\text{BN}(Wu))$$

where the BN transform is applied independently to each dimension of $x = Wu$, with a separate pair of learned parameters $\gamma^{(k)}$, $\beta^{(k)}$ per dimension.

For convolutional layers, we additionally want the normalization to obey the convolutional property – so that different elements of the same feature map, at different locations, are normalized in the same way. To achieve this, we jointly normalize all the activations in a mini-batch, over all locations. In Algorithm 1, we let $\mathcal{B}$ be the set of all values in a feature map across both the elements of a mini-batch and spatial locations – so for a mini-batch of size $m$ and feature maps of size $p \times q$, we use the effective mini-batch size of $m' = |\mathcal{B}| = m \cdot pq$. We learn a pair of parameters $\gamma^{(k)}$ and $\beta^{(k)}$ per feature map, rather than per activation. Algorithm 2 is modified similarly, so that during inference the BN transform applies the same linear transformation to each activation in a given feature map.

### 4.1 Batch Normalization enables higher learning rates

In traditional deep networks, too-high learning rate may result in the gradients that explode or vanish, as well as getting stuck in poor local minima. Batch Normalization helps address these issues in several ways. First, it eliminates the effect of the scale of the parameters on the gradient. To see this, consider the gradient of the loss $\ell$ with respect to some layer $i$, before normalization:

$$\frac{\partial \ell}{\partial \mathbf{u}} = \frac{\partial \ell}{\partial \mathbf{z}} \cdot g'(W\mathbf{u}) \cdot W$$

For a layer with BN:

$$\frac{\partial \ell}{\partial \mathbf{u}} = \frac{\partial \ell}{\partial \mathbf{z}} \cdot g'(\text{BN}(W\mathbf{u})) \cdot \frac{\partial \text{BN}(W\mathbf{u})}{\partial W\mathbf{u}} \cdot W$$

Crucially, $\frac{\partial \text{BN}(W\mathbf{u})}{\partial W\mathbf{u}}$ does not depend on the scale of $W$. This makes the gradient flow through the network independent of the parameter scale, which is important because changing the scale of a layer's weights does not change its output when Batch Normalization is applied. This allows us to use much higher learning rates without the risk of divergence.

Furthermore, Batch Normalization makes training more resilient to the parameter scale. This is crucial in enabling networks to learn using saturating nonlinearities such as sigmoid, which would otherwise slow down or even prevent learning. With Batch Normalization, back-propagation through a layer is unaffected by the scale of its parameters. Therefore, we do not need to be as careful about parameter initialization, and can afford to use higher learning rates.

### 4.2 Batch Normalization regularizes the model

When training with Batch Normalization, a training example is seen in conjunction with other examples in the mini-batch, and the training network no longer producing deterministic values for a given training example. In our experiments, we found that this effect acts as a regularizer, reducing (and sometimes eliminating) the need for Dropout. We find Batch Normalization to be an effective regularizer, improving the generalization of trained models.

---

### النسخة العربية

يمكن تطبيق تطبيع الحزمة على أي مجموعة من التنشيطات في الشبكة. هنا، نركز على التحويلات التي تتكون من تحويل أفيني متبوعاً بلاخطية عنصرية:

$$z = g(Wu + b)$$

حيث $W$ و $b$ هما معاملات متعلمة للنموذج، و $g(\cdot)$ هي اللاخطية مثل sigmoid أو ReLU. تغطي هذه الصيغة كلاً من الطبقات المتصلة بالكامل والطبقات الالتفافية. نضيف تحويل BN مباشرة قبل اللاخطية، من خلال تطبيع $x = Wu+b$. كان بإمكاننا أيضاً تطبيع مدخلات الطبقة $u$، ولكن نظراً لأن $u$ من المحتمل أن يكون مخرج لاخطية أخرى، فإن شكل توزيعها من المحتمل أن يتغير أثناء التدريب، وتقييد عزومها الأول والثاني لن يقضي على التحول التبايني. في المقابل، $Wu+b$ من المرجح أن يكون له توزيع متماثل، غير متناثر، وهو "أكثر غاوسية"؛ تطبيعه من المحتمل أن ينتج تنشيطات ذات توزيع مستقر.

لاحظ أنه، نظراً لأننا نطبع $Wu+b$، يمكن تجاهل الانحياز $b$ لأن تأثيره سيتم إلغاؤه بواسطة طرح المتوسط اللاحق (يتم تضمين دور الانحياز بواسطة $\beta$ في المعادلة (3.2)). وبالتالي، يتم استبدال $z = g(Wu + b)$ بـ:

$$z = g(\text{BN}(Wu))$$

حيث يتم تطبيق تحويل BN بشكل مستقل على كل بُعد من $x = Wu$، مع زوج منفصل من المعاملات المتعلمة $\gamma^{(k)}$، $\beta^{(k)}$ لكل بُعد.

بالنسبة للطبقات الالتفافية، نريد بالإضافة إلى ذلك أن يطيع التطبيع الخاصية الالتفافية - بحيث يتم تطبيع العناصر المختلفة لنفس خريطة الميزات، في مواقع مختلفة، بنفس الطريقة. لتحقيق ذلك، نقوم بتطبيع جميع التنشيطات في حزمة صغيرة بشكل مشترك، عبر جميع المواقع. في الخوارزمية 1، نجعل $\mathcal{B}$ مجموعة جميع القيم في خريطة ميزات عبر كل من عناصر الحزمة الصغيرة والمواقع المكانية - لذلك بالنسبة لحزمة صغيرة بحجم $m$ وخرائط ميزات بحجم $p \times q$، نستخدم حجم الحزمة الصغيرة الفعلي $m' = |\mathcal{B}| = m \cdot pq$. نتعلم زوجاً من المعاملات $\gamma^{(k)}$ و $\beta^{(k)}$ لكل خريطة ميزات، بدلاً من كل تنشيط. يتم تعديل الخوارزمية 2 بشكل مماثل، بحيث أثناء الاستدلال يطبق تحويل BN نفس التحويل الخطي على كل تنشيط في خريطة ميزات معينة.

### 4.1 تطبيع الحزمة يمكّن من معدلات تعلم أعلى

في الشبكات العميقة التقليدية، قد يؤدي معدل التعلم المرتفع جداً إلى تدرجات تنفجر أو تتلاشى، بالإضافة إلى التعثر في قيم دنيا محلية سيئة. يساعد تطبيع الحزمة في معالجة هذه المشكلات بعدة طرق. أولاً، يقضي على تأثير مقياس المعاملات على التدرج. لنرى ذلك، لنعتبر تدرج الخسارة $\ell$ بالنسبة لطبقة ما $i$، قبل التطبيع:

$$\frac{\partial \ell}{\partial \mathbf{u}} = \frac{\partial \ell}{\partial \mathbf{z}} \cdot g'(W\mathbf{u}) \cdot W$$

لطبقة مع BN:

$$\frac{\partial \ell}{\partial \mathbf{u}} = \frac{\partial \ell}{\partial \mathbf{z}} \cdot g'(\text{BN}(W\mathbf{u})) \cdot \frac{\partial \text{BN}(W\mathbf{u})}{\partial W\mathbf{u}} \cdot W$$

بشكل حاسم، $\frac{\partial \text{BN}(W\mathbf{u})}{\partial W\mathbf{u}}$ لا يعتمد على مقياس $W$. هذا يجعل تدفق التدرج عبر الشبكة مستقلاً عن مقياس المعاملات، وهو أمر مهم لأن تغيير مقياس أوزان الطبقة لا يغير مخرجها عند تطبيق تطبيع الحزمة. هذا يسمح لنا باستخدام معدلات تعلم أعلى بكثير دون خطر التباعد.

علاوة على ذلك، يجعل تطبيع الحزمة التدريب أكثر مرونة لمقياس المعاملات. هذا أمر بالغ الأهمية في تمكين الشبكات من التعلم باستخدام اللاخطيات المشبعة مثل sigmoid، والتي من شأنها أن تبطئ أو حتى تمنع التعلم. مع تطبيع الحزمة، لا يتأثر الانتشار العكسي عبر الطبقة بمقياس معاملاتها. لذلك، لا نحتاج إلى أن نكون حذرين بشأن تهيئة المعاملات، ويمكننا استخدام معدلات تعلم أعلى.

### 4.2 تطبيع الحزمة ينظم النموذج

عند التدريب مع تطبيع الحزمة، يُرى مثال التدريب بالتزامن مع أمثلة أخرى في الحزمة الصغيرة، ولم تعد شبكة التدريب تنتج قيماً حتمية لمثال تدريب معين. في تجاربنا، وجدنا أن هذا التأثير يعمل كمنظم، مما يقلل (وأحياناً يلغي) الحاجة إلى الإسقاط (Dropout). نجد أن تطبيع الحزمة منظم فعال، يحسن التعميم للنماذج المدربة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Element-wise nonlinearity (لاخطية عنصرية)
  - Fully-connected layers (الطبقات المتصلة بالكامل)
  - Convolutional property (الخاصية الالتفافية)
  - Spatial locations (المواقع المكانية)
  - Exploding/vanishing gradients (التدرجات المنفجرة/المتلاشية)
  - Local minima (القيم الدنيا المحلية)
  - Deterministic values (القيم الحتمية)
- **Equations:** 4 mathematical equations
- **Citations:** None explicit
- **Special handling:** Gradient flow equations explained with mathematical rigor

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
