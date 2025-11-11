---
# An Improved Illumination Model for Shaded Display
## نموذج إضاءة محسّن للعرض المظلل

**Author:** Turner Whitted
**Year:** 1980
**Publication:** Communications of the ACM, Volume 23, Issue 6, Pages 343-349
**DOI:** 10.1145/358876.358882
**Translation Quality:** 0.93
**Glossary Terms Used:** algorithm (خوارزمية), rendering (التقديم), simulation (محاكاة), ray tracing (تتبع الأشعة)

### English Abstract
To accurately render a two-dimensional image of a three-dimensional scene, global illumination information that affects the intensity of each pixel of the image must be known at the time the intensity is calculated. In a simplified form, this information is stored in a tree of 'rays' extending from the viewer to the first surface encountered and from there to other surfaces and to the light sources. A visible surface algorithm creates this tree for each pixel of the display and passes it to the shader. The shader then traverses the tree to determine the intensity of the light received by the viewer. Consideration of all of these factors allows the shader to accurately simulate true reflection, shadows, and refraction, as well as the effects simulated by conventional shaders.

### الملخص العربي
لتقديم صورة ثنائية الأبعاد بدقة لمشهد ثلاثي الأبعاد، يجب معرفة معلومات الإضاءة الشاملة التي تؤثر على شدة كل بكسل من الصورة في وقت حساب الشدة. في شكل مبسط، يتم تخزين هذه المعلومات في شجرة من "الأشعة" تمتد من المشاهد إلى السطح الأول الذي يتم مواجهته ومن هناك إلى الأسطح الأخرى وإلى مصادر الضوء. تقوم خوارزمية الأسطح المرئية بإنشاء هذه الشجرة لكل بكسل من الشاشة وتمريرها إلى مظلل التقديم. يجتاز المظلل بعد ذلك الشجرة لتحديد شدة الضوء الذي يستقبله المشاهد. يتيح النظر في جميع هذه العوامل للمظلل محاكاة الانعكاس الحقيقي والظلال والانكسار بدقة، بالإضافة إلى التأثيرات التي تحاكيها المظللات التقليدية.

### Back-Translation (Validation)
To accurately render a two-dimensional image of a three-dimensional scene, global illumination information that affects the intensity of each pixel of the image must be known at the time of intensity calculation. In a simplified form, this information is stored in a tree of 'rays' extending from the viewer to the first surface encountered and from there to other surfaces and to the light sources. The visible surface algorithm creates this tree for each pixel of the screen and passes it to the rendering shader. The shader then traverses the tree to determine the intensity of the light received by the viewer. Considering all these factors allows the shader to accurately simulate true reflection, shadows, and refraction, as well as the effects simulated by conventional shaders.

### Translation Metrics
- Iterations: 1
- Final Score: 0.93
- Quality: High
---
