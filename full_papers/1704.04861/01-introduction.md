# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** convolutional neural network, computer vision, deep learning, accuracy, architecture, hyperparameter, latency, embedded systems, efficient

---

### English Version

Convolutional neural networks have become ubiquitous in computer vision ever since AlexNet [19] popularized deep convolutional neural networks by winning the ImageNet Challenge: ILSVRC 2012 [24]. The general trend has been to make deeper and more complicated networks in order to achieve higher accuracy [27, 31, 29, 8]. However, these advances to improve accuracy are not necessarily making networks more efficient with respect to size and speed. In many real world applications such as robotics, self-driving car and augmented reality, the recognition tasks need to be carried out in a timely fashion on a computationally limited platform.

This paper describes an efficient network architecture and a set of two hyper-parameters in order to build very small, low latency models that can be easily matched to the design requirements for mobile and embedded vision applications. Section 2 reviews prior work in building small models. Section 3 describes the MobileNet architecture and two hyper-parameters width multiplier and resolution multiplier to define smaller and more efficient MobileNets. Section 4 describes experiments on ImageNet as well a variety of different applications and use cases. Section 5 closes with a summary and conclusion.

---

### النسخة العربية

أصبحت الشبكات العصبية الالتفافية منتشرة في كل مكان في مجال الرؤية الحاسوبية منذ أن جعلت AlexNet [19] الشبكات العصبية الالتفافية العميقة شائعة من خلال الفوز بتحدي ImageNet: ILSVRC 2012 [24]. كان الاتجاه العام هو بناء شبكات أعمق وأكثر تعقيداً من أجل تحقيق دقة أعلى [27، 31، 29، 8]. ومع ذلك، فإن هذه التطورات لتحسين الدقة لا تجعل الشبكات بالضرورة أكثر كفاءة من حيث الحجم والسرعة. في العديد من تطبيقات العالم الحقيقي مثل الروبوتات والسيارات ذاتية القيادة والواقع المعزز، تحتاج مهام التعرف إلى تنفيذها في الوقت المناسب على منصة محدودة حسابياً.

تصف هذه الورقة معمارية شبكة فعالة ومجموعة من معاملين فائقين من أجل بناء نماذج صغيرة جداً ومنخفضة زمن الاستجابة يمكن مطابقتها بسهولة مع متطلبات التصميم لتطبيقات الرؤية الحاسوبية المحمولة والمدمجة. يستعرض القسم 2 الأعمال السابقة في بناء النماذج الصغيرة. يصف القسم 3 معمارية MobileNet ومعاملين فائقين هما مضاعف العرض ومضاعف الدقة لتعريف نماذج MobileNets أصغر وأكثر كفاءة. يصف القسم 4 التجارب على ImageNet بالإضافة إلى مجموعة متنوعة من التطبيقات وحالات الاستخدام المختلفة. يُختتم القسم 5 بملخص واستنتاج.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** AlexNet, ImageNet Challenge, width multiplier (مضاعف العرض), resolution multiplier (مضاعف الدقة)
- **Equations:** 0
- **Citations:** [19], [24], [27], [31], [29], [8]
- **Special handling:** Kept proper names (AlexNet, ImageNet, ILSVRC, MobileNet) in English as standard practice

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89
