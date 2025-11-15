# Section 4: Implementation
## القسم 4: التنفيذ

**Section:** implementation
**Translation Quality:** 0.86
**Glossary Terms Used:** algorithm (خوارزمية), data structure (بنية البيانات), intersection (تقاطع), anti-aliasing (إزالة التعرج), rendering (التقديم), computational cost (تكلفة حسابية)

---

### English Version

## Ray-Object Intersection

The computational core of the ray tracing algorithm is testing whether a ray intersects an object and, if so, finding the intersection point and surface normal. The ray is defined parametrically as:

$$\mathbf{P}(t) = \mathbf{O} + t\mathbf{D}$$

where $\mathbf{O}$ is the ray origin, $\mathbf{D}$ is the ray direction (normalized), and $t$ is the parameter along the ray.

### Sphere Intersection

For a sphere with center $\mathbf{C}$ and radius $r$, the intersection is found by solving:

$$||\mathbf{P}(t) - \mathbf{C}||^2 = r^2$$

This yields a quadratic equation in $t$:

$$(\mathbf{D} \cdot \mathbf{D})t^2 + 2\mathbf{D} \cdot (\mathbf{O} - \mathbf{C})t + ||\mathbf{O} - \mathbf{C}||^2 - r^2 = 0$$

The discriminant determines whether the ray hits the sphere (positive discriminant), is tangent (zero), or misses (negative). The smallest positive $t$ value gives the nearest intersection.

### Polygon Intersection

For planar polygons, the process involves:

1. **Plane intersection:** Find where the ray intersects the plane containing the polygon
2. **Inside test:** Determine if the intersection point lies inside the polygon boundary

The plane is defined by a point $\mathbf{P}_0$ on the plane and normal $\mathbf{N}$. The intersection parameter is:

$$t = \frac{(\mathbf{P}_0 - \mathbf{O}) \cdot \mathbf{N}}{\mathbf{D} \cdot \mathbf{N}}$$

If $\mathbf{D} \cdot \mathbf{N} = 0$, the ray is parallel to the plane.

## Data Structures for Efficiency

Naive ray tracing tests every ray against every object in the scene, giving $O(n)$ complexity per ray where $n$ is the number of objects. For complex scenes, this becomes prohibitively expensive.

**Bounding Volumes:** Objects are enclosed in simple bounding shapes (typically spheres or boxes). A ray is tested against the bounding volume first; only if it hits the bounding volume is the more expensive exact intersection test performed.

**Spatial Subdivision:** The scene is divided into a regular grid or hierarchical spatial structure (octree, BSP tree). Rays traverse this structure, only testing objects in the cells the ray passes through. This reduces average complexity significantly.

## Anti-Aliasing

A single ray per pixel produces aliased images with jagged edges. To achieve smooth edges, multiple rays are cast per pixel and their results averaged. This is called supersampling or distributed ray tracing.

**Adaptive Supersampling:** Rather than using a fixed number of samples per pixel, adaptive methods detect edges by comparing adjacent pixels. More samples are taken in high-contrast regions, while uniform regions use fewer samples.

For the images in this paper, a simple $4 \times 4$ supersampling pattern was used, casting 16 rays per pixel arranged in a regular grid within the pixel area.

## Termination and Recursion Depth

Each reflection or refraction spawns a new ray, potentially leading to infinite recursion. Practical implementations limit recursion depth to a fixed maximum (typically 5-10 levels).

Additionally, the contribution of each recursive level is attenuated by the reflection coefficient $k_s$ or transmission coefficient $k_t$. When the accumulated attenuation falls below a threshold (e.g., 0.01), further recursion is terminated as it contributes negligibly to the final pixel value.

## Performance Considerations

**Computational Cost:** Ray tracing is computationally expensive. For the test images (512×512 pixels with 16 samples per pixel), rendering time was several hours on the hardware available in 1980.

**Coherence:** Unlike scanline rendering algorithms that exploit coherence between adjacent pixels, ray tracing treats each pixel independently. This makes parallelization straightforward but eliminates traditional coherence optimizations.

**Intersection Optimization:** Most rendering time is spent computing ray-object intersections. Efficient data structures and culling techniques are essential for practical performance.

## Material Properties

Each surface in the scene is assigned material properties:

- $k_a$: Ambient reflection coefficient
- $k_d$: Diffuse reflection coefficient
- $k_s$: Specular reflection coefficient
- $k_t$: Transmission coefficient
- $n$: Specular exponent (shininess)
- $\eta$: Index of refraction (for transparent materials)

These properties control how the surface interacts with light. For example:
- A mirror has high $k_s$ and low $k_d$ and $k_t$
- Matte surfaces have high $k_d$ and low $k_s$ and $k_t$
- Glass has both significant $k_s$ and $k_t$

## Algorithm Summary

The complete ray tracing algorithm can be summarized as:

```
function TraceRay(ray, depth):
    if depth > MAX_DEPTH:
        return background_color

    intersection = FindNearestIntersection(ray, scene)

    if no intersection:
        return background_color

    point = intersection.point
    normal = intersection.normal
    material = intersection.material

    color = material.ka * ambient_light

    for each light in lights:
        shadow_ray = Ray(point, direction_to_light)
        if not InShadow(shadow_ray, light):
            color += PhongShading(point, normal, light, material)

    if material.ks > threshold:
        reflect_dir = ReflectDirection(ray.direction, normal)
        reflect_ray = Ray(point, reflect_dir)
        color += material.ks * TraceRay(reflect_ray, depth + 1)

    if material.kt > threshold:
        refract_dir = RefractDirection(ray.direction, normal, material.eta)
        if refract_dir exists:
            refract_ray = Ray(point, refract_dir)
            color += material.kt * TraceRay(refract_ray, depth + 1)

    return color
```

This recursive structure elegantly captures the global illumination effects while building on the familiar Phong shading model.

---

### النسخة العربية

## تقاطع الشعاع مع الأجسام

النواة الحسابية لخوارزمية تتبع الأشعة هي اختبار ما إذا كان الشعاع يتقاطع مع جسم، وإذا كان الأمر كذلك، إيجاد نقطة التقاطع والعمودي على السطح. يُعرّف الشعاع بارامترياً على النحو التالي:

$$\mathbf{P}(t) = \mathbf{O} + t\mathbf{D}$$

حيث $\mathbf{O}$ هو أصل الشعاع، و $\mathbf{D}$ هو اتجاه الشعاع (مُطبّع)، و $t$ هو البارامتر على طول الشعاع.

### تقاطع الكرة

بالنسبة لكرة مركزها $\mathbf{C}$ ونصف قطرها $r$، يتم إيجاد التقاطع من خلال حل:

$$||\mathbf{P}(t) - \mathbf{C}||^2 = r^2$$

ينتج عن هذا معادلة تربيعية في $t$:

$$(\mathbf{D} \cdot \mathbf{D})t^2 + 2\mathbf{D} \cdot (\mathbf{O} - \mathbf{C})t + ||\mathbf{O} - \mathbf{C}||^2 - r^2 = 0$$

يحدد المميز ما إذا كان الشعاع يصيب الكرة (مميز موجب)، أو مماس (صفر)، أو يخطئها (سالب). تعطي أصغر قيمة موجبة لـ $t$ أقرب تقاطع.

### تقاطع المضلع

بالنسبة للمضلعات المستوية، تتضمن العملية:

1. **تقاطع المستوى:** ابحث عن مكان تقاطع الشعاع مع المستوى الذي يحتوي على المضلع
2. **اختبار الداخل:** حدد ما إذا كانت نقطة التقاطع تقع داخل حدود المضلع

يُعرّف المستوى بنقطة $\mathbf{P}_0$ على المستوى وعمودي $\mathbf{N}$. بارامتر التقاطع هو:

$$t = \frac{(\mathbf{P}_0 - \mathbf{O}) \cdot \mathbf{N}}{\mathbf{D} \cdot \mathbf{N}}$$

إذا كان $\mathbf{D} \cdot \mathbf{N} = 0$، فإن الشعاع موازٍ للمستوى.

## بنى البيانات من أجل الكفاءة

يختبر تتبع الأشعة الساذج كل شعاع مقابل كل جسم في المشهد، مما يعطي تعقيداً $O(n)$ لكل شعاع حيث $n$ هو عدد الأجسام. بالنسبة للمشاهد المعقدة، يصبح هذا مكلفاً بشكل باهظ.

**الأحجام المحيطة:** تُحاط الأجسام بأشكال محيطة بسيطة (عادةً كرات أو صناديق). يتم اختبار الشعاع مقابل الحجم المحيط أولاً؛ فقط إذا أصاب الحجم المحيط يتم إجراء اختبار التقاطع الدقيق الأكثر تكلفة.

**التقسيم المكاني:** يُقسم المشهد إلى شبكة منتظمة أو بنية مكانية هرمية (شجرة ثمانية، شجرة BSP). تجتاز الأشعة هذه البنية، تختبر فقط الأجسام في الخلايا التي يمر بها الشعاع. هذا يقلل من التعقيد المتوسط بشكل كبير.

## إزالة التعرج

ينتج شعاع واحد لكل بكسل صوراً بها تعرج مع حواف خشنة. لتحقيق حواف ناعمة، يتم إطلاق أشعة متعددة لكل بكسل ويتم حساب متوسط نتائجها. يُسمى هذا أخذ العينات الفائق أو تتبع الأشعة الموزع.

**أخذ العينات الفائق التكيفي:** بدلاً من استخدام عدد ثابت من العينات لكل بكسل، تكتشف الطرق التكيفية الحواف من خلال مقارنة البكسلات المجاورة. يتم أخذ المزيد من العينات في المناطق عالية التباين، بينما تستخدم المناطق المنتظمة عينات أقل.

بالنسبة للصور في هذه الورقة، تم استخدام نمط أخذ عينات فائق بسيط $4 \times 4$، بإطلاق 16 شعاعاً لكل بكسل مرتبة في شبكة منتظمة داخل منطقة البكسل.

## الإنهاء وعمق العودية

ينتج كل انعكاس أو انكسار شعاعاً جديداً، مما قد يؤدي إلى عودية لانهائية. تحد التنفيذات العملية من عمق العودية إلى حد أقصى ثابت (عادةً 5-10 مستويات).

بالإضافة إلى ذلك، تُضعَّف مساهمة كل مستوى عودي بواسطة معامل الانعكاس $k_s$ أو معامل النقل $k_t$. عندما يقل التضعيف المتراكم عن عتبة (على سبيل المثال، 0.01)، يتم إنهاء المزيد من العودية حيث تساهم بشكل ضئيل في قيمة البكسل النهائية.

## اعتبارات الأداء

**التكلفة الحسابية:** تتبع الأشعة مكلف حسابياً. بالنسبة لصور الاختبار (512×512 بكسل مع 16 عينة لكل بكسل)، كان وقت التقديم عدة ساعات على الأجهزة المتاحة في عام 1980.

**التماسك:** على عكس خوارزميات التقديم بخط المسح التي تستغل التماسك بين البكسلات المجاورة، يتعامل تتبع الأشعة مع كل بكسل بشكل مستقل. هذا يجعل التوازي مباشراً لكنه يزيل تحسينات التماسك التقليدية.

**تحسين التقاطع:** يُنفق معظم وقت التقديم في حساب تقاطعات الشعاع-الجسم. بنى البيانات الفعالة وتقنيات الاستبعاد ضرورية للأداء العملي.

## خصائص المواد

يتم تعيين خصائص مادة لكل سطح في المشهد:

- $k_a$: معامل الانعكاس المحيط
- $k_d$: معامل الانعكاس المنتشر
- $k_s$: معامل الانعكاس اللامع
- $k_t$: معامل النقل
- $n$: الأس اللامع (درجة اللمعان)
- $\eta$: معامل الانكسار (للمواد الشفافة)

تتحكم هذه الخصائص في كيفية تفاعل السطح مع الضوء. على سبيل المثال:
- تحتوي المرآة على $k_s$ عالٍ و $k_d$ و $k_t$ منخفضين
- تحتوي الأسطح غير اللامعة على $k_d$ عالٍ و $k_s$ و $k_t$ منخفضين
- يحتوي الزجاج على كل من $k_s$ و $k_t$ كبيرين

## ملخص الخوارزمية

يمكن تلخيص خوارزمية تتبع الأشعة الكاملة على النحو التالي:

```
function TraceRay(ray, depth):
    if depth > MAX_DEPTH:
        return background_color

    intersection = FindNearestIntersection(ray, scene)

    if no intersection:
        return background_color

    point = intersection.point
    normal = intersection.normal
    material = intersection.material

    color = material.ka * ambient_light

    for each light in lights:
        shadow_ray = Ray(point, direction_to_light)
        if not InShadow(shadow_ray, light):
            color += PhongShading(point, normal, light, material)

    if material.ks > threshold:
        reflect_dir = ReflectDirection(ray.direction, normal)
        reflect_ray = Ray(point, reflect_dir)
        color += material.ks * TraceRay(reflect_ray, depth + 1)

    if material.kt > threshold:
        refract_dir = RefractDirection(ray.direction, normal, material.eta)
        if refract_dir exists:
            refract_ray = Ray(point, refract_dir)
            color += material.kt * TraceRay(refract_ray, depth + 1)

    return color
```

تلتقط هذه البنية العودية بشكل أنيق تأثيرات الإضاءة الشاملة مع البناء على نموذج تظليل فونغ المألوف.

---

### Translation Notes

- **Figures referenced:** None explicitly, but would reference ray-sphere intersection diagrams
- **Key terms introduced:**
  - Ray-object intersection (تقاطع الشعاع مع الأجسام)
  - Parametric ray (شعاع بارامتري)
  - Quadratic equation (معادلة تربيعية)
  - Discriminant (مميز)
  - Bounding volume (حجم محيط)
  - Spatial subdivision (تقسيم مكاني)
  - Octree (شجرة ثمانية)
  - BSP tree (شجرة BSP)
  - Supersampling (أخذ العينات الفائق)
  - Adaptive supersampling (أخذ العينات الفائق التكيفي)
  - Attenuation (تضعيف)
  - Scanline rendering (التقديم بخط المسح)
- **Equations:** 3 main equations (parametric ray, sphere intersection, plane intersection)
- **Citations:** None in this section
- **Special handling:** Pseudocode kept in English as per convention; mathematical formulations preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.86
