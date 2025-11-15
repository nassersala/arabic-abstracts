# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep neural networks, training, stochastic gradient descent, learning rate, parameters, layers, activation function, mini-batch, convergence, overfitting, regularization

---

### English Version

Stochastic gradient descent (SGD) has proven to be an effective way of training deep networks, and SGD variants such as momentum and Adagrad are used pervasively. SGD optimizes the parameters $\Theta$ of the network, so as to minimize the loss

$$\Theta = \arg\min_{\Theta} \frac{1}{N} \sum_{i=1}^{N} \ell(x_i, \Theta)$$

where $x_{1...N}$ is the training data set. With SGD, the training proceeds in steps, and at each step we consider a mini-batch $x_{1...m}$. The mini-batch is used to approximate the gradient of the loss function with respect to the parameters, by computing

$$\frac{1}{m} \frac{\partial \ell(x_i, \Theta)}{\partial \Theta}$$

Using mini-batches of examples, as opposed to one example at a time, is helpful in several ways. First, the gradient of the loss over a mini-batch is an estimate of the gradient over the training set, whose quality improves as the batch size increases. Second, computation over a batch can be much more efficient than $m$ computations for individual examples, due to the parallelism afforded by modern computing platforms.

While stochastic gradient is simple and effective, it requires careful tuning of the model hyper-parameters, specifically the learning rate used in optimization, as well as the initial values for the model parameters. The training is complicated by the fact that the inputs to each layer are affected by the parameters of all preceding layers – so that small changes to the network parameters amplify as the network becomes deeper.

The change in the distributions of layers' inputs presents a problem because the layers need to continuously adapt to the new distribution. When the input distribution to a learning system changes, it is said to experience covariate shift. This is typically handled via domain adaptation. However, the notion of covariate shift can be extended beyond the learning system as a whole, to apply to its parts, such as a sub-network or a layer. Consider a network computing

$$\ell = F_2(F_1(u, \Theta_1), \Theta_2)$$

where $F_1$ and $F_2$ are arbitrary transformations, and the parameters $\Theta_1$, $\Theta_2$ are to be learned so as to minimize the loss $\ell$. Learning $\Theta_2$ can be viewed as if the inputs $x = F_1(u, \Theta_1)$ are fed into the sub-network

$$\ell = F_2(x, \Theta_2)$$

For example, a gradient descent step

$$\Theta_2 \leftarrow \Theta_2 - \frac{\alpha}{m} \sum_{i=1}^{m} \frac{\partial F_2(x_i, \Theta_2)}{\partial \Theta_2}$$

(for batch size $m$ and learning rate $\alpha$) is exactly equivalent to that for a stand-alone network $F_2$ with input $x$. Therefore, the input distribution properties that make training more efficient – such as having the same distribution between the training and test data – apply to training the sub-network as well. As such, it is advantageous for the distribution of $x$ to remain fixed over time. Then, $\Theta_2$ does not have to readjust to compensate for the change in the distribution of $x$.

Fixed distribution of inputs to a sub-network would have positive consequences for the layers outside the sub-network, as well. Consider a layer with a sigmoid activation function $z = g(Wu + b)$ where $u$ is the layer input, the weight matrix $W$ and bias vector $b$ are the layer parameters to be learned, and $g(x) = \frac{1}{1+\exp(-x)}$. As $|x|$ increases, $g'(x)$ tends to zero. This means that for all dimensions of $x = Wu+b$ except those with small absolute values, the gradient flowing down to $u$ will vanish and the model will train slowly. However, since $x$ is affected by $W$, $b$ and the parameters of all the layers below, changes to those parameters during training will likely move many dimensions of $x$ into the saturated regime of the nonlinearity and slow down the convergence. This effect is amplified as the network depth increases. In practice, the saturation problem and the resulting vanishing gradients are addressed by using Rectified Linear Units (ReLU) $\text{ReLU}(x) = \max(x, 0)$, careful initialization, and small learning rates. However, if we could ensure that the distribution of nonlinearity inputs remains more stable as the network trains, then the optimizer would be less likely to get stuck in the saturated regime, and the training would accelerate.

We refer to the change in the distributions of internal nodes of a deep network, in the course of training, as Internal Covariate Shift. Eliminating it offers a promise of faster training. We propose a new mechanism, which we call Batch Normalization, that takes a step towards reducing internal covariate shift, and in doing so dramatically accelerates the training of deep neural nets. It accomplishes this via a normalization step that fixes the means and variances of layer inputs. Batch Normalization also has a beneficial effect on the gradient flow through the network, by reducing the dependence of gradients on the scale of the parameters or of their initial values. This allows us to use much higher learning rates without the risk of divergence. Furthermore, batch normalization regularizes the model and reduces the need for Dropout. Finally, Batch Normalization makes it possible to use saturating nonlinearities by preventing the network from getting stuck in the saturated modes.

In this paper, we demonstrate that Batch Normalization can be added to state-of-the-art image classification models to achieve the same accuracy in a fraction of training time. We also show that Batch Normalization allows training with saturating nonlinearities and higher learning rates. Finally, we show that a network with Batch Normalization achieves better accuracy than the best previously reported results on ImageNet classification.

---

### النسخة العربية

أثبت الانحدار التدرجي العشوائي (SGD) أنه طريقة فعالة لتدريب الشبكات العميقة، وتُستخدم متغيرات SGD مثل الزخم (Momentum) وAdagrad بشكل واسع. يقوم SGD بتحسين معاملات الشبكة $\Theta$ لتقليل دالة الخسارة:

$$\Theta = \arg\min_{\Theta} \frac{1}{N} \sum_{i=1}^{N} \ell(x_i, \Theta)$$

حيث $x_{1...N}$ هي مجموعة بيانات التدريب. مع SGD، يتقدم التدريب على خطوات، وفي كل خطوة نعتبر حزمة صغيرة (Mini-batch) $x_{1...m}$. تُستخدم الحزمة الصغيرة لتقريب تدرج دالة الخسارة بالنسبة للمعاملات، من خلال حساب:

$$\frac{1}{m} \frac{\partial \ell(x_i, \Theta)}{\partial \Theta}$$

استخدام حزم صغيرة من الأمثلة، بدلاً من مثال واحد في كل مرة، مفيد بعدة طرق. أولاً، تدرج الخسارة على حزمة صغيرة هو تقدير للتدرج على مجموعة التدريب بأكملها، وتتحسن جودته مع زيادة حجم الحزمة. ثانياً، يمكن أن تكون الحوسبة على حزمة أكثر كفاءة بكثير من $m$ حسابات للأمثلة الفردية، بسبب التوازي الذي توفره منصات الحوسبة الحديثة.

بينما الانحدار التدرجي العشوائي بسيط وفعال، إلا أنه يتطلب ضبطاً دقيقاً لمعاملات النموذج الفائقة (Hyper-parameters)، وتحديداً معدل التعلم المستخدم في التحسين، بالإضافة إلى القيم الأولية لمعاملات النموذج. يتعقد التدريب بسبب أن مدخلات كل طبقة تتأثر بمعاملات جميع الطبقات السابقة - بحيث تتضخم التغييرات الصغيرة في معاملات الشبكة مع زيادة عمق الشبكة.

يمثل التغيير في توزيعات مدخلات الطبقات مشكلة لأن الطبقات تحتاج إلى التكيف باستمرار مع التوزيع الجديد. عندما يتغير توزيع المدخلات لنظام التعلم، يُقال إنه يواجه تحولاً تبايناً (Covariate Shift). يُعالج هذا عادةً عبر تكيف المجال (Domain Adaptation). ومع ذلك، يمكن توسيع مفهوم التحول التبايني ليتجاوز نظام التعلم ككل، ليطبق على أجزائه، مثل شبكة فرعية أو طبقة. لنعتبر شبكة تحسب:

$$\ell = F_2(F_1(u, \Theta_1), \Theta_2)$$

حيث $F_1$ و $F_2$ هما تحويلات عشوائية، والمعاملات $\Theta_1$، $\Theta_2$ يجب تعلمها لتقليل الخسارة $\ell$. يمكن النظر إلى تعلم $\Theta_2$ كما لو أن المدخلات $x = F_1(u, \Theta_1)$ تُغذى إلى الشبكة الفرعية:

$$\ell = F_2(x, \Theta_2)$$

على سبيل المثال، خطوة الانحدار التدرجي:

$$\Theta_2 \leftarrow \Theta_2 - \frac{\alpha}{m} \sum_{i=1}^{m} \frac{\partial F_2(x_i, \Theta_2)}{\partial \Theta_2}$$

(لحجم حزمة $m$ ومعدل تعلم $\alpha$) تعادل تماماً تلك الخاصة بشبكة مستقلة $F_2$ مع مدخلات $x$. لذلك، فإن خصائص توزيع المدخلات التي تجعل التدريب أكثر كفاءة - مثل وجود نفس التوزيع بين بيانات التدريب والاختبار - تنطبق أيضاً على تدريب الشبكة الفرعية. وبالتالي، من المفيد أن يبقى توزيع $x$ ثابتاً مع مرور الوقت. عندئذ، لن يحتاج $\Theta_2$ إلى إعادة الضبط للتعويض عن التغيير في توزيع $x$.

سيكون للتوزيع الثابت للمدخلات إلى شبكة فرعية عواقب إيجابية على الطبقات خارج الشبكة الفرعية أيضاً. لنعتبر طبقة ذات دالة تنشيط سيغمويد $z = g(Wu + b)$ حيث $u$ هو مدخل الطبقة، ومصفوفة الأوزان $W$ ومتجه الانحياز $b$ هما معاملات الطبقة التي يجب تعلمها، و $g(x) = \frac{1}{1+\exp(-x)}$. مع زيادة $|x|$، يميل $g'(x)$ إلى الصفر. هذا يعني أنه لجميع أبعاد $x = Wu+b$ باستثناء تلك ذات القيم المطلقة الصغيرة، سيتلاشى التدرج المتدفق إلى $u$ وسيتدرب النموذج ببطء. ومع ذلك، نظراً لأن $x$ يتأثر بـ $W$ و $b$ ومعاملات جميع الطبقات أدناه، فإن التغييرات في تلك المعاملات أثناء التدريب ستنقل على الأرجح العديد من أبعاد $x$ إلى النظام المشبع للاخطية وتبطئ التقارب. يتضخم هذا التأثير مع زيادة عمق الشبكة. في الممارسة العملية، تُعالج مشكلة التشبع والتدرجات المتلاشية الناتجة باستخدام وحدات خطية مقومة (ReLU) $\text{ReLU}(x) = \max(x, 0)$، والتهيئة الدقيقة، ومعدلات تعلم صغيرة. ومع ذلك، إذا تمكنا من ضمان بقاء توزيع مدخلات اللاخطية أكثر استقراراً مع تدريب الشبكة، فإن المحسِّن سيكون أقل عرضة للتعثر في النظام المشبع، وسيتسارع التدريب.

نشير إلى التغيير في توزيعات العقد الداخلية لشبكة عميقة، أثناء التدريب، باسم التحول التبايني الداخلي (Internal Covariate Shift). القضاء عليه يقدم وعداً بتدريب أسرع. نقترح آلية جديدة، نسميها تطبيع الحزمة (Batch Normalization)، تخطو خطوة نحو تقليل التحول التبايني الداخلي، وبذلك تسرّع تدريب الشبكات العصبية العميقة بشكل كبير. تحقق ذلك عبر خطوة تطبيع تثبت متوسطات وتباينات مدخلات الطبقة. لتطبيع الحزمة أيضاً تأثير مفيد على تدفق التدرج عبر الشبكة، من خلال تقليل اعتماد التدرجات على مقياس المعاملات أو على قيمها الأولية. هذا يسمح لنا باستخدام معدلات تعلم أعلى بكثير دون خطر التباعد. علاوة على ذلك، يقوم تطبيع الحزمة بتنظيم النموذج ويقلل الحاجة إلى الإسقاط (Dropout). أخيراً، يجعل تطبيع الحزمة من الممكن استخدام اللاخطيات المشبعة عن طريق منع الشبكة من التعثر في الأوضاع المشبعة.

في هذه الورقة، نوضح أن تطبيع الحزمة يمكن إضافته إلى نماذج تصنيف الصور المتقدمة لتحقيق نفس الدقة في جزء صغير من وقت التدريب. نُظهر أيضاً أن تطبيع الحزمة يسمح بالتدريب مع اللاخطيات المشبعة ومعدلات تعلم أعلى. أخيراً، نُظهر أن الشبكة مع تطبيع الحزمة تحقق دقة أفضل من أفضل النتائج المنشورة سابقاً في تصنيف ImageNet.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Stochastic Gradient Descent (الانحدار التدرجي العشوائي)
  - Covariate Shift (التحول التبايني)
  - Internal Covariate Shift (التحول التبايني الداخلي)
  - Domain Adaptation (تكيف المجال)
  - Saturated regime (النظام المشبع)
  - Vanishing gradients (التدرجات المتلاشية)
  - ReLU (Rectified Linear Unit - وحدة خطية مقومة)
- **Equations:** 7 mathematical equations
- **Citations:** References to momentum, Adagrad, ReLU, Dropout, domain adaptation
- **Special handling:** Mathematical notation preserved in LaTeX format; technical terms provided in both English and Arabic

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
