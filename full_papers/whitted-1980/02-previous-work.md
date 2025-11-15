# Section 2: Previous Work and Background
## القسم 2: الأعمال السابقة والخلفية

**Section:** previous-work
**Translation Quality:** 0.87
**Glossary Terms Used:** shading model (نموذج التظليل), diffuse reflection (انعكاس منتشر), specular reflection (انعكاس لامع), ambient light (ضوء محيط), normal vector (متجه عمودي), light source (مصدر ضوء), intensity (شدة), illumination (إضاءة)

---

### English Version

Early computer graphics rendering relied primarily on **hidden surface removal** algorithms to determine which surfaces are visible from the viewer's perspective. Once visibility was established, simple shading models were applied to compute surface colors. The most widely used shading model at the time this paper was written was the **Phong illumination model**, developed by Bui Tuong Phong.

#### The Phong Shading Model

The Phong model computes the intensity at a point on a surface as the sum of three components:

$$I = I_a + I_d + I_s$$

where:

1. **Ambient term** ($I_a$): Represents uniform background illumination
   $$I_a = k_a I_\text{ambient}$$

2. **Diffuse term** ($I_d$): Represents matte, Lambertian reflection
   $$I_d = k_d I_\text{light} (\vec{N} \cdot \vec{L})$$

3. **Specular term** ($I_s$): Represents shiny highlights
   $$I_s = k_s I_\text{light} (\vec{R} \cdot \vec{V})^n$$

Here, $\vec{N}$ is the surface normal, $\vec{L}$ is the direction to the light source, $\vec{R}$ is the reflection direction, $\vec{V}$ is the view direction, and $n$ is the specular exponent controlling highlight sharpness. The coefficients $k_a$, $k_d$, and $k_s$ control the relative weights of each component.

#### Limitations of Local Shading Models

While the Phong model produces reasonable results for many surfaces, it has fundamental limitations:

1. **No inter-object reflections**: Mirror-like surfaces cannot reflect other objects in the scene. The specular term only produces highlights from light sources, not reflections of surrounding geometry.

2. **No transparency**: The model cannot handle transparent materials like glass or water that refract light according to Snell's law.

3. **No realistic shadows**: Shadows are typically handled as a separate visibility problem, often with techniques like shadow volumes or shadow maps. These approaches are complex and may not integrate naturally with the shading model.

4. **Local computation**: Each surface point is shaded independently based only on its local properties and direct illumination. There is no mechanism to account for global light transport.

5. **No color bleeding**: Light bouncing between colored surfaces (interreflection) cannot be represented.

#### Early Ray Tracing Work

The concept of ray tracing itself predates this paper. **Appel (1968)** used ray casting for visibility determination, tracing rays from the eye through pixels to find the nearest surface. **Goldstein and Nagel (1971)** extended this to handle shadows by testing visibility to light sources. However, these early approaches did not use **recursive** ray tracing to follow reflections and refractions.

The key innovation of this paper is the **recursive** nature of the ray tracing: when a ray hits a reflective or transparent surface, additional rays are spawned to follow the reflection or refraction. This recursion continues until rays either hit a light source, escape the scene, or reach a maximum depth limit.

#### Motivation for the Improved Model

The goal of this work is to extend ray tracing to accurately simulate global illumination phenomena that local models cannot handle. By recursively tracing rays through reflections, refractions, and shadow tests, we can compute illumination that accounts for the entire environment, not just direct lighting.

The resulting images can show:
- Perfect mirror reflections of other objects
- Transparent objects with correct refraction (bending of light)
- Accurate hard shadows from point light sources
- Multiple levels of reflection (e.g., a mirror reflecting another mirror)

This comes at a computational cost - recursive ray tracing is significantly more expensive than local shading. However, for applications requiring high visual fidelity, this trade-off is acceptable.

---

### النسخة العربية

اعتمد التقديم في الرسومات الحاسوبية المبكرة بشكل أساسي على خوارزميات **إزالة الأسطح المخفية** لتحديد الأسطح المرئية من منظور المشاهد. بمجرد تحديد الرؤية، تم تطبيق نماذج تظليل بسيطة لحساب ألوان الأسطح. كان نموذج التظليل الأكثر استخداماً في وقت كتابة هذه الورقة هو **نموذج إضاءة فونج**، الذي طوره بوي توونج فونج.

#### نموذج تظليل فونج

يحسب نموذج فونج الشدة عند نقطة على سطح كمجموع ثلاثة مكونات:

$$I = I_a + I_d + I_s$$

حيث:

1. **حد الإضاءة المحيطة** ($I_a$): يمثل الإضاءة الخلفية الموحدة
   $$I_a = k_a I_\text{ambient}$$

2. **حد الانعكاس المنتشر** ($I_d$): يمثل الانعكاس غير اللامع، الانعكاس اللامبرتي
   $$I_d = k_d I_\text{light} (\vec{N} \cdot \vec{L})$$

3. **حد الانعكاس اللامع** ($I_s$): يمثل البقع اللامعة
   $$I_s = k_s I_\text{light} (\vec{R} \cdot \vec{V})^n$$

هنا، $\vec{N}$ هو العمودي على السطح، $\vec{L}$ هو الاتجاه إلى مصدر الضوء، $\vec{R}$ هو اتجاه الانعكاس، $\vec{V}$ هو اتجاه الرؤية، و $n$ هو الأس اللامع الذي يتحكم في حدة البقعة اللامعة. تتحكم المعاملات $k_a$ و $k_d$ و $k_s$ في الأوزان النسبية لكل مكون.

#### قيود نماذج التظليل المحلية

بينما ينتج نموذج فونج نتائج معقولة للعديد من الأسطح، إلا أن له قيوداً أساسية:

1. **لا توجد انعكاسات بين الكائنات**: الأسطح الشبيهة بالمرآة لا يمكنها عكس كائنات أخرى في المشهد. ينتج الحد اللامع فقط بقعاً لامعة من مصادر الضوء، وليس انعكاسات للهندسة المحيطة.

2. **لا شفافية**: لا يمكن للنموذج التعامل مع المواد الشفافة مثل الزجاج أو الماء التي تنكسر الضوء وفقاً لقانون سنل.

3. **لا ظلال واقعية**: يتم التعامل مع الظلال عادةً كمشكلة رؤية منفصلة، غالباً بتقنيات مثل أحجام الظل أو خرائط الظل. هذه الأساليب معقدة وقد لا تتكامل بشكل طبيعي مع نموذج التظليل.

4. **حساب محلي**: يتم تظليل كل نقطة على السطح بشكل مستقل بناءً فقط على خصائصها المحلية والإضاءة المباشرة. لا توجد آلية لحساب نقل الضوء الشامل.

5. **لا نزيف لوني**: لا يمكن تمثيل الضوء المرتد بين الأسطح الملونة (الانعكاس المتبادل).

#### أعمال تتبع الأشعة المبكرة

مفهوم تتبع الأشعة نفسه يسبق هذه الورقة. استخدم **أبل (1968)** إرسال الأشعة لتحديد الرؤية، حيث تتبع الأشعة من العين عبر البكسلات لإيجاد أقرب سطح. وسع **غولدستين وناجل (1971)** هذا للتعامل مع الظلال باختبار الرؤية إلى مصادر الضوء. ومع ذلك، لم تستخدم هذه الأساليب المبكرة تتبع الأشعة **التكراري** لمتابعة الانعكاسات والانكسارات.

الابتكار الرئيسي في هذه الورقة هو الطبيعة **التكرارية** لتتبع الأشعة: عندما يصطدم شعاع بسطح عاكس أو شفاف، يتم توليد أشعة إضافية لمتابعة الانعكاس أو الانكسار. يستمر هذا التكرار حتى تصطدم الأشعة بمصدر ضوء، أو تهرب من المشهد، أو تصل إلى حد أقصى للعمق.

#### الدافع للنموذج المحسّن

الهدف من هذا العمل هو توسيع تتبع الأشعة لمحاكاة ظواهر الإضاءة الشاملة بدقة والتي لا يمكن للنماذج المحلية التعامل معها. من خلال تتبع الأشعة بشكل تكراري عبر الانعكاسات والانكسارات واختبارات الظل، يمكننا حساب الإضاءة التي تأخذ في الاعتبار البيئة بأكملها، وليس فقط الإضاءة المباشرة.

يمكن للصور الناتجة أن تُظهر:
- انعكاسات مرآة مثالية لكائنات أخرى
- كائنات شفافة مع انكسار صحيح (انحناء الضوء)
- ظلال حادة دقيقة من مصادر ضوء نقطية
- مستويات متعددة من الانعكاس (مثلاً، مرآة تعكس مرآة أخرى)

يأتي هذا بتكلفة حسابية - تتبع الأشعة التكراري أغلى بكثير من التظليل المحلي. ومع ذلك، للتطبيقات التي تتطلب دقة بصرية عالية، هذه المقايضة مقبولة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Phong illumination model (نموذج إضاءة فونج)
  - Lambertian reflection (انعكاس لامبرتي)
  - Specular exponent (أس لامع)
  - Color bleeding (نزيف لوني)
  - Ray casting (إرسال الأشعة)
  - Recursive ray tracing (تتبع الأشعة التكراري)
- **Equations:** 5 mathematical formulas for Phong shading model
- **Citations:** Appel (1968), Goldstein and Nagel (1971), Phong shading model
- **Special handling:** Mathematical equations preserved in LaTeX, Arabic explanations added

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-Translation Verification

Early computer graphics rendering relied primarily on hidden surface removal algorithms. The most widely used shading model was the Phong illumination model, which computes intensity as the sum of ambient, diffuse, and specular components. While producing reasonable results, it has fundamental limitations: no inter-object reflections, no transparency, no realistic shadows, local computation only, and no color bleeding. Early ray tracing work by Appel (1968) and Goldstein and Nagel (1971) traced rays for visibility but did not use recursive ray tracing. The key innovation is the recursive nature: spawning additional rays to follow reflections and refractions, continuing until rays hit a light source, escape, or reach maximum depth.
