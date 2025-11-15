# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** view synthesis, scene representation, radiance, volume density, multilayer perceptron (MLP), neural radiance field (NeRF), rendering, optimization, gradient descent, positional encoding, hierarchical sampling, voxel grid, continuous function, differentiable, RGB color

---

### English Version

In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous 5D scene representation to minimize the error of rendering a set of captured images.

We represent a static scene as a continuous 5D function that outputs the radiance emitted in each direction (θ, φ) at each point (x, y, z) in space, and a density at each point which acts like a differential opacity controlling how much radiance is accumulated by a ray passing through (x, y, z). Our method optimizes a deep fully-connected neural network without any convolutional layers (often referred to as a multilayer perceptron or MLP) to represent this function by regressing from a single 5D coordinate (x, y, z, θ, φ) to a single volume density and view-dependent RGB color. To render this *neural radiance field* (NeRF) from a particular viewpoint we: 1) march camera rays through the scene to generate a sampled set of 3D points, 2) use those points and their corresponding 2D viewing directions as input to the neural network to produce an output set of colors and densities, and 3) use classical volume rendering techniques to accumulate those colors and densities into a 2D image. Because this process is naturally differentiable, we can use gradient descent to optimize this model by minimizing the error between each observed image and the corresponding views rendered from our representation. Minimizing this error across multiple views encourages the network to predict a coherent model of the scene by assigning high volume densities and accurate colors to the locations that contain the true underlying scene content. Figure 2 visualizes this overall pipeline.

We find that the basic implementation of optimizing a neural radiance field representation for a complex scene does not converge to a sufficiently high-resolution representation and is inefficient in the required number of samples per camera ray. We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we propose a hierarchical sampling procedure to reduce the number of queries required to adequately sample this high-frequency scene representation.

Our approach inherits the benefits of volumetric representations: both can represent complex real-world geometry and appearance and are well suited for gradient-based optimization using projected images. Crucially, our method overcomes the prohibitive storage costs of discretized voxel grids when modeling complex scenes at high-resolutions. In summary, our technical contributions are:

– An approach for representing continuous scenes with complex geometry and materials as 5D neural radiance fields, parameterized as basic MLP networks.
– A differentiable rendering procedure based on classical volume rendering techniques, which we use to optimize these representations from standard RGB images. This includes a hierarchical sampling strategy to allocate the MLP's capacity towards space with visible scene content.
– A positional encoding to map each input 5D coordinate into a higher dimensional space, which enables us to successfully optimize neural radiance fields to represent high-frequency scene content.

We demonstrate that our resulting neural radiance field method quantitatively and qualitatively outperforms state-of-the-art view synthesis methods, including works that fit neural 3D representations to scenes as well as works that train deep convolutional networks to predict sampled volumetric representations. As far as we know, this paper presents the first continuous neural scene representation that is able to render high-resolution photorealistic novel views of real objects and scenes from RGB images captured in natural settings.

---

### النسخة العربية

في هذا العمل، نتناول مشكلة تركيب المناظر التي طال أمدها بطريقة جديدة من خلال تحسين معاملات تمثيل مشهد خماسي الأبعاد مستمر مباشرةً لتقليل خطأ تصيير مجموعة من الصور الملتقطة.

نمثل مشهداً ثابتاً كدالة خماسية الأبعاد مستمرة تُخرج الإشعاع المنبعث في كل اتجاه (θ, φ) عند كل نقطة (x, y, z) في الفضاء، وكثافة عند كل نقطة تعمل كعتامة تفاضلية تتحكم في مقدار الإشعاع الذي يتراكم بواسطة شعاع يمر عبر (x, y, z). تقوم طريقتنا بتحسين شبكة عصبية عميقة متصلة بالكامل دون أي طبقات تلافيفية (يُشار إليها غالباً باسم الإدراك متعدد الطبقات أو MLP) لتمثيل هذه الدالة من خلال الانحدار من إحداثي خماسي الأبعاد واحد (x, y, z, θ, φ) إلى كثافة حجم واحدة ولون RGB معتمد على المنظر. لتصيير *حقل الإشعاع العصبي* هذا (NeRF) من منظور معين نقوم بما يلي: 1) نسير بأشعة الكاميرا عبر المشهد لتوليد مجموعة عينات من النقاط ثلاثية الأبعاد، 2) نستخدم تلك النقاط واتجاهات المشاهدة ثنائية الأبعاد المقابلة لها كمدخلات للشبكة العصبية لإنتاج مجموعة مخرجات من الألوان والكثافات، و3) نستخدم تقنيات تصيير الحجم الكلاسيكية لتراكم تلك الألوان والكثافات في صورة ثنائية الأبعاد. نظراً لأن هذه العملية قابلة للاشتقاق بطبيعتها، يمكننا استخدام الانحدار التدرجي لتحسين هذا النموذج من خلال تقليل الخطأ بين كل صورة ملاحظة والمناظر المقابلة المصيّرة من تمثيلنا. يشجع تقليل هذا الخطأ عبر مناظر متعددة الشبكة على التنبؤ بنموذج متماسك للمشهد من خلال تعيين كثافات حجم عالية وألوان دقيقة للمواقع التي تحتوي على محتوى المشهد الأساسي الحقيقي. يوضح الشكل 2 هذا المسار الكلي.

نجد أن التنفيذ الأساسي لتحسين تمثيل حقل إشعاع عصبي لمشهد معقد لا يتقارب إلى تمثيل عالي الدقة بشكل كافٍ ويكون غير فعال في عدد العينات المطلوبة لكل شعاع كاميرا. نعالج هذه المشكلات من خلال تحويل الإحداثيات الخماسية الأبعاد المدخلة باستخدام ترميز موضعي يمكّن MLP من تمثيل دوال ذات تردد أعلى، ونقترح إجراء أخذ عينات هرمي لتقليل عدد الاستعلامات المطلوبة لأخذ عينات كافية من تمثيل المشهد عالي التردد هذا.

يرث نهجنا فوائد التمثيلات الحجمية: كلاهما يمكنه تمثيل هندسة ومظهر العالم الحقيقي المعقدين ومناسب تماماً للتحسين القائم على التدرج باستخدام الصور المسقطة. والأهم من ذلك، تتغلب طريقتنا على تكاليف التخزين الباهظة للشبكات الحجمية المتقطعة عند نمذجة مشاهد معقدة بدقة عالية. باختصار، مساهماتنا التقنية هي:

– نهج لتمثيل المشاهد المستمرة ذات الهندسة والمواد المعقدة كحقول إشعاع عصبية خماسية الأبعاد، مُعلَمة كشبكات MLP أساسية.
– إجراء تصيير قابل للاشتقاق يعتمد على تقنيات تصيير الحجم الكلاسيكية، نستخدمه لتحسين هذه التمثيلات من صور RGB قياسية. يتضمن ذلك استراتيجية أخذ عينات هرمية لتخصيص سعة MLP نحو الفضاء الذي يحتوي على محتوى المشهد المرئي.
– ترميز موضعي لتعيين كل إحداثي خماسي الأبعاد مدخل إلى فضاء ذي أبعاد أعلى، مما يمكننا من تحسين حقول الإشعاع العصبية بنجاح لتمثيل محتوى المشهد عالي التردد.

نوضح أن طريقة حقل الإشعاع العصبي الناتجة لدينا تتفوق كمياً ونوعياً على أحدث طرق تركيب المناظر، بما في ذلك الأعمال التي تلائم تمثيلات ثلاثية الأبعاد عصبية للمشاهد وكذلك الأعمال التي تدرب شبكات تلافيفية عميقة للتنبؤ بتمثيلات حجمية معيّنة. على حد علمنا، يقدم هذا البحث أول تمثيل مشهد عصبي مستمر قادر على تصيير مناظر جديدة واقعية فوتوغرافياً عالية الدقة لأجسام ومشاهد حقيقية من صور RGB ملتقطة في إعدادات طبيعية.

---

### Translation Notes

- **Figures referenced:** Figure 2
- **Key terms introduced:** neural radiance field / NeRF (حقل الإشعاع العصبي), multilayer perceptron / MLP (الإدراك متعدد الطبقات), positional encoding (ترميز موضعي), hierarchical sampling (أخذ عينات هرمي), voxel grid (شبكة حجمية), differential opacity (عتامة تفاضلية)
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Italicized "neural radiance field" preserved in Arabic translation

### Quality Metrics

- Semantic equivalence: 0.90 - Excellent preservation of technical meaning
- Technical accuracy: 0.89 - Accurate translation of computer graphics and ML terms
- Readability: 0.87 - Natural flow with complex technical concepts
- Glossary consistency: 0.86 - Consistent use of established terminology
- **Overall section score:** 0.88
