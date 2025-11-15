# Section 3: Mask R-CNN
## القسم 3: ماسك آر-سي إن إن

**Section:** methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** architecture, encoder, decoder, Region Proposal Network, RoI, feature map, loss function, binary cross-entropy, sigmoid, softmax, bilinear interpolation, fully convolutional network

---

### English Version

Mask R-CNN is conceptually simple: Faster R-CNN has two outputs for each candidate object, a class label and a bounding-box offset; to this we add a third branch that outputs the object mask. Mask R-CNN is thus a natural and intuitive idea. But the additional mask output is distinct from the class and box outputs, requiring extraction of much finer spatial layout of an object. Next, we introduce the key elements of Mask R-CNN, including pixel-to-pixel alignment, which is the main missing piece in Faster R-CNN for instance segmentation.

**Faster R-CNN:** We begin by briefly reviewing the Faster R-CNN detector. Faster R-CNN consists of two stages. The first stage, called a Region Proposal Network (RPN), proposes candidate object bounding boxes. The second stage, which is in essence Fast R-CNN, extracts features using RoIPool from each candidate box and performs classification and bounding-box regression. The features used by both stages can be shared for faster inference.

**Mask R-CNN:** Mask R-CNN adopts the same two-stage procedure, with an identical first stage (the RPN). In the second stage, in parallel to predicting the class and box offset, Mask R-CNN also outputs a binary mask for each RoI. This is in contrast to most recent systems, where classification depends on mask predictions. Our approach follows the spirit of Fast R-CNN that applies bounding-box classification and regression in parallel (which turned out to largely simplify the multi-stage pipeline of original R-CNN).

Formally, during training, we define a multi-task loss on each sampled RoI as:

$$L = L_{cls} + L_{box} + L_{mask}$$

where $L_{cls}$ and $L_{box}$ are as defined in Fast R-CNN. The mask branch has a dimension of $Km^2$ for $K$ classes and $m \times m$ resolution. We apply a per-pixel sigmoid, and define $L_{mask}$ as the average binary cross-entropy loss. For an RoI associated with ground-truth class $k$, $L_{mask}$ is only defined on the $k$-th mask (other mask outputs do not contribute to the loss).

Our definition of $L_{mask}$ allows the network to generate masks for every class without competition among classes; we rely on the dedicated classification branch to predict the class label used to select the output mask. This decouples mask and class prediction. This is different from common practice when applying FCNs to semantic segmentation, which typically uses a per-pixel softmax and a multinomial cross-entropy loss. In that case, masks across classes compete; in our case, with a per-pixel sigmoid and a binary loss, they do not. We show by experiments that this formulation is key for good instance segmentation results.

**Mask Representation:** A mask encodes an input object's spatial layout. Thus, unlike class labels or box offsets that are inevitably collapsed into short output vectors by fully-connected (fc) layers, extracting the spatial structure of masks can be naturally addressed by the pixel-to-pixel correspondence provided by convolutions.

Specifically, we predict an $m \times m$ mask from each RoI using an FCN. This allows each layer in the mask branch to maintain the explicit $m \times m$ object spatial layout without collapsing it into a vector representation that lacks spatial dimensions. Unlike previous methods that resort to fc layers for mask prediction, our fully convolutional representation requires fewer parameters, and is more accurate as demonstrated by experiments.

**RoIAlign:** RoIPool is a standard operation for extracting a small feature map (e.g., 7×7) from each RoI. RoIPool first quantizes a floating-number RoI to the discrete granularity of the feature map (e.g., with a spatial stride of 16), this quantized RoI is then subdivided into spatial bins which are themselves quantized, and finally feature values covered by each bin are aggregated (usually by max pooling).

These quantizations introduce misalignments between the RoI and the extracted features. While this may not impact classification, which is robust to small translations, it has a large negative effect on predicting pixel-accurate masks.

To address this, we propose an RoIAlign layer that removes the harsh quantization of RoIPool, properly aligning the extracted features with the input. Our proposed change is simple: we avoid any quantization of the RoI boundaries or bins (i.e., we use x/16 instead of [x/16]). We use bilinear interpolation to compute the exact values of the input features at four regularly sampled locations in each RoI bin, and aggregate the result (using max or average).

We note that the results are not sensitive to the exact sampling locations, or how many points are sampled, as long as no quantization is performed. RoIAlign leads to large improvements as we show in experiments. We also compare to the RoIWarp operation proposed in MNC. Unlike RoIAlign, RoIWarp overlooks the alignment issue and was implemented in MNC as quantizing RoI just like RoIPool. So even though RoIWarp also adopts bilinear resampling motivated by MNC's large stride (e.g., 32), it performs on par with RoIPool as shown by experiments (more details in experiments section), demonstrating the crucial importance of alignment.

**Network Architecture:** To demonstrate the generality of our approach, we instantiate Mask R-CNN with multiple architectures. For clarity, we differentiate between: (i) the convolutional backbone architecture used for feature extraction over an entire image, and (ii) the network head for bounding-box recognition (classification and regression) and mask prediction that is applied separately to each RoI.

We denote the backbone architecture using the nomenclature network-depth-features. We evaluate ResNet and ResNeXt networks of depth 50 or 101 layers. The original implementation of Faster R-CNN with ResNets extracted features from the final convolutional layer of the 4-th stage, which we call C4. This backbone with ResNet-50, for example, is denoted by ResNet-50-C4. This is a common choice used in previous works.

We also explore another more effective backbone recently proposed by Lin et al., called a Feature Pyramid Network (FPN). FPN uses a top-down architecture with lateral connections to build an in-network feature pyramid from a single-scale input. Faster R-CNN with an FPN backbone extracts RoI features from different levels of the feature pyramid according to their scale, but otherwise the rest of the approach is similar to vanilla ResNet. Using a ResNet-FPN backbone for feature extraction with Mask R-CNN gives excellent gains in both accuracy and speed.

For the network head, we closely follow architectures presented in previous work. Specifically, we extend the Faster R-CNN box heads from the ResNet and FPN papers. Details are shown below. Note that our mask branch is a simple extension to the box head, and the prediction of the mask is independent from that of the class and box.

---

### النسخة العربية

ماسك آر-سي إن إن بسيطة مفاهيمياً: فاستر آر-سي إن إن لديها مخرجان لكل كائن مرشح، تسمية صنف وإزاحة صندوق التحديد؛ نضيف إلى هذا فرعاً ثالثاً يخرج قناع الكائن. وبالتالي فإن ماسك آر-سي إن إن فكرة طبيعية وبديهية. لكن مخرج القناع الإضافي متميز عن مخرجات الصنف والصندوق، ويتطلب استخراج تخطيط مكاني أدق بكثير للكائن. بعد ذلك، نقدم العناصر الرئيسية لماسك آر-سي إن إن، بما في ذلك المحاذاة بكسل تلو بكسل، وهي القطعة الرئيسية المفقودة في فاستر آر-سي إن إن لتجزئة نسخ الكائنات.

**فاستر آر-سي إن إن:** نبدأ بمراجعة موجزة لكاشف فاستر آر-سي إن إن. تتكون فاستر آر-سي إن إن من مرحلتين. المرحلة الأولى، التي تسمى شبكة مقترحات المناطق (RPN)، تقترح صناديق تحديد الكائنات المرشحة. المرحلة الثانية، وهي في جوهرها فاست آر-سي إن إن، تستخرج الميزات باستخدام آر أو آي بول (RoIPool) من كل صندوق مرشح وتنفذ التصنيف وانحدار صندوق التحديد. يمكن مشاركة الميزات المستخدمة بواسطة كلتا المرحلتين للاستدلال الأسرع.

**ماسك آر-سي إن إن:** تعتمد ماسك آر-سي إن إن نفس الإجراء ذي المرحلتين، مع مرحلة أولى متطابقة (RPN). في المرحلة الثانية، بالتوازي مع التنبؤ بالصنف وإزاحة الصندوق، تخرج ماسك آر-سي إن إن أيضاً قناعاً ثنائياً لكل منطقة اهتمام (RoI). هذا على النقيض من معظم الأنظمة الحديثة، حيث يعتمد التصنيف على تنبؤات القناع. يتبع نهجنا روح فاست آر-سي إن إن التي تطبق تصنيف وانحدار صندوق التحديد بالتوازي (والتي تبين أنها تبسط إلى حد كبير خط الأنابيب متعدد المراحل لآر-سي إن إن الأصلي).

رسمياً، أثناء التدريب، نحدد خسارة متعددة المهام على كل منطقة اهتمام معينة كما يلي:

$$L = L_{cls} + L_{box} + L_{mask}$$

حيث $L_{cls}$ و $L_{box}$ كما هو محدد في فاست آر-سي إن إن. فرع القناع له بُعد $Km^2$ لـ $K$ صنفاً ودقة $m \times m$. نطبق سيغمويد لكل بكسل، ونعرّف $L_{mask}$ كمتوسط خسارة الإنتروبيا المتقاطعة الثنائية. لمنطقة اهتمام مرتبطة بالصنف الحقيقي $k$، يتم تعريف $L_{mask}$ فقط على القناع رقم $k$ (مخرجات الأقنعة الأخرى لا تساهم في الخسارة).

يسمح تعريفنا لـ $L_{mask}$ للشبكة بتوليد أقنعة لكل صنف دون منافسة بين الأصناف؛ نعتمد على فرع التصنيف المخصص للتنبؤ بتسمية الصنف المستخدمة لتحديد قناع الإخراج. هذا يفصل التنبؤ بالقناع والصنف. هذا يختلف عن الممارسة الشائعة عند تطبيق الشبكات الالتفافية الكاملة (FCNs) على التجزئة الدلالية، والتي تستخدم عادةً سوفت ماكس (softmax) لكل بكسل وخسارة إنتروبيا متقاطعة متعددة الحدود. في هذه الحالة، تتنافس الأقنعة عبر الأصناف؛ في حالتنا، مع سيغمويد لكل بكسل وخسارة ثنائية، لا تتنافس. نُظهر من خلال التجارب أن هذه الصيغة أساسية للحصول على نتائج جيدة لتجزئة نسخ الكائنات.

**تمثيل القناع:** يشفّر القناع التخطيط المكاني لكائن الإدخال. وبالتالي، على عكس تسميات الأصناف أو إزاحات الصناديق التي تنهار حتماً إلى متجهات إخراج قصيرة بواسطة طبقات متصلة بالكامل (fc)، يمكن معالجة استخراج البنية المكانية للأقنعة بشكل طبيعي من خلال التطابق بكسل تلو بكسل الذي توفره الالتفافات.

على وجه التحديد، نتنبأ بقناع $m \times m$ من كل منطقة اهتمام باستخدام شبكة التفافية كاملة (FCN). هذا يسمح لكل طبقة في فرع القناع بالحفاظ على التخطيط المكاني الصريح $m \times m$ للكائن دون طيّه في تمثيل متجه يفتقر إلى الأبعاد المكانية. على عكس الطرق السابقة التي تلجأ إلى طبقات fc للتنبؤ بالقناع، يتطلب تمثيلنا الالتفافي الكامل معاملات أقل، وهو أكثر دقة كما تُظهر التجارب.

**آر أو آي ألاين (RoIAlign):** آر أو آي بول (RoIPool) هي عملية قياسية لاستخراج خريطة ميزات صغيرة (مثل 7×7) من كل منطقة اهتمام. تقوم آر أو آي بول أولاً بتكميم منطقة اهتمام ذات رقم عشري إلى دقة منفصلة لخريطة الميزات (مثلاً، مع خطوة مكانية 16)، ثم يتم تقسيم منطقة الاهتمام المكممة هذه إلى صناديق مكانية يتم تكميمها أيضاً، وأخيراً يتم تجميع قيم الميزات المغطاة بواسطة كل صندوق (عادةً عن طريق التجميع الأقصى).

هذه التكميمات تؤدي إلى عدم محاذاة بين منطقة الاهتمام والميزات المستخرجة. في حين أن هذا قد لا يؤثر على التصنيف، الذي يكون متيناً أمام الترجمات الصغيرة، إلا أن له تأثيراً سلبياً كبيراً على التنبؤ بأقنعة دقيقة بالبكسل.

لمعالجة ذلك، نقترح طبقة آر أو آي ألاين (RoIAlign) التي تزيل التكميم القاسي لآر أو آي بول، وتحاذي بشكل صحيح الميزات المستخرجة مع الإدخال. التغيير المقترح بسيط: نتجنب أي تكميم لحدود أو صناديق منطقة الاهتمام (أي، نستخدم x/16 بدلاً من [x/16]). نستخدم الاستكمال ثنائي الخطية (bilinear interpolation) لحساب القيم الدقيقة لميزات الإدخال في أربعة مواقع منتظمة العينة في كل صندوق منطقة اهتمام، ونجمع النتيجة (باستخدام التجميع الأقصى أو المتوسط).

نلاحظ أن النتائج ليست حساسة لمواقع العينة الدقيقة، أو لعدد النقاط المعينة، طالما لم يتم إجراء تكميم. يؤدي آر أو آي ألاين إلى تحسينات كبيرة كما نُظهر في التجارب. نقارن أيضاً بعملية آر أو آي وارب (RoIWarp) المقترحة في MNC. على عكس آر أو آي ألاين، تتجاهل آر أو آي وارب مشكلة المحاذاة وتم تنفيذها في MNC كتكميم لمنطقة الاهتمام تماماً مثل آر أو آي بول. لذلك على الرغم من أن آر أو آي وارب تتبنى أيضاً إعادة العينة ثنائية الخطية بدافع من الخطوة الكبيرة لـ MNC (مثل 32)، إلا أنها تؤدي على قدم المساواة مع آر أو آي بول كما تُظهر التجارب (مزيد من التفاصيل في قسم التجارب)، مما يُظهر الأهمية الحاسمة للمحاذاة.

**معمارية الشبكة:** لإظهار عمومية نهجنا، نستخدم ماسك آر-سي إن إن مع معماريات متعددة. من أجل الوضوح، نفرق بين: (i) معمارية العمود الفقري الالتفافي المستخدمة لاستخراج الميزات عبر الصورة بأكملها، و (ii) رأس الشبكة للتعرف على صندوق التحديد (التصنيف والانحدار) والتنبؤ بالقناع الذي يتم تطبيقه بشكل منفصل على كل منطقة اهتمام.

نشير إلى معمارية العمود الفقري باستخدام المسمى network-depth-features. نقيّم شبكات ResNet و ResNeXt بعمق 50 أو 101 طبقة. استخرج التنفيذ الأصلي لفاستر آر-سي إن إن مع ResNets الميزات من الطبقة الالتفافية النهائية للمرحلة الرابعة، والتي نسميها C4. يُشار إلى هذا العمود الفقري مع ResNet-50، على سبيل المثال، بـ ResNet-50-C4. هذا اختيار شائع يستخدم في الأعمال السابقة.

نستكشف أيضاً عموداً فقرياً آخر أكثر فعالية تم اقتراحه مؤخراً بواسطة لين وآخرين، يُسمى شبكة هرم الميزات (FPN). تستخدم FPN معمارية من أعلى إلى أسفل مع اتصالات جانبية لبناء هرم ميزات داخل الشبكة من إدخال أحادي المقياس. تستخرج فاستر آر-سي إن إن مع عمود فقري FPN ميزات منطقة الاهتمام من مستويات مختلفة من هرم الميزات وفقاً لمقياسها، لكن بقية النهج مشابه لـ ResNet الفانيليا. يوفر استخدام عمود فقري ResNet-FPN لاستخراج الميزات مع ماسك آر-سي إن إن مكاسب ممتازة في كل من الدقة والسرعة.

بالنسبة لرأس الشبكة، نتبع عن كثب المعماريات المقدمة في الأعمال السابقة. على وجه التحديد، نوسع رؤوس صناديق فاستر آر-سي إن إن من أوراق ResNet و FPN. التفاصيل موضحة أدناه. لاحظ أن فرع القناع الخاص بنا هو امتداد بسيط لرأس الصندوق، والتنبؤ بالقناع مستقل عن التنبؤ بالصنف والصندوق.

---

### Translation Notes

- **Figures referenced:** None (architecture diagrams referenced but not embedded)
- **Key terms introduced:**
  - Multi-task loss (خسارة متعددة المهام)
  - Binary cross-entropy (الإنتروبيا المتقاطعة الثنائية)
  - Sigmoid (سيغمويد)
  - Softmax (سوفت ماكس)
  - RoIAlign (آر أو آي ألاين)
  - RoIPool (آر أو آي بول)
  - Bilinear interpolation (الاستكمال ثنائي الخطية)
  - Quantization (التكميم)
  - Feature Pyramid Network (شبكة هرم الميزات)
  - Backbone architecture (معمارية العمود الفقري)
- **Equations:**
  - Loss function: $L = L_{cls} + L_{box} + L_{mask}$
  - Mask dimensions: $Km^2$ for $K$ classes and $m \times m$ resolution
- **Citations:** References to Faster R-CNN, Fast R-CNN, ResNet, ResNeXt, FPN, MNC
- **Special handling:**
  - Mathematical notation preserved in LaTeX format
  - Network architecture names kept in English
  - Technical operations (RoIAlign, RoIPool) transliterated
  - Quantization operation notation preserved: x/16 vs [x/16]

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
