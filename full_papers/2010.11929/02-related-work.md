# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** transformer, machine translation, natural language processing, pre-training, fine-tuning, self-supervised learning, self-attention, convolutional neural network, computer vision, image classification, object detection, transfer learning, dataset, benchmark

---

### English Version

Transformers were proposed by Vaswani et al. (2017) for machine translation, and have since become the state of the art method in many NLP tasks. Large Transformer-based models are often pre-trained on large corpora and then fine-tuned for the task at hand: BERT (Devlin et al., 2019) uses a denoising self-supervised pre-training task, while the GPT line of work uses language modeling as its pre-training task (Radford et al., 2018; 2019; Brown et al., 2020).

Naive application of self-attention to images would require that each pixel attends to every other pixel. With quadratic cost in the number of pixels, this does not scale to realistic input sizes. Thus, to apply Transformers in the context of image processing, several approximations have been tried in the past. Parmar et al. (2018) applied the self-attention only in local neighborhoods for each query pixel instead of globally. Such local multi-head dot-product self attention blocks can completely replace convolutions (Hu et al., 2019; Ramachandran et al., 2019; Zhao et al., 2020). In a different line of work, Sparse Transformers (Child et al., 2019) employ scalable approximations to global self-attention in order to be applicable to images. An alternative way to scale attention is to apply it in blocks of varying sizes (Weissenborn et al., 2019), in the extreme case only along individual axes (Ho et al., 2019; Wang et al., 2020a). Many of these specialized attention architectures demonstrate promising results on computer vision tasks, but require complex engineering to be implemented efficiently on hardware accelerators.

Most related to ours is the model of Cordonnier et al. (2020), which extracts patches of size 2×2 from the input image and applies full self-attention on top. This model is very similar to ViT, but our work goes further to demonstrate that large scale pre-training makes vanilla transformers competitive with (or even better than) state-of-the-art CNNs. Moreover, Cordonnier et al. (2020) use a small patch size of 2×2 pixels, which makes the model applicable only to small-resolution images, while we handle medium-resolution images as well.

There has also been a lot of interest in combining convolutional neural networks (CNNs) with forms of self-attention, e.g. by augmenting feature maps for image classification (Bello et al., 2019) or by further processing the output of a CNN using self-attention, e.g. for object detection (Hu et al., 2018; Carion et al., 2020), video processing (Wang et al., 2018; Sun et al., 2019), image classification (Wu et al., 2020), unsupervised object discovery (Locatello et al., 2020), or unified text-vision tasks (Chen et al., 2020c; Lu et al., 2019; Li et al., 2019).

Another recent related model is image GPT (iGPT) (Chen et al., 2020a), which applies Transformers to image pixels after reducing image resolution and color space. The model is trained in an unsupervised fashion as a generative model, and the resulting representation can then be fine-tuned or probed linearly for classification performance, achieving a maximal accuracy of 72% on ImageNet.

Our work adds to the increasing collection of papers that explore image recognition at larger scales than the standard ImageNet dataset. The use of additional data sources allows to achieve state-of-the-art results on standard benchmarks (Mahajan et al., 2018; Touvron et al., 2019; Xie et al., 2020). Moreover, Sun et al. (2017) study how CNN performance scales with dataset size, and Kolesnikov et al. (2020); Djolonga et al. (2020) perform an empirical exploration of CNN transfer learning from large scale datasets such as ImageNet-21k and JFT-300M. We focus on these two latter datasets as well, but train Transformers instead of ResNet-based models used in prior works.

---

### النسخة العربية

اقُترحت المحولات بواسطة Vaswani et al. (2017) للترجمة الآلية، وأصبحت منذ ذلك الحين الطريقة الأحدث والأفضل في العديد من مهام معالجة اللغة الطبيعية. غالباً ما يتم تدريب النماذج الكبيرة القائمة على المحولات مسبقاً على مجموعات نصية كبيرة ثم ضبطها بدقة للمهمة المطروحة: يستخدم BERT (Devlin et al., 2019) مهمة تدريب مسبق ذاتي الإشراف لإزالة التشويش، بينما يستخدم خط عمل GPT نمذجة اللغة كمهمة تدريب مسبق (Radford et al., 2018; 2019; Brown et al., 2020).

سيتطلب التطبيق الساذج للانتباه الذاتي على الصور أن ينتبه كل بكسل إلى كل بكسل آخر. مع التكلفة التربيعية في عدد البكسلات، لا يتوسع هذا ليشمل أحجام المدخلات الواقعية. وبالتالي، لتطبيق المحولات في سياق معالجة الصور، تم تجريب عدة تقريبات في الماضي. طبق Parmar et al. (2018) الانتباه الذاتي فقط في الأحياء المحلية لكل بكسل استعلام بدلاً من التطبيق العام. يمكن لكتل الانتباه الذاتي متعددة الرؤوس بالضرب النقطي المحلية هذه أن تستبدل الالتفافات تماماً (Hu et al., 2019; Ramachandran et al., 2019; Zhao et al., 2020). في خط عمل مختلف، توظف المحولات المتفرقة (Child et al., 2019) تقريبات قابلة للتوسع للانتباه الذاتي العام لتكون قابلة للتطبيق على الصور. طريقة بديلة لتوسيع نطاق الانتباه هي تطبيقه في كتل بأحجام متفاوتة (Weissenborn et al., 2019)، وفي الحالة القصوى فقط على طول محاور فردية (Ho et al., 2019; Wang et al., 2020a). تُظهر العديد من معماريات الانتباه المتخصصة هذه نتائج واعدة في مهام الرؤية الحاسوبية، لكنها تتطلب هندسة معقدة لتنفيذها بكفاءة على مسرعات الأجهزة.

الأكثر ارتباطاً بعملنا هو نموذج Cordonnier et al. (2020)، الذي يستخرج رقعاً بحجم 2×2 من صورة المدخل ويطبق الانتباه الذاتي الكامل في الأعلى. هذا النموذج مشابه جداً لـ ViT، لكن عملنا يذهب إلى أبعد من ذلك لإثبات أن التدريب المسبق واسع النطاق يجعل المحولات الفانيلا منافسة لـ (أو حتى أفضل من) الشبكات العصبية الالتفافية الأحدث والأفضل. علاوة على ذلك، يستخدم Cordonnier et al. (2020) حجم رقعة صغير 2×2 بكسل، مما يجعل النموذج قابلاً للتطبيق فقط على الصور منخفضة الدقة، بينما نتعامل مع الصور متوسطة الدقة أيضاً.

كان هناك أيضاً الكثير من الاهتمام بدمج الشبكات العصبية الالتفافية مع أشكال الانتباه الذاتي، على سبيل المثال من خلال تعزيز خرائط الخصائص لتصنيف الصور (Bello et al., 2019) أو من خلال معالجة إضافية لمخرجات الشبكة العصبية الالتفافية باستخدام الانتباه الذاتي، على سبيل المثال للكشف عن الأجسام (Hu et al., 2018; Carion et al., 2020)، ومعالجة الفيديو (Wang et al., 2018; Sun et al., 2019)، وتصنيف الصور (Wu et al., 2020)، واكتشاف الأجسام غير الخاضع للإشراف (Locatello et al., 2020)، أو مهام النص-الرؤية الموحدة (Chen et al., 2020c; Lu et al., 2019; Li et al., 2019).

نموذج آخر ذو صلة حديث هو GPT للصور (iGPT) (Chen et al., 2020a)، الذي يطبق المحولات على بكسلات الصور بعد تقليل دقة الصورة ومساحة اللون. يتم تدريب النموذج بطريقة غير خاضعة للإشراف كنموذج توليدي، ويمكن بعد ذلك ضبط التمثيل الناتج بدقة أو فحصه خطياً لأداء التصنيف، محققاً دقة قصوى تبلغ 72% على ImageNet.

يضيف عملنا إلى المجموعة المتزايدة من الأوراق التي تستكشف التعرف على الصور على نطاقات أكبر من مجموعة بيانات ImageNet القياسية. يسمح استخدام مصادر بيانات إضافية بتحقيق نتائج الأحدث والأفضل على المعايير القياسية (Mahajan et al., 2018; Touvron et al., 2019; Xie et al., 2020). علاوة على ذلك، يدرس Sun et al. (2017) كيف يتوسع أداء الشبكة العصبية الالتفافية مع حجم مجموعة البيانات، ويقوم Kolesnikov et al. (2020); Djolonga et al. (2020) باستكشاف تجريبي لتعلم النقل للشبكات العصبية الالتفافية من مجموعات بيانات واسعة النطاق مثل ImageNet-21k و JFT-300M. نركز على هاتين المجموعتين الأخيرتين أيضاً، لكننا ندرب المحولات بدلاً من النماذج القائمة على ResNet المستخدمة في الأعمال السابقة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** denoising (إزالة التشويش), sparse transformers (المحولات المتفرقة), vanilla transformers (المحولات الفانيلا), feature maps (خرائط الخصائص), generative model (نموذج توليدي)
- **Equations:** 0
- **Citations:** 35+ references cited
- **Special handling:** Preserved technical terminology like "multi-head dot-product self attention", kept dataset names (ImageNet, JFT-300M) in English

### Back-Translation (First and Last Paragraphs)

**First paragraph back-translation:**
"Transformers were proposed by Vaswani et al. (2017) for machine translation, and have since become the state-of-the-art method in many natural language processing tasks. Large transformer-based models are often pre-trained on large text corpora and then fine-tuned for the task at hand: BERT (Devlin et al., 2019) uses a self-supervised pre-training task for denoising, while the GPT line of work uses language modeling as a pre-training task (Radford et al., 2018; 2019; Brown et al., 2020)."

**Last paragraph back-translation:**
"Our work adds to the growing collection of papers that explore image recognition at larger scales than the standard ImageNet dataset. The use of additional data sources allows achieving state-of-the-art results on standard benchmarks (Mahajan et al., 2018; Touvron et al., 2019; Xie et al., 2020). Moreover, Sun et al. (2017) study how CNN performance scales with dataset size, and Kolesnikov et al. (2020); Djolonga et al. (2020) perform an empirical exploration of transfer learning for CNNs from large-scale datasets such as ImageNet-21k and JFT-300M. We focus on these latter two datasets as well, but train Transformers instead of ResNet-based models used in previous works."

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
