# Section 5: Details of Learning
## القسم 5: تفاصيل التعلم

**Section:** details-of-learning
**Translation Quality:** 0.89
**Glossary Terms Used:** training, neural network, gradient, learning rate, convergence, initialization

---

### English Version

We trained our models using stochastic gradient descent with a batch size of 128 examples, momentum of 0.9, and weight decay of 0.0005. We found that this small amount of weight decay was important for the model to learn. In other words, weight decay here is not merely a regularizer: it reduces the model's training error. The update rule for weight w was

$$v_{i+1} := 0.9 \\cdot v_i - 0.0005 \\cdot \\epsilon \\cdot w_i - \\epsilon \\cdot \\left\\langle \\frac{\\partial L}{\\partial w} \\Big|_{w_i} \\right\\rangle_{D_i}$$

$$w_{i+1} := w_i + v_{i+1}$$

where i is the iteration index, v is the momentum variable, ε is the learning rate, and ⟨∂L/∂w|_{w_i}⟩_{D_i} is the average over the i-th batch D_i of the derivative of the objective with respect to w, evaluated at w_i.

We initialized the weights in each layer from a zero-mean Gaussian distribution with standard deviation 0.01. We initialized the neuron biases in the second, fourth, and fifth convolutional layers, as well as in the fully-connected hidden layers, with the constant 1. This initialization accelerates the early stages of learning by providing the ReLUs with positive inputs. We initialized the neuron biases in the remaining layers with the constant 0.

We used an equal learning rate for all layers, which we adjusted manually throughout training. The heuristic which we followed was to divide the learning rate by 10 when the validation error rate stopped improving with the current learning rate. The learning rate was initialized at 0.01 and reduced three times prior to termination. We trained the network for roughly 90 cycles through the training set of 1.2 million images, which took five to six days on two NVIDIA GTX 580 3GB GPUs.

---

### النسخة العربية

قمنا بتدريب نماذجنا باستخدام الانحدار التدرجي العشوائي (stochastic gradient descent) بحجم دفعة 128 مثالاً، وزخم (momentum) 0.9، وتضاؤل وزن (weight decay) 0.0005. وجدنا أن هذه الكمية الصغيرة من تضاؤل الوزن كانت مهمة للنموذج للتعلم. بمعنى آخر، تضاؤل الوزن هنا ليس مجرد منظم: إنه يقلل من خطأ التدريب للنموذج. كانت قاعدة التحديث للوزن w هي

$$v_{i+1} := 0.9 \\cdot v_i - 0.0005 \\cdot \\epsilon \\cdot w_i - \\epsilon \\cdot \\left\\langle \\frac{\\partial L}{\\partial w} \\Big|_{w_i} \\right\\rangle_{D_i}$$

$$w_{i+1} := w_i + v_{i+1}$$

حيث i هو مؤشر التكرار، وv هو متغير الزخم، وε هو معدل التعلم، و⟨∂L/∂w|_{w_i}⟩_{D_i} هو المتوسط على الدفعة i-th، D_i، لمشتق الهدف بالنسبة إلى w، محسوباً عند w_i.

قمنا بتهيئة الأوزان في كل طبقة من توزيع غاوسي بمتوسط صفر وانحراف معياري 0.01. قمنا بتهيئة انحيازات العصبونات (neuron biases) في الطبقات الالتفافية الثانية والرابعة والخامسة، وكذلك في الطبقات المخفية المتصلة بالكامل، بالثابت 1. يسرع هذا التهيئة المراحل المبكرة من التعلم من خلال توفير مدخلات موجبة لـ ReLUs. قمنا بتهيئة انحيازات العصبونات في الطبقات المتبقية بالثابت 0.

استخدمنا معدل تعلم متساوٍ لجميع الطبقات، قمنا بتعديله يدوياً طوال التدريب. الإرشاد الذي اتبعناه كان تقسيم معدل التعلم على 10 عندما توقف معدل خطأ التحقق عن التحسن مع معدل التعلم الحالي. تمت تهيئة معدل التعلم عند 0.01 وتم تخفيضه ثلاث مرات قبل الإنهاء. قمنا بتدريب الشبكة لحوالي 90 دورة عبر مجموعة التدريب المكونة من 1.2 مليون صورة، والتي استغرقت من خمسة إلى ستة أيام على وحدتي معالجة رسومات NVIDIA GTX 580 بذاكرة 3 جيجابايت.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - stochastic gradient descent (الانحدار التدرجي العشوائي)
  - batch size (حجم دفعة)
  - momentum (زخم)
  - weight decay (تضاؤل وزن)
  - regularizer (منظم)
  - training error (خطأ التدريب)
  - update rule (قاعدة التحديث)
  - iteration index (مؤشر التكرار)
  - momentum variable (متغير الزخم)
  - learning rate (معدل التعلم)
  - derivative (مشتق)
  - objective (الهدف)
  - zero-mean Gaussian distribution (توزيع غاوسي بمتوسط صفر)
  - neuron biases (انحيازات العصبونات)
  - initialization (تهيئة)
  - validation error rate (معدل خطأ التحقق)
  - heuristic (إرشاد)
  - cycles (دورات)
- **Equations:**
  - Weight update rule (preserved in LaTeX)
  - Momentum equation (preserved in LaTeX)
- **Citations:** None
- **Special handling:**
  - Mathematical notation preserved exactly
  - Greek letters preserved (ε for learning rate, ∂ for partial derivative)
  - Subscripts and superscripts maintained
  - Numerical values preserved (0.9, 0.0005, 0.01, 128, 90, etc.)
  - GPU model kept in English (NVIDIA GTX 580 3GB)
  - Technical terms like "stochastic gradient descent" translated with English in parentheses
  - Batch notation D_i preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Check

Training description back-translated:
Arabic: "قمنا بتدريب نماذجنا باستخدام الانحدار التدرجي العشوائي بحجم دفعة 128 مثالاً، وزخم 0.9، وتضاؤل وزن 0.0005"
Back to English: "We trained our models using stochastic gradient descent with a batch size of 128 examples, momentum of 0.9, and weight decay of 0.0005"
✓ Semantic match confirmed

Learning rate policy back-translated:
Arabic: "الإرشاد الذي اتبعناه كان تقسيم معدل التعلم على 10 عندما توقف معدل خطأ التحقق عن التحسن..."
Back to English: "The heuristic we followed was to divide the learning rate by 10 when the validation error rate stopped improving..."
✓ Semantic match confirmed
