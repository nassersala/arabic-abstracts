# Section 3: The Illumination Model
## القسم 3: نموذج الإضاءة

**Section:** illumination-model
**Translation Quality:** 0.90
**Glossary Terms Used:** reflection (انعكاس), vector (متجه), normal (ناظم), intensity (شدة), angle (زاوية), cosine (جيب التمام)

---

### English Version

The illumination model presented in this section forms the basis for calculating the intensity of light at any point on a surface. The model considers three components of light reflection: ambient reflection, diffuse reflection, and specular reflection. Each component contributes to the final intensity based on the surface properties and the geometry of the viewing situation.

#### Basic Assumptions

We assume that light sources are point sources, and we ignore atmospheric effects and interreflection between objects. The model focuses on local illumination at a single point on the surface. The following vectors are defined at each surface point:

- **N**: the unit normal vector to the surface
- **L**: the unit vector from the surface point toward the light source
- **V**: the unit vector from the surface point toward the viewer
- **R**: the unit reflection vector, which is the direction a perfect mirror would reflect light from source L

The reflection vector R can be computed from L and N using the reflection law:

$$\mathbf{R} = 2(\mathbf{N} \cdot \mathbf{L})\mathbf{N} - \mathbf{L}$$

#### Ambient Reflection

Ambient light represents the overall level of illumination in the scene, coming from all directions due to multiple reflections from other surfaces. It is assumed to be constant everywhere and is independent of the surface orientation. The ambient component of intensity is:

$$I_a = k_a I_{a,light}$$

where:
- $k_a$ is the ambient reflection coefficient (0 ≤ $k_a$ ≤ 1)
- $I_{a,light}$ is the intensity of ambient light

#### Diffuse Reflection (Lambertian Reflection)

Diffuse reflection occurs on matte surfaces that scatter light equally in all directions. According to Lambert's cosine law, the intensity of diffusely reflected light is proportional to the cosine of the angle between the surface normal N and the light direction L. The diffuse component is:

$$I_d = k_d I_{light} (\mathbf{N} \cdot \mathbf{L})$$

where:
- $k_d$ is the diffuse reflection coefficient (0 ≤ $k_d$ ≤ 1)
- $I_{light}$ is the intensity of the point light source
- $\mathbf{N} \cdot \mathbf{L}$ is the dot product of the normal and light vectors (equals cos θ)

If $\mathbf{N} \cdot \mathbf{L}$ is negative (light source behind the surface), the diffuse component is zero.

#### Specular Reflection

Specular reflection creates highlights on shiny surfaces. Unlike diffuse reflection, specular reflection is highly directional. The intensity of specular reflection depends on the angle between the reflection vector R and the viewing direction V. The specular component is modeled as:

$$I_s = k_s I_{light} (\mathbf{R} \cdot \mathbf{V})^n$$

where:
- $k_s$ is the specular reflection coefficient (0 ≤ $k_s$ ≤ 1)
- $n$ is the shininess exponent (typically 1 to 200)
- $\mathbf{R} \cdot \mathbf{V}$ is the dot product of reflection and view vectors (equals cos α)

The exponent $n$ controls the size and sharpness of the specular highlight. Large values of $n$ produce small, sharp highlights characteristic of very shiny surfaces (like polished metal), while small values produce larger, softer highlights (like plastic or semi-gloss surfaces).

If $\mathbf{R} \cdot \mathbf{V}$ is negative, the specular component is zero.

#### Complete Illumination Model

The total intensity at a surface point is the sum of all three components:

$$I = I_a + I_d + I_s = k_a I_{a,light} + k_d I_{light} (\mathbf{N} \cdot \mathbf{L}) + k_s I_{light} (\mathbf{R} \cdot \mathbf{V})^n$$

For colored images, this calculation is performed separately for red, green, and blue components, with potentially different reflection coefficients ($k_a$, $k_d$, $k_s$) for each color channel.

#### Multiple Light Sources

When multiple light sources are present, the contributions from each source are summed. The ambient component is computed once, while diffuse and specular components are computed for each light source:

$$I = k_a I_{a,light} + \sum_{i=1}^{m} [k_d I_{i} (\mathbf{N} \cdot \mathbf{L}_i) + k_s I_{i} (\mathbf{R}_i \cdot \mathbf{V})^n]$$

where $m$ is the number of light sources, and subscript $i$ denotes quantities for the $i$-th light source.

#### Physical Basis

This model is a simplification of physical optics but captures the essential visual characteristics of surface appearance. The ambient term approximates global illumination effects. The diffuse term follows Lambert's law, which is physically accurate for ideal matte surfaces. The specular term is an empirical approximation (not derived from physics) but effectively models the appearance of glossy surfaces as perceived by human vision.

The model parameters ($k_a$, $k_d$, $k_s$, $n$) can be adjusted to simulate different material properties:
- Matte surfaces: high $k_d$, low $k_s$
- Shiny surfaces: moderate $k_d$, high $k_s$, large $n$
- Metallic surfaces: low $k_d$, high $k_s$, very large $n$

---

### النسخة العربية

نموذج الإضاءة المقدم في هذا القسم يشكل الأساس لحساب شدة الضوء عند أي نقطة على السطح. يأخذ النموذج في الاعتبار ثلاثة مكونات لانعكاس الضوء: الانعكاس المحيط، والانعكاس المنتشر، والانعكاس اللامع. كل مكون يساهم في الشدة النهائية بناءً على خصائص السطح وهندسة موقف المشاهدة.

#### الافتراضات الأساسية

نفترض أن مصادر الضوء هي مصادر نقطية، ونتجاهل التأثيرات الجوية والانعكاس المتبادل بين الأجسام. يركز النموذج على الإضاءة المحلية عند نقطة واحدة على السطح. يتم تعريف المتجهات التالية عند كل نقطة سطح:

- **N**: متجه الناظم الوحدوي للسطح
- **L**: المتجه الوحدوي من نقطة السطح باتجاه مصدر الضوء
- **V**: المتجه الوحدوي من نقطة السطح باتجاه المشاهد
- **R**: متجه الانعكاس الوحدوي، وهو الاتجاه الذي ستعكس فيه مرآة مثالية الضوء من المصدر L

يمكن حساب متجه الانعكاس R من L و N باستخدام قانون الانعكاس:

$$\mathbf{R} = 2(\mathbf{N} \cdot \mathbf{L})\mathbf{N} - \mathbf{L}$$

#### الانعكاس المحيط

يمثل الضوء المحيط المستوى العام للإضاءة في المشهد، القادم من جميع الاتجاهات بسبب الانعكاسات المتعددة من الأسطح الأخرى. يُفترض أنه ثابت في كل مكان ومستقل عن اتجاه السطح. مكون الشدة المحيط هو:

$$I_a = k_a I_{a,light}$$

حيث:
- $k_a$ هو معامل الانعكاس المحيط (0 ≤ $k_a$ ≤ 1)
- $I_{a,light}$ هي شدة الضوء المحيط

#### الانعكاس المنتشر (الانعكاس اللامبرتي)

يحدث الانعكاس المنتشر على الأسطح غير اللامعة التي تشتت الضوء بالتساوي في جميع الاتجاهات. وفقاً لقانون جيب التمام لامبرت، تتناسب شدة الضوء المنعكس بشكل منتشر مع جيب تمام الزاوية بين ناظم السطح N واتجاه الضوء L. المكون المنتشر هو:

$$I_d = k_d I_{light} (\mathbf{N} \cdot \mathbf{L})$$

حيث:
- $k_d$ هو معامل الانعكاس المنتشر (0 ≤ $k_d$ ≤ 1)
- $I_{light}$ هي شدة مصدر الضوء النقطي
- $\mathbf{N} \cdot \mathbf{L}$ هو الضرب النقطي لمتجهي الناظم والضوء (يساوي cos θ)

إذا كان $\mathbf{N} \cdot \mathbf{L}$ سالباً (مصدر الضوء خلف السطح)، فإن المكون المنتشر يساوي صفراً.

#### الانعكاس اللامع

ينشئ الانعكاس اللامع إبرازات على الأسطح اللامعة. على عكس الانعكاس المنتشر، الانعكاس اللامع اتجاهي للغاية. تعتمد شدة الانعكاس اللامع على الزاوية بين متجه الانعكاس R واتجاه المشاهدة V. يتم نمذجة المكون اللامع كـ:

$$I_s = k_s I_{light} (\mathbf{R} \cdot \mathbf{V})^n$$

حيث:
- $k_s$ هو معامل الانعكاس اللامع (0 ≤ $k_s$ ≤ 1)
- $n$ هو أس اللمعان (عادةً من 1 إلى 200)
- $\mathbf{R} \cdot \mathbf{V}$ هو الضرب النقطي لمتجهي الانعكاس والمشاهدة (يساوي cos α)

يتحكم الأس $n$ في حجم وحدة الإبراز اللامع. القيم الكبيرة لـ $n$ تنتج إبرازات صغيرة حادة مميزة للأسطح اللامعة جداً (مثل المعدن المصقول)، بينما القيم الصغيرة تنتج إبرازات أكبر وأنعم (مثل البلاستيك أو الأسطح شبه اللامعة).

إذا كان $\mathbf{R} \cdot \mathbf{V}$ سالباً، فإن المكون اللامع يساوي صفراً.

#### نموذج الإضاءة الكامل

الشدة الكلية عند نقطة السطح هي مجموع المكونات الثلاثة:

$$I = I_a + I_d + I_s = k_a I_{a,light} + k_d I_{light} (\mathbf{N} \cdot \mathbf{L}) + k_s I_{light} (\mathbf{R} \cdot \mathbf{V})^n$$

للصور الملونة، يتم إجراء هذا الحساب بشكل منفصل لمكونات الأحمر والأخضر والأزرق، مع معاملات انعكاس مختلفة محتملة ($k_a$، $k_d$، $k_s$) لكل قناة لونية.

#### مصادر ضوء متعددة

عندما تكون مصادر ضوء متعددة موجودة، يتم جمع المساهمات من كل مصدر. يتم حساب المكون المحيط مرة واحدة، بينما يتم حساب المكونات المنتشرة واللامعة لكل مصدر ضوء:

$$I = k_a I_{a,light} + \sum_{i=1}^{m} [k_d I_{i} (\mathbf{N} \cdot \mathbf{L}_i) + k_s I_{i} (\mathbf{R}_i \cdot \mathbf{V})^n]$$

حيث $m$ هو عدد مصادر الضوء، والمؤشر السفلي $i$ يشير إلى الكميات لمصدر الضوء $i$.

#### الأساس الفيزيائي

هذا النموذج هو تبسيط للبصريات الفيزيائية لكنه يلتقط الخصائص البصرية الأساسية لمظهر السطح. يقرّب المصطلح المحيط تأثيرات الإضاءة العالمية. يتبع المصطلح المنتشر قانون لامبرت، وهو دقيق فيزيائياً للأسطح غير اللامعة المثالية. المصطلح اللامع هو تقريب تجريبي (غير مشتق من الفيزياء) لكنه يمذّج بشكل فعال مظهر الأسطح اللامعة كما يدركها الرؤية البشرية.

يمكن ضبط معاملات النموذج ($k_a$، $k_d$، $k_s$، $n$) لمحاكاة خصائص المواد المختلفة:
- الأسطح غير اللامعة: $k_d$ عالية، $k_s$ منخفضة
- الأسطح اللامعة: $k_d$ معتدلة، $k_s$ عالية، $n$ كبيرة
- الأسطح المعدنية: $k_d$ منخفضة، $k_s$ عالية، $n$ كبيرة جداً

---

### Translation Notes

- **Figures referenced:** None explicitly, but geometric relationships described
- **Key terms introduced:**
  - point source (مصدر نقطي)
  - unit vector (متجه وحدوي)
  - reflection vector (متجه الانعكاس)
  - dot product (ضرب نقطي)
  - ambient light (ضوء محيط)
  - diffuse reflection (انعكاس منتشر)
  - Lambertian reflection (انعكاس لامبرتي)
  - Lambert's cosine law (قانون جيب التمام لامبرت)
  - specular reflection (انعكاس لامع)
  - shininess exponent (أس اللمعان)
  - matte surface (سطح غير لامع)
  - glossy surface (سطح لامع)
  - metallic surface (سطح معدني)
- **Equations:** 6 major equations with proper LaTeX formatting
- **Citations:** Lambert's law referenced
- **Special handling:** Mathematical notation preserved, Arabic explanations added for key variables

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.93
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.90
