# Section 3: The Improved Illumination Model
## القسم 3: نموذج الإضاءة المحسّن

**Section:** methodology
**Translation Quality:** 0.89
**Glossary Terms Used:** ray tracing (تتبع الأشعة), algorithm (خوارزمية), reflection (انعكاس), refraction (انكسار), illumination (إضاءة), recursive (عودي), tree (شجرة), vector (متجه)

---

### English Version

## The Ray Tree Concept

The improved illumination model presented in this paper extends the Phong model by adding two new terms to account for specular reflection and transmission:

$$I = I_a k_a + \sum_{i=1}^{n} I_i [k_d (\mathbf{N} \cdot \mathbf{L}_i) + k_s (\mathbf{R}_i \cdot \mathbf{V})^n] + k_s I_{refl} + k_t I_{trans}$$

where:
- $k_s$ is the reflection coefficient (determines how mirror-like the surface is)
- $I_{refl}$ is the intensity from the reflected ray
- $k_t$ is the transmission coefficient (determines transparency)
- $I_{trans}$ is the intensity from the transmitted (refracted) ray

The key innovation is that $I_{refl}$ and $I_{trans}$ are not simple constants but are themselves computed recursively by tracing rays in the reflection and refraction directions.

## Recursive Ray Tracing Algorithm

The algorithm works as follows:

1. **Primary Ray:** For each pixel, cast a ray from the eye through the pixel into the scene
2. **Intersection Test:** Find the nearest surface that the ray intersects
3. **Generate Secondary Rays:** At the intersection point, generate:
   - **Shadow rays:** One ray toward each light source to test visibility
   - **Reflection ray:** A ray in the mirror reflection direction
   - **Refraction ray:** A ray in the transmitted direction (if surface is transparent)
4. **Recursive Evaluation:** Repeat steps 2-3 for each secondary ray
5. **Combine Results:** Compute final intensity using the illumination equation

This process builds a tree structure where:
- The root is the primary ray from the eye
- Each node represents a ray-surface intersection
- Children of a node are the secondary rays (shadow, reflection, refraction)
- Leaf nodes are rays that escape the scene or reach maximum recursion depth

## Computing Reflection Direction

When a ray with direction $\mathbf{D}$ hits a surface with normal $\mathbf{N}$, the reflection direction $\mathbf{R}$ is computed as:

$$\mathbf{R} = \mathbf{D} - 2(\mathbf{D} \cdot \mathbf{N})\mathbf{N}$$

This is the standard law of reflection: the angle of incidence equals the angle of reflection.

## Computing Refraction Direction

For transparent surfaces, the refracted ray direction $\mathbf{T}$ is computed using Snell's law. If $\eta_1$ and $\eta_2$ are the indices of refraction on the two sides of the surface:

$$\eta_1 \sin(\theta_1) = \eta_2 \sin(\theta_2)$$

where $\theta_1$ is the angle of incidence and $\theta_2$ is the angle of refraction.

The transmitted ray direction can be computed as:

$$\mathbf{T} = \frac{\eta_1}{\eta_2}\mathbf{D} + \left(\frac{\eta_1}{\eta_2}(\mathbf{D} \cdot \mathbf{N}) - \sqrt{1 - \left(\frac{\eta_1}{\eta_2}\right)^2(1 - (\mathbf{D} \cdot \mathbf{N})^2)}\right)\mathbf{N}$$

**Total Internal Reflection:** When light travels from a denser medium to a less dense medium at a shallow angle, total internal reflection occurs. This happens when the term under the square root becomes negative. In this case, no refracted ray is generated, and all light is reflected.

## Shadow Computation

To determine if a surface point is in shadow with respect to a light source:

1. Cast a ray from the surface point toward the light source
2. Test if any object intersects this ray between the surface and the light
3. If an intersection is found, the point is in shadow from that light
4. The contribution from that light is set to zero in the illumination equation

This shadow ray testing adds realism by ensuring that objects properly cast shadows on other surfaces.

## Fresnel Reflection

For the most physically accurate results, the coefficients $k_s$ and $k_t$ should vary based on the viewing angle according to the Fresnel equations. At grazing angles, surfaces become more reflective; at perpendicular viewing angles, transparency dominates (for transparent materials).

For the implementation described in this paper, simplified constant values of $k_s$ and $k_t$ are used, but the framework supports angle-dependent coefficients for enhanced realism.

## Termination Criteria

The recursive ray tracing must terminate at some point. Rays stop generating children when:

1. **Maximum depth reached:** A predefined recursion limit prevents infinite loops
2. **Escapes scene:** The ray does not intersect any object
3. **Contribution threshold:** When $k_s$ or $k_t$ becomes very small, further recursion contributes negligibly to the final pixel intensity

This recursive approach captures global illumination effects including multiple reflections and refractions, producing images with a level of realism not achievable with local illumination models.

---

### النسخة العربية

## مفهوم شجرة الأشعة

يوسع نموذج الإضاءة المحسّن المقدم في هذه الورقة نموذج فونغ بإضافة حدّين جديدين لحساب الانعكاس اللامع والنقل:

$$I = I_a k_a + \sum_{i=1}^{n} I_i [k_d (\mathbf{N} \cdot \mathbf{L}_i) + k_s (\mathbf{R}_i \cdot \mathbf{V})^n] + k_s I_{refl} + k_t I_{trans}$$

حيث:
- $k_s$ هو معامل الانعكاس (يحدد مدى مرآوية السطح)
- $I_{refl}$ هي الشدة من الشعاع المنعكس
- $k_t$ هو معامل النقل (يحدد الشفافية)
- $I_{trans}$ هي الشدة من الشعاع المنقول (المنكسر)

الابتكار الرئيسي هو أن $I_{refl}$ و $I_{trans}$ ليسا ثوابت بسيطة بل يتم حسابهما بشكل عودي من خلال تتبع الأشعة في اتجاهات الانعكاس والانكسار.

## خوارزمية تتبع الأشعة العودية

تعمل الخوارزمية على النحو التالي:

1. **الشعاع الأساسي:** لكل بكسل، قم بإطلاق شعاع من العين عبر البكسل إلى المشهد
2. **اختبار التقاطع:** ابحث عن أقرب سطح يتقاطع معه الشعاع
3. **توليد الأشعة الثانوية:** عند نقطة التقاطع، قم بتوليد:
   - **أشعة الظل:** شعاع واحد باتجاه كل مصدر ضوء لاختبار الرؤية
   - **شعاع الانعكاس:** شعاع في اتجاه الانعكاس المرآوي
   - **شعاع الانكسار:** شعاع في اتجاه النقل (إذا كان السطح شفافاً)
4. **التقييم العودي:** كرر الخطوات 2-3 لكل شعاع ثانوي
5. **دمج النتائج:** احسب الشدة النهائية باستخدام معادلة الإضاءة

تبني هذه العملية بنية شجرية حيث:
- الجذر هو الشعاع الأساسي من العين
- كل عقدة تمثل تقاطع شعاع-سطح
- أبناء العقدة هم الأشعة الثانوية (الظل، الانعكاس، الانكسار)
- العقد الطرفية هي الأشعة التي تهرب من المشهد أو تصل إلى عمق العودية الأقصى

## حساب اتجاه الانعكاس

عندما يصطدم شعاع باتجاه $\mathbf{D}$ بسطح له عمودي $\mathbf{N}$، يُحسب اتجاه الانعكاس $\mathbf{R}$ كما يلي:

$$\mathbf{R} = \mathbf{D} - 2(\mathbf{D} \cdot \mathbf{N})\mathbf{N}$$

هذا هو قانون الانعكاس القياسي: زاوية السقوط تساوي زاوية الانعكاس.

## حساب اتجاه الانكسار

بالنسبة للأسطح الشفافة، يُحسب اتجاه الشعاع المنكسر $\mathbf{T}$ باستخدام قانون سنيل. إذا كان $\eta_1$ و $\eta_2$ هما معاملا الانكسار على جانبي السطح:

$$\eta_1 \sin(\theta_1) = \eta_2 \sin(\theta_2)$$

حيث $\theta_1$ هي زاوية السقوط و $\theta_2$ هي زاوية الانكسار.

يمكن حساب اتجاه الشعاع المنقول كما يلي:

$$\mathbf{T} = \frac{\eta_1}{\eta_2}\mathbf{D} + \left(\frac{\eta_1}{\eta_2}(\mathbf{D} \cdot \mathbf{N}) - \sqrt{1 - \left(\frac{\eta_1}{\eta_2}\right)^2(1 - (\mathbf{D} \cdot \mathbf{N})^2)}\right)\mathbf{N}$$

**الانعكاس الداخلي الكلي:** عندما ينتقل الضوء من وسط أكثر كثافة إلى وسط أقل كثافة بزاوية ضحلة، يحدث الانعكاس الداخلي الكلي. يحدث هذا عندما يصبح الحد تحت الجذر التربيعي سالباً. في هذه الحالة، لا يتم توليد شعاع منكسر، وينعكس كل الضوء.

## حساب الظلال

لتحديد ما إذا كانت نقطة السطح في الظل بالنسبة لمصدر ضوء:

1. قم بإطلاق شعاع من نقطة السطح باتجاه مصدر الضوء
2. اختبر ما إذا كان أي جسم يتقاطع مع هذا الشعاع بين السطح والضوء
3. إذا تم العثور على تقاطع، فإن النقطة في الظل من ذلك الضوء
4. يتم تعيين المساهمة من ذلك الضوء إلى صفر في معادلة الإضاءة

يضيف اختبار شعاع الظل هذا واقعية من خلال ضمان أن الأجسام تلقي ظلالاً بشكل صحيح على الأسطح الأخرى.

## انعكاس فرينل

للحصول على أدق النتائج فيزيائياً، يجب أن تتغير المعاملات $k_s$ و $k_t$ بناءً على زاوية المشاهدة وفقاً لمعادلات فرينل. عند الزوايا المائلة، تصبح الأسطح أكثر عكساً؛ عند زوايا المشاهدة العمودية، تسود الشفافية (للمواد الشفافة).

بالنسبة للتنفيذ الموصوف في هذه الورقة، يتم استخدام قيم ثابتة مبسطة لـ $k_s$ و $k_t$، لكن الإطار يدعم المعاملات التابعة للزاوية لتحسين الواقعية.

## معايير الإنهاء

يجب أن ينتهي تتبع الأشعة العودي في مرحلة ما. تتوقف الأشعة عن توليد الأبناء عندما:

1. **الوصول إلى العمق الأقصى:** حد العودية المحدد مسبقاً يمنع الحلقات اللانهائية
2. **الهروب من المشهد:** الشعاع لا يتقاطع مع أي جسم
3. **عتبة المساهمة:** عندما يصبح $k_s$ أو $k_t$ صغيراً جداً، فإن المزيد من العودية يساهم بشكل ضئيل في شدة البكسل النهائية

يلتقط هذا النهج العودي تأثيرات الإضاءة الشاملة بما في ذلك الانعكاسات والانكسارات المتعددة، منتجاً صوراً بمستوى من الواقعية لا يمكن تحقيقه مع نماذج الإضاءة المحلية.

---

### Translation Notes

- **Figures referenced:** Conceptual ray tree structure (would be Figure 1 in paper)
- **Key terms introduced:**
  - Ray tree (شجرة الأشعة)
  - Primary ray (الشعاع الأساسي)
  - Secondary rays (الأشعة الثانوية)
  - Shadow ray (شعاع الظل)
  - Reflection ray (شعاع الانعكاس)
  - Refraction ray (شعاع الانكسار)
  - Snell's law (قانون سنيل)
  - Total internal reflection (الانعكاس الداخلي الكلي)
  - Fresnel equations (معادلات فرينل)
  - Index of refraction (معامل الانكسار)
  - Recursion depth (عمق العودية)
- **Equations:** 4 main equations (illumination model, reflection direction, Snell's law, refraction vector)
- **Citations:** None in this section
- **Special handling:** Complex mathematical formulas preserved in LaTeX with detailed Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89
