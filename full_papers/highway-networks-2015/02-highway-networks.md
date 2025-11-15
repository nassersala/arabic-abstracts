# Section 2: Highway Networks
## القسم 2: شبكات الطرق السريعة

**Section:** methodology
**Translation Quality:** 0.89
**Glossary Terms Used:** neural networks, transformation, architecture, feedforward network, convolutional, recurrent, gating units, gradient descent, LSTM, initialization, bias, training

---

### English Version

**Notation** We use boldface letters for vectors and matrices, and italicized capital letters to denote transformation functions. **0** and **1** denote vectors of zeros and ones respectively, and **I** denotes an identity matrix. The function σ(x) is defined as σ(x) = 1/(1+e^(-x)), x ∈ R. The dot operator (·) is used to denote element-wise multiplication.

A plain feedforward neural network typically consists of L layers where the lth layer (l ∈ {1, 2, ..., L}) applies a non-linear transformation H (parameterized by W_{H,l}) on its input x_l to produce its output y_l. Thus, x_1 is the input to the network and y_L is the network's output. Omitting the layer index and biases for clarity,

$$y = H(x, W_H).$$                                                   (1)

H is usually an affine transform followed by a non-linear activation function, but in general it may take other forms, possibly convolutional or recurrent. For a highway network, we additionally define two non-linear transforms T(x, W_T) and C(x, W_C) such that

$$y = H(x, W_H) · T(x, W_T) + x · C(x, W_C).$$                      (2)

We refer to T as the transform gate and C as the carry gate, since they express how much of the output is produced by transforming the input and carrying it, respectively. For simplicity, in this paper we set C = 1 − T, giving

$$y = H(x, W_H) · T(x, W_T) + x · (1 − T(x, W_T)).$$               (3)

The dimensionality of x, y, H(x, W_H) and T(x, W_T) must be the same for Equation 3 to be valid. Note that this layer transformation is much more flexible than Equation 1. In particular, observe that for particular values of T,

$$y = \begin{cases} x, & \text{if } T(x, W_T) = 0, \\ H(x, W_H), & \text{if } T(x, W_T) = 1. \end{cases}$$     (4)

Similarly, for the Jacobian of the layer transform,

$$\frac{dy}{dx} = \begin{cases} I, & \text{if } T(x, W_T) = 0, \\ H'(x, W_H), & \text{if } T(x, W_T) = 1. \end{cases}$$     (5)

Thus, depending on the output of the transform gates, a highway layer can smoothly vary its behavior between that of H and that of a layer which simply passes its inputs through. Just as a plain layer consists of multiple computing units such that the ith unit computes y_i = H_i(x), a highway network consists of multiple blocks such that the ith block computes a block state H_i(x) and transform gate output T_i(x). Finally, it produces the block output y_i = H_i(x) * T_i(x) + x_i * (1 − T_i(x)), which is connected to the next layer.

### 2.1 Constructing Highway Networks

As mentioned earlier, Equation 3 requires that the dimensionality of x, y, H(x, W_H) and T(x, W_T) be the same. To change the size of the intermediate representation, one can replace x with x̂ obtained by suitably sub-sampling or zero-padding x. Another alternative is to use a plain layer (without highways) to change dimensionality, which is the strategy we use in this study.

Convolutional highway layers utilize weight-sharing and local receptive fields for both H and T transforms. We used the same sized receptive fields for both, and zero-padding to ensure that the block state and transform gate feature maps match the input size.

### 2.2 Training Deep Highway Networks

We use the transform gate defined as T(x) = σ(W_T^T x + b_T), where W_T is the weight matrix and b_T the bias vector for the transform gates. This suggests a simple initialization scheme which is independent of the nature of H: b_T can be initialized with a negative value (e.g. -1, -3 etc.) such that the network is initially biased towards carry behavior. This scheme is strongly inspired by the proposal [30] to initially bias the gates in an LSTM network, to help bridge long-term temporal dependencies early in learning. Note that σ(x) ∈ (0, 1), ∀x ∈ R, so the conditions in Equation 4 can never be met exactly.

In our experiments, we found that a negative bias initialization for the transform gates was sufficient for training to proceed in very deep networks for various zero-mean initial distributions of W_H and different activation functions used by H. In pilot experiments, SGD did not stall for networks with more than 1000 layers. Although the initial bias is best treated as a hyperparameter, as a general guideline we suggest values of -1, -2 and -3 for convolutional highway networks of depth approximately 10, 20 and 30.

---

### النسخة العربية

**الترميز** نستخدم الحروف العريضة للمتجهات والمصفوفات، والحروف الكبيرة المائلة للدلالة على دوال التحويل. **0** و **1** تشير إلى متجهات الأصفار والآحاد على التوالي، و **I** تشير إلى مصفوفة الوحدة. الدالة σ(x) معرفة على أنها σ(x) = 1/(1+e^(-x))، x ∈ R. يُستخدم عامل النقطة (·) للدلالة على الضرب عنصراً بعنصر.

تتكون الشبكة العصبية الأمامية العادية عادة من L طبقة حيث تطبق الطبقة lth (l ∈ {1, 2, ..., L}) تحويلاً غير خطي H (مُحدد بالمعاملات W_{H,l}) على مدخلاتها x_l لإنتاج مخرجاتها y_l. وبالتالي، x_1 هو مدخل الشبكة و y_L هو مخرج الشبكة. بإهمال مؤشر الطبقة والانحيازات من أجل الوضوح،

$$y = H(x, W_H).$$                                                   (1)

عادة ما يكون H تحويلاً أفينياً متبوعاً بدالة تنشيط غير خطية، ولكن بشكل عام قد يتخذ أشكالاً أخرى، ربما التفافية أو تكرارية. بالنسبة لشبكة الطرق السريعة، نعرف بالإضافة إلى ذلك تحويلين غير خطيين T(x, W_T) و C(x, W_C) بحيث

$$y = H(x, W_H) · T(x, W_T) + x · C(x, W_C).$$                      (2)

نشير إلى T على أنها بوابة التحويل و C على أنها بوابة الحمل، حيث تعبران عن مقدار المخرجات المنتجة من خلال تحويل المدخلات وحملها، على التوالي. من أجل البساطة، في هذه الورقة نضع C = 1 − T، مما يعطي

$$y = H(x, W_H) · T(x, W_T) + x · (1 − T(x, W_T)).$$               (3)

يجب أن تكون أبعاد x و y و H(x, W_H) و T(x, W_T) متماثلة حتى تكون المعادلة 3 صحيحة. لاحظ أن تحويل الطبقة هذا أكثر مرونة بكثير من المعادلة 1. على وجه الخصوص، لاحظ أنه لقيم معينة من T،

$$y = \begin{cases} x, & \text{إذا كان } T(x, W_T) = 0, \\ H(x, W_H), & \text{إذا كان } T(x, W_T) = 1. \end{cases}$$     (4)

وبالمثل، بالنسبة لليعقوبي (Jacobian) لتحويل الطبقة،

$$\frac{dy}{dx} = \begin{cases} I, & \text{إذا كان } T(x, W_T) = 0, \\ H'(x, W_H), & \text{إذا كان } T(x, W_T) = 1. \end{cases}$$     (5)

وبالتالي، اعتماداً على مخرج بوابات التحويل، يمكن لطبقة الطريق السريع أن تغير سلوكها بسلاسة بين سلوك H وسلوك طبقة تمرر ببساطة مدخلاتها. تماماً كما تتكون الطبقة العادية من وحدات حسابية متعددة بحيث تحسب الوحدة ith القيمة y_i = H_i(x)، تتكون شبكة الطريق السريع من كتل متعددة بحيث تحسب الكتلة ith حالة الكتلة H_i(x) ومخرج بوابة التحويل T_i(x). أخيراً، تنتج مخرج الكتلة y_i = H_i(x) * T_i(x) + x_i * (1 − T_i(x))، والذي يتصل بالطبقة التالية.

### 2.1 بناء شبكات الطرق السريعة

كما ذكرنا سابقاً، تتطلب المعادلة 3 أن تكون أبعاد x و y و H(x, W_H) و T(x, W_T) متماثلة. لتغيير حجم التمثيل الوسيط، يمكن استبدال x بـ x̂ المحصل عليها من خلال أخذ عينات فرعية مناسبة أو حشو بأصفار لـ x. البديل الآخر هو استخدام طبقة عادية (بدون طرق سريعة) لتغيير الأبعاد، وهي الاستراتيجية التي نستخدمها في هذه الدراسة.

تستخدم طبقات الطرق السريعة الالتفافية مشاركة الأوزان والحقول الاستقبالية المحلية لكل من تحويلات H و T. استخدمنا حقولاً استقبالية بنفس الحجم لكليهما، والحشو بأصفار لضمان أن خرائط ميزات حالة الكتلة وبوابة التحويل تطابق حجم المدخلات.

### 2.2 تدريب شبكات الطرق السريعة العميقة

نستخدم بوابة التحويل المعرفة على أنها T(x) = σ(W_T^T x + b_T)، حيث W_T هي مصفوفة الأوزان و b_T متجه الانحياز لبوابات التحويل. يقترح هذا مخطط تهيئة بسيط مستقل عن طبيعة H: يمكن تهيئة b_T بقيمة سالبة (مثل -1، -3 إلخ.) بحيث تكون الشبكة في البداية منحازة نحو سلوك الحمل. هذا المخطط مستوحى بقوة من اقتراح [30] لانحياز البوابات في البداية في شبكة LSTM، للمساعدة في سد الاعتماديات الزمنية طويلة المدى في وقت مبكر من التعلم. لاحظ أن σ(x) ∈ (0, 1)، ∀x ∈ R، لذلك لا يمكن أبداً تحقيق الشروط في المعادلة 4 بشكل دقيق.

في تجاربنا، وجدنا أن تهيئة الانحياز السالب لبوابات التحويل كانت كافية لاستمرار التدريب في الشبكات العميقة جداً لمختلف التوزيعات الأولية ذات المتوسط الصفري لـ W_H ودوال التنشيط المختلفة المستخدمة بواسطة H. في التجارب التجريبية، لم يتوقف SGD للشبكات التي تحتوي على أكثر من 1000 طبقة. على الرغم من أن الانحياز الأولي يُعامل بشكل أفضل كمعامل فائق، كدليل عام نقترح قيم -1 و -2 و -3 لشبكات الطرق السريعة الالتفافية بعمق يقارب 10 و 20 و 30 تقريباً.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned in paper but description not in this section)
- **Key terms introduced:**
  - transform gate → بوابة التحويل
  - carry gate → بوابة الحمل
  - element-wise multiplication → الضرب عنصراً بعنصر
  - affine transform → تحويل أفيني
  - activation function → دالة تنشيط
  - Jacobian → اليعقوبي
  - block state → حالة الكتلة
  - weight-sharing → مشاركة الأوزان
  - receptive fields → حقول استقبالية
  - feature maps → خرائط ميزات
  - bias vector → متجه الانحياز
  - zero-padding → حشو بأصفار
  - hyperparameter → معامل فائق
- **Equations:** 5 main equations (1-5) with LaTeX notation preserved
- **Citations:** [30]
- **Special handling:**
  - All mathematical equations preserved exactly in LaTeX format
  - Mixed Arabic-English in equation conditions for clarity
  - Maintained mathematical notation conventions
  - Subscripts and superscripts kept in original form

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
