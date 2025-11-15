# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** transformer, self-attention, architecture, natural language processing, pre-training, fine-tuning, convolutional neural network, computer vision, image classification, inductive bias, translation equivariance, dataset, benchmark, state-of-the-art

---

### English Version

Self-attention-based architectures, in particular Transformers (Vaswani et al., 2017), have become the model of choice in natural language processing (NLP). The dominant approach is to pre-train on a large text corpus and then fine-tune on a smaller task-specific dataset (Devlin et al., 2019). Thanks to Transformers' computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters (Brown et al., 2020; Lepikhin et al., 2020). With the models and datasets growing, there is still no sign of saturating performance.

In computer vision, however, convolutional architectures remain dominant (LeCun et al., 1989; Krizhevsky et al., 2012; He et al., 2016). Inspired by NLP successes, multiple works try combining CNN-like architectures with self-attention (Wang et al., 2018; Carion et al., 2020), some replacing the convolutions entirely (Ramachandran et al., 2019; Wang et al., 2020a). The latter models, while theoretically efficient, have not yet been scaled effectively on modern hardware accelerators due to the use of specialized attention patterns. Therefore, in large-scale image recognition, classic ResNet-like architectures are still state of the art (Mahajan et al., 2018; Xie et al., 2020; Kolesnikov et al., 2020).

Inspired by the Transformer scaling successes in NLP, we experiment with applying a standard Transformer directly to images, with the fewest possible modifications. To do so, we split an image into patches and provide the sequence of linear embeddings of these patches as an input to a Transformer. Image patches are treated the same way as tokens (words) in an NLP application. We train the model on image classification in supervised fashion.

When trained on mid-sized datasets such as ImageNet without strong regularization, these models yield modest accuracies of a few percentage points below ResNets of comparable size. This seemingly discouraging outcome may be expected: Transformers lack some of the inductive biases inherent to CNNs, such as translation equivariance and locality, and therefore do not generalize well when trained on insufficient amounts of data.

However, the picture changes if the models are trained on larger datasets (14M-300M images). We find that large scale training trumps inductive bias. Our Vision Transformer (ViT) attains excellent results when pre-trained at sufficient scale and transferred to tasks with fewer datapoints. When pre-trained on the public ImageNet-21k dataset or the in-house JFT-300M dataset, ViT approaches or beats state of the art on multiple image recognition benchmarks. In particular, the best model reaches the accuracy of 88.55% on ImageNet, 90.72% on ImageNet-ReaL, 94.55% on CIFAR-100, and 77.63% on the VTAB suite of 19 tasks.

---

### النسخة العربية

أصبحت المعماريات القائمة على الانتباه الذاتي، وخاصة المحولات (Vaswani et al., 2017)، النموذج المفضل في معالجة اللغة الطبيعية. يتمثل النهج السائد في التدريب المسبق على مجموعة نصية كبيرة ثم الضبط الدقيق على مجموعة بيانات أصغر خاصة بمهمة معينة (Devlin et al., 2019). بفضل الكفاءة الحسابية والقابلية للتوسع للمحولات، أصبح من الممكن تدريب نماذج بحجم غير مسبوق، تحتوي على أكثر من 100 مليار معامل (Brown et al., 2020; Lepikhin et al., 2020). ومع نمو النماذج ومجموعات البيانات، لا تزال لا توجد علامات على تشبع الأداء.

في الرؤية الحاسوبية، مع ذلك، تظل المعماريات الالتفافية هي المهيمنة (LeCun et al., 1989; Krizhevsky et al., 2012; He et al., 2016). مستوحاة من نجاحات معالجة اللغة الطبيعية، تحاول أعمال متعددة دمج معماريات شبيهة بالشبكات العصبية الالتفافية مع الانتباه الذاتي (Wang et al., 2018; Carion et al., 2020)، بينما يستبدل بعضها الالتفافات بالكامل (Ramachandran et al., 2019; Wang et al., 2020a). هذه النماذج الأخيرة، رغم كفاءتها النظرية، لم يتم توسيع نطاقها بفعالية بعد على مسرعات الأجهزة الحديثة بسبب استخدام أنماط انتباه متخصصة. لذلك، في التعرف على الصور واسع النطاق، لا تزال المعماريات الكلاسيكية الشبيهة بـ ResNet هي الأحدث والأفضل (Mahajan et al., 2018; Xie et al., 2020; Kolesnikov et al., 2020).

مستوحين من نجاحات توسيع نطاق المحولات في معالجة اللغة الطبيعية، نجرب تطبيق محول قياسي مباشرة على الصور، مع أقل التعديلات الممكنة. للقيام بذلك، نقسم الصورة إلى رقع ونوفر تسلسل التضمينات الخطية لهذه الرقع كمدخل للمحول. تُعامل رقع الصور بنفس الطريقة التي تُعامل بها الرموز (الكلمات) في تطبيق معالجة اللغة الطبيعية. نقوم بتدريب النموذج على تصنيف الصور بطريقة خاضعة للإشراف.

عند التدريب على مجموعات بيانات متوسطة الحجم مثل ImageNet دون تنظيم قوي، تحقق هذه النماذج دقة متواضعة أقل بعدة نقاط مئوية من شبكات ResNet ذات الحجم المماثل. قد تكون هذه النتيجة المحبطة ظاهرياً متوقعة: تفتقر المحولات إلى بعض الانحيازات الاستقرائية المتأصلة في الشبكات العصبية الالتفافية، مثل ثبات الإزاحة والمحلية، وبالتالي لا تعمم بشكل جيد عند التدريب على كميات غير كافية من البيانات.

ومع ذلك، تتغير الصورة إذا تم تدريب النماذج على مجموعات بيانات أكبر (14 مليون - 300 مليون صورة). نجد أن التدريب واسع النطاق يتفوق على الانحياز الاستقرائي. يحقق محول الرؤية الخاص بنا (ViT) نتائج ممتازة عند التدريب المسبق على نطاق كافٍ ونقله إلى مهام تحتوي على نقاط بيانات أقل. عند التدريب المسبق على مجموعة بيانات ImageNet-21k العامة أو مجموعة بيانات JFT-300M الداخلية، يقترب ViT من أو يتفوق على الأحدث والأفضل في معايير متعددة للتعرف على الصور. على وجه الخصوص، يحقق أفضل نموذج دقة 88.55% على ImageNet، و90.72% على ImageNet-ReaL، و94.55% على CIFAR-100، و77.63% على مجموعة VTAB المكونة من 19 مهمة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** Vision Transformer (ViT), image patches (رقع الصور), inductive bias (الانحياز الاستقرائي), translation equivariance (ثبات الإزاحة), linear embeddings (التضمينات الخطية)
- **Equations:** 0
- **Citations:** 15 references cited
- **Special handling:** Preserved all numerical accuracy metrics and dataset names

### Back-Translation (First and Last Paragraphs)

**First paragraph back-translation:**
"Self-attention-based architectures, especially Transformers, have become the preferred model in natural language processing. The prevailing approach consists of pre-training on a large text corpus and then fine-tuning on a smaller dataset specific to a particular task. Thanks to the computational efficiency and scalability of Transformers, it has become possible to train models of unprecedented size, containing over 100 billion parameters. With the growth of models and datasets, there are still no signs of performance saturation."

**Last paragraph back-translation:**
"However, the picture changes if models are trained on larger datasets (14M-300M images). We find that large-scale training surpasses inductive bias. Our Vision Transformer (ViT) achieves excellent results when pre-trained at sufficient scale and transferred to tasks containing fewer data points. When pre-trained on the public ImageNet-21k dataset or the internal JFT-300M dataset, ViT approaches or exceeds the state-of-the-art in multiple image recognition benchmarks. Specifically, the best model achieves an accuracy of 88.55% on ImageNet, 90.72% on ImageNet-ReaL, 94.55% on CIFAR-100, and 77.63% on the VTAB suite consisting of 19 tasks."

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
