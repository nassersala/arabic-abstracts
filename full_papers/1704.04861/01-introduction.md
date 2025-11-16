# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** convolutional neural networks, computer vision, deep learning, accuracy, efficient, architecture, latency, hyperparameter

---

### English Version

Convolutional neural networks have become ubiquitous in computer vision ever since AlexNet [19] popularized deep convolutional neural networks by winning the ImageNet Challenge: ILSVRC 2012 [24]. The general trend has been to make deeper and more complicated networks in order to achieve higher accuracy [27, 31, 29, 8]. However, these advances to improve accuracy are not necessarily making networks more efficient with respect to size and speed. In many real world applications such as robotics, self-driving car and augmented reality, the recognition tasks need to be carried out in a timely fashion on a computationally limited platform.

This paper describes an efficient network architecture and a set of two hyper-parameters in order to build very small, low latency models that can be easily matched to the design requirements for mobile and embedded vision applications. Section 2 reviews prior work in building small models. Section 3 describes the MobileNet architecture and two hyper-parameters width multiplier and resolution multiplier to define smaller and more efficient MobileNets. Section 4 describes experiments on ImageNet as well a variety of different applications and use cases. Section 5 closes with a summary and conclusion.

---

### النسخة العربية

أصبحت الشبكات العصبية الالتفافية منتشرة في كل مكان في مجال الرؤية الحاسوبية منذ أن عممت شبكة AlexNet [19] استخدام الشبكات العصبية الالتفافية العميقة من خلال الفوز بتحدي ImageNet: ILSVRC 2012 [24]. كان الاتجاه العام هو بناء شبكات أعمق وأكثر تعقيداً لتحقيق دقة أعلى [27, 31, 29, 8]. ومع ذلك، فإن هذه التطورات لتحسين الدقة لا تجعل الشبكات بالضرورة أكثر كفاءة من حيث الحجم والسرعة. في العديد من التطبيقات الواقعية مثل الروبوتات والسيارات ذاتية القيادة والواقع المعزز، تحتاج مهام التعرف إلى التنفيذ في الوقت المناسب على منصة محدودة الموارد الحسابية.

تصف هذه الورقة معمارية شبكة فعالة ومجموعة من معاملين فائقين لبناء نماذج صغيرة جداً ذات زمن استجابة منخفض يمكن مطابقتها بسهولة مع متطلبات التصميم لتطبيقات الرؤية الحاسوبية المحمولة والمدمجة. يستعرض القسم 2 الأعمال السابقة في بناء النماذج الصغيرة. يصف القسم 3 معمارية MobileNet ومعاملين فائقين هما مضاعف العرض ومضاعف دقة الوضوح لتعريف شبكات MobileNets أصغر وأكثر كفاءة. يصف القسم 4 التجارب على ImageNet بالإضافة إلى مجموعة متنوعة من التطبيقات وحالات الاستخدام المختلفة. يختتم القسم 5 بملخص واستنتاج.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** AlexNet, ImageNet Challenge, ILSVRC, width multiplier, resolution multiplier, computationally limited platform
- **Equations:** None
- **Citations:** [19], [24], [27, 31, 29, 8]
- **Special handling:** 
  - "AlexNet", "ImageNet", "ILSVRC" kept as proper nouns
  - "width multiplier" translated as "مضاعف العرض"
  - "resolution multiplier" translated as "مضاعف دقة الوضوح"
  - "computationally limited" translated as "محدودة الموارد الحسابية"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
