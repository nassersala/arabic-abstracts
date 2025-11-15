# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** deep neural networks (الشبكات العصبية العميقة), accuracy (دقة), architecture (معمارية), distributed training (تدريب موزع), bandwidth (نطاق ترددي), autonomous (ذاتي), FPGA (مصفوفات البوابات القابلة للبرمجة), model compression (ضغط النموذج), parameters (معاملات)

---

### English Version

Recent research on deep neural networks has focused primarily on improving accuracy. For a given accuracy level, it is typically possible to identify multiple DNN architectures that achieve that accuracy level. With equivalent accuracy, smaller DNN architectures offer at least three advantages: (1) Smaller DNNs require less communication across servers during distributed training. (2) Smaller DNNs require less bandwidth to export a new model from the cloud to an autonomous car. (3) Smaller DNNs are more feasible to deploy on FPGAs and other hardware with limited memory. To provide all of these advantages, we propose a small DNN architecture called SqueezeNet. SqueezeNet achieves AlexNet-level accuracy on ImageNet with 50x fewer parameters. Additionally, with model compression techniques we are able to compress SqueezeNet to less than 0.5MB (510x smaller than AlexNet).

---

### النسخة العربية

ركزت الأبحاث الحديثة في مجال الشبكات العصبية العميقة بشكل أساسي على تحسين الدقة. ولمستوى دقة معين، يكون من الممكن عادةً تحديد معماريات متعددة للشبكات العصبية العميقة تحقق ذلك المستوى من الدقة. ومع تساوي الدقة، تقدم معماريات الشبكات العصبية العميقة الأصغر حجماً ثلاث مزايا على الأقل: (1) تتطلب الشبكات العصبية العميقة الأصغر حجماً اتصالاً أقل عبر الخوادم أثناء التدريب الموزع. (2) تتطلب الشبكات العصبية العميقة الأصغر حجماً نطاقاً ترددياً أقل لتصدير نموذج جديد من السحابة إلى سيارة ذاتية القيادة. (3) تكون الشبكات العصبية العميقة الأصغر حجماً أكثر قابلية للنشر على مصفوفات البوابات القابلة للبرمجة والأجهزة الأخرى ذات الذاكرة المحدودة. ولتوفير جميع هذه المزايا، نقترح معمارية شبكة عصبية عميقة صغيرة تسمى SqueezeNet. تحقق SqueezeNet دقة بمستوى AlexNet على مجموعة بيانات ImageNet باستخدام معاملات أقل بـ 50 مرة. بالإضافة إلى ذلك، ومع تقنيات ضغط النموذج، نستطيع ضغط SqueezeNet إلى أقل من 0.5 ميجابايت (أصغر بـ 510 مرات من AlexNet).

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** SqueezeNet, AlexNet, ImageNet, DNN (Deep Neural Network), model compression
- **Equations:** 0
- **Citations:** 0
- **Special handling:**
  - Kept "SqueezeNet", "AlexNet", and "ImageNet" as proper nouns in Arabic
  - Translated "autonomous car" as "سيارة ذاتية القيادة" (self-driving car)
  - Used established glossary terms for technical concepts

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.92

### Back-Translation Check

The Arabic translation accurately conveys:
- The focus on model compression and efficiency
- Three specific advantages of smaller models
- Quantitative achievements (50x fewer parameters, 510x smaller size)
- The comparison to AlexNet as a baseline
