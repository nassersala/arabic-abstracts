# Section 4: Experiments
## القسم 4: التجارب

**Section:** Experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** object detection, mean average precision (mAP), precision, recall, bounding box, localization, classification, real-time, convolutional, neural network, false positive, training, validation, generalization

---

### English Version

First we compare YOLO with other real-time detection systems on PASCAL VOC 2007. To understand the differences between YOLO and R-CNN variants we explore the errors on VOC 2007 made by YOLO and Fast R-CNN, one of the highest performing versions of R-CNN [14]. Based on the different error profiles we show that YOLO can be used to rescore Fast R-CNN detections and reduce the errors from background false positives, giving a significant performance boost. We also present VOC 2012 results and compare mAP to current state-of-the-art methods. Finally, we show that YOLO generalizes to new domains better than other detectors on two artwork datasets.

**4.1 Comparison to Other Real-Time Systems**

Many research efforts in object detection focus on making standard detection pipelines fast. [5][38][31][14][17][28] However, only Sadeghi et al. actually produce a detection system that runs in real-time (30 frames per second or better) [31]. We compare YOLO to their GPU implementation of DPM which runs either at 30Hz or 100Hz. While the other efforts don't reach the real-time milestone we also compare their relative mAP and speed to examine the accuracy-performance tradeoffs available in object detection systems.

Fast YOLO is the fastest object detection method on PASCAL; as far as we know, it is the fastest extant object detector. With 52.7% mAP, it is more than twice as accurate as prior work on real-time detection. YOLO pushes mAP to 63.4% while still maintaining real-time performance.

We also train YOLO using VGG-16. This model is more accurate but also significantly slower than YOLO. It is useful for comparison to other detection systems that rely on VGG-16 but since it is slower than real-time the rest of the paper focuses on our faster models.

Fastest DPM effectively speeds up DPM without sacrificing much mAP but it still misses real-time performance by a factor of 2×. It also is limited by DPM's relatively low accuracy on detection compared to neural network approaches.

R-CNN minus R replaces Selective Search with static bounding box proposals [20]. While it is much faster than R-CNN, it still falls short of real-time and takes a significant accuracy hit from not having good proposals.

Fast R-CNN speeds up the classification stage of R-CNN but it still relies on selective search which can take around 2 seconds per image to generate bounding box proposals. Thus it has high mAP but at 0.5 fps it is still far from real-time.

The recent Faster R-CNN replaces selective search with a neural network to propose bounding boxes, similar to Szegedy et al.[8] In our tests, their most accurate model achieves 7 fps while a smaller, less accurate one runs at 18 fps. The VGG-16 version of Faster R-CNN is 10 mAP higher but is also 6 times slower than YOLO. The ZeilerFergus Faster R-CNN is only 2.5 times slower than YOLO but is also less accurate.

**4.2 VOC 2007 Error Analysis**

To further examine the differences between YOLO and state-of-the-art detectors, we look at a detailed breakdown of results on VOC 2007. We compare YOLO to Fast R-CNN since Fast R-CNN is one of the highest performing detectors on PASCAL and its detections are publicly available.

We use the methodology and tools of Hoiem et al. [19] For each category at test time we look at the top N predictions for that category. Each prediction is either correct or it is classified based on the type of error:

- **Correct**: correct class and IOU > .5
- **Localization**: correct class, .1 < IOU < .5
- **Similar**: class is similar, IOU > .1
- **Other**: class is wrong, IOU > .1
- **Background**: IOU < .1 for any object

Figure 4 shows the breakdown of each error type averaged across all 20 classes.

YOLO struggles to localize objects correctly. Localization errors account for more of YOLO's errors than all other sources combined. Fast R-CNN makes much fewer localization errors but far more background errors. 13.6% of its top detections are false positives that don't contain any objects. Fast R-CNN is almost 3x more likely than YOLO to predict background detections.

**4.3 Combining Fast R-CNN and YOLO**

YOLO makes far fewer background mistakes than Fast R-CNN. By using YOLO to eliminate background detections from Fast R-CNN we get a significant boost in performance. For every bounding box that R-CNN predicts we check to see if YOLO predicts a similar box. If it does, we give that prediction a boost based on the probability predicted by YOLO and the overlap between the two boxes.

The best Fast R-CNN model achieves a mAP of 71.8% on the VOC 2007 test set. When combined with YOLO, its mAP increases by 3.2% to 75.0%. We also tried combining the top Fast R-CNN model with several other versions of Fast R-CNN. Those ensembles produced small increases in mAP between .3 and .6%, see Table 2 for details.

The boost from YOLO is not simply a byproduct of model ensembling since there is little benefit from combining different versions of Fast R-CNN. Rather, it is precisely because YOLO makes different kinds of mistakes at test time that it is so effective at boosting Fast R-CNN's performance.

Unfortunately, this combination doesn't benefit from the speed of YOLO since we run each model separately and then combine the results. However, since YOLO is so fast it doesn't add any significant computational time compared to Fast R-CNN.

**4.4 VOC 2012 Results**

On the VOC 2012 test set, YOLO scores 57.9% mAP. This is lower than the current state of the art, closer to the original R-CNN using VGG-16, see Table 3. Our system struggles with small objects compared to its closest competitors. On categories like bottle, sheep, and tv/monitor YOLO scores 8-10% lower than R-CNN or Feature Edit. However, on other categories like cat and train YOLO achieves higher performance.

Our combined Fast R-CNN + YOLO model is one of the highest performing detection methods. Fast R-CNN gets a 2.3% improvement from the combination with YOLO, boosting it 5 spots up on the public leaderboard.

**4.5 Generalization to Other Domains**

We train YOLO on VOC 2012 and test it on the Picasso Dataset [12] and the People-Art Dataset [3], two datasets for testing person detection on artwork. Figure 5 shows comparative performance between YOLO and other detection methods.

For reference we give the VOC 2007 detection AP for all methods on the person category as well as the AP on the artwork datasets. R-CNN has high AP on VOC 2007. However, R-CNN drops off considerably when applied to artwork. R-CNN uses Selective Search for bounding box proposals which is tuned for natural images. The classifier step in R-CNN only sees small regions and needs good proposals.

DPM maintains its AP well when applied to artwork. Prior work theorizes that DPM performs well because it has strong spatial models of the shape and layout of objects. Though DPM doesn't degrade as much as R-CNN, it starts from a lower AP.

YOLO has good performance on VOC 2007 and its AP degrades less than other methods when applied to artwork. Like DPM, YOLO models the size and shape of objects, as well as relationships between objects and where objects commonly appear. Artwork and natural images are very different on a pixel level but they are similar in terms of the size and shape of objects, thus YOLO still performs well.

---

### النسخة العربية

أولاً نقارن YOLO مع أنظمة الكشف الأخرى في الوقت الفعلي على PASCAL VOC 2007. لفهم الاختلافات بين YOLO ومتغيرات R-CNN نستكشف الأخطاء على VOC 2007 التي يرتكبها YOLO وFast R-CNN، وهي واحدة من أكثر إصدارات R-CNN أداءً عالياً [14]. بناءً على ملفات الأخطاء المختلفة نُظهر أن YOLO يمكن استخدامه لإعادة تسجيل اكتشافات Fast R-CNN وتقليل الأخطاء من الإيجابيات الخاطئة للخلفية، مما يعطي دفعة أداء كبيرة. نقدم أيضاً نتائج VOC 2012 ونقارن mAP بالطرق الحالية المتقدمة. أخيراً، نُظهر أن YOLO يعمم إلى مجالات جديدة أفضل من الكاشفات الأخرى على مجموعتي بيانات أعمال فنية.

**4.1 المقارنة مع أنظمة الوقت الفعلي الأخرى**

تركز العديد من جهود البحث في كشف الأجسام على جعل خطوط أنابيب الكشف القياسية سريعة. [5][38][31][14][17][28] ومع ذلك، فإن Sadeghi et al. فقط ينتجون فعلياً نظام كشف يعمل في الوقت الفعلي (30 إطاراً في الثانية أو أفضل) [31]. نقارن YOLO بتنفيذهم لـ DPM على GPU والذي يعمل إما عند 30Hz أو 100Hz. بينما لا تصل الجهود الأخرى إلى معلم الوقت الفعلي، فإننا نقارن أيضاً mAP النسبي والسرعة لدراسة مقايضات الدقة والأداء المتاحة في أنظمة كشف الأجسام.

Fast YOLO هو أسرع طريقة لكشف الأجسام على PASCAL؛ بقدر ما نعلم، إنه أسرع كاشف أجسام موجود. مع 52.7% mAP، إنه أكثر دقة بمرتين من العمل السابق على الكشف في الوقت الفعلي. يدفع YOLO mAP إلى 63.4% مع الحفاظ على الأداء في الوقت الفعلي.

نقوم أيضاً بتدريب YOLO باستخدام VGG-16. هذا النموذج أكثر دقة ولكنه أيضاً أبطأ بكثير من YOLO. إنه مفيد للمقارنة مع أنظمة الكشف الأخرى التي تعتمد على VGG-16 ولكن نظراً لأنه أبطأ من الوقت الفعلي، فإن بقية البحث تركز على نماذجنا الأسرع.

يسرع Fastest DPM بشكل فعال DPM دون التضحية بالكثير من mAP ولكنه لا يزال يفوت أداء الوقت الفعلي بعامل 2×. كما أنه محدود بدقة DPM المنخفضة نسبياً على الكشف مقارنة بنهج الشبكات العصبية.

يستبدل R-CNN minus R البحث الانتقائي باقتراحات صندوق تحديد ثابتة [20]. بينما هو أسرع بكثير من R-CNN، لا يزال يقصر عن الوقت الفعلي ويأخذ ضربة دقة كبيرة من عدم وجود اقتراحات جيدة.

يسرع Fast R-CNN مرحلة التصنيف من R-CNN ولكنه لا يزال يعتمد على البحث الانتقائي الذي يمكن أن يستغرق حوالي 2 ثانية لكل صورة لتوليد اقتراحات صندوق التحديد. وبالتالي لديه mAP عالٍ ولكن عند 0.5 fps لا يزال بعيداً عن الوقت الفعلي.

يستبدل Faster R-CNN الأحدث البحث الانتقائي بشبكة عصبية لاقتراح صناديق التحديد، على غرار Szegedy et al.[8] في اختباراتنا، يحقق نموذجهم الأكثر دقة 7 fps بينما يعمل نموذج أصغر وأقل دقة عند 18 fps. إصدار VGG-16 من Faster R-CNN أعلى بـ 10 mAP ولكنه أيضاً أبطأ 6 مرات من YOLO. ZeilerFergus Faster R-CNN أبطأ فقط 2.5 مرة من YOLO ولكنه أيضاً أقل دقة.

**4.2 تحليل أخطاء VOC 2007**

لمزيد من فحص الاختلافات بين YOLO والكاشفات المتقدمة، ننظر إلى تفصيل مفصل للنتائج على VOC 2007. نقارن YOLO بـ Fast R-CNN حيث أن Fast R-CNN هي واحدة من أعلى الكاشفات أداءً على PASCAL واكتشافاتها متاحة للجمهور.

نستخدم منهجية وأدوات Hoiem et al. [19] لكل فئة في وقت الاختبار ننظر إلى أعلى N تنبؤ لتلك الفئة. كل تنبؤ إما صحيح أو يتم تصنيفه بناءً على نوع الخطأ:

- **صحيح**: فئة صحيحة وIOU > .5
- **التحديد الموضعي**: فئة صحيحة، .1 < IOU < .5
- **مشابه**: الفئة متشابهة، IOU > .1
- **آخر**: الفئة خاطئة، IOU > .1
- **خلفية**: IOU < .1 لأي جسم

يُظهر الشكل 4 تفصيل كل نوع خطأ بمتوسط عبر جميع الفئات الـ 20.

يكافح YOLO لتحديد موقع الأجسام بشكل صحيح. تمثل أخطاء التحديد الموضعي المزيد من أخطاء YOLO من جميع المصادر الأخرى مجتمعة. يرتكب Fast R-CNN أخطاء تحديد موضعي أقل بكثير ولكن أخطاء خلفية أكثر بكثير. 13.6% من اكتشافاته العليا هي إيجابيات خاطئة لا تحتوي على أي أجسام. Fast R-CNN أكثر احتمالاً بحوالي 3 مرات من YOLO للتنبؤ باكتشافات خلفية.

**4.3 دمج Fast R-CNN وYOLO**

يرتكب YOLO أخطاء خلفية أقل بكثير من Fast R-CNN. باستخدام YOLO للقضاء على اكتشافات الخلفية من Fast R-CNN نحصل على دفعة كبيرة في الأداء. لكل صندوق تحديد يتنبأ به R-CNN نتحقق لنرى ما إذا كان YOLO يتنبأ بصندوق مشابه. إذا كان الأمر كذلك، نعطي ذلك التنبؤ دفعة بناءً على الاحتمال الذي تنبأ به YOLO والتداخل بين الصندوقين.

يحقق أفضل نموذج Fast R-CNN mAP بنسبة 71.8% على مجموعة اختبار VOC 2007. عندما يتم دمجه مع YOLO، يزيد mAP بنسبة 3.2% إلى 75.0%. حاولنا أيضاً دمج نموذج Fast R-CNN الأعلى مع عدة إصدارات أخرى من Fast R-CNN. أنتجت تلك المجموعات زيادات صغيرة في mAP بين .3 و.6%، انظر الجدول 2 للتفاصيل.

الدفعة من YOLO ليست مجرد منتج ثانوي لتجميع النماذج حيث أن هناك فائدة قليلة من دمج إصدارات مختلفة من Fast R-CNN. بدلاً من ذلك، هو بالتحديد لأن YOLO يرتكب أنواعاً مختلفة من الأخطاء في وقت الاختبار أنه فعال جداً في تعزيز أداء Fast R-CNN.

لسوء الحظ، هذا المزيج لا يستفيد من سرعة YOLO لأننا نشغل كل نموذج بشكل منفصل ثم ندمج النتائج. ومع ذلك، نظراً لأن YOLO سريع جداً فإنه لا يضيف أي وقت حسابي كبير مقارنة بـ Fast R-CNN.

**4.4 نتائج VOC 2012**

على مجموعة اختبار VOC 2012، يسجل YOLO 57.9% mAP. هذا أقل من الحالة الحالية المتقدمة، أقرب إلى R-CNN الأصلي باستخدام VGG-16، انظر الجدول 3. يكافح نظامنا مع الأجسام الصغيرة مقارنة بمنافسيه الأقرب. على فئات مثل الزجاجة، الأغنام، وتلفاز/شاشة، يسجل YOLO 8-10% أقل من R-CNN أو Feature Edit. ومع ذلك، على فئات أخرى مثل القطة والقطار يحقق YOLO أداء أعلى.

نموذجنا المدمج Fast R-CNN + YOLO هو واحد من أعلى طرق الكشف أداءً. يحصل Fast R-CNN على تحسن 2.3% من المزيج مع YOLO، مما يدفعه 5 مراكز لأعلى في لوحة المتصدرين العامة.

**4.5 التعميم إلى مجالات أخرى**

نقوم بتدريب YOLO على VOC 2012 ونختبره على مجموعة بيانات بيكاسو [12] ومجموعة بيانات الأشخاص والفن [3]، مجموعتا بيانات لاختبار كشف الأشخاص على الأعمال الفنية. يُظهر الشكل 5 الأداء المقارن بين YOLO وطرق الكشف الأخرى.

للمرجعية نعطي VOC 2007 detection AP لجميع الطرق على فئة الشخص بالإضافة إلى AP على مجموعات بيانات الأعمال الفنية. R-CNN لديها AP عالية على VOC 2007. ومع ذلك، تنخفض R-CNN بشكل كبير عند تطبيقها على الأعمال الفنية. تستخدم R-CNN البحث الانتقائي لاقتراحات صندوق التحديد والتي يتم ضبطها للصور الطبيعية. خطوة المصنف في R-CNN ترى فقط مناطق صغيرة وتحتاج إلى اقتراحات جيدة.

يحافظ DPM على AP جيداً عند تطبيقه على الأعمال الفنية. تنظّر الأعمال السابقة أن DPM يؤدي جيداً لأن لديه نماذج مكانية قوية لشكل وتخطيط الأجسام. على الرغم من أن DPM لا يتدهور بقدر R-CNN، فإنه يبدأ من AP أقل.

YOLO لديه أداء جيد على VOC 2007 وAP الخاص به يتدهور أقل من الطرق الأخرى عند تطبيقه على الأعمال الفنية. مثل DPM، يمثل YOLO حجم وشكل الأجسام، بالإضافة إلى العلاقات بين الأجسام وأين تظهر الأجسام عادة. الأعمال الفنية والصور الطبيعية مختلفة جداً على مستوى البكسل ولكنها متشابهة من حيث حجم وشكل الأجسام، وبالتالي لا يزال YOLO يؤدي بشكل جيد.

---

### Translation Notes

- **Figures referenced:** Figure 4 (error breakdown), Figure 5 (generalization performance)
- **Tables referenced:** Table 2 (ensemble results), Table 3 (VOC 2012 results)
- **Key terms introduced:** VOC 2007, VOC 2012, PASCAL, mAP (mean Average Precision), AP (Average Precision), fps (frames per second), VGG-16, ZeilerFergus, Picasso Dataset, People-Art Dataset, false positive, background error, localization error, ensemble
- **Equations:** 0
- **Citations:** [3], [5], [8], [12], [14], [17], [19], [20], [28], [31], [38]
- **Special handling:**
  - Performance numbers preserved (52.7% mAP, 63.4% mAP, 71.8% mAP, 75.0% mAP, 57.9% mAP, etc.)
  - Speed metrics preserved (30 fps, 100Hz, 7 fps, 18 fps, 0.5 fps)
  - Dataset names kept in English (PASCAL VOC, Picasso Dataset, People-Art Dataset)
  - Model names kept in English (VGG-16, ZeilerFergus, etc.)
  - Error categories translated but kept technical precision

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
