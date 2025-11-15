# Section 6: Conclusion
## القسم 6: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.89
**Glossary Terms Used:** convolutional neural networks, model scaling, accuracy, efficiency, compound scaling, depth, width, resolution, ImageNet, transfer learning, neural architecture search

---

### English Version

In this paper, we systematically study ConvNet accuracy and efficiency, and observe that carefully balancing network depth, width, and resolution is critical for better performance. Inspired by this observation, we propose a simple and highly effective compound scaling method, which enables us to easily scale up a baseline ConvNet to any target resource constraints in a more principled way, while maintaining model efficiency.

Powered by this compound scaling method and recent progress on AutoML, we have developed a family of models, called EfficientNets, which achieve much better accuracy and efficiency than previous ConvNets. In particular, our EfficientNet-B7 achieves state-of-the-art 84.3% top-1 accuracy on ImageNet with 66M parameters and 37B FLOPS, being 8.4x smaller and 6.1x faster on inference than the best existing ConvNet. Our EfficientNets also transfer well and achieve state-of-the-art accuracy on CIFAR-100 (91.7%), Flowers (98.8%), and three other transfer learning datasets, while having an order of magnitude fewer parameters than existing ConvNets.

We believe our work offers a new perspective on model scaling and demonstrates its potential to improve accuracy and efficiency for a broad range of models and tasks. For future work, we will study how to transfer this compound scaling method to more types of networks beyond image classification.

---

### النسخة العربية

في هذه الورقة، ندرس بشكل منهجي دقة وكفاءة الشبكة الالتفافية، ونلاحظ أن الموازنة الدقيقة بين عمق الشبكة وعرضها ودقة وضوحها أمر بالغ الأهمية للحصول على أداء أفضل. مستوحاة من هذه الملاحظة، نقترح طريقة توسيع مركبة بسيطة وفعالة للغاية، والتي تمكننا من توسيع شبكة التفافية خط الأساس بسهولة إلى أي قيود موارد مستهدفة بطريقة أكثر منهجية، مع الحفاظ على كفاءة النموذج.

مدعومين بطريقة التوسيع المركبة هذه والتقدم الأخير في AutoML، قمنا بتطوير عائلة من النماذج، تسمى EfficientNets، والتي تحقق دقة وكفاءة أفضل بكثير من الشبكات الالتفافية السابقة. على وجه الخصوص، يحقق EfficientNet-B7 دقة متقدمة 84.3% في أفضل 1 على ImageNet مع 66 مليون معامل و37 مليار FLOPS، كونه أصغر بمقدار 8.4 مرة وأسرع بمقدار 6.1 مرة في الاستنتاج من أفضل شبكة التفافية موجودة. تنتقل EfficientNets أيضاً بشكل جيد وتحقق دقة متقدمة على CIFAR-100 (91.7%)، وFlowers (98.8%)، وثلاث مجموعات بيانات أخرى للتعلم بالنقل، مع وجود عدد معاملات أقل بمرتبة من حيث الحجم من الشبكات الالتفافية الموجودة.

نعتقد أن عملنا يقدم منظوراً جديداً حول توسيع النموذج ويوضح إمكاناته لتحسين الدقة والكفاءة لمجموعة واسعة من النماذج والمهام. بالنسبة للعمل المستقبلي، سندرس كيفية نقل طريقة التوسيع المركبة هذه إلى المزيد من أنواع الشبكات بخلاف تصنيف الصور.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** AutoML (automated machine learning)
- **Equations:** 0
- **Citations:** General references to previous sections
- **Special handling:** Maintained formal academic tone appropriate for conclusion section

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89

### Back-Translation (Key Message)

"In this paper, we systematically study the accuracy and efficiency of convolutional networks, and observe that careful balancing between network depth, width, and resolution is critically important for better performance. Inspired by this observation, we propose a simple and highly effective compound scaling method, which enables us to easily scale up a baseline convolutional network to any target resource constraints in a more systematic way, while maintaining model efficiency."

---

## Additional Sections

### Acknowledgments
## الشكر والتقدير

The authors would like to thank the Google Brain team, the Google TPU team, and all the collaborators who contributed to this work.

يود المؤلفون أن يشكروا فريق Google Brain، وفريق Google TPU، وجميع المتعاونين الذين ساهموا في هذا العمل.

---

### References

The paper contains extensive references to prior work in ConvNets, model scaling, neural architecture search, and image classification. Key references include:

- AlexNet, VGGNet, Inception, ResNet families
- MobileNet, ShuffleNet, SqueezeNet
- NASNet, MnasNet, AmoebaNet
- GPipe, SENet
- ImageNet, CIFAR datasets

تحتوي الورقة على مراجع واسعة للأعمال السابقة في الشبكات الالتفافية، وتوسيع النموذج، والبحث عن معمارية عصبية، وتصنيف الصور. تشمل المراجع الرئيسية:

- عائلات AlexNet وVGGNet وInception وResNet
- MobileNet وShuffleNet وSqueezeNet
- NASNet وMnasNet وAmoebaNet
- GPipe وSENet
- مجموعات بيانات ImageNet وCIFAR
