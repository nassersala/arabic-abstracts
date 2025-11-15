# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep networks, convolutional network, segmentation, training, architecture, localization, annotation, data augmentation, GPU

---

### English Version

In the last two years, deep convolutional networks have outperformed the state of the art in many visual recognition tasks, e.g. [1,7]. While convolutional networks have already existed for a long time [8], their success was limited due to the size of the available training sets and the size of the considered networks. The breakthrough by Krizhevsky et al. [7] was due to supervised training of a large network with 8 layers and millions of parameters on the ImageNet dataset with 1 million training images. Since then, even larger and deeper networks have been trained [12].

The typical use of convolutional networks is on classification tasks, where the output to an image is a single class label. However, in many visual tasks, especially in biomedical image processing, the desired output should include localization, i.e., a class label is supposed to be assigned to each pixel. Moreover, thousands of training images are usually beyond reach in biomedical tasks. Hence, Ciresan et al. [2] trained a network in a sliding-window setup to predict the class label of each pixel by providing a local region (patch) around that pixel as input. First, this network can localize. Secondly, the training data in terms of patches is much larger than the number of training images. The resulting network won the EM segmentation challenge at ISBI 2012 by a large margin.

Obviously, the strategy in Ciresan et al. [2] has two drawbacks. First, it is quite slow because the network must be run separately for each patch, and there is a lot of redundancy due to overlapping patches. Secondly, there is a trade-off between localization accuracy and the use of context. Larger patches require more max-pooling layers that reduce the localization accuracy, while small patches allow the network to see only little context. More recent approaches [10,3] proposed a classifier output that takes into account the features from multiple layers. Good localization and the use of context are possible at the same time.

In this paper, we build upon a more elegant architecture, the so-called "fully convolutional network" [9]. We modify and extend this architecture such that it works with very few training images and yields more precise segmentations. The main idea in [9] is to supplement a usual contracting network by successive layers, where pooling operators are replaced by upsampling operators. Hence, these layers increase the resolution of the output. In order to localize, high resolution features from the contracting path are combined with the upsampled output. A successive convolution layer can then learn to assemble a more precise output based on this information.

One important modification in our architecture is that in the upsampling part we have also a large number of feature channels, which allow the network to propagate context information to higher resolution layers. As a consequence, the expansive path is more or less symmetric to the contracting path, and yields a u-shaped architecture. The network does not have any fully connected layers and only uses the valid part of each convolution, i.e., the segmentation map only contains the pixels, for which the full context is available in the input image. This strategy allows the seamless segmentation of arbitrarily large images by an overlap-tile strategy (see Figure 2). To predict the pixels in the border region of the image, the missing context is extrapolated by mirroring the input image. This tiling strategy is important to apply the network to large images, since otherwise the resolution would be limited by the GPU memory.

As for our tasks there is very little training data available, we use excessive data augmentation by applying elastic deformations to the available training images. This allows the network to learn invariance to such deformations, without the need to see these transformations in the annotated image corpus. This is particularly important in biomedical segmentation, since deformation used to be the most common variation in tissue and realistic deformations can be simulated efficiently. The value of data augmentation for learning invariance has been shown in Dosovitskiy et al. [4] in the scope of unsupervised feature learning.

Another challenge in many cell segmentation tasks is the separation of touching objects of the same class; see Figure 3. To this end, we propose the use of a weighted loss, where the separating background labels between touching cells obtain a large weight in the loss function.

The resulting network is applicable to various biomedical segmentation problems. In this paper, we show results on the segmentation of neuronal structures in EM stacks (an ongoing competition started at ISBI 2012), where we outperformed the network of Ciresan et al. [2], the winner of the ISBI 2012 challenge. Furthermore, we show results for cell segmentation in light microscopy images from the ISBI cell tracking challenge 2015. Here we won with a large margin on the two most challenging 2D transmitted light datasets.

---

### النسخة العربية

في السنتين الأخيرتين، تفوقت الشبكات الالتفافية العميقة على أحدث ما توصلت إليه التقنية في العديد من مهام التعرف البصري، على سبيل المثال [1,7]. بينما كانت الشبكات الالتفافية موجودة بالفعل منذ وقت طويل [8]، كان نجاحها محدوداً بسبب حجم مجموعات التدريب المتاحة وحجم الشبكات المعنية. كان الاختراق الذي حققه Krizhevsky وآخرون [7] بسبب التدريب الموجه لشبكة كبيرة تحتوي على 8 طبقات وملايين المعاملات على مجموعة بيانات ImageNet التي تضم مليون صورة تدريب. منذ ذلك الحين، تم تدريب شبكات أكبر وأعمق [12].

الاستخدام النموذجي للشبكات الالتفافية هو في مهام التصنيف، حيث يكون الناتج لصورة ما هو تسمية صنف واحدة. ومع ذلك، في العديد من المهام البصرية، وخاصة في معالجة الصور الطبية الحيوية، يجب أن يتضمن الناتج المطلوب التحديد الموضعي، أي يُفترض تعيين تسمية صنف لكل بكسل. علاوة على ذلك، فإن آلاف صور التدريب عادة ما تكون بعيدة المنال في المهام الطبية الحيوية. لذلك، قام Ciresan وآخرون [2] بتدريب شبكة في إعداد نافذة منزلقة للتنبؤ بتسمية صنف كل بكسل من خلال توفير منطقة محلية (رقعة) حول ذلك البكسل كمدخل. أولاً، يمكن لهذه الشبكة التحديد الموضعي. ثانياً، بيانات التدريب من حيث الرقع أكبر بكثير من عدد صور التدريب. فازت الشبكة الناتجة بتحدي تجزئة المجهر الإلكتروني في ISBI 2012 بهامش كبير.

من الواضح أن الاستراتيجية في Ciresan وآخرون [2] لديها عيبان. أولاً، إنها بطيئة جداً لأنه يجب تشغيل الشبكة بشكل منفصل لكل رقعة، وهناك الكثير من التكرار بسبب تداخل الرقع. ثانياً، هناك مفاضلة بين دقة التحديد الموضعي واستخدام السياق. تتطلب الرقع الأكبر المزيد من طبقات التجميع الأعظمي التي تقلل من دقة التحديد الموضعي، بينما تسمح الرقع الصغيرة للشبكة برؤية القليل فقط من السياق. اقترحت الأساليب الأحدث [10,3] ناتج مصنف يأخذ في الاعتبار الميزات من طبقات متعددة. يمكن التحديد الموضعي الجيد واستخدام السياق في نفس الوقت.

في هذه الورقة، نبني على معمارية أكثر أناقة، ما يسمى بـ "الشبكة الالتفافية الكاملة" [9]. نقوم بتعديل وتوسيع هذه المعمارية بحيث تعمل مع عدد قليل جداً من صور التدريب وتنتج تجزئة أكثر دقة. الفكرة الرئيسية في [9] هي استكمال شبكة انقباضية عادية بطبقات متتالية، حيث يتم استبدال عوامل التجميع بعوامل زيادة العينات. وبالتالي، تزيد هذه الطبقات من دقة الناتج. من أجل التحديد الموضعي، يتم دمج الميزات عالية الدقة من المسار الانقباضي مع الناتج المزاد عيناته. يمكن لطبقة التفاف متتالية بعد ذلك أن تتعلم تجميع ناتج أكثر دقة بناءً على هذه المعلومات.

أحد التعديلات الهامة في معماريتنا هو أنه في جزء زيادة العينات لدينا أيضاً عدد كبير من قنوات الميزات، والتي تسمح للشبكة بنشر معلومات السياق إلى طبقات ذات دقة أعلى. ونتيجة لذلك، فإن المسار التوسعي متماثل إلى حد كبير مع المسار الانقباضي، ويعطي معمارية على شكل حرف U. لا تحتوي الشبكة على أي طبقات متصلة بالكامل وتستخدم فقط الجزء الصالح من كل التفاف، أي أن خريطة التجزئة تحتوي فقط على البكسلات التي يكون السياق الكامل لها متاحاً في الصورة المدخلة. تسمح هذه الاستراتيجية بالتجزئة السلسة للصور الكبيرة تعسفياً بواسطة استراتيجية بلاط متداخل (انظر الشكل 2). للتنبؤ بالبكسلات في المنطقة الحدودية للصورة، يتم استقراء السياق المفقود عن طريق عكس الصورة المدخلة. هذه الاستراتيجية مهمة لتطبيق الشبكة على الصور الكبيرة، حيث أن الدقة ستكون محدودة بخلاف ذلك بذاكرة وحدة معالجة الرسومات.

نظراً لأن مهامنا تحتوي على القليل جداً من بيانات التدريب المتاحة، نستخدم زيادة البيانات المفرطة من خلال تطبيق التشوهات المرنة على صور التدريب المتاحة. يسمح هذا للشبكة بتعلم الثبات أمام مثل هذه التشوهات، دون الحاجة إلى رؤية هذه التحويلات في مجموعة الصور الموسومة. هذا مهم بشكل خاص في التجزئة الطبية الحيوية، حيث كان التشوه هو الاختلاف الأكثر شيوعاً في الأنسجة ويمكن محاكاة التشوهات الواقعية بكفاءة. تم عرض قيمة زيادة البيانات لتعلم الثبات في Dosovitskiy وآخرون [4] في نطاق تعلم الميزات غير الموجه.

تحدٍ آخر في العديد من مهام تجزئة الخلايا هو فصل الكائنات المتلامسة من نفس الصنف؛ انظر الشكل 3. لهذه الغاية، نقترح استخدام خسارة موزونة، حيث تحصل تسميات الخلفية الفاصلة بين الخلايا المتلامسة على وزن كبير في دالة الخسارة.

الشبكة الناتجة قابلة للتطبيق على مشاكل التجزئة الطبية الحيوية المختلفة. في هذه الورقة، نعرض نتائج حول تجزئة البنى العصبية في حزم المجهر الإلكتروني (مسابقة مستمرة بدأت في ISBI 2012)، حيث تفوقنا على شبكة Ciresan وآخرون [2]، الفائز بتحدي ISBI 2012. علاوة على ذلك، نعرض نتائج لتجزئة الخلايا في صور المجهر الضوئي من تحدي تتبع الخلايا ISBI 2015. هنا فزنا بهامش كبير في مجموعتي البيانات الأكثر تحدياً للضوء المنقول ثنائي الأبعاد.

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 3
- **Key terms introduced:** fully convolutional network, contracting path, expansive path, overlap-tile strategy, elastic deformations, weighted loss
- **Equations:** None in introduction
- **Citations:** [1], [2], [3], [4], [7], [8], [9], [10], [12]
- **Special handling:** Preserved author names (Krizhevsky, Ciresan, Dosovitskiy), dataset names (ImageNet, ISBI), and technical terms

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
