# Section 3: Interpolated Shading
## القسم 3: التظليل بالاستيفاء

**Section:** interpolated-shading
**Translation Quality:** 0.89
**Glossary Terms Used:** interpolation (استيفاء), Gouraud shading (تظليل جورو), Phong shading (تظليل فونج), vertex (رأس), scan line (خط مسح)

---

### English Version

To overcome the limitations of flat shading, several interpolation techniques have been developed. These methods compute intensities at certain points and then interpolate to obtain smooth intensity variations across polygon surfaces.

#### Gouraud Shading (Intensity Interpolation)

The first widely-used interpolation technique was developed by Gouraud [1971]. **Gouraud shading**, also known as **intensity interpolation shading**, works as follows:

1. **Compute vertex normals**: For each vertex shared by multiple polygons, compute an average normal vector from the normals of the adjacent polygons
2. **Compute vertex intensities**: Use the illumination model to calculate intensity values at each polygon vertex using the vertex normals
3. **Interpolate along edges**: Linearly interpolate intensities along each polygon edge between vertices
4. **Interpolate along scan lines**: For each scan line crossing the polygon, linearly interpolate intensities between the edge intersection points

The intensity at an interior point $(x, y)$ within a polygon is thus obtained through bilinear interpolation.

**Advantages of Gouraud shading:**
- Eliminates intensity discontinuities at polygon boundaries
- Produces smooth-looking curved surfaces from polygon meshes
- Computationally efficient (only additions required during scan conversion)
- Works well for diffuse surfaces

**Limitations of Gouraud shading:**
- **Specular highlights are poorly rendered**: Since intensities are interpolated linearly, specular highlights that should appear in the middle of a polygon may be lost or distorted if none of the vertices are brightly lit
- **Orientation dependence**: The appearance can change depending on how the polygon is positioned relative to the scan lines
- **Mach bands**: Though reduced compared to flat shading, subtle intensity discontinuities can still occur at silhouette edges

#### Phong Shading (Normal Vector Interpolation)

We propose an alternative approach called **Phong shading** or **normal vector interpolation shading**:

1. **Compute vertex normals**: Same as Gouraud shading - average the normals of adjacent polygons at each vertex
2. **Interpolate normals**: Instead of interpolating intensities, linearly interpolate the normal vectors across the polygon surface
3. **Normalize interpolated normals**: At each pixel, normalize the interpolated normal to unit length
4. **Compute pixel intensity**: Apply the full illumination model at each pixel using the interpolated normal vector

The key difference is that Phong shading applies the illumination calculation (including specular terms) at every pixel rather than only at vertices.

**Algorithm:**
- For edge interpolation: $\vec{N}_{edge}(t) = (1-t)\vec{N}_1 + t\vec{N}_2$ where $t \in [0,1]$
- For scan line interpolation: $\vec{N}_{pixel}(s) = (1-s)\vec{N}_{left} + s\vec{N}_{right}$ where $s \in [0,1]$
- Normalize: $\vec{N}_{unit} = \vec{N}_{pixel} / |\vec{N}_{pixel}|$
- Apply illumination model using $\vec{N}_{unit}$

**Advantages of Phong shading over Gouraud shading:**
- **Accurate specular highlights**: Specular reflections are properly rendered even when they occur in the interior of polygons
- **Better quality**: More faithful to the underlying lighting physics
- **View-dependent effects**: Properly handles view-dependent specular reflections
- **Reduced artifacts**: Fewer Mach bands and orientation dependencies

**Computational cost:**
Phong shading requires:
- Normal vector interpolation and normalization at each pixel
- Full illumination model evaluation (including potentially expensive specular term calculation) at each pixel
- Approximately 2-3 times more computation than Gouraud shading

However, the visual improvement is substantial, especially for surfaces with specular reflections. The technique produces images that appear much more realistic, with proper highlights on curved shiny surfaces.

#### Comparison Summary

| Aspect | Flat Shading | Gouraud Shading | Phong Shading |
|--------|-------------|-----------------|---------------|
| Computation per polygon | Once | Once per vertex + interpolation | Interpolation + illumination per pixel |
| Smooth surfaces | No | Yes | Yes |
| Specular highlights | No | Poor | Excellent |
| Computational cost | Lowest | Medium | Highest |
| Visual quality | Faceted | Smooth diffuse | Realistic with highlights |

The choice of shading method depends on the application requirements. For real-time applications where speed is critical, Gouraud shading may be preferred. For high-quality rendering where realism is paramount, Phong shading produces superior results.

---

### النسخة العربية

للتغلب على قيود التظليل المسطح، تم تطوير عدة تقنيات استيفاء. تحسب هذه الطرق الشدات عند نقاط معينة ثم تستوفيها للحصول على تغيرات شدة سلسة عبر أسطح المضلعات.

#### تظليل جورو (استيفاء الشدة)

تم تطوير أول تقنية استيفاء مستخدمة على نطاق واسع بواسطة جورو [1971]. يعمل **تظليل جورو**، المعروف أيضاً باسم **تظليل استيفاء الشدة**، على النحو التالي:

1. **حساب نواظم الرؤوس**: لكل رأس مشترك بين عدة مضلعات، احسب متجه ناظم متوسط من نواظم المضلعات المجاورة
2. **حساب شدات الرؤوس**: استخدم نموذج الإضاءة لحساب قيم الشدة عند كل رأس مضلع باستخدام نواظم الرؤوس
3. **الاستيفاء على طول الحواف**: استوفِ الشدات خطياً على طول كل حافة مضلع بين الرؤوس
4. **الاستيفاء على طول خطوط المسح**: لكل خط مسح يعبر المضلع، استوفِ الشدات خطياً بين نقاط تقاطع الحواف

يتم الحصول على الشدة عند نقطة داخلية $(x, y)$ داخل مضلع من خلال الاستيفاء ثنائي الخطية.

**مزايا تظليل جورو:**
- يزيل انقطاعات الشدة عند حدود المضلعات
- ينتج أسطحاً منحنية ذات مظهر سلس من شبكات المضلعات
- فعال حسابياً (فقط عمليات جمع مطلوبة أثناء تحويل المسح)
- يعمل بشكل جيد للأسطح المنتشرة

**قيود تظليل جورو:**
- **يتم تقديم نقاط التمييز المرآوية بشكل ضعيف**: نظراً لأن الشدات مستوفاة خطياً، فإن نقاط التمييز المرآوية التي يجب أن تظهر في منتصف المضلع قد تُفقد أو تُشوه إذا لم يكن أي من الرؤوس مضاءً بشكل ساطع
- **الاعتماد على الاتجاه**: يمكن أن يتغير المظهر اعتماداً على كيفية وضع المضلع بالنسبة لخطوط المسح
- **نطاقات ماخ**: على الرغم من التقليل مقارنة بالتظليل المسطح، لا يزال من الممكن حدوث انقطاعات شدة دقيقة عند حواف الصورة الظلية

#### تظليل فونج (استيفاء متجه الناظم)

نقترح نهجاً بديلاً يسمى **تظليل فونج** أو **تظليل استيفاء متجه الناظم**:

1. **حساب نواظم الرؤوس**: نفس تظليل جورو - متوسط نواظم المضلعات المجاورة عند كل رأس
2. **استيفاء النواظم**: بدلاً من استيفاء الشدات، استوفِ متجهات الناظم خطياً عبر سطح المضلع
3. **تطبيع النواظم المستوفاة**: عند كل بكسل، طبّع الناظم المستوفى إلى طول وحدوي
4. **حساب شدة البكسل**: طبق نموذج الإضاءة الكامل عند كل بكسل باستخدام متجه الناظم المستوفى

الفرق الرئيسي هو أن تظليل فونج يطبق حساب الإضاءة (بما في ذلك المصطلحات المرآوية) عند كل بكسل بدلاً من الرؤوس فقط.

**الخوارزمية:**
- لاستيفاء الحافة: $\vec{N}_{edge}(t) = (1-t)\vec{N}_1 + t\vec{N}_2$ حيث $t \in [0,1]$
- لاستيفاء خط المسح: $\vec{N}_{pixel}(s) = (1-s)\vec{N}_{left} + s\vec{N}_{right}$ حيث $s \in [0,1]$
- التطبيع: $\vec{N}_{unit} = \vec{N}_{pixel} / |\vec{N}_{pixel}|$
- تطبيق نموذج الإضاءة باستخدام $\vec{N}_{unit}$

**مزايا تظليل فونج على تظليل جورو:**
- **نقاط تمييز مرآوية دقيقة**: يتم تقديم الانعكاسات المرآوية بشكل صحيح حتى عندما تحدث في داخل المضلعات
- **جودة أفضل**: أكثر وفاءً للفيزياء الأساسية للإضاءة
- **تأثيرات تعتمد على الرؤية**: يتعامل بشكل صحيح مع الانعكاسات المرآوية التي تعتمد على الرؤية
- **تقليل العيوب**: نطاقات ماخ أقل واعتماد أقل على الاتجاه

**التكلفة الحسابية:**
يتطلب تظليل فونج:
- استيفاء وتطبيع متجه الناظم عند كل بكسل
- تقييم نموذج الإضاءة الكامل (بما في ذلك حساب المصطلح المرآوي المكلف محتملاً) عند كل بكسل
- حوالي 2-3 أضعاف الحساب مقارنة بتظليل جورو

ومع ذلك، فإن التحسن البصري كبير، خاصة للأسطح ذات الانعكاسات المرآوية. تنتج هذه التقنية صوراً تبدو أكثر واقعية، مع نقاط تمييز صحيحة على الأسطح المنحنية اللامعة.

#### ملخص المقارنة

| الجانب | التظليل المسطح | تظليل جورو | تظليل فونج |
|--------|-------------|-----------------|---------------|
| الحساب لكل مضلع | مرة واحدة | مرة لكل رأس + استيفاء | استيفاء + إضاءة لكل بكسل |
| أسطح ملساء | لا | نعم | نعم |
| نقاط تمييز مرآوية | لا | ضعيف | ممتاز |
| التكلفة الحسابية | الأدنى | متوسط | الأعلى |
| الجودة البصرية | مضلعي | منتشر سلس | واقعي مع نقاط تمييز |

يعتمد اختيار طريقة التظليل على متطلبات التطبيق. بالنسبة للتطبيقات في الوقت الفعلي حيث السرعة حاسمة، قد يُفضل تظليل جورو. للتقديم عالي الجودة حيث الواقعية هي الأهم، ينتج تظليل فونج نتائج أفضل.

---

### Translation Notes

- **Figures referenced:** Comparison table summarizing three shading methods
- **Key terms introduced:**
  - Gouraud shading (تظليل جورو)
  - Phong shading (تظليل فونج)
  - intensity interpolation (استيفاء الشدة)
  - normal vector interpolation (استيفاء متجه الناظم)
  - vertex normal (ناظم الرأس)
  - scan line (خط المسح)
  - bilinear interpolation (استيفاء ثنائي الخطية)
  - silhouette edge (حافة الصورة الظلية)
  - view-dependent (يعتمد على الرؤية)
- **Equations:** 3 equations for normal interpolation
- **Citations:** Reference to Gouraud [1971]
- **Special handling:** Detailed algorithmic descriptions, comparison table

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89

### Back-Translation (Validation)

To overcome limitations of flat shading, several interpolation techniques were developed that compute intensities at certain points and interpolate for smooth variations across polygon surfaces.

Gouraud shading (intensity interpolation shading) works by: (1) computing vertex normals by averaging normals of adjacent polygons, (2) computing vertex intensities using the illumination model, (3) linearly interpolating intensities along edges, (4) interpolating along scan lines. Advantages include eliminating intensity discontinuities and producing smooth surfaces efficiently. Limitations include poorly rendered specular highlights, orientation dependence, and subtle Mach bands.

Phong shading (normal vector interpolation shading) instead interpolates normal vectors across the polygon surface, normalizes them, and applies the full illumination model at each pixel. This produces accurate specular highlights and better visual quality at 2-3x computational cost compared to Gouraud shading.

The choice depends on application requirements: Gouraud for real-time speed, Phong for high-quality realistic rendering.
