# Section 3: Replacing ResNets with ODEs for Supervised Learning
## القسم 3: استبدال الشبكات المتبقية بالمعادلات التفاضلية العادية للتعلم المُشرف

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** residual network, supervised learning, classification, neural network, training, accuracy, parameter, memory, evaluation

---

### English Version

In this section, we experimentally investigate the cost and performance of ODE-Nets. Specifically, we test whether ODE-Nets can achieve the same performance as their discrete-layer analogues while simultaneously being cheaper to evaluate and less memory-intensive to train.

**Replacing residual networks:** We first replace a standard ResNet architecture with an ODE-Net. ResNets are motivated by an Euler discretization of a continuous transformation (Lu et al., 2017). Specifically, standard ResNets define a discrete sequence of transformations:

$$h_{t+1} = h_t + f(h_t, \theta_t)$$

As the step size approaches zero and the number of layers grows, the discrete dynamics defined by a ResNet approaches a continuous transformation. We can directly parameterize this continuous transformation by defining an ODE:

$$\frac{dh(t)}{dt} = f(h(t), t, \theta)$$

Following the work of Lu et al. (2017), we denote this model as an ODE-Net. To evaluate this model, we can explicitly define the output to be the result of integrating from an initial layer $t_0$ to a final layer time $t_1$:

$$z(t_1) = z(t_0) + \int_{t_0}^{t_1} f(z(t), t, \theta) dt = \text{ODESolve}(z(t_0), f, t_0, t_1, \theta)$$

**Experiments on MNIST:** We trained a small residual network and an ODE-Net to classify MNIST digits. Both models had comparable test set accuracy. However, the ODE-Net used roughly one-third fewer parameters than its discrete analogue. Figure 2 shows the evaluation trajectories during inference for both the ResNet and ODE-Net, visualizing how the hidden state travels from input to classification output in the network's feature space.

**Figure 2 caption:** **Illustration of how different architectures compute the transformation from input to output:** A comparison of residual network blocks (left) with an ODE network (right). Arrows denote evaluation steps. The points on the right show where an ODE solver evaluates the network dynamics. These evaluations are not equally spaced, and the locations are adaptive to the complexity of the input.

The number of evaluations of the hidden state dynamics required in the forward pass is roughly half that of the ResNet, and only 2 evaluations are required in the backward pass. This gives the model an implicit capacity to trade off speed for accuracy during both training and testing. For a sense of scale, a comparable ResNet architecture used 6 evaluations.

**Memory cost:** Table 1 shows a comparison of maximum memory usage during training for an ODE-Net versus a ResNet with the same number of parameters. Training typical architectures using our adjoint method is significantly less memory-intensive than backpropagation through the operations of an ODE solver. The advantage grows as the number of layers increases.

**Table 1:** Memory cost of backpropagation. All experiments trained on a single GPUs.

| Method | Memory cost (MB) |
|--------|------------------|
| Naive backprop through RK-45 | 17,400 |
| Adjoint method (ours) | 2,700 |
| ResNet (6 layers) | 2,900 |

Our approach uses memory comparable to that of a 6-layer ResNet, while the naive application of backpropagation to an adaptive ODE solver requires 17GB of GPU memory, far more than is available on typical GPUs.

**Effectiveness on CIFAR10:** We also trained a network on CIFAR10, to verify that our approach scales to natural images. Starting from a downsampled 32x32 input, we trained a network to classify 10 categories. The final test accuracy was 64.2%. While not state-of-the-art, this result demonstrates that continuous-depth networks can be trained to competitive performance on standard benchmarks.

---

### النسخة العربية

في هذا القسم، نحقق تجريبياً في تكلفة وأداء شبكات المعادلات التفاضلية العادية (ODE-Nets). على وجه التحديد، نختبر ما إذا كانت شبكات المعادلات التفاضلية العادية يمكن أن تحقق نفس الأداء مثل نظيراتها ذات الطبقات المنفصلة بينما تكون في نفس الوقت أرخص في التقييم وأقل كثافة في الذاكرة للتدريب.

**استبدال الشبكات المتبقية:** نستبدل أولاً معمارية ResNet القياسية بشبكة المعادلات التفاضلية العادية (ODE-Net). يتم تحفيز شبكات ResNet من خلال تقطيع أويلر لتحويل مستمر (Lu et al., 2017). على وجه التحديد، تحدد شبكات ResNet القياسية تسلسلاً منفصلاً من التحويلات:

$$h_{t+1} = h_t + f(h_t, \theta_t)$$

عندما يقترب حجم الخطوة من الصفر ويزداد عدد الطبقات، تقترب الديناميكيات المنفصلة المحددة بواسطة ResNet من تحويل مستمر. يمكننا تحديد معاملات هذا التحويل المستمر مباشرة من خلال تعريف معادلة تفاضلية عادية:

$$\frac{dh(t)}{dt} = f(h(t), t, \theta)$$

باتباع عمل Lu et al. (2017)، نشير إلى هذا النموذج باسم شبكة المعادلات التفاضلية العادية (ODE-Net). لتقييم هذا النموذج، يمكننا تعريف المخرج بشكل صريح ليكون نتيجة التكامل من طبقة ابتدائية $t_0$ إلى وقت طبقة نهائية $t_1$:

$$z(t_1) = z(t_0) + \int_{t_0}^{t_1} f(z(t), t, \theta) dt = \text{ODESolve}(z(t_0), f, t_0, t_1, \theta)$$

**تجارب على MNIST:** قمنا بتدريب شبكة متبقية صغيرة وشبكة معادلات تفاضلية عادية لتصنيف أرقام MNIST. كان لكلا النموذجين دقة مجموعة اختبار قابلة للمقارنة. ومع ذلك، استخدمت شبكة المعادلات التفاضلية العادية تقريباً ثلث عدد المعاملات مقارنة بنظيرتها المنفصلة. يُظهر الشكل 2 مسارات التقييم أثناء الاستنتاج لكل من ResNet و ODE-Net، مما يُصوّر كيف تنتقل الحالة المخفية من المدخل إلى مخرج التصنيف في فضاء الميزات للشبكة.

**تسمية الشكل 2:** **توضيح لكيفية قيام المعماريات المختلفة بحساب التحويل من المدخل إلى المخرج:** مقارنة بين كتل الشبكة المتبقية (يسار) مع شبكة المعادلات التفاضلية العادية (يمين). تشير الأسهم إلى خطوات التقييم. تُظهر النقاط على اليمين أين يقيّم حلال المعادلات التفاضلية العادية ديناميكيات الشبكة. هذه التقييمات ليست متباعدة بشكل متساوٍ، والمواقع تتكيف مع تعقيد المدخل.

عدد التقييمات لديناميكيات الحالة المخفية المطلوبة في المرور الأمامي هو تقريباً نصف عدد تقييمات ResNet، ويتطلب مرورين فقط للتقييم في المرور العكسي. هذا يمنح النموذج قدرة ضمنية على المقايضة بين السرعة والدقة أثناء التدريب والاختبار. للحصول على فكرة عن النطاق، استخدمت معمارية ResNet قابلة للمقارنة 6 تقييمات.

**تكلفة الذاكرة:** يُظهر الجدول 1 مقارنة لأقصى استخدام للذاكرة أثناء التدريب لشبكة المعادلات التفاضلية العادية مقابل ResNet بنفس عدد المعاملات. تدريب المعماريات النموذجية باستخدام طريقة المرافق الخاصة بنا أقل كثافة في الذاكرة بشكل كبير من الانتشار العكسي عبر عمليات حلال المعادلات التفاضلية العادية. تزداد الميزة مع زيادة عدد الطبقات.

**الجدول 1:** تكلفة ذاكرة الانتشار العكسي. جميع التجارب تم تدريبها على وحدة معالجة رسومات واحدة.

| الطريقة | تكلفة الذاكرة (ميجابايت) |
|--------|------------------|
| الانتشار العكسي الساذج عبر RK-45 | 17,400 |
| طريقة المرافق (الخاصة بنا) | 2,700 |
| ResNet (6 طبقات) | 2,900 |

تستخدم طريقتنا ذاكرة قابلة للمقارنة مع شبكة ResNet ذات 6 طبقات، بينما يتطلب التطبيق الساذج للانتشار العكسي لحلال معادلات تفاضلية عادية تكيفي 17 جيجابايت من ذاكرة GPU، وهو أكثر بكثير مما هو متاح على وحدات معالجة الرسومات النموذجية.

**الفعالية على CIFAR10:** قمنا أيضاً بتدريب شبكة على CIFAR10، للتحقق من أن طريقتنا تتوسع إلى الصور الطبيعية. بدءاً من مدخل مخفض العينة 32x32، قمنا بتدريب شبكة لتصنيف 10 فئات. كانت دقة الاختبار النهائية 64.2٪. على الرغم من أنها ليست الأفضل في فئتها، فإن هذه النتيجة توضح أن الشبكات ذات العمق المستمر يمكن تدريبها لتحقيق أداء تنافسي على المعايير القياسية.

---

### Translation Notes

- **Figures referenced:** Figure 2
- **Key terms introduced:** ODE-Net, continuous transformation, evaluation trajectories, forward pass, backward pass
- **Equations:** 3 main equations
- **Citations:** Lu et al. (2017)
- **Special handling:** Table 1 translated with memory metrics, experimental results carefully translated
- **Datasets:** MNIST, CIFAR10

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
