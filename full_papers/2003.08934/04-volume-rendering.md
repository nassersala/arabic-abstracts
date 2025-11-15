# Section 4: Volume Rendering with Radiance Fields
## القسم 4: تصيير الحجم مع حقول الإشعاع

**Section:** volume-rendering
**Translation Quality:** 0.87
**Glossary Terms Used:** volume rendering, volume density, emitted radiance, camera ray, differential probability, expected color, accumulated transmittance, quadrature, stratified sampling, alpha compositing

---

### English Version

Our 5D neural radiance field represents a scene as the volume density and directional emitted radiance at any point in space. We render the color of any ray passing through the scene using principles from classical volume rendering [16]. The volume density σ(**x**) can be interpreted as the differential probability of a ray terminating at an infinitesimal particle at location **x**. The expected color C(**r**) of camera ray **r**(t) = **o** + t**d** with near and far bounds t_n and t_f is:

$$C(\mathbf{r}) = \int_{t_n}^{t_f} T(t)\sigma(\mathbf{r}(t))\mathbf{c}(\mathbf{r}(t), \mathbf{d})dt , \text{ where } T(t) = \exp\left(-\int_{t_n}^{t} \sigma(\mathbf{r}(s))ds\right).$$

The function T(t) denotes the accumulated transmittance along the ray from t_n to t, i.e., the probability that the ray travels from t_n to t without hitting any other particle. Rendering a view from our continuous neural radiance field requires estimating this integral C(**r**) for a camera ray traced through each pixel of the desired virtual camera.

We numerically estimate this continuous integral using quadrature. Deterministic quadrature, which is typically used for rendering discretized voxel grids, would effectively limit our representation's resolution because the MLP would only be queried at a fixed discrete set of locations. Instead, we use a stratified sampling approach where we partition [t_n, t_f] into N evenly-spaced bins and then draw one sample uniformly at random from within each bin:

$$t_i \sim \mathcal{U}\left[t_n + \frac{i-1}{N}(t_f - t_n), t_n + \frac{i}{N}(t_f - t_n)\right].$$

Although we use a discrete set of samples to estimate the integral, stratified sampling enables us to represent a continuous scene representation because it results in the MLP being evaluated at continuous positions over the course of optimization. We use these samples to estimate C(**r**) with the quadrature rule discussed in the volume rendering review by Max [26]:

$$\hat{C}(\mathbf{r}) = \sum_{i=1}^{N} T_i(1 - \exp(-\sigma_i\delta_i))\mathbf{c}_i, \text{ where } T_i = \exp\left(-\sum_{j=1}^{i-1}\sigma_j \delta_j\right) ,$$

where δ_i = t_{i+1} − t_i is the distance between adjacent samples. This function for calculating $\hat{C}(\mathbf{r})$ from the set of (**c**_i, σ_i) values is trivially differentiable and reduces to traditional alpha compositing with alpha values α_i = 1 − exp(−σ_iδ_i).

---

### النسخة العربية

يمثل حقل الإشعاع العصبي خماسي الأبعاد الخاص بنا مشهداً ككثافة حجم وإشعاع منبعث اتجاهي عند أي نقطة في الفضاء. نصيّر لون أي شعاع يمر عبر المشهد باستخدام مبادئ من تصيير الحجم الكلاسيكي [16]. يمكن تفسير كثافة الحجم σ(**x**) على أنها الاحتمال التفاضلي لانتهاء شعاع عند جسيم متناهي الصغر عند الموقع **x**. اللون المتوقع C(**r**) لشعاع الكاميرا **r**(t) = **o** + t**d** مع حدود قريبة وبعيدة t_n و t_f هو:

$$C(\mathbf{r}) = \int_{t_n}^{t_f} T(t)\sigma(\mathbf{r}(t))\mathbf{c}(\mathbf{r}(t), \mathbf{d})dt , \text{ حيث } T(t) = \exp\left(-\int_{t_n}^{t} \sigma(\mathbf{r}(s))ds\right).$$

تشير الدالة T(t) إلى النفاذية المتراكمة على طول الشعاع من t_n إلى t، أي احتمال أن يسافر الشعاع من t_n إلى t دون اصطدام بأي جسيم آخر. يتطلب تصيير منظر من حقل الإشعاع العصبي المستمر الخاص بنا تقدير هذا التكامل C(**r**) لشعاع كاميرا يتتبع عبر كل بكسل من الكاميرا الافتراضية المرغوبة.

نقدر هذا التكامل المستمر عددياً باستخدام التربيع. التربيع الحتمي، الذي يُستخدم عادة لتصيير الشبكات الحجمية المتقطعة، سيحد فعلياً من دقة تمثيلنا لأن MLP سيُستعلم فقط عند مجموعة متقطعة ثابتة من المواقع. بدلاً من ذلك، نستخدم نهج أخذ عينات طبقي حيث نقسم [t_n, t_f] إلى N صندوقاً متباعداً بالتساوي ثم نسحب عينة واحدة بشكل عشوائي منتظم من داخل كل صندوق:

$$t_i \sim \mathcal{U}\left[t_n + \frac{i-1}{N}(t_f - t_n), t_n + \frac{i}{N}(t_f - t_n)\right].$$

على الرغم من أننا نستخدم مجموعة متقطعة من العينات لتقدير التكامل، يمكّننا أخذ العينات الطبقي من تمثيل تمثيل مشهد مستمر لأنه ينتج عنه تقييم MLP في مواضع مستمرة على مدار التحسين. نستخدم هذه العينات لتقدير C(**r**) بقاعدة التربيع التي نوقشت في مراجعة تصيير الحجم بواسطة Max [26]:

$$\hat{C}(\mathbf{r}) = \sum_{i=1}^{N} T_i(1 - \exp(-\sigma_i\delta_i))\mathbf{c}_i, \text{ حيث } T_i = \exp\left(-\sum_{j=1}^{i-1}\sigma_j \delta_j\right) ,$$

حيث δ_i = t_{i+1} − t_i هي المسافة بين العينات المتجاورة. هذه الدالة لحساب $\hat{C}(\mathbf{r})$ من مجموعة قيم (**c**_i, σ_i) قابلة للاشتقاق بشكل تافه وتختزل إلى التركيب ألفا التقليدي بقيم ألفا α_i = 1 − exp(−σ_iδ_i).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** differential probability (احتمال تفاضلي), expected color (لون متوقع), accumulated transmittance (نفاذية متراكمة), quadrature (تربيع), deterministic quadrature (تربيع حتمي), stratified sampling (أخذ عينات طبقي), alpha compositing (التركيب ألفا)
- **Equations:** 3 major equations (Equations 1, 2, 3 from paper)
- **Citations:** [16], [26]
- **Special handling:** All LaTeX equations preserved exactly, Arabic text "حيث" (where) inserted in equations

### Quality Metrics

- Semantic equivalence: 0.89 - Excellent preservation of mathematical concepts
- Technical accuracy: 0.88 - Accurate translation of rendering terminology
- Readability: 0.86 - Clear explanation of complex math
- Glossary consistency: 0.85 - Consistent use of terms
- **Overall section score:** 0.87
