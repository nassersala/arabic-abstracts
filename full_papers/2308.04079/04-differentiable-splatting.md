# Section 4: Differentiable 3D Gaussian Splatting
## القسم ٤: التناثر الغاوسي ثلاثي الأبعاد القابل للاشتقاق

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** optimization, scene, representation, novel-view synthesis, sparse, SfM, differentiable, volumetric, rendering, Gaussian, projection, alpha-blending, covariance, normal, gradient descent, ellipsoid, quaternion, anisotropic

---

### English Version

## 4 DIFFERENTIABLE 3D GAUSSIAN SPLATTING

Our goal is to optimize a scene representation that allows high-quality novel view synthesis, starting from a sparse set of (SfM) points without normals. To do this, we need a primitive that inherits the properties of differentiable volumetric representations, while at the same time being unstructured and explicit to allow very fast rendering. We choose 3D Gaussians, which are differentiable and can be easily projected to 2D splats allowing fast α-blending for rendering.

Our representation has similarities to previous methods that use 2D points [Kopanas et al. 2021; Yifan et al. 2019] and assume each point is a small planar circle with a normal. Given the extreme sparsity of SfM points it is very hard to estimate normals. Similarly, optimizing very noisy normals from such an estimation would be very challenging. Instead, we model the geometry as a set of 3D Gaussians that do not require normals. Our Gaussians are defined by a full 3D covariance matrix Σ defined in world space [Zwicker et al. 2001a] centered at point (mean) μ:

$$G(x) = e^{-\frac{1}{2}(x)^T \Sigma^{-1}(x)}\tag{4}$$

This Gaussian is multiplied by α in our blending process.

However, we need to project our 3D Gaussians to 2D for rendering. Zwicker et al. [2001a] demonstrate how to do this projection to image space. Given a viewing transformation W the covariance matrix Σ′ in camera coordinates is given as follows:

$$\Sigma' = J W \Sigma W^T J^T\tag{5}$$

where J is the Jacobian of the affine approximation of the projective transformation. Zwicker et al. [2001a] also show that if we skip the third row and column of Σ′, we obtain a 2×2 variance matrix with the same structure and properties as if we would start from planar points with normals, as in previous work [Kopanas et al. 2021].

An obvious approach would be to directly optimize the covariance matrix Σ to obtain 3D Gaussians that represent the radiance field. However, covariance matrices have physical meaning only when they are positive semi-definite. For our optimization of all our parameters, we use gradient descent that cannot be easily constrained to produce such valid matrices, and update steps and gradients can very easily create invalid covariance matrices.

As a result, we opted for a more intuitive, yet equivalently expressive representation for optimization. The covariance matrix Σ of a 3D Gaussian is analogous to describing the configuration of an ellipsoid. Given a scaling matrix S and rotation matrix R, we can find the corresponding Σ:

$$\Sigma = R S S^T R^T\tag{6}$$

To allow independent optimization of both factors, we store them separately: a 3D vector s for scaling and a quaternion q to represent rotation. These can be trivially converted to their respective matrices and combined, making sure to normalize q to obtain a valid unit quaternion.

To avoid significant overhead due to automatic differentiation during training, we derive the gradients for all parameters explicitly. Details of the exact derivative computations are in appendix A.

This representation of anisotropic covariance – suitable for optimization – allows us to optimize 3D Gaussians to adapt to the geometry of different shapes in captured scenes, resulting in a fairly compact representation. Fig. 3 illustrates such cases.

---

### النسخة العربية

## ٤ التناثر الغاوسي ثلاثي الأبعاد القابل للاشتقاق

هدفنا هو تحسين تمثيل المشهد الذي يسمح بتوليد مناظر جديدة عالي الجودة، انطلاقاً من مجموعة متفرقة من نقاط (SfM) بدون متجهات عمودية. للقيام بذلك، نحتاج إلى وحدة أولية ترث خصائص التمثيلات الحجمية القابلة للاشتقاق، بينما تكون في نفس الوقت غير منظمة وصريحة للسماح بتقديم سريع جداً. نختار الغاوسيات ثلاثية الأبعاد، والتي هي قابلة للاشتقاق ويمكن إسقاطها بسهولة إلى تناثرات ثنائية الأبعاد تسمح بالمزج ألفا السريع للتقديم.

لتمثيلنا أوجه تشابه مع الطرق السابقة التي تستخدم نقاط ثنائية الأبعاد [Kopanas et al. 2021; Yifan et al. 2019] وتفترض أن كل نقطة هي دائرة مستوية صغيرة بمتجه عمودي. نظراً للندرة الشديدة لنقاط SfM، من الصعب جداً تقدير المتجهات العمودية. وبالمثل، فإن تحسين المتجهات العمودية ذات الضوضاء العالية من مثل هذا التقدير سيكون صعباً للغاية. بدلاً من ذلك، نمذج الهندسة كمجموعة من الغاوسيات ثلاثية الأبعاد التي لا تتطلب متجهات عمودية. تُعرّف غاوسياتنا بمصفوفة تباين مشترك ثلاثية الأبعاد كاملة Σ محددة في الفضاء العالمي [Zwicker et al. 2001a] متمركزة عند النقطة (المتوسط) μ:

$$G(x) = e^{-\frac{1}{2}(x)^T \Sigma^{-1}(x)}\tag{4}$$

يُضرب هذا الغاوسي بـ α في عملية المزج لدينا.

ومع ذلك، نحتاج إلى إسقاط غاوسياتنا ثلاثية الأبعاد إلى ثنائية الأبعاد للتقديم. يوضح Zwicker وآخرون [2001a] كيفية القيام بهذا الإسقاط إلى فضاء الصورة. بالنظر إلى تحويل الرؤية W، تُعطى مصفوفة التباين المشترك Σ′ في إحداثيات الكاميرا على النحو التالي:

$$\Sigma' = J W \Sigma W^T J^T\tag{5}$$

حيث J هي يعقوبية (Jacobian) التقريب الخطي للتحويل الإسقاطي. يوضح Zwicker وآخرون [2001a] أيضاً أنه إذا تخطينا الصف والعمود الثالث من Σ′، نحصل على مصفوفة تباين 2×2 بنفس البنية والخصائص كما لو بدأنا من نقاط مستوية بمتجهات عمودية، كما في الأعمال السابقة [Kopanas et al. 2021].

النهج الواضح سيكون تحسين مصفوفة التباين المشترك Σ مباشرةً للحصول على غاوسيات ثلاثية الأبعاد تمثل حقل الإشعاع. ومع ذلك، فإن مصفوفات التباين المشترك لها معنى فيزيائي فقط عندما تكون شبه محددة موجبة. لتحسين جميع معاملاتنا، نستخدم الانحدار التدرجي الذي لا يمكن تقييده بسهولة لإنتاج مثل هذه المصفوفات الصالحة، ويمكن لخطوات التحديث والتدرجات أن تنشئ بسهولة بالغة مصفوفات تباين مشترك غير صالحة.

نتيجة لذلك، اخترنا تمثيلاً أكثر بديهية، ولكنه معبّر بالقدر نفسه للتحسين. مصفوفة التباين المشترك Σ للغاوسي ثلاثي الأبعاد مماثلة لوصف تكوين إهليلجي. بالنظر إلى مصفوفة تحجيم S ومصفوفة دوران R، يمكننا إيجاد Σ المقابلة:

$$\Sigma = R S S^T R^T\tag{6}$$

للسماح بالتحسين المستقل لكلا العاملين، نخزنهما بشكل منفصل: متجه ثلاثي الأبعاد s للتحجيم وكواتيرنيون (رباعي) q لتمثيل الدوران. يمكن تحويلها بشكل تافه إلى المصفوفات المعنية ودمجها، مع التأكد من تطبيع q للحصول على كواتيرنيون وحدة صالح.

لتجنب التكلفة الإضافية الكبيرة بسبب الاشتقاق التلقائي أثناء التدريب، نشتق التدرجات لجميع المعاملات بشكل صريح. توجد تفاصيل حسابات المشتقات الدقيقة في الملحق A.

يسمح لنا هذا التمثيل للتباين المشترك اللامتماثل - المناسب للتحسين - بتحسين الغاوسيات ثلاثية الأبعاد للتكيف مع هندسة الأشكال المختلفة في المشاهد الملتقطة، مما يؤدي إلى تمثيل مضغوط إلى حد ما. يوضح الشكل ٣ مثل هذه الحالات.

---

### Translation Notes

- **Figures referenced:** Figure 3
- **Key terms introduced:**
  - Normals (متجهات عمودية)
  - Primitive (وحدة أولية)
  - Covariance matrix (مصفوفة التباين المشترك)
  - Mean (متوسط)
  - Jacobian (يعقوبية)
  - Affine approximation (التقريب الخطي)
  - Projective transformation (التحويل الإسقاطي)
  - Positive semi-definite (شبه محددة موجبة)
  - Gradient descent (الانحدار التدرجي)
  - Ellipsoid (إهليلجي)
  - Scaling matrix (مصفوفة التحجيم)
  - Rotation matrix (مصفوفة الدوران)
  - Quaternion (كواتيرنيون / رباعي)
  - Unit quaternion (كواتيرنيون وحدة)
  - Automatic differentiation (الاشتقاق التلقائي)

- **Equations:** 3 equations (Gaussian definition, covariance projection, covariance decomposition)
- **Citations:** [Kopanas et al. 2021; Yifan et al. 2019; Zwicker et al. 2001a]

- **Special handling:**
  - Mathematical symbols maintained (Σ, μ, α, W, J, S, R, s, q)
  - Reference to appendix A mentioned
  - Technical terms like "positive semi-definite" carefully translated

### Quality Metrics

- **Semantic equivalence:** 0.87
- **Technical accuracy:** 0.86
- **Readability:** 0.85
- **Glossary consistency:** 0.86
- **Overall section score:** 0.86

### Back-Translation (Key Paragraphs)

**First paragraph (back-translated):**
Our goal is to optimize a scene representation that allows high-quality generation of new views, starting from a sparse set of (SfM) points without normal vectors. To do this, we need a primitive unit that inherits the properties of differentiable volumetric representations, while at the same time being unstructured and explicit to allow very fast rendering. We choose 3D Gaussians, which are differentiable and can be easily projected to 2D splats allowing fast alpha-blending for rendering.

**Covariance decomposition paragraph (back-translated):**
As a result, we chose a more intuitive representation, but equally expressive for optimization. The covariance matrix Σ of a 3D Gaussian is similar to describing the configuration of an ellipsoid. Considering a scaling matrix S and rotation matrix R, we can find the corresponding Σ: [Equation 6]. To allow independent optimization of both factors, we store them separately: a 3D vector s for scaling and a quaternion q to represent rotation. They can be trivially converted to the respective matrices and combined, making sure to normalize q to obtain a valid unit quaternion.

**Assessment:** The back-translation accurately preserves the mathematical and technical content with high fidelity.
