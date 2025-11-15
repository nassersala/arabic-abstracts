# Section 6: Results
## القسم 6: النتائج

**Section:** results
**Translation Quality:** 0.90
**Glossary Terms Used:** neural network, training, dataset, classification, accuracy, error rate

---

### English Version

Our results on ILSVRC-2010 are summarized in Table 1. Our network achieves top-1 and top-5 test set error rates of 37.5% and 17.0%. The best performance achieved during the ILSVRC-2010 competition was 47.1% and 28.2% with an approach that averages the predictions produced from six sparse-coding models trained on different features [2], and since then the best published results are 45.7% and 25.7% with an approach that averages the predictions of two classifiers trained on Fisher Vectors (FVs) computed from two types of densely-sampled features [24].

#### 6.1 Qualitative Evaluations

Figure 3 shows the convolutional kernels learned by the network's two data-connected layers. The network has learned a variety of frequency- and orientation-selective kernels, as well as various colored blobs. Notice the specialization exhibited by the two GPUs, a result of the restricted connectivity described in Section 3.5. The kernels on GPU 1 are largely color-agnostic, while the kernels on GPU 2 are largely color-specific. This kind of specialization occurs during every run and is independent of any particular random weight initialization (modulo a renumbering of the GPUs).

In the left panel of Figure 4 we qualitatively assess what the network has learned by computing its top-5 predictions on eight test images. Notice that even off-center objects, such as the mite in the top-left, can be recognized by the net. Most of the top-5 labels appear reasonable. For example, only other types of cat are considered plausible labels for the leopard. In some cases (grille, cherry) there is genuine ambiguity about the intended focus of the photograph.

Another way to probe the network's visual knowledge is to consider the feature activations induced by an image at the last, 4096-dimensional hidden layer. If two images produce feature activation vectors with a small Euclidean separation, we can say that the higher levels of the neural network consider them to be similar. Figure 4 shows five images from the test set and the six images from the training set that produce feature vectors in this last hidden layer with the smallest Euclidean distance from the feature vector for the test image. Notice that at the pixel level, the retrieved training images are generally not close in L2 to the query images in the first column. For example, the retrieved dogs and elephants appear in a variety of poses. We present the results for many more test images in the supplementary material.

Computing similarity by using Euclidean distance between two 4096-dimensional, real-valued vectors is inefficient, but it could be made efficient by training an auto-encoder to compress these vectors to short binary codes. This should produce a much better image retrieval method than applying auto-encoders to the raw pixels [14], which does not make use of image labels and hence has a tendency to retrieve images with similar patterns of edges, whether or not they are semantically similar.

#### 6.2 Quantitative Results

Table 1 shows our results compared with the best methods on ILSVRC-2010. Our network achieves state-of-the-art results. We also entered our model in the ILSVRC-2012 competition and report our results in Table 2. Since the ILSVRC-2012 test set labels are not publicly available, we cannot report test error rates for all the models that we tried. In the remainder of this paragraph, we use validation and test error rates interchangeably because in our experience they do not differ by more than 0.1% (see Table 2). The CNN described in this paper achieves a top-5 error rate of 18.2%. Averaging the predictions of five similar CNNs gives an error rate of 16.4%. Training one CNN, with an extra sixth convolutional layer over the last pooling layer, to classify the entire ImageNet Fall 2011 release (15M images, 22K categories), and then "fine-tuning" it on ILSVRC-2012 gives an error rate of 16.6%. Averaging the predictions of two CNNs that were pre-trained on the entire Fall 2011 release with the aforementioned five CNNs gives an error rate of 15.3%. The second-best contest entry achieved an error rate of 26.2% with an approach that averages the predictions of several classifiers trained on FVs computed from different types of densely sampled features [7].

Finally, we also report our error rates on the Fall 2009 version of ImageNet with 10,184 categories and 8.9 million images. On this dataset we follow the convention in the literature of using half of the images for training and half for testing. Since there is no established test set, our split necessarily differs from the splits used by previous authors, but this does not affect the results appreciably. Our top-1 and top-5 error rates on this dataset are 67.4% and 40.9%, attained by the net described above but with an additional, sixth convolutional layer over the last pooling layer. The best published results on this dataset are 78.1% and 60.9% [19].

---

### النسخة العربية

يتم تلخيص نتائجنا على ILSVRC-2010 في الجدول 1. تحقق شبكتنا معدلات خطأ في مجموعة الاختبار top-1 وtop-5 بنسبة 37.5% و17.0%. كان أفضل أداء تم تحقيقه خلال مسابقة ILSVRC-2010 هو 47.1% و28.2% باستخدام نهج يحسب متوسط التنبؤات الناتجة من ستة نماذج ترميز متفرق (sparse-coding) مدربة على ميزات مختلفة [2]، ومنذ ذلك الحين فإن أفضل النتائج المنشورة هي 45.7% و25.7% باستخدام نهج يحسب متوسط تنبؤات اثنين من المصنفات المدربة على متجهات فيشر (Fisher Vectors - FVs) المحسوبة من نوعين من الميزات المأخوذة بكثافة [24].

#### 6.1 التقييمات النوعية

يوضح الشكل 3 النوى الالتفافية التي تعلمتها طبقتا الشبكة المتصلتان بالبيانات. تعلمت الشبكة مجموعة متنوعة من النوى الانتقائية للتردد والاتجاه، بالإضافة إلى بقع ملونة مختلفة. لاحظ التخصص الذي تظهره وحدتا معالجة الرسومات، نتيجة للاتصال المقيد الموصوف في القسم 3.5. النوى على وحدة معالجة الرسومات 1 خالية من اللون إلى حد كبير، بينما النوى على وحدة معالجة الرسومات 2 خاصة باللون إلى حد كبير. يحدث هذا النوع من التخصص في كل تشغيل ويكون مستقلاً عن أي تهيئة عشوائية معينة للأوزان (باستثناء إعادة ترقيم وحدات معالجة الرسومات).

في اللوحة اليسرى من الشكل 4 نقيم نوعياً ما تعلمته الشبكة من خلال حساب أعلى 5 تنبؤات لها على ثماني صور اختبار. لاحظ أنه حتى الأشياء خارج المركز، مثل العثة في الأعلى اليسار، يمكن للشبكة التعرف عليها. تبدو معظم تسميات top-5 معقولة. على سبيل المثال، فقط أنواع أخرى من القطط تعتبر تسميات محتملة للفهد. في بعض الحالات (الشبكة، الكرز) يوجد غموض حقيقي حول التركيز المقصود للصورة.

طريقة أخرى لفحص المعرفة البصرية للشبكة هي النظر في تنشيطات الميزات الناتجة عن صورة في الطبقة المخفية الأخيرة ذات 4096 بُعداً. إذا أنتجت صورتان متجهي تنشيط ميزات بمسافة إقليدية صغيرة، يمكننا القول إن المستويات الأعلى من الشبكة العصبية تعتبرهما متشابهتين. يوضح الشكل 4 خمس صور من مجموعة الاختبار والست صور من مجموعة التدريب التي تنتج متجهات ميزات في هذه الطبقة المخفية الأخيرة بأصغر مسافة إقليدية من متجه الميزة لصورة الاختبار. لاحظ أنه على مستوى البكسل، صور التدريب المسترجعة بشكل عام ليست قريبة في L2 من صور الاستعلام في العمود الأول. على سبيل المثال، تظهر الكلاب والفيلة المسترجعة في مجموعة متنوعة من الأوضاع. نقدم النتائج للعديد من صور الاختبار الأخرى في المواد التكميلية.

حساب التشابه باستخدام المسافة الإقليدية بين متجهين ذوي 4096 بُعداً بقيم حقيقية غير فعال، لكن يمكن جعله فعالاً عن طريق تدريب مشفر تلقائي (auto-encoder) لضغط هذه المتجهات إلى أكواد ثنائية قصيرة. يجب أن ينتج هذا طريقة استرجاع صور أفضل بكثير من تطبيق المشفرات التلقائية على البكسلات الخام [14]، والتي لا تستخدم تسميات الصور وبالتالي لديها ميل لاسترجاع الصور ذات الأنماط المتشابهة من الحواف، سواء كانت متشابهة دلالياً أم لا.

#### 6.2 النتائج الكمية

يوضح الجدول 1 نتائجنا مقارنة بأفضل الطرق على ILSVRC-2010. تحقق شبكتنا نتائج متقدمة على مستوى الفن. شاركنا أيضاً بنموذجنا في مسابقة ILSVRC-2012 ونقدم نتائجنا في الجدول 2. نظراً لأن تسميات مجموعة اختبار ILSVRC-2012 غير متاحة للجمهور، لا يمكننا الإبلاغ عن معدلات خطأ الاختبار لجميع النماذج التي جربناها. في بقية هذه الفقرة، نستخدم معدلات خطأ التحقق والاختبار بشكل متبادل لأنه في خبرتنا لا تختلف بأكثر من 0.1% (انظر الجدول 2). تحقق الشبكة العصبية الالتفافية الموصوفة في هذه الورقة معدل خطأ top-5 بنسبة 18.2%. حساب متوسط تنبؤات خمس شبكات عصبية التفافية مماثلة يعطي معدل خطأ 16.4%. تدريب شبكة عصبية التفافية واحدة، مع طبقة التفافية سادسة إضافية فوق طبقة التجميع الأخيرة، لتصنيف إصدار ImageNet Fall 2011 بالكامل (15 مليون صورة، 22 ألف فئة)، ثم "الضبط الدقيق" لها على ILSVRC-2012 يعطي معدل خطأ 16.6%. حساب متوسط تنبؤات شبكتين عصبيتين التفافيتين تم تدريبهما مسبقاً على إصدار Fall 2011 بالكامل مع الشبكات العصبية الالتفافية الخمس المذكورة سابقاً يعطي معدل خطأ 15.3%. حقق صاحب المركز الثاني في المسابقة معدل خطأ 26.2% باستخدام نهج يحسب متوسط تنبؤات عدة مصنفات مدربة على متجهات فيشر المحسوبة من أنواع مختلفة من الميزات المأخوذة بكثافة [7].

أخيراً، نبلغ أيضاً عن معدلات الخطأ لدينا على نسخة Fall 2009 من ImageNet مع 10,184 فئة و8.9 مليون صورة. على مجموعة البيانات هذه نتبع الاتفاقية في الأدبيات باستخدام نصف الصور للتدريب ونصفها للاختبار. نظراً لعدم وجود مجموعة اختبار محددة، فإن تقسيمنا يختلف بالضرورة عن التقسيمات المستخدمة من قبل المؤلفين السابقين، ولكن هذا لا يؤثر على النتائج بشكل ملموس. معدلات الخطأ top-1 وtop-5 لدينا على مجموعة البيانات هذه هي 67.4% و40.9%، التي حققتها الشبكة الموصوفة أعلاه ولكن مع طبقة التفافية سادسة إضافية فوق طبقة التجميع الأخيرة. أفضل النتائج المنشورة على مجموعة البيانات هذه هي 78.1% و60.9% [19].

---

### Translation Notes

- **Figures referenced:** Figure 3, Figure 4
- **Tables referenced:** Table 1, Table 2
- **Key terms introduced:**
  - test set (مجموعة الاختبار)
  - sparse-coding models (نماذج ترميز متفرق)
  - Fisher Vectors (متجهات فيشر)
  - densely-sampled features (الميزات المأخوذة بكثافة)
  - qualitative evaluations (التقييمات النوعية)
  - quantitative results (النتائج الكمية)
  - convolutional kernels (النوى الالتفافية)
  - frequency-selective (الانتقائية للتردد)
  - orientation-selective (الانتقائية للاتجاه)
  - colored blobs (بقع ملونة)
  - specialization (التخصص)
  - color-agnostic (خالية من اللون)
  - color-specific (خاصة باللون)
  - off-center objects (الأشياء خارج المركز)
  - feature activations (تنشيطات الميزات)
  - 4096-dimensional (ذات 4096 بُعداً)
  - hidden layer (الطبقة المخفية)
  - Euclidean separation/distance (مسافة إقليدية)
  - pixel level (مستوى البكسل)
  - L2 distance (مسافة L2)
  - query images (صور الاستعلام)
  - auto-encoder (مشفر تلقائي)
  - binary codes (أكواد ثنائية)
  - image retrieval (استرجاع صور)
  - raw pixels (البكسلات الخام)
  - semantically similar (متشابهة دلالياً)
  - state-of-the-art (متقدمة على مستوى الفن)
  - validation error (خطأ التحقق)
  - fine-tuning (الضبط الدقيق)
  - pre-trained (مدربة مسبقاً)
- **Equations:** None
- **Citations:** [2], [7], [14], [19], [24]
- **Special handling:**
  - Competition names (ILSVRC-2010, ILSVRC-2012) kept in English
  - Dataset names (ImageNet Fall 2011, Fall 2009) kept in English
  - Table and Figure references maintained
  - Numerical data preserved exactly
  - Error rates and percentages preserved
  - Dimensional information preserved (4096-dimensional)
  - Technical acronyms explained (FVs = Fisher Vectors)

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.93
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.90

### Back-Translation Check

Results summary back-translated:
Arabic: "تحقق شبكتنا معدلات خطأ في مجموعة الاختبار top-1 وtop-5 بنسبة 37.5% و17.0%"
Back to English: "Our network achieves test set error rates for top-1 and top-5 of 37.5% and 17.0%"
✓ Semantic match confirmed

Feature similarity description back-translated:
Arabic: "إذا أنتجت صورتان متجهي تنشيط ميزات بمسافة إقليدية صغيرة، يمكننا القول إن المستويات الأعلى من الشبكة العصبية تعتبرهما متشابهتين"
Back to English: "If two images produce feature activation vectors with a small Euclidean distance, we can say that the higher levels of the neural network consider them to be similar"
✓ Semantic match confirmed
