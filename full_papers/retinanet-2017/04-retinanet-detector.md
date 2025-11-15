# Section 4: RetinaNet Detector
## القسم 4: كاشف RetinaNet

**Section:** RetinaNet Detector
**Translation Quality:** 0.90
**Glossary Terms Used:** architecture, backbone, feature pyramid, anchor boxes, convolutional neural network, classification, bounding box, ResNet, subnetwork, inference

---

### English Version

RetinaNet is a single, unified network composed of a backbone network and two task-specific subnetworks. The backbone is responsible for computing a convolutional feature map over an entire input image and is an off-the-shelf convolutional network. The first subnet performs convolutional object classification on the backbone's output; the second subnet performs convolutional bounding box regression. The two subnetworks feature a simple design that we propose specifically for one-stage, dense detection, see Figure 3. While there are many possible choices for the details of these components, most design parameters are not particularly sensitive. We describe the default RetinaNet architecture used in our experiments, recognizing that many alternatives may also be effective.

**Feature Pyramid Network Backbone:** We adopt the Feature Pyramid Network (FPN) from [20] as the backbone network for RetinaNet. In brief, FPN augments a standard convolutional network with a top-down pathway and lateral connections so the network efficiently constructs a rich, multi-scale feature pyramid from a single resolution input image, see Figure 3(a). Each level of the pyramid can be used for detecting objects at a different scale. FPN improves multi-scale predictions from fully convolutional networks, as shown in [20], and thus is a natural choice for our experiments. Note that we use the variant of FPN described in [20] which uses ResNet [15] architecture. We construct a pyramid with levels P3 through P7, where $\ell$ indicates pyramid level ($P_\ell$ has resolution $2^\ell$ lower than the input). All pyramid levels have C = 256 channels. Details of the pyramid generally follow [20] with a few modest modifications. While many design choices are possible, we emphasize that our simple detector works well with a standard FPN. We leave further exploration of alternative backbones and pyramid representations to future work.

**Anchors:** We use translation invariant anchor boxes similar to those in the RPN variant in [20]. The anchors have areas of $32^2$ to $512^2$ on pyramid levels P3 to P7, respectively. As in [20], at each pyramid level we use anchors at three aspect ratios {1:2, 1:1, 2:1}. For denser scale coverage than in [20], at each level we add anchors of sizes {$2^0$, $2^{1/3}$, $2^{2/3}$} of the original set of 3 aspect ratio anchors. This improves AP in our setting. In total there are A = 9 anchors per level and across levels they cover the scale range 32 - 813 pixels with respect to the network's input image.

Each anchor is assigned a length K one-hot vector of classification targets, where K is the number of object classes, and a 4-vector of box regression targets. We use the assignment rule from RPN [28] but modified for multi-class detection and with adjusted thresholds. Specifically, anchors are assigned to ground-truth object boxes using an intersection-over-union (IoU) threshold of 0.5; and to background if their IoU is in [0, 0.4). As each anchor is assigned to at most one object box, we set the corresponding entry in its length K label vector to 1 and all other entries to 0. If an anchor is unassigned, which may happen with overlap in [0.4, 0.5), it is ignored during training. Box regression targets are computed as the offset between each anchor and its assigned object box, or omitted if there is no assignment.

**Classification Subnet:** The classification subnet predicts the probability of object presence at each spatial position for each of the A anchors and K object classes. This subnet is a small FCN attached to each FPN level; parameters of this subnet are shared across all pyramid levels. Taking an input feature map with C channels from a given pyramid level, the subnet applies four 3×3 conv layers, each with C filters and each followed by ReLU activations, followed by a 3×3 conv layer with KA filters. Finally sigmoid activations are attached to output the KA binary predictions per spatial location, see Figure 3(c). We use C = 256 and A = 9 in most experiments.

In contrast to RPN [28], our object classification subnet is deeper, uses only 3×3 convs, and does not share parameters with the box regression subnet (described next). We found these higher-level design decisions to be more important than specific values of hyperparameters.

**Box Regression Subnet:** In parallel with the object classification subnet, we attach another small FCN to each pyramid level for the purpose of regressing the offset from each anchor box to a nearby ground-truth object box, if one exists. The design of the box regression subnet is identical to the classification subnet except that it terminates in 4A linear outputs per spatial location, see Figure 3(d). For each of the A anchors per spatial location, these 4 outputs predict the relative offset between the anchor and the ground-truth box (as in RPN [28] a parameterization of the coordinates is used). The box regression subnet shares the same structure as the classification subnet, except the final layer. We note that unlike most recent work, we use a class-agnostic bounding box regressor which uses fewer parameters and we found to be equally effective.

**Inference and Training:**

*Inference:* To improve speed, we only decode box predictions from at most 1k top-scoring predictions per FPN level, after thresholding detector confidence at 0.05. The top predictions from all levels are merged and non-maximum suppression with a threshold of 0.5 is applied to yield the final detections.

*Focal Loss:* We use the focal loss introduced in Section 3 as the classification loss. As described in Section 3, we find that $\gamma = 2$ works well in practice and the RetinaNet is relatively robust to $\gamma$; we use this default value in all experiments. For the final loss, we also use an $\alpha$-balanced variant of the focal loss with $\alpha = 0.25$ yielding slightly improved results over the non-$\alpha$-balanced form.

*Initialization:* We experiment with ResNet-50-FPN and ResNet-101-FPN backbones [15, 20]. The base ResNet-50 and ResNet-101 models are pre-trained on ImageNet1k; we use the models released by [15]. New layers added for FPN are initialized as in [20]. All new conv layers except the final one in the RetinaNet subnets are initialized with bias b = 0 and a Gaussian weight fill with $\sigma = 0.01$. For the final conv layer of the classification subnet, we set the bias initialization to $b = -\log((1-\pi)/\pi)$, where $\pi$ specifies that at the start of training every anchor should be labeled as foreground with confidence of ~$\pi$. We use $\pi = 0.01$ in all experiments, although results are robust to the exact value. As explained in Section 3, this initialization prevents the large number of background anchors from generating a large, destabilizing loss value in the first iteration of training.

*Optimization:* RetinaNet is trained with stochastic gradient descent (SGD). We use synchronized SGD over 8 GPUs with a total of 16 images per minibatch (2 images per GPU). Unless otherwise specified, all models are trained for 90k iterations with an initial learning rate of 0.01, which is then divided by 10 at 60k and again at 80k iterations. We use horizontal image flipping as the only form of data augmentation unless otherwise noted. Weight decay of 0.0001 and momentum of 0.9 are used. The training loss is the sum of the focal loss and the standard smooth L1 loss used for box regression [10]. Training time ranges between 10-35 hours for the models in Table 1.

---

### النسخة العربية

RetinaNet هي شبكة واحدة موحدة تتكون من شبكة عمود فقري وشبكتين فرعيتين خاصتين بالمهام. العمود الفقري مسؤول عن حساب خريطة ميزات التفافية على صورة إدخال كاملة وهو شبكة التفافية جاهزة. تُنفذ الشبكة الفرعية الأولى تصنيف أجسام التفافي على خرج العمود الفقري؛ تُنفذ الشبكة الفرعية الثانية انحدار صندوق التحديد الالتفافي. تتميز الشبكتان الفرعيتان بتصميم بسيط نقترحه خصيصاً للكشف الكثيف أحادي المرحلة، انظر الشكل 3. بينما توجد خيارات عديدة ممكنة لتفاصيل هذه المكونات، معظم معاملات التصميم ليست حساسة بشكل خاص. نصف معمارية RetinaNet الافتراضية المستخدمة في تجاربنا، مع إدراك أن العديد من البدائل قد تكون فعالة أيضاً.

**العمود الفقري لشبكة الهرم الميزاتي:** نعتمد شبكة الهرم الميزاتي (FPN) من [20] كشبكة عمود فقري لـ RetinaNet. باختصار، يُعزز FPN شبكة التفافية قياسية بمسار من أعلى إلى أسفل واتصالات جانبية بحيث تبني الشبكة بكفاءة هرم ميزات غني ومتعدد المقاييس من صورة إدخال بدقة واحدة، انظر الشكل 3(أ). يمكن استخدام كل مستوى من الهرم لكشف أجسام بمقياس مختلف. يحسن FPN التنبؤات متعددة المقاييس من الشبكات الالتفافية الكاملة، كما هو موضح في [20]، وبالتالي فهو خيار طبيعي لتجاربنا. لاحظ أننا نستخدم متغير FPN الموصوف في [20] والذي يستخدم معمارية ResNet [15]. نبني هرماً بمستويات من P3 إلى P7، حيث $\ell$ يشير إلى مستوى الهرم ($P_\ell$ له دقة أقل بمقدار $2^\ell$ من الإدخال). جميع مستويات الهرم لها C = 256 قناة. تفاصيل الهرم تتبع بشكل عام [20] مع بعض التعديلات المتواضعة. بينما العديد من خيارات التصميم ممكنة، نؤكد أن كاشفنا البسيط يعمل بشكل جيد مع FPN قياسي. نترك مزيداً من الاستكشاف للأعمدة الفقرية البديلة وتمثيلات الهرم للعمل المستقبلي.

**المراسي:** نستخدم صناديق مراسي ثابتة الترجمة مماثلة لتلك الموجودة في متغير RPN في [20]. للمراسي مساحات من $32^2$ إلى $512^2$ على مستويات الهرم من P3 إلى P7، على التوالي. كما في [20]، في كل مستوى هرمي نستخدم مراسي بثلاث نسب أبعاد {1:2، 1:1، 2:1}. للحصول على تغطية مقياس أكثر كثافة من [20]، في كل مستوى نضيف مراسي بأحجام {$2^0$، $2^{1/3}$، $2^{2/3}$} من المجموعة الأصلية لمراسي نسب الأبعاد الثلاث. هذا يحسن AP في إعدادنا. إجمالاً يوجد A = 9 مراسي لكل مستوى وعبر المستويات تغطي نطاق المقياس من 32 إلى 813 بكسل بالنسبة لصورة إدخال الشبكة.

يُخصص لكل مرساة متجه واحد ساخن بطول K من أهداف التصنيف، حيث K هو عدد فئات الأجسام، ومتجه 4 من أهداف انحدار الصندوق. نستخدم قاعدة التخصيص من RPN [28] ولكن معدلة للكشف متعدد الفئات ومع عتبات معدلة. تحديداً، تُخصص المراسي لصناديق الأجسام الحقيقية الأرضية باستخدام عتبة تقاطع على اتحاد (IoU) بمقدار 0.5؛ وللخلفية إذا كان IoU في [0، 0.4). حيث يُخصص كل مرساة لصندوق جسم واحد على الأكثر، نضبط الإدخال المقابل في متجه التسمية بطول K إلى 1 وجميع الإدخالات الأخرى إلى 0. إذا لم يُخصص المرساة، والذي قد يحدث مع تداخل في [0.4، 0.5)، فإنه يُتجاهل أثناء التدريب. تُحسب أهداف انحدار الصندوق كالإزاحة بين كل مرساة وصندوق الجسم المخصص لها، أو تُحذف إذا لم يكن هناك تخصيص.

**الشبكة الفرعية للتصنيف:** تتنبأ الشبكة الفرعية للتصنيف باحتمالية وجود جسم في كل موضع مكاني لكل من المراسي A وفئات الأجسام K. هذه الشبكة الفرعية هي FCN صغيرة متصلة بكل مستوى FPN؛ تُشارك معاملات هذه الشبكة الفرعية عبر جميع مستويات الهرم. عند أخذ خريطة ميزات إدخال بقنوات C من مستوى هرمي معين، تُطبق الشبكة الفرعية أربع طبقات التفاف 3×3، كل منها بمرشحات C وكل منها متبوعة بتفعيلات ReLU، متبوعة بطبقة التفاف 3×3 بمرشحات KA. أخيراً، تُرفق تفعيلات sigmoid لإخراج التنبؤات الثنائية KA لكل موقع مكاني، انظر الشكل 3(ج). نستخدم C = 256 و A = 9 في معظم التجارب.

على النقيض من RPN [28]، الشبكة الفرعية لتصنيف الأجسام لدينا أعمق، تستخدم التفافات 3×3 فقط، ولا تشارك المعاملات مع الشبكة الفرعية لانحدار الصندوق (الموصوفة تالياً). وجدنا أن قرارات التصميم عالية المستوى هذه أكثر أهمية من القيم المحددة للمعاملات الفائقة.

**الشبكة الفرعية لانحدار الصندوق:** بالتوازي مع الشبكة الفرعية لتصنيف الأجسام، نرفق FCN صغيرة أخرى بكل مستوى هرمي لغرض انحدار الإزاحة من كل صندوق مرساة إلى صندوق جسم حقيقي أرضي قريب، إذا كان موجوداً. تصميم الشبكة الفرعية لانحدار الصندوق مطابق للشبكة الفرعية للتصنيف باستثناء أنها تنتهي بمخرجات خطية 4A لكل موقع مكاني، انظر الشكل 3(د). لكل من المراسي A لكل موقع مكاني، هذه المخرجات الأربعة تتنبأ بالإزاحة النسبية بين المرساة وصندوق الحقيقة الأرضية (كما في RPN [28] يُستخدم تحديد معاملات الإحداثيات). تشارك الشبكة الفرعية لانحدار الصندوق نفس البنية مع الشبكة الفرعية للتصنيف، باستثناء الطبقة النهائية. نلاحظ أنه على عكس معظم الأعمال الحديثة، نستخدم منحدر صندوق تحديد لا يعتمد على الفئة والذي يستخدم معاملات أقل ووجدناه فعالاً بنفس القدر.

**الاستدلال والتدريب:**

*الاستدلال:* لتحسين السرعة، نفك تشفير تنبؤات الصندوق فقط من 1000 تنبؤ على الأكثر الأعلى درجة لكل مستوى FPN، بعد تطبيق عتبة ثقة الكاشف عند 0.05. تُدمج التنبؤات العليا من جميع المستويات ويُطبق قمع غير الحد الأقصى بعتبة 0.5 لإنتاج الكشوفات النهائية.

*الخسارة المُركزة:* نستخدم الخسارة المُركزة المقدمة في القسم 3 كخسارة التصنيف. كما هو موضح في القسم 3، نجد أن $\gamma = 2$ يعمل بشكل جيد في الممارسة وأن RetinaNet صلب نسبياً لـ $\gamma$؛ نستخدم هذه القيمة الافتراضية في جميع التجارب. للخسارة النهائية، نستخدم أيضاً متغير موزون بـ $\alpha$ من الخسارة المُركزة مع $\alpha = 0.25$ منتجاً نتائج محسنة قليلاً على الشكل غير الموزون بـ $\alpha$.

*التهيئة:* نُجري تجارب مع أعمدة فقرية ResNet-50-FPN و ResNet-101-FPN [15، 20]. نماذج ResNet-50 و ResNet-101 الأساسية مُدربة مسبقاً على ImageNet1k؛ نستخدم النماذج المنشورة بواسطة [15]. الطبقات الجديدة المضافة لـ FPN تُهيأ كما في [20]. جميع طبقات الالتفاف الجديدة باستثناء الطبقة النهائية في الشبكات الفرعية لـ RetinaNet تُهيأ بانحياز b = 0 وملء وزن غاوسي بـ $\sigma = 0.01$. لطبقة الالتفاف النهائية للشبكة الفرعية للتصنيف، نضبط تهيئة الانحياز إلى $b = -\log((1-\pi)/\pi)$، حيث $\pi$ يحدد أنه في بداية التدريب يجب تسمية كل مرساة كمقدمة بثقة ~$\pi$. نستخدم $\pi = 0.01$ في جميع التجارب، على الرغم من أن النتائج صلبة للقيمة الدقيقة. كما هو موضح في القسم 3، هذه التهيئة تمنع العدد الكبير من مراسي الخلفية من توليد قيمة خسارة كبيرة تزعزع الاستقرار في التكرار الأول من التدريب.

*التحسين:* يُدرب RetinaNet بانحدار تدرجي عشوائي (SGD). نستخدم SGD متزامن على 8 وحدات معالجة رسومات بإجمالي 16 صورة لكل دفعة صغيرة (صورتان لكل GPU). ما لم يُحدد خلاف ذلك، تُدرب جميع النماذج لـ 90 ألف تكرار بمعدل تعلم أولي 0.01، والذي يُقسم بعد ذلك على 10 عند 60 ألف ومرة أخرى عند 80 ألف تكرار. نستخدم انعكاس الصورة الأفقي كالشكل الوحيد لزيادة البيانات ما لم يُذكر خلاف ذلك. يُستخدم انحلال وزن 0.0001 وزخم 0.9. خسارة التدريب هي مجموع الخسارة المُركزة وخسارة L1 الناعمة القياسية المستخدمة لانحدار الصندوق [10]. يتراوح وقت التدريب بين 10-35 ساعة للنماذج في الجدول 1.

---

### Translation Notes

- **Figures referenced:** Figure 3 (architecture diagrams: 3(a) FPN, 3(c) classification subnet, 3(d) box regression subnet)
- **Key terms introduced:**
  - Backbone network (شبكة عمود فقري)
  - Task-specific subnetwork (شبكة فرعية خاصة بالمهام)
  - Off-the-shelf (جاهزة)
  - Top-down pathway (مسار من أعلى إلى أسفل)
  - Lateral connections (اتصالات جانبية)
  - Translation invariant (ثابتة الترجمة)
  - Intersection-over-union (IoU) (تقاطع على اتحاد)
  - One-hot vector (متجه واحد ساخن)
  - Non-maximum suppression (قمع غير الحد الأقصى)
  - Stochastic gradient descent (انحدار تدرجي عشوائي)
  - Weight decay (انحلال وزن)
  - Smooth L1 loss (خسارة L1 الناعمة)

- **Equations:** Mathematical expressions for pyramid levels ($2^\ell$), anchor sizes, etc.
- **Citations:** [20], [15], [28], [10], Table 1 referenced
- **Special handling:**
  - Model names preserved: ResNet, FPN, RPN, ImageNet1k
  - Technical values: C=256, A=9, γ=2, α=0.25, π=0.01
  - Layer specifications: 3×3 conv, 4A outputs, KA filters
  - Training parameters: 90k iterations, learning rate 0.01, 8 GPUs, 16 images batch
  - FCN = Fully Convolutional Network kept as abbreviation
  - ReLU preserved as activation function name

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.89
- Glossary consistency: 0.88
- **Overall section score: 0.90**

### Back-translation Check

Key technical phrases:
- "شبكة عمود فقري" → "Backbone network" ✓
- "مسار من أعلى إلى أسفل" → "Top-down pathway" ✓
- "اتصالات جانبية" → "Lateral connections" ✓
- "تقاطع على اتحاد" → "Intersection-over-union" ✓
- "قمع غير الحد الأقصى" → "Non-maximum suppression" ✓
- "انحدار تدرجي عشوائي" → "Stochastic gradient descent" ✓
