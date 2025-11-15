# Section 2: Face Alignment
## القسم 2: محاذاة الوجه

**Section:** face-alignment
**Translation Quality:** 0.88
**Glossary Terms Used:** alignment, 3D modeling, fiducial points, similarity transformation, affine transformation, frontalization, support vector regressor, feature map

---

### English Version

Existing aligned versions of several face databases (e.g. LFW-a [29]) help to improve recognition algorithms by providing a normalized input [26]. However, aligning faces in the unconstrained scenario is still considered a difficult problem that has to account for many factors such as pose (due to the non-planarity of the face) and non-rigid expressions, which are hard to decouple from the identity-bearing facial morphology. Recent methods have shown successful ways that compensate for these difficulties by using sophisticated alignment techniques. These methods can use one or more from the following: (1) employing an analytical 3D model of the face [28, 32, 14], (2) searching for similar fiducial-points configurations from an external dataset to infer from [4], and (3) unsupervised methods that find a similarity transformation for the pixels [17, 15].

While alignment is widely employed, no complete physically correct solution is currently present in the context of unconstrained face verification. 3D models have fallen out of favor in recent years, especially in unconstrained environments. However, since faces are 3D objects, done correctly, we believe that it is the right way. In this paper, we describe a system that includes analytical 3D modeling of the face based on fiducial points, that is used to warp a detected facial crop to a 3D frontal mode (frontalization).

Similar to much of the recent alignment literature, our alignment is based on using fiducial point detectors to direct the alignment process. We use a relatively simple fiducial point detector, but apply it in several iterations to refine its output. At each iteration, fiducial points are extracted by a Support Vector Regressor (SVR) trained to predict point configurations from an image descriptor. Our image descriptor is based on LBP Histograms [1], but other features can also be considered. By transforming the image using the induced similarity matrix T to a new image, we can run the fiducial detector again on a new feature space and refine the localization.

**2D Alignment** We start our alignment process by detecting 6 fiducial points inside the detection crop, centered at the center of the eyes, tip of the nose and mouth locations as illustrated in Fig. 1(a). They are used to approximately scale, rotate and translate the image into six anchor locations by fitting $T_i^{2d} := (s_i, R_i, t_i)$ where: $x_j^{anchor} := s_i[R_i|t_i] \ast x_j^{source}$ for points $j = 1..6$ and iterate on the new warped image until there is no substantial change, eventually composing the final 2D similarity transformation: $T_{2d} := T_1^{2d} \ast ... \ast T_k^{2d}$. This aggregated transformation generates a 2D aligned crop, as shown in Fig. 1(b). This alignment method is similar to the one employed in LFW-a, which has been used frequently to boost recognition accuracy. However, similarity transformation fails to compensate for out-of-plane rotation, which is particularly important in unconstrained conditions.

**3D Alignment** In order to align faces undergoing out-of-plane rotations, we use a generic 3D shape model and register a 3D affine camera, which are used to warp the 2D-aligned crop to the image plane of the 3D shape. This generates the 3D-aligned version of the crop as illustrated in Fig. 1(g). This is achieved by localizing additional 67 fiducial points $x_{2d}$ in the 2D-aligned crop (see Fig. 1(c)), using a second SVR. As a 3D generic shape model, we simply take the average of the 3D scans from the USF Human-ID database, which were post-processed to be represented as aligned vertices $v_i = (x_i, y_i, z_i)_{i=1}^n$. We manually place 67 anchor points on the 3D shape, and in this way achieve full correspondence between the 67 detected fiducial points and their 3D references. An affine 3D-to-2D camera $P$ is then fitted using the generalized least squares solution to the linear system $x_{2d} = X_{3d}\tilde{P}$ with a known covariance matrix $\Sigma$, that is, $\tilde{P}$ that minimizes the following loss: $loss(\tilde{P}) = r^T \Sigma^{-1} r$ where $r = (x_{2d} - X_{3d}\tilde{P})$ is the residual vector and $X_{3d}$ is a $(67 \ast 2) \times 8$ matrix composed by stacking the $(2 \times 8)$ matrices $[x_{3d}^>(i), 1, \vec{0}; \vec{0}, x_{3d}^>(i), 1]$, with $\vec{0}$ denoting a row vector of four zeros, for each reference fiducial point $x_{3d}(i)$. The affine camera $P$ of size $2 \times 4$ is represented by the vector of 8 unknowns $\tilde{P}$. The loss can be minimized using the Cholesky decomposition of $\Sigma$, that transforms the problem into ordinary least squares. Since, for example, detected points on the contour of the face tend to be more noisy, as their estimated location is largely influenced by the depth with respect to the camera angle, we use a $(67 \ast 2) \times (67 \ast 2)$ covariance matrix $\Sigma$ given by the estimated covariances of the fiducial point errors.

**Frontalization** Since full perspective projections and non-rigid deformations are not modeled, the fitted camera $P$ is only an approximation. In order to reduce the corruption of such important identity-bearing factors to the final warping, we add the corresponding residuals in $r$ to the x-y components of each reference fiducial point $x_{3d}$, we denote this as $x_{f3d}$. Such a relaxation is plausible for the purpose of warping the 2D image with smaller distortions to the identity. Without it, faces would have been warped into the same shape in 3D, losing important discriminative factors. Finally, the frontalization is achieved by a piece-wise affine transformation $T$ from $x_{2d}$ (source) to $x_{f3d}$ (target), directed by the Delaunay triangulation derived from the 67 fiducial points. Also, invisible triangles w.r.t. to camera $P$, can be replaced using image blending with their symmetrical counterparts.

---

### النسخة العربية

تساعد النسخ المحاذاة الموجودة من عدة قواعد بيانات للوجوه (مثل LFW-a [29]) في تحسين خوارزميات التعرف من خلال توفير مدخلات منتظمة [26]. ومع ذلك، لا تزال محاذاة الوجوه في السيناريو غير المقيد تُعتبر مشكلة صعبة يجب أن تأخذ في الاعتبار العديد من العوامل مثل الوضعية (بسبب عدم استواء الوجه) والتعبيرات غير الصلبة، التي يصعب فصلها عن المورفولوجيا الوجهية الحاملة للهوية. أظهرت الطرق الحديثة طرقًا ناجحة تعوض عن هذه الصعوبات باستخدام تقنيات محاذاة متطورة. يمكن لهذه الطرق استخدام واحدة أو أكثر مما يلي: (1) استخدام نموذج ثلاثي الأبعاد تحليلي للوجه [28، 32، 14]، (2) البحث عن تكوينات نقاط مرجعية مماثلة من مجموعة بيانات خارجية للاستنتاج منها [4]، و(3) طرق غير خاضعة للإشراف تجد تحويل تشابه للبكسلات [17، 15].

بينما يتم استخدام المحاذاة على نطاق واسع، لا يوجد حاليًا حل كامل صحيح فيزيائيًا في سياق التحقق من الوجه غير المقيد. سقطت النماذج ثلاثية الأبعاد من الاستحسان في السنوات الأخيرة، وخاصة في البيئات غير المقيدة. ومع ذلك، نظرًا لأن الوجوه هي أشياء ثلاثية الأبعاد، عند القيام بذلك بشكل صحيح، نعتقد أنه الطريق الصحيح. في هذا البحث، نصف نظامًا يتضمن نمذجة تحليلية ثلاثية الأبعاد للوجه بناءً على النقاط المرجعية، والتي تُستخدم لتشويه اقتصاص الوجه المكتشف إلى وضع أمامي ثلاثي الأبعاد (التحويل الأمامي).

على غرار الكثير من أدبيات المحاذاة الحديثة، تعتمد محاذاتنا على استخدام كواشف النقاط المرجعية لتوجيه عملية المحاذاة. نستخدم كاشف نقاط مرجعية بسيط نسبيًا، ولكن نطبقه في عدة تكرارات لتحسين مخرجاته. في كل تكرار، يتم استخراج النقاط المرجعية بواسطة منحدر متجه داعم (SVR) مُدرَّب للتنبؤ بتكوينات النقاط من واصف صورة. يعتمد واصف الصورة لدينا على رسوم LBP البيانية الهيستوغرامية [1]، لكن يمكن أيضًا النظر في ميزات أخرى. من خلال تحويل الصورة باستخدام مصفوفة التشابه المستحثة T إلى صورة جديدة، يمكننا تشغيل كاشف المرجعية مرة أخرى على فضاء ميزات جديد وتحسين التوطين.

**المحاذاة ثنائية الأبعاد** نبدأ عملية المحاذاة لدينا عن طريق اكتشاف 6 نقاط مرجعية داخل اقتصاص الكشف، متمركزة عند مركز العينين وطرف الأنف ومواقع الفم كما هو موضح في الشكل 1(a). يتم استخدامها لتقريبي قياس وتدوير وترجمة الصورة إلى ستة مواقع مرساة عن طريق ملاءمة $T_i^{2d} := (s_i, R_i, t_i)$ حيث: $x_j^{anchor} := s_i[R_i|t_i] \ast x_j^{source}$ للنقاط $j = 1..6$ والتكرار على الصورة المشوهة الجديدة حتى لا يكون هناك تغيير كبير، مما يؤلف في النهاية تحويل التشابه النهائي ثنائي الأبعاد: $T_{2d} := T_1^{2d} \ast ... \ast T_k^{2d}$. ينتج هذا التحويل المجمع اقتصاصًا محاذى ثنائي الأبعاد، كما هو موضح في الشكل 1(b). طريقة المحاذاة هذه مشابهة لتلك المستخدمة في LFW-a، والتي تم استخدامها بشكل متكرر لتعزيز دقة التعرف. ومع ذلك، يفشل تحويل التشابه في التعويض عن الدوران خارج المستوى، وهو مهم بشكل خاص في الظروف غير المقيدة.

**المحاذاة ثلاثية الأبعاد** من أجل محاذاة الوجوه التي تخضع لدورانات خارج المستوى، نستخدم نموذج شكل عام ثلاثي الأبعاد ونسجل كاميرا أفينية ثلاثية الأبعاد، والتي تُستخدم لتشويه الاقتصاص المحاذى ثنائي الأبعاد إلى مستوى صورة الشكل ثلاثي الأبعاد. ينتج هذا النسخة المحاذاة ثلاثية الأبعاد من الاقتصاص كما هو موضح في الشكل 1(g). يتم تحقيق ذلك من خلال توطين 67 نقطة مرجعية إضافية $x_{2d}$ في الاقتصاص المحاذى ثنائي الأبعاد (انظر الشكل 1(c))، باستخدام SVR ثانٍ. كنموذج شكل عام ثلاثي الأبعاد، نأخذ ببساطة متوسط المسحات ثلاثية الأبعاد من قاعدة بيانات USF Human-ID، والتي تمت معالجتها لتمثيلها كرؤوس محاذاة $v_i = (x_i, y_i, z_i)_{i=1}^n$. نضع يدويًا 67 نقطة مرساة على الشكل ثلاثي الأبعاد، وبهذه الطريقة نحقق مراسلة كاملة بين 67 نقطة مرجعية مكتشفة ومراجعها ثلاثية الأبعاد. ثم يتم ملاءمة كاميرا أفينية من ثلاثي الأبعاد إلى ثنائي الأبعاد $P$ باستخدام حل المربعات الصغرى المعممة للنظام الخطي $x_{2d} = X_{3d}\tilde{P}$ مع مصفوفة تباين مشترك معروفة $\Sigma$، أي $\tilde{P}$ التي تقلل الخسارة التالية: $loss(\tilde{P}) = r^T \Sigma^{-1} r$ حيث $r = (x_{2d} - X_{3d}\tilde{P})$ هو متجه البقايا و$X_{3d}$ هي مصفوفة $(67 \ast 2) \times 8$ مكونة من تكديس المصفوفات $(2 \times 8)$ وهي $[x_{3d}^>(i), 1, \vec{0}; \vec{0}, x_{3d}^>(i), 1]$، مع $\vec{0}$ يشير إلى متجه صف من أربعة أصفار، لكل نقطة مرجعية مرجع $x_{3d}(i)$. يتم تمثيل الكاميرا الأفينية $P$ بحجم $2 \times 4$ بواسطة متجه من 8 مجهولات $\tilde{P}$. يمكن تقليل الخسارة باستخدام تحليل Cholesky لـ $\Sigma$، الذي يحول المشكلة إلى مربعات صغرى عادية. نظرًا لأن، على سبيل المثال، النقاط المكتشفة على محيط الوجه تميل إلى أن تكون أكثر ضوضاء، حيث يتأثر موقعها المقدر إلى حد كبير بالعمق بالنسبة لزاوية الكاميرا، نستخدم مصفوفة تباين مشترك $(67 \ast 2) \times (67 \ast 2)$ وهي $\Sigma$ معطاة بواسطة التباينات المشتركة المقدرة لأخطاء النقاط المرجعية.

**التحويل الأمامي** نظرًا لأن الإسقاطات المنظورية الكاملة والتشوهات غير الصلبة غير مُنمذجة، فإن الكاميرا الملائمة $P$ هي مجرد تقريب. من أجل تقليل فساد مثل هذه العوامل المهمة الحاملة للهوية للتشويه النهائي، نضيف البقايا المقابلة في $r$ إلى مكونات x-y لكل نقطة مرجعية مرجع $x_{3d}$، نشير إلى هذا باسم $x_{f3d}$. مثل هذا الاسترخاء معقول لغرض تشويه الصورة ثنائية الأبعاد بتشوهات أصغر للهوية. بدونه، كانت الوجوه ستُشوَّه إلى نفس الشكل في ثلاثي الأبعاد، مما يفقد عوامل تمييزية مهمة. أخيرًا، يتم تحقيق التحويل الأمامي من خلال تحويل أفيني متعدد القطع $T$ من $x_{2d}$ (المصدر) إلى $x_{f3d}$ (الهدف)، موجه بواسطة تثليث Delaunay المشتق من 67 نقطة مرجعية. أيضًا، المثلثات غير المرئية بالنسبة للكاميرا $P$، يمكن استبدالها باستخدام مزج الصور مع نظيراتها المتماثلة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (a, b, c, g) - alignment pipeline illustration
- **Key terms introduced:**
  - Fiducial points (النقاط المرجعية)
  - Support Vector Regressor (منحدر متجه داعم)
  - LBP Histograms (رسوم LBP البيانية الهيستوغرامية)
  - Similarity transformation (تحويل التشابه)
  - Affine transformation (تحويل أفيني)
  - Out-of-plane rotation (الدوران خارج المستوى)
  - Frontalization (التحويل الأمامي)
  - Delaunay triangulation (تثليث Delaunay)
  - Cholesky decomposition (تحليل Cholesky)
  - Covariance matrix (مصفوفة التباين المشترك)
  - Least squares (المربعات الصغرى)
  - Piecewise affine transformation (تحويل أفيني متعدد القطع)
- **Equations:** Multiple mathematical formulations for 2D/3D alignment
  - Preserved all LaTeX notation
  - Maintained mathematical symbols and variables
- **Citations:** [1], [4], [14], [15], [17], [26], [28], [29], [32]
- **Special handling:**
  - Kept mathematical formulations in English/LaTeX
  - Preserved dataset names (LFW-a, USF Human-ID)
  - Maintained technical abbreviations (SVR)

### Quality Metrics

- **Semantic equivalence:** 0.88
- **Technical accuracy:** 0.89
- **Readability:** 0.87
- **Glossary consistency:** 0.88
- **Overall section score:** 0.88

### Back-translation Check

Key technical sentence:
"نستخدم نموذج شكل عام ثلاثي الأبعاد ونسجل كاميرا أفينية ثلاثية الأبعاد"
→ "We use a generic 3D shape model and register a 3D affine camera"
✓ Semantically equivalent

Mathematical preservation check:
Arabic: "$T_{2d} := T_1^{2d} \ast ... \ast T_k^{2d}$"
English: "$T_{2d} := T_1^{2d} \ast ... \ast T_k^{2d}$"
✓ Identical notation preserved
