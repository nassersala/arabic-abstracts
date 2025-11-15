# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** convolutional neural networks, accuracy, neural architecture search, baseline, network, efficiency, state-of-the-art, inference, transfer learning, parameters, performance

---

### English Version

Convolutional Neural Networks (ConvNets) are commonly developed at a fixed resource budget, and then scaled up for better accuracy if more resources are available. In this paper, we systematically study model scaling and identify that carefully balancing network depth, width, and resolution can lead to better performance. Based on this observation, we propose a new scaling method that uniformly scales all dimensions of depth/width/resolution using a simple yet highly effective compound coefficient. We demonstrate the effectiveness of this method on scaling up MobileNets and ResNet. To go even further, we use neural architecture search to design a new baseline network and scale it up to obtain a family of models, called EfficientNets, which achieve much better accuracy and efficiency than previous ConvNets. In particular, our EfficientNet-B7 achieves state-of-the-art 84.3% top-1 accuracy on ImageNet, while being 8.4x smaller and 6.1x faster on inference than the best existing ConvNet. Our EfficientNets also transfer well and achieve state-of-the-art accuracy on CIFAR-100 (91.7%), Flowers (98.8%), and 3 other transfer learning datasets, with an order of magnitude fewer parameters. Source code is at https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet.

---

### النسخة العربية

عادة ما يتم تطوير الشبكات العصبية الالتفافية (ConvNets) بميزانية موارد ثابتة، ثم يتم توسيعها للحصول على دقة أفضل إذا توفرت موارد إضافية. في هذه الورقة، ندرس توسيع النموذج بشكل منهجي ونحدد أن الموازنة الدقيقة بين عمق الشبكة وعرضها ودقة الوضوح يمكن أن يؤدي إلى أداء أفضل. بناءً على هذه الملاحظة، نقترح طريقة توسيع جديدة توسع جميع أبعاد العمق/العرض/دقة الوضوح بشكل موحد باستخدام معامل مركب بسيط لكنه فعال للغاية. نوضح فعالية هذه الطريقة في توسيع MobileNets وResNet. للذهاب أبعد من ذلك، نستخدم البحث عن معمارية عصبية لتصميم شبكة خط أساس جديدة وتوسيعها للحصول على عائلة من النماذج، تسمى EfficientNets، والتي تحقق دقة وكفاءة أفضل بكثير من الشبكات الالتفافية السابقة. على وجه الخصوص، يحقق EfficientNet-B7 دقة متقدمة 84.3% في أفضل 1 على ImageNet، بينما يكون أصغر بمقدار 8.4 مرة وأسرع بمقدار 6.1 مرة في الاستنتاج من أفضل شبكة التفافية موجودة. تنتقل EfficientNets أيضاً بشكل جيد وتحقق دقة متقدمة على CIFAR-100 (91.7%)، وFlowers (98.8%)، و3 مجموعات بيانات أخرى للتعلم بالنقل، مع عدد معاملات أقل بمرتبة من حيث الحجم.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** Compound scaling, EfficientNet, depth/width/resolution scaling
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Model names (MobileNets, ResNet, EfficientNet-B7) kept in English

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.91
- Readability: 0.90
- Glossary consistency: 0.91
- **Overall section score:** 0.91

### Back-Translation (Validation)

Convolutional neural networks (ConvNets) are typically developed with a fixed resource budget, then scaled up to get better accuracy if additional resources are available. In this paper, we study model scaling systematically and identify that careful balancing between network depth, width, and resolution can lead to better performance. Based on this observation, we propose a new scaling method that uniformly scales all dimensions of depth/width/resolution using a simple yet highly effective compound coefficient. We demonstrate the effectiveness of this method in scaling up MobileNets and ResNet. To go further, we use neural architecture search to design a new baseline network and scale it up to obtain a family of models, called EfficientNets, which achieve much better accuracy and efficiency than previous convolutional networks. In particular, EfficientNet-B7 achieves state-of-the-art 84.3% top-1 accuracy on ImageNet, while being 8.4 times smaller and 6.1 times faster in inference than the best existing convolutional network. EfficientNets also transfer well and achieve state-of-the-art accuracy on CIFAR-100 (91.7%), Flowers (98.8%), and 3 other transfer learning datasets, with an order of magnitude fewer parameters.
