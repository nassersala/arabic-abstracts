# Section 5: Control Induced Measure
## القسم 5: التحكم في القياس المستحث

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** optimal mass transportation, Wasserstein distance, latent space, encoder, VAE, GAN, WGAN, discriminator, generator, Monge-Ampere equation, Brenier potential, Kantorovich potential

---

### English Version

In generative models, such as VAE [15] or GAN [1], the probability measure in the latent space induced by the encoding mapping $(\varphi_\theta)_*\mu$ is controlled to be simple distributions, such as Gaussian or uniform, then in the generating process, we can sample from the simple distribution in the latent space, and use the decoding map to produce a sample in the ambient space.

The buddha surface $\Sigma$ is conformally mapped onto the planar unit disk $\varphi : \Sigma \to \mathbb{D}$ using the Ricci flow method [32], the uniform distribution on the parameter domain induces a non-uniform distribution on the surface, as shown in the top row of Fig. 9. Then by composing with an optimal mass transportation map $\psi : \mathbb{D} \to \mathbb{D}$ using the algorithm in [25], one obtain an area-preserving mapping $\psi \circ \varphi : \Sigma \to \mathbb{D}$, the image is shown in the bottom row of Fig. 9 left frame. Then we uniformly sample the planar disk to get the samples $Z = \{z_1, \ldots, z_k\}$, then pull them back on to $\Sigma$ by $\psi \circ \varphi$, $X = \{x_1, \ldots, x_k\}$, $x_i = (\psi \circ \varphi)^{-1}(z_i)$. Because $\psi \circ \varphi$ is area-preserving, $Z$ is uniformly distributed on the disk, $X$ is uniformly distributed on $\Sigma$ as shown in the bottom row of Fig. 9 right frame.

**Optimal Mass Transportation** The optimal transportation theory can be found in Villani's classical books [27][28]. Suppose $\nu = (\varphi_\theta)_*\mu$ is the induced probability in the latent space with a convex support $\Omega \subset \mathcal{F}$, $\zeta$ is the simple distribution, e.g. the uniform distribution on $\Omega$. A mapping $T : \Omega \to \Omega$ is measure-preserving if $T_*\nu = \zeta$. Given the transportation cost between two points $c : \Omega \times \Omega \to \mathbb{R}$, the transportation cost of $T$ is defined as

$$\mathcal{E}(T) := \int_\Omega c(x, T(x))d\nu(x).$$

The Wasserstein distance between $\nu$ and $\zeta$ is defined as

$$\mathcal{W}(\nu, \zeta) := \inf_{T_*\nu=\zeta} \mathcal{E}(T).$$

The measure-preserving map $T$ that minimizes the transportation cost is called the *optimal mass transportation map*.

Kantorovich proved that the Wasserstein distance can be represented as

$$\mathcal{W}(\nu, \zeta) := \max_f \int_\Omega f d\nu + \int_\Omega f^c d\zeta$$

where $f : \Omega \to \mathbb{R}$ is called the Kontarovhich potential, its c-transform

$$f^c(y) := \inf_{x \in \Omega} c(x, y) - f(x).$$

In WGAN, the discriminator computes the generator computes the decoding map $\psi_\theta : \mathcal{F} \to \mathcal{X}$, the discriminator computes the Wasserstein distance between $(\psi_\theta)_*\zeta$ and $\mu$. If the cost function is chosen to be the $L^1$ norm, $c(x, y) = |x - y|$, $f$ is 1-Lipsitz, then $f^c = -f$, the discriminator computes the Kontarovich potential, the generator computes the optimal mass transportation map, hence WGAN can be modeled as an optimization

$$\min_\theta \max_f \int_\Omega f \circ \psi_\theta(z)d\zeta(z) - \int_{\mathcal{X}} f(x)d\mu(x).$$

The competition between the discriminator and the generator leads to the solution.

If we choose the cost function to be the $L^2$ norm, $c(x, y) = \frac{1}{2}|x - y|^2$, then the computation can be greatly simplified. Briener's theorem [6] claims that there exists a convex function $u : \Omega \to \mathbb{R}$, the so-called Brenier's potential, such that its gradient map $\nabla u : \Omega \to \Omega$ gives the optimal mass transportation map. The Brenier's potential satisfies the Monge-Ampere equation

$$\det\left(\frac{\partial^2 u}{\partial x_i \partial x_j}\right) = \frac{\nu(x)}{\zeta(\nabla u(x))}.$$

Geometrically, the Monge-Ampere equation can be understood as solving Alexandroff problem: finding a convex surface with prescribed Gaussian curvature. A practical algorithm based on variational principle can be found in [13]. The Brenier's potential and the Kontarovich's potential are related by the closed form

$$u(x) = \frac{1}{2}|x|^2 - f(x).$$

Eqn.(5) shows that: the generator computes the optimal transportation map $\nabla u$, the discriminator computes the Wasserstein distance by finding Kontarovich's potential $f$; $u$ and $f$ can be converted to each other, hence the competition between the generator and the discriminator is unnecessary, the two deep neural networks for the generator and the discriminator are redundant.

**Autoencoder-OMT model** As shown in Fig. 10, we can use autoencoder to realize encoder $\varphi_\theta : \mathcal{X} \to \mathcal{F}$ and decoder $\psi_\theta : \mathcal{F} \to \mathcal{X}$, use OMT in the latent space to realize probability transformation $T : \mathcal{F} \to \mathcal{F}$, such that

$$T_*\zeta = (\varphi_\theta)_*\mu.$$

We call this model as OMT-autoencoder.

Fig. 5 shows the experiments on the MNIST data set. The digits generates by OMT-AE have better qualities than those generated by VAE and WGAN. Fig.(5) shows the human facial images on CelebA data set. The images generated by OMT-AE look better than those produced by VAE.

---

### النسخة العربية

في النماذج التوليدية، مثل VAE [15] أو GAN [1]، يتم التحكم في قياس الاحتمالات في الفضاء الكامن المستحث بواسطة خريطة الترميز $(\varphi_\theta)_*\mu$ ليكون توزيعات بسيطة، مثل التوزيع الغاوسي أو الموحد، ثم في عملية التوليد، يمكننا أخذ عينات من التوزيع البسيط في الفضاء الكامن، واستخدام خريطة فك الترميز لإنتاج عينة في الفضاء المحيط.

سطح بوذا $\Sigma$ مُرسَم بشكل مطابق على قرص الوحدة المستوي $\varphi : \Sigma \to \mathbb{D}$ باستخدام طريقة تدفق ريتشي [32]، التوزيع الموحد على مجال البارامتر يستحث توزيعاً غير موحد على السطح، كما هو موضح في الصف العلوي من الشكل 9. ثم بالتركيب مع خريطة نقل الكتلة الأمثل $\psi : \mathbb{D} \to \mathbb{D}$ باستخدام الخوارزمية في [25]، يحصل المرء على خريطة حافظة للمساحة $\psi \circ \varphi : \Sigma \to \mathbb{D}$، والصورة موضحة في الصف السفلي من الشكل 9 الإطار الأيسر. ثم نأخذ عينات موحدة من القرص المستوي للحصول على العينات $Z = \{z_1, \ldots, z_k\}$، ثم نسحبها مرة أخرى على $\Sigma$ بواسطة $\psi \circ \varphi$، $X = \{x_1, \ldots, x_k\}$، $x_i = (\psi \circ \varphi)^{-1}(z_i)$. لأن $\psi \circ \varphi$ حافظة للمساحة، $Z$ موزع بشكل موحد على القرص، $X$ موزع بشكل موحد على $\Sigma$ كما هو موضح في الصف السفلي من الشكل 9 الإطار الأيمن.

**النقل الأمثل للكتلة** يمكن العثور على نظرية النقل الأمثل في كتب فيلاني الكلاسيكية [27][28]. افترض أن $\nu = (\varphi_\theta)_*\mu$ هو الاحتمال المستحث في الفضاء الكامن مع دعم محدب $\Omega \subset \mathcal{F}$، $\zeta$ هو التوزيع البسيط، على سبيل المثال التوزيع الموحد على $\Omega$. الخريطة $T : \Omega \to \Omega$ حافظة للقياس إذا كانت $T_*\nu = \zeta$. لتكلفة النقل المعطاة بين نقطتين $c : \Omega \times \Omega \to \mathbb{R}$، تُعرّف تكلفة النقل لـ $T$ كـ

$$\mathcal{E}(T) := \int_\Omega c(x, T(x))d\nu(x).$$

تُعرّف مسافة فاسرشتاين بين $\nu$ و $\zeta$ كـ

$$\mathcal{W}(\nu, \zeta) := \inf_{T_*\nu=\zeta} \mathcal{E}(T).$$

الخريطة الحافظة للقياس $T$ التي تقلل تكلفة النقل تسمى *خريطة النقل الأمثل للكتلة*.

أثبت كانتوروفيتش أن مسافة فاسرشتاين يمكن تمثيلها كـ

$$\mathcal{W}(\nu, \zeta) := \max_f \int_\Omega f d\nu + \int_\Omega f^c d\zeta$$

حيث $f : \Omega \to \mathbb{R}$ تسمى جهد كانتوروفيتش، وتحويله c

$$f^c(y) := \inf_{x \in \Omega} c(x, y) - f(x).$$

في WGAN، يحسب المميز ويحسب المولد خريطة فك الترميز $\psi_\theta : \mathcal{F} \to \mathcal{X}$، يحسب المميز مسافة فاسرشتاين بين $(\psi_\theta)_*\zeta$ و $\mu$. إذا تم اختيار دالة التكلفة لتكون معيار $L^1$، $c(x, y) = |x - y|$، $f$ هو 1-ليبسيتز، ثم $f^c = -f$، يحسب المميز جهد كانتوروفيتش، يحسب المولد خريطة النقل الأمثل للكتلة، وبالتالي يمكن نمذجة WGAN كتحسين

$$\min_\theta \max_f \int_\Omega f \circ \psi_\theta(z)d\zeta(z) - \int_{\mathcal{X}} f(x)d\mu(x).$$

المنافسة بين المميز والمولد تؤدي إلى الحل.

إذا اخترنا دالة التكلفة لتكون معيار $L^2$، $c(x, y) = \frac{1}{2}|x - y|^2$، فيمكن تبسيط الحساب بشكل كبير. تدعي نظرية برينير [6] أنه توجد دالة محدبة $u : \Omega \to \mathbb{R}$، ما يسمى بجهد برينير، بحيث أن خريطة تدرجها $\nabla u : \Omega \to \Omega$ تعطي خريطة النقل الأمثل للكتلة. يلبي جهد برينير معادلة مونج-أمبير

$$\det\left(\frac{\partial^2 u}{\partial x_i \partial x_j}\right) = \frac{\nu(x)}{\zeta(\nabla u(x))}.$$

هندسياً، يمكن فهم معادلة مونج-أمبير على أنها حل مسألة ألكساندروف: إيجاد سطح محدب مع انحناء غاوسي محدد. يمكن العثور على خوارزمية عملية قائمة على المبدأ التباينيفي [13]. جهد برينير وجهد كانتوروفيتش مرتبطان بالصيغة المغلقة

$$u(x) = \frac{1}{2}|x|^2 - f(x).$$

تُظهر المعادلة (5) أن: المولد يحسب خريطة النقل الأمثل $\nabla u$، والمميز يحسب مسافة فاسرشتاين عن طريق إيجاد جهد كانتوروفيتش $f$؛ يمكن تحويل $u$ و $f$ إلى بعضهما البعض، وبالتالي فإن المنافسة بين المولد والمميز غير ضرورية، والشبكتان العصبيتان العميقتان للمولد والمميز زائدتان عن الحاجة.

**نموذج المشفر التلقائي-OMT** كما هو موضح في الشكل 10، يمكننا استخدام المشفر التلقائي لتحقيق المشفر $\varphi_\theta : \mathcal{X} \to \mathcal{F}$ وفك التشفير $\psi_\theta : \mathcal{F} \to \mathcal{X}$، واستخدام OMT في الفضاء الكامن لتحقيق تحويل الاحتمالات $T : \mathcal{F} \to \mathcal{F}$، بحيث

$$T_*\zeta = (\varphi_\theta)_*\mu.$$

نسمي هذا النموذج المشفر التلقائي-OMT.

يوضح الشكل 5 التجارب على مجموعة بيانات MNIST. الأرقام المولدة بواسطة OMT-AE لها جودات أفضل من تلك المولدة بواسطة VAE و WGAN. يوضح الشكل (5) صور الوجوه البشرية على مجموعة بيانات CelebA. الصور المولدة بواسطة OMT-AE تبدو أفضل من تلك المنتجة بواسطة VAE.

---

### Translation Notes

- **Figures referenced:** Figure 9, Figure 10, Figure 5
- **Key terms introduced:**
  - Ricci flow → تدفق ريتشي
  - area-preserving → حافظة للمساحة
  - measure-preserving → حافظة للقياس
  - Wasserstein distance → مسافة فاسرشتاين
  - Kantorovich potential → جهد كانتوروفيتش
  - Brenier potential → جهد برينير
  - Monge-Ampere equation → معادلة مونج-أمبير
  - Alexandroff problem → مسألة ألكساندروف
  - Gaussian curvature → انحناء غاوسي

- **Equations:** Multiple LaTeX equations throughout
- **Citations:** [1], [6], [13], [15], [25], [27], [28], [32]
- **Special handling:** Mathematical optimization formulations preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
