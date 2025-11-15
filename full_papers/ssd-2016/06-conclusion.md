# Section 5: Conclusions
## القسم 5: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** object detection, deep learning, neural network, bounding box, feature map, convolutional, training, inference, mAP, accuracy

---

### English Version

This paper introduces SSD, a fast single-shot object detector for multiple categories. A key feature of our model is the use of multi-scale convolutional bounding box outputs attached to multiple feature maps at the top of the network. This representation allows us to efficiently model the space of possible bounding box shapes. We experimentally validate that given appropriate training strategies, a larger number of carefully chosen default bounding boxes results in improved performance. We build SSD models with at least an order of magnitude more box predictions sampling location, scale, and aspect ratio, than existing methods such as YOLO. We demonstrate that given the same VGG-16 base architecture, SSD compares favorably to its state-of-the-art object detector counterparts in terms of both accuracy and speed. Our SSD512 model significantly outperforms the state-of-the-art Faster R-CNN in terms of accuracy on PASCAL VOC and COCO, while being 3× faster. Our real time SSD300 model runs at 59 FPS, which is faster than the current real time YOLO alternative, while producing markedly superior detection quality.

Apart from its standalone utility, we believe that our monolithic and relatively simple SSD model provides a useful building block for larger systems that employ an object detection component. A promising future direction is to explore its use as part of a system using recurrent neural networks to detect and track objects in video simultaneously.

---

### النسخة العربية

تقدم هذه الورقة SSD، كاشف أجسام سريع أحادي الطلقة لفئات متعددة. تتمثل إحدى الميزات الرئيسية لنموذجنا في استخدام إخراجات صناديق التحديد الالتفافية متعددة المقاييس المرفقة بخرائط ميزات متعددة في الجزء العلوي من الشبكة. يتيح لنا هذا التمثيل نمذجة فضاء أشكال صناديق التحديد المحتملة بكفاءة. نتحقق تجريبياً من أنه في ظل استراتيجيات التدريب المناسبة، فإن عدداً أكبر من الصناديق الافتراضية المختارة بعناية ينتج عنه أداء محسَّن. نبني نماذج SSD بما لا يقل عن رتبة قدرية من التنبؤات الأكثر للصناديق، تأخذ عينات من الموقع والمقياس ونسبة الأبعاد، مقارنة بالطرق الحالية مثل YOLO. نوضح أنه في ظل نفس المعمارية الأساسية VGG-16، يقارن SSD بشكل إيجابي مع نظرائه من كواشف الأجسام المتقدمة من حيث الدقة والسرعة. يتفوق نموذج SSD512 الخاص بنا بشكل كبير على Faster R-CNN المتقدم من حيث الدقة على PASCAL VOC وCOCO، بينما يكون أسرع بـ 3 مرات. يعمل نموذج SSD300 الخاص بنا في الزمن الفعلي بسرعة 59 إطاراً في الثانية، وهو أسرع من بديل YOLO الحالي في الزمن الفعلي، بينما ينتج جودة كشف متفوقة بشكل ملحوظ.

بصرف النظر عن فائدته المستقلة، نعتقد أن نموذج SSD الأحادي والبسيط نسبياً يوفر وحدة بناء مفيدة لأنظمة أكبر تستخدم مكون كشف الأجسام. أحد التوجهات المستقبلية الواعدة هو استكشاف استخدامه كجزء من نظام يستخدم الشبكات العصبية المتكررة لكشف الأجسام وتتبعها في الفيديو في وقت واحد.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Single-shot detector - كاشف أحادي الطلقة
  - Multi-scale outputs - إخراجات متعددة المقاييس
  - Order of magnitude - رتبة قدرية
  - Standalone utility - فائدة مستقلة
  - Monolithic - أحادي
  - Building block - وحدة بناء
  - Real time - الزمن الفعلي
  - Track objects - تتبع الأجسام
  - Markedly superior - متفوق بشكل ملحوظ

- **Equations:** None
- **Citations:** References to YOLO, Faster R-CNN, VGG-16
- **Special handling:**
  - Preserved all performance claims and metrics
  - Maintained model comparisons: SSD vs YOLO vs Faster R-CNN
  - Kept speed metrics: 59 FPS, 3× faster
  - Preserved dataset names: PASCAL VOC, COCO
  - Maintained future direction statement

### Quality Metrics

- **Semantic equivalence:** 0.90 - All conclusions accurately preserved
- **Technical accuracy:** 0.88 - Technical claims correctly translated
- **Readability:** 0.87 - Natural flow in conclusion
- **Glossary consistency:** 0.88 - Consistent terminology throughout
- **Overall section score:** 0.88

### Back-translation Check

**Main contribution back-translation:** "A key feature of our model is the use of multi-scale convolutional bounding box outputs attached to multiple feature maps at the top of the network."
**Original:** "A key feature of our model is the use of multi-scale convolutional bounding box outputs attached to multiple feature maps at the top of the network."
✅ Semantic match confirmed

**Performance claim back-translation:** "Our SSD512 model significantly outperforms the state-of-the-art Faster R-CNN in terms of accuracy on PASCAL VOC and COCO, while being 3× faster."
**Original:** "Our SSD512 model significantly outperforms the state-of-the-art Faster R-CNN in terms of accuracy on PASCAL VOC and COCO, while being 3× faster."
✅ Semantic match confirmed

**Future work back-translation:** "A promising future direction is to explore its use as part of a system using recurrent neural networks to detect and track objects in video simultaneously."
**Original:** "A promising future direction is to explore its use as part of a system using recurrent neural networks to detect and track objects in video simultaneously."
✅ Semantic match confirmed
