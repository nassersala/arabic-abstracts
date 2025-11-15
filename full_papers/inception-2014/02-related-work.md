# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional neural network, architecture, max-pooling, fully-connected, dropout, regularization, localization, detection, dimension reduction

---

### English Version

Starting with LeNet-5 [10], convolutional neural networks (CNN) have typically had a standard structure – stacked convolutional layers (optionally followed by contrast normalization and max-pooling) are followed by one or more fully-connected layers. Variations of this basic design are prevalent in the image classification literature and have yielded the best results to-date on MNIST, CIFAR and most notably on the ImageNet classification challenge [9]. For larger datasets, such as ImageNet, the recent trend has been to increase the number of layers [12] and layer size [21, 14], while using dropout [7] for addressing the problem of overfitting.

Despite concerns that max-pooling layers result in loss of accurate spatial information, the same convolutional network architecture as [9] has also been successfully employed for localization [9, 14], object detection [6, 14, 18, 5] and human pose estimation [19]. Inspired by a neuroscience model of the primate visual cortex, Serre et al. [15] use a series of fixed Gabor filters of different sizes in order to handle multiple scales. We use a similar strategy here. However, contrary to the fixed 2-layer deep model of [15], all filters in the Inception architecture are learned. Furthermore, Inception layers are repeated many times, leading to a 22-layer deep model in the case of the GoogLeNet model.

Network-in-Network is an approach proposed by Lin et al. [12] in order to increase the representational power of neural networks. In their model, additional 1 × 1 convolutional layers are added to the network, increasing its depth. We use this approach heavily in our architecture. However, in our setting, 1 × 1 convolutions have dual purpose: most critically, they are used mainly as dimension reduction modules to remove computational bottlenecks, that would otherwise limit the size of our networks. This allows for not just increasing the depth, but also the width of our networks without significant performance penalty.

The current leading approach for object detection is the Regions with Convolutional Neural Networks (R-CNN) proposed by Girshick et al. [6]. R-CNN decomposes the overall detection problem into two subproblems: to first utilize low-level cues such as color and superpixel consistency for potential object proposals in a category-agnostic fashion, and to then use CNN classifiers to identify object categories at those locations. Such a two stage approach leverages the accuracy of bounding box segmentation with low-level cues, as well as the highly powerful classification power of state-of-the-art CNNs. We adopted a similar pipeline in our detection submissions, but have explored enhancements in both stages, such as multi-box [5] prediction for higher object bounding box recall, and ensemble approaches for better categorization of bounding box proposals.

---

### النسخة العربية

بدءاً من LeNet-5 [10]، كانت الشبكات العصبية الالتفافية (CNN) تمتلك عادةً بنية قياسية - طبقات التفافية مكدسة (يتبعها اختيارياً تطبيع التباين والتجميع الأقصى) تليها طبقة واحدة أو أكثر متصلة بالكامل. تنويعات هذا التصميم الأساسي سائدة في أدبيات تصنيف الصور وقد حققت أفضل النتائج حتى الآن على MNIST وCIFAR والأهم من ذلك على تحدي تصنيف ImageNet [9]. بالنسبة لمجموعات البيانات الأكبر، مثل ImageNet، كان الاتجاه الحديث هو زيادة عدد الطبقات [12] وحجم الطبقة [21, 14]، مع استخدام dropout [7] لمعالجة مشكلة الإفراط في التكيف.

على الرغم من المخاوف من أن طبقات التجميع الأقصى تؤدي إلى فقدان معلومات مكانية دقيقة، فقد تم أيضاً استخدام نفس معمارية الشبكة الالتفافية كما في [9] بنجاح للتوطين [9, 14]، والكشف عن الكائنات [6, 14, 18, 5]، وتقدير وضعية الإنسان [19]. مستوحاة من نموذج علم الأعصاب للقشرة البصرية للرئيسيات، يستخدم Serre وآخرون [15] سلسلة من مرشحات Gabor الثابتة بأحجام مختلفة للتعامل مع مقاييس متعددة. نستخدم استراتيجية مماثلة هنا. ومع ذلك، على عكس النموذج الثابت ذو الطبقتين في [15]، يتم تعلم جميع المرشحات في معمارية Inception. علاوة على ذلك، تتكرر طبقات Inception عدة مرات، مما يؤدي إلى نموذج بعمق 22 طبقة في حالة نموذج GoogLeNet.

الشبكة داخل الشبكة (Network-in-Network) هو نهج اقترحه Lin وآخرون [12] لزيادة القوة التمثيلية للشبكات العصبية. في نموذجهم، تُضاف طبقات التفافية إضافية بحجم 1×1 إلى الشبكة، مما يزيد من عمقها. نستخدم هذا النهج بكثافة في معماريتنا. ومع ذلك، في إعدادنا، الالتفافات 1×1 لها غرض مزدوج: والأهم من ذلك، تُستخدم بشكل رئيسي كوحدات لتخفيض الأبعاد لإزالة الاختناقات الحسابية، التي من شأنها أن تحد من حجم شبكاتنا. وهذا يسمح ليس فقط بزيادة العمق، بل أيضاً باتساع شبكاتنا دون عقوبة أداء كبيرة.

النهج الرائد الحالي للكشف عن الكائنات هو المناطق مع الشبكات العصبية الالتفافية (R-CNN) الذي اقترحه Girshick وآخرون [6]. يقوم R-CNN بتحليل مشكلة الكشف الإجمالية إلى مشكلتين فرعيتين: أولاً استخدام الإشارات ذات المستوى المنخفض مثل اللون واتساق الـ superpixel للاقتراحات المحتملة للكائنات بطريقة مستقلة عن الفئة، ثم استخدام مصنفات CNN لتحديد فئات الكائنات في تلك المواقع. مثل هذا النهج ثنائي المرحلة يستفيد من دقة تجزئة صندوق التحديد باستخدام الإشارات ذات المستوى المنخفض، بالإضافة إلى قوة التصنيف القوية جداً لشبكات CNN الحديثة. اعتمدنا خط أنابيب مماثلاً في تقديمات الكشف الخاصة بنا، لكننا استكشفنا تحسينات في كلتا المرحلتين، مثل التنبؤ بـ multi-box [5] لزيادة استدعاء صندوق التحديد للكائنات، ونُهج المجموعات (ensemble) لتصنيف أفضل لمقترحات صندوق التحديد.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** LeNet-5, dropout, overfitting, max-pooling, localization, Gabor filters, Network-in-Network, R-CNN, multi-box, ensemble
- **Equations:** None
- **Citations:** [5], [6], [7], [9], [10], [12], [14], [15], [18], [19], [21]
- **Special handling:**
  - Kept model names in English: LeNet-5, GoogLeNet, R-CNN, MNIST, CIFAR, ImageNet
  - Kept "dropout" as transliteration since it's a standard technical term
  - Translated "overfitting" as "الإفراط في التكيف"
  - Kept "1×1 convolutions" with mathematical notation
  - Kept "multi-box" and "ensemble" as English terms since they're specific technical approaches
  - Translated "superpixel" as "superpixel" (kept in English as it's a standard computer vision term)
  - Translated "fully-connected" as "متصلة بالكامل"

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
