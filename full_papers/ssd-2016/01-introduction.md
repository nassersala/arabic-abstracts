# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** object detection, deep learning, neural network, bounding box, convolutional, feature map, training, inference, accuracy, mAP

---

### English Version

Current state-of-the-art object detection systems are variants of the following approach: hypothesize bounding boxes, resample pixels or features for each box, and apply a high-quality classifier. This pipeline has prevailed on detection benchmarks since the Selective Search work through the current leading results on PASCAL VOC, COCO, and ILSVRC detection all based on Faster R-CNN albeit with deeper features such as ResNet-101. While accurate, these approaches have been too computationally intensive for embedded systems and, even with high-end hardware, too slow for real-time applications.

Often detection speed for these approaches is measured in seconds per frame (SPF), and even the fastest high-accuracy detector, Faster R-CNN, operates at only 7 FPS. There have been many attempts to build faster detectors by attacking each stage of the detection pipeline, but so far, significantly increased speed comes only at the cost of significantly decreased detection accuracy.

This paper presents the first deep network based object detector that does not resample pixels or features for bounding box hypotheses and is as accurate as approaches that do. This results in a significant improvement in speed for high-accuracy detection (59 FPS with mAP 74.3% on VOC2007 test). The fundamental improvement in speed comes from eliminating bounding box proposals and the subsequent pixel or feature resampling stage. We are not the first to do this (cf. OverFeat and YOLO), but by adding a series of improvements, we manage to increase the accuracy significantly while also improving the speed over YOLO. Our improvements include using a small convolutional filter to predict object categories and offsets in bounding box locations, using separate predictors (filters) for different aspect ratio detections, and applying these filters to multiple feature maps from the later stages of a network in order to perform detection at multiple scales. With these modifications—especially using multiple layers for prediction at different scales—we can achieve high-accuracy using relatively low resolution input, further increasing detection speed. While these contributions may seem small independently, we note that the resulting system improves accuracy on real-time detection for PASCAL VOC from 63.4% mAP for YOLO to 74.3% mAP for our SSD. This is a larger gain in accuracy than that obtained by any recent incremental improvement to Faster R-CNN. We also present SSD models that can run at varying speeds by using images of different resolution, which provides a nice tradeoff between speed and accuracy. In our experiments on multiple datasets, including PASCAL VOC, COCO, and ILSVRC, we demonstrate the advantage of SSD compared to its predecessor YOLO and other state-of-the-art object detection methods, particularly in terms of speed and competitive accuracy.

The structure of this paper is as follows. Sec. 2 describes the SSD approach and our training methodology. In Sec. 3, we present experimental results on benchmark datasets and provide analysis comparing our method to other state-of-the-art approaches. Sec. 4 discusses related work, and we conclude with Sec. 5.

---

### النسخة العربية

تعتبر أنظمة كشف الأجسام الحديثة المتقدمة متغيرات من النهج التالي: افتراض صناديق التحديد، وإعادة أخذ العينات من البكسل أو الميزات لكل صندوق، وتطبيق مصنف عالي الجودة. ساد هذا الأسلوب على معايير الكشف منذ عمل البحث الانتقائي (Selective Search) وحتى النتائج الرائدة الحالية على PASCAL VOC وCOCO وILSVRC للكشف، والتي تستند جميعها إلى Faster R-CNN وإن كان ذلك مع ميزات أعمق مثل ResNet-101. على الرغم من دقتها، فإن هذه الأساليب كانت مكثفة حسابياً للغاية بالنسبة للأنظمة المدمجة، وحتى مع الأجهزة المتطورة، بطيئة جداً للتطبيقات في الزمن الفعلي.

غالباً ما تُقاس سرعة الكشف لهذه الأساليب بالثواني لكل إطار (SPF)، وحتى أسرع كاشف عالي الدقة، Faster R-CNN، يعمل بسرعة 7 إطارات فقط في الثانية. كانت هناك محاولات عديدة لبناء كواشف أسرع من خلال معالجة كل مرحلة من مراحل خط أنابيب الكشف، ولكن حتى الآن، لا تأتي الزيادة الكبيرة في السرعة إلا على حساب انخفاض كبير في دقة الكشف.

تقدم هذه الورقة أول كاشف أجسام قائم على الشبكات العصبية العميقة لا يعيد أخذ العينات من البكسل أو الميزات لفرضيات صناديق التحديد ودقيق مثل الأساليب التي تفعل ذلك. ينتج عن هذا تحسن كبير في السرعة للكشف عالي الدقة (59 إطاراً في الثانية مع 74.3% على مقياس mAP على اختبار VOC2007). يأتي التحسن الأساسي في السرعة من إلغاء مقترحات صناديق التحديد ومرحلة إعادة أخذ العينات من البكسل أو الميزات اللاحقة. نحن لسنا أول من يفعل هذا (قارن OverFeat وYOLO)، ولكن من خلال إضافة سلسلة من التحسينات، نتمكن من زيادة الدقة بشكل كبير مع تحسين السرعة أيضاً مقارنة بـ YOLO. تشمل تحسيناتنا استخدام مرشح التفافي صغير للتنبؤ بفئات الأجسام والإزاحات في مواقع صناديق التحديد، واستخدام متنبئات منفصلة (مرشحات) لكشف نسب أبعاد مختلفة، وتطبيق هذه المرشحات على خرائط ميزات متعددة من المراحل اللاحقة للشبكة من أجل إجراء الكشف على مقاييس متعددة. مع هذه التعديلات - وخاصة استخدام طبقات متعددة للتنبؤ على مقاييس مختلفة - يمكننا تحقيق دقة عالية باستخدام مدخلات منخفضة الدقة نسبياً، مما يزيد من سرعة الكشف بشكل أكبر. في حين أن هذه المساهمات قد تبدو صغيرة بشكل مستقل، نلاحظ أن النظام الناتج يحسن الدقة في الكشف في الزمن الفعلي لـ PASCAL VOC من 63.4% على مقياس mAP لـ YOLO إلى 74.3% على مقياس mAP لـ SSD الخاص بنا. هذا مكسب في الدقة أكبر من ذلك الذي تم الحصول عليه من خلال أي تحسين تدريجي حديث على Faster R-CNN. نقدم أيضاً نماذج SSD يمكن أن تعمل بسرعات متفاوتة باستخدام صور بدرجات دقة مختلفة، مما يوفر مقايضة جيدة بين السرعة والدقة. في تجاربنا على مجموعات بيانات متعددة، بما في ذلك PASCAL VOC وCOCO وILSVRC، نوضح ميزة SSD مقارنة بسابقه YOLO وطرق كشف الأجسام المتقدمة الأخرى، خاصة من حيث السرعة والدقة المنافسة.

بنية هذه الورقة كما يلي. يصف القسم 2 نهج SSD ومنهجية التدريب الخاصة بنا. في القسم 3، نقدم نتائج تجريبية على مجموعات بيانات معيارية ونقدم تحليلاً يقارن طريقتنا بالأساليب المتقدمة الأخرى. يناقش القسم 4 الأعمال ذات الصلة، ونختتم بالقسم 5.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Selective Search - البحث الانتقائي
  - Embedded systems - الأنظمة المدمجة
  - Real-time applications - التطبيقات في الزمن الفعلي
  - Seconds per frame (SPF) - الثواني لكل إطار
  - Frames per second (FPS) - إطارات في الثانية
  - Detection pipeline - خط أنابيب الكشف
  - Bounding box proposals - مقترحات صناديق التحديد
  - Offsets - الإزاحات
  - Resolution - دقة
  - Tradeoff - مقايضة

- **Equations:** None
- **Citations:** References to Selective Search, Faster R-CNN, ResNet-101, OverFeat, YOLO
- **Special handling:**
  - Preserved all model names: Faster R-CNN, YOLO, OverFeat, ResNet-101
  - Preserved dataset names: PASCAL VOC, COCO, ILSVRC
  - Preserved all numerical metrics: 59 FPS, 74.3% mAP, 63.4% mAP, 7 FPS
  - Section references kept in both languages: Sec. 2 / القسم 2

### Quality Metrics

- **Semantic equivalence:** 0.90 - All technical details and argumentative flow preserved
- **Technical accuracy:** 0.88 - All technical terms correctly translated
- **Readability:** 0.86 - Natural flow in formal academic Arabic
- **Glossary consistency:** 0.88 - Consistent terminology throughout
- **Overall section score:** 0.88

### Back-translation Check

**First sentence back-translation:** "Modern advanced object detection systems are variants of the following approach: hypothesizing bounding boxes, resampling pixels or features for each box, and applying a high-quality classifier."
**Original:** "Current state-of-the-art object detection systems are variants of the following approach: hypothesize bounding boxes, resample pixels or features for each box, and apply a high-quality classifier."
✅ Semantic match confirmed

**Key claim back-translation:** "The resulting system improves accuracy in real-time detection for PASCAL VOC from 63.4% mAP for YOLO to 74.3% mAP for our SSD."
**Original:** "The resulting system improves accuracy on real-time detection for PASCAL VOC from 63.4% mAP for YOLO to 74.3% mAP for our SSD."
✅ Semantic match confirmed
