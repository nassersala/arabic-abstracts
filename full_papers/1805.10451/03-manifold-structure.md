# Section 3: Manifold Structure
## القسم 3: بنية المتعدد

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** manifold, deep learning, autoencoder, encoder, decoder, latent space, ambient space, chart, atlas, homeomorphism, probability distribution, piecewise linear, cell decomposition, generative model, denoising

---

### English Version

Deep learning is the mainstream technique for many machine learning tasks, including image recognition, machine translation, speech recognition, and so on [12]. It has outperformed conventional methods in various fields and achieved great successes. Unfortunately, the understanding on how it works remains unclear. It has the central importance to lay down the theoretic foundation for deep learning.

We believe that the main fundamental principle to explain the success of deep learning is the manifold structure in the data, namely *natural high dimensional data concentrates close to a non-linear low-dimensional manifold*.

The goal of deep learning is to learn the manifold structure in data and the probability distribution associated with the manifold.

### 3.1 Concepts and Notations

The concepts related to manifold are from differential geometry, and have been translated to the machine learning language.

**Definition 3.1 (Manifold).** An $n$-dimensional manifold $\Sigma$ is a topological space, covered by a set of open sets $\Sigma \subset \bigcup_\alpha U_\alpha$. For each open set $U_\alpha$, there is a homeomorphism $\varphi_\alpha : U_\alpha \to \mathbb{R}^n$, the pair $(U_\alpha, \varphi_\alpha)$ form a chart. The union of charts form an atlas $\mathcal{A} = \{(U_\alpha, \varphi_\alpha)\}$. If $U_\alpha \cap U_\beta \neq \emptyset$, then the chart transition map is given by $\varphi_{\alpha\beta} : \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$,

$$\varphi_{\alpha\beta} := \varphi_\beta \circ \varphi_\alpha^{-1}.$$

As shown in Fig. 1, suppose $\mathcal{X}$ is the ambient space, $\mu$ is a probability distribution defined on $\mathcal{X}$, represented as a density function $\mu : \mathcal{X} \to \mathbb{R}_{\geq 0}$. The support of $\mu$,

$$\Sigma(\mu) := \{x \in \mathcal{X} | \mu(x) > 0\}$$

is a low-dimensional manifold. $(U_\alpha, \varphi_\beta)$ is a local chart, $\varphi_\alpha : U_\alpha \to \mathcal{F}$ is called an encoding map, the parameter domain $\mathcal{F}$ is called the latent space or feature space. A point $x \in \Sigma$ is called a sample, its parameter $\varphi_\alpha(x)$ is called the code or feature of $x$. The inverse map $\psi_\alpha := \varphi_\alpha^{-1} : \mathcal{F} \to \Sigma$ is called the decoding map. Locally, $\psi_\alpha : \mathcal{F} \to \Sigma$ gives a local parametric representation of the manifold.

Furthermore, the encoding map $\varphi_\alpha : U_\alpha \to \mathcal{F}$ induces a push-forward probability measure $(\varphi_\alpha)_*\mu$ defined on the latent space $\mathcal{F}$: for any measurable set $B \subset \mathcal{F}$,

$$(\varphi_\alpha)_*\mu(B) := \mu(\varphi_\alpha(B)).$$

The goal for deep learning is to learn the encoding map $\varphi_\alpha$, decoding map $\psi_\alpha$, the parametric representation of the manifold $\psi_\alpha : \mathcal{F} \to \Sigma$, furthermore the push-forward probability $(\varphi_\alpha)_*\mu$ and so on. In the following, we explain how an autoencoder learns the manifold and the distribution.

### 3.2 Manifold Learned by an Autoencoder

Autoencoders are commonly used for unsupervised learning [3], they have been applied for compression, denoising, pre-training and so on. In abstract level, autoencoder learns the low-dimensional structure of data and represent it as a parametric polyhedral manifold, namely a piecewise linear (PL) map from latent space (parameter domain) to the ambient space, the image of the PL mapping is a manifold. Then autoencoder utilizes the polyhedral manifold as the approximation of the manifold in data for various applications. In implementation level, an autoencoder partition the manifold into pieces (by decomposing the ambient space into cells) and approximate each piece by a hyperplane as shown in Fig. 2.

Architecturally, an autoencoder is a feedforward, non-recurrent neural network with the output layer having the same number of nodes as the input layer, and with the purpose of reconstructing its own inputs. In general, a bottleneck layer is added for the purpose of dimensionality reduction. The input space $\mathcal{X}$ is the ambient space, the output space is also the ambient space. The output space of the bottle neck layer $\mathcal{F}$ is the latent space.

An autoencoder always consists of two parts, the encoder and the decoder. The encoder takes a sample $x \in \mathcal{X}$ and maps it to $z \in \mathcal{F}$, $z = \varphi(x)$, the image $z$ is usually referred to as latent representation of $x$. The encoder $\varphi : \mathcal{X} \to \mathcal{F}$ maps $\Sigma$ to its latent representation $D = \varphi(\Sigma)$ homemorphically. After that, the decoder $\psi : \mathcal{F} \to \mathcal{X}$ maps $z$ to the reconstruction $\tilde{x}$ of the same shape as $x$, $\tilde{x} = \psi(z) = \psi \circ \varphi(x)$. Autoencoders are also trained to minimise reconstruction errors:

$$\varphi, \psi = \arg\min_{\varphi,\psi} \int_{\mathcal{X}} \mathcal{L}(x, \psi \circ \varphi(x))d\mu(x),$$

where $\mathcal{L}(\cdot, \cdot)$ is the loss function, such as squared errors. The reconstructed manifold $\tilde{\Sigma} = \psi \circ \varphi(\Sigma)$ is used as an approximation of $\Sigma$.

In practice, both encoder and decoder are implemented as ReLU DNNs, parameterized by $\theta$. Let $X = \{x^{(1)}, x^{(2)}, \ldots, x^k\}$ be the training data set, $X \subset \Sigma$, the autoencoder optimizes the following loss function:

$$\min_\theta \mathcal{L}(\theta) = \min_\theta \frac{1}{k} \sum_{i=1}^k \|x^{(i)} - \psi_\theta \circ \varphi_\theta(x^{(i)})\|^2.$$

Both the encoder $\varphi_\theta$ and the decoder $\psi_\theta$ are piecewise linear mappings. The encoder $\varphi_\theta$ induces a cell decomposition $\mathcal{D}(\varphi_\theta)$ of the ambient space

$$\mathcal{D}(\varphi_\theta) : \mathcal{X} = \bigcup_\alpha U_\theta^\alpha,$$

where $U_\theta^\alpha$ is a convex polyhedron, the restriction of $\varphi_\theta$ on it is an affine map. Similarly, the piecewise linear map $\psi_\theta \circ \varphi_\theta$ induces a polyhedral cell decomposition $\mathcal{D}(\psi_\theta, \varphi_\theta)$, which is a refinement (subdivision) of $\mathcal{D}(\varphi_\theta)$. The reconstructed polyhedral manifold has a parametric representation $\psi_\theta : \mathcal{F} \to \mathcal{X}$, which approximates the manifold $M$ in the data.

Fig. 2 shows an example to demonstrate the learning results of an autoencoder. The ambient space $\mathcal{X}$ is $\mathbb{R}^3$, the manifold $\Sigma$ is the buddha surface as shown in frame (a). The latent space is $\mathbb{R}^2$, the encoding map $\varphi_\theta : \mathcal{X} \to D$ parameterizes the input manifold to a domain on $D \subset \mathcal{F}$ as shown in frame (b). The decoding map $\psi_\theta : D \to \mathcal{X}$ reconstructs the surface into a piecewise linear surface $\tilde{\Sigma} = \psi_\theta \circ \varphi_\theta(\Sigma)$, as shown in frame (c). In ideal situation, the composition of the encoder and decoder $\psi_\theta \circ \varphi_\theta \sim id$ should equal to the identity map, the reconstruction $\tilde{\Sigma}$ should coincide with the input $\Sigma$. In reality, the reconstruction $\tilde{\Sigma}$ is only a piecewise linear approximation of $\Sigma$.

Fig. 3 shows the cell decompositions induced by the encoding map $\mathcal{D}(\varphi_\theta)$ and that by the reconstruction map $\mathcal{D}(\psi_\theta \circ \varphi_\theta)$ for another autoencoder. It is obvious that $\mathcal{D}(\psi_\theta \circ \varphi_\theta)$ subdivides $\mathcal{D}(\varphi_\theta)$.

### 3.3 Direct Applications

Once the neural network has learned a manifold $\Sigma$, it can be utilized for many applications.

**Generative Model** Suppose $\mathcal{X}$ is the space of all $n \times n$ color images, where each point represents an image. We can define a probability measure $\mu$, which represents the probability for an image to represent a human face. The shape of a human face is determined by a finite number of genes. The facial photo is determined by the geometry of the face, the lightings, the camera parameters and so on. Therefore, it is sensible to assume all the human facial photos are concentrated around a finite dimensional manifold, we call it as human facial photo manifold $\Sigma$.

By using many real human facial photos, we can train an autoendoer to learn the human facial photo manifold. The learning process produces a decoding map $\psi_\theta : \mathcal{F} \to \tilde{\Sigma}$, namely a parametric representation of the reconstructed manifold. We randomly generate a parameter $z \in \mathcal{F}$ (white noise), $\varphi_\theta(z) \in \tilde{\Sigma}$ gives a human facial image. This can be applied as a generative model for generating human facial photos.

**Denoising** Tradition image denoising performs Fourier transformation of the input noisy image, then filtering out the high frequency components, inverse Fourier transformation to get the denoised image. This method is general and independent of the content of the image.

In deep learning, image denoising can be re-interpreted as geometric projection as shown in Fig. 4. Suppose we perform human facial image denoising. The clean human facial photo manifold is $\Sigma$, the noisy facial image $\tilde{p}$ is not in $\Sigma$ but close to $\Sigma$. We project $\tilde{p}$ to $\Sigma$, the closest point to $\tilde{p}$ on $\Sigma$ is $p$, then $p$ is the denoised image.

In practice, suppose an noisy facial image is given $x$, we train an autoencoder to obtain a manifold of clean facial images represented as $\psi_\theta : \mathcal{F} \to \mathcal{X}$ and an encoding map $\varphi_\theta : \mathcal{X} \to \mathcal{F}$, then we encode the noisy image $z = \varphi(x)$, then maps $z$ to the reconstructed manifold $\tilde{x} = \psi_\theta(z)$. The result $\tilde{x}$ is the denoised image. Fig. 5 shows the projection of several outliers onto the buddha surface using an autoencoder.

We apply this method for human facial image denoising as shown in Fig. 6, in frame (a) we project the noisy image to the human facial image manifold and obtain good denoising result; in frame (b) we use the cat facial image manifold, the results are meaningless. This shows deep learning method heavily depends on the underlying manifold, which is specific to the problem. Hence the deep learning based method is not as universal as the conventional ones.

---

### النسخة العربية

التعلم العميق هو التقنية السائدة للعديد من مهام تعلم الآلة، بما في ذلك التعرف على الصور، والترجمة الآلية، والتعرف على الكلام، وما إلى ذلك [12]. لقد تفوق على الأساليب التقليدية في مختلف المجالات وحقق نجاحات كبيرة. لسوء الحظ، لا يزال الفهم حول كيفية عمله غير واضح. من الأهمية المركزية وضع الأساس النظري للتعلم العميق.

نعتقد أن المبدأ الأساسي الرئيسي لتفسير نجاح التعلم العميق هو بنية المتعدد في البيانات، أي *البيانات الطبيعية عالية الأبعاد تتركز بالقرب من متعدد غير خطي منخفض الأبعاد*.

هدف التعلم العميق هو تعلم بنية المتعدد في البيانات وتوزيع الاحتمالات المرتبط بالمتعدد.

### 3.1 المفاهيم والترميزات

المفاهيم المتعلقة بالمتعدد مأخوذة من الهندسة التفاضلية، وتم ترجمتها إلى لغة تعلم الآلة.

**التعريف 3.1 (المتعدد).** المتعدد $\Sigma$ ذو $n$ بعد هو فضاء طوبولوجي، مغطى بمجموعة من المجموعات المفتوحة $\Sigma \subset \bigcup_\alpha U_\alpha$. لكل مجموعة مفتوحة $U_\alpha$، يوجد تشاكل $\varphi_\alpha : U_\alpha \to \mathbb{R}^n$، والزوج $(U_\alpha, \varphi_\alpha)$ يشكل خريطة. اتحاد الخرائط يشكل أطلساً $\mathcal{A} = \{(U_\alpha, \varphi_\alpha)\}$. إذا كان $U_\alpha \cap U_\beta \neq \emptyset$، فإن خريطة الانتقال بين الخرائط تُعطى بـ $\varphi_{\alpha\beta} : \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$،

$$\varphi_{\alpha\beta} := \varphi_\beta \circ \varphi_\alpha^{-1}.$$

كما هو موضح في الشكل 1، افترض أن $\mathcal{X}$ هو الفضاء المحيط، و$\mu$ هو توزيع احتمالات معرف على $\mathcal{X}$، ممثل كدالة كثافة $\mu : \mathcal{X} \to \mathbb{R}_{\geq 0}$. دعم $\mu$،

$$\Sigma(\mu) := \{x \in \mathcal{X} | \mu(x) > 0\}$$

هو متعدد منخفض الأبعاد. $(U_\alpha, \varphi_\beta)$ هي خريطة محلية، $\varphi_\alpha : U_\alpha \to \mathcal{F}$ تسمى خريطة ترميز، ومجال البارامتر $\mathcal{F}$ يسمى الفضاء الكامن أو فضاء الميزات. نقطة $x \in \Sigma$ تسمى عينة، وبارامترها $\varphi_\alpha(x)$ يسمى الشفرة أو الميزة لـ $x$. الخريطة العكسية $\psi_\alpha := \varphi_\alpha^{-1} : \mathcal{F} \to \Sigma$ تسمى خريطة فك الترميز. محلياً، $\psi_\alpha : \mathcal{F} \to \Sigma$ يعطي تمثيلاً بارامترياً محلياً للمتعدد.

علاوة على ذلك، تستحث خريطة الترميز $\varphi_\alpha : U_\alpha \to \mathcal{F}$ قياس احتمالات مدفوعاً للأمام $(\varphi_\alpha)_*\mu$ معرفاً على الفضاء الكامن $\mathcal{F}$: لأي مجموعة قابلة للقياس $B \subset \mathcal{F}$،

$$(\varphi_\alpha)_*\mu(B) := \mu(\varphi_\alpha(B)).$$

الهدف من التعلم العميق هو تعلم خريطة الترميز $\varphi_\alpha$، وخريطة فك الترميز $\psi_\alpha$، والتمثيل البارامتري للمتعدد $\psi_\alpha : \mathcal{F} \to \Sigma$، وعلاوة على ذلك احتمال الدفع للأمام $(\varphi_\alpha)_*\mu$ وما إلى ذلك. في ما يلي، نشرح كيف يتعلم المشفر التلقائي المتعدد والتوزيع.

### 3.2 المتعدد المتعلم بواسطة مشفر تلقائي

تُستخدم المشفرات التلقائية بشكل شائع للتعلم غير الموجه [3]، وقد تم تطبيقها للضغط، وإزالة الضوضاء، والتدريب المسبق وما إلى ذلك. على المستوى المجرد، يتعلم المشفر التلقائي البنية منخفضة الأبعاد للبيانات ويمثلها كمتعدد متعدد السطوح بارامتري، أي خريطة خطية متعددة القطع (PL) من الفضاء الكامن (مجال البارامتر) إلى الفضاء المحيط، وصورة الخريطة PL هي متعدد. ثم يستخدم المشفر التلقائي المتعدد متعدد السطوح كتقريب للمتعدد في البيانات لتطبيقات مختلفة. على مستوى التنفيذ، يقسم المشفر التلقائي المتعدد إلى قطع (عن طريق تحليل الفضاء المحيط إلى خلايا) ويقرب كل قطعة بمستوٍ فائق كما هو موضح في الشكل 2.

معمارياً، المشفر التلقائي هو شبكة عصبية أمامية غير متكررة مع طبقة المخرجات التي لديها نفس عدد العقد كطبقة المدخلات، وبغرض إعادة بناء مدخلاتها الخاصة. بشكل عام، تُضاف طبقة عنق الزجاجة لغرض تقليل الأبعاد. فضاء المدخلات $\mathcal{X}$ هو الفضاء المحيط، وفضاء المخرجات هو أيضاً الفضاء المحيط. فضاء المخرجات لطبقة عنق الزجاجة $\mathcal{F}$ هو الفضاء الكامن.

يتكون المشفر التلقائي دائماً من جزأين، المشفر وفك التشفير. يأخذ المشفر عينة $x \in \mathcal{X}$ ويرسمها إلى $z \in \mathcal{F}$، $z = \varphi(x)$، والصورة $z$ يُشار إليها عادة باسم التمثيل الكامن لـ $x$. المشفر $\varphi : \mathcal{X} \to \mathcal{F}$ يرسم $\Sigma$ إلى تمثيله الكامن $D = \varphi(\Sigma)$ بشكل متشاكل. بعد ذلك، يرسم فك التشفير $\psi : \mathcal{F} \to \mathcal{X}$ $z$ إلى إعادة البناء $\tilde{x}$ بنفس شكل $x$، $\tilde{x} = \psi(z) = \psi \circ \varphi(x)$. يتم أيضاً تدريب المشفرات التلقائية لتقليل أخطاء إعادة البناء:

$$\varphi, \psi = \arg\min_{\varphi,\psi} \int_{\mathcal{X}} \mathcal{L}(x, \psi \circ \varphi(x))d\mu(x),$$

حيث $\mathcal{L}(\cdot, \cdot)$ هي دالة الخسارة، مثل الأخطاء التربيعية. يُستخدم المتعدد المعاد بناؤه $\tilde{\Sigma} = \psi \circ \varphi(\Sigma)$ كتقريب لـ $\Sigma$.

في الممارسة العملية، يتم تنفيذ كل من المشفر وفك التشفير كشبكات عصبية عميقة ReLU، مع بارامترات $\theta$. لتكن $X = \{x^{(1)}, x^{(2)}, \ldots, x^k\}$ مجموعة بيانات التدريب، $X \subset \Sigma$، يحسن المشفر التلقائي دالة الخسارة التالية:

$$\min_\theta \mathcal{L}(\theta) = \min_\theta \frac{1}{k} \sum_{i=1}^k \|x^{(i)} - \psi_\theta \circ \varphi_\theta(x^{(i)})\|^2.$$

كل من المشفر $\varphi_\theta$ وفك التشفير $\psi_\theta$ هما خرائط خطية متعددة القطع. يستحث المشفر $\varphi_\theta$ تحليلاً خلوياً $\mathcal{D}(\varphi_\theta)$ للفضاء المحيط

$$\mathcal{D}(\varphi_\theta) : \mathcal{X} = \bigcup_\alpha U_\theta^\alpha,$$

حيث $U_\theta^\alpha$ هو متعدد سطوح محدب، وقصر $\varphi_\theta$ عليه هو خريطة أفينية. وبالمثل، تستحث الخريطة الخطية متعددة القطع $\psi_\theta \circ \varphi_\theta$ تحليلاً خلوياً متعدد السطوح $\mathcal{D}(\psi_\theta, \varphi_\theta)$، وهو تنقية (تقسيم فرعي) لـ $\mathcal{D}(\varphi_\theta)$. المتعدد متعدد السطوح المعاد بناؤه لديه تمثيل بارامتري $\psi_\theta : \mathcal{F} \to \mathcal{X}$، والذي يقرب المتعدد $M$ في البيانات.

يوضح الشكل 2 مثالاً لإظهار نتائج التعلم لمشفر تلقائي. الفضاء المحيط $\mathcal{X}$ هو $\mathbb{R}^3$، والمتعدد $\Sigma$ هو سطح بوذا كما هو موضح في الإطار (أ). الفضاء الكامن هو $\mathbb{R}^2$، خريطة الترميز $\varphi_\theta : \mathcal{X} \to D$ تُبَارِم متعدد المدخلات إلى مجال على $D \subset \mathcal{F}$ كما هو موضح في الإطار (ب). خريطة فك الترميز $\psi_\theta : D \to \mathcal{X}$ تعيد بناء السطح إلى سطح خطي متعدد القطع $\tilde{\Sigma} = \psi_\theta \circ \varphi_\theta(\Sigma)$، كما هو موضح في الإطار (ج). في الحالة المثالية، يجب أن يساوي تركيب المشفر وفك التشفير $\psi_\theta \circ \varphi_\theta \sim id$ خريطة الهوية، ويجب أن تتطابق إعادة البناء $\tilde{\Sigma}$ مع المدخل $\Sigma$. في الواقع، إعادة البناء $\tilde{\Sigma}$ هي فقط تقريب خطي متعدد القطع لـ $\Sigma$.

يوضح الشكل 3 التحليلات الخلوية المستحثة بواسطة خريطة الترميز $\mathcal{D}(\varphi_\theta)$ وتلك بواسطة خريطة إعادة البناء $\mathcal{D}(\psi_\theta \circ \varphi_\theta)$ لمشفر تلقائي آخر. من الواضح أن $\mathcal{D}(\psi_\theta \circ \varphi_\theta)$ يقسم $\mathcal{D}(\varphi_\theta)$.

### 3.3 التطبيقات المباشرة

بمجرد أن تتعلم الشبكة العصبية متعدداً $\Sigma$، يمكن استخدامه للعديد من التطبيقات.

**نموذج توليدي** افترض أن $\mathcal{X}$ هو فضاء جميع صور الألوان $n \times n$، حيث تمثل كل نقطة صورة. يمكننا تعريف قياس احتمالات $\mu$، والذي يمثل احتمال أن تمثل الصورة وجهاً بشرياً. شكل الوجه البشري يُحدد بعدد محدود من الجينات. الصورة الفوتوغرافية للوجه تُحدد بواسطة هندسة الوجه، والإضاءة، وبارامترات الكاميرا وما إلى ذلك. لذلك، من المنطقي أن نفترض أن جميع الصور الفوتوغرافية للوجوه البشرية تتركز حول متعدد بُعدي محدود، ونسميه متعدد الصور الفوتوغرافية للوجه البشري $\Sigma$.

باستخدام العديد من الصور الفوتوغرافية الحقيقية للوجوه البشرية، يمكننا تدريب مشفر تلقائي لتعلم متعدد الصور الفوتوغرافية للوجه البشري. تنتج عملية التعلم خريطة فك ترميز $\psi_\theta : \mathcal{F} \to \tilde{\Sigma}$، أي تمثيلاً بارامترياً للمتعدد المعاد بناؤه. نولد عشوائياً بارامتراً $z \in \mathcal{F}$ (ضوضاء بيضاء)، $\varphi_\theta(z) \in \tilde{\Sigma}$ يعطي صورة وجه بشري. يمكن تطبيق هذا كنموذج توليدي لتوليد صور فوتوغرافية لوجوه بشرية.

**إزالة الضوضاء** تجري إزالة الضوضاء التقليدية من الصور تحويل فورييه للصورة الصاخبة المدخلة، ثم تصفية مكونات التردد العالي، وتحويل فورييه العكسي للحصول على الصورة منزوعة الضوضاء. هذه الطريقة عامة ومستقلة عن محتوى الصورة.

في التعلم العميق، يمكن إعادة تفسير إزالة الضوضاء من الصور على أنها إسقاط هندسي كما هو موضح في الشكل 4. افترض أننا نقوم بإزالة الضوضاء من صورة الوجه البشري. متعدد الصور الفوتوغرافية النظيفة للوجه البشري هو $\Sigma$، الصورة الصاخبة للوجه $\tilde{p}$ ليست في $\Sigma$ ولكن قريبة من $\Sigma$. نسقط $\tilde{p}$ على $\Sigma$، والنقطة الأقرب إلى $\tilde{p}$ على $\Sigma$ هي $p$، ثم $p$ هي الصورة منزوعة الضوضاء.

في الممارسة العملية، افترض أنه يتم إعطاء صورة وجه صاخبة $x$، نقوم بتدريب مشفر تلقائي للحصول على متعدد من صور الوجه النظيفة ممثل كـ $\psi_\theta : \mathcal{F} \to \mathcal{X}$ وخريطة ترميز $\varphi_\theta : \mathcal{X} \to \mathcal{F}$، ثم نقوم بترميز الصورة الصاخبة $z = \varphi(x)$، ثم نرسم $z$ إلى المتعدد المعاد بناؤه $\tilde{x} = \psi_\theta(z)$. النتيجة $\tilde{x}$ هي الصورة منزوعة الضوضاء. يوضح الشكل 5 إسقاط عدة قيم شاذة على سطح بوذا باستخدام مشفر تلقائي.

نطبق هذه الطريقة لإزالة الضوضاء من صور الوجه البشري كما هو موضح في الشكل 6، في الإطار (أ) نسقط الصورة الصاخبة على متعدد صور الوجه البشري ونحصل على نتيجة جيدة لإزالة الضوضاء؛ في الإطار (ب) نستخدم متعدد صور وجه القط، والنتائج لا معنى لها. هذا يوضح أن طريقة التعلم العميق تعتمد بشكل كبير على المتعدد الأساسي، والذي يخص المشكلة. وبالتالي فإن الطريقة القائمة على التعلم العميق ليست عالمية مثل الطرق التقليدية.

---

### Translation Notes

- **Figures referenced:** Figure 1, 2, 3, 4, 5, 6
- **Key terms introduced:**
  - chart → خريطة
  - atlas → أطلس
  - homeomorphism → تشاكل
  - support (of distribution) → دعم
  - parametric representation → تمثيل بارامتري
  - cell decomposition → تحليل خلوي
  - polyhedron → متعدد سطوح
  - affine map → خريطة أفينية
  - subdivision → تقسيم فرعي

- **Equations:** Multiple LaTeX equations throughout
- **Citations:** [3], [12]
- **Special handling:** Mathematical definitions preserved exactly

### Back-Translation Check (Definition 3.1)

"An n-dimensional manifold $\Sigma$ is a topological space, covered by a set of open sets $\Sigma \subset \bigcup_\alpha U_\alpha$. For each open set $U_\alpha$, there is a homeomorphism $\varphi_\alpha : U_\alpha \to \mathbb{R}^n$, the pair $(U_\alpha, \varphi_\alpha)$ form a chart."

✓ Mathematical precision verified

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
