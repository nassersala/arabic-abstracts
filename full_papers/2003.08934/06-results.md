# Section 6: Results
## القسم 6: النتائج

**Section:** results
**Translation Quality:** 0.85
**Glossary Terms Used:** quantitative, qualitative, ablation study, baseline, PSNR, SSIM, LPIPS, dataset, synthetic rendering, pathtracing, forward-facing capture, DeepVoxels, Scene Representation Networks (SRN), Neural Volumes (NV), Local Light Field Fusion (LLFF)

---

### English Version

We quantitatively (Tables 1) and qualitatively (Figs. 8 and 6) show that our method outperforms prior work, and provide extensive ablation studies to validate our design choices (Table 2). We urge the reader to view our supplementary video to better appreciate our method's significant improvement over baseline methods when rendering smooth paths of novel views.

## 6.1 Datasets

**Synthetic renderings of objects** We first show experimental results on two datasets of synthetic renderings of objects (Table 1, "Diffuse Synthetic 360°" and "Realistic Synthetic 360°"). The DeepVoxels [41] dataset contains four Lambertian objects with simple geometry. Each object is rendered at 512 × 512 pixels from viewpoints sampled on the upper hemisphere (479 as input and 1000 for testing). We additionally generate our own dataset containing pathtraced images of eight objects that exhibit complicated geometry and realistic non-Lambertian materials. Six are rendered from viewpoints sampled on the upper hemisphere, and two are rendered from viewpoints sampled on a full sphere. We render 100 views of each scene as input and 200 for testing, all at 800 × 800 pixels.

**Real images of complex scenes** We show results on complex real-world scenes captured with roughly forward-facing images (Table 1, "Real Forward-Facing"). This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), captured with 20 to 62 images, and hold out 1/8 of these for the test set. All images are 1008×756 pixels.

## 6.2 Comparisons

To evaluate our model we compare against current top-performing techniques for view synthesis, detailed below. All methods use the same set of input views to train a separate network for each scene except Local Light Field Fusion [28], which trains a single 3D convolutional network on a large dataset, then uses the same trained network to process input images of new scenes at test time.

**Neural Volumes (NV) [24]** synthesizes novel views of objects that lie entirely within a bounded volume in front of a distinct background (which must be separately captured without the object of interest). It optimizes a deep 3D convolutional network to predict a discretized RGBα voxel grid with 128³ samples as well as a 3D warp grid with 32³ samples. The algorithm renders novel views by marching camera rays through the warped voxel grid.

**Scene Representation Networks (SRN) [42]** represent a continuous scene as an opaque surface, implicitly defined by a MLP that maps each (x, y, z) coordinate to a feature vector. They train a recurrent neural network to march along a ray through the scene representation by using the feature vector at any 3D coordinate to predict the next step size along the ray. The feature vector from the final step is decoded into a single color for that point on the surface. Note that SRN is a better-performing followup to DeepVoxels [41] by the same authors, which is why we do not include comparisons to DeepVoxels.

**Local Light Field Fusion (LLFF) [28]** LLFF is designed for producing photorealistic novel views for well-sampled forward facing scenes. It uses a trained 3D convolutional network to directly predict a discretized frustum-sampled RGBα grid (multiplane image or MPI [52]) for each input view, then renders novel views by alpha compositing and blending nearby MPIs into the novel viewpoint.

## 6.3 Discussion

We thoroughly outperform both baselines that also optimize a separate network per scene (NV and SRN) in all scenarios. Furthermore, we produce qualitatively and quantitatively superior renderings compared to LLFF (across all except one metric) while using only their input images as our entire training set.

The SRN method produces heavily smoothed geometry and texture, and its representational power for view synthesis is limited by selecting only a single depth and color per camera ray. The NV baseline is able to capture reasonably detailed volumetric geometry and appearance, but its use of an underlying explicit 128³ voxel grid prevents it from scaling to represent fine details at high resolutions. LLFF specifically provides a "sampling guideline" to not exceed 64 pixels of disparity between input views, so it frequently fails to estimate correct geometry in the synthetic datasets which contain up to 400-500 pixels of disparity between views. Additionally, LLFF blends between different scene representations for rendering different views, resulting in perceptually-distracting inconsistency as is apparent in our supplementary video.

The biggest practical tradeoffs between these methods are time versus space. All compared single scene methods take at least 12 hours to train per scene. In contrast, LLFF can process a small input dataset in under 10 minutes. However, LLFF produces a large 3D voxel grid for every input image, resulting in enormous storage requirements (over 15GB for one "Realistic Synthetic" scene). Our method requires only 5 MB for the network weights (a relative compression of 3000× compared to LLFF), which is even less memory than the input images alone for a single scene from any of our datasets.

## 6.4 Ablation studies

We validate our algorithm's design choices and parameters with an extensive ablation study in Table 2. We present results on our "Realistic Synthetic 360°" scenes. Row 9 shows our complete model as a point of reference. Row 1 shows a minimalist version of our model without positional encoding (PE), view-dependence (VD), or hierarchical sampling (H). In rows 2–4 we remove these three components one at a time from the full model, observing that positional encoding (row 2) and view-dependence (row 3) provide the largest quantitative benefit followed by hierarchical sampling (row 4). Rows 5–6 show how our performance decreases as the number of input images is reduced. Note that our method's performance using only 25 input images still exceeds NV, SRN, and LLFF across all metrics when they are provided with 100 images (see supplementary material). In rows 7–8 we validate our choice of the maximum frequency L used in our positional encoding for **x** (the maximum frequency used for **d** is scaled proportionally). Only using 5 frequencies reduces performance, but increasing the number of frequencies from 10 to 15 does not improve performance. We believe the benefit of increasing L is limited once 2^L exceeds the maximum frequency present in the sampled input images (roughly 1024 in our data).

---

### النسخة العربية

نوضح كمياً (الجداول 1) ونوعياً (الأشكال 8 و6) أن طريقتنا تتفوق على الأعمال السابقة، ونقدم دراسات استئصال واسعة للتحقق من صحة خياراتنا التصميمية (الجدول 2). نحث القارئ على مشاهدة الفيديو التكميلي الخاص بنا لتقدير أفضل للتحسين الكبير لطريقتنا على طرق الخط الأساسي عند تصيير مسارات سلسة من المناظر الجديدة.

## 6.1 مجموعات البيانات

**تصييرات اصطناعية للأجسام** نعرض أولاً النتائج التجريبية على مجموعتي بيانات من التصييرات الاصطناعية للأجسام (الجدول 1، "اصطناعي منتشر 360°" و"اصطناعي واقعي 360°"). تحتوي مجموعة بيانات DeepVoxels [41] على أربعة أجسام لامبرتية ذات هندسة بسيطة. يُصيَّر كل جسم بدقة 512 × 512 بكسل من نقاط مشاهدة معيّنة على نصف الكرة العلوي (479 كمدخل و1000 للاختبار). نولد بالإضافة إلى ذلك مجموعة بياناتنا الخاصة التي تحتوي على صور متتبعة المسار لثمانية أجسام تظهر هندسة معقدة ومواد واقعية غير لامبرتية. يُصيَّر ستة منها من نقاط مشاهدة معيّنة على نصف الكرة العلوي، ويُصيَّر اثنان من نقاط مشاهدة معيّنة على كرة كاملة. نصيّر 100 منظر لكل مشهد كمدخل و200 للاختبار، جميعها بدقة 800 × 800 بكسل.

**صور حقيقية لمشاهد معقدة** نعرض النتائج على مشاهد من العالم الحقيقي معقدة تم التقاطها بصور متجهة للأمام تقريباً (الجدول 1، "حقيقي متجه للأمام"). تتكون مجموعة البيانات هذه من 8 مشاهد تم التقاطها بهاتف محمول محمول باليد (5 مأخوذة من ورقة LLFF و3 نلتقطها نحن)، تم التقاطها بـ 20 إلى 62 صورة، ونحتفظ بـ 1/8 منها لمجموعة الاختبار. جميع الصور بدقة 1008×756 بكسل.

## 6.2 المقارنات

لتقييم نموذجنا، نقارنه بالتقنيات الحالية الأفضل أداءً لتركيب المناظر، الموضحة أدناه. تستخدم جميع الطرق نفس مجموعة المناظر المدخلة لتدريب شبكة منفصلة لكل مشهد باستثناء Local Light Field Fusion [28]، الذي يدرب شبكة تلافيفية ثلاثية الأبعاد واحدة على مجموعة بيانات كبيرة، ثم يستخدم نفس الشبكة المدربة لمعالجة صور مدخلة لمشاهد جديدة في وقت الاختبار.

**Neural Volumes (NV) [24]** يركب مناظر جديدة للأجسام التي تقع بالكامل داخل حجم محدد أمام خلفية متميزة (والتي يجب التقاطها بشكل منفصل بدون الجسم محل الاهتمام). يحسّن شبكة تلافيفية ثلاثية الأبعاد عميقة للتنبؤ بشبكة حجمية RGBα متقطعة بـ 128³ عينة بالإضافة إلى شبكة انحراف ثلاثية الأبعاد بـ 32³ عينة. تصيّر الخوارزمية مناظر جديدة من خلال السير بأشعة الكاميرا عبر الشبكة الحجمية المنحرفة.

**Scene Representation Networks (SRN) [42]** تمثل مشهداً مستمراً كسطح معتم، محدد ضمنياً بواسطة MLP يعيّن كل إحداثي (x, y, z) إلى متجه ميزات. يدربون شبكة عصبية متكررة للسير على طول شعاع عبر تمثيل المشهد باستخدام متجه الميزات عند أي إحداثي ثلاثي الأبعاد للتنبؤ بحجم الخطوة التالية على طول الشعاع. يتم فك تشفير متجه الميزات من الخطوة النهائية إلى لون واحد لتلك النقطة على السطح. لاحظ أن SRN هو متابعة أفضل أداءً لـ DeepVoxels [41] من قبل نفس المؤلفين، ولهذا السبب لا نضمّن مقارنات مع DeepVoxels.

**Local Light Field Fusion (LLFF) [28]** صُمم LLFF لإنتاج مناظر جديدة واقعية فوتوغرافياً للمشاهد المتجهة للأمام ذات العينات الجيدة. يستخدم شبكة تلافيفية ثلاثية الأبعاد مدربة للتنبؤ مباشرة بشبكة RGBα معيّنة بعينات مخروطية متقطعة (صورة متعددة المستويات أو MPI [52]) لكل منظر مدخل، ثم يصيّر مناظر جديدة من خلال التركيب ألفا ودمج MPIs القريبة في نقطة المشاهدة الجديدة.

## 6.3 النقاش

نتفوق بشكل كامل على كلا الخطوط الأساسية التي تحسّن أيضاً شبكة منفصلة لكل مشهد (NV و SRN) في جميع السيناريوهات. علاوة على ذلك، ننتج تصييرات متفوقة نوعياً وكمياً مقارنة بـ LLFF (عبر جميع المقاييس باستثناء واحدة) بينما نستخدم فقط صورهم المدخلة كمجموعة تدريبنا بالكامل.

تنتج طريقة SRN هندسة ونسيجاً ناعمين بشكل كبير، وتقتصر قدرتها التمثيلية لتركيب المناظر من خلال اختيار عمق ولون واحد فقط لكل شعاع كاميرا. يستطيع خط الأساس NV التقاط هندسة ومظهر حجميين مفصلين بشكل معقول، ولكن استخدامه لشبكة حجمية صريحة أساسية بدقة 128³ يمنعه من التوسع لتمثيل التفاصيل الدقيقة بدقة عالية. يوفر LLFF تحديداً "دليل أخذ عينات" لعدم تجاوز 64 بكسل من التباين بين المناظر المدخلة، لذلك غالباً ما يفشل في تقدير الهندسة الصحيحة في مجموعات البيانات الاصطناعية التي تحتوي على ما يصل إلى 400-500 بكسل من التباين بين المناظر. بالإضافة إلى ذلك، يمزج LLFF بين تمثيلات مشهد مختلفة لتصيير مناظر مختلفة، مما ينتج عنه عدم اتساق مزعج إدراكياً كما هو واضح في الفيديو التكميلي الخاص بنا.

أكبر المقايضات العملية بين هذه الطرق هي الوقت مقابل المساحة. تستغرق جميع طرق المشهد الواحد المقارنة ما لا يقل عن 12 ساعة للتدريب لكل مشهد. في المقابل، يمكن لـ LLFF معالجة مجموعة بيانات مدخلة صغيرة في أقل من 10 دقائق. ومع ذلك، ينتج LLFF شبكة حجمية ثلاثية الأبعاد كبيرة لكل صورة مدخلة، مما يؤدي إلى متطلبات تخزين هائلة (أكثر من 15 جيجابايت لمشهد "اصطناعي واقعي" واحد). تتطلب طريقتنا 5 ميجابايت فقط لأوزان الشبكة (ضغط نسبي بمقدار 3000× مقارنة بـ LLFF)، وهو أقل من ذاكرة الصور المدخلة وحدها لمشهد واحد من أي من مجموعات بياناتنا.

## 6.4 دراسات الاستئصال

نتحقق من صحة خيارات التصميم والمعاملات الخاصة بخوارزميتنا من خلال دراسة استئصال واسعة في الجدول 2. نقدم النتائج على مشاهد "اصطناعي واقعي 360°" الخاصة بنا. يوضح الصف 9 نموذجنا الكامل كنقطة مرجعية. يوضح الصف 1 نسخة بسيطة من نموذجنا بدون ترميز موضعي (PE) أو اعتماد على المنظر (VD) أو أخذ عينات هرمي (H). في الصفوف 2-4 نزيل هذه المكونات الثلاثة واحداً تلو الآخر من النموذج الكامل، لاحظين أن الترميز الموضعي (الصف 2) والاعتماد على المنظر (الصف 3) يوفران أكبر فائدة كمية متبوعين بأخذ العينات الهرمي (الصف 4). توضح الصفوف 5-6 كيف ينخفض أداؤنا مع انخفاض عدد الصور المدخلة. لاحظ أن أداء طريقتنا باستخدام 25 صورة مدخلة فقط لا يزال يتجاوز NV و SRN و LLFF عبر جميع المقاييس عندما يتم توفير 100 صورة لها (انظر المواد التكميلية). في الصفوف 7-8 نتحقق من صحة اختيارنا للتردد الأقصى L المستخدم في الترميز الموضعي الخاص بنا لـ **x** (يتم قياس التردد الأقصى المستخدم لـ **d** بشكل متناسب). يقلل استخدام 5 ترددات فقط من الأداء، ولكن زيادة عدد الترددات من 10 إلى 15 لا تحسن الأداء. نعتقد أن فائدة زيادة L محدودة بمجرد أن يتجاوز 2^L التردد الأقصى الموجود في الصور المدخلة المعيّنة (حوالي 1024 في بياناتنا).

---

### Translation Notes

- **Figures referenced:** Table 1, Table 2, Figures 6, 8
- **Key terms introduced:** ablation study (دراسة استئصال), baseline (خط الأساس), PSNR (PSNR), SSIM (SSIM), LPIPS (LPIPS), pathtracing (تتبع المسار), forward-facing (متجه للأمام), disparity (تباين), multiplane image / MPI (صورة متعددة المستويات)
- **Equations:** 0
- **Citations:** [24], [28], [41], [42], [52]
- **Special handling:** Tables and quantitative comparisons, dataset descriptions

### Quality Metrics

- Semantic equivalence: 0.87 - Excellent preservation of experimental details
- Technical accuracy: 0.86 - Accurate translation of evaluation terminology
- Readability: 0.84 - Clear presentation of results
- Glossary consistency: 0.83 - Consistent terminology
- **Overall section score:** 0.85
