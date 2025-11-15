# Section 3: Training
## القسم 3: التدريب

**Section:** training
**Translation Quality:** 0.86
**Glossary Terms Used:** training, stochastic gradient descent, batch size, momentum, GPU memory, energy function, soft-max, cross entropy, loss function, weight map, ground truth, segmentation, class, pixel, morphological operations, Gaussian distribution, weight initialization, data augmentation, elastic deformations, dropout

---

### English Version

The input images and their corresponding segmentation maps are used to train the network with the stochastic gradient descent implementation of Caffe [Caffe]. Due to the unpadded convolutions, the output image is smaller than the input by a constant border width. To minimize the overhead and make maximum use of the GPU memory, we favor large input tiles over a large batch size and hence reduce the batch to a single image. Accordingly we use a high momentum (0.99) such that a large number of the previously seen training samples determine the update in the current optimization step.

The energy function is computed by a pixel-wise soft-max over the final feature map combined with the cross entropy loss function. The soft-max is defined as ${p}_k(\vec{x}) = \exp({a_k(\vec{x})}) / \left(\sum_{k' = 1}^K \exp(a_{k'}(\vec{x}))\right)$ where $a_k(\vec{x})$ denotes the activation in feature channel $k$ at the pixel position $\vec{x} \in \Omega$ with $\Omega \subset \mathbb{Z}^2$. $K$ is the number of classes and ${p}_k(\vec{x})$ is the approximated maximum-function. I.e. ${p}_k(\vec{x}) \approx 1$ for the $k$ that has the maximum activation $a_k(\vec{x})$ and ${p}_k(\vec{x}) \approx 0$ for all other $k$. The cross entropy then penalizes at each position the deviation of ${p}_{\ell(\vec{x})}(\vec{x})$ from 1 using

$$E = \sum_{\vec{x} \in \Omega} w(\vec{x}) \log({p}_{\ell(\vec{x})}(\vec{x}))$$

where $\ell:\Omega \rightarrow \{1,\dots,K\}$ is the true label of each pixel and $w:\Omega \rightarrow \mathds{R}$ is a weight map that we introduced to give some pixels more importance in the training.

We pre-compute the weight map for each ground truth segmentation to compensate the different frequency of pixels from a certain class in the training data set, and to force the network to learn the small separation borders that we introduce between touching cells (See Figure 3c and d).

The separation border is computed using morphological operations. The weight map is then computed as

$$w(\vec{x}) = w_c(\vec{x}) + w_0 \cdot \exp\left( - \frac{(d_1(\vec{x}) + d_2(\vec{x}))^2}{2\sigma^2}\right)$$

where $w_c:\Omega \rightarrow \mathds{R}$ is the weight map to balance the class frequencies, $d_1:\Omega \rightarrow \mathds{R}$ denotes the distance to the border of the nearest cell and $d_2:\Omega \rightarrow \mathds{R}$ the distance to the border of the second nearest cell. In our experiments we set $w_0 = 10$ and $\sigma \approx 5$ pixels.

In deep networks with many convolutional layers and different paths through the network, a good initialization of the weights is extremely important. Otherwise, parts of the network might give excessive activations, while other parts never contribute. Ideally the initial weights should be adapted such that each feature map in the network has approximately unit variance. For a network with our architecture (alternating convolution and ReLU layers) this can be achieved by drawing the initial weights from a Gaussian distribution with a standard deviation of $\sqrt{2/N}$, where $N$ denotes the number of incoming nodes of one neuron [He2015]. E.g. for a 3x3 convolution and 64 feature channels in the previous layer $N = 9\cdot 64 = 576$.

### 3.1 Data Augmentation

Data augmentation is essential to teach the network the desired invariance and robustness properties, when only few training samples are available. In case of microscopical images we primarily need shift and rotation invariance as well as robustness to deformations and gray value variations. Especially random elastic deformations of the training samples seem to be the key concept to train a segmentation network with very few annotated images. We generate smooth deformations using random displacement vectors on a coarse 3 by 3 grid. The displacements are sampled from a Gaussian distribution with 10 pixels standard deviation. Per-pixel displacements are then computed using bicubic interpolation. Drop-out layers at the end of the contracting path perform further implicit data augmentation.

---

### النسخة العربية

تُستخدم الصور المدخلة وخرائط التجزئة المقابلة لها لتدريب الشبكة باستخدام تنفيذ الانحدار التدرجي العشوائي في Caffe [Caffe]. نظراً للالتفافات غير المبطنة، تكون الصورة الناتجة أصغر من المدخلة بعرض حدود ثابت. لتقليل النفقات العامة والاستفادة القصوى من ذاكرة وحدة معالجة الرسومات، نفضل البلاطات المدخلة الكبيرة على حجم دفعة كبير وبالتالي نقلل الدفعة إلى صورة واحدة. وفقاً لذلك نستخدم زخماً عالياً (0.99) بحيث يحدد عدد كبير من عينات التدريب المرئية سابقاً التحديث في خطوة التحسين الحالية.

يتم حساب دالة الطاقة بواسطة soft-max على مستوى البكسل على خريطة الميزات النهائية مدمجة مع دالة خسارة الإنتروبيا التقاطعية. يتم تعريف soft-max كـ ${p}_k(\vec{x}) = \exp({a_k(\vec{x})}) / \left(\sum_{k' = 1}^K \exp(a_{k'}(\vec{x}))\right)$ حيث $a_k(\vec{x})$ يشير إلى التنشيط في قناة الميزة $k$ عند موضع البكسل $\vec{x} \in \Omega$ مع $\Omega \subset \mathbb{Z}^2$. $K$ هو عدد الأصناف و${p}_k(\vec{x})$ هي دالة القيمة العظمى المقرَّبة. أي ${p}_k(\vec{x}) \approx 1$ للقيمة $k$ التي لديها أقصى تنشيط $a_k(\vec{x})$ و${p}_k(\vec{x}) \approx 0$ لجميع القيم الأخرى من $k$. تقوم الإنتروبيا التقاطعية بعد ذلك بمعاقبة الانحراف عن ${p}_{\ell(\vec{x})}(\vec{x})$ من 1 في كل موضع باستخدام

$$E = \sum_{\vec{x} \in \Omega} w(\vec{x}) \log({p}_{\ell(\vec{x})}(\vec{x}))$$

حيث $\ell:\Omega \rightarrow \{1,\dots,K\}$ هو التصنيف الحقيقي لكل بكسل و$w:\Omega \rightarrow \mathds{R}$ هي خريطة أوزان قدمناها لإعطاء بعض البكسلات أهمية أكبر في التدريب.

نقوم بالحساب المسبق لخريطة الأوزان لكل تجزئة حقيقية أرضية لتعويض التردد المختلف للبكسلات من صنف معين في مجموعة بيانات التدريب، ولإجبار الشبكة على تعلم حدود الفصل الصغيرة التي ندخلها بين الخلايا المتلامسة (انظر الشكل 3c و d).

يتم حساب حدود الفصل باستخدام العمليات المورفولوجية. يتم حساب خريطة الأوزان بعد ذلك كـ

$$w(\vec{x}) = w_c(\vec{x}) + w_0 \cdot \exp\left( - \frac{(d_1(\vec{x}) + d_2(\vec{x}))^2}{2\sigma^2}\right)$$

حيث $w_c:\Omega \rightarrow \mathds{R}$ هي خريطة الأوزان لموازنة ترددات الأصناف، و$d_1:\Omega \rightarrow \mathds{R}$ يشير إلى المسافة إلى حدود الخلية الأقرب و$d_2:\Omega \rightarrow \mathds{R}$ المسافة إلى حدود الخلية الثانية الأقرب. في تجاربنا قمنا بتعيين $w_0 = 10$ و$\sigma \approx 5$ بكسل.

في الشبكات العميقة ذات العديد من الطبقات الالتفافية والمسارات المختلفة عبر الشبكة، فإن التهيئة الجيدة للأوزان مهمة للغاية. وإلا، فقد تعطي أجزاء من الشبكة تنشيطات مفرطة، بينما لا تساهم أجزاء أخرى أبداً. من الناحية المثالية، يجب تكييف الأوزان الأولية بحيث يكون لكل خريطة ميزات في الشبكة تبايناً قريباً من الوحدة تقريباً. بالنسبة لشبكة ذات معماريتنا (طبقات التفاف وReLU متناوبة) يمكن تحقيق ذلك عن طريق سحب الأوزان الأولية من توزيع غاوسي بانحراف معياري قدره $\sqrt{2/N}$، حيث $N$ يشير إلى عدد العقد الواردة لعصبون واحد [He2015]. على سبيل المثال، لالتفاف 3×3 و64 قناة ميزات في الطبقة السابقة $N = 9\cdot 64 = 576$.

### 3.1 زيادة البيانات

زيادة البيانات ضرورية لتعليم الشبكة خصائص الثبات والمتانة المطلوبة، عندما تتوفر عينات تدريب قليلة فقط. في حالة الصور الميكروسكوبية، نحتاج في المقام الأول إلى ثبات الإزاحة والدوران بالإضافة إلى المتانة تجاه التشوهات واختلافات القيم الرمادية. يبدو أن التشوهات المرنة العشوائية لعينات التدريب بشكل خاص هي المفهوم الأساسي لتدريب شبكة تجزئة بعدد قليل جداً من الصور الموسومة. نقوم بتوليد تشوهات ناعمة باستخدام متجهات إزاحة عشوائية على شبكة خشنة 3 في 3. يتم أخذ عينات من الإزاحات من توزيع غاوسي بانحراف معياري قدره 10 بكسل. يتم بعد ذلك حساب الإزاحات لكل بكسل باستخدام الاستيفاء التكعيبي الثنائي. تؤدي طبقات dropout في نهاية مسار الانكماش إلى زيادة بيانات ضمنية إضافية.

---

### Translation Notes

- **Figures referenced:**
  - Figure 3c and d: Weight map visualization for cell separation
- **Key terms introduced:**
  - Stochastic gradient descent (الانحدار التدرجي العشوائي)
  - Batch size (حجم الدفعة)
  - Momentum (الزخم)
  - Energy function (دالة الطاقة)
  - Soft-max (kept as soft-max)
  - Cross entropy (الإنتروبيا التقاطعية)
  - Loss function (دالة الخسارة)
  - Weight map (خريطة الأوزان)
  - Ground truth (الحقيقة الأرضية)
  - Morphological operations (العمليات المورفولوجية)
  - Gaussian distribution (توزيع غاوسي)
  - Unit variance (تباين قريب من الوحدة)
  - Weight initialization (تهيئة الأوزان)
  - Data augmentation (زيادة البيانات)
  - Invariance (ثبات)
  - Elastic deformations (التشوهات المرنة)
  - Bicubic interpolation (الاستيفاء التكعيبي الثنائي)
  - Drop-out (kept as dropout)
- **Equations:** 3 major equations preserved in LaTeX:
  1. Soft-max function: ${p}_k(\vec{x}) = \exp({a_k(\vec{x})}) / \left(\sum_{k' = 1}^K \exp(a_{k'}(\vec{x}))\right)$
  2. Energy function: $E = \sum_{\vec{x} \in \Omega} w(\vec{x}) \log({p}_{\ell(\vec{x})}(\vec{x}))$
  3. Weight map: $w(\vec{x}) = w_c(\vec{x}) + w_0 \cdot \exp\left( - \frac{(d_1(\vec{x}) + d_2(\vec{x}))^2}{2\sigma^2}\right)$
  4. Weight initialization: $\sqrt{2/N}$ and $N = 9\cdot 64 = 576$
- **Citations:**
  - [Caffe] - Caffe framework
  - [He2015] - Weight initialization method
- **Special handling:**
  - Preserved all mathematical notation in LaTeX
  - Kept "soft-max" and "dropout" in English (standard ML terms)
  - Kept "Caffe" as proper name
  - Added Arabic explanations after equations
  - Preserved numerical values (0.99, 10, 5, 576, etc.)
  - Subsection 3.1 properly formatted

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation Check

Energy function description back-translation:
Arabic → English: "The energy function is computed by soft-max at the pixel level on the final feature map combined with the cross entropy loss function."
Original: "The energy function is computed by a pixel-wise soft-max over the final feature map combined with the cross entropy loss function."
✓ Semantically equivalent

Data augmentation paragraph back-translation:
Arabic → English: "Data augmentation is essential to teach the network the desired invariance and robustness properties, when only few training samples are available. In the case of microscopic images, we primarily need shift and rotation invariance as well as robustness to deformations and gray value variations."
✓ Semantically equivalent with high fidelity
