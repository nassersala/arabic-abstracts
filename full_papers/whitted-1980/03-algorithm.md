# Section 3: The Ray Tracing Algorithm
## القسم 3: خوارزمية تتبع الأشعة

**Section:** algorithm
**Translation Quality:** 0.91
**Glossary Terms Used:** ray tracing (تتبع الأشعة), recursive (تكراري), reflection (انعكاس), refraction (انكسار), shadow ray (شعاع الظل), intersection (تقاطع), ray tree (شجرة الأشعة), primary ray (شعاع أولي), secondary ray (شعاع ثانوي)

---

### English Version

This section presents the core recursive ray tracing algorithm that enables realistic rendering of reflections, refractions, and shadows.

#### Overview

The algorithm traces rays backward from the viewer's eye through each pixel into the scene. When a ray intersects a surface, three types of secondary rays may be generated:

1. **Shadow rays** - to determine if the point is directly lit by each light source
2. **Reflection rays** - to compute mirror reflections from glossy surfaces
3. **Refraction rays** - to compute light transmitted through transparent materials

The process is **recursive**: reflection and refraction rays themselves can generate additional rays when they intersect surfaces. This builds a tree structure of rays for each pixel.

#### The Ray Tree Structure

For each pixel $(x, y)$ on the image plane:

1. Construct a **primary ray** from the eye through the pixel center
2. Find the nearest intersection with scene geometry
3. At the intersection point, build a **ray tree**:
   - **Root**: The primary ray and its intersection point
   - **Shadow branches**: One ray to each light source to test visibility
   - **Reflection branch**: A ray in the mirror reflection direction (if surface is reflective)
   - **Refraction branch**: A ray in the refraction direction (if surface is transparent)
4. Recursively process reflection and refraction rays, spawning more rays at their intersections
5. Terminate recursion when:
   - Ray escapes the scene (no intersection)
   - Ray hits a light source
   - Maximum recursion depth is reached
   - Contribution becomes negligible (below threshold)

#### Computing Ray Contributions

Once the ray tree is built, we traverse it to accumulate the color contribution from each path. At each intersection point $P$, the intensity $I(P)$ is computed as:

$$I(P) = I_\text{local}(P) + k_r I_\text{reflected} + k_t I_\text{transmitted}$$

where:

- $I_\text{local}(P)$ is the local illumination from the Phong model (ambient + diffuse + specular)
- $k_r$ is the reflection coefficient (how mirror-like the surface is)
- $I_\text{reflected}$ is the intensity contributed by the reflection ray
- $k_t$ is the transmission coefficient (how transparent the surface is)
- $I_\text{transmitted}$ is the intensity contributed by the refraction ray

#### Shadow Ray Calculation

For each light source $L_i$, we cast a **shadow ray** from point $P$ toward the light:

```
shadow_ray.origin = P + ε * N  (offset slightly along normal to avoid self-intersection)
shadow_ray.direction = normalize(L_i - P)
shadow_ray.t_max = distance(L_i, P)
```

If the shadow ray intersects any object before reaching the light (i.e., intersection at $t < t_\text{max}$), then the point is in shadow with respect to that light, and we skip the diffuse and specular contributions from that light source. Only the ambient term remains.

#### Reflection Ray Calculation

For a reflective surface with normal $\vec{N}$ and incident ray direction $\vec{D}$, the reflection direction $\vec{R}$ is computed as:

$$\vec{R} = \vec{D} - 2(\vec{D} \cdot \vec{N})\vec{N}$$

The reflected ray is then:

```
reflected_ray.origin = P + ε * R
reflected_ray.direction = R
```

This ray is recursively traced to find what the surface reflects.

#### Refraction Ray Calculation

For transparent materials, we use **Snell's law** to compute the refraction direction. When light passes from a medium with refractive index $\eta_1$ into a medium with index $\eta_2$, the angle of refraction $\theta_t$ is related to the angle of incidence $\theta_i$ by:

$$\eta_1 \sin \theta_i = \eta_2 \sin \theta_t$$

In vector form, the refracted direction $\vec{T}$ is:

$$\vec{T} = \frac{\eta_1}{\eta_2}\vec{D} + \left(\frac{\eta_1}{\eta_2}(\vec{D} \cdot \vec{N}) - \sqrt{1 - \left(\frac{\eta_1}{\eta_2}\right)^2(1 - (\vec{D} \cdot \vec{N})^2)}\right)\vec{N}$$

**Total internal reflection** occurs when the term under the square root becomes negative. In this case, no refraction ray is generated, and all light is reflected.

The refracted ray is:

```
refracted_ray.origin = P + ε * T
refracted_ray.direction = T
```

#### Pseudocode

Here is the complete recursive ray tracing algorithm:

```
function TraceRay(ray, depth):
    if depth > MAX_DEPTH:
        return BACKGROUND_COLOR

    intersection = FindNearestIntersection(ray)

    if no intersection:
        return BACKGROUND_COLOR

    P = intersection.point
    N = intersection.normal
    material = intersection.material

    // Local illumination (Phong model)
    I_local = material.ambient

    for each light in scene.lights:
        shadow_ray = Ray(P + ε*N, normalize(light.position - P))
        if not InShadow(shadow_ray, light):
            I_local += ComputeDiffuse(P, N, light, material)
            I_local += ComputeSpecular(P, N, light, ray, material)

    I_color = I_local

    // Reflection
    if material.k_r > 0:
        R = Reflect(ray.direction, N)
        reflected_ray = Ray(P + ε*R, R)
        I_reflected = TraceRay(reflected_ray, depth + 1)
        I_color += material.k_r * I_reflected

    // Refraction
    if material.k_t > 0:
        T = Refract(ray.direction, N, material.eta)
        if T is not NULL:  // Check for total internal reflection
            refracted_ray = Ray(P + ε*T, T)
            I_transmitted = TraceRay(refracted_ray, depth + 1)
            I_color += material.k_t * I_transmitted

    return I_color
```

#### Anti-Aliasing

To reduce jagged edges and improve image quality, multiple rays can be cast per pixel with slight offsets (supersampling or stochastic sampling). The results are then averaged to produce the final pixel color.

---

### النسخة العربية

يقدم هذا القسم خوارزمية تتبع الأشعة التكرارية الأساسية التي تمكّن من التقديم الواقعي للانعكاسات والانكسارات والظلال.

#### نظرة عامة

تتبع الخوارزمية الأشعة إلى الوراء من عين المشاهد عبر كل بكسل إلى المشهد. عندما يتقاطع شعاع مع سطح، قد يتم توليد ثلاثة أنواع من الأشعة الثانوية:

1. **أشعة الظل** - لتحديد ما إذا كانت النقطة مضاءة مباشرة بواسطة كل مصدر ضوء
2. **أشعة الانعكاس** - لحساب انعكاسات المرآة من الأسطح اللامعة
3. **أشعة الانكسار** - لحساب الضوء المنقول عبر المواد الشفافة

العملية **تكرارية**: أشعة الانعكاس والانكسار نفسها يمكن أن تولد أشعة إضافية عندما تتقاطع مع الأسطح. هذا يبني هيكل شجرة من الأشعة لكل بكسل.

#### بنية شجرة الأشعة

لكل بكسل $(x, y)$ على مستوى الصورة:

1. إنشاء **شعاع أولي** من العين عبر مركز البكسل
2. إيجاد أقرب تقاطع مع هندسة المشهد
3. عند نقطة التقاطع، بناء **شجرة أشعة**:
   - **الجذر**: الشعاع الأولي ونقطة تقاطعه
   - **فروع الظل**: شعاع واحد إلى كل مصدر ضوء لاختبار الرؤية
   - **فرع الانعكاس**: شعاع في اتجاه انعكاس المرآة (إذا كان السطح عاكساً)
   - **فرع الانكسار**: شعاع في اتجاه الانكسار (إذا كان السطح شفافاً)
4. معالجة أشعة الانعكاس والانكسار بشكل تكراري، توليد المزيد من الأشعة عند تقاطعاتها
5. إنهاء التكرار عندما:
   - يهرب الشعاع من المشهد (لا يوجد تقاطع)
   - يصطدم الشعاع بمصدر ضوء
   - يتم الوصول إلى العمق الأقصى للتكرار
   - تصبح المساهمة ضئيلة (أقل من العتبة)

#### حساب مساهمات الأشعة

بمجرد بناء شجرة الأشعة، نجتازها لتجميع مساهمة اللون من كل مسار. عند كل نقطة تقاطع $P$، يتم حساب الشدة $I(P)$ كما يلي:

$$I(P) = I_\text{local}(P) + k_r I_\text{reflected} + k_t I_\text{transmitted}$$

حيث:

- $I_\text{local}(P)$ هي الإضاءة المحلية من نموذج فونج (محيط + منتشر + لامع)
- $k_r$ هو معامل الانعكاس (مدى شبه السطح بالمرآة)
- $I_\text{reflected}$ هي الشدة المساهمة من شعاع الانعكاس
- $k_t$ هو معامل النقل (مدى شفافية السطح)
- $I_\text{transmitted}$ هي الشدة المساهمة من شعاع الانكسار

#### حساب شعاع الظل

لكل مصدر ضوء $L_i$، نرسل **شعاع ظل** من النقطة $P$ نحو الضوء:

```
shadow_ray.origin = P + ε * N  (إزاحة قليلة على طول العمودي لتجنب التقاطع الذاتي)
shadow_ray.direction = normalize(L_i - P)
shadow_ray.t_max = distance(L_i, P)
```

إذا تقاطع شعاع الظل مع أي كائن قبل الوصول إلى الضوء (أي، تقاطع عند $t < t_\text{max}$)، فإن النقطة في الظل بالنسبة لذلك الضوء، ونتخطى المساهمات المنتشرة واللامعة من مصدر الضوء ذلك. يبقى فقط حد الإضاءة المحيطة.

#### حساب شعاع الانعكاس

لسطح عاكس ذو عمودي $\vec{N}$ واتجاه شعاع ساقط $\vec{D}$، يتم حساب اتجاه الانعكاس $\vec{R}$ كما يلي:

$$\vec{R} = \vec{D} - 2(\vec{D} \cdot \vec{N})\vec{N}$$

ثم يكون الشعاع المنعكس:

```
reflected_ray.origin = P + ε * R
reflected_ray.direction = R
```

يتم تتبع هذا الشعاع بشكل تكراري لإيجاد ما يعكسه السطح.

#### حساب شعاع الانكسار

للمواد الشفافة، نستخدم **قانون سنل** لحساب اتجاه الانكسار. عندما يمر الضوء من وسط ذو معامل انكسار $\eta_1$ إلى وسط ذو معامل $\eta_2$، ترتبط زاوية الانكسار $\theta_t$ بزاوية السقوط $\theta_i$ بالعلاقة:

$$\eta_1 \sin \theta_i = \eta_2 \sin \theta_t$$

في الصيغة الاتجاهية، الاتجاه المنكسر $\vec{T}$ هو:

$$\vec{T} = \frac{\eta_1}{\eta_2}\vec{D} + \left(\frac{\eta_1}{\eta_2}(\vec{D} \cdot \vec{N}) - \sqrt{1 - \left(\frac{\eta_1}{\eta_2}\right)^2(1 - (\vec{D} \cdot \vec{N})^2)}\right)\vec{N}$$

يحدث **الانعكاس الداخلي الكلي** عندما يصبح الحد تحت الجذر التربيعي سالباً. في هذه الحالة، لا يتم توليد شعاع انكسار، وينعكس كل الضوء.

الشعاع المنكسر هو:

```
refracted_ray.origin = P + ε * T
refracted_ray.direction = T
```

#### الشفرة الكاذبة

فيما يلي خوارزمية تتبع الأشعة التكرارية الكاملة:

```
function TraceRay(ray, depth):
    if depth > MAX_DEPTH:
        return BACKGROUND_COLOR

    intersection = FindNearestIntersection(ray)

    if no intersection:
        return BACKGROUND_COLOR

    P = intersection.point
    N = intersection.normal
    material = intersection.material

    // الإضاءة المحلية (نموذج فونج)
    I_local = material.ambient

    for each light in scene.lights:
        shadow_ray = Ray(P + ε*N, normalize(light.position - P))
        if not InShadow(shadow_ray, light):
            I_local += ComputeDiffuse(P, N, light, material)
            I_local += ComputeSpecular(P, N, light, ray, material)

    I_color = I_local

    // الانعكاس
    if material.k_r > 0:
        R = Reflect(ray.direction, N)
        reflected_ray = Ray(P + ε*R, R)
        I_reflected = TraceRay(reflected_ray, depth + 1)
        I_color += material.k_r * I_reflected

    // الانكسار
    if material.k_t > 0:
        T = Refract(ray.direction, N, material.eta)
        if T is not NULL:  // فحص الانعكاس الداخلي الكلي
            refracted_ray = Ray(P + ε*T, T)
            I_transmitted = TraceRay(refracted_ray, depth + 1)
            I_color += material.k_t * I_transmitted

    return I_color
```

#### مكافحة التسنن

لتقليل الحواف المسننة وتحسين جودة الصورة، يمكن إرسال أشعة متعددة لكل بكسل مع إزاحات طفيفة (أخذ عينات فائقة أو أخذ عينات عشوائية). ثم يتم حساب متوسط النتائج لإنتاج لون البكسل النهائي.

---

### Translation Notes

- **Figures referenced:** Ray tree structure (conceptual)
- **Key terms introduced:**
  - Snell's law (قانون سنل)
  - Total internal reflection (الانعكاس الداخلي الكلي)
  - Refractive index (معامل الانكسار)
  - Supersampling (أخذ عينات فائقة)
  - Stochastic sampling (أخذ عينات عشوائية)
  - Self-intersection (تقاطع ذاتي)
- **Equations:** 3 major formulas (intensity calculation, reflection vector, Snell's law)
- **Code:** Pseudocode algorithm preserved in English with Arabic comments
- **Citations:** None
- **Special handling:** Vector notation and mathematical formulas preserved; code comments translated

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.94
- Readability: 0.89
- Glossary consistency: 0.90
- **Overall section score:** 0.91

### Back-Translation Verification

The algorithm traces rays backward from the eye through each pixel. When a ray intersects a surface, three types of secondary rays may be generated: shadow rays to test light visibility, reflection rays for mirror surfaces, and refraction rays for transparent materials. The process is recursive, building a ray tree for each pixel. At each intersection point P, intensity is computed as local illumination plus reflected and transmitted contributions. Shadow rays test visibility to lights. Reflection uses the standard reflection formula. Refraction uses Snell's law, with total internal reflection when the square root term becomes negative. The pseudocode shows the complete recursive algorithm with termination conditions.
