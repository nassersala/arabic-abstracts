# Section 4: Related Work
## القسم 4: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** stochastic gradient descent, learning rate, adaptive methods, momentum, optimization

---

### English Version

#### Stochastic Gradient Descent (SGD)

The most popular optimization algorithm in machine learning is stochastic gradient descent (SGD). In its basic form, SGD updates parameters by moving in the direction of the negative gradient:

$$\theta_{t+1} = \theta_t - \alpha \nabla f_t(\theta_t)$$

where $\alpha$ is a fixed learning rate. While SGD is simple and effective for many problems, it has several limitations. The choice of learning rate is critical: too large and the algorithm will diverge, too small and convergence will be very slow. Additionally, SGD uses the same learning rate for all parameters, which can be inefficient when parameters have different sensitivities.

#### Momentum Methods

To address some of SGD's limitations, momentum methods maintain a moving average of past gradients:

$$v_t = \gamma v_{t-1} + \alpha \nabla f_t(\theta_t)$$
$$\theta_{t+1} = \theta_t - v_t$$

where $\gamma$ is the momentum coefficient, typically set around 0.9. Momentum helps accelerate SGD in relevant directions and dampens oscillations. Nesterov's accelerated gradient (NAG) is a variant that achieves better convergence rates for convex problems.

#### AdaGrad

AdaGrad is an adaptive learning rate method that adapts the learning rate for each parameter based on the historical gradient information:

$$\theta_{t+1,i} = \theta_{t,i} - \frac{\alpha}{\sqrt{G_{t,ii} + \epsilon}} g_{t,i}$$

where $G_t = \sum_{\tau=1}^t g_\tau g_\tau^T$ is the sum of outer products of all historical gradients, and $g_{t,i}$ is the partial derivative w.r.t. the $i$-th parameter at time $t$. AdaGrad performs larger updates for infrequent parameters and smaller updates for frequent parameters, making it well-suited for sparse data.

However, AdaGrad's main weakness is that the learning rate monotonically decreases during training due to the accumulation of squared gradients in the denominator. In non-convex settings like deep learning, this can cause the learning rate to become infinitesimally small before reaching a good solution.

#### RMSProp

RMSProp was proposed to address AdaGrad's diminishing learning rates. Instead of accumulating all past squared gradients, RMSProp uses an exponentially decaying average:

$$v_t = \beta v_{t-1} + (1-\beta) g_t^2$$
$$\theta_{t+1} = \theta_t - \frac{\alpha}{\sqrt{v_t + \epsilon}} g_t$$

This prevents the learning rate from decreasing too quickly. RMSProp has been very successful in practice, particularly for recurrent neural networks. However, it lacks a formal convergence proof in the general non-convex case.

#### AdaDelta

AdaDelta is another method that addresses AdaGrad's learning rate decay. Like RMSProp, it uses exponential moving averages of squared gradients, but it also maintains a moving average of squared parameter updates:

$$E[g^2]_t = \rho E[g^2]_{t-1} + (1-\rho) g_t^2$$
$$\Delta\theta_t = -\frac{\sqrt{E[\Delta\theta^2]_{t-1} + \epsilon}}{\sqrt{E[g^2]_t + \epsilon}} g_t$$
$$E[\Delta\theta^2]_t = \rho E[\Delta\theta^2]_{t-1} + (1-\rho) \Delta\theta_t^2$$

AdaDelta eliminates the need to set a learning rate hyperparameter, as the update scale is determined by the ratio of the RMS of parameter updates to the RMS of gradients.

#### Natural Gradient and TONGA

Natural gradient methods use the Fisher information matrix to rescale gradients, which can lead to faster convergence. However, computing the full Fisher matrix is prohibitively expensive for large models. TONGA (Trusted Online Natural Gradient Algorithm) and other natural gradient variants attempt to approximate the natural gradient more efficiently, but they still require more computation than first-order methods like Adam.

#### Comparison with Adam

Adam combines ideas from both momentum methods and adaptive learning rate methods. Like momentum, Adam maintains exponential moving averages of gradients (first moments). Like RMSProp and AdaGrad, Adam adapts learning rates based on gradient magnitudes (second moments). The key innovations in Adam are:

1. **Bias correction**: Unlike RMSProp, Adam includes bias correction for the moment estimates, which is particularly important during the initial timesteps.

2. **Both first and second moments**: While RMSProp only uses second moments, Adam uses both first and second moment estimates, combining the benefits of momentum and adaptive learning rates.

3. **Theoretical guarantees**: Adam has formal regret bounds in the online convex optimization framework, providing theoretical justification for its convergence properties.

4. **Simplicity and efficiency**: Adam is straightforward to implement, computationally efficient, and requires minimal memory overhead compared to second-order methods.

These properties make Adam particularly well-suited for large-scale machine learning problems with high-dimensional parameter spaces and noisy gradients.

---

### النسخة العربية

#### الانحدار التدرجي العشوائي (SGD)

خوارزمية التحسين الأكثر شيوعاً في تعلم الآلة هي الانحدار التدرجي العشوائي (SGD). في شكلها الأساسي، تحدّث SGD المعاملات بالتحرك في اتجاه التدرج السالب:

$$\theta_{t+1} = \theta_t - \alpha \nabla f_t(\theta_t)$$

حيث $\alpha$ هو معدل تعلم ثابت. بينما SGD بسيطة وفعالة للعديد من المسائل، لديها عدة قيود. اختيار معدل التعلم أمر بالغ الأهمية: كبير جداً وستتباعد الخوارزمية، صغير جداً وسيكون التقارب بطيئاً جداً. بالإضافة إلى ذلك، تستخدم SGD نفس معدل التعلم لجميع المعاملات، مما قد يكون غير فعال عندما يكون للمعاملات حساسيات مختلفة.

#### طرق الزخم

لمعالجة بعض قيود SGD، تحافظ طرق الزخم على متوسط متحرك للتدرجات السابقة:

$$v_t = \gamma v_{t-1} + \alpha \nabla f_t(\theta_t)$$
$$\theta_{t+1} = \theta_t - v_t$$

حيث $\gamma$ هو معامل الزخم، يُضبط عادة حول 0.9. يساعد الزخم على تسريع SGD في الاتجاهات ذات الصلة ويخفف التذبذبات. التدرج المتسارع لـ Nesterov (NAG) هو متغير يحقق معدلات تقارب أفضل للمسائل المحدبة.

#### AdaGrad

AdaGrad هي طريقة معدل تعلم تكيفي تكيف معدل التعلم لكل معامل بناءً على معلومات التدرج التاريخية:

$$\theta_{t+1,i} = \theta_{t,i} - \frac{\alpha}{\sqrt{G_{t,ii} + \epsilon}} g_{t,i}$$

حيث $G_t = \sum_{\tau=1}^t g_\tau g_\tau^T$ هو مجموع الضربات الخارجية لجميع التدرجات التاريخية، و $g_{t,i}$ هو المشتق الجزئي بالنسبة للمعامل $i$ في الزمن $t$. تؤدي AdaGrad تحديثات أكبر للمعاملات النادرة وتحديثات أصغر للمعاملات المتكررة، مما يجعلها مناسبة تماماً للبيانات المتفرقة.

ومع ذلك، فإن نقطة الضعف الرئيسية في AdaGrad هي أن معدل التعلم ينخفض بشكل رتيب أثناء التدريب بسبب تراكم التدرجات التربيعية في المقام. في الإعدادات غير المحدبة مثل التعلم العميق، يمكن أن يتسبب هذا في أن يصبح معدل التعلم صغيراً جداً قبل الوصول إلى حل جيد.

#### RMSProp

تم اقتراح RMSProp لمعالجة معدلات التعلم المتناقصة في AdaGrad. بدلاً من تراكم جميع التدرجات التربيعية السابقة، يستخدم RMSProp متوسطاً متناقصاً أسياً:

$$v_t = \beta v_{t-1} + (1-\beta) g_t^2$$
$$\theta_{t+1} = \theta_t - \frac{\alpha}{\sqrt{v_t + \epsilon}} g_t$$

يمنع هذا معدل التعلم من الانخفاض بسرعة كبيرة. كان RMSProp ناجحاً جداً في الممارسة، خاصة للشبكات العصبية التكرارية. ومع ذلك، يفتقر إلى برهان تقارب رسمي في الحالة العامة غير المحدبة.

#### AdaDelta

AdaDelta هي طريقة أخرى تعالج انحلال معدل التعلم في AdaGrad. مثل RMSProp، تستخدم متوسطات متحركة أسية للتدرجات التربيعية، ولكنها تحافظ أيضاً على متوسط متحرك لتحديثات المعاملات التربيعية:

$$E[g^2]_t = \rho E[g^2]_{t-1} + (1-\rho) g_t^2$$
$$\Delta\theta_t = -\frac{\sqrt{E[\Delta\theta^2]_{t-1} + \epsilon}}{\sqrt{E[g^2]_t + \epsilon}} g_t$$
$$E[\Delta\theta^2]_t = \rho E[\Delta\theta^2]_{t-1} + (1-\rho) \Delta\theta_t^2$$

تلغي AdaDelta الحاجة إلى تعيين معامل فائق لمعدل التعلم، حيث يتم تحديد مقياس التحديث بواسطة نسبة الجذر التربيعي للمتوسط لتحديثات المعاملات إلى الجذر التربيعي للمتوسط للتدرجات.

#### التدرج الطبيعي وTONGA

تستخدم طرق التدرج الطبيعي مصفوفة معلومات Fisher لإعادة قياس التدرجات، مما قد يؤدي إلى تقارب أسرع. ومع ذلك، فإن حساب مصفوفة Fisher الكاملة مكلف للغاية بالنسبة للنماذج الكبيرة. TONGA (خوارزمية التدرج الطبيعي الموثوق عبر الإنترنت) ومتغيرات التدرج الطبيعي الأخرى تحاول تقريب التدرج الطبيعي بكفاءة أكبر، لكنها لا تزال تتطلب حسابات أكثر من طرق الدرجة الأولى مثل Adam.

#### المقارنة مع Adam

يجمع Adam بين الأفكار من كل من طرق الزخم وطرق معدل التعلم التكيفي. مثل الزخم، يحافظ Adam على متوسطات متحركة أسية للتدرجات (العزوم الأولى). مثل RMSProp و AdaGrad، يكيف Adam معدلات التعلم بناءً على مقادير التدرج (العزوم الثانية). الابتكارات الرئيسية في Adam هي:

1. **تصحيح الانحياز**: على عكس RMSProp، يتضمن Adam تصحيح الانحياز لتقديرات العزوم، وهو أمر مهم بشكل خاص خلال الخطوات الزمنية الأولية.

2. **كلا العزمين الأول والثاني**: بينما يستخدم RMSProp العزوم الثانية فقط، يستخدم Adam تقديرات العزم الأول والثاني، مما يجمع بين فوائد الزخم ومعدلات التعلم التكيفية.

3. **ضمانات نظرية**: لدى Adam حدود ندم رسمية في إطار التحسين المحدب المتصل، مما يوفر مبرراً نظرياً لخصائص التقارب الخاصة به.

4. **البساطة والكفاءة**: Adam بسيط في التنفيذ، وفعال حسابياً، ويتطلب حمولة ذاكرة ضئيلة مقارنة بطرق الدرجة الثانية.

تجعل هذه الخصائص Adam مناسباً بشكل خاص لمسائل تعلم الآلة واسعة النطاق مع فضاءات معاملات عالية الأبعاد وتدرجات صاخبة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** SGD, momentum, AdaGrad, RMSProp, AdaDelta, natural gradient, Fisher information matrix, exponential moving average
- **Equations:** Multiple update rules for different optimization algorithms
- **Citations:** Implicit references to various optimization methods
- **Special handling:**
  - Algorithm names (SGD, AdaGrad, RMSProp, AdaDelta, NAG, TONGA) kept in English
  - "Momentum" translated as "الزخم" (standard physics/ML term)
  - "Fisher information matrix" translated as "مصفوفة معلومات Fisher" (Fisher kept in English)
  - Technical comparisons maintained with clarity

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-Translation Check (Key Paragraph)

**Arabic:** "يجمع Adam بين الأفكار من كل من طرق الزخم وطرق معدل التعلم التكيفي..."

**Back-Translation:** "Adam combines ideas from both momentum methods and adaptive learning rate methods..."

✓ Semantic equivalence confirmed
