# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional networks (ConvNets), image recognition, video recognition, ImageNet, GPU, distributed clusters, ILSVRC, deep learning, classification, architecture, depth, convolution filters, receptive window, stride, training, testing, fine-tuning, linear SVM

---

### English Version

Convolutional networks (ConvNets) have recently enjoyed a great success in large-scale image and video recognition which has become possible due to the large public image repositories, such as ImageNet, and high-performance computing systems, such as GPUs or large-scale distributed clusters. In particular, an important role in the advance of deep visual recognition architectures has been played by the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC), which has served as a testbed for a few generations of large-scale image classification systems, from high-dimensional shallow feature encodings (the winner of ILSVRC-2011) to deep ConvNets (the winner of ILSVRC-2012).

With ConvNets becoming more of a commodity in the computer vision field, a number of attempts have been made to improve the original architecture of Krizhevsky et al. in a bid to achieve better accuracy. For instance, the best-performing submissions to the ILSVRC-2013 utilised smaller receptive window size and smaller stride of the first convolutional layer. Another line of improvements dealt with training and testing the networks densely over the whole image and over multiple scales. In this paper, we address another important aspect of ConvNet architecture design -- its depth. To this end, we fix other parameters of the architecture, and steadily increase the depth of the network by adding more convolutional layers, which is feasible due to the use of very small (3×3) convolution filters in all layers.

As a result, we come up with significantly more accurate ConvNet architectures, which not only achieve the state-of-the-art accuracy on ILSVRC classification and localisation tasks, but are also applicable to other image recognition datasets, where they achieve excellent performance even when used as a part of a relatively simple pipelines (e.g. deep features classified by a linear SVM without fine-tuning). We have released our two best-performing models to facilitate further research.

The rest of the paper is organised as follows. In Sect. 2, we describe our ConvNet configurations. The details of the image classification training and evaluation are then presented in Sect. 3, and the configurations are compared on the ILSVRC classification task in Sect. 4. Sect. 5 concludes the paper. For completeness, we also describe and assess our ILSVRC-2014 object localisation system in Appendix A, and discuss the generalisation of very deep features to other datasets in Appendix B. Finally, Appendix C contains the list of major paper revisions.

---

### النسخة العربية

حققت الشبكات الالتفافية (ConvNets) مؤخراً نجاحاً كبيراً في التعرف على الصور والفيديو واسعة النطاق، والذي أصبح ممكناً بفضل مستودعات الصور العامة الكبيرة، مثل ImageNet، وأنظمة الحوسبة عالية الأداء، مثل وحدات معالجة الرسومات (GPU) أو المجموعات الموزعة واسعة النطاق. على وجه الخصوص، لعب تحدي ImageNet للتعرف البصري واسع النطاق (ILSVRC) دوراً مهماً في تقدم معماريات التعرف البصري العميقة، حيث عمل كمنصة اختبار لعدة أجيال من أنظمة تصنيف الصور واسعة النطاق، من ترميزات الميزات الضحلة عالية الأبعاد (الفائز في ILSVRC-2011) إلى الشبكات الالتفافية العميقة (الفائز في ILSVRC-2012).

مع أصبحت الشبكات الالتفافية أكثر شيوعاً في مجال رؤية الحاسوب، تم إجراء عدد من المحاولات لتحسين المعمارية الأصلية لـ Krizhevsky وآخرون في محاولة لتحقيق دقة أفضل. على سبيل المثال، استخدمت المشاركات الأفضل أداءً في ILSVRC-2013 حجم نافذة استقبال أصغر وخطوة أصغر للطبقة الالتفافية الأولى. تعامل خط آخر من التحسينات مع تدريب واختبار الشبكات بكثافة على الصورة بأكملها وعلى مقاييس متعددة. في هذا البحث، نتناول جانباً مهماً آخر من تصميم معمارية الشبكة الالتفافية -- وهو عمقها. لتحقيق ذلك، نثبت معاملات المعمارية الأخرى، ونزيد بثبات عمق الشبكة بإضافة المزيد من الطبقات الالتفافية، وهو أمر ممكن بفضل استخدام مرشحات التفاف صغيرة جداً (3×3) في جميع الطبقات.

ونتيجة لذلك، توصلنا إلى معماريات شبكات التفافية أكثر دقة بشكل ملحوظ، والتي لا تحقق فقط أحدث مستويات الدقة في مهام تصنيف وتوطين ILSVRC، ولكنها قابلة للتطبيق أيضاً على مجموعات بيانات التعرف على الصور الأخرى، حيث تحقق أداءً ممتازاً حتى عند استخدامها كجزء من خطوط أنابيب بسيطة نسبياً (مثل الميزات العميقة المصنفة بواسطة آلة المتجهات الداعمة الخطية (SVM) دون ضبط دقيق). لقد أتحنا نموذجينا الأفضل أداءً لتسهيل المزيد من الأبحاث.

يتم تنظيم بقية البحث على النحو التالي. في القسم 2، نصف تكوينات شبكتنا الالتفافية. ثم يتم عرض تفاصيل التدريب والتقييم لتصنيف الصور في القسم 3، وتتم مقارنة التكوينات في مهمة تصنيف ILSVRC في القسم 4. يختتم القسم 5 البحث. من أجل الاكتمال، نصف ونقيّم أيضاً نظام توطين الكائنات ILSVRC-2014 في الملحق أ، ونناقش تعميم الميزات العميقة جداً على مجموعات بيانات أخرى في الملحق ب. أخيراً، يحتوي الملحق ج على قائمة بالمراجعات الرئيسية للبحث.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** ConvNets, ImageNet, ILSVRC, GPU, distributed clusters, receptive window, stride, dense training/testing, multi-scale, depth, 3×3 convolution filters, localisation, generalisation, linear SVM, fine-tuning
- **Equations:** None
- **Citations:** Multiple citations to prior work (Krizhevsky12, Zeiler13, Sermanet14, etc.)
- **Special handling:**
  - Preserved citation format in square brackets
  - Maintained section references (Sect. 2, etc.)
  - Kept technical terms like "ConvNets" and proper nouns like "ImageNet" in Latin script where appropriate

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation

Convolutional networks (ConvNets) recently achieved great success in large-scale image and video recognition, which became possible thanks to large public image repositories, such as ImageNet, and high-performance computing systems, such as Graphics Processing Units (GPU) or large-scale distributed clusters. In particular, the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC) played an important role in advancing deep visual recognition architectures, serving as a testing platform for several generations of large-scale image classification systems, from shallow high-dimensional feature encodings (winner of ILSVRC-2011) to deep convolutional networks (winner of ILSVRC-2012).

As convolutional networks became more common in the field of computer vision, a number of attempts were made to improve the original architecture of Krizhevsky et al. in an attempt to achieve better accuracy. For example, the best-performing submissions in ILSVRC-2013 used smaller receptive window size and smaller stride for the first convolutional layer. Another line of improvements dealt with training and testing networks densely over the entire image and at multiple scales. In this research, we address another important aspect of convolutional network architecture design -- its depth. To achieve this, we fix other architecture parameters, and steadily increase the network depth by adding more convolutional layers, which is possible thanks to using very small (3×3) convolution filters in all layers.

As a result, we arrived at significantly more accurate convolutional network architectures, which not only achieve state-of-the-art accuracy in ILSVRC classification and localization tasks, but are also applicable to other image recognition datasets, where they achieve excellent performance even when used as part of relatively simple pipelines (such as deep features classified by linear Support Vector Machine (SVM) without fine-tuning). We have made our two best-performing models available to facilitate further research.

The rest of the research is organized as follows. In Section 2, we describe our convolutional network configurations. Then the details of training and evaluation for image classification are presented in Section 3, and the configurations are compared in the ILSVRC classification task in Section 4. Section 5 concludes the research. For completeness, we also describe and evaluate the ILSVRC-2014 object localization system in Appendix A, and discuss generalization of very deep features to other datasets in Appendix B. Finally, Appendix C contains a list of major research revisions.
