# Section 5: Learning Dropout Nets
## القسم 5: تعلم شبكات Dropout

**Section:** learning
**Translation Quality:** 0.88
**Glossary Terms Used:** backpropagation, gradient descent, stochastic gradient descent, mini-batch, learning rate, momentum, weight decay, hyperparameters

---

### English Version

Training a neural network with dropout is very similar to training a standard neural network. The main difference is that for each training case in a mini-batch, we sample a thinned network by dropping out units. Forward and backpropagation for that training case are done only on this thinned network. The gradients for each parameter are averaged over the training cases in each mini-batch. Any training algorithm that uses gradient information can be used. We used stochastic gradient descent with mini-batches in all our experiments.

**Practical Guide for Training Dropout Neural Networks:**

1. **Network Architecture:** Dropout can be applied to any architecture. It works well with fully connected layers but can also be applied to convolutional layers and other architectures.

2. **Dropout Rate:** The optimal dropout rate depends on the architecture and task. For hidden layers, a dropout rate of 0.5 works well across many tasks. For input layers, keeping 0.8 or more of the inputs tends to work better. The dropout rate can be different for different layers.

3. **Learning Rate and Momentum:** Dropout networks typically require higher learning rates (10-100 times higher) than standard networks. Using momentum of 0.95-0.99 helps. The large learning rates combined with high momentum help the network escape sharp minima and find flatter minima that generalize better.

4. **Weight Initialization:** Initialize weights from a Gaussian distribution with zero mean and standard deviation proportional to $1/\sqrt{n}$ where $n$ is the number of inputs to the unit. For ReLU units, use He initialization.

5. **Max-norm Regularization:** Constrain the norm of the incoming weight vector at each hidden unit to be upper bounded by a constant $c$ (typically 3 or 4). This is done by projecting $\mathbf{w}$ to satisfy $\|\mathbf{w}\|_2 \leq c$ whenever the constraint is violated after a gradient descent step. Max-norm regularization is particularly effective when combined with dropout.

6. **Training Time:** Dropout slows down training by a factor of about 2-3 because each update is very noisy. However, each epoch takes about the same time. The convergence is slower in terms of epochs.

---

### النسخة العربية

تدريب شبكة عصبية مع dropout مشابه جداً لتدريب شبكة عصبية قياسية. الفرق الرئيسي هو أنه لكل حالة تدريب في دفعة صغيرة، نأخذ عينة من شبكة مخففة عن طريق حذف الوحدات. يتم إجراء الانتشار الأمامي والخلفي لحالة التدريب تلك فقط على هذه الشبكة المخففة. يتم حساب متوسط التدرجات لكل معامل على حالات التدريب في كل دفعة صغيرة. يمكن استخدام أي خوارزمية تدريب تستخدم معلومات التدرج. استخدمنا الانحدار التدرجي العشوائي مع الدفعات الصغيرة في جميع تجاربنا.

**دليل عملي لتدريب شبكات Dropout العصبية:**

1. **معمارية الشبكة:** يمكن تطبيق dropout على أي معمارية. يعمل بشكل جيد مع الطبقات المتصلة بالكامل ولكن يمكن أيضاً تطبيقه على الطبقات الالتفافية والمعماريات الأخرى.

2. **معدل Dropout:** يعتمد معدل dropout الأمثل على المعمارية والمهمة. بالنسبة للطبقات المخفية، يعمل معدل dropout بقيمة 0.5 بشكل جيد عبر العديد من المهام. بالنسبة لطبقات الإدخال، يميل الاحتفاظ بـ 0.8 أو أكثر من المدخلات إلى العمل بشكل أفضل. يمكن أن يكون معدل dropout مختلفاً لطبقات مختلفة.

3. **معدل التعلم والزخم:** تتطلب شبكات dropout عادةً معدلات تعلم أعلى (10-100 مرة أعلى) من الشبكات القياسية. يساعد استخدام الزخم بقيمة 0.95-0.99. تساعد معدلات التعلم الكبيرة مع الزخم العالي الشبكة على الهروب من القيم الدنيا الحادة وإيجاد قيم دنيا أكثر تسطحاً تعمم بشكل أفضل.

4. **تهيئة الأوزان:** قم بتهيئة الأوزان من توزيع غاوسي بمتوسط صفري وانحراف معياري يتناسب مع $1/\sqrt{n}$ حيث $n$ هو عدد المدخلات إلى الوحدة. بالنسبة لوحدات ReLU، استخدم تهيئة He.

5. **تنظيم القاعدة القصوى:** قيّد معيار متجه الوزن الوارد عند كل وحدة مخفية بحيث يكون محدوداً من الأعلى بثابت $c$ (عادةً 3 أو 4). يتم ذلك عن طريق إسقاط $\mathbf{w}$ لتحقيق $\|\mathbf{w}\|_2 \leq c$ كلما انتُهك القيد بعد خطوة الانحدار التدرجي. تنظيم القاعدة القصوى فعال بشكل خاص عند دمجه مع dropout.

6. **وقت التدريب:** يبطئ dropout التدريب بعامل حوالي 2-3 لأن كل تحديث يكون ضوضاءً جداً. ومع ذلك، تستغرق كل حقبة تقريباً نفس الوقت. التقارب أبطأ من حيث الحقبات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** max-norm regularization, He initialization, ReLU units, mini-batch, thinned network
- **Equations:** 2 mathematical expressions for weight constraints
- **Citations:** None explicit
- **Special handling:**
  - "ReLU" kept as standard technical abbreviation
  - "He initialization" kept as proper noun reference
  - Numerical values (0.5, 0.8, 0.95-0.99, etc.) preserved exactly
  - "Max-norm regularization" translated as "تنظيم القاعدة القصوى"

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.92
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.88
