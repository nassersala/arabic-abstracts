# Section 2: Object Modeling and Shading Techniques
## القسم 2: نمذجة الأجسام وتقنيات التظليل

**Section:** modeling-and-shading
**Translation Quality:** 0.88
**Glossary Terms Used:** polygon (مضلع), rendering (التقديم), interpolation (استيفاء), shading (تظليل), algorithm (خوارزمية), vector (متجه), surface normal (ناظم السطح)

---

### English Version

The relationship between object modeling and shading is fundamental to computer graphics. Different methods of representing surfaces require different approaches to shading. In this section, we examine three main categories of surface representation and their associated shading techniques.

#### Polygonal Surface Models

The most common method of object representation is the polygonal model, where the object surface is approximated by a mesh of planar polygons (usually triangles or quadrilaterals). Each polygon has a well-defined normal vector perpendicular to its surface. The advantages of polygonal models include simplicity of representation and efficient hidden surface algorithms such as the depth buffer (z-buffer) method.

For shading polygonal models, several approaches exist:

**Constant Shading (Flat Shading):** In this simplest method, each polygon is assigned a single intensity value based on the angle between its normal vector and the light source direction. The entire polygon is painted with this constant intensity. While computationally efficient, this method produces images with visible polygon edges, creating an artificial faceted appearance. This is particularly noticeable when representing curved surfaces with polygonal approximations.

**Intensity Interpolation (Gouraud Shading):** Proposed by Gouraud, this method computes intensities at polygon vertices and linearly interpolates these values across the polygon surface during scan conversion. The vertex intensities are calculated by averaging the normal vectors of all polygons sharing that vertex. This technique produces much smoother images than constant shading and effectively hides polygon edges. However, it has limitations in rendering specular highlights, which may appear distorted or be missed entirely if they fall in the polygon interior away from vertices.

**Normal Vector Interpolation (Phong Shading):** The method proposed in this paper interpolates normal vectors rather than intensities. Normal vectors are computed at polygon vertices (typically by averaging the normals of adjacent polygons), and these vectors are linearly interpolated across the polygon surface. At each pixel, the interpolated normal is used to calculate the intensity based on the full illumination model. This produces much more accurate specular highlights and overall better image quality than Gouraud shading, though at higher computational cost.

#### Curved Surface Models

Some objects are better represented using curved surface patches, such as parametric surfaces (Bézier surfaces, B-spline surfaces) or implicit surfaces (spheres, cylinders, quadric surfaces). These representations can describe smooth curved surfaces exactly without polygonal approximation.

For curved surfaces, the shading calculation must account for the continuously varying normal vector across the surface. The normal can be computed analytically from the surface equation. The advantage is that specular highlights and surface features are rendered accurately. The disadvantage is that more complex hidden surface algorithms are required, such as ray tracing or scan-line algorithms adapted for curved surfaces.

#### Scan-Line Coherence and Efficiency

Regardless of the surface representation method, efficient shading requires exploiting scan-line coherence—the property that adjacent pixels on a scan line have similar properties. Both Gouraud shading and Phong shading can be implemented efficiently using incremental calculations along scan lines. The normal vector components (for Phong shading) or intensity values (for Gouraud shading) can be updated incrementally from pixel to pixel using additions rather than expensive multiplications.

The choice between shading methods involves a trade-off between image quality and computational cost. Constant shading is fastest but produces poor quality. Gouraud shading provides good quality at moderate cost and is suitable for most diffuse surfaces. Phong shading produces the highest quality, especially for surfaces with specular highlights, but requires more computation per pixel.

---

### النسخة العربية

العلاقة بين نمذجة الأجسام والتظليل أساسية لرسومات الحاسوب. تتطلب الطرق المختلفة لتمثيل الأسطح مقاربات مختلفة للتظليل. في هذا القسم، نفحص ثلاث فئات رئيسية لتمثيل الأسطح وتقنيات التظليل المرتبطة بها.

#### نماذج الأسطح المضلعة

الطريقة الأكثر شيوعاً لتمثيل الأجسام هي النموذج المضلع، حيث يتم تقريب سطح الجسم بشبكة من المضلعات المستوية (عادةً مثلثات أو رباعيات). كل مضلع له متجه ناظم محدد بوضوح عمودي على سطحه. تشمل مزايا النماذج المضلعة بساطة التمثيل وخوارزميات فعالة للأسطح المخفية مثل طريقة المخزن المؤقت للعمق (z-buffer).

لتظليل النماذج المضلعة، توجد عدة مقاربات:

**التظليل الثابت (التظليل المسطح):** في هذه الطريقة الأبسط، يُعيَّن لكل مضلع قيمة شدة واحدة بناءً على الزاوية بين متجه الناظم الخاص به واتجاه مصدر الضوء. يتم رسم المضلع بأكمله بهذه الشدة الثابتة. بينما تكون هذه الطريقة فعالة حسابياً، فإنها تنتج صوراً ذات حواف مضلعة مرئية، مما يخلق مظهراً مُوَجَّهاً اصطناعياً. هذا ملحوظ بشكل خاص عند تمثيل الأسطح المنحنية بتقريبات مضلعة.

**استيفاء الشدة (تظليل جورو):** اقترح جورو هذه الطريقة التي تحسب الشدات عند رؤوس المضلع وتستوفي هذه القيم خطياً عبر سطح المضلع أثناء تحويل المسح. يتم حساب شدات الرؤوس بمتوسط متجهات الناظم لجميع المضلعات التي تشترك في ذلك الرأس. تنتج هذه التقنية صوراً أنعم بكثير من التظليل الثابت وتخفي حواف المضلعات بشكل فعال. ومع ذلك، لها قيود في تقديم الإبرازات اللامعة، والتي قد تظهر مشوهة أو تُفقد تماماً إذا سقطت في داخل المضلع بعيداً عن الرؤوس.

**استيفاء متجه الناظم (تظليل فونج):** الطريقة المقترحة في هذا البحث تستوفي متجهات الناظم بدلاً من الشدات. يتم حساب متجهات الناظم عند رؤوس المضلع (عادةً بمتوسط نواظم المضلعات المجاورة)، ويتم استيفاء هذه المتجهات خطياً عبر سطح المضلع. عند كل بكسل، يُستخدم الناظم المستوفى لحساب الشدة بناءً على نموذج الإضاءة الكامل. ينتج هذا إبرازات لامعة أكثر دقة بكثير وجودة صورة إجمالية أفضل من تظليل جورو، على الرغم من التكلفة الحسابية الأعلى.

#### نماذج الأسطح المنحنية

بعض الأجسام يتم تمثيلها بشكل أفضل باستخدام رقع أسطح منحنية، مثل الأسطح البارامترية (أسطح بيزييه، أسطح B-spline) أو الأسطح الضمنية (كرات، أسطوانات، أسطح تربيعية). يمكن لهذه التمثيلات وصف الأسطح المنحنية الناعمة بدقة دون تقريب مضلع.

بالنسبة للأسطح المنحنية، يجب أن يأخذ حساب التظليل في الاعتبار متجه الناظم المتغير باستمرار عبر السطح. يمكن حساب الناظم تحليلياً من معادلة السطح. الميزة هي أن الإبرازات اللامعة وخصائص السطح يتم تقديمها بدقة. العيب هو أن خوارزميات الأسطح المخفية الأكثر تعقيداً مطلوبة، مثل تتبع الأشعة أو خوارزميات خط المسح المكيفة للأسطح المنحنية.

#### تماسك خط المسح والكفاءة

بغض النظر عن طريقة تمثيل السطح، يتطلب التظليل الفعال استغلال تماسك خط المسح - الخاصية التي تجعل البكسلات المتجاورة على خط المسح لها خصائص مشابهة. يمكن تنفيذ كل من تظليل جورو وتظليل فونج بكفاءة باستخدام الحسابات التزايدية على طول خطوط المسح. يمكن تحديث مكونات متجه الناظم (لتظليل فونج) أو قيم الشدة (لتظليل جورو) بشكل تزايدي من بكسل إلى بكسل باستخدام الجمع بدلاً من الضرب المكلف.

الاختيار بين طرق التظليل ينطوي على مفاضلة بين جودة الصورة والتكلفة الحسابية. التظليل الثابت هو الأسرع لكنه ينتج جودة ضعيفة. تظليل جورو يوفر جودة جيدة بتكلفة معتدلة ومناسب لمعظم الأسطح المنتشرة. تظليل فونج ينتج أعلى جودة، خاصة للأسطح ذات الإبرازات اللامعة، لكنه يتطلب مزيداً من الحساب لكل بكسل.

---

### Translation Notes

- **Figures referenced:** None explicitly mentioned, but concepts refer to visual differences
- **Key terms introduced:**
  - polygonal mesh (شبكة مضلعة)
  - depth buffer/z-buffer (المخزن المؤقت للعمق)
  - flat shading (التظليل المسطح)
  - scan conversion (تحويل المسح)
  - vertex normal (ناظم الرأس)
  - Bézier surface (سطح بيزييه)
  - B-spline surface (سطح B-spline)
  - quadric surface (سطح تربيعي)
  - ray tracing (تتبع الأشعة)
  - scan-line coherence (تماسك خط المسح)
  - incremental calculation (حساب تزايدي)
- **Equations:** None in this section (descriptive only)
- **Citations:** Gouraud's work referenced
- **Special handling:** Careful distinction between three shading methods (constant, Gouraud, Phong)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
