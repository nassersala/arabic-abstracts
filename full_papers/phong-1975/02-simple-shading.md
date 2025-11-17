# Section 2: Simple Shading Models
## القسم 2: نماذج التظليل البسيطة

**Section:** simple-shading-models
**Translation Quality:** 0.87
**Glossary Terms Used:** diffuse reflection (الانعكاس المنتشر), Lambert's law (قانون لامبرت), surface normal (ناظم السطح), light source (مصدر ضوئي), intensity (شدة)

---

### English Version

The simplest approach to shading a polygon is to assign it a single constant intensity value. This is called **flat shading** or **constant shading**. In this method, the intensity is computed once for each polygon, typically using the polygon's surface normal and assuming the polygon is illuminated by one or more point light sources.

#### Diffuse Reflection (Lambert's Law)

The most basic illumination model considers only **diffuse reflection** from matte surfaces. According to Lambert's cosine law, the intensity $I$ reflected from a perfectly diffuse surface is proportional to the cosine of the angle between the surface normal $\vec{N}$ and the direction to the light source $\vec{L}$:

$$I_d = I_p k_d (\vec{N} \cdot \vec{L})$$

where:
- $I_d$ is the diffuse intensity
- $I_p$ is the intensity of the point light source
- $k_d$ is the diffuse reflection coefficient (0 ≤ $k_d$ ≤ 1)
- $\vec{N}$ is the unit surface normal vector
- $\vec{L}$ is the unit vector pointing toward the light source
- $\vec{N} \cdot \vec{L}$ is the dot product, which equals $\cos\theta$ where $\theta$ is the angle between the vectors

If $\vec{N} \cdot \vec{L}$ is negative (surface facing away from light), the intensity is set to zero since the surface is not directly illuminated.

#### Ambient Illumination

Real scenes contain indirect lighting from reflections off other surfaces and general environmental illumination. This is approximated by adding an **ambient term** $I_a$:

$$I = I_a k_a + I_p k_d (\vec{N} \cdot \vec{L})$$

where:
- $I_a$ is the ambient light intensity
- $k_a$ is the ambient reflection coefficient

The ambient term provides a baseline illumination level, ensuring that surfaces not directly lit are not completely black.

#### Limitations of Flat Shading

While computationally efficient, flat shading has severe visual limitations:

1. **Faceted appearance**: Each polygon is rendered with uniform intensity, making polygon boundaries highly visible
2. **Mach banding**: The human eye is sensitive to intensity discontinuities at polygon edges, making the faceting even more apparent
3. **Poor representation of curved surfaces**: Smooth curved objects appear angular and artificial
4. **No specular highlights**: Shiny materials cannot be represented since specular reflection requires view-dependent calculations

These limitations motivated the development of more sophisticated shading techniques that interpolate intensities across polygon surfaces, producing smoother, more realistic images. The following sections describe such interpolation methods.

---

### النسخة العربية

أبسط نهج لتظليل مضلع هو تعيين قيمة شدة ثابتة واحدة له. يُسمى هذا **التظليل المسطح** أو **التظليل الثابت**. في هذه الطريقة، يتم حساب الشدة مرة واحدة لكل مضلع، وعادة ما يتم ذلك باستخدام ناظم سطح المضلع وافتراض أن المضلع مضاء بواسطة مصدر ضوئي نقطي واحد أو أكثر.

#### الانعكاس المنتشر (قانون لامبرت)

يأخذ نموذج الإضاءة الأساسي في الاعتبار فقط **الانعكاس المنتشر** من الأسطح غير اللامعة. وفقاً لقانون جيب التمام للامبرت، فإن الشدة $I$ المنعكسة من سطح منتشر تماماً تتناسب مع جيب تمام الزاوية بين ناظم السطح $\vec{N}$ والاتجاه إلى المصدر الضوئي $\vec{L}$:

$$I_d = I_p k_d (\vec{N} \cdot \vec{L})$$

حيث:
- $I_d$ هي الشدة المنتشرة
- $I_p$ هي شدة المصدر الضوئي النقطي
- $k_d$ هو معامل الانعكاس المنتشر (0 ≤ $k_d$ ≤ 1)
- $\vec{N}$ هو متجه ناظم السطح الوحدوي
- $\vec{L}$ هو المتجه الوحدوي المشير نحو المصدر الضوئي
- $\vec{N} \cdot \vec{L}$ هو حاصل الضرب القياسي، والذي يساوي $\cos\theta$ حيث $\theta$ هي الزاوية بين المتجهين

إذا كان $\vec{N} \cdot \vec{L}$ سالباً (السطح يواجه بعيداً عن الضوء)، يتم تعيين الشدة إلى صفر لأن السطح غير مضاء بشكل مباشر.

#### الإضاءة المحيطة

تحتوي المشاهد الحقيقية على إضاءة غير مباشرة من الانعكاسات عن الأسطح الأخرى والإضاءة البيئية العامة. يتم تقريب ذلك بإضافة **مصطلح محيط** $I_a$:

$$I = I_a k_a + I_p k_d (\vec{N} \cdot \vec{L})$$

حيث:
- $I_a$ هي شدة الضوء المحيط
- $k_a$ هو معامل الانعكاس المحيط

يوفر المصطلح المحيط مستوى إضاءة أساسي، مما يضمن أن الأسطح التي لا تُضاء بشكل مباشر ليست سوداء تماماً.

#### قيود التظليل المسطح

على الرغم من الكفاءة الحسابية، فإن التظليل المسطح له قيود بصرية شديدة:

1. **المظهر المضلعي**: يُقدم كل مضلع بشدة موحدة، مما يجعل حدود المضلعات مرئية للغاية
2. **نطاق ماخ**: العين البشرية حساسة لانقطاعات الشدة عند حواف المضلعات، مما يجعل التضليع أكثر وضوحاً
3. **تمثيل ضعيف للأسطح المنحنية**: تظهر الأجسام المنحنية الملساء بمظهر زاوي واصطناعي
4. **عدم وجود نقاط تمييز مرآوية**: لا يمكن تمثيل المواد اللامعة لأن الانعكاس المرآوي يتطلب حسابات تعتمد على الرؤية

حفزت هذه القيود تطوير تقنيات تظليل أكثر تطوراً تستوفي الشدات عبر أسطح المضلعات، مما ينتج صوراً أكثر سلاسة وواقعية. تصف الأقسام التالية طرق الاستيفاء هذه.

---

### Translation Notes

- **Figures referenced:** None (equations and conceptual descriptions)
- **Key terms introduced:**
  - flat shading / constant shading (التظليل المسطح / التظليل الثابت)
  - diffuse reflection (الانعكاس المنتشر)
  - Lambert's law (قانون لامبرت)
  - surface normal (ناظم السطح)
  - ambient illumination (الإضاءة المحيطة)
  - Mach banding (نطاق ماخ) - perceptual edge enhancement effect
  - specular highlights (نقاط التمييز المرآوية)
  - matte surface (سطح غير لامع)
- **Equations:** 2 main equations (diffuse reflection, ambient + diffuse)
- **Citations:** Implicit reference to Lambert's law (18th century physics)
- **Special handling:** Mathematical formulas preserved in LaTeX, Arabic explanations provided

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation (Validation)

The simplest approach to shading a polygon is to assign it a single constant intensity value, called flat shading or constant shading. The intensity is computed once per polygon using the polygon's surface normal, assuming illumination by one or more point light sources.

The basic illumination model considers only diffuse reflection from non-shiny surfaces. According to Lambert's cosine law, the intensity $I$ reflected from a perfectly diffuse surface is proportional to the cosine of the angle between the surface normal $\vec{N}$ and the direction to the light source $\vec{L}$: $I_d = I_p k_d (\vec{N} \cdot \vec{L})$.

Real scenes contain indirect lighting from reflections and general environmental illumination, approximated by adding an ambient term: $I = I_a k_a + I_p k_d (\vec{N} \cdot \vec{L})$.

Despite computational efficiency, flat shading has severe visual limitations: faceted appearance, Mach banding sensitivity, poor representation of curved surfaces, and no specular highlights. These limitations motivated development of more sophisticated techniques that interpolate intensities across polygon surfaces.
