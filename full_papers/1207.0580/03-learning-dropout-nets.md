# Section 3: Learning Dropout Nets
## القسم 3: تعلم شبكات Dropout

**Section:** learning-dropout-nets
**Translation Quality:** 0.86
**Glossary Terms Used:** backpropagation, stochastic gradient descent, learning rate, minibatch, momentum, regularization, hyperparameter, max-norm constraint

---

### English Version

Training a neural network with dropout is very similar to training a standard neural network. The gradient is computed as normal, except that it is computed only for the thinned network. At each training case, a new thinned network is sampled and trained. So each parameter update is computed using a different thinned network.

We train dropout neural networks using stochastic gradient descent with mini-batches. The gradients for each parameter are averaged over the training cases in each mini-batch. The standard momentum method is used. The learning rate, momentum, and weight decay parameters used are similar to those used for training standard neural nets. However, dropout training is slower and we find that it is beneficial to use a higher learning rate and higher momentum.

Dropout can be combined with other forms of regularization such as max-norm regularization. We constrain the norm of the incoming weight vector at each hidden unit to be bounded by a constant $c$. This is often called max-norm regularization. We enforce this constraint by projecting $\mathbf{w}$ onto a ball of radius $c$ centered at the origin whenever $\|\mathbf{w}\| > c$ after a gradient descent step. Typical values of $c$ range from 3 to 4. Max-norm regularization helps to combat the tendency of dropout to produce very large weights, especially in the later stages of training.

The choice of the dropout rate $p$ is also important. We typically use $p = 0.5$ for hidden units and $p = 0.2$ (or no dropout) for the input units. These are reasonable defaults for a wide range of tasks. For some tasks, tuning $p$ can give significant improvements.

During training with dropout, the gradient of the loss is averaged over the mini-batch using only the weights and activations of the currently active (non-dropped) units. Backpropagation is applied as normal, but only to the thinned network. The gradients for the weights of the dropped units are set to zero.

At test time, we do not use dropout. Instead, we use the full network with all units present but with the weights scaled as described earlier. This is an approximation to averaging the predictions of all possible thinned networks, which would be computationally expensive. The approximation works well in practice.

---

### النسخة العربية

تدريب شبكة عصبية مع dropout يشبه إلى حد كبير تدريب شبكة عصبية قياسية. يتم حساب التدرج بشكل طبيعي، باستثناء أنه يُحسب فقط للشبكة المخففة. في كل حالة تدريب، يتم أخذ عينة من شبكة مخففة جديدة وتدريبها. لذلك يتم حساب كل تحديث للمعاملات باستخدام شبكة مخففة مختلفة.

نقوم بتدريب الشبكات العصبية باستخدام dropout من خلال الانحدار التدرجي العشوائي مع دفعات صغيرة. يتم حساب متوسط التدرجات لكل معامل على حالات التدريب في كل دفعة صغيرة. يتم استخدام طريقة الزخم القياسية. معاملات معدل التعلم والزخم وتضاؤل الأوزان المستخدمة مشابهة لتلك المستخدمة في تدريب الشبكات العصبية القياسية. ومع ذلك، فإن تدريب dropout أبطأ ونجد أنه من المفيد استخدام معدل تعلم أعلى وزخم أعلى.

يمكن دمج dropout مع أشكال أخرى من التنظيم مثل تنظيم القاعدة القصوى (max-norm regularization). نقيد قاعدة متجه الأوزان الواردة عند كل وحدة مخفية لتكون محدودة بثابت $c$. غالباً ما يُطلق على هذا تنظيم القاعدة القصوى. نفرض هذا القيد عن طريق إسقاط $\mathbf{w}$ على كرة نصف قطرها $c$ متمركزة عند الأصل كلما كان $\|\mathbf{w}\| > c$ بعد خطوة الانحدار التدرجي. تتراوح القيم النموذجية لـ $c$ من 3 إلى 4. يساعد تنظيم القاعدة القصوى على مكافحة ميل dropout إلى إنتاج أوزان كبيرة جداً، خاصة في المراحل اللاحقة من التدريب.

اختيار معدل dropout $p$ مهم أيضاً. نستخدم عادة $p = 0.5$ للوحدات المخفية و $p = 0.2$ (أو بدون dropout) لوحدات الإدخال. هذه إعدادات افتراضية معقولة لمجموعة واسعة من المهام. بالنسبة لبعض المهام، يمكن أن يؤدي ضبط $p$ إلى تحسينات كبيرة.

أثناء التدريب مع dropout، يتم حساب متوسط تدرج الخسارة على الدفعة الصغيرة باستخدام الأوزان والتفعيلات فقط للوحدات النشطة حالياً (غير المسقطة). يتم تطبيق الانتشار العكسي بشكل طبيعي، ولكن فقط على الشبكة المخففة. يتم تعيين تدرجات أوزان الوحدات المسقطة إلى صفر.

في وقت الاختبار، لا نستخدم dropout. بدلاً من ذلك، نستخدم الشبكة الكاملة مع جميع الوحدات الموجودة ولكن مع قياس الأوزان كما هو موضح سابقاً. هذا تقريب لحساب متوسط تنبؤات جميع الشبكات المخففة الممكنة، والذي سيكون مكلفاً من الناحية الحسابية. التقريب يعمل بشكل جيد في الممارسة العملية.

---

### Translation Notes

- **Key concepts:**
  - Backpropagation through thinned networks
  - Stochastic gradient descent with mini-batches
  - Max-norm regularization as complementary technique
  - Hyperparameter choices (p=0.5 for hidden, p=0.2 for input)
  - Test-time approximation

- **Technical terms:**
  - "stochastic gradient descent" - translated as "الانحدار التدرجي العشوائي"
  - "mini-batch" - translated as "دفعة صغيرة"
  - "momentum" - translated as "الزخم"
  - "max-norm regularization" - translated as "تنظيم القاعدة القصوى"
  - "weight decay" - translated as "تضاؤل الأوزان"
  - "backpropagation" - translated as "الانتشار العكسي"

- **Mathematical notation:**
  - $c$ - constraint constant for max-norm
  - $p$ - dropout probability
  - $\|\mathbf{w}\|$ - norm of weight vector

- **Practical insights:**
  - Dropout requires higher learning rate
  - Typical dropout rates: 0.5 for hidden layers, 0.2 for input
  - Max-norm values typically 3-4

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
