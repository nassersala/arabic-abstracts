---
# Global Illumination using Photon Maps
## الإضاءة الشاملة باستخدام خرائط الفوتون

**Author:** Henrik Wann Jensen
**Year:** 1996
**Publication:** Rendering Techniques '96 (Eurographics Workshop on Rendering)
**Translation Quality:** 0.90
**Glossary Terms Used:** algorithm (خوارزمية), rendering (التقديم), ray tracing (تتبع الأشعة), photon mapping (خرائط الفوتون)

### English Abstract
This paper presents a two pass global illumination method based on the concept of photon maps. It represents a significant improvement of a previously described approach both with respect to speed, accuracy and versatility. In the first pass two photon maps are created by emitting packets of energy (photons) from the light sources and storing these as they hit surfaces within the scene. We use one high resolution caustics photon map to render caustics that are visualized directly and one low resolution photon map that is used during the rendering step. The scene is rendered using a distribution ray tracing algorithm optimized by using the information in the photon maps.

### الملخص العربي
تقدم هذه الورقة طريقة إضاءة شاملة ثنائية المرور تعتمد على مفهوم خرائط الفوتون. تمثل تحسيناً كبيراً لنهج موصوف سابقاً من حيث السرعة والدقة والمرونة. في المرور الأول، يتم إنشاء خريطتي فوتون عن طريق إصدار حزم من الطاقة (فوتونات) من مصادر الضوء وتخزينها عند اصطدامها بالأسطح داخل المشهد. نستخدم خريطة فوتون عالية الدقة للظواهر الكاوية لتقديم الظواهر الكاوية التي يتم تصورها مباشرة، وخريطة فوتون منخفضة الدقة تُستخدم أثناء خطوة التقديم. يتم تقديم المشهد باستخدام خوارزمية تتبع الأشعة الموزعة المُحسّنة باستخدام المعلومات في خرائط الفوتون.

### Back-Translation (Validation)
This paper presents a two-pass global illumination method based on the concept of photon maps. It represents a significant improvement over a previously described approach in terms of speed, accuracy, and flexibility. In the first pass, two photon maps are created by emitting energy packets (photons) from light sources and storing them when they hit surfaces within the scene. We use a high-resolution photon map for caustic phenomena to render caustic phenomena that are visualized directly, and a low-resolution photon map that is used during the rendering step. The scene is rendered using a distributed ray tracing algorithm optimized using the information in the photon maps.

### Translation Metrics
- Iterations: 1
- Final Score: 0.90
- Quality: High
---
