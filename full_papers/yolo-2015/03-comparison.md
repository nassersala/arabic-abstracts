# Section 3: Comparison to Other Detection Systems
## القسم 3: المقارنة بأنظمة الكشف الأخرى

**Section:** comparison
**Translation Quality:** 0.86
**Glossary Terms Used:** object detection, feature extraction, classifier, sliding window, bounding box, convolutional neural network, region proposal, non-maximal suppression, real-time, pipeline, SVM, localization

---

### English Version

Object detection is a core problem in computer vision. Detection pipelines generally start by extracting a set of robust features from input images (Haar, SIFT, HOG, convolutional features). Then, classifiers or localizers are used to identify objects in the feature space. These classifiers or localizers are run either in sliding window fashion over the whole image or on some subset of regions in the image. We compare the YOLO detection system to several top detection frameworks, highlighting key similarities and differences.

**Deformable parts models.** Deformable parts models (DPM) use a sliding window approach to object detection. DPM uses a disjoint pipeline to extract static features, classify regions, predict bounding boxes for high scoring regions, etc. Our system replaces all of these disparate parts with a single convolutional neural network. The network performs feature extraction, bounding box prediction, non-maximal suppression, and contextual reasoning all concurrently. Instead of static features, the network trains the features in-line and optimizes them for the detection task. Our unified architecture leads to a faster, more accurate model than DPM.

**R-CNN.** R-CNN and its variants use region proposals instead of sliding windows to find objects in images. Selective Search generates potential bounding boxes, a convolutional network extracts features, an SVM scores the boxes, a linear model adjusts the bounding boxes, and non-max suppression eliminates duplicate detections. Each stage of this complex pipeline must be precisely tuned independently and the resulting system is very slow, taking more than 40 seconds per image at test time.

YOLO shares some similarities with R-CNN. Each grid cell proposes potential bounding boxes and scores those boxes using convolutional features. However, our system puts spatial constraints on the grid cell proposals which helps mitigate multiple detections of the same object. Our system also proposes far fewer bounding boxes, only 98 per image compared to about 2000 from Selective Search. Finally, our system combines these individual components into a single, jointly optimized model.

**Other Fast Detectors** Fast and Faster R-CNN focus on speeding up the R-CNN framework by sharing computation and using neural networks to propose regions instead of Selective Search. While they offer speed and accuracy improvements over R-CNN, both still fall short of real-time performance.

Many research efforts focus on speeding up the DPM pipeline. They speed up HOG computation, use cascades, and push computation to GPUs. However, only 30Hz DPM actually runs in real-time.

Instead of trying to optimize individual components of a large detection pipeline, YOLO throws out the pipeline entirely and is fast by design.

Detectors for single classes like faces or people can be highly optimized since they have to deal with much less variation. YOLO is a general purpose detector that learns to detect a variety of objects simultaneously.

**Deep MultiBox.** Unlike R-CNN, Szegedy et al. train a convolutional neural network to predict regions of interest instead of using Selective Search. MultiBox can also perform single object detection by replacing the confidence prediction with a single class prediction. However, MultiBox cannot perform general object detection and is still just a piece in a larger detection pipeline, requiring further image patch classification. Both YOLO and MultiBox use a convolutional network to predict bounding boxes in an image but YOLO is a complete detection system.

**OverFeat.** Sermanet et al. train a convolutional neural network to perform localization and adapt that localizer to perform detection. OverFeat efficiently performs sliding window detection but it is still a disjoint system. OverFeat optimizes for localization, not detection performance. Like DPM, the localizer only sees local information when making a prediction. OverFeat cannot reason about global context and thus requires significant post-processing to produce coherent detections.

**MultiGrasp.** Our work is similar in design to work on grasp detection by Redmon et al. Our grid approach to bounding box prediction is based on the MultiGrasp system for regression to grasps. However, grasp detection is a much simpler task than object detection. MultiGrasp only needs to predict a single graspable region for an image containing one object. It doesn't have to estimate the size, location, or boundaries of the object or predict it's class, only find a region suitable for grasping. YOLO predicts both bounding boxes and class probabilities for multiple objects of multiple classes in an image.

---

### النسخة العربية

كشف الأجسام هو مشكلة أساسية في الرؤية الحاسوبية. تبدأ خطوط أنابيب الكشف عموماً باستخراج مجموعة من الميزات القوية من صور الإدخال (Haar، SIFT، HOG، الميزات الالتفافية). ثم تُستخدم المصنفات أو محددات الموقع لتحديد الأجسام في فضاء الميزات. تعمل هذه المصنفات أو محددات الموقع إما بطريقة النافذة المنزلقة على الصورة بأكملها أو على مجموعة فرعية من المناطق في الصورة. نقارن نظام الكشف YOLO بالعديد من أطر الكشف الرائدة، مع تسليط الضوء على أوجه التشابه والاختلاف الرئيسية.

**نماذج الأجزاء القابلة للتشوه.** تستخدم نماذج الأجزاء القابلة للتشوه (DPM) نهج النافذة المنزلقة لكشف الأجسام. يستخدم DPM خط أنابيب منفصل لاستخراج الميزات الثابتة، وتصنيف المناطق، والتنبؤ بصناديق التحديد للمناطق ذات الدرجات العالية، إلخ. يستبدل نظامنا كل هذه الأجزاء المتباينة بشبكة عصبية التفافية واحدة. تقوم الشبكة باستخراج الميزات، والتنبؤ بصندوق التحديد، وقمع غير الأعظمي، والاستدلال السياقي كلها في وقت واحد. بدلاً من الميزات الثابتة، تدرب الشبكة الميزات مباشرة وتحسنها لمهمة الكشف. تؤدي معماريتنا الموحدة إلى نموذج أسرع وأكثر دقة من DPM.

**R-CNN.** تستخدم R-CNN ومتغيراتها اقتراح المناطق بدلاً من النوافذ المنزلقة للعثور على الأجسام في الصور. يولد البحث الانتقائي صناديق تحديد محتملة، وتستخرج شبكة التفافية الميزات، وتقوم آلة المتجهات الداعمة (SVM) بتقييم الصناديق، ويضبط نموذج خطي صناديق التحديد، ويزيل قمع غير الأعظمي الكشوفات المكررة. يجب ضبط كل مرحلة من هذا خط الأنابيب المعقد بدقة بشكل مستقل والنظام الناتج بطيء جداً، حيث يستغرق أكثر من 40 ثانية لكل صورة في وقت الاختبار.

يشترك YOLO في بعض أوجه التشابه مع R-CNN. تقترح كل خلية شبكة صناديق تحديد محتملة وتقيّم تلك الصناديق باستخدام الميزات الالتفافية. ومع ذلك، يضع نظامنا قيوداً مكانية على مقترحات خلايا الشبكة مما يساعد على التخفيف من الكشوفات المتعددة لنفس الجسم. يقترح نظامنا أيضاً عدداً أقل بكثير من صناديق التحديد، 98 فقط لكل صورة مقارنة بحوالي 2000 من البحث الانتقائي. أخيراً، يجمع نظامنا هذه المكونات الفردية في نموذج واحد محسّن بشكل مشترك.

**كاشفات سريعة أخرى** يركز Fast وFaster R-CNN على تسريع إطار عمل R-CNN من خلال مشاركة الحوسبة واستخدام الشبكات العصبية لاقتراح المناطق بدلاً من البحث الانتقائي. بينما يقدمان تحسينات في السرعة والدقة على R-CNN، كلاهما لا يزال قاصراً عن الأداء في الوقت الفعلي.

تركز العديد من جهود البحث على تسريع خط أنابيب DPM. إنهم يسرعون حساب HOG، ويستخدمون التتابعات، ويدفعون الحوسبة إلى معالجات الرسومات. ومع ذلك، فقط DPM بسرعة 30Hz يعمل فعلياً في الوقت الفعلي.

بدلاً من محاولة تحسين المكونات الفردية لخط أنابيب كشف كبير، يتخلص YOLO من خط الأنابيب بالكامل وهو سريع بالتصميم.

يمكن تحسين الكاشفات لفئات فردية مثل الوجوه أو الأشخاص بشكل كبير نظراً لأنها تتعامل مع تباين أقل بكثير. YOLO هو كاشف متعدد الأغراض يتعلم اكتشاف مجموعة متنوعة من الأجسام في وقت واحد.

**Deep MultiBox.** على عكس R-CNN، يدرب Szegedy وآخرون شبكة عصبية التفافية للتنبؤ بمناطق الاهتمام بدلاً من استخدام البحث الانتقائي. يمكن لـ MultiBox أيضاً إجراء كشف جسم واحد عن طريق استبدال التنبؤ بالثقة بتنبؤ فئة واحدة. ومع ذلك، لا يمكن لـ MultiBox إجراء كشف أجسام عام ولا يزال مجرد قطعة في خط أنابيب كشف أكبر، يتطلب مزيداً من تصنيف رقعة الصورة. يستخدم كل من YOLO وMultiBox شبكة التفافية للتنبؤ بصناديق التحديد في صورة ولكن YOLO هو نظام كشف كامل.

**OverFeat.** يدرب Sermanet وآخرون شبكة عصبية التفافية لتنفيذ التحديد الموضعي ويكيفون ذلك محدد الموقع لتنفيذ الكشف. ينفذ OverFeat كشف النافذة المنزلقة بكفاءة ولكنه لا يزال نظاماً منفصلاً. يحسن OverFeat للتحديد الموضعي، وليس لأداء الكشف. مثل DPM، يرى محدد الموقع المعلومات المحلية فقط عند إجراء التنبؤ. لا يمكن لـ OverFeat الاستدلال حول السياق العام وبالتالي يتطلب معالجة لاحقة كبيرة لإنتاج كشوفات متماسكة.

**MultiGrasp.** عملنا مشابه في التصميم للعمل على كشف القبضة بواسطة Redmon وآخرون. يعتمد نهج الشبكة لدينا للتنبؤ بصندوق التحديد على نظام MultiGrasp للانحدار إلى القبضات. ومع ذلك، فإن كشف القبضة مهمة أبسط بكثير من كشف الأجسام. يحتاج MultiGrasp فقط إلى التنبؤ بمنطقة واحدة قابلة للقبض لصورة تحتوي على جسم واحد. لا يتعين عليه تقدير حجم أو موقع أو حدود الجسم أو التنبؤ بفئته، بل فقط إيجاد منطقة مناسبة للقبض. يتنبأ YOLO بكل من صناديق التحديد واحتماليات الفئة لأجسام متعددة من فئات متعددة في صورة.

---

### Translation Notes

- **Key systems compared:** DPM, R-CNN, Fast R-CNN, Faster R-CNN, Deep MultiBox, OverFeat, MultiGrasp
- **Key terms introduced:** Deformable parts models, region proposal, Selective Search, SVM, localizer, disjoint pipeline, HOG, cascade
- **Performance metrics:** 98 boxes (YOLO) vs 2000 (Selective Search), >40 seconds per image (R-CNN), 30Hz (real-time DPM)
- **Technical features:** Haar, SIFT, HOG features mentioned
- **Citations:** References to Szegedy et al., Sermanet et al., Redmon et al.
- **Special handling:** Preserved algorithm names (DPM, R-CNN, OverFeat, MultiBox), kept acronyms

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
