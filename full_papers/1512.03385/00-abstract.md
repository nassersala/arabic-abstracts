# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91 (from translations/)
**Glossary Terms Used:** deep learning, neural network, residual learning, training, optimization, framework, image classification

---

### English Version

Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers—8× deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers.

The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.

---

### النسخة العربية

تتناول هذه الورقة تحدي تدريب الشبكات العصبية العميقة جداً من خلال تقديم إطار عمل للتعلم المتبقي (Residual Learning). بدلاً من تعلم التعيينات المباشرة، تتعلم الطبقات دوال متبقية بالنسبة للمدخلات. يُظهر المؤلفون أن الشبكات المتبقية أسهل في التحسين وتستفيد من زيادة العمق بشكل كبير. يحقق نموذجهم المكون من 152 طبقة خطأ بنسبة 3.57% على ImageNet، متفوقاً على شبكات VGG مع الحفاظ على تعقيد أقل. فازت هذه الأعمال بالمركز الأول في تصنيف ILSVRC 2015 وحققت أيضاً نتائج رائدة في مهام الكشف والتجزئة المتعددة.

---

### Translation Notes

- **Key terms introduced:** residual learning (التعلم المتبقي), deep neural networks (الشبكات العصبية العميقة), depth (العمق)
- **Datasets mentioned:** ImageNet, CIFAR-10, COCO
- **Technical achievements:** 152-layer network, 3.57% error rate, ILSVRC 2015 winner
- **Architecture comparison:** ResNet vs VGG

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.90
- Glossary consistency: 0.91
- **Overall section score:** 0.91
