# Section 3: Comparison to Other Detection Systems
## القسم 3: المقارنة مع أنظمة الكشف الأخرى

**Section:** Comparison to Other Detection Systems
**Translation Quality:** 0.86
**Glossary Terms Used:** object detection, classification, localization, sliding window, region proposal, neural network, convolutional, deep learning, bounding box, feature extraction, real-time

---

### English Version

Object detection is a core problem in computer vision. The detection pipeline typically involves extracting a set of robust features from input images (Haar [25], SIFT [23], HOG [4], convolutional features [6]), then using a classifier or localizer to identify objects in the feature space. These classifiers or localizers are run either in sliding window fashion over the whole image or on some subset of regions in the image [35, 15, 39]. We compare the YOLO detection system to several top detection frameworks, highlighting key similarities and differences.

**Deformable parts models.** Deformable parts models (DPM) use a sliding window approach to object detection [10]. DPM uses a disjoint pipeline to extract static features, classify regions, predict bounding boxes for high scoring regions, etc. Our system replaces all of these disparate parts with a single convolutional neural network. The network performs feature extraction, bounding box prediction, non-maximum suppression, and contextual reasoning all concurrently. Instead of static features, the network trains the features in-line and optimizes them for the detection task. Our unified architecture leads to a faster, more accurate model than DPM.

**R-CNN.** R-CNN and its variants use region proposals instead of sliding windows to find objects in images. Selective Search [35] generates potential bounding boxes, a convolutional network extracts features, an SVM scores the boxes, a linear model adjusts the bounding boxes, and non-maximum suppression eliminates duplicate detections. Each stage of this complex pipeline must be precisely tuned independently and the resulting system is very slow, taking more than 40 seconds per image at test time.

YOLO shares some similarities with R-CNN. Each grid cell proposes potential bounding boxes and scores those boxes using convolutional features. However, our system puts spatial constraints on the grid cell proposals which helps mitigate multiple detections of the same object. Our system also proposes far fewer bounding boxes, only 98 per image compared to about 2000 from Selective Search. Finally, our system combines these individual components into a single, jointly optimized model.

**Other Fast Detectors.** Fast and Faster R-CNN focus on speeding up the R-CNN framework by sharing computation and using neural networks to propose regions instead of Selective Search [14][28]. While they offer speed and accuracy improvements over R-CNN, both still fall short of real-time performance.

Many research efforts focus on speeding up the DPM pipeline [31][38][5]. They speed up HOG computation, use cascades, and push computation to GPUs. However, only 30Hz DPM [31] actually runs in real-time.

Instead of trying to optimize individual components of a large detection pipeline, YOLO throws out the pipeline entirely and is fast by design.

Detectors for single classes like faces or people can be highly optimized since they have to deal with much less variation [37]. YOLO is a general purpose detector that learns to detect a variety of objects simultaneously.

**Deep MultiBox.** Unlike R-CNN, Szegedy et al. train a convolutional neural network to predict regions of interest [8] instead of using Selective Search. MultiBox can also perform single object detection by replacing the confidence prediction with a single class prediction. However, MultiBox cannot perform general object detection and is still just a piece in a larger detection pipeline, requiring further image patch classification. Both YOLO and MultiBox use a convolutional network to predict bounding boxes in an image but YOLO is a complete detection system.

**OverFeat.** Szegedy et al. train a convolutional neural network to perform localization and adapt that localizer to perform detection [32]. OverFeat efficiently performs sliding window detection but it is still a disjoint system. OverFeat optimizes for localization, not detection performance. Like DPM, the localizer only sees local information when making a prediction. OverFeat cannot reason about global context and thus requires significant post-processing to produce coherent detections.

**MultiGrasp.** Our work is similar in design to Redmon et al.'s work on grasp detection [27]. Our grid approach to bounding box prediction is based on the MultiGrasp system for regression to grasps. However, grasp detection is a much simpler task than object detection. MultiGrasp only needs to predict a single graspable region for an image containing one object. It doesn't have to estimate the size, location, or boundaries of the object or predict its class, only find a region suitable for grasping. YOLO predicts both bounding boxes and class probabilities for multiple objects of multiple classes in an image.

---

### النسخة العربية

كشف الأجسام هو مشكلة أساسية في الرؤية الحاسوبية. يتضمن خط أنابيب الكشف عادةً استخراج مجموعة من الميزات القوية من صور الإدخال (Haar [25]، SIFT [23]، HOG [4]، الميزات الالتفافية [6])، ثم استخدام مصنف أو محدد موقع لتحديد الأجسام في فضاء الميزات. يتم تشغيل هذه المصنفات أو محددات المواقع إما بطريقة النافذة المنزلقة على الصورة بأكملها أو على مجموعة فرعية من المناطق في الصورة [35، 15، 39]. نقارن نظام كشف YOLO بعدة أطر كشف رائدة، مع تسليط الضوء على أوجه التشابه والاختلاف الرئيسية.

**نماذج الأجزاء القابلة للتشوه.** تستخدم نماذج الأجزاء القابلة للتشوه (DPM) نهج النافذة المنزلقة لكشف الأجسام [10]. يستخدم DPM خط أنابيب منفصل لاستخراج الميزات الثابتة، وتصنيف المناطق، والتنبؤ بصناديق التحديد للمناطق ذات الدرجات العالية، إلخ. يستبدل نظامنا كل هذه الأجزاء المتباينة بشبكة عصبية التفافية واحدة. تؤدي الشبكة استخراج الميزات، والتنبؤ بصندوق التحديد، وقمع عدم الحد الأقصى، والاستنتاج السياقي كلها في وقت واحد. بدلاً من الميزات الثابتة، تدرب الشبكة الميزات ضمنياً وتحسنها لمهمة الكشف. تؤدي معماريتنا الموحدة إلى نموذج أسرع وأكثر دقة من DPM.

**R-CNN.** تستخدم R-CNN ومتغيراتها اقتراحات المناطق بدلاً من النوافذ المنزلقة للعثور على الأجسام في الصور. يولد Selective Search [35] صناديق تحديد محتملة، وتستخرج شبكة التفافية الميزات، ويسجل SVM الصناديق، ويضبط نموذج خطي صناديق التحديد، ويزيل قمع عدم الحد الأقصى الاكتشافات المكررة. يجب ضبط كل مرحلة من هذا الخط المعقد بدقة بشكل مستقل والنظام الناتج بطيء جداً، يستغرق أكثر من 40 ثانية لكل صورة في وقت الاختبار.

يشترك YOLO في بعض أوجه التشابه مع R-CNN. تقترح كل خلية شبكة صناديق تحديد محتملة وتسجل تلك الصناديق باستخدام الميزات الالتفافية. ومع ذلك، يضع نظامنا قيوداً مكانية على اقتراحات خلايا الشبكة مما يساعد على تخفيف الاكتشافات المتعددة لنفس الجسم. يقترح نظامنا أيضاً عدداً أقل بكثير من صناديق التحديد، 98 فقط لكل صورة مقارنة بحوالي 2000 من Selective Search. أخيراً، يجمع نظامنا هذه المكونات الفردية في نموذج واحد محسّن بشكل مشترك.

**كاشفات سريعة أخرى.** تركز Fast وFaster R-CNN على تسريع إطار عمل R-CNN من خلال مشاركة الحساب واستخدام الشبكات العصبية لاقتراح المناطق بدلاً من Selective Search [14][28]. بينما تقدم تحسينات في السرعة والدقة على R-CNN، لا يزال كلاهما يقصر عن الأداء في الوقت الفعلي.

تركز العديد من جهود البحث على تسريع خط أنابيب DPM [31][38][5]. تسرع حساب HOG، وتستخدم التتابعات، وتدفع الحساب إلى وحدات معالجة الرسومات. ومع ذلك، فإن DPM 30Hz [31] فقط يعمل فعلياً في الوقت الفعلي.

بدلاً من محاولة تحسين المكونات الفردية لخط أنابيب كشف كبير، يتخلص YOLO من خط الأنابيب بالكامل ويكون سريعاً بالتصميم.

يمكن تحسين الكاشفات لفئات فردية مثل الوجوه أو الأشخاص بشكل كبير نظراً لأنها يجب أن تتعامل مع تباين أقل بكثير [37]. YOLO هو كاشف للأغراض العامة يتعلم اكتشاف مجموعة متنوعة من الأجسام في وقت واحد.

**Deep MultiBox.** على عكس R-CNN، يدرب Szegedy et al. شبكة عصبية التفافية للتنبؤ بمناطق الاهتمام [8] بدلاً من استخدام Selective Search. يمكن لـ MultiBox أيضاً إجراء كشف جسم واحد عن طريق استبدال تنبؤ الثقة بتنبؤ فئة واحدة. ومع ذلك، لا يمكن لـ MultiBox إجراء كشف أجسام عام وهو لا يزال مجرد قطعة في خط أنابيب كشف أكبر، يتطلب مزيداً من تصنيف رقع الصورة. يستخدم كل من YOLO وMultiBox شبكة التفافية للتنبؤ بصناديق التحديد في صورة ولكن YOLO هو نظام كشف كامل.

**OverFeat.** يدرب Szegedy et al. شبكة عصبية التفافية لإجراء التحديد الموضعي ويكيف ذلك المحدد لإجراء الكشف [32]. يقوم OverFeat بكفاءة بكشف النافذة المنزلقة ولكنه لا يزال نظاماً منفصلاً. يحسن OverFeat للتحديد الموضعي، وليس أداء الكشف. مثل DPM، يرى المحدد الموضعي فقط المعلومات المحلية عند إجراء تنبؤ. لا يمكن لـ OverFeat الاستنتاج حول السياق العالمي وبالتالي يتطلب معالجة لاحقة كبيرة لإنتاج اكتشافات متماسكة.

**MultiGrasp.** عملنا مشابه في التصميم لعمل Redmon et al. على كشف القبضة [27]. نهجنا الشبكي للتنبؤ بصندوق التحديد يعتمد على نظام MultiGrasp للانحدار إلى القبضات. ومع ذلك، فإن كشف القبضة مهمة أبسط بكثير من كشف الأجسام. يحتاج MultiGrasp فقط للتنبؤ بمنطقة واحدة قابلة للقبض لصورة تحتوي على جسم واحد. لا يحتاج إلى تقدير الحجم أو الموقع أو حدود الجسم أو التنبؤ بفئته، فقط العثور على منطقة مناسبة للقبض. يتنبأ YOLO بصناديق التحديد واحتماليات الفئة لأجسام متعددة من فئات متعددة في صورة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** DPM (Deformable Parts Models), R-CNN, Fast R-CNN, Faster R-CNN, Selective Search, SVM (Support Vector Machine), Deep MultiBox, OverFeat, MultiGrasp, HOG (Histogram of Oriented Gradients), SIFT, Haar features, cascade
- **Equations:** 0
- **Citations:** [4], [5], [6], [8], [10], [14], [15], [23], [25], [27], [28], [31], [32], [35], [37], [38], [39]
- **Special handling:**
  - Method names kept in English (R-CNN, DPM, OverFeat, etc.)
  - Technical terms explained in context
  - Performance numbers preserved (40 seconds, 98 boxes vs 2000 boxes, 30Hz)
  - Author names kept in English (Szegedy et al., Redmon et al.)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
