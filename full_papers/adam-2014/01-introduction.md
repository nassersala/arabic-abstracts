# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** stochastic, gradient, optimization, algorithm, deep learning, objective function, parameters, SGD (stochastic gradient descent), adaptive learning rates, first moment, second moment, AdaGrad, RMSProp, stepsize, sparse gradients, non-stationary

---

### English Version

Stochastic gradient-based optimization is of core practical importance in many fields of science and engineering. Many problems in these fields can be cast as the optimization of some scalar parameterized objective function requiring maximization or minimization with respect to its parameters. If the function is differentiable w.r.t. its parameters, gradient descent is a relatively efficient optimization method, since the computation of first-order partial derivatives w.r.t. all the parameters is of the same computational complexity as just evaluating the function. Often, objective functions are stochastic. For example, many objective functions are composed of a sum of subfunctions evaluated at different subsamples of data; in this case optimization can be made more efficient by taking gradient steps w.r.t. individual subfunctions, i.e. stochastic gradient descent (SGD) or ascent. SGD proved itself as an efficient and effective optimization method that was central in many machine learning success stories, such as recent advances in deep learning (Deng et al., 2013; Krizhevsky et al., 2012; Hinton & Salakhutdinov, 2006; Hinton et al., 2012a; Graves et al., 2013). Objectives may also have other sources of noise than data subsampling, such as dropout (Hinton et al., 2012b) regularization. For all such noisy objectives, efficient stochastic optimization techniques are required. The focus of this paper is on the optimization of stochastic objectives with high-dimensional parameters spaces. In these cases, higher-order optimization methods are ill-suited, and discussion in this paper will be restricted to first-order methods.

We propose Adam, a method for efficient stochastic optimization that only requires first-order gradients with little memory requirement. The method computes individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients; the name Adam is derived from adaptive moment estimation. Our method is designed to combine the advantages of two recently popular methods: AdaGrad (Duchi et al., 2011), which works well with sparse gradients, and RMSProp (Tieleman & Hinton, 2012), which works well in on-line and non-stationary settings; important connections to these and other stochastic optimization methods are clarified in section 5. Some of Adam's advantages are that the magnitudes of parameter updates are invariant to rescaling of the gradient, its stepsizes are approximately bounded by the stepsize hyperparameter, it does not require a stationary objective, it works with sparse gradients, and it naturally performs a form of step size annealing.

---

### النسخة العربية

يُعد التحسين العشوائي القائم على التدرج ذا أهمية عملية أساسية في العديد من مجالات العلوم والهندسة. يمكن صياغة العديد من المسائل في هذه المجالات كتحسين لدالة هدفية معلمة قياسية تتطلب التعظيم أو التصغير فيما يتعلق بمعاملاتها. إذا كانت الدالة قابلة للاشتقاق فيما يتعلق بمعاملاتها، فإن الانحدار التدرجي يُعد طريقة تحسين فعالة نسبياً، حيث أن حساب المشتقات الجزئية من الدرجة الأولى فيما يتعلق بجميع المعاملات له نفس التعقيد الحسابي لمجرد تقييم الدالة. غالباً ما تكون الدوال الهدفية عشوائية. على سبيل المثال، تتكون العديد من الدوال الهدفية من مجموع دوال فرعية يتم تقييمها عند عينات فرعية مختلفة من البيانات؛ في هذه الحالة يمكن جعل التحسين أكثر كفاءة من خلال اتخاذ خطوات تدرجية فيما يتعلق بالدوال الفرعية الفردية، أي الانحدار التدرجي العشوائي (SGD) أو الصعود. أثبت الانحدار التدرجي العشوائي نفسه كطريقة تحسين فعالة وناجعة كانت محورية في العديد من قصص نجاح التعلم الآلي، مثل التطورات الحديثة في التعلم العميق (Deng et al., 2013; Krizhevsky et al., 2012; Hinton & Salakhutdinov, 2006; Hinton et al., 2012a; Graves et al., 2013). قد تحتوي الأهداف أيضاً على مصادر ضوضاء أخرى غير أخذ العينات الفرعية للبيانات، مثل تنظيم dropout (Hinton et al., 2012b). لجميع هذه الأهداف الصاخبة، مطلوبة تقنيات تحسين عشوائية فعالة. يركز هذا البحث على تحسين الأهداف العشوائية ذات فضاءات المعاملات عالية الأبعاد. في هذه الحالات، طرق التحسين من الرتبة العليا غير مناسبة، وسيقتصر النقاش في هذا البحث على طرق الدرجة الأولى.

نقترح Adam، وهي طريقة للتحسين العشوائي الفعال تتطلب فقط تدرجات من الدرجة الأولى مع متطلبات ذاكرة قليلة. تحسب الطريقة معدلات تعلم تكيفية فردية لمختلف المعاملات من تقديرات العزم الأول والثاني للتدرجات؛ اسم Adam مشتق من تقدير العزم التكيفي (adaptive moment estimation). صُممت طريقتنا للجمع بين مزايا طريقتين شهيرتين مؤخراً: AdaGrad (Duchi et al., 2011)، التي تعمل بشكل جيد مع التدرجات المتفرقة، و RMSProp (Tieleman & Hinton, 2012)، التي تعمل بشكل جيد في الإعدادات عبر الإنترنت وغير الثابتة؛ يتم توضيح الروابط المهمة بهذه الطرق وطرق التحسين العشوائية الأخرى في القسم 5. من بين مزايا Adam أن قيم تحديثات المعاملات ثابتة تجاه إعادة قياس التدرج، وأن أحجام خطواتها محدودة تقريباً بواسطة المعامل الفائق لحجم الخطوة، وأنها لا تتطلب هدفاً ثابتاً، وتعمل مع التدرجات المتفرقة، وتؤدي بشكل طبيعي شكلاً من أشكال تلدين حجم الخطوة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Stochastic gradient descent (الانحدار التدرجي العشوائي)
  - Adaptive moment estimation (تقدير العزم التكيفي)
  - First and second moments (العزم الأول والثاني)
  - Sparse gradients (التدرجات المتفرقة)
  - Non-stationary objectives (الأهداف غير الثابتة)
  - Step size annealing (تلدين حجم الخطوة)
  - High-dimensional parameter spaces (فضاءات المعاملات عالية الأبعاد)
- **Equations:** None
- **Citations:** Multiple citations preserved in English as per convention (Deng et al., 2013; etc.)
- **Special handling:**
  - "w.r.t." translated as "فيما يتعلق ب"
  - Algorithm names (Adam, AdaGrad, RMSProp, SGD) kept in English
  - Technical terms consistently using glossary

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation (Validation)

Stochastic optimization based on gradients is of fundamental practical importance in many fields of science and engineering. Many problems in these fields can be formulated as optimization of a scalar parameterized objective function that requires maximization or minimization with respect to its parameters. If the function is differentiable with respect to its parameters, gradient descent is a relatively efficient optimization method, since computing first-order partial derivatives with respect to all parameters has the same computational complexity as merely evaluating the function. Often objective functions are stochastic. For example, many objective functions consist of a sum of subfunctions evaluated on different subsamples of data; in this case optimization can be made more efficient by taking gradient steps with respect to individual subfunctions, i.e., stochastic gradient descent (SGD) or ascent. Stochastic gradient descent has proven itself as an effective and efficient optimization method that was central to many machine learning success stories, such as recent developments in deep learning. Objectives may also contain other sources of noise besides data subsampling, such as dropout regularization. For all such noisy objectives, efficient stochastic optimization techniques are required. This research focuses on optimizing stochastic objectives with high-dimensional parameter spaces. In these cases, higher-order optimization methods are unsuitable, and the discussion in this research will be limited to first-order methods.

We propose Adam, a method for efficient stochastic optimization that requires only first-order gradients with little memory requirements. The method computes individual adaptive learning rates for different parameters from estimates of the first and second moments of gradients; the name Adam is derived from adaptive moment estimation. Our method is designed to combine the advantages of two recently popular methods: AdaGrad, which works well with sparse gradients, and RMSProp, which works well in online and non-stationary settings; important connections to these and other stochastic optimization methods are clarified in Section 5. Among Adam's advantages are that parameter update values are invariant to gradient rescaling, its step sizes are approximately bounded by the step size hyperparameter, it does not require a stationary objective, works with sparse gradients, and naturally performs a form of step size annealing.
