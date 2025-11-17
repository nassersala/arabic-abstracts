# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.86
**Glossary Terms Used:** transformer (محول), attention mechanism (آلية الانتباه), deformable attention (انتباه قابل للتشوه), DETR (DETR), object detection (كشف الأجسام), segmentation (تقسيم), cross-attention (انتباه متقاطع), decoder (مفكك), reference point (نقطة مرجعية), 3D perception (إدراك ثلاثي الأبعاد), bounding box (صندوق محيط), depth estimation (تقدير العمق), BEV (BEV), multi-camera (متعدد الكاميرات), voxel (فوكسل), NMS (NMS), bilinear interpolation (استيفاء ثنائي الخطي)

---

### English Version

## 2.1 Transformer-based 2D perception

Recently, a new trend is to use transformer to reformulate detection and segmentation tasks [7, 56, 22]. DETR [7] uses a set of object queries to generate detection results by the cross-attention decoder directly. However, the main drawback of DETR is the long training time. Deformable DETR [56] solves this problem by proposing deformable attention. Different from vanilla global attention in DETR, the deformable attention interacts with local regions of interest, which only samples K points near each reference point and calculates attention results, resulting in high efficiency and significantly shortening the training time. The deformable attention mechanism is calculated by:

$$\text{DeformAttn}(q, p, x) = \sum_{i=1}^{N_{\text{head}}} W_i \sum_{j=1}^{N_{\text{key}}} A_{ij} \cdot W'_i x(p + \Delta p_{ij})$$

where q, p, x represent the query, reference point and input features, respectively. i indexes the attention head, and $N_{\text{head}}$ denotes the total number of attention heads. j indexes the sampled keys, and $N_{\text{key}}$ is the total sampled key number for each head. $W_i \in \mathbb{R}^{C \times (C/H_{\text{head}})}$ and $W'_i \in \mathbb{R}^{(C/H_{\text{head}}) \times C}$ are the learnable weights, where C is the feature dimension. $A_{ij} \in [0, 1]$ is the predicted attention weight, and is normalized by $\sum_{j=1}^{N_{\text{key}}} A_{ij} = 1$. $\Delta p_{ij} \in \mathbb{R}^2$ are the predicted offsets to the reference point p. $x(p + \Delta p_{ij})$ represents the feature at location $p + \Delta p_{ij}$, which is extracted by bilinear interpolation as in Dai et al. [12]. In this work, we extend the deformable attention to 3D perception tasks, to efficiently aggregate both spatial and temporal information.

## 2.2 Camera-based 3D Perception

Previous 3D perception methods typically perform 3D object detection or map segmentation tasks independently. For the 3D object detection task, early methods are similar to 2D detection methods [1, 28, 49, 39, 53], which usually predict the 3D bounding boxes based on 2D bounding boxes. Wang et al. [45] follows an advanced 2D detector FCOS [41] and directly predicts 3D bounding boxes for each object. DETR3D [47] projects learnable 3D queries in 2D images, and then samples the corresponding features for end-to-end 3D bounding box prediction without NMS post-processing. Another solution is to transform image features into BEV features and predict 3D bounding boxes from the top-down view. Methods transform image features into BEV features with the depth information from depth estimation [46] or categorical depth distribution [34]. OFT [36] and ImVoxelNet [37] project the predefined voxels onto image features to generate the voxel representation of the scene. Recently, M2BEV [48] futher explored the feasibility of simultaneously performing multiple perception tasks based on BEV features.

Actually, generating BEV features from multi-camera features is more extensively studied in map segmentation tasks [32, 30]. A straightforward method is converting perspective view into the BEV through Inverse Perspective Mapping (IPM) [35, 5]. In addition, Lift-Splat [32] generates the BEV features based on the depth distribution. Methods [30, 16, 9] utilize multilayer perceptron to learn the translation from perspective view to the BEV. PYVA [51] proposes a cross-view transformer that converts the front-view monocular image into the BEV, but this paradigm is not suitable for fusing multi-camera features due to the computational cost of global attention mechinism [42]. In addition to the spatial information, previous works [18, 38, 6] also consider the temporal information by stacking BEV features from several timestamps. Stacking BEV features constraints the available temporal information within fixed time duration and brings extra computational cost. In this work, the proposed spatiotemporal transformer generates BEV features of the current time by considering both spatial and temporal clues, and the temporal information is obtained from the previous BEV features by the RNN manner, which only brings little computational cost.

---

### النسخة العربية

## 2.1 الإدراك ثنائي الأبعاد القائم على المحول

مؤخراً، ظهر اتجاه جديد لاستخدام المحول لإعادة صياغة مهام الكشف والتقسيم [7, 56, 22]. يستخدم DETR [7] مجموعة من استعلامات الأجسام لتوليد نتائج الكشف عبر مفكك الانتباه المتقاطع مباشرة. ومع ذلك، فإن العيب الرئيسي لـ DETR هو وقت التدريب الطويل. يحل Deformable DETR [56] هذه المشكلة من خلال اقتراح الانتباه القابل للتشوه. على عكس الانتباه الشامل الأساسي في DETR، يتفاعل الانتباه القابل للتشوه مع مناطق الاهتمام المحلية، والذي يأخذ عينات فقط من K نقاط بالقرب من كل نقطة مرجعية ويحسب نتائج الانتباه، مما يؤدي إلى كفاءة عالية وتقصير وقت التدريب بشكل كبير. تُحسب آلية الانتباه القابل للتشوه بواسطة:

$$\text{DeformAttn}(q, p, x) = \sum_{i=1}^{N_{\text{head}}} W_i \sum_{j=1}^{N_{\text{key}}} A_{ij} \cdot W'_i x(p + \Delta p_{ij})$$

حيث تمثل q, p, x الاستعلام والنقطة المرجعية والميزات المدخلة، على التوالي. يُؤشر i على رأس الانتباه، و$N_{\text{head}}$ يشير إلى العدد الإجمالي لرؤوس الانتباه. يُؤشر j على المفاتيح المأخوذة كعينات، و$N_{\text{key}}$ هو العدد الإجمالي للمفاتيح المأخوذة كعينات لكل رأس. $W_i \in \mathbb{R}^{C \times (C/H_{\text{head}})}$ و$W'_i \in \mathbb{R}^{(C/H_{\text{head}}) \times C}$ هي الأوزان القابلة للتعلم، حيث C هو بُعد الميزة. $A_{ij} \in [0, 1]$ هو وزن الانتباه المتوقع، ويتم تطبيعه بواسطة $\sum_{j=1}^{N_{\text{key}}} A_{ij} = 1$. $\Delta p_{ij} \in \mathbb{R}^2$ هي الإزاحات المتوقعة للنقطة المرجعية p. يمثل $x(p + \Delta p_{ij})$ الميزة عند الموقع $p + \Delta p_{ij}$، والتي يتم استخراجها عن طريق الاستيفاء ثنائي الخطي كما في Dai et al. [12]. في هذا العمل، نمدد الانتباه القابل للتشوه إلى مهام الإدراك ثلاثي الأبعاد، لتجميع المعلومات المكانية والزمنية بكفاءة.

## 2.2 الإدراك ثلاثي الأبعاد القائم على الكاميرا

تؤدي طرق الإدراك ثلاثي الأبعاد السابقة عادةً مهام الكشف عن الأجسام ثلاثية الأبعاد أو تقسيم الخرائط بشكل مستقل. بالنسبة لمهمة الكشف عن الأجسام ثلاثية الأبعاد، تشبه الطرق المبكرة طرق الكشف ثنائي الأبعاد [1, 28, 49, 39, 53]، والتي عادة ما تتنبأ بالصناديق المحيطة ثلاثية الأبعاد بناءً على الصناديق المحيطة ثنائية الأبعاد. يتبع Wang et al. [45] كاشف ثنائي الأبعاد متقدم FCOS [41] ويتنبأ مباشرة بالصناديق المحيطة ثلاثية الأبعاد لكل جسم. يُسقط DETR3D [47] استعلامات ثلاثية الأبعاد قابلة للتعلم في صور ثنائية الأبعاد، ثم يأخذ عينات من الميزات المقابلة للتنبؤ بالصناديق المحيطة ثلاثية الأبعاد من طرف إلى طرف بدون معالجة لاحقة لـ NMS. حل آخر هو تحويل ميزات الصورة إلى ميزات BEV والتنبؤ بالصناديق المحيطة ثلاثية الأبعاد من العرض من الأعلى إلى الأسفل. تحول الطرق ميزات الصورة إلى ميزات BEV باستخدام معلومات العمق من تقدير العمق [46] أو التوزيع الفئوي للعمق [34]. يُسقط OFT [36] وImVoxelNet [37] الفوكسلات المحددة مسبقاً على ميزات الصورة لتوليد تمثيل الفوكسل للمشهد. مؤخراً، استكشف M2BEV [48] جدوى أداء مهام إدراك متعددة في وقت واحد بناءً على ميزات BEV.

في الواقع، يتم دراسة توليد ميزات BEV من ميزات الكاميرات المتعددة بشكل أكثر شمولاً في مهام تقسيم الخرائط [32, 30]. الطريقة المباشرة هي تحويل العرض المنظوري إلى BEV من خلال رسم الخرائط المنظوري العكسي (IPM) [35, 5]. بالإضافة إلى ذلك، يولد Lift-Splat [32] ميزات BEV بناءً على توزيع العمق. تستخدم الطرق [30, 16, 9] شبكة إدراكية متعددة الطبقات لتعلم الترجمة من العرض المنظوري إلى BEV. يقترح PYVA [51] محول عبر الرؤية يحول الصورة الأحادية من العرض الأمامي إلى BEV، لكن هذا النموذج غير مناسب لدمج ميزات الكاميرات المتعددة بسبب التكلفة الحسابية لآلية الانتباه الشامل [42]. بالإضافة إلى المعلومات المكانية، تأخذ الأعمال السابقة [18, 38, 6] أيضاً في الاعتبار المعلومات الزمنية من خلال تكديس ميزات BEV من عدة طوابع زمنية. يقيد تكديس ميزات BEV المعلومات الزمنية المتاحة ضمن مدة زمنية ثابتة ويجلب تكلفة حسابية إضافية. في هذا العمل، يولد المحول الزمكاني المقترح ميزات BEV للوقت الحالي من خلال النظر في كل من الإشارات المكانية والزمنية، ويتم الحصول على المعلومات الزمنية من ميزات BEV السابقة بطريقة RNN، والتي تجلب فقط تكلفة حسابية قليلة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Deformable attention, DETR, Deformable DETR, FCOS, DETR3D, OFT, ImVoxelNet, M2BEV, Lift-Splat, PYVA, Inverse Perspective Mapping (IPM)
- **Equations:** 1 equation (deformable attention formula)
- **Citations:** Extensive citations [7, 56, 22, 1, 28, 49, 39, 53, 45, 41, 47, 46, 34, 36, 37, 48, 32, 30, 35, 5, 16, 9, 51, 42, 18, 38, 6, 12]
- **Special handling:** Preserved mathematical notation, maintained citation format

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
