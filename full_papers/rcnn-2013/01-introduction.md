# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** features, visual recognition, object detection, CNNs, convolutional neural networks, SIFT, HOG, supervised training, backpropagation, image classification, region proposals, semantic segmentation, bounding box, fine-tuning, pre-training

---

### English Version

Features matter. The last decade of progress on various visual recognition tasks has been based considerably on the use of SIFT [29] and HOG [7]. But if we look at performance on the canonical visual recognition task, PASCAL VOC object detection [15], it is generally acknowledged that progress has been slow during 2010-2012, with small gains obtained by building ensemble systems and employing minor variants of successful methods.

SIFT and HOG are blockwise orientation histograms, a representation we could associate roughly with complex cells in V1, the first cortical area in the primate visual pathway. But we also know that recognition occurs several stages downstream, which suggests that there might be hierarchical, multi-stage processes for computing features that are even more informative for visual recognition.

Fukushima's "neocognitron" [19], a biologically-inspired hierarchical and shift-invariant model for pattern recognition, was an early attempt at just such a process. The neocognitron, however, lacked a supervised training algorithm. Building on Rumelhart et al. [33], LeCun et al. [26] showed that stochastic gradient descent via backpropagation was effective for training convolutional neural networks (CNNs), a class of models that extend the neocognitron.

CNNs saw heavy use in the 1990s (e.g., [27]), but then fell out of fashion with the rise of support vector machines. In 2012, Krizhevsky et al. [25] rekindled interest in CNNs by showing substantially higher image classification accuracy on the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) [9, 10]. Their success resulted from training a large CNN on 1.2 million labeled images, together with a few twists on LeCun's CNN (e.g., max(x,0) rectifying non-linearities and "dropout" regularization).

The significance of the ImageNet result was vigorously debated during the ILSVRC 2012 workshop. The central issue can be distilled to the following: To what extent do the CNN classification results on ImageNet generalize to object detection results on the PASCAL VOC Challenge?

We answer this question by bridging the gap between image classification and object detection. This paper is the first to show that a CNN can lead to dramatically higher object detection performance on PASCAL VOC as compared to systems based on simpler HOG-like features. To achieve this result, we focused on two problems: localizing objects with a deep network and training a high-capacity model with only a small quantity of annotated detection data.

Unlike image classification, detection requires localizing (likely many) objects within an image. One approach frames localization as a regression problem. However, work from Szegedy et al. [38], concurrent with our own, indicates that this strategy may not fare well in practice (they report a mAP of 30.5% on VOC 2007 compared to the 58.5% achieved by our method). An alternative is to build a sliding-window detector. CNNs have been used in this way for at least two decades, typically on constrained object categories, such as faces [32, 40] and pedestrians [35]. In order to maintain high spatial resolution, these CNNs typically only have two convolutional and pooling layers. We also considered adopting a sliding-window approach. However, units high up in our network, which has five convolutional layers, have very large receptive fields (≈195×195 pixels) and strides (≈32×32 pixels) in the input image, which makes precise localization within the sliding-window paradigm an open technical challenge.

Instead, we solve the CNN localization problem by operating within the "recognition using regions" paradigm [21], which has been successful for both object detection [39] and semantic segmentation [5]. At test time, our method generates around 2000 category-independent region proposals for the input image, extracts a fixed-length feature vector from each proposal using a CNN, and then classifies each region with category-specific linear SVMs. We use a simple technique (affine image warping) to compute a fixed-size CNN input from each region proposal, regardless of the region's shape. Figure 1 presents an overview of our method and highlights some of our results. Since our system combines region proposals with CNNs, we dub the method R-CNN: Regions with CNN features.

In this updated version of this paper, we provide a head-to-head comparison of R-CNN and the recently proposed OverFeat [34] detection system by running R-CNN on the 200-class ILSVRC2013 detection dataset. OverFeat uses a sliding-window CNN for detection and until now was the best performing method on ILSVRC2013 detection. We show that R-CNN significantly outperforms OverFeat, with a mAP of 31.4% versus 24.3%.

A second challenge faced in detection is that labeled data is scarce and the amount currently available is insufficient for training a large CNN. The conventional solution to this problem is to use unsupervised pre-training, followed by supervised fine-tuning (e.g., [35]). The second principle contribution of this paper is to show that supervised pre-training on a large auxiliary dataset (ILSVRC), followed by domain-specific fine-tuning on a small dataset (PASCAL), is an effective paradigm for learning high-capacity CNNs when data is scarce. In our experiments, fine-tuning for detection improves mAP performance by 8 percentage points. After fine-tuning, our system achieves a mAP of 54% on VOC 2010 compared to 33% for the highly-tuned, HOG-based deformable part model (DPM) [17, 20]. We also point readers to contemporaneous work by Donahue et al. [12], who show that Krizhevsky's CNN can be used (without fine-tuning) as a blackbox feature extractor, yielding excellent performance on several recognition tasks including scene classification, fine-grained sub-categorization, and domain adaptation.

Our system is also quite efficient. The only class-specific computations are a reasonably small matrix-vector product and greedy non-maximum suppression. This computational property follows from features that are shared across all categories and that are also two orders of magnitude lower-dimensional than previously used region features (cf. [39]).

Understanding the failure modes of our approach is also critical for improving it, and so we report results from the detection analysis tool of Hoiem et al. [23]. As an immediate consequence of this analysis, we demonstrate that a simple bounding-box regression method significantly reduces mislocalizations, which are the dominant error mode.

Before developing technical details, we note that because R-CNN operates on regions it is natural to extend it to the task of semantic segmentation. With minor modifications, we also achieve competitive results on the PASCAL VOC segmentation task, with an average segmentation accuracy of 47.9% on the VOC 2011 test set.

---

### النسخة العربية

الميزات مهمة. لقد اعتمد التقدم في العقد الأخير على مختلف مهام التعرف البصري بشكل كبير على استخدام SIFT [29] وHOG [7]. لكن إذا نظرنا إلى الأداء على مهمة التعرف البصري المعيارية، كشف الأجسام في PASCAL VOC [15]، فمن المعترف به عموماً أن التقدم كان بطيئاً خلال الفترة 2010-2012، مع مكاسب صغيرة تم الحصول عليها من خلال بناء أنظمة تجميعية وتوظيف متغيرات طفيفة من الطرق الناجحة.

SIFT وHOG هما رسوم بيانية اتجاهية على مستوى الكتل، وهو تمثيل يمكننا ربطه تقريباً بالخلايا المعقدة في V1، المنطقة القشرية الأولى في المسار البصري للرئيسيات. لكننا نعلم أيضاً أن التعرف يحدث في عدة مراحل لاحقة، مما يشير إلى أنه قد تكون هناك عمليات هرمية متعددة المراحل لحساب الميزات التي تكون أكثر إفادة للتعرف البصري.

كان "النيوكوجنيترون" لفوكوشيما [19]، وهو نموذج هرمي ومستقل عن الإزاحة مستوحى من الأحياء للتعرف على الأنماط، محاولة مبكرة لمثل هذه العملية. ومع ذلك، افتقر النيوكوجنيترون إلى خوارزمية تدريب موجّهة. بناءً على عمل Rumelhart وآخرون [33]، أظهر LeCun وآخرون [26] أن الانحدار التدرجي العشوائي عبر الانتشار العكسي كان فعالاً لتدريب الشبكات العصبية الالتفافية (CNNs)، وهي فئة من النماذج التي توسع النيوكوجنيترون.

شهدت الشبكات العصبية الالتفافية استخداماً كثيفاً في التسعينيات (على سبيل المثال، [27])، لكنها خرجت من الموضة مع صعود آلات المتجهات الداعمة. في عام 2012، أعاد Krizhevsky وآخرون [25] إحياء الاهتمام بالشبكات العصبية الالتفافية من خلال إظهار دقة تصنيف صور أعلى بكثير في تحدي التعرف البصري واسع النطاق ImageNet (ILSVRC) [9، 10]. نتج نجاحهم من تدريب شبكة عصبية التفافية كبيرة على 1.2 مليون صورة موسومة، بالإضافة إلى بعض التعديلات على شبكة LeCun العصبية الالتفافية (مثل اللاخطيات التصحيحية max(x,0) وتنظيم "الإسقاط" dropout).

تم النقاش بقوة حول أهمية نتيجة ImageNet خلال ورشة عمل ILSVRC 2012. يمكن تلخيص القضية المركزية في ما يلي: إلى أي مدى تعمم نتائج تصنيف الشبكات العصبية الالتفافية على ImageNet إلى نتائج كشف الأجسام على تحدي PASCAL VOC؟

نجيب على هذا السؤال من خلال سد الفجوة بين تصنيف الصور وكشف الأجسام. هذا البحث هو الأول الذي يُظهر أن الشبكات العصبية الالتفافية يمكن أن تؤدي إلى أداء أعلى بشكل كبير في كشف الأجسام على PASCAL VOC مقارنة بالأنظمة القائمة على ميزات أبسط شبيهة بـ HOG. لتحقيق هذه النتيجة، ركزنا على مشكلتين: تحديد موقع الأجسام باستخدام شبكة عميقة وتدريب نموذج عالي السعة باستخدام كمية صغيرة فقط من بيانات الكشف الموسومة.

على عكس تصنيف الصور، يتطلب الكشف تحديد موقع (على الأرجح العديد من) الأجسام داخل الصورة. أحد الأساليب يصيغ تحديد الموقع كمسألة انحدار. ومع ذلك، يشير عمل Szegedy وآخرون [38]، المتزامن مع عملنا، إلى أن هذه الاستراتيجية قد لا تحقق نتائج جيدة عملياً (حيث يبلغون عن mAP بنسبة 30.5% على VOC 2007 مقارنة بـ 58.5% التي حققتها طريقتنا). البديل هو بناء كاشف بنافذة منزلقة. تم استخدام الشبكات العصبية الالتفافية بهذه الطريقة لعقدين على الأقل، عادةً على فئات أجسام محدودة، مثل الوجوه [32، 40] والمشاة [35]. للحفاظ على دقة مكانية عالية، تحتوي هذه الشبكات العصبية الالتفافية عادةً على طبقتين فقط من الطبقات الالتفافية وطبقات التجميع. لقد فكرنا أيضاً في اعتماد نهج النافذة المنزلقة. ومع ذلك، فإن الوحدات العالية في شبكتنا، التي تحتوي على خمس طبقات التفافية، لديها حقول استقبال كبيرة جداً (≈195×195 بكسل) وخطوات (≈32×32 بكسل) في الصورة المدخلة، مما يجعل التحديد الدقيق للموقع ضمن نموذج النافذة المنزلقة تحدياً تقنياً مفتوحاً.

بدلاً من ذلك، نحل مشكلة تحديد الموقع بالشبكات العصبية الالتفافية من خلال العمل ضمن نموذج "التعرف باستخدام المناطق" [21]، الذي نجح في كل من كشف الأجسام [39] والتقسيم الدلالي [5]. في وقت الاختبار، تولد طريقتنا حوالي 2000 مقترح منطقة مستقل عن الفئة للصورة المدخلة، وتستخرج متجه ميزات ذو طول ثابت من كل مقترح باستخدام شبكة عصبية التفافية، ثم تصنف كل منطقة باستخدام آلات متجهات داعمة خطية خاصة بالفئة. نستخدم تقنية بسيطة (التشويه الأفيني للصورة) لحساب مدخل شبكة عصبية التفافية بحجم ثابت من كل مقترح منطقة، بغض النظر عن شكل المنطقة. يعرض الشكل 1 نظرة عامة على طريقتنا ويسلط الضوء على بعض نتائجنا. نظراً لأن نظامنا يجمع بين مقترحات المناطق والشبكات العصبية الالتفافية، نطلق على الطريقة اسم R-CNN: المناطق بميزات الشبكات العصبية الالتفافية.

في هذا الإصدار المحدث من هذا البحث، نقدم مقارنة مباشرة بين R-CNN ونظام الكشف OverFeat [34] المقترح حديثاً من خلال تشغيل R-CNN على مجموعة بيانات كشف ILSVRC2013 المكونة من 200 صنف. يستخدم OverFeat شبكة عصبية التفافية بنافذة منزلقة للكشف وكان حتى الآن الطريقة الأفضل أداءً على كشف ILSVRC2013. نُظهر أن R-CNN يتفوق بشكل كبير على OverFeat، مع mAP بنسبة 31.4% مقابل 24.3%.

التحدي الثاني الذي يواجه الكشف هو أن البيانات الموسومة نادرة والكمية المتاحة حالياً غير كافية لتدريب شبكة عصبية التفافية كبيرة. الحل التقليدي لهذه المشكلة هو استخدام التدريب المسبق غير الموجّه، يليه الضبط الدقيق الموجّه (على سبيل المثال، [35]). المساهمة الرئيسية الثانية لهذا البحث هي إظهار أن التدريب المسبق الموجّه على مجموعة بيانات مساعدة كبيرة (ILSVRC)، يليه الضبط الدقيق الخاص بالمجال على مجموعة بيانات صغيرة (PASCAL)، هو نموذج فعال لتعلم الشبكات العصبية الالتفافية عالية السعة عندما تكون البيانات نادرة. في تجاربنا، يحسّن الضبط الدقيق للكشف أداء mAP بمقدار 8 نقاط مئوية. بعد الضبط الدقيق، يحقق نظامنا mAP بنسبة 54% على VOC 2010 مقارنة بـ 33% لنموذج الأجزاء القابلة للتشويه (DPM) [17، 20] المضبوط بعناية والقائم على HOG. نوجه القراء أيضاً إلى العمل المتزامن لـ Donahue وآخرون [12]، الذين يُظهرون أن شبكة Krizhevsky العصبية الالتفافية يمكن استخدامها (بدون ضبط دقيق) كمستخرج ميزات صندوق أسود، مما يحقق أداءً ممتازاً في عدة مهام تعرف بما في ذلك تصنيف المشهد، والتصنيف الفرعي الدقيق، والتكيف مع المجال.

نظامنا أيضاً فعال للغاية. الحسابات الخاصة بالفئة الوحيدة هي ضرب مصفوفة-متجه صغير نسبياً وقمع عدم الحد الأقصى الجشع. تنبع هذه الخاصية الحسابية من الميزات المشتركة عبر جميع الفئات والتي هي أيضاً أقل بمقدار رتبتين من حيث الأبعاد من ميزات المناطق المستخدمة سابقاً (راجع [39]).

فهم أوضاع الفشل في نهجنا أمر بالغ الأهمية أيضاً لتحسينه، ولذلك نبلغ عن النتائج من أداة تحليل الكشف لـ Hoiem وآخرون [23]. كنتيجة مباشرة لهذا التحليل، نُظهر أن طريقة انحدار صندوق التحديد البسيطة تقلل بشكل كبير من الأخطاء في تحديد الموقع، وهو وضع الخطأ المهيمن.

قبل تطوير التفاصيل التقنية، نلاحظ أنه نظراً لأن R-CNN يعمل على المناطق، فمن الطبيعي توسيعه إلى مهمة التقسيم الدلالي. مع تعديلات طفيفة، نحقق أيضاً نتائج منافسة على مهمة تقسيم PASCAL VOC، مع دقة تقسيم متوسطة تبلغ 47.9% على مجموعة اختبار VOC 2011.

---

### Translation Notes

- **Figures referenced:** Figure 1 (system overview)
- **Key terms introduced:** SIFT, HOG, neocognitron, receptive fields, region proposals, affine image warping, sliding-window detector, OverFeat, DPM (deformable part model), non-maximum suppression
- **Equations:** None
- **Citations:** [7], [15], [19], [21], [23], [25], [26], [27], [29], [32], [33], [34], [35], [38], [39], [40]
- **Special handling:**
  - Preserved technical acronyms: SIFT, HOG, CNN, PASCAL VOC, ILSVRC, DPM, SVM
  - Kept mathematical notation: max(x,0), ≈195×195, ≈32×32
  - Maintained all citation numbers
  - Translated proper names kept in English: Fukushima, Rumelhart, LeCun, Krizhevsky, ImageNet, OverFeat

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
