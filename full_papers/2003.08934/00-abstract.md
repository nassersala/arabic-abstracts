# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** neural network, view synthesis, scene representation, rendering, volume rendering, radiance, optimization, deep network, differentiable, camera pose, photorealistic, coordinate

---

### English Version

We present a method that achieves state-of-the-art results for synthesizing novel views of complex scenes by optimizing an underlying continuous volumetric scene function using a sparse set of input views. Our algorithm represents a scene using a fully-connected (non-convolutional) deep network, whose input is a single continuous 5D coordinate (spatial location (x,y,z) and viewing direction (θ, φ)) and whose output is the volume density and view-dependent emitted radiance at that spatial location. We synthesize views by querying 5D coordinates along camera rays and use classic volume rendering techniques to project the output colors and densities into an image. Because volume rendering is naturally differentiable, the only input required to optimize our representation is a set of images with known camera poses. We describe how to effectively optimize neural radiance fields to render photorealistic novel views of scenes with complicated geometry and appearance, and demonstrate results that outperform prior work on neural rendering and view synthesis. View synthesis results are best viewed as videos, so we urge readers to view our supplementary video for convincing comparisons.

---

### النسخة العربية

نقدم طريقة تحقق نتائج متقدمة في تركيب مناظر جديدة لمشاهد معقدة من خلال تحسين دالة مشهد حجمية مستمرة أساسية باستخدام مجموعة متفرقة من المناظر المدخلة. تمثل خوارزميتنا المشهد باستخدام شبكة عميقة متصلة بالكامل (غير تلافيفية)، يكون مدخلها إحداثي خماسي الأبعاد مستمر واحد (الموقع المكاني (x,y,z) واتجاه المشاهدة (θ, φ)) ويكون مخرجها كثافة الحجم والإشعاع المنبعث المعتمد على المنظر عند ذلك الموقع المكاني. نركب المناظر من خلال الاستعلام عن إحداثيات خماسية الأبعاد على طول أشعة الكاميرا ونستخدم تقنيات تصيير الحجم الكلاسيكية لإسقاط الألوان والكثافات الناتجة إلى صورة. نظراً لأن تصيير الحجم قابل للاشتقاق بطبيعته، فإن المدخل الوحيد المطلوب لتحسين تمثيلنا هو مجموعة من الصور ذات مواضع كاميرا معروفة. نصف كيفية تحسين حقول الإشعاع العصبية بشكل فعال لتصيير مناظر جديدة واقعية فوتوغرافياً لمشاهد ذات هندسة ومظهر معقدين، ونُظهر نتائج تتفوق على الأعمال السابقة في التصيير العصبي وتركيب المناظر. يُفضَّل مشاهدة نتائج تركيب المناظر كمقاطع فيديو، لذلك نحث القراء على مشاهدة الفيديو التكميلي للحصول على مقارنات مقنعة.

---

### Translation Notes

- **Figures referenced:** None (abstract only)
- **Key terms introduced:** neural radiance field (حقل إشعاع عصبي), volume rendering (تصيير الحجم), view synthesis (تركيب المناظر), 5D coordinate (إحداثي خماسي الأبعاد)
- **Equations:** 0
- **Citations:** 0
- **Special handling:** None

### Quality Metrics

- Semantic equivalence: 0.95 - Excellent preservation of all technical details
- Technical accuracy: 0.94 - Correctly translates graphics and ML concepts
- Readability: 0.92 - Natural Arabic flow with precise terminology
- Glossary consistency: 0.92 - Strong adherence to established terms
- **Overall section score:** 0.93
