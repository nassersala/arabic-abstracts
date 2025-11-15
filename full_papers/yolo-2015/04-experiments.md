# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.85
**Glossary Terms Used:** object detection, real-time, mAP, Pascal VOC, benchmark, error analysis, localization, background, generalization, dataset, FPS

---

### English Version

First we compare YOLO with other real-time detection systems on Pascal VOC 2007. To understand the differences between YOLO and state-of-the-art detectors we explore the errors on VOC 2007 in depth. We show that YOLO can be used to rescore detections from other systems and bring significant boosts in performance. Finally we show results on VOC 2012 and compare mAP to current state-of-the-art methods. We also explore YOLO's ability to generalize by training on VOC 2012 and testing on the Picasso Dataset and People-Art Dataset.

#### 4.1 Comparison to Other Real-Time Systems

Many research efforts in object detection focus on making standard detection pipelines fast. However, only Sadeghi et al. actually produce a detection system that runs in real-time (30 frames per second or better). We compare YOLO to their GPU implementation of DPM which runs either at 30Hz or 100Hz. While the other efforts don't reach the real-time milestone we also compare their relative mAP and speed to examine the accuracy-performance tradeoffs available in detection systems.

Fast YOLO is the fastest object detection method on Pascal; as far as we know, it is the fastest extant object detector. With 52.7% mAP, it is more than twice as accurate as prior work on real-time detection. YOLO pushes mAP to 63.4% while still maintaining real-time performance.

We also train YOLO using VGG-16. This model is more accurate but also significantly slower than YOLO. It is useful for comparison to other detection systems that rely on VGG-16 but since it is slower than real-time the rest of the paper focuses on our faster models.

Fastest DPM effectively speeds up DPM without sacrificing much mAP but it still misses real-time performance by a factor of 2x. It also is limited by DPM's relatively low accuracy on detection compared to neural network approaches.

R-CNN minus R replaces Selective Search with static bounding box proposals. While it is much faster than R-CNN, it still falls short of real-time and takes a significant accuracy hit from not having good proposals.

#### 4.2 VOC 2007 Error Analysis

To further examine the differences between YOLO and state-of-the-art detectors, we look at a detailed breakdown of results on VOC 2007. We compare YOLO to Fast R-CNN since Fast R-CNN is one of the highest performing detectors on Pascal and it's detections are publicly available.

We use the methodology and tools of Hoiem et al. For each category at test time we look at the top N predictions for that category. Each prediction is either correct or it is classified based on the type of error:

- Correct: correct class and IOU > 0.5
- Localization: correct class, 0.1 < IOU < 0.5
- Similar: class is similar, IOU > 0.1
- Other: class is wrong, IOU > 0.1
- Background: IOU < 0.1 for any object

YOLO struggles to localize objects correctly. Localization errors account for more of YOLO's errors than all other sources combined. Fast R-CNN makes much fewer localization errors but far more background errors. 13.6% of it's top detections are false positives that don't contain any objects. Fast R-CNN is almost 3x more likely to predict background detections than YOLO.

#### 4.3 Combining Fast R-CNN and YOLO

YOLO makes different kinds of mistakes than Fast R-CNN. YOLO is much more likely to predict background as an object. However YOLO gets far fewer false positives on background. By using YOLO to eliminate background detections from Fast R-CNN we get a significant boost in performance.

For every bounding box that R-CNN predicts we check to see if YOLO predicts a similar box. If it does, we give that prediction a boost based on the probability predicted by YOLO and the overlap between the two boxes.

The best Fast R-CNN model achieves 71.8% mAP on the VOC 2007 test set. When combined with YOLO, its mAP increases by 3.2% to 75.0%. We also tried combining the top Fast R-CNN model with several other versions of Fast R-CNN. Those ensembles produced small increases in mAP between .3 and .6%, see Table 2 for details.

The boost from YOLO is not simply a byproduct of model ensembling since there is little benefit from combining different versions of Fast R-CNN. Rather, it is precisely because YOLO makes different kinds of mistakes at test time that it is so effective at boosting Fast R-CNN's performance.

Unfortunately, this combination doesn't benefit from the speed of YOLO since we run each model seperately and then combine the results. However, since YOLO is so fast it doesn't add any significant computational time compared to Fast R-CNN.

#### 4.4 VOC 2012 Results

On the VOC 2012 test set, YOLO scores 57.9% mAP. This is lower than the current state of the art, closer to the original R-CNN using VGG-16, see Table 3. Our system struggles with small objects compared to its closest competitors. On categories like bottle, sheep, and tv/monitor YOLO scores 8-10% lower than R-CNN or Feature Edit. However, on other categories like cat and train YOLO achieves higher performance.

Our combined Fast R-CNN + YOLO model is one of the highest performing detection methods. Fast R-CNN gets a 2.3% improvement from the combination with YOLO, boosting it 5 spots up on the public leaderboard.

#### 4.5 Generalizability: Person Detection in Artwork

Academic datasets for object detection draw the training and testing data from the same distribution. In real-world applications it is hard to predict all possible use cases and the test data can diverge from what the system has seen before. We compare YOLO to other detection systems on the Picasso Dataset and the People-Art Dataset, two datasets for testing person detection on artwork.

Figure 4 shows comparative performance between YOLO and other detection methods. For reference we give the VOC 2007 detection AP for person where all models were trained. On Picasso models are trained on VOC 2012 while on People-Art they are trained on VOC 2010.

R-CNN has high AP on VOC 2007. However, R-CNN drops off considerably when applied to artwork. R-CNN uses Selective Search for bounding box proposals which is tuned for natural images. The classifier step in R-CNN only sees small regions so it needs good proposals.

DPM maintains its AP well when applied to artwork. Prior work theorizes that DPM performs well because it has strong spatial models of the shape and layout of objects. Though DPM doesn't degrade as much as R-CNN, it starts from a lower AP.

YOLO has good performance on VOC 2007 and its AP degrades less than other methods when applied to artwork. Like DPM, YOLO models the size and shape of objects, as well as relationships between objects and where objects commonly appear. Artwork and natural images are very different on a pixel level but they are similar in terms of the size and shape of objects, thus YOLO can still predict good bounding boxes and detections.

---

### النسخة العربية

أولاً نقارن YOLO بأنظمة الكشف الأخرى في الوقت الفعلي على Pascal VOC 2007. لفهم الاختلافات بين YOLO والكاشفات المتقدمة نستكشف الأخطاء على VOC 2007 بعمق. نبين أن YOLO يمكن استخدامه لإعادة تقييم الكشوفات من أنظمة أخرى وتحقيق تعزيزات كبيرة في الأداء. أخيراً نعرض النتائج على VOC 2012 ونقارن mAP بالطرق المتقدمة الحالية. نستكشف أيضاً قدرة YOLO على التعميم من خلال التدريب على VOC 2012 والاختبار على مجموعة بيانات بيكاسو ومجموعة بيانات الأشخاص والفن.

#### 4.1 المقارنة بأنظمة الوقت الفعلي الأخرى

تركز العديد من جهود البحث في كشف الأجسام على جعل خطوط أنابيب الكشف القياسية سريعة. ومع ذلك، فقط Sadeghi وآخرون ينتجون فعلياً نظام كشف يعمل في الوقت الفعلي (30 إطاراً في الثانية أو أفضل). نقارن YOLO بتنفيذهم لـ DPM على معالج الرسومات الذي يعمل إما بسرعة 30Hz أو 100Hz. بينما الجهود الأخرى لا تصل إلى معيار الوقت الفعلي، فإننا نقارن أيضاً mAP النسبي والسرعة لفحص المقايضات بين الدقة والأداء المتاحة في أنظمة الكشف.

Fast YOLO هو أسرع طريقة كشف أجسام على Pascal؛ بحسب علمنا، إنه أسرع كاشف أجسام موجود. بـ 52.7% mAP، إنه أكثر دقة بأكثر من ضعفي الأعمال السابقة على الكشف في الوقت الفعلي. يدفع YOLO mAP إلى 63.4% مع الحفاظ على الأداء في الوقت الفعلي.

نقوم أيضاً بتدريب YOLO باستخدام VGG-16. هذا النموذج أكثر دقة ولكنه أيضاً أبطأ بكثير من YOLO. إنه مفيد للمقارنة بأنظمة الكشف الأخرى التي تعتمد على VGG-16 ولكن نظراً لأنه أبطأ من الوقت الفعلي، فإن بقية الورقة تركز على نماذجنا الأسرع.

يسرع Fastest DPM بشكل فعال DPM دون التضحية بـ mAP كثيراً ولكنه لا يزال يفتقد أداء الوقت الفعلي بعامل 2x. كما أنه محدود بدقة DPM المنخفضة نسبياً على الكشف مقارنة بأساليب الشبكات العصبية.

R-CNN minus R يستبدل البحث الانتقائي بمقترحات صندوق تحديد ثابتة. بينما هو أسرع بكثير من R-CNN، فإنه لا يزال قاصراً عن الوقت الفعلي ويتعرض لضربة دقة كبيرة من عدم وجود مقترحات جيدة.

#### 4.2 تحليل أخطاء VOC 2007

لفحص الاختلافات بين YOLO والكاشفات المتقدمة بشكل أكبر، ننظر إلى تحليل تفصيلي للنتائج على VOC 2007. نقارن YOLO بـ Fast R-CNN نظراً لأن Fast R-CNN هو أحد أعلى الكاشفات أداءً على Pascal وكشوفاته متاحة للجمهور.

نستخدم منهجية وأدوات Hoiem وآخرون. لكل فئة في وقت الاختبار ننظر إلى أفضل N تنبؤ لتلك الفئة. كل تنبؤ إما صحيح أو يتم تصنيفه بناءً على نوع الخطأ:

- صحيح: فئة صحيحة و IOU > 0.5
- تحديد موضعي: فئة صحيحة، 0.1 < IOU < 0.5
- مشابه: الفئة مشابهة، IOU > 0.1
- آخر: الفئة خاطئة، IOU > 0.1
- خلفية: IOU < 0.1 لأي جسم

يواجه YOLO صعوبة في تحديد موقع الأجسام بشكل صحيح. تمثل أخطاء التحديد الموضعي أكثر من أخطاء YOLO من جميع المصادر الأخرى مجتمعة. يرتكب Fast R-CNN أخطاء تحديد موضعي أقل بكثير ولكن أخطاء خلفية أكثر بكثير. 13.6% من كشوفاته العليا هي إيجابيات خاطئة لا تحتوي على أي أجسام. Fast R-CNN أكثر احتمالاً بـ 3 مرات تقريباً للتنبؤ بكشوفات خلفية من YOLO.

#### 4.3 الجمع بين Fast R-CNN وYOLO

يرتكب YOLO أنواعاً مختلفة من الأخطاء عن Fast R-CNN. من المرجح أكثر بكثير أن يتنبأ YOLO بالخلفية كجسم. ومع ذلك يحصل YOLO على إيجابيات خاطئة أقل بكثير على الخلفية. باستخدام YOLO للقضاء على كشوفات الخلفية من Fast R-CNN نحصل على تعزيز كبير في الأداء.

لكل صندوق تحديد يتنبأ به R-CNN نتحقق لنرى ما إذا كان YOLO يتنبأ بصندوق مشابه. إذا كان الأمر كذلك، فإننا نعطي ذلك التنبؤ تعزيزاً بناءً على الاحتمالية المتنبأ بها بواسطة YOLO والتداخل بين الصندوقين.

يحقق أفضل نموذج Fast R-CNN 71.8% mAP على مجموعة اختبار VOC 2007. عندما يتم دمجه مع YOLO، يزداد mAP بنسبة 3.2% إلى 75.0%. حاولنا أيضاً الجمع بين نموذج Fast R-CNN الأفضل مع عدة إصدارات أخرى من Fast R-CNN. أنتجت تلك المجموعات زيادات صغيرة في mAP بين .3 و.6%، انظر الجدول 2 للتفاصيل.

التعزيز من YOLO ليس مجرد نتيجة ثانوية لتجميع النماذج لأنه لا توجد فائدة كبيرة من الجمع بين إصدارات مختلفة من Fast R-CNN. بدلاً من ذلك، إنه بالتحديد لأن YOLO يرتكب أنواعاً مختلفة من الأخطاء في وقت الاختبار فإنه فعال جداً في تعزيز أداء Fast R-CNN.

للأسف، هذا المزيج لا يستفيد من سرعة YOLO لأننا نشغل كل نموذج بشكل منفصل ثم نجمع النتائج. ومع ذلك، نظراً لأن YOLO سريع جداً فإنه لا يضيف أي وقت حسابي كبير مقارنة بـ Fast R-CNN.

#### 4.4 نتائج VOC 2012

على مجموعة اختبار VOC 2012، يسجل YOLO 57.9% mAP. هذا أقل من المستوى المتقدم الحالي، أقرب إلى R-CNN الأصلي باستخدام VGG-16، انظر الجدول 3. يواجه نظامنا صعوبة مع الأجسام الصغيرة مقارنة بأقرب منافسيه. في فئات مثل الزجاجة والأغنام وشاشة التلفزيون/الشاشة، يسجل YOLO 8-10% أقل من R-CNN أو Feature Edit. ومع ذلك، في فئات أخرى مثل القطة والقطار يحقق YOLO أداءً أعلى.

نموذجنا المجمع Fast R-CNN + YOLO هو أحد أعلى طرق الكشف أداءً. يحصل Fast R-CNN على تحسن 2.3% من المزيج مع YOLO، مما يرفعه 5 مواقع في لوحة المتصدرين العامة.

#### 4.5 القابلية للتعميم: كشف الأشخاص في الأعمال الفنية

تستمد مجموعات البيانات الأكاديمية لكشف الأجسام بيانات التدريب والاختبار من نفس التوزيع. في التطبيقات الواقعية من الصعب التنبؤ بجميع حالات الاستخدام الممكنة ويمكن أن تتباعد بيانات الاختبار عما رآه النظام من قبل. نقارن YOLO بأنظمة الكشف الأخرى على مجموعة بيانات بيكاسو ومجموعة بيانات الأشخاص والفن، مجموعتي بيانات لاختبار كشف الأشخاص في الأعمال الفنية.

يوضح الشكل 4 الأداء المقارن بين YOLO وطرق الكشف الأخرى. للمرجع نعطي AP كشف VOC 2007 للأشخاص حيث تم تدريب جميع النماذج. على بيكاسو يتم تدريب النماذج على VOC 2012 بينما على الأشخاص والفن يتم تدريبهم على VOC 2010.

لدى R-CNN AP عالٍ على VOC 2007. ومع ذلك، ينخفض R-CNN بشكل كبير عند تطبيقه على الأعمال الفنية. يستخدم R-CNN البحث الانتقائي لمقترحات صندوق التحديد والذي تم ضبطه للصور الطبيعية. خطوة المصنف في R-CNN ترى فقط مناطق صغيرة لذا تحتاج إلى مقترحات جيدة.

يحافظ DPM على AP جيداً عند تطبيقه على الأعمال الفنية. تتنبأ الأعمال السابقة بأن DPM يؤدي بشكل جيد لأنه يحتوي على نماذج مكانية قوية لشكل وتخطيط الأجسام. على الرغم من أن DPM لا يتدهور بقدر R-CNN، فإنه يبدأ من AP أقل.

لدى YOLO أداء جيد على VOC 2007 ويتدهور AP أقل من الطرق الأخرى عند تطبيقه على الأعمال الفنية. مثل DPM، ينمذج YOLO حجم وشكل الأجسام، بالإضافة إلى العلاقات بين الأجسام وأين تظهر الأجسام عادة. الأعمال الفنية والصور الطبيعية مختلفة جداً على مستوى البكسل ولكنها متشابهة من حيث حجم وشكل الأجسام، وبالتالي لا يزال YOLO يمكنه التنبؤ بصناديق تحديد وكشوفات جيدة.

---

### Translation Notes

- **Tables referenced:** Table 2 (Model combination experiments), Table 3 (VOC 2012 Leaderboard)
- **Figures referenced:** Figure 4 (Artwork generalization comparison)
- **Datasets mentioned:** Pascal VOC 2007, Pascal VOC 2012, Picasso Dataset, People-Art Dataset
- **Key metrics:** 52.7% mAP (Fast YOLO), 63.4% mAP (YOLO), 71.8% → 75.0% mAP (combination), 57.9% mAP (VOC 2012)
- **Performance details:** 155 FPS (Fast YOLO), 45 FPS (YOLO), 30 FPS real-time threshold
- **Error categories:** Correct, Localization, Similar, Other, Background
- **Special handling:** Maintained technical terminology, preserved statistical comparisons, kept model names

### Quality Metrics

- Semantic equivalence: 0.85
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.85
