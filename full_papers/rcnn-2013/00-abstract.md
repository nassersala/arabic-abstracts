# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** object detection, convolutional neural networks, region proposals, supervised pre-training, fine-tuning, mean average precision, semantic segmentation

---

### English Version

Object detection performance, as measured on the canonical PASCAL VOC dataset, has plateaued in the last few years. The best-performing methods are complex ensemble systems that typically combine multiple low-level image features with high-level context. In this paper, we propose a simple and scalable detection algorithm that improves mean average precision (mAP) by more than 30% relative to the previous best result on VOC 2012—achieving a mAP of 53.3%. Our approach combines two key insights: (1) one can apply high-capacity convolutional neural networks (CNNs) to bottom-up region proposals in order to localize and segment objects and (2) when labeled training data is scarce, supervised pre-training for an auxiliary task, followed by domain-specific fine-tuning, yields a significant performance boost. Since we combine region proposals with CNNs, we call our method R-CNN: Regions with CNN features. We also compare R-CNN to OverFeat, a recently proposed sliding-window detector based on a similar CNN architecture. We find that R-CNN outperforms OverFeat by a large margin on the 200-class ILSVRC2013 detection dataset. Source code for the complete system is available at http://www.cs.berkeley.edu/~rbg/rcnn.

---

### النسخة العربية

لقد توقف تحسن أداء كشف الأجسام، كما يُقاس على مجموعة بيانات PASCAL VOC المعيارية، في السنوات القليلة الماضية. تعتمد الطرق الأفضل أداءً على أنظمة تجميعية معقدة تجمع عادةً بين ميزات صور متعددة منخفضة المستوى مع سياق عالي المستوى. في هذا البحث، نقترح خوارزمية كشف بسيطة وقابلة للتوسع تحسّن متوسط الدقة المتوسط (mAP) بأكثر من 30% مقارنةً بأفضل نتيجة سابقة على VOC 2012 - محققةً mAP بنسبة 53.3%. يجمع نهجنا بين رؤيتين أساسيتين: (1) يمكن تطبيق الشبكات العصبية الالتفافية (CNNs) عالية السعة على مقترحات المناطق من الأسفل إلى الأعلى من أجل تحديد موقع الأجسام وتقسيمها، و(2) عندما تكون بيانات التدريب الموسومة نادرة، فإن التدريب المسبق الموجّه لمهمة مساعدة، يليه الضبط الدقيق الخاص بالمجال، يُحقق تحسيناً كبيراً في الأداء. نظراً لأننا نجمع بين مقترحات المناطق والشبكات العصبية الالتفافية، نطلق على طريقتنا اسم R-CNN: المناطق بميزات الشبكات العصبية الالتفافية. كما نقارن R-CNN مع OverFeat، وهو كاشف بنافذة منزلقة مُقترح حديثاً يعتمد على معمارية شبكات عصبية التفافية مماثلة. نجد أن R-CNN يتفوق على OverFeat بفارق كبير على مجموعة بيانات كشف ILSVRC2013 المكونة من 200 صنف. الشفرة المصدرية للنظام الكامل متاحة على http://www.cs.berkeley.edu/~rbg/rcnn.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** R-CNN (Regions with CNN features), region proposals, supervised pre-training, domain-specific fine-tuning
- **Equations:** None
- **Citations:** None
- **Special handling:**
  - Preserved technical acronyms: PASCAL VOC, mAP, CNN, ILSVRC2013
  - Translated R-CNN as "المناطق بميزات الشبكات العصبية الالتفافية" with acronym preserved
  - Maintained URL in English

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90
