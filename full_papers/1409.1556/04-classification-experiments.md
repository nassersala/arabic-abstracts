# Section 4: Classification Experiments
## القسم 4: تجارب التصنيف

**Section:** experiments/results
**Translation Quality:** 0.87
**Glossary Terms Used:** dataset, validation, classification, error, top-1, top-5, ILSVRC, accuracy, depth, scale jittering, multi-scale evaluation, multi-crop evaluation, ensemble, fusion, state-of-the-art, GoogLeNet

---

### English Version

**Dataset.** In this section, we present the image classification results achieved by the described ConvNet architectures on the ILSVRC-2012 dataset (which was used for ILSVRC 2012–2014 challenges). The dataset includes images of 1000 classes, and is split into three sets: training (1.3M images), validation (50K images), and testing (100K images with held-out class labels). The classification performance is evaluated using two measures: the top-1 and top-5 error. The former is a multi-class classification error, i.e. the proportion of incorrectly classified images; the latter is the main evaluation criterion used in ILSVRC, and is computed as the proportion of images such that the ground-truth category is outside the top-5 predicted categories.

For the majority of experiments, we used the validation set as the test set. Certain experiments were also carried out on the test set and submitted to the official ILSVRC server as a "VGG" team entry to the ILSVRC-2014 competition (Russakovsky et al., 2014).

**4.1 SINGLE SCALE EVALUATION**

We begin with evaluating the performance of individual ConvNet models at a single scale with the layer configurations described in Sect. 2.2. The test image size was set as follows: Q = S for fixed S, and Q = 0.5(Sₘᵢₙ + Sₘₐₓ) for jittered S ∈ [Sₘᵢₙ, Sₘₐₓ]. The results are shown in Table 3.

First, we note that using local response normalisation (A-LRN network) does not improve on the model A without any normalisation layers. We thus do not employ normalisation in the deeper architectures (B–E).

Second, we observe that the classification error decreases with the increased ConvNet depth: from 11 layers in A to 19 layers in E. Notably, in spite of the same depth, the configuration C (which contains three 1 × 1 conv. layers), performs worse than the configuration D, which uses 3 × 3 conv. layers throughout the network. This indicates that while the additional non-linearity does help (C is better than B), it is also important to capture spatial context by using conv. filters with non-trivial receptive fields (D is better than C). The error rate of our architecture saturates when the depth reaches 19 layers, but even deeper models might be beneficial for larger datasets. We also compared the net B with a shallow net with five 5 × 5 conv. layers, which was derived from B by replacing each pair of 3 × 3 conv. layers with a single 5 × 5 conv. layer (which has the same receptive field as explained in Sect. 2.3). The top-1 error of the shallow net was measured to be 7% higher than that of B (on a center crop), which confirms that a deep net with small filters outperforms a shallow net with larger filters.

Finally, scale jittering at training time (S ∈ [256; 512]) leads to significantly better results than training on images with fixed smallest side (S = 256 or S = 384), even though a single scale is used at test time. This confirms that training set augmentation by scale jittering is indeed helpful for capturing multi-scale image statistics.

**4.2 MULTI-SCALE EVALUATION**

Having evaluated the ConvNet models at a single scale, we now assess the effect of scale jittering at test time. It consists of running a model over several rescaled versions of a test image (corresponding to different values of Q), followed by averaging the resulting class posteriors. Considering that a large discrepancy between training and testing scales leads to a drop in performance, the models trained with fixed S were evaluated over three test image sizes, close to the training one: Q = {S − 32, S, S + 32}. At the same time, scale jittering at training time allows the network to be applied to a wider range of scales at test time, so the model trained with variable S ∈ [Sₘᵢₙ; Sₘₐₓ] was evaluated over a larger range of sizes Q = {Sₘᵢₙ, 0.5(Sₘᵢₙ + Sₘₐₓ), Sₘₐₓ}.

The results, presented in Table 4, indicate that scale jittering at test time leads to better performance (as compared to evaluating the same model at a single scale, shown in Table 3). As before, the deepest configurations (D and E) perform the best, and scale jittering is better than training with a fixed smallest side S. Our best single-network performance on the validation set is 24.8%/7.5% top-1/top-5 error (highlighted in bold in Table 4). On the test set, the configuration E achieves 7.3% top-5 error.

**4.3 MULTI-CROP EVALUATION**

In Table 5 we compare dense ConvNet evaluation with multi-crop evaluation (see Sect. 3.2 for details). We also assess the complementarity of the two evaluation techniques by averaging their soft-max outputs. As can be seen, using multiple crops performs slightly better than dense evaluation, and the two approaches are indeed complementary, as their combination outperforms each of them. As noted above, we hypothesize that this is due to a different treatment of convolution boundary conditions.

**4.4 CONVNET FUSION**

Up until now, we evaluated the performance of individual ConvNet models. In this part of the experiments, we combine the outputs of several models by averaging their soft-max class posteriors. This improves the performance due to complementarity of the models, and was used in the top ILSVRC submissions in 2012 (Krizhevsky et al., 2012) and 2013 (Zeiler & Fergus, 2013; Sermanet et al., 2014).

The results are shown in Table 6. By the time of ILSVRC submission we had only trained the single-scale networks, as well as a multi-scale model D (by fine-tuning only the fully-connected layers rather than all layers). The resulting ensemble of 7 networks has 7.3% ILSVRC test error. After the submission, we considered an ensemble of only two best-performing multi-scale models (configurations D and E), which reduced the test error to 7.0% using dense evaluation and 6.8% using combined dense and multi-crop evaluation. For reference, our best-performing single model achieves 7.1% error (model E, Table 5).

**4.5 COMPARISON WITH THE STATE OF THE ART**

Finally, we compare our results with the state of the art in Table 7. In the classification task of ILSVRC-2014 challenge (Russakovsky et al., 2014), our "VGG" team secured the 2nd place with 7.3% test error using an ensemble of 7 models. After the submission, we decreased the error rate to 6.8% using an ensemble of 2 models.

As can be seen from Table 7, our very deep ConvNets significantly outperform the previous generation of models, which achieved the best results in the ILSVRC-2012 and ILSVRC-2013 competitions. Our result is also competitive with respect to the classification task winner (GoogLeNet with 6.7% error) and substantially outperforms the ILSVRC-2013 winning submission Clarifai, which achieved 11.2% with outside training data and 11.7% without it. This is remarkable, considering that our best result is achieved by combining just two models – significantly less than used in most ILSVRC submissions. In terms of the single-net performance, our architecture achieves the best result (7.0% test error), outperforming a single GoogLeNet by 0.9%. Notably, we did not depart from the classical ConvNet architecture of LeCun et al. (1989), but improved it by substantially increasing the depth.

---

### النسخة العربية

**مجموعة البيانات.** في هذا القسم، نعرض نتائج تصنيف الصور التي حققتها معماريات الشبكة الالتفافية الموصوفة على مجموعة بيانات ILSVRC-2012 (التي تم استخدامها لتحديات ILSVRC 2012-2014). تتضمن مجموعة البيانات صوراً من 1000 صنف، وتنقسم إلى ثلاث مجموعات: التدريب (1.3 مليون صورة)، والتحقق (50 ألف صورة)، والاختبار (100 ألف صورة مع تسميات أصناف محتفظ بها). يتم تقييم أداء التصنيف باستخدام مقياسين: خطأ top-1 وخطأ top-5. الأول هو خطأ تصنيف متعدد الأصناف، أي نسبة الصور المصنفة بشكل غير صحيح؛ والأخير هو معيار التقييم الرئيسي المستخدم في ILSVRC، ويُحسب كنسبة الصور بحيث يكون الصنف الحقيقي خارج الأصناف الخمسة المتوقعة الأولى.

بالنسبة لغالبية التجارب، استخدمنا مجموعة التحقق كمجموعة اختبار. تم أيضاً إجراء تجارب معينة على مجموعة الاختبار وإرسالها إلى خادم ILSVRC الرسمي كمشاركة فريق "VGG" في مسابقة ILSVRC-2014 (Russakovsky et al., 2014).

**4.1 تقييم المقياس الواحد**

نبدأ بتقييم أداء نماذج الشبكة الالتفافية الفردية على مقياس واحد مع تكوينات الطبقات الموصوفة في القسم 2.2. تم تعيين حجم صورة الاختبار على النحو التالي: Q = S لـ S الثابت، و Q = 0.5(Sₘᵢₙ + Sₘₐₓ) لـ S المهتز ∈ [Sₘᵢₙ, Sₘₐₓ]. يتم عرض النتائج في الجدول 3.

أولاً، نلاحظ أن استخدام تطبيع الاستجابة المحلية (شبكة A-LRN) لا يحسن من النموذج A بدون أي طبقات تطبيع. وبالتالي لا نستخدم التطبيع في المعماريات الأعمق (B-E).

ثانياً، نلاحظ أن خطأ التصنيف ينخفض مع زيادة عمق الشبكة الالتفافية: من 11 طبقة في A إلى 19 طبقة في E. والجدير بالذكر أنه على الرغم من نفس العمق، فإن التكوين C (الذي يحتوي على ثلاث طبقات conv. بحجم 1 × 1)، يؤدي أداءً أسوأ من التكوين D، الذي يستخدم طبقات conv. بحجم 3 × 3 في جميع أنحاء الشبكة. يشير هذا إلى أنه بينما تساعد اللاخطية الإضافية (C أفضل من B)، فإنه من المهم أيضاً التقاط السياق المكاني باستخدام مرشحات conv. ذات مجالات استقبال غير تافهة (D أفضل من C). يتشبع معدل الخطأ لمعماريتنا عندما يصل العمق إلى 19 طبقة، لكن النماذج الأعمق قد تكون مفيدة لمجموعات البيانات الأكبر. قارنا أيضاً الشبكة B بشبكة سطحية ذات خمس طبقات conv. بحجم 5 × 5، والتي تم اشتقاقها من B عن طريق استبدال كل زوج من طبقات conv. بحجم 3 × 3 بطبقة conv. واحدة بحجم 5 × 5 (التي لها نفس مجال الاستقبال كما هو موضح في القسم 2.3). تم قياس خطأ top-1 للشبكة السطحية بأنه أعلى بنسبة 7٪ من خطأ B (على محصول مركزي)، مما يؤكد أن الشبكة العميقة ذات المرشحات الصغيرة تتفوق على الشبكة السطحية ذات المرشحات الأكبر.

أخيراً، يؤدي اهتزاز المقياس في وقت التدريب (S ∈ [256; 512]) إلى نتائج أفضل بكثير من التدريب على صور ذات جانب أصغر ثابت (S = 256 أو S = 384)، على الرغم من استخدام مقياس واحد في وقت الاختبار. يؤكد هذا أن زيادة مجموعة التدريب عن طريق اهتزاز المقياس مفيدة بالفعل لالتقاط إحصائيات الصور متعددة المقاييس.

**4.2 تقييم متعدد المقاييس**

بعد تقييم نماذج الشبكة الالتفافية على مقياس واحد، نقوم الآن بتقييم تأثير اهتزاز المقياس في وقت الاختبار. يتكون من تشغيل نموذج على عدة إصدارات معاد قياسها من صورة الاختبار (المقابلة لقيم مختلفة من Q)، متبوعاً بحساب متوسط توزيعات الأصناف الخلفية الناتجة. بالنظر إلى أن التباين الكبير بين مقاييس التدريب والاختبار يؤدي إلى انخفاض في الأداء، تم تقييم النماذج المدربة بـ S الثابت على ثلاثة أحجام صور اختبار، قريبة من حجم التدريب: Q = {S − 32, S, S + 32}. في الوقت نفسه، يسمح اهتزاز المقياس في وقت التدريب بتطبيق الشبكة على نطاق أوسع من المقاييس في وقت الاختبار، لذلك تم تقييم النموذج المدرب بـ S المتغير ∈ [Sₘᵢₙ; Sₘₐₓ] على نطاق أكبر من الأحجام Q = {Sₘᵢₙ, 0.5(Sₘᵢₙ + Sₘₐₓ), Sₘₐₓ}.

تشير النتائج، المعروضة في الجدول 4، إلى أن اهتزاز المقياس في وقت الاختبار يؤدي إلى أداء أفضل (مقارنة بتقييم نفس النموذج على مقياس واحد، المعروض في الجدول 3). كما كان من قبل، فإن التكوينات الأعمق (D و E) تؤدي الأفضل، واهتزاز المقياس أفضل من التدريب بجانب أصغر ثابت S. أفضل أداء لشبكة واحدة لدينا على مجموعة التحقق هو 24.8٪/7.5٪ خطأ top-1/top-5 (مميز بالخط الغامق في الجدول 4). على مجموعة الاختبار، يحقق التكوين E خطأ top-5 بنسبة 7.3٪.

**4.3 تقييم المحاصيل المتعددة**

في الجدول 5 نقارن تقييم الشبكة الالتفافية الكثيفة بتقييم المحاصيل المتعددة (انظر القسم 3.2 للحصول على التفاصيل). نقيّم أيضاً تكامل تقنيتي التقييم عن طريق حساب متوسط مخرجات soft-max الخاصة بهما. كما يمكن رؤيته، فإن استخدام محاصيل متعددة يؤدي أداءً أفضل قليلاً من التقييم الكثيف، وأن النهجين متكاملان بالفعل، حيث أن مزيجهما يتفوق على كل منهما. كما لوحظ أعلاه، نفترض أن هذا يرجع إلى معالجة مختلفة لشروط حدود الالتفاف.

**4.4 دمج الشبكات الالتفافية**

حتى الآن، قيّمنا أداء نماذج الشبكة الالتفافية الفردية. في هذا الجزء من التجارب، نجمع مخرجات عدة نماذج من خلال حساب متوسط توزيعات أصناف soft-max الخاصة بها. يحسن هذا من الأداء بسبب تكامل النماذج، وتم استخدامه في أفضل مشاركات ILSVRC في عامي 2012 (Krizhevsky et al., 2012) و 2013 (Zeiler & Fergus, 2013; Sermanet et al., 2014).

يتم عرض النتائج في الجدول 6. بحلول وقت إرسال ILSVRC، كنا قد دربنا فقط الشبكات أحادية المقياس، بالإضافة إلى نموذج D متعدد المقاييس (عن طريق الضبط الدقيق للطبقات المتصلة بالكامل فقط بدلاً من جميع الطبقات). مجموعة الـ 7 شبكات الناتجة لها خطأ اختبار ILSVRC بنسبة 7.3٪. بعد التقديم، نظرنا في مجموعة من أفضل نموذجين متعددي المقاييس فقط (التكوينات D و E)، مما قلل من خطأ الاختبار إلى 7.0٪ باستخدام التقييم الكثيف و 6.8٪ باستخدام التقييم الكثيف والمحاصيل المتعددة المدمجة. للمرجعية، فإن أفضل نموذج فردي لدينا يحقق خطأ 7.1٪ (النموذج E، الجدول 5).

**4.5 المقارنة مع أحدث ما توصلت إليه التقنية**

أخيراً، نقارن نتائجنا مع أحدث ما توصلت إليه التقنية في الجدول 7. في مهمة التصنيف لتحدي ILSVRC-2014 (Russakovsky et al., 2014)، حصل فريق "VGG" الخاص بنا على المركز الثاني بخطأ اختبار 7.3٪ باستخدام مجموعة من 7 نماذج. بعد التقديم، قللنا معدل الخطأ إلى 6.8٪ باستخدام مجموعة من نموذجين.

كما يمكن ملاحظته من الجدول 7، فإن شبكاتنا الالتفافية العميقة جداً تتفوق بشكل كبير على الجيل السابق من النماذج، التي حققت أفضل النتائج في مسابقات ILSVRC-2012 و ILSVRC-2013. نتيجتنا أيضاً تنافسية فيما يتعلق بالفائز بمهمة التصنيف (GoogLeNet بخطأ 6.7٪) وتتفوق بشكل كبير على المشاركة الفائزة في ILSVRC-2013 وهي Clarifai، والتي حققت 11.2٪ ببيانات تدريب خارجية و 11.7٪ بدونها. هذا ملحوظ، بالنظر إلى أن أفضل نتيجة لدينا تم تحقيقها من خلال الجمع بين نموذجين فقط - أقل بكثير مما تم استخدامه في معظم مشاركات ILSVRC. من حيث أداء الشبكة الواحدة، تحقق معماريتنا أفضل نتيجة (خطأ اختبار 7.0٪)، متفوقة على GoogLeNet واحدة بنسبة 0.9٪. والجدير بالذكر أننا لم نبتعد عن المعمارية الكلاسيكية للشبكة الالتفافية لـ LeCun et al. (1989)، ولكن حسّناها من خلال زيادة العمق بشكل كبير.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** ILSVRC-2012 dataset, training set, validation set, test set, top-1 error, top-5 error, ground-truth category, single scale evaluation, multi-scale evaluation, multi-crop evaluation, dense evaluation, ensemble, model fusion, scale jittering, state-of-the-art, GoogLeNet, Clarifai
- **Equations:** Mathematical expressions for test scale Q and error rates
- **Citations:** Multiple references to ILSVRC competitions, Krizhevsky, Zeiler & Fergus, Sermanet, Russakovsky, Szegedy (GoogLeNet), LeCun
- **Special handling:** Preserved all Table references (Tables 3-7); maintained percentage values and error rates; kept comparison metrics intact

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
