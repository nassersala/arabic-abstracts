---
# Neural Ordinary Differential Equations
## المعادلات التفاضلية العادية العصبية

**arXiv ID:** 1806.07366
**Authors:** Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud
**Year:** 2018
**Categories:** cs.LG, cs.AI, stat.ML
**Translation Quality:** 0.89
**Glossary Terms Used:** neural network, deep learning, derivative, memory, residual, latent, training, backpropagate, generative

### English Abstract
We introduce a new family of deep neural network models. Instead of specifying a discrete sequence of hidden layers, we parameterize the derivative of the hidden state using a neural network. The output of the network is computed using a black-box differential equation solver. These continuous-depth models have constant memory cost, adapt their evaluation strategy to each input, and can explicitly trade numerical precision for speed. We demonstrate these properties in continuous-depth residual networks and continuous-time latent variable models. We also construct continuous normalizing flows, a generative model that can train by maximum likelihood, without partitioning or ordering the data dimensions. For training, we show how to scalably backpropagate through any ODE solver, without access to its internal operations. This allows end-to-end training of ODEs within larger models.

### الملخص العربي
نقدم عائلة جديدة من نماذج الشبكات العصبية العميقة. بدلاً من تحديد تسلسل منفصل من الطبقات المخفية، نحدد بارامتراً للمشتقة للحالة المخفية باستخدام شبكة عصبية. يتم حساب مخرجات الشبكة باستخدام حلال معادلات تفاضلية صندوق أسود. هذه النماذج ذات العمق المستمر لها تكلفة ذاكرة ثابتة، وتكيف استراتيجية التقييم الخاصة بها لكل مدخل، ويمكنها المقايضة بشكل صريح بين الدقة العددية والسرعة. نوضح هذه الخصائص في الشبكات المتبقية ذات العمق المستمر ونماذج المتغيرات الكامنة ذات الزمن المستمر. نقوم أيضاً ببناء تدفقات التطبيع المستمر، وهو نموذج توليدي يمكن تدريبه بأقصى احتمالية، دون تقسيم أو ترتيب أبعاد البيانات. للتدريب، نوضح كيفية الانتشار العكسي بشكل قابل للتوسع عبر أي حلال لمعادلة تفاضلية عادية، دون الوصول إلى عملياته الداخلية. هذا يسمح بالتدريب الشامل للمعادلات التفاضلية العادية ضمن نماذج أكبر.

### Back-Translation (Validation)
We present a new family of deep neural network models. Instead of specifying a discrete sequence of hidden layers, we parameterize the derivative of the hidden state using a neural network. The network outputs are computed using a black-box differential equation solver. These continuous-depth models have constant memory cost, adapt their evaluation strategy for each input, and can explicitly trade off between numerical precision and speed. We demonstrate these properties in continuous-depth residual networks and continuous-time latent variable models. We also construct continuous normalizing flows, which is a generative model that can be trained with maximum likelihood, without partitioning or ordering the data dimensions. For training, we show how to scalably backpropagate through any ordinary differential equation solver, without access to its internal operations. This allows end-to-end training of ordinary differential equations within larger models.

### Translation Metrics
- Iterations: 1
- Final Score: 0.89
- Quality: High
---
