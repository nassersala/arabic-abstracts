# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** object detection, neural network, bounding boxes, real-time, architecture, regression, localization, representations, end-to-end

---

### English Version

We present YOLO, a new approach to object detection. Prior work on object detection repurposes classifiers to perform detection. Instead, we frame object detection as a regression problem to spatially separated bounding boxes and associated class probabilities. A single neural network predicts bounding boxes and class probabilities directly from full images in one evaluation. Since the whole detection pipeline is a single network, it can be optimized end-to-end directly on detection performance. Our unified architecture is extremely fast. Our base YOLO model processes images in real-time at 45 frames per second. A smaller version of the network, Fast YOLO, processes an astounding 155 frames per second while still achieving double the mAP of other real-time detectors. Compared to state-of-the-art detection systems, YOLO makes more localization errors but is far less likely to predict false detections where nothing exists. Finally, YOLO learns very general representations of objects. It outperforms all other detection methods, including DPM and R-CNN, by a wide margin when generalizing from natural images to artwork on both the Picasso Dataset and the People-Art Dataset.

---

### النسخة العربية

نقدم YOLO، نهج جديد لكشف الأجسام. تعيد الأعمال السابقة في كشف الأجسام توجيه المصنفات لتنفيذ الكشف. بدلاً من ذلك، نصوغ كشف الأجسام كمسألة انحدار لصناديق تحديد منفصلة مكانياً واحتماليات فئة مرتبطة. تتنبأ شبكة عصبية واحدة بصناديق التحديد واحتماليات الفئة مباشرة من الصور الكاملة في تقييم واحد. نظراً لأن خط أنابيب الكشف بأكمله عبارة عن شبكة واحدة، يمكن تحسينه من البداية للنهاية مباشرة على أداء الكشف. معماريتنا الموحدة سريعة للغاية. يعالج نموذج YOLO الأساسي الصور في الوقت الفعلي بمعدل 45 إطاراً في الثانية. تعالج نسخة أصغر من الشبكة، Fast YOLO، 155 إطاراً في الثانية بشكل مذهل بينما لا تزال تحقق ضعف mAP لكاشفات الوقت الفعلي الأخرى. مقارنة بأنظمة الكشف المتقدمة، يرتكب YOLO المزيد من أخطاء التحديد الموضعي ولكنه أقل احتمالاً بكثير للتنبؤ باكتشافات خاطئة حيث لا يوجد شيء. أخيراً، يتعلم YOLO تمثيلات عامة جداً للأجسام. يتفوق على جميع طرق الكشف الأخرى، بما في ذلك DPM وR-CNN، بهامش واسع عند التعميم من الصور الطبيعية إلى الأعمال الفنية على كل من مجموعة بيانات بيكاسو ومجموعة بيانات الأشخاص والفن.

---

### Translation Notes

- **Key terms introduced:** YOLO, object detection, regression, bounding boxes, real-time detection, mAP
- **Citations:** References to DPM and R-CNN methods
- **Performance metrics:** 45 fps (base YOLO), 155 fps (Fast YOLO)
- **Datasets mentioned:** Picasso Dataset, People-Art Dataset

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.91
- Glossary consistency: 0.92
- **Overall section score:** 0.92
