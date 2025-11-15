# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** algorithm (خوارزمية), rendering (التقديم), simulation (محاكاة), ray tracing (تتبع الأشعة), illumination (إضاءة), shader (مظلل), visible surface (سطح مرئي)

---

### English Version

To accurately render a two-dimensional image of a three-dimensional scene, global illumination information that affects the intensity of each pixel of the image must be known at the time the intensity is calculated. In a simplified form, this information is stored in a tree of 'rays' extending from the viewer to the first surface encountered and from there to other surfaces and to the light sources. A visible surface algorithm creates this tree for each pixel of the display and passes it to the shader. The shader then traverses the tree to determine the intensity of the light received by the viewer. Consideration of all of these factors allows the shader to accurately simulate true reflection, shadows, and refraction, as well as the effects simulated by conventional shaders.

---

### النسخة العربية

لتقديم صورة ثنائية الأبعاد بدقة لمشهد ثلاثي الأبعاد، يجب معرفة معلومات الإضاءة الشاملة التي تؤثر على شدة كل بكسل من الصورة في وقت حساب الشدة. في شكل مبسط، يتم تخزين هذه المعلومات في شجرة من "الأشعة" تمتد من المشاهد إلى السطح الأول الذي يتم مواجهته ومن هناك إلى الأسطح الأخرى وإلى مصادر الضوء. تقوم خوارزمية الأسطح المرئية بإنشاء هذه الشجرة لكل بكسل من الشاشة وتمريرها إلى مظلل التقديم. يجتاز المظلل بعد ذلك الشجرة لتحديد شدة الضوء الذي يستقبله المشاهد. يتيح النظر في جميع هذه العوامل للمظلل محاكاة الانعكاس الحقيقي والظلال والانكسار بدقة، بالإضافة إلى التأثيرات التي تحاكيها المظللات التقليدية.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Ray tree (شجرة الأشعة)
  - Global illumination (إضاءة شاملة)
  - Visible surface algorithm (خوارزمية الأسطح المرئية)
  - Shader (مظلل التقديم)
  - Reflection (انعكاس)
  - Refraction (انكسار)
- **Equations:** None in abstract
- **Citations:** None in abstract
- **Special handling:** Technical terminology maintained consistently with glossary

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.92
- **Overall section score:** 0.93
