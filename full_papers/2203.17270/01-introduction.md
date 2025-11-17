# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** 3D perception (إدراك ثلاثي الأبعاد), autonomous driving (القيادة الذاتية), LiDAR (ليدار), camera-based (قائم على الكاميرا), bird's-eye-view (منظور عين الطائر), transformer (محول), attention mechanism (آلية الانتباه), BEV queries (استعلامات BEV), spatial cross-attention (انتباه متقاطع مكاني), temporal self-attention (انتباه ذاتي زمني), multi-camera (متعدد الكاميرات), object detection (كشف الأجسام), map segmentation (تقسيم الخرائط), depth estimation (تقدير العمق), RNN (شبكة عصبية متكررة), inference (استدلال)

---

### English Version

Perception in 3D space is critical for various applications such as autonomous driving, robotics, etc. Despite the remarkable progress of LiDAR-based methods [43, 20, 54, 50, 8], camera-based approaches [45, 32, 47, 30] have attracted extensive attention in recent years. Apart from the low cost for deployment, cameras own the desirable advantages to detect long-range distance objects and identify vision-based road elements (e.g., traffic lights, stoplines), compared to LiDAR-based counterparts.

Visual perception of the surrounding scene in autonomous driving is expected to predict the 3D bounding boxes or the semantic maps from 2D cues given by multiple cameras. The most straightforward solution is based on the monocular frameworks [45, 44, 31, 35, 3] and cross-camera post-processing. The downside of this framework is that it processes different views separately and cannot capture information across cameras, leading to low performance and efficiency [32, 47].

As an alternative to the monocular frameworks, a more unified framework is extracting holistic representations from multi-camera images. The bird's-eye-view (BEV) is a commonly used representation of the surrounding scene since it clearly presents the location and scale of objects and is suitable for various autonomous driving tasks, such as perception and planning [29]. Although previous map segmentation methods demonstrate BEV's effectiveness [32, 18, 29], BEV-based approaches have not shown significant advantages over other paradigm in 3D object detections [47, 31, 34]. The underlying reason is that the 3D object detection task requires strong BEV features to support accurate 3D bounding box prediction, but generating BEV from the 2D planes is ill-posed. A popular BEV framework that generates BEV features is based on depth information [46, 32, 34], but this paradigm is sensitive to the accuracy of depth values or the depth distributions. The detection performance of BEV-based methods is thus subject to compounding errors [47], and inaccurate BEV features can seriously hurt the final performance. Therefore, we are motivated to design a BEV generating method that does not rely on depth information and can learn BEV features adaptively rather than strictly rely on 3D prior. Transformer, which uses an attention mechanism to aggregate valuable features dynamically, meets our demands conceptually.

Another motivation for using BEV features to perform perception tasks is that BEV is a desirable bridge to connect temporal and spatial space. For the human visual perception system, temporal information plays a crucial role in inferring the motion state of objects and identifying occluded objects, and many works in vision fields have demonstrated the effectiveness of using video data [2, 27, 26, 33, 19]. However, the existing state-of-the-art multi-camera 3D detection methods rarely exploit temporal information. The significant challenges are that autonomous driving is time-critical and objects in the scene change rapidly, and thus simply stacking BEV features of cross timestamps brings extra computational cost and interference information, which might not be ideal. Inspired by recurrent neural networks (RNNs) [17, 10], we utilize the BEV features to deliver temporal information from past to present recurrently, which has the same spirit as the hidden states of RNN models.

To this end, we present a transformer-based bird's-eye-view (BEV) encoder, termed BEVFormer, which can effectively aggregate spatiotemporal features from multi-view cameras and history BEV features. The BEV features generated from the BEVFormer can simultaneously support multiple 3D perception tasks such as 3D object detection and map segmentation, which is valuable for the autonomous driving system. As shown in Fig. 1, our BEVFormer contains three key designs, which are (1) grid-shaped BEV queries to fuse spatial and temporal features via attention mechanisms flexibly, (2) spatial cross-attention module to aggregate the spatial features from multi-camera images, and (3) temporal self-attention module to extract temporal information from history BEV features, which benefits the velocity estimation of moving objects and the detection of heavily occluded objects, while bringing negligible computational overhead. With the unified features generated by BEVFormer, the model can collaborate with different task-specific heads such as Deformable DETR [56] and mask decoder [22], for end-to-end 3D object detection and map segmentation.

**Our main contributions are as follows:**

• We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations. With the unified BEV features, our model can simultaneously support multiple autonomous driving perception tasks, including 3D detection and map segmentation.

• We designed learnable BEV queries along with a spatial cross-attention layer and a temporal self-attention layer to lookup spatial features from cross cameras and temporal features from history BEV, respectively, and then aggregate them into unified BEV features.

• We evaluate the proposed BEVFormer on multiple challenging benchmarks, including nuScenes [4] and Waymo [40]. Our BEVFormer consistently achieves improved performance compared to the prior arts. For example, under a comparable parameters and computation overhead, BEVFormer achieves 56.9% NDS on nuScenes test set, outperforming previous best detection method DETR3D [47] by 9.0 points (56.9% vs. 47.9%). For the map segmentation task, we also achieve the state-of-the-art performance, more than 5.0 points higher than Lift-Splat [32] on the most challenging lane segmentation. We hope this straightforward and strong framework can serve as a new baseline for following 3D perception tasks.

---

### النسخة العربية

يُعد الإدراك في الفضاء ثلاثي الأبعاد أمراً بالغ الأهمية لتطبيقات متنوعة مثل القيادة الذاتية والروبوتات وغيرها. على الرغم من التقدم الملحوظ للطرق القائمة على الليدار [43, 20, 54, 50, 8]، فقد اجتذبت الأساليب القائمة على الكاميرا [45, 32, 47, 30] اهتماماً واسع النطاق في السنوات الأخيرة. بصرف النظر عن التكلفة المنخفضة للنشر، تمتلك الكاميرات مزايا مرغوبة لاكتشاف الأجسام على مسافات بعيدة وتحديد عناصر الطريق القائمة على الرؤية (مثل إشارات المرور وخطوط التوقف)، مقارنة بنظيراتها القائمة على الليدار.

من المتوقع أن يتنبأ الإدراك البصري للمشهد المحيط في القيادة الذاتية بالصناديق المحيطة ثلاثية الأبعاد أو الخرائط الدلالية من الإشارات ثنائية الأبعاد المقدمة من كاميرات متعددة. الحل الأكثر مباشرة يعتمد على أطر العمل الأحادية [45, 44, 31, 35, 3] والمعالجة اللاحقة عبر الكاميرات. العيب في هذا الإطار هو أنه يعالج الرؤى المختلفة بشكل منفصل ولا يمكنه التقاط المعلومات عبر الكاميرات، مما يؤدي إلى انخفاض الأداء والكفاءة [32, 47].

كبديل لأطر العمل الأحادية، يُعد إطار العمل الأكثر توحيداً هو استخراج تمثيلات شاملة من صور الكاميرات المتعددة. يُعتبر منظور عين الطائر (BEV) تمثيلاً شائع الاستخدام للمشهد المحيط لأنه يعرض بوضوح موقع ومقياس الأجسام ومناسب لمهام القيادة الذاتية المختلفة، مثل الإدراك والتخطيط [29]. على الرغم من أن طرق تقسيم الخرائط السابقة تُظهر فعالية BEV [32, 18, 29]، إلا أن الأساليب القائمة على BEV لم تُظهر مزايا كبيرة على نماذج أخرى في عمليات الكشف عن الأجسام ثلاثية الأبعاد [47, 31, 34]. السبب الأساسي هو أن مهمة الكشف عن الأجسام ثلاثية الأبعاد تتطلب ميزات BEV قوية لدعم التنبؤ الدقيق بالصناديق المحيطة ثلاثية الأبعاد، لكن توليد BEV من المستويات ثنائية الأبعاد هو مشكلة سيئة التحديد. يعتمد إطار عمل BEV الشائع الذي يولد ميزات BEV على معلومات العمق [46, 32, 34]، لكن هذا النموذج حساس لدقة قيم العمق أو توزيعات العمق. وبالتالي، يخضع أداء الكشف للطرق القائمة على BEV للأخطاء المتراكمة [47]، ويمكن أن تضر ميزات BEV غير الدقيقة بشكل خطير بالأداء النهائي. لذلك، نحن مدفوعون لتصميم طريقة توليد BEV لا تعتمد على معلومات العمق ويمكنها تعلم ميزات BEV بشكل تكيفي بدلاً من الاعتماد بشكل صارم على المعلومات المسبقة ثلاثية الأبعاد. المحول (Transformer)، الذي يستخدم آلية انتباه لتجميع الميزات القيمة ديناميكياً، يلبي متطلباتنا من الناحية المفاهيمية.

دافع آخر لاستخدام ميزات BEV لأداء مهام الإدراك هو أن BEV جسر مرغوب فيه لربط الفضاء الزمني والمكاني. بالنسبة لنظام الإدراك البصري البشري، تلعب المعلومات الزمنية دوراً حاسماً في استنتاج حالة حركة الأجسام وتحديد الأجسام المحجوبة، وقد أظهرت العديد من الأعمال في مجالات الرؤية فعالية استخدام بيانات الفيديو [2, 27, 26, 33, 19]. ومع ذلك، نادراً ما تستغل طرق الكشف ثلاثي الأبعاد متعددة الكاميرات الحديثة المعلومات الزمنية. التحديات الكبيرة هي أن القيادة الذاتية حرجة من حيث الوقت وأن الأجسام في المشهد تتغير بسرعة، وبالتالي فإن تكديس ميزات BEV عبر الطوابع الزمنية يجلب تكلفة حسابية إضافية ومعلومات تداخل، وهو ما قد لا يكون مثالياً. مستوحى من الشبكات العصبية المتكررة (RNNs) [17, 10]، نستخدم ميزات BEV لتوصيل المعلومات الزمنية من الماضي إلى الحاضر بشكل متكرر، وهو ما له نفس روح الحالات المخفية لنماذج RNN.

تحقيقاً لهذه الغاية، نقدم مشفر منظور عين الطائر (BEV) قائم على المحول، يُسمى BEVFormer، والذي يمكنه تجميع الميزات الزمكانية بشكل فعال من كاميرات متعددة الرؤية وميزات BEV التاريخية. يمكن لميزات BEV المُولدة من BEVFormer دعم مهام إدراك ثلاثية الأبعاد متعددة في وقت واحد، مثل الكشف عن الأجسام ثلاثية الأبعاد وتقسيم الخرائط، وهو أمر ذو قيمة لنظام القيادة الذاتية. كما هو موضح في الشكل 1، يحتوي BEVFormer على ثلاثة تصميمات رئيسية، وهي (1) استعلامات BEV على شكل شبكة لدمج الميزات المكانية والزمنية عبر آليات الانتباه بمرونة، (2) وحدة انتباه متقاطع مكاني لتجميع الميزات المكانية من صور الكاميرات المتعددة، و(3) وحدة انتباه ذاتي زمني لاستخراج المعلومات الزمنية من ميزات BEV التاريخية، مما يفيد تقدير سرعة الأجسام المتحركة واكتشاف الأجسام المحجوبة بشدة، مع إضافة تكلفة حسابية ضئيلة. مع الميزات الموحدة المُولدة بواسطة BEVFormer، يمكن للنموذج التعاون مع رؤوس مهام مختلفة مثل Deformable DETR [56] ومفكك الأقنعة [22]، للكشف عن الأجسام ثلاثية الأبعاد وتقسيم الخرائط من طرف إلى طرف.

**مساهماتنا الرئيسية هي كما يلي:**

• نقترح BEVFormer، وهو مشفر محول زمكاني يُسقط مدخلات الكاميرات المتعددة و/أو الطوابع الزمنية إلى تمثيلات BEV. مع ميزات BEV الموحدة، يمكن لنموذجنا دعم مهام إدراك القيادة الذاتية المتعددة في وقت واحد، بما في ذلك الكشف ثلاثي الأبعاد وتقسيم الخرائط.

• صممنا استعلامات BEV قابلة للتعلم جنباً إلى جنب مع طبقة انتباه متقاطع مكاني وطبقة انتباه ذاتي زمني للبحث عن الميزات المكانية من الكاميرات المتقاطعة والميزات الزمنية من BEV التاريخية، على التوالي، ثم تجميعها في ميزات BEV موحدة.

• نقيّم BEVFormer المُقترح على معايير صعبة متعددة، بما في ذلك nuScenes [4] وWaymo [40]. يحقق BEVFormer باستمرار أداءً محسّناً مقارنة بالأساليب السابقة. على سبيل المثال، تحت معاملات وتكلفة حسابية قابلة للمقارنة، يحقق BEVFormer نسبة 56.9% NDS على مجموعة اختبار nuScenes، متفوقاً على أفضل طريقة كشف سابقة DETR3D [47] بمقدار 9.0 نقاط (56.9% مقابل 47.9%). بالنسبة لمهمة تقسيم الخرائط، نحقق أيضاً أداءً حديثاً، أعلى بأكثر من 5.0 نقاط من Lift-Splat [32] في تقسيم الممرات الأكثر تحدياً. نأمل أن يكون هذا الإطار المباشر والقوي بمثابة خط أساس جديد لمهام الإدراك ثلاثي الأبعاد اللاحقة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (main architecture diagram)
- **Key terms introduced:** Bird's-eye-view (BEV), spatial cross-attention, temporal self-attention, grid-shaped BEV queries, Deformable DETR, monocular frameworks, depth estimation, RNN
- **Equations:** None in introduction
- **Citations:** Multiple references [43, 20, 54, 50, 8], [45, 32, 47, 30], etc.
- **Special handling:** Preserved citation format, maintained technical terminology consistency

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
