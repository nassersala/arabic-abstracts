# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** object detection, bounding box, classifier, regression, convolutional network, real-time, frames per second, mean average precision, sliding window, region proposal, post-processing, unified model, generalizable

---

### English Version

Humans glance at an image and instantly know what objects are in the image, where they are, and how they interact. The human visual system is fast and accurate, allowing us to perform complex tasks like driving with little conscious thought. Fast, accurate algorithms for object detection would allow computers to drive cars without specialized sensors, enable assistive devices to convey real-time scene information to human users, and unlock the potential for general purpose, responsive robotic systems.

Current detection systems repurpose classifiers to perform detection. To detect an object, these systems take a classifier for that object and evaluate it at various locations and scales in a test image. Systems like deformable parts models (DPM) use a sliding window approach where the classifier is run at evenly spaced locations over the entire image [[10]].

More recent approaches like R-CNN use region proposal methods to first generate potential bounding boxes in an image and then run a classifier on these proposed boxes. After classification, post-processing is used to refine the bounding boxes, eliminate duplicate detections, and rescore the boxes based on other objects in the scene [[13]]. These complex pipelines are slow and hard to optimize because each individual component must be trained separately.

We reframe object detection as a single regression problem, straight from image pixels to bounding box coordinates and class probabilities. Using our system, you only look once (YOLO) at an image to predict what objects are present and where they are.

YOLO is refreshingly simple: see Figure [1]. A single convolutional network simultaneously predicts multiple bounding boxes and class probabilities for those boxes. YOLO trains on full images and directly optimizes detection performance. This unified model has several benefits over traditional methods of object detection.

First, YOLO is extremely fast. Since we frame detection as a regression problem we don't need a complex pipeline. We simply run our neural network on a new image at test time to predict detections. Our base network runs at 45 frames per second with no batch processing on a Titan X GPU and a fast version runs at more than 150 fps. This means we can process streaming video in real-time with less than 25 milliseconds of latency. Furthermore, YOLO achieves more than twice the mean average precision of other real-time systems. For a demo of our system running in real-time on a webcam please see our project webpage: http://pjreddie.com/yolo/.

Second, YOLO reasons globally about the image when making predictions. Unlike sliding window and region proposal-based techniques, YOLO sees the entire image during training and test time so it implicitly encodes contextual information about classes as well as their appearance. Fast R-CNN, a top detection method [[14]], mistakes background patches in an image for objects because it can't see the larger context. YOLO makes less than half the number of background errors compared to Fast R-CNN.

Third, YOLO learns generalizable representations of objects. When trained on natural images and tested on artwork, YOLO outperforms top detection methods like DPM and R-CNN by a wide margin. Since YOLO is highly generalizable it is less likely to break down when applied to new domains or unexpected inputs.

YOLO still lags behind state-of-the-art detection systems in accuracy. While it can quickly identify objects in images it struggles to precisely localize some objects, especially small ones. We examine these tradeoffs further in our experiments.

All of our training and testing code is open source. A variety of pretrained models are also available to download.

---

### النسخة العربية

ينظر البشر إلى صورة ما ويعرفون على الفور ما هي الأجسام الموجودة في الصورة، وأين تقع، وكيف تتفاعل. النظام البصري البشري سريع ودقيق، مما يسمح لنا بأداء مهام معقدة مثل القيادة دون الكثير من التفكير الواعي. ستسمح الخوارزميات السريعة والدقيقة لكشف الأجسام لأجهزة الكمبيوتر بقيادة السيارات دون مستشعرات متخصصة، وتمكين الأجهزة المساعدة من نقل معلومات المشهد في الوقت الفعلي إلى المستخدمين البشريين، وإطلاق إمكانات الأنظمة الروبوتية متعددة الأغراض والمستجيبة.

تعيد أنظمة الكشف الحالية توجيه المصنفات لتنفيذ الكشف. لاكتشاف جسم ما، تأخذ هذه الأنظمة مصنفاً لذلك الجسم وتقيّمه في مواقع ومقاييس مختلفة في صورة الاختبار. تستخدم أنظمة مثل نماذج الأجزاء القابلة للتشوه (DPM) نهج النافذة المنزلقة حيث يتم تشغيل المصنف في مواقع متباعدة بشكل متساوٍ على الصورة بأكملها [[10]].

تستخدم الأساليب الأحدث مثل R-CNN طرق اقتراح المناطق لتوليد صناديق تحديد محتملة في الصورة أولاً ثم تشغيل مصنف على هذه الصناديق المقترحة. بعد التصنيف، تُستخدم المعالجة اللاحقة لتحسين صناديق التحديد، والقضاء على الكشوفات المكررة، وإعادة تسجيل الصناديق بناءً على الأجسام الأخرى في المشهد [[13]]. هذه الخطوط الأنبوبية المعقدة بطيئة ويصعب تحسينها لأن كل مكون فردي يجب تدريبه بشكل منفصل.

نعيد صياغة كشف الأجسام كمسألة انحدار واحدة، مباشرة من بكسلات الصورة إلى إحداثيات صندوق التحديد واحتماليات الفئة. باستخدام نظامنا، تنظر مرة واحدة فقط (YOLO) إلى صورة للتنبؤ بالأجسام الموجودة ومكانها.

YOLO بسيط بشكل منعش: انظر الشكل [1]. تتنبأ شبكة التفافية واحدة في وقت واحد بصناديق تحديد متعددة واحتماليات الفئة لتلك الصناديق. يتدرب YOLO على الصور الكاملة ويحسن أداء الكشف مباشرة. لهذا النموذج الموحد عدة فوائد مقارنة بالطرق التقليدية لكشف الأجسام.

أولاً، YOLO سريع للغاية. نظراً لأننا نصوغ الكشف كمسألة انحدار، فإننا لا نحتاج إلى خط أنابيب معقد. نقوم ببساطة بتشغيل شبكتنا العصبية على صورة جديدة في وقت الاختبار للتنبؤ بالكشوفات. تعمل شبكتنا الأساسية بمعدل 45 إطاراً في الثانية دون معالجة دفعية على معالج رسومات Titan X، وتعمل النسخة السريعة بأكثر من 150 إطاراً في الثانية. هذا يعني أنه يمكننا معالجة الفيديو المباشر في الوقت الفعلي بزمن انتقال أقل من 25 ميلي ثانية. علاوة على ذلك، يحقق YOLO أكثر من ضعف متوسط الدقة المتوسط لأنظمة الوقت الفعلي الأخرى. للحصول على عرض توضيحي لنظامنا يعمل في الوقت الفعلي على كاميرا ويب، يرجى زيارة صفحة مشروعنا: http://pjreddie.com/yolo/.

ثانياً، يستدل YOLO بشكل شامل حول الصورة عند إجراء التنبؤات. على عكس تقنيات النافذة المنزلقة والتقنيات القائمة على اقتراح المناطق، يرى YOLO الصورة بأكملها أثناء التدريب ووقت الاختبار، لذلك يقوم ضمنياً بترميز المعلومات السياقية حول الفئات وكذلك مظهرها. يخطئ Fast R-CNN، وهو طريقة كشف رائدة [[14]]، في تحديد بقع الخلفية في الصورة كأجسام لأنه لا يمكنه رؤية السياق الأوسع. يرتكب YOLO أقل من نصف عدد أخطاء الخلفية مقارنة بـ Fast R-CNN.

ثالثاً، يتعلم YOLO تمثيلات قابلة للتعميم للأجسام. عندما يتم تدريبه على الصور الطبيعية واختباره على الأعمال الفنية، يتفوق YOLO على طرق الكشف الرائدة مثل DPM وR-CNN بهامش واسع. نظراً لأن YOLO قابل للتعميم بدرجة عالية، فمن غير المرجح أن ينهار عند تطبيقه على مجالات جديدة أو مدخلات غير متوقعة.

لا يزال YOLO متأخراً عن أنظمة الكشف المتقدمة من حيث الدقة. بينما يمكنه تحديد الأجسام في الصور بسرعة، فإنه يواجه صعوبة في تحديد موقع بعض الأجسام بدقة، وخاصة الصغيرة منها. نفحص هذه المقايضات بشكل أكبر في تجاربنا.

جميع شفرات التدريب والاختبار الخاصة بنا مفتوحة المصدر. كما تتوفر مجموعة متنوعة من النماذج المدربة مسبقاً للتنزيل.

---

### Translation Notes

- **Figures referenced:** Figure 1 (YOLO Detection System)
- **Key terms introduced:** YOLO, sliding window, region proposal, DPM, R-CNN, Fast R-CNN, post-processing, unified model
- **Performance metrics:** 45 fps (base), 150+ fps (fast version), <25ms latency, 2x mAP of real-time systems
- **Citations:** [10] for DPM, [13] for R-CNN, [14] for Fast R-CNN
- **Special handling:** Preserved project URL, kept technical acronyms (DPM, R-CNN, GPU model names)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
