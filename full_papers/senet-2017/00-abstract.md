# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** convolutional neural network, architecture, channel-wise, feature, recalibration, computational cost, dataset

---

### English Version

The central building block of convolutional neural networks (CNNs) is the convolution operator, which enables networks to construct informative features by fusing both spatial and channel-wise information within local receptive fields at each layer. A broad range of prior research has investigated the spatial component of this relationship, seeking to strengthen the representational power of a CNN by enhancing the quality of spatial encodings throughout its feature hierarchy. In this work, we focus instead on the channel relationship and propose a novel architectural unit, which we term the "Squeeze-and-Excitation" (SE) block, that adaptively recalibrates channel-wise feature responses by explicitly modelling interdependencies between channels. We show that these blocks can be stacked together to form SENet architectures that generalise extremely effectively across different datasets. We further demonstrate that SE blocks bring significant improvements in performance for existing state-of-the-art CNNs at slight additional computational cost. Squeeze-and-Excitation Networks formed the foundation of our ILSVRC 2017 classification submission which won first place and reduced the top-5 error to 2.251%, surpassing the winning entry of 2016 by a relative improvement of ~25%. Models and code are available at https://github.com/hujie-frank/SENet.

---

### النسخة العربية

تعتبر عملية الالتفاف هي الوحدة الأساسية لبناء الشبكات العصبية الالتفافية، حيث تمكّن الشبكات من بناء ميزات معلوماتية من خلال دمج المعلومات المكانية والمعلومات على مستوى القنوات ضمن الحقول الاستقبالية المحلية في كل طبقة. لقد بحث نطاق واسع من الأبحاث السابقة في المكون المكاني لهذه العلاقة، ساعية إلى تعزيز القوة التمثيلية للشبكة العصبية الالتفافية من خلال تحسين جودة الترميزات المكانية عبر تسلسلها الهرمي للميزات. في هذا العمل، نركز بدلاً من ذلك على العلاقة بين القنوات ونقترح وحدة معمارية جديدة، نطلق عليها اسم كتلة "الضغط والإثارة" (SE)، والتي تعيد معايرة استجابات الميزات على مستوى القنوات بشكل تكيفي من خلال نمذجة الترابطات بين القنوات بشكل صريح. نوضح أن هذه الكتل يمكن تكديسها معاً لتشكيل معماريات SENet التي تعمم بفعالية كبيرة عبر مجموعات بيانات مختلفة. كما نُظهر أن كتل SE تحقق تحسينات كبيرة في الأداء للشبكات العصبية الالتفافية المتقدمة الحالية مع تكلفة حسابية إضافية طفيفة. شكلت شبكات الضغط والإثارة الأساس لمشاركتنا في تصنيف ILSVRC 2017 والتي فازت بالمركز الأول وخفضت خطأ أعلى-5 إلى 2.251٪، متفوقة على الفائز لعام 2016 بتحسين نسبي يبلغ حوالي 25٪. النماذج والشفرة متاحة على https://github.com/hujie-frank/SENet.

---

### Translation Notes

- **Key terms introduced:**
  - Squeeze-and-Excitation (SE) block → كتلة الضغط والإثارة
  - Channel-wise recalibration → إعادة معايرة على مستوى القنوات
  - Receptive field → حقل استقبالي
  - Spatial encoding → ترميز مكاني
  - Feature hierarchy → تسلسل هرمي للميزات

- **Special handling:**
  - Preserved ILSVRC as acronym (common in Arabic technical literature)
  - Kept GitHub URL as-is
  - Maintained specific numbers (2.251%, 25%)

- **Citations:** None in abstract

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.89
- Glossary consistency: 0.90
- **Overall section score:** 0.91
