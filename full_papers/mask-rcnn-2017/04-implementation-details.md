# Section 4: Implementation Details
## القسم 4: تفاصيل التنفيذ

**Section:** implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** hyperparameters, batch size, learning rate, weight decay, momentum, RPN, anchor, aspect ratio, IoU, non-maximum suppression, inference, backbone

---

### English Version

We set hyper-parameters following existing Fast/Faster R-CNN work. Although these decisions were made for object detection in original papers, we found our instance segmentation system is robust to them.

**Training:** As in Fast R-CNN, an RoI is considered positive if it has IoU with a ground-truth box of at least 0.5 and negative otherwise. The mask loss $L_{mask}$ is defined only on positive RoIs. The mask target is the intersection between an RoI and its associated ground-truth mask.

We adopt image-centric training. Images are resized such that their scale (shorter edge) is 800 pixels. Each mini-batch has 2 images per GPU and each image has N sampled RoIs, with a ratio of 1:3 of positive to negatives. N is 64 for the C4 backbone and 512 for FPN. We train on 8 GPUs (so effective mini-batch size is 16) for 160k iterations, with a learning rate of 0.02 which is decreased by 10 at the 120k iteration. We use a weight decay of 0.0001 and momentum of 0.9. With ResNets, training Mask R-CNN with ResNet-50-FPN backbone takes about 32 hours on our synchronized 8-GPU implementation (0.72s per 16-image mini-batch), and 44 hours with ResNet-101-FPN.

The RPN anchors span 5 scales and 3 aspect ratios, following. For convenient ablation, RPN is trained separately and does not share features with Mask R-CNN, unless specified. For every entry in this paper, RPN and Mask R-CNN have consistent backbones and so are shareable.

**Inference:** At test time, the proposal number is 300 for the C4 backbone (as in Faster R-CNN) and 1000 for FPN. We run the box prediction branch on these proposals, followed by non-maximum suppression. The mask branch is then applied to the highest scoring 100 detection boxes. Although this differs from the parallel computation used in training, it speeds up inference and improves accuracy (due to the use of fewer, more accurate RoIs).

The mask branch can predict K masks per RoI, but we only use the k-th mask, where k is the predicted class by the classification branch. The m×m floating-number mask output is then resized to the RoI size, and binarized at a threshold of 0.5.

Note that since we only compute masks on the top 100 detection boxes, Mask R-CNN adds a small overhead to its Faster R-CNN counterpart (e.g., ~20% on typical models). This leads to a fast system that still achieves top results.

**Mask Representation:** For ResNet C4 backbone, the mask branch has the architecture given in Table 1. For FPN, we adopt a similar strategy where the mask branch is a 4-consecutive convolution layer, added on top of the shared RoI feature extractor (which itself is a small FCN). This head architecture is shown in Table 1.

Specifically, our mask prediction branch is a fully convolutional network. Given a $14 \times 14$ feature patch, the mask branch consists of four 3×3 conv layers (each followed by ReLU) and one deconv layer. This simple design is effective and fast. Note the mask targets of training examples are resized to 28×28. This small mask size helps fast training and testing.

---

### النسخة العربية

نضع المعاملات الفائقة (hyperparameters) متبعين أعمال فاست/فاستر آر-سي إن إن الموجودة. على الرغم من أن هذه القرارات اتُخذت للكشف عن الكائنات في الأوراق الأصلية، وجدنا أن نظام تجزئة نسخ الكائنات الخاص بنا متين أمامها.

**التدريب:** كما في فاست آر-سي إن إن، تُعتبر منطقة الاهتمام (RoI) إيجابية إذا كان لها تقاطع فوق الاتحاد (IoU) مع صندوق حقيقة أساسية يبلغ 0.5 على الأقل وسلبية خلاف ذلك. يتم تعريف خسارة القناع $L_{mask}$ فقط على مناطق الاهتمام الإيجابية. هدف القناع هو تقاطع منطقة الاهتمام وقناع الحقيقة الأساسية المرتبط بها.

نعتمد التدريب المتمركز حول الصورة. يتم تغيير حجم الصور بحيث يكون مقياسها (الحافة الأقصر) 800 بكسل. كل دفعة صغيرة (mini-batch) تحتوي على صورتين لكل GPU وكل صورة لديها N منطقة اهتمام معينة، بنسبة 1:3 من الإيجابية إلى السلبية. N هو 64 للعمود الفقري C4 و512 لـ FPN. نُدرّب على 8 GPUs (لذا فإن حجم الدفعة الصغيرة الفعال هو 16) لـ 160k تكرار، بمعدل تعلم 0.02 الذي ينخفض بمقدار 10 عند التكرار 120k. نستخدم اضمحلال وزن (weight decay) قدره 0.0001 وزخم (momentum) قدره 0.9. مع شبكات ResNets، يستغرق تدريب ماسك آر-سي إن إن مع عمود فقري ResNet-50-FPN حوالي 32 ساعة على تنفيذنا المتزامن بـ 8 GPUs (0.72 ثانية لكل دفعة صغيرة من 16 صورة)، و44 ساعة مع ResNet-101-FPN.

تمتد مراسي RPN (RPN anchors) على 5 مقاييس و3 نسب أبعاد، وفقاً لذلك. من أجل الاستئصال المريح، يتم تدريب RPN بشكل منفصل ولا تشارك الميزات مع ماسك آر-سي إن إن، ما لم يُحدد خلاف ذلك. لكل إدخال في هذا البحث، RPN وماسك آر-سي إن إن لديهما أعمدة فقرية متسقة وبالتالي قابلة للمشاركة.

**الاستدلال:** في وقت الاختبار، يكون عدد المقترحات 300 للعمود الفقري C4 (كما في فاستر آر-سي إن إن) و1000 لـ FPN. نُشغّل فرع التنبؤ بالصندوق على هذه المقترحات، متبوعاً بقمع غير الأعظمي (non-maximum suppression). يتم بعد ذلك تطبيق فرع القناع على أعلى 100 صندوق كشف بالنتيجة. على الرغم من أن هذا يختلف عن الحساب المتوازي المستخدم في التدريب، إلا أنه يسرع الاستدلال ويحسن الدقة (بسبب استخدام عدد أقل من مناطق الاهتمام الأكثر دقة).

يمكن لفرع القناع التنبؤ بـ K أقنعة لكل منطقة اهتمام، لكننا نستخدم فقط القناع رقم k، حيث k هو الصنف المتنبأ به بواسطة فرع التصنيف. يتم بعد ذلك تغيير حجم مخرج القناع ذي الأرقام العشرية $m \times m$ إلى حجم منطقة الاهتمام، ويتم تحويله إلى ثنائي عند عتبة 0.5.

لاحظ أنه نظراً لأننا نحسب الأقنعة فقط على أعلى 100 صندوق كشف، تضيف ماسك آر-سي إن إن عبئاً حسابياً صغيراً إلى نظيرتها فاستر آر-سي إن إن (مثلاً، ~20٪ على النماذج النموذجية). هذا يؤدي إلى نظام سريع لا يزال يحقق نتائج متفوقة.

**تمثيل القناع:** بالنسبة للعمود الفقري ResNet C4، فإن فرع القناع له المعمارية المعطاة في الجدول 1. بالنسبة لـ FPN، نعتمد استراتيجية مماثلة حيث يكون فرع القناع عبارة عن 4 طبقات التفاف متتالية، مضافة فوق مستخرج ميزات منطقة الاهتمام المشترك (والذي هو نفسه شبكة التفافية كاملة صغيرة). تظهر معمارية هذا الرأس في الجدول 1.

على وجه التحديد، فرع التنبؤ بالقناع الخاص بنا هو شبكة التفافية كاملة. بالنظر إلى رقعة ميزات $14 \times 14$، يتكون فرع القناع من أربع طبقات التفاف 3×3 (كل منها متبوعة بـ ReLU) وطبقة فك التفاف واحدة (deconv). هذا التصميم البسيط فعال وسريع. لاحظ أن أهداف القناع لأمثلة التدريب يتم تغيير حجمها إلى 28×28. يساعد هذا الحجم الصغير للقناع في التدريب والاختبار السريع.

---

### Translation Notes

- **Figures referenced:** Table 1 (network architecture table - not included in text)
- **Key terms introduced:**
  - Hyperparameters (المعاملات الفائقة)
  - Mini-batch (الدفعة الصغيرة)
  - IoU - Intersection over Union (تقاطع فوق الاتحاد)
  - Learning rate (معدل التعلم)
  - Weight decay (اضمحلال الوزن)
  - Momentum (الزخم)
  - Anchor (المرسى / المرساة)
  - Aspect ratio (نسبة الأبعاد)
  - Non-maximum suppression (قمع غير الأعظمي)
  - ReLU (Rectified Linear Unit) (وحدة خطية مصححة)
  - Deconvolution / deconv (فك الالتفاف)
  - Feature patch (رقعة الميزات)
- **Equations:** None (numerical values preserved)
- **Citations:** References to Fast R-CNN, Faster R-CNN
- **Special handling:**
  - Technical hyperparameters kept as numbers (0.02, 0.5, etc.)
  - GPU, RPN, FPN kept as English acronyms
  - Architecture names (ResNet-50-FPN, etc.) kept in English
  - Training times kept in original units (hours, seconds)
  - Size specifications (14×14, 28×28) preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
