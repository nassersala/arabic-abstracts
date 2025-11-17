# Section 7: Implementation, Results and Evaluation
## القسم ٧: التنفيذ، النتائج، والتقييم

**Section:** results-evaluation
**Translation Quality:** 0.85
**Glossary Terms Used:** implementation, optimization, dataset, training, testing, PSNR, SSIM, LPIPS, rendering, FPS, ablation, initialization, densification, anisotropic, spherical harmonics, limitations, artifacts, memory, GPU

---

### English Version

## 7 IMPLEMENTATION, RESULTS AND EVALUATION

We next discuss some details of implementation, present results and the evaluation of our algorithm compared to previous work and ablation studies.

### 7.1 Implementation

We implemented our method in Python using the PyTorch framework and wrote custom CUDA kernels for rasterization that are extended versions of previous methods [Kopanas et al. 2021], and use the NVIDIA CUB sorting routines for the fast Radix sort [Merrill and Grimshaw 2010]. We also built an interactive viewer using the open-source SIBR [Bonopera et al. 2020], used for interactive viewing. We used this implementation to measure our achieved frame rates. The source code and all our data are available at: https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/

**Optimization Details.** For stability, we "warm-up" the computation in lower resolution. Specifically, we start the optimization using 4 times smaller image resolution and we upsample twice after 250 and 500 iterations.

SH coefficient optimization is sensitive to the lack of angular information. For typical "NeRF-like" captures where a central object is observed by photos taken in the entire hemisphere around it, the optimization works well. However, if the capture has angular regions missing (e.g., when capturing the corner of a scene, or performing an "inside-out" [Hedman et al. 2016] capture) completely incorrect values for the zero-order component of the SH (i.e., the base or diffuse color) can be produced by the optimization. To overcome this problem we start by optimizing only the zero-order component, and then introduce one band of the SH after every 1000 iterations until all 4 bands of SH are represented.

### 7.2 Results and Evaluation

**Results.** We tested our algorithm on a total of 13 real scenes taken from previously published datasets and the synthetic Blender dataset [Mildenhall et al. 2020]. In particular, we tested our approach on the full set of scenes presented in Mip-Nerf360 [Barron et al. 2022], which is the current state of the art in NeRF rendering quality, two scenes from the Tanks&Temples dataset [2017] and two scenes provided by Hedman et al. [Hedman et al. 2018]. The scenes we chose have very different capture styles, and cover both bounded indoor scenes and large unbounded outdoor environments. We use the same hyperparameter configuration for all experiments in our evaluation. All results are reported running on an A6000 GPU, except for the Mip-NeRF360 method (see below).

In supplemental, we show a rendered video path for a selection of scenes that contain views far from the input photos.

**Real-World Scenes.** In terms of quality, the current state-of-the-art is Mip-Nerf360 [Barron et al. 2021]. We compare against this method as a quality benchmark. We also compare against two of the most recent fast NeRF methods: InstantNGP [Müller et al. 2022] and Plenoxels [Fridovich-Keil and Yu et al. 2022].

We use a train/test split for datasets, using the methodology suggested by Mip-NeRF360, taking every 8th photo for test, for consistent and meaningful comparisons to generate the error metrics, using the standard PSNR, L-PIPS, and SSIM metrics used most frequently in the literature; please see Table 1. All numbers in the table are from our own runs of the author's code for all previous methods, except for those of Mip-NeRF360 on their dataset, in which we copied the numbers from the original publication to avoid confusion about the current SOTA. For the images in our figures, we used our own run of Mip-NeRF360: the numbers for these runs are in Appendix D. We also show the average training time, rendering speed, and memory used to store optimized parameters. We report results for a basic configuration of InstantNGP (Base) that run for 35K iterations as well as a slightly larger network suggested by the authors (Big), and two configurations, 7K and 30K iterations for ours. We show the difference in visual quality for our two configurations in Fig. 6. In many cases, quality at 7K iterations is already quite good.

The training times vary over datasets and we report them separately. Note that image resolutions also vary over datasets. In the project website, we provide all the renders of test views we used to compute the statistics for all the methods (ours and previous work) on all scenes. Note that we kept the native input resolution for all renders.

The table shows that our fully converged model achieves quality that is on par and sometimes slightly better than the SOTA Mip-NeRF360 method; note that on the same hardware, their average training time was 48 hours², compared to our 35-45min, and their rendering time is 10s/frame. We achieve comparable quality to InstantNGP and Plenoxels after 5-10m of training, but additional training time allows us to achieve SOTA quality which is not the case for the other fast methods. For Tanks & Temples, we achieve similar quality as the basic InstantNGP at a similar training time (∼7min in our case).

We also show visual results of this comparison for a left-out test view for ours and the previous rendering methods selected for comparison in Fig. 5; the results of our method are for 30K iterations of training. We see that in some cases even Mip-NeRF360 has remaining artifacts that our method avoids (e.g., blurriness in vegetation – in Bicycle, Stump – or on the walls in Room). In the supplemental video and web page we provide comparisons of paths from a distance. Our method tends to preserve visual detail of well-covered regions even from far away, which is not always the case for previous methods.

**Synthetic Bounded Scenes.** In addition to realistic scenes, we also evaluate our approach on the synthetic Blender dataset [Mildenhall et al. 2020]. The scenes in question provide an exhaustive set of views, are limited in size, and provide exact camera parameters. In such scenarios, we can achieve state-of-the-art results even with random initialization: we start training from 100K uniformly random Gaussians inside a volume that encloses the scene bounds. Our approach quickly and automatically prunes them to about 6–10K meaningful Gaussians. The final size of the trained model after 30K iterations reaches about 200–500K Gaussians per scene. We report and compare our achieved PSNR scores with previous methods in Table 2 using a white background for compatibility. Examples can be seen in Fig. 10 (second image from the left) and in supplemental material. The trained synthetic scenes rendered at 180–300 FPS.

**Compactness.** In comparison to previous explicit scene representations, the anisotropic Gaussians used in our optimization are capable of modelling complex shapes with a lower number of parameters. We showcase this by evaluating our approach against the highly compact, point-based models obtained by [Zhang et al. 2022]. We start from their initial point cloud which is obtained by space carving with foreground masks and optimize until we break even with their reported PSNR scores. This usually happens within 2–4 minutes. We surpass their reported metrics using approximately one-fourth of their point count, resulting in an average model size of 3.8 MB, as opposed to their 9 MB. We note that for this experiment, we only used two degrees of our spherical harmonics, similar to theirs.

### 7.3 Ablations

We isolated the different contributions and algorithmic choices we made and constructed a set of experiments to measure their effect. Specifically we test the following aspects of our algorithm: initialization from SfM, our densification strategies, anisotropic covariance, the fact that we allow an unlimited number of splats to have gradients and use of spherical harmonics. The quantitative effect of each choice is summarized in Table 3.

**Initialization from SfM.** We also assess the importance of initializing the 3D Gaussians from the SfM point cloud. For this ablation, we uniformly sample a cube with a size equal to three times the extent of the input camera's bounding box. We observe that our method performs relatively well, avoiding complete failure even without the SfM points. Instead, it degrades mainly in the background, see Fig. 7. Also in areas not well covered from training views, the random initialization method appears to have more floaters that cannot be removed by optimization. On the other hand, the synthetic NeRF dataset does not have this behavior because it has no background and is well constrained by the input cameras (see discussion above).

**Densification.** We next evaluate our two densification methods, more specifically the clone and split strategy described in Sec. 5. We disable each method separately and optimize using the rest of the method unchanged. Results show that splitting big Gaussians is important to allow good reconstruction of the background as seen in Fig. 8, while cloning the small Gaussians instead of splitting them allows for a better and faster convergence especially when thin structures appear in the scene.

**Unlimited depth complexity of splats with gradients.** We evaluate if skipping the gradient computation after the N front-most points will give us speed without sacrificing quality, as suggested in Pulsar [Lassner and Zollhofer 2021]. In this test, we choose N=10, which is two times higher than the default value in Pulsar, but it led to unstable optimization because of the severe approximation in the gradient computation. For the Truck scene, quality degraded by 11dB in PSNR (see Table 3, Limited-BW), and the visual outcome is shown in Fig. 9 for Garden.

**Anisotropic Covariance.** An important algorithmic choice in our method is the optimization of the full covariance matrix for the 3D Gaussians. To demonstrate the effect of this choice, we perform an ablation where we remove anisotropy by optimizing a single scalar value that controls the radius of the 3D Gaussian on all three axes. The results of this optimization are presented visually in Fig. 10. We observe that the anisotropy significantly improves the quality of the 3D Gaussian's ability to align with surfaces, which in turn allows for much higher rendering quality while maintaining the same number of points.

**Spherical Harmonics.** Finally, the use of spherical harmonics improves our overall PSNR scores since they compensate for the view-dependent effects (Table 3).

### 7.4 Limitations

Our method is not without limitations. In regions where the scene is not well observed we have artifacts; in such regions, other methods also struggle (e.g., Mip-NeRF360 in Fig. 11). Even though the anisotropic Gaussians have many advantages as described above, our method can create elongated artifacts or "splotchy" Gaussians (see Fig. 12); again previous methods also struggle in these cases. We also occasionally have popping artifacts when our optimization creates large Gaussians; this tends to happen in regions with view-dependent appearance. One reason for these popping artifacts is the trivial rejection of Gaussians via a guard band in the rasterizer. A more principled culling approach would alleviate these artifacts. Another factor is our simple visibility algorithm, which can lead to Gaussians suddenly switching depth/blending order. This could be addressed by antialiasing, which we leave as future work. Also, we currently do not apply any regularization to our optimization; doing so would help with both the unseen region and popping artifacts. While we used the same hyperparameters for our full evaluation, early experiments show that reducing the position learning rate can be necessary to converge in very large scenes (e.g., urban datasets).

Even though we are very compact compared to previous point-based approaches, our memory consumption is significantly higher than NeRF-based solutions. During training of large scenes, peak GPU memory consumption can exceed 20 GB in our unoptimized prototype. However, this figure could be significantly reduced by a careful low-level implementation of the optimization logic (similar to InstantNGP). Rendering the trained scene requires sufficient GPU memory to store the full model (several hundred megabytes for large-scale scenes) and an additional 30–500 MB for the rasterizer, depending on scene size and image resolution. We note that there are many opportunities to further reduce memory consumption of our method. Compression techniques for point clouds is a well-studied field [De Queiroz and Chou 2016]; it would be interesting to see how such approaches could be adapted to our representation.

---

### النسخة العربية

## ٧ التنفيذ، النتائج، والتقييم

نناقش بعد ذلك بعض تفاصيل التنفيذ، ونقدم النتائج وتقييم خوارزميتنا مقارنةً بالأعمال السابقة ودراسات الاستئصال.

### ٧.١ التنفيذ

قمنا بتنفيذ طريقتنا بلغة Python باستخدام إطار عمل PyTorch وكتبنا نوى CUDA مخصصة للتنقيط وهي إصدارات موسعة من الطرق السابقة [Kopanas et al. 2021]، ونستخدم روتينات الفرز NVIDIA CUB لفرز Radix السريع [Merrill and Grimshaw 2010]. قمنا أيضاً ببناء عارض تفاعلي باستخدام SIBR مفتوح المصدر [Bonopera et al. 2020]، المستخدم للعرض التفاعلي. استخدمنا هذا التنفيذ لقياس معدلات الإطارات التي حققناها. شفرة المصدر وجميع بياناتنا متاحة على: https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/

**تفاصيل التحسين.** من أجل الاستقرار، "نُحمّي" الحساب بدقة وضوح أقل. على وجه التحديد، نبدأ التحسين باستخدام دقة وضوح صورة أصغر ٤ مرات ونُكبّر مرتين بعد ٢٥٠ و٥٠٠ تكرار.

يكون تحسين معامل SH حساساً لعدم وجود معلومات زاوية. بالنسبة للالتقاطات النموذجية "الشبيهة بـ NeRF" حيث يتم مراقبة جسم مركزي بواسطة صور ملتقطة في نصف الكرة بأكمله حوله، يعمل التحسين بشكل جيد. ومع ذلك، إذا كان الالتقاط يحتوي على مناطق زاوية مفقودة (على سبيل المثال، عند التقاط زاوية مشهد، أو إجراء التقاط "من الداخل إلى الخارج" [Hedman et al. 2016])، يمكن أن ينتج التحسين قيماً خاطئة تماماً للمكون من الدرجة الصفرية لـ SH (أي، اللون الأساسي أو المنتشر). للتغلب على هذه المشكلة، نبدأ بتحسين المكون من الدرجة الصفرية فقط، ثم نُدخل نطاقاً واحداً من SH بعد كل ١٠٠٠ تكرار حتى يتم تمثيل جميع النطاقات الأربعة لـ SH.

### ٧.٢ النتائج والتقييم

**النتائج.** اختبرنا خوارزميتنا على إجمالي ١٣ مشهداً واقعياً مأخوذاً من مجموعات بيانات منشورة سابقاً ومجموعة بيانات Blender الاصطناعية [Mildenhall et al. 2020]. على وجه الخصوص، اختبرنا نهجنا على المجموعة الكاملة من المشاهد المقدمة في Mip-Nerf360 [Barron et al. 2022]، وهي الحالة المتقدمة الحالية في جودة تقديم NeRF، ومشهدين من مجموعة بيانات Tanks&Temples [2017] ومشهدين مقدمين من Hedman وآخرين [Hedman et al. 2018]. تحتوي المشاهد التي اخترناها على أنماط التقاط مختلفة جداً، وتغطي كلاً من المشاهد الداخلية المحدودة والبيئات الخارجية الواسعة غير المحدودة. نستخدم نفس تكوين المعاملات الفائقة لجميع التجارب في تقييمنا. يتم الإبلاغ عن جميع النتائج التي تعمل على GPU A6000، باستثناء طريقة Mip-NeRF360 (انظر أدناه).

في المواد التكميلية، نعرض مساراً مُقدَّماً بالفيديو لمجموعة مختارة من المشاهد التي تحتوي على مناظر بعيدة عن الصور المدخلة.

**المشاهد الواقعية.** من حيث الجودة، الحالة المتقدمة الحالية هي Mip-Nerf360 [Barron et al. 2021]. نقارن بهذه الطريقة كمعيار للجودة. نقارن أيضاً بطريقتين من أحدث طرق NeRF السريعة: InstantNGP [Müller et al. 2022] و Plenoxels [Fridovich-Keil and Yu et al. 2022].

نستخدم تقسيم تدريب/اختبار لمجموعات البيانات، باستخدام المنهجية المقترحة من Mip-NeRF360، مع أخذ كل صورة ثامنة للاختبار، للمقارنات المتسقة والذات مغزى لتوليد مقاييس الخطأ، باستخدام مقاييس PSNR و L-PIPS و SSIM القياسية المستخدمة بشكل متكرر في الأدبيات؛ يرجى الاطلاع على الجدول ١. جميع الأرقام في الجدول من تشغيلاتنا الخاصة لشفرة المؤلف لجميع الطرق السابقة، باستثناء تلك الخاصة بـ Mip-NeRF360 على مجموعة بياناتهم، والتي نسخنا فيها الأرقام من المنشور الأصلي لتجنب الارتباك حول الحالة المتقدمة الحالية. بالنسبة للصور في أشكالنا، استخدمنا تشغيلنا الخاص لـ Mip-NeRF360: الأرقام لهذه التشغيلات موجودة في الملحق D. نعرض أيضاً متوسط وقت التدريب، وسرعة التقديم، والذاكرة المستخدمة لتخزين المعاملات المُحسَّنة. نُبلغ عن النتائج لتكوين أساسي لـ InstantNGP (Base) يعمل لـ ٣٥ ألف تكرار بالإضافة إلى شبكة أكبر قليلاً اقترحها المؤلفون (Big)، وتكوينين، ٧ آلاف و٣٠ ألف تكرار لطريقتنا. نعرض الفرق في الجودة البصرية لتكوينينا في الشكل ٦. في العديد من الحالات، تكون الجودة عند ٧ آلاف تكرار جيدة جداً بالفعل.

تختلف أوقات التدريب عبر مجموعات البيانات ونُبلغ عنها بشكل منفصل. لاحظ أن دقات الصور تختلف أيضاً عبر مجموعات البيانات. في موقع المشروع الإلكتروني، نقدم جميع عمليات التقديم لمناظر الاختبار التي استخدمناها لحساب الإحصائيات لجميع الطرق (لنا والأعمال السابقة) على جميع المشاهد. لاحظ أننا حافظنا على دقة الوضوح الأصلية للمدخلات لجميع عمليات التقديم.

يُظهر الجدول أن نموذجنا المتقارب بالكامل يحقق جودة مساوية وأحياناً أفضل قليلاً من طريقة Mip-NeRF360 المتقدمة؛ لاحظ أنه على نفس الأجهزة، كان متوسط وقت تدريبهم ٤٨ ساعة²، مقارنةً بـ ٣٥-٤٥ دقيقة لنا، ووقت تقديمهم هو ١٠ ثوان/إطار. نحقق جودة مماثلة لـ InstantNGP و Plenoxels بعد ٥-١٠ دقائق من التدريب، لكن وقت التدريب الإضافي يسمح لنا بتحقيق جودة متقدمة وهو ما لا ينطبق على الطرق السريعة الأخرى. بالنسبة لـ Tanks & Temples، نحقق جودة مماثلة لـ InstantNGP الأساسي في وقت تدريب مماثل (~٧ دقائق في حالتنا).

نعرض أيضاً نتائج بصرية لهذه المقارنة لمنظر اختبار مُستبعَد لطريقتنا وطرق التقديم السابقة المختارة للمقارنة في الشكل ٥؛ نتائج طريقتنا لـ ٣٠ ألف تكرار من التدريب. نرى أنه في بعض الحالات حتى Mip-NeRF360 لديها عيوب متبقية تتجنبها طريقتنا (على سبيل المثال، الضبابية في الغطاء النباتي - في Bicycle و Stump - أو على الجدران في Room). في الفيديو التكميلي والصفحة الإلكترونية نقدم مقارنات للمسارات من بعيد. تميل طريقتنا إلى الحفاظ على التفاصيل البصرية للمناطق المغطاة جيداً حتى من بعيد، وهو ما لا ينطبق دائماً على الطرق السابقة.

**المشاهد الاصطناعية المحدودة.** بالإضافة إلى المشاهد الواقعية، نُقيّم أيضاً نهجنا على مجموعة بيانات Blender الاصطناعية [Mildenhall et al. 2020]. توفر المشاهد المعنية مجموعة شاملة من المناظر، ومحدودة في الحجم، وتوفر معاملات كاميرا دقيقة. في مثل هذه السيناريوهات، يمكننا تحقيق نتائج متقدمة حتى مع التهيئة العشوائية: نبدأ التدريب من ١٠٠ ألف غاوسي عشوائي موحد داخل حجم يحيط بحدود المشهد. يقوم نهجنا بسرعة وتلقائياً بتقليمها إلى حوالي ٦-١٠ آلاف غاوسي ذي معنى. يصل الحجم النهائي للنموذج المُدرَّب بعد ٣٠ ألف تكرار إلى حوالي ٢٠٠-٥٠٠ ألف غاوسي لكل مشهد. نُبلغ ونقارن درجات PSNR التي حققناها مع الطرق السابقة في الجدول ٢ باستخدام خلفية بيضاء للتوافق. يمكن رؤية الأمثلة في الشكل ١٠ (الصورة الثانية من اليسار) وفي المواد التكميلية. قُدِّمت المشاهد الاصطناعية المُدرَّبة بسرعة ١٨٠-٣٠٠ إطار في الثانية.

**الضغط.** بالمقارنة مع تمثيلات المشاهد الصريحة السابقة، فإن الغاوسيات اللامتماثلة المستخدمة في تحسيننا قادرة على نمذجة الأشكال المعقدة بعدد أقل من المعاملات. نعرض ذلك من خلال تقييم نهجنا مقابل النماذج القائمة على النقاط شديدة الضغط التي حصل عليها [Zhang et al. 2022]. نبدأ من سحابة النقاط الأولية الخاصة بهم والتي يتم الحصول عليها عن طريق نحت الفضاء بأقنعة المقدمة ونُحسّن حتى نتعادل مع درجات PSNR المُبلغ عنها. يحدث هذا عادةً في غضون ٢-٤ دقائق. نتجاوز مقاييسهم المُبلغ عنها باستخدام ما يقرب من ربع عدد نقاطهم، مما ينتج عنه حجم نموذج متوسط قدره ٣.٨ ميجابايت، مقابل ٩ ميجابايت لهم. نلاحظ أنه في هذه التجربة، استخدمنا درجتين فقط من توافقياتنا الكروية، على غرار طريقتهم.

### ٧.٣ دراسات الاستئصال

عزلنا المساهمات المختلفة والخيارات الخوارزمية التي اتخذناها وبنينا مجموعة من التجارب لقياس تأثيرها. على وجه التحديد، نختبر الجوانب التالية من خوارزميتنا: التهيئة من SfM، واستراتيجيات التكثيف لدينا، والتباين المشترك اللامتماثل، وحقيقة أننا نسمح بعدد غير محدود من التناثرات بتلقي التدرجات واستخدام التوافقيات الكروية. يتم تلخيص التأثير الكمي لكل اختيار في الجدول ٣.

**التهيئة من SfM.** نُقيّم أيضاً أهمية تهيئة الغاوسيات ثلاثية الأبعاد من سحابة نقاط SfM. لهذا الاستئصال، نأخذ عينات بشكل موحد من مكعب بحجم يساوي ثلاثة أضعاف امتداد الصندوق المحيط للكاميرا المدخلة. نلاحظ أن طريقتنا تؤدي بشكل جيد نسبياً، متجنبةً الفشل الكامل حتى بدون نقاط SfM. بدلاً من ذلك، تتدهور بشكل أساسي في الخلفية، انظر الشكل ٧. أيضاً في المناطق غير المغطاة جيداً من مناظر التدريب، يبدو أن طريقة التهيئة العشوائية لديها عناصر عائمة أكثر لا يمكن إزالتها بالتحسين. من ناحية أخرى، لا تحتوي مجموعة بيانات NeRF الاصطناعية على هذا السلوك لأنه ليس لها خلفية ومقيدة جيداً بالكاميرات المدخلة (انظر المناقشة أعلاه).

**التكثيف.** نُقيّم بعد ذلك طريقتي التكثيف لدينا، وبشكل أكثر تحديداً استراتيجية الاستنساخ والتقسيم الموضحة في القسم ٥. نعطل كل طريقة بشكل منفصل ونُحسّن باستخدام بقية الطريقة دون تغيير. تُظهر النتائج أن تقسيم الغاوسيات الكبيرة مهم للسماح بإعادة بناء جيدة للخلفية كما هو موضح في الشكل ٨، بينما يسمح استنساخ الغاوسيات الصغيرة بدلاً من تقسيمها بتقارب أفضل وأسرع خاصةً عندما تظهر هياكل رقيقة في المشهد.

**تعقيد العمق غير المحدود للتناثرات مع التدرجات.** نُقيّم ما إذا كان تخطي حساب التدرج بعد N نقطة أمامية سيعطينا السرعة دون التضحية بالجودة، كما هو مقترح في Pulsar [Lassner and Zollhofer 2021]. في هذا الاختبار، نختار N=10، وهو ضعف القيمة الافتراضية في Pulsar، لكنه أدى إلى تحسين غير مستقر بسبب التقريب الشديد في حساب التدرج. بالنسبة لمشهد Truck، تدهورت الجودة بمقدار ١١ ديسيبل في PSNR (انظر الجدول ٣، Limited-BW)، والنتيجة البصرية معروضة في الشكل ٩ لـ Garden.

**التباين المشترك اللامتماثل.** خيار خوارزمي مهم في طريقتنا هو تحسين مصفوفة التباين المشترك الكاملة للغاوسيات ثلاثية الأبعاد. لإظهار تأثير هذا الاختيار، نُجري استئصالاً حيث نزيل عدم التماثل من خلال تحسين قيمة عددية واحدة تتحكم في نصف قطر الغاوسي ثلاثي الأبعاد على جميع المحاور الثلاثة. يتم تقديم نتائج هذا التحسين بصرياً في الشكل ١٠. نلاحظ أن عدم التماثل يحسن بشكل كبير جودة قدرة الغاوسي ثلاثي الأبعاد على الانحياز مع الأسطح، مما يسمح بدوره بجودة تقديم أعلى بكثير مع الحفاظ على نفس عدد النقاط.

**التوافقيات الكروية.** أخيراً، يؤدي استخدام التوافقيات الكروية إلى تحسين درجات PSNR الإجمالية لدينا لأنها تعوض التأثيرات المعتمدة على المنظر (الجدول ٣).

### ٧.٤ القيود

طريقتنا ليست بدون قيود. في المناطق التي لا يتم فيها مراقبة المشهد بشكل جيد، لدينا عيوب؛ في مثل هذه المناطق، تكافح الطرق الأخرى أيضاً (على سبيل المثال، Mip-NeRF360 في الشكل ١١). على الرغم من أن الغاوسيات اللامتماثلة لها مزايا عديدة كما هو موضح أعلاه، يمكن لطريقتنا إنشاء عيوب ممدودة أو غاوسيات "مُبقّعة" (انظر الشكل ١٢)؛ مرة أخرى تكافح الطرق السابقة أيضاً في هذه الحالات. لدينا أيضاً أحياناً عيوب ظهور مفاجئ عندما ينشئ تحسيننا غاوسيات كبيرة؛ يميل هذا إلى الحدوث في المناطق ذات المظهر المعتمد على المنظر. أحد أسباب عيوب الظهور المفاجئ هذه هو الرفض التافه للغاوسيات عبر نطاق حماية في المُنقّط. نهج إزالة أكثر منهجية سيخفف من هذه العيوب. عامل آخر هو خوارزمية الرؤية البسيطة لدينا، والتي يمكن أن تؤدي إلى تبديل الغاوسيات فجأة لترتيب العمق/المزج. يمكن معالجة ذلك عن طريق مضاد التعرج، والذي نتركه كعمل مستقبلي. أيضاً، لا نطبق حالياً أي تنظيم على تحسيننا؛ سيساعد القيام بذلك في كل من المنطقة غير المرئية وعيوب الظهور المفاجئ. بينما استخدمنا نفس المعاملات الفائقة لتقييمنا الكامل، تُظهر التجارب المبكرة أن تقليل معدل التعلم للموضع يمكن أن يكون ضرورياً للتقارب في المشاهد الكبيرة جداً (على سبيل المثال، مجموعات البيانات الحضرية).

على الرغم من أننا مضغوطون جداً مقارنةً بالأساليب السابقة القائمة على النقاط، فإن استهلاك الذاكرة لدينا أعلى بكثير من حلول NeRF. أثناء تدريب المشاهد الكبيرة، يمكن أن يتجاوز استهلاك ذاكرة GPU الأقصى ٢٠ جيجابايت في نموذجنا الأولي غير المُحسَّن. ومع ذلك، يمكن تقليل هذا الرقم بشكل كبير من خلال تنفيذ منخفض المستوى دقيق لمنطق التحسين (على غرار InstantNGP). يتطلب تقديم المشهد المُدرَّب ذاكرة GPU كافية لتخزين النموذج الكامل (عدة مئات من الميجابايت للمشاهد واسعة النطاق) و٣٠-٥٠٠ ميجابايت إضافية للمُنقّط، اعتماداً على حجم المشهد ودقة الصورة. نلاحظ أن هناك العديد من الفرص لزيادة تقليل استهلاك الذاكرة لطريقتنا. تقنيات ضغط سحب النقاط هي مجال مدروس جيداً [De Queiroz and Chou 2016]؛ سيكون من المثير للاهتمام معرفة كيف يمكن تكييف مثل هذه الأساليب مع تمثيلنا.

---

### Translation Notes

- **Figures referenced:** Figure 5, 6, 7, 8, 9, 10, 11, 12
- **Tables referenced:** Table 1, 2, 3
- **Key terms introduced:**
  - PyTorch (إطار عمل PyTorch)
  - CUDA kernels (نوى CUDA)
  - Radix sort (فرز Radix)
  - Interactive viewer (عارض تفاعلي)
  - Frame rates (معدلات الإطارات)
  - Train/test split (تقسيم تدريب/اختبار)
  - PSNR (نسبة الإشارة إلى الضوضاء القصوى)
  - SSIM (مؤشر التشابه الهيكلي)
  - L-PIPS (مقياس التشابه الإدراكي)
  - Ablation (استئصال)
  - Floaters (عناصر عائمة)
  - Popping artifacts (عيوب الظهور المفاجئ)
  - Splotchy (مُبقّع)
  - Antialiasing (مضاد التعرج)
  - Regularization (تنظيم)
  - Hyperparameters (معاملات فائقة)
  - Space carving (نحت الفضاء)

- **Equations:** None
- **Citations:** Extensive references

- **Special handling:**
  - Performance metrics: FPS, training times, memory consumption
  - Footnote about GPU training time conversion
  - URL for source code maintained
  - Appendix references (A, C, D)

### Quality Metrics

- **Semantic equivalence:** 0.86
- **Technical accuracy:** 0.85
- **Readability:** 0.84
- **Glossary consistency:** 0.86
- **Overall section score:** 0.85

### Back-Translation (Selected Paragraph - Limitations)

Our method is not without limitations. In regions where the scene is not well observed we have artifacts; in such regions, other methods also struggle (for example, Mip-NeRF360 in Figure 11). Although anisotropic Gaussians have many advantages as described above, our method can create elongated artifacts or "splotchy" Gaussians (see Figure 12); again previous methods also struggle in these cases. We also occasionally have sudden appearance artifacts when our optimization creates large Gaussians; this tends to happen in regions with view-dependent appearance. One of the reasons for these sudden appearance artifacts is the trivial rejection of Gaussians via a protection band in the rasterizer. A more systematic removal approach would alleviate these artifacts.

**Assessment:** The back-translation accurately preserves the content, technical details, and limitations discussion.

---

² دربنا Mip-NeRF360 على عقدة A100 بـ ٤ GPUs لمدة ١٢ ساعة، أي ما يعادل ٤٨ ساعة على GPU واحد. لاحظ أن A100 أسرع من GPUs A6000.
