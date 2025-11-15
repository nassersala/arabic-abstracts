# Section 2: Towards Reducing Internal Covariate Shift
## القسم 2: نحو تقليل التحول التبايني الداخلي

**Section:** theoretical-foundations
**Translation Quality:** 0.87
**Glossary Terms Used:** normalization, whitening, training, convergence, gradient descent, layers, activation, covariance matrix, mini-batch

---

### English Version

We define Internal Covariate Shift as the change in the distribution of network activations due to the change in network parameters during training. To improve the training, we seek to reduce the internal covariate shift. By fixing the distribution of the layer inputs $x$ as the training progresses, we expect to improve the training speed. It has been long known that the network training converges faster if its inputs are whitened – i.e., linearly transformed to have zero means and unit variances, and decorrelated. As each layer observes the inputs produced by the layers below, it would be advantageous to achieve the same whitening of the inputs of each layer. By whitening the inputs to each layer, we would take a step towards achieving the fixed distributions of inputs that would remove the ill effects of the internal covariate shift.

We could consider whitening activations at every training step or at some interval, either by modifying the network directly, or by changing the parameters of the optimization algorithm to depend on the network activation values. However, if we are to use gradient descent, we would need to compute the Jacobians of the transformation of the data by the whitening operation, which is computationally expensive and not everywhere differentiable. This motivates us to seek an alternative that performs input normalization in a way that is differentiable and does not require the analysis of the entire training set after every parameter update.

Some of the previous approaches (e.g., LeCun et al., 1998b; Wiesler & Ney, 2011) use statistics computed over a single training example, or, in the case of image networks, over different feature maps at a given location. However, this changes the representation ability of a network by discarding the absolute scale of activations. We want to a preserve the information in the network, by normalizing the activations in a training example relative to the statistics of the entire training data.

---

### النسخة العربية

نُعرّف التحول التبايني الداخلي على أنه التغيير في توزيع تنشيطات الشبكة بسبب التغيير في معاملات الشبكة أثناء التدريب. لتحسين التدريب، نسعى إلى تقليل التحول التبايني الداخلي. من خلال تثبيت توزيع مدخلات الطبقة $x$ مع تقدم التدريب، نتوقع تحسين سرعة التدريب. من المعروف منذ فترة طويلة أن تدريب الشبكة يتقارب بشكل أسرع إذا تم تبييض مدخلاتها (Whitening) - أي تحويلها خطياً لتصبح ذات متوسطات صفرية وتباينات أحادية، وغير مرتبطة. نظراً لأن كل طبقة تراقب المدخلات التي تنتجها الطبقات أدناه، سيكون من المفيد تحقيق نفس التبييض لمدخلات كل طبقة. من خلال تبييض المدخلات لكل طبقة، سنخطو خطوة نحو تحقيق التوزيعات الثابتة للمدخلات التي من شأنها إزالة الآثار السيئة للتحول التبايني الداخلي.

يمكننا النظر في تبييض التنشيطات في كل خطوة تدريب أو على فترات معينة، إما عن طريق تعديل الشبكة مباشرة، أو عن طريق تغيير معاملات خوارزمية التحسين لتعتمد على قيم تنشيط الشبكة. ومع ذلك، إذا كنا سنستخدم الانحدار التدرجي، فسنحتاج إلى حساب مصفوفات جاكوبيان (Jacobians) لتحويل البيانات بواسطة عملية التبييض، وهو أمر مكلف حسابياً وليس قابلاً للتفاضل في كل مكان. هذا يحفزنا للبحث عن بديل يقوم بتطبيع المدخلات بطريقة قابلة للتفاضل ولا تتطلب تحليل مجموعة التدريب بأكملها بعد كل تحديث للمعاملات.

تستخدم بعض الأساليب السابقة (مثل LeCun et al., 1998b; Wiesler & Ney, 2011) إحصائيات محسوبة على مثال تدريب واحد، أو، في حالة شبكات الصور، على خرائط ميزات مختلفة في موقع معين. ومع ذلك، هذا يغير قدرة التمثيل للشبكة من خلال تجاهل المقياس المطلق للتنشيطات. نريد الحفاظ على المعلومات في الشبكة، من خلال تطبيع التنشيطات في مثال التدريب بالنسبة لإحصائيات بيانات التدريب بأكملها.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Whitening (التبييض)
  - Decorrelated (غير مرتبطة)
  - Jacobian (مصفوفة جاكوبيان)
  - Feature maps (خرائط الميزات)
  - Absolute scale (المقياس المطلق)
- **Equations:** None explicit, mathematical concepts discussed
- **Citations:** LeCun et al., 1998b; Wiesler & Ney, 2011
- **Special handling:** Mathematical terminology preserved; whitening concept explained in context

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
