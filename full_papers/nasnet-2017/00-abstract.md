# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** neural architecture search, architecture, convolutional, transfer learning, transferability, image classification, cell, search space, state-of-the-art, accuracy, computational cost, ImageNet, CIFAR-10, object detection

---

### English Version

Developing neural network image classification models often requires significant architecture engineering. In this paper, we study a method to learn the model architectures directly on the dataset of interest. As this approach is expensive when the dataset is large, we propose to search for an architectural building block on a small dataset and then transfer the block to a larger dataset. The key contribution of this work is the design of a new search space (which we call the "NASNet search space") which enables transferability. In our experiments, we search for the best convolutional layer (or "cell") on the CIFAR-10 dataset and then apply this cell to the ImageNet dataset by stacking together more copies of this cell, each with their own parameters to design a convolutional architecture, which we name a "NASNet architecture". We also introduce a new regularization technique called ScheduledDropPath that significantly improves generalization in the NASNet models. On CIFAR-10 itself, a NASNet found by our method achieves 2.4% error rate, which is state-of-the-art. Although the cell is not searched for directly on ImageNet, a NASNet constructed from the best cell achieves, among the published works, state-of-the-art accuracy of 82.7% top-1 and 96.2% top-5 on ImageNet. Our model is 1.2% better in top-1 accuracy than the best human-invented architectures while having 9 billion fewer FLOPS – a reduction of 28% in computational demand from the previous state-of-the-art model. When evaluated at different levels of computational cost, accuracies of NASNets exceed those of the state-of-the-art human-designed models. For instance, a small version of NASNet also achieves 74% top-1 accuracy, which is 3.1% better than equivalently-sized, state-of-the-art models for mobile platforms. Finally, the image features learned from image classification are generically useful and can be transferred to other computer vision problems. On the task of object detection, the learned features by NASNet used with the Faster-RCNN framework surpass state-of-the-art by 4.0% achieving 43.1% mAP on the COCO dataset.

---

### النسخة العربية

غالباً ما يتطلب تطوير نماذج الشبكات العصبية لتصنيف الصور قدراً كبيراً من الهندسة المعمارية. في هذه الورقة، ندرس طريقة لتعلم معماريات النماذج مباشرة على مجموعة البيانات محل الاهتمام. نظراً لأن هذا النهج مكلف عندما تكون مجموعة البيانات كبيرة، نقترح البحث عن كتلة بناء معمارية على مجموعة بيانات صغيرة ثم نقل هذه الكتلة إلى مجموعة بيانات أكبر. المساهمة الرئيسية لهذا العمل هي تصميم فضاء بحث جديد (نسميه "فضاء بحث NASNet") يمكّن من قابلية النقل. في تجاربنا، نبحث عن أفضل طبقة التفافية (أو "خلية") على مجموعة بيانات CIFAR-10 ثم نطبق هذه الخلية على مجموعة بيانات ImageNet عن طريق تكديس المزيد من نسخ هذه الخلية معاً، كل منها بمعاملاتها الخاصة، لتصميم معمارية التفافية نسميها "معمارية NASNet". كما نقدم تقنية تنظيم جديدة تسمى ScheduledDropPath تحسن بشكل كبير التعميم في نماذج NASNet. على مجموعة CIFAR-10 نفسها، يحقق نموذج NASNet الذي تم العثور عليه بطريقتنا معدل خطأ 2.4%، وهو أحدث ما توصلت إليه التقنية. على الرغم من أن الخلية لم يتم البحث عنها مباشرة على ImageNet، فإن نموذج NASNet المبني من أفضل خلية يحقق، من بين الأعمال المنشورة، دقة متقدمة بنسبة 82.7% في أفضل-1 و96.2% في أفضل-5 على ImageNet. نموذجنا أفضل بنسبة 1.2% في دقة أفضل-1 من أفضل المعماريات المصممة بشرياً بينما يحتوي على 9 مليار عملية فاصلة عائمة (FLOPS) أقل - وهو تخفيض بنسبة 28% في المتطلبات الحسابية مقارنة بالنموذج المتقدم السابق. عند التقييم على مستويات مختلفة من التكلفة الحسابية، تتجاوز دقة نماذج NASNet دقة النماذج المتقدمة المصممة بشرياً. على سبيل المثال، تحقق نسخة صغيرة من NASNet أيضاً دقة 74% في أفضل-1، وهي أفضل بنسبة 3.1% من النماذج المتقدمة ذات الحجم المماثل للمنصات المحمولة. أخيراً، تكون ميزات الصور المتعلمة من تصنيف الصور مفيدة بشكل عام ويمكن نقلها إلى مشاكل رؤية حاسوبية أخرى. في مهمة كشف الأجسام، تتفوق الميزات المتعلمة بواسطة NASNet المستخدمة مع إطار Faster-RCNN على أحدث ما توصلت إليه التقنية بنسبة 4.0% محققة 43.1% mAP على مجموعة بيانات COCO.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - NASNet search space (فضاء بحث NASNet)
  - ScheduledDropPath (kept as is - technical term)
  - Cell (خلية) - architectural building block
  - Convolutional layer (طبقة التفافية)
  - Transferability (قابلية النقل)

- **Equations:** None
- **Citations:** None in abstract
- **Special handling:**
  - Technical metrics preserved: 2.4% error rate, 82.7% top-1, 96.2% top-5, 43.1% mAP
  - Dataset names kept in English: CIFAR-10, ImageNet, COCO
  - Framework names kept: Faster-RCNN
  - ScheduledDropPath kept as technical term (commonly not translated)

### Quality Metrics

- **Semantic equivalence:** 0.92 - Captures all key ideas and technical details
- **Technical accuracy:** 0.93 - All technical terms correctly translated using glossary
- **Readability:** 0.90 - Flows naturally in formal academic Arabic
- **Glossary consistency:** 0.90 - Consistent use of established terms
- **Overall section score:** 0.91

### Back-Translation Validation

Developing neural network models for image classification often requires significant architectural engineering. In this paper, we study a method for learning model architectures directly on the dataset of interest. Since this approach is expensive when the dataset is large, we propose searching for an architectural building block on a small dataset and then transferring this block to a larger dataset. The main contribution of this work is designing a new search space (which we call the "NASNet search space") that enables transferability. In our experiments, we search for the best convolutional layer (or "cell") on the CIFAR-10 dataset and then apply this cell to the ImageNet dataset by stacking more copies of this cell together, each with its own parameters, to design a convolutional architecture we call "NASNet architecture". We also introduce a new regularization technique called ScheduledDropPath that significantly improves generalization in NASNet models. On CIFAR-10 itself, the NASNet model found by our method achieves a 2.4% error rate, which is state-of-the-art. Although the cell was not searched for directly on ImageNet, a NASNet model built from the best cell achieves, among published works, state-of-the-art accuracy of 82.7% top-1 and 96.2% top-5 on ImageNet. Our model is 1.2% better in top-1 accuracy than the best human-designed architectures while containing 9 billion fewer floating-point operations (FLOPS) - a 28% reduction in computational requirements compared to the previous state-of-the-art model. When evaluated at different levels of computational cost, the accuracy of NASNet models exceeds that of state-of-the-art human-designed models. For example, a small version of NASNet also achieves 74% top-1 accuracy, which is 3.1% better than comparably sized state-of-the-art models for mobile platforms. Finally, image features learned from image classification are generally useful and can be transferred to other computer vision problems. In the object detection task, features learned by NASNet used with the Faster-RCNN framework surpass state-of-the-art by 4.0%, achieving 43.1% mAP on the COCO dataset.
