# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional neural network, architecture, mobile devices, pointwise convolution, group convolution, channel shuffle, feature map, computational complexity, MFLOPs, ImageNet, object detection

---

### English Version

We introduce an extremely computation-efficient CNN architecture named ShuffleNet, which is designed specially for mobile devices with very limited computing power (e.g., 10-150 MFLOPs). The new architecture utilizes two new operations, pointwise group convolution and channel shuffle, to greatly reduce computation cost while maintaining accuracy. Experiments on ImageNet classification and MS COCO object detection demonstrate the superior performance of ShuffleNet over other structures, e.g. lower top-1 error (absolute 7.8%) than recent MobileNet on ImageNet classification task under the computation budget of 40 MFLOPs. On an ARM-based mobile device, ShuffleNet achieves ~13× actual speedup over AlexNet while maintaining comparable accuracy.

---

### النسخة العربية

نقدم معمارية شبكة عصبية التفافية فائقة الكفاءة الحسابية تُدعى ShuffleNet (شَفل نت)، والتي صُممت خصيصاً للأجهزة المحمولة ذات القدرة الحسابية المحدودة جداً (على سبيل المثال، 10-150 ميجا عملية فاصلة عائمة). تستخدم المعمارية الجديدة عمليتين جديدتين هما الالتفاف النقطي المجموعي وخلط القنوات، لتقليل التكلفة الحسابية بشكل كبير مع الحفاظ على الدقة. تُظهر التجارب على تصنيف ImageNet وكشف الأجسام MS COCO الأداء المتفوق لـ ShuffleNet مقارنة بالمعماريات الأخرى، على سبيل المثال خطأ top-1 أقل (بفارق مطلق 7.8%) من شبكة MobileNet الحديثة في مهمة تصنيف ImageNet تحت ميزانية حسابية قدرها 40 ميجا عملية فاصلة عائمة. على جهاز محمول يعتمد على معمارية ARM، تحقق ShuffleNet تسريعاً فعلياً بمقدار ~13 ضعفاً مقارنة بشبكة AlexNet مع الحفاظ على دقة مماثلة.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - ShuffleNet (شَفل نت) - kept as transliteration
  - Pointwise group convolution (الالتفاف النقطي المجموعي)
  - Channel shuffle (خلط القنوات)
  - MFLOPs (ميجا عملية فاصلة عائمة)
  - Computational budget (ميزانية حسابية)

- **Equations:** 0
- **Citations:** ImageNet, MS COCO, MobileNet, AlexNet
- **Special handling:**
  - Kept technical dataset/model names in English (ImageNet, MS COCO, MobileNet, AlexNet, ARM)
  - Translated numerical values directly (10-150, 40, ~13×, 7.8%)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-translation Check (Key Sentence)

Arabic: "تستخدم المعمارية الجديدة عمليتين جديدتين هما الالتفاف النقطي المجموعي وخلط القنوات"
Back to English: "The new architecture uses two new operations: pointwise group convolution and channel shuffle"
✓ Semantically equivalent to original
