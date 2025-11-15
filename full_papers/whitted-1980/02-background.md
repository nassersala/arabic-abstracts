# Section 2: Background - Previous Shading Models
## القسم 2: الخلفية - نماذج التظليل السابقة

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** illumination (إضاءة), algorithm (خوارزمية), shading (التظليل), rendering (التقديم), vector (متجه), normal (عمودي), surface (سطح)

---

### English Version

## The Phong Illumination Model

The standard approach to shading in computer graphics at the time of this work was the illumination model developed by Phong. This model calculates the intensity $I$ at a point on a surface as:

$$I = I_a k_a + \sum_{i=1}^{n} I_i [k_d (\mathbf{N} \cdot \mathbf{L}_i) + k_s (\mathbf{R}_i \cdot \mathbf{V})^n]$$

where:
- $I_a$ is the intensity of ambient light
- $k_a$ is the ambient reflection coefficient
- $I_i$ is the intensity of light source $i$
- $k_d$ is the diffuse reflection coefficient
- $k_s$ is the specular reflection coefficient
- $\mathbf{N}$ is the surface normal vector
- $\mathbf{L}_i$ is the direction vector to light source $i$
- $\mathbf{R}_i$ is the reflection direction of $\mathbf{L}_i$ about $\mathbf{N}$
- $\mathbf{V}$ is the direction vector to the viewer
- $n$ is the specular exponent (shininess)

### Components of the Phong Model

**Ambient Term ($I_a k_a$):** This constant term approximates light that has been scattered so many times in the environment that its directional distribution is uniform. It ensures that no surface appears completely black.

**Diffuse Term ($k_d (\mathbf{N} \cdot \mathbf{L}_i)$):** This implements Lambert's cosine law, stating that the intensity of diffusely reflected light is proportional to the cosine of the angle between the surface normal and the light direction. This gives surfaces a matte appearance.

**Specular Term ($k_s (\mathbf{R}_i \cdot \mathbf{V})^n$):** This produces highlights on shiny surfaces. The intensity falls off sharply as the viewing direction deviates from the perfect reflection direction. The exponent $n$ controls the size and sharpness of the highlight.

### Limitations of the Phong Model

While the Phong model successfully simulates local illumination effects, it has several significant limitations:

1. **No Mirror Reflections:** The specular term produces highlights but does not show reflections of other objects. A mirror should reflect the entire scene, not just produce bright spots.

2. **No Transparency:** The model has no mechanism for simulating transparent materials like glass or water, which both reflect and transmit light.

3. **No Shadows:** The model assumes all lights contribute to every visible surface point. It does not test whether light paths are blocked by other objects.

4. **Local Illumination Only:** Each surface point is shaded independently based only on direct lighting. Light reflected from one surface to another (indirect illumination) is ignored.

5. **No Refraction:** When light passes through transparent materials, it bends according to Snell's law. This is not modeled.

These limitations prevent the Phong model from producing photorealistic images. Real scenes exhibit rich interplay of reflections, refractions, and shadows that are essential for visual realism but absent from the Phong model.

---

### النسخة العربية

## نموذج إضاءة فونغ

كان النهج القياسي للتظليل في الرسومات الحاسوبية في وقت هذا العمل هو نموذج الإضاءة الذي طوره فونغ. يحسب هذا النموذج الشدة $I$ عند نقطة على السطح على النحو التالي:

$$I = I_a k_a + \sum_{i=1}^{n} I_i [k_d (\mathbf{N} \cdot \mathbf{L}_i) + k_s (\mathbf{R}_i \cdot \mathbf{V})^n]$$

حيث:
- $I_a$ هي شدة الضوء المحيط
- $k_a$ هو معامل الانعكاس المحيط
- $I_i$ هي شدة مصدر الضوء $i$
- $k_d$ هو معامل الانعكاس المنتشر
- $k_s$ هو معامل الانعكاس اللامع
- $\mathbf{N}$ هو متجه العمودي على السطح
- $\mathbf{L}_i$ هو متجه الاتجاه إلى مصدر الضوء $i$
- $\mathbf{R}_i$ هو اتجاه انعكاس $\mathbf{L}_i$ حول $\mathbf{N}$
- $\mathbf{V}$ هو متجه الاتجاه إلى المشاهد
- $n$ هو الأس اللامع (درجة اللمعان)

### مكونات نموذج فونغ

**الحد المحيط ($I_a k_a$):** يقرّب هذا الحد الثابت الضوء الذي تم تشتيته عدة مرات في البيئة بحيث أصبح توزيعه الاتجاهي موحداً. يضمن عدم ظهور أي سطح بشكل أسود تماماً.

**الحد المنتشر ($k_d (\mathbf{N} \cdot \mathbf{L}_i)$):** ينفذ هذا قانون جيب التمام لامبرت، الذي ينص على أن شدة الضوء المنعكس بشكل منتشر تتناسب مع جيب تمام الزاوية بين العمودي على السطح واتجاه الضوء. يعطي هذا الأسطح مظهراً غير لامع.

**الحد اللامع ($k_s (\mathbf{R}_i \cdot \mathbf{V})^n$):** ينتج هذا نقاط سطوع على الأسطح اللامعة. تنخفض الشدة بشكل حاد مع انحراف اتجاه المشاهدة عن اتجاه الانعكاس المثالي. يتحكم الأس $n$ في حجم وحدة نقطة السطوع.

### قيود نموذج فونغ

بينما ينجح نموذج فونغ في محاكاة تأثيرات الإضاءة المحلية، لديه عدة قيود كبيرة:

1. **عدم وجود انعكاسات مرآوية:** ينتج الحد اللامع نقاط سطوع لكنه لا يُظهر انعكاسات الأجسام الأخرى. يجب أن تعكس المرآة المشهد بأكمله، وليس فقط إنتاج نقاط ساطعة.

2. **عدم وجود شفافية:** لا يوجد لدى النموذج آلية لمحاكاة المواد الشفافة مثل الزجاج أو الماء، والتي تعكس وتنقل الضوء.

3. **عدم وجود ظلال:** يفترض النموذج أن جميع الأضواء تساهم في كل نقطة سطح مرئية. لا يختبر ما إذا كانت مسارات الضوء محجوبة بواسطة أجسام أخرى.

4. **الإضاءة المحلية فقط:** يتم تظليل كل نقطة سطح بشكل مستقل بناءً على الإضاءة المباشرة فقط. يتم تجاهل الضوء المنعكس من سطح إلى آخر (الإضاءة غير المباشرة).

5. **عدم وجود انكسار:** عندما يمر الضوء عبر المواد الشفافة، ينحني وفقاً لقانون سنيل. هذا غير مُنمذَج.

تمنع هذه القيود نموذج فونغ من إنتاج صور واقعية فوتوغرافياً. تُظهر المشاهد الحقيقية تفاعلاً غنياً من الانعكاسات والانكسارات والظلال الضرورية للواقعية البصرية ولكنها غائبة عن نموذج فونغ.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Phong illumination model (نموذج إضاءة فونغ)
  - Ambient reflection coefficient (معامل الانعكاس المحيط)
  - Diffuse reflection coefficient (معامل الانعكاس المنتشر)
  - Specular reflection coefficient (معامل الانعكاس اللامع)
  - Surface normal (العمودي على السطح)
  - Lambert's cosine law (قانون جيب التمام لامبرت)
  - Snell's law (قانون سنيل)
  - Local illumination (الإضاءة المحلية)
  - Indirect illumination (الإضاءة غير المباشرة)
- **Equations:** 1 main illumination equation
- **Citations:** Reference to Phong's work
- **Special handling:** Mathematical equations preserved in LaTeX format with Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.87
