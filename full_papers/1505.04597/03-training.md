# Section 3: Training
## القسم 3: التدريب

**Section:** training
**Translation Quality:** 0.86
**Glossary Terms Used:** training, data augmentation, loss function, optimization, stochastic gradient descent, momentum, weight initialization, GPU, batch normalization

---

### English Version

The input images and their corresponding segmentation maps are used to train the network with the stochastic gradient descent implementation of Caffe [6]. Due to the unpadded convolutions, the output image is smaller than the input by a constant border width. To minimize the overhead and make maximum use of the GPU memory, we favor large input tiles over a large batch size and hence reduce the batch to a single image. Accordingly we use a high momentum (0.99) such that a large number of the previously seen training samples determine the update in the current optimization step.

The energy function is computed by a pixel-wise soft-max over the final feature map combined with the cross entropy loss function. The soft-max is defined as

$$p_k(x) = \frac{\exp(a_k(x))}{\sum_{k'=1}^{K} \exp(a_{k'}(x))}$$

where $a_k(x)$ denotes the activation in feature channel $k$ at the pixel position $x \in \Omega$ with $\Omega \subset \mathbb{Z}^2$. $K$ is the number of classes and $p_k(x)$ is the approximated maximum-function. I.e. $p_k(x) \approx 1$ for the $k$ that has the maximum activation $a_k(x)$ and $p_k(x) \approx 0$ for all other $k$. The cross entropy then penalizes at each position the deviation of $p_{\ell(x)}(x)$ from 1 using

$$E = \sum_{x \in \Omega} w(x) \log(p_{\ell(x)}(x))$$

where $\ell: \Omega \rightarrow \{1,...,K\}$ is the true label of each pixel and $w: \Omega \rightarrow \mathbb{R}$ is a weight map that we introduced to give some pixels more importance in the training.

We pre-compute the weight map for each ground truth segmentation to compensate the different frequency of pixels from a certain class in the training data set, and to force the network to learn the small separation borders that we introduce between touching cells (See Figure 3c and d).

The separation border is computed using morphological operations. The weight map is then computed as

$$w(x) = w_c(x) + w_0 \cdot \exp\left(-\frac{(d_1(x)+d_2(x))^2}{2\sigma^2}\right)$$

where $w_c: \Omega \rightarrow \mathbb{R}$ is the weight map to balance the class frequencies, $d_1: \Omega \rightarrow \mathbb{R}$ denotes the distance to the border of the nearest cell and $d_2: \Omega \rightarrow \mathbb{R}$ the distance to the border of the second nearest cell. In our experiments we set $w_0 = 10$ and $\sigma \approx 5$ pixels.

In deep networks with many convolutional layers and different paths through the network, a good initialization of the weights is extremely important. Otherwise, parts of the network might give excessive activations, while other parts never contribute. Ideally the initial weights should be adapted such that each feature map in the network has approximately unit variance. For a network with our architecture (alternating convolution and ReLU layers) this can be achieved by drawing the initial weights from a Gaussian distribution with a standard deviation of $\sqrt{2/N}$, where $N$ denotes the number of incoming nodes of one neuron [5]. E.g. for a 3x3 convolution and 64 feature channels in the previous layer $N = 9 \cdot 64 = 576$.

**Data Augmentation.** Data augmentation is essential to teach the network the desired invariance and robustness properties, when only few training samples are available. In case of microscopical images we primarily need shift and rotation invariance as well as robustness to deformations and gray value variations. Especially random elastic deformations of the training samples seem to be the key concept to train a segmentation network with very few annotated images. We generate smooth deformations using random displacement vectors on a coarse 3 by 3 grid. The displacements are sampled from a Gaussian distribution with 10 pixels standard deviation. Per-pixel displacements are then computed using bicubic interpolation. Drop-out layers at the end of the contracting path perform further implicit data augmentation.

---

### النسخة العربية

يتم استخدام الصور المدخلة وخرائط التجزئة المقابلة لها لتدريب الشبكة بتطبيق الانحدار التدرجي العشوائي من Caffe [6]. بسبب الالتفافات بدون حشو، تكون الصورة الناتجة أصغر من المدخل بعرض حدود ثابت. لتقليل التكلفة الإضافية وتحقيق أقصى استفادة من ذاكرة وحدة معالجة الرسومات، نفضل البلاطات المدخلة الكبيرة على حجم دفعة كبير وبالتالي نقلل الدفعة إلى صورة واحدة. وبناءً على ذلك، نستخدم زخماً عالياً (0.99) بحيث يحدد عدد كبير من عينات التدريب المشاهدة مسبقاً التحديث في خطوة التحسين الحالية.

يتم حساب دالة الطاقة بواسطة سوفت ماكس بحسب البكسل على خريطة الميزات النهائية مجتمعة مع دالة خسارة الإنتروبيا التقاطعية. يتم تعريف السوفت ماكس كما يلي:

$$p_k(x) = \frac{\exp(a_k(x))}{\sum_{k'=1}^{K} \exp(a_{k'}(x))}$$

حيث $a_k(x)$ تشير إلى التنشيط في قناة الميزات $k$ عند موضع البكسل $x \in \Omega$ مع $\Omega \subset \mathbb{Z}^2$. $K$ هو عدد الأصناف و $p_k(x)$ هي دالة القيمة العظمى التقريبية. أي $p_k(x) \approx 1$ لـ $k$ التي لديها أقصى تنشيط $a_k(x)$ و $p_k(x) \approx 0$ لجميع $k$ الأخرى. ثم تعاقب الإنتروبيا التقاطعية في كل موضع انحراف $p_{\ell(x)}(x)$ عن 1 باستخدام:

$$E = \sum_{x \in \Omega} w(x) \log(p_{\ell(x)}(x))$$

حيث $\ell: \Omega \rightarrow \{1,...,K\}$ هي التسمية الحقيقية لكل بكسل و $w: \Omega \rightarrow \mathbb{R}$ هي خريطة أوزان قدمناها لإعطاء بعض البكسلات أهمية أكبر في التدريب.

نحسب مسبقاً خريطة الأوزان لكل تجزئة حقيقة أرضية للتعويض عن التردد المختلف للبكسلات من صنف معين في مجموعة بيانات التدريب، وإجبار الشبكة على تعلم حدود الفصل الصغيرة التي نقدمها بين الخلايا المتلامسة (انظر الشكل 3c و d).

يتم حساب حدود الفصل باستخدام العمليات المورفولوجية. ثم يتم حساب خريطة الأوزان كما يلي:

$$w(x) = w_c(x) + w_0 \cdot \exp\left(-\frac{(d_1(x)+d_2(x))^2}{2\sigma^2}\right)$$

حيث $w_c: \Omega \rightarrow \mathbb{R}$ هي خريطة الأوزان لموازنة ترددات الأصناف، $d_1: \Omega \rightarrow \mathbb{R}$ تشير إلى المسافة إلى حدود أقرب خلية و $d_2: \Omega \rightarrow \mathbb{R}$ المسافة إلى حدود ثاني أقرب خلية. في تجاربنا قمنا بتعيين $w_0 = 10$ و $\sigma \approx 5$ بكسلات.

في الشبكات العميقة ذات العديد من الطبقات الالتفافية والمسارات المختلفة عبر الشبكة، يكون التهيئة الجيدة للأوزان مهماً للغاية. وإلا، قد تعطي أجزاء من الشبكة تنشيطات مفرطة، بينما لا تساهم أجزاء أخرى أبداً. من الناحية المثالية، يجب تكييف الأوزان الأولية بحيث يكون لكل خريطة ميزات في الشبكة تباين وحدة تقريباً. بالنسبة لشبكة بمعماريتنا (طبقات التفاف و ReLU متناوبة) يمكن تحقيق ذلك من خلال سحب الأوزان الأولية من توزيع غاوسي بانحراف معياري قدره $\sqrt{2/N}$، حيث $N$ تشير إلى عدد العقد الواردة لعصبون واحد [5]. على سبيل المثال، لالتفاف 3×3 و 64 قناة ميزات في الطبقة السابقة $N = 9 \cdot 64 = 576$.

**زيادة البيانات.** تعد زيادة البيانات أمراً أساسياً لتعليم الشبكة خصائص الثبات والمتانة المطلوبة، عندما تكون عينات التدريب قليلة فقط متاحة. في حالة الصور المجهرية، نحتاج في المقام الأول إلى ثبات الإزاحة والدوران بالإضافة إلى المتانة أمام التشوهات والتغيرات في القيم الرمادية. يبدو أن التشوهات المرنة العشوائية لعينات التدريب على وجه الخصوص هي المفهوم الرئيسي لتدريب شبكة تجزئة بصور موسومة قليلة جداً. نقوم بتوليد تشوهات سلسة باستخدام متجهات إزاحة عشوائية على شبكة خشنة 3 في 3. يتم أخذ عينات الإزاحات من توزيع غاوسي بانحراف معياري قدره 10 بكسلات. ثم يتم حساب الإزاحات لكل بكسل باستخدام الاستيفاء التكعيبي الثنائي. تقوم طبقات الإسقاط في نهاية المسار الانقباضي بزيادة بيانات ضمنية إضافية.

---

### Translation Notes

- **Figures referenced:** Figure 3c, Figure 3d
- **Key terms introduced:** soft-max, cross entropy loss, weight map, class frequency balancing, elastic deformations, drop-out layers, Gaussian distribution, morphological operations
- **Equations:** 3 main equations (soft-max, cross entropy, weight map formula)
- **Citations:** [5], [6] (Caffe framework)
- **Special handling:** Mathematical notation preserved in LaTeX, technical parameters (momentum=0.99, w_0=10, σ≈5, N=576)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
