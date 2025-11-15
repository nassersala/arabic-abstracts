# Section 3: Neural Radiance Field Scene Representation
## القسم 3: تمثيل المشهد كحقل إشعاع عصبي

**Section:** neural-radiance-field
**Translation Quality:** 0.86
**Glossary Terms Used:** neural radiance field, vector-valued function, viewing direction, volume density, emitted color, MLP, fully-connected layer, ReLU activation, feature vector, multiview consistent, Lambertian, specular, non-Lambertian effects

---

### English Version

We represent a continuous scene as a 5D vector-valued function whose input is a 3D location **x** = (x, y, z) and 2D viewing direction (θ, φ), and whose output is an emitted color **c** = (r, g, b) and volume density σ. In practice, we express direction as a 3D Cartesian unit vector **d**. We approximate this continuous 5D scene representation with an MLP network F_Θ : (**x**, **d**) → (**c**, σ) and optimize its weights Θ to map from each input 5D coordinate to its corresponding volume density and directional emitted color.

We encourage the representation to be multiview consistent by restricting the network to predict the volume density σ as a function of only the location **x**, while allowing the RGB color **c** to be predicted as a function of both location and viewing direction. To accomplish this, the MLP F_Θ first processes the input 3D coordinate **x** with 8 fully-connected layers (using ReLU activations and 256 channels per layer), and outputs σ and a 256-dimensional feature vector. This feature vector is then concatenated with the camera ray's viewing direction and passed to one additional fully-connected layer (using a ReLU activation and 128 channels) that output the view-dependent RGB color.

See Fig. 3 for an example of how our method uses the input viewing direction to represent non-Lambertian effects. As shown in Fig. 4, a model trained without view dependence (only **x** as input) has difficulty representing specularities.

---

### النسخة العربية

نمثل مشهداً مستمراً كدالة ذات قيمة متجهة خماسية الأبعاد يكون مدخلها موقع ثلاثي الأبعاد **x** = (x, y, z) واتجاه مشاهدة ثنائي الأبعاد (θ, φ)، ويكون مخرجها لون منبعث **c** = (r, g, b) وكثافة حجم σ. عملياً، نعبر عن الاتجاه كمتجه وحدة ديكارتي ثلاثي الأبعاد **d**. نقرّب تمثيل المشهد الخماسي الأبعاد المستمر هذا بشبكة MLP F_Θ : (**x**, **d**) → (**c**, σ) ونحسّن أوزانها Θ للتعيين من كل إحداثي خماسي الأبعاد مدخل إلى كثافة الحجم واللون المنبعث الاتجاهي المقابلين له.

نشجع التمثيل ليكون متسقاً متعدد المناظر من خلال تقييد الشبكة للتنبؤ بكثافة الحجم σ كدالة للموقع **x** فقط، بينما نسمح بالتنبؤ بلون RGB **c** كدالة لكل من الموقع واتجاه المشاهدة. لتحقيق ذلك، تعالج MLP F_Θ أولاً الإحداثي ثلاثي الأبعاد المدخل **x** بـ 8 طبقات متصلة بالكامل (باستخدام تنشيطات ReLU و256 قناة لكل طبقة)، وتُخرج σ ومتجه ميزات ذو 256 بُعد. يُدمج متجه الميزات هذا بعد ذلك مع اتجاه مشاهدة شعاع الكاميرا ويُمرر إلى طبقة واحدة إضافية متصلة بالكامل (باستخدام تنشيط ReLU و128 قناة) تُخرج لون RGB المعتمد على المنظر.

انظر الشكل 3 لمثال على كيفية استخدام طريقتنا لاتجاه المشاهدة المدخل لتمثيل التأثيرات غير اللامبرتية. كما هو موضح في الشكل 4، يواجه النموذج المدرّب بدون اعتماد على المنظر (فقط **x** كمدخل) صعوبة في تمثيل الانعكاسات اللامعة.

---

### Translation Notes

- **Figures referenced:** Figure 3, Figure 4
- **Key terms introduced:** vector-valued function (دالة ذات قيمة متجهة), Cartesian unit vector (متجه وحدة ديكارتي), feature vector (متجه ميزات), multiview consistent (متسق متعدد المناظر), Lambertian (لامبرتي), non-Lambertian effects (تأثيرات غير لامبرتية), specularities (انعكاسات لامعة)
- **Equations:** Network notation F_Θ : (**x**, **d**) → (**c**, σ)
- **Citations:** 0
- **Special handling:** Bold vectors preserved, network architecture details

### Quality Metrics

- Semantic equivalence: 0.88 - Excellent preservation of architecture description
- Technical accuracy: 0.87 - Accurate translation of network components
- Readability: 0.85 - Clear technical flow
- Glossary consistency: 0.84 - Consistent terminology
- **Overall section score:** 0.86
