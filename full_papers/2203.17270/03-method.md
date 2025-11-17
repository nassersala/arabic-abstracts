# Section 3: BEVFormer
## القسم 3: BEVFormer

**Section:** Method
**Translation Quality:** 0.88
**Glossary Terms Used:** bird's-eye-view (منظور عين الطائر), BEV features (ميزات BEV), transformer (محول), encoder layer (طبقة مشفر), BEV queries (استعلامات BEV), spatial cross-attention (انتباه متقاطع مكاني), temporal self-attention (انتباه ذاتي زمني), attention mechanism (آلية الانتباه), multi-camera (متعدد الكاميرات), backbone (العمود الفقري), ResNet (ResNet), feed-forward network (شبكة أمامية), detection head (رأس الكشف), segmentation head (رأس التقسيم), deformable attention (انتباه قابل للتشوه), reference point (نقطة مرجعية), projection matrix (مصفوفة الإسقاط), ego-motion (حركة الذات), positional embedding (تضمين موضعي)

---

### English Version

Converting multi-camera image features to bird's-eye-view (BEV) features can provide a unified surrounding environment representation for various autonomous driving perception tasks. In this work, we present a new transformer-based framework for BEV generation, which can effectively aggregate spatiotemporal features from multi-view cameras and history BEV features via attention mechanisms.

## 3.1 Overall Architecture

As illustrated in Fig. 2, BEVFormer has 6 encoder layers, each of which follows the conventional structure of transformers [42], except for three tailored designs, namely BEV queries, spatial cross-attention, and temporal self-attention. Specifically, BEV queries are grid-shaped learnable parameters, which is designed to query features in BEV space from multi-camera views via attention mechanisms. Spatial cross-attention and temporal self-attention are attention layers working with BEV queries, which are used to lookup and aggregate spatial features from multi-camera images as well as temporal features from history BEV, according to the BEV query.

During inference, at timestamp t, we feed multi-camera images to the backbone network (e.g., ResNet-101 [15]), and obtain the features $F_t = \{F^i_t\}_{i=1}^{N_{\text{view}}}$ of different camera views, where $F^i_t$ is the feature of the i-th view, $N_{\text{view}}$ is the total number of camera views. At the same time, we preserved the BEV features $B_{t-1}$ at the prior timestamp t−1. In each encoder layer, we first use BEV queries Q to query the temporal information from the prior BEV features $B_{t-1}$ via the temporal self-attention. We then employ BEV queries Q to inquire about the spatial information from the multi-camera features $F_t$ via the spatial cross-attention. After the feed-forward network [42], the encoder layer output the refined BEV features, which is the input of the next encoder layer. After 6 stacking encoder layers, unified BEV features $B_t$ at current timestamp t are generated. Taking the BEV features $B_t$ as input, the 3D detection head and map segmentation head predict the perception results such as 3D bounding boxes and semantic map.

## 3.2 BEV Queries

We predefine a group of grid-shaped learnable parameters $Q \in \mathbb{R}^{H \times W \times C}$ as the queries of BEVFormer, where H, W are the spatial shape of the BEV plane. To be specific, the query $Q_p \in \mathbb{R}^{1 \times C}$ located at $p = (x, y)$ of Q is responsible for the corresponding grid cell region in the BEV plane. Each grid cell in the BEV plane corresponds to a real-world size of s meters. The center of BEV features corresponds to the position of the ego car by default. Following common practices [14], we add learnable positional embedding to BEV queries Q before inputting them to BEVFormer.

## 3.3 Spatial Cross-Attention

Due to the large input scale of multi-camera 3D perception (containing $N_{\text{view}}$ camera views), the computational cost of vanilla multi-head attention [42] is extremely high. Therefore, we develop the spatial cross-attention based on deformable attention [56], which is a resource-efficient attention layer where each BEV query $Q_p$ only interacts with its regions of interest across camera views. However, deformable attention is originally designed for 2D perception, so some adjustments are required for 3D scenes.

As shown in Fig. 2 (b), we first lift each query on the BEV plane to a pillar-like query [20], sample $N_{\text{ref}}$ 3D reference points from the pillar, and then project these points to 2D views. For one BEV query, the projected 2D points can only fall on some views, and other views are not hit. Here, we term the hit views as $\mathcal{V}_{\text{hit}}$. After that, we regard these 2D points as the reference points of the query $Q_p$ and sample the features from the hit views $\mathcal{V}_{\text{hit}}$ around these reference points. Finally, we perform a weighted sum of the sampled features as the output of spatial cross-attention. The process of spatial cross-attention (SCA) can be formulated as:

$$\text{SCA}(Q_p, F_t) = \frac{1}{|\mathcal{V}_{\text{hit}}|} \sum_{i \in \mathcal{V}_{\text{hit}}} \sum_{j=1}^{N_{\text{ref}}} \text{DeformAttn}(Q_p, \mathcal{P}(p, i, j), F^i_t)$$

where i indexes the camera view, j indexes the reference points, and $N_{\text{ref}}$ is the total reference points for each BEV query. $F^i_t$ is the features of the i-th camera view. For each BEV query $Q_p$, we use a project function $\mathcal{P}(p, i, j)$ to get the j-th reference point on the i-th view image.

Next, we introduce how to obtain the reference points on the view image from the projection function $\mathcal{P}$. We first calculate the real world location $(x', y')$ corresponding to the query $Q_p$ located at $p = (x, y)$ of Q as Eqn. 3.

$$x' = (x - \frac{W}{2}) \times s; \quad y' = (y - \frac{H}{2}) \times s$$

where H, W are the spatial shape of BEV queries, s is the size of resolution of BEV's grids, and $(x', y')$ are the coordinates where the position of ego car is the origin. In 3D space, the objects located at $(x', y')$ will appear at the height of $z'$ on the z-axis. So we predefine a set of anchor heights $\{z'_j\}_{j=1}^{N_{\text{ref}}}$ to make sure we can capture clues that appeared at different heights. In this way, for each query $Q_p$, we obtain a pillar of 3D reference points $(x', y', z'_j)_{j=1}^{N_{\text{ref}}}$. Finally, we project the 3D reference points to different image views through the projection matrix of cameras, which can be written as:

$$\mathcal{P}(p, i, j) = (x_{ij}, y_{ij})$$
$$\text{where } z_{ij} \cdot [x_{ij} \quad y_{ij} \quad 1]^T = T_i \cdot [x' \quad y' \quad z'_j \quad 1]^T$$

Here, $\mathcal{P}(p, i, j)$ is the 2D point on i-th view projected from j-th 3D point $(x', y', z'_j)$, $T_i \in \mathbb{R}^{3 \times 4}$ is the known projection matrix of the i-th camera.

## 3.4 Temporal Self-Attention

In addition to spatial information, temporal information is also crucial for the visual system to understand the surrounding environment [27]. For example, it is challenging to infer the velocity of moving objects or detect highly occluded objects from static images without temporal clues. To address this problem, we design temporal self-attention, which can represent the current environment by incorporating history BEV features.

Given the BEV queries Q at current timestamp t and history BEV features $B_{t-1}$ preserved at timestamp t−1, we first align $B_{t-1}$ to Q according to ego-motion to make the features at the same grid correspond to the same real-world location. Here, we denote the aligned history BEV features $B_{t-1}$ as $B'_{t-1}$. However, from times t − 1 to t, movable objects travel in the real world with various offsets. It is challenging to construct the precise association of the same objects between the BEV features of different times. Therefore, we model this temporal connection between features through the temporal self-attention (TSA) layer, which can be written as follows:

$$\text{TSA}(Q_p, \{Q, B'_{t-1}\}) = \sum_{V \in \{Q, B'_{t-1}\}} \text{DeformAttn}(Q_p, p, V)$$

where $Q_p$ denotes the BEV query located at $p = (x, y)$. In addition, different from the vanilla deformable attention, the offsets $\Delta p$ in temporal self-attention are predicted by the concatenation of Q and $B'_{t-1}$. Specially, for the first sample of each sequence, the temporal self-attention will degenerate into a self-attention without temporal information, where we replace the BEV features $\{Q, B'_{t-1}\}$ with duplicate BEV queries $\{Q, Q\}$.

Compared to simply stacking BEV in [18, 38, 6], our temporal self-attention can more effectively model long temporal dependency. BEVFormer extracts temporal information from the previous BEV features rather than multiple stacking BEV features, thus requiring less computational cost and suffering less disturbing information.

## 3.5 Applications of BEV Features

Since the BEV features $B_t \in \mathbb{R}^{H \times W \times C}$ is a versatile 2D feature map that can be used for various autonomous driving perception tasks, the 3D object detection and map segmentation task heads can be developed based on 2D perception methods [56, 22] with minor modifications.

**For 3D object detection**, we design an end-to-end 3D detection head based on the 2D detector Deformable DETR [56]. The modifications include using single-scale BEV features $B_t$ as the input of the decoder, predicting 3D bounding boxes and velocity rather than 2D bounding boxes, and only using L1 loss to supervise 3D bounding box regression. With the detection head, our model can end-to-end predict 3D bounding boxes and velocity without the NMS post-processing.

**For map segmentation**, we design a map segmentation head based on a 2D segmentation method Panoptic SegFormer [22]. Since the map segmentation based on the BEV is basically the same as the common semantic segmentation, we utilize the mask decoder of [22] and class-fixed queries to target each semantic category, including the car, vehicles, road (drivable area), and lane.

## 3.6 Implementation Details

**Training Phase.** For each sample at timestamp t, we randomly sample another 3 samples from the consecutive sequence of the past 2 seconds, and this random sampling strategy can augment the diversity of ego-motion [57]. We denote the timestamps of these four samples as t−3, t−2, t−1 and t. For the samples of the first three timestamps, they are responsible for recurrently generating the BEV features $\{B_{t-3}, B_{t-2}, B_{t-1}\}$ and this phase requires no gradients. For the first sample at timestamp t−3, there is no previous BEV features, and temporal self-attention degenerate into self-attention. At the time t, the model generates the BEV features $B_t$ based on both multi-camera inputs and the prior BEV features $B_{t-1}$, so that $B_t$ contains the temporal and spatial clues crossing the four samples. Finally, we feed the BEV features $B_t$ into the detection and segmentation heads and compute the corresponding loss functions.

**Inference Phase.** During the inference phase, we evaluate each frame of the video sequence in chronological order. The BEV features of the previous timestamp are saved and used for the next, and this online inference strategy is time-efficient and consistent with practical applications. Although we utilize temporal information, our inference speed is still comparable with other methods [45, 47].

---

### النسخة العربية

يمكن أن يوفر تحويل ميزات صور الكاميرات المتعددة إلى ميزات منظور عين الطائر (BEV) تمثيلاً موحداً للبيئة المحيطة لمهام الإدراك المختلفة للقيادة الذاتية. في هذا العمل، نقدم إطار عمل جديد قائم على المحول لتوليد BEV، والذي يمكنه تجميع الميزات الزمكانية بشكل فعال من كاميرات متعددة الرؤية وميزات BEV التاريخية عبر آليات الانتباه.

## 3.1 المعمارية الشاملة

كما هو موضح في الشكل 2، يحتوي BEVFormer على 6 طبقات مشفر، كل منها يتبع البنية التقليدية للمحولات [42]، باستثناء ثلاثة تصميمات مخصصة، وهي استعلامات BEV والانتباه المتقاطع المكاني والانتباه الذاتي الزمني. على وجه التحديد، استعلامات BEV هي معاملات قابلة للتعلم على شكل شبكة، والتي صُممت للاستعلام عن الميزات في فضاء BEV من رؤى الكاميرات المتعددة عبر آليات الانتباه. الانتباه المتقاطع المكاني والانتباه الذاتي الزمني هما طبقتا انتباه تعملان مع استعلامات BEV، والتي تُستخدم للبحث عن الميزات المكانية من صور الكاميرات المتعددة وكذلك الميزات الزمنية من BEV التاريخية وتجميعها، وفقاً لاستعلام BEV.

أثناء الاستدلال، في الطابع الزمني t، نُدخل صور الكاميرات المتعددة إلى شبكة العمود الفقري (مثل ResNet-101 [15])، ونحصل على الميزات $F_t = \{F^i_t\}_{i=1}^{N_{\text{view}}}$ لرؤى الكاميرات المختلفة، حيث $F^i_t$ هي ميزة الرؤية الـ i، $N_{\text{view}}$ هو العدد الإجمالي لرؤى الكاميرا. في الوقت نفسه، نحتفظ بميزات BEV $B_{t-1}$ في الطابع الزمني السابق t−1. في كل طبقة مشفر، نستخدم أولاً استعلامات BEV Q للاستعلام عن المعلومات الزمنية من ميزات BEV السابقة $B_{t-1}$ عبر الانتباه الذاتي الزمني. ثم نستخدم استعلامات BEV Q للاستفسار عن المعلومات المكانية من ميزات الكاميرات المتعددة $F_t$ عبر الانتباه المتقاطع المكاني. بعد الشبكة الأمامية [42]، تُخرج طبقة المشفر ميزات BEV المُنقّحة، والتي هي مدخل طبقة المشفر التالية. بعد 6 طبقات مشفر متراصة، يتم توليد ميزات BEV الموحدة $B_t$ في الطابع الزمني الحالي t. بأخذ ميزات BEV $B_t$ كمدخل، يتنبأ رأس الكشف ثلاثي الأبعاد ورأس تقسيم الخرائط بنتائج الإدراك مثل الصناديق المحيطة ثلاثية الأبعاد والخريطة الدلالية.

## 3.2 استعلامات BEV

نُحدد مسبقاً مجموعة من المعاملات القابلة للتعلم على شكل شبكة $Q \in \mathbb{R}^{H \times W \times C}$ كاستعلامات لـ BEVFormer، حيث H, W هما الشكل المكاني لمستوى BEV. على وجه التحديد، الاستعلام $Q_p \in \mathbb{R}^{1 \times C}$ الموجود عند $p = (x, y)$ من Q مسؤول عن منطقة خلية الشبكة المقابلة في مستوى BEV. تتوافق كل خلية شبكة في مستوى BEV مع حجم في العالم الحقيقي يبلغ s متر. يتوافق مركز ميزات BEV مع موقع السيارة الذاتية بشكل افتراضي. باتباع الممارسات الشائعة [14]، نضيف تضميناً موضعياً قابلاً للتعلم إلى استعلامات BEV Q قبل إدخالها إلى BEVFormer.

## 3.3 الانتباه المتقاطع المكاني

بسبب مقياس المدخلات الكبير للإدراك ثلاثي الأبعاد متعدد الكاميرات (يحتوي على $N_{\text{view}}$ رؤى كاميرا)، فإن التكلفة الحسابية للانتباه متعدد الرؤوس الأساسي [42] عالية للغاية. لذلك، نطور الانتباه المتقاطع المكاني بناءً على الانتباه القابل للتشوه [56]، وهو طبقة انتباه فعالة في الموارد حيث يتفاعل كل استعلام BEV $Q_p$ فقط مع مناطق الاهتمام الخاصة به عبر رؤى الكاميرا. ومع ذلك، صُمم الانتباه القابل للتشوه في الأصل للإدراك ثنائي الأبعاد، لذا يلزم إجراء بعض التعديلات للمشاهد ثلاثية الأبعاد.

كما هو موضح في الشكل 2 (ب)، نرفع أولاً كل استعلام على مستوى BEV إلى استعلام يشبه العمود [20]، ونأخذ عينات من $N_{\text{ref}}$ نقاط مرجعية ثلاثية الأبعاد من العمود، ثم نُسقط هذه النقاط على رؤى ثنائية الأبعاد. بالنسبة لاستعلام BEV واحد، يمكن أن تقع النقاط ثنائية الأبعاد المُسقطة فقط على بعض الرؤى، ولا تُصاب الرؤى الأخرى. هنا، نُسمي الرؤى المُصابة بـ $\mathcal{V}_{\text{hit}}$. بعد ذلك، نعتبر هذه النقاط ثنائية الأبعاد كنقاط مرجعية للاستعلام $Q_p$ ونأخذ عينات من الميزات من الرؤى المُصابة $\mathcal{V}_{\text{hit}}$ حول هذه النقاط المرجعية. أخيراً، نُجري مجموعاً مرجحاً للميزات المأخوذة كعينات كمخرج للانتباه المتقاطع المكاني. يمكن صياغة عملية الانتباه المتقاطع المكاني (SCA) على النحو التالي:

$$\text{SCA}(Q_p, F_t) = \frac{1}{|\mathcal{V}_{\text{hit}}|} \sum_{i \in \mathcal{V}_{\text{hit}}} \sum_{j=1}^{N_{\text{ref}}} \text{DeformAttn}(Q_p, \mathcal{P}(p, i, j), F^i_t)$$

حيث يؤشر i على رؤية الكاميرا، يؤشر j على النقاط المرجعية، و$N_{\text{ref}}$ هو إجمالي النقاط المرجعية لكل استعلام BEV. $F^i_t$ هي ميزات رؤية الكاميرا الـ i. لكل استعلام BEV $Q_p$، نستخدم دالة إسقاط $\mathcal{P}(p, i, j)$ للحصول على النقطة المرجعية الـ j على صورة الرؤية الـ i.

بعد ذلك، نقدم كيفية الحصول على النقاط المرجعية على صورة الرؤية من دالة الإسقاط $\mathcal{P}$. نحسب أولاً الموقع في العالم الحقيقي $(x', y')$ المقابل للاستعلام $Q_p$ الموجود عند $p = (x, y)$ من Q كما في المعادلة 3.

$$x' = (x - \frac{W}{2}) \times s; \quad y' = (y - \frac{H}{2}) \times s$$

حيث H, W هما الشكل المكاني لاستعلامات BEV، s هو حجم دقة شبكات BEV، و$(x', y')$ هي الإحداثيات حيث موقع السيارة الذاتية هو الأصل. في الفضاء ثلاثي الأبعاد، ستظهر الأجسام الموجودة عند $(x', y')$ على ارتفاع $z'$ على المحور z. لذا نُحدد مسبقاً مجموعة من ارتفاعات المرساة $\{z'_j\}_{j=1}^{N_{\text{ref}}}$ للتأكد من أننا يمكننا التقاط الإشارات التي ظهرت على ارتفاعات مختلفة. بهذه الطريقة، لكل استعلام $Q_p$، نحصل على عمود من النقاط المرجعية ثلاثية الأبعاد $(x', y', z'_j)_{j=1}^{N_{\text{ref}}}$. أخيراً، نُسقط النقاط المرجعية ثلاثية الأبعاد على رؤى الصور المختلفة من خلال مصفوفة الإسقاط للكاميرات، والتي يمكن كتابتها على النحو التالي:

$$\mathcal{P}(p, i, j) = (x_{ij}, y_{ij})$$
$$\text{حيث } z_{ij} \cdot [x_{ij} \quad y_{ij} \quad 1]^T = T_i \cdot [x' \quad y' \quad z'_j \quad 1]^T$$

هنا، $\mathcal{P}(p, i, j)$ هي النقطة ثنائية الأبعاد على الرؤية الـ i المُسقطة من النقطة ثلاثية الأبعاد الـ j $(x', y', z'_j)$، $T_i \in \mathbb{R}^{3 \times 4}$ هي مصفوفة الإسقاط المعروفة للكاميرا الـ i.

## 3.4 الانتباه الذاتي الزمني

بالإضافة إلى المعلومات المكانية، تُعد المعلومات الزمنية أيضاً حاسمة للنظام البصري لفهم البيئة المحيطة [27]. على سبيل المثال، من الصعب استنتاج سرعة الأجسام المتحركة أو اكتشاف الأجسام المحجوبة بشدة من الصور الثابتة بدون إشارات زمنية. لمعالجة هذه المشكلة، نُصمم الانتباه الذاتي الزمني، والذي يمكنه تمثيل البيئة الحالية من خلال دمج ميزات BEV التاريخية.

بالنظر إلى استعلامات BEV Q في الطابع الزمني الحالي t وميزات BEV التاريخية $B_{t-1}$ المحفوظة في الطابع الزمني t−1، نُوائم أولاً $B_{t-1}$ مع Q وفقاً لحركة الذات لجعل الميزات في نفس الشبكة تتوافق مع نفس الموقع في العالم الحقيقي. هنا، نرمز إلى ميزات BEV التاريخية المُواءمة $B_{t-1}$ بـ $B'_{t-1}$. ومع ذلك، من الأوقات t − 1 إلى t، تنتقل الأجسام المتحركة في العالم الحقيقي بإزاحات مختلفة. من الصعب بناء الارتباط الدقيق لنفس الأجسام بين ميزات BEV في أوقات مختلفة. لذلك، نُنمذج هذا الاتصال الزمني بين الميزات من خلال طبقة الانتباه الذاتي الزمني (TSA)، والتي يمكن كتابتها على النحو التالي:

$$\text{TSA}(Q_p, \{Q, B'_{t-1}\}) = \sum_{V \in \{Q, B'_{t-1}\}} \text{DeformAttn}(Q_p, p, V)$$

حيث يشير $Q_p$ إلى استعلام BEV الموجود عند $p = (x, y)$. بالإضافة إلى ذلك، على عكس الانتباه القابل للتشوه الأساسي، يتم التنبؤ بالإزاحات $\Delta p$ في الانتباه الذاتي الزمني من خلال تسلسل Q و$B'_{t-1}$. خاصة، بالنسبة للعينة الأولى من كل تسلسل، سيتحول الانتباه الذاتي الزمني إلى انتباه ذاتي بدون معلومات زمنية، حيث نستبدل ميزات BEV $\{Q, B'_{t-1}\}$ باستعلامات BEV مكررة $\{Q, Q\}$.

مقارنة بتكديس BEV ببساطة في [18, 38, 6]، يمكن للانتباه الذاتي الزمني لدينا نمذجة التبعية الزمنية الطويلة بشكل أكثر فعالية. يستخرج BEVFormer المعلومات الزمنية من ميزات BEV السابقة بدلاً من ميزات BEV المتراصة المتعددة، وبالتالي يتطلب تكلفة حسابية أقل ويعاني من معلومات مُزعجة أقل.

## 3.5 تطبيقات ميزات BEV

نظراً لأن ميزات BEV $B_t \in \mathbb{R}^{H \times W \times C}$ هي خريطة ميزات ثنائية الأبعاد متعددة الاستخدامات يمكن استخدامها لمهام الإدراك المختلفة للقيادة الذاتية، يمكن تطوير رؤوس مهام الكشف عن الأجسام ثلاثية الأبعاد وتقسيم الخرائط بناءً على طرق الإدراك ثنائي الأبعاد [56, 22] مع تعديلات طفيفة.

**بالنسبة للكشف عن الأجسام ثلاثية الأبعاد**، نُصمم رأس كشف ثلاثي الأبعاد من طرف إلى طرف بناءً على الكاشف ثنائي الأبعاد Deformable DETR [56]. تتضمن التعديلات استخدام ميزات BEV أحادية المقياس $B_t$ كمدخل للمفكك، والتنبؤ بالصناديق المحيطة ثلاثية الأبعاد والسرعة بدلاً من الصناديق المحيطة ثنائية الأبعاد، واستخدام خسارة L1 فقط للإشراف على انحدار الصندوق المحيط ثلاثي الأبعاد. مع رأس الكشف، يمكن لنموذجنا التنبؤ من طرف إلى طرف بالصناديق المحيطة ثلاثية الأبعاد والسرعة بدون معالجة لاحقة لـ NMS.

**بالنسبة لتقسيم الخرائط**، نُصمم رأس تقسيم خرائط بناءً على طريقة تقسيم ثنائية الأبعاد Panoptic SegFormer [22]. نظراً لأن تقسيم الخرائط بناءً على BEV هو في الأساس نفس التقسيم الدلالي الشائع، فإننا نستخدم مفكك الأقنعة من [22] واستعلامات ثابتة الفئة لاستهداف كل فئة دلالية، بما في ذلك السيارة والمركبات والطريق (المنطقة القابلة للقيادة) والممر.

## 3.6 تفاصيل التنفيذ

**مرحلة التدريب.** لكل عينة في الطابع الزمني t، نأخذ عينات عشوائية من 3 عينات أخرى من التسلسل المتتالي للثانيتين الماضيتين، ويمكن لاستراتيجية أخذ العينات العشوائية هذه زيادة تنوع حركة الذات [57]. نرمز إلى الطوابع الزمنية لهذه العينات الأربع بـ t−3, t−2, t−1 و t. بالنسبة لعينات الطوابع الزمنية الثلاثة الأولى، فهي مسؤولة عن توليد ميزات BEV $\{B_{t-3}, B_{t-2}, B_{t-1}\}$ بشكل متكرر وهذه المرحلة لا تتطلب تدرجات. بالنسبة للعينة الأولى في الطابع الزمني t−3، لا توجد ميزات BEV سابقة، ويتحول الانتباه الذاتي الزمني إلى انتباه ذاتي. في الوقت t، يولد النموذج ميزات BEV $B_t$ بناءً على كل من مدخلات الكاميرات المتعددة وميزات BEV السابقة $B_{t-1}$، بحيث تحتوي $B_t$ على الإشارات الزمنية والمكانية التي تعبر العينات الأربع. أخيراً، نُدخل ميزات BEV $B_t$ إلى رؤوس الكشف والتقسيم ونحسب دوال الخسارة المقابلة.

**مرحلة الاستدلال.** أثناء مرحلة الاستدلال، نُقيّم كل إطار من تسلسل الفيديو بترتيب زمني. يتم حفظ ميزات BEV للطابع الزمني السابق واستخدامها للتالي، وهذه استراتيجية الاستدلال عبر الإنترنت فعالة من حيث الوقت ومتسقة مع التطبيقات العملية. على الرغم من أننا نستخدم المعلومات الزمنية، إلا أن سرعة الاستدلال لدينا لا تزال قابلة للمقارنة مع الطرق الأخرى [45, 47].

---

### Translation Notes

- **Figures referenced:** Figure 2 (a), (b), (c)
- **Key terms introduced:** Pillar-like query, hit views, projection function, anchor heights, ego-motion alignment, Deformable DETR, Panoptic SegFormer
- **Equations:** 5 equations (Eqs. 2, 3, 4, 5)
- **Citations:** Multiple references to previous work
- **Special handling:** Preserved all mathematical notation exactly, explained technical concepts in Arabic

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
