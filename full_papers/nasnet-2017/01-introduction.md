# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** architecture, convolutional, neural architecture search, reinforcement learning, search space, cell, transferability, ImageNet, CIFAR-10, state-of-the-art, accuracy, computational cost, object detection

---

### English Version

Developing neural network image classification models often requires significant _architecture engineering_. Starting from the seminal work of [32] on using convolutional architectures [17, 34] for ImageNet [11] classification, successive advancements through architecture engineering have achieved impressive results [53, 59, 20, 60, 58, 68].

In this paper, we study a new paradigm of designing convolutional architectures and describe a scalable method to optimize convolutional architectures on a dataset of interest, for instance the ImageNet classification dataset. Our approach is inspired by the recently proposed Neural Architecture Search (NAS) framework [71], which uses a reinforcement learning search method to optimize architecture configurations. Applying NAS, or any other search methods, directly to a large dataset, such as the ImageNet dataset, is however computationally expensive. We therefore propose to search for a good architecture on a proxy dataset, for example the smaller CIFAR-10 dataset, and then transfer the learned architecture to ImageNet. We achieve this transferrability by designing a search space (which we call "the NASNet search space") so that the complexity of the architecture is independent of the depth of the network and the size of input images. More concretely, all convolutional networks in our search space are composed of convolutional layers (or "cells") with identical structure but different weights. Searching for the best convolutional architectures is therefore reduced to searching for the best cell structure. Searching for the best cell structure has two main benefits: it is much faster than searching for an entire network architecture and the cell itself is more likely to generalize to other problems. In our experiments, this approach significantly accelerates the search for the best architectures using CIFAR-10 by a factor of 7× and learns architectures that successfully transfer to ImageNet.

Our main result is that the best architecture found on CIFAR-10, called NASNet, achieves state-of-the-art accuracy when transferred to ImageNet classification without much modification. On ImageNet, NASNet achieves, among the published works, state-of-the-art accuracy of 82.7% top-1 and 96.2% top-5. This result amounts to a 1.2% improvement in top-1 accuracy than the best human-invented architectures while having 9 billion fewer FLOPS. On CIFAR-10 itself, NASNet achieves 2.4% error rate, which is also state-of-the-art.

Additionally, by simply varying the number of the convolutional cells and number of filters in the convolutional cells, we can create different versions of NASNets with different computational demands. Thanks to this property of the cells, we can generate a family of models that achieve accuracies superior to all human-invented models at equivalent or smaller computational budgets [60, 29]. Notably, the smallest version of NASNet achieves 74.0% top-1 accuracy on ImageNet, which is 3.1% better than previously engineered architectures targeted towards mobile and embedded vision tasks [24, 70].

Finally, we show that the image features learned by NASNets are generically useful and transfer to other computer vision problems. In our experiments, the features learned by NASNets from ImageNet classification can be combined with the Faster-RCNN framework [47] to achieve state-of-the-art on COCO object detection task for both the largest as well as mobile-optimized models. Our largest NASNet model achieves 43.1% mAP, which is 4% better than previous state-of-the-art.

---

### النسخة العربية

غالباً ما يتطلب تطوير نماذج الشبكات العصبية لتصنيف الصور قدراً كبيراً من _الهندسة المعمارية_. بدءاً من العمل الرائد [32] حول استخدام المعماريات الالتفافية [17، 34] لتصنيف ImageNet [11]، حققت التطورات المتعاقبة من خلال الهندسة المعمارية نتائج مبهرة [53، 59، 20، 60، 58، 68].

في هذه الورقة، ندرس نموذجاً جديداً لتصميم المعماريات الالتفافية ونصف طريقة قابلة للتوسع لتحسين المعماريات الالتفافية على مجموعة بيانات محل الاهتمام، على سبيل المثال مجموعة بيانات تصنيف ImageNet. يستوحى نهجنا من إطار البحث عن المعمارية العصبية (NAS) المقترح مؤخراً [71]، والذي يستخدم طريقة بحث التعلم المعزز لتحسين تكوينات المعمارية. ومع ذلك، فإن تطبيق NAS، أو أي طرق بحث أخرى، مباشرة على مجموعة بيانات كبيرة، مثل مجموعة بيانات ImageNet، مكلف حسابياً. لذلك نقترح البحث عن معمارية جيدة على مجموعة بيانات بديلة، على سبيل المثال مجموعة بيانات CIFAR-10 الأصغر، ثم نقل المعمارية المتعلمة إلى ImageNet. نحقق قابلية النقل هذه من خلال تصميم فضاء بحث (نسميه "فضاء بحث NASNet") بحيث يكون تعقيد المعمارية مستقلاً عن عمق الشبكة وحجم صور الإدخال. بشكل أكثر تحديداً، تتكون جميع الشبكات الالتفافية في فضاء البحث لدينا من طبقات التفافية (أو "خلايا") ذات بنية متطابقة ولكن بأوزان مختلفة. وبالتالي، يُختزل البحث عن أفضل المعماريات الالتفافية إلى البحث عن أفضل بنية خلية. للبحث عن أفضل بنية خلية فائدتان رئيسيتان: فهو أسرع بكثير من البحث عن معمارية شبكة كاملة، ومن المرجح أن تعمم الخلية نفسها على مشاكل أخرى. في تجاربنا، يسرّع هذا النهج البحث عن أفضل المعماريات باستخدام CIFAR-10 بشكل كبير بمعامل 7× ويتعلم معماريات تنتقل بنجاح إلى ImageNet.

نتيجتنا الرئيسية هي أن أفضل معمارية تم العثور عليها على CIFAR-10، والتي تسمى NASNet، تحقق دقة متقدمة عند نقلها إلى تصنيف ImageNet دون تعديل كبير. على ImageNet، يحقق NASNet، من بين الأعمال المنشورة، دقة متقدمة بنسبة 82.7% في أفضل-1 و96.2% في أفضل-5. تعادل هذه النتيجة تحسيناً بنسبة 1.2% في دقة أفضل-1 مقارنة بأفضل المعماريات المصممة بشرياً بينما تحتوي على 9 مليار عملية فاصلة عائمة أقل. على CIFAR-10 نفسها، يحقق NASNet معدل خطأ 2.4%، وهو أيضاً أحدث ما توصلت إليه التقنية.

بالإضافة إلى ذلك، من خلال تغيير عدد الخلايا الالتفافية وعدد المرشحات في الخلايا الالتفافية ببساطة، يمكننا إنشاء إصدارات مختلفة من NASNet بمتطلبات حسابية مختلفة. بفضل هذه الخاصية للخلايا، يمكننا توليد عائلة من النماذج التي تحقق دقة أفضل من جميع النماذج المصممة بشرياً عند ميزانيات حسابية مماثلة أو أصغر [60، 29]. والجدير بالذكر أن أصغر إصدار من NASNet يحقق دقة 74.0% في أفضل-1 على ImageNet، وهو أفضل بنسبة 3.1% من المعماريات المصممة سابقاً والموجهة نحو مهام الرؤية المحمولة والمدمجة [24، 70].

أخيراً، نُظهر أن ميزات الصور المتعلمة بواسطة NASNet مفيدة بشكل عام وتنتقل إلى مشاكل رؤية حاسوبية أخرى. في تجاربنا، يمكن دمج الميزات المتعلمة بواسطة NASNet من تصنيف ImageNet مع إطار Faster-RCNN [47] لتحقيق أحدث ما توصلت إليه التقنية في مهمة كشف أجسام COCO لكل من النماذج الأكبر والمحسّنة للمحمول. يحقق أكبر نموذج NASNet لدينا 43.1% mAP، وهو أفضل بنسبة 4% من أحدث ما توصلت إليه التقنية السابقة.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:**
  - Architecture engineering (الهندسة المعمارية)
  - Neural Architecture Search (NAS) (البحث عن المعمارية العصبية)
  - NASNet search space (فضاء بحث NASNet)
  - Cell (خلية)
  - Proxy dataset (مجموعة بيانات بديلة)
  - Transferability (قابلية النقل)

- **Equations:** None
- **Citations:** [32], [17, 34], [11], [53, 59, 20, 60, 58, 68], [71], [60, 29], [24, 70], [47]
- **Special handling:**
  - Kept technical metrics: 82.7% top-1, 96.2% top-5, 2.4% error rate, 74.0% top-1, 43.1% mAP
  - Preserved dataset names: ImageNet, CIFAR-10, COCO
  - Kept framework name: Faster-RCNN
  - Used established glossary terms consistently
  - Preserved speedup factor: 7×

### Quality Metrics

- **Semantic equivalence:** 0.90 - Accurately captures all key concepts and research contributions
- **Technical accuracy:** 0.91 - All technical terms correctly translated using glossary
- **Readability:** 0.88 - Natural flow in formal academic Arabic
- **Glossary consistency:** 0.89 - Consistent terminology throughout
- **Overall section score:** 0.89

### Back-Translation Validation

Developing neural network models for image classification often requires significant _architectural engineering_. Starting from the pioneering work [32] on using convolutional architectures [17, 34] for ImageNet [11] classification, successive developments through architectural engineering have achieved impressive results [53, 59, 20, 60, 58, 68].

In this paper, we study a new paradigm for designing convolutional architectures and describe a scalable method for optimizing convolutional architectures on a dataset of interest, for example the ImageNet classification dataset. Our approach is inspired by the recently proposed Neural Architecture Search (NAS) framework [71], which uses a reinforcement learning search method to optimize architecture configurations. However, applying NAS, or any other search methods, directly to a large dataset, such as the ImageNet dataset, is computationally expensive. Therefore, we propose searching for a good architecture on a proxy dataset, for example the smaller CIFAR-10 dataset, and then transferring the learned architecture to ImageNet. We achieve this transferability by designing a search space (which we call the "NASNet search space") so that the complexity of the architecture is independent of the network depth and the size of input images. More specifically, all convolutional networks in our search space consist of convolutional layers (or "cells") with identical structure but different weights. Thus, searching for the best convolutional architectures is reduced to searching for the best cell structure. Searching for the best cell structure has two main benefits: it is much faster than searching for a complete network architecture, and the cell itself is more likely to generalize to other problems. In our experiments, this approach significantly accelerates the search for the best architectures using CIFAR-10 by a factor of 7× and learns architectures that successfully transfer to ImageNet.

Our main result is that the best architecture found on CIFAR-10, called NASNet, achieves state-of-the-art accuracy when transferred to ImageNet classification without significant modification. On ImageNet, NASNet achieves, among published works, state-of-the-art accuracy of 82.7% top-1 and 96.2% top-5. This result represents a 1.2% improvement in top-1 accuracy compared to the best human-designed architectures while containing 9 billion fewer floating-point operations. On CIFAR-10 itself, NASNet achieves a 2.4% error rate, which is also state-of-the-art.

Additionally, by simply varying the number of convolutional cells and the number of filters in the convolutional cells, we can create different versions of NASNet with different computational requirements. Thanks to this property of cells, we can generate a family of models that achieve better accuracy than all human-designed models at comparable or smaller computational budgets [60, 29]. Notably, the smallest version of NASNet achieves 74.0% top-1 accuracy on ImageNet, which is 3.1% better than previously designed architectures targeted at mobile and embedded vision tasks [24, 70].

Finally, we show that image features learned by NASNet are generally useful and transfer to other computer vision problems. In our experiments, features learned by NASNet from ImageNet classification can be combined with the Faster-RCNN framework [47] to achieve state-of-the-art in the COCO object detection task for both the largest and mobile-optimized models. Our largest NASNet model achieves 43.1% mAP, which is 4% better than the previous state-of-the-art.
