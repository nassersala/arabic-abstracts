# Section 6: Limitations and Discussion
## القسم 6: القيود والمناقشة

**Section:** limitations-and-discussion
**Translation Quality:** 0.88
**Glossary Terms Used:** failure cases, geometric changes, distribution characteristics, weak supervision, semi-supervised, unpaired data, unsupervised setting

---

### English Version

Although our method can achieve compelling results in many cases, the results are far from uniformly positive. Figure 17 shows several typical failure cases. On translation tasks that involve color and texture changes, as many of those reported above, the method often succeeds. We have also explored tasks that require geometric changes, with little success. For example, on the task of dog → cat transfiguration, the learned translation degenerates into making minimal changes to the input (Figure 17). This failure might be caused by our generator architectures which are tailored for good performance on the appearance changes. Handling more varied and extreme transformations, especially geometric changes, is an important problem for future work.

Some failure cases are caused by the distribution characteristics of the training datasets. For example, our method has got confused in the horse → zebra example (Figure 17, right), because our model was trained on the wild horse and zebra synsets of ImageNet, which does not contain images of a person riding a horse or zebra.

We also observe a lingering gap between the results achievable with paired training data and those achieved by our unpaired method. In some cases, this gap may be very hard – or even impossible – to close: for example, our method sometimes permutes the labels for tree and building in the output of the photos → labels task. Resolving this ambiguity may require some form of weak semantic supervision. Integrating weak or semi-supervised data may lead to substantially more powerful translators, still at a fraction of the annotation cost of the fully-supervised systems.

Nonetheless, in many cases completely unpaired data is plentifully available and should be made use of. This paper pushes the boundaries of what is possible in this "unsupervised" setting.

---

### النسخة العربية

على الرغم من أن طريقتنا يمكنها تحقيق نتائج مقنعة في العديد من الحالات، إلا أن النتائج بعيدة كل البعد عن أن تكون إيجابية بشكل موحد. يُظهر الشكل 17 عدة حالات فشل نموذجية. في مهام الترجمة التي تتضمن تغييرات في اللون والنسيج، مثل العديد من تلك المبلغ عنها أعلاه، تنجح الطريقة غالباً. استكشفنا أيضاً مهام تتطلب تغييرات هندسية، مع نجاح ضئيل. على سبيل المثال، في مهمة تحويل كلب → قطة، تتدهور الترجمة المُتعلمة إلى إجراء تغييرات ضئيلة على المدخل (الشكل 17). قد يكون هذا الفشل ناتجاً عن معماريات مولدنا المُصممة للأداء الجيد على تغييرات المظهر. تُعد معالجة التحويلات الأكثر تنوعاً وتطرفاً، وخاصة التغييرات الهندسية، مشكلة مهمة للعمل المستقبلي.

بعض حالات الفشل ناتجة عن خصائص توزيع مجموعات بيانات التدريب. على سبيل المثال، ارتبكت طريقتنا في مثال حصان → حمار وحشي (الشكل 17، اليمين)، لأن نموذجنا تم تدريبه على مجموعات الحصان البري والحمار الوحشي في ImageNet، والتي لا تحتوي على صور لشخص يركب حصاناً أو حمار وحشي.

نلاحظ أيضاً فجوة باقية بين النتائج القابلة للتحقيق مع بيانات التدريب المقترنة وتلك التي تحققها طريقتنا غير المقترنة. في بعض الحالات، قد يكون من الصعب جداً - أو حتى المستحيل - سد هذه الفجوة: على سبيل المثال، تقوم طريقتنا أحياناً بتبديل التسميات للشجرة والمبنى في مخرجات مهمة الصور → التسميات. قد يتطلب حل هذا الغموض شكلاً من أشكال الإشراف الدلالي الضعيف. قد يؤدي دمج البيانات ذات الإشراف الضعيف أو شبه الخاضع للإشراف إلى مترجمات أكثر قوة بشكل كبير، ولا تزال بجزء بسيط من تكلفة التعليق التوضيحي للأنظمة الخاضعة للإشراف الكامل.

ومع ذلك، في العديد من الحالات، تتوفر البيانات غير المقترنة بالكامل بكثرة ويجب الاستفادة منها. يدفع هذا البحث حدود ما هو ممكن في هذا الإعداد "غير الخاضع للإشراف".

---

### Translation Notes

- **Figures referenced:** Figure 17
- **Key terms introduced:**
  - failure cases (حالات الفشل)
  - geometric changes (التغييرات الهندسية)
  - appearance changes (تغييرات المظهر)
  - distribution characteristics (خصائص التوزيع)
  - weak semantic supervision (الإشراف الدلالي الضعيف)
  - semi-supervised (شبه الخاضع للإشراف)
  - annotation cost (تكلفة التعليق التوضيحي)
  - unsupervised setting (الإعداد غير الخاضع للإشراف)
  - label permutation (تبديل التسميات)

- **Equations:** None
- **Citations:** None directly in this section
- **Special handling:**
  - Task examples preserved with arrows: dog → cat, horse → zebra, photos → labels
  - "ImageNet" kept as proper dataset name
  - Maintained the reflective and forward-looking tone of the discussion
  - Preserved the acknowledgment of limitations while emphasizing contributions

### Quality Metrics

- **Semantic equivalence:** 0.89 - All limitations and future directions accurately conveyed
- **Technical accuracy:** 0.90 - Failure modes and technical challenges correctly described
- **Readability:** 0.87 - Clear discussion of limitations and future work
- **Glossary consistency:** 0.86 - Consistent terminology for evaluation concepts
- **Overall section score:** 0.88

### Back-Translation Check (Key Paragraph)

**Arabic:** نلاحظ أيضاً فجوة باقية بين النتائج القابلة للتحقيق مع بيانات التدريب المقترنة وتلك التي تحققها طريقتنا غير المقترنة. في بعض الحالات، قد يكون من الصعب جداً - أو حتى المستحيل - سد هذه الفجوة.

**Back to English:** We also observe a remaining gap between the results achievable with paired training data and those achieved by our unpaired method. In some cases, it may be very difficult - or even impossible - to close this gap.

**Assessment:** ✅ Semantically equivalent, honest assessment of limitations preserved
