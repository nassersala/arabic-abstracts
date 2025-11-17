# Section 2: Related Work
## القسم ٢: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** reconstruction, rendering, novel-view synthesis, radiance field, neural network, volumetric, ray-marching, MLP, NeRF, point-based, alpha-blending, SfM, MVS, spherical harmonics, differentiable, GPU, CNN, optimization, density, transmittance, covariance, Gaussian

---

### English Version

## 2 RELATED WORK

We first briefly overview traditional reconstruction, then discuss point-based rendering and radiance field work, discussing their similarity; radiance fields are a vast area, so we focus only on directly related work. For complete coverage of the field, please see the excellent recent surveys [Tewari et al. 2022; Xie et al. 2022].

### 2.1 Traditional Scene Reconstruction and Rendering

The first novel-view synthesis approaches were based on light fields, first densely sampled [Gortler et al. 1996; Levoy and Hanrahan 1996] then allowing unstructured capture [Buehler et al. 2001]. The advent of Structure-from-Motion (SfM) [Snavely et al. 2006] enabled an entire new domain where a collection of photos could be used to synthesize novel views. SfM estimates a sparse point cloud during camera calibration, that was initially used for simple visualization of 3D space. Subsequent multi-view stereo (MVS) produced impressive full 3D reconstruction algorithms over the years [Goesele et al. 2007], enabling the development of several view synthesis algorithms [Chaurasia et al. 2013; Eisemann et al. 2008; Hedman et al. 2018; Kopanas et al. 2021]. All these methods re-project and blend the input images into the novel view camera, and use the geometry to guide this re-projection. These methods produced excellent results in many cases, but typically cannot completely recover from unreconstructed regions, or from "over-reconstruction", when MVS generates inexistent geometry. Recent neural rendering algorithms [Tewari et al. 2022] vastly reduce such artifacts and avoid the overwhelming cost of storing all input images on the GPU, outperforming these methods on most fronts.

### 2.2 Neural Rendering and Radiance Fields

Deep learning techniques were adopted early for novel-view synthesis [Flynn et al. 2016; Zhou et al. 2016]; CNNs were used to estimate blending weights [Hedman et al. 2018], or for texture-space solutions [Riegler and Koltun 2020; Thies et al. 2019]. The use of MVS-based geometry is a major drawback of most of these methods; in addition, the use of CNNs for final rendering frequently results in temporal flickering.

Volumetric representations for novel-view synthesis were initiated by Soft3D [Penner and Zhang 2017]; deep-learning techniques coupled with volumetric ray-marching were subsequently proposed [Henzler et al. 2019; Sitzmann et al. 2019] building on a continuous differentiable density field to represent geometry. Rendering using volumetric ray-marching has a significant cost due to the large number of samples required to query the volume. Neural Radiance Fields (NeRFs) [Mildenhall et al. 2020] introduced importance sampling and positional encoding to improve quality, but used a large Multi-Layer Perceptron negatively affecting speed. The success of NeRF has resulted in an explosion of follow-up methods that address quality and speed, often by introducing regularization strategies; the current state-of-the-art in image quality for novel-view synthesis is Mip-NeRF360 [Barron et al. 2022]. While the rendering quality is outstanding, training and rendering times remain extremely high; we are able to equal or in some cases surpass this quality while providing fast training and real-time rendering.

The most recent methods have focused on faster training and/or rendering mostly by exploiting three design choices: the use of spatial data structures to store (neural) features that are subsequently interpolated during volumetric ray-marching, different encodings, and MLP capacity. Such methods include different variants of space discretization [Chen et al. 2022b,a; Fridovich-Keil and Yu et al. 2022; Garbin et al. 2021; Hedman et al. 2021; Reiser et al. 2021; Takikawa et al. 2021; Wu et al. 2022; Yu et al. 2021], codebooks [Takikawa et al. 2022], and encodings such as hash tables [Müller et al. 2022], allowing the use of a smaller MLP or foregoing neural networks completely [Fridovich-Keil and Yu et al. 2022; Sun et al. 2022]. Most notable of these methods are InstantNGP [Müller et al. 2022] which uses a hash grid and an occupancy grid to accelerate computation and a smaller MLP to represent density and appearance; and Plenoxels [Fridovich-Keil and Yu et al. 2022] that use a sparse voxel grid to interpolate a continuous density field, and are able to forgo neural networks altogether. Both rely on Spherical Harmonics: the former to represent directional effects directly, the latter to encode its inputs to the color network. While both provide outstanding results, these methods can still struggle to represent empty space effectively, depending in part on the scene/capture type. In addition, image quality is limited in large part by the choice of the structured grids used for acceleration, and rendering speed is hindered by the need to query many samples for a given ray-marching step. The unstructured, explicit GPU-friendly 3D Gaussians we use achieve faster rendering speed and better quality without neural components.

### 2.3 Point-Based Rendering and Radiance Fields

Point-based methods efficiently render disconnected and unstructured geometry samples (i.e., point clouds) [Gross and Pfister 2011]. In its simplest form, point sample rendering [Grossman and Dally 1998] rasterizes an unstructured set of points with a fixed size, for which it may exploit natively supported point types of graphics APIs [Sainz and Pajarola 2004] or parallel software rasterization on the GPU [Laine and Karras 2011; Schütz et al. 2022]. While true to the underlying data, point sample rendering suffers from holes, causes aliasing, and is strictly discontinuous. Seminal work on high-quality point-based rendering addresses these issues by "splatting" point primitives with an extent larger than a pixel, e.g., circular or elliptic discs, ellipsoids, or surfels [Botsch et al. 2005; Pfister et al. 2000; Ren et al. 2002; Zwicker et al. 2001b].

There has been recent interest in differentiable point-based rendering techniques [Wiles et al. 2020; Yifan et al. 2019]. Points have been augmented with neural features and rendered using a CNN [Aliev et al. 2020; Rückert et al. 2022] resulting in fast or even real-time view synthesis; however they still depend on MVS for the initial geometry, and as such inherit its artifacts, most notably over- or under-reconstruction in hard cases such as featureless/shiny areas or thin structures.

Point-based α-blending and NeRF-style volumetric rendering share essentially the same image formation model. Specifically, the color C is given by volumetric rendering along a ray:

$$C = \sum_{i=1}^{N} T_i (1 - \exp(-\sigma_i \delta_i)) c_i \quad \text{with} \quad T_i = \exp\left(-\sum_{j=1}^{i-1} \sigma_j \delta_j\right),\tag{1}$$

where samples of density σ, transmittance T, and color c are taken along the ray with intervals δᵢ. This can be re-written as

$$C = \sum_{i=1}^{N} T_i \alpha_i c_i,\tag{2}$$

with

$$\alpha_i = (1 - \exp(-\sigma_i \delta_i)) \quad \text{and} \quad T_i = \prod_{j=1}^{i-1} (1 - \alpha_i).$$

A typical neural point-based approach (e.g., [Kopanas et al. 2022, 2021]) computes the color C of a pixel by blending N ordered points overlapping the pixel:

$$C = \sum_{i \in N} c_i \alpha_i \prod_{j=1}^{i-1} (1 - \alpha_j),\tag{3}$$

where cᵢ is the color of each point and αᵢ is given by evaluating a 2D Gaussian with covariance Σ [Yifan et al. 2019] multiplied with a learned per-point opacity.

From Eq. 2 and Eq. 3, we can clearly see that the image formation model is the same. However, the rendering algorithm is very different. NeRFs are a continuous representation implicitly representing empty/occupied space; expensive random sampling is required to find the samples in Eq. 2 with consequent noise and computational expense. In contrast, points are an unstructured, discrete representation that is flexible enough to allow creation, destruction, and displacement of geometry similar to NeRF. This is achieved by optimizing opacity and positions, as shown by previous work [Kopanas et al. 2021], while avoiding the shortcomings of a full volumetric representation.

Pulsar [Lassner and Zollhofer 2021] achieves fast sphere rasterization which inspired our tile-based and sorting renderer. However, given the analysis above, we want to maintain (approximate) conventional α-blending on sorted splats to have the advantages of volumetric representations: Our rasterization respects visibility order in contrast to their order-independent method. In addition, we backpropagate gradients on all splats in a pixel and rasterize anisotropic splats. These elements all contribute to the high visual quality of our results (see Sec. 7.3). In addition, previous methods mentioned above also use CNNs for rendering, which results in temporal instability. Nonetheless, the rendering speed of Pulsar [Lassner and Zollhofer 2021] and ADOP [Rückert et al. 2022] served as motivation to develop our fast rendering solution.

While focusing on specular effects, the diffuse point-based rendering track of Neural Point Catacaustics [Kopanas et al. 2022] overcomes this temporal instability by using an MLP, but still required MVS geometry as input. The most recent method [Zhang et al. 2022] in this category does not require MVS, and also uses SH for directions; however, it can only handle scenes of one object and needs masks for initialization. While fast for small resolutions and low point counts, it is unclear how it can scale to scenes of typical datasets [Barron et al. 2022; Hedman et al. 2018; Knapitsch et al. 2017]. We use 3D Gaussians for a more flexible scene representation, avoiding the need for MVS geometry and achieving real-time rendering thanks to our tile-based rendering algorithm for the projected Gaussians.

A recent approach [Xu et al. 2022] uses points to represent a radiance field with a radial basis function approach. They employ point pruning and densification techniques during optimization, but use volumetric ray-marching and cannot achieve real-time display rates.

In the domain of human performance capture, 3D Gaussians have been used to represent captured human bodies [Rhodin et al. 2015; Stoll et al. 2011]; more recently they have been used with volumetric ray-marching for vision tasks [Wang et al. 2023]. Neural volumetric primitives have been proposed in a similar context [Lombardi et al. 2021]. While these methods inspired the choice of 3D Gaussians as our scene representation, they focus on the specific case of reconstructing and rendering a single isolated object (a human body or face), resulting in scenes with small depth complexity. In contrast, our optimization of anisotropic covariance, our interleaved optimization/density control, and efficient depth sorting for rendering allow us to handle complete, complex scenes including background, both indoors and outdoors and with large depth complexity.

---

### النسخة العربية

## ٢ الأعمال ذات الصلة

نستعرض أولاً بإيجاز إعادة البناء التقليدية، ثم نناقش التقديم القائم على النقاط وأعمال حقول الإشعاع، مناقشين تشابههما؛ حقول الإشعاع مجال واسع، لذلك نركز فقط على الأعمال ذات الصلة المباشرة. للتغطية الكاملة للمجال، يرجى الاطلاع على الدراسات الاستقصائية الحديثة الممتازة [Tewari et al. 2022; Xie et al. 2022].

### ٢.١ إعادة البناء والتقديم التقليدي للمشاهد

كانت أول أساليب توليد المناظر الجديدة قائمة على حقول الضوء، التي تم أخذ عيناتها بكثافة أولاً [Gortler et al. 1996; Levoy and Hanrahan 1996] ثم سمحت بالالتقاط غير المنظم [Buehler et al. 2001]. أدى ظهور البنية من الحركة (SfM) [Snavely et al. 2006] إلى تمكين مجال جديد بالكامل حيث يمكن استخدام مجموعة من الصور لتوليف مناظر جديدة. يُقدّر SfM سحابة نقاط متفرقة أثناء معايرة الكاميرا، والتي استُخدمت في البداية للتصور البسيط للفضاء ثلاثي الأبعاد. أنتج الاستريو متعدد المناظر (MVS) اللاحق خوارزميات مذهلة لإعادة البناء ثلاثي الأبعاد الكامل على مر السنين [Goesele et al. 2007]، مما مكّن من تطوير عدة خوارزميات لتوليف المناظر [Chaurasia et al. 2013; Eisemann et al. 2008; Hedman et al. 2018; Kopanas et al. 2021]. تُعيد جميع هذه الطرق إسقاط ومزج الصور المدخلة في كاميرا المنظر الجديد، وتستخدم الهندسة لتوجيه هذا الإسقاط مجدداً. أنتجت هذه الطرق نتائج ممتازة في كثير من الحالات، لكنها عادةً لا يمكنها التعافي بالكامل من المناطق غير المُعاد بناؤها، أو من "الإفراط في إعادة البناء"، عندما يُولّد MVS هندسة غير موجودة. تُقلل خوارزميات التقديم العصبية الحديثة [Tewari et al. 2022] بشكل كبير من مثل هذه العيوب وتتجنب التكلفة الباهظة لتخزين جميع الصور المدخلة على GPU، متفوقةً على هذه الطرق في معظم الجوانب.

### ٢.٢ التقديم العصبي وحقول الإشعاع

تم اعتماد تقنيات التعلم العميق مبكراً لتوليد المناظر الجديدة [Flynn et al. 2016; Zhou et al. 2016]؛ استُخدمت الشبكات العصبية التلافيفية (CNNs) لتقدير أوزان المزج [Hedman et al. 2018]، أو لحلول فضاء النسيج [Riegler and Koltun 2020; Thies et al. 2019]. يُعد استخدام الهندسة القائمة على MVS عيباً رئيسياً في معظم هذه الطرق؛ بالإضافة إلى ذلك، فإن استخدام CNNs للتقديم النهائي يؤدي في كثير من الأحيان إلى الوميض الزمني.

بدأت التمثيلات الحجمية لتوليد المناظر الجديدة بواسطة Soft3D [Penner and Zhang 2017]؛ اقتُرحت لاحقاً تقنيات التعلم العميق المقترنة بالتتبع الشعاعي الحجمي [Henzler et al. 2019; Sitzmann et al. 2019] بناءً على حقل كثافة مستمر قابل للاشتقاق لتمثيل الهندسة. يكون للتقديم باستخدام التتبع الشعاعي الحجمي تكلفة كبيرة بسبب العدد الكبير من العينات المطلوبة للاستعلام عن الحجم. قدمت حقول الإشعاع العصبية (NeRFs) [Mildenhall et al. 2020] أخذ العينات بالأهمية والترميز الموضعي لتحسين الجودة، لكنها استخدمت بيرسبتروناً متعدد الطبقات كبيراً أثر سلباً على السرعة. أدى نجاح NeRF إلى انفجار في الطرق اللاحقة التي تعالج الجودة والسرعة، غالباً من خلال إدخال استراتيجيات التنظيم؛ الحالة المتقدمة الحالية في جودة الصورة لتوليد المناظر الجديدة هي Mip-NeRF360 [Barron et al. 2022]. بينما تكون جودة التقديم متميزة، تظل أوقات التدريب والتقديم عالية للغاية؛ نحن قادرون على مساواة أو في بعض الحالات تجاوز هذه الجودة مع توفير تدريب سريع وتقديم في الوقت الفعلي.

ركزت الطرق الأحدث على تدريب و/أو تقديم أسرع في الغالب من خلال استغلال ثلاثة خيارات تصميم: استخدام هياكل البيانات المكانية لتخزين الميزات (العصبية) التي يتم استيفاؤها لاحقاً أثناء التتبع الشعاعي الحجمي، والترميزات المختلفة، وسعة MLP. تشمل هذه الطرق متغيرات مختلفة من تقطيع الفضاء [Chen et al. 2022b,a; Fridovich-Keil and Yu et al. 2022; Garbin et al. 2021; Hedman et al. 2021; Reiser et al. 2021; Takikawa et al. 2021; Wu et al. 2022; Yu et al. 2021]، ودفاتر الرموز [Takikawa et al. 2022]، والترميزات مثل جداول الهاش [Müller et al. 2022]، مما يسمح باستخدام MLP أصغر أو التخلي عن الشبكات العصبية تماماً [Fridovich-Keil and Yu et al. 2022; Sun et al. 2022]. الأبرز من هذه الطرق هي InstantNGP [Müller et al. 2022] التي تستخدم شبكة هاش وشبكة إشغال لتسريع الحساب و MLP أصغر لتمثيل الكثافة والمظهر؛ و Plenoxels [Fridovich-Keil and Yu et al. 2022] التي تستخدم شبكة فوكسل متفرقة لاستيفاء حقل كثافة مستمر، وقادرة على التخلي عن الشبكات العصبية تماماً. كلاهما يعتمد على التوافقيات الكروية: الأول لتمثيل التأثيرات الاتجاهية مباشرةً، والثاني لترميز مدخلاته إلى شبكة الألوان. بينما يوفر كلاهما نتائج متميزة، لا تزال هذه الطرق تكافح لتمثيل الفضاء الفارغ بشكل فعال، اعتماداً جزئياً على نوع المشهد/الالتقاط. بالإضافة إلى ذلك، تكون جودة الصورة محدودة إلى حد كبير باختيار الشبكات المنظمة المستخدمة للتسريع، وتُعاق سرعة التقديم بالحاجة للاستعلام عن عينات كثيرة لخطوة تتبع شعاعي معينة. تحقق الغاوسيات ثلاثية الأبعاد غير المنظمة والصريحة والصديقة لـ GPU التي نستخدمها سرعة تقديم أسرع وجودة أفضل دون مكونات عصبية.

### ٢.٣ التقديم القائم على النقاط وحقول الإشعاع

تُقدم الطرق القائمة على النقاط بكفاءة عينات هندسية منفصلة وغير منظمة (أي، سحب النقاط) [Gross and Pfister 2011]. في أبسط أشكالها، يُنقط تقديم عينات النقاط [Grossman and Dally 1998] مجموعة غير منظمة من النقاط بحجم ثابت، والتي قد تستغل أنواع النقاط المدعومة أصلاً في واجهات برمجة التطبيقات الرسومية [Sainz and Pajarola 2004] أو التنقيط البرمجي المتوازي على GPU [Laine and Karras 2011; Schütz et al. 2022]. بينما يكون صحيحاً للبيانات الأساسية، يعاني تقديم عينات النقاط من الثقوب، ويسبب الحواف المسننة، وهو غير متصل بشكل صارم. يعالج العمل الرائد في التقديم عالي الجودة القائم على النقاط هذه المشاكل من خلال "تناثر" وحدات النقاط الأولية بامتداد أكبر من بكسل، على سبيل المثال، الأقراص الدائرية أو الإهليلجية، أو الإهليلجيات، أو السطوح [Botsch et al. 2005; Pfister et al. 2000; Ren et al. 2002; Zwicker et al. 2001b].

كان هناك اهتمام حديث بتقنيات التقديم القائمة على النقاط القابلة للاشتقاق [Wiles et al. 2020; Yifan et al. 2019]. تم تعزيز النقاط بميزات عصبية وتقديمها باستخدام CNN [Aliev et al. 2020; Rückert et al. 2022] مما أدى إلى توليف مناظر سريع أو حتى في الوقت الفعلي؛ ومع ذلك فإنها لا تزال تعتمد على MVS للهندسة الأولية، وبالتالي ترث عيوبها، وأبرزها الإفراط أو النقص في إعادة البناء في الحالات الصعبة مثل المناطق عديمة الملامح/اللامعة أو الهياكل الرقيقة.

يتشارك المزج ألفا القائم على النقاط والتقديم الحجمي بأسلوب NeRF بشكل أساسي نفس نموذج تشكيل الصورة. على وجه التحديد، يُعطى اللون C بالتقديم الحجمي على طول الشعاع:

$$C = \sum_{i=1}^{N} T_i (1 - \exp(-\sigma_i \delta_i)) c_i \quad \text{حيث} \quad T_i = \exp\left(-\sum_{j=1}^{i-1} \sigma_j \delta_j\right),\tag{1}$$

حيث تُؤخذ عينات من الكثافة σ، والنفاذية T، واللون c على طول الشعاع بفواصل δᵢ. يمكن إعادة كتابة هذا على النحو

$$C = \sum_{i=1}^{N} T_i \alpha_i c_i,\tag{2}$$

مع

$$\alpha_i = (1 - \exp(-\sigma_i \delta_i)) \quad \text{و} \quad T_i = \prod_{j=1}^{i-1} (1 - \alpha_i).$$

يحسب نهج نموذجي قائم على النقاط العصبية (على سبيل المثال، [Kopanas et al. 2022, 2021]) اللون C للبكسل من خلال مزج N نقطة مرتبة متداخلة مع البكسل:

$$C = \sum_{i \in N} c_i \alpha_i \prod_{j=1}^{i-1} (1 - \alpha_j),\tag{3}$$

حيث cᵢ هو لون كل نقطة و αᵢ يُعطى بتقييم غاوسي ثنائي الأبعاد بالتباين المشترك Σ [Yifan et al. 2019] مضروباً بعتامة مُتعلَّمة لكل نقطة.

من المعادلة ٢ والمعادلة ٣، يمكننا أن نرى بوضوح أن نموذج تشكيل الصورة هو نفسه. ومع ذلك، فإن خوارزمية التقديم مختلفة جداً. NeRFs هي تمثيل مستمر يمثل ضمنياً الفضاء الفارغ/المشغول؛ يلزم أخذ عينات عشوائية مكلفة لإيجاد العينات في المعادلة ٢ مع ما يترتب على ذلك من ضوضاء ونفقات حسابية. في المقابل، النقاط هي تمثيل منفصل غير منظم مرن بما يكفي للسماح بإنشاء وإزالة وإزاحة الهندسة بشكل مشابه لـ NeRF. يتم تحقيق ذلك من خلال تحسين العتامة والمواضع، كما هو موضح في الأعمال السابقة [Kopanas et al. 2021]، مع تجنب أوجه القصور في التمثيل الحجمي الكامل.

يحقق Pulsar [Lassner and Zollhofer 2021] تنقيطاً سريعاً للكرات مما ألهم مُقدِّمنا القائم على البلاط والفرز. ومع ذلك، بالنظر إلى التحليل أعلاه، نريد الحفاظ على المزج ألفا التقليدي (التقريبي) على التناثرات المفروزة للحصول على مزايا التمثيلات الحجمية: يحترم تنقيطنا ترتيب الرؤية على عكس طريقتهم المستقلة عن الترتيب. بالإضافة إلى ذلك، ننشر التدرجات بشكل عكسي على جميع التناثرات في بكسل ونُنقط تناثرات لامتماثلة. تساهم كل هذه العناصر في الجودة البصرية العالية لنتائجنا (انظر القسم ٧.٣). بالإضافة إلى ذلك، تستخدم الطرق السابقة المذكورة أعلاه أيضاً CNNs للتقديم، مما يؤدي إلى عدم الاستقرار الزمني. ومع ذلك، فإن سرعة التقديم لـ Pulsar [Lassner and Zollhofer 2021] و ADOP [Rückert et al. 2022] كانت بمثابة دافع لتطوير حل التقديم السريع لدينا.

بينما يركز على التأثيرات الطيفية، يتغلب مسار التقديم القائم على النقاط المنتشرة لـ Neural Point Catacaustics [Kopanas et al. 2022] على عدم الاستقرار الزمني هذا باستخدام MLP، لكنه لا يزال يتطلب هندسة MVS كمدخل. الطريقة الأحدث [Zhang et al. 2022] في هذه الفئة لا تتطلب MVS، وتستخدم أيضاً SH للاتجاهات؛ ومع ذلك، يمكنها فقط التعامل مع مشاهد كائن واحد وتحتاج إلى أقنعة للتهيئة. بينما تكون سريعة للدقات المنخفضة وأعداد النقاط المنخفضة، من غير الواضح كيف يمكنها التوسع إلى مشاهد مجموعات البيانات النموذجية [Barron et al. 2022; Hedman et al. 2018; Knapitsch et al. 2017]. نستخدم الغاوسيات ثلاثية الأبعاد لتمثيل مشهد أكثر مرونة، متجنبين الحاجة إلى هندسة MVS ومحققين التقديم في الوقت الفعلي بفضل خوارزمية التقديم القائمة على البلاط للغاوسيات المُسقطة.

يستخدم نهج حديث [Xu et al. 2022] النقاط لتمثيل حقل إشعاع مع نهج دالة الأساس الشعاعي. يستخدمون تقنيات تقليم وتكثيف النقاط أثناء التحسين، لكنهم يستخدمون التتبع الشعاعي الحجمي ولا يمكنهم تحقيق معدلات عرض في الوقت الفعلي.

في مجال التقاط الأداء البشري، تم استخدام الغاوسيات ثلاثية الأبعاد لتمثيل الأجسام البشرية الملتقطة [Rhodin et al. 2015; Stoll et al. 2011]؛ في الآونة الأخيرة تم استخدامها مع التتبع الشعاعي الحجمي لمهام الرؤية [Wang et al. 2023]. تم اقتراح الوحدات الأولية الحجمية العصبية في سياق مماثل [Lombardi et al. 2021]. بينما ألهمت هذه الطرق اختيار الغاوسيات ثلاثية الأبعاد كتمثيل للمشهد لدينا، فإنها تركز على الحالة المحددة لإعادة بناء وتقديم كائن واحد معزول (جسم أو وجه بشري)، مما يؤدي إلى مشاهد ذات تعقيد عمق صغير. في المقابل، يسمح لنا تحسين التباين المشترك اللامتماثل، والتحكم في التحسين/الكثافة المتشابك، والفرز الفعال للعمق للتقديم بالتعامل مع مشاهد كاملة ومعقدة تشمل الخلفية، في الداخل والخارج ومع تعقيد عمق كبير.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Light fields (حقول الضوء)
  - Importance sampling (أخذ العينات بالأهمية)
  - Positional encoding (الترميز الموضعي)
  - Hash grid (شبكة هاش)
  - Occupancy grid (شبكة الإشغال)
  - Sparse voxel grid (شبكة فوكسل متفرقة)
  - Surfels (السطوح)
  - Temporal flickering (الوميض الزمني)
  - Radial basis function (دالة الأساس الشعاعي)
  - Depth complexity (تعقيد العمق)

- **Equations:** 3 equations (volumetric rendering formulation, α-blending equations)
- **Citations:** Extensive references to prior work (40+ citations)

- **Special handling:**
  - Mathematical equations kept in LaTeX with Arabic text for "with" (حيث) and "and" (و)
  - Method names kept in English (NeRF, InstantNGP, Plenoxels, Pulsar, etc.)
  - Technical acronyms maintained (SfM, MVS, CNN, MLP, SH)

### Quality Metrics

- **Semantic equivalence:** 0.87
- **Technical accuracy:** 0.86
- **Readability:** 0.85
- **Glossary consistency:** 0.87
- **Overall section score:** 0.86

### Back-Translation (Selected Paragraph)

**Subsection 2.3, key paragraph (back-translated):**
Point-based α-blending and NeRF-style volumetric rendering essentially share the same image formation model. Specifically, color C is given by volumetric rendering along the ray: [Equation 1] where samples of density σ, transmittance T, and color c are taken along the ray with intervals δᵢ. This can be rewritten as [Equation 2] with [equations for αᵢ and Tᵢ]. A typical neural point-based approach (for example, [Kopanas et al. 2022, 2021]) computes the color C for a pixel through blending N ordered points overlapping with the pixel: [Equation 3] where cᵢ is the color of each point and αᵢ is given by evaluating a 2D Gaussian with covariance Σ [Yifan et al. 2019] multiplied by a learned opacity for each point.

**Assessment:** The back-translation accurately preserves the technical content and mathematical relationships described in the original text.
