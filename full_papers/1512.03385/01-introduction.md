# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** deep convolutional neural networks, image classification, depth, network depth, degradation problem, residual learning, shortcut connections, vanishing/exploding gradients, normalization, identity mapping, optimization

---

### English Version

Deep convolutional neural networks [22, 21] have led to a series of breakthroughs for image classification [21, 50, 40]. Deep networks naturally integrate low/mid/high-level features [50] and classifiers in an end-to-end multi-layer fashion, and the "levels" of features can be enriched by the number of stacked layers (depth). Recent evidence [41, 44] reveals that network depth is of crucial importance, and the leading results [41, 44, 13, 16] on the challenging ImageNet dataset [36] all exploit "very deep" [41] models, with a depth of sixteen [41] to thirty [16] layers. Many other non-trivial visual recognition tasks [8, 12, 7, 32, 27] have also greatly benefited from very deep models.

Driven by the significance of depth, a question arises: Is learning better networks as easy as stacking more layers? An obstacle to answering this question was the notorious problem of vanishing/exploding gradients [1, 9], which hamper convergence from the beginning. This problem, however, has been largely addressed by normalized initialization [23, 9, 37, 13] and intermediate normalization layers [16], which enable networks with tens of layers to start converging for stochastic gradient descent (SGD) with backpropagation [22].

When deeper networks are able to start converging, a degradation problem has been exposed: with the network depth increasing, accuracy gets saturated (which might be unsurprising) and then degrades rapidly. Unexpectedly, such degradation is not caused by overfitting, and adding more layers to a suitably deep model leads to higher training error, as reported in [11, 42] and thoroughly verified by our experiments. Fig. 1 shows a typical example.

The degradation (of training accuracy) indicates that not all systems are similarly easy to optimize. Let us consider a shallower architecture and its deeper counterpart that adds more layers onto it. There exists a solution by construction to the deeper model: the added layers are identity mapping, and the other layers are copied from the learned shallower model. The existence of this constructed solution indicates that a deeper model should produce no higher training error than its shallower counterpart. But experiments show that our current solvers on hand are unable to find solutions that are comparably good or better than the constructed solution (or unable to do so in feasible time).

In this paper, we address the degradation problem by introducing a deep residual learning framework. Instead of hoping each few stacked layers directly fit a desired underlying mapping, we explicitly let these layers fit a residual mapping. Formally, denoting the desired underlying mapping as H(x), we let the stacked nonlinear layers fit another mapping of F(x) := H(x)−x. The original mapping is recast into F(x)+x. We hypothesize that it is easier to optimize the residual mapping than to optimize the original, unreferenced mapping. To the extreme, if an identity mapping were optimal, it would be easier to push the residual to zero than to fit an identity mapping by a stack of nonlinear layers.

The formulation of F(x) +x can be realized by feedforward neural networks with "shortcut connections" (Fig. 2). Shortcut connections [2, 34, 49] are those skipping one or more layers. In our case, the shortcut connections simply perform identity mapping, and their outputs are added to the outputs of the stacked layers (Fig. 2). Identity shortcut connections add neither extra parameter nor computational complexity. The entire network can still be trained end-to-end by SGD with backpropagation, and can be easily implemented using common libraries (e.g., Caffe [19]) without modifying the solvers.

We present comprehensive experiments on ImageNet [36] to show the degradation problem and evaluate our method. We show that: 1) Our extremely deep residual nets are easy to optimize, but the counterpart "plain" nets (that simply stack layers) exhibit higher training error when the depth increases; 2) Our deep residual nets can easily enjoy accuracy gains from greatly increased depth, producing results substantially better than previous networks.

Similar phenomena are also shown on the CIFAR-10 set [20], suggesting that the optimization difficulties and the effects of our method are not just akin to a particular dataset. We present successfully trained models on this dataset with over 100 layers, and explore models with over 1000 layers.

On the ImageNet classification dataset [36], we obtain excellent results by extremely deep residual nets. Our 152-layer residual net is the deepest network ever presented on ImageNet, while still having lower complexity than VGG nets [41]. Our ensemble has 3.57% top-5 error on the ImageNet test set, and won the 1st place in the ILSVRC 2015 classification competition. The extremely deep representations also have excellent generalization performance on other recognition tasks, and lead us to further win the 1st places on: ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation in ILSVRC & COCO 2015 competitions. This strong evidence shows that the residual learning principle is generic, and we expect that it is applicable in other vision and non-vision problems.

---

### النسخة العربية

أدت الشبكات العصبية الالتفافية العميقة [22, 21] إلى سلسلة من الاختراقات في مجال تصنيف الصور [21, 50, 40]. تدمج الشبكات العميقة بشكل طبيعي الميزات منخفضة/متوسطة/عالية المستوى [50] والمصنفات بطريقة متعددة الطبقات من البداية إلى النهاية، ويمكن إثراء "مستويات" الميزات من خلال عدد الطبقات المكدسة (العمق). تكشف الأدلة الحديثة [41, 44] أن عمق الشبكة ذو أهمية حاسمة، وجميع النتائج الرائدة [41, 44, 13, 16] على مجموعة بيانات ImageNet الصعبة [36] تستغل نماذج "عميقة جداً" [41]، بعمق يتراوح من ستة عشر [41] إلى ثلاثين طبقة [16]. استفادت أيضاً العديد من مهام التعرف البصري غير البسيطة الأخرى [8, 12, 7, 32, 27] بشكل كبير من النماذج العميقة جداً.

مدفوعين بأهمية العمق، يطرح السؤال التالي: هل تعلم شبكات أفضل سهل مثل تكديس المزيد من الطبقات؟ كانت العقبة في الإجابة على هذا السؤال هي مشكلة تلاشي/انفجار التدرجات السيئة السمعة [1, 9]، التي تعيق التقارب من البداية. ومع ذلك، تمت معالجة هذه المشكلة إلى حد كبير من خلال التهيئة المعيارية [23, 9, 37, 13] وطبقات التطبيع الوسيطة [16]، التي تمكن الشبكات ذات عشرات الطبقات من البدء في التقارب للانحدار التدرجي العشوائي (SGD) مع الانتشار العكسي [22].

عندما أصبحت الشبكات الأعمق قادرة على البدء في التقارب، ظهرت مشكلة التدهور: مع زيادة عمق الشبكة، تصل الدقة إلى حد التشبع (وهو أمر قد لا يكون مفاجئاً) ثم تتدهور بسرعة. بشكل غير متوقع، هذا التدهور ليس ناتجاً عن فرط التلاؤم، وإضافة المزيد من الطبقات إلى نموذج عميق بشكل مناسب يؤدي إلى خطأ تدريب أعلى، كما ورد في [11, 42] وتم التحقق منه بدقة من خلال تجاربنا. يوضح الشكل 1 مثالاً نموذجياً.

يشير التدهور (في دقة التدريب) إلى أن ليست كل الأنظمة سهلة التحسين بالمثل. دعونا ننظر في معمارية أقل عمقاً ونظيرتها الأعمق التي تضيف المزيد من الطبقات عليها. يوجد حل بالبناء للنموذج الأعمق: الطبقات المضافة هي تعيينات هوية، والطبقات الأخرى منسوخة من النموذج الأقل عمقاً الذي تم تعلمه. وجود هذا الحل المبني يشير إلى أن النموذج الأعمق يجب ألا ينتج خطأ تدريب أعلى من نظيره الأقل عمقاً. لكن التجارب تظهر أن المحللات الحالية المتاحة لدينا غير قادرة على إيجاد حلول جيدة بشكل مماثل أو أفضل من الحل المبني (أو غير قادرة على القيام بذلك في وقت معقول).

في هذه الورقة، نعالج مشكلة التدهور من خلال تقديم إطار عمل للتعلم المتبقي العميق. بدلاً من الأمل في أن كل بضع طبقات مكدسة تتلاءم مباشرة مع تعيين أساسي مرغوب، نسمح صراحة لهذه الطبقات بتلاؤم تعيين متبقي. رسمياً، من خلال تعريف التعيين الأساسي المرغوب بـ H(x)، نسمح للطبقات غير الخطية المكدسة بتلاؤم تعيين آخر F(x) := H(x)−x. يتم إعادة صياغة التعيين الأصلي إلى F(x)+x. نفترض أنه من الأسهل تحسين التعيين المتبقي من تحسين التعيين الأصلي غير المرجعي. في الحالة القصوى، إذا كان تعيين الهوية هو الأمثل، فسيكون من الأسهل دفع المتبقي إلى الصفر بدلاً من تلاؤم تعيين هوية بواسطة كومة من الطبقات غير الخطية.

يمكن تحقيق صيغة F(x) +x من خلال الشبكات العصبية ذات التغذية الأمامية مع "اتصالات الاختصار" (الشكل 2). اتصالات الاختصار [2, 34, 49] هي تلك التي تتخطى طبقة واحدة أو أكثر. في حالتنا، تقوم اتصالات الاختصار ببساطة بتعيين الهوية، ويتم إضافة مخرجاتها إلى مخرجات الطبقات المكدسة (الشكل 2). اتصالات اختصار الهوية لا تضيف معاملات إضافية ولا تعقيد حسابي. لا يزال من الممكن تدريب الشبكة بأكملها من البداية إلى النهاية بواسطة SGD مع الانتشار العكسي، ويمكن تنفيذها بسهولة باستخدام المكتبات الشائعة (مثل Caffe [19]) دون تعديل المحللات.

نقدم تجارب شاملة على ImageNet [36] لإظهار مشكلة التدهور وتقييم طريقتنا. نُظهر أن: 1) الشبكات المتبقية العميقة جداً الخاصة بنا سهلة التحسين، لكن الشبكات "البسيطة" النظيرة (التي تكدس الطبقات ببساطة) تظهر خطأ تدريب أعلى عندما يزداد العمق؛ 2) يمكن للشبكات المتبقية العميقة الخاصة بنا أن تستفيد بسهولة من مكاسب الدقة من العمق المتزايد بشكل كبير، منتجة نتائج أفضل بكثير من الشبكات السابقة.

تظهر ظواهر مماثلة أيضاً على مجموعة CIFAR-10 [20]، مما يشير إلى أن صعوبات التحسين وآثار طريقتنا ليست مشابهة فقط لمجموعة بيانات معينة. نقدم نماذج مدربة بنجاح على مجموعة البيانات هذه بأكثر من 100 طبقة، ونستكشف نماذج بأكثر من 1000 طبقة.

على مجموعة بيانات تصنيف ImageNet [36]، نحصل على نتائج ممتازة من خلال الشبكات المتبقية العميقة جداً. شبكتنا المتبقية المكونة من 152 طبقة هي أعمق شبكة تم تقديمها على الإطلاق على ImageNet، بينما لا تزال أقل تعقيداً من شبكات VGG [41]. تحقق مجموعتنا خطأ 3.57% في أفضل 5 على مجموعة اختبار ImageNet، وفازت بالمركز الأول في مسابقة تصنيف ILSVRC 2015. التمثيلات العميقة جداً لديها أيضاً أداء تعميم ممتاز في مهام التعرف الأخرى، وتقودنا للفوز بالمراكز الأولى في: كشف ImageNet، وتوطين ImageNet، وكشف COCO، وتجزئة COCO في مسابقات ILSVRC وCOCO 2015. هذا الدليل القوي يظهر أن مبدأ التعلم المتبقي عام، ونتوقع أنه قابل للتطبيق في مشاكل الرؤية وغير الرؤية الأخرى.

---

### Translation Notes

- **Figures referenced:** Figure 1 (training/test error comparison), Figure 2 (residual learning building block)
- **Key terms introduced:**
  - degradation problem (مشكلة التدهور)
  - residual learning (التعلم المتبقي)
  - residual mapping (التعيين المتبقي)
  - shortcut connections (اتصالات الاختصار)
  - identity mapping (تعيين الهوية)
  - plain networks (الشبكات البسيطة)
  - vanishing/exploding gradients (تلاشي/انفجار التدرجات)
  - overfitting (فرط التلاؤم)
  - stochastic gradient descent (الانحدار التدرجي العشوائي)
  - backpropagation (الانتشار العكسي)
- **Datasets:** ImageNet, CIFAR-10, COCO
- **Competitions:** ILSVRC 2015, COCO 2015
- **Key contributions:**
  1. Identified and addressed the degradation problem
  2. Introduced residual learning framework with shortcut connections
  3. Achieved state-of-the-art results with 152-layer network
  4. Won multiple ILSVRC & COCO 2015 competitions

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
