# Section 5: Results and Discussion
## القسم 5: النتائج والنقاش

**Section:** results
**Translation Quality:** 0.86
**Glossary Terms Used:** rendering (التقديم), shading (تظليل), specular highlight (إبراز لامع), polygon (مضلع), visual quality (جودة بصرية)

---

### English Version

The shading techniques described in this paper have been implemented and tested on various three-dimensional objects. This section presents the results and compares the visual quality achieved by different shading methods.

#### Implementation and Test Objects

The shading algorithms were implemented on a computer graphics system with a display resolution of 512 × 512 pixels. Several test objects were rendered, including:

1. **Spheres** - to test the handling of curved surfaces approximated by polygons
2. **Teapots** - complex surfaces with both convex and concave regions
3. **Torus** - to demonstrate handling of self-occlusion and varying curvature
4. **Geometric solids** - cubes, cylinders, and cones with different material properties

Each object was rendered using three different shading techniques for comparison:
- Constant shading (flat shading)
- Intensity interpolation (Gouraud shading)
- Normal vector interpolation (Phong shading)

#### Visual Quality Comparison

**Constant Shading Results:**

Objects rendered with constant shading display a distinct faceted appearance. Each polygon face is clearly visible as a separate flat region with uniform intensity. This creates an artificial appearance, particularly noticeable on curved surfaces like spheres. The polygon edges create visible discontinuities in the shading, destroying the illusion of a smooth surface. Specular highlights, when present, are confined to entire polygon faces rather than appearing as localized bright spots.

**Gouraud Shading Results:**

Gouraud shading produces a significant improvement over constant shading. The intensity interpolation successfully hides polygon edges, creating the appearance of smooth surfaces. For diffuse objects (matte surfaces) without strong specular highlights, Gouraud shading produces visually acceptable results at reasonable computational cost.

However, limitations become apparent with specular surfaces. Specular highlights may appear distorted, elongated, or faceted. In some cases, highlights are missed entirely when the peak intensity falls in the interior of a large polygon away from vertices. The highlight shape and position depend on the polygon tessellation, which is undesirable.

**Phong Shading Results:**

Normal vector interpolation (Phong shading) produces noticeably superior results, especially for surfaces with specular reflection. The key improvements include:

1. **Accurate Specular Highlights:** Highlights appear as smooth, circular (or elliptical) bright regions with correct position and size. The highlight shape is independent of polygon tessellation.

2. **Smooth Surface Appearance:** Even with relatively coarse polygon meshes, the surface appears smooth and continuous. The illusion of a curved surface is maintained.

3. **Material Realism:** Different material properties (controlled by $k_a$, $k_d$, $k_s$, and $n$ parameters) are rendered accurately. Metallic surfaces show small, sharp highlights; plastic surfaces show larger, softer highlights.

4. **Reduced Polygon Count:** Because Phong shading produces smooth results even with fewer polygons, objects can be modeled with coarser meshes while maintaining visual quality. This can offset the increased per-pixel computational cost.

#### Computational Performance

The computational cost comparison for a typical scene (measured in relative time units):

- **Constant shading:** 1.0× (baseline)
- **Gouraud shading:** 1.2× (20% overhead)
- **Phong shading:** 2.5× to 3.0× (150-200% overhead)

The additional cost of Phong shading comes from:
1. Per-pixel normal interpolation and normalization
2. Per-pixel illumination model evaluation (including dot products and exponentiation)

However, this overhead must be considered in context:
- For high-quality rendering, the improved visual results often justify the cost
- Hardware acceleration or optimized implementations can reduce the overhead
- The ability to use coarser polygon meshes with Phong shading can reduce overall scene complexity

#### Parameter Selection

The illumination model parameters significantly affect the rendered appearance:

**Ambient coefficient ($k_a$):** Controls overall brightness and visibility of unlit regions. Values typically range from 0.1 to 0.3. Too high values wash out the image; too low values make shadowed regions completely black.

**Diffuse coefficient ($k_d$):** Controls the matte appearance. High values (0.5-0.8) create matte surfaces; low values create surfaces that appear darker or more metallic. For colored objects, $k_d$ often varies by color channel to produce the object's color.

**Specular coefficient ($k_s$):** Controls highlight brightness. Values range from 0.0 (no highlights) to 1.0 (mirror-like). Metallic surfaces typically use high values (0.7-1.0), while matte surfaces use low values (0.0-0.2).

**Shininess exponent ($n$):** Controls highlight size and sharpness. Values range from 1 to 200 or higher:
- $n$ = 1-5: Very broad, soft highlights (rough plastic, matte finish)
- $n$ = 10-50: Moderate highlights (smooth plastic, ceramic)
- $n$ = 100-200: Sharp, small highlights (polished metal, glass)

Realistic rendering requires careful selection of these parameters to match real material properties. Through experimentation, standard parameter sets have been developed for common materials (wood, metal, plastic, etc.).

#### Limitations and Future Work

While Phong shading represents a significant improvement, several limitations remain:

1. **Local Illumination Only:** The model does not account for shadows, reflections between objects, or global illumination effects. Objects appear to float in space without casting shadows.

2. **Point Light Sources:** Only point sources are modeled. Extended light sources (area lights) would require integration over the light source, significantly increasing computational cost.

3. **Simple Material Model:** Real materials exhibit more complex behavior (anisotropic reflection, subsurface scattering, texture). The three-component model is a simplification.

4. **Normalization Cost:** The need to normalize interpolated normals adds computational overhead. Approximate normalization methods could be investigated.

Future improvements could address these limitations through ray tracing (for shadows and reflections), radiosity methods (for global illumination), and more sophisticated material models. However, even with these limitations, Phong shading provides a practical balance between visual quality and computational efficiency for real-time and near-real-time rendering applications.

---

### النسخة العربية

تم تنفيذ واختبار تقنيات التظليل الموصوفة في هذا البحث على أجسام ثلاثية الأبعاد مختلفة. يقدم هذا القسم النتائج ويقارن الجودة البصرية التي تحققها طرق التظليل المختلفة.

#### التنفيذ والأجسام الاختبارية

تم تنفيذ خوارزميات التظليل على نظام رسومات حاسوب بدقة عرض 512 × 512 بكسل. تم تقديم عدة أجسام اختبارية، بما في ذلك:

1. **الكرات** - لاختبار معالجة الأسطح المنحنية المُقَرَّبة بالمضلعات
2. **إبريق الشاي** - أسطح معقدة ذات مناطق محدبة ومقعرة
3. **الطارة** - لإظهار معالجة الانسداد الذاتي والانحناء المتغير
4. **الأجسام الهندسية** - مكعبات، أسطوانات، ومخاريط بخصائص مواد مختلفة

تم تقديم كل جسم باستخدام ثلاث تقنيات تظليل مختلفة للمقارنة:
- التظليل الثابت (التظليل المسطح)
- استيفاء الشدة (تظليل جورو)
- استيفاء متجه الناظم (تظليل فونج)

#### مقارنة الجودة البصرية

**نتائج التظليل الثابت:**

تُظهر الأجسام المُقَدَّمة بالتظليل الثابت مظهراً مُوَجَّهاً واضحاً. كل وجه مضلع مرئي بوضوح كمنطقة مسطحة منفصلة بشدة موحدة. هذا يخلق مظهراً اصطناعياً، ملحوظاً بشكل خاص على الأسطح المنحنية مثل الكرات. تخلق حواف المضلعات عدم استمرارية مرئية في التظليل، مدمرة وهم السطح الناعم. الإبرازات اللامعة، عند وجودها، محصورة في وجوه مضلعة كاملة بدلاً من الظهور كبقع ساطعة موضعية.

**نتائج تظليل جورو:**

ينتج تظليل جورو تحسناً كبيراً على التظليل الثابت. يخفي استيفاء الشدة بنجاح حواف المضلعات، خالقاً مظهر الأسطح الناعمة. بالنسبة للأجسام المنتشرة (الأسطح غير اللامعة) بدون إبرازات لامعة قوية، ينتج تظليل جورو نتائج مقبولة بصرياً بتكلفة حسابية معقولة.

ومع ذلك، تصبح القيود واضحة مع الأسطح اللامعة. قد تظهر الإبرازات اللامعة مشوهة أو ممدودة أو مُوَجَّهة. في بعض الحالات، تُفقد الإبرازات تماماً عندما تسقط الشدة القصوى في داخل مضلع كبير بعيداً عن الرؤوس. يعتمد شكل وموضع الإبراز على تفليج المضلع، وهو أمر غير مرغوب فيه.

**نتائج تظليل فونج:**

ينتج استيفاء متجه الناظم (تظليل فونج) نتائج متفوقة بشكل ملحوظ، خاصة للأسطح ذات الانعكاس اللامع. تشمل التحسينات الرئيسية:

1. **إبرازات لامعة دقيقة:** تظهر الإبرازات كمناطق ساطعة دائرية (أو بيضاوية) ناعمة بالموضع والحجم الصحيحين. شكل الإبراز مستقل عن تفليج المضلع.

2. **مظهر سطح ناعم:** حتى مع شبكات مضلعات خشنة نسبياً، يظهر السطح ناعماً ومستمراً. يُحافظ على وهم السطح المنحني.

3. **واقعية المادة:** تُقدَّم خصائص المواد المختلفة (المتحكم فيها بمعاملات $k_a$، $k_d$، $k_s$، و $n$) بدقة. تُظهر الأسطح المعدنية إبرازات صغيرة حادة؛ تُظهر الأسطح البلاستيكية إبرازات أكبر وأنعم.

4. **عدد مضلعات مُخَفَّض:** لأن تظليل فونج ينتج نتائج ناعمة حتى مع عدد أقل من المضلعات، يمكن نمذجة الأجسام بشبكات أخشن مع الحفاظ على الجودة البصرية. هذا يمكن أن يعوض التكلفة الحسابية المتزايدة لكل بكسل.

#### الأداء الحسابي

مقارنة التكلفة الحسابية لمشهد نموذجي (مقاسة بوحدات زمنية نسبية):

- **التظليل الثابت:** 1.0× (خط الأساس)
- **تظليل جورو:** 1.2× (زيادة 20%)
- **تظليل فونج:** 2.5× إلى 3.0× (زيادة 150-200%)

تأتي التكلفة الإضافية لتظليل فونج من:
1. استيفاء وتطبيع الناظم لكل بكسل
2. تقييم نموذج الإضاءة لكل بكسل (بما في ذلك الضربات النقطية والأُسِّيَّة)

ومع ذلك، يجب النظر في هذه الزيادة في السياق:
- للتقديم عالي الجودة، غالباً ما تبرر النتائج البصرية المحسنة التكلفة
- يمكن أن يقلل تسريع الأجهزة أو التنفيذات المحسنة من الزيادة
- القدرة على استخدام شبكات مضلعات أخشن مع تظليل فونج يمكن أن تقلل التعقيد الإجمالي للمشهد

#### اختيار المعاملات

تؤثر معاملات نموذج الإضاءة بشكل كبير على المظهر المُقدَّم:

**معامل المحيط ($k_a$):** يتحكم في السطوع العام ورؤية المناطق غير المضاءة. تتراوح القيم عادةً من 0.1 إلى 0.3. القيم المرتفعة جداً تغسل الصورة؛ القيم المنخفضة جداً تجعل المناطق المظللة سوداء تماماً.

**معامل الانتشار ($k_d$):** يتحكم في المظهر غير اللامع. القيم المرتفعة (0.5-0.8) تخلق أسطحاً غير لامعة؛ القيم المنخفضة تخلق أسطحاً تبدو أغمق أو أكثر معدنية. بالنسبة للأجسام الملونة، غالباً ما يختلف $k_d$ حسب القناة اللونية لإنتاج لون الجسم.

**معامل اللمعان ($k_s$):** يتحكم في سطوع الإبراز. تتراوح القيم من 0.0 (بدون إبرازات) إلى 1.0 (مثل المرآة). تستخدم الأسطح المعدنية عادةً قيماً عالية (0.7-1.0)، بينما تستخدم الأسطح غير اللامعة قيماً منخفضة (0.0-0.2).

**أس اللمعان ($n$):** يتحكم في حجم وحدة الإبراز. تتراوح القيم من 1 إلى 200 أو أعلى:
- $n$ = 1-5: إبرازات واسعة جداً، ناعمة (بلاستيك خشن، لمسة نهائية غير لامعة)
- $n$ = 10-50: إبرازات معتدلة (بلاستيك ناعم، سيراميك)
- $n$ = 100-200: إبرازات حادة، صغيرة (معدن مصقول، زجاج)

يتطلب التقديم الواقعي اختياراً دقيقاً لهذه المعاملات لمطابقة خصائص المواد الحقيقية. من خلال التجربة، تم تطوير مجموعات معاملات قياسية للمواد الشائعة (الخشب، المعدن، البلاستيك، إلخ).

#### القيود والعمل المستقبلي

بينما يمثل تظليل فونج تحسناً كبيراً، تبقى عدة قيود:

1. **الإضاءة المحلية فقط:** لا يأخذ النموذج في الاعتبار الظلال، أو الانعكاسات بين الأجسام، أو تأثيرات الإضاءة العالمية. تبدو الأجسام وكأنها تطفو في الفضاء دون إلقاء ظلال.

2. **مصادر ضوء نقطية:** يتم نمذجة المصادر النقطية فقط. ستتطلب مصادر الضوء الممتدة (أضواء المساحة) تكاملاً على مصدر الضوء، مما يزيد بشكل كبير التكلفة الحسابية.

3. **نموذج مادة بسيط:** تُظهر المواد الحقيقية سلوكاً أكثر تعقيداً (انعكاس لامتماثل، تشتت تحت السطح، ملمس). نموذج المكونات الثلاثة هو تبسيط.

4. **تكلفة التطبيع:** الحاجة لتطبيع النواظم المستوفاة يضيف عبئاً حسابياً. يمكن التحقيق في طرق التطبيع التقريبية.

يمكن للتحسينات المستقبلية معالجة هذه القيود من خلال تتبع الأشعة (للظلال والانعكاسات)، وطرق الإشعاعية (للإضاءة العالمية)، ونماذج مواد أكثر تطوراً. ومع ذلك، حتى مع هذه القيود، يوفر تظليل فونج توازناً عملياً بين الجودة البصرية والكفاءة الحسابية لتطبيقات التقديم في الزمن الحقيقي والقريب من الزمن الحقيقي.

---

### Translation Notes

- **Figures referenced:** Implicit references to rendered images comparing shading methods
- **Key terms introduced:**
  - test object (جسم اختباري)
  - teapot (إبريق الشاي)
  - torus (طارة)
  - tessellation (تفليج)
  - polygon mesh (شبكة مضلعات)
  - coarse mesh (شبكة خشنة)
  - hardware acceleration (تسريع الأجهزة)
  - global illumination (إضاءة عالمية)
  - ray tracing (تتبع الأشعة)
  - radiosity (إشعاعية)
  - anisotropic reflection (انعكاس لامتماثل)
  - subsurface scattering (تشتت تحت السطح)
- **Equations:** References to earlier equations with parameters
- **Performance data:** Relative computational costs included
- **Citations:** None specific in this section
- **Special handling:** Material parameter ranges carefully translated with Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
