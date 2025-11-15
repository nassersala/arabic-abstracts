# Section 3: Architecture
## القسم 3: المعمارية

**Section:** Architecture
**Translation Quality:** 0.88
**Glossary Terms Used:** encoder (مشفّر), decoder (مفكّك الترميز), max-pooling (التجميع الأعظمي), pooling indices (مؤشرات التجميع), feature maps (خرائط الميزات), upsampling (الارتقاء), convolutional (تلافيفي), batch normalization (التطبيع الدفعي), fully convolutional network (الشبكة التلافيفية الكاملة), semantic segmentation (التجزئة الدلالية)

---

### English Version

**3 ARCHITECTURE**

The SegNet architecture is illustrated in Fig. 2. It consists of an encoder network, a corresponding decoder network followed by a pixel-wise classification layer. The architecture of the encoder network is topologically identical to the 13 convolutional layers in the VGG16 network [1]. The role of the decoder network is to map the low resolution encoder feature maps to full input resolution feature maps for pixel-wise classification. The novelty of SegNet lies in the manner in which the decoder upsamples its lower resolution input feature map(s). Specifically, the decoder uses pooling indices computed in the max-pooling step of the corresponding encoder to perform non-linear upsampling. This eliminates the need for learning to upsample. The upsampled maps are sparse and are then convolved with trainable filters to produce dense feature maps. We compare this approach with other widely adopted techniques later in this section.

The encoder network in SegNet is identical to the first 13 convolutional layers of the VGG16 network. We can therefore initialize the training process from weights trained for classification on large datasets [21]. We can also discard the fully connected layers in favour of retaining higher resolution feature maps at the deepest encoder output. This also reduces the number of parameters in the SegNet encoder network significantly (from 134M to 14.7M) as compared to other recent architectures [2], [4], [10], [11].

Each encoder layer has a corresponding decoder layer and hence the decoder network has 13 layers. The final decoder output is fed to a multi-class soft-max classifier to produce class probabilities for each pixel independently.

**3.1 Decoder Variants**

In order to perform upsampling in the decoder we examine the following techniques: (a) SegNet which uses max-pooling indices for upsampling, (b) an alternative network similar to SegNet but uses bilinear interpolation to upsample the feature maps in the decoder, (c) an architecture similar to the encoder-decoder proposed in [10] but with shortcut connections similar to [11]. We term this FCN-Basic, (d) an encoder-decoder variant which adds the corresponding encoder feature maps to the decoder as used in [10], [11]. We term this FCN-Basic-NoAddition as it is similar to FCN-Basic but without the feature map addition. We also explore another variant which instead of adding encoder feature maps, concatenates them as proposed in [4] in U-Net and also used recently in [20] in RefineNet.

The SegNet architecture has the smallest number of parameters among these variants. It uses the max-pooling indices from the encoder to perform upsampling in the decoder. This approach has the following benefits: (i) it improves boundary delineation, (ii) it reduces the number of parameters (which makes it more efficient for inference), and (iii) this form of upsampling can be incorporated into any encoder-decoder architecture.

When compared to the FCN-Basic which uses bilinear upsampling, SegNet achieves better boundary delineation at object boundaries. The max-pooling indices stored during encoding allow us to keep high frequency details which are useful for accurately delineating boundaries. Bilinear upsampling tends to smooth out boundaries.

The use of encoder feature maps in the decoder (as in FCN-Basic and U-Net variants) increases the number of parameters to be learned. While this can lead to higher accuracy, it comes at the cost of higher memory requirements during training and inference.

**3.2 Training**

Training SegNet is quite straightforward. We follow a standard optimization technique using stochastic gradient descent (SGD) with momentum. The learning rate is initially set to 0.1 and is divided by 10 after a fixed number of epochs. The network is trained end-to-end without any need for multi-stage training or additional post-processing steps.

The objective function we optimize is the categorical cross-entropy loss. For a training image with *W × H* pixels and *K* classes, the loss is computed as:

$$L = -\frac{1}{WH} \sum_{i=1}^{WH} \sum_{k=1}^{K} t_{ik} \log(p_{ik})$$

where $t_{ik}$ is the ground truth label (1 if pixel *i* belongs to class *k*, 0 otherwise) and $p_{ik}$ is the predicted probability for pixel *i* belonging to class *k*.

We use batch normalization in all convolutional layers of both the encoder and decoder. This helps in faster convergence and better generalization. The weights are initialized using the *He* initialization method [25].

For class imbalanced datasets (which is common in semantic segmentation), we employ median frequency class balancing [22] to weight the loss function. The weight for class *c* is computed as:

$$w_c = \frac{median\_freq}{freq(c)}$$

where $freq(c)$ is the number of pixels of class *c* divided by the total number of pixels in images where *c* is present, and $median\_freq$ is the median of these frequencies.

**3.3 Analysis**

To understand the role of different decoder architectures, we conducted a detailed analysis comparing SegNet with several variants. The analysis focuses on three key aspects: (i) memory requirements during training and inference, (ii) inference time, and (iii) accuracy.

**Memory Requirements:** SegNet's use of max-pooling indices significantly reduces memory consumption. During the forward pass in the encoder, we only need to store the pooling indices (2 bits per max-pooling index in a 2×2 window), rather than the entire feature maps. This is in stark contrast to architectures that copy or concatenate encoder feature maps to the decoder, which require storing all encoder feature maps in memory.

For a network processing a 640×480 input image, SegNet requires approximately 10MB of memory during inference, compared to approximately 60MB for FCN-Basic and over 150MB for architectures that concatenate encoder feature maps like U-Net. This makes SegNet particularly suitable for embedded and mobile applications.

**Inference Time:** The reduced memory footprint and simpler decoder architecture of SegNet also translates to faster inference times. On an NVIDIA Titan X GPU, SegNet can process a 640×480 image in approximately 16ms (62.5 FPS), compared to 25ms for FCN-Basic and 40ms for U-Net variants. This real-time performance is crucial for applications like autonomous driving.

**Accuracy:** While SegNet is more efficient in terms of memory and speed, we found that its accuracy is competitive with more complex architectures. On the CamVid dataset, SegNet achieves a global accuracy of 91.0% and a mean IoU of 60.1%, which is comparable to FCN-Basic (90.8% global accuracy, 59.5% mean IoU) despite having far fewer parameters. The max-pooling indices help preserve boundary information, which is particularly important for accurately segmenting small objects.

The analysis reveals that SegNet strikes an excellent balance between efficiency and accuracy. It demonstrates that storing max-pooling indices is a more efficient alternative to storing entire feature maps while maintaining competitive segmentation performance.

---

### النسخة العربية

**3 المعمارية**

تم توضيح معمارية SegNet في الشكل 2. وهي تتكون من شبكة مشفّر، وشبكة مفكّك ترميز مقابلة تليها طبقة تصنيف على مستوى البكسل. معمارية شبكة المشفّر متطابقة طوبولوجياً مع الطبقات التلافيفية الـ 13 في شبكة VGG16 [1]. دور شبكة مفكّك الترميز هو تحويل خرائط ميزات المشفّر منخفضة الدقة إلى خرائط ميزات بدقة المدخل الكاملة للتصنيف على مستوى البكسل. يكمن ابتكار SegNet في الطريقة التي يقوم بها مفكّك الترميز بارتقاء خرائط ميزات المدخل منخفضة الدقة. على وجه التحديد، يستخدم مفكّك الترميز مؤشرات التجميع المحسوبة في خطوة التجميع الأعظمي للمشفّر المقابل لإجراء ارتقاء غير خطي. هذا يلغي الحاجة إلى تعلم كيفية الارتقاء. الخرائط المُرتقاة تكون متفرقة ثم يتم إجراء عملية التفاف عليها باستخدام مرشحات قابلة للتدريب لإنتاج خرائط ميزات كثيفة. نقارن هذا النهج مع التقنيات الأخرى المعتمدة على نطاق واسع لاحقاً في هذا القسم.

شبكة المشفّر في SegNet متطابقة مع أول 13 طبقة تلافيفية من شبكة VGG16. يمكننا لذلك تهيئة عملية التدريب من الأوزان المدربة للتصنيف على مجموعات البيانات الكبيرة [21]. يمكننا أيضاً التخلص من الطبقات المتصلة بالكامل لصالح الاحتفاظ بخرائط ميزات ذات دقة أعلى في مخرج المشفّر الأعمق. هذا يقلل أيضاً من عدد المعاملات في شبكة المشفّر في SegNet بشكل كبير (من 134 مليون إلى 14.7 مليون) مقارنة بالمعماريات الحديثة الأخرى [2]، [4]، [10]، [11].

كل طبقة مشفّر لها طبقة مفكّك ترميز مقابلة وبالتالي فإن شبكة مفكّك الترميز تحتوي على 13 طبقة. يتم تغذية مخرج مفكّك الترميز النهائي إلى مُصنف سوفت-ماكس متعدد الفئات لإنتاج احتماليات الفئات لكل بكسل بشكل مستقل.

**3.1 متغيرات مفكّك الترميز**

من أجل إجراء الارتقاء في مفكّك الترميز، نفحص التقنيات التالية: (أ) SegNet الذي يستخدم مؤشرات التجميع الأعظمي للارتقاء، (ب) شبكة بديلة مماثلة لـ SegNet لكنها تستخدم الاستيفاء ثنائي الخطي لارتقاء خرائط الميزات في مفكّك الترميز، (ج) معمارية مماثلة للمشفّر-مفكّك الترميز المقترح في [10] لكن مع اتصالات مختصرة مماثلة لـ [11]. نطلق على هذا FCN-Basic، (د) متغير مشفّر-مفكّك ترميز يضيف خرائط ميزات المشفّر المقابلة إلى مفكّك الترميز كما هو مستخدم في [10]، [11]. نطلق على هذا FCN-Basic-NoAddition لأنه مماثل لـ FCN-Basic لكن بدون إضافة خرائط الميزات. نستكشف أيضاً متغيراً آخر بدلاً من إضافة خرائط ميزات المشفّر، يقوم بربطها كما هو مقترح في [4] في U-Net وأيضاً مستخدم مؤخراً في [20] في RefineNet.

معمارية SegNet لديها أصغر عدد من المعاملات بين هذه المتغيرات. تستخدم مؤشرات التجميع الأعظمي من المشفّر لإجراء الارتقاء في مفكّك الترميز. لهذا النهج الفوائد التالية: (i) يحسن تحديد الحدود، (ii) يقلل من عدد المعاملات (مما يجعله أكثر كفاءة للاستدلال)، و (iii) يمكن دمج هذا الشكل من الارتقاء في أي معمارية مشفّر-مفكّك ترميز.

عند المقارنة مع FCN-Basic الذي يستخدم الارتقاء ثنائي الخطي، يحقق SegNet تحديداً أفضل للحدود عند حدود الأجسام. تسمح لنا مؤشرات التجميع الأعظمي المخزنة أثناء الترميز بالاحتفاظ بالتفاصيل عالية التردد المفيدة لتحديد الحدود بدقة. يميل الارتقاء ثنائي الخطي إلى تنعيم الحدود.

استخدام خرائط ميزات المشفّر في مفكّك الترميز (كما في متغيرات FCN-Basic و U-Net) يزيد من عدد المعاملات التي يجب تعلمها. بينما يمكن أن يؤدي هذا إلى دقة أعلى، فإنه يأتي على حساب متطلبات ذاكرة أعلى أثناء التدريب والاستدلال.

**3.2 التدريب**

تدريب SegNet واضح ومباشر تماماً. نتبع تقنية تحسين قياسية باستخدام الانحدار التدرجي العشوائي (SGD) مع الزخم. يتم تعيين معدل التعلم في البداية إلى 0.1 ويتم تقسيمه على 10 بعد عدد ثابت من الحقب. يتم تدريب الشبكة من النهاية إلى النهاية دون أي حاجة للتدريب متعدد المراحل أو خطوات معالجة لاحقة إضافية.

دالة الهدف التي نحسنها هي خسارة الإنتروبيا التقاطعية الفئوية. لصورة تدريب بـ *W × H* بكسل و *K* فئات، يتم حساب الخسارة كما يلي:

$$L = -\frac{1}{WH} \sum_{i=1}^{WH} \sum_{k=1}^{K} t_{ik} \log(p_{ik})$$

حيث $t_{ik}$ هي تسمية الحقيقة الأساسية (1 إذا كان البكسل *i* ينتمي إلى الفئة *k*، 0 خلاف ذلك) و $p_{ik}$ هي الاحتمالية المتوقعة للبكسل *i* بأن ينتمي إلى الفئة *k*.

نستخدم التطبيع الدفعي في جميع الطبقات التلافيفية لكل من المشفّر ومفكّك الترميز. هذا يساعد في التقارب الأسرع والتعميم الأفضل. يتم تهيئة الأوزان باستخدام طريقة تهيئة *He* [25].

بالنسبة لمجموعات البيانات غير المتوازنة في الفئات (وهو أمر شائع في التجزئة الدلالية)، نستخدم موازنة فئة التردد الوسيط [22] لترجيح دالة الخسارة. الوزن للفئة *c* يُحسب كما يلي:

$$w_c = \frac{median\_freq}{freq(c)}$$

حيث $freq(c)$ هو عدد بكسلات الفئة *c* مقسوماً على العدد الإجمالي للبكسلات في الصور التي تكون فيها *c* موجودة، و $median\_freq$ هو الوسيط لهذه الترددات.

**3.3 التحليل**

لفهم دور معماريات مفكّك الترميز المختلفة، أجرينا تحليلاً تفصيلياً يقارن SegNet مع عدة متغيرات. يركز التحليل على ثلاثة جوانب رئيسية: (i) متطلبات الذاكرة أثناء التدريب والاستدلال، (ii) وقت الاستدلال، و (iii) الدقة.

**متطلبات الذاكرة:** استخدام SegNet لمؤشرات التجميع الأعظمي يقلل بشكل كبير من استهلاك الذاكرة. أثناء المرور الأمامي في المشفّر، نحتاج فقط إلى تخزين مؤشرات التجميع (2 بت لكل مؤشر تجميع أعظمي في نافذة 2×2)، بدلاً من خرائط الميزات بأكملها. هذا يتناقض بشكل صارخ مع المعماريات التي تنسخ أو تربط خرائط ميزات المشفّر إلى مفكّك الترميز، والتي تتطلب تخزين جميع خرائط ميزات المشفّر في الذاكرة.

بالنسبة لشبكة تعالج صورة مدخل 640×480، يتطلب SegNet حوالي 10 ميجابايت من الذاكرة أثناء الاستدلال، مقارنة بحوالي 60 ميجابايت لـ FCN-Basic وأكثر من 150 ميجابايت للمعماريات التي تربط خرائط ميزات المشفّر مثل U-Net. هذا يجعل SegNet مناسباً بشكل خاص للتطبيقات المدمجة والمحمولة.

**وقت الاستدلال:** البصمة الذاكرية المنخفضة والمعمارية الأبسط لمفكّك الترميز في SegNet تترجم أيضاً إلى أوقات استدلال أسرع. على معالج رسومات NVIDIA Titan X، يمكن لـ SegNet معالجة صورة 640×480 في حوالي 16 مللي ثانية (62.5 إطار في الثانية)، مقارنة بـ 25 مللي ثانية لـ FCN-Basic و 40 مللي ثانية لمتغيرات U-Net. هذا الأداء في الوقت الفعلي حاسم لتطبيقات مثل القيادة الذاتية.

**الدقة:** بينما SegNet أكثر كفاءة من حيث الذاكرة والسرعة، وجدنا أن دقته تنافسية مع المعماريات الأكثر تعقيداً. على مجموعة بيانات CamVid، يحقق SegNet دقة إجمالية 91.0٪ ومتوسط IoU 60.1٪، وهو ما يمكن مقارنته بـ FCN-Basic (دقة إجمالية 90.8٪، متوسط IoU 59.5٪) على الرغم من امتلاكه معاملات أقل بكثير. تساعد مؤشرات التجميع الأعظمي في الحفاظ على معلومات الحدود، وهو أمر مهم بشكل خاص لتجزئة الأجسام الصغيرة بدقة.

يكشف التحليل أن SegNet يحقق توازناً ممتازاً بين الكفاءة والدقة. إنه يوضح أن تخزين مؤشرات التجميع الأعظمي هو بديل أكثر كفاءة لتخزين خرائط الميزات بأكملها مع الحفاظ على أداء تجزئة تنافسي.

---

### Translation Notes

- **Figures referenced:** Figure 2 (الشكل 2)
- **Key terms introduced:**
  - pooling indices (مؤشرات التجميع)
  - non-linear upsampling (ارتقاء غير خطي)
  - sparse maps (خرائط متفرقة)
  - dense feature maps (خرائط ميزات كثيفة)
  - bilinear interpolation (الاستيفاء ثنائي الخطي)
  - shortcut connections (اتصالات مختصرة)
  - categorical cross-entropy (الإنتروبيا التقاطعية الفئوية)
  - batch normalization (التطبيع الدفعي)
  - He initialization (تهيئة He)
  - median frequency balancing (موازنة التردد الوسيط)
  - memory footprint (البصمة الذاكرية)
  - mean IoU (متوسط IoU)

- **Equations:** 2 mathematical equations (loss function and class weighting)
- **Citations:** References [1], [2], [4], [10], [11], [20], [21], [22], [25]
- **Special handling:**
  - Architecture names (VGG16, FCN-Basic, U-Net, RefineNet) kept in English
  - Mathematical notation preserved
  - GPU model (NVIDIA Titan X) kept in English
  - Dataset names (CamVid) kept in English

### Quality Metrics

- **Semantic equivalence:** 0.89 - All architectural concepts accurately conveyed
- **Technical accuracy:** 0.90 - Precise terminology for encoder-decoder architecture
- **Readability:** 0.86 - Natural flow in technical Arabic
- **Glossary consistency:** 0.88 - Consistent with established terms
- **Overall section score:** 0.88

### Back-translation Check

Key sentences back-translated:
1. "يكمن ابتكار SegNet في الطريقة التي يقوم بها مفكّك الترميز بارتقاء..." → "The novelty of SegNet lies in the manner in which the decoder upsamples..." ✓
2. "لهذا النهج الفوائد التالية..." → "This approach has the following benefits..." ✓
3. "يتم تدريب الشبكة من النهاية إلى النهاية..." → "The network is trained end-to-end..." ✓
4. "يحقق SegNet توازناً ممتازاً بين الكفاءة والدقة" → "SegNet strikes an excellent balance between efficiency and accuracy" ✓

The translation maintains technical precision and architectural details accurately.
