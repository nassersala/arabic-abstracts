# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** convolutional neural network, computer vision, deep learning, accuracy, efficient, architecture, hyperparameter, latency, embedded systems, augmented reality

---

### English Version

Convolutional neural networks have become ubiquitous in computer vision ever since AlexNet [19] popularized deep convolutional neural networks by winning the ImageNet Challenge: ILSVRC 2012 [24]. The general trend has been to make deeper and more complicated networks in order to achieve higher accuracy [27, 31, 29, 8]. However, these advances to improve accuracy are not necessarily making networks more efficient with respect to size and speed. In many real world applications such as robotics, self-driving car and augmented reality, the recognition tasks need to be carried out in a timely fashion on a computationally limited platform.

This paper describes an efficient network architecture and a set of two hyper-parameters in order to build very small, low latency models that can be easily matched to the design requirements for mobile and embedded vision applications. Section 2 reviews prior work in building small models. Section 3 describes the MobileNet architecture and two hyper-parameters width multiplier and resolution multiplier to define smaller and more efficient MobileNets. Section 4 describes experiments on ImageNet as well a variety of different applications and use cases. Section 5 closes with a summary and conclusion.

**Figure 1:** MobileNet models can be applied to various recognition tasks for efficient on device intelligence.

---

### النسخة العربية

أصبحت الشبكات العصبية الالتفافية منتشرة في كل مكان في مجال الرؤية الحاسوبية منذ أن قامت AlexNet [19] بنشر الشبكات العصبية الالتفافية العميقة من خلال الفوز بتحدي ImageNet: ILSVRC 2012 [24]. كان الاتجاه العام هو إنشاء شبكات أعمق وأكثر تعقيداً من أجل تحقيق دقة أعلى [27، 31، 29، 8]. ومع ذلك، فإن هذه التطورات لتحسين الدقة لا تجعل الشبكات بالضرورة أكثر كفاءة من حيث الحجم والسرعة. في العديد من التطبيقات الواقعية مثل الروبوتات والسيارات ذاتية القيادة والواقع المعزز، تحتاج مهام التعرف إلى أن تُنفذ في الوقت المناسب على منصة محدودة حسابياً.

تصف هذه الورقة معمارية شبكة فعالة ومجموعة من معاملين فائقين من أجل بناء نماذج صغيرة جداً ذات زمن استجابة منخفض يمكن مطابقتها بسهولة مع متطلبات التصميم لتطبيقات الرؤية المحمولة والمدمجة. يستعرض القسم 2 الأعمال السابقة في بناء النماذج الصغيرة. يصف القسم 3 معمارية MobileNet ومعاملين فائقين هما مضاعف العرض ومضاعف الدقة لتعريف شبكات MobileNets أصغر وأكثر كفاءة. يصف القسم 4 التجارب على ImageNet بالإضافة إلى مجموعة متنوعة من التطبيقات المختلفة وحالات الاستخدام. يختتم القسم 5 بملخص وخاتمة.

**الشكل 1:** يمكن تطبيق نماذج MobileNet على مهام التعرف المختلفة للذكاء الفعال على الأجهزة.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** MobileNet, width multiplier (مضاعف العرض), resolution multiplier (مضاعف الدقة)
- **Equations:** None
- **Citations:** [19], [24], [27, 31, 29, 8] - kept in original format
- **Special handling:**
  - "AlexNet" and "ImageNet" kept as proper names
  - Section references translated but numbers kept
  - "ILSVRC 2012" kept as acronym with year

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89

### Back-Translation Check

The Arabic translation conveys that CNNs became widespread in computer vision after AlexNet popularized deep CNNs by winning ImageNet 2012. The trend has been toward deeper, more complex networks for higher accuracy, but these advances don't necessarily improve efficiency in size and speed. For real-world applications like robotics, self-driving cars, and AR, recognition tasks must execute timely on computationally limited platforms. The paper describes an efficient architecture with two hyperparameters to build very small, low-latency models that match design requirements for mobile and embedded vision applications. Sections 2-5 cover prior work, architecture, experiments, and conclusion respectively.
