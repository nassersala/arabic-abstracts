# Section 7: Conclusions
## القسم 7: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** deep neural networks, differential privacy, privacy loss, moments accountant, DP-SGD, TensorFlow, MNIST, CIFAR-10, privacy budget, stochastic gradient descent, first-order optimization, LSTMs, language modeling

---

### English Version

We demonstrate the training of deep neural networks with differential privacy, incurring a modest total privacy loss, computed over entire models with many parameters. In our experiments for MNIST, we achieve 97% training accuracy and for CIFAR-10 we achieve 73% accuracy, both with (8,10⁻⁵)-differential privacy. Our algorithms are based on a differentially private version of stochastic gradient descent; they run on the TensorFlow software library for machine learning. Since our approach applies directly to gradient computations, it can be adapted to many other classical and more recent first-order optimization methods, such as NAG, Momentum, AdaGrad, or SVRG.

A new tool, which may be of independent interest, is a mechanism for tracking privacy loss, the moments accountant. It permits tight automated analysis of the privacy loss of complex composite mechanisms that are currently beyond the reach of advanced composition theorems.

A number of avenues for further work are attractive. In particular, we would like to consider other classes of deep networks. Our experience with MNIST and CIFAR-10 should be helpful, but we see many opportunities for new research, for example in applying our techniques to LSTMs used for language modeling tasks. In addition, we would like to obtain additional improvements in accuracy. Many training datasets are much larger than those of MNIST and CIFAR-10; accuracy should benefit from their size.

---

### النسخة العربية

نوضح تدريب الشبكات العصبية العميقة مع الخصوصية التفاضلية، متكبدين خسارة خصوصية إجمالية متواضعة، محسوبة على نماذج كاملة بمعاملات عديدة. في تجاربنا لـ MNIST، نحقق دقة تدريب 97% ولـ CIFAR-10 نحقق دقة 73%، كلاهما مع خصوصية تفاضلية (8,10⁻⁵). تعتمد خوارزمياتنا على نسخة خاصة بالخصوصية التفاضلية من الانحدار التدرجي العشوائي؛ تعمل على مكتبة البرمجيات TensorFlow لتعلم الآلة. نظراً لأن نهجنا ينطبق مباشرة على حسابات التدرج، يمكن تكييفه مع العديد من طرق التحسين من الرتبة الأولى الكلاسيكية والأحدث، مثل NAG، أو Momentum، أو AdaGrad، أو SVRG.

أداة جديدة، قد تكون ذات اهتمام مستقل، هي آلية لتتبع خسارة الخصوصية، وهي محاسب العزوم. يسمح بالتحليل الآلي المحكم لخسارة الخصوصية للآليات المركبة المعقدة التي هي حالياً خارج نطاق مبرهنات التركيب المتقدمة.

هناك عدد من السبل للعمل الإضافي جذابة. على وجه الخصوص، نود النظر في فئات أخرى من الشبكات العميقة. يجب أن تكون تجربتنا مع MNIST و CIFAR-10 مفيدة، لكننا نرى العديد من الفرص للبحث الجديد، على سبيل المثال في تطبيق تقنياتنا على شبكات LSTM المستخدمة لمهام نمذجة اللغة. بالإضافة إلى ذلك، نود الحصول على تحسينات إضافية في الدقة. العديد من مجموعات بيانات التدريب أكبر بكثير من تلك الخاصة بـ MNIST و CIFAR-10؛ يجب أن تستفيد الدقة من حجمها.

---

### Translation Notes

- **Key contributions:**
  - Demonstrated practical deep learning with strong privacy guarantees
  - Introduced moments accountant for tighter privacy bounds
  - Achieved 97% (MNIST) and 73% (CIFAR-10) with (8,10⁻⁵)-DP
  - Applicable to various first-order optimization methods

- **Technical terms:**
  - "first-order optimization methods" - طرق التحسين من الرتبة الأولى
  - "NAG" (Nesterov Accelerated Gradient) - kept as abbreviation
  - "Momentum" - kept in English (standard ML term)
  - "AdaGrad" - kept in English (algorithm name)
  - "SVRG" (Stochastic Variance Reduced Gradient) - kept as abbreviation
  - "LSTMs" - kept in English (Long Short-Term Memory networks)
  - "language modeling" - نمذجة اللغة

- **Future work:**
  - Extending to other network architectures (LSTMs)
  - Improving accuracy on more complex tasks
  - Leveraging larger datasets

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
