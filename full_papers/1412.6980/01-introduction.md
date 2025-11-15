# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** stochastic optimization, gradient descent, learning rate, hyperparameter, adaptive, deep learning, convergence, momentum

---

### English Version

Stochastic gradient-based optimization is of core practical importance in many fields of science and engineering. Many problems in these fields can be cast as the optimization of some scalar parameterized objective function requiring maximization or minimization with respect to its parameters. If the function is differentiable w.r.t. its parameters, gradient descent is a relatively efficient optimization method, since the computation of first-order partial derivatives w.r.t. all the parameters is of the same computational complexity as just evaluating the function. Often, objective functions are stochastic. For example, many objective functions are composed of a sum of subfunctions evaluated at different subsamples of data; in this case optimization can be made more efficient by taking gradient steps w.r.t. individual subfunctions, i.e. stochastic gradient descent (SGD) or ascent. SGD and related stochastic optimization methods are particularly well suited to optimization in the context of machine-learning tasks with large datasets and/or large numbers of parameters.

However, many practical problems in machine learning also involve objectives with very noisy gradients or gradients with large and/or sparse curvature, making plain stochastic gradient descent less well-suited. In particular, the choice of learning rate in plain SGD is critical but can be difficult: too small a step size leads to painfully slow convergence, while a step size that is too large will cause the loss to diverge. This has motivated the development of adaptive methods that scale the learning rate for each parameter according to some measure of the typical magnitude of recent gradient updates for that parameter.

A well-known member of the class of adaptive methods is AdaGrad, which scales the learning rate for each parameter inversely proportional to the square root of the sum of all the historical squared values of the gradient. This leads to greater progress in the less steep (and presumably more noise-prone) directions, and can be quite effective in the convex setting. However, in the non-convex setting common in deep learning, AdaGrad's learning rate becomes infinitesimally small after a number of updates due to the accumulation of historical squared gradients in the denominator.

RMSProp is another adaptive learning rate method that seeks to improve upon AdaGrad, especially in the non-stationary and online setting. RMSProp uses a moving average of squared gradients to normalize the gradient, preventing the learning rate from shrinking monotonically as in AdaGrad. However, RMSProp lacks a theoretical convergence proof in the general case.

In this paper, we propose Adam, a method for efficient stochastic optimization that only requires first-order gradients with little memory requirement. The method computes individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients; the name Adam is derived from adaptive moment estimation. Our method is designed to combine the advantages of two recently popular methods: AdaGrad, which works well with sparse gradients, and RMSProp, which works well in on-line and non-stationary settings. Some of Adam's advantages are that the magnitudes of parameter updates are invariant to rescaling of the gradient, its step sizes are approximately bounded by the stepsize hyperparameter, it does not require a stationary objective, it works with sparse gradients, and it naturally performs a form of step size annealing.

We provide a regret bound on the convergence rate that is comparable to the best known results under the online convex optimization framework. An empirical analysis on a number of models and datasets shows that Adam works well in practice and compares favorably to other stochastic optimization methods in deep learning.

---

### النسخة العربية

يُعد التحسين العشوائي القائم على التدرجات ذا أهمية عملية محورية في العديد من المجالات العلمية والهندسية. يمكن صياغة العديد من المسائل في هذه المجالات على شكل تحسين لدالة هدفية قياسية معلمية تتطلب التعظيم أو التصغير بالنسبة لمعاملاتها. إذا كانت الدالة قابلة للاشتقاق بالنسبة لمعاملاتها، فإن الانحدار التدرجي (gradient descent) يُعد طريقة تحسين فعالة نسبياً، حيث أن حساب المشتقات الجزئية من الدرجة الأولى بالنسبة لجميع المعاملات له نفس التعقيد الحسابي لمجرد تقييم الدالة. غالباً ما تكون الدوال الهدفية عشوائية. على سبيل المثال، تتكون العديد من الدوال الهدفية من مجموع دوال فرعية يتم تقييمها على عينات فرعية مختلفة من البيانات؛ في هذه الحالة يمكن جعل التحسين أكثر كفاءة عن طريق أخذ خطوات تدرجية بالنسبة للدوال الفرعية الفردية، أي الانحدار التدرجي العشوائي (SGD) أو الصعود العشوائي. تُعد طريقة SGD وطرق التحسين العشوائي ذات الصلة مناسبة بشكل خاص للتحسين في سياق مهام تعلم الآلة مع مجموعات البيانات الكبيرة و/أو الأعداد الكبيرة من المعاملات.

ومع ذلك، تتضمن العديد من المسائل العملية في تعلم الآلة أيضاً أهدافاً ذات تدرجات صاخبة جداً أو تدرجات ذات انحناء كبير و/أو متفرق، مما يجعل الانحدار التدرجي العشوائي البسيط أقل ملاءمة. على وجه الخصوص، يُعد اختيار معدل التعلم في SGD البسيط أمراً بالغ الأهمية ولكنه قد يكون صعباً: حجم الخطوة الصغير جداً يؤدي إلى تقارب بطيء مؤلم، في حين أن حجم الخطوة الكبير جداً سيتسبب في تباعد الخسارة. وقد حفز هذا تطوير الطرق التكيفية التي تقيس معدل التعلم لكل معامل وفقاً لبعض مقاييس الحجم النموذجي لتحديثات التدرج الأخيرة لذلك المعامل.

أحد الأعضاء المعروفين في فئة الطرق التكيفية هو AdaGrad، الذي يقيس معدل التعلم لكل معامل بشكل متناسب عكسياً مع الجذر التربيعي لمجموع جميع القيم التربيعية التاريخية للتدرج. يؤدي هذا إلى تقدم أكبر في الاتجاهات الأقل انحداراً (والتي من المفترض أن تكون أكثر عرضة للضوضاء)، ويمكن أن يكون فعالاً تماماً في الإعداد المحدب. ومع ذلك، في الإعداد غير المحدب الشائع في التعلم العميق، يصبح معدل التعلم في AdaGrad صغيراً جداً بعد عدد من التحديثات بسبب تراكم التدرجات التربيعية التاريخية في المقام.

RMSProp هي طريقة أخرى لمعدل التعلم التكيفي تسعى إلى التحسين على AdaGrad، خاصة في الإعداد غير الثابت والمتصل. يستخدم RMSProp متوسطاً متحركاً للتدرجات التربيعية لتطبيع التدرج، مما يمنع معدل التعلم من الانكماش الرتيب كما في AdaGrad. ومع ذلك، يفتقر RMSProp إلى برهان تقارب نظري في الحالة العامة.

في هذه الورقة، نقترح Adam، وهي طريقة للتحسين العشوائي الفعال تتطلب فقط تدرجات من الدرجة الأولى مع متطلبات ذاكرة قليلة. تحسب الطريقة معدلات تعلم تكيفية فردية لمعاملات مختلفة من تقديرات العزوم من الدرجة الأولى والثانية للتدرجات؛ الاسم Adam مشتق من التقدير التكيفي للعزوم (adaptive moment estimation). طريقتنا مصممة للجمع بين مزايا طريقتين شائعتين مؤخراً: AdaGrad، الذي يعمل بشكل جيد مع التدرجات المتفرقة، وRMSProp، الذي يعمل بشكل جيد في الإعدادات المتصلة وغير الثابتة. بعض مزايا Adam هي أن حجم تحديثات المعاملات ثابت بالنسبة لإعادة القياس للتدرج، وأحجام خطواته محدودة تقريباً بواسطة المعامل الفائق لحجم الخطوة، ولا يتطلب هدفاً ثابتاً، ويعمل مع التدرجات المتفرقة، ويؤدي بشكل طبيعي شكلاً من أشكال تلدين حجم الخطوة.

نقدم حداً للندم على معدل التقارب يمكن مقارنته بأفضل النتائج المعروفة في إطار التحسين المحدب المتصل. يُظهر التحليل التجريبي على عدد من النماذج ومجموعات البيانات أن Adam يعمل بشكل جيد في الممارسة العملية ويقارن بشكل إيجابي مع طرق التحسين العشوائي الأخرى في التعلم العميق.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** stochastic gradient descent (SGD), AdaGrad, RMSProp, adaptive learning rate, moment estimation, regret bound, convex optimization
- **Equations:** 0
- **Citations:** Implicit references to AdaGrad, RMSProp
- **Special handling:**
  - Algorithm names (Adam, AdaGrad, RMSProp, SGD) kept in English as they are standard in ML community
  - "w.r.t." translated as "بالنسبة لـ" (with respect to)
  - Technical terms like "moment estimation" carefully translated with explanatory Arabic

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Check (Key Paragraph)

**Arabic:** "في هذه الورقة، نقترح Adam، وهي طريقة للتحسين العشوائي الفعال تتطلب فقط تدرجات من الدرجة الأولى مع متطلبات ذاكرة قليلة..."

**Back-Translation:** "In this paper, we propose Adam, a method for efficient stochastic optimization that requires only first-order gradients with little memory requirements..."

✓ Semantic equivalence confirmed
