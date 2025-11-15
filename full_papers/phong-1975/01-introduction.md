# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** rendering (التقديم), algorithm (خوارزمية), shading (تظليل), polygon (مضلع), hidden surface (السطح المخفي), cathode-ray tube (أنبوب الأشعة المهبطية)

---

### English Version

The display of computer generated pictures of three-dimensional objects has been a field of increasing importance in computer graphics. The techniques for hidden surface removal and realistic rendering have been extensively studied. The purpose of this paper is to present several shading techniques to render three-dimensional objects more realistically. To fully appreciate the shading methods presented here, it is necessary to understand the relationship between the shading algorithm, the object modeling scheme, and the hidden surface algorithm.

In computer graphics, an object is usually modeled as a collection of surface patches. Each surface patch may be represented in different ways: as a polygon, as a parametric surface, or as an implicit surface defined by an equation. The choice of surface representation affects both the hidden surface removal algorithm and the shading algorithm. The hidden surface problem involves determining which surfaces are visible from a given viewpoint. Once the visible surfaces are determined, they must be shaded to provide realistic appearance.

The shading of an object determines how light it appears to be. In the real world, the appearance of an object depends on several factors: the properties of the object's surface (color, reflectance, texture), the position and characteristics of the light sources, and the position of the observer. A good shading algorithm should take into account these factors to produce realistic images.

Previous work in computer graphics has used various shading methods. The simplest method is constant shading, where each polygon is painted with a uniform intensity. This method is fast but produces images with a faceted appearance. A better method is intensity interpolation (Gouraud shading), where intensities are computed at polygon vertices and interpolated across the polygon surface. This produces smoother-looking images but still has limitations in rendering specular highlights.

This paper presents an improved shading method that interpolates the surface normal vectors rather than intensities. The normal vector interpolation produces more accurate specular highlights and better overall image quality. The method considers ambient light, diffuse reflection, and specular reflection components to calculate the intensity at each point on the visible surface.

---

### النسخة العربية

يُعد عرض الصور المولّدة حاسوبياً للأجسام ثلاثية الأبعاد مجالاً ذا أهمية متزايدة في رسومات الحاسوب. تمت دراسة تقنيات إزالة الأسطح المخفية والتقديم الواقعي على نطاق واسع. الغرض من هذا البحث هو تقديم عدة تقنيات تظليل لتقديم الأجسام ثلاثية الأبعاد بشكل أكثر واقعية. لتقدير كامل لطرق التظليل المقدمة هنا، من الضروري فهم العلاقة بين خوارزمية التظليل، ومخطط نمذجة الأجسام، وخوارزمية الأسطح المخفية.

في رسومات الحاسوب، عادةً ما يتم نمذجة الجسم كمجموعة من رقع السطح. يمكن تمثيل كل رقعة سطح بطرق مختلفة: كمضلع، أو كسطح بارامتري، أو كسطح ضمني محدد بمعادلة. يؤثر اختيار تمثيل السطح على كل من خوارزمية إزالة السطح المخفي وخوارزمية التظليل. تتضمن مشكلة السطح المخفي تحديد الأسطح المرئية من نقطة مشاهدة معينة. بمجرد تحديد الأسطح المرئية، يجب تظليلها لتوفير مظهر واقعي.

يحدد تظليل الجسم مدى سطوع ظهوره. في العالم الحقيقي، يعتمد مظهر الجسم على عدة عوامل: خصائص سطح الجسم (اللون، الانعكاسية، الملمس)، وموضع وخصائص مصادر الضوء، وموضع المراقب. يجب أن تأخذ خوارزمية التظليل الجيدة هذه العوامل في الاعتبار لإنتاج صور واقعية.

استخدمت الأعمال السابقة في رسومات الحاسوب طرق تظليل مختلفة. الطريقة الأبسط هي التظليل الثابت، حيث يتم رسم كل مضلع بشدة موحدة. هذه الطريقة سريعة لكنها تنتج صوراً ذات مظهر مُوَجَّه. الطريقة الأفضل هي استيفاء الشدة (تظليل جورو)، حيث يتم حساب الشدات عند رؤوس المضلع واستيفائها عبر سطح المضلع. ينتج هذا صوراً ذات مظهر أنعم لكن لا يزال لها قيود في تقديم الإبرازات اللامعة.

يقدم هذا البحث طريقة تظليل محسّنة تستوفي متجهات الناظم (العمودي) للسطح بدلاً من الشدات. ينتج استيفاء متجه الناظم إبرازات لامعة أكثر دقة وجودة صورة إجمالية أفضل. تأخذ الطريقة في الاعتبار مكونات الضوء المحيط، والانعكاس المنتشر، والانعكاس اللامع لحساب الشدة عند كل نقطة على السطح المرئي.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - surface patch (رقعة السطح)
  - parametric surface (سطح بارامتري)
  - implicit surface (سطح ضمني)
  - constant shading (تظليل ثابت)
  - Gouraud shading (تظليل جورو)
  - intensity interpolation (استيفاء الشدة)
  - normal vector (متجه الناظم/العمودي)
  - ambient light (ضوء محيط)
  - diffuse reflection (انعكاس منتشر)
  - specular reflection (انعكاس لامع)
  - specular highlights (إبرازات لامعة)
- **Equations:** None in this section
- **Citations:** References to previous work (general)
- **Special handling:** Technical terms carefully translated to maintain consistency with glossary

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89
