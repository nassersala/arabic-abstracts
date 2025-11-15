# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional networks, image recognition, architecture, accuracy, deep learning, classification, training, GPU, ImageNet, depth

---

### English Version

Convolutional networks (ConvNets) have recently enjoyed a great success in large-scale image and video recognition (Krizhevsky et al., 2012; Zeiler & Fergus, 2013; Sermanet et al., 2014; Simonyan & Zisserman, 2014) which has become possible due to the large public image repositories, such as ImageNet (Deng et al., 2009), and high-performance computing systems, such as GPUs or large-scale distributed clusters (Dean et al., 2012). In particular, an important role in the advance of deep visual recognition architectures has been played by the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC) (Russakovsky et al., 2014), which has served as a testbed for a few generations of large-scale image classification systems, from high-dimensional shallow feature encodings (Perronnin et al., 2010) (the winner of ILSVRC-2011) to deep ConvNets (Krizhevsky et al., 2012) (the winner of ILSVRC-2012).

With ConvNets becoming more of a commodity in the computer vision field, a number of attempts have been made to improve the original architecture of Krizhevsky et al. (2012) in a bid to achieve better accuracy. For instance, the best-performing submissions to the ILSVRC-2013 (Zeiler & Fergus, 2013; Sermanet et al., 2014) utilised smaller receptive window size and smaller stride of the first convolutional layer. Another line of improvements dealt with training and testing the networks densely over the whole image and over multiple scales (Sermanet et al., 2014; Howard, 2014). In this paper, we address another important aspect of ConvNet architecture design – its depth. To this end, we fix other parameters of the architecture, and steadily increase the depth of the network by adding more convolutional layers, which is feasible due to the use of very small (3×3) convolution filters in all layers.

As a result, we come up with significantly more accurate ConvNet architectures, which not only achieve the state-of-the-art accuracy on ILSVRC classification and localisation tasks, but are also applicable to other image recognition datasets, where they achieve excellent performance even when used as a part of a relatively simple pipelines (e.g. deep features classified by a linear SVM without fine-tuning). We have released our two best-performing models to facilitate further research.

The rest of the paper is organised as follows. In Sect. 2, we describe our ConvNet configurations. The details of the image classification training and evaluation are then presented in Sect. 3, and the configurations are compared on the ILSVRC classification task in Sect. 4. Sect. 5 concludes the paper. For completeness, we also describe and assess our ILSVRC-2014 object localisation system in Appendix A, and discuss the generalisation of very deep features to other datasets in Appendix B. Finally, Appendix C contains the list of major paper revisions.

---

### النسخة العربية

حققت الشبكات الالتفافية (ConvNets) مؤخراً نجاحاً كبيراً في التعرف على الصور والفيديو واسع النطاق (Krizhevsky et al., 2012; Zeiler & Fergus, 2013; Sermanet et al., 2014; Simonyan & Zisserman, 2014) والذي أصبح ممكناً بفضل مستودعات الصور العامة الكبيرة، مثل ImageNet (Deng et al., 2009)، وأنظمة الحوسبة عالية الأداء، مثل وحدات معالجة الرسومات (GPUs) أو المجموعات الموزعة واسعة النطاق (Dean et al., 2012). على وجه الخصوص، لعبت تحدي ImageNet للتعرف البصري واسع النطاق (ILSVRC) (Russakovsky et al., 2014) دوراً مهماً في تقدم معماريات التعرف البصري العميق، حيث عملت كمنصة اختبار لعدة أجيال من أنظمة تصنيف الصور واسعة النطاق، من ترميز الميزات السطحية عالية الأبعاد (Perronnin et al., 2010) (الفائز في ILSVRC-2011) إلى الشبكات الالتفافية العميقة (Krizhevsky et al., 2012) (الفائز في ILSVRC-2012).

مع تحول الشبكات الالتفافية إلى تقنية شائعة في مجال رؤية الحاسوب، تم إجراء عدد من المحاولات لتحسين المعمارية الأصلية لـ Krizhevsky et al. (2012) في محاولة لتحقيق دقة أفضل. على سبيل المثال، استخدمت المساهمات الأفضل أداءً في ILSVRC-2013 (Zeiler & Fergus, 2013; Sermanet et al., 2014) حجم نافذة استقبال أصغر وخطوة أصغر للطبقة الالتفافية الأولى. وتناول خط آخر من التحسينات تدريب واختبار الشبكات بكثافة على الصورة بأكملها وعلى مقاييس متعددة (Sermanet et al., 2014; Howard, 2014). في هذه الورقة، نتناول جانباً مهماً آخر من تصميم معمارية الشبكات الالتفافية - وهو عمقها. لهذه الغاية، نُثبّت المعاملات الأخرى للمعمارية، ونزيد باستمرار من عمق الشبكة من خلال إضافة المزيد من الطبقات الالتفافية، وهو ما يكون ممكناً بفضل استخدام مرشحات التفاف صغيرة جداً (3×3) في جميع الطبقات.

ونتيجة لذلك، نتوصل إلى معماريات شبكات التفافية أكثر دقة بشكل كبير، والتي لا تحقق فقط دقة متقدمة على مهام التصنيف والتوطين في ILSVRC، ولكنها أيضاً قابلة للتطبيق على مجموعات بيانات التعرف على الصور الأخرى، حيث تحقق أداءً ممتازاً حتى عند استخدامها كجزء من خطوط معالجة بسيطة نسبياً (مثل الميزات العميقة المصنفة بواسطة SVM خطي دون ضبط دقيق). لقد أصدرنا أفضل نموذجين لدينا لتسهيل المزيد من البحث.

تم تنظيم بقية الورقة على النحو التالي. في القسم 2، نصف تكوينات الشبكة الالتفافية الخاصة بنا. ثم يتم عرض تفاصيل تدريب وتقييم تصنيف الصور في القسم 3، وتتم مقارنة التكوينات على مهمة تصنيف ILSVRC في القسم 4. يختتم القسم 5 الورقة. للاكتمال، نصف أيضاً ونقيّم نظام توطين الأشياء ILSVRC-2014 الخاص بنا في الملحق A، ونناقش تعميم الميزات العميقة جداً على مجموعات البيانات الأخرى في الملحق B. وأخيراً، يحتوي الملحق C على قائمة بالمراجعات الرئيسية للورقة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Convolutional networks (ConvNets), ImageNet, ILSVRC, receptive window, stride, depth, convolution filters, localisation, feature encoding, GPUs
- **Equations:** 0
- **Citations:** Multiple references to ImageNet Challenge, Krizhevsky et al., and other foundational works
- **Special handling:** Preserved all citation formats [Author et al., Year]

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
