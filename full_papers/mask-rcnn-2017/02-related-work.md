# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** R-CNN, Fast R-CNN, Faster R-CNN, Region Proposal Network (RPN), instance segmentation, semantic segmentation, DeepMask, SharpMask, MultiPathNet, FCIS

---

### English Version

Our approach is related to a large body of prior work in object detection, instance segmentation, and semantic segmentation. In particular, it builds on the R-CNN family of methods.

**R-CNN:** The Region-based CNN (R-CNN) approach to bounding-box object detection is to attend to a manageable number of candidate object regions and evaluate convolutional networks independently on each RoI. R-CNN was extended to allow attending to RoIs on feature maps using RoIPool, leading to Fast R-CNN, which is the current leading framework for object detection. Faster R-CNN advanced this stream by learning the attention mechanism with a Region Proposal Network (RPN). Faster R-CNN is flexible and robust to many follow-up improvements (e.g., feature pyramids), and is the current leading framework in several benchmarks.

**Instance Segmentation:** Driven by the success of R-CNN, many approaches to instance segmentation are based on segment proposals. Earlier methods resorted to bottom-up segments. DeepMask and following works learn to propose segment candidates, which are then classified by Fast R-CNN. In these methods, segmentation precedes recognition, which is slow and less accurate. Likewise, Dai et al. proposed a complex multiple-stage cascade that predicts segment proposals from bounding-box proposals, followed by classification. Instead, our method is based on parallel prediction of masks and class labels, which is simpler and more flexible.

Most recently, Li et al. presented a fully convolutional instance segmentation method (FCIS) that achieves competitive results. In contrast to the segmentation-first strategy of previous works, FCIS is based on an instance-first strategy. Unlike Mask R-CNN, FCIS builds on top of position-sensitive output channels that are fully shared for mask prediction and classification. Our experimental comparisons show that this leads to systematic errors, particularly evident in overlapping instances. FCIS also exhibits systematic errors on objects that are significantly smaller or larger than the training window size.

Our method, Mask R-CNN, is also related to recent work on human pose estimation. In these methods, keypoints are detected as a separate process following object detection. Mask R-CNN can be viewed as a generalization of these approaches, where the mask prediction branch replaces the keypoint detection branch.

---

### النسخة العربية

يرتبط نهجنا بمجموعة كبيرة من الأعمال السابقة في الكشف عن الكائنات، وتجزئة نسخ الكائنات، والتجزئة الدلالية. على وجه الخصوص، يبني على عائلة طرق آر-سي إن إن (R-CNN).

**آر-سي إن إن:** نهج الشبكة العصبية الالتفافية القائمة على المناطق (R-CNN) للكشف عن الكائنات بصناديق التحديد هو الانتباه إلى عدد يمكن التحكم فيه من مناطق الكائنات المرشحة وتقييم الشبكات الالتفافية بشكل مستقل على كل منطقة اهتمام (RoI). تم توسيع آر-سي إن إن للسماح بالانتباه إلى مناطق الاهتمام على خرائط الميزات باستخدام آر أو آي بول (RoIPool)، مما أدى إلى فاست آر-سي إن إن، وهو الإطار الرائد الحالي للكشف عن الكائنات. طورت فاستر آر-سي إن إن (Faster R-CNN) هذا المسار بتعلم آلية الانتباه باستخدام شبكة مقترحات المناطق (Region Proposal Network - RPN). فاستر آر-سي إن إن مرنة ومتينة أمام العديد من التحسينات اللاحقة (مثل أهرامات الميزات)، وهي الإطار الرائد الحالي في العديد من المعايير المرجعية.

**تجزئة نسخ الكائنات:** مدفوعة بنجاح آر-سي إن إن، تستند العديد من الأساليب لتجزئة نسخ الكائنات إلى مقترحات القطع. لجأت الطرق المبكرة إلى القطع من الأسفل إلى الأعلى. ديب ماسك (DeepMask) والأعمال التالية تتعلم اقتراح مرشحي القطع، والتي يتم تصنيفها بعد ذلك بواسطة فاست آر-سي إن إن. في هذه الطرق، تسبق التجزئة التعرف، وهو أمر بطيء وأقل دقة. وبالمثل، اقترح داي وآخرون تتالياً متعدد المراحل معقداً يتنبأ بمقترحات القطع من مقترحات صناديق التحديد، متبوعاً بالتصنيف. بدلاً من ذلك، تستند طريقتنا إلى التنبؤ المتوازي للأقنعة وتسميات الفئات، وهو أبسط وأكثر مرونة.

في الآونة الأخيرة، قدم لي وآخرون طريقة تجزئة نسخ كائنات التفافية كاملة (FCIS) تحقق نتائج تنافسية. على النقيض من استراتيجية التجزئة أولاً للأعمال السابقة، تستند FCIS إلى استراتيجية النسخة أولاً. على عكس ماسك آر-سي إن إن، تبني FCIS على قنوات إخراج حساسة للموقع يتم مشاركتها بالكامل للتنبؤ بالقناع والتصنيف. تُظهر مقارناتنا التجريبية أن هذا يؤدي إلى أخطاء منهجية، واضحة بشكل خاص في النسخ المتداخلة. تُظهر FCIS أيضاً أخطاء منهجية على الكائنات الأصغر أو الأكبر بكثير من حجم نافذة التدريب.

ترتبط طريقتنا، ماسك آر-سي إن إن، أيضاً بالأعمال الحديثة على تقدير وضعية الإنسان. في هذه الطرق، يتم الكشف عن النقاط المفصلية كعملية منفصلة بعد الكشف عن الكائنات. يمكن النظر إلى ماسك آر-سي إن إن كتعميم لهذه الأساليب، حيث يحل فرع التنبؤ بالقناع محل فرع الكشف عن النقاط المفصلية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - R-CNN family (عائلة آر-سي إن إن)
  - Region Proposal Network (شبكة مقترحات المناطق)
  - RoIPool (آر أو آي بول)
  - DeepMask (ديب ماسك)
  - FCIS - Fully Convolutional Instance Segmentation (التجزئة الالتفافية الكاملة لنسخ الكائنات)
  - Position-sensitive (حساسة للموقع)
  - Bottom-up segments (قطع من الأسفل إلى الأعلى)
  - Keypoint detection (الكشف عن النقاط المفصلية)
  - Pose estimation (تقدير الوضعية)
- **Equations:** None
- **Citations:** References to R-CNN, Fast R-CNN, Faster R-CNN, DeepMask, SharpMask, FCIS, and various instance segmentation methods
- **Special handling:**
  - Model names kept in English with Arabic transliteration
  - Technical architectural terms translated consistently with glossary
  - Acronyms like RPN, FCIS explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
