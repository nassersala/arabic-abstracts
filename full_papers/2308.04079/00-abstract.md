---
# 3D Gaussian Splatting for Real-Time Radiance Field Rendering
## تناثر غاوسي ثلاثي الأبعاد لتقديم حقول الإشعاع في الوقت الفعلي

**arXiv ID:** 2308.04079
**Authors:** Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
**Year:** 2023
**Categories:** cs.GR (Graphics); cs.CV (Computer Vision and Pattern Recognition)
**Translation Quality:** 0.88
**Glossary Terms Used:** rendering, real-time, method, novel, scene, neural network, training, visual fidelity, competitive, sparse, camera, optimization, covariance, representation, algorithm, dataset, computation, state-of-the-art, calibration, Gaussian, splatting, view synthesis, volumetric, anisotropic, visibility, display rate, unbounded, resolution, fps, interleaved, density control, established

### English Abstract
Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos. However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality. For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (>= 30 fps) novel-view synthesis at 1080p resolution. First, starting from sparse points produced during camera calibration, we represent the scene with 3D Gaussians that preserve desirable properties of continuous volumetric radiance fields for scene optimization while avoiding unnecessary computation in empty space; Second, we perform interleaved optimization/density control of the 3D Gaussians, notably optimizing anisotropic covariance to achieve an accurate representation of the scene; Third, we develop a fast visibility-aware rendering algorithm that supports anisotropic splatting and both accelerates training and allows realtime rendering. We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets.

### الملخص العربي
أحدثت طرق حقول الإشعاع ثورةً مؤخراً في توليد المناظر الجديدة للمشاهد الملتقطة بصور أو فيديوهات متعددة. ومع ذلك، لا يزال تحقيق جودة بصرية عالية يتطلب شبكات عصبية مكلفة في التدريب والتقديم، بينما تتنازل الطرق الأسرع الحديثة حتماً عن السرعة مقابل الجودة. بالنسبة للمشاهد غير المحدودة والكاملة (بدلاً من الأجسام المعزولة) والتقديم بدقة وضوح ١٠٨٠ بكسل، لا توجد طريقة حالية يمكنها تحقيق معدلات عرض في الوقت الفعلي. نقدم ثلاثة عناصر رئيسية تسمح لنا بتحقيق جودة بصرية متقدمة مع الحفاظ على أوقات تدريب منافسة، والأهم من ذلك، تتيح توليد مناظر جديدة عالي الجودة في الوقت الفعلي (>= ٣٠ إطاراً في الثانية) بدقة وضوح ١٠٨٠ بكسل. أولاً، انطلاقاً من النقاط المتفرقة الناتجة أثناء معايرة الكاميرا، نمثل المشهد بغاوسيات ثلاثية الأبعاد تحافظ على الخصائص المرغوبة لحقول الإشعاع الحجمية المستمرة لتحسين المشهد مع تجنب الحسابات غير الضرورية في المساحات الفارغة؛ ثانياً، نجري تحسيناً متشابكاً والتحكم في الكثافة للغاوسيات ثلاثية الأبعاد، مع تحسين التباين المشترك اللامتماثل بشكل خاص لتحقيق تمثيل دقيق للمشهد؛ ثالثاً، نطور خوارزمية تقديم سريعة واعية للرؤية تدعم التناثر اللامتماثل وتسرّع التدريب وتتيح التقديم في الوقت الفعلي. نُظهر جودة بصرية متقدمة وتقديماً في الوقت الفعلي على عدة مجموعات بيانات راسخة.

### Back-Translation (Validation)
Radiance field methods have recently revolutionized the generation of new views for scenes captured with multiple images or videos. However, achieving high visual quality still requires neural networks that are costly in training and rendering, while recent faster methods inevitably trade off speed for quality. For unbounded and complete scenes (rather than isolated objects) and rendering at 1080p resolution, there is no current method that can achieve real-time display rates. We present three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times, and more importantly, enable high-quality generation of new views in real-time (>= 30 frames per second) at 1080p resolution. First, starting from sparse points produced during camera calibration, we represent the scene with 3D Gaussians that preserve the desirable properties of continuous volumetric radiance fields for scene optimization while avoiding unnecessary computations in empty spaces; Second, we perform interleaved optimization and density control of the 3D Gaussians, particularly optimizing anisotropic covariance to achieve an accurate representation of the scene; Third, we develop a fast visibility-aware rendering algorithm that supports anisotropic splatting and accelerates training and enables real-time rendering. We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets.

### Translation Metrics
- Iterations: 1
- Final Score: 0.88
- Quality: High

### Translation Notes
This paper introduces 3D Gaussian Splatting, a breakthrough method in real-time rendering of radiance fields. Key technical terms:
- **Radiance field** (حقل الإشعاع): A 3D representation encoding light information
- **Gaussian splatting** (تناثر غاوسي): Rendering technique using Gaussian functions
- **Anisotropic covariance** (التباين المشترك اللامتماثل): Non-uniform directional properties
- **Novel-view synthesis** (توليد المناظر الجديدة): Generating new viewpoints from captured data
- **Volumetric** (حجمي): 3D volume-based representation
---
