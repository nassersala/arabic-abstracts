# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** deep learning, convolutional networks, neural network, supervised training, classification, localization, biomedical, segmentation, training images, sliding-window, patch, data augmentation, elastic deformations, architecture, fully convolutional network, upsampling, feature channels, GPU memory

---

### English Version

In the last two years, deep convolutional networks have outperformed the state of the art in many visual recognition tasks, e.g. [Krizhevsky, R-CNN]. While convolutional networks have already existed for a long time [LeCun_NC1989], their success was limited due to the size of the available training sets and the size of the considered networks. The breakthrough by Krizhevsky et al. [Krizhevsky] was due to supervised training of a large network with 8 layers and millions of parameters on the ImageNet dataset with 1 million training images. Since then, even larger and deeper networks have been trained [VGG].

The typical use of convolutional networks is on classification tasks, where the output to an image is a single class label. However, in many visual tasks, especially in biomedical image processing, the desired output should include localization, i.e., a class label is supposed to be assigned to each pixel. Moreover, thousands of training images are usually beyond reach in biomedical tasks. Hence, Ciresan et al. [schmidhuber12deepneural] trained a network in a sliding-window setup to predict the class label of each pixel by providing a local region (patch) around that pixel as input. First, this network can localize. Secondly, the training data in terms of patches is much larger than the number of training images. The resulting network won the EM segmentation challenge at ISBI 2012 by a large margin.

Obviously, the strategy in Ciresan et al. [schmidhuber12deepneural] has two drawbacks. First, it is quite slow because the network must be run separately for each patch, and there is a lot of redundancy due to overlapping patches. Secondly, there is a trade-off between localization accuracy and the use of context. Larger patches require more max-pooling layers that reduce the localization accuracy, while small patches allow the network to see only little context. More recent approaches [Seyedhosseini2013, hypercolumns] proposed a classifier output that takes into account the features from multiple layers. Good localization and the use of context are possible at the same time.

In this paper, we build upon a more elegant architecture, the so-called "fully convolutional network" [fullyconv]. We modify and extend this architecture such that it works with very few training images and yields more precise segmentations; see Figure 1. The main idea in [fullyconv] is to supplement a usual contracting network by successive layers, where pooling operators are replaced by upsampling operators. Hence, these layers increase the resolution of the output. In order to localize, high resolution features from the contracting path are combined with the upsampled output. A successive convolution layer can then learn to assemble a more precise output based on this information.

One important modification in our architecture is that in the upsampling part we have also a large number of feature channels, which allow the network to propagate context information to higher resolution layers. As a consequence, the expansive path is more or less symmetric to the contracting path, and yields a u-shaped architecture. The network does not have any fully connected layers and only uses the valid part of each convolution, i.e., the segmentation map only contains the pixels, for which the full context is available in the input image. This strategy allows the seamless segmentation of arbitrarily large images by an overlap-tile strategy (see Figure 2). To predict the pixels in the border region of the image, the missing context is extrapolated by mirroring the input image. This tiling strategy is important to apply the network to large images, since otherwise the resolution would be limited by the GPU memory.

As for our tasks there is very little training data available, we use excessive data augmentation by applying elastic deformations to the available training images. This allows the network to learn invariance to such deformations, without the need to see these transformations in the annotated image corpus. This is particularly important in biomedical segmentation, since deformation used to be the most common variation in tissue and realistic deformations can be simulated efficiently. The value of data augmentation for learning invariance has been shown in Dosovitskiy et al. [unsupervised] in the scope of unsupervised feature learning.

Another challenge in many cell segmentation tasks is the separation of touching objects of the same class; see Figure 3. To this end, we propose the use of a weighted loss, where the separating background labels between touching cells obtain a large weight in the loss function.

The resulting network is applicable to various biomedical segmentation problems. In this paper, we show results on the segmentation of neuronal structures in EM stacks (an ongoing competition started at ISBI 2012), where we outperformed the network of Ciresan et al. [schmidhuber12deepneural]. Furthermore, we show results for cell segmentation in light microscopy images from the ISBI cell tracking challenge 2015. Here we won with a large margin on the two most challenging 2D transmitted light datasets.

---

### النسخة العربية

في العامين الماضيين، تفوقت الشبكات الالتفافية العميقة على أحدث ما توصل إليه العلم في العديد من مهام التعرف البصري، على سبيل المثال [Krizhevsky, R-CNN]. وبينما كانت الشبكات الالتفافية موجودة منذ وقت طويل [LeCun_NC1989]، كان نجاحها محدوداً بسبب حجم مجموعات التدريب المتاحة وحجم الشبكات المُعتبرة. كان الإنجاز الذي حققه Krizhevsky وزملاؤه [Krizhevsky] بسبب التدريب الموجه لشبكة كبيرة ذات 8 طبقات وملايين المعاملات على مجموعة بيانات ImageNet التي تحتوي على مليون صورة تدريب. منذ ذلك الحين، تم تدريب شبكات أكبر وأعمق [VGG].

الاستخدام النموذجي للشبكات الالتفافية هو في مهام التصنيف، حيث يكون الناتج لصورة ما هو تصنيف واحد. ومع ذلك، في العديد من المهام البصرية، وخاصة في معالجة الصور الطبية الحيوية، يجب أن يتضمن الناتج المطلوب التوطين، أي يُفترض تعيين تصنيف لكل بكسل. علاوة على ذلك، فإن الآلاف من صور التدريب عادة ما تكون بعيدة المنال في المهام الطبية الحيوية. لذلك، قام Ciresan وزملاؤه [schmidhuber12deepneural] بتدريب شبكة في إعداد نافذة منزلقة للتنبؤ بتصنيف كل بكسل من خلال توفير منطقة محلية (رقعة) حول ذلك البكسل كمدخل. أولاً، يمكن لهذه الشبكة التوطين. ثانياً، بيانات التدريب من حيث الرقع أكبر بكثير من عدد صور التدريب. فازت الشبكة الناتجة بتحدي تجزئة المجهر الإلكتروني في ISBI 2012 بفارق كبير.

من الواضح أن الاستراتيجية في Ciresan وزملائه [schmidhuber12deepneural] لها عيبان. أولاً، إنها بطيئة جداً لأن الشبكة يجب أن تُشغَّل بشكل منفصل لكل رقعة، وهناك الكثير من التكرار بسبب الرقع المتداخلة. ثانياً، هناك مفاضلة بين دقة التوطين واستخدام السياق. تتطلب الرقع الأكبر المزيد من طبقات التجميع الأعظمي (max-pooling) التي تقلل من دقة التوطين، بينما تسمح الرقع الصغيرة للشبكة برؤية سياق قليل فقط. اقترحت الطرق الحديثة [Seyedhosseini2013, hypercolumns] ناتج مصنف يأخذ في الاعتبار الميزات من طبقات متعددة. التوطين الجيد واستخدام السياق ممكنان في نفس الوقت.

في هذا البحث، نبني على معمارية أكثر أناقة، ما يسمى بـ "الشبكة الالتفافية الكاملة" [fullyconv]. نقوم بتعديل وتوسيع هذه المعمارية بحيث تعمل مع عدد قليل جداً من صور التدريب وتنتج تجزئات أكثر دقة؛ انظر الشكل 1. الفكرة الرئيسية في [fullyconv] هي استكمال شبكة الانكماش المعتادة بطبقات متتالية، حيث يتم استبدال عوامل التجميع بعوامل الزيادة الترددية (upsampling). وبالتالي، تزيد هذه الطبقات من دقة وضوح الناتج. من أجل التوطين، يتم دمج ميزات عالية الدقة من مسار الانكماش مع الناتج المُزاد تردديا. يمكن لطبقة التفاف متتالية بعد ذلك أن تتعلم تجميع ناتج أكثر دقة بناءً على هذه المعلومات.

أحد التعديلات المهمة في معماريتنا هو أننا في جزء الزيادة الترددية لدينا أيضاً عدد كبير من قنوات الميزات، والتي تسمح للشبكة بنشر معلومات السياق إلى طبقات ذات دقة وضوح أعلى. ونتيجة لذلك، فإن المسار التوسعي متماثل إلى حد ما مع المسار الانكماشي، وينتج معمارية على شكل حرف U. لا تحتوي الشبكة على أي طبقات متصلة بالكامل وتستخدم فقط الجزء الصالح من كل التفاف، أي أن خريطة التجزئة تحتوي فقط على البكسلات التي يكون السياق الكامل لها متاحاً في الصورة المدخلة. تسمح هذه الاستراتيجية بالتجزئة السلسة لصور كبيرة تعسفياً من خلال استراتيجية البلاط المتداخل (انظر الشكل 2). للتنبؤ بالبكسلات في المنطقة الحدودية للصورة، يتم استقراء السياق المفقود عن طريق عكس الصورة المدخلة. هذه الاستراتيجية المبلطة مهمة لتطبيق الشبكة على الصور الكبيرة، لأن دقة الوضوح ستكون محدودة بذاكرة وحدة معالجة الرسومات بخلاف ذلك.

نظراً لأن هناك القليل جداً من بيانات التدريب المتاحة لمهامنا، فإننا نستخدم زيادة البيانات المفرطة من خلال تطبيق التشوهات المرنة على صور التدريب المتاحة. يتيح ذلك للشبكة تعلم الثبات تجاه هذه التشوهات، دون الحاجة إلى رؤية هذه التحويلات في مدونة الصور الموسومة. هذا مهم بشكل خاص في التجزئة الطبية الحيوية، نظراً لأن التشوه كان الاختلاف الأكثر شيوعاً في الأنسجة ويمكن محاكاة التشوهات الواقعية بكفاءة. تم إثبات قيمة زيادة البيانات لتعلم الثبات في Dosovitskiy وزملائه [unsupervised] في نطاق التعلم غير الموجه للميزات.

التحدي الآخر في العديد من مهام تجزئة الخلايا هو فصل الأجسام المتلامسة من نفس الصنف؛ انظر الشكل 3. لهذه الغاية، نقترح استخدام خسارة موزونة، حيث تحصل تصنيفات الخلفية الفاصلة بين الخلايا المتلامسة على وزن كبير في دالة الخسارة.

الشبكة الناتجة قابلة للتطبيق على مشاكل تجزئة طبية حيوية مختلفة. في هذا البحث، نُظهر النتائج على تجزئة البنى العصبية في مكدسات المجهر الإلكتروني (مسابقة مستمرة بدأت في ISBI 2012)، حيث تفوقنا على شبكة Ciresan وزملائه [schmidhuber12deepneural]. علاوة على ذلك، نُظهر نتائج تجزئة الخلايا في صور المجهر الضوئي من تحدي تتبع الخلايا ISBI 2015. هنا فزنا بفارق كبير على مجموعتي البيانات ثنائية الأبعاد الأكثر تحدياً للضوء المُرسَل.

---

### Translation Notes

- **Figures referenced:**
  - Figure 1: U-net architecture diagram
  - Figure 2: Overlap-tile strategy illustration
  - Figure 3: HeLa cells ground truth segmentation
- **Key terms introduced:**
  - Deep convolutional networks (الشبكات الالتفافية العميقة)
  - Visual recognition tasks (مهام التعرف البصري)
  - Supervised training (التدريب الموجه)
  - Sliding-window setup (إعداد نافذة منزلقة)
  - Patch (رقعة)
  - Max-pooling layers (طبقات التجميع الأعظمي)
  - Fully convolutional network (الشبكة الالتفافية الكاملة)
  - Upsampling operators (عوامل الزيادة الترددية)
  - Feature channels (قنوات الميزات)
  - Fully connected layers (طبقات متصلة بالكامل)
  - Overlap-tile strategy (استراتيجية البلاط المتداخل)
  - Elastic deformations (التشوهات المرنة)
  - Weighted loss (خسارة موزونة)
  - U-shaped architecture (معمارية على شكل حرف U)
  - EM stacks (مكدسات المجهر الإلكتروني)
  - Transmitted light (الضوء المُرسَل)
- **Equations:** None in introduction
- **Citations:** Multiple references preserved in square brackets
  - Krizhevsky, R-CNN, LeCun_NC1989, VGG
  - schmidhuber12deepneural, Seyedhosseini2013, hypercolumns
  - fullyconv, unsupervised
- **Special handling:**
  - Kept author names in English (Krizhevsky, Ciresan, Dosovitskiy)
  - Kept dataset names in English (ImageNet)
  - Kept conference abbreviations (ISBI)
  - Translated technical concepts while preserving citation markers

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Check

First paragraph back-translation:
Arabic → English: "In the past two years, deep convolutional networks have surpassed the state of the art in many visual recognition tasks, for example [Krizhevsky, R-CNN]. While convolutional networks had existed for a long time [LeCun_NC1989], their success was limited due to the size of available training sets and the size of considered networks. The achievement by Krizhevsky et al. [Krizhevsky] was due to supervised training of a large network with 8 layers and millions of parameters on the ImageNet dataset containing one million training images. Since then, larger and deeper networks have been trained [VGG]."

✓ Semantically equivalent with high fidelity to original meaning
