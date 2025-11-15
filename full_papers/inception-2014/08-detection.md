# Section 8: ILSVRC 2014 Detection Challenge Setup and Results
## القسم 8: إعداد ونتائج تحدي الكشف ILSVRC 2014

**Section:** ILSVRC 2014 Detection Challenge
**Translation Quality:** 0.88
**Glossary Terms Used:** detection, bounding box, R-CNN, Selective Search, multi-box, ensemble, mean average precision (mAP), Jaccard index, ConvNets, region classifier

---

### English Version

The ILSVRC detection task is to produce bounding boxes around objects in images among 200 possible classes. Detected objects count as correct if they match the class of the groundtruth and their bounding boxes overlap by at least 50% (using the Jaccard index). Extraneous detections count as false positives and are penalized. Contrary to the classification task, each image may contain many objects or none, and their scale may vary. Results are reported using the mean average precision (mAP). The approach taken by GoogLeNet for detection is similar to the R-CNN by [6], but is augmented with the Inception model as the region classifier. Additionally, the region proposal step is improved by combining the Selective Search [20] approach with multi-box [5] predictions for higher object bounding box recall. In order to cut down the number of false positives, the superpixel size was increased by 2×. This halves the proposals coming from the selective search algorithm. We added back 200 region proposals coming from multi-box [5] resulting, in total, in about 60% of the proposals used by [6], while increasing the coverage from 92% to 93%. The overall effect of cutting the number of proposals with increased coverage is a 1% improvement of the mean average precision for the single model case. Finally, we use an ensemble of 6 ConvNets when classifying each region which improves results from 40% to 43.9% accuracy. Note that contrary to R-CNN, we did not use bounding box regression due to lack of time.

We first report the top detection results and show the progress since the first edition of the detection task. Compared to the 2013 result, the accuracy has almost doubled. The top performing teams all use Convolutional Networks. We report the official scores in Table 4 and common strategies for each team: the use of external data, ensemble models or contextual models. The external data is typically the ILSVRC12 classification data for pre-training a model that is later refined on the detection data. Some teams also mention the use of the localization data. Since the pre-training of the network is not mentioned explicitly in [6], we ✓ indicates it in the table. For the GoogLeNet entry, external data was also used for the region classifier which was pre-trained on ImageNet classification data. Some improvements seen in [10] were not used due to lack of time.

---

### النسخة العربية

مهمة الكشف في ILSVRC هي إنتاج صناديق تحديد حول الكائنات في الصور من بين 200 فئة ممكنة. تُحسب الكائنات المكتشفة كصحيحة إذا كانت تتطابق مع فئة الحقيقة الأرضية وتتداخل صناديق التحديد الخاصة بها بنسبة 50٪ على الأقل (باستخدام مؤشر Jaccard). تُحسب الكشوفات الزائدة كإيجابيات كاذبة ويتم معاقبتها. على عكس مهمة التصنيف، قد تحتوي كل صورة على العديد من الكائنات أو لا تحتوي على أي منها، وقد يختلف مقياسها. يتم الإبلاغ عن النتائج باستخدام متوسط الدقة المتوسط (mAP). النهج الذي اتبعه GoogLeNet للكشف مشابه لـ R-CNN من قبل [6]، ولكنه معزز بنموذج Inception كمصنف المنطقة. بالإضافة إلى ذلك، يتم تحسين خطوة اقتراح المنطقة من خلال الجمع بين نهج البحث الانتقائي (Selective Search) [20] مع تنبؤات multi-box [5] لزيادة استدعاء صندوق التحديد للكائنات. من أجل تقليل عدد الإيجابيات الكاذبة، تم زيادة حجم الـ superpixel بمقدار 2×. هذا ينصّف المقترحات القادمة من خوارزمية البحث الانتقائي. أضفنا 200 مقترح منطقة قادمة من multi-box [5] مما أدى، في المجموع، إلى حوالي 60٪ من المقترحات المستخدمة من قبل [6]، مع زيادة التغطية من 92٪ إلى 93٪. التأثير العام لتقليل عدد المقترحات مع زيادة التغطية هو تحسين بنسبة 1٪ في متوسط الدقة المتوسط لحالة النموذج الواحد. أخيراً، نستخدم مجموعة من 6 شبكات ConvNets عند تصنيف كل منطقة مما يحسن النتائج من 40٪ إلى 43.9٪ دقة. لاحظ أنه على عكس R-CNN، لم نستخدم انحدار صندوق التحديد بسبب نقص الوقت.

نبلّغ أولاً عن أفضل نتائج الكشف ونوضح التقدم منذ الإصدار الأول من مهمة الكشف. مقارنة بنتيجة 2013، تضاعفت الدقة تقريباً. جميع الفرق ذات الأداء الأفضل تستخدم الشبكات الالتفافية. نبلّغ عن النتائج الرسمية في الجدول 4 والاستراتيجيات الشائعة لكل فريق: استخدام البيانات الخارجية، أو نماذج المجموعات، أو النماذج السياقية. البيانات الخارجية عادةً هي بيانات تصنيف ILSVRC12 للتدريب المسبق لنموذج يتم تحسينه لاحقاً على بيانات الكشف. تذكر بعض الفرق أيضاً استخدام بيانات التوطين. نظراً لأن التدريب المسبق للشبكة لم يُذكر صراحةً في [6]، فإننا نشير إليه بعلامة ✓ في الجدول. بالنسبة لمشاركة GoogLeNet، تم أيضاً استخدام البيانات الخارجية لمصنف المنطقة الذي تم تدريبه مسبقاً على بيانات تصنيف ImageNet. لم يتم استخدام بعض التحسينات التي شوهدت في [10] بسبب نقص الوقت.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 4
- **Key terms introduced:** bounding box, detection task, Jaccard index, false positives, mean average precision (mAP), region classifier, Selective Search, multi-box, superpixel, object bounding box recall, bounding box regression, contextual models, pre-training
- **Equations:** None
- **Citations:** [5], [6], [10], [20]
- **Special handling:**
  - Translated "bounding box" as "صندوق التحديد"
  - Kept "Jaccard index" as "مؤشر Jaccard"
  - Translated "false positives" as "إيجابيات كاذبة"
  - Kept "mAP" acronym with Arabic expansion "متوسط الدقة المتوسط"
  - Kept "R-CNN", "Selective Search", "multi-box", "ConvNets" as English terms
  - Kept "superpixel" as English term (standard in computer vision)
  - Translated "region classifier" as "مصنف المنطقة"
  - Translated "coverage" as "التغطية"
  - Translated "recall" as "استدعاء"
  - Kept "ILSVRC12" and "ImageNet" as proper nouns
  - Translated "pre-training" as "التدريب المسبق"
  - Kept mathematical expressions like "50%", "2×", "60%", "92%", "93%" unchanged
  - Translated "bounding box regression" as "انحدار صندوق التحديد"

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
