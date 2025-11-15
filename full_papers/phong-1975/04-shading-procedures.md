# Section 4: Shading Procedures
## القسم 4: إجراءات التظليل

**Section:** shading-procedures
**Translation Quality:** 0.87
**Glossary Terms Used:** interpolation (استيفاء), scan line (خط المسح), polygon (مضلع), vertex (رأس), normal vector (متجه الناظم), algorithm (خوارزمية)

---

### English Version

This section describes the practical implementation of the normal vector interpolation shading method (Phong shading). The goal is to efficiently compute shaded intensities for all pixels on visible polygon surfaces during scan-line rendering.

#### Computing Vertex Normals

The first step is to compute normal vectors at polygon vertices. For a mesh of polygons approximating a smooth surface, the vertex normal is typically computed as the average of the normals of all polygons sharing that vertex:

$$\mathbf{N}_v = \frac{\sum_{j=1}^{p} \mathbf{N}_j}{|\sum_{j=1}^{p} \mathbf{N}_j|}$$

where $\mathbf{N}_v$ is the normalized vertex normal, $\mathbf{N}_j$ are the face normals of the $p$ polygons meeting at the vertex, and the denominator normalizes the result to unit length.

For objects with sharp edges or corners (like cubes), vertices along the edge should not average normals from faces on different sides of the edge. This preserves the intended sharp visual discontinuity.

#### Scan-Line Algorithm Overview

The shading procedure operates within a scan-line hidden surface removal algorithm. For each scan line:

1. Determine which polygon edges intersect the scan line
2. For each polygon span on the scan line (between left and right edges):
   - Interpolate normal vectors across the span
   - For each pixel in the span:
     - Calculate intensity using the interpolated normal and the illumination model
     - Display the pixel

#### Normal Vector Interpolation

Consider a polygon with vertices $V_1, V_2, V_3$ having normal vectors $\mathbf{N}_1, \mathbf{N}_2, \mathbf{N}_3$. For a point $P$ on the polygon surface, we need to compute an interpolated normal $\mathbf{N}_P$.

**Two-Stage Interpolation:**

The interpolation is performed in two stages using the scan-line coherence property:

**Stage 1 - Edge Interpolation:** As we scan vertically down the polygon, at each scan line we compute normals at the polygon edges. For an edge between vertices $V_i$ and $V_j$, the normal at a point on the edge is:

$$\mathbf{N}_{edge} = \mathbf{N}_i + t(\mathbf{N}_j - \mathbf{N}_i)$$

where $t$ is the parametric distance along the edge (0 ≤ $t$ ≤ 1).

This can be computed incrementally: if $\Delta y$ is the vertical step between scan lines and $\Delta y_{ij}$ is the total vertical distance from $V_i$ to $V_j$, then:

$$\mathbf{N}_{edge}^{next} = \mathbf{N}_{edge}^{current} + \frac{\mathbf{N}_j - \mathbf{N}_i}{\Delta y_{ij}} \Delta y$$

**Stage 2 - Span Interpolation:** Along a scan line between left edge normal $\mathbf{N}_L$ and right edge normal $\mathbf{N}_R$, the normal at pixel position $x$ is:

$$\mathbf{N}(x) = \mathbf{N}_L + s(\mathbf{N}_R - \mathbf{N}_L)$$

where $s$ is the fractional distance across the span (0 ≤ $s$ ≤ 1).

Again, this can be computed incrementally:

$$\mathbf{N}(x+1) = \mathbf{N}(x) + \frac{\mathbf{N}_R - \mathbf{N}_L}{\Delta x}$$

where $\Delta x$ is the horizontal span width.

#### Intensity Calculation

At each pixel position, once the interpolated normal $\mathbf{N}$ is known, the intensity is calculated using the full illumination model:

$$I = k_a I_{a,light} + k_d I_{light} (\mathbf{N} \cdot \mathbf{L}) + k_s I_{light} (\mathbf{R} \cdot \mathbf{V})^n$$

The reflection vector $\mathbf{R}$ must be recomputed for each pixel since it depends on the interpolated normal:

$$\mathbf{R} = 2(\mathbf{N} \cdot \mathbf{L})\mathbf{N} - \mathbf{L}$$

**Optimization Considerations:**

1. **Vector Normalization:** The interpolated normals should be normalized to unit length before use in intensity calculations. However, normalization is expensive. For small polygons with similar vertex normals, the error from using unnormalized interpolated normals may be acceptable.

2. **Dot Product Calculations:** The dot products $\mathbf{N} \cdot \mathbf{L}$ and $\mathbf{R} \cdot \mathbf{V}$ require 3 multiplications and 2 additions each.

3. **Exponentiation:** Computing $(\mathbf{R} \cdot \mathbf{V})^n$ is expensive. This can be optimized using table lookup for common exponent values.

4. **Incremental Computation:** All interpolations use addition rather than multiplication, exploiting scan-line coherence for efficiency.

#### Comparison with Gouraud Shading

**Gouraud Shading** interpolates intensity values rather than normals:
- **Advantages:** Faster (intensity computed only at vertices)
- **Disadvantages:** Specular highlights incorrectly rendered, can miss highlights entirely

**Phong Shading** interpolates normal vectors:
- **Advantages:** Accurate specular highlights, better overall quality
- **Disadvantages:** More computation per pixel (must evaluate illumination equation at each pixel)

The quality improvement of Phong shading is most noticeable for surfaces with specular highlights. For purely diffuse surfaces, Gouraud shading may be sufficient.

#### Implementation Pseudo-code

```
For each scan line y:
    For each polygon span on this scan line:
        // Get normals at left and right edges
        N_left = interpolate_edge_normal(left_edge, y)
        N_right = interpolate_edge_normal(right_edge, y)

        // Set up incremental normal computation
        delta_N = (N_right - N_left) / span_width
        N_current = N_left

        For each pixel x in span:
            // Normalize the interpolated normal
            N_normalized = normalize(N_current)

            // Compute intensity using illumination model
            I = compute_intensity(N_normalized, L, V, material_params)

            // Display pixel
            set_pixel(x, y, I)

            // Increment normal for next pixel
            N_current = N_current + delta_N
```

This algorithm integrates smoothly with scan-line hidden surface algorithms, processing each scan line once and computing shading on-the-fly for visible surfaces.

---

### النسخة العربية

يصف هذا القسم التنفيذ العملي لطريقة تظليل استيفاء متجه الناظم (تظليل فونج). الهدف هو حساب شدات التظليل بكفاءة لجميع البكسلات على أسطح المضلعات المرئية أثناء التقديم بخط المسح.

#### حساب نواظم الرؤوس

الخطوة الأولى هي حساب متجهات الناظم عند رؤوس المضلع. بالنسبة لشبكة من المضلعات تقرّب سطحاً ناعماً، يتم حساب ناظم الرأس عادةً كمتوسط نواظم جميع المضلعات التي تشترك في ذلك الرأس:

$$\mathbf{N}_v = \frac{\sum_{j=1}^{p} \mathbf{N}_j}{|\sum_{j=1}^{p} \mathbf{N}_j|}$$

حيث $\mathbf{N}_v$ هو ناظم الرأس المُطَبَّع، $\mathbf{N}_j$ هي نواظم الوجوه للمضلعات $p$ التي تلتقي عند الرأس، والمقام يُطَبِّع النتيجة إلى طول وحدوي.

بالنسبة للأجسام ذات الحواف أو الزوايا الحادة (مثل المكعبات)، يجب ألا تتوسط الرؤوس على طول الحافة النواظم من الوجوه على جوانب مختلفة من الحافة. هذا يحافظ على عدم الاستمرارية البصرية الحادة المقصودة.

#### نظرة عامة على خوارزمية خط المسح

يعمل إجراء التظليل ضمن خوارزمية إزالة السطح المخفي بخط المسح. لكل خط مسح:

1. تحديد حواف المضلع التي تتقاطع مع خط المسح
2. لكل امتداد مضلع على خط المسح (بين الحافتين اليسرى واليمنى):
   - استيفاء متجهات الناظم عبر الامتداد
   - لكل بكسل في الامتداد:
     - حساب الشدة باستخدام الناظم المستوفى ونموذج الإضاءة
     - عرض البكسل

#### استيفاء متجه الناظم

لننظر في مضلع برؤوس $V_1، V_2، V_3$ لها متجهات ناظم $\mathbf{N}_1، \mathbf{N}_2، \mathbf{N}_3$. لنقطة $P$ على سطح المضلع، نحتاج إلى حساب ناظم مستوفى $\mathbf{N}_P$.

**استيفاء ثنائي المرحلة:**

يتم إجراء الاستيفاء على مرحلتين باستخدام خاصية تماسك خط المسح:

**المرحلة 1 - استيفاء الحافة:** بينما نمسح عمودياً لأسفل المضلع، عند كل خط مسح نحسب النواظم عند حواف المضلع. لحافة بين رأسين $V_i$ و $V_j$، الناظم عند نقطة على الحافة هو:

$$\mathbf{N}_{edge} = \mathbf{N}_i + t(\mathbf{N}_j - \mathbf{N}_i)$$

حيث $t$ هي المسافة البارامترية على طول الحافة (0 ≤ $t$ ≤ 1).

يمكن حساب هذا تزايدياً: إذا كان $\Delta y$ هو الخطوة العمودية بين خطوط المسح و $\Delta y_{ij}$ هي المسافة العمودية الكلية من $V_i$ إلى $V_j$، إذن:

$$\mathbf{N}_{edge}^{next} = \mathbf{N}_{edge}^{current} + \frac{\mathbf{N}_j - \mathbf{N}_i}{\Delta y_{ij}} \Delta y$$

**المرحلة 2 - استيفاء الامتداد:** على طول خط مسح بين ناظم الحافة اليسرى $\mathbf{N}_L$ وناظم الحافة اليمنى $\mathbf{N}_R$، الناظم عند موضع البكسل $x$ هو:

$$\mathbf{N}(x) = \mathbf{N}_L + s(\mathbf{N}_R - \mathbf{N}_L)$$

حيث $s$ هي المسافة الكسرية عبر الامتداد (0 ≤ $s$ ≤ 1).

مرة أخرى، يمكن حساب هذا تزايدياً:

$$\mathbf{N}(x+1) = \mathbf{N}(x) + \frac{\mathbf{N}_R - \mathbf{N}_L}{\Delta x}$$

حيث $\Delta x$ هو عرض الامتداد الأفقي.

#### حساب الشدة

عند كل موضع بكسل، بمجرد معرفة الناظم المستوفى $\mathbf{N}$، يتم حساب الشدة باستخدام نموذج الإضاءة الكامل:

$$I = k_a I_{a,light} + k_d I_{light} (\mathbf{N} \cdot \mathbf{L}) + k_s I_{light} (\mathbf{R} \cdot \mathbf{V})^n$$

يجب إعادة حساب متجه الانعكاس $\mathbf{R}$ لكل بكسل لأنه يعتمد على الناظم المستوفى:

$$\mathbf{R} = 2(\mathbf{N} \cdot \mathbf{L})\mathbf{N} - \mathbf{L}$$

**اعتبارات التحسين:**

1. **تطبيع المتجه:** يجب تطبيع النواظم المستوفاة إلى طول وحدوي قبل الاستخدام في حسابات الشدة. ومع ذلك، التطبيع مكلف. بالنسبة للمضلعات الصغيرة ذات نواظم الرؤوس المتشابهة، قد يكون الخطأ من استخدام النواظم المستوفاة غير المطبَّعة مقبولاً.

2. **حسابات الضرب النقطي:** تتطلب الضربات النقطية $\mathbf{N} \cdot \mathbf{L}$ و $\mathbf{R} \cdot \mathbf{V}$ 3 عمليات ضرب وعمليتي جمع لكل منهما.

3. **الأُسِّيَّة:** حساب $(\mathbf{R} \cdot \mathbf{V})^n$ مكلف. يمكن تحسين هذا باستخدام البحث في جدول لقيم الأس الشائعة.

4. **الحساب التزايدي:** جميع الاستيفاءات تستخدم الجمع بدلاً من الضرب، مستغلة تماسك خط المسح للكفاءة.

#### المقارنة مع تظليل جورو

**تظليل جورو** يستوفي قيم الشدة بدلاً من النواظم:
- **المزايا:** أسرع (يتم حساب الشدة فقط عند الرؤوس)
- **العيوب:** الإبرازات اللامعة تُقدَّم بشكل غير صحيح، يمكن أن تفقد الإبرازات تماماً

**تظليل فونج** يستوفي متجهات الناظم:
- **المزايا:** إبرازات لامعة دقيقة، جودة إجمالية أفضل
- **العيوب:** مزيد من الحساب لكل بكسل (يجب تقييم معادلة الإضاءة عند كل بكسل)

تحسين الجودة من تظليل فونج ملحوظ بشكل أكبر للأسطح ذات الإبرازات اللامعة. بالنسبة للأسطح المنتشرة بحتة، قد يكون تظليل جورو كافياً.

#### كود شبه برمجي للتنفيذ

```
لكل خط مسح y:
    لكل امتداد مضلع على هذا الخط:
        // الحصول على النواظم عند الحافتين اليسرى واليمنى
        N_left = interpolate_edge_normal(left_edge, y)
        N_right = interpolate_edge_normal(right_edge, y)

        // إعداد الحساب التزايدي للناظم
        delta_N = (N_right - N_left) / span_width
        N_current = N_left

        لكل بكسل x في الامتداد:
            // تطبيع الناظم المستوفى
            N_normalized = normalize(N_current)

            // حساب الشدة باستخدام نموذج الإضاءة
            I = compute_intensity(N_normalized, L, V, material_params)

            // عرض البكسل
            set_pixel(x, y, I)

            // زيادة الناظم للبكسل التالي
            N_current = N_current + delta_N
```

تتكامل هذه الخوارزمية بسلاسة مع خوارزميات السطح المخفي بخط المسح، معالجة كل خط مسح مرة واحدة وحساب التظليل أثناء التنقل للأسطح المرئية.

---

### Translation Notes

- **Figures referenced:** None explicitly, but algorithmic flow described
- **Key terms introduced:**
  - vertex normal (ناظم الرأس)
  - face normal (ناظم الوجه)
  - edge interpolation (استيفاء الحافة)
  - span interpolation (استيفاء الامتداد)
  - parametric distance (مسافة بارامترية)
  - incremental computation (حساب تزايدي)
  - normalization (تطبيع)
  - exponentiation (أُسِّيَّة)
  - table lookup (بحث في جدول)
  - pseudo-code (كود شبه برمجي)
- **Equations:** 7 equations showing interpolation formulas
- **Code:** Pseudo-code included (kept in English with Arabic comments in description)
- **Citations:** Reference to Gouraud's method
- **Special handling:** Mathematical incremental formulas carefully translated

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
