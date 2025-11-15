# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** deep neural networks, training, stochastic gradient descent, learning rate, parameters, initialization, layer, gradient, activation, saturating nonlinearities, convergence, optimization

---

### English Version

Stochastic gradient descent (SGD) has proven to be an effective way of training deep networks, and SGD variants such as momentum and Adagrad are used by state-of-the-art systems for a variety of tasks. SGD optimizes the parameters Θ of the network, so as to minimize the loss:

$$Θ = \arg\min_Θ \frac{1}{N} \sum_{i=1}^N ℓ(x_i, Θ)$$

where $x_{1...N}$ is the training data set. With SGD, the training proceeds in steps, and at each step we consider a mini-batch $x_{1...m}$ of size m. The mini-batch is used to approximate the gradient of the loss function with respect to the parameters, by computing

$$\frac{1}{m} \frac{∂ℓ(x_i, Θ)}{∂Θ}$$

Using mini-batches of examples, as opposed to one example at a time, is helpful in several ways. First, the gradient of the loss over a mini-batch is an estimate of the gradient over the training set, whose quality improves as the batch size increases. Second, computation over a batch can be much more efficient than m computations for individual examples, due to the parallelism afforded by modern computing platforms.

While stochastic gradient descent is simple and effective, it requires careful tuning of the model hyper-parameters, specifically the learning rate used in optimization, as well as the initial values for the model parameters. The training is complicated by the fact that the inputs to each layer are affected by the parameters of all preceding layers – so that small changes to the network parameters amplify as the network becomes deeper.

The change in the distributions of layers' inputs presents a problem because the layers need to continuously adapt to the new distribution. When the input distribution to a learning system changes, it is said to experience covariate shift. This is typically handled via domain adaptation. However, the notion of covariate shift can be extended beyond the learning system as a whole, to apply to its parts, such as a sub-network or a layer. Consider a network computing

$$ℓ = F_2(F_1(u, Θ_1), Θ_2)$$

where $F_1$ and $F_2$ are arbitrary transformations, and the parameters $Θ_1$, $Θ_2$ are to be learned so as to minimize the loss $ℓ$. Learning $Θ_2$ can be viewed as if the inputs $x = F_1(u, Θ_1)$ are fed into the sub-network

$$ℓ = F_2(x, Θ_2)$$

For example, a gradient descent step

$$Θ_2 ← Θ_2 - \frac{α}{m} \sum_{i=1}^m \frac{∂F_2(x_i, Θ_2)}{∂Θ_2}$$

(for batch size m and learning rate α) is exactly equivalent to that for a stand-alone network $F_2$ with input $x$. Therefore, the input distribution properties that make training more efficient – such as having the same distribution between the training and test data – apply to training the sub-network as well. As such it is advantageous for the distribution of $x$ to remain fixed over time. Then, $Θ_2$ does not have to readjust to compensate for the change in the distribution of $x$.

Fixed distribution of inputs to a sub-network would have positive consequences for the layers outside the sub-network, as well. Consider a layer with a sigmoid activation function $z = g(Wu + b)$ where $u$ is the layer input, the weight matrix $W$ and bias vector $b$ are the layer parameters to be learned, and $g(x) = \frac{1}{1+\exp(-x)}$. As $|x|$ increases, $g'(x)$ tends to zero. This means that for all dimensions of $x = Wu + b$ except those with small absolute values, the gradient flowing down to $u$ will vanish and the model will train slowly. However, since $x$ is affected by $W$, $b$ and the parameters of all the layers below, changes to those parameters during training will likely move many dimensions of $x$ into the saturated regime of the nonlinearity and slow down the convergence. This effect is amplified as the network depth increases. In practice, the saturation problem and the resulting vanishing gradients are addressed by using Rectified Linear Units (ReLU) $\text{ReLU}(x) = \max(x, 0)$, careful initialization, and small learning rates. If, however, we could ensure that the distribution of nonlinearity inputs remains more stable as the network trains, then the optimizer would be less likely to get stuck in the saturated regime, and the training would accelerate.

We refer to the change in the distributions of internal nodes of a deep network, in the course of training, as Internal Covariate Shift. Eliminating it offers a promise of faster training. We propose a new mechanism, which we call Batch Normalization, that takes a step towards reducing internal covariate shift, and in doing so dramatically accelerates the training of deep neural nets. It accomplishes this via a normalization step that fixes the means and variances of layer inputs. Batch Normalization also has a beneficial effect on the gradient flow through the network, by reducing the dependence of gradients on the scale of the parameters or of their initial values. This allows us to use much higher learning rates without the risk of divergence. Furthermore, batch normalization regularizes the model and reduces the need for Dropout. Finally, Batch Normalization makes it possible to use saturating nonlinearities by preventing the network from getting stuck in the saturated modes.

In this work, we demonstrate that Batch Normalization achieves all of the above. We apply Batch Normalization to the best-performing ImageNet classification network, and show that we can match its performance using only 7% of the training steps, and can further exceed its accuracy by a substantial margin. Using an ensemble of such networks trained with Batch Normalization, we achieve top-5 error rate better than the best known results on ImageNet classification.

---

### النسخة العربية

أثبت الانحدار التدرجي العشوائي (SGD) أنه طريقة فعالة لتدريب الشبكات العميقة، وتُستخدم متغيرات SGD مثل الزخم و Adagrad في الأنظمة المتقدمة لمجموعة متنوعة من المهام. يحسّن SGD معاملات الشبكة Θ، بهدف تقليل دالة الخسارة:

$$Θ = \arg\min_Θ \frac{1}{N} \sum_{i=1}^N ℓ(x_i, Θ)$$

حيث $x_{1...N}$ هي مجموعة بيانات التدريب. مع SGD، يتقدم التدريب على خطوات، وفي كل خطوة نعتبر حزمة صغيرة $x_{1...m}$ بحجم m. تُستخدم الحزمة الصغيرة لتقريب تدرج دالة الخسارة فيما يتعلق بالمعاملات، من خلال حساب

$$\frac{1}{m} \frac{∂ℓ(x_i, Θ)}{∂Θ}$$

يُفيد استخدام حزم صغيرة من الأمثلة، بدلاً من مثال واحد في كل مرة، بعدة طرق. أولاً، تدرج الخسارة على الحزمة الصغيرة هو تقدير للتدرج على مجموعة التدريب، وتتحسن جودته مع زيادة حجم الحزمة. ثانياً، يمكن أن يكون الحساب على الحزمة أكثر كفاءة بكثير من m حسابات للأمثلة الفردية، بسبب التوازي الذي توفره منصات الحوسبة الحديثة.

بينما الانحدار التدرجي العشوائي بسيط وفعال، فإنه يتطلب ضبطاً دقيقاً للمعاملات الفائقة للنموذج، وتحديداً معدل التعلم المستخدم في التحسين، بالإضافة إلى القيم الأولية لمعاملات النموذج. يتعقد التدريب بسبب أن مدخلات كل طبقة تتأثر بمعاملات جميع الطبقات السابقة - بحيث تتضخم التغييرات الصغيرة في معاملات الشبكة مع زيادة عمق الشبكة.

يمثل التغيير في توزيعات مدخلات الطبقات مشكلة لأن الطبقات تحتاج إلى التكيف المستمر مع التوزيع الجديد. عندما يتغير توزيع المدخلات لنظام التعلم، يُقال إنه يواجه تحول تباين (covariate shift). يتم التعامل مع هذا عادةً عبر تكيف المجال. ومع ذلك، يمكن تمديد مفهوم تحول التباين إلى ما هو أبعد من نظام التعلم ككل، ليشمل أجزائه، مثل شبكة فرعية أو طبقة. لنأخذ شبكة تحسب

$$ℓ = F_2(F_1(u, Θ_1), Θ_2)$$

حيث $F_1$ و $F_2$ هما تحويلات تعسفية، والمعاملات $Θ_1$، $Θ_2$ يتم تعلمها لتقليل الخسارة $ℓ$. يمكن النظر إلى تعلم $Θ_2$ كما لو أن المدخلات $x = F_1(u, Θ_1)$ تُغذى إلى الشبكة الفرعية

$$ℓ = F_2(x, Θ_2)$$

على سبيل المثال، خطوة الانحدار التدرجي

$$Θ_2 ← Θ_2 - \frac{α}{m} \sum_{i=1}^m \frac{∂F_2(x_i, Θ_2)}{∂Θ_2}$$

(لحجم حزمة m ومعدل تعلم α) تعادل تماماً تلك الخاصة بشبكة مستقلة $F_2$ بمدخل $x$. لذلك، فإن خصائص توزيع المدخلات التي تجعل التدريب أكثر كفاءة - مثل وجود نفس التوزيع بين بيانات التدريب والاختبار - تنطبق على تدريب الشبكة الفرعية أيضاً. وبالتالي، من المفيد أن يبقى توزيع $x$ ثابتاً مع مرور الوقت. عندئذ، لا يحتاج $Θ_2$ إلى إعادة الضبط للتعويض عن التغيير في توزيع $x$.

سيكون للتوزيع الثابت للمدخلات إلى شبكة فرعية عواقب إيجابية على الطبقات خارج الشبكة الفرعية أيضاً. لننظر إلى طبقة بدالة تفعيل سيغمويد $z = g(Wu + b)$ حيث $u$ هو مدخل الطبقة، ومصفوفة الوزن $W$ ومتجه الانحياز $b$ هما معاملات الطبقة التي يتم تعلمها، و $g(x) = \frac{1}{1+\exp(-x)}$. مع زيادة $|x|$، يميل $g'(x)$ إلى الصفر. هذا يعني أنه بالنسبة لجميع أبعاد $x = Wu + b$ باستثناء تلك ذات القيم المطلقة الصغيرة، سيتلاشى التدرج المتدفق إلى $u$ وسيتدرب النموذج ببطء. ومع ذلك، نظراً لأن $x$ يتأثر بـ $W$ و $b$ ومعاملات جميع الطبقات الأدنى، فمن المحتمل أن تنقل التغييرات على تلك المعاملات أثناء التدريب العديد من أبعاد $x$ إلى النظام المشبع للاخطية وتبطئ التقارب. يتضخم هذا التأثير مع زيادة عمق الشبكة. في الممارسة العملية، تتم معالجة مشكلة التشبع والتدرجات المتلاشية الناتجة باستخدام وحدات خطية مُقومة (ReLU) $\text{ReLU}(x) = \max(x, 0)$، والتهيئة الدقيقة، ومعدلات التعلم الصغيرة. ومع ذلك، إذا تمكنا من ضمان أن توزيع مدخلات اللاخطية يبقى أكثر استقراراً أثناء تدريب الشبكة، فإن المحسّن سيكون أقل عرضة للتعثر في النظام المشبع، وسيتسارع التدريب.

نشير إلى التغيير في توزيعات العقد الداخلية للشبكة العميقة، أثناء التدريب، باسم التحول التباين الداخلي. إن إزالته يعد بتدريب أسرع. نقترح آلية جديدة، نسميها تطبيع الحزمة، تخطو خطوة نحو تقليل التحول التباين الداخلي، وبذلك تسرّع بشكل كبير تدريب الشبكات العصبية العميقة. يحقق ذلك عبر خطوة تطبيع تثبت متوسطات وتباينات مدخلات الطبقة. كما أن لتطبيع الحزمة تأثيراً مفيداً على تدفق التدرج عبر الشبكة، من خلال تقليل اعتماد التدرجات على مقياس المعاملات أو على قيمها الأولية. يتيح لنا ذلك استخدام معدلات تعلم أعلى بكثير دون خطر التباعد. علاوة على ذلك، يعمل تطبيع الحزمة على تنظيم النموذج ويقلل من الحاجة إلى Dropout. أخيراً، يجعل تطبيع الحزمة من الممكن استخدام اللاخطيات المشبعة من خلال منع الشبكة من التعثر في الأوضاع المشبعة.

في هذا العمل، نُظهر أن تطبيع الحزمة يحقق كل ما سبق. نطبق تطبيع الحزمة على شبكة تصنيف ImageNet الأفضل أداءً، ونُظهر أننا يمكننا مطابقة أدائها باستخدام 7% فقط من خطوات التدريب، ويمكننا أيضاً تجاوز دقتها بهامش كبير. باستخدام مجموعة من هذه الشبكات المُدربة بتطبيع الحزمة، نحقق معدل خطأ في أفضل 5 أفضل من أفضل النتائج المعروفة في تصنيف ImageNet.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Stochastic Gradient Descent (الانحدار التدرجي العشوائي)
  - Internal Covariate Shift (التحول التباين الداخلي)
  - Covariate Shift (تحول التباين)
  - Mini-batch (حزمة صغيرة)
  - Saturating nonlinearities (اللاخطيات المشبعة)
  - Vanishing gradients (التدرجات المتلاشية)
  - ReLU (وحدات خطية مُقومة)
  - Domain adaptation (تكيف المجال)
- **Equations:** 7 mathematical equations translated and preserved in LaTeX format
- **Citations:** References to Adagrad, momentum, ReLU
- **Special handling:**
  - Mathematical notation maintained throughout
  - Technical terminology consistently translated using glossary
  - Formal academic Arabic style maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87
