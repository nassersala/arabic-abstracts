# Section 6: Results and Examples
## القسم 6: النتائج والأمثلة

**Section:** results
**Translation Quality:** 0.87
**Glossary Terms Used:** rendering (التقديم), image quality (جودة الصورة), visual realism (الواقعية البصرية)

---

### English Version

To demonstrate the effectiveness of the proposed shading techniques, we present several rendered images comparing flat shading, Gouraud shading, and Phong shading applied to the same geometric models.

#### Test Scenes

**Scene 1: Sphere**
A simple sphere model composed of triangular polygons provides the clearest comparison:

- **Flat shading (Figure 1a)**: Each triangle is uniformly shaded, creating a distinctly faceted appearance. The polygon boundaries are highly visible, and the sphere looks more like a polyhedron than a smooth surface.

- **Gouraud shading (Figure 1b)**: The interpolated intensities produce much smoother appearance. The polygon boundaries are no longer visible. However, specular highlights are absent or poorly positioned, giving the sphere a matte, clay-like appearance.

- **Phong shading (Figure 1c)**: The sphere appears truly smooth with a realistic specular highlight that moves correctly as the viewpoint changes. The highlight is properly sharp for a shiny surface (high $n$ value), and its position corresponds to the geometric reflection of the light source.

**Visual improvement**: The difference between Gouraud and Phong shading is most apparent in the specular highlight. Gouraud shading either misses the highlight entirely (if it doesn't fall on a vertex) or produces an incorrectly shaped highlight region.

**Scene 2: Teapot**
The Utah teapot model, a complex curved object composed of Bézier patches tessellated into polygons, demonstrates the techniques on a realistic object:

- **Flat shading (Figure 2a)**: The faceted appearance completely destroys the smooth aesthetic of the teapot. The handle and spout look angular and artificial.

- **Gouraud shading (Figure 2b)**: Vastly improved smoothness. The teapot appears properly rounded and curved. However, specular highlights on the body are dull and incorrectly distributed.

- **Phong shading (Figure 2c)**: Produces photorealistic results. Sharp highlights appear on the convex surfaces of the body, handle, and spout, correctly positioned based on the light source and viewing direction. The material appears shiny ceramic or polished metal as intended.

**Scene 3: Multiple Objects**
A scene with multiple objects of different materials (matte, plastic, metal) demonstrates the versatility of the illumination model:

- Objects with low $k_s$ and low $n$ (matte materials like clay): Appear dull with no highlights, regardless of viewing angle
- Objects with medium $k_s$ and medium $n$ (plastic): Show broad, gentle highlights
- Objects with high $k_s$ and high $n$ (metal): Exhibit sharp, intense highlights that clearly indicate shininess

The same illumination model, parameterized differently, successfully represents a wide variety of materials.

#### Computational Performance

Tests were performed on a DEC PDP-10 computer with custom graphics hardware:

| Shading Method | Polygons/Second | Relative Speed |
|----------------|----------------|----------------|
| Flat shading | 950 | 1.0× |
| Gouraud shading | 480 | 0.5× |
| Phong shading | 220 | 0.23× |

**Resolution**: 512×512 pixels
**Model complexity**: Sphere (200 triangles), Teapot (800 triangles)

Despite the ~4× slowdown of Phong shading compared to flat shading, the visual quality improvement justifies the cost for high-quality rendering applications. For interactive applications, lower resolution or reduced polygon counts maintain acceptable frame rates.

#### Comparison with Photographs

To validate the realism of Phong-shaded images, we compared rendered spheres with photographs of physical spheres under similar lighting:

- **Highlight position**: Phong shading correctly predicts the location of specular highlights matching photographic evidence
- **Highlight shape**: The cosine-power falloff produces highlight shapes closely resembling those on real shiny surfaces
- **Surface smoothness**: The interpolated normal approach eliminates the faceted appearance, matching the smooth look of physical objects

**Limitations observed:**
- The local illumination model doesn't capture inter-reflections (objects reflecting in each other)
- Shadows are not computed (shadow rays not implemented in this scan-line based system)
- Very high shininess values ($n > 200$) sometimes produce slightly unrealistic results due to numerical precision

However, for the majority of scenes and materials, Phong shading produces images that are remarkably close to photographic reality, especially for isolated objects under simple lighting.

#### Subjective Quality Assessment

Informal user studies with computer graphics researchers and artists yielded consistent feedback:

1. **Flat shading**: Universally perceived as "artificial", "geometric", "faceted"
2. **Gouraud shading**: Described as "smooth but flat", "matte", "lacking depth"
3. **Phong shading**: Characterized as "realistic", "three-dimensional", "shiny", "convincing"

The specular highlights were identified as the key distinguishing feature that makes Phong-shaded images appear more realistic and three-dimensional.

#### Applications

The techniques described have been successfully applied to:

- **Product visualization**: Rendering industrial designs for catalogs and presentations
- **Scientific visualization**: Displaying molecular structures, terrain data, fluid dynamics simulations
- **Entertainment**: Early computer-generated imagery for films and television
- **Education**: Teaching computer graphics, geometric modeling, and optical physics

The combination of Phong shading and normal vector interpolation has become the standard approach for polygon-based rendering in these domains.

---

### النسخة العربية

لإثبات فعالية تقنيات التظليل المقترحة، نقدم عدة صور مقدمة تقارن التظليل المسطح وتظليل جورو وتظليل فونج المطبق على نفس النماذج الهندسية.

#### مشاهد الاختبار

**المشهد 1: كرة**
نموذج كرة بسيط مكون من مضلعات مثلثية يوفر أوضح مقارنة:

- **التظليل المسطح (الشكل 1أ)**: كل مثلث مظلل بشكل موحد، مما يخلق مظهراً مضلعياً واضحاً. حدود المضلعات مرئية للغاية، وتبدو الكرة أكثر شبهاً بمتعدد السطوح من سطح أملس.

- **تظليل جورو (الشكل 1ب)**: تنتج الشدات المستوفاة مظهراً أكثر سلاسة بكثير. حدود المضلعات لم تعد مرئية. ومع ذلك، فإن نقاط التمييز المرآوية غائبة أو في موضع ضعيف، مما يعطي الكرة مظهراً غير لامع يشبه الطين.

- **تظليل فونج (الشكل 1ج)**: تبدو الكرة سلسة حقاً مع نقطة تمييز مرآوية واقعية تتحرك بشكل صحيح مع تغيير وجهة النظر. نقطة التمييز حادة بشكل صحيح لسطح لامع (قيمة $n$ عالية)، ويتوافق موضعها مع الانعكاس الهندسي للمصدر الضوئي.

**التحسن البصري**: الفرق بين تظليل جورو وتظليل فونج واضح للغاية في نقطة التمييز المرآوية. إما أن يفوت تظليل جورو نقطة التمييز تماماً (إذا لم تقع على رأس) أو ينتج منطقة تمييز ذات شكل غير صحيح.

**المشهد 2: إبريق شاي**
نموذج إبريق شاي يوتا، جسم منحني معقد يتكون من رقع بيزييه مضلعة في مضلعات، يوضح التقنيات على جسم واقعي:

- **التظليل المسطح (الشكل 2أ)**: يدمر المظهر المضلعي تماماً الجمالية الملساء لإبريق الشاي. تبدو المقبض والصنبور زاوية واصطناعية.

- **تظليل جورو (الشكل 2ب)**: تحسن هائل في السلاسة. يبدو إبريق الشاي مستديراً ومنحنياً بشكل صحيح. ومع ذلك، فإن نقاط التمييز المرآوية على الجسم باهتة وموزعة بشكل غير صحيح.

- **تظليل فونج (الشكل 2ج)**: ينتج نتائج واقعية للصور. تظهر نقاط تمييز حادة على الأسطح المحدبة للجسم والمقبض والصنبور، في موضعها الصحيح بناءً على المصدر الضوئي واتجاه المشاهدة. تبدو المادة سيراميك لامع أو معدن مصقول كما هو مقصود.

**المشهد 3: أجسام متعددة**
مشهد مع أجسام متعددة من مواد مختلفة (غير لامع، بلاستيك، معدن) يوضح تنوع نموذج الإضاءة:

- أجسام بـ $k_s$ منخفض و$n$ منخفض (مواد غير لامعة مثل الطين): تبدو باهتة بدون نقاط تمييز، بغض النظر عن زاوية المشاهدة
- أجسام بـ $k_s$ متوسط و$n$ متوسط (بلاستيك): تظهر نقاط تمييز واسعة ولطيفة
- أجسام بـ $k_s$ مرتفع و$n$ مرتفع (معدن): تظهر نقاط تمييز حادة ومكثفة تشير بوضوح إلى اللمعان

نفس نموذج الإضاءة، مع معاملات مختلفة، يمثل بنجاح مجموعة واسعة من المواد.

#### الأداء الحسابي

تم إجراء الاختبارات على حاسوب DEC PDP-10 مع أجهزة رسوميات مخصصة:

| طريقة التظليل | مضلعات/ثانية | السرعة النسبية |
|----------------|----------------|----------------|
| التظليل المسطح | 950 | 1.0× |
| تظليل جورو | 480 | 0.5× |
| تظليل فونج | 220 | 0.23× |

**الدقة**: 512×512 بكسل
**تعقيد النموذج**: كرة (200 مثلث)، إبريق شاي (800 مثلث)

على الرغم من التباطؤ بمقدار ~4× لتظليل فونج مقارنة بالتظليل المسطح، فإن تحسن الجودة البصرية يبرر التكلفة لتطبيقات التقديم عالية الجودة. بالنسبة للتطبيقات التفاعلية، تحافظ الدقة المنخفضة أو أعداد المضلعات المنخفضة على معدلات إطارات مقبولة.

#### مقارنة مع الصور الفوتوغرافية

للتحقق من واقعية الصور المظللة بفونج، قارنا الكرات المقدمة بصور فوتوغرافية لكرات فيزيائية تحت إضاءة مماثلة:

- **موضع نقطة التمييز**: يتنبأ تظليل فونج بشكل صحيح بموقع نقاط التمييز المرآوية المطابقة للأدلة الفوتوغرافية
- **شكل نقطة التمييز**: ينتج تناقص قوة جيب التمام أشكال نقاط تمييز تشبه إلى حد كبير تلك الموجودة على الأسطح اللامعة الحقيقية
- **سلاسة السطح**: يلغي نهج الناظم المستوفى المظهر المضلعي، مطابقاً المظهر الأملس للأجسام الفيزيائية

**القيود الملاحظة:**
- نموذج الإضاءة المحلي لا يلتقط الانعكاسات المتبادلة (أجسام تنعكس في بعضها البعض)
- لا يتم حساب الظلال (أشعة الظل غير منفذة في هذا النظام القائم على خطوط المسح)
- قيم اللمعان العالية جداً ($n > 200$) تنتج أحياناً نتائج غير واقعية قليلاً بسبب الدقة العددية

ومع ذلك، بالنسبة لغالبية المشاهد والمواد، ينتج تظليل فونج صوراً قريبة بشكل ملحوظ من الواقع الفوتوغرافي، خاصة للأجسام المعزولة تحت إضاءة بسيطة.

#### تقييم الجودة الذاتي

أسفرت دراسات المستخدم غير الرسمية مع باحثي الرسوميات الحاسوبية والفنانين عن ملاحظات متسقة:

1. **التظليل المسطح**: يُدرك عالمياً على أنه "اصطناعي"، "هندسي"، "مضلعي"
2. **تظليل جورو**: يُوصف بأنه "سلس ولكن مسطح"، "غير لامع"، "يفتقر إلى العمق"
3. **تظليل فونج**: يُوصف بأنه "واقعي"، "ثلاثي الأبعاد"، "لامع"، "مقنع"

تم تحديد نقاط التمييز المرآوية على أنها السمة المميزة الرئيسية التي تجعل الصور المظللة بفونج تبدو أكثر واقعية وثلاثية الأبعاد.

#### التطبيقات

تم تطبيق التقنيات الموصوفة بنجاح على:

- **تصور المنتجات**: تقديم تصاميم صناعية للكتالوجات والعروض التقديمية
- **التصور العلمي**: عرض الهياكل الجزيئية، بيانات التضاريس، محاكاة ديناميكيات الموائع
- **الترفيه**: الصور المولدة حاسوبياً المبكرة للأفلام والتلفزيون
- **التعليم**: تدريس الرسوميات الحاسوبية، النمذجة الهندسية، الفيزياء البصرية

أصبح الجمع بين تظليل فونج واستيفاء متجه الناظم النهج القياسي للتقديم القائم على المضلعات في هذه المجالات.

---

### Translation Notes

- **Figures referenced:** Figure 1a-c (sphere comparisons), Figure 2a-c (teapot comparisons)
- **Key terms introduced:**
  - faceted appearance (مظهر مضلعي)
  - polyhedron (متعدد السطوح)
  - Utah teapot (إبريق شاي يوتا)
  - Bézier patch (رقعة بيزييه)
  - tessellation (تضليع)
  - photorealistic (واقعي للصور)
  - inter-reflection (انعكاس متبادل)
  - shadow ray (شعاع الظل)
  - frame rate (معدل الإطارات)
- **Equations:** None (results and observations)
- **Citations:** Reference to DEC PDP-10 computer, Utah teapot model
- **Special handling:** Performance table, subjective assessments, comparison with photography

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation (Validation)

Rendered images demonstrate the effectiveness of the proposed techniques by comparing flat, Gouraud, and Phong shading on the same models.

For a sphere: flat shading shows faceted appearance with visible polygon boundaries; Gouraud shading is smooth but lacks specular highlights; Phong shading produces realistic highlights that move correctly with viewpoint. The Utah teapot model shows similar progression from angular (flat) to smooth but dull (Gouraud) to photorealistic (Phong).

Performance on DEC PDP-10: flat shading 950 polygons/second, Gouraud 480, Phong 220. Despite 4× slowdown, visual quality justifies the cost. Comparison with photographs validates realism, though limitations include no inter-reflections or shadows.

User feedback: flat shading perceived as "artificial", Gouraud as "smooth but flat", Phong as "realistic" and "three-dimensional". Applications include product visualization, scientific visualization, entertainment, and education.
