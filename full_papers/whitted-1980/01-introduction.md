# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** rendering (التقديم), algorithm (خوارزمية), shading (التظليل), computer graphics (رسومات حاسوبية), illumination (إضاءة), visible surface (سطح مرئي), ray tracing (تتبع الأشعة)

---

### English Version

The production of shaded pictures of three-dimensional objects by computer has been an active area of research in computer graphics for some time. The fundamental problem is to determine which surfaces in the scene are visible from a given viewpoint and what intensity value should be assigned to each visible surface element to produce a realistic image.

Early computer graphics systems used simple shading models that calculated the intensity at each point on a surface based only on the light arriving directly from light sources. While these methods could produce images showing the general shape of objects, they failed to capture many important visual effects that make real scenes appear realistic.

The most commonly used shading model prior to this work was developed by Phong. The Phong illumination model calculates the intensity at a point on a surface as a combination of three components: ambient reflection (constant background illumination), diffuse reflection (following Lambert's cosine law), and specular reflection (producing highlights). While this model works well for opaque surfaces lit by direct illumination, it does not account for several important phenomena:

1. **Mirror reflections:** Shiny surfaces should reflect images of other objects in the scene
2. **Transparent objects:** Glass and water should show both reflections and refractions
3. **Shadows:** Objects should cast shadows on other objects
4. **Inter-reflection:** Light should bounce between surfaces

This paper presents an improved illumination model that extends the Phong model to simulate these additional effects. The key innovation is the use of recursive ray tracing: when a ray from the eye intersects a surface, additional rays are traced in the directions of reflection and refraction, and toward each light source to test for shadows. These secondary rays can themselves spawn additional rays, forming a tree structure that captures the global illumination in the scene.

The recursive approach allows the renderer to accurately simulate mirror reflections, transparent refractions, and shadows while maintaining compatibility with conventional shading models for diffuse surfaces. The algorithm determines the intensity of each pixel by constructing and evaluating a ray tree that represents all the paths by which light can reach the viewer's eye.

---

### النسخة العربية

كان إنتاج صور مظللة لأجسام ثلاثية الأبعاد بواسطة الحاسوب مجالاً نشطاً للبحث في الرسومات الحاسوبية لبعض الوقت. المشكلة الأساسية هي تحديد الأسطح المرئية في المشهد من نقطة مشاهدة معينة وما هي قيمة الشدة التي يجب تعيينها لكل عنصر سطح مرئي لإنتاج صورة واقعية.

استخدمت أنظمة الرسومات الحاسوبية المبكرة نماذج تظليل بسيطة تحسب الشدة عند كل نقطة على السطح بناءً فقط على الضوء الوارد مباشرة من مصادر الضوء. بينما يمكن لهذه الطرق إنتاج صور تُظهر الشكل العام للأجسام، فشلت في التقاط العديد من التأثيرات البصرية المهمة التي تجعل المشاهد الحقيقية تبدو واقعية.

كان نموذج التظليل الأكثر استخداماً قبل هذا العمل قد طوره فونغ (Phong). يحسب نموذج إضاءة فونغ الشدة عند نقطة على السطح كمجموع لثلاثة مكونات: الانعكاس المحيط (إضاءة خلفية ثابتة)، والانعكاس المنتشر (باتباع قانون جيب التمام لامبرت)، والانعكاس اللامع (الذي ينتج نقاط سطوع). بينما يعمل هذا النموذج بشكل جيد للأسطح المعتمة المضاءة بإضاءة مباشرة، إلا أنه لا يأخذ في الاعتبار عدة ظواهر مهمة:

1. **الانعكاسات المرآوية:** يجب أن تعكس الأسطح اللامعة صور الأجسام الأخرى في المشهد
2. **الأجسام الشفافة:** يجب أن تُظهر الأجسام الزجاجية والمائية كلاً من الانعكاسات والانكسارات
3. **الظلال:** يجب أن تلقي الأجسام ظلالاً على الأجسام الأخرى
4. **الانعكاس المتبادل:** يجب أن يرتد الضوء بين الأسطح

تقدم هذه الورقة نموذج إضاءة محسّن يوسع نموذج فونغ لمحاكاة هذه التأثيرات الإضافية. الابتكار الرئيسي هو استخدام تتبع الأشعة العودي: عندما يتقاطع شعاع من العين مع سطح، يتم تتبع أشعة إضافية في اتجاهات الانعكاس والانكسار، وباتجاه كل مصدر ضوء لاختبار الظلال. يمكن لهذه الأشعة الثانوية نفسها أن تولد أشعة إضافية، مكونة بنية شجرية تلتقط الإضاءة الشاملة في المشهد.

يسمح النهج العودي للمُقدِّم بمحاكاة الانعكاسات المرآوية والانكسارات الشفافة والظلال بدقة مع الحفاظ على التوافق مع نماذج التظليل التقليدية للأسطح المنتشرة. تحدد الخوارزمية شدة كل بكسل من خلال بناء وتقييم شجرة أشعة تمثل جميع المسارات التي يمكن للضوء من خلالها الوصول إلى عين المشاهد.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:**
  - Phong illumination model (نموذج إضاءة فونغ)
  - Ambient reflection (الانعكاس المحيط)
  - Diffuse reflection (الانعكاس المنتشر)
  - Specular reflection (الانعكاس اللامع)
  - Mirror reflection (الانعكاس المرآوي)
  - Recursive ray tracing (تتبع الأشعة العودي)
  - Ray tree (شجرة الأشعة)
  - Global illumination (الإضاءة الشاملة)
- **Equations:** None in introduction
- **Citations:** Reference to Phong's work
- **Special handling:** Technical introduction establishing context and motivation for the improved model

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.85
- **Overall section score:** 0.88
