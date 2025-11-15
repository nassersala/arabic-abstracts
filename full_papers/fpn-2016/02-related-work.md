# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.88
**Glossary Terms Used:** features, neural network, object detection, segmentation, ConvNets, feature pyramid, architecture, accuracy

---

### English Version

**Hand-engineered features and early neural networks.**
SIFT features [25] were originally extracted at scale-space extrema and used for feature point matching. HOG features [5], and later SIFT features as well, were computed densely over entire image pyramids. These HOG and SIFT pyramids have been used in numerous works for image classification, object detection, human pose estimation, and more. There has also been significant interest in computing featurized image pyramids quickly. Dollár et al. [6] demonstrated fast pyramid computation by first computing a sparsely sampled (in scale) pyramid and then interpolating missing levels. Before HOG and SIFT, early work on face detection with ConvNets [38, 32] computed shallow networks over image pyramids to detect faces across scales.

**Deep ConvNet object detectors.** With the development of modern deep ConvNets [19], object detectors like OverFeat [34] and R-CNN [12] showed dramatic improvements in accuracy. OverFeat adopted a strategy similar to early neural network face detectors by applying a ConvNet as a sliding window detector on an image pyramid. R-CNN adopted a region proposal-based strategy [37] in which each proposal was scale-normalized before classifying with a ConvNet. SPPnet [15] demonstrated that such region-based detectors could be applied much more efficiently on feature maps extracted on a single image scale. Recent and more accurate detection methods like Fast R-CNN [11] and Faster R-CNN [29] advocate using features computed from a single scale, because it offers a good trade-off between accuracy and speed. Multi-scale detection, however, still performs better, especially for small objects.

**Methods using multiple layers.** A number of recent approaches improve detection and segmentation by using different layers in a ConvNet. FCN [24] sums partial scores for each category over multiple scales to compute semantic segmentations. Hypercolumns [13] uses a similar method for object instance segmentation. Several other approaches (HyperNet [18], ParseNet [23], and ION [2]) concatenate features of multiple layers before computing predictions, which is equivalent to summing transformed features. SSD [22] and MS-CNN [3] predict objects at multiple layers of the feature hierarchy without combining features or scores.

There are recent methods exploiting lateral/skip connections that associate low-level feature maps across resolutions and semantic levels, including U-Net [31] and SharpMask [28] for segmentation, Recombinator networks [17] for face detection, and Stacked Hourglass networks [26] for keypoint estimation. Ghiasi et al. [8] present a Laplacian pyramid presentation for FCNs to progressively refine segmentation. Although these methods adopt architectures with pyramidal shapes, they are unlike featurized image pyramids [5, 7, 34] where predictions are made independently at all levels, see Fig. 2. In fact, for the pyramidal architecture in Fig. 2 (top), image pyramids are still needed to recognize objects across multiple scales [28].

---

### النسخة العربية

**السمات المُصممة يدويًا والشبكات العصبية المبكرة.**
تم استخراج سمات SIFT [25] في الأصل عند نقاط التطرف في فضاء المقياس واستخدامها لمطابقة نقاط السمات. تم حساب سمات HOG [5]، وسمات SIFT لاحقًا أيضًا، بكثافة على أهرام الصور بأكملها. تم استخدام هذه الأهرام من HOG و SIFT في أعمال عديدة لتصنيف الصور، والكشف عن الأشياء، وتقدير وضعية الإنسان، والمزيد. كان هناك أيضًا اهتمام كبير بحساب أهرام الصور المُسمّتة بسرعة. أظهر Dollár وآخرون [6] حساب الهرم السريع عن طريق حساب هرم تم أخذ عيناته بشكل متفرق (من حيث المقياس) أولاً ثم استكمال المستويات المفقودة. قبل HOG و SIFT، حسبت الأعمال المبكرة حول الكشف عن الوجوه باستخدام الشبكات الالتفافية [38، 32] شبكات ضحلة على أهرام الصور للكشف عن الوجوه عبر المقاييس.

**كاشفات الأشياء بالشبكات الالتفافية العميقة.** مع تطوير الشبكات الالتفافية العميقة الحديثة [19]، أظهرت كاشفات الأشياء مثل OverFeat [34] و R-CNN [12] تحسينات هائلة في الدقة. اعتمدت OverFeat استراتيجية مماثلة لكاشفات الوجوه المبكرة بالشبكات العصبية من خلال تطبيق شبكة التفافية ككاشف نافذة منزلقة على هرم صورة. اعتمدت R-CNN استراتيجية قائمة على مقترحات المناطق [37] حيث تم تطبيع المقياس لكل مقترح قبل التصنيف باستخدام شبكة التفافية. أظهرت SPPnet [15] أن مثل هذه الكاشفات القائمة على المناطق يمكن تطبيقها بكفاءة أكبر بكثير على خرائط السمات المستخرجة على مقياس صورة واحد. تدعو طرق الكشف الأحدث والأكثر دقة مثل Fast R-CNN [11] و Faster R-CNN [29] إلى استخدام السمات المحسوبة من مقياس واحد، لأنها توفر توازنًا جيدًا بين الدقة والسرعة. ومع ذلك، لا يزال الكشف متعدد النطاقات يؤدي بشكل أفضل، خاصة بالنسبة للأشياء الصغيرة.

**الطرق التي تستخدم طبقات متعددة.** عدد من النهج الحديثة تُحسن الكشف والتجزئة باستخدام طبقات مختلفة في الشبكة الالتفافية. تجمع FCN [24] الدرجات الجزئية لكل فئة عبر مقاييس متعددة لحساب التجزئات الدلالية. تستخدم Hypercolumns [13] طريقة مماثلة لتجزئة مثيل الشيء. تسلسل عدة نهج أخرى (HyperNet [18]، ParseNet [23]، و ION [2]) سمات طبقات متعددة قبل حساب التنبؤات، وهو ما يعادل جمع السمات المحولة. تتنبأ SSD [22] و MS-CNN [3] بالأشياء في طبقات متعددة من التسلسل الهرمي للسمات دون دمج السمات أو الدرجات.

هناك طرق حديثة تستغل الاتصالات الجانبية/القافزة التي تربط خرائط السمات منخفضة المستوى عبر الدقة والمستويات الدلالية، بما في ذلك U-Net [31] و SharpMask [28] للتجزئة، وشبكات Recombinator [17] للكشف عن الوجوه، وشبكات Stacked Hourglass [26] لتقدير النقاط الرئيسية. يقدم Ghiasi وآخرون [8] عرض هرم Laplacian لشبكات FCN لتحسين التجزئة تدريجيًا. على الرغم من أن هذه الطرق تعتمد معماريات ذات أشكال هرمية، إلا أنها لا تشبه أهرام الصور المُسمّتة [5، 7، 34] حيث يتم إجراء التنبؤات بشكل مستقل على جميع المستويات، انظر الشكل 2. في الواقع، بالنسبة للمعمارية الهرمية في الشكل 2 (أعلى)، لا تزال أهرام الصور مطلوبة للتعرف على الأشياء عبر مقاييس متعددة [28].

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 3 (mentioned)
- **Key terms introduced:**
  - scale-space extrema: نقاط التطرف في فضاء المقياس
  - feature point matching: مطابقة نقاط السمات
  - region proposal: مقترحات المناطق
  - scale-normalized: تطبيع المقياس
  - sliding window: نافذة منزلقة
  - semantic segmentations: التجزئات الدلالية
  - keypoint estimation: تقدير النقاط الرئيسية
  - Laplacian pyramid: هرم Laplacian
- **Equations:** 0
- **Citations:** Multiple references [2-38], including SIFT, HOG, OverFeat, R-CNN, SPPnet, FCN, U-Net, etc.
- **Special handling:**
  - Technical names kept in English: SIFT, HOG, OverFeat, R-CNN, SPPnet, FCN, Hypercolumns, HyperNet, ParseNet, ION, SSD, MS-CNN, U-Net, SharpMask, Recombinator, Stacked Hourglass
  - "Dollár et al." kept as author reference

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.85
- **Overall section score:** 0.88

### Back-Translation Check

Key phrases verified:
- "السمات المُصممة يدويًا" → Hand-engineered features ✓
- "نقاط التطرف في فضاء المقياس" → Scale-space extrema ✓
- "كاشف نافذة منزلقة" → Sliding window detector ✓
- "مقترحات المناطق" → Region proposals ✓
- "التجزئات الدلالية" → Semantic segmentations ✓
- "الاتصالات الجانبية/القافزة" → Lateral/skip connections ✓
